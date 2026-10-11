# Rev8 -> Rev9: all fixes from the 11 Oct 2026 critical review. Run on a copy; prints a check list.
import copy, re, sys, unicodedata
import docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from PIL import Image
SRC, DST = sys.argv[1], sys.argv[2]
IMG='/workspace/grav9/img/'
d = docx.Document(SRC); body = d.element.body
log=[]; errs=[]
def paras(): return [p for p in d.paragraphs]
def txt(p): return ''.join(t.text or '' for t in p._p.iter(qn('w:t')))
TOC_END = next(i for i,p in enumerate(paras()) if p.style.name=='Heading 1' and p.text=='Before you start')
heads = {}
for p in paras():
    if p.style.name.startswith('Heading'):
        bm = p._p.find(qn('w:bookmarkStart'))
        if bm is not None: heads[p.text] = bm.get(qn('w:name'))
def F(prefix, after=None):
    ps = paras(); start = TOC_END if after is None else after
    hits = [p for p in ps[start:] if txt(p).startswith(prefix)]
    if len(hits)!=1: raise SystemExit(f'F({prefix!r}) -> {len(hits)} hits')
    return hits[0]
def idx(p): return [q._p for q in paras()].index(p._p)
def rpr_of(r):
    x = r.find(qn('w:rPr')); return copy.deepcopy(x) if x is not None else None
def mk_run(text, rpr=None):
    r = OxmlElement('w:r')
    if rpr is not None: r.append(copy.deepcopy(rpr))
    t = OxmlElement('w:t'); t.text = text; t.set('{http://www.w3.org/XML/1998/namespace}space','preserve'); r.append(t); return r
LINK_RPR = None
def link_rpr():
    global LINK_RPR
    if LINK_RPR is None:
        h = next(body.iter(qn('w:hyperlink')))
        LINK_RPR = rpr_of(h.find(qn('w:r')))
    return LINK_RPR
def mk_link(anchor, text):
    h = OxmlElement('w:hyperlink'); h.set(qn('w:anchor'), anchor); h.set(qn('w:history'),'1')
    h.append(mk_run(text, link_rpr())); return h
def to_markup(p):
    out=[]
    for ch in p._p:
        tag = ch.tag.split('}')[1]
        if tag=='r': out.append(''.join(t.text or '' for t in ch.iter(qn('w:t'))))
        elif tag=='hyperlink':
            a = ch.get(qn('w:anchor'))
            if a is None: raise SystemExit('external link in rebuilt paragraph: '+txt(p)[:60])
            out.append('[[#%s|%s]]' % (a, ''.join(t.text or '' for t in ch.iter(qn('w:t')))))
    return ''.join(out)
def base_rpr(p):
    rs = [ch for ch in p._p if ch.tag==qn('w:r')]
    return rpr_of(rs[0]) if rs else None
def rebuild(p, markup, rpr=None):
    if rpr is None: rpr = base_rpr(p)
    for ch in list(p._p):
        if ch.tag in (qn('w:r'), qn('w:hyperlink')): p._p.remove(ch)
    pos = 0
    for m in re.finditer(r'\[\[(.+?)\]\]', markup):
        if m.start()>pos: p._p.append(mk_run(markup[pos:m.start()], rpr))
        inner = m.group(1)
        if inner.startswith('#'):
            a, t = inner[1:].split('|',1)
        else:
            if inner not in heads: raise SystemExit('no heading: '+inner)
            a, t = heads[inner], '“%s”' % inner
        p._p.append(mk_link(a, t)); pos = m.end()
    if pos < len(markup): p._p.append(mk_run(markup[pos:], rpr))
def uniform(p):
    rs = [ch for ch in p._p if ch.tag==qn('w:r')]
    ss = set((str(r.find(qn('w:rPr')).xml) if r.find(qn('w:rPr')) is not None else '') for r in rs)
    return len(ss)<=1
def R(prefix, old, new, after=None):
    p = F(prefix, after)
    if '[[' not in new:
        for t in p._p.iter(qn('w:t')):
            if t.text and old in t.text:
                t.text = t.text.replace(old, new, 1); log.append('R '+prefix[:40]); return p
    m = to_markup(p)
    if old not in m: errs.append(f'R miss: {prefix[:40]!r} / {old[:50]!r}'); return p
    if not uniform(p): errs.append('R non-uniform: '+prefix[:40]); return p
    rebuild(p, m.replace(old, new, 1)); log.append('R* '+prefix[:40]); return p
def T(prefix, new, after=None):
    p = F(prefix, after)
    if not uniform(p):
        rs=[ch for ch in p._p if ch.tag==qn('w:r')]; lab=''.join(x.text or '' for x in rs[0].iter(qn('w:t')))
        if not new.startswith(lab) or any(ch.tag==qn('w:hyperlink') for ch in p._p): errs.append('T non-uniform: '+prefix[:40]); return p
        br=rpr_of(rs[1])
        for r in rs[1:]: p._p.remove(r)
        p._p.append(mk_run(new[len(lab):], br)); log.append('TL '+prefix[:40]); return p
    rebuild(p, new); log.append('T '+prefix[:40]); return p
def DEL(prefix, after=None):
    p = F(prefix, after); p._p.getparent().remove(p._p); log.append('DEL '+prefix[:40])
def G(old, new, expect=None):
    n=0
    for t in body.iter(qn('w:t')):
        if t.text and old in t.text: n+=t.text.count(old); t.text=t.text.replace(old,new)
    if expect is not None and n!=expect: errs.append(f'G {old!r}: {n} (expected {expect})')
    log.append(f'G {old!r} x{n}')
def clone_after(anchor_el, template_p, label, text):
    np_ = copy.deepcopy(template_p._p)
    anchor_el.addnext(np_)
    rs = [ch for ch in np_ if ch.tag==qn('w:r')]
    lab_rpr, body_rpr = rpr_of(rs[0]), rpr_of(rs[-1])
    for ch in list(np_):
        if ch.tag in (qn('w:r'), qn('w:hyperlink')): np_.remove(ch)
    if label: np_.append(mk_run(label, lab_rpr))
    np_.append(mk_run(text, body_rpr))
    return np_

# ---------- front matter ----------
SUB = 'Einstein’s Gravity in Plain Words: Falling, Time, Black Holes, and the Waves We Finally Heard'
ps = paras()
sub_p = next(p for p in ps[:12] if p.text=='A Short Book on Gravity')
for t in sub_p._p.iter(qn('w:t')): t.text = ''
sub_p._p.findall(qn('w:r'))[0].find(qn('w:t')).text = SUB
cp = next(p for p in ps[:30] if p.text.startswith('Gravitation, Actually: A Short Book on Gravity'))
for t in cp._p.iter(qn('w:t')):
    if t.text: t.text = t.text.replace('A Short Book on Gravity', SUB)
d.core_properties.title = 'Gravitation, Actually: ' + SUB
d.core_properties.subject = 'Einstein’s gravity for general readers: falling, time, black holes, and gravitational waves'
pic = next(p for p in ps[:30] if p.text.startswith('Pictures. The twelve diagrams'))
rebuild(pic, 'Pictures. The thirteen diagrams (the two ants, the light clock, the two surveyors, the light cone, tidal stretching, the sheet and the clock-rate curve, the stack of clock-rate surfaces, the GPS clock budget, gravitational lensing, the slice of space around a black hole, the Kruskal map, the LIGO layout, and the slice through a wormhole), the three number tables, and both covers were drawn for this book with Python plotting scripts. No AI image generator was used for any picture in this book. Three pictures are real images, used under their licenses and credited where they appear: fruit floating in the International Space Station (NASA, public domain), the black hole in M87 by the Event Horizon Telescope Collaboration (CC BY 4.0), and the Bullet Cluster composite released by NASA (public domain). Details are on the Picture credits page.')

# ---------- Before you start (Look Inside opens with the apple) ----------
pa = T('The idea is simple, and it is strange.', 'Let go of an apple and nothing pulls it down. That is the idea of this book, and it is simple and strange. In a falling room the apple stays put beside your hand. The straight path is the falling one. The push you feel, standing on the Earth, is the ground getting in the way.')
pb = T('You may be on a beach.', 'That one idea is at work all around you. The sea will rise twice today. The phone in your pocket found you by comparing clocks. The cup on the table has a weight only while the table refuses to fall. Curiosity is enough to start, and the questions in this book are there for teaching yourself.')
pc = F('This is a book about gravity for a reader'); pr = F('Read a chapter. Close the book.'); pe = F('That picture comes from Einstein, worked out')
h = F('Before you start'); 
for el in (pa,pb,pe,pc,pr): el._p.getparent().remove(el._p)
anchor = h._p
for el in (pa,pb,pe,pc,pr): anchor.addnext(el._p); anchor = el._p
T('Each chapter opens with a box that names its one job', 'Early in each chapter, right after the opening scene, a short box headed In this chapter gives the goal, the route the chapter takes, the sentence to say and the sentence to retire, and one question to carry. Each chapter closes with a recap box and a set of exercises. The exercises are optional. They have numbers in them, and every one has a worked solution and the usual mistake, because the usual mistake is where most of the learning is. Where a later page leans on an earlier one, it names the section, so you can turn back to it.')

# ---------- chapter boxes: rebuild 7 and 8, relabel all, move below the opening scene ----------
c1q = F('The question to carry. If the apple is not being pulled')
c1_tpl = {k: F(v) for k,v in {'job':'The job. By the end you should be able to say: the apple','order':'The order. First the falling room','say':'Say. the apple let go','dont':'Do not say. zero gravity','q':'The question to carry. If the apple'}.items()}
def rebuild_box(header_prefix_after, items):
    hi = idx(F(header_prefix_after)); hdr = next(q for q in paras()[hi:] if q.text=='IN THIS CHAPTER')
    # remove everything after header until first non-box paragraph that is real prose
    el = hdr._p.getnext(); removed=0
    while el is not None and el.tag==qn('w:p'):
        t = ''.join(x.text or '' for x in el.iter(qn('w:t')))
        if t.startswith(('The job.','The order.','Say.','The question to carry.','If nothing is there to knock on')):
            nxt = el.getnext(); el.getparent().remove(el); el = nxt; removed+=1
        else: break
    a = hdr._p
    for key,(lab,text) in items:
        a = clone_after(a, c1_tpl[key], lab, text)
    log.append(f'box rebuilt after {header_prefix_after[:20]} (removed {removed})')
rebuild_box('7. The place you do not come back from', [
 ('job',('The job. ','By the end you should be able to say: a horizon is the last outward path, not a wall, and the shadow is larger than the door.')),
 ('order',('The order. ','First two true stories of one fall. Then how we know the holes are there, what the shell observers measure, spin, and the shadow. Then the temperature, which is calculated and unseen. Then two better pictures, the slice and the Kruskal map, and the orbits near the door.')),
 ('say',('Say. ','The horizon is the last outward path, and the shadow is larger than the door.')),
 ('dont',('Do not say. ','A wall, a funnel you fall into, a white hole in the catalog. The temperature is calculated; the glow has not been seen.')),
 ('q',('The question to carry. ','If nothing is there to knock on, what did the dishes photograph?'))])
rebuild_box('8. The bends can travel', [
 ('job',('The job. ','By the end you should be able to say: a lopsided change sends a ripple through the geometry, and since 2015 detectors have caught them.')),
 ('order',('The order. ','First why a still sphere does not send ripples. Then the bill, the shrinking pulsar orbit. Then the signal of 14 September 2015 and the months spent trying to kill it. Then the neutron-star collision, ripple and light 1.7 seconds apart.')),
 ('say',('Say. ','A lopsided change sends a ripple, and a detector caught one.')),
 ('dont',('Do not say. ','The black holes hummed. The audio online was shifted in pitch; the graph is the result.')),
 ('q',('The question to carry. ','If space between the mirrors is empty, what exactly stretched?'))])
# capitalize body after Say./Do not say., then relabel
LAB = {'The job. ':'Goal. ','The order. ':'Route. ','Say. ':'Say. ','Do not say. ':'Do not say. ','The question to carry. ':'A question to carry. '}
for p in paras()[TOC_END:]:
    rs = [ch for ch in p._p if ch.tag==qn('w:r')]
    if len(rs)>=2:
        t0 = ''.join(x.text or '' for x in rs[0].iter(qn('w:t')))
        if t0 in LAB and rs[0].find(qn('w:rPr')) is not None and rs[0].find(qn('w:rPr')).find(qn('w:b')) is not None:
            rs[0].find(qn('w:t')).text = LAB[t0]
            bt = rs[1].find(qn('w:t'))
            if bt is not None and bt.text and bt.text[0].islower(): bt.text = bt.text[0].upper()+bt.text[1:]
# move each box (header + following box paragraphs) to just before the chapter's first Heading 2
ps = paras(); moved=0
for i,p in enumerate(ps):
    if p.style.name=='Heading 1' and i>TOC_END:
        j=i+1
        if j<len(ps) and ps[j].text=='IN THIS CHAPTER':
            box=[ps[j]]; k=j+1
            while k<len(ps) and ps[k]._p.find(qn('w:pPr')) is not None and ps[k]._p.find(qn('w:pPr')).find(qn('w:pBdr')) is not None and ps[k].text!='IN THIS CHAPTER':
                box.append(ps[k]); k+=1
            h2 = next((q for q in ps[k:] if q.style.name.startswith('Heading')), None)
            if h2 is None or h2.style.name!='Heading 2': errs.append('no H2 after box '+p.text); continue
            for b in box: b._p.getparent().remove(b._p)
            for b in box: h2._p.addprevious(b._p)
            moved+=1
log.append(f'boxes moved: {moved}')
T('Route. First the minus sign, with no paradox attached.', 'Route. First the minus sign, with no paradox attached. Then the surveyors, the train, and the twin, each one interval sliced two ways. Then the light clock and the muons, orbits and light as straight paths, the light cone, the pole in the barn, and clocks flown on airliners. A paradox in a popular book is usually two slices treated as one.') if False else None
def box_body(prefix, newbody):
    p = F(prefix); rs=[ch for ch in p._p if ch.tag==qn('w:r')]
    for r in rs[1:]: p._p.remove(r)
    rs[1].find(qn('w:t')).text = newbody if False else None
    p._p.append(mk_run(newbody, rpr_of(rs[1]))); log.append('box '+prefix[:30])
box_body('Route. First the minus sign, with no paradox attached.', 'First the minus sign, with no paradox attached. Then the surveyors, the train, and the twin, each one interval sliced two ways. Then the light clock and the muons, orbits and light as straight paths, the light cone, the pole in the barn, and clocks flown on airliners. A paradox in a popular book is usually two slices treated as one.')
box_body('Route. First one cabin.', 'First one cabin. Then two cabins whose straight paths will not stay parallel. Then the beach, where the sea rises twice a day, so a string from the Moon is the wrong picture. The harbor table can stay Newton’s. The explanation cannot.')
box_body('Route. First the hair in Mercury', 'First the one equation, said in a sentence: the bend follows the stuff. Then the audits: Mercury’s orbit, the phone in your pocket, late radar echoes, the Moon, and spinning gyroscopes. Then gradients pictured as stacks of surfaces, and two pieces of history, the 1919 eclipse and the Harvard tower. You do not calculate the equation here. You do not drop it.')
R('A question to carry. If Newton', 'what was the hair in Mercury’s orbit doing there?', 'what was the small leftover turn in Mercury’s orbit doing there?')
R('Do not say. The Moon lifts the ocean on a string.', 'The beach has two.', 'Most beaches have two.')
R('Say. Weighed, timed, or imaged is a result.', 'Weighed, timed, or imaged is a result. A reading is a reading.', 'What has been weighed, timed, or imaged is a result. An interpretation is only an interpretation.')
R('Route. First what has been weighed', 'Then what is a proposal: grains, strings, a frozen river, Nows, an Omega Point, a traversable throat.', 'Then what is a proposal: candidates for quantum gravity, readings of time, an Omega Point, a traversable throat.')


# box wording tidy (after relabel)
box_body('Do not say. Time slows down for the person', 'Time slows down for the person holding the clock. One of the two observers must be mistaken.')
box_body('Do not say. A black hole is a hole in the sky', 'A black hole is a hole in the sky. Every heavy star becomes one.')
box_body('Do not say. Galaxies are flying into a dark room', 'Galaxies are flying into a dark room. Dark energy is a substance someone has caught.')
box_body('Route. White dwarf, then the limit', 'First the white dwarf and its limit, then the neutron star and its limit, then what happens past the last size. Then the shrinking pulsar orbit that paid the wave bill. The first pulsar and Chandrasekhar’s voyage come last, as history.')

# ---------- chapter 1 ----------
R('Now imagine the same let-go', 'For those few seconds the room is quiet a room on the ground never is.', 'For those few seconds the room is quieter than any room on the ground.')
R('Pilots know the other way around.', 'In a training plane, when the nose is pointed right and the engine is quiet, there is a stretch of the dive where a pencil floated in the cockpit will stay where it is put.', 'In a training plane flying a parabola, with the engines set just to cancel the drag of the air, there is a stretch of about twenty seconds, over the top and down again, where a pencil let go in the cockpit stays where it is put.')
DEL('The space station is about 400 kilometers up. Gravity there is still about nine-tenths')
DEL('Newton’s pull is still the tool for a harbor and a probe to Mars.')
R('The eight years after were not happy', 'Mercury’s hair came out. The light-bending came out, twice the number he had published earlier and then doubted.', 'The tiny leftover turn in Mercury’s orbit, a hair’s width in the sky that had puzzled astronomers for decades (see [[The planet that would not sit still]]), came out. The bending of starlight by the Sun came out, twice the number he had published in 1911.')
R('That failure to join is the whole of gravity.', 'That failure to join is the whole of gravity.', 'That failure to join is the signature of gravity: the part that no choice of room can remove.')
R('That failure to join is the signature', 'The world has a shape that will not lie flat.', 'The world has a shape that will not lie flat. What sets the falling path itself, near the Earth, is the way clocks run faster with height (see [[A clock higher up]]).')
R('The first wrong picture is that astronauts', 'The station is a long day’s drive up, if a road went there,', 'The station is about 400 kilometers up, a four-hour drive at highway speed if a road went straight up,')
R('The second wrong picture is that weightlessness', 'The experiment has stopped fighting.', 'You have simply stopped resisting the fall.')
R('The third wrong picture is that Newton', 'when a star has no last size', 'when a dying star finds no size it can hold')
DEL('This is why a bathroom scale cannot be trusted')
T('The shop can keep the sentence that the apple fell.', 'Everyday speech can keep the sentence that the apple fell. Physics adds what the scale cannot see: nothing tugs the apple down, and the ground declined the path the apple is on.')
R('A company will sell you twenty seconds', 'The plane is over the Earth, close enough that a road, if it went straight up, would be a long drive and not a voyage.', 'The plane is only about ten kilometers up, a ten-minute drive if a road went straight up.')
R('Pilots call the path a parabola.', 'Agreement is what removes the sensation of weight. Disagreement is what you have been paying the scale to report.', 'When the floor follows the same path as your body, you feel no weight. When it refuses, the scale reports the push.')
R('John Wheeler liked sentences a person could carry', 'Mass tells spacetime how to curve. Spacetime tells mass how to move.', 'His two-part slogan for the theory is the one quoted in [[The ant on the apple]].')
R('Wheeler did not invent the name black hole.', 'Good names do that. They do not ask permission twice.', 'A good name, once it sticks, rarely needs defending.')
R('•  Small falling rooms work.', 'and that failure to join is gravity.', 'and that failure to join is the part of gravity no falling room can hide.')

# ---------- chapter 2 ----------
T('•  Ground book: the event is 5 seconds', '•  Ground book: the event is 5 seconds after the start and 3 light-seconds away. With the book’s sign convention, the interval squared is −5² + 3² = −25 + 9 = −16. Negative means timelike.')
R('•  Ship book: the ship left the start at 0.6c', 'whatever makes the interval 16, so 4 seconds.', 'whatever makes the interval squared −16 again, so 4 seconds.')
T('•  The ship’s clock reads 4 s', '•  The ship’s clock reads 4 s, the ground’s clocks read 5 s, and both books agree on −16. (Some books put the minus on space instead and write +16. The sign is a convention. The agreement is the physics.)')
R('A lamp flashes in the middle of a moving train.', 'The platform person sees the back flash first.', 'The platform person sees the flash reach the back of the train first.')
T('Taylor and Wheeler give the rule a name, the principle of maximal aging', 'Taylor and Wheeler, in Spacetime Physics and again in Exploring Black Holes, give the rule a name, the principle of maximal aging: between two meetings, a free clock takes the path on which it ages the most. In flat spacetime any detour, turnaround, or rocket burn costs the traveler time. Near a mass the rule still holds for nearby paths: a free fall ages more than its close neighbors.')
R('At a walk, the disagreement of clocks', 'The particle’s own clock is not generous. The laboratory is watching a detour.', 'The particle’s own clock runs normally. The laboratory sees a longer life because the particle’s path through spacetime is not the laboratory’s path.')
R('The same is true of the Moon, and of the Earth around the Sun.', 'and the straightness there looks like an ellipse to us, standing on the moving Earth and counting days.', 'and that straightest path, drawn in space alone, is the nearly circular ellipse astronomers chart.')
R('A light ray is the interval set to zero.', 'The edge is policed. The police are the measurements.', 'Every measurement so far has respected that edge.')
R('The crews did not age differently', 'You need a clock ruder than a wristwatch', 'You need a clock far better than a wristwatch')

# ---------- chapter 3 ----------
R('In a small falling room, gravity disappears.', 'In a small falling room, gravity disappears.', 'In a small falling room, the feel of gravity disappears.')
R('That leftover, the drift you cannot remove', 'It is gravity in the only sense that is not just the floor pushing back.', 'It is the part of gravity that no falling room can hide. (The ordinary fall itself is set by how clocks run at different heights; see [[A clock higher up]].)')
R('The Moon is falling around the Earth, and the Earth', 'The Earth turns under them, and a beach has two high tides a day.', 'The Earth turns under them, and most beaches have two high tides a day. (The shape of a coast and its basins can change that, and a few places get only one.)')
T('Spring tides, when Sun and Moon line up', 'Spring tides, when Sun and Moon line up, are the two mismatches adding. Neap tides, when Sun and Moon pull at right angles, are the two partly cancelling, so the tides are smaller. The geometry does not take sides. It adds.')
R('The apple’s fall is this fact, seen as a path.', 'It is taking the route that spends the time the geometry allows.', 'It takes the path on which its own clock records the most time, and near the Earth that path curves downward.')
R('The tide is not the Moon lifting the ocean', 'and it is why a beach has two.', 'and it is why most beaches have two.')
R('•  The beach has two high tides a day', 'The beach has two high tides a day', 'Most beaches have two high tides a day')
R('Worked solution. 9.81 × 3 / (3.0 × 10⁸)²', 'Optical clocks now see height differences of a few centimeters.', 'Optical clocks now resolve height differences of a centimeter or less.')

# ---------- chapter 4 ----------
R('There is a way to see the right-hand side', 'For light it is not, which is one reason light gravitates more than a simple tally of its mass would suggest.', 'For light it is not. In a box of light the pressures in the three directions add up to as much as the energy density itself, so the ball shrinks twice as fast as it would around the same energy at rest.')
R('Vulcan is a useful ghost.', 'Later, the same habit will invent substances for dark matter and dark energy. Some of those may be real bodies.', 'Later, astronomers will again meet missing pulls, in galaxies and in the expansion of the universe, and name them dark matter and dark energy. The evidence for dark matter is strong, and it may well be a real substance.')
R('That sounds like nothing. Light travels about 11', 'The receiver in your phone finds you by comparing clock signals from several satellites. Leave the correction out and your position wanders by kilometers in a day.', 'The receiver in your phone finds you by timing signals from several satellites, so a clock error becomes a distance error. Leave the correction out and the computed distances to the satellites grow wrong by about 11 kilometers a day, and the fix on your position wanders by kilometers.')
R('The satellite clock is not in a weaker force', 'The satellite clock is not in a weaker force, so it runs oddly. It is higher in a bend.', 'The satellite clock does not run fast because some force on it is weaker. It runs fast because it sits higher in the bend in time.')
R('It is not a recipe for every motion in the sky.', 'Wheeler’s sentence is the whole of it. Mass-energy tells spacetime how to curve. Spacetime tells mass-energy how to move.', 'That is Wheeler’s two-way grip again (see [[The other equation]]).')
R('The picture fits this book better than it looks.', 'If each layer marks one part in 10¹⁶, about what the best optical clocks can see,', 'If each layer marks one part in 10¹⁶ (the best optical clocks now resolve about a hundred times finer),')
R('Einstein, shown the telegram', 'A story has him saying he would have been sorry for the Lord, the theory being correct. The story is too neat.', 'His student Ilse Rosenthal-Schneider later recalled him saying that, had the result gone the other way, he would have felt sorry for the dear Lord, because the theory was correct. The story rests on one memory, written down years later, and it is too neat to lean on.')
R('Einstein, shown the telegram', 'The theory had already got Mercury’s hair without an audience.', 'The theory had already explained Mercury’s orbit without an audience.')
R('Their first result matched the prediction', 'across a few centimeters of height on a laboratory bench', 'across a centimeter or less of height on a laboratory bench')
R('•  A GPS clock gains about 45.7 microseconds', 'Without the net correction, positions drift about 11 kilometers a day.', 'Without the net correction, the distances to the satellites would grow wrong by about 11 kilometers a day.')
G('the speed that cancelled the shift', 'the speed that canceled the shift', 1)
# exercises 4.4 (Extension) after the Core ones: new order 4.5->4.4, 4.6->4.5, 4.7->4.6, 4.4->4.7
e44 = F('Exercise 4.4'); ps=paras(); i44=idx(e44); blk=ps[i44:i44+4]
e48 = F('Exercise 4.8')
for b in blk: b._p.getparent().remove(b._p)
for b in blk: e48._p.addprevious(b._p)
for old,new in (('Exercise 4.5','Exercise 4.4'),('Exercise 4.6','Exercise 4.5'),('Exercise 4.7','Exercise 4.6')):
    t = F(old)._p.find(qn('w:r')).find(qn('w:t')); t.text = new
t = blk[0]._p.find(qn('w:r')).find(qn('w:t')); t.text='Exercise 4.7'
log.append('exercises 4.4-4.7 reordered')

# ---------- chapter 5 ----------
R('A star like the Sun ends as a white dwarf', 'on the boat to England. Older astronomers', 'on the boat to England. Wilhelm Anderson and Edmund Stoner had reached similar limits a little earlier by rougher routes; Chandrasekhar’s treatment is the one that lasted. Older astronomers')
R('What they had found was a neutron star', 'The city-sized ember of the last chapter was no longer a dare.', 'The city-sized ember described earlier in this chapter was no longer a dare.')
R('In 1974 the Nobel Prize for pulsars', 'She has told the story since without the bitterness a lesser person would have rented out. She has also said, which is the useful part, that the finding was real and the omission was real, and that both can be true.', 'She has told the story since without bitterness. She has said that, by the custom of the time, the prize went to the senior people who led the project, and that she did not think it unfair, although many colleagues protested on her behalf.')
R('Eddington had been right about the eclipse.', 'Being right once is not a subscription. The sky does not offer those.', 'Being right once does not make anyone right the next time.')
R('Worked solution. Per year: 2.4 × 10⁻¹²', 'and it matches the energy the waves should carry away.', 'and it matches the energy the waves should carry away. What astronomers actually track is the time of each closest approach, which comes earlier and earlier as the orbit shrinks. After three decades the accumulated shift is tens of seconds, and it follows Einstein’s prediction closely.')

# ---------- chapter 6 ----------
R('The galaxies are not rushing outward', 'A galaxy is not, for this purpose, moving. The ruler is growing.', 'It is better to say the galaxies are carried apart by the stretching than that they fly through space. The ruler is growing.')
T('Edwin Hubble, in 1929, found', 'Georges Lemaître in 1927, and Edwin Hubble in 1929 with better distances, found that galaxies have their light shifted redder, and the farther ones more so. Redder, for light, means the wave was stretched on the way. The simple reading, and the right one, is that the stretch happened in the travel. In the old language, distance and speed go together. In the better language, the redshift says how much the scale of the universe grew while the light was on its way.')
R('Arno Penzias and Robert Wilson found the glow in 1964', 'while trying to get a hiss out of an antenna. They thought it might be pigeon droppings. It was the early universe.', 'while trying to get rid of a hiss in an antenna (see [[The pigeons were innocent]]). It was the early universe.')
T('The speedup is young as a discovery', 'The speedup is young as a discovery and old as a fact. The supernovae that revealed it exploded billions of years ago, many of them before the Earth existed. Their light was already on its way. In 1998 it arrived in the data.')
G('travelling', 'traveling')

# ---------- chapter 7 ----------
ps=paras()
for name in ('Two true stories','How we know they are there'):
    dup=[p for p in ps[TOC_END:] if p.text==name and p.style.name=='Normal']
    for p in dup: p._p.getparent().remove(p._p); log.append('DEL dup '+name)
R('At the center of the Milky Way, stars whip', 'The region they orbit in is not much larger than the solar system.', 'The region they orbit in is tiny on a galactic scale: the closest star’s orbit is only about thirty times the size of Neptune’s.')
R('At the center of the Milky Way, stars whip', ' Patience is an instrument. It just looks like a career.', '')
R('Most of these objects spin.', 'Outside the horizon of a fast spinner', 'Outside the horizon of a spinning hole')
R('The Sun, squeezed to a black hole', 'M87’s horizon is larger than the solar system.', 'M87’s horizon is larger than the orbits of all the planets around the Sun.')
R('The Sun, squeezed to a black hole', 'Size is not a detail. Size is the experience.', 'What you would feel depends on the size of the hole.')
R('John Wheeler put the name “black hole” into general use', 'John Wheeler put the name “black hole” into general use in 1967; he did not coin it, and he adopted it gladly. The geometry was older.', 'The name came later (see [[A room at Princeton]]). The geometry was older.')
# Figure 16 caption and text
T('A flask-shaped slice', 'Two sheets joined by a throat: a slice through a wormhole geometry at one moment, drawn as a surface. A still picture, not a tunnel that stays open.')
R('The funnel in the tides chapter was a dent in a sheet.', 'Far away the surface is flat.', 'Far away the surface is nearly flat.')

# ---------- chapter 8 ----------
R('The instrument is a ruler made of light.', 'The change in a 4 kilometer arm, for the waves we can catch, is a few thousandths of the width of a proton.', 'For the strongest waves caught so far, the difference between the two arm lengths changes by a few thousandths of the width of a proton.')
R('Since 2015 the catalogs have filled.', 'and at least one pair that looks like a black hole with a neutron star', 'and black hole with neutron star')
T('On 14 September 2015 the two LIGO sites recorded the same rising note', 'The signal arrived on 14 September 2015, days after the upgraded detectors had been switched on, and the collaboration’s first reaction was suspicion. A blind injection, a fake signal planted to test the team, was one fear. A fault, or a disturbance felt at both sites, was another. They confirmed that no injection had been made, searched thousands of sensors for local noise, and showed that the delay between the sites matched light travel and the shape matched waveforms computed years before. Only then, in February 2016, did they say it out loud.')
T('•  LIGO’s 4-kilometer arms changed length', '•  The difference between LIGO’s two 4-kilometer arms changed by a few thousandths of a proton’s width in 2015.')
T('Horizon area grows as the square of the mass.', 'For a hole that does not spin, horizon area grows as the square of the mass. Before GW150914: 36 and 29 Suns, both spinning little. After: one hole of 62 Suns, spinning at about two-thirds of the maximum. Compare the total horizon area before and after, first ignoring the spin, then allowing for it.')
T('Worked solution. Before: 36² + 29²', 'Worked solution. Ignoring spin: before, 36² + 29² = 1,296 + 841 = 2,137 units; after, 62² = 3,844 units, about 80 percent more. Spin shrinks a horizon: at two-thirds of the maximum the area is about 0.87 of the non-spinning value, so the final hole has about 3,350 units, still about 57 percent more than before. Either way the area grew while the mass went down by 3 Suns, as Hawking’s area theorem requires.')
R('The usual mistake. Adding the masses first and squaring once', 'Areas add, masses squared.', 'Areas add; masses are squared first.')

# ---------- What is still open ----------
R('The inside is not in order.', 'Stephen Hawking showed that', 'Stephen Hawking calculated that')
R('Empty space weighs a little', 'Neither is explained.', 'Neither is explained. A third, smaller puzzle is a disagreement over how fast the universe expands today: measured nearby, from stars and supernovae, the rate comes out near 73 kilometers a second per megaparsec; inferred from the microwave glow, near 67. This Hubble tension may be a hidden error or a hint of something new.')
R('Proposals. A multiverse', 'Grains of space, strings, a frozen river, time made only of Nows, an Omega Point.', 'Grains of space (loop quantum gravity, in which space comes in smallest pieces). Strings (string theory, in which particles are tiny vibrating strings). A “frozen river” (the block-universe reading, in which past, present, and future all exist alike). Time made only of “Nows” (Julian Barbour’s proposal that time is not fundamental). An Omega Point (Frank Tipler’s final state of unlimited computation).')

# ---------- Appendix A ----------
T('Check. Can a later notice in the same room', 'Check. Can a change of frame reverse the order of two events in the same room, one after the other? No. Those two events are timelike, and their order is the same for everyone.')
T('Keep straight. Petrol is the wrong analogy.', 'Keep straight. Fuel is the wrong analogy. On a road the direct driver burns less fuel. In spacetime the straight path ages more.')
R('The detail. Two balls a mile apart', 'Two balls a mile apart', 'Two balls a kilometer apart')
R('Keep straight. The principle was never a promise', 'The mismatch is the tide, and the tide is the real gravity.', 'The mismatch is the tide: the part of gravity no falling room can hide.')
T('The detail. The gap is an argument about the last size.', 'The detail. The gap is an argument about the last size. A few merging objects have been weighed inside it, at about 2.5 to 4 Suns, so the gap may be a scarcity rather than an empty band. The argument is not closed.')
T('Check. What would close the gap as a fact?', 'Check. What would settle what the objects in the gap are? A measured size, or light from the merger, showing whether each is a neutron star or a black hole.')
T('Check. What is the door for the Sun, as a comparison?', 'Check. How big would the horizon be if the Sun were squeezed into a black hole? About 3 kilometers in radius. The Sun will never be squeezed like that.')
T('The detail. M87, 2019, about 6.5 billion suns', 'The detail. M87, 2019: about 6.5 billion Suns, a horizon larger than the orbits of all the planets. Our own center, 2022: about 4 million Suns, already weighed by the star S2, followed for about thirty years around its sixteen-year orbit, with a reddening at closest approach.')
T('The detail. The glow has not been seen.', 'The detail. The radiation has not been seen. The temperature is a result of the theory. Observing it is still an open bill.')
T('Keep straight. A smooth paragraph about information', 'Keep straight. A confident story about what happens to information that falls in is not a result. It is an open question.')
T('Keep straight. A ringdown is not a hum', 'Keep straight. A ringdown is not a hum you could sing. It is the last part of the measured signal, fitted with the predicted pitches.')
R('What it is. A chirp used as a distance.', 'The waves tell you how far they have come if you know the masses.', 'The waveform itself gives the masses, so its strength gives the distance.')
T('Keep straight. A siren is not a lamp.', 'Keep straight. A siren is not a lamp. It does not need a known brightness. It needs only the waveform: the masses come from its shape, the distance from its strength.')
T('The detail. Satellites have seen the same drag', 'The detail. The orbits of the laser-ranged satellites LAGEOS and LARES show the same drag. How precise those results are is still argued over.')
T('Keep straight. Frame dragging is not a flourish.', 'Keep straight. Frame dragging is a real prediction, and it has been measured, though not yet very precisely.')
T('Check. Which instrument was cleaner', 'Check. Has frame dragging been seen by more than one method? Yes: by gyroscopes in orbit and by satellite orbits.')
T('Keep straight. An orbit is not a track.', 'Keep straight. An orbit near a hole does not close. Each lap swings around a little, as Mercury’s does, and near the last stable orbit the swing is large.')
T('Check. Can you send Tuesday to Andromeda', 'Check. Can walking get a message to Andromeda faster? No.')
T('Keep straight. Calling the 2017 merger a supernova.', 'Keep straight. The 2017 merger was a kilonova, not a supernova.')

# ---------- Appendix C ----------
T('The 1960s experiment is the cleaner classroom version.', 'The 1963 measurement by David Frisch and James Smith, on Mount Washington, is the cleaner classroom version. Rossi and Hall’s wartime one came first.')
T('Priority and clarity are different virtues.', 'The first experiment and the clearest one are both worth citing.')
T('A rocket clock is a tower with a larger tower.', 'A clock on a rocket is the tower experiment with a much taller tower.')
T('An orbit is a weigh. A reddening is a clock.', 'The orbit gives the mass. The reddening tests how clocks run near it.')
T('The patch is larger than the door.', 'The dark patch is larger than the horizon: about 5.2 horizon radii across for a hole that does not spin. Leave out that factor and the mass comes out about 2.6 times too large.')
T('A fidgeting patient is a worse photograph', 'A changing source blurs the picture. It does not change the mass.')
T('The center of the Milky Way is not a quiet lamp.', 'The gas around our own black hole flickers within minutes.')
T('A subscription is not a measurement.', 'The bet is a story. The orbit is the measurement.')
T('A hum you can sing has been moved.', 'If you can hum it, it has been shifted in pitch. Say so when you play it.')
R('The round trip to the Apollo mirrors is timed to centimeters.', 'The round trip to the Apollo mirrors is timed to centimeters.', 'The round trip to the mirrors left by Apollo crews is timed well enough to give the distance to a few millimeters.')
T('A centimeter is the result. The romance', 'The measurement needs only the mirrors, not the history of the landings.')
T('A centimeter of height is a rate.', 'Comparing two clocks can now measure a difference in height.')
T('The birthday remains a rude instrument.', 'Over a human lifetime these differences remain far too small to notice.')

# ---------- Appendix D ----------
T('Energy density is the familiar source.', 'Energy density is the familiar source. Momentum, pressure, and shear are sources too. A single particle of light has no rest mass, yet a box full of light weighs more than the empty box, and it bends the geometry, because the light carries energy and pressure. Inside a neutron star the pressure that keeps the star from collapsing is itself a source of the bend that is trying to collapse it. That is why pushing harder is not a strategy past the last size: the push joins the load. In the solar system these extra sources are tiny beside mass, which is why Newton remains the tool for a probe. Mercury’s extra 43 seconds of arc a century do not come from them. They come from the shape of the geometry outside the Sun itself, where space is slightly curved and the rule’s corrections to Newton grow as Mercury swings close.')
R('Each arm is four kilometers.', 'Hospitality is not data.', 'Shifting the pitch makes it audible. It does not change the measurement.')

# ---------- Appendix E ----------
R('Why do astronauts float if gravity', 'The floor has agreed to the path. Agreement removes the press. Escape would be a speed that does not come back. They are coming back, and missing.', 'The floor falls with them, so nothing presses. They are not escaping. They keep falling around the Earth and missing it.')
R('Why two high tides?', 'The harbor has been counting for longer than there have been harbors.', 'Tide tables have recorded the pattern for centuries.')
R('What did Mercury’s hair measure?', 'What did Mercury’s hair measure?', 'What did the leftover turn in Mercury’s orbit measure?')
R('Has Hawking radiation been seen?', 'The glow is an unpaid observation.', 'No one has observed it yet.')
R('Why were the lamps too faint?', 'and not the enormous little the quantum rules suggest', 'and not the enormous value the quantum rules suggest')
R('What is dark matter, as a measurement?', 'The Bullet cluster passed through itself, the gas stayed in the middle', 'In the Bullet Cluster two clusters passed through each other, the gas stayed in the middle')
R('What is dark matter, as a measurement?', 'The owner has not been caught in a tank.', 'No detector has yet caught a dark-matter particle.')
R('What did the mailbox catch in 2015?', 'The change in a four-kilometer arm was a few thousandths of a proton.', 'At the peak, the two arm lengths differed by a few thousandths of a proton’s width.')
R('What arrived 1.7 seconds after the 2017 ripple?', 'Ideas in which the ripples would outrun light had a bad afternoon.', 'Theories in which gravity and light travel at different speeds were ruled out.')
R('What is a standard siren?', 'The waves tell you how far they have come if you know the masses.', 'The waveform itself gives the masses, so its strength gives the distance.')

# ---------- glossary: add and sort ----------
g = F('Glossary'); ps=paras(); gi=idx(g); gl=[]
for q in ps[gi+1:]:
    if q.style.name.startswith('Heading'): break
    gl.append(q)
tpl = gl[0]
for e in ['Cosmological constant. A steady weight of empty space, written into Einstein’s rule as one extra number. The simplest candidate for dark energy.',
          'Geoid. The surface of equal gravitational-plus-rotational potential that the sea settles on. Clocks at rest on it tick at the same rate.',
          'Innermost stable orbit. The smallest circular orbit a stone can keep around a black hole: three horizon radii for one that does not spin. Inside it, the stone plunges.',
          'Photon sphere. The radius, 1.5 times the horizon radius for a hole that does not spin, where light can circle the hole. The circle is unstable.',
          'Standard siren. A gravitational-wave event used to measure distance: the waveform gives the masses, and its strength gives the distance.',
          'Strain. The fractional change in length that a gravitational wave causes, a pure number. LIGO’s first signal peaked at about 10⁻²¹.']:
    np_=copy.deepcopy(tpl._p); gl[-1]._p.addnext(np_); import docx.text.paragraph as dtp; P=dtp.Paragraph(np_, tpl._parent)
    lab,rest=e.split('. ',1); rs=[ch for ch in np_ if ch.tag==qn('w:r')]
    if len(rs)>=2:
        lr,br=rpr_of(rs[0]),rpr_of(rs[-1])
        for r in rs: np_.remove(r)
        np_.append(mk_run(lab+'. ',lr)); np_.append(mk_run(rest,br))
    else: rebuild(P,e)
    gl.append(P)
def key(p): return unicodedata.normalize('NFKD',txt(p)).encode('ascii','ignore').decode().lower()
srt=sorted(gl,key=key)
for q in gl: q._p.getparent().remove(q._p)
a=g._p
for q in srt: a.addnext(q._p); a=q._p
log.append(f'glossary sorted: {len(srt)} entries')

# ---------- sources ----------
R('Taylor, Edwin F., and John Archibald Wheeler. Exploring Black Holes', 'Second edition with Edmund Bertschinger, free online under a Creative Commons licence, 2017.', 'A second edition, with Edmund Bertschinger, is free online.')
pb_ = F('Baez, John C., and Emory F. Bunn.')
hp = F('Papers and measurements'); ps=paras(); pi=idx(hp); papers=[]
for q in ps[pi+1:]:
    if q.style.name.startswith('Heading'): break
    papers.append(q)
pb_._p.getparent().remove(pb_._p); papers[-1]._p.addnext(pb_._p); papers.append(pb_)
tplp=papers[0]
for e in ['Clowe, D., et al. “A Direct Empirical Proof of the Existence of Dark Matter.” The Astrophysical Journal Letters 648, L109 (2006). The Bullet Cluster.',
 'Delva, P., et al. “Gravitational Redshift Test Using Eccentric Galileo Satellites.” Physical Review Letters 121, 231101 (2018).',
 'Frisch, D. H., and J. H. Smith. “Measurement of the Relativistic Time Dilation Using μ-Mesons.” American Journal of Physics 31, 342 (1963).',
 'Herrmann, S., et al. “Test of the Gravitational Redshift with Galileo Satellites in an Eccentric Orbit.” Physical Review Letters 121, 231102 (2018).',
 'Hewish, A., S. J. Bell, J. D. H. Pilkington, P. F. Scott, and R. A. Collins. “Observation of a Rapidly Pulsating Radio Source.” Nature 217, 709 (1968).',
 'Hubble, Edwin. “A Relation between Distance and Radial Velocity among Extra-Galactic Nebulae.” Proceedings of the National Academy of Sciences 15, 168 (1929).',
 'Lemaître, Georges. “Un Univers homogène de masse constante et de rayon croissant rendant compte de la vitesse radiale des nébuleuses extra-galactiques.” Annales de la Société Scientifique de Bruxelles A47, 49 (1927).',
 'Oppenheimer, J. R., and H. Snyder. “On Continued Gravitational Contraction.” Physical Review 56, 455 (1939).',
 'Planck Collaboration. “Planck 2018 Results. VI. Cosmological Parameters.” Astronomy & Astrophysics 641, A6 (2020). The expansion rate from the microwave glow.',
 'Riess, A. G., et al. “A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km s⁻¹ Mpc⁻¹ Uncertainty from the Hubble Space Telescope and the SH0ES Team.” The Astrophysical Journal Letters 934, L7 (2022). The expansion rate measured nearby.',
 'Rossi, Bruno, and David B. Hall. “Variation of the Rate of Decay of Mesotrons with Momentum.” Physical Review 59, 223 (1941).',
 'Vessot, R. F. C., et al. “Test of Relativistic Gravitation with a Space-Borne Hydrogen Maser.” Physical Review Letters 45, 2081 (1980). Gravity Probe A.',
 'Weisberg, J. M., and Y. Huang. “Relativistic Measurements from Timing the Binary Pulsar PSR B1913+16.” The Astrophysical Journal 829, 55 (2016). The accumulated shift of the orbit.']:
    np_=copy.deepcopy(tplp._p); papers[-1]._p.addnext(np_); P=dtp.Paragraph(np_, tplp._parent); rebuild(P,e); papers.append(P)
def pkey(p):
    t=txt(p); m=re.search(r'\((\d{4})\)',t); a=unicodedata.normalize('NFKD',t.split('“')[0]).encode('ascii','ignore').decode().lower()
    return (a, m.group(1) if m else '')
srt=sorted(papers,key=pkey)
for q in papers: q._p.getparent().remove(q._p)
a=hp._p
for q in srt: a.addnext(q._p); a=q._p
log.append(f'papers sorted: {len(srt)}')

# ---------- picture credits page ----------
T('Diagrams (two ants, light clock', 'Diagrams (two ants, light clock, two surveyors, light cone, tidal stretching, the sheet and the clock-rate curve, stack of clock-rate surfaces, GPS clock budget, gravitational lensing, slice of space around a black hole, Kruskal map, LIGO layout, slice through a wormhole) and the three number tables: drawn for this book with Python plotting scripts. The ants, surveyors, stack, slice, and Kruskal diagrams illustrate teaching ideas from Taylor and Wheeler and from Misner, Thorne, and Wheeler, drawn new. They are not copies of those books’ figures.')
DEL('Illustration (wormhole flask): made for this book.')
T('Cover: illustration made for this book; lettering by the author.', 'Covers: drawn for this book with Python scripts, a falling apple on a spacetime grid. No photographs and no AI image generators were used.')
bc = F('Bullet Cluster, chapter 6: X-ray')
rid = d.part.relate_to('https://commons.wikimedia.org/wiki/File:1e0657_scale.jpg', RT.HYPERLINK, is_external=True)
last = [ch for ch in bc._p if ch.tag==qn('w:r')][-1]; lt=last.find(qn('w:t'))
assert lt.text.endswith('Source: Wikimedia Commons, resized.'), lt.text[-60:]
lt.text = lt.text[:-len('Wikimedia Commons, resized.')]
hl=OxmlElement('w:hyperlink'); hl.set(qn('r:id'),rid); hl.set(qn('w:history'),'1'); hl.append(mk_run('Wikimedia Commons',link_rpr()))
last.addnext(hl); hl.addnext(mk_run(', resized.', rpr_of(last)))
log.append('Bullet Cluster credit linked')
G('licences','licenses'); G('licence','license')

# ---------- images ----------
def quant(path):
    im=Image.open(path)
    if path.endswith('.png'):
        q=im.convert('RGB').quantize(256, method=Image.Quantize.MEDIANCUT); out=path.replace('.png','_q.png'); q.save(out,optimize=True); return out
    return path
def replace_image(figname, path, descr=None):
    dp=[x for x in body.iter(qn('wp:docPr')) if x.get('name')==figname]
    assert len(dp)==1, figname
    inline=dp[0].getparent(); ext=inline.find(qn('wp:extent'))
    blip=next(inline.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip'))
    old=blip.get(qn('r:embed'))
    path=quant(path); rid,_=d.part.get_or_add_image(path); blip.set(qn('r:embed'),rid)
    w,h=Image.open(path).size; cx=int(ext.get('cx')); cy=int(cx*h/w)
    ext.set('cy',str(cy))
    for a in inline.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}ext'): a.set('cx',str(cx)); a.set('cy',str(cy))
    if descr:
        dp[0].set('descr',descr)
        for c in inline.iter('{http://schemas.openxmlformats.org/drawingml/2006/picture}cNvPr'): c.set('descr',descr)
    d.part.drop_rel(old) if sum(1 for b in body.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip') if b.get(qn('r:embed'))==old)==0 else None
    log.append(f'image {figname} -> {path.split("/")[-1]} {w}x{h}')
replace_image('Figure 1', IMG+'photo_iss_fruit_1200.jpg')
replace_image('Figure 3', IMG+'diag_surveyors.png', 'Two-panel diagram. Left: two pairs of map axes rotated against each other, with one line from the origin to a stake, labeled 5 km, with both sets of components. Right: ground time and space axes and a tilted pair of ship axes, with one event whose time and space parts differ in the two frames but whose interval squared is minus 16 in both.')
replace_image('Figure 13', IMG+'diag_embedding.png')
replace_image('Figure 14', IMG+'diag_kruskal.png')
replace_image('Figure 16', IMG+'diag_wormhole.png', 'Wireframe diagram of two flaring sheets joined by a narrow throat marked in red, with a green path from point A on the upper sheet through the throat to point B on the lower sheet.')
replace_image('Table 1', IMG+'table_speed.png')
replace_image('Table 2', IMG+'table_horizon.png', None)
replace_image('Table 3', IMG+'table_height.png')
t2=[x for x in body.iter(qn('wp:docPr')) if x.get('name')=='Table 2'][0]; t2.set('descr', t2.get('descr').replace('Horizon radius |','Horizon radius (if not spinning) |',1))

d.save(DST)
print('\n'.join(log)); print('ERRORS:' if errs else 'no errors'); print('\n'.join(errs))
