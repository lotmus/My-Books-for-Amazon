"""Quantum, Actually Vol 1: strict rescore fixes, 10 Oct 2026 (sampled reread).
Usage: python rescore_2026-10-10.py IN.docx OUT.docx"""
import sys, re, copy, docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
SRC, DST = sys.argv[1:3]
d = docx.Document(SRC); P = d.paragraphs
RT = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink"
def one(pred, style=None):
    h = [i for i, p in enumerate(P) if pred(p.text) and (style is None or p.style.name == style)]
    assert len(h) == 1, (h, pred); return h[0]
def set_text(p, new):
    """replace whole paragraph text, keep first run formatting (plain paragraphs only)"""
    rs = p.runs; rs[0].text = new
    for r in rs[1:]: r._r.getparent().remove(r._r)
def rep(p, old, new):
    for t in p._p.iter(qn('w:t')):
        if t.text and old in t.text: t.text = t.text.replace(old, new, 1); return
    raise AssertionError((old, p.text[:80]))

# 1. Prologue: the "that assumption" sentence came before the assumption
a = one(lambda s: s.startswith('This book is about the specific, well-tested ways that assumption'))
b = a + 1; assert P[b].text.startswith('For three hundred years')
P[a]._p.addprevious(P[b]._p)
# 2. old title left in the prologue
i = one(lambda s: s.strip() == 'That is where Quantum World begins'); set_text(P[i], 'That is where the quantum world begins.')
# 3. road map step 7 styled like steps 1-6
i = one(lambda s: s.startswith('7. Name the collision')); P[i].style = d.styles['Heading 2']
# 4. wrong opening quote in a box head
i = one(lambda s: s == 'HOW PRECISE IS \u2019ONE PART IN A TRILLION\u2019'); rep(P[i], '\u2019ONE', '\u2018ONE')
# 5. Psi = sqrt(n) e^{i theta(r)}: the (r) belongs in the exponent
i = one(lambda s: s.startswith('\u03a8(r) = \u221an(r)e')); P[i].runs[2].font.superscript = True
# 6. Chapter 13: three overlong or loose sentences
i = one(lambda s: s.startswith('Cool the same box down, far enough'))
rep(P[i], 'Cool the same box down, far enough that thermal jostling stops scrambling everything, typically within a few degrees of absolute zero, though some materials manage the trick above the temperature of liquid nitrogen (still colder than anywhere on Earth\u2019s surface has ever naturally been, but warm enough to reach with a cooling method any lab can buy off the shelf), and something changes qualitatively, not just quantitatively.',
    'Cool the same box down far enough that thermal jostling stops scrambling everything, and something changes qualitatively, not just quantitatively. For most materials that means within a few degrees of absolute zero; some manage it above the temperature of liquid nitrogen, still colder than anywhere on Earth\u2019s surface has ever naturally been, but easy to reach with equipment any lab can buy off the shelf.')
i = one(lambda s: s.startswith('That interference pattern is sensitive enough'))
rep(P[i], 'sensitive enough to detect a change in magnetic field measured in single flux quanta,', 'sensitive enough to register a change of a tiny fraction of one flux quantum,')
i = one(lambda s: s.startswith('A radio engineer meets this fact constantly'))
rep(P[i], 'does not simply scale with the hundred elements doing the radiating \u2014 it scales with the hundred elements ', 'does not simply scale with the hundred elements doing the radiating; it scales with the hundred elements ')
rep(P[i], ', ten thousand times the output of one element alone \u2014 concentrated into a narrower beam, not manufactured from nowhere, since the total power radiated in every direction combined is still set by what the array is fed \u2014 which is why phased-array radar',
    ', ten thousand times the output of one element alone. That power is concentrated into a narrower beam, not manufactured from nowhere: the total radiated in every direction combined is still set by what the array is fed. It is why phased-array radar')
# 7. double spaces used as separators
n2 = 0
for p in P:
    for t in p._p.iter(qn('w:t')):
        if t.text and '  ' in t.text:
            s = re.sub(r'^(Chapter \d+)  ', r'\1: ', t.text)
            s = re.sub(r'^([QA]\.)  ', r'\1 ', s)
            if s == '  ' and re.match(r'Chapter \d+  ', p.text): s = ': '
            s = re.sub(r'(?<=\S)  +(?=\S)', ' ', s)
            if s != t.text: t.text = s; n2 += 1
# 8. trailing spaces at paragraph ends
nt = 0
for p in P:
    ts = [t for t in p._p.iter(qn('w:t')) if t.text]
    if ts and ts[-1].text != ts[-1].text.rstrip() and p.text.strip():
        ts[-1].text = ts[-1].text.rstrip(); nt += 1
# 9. Notes on Sources: doubled full stops, Peskin's 1995 publisher, g/2 vs a_e
nd = 0
for p in P:
    if p.text.endswith('..') and not p.text.endswith('...'):
        ts = [t for t in p._p.iter(qn('w:t')) if t.text]; ts[-1].text = ts[-1].text[:-1]; nd += 1
i = one(lambda s: s.startswith('Advanced. Michael E. Peskin')); rep(P[i], '(Westview Press, 1995)', '(Addison-Wesley, 1995)')
i = one(lambda s: s.startswith('The comparison with the calculated series is limited'))
ts = [t for t in P[i]._p.iter(qn('w:t')) if t.text]
ts[-1].text = ts[-1].text + ' Measured on g/2 itself rather than on ae, the same agreement is about one part in a trillion, the figure Part One uses.'
# 10. empty hyperlinks: unwrap (keep any runs), Kindle shows nothing for them
ne = 0
for h in list(d.element.body.iter(qn('w:hyperlink'))):
    if ''.join(x.text or '' for x in h.iter(qn('w:t'))).strip() == '' and not list(h.iter(qn('w:drawing'))):
        par = h.getparent()
        for ch in list(h): h.addprevious(ch)
        par.remove(h); ne += 1
# 11. sources as keyword links (Open Library for books, DOI or arXiv for papers), no visible URLs
OL = 'https://openlibrary.org/works/'
def linkify(p, phrase, url):
    for r in p._p.iter(qn('w:r')):
        if r.getparent().tag == qn('w:hyperlink'): continue
        t = r.find(qn('w:t'))
        if t is None or not t.text or phrase not in t.text: continue
        a, b = t.text.split(phrase, 1); rpr = r.find(qn('w:rPr'))
        def mk(text, link=False):
            nr = OxmlElement('w:r'); rp = copy.deepcopy(rpr) if rpr is not None else OxmlElement('w:rPr')
            if link:
                for c in list(rp):
                    if c.tag in (qn('w:color'), qn('w:u')): rp.remove(c)
                c = OxmlElement('w:color'); c.set(qn('w:val'), '0563C1'); rp.append(c)
                u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rp.append(u)
            if len(rp): nr.append(rp)
            nt_ = OxmlElement('w:t'); nt_.set(qn('xml:space'), 'preserve'); nt_.text = text; nr.append(nt_); return nr
        h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), d.part.relate_to(url, RT, is_external=True)); h.set(qn('w:history'), '1'); h.append(mk(phrase, True))
        if a: r.addprevious(mk(a))
        r.addprevious(h)
        if b: r.addprevious(mk(b))
        r.getparent().remove(r); return
    raise AssertionError((phrase, p.text[:90]))
L = [  # (paragraph start, phrase, url)
 ('2. The flux-quantization argument', 'Collective Electrodynamics: Quantum Foundations of Electromagnetism', OL + 'OL9170810W'),
 ('Accessible. Richard Feynman', 'QED: The Strange Theory of Light and Matter', OL + 'OL271752W'),
 ('Intermediate. Carver Mead', 'Collective Electrodynamics: Quantum Foundations of Electromagnetism', OL + 'OL9170810W'),
 ('Intermediate. Carver Mead', 'Introduction to Electrodynamics', OL + 'OL1999763W'),
 ('Advanced. Michael E. Peskin', 'An Introduction to Quantum Field Theory', OL + 'OL4790920W'),
 ('Advanced. Michael E. Peskin', 'Quantum Field Theory and the Standard Model', OL + 'OL26347833W'),
 ('Collective Electrodynamics: Quantum Foundations of Electromagnetism, by Carver Mead', 'Collective Electrodynamics: Quantum Foundations of Electromagnetism', OL + 'OL9170810W'),
 ('On the Einstein Podolsky Rosen Paradox, by John S. Bell', 'On the Einstein Podolsky Rosen Paradox', 'https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195'),
 ('QED: The Strange Theory of Light and Matter, by Richard Feynman', 'QED: The Strange Theory of Light and Matter', OL + 'OL271752W'),
 ('Quantum Computing for Everyone, by Chris Bernhardt', 'Quantum Computing for Everyone', OL + 'OL20156617W'),
 ('Quantum Mechanics: The Theoretical Minimum, by Leonard Susskind', 'Quantum Mechanics: The Theoretical Minimum', OL + 'OL19333423W'),
 ('Something Deeply Hidden, by Sean Carroll', 'Something Deeply Hidden', OL + 'OL20128006W'),
 ('Spooky Action at a Distance, by George Musser', 'Spooky Action at a Distance', OL + 'OL19655016W'),
 ('The Anthropic Cosmological Principle, by John D. Barrow', 'The Anthropic Cosmological Principle', OL + 'OL865340W'),
 ('The Black Hole War, by Leonard Susskind', 'The Black Hole War', OL + 'OL5827350W'),
 ('The Fabric of the Cosmos, by Brian Greene', 'The Fabric of the Cosmos', OL + 'OL1909291W'),
 ('The Theory of Almost Everything, by Robert Oerter', 'The Theory of Almost Everything', OL + 'OL7954525W'),
 ('Abrikosov, A. A.', 'On the Magnetic Properties of Superconductors of the Second Group', 'https://jetp.ras.ru/cgi-bin/dn/e_005_06_1174.pdf'),
 ('Barrow, John D., and Frank J. Tipler', 'The Anthropic Cosmological Principle', OL + 'OL865340W'),
 ('Bennett, Charles H., and Gilles Brassard', 'Quantum Cryptography: Public Key Distribution and Coin Tossing', 'https://doi.org/10.1016/j.tcs.2014.05.025'),
 ('Casimir, H. B. G.', 'On the Attraction Between Two Perfectly Conducting Plates', 'https://dwc.knaw.nl/DL/publications/PU00018547.pdf'),
 ('Christenson, J. H.', 'Evidence for the 2\u03c0 Decay of the K\u2082\u2070 Meson', 'https://doi.org/10.1103/PhysRevLett.13.138'),
 ('Close, Frank.', 'The Cosmic Onion: Quarks and the Nature of the Universe', OL + 'OL4082416W'),
 ('Feynman, Richard P. QED', 'QED: The Strange Theory of Light and Matter', OL + 'OL271752W'),
 ('Fleisch, Daniel A.', 'A Student\u2019s Guide to Maxwell\u2019s Equations', OL + 'OL281805W'),
 ('Griffiths, David J. Introduction to Electrodynamics', 'Introduction to Electrodynamics', OL + 'OL1999763W'),
 ('Griffiths, David J., and Darrell F. Schroeter', 'Introduction to Quantum Mechanics', OL + 'OL1999759W'),
 ('Lamoreaux, S. K.', 'Demonstration of the Casimir Force in the 0.6 to 6 \u03bcm Range', 'https://doi.org/10.1103/PhysRevLett.78.5'),
 ('Mead, Carver A.', 'Collective Electrodynamics: Quantum Foundations of Electromagnetism', OL + 'OL9170810W'),
 ('Nielsen, Michael A., and Isaac L. Chuang', 'Quantum Computation and Quantum Information', OL + 'OL13301633W'),
 ('Peskin, Michael E., and Daniel V. Schroeder', 'An Introduction to Quantum Field Theory', OL + 'OL4790920W'),
 ('Reichenbach, Hans. Philosophic', 'Philosophic Foundations of Quantum Mechanics', OL + 'OL70836W'),
 ('Reichenbach, Hans. The Philosophy', 'The Philosophy of Space and Time', OL + 'OL18432059W'),
 ('Reichenbach, Hans. The Direction', 'The Direction of Time', OL + 'OL70835W'),
 ('Reichenbach, Hans. Experience', 'Experience and Prediction: An Analysis of the Foundations and the Structure of Knowledge', OL + 'OL70840W'),
 ('Schwartz, Matthew D.', 'Quantum Field Theory and the Standard Model', OL + 'OL26347833W'),
 ('Shor, Peter W. \u201cAlgorithms', 'Algorithms for Quantum Computation: Discrete Logarithms and Factoring', 'https://doi.org/10.1109/SFCS.1994.365700'),
 ('\u2019t Hooft, Gerard.', 'Dimensional Reduction in Quantum Gravity', 'https://arxiv.org/abs/gr-qc/9310026'),
 ('Tinkham, Michael.', 'Introduction to Superconductivity', OL + 'OL2931765W'),
]
for start, phrase, url in L:
    h = [p for p in P if p.text.startswith(start)]; assert len(h) == 1, (start, len(h))
    linkify(h[0], phrase, url)
i = one(lambda s: s.startswith('Bennett, Charles H., and Gilles Brassard'))
rep(P[i], '(1984): 175\u2013179.', '(1984): 175\u2013179. Reprinted in Theoretical Computer Science 560 (2014): 7\u201311.')
d.save(DST)
print('double-space runs', n2, 'trailing', nt, 'doubled stops', nd, 'empty links unwrapped', ne, 'source links added', len(L))
