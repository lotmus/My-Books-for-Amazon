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
    new_t = etree.SubElement(new_r, f'{{{W}}}t')
    new_t.text = text
    return new_p

log = []

# ===== Item 7: a Derek/Penny beat (family trust, non-romantic -- she is his cousin) =====
anchor = find_p('6A55E68A')  # 'It read 11:17. Derek stared at Penny. Penny gazed at the clock.'
beat = make_p('Neither of them reached for a notebook. After the year they’d had, some things no longer needed writing down. They had simply become family shorthand — the kind their grandmother would have recognised, and approved of, in her own alarming way.', anchor)
anchor.addnext(beat)
log.append('Item 7: added a Derek/Penny family-history beat in the Epilogue')

tree.write("unpacked/word/document.xml", xml_declaration=True, encoding="UTF-8", standalone=True)
print("\n".join(log))
print("saved")

tree2 = etree.parse("unpacked/word/document.xml")
root2 = tree2.getroot()
def gft2(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))
found = any('family shorthand' in gft2(p) for p in root2.iter(f'{{{W}}}p'))
print('verified:', found)
