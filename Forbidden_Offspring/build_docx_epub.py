"""Build the Word master and the Kindle EPUB from the assembled manuscript.
Run from the repo root, after build_manuscript.py:  python Forbidden_Offspring/build_docx_epub.py
docx: 6x9 in, Georgia, headings bold 16pt blue centered, each chapter / top-level heading on a fresh page.
epub: built from the docx (LOTHAR_RULES: docx is the master, EPUB is built from it).
"""
import subprocess, os, sys, tempfile
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

D = 'Forbidden_Offspring'
VER = 'v1'
MD = f'{D}/manuscript/Forbidden_Offspring_working_v1.md'
DOCX = f'{D}/Forbidden_Offspring_{VER}.docx'
EPUB = f'{D}/Forbidden_Offspring_{VER}.epub'
BLUE = RGBColor(0x1F, 0x4E, 0x8C)

tmp = tempfile.mkdtemp()
ref = os.path.join(tmp, 'ref.docx')
with open(ref, 'wb') as f:
    f.write(subprocess.run(['pandoc', '--print-default-data-file', 'reference.docx'],
                           capture_output=True, check=True).stdout)

def font(style, name='Georgia', size=None, bold=None, color=None):
    style.font.name = name
    rpr = style.element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = rpr.makeelement(qn('w:rFonts'), {}); rpr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        rf.set(qn(a), name)
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    if size: style.font.size = Pt(size)
    if bold is not None: style.font.bold = bold
    if color is not None: style.font.color.rgb = color

r = Document(ref)
for s in r.styles:
    if s.type == 1 and s.name in ('Normal', 'Body Text', 'First Paragraph', 'Compact', 'Block Text'):
        font(s, size=11)
for n in ('Title', 'Subtitle', 'Heading 1', 'Heading 2', 'Heading 3'):
    s = r.styles[n]
    font(s, size=16 if n != 'Title' else 24, bold=True, color=BLUE)
    s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    s.paragraph_format.keep_with_next = True
r.styles['Subtitle'].font.size = Pt(14)
sec = r.sections[0]
sec.page_width, sec.page_height = Inches(6), Inches(9)
for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
    setattr(sec, m, Inches(0.8))
r.save(ref)

import re
BYLINE = 'Lothar J. Musiol writing as Frank Stone'
src = open(MD, encoding='utf-8').read()
src = re.sub(r'\A# Forbidden Offspring\n+\*A novel\*\n+' + re.escape(BYLINE) + r'\n+', '', src)  # title page comes from metadata
src_md = os.path.join(tmp, 'book.md')
open(src_md, 'w', encoding='utf-8').write(src)
meta = os.path.join(tmp, 'meta.yaml')
open(meta, 'w', encoding='utf-8').write(
    'title: Forbidden Offspring\nsubtitle: A Novel\nlang: en-US\nauthor: ' + BYLINE + '\n')
subprocess.run(['pandoc', src_md, '-f', 'markdown+smart', '-o', DOCX, f'--reference-doc={ref}',
                f'--metadata-file={meta}'], check=True)

# page break before every H1, and before H2 chapters (not the appendix/notes sub-sections)
doc = Document(DOCX)
in_part = False
for p in doc.paragraphs:
    if p.style.name == 'Heading 1':
        in_part = p.text.startswith('PART')
        p.paragraph_format.page_break_before = True
    elif p.style.name == 'Heading 2' and in_part:
        p.paragraph_format.page_break_before = True
doc.core_properties.author = 'Lothar J. Musiol'  # property holds the name only; the byline is on the title page
doc.save(DOCX)

# EPUB metadata carries names only (as for Lolly Wren): Lothar J. Musiol primary author, Frank Stone contributor
open(meta, 'w', encoding='utf-8').write(
    'title: Forbidden Offspring\nsubtitle: A Novel\nlang: en-US\n'
    'author: []\ncreator:\n  - role: author\n    text: Lothar J. Musiol\n  - role: author\n    text: Frank Stone\n')
subprocess.run(['pandoc', DOCX, '-o', EPUB, '--toc', '--toc-depth=2', '--split-level=2',
                f'--metadata-file={meta}'], check=True)
print(DOCX, os.path.getsize(DOCX), EPUB, os.path.getsize(EPUB))

# drop the byline-as-creator entry pandoc copies from the docx title page (metadata keeps names only)
import zipfile, re, shutil
tmp_epub = EPUB + '.tmp'
with zipfile.ZipFile(EPUB) as zin, zipfile.ZipFile(tmp_epub, 'w') as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == 'EPUB/content.opf':
            t = data.decode('utf-8')
            t = re.sub(r'\s*<dc:creator id="epub-creator-1">Lothar J\. Musiol writing as Frank Stone</dc:creator>', '', t)
            data = t.encode('utf-8')
        zout.writestr(item, data, compress_type=zipfile.ZIP_STORED if item.filename == 'mimetype' else zipfile.ZIP_DEFLATED)
shutil.move(tmp_epub, EPUB)
