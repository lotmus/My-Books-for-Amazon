# -*- coding: utf-8 -*-
import copy
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W14 = 'http://schemas.microsoft.com/office/word/2010/wordml'

tree = etree.parse("unpacked/word/document.xml")
root = tree.getroot()

def get_full_text(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))

def find_p(paraId):
    m = root.findall(f'.//{{{W}}}p[@{{{W14}}}paraId="{paraId}"]')
    assert len(m) == 1, paraId
    return m[0]

log = []

# ===== Remove the misplaced bookmarkStart markers (still leave bookmarkEnd where the Word
# session put it -- we'll add a matching fresh pair around each proper heading instead, and
# strip the now-redundant orphan bookmarkEnd too). =====
allp = list(root.iter(f'{{{W}}}p'))

def strip_bookmark(name, expected_id):
    for p in allp:
        for bm in list(p.iter(f'{{{W}}}bookmarkStart')):
            if bm.get(f'{{{W}}}name') == name:
                assert bm.get(f'{{{W}}}id') == expected_id
                bm.getparent().remove(bm)
        for bm in list(p.iter(f'{{{W}}}bookmarkEnd')):
            if bm.get(f'{{{W}}}id') == expected_id:
                bm.getparent().remove(bm)

strip_bookmark('toc_next', '22')
strip_bookmark('toc_review', '23')
log.append('Removed misplaced toc_next / toc_review bookmark markers')

# ===== Rebuild the two heading paragraphs to match the working "Acknowledgments" template =====
def make_heading_children(text, bm_id, bm_name):
    xml = (
        f'<root xmlns:w="{W}">'
        f'<w:pPr><w:pStyle w:val="Heading1"/><w:pageBreakBefore/>'
        f'<w:spacing w:before="480" w:after="240"/><w:ind w:firstLine="0"/>'
        f'<w:rPr><w:sz w:val="40"/><w:szCs w:val="32"/></w:rPr></w:pPr>'
        f'<w:bookmarkStart w:id="{bm_id}" w:name="{bm_name}"/>'
        f'<w:r><w:rPr><w:rFonts w:ascii="Palatino" w:eastAsia="Palatino Linotype" w:hAnsi="Palatino" w:cs="Palatino Linotype"/><w:sz w:val="24"/><w:szCs w:val="32"/></w:rPr>'
        f'<w:t>{text}</w:t></w:r>'
        f'<w:bookmarkEnd w:id="{bm_id}"/>'
        f'</root>'
    )
    return list(etree.fromstring(xml))

def rebuild_heading(paraId_or_text_match, bm_id, bm_name, expect_text):
    p = None
    for cand in allp:
        if get_full_text(cand).strip() == expect_text:
            p = cand
            break
    assert p is not None, expect_text
    for child in list(p):
        p.remove(child)
    for child in make_heading_children(expect_text, bm_id, bm_name):
        p.append(child)

rebuild_heading(None, '22', 'toc_next', 'Coming Next in the Relativistic Investigation Bureau Series')
rebuild_heading(None, '23', 'toc_review', 'One Last Thing')
log.append('Rebuilt both headings as proper Heading1 with pageBreakBefore and correctly-placed bookmarks')

tree.write("unpacked/word/document.xml", xml_declaration=True, encoding="UTF-8", standalone=True)
print("\n".join(log))
print("saved")

# verify
tree2 = etree.parse("unpacked/word/document.xml")
root2 = tree2.getroot()
def gft2(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))
defined = set()
for bm in root2.iter(f'{{{W}}}bookmarkStart'):
    n = bm.get(f'{{{W}}}name')
    if n: defined.add(n)
referenced = set()
for hl in root2.iter(f'{{{W}}}hyperlink'):
    a = hl.get(f'{{{W}}}anchor')
    if a: referenced.add(a)
print('missing after fix:', referenced - defined)
for p in root2.iter(f'{{{W}}}p'):
    t = gft2(p)
    if t.strip() in ('Coming Next in the Relativistic Investigation Bureau Series', 'One Last Thing'):
        pStyle = p.find(f'{{{W}}}pPr/{{{W}}}pStyle')
        print(t[:40], '-> pStyle:', pStyle.get(f'{{{W}}}val') if pStyle is not None else None)
