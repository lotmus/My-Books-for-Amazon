"""Shared build steps for the EE series: reference renumbering, warm-up content, figures, bullets."""
import re, zipfile
from eedoc import *
def bullet_numid(doc):
    x = doc.part.numbering_part.element
    fmt = {}
    for a in x.findall(W('abstractNum')):
        f = a.find('.//' + W('numFmt')); fmt[a.get(W('abstractNumId'))] = f.get(W('val')) if f is not None else ''
    for n in x.findall(W('num')):
        if fmt.get(n.find(W('abstractNumId')).get(W('val'))) == 'bullet': return int(n.get(W('numId')))
    raise SystemExit('no bullet list definition')
def chapters(doc):
    ps = body_ps(doc); H1 = [i for i, p in enumerate(ps) if sty(p) == 'Heading1']; out = {}
    for k, i in enumerate(H1):
        m = re.match(r'Chapter (\d+) —', ptext(ps[i]))
        if m: out[int(m.group(1))] = (ps[i], ps[H1[k+1]] if k+1 < len(H1) else None)
    return out
def seg(h, nxt):
    s = []; e = h.getnext()
    while e is not None and e is not nxt:
        if e.tag == W('p') and sty(e) == 'Heading1': break
        s.append(e); e = e.getnext()
    return s
NUMLIST = r'(\d+)((?:\s*(?:,|and|or|to|–|-|,\s*and)\s*\d+)*)'
REFKW = r'(?:Figures?|Worked Examples?|Examples?|Sections?)'
def renumber(ps, chap, ref):
    """chap(n)->new chapter number; ref(n,k)->'N.K' string for figure/example/section references."""
    def fl(m): return m.group(1) + re.sub(r'\d+', lambda k: str(chap(int(k.group()))), m.group(2) + m.group(3))
    def rl(m): return m.group(1) + re.sub(r'(\d+)\.(\d+)', lambda k: ref(int(k.group(1)), int(k.group(2)), m.group(1)), m.group(2))
    for p in ps:
        re_sub_para(p, r'\b([Cc]hapters?\s+)' + NUMLIST, fl)
        re_sub_para(p, r'\b(' + REFKW + r'\s+)(\d+\.\d+(?:\s*(?:,|and|to|–|-|or)\s*\d+\.\d+)*)', rl)
        re_sub_para(p, r'(§\s?)(\d+\.\d+)', rl)
        if sty(p) in ('Heading2', 'Heading3'):
            re_sub_para(p, r'^(\d+)\.(\d+)', lambda m: ref(int(m.group(1)), int(m.group(2)), 'Section '))
def warm(doc, C, chap_map=None, fill='E8F1E4'):
    BUL = bullet_numid(doc); counts = dict(hook=0, bench=0, use=0)
    for n, (h, nxt) in chapters(doc).items():
        c = C.get(n)
        if not c: continue
        new = [mkpara([mkrun(c['hook'])], spacing={'after': 160})]; counts['hook'] += 1
        if c.get('meet'): new.append(mkpara([mkrun('Where you meet this: ', bold=True), mkrun(c['meet'])], spacing={'after': 200}))
        insert_after(h, new)
        s = [x for x in seg(h, nxt) if x.tag == W('p')]
        last = s[-1]
        while not ptext(last).strip() and not last.findall('.//' + qn('w:drawing')): last = last.getprevious()
        pp = next((x for x in s if sty(x) in ('Heading2', 'Heading3') and ptext(x).strip() in ('Practice Problems', 'Review Questions', 'Exercises')), None)
        if c.get('bench'):
            b = [mkpara([mkrun('From the Bench', bold=True)], shade=fill, spacing={'after': 80, 'before': 120}),
                 mkpara([mkrun(c['bench'])], shade=fill, spacing={'after': 120})]
            if pp is not None: insert_before(pp, b)
            else: insert_after(last, b); last = b[-1]
            counts['bench'] += 1
        ev, dp = c['use']; t = [mkpara([mkrun('What You\u2019ll Actually Use')], style='Heading3', spacing={'after': 120, 'before': 280}),
                                mkpara([mkrun('Everyday working tools', bold=True)], spacing={'after': 60})]
        t += [mkpara([mkrun(x)], style='ListParagraph', num=BUL, spacing={'after': 60}) for x in ev]
        if dp:
            t.append(mkpara([mkrun('Mostly for exams and deeper study', bold=True)], spacing={'after': 60, 'before': 120}))
            t += [mkpara([mkrun(x)], style='ListParagraph', num=BUL, spacing={'after': 60}) for x in dp]
        insert_after(last, t); counts['use'] += 1
    return counts
def figures(doc, refs, figdir, width_in=5.6):
    for ref, f, cap, alt in refs:
        insert_after(ref, picture_para(doc, figdir + '/' + f, width_in, cap.split(' — ')[0], alt, cap))
def jc(p):
    pp = p.find(W('pPr')); j = pp.find(W('jc')) if pp is not None else None
    return j.get(W('val')) if j is not None else ''
def anchor(doc, a):
    """'H:<text>' = heading containing text; 'C:<n>' = chapter heading. Returns the paragraph to insert after:
    the first body paragraph after it, moved past any equations or figures that follow."""
    ps = body_ps(doc)
    if a.startswith('C:'): hits = [i for i, p in enumerate(ps) if sty(p) == 'Heading1' and ptext(p).startswith('Chapter %s —' % a[2:])]
    else: hits = [i for i, p in enumerate(ps) if sty(p).startswith('Heading') and a[2:] in ptext(p)]
    if len(hits) != 1: raise SystemExit('anchor %r matched %d' % (a, len(hits)))
    i = hits[0] + 1
    while not ptext(ps[i]).strip(): i += 1
    while i + 1 < len(ps) and ((jc(ps[i+1]) == 'center' and len(ptext(ps[i+1])) < 160) or ps[i+1].findall('.//' + qn('w:drawing'))) and not sty(ps[i+1]).startswith('Heading'): i += 1
    return ps[i]
def renumber_figures(doc):
    """Number figure captions sequentially within each chapter, and remap text references to existing figures."""
    ps = body_ps(doc); cur = None; k = 0; mp = {}; caps = set()
    for p in ps:
        t = ptext(p)
        m = re.match(r'Chapter (\d+) —', t) if sty(p) == 'Heading1' else None
        if m: cur = int(m.group(1)); k = 0; continue
        if sty(p) == 'Heading1': cur = None
        m = re.match(r'Figure (\d+)\.(\d+|\?) —', t)
        if m and cur:
            k += 1
            if m.group(2) != '?': mp[(int(m.group(1)), int(m.group(2)))] = (cur, k)
            re_sub_para(p, r'^Figure \d+\.(?:\d+|\?)', 'Figure %d.%d' % (cur, k)); caps.add(p)
    for p in ps:
        if p in caps: continue
        re_sub_para(p, r'\b(Figures?\s+)(\d+\.\d+(?:\s*(?:,|and|to|–|-|or)\s*\d+\.\d+)*)', lambda m: m.group(1) + re.sub(r'(\d+)\.(\d+)', lambda q: '%d.%d' % mp.get((int(q.group(1)), int(q.group(2))), (int(q.group(1)), int(q.group(2)))), m.group(2)))
    return mp
