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

def set_text(paraId, new_text):
    p = find_p(paraId)
    ts = list(p.iter(f'{{{W}}}t'))
    ts[0].text = new_text
    for extra in ts[1:]:
        extra.text = ""

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

# ===== ITEM 4: Underground woman -- nudge into a deliberate series hook =====
p_uw = find_p('77C8A51E')
insert_uw = make_p('He did not write her down as irrelevant a second time.', p_uw)
p_uw.addnext(insert_uw)
log.append('Item 4: Underground-woman beat given a deliberate-hook closer')

# ===== ITEM 1: explicit established-physics-vs-speculation flag, right after RELATIONS =====
p_relations = find_p('23AE2C91')  # 'RELATIONS.'
flag1 = make_p('Weinstein sat with that for a moment.', p_relations)
flag2 = make_p('“Everything up to this point,” he said quietly, “has been physics. This is not physics. This is a possibility.”', p_relations)
flag3 = make_p('Sherlock did not disagree.', p_relations)
p_relations.addnext(flag1)
flag1.addnext(flag2)
flag2.addnext(flag3)
log.append('Item 1: added explicit physics-vs-speculation flag after RELATIONS')

# ===== ITEM 5: give Trevor a genuine standalone deduction instead of resignation =====
# Replace the "Derek smiled. / Well, that's settled. / Trevor exhaled, relieved. / Good."
# beat with Trevor's own breakthrough, then a revised Derek reaction.
old_derek_smiled = find_p('23C0BA3F')
old_settled = find_p('33B5BA8F')
old_exhaled = find_p('5DC2D837')
old_good = find_p('16ED8EC6')
parent = old_derek_smiled.getparent()
idx = list(parent).index(old_derek_smiled)

trevor_texts = [
    'He paused.',
    '“Unless that’s the point.”',
    'Derek looked up.',
    '“What do you mean?”',
    '“If whoever wrote this knew we couldn’t solve it without the missing information, they weren’t actually asking us to calculate τ. They were showing us that τ is missing. That’s not a question. That’s a diagnosis.”',
    'Derek studied him for a moment.',
    '“That’s rather good, Trevor.”',
    'Trevor looked pleased, and then faintly suspicious of looking pleased.',
    '“Thank you.”',
]
new_ps = [make_p(t, old_derek_smiled) for t in trevor_texts]
for i, np in enumerate(new_ps):
    parent.insert(idx + i, np)
for old_p in (old_derek_smiled, old_settled, old_exhaled, old_good):
    parent.remove(old_p)
log.append('Item 5: gave Trevor a standalone deduction (Ch6, the tau puzzle) replacing his resignation beat')

# ===== ITEM 2: a genuine quiet moment in the Epilogue, no joke immediately after =====
p_quiet = find_p('0EF1B914')
full = get_full_text(p_quiet)
assert full == 'Derek therefore allowed himself one dangerous thought. Perhaps it was over. He was standing in the Bureau that evening when the brass clock appeared on his desk.'
set_text('0EF1B914', 'Derek therefore allowed himself one dangerous thought. Perhaps it was over.')
quiet_texts = [
    'He sat for a while without doing anything useful, which was, for Derek, its own kind of achievement. He thought about the photograph — his own face, on the floor, in a moment that had never happened and now, perhaps, never would. He thought about how close those two things had sat, for a while: never would, and hadn’t happened yet. The distance between them turned out to matter more than he had expected. He did not examine the thought any further than that. Some thoughts, he had found, were better left proper time to settle.',
    'He was standing in the Bureau that evening when the brass clock appeared on his desk.',
]
new_qp = [make_p(t, p_quiet) for t in quiet_texts]
p_quiet.addnext(new_qp[0])
new_qp[0].addnext(new_qp[1])
log.append('Item 2: added a genuine quiet Epilogue beat, undercut by nothing, before the plot resumes')

tree.write("unpacked/word/document.xml", xml_declaration=True, encoding="UTF-8", standalone=True)
print("\n".join(log))
print("saved")

# ===== verification =====
tree2 = etree.parse("unpacked/word/document.xml")
root2 = tree2.getroot()
def gft2(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))
checks = [
    'did not write her down as irrelevant a second time',
    'This is not physics. This is a possibility',
    'Unless that’s the point',
    'That’s rather good, Trevor',
    'proper time to settle',
]
for c in checks:
    found = any(c in gft2(p) for p in root2.iter(f'{{{W}}}p'))
    print(c[:40], '->', 'FOUND' if found else 'MISSING')
