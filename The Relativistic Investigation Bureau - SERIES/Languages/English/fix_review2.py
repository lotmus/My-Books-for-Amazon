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

# ===== Priority 3: trim the "oversubscribed" digression (~20%) while keeping the
# already-praised "master clock" line and the strong closing line intact =====
p_tabitha_scene = find_p('78BF4D12')
old = get_full_text(p_tabitha_scene)
assert old.endswith('was not the same as kindness.')
new = (
    '“Exactly,” Tabitha said. “The universe doesn’t keep a master clock. It only keeps local ones. '
    'People keep inventing the master clock. The universe never asked for one.” '
    'Derek, for reasons he chose not to examine, found himself watching Tabitha rather than the clock. '
    'Her presence made the situation feel slightly more manageable, which he decided was an unhelpful '
    'development. He filed the observation under ‘later,’ which was, by now, a considerably overstuffed '
    'drawer. The universe was consistent on this point as well. Consistency, Derek had noticed, was not '
    'the same as kindness.'
)
set_text('78BF4D12', new)
log.append('Priority 3: trimmed the "later" digression by roughly 20%, kept the two strongest lines')

# ===== Priority 1: a grounding recap beat at the start of Chapter 9 =====
anchor_ch9 = find_p('0EB1C419')  # 'The first important observation was that Derek Gent...'
recap = make_p(
    'Derek took stock. He had a murder that had not happened, a clock that disagreed with every other '
    'clock in London, a suspect who was also the victim, and a growing suspicion that the actual crime '
    'scene was spacetime itself. Four facts. No arrests. One reassuringly ordinary cucumber, for scale.',
    anchor_ch9
)
anchor_ch9.addnext(recap)
log.append('Priority 1: added a grounding case-status recap at the start of Chapter 9')

# ===== Priority 2: subvert the smile pattern at the "other Derek" first-sighting =====
anchor_smile = find_p('2C55E7A9')  # 'The other Derek tipped his head back. Their eyes met. The other Derek smiled.'
subvert = make_p('Derek did not smile back.', anchor_smile)
anchor_smile.addnext(subvert)
log.append('Priority 2: added a pattern-subversion beat at the other-Derek reveal')

# ===== Priority 5: clarify Tabitha's stake by paying off her Chapter 1 setup =====
anchor_tabitha = find_p('4B5E5B38')  # 'Which was, in retrospect, the first sign that this was going to be a problem.'
clarity = make_p(
    'He remembered, belatedly, that she had once asked a single question about simultaneous events at a '
    'Bureau function and left before anyone could answer it properly. He suspected, uneasily, that she had '
    'already worked out the answer herself.',
    anchor_tabitha
)
anchor_tabitha.addnext(clarity)
log.append('Priority 5: paid off Tabitha’s Chapter 1 setup to clarify her stake in the mystery')

tree.write("unpacked/word/document.xml", xml_declaration=True, encoding="UTF-8", standalone=True)
print("\n".join(log))
print("saved")

# ===== verification =====
tree2 = etree.parse("unpacked/word/document.xml")
root2 = tree2.getroot()
def gft2(p):
    return "".join(t.text or "" for t in p.iter(f'{{{W}}}t'))
checks = [
    'overstuffed drawer',
    'One reassuringly ordinary cucumber, for scale',
    'Derek did not smile back',
    'already worked out the answer herself',
]
for c in checks:
    found = any(c in gft2(p) for p in root2.iter(f'{{{W}}}p'))
    print(c[:40], '->', 'FOUND' if found else 'MISSING')
