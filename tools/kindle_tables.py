"""Kindle: replace Word tables with Kindle-friendly text or, for tables that need columns, an inline PNG.

Called from kindle_postbuild.py when the spec has "tables": true (10 Oct 2026, see notes/FILE_SIZES.md).
  * 1 column (boxes such as "Try it now"): the paragraphs are lifted out unchanged.
  * 2 columns: one paragraph per row, "first cell — second cell" (first cell bold; "1." for numbered rows).
  * 3+ columns: a key line with the headings, then one paragraph per row: first cell bold, each further
    value labelled with its column heading, on its own line.
  * Matrices (narrow bracket cells), numeric tables (3+ columns, mostly numbers) and wide tables
    (5+ columns of short entries): drawn as a PNG about 800 px wide; all the table's text goes in the alt text.
Run formatting, links, bookmarks and footnote marks inside cells are kept in the text forms.
"""
import io, os, re, copy
from lxml import etree
from PIL import Image, ImageDraw, ImageFont

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
RNS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
PIC = 'http://schemas.openxmlformats.org/drawingml/2006/picture'
XS = '{http://www.w3.org/XML/1998/namespace}space'
def q(t): return '{%s}%s' % (W, t)
def val(el, path, attr='val'):
    e = el.find(path) if el is not None else None
    return None if e is None else e.get(q(attr))
def ctext(el): return ''.join(t.text or '' for t in el.iter(q('t')))

# ---------- fonts ----------
FD = os.environ.get('KINDLE_FONT_DIR', r'C:\Windows\Fonts')
FACES = {(0, 0): 'DejaVuSans.ttf', (1, 0): 'DejaVuSans-Bold.ttf', (0, 1): 'DejaVuSans-Oblique.ttf', (1, 1): 'DejaVuSans-BoldOblique.ttf'}
FALLBACK = ['seguisym.ttf', 'cambria.ttc', 'arial.ttf']
_fc = {}; _cmap = {}
def cmap(fn):
    if fn not in _cmap:
        try:
            from fontTools.ttLib import TTFont
            f = TTFont(os.path.join(FD, fn), fontNumber=0, lazy=True); _cmap[fn] = set(f.getBestCmap() or {})
        except Exception: _cmap[fn] = None
    return _cmap[fn]
def font(fn, px):
    k = (fn, px)
    if k not in _fc: _fc[k] = ImageFont.truetype(os.path.join(FD, fn), px)
    return _fc[k]
def face_for(ch, b, i):
    fn = FACES[(b, i)]; cm = cmap(fn)
    if cm is None or ord(ch) in cm or ch in ' \t': return fn
    for f in FALLBACK:
        c = cmap(f)
        if c and ord(ch) in c: return f
    return fn

# ---------- reading a table ----------
def rpr_props(r):
    rp = r.find(q('rPr'))
    def on(tag):
        e = rp.find(q(tag)) if rp is not None else None
        return e is not None and e.get(q('val')) not in ('0', 'false')
    va = val(rp, q('vertAlign')); col = val(rp, q('color')); sz = val(rp, q('sz'))
    return dict(b=on('b'), i=on('i'), va=va, color=col if col and col != 'auto' else None, sz=int(sz) if sz else None)
def cell_lines(tc):
    """[[ (text, props), ... ] per paragraph]"""
    out = []
    for p in tc.findall(q('p')):
        segs = []
        for r in p.iter(q('r')):
            pr = rpr_props(r)
            for ch in r:
                if ch.tag == q('t'): segs.append((ch.text or '', pr))
                elif ch.tag == q('tab'): segs.append((' ', pr))
                elif ch.tag in (q('br'), q('cr')): segs.append(('\n', pr))
        out.append((segs, val(p, q('pPr') + '/' + q('jc')) or ''))
    return out
def grid(tbl):
    cols = [int(g.get(q('w')) or 0) for g in tbl.findall(q('tblGrid') + '/' + q('gridCol'))]
    rows = []
    for tr in tbl.findall(q('tr')):
        row = []; c = 0
        for tc in tr.findall(q('tc')):
            pr = tc.find(q('tcPr')); span = int(val(pr, q('gridSpan')) or 1)
            vm = pr.find(q('vMerge')) if pr is not None else None
            row.append(dict(tc=tc, c0=c, span=span, vm=None if vm is None else (vm.get(q('val')) or 'continue')))
            c += span
        rows.append(row)
    n = max([sum(x['span'] for x in r) for r in rows] + [len(cols)])
    if len(cols) < n or not all(cols): cols = (cols + [0] * n)[:n]; cols = [w or 1500 for w in cols]
    return cols, rows

# ---------- deciding the form ----------
NUM = re.compile(r'^[\s(]*[−\-+~≈<>±]?\s*\d[\d\s.,·×^⁰¹²³⁴⁵⁶⁷⁸⁹⁻%°½¼¾/:()−\-+e]*\s*([a-zA-Zµμ°%/²³]{0,4}(\s*[a-zA-Zµμ/²³]{0,4})?)?\s*$')
def is_num(s): s = s.strip(); return bool(s) and len(s) <= 18 and bool(NUM.match(s))
def classify(tbl):
    cols, rows = grid(tbl); ncol = len(cols)
    tx = [[ctext(c['tc']).strip() for c in r] for r in rows]
    if tbl.find('.//' + q('tbl')) is not None: return 'text'
    for r in rows:
        for c in r:
            pr = c['tc'].find(q('tcPr')); w = sum(cols[c['c0']:c['c0'] + c['span']])
            if w <= 200 and not ctext(c['tc']).strip() and pr is not None and pr.find(q('tcBorders')) is not None:
                bd = pr.find(q('tcBorders'))
                if any(e.get(q('val')) not in (None, 'nil', 'none') for e in bd): return 'matrix'
    if ncol < 3: return 'text'
    if tbl.find('.//' + q('footnoteReference')) is not None or tbl.find('.//' + q('hyperlink')) is not None: return 'text'
    numcols = 0
    for k in range(ncol):
        colv = [r[k] for r in tx[1:] if len(r) == ncol and r[k]]
        if colv and sum(map(is_num, colv)) / len(colv) >= 0.7: numcols += 1
    if numcols >= 2: return 'image'          # columns of numbers to compare
    allc = [t for r in tx[1:] for t in r if t]
    if ncol >= 5 and allc and sorted(map(len, allc))[len(allc) // 2] <= 14: return 'image'
    return 'text'

# ---------- text forms ----------
def has_header(tbl, rows):
    if len(rows) < 2: return False
    tr = tbl.find(q('tr'))
    if tr.find(q('trPr') + '/' + q('tblHeader')) is not None: return True
    cells = rows[0]
    if not all(ctext(c['tc']).strip() for c in cells): return False
    runs = [r for c in cells for r in c['tc'].iter(q('r')) if ctext(r).strip()]
    if runs and all(rpr_props(r)['b'] for r in runs): return True
    f0 = [val(c['tc'].find(q('tcPr')), q('shd'), 'fill') for c in cells]
    f1 = [val(c['tc'].find(q('tcPr')), q('shd'), 'fill') for c in rows[1]]
    if f0[0] and f0[0] not in ('auto', 'FFFFFF') and f0 != f1: return True
    look = tbl.find(q('tblPr') + '/' + q('tblLook'))
    sty = val(tbl.find(q('tblPr')), q('tblStyle'))
    return bool(look is not None and look.get(q('firstRow')) == '1' and sty)
def clean_runs(els, bold=None, italic=None, header=False):
    out = []
    for e in els:
        e = copy.deepcopy(e)
        for r in ([e] if e.tag == q('r') else list(e.iter(q('r')))):
            rp = r.find(q('rPr'))
            if rp is None: rp = etree.SubElement(r, q('rPr')); r.remove(rp); r.insert(0, rp)
            for c in rp.findall(q('color')):
                v = (c.get(q('val')) or '').upper()
                if header or v in ('FFFFFF', 'FFFFFE', 'F2F2F2'): rp.remove(c)
            for s in rp.findall(q('shd')): rp.remove(s)
            if bold and rp.find(q('b')) is None: rp.insert(0, etree.Element(q('b')))
            if italic and rp.find(q('i')) is None: rp.insert(0, etree.Element(q('i')))
        out.append(e)
    return out
def content_of(tc):
    """Paragraph children (runs, links, bookmarks...) of every paragraph in the cell, paragraphs joined by a line break."""
    out = []; first = True
    for p in tc.findall(q('p')):
        kids = [k for k in p if k.tag != q('pPr')]
        if not any(ctext(k).strip() for k in kids) and not any(k.tag in (q('bookmarkStart'), q('bookmarkEnd')) for k in kids): continue
        if not first: out.append(br())
        out += kids; first = False
    return out
def mkrun(text, b=False, i=False):
    r = etree.Element(q('r')); rp = etree.SubElement(r, q('rPr'))
    if b: etree.SubElement(rp, q('b'))
    if i: etree.SubElement(rp, q('i'))
    t = etree.SubElement(r, q('t')); t.text = text; t.set(XS, 'preserve'); return r
def br(): r = etree.Element(q('r')); etree.SubElement(r, q('br')); return r
def para(ppr, kids):
    p = etree.Element(q('p'))
    if ppr is not None: p.append(copy.deepcopy(ppr))
    for k in kids: p.append(k)
    return p
def body_ppr(tbl, styles_ok):
    """pPr for the new paragraphs: the style of the nearest body paragraph before the table, spacing 80 after."""
    e = tbl.getprevious(); sty = None
    while e is not None:
        if e.tag == q('p') and ctext(e).strip():
            s = val(e.find(q('pPr')), q('pStyle'))
            if s is None or styles_ok(s): sty = s; break
        e = e.getprevious()
    ppr = etree.Element(q('pPr'))
    if sty: etree.SubElement(ppr, q('pStyle')).set(q('val'), sty)
    sp = etree.SubElement(ppr, q('spacing')); sp.set(q('before'), '0'); sp.set(q('after'), '100')
    return ppr
def to_text(tbl, styles_ok):
    cols, rows = grid(tbl); ncol = len(cols); ppr = body_ppr(tbl, styles_ok); out = []
    rows = [[c for c in r if c['vm'] != 'continue'] for r in rows]
    if ncol == 1 or all(len(r) == 1 for r in rows):
        for r in rows:
            for c in r:
                for p in c['tc'].findall(q('p')):
                    p = copy.deepcopy(p)
                    for rr in p.iter(q('r')):
                        rp = rr.find(q('rPr'))
                        if rp is not None:
                            for cc in rp.findall(q('color')):
                                if (cc.get(q('val')) or '').upper() == 'FFFFFF': rp.remove(cc)
                    out.append(p)
        return out
    hdr = has_header(tbl, rows); heads = [ctext(c['tc']).strip() for c in rows[0]] if hdr else None
    body = rows[1:] if hdr else rows
    if hdr:
        kids = []
        for k, c in enumerate(rows[0]):
            if k: kids.append(mkrun(' — ', b=True))
            kids += clean_runs(content_of(c['tc']), bold=True, header=True)
        out.append(para(ppr, kids))   # the column headings, as a key line
    for r in body:
        cells = [c for c in r]; kids = []
        if ncol == 2 or len(cells) == 2:
            a = content_of(cells[0]['tc']); at = ctext(cells[0]['tc']).strip()
            kids += clean_runs(a, bold=True)
            rest = [x for c in cells[1:] for x in content_of(c['tc'])]
            if rest:
                kids.append(mkrun('. ' if re.fullmatch(r'\(?\d+[a-z]?\)?', at) else ' — ', b=bool(re.fullmatch(r'\(?\d+[a-z]?\)?', at))))
                kids += clean_runs(rest)
        elif hdr:
            first = True
            for k, c in enumerate(cells):
                cc = content_of(c['tc'])
                if not ctext(c['tc']).strip(): continue
                if not first: kids.append(br())
                h = heads[k] if k < len(heads) else ''
                if k == 0: kids += clean_runs(cc, bold=True)   # its heading is in the key line
                else:
                    if h: kids.append(mkrun(h + ': ', i=True))
                    kids += clean_runs(cc)
                first = False
        else:
            first = True
            for k, c in enumerate(cells):
                cc = content_of(c['tc'])
                if not ctext(c['tc']).strip(): continue
                if not first: kids.append(mkrun(' — '))
                kids += clean_runs(cc, bold=(k == 0)); first = False
        if kids: out.append(para(ppr, kids))
    return out

# ---------- image form ----------
def borders_of(tbl):
    tp = tbl.find(q('tblPr')); bd = tp.find(q('tblBorders')) if tp is not None else None
    d = {}
    if bd is not None:
        for e in bd: d[etree.QName(e).localname] = e
    sty = val(tp, q('tblStyle')) or ''
    if not d and re.search(r'grid', sty, re.I):
        for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
            e = etree.Element(q(s)); e.set(q('val'), 'single'); e.set(q('sz'), '4'); e.set(q('color'), '000000'); d[s] = e
    return d
def line_of(e):
    if e is None or e.get(q('val')) in (None, 'nil', 'none'): return None
    c = e.get(q('color')) or '000000'; c = '000000' if c == 'auto' else c
    return (int(e.get(q('sz')) or 4), '#' + c)
def render(tbl, scale_px=None, target_w=800):
    cols, rows = grid(tbl); tb = borders_of(tbl); kind = classify(tbl)
    # trim empty, unbordered side columns (matrix layouts sit in a full-width band)
    def col_used(k):
        for r in rows:
            for c in r:
                if c['c0'] <= k < c['c0'] + c['span'] and ctext(c['tc']).strip(): return True
        return False
    lo, hi = 0, len(cols)
    if kind == 'matrix':
        while lo < hi and not col_used(lo) and cols[lo] > 200: lo += 1
        while hi > lo and not col_used(hi - 1) and cols[hi - 1] > 200: hi -= 1
    total = sum(cols[lo:hi]) or 1
    S = (target_w / total) if kind != 'matrix' else (target_w / 9360.0) * 1.3
    if kind != 'matrix' and total * S > target_w: S = target_w / total
    base = 22
    def fpx(sz, sup=False): return max(10, round(max(18, (sz or base) / 2 * 20 * S) * (0.68 if sup else 1)))
    padx = max(5, round(90 * S)); pady = max(4, round(50 * S))
    cw_px = [w * S for w in cols[lo:hi]]
    if kind == 'matrix':   # never wrap a matrix entry or its label: widen the column instead
        for r in rows:
            for c in r:
                if c['span'] != 1 or not (lo <= c['c0'] < hi): continue
                for segs, jc in cell_lines(c['tc']):
                    nat = sum(measure(t, pr, fpx) for t, pr in segs if t != '\n') + 2 * padx + 2
                    cw_px[c['c0'] - lo] = max(cw_px[c['c0'] - lo], nat)
    X = [0]
    for w in cw_px: X.append(X[-1] + w)
    # lay out each cell
    lay = {}
    for ri, r in enumerate(rows):
        for c in r:
            a, b = max(c['c0'], lo), min(c['c0'] + c['span'], hi)
            if a >= b: continue
            cw = X[b - lo] - X[a - lo] - 2 * padx; lines = []
            for segs, jc in cell_lines(c['tc']):
                cur = []; curw = 0; words = []
                for t, pr in segs:
                    for tok in re.split(r'(\s+|\n)', t):
                        if tok: words.append((tok, pr))
                for tok, pr in words:
                    if tok == '\n': lines.append((cur, jc)); cur = []; curw = 0; continue
                    w = measure(tok, pr, fpx)
                    if cur and curw + w > cw and tok.strip():
                        while cur and not cur[-1][0].strip(): curw -= measure(cur[-1][0], cur[-1][1], fpx); cur.pop()
                        lines.append((cur, jc)); cur = []; curw = 0
                    if not cur and not tok.strip(): continue
                    cur.append((tok, pr)); curw += w
                lines.append((cur, jc))
            lh = round(fpx(None) * 1.3)
            lay[(ri, c['c0'])] = (lines, lh)
    H = []
    for ri, r in enumerate(rows):
        h = 0
        for c in r:
            if (ri, c['c0']) in lay and c['vm'] is None:
                lines, lh = lay[(ri, c['c0'])]; h = max(h, len(lines) * lh + 2 * pady)
        H.append(max(h, round(fpx(None) * 1.3) + 2 * pady))
    Y = [0]
    for h in H: Y.append(Y[-1] + h)
    m = 2; img = Image.new('RGB', (round(X[-1]) + 2 * m, round(Y[-1]) + 2 * m), 'white'); d = ImageDraw.Draw(img)
    def span_rows(ri, c):
        if c['vm'] != 'restart': return ri + 1
        e = ri + 1
        while e < len(rows) and any(x['c0'] == c['c0'] and x['vm'] == 'continue' for x in rows[e]): e += 1
        return e
    edges = []
    for ri, r in enumerate(rows):
        for c in r:
            if (ri, c['c0']) not in lay or c['vm'] == 'continue': continue
            a, b = max(c['c0'], lo) - lo, min(c['c0'] + c['span'], hi) - lo; re_ = span_rows(ri, c)
            x0, x1, y0, y1 = m + X[a], m + X[b], m + Y[ri], m + Y[re_]
            pr = c['tc'].find(q('tcPr')); fill = val(pr, q('shd'), 'fill')
            if fill and fill != 'auto' and re.fullmatch(r'[0-9A-Fa-f]{6}', fill): d.rectangle([x0, y0, x1, y1], fill='#' + fill)
            cb = {}
            bd = pr.find(q('tcBorders')) if pr is not None else None
            if bd is not None:
                for e in bd: cb[etree.QName(e).localname.replace('start', 'left').replace('end', 'right')] = e
            for side, outer, inner in (('top', ri == 0, 'insideH'), ('bottom', re_ == len(rows), 'insideH'), ('left', a == 0, 'insideV'), ('right', b == len(cols[lo:hi]), 'insideV')):
                e = cb[side] if side in cb else tb.get(side if outer else inner)
                ln = line_of(e)
                if ln: edges.append((side, x0, x1, y0, y1, ln))
            lines, lh = lay[(ri, c['c0'])]
            va = val(pr, q('vAlign')) or 'top'; th = len(lines) * lh
            ty = y0 + pady + ((y1 - y0 - 2 * pady - th) / 2 if va == 'center' else (y1 - y0 - 2 * pady - th) if va == 'bottom' else 0)
            for k, (segs, jc) in enumerate(lines):
                lw = sum(measure(t, p, fpx) for t, p in segs)
                tx = x0 + padx + ((x1 - x0 - 2 * padx - lw) / 2 if jc == 'center' else (x1 - x0 - 2 * padx - lw) if jc in ('right', 'end') else 0)
                for t, p in segs: tx += draw_seg(d, tx, ty + k * lh, t, p, fpx)
    for side, x0, x1, y0, y1, (sz, col) in edges:
        w = max(1, round(sz / 8 * 20 * S / 2.2))
        if side == 'top': d.rectangle([x0, y0, x1, y0 + w - 1], fill=col)
        elif side == 'bottom': d.rectangle([x0, y1 - w + 1, x1, y1], fill=col)
        elif side == 'left': d.rectangle([x0, y0, x0 + w - 1, y1], fill=col)
        else: d.rectangle([x1 - w + 1, y0, x1, y1], fill=col)
    return img
def runs_by_face(t, pr):
    out = []; b, i = int(pr['b']), int(pr['i'])
    for ch in t:
        f = face_for(ch, b, i)
        if out and out[-1][0] == f: out[-1][1] += ch
        else: out.append([f, ch])
    return out
def measure(t, pr, fpx):
    px = fpx(pr['sz'], pr['va'] in ('superscript', 'subscript'))
    return sum(font(f, px).getlength(s) for f, s in runs_by_face(t, pr))
def draw_seg(d, x, y, t, pr, fpx):
    sup = pr['va'] in ('superscript', 'subscript'); px = fpx(pr['sz'], sup); full = fpx(pr['sz'])
    dy = -round(full * 0.12) if pr['va'] == 'superscript' else round(full * 0.45) if pr['va'] == 'subscript' else 0
    col = '#' + pr['color'] if pr['color'] and re.fullmatch(r'[0-9A-Fa-f]{6}', pr['color']) else '#000000'
    w = 0
    for f, s in runs_by_face(t, pr):
        fo = font(f, px); d.text((x + w, y + dy + (full - px) * (0.0 if pr['va'] == 'superscript' else 0)), s, font=fo, fill=col); w += fo.getlength(s)
    return w
def alt_text(tbl, kind):
    cols, rows = grid(tbl); sep = ' ' if kind == 'matrix' else ' | '
    out = []
    for r in rows:
        cells = [re.sub(r'\s+', ' ', ctext(c['tc'])).strip() for c in r if c['vm'] != 'continue']
        cells = [c for c in cells if c]
        if cells: out.append(sep.join(cells))
    return ('; ' if kind == 'matrix' else '. ').join(out)
def png_bytes(img):
    qi = img.quantize(colors=64, method=Image.Quantize.MEDIANCUT); b = io.BytesIO(); qi.save(b, 'PNG', optimize=True); return b.getvalue()

def inline_drawing(rid, cx, cy, pid, name, descr):
    x = ('<w:r xmlns:w="%s" xmlns:wp="%s" xmlns:a="%s" xmlns:pic="%s" xmlns:r="%s"><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
         '<wp:extent cx="%d" cy="%d"/><wp:docPr id="%d" name="%s" descr=""/><wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>'
         '<a:graphic><a:graphicData uri="%s"><pic:pic><pic:nvPicPr><pic:cNvPr id="%d" name="%s"/><pic:cNvPicPr/></pic:nvPicPr>'
         '<pic:blipFill><a:blip r:embed="%s"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
         '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>'
         ) % (W, WP, A, PIC, RNS, cx, cy, pid, name, PIC, pid, name, rid, cx, cy)
    r = etree.fromstring(x); r.find('.//{%s}docPr' % WP).set('descr', descr); return r

def add_media(doc, name, data):
    import zipfile
    path = 'word/media/' + name; doc.data[path] = data
    doc.infos.append(zipfile.ZipInfo(path, date_time=(2026, 10, 10, 0, 0, 0)))
    relx = doc.data['word/_rels/document.xml.rels'].decode('utf8')
    ids = set(re.findall(r'Id="([^"]+)"', relx)); k = 1
    while 'rIdTbl%d' % k in ids: k += 1
    rid = 'rIdTbl%d' % k
    relx = relx.replace('</Relationships>', '<Relationship Id="%s" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/%s"/></Relationships>' % (rid, name))
    doc.data['word/_rels/document.xml.rels'] = relx.encode('utf8')
    ct = doc.data['[Content_Types].xml'].decode('utf8')
    if not re.search(r'Extension="png"', ct, re.I): ct = ct.replace('</Types>', '<Default Extension="png" ContentType="image/png"/></Types>')
    doc.data['[Content_Types].xml'] = ct.encode('utf8')
    return rid

def style_names(doc):
    try: sx = etree.fromstring(doc.data['word/styles.xml'])
    except KeyError: return {}
    return {s.get(q('styleId')): (val(s, q('name')) or '') for s in sx.iter(q('style'))}

def detable(doc, preview_dir=None, text_width_in=6.0):
    """Replace every top-level table. Returns [(index, kind, rows x cols, first text)]."""
    names = style_names(doc)
    def styles_ok(sid):
        n = (names.get(sid) or sid).lower()
        return not re.search(r'heading|title|caption|toc|contents|header|footer|quote|list|note|box', n)
    log = []; pid = max([int(x) for x in re.findall(rb'<wp:docPr id="(\d+)"', doc.data['word/document.xml'])] + [0]) + 1000
    pid = max([pid] + [int(e.get('id')) + 1 for e in doc.tree.iter('{%s}docPr' % WP) if (e.get('id') or '').isdigit()])
    tbls = [t for t in doc.tree.iter(q('tbl')) if not [a for a in t.iterancestors(q('tbl'))]]
    for n, t in enumerate(tbls):
        cols, rows = grid(t); kind = classify(t); first = re.sub(r'\s+', ' ', ctext(t))[:50]
        parent = t.getparent(); at = parent.index(t)
        if kind == 'text':
            new = to_text(t, styles_ok)
        else:
            img = render(t); data = png_bytes(img)
            if preview_dir: img.save(os.path.join(preview_dir, 'table_%03d_%s.png' % (n, kind)))
            fname = 'table_%03d.png' % n
            while 'word/media/' + fname in doc.data: fname = fname.replace('.png', 'b.png')
            rid = add_media(doc, fname, data)
            wi = min(text_width_in, img.width / (800 / text_width_in) if kind != 'matrix' else img.width / 140.0)
            cx = int(wi * 914400); cy = int(cx * img.height / img.width)
            ppr = etree.Element(q('pPr')); etree.SubElement(ppr, q('jc')).set(q('val'), 'center')
            sp = etree.SubElement(ppr, q('spacing')); sp.set(q('before'), '60'); sp.set(q('after'), '120')
            kids = [copy.deepcopy(b) for b in t.iter(q('bookmarkStart'), q('bookmarkEnd'))]
            kids.append(inline_drawing(rid, cx, cy, pid, 'Table %d' % (n + 1), alt_text(t, kind))); pid += 1
            new = [para(ppr, kids)]
        parent.remove(t)
        for k, p in enumerate(new): parent.insert(at + k, p)
        if parent.tag == q('tc') and not parent.findall(q('p')): parent.append(etree.Element(q('p')))
        log.append((n, kind, '%dx%d' % (len(rows), len(cols)), first))
    # a table that ended the body (before sectPr) needs nothing more; floating pictures become inline
    log += unfloat(doc)
    return log

def unfloat(doc):
    out = []
    for an in list(doc.tree.iter('{%s}anchor' % WP)):
        ext = an.find('{%s}extent' % WP); gr = an.find('{%s}graphic' % A); pr = an.find('{%s}docPr' % WP)
        if gr is None or ext is None: continue
        inl = etree.Element('{%s}inline' % WP)
        for k in ('distT', 'distB', 'distL', 'distR'): inl.set(k, '0')
        for e in (ext, an.find('{%s}effectExtent' % WP), pr, an.find('{%s}cNvGraphicFramePr' % WP), gr):
            if e is not None: inl.append(copy.deepcopy(e))
        an.getparent().replace(an, inl); out.append(('anchor', 'inline', '', pr.get('name') if pr is not None else ''))
    return out
