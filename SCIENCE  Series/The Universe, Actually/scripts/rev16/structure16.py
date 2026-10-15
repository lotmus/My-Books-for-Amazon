import re, copy
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from model16 import text, style
from engine import newpara, sub, W
ROMAN = 'I II III IV V VI VII VIII IX X XI XII'.split()
PARTS = [
 ('The Rules of Motion and Energy', 'The everyday laws of motion, heat, waves and fields that every later part relies on', [18, 19, 20, 21]),
 ('The Quantum World', 'The rules of the very small, and what they let us build', [26, 27, 28, 29, 30]),
 ('Particles, Nuclei and Atoms', 'From quarks and the Standard Model up through nuclei and atoms to chemistry and materials', [31, 32, 33, 24, 25, 22, 23, 34]),
 ('Space, Time and Gravity', 'Relativity, gravitational waves and black holes', [8, 9, 10, 11, 12, 13, 14]),
 ('Planets, Stars and Galaxies', 'From our own Solar System out to other stars and the galaxies that hold them', [55, 56, 57, 6, 7, 5]),
 ('The Universe as a Whole', 'The expanding cosmos, its hot beginning, its dark contents, and the nature of time', [2, 3, 4, 17, 15, 16]),
 ('Life', 'From the first chemistry that copied itself to chemistry we can write, and to ourselves', [36, 37, 38, 39, 40, 41, 42, 43, 46, 47, 44]),
 ('The Human Body and Mind', 'How a body is run and defended, how a brain works, and what we do not yet know about experience', [48, 45, 52, 53, 51, 49, 50, 54]),
 ('Earth, the Living Planet', 'The ground, the air, the oceans, the web of life, and the energy that keeps a civilization running', [58, 59, 60, 61, 62, 63, 64]),
 ('Technology', 'Information, codes, machines that learn, living technology and spaceflight', [73, 69, 65, 66, 67, 68]),
 ('How We Know, and What Comes Next', 'How people came to know, count and doubt, and where that might lead', [70, 35, 71, 72, 74, 75, 76, 77]),
]
def P(body): return list(body.iterchildren())
def settext(p, s):
    ts = list(p.iter(W('t'))); ts[0].text = s
    for t in ts[1:]: t.text = ''
def bms(p): return list(p.iter(W('bookmarkStart')))
def run(d, body, out):
    els = P(body)
    i_part1 = next(i for i, e in enumerate(els) if e.tag == W('p') and style(e) == 'Heading1' and text(e).startswith('Part I:'))
    i_epi = next(i for i, e in enumerate(els) if e.tag == W('p') and style(e) == 'Heading1' and text(e).startswith('Epilogue'))
    mid = els[i_part1:i_epi]
    part_h_tpl = copy.deepcopy(mid[0]); part_line_tpl = copy.deepcopy(mid[1])
    chap = {}; cur = None
    for e in mid:
        if e.tag == W('p') and style(e) == 'Heading1': cur = None; continue
        if e.tag == W('p') and style(e) == 'Heading2': cur = int(text(e).split('.')[0]); chap[cur] = [e]; continue
        if cur is None: continue   # part intro lines
        chap[cur].append(e)
    used = sorted(sum([p[2] for p in PARTS], []) + [1]); assert used == list(range(1, 78)), used
    for e in mid: body.remove(e)
    anchor = els[i_epi]
    def put(e): anchor.addprevious(e)
    # Introduction from old chapter 1
    intro = chap[1]; h = copy.deepcopy(part_h_tpl)
    for b in bms(h): b.set(W('name'), 'bm_intro')
    settext(h, 'Introduction: Why Any of This Matters'); put(h)
    for e in intro[1:]: put(e)
    oldnew = {}; n = 0
    for pi, (title, line, chs) in enumerate(PARTS):
        h = copy.deepcopy(part_h_tpl)
        for b in bms(h): b.set(W('name'), 'part_%d' % (pi + 1)); b.set(W('id'), str(8000 + pi))
        for b in h.iter(W('bookmarkEnd')): b.set(W('id'), str(8000 + pi))
        settext(h, 'Part %s: %s' % (ROMAN[pi], title)); put(h)
        l = copy.deepcopy(part_line_tpl); settext(l, line); put(l)
        for c in chs:
            n += 1; oldnew[c] = n; hh = chap[c][0]
            settext(hh, re.sub(r'^\d+\.', '%d.' % n, text(hh)))
            b = bms(hh); assert len(b) == 1; b[0].set(W('name'), 'ch_%d' % n)
            for e in chap[c]: put(e)
    print('chapters', n)
    # fix bookmark ids of intro heading
    # cross references {chN}
    for hl in body.iter(W('hyperlink')):
        a = hl.get(W('anchor')) or ''
        if a.startswith('oldch_'):
            o = int(a[6:]); nn = oldnew[o]; hl.set(W('anchor'), 'ch_%d' % nn)
            for t in hl.iter(W('t')):
                if t.text and '@@CH' in t.text: t.text = 'Chapter %d' % nn
    for p in body.iter(W('p')):
        ts = list(p.iter(W('t')))
        if ts and ts[0].text and ts[0].text.startswith('Chapter ') and p.find(W('hyperlink')) is not None:
            pass
    # sentence-initial capitalization handled in markup; lowercase 'chapter' not used
    import contents16; contents16.run(d, body, oldnew, PARTS, ROMAN)
    import post16; post16.run(d, body)
    names = {b.get(W('name')) for b in body.iter(W('bookmarkStart'))}
    dead = [h.get(W('anchor')) for h in body.iter(W('hyperlink')) if h.get(W('anchor')) and h.get(W('anchor')) not in names]
    assert not dead, dead
    ids = [b.get(W('id')) for b in body.iter(W('bookmarkStart'))]
    dup = {i for i in ids if ids.count(i) > 1}
    assert not dup, dup
    d.core_properties.title = 'The Universe, Actually'; d.core_properties.author = 'Lothar J. Musiol'
    d.save(out); print('saved', out)
