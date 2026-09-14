# -*- coding: utf-8 -*-
from lxml import etree
import itertools

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W14 = 'http://schemas.microsoft.com/office/word/2010/wordml'

tree = etree.parse("unpacked/word/document.xml")
root = tree.getroot()

def get_full_text(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))

allp = list(root.iter(f'{{{W}}}p'))

SYNONYMS = {
    '“Apparently.”': ['“So it appears.”', '“Evidently.”', '“It would seem so.”'],
    '“Good.”': ['“Right.”', '“Fine.”', '“Excellent.”'],
    '“Exactly.”': ['“Precisely.”', '“Quite.”', '“Just so.”'],
    '“Possibly.”': ['“Perhaps.”', '“Maybe.”', '“Could be.”'],
    '“Fair.”': ['“Fair enough.”', '“True.”'],
    '“Again?”': ['“Still?”'],
}

log = []
total_varied = 0
for target, syns in SYNONYMS.items():
    locs = [p for p in allp if get_full_text(p).strip() == target]
    cycle = itertools.cycle(syns)
    varied_here = 0
    for i, p in enumerate(locs):
        if i % 4 == 3:  # vary every 4th occurrence (~25%), spread evenly
            new_text = next(cycle)
            ts = list(p.iter(f'{{{W}}}t'))
            ts[0].text = new_text
            for extra in ts[1:]:
                extra.text = ""
            varied_here += 1
    log.append(f'{target}: {len(locs)} total, varied {varied_here}')
    total_varied += varied_here

tree.write("unpacked/word/document.xml", xml_declaration=True, encoding="UTF-8", standalone=True)
print("\n".join(log))
print(f"Total varied: {total_varied}")
print("saved")

# ===== verification with fresh reload =====
tree2 = etree.parse("unpacked/word/document.xml")
root2 = tree2.getroot()
def gft2(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))
allp2 = list(root2.iter(f'{{{W}}}p'))
remaining = {}
for target in SYNONYMS:
    remaining[target] = sum(1 for p in allp2 if gft2(p).strip() == target)
print()
print("remaining counts after fix:", remaining)
