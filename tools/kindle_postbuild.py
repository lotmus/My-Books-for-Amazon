"""Kindle post-build step: shrink images, swap decorative pictures for drawings, split a book.

Run after a book's own build script has written its docx:

    python tools/kindle_postbuild.py "<book folder>/kindle_postbuild.json"

The spec (JSON, paths relative to the spec's folder):
  source         docx written by the build (required)
  photo_width    photos are scaled to this width, px (default 440, never upscaled); photo-like images with
                 labels (large flat background) use diagram_width (800); portrait covers use cover_max (1600)
  jpeg_quality   default 80; line art becomes a 256-colour PNG, longest side lineart_max (1600)
  drawings       {"<regex on the picture's alt text>": "<png>"}: replaces that picture's bytes
  split          optional: {"unsplit_to": "<bak path>", "parts": [...]} (see split_part below)
Nothing is deleted. The unsplit build is moved to split.unsplit_to (overwritten on each build).
Written for the 10 Oct 2026 Kindle size pass; see notes/FILE_SIZES.md.
"""
import zipfile, io, os, sys, re, json, copy, shutil
from lxml import etree
from PIL import Image, ImageOps, ImageEnhance
Image.MAX_IMAGE_PIXELS = None
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
RNS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
XS = '{http://www.w3.org/XML/1998/namespace}space'
def q(t): return '{%s}%s' % (W, t)

# ---------- docx container ----------
class Doc:
    def __init__(self, path):
        z = zipfile.ZipFile(path); self.infos = z.infolist()
        self.data = {i.filename: z.read(i.filename) for i in self.infos}
        self.tree = etree.fromstring(self.data['word/document.xml']); self.body = self.tree.find(q('body'))
    def rels(self):
        x = self.data['word/_rels/document.xml.rels'].decode('utf8')
        return {re.search(r'Id="([^"]+)"', m).group(1): re.search(r'Target="([^"]+)"', m).group(1) for m in re.findall(r'<Relationship [^>]*/>', x)}
    def rename_media(self, old, new):
        for k in list(self.data):
            if k.endswith('.rels'):
                self.data[k] = self.data[k].replace(('"media/' + old[11:] + '"').encode(), ('"media/' + new[11:] + '"').encode())
        self.data[new] = self.data.pop(old)
        for i in self.infos:
            if i.filename == old: i.filename = new
        ext = new.rsplit('.', 1)[1].lower(); ct = self.data['[Content_Types].xml'].decode('utf8')
        if not re.search(r'Extension="%s"' % ext, ct, re.I):
            ct = ct.replace('</Types>', '<Default Extension="%s" ContentType="%s"/></Types>' % (ext, 'image/jpeg' if ext in ('jpg', 'jpeg') else 'image/png'))
        self.data['[Content_Types].xml'] = ct.encode('utf8')
    def save(self, out, images_only=False):
        """images_only: keep document.xml bytes and every part as they were (only media and rels changed)."""
        if images_only: return self._write(out, set())
        xml = etree.tostring(self.tree, xml_declaration=True, encoding='UTF-8', standalone=True); self.data['word/document.xml'] = xml
        sx = xml.decode('utf8'); used = set(re.findall(r'r:(?:embed|id|link)="([^"]+)"', sx))
        relx = self.data['word/_rels/document.xml.rels'].decode('utf8'); drop = set(); keep = []
        for r in re.findall(r'<Relationship [^>]*/>', relx):
            rid = re.search(r'Id="([^"]+)"', r).group(1); tgt = re.search(r'Target="([^"]+)"', r).group(1)
            if 'relationships/image' in r and rid not in used: drop.add('word/' + tgt.replace('/word/', '').lstrip('/')); continue
            keep.append(r)
        head = relx[:relx.index('<Relationship ')]
        self.data['word/_rels/document.xml.rels'] = (head + ''.join(keep) + '</Relationships>').encode('utf8')
        other = b''.join(v for k, v in self.data.items() if k.endswith('.rels') and k != 'word/_rels/document.xml.rels')
        drop = {d for d in drop if d[5:].encode() not in other}
        return self._write(out, drop)
    def _write(self, out, drop):
        tmp = out + '.tmp'
        with zipfile.ZipFile(tmp, 'w') as o:
            for i in self.infos:
                if i.filename in drop: continue
                zi = zipfile.ZipInfo(i.filename, date_time=i.date_time); zi.external_attr = i.external_attr
                if i.filename.startswith('word/media/'): zi.compress_type = zipfile.ZIP_STORED; o.writestr(zi, self.data[i.filename])
                else: zi.compress_type = zipfile.ZIP_DEFLATED; o.writestr(zi, self.data[i.filename], compresslevel=9)
        os.replace(tmp, out)

def text(el): return ''.join(el.itertext())
def style(el):
    s = el.find(q('pPr') + '/' + q('pStyle')); return s.get(q('val')) if s is not None else ''
def bms(el): return [b.get(q('name')) for b in el.iter(q('bookmarkStart'))]
def est(path):
    z = zipfile.ZipFile(path); return sum(i.file_size if i.filename.startswith('word/media/') else i.compress_size for i in z.infolist())

# ---------- images ----------
def is_photo(im):
    t = im.convert('RGB'); t.thumbnail((256, 256)); return len(set(t.getdata())) > 3000
def flatten(im):
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        im = im.convert('RGBA'); bg = Image.new('RGB', im.size, (255, 255, 255)); bg.paste(im, mask=im.split()[3]); return bg
    return im.convert('RGB')
def scale(im, mx):
    w, h = im.size
    if max(w, h) > mx: r = mx / max(w, h); im = im.resize((max(1, round(w * r)), max(1, round(h * r))), Image.LANCZOS)
    return im
def labelled(im):
    """A 'photo' that is really a labelled diagram: large flat background areas."""
    t = im.convert('L'); t.thumbnail((200, 200)); h = t.histogram(); mode = max(range(256), key=lambda i: h[i])
    flat = sum(h[max(0, mode - 6):mode + 7]) / max(1, sum(h))
    return flat > 0.35
def scale_w(im, w):
    if im.width > w: im = im.resize((w, max(1, round(im.height * w / im.width))), Image.LANCZOS)
    return im
def front_cover_media(doc):
    """The embedded front cover: the first picture in the document, or any picture whose name/alt text says cover."""
    rels = doc.rels(); out = set(); A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
    WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
    for k, dr in enumerate(doc.tree.iter(q('drawing'))):
        blip = dr.find('.//{%s}blip' % A); pr = dr.find('.//{%s}docPr' % WP)
        if blip is None: continue
        alt = ((pr.get('name') or '') + ' ' + (pr.get('descr') or '') + ' ' + (pr.get('title') or '')).lower() if pr is not None else ''
        rid = blip.get('{%s}embed' % RNS)
        if rid in rels and (k == 0 or re.search(r'front cover|\bcover\b', alt)) and 'back' not in alt:
            out.add('word/' + rels[rid].replace('/word/', '').lstrip('/'))
        if k > 0 and not out: break
    return out
def shrink_media(doc, photo_width=440, diagram_width=800, cover_max=1600, quality=80, lineart_max=1600, skip=(), boost=True):
    """Photos: 440 px wide (never upscaled), JPEG q80. Photo-like images with labels: 800 px wide.
    Photos get a mild colour boost (saturation x1.10, contrast x1.04) because small JPEGs look flat.
    Portrait covers: longest side 1600. Line art: 256-colour PNG, longest side 1600."""
    log = []; covers = front_cover_media(doc)
    for name in [n for n in doc.data if n.startswith('word/media/')]:
        if name in skip: continue
        ext = name.rsplit('.', 1)[-1].lower()
        if ext not in ('png', 'jpg', 'jpeg', 'gif', 'bmp', 'tif', 'tiff'): continue
        data = doc.data[name]; im = Image.open(io.BytesIO(data)); im.load()
        if getattr(im, 'n_frames', 1) > 1: continue
        if ext in ('jpg', 'jpeg'): im = ImageOps.exif_transpose(im)
        if ext in ('jpg', 'jpeg') or is_photo(im):
            f = flatten(im)
            if name in covers and im.height > im.width * 1.3: f = scale(f, cover_max); kind = 'cover'
            elif labelled(f): f = scale_w(f, diagram_width); kind = 'labelled'
            else:
                f = scale_w(f, photo_width); kind = 'photo'
                if boost: f = ImageEnhance.Contrast(ImageEnhance.Color(f).enhance(1.10)).enhance(1.04)
            b = io.BytesIO(); f.save(b, 'JPEG', quality=quality, optimize=True); nd = b.getvalue(); nn = name.rsplit('.', 1)[0] + '.jpg' if ext not in ('jpg', 'jpeg') else name
        else:
            im2 = scale(im, lineart_max); kind = 'lineart'
            qi = im2.convert('RGBA').quantize(colors=256, method=Image.Quantize.FASTOCTREE) if (im2.mode in ('RGBA', 'LA') or 'transparency' in im2.info) else im2.convert('RGB').quantize(colors=256, method=Image.Quantize.MEDIANCUT)
            b = io.BytesIO(); qi.save(b, 'PNG', optimize=True); nd = b.getvalue(); nn = name.rsplit('.', 1)[0] + '.png'
        if len(nd) < len(data) * 0.92:
            doc.data[name] = nd
            if nn != name:
                if nn in doc.data: nn = nn.rsplit('.', 1)[0] + '_k.' + nn.rsplit('.', 1)[1]
                doc.rename_media(name, nn)
            log.append((name, len(data), len(nd), kind))
    return log
def swap_drawings(doc, drawings, base):
    rels = doc.rels(); done = []
    WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'; A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
    for dr in doc.tree.iter(q('drawing')):
        pr = dr.find('.//{%s}docPr' % WP); blip = dr.find('.//{%s}blip' % A)
        if pr is None or blip is None: continue
        alt = (pr.get('descr') or '') + ' ' + (pr.get('title') or '')
        for pat, png in drawings.items():
            if re.search(pat, alt.strip()):
                rid = blip.get('{%s}embed' % RNS); name = 'word/' + rels[rid].replace('/word/', '').lstrip('/')
                doc.data[name] = open(os.path.join(base, png), 'rb').read()
                if not name.lower().endswith('.png'):
                    nn = name.rsplit('.', 1)[0] + '.png'
                    if nn in doc.data: nn = name.rsplit('.', 1)[0] + '_d.png'
                    doc.rename_media(name, nn); rels = doc.rels()
                done.append(pat); break
    return done

# ---------- paragraph helpers ----------
def run(textv, rpr=None):
    r = etree.Element(q('r'))
    if rpr is not None: r.append(copy.deepcopy(rpr))
    t = etree.SubElement(r, q('t')); t.text = textv; t.set(XS, 'preserve'); return r
def set_text(p, new):
    first = next((r for r in p.iter(q('r')) if r.find(q('t')) is not None), None)
    rpr = first.find(q('rPr')) if first is not None else None
    for c in list(p):
        if c.tag != q('pPr'): p.remove(c)
    p.append(run(new, rpr)); return p
def clone(like, new_text):
    p = copy.deepcopy(like)
    for b in list(p.iter(q('bookmarkStart'))) + list(p.iter(q('bookmarkEnd'))): b.getparent().remove(b)
    return set_text(p, new_text)
_bid = [900000]
def add_bookmark(p, name):
    _bid[0] += 1; s = etree.Element(q('bookmarkStart')); s.set(q('id'), str(_bid[0])); s.set(q('name'), name)
    e = etree.Element(q('bookmarkEnd')); e.set(q('id'), str(_bid[0]))
    p.insert(1 if p.find(q('pPr')) is not None else 0, s); p.append(e)
def link_whole(p, anchor):
    h = etree.Element(q('hyperlink')); h.set(q('anchor'), anchor); h.set(q('history'), '1')
    for c in [c for c in p if c.tag in (q('r'), q('hyperlink'))]:
        p.remove(c)
        for r in (c.iter(q('r')) if c.tag == q('hyperlink') else [c]): h.append(copy.deepcopy(r))
    p.append(h)
def page_break():
    p = etree.Element(q('p')); r = etree.SubElement(p, q('r')); b = etree.SubElement(r, q('br')); b.set(q('type'), 'page'); return p
def replace_in(p, old, new):
    for t in p.iter(q('t')):
        if t.text and old in t.text: t.text = t.text.replace(old, new); return True
    full = text(p)
    if old in full and p.find('.//' + q('hyperlink')) is None: set_text(p, full.replace(old, new)); return True
    return False

# ---------- split ----------
def locate(els, key):
    if key == 'START': return 0
    if key == 'END': return len(els) - 1 if etree.QName(els[-1]).localname == 'sectPr' else len(els)
    if key.startswith('text:'):
        rx = re.compile(key[5:]); return next(i for i, e in enumerate(els) if rx.search(text(e)))
    return next(i for i, e in enumerate(els) if key in bms(e))
def find_like(els, like):
    kind, v = like.split(':', 1)
    if kind == 'style': return next(e for e in els if style(e) == v and text(e).strip())
    if kind == 'text': return next(e for e in els if re.search(v, text(e)))
    if kind == 'sty':
        st, rx = v.split(':', 1); return next(e for e in els if style(e) == st and re.search(rx, text(e)))
    raise ValueError(like)

def apply_credits(els, cr):
    """Photo credit line 'Photographs. Fig N: ... .': keep figures in cr['figs'], drop those redrawn (cr['drawn'])."""
    if not cr: return
    p = next((e for e in els if text(e).startswith(cr['para_startswith'])), None)
    if p is None: return

    full = text(p); head, rest = full.split(' ', 1)
    items = re.findall(r'(Fig (\d+): .*?\.)(?= Fig \d+:| Diagrams| *$)', rest)
    tail = rest[rest.rfind('Diagrams'):] if 'Diagrams' in rest else ''
    kept = [t for t, n in items if int(n) in cr['figs'] and int(n) not in cr.get('drawn', [])]
    drawn = [n for n in cr.get('drawn', []) if n in cr['figs']]
    extra = (' Figures %s are simple drawings made for this edition.' % ', '.join(str(n) for n in drawn)) if drawn else ''
    set_text(p, head + ' ' + ' '.join(kept) + (' ' if kept else '') + tail + extra)

def split_part(src_doc, part, all_bms_by_part, me, base):
    doc = copy.deepcopy(src_doc); doc.tree = copy.deepcopy(src_doc.tree); doc.body = doc.tree.find(q('body'))
    els = list(doc.body); keep = set()
    for a, b in part['ranges']: keep.update(range(locate(els, a), locate(els, b)))
    sect = els[-1] if etree.QName(els[-1]).localname == 'sectPr' else None
    for i, e in enumerate(els):
        if i not in keep and e is not sect: doc.body.remove(e)
    els = list(doc.body)
    # text edits
    for old, new in part.get('replace', []):
        hit = sum(replace_in(p, old, new) for p in doc.body.iter(q('p')))
        if not hit: print('  WARN replace not found:', old[:60])
    # credits: keep only the named figures
    apply_credits(els, part.get('credits'))    # inserts
    for ins in part.get('insert', []):
        els = list(doc.body)
        at = locate(els, ins['before']) if 'before' in ins else locate(els, ins['after']) + 1
        if ins.get('after') == 'END': at = locate(els, 'END')
        new = []
        if ins.get('page_break'): new.append(page_break())
        for spec in ins['paras']:
            p = clone(find_like(els + list(src_doc.body), spec['like']), spec['text'])
            if spec.get('bold'):
                for r in p.iter(q('r')):
                    rpr = r.find(q('rPr'))
                    if rpr is None: rpr = etree.SubElement(r, q('rPr')); r.remove(rpr); r.insert(0, rpr)
                    if rpr.find(q('b')) is None: rpr.insert(0, etree.Element(q('b')))
            if spec.get('bookmark'): add_bookmark(p, spec['bookmark'])
            if spec.get('link'): link_whole(p, spec['link'])
            new.append(p)
        for k, p in enumerate(new): doc.body.insert(at + k, p)
    els = list(doc.body)
    body_bms = set().union(*[set(bms(e)) for e in els])
    # notes: keep a note only if the text that cites it is in this part
    if part.get('notes'):
        for e in els:
            nb = [b for b in bms(e) if re.match(part['notes']['bookmark'], b)]
            if nb:
                back = next((h.get(q('anchor')) for h in e.iter(q('hyperlink')) if h.get(q('anchor'))), None)
                if back and back not in body_bms: doc.body.remove(e)
    # bibliography by chapter: drop groups whose chapter is not in this part
    if part.get('biblio'):
        els = list(doc.body); a = locate(els, part['biblio']['start']); stop = re.compile(part['biblio']['stop'])
        drop = False
        for e in els[a + 1:]:
            if stop.search(text(e)) or style(e).startswith('Heading'): break
            hs = [h.get(q('anchor')) for h in e.iter(q('hyperlink')) if h.get(q('anchor'))]
            if style(e) != part['biblio']['item_style']:
                drop = bool(hs) and hs[0] not in body_bms
            if drop: doc.body.remove(e)
    els = list(doc.body); body_bms = set().union(*[set(bms(e)) for e in els])
    # contents page: drop entries that point outside this part
    t = part['toc']; a = locate(els, t['start']); b = locate(els, t['end']); removed = 0
    for e in els[a + 1:b]:
        hs = [h.get(q('anchor')) for h in e.iter(q('hyperlink')) if h.get(q('anchor'))]
        if hs and hs[0] not in body_bms: doc.body.remove(e); removed += 1
    for add in t.get('add', []):
        els = list(doc.body); a = locate(els, t['start']); b = locate(els, t['end'])
        entries = [e for e in els[a + 1:b] if any(h.get(q('anchor')) for h in e.iter(q('hyperlink')))]
        like = next(e for e in entries if style(e) == add['like_style']) if add.get('like_style') else entries[-1]
        p = clone(like, add['text']); link_whole(p, add['anchor'])
        if add.get('before_anchor'):
            ref = next(e for e in entries if any(h.get(q('anchor')) == add['before_anchor'] for h in e.iter(q('hyperlink'))))
            ref.addprevious(p)
        elif add.get('after_anchor'):
            ref = next(e for e in entries if any(h.get(q('anchor')) == add['after_anchor'] for h in e.iter(q('hyperlink'))))
            ref.addnext(p)
        else: entries[-1].addnext(p)
    # links into the other part become plain text with a pointer
    els = list(doc.body); body_bms = set().union(*[set(bms(e)) for e in els]); other = set()
    for k, s in all_bms_by_part.items():
        if k != me: other |= s
    dead = 0
    for h in list(doc.body.iter(q('hyperlink'))):
        an = h.get(q('anchor'))
        if an and an not in body_bms:
            par = h.getparent(); i = par.index(h); kids = list(h)
            for k, r in enumerate(kids): par.insert(i + k, r)
            par.remove(h); dead += 1
            if an in other and part.get('other_suffix') and not re.match(r'^\s*\d+\s*$', ''.join(text(r) for r in kids)):
                rpr = kids[-1].find(q('rPr')) if kids else None
                rr = run(part['other_suffix'], rpr)
                for va in rr.iter(q('vertAlign')): va.getparent().remove(va)
                par.insert(par.index(kids[-1]) + 1 if kids else i, rr)
    out = os.path.join(base, part['out']); doc.save(out)
    import docx; d = docx.Document(out); assert len(d.paragraphs) > 10
    print('  wrote %s  est %.2f MB  (toc entries dropped %d, cross-part links unlinked %d)' % (part['out'], est(out) / 1e6, removed, dead))
    return out

def part_bookmarks(doc, part):
    els = list(doc.body); keep = set()
    for a, b in part['ranges']: keep.update(range(locate(els, a), locate(els, b)))
    s = set()
    for i in keep: s |= set(bms(els[i]))
    return s

def main(spec_path, src_override=None):
    base = os.path.dirname(os.path.abspath(spec_path)); spec = json.load(open(spec_path, encoding='utf8'))
    if isinstance(spec.get('source'), list):
        for s in spec['source']:
            one = dict(spec, source=s); tmp = spec_path + '.one.json'
            json.dump(one, open(tmp, 'w', encoding='utf8')); main(tmp); os.replace(tmp, tmp + '.last')
        return
    src = src_override or os.path.join(base, spec['source'])
    if not os.path.exists(src): print('postbuild: nothing to do, no', src); return
    print('postbuild:', src, 'est %.2f MB' % (est(src) / 1e6))
    doc = Doc(src)
    if spec.get('drawings'): print('  drawings swapped:', len(swap_drawings(doc, spec['drawings'], base)))
    lg = shrink_media(doc, spec.get('photo_width', 440), spec.get('diagram_width', 800), spec.get('cover_max', 1600), spec.get('jpeg_quality', 80), spec.get('lineart_max', 1600))
    print('  images recompressed:', len(lg))
    sp = spec.get('split')
    if not sp:
        if spec.get('credits'): apply_credits(list(doc.body), spec['credits']); doc.save(src)
        else: doc.save(src, images_only=True)
        print('  est after %.2f MB' % (est(src) / 1e6)); return
    allb = {k: part_bookmarks(doc, p) for k, p in enumerate(sp['parts'])}
    for k, p in enumerate(sp['parts']): split_part(doc, p, allb, k, base)
    dst = os.path.join(base, sp['unsplit_to']); os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.environ.get('POSTBUILD_KEEP_SOURCE'): print('  (test run: unsplit build left in place)'); return
    shutil.move(src, dst); print('  unsplit build moved to', sp['unsplit_to'])

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)



