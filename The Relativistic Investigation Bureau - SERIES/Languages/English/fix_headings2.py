# -*- coding: utf-8 -*-
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W14 = 'http://schemas.microsoft.com/office/word/2010/wordml'

tree = etree.parse("unpacked/word/document.xml")
root = tree.getroot()

def get_full_text(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))

def find_by_paraid(paraId):
    m = root.findall(f'.//{{{W}}}p[@{{{W14}}}paraId="{paraId}"]')
    assert len(m) == 1, paraId
    return m[0]

log = []
allp = list(root.iter(f'{{{W}}}p'))

# ===== Remove the misplaced bookmarkStart/End markers by NAME/ID, wherever they are =====
def strip_bookmark(name, expected_id):
    removed_start = removed_end = 0
    for p in allp:
        for bm in list(p.iter(f'{{{W}}}bookmarkStart')):
            if bm.get(f'{{{W}}}name') == name:
                assert bm.get(f'{{{W}}}id') == expected_id
                bm.getparent().remove(bm)
                removed_start += 1
        for bm in list(p.iter(f'{{{W}}}bookmarkEnd')):
            if bm.get(f'{{{W}}}id') == expected_id:
                bm.getparent().remove(bm)
                removed_end += 1
    return removed_start, removed_end

r1 = strip_bookmark('toc_next', '22')
r2 = strip_bookmark('toc_review', '23')
log.append(f'Stripped old toc_next markers: {r1}, toc_review markers: {r2}')

# ===== Rebuild ONLY the two specific back-matter heading paragraphs, targeted by their exact paraId =====
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

def rebuild_heading(paraId, bm_id, bm_name, expect_text):
    p = find_by_paraid(paraId)
    actual = get_full_text(p).strip()
    assert actual == expect_text, (actual, expect_text)
    for child in list(p):
        p.remove(child)
    for child in make_heading_children(expect_text, bm_id, bm_name):
        p.append(child)

rebuild_heading('11F7D61E', '22', 'toc_next', 'Coming Next in the Relativistic Investigation Bureau Series')
rebuild_heading('4F76105D', '23', 'toc_review', 'One Last Thing')
log.append('Rebuilt the two REAL back-matter headings (by paraId) as proper Heading1')

tree.write("unpacked/word/document.xml", xml_declaration=True, encoding="UTF-8", standalone=True)
print("\n".join(log))
print("saved")

# ===== verification with fresh reload =====
tree2 = etree.parse("unpacked/word/document.xml")
root2 = tree2.getroot()
def gft2(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))
def pstyle2(p):
    ps = p.find(f'{{{W}}}pPr/{{{W}}}pStyle')
    return ps.get(f'{{{W}}}val') if ps is not None else None

allp2 = list(root2.iter(f'{{{W}}}p'))
print()
print("=== all paragraphs matching the two target texts, with index + style ===")
for i, p in enumerate(allp2):
    t = gft2(p).strip()
    if t in ('Coming Next in the Relativistic Investigation Bureau Series', 'One Last Thing'):
        print(i, pstyle2(p), repr(t[:50]))

defined = set()
for bm in root2.iter(f'{{{W}}}bookmarkStart'):
    n = bm.get(f'{{{W}}}name')
    if n: defined.add(n)
referenced = set()
for hl in root2.iter(f'{{{W}}}hyperlink'):
    a = hl.get(f'{{{W}}}anchor')
    if a: referenced.add(a)
print()
print('missing bookmarks:', referenced - defined)
print('bookmarks:', len(defined), 'hyperlinks:', len(referenced))
