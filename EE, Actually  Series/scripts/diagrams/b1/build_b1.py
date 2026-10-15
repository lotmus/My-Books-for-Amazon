"""EE Book 1 (Foundations of Electronics): Smith chart chapter to the end of Part III, renumbering,
warm-up content (hooks, where-you-meet, From the Bench, What You'll Actually Use), new diagrams."""
import sys, re, copy, docx
sys.path.insert(0, '../common')
from eedoc import *
from content_b1 import C
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src); body = d.element.body
P = body_ps(d)
orig = list(P)
H1 = [i for i, p in enumerate(P) if sty(p) == 'Heading1']
def h1(txt): return next(P[i] for i in H1 if ptext(P[i]).startswith(txt))
# ---- figure anchors captured on the original paragraphs
def after_eq(i):
    j = i
    if len(ptext(P[i+1])) < 60 and sty(P[i+1]) == '' and ptext(P[i+1]).strip(): j = i + 1
    return P[j]
FIGS = [
 (127, 'b1_conductor_insulator.png', 'Figure 1.1 — Why copper conducts and glass doesn\u2019t: in a metal the outer electrons roam freely between the ions; in an insulator each one stays tied to its own atom.',
  'Two boxes side by side. Left, a metal: a grid of positive ions with small blue electrons scattered between them, each with an arrow showing random motion; caption, outer electrons wander freely between ions. Right, an insulator: the same grid of positive ions, but each electron sits on a dashed orbit around its own ion; caption, each electron stays tied to its own atom.'),
 (365, 'b1_color_code.png', 'Figure 7.2 — Reading a resistor\u2019s color bands: yellow, violet, red, gold means 4, 7, two zeros and ±5%, so 4.7 kΩ. Start from the end where the bands bunch together; the tolerance band comes last.',
  'A through-hole resistor with four bands: yellow (first digit 4), violet (second digit 7), red (multiplier times 100) and, after a gap, gold (tolerance plus or minus 5 percent). Text above: 4 7 times 100 equals 4700 ohms, 4.7 kilohms, plus or minus 5 percent, so anything from 4.465 to 4.935 kilohms passes.'),
 (425, 'b1_led.png', 'Figure 8.2 — The resistor that saves the LED: it takes the 3 V the LED doesn\u2019t need and sets the current at about 9 mA, plenty for an indicator.',
  'Schematic: a 5.0 V source, positive terminal at the top, feeds a 330 ohm resistor, labeled drops 3.0 V, and then a red LED pointing downward (anode at the top) with forward voltage about 2.0 V, returning to the negative terminal. An arrow marks current I flowing clockwise. Below: I equals 5.0 V minus 2.0 V, divided by 330 ohms, about 9 milliamps.'),
 (450, 'b1_charge_in_B.png', 'Figure 9.1 — A positive charge in a field pointing out of the page goes round clockwise. The force always points at the center, so it bends the path but never changes the speed.',
  'A grid of dots, each a small circle with a center dot, meaning a magnetic field B pointing out of the page. A positive charge at the top of a dashed circle moves to the right (velocity v); a red arrow from it points down toward the center, labeled force F equals q v cross B. An arrow on the circle shows clockwise motion. Notes: positive charge clockwise, negative charge counterclockwise, radius r equals m v over q B.'),
 (572, 'b1_em_wave.png', 'Figure 12.1 — A light or radio wave: the electric field (red) and magnetic field (blue) rise and fall together, at right angles to each other and to the direction of travel.',
  'Three-dimensional sketch of a plane wave moving to the right along an axis. The electric field, in red, oscillates vertically; the magnetic field, in blue, oscillates horizontally, in phase with the electric field. A bar above marks one wavelength, lambda equals c over f, and an arrow at the right says travels at c.'),
 (880, 'b1_db_ladder.png', 'Figure 19.2 — A decibel cheat sheet worth memorizing: +3 dB is about double the power, +10 dB is ten times, and because power goes as voltage squared, +6 dB doubles the voltage.',
  'A ladder of decibel values, not to scale, from minus 30 to plus 30 dB, with the matching power ratio above and voltage ratio below: minus 30 dB, power 1/1000, voltage 0.032; minus 20, 1/100, 0.1; minus 10, 1/10, 0.32; minus 6, 1/4, 0.5; minus 3, 1/2, 0.71; 0 dB, 1, 1; plus 3, 2, 1.41; plus 6, 4, 2; plus 10, 10, 3.16; plus 20, 100, 10; plus 30, 1000, 31.6. Formula: dB equals 10 log of the power ratio, equals 20 log of the voltage ratio.'),
 (1379, 'b1_thevenin_line.png', 'Figure 30.2 — A real source on one graph: open-circuit voltage at the top, short-circuit current at the right, and a straight line between them. A load equal to R_Th (here 2 kΩ) gets the most power out, at the price of wasting as much again inside the source.',
  'Graph of terminal voltage in volts against load current in milliamps. A blue line falls from 10 V at zero current (the open-circuit Thevenin voltage) to zero volts at 5 mA (the Norton short-circuit current). A dashed 2 kilohm load line rises from the origin. They cross at 2.5 mA and 5 V, marked as the operating point where the load equals the Thevenin resistance and receives the maximum power, 12.5 milliwatts.'),
 (1498, 'b1_rl_phase.png', 'Figure 34.1 — In a series RL circuit the current lags the voltage. With ωL = √3·R the lag is exactly 60°, one sixth of a period, and a two-channel scope shows it directly.',
  'Two sine waves over two periods. The blue source voltage peaks at a quarter period; the smaller red current peaks one sixth of a period later. A double arrow between the peaks is labeled 60 degrees equals one sixth of a period. Note: series RL with omega L equal to root 3 times R, tan phi equals omega L over R, phi equals 60 degrees.'),
 (1528, 'b1_inst_power.png', 'Figure 35.1 — Power as it actually flows. With a resistor (left) the product v·i never goes negative. With the current lagging by 60° (right) part of every cycle sends energy back to the source, and the average power halves.',
  'Two panels over two periods, normalized. Left, power factor 1: voltage and current in phase, and their product, shaded orange, is always positive, with an average of 0.5. Right, power factor 0.5 with the current lagging 60 degrees: the shaded product dips below zero for part of each cycle, marking energy flowing back to the source, and the dashed average line sits at 0.25.'),

 (1618, 'b1_diode_tangent.png', 'Figure 38.1 — The trick behind the next book: zoom in far enough on any smooth curve and it looks straight. Near its 1 mA bias point this diode behaves like a 26 Ω resistor for small signals.',
  'Graph of diode current in milliamps against diode voltage from 0.55 to 0.72 volts. A blue exponential curve rises steeply past about 0.65 volts. A black dot marks the bias point at 1 milliamp and about 0.65 volts. A red dashed tangent line touches the curve there; its slope is one over r d. Text: r d equals V T over I D, about 26 millivolts over 1 milliamp, which is 26 ohms.'),
]
SKIP = {450: 1, 572: 1, 880: 1, 1498: 1}
fig_refs = [(P[i + SKIP.get(i, 0)], f, c, a) for i, f, c, a in FIGS]
# ---- 1. move the Smith chart chapter (old 24) to just before old Chapter 38, and its TOC line, solutions and summary
def block(start_txt, end_txt, within=None):
    ps = body_ps(d)
    a = next(i for i, p in enumerate(ps) if ptext(p).startswith(start_txt) and (within is None or within(i, p)))
    b = next(i for i in range(a+1, len(ps)) if ptext(ps[i]).startswith(end_txt))
    return ps[a:b], ps[b]
H1set = lambda i, p: sty(p) == 'Heading1'
smith, cal = block('Chapter 24 — The Smith Chart', 'Chapter 25 — Calculus', H1set)
ch38 = h1('Chapter 38 — Where This Series Goes Next')
# body elements between, including any non-paragraph elements: move every sibling from smith[0] up to cal
els = []; e = smith[0]
while e is not cal: els.append(e); e = e.getnext()
for e in els: ch38.addprevious(e)
# TOC
ps = body_ps(d)
toc24 = next(p for p in ps[:120] if ptext(p).startswith('Chapter 24 — The Smith'))
toc38 = next(p for p in ps[:120] if ptext(p).startswith('Chapter 38 —'))
toc38.addprevious(toc24)
# Appendix B solutions block
sol, _ = block('Chapter 24 Solutions', 'Chapter 25 Solutions')
ps = body_ps(d)
nxt = next((p for p in ps if ptext(p).startswith('Chapter 38 Solutions')), None)
if nxt is None:  # no ch38 solutions: put before the Appendix C heading
    nxt = next(p for p in ps if sty(p) == 'Heading1' and ptext(p).startswith('Appendix C'))
for e in sol: nxt.addprevious(e)
# Appendix D summary
ps = body_ps(d)
appD = next(i for i, p in enumerate(ps) if sty(p) == 'Heading1' and ptext(p).startswith('Appendix D'))
s24 = next(i for i in range(appD, len(ps)) if ptext(ps[i]).startswith('Chapter 24 — The Smith'))
summ = [ps[s24], ps[s24+1]]
s38 = next(p for p in ps[appD:] if ptext(p).startswith('Chapter 38 —'))
for e in summ: s38.addprevious(e)
# Appendix A: Smith chart formulas from Part II to the end of Part III
ps = body_ps(d)
a = next(i for i, p in enumerate(ps) if sty(p) == 'Heading3' and ptext(p).startswith('Smith Chart and Impedance Matching'))
b = next(i for i in range(a+1, len(ps)) if sty(ps[i]).startswith('Heading'))
blk = ps[a:b]
appB = next(i for i, p in enumerate(ps) if sty(p) == 'Heading1' and ptext(p).startswith('Appendix B'))
j = appB - 1
while not ptext(ps[j]).strip(): j -= 1
insert_after(ps[j], blk)
# ---- 2. renumber: old -> new
def M(n):
    n = int(n)
    return 37 if n == 24 else (n - 1 if 25 <= n <= 37 else n)
ps = body_ps(d)
also = max(i for i, p in enumerate(ps) if ptext(p).startswith('Also by Lothar'))
NUMLIST = r'(\d+)((?:\s*(?:,|and|or|to|–|-|,\s*and)\s*\d+)*)'
def fix_list(m):
    head, nums = m.group(1), m.group(2) + m.group(3)
    return head + re.sub(r'\d+', lambda k: str(M(k.group())), nums)
for p in ps[:also]:
    re_sub_para(p, r'\b([Cc]hapters?\s+)' + NUMLIST, fix_list)
    re_sub_para(p, r'\b((?:Figures?|Worked Examples?|Examples?|Sections?)\s+)(\d+)\.(\d+)((?:\s*(?:,|and|–|-)\s*\d+\.\d+)*)',
                lambda m: m.group(1) + str(M(m.group(2))) + '.' + m.group(3) + re.sub(r'(\d+)\.(\d+)', lambda k: str(M(k.group(1))) + '.' + k.group(2), m.group(4)))
    re_sub_para(p, r'§\s?(\d+)\.(\d+)', lambda m: '§' + str(M(m.group(1))) + '.' + m.group(2))
    if sty(p) in ('Heading2', 'Heading3'):
        re_sub_para(p, r'^(\d+)\.(\d+)', lambda m: str(M(m.group(1))) + '.' + m.group(2))
    if ptext(p).startswith('Worked Example '):
        pass
# special figure swaps where a new figure precedes an existing one in its chapter
for p in ps:
    re_sub_para(p, r'^Figure 34\.1 — A sinusoid', 'Figure 34.2 — A sinusoid')
    re_sub_para(p, r'^Figure 35\.1 — The power triangle', 'Figure 35.2 — The power triangle')
# manual sentence fixes
FIX = [
 ('between 26 and 27', 'between 25 and 26'),
 ('(12, 26, and 38)', '(12, 25, and 38)'),
 ('Chapters 20 to 37 continuously for AC', 'Chapters 20 to 23 continuously for AC, with the Smith chart of Chapter 37 as the RF extension'),
 ('Chapter 30 will answer this for purely resistive networks', 'Chapter 30 answered this for purely resistive networks'),
 ('ending with resonance and frequency response.', 'ending with resonance, frequency response, and a first look at the Smith chart and impedance matching.'),
 ('and resonance, frequency response, and transformers.', 'resonance, frequency response, and transformers, and finally the Smith chart, impedance matching, and bias networks.'),
 ('shopping trolley', 'shopping cart'),
 ('Push the same trolley', 'Push the same cart'),
]
for p in body_ps(d):
    for a, b in FIX:
        if a in ptext(p): re_sub_para(p, re.escape(a), lambda m, b=b: b)
# Chapter 38 headings: replace the odd '38.1a' with sequential numbers
ps = body_ps(d); a = next(i for i, p in enumerate(ps) if sty(p) == 'Heading1' and ptext(p).startswith('Chapter 38'))
k = 0
for p in ps[a+1:]:
    if sty(p) == 'Heading1': break
    if sty(p) == 'Heading2' and re.match(r'38\.\d+a? ', ptext(p)):
        k += 1; re_sub_para(p, r'^38\.\d+a?', lambda m, k=k: '38.%d' % k)
# ---- 3. warm-up content per chapter (new numbering)
ps = body_ps(d)
H1 = [i for i, p in enumerate(ps) if sty(p) == 'Heading1']
chap = {}
for k, i in enumerate(H1):
    m = re.match(r'Chapter (\d+) —', ptext(ps[i]))
    if m: chap[int(m.group(1))] = (ps[i], ps[H1[k+1]] if k+1 < len(H1) else None)
BUL = 2
def tailfor(c):
    t = []
    ev, dp = c['use']
    t.append(mkpara([mkrun("What You\u2019ll Actually Use")], style='Heading3', spacing={'after': 120, 'before': 280}))
    t.append(mkpara([mkrun('Everyday working tools', bold=True)], spacing={'after': 60}))
    t += [mkpara([mkrun(x)], style='ListParagraph', num=BUL, spacing={'after': 60}) for x in ev]
    if dp:
        t.append(mkpara([mkrun('Mostly for exams and deeper study', bold=True)], spacing={'after': 60, 'before': 120}))
        t += [mkpara([mkrun(x)], style='ListParagraph', num=BUL, spacing={'after': 60}) for x in dp]
    return t
counts = dict(hook=0, bench=0, use=0)
for n, (h, nxt) in chap.items():
    c = C[n]
    new = [mkpara([mkrun(c['hook'])], spacing={'after': 160})]; counts['hook'] += 1
    if c.get('meet'): new.append(mkpara([mkrun('Where you meet this: ', bold=True), mkrun(c['meet'])], spacing={'after': 200}))
    insert_after(h, new)
    # chapter range
    seg = []; e = h.getnext()
    while e is not None and e is not nxt:
        if e.tag == W('p') and sty(e) == 'Heading1' and e is not h: break
        seg.append(e); e = e.getnext()
    segp = [x for x in seg if x.tag == W('p')]
    last = segp[-1]
    while not ptext(last).strip() and not last.findall('.//' + qn('w:drawing')): last = last.getprevious()
    pp = next((x for x in segp if sty(x) == 'Heading3' and ptext(x).strip() in ('Practice Problems', 'Review Questions')), None)
    if c.get('bench'):
        bench = [mkpara([mkrun('From the Bench', bold=True)], shade='E8F1E4', spacing={'after': 80, 'before': 120}),
                 mkpara([mkrun(c['bench'])], shade='E8F1E4', spacing={'after': 120})]
        if pp is not None: insert_before(pp, bench)
        else: insert_after(last, bench); last = bench[-1]
        counts['bench'] += 1
    insert_after(last, tailfor(c)); counts['use'] += 1
# ---- 4. figures
for ref, f, cap, alt in fig_refs:
    els = picture_para(d, 'fig/' + f, 5.6, cap.split(' — ')[0], alt, cap)
    insert_after(ref, els)
d.save(out)
print('chapters', len(chap), counts, 'figures', len(fig_refs))
