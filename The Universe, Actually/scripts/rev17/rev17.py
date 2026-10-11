"""The Universe, Actually REV16 -> REV17 (11 Oct 2026).
Adds: a hook at the start of each of the 76 chapters, a 'Questions to Keep Asking' block at the end of each, and 40 computed diagrams.
Usage (from scripts/rev17):  python rev17.py ../../The_Universe_Actually__REV16.docx ../../The_Universe_Actually__REV17.docx
Figures are drawn first by figs_a.py ... figs_e.py (they write fig/*.png and fig/registry.json)."""
import sys, os, re, json, copy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rev16'))
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
import docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from engine import newpara, runs_of, base_rpr, mkrun, sub
from chapters17_b import CH
W = lambda t: qn('w:' + t)
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src); body = d.element.body
text = lambda p: ''.join(t.text or '' for t in p.iter(W('t')))
def style(p):
    s = p.find(W('pPr')); s = s.find(W('pStyle')) if s is not None else None
    return s.get(W('val')) if s is not None else ''
kids = [e for e in body.iterchildren() if e.tag == W('p')]
# template: first ordinary body paragraph (non-empty, no style) after chapter 1
tpl = next(p for p in kids if style(p) == '' and len(text(p)) > 150)
chap = {}   # n -> h2 element
for e in kids:
    if style(e) == 'Heading2':
        m = re.match(r'(\d+)\. ', text(e))
        if m: chap[int(m.group(1))] = e
assert len(chap) == 76, len(chap)
def norm(t): return re.sub(r'[^a-z0-9]', '', t.lower().replace('’', "'"))
# ---------- chapter ranges (before any insertion)
order = [e for e in kids]
idx = {id(e): i for i, e in enumerate(order)}
def chapter_end(h):
    i = idx[id(h)] + 1
    while i < len(order) and style(order[i]) not in ('Heading1', 'Heading2'): i += 1
    return order[i - 1]            # last element belonging to the chapter
ends = {n: chapter_end(h) for n, h in chap.items()}
# ---------- figure anchors
h3 = {}
for e in kids:
    if style(e) == 'Heading3': h3.setdefault(norm(text(e)), e)
reg = json.load(open('fig/registry.json', encoding='utf-8'))
OVERRIDE = {'a08_blackbody': ('LEAD', 5, 1), 'e04_energy_balance': ('H3', 'Climate Science: Definitions and Methods'), 'e08_carbon_budget': ('H3', 'Paleoclimate, Feedbacks and Sea Level'),
            'e05_shannon': ('H3', 'Information, Channels and Capacity'), 'e03_logistic_growth': ('H3', 'Ecology'), 'e02_action_potential': ('H3', 'The Nervous System'),
            'e06_earth_layers': ('LEAD', 56, 1), 'e07_dna': ('H3', 'The Double Helix'), 'e01_popgen': ('H3', 'Population Genetics'), 'd10_calendar': ('H3', 'The Cosmic Calendar'),
            'd09_entropy': ('H3', 'Entropy'), 'd08_budget': ('H3', 'The Dark Sector at a Glance')}
def first_para_after(h):
    i = idx[id(h)] + 1
    while i < len(order) and style(order[i]) == '' and not len(text(order[i]).strip()): i += 1
    return order[i]
def add_figure(after, caption, alt, title):
    ip = d.add_paragraph(); ip.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ip.add_run().add_picture(title, width=Inches(6.0))
    for dp in ip._p.iter('{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr'):
        dp.set('descr', alt); dp.set('title', caption[:80])
    cp = newpara(tpl, '*Figure @@. ' + caption.replace('*', '') + '*')
    ppr = cp.find(W('pPr'))
    if ppr is None: ppr = OxmlElement('w:pPr'); cp.insert(0, ppr)
    for x in ppr.findall(W('jc')): ppr.remove(x)
    jc = OxmlElement('w:jc'); jc.set(W('val'), 'center'); ppr.append(jc)
    kn = OxmlElement('w:keepNext')
    after.addnext(ip._p); ip._p.addnext(cp)
    ipp = ip._p.find(W('pPr'))
    if ipp is None: ipp = OxmlElement('w:pPr'); ip._p.insert(0, ipp)
    ipp.insert(0, kn)
    return cp
placed = []
for name, r in reg.items():
    ov = OVERRIDE.get(name)
    if ov and ov[0] == 'LEAD':
        h = chap[ov[1]]; i = idx[id(h)] + 1; paras = []
        while i < len(order) and style(order[i]) not in ('Heading1', 'Heading2', 'Heading3'):
            if len(text(order[i]).strip()) > 40: paras.append(order[i])
            i += 1
        anchor = paras[ov[2]]
    else:
        title = ov[1] if ov else r['anchor']
        h = h3.get(norm(title))
        if h is None: print('MISSING anchor', name, title); continue
        anchor = first_para_after(h)
        # skip a leading hook-like short paragraph; insert after the first full paragraph
        j = idx[id(anchor)]
        while j < len(order) and style(order[j]) == '' and len(text(order[j]).strip()) < 60 and style(order[j + 1]) == '': j += 1
        anchor = order[j]
    add_figure(anchor, r['caption'], r['alt'], r['file']); placed.append(name)
print('figures placed', len(placed))
# ---------- hooks and questions
rpr0 = base_rpr(runs_of(tpl)[0])
def bold_run(txt):
    r = mkrun(txt, rpr0); rp = r.find(W('rPr'))
    rp.insert(0, OxmlElement('w:b')); return r
def qpara(txt, label=None):
    """paragraph whose first question sentence (or a fixed label) is bold"""
    if label is None:
        i = txt.find('? ')
        lead, rest = (txt[:i + 1], txt[i + 2:]) if i > 0 else (txt, '')
    else:
        lead, rest = label, txt
    p = newpara(tpl, rest if rest else ' ')
    first = [c for c in p if c.tag == W('r')][0]
    first.addprevious(bold_run(lead + (' ' if rest else '')))
    if not rest: p.remove(first)
    return p
for n in range(1, 77):
    c = CH[n]
    hook = newpara(tpl, '*' + c['hook'] + '*'); chap[n].addnext(hook)
    end = ends[n]
    head = newpara(tpl, 'Questions to Keep Asking')
    hr = [x for x in head if x.tag == W('r')][0]; hr.find(W('rPr')).insert(0, OxmlElement('w:b'))
    hp = head.find(W('pPr'))
    if hp is None: hp = OxmlElement('w:pPr'); head.insert(0, hp)
    for x in hp.findall(W('spacing')) + hp.findall(W('keepNext')): hp.remove(x)
    hp.append(OxmlElement('w:keepNext'))
    sp = OxmlElement('w:spacing'); sp.set(W('before'), '280'); sp.set(W('after'), '60'); hp.append(sp)
    p1 = qpara(c['how']); p2 = qpara(c['change']); p3 = qpara(c['tryit'], 'Try it yourself.')
    a = end
    for e in (head, p1, p2, p3): a.addnext(e); a = e
# ---------- renumber figures in reading order
cap_re = re.compile(r'^Figure (\d+|@@)\. ')
els = [e for e in body.iterchildren() if e.tag == W('p')]
oldmap = {}; k = 0
for e in els:
    t = text(e); m = cap_re.match(t)
    if m:
        k += 1
        if m.group(1) != '@@': oldmap[m.group(1)] = str(k)
        sub(e, m.group(0), 'Figure %d. ' % k)
for e in els:
    t = text(e)
    if cap_re.match(t): continue
    for m in sorted(set(re.findall(r'Figure (\d+)', t)), reverse=True):
        if m in oldmap and oldmap[m] != m: sub(e, 'Figure ' + m, 'Figure ' + oldmap[m])
print('figures total', k, 'map', oldmap)
d.save(out); print('saved', out)
