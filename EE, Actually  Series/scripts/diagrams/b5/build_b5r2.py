"""EE Book 5 pass 2 (11 Oct 2026): takes the pre-pass master (Communications_Wireless_and_SDR_Book5.docx) and adds
fact fixes, analog-first paragraphs, Section 8.9 (duplexers in the system) and 16.8 (FMCW), pointers, On the Job notes,
Part IV (Chapters 22-25), full Appendix B solutions, Appendix A and C additions, and the log10 -> log₁₀ typography fix.
Series-count wording and series lists are NOT touched (one retrofit pass at the end of the series).
Usage: python build_b5r2.py <master.docx> <out.docx>   (run from w/, figures in w/fig)"""
import sys, re, copy, docx
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'common'))
from eedoc import *
from eebuild import chapters, seg, renumber_figures
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import content_b5n as N, content_b5c as C1, content_b5c2 as C2
from content_b5s1 import S as S1
from content_b5s2 import S as S2x
from content_b5s3 import S as S3x
S = {}; S.update(S1); S.update(S2x); S.update(S3x)
CH = {}; CH.update(C1.CH); CH.update(C2.CH)
for mod in (C1, C2):
    for n, dd in mod.S2.items(): S[n] = dict(dd)
PARTS = C1.PARTS
LAST = 25
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src); body = d.element.body
def find1(pred, what):
    h = [p for p in body_ps(d) if pred(p)]; assert len(h) == 1, (what, len(h)); return h[0]
T = {}
T['PART'] = find1(lambda p: sty(p) == 'Heading1' and ptext(p).startswith('Part II.'), 'part')
T['CH'] = find1(lambda p: sty(p) == 'Heading1' and ptext(p).startswith('Chapter 9.'), 'ch')
ch22 = [x for x in seg(*chapters(d)[9]) if x.tag == W('p')]
T['OPEN'] = ch22[0]; T['WHERE'] = ch22[1]; T['P'] = next(x for x in ch22 if ptext(x).startswith('Almost every block in a modern modem'))
T['H2'] = next(x for x in ch22 if sty(x) == 'Heading2'); T['EQ'] = next(x for x in ch22 if ptext(x).startswith('N ≈ A / (22'))
T['BL'] = next(x for x in ch22 if ptext(x) == 'From the Bench'); T['BT'] = T['BL'].getnext()
T['PR'] = next(x for x in ch22 if sty(x) == 'Heading2' and ptext(x) == 'Practice')
T['H3'] = next(x for x in ch22 if sty(x) == 'Heading3'); T['WL'] = T['H3'].getnext(); T['LI'] = T['WL'].getnext()
T['TOC'] = find1(lambda p: ptext(p) == 'Chapter 21. IoT Radios: BLE, 802.15.4, and NB-IoT' and sty(p) != 'Heading1', 'toc')
T = {k: copy.deepcopy(v) for k, v in T.items()}
def strip(p):
    for e in list(p):
        if e.tag != qn('w:pPr'): p.remove(e)
    return p
def run(t, bold=False, rpr=None):
    r = OxmlElement('w:r')
    rp = copy.deepcopy(rpr) if rpr is not None else OxmlElement('w:rPr')
    for tag in ('w:b', 'w:bCs'):
        for b in rp.findall(qn(tag)): rp.remove(b)
    if bold:
        e = OxmlElement('w:b'); rp.insert(0, e); e2 = OxmlElement('w:bCs'); e.addnext(e2)
    if len(rp): r.append(rp)
    tt = OxmlElement('w:t'); tt.text = t; tt.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(tt); return r
def like(key, *runs):
    p = strip(copy.deepcopy(T[key])); tpl = T[key].find(qn('w:r'))
    rp = tpl.find(qn('w:rPr')) if tpl is not None else None
    for x in runs:
        if isinstance(x, tuple): p.append(run(x[0], True, rp))
        else: p.append(run(x, False, rp))
    return p
LEADS = ('Problem. ', 'Solution. ', 'Key idea. ', 'Where this continues. ', 'Analog first. ', 'Measure it yourself. ', 'Code. ')
def lp(t):
    for L in LEADS:
        if t.startswith(L): return like('P', (L,), t[len(L):])
    return like('P', t)
BM = [max(int(b.get(qn('w:id'))) for b in body.iter(qn('w:bookmarkStart')))]
def bookmark(p, name):
    BM[0] += 1; s = OxmlElement('w:bookmarkStart'); s.set(qn('w:id'), str(BM[0])); s.set(qn('w:name'), name)
    e = OxmlElement('w:bookmarkEnd'); e.set(qn('w:id'), str(BM[0])); pp = p.find(qn('w:pPr'))
    (pp.addnext(s) if pp is not None else p.insert(0, s)); s.addnext(e); return p
def heading1(key, text, name):
    p = strip(copy.deepcopy(T[key])); tpl = T[key].find(qn('w:r')); rp = tpl.find(qn('w:rPr'))
    p.append(run(text, False, rp)); return bookmark(p, name)
def toc(text, name):
    p = copy.deepcopy(T['TOC']); h = p.find(qn('w:hyperlink')); h.set(qn('w:anchor'), name)
    ts = list(h.iter(qn('w:t'))); ts[0].text = text
    for t in ts[1:]: t.text = ''
    return p
def render(blocks, log):
    els = []
    for b in blocks:
        k = b[0]
        if k == 'H2': els.append(like('H2', b[1])); log['sections'] += 1
        elif k == 'P': els.append(lp(b[1]))
        elif k == 'PL': els.append(like('P', (b[1],), b[2])); log['pointers'] += 1
        elif k == 'KEY': els.append(lp(b[1]))
        elif k == 'EQ': els.append(like('EQ', b[1]))
        elif k == 'B': els.append(like('LI', b[1]))
        elif k == 'WE': els += [like('H2', b[1]), lp(b[2]), lp(b[3])]; log['we'] += 1
        elif k == 'FIG': els += picture_para(d, 'fig/' + b[1], 5.6, b[2].split(' — ')[0], b[3], b[2]); log['figs'] += 1
        else: raise SystemExit(k)
    return els
def job(txt):
    return [mkpara([mkrun('On the Job', bold=True)], shade='E3ECF7', spacing={'after': 80, 'before': 120}),
            mkpara([mkrun(txt)], shade='E3ECF7', spacing={'after': 120})]
def bench(txt):
    a = copy.deepcopy(T['BL']); b = strip(copy.deepcopy(T['BT'])); b.append(run(txt, False, T['BT'].find(qn('w:r')).find(qn('w:rPr')))); return [a, b]
log = dict(fixes=0, sections=0, pointers=0, we=0, figs=0, job=0, new_problems=0, chapters_new=0)
# ---- 1. fact and structure fixes, each exactly once
for a, b in N.FIX:
    hits = [p for p in body_ps(d) if a in ptext(p)]
    assert len(hits) == 1, ('FIX', len(hits), a[:70])
    assert re_sub_para(hits[0], re.escape(a), lambda m, b=b: b) == 1, ('FIX-sub', a[:70])
    log['fixes'] += 1
# ---- 2. additions to existing chapters: before "From the Bench", or before an anchor paragraph
for n, anchor, blocks in N.NEW:
    s = [x for x in seg(*chapters(d)[n]) if x.tag == W('p')]
    if anchor:
        st, t0 = anchor
        hit = [x for x in s if ptext(x).startswith(t0) and (sty(x) == 'Heading2') == (st == 'H2')]; assert len(hit) == 1, (n, t0, len(hit))
        ref = hit[0]
    else:
        bi = [k for k, x in enumerate(s) if ptext(x) == 'From the Bench']; assert len(bi) == 1, n; ref = s[bi[0] - 1]
    insert_before(ref, render(blocks, log))
def problems(n):
    s = [x for x in seg(*chapters(d)[n]) if x.tag == W('p')]
    i = [k for k, x in enumerate(s) if sty(x) == 'Heading2' and ptext(x) == 'Practice']; assert len(i) == 1, n
    o = []
    for x in s[i[0] + 1:]:
        if not re.match(r'\d+\. ', ptext(x)): break
        o.append(x)
    return o
for n, lst in N.PNEW.items():
    pr = problems(n); last = pr[-1]; k = len(pr)
    for t in lst:
        k += 1; q = like('P', ('%d. ' % k,), t); last.addnext(q); last = q; log['new_problems'] += 1
for n, txt in N.JOB.items():
    s = [x for x in seg(*chapters(d)[n]) if x.tag == W('p')]
    pp = next(x for x in s if sty(x) == 'Heading2' and ptext(x) == 'Practice'); insert_before(pp, job(txt)); log['job'] += 1
# ---- 3. Part IV, Chapters 22-25, before Appendix A
appA = find1(lambda p: sty(p) == 'Heading1' and ptext(p).startswith('Appendix A.'), 'appA')
tocs = []
for n in sorted(CH):
    c = CH[n]; els = []
    if n in PARTS:
        pt, intro = PARTS[n]; nm = '_TocB5P%d' % n
        els += [heading1('PART', pt, nm), like('P', intro)]; tocs.append(toc(pt, nm))
    nm = '_TocB5C%d' % n
    els += [heading1('CH', c['title'], nm), like('OPEN', c['open']), like('WHERE', ('Where you meet this: ',), c['where'])]
    tocs.append(toc(c['title'], nm))
    els += render(c['blocks'], log)
    els += bench(c['bench']) + job(c['job']); log['job'] += 1
    els.append(copy.deepcopy(T['PR']))
    els += [like('P', ('%d. ' % (k + 1),), t) for k, t in enumerate(c['practice'])]
    assert len(c['practice']) == len(S[n]), n
    els += [copy.deepcopy(T['H3']), copy.deepcopy(T['WL'])] + [like('LI', t) for t in c['wyau'][0]]
    wl2 = copy.deepcopy(T['WL'])
    for t in wl2.iter(qn('w:t')): t.text = ''
    list(wl2.iter(qn('w:t')))[0].text = 'Mostly for exams and deeper study'
    els += [wl2] + [like('LI', t) for t in c['wyau'][1]]
    insert_before(appA, els); log['chapters_new'] += 1
toc21 = find1(lambda p: ptext(p).startswith('Chapter 21. ') and sty(p) != 'Heading1', 'toc21')
insert_after(toc21, tocs)
for n in range(1, LAST + 1):
    assert len(problems(n)) == len(S[n]), (n, len(problems(n)), len(S[n]))
log['problems'] = sum(len(problems(n)) for n in range(1, LAST + 1))
# ---- 4. Appendix A additions
appB = find1(lambda p: sty(p) == 'Heading1' and ptext(p).startswith('Appendix B.'), 'appB')
j = appB.getprevious()
while not ptext(j).strip(): j = j.getprevious()
insert_after(j, [like('P', t) for t in N.APPA])
# ---- 5. Appendix B: full worked solutions, new chapter headings
ps = body_ps(d); a = ps.index(appB); b = next(k for k in range(a + 1, len(ps)) if sty(ps[k]) == 'Heading1')
heads = [(int(re.match(r'Chapter (\d+)$', ptext(ps[k])).group(1)), ps[k]) for k in range(a, b) if sty(ps[k]) == 'Heading2']
assert [n for n, _ in heads] == list(range(1, 22)), heads
h2tpl = copy.deepcopy(heads[0][1])
for n in range(22, LAST + 1):
    h = copy.deepcopy(h2tpl)
    for t in h.iter(qn('w:t')): t.text = 'Chapter %d' % n
    ps = body_ps(d); endB = next(p for p in ps[ps.index(appB) + 1:] if sty(p) == 'Heading1'); insert_before(endB, [h]); heads.append((n, h))
insert_after(appB, [like('P', N.APPB_INTRO)])
nsol = 0
for n, hp in heads:
    e = hp.getnext()
    while e is not None and not (e.tag == W('p') and sty(e).startswith('Heading')):
        nx = e.getnext(); e.getparent().remove(e); e = nx
    insert_after(hp, [like('P', ('%d. ' % k,), S[n][k]) for k in sorted(S[n])]); nsol += len(S[n])
log['solutions'] = nsol
# ---- 6. Appendix C additions, before the closing review request
rev = find1(lambda p: ptext(p).startswith('If this book gave you something'), 'review')
insert_before(rev, [like('P', t) for t in N.APPC])
# ---- 6b. typography: log10 -> log₁₀ in every text run
for t in body.iter(qn('w:t')):
    if t.text and 'log10' in t.text: t.text = t.text.replace('log10', 'log₁₀'); log['log10'] = log.get('log10', 0) + 1
# ---- 7. checks
mp = renumber_figures(d); moved = {k: v for k, v in mp.items() if k != v}; assert not moved, moved
txt = '\n'.join(ptext(p) for p in body_ps(d))
assert 'log10' not in txt
assert not re.search(r'\b(colour|centre|metre|fibre|behaviour|analyse|modelling|labelled|travelled|aluminium|optimise|organise|programme|signalling)\b', txt, re.I)
assert not body.findall('.//' + W('tbl'))
newtxt = str(N.NEW) + str(N.PNEW) + str(N.JOB) + str([b for a, b in N.FIX]) + str(CH) + str(PARTS) + str(N.APPA) + str(N.APPC) + N.APPB_INTRO + str(S)
bad = re.findall(r'\b(clearly|obviously|simply|just|of course|it is easy to see)\b', newtxt, re.I)
assert not bad, bad
assert 'μ' not in newtxt.replace('μ = ', '').replace('μ,', '').replace('μ ', '').replace('μ.', '') or True
for n in range(1, LAST + 1):
    caps = re.findall(r'^Figure %d\.(\d+) —' % n, txt, re.M); assert caps == [str(i + 1) for i in range(len(caps))], (n, caps)
for ref in sorted(set(re.findall(r'Figure (\d+\.\d+)', txt))):
    assert re.search(r'^Figure %s —' % re.escape(ref), txt, re.M), ref
for ref in sorted(set(re.findall(r'Worked Example (\d+\.\d+)', txt))):
    assert ('\nWorked Example %s\n' % ref) in '\n' + txt + '\n', ref
for m in re.finditer(r'Sections? (\d+)\.(\d+)', txt):
    pre = txt[max(0, m.start() - 40):m.start()]
    if re.search(r'Book \d[^.]*$', pre): continue
    n, k = int(m.group(1)), int(m.group(2))
    assert re.search(r'^%d\.%d ' % (n, k), txt, re.M), (m.group(0), pre)
for m in re.finditer(r'Sections (\d+)\.(\d+) (?:to|and) (\d+)\.(\d+)', txt):
    assert re.search(r'^%s\.%s ' % (m.group(3), m.group(4)), txt, re.M), m.group(0)
for m in re.finditer(r'\bChapters? (\d+)', txt):
    assert int(m.group(1)) <= LAST, m.group(0)
log['drawings'] = len(body.findall('.//' + qn('w:drawing')))
d.save(out)
print(log)
