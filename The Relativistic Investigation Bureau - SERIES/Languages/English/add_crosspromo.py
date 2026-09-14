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

def make_p(text, template_p):
    new_p = etree.Element(f'{{{W}}}p')
    pPr_t = template_p.find(f'{{{W}}}pPr')
    if pPr_t is not None:
        new_p.append(copy.deepcopy(pPr_t))
    r_t = template_p.find(f'{{{W}}}r')
    rPr_t = r_t.find(f'{{{W}}}rPr') if r_t is not None else None
    new_r = etree.SubElement(new_p, f'{{{W}}}r')
    if rPr_t is not None:
        new_r.append(copy.deepcopy(rPr_t))
    if text:
        new_t = etree.SubElement(new_r, f'{{{W}}}t')
        new_t.text = text
    return new_p

anchor = find_p('1D615829')  # "The real author, Lothar J. Musiol..."
template = anchor

spacer = make_p(None, template)
line = make_p(
    'Readers who would like the mathematics behind Derek’s cases explained without any of the murder can find it in Musiol’s nonfiction Physics, Actually series — Volume 1, Motion, Forces, Time, and Relativity, covers the relativity in these pages properly, equations and all, and considerably fewer clocks are harmed in the process.',
    template
)

anchor.addnext(spacer)
spacer.addnext(line)

tree.write("unpacked/word/document.xml", xml_declaration=True, encoding="UTF-8", standalone=True)
print("Cross-promotion line inserted after the About the Author section")

# verify
tree2 = etree.parse("unpacked/word/document.xml")
root2 = tree2.getroot()
def gft2(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))
found = any('Physics, Actually series' in gft2(p) for p in root2.iter(f'{{{W}}}p'))
print('verified after reload:', found)
