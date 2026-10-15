# -*- coding: utf-8 -*-
"""Physics, Actually Vol 1: 11 Oct 2026 improve pass (restructure, merge, exercises, sources, credits, TOC).
Usage: python improve_v1.py <in.docx> <out.docx> <omega_out.docx>"""
import sys, copy, re, io
sys.path.insert(0, __file__.rsplit('/',1)[0] if '/' in __file__ else '.')
import docx
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from lxml import etree
from PIL import Image
import v1_content as C

src, out, omega_out = sys.argv[1:4]
PRINT = '--print' in sys.argv  # paperback master: keep full-resolution pictures
D = docx.Document(src)
body = D.element.body
els = list(body.iterchildren())
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
XS = '{http://www.w3.org/XML/1998/namespace}space'

def text(el): return ''.join(t.text or '' for t in el.iter(qn('w:t')))
def style(el):
    pp = el.find(qn('w:pPr'))
    if pp is None: return ''
    ps = pp.find(qn('w:pStyle'))
    return ps.get(qn('w:val')) if ps is not None else ''
def bms(el): return [b.get(qn('w:name')) for b in el.iter(qn('w:bookmarkStart'))]
def is_pb(el): return el.tag == qn('w:p') and not text(el).strip() and any(b.get(qn('w:type')) == 'page' for b in el.iter(qn('w:br')))

# ---- id counters ----
_bmid = [max([int(b.get(qn('w:id'))) for b in body.iter(qn('w:bookmarkStart'))] + [0]) + 1000]
def bookmark(p, name):
    i = str(_bmid[0]); _bmid[0] += 1
    s = etree.Element(qn('w:bookmarkStart')); s.set(qn('w:id'), i); s.set(qn('w:name'), name)
    e = etree.Element(qn('w:bookmarkEnd')); e.set(qn('w:id'), i)
    pp = p.find(qn('w:pPr')); pos = 1 if pp is not None else 0
    p.insert(pos, s); p.insert(pos + 1, e)

def run(t, b=False, i=False, link=False, sz=None):
    r = etree.Element(qn('w:r')); rp = etree.SubElement(r, qn('w:rPr'))
    if b: etree.SubElement(rp, qn('w:b'))
    if i: etree.SubElement(rp, qn('w:i'))
    if link:
        c = etree.SubElement(rp, qn('w:color')); c.set(qn('w:val'), '0563C1')
        u = etree.SubElement(rp, qn('w:u')); u.set(qn('w:val'), 'single')
    if sz: s = etree.SubElement(rp, qn('w:sz')); s.set(qn('w:val'), str(sz))
    if len(rp) == 0: r.remove(rp)
    tt = etree.SubElement(r, qn('w:t')); tt.text = t; tt.set(XS, 'preserve')
    return r

def hyper(target, runs):
    h = etree.Element(qn('w:hyperlink'))
    if target.startswith('#'): h.set(qn('w:anchor'), target[1:])
    else: h.set(qn('r:id'), D.part.relate_to(target, RT.HYPERLINK, is_external=True))
    h.set(qn('w:history'), '1')
    for r in runs: h.append(r)
    return h

def para(parts, st=None, jc='both', keep=False, ind=None, before=None, after=None):
    """parts: list of str or (str, dict(b,i,link))"""
    p = etree.Element(qn('w:p')); pp = etree.SubElement(p, qn('w:pPr'))
    if st: e = etree.SubElement(pp, qn('w:pStyle')); e.set(qn('w:val'), st)
    if keep: etree.SubElement(pp, qn('w:keepNext'))
    if before is not None or after is not None:
        sp = etree.SubElement(pp, qn('w:spacing'))
        if before is not None: sp.set(qn('w:before'), str(before))
        if after is not None: sp.set(qn('w:after'), str(after))
    if ind is not None: e = etree.SubElement(pp, qn('w:ind')); e.set(qn('w:left'), str(ind))
    if jc: e = etree.SubElement(pp, qn('w:jc')); e.set(qn('w:val'), jc)
    if isinstance(parts, str): parts = [parts]
    for x in parts:
        if isinstance(x, str): p.append(run(x)); continue
        t, o = x
        if o.get('link'): p.append(hyper(o['link'], [run(t, o.get('b'), o.get('i'), True)]))
        else: p.append(run(t, o.get('b'), o.get('i')))
    return p
def H1(t, bm=None):
    p = para(t, 'Heading1', jc=None)
    if bm: bookmark(p, bm)
    return p
def H2(t, bm=None):
    p = para(t, 'Heading2', jc=None)
    if bm: bookmark(p, bm)
    return p
def PB():
    p = etree.Element(qn('w:p')); r = etree.SubElement(p, qn('w:r')); b = etree.SubElement(r, qn('w:br')); b.set(qn('w:type'), 'page'); return p
def set_text(p, new):
    rs = [r for r in p.findall(qn('w:r')) if r.find(qn('w:t')) is not None]
    rp = rs[0].find(qn('w:rPr')) if rs else None
    for r in list(p):
        if r.tag in (qn('w:r'), qn('w:hyperlink')): p.remove(r)
    r = etree.SubElement(p, qn('w:r'))
    if rp is not None: r.append(copy.deepcopy(rp))
    t = etree.SubElement(r, qn('w:t')); t.text = new; t.set(XS, 'preserve')
def replace_in(p, old, new):
    for t in p.iter(qn('w:t')):
        if t.text and old in t.text: t.text = t.text.replace(old, new); return True
    full = text(p)
    if old in full:  # spans runs: collapse to one run
        set_text(p, full.replace(old, new)); return True
    return False

def drop_unused_images(doc):
    used = {b.get(qn('r:embed')) for b in doc.element.body.iter(qn('a:blip'))}
    for rid, rel in list(doc.part.rels.items()):
        if 'image' in rel.reltype and rid not in used: doc.part.drop_rel(rid) if hasattr(doc.part, 'drop_rel') else doc.part.rels.pop(rid)
LOG = []
def must(cond, msg):
    if not cond: raise SystemExit('FAILED: ' + msg)
    LOG.append('ok: ' + msg)

# ---- locate blocks by bookmark ----
def idx_bm(name):
    for i, e in enumerate(els):
        if name in bms(e): return i
    raise SystemExit('no bookmark ' + name)
order_bm = ['chPROLOGUE','ch00','ch01','ch02','ch03','ch04','ch04a','ch04b','ch04c','ch04d','ch33','ch34','ch39','ch05','ch06','ch06a','ch06b','ch06c','ch06d','ch07','ch35']
starts = [idx_bm(b) - (1 if style(els[idx_bm(b) - 1]) == 'Title' else 0) for b in order_bm]
appx = idx_bm('_TocAll0002')
must(starts == sorted(starts), 'chapter bookmarks in expected order')
blocks = {}
for k, b in enumerate(order_bm):
    end = starts[k + 1] if k + 1 < len(starts) else appx
    blocks[b] = els[starts[k]:end]
front = els[:starts[0]]
back = els[appx:]
sect = back[-1]; must(sect.tag == qn('w:sectPr'), 'sectPr last'); back = back[:-1]

def find(block, pred, what):
    for i, e in enumerate(block):
        if pred(e): return i
    raise SystemExit('not found: ' + what)
def h2i(block, t): return find(block, lambda e: style(e) == 'Heading2' and text(e).strip() == t, 'H2 ' + t)
def section(block, t):
    """return (start,end) indices of an H2 section incl. heading"""
    a = h2i(block, t); b = a + 1
    while b < len(block) and style(block[b]) not in ('Heading1', 'Heading2') and not is_pb(block[b]): b += 1
    return a, b

# ---- 1. Omega Point chapter to bak ----
omega = blocks.pop('ch06c')

# ---- 2. Merge Reichenbach (ch06b) into the arrow chapter (ch05) ----
A = blocks['ch05']; R = blocks['ch06b']
r_open_a, r_open_b = section(R, 'Same Puzzle, a Sharper Question')
intro = R[r_open_a + 2]  # 'Hans Reichenbach, in his book ...'
must('Reichenbach' in text(intro), 'Reichenbach intro paragraph found')
set_text(intro, 'The philosopher of science Hans Reichenbach, in his book The Direction of Time, published in 1956, wanted more than the entropy story told so far. He was not satisfied with “entropy increases.” He wanted to know why an enormous variety of separate things — a cooling cup, a photograph, a memory, a footprint in sand — all point the same way, as though they had agreed on it in advance. His answer starts with an idea he called the branch system.')
rs_a, _ = section(R, 'Branch systems')
bt_a, bt_b = section(R, 'Barbour and Reichenbach together')
eg_a, eg_b = section(R, 'One last broken egg')
reich_core = R[rs_a:bt_a]  # Branch systems ... What Reichenbach did not prove
barbour_reich = R[bt_a:bt_b]
egg = R[eg_a:eg_b]
for e in reich_core:
    if style(e) == 'Heading2' and text(e).strip() == 'Why do we remember the past?':
        set_text(e, 'Records: photographs, fossils, footprints')
tf_a, tf_b = section(A, 'Time, finally')
set_text(A[tf_a], 'Time’s arrow, in summary')
keep_egg = [e for e in egg[1:] if text(e).startswith(('Yet the egg stays broken', 'We call that direction the future'))]
must(len(keep_egg) == 2, 'two closing egg paragraphs kept')
A[tf_b:tf_b] = keep_egg
A[tf_a:tf_a] = [H2('Reichenbach’s sharper question'), intro] + reich_core
blocks['ch05'] = A
blocks.pop('ch06b')

# ---- 3. Barbour chapter (ch06a): condense arrow repeats, add the Reichenbach link ----
B = blocks['ch06a']
a1, _ = section(B, 'The arrow of time'); _, a2 = section(B, 'A broken egg knows something your equations don’t')
new_arrow = [H2('Where the arrow fits'),
 para('Even if the fundamental laws contain no flowing time, our world has an unmistakable direction, and Chapter 13 traced it to entropy and to the universe’s special low-entropy start. Barbour’s approach encourages us to separate two questions that usually get mixed up: why does time seem to flow, and why does the universe contain such a strong distinction between remembered past and unknown future?'),
 para('Maybe the fundamental world is timeless, while the arrow emerges from the special structure of the configurations we inhabit. The fundamental laws need not say, “Time flows from yesterday toward tomorrow.” A special class of configurations can contain records and correlations that make one direction stand out: entropy increases in that direction, memory and biology work in that direction, and we call it the past-to-future direction. The arrow would then be a property of the universe’s state, not a fundamental ingredient of its laws.')]
B[a1:a2] = new_arrow
e1, e2 = section(B, 'The arrow may be an emergent phenomenon'); del B[e1:e2]
sr = h2i(B, 'Why do we remember the past?'); set_text(B[sr], 'Records without a flowing past')
f1 = h2i(B, 'One final second')
B[f1:f1] = [H2('Barbour and Reichenbach together'),
 para('Barbour’s question and Reichenbach’s now fit together. Barbour asks: does time itself really exist as a flowing thing? Reichenbach, in Chapter 13, asked: if time has no intrinsic direction, why does the physical world have such a powerful arrow? Those are different questions. We might eventually discover that time is emergent and that its direction is emergent too. Or we might discover that one of these ideas is wrong.'),
 para('The important thing is that we have separated the problems. The existence of time and the direction of time are not the same mystery.')]
blocks['ch06a'] = B

# ---- 4. Electromagnetism chapter (ch00): fold the two ether sections into one; retitle 'comes first' ----
E = blocks['ch00']
m1, _ = section(E, 'The mysterious ether'); _, m2 = section(E, 'Einstein removes the ether')
E[m1:m2] = [H2('The ether, and why it went away'),
 para('For a long time, physicists assumed that light, like sound, needed a medium, an invisible substance called the ether. It was a reasonable idea. Experiments designed to detect Earth’s motion through it found nothing; the next chapter tells the story of the most famous one, by Albert Michelson and Edward Morley.'),
 para('Einstein’s special theory of relativity then changed the question. The speed of light in vacuum is the same for all inertial observers, so there is no need for a preferred invisible medium; instead, space and time themselves adjust. This is where our electromagnetic story joins relativity. Maxwell’s equations were already hinting that c was special. Einstein showed that taking that fact seriously changes our understanding of space and time.')]
w = h2i(E, 'Why this chapter comes first'); set_text(E[w], 'Why electromagnetism leads to relativity')
bq, _ = section(E, 'The bridge to quantum physics')
must(replace_in(E[bq + 1], 'depends on discrete amounts of energy.', 'depends on discrete amounts of energy; the next chapter tells that story.'), 'EM bridge forward reference')
blocks['ch00'] = E

# ---- 5. What Is Time (ch06): its closing bridge to Barbour moves to the end of special relativity (ch07) ----
T = blocks['ch06']; S = blocks['ch07']
bi = find(T, lambda e: text(e).startswith('But spacetime raises a question even stranger'), 'ch14 bridge')
bridge = T.pop(bi)
spb = len(S) - 1; must(is_pb(S[spb]), 'SR chapter ends with page break')
set_text(bridge, 'Spacetime raises a question even stranger than the ones this chapter answered. If every observer’s “now” is different, and there is no universal present moment shared by everyone, then in what sense does time actually flow at all? Some physicists have followed that question all the way to its most radical possible conclusion: that time, as something that passes, might not exist the way we think it does.')
S.insert(spb, bridge)

# ---- 6. Limits chapter: give it a closing page break ----
L = blocks['ch35']
if not is_pb(L[-1]): L.append(PB())

# ---- 7. New order and numbering ----
NEW = [('chPROLOGUE', None), ('ch01', 1), ('ch02', 2), ('ch03', 3), ('ch04', 4), ('ch04a', 5), ('ch04b', 6), ('ch04c', 7), ('ch04d', 8), ('ch33', 9),
       ('ch00', 10), ('ch34', 11), ('ch39', 12), ('ch05', 13), ('ch06', 14), ('ch06d', 15), ('ch07', 16), ('ch06a', 17), ('ch35', 18)]
PARTS = {1: ('Part One', 'How Physics Thinks', 'What physics is for, and why it so often surprises us.'),
         2: ('Part Two', 'Motion, Forces, and Energy', 'Newton’s world, its bookkeeping rules, and the rhythms and waves that follow from them.'),
         10: ('Part Three', 'Fields and Light', 'Electricity, magnetism, and the wave that turned out to be light.'),
         13: ('Part Four', 'Time, Relativity, and the Limits of Nature', 'Why time has a direction, how clocks are built, what Einstein did to time, and the limits nature seems to impose.')}
OLD2NEW = {1: 10, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 11, 12: 12, 13: 13, 14: 14, 15: 17, 16: 13, 18: 15, 19: 16, 20: 18}
titles = {}

def renumber(el):
    for t in el.iter(qn('w:t')):
        if t.text and re.search(r'Chapter \d+', t.text):
            t.text = re.sub(r'Chapter (\d+)', lambda m: 'Chapter %d' % OLD2NEW.get(int(m.group(1)), int(m.group(1))), t.text)
for b, n in NEW:
    for e in blocks[b][3:]: renumber(e)
for e in back: renumber(e)

SUB_H1 = {'Springs, Pendulums, and their Rhythm': 'Springs, Pendulums, and Their Rhythm'}
def chapter_head(block, n, bm):
    # block[0] Title 'Physics, Actually' (bookmark), block[1] H1 'Chapter N'/'PROLOGUE', block[2] H1 title
    must(style(block[0]) == 'Title' and style(block[1]) == 'Heading1' and style(block[2]) == 'Heading1', 'head shape ' + bm)
    title = text(block[2]).strip(); title = SUB_H1.get(title, title)
    label = para([('Prologue' if n is None else 'Chapter %d' % n, {'b': True})], jc='center', keep=True, after=60)
    h = H1(title, bm)
    titles[bm] = title
    return [label, h] + block[3:]

body_new = []
for b, n in NEW:
    if n in PARTS:
        pn, pt, pd = PARTS[n]
        body_new += [para([(pn, {'b': True})], jc='center', keep=True, after=60), H1(pt, 'part%d' % n), para([(pd, {'i': True})], jc='center'), PB()]
    body_new += chapter_head(blocks[b], n, b)

# ---- 8. Heading clean-up: fragment subheads to plain words ----
SUB = {'The Punchline': 'Summing Up', 'Keep This Picture': 'Summing Up', 'Now Notice What Happened': 'Summing Up',
       'The Deeper Idea': 'Summing Up', 'So What Have We Learned?': 'Summing Up', 'The Surprising Part': 'Summing Up',
       'Why any of this matters for the rest of the book': 'Why this matters for relativity',
       'Why this matters beyond the physics classroom': 'Why this matters beyond the classroom'}
for e in body_new:
    if style(e) == 'Heading2' and text(e).strip() in SUB: set_text(e, SUB[text(e).strip()])

# ---- 9. Fact fixes ----
FIX = [
 ('By the eighteenth century, Lagrange and later William Rowan Hamilton had turned', 'In the late eighteenth century Joseph-Louis Lagrange, and in the 1830s William Rowan Hamilton, turned'),
 ('Two centuries after Newton described forces acting instant by instant, physics discovered', 'Within about a century of Newton’s forces acting instant by instant, physics had found'),
 ('The nearest star system to our own, Alpha Centauri, is about 4.2 light-years away.', 'The nearest star to the Sun, Proxima Centauri, is about 4.2 light-years away.'),
]
for old, new in FIX:
    hit = [e for e in body_new if old in text(e)]
    must(len(hit) == 1, 'fact fix: ' + old[:40])
    replace_in(hit[0], old, new)

# ---- 10. Join paragraphs split mid-sentence (ending with ':' and continuing in lower case) ----
joined = 0
i = 0
while i < len(body_new) - 1:
    a, b = body_new[i], body_new[i + 1]
    if a.tag == qn('w:p') and b.tag == qn('w:p') and not style(a) and not style(b) and not list(a.iter(qn('w:drawing'))) and not list(b.iter(qn('w:drawing'))):
        ta, tb = text(a).rstrip(), text(b).lstrip()
        if ta.endswith(':') and len(ta) > 40 and '=' not in tb and re.match(r'[a-z]+[ .,]', tb) and len(tb) > 30:
            for r in list(b):
                if r.tag in (qn('w:r'), qn('w:hyperlink')): a.append(r)
            ts = [t for t in a.iter(qn('w:t'))]
            # add a space at the seam
            for t in ts:
                if t.text and t.text.endswith(':') or (t.text and t.text.rstrip() == t.text and t is ts[-1]): pass
            seam = None
            LOG.append('  join: ...%s || %s...' % (ta[-50:], tb[:50])); body_new.pop(i + 1); joined += 1
            continue
    i += 1
# put a single space at each seam created above (the joined run starts without one)
for e in body_new:
    if e.tag != qn('w:p'): continue
    ts = [t for t in e.iter(qn('w:t')) if t.text]
    for x, y in zip(ts, ts[1:]):
        if x.text.endswith(':') and y.text[:1].isalpha() and y.text[:1].islower(): y.text = ' ' + y.text
LOG.append('joined split paragraphs: %d' % joined)

# ---- 11. Exercises at the end of each chapter ----
def ex_block(n):
    out = [H2('Try It Yourself', 'ex_ch%d' % n),
           para(['Worked solutions, each with the usual mistake, are in ', ('Solutions to the Exercises', {'link': '#sol_ch%d' % n}), '.'])]
    for k, (q, s, m) in enumerate(C.EX[n], 1):
        out.append(para([('%d.%d  ' % (n, k), {'b': True}), q]))
    return out
res = []; cur = None
for e in body_new:
    res.append(e)
# insert before the closing page break of each chapter
final = []
chap_of = None
for j, e in enumerate(body_new):
    if e.tag == qn('w:p') and style(e) == 'Heading1':
        nm = [x for x in bms(e) if x.startswith('ch')]
        chap_of = dict(NEW).get(nm[0]) if nm else None
    if is_pb(e) and chap_of:
        final += ex_block(chap_of); chap_of = None
    final.append(e)
must(sum(1 for e in final if style(e) == 'Heading2' and text(e) == 'Try It Yourself') == 18, '18 exercise sets')
body_new = final

# ---- 12. In-text citations -> source entries ----
def link_phrase(p, phrase, anchor):
    for r in p.iter(qn('w:r')):
        t = r.find(qn('w:t'))
        if t is None or not t.text or phrase not in t.text: continue
        if r.getparent().tag == qn('w:hyperlink'): return False
        pre, post = t.text.split(phrase, 1)
        par = r.getparent(); pos = par.index(r)
        rp = r.find(qn('w:rPr'))
        def mk(tx, lk=False):
            nr = etree.Element(qn('w:r'))
            nrp = copy.deepcopy(rp) if rp is not None else etree.Element(qn('w:rPr'))
            if lk:
                for tag in ('w:color', 'w:u'):
                    for x in nrp.findall(qn(tag)): nrp.remove(x)
                c = etree.SubElement(nrp, qn('w:color')); c.set(qn('w:val'), '0563C1')
                u = etree.SubElement(nrp, qn('w:u')); u.set(qn('w:val'), 'single')
            if len(nrp): nr.append(nrp)
            tt = etree.SubElement(nr, qn('w:t')); tt.text = tx; tt.set(XS, 'preserve'); return nr
        new = []
        if pre: new.append(mk(pre))
        h = etree.Element(qn('w:hyperlink')); h.set(qn('w:anchor'), anchor); h.set(qn('w:history'), '1'); h.append(mk(phrase, True)); new.append(h)
        if post: new.append(mk(post))
        par.remove(r)
        for k, x in enumerate(new): par.insert(pos + k, x)
        return True
    return False
CITES = [('objects fall with the same gravitational acceleration', 'apollo15'), ('the mathematician Emmy Noether', 'noether'),
 ('Emmy Noether showed', 'noether'), ('Richard Feynman pushed the idea', 'feynmanrmp'), ('Michael Faraday discovered', 'faraday'),
 ('James Clerk Maxwell took the experimental laws', 'maxwell'), ('Albert Michelson and Edward Morley built', 'michelson'),
 ('Thomas Young’s famous double-slit experiment', 'young'), ('Einstein explained this in 1905', 'einstein_photo'),
 ('earned Einstein the Nobel Prize', 'nobel1921'), ('Ibn Sahl', 'rashed'), ('Rayleigh scattering', 'rayleigh'), ('Charles Kao', 'kao'),
 ('Event Horizon Telescope', 'eht'), ('Theodore Maiman', 'maiman'), ('The Direction of Time, published in 1956', 'reichenbach'),
 ('principle of the common cause', 'sep_rpcc'), ('Julian Barbour has pushed this idea', 'barbour'), ('9,192,631,770 oscillations', 'bipm'),
 ('John Harrison', 'rmg'), ('Your GPS receiver would become wrong', 'ashby'), ('GPS satellites, which move faster than you', 'ashby'),
 ('Black-hole thermodynamics tells us', 'bekenstein'), ('Erasing information has thermodynamic consequences', 'landauer'),
 ('AdS/CFT correspondence', 'maldacena'), ('This inspired the holographic principle', 'susskind'), ('“maximum force”', 'gibbons'),
 ('the Planck length, approximately', 'codata'), ('In 1905, Einstein took the next step', 'einstein_sr')]
cited = set()
for phrase, key in CITES:
    done = False
    for e in body_new + back:
        if e.tag == qn('w:p') and phrase in text(e) and link_phrase(e, phrase, 'src_' + key): done = True; break
    if done: cited.add(key)
    else: LOG.append('citation not placed: ' + phrase)

# ---- 13. Pictures: alt text, 440 px photos ----
alt_by_bm = {}
cur = None
for e in body_new:
    if style(e) == 'Heading1':
        nm = [x for x in bms(e) if x.startswith('ch')]
        if nm: cur = (dict(NEW)[nm[0]], text(e).strip())
    for dr in e.iter(qn('w:drawing')):
        dp = dr.find('.//' + qn('wp:docPr'))
        if dp is not None and not dp.get('descr'):
            nm = dp.get('name') or ''
            blip = dr.find('.//' + qn('a:blip')); tgt = D.part.rels[blip.get(qn('r:embed'))].target_ref
            DIAG = {'media/image14.png': 'Diagram: a light clock at rest ticks straight up and down; seen moving, its light follows a longer diagonal path, so the moving clock ticks slower.',
                    'media/image15.png': 'Diagram: the light cone of an event, the future events it can influence and the past events that can influence it.',
                    'media/image21.png': 'Spacetime diagram, time up and space across: a worldline always stays inside the light lines; steeper means slower through space and faster through time.'}
            if tgt in DIAG: dp.set('descr', DIAG[tgt])
            elif nm.startswith('ChapterImage') or tgt.endswith(('.jpg', '.jpeg')):
                dp.set('descr', 'Chapter %d opening illustration for “%s”, with the chapter’s key idea and what it will explore.' % cur)
            else:
                dp.set('descr', 'Diagram for Chapter %d, “%s”.' % cur)
# shrink an oversized chapter opener (image1, 1008 px) to 440 px wide
for rel in ([] if PRINT else D.part.rels.values()):
    if 'image' in rel.reltype:
        part = rel.target_part
        im = Image.open(io.BytesIO(part.blob))
        if im.format == 'PNG' and im.width > 800:
            im2 = im.convert('RGBA') if im.mode in ('P', 'LA') else im
            im2 = im2.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS)
            bio = io.BytesIO(); im2.save(bio, 'PNG', optimize=True); part._blob = bio.getvalue()
            LOG.append('diagram %s to 800 px' % rel.target_ref); continue
        if im.format == 'JPEG' and im.width > 440:
            im = im.convert('RGB').resize((440, round(im.height * 440 / im.width)), Image.LANCZOS)
            bio = io.BytesIO(); im.save(bio, 'JPEG', quality=80, optimize=True); part._blob = bio.getvalue()
            LOG.append('resized %s to 440 px' % rel.target_ref)

# ---- 14. Back matter ----
bk = {}
for e in back:
    for nm in bms(e): bk[nm] = e
def back_section(start_bm, stop_pred):
    i = back.index(bk[start_bm]); j = i + 1
    while j < len(back) and not stop_pred(back[j]): j += 1
    return back[i:j]
recap = back_section('_TocAll0002', lambda e: style(e) == 'Heading1')
gloss = back_section('_TocAll0003', lambda e: is_pb(e) or style(e) == 'Heading1')
about = back_section('_TocAll0004', lambda e: style(e) == 'Heading1')
alsob = back_section('_TocAll0005', lambda e: is_pb(e) or style(e) == 'Heading1')
note = back_section('_TocAll0006', lambda e: False)
review_lines = [e for e in back if text(e).startswith('If this book gave you something')]
must(len(review_lines) == 1, 'duplicate standalone review line found (kept the one in A Note Before You Go)')
for h in recap:
    if style(h) == 'Heading2':
        t = text(h).strip()
        if t == 'The Final Punchline': set_text(h, 'The Whole Volume in One Paragraph')
        if t == 'The Final Feynman-ish Rule': set_text(h, 'A Rule Worth Keeping')

# Also by: link each title to its Amazon search page (no product pages yet), keep groups unlinked
def amazon(q): 
    from urllib.parse import quote_plus
    return 'https://www.amazon.com/s?k=' + quote_plus(q)
for e in alsob[1:]:
    t = text(e).strip()
    if not t or e.find('.//' + qn('w:b')) is not None: continue
    if e.find('.//' + qn('w:hyperlink')) is not None: continue
    m = re.match(r'(.+?)(, Lothar J\. Musiol writing as .+)?$', t)
    title, pen = m.group(1), m.group(2) or ''
    q = re.sub(r'\s*\(.*?\)\s*', ' ', title).strip()
    q = re.split(r':', q)[0].strip()
    q = q + ('' if pen else ' Lothar J. Musiol')
    rp = e.find('.//' + qn('w:rPr'))
    for r in list(e):
        if r.tag == qn('w:r'): e.remove(r)
    e.append(hyper(amazon(q), [run(title, link=True)]))
    if pen: e.append(run(pen))

# Solutions
sol = [H1('Solutions to the Exercises', 'sol_all'), para('Each solution ends with the mistake people most often make on that question, because seeing the trap is half of understanding the physics.')]
for b, n in NEW:
    if n is None: continue
    sol.append(H2('Chapter %d: %s' % (n, titles[b]), 'sol_ch%d' % n))
    for k, (q, s, m) in enumerate(C.EX[n], 1):
        sol.append(para([('%d.%d  ' % (n, k), {'b': True}), s]))
        sol.append(para([('Usual mistake: ', {'b': True}), m], ind=360))
    sol.append(para([('Back to the exercises for Chapter %d' % n, {'link': '#ex_ch%d' % n})], jc='left'))
sol.append(PB())

# Sources
srcs = [H1('Sources and Further Reading', 'src_all'),
        para('Works the text relies on, grouped by chapter, with free or official versions linked where they exist. Links in the chapters lead to the entries here.')]
for g, keys in C.SRC_GROUPS:
    srcs.append(H2(g))
    for k in keys:
        v = C.SRC[k]
        parts = [v[0], (v[1], {'link': v[2]})] + ([v[3]] if len(v) > 3 else [])
        p = para(parts, jc='left', after=80); bookmark(p, 'src_' + k); srcs.append(p)
        if k == 'kao':
            p.append(hyper('#src_nobel2009', [run('the 2009 Nobel Prize entry', link=True)])); p.append(run('.'))
srcs.append(PB())

credits = [H1('Picture Credits', 'credits'),
 para('All pictures in this book were created for it; none is reproduced from another source.'),
 para([('Chapter-opening illustrations, Chapters 1–18: ', {'b': True}), 'one per chapter except Chapter 12, each with the chapter’s key idea and what it will explore.']),
 para([('Diagrams, Chapter 14: ', {'b': True}), 'the light clock seen at rest and in motion; the light cone, what an event can influence and be influenced by.']),
 para([('Diagram, Chapter 16: ', {'b': True}), 'a spacetime diagram showing that every path (worldline) stays inside the light lines.']),
 PB()]

# Remove the standalone review line (and its page break); it stays in A Note Before You Go
rv = review_lines[0]

new_back = recap + [PB()] + sol + gloss + [PB()] + srcs + credits + about + alsob + [PB()] + note
# ---- 15. Contents ----
toc_i = find(front, lambda e: text(e).strip().endswith('Table of Contents') or text(e).strip() == 'Contents', 'TOC heading')
toc_end = toc_i + 1
while toc_end < len(front) and (front[toc_end].find('.//' + qn('w:hyperlink')) is not None or not text(front[toc_end]).strip()): toc_end += 1
def tl(label, anchor, ind=0, b=False): return para([(label, {'link': '#' + anchor, 'b': b})], jc='left', ind=ind if ind else None, after=40)
toc = [para(''), tl('Also in This Series', '_TocAll0001')]
for b, n in NEW:
    if n in PARTS: toc.append(tl('%s: %s' % (PARTS[n][0], PARTS[n][1]), 'part%d' % n, b=True))
    toc.append(tl(('Prologue: ' if n is None else 'Chapter %d: ' % n) + titles[b], b, ind=0 if n is None else 360))
for lbl, a in [('Appendix: The Universe, Explained Badly Enough to Be Memorable', '_TocAll0002'), ('Solutions to the Exercises', 'sol_all'),
               ('Glossary', '_TocAll0003'), ('Sources and Further Reading', 'src_all'), ('Picture Credits', 'credits'),
               ('About the Author', '_TocAll0004'), ('Also by Lothar J. Musiol', '_TocAll0005'), ('A Note Before You Go', '_TocAll0006')]:
    toc.append(tl(lbl, a))
front[toc_i + 1:toc_end] = toc
# title page subtitle is not a chapter: Subtitle style instead of Heading 1
for e in front[:6]:
    if style(e) == 'Heading1' and text(e).startswith('Volume 1'):
        e.find(qn('w:pPr')).find(qn('w:pStyle')).set(qn('w:val'), 'Subtitle')

# ---- 16. Write body ----
for e in list(body): body.remove(e)
for e in front + body_new + new_back: body.append(e)
body.append(sect)
# all internal anchors must resolve
names = {b.get(qn('w:name')) for b in body.iter(qn('w:bookmarkStart'))}
bad = sorted({h.get(qn('w:anchor')) for h in body.iter(qn('w:hyperlink')) if h.get(qn('w:anchor')) and h.get(qn('w:anchor')) not in names})
must(not bad, 'all internal links resolve %s' % bad)
must('Omega' not in ''.join(text(e) for e in body_new), 'no Omega Point text left in the chapters')
D.core_properties.author = 'Lothar J. Musiol'
drop_unused_images(D); D.save(out)

# ---- Omega Point chapter as its own docx in bak ----
O = docx.Document(src); ob = O.element.body
oe = list(ob.iterchildren()); osect = oe[-1]
for e in oe: ob.remove(e)
on = starts[order_bm.index('ch06c')]; oend = starts[order_bm.index('ch06d')]
ob.append(para([('Moved out of Physics, Actually, Volume 1 on 11 Oct 2026 (PT).', {'b': True})], jc='left'))
ob.append(para('This was Chapter 17, “The Omega Point: Outside Space and Time” (Teilhard de Chardin and Frank Tipler). The 11 Oct 2026 strict review called it off-topic for a volume on motion, forces, time and relativity: it is theology and speculative cosmology rather than physics the book teaches. It is kept here unchanged so nothing is lost; it could return in Volume 2 (cosmology) or a future essay collection. The chapter text follows exactly as it stood in the master.', jc='left'))
ob.append(PB())
for e in list(O.element.body.iterchildren()): pass
src_els = list(docx.Document(src).element.body.iterchildren())
# reuse the original doc to keep its images: copy the omega elements from this document's own tree instead
for e in [list(O.element.body.iterchildren())]: pass
O2 = docx.Document(src); b2 = O2.element.body; all2 = list(b2.iterchildren())
keep = all2[on:oend]
for e in all2:
    if e not in keep and e.tag != qn('w:sectPr'): b2.remove(e)
b2.insert(0, para('This was Chapter 17, “The Omega Point: Outside Space and Time” (Teilhard de Chardin and Frank Tipler). The 11 Oct 2026 strict review called it off-topic for a volume on motion, forces, time and relativity: it is theology and speculative cosmology rather than physics the book teaches. It is kept here unchanged so nothing is lost; it could return in Volume 2 (cosmology) or a future essay collection.', jc='left'))
b2.insert(0, para([('Moved out of Physics, Actually, Volume 1 on 11 Oct 2026 (PT).', {'b': True})], jc='left'))
drop_unused_images(O2); O2.save(omega_out)
print('\n'.join(LOG))
