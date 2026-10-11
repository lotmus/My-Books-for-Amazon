import copy
from model16 import text, style
from engine import W
def settext(p, s):
    ts = list(p.iter(W('t'))); ts[0].text = s
    for t in ts[1:]: t.text = ''
def run(d, body, oldnew, PARTS, ROMAN):
    ps = [e for e in body.iterchildren() if e.tag == W('p')]
    c0 = next(i for i, p in enumerate(ps) if style(p) == 'Heading1' and text(p) == 'Contents')
    toc = []; i = c0 + 1
    while style(ps[i]) != 'Heading1':
        toc.append(ps[i]); i += 1
    settext(toc[0], 'An introduction, eleven parts and the back matter. Select a title to jump to it.')
    links = [p for p in toc if p.find(W('hyperlink')) is not None]
    A = lambda p: p.find(W('hyperlink')).get(W('anchor'))
    part_tpl = next(p for p in links if A(p).startswith('part_')); ch_tpl = next(p for p in links if A(p).startswith('ch_'))
    fm_tpl = next(p for p in links if A(p) == 'fm_preface')
    epi = next(p for p in links if A(p) == 'bm_epilogue')
    def entry(tpl, anchor, label):
        e = copy.deepcopy(tpl); e.find(W('hyperlink')).set(W('anchor'), anchor); settext(e, label); return e
    new = [entry(part_tpl, 'bm_intro', 'Introduction: Why Any of This Matters')]
    for p in [e for e in body.iterchildren() if e.tag == W('p')]:
        s = style(p)
        if s == 'Heading1':
            b = [x.get(W('name')) for x in p.iter(W('bookmarkStart'))]
            if b and b[0].startswith('part_'): new.append(entry(part_tpl, b[0], text(p)))
        elif s == 'Heading2':
            new.append(entry(ch_tpl, 'ch_%s' % text(p).split('.')[0], text(p)))
    drop = [p for p in links if A(p).startswith(('part_', 'ch_'))]
    for e in new: epi.addprevious(e)
    for e in drop: body.remove(e)
