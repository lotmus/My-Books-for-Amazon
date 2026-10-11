"""Quantum, Actually Vol 2 (A QED Course): strict rescore fixes, 10 Oct 2026 (careful sampled reread).
Usage: python rescore_2026-10-10.py IN.docx OUT.docx"""
import sys, re, copy, docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
SRC, DST = sys.argv[1:3]
d = docx.Document(SRC); P = d.paragraphs

# 1. curly quotes in prose (equations are OMML and untouched), as in Volume 1
ELIS = re.compile(r"(em|tis|twas|til|cause|n|ere|ow|im|er)\b|\d\d?s\b|\d\d\b", re.I)
OPEN_BEFORE = set(' \t\n([{\u2014\u2013-/\u201c\u2018')
def curl(s):
    out = list(s)
    for k, c in enumerate(s):
        prev = s[k-1] if k else ' '; nxt = s[k+1] if k + 1 < len(s) else ' '
        if c == '"':
            out[k] = '\u201c' if (prev in OPEN_BEFORE or k == 0) and not nxt.isspace() else '\u201d'
            if prev in OPEN_BEFORE and nxt.isspace(): out[k] = '\u201d' if k else '\u201c'
        elif c == "'":
            if prev.isalnum() and nxt.isalnum(): out[k] = '\u2019'
            elif prev in OPEN_BEFORE or k == 0: out[k] = '\u2019' if ELIS.match(s[k+1:]) else '\u2018'
            else: out[k] = '\u2019'
    return ''.join(out)
nq = 0
for p in d.element.body.iter(qn('w:p')):
    ts = list(p.iter(qn('w:t'))); full = ''.join(t.text or '' for t in ts)
    if '"' not in full and "'" not in full: continue
    new = curl(full); pos = 0
    for t in ts:
        L = len(t.text or '')
        if L: t.text = new[pos:pos + L]
        pos += L
    nq += 1
for s in d.sections:
    for part in (s.header, s.footer):
        for t in part._element.iter(qn('w:t')):
            if t.text and ('"' in t.text or "'" in t.text): t.text = curl(t.text)

# 2. the nine opening chapters are no longer called prologues (headings and TOC already say Opening Chapter)
REPL = [(r'\bPrologues (\d)', r'Opening Chapters \1'), (r'Opening Chapters 8 an\b', 'Opening Chapters 8 an'),
        (r'\bthe last of the four prologues that follow', 'the last of the six opening chapters that follow'),
        (r'\bthis whole prologue\b', 'this whole chapter'), (r'\bthis prologue\u2019s\b', 'this chapter\u2019s'),
        (r'\b([Tt]his) prologue\b', r'\1 chapter'), (r'\bthe next prologue\b', 'the next chapter'),
        (r'\bof this prologue\b', 'of this chapter'), (r'\bin this prologue\b', 'in this chapter'),
        (r'\bfor this prologue\b', 'for this chapter'), (r'\bend of the prologue\b', 'end of the chapter')]
npro = 0
for t in d.element.body.iter(qn('w:t')):
    if t.text and 'rologue' in t.text:
        s = t.text
        for a, b in REPL: s = re.sub(a, b, s)
        if s != t.text: t.text = s; npro += 1
left = [p.text[:90] for p in P if re.search(r'prologue|Prologues', p.text)]
assert not left, left

# 3. double spaces in prose
n2 = 0
for t in d.element.body.iter(qn('w:t')):
    if t.text and '  ' in t.text:
        s = re.sub(r'(?<=\S)  +(?=\S)', ' ', t.text)
        if s != t.text: t.text = s; n2 += 1

# 4. in-text citations: first mention of each Bibliography work links to its entry
BMID = [900000]
def bookmark(p, name):
    BMID[0] += 1
    a = OxmlElement('w:bookmarkStart'); a.set(qn('w:id'), str(BMID[0])); a.set(qn('w:name'), name)
    b = OxmlElement('w:bookmarkEnd'); b.set(qn('w:id'), str(BMID[0]))
    ppr = p._p.find(qn('w:pPr')); (ppr.addnext(a) if ppr is not None else p._p.insert(0, a)); p._p.append(b)
def wrap(p, phrase, anchor):
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
            x = OxmlElement('w:t'); x.set(qn('xml:space'), 'preserve'); x.text = text; nr.append(x); return nr
        h = OxmlElement('w:hyperlink'); h.set(qn('w:anchor'), anchor); h.set(qn('w:history'), '1'); h.append(mk(phrase, True))
        if a: r.addprevious(mk(a))
        r.addprevious(h)
        if b: r.addprevious(mk(b))
        r.getparent().remove(r); return True
    return False
bib = [i for i, p in enumerate(P) if p.text == 'Bibliography' and p.style.name == 'Heading 1'][0]
CITE = [('Easy QED (opening)', 'bib_feynman_qed', 'Strange Theory of Light and Matter'),
        ('Single-photon interference', 'bib_grangier', 'Grangier'),
        ('Mead\u2019s view (Interlude)', 'bib_mead', 'Collective Electrodynamics'),
        ('Lamb\u2013Retherford interval', 'bib_lamb', 'Lamb and Retherford'),
        ('Bethe logarithm', 'bib_bethe', 'Bethe'),
        ('Uehling potential', 'bib_uehling', 'Uehling'),
        ('Bloch\u2013Nordsieck IR', 'bib_bloch', 'Bloch\u2013Nordsieck'),
        ('Constants', 'bib_codata', 'CODATA')]
nc = 0; missing = []
for start, name, phrase in CITE:
    hit = [i for i in range(bib, len(P)) if P[i].text.startswith(start + ' \u2014')]; assert len(hit) == 1, start
    bookmark(P[hit[0]], name)
    for i in range(170, bib):
        if P[i].style.name.startswith('Heading'): continue
        if wrap(P[i], phrase, name): nc += 1; break
    else: missing.append(phrase)
d.save(DST)
print('quote paras', nq, 'prologue refs', npro, 'double spaces', n2, 'citation links', nc, 'not linkable', missing)
