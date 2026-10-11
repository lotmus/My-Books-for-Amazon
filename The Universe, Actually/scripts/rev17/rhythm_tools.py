"""Rhythm pass tooling.
 dump:   python rhythm_tools.py dump DOCX START COUNT   -> prints numbered sentences for flagged paragraphs (runs of 3+ sentences of <= 9 words are marked >>)
 apply:  python rhythm_tools.py apply DOCX             -> applies FIX lists from rhythm_fix_*.py (key, a, b, new) in place
A fix replaces sentences a..b (1-based, inclusive, numbering as printed by dump) of the paragraph whose text starts with key."""
import sys, os, re, io, glob, importlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rev16'))
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import docx
from docx.oxml.ns import qn
from engine import sub
W = lambda t: qn('w:' + t)
SHORT = 9
def style(p):
    s = p.find(W('pPr')); s = s.find(W('pStyle')) if s is not None else None
    return s.get(W('val')) if s is not None else ''
def text(p): return ''.join(t.text or '' for t in p.iter(W('t')))
def runinfo(p):
    out = []; pos = 0
    for r in p.iter(W('r')):
        if r.find(W('t')) is None: continue
        t = ''.join(x.text or '' for x in r.iter(W('t')))
        rp = r.find(W('rPr')); va = None; it = False
        if rp is not None:
            v = rp.find(W('vertAlign')); va = v.get(W('val')) if v is not None else None
            it = rp.find(W('i')) is not None
        link = r.getparent().tag == W('hyperlink')
        out.append((pos, pos + len(t), t, va, it, link)); pos += len(t)
    return out
def render(p, a, b):
    s = ''; link = False
    for (x, y, t, va, it, lk) in runinfo(p):
        if y <= a or x >= b: continue
        seg = t[max(a, x) - x:min(b, y) - x]
        if lk: link = True
        if va == 'superscript': seg = '^{' + seg + '}'
        elif va == 'subscript': seg = '_{' + seg + '}'
        elif it and seg.strip(): seg = '*' + seg + '*'
        s += seg
    return s, link
def sentences(t):
    return [(m.start(), m.end(), m.group(0)) for m in re.finditer(r'\S.*?(?:[.!?]+["”’)]*(?=\s|$)|$)', t, re.S)]
def skips():
    f = os.path.join(HERE, 'rhythm_skip.txt')
    return [l.rstrip() for l in open(f, encoding='utf-8') if l.strip()] if os.path.exists(f) else []
def flagged(doc):
    out = []; sk = skips()
    for p in doc.element.body.iter(W('p')):
        if style(p): continue
        t = text(p)
        if len(t.split()) < 25 or any(t.startswith(k) for k in sk): continue
        ss = sentences(t); runs = []; run = []
        for i, (a, b, x) in enumerate(ss, 1):
            if len(x.split()) <= SHORT: run.append(i)
            else:
                if len(run) >= 3: runs.append((run[0], run[-1]))
                run = []
        if len(run) >= 3: runs.append((run[0], run[-1]))
        if runs: out.append((p, t, ss, runs))
    return out
if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    cmd, path = sys.argv[1], sys.argv[2]
    d = docx.Document(path)
    if cmd == 'dump':
        start, cnt = int(sys.argv[3]), int(sys.argv[4])
        fl = flagged(d); print('total flagged', len(fl))
        for p, t, ss, runs in fl[start:start + cnt]:
            print('\n### KEY: ' + t[:40].replace('\n', ' ') + '   runs ' + str(runs))
            mark = set(i for a, b in runs for i in range(a, b + 1))
            for i, (a, b, x) in enumerate(ss, 1):
                m, lk = render(p, a, b)
                print((' >>' if i in mark else '   ') + '%d. %s' % (i, m) + ('   [HAS LINK - leave alone]' if lk else ''))
    elif cmd == 'apply':
        fixes = []
        files = [os.path.join(HERE, sys.argv[3])] if len(sys.argv) > 3 else sorted(glob.glob(os.path.join(HERE, 'rhythm_fix_*.py')))
        for f in files:
            fixes += importlib.import_module(os.path.basename(f)[:-3]).FIX
        paras = [p for p in d.element.body.iter(W('p')) if not style(p)]
        done = 0
        byp = {}
        for key, a, b, new in fixes:
            hit = [p for p in paras if text(p).startswith(key)]
            assert len(hit) == 1, ('key not unique or missing', key, len(hit))
            byp.setdefault(id(hit[0]), (hit[0], []))[1].append((a, b, new))
        for p, lst in byp.values():
            t = text(p); ss = sentences(t)
            for a, b, new in sorted(lst, reverse=True):
                old = t[ss[a - 1][0]:ss[b - 1][1]]
                # keep sup/sub formatting safe: skip spans that contain vertically aligned runs
                if sub(p, old, new): done += 1
                else: print('FAILED', old[:60])
        d.save(path); print('applied', done, 'of', len(fixes))
