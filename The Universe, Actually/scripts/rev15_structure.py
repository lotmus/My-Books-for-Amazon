"""The Universe, Actually REV14 -> REV15 (10 Oct 2026).
Structure: merge the near-duplicate chapter pairs (39/40 Evolution, 51/52 Brain/Neuroscience,
29/30 + 70 Quantum Information/Computation), renumber 81 -> 77 chapters, rebuild the linked Contents.
Also: American spelling throughout the main text (bibliography and resource titles untouched),
the three leftover "In this section:" lines removed, back matter given real headings
(About the Author, Also by) in place of the catch-all "Appendix".
Usage: python rev15_structure.py REV14.docx REV15.docx   (then tools/kindle_links.py with kindle_links.json)"""
import sys, re, copy, docx
from docx.oxml.ns import qn
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src); body = d.element.body
P = lambda: list(body.iterchildren(qn('w:p')))
def text(p): return ''.join(t.text or '' for t in p.iter(qn('w:t')))
def style(p):
    s = p.find(qn('w:pPr'))
    s = s.find(qn('w:pStyle')) if s is not None else None
    return s.get(qn('w:val')) if s is not None else ''
def settext(p, s):
    ts = list(p.iter(qn('w:t'))); ts[0].text = s
    for t in ts[1:]: t.text = ''

# ---------- 1. American spelling in the main text (stop at "A Note on Sources")
SP = [(r'\b(colo|behavio|favo|vapo|neighbo|labo|odo|harbo|tumo)ur', r'\1r'),
      (r'\b(cen|kilome|centime|nanome|microme|millime|femtome|submillime|me|fib|lit)tre', r'\1ter'),
      (r'\b(organi|reorgani|reali|renormali|ioni|reioni|photoioni|stabili|recogni|unrecogni|generali|optimi|polari|maximi|minimi|summari|visuali|crystalli|synthesi|hypothesi)s(e|ed|es|ing|er|ation|ations|able)\b', r'\1z\2'),
      (r'\bcharacteris(e|ed|es|ing|ation)\b', r'characteriz\1'), (r'\bemphasis(e|ed|es|ing)\b', r'emphasiz\1'),
      (r'\b(signa|labe|unlabe|trave|mode|mode)ll(ing|ed|er|ers)\b', r'\1l\2'),
      (r'\bhaem', 'hem'), (r'\bHaem', 'Hem'), (r'\bdefence', 'defense'), (r'\bcatalogue(d|s)?\b', lambda m: 'catalog' + ({'d':'ed','s':'s'}.get(m.group(1) or '', ''))),
      (r'\bartefact', 'artifact'), (r'\bsulphur', 'sulfur'), (r'\baluminium', 'aluminum'), (r'\bageing', 'aging'),
      (r'\bgrey\b', 'gray'), (r'\bmould', 'mold'), (r'\bjudgement', 'judgment'), (r'\b([Pp])rogramme(s?)\b', r'\1rogram\2')]
paras = P()
stop = next(i for i, p in enumerate(paras) if style(p) == 'Heading1' and text(p) == 'A Note on Sources')
nsp = 0
for p in paras[:stop]:
    for t in p.iter(qn('w:t')):
        s = t.text or ''
        if not s: continue
        n = s
        for a, b in SP:
            n = re.sub(a, b, n)
        n = re.sub(r'\b(Colo|Behavio|Favo|Neighbo)ur', r'\1r', n); n = re.sub(r'\bCentre', 'Center', n)
        n = re.sub(r'\b(Organi|Reali|Recogni|Stabili|Generali|Optimi)s(e|ed|es|ing|ation)\b', r'\1z\2', n)
        if n != s: t.text = n; nsp += 1
print('spelling runs changed', nsp)

# ---------- 2. leftover "In this section:" outline lines
for p in P():
    if text(p).startswith('In this section:'): body.remove(p)

# ---------- 3. chapter model
def chapters():
    ps = P(); idx = [i for i, p in enumerate(ps) if style(p) == 'Heading2']
    parts = [i for i, p in enumerate(ps) if style(p) == 'Heading1']
    ch = {}
    for k, i in enumerate(idx):
        end = min([j for j in idx + parts if j > i] or [len(ps)])
        num = int(text(ps[i]).split('.')[0]); ch[num] = ps[i:end]
    return ch
def split(chap):  # -> heading, intro list, [(h3, [paras])]
    h, rest = chap[0], chap[1:]; intro = []; secs = []
    for p in rest:
        if style(p) == 'Heading3': secs.append((p, []))
        elif secs: secs[-1][1].append(p)
        else: intro.append(p)
    return h, intro, secs
C = chapters()
def sec(secs, title):
    m = [s for s in secs if text(s[0]) == title]; assert len(m) == 1, title; return m[0]
def h3like(template, title):
    e = copy.deepcopy(template)
    for b in e.iter(qn('w:bookmarkStart')): b.getparent().remove(b)
    for b in e.iter(qn('w:bookmarkEnd')): b.getparent().remove(b)
    settext(e, title); return e
def place(anchor, els):  # replace the chapter that starts at anchor with els
    for e in els[1:]:
        if e.getparent() is not None: e.getparent().remove(e)
    for e in reversed(els[1:]): anchor.addnext(e)

# 3a. Quantum Information and Computation (29 + 30 + 70) in Part III
h29, i29, s29 = split(C[29]); h30, i30, s30 = split(C[30]); h70, i70, s70 = split(C[70])
assert not i30 and not s70 and len(i70) == 9
settext(h29, '29. Quantum Information and Computation')
qec = sec(s29, 'Quantum Error Correction'); qec2 = sec(s29, 'Further Aspects of Quantum Error Correction')
new = [h29] + i70[:2] + i29
for t in ['No-Cloning and Quantum Information', 'Quantum Key Distribution', 'Quantum Teleportation', 'Quantum Networks']:
    s = sec(s29, t); new += [s[0]] + s[1]
s = sec(s30, 'Quantum Computing'); new += [s[0]] + s[1]
new += [qec[0]] + qec[1] + qec2[1]
for t in ['Topological Quantum Computation', 'Measurement-Based Quantum Computation', 'Adiabatic Quantum Computation', 'Quantum Annealing', 'Variational Quantum Algorithms', 'Blind Quantum Computation']:
    s = sec(s30, t); new += [s[0]] + s[1]
new += [h3like(qec[0], 'Building One, and What It Is For')] + i70[2:]
for e in [qec2[0], h30, h70]: e.getparent().remove(e)
place(h29, new)

# 3b. Evolution and Genetics (39 + 40)
h39, i39, s39 = split(C[39]); h40, i40, s40 = split(C[40])
S = {text(h): (h, b) for h, b in s39 + s40}
assert len(S) == len(s39) + len(s40)
order = ['Natural Selection', '+Natural Selection Without a Designer', 'Genetics Before DNA', 'Mendel and the Chromosomes', '+Mendelian Inheritance',
         'The Double Helix', 'The Structure and Replication of DNA', 'DNA and the Genetic Code', 'Mutation and Variation', 'The Gene That Was Not Supposed to Move',
         'Epigenetic Inheritance', 'Genomic Imprinting', 'Parental-Conflict Theory of Imprinting', 'Horizontal Gene Transfer', 'Population Genetics',
         'Worked Examples: Population Genetics', 'Speciation', 'Classification and the Tree of Life', '+The Tree of Life',
         'Sexual Reproduction and Parthenogenesis', 'Ethology and the Evolution of Behavior', 'Ants, Termites and Bees', 'The Map That Contains Itself']
assert sorted(o.lstrip('+') for o in order) == sorted(S), set(S) ^ set(o.lstrip('+') for o in order)
new = [h39] + i39 + i40
for o in order:
    h, b = S[o.lstrip('+')]
    if o.startswith('+'): new += b; h.getparent().remove(h)
    else: new += [h] + b
h40.getparent().remove(h40); place(h39, new)

# 3c. The Brain and Nervous System (51 + 52)
h51, i51, s51 = split(C[51]); h52, i52, s52 = split(C[52])
settext(h51, '51. The Brain and Nervous System')
S = {text(h): (h, b) for h, b in s51 + s52}
new = [h51] + i51
for t in ['The Nervous System', 'The Human Brain']: new += [S[t][0]] + S[t][1]
new += [h3like(S['The Human Brain'][0], 'What Neuroscience Knows')] + i52
new += [S['Systems Neuroscience'][0]] + S['Systems Neuroscience'][1] + S['Further Aspects of Systems Neuroscience'][1]
S['Further Aspects of Systems Neuroscience'][0].getparent().remove(S['Further Aspects of Systems Neuroscience'][0])
for t in ['Brain Plasticity', 'Sleep and Memory Consolidation', 'Memory Improvement', 'Brain Exercises and Cognitive Training', 'Unused Brain Potential']:
    new += [S[t][0]] + S[t][1]
h52.getparent().remove(h52); place(h51, new)

# ---------- 4. back matter: About the Author and Also by as real headings, no "Appendix"
ps = P()
app = next(p for p in ps if style(p) == 'Heading1' and text(p) == 'Appendix')
about = next(p for p in ps if text(p) == 'About the Author')
settext(app, 'About the Author')
for b in app.iter(qn('w:bookmarkStart')): b.set(qn('w:name'), 'bm_about')
review = app.getnext()
assert text(review).startswith('If this book gave you something')
# review line goes before the heading (end of the External Resources page), the old bold label goes
app.addprevious(review); about.getparent().remove(about)
first_alsoby = next(p for p in P() if text(p).startswith('Physics, Actually · '))
also = copy.deepcopy(app); settext(also, 'Also by Lothar J. Musiol')
for b in also.iter(qn('w:bookmarkStart')): b.set(qn('w:name'), 'bm_alsoby'); b.set(qn('w:id'), '9001')
for b in also.iter(qn('w:bookmarkEnd')): b.set(qn('w:id'), '9001')
first_alsoby.addprevious(also)

# ---------- 5. renumber chapters, bookmarks ch_N
n = 0; chap_heads = []
for p in P():
    if style(p) == 'Heading2':
        n += 1; t = text(p); new = re.sub(r'^\d+\.', '%d.' % n, t); settext(p, new)
        bs = list(p.iter(qn('w:bookmarkStart'))); assert len(bs) == 1; bs[0].set(qn('w:name'), 'ch_%d' % n)
        chap_heads.append(p)
print('chapters', n)

# ---------- 6. rebuild the linked Contents
ps = P()
c0 = next(i for i, p in enumerate(ps) if style(p) == 'Heading1' and text(p) == 'Contents')
part_tpl = ch_tpl = None; toc = []
i = c0 + 1
while style(ps[i]) != 'Heading1':
    hl = ps[i].find(qn('w:hyperlink'))
    if hl is not None:
        a = hl.get(qn('w:anchor'))
        if a.startswith('part_') and part_tpl is None: part_tpl = ps[i]
        if a.startswith('ch_') and ch_tpl is None: ch_tpl = ps[i]
        toc.append(ps[i])
    i += 1
first_part = next(p for p in toc if p.find(qn('w:hyperlink')).get(qn('w:anchor')).startswith('part_'))
epi = next(p for p in toc if p.find(qn('w:hyperlink')).get(qn('w:anchor')) == 'bm_epilogue')
appx = next(p for p in toc if p.find(qn('w:hyperlink')).get(qn('w:anchor')) == 'bm_appendix')
def entry(tpl, anchor, label):
    e = copy.deepcopy(tpl); e.find(qn('w:hyperlink')).set(qn('w:anchor'), anchor); settext(e, label); return e
newtoc = []
for p in P():
    if style(p) == 'Heading1':
        b = [x.get(qn('w:name')) for x in p.iter(qn('w:bookmarkStart'))]
        if b and b[0].startswith('part_'): newtoc.append(entry(part_tpl, b[0], text(p)))
    elif style(p) == 'Heading2':
        newtoc.append(entry(ch_tpl, 'ch_%s' % text(p).split('.')[0], text(p)))
# drop old part/chapter entries (first_part .. before epilogue), insert the new ones
drop = toc[toc.index(first_part):toc.index(epi)]
for e in newtoc: epi.addprevious(e)
for e in drop: body.remove(e)
appx.addprevious(entry(appx, 'bm_about', 'About the Author')); appx.addprevious(entry(appx, 'bm_alsoby', 'Also by Lothar J. Musiol')); body.remove(appx)

# ---------- 7. dead-link check
names = {b.get(qn('w:name')) for b in body.iter(qn('w:bookmarkStart'))}
dead = [h.get(qn('w:anchor')) for h in body.iter(qn('w:hyperlink')) if h.get(qn('w:anchor')) and h.get(qn('w:anchor')) not in names]
assert not dead, dead
ids = [b.get(qn('w:id')) for b in body.iter(qn('w:bookmarkStart'))]; assert len(ids) == len(set(ids))
d.core_properties.title = 'The Universe, Actually'
d.save(out); print('saved', out)
