"""Build a Mathematics Tower volume as EPUB 3, straight from its .docx.

    python Tools/make_epub.py 4            # build Volume 4 beside the .docx
    python Tools/make_epub.py all          # build all four
    python Tools/make_epub.py 4 -o X.epub  # build somewhere else

Word is not involved: the .docx is read as a zip and its document.xml is
walked directly, so nothing here can crash Word or be rewritten by it. Every
build is verified before the script exits, and a failed verification is a
non-zero exit — see verify() at the bottom for what is checked.

What the conversion preserves, and the three places it deliberately departs
from the printed layout, are recorded in the commit that introduced this file
("Volume 4: add the EPUB edition"). In short: diagram widths become
percentages so they stay legible on a phone; the body carries an explicit
white ground, because Kindle's dark theme would otherwise put dark text on a
dark page; and diagrams are flattened RGBA to RGB, since Kindle does not
support transparency and every diagram carries a fully opaque alpha band it
has no use for. The flattening is pixel-identical.

Assumes the house conventions all four volumes share: one Heading1 per
chapter, the printed Table of Contents as its own Heading1 (dropped here, the
EPUB nav replaces it), shaded paragraphs for example boxes, an italic gold
centred paragraph after each diagram as its caption, and w:anchor bookmarks
for every cross-reference.
"""

import argparse
import collections
import datetime
import html
import io
import os
import posixpath
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

from PIL import Image

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BOOKS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG = 'en-GB'

BLOCK = re.compile(r'<w:(p|tbl)(?:\s[^>]*)?>.*?</w:\1>|<w:(?:p|tbl)(?:\s[^>]*)?/>', re.S)
STYLE = re.compile(r'<w:pStyle w:val="([^"]+)"')
PPR = re.compile(r'<w:pPr>.*?</w:pPr>', re.S)
RPR = re.compile(r'<w:rPr>.*?</w:rPr>', re.S)
TXT = re.compile(r'<w:t(?:\s[^>]*)?>(.*?)</w:t>', re.S)
CHILD = re.compile(r'<w:bookmarkStart[^>]*/>|<w:hyperlink[^>]*>.*?</w:hyperlink>'
                   r'|<w:r(?:\s[^>]*)?>.*?</w:r>', re.S)
ROW = re.compile(r'<w:tr(?:\s[^>]*)?>.*?</w:tr>', re.S)
CELL = re.compile(r'<w:tc(?:\s[^>]*)?>.*?</w:tc>', re.S)
PARA = re.compile(r'<w:p(?:\s[^>]*)?>.*?</w:p>|<w:p(?:\s[^>]*)?/>', re.S)

TAG_COLOR = '3B5170'    # [Understand] / [Calculate] / [Prove] / [Think Further]
CAP_COLOR = '9C7A1E'    # figure captions
BOX = {'E8F1FB': 'ex-num', 'F1ECF7': 'ex-both', 'F3F6FA': 'callout',
       'EFEFEF': 'notice', 'FCEEEA': 'warn'}
BOX_START_SPACING = 160  # twips before a paragraph that opens a new box

CSS = """
body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.5;
       margin: 0 5%; color: #1a1a1a; background: #ffffff; }
h1 { font-size: 1.6em; color: #1B2A44; margin: 1.4em 0 .2em; line-height: 1.25;
     border-bottom: 2px solid #C9A227; padding-bottom: .25em; }
h2 { font-size: 1.22em; color: #1B2A44; margin: 1.5em 0 .3em; line-height: 1.3; }
h3 { font-size: 1.05em; color: #3B5578; margin: 1.2em 0 .3em; }
p  { margin: 0 0 .75em; text-align: justify; }
.ex-num, .ex-both, .callout, .notice, .warn {
     padding: .6em .8em; margin: 1em 0; border-radius: 2px; color: #1a1a1a; }
.ex-num  { background: #E8F1FB; border-left: 4px solid #3B6EA5; }
.ex-both { background: #F1ECF7; border-left: 4px solid #7A5CA5; }
.callout { background: #F3F6FA; border-left: 4px solid #C9A227; }
.notice  { background: #EFEFEF; border-left: 4px solid #777; }
.warn    { background: #FCEEEA; border-left: 4px solid #B5502F; }
.ex-num p, .ex-both p, .callout p, .notice p, .warn p { margin: 0 0 .4em; }
figure { margin: 1.2em 0; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; height: auto; }
figcaption { font-style: italic; color: #6a5a2a; font-size: .9em; margin-top: .4em; }
a { color: #2B5C9B; }
table { border-collapse: collapse; margin: 1.2em auto; font-size: .95em; }
td, th { border: 1px solid #bfc7d2; padding: .3em .55em; text-align: left;
         vertical-align: top; }
td p, th p { margin: 0; text-align: left; }
.title  { text-align: center; font-size: 2em; margin-top: 3em; color: #1B2A44;
          border-bottom: none; }
.subtit { text-align: center; font-style: italic; font-size: 1.1em; color: #444; }
.byline { text-align: center; margin-top: 2em; }
.small  { text-align: center; font-size: .85em; color: #555; }
.eq     { text-align: center; margin: .8em 0; }
.ind    { margin-left: 1.2em; }
.tag    { color: #3B5170; font-weight: bold; }
"""

PAGE = ('<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" '
        'xmlns:epub="http://www.idpf.org/2007/ops" lang="%s" xml:lang="%s">\n'
        '<head>\n<title>%s</title>\n'
        '<link href="../style/main.css" rel="stylesheet" type="text/css"/>\n'
        '</head>\n<body>\n%s\n</body>\n</html>\n')


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def plain(xml):
    return html.unescape(''.join(TXT.findall(xml)))


def style_of(b):
    m = STYLE.search(b)
    return m.group(1) if m else ''


def ppr_of(b):
    m = PPR.search(b)
    return m.group(0) if m else ''


def fill_of(b):
    m = re.search(r'<w:shd[^>]*w:fill="([0-9A-Fa-f]{6})"', ppr_of(b))
    return m.group(1).upper() if m else None


def before_of(b):
    m = re.search(r'<w:spacing[^>]*w:before="(\d+)"', ppr_of(b))
    return int(m.group(1)) if m else 0


def is_centered(b):
    return '<w:jc w:val="center"/>' in ppr_of(b)


def is_caption(b):
    """The italic, gold, 10pt centred line Word puts under each diagram."""
    return (is_centered(b) and '<w:i/>' in b
            and 'w:val="%s"' % CAP_COLOR in b and '<w:sz w:val="20"/>' in b)


def flatten_png(data):
    """Drop a useless alpha channel. Kindle does not support transparency."""
    im = Image.open(io.BytesIO(data))
    if im.mode not in ('RGBA', 'LA'):
        return data
    ground = Image.new('RGB', im.size, (255, 255, 255))
    ground.paste(im, mask=im.convert('RGBA').getchannel('A'))
    buf = io.BytesIO()
    ground.save(buf, 'PNG', optimize=True)
    return buf.getvalue()


class Volume:
    def __init__(self, docx, cover, out):
        self.z = zipfile.ZipFile(docx)
        self.cover = cover
        self.out = out
        self.doc = self.z.read('word/document.xml').decode('utf-8')
        self.rels = dict(re.findall(
            r'Id="([^"]+)"[^>]*Target="media/([^"]+)"',
            self.z.read('word/_rels/document.xml.rels').decode('utf-8')))
        body = self.doc[self.doc.index('<w:body>') + len('<w:body>'):
                        self.doc.rindex('</w:body>')]
        self.blocks = [m.group(0) for m in BLOCK.finditer(body)]
        extents = [int(m) for m in re.findall(r'<wp:extent[^>]*cx="(\d+)"', self.doc)]
        self.max_extent = max(extents) if extents else 1
        self.images = []

        # Metadata comes out of the book itself, so it cannot drift from it.
        ti = next(i for i, b in enumerate(self.blocks) if style_of(b) == 'Title')
        self.title = plain(self.blocks[ti]).strip()
        rest = [plain(b).strip() for b in self.blocks[ti + 1:ti + 4]]
        self.subtitle = next((t for t in rest if t and not t.startswith('by ')), '')
        self.author = next((t[3:] for t in rest if t.startswith('by ')), '')
        n = re.search(r'Volume (\d+)', self.title)
        self.ident = 'mathematics-tower-vol%s' % (n.group(1) if n else '0')

        self.front_end = next(i for i, b in enumerate(self.blocks)
                              if style_of(b) == 'Heading1')
        self.chapters = []
        h1 = [i for i, b in enumerate(self.blocks) if style_of(b) == 'Heading1']
        for k, i in enumerate(h1):
            end = h1[k + 1] if k + 1 < len(h1) else len(self.blocks)
            t = plain(self.blocks[i])
            if t.strip().lower() == 'table of contents':
                continue            # the EPUB nav replaces the printed one
            self.chapters.append((t, i, end))
        self.files = ['text/ch%03d.xhtml' % k for k in range(len(self.chapters) + 1)]

        # Which file each bookmark ends up in, so cross-references can be wired.
        self.home = {}
        for i in range(self.front_end):
            for name in re.findall(r'<w:bookmarkStart[^>]*w:name="([^"]+)"',
                                   self.blocks[i]):
                self.home[name] = self.files[0]
        for k, (_t, a, b2) in enumerate(self.chapters):
            for i in range(a, b2):
                for name in re.findall(r'<w:bookmarkStart[^>]*w:name="([^"]+)"',
                                       self.blocks[i]):
                    self.home[name] = self.files[k + 1]

    # ------------------------------------------------------------------ runs
    def render_run(self, r):
        rpr = RPR.search(r)
        rpr = rpr.group(0) if rpr else ''
        t = esc(html.unescape(''.join(TXT.findall(r))))
        if not t:
            return ''
        bold = '<w:b/>' in rpr
        ital = '<w:i/>' in rpr
        col = re.search(r'<w:color w:val="([0-9A-Fa-f]{6})"', rpr)
        col = col.group(1).upper() if col else None
        if col == TAG_COLOR and bold:
            return '<span class="tag">%s</span>' % t
        if ital:
            t = '<em>%s</em>' % t
        if bold:
            t = '<strong>%s</strong>' % t
        return t

    def render_inline(self, b, cur):
        out = []
        for m in CHILD.finditer(PPR.sub('', b, count=1)):
            s = m.group(0)
            if s.startswith('<w:bookmarkStart'):
                name = re.search(r'w:name="([^"]+)"', s)
                if name and not name.group(1).startswith('_GoBack'):
                    out.append('<a id="%s"/>' % name.group(1))
            elif s.startswith('<w:hyperlink'):
                anchor = re.search(r'w:anchor="([^"]+)"', s)
                text = ''.join(self.render_run(r.group(0)) for r in
                               re.finditer(r'<w:r(?:\s[^>]*)?>.*?</w:r>', s, re.S))
                target = self.home.get(anchor.group(1)) if anchor else None
                if target and text:
                    href = ('#' + anchor.group(1)) if target == cur else \
                           (posixpath.basename(target) + '#' + anchor.group(1))
                    out.append('<a href="%s">%s</a>' % (href, text))
                else:
                    out.append(text)    # dangling link: keep the words, drop the link
            else:
                out.append(self.render_run(s))
        return ''.join(out)

    def image_of(self, b):
        if '<w:drawing>' not in b:
            return None
        m = re.search(r'<a:blip[^>]*r:embed="([^"]+)"', b)
        if not m or m.group(1) not in self.rels:
            return None
        ext = re.search(r'<wp:extent[^>]*cx="(\d+)"', b)
        # Print widths run 59-73% of the 6.3in text column, which is too small
        # for a line diagram on a phone. Rescale to 82-100% of the reading
        # width, keeping the relative sizes the print layout gave them.
        pct = round(int(ext.group(1)) / self.max_extent * 100) if ext else None
        return self.rels[m.group(1)], pct

    def render_table(self, tbl, cur):
        rows = []
        for r in ROW.finditer(tbl):
            cells = []
            for c in CELL.finditer(r.group(0)):
                inner = '\n'.join('<p>%s</p>' % self.render_inline(p.group(0), cur)
                                  for p in PARA.finditer(c.group(0))
                                  if plain(p.group(0)).strip())
                cells.append('<td>%s</td>' % (inner or '&#160;'))
            rows.append('<tr>%s</tr>' % ''.join(cells))
        return '<table>%s</table>' % ''.join(rows)

    # ---------------------------------------------------------------- blocks
    def render_blocks(self, idxs, cur):
        out = []
        box = None
        idxs = list(idxs)
        i = 0
        while i < len(idxs):
            b = self.blocks[idxs[i]]
            st = style_of(b)
            if st in ('TOC1', 'TOC2'):
                i += 1
                continue

            cls = BOX.get(fill_of(b))
            if box and (cls != box or before_of(b) == BOX_START_SPACING):
                out.append('</div>')
                box = None
            if cls and not box:
                out.append('<div class="%s">' % cls)
                box = cls

            if b.startswith('<w:tbl'):
                out.append(self.render_table(b, cur))
                i += 1
                continue

            img = self.image_of(b)
            if img:
                fn, pct = img
                self.images.append(fn)
                cap = ''
                if i + 1 < len(idxs) and is_caption(self.blocks[idxs[i + 1]]):
                    cap = '<figcaption>%s</figcaption>' % self.render_inline(
                        self.blocks[idxs[i + 1]], cur)
                    i += 1
                width = ' style="width:%d%%"' % pct if pct else ''
                out.append('<figure><img src="../images/%s" alt="Diagram"%s/>%s'
                           '</figure>' % (fn, width, cap))
                i += 1
                continue

            inner = self.render_inline(b, cur)
            if st == 'Heading1':
                out.append('<h1>%s</h1>' % inner)
            elif st == 'Heading2':
                out.append('<h2>%s</h2>' % inner)
            elif st == 'Heading3':
                out.append('<h3>%s</h3>' % inner)
            elif st == 'Title':
                out.append('<h1 class="title">%s</h1>' % inner)
            elif not inner.strip():
                pass
            elif is_centered(b):
                out.append('<p class="eq">%s</p>' % inner)
            else:
                ind = re.search(r'<w:ind[^>]*w:left="(\d+)"', ppr_of(b))
                cl = ' class="ind"' if ind and int(ind.group(1)) >= 200 else ''
                out.append('<p%s>%s</p>' % (cl, inner))
            i += 1
        if box:
            out.append('</div>')
        return '\n'.join(out)

    def title_page(self):
        out = ['<h1 class="title">%s</h1>' % esc(self.title),
               '<p class="subtit">%s</p>' % esc(self.subtitle),
               '<p class="byline">by %s</p>' % esc(self.author)]
        for i in range(self.front_end):
            b = self.blocks[i]
            t = plain(b).strip()
            if (style_of(b) == 'Title' or not t or t == self.subtitle
                    or t.startswith('by ')):
                continue
            out.append('<p class="small">%s</p>' % esc(t))
        return '\n'.join(out)

    # ----------------------------------------------------------------- build
    def build(self):
        pages = [('Title Page', PAGE % (LANG, LANG, 'Title Page', self.title_page()))]
        for k, (t, a, b2) in enumerate(self.chapters):
            content = self.render_blocks(range(a, b2), self.files[k + 1])
            pages.append((t, PAGE % (LANG, LANG, esc(t), content)))

        imgs = sorted(set(self.images), key=lambda s: int(re.sub(r'\D', '', s) or 0))
        manifest = [
            '<item href="style/main.css" id="style" media-type="text/css"/>',
            '<item href="nav.xhtml" id="nav" media-type="application/xhtml+xml" '
            'properties="nav"/>',
            '<item href="toc.ncx" id="ncx" media-type="application/x-dtbncx+xml"/>',
            '<item href="images/cover.png" id="cover-img" media-type="image/png" '
            'properties="cover-image"/>']
        manifest += ['<item href="images/%s" id="img_%s" media-type="image/png"/>'
                     % (fn, os.path.splitext(fn)[0]) for fn in imgs]
        spine = ['<itemref idref="nav"/>']
        for k in range(len(pages)):
            manifest.append('<item href="%s" id="chapter_%d" '
                            'media-type="application/xhtml+xml"/>' % (self.files[k], k))
            spine.append('<itemref idref="chapter_%d"/>' % k)

        now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        opf = ('<?xml version="1.0" encoding="utf-8"?>\n'
               '<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="id" '
               'version="3.0">\n  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
               '    <dc:identifier id="id">%s</dc:identifier>\n'
               '    <dc:title>%s</dc:title>\n'
               '    <dc:language>%s</dc:language>\n'
               '    <dc:creator id="creator">%s</dc:creator>\n'
               '    <dc:description>%s</dc:description>\n'
               '    <dc:date>2026</dc:date>\n'
               '    <dc:rights>Copyright \u00a9 2026 %s. All rights reserved.</dc:rights>\n'
               '    <meta property="dcterms:modified">%s</meta>\n'
               '    <meta name="cover" content="cover-img"/>\n'
               '  </metadata>\n  <manifest>\n    %s\n  </manifest>\n'
               '  <spine toc="ncx">\n    %s\n  </spine>\n</package>\n'
               % (self.ident, esc(self.title), LANG, esc(self.author),
                  esc(self.subtitle), esc(self.author), now,
                  '\n    '.join(manifest), '\n    '.join(spine)))

        nav = ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
               '<html xmlns="http://www.w3.org/1999/xhtml" '
               'xmlns:epub="http://www.idpf.org/2007/ops" lang="%s" xml:lang="%s">\n'
               '<head><title>%s</title></head>\n<body>\n'
               '  <nav epub:type="toc" id="toc" role="doc-toc">\n    <h1>Contents</h1>\n'
               '    <ol>\n%s\n    </ol>\n  </nav>\n</body>\n</html>\n'
               % (LANG, LANG, esc(self.title),
                  '\n'.join('      <li><a href="%s">%s</a></li>'
                            % (self.files[k], esc(t))
                            for k, (t, _c) in enumerate(pages))))

        ncx = ('<?xml version="1.0" encoding="utf-8"?>\n'
               '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
               '<head><meta name="dtb:uid" content="%s"/></head>\n'
               '<docTitle><text>%s</text></docTitle>\n<navMap>\n%s\n</navMap>\n</ncx>\n'
               % (self.ident, esc(self.title),
                  '\n'.join('  <navPoint id="np%d" playOrder="%d"><navLabel><text>%s'
                            '</text></navLabel><content src="%s"/></navPoint>'
                            % (k, k + 1, esc(t), self.files[k])
                            for k, (t, _c) in enumerate(pages))))

        container = ('<?xml version="1.0" encoding="utf-8"?>\n'
                     '<container version="1.0" '
                     'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
                     '  <rootfiles><rootfile full-path="EPUB/content.opf" '
                     'media-type="application/oebps-package+xml"/></rootfiles>\n'
                     '</container>\n')

        tmp = self.out + '.building'
        with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as o:
            # mimetype must be first and stored, per the EPUB spec.
            o.writestr(zipfile.ZipInfo('mimetype'), 'application/epub+zip',
                       compress_type=zipfile.ZIP_STORED)
            o.writestr('META-INF/container.xml', container)
            o.writestr('EPUB/content.opf', opf)
            o.writestr('EPUB/style/main.css', CSS)
            o.writestr('EPUB/nav.xhtml', nav)
            o.writestr('EPUB/toc.ncx', ncx)
            for k, (_t, c) in enumerate(pages):
                o.writestr('EPUB/' + self.files[k], c)
            for fn in imgs:
                o.writestr('EPUB/images/' + fn,
                           flatten_png(self.z.read('word/media/' + fn)))
            with open(self.cover, 'rb') as fh:
                o.writestr('EPUB/images/cover.png', flatten_png(fh.read()))
        os.replace(tmp, self.out)
        return len(pages), len(imgs)


# --------------------------------------------------------------------- verify
def verify(epub, docx):
    """Everything that has to hold before this file is fit to upload."""
    z = zipfile.ZipFile(epub)
    names = set(z.namelist())
    problems = []

    if z.testzip() is not None:
        problems.append('zip CRC failure')
    if z.namelist()[0] != 'mimetype' or \
            z.getinfo('mimetype').compress_type != zipfile.ZIP_STORED:
        problems.append('mimetype must be the first entry and stored uncompressed')

    for n in sorted(names):
        if n.endswith(('.xhtml', '.opf', '.ncx', '.xml')):
            try:
                ET.fromstring(z.read(n))
            except ET.ParseError as e:
                problems.append('not well-formed: %s (%s)' % (n, e))

    opf = z.read('EPUB/content.opf').decode()
    manifest = dict(re.findall(r'<item href="([^"]+)" id="([^"]+)"', opf))
    declared = {posixpath.normpath('EPUB/' + h) for h in manifest}
    for h in manifest:
        if posixpath.normpath('EPUB/' + h) not in names:
            problems.append('manifest points at a missing file: ' + h)
    for n in names:
        if n.startswith('EPUB/') and n not in declared and n != 'EPUB/content.opf':
            problems.append('file is in the package but not the manifest: ' + n)
    ids = set(manifest.values())
    spine = re.findall(r'<itemref idref="([^"]+)"/>', opf)
    for s in spine:
        if s not in ids:
            problems.append('spine references an unknown id: ' + s)

    docs = sorted(n for n in names if n.endswith('.xhtml'))
    anchors = {n: set(re.findall(r'\sid="([^"]+)"', z.read(n).decode())) for n in docs}
    links = 0
    for n in docs:
        d = z.read(n).decode()
        base = posixpath.dirname(n)
        for src in (re.findall(r'<img[^>]+src="([^"]+)"', d)
                    + re.findall(r'<link[^>]+href="([^"]+)"', d)):
            if posixpath.normpath(posixpath.join(base, src)) not in names:
                problems.append('broken resource in %s: %s' % (n, src))
        for href in re.findall(r'<a href="([^"]+)"', d):
            links += 1
            f, _, frag = href.partition('#')
            target = n if not f else posixpath.normpath(posixpath.join(base, f))
            if target not in names:
                problems.append('link to a missing file in %s: %s' % (n, href))
            elif frag and frag not in anchors.get(target, ()):
                problems.append('link to a missing anchor in %s: %s' % (n, href))

    # No chapter may lose text. Small positive drift is expected: a word split
    # across two runs in Word becomes two words once the tags are stripped.
    dd = zipfile.ZipFile(docx).read('word/document.xml').decode()
    body = dd[dd.index('<w:body>'):dd.rindex('</w:body>')]
    blocks = [m.group(0) for m in BLOCK.finditer(body)]
    h1 = [i for i, b in enumerate(blocks) if style_of(b) == 'Heading1']
    k = 0
    for j, i in enumerate(h1):
        end = h1[j + 1] if j + 1 < len(h1) else len(blocks)
        title = plain(blocks[i]).strip()
        if title.lower() == 'table of contents':
            continue
        k += 1
        want = len(' '.join(plain(blocks[q]) for q in range(i, end)
                            if style_of(blocks[q]) not in ('TOC1', 'TOC2')).split())
        d = z.read('EPUB/text/ch%03d.xhtml' % k).decode()
        got = len(html.unescape(re.sub(r'<[^>]+>', ' ', d[d.index('<body'):])).split())
        if got < want:
            problems.append('chapter "%s" lost %d words' % (title, want - got))

    imgs = [n for n in names if n.startswith('EPUB/images/') and n != 'EPUB/images/cover.png']
    for n in imgs:
        if Image.open(io.BytesIO(z.read(n))).mode not in ('RGB', 'L', 'P'):
            problems.append('image still carries an alpha channel: ' + n)
    if len(imgs) != dd.count('<w:drawing>'):
        problems.append('%d diagrams in the .docx, %d in the EPUB'
                        % (dd.count('<w:drawing>'), len(imgs)))

    return problems, {'chapters': len(docs) - 1, 'images': len(imgs), 'links': links}


VOLUMES = {
    n: (os.path.join(BOOKS, 'The Mathematics Tower - Volume %d.docx' % n),
        os.path.join(BOOKS, 'Cover Art', 'Cover - Volume %d.png' % n),
        os.path.join(BOOKS, 'The Mathematics Tower - Volume %d.epub' % n))
    for n in (1, 2, 3, 4)}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('volume', help="1, 2, 3, 4, or 'all'")
    ap.add_argument('-o', '--out', help='write here instead of beside the .docx')
    args = ap.parse_args()

    if args.volume.lower() == 'all':
        wanted = [1, 2, 3, 4]
    else:
        wanted = [int(args.volume)]
    if args.out and len(wanted) > 1:
        ap.error('--out takes a single volume')

    failed = False
    for n in wanted:
        docx, cover, out = VOLUMES[n]
        out = args.out or out
        for p in (docx, cover):
            if not os.path.exists(p):
                print('Volume %d: missing %s' % (n, p))
                failed = True
                break
        else:
            vol = Volume(docx, cover, out)
            chapters, images = vol.build()
            problems, stats = verify(out, docx)
            print('Volume %d  %s' % (n, os.path.basename(out)))
            print('  %s' % vol.title)
            print('  %d chapters, %d diagrams, %d cross-links, %.1f MB'
                  % (chapters, images, stats['links'], os.path.getsize(out) / 1048576))
            if problems:
                failed = True
                print('  FAILED verification:')
                for p in problems[:25]:
                    print('    - %s' % p)
                if len(problems) > 25:
                    print('    ... and %d more' % (len(problems) - 25))
            else:
                print('  verified: well-formed, complete manifest, '
                      'no broken links, no text lost')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
