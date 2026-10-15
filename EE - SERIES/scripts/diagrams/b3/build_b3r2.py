"""EE Book 3 pass 2 (11 Oct 2026): takes the pre-pass master (Semiconductor_Physics_and_Devices_Book3.docx) and adds
fact fixes, new sections in Chapters 6-7, 9-10, 13, 17-19, 21-22, On the Job notes, Part VIII (Ch 23-24, datasheet to SPICE)
and Part IX (Ch 25-28), full Appendix B solutions, Appendix A/D additions and a new Appendix E.
Series-count wording and series lists are NOT touched (one retrofit pass at the end of the series).
Usage: python build_b3r2.py <master.docx> <out.docx>"""
import sys, re, copy, docx
sys.path.insert(0, '../common')
from eedoc import *
from eebuild import chapters, seg, renumber_figures
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import content_b3r as R, content_b3n as N, content_b3c as C, content_b3x as X
from content_b3s import S
for n, dd in X.S2.items():
    S.setdefault(n, {}); base = len(S[n]) if n < 23 else 0
    for k, v in dd.items(): S[n][k] = v
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src); body = d.element.body
ps = body_ps(d)
def find1(pred, what):
    h = [p for p in body_ps(d) if pred(p)]; assert len(h) == 1, (what, len(h)); return h[0]
# ---- templates (deep copies of existing paragraphs, so new text matches the book's formatting exactly)
T = {}
T['PART'] = find1(lambda p: sty(p) == 'Heading1' and ptext(p).startswith('Part VII.'), 'part')
T['CH'] = find1(lambda p: sty(p) == 'Heading1' and ptext(p).startswith('Chapter 22.'), 'ch')
ch22 = [x for x in seg(*chapters(d)[22]) if x.tag == W('p')]
T['OPEN'] = ch22[0]; T['WHERE'] = ch22[1]; T['P'] = next(x for x in ch22 if ptext(x).startswith('A diode carries 1 mA'))
T['H2'] = next(x for x in ch22 if sty(x) == 'Heading2'); T['EQ'] = next(x for x in ch22 if ptext(x).startswith('n = ΔV'))
T['BL'] = next(x for x in ch22 if ptext(x) == 'From the Bench'); T['BT'] = T['BL'].getnext()
T['PR'] = next(x for x in ch22 if sty(x) == 'Heading2' and ptext(x) == 'Practice')
T['H3'] = next(x for x in ch22 if sty(x) == 'Heading3'); T['WL'] = T['H3'].getnext(); T['LI'] = T['WL'].getnext()
T['TOC'] = find1(lambda p: ptext(p) == 'Chapter 22. Compact Models and the Process Design Kit' and sty(p) != 'Heading1', 'toc')
T = {k: copy.deepcopy(v) for k, v in T.items()}
RPR = copy.deepcopy(T['P'].find(qn('w:r')).find(qn('w:rPr')))
def strip(p):
    for e in list(p):
        if e.tag not in (qn('w:pPr'),): p.remove(e)
    return p
def run(t, bold=False, rpr=None):
    r = OxmlElement('w:r')
    if rpr is not None:
        rp = copy.deepcopy(rpr)
        if bold:
            for b in rp.findall(qn('w:b')): rp.remove(b)
            e = OxmlElement('w:b'); rp.insert(0, e)
        r.append(rp)
    elif bold:
        rp = OxmlElement('w:rPr'); rp.append(OxmlElement('w:b')); rp.append(OxmlElement('w:bCs')); r.append(rp)
    tt = OxmlElement('w:t'); tt.text = t; tt.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(tt); return r
def like(key, *runs):
    p = strip(copy.deepcopy(T[key])); tpl = T[key].find(qn('w:r'))
    rp = tpl.find(qn('w:rPr')) if tpl is not None else None
    for x in runs:
        if isinstance(x, tuple): p.append(run(x[0], True, rp if key not in ('WHERE',) else None))
        else: p.append(run(x, False, rp if key != 'WHERE' else None))
    return p
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
    for t in h.iter(qn('w:t')): t.text = text
    return p
def render(blocks, log):
    els = []
    for b in blocks:
        k = b[0]
        if k == 'H2': els.append(like('H2', b[1])); log['sections'] += 1
        elif k == 'P': els.append(like('P', b[1]))
        elif k == 'PL': els.append(like('P', (b[1],), b[2])); log['pointers'] += 1
        elif k == 'KEY': els.append(like('P', b[1]))
        elif k == 'EQ': els.append(like('EQ', b[1]))
        elif k == 'B': els.append(like('LI', b[1]))
        elif k == 'WE': els += [like('H2', b[1]), like('P', b[2]), like('P', b[3])]; log['we'] += 1
        elif k == 'FIG': els += picture_para(d, 'fig/' + b[1], 5.6, b[2].split(' — ')[0], b[3], b[2]); log['figs'] += 1
        else: raise SystemExit(k)
    return els
def job(txt):
    return [mkpara([mkrun('On the Job', bold=True)], shade='E3ECF7', spacing={'after': 80, 'before': 120}),
            mkpara([mkrun(txt)], shade='E3ECF7', spacing={'after': 120})]
def bench(txt):
    a = copy.deepcopy(T['BL']); b = strip(copy.deepcopy(T['BT'])); b.append(run(txt)); return [a, b]
log = dict(fixes=0, sections=0, pointers=0, we=0, figs=0, job=0, new_problems=0, chapters_new=0)
# ---- 1. fact fixes and structural text fixes, each exactly once
for a, b in R.FIX + N.FIX_MORE:
    hits = [p for p in body_ps(d) if a in ptext(p)]
    assert len(hits) == 1, ('FIX', len(hits), a[:70])
    assert re_sub_para(hits[0], re.escape(a), lambda m, b=b: b) == 1, ('FIX-sub', a[:70])
    log['fixes'] += 1
# ---- 2. additions to existing chapters: before the closing paragraph that precedes From the Bench
for n, blocks in N.NEW.items():
    s = [x for x in seg(*chapters(d)[n]) if x.tag == W('p')]
    bi = [i for i, x in enumerate(s) if ptext(x) == 'From the Bench']; assert len(bi) == 1, n
    j = bi[0] - 1
    while not ptext(s[j]).strip(): j -= 1
    assert sty(s[j]) == '' or sty(s[j]) == 'Normal', (n, sty(s[j]))
    insert_before(s[j], render(blocks, log))
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
        k += 1; q = like('P', '%d. %s' % (k, t)); last.addnext(q); last = q; log['new_problems'] += 1
for n, txt in N.JOB.items():
    s = [x for x in seg(*chapters(d)[n]) if x.tag == W('p')]
    pp = next(x for x in s if sty(x) == 'Heading2' and ptext(x) == 'Practice'); insert_before(pp, job(txt)); log['job'] += 1
# ---- 3. Parts VIII and IX, Chapters 23-28, before Appendix A
appA = find1(lambda p: sty(p) == 'Heading1' and ptext(p).startswith('Appendix A.'), 'appA')
tocs = []
for n in sorted(C.CH):
    c = C.CH[n]; els = []
    if n in C.PARTS:
        pt, intro = C.PARTS[n]; nm = '_TocB3P%d' % n
        els += [heading1('PART', pt, nm), like('P', intro)]; tocs.append(toc(pt, nm))
    nm = '_TocB3C%d' % n
    els += [heading1('CH', c['title'], nm), like('OPEN', c['open']), like('WHERE', ('Where you meet this: ',), c['where'])]
    tocs.append(toc(c['title'], nm))
    els += render(c['blocks'], log)
    els += bench(c['bench']) + job(c['job']); log['job'] += 1
    els.append(copy.deepcopy(T['PR']))
    els += [like('P', '%d. %s' % (k + 1, t)) for k, t in enumerate(c['practice'])]
    assert len(c['practice']) == len(X.S2[n]), n
    els += [copy.deepcopy(T['H3']), like('WL', 'Everyday working tools')] + [like('LI', t) for t in c['wyau'][0]]
    els += [like('WL', 'Mostly for exams and deeper study')] + [like('LI', t) for t in c['wyau'][1]]
    insert_before(appA, els); log['chapters_new'] += 1
toc22 = find1(lambda p: ptext(p) == 'Chapter 22. Compact Models and the Process Design Kit' and sty(p) != 'Heading1', 'toc22')
insert_after(toc22, tocs)
for n in range(1, 29):
    assert len(problems(n)) == len(S[n]), (n, len(problems(n)), len(S[n]))
log['problems'] = sum(len(problems(n)) for n in range(1, 29))
# ---- 4. Appendix A additions
appB = find1(lambda p: sty(p) == 'Heading1' and ptext(p).startswith('Appendix B.'), 'appB')
j = appB.getprevious()
while not ptext(j).strip(): j = j.getprevious()
insert_after(j, [like('P', t) for t in X.APPA])
# ---- 5. Appendix B: full worked solutions, new chapter headings
ps = body_ps(d); a = ps.index(appB); b = next(k for k in range(a + 1, len(ps)) if sty(ps[k]) == 'Heading1')
heads = [(int(re.match(r'Chapter (\d+)$', ptext(ps[k])).group(1)), ps[k]) for k in range(a, b) if sty(ps[k]) == 'Heading2']
assert [n for n, _ in heads] == list(range(1, 23)), heads
h2tpl = copy.deepcopy(heads[0][1]); lastsol = None
for n in range(23, 29):
    h = copy.deepcopy(h2tpl)
    for t in h.iter(qn('w:t')): t.text = 'Chapter %d' % n
    ps = body_ps(d); endB = next(p for p in ps[ps.index(appB) + 1:] if sty(p) == 'Heading1'); insert_before(endB, [h]); heads.append((n, h))
insert_after(appB, [like('P', X.APPB_INTRO)])
nsol = 0
for n, hp in heads:
    e = hp.getnext()
    while e is not None and not (e.tag == W('p') and sty(e).startswith('Heading')):
        nx = e.getnext(); e.getparent().remove(e); e = nx
    insert_after(hp, [like('P', ('%d. ' % k,), S[n][k]) for k in sorted(S[n])]); nsol += len(S[n])
log['solutions'] = nsol
# ---- 6. Appendix D: new part headings; Appendix E before the closing review request
d7 = find1(lambda p: sty(p) == 'Heading2' and ptext(p).startswith('Part VII:'), 'd7')
d7p = d7.getnext(); dh = copy.deepcopy(d7)
new = []
for title, txt in X.APPD:
    h = copy.deepcopy(dh)
    for t in h.iter(qn('w:t')): t.text = title
    new += [h, like('P', txt)]
insert_after(d7p, new)
rev = find1(lambda p: ptext(p).startswith('If this book gave you something'), 'review')
els = [heading1('CH', X.APPE_TITLE, '_TocB3AppE'), like('P', X.APPE_INTRO)]
for title, items in X.APPE:
    h = copy.deepcopy(dh)
    for t in h.iter(qn('w:t')): t.text = title
    els += [h] + [like('LI', t) for t in items]
insert_before(rev, els)
tocD = find1(lambda p: ptext(p) == 'Appendix D. Sources and Further Reading' and sty(p) != 'Heading1', 'tocD')
insert_after(tocD, [toc(X.APPE_TITLE, '_TocB3AppE')])
# ---- 7. checks
mp = renumber_figures(d); moved = {k: v for k, v in mp.items() if k != v}; assert not moved, moved
txt = '\n'.join(ptext(p) for p in body_ps(d))
assert not re.search(r'\b(colour|centre|metre|fibre|behaviour|analyse|modelling|labelled|travelled|aluminium|optimise|organise|programme)\b', txt, re.I)
assert 'Trump' not in txt
assert not body.findall('.//' + W('tbl'))
newtxt = str(N.NEW) + str(N.PNEW) + str(N.JOB) + str([b for a, b in N.FIX_MORE + R.FIX]) + str(C.CH) + str(C.PARTS) + str(X.__dict__) + str(S)
bad = re.findall(r'\b(clearly|obviously|simply|just|of course|it is easy to see)\b', newtxt, re.I)
assert not bad, bad
for n in range(1, 29):
    caps = re.findall(r'^Figure %d\.(\d+) —' % n, txt, re.M); assert caps == [str(i + 1) for i in range(len(caps))], (n, caps)
for ref in sorted(set(re.findall(r'Figure (\d+\.\d+)', txt))):
    assert re.search(r'^Figure %s —' % re.escape(ref), txt, re.M), ref
for ref in sorted(set(re.findall(r'Worked Example (\d+\.\d+)', txt))):
    assert ('\nWorked Example %s\n' % ref) in '\n' + txt + '\n', ref
for ref in sorted(set(re.findall(r'Section (\d+)\.(\d+)', txt))):
    n, k = map(int, ref)
    if n <= 28: assert re.search(r'^%d\.%d ' % (n, k), txt, re.M), ref
log['drawings'] = len(body.findall('.//' + qn('w:drawing')))
d.save(out)
print(log)
