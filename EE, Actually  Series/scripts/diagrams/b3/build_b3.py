"""EE Book 3 (Semiconductor Physics and Devices): duplicate worked-example numbers fixed, 22 new diagrams,
hooks, 'Where you meet this', From the Bench, What You'll Actually Use. Usage: python3 build_b3.py <old master> <out.docx>"""
import sys, re, json, docx
sys.path.insert(0, '../common')
from eedoc import *
from eebuild import *
from urllib.parse import quote_plus
src, out = sys.argv[1], sys.argv[2]
d = docx.Document(src)
# ---- 0. typography: 10^16 -> 10¹⁶ and calculator output 1.0e+04 -> 1.0×10⁴ (Kindle shows carets literally)
SUP = str.maketrans('0123456789-', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻')
typo = 0
for p in body_ps(d):
    typo += re_sub_para(p, r'\b10\^(\d+)\b(?!\.\d)', lambda m: '10' + m.group(1).translate(SUP))
    typo += re_sub_para(p, r'\b(\d+\.\d+)e([+-])(\d+)\b', lambda m: m.group(1) + '×10' + (('-' if m.group(2) == '-' else '') + str(int(m.group(3)))).translate(SUP))
# ---- 1. every chapter from 7 on ended with a second "Worked Example N.1"; give it the next free number
ren = {}
for n, (h, nxt) in chapters(d).items():
    wes = [e for e in seg(h, nxt) if e.tag == W('p') and sty(e) == 'Heading2' and re.match(r'Worked Example %d\.\d+$' % n, ptext(e).strip())]
    seen = set(); top = max([int(ptext(e).split('.')[-1]) for e in wes] or [0])
    for e in wes:
        k = int(ptext(e).split('.')[-1])
        if k in seen:
            top += 1; re_sub_para(e, r'\d+\.\d+$', '%d.%d' % (n, top)); ren[n] = top
        seen.add(k)
# references that point at the renumbered (later) example, checked one by one against its content
REF = [('Find the gain of the stage in Worked Example 9.1', '9.1', '9.5'),
       ('For the transistor of Worked Example 10.1, what threshold', '10.1', '10.4'),
       ('For the core of Worked Example 15.1', '15.1', '15.5'),
       ('The diode of Worked Example 18.1 is operated at zero bias', '18.1', '18.6'),
       ('Repeat Worked Example 19.1 at 15 A rms', '19.1', '19.3')]
for p in body_ps(d):
    for key, a, b in REF:
        if key in ptext(p): assert ren.get(int(a.split('.')[0])) == int(b.split('.')[1]); re_sub_para(p, r'Worked Example ' + re.escape(a), 'Worked Example ' + b)
# ---- 2. figures: after the first paragraph of the named section, past any equation lines (+k = k more paragraphs)
def eqlike(t): t = t.strip(); return 0 < len(t) < 140 and ('=' in t or '≈' in t) and not t.endswith('.')
def anchor3(a):
    m = re.match(r'H:(.*?)(?:\+(\d+))?$', a); key, extra = m.group(1), int(m.group(2) or 0)
    ps = body_ps(d); hits = [i for i, p in enumerate(ps) if sty(p).startswith('Heading') and ptext(p).startswith(key)]
    if len(hits) != 1: raise SystemExit('anchor %r matched %d' % (a, len(hits)))
    i = hits[0] + 1
    while not ptext(ps[i]).strip(): i += 1
    while eqlike(ptext(ps[i + 1])): i += 1
    i += extra
    assert not sty(ps[i]).startswith('Heading'), a
    return ps[i]
from content_b3 import C, FIGS
refs = [(anchor3(a), f, cap, alt) for a, f, cap, alt in FIGS]
figures(d, refs, 'fig')
mp = renumber_figures(d)
# ---- 3. warm-up content
counts = warm(d, C)
d.save(out)
# ---- 4. link rules: Appendix D titles -> Open Library (books) or Crossref (papers); Also-by -> Amazon Kindle search
OL = lambda t, a: 'https://openlibrary.org/search?q=' + quote_plus(t + ' ' + a)
CR = lambda t: 'https://search.crossref.org/?q=' + quote_plus(t)
SRC = {'Sze and Ng, Physics': [('Physics of Semiconductor Devices', OL, 'Sze'), ('Semiconductor Device Fundamentals', OL, 'Pierret'),
          ('Solid State Electronic Devices', OL, 'Streetman'), ('Semiconductor Material and Device Characterization', OL, 'Schroder')],
       'Chapter 7: Cripps': [('RF Power Amplifiers for Wireless Communications', OL, 'Cripps'), ('Advanced Techniques in RF Power Amplifier Design', OL, 'Cripps'),
          ('RF and Microwave Transmitter Design', OL, 'Grebennikov'), ('Switchmode RF and Microwave Power Amplifiers', OL, 'Grebennikov'),
          ('Gallium Nitride Electronics', OL, 'Quay'), ('Microwave Transistor Amplifiers', OL, 'Gonzalez'), ('Nonlinear Microwave and RF Circuits', OL, 'Maas'),
          ('Fundamentals of Power Electronics', OL, 'Erickson')],
       'Tietze, Schenk, and Gamm, Halbleiter': [('Halbleiter-Schaltungstechnik', OL, 'Tietze'), ('Microelectronic Circuits', OL, 'Sedra'),
          ('Analysis and Design of Analog Integrated Circuits', OL, 'Gray'), ('Fundamentals of Modern VLSI Devices', OL, 'Taur'), ('Nanometer CMOS ICs', OL, 'Veendrick')],
       'Razavi, Design': [('Design of Analog CMOS Integrated Circuits', OL, 'Razavi'), ('Analog Integrated Circuit Design', OL, 'Johns'),
          ('Matching Properties of MOS Transistors', CR, None), ('Low-Noise Electronic System Design', OL, 'Motchenbacher')],
       'Rabaey, Chandrakasan': [('Digital Integrated Circuits', OL, 'Rabaey'), ('CMOS VLSI Design', OL, 'Weste'), ('Memory Systems', OL, 'Jacob'),
          ('ESD in Silicon Integrated Circuits', OL, 'Amerasekera')],
       'Sze and Ng for recombination': [('Light-Emitting Diodes', OL, 'Schubert'), ('Photodiode Amplifiers', OL, 'Graeme'),
          ('Fundamentals of Power Semiconductor Devices', OL, 'Baliga')],
       'Plummer, Deal, and Griffin': [('Silicon VLSI Technology', OL, 'Plummer'), ('Thin Film Resonator Technology', CR, None),
          ('Enhancement of Piezoelectric Response in Scandium Aluminum Nitride Alloy Thin Films', CR, None),
          ('RF Bulk Acoustic Wave Filters for Communications', OL, 'Hashimoto'), ('FinFET Modeling for IC Simulation and Design', OL, 'Chauhan'),
          ('An Integral Charge Control Model of Bipolar Transistors', CR, None)]}
rules = []
for inn, L in SRC.items():
    for t, fn, a in L:
        url = fn(t) if a is None else fn(t, a)
        rules.append({'find': t, 'to': '[%s](%s)' % (t, url), 'in': inn, 'max': 1})
from mklinks import alsoby_rules
rules += alsoby_rules(out)
links_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'publishing', 'kindle-links', 'kindle_links - Semiconductor_Physics_and_Devices_Book3.json'))
json.dump({'note': 'EE Book 3 link rules (11 Oct 2026): Appendix D book titles -> Open Library search, papers -> Crossref search, Also-by -> Amazon Kindle search; keyword links, hidden URLs.', 'rules': rules},
          open(links_path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('typography', typo, 'renumbered WE', ren, counts, 'figures', len(refs), 'links', len(rules))
