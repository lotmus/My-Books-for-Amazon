"""Quantum, Actually Vol 1, 11 Oct 2026: exercise pass.
Rebuilds REV03 from the REV02 master (now in bak/2026-10-11 pre-exercises/):
  python engine.py batch1,batch2,... out.docx   (set QA1_SRC to the REV02 path)
Each batchN.py holds text FIXES, Try it now checks and end-of-chapter exercises with solutions.
"""
import copy, re, sys, importlib, zipfile, os
import docx
from docx.oxml.ns import qn
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
SRC = os.environ.get('QA1_SRC', '/workspace/qa1x/src/Quantum, Actually - Volume 1_REV02_2026-10-05.docx')
LABEL_COLOR = '1F4E78'

def ptext(p):
    return ''.join(t.text or '' for t in p.iter(qn('w:t')))

def mk_run(text, bold=False, color=None, italic=False):
    r = etree.SubElement(etree.Element(qn('w:dummy')), qn('w:r'))
    if bold or color or italic:
        rpr = etree.SubElement(r, qn('w:rPr'))
        if bold: etree.SubElement(rpr, qn('w:b'))
        if italic: etree.SubElement(rpr, qn('w:i'))
        if color:
            c = etree.SubElement(rpr, qn('w:color')); c.set(qn('w:val'), color)
    t = etree.SubElement(r, qn('w:t')); t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return r

def mk_p(runs, style=None, after=None, jc='both', keep_next=False):
    p = etree.Element(qn('w:p'))
    ppr = etree.SubElement(p, qn('w:pPr'))
    if style:
        s = etree.SubElement(ppr, qn('w:pStyle')); s.set(qn('w:val'), style)
    if keep_next:
        etree.SubElement(ppr, qn('w:keepNext'))
    if after is not None:
        sp = etree.SubElement(ppr, qn('w:spacing')); sp.set(qn('w:before'), '0'); sp.set(qn('w:after'), str(after))
    if jc and not style:
        j = etree.SubElement(ppr, qn('w:jc')); j.set(qn('w:val'), jc)
    for r in runs:
        p.append(r)
    return p

def rich(text, base_bold=False):
    """*italic* segments supported."""
    out = []
    parts = re.split(r'(\*[^*]+\*)', text)
    for part in parts:
        if not part: continue
        if part.startswith('*') and part.endswith('*') and len(part) > 2:
            out.append(mk_run(part[1:-1], italic=True, bold=base_bold))
        else:
            out.append(mk_run(part, bold=base_bold))
    return out

def try_block(n, q):
    return [mk_p([mk_run(f'Try it now {n}', bold=True, color=LABEL_COLOR)], keep_next=True, after=60),
            mk_p(rich(q), after=160)]

INTRO_EX = ('Each exercise is labeled ', 'Core', ' (the minimum before moving on), ', 'Extension',
            ' (deepens the idea) or ', 'Challenge', ' (stretches it). Solutions follow the exercises; each one also names the usual mistake.')
INTRO_SOL = 'Try each exercise on paper before you look. If you are stuck, re-read the section the exercise points to, try again, and only then read the solution below.'

def exercise_block(chap, exs, tries):
    out = []
    out.append(mk_p([mk_run('Exercises')], style='Heading2'))
    runs = []
    for i, s in enumerate(INTRO_EX):
        runs.append(mk_run(s, bold=(i % 2 == 1)))
    out.append(mk_p(runs, after=120))
    for i, (lvl, q, sol) in enumerate(exs, 1):
        out.append(mk_p([mk_run(f'{i}. ', bold=True), mk_run(f'{lvl}.', bold=True), mk_run(' ')] + rich(q), after=100))
    out.append(mk_p([mk_run('Solutions')], style='Heading2'))
    out.append(mk_p([mk_run(INTRO_SOL)], after=120))
    for i, (lvl, q, sol) in enumerate(exs, 1):
        out.append(mk_p([mk_run(f'{i}.', bold=True), mk_run(' ')] + rich(sol), after=100))
    if tries:
        out.append(mk_p([mk_run('Answers to Try it now')], style='Heading2'))
        for i, (anchor, q, a) in enumerate(tries, 1):
            out.append(mk_p([mk_run(f'{i}.', bold=True), mk_run(' ')] + rich(a), after=100))
    return out

def replace_in_p(p, old, new):
    ts = list(p.iter(qn('w:t')))
    full = ''.join(t.text or '' for t in ts)
    cnt = full.count(old)
    if cnt != 1:
        raise ValueError(f'count={cnt} for {old[:60]!r} in {full[:120]!r}')
    start = full.index(old); end = start + len(old)
    pos = 0; first = None
    for t in ts:
        txt = t.text or ''; a, b = pos, pos + len(txt); pos = b
        if b <= start or a >= end:
            continue
        s0 = max(start, a) - a; s1 = min(end, b) - a
        if first is None:
            t.text = txt[:s0] + new + txt[s1:]
            first = t
        else:
            t.text = txt[:s0] + txt[s1:]
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')


def mu_fix(body):
    """Restore Greek mu/nu that an earlier conversion turned into u/v in Chapter 22 and the back matter."""
    n = 0
    for r in list(body.iter(qn('w:r'))):
        ts = list(r.iter(qn('w:t')))
        if not ts: continue
        t = ''.join(x.text or '' for x in ts)
        rpr = r.find(qn('w:rPr'))
        va = rpr.find(qn('w:vertAlign')) if rpr is not None else None
        def clone(text, sup=None):
            nr = copy.deepcopy(r)
            for x in list(nr):
                if x.tag != qn('w:rPr'): nr.remove(x)
            npr = nr.find(qn('w:rPr'))
            if npr is not None:
                for v in npr.findall(qn('w:vertAlign')): npr.remove(v)
            if sup:
                if npr is None:
                    npr = etree.SubElement(nr, qn('w:rPr')); nr.insert(0, npr)
                v = etree.SubElement(npr, qn('w:vertAlign')); v.set(qn('w:val'), sup)
            tt = etree.SubElement(nr, qn('w:t')); tt.text = text
            tt.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
            return nr
        if va is not None and t in ('u', 'uv', 'uvF', 'uψ'):
            ts[0].text = {'u': 'μ', 'uv': 'μν', 'uvF': 'μν', 'uψ': 'μ'}[t]
            for x in ts[1:]: x.text = ''
            if t == 'uvF': r.addnext(clone('F'))
            if t == 'uψ': r.addnext(clone('ψ'))
            n += 1
        elif 'ᵘ' in t and va is None:
            a, b = t.split('ᵘ', 1)
            ts[0].text = a
            ts[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
            for x in ts[1:]: x.text = ''
            after = clone(b); r.addnext(after)
            r.addnext(clone('μ', 'superscript'))
            n += 1
    return n

def build(batches, out_path):
    d = docx.Document(SRC)
    body = d.element.body
    els = list(body.iterchildren())
    btc = None
    for i, e in enumerate(els):
        if e.tag == qn('w:p') and ptext(e).strip() == '↑ Back to Contents':
            btc = e; break
    log = []
    nT = nE = 0
    for bname in batches:
        m = importlib.import_module(bname)
        for (idx, old, new) in getattr(m, 'FIXES', []):
            if idx is None:
                hits = [e for e in els if e.tag == qn('w:p') and old in ptext(e)]
                if len(hits) != 1:
                    raise ValueError(f'auto-find {len(hits)} hits for {old[:60]!r}')
                replace_in_p(hits[0], old, new)
            else:
                replace_in_p(els[idx], old, new)
            log.append(f'fix {idx}')
        for (idx, newtext) in getattr(m, 'REWRITE', []):
            p = els[idx]
            ts = list(p.iter(qn('w:t')))
            ts[0].text = newtext
            ts[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
            for t in ts[1:]: t.text = ''
            log.append(f'rewrite {idx}')
        for idx in getattr(m, 'DELETE', []):
            els[idx].getparent().remove(els[idx]); log.append(f'del {idx}')
        for (idx, texts) in getattr(m, 'INSERT_AFTER', []):
            # new body paragraphs cloned from paragraph idx formatting
            ref = els[idx]
            for tx in reversed(texts):
                np_ = copy.deepcopy(ref)
                for r in list(np_):
                    if r.tag != qn('w:pPr'): np_.remove(r)
                for r in rich(tx): np_.append(r)
                ref.addnext(np_)
        for chap, spec in m.CHAPTERS.items():
            tries = spec.get('try', [])
            for n, (anchor, q, a) in enumerate(tries, 1):
                ref = els[anchor]
                for blk in reversed(try_block(n, q)):
                    ref.addnext(blk)
                nT += 1
            end_idx = spec['end']  # insert BEFORE this element
            blk = exercise_block(chap, spec['ex'], tries)
            if spec.get('add_btc'):
                blk.append(copy.deepcopy(btc))
            for b in blk:
                els[end_idx].addprevious(b)
            nE += len(spec['ex'])
    if any(getattr(importlib.import_module(b), 'MUFIX', False) for b in batches):
        log.append(f'mu_fix {mu_fix(body)}')
    d.save(out_path)
    return nT, nE, log

if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    batches = sys.argv[1].split(',')
    nT, nE, log = build(batches, sys.argv[2])
    print('try', nT, 'exercises', nE, 'edits', len(log))
