"""Build EE Book 9, Test and Measurement Instruments, from its tagged sources (modeled on build_b8.py).

The Book 5 master is opened read-only as a style template (styles, numbering, page setup); its body is
discarded. Sources: chapters/Book9/src (front.txt, ch01..ch38.txt, back.txt), listings and figures in
scripts/diagrams/b9 (figs_b9.py, figs_b9_labview.py; numbers checked by check_numbers_b9.py). Shared helpers are imported read-only from scripts/diagrams/common.

Tags: PART, PINTRO, H1, H2, P (the first P of a chapter is its hook), MEET, EQ, WE, PROB, SOL, KEY, MIS, BENCH,
JOB, AI, BOXH/BOXL, LI, CODE: file | caption, FIG: file | caption | alt, PP, ANS (collected into Appendix B),
USE1/USE2; front: TITLE, SERIES, AUTHOR, COPY, SUB; back: BOXCOPY, ANSWERS, SRC, REVIEW, ALSOG, ALSOT.

Usage: python build_b9.py [--template T.docx] [--src DIR] [--listings DIR] [--figs DIR] [--common DIR]
                          [--out OUT.docx] [--links OUT.json] [--chapters N]   (N < 38: partial proof build)
"""
import argparse, copy, json, os, re, sys
from urllib.parse import quote_plus

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ap = argparse.ArgumentParser()
ap.add_argument('--template', default=os.path.join(ROOT, 'Communications_Wireless_and_SDR_Book5.docx'))
ap.add_argument('--src', default=os.path.join(ROOT, 'chapters', 'Book9', 'src'))
ap.add_argument('--listings', default=os.path.join(HERE, 'diagrams', 'b9', 'listings'))
ap.add_argument('--figs', default=os.path.join(HERE, 'diagrams', 'b9', 'fig'))
ap.add_argument('--common', default=os.path.join(HERE, 'diagrams', 'common'))
ap.add_argument('--out', default=os.path.join(ROOT, 'Test_and_Measurement_Instruments_Book9.docx'))
ap.add_argument('--links', default=os.path.join(ROOT, 'kindle_links - Test_and_Measurement_Instruments_Book9.json'))
ap.add_argument('--chapters', type=int, default=38)
A = ap.parse_args()
sys.path.insert(0, A.common)
import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from eedoc import W, sty, ptext, body_ps, mkrun, mkpara, picture_para
from eebuild import bullet_numid

FIG_WIDTH_IN = 5.6
SHADE = {'bench': 'E8F1E4', 'job': 'E3ECF7', 'ai': 'FDF0DC', 'box': 'F2F2F2', 'code': 'F4F4F4'}
HINGE = re.compile(r'(?i)\b(clearly|obviously|simply|of course|it is easy to see)\b|\bjust\b')

# ---------------------------------------------------------------- template
d = docx.Document(A.template)
body = d.element.body
tps = body_ps(d)
TITLE_PS = [copy.deepcopy(p) for p in tps[:5]]          # title, series, author, copyright, subtitle
assert ptext(TITLE_PS[1]).startswith('Book 5 of the'), ptext(TITLE_PS[1])
def first_rpr(style):
    p = next(p for p in tps if sty(p) == style)
    r = p.find(W('r')); rp = r.find(W('rPr')) if r is not None else None
    return copy.deepcopy(rp) if rp is not None else None
HRPR = {s: first_rpr(s) for s in ('Heading1', 'Heading2', 'Heading3')}
for e in list(body):
    if e.tag != W('sectPr'):
        body.remove(e)
for rid, rel in list(d.part.rels.items()):          # drop the template's images and links
    if rel.reltype.endswith('/image') or rel.reltype.endswith('/hyperlink'):
        d.part.drop_rel(rid)
BUL = bullet_numid(d)
SECT = body.find(W('sectPr'))
def add(*els):
    for e in els:
        SECT.addprevious(e)

# ---------------------------------------------------------------- paragraph builders
BM = {'id': 900, 'n': 0}
TOC = []                                             # (text, bookmark)
def heading(text, level, toc=False):
    rp = HRPR.get('Heading%d' % level)
    p = mkpara([mkrun(text, rpr=rp)], style='Heading%d' % level)
    if toc:
        BM['id'] += 1; BM['n'] += 1; name = '_TocAll%04d' % BM['n']
        bs = OxmlElement('w:bookmarkStart'); bs.set(W('id'), str(BM['id'])); bs.set(W('name'), name)
        be = OxmlElement('w:bookmarkEnd'); be.set(W('id'), str(BM['id']))
        p.find(W('pPr')).addnext(bs); bs.addnext(be)
        TOC.append((text, name))
    return p
def para(text, after=160):
    return mkpara([mkrun(text)], spacing={'after': after})
def labeled(label, text, after=160):
    return mkpara([mkrun(label, bold=True), mkrun(text)], spacing={'after': after})
def shaded(title, text, fill):
    return [mkpara([mkrun(title, bold=True)], shade=fill, spacing={'after': 80, 'before': 120}),
            mkpara([mkrun(text)], shade=fill, spacing={'after': 120})]
def bullet(text):
    return mkpara([mkrun(text)], style='ListParagraph', num=BUL, spacing={'after': 60})
def centered(text, font=None):
    rp = None
    if font:
        rp = OxmlElement('w:rPr'); f = OxmlElement('w:rFonts')
        for k in ('ascii', 'hAnsi', 'cs'):
            f.set(W(k), font)
        rp.append(f)
    p = mkpara([mkrun(text, rpr=rp)], spacing={'after': 160, 'before': 80})
    jc = OxmlElement('w:jc'); jc.set(W('val'), 'center'); p.find(W('pPr')).append(jc)
    return p
def code_block(path):
    lines = open(path, encoding='utf8').read().replace('\t', '    ').rstrip('\n').split('\n')
    rp = OxmlElement('w:rPr'); f = OxmlElement('w:rFonts')
    for k in ('ascii', 'hAnsi', 'cs'):
        f.set(W(k), 'Consolas')
    rp.append(f)
    for tag in ('sz', 'szCs'):
        e = OxmlElement('w:' + tag); e.set(W('val'), '16'); rp.append(e)
    p = mkpara([], shade=SHADE['code'], spacing={'after': 200, 'before': 40, 'line': 240, 'lineRule': 'auto'})
    ind = OxmlElement('w:ind'); ind.set(W('left'), '144'); ind.set(W('right'), '144'); p.find(W('pPr')).append(ind)
    for i, line in enumerate(lines):
        r = mkrun(line, rpr=rp)
        if i:
            r.insert(1, OxmlElement('w:br'))
        p.append(r)
    return p, len(lines)
def listing_label(num, part, caption):
    lab = 'Listing %s%s — ' % (num, (', part %d' % part) if part else '')
    return mkpara([mkrun(lab, bold=True), mkrun(caption)], spacing={'after': 60, 'before': 160}, )

# ---------------------------------------------------------------- read sources
def tagged(path):
    out = []
    for raw in open(path, encoding='utf8'):
        line = raw.rstrip('\n')
        if not line.strip():
            continue
        m = re.match(r'^([A-Z0-9]+): ?(.*)$', line)
        assert m, (path, line[:80])
        out.append((m.group(1), m.group(2)))
    return out
CH = [tagged(os.path.join(A.src, 'ch%02d.txt' % n)) for n in range(1, A.chapters + 1)]
FRONT = tagged(os.path.join(A.src, 'front.txt'))
BACK = tagged(os.path.join(A.src, 'back.txt'))
F = dict((t, v) for t, v in FRONT if t in ('TITLE', 'SERIES', 'AUTHOR', 'COPY', 'SUB'))

# ---------------------------------------------------------------- title page
def retext(p, text):
    ts = list(p.iter(W('t')))
    ts[0].text = text
    for t in ts[1:]:
        t.getparent().remove(t)
for p, key in zip(TITLE_PS, ('TITLE', 'SERIES', 'AUTHOR', 'COPY', 'SUB')):
    retext(p, F[key]); add(p)

# ---------------------------------------------------------------- How to Use, then a Contents placeholder
for t, v in FRONT:
    if t == 'H1':
        add(heading(v, 1))
    elif t == 'P':
        add(para(v))
toc_anchor = heading('Contents', 1); add(toc_anchor)
toc_end = mkpara([]); add(toc_end)

# ---------------------------------------------------------------- chapters
stats = dict(figs=0, listings=0, listing_files=0, code_lines=0, we=0, pp=0, bench=0, job=0, ai=0, hooks=0, use=0)
ANS = {}
CODEPS = set()
for n, items in enumerate(CH, 1):
    fig_k = 0; lst_k = {}; first_p = True; use1 = []; use2 = []
    groups = {}
    for t, v in items:                                  # listing numbering: files with the same lNN_K share a number
        if t == 'CODE':
            k = int(re.match(r'l\d+_(\d+)', v.split('|')[0].strip()).group(1))
            groups.setdefault(k, []).append(v)
    seen = {}
    i = 0
    while i < len(items):
        t, v = items[i]
        if t == 'PART':
            add(heading(v, 1, toc=True))
        elif t == 'PINTRO':
            add(para(v, after=200))
        elif t == 'H1':
            assert v.startswith('Chapter %d. ' % n), v
            add(heading(v, 1, toc=True))
        elif t == 'H2':
            add(heading(v, 2))
        elif t == 'P':
            add(para(v))
            if first_p:
                stats['hooks'] += 1; first_p = False
        elif t == 'MEET':
            add(labeled('Where you meet this: ', v, after=200))
        elif t == 'EQ':
            add(centered(v, font='Cambria Math'))
        elif t == 'WE':
            add(heading(v, 2)); stats['we'] += 1
        elif t == 'PROB':
            add(labeled('Problem. ', v))
        elif t == 'SOL':
            add(labeled('Solution. ', v))
        elif t == 'KEY':
            add(labeled('Key idea. ', v))
        elif t == 'MIS':
            add(labeled('Common misconception. ', v))
        elif t == 'BENCH':
            add(*shaded('From the Bench', v, SHADE['bench'])); stats['bench'] += 1
        elif t == 'JOB':
            add(*shaded('On the Job', v, SHADE['job'])); stats['job'] += 1
        elif t == 'AI':
            add(*shaded('AI Pair-Programming Note', v, SHADE['ai'])); stats['ai'] += 1
        elif t == 'BOXH':
            add(mkpara([mkrun(v, bold=True)], shade=SHADE['box'], spacing={'after': 60, 'before': 160}))
        elif t == 'BOXL':
            p = bullet(v); pp = p.find(W('pPr'))
            sh = OxmlElement('w:shd'); sh.set(W('fill'), SHADE['box']); sh.set(W('val'), 'clear')
            pp.find(W('numPr')).addnext(sh); add(p)
        elif t == 'LI':
            p = para(v, after=60); ind = OxmlElement('w:ind'); ind.set(W('left'), '360'); p.find(W('pPr')).append(ind); add(p)
        elif t == 'CODE':
            fn, cap = [x.strip() for x in v.split('|', 1)]
            k = int(re.match(r'l\d+_(\d+)', fn).group(1))
            if k not in lst_k:
                lst_k[k] = len(lst_k) + 1; stats['listings'] += 1
            assert lst_k[k] == k, (n, fn)
            seen[k] = seen.get(k, 0) + 1
            part = seen[k] if len(groups[k]) > 1 else 0
            cb, nl = code_block(os.path.join(A.listings, fn)); CODEPS.add(cb)
            add(listing_label('%d.%d' % (n, k), part, cap), cb)
            stats['listing_files'] += 1; stats['code_lines'] += nl
        elif t == 'FIG':
            fn, cap, alt = [x.strip() for x in v.split('|')]
            fig_k += 1
            assert re.match(r'Figure %d\.\? — ' % n, cap), cap
            cap = cap.replace('Figure %d.?' % n, 'Figure %d.%d' % (n, fig_k), 1)
            add(*picture_para(d, os.path.join(A.figs, fn), FIG_WIDTH_IN, cap.split(' — ')[0], alt, cap))
            stats['figs'] += 1
        elif t == 'PP':
            m = re.match(r'(\d+\. )(.*)$', v); add(mkpara([mkrun(m.group(1), bold=True), mkrun(m.group(2))], spacing={'after': 120}))
            stats['pp'] += 1
        elif t == 'ANS':
            ANS.setdefault(n, []).append(v)
        elif t == 'USE1':
            use1.append(v)
        elif t == 'USE2':
            use2.append(v)
        else:
            raise SystemExit('unknown tag %s in chapter %d' % (t, n))
        i += 1
    assert use1, n
    add(mkpara([mkrun('What You\u2019ll Actually Use', rpr=HRPR['Heading3'])], style='Heading3', spacing={'after': 120, 'before': 280}),
        mkpara([mkrun('Everyday working tools', bold=True)], spacing={'after': 60}), *[bullet(x) for x in use1])
    if use2:
        add(mkpara([mkrun('Mostly for exams and deeper study', bold=True)], spacing={'after': 60, 'before': 120}), *[bullet(x) for x in use2])
    stats['use'] += 1
    npp = sum(1 for t, _ in items if t == 'PP')
    assert len(ANS.get(n, [])) == npp, (n, npp, len(ANS.get(n, [])))

# ---------------------------------------------------------------- back matter
def box_lines(chfile, prefix):
    items = tagged(os.path.join(A.src, chfile)); out = []; on = False
    for t, v in items:
        if t == 'BOXH':
            on = v.startswith(prefix)
            continue
        if t == 'BOXL' and on:
            out.append(v)
        elif on and t != 'BOXL':
            on = False
    assert out, (chfile, prefix)
    return out
also_start = None
for t, v in BACK:
    if t == 'H1':
        add(heading(v, 1, toc=True))
    elif t == 'H2':
        add(heading(v, 2))
    elif t == 'P':
        add(para(v))
    elif t == 'BOXCOPY':
        f_, pre = [x.strip() for x in v.split('|')]
        add(*[bullet(x) for x in box_lines(f_, pre)])
    elif t == 'ANSWERS':
        add(heading(v, 1, toc=True))
        add(para('Each solution shows the working and, where one is common, the usual mistake. Problems are numbered as in their chapter.'))
        for n in range(1, A.chapters + 1):
            add(heading('Chapter %d' % n, 2))
            for a in ANS[n]:
                m = re.match(r'(\d+\. )(.*)$', a)
                add(mkpara([mkrun(m.group(1), bold=True), mkrun(m.group(2))], spacing={'after': 120}))
    elif t == 'SRC':
        add(para(v, after=120))
    elif t == 'REVIEW':
        add(mkpara([mkrun(v, italic=True)], spacing={'after': 200, 'before': 240}))
    elif t == 'ALSOG':
        p = mkpara([mkrun(v, bold=True)], spacing={'after': 60, 'before': 160}); add(p)
    elif t == 'ALSOT':
        add(mkpara([mkrun(v)], spacing={'after': 40}))
    else:
        raise SystemExit('unknown back tag ' + t)

# ---------------------------------------------------------------- contents (linked, no page numbers)
for text, name in TOC:
    h = OxmlElement('w:hyperlink'); h.set(W('anchor'), name); h.set(W('history'), '1')
    h.append(mkrun(text)); p = mkpara([]); p.append(h); toc_end.addprevious(p)
toc_end.getparent().remove(toc_end)

# ---------------------------------------------------------------- metadata, checks, save
cp = d.core_properties
cp.title = F['TITLE']; cp.subject = F['SUB']; cp.author = 'Lothar J. Musiol'; cp.keywords = 'test and measurement; oscilloscope; spectrum analyzer; vector network analyzer; SMU; curve tracer; modulation analysis; SCPI; LabVIEW'
cp.comments = ''; cp.last_modified_by = 'Lothar J. Musiol'
allt = '\n'.join(ptext(p) for p in body_ps(d))
prose = '\n'.join(ptext(p) for p in body_ps(d) if p not in CODEPS)
assert 'Trump' not in allt
assert '`' not in prose
assert 'Book 5 of the' not in allt and 'Communications, Wireless, and SDR' in allt   # only in Also-by
assert 'Book 9 of the' in allt
bad = [prose[max(0, m.start() - 40):m.end() + 40] for m in HINGE.finditer(prose)]
d.save(A.out)

# ---------------------------------------------------------------- kindle_links rules
OL = lambda q: 'https://openlibrary.org/search?q=' + quote_plus(q)
SRC = [v for t, v in BACK if t == 'SRC']
def where(key):
    hits = [s for s in SRC if key in s]
    assert len(hits) == 1, (key, len(hits))
    return hits[0][:60]
LINKS = [
    ('JCGM 100:2008', 'https://www.bipm.org/en/committees/jc/jcgm/publications'),
    ('ILAC-G8:09/2019', 'https://ilac.org/publications-and-resources/ilac-guidance-series/'),
    ('IEC 61010-1', 'https://webstore.iec.ch/en/publication/4279'),
    ('Low Level Measurements Handbook', 'https://www.tek.com/en/documents/product-article/keithley-low-level-measurements-handbook---7th-edition'),
    ('Model 2450 SourceMeter Reference Manual', 'https://www.tek.com/en/products/keithley/source-measure-units/2400-graphical-series-sourcemeter'),
    ('npTDMS documentation', 'https://nptdms.readthedocs.io/'),
    ('Parametric Measurement Handbook', 'https://www.keysight.com/us/en/assets/7018-06784/handbooks/5992-3684.pdf'),
    ('ngspice user\'s manual', 'https://ngspice.sourceforge.io/docs.html'),
    ('Impedance Measurement Handbook', 'https://www.keysight.com/us/en/assets/7018-06840/application-notes/5950-3000.pdf'),
    ('Handbook of Frequency Stability Analysis', 'https://tf.nist.gov/general/pdf/2220.pdf'),
    ('LabVIEW manual', 'https://www.ni.com/docs/en-US/bundle/labview/page/user-manual-welcome.html'),
    ('LabVIEW API reference', 'https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/functions/python-node.html'),
    ('TestStand help', 'https://www.ni.com/en/shop/electronic-test-instrumentation/application-software-for-electronic-test-and-instrumentation-category/what-is-teststand.html'),
    ('nidaqmx Python API reference', 'https://nidaqmx-python.readthedocs.io/'),
    ('PyVISA documentation', 'https://pyvisa.readthedocs.io/'),
    ('ABCs of Probes Primer', 'https://www.tek.com/en/documents/whitepaper/abcs-probes-primer'),
    ('Spectrum Analysis Basics', 'https://www.keysight.com/us/en/assets/7018-06714/application-notes/5952-0292.pdf'),
    ('Noise Figure Measurement Accuracy: The Y-Factor Method', 'https://www.keysight.com/us/en/assets/7018-06829/application-notes/5952-8255.pdf'),
    ('Understanding the Fundamental Principles of Vector Network Analysis', 'https://www.keysight.com/us/en/assets/7018-06841/application-notes/5965-7707.pdf'),
    ('3GPP TS 38.104', 'https://www.3gpp.org/dynareport/38104.htm'),
    ('Bluetooth specifications page', 'https://www.bluetooth.com/specifications/specs/'),
    ('IVI Foundation specifications page', 'https://www.ivifoundation.org/specifications/'),
    ('PyMeasure documentation', 'https://pymeasure.readthedocs.io/'),
    ('OpenHTF documentation', 'https://openhtf.readthedocs.io/'),
    ('tinySA wiki', 'https://tinysa.org/wiki/'),
    ('nanovna.com', 'https://nanovna.com/'),
    ('RTL-SDR Blog V4 datasheet', 'https://www.rtl-sdr.com/wp-content/uploads/2024/12/RTLSDR_V4_Datasheet_V_1_0.pdf'),
    ('HackRF One documentation', 'https://hackrf.readthedocs.io/'),
    ('MicroPython documentation', 'https://docs.micropython.org/'),
]
rules = [{'find': k, 'to': '[%s](%s)' % (k, u), 'in': where(k), 'max': 1} for k, u in LINKS]
from mklinks import alsoby_rules
rules += alsoby_rules(A.out)
json.dump({'note': 'EE Book 9 link rules (11 Oct 2026): Appendix C documentation -> official pages, books -> Open Library search, '
                   'Also-by -> Amazon Kindle search; keyword links, hidden URLs.', 'rules': rules},
          open(A.links, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
stats['toc'] = len(TOC); stats['links'] = len(rules); stats['words'] = len(allt.split())
print('built', A.out); print(stats)
if A.chapters < 38:
    print('PARTIAL proof build: chapters 1-%d only' % A.chapters)
if bad:
    print('hinge words (check context):', bad[:20])
