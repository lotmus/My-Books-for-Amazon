"""Kindle link pass: sources and bibliographies as clickable keywords, never as visible URLs.

Lothar's rule (10 Oct 2026): every external source is a hyperlink whose visible text is a title or keyword
(e.g. "NASA Image and Video Library"); the URL is only the link target. Citations that point to a
bibliography entry become internal links to that entry. Kindle-safe: plain <w:hyperlink> elements
(r:id for external targets, w:anchor for bookmarks), never HYPERLINK fields.

Usage, on a finished docx (normally called by kindle_postbuild.py when the spec says "links": "<rules json>"):
    python tools/kindle_links.py <book.docx> <links.json> [--out <new.docx>] [--check]

links.json (paths relative to the json):
  rules      [{"find": "<visible text, as in the docx>", "to": "<new text with [label](url) or [label](#bookmark)>",
              "in": "<optional: only paragraphs containing this>", "max": <optional count>}]
             Text kept from "find" keeps its formatting; added text takes the formatting of its neighbour.
  bookmarks  [{"name": "<bookmark>", "para": "<regex matching the start of the target paragraph>"}]
             added before the rules run, so rules can link to them
  fields     true: HYPERLINK fields (fldChar/instrText or fldSimple) become plain <w:hyperlink> first
  allow      [regex]: visible URL-like text that is fine (brand names such as Amazon.com)
After the rules, every paragraph is scanned again; visible URLs that remain are reported (exit code stays 0).
Nothing is deleted: the caller keeps the old file in bak/.
"""
import zipfile, re, sys, os, json, copy, difflib
from lxml import etree
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
RNS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
HL = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink'
XS = '{http://www.w3.org/XML/1998/namespace}space'
def q(t): return '{%s}%s' % (W, t)
RID = '{%s}id' % RNS
URL_RX = re.compile(r'(?:https?://|www\.)(?:[^\s<>"()\[\]]|\([^\s()]*\))+|\bdoi:\s*10\.\d{4,}/\S+|'
                    r'\b[a-z0-9][a-z0-9-]*(?:\.[a-z0-9-]+)*\.(?:org|com|gov|edu|net|int|io|info|de|uk|mx|eu|ca|au|nz|ch|cern|google|ai|dev|app|co|me|tv|ly|us|fr|jp|in|sh|aq|nl|ru|at|it|es|se|no|dk|fi|be|pl|cz)\b(?:/(?:[^\s<>"()\[\]]|\([^\s()]*\))*)?', re.I)
TRAIL = '.,;:!?\u2019\u201d\'"'
def visible_urls(s, allow=()):
    out = []
    for m in URL_RX.finditer(s):
        u = m.group().rstrip(TRAIL)
        if any(re.fullmatch(a, u, re.I) for a in allow): continue
        if '@' in s[max(0, m.start() - 1):m.start()]: continue  # e-mail addresses
        out.append(u)
    return out

# ---------- relationships ----------
class Rels:
    def __init__(self, data):
        self.data = data; self.name = 'word/_rels/document.xml.rels'
        self.x = etree.fromstring(data[self.name])
    def target(self, rid):
        for r in self.x:
            if r.get('Id') == rid: return r.get('Target')
    def add(self, url):
        for r in self.x:
            if r.get('Type') == HL and r.get('Target') == url and r.get('TargetMode') == 'External': return r.get('Id')
        ids = {r.get('Id') for r in self.x}; n = 1
        while 'rIdL%d' % n in ids: n += 1
        e = etree.SubElement(self.x, '{http://schemas.openxmlformats.org/package/2006/relationships}Relationship')
        e.set('Id', 'rIdL%d' % n); e.set('Type', HL); e.set('Target', url); e.set('TargetMode', 'External'); return 'rIdL%d' % n
    def save(self, used):
        for r in list(self.x):  # drop hyperlink rels nothing points at any more
            if r.get('Type') == HL and r.get('Id') not in used: self.x.remove(r)
        self.data[self.name] = etree.tostring(self.x, xml_declaration=True, encoding='UTF-8', standalone=True)

# ---------- paragraph character model ----------
ZERO = {q('bookmarkStart'), q('bookmarkEnd'), q('proofErr'), q('commentRangeStart'), q('commentRangeEnd'), q('permStart'), q('permEnd')}
def model(p):
    """items: ('c', char, rPr, link) | ('e', run-child element, rPr, link) | ('z', element, link) | ('b', element) ; link = None or (attrib dict)."""
    items = []
    def runs(r, link):
        rpr = r.find(q('rPr'))
        for c in r:
            if c.tag == q('rPr'): continue
            if c.tag == q('t'):
                for ch in (c.text or ''): items.append(('c', ch, rpr, link))
            else: items.append(('e', c, rpr, link))
    for c in p:
        if c.tag == q('pPr'): continue
        if c.tag == q('r'): runs(c, None)
        elif c.tag == q('hyperlink'):
            link = dict(c.attrib)
            for k in c:
                if k.tag == q('r'): runs(k, link)
                elif k.tag in ZERO: items.append(('z', k, link))
                else: items.append(('b', k))
        elif c.tag in ZERO: items.append(('z', c, None))
        else: items.append(('b', c))
    return items
def mtext(items):
    return ''.join(i[1] if i[0] == 'c' else ('\uFFFC' if i[0] in ('e', 'b') else '') for i in items)
def textpos(items):
    """index in items for each char of mtext"""
    return [k for k, i in enumerate(items) if i[0] in ('c', 'e', 'b')]
def ptext(p): return mtext(model(p))

def link_rpr(rpr):
    r = copy.deepcopy(rpr) if rpr is not None else etree.Element(q('rPr'))
    for t in ('color', 'u'):
        for e in r.findall(q(t)): r.remove(e)
    # schema order: ... color(after b,i,caps..,strike..) ... sz ... u ...; inserting at the end is accepted by Word/LibreOffice/Kindle
    c = etree.SubElement(r, q('color')); c.set(q('val'), '0563C1')
    u = etree.SubElement(r, q('u')); u.set(q('val'), 'single')
    order = ['rStyle', 'rFonts', 'b', 'bCs', 'i', 'iCs', 'caps', 'smallCaps', 'strike', 'dstrike', 'outline', 'shadow', 'emboss', 'imprint',
             'noProof', 'snapToGrid', 'vanish', 'webHidden', 'color', 'spacing', 'w', 'kern', 'position', 'sz', 'szCs', 'highlight', 'u',
             'effect', 'bdr', 'shd', 'fitText', 'vertAlign', 'rtl', 'cs', 'em', 'lang', 'eastAsianLayout', 'specVanish', 'oMath']
    kids = sorted(list(r), key=lambda e: order.index(etree.QName(e).localname) if etree.QName(e).localname in order else 99)
    for k in kids: r.remove(k)
    for k in kids: r.append(k)
    return r
def unlink_rpr(rpr):
    if rpr is None: return None
    r = copy.deepcopy(rpr)
    for e in r.findall(q('color')):
        if e.get(q('val'), '').upper() in ('0563C1', '0000FF', '0000EE', '1155CC'): r.remove(e)
    for e in r.findall(q('u')): r.remove(e)
    for e in r.findall(q('rStyle')):
        if e.get(q('val')) == 'Hyperlink': r.remove(e)
    return r
def key(rpr): return etree.tostring(rpr, method='c14n') if rpr is not None else b''

def rebuild(p, items):
    for c in [c for c in p if c.tag != q('pPr')]: p.remove(c)
    cur_link = None; cur_h = None; cur_run = None; cur_key = None
    def container(link):
        nonlocal cur_link, cur_h, cur_run
        if link is None:
            cur_h = None; cur_link = None; return p
        if cur_h is None or cur_link is not link:
            cur_h = etree.SubElement(p, q('hyperlink'))
            for k, v in link.items(): cur_h.set(k, v)
            cur_link = link; cur_run = None
        return cur_h
    for it in items:
        kind = it[0]
        if kind == 'b':
            cur_h = None; cur_link = None; cur_run = None; p.append(it[1]); continue
        link = it[-1] if kind != 'b' else None
        if kind == 'z':
            par = container(link) if link is not None else (cur_h if cur_h is not None else p)
            par.append(it[1]); continue
        rpr = it[2]; k = key(rpr)
        par = container(link)
        if cur_run is None or cur_run.getparent() is not par or cur_key != k or par[-1] is not cur_run:
            cur_run = etree.SubElement(par, q('r')); cur_key = k
            if rpr is not None: cur_run.append(copy.deepcopy(rpr))
        if kind == 'c':
            last = cur_run[-1] if len(cur_run) else None
            if last is not None and last.tag == q('t'): last.text += it[1]
            else:
                t = etree.SubElement(cur_run, q('t')); t.text = it[1]
        else: cur_run.append(it[1])
    for t in p.iter(q('t')):
        if t.text and (t.text[0] == ' ' or t.text[-1] == ' ' or '  ' in t.text): t.set(XS, 'preserve')

MD = re.compile(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)')
def parse_to(to):
    plain = []; links = []; pos = 0; n = 0
    for m in MD.finditer(to):
        plain.append(to[pos:m.start()]); n += len(to[pos:m.start()])
        links.append((n, n + len(m.group(1)), m.group(2))); plain.append(m.group(1)); n += len(m.group(1)); pos = m.end()
    plain.append(to[pos:]); return ''.join(plain), links

def apply_rule(p, find, to, rels):
    items = model(p); txt = mtext(items); a = txt.find(find)
    if a < 0: return 0
    pos = textpos(items); b = a + len(find)
    span_items = items[pos[a]:pos[b - 1] + 1]
    if any(i[0] == 'b' for i in span_items): return -1
    # zero-width items inside the span stay (bookmarks), moved before the replacement
    zeros = [i for i in span_items if i[0] == 'z']
    old = [i for i in span_items if i[0] in ('c', 'e')]
    plain, links = parse_to(to)
    sm = difflib.SequenceMatcher(None, find, plain, autojunk=False)
    new = [None] * len(plain)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(j2 - j1): new[j1 + k] = old[i1 + k]
    def neigh(j):
        for d in range(1, len(plain) + 1):
            for jj in (j - d, j + d):
                if 0 <= jj < len(plain) and new[jj] is not None and new[jj][0] == 'c': return new[jj]
        return old[0] if old and old[0][0] == 'c' else ('c', ' ', None, None)
    in_new = lambda j: any(s <= j < e for s, e, _ in links)
    for j in range(len(plain)):  # text that came out of an old external link and is not linked now: take plain neighbour formatting
        if new[j] is not None and new[j][0] == 'c' and new[j][3] is not None and RID in new[j][3] and not in_new(j): new[j] = None
    base = [new[j] for j in range(len(plain))]
    def neigh(j):
        for d in range(1, len(plain) + 1):
            for jj in (j - d, j + d):
                if 0 <= jj < len(plain) and base[jj] is not None and base[jj][0] == 'c' and (base[jj][3] is None or RID not in base[jj][3]): return base[jj]
        for it in items[:pos[a]][::-1] + items[pos[b - 1] + 1:]:
            if it[0] == 'c' and (it[3] is None or RID not in it[3]): return it
        return old[0] if old and old[0][0] == 'c' else ('c', ' ', None, None)
    for j in range(len(plain)):
        if base[j] is None: n = neigh(j); new[j] = ('c', plain[j], n[2], n[3] if (n[3] is None or RID not in n[3]) else None)
        elif base[j][0] == 'c': new[j] = ('c', plain[j], base[j][2], base[j][3])
    # links: old external links inside the span are dropped (plain); internal anchors kept; new links applied
    linkobj = {}
    out = []
    for j, it in enumerate(new):
        lk = it[-1]
        if lk is not None and RID in lk: lk = None
        rpr = it[2]
        if lk is None and it[-1] is not None: rpr = unlink_rpr(rpr)
        for (s, e, tgt) in links:
            if s <= j < e:
                if tgt not in linkobj:
                    if tgt.startswith('#'): linkobj[tgt] = {q('anchor'): tgt[1:], q('history'): '1'}
                    else: linkobj[tgt] = {RID: rels.add(tgt), q('history'): '1'}
                lk = linkobj[tgt]; rpr = link_rpr(unlink_rpr(rpr)); break
        out.append((it[0], it[1], rpr, lk))
    items[pos[a]:pos[b - 1] + 1] = zeros + out
    # normalise link identity: consecutive items sharing an equal attrib dict should share the object
    rebuild(p, items)
    return 1

# ---------- HYPERLINK fields -> w:hyperlink ----------
FLD = re.compile(r'HYPERLINK\s+(?:"([^"]+)")?(?:.*?\\l\s+"([^"]+)")?', re.S)
def fields_to_links(body, rels):
    n = 0
    for fs in list(body.iter(q('fldSimple'))):
        m = FLD.search(fs.get(q('instr')) or '')
        if not m: continue
        h = etree.Element(q('hyperlink'))
        if m.group(2): h.set(q('anchor'), m.group(2))
        else: h.set(RID, rels.add(m.group(1)))
        h.set(q('history'), '1')
        for r in list(fs): h.append(r)
        fs.addprevious(h); fs.getparent().remove(fs); n += 1
    for p in body.iter(q('p')):
        while True:
            kids = list(p); begin = None
            for i, c in enumerate(kids):
                if c.tag == q('r') and c.find(q('fldChar')) is not None and c.find(q('fldChar')).get(q('fldCharType')) == 'begin': begin = i; break
            if begin is None: break
            instr = ''; sep = end = None; depth = 0
            for j in range(begin, len(kids)):
                c = kids[j]
                if c.tag != q('r'): continue
                fc = c.find(q('fldChar'))
                if fc is not None:
                    t = fc.get(q('fldCharType'))
                    if t == 'begin': depth += 1
                    elif t == 'separate' and depth == 1: sep = j
                    elif t == 'end':
                        depth -= 1
                        if depth == 0: end = j; break
                it = c.find(q('instrText'))
                if it is not None and depth == 1 and sep is None: instr += it.text or ''
            m = FLD.search(instr)
            if m and sep is not None and end is None:
                # broken field (no end mark in the paragraph): keep the visible result as plain text
                for c in kids[begin:sep + 1]: p.remove(c)
                n += 1; continue
            if not m or sep is None or end is None:
                # not a hyperlink field: mark and move on by renaming nothing; stop scanning this paragraph
                break
            h = etree.Element(q('hyperlink'))
            if m.group(2): h.set(q('anchor'), m.group(2))
            else: h.set(RID, rels.add(m.group(1)))
            h.set(q('history'), '1')
            for c in kids[sep + 1:end]: h.append(c)
            kids[begin].addprevious(h)
            for c in kids[begin:sep + 1] + [kids[end]]: p.remove(c)
            n += 1
    return n

def add_bookmarks(body, specs):
    have = {b.get(q('name')) for b in body.iter(q('bookmarkStart'))}
    ids = [int(b.get(q('id'))) for b in body.iter(q('bookmarkStart')) if (b.get(q('id')) or '').isdigit()]
    nid = max(ids + [800000]) + 1; done = 0; miss = []
    for s in specs:
        if s['name'] in have: done += 1; continue
        rx = re.compile(s['para']); p = next((p for p in body.iter(q('p')) if rx.match(ptext(p))), None)
        if p is None: miss.append(s['name']); continue
        st = etree.Element(q('bookmarkStart')); st.set(q('id'), str(nid)); st.set(q('name'), s['name'])
        en = etree.Element(q('bookmarkEnd')); en.set(q('id'), str(nid)); nid += 1
        p.insert(1 if p.find(q('pPr')) is not None else 0, st); p.append(en); have.add(s['name']); done += 1
    return done, miss

PARTS = ('word/document.xml', 'word/footnotes.xml', 'word/endnotes.xml')
def linkify_data(data, spec, log=print):
    """data: {zip name: bytes}. Changes document/footnotes/endnotes and the rels in place. Returns a report dict."""
    rels = Rels(data); rep = {'rules': [], 'fields': 0, 'bookmarks': 0, 'missing_bookmarks': [], 'left': []}
    trees = {n: etree.fromstring(data[n]) for n in PARTS if n in data}
    # footnotes/endnotes have their own rels file; we only add links in document.xml (all our masters keep sources there)
    doc = trees['word/document.xml']; body = doc.find(q('body'))
    if spec.get('fields'): rep['fields'] = fields_to_links(body, rels)
    if spec.get('bookmarks'): rep['bookmarks'], rep['missing_bookmarks'] = add_bookmarks(body, spec['bookmarks'])
    paras = list(body.iter(q('p')))
    for r in spec.get('rules', []):
        n = 0; blocked = 0
        for p in paras:
            if r.get('max') and n >= r['max']: break
            if r.get('in') and r['in'] not in ptext(p): continue
            while True:
                k = apply_rule(p, r['find'], r['to'], rels)
                if k == 1:
                    n += 1
                    if r['find'] in parse_to(r['to'])[0] or (r.get('max') and n >= r['max']): break
                    continue
                if k == -1: blocked += 1
                break
        rep['rules'].append((r['find'][:70], n, blocked))
        if n == 0: log('  WARN rule matched nothing: %r' % r['find'][:90])
    allow = spec.get('allow', [])
    for n, t in trees.items():
        for p in t.iter(q('p')):
            for u in visible_urls(ptext(p), allow): rep['left'].append((n[5:-4], u, ptext(p)[:120]))
    used = set()
    for t in trees.values():
        for e in t.iter():
            v = e.get(RID)
            if v: used.add(v)
    # rels used by footnotes etc. are in their own rels files; only document.xml rels are pruned
    rels.save(used | {e.get(RID) for e in doc.iter() if e.get(RID)} | set(re.findall(rb'r:id="([^"]+)"', data['word/document.xml'])) - {None})
    data['word/document.xml'] = etree.tostring(doc, xml_declaration=True, encoding='UTF-8', standalone=True)
    return rep

def external_links(data):
    rels = Rels(data); doc = etree.fromstring(data['word/document.xml']); out = []
    for h in doc.iter(q('hyperlink')):
        if h.get(RID): out.append((rels.target(h.get(RID)), ''.join(h.itertext())))
    return out
def internal_links(data):
    doc = etree.fromstring(data['word/document.xml'])
    bm = {b.get(q('name')) for b in doc.iter(q('bookmarkStart'))}
    an = [h.get(q('anchor')) for h in doc.iter(q('hyperlink')) if h.get(q('anchor'))]
    return an, [a for a in an if a not in bm]

def run_file(path, spec_path, out=None):
    spec = json.load(open(spec_path, encoding='utf8'))
    z = zipfile.ZipFile(path); infos = z.infolist(); data = {i.filename: z.read(i.filename) for i in infos}; z.close()
    before_ext = len(external_links(data))
    rep = linkify_data(data, spec)
    out = out or path; tmp = out + '.tmp'
    with zipfile.ZipFile(tmp, 'w') as o:
        for i in infos:
            zi = zipfile.ZipInfo(i.filename, date_time=i.date_time); zi.external_attr = i.external_attr
            zi.compress_type = zipfile.ZIP_STORED if i.filename.startswith('word/media/') else zipfile.ZIP_DEFLATED
            o.writestr(zi, data[i.filename])
    os.replace(tmp, out)
    an, dead = internal_links(data)
    print('links: %d rules applied (%d matched nothing), %d fields converted, %d bookmarks; external links %d -> %d; internal %d (dead %d); visible URLs left %d' % (
        sum(r[1] for r in rep['rules']), sum(1 for r in rep['rules'] if r[1] == 0), rep['fields'], rep['bookmarks'], before_ext, len(external_links(data)), len(an), len(dead), len(rep['left'])))
    for l in rep['left']: print('  left:', l[1], '|', l[2][:90])
    return rep

if __name__ == '__main__':
    a = sys.argv[1:]; out = a[a.index('--out') + 1] if '--out' in a else None
    run_file(a[0], a[1], out)
