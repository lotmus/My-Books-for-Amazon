# -*- coding: utf-8 -*-
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

# ===== Item 6: trim the redundant mechanical-properties list (Ch6) from 6 pairs to 3 =====
to_remove = ['3B0DF440', '21601B89', '7F0D19E7', '34A7A988', '1F1F8E91', '18AD0115']
expected_texts = ['Spring tension.', 'Yes.', 'Temperature.', 'Yes.', 'Position.', 'Yes.']
for pid, expected in zip(to_remove, expected_texts):
    p = find_p(pid)
    actual = get_full_text(p).strip().strip('“”')
    assert actual == expected, (pid, actual, expected)
    p.getparent().remove(p)
log.append('Item 6: trimmed the mechanical-properties list from 6 pairs to 3 (Ch6)')

tree.write("unpacked/word/document.xml", xml_declaration=True, encoding="UTF-8", standalone=True)
print("\n".join(log))
print("saved")

# verify
tree2 = etree.parse("unpacked/word/document.xml")
root2 = tree2.getroot()
def gft2(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))
still_there = any('Spring tension' in gft2(p) for p in root2.iter(f'{{{W}}}p'))
print('Spring tension still present (should be False):', still_there)
gp_present = any('Gravitational potential' in gft2(p) for p in root2.iter(f'{{{W}}}p'))
print('Gravitational potential still present (should be True):', gp_present)
