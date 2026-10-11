"""Math, Actually (all four volumes): 10 Oct 2026 strict-rescore fixes.
Usage: python ma_rescore_2026-10-10.py VOL IN.docx OUT.docx

- Contents: the Word page numbers (PAGEREF fields) come out; Kindle has no pages, and the stale numbers
  read as wrong. Every entry stays a link.
- A Note Before You Go moves before About the Author (review line before the bio, house rule) and gains
  the review request; its Contents entry moves with it.
- Further Reading: each book title links to its Open Library record (no visible URLs).
- Chapter names in plain English: Logarithms & Potencies -> Logarithms & Powers; Differential ->
  Differential Calculus; Integral -> Integral Calculus (headings, Contents and cross-references).
- Title page "Volume N - X" -> "Volume N: X", as on the cover and in KDP.
- Empty hyperlinks unwrapped; trailing spaces; V1 Preface no longer says the author taught undergraduates;
  V2 British stragglers (colour, neighbouring) and spaced hyphens used as dashes.
"""
import sys, re, copy, docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
VOL, SRC, DST = int(sys.argv[1]), sys.argv[2], sys.argv[3]
d = docx.Document(SRC); body = d.element.body
RT = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink"
W = lambda tag: qn('w:' + tag)
def P(): return d.paragraphs
def heading(text):
    h = [p for p in P() if p.text == text and p.style.name == 'Heading 1']; assert len(h) == 1, (text, len(h)); return h[0]
log = {}

# 1. Contents without page numbers
npg = 0
for p in P():
    x = p._p
    if not any('PAGEREF' in (t.text or '') for t in x.iter(W('instrText'))): continue
    for h in x.iter(W('hyperlink')):
        runs = list(h.iter(W('r')))
        # drop from the tab run (or the field begin) to the end of the hyperlink
        start = None
        for k, r in enumerate(runs):
            if r.find(W('tab')) is not None or (r.find(W('fldChar')) is not None and r.find(W('fldChar')).get(W('fldCharType')) == 'begin'):
                start = k; break
        if start is not None:
            for r in runs[start:]: r.getparent().remove(r)
            npg += 1
    tabs = x.find(W('pPr'))
    if tabs is not None and tabs.find(W('tabs')) is not None: tabs.remove(tabs.find(W('tabs')))
log['contents entries without page numbers'] = npg
assert not any('PAGEREF' in (t.text or '') for t in body.iter(W('instrText')))

# 2. A Note Before You Go before About the Author, with the review request
note = heading('A Note Before You Go')._p; about = heading('About the Author')._p
block = [note]; el = note.getnext()
while el is not None and el.tag == W('p'): block.append(el); el = el.getnext()
first = block[1]
for e in block: about.addprevious(e)
rv = copy.deepcopy(first)
ts = list(rv.iter(W('t'))); ts[0].text = ('If it helped, a short review on Amazon, even a sentence or two, helps other readers find the series, '
                                           'and I read every one.')
for t in ts[1:]: t.getparent().remove(t)
for h in list(rv.iter(W('hyperlink'))): h.getparent().remove(h)
first.addnext(rv)
toc = [p for p in P() if p.style.name != 'Heading 1' and p.text in ('About the Author', 'A Note Before You Go') and p._p.find('.//' + W('hyperlink')) is not None]
assert [p.text for p in toc] == ['About the Author', 'A Note Before You Go'], [p.text for p in toc]
toc[0]._p.addprevious(toc[1]._p)

# 3. Further Reading: titles link to Open Library
OL = 'https://openlibrary.org/works/'
FR = [('Silverman, ', 'A Friendly Introduction to Number Theory', 'OL3275858W'), ('Euclid, ', 'Elements', 'OL912133W'),
      ('Spivak, ', 'Calculus', 'OL3169378W'), ('Stewart, ', 'Calculus', 'OL100903W'),
      ('Strang, ', 'Introduction to Linear Algebra', 'OL3285486W'), ('Axler, ', 'Linear Algebra Done Right', 'OL2666012W'),
      ('Bracewell, ', 'The Fourier Transform and Its Applications', 'OL14292W'), ('Needham, ', 'Visual Complex Analysis', 'OL2882085W'),
      ('Halmos, ', 'Naive Set Theory', 'OL2776836W'), ('Strogatz, ', 'Nonlinear Dynamics and Chaos', 'OL3907581W'),
      ('Evans, ', 'Partial Differential Equations', 'OL15596967W'), ('Trefethen and Bau, ', 'Numerical Linear Algebra', 'OL3357483W'),
      ('Munkres, ', 'Topology', 'OL113948W'), ('do Carmo, ', 'Differential Geometry of Curves and Surfaces', 'OL3488346W'),
      ('Rudin, ', 'Principles of Mathematical Analysis', 'OL1295436W'), ('Dummit and Foote, ', 'Abstract Algebra', 'OL1968605W'),
      ('Leinster, ', 'Basic Category Theory', 'OL17472285W'), ('Mac Lane, ', 'Categories for the Working Mathematician', 'OL2739892W'),
      ('Cover and Thomas, ', 'Elements of Information Theory', 'OL4477088W'), ('Wasserman, ', 'All of Statistics', 'OL8055600W'),
      ('Bishop, ', 'Pattern Recognition and Machine Learning', 'OL2963587W'), ('\u00c5str\u00f6m and Murray, ', 'Feedback Systems', 'OL3332632W'),
      ('de Berg et al., ', 'Computational Geometry: Algorithms and Applications', 'OL3406114W'),
      ('Courant and Robbins, ', 'What Is Mathematics?', 'OL811195W')]
def linkify(p, phrase, url):
    for r in p._p.iter(W('r')):
        if r.getparent().tag == W('hyperlink'): continue
        t = r.find(W('t'))
        if t is None or not t.text or phrase not in t.text: continue
        a, b = t.text.split(phrase, 1); rpr = r.find(W('rPr'))
        def mk(text, link=False):
            nr = OxmlElement('w:r'); rp = copy.deepcopy(rpr) if rpr is not None else OxmlElement('w:rPr')
            if link:
                for c in list(rp):
                    if c.tag in (W('color'), W('u')): rp.remove(c)
                c = OxmlElement('w:color'); c.set(W('val'), '0563C1'); rp.append(c)
                u = OxmlElement('w:u'); u.set(W('val'), 'single'); rp.append(u)
            if len(rp): nr.append(rp)
            x = OxmlElement('w:t'); x.set(qn('xml:space'), 'preserve'); x.text = text; nr.append(x); return nr
        h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), d.part.relate_to(url, RT, is_external=True)); h.set(W('history'), '1'); h.append(mk(phrase, True))
        if a: r.addprevious(mk(a))
        r.addprevious(h)
        if b: r.addprevious(mk(b))
        r.getparent().remove(r); return
    raise AssertionError((phrase, p.text[:80]))
fr = [i for i, p in enumerate(P()) if p.text == 'Appendix \u2014 Further Reading' and p.style.name == 'Heading 1'][0]
for who, title, key in FR:
    hit = [p for p in P()[fr:fr + 40] if p.text.startswith(who + title)]; assert len(hit) == 1, (who, len(hit))
    linkify(hit[0], title, OL + key)
log['Further Reading links'] = len(FR)

# 4. chapter names, title page
REN = [('Logarithms & Potencies', 'Logarithms & Powers'),
       ('Chapter 11: Differential', 'Chapter 11: Differential Calculus'), ('Chapter 11 \u2014 Differential', 'Chapter 11 \u2014 Differential Calculus'),
       ('(Differential)', '(Differential Calculus)'),
       ('Chapter 12: Integral', 'Chapter 12: Integral Calculus'), ('Chapter 12 \u2014 Integral', 'Chapter 12 \u2014 Integral Calculus'),
       ('(Integral)', '(Integral Calculus)')]
nren = 0
for t in body.iter(W('t')):
    s = t.text
    if not s: continue
    for a, b in REN:
        if a in s and b not in s: s = s.replace(a, b)
    if s != t.text: t.text = s; nren += 1
if VOL == 1:
    for old, new in (('Differential', 'Differential Calculus'), ('Integral', 'Integral Calculus')):
        h = heading(old); ts = list(h._p.iter(W('t'))); ts[0].text = new
        for t in ts[1:]: t.text = ''
        nren += 1
log['chapter-name edits'] = nren
tp = [p for p in P()[:6] if p.style.name == 'Heading 1' and re.match(r'Volume \d - ', p.text)]; assert len(tp) == 1
for t in tp[0]._p.iter(W('t')):
    if t.text and re.search(r'Volume \d - ', t.text): t.text = re.sub(r'(Volume \d) - ', r'\1: ', t.text)

# 5. small text fixes
FIX = []
if VOL == 1:
    FIX += [('and I say this as someone who has spent an unreasonable fraction of one career telling undergraduates how to read things.',
             'and I say this as someone who has spent a long career reading technical books in every order except the intended one.')]
if VOL == 2:
    FIX += [('colourings', 'colorings'), ('coloured', 'colored'), ('colours', 'colors'), ('colour ', 'color '), ('neighbouring', 'neighboring'),
            ('neighbour', 'neighbor')]
nfix = 0
for t in body.iter(W('t')):
    if not t.text: continue
    s = t.text
    for a, b in FIX: s = s.replace(a, b)
    if VOL == 2: s = re.sub(r'(?<=[a-z,]) - (?=[a-z])', ' \u2014 ', s)
    if s != t.text: t.text = s; nfix += 1
log['text fixes (runs)'] = nfix
ne = 0
for h in list(body.iter(W('hyperlink'))):
    if ''.join(x.text or '' for x in h.iter(W('t'))).strip() == '' and not list(h.iter(W('drawing'))):
        par = h.getparent()
        for ch in list(h): h.addprevious(ch)
        par.remove(h); ne += 1
log['empty links unwrapped'] = ne
nt = 0
for p in P():
    ts = [t for t in p._p.iter(W('t')) if t.text]
    if ts and p.text.strip() and ts[-1].text != ts[-1].text.rstrip(): ts[-1].text = ts[-1].text.rstrip(); nt += 1
log['trailing spaces'] = nt
d.save(DST)
print(VOL, log)
