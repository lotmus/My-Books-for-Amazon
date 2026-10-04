# One-time build (2026-10-03), run from the book folder. The merged docx is now the master; edit it directly.
# Builds the merged "The Quantum World" (Part One = QW, Part Two = QC) from world.docx + merge/ md.
import docx, copy, re, json, os, sys
from docx.oxml import parse_xml
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from xml.sax.saxutils import escape
import qa_content as QA

SRC = sys.argv[1]  # the PRE-merge master, from D:\\bak\\2026-10-03 quanta merge\\
OUT = sys.argv[2] if len(sys.argv) > 2 else 'build/The Quantum World.docx'
MD = 'chapters/'; BACK = 'chapters/back/'; FIG = 'Figures/'
NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
      'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
      'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
      'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"')
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
UNUSED = []   # QW passages cut in this build

d = docx.Document(SRC)
body = d.element.body
from lxml import etree
NSMAP={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','a':'http://schemas.openxmlformats.org/drawingml/2006/main','wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing','pic':'http://schemas.openxmlformats.org/drawingml/2006/picture'}
def xp(el, path): return etree._Element.xpath(el, path, namespaces=NSMAP)
def els(): return list(body.iterchildren())
def txt(el): return ''.join(xp(el, './/w:t/text()'))
def X(s):
    if 'xmlns:w=' not in s.split('>',1)[0]: s = re.sub(r'^<(w:\w+)', lambda m: f'<{m.group(1)} {NS}', s, 1)
    return parse_xml(s)
def idx(pred, start=0, end=None):
    E = els()
    for i in range(start, len(E) if end is None else end):
        if pred(E[i]): return i
    raise KeyError('not found')
def is_style(el, s):
    v = xp(el, './w:pPr/w:pStyle/@w:val'); return bool(v) and v[0] == s
def h1(text):
    return lambda el: is_style(el, 'Heading1') and txt(el).strip().casefold() == text.casefold()
def starts(text):
    return lambda el: txt(el).strip().startswith(text)
def bm_idx(name):
    i = idx(lambda el: bool(xp(el, f'descendant-or-self::w:bookmarkStart[@w:name="{name}"]')))
    while els()[i].tag != W + 'p' or not txt(els()[i]).strip(): i += 1
    return i

_bid = [max(int(x) for x in xp(body, './/w:bookmarkStart/@w:id')) + 100]
def bid():
    _bid[0] += 1; return _bid[0]

def cut(i, j, topic, source, title, note=''):
    """remove body elements i..j-1 and record their text"""
    E = els()[i:j]
    def desc(e):
        t = txt(e).strip()
        if e.tag == W + 'tbl':
            t = '[Box] ' + ' / '.join(x for x in (''.join(xp(p, './/w:t/text()')).strip() for p in xp(e, './/w:p')) if x)
        for a in xp(e, './/wp:docPr/@descr'):
            t = (f'[Illustration: {a}]' + ('\n\n' + t if t else ''))
        return t
    text = '\n\n'.join(t for t in (desc(e) for e in E) if t)
    if text: UNUSED.append(dict(topic=topic, source=source, title=title, text=text, note=note))
    for e in E: body.remove(e)
    return i

def insert_at(i, elements):
    E = els(); anchor = E[i]
    for e in elements: anchor.addprevious(e)
    return i + len(elements)

# ---------------- inline markdown -> runs ----------------
def rpr(b=False, i=False, color=None, sz=None, u=False, va=None, style=None, font=None):
    s = ''
    if style: s += f'<w:rStyle w:val="{style}"/>'
    if font: s += f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>'
    if b: s += '<w:b/><w:bCs/>'
    if i: s += '<w:i/><w:iCs/>'
    if color: s += f'<w:color w:val="{color}"/>'
    if sz: s += f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
    if u: s += '<w:u w:val="single"/>'
    if va: s += f'<w:vertAlign w:val="{va}"/>'
    return f'<w:rPr>{s}</w:rPr>' if s else ''
def run(t, **k):
    if not t: return ''
    return f'<w:r>{rpr(**k)}<w:t xml:space="preserve">{escape(t)}</w:t></w:r>'
def ilink(anchor, inner): return f'<w:hyperlink w:anchor="{anchor}" w:history="1">{inner}</w:hyperlink>'
def xlink(url, inner):
    rid = d.part.relate_to(url, RT.HYPERLINK, is_external=True)
    return f'<w:hyperlink r:id="{rid}" w:history="1">{inner}</w:hyperlink>'
def ch_anchor(n):
    n = int(n)
    if n <= 7: return f'chapter_{n}'
    if n == 8: return 'chapter_9'
    if n == 9: return 'chapter_10'
    return f'qch_{n}'
TOKEN = re.compile(r'([\^_])([A-Za-z0-9\u0370-\u03ff]+)')
def math_runs(s, base):
    out = ''; pos = 0
    for m in TOKEN.finditer(s):
        out += run(s[pos:m.start()], **base)
        out += run(m.group(2), **dict(base, va='superscript' if m.group(1) == '^' else 'subscript'))
        pos = m.end()
    return out + run(s[pos:], **base)
PLAIN = re.compile(r'(https?://[^\s)]+)|\^(\d+)|\b(Chapters?) (\d+(?:(?:–|, |, and | and | or | through )\d+)*)')
def plain_runs(s, base, links=True):
    out = ''; pos = 0
    if not links: return run(s, **base)
    for m in PLAIN.finditer(s):
        out += run(s[pos:m.start()], **base); pos = m.end()
        if m.group(1):
            url = m.group(1); trail = ''
            while url[-1] in '.,;:': trail = url[-1] + trail; url = url[:-1]
            out += xlink(url, run(url, **dict(base, style='Hyperlink'))) + run(trail, **base)
        elif m.group(2):
            out += ilink(f'qc_note_{m.group(2)}', run(m.group(2), **dict(base, va='superscript', style='Hyperlink')))
        else:
            out += run(m.group(3) + ' ', **base)
            for part in re.split(r'(\d+)', m.group(4)):
                if not part: continue
                if part.isdigit(): out += ilink(ch_anchor(part), run(part, **dict(base, style='Hyperlink')))
                else: out += run(part, **base)
    return out + run(s[pos:], **base)
EMPH = re.compile(r'\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|\*(.+?)\*')
def inline(s, links=True, **base):
    out = ''; pos = 0
    for m in EMPH.finditer(s):
        out += plain_runs(s[pos:m.start()], base, links); pos = m.end()
        if m.group(1): out += inline(m.group(1), links, **dict(base, b=True, i=True))
        elif m.group(2): out += inline(m.group(2), links, **dict(base, b=True))
        else: out += math_runs(m.group(3), dict(base, i=True))
    return out + plain_runs(s[pos:], base, links)

# ---------------- block builders ----------------
def P(runs, jc='both', ppr=''):
    return X(f'<w:p><w:pPr>{ppr}<w:jc w:val="{jc}"/></w:pPr>{runs}</w:p>')
def body_para(s): return P(inline(s))
def empty(): return X('<w:p/>')
def H2(s): return X(f'<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr>{inline(s, links=False)}</w:p>')
def H1_label(text, bookmark=None):
    b1 = b2 = ''
    if bookmark:
        i = bid(); b1 = f'<w:bookmarkStart w:id="{i}" w:name="{bookmark}"/>'; b2 = f'<w:bookmarkEnd w:id="{i}"/>'
    return X(f'<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:pageBreakBefore/><w:spacing w:before="300"/><w:jc w:val="center"/>'
             f'<w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:pPr>{b1}<w:r><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>{b2}</w:p>')
def H1_title(text, bookmark):
    i = bid()
    return X(f'<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:pBdr><w:bottom w:val="single" w:sz="8" w:space="31" w:color="4F81BD"/></w:pBdr>'
             f'<w:spacing w:after="300"/><w:jc w:val="center"/><w:outlineLvl w:val="0"/></w:pPr>'
             f'<w:bookmarkStart w:id="{i}" w:name="{bookmark}"/><w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r><w:bookmarkEnd w:id="{i}"/></w:p>')
def H1_plain(text, bookmark):
    i = bid()
    return X(f'<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:pageBreakBefore/></w:pPr><w:bookmarkStart w:id="{i}" w:name="{bookmark}"/>'
             f'<w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r><w:bookmarkEnd w:id="{i}"/></w:p>')
def question(q):
    return P(run('The question: ', b=True, color='17365D') + inline(q, links=False, i=True, color='17365D'),
             jc='center', ppr='<w:spacing w:before="120" w:after="360"/><w:ind w:left="360" w:right="360"/>')
def caption(s):
    return P(inline(s, links=False, b=True, color='4F81BD', sz=18), jc='center', ppr='<w:spacing w:after="240"/>')
def image(fname, alt):
    from PIL import Image
    path = FIG + fname; w, h = Image.open(path).size
    width_in = 4.6 if w / h > 1.2 else (3.0 if 'vertex' in fname else 4.0)
    if 'vertex' in fname: width_in = 3.0
    height_in = width_in * h / w
    if height_in > 5.4: height_in = 5.4; width_in = height_in * w / h
    inl = d.part.new_pic_inline(path, int(width_in * 914400), int(height_in * 914400))
    inl.docPr.set('descr', alt)
    p = X('<w:p><w:pPr><w:keepNext/><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:noProof/></w:rPr><w:drawing/></w:r></w:p>')
    xp(p, './/w:drawing')[0].append(inl)
    return p
def equation(lines):
    out = []
    cap = None
    m = re.match(r'\*\*Equation \((\d+)\)\.\*\*\s*(.*)$', lines[0])
    if m:
        cap = f'Equation ({m.group(1)}). ' + m.group(2); lines = lines[1:]
        out.append(P(inline(cap, b=True, color='4F81BD', sz=18), jc='center', ppr='<w:keepNext/><w:spacing w:before="120" w:after="60"/>'))
    for k, ln in enumerate(lines):
        last = k == len(lines) - 1
        out.append(P(inline(ln, font='Cambria Math'), jc='center',
                     ppr=('' if last else '<w:keepNext/>') + f'<w:spacing w:after="{200 if last else 40}"/>'))
    return out
def qa_box(title, pairs):
    rows = ''
    for q, a in pairs:
        rows += (f'<w:p><w:pPr><w:keepNext/><w:spacing w:before="80" w:after="40"/></w:pPr>{run("Q.  ", b=True, color="17365D", sz=18)}{inline(q, links=False, b=True, color="17365D", sz=18)}</w:p>'
                 f'<w:p><w:pPr><w:spacing w:after="100"/><w:jc w:val="both"/></w:pPr>{run("A.  ", b=True, color="17365D", sz=18)}{inline(a, links=False, sz=18)}</w:p>')
    bd = ''.join(f'<w:{s} w:val="single" w:sz="12" w:space="0" w:color="17365D"/>' for s in ('top', 'left', 'bottom', 'right'))
    t = (f'<w:tbl><w:tblPr><w:tblW w:w="6600" w:type="dxa"/><w:jc w:val="center"/><w:tblBorders>{bd}</w:tblBorders><w:tblLayout w:type="fixed"/>'
         f'<w:tblCellMar><w:top w:w="100" w:type="dxa"/><w:left w:w="160" w:type="dxa"/><w:bottom w:w="100" w:type="dxa"/><w:right w:w="160" w:type="dxa"/></w:tblCellMar>'
         f'<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr>'
         f'<w:tblGrid><w:gridCol w:w="6600"/></w:tblGrid>'
         f'<w:tr><w:trPr><w:cantSplit/><w:jc w:val="center"/></w:trPr><w:tc><w:tcPr><w:tcW w:w="6600" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="17365D"/></w:tcPr>'
         f'<w:p><w:pPr><w:keepNext/><w:spacing w:after="40"/></w:pPr>{run(title.upper(), b=True, color="FFFFFF", sz=18)}</w:p></w:tc></w:tr>'
         f'<w:tr><w:trPr><w:jc w:val="center"/></w:trPr><w:tc><w:tcPr><w:tcW w:w="6600" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="EAF0F8"/></w:tcPr>{rows}</w:tc></w:tr></w:tbl>')
    return [X(t), empty()]
BOX_LOG = []
def render_md(text, chapter=None):
    out = []
    blocks = [b.strip('\n') for b in re.split(r'\n\s*\n', text) if b.strip()]
    for b in blocks:
        if b.startswith('## '): continue
        if b.startswith('### '): out.append(H2(b[4:].strip())); continue
        if b.startswith('?> '): out.append(question(b[3:].strip())); continue
        if b.startswith(':::qa'):
            L = b.split('\n'); title = L[0][5:].strip(); pairs = []
            for ln in L[1:]:
                if ln.startswith('Q: '): pairs.append([ln[3:], ''])
                elif ln.startswith('A: '): pairs[-1][1] = ln[3:]
            BOX_LOG.append((chapter, title, len(pairs)))
            out += qa_box(title, pairs); continue
        m = re.match(r'^!\[(.*)\]\((.*)\)$', b, re.S)
        if m: out += [image(m.group(2), re.sub(r'[*]', '', m.group(1))), caption(m.group(1))]; continue
        L = b.split('\n')
        if all(l.startswith('>') for l in L):
            out += equation([re.sub(r'^>\s?', '', l).strip() for l in L]); continue
        nm = re.match(r'^\*\*(\d+)\.\*\*\s*(.*)$', b, re.S)
        if nm:
            i = bid()
            out.append(X(f'<w:p><w:pPr><w:jc w:val="both"/></w:pPr><w:bookmarkStart w:id="{i}" w:name="qc_note_{nm.group(1)}"/>'
                         f'{run(nm.group(1) + ".", b=True)}<w:bookmarkEnd w:id="{i}"/>{run(" ")}{inline(nm.group(2).replace(chr(10), " "))}</w:p>'))
            continue
        out.append(body_para(' '.join(l.strip() for l in L)))
    return out

backlink_tpl = copy.deepcopy(els()[idx(lambda el: txt(el).strip() == '↑ Back to Contents')])
def back(): return copy.deepcopy(backlink_tpl)

# =============== 1. Part One edits ===============
# --- Ch7 dedup
s7 = bm_idx('chapter_7')
SRC7 = 'The Quantum World, Chapter 7 "QED — The Strange Theory of Light and Matter"'
i = idx(starts('The classical path wins out for a specific reason'), s7)
j = idx(starts('The paths around the classical one reinforce'), i)
cut(i, j, 'Paths, least time, and stationary action', SRC7 + ', section "Feynman’s sum over possibilities"', 'Classical path, Fermat’s least time, stationary action (duplicated in Part Two, Chapter 21)')
insert_at(i, [body_para('Why the classical path survives all that cancellation, and how Fermat’s least time and the principle of stationary action fall out of it, is worked through properly in Chapter 21.')])
i = idx(starts('Take one specific diagram and translate it into plain English'), s7)
j = idx(starts('There is a stranger way to read these diagrams'), i)
cut(i, j, 'Feynman diagrams', SRC7 + ', section "The little diagram that lied"', 'One diagram translated into plain English; loop corrections (duplicated in Part Two, Chapters 23, 26, 27)')
insert_at(i, [body_para('Chapter 23 slows one of these diagrams down and shows the ordinary Coulomb force coming out of it, and Chapters 26 and 27 follow the loop corrections all the way into renormalization.')])
i = idx(lambda el: is_style(el, 'Heading2') and txt(el).strip() == 'The vacuum is not empty', s7)
k = idx(starts('As Chapter 5 already established'), i)
j = idx(lambda el: is_style(el, 'Heading2') and txt(el).strip().startswith('Why QED is so successful'), k)
cut(k + 1, j, 'Vacuum energy and the Casimir effect', SRC7 + ', section "The vacuum is not empty" and section "What does an electron actually do?"',
    'Casimir paragraph(s) and the internally duplicated section "What does an electron actually do?"')
insert_at(k + 1, [body_para('The Casimir force between two uncharged metal plates measures that structure directly. Chapter 21 returns to it, and Chapter 26 shows the same vacuum screening the electron’s own charge.')])
i = idx(starts('Take one concrete example: an electron interacting with its own electromagnetic field'), s7)
cut(i, i + 1, 'Renormalization', SRC7 + ', section "Renormalization: the horrible calculation that works"', 'Worked example of the self-energy (covered in Part Two, Chapters 26–27)')
i = idx(starts('Reality is more subtle than the first draft of the equations'), s7)
insert_at(i + 1, [body_para('Chapters 26 and 27 take renormalization apart properly and show why it is honest bookkeeping across scales rather than a trick.')])
i = idx(starts('If you want to see how far this picture can be pushed'), s7)
cut(i, i + 2, 'Series and cross-references', SRC7, 'Old pointers to Appendix 4 and to the QED Course as Volume 3')
insert_at(i, [body_para('If you want to see how far this picture can be pushed — electromagnetism itself read outward from the quantum phase of matter, rather than assumed as a starting point — Part Two of this book takes exactly that road, starting with Chapter 10.'),
              body_para('If you would rather calculate than picture it, the *Complete Quantum Electrodynamics Course* (Volume 2) derives this chapter’s results with pencil and paper: the Feynman rules, renormalization, and the electron’s magnetic moment.')])

# --- Ch9 superconducting-circuit pointer
i = idx(starts('A superconducting circuit is a small loop of very cold metal'))
p = els()[i]
for t in xp(p, './/w:t'):
    if t.text and t.text.endswith('knocks the wave apart. The '): t.text = t.text[:-4] + ' '
    if t.text == 'collective-electrodynamics appendix': t.text = 'Part Two of this book'
    if t.text and 'The appendix is the argument' in t.text: t.text = t.text.replace('The appendix is the argument', 'Part Two is the argument')
for h in xp(p, './/w:hyperlink[@w:anchor="chapter_8"]'): h.set(W + 'anchor', 'part_two')

# --- opening questions for Part One
for n in range(1, 10):
    i = bm_idx(ch_anchor(n)); insert_at(i + 1, [question(QA.Q_PART1[n])])

# --- Common questions, end of Part One (before Ch9's back link)
a10 = bm_idx('appendix_1')
i = idx(h1('Appendix 1'))
bl = i - 1
while txt(els()[bl]).strip() != '↑ Back to Contents': bl -= 1
insert_at(bl, qa_box('Common questions about Part One', QA.COMMON1)); BOX_LOG.append((9, 'Common questions about Part One', len(QA.COMMON1)))

# --- Part One page before Chapter 1
def part_page(label, bookmark, name, blurb):
    return [H1_label(label, bookmark),
            P(run(name, b=True, color='4F81BD', sz=40), jc='center', ppr='<w:spacing w:before="600" w:after="600"/>'),
            P(inline(blurb, links=True, i=True), jc='center', ppr='<w:ind w:left="720" w:right="720"/>')]
i = idx(h1('Chapter 1'))
insert_at(i, part_page('Part One', 'part_one', 'The Map',
    'Nine chapters, one survey: what quantum mechanics says, how entanglement and the Bell tests settled the argument, and how quantum fields, the strong force, QED, cryptography, and computing grow out of it.'))

# =============== 2. Part Two ===============
titles = {}
p2 = part_page('Part Two', 'part_two', 'One Road Through It',
    'One question from Chapter 7, followed all the way down: what is the electromagnetic field? From the phase of a single electron to the potential, the photon, renormalization, and a superconducting circuit on a laboratory bench. The pace steps up here, and Chapter 10 hands over the tools.')
for n in range(10, 32):
    t = open(f'{MD}ch{n}.md').read()
    title = re.match(r'## \d+\. (.+)', t).group(1).strip(); titles[n] = title
    p2 += [H1_label(f'Chapter {n}'), empty(), H1_title(title, f'qch_{n}'), empty()]
    p2 += render_md(t, n)
    p2.append(back())
i = idx(h1('Appendix 1'))
insert_at(i, p2)

# =============== 3. Appendices ===============
# App1: Part Two section, sixth thing, punchline
i = idx(lambda el: is_style(el, 'Heading2') and txt(el).strip().startswith('The ideas that did not make it'))
insert_at(i, [H2('One road through electromagnetism')] + [body_para(x) for x in [
    'Part Two took one question and refused to let go of it: what is the electromagnetic field?',
    'The answer ran backward through the usual teaching order. Quantum phase came first. The potential tells a charged particle how to compare its phase from one point to the next. The fields are what you build from the potential, and Maxwell’s equations follow.',
    'In a superconductor, an enormous number of electrons share one phase, and quantum mechanics becomes something you can read on a voltmeter and build into a circuit.',
    'QED stayed in charge of photons, particle creation, and precision. Renormalization turned out to be honest bookkeeping across scales, not a trick.',
    'Whether the field is a thing in its own right was left exactly as open as the evidence leaves it: real in every way an experiment can reach, and not proven to be a substance.']])
i = idx(lambda el: is_style(el, 'Heading2') and txt(el).strip() == 'Five things worth remembering')
for t in xp(els()[i], './/w:t'):
    t.text = t.text.replace('Five things', 'Six things')
i = idx(starts('Every successful theory has opened another question'), i)
tpl_num = copy.deepcopy(els()[i - 1]); tpl_txt = copy.deepcopy(els()[i])
def retext(p, s):
    ts = xp(p, './/w:t'); ts[0].text = s
    for t in ts[1:]: t.text = ''
    return p
insert_at(i + 1, [retext(tpl_num, '6. Electromagnetism can be read from the phase outward.'),
                  retext(tpl_txt, 'The potential steers the quantum phase of charged matter; the fields, and Maxwell’s equations, grow out of it.')])
i = idx(starts('Nature does not commit to a definite answer until something forces the question'))
for t in xp(els()[i], './/w:t'):
    if 'Standard Model that is spectacularly successful but incomplete.' in t.text:
        t.text = t.text.replace('Standard Model that is spectacularly successful but incomplete.',
            'Standard Model that is spectacularly successful but incomplete. Follow light all the way down and it starts with phase: the potential steers the phase of charged matter, the fields and Maxwell’s equations grow out of that, and in a superconducting wire the same phase becomes something you can measure with a voltmeter.')
        break
else: raise SystemExit('punchline not found')

# App2: replace image + dialogue with narrator Q&A
a2 = bm_idx('appendix_2')
j = idx(h1('Appendix 3'), a2)
blk = j - 1
while txt(els()[blk]).strip() != '↑ Back to Contents': blk -= 1
cut(a2 + 1, blk, 'The Alice and Bob coda', 'The Quantum World, Appendix 2 "What We Actually Learned"',
    'Illustration of Alice and Bob with speech bubbles, its three caption lines, and the dialogue "A last argument in two voices"',
    note='The illustration itself (Alice and Bob with speech bubbles) is preserved in the old Quantum World docx in the backup folder.')
insert_at(a2 + 1, [empty(), body_para('Two questions have run underneath every chapter: does the universe make sense, and does the experiment agree? Good physics needs both. Here they are, asked one last time and answered plainly.')]
          + qa_box('A last round of questions', QA.APP2))
BOX_LOG.append(('App2', 'A last round of questions', len(QA.APP2)))

# App4: remove whole appendix (label H1 .. before Epilogue label)
i = idx(h1('Appendix 4')); j = idx(h1('Epilogue'), i)
cut(i, j, 'Collective electrodynamics (QW overview)', 'The Quantum World, Appendix 4 "Collective Electrodynamics: An Alternative Foundation for Electromagnetism"',
    'The whole appendix, replaced by Part Two (its figures and boxes are preserved in the old Quantum World docx in the backup folder)')

# =============== 4. Back matter ===============
# Glossary merge
g0 = bm_idx('glossary'); g1 = idx(h1('Translate this to your field'), g0)
qw_entries = {}
for k in range(g0 + 1, g1):
    t = txt(els()[k]).strip()
    m = re.match(r'(.+?)\s+—', t)
    if m: qw_entries[m.group(1).strip().lower()] = els()[k]
gq = open(BACK + 'glossary_qc.md').read()
qc_items = re.findall(r'^\*\*(.+?)\.\*\*\s*(.+)$', gq, re.M)
UNUSED.append(dict(topic='Back matter of The Quantum Conversation', source='The Quantum Conversation, Appendix C "Glossary" (introduction only)', title='Glossary introduction (the entries themselves were merged into the Glossary)', text=gq.split('\n\n')[1], note=''))
added = merged = 0
tpl = None
for term, defin in qc_items:
    key = term.lower()
    if key in qw_entries:
        p = qw_entries[key]
        frag = X(f'<w:p>{run(" In Part Two: ", i=True)}{inline(defin)}</w:p>')
        for r in list(frag): 
            if r.tag != W + 'pPr': p.append(r)
        merged += 1; continue
    # new entry: insert alphabetically
    newp = X(f'<w:p><w:pPr><w:jc w:val="both"/></w:pPr>{run(term, b=True, color="4F81BD")}{run(" — ")}{inline(defin)}</w:p>')
    E = els(); g0 = bm_idx('glossary'); g1 = idx(h1('Translate this to your field'), g0)
    pos = g1
    for k in range(g0 + 1, g1):
        t = txt(E[k]).strip()
        if '—' in t and t.split('—')[0].strip().lower() > key: pos = k; break
    E[pos].addprevious(newp); added += 1
i = idx(starts('Collective electrodynamics —'))
els()[i].append(xp(X(f'<w:p>{run(" Part Two of this book (Chapters 10–31) follows this perspective in detail.")}</w:p>'), './w:r')[0])

# Equations of Part Two + symbols, at the end of "The equations, decoded"
fr = idx(h1('Further reading'))
eqA = open(BACK + 'equations_part2.md').read().split('\n', 1)[1]
symE = open(BACK + 'symbols.md').read().split('\n', 1)[1]
notes = open(BACK + 'notes_sources.md').read().split('\n', 1)[1]
blk = [H2('The twelve equations of Part Two')] + render_md(eqA) + [H2('Symbols, numbers, and distinctions')] + render_md(symE)
blk += [back(), H1_plain('Notes on Sources', 'notes_sources')] + render_md(notes) + [back()]
# put before the back-link that closes the equations section (if any) else before Further reading
k = fr - 1
while k > fr - 6 and txt(els()[k]).strip() != '↑ Back to Contents': k -= 1
if txt(els()[k]).strip() == '↑ Back to Contents':
    insert_at(k, blk[:-3 - len(render_md(notes))] if False else blk[:blk.index(blk[-1])] if False else [])
    # place equations before that existing back link, notes after it
    n_notes = len(render_md(notes)) + 3
    insert_at(k, blk[:-n_notes + 1])  # equations + symbols (without our back link)
    k2 = idx(h1('Further reading'))
    insert_at(k2, blk[-n_notes + 1:])
else:
    insert_at(fr, blk)

# Further reading Mead line
i = idx(starts('Collective Electrodynamics: Quantum Foundations of Electromagnetism, by Carver Mead'))
for t in xp(els()[i], './/w:t'):
    if 'Appendix 4’s minority research program' in t.text:
        t.text = t.text.replace('behind Appendix 4’s minority research program', 'behind Part Two of this book'); break
else: raise SystemExit('Mead further reading not found')

# Closing blurb: add Part Two sentence
i = idx(starts('An electron does not know which slit it went through'))
insert_at(i + 1, [empty(), body_para('Part Two then takes one road through that map, all the way down: what the electromagnetic field really is, read outward from the quantum phase of an electron to the photon, renormalization, and a superconducting circuit you could build on a bench.')])

# Also by: Quanta group
i = idx(lambda el: txt(el).strip() == 'Quanta, Actually, Volume 2: The Quantum Conversation')
cut(i, i + 1, 'Series and cross-references', 'The Quantum World, "Also by" page', 'Old Quanta, Actually entries')
for t in xp(els()[i], './/w:t'):
    t.text = t.text.replace('Volume 3: Complete Quantum Electrodynamics Course', 'Volume 2: Complete Quantum Electrodynamics Course')
assert txt(els()[i]).strip() == 'Quanta, Actually, Volume 2: Complete Quantum Electrodynamics Course', txt(els()[i])
i = idx(starts('The Quantum Conversation (Volume 2) — if this book'))
cut(i, i + 1, 'Series and cross-references', 'The Quantum World, "Where this series goes next"', 'Old series pointer')
insert_at(i, [body_para('*Complete Quantum Electrodynamics Course* (Volume 2) — if Part Two left you wanting to calculate rather than picture, Volume 2 does the full calculation: from complex numbers and the Dirac equation to Feynman rules, renormalization, the electron’s anomalous magnetic moment, and the Lamb shift.')])

# =============== 5. Front matter ===============
i = idx(starts('Volume 2 — The Quantum Conversation'))
cut(i, i + 2, 'Series and cross-references', 'The Quantum World, "Also in This Series"', 'Old Volume 2 and Volume 3 entries')
insert_at(i, [body_para('Volume 2 — *Complete Quantum Electrodynamics Course: From Mathematical Foundations to One-Loop QED*. The calculation course: from complex numbers and the Dirac equation to Feynman rules, renormalization, the electron’s anomalous magnetic moment, and the Lamb shift, derived step by step.')])
i = idx(starts('Volume 1 — The Quantum World'))
for t in xp(els()[i], './/w:t'):
    if 'This book: the survey' in t.text:
        t.text = t.text.replace('This book: the survey, from the break with classical physics to quantum fields, QED, cryptography, and computing.',
            'This book: in Part One, the survey, from the break with classical physics to quantum fields, QED, cryptography, and computing; in Part Two, one road through it, electromagnetism read outward from quantum phase and the potential.')
assert 'Part Two, one road' in txt(els()[i]), txt(els()[i])
i = idx(starts('Near the back, Quantum'))
insert_at(i + 1, [empty(), body_para('The book comes in two Parts. Part One, The Map, is the survey. Part Two, One Road Through It, follows a single question, what the electromagnetic field really is, from the phase of one electron to a superconducting circuit. Part Two is a step up in density, and Chapter 10 is the bridge: it hands over the small toolkit the rest of Part Two needs.'),
                  empty(), body_para('Every chapter opens with the question it answers, and “Questions This Book Answers,” just after the contents, lists them all. Boxes headed QUESTION AND ANSWER take an objection a careful reader would raise and answer it directly, and each Part ends with a box of common questions.')])
i = idx(lambda el: is_style(el, 'Heading2') and txt(el).strip() == '5. Turn weirdness into information')
i = idx(starts('Entanglement becomes a resource'), i)
h2tpl = copy.deepcopy(els()[i - 1]); ntpl = copy.deepcopy(els()[i])
insert_at(i + 1, [retext(h2tpl, '6. Take one road through it'),
                  retext(ntpl, 'Part Two follows one question, what the electromagnetic field is, from an electron’s phase to a superconducting circuit.')])
i = idx(starts('6. Name the collision'))
ts = xp(els()[i], './/w:t')
assert ts[0].text.startswith('6'), ts[0].text
ts[0].text = '7' + ts[0].text[1:]
i = idx(starts('The Alice and Bob dialogue in Appendix 2 is explicitly fictional'))
cut(i, i + 1, 'The Alice and Bob coda', 'The Quantum World, front matter "About this book"', 'Line about the fictional dialogue')
insert_at(i, [body_para('Appendix 2 closes the book with a last round of questions, asked and answered plainly.')])

# TOC rebuild
c0 = bm_idx('contents'); c1 = idx(h1('Also in This Series'), c0)
E = els(); entries = [k for k in range(c0 + 1, c1) if xp(E[k], './/w:hyperlink/@w:anchor')]
tpl = copy.deepcopy(E[entries[0]])
first = entries[0]
for k in reversed(entries): body.remove(els()[k])
def toc_entry(text, anchor, bold=False, indent=False):
    p = copy.deepcopy(tpl)
    xp(p, './/w:hyperlink')[0].set(W + 'anchor', anchor)
    ts = xp(p, './/w:t'); ts[0].text = text
    for t in ts[1:]: t.text = ''
    if bold:
        for r in xp(p, './/w:r/w:rPr'): r.insert(0, X('<w:b/>'))
    return p
L = [toc_entry('Questions This Book Answers', 'questions_page'), toc_entry('Prologue', 'prologue'), toc_entry('Part One — The Map', 'part_one', True)]
for n in range(1, 10): L.append(toc_entry(f'Chapter {n} — ' + txt(els()[bm_idx(ch_anchor(n))]).strip(), ch_anchor(n)))
L.append(toc_entry('Part Two — One Road Through It', 'part_two', True))
for n in range(10, 32): L.append(toc_entry(f'Chapter {n} — {titles[n]}', f'qch_{n}'))
for a, lab in [('appendix_1', 'Appendix 1'), ('appendix_2', 'Appendix 2'), ('appendix_3', 'Appendix 3')]:
    L.append(toc_entry(f'{lab} — ' + txt(els()[bm_idx(a)]).strip(), a))
L.append(toc_entry('Epilogue — ' + txt(els()[bm_idx('epilogue')]).strip(), 'epilogue'))
for a, lab in [('glossary', 'Glossary'), ('translate_field', 'Translate This to Your Field'), ('party_cheatsheet', 'Quantum Mechanics at a Party: A Myth-Busting Cheat Sheet'),
               ('math_appendix', 'The Equations, Decoded'), ('notes_sources', 'Notes on Sources'), ('further_reading', 'Further Reading'), ('bibliography', 'Bibliography'), ('about_author', 'About the Author')]:
    L.append(toc_entry(lab, a))
insert_at(first, L)

# Questions page before "Also in This Series"
i = idx(h1('Also in This Series'))
Q = [H1_plain('Questions This Book Answers', 'questions_page'),
     body_para('Every chapter opens with the question it answers. Here they all are, in order; each chapter number links to its chapter.')]
def qline(n, q):
    return P(ilink(ch_anchor(n), run(f'Chapter {n}', style='Hyperlink', b=True)) + run('  ') + inline(q, links=False, i=True), jc='left', ppr='<w:spacing w:after="100"/>')
Q.append(P(run('Part One — The Map', b=True, color='17365D'), jc='left', ppr='<w:spacing w:before="200" w:after="100"/>'))
Q += [qline(n, QA.Q_PART1[n]) for n in range(1, 10)]
Q.append(P(run('Part Two — One Road Through It', b=True, color='17365D'), jc='left', ppr='<w:spacing w:before="200" w:after="100"/>'))
Q += [qline(n, QA.Q_PART2[n]) for n in range(10, 32)]
insert_at(i, Q)
# make sure "Also in This Series" still starts a new page
hdr = els()[idx(h1('Also in This Series'))]
if not xp(hdr, './w:pPr/w:pageBreakBefore'):
    xp(hdr, './w:pPr')[0].insert(1, X('<w:pageBreakBefore/>'))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
d.save(OUT)
json.dump(UNUSED, open(os.path.join(os.path.dirname(OUT) or '.', 'unused_qw.json'), 'w'), indent=1, ensure_ascii=False)

print('saved', OUT, 'boxes', len(BOX_LOG), 'gloss added', added, 'merged', merged)
