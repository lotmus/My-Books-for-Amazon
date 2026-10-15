"""EE Book 2 (Circuits, Components, and Control): merge split topics (filters 6+21, resistors 7+22,
capacitors 8+23, inductors 9+20), renumber 24-32 -> 20-28, then warm-up content, new diagrams."""
import sys, re, docx
sys.path.insert(0, '../common')
from eedoc import *
from eebuild import *
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src); P = body_ps(d)
GUEST = {21: 6, 22: 7, 23: 8, 20: 9}
NEWSEC = {21: 'Active Filter Design: Sallen-Key and Multiple Feedback', 22: 'Resistors in Practice: Heat, Drift, and Pulses',
          23: 'Capacitors in Practice: Decoupling and Real Impedance', 20: 'Inductors in Practice: Reading the Datasheet'}
ch = chapters(d)
def parts(n):
    h, nxt = ch[n]; s = seg(h, nxt)
    pp = next(i for i, e in enumerate(s) if sty(e) == 'Heading2' and ptext(e).strip() == 'Practice Problems')
    secs = [e for e in s[:pp] if sty(e) == 'Heading2' and re.match(r'%d\.\d+ ' % n, ptext(e))]
    figs = [e for e in s if re.match(r'Figure %d\.\d+ —' % n, ptext(e))]
    wes = [e for e in s if re.match(r'Worked Example %d\.\d+' % n, ptext(e))]
    lis = [e for e in s[pp+1:] if sty(e) == 'ListParagraph']
    return dict(h=h, body=s[:pp], pph=s[pp], lis=lis, rest=[e for e in s[pp+1:] if e not in lis], secs=secs, figs=figs, wes=wes)
I = {n: parts(n) for n in list(GUEST) + list(GUEST.values())}
OFF = {g: dict(sec=len(I[hst]['secs']) + 1, fig=len(I[hst]['figs']), we=len(I[hst]['wes']), prob=len(I[hst]['lis'])) for g, hst in GUEST.items()}
def numid(p):
    n = p.find('.//' + W('numId')); return n
# ---- merge
for g, hst in GUEST.items():
    G, H = I[g], I[hst]
    gh = G['h']; pPr = gh.find(W('pPr'))
    pPr.find(W('pStyle')).set(W('val'), 'Heading2')
    for t in list(gh.iter(W('t')))[1:]: t.text = ''
    list(gh.iter(W('t')))[0].text = '%d.%d %s' % (hst, OFF[g]['sec'], NEWSEC[g])
    insert_before(H['pph'], [gh] + G['body'])
    hid = numid(H['lis'][0]).get(W('val'))
    last = H['lis'][-1]
    for li in G['lis']: numid(li).set(W('val'), hid)
    insert_after(last, G['lis'])
    G['pph'].getparent().remove(G['pph'])
    for e in G['rest']:
        if e.tag == W('p') and not ptext(e).strip() and not e.findall('.//' + qn('w:drawing')): e.getparent().remove(e)
        else: insert_after(G['lis'][-1], [e])
# ---- TOC, Appendix B solutions, Appendix D summaries (old numbers still in text)
ps = body_ps(d)
toc_end = next(i for i, p in enumerate(ps) if sty(p) == 'Heading1' and ptext(p).startswith('Chapter 1 —'))
for g in GUEST:
    for p in ps[:toc_end]:
        if re.match(r'Chapter %d —' % g, ptext(p)): p.getparent().remove(p)
ps = body_ps(d)
def h2block(title):
    i = next(k for k, p in enumerate(ps) if sty(p) == 'Heading2' and ptext(p).strip() == title)
    j = next(k for k in range(i+1, len(ps)) if sty(ps[k]).startswith('Heading'))
    return ps[i], [p for p in ps[i+1:j] if ptext(p).strip()]
for g, hst in GUEST.items():
    gh, gb = h2block('Chapter %d Solutions' % g); hh, hb = h2block('Chapter %d Solutions' % hst)
    for p in gb: re_sub_para(p, r'^(\d+)\.', lambda m, o=OFF[g]['prob']: '%d.' % (int(m.group(1)) + o))
    insert_after(hb[-1], gb); gh.getparent().remove(gh)
    gh, gb = h2block('Chapter %d' % g); hh, hb = h2block('Chapter %d' % hst)
    insert_after(hb[-1], gb); gh.getparent().remove(gh)
    ps = body_ps(d)
# ---- renumber
def CH(n): return GUEST.get(n, n if n <= 19 else (n - 4 if 24 <= n <= 32 else n))
def REF(n, k, kw):
    if n in GUEST:
        o = OFF[n]; kw = kw.strip()
        k += o['fig'] if kw.startswith('Fig') else o['we'] if kw.startswith(('Worked', 'Example')) else o['sec']
    return '%d.%d' % (CH(n), k)
ps = body_ps(d)
also = max(i for i, p in enumerate(ps) if ptext(p).startswith('Also by Lothar'))
org = [p for p in ps[:toc_end] if ptext(p).startswith(('Chapters 1–2 build', 'Chapter 10 introduces the control loop'))]
renumber([p for p in ps[:also] if p not in org], CH, REF)
ORG = ["Chapters 1–2 build the vocabulary shared by every later chapter: bias points, headroom, and small-signal behavior for analog circuits, and logic levels and noise margins for digital ones. Chapters 3–4 develop digital design specifically, from Boolean algebra through sequential circuits with memory. Chapter 5 introduces the operational amplifier as an ideal building block, in the same spirit Book 1 used for the resistor, capacitor, and inductor. Chapter 6 generalizes Book 1's filter and resonance results into a full filter-design vocabulary, passive and active, and carries it through to Sallen-Key and multiple-feedback designs built from standard parts. Chapters 7–9 return to the resistor, capacitor, and inductor themselves as real, physical parts: first their types, tolerances, ratings, and parasitics, then the practical side, from heat, drift, and pulse ratings to decoupling, real impedance, and reading an inductor datasheet.",
       "Chapter 10 introduces the control loop that runs underneath a robot model. Chapters 11–16 return to the op-amp with real numbers: feedback as a quantitative tool, followers and capacitive loads, bandwidth and slew rate, noise, DC errors, and comparators. Chapters 17–19 build classical control on that foundation, from plant and controller through PID and lead-lag compensation to the digital loop and its sampling delay. Chapters 20–24 add five building blocks that join the book's two halves: the instrumentation amplifier, state feedback with observers, the sample-and-hold circuit, the voltage reference, and the H-bridge motor drive written as a plant for the loops of Chapters 17–19. Chapters 25–28 complete both halves: the root locus and the stability margins and sensitivity peak on the control side, and oscillators and digital timing with metastability on the circuit side."]
for p, t in zip(org, ORG):
    for x in list(p.iter(W('t')))[1:]: x.text = ''
    list(p.iter(W('t')))[0].text = t
FIX = [('Chapter 6 built the vocabulary of filters:', 'The first half of this chapter built the vocabulary of filters:'),
 ('Chapter 7 gave the real resistor', 'Sections 7.1 to 7.4 gave the real resistor'),
 ('Chapter 8 showed that a real capacitor', 'Section 8.3 showed that a real capacitor'),
 ('Chapters 8 and 6 reserve them', 'this chapter and Chapter 6 reserve them'),
 ('Chapter 9 introduced the real inductor:', 'Sections 9.1 to 9.3 introduced the real inductor:'),
 ('Chapter 9 checked a peak', 'Section 9.2 checked a peak'), ("Chapter 9's toroid", "Section 9.1's toroid"),
 ('introduced in Chapter 9,', 'introduced in Section 9.3,')]
for p in body_ps(d):
    for x, y in FIX:
        if x in ptext(p): re_sub_para(p, re.escape(x), lambda m, y=y: y)
# ---- new figures (placed before the warm-up text), sequential figure numbering, warm-up content
from content_b2 import C, FIGS
refs = [(anchor(d, a), f, cap, alt) for a, f, cap, alt in FIGS]
figures(d, refs, 'fig')
mp = renumber_figures(d)
counts = warm(d, C)
d.save(out)
print('merged', OFF, counts, 'figures', len(refs), 'moved', {k: v for k, v in mp.items() if k != v})
