"""EE Book 4 (RF, Microwave, and Transceivers): 41 new diagrams, hooks, 'Where you meet this', From the Bench,
What You'll Actually Use, one statistics fix, keyword links. Usage: python3 build_b4.py <old master> <out.docx> <old links json>"""
import sys, re, json, docx
sys.path.insert(0, '../common')
from eedoc import *
from eebuild import *
from urllib.parse import quote_plus
src, out, oldlinks = sys.argv[1], sys.argv[2], sys.argv[3]
d = docx.Document(src)
# ---- 0. text fix: exp(-10^0.9) = 0.036 %, which rounds to 0.04 %, not 0.03 %
fix = 0
for p in body_ps(d):
    if 'probability that the instantaneous power exceeds the average' in ptext(p):
        fix += re_sub_para(p, r'0\.03 % at 9 dB', '0.04 % at 9 dB')
assert fix == 1, fix
# ---- 1. figures: after the first paragraph of the named section, past any equation lines (+k = k more paragraphs)
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
from content_b4 import C, FIGS
refs = [(anchor3(a), f, cap, alt) for a, f, cap, alt in FIGS]
figures(d, refs, 'fig')
mp = renumber_figures(d)
# ---- 2. warm-up content
counts = warm(d, C)
d.save(out)
# ---- 3. link rules: keep the curated DOI links for papers; add Open Library searches for the books in Appendix C;
#         Also-by -> Amazon Kindle search
OL = lambda t, a: 'https://openlibrary.org/search?q=' + quote_plus(t + ' ' + a)
old = [r for r in json.load(open(oldlinks))['rules'] if 'doi.org' in r.get('to', '')]
BOOKS = [('RF Circuit Design', 'Bowick'), ('Microwave Engineering', 'Pozar'), ('Microwave and RF Design', 'Steer'),
         ('Microwave Transistor Amplifiers', 'Gonzalez'), ('Microwave Filters, Impedance-Matching Networks, and Coupling Structures', 'Matthaei'),
         ('Microstrip Filters for RF/Microwave Applications', 'Hong'), ('Antenna Theory', 'Balanis'), ('Antenna Engineering Handbook', 'Volakis'),
         ('Phased Array Antenna Handbook', 'Mailloux'), ('Microwave Ferrites and Ferrimagnetics', 'Lax'), ('Antenna Measurement Techniques', 'Evans'),
         ('Microwave Mixers', 'Maas'), ('RF Power Amplifiers for Wireless Communications', 'Cripps'), ('Advanced Techniques in RF Power Amplifier Design', 'Cripps'),
         ('Switchmode RF and Microwave Power Amplifiers', 'Grebennikov'), ('High-Linearity RF Amplifier Design', 'Kenington'),
         ('Wireless Receiver Design for Digital Communications', 'McClaning'), ('RF Microelectronics', 'Razavi'), ('Phaselock Techniques', 'Gardner'),
         ('Phase-Locked Loops', 'Best'), ('Introduction to Radar Systems', 'Skolnik'), ('Fundamentals of Radar Signal Processing', 'Richards'),
         ('Practical RF Circuit Design for Modern Wireless Systems', 'Besser'), ('Power Vacuum Tubes Handbook', 'Whitaker'),
         ('Klystrons, Traveling Wave Tubes, Magnetrons, Crossed-Field Amplifiers, and Gyrotrons', 'Gilmour'), ('RF Power Amplifiers', 'Kazimierczuk'),
         ('Behavioral Modeling and Predistortion of Wideband Wireless Transmitters', 'Ghannouchi'), ('PLL Performance, Simulation, and Design', 'Banerjee')]
PAPERS = ['Accurate Models for Microstrip Computer-Aided Design', 'A Simple Model of Feedback Oscillator Noise Spectrum',
          'A New High Efficiency Power Amplifier for Modulated Waves', 'Power Amplifiers and Transmitters for RF and Microwave']
CR = lambda t: 'https://search.crossref.org/?q=' + quote_plus(t)
ps = [ptext(p) for p in body_ps(d)]; i0 = max(i for i, t in enumerate(ps) if t.strip() == 'Appendix C. Sources')
srcs = ps[i0 + 1:i0 + 40]
def where(t):
    for s in srcs:
        if t in s: return s[:60]
    raise SystemExit('source not found: ' + t)
rules = list(old); seen = set()
for t, a in BOOKS:
    # 'RF Power Amplifiers' and 'Microwave Engineering' are prefixes of other titles: match the exact cited paragraph
    rules.append({'find': t, 'to': '[%s](%s)' % (t, OL(t, a)), 'in': where(t + (',' if t in ('RF Power Amplifiers', 'Antenna Theory', 'Microwave Engineering') else '')), 'max': 1})
for t in PAPERS: rules.append({'find': t, 'to': '[%s](%s)' % (t, CR(t)), 'in': where(t), 'max': 1})
from mklinks import alsoby_rules
rules += alsoby_rules(out)
links_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'publishing', 'kindle-links', 'kindle_links - RF_Microwave_and_Transceivers_Book4.json'))
json.dump({'note': 'EE Book 4 link rules (11 Oct 2026): papers -> DOI (curated 10 Oct) or Crossref search, Appendix C books -> Open Library search, Also-by -> Amazon Kindle search; keyword links, hidden URLs.', 'rules': rules},
          open(links_path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('fix', fix, counts, 'figures', len(refs), 'links', len(rules), '(doi kept %d)' % len(old))
