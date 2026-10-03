# -*- coding: utf-8 -*-
"""Build the four "Math, Actually" volume masters from the former
"The Mathematics Tower" sources.

    python build_math_actually.py SRC_DIR OUT_DIR

SRC_DIR holds the four source masters ("The Mathematics Tower - Volume N.docx").
OUT_DIR receives "Math, Actually - Volume N.docx".  Needs Python 3.8+ and lxml.

What it does (all generated, so it survives rebuilds):
  * series line, title page, copyright line, docx properties
  * floors -> chapters, rooms -> sections, Tower -> series, in every paragraph
  * every mention of another section becomes an internal hyperlink to that
    section's bookmark, named by its topic; sections in another volume are
    written as plain "Topic (Volume N)"; chapters likewise
  * chapter openings in the Physics, Actually layout (series line, "Chapter N",
    chapter title), section headings "Section N.M: Title"
  * new front matter / epilogue / closing note (text in ma_text.py)
  * a hyperlinked Contents page in the Physics, Actually style
  * heading styles copied from Physics, Actually
"""
import copy, json, os, re, sys, zipfile
from lxml import etree
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docxtext import W, q, flatten, apply_edits, rebuild, text_of, link_look, XMLSPACE
from rules import vocab_edits
import ma_text as T

NS = {'w': W}
SERIES = 'Math, Actually'
VOLS = T.VOLUMES          # {1: {'subtitle':..., 'chapters':(1,12)}, ...}
STATS = {}

# ---------------------------------------------------------------- index
def style_of(p):
    s = p.find('w:pPr/w:pStyle', NS)
    return s.get(q('val')) if s is not None else ''

def ptext(p):
    return ''.join(t.text or '' for t in p.iter(q('t')))

def build_index(src_docs):
    rooms, chaps = {}, {}
    for v, root in src_docs.items():
        for p in root.iter(q('p')):
            st = style_of(p); t = ptext(p).strip()
            if st == 'Heading2':
                m = re.match(r'Room (\d+)\.(\d+): (.*)', t)
                if m: rooms[f'{m[1]}.{m[2]}'] = {'vol': v, 'title': re.sub(r'\bThe Tower\b', 'The Series', m[3]), 'ch': int(m[1])}
            elif st == 'Heading1':
                m = re.match(r'Floor (\d+): (.*)', t)
                if m: chaps[int(m[1])] = {'vol': v, 'title': T.CHAPTER_TITLE_FIX.get(int(m[1]), m[2])}
    GEN = ('Looking Ahead', 'Looking Back', 'Applications', 'Case Studies')
    def topic(k, t):
        if k in T.TOPIC_OVERRIDE: return T.TOPIC_OVERRIDE[k]
        a = t.split(':')[0].strip() if ':' in t else t
        if a.startswith(GEN): a = t
        return re.sub(r'\s*\([^)]*\)\s*$', '', a)
    for k, r in rooms.items(): r['topic'] = topic(k, r['title'])
    seen = {}
    for k, r in rooms.items(): seen.setdefault(r['topic'], []).append(k)
    for tp, ks in seen.items():
        if len(ks) > 1:
            for k in ks: rooms[k]['topic'] = f"{tp} (Chapter {rooms[k]['ch']})"
    return rooms, chaps

def sec_bm(k): return 'sec_' + k.replace('.', '_')
def ch_bm(n): return f'ch_{n}'

# ---------------------------------------------------------------- references
R_RANGE = re.compile(r'\bRooms (\d+\.\d+)(\s*(?:–|-|—|through|to)\s*)(\d+\.\d+|\d+)\b')
R_LIST = re.compile(r'\bRooms? (\d+\.\d+)((?:,\s*\d+\.\d+)*)(,?\s+(?:and|or)\s+)(?:Room\s+)?(\d+\.\d+)\b')
R_ONE = re.compile(r'\b[Rr]oom (\d+\.\d+)\b')
R_PL = re.compile(r'\bRooms (\d+\.\d+)\b')
F_RANGE = re.compile(r'\bFloors (\d+)(\s*(?:–|-|—|through|to)\s*)(\d+)\b')
F_LIST = re.compile(r'\bFloors (\d+)((?:,\s*\d+)*)(,?\s+(?:and|or)\s+)(\d+)\b')
F_ONE = re.compile(r'\b[Ff]loor (\d+)\b')

class Ctx:
    def __init__(self, vol, rooms, chaps):
        self.vol, self.rooms, self.chaps = vol, rooms, chaps

def vol_note(ctx, v, text, s, e):
    """'(Volume N)' unless the sentence already names that volume nearby."""
    win = text[max(0, s - 60): e + 40]
    if f'Volume {v}' in win: return ''
    return f' (Volume {v})'

def sec_piece(ctx, k, mode, text, s, e, numeric=False):
    r = ctx.rooms.get(k)
    if r is None:
        return [(f'Section {k}', ('plain',))]
    label = f'Section {k}' if (numeric or mode in ('ref', 'heading')) else r['topic']
    if r['vol'] == ctx.vol and mode != 'heading':
        STATS['links'] = STATS.get('links', 0) + 1
        return [(label, ('link', sec_bm(k), None))]
    if r['vol'] != ctx.vol:
        STATS['plain_xvol'] = STATS.get('plain_xvol', 0) + 1
        return [(label + vol_note(ctx, r['vol'], text, s, e), ('plain',))]
    return [(label, ('plain',))]

def ch_piece(ctx, n, mode, text, s, e, word='Chapter'):
    c = ctx.chaps.get(n)
    label = f'{word} {n}'
    if c is None: return [(label, ('plain',))]
    if c['vol'] == ctx.vol and mode not in ('heading', 'label'):
        STATS['ch_links'] = STATS.get('ch_links', 0) + 1
        return [(label, ('link', ch_bm(n), None))]
    if c['vol'] != ctx.vol and mode != 'heading':
        STATS['ch_plain_xvol'] = STATS.get('ch_plain_xvol', 0) + 1
        return [(label + vol_note(ctx, c['vol'], text, s, e), ('plain',))]
    return [(label, ('plain',))]

def ref_edits(ctx, text, mode):
    edits = []; taken = []
    def free(s, e): return all(not (s < b and a < e) for a, b in taken)
    def add(s, e, pieces):
        edits.append((s, e, pieces)); taken.append((s, e))
    for m in R_RANGE.finditer(text):
        a, sep, b = m.group(1), m.group(2), m.group(3)
        if '.' not in b: b = a.split('.')[0] + '.' + b
        pieces = [('Sections ', ('plain',))]
        pieces += sec_piece(ctx, a, mode, text, m.start(), m.end(), numeric=True)
        pieces += [(sep.replace('-', '–'), ('plain',))]
        pieces += sec_piece(ctx, b, mode, text, m.start(), m.end(), numeric=True)
        # range: volume note only once, at the end
        pieces = [(t.replace(f" (Volume {ctx.rooms.get(a,{}).get('vol')})", '') if i < len(pieces) - 1 else t, md) for i, (t, md) in enumerate(pieces)]
        add(m.start(), m.end(), _strip_label(pieces))
    for m in R_LIST.finditer(text):
        if not free(m.start(), m.end()): continue
        keys = [m.group(1)] + re.findall(r'\d+\.\d+', m.group(2)) + [m.group(4)]
        pieces = []
        for i, k in enumerate(keys):
            if i: pieces.append((', ' if i < len(keys) - 1 else m.group(3), ('plain',)))
            pieces += sec_piece(ctx, k, mode, text, m.start(), m.end())
        add(m.start(), m.end(), pieces)
    for m in R_ONE.finditer(text):
        if not free(m.start(), m.end()): continue
        poss = text[m.end():m.end() + 2] in ('’s', "'s")   # possessive reads better numbered
        add(m.start(), m.end(), sec_piece(ctx, m.group(1), mode, text, m.start(), m.end(), numeric=poss))
    for m in R_PL.finditer(text):
        if not free(m.start(), m.end()): continue
        add(m.start(), m.end(), _strip_label([('Sections ', ('plain',))] + sec_piece(ctx, m.group(1), mode, text, m.start(), m.end(), numeric=True)))
    for m in F_RANGE.finditer(text):
        if not free(m.start(), m.end()): continue
        a, b = int(m.group(1)), int(m.group(3))
        va, vb = ctx.chaps.get(a, {}).get('vol'), ctx.chaps.get(b, {}).get('vol')
        t = f'Chapters {a}{m.group(2).replace("-", "–")}{b}'
        if va == vb and va != ctx.vol and mode != 'heading':
            t += vol_note(ctx, va, text, m.start(), m.end())
        add(m.start(), m.end(), [(t, ('plain',))])
    for m in F_LIST.finditer(text):
        if not free(m.start(), m.end()): continue
        nums = [int(m.group(1))] + [int(x) for x in re.findall(r'\d+', m.group(2))] + [int(m.group(4))]
        pieces = [('Chapters ', ('plain',))]
        for i, n in enumerate(nums):
            if i: pieces.append((', ' if i < len(nums) - 1 else m.group(3), ('plain',)))
            pieces += [(p[0].replace('Chapter ', '', 1), p[1]) for p in ch_piece(ctx, n, mode, text, m.start(), m.end())]
        vols = {ctx.chaps.get(n, {}).get('vol') for n in nums}
        if len(vols) == 1:
            v = vols.pop(); note = f' (Volume {v})'
            if any(t.endswith(note) for t, _ in pieces):
                pieces = [(t[:-len(note)] if t.endswith(note) else t, md) for t, md in pieces]
                pieces[-1] = (pieces[-1][0] + note, pieces[-1][1])
        add(m.start(), m.end(), pieces)
    for m in F_ONE.finditer(text):
        if not free(m.start(), m.end()): continue
        add(m.start(), m.end(), ch_piece(ctx, int(m.group(1)), mode, text, m.start(), m.end()))
    return edits, taken

def _strip_label(pieces):
    out = []
    for t, md in pieces:
        if t.startswith('Section ') and out and out[-1][0] in ('Sections ',):
            t = t[len('Section '):]
        elif t.startswith('Section ') and out and re.search(r'(–|through|to)\s*$', out[-1][0]):
            t = t[len('Section '):]
        out.append((t, md))
    return out

def lit_rules(vol):
    pairs = T.literal_fixes(vol)
    def f(text):
        out = []
        for old, new in pairs:
            i = text.find(old)
            while i >= 0:
                out.append((i, i + len(old), new)); i = text.find(old, i + len(old))
        return out
    return f

def edit_paragraph(ctx, p, mode, extra_rules=None):
    atoms = flatten(p)
    if atoms is None:
        STATS.setdefault('skipped_paras', []).append(ptext(p)[:80]); return False
    text = text_of(atoms)
    if not text: return False
    edits, taken = ref_edits(ctx, text, mode)
    for s, e, r in (extra_rules(text) if extra_rules else []):
        if all(not (s < b and a < e) for a, b in taken):
            edits.append((s, e, [(r, None)])); taken.append((s, e))
    for s, e, r in vocab_edits(text):
        if all(not (s < b and a < e) for a, b in taken):
            edits.append((s, e, [(r, None)])); taken.append((s, e))
    if not edits: return False
    # existing hyperlinks to rooms/floors that we did not rewrite: re-point anchors
    atoms = apply_edits(atoms, edits)
    rebuild(p, atoms)
    return True

# ---------------------------------------------------------------- paragraph factory
def mk_p(text, style=None, ppr_extra=None, rpr=None, bookmark=None, bm_id=None, page_break=False, jc=None):
    p = etree.Element(q('p'))
    ppr = etree.SubElement(p, q('pPr'))
    if style:
        s = etree.SubElement(ppr, q('pStyle')); s.set(q('val'), style)
    if page_break:
        etree.SubElement(ppr, q('pageBreakBefore'))
    if ppr_extra is not None:
        for el in ppr_extra: ppr.append(copy.deepcopy(el))
    if jc:
        j = etree.SubElement(ppr, q('jc')); j.set(q('val'), jc)
    if bookmark:
        b = etree.SubElement(p, q('bookmarkStart')); b.set(q('id'), str(bm_id)); b.set(q('name'), bookmark)
        e = etree.SubElement(p, q('bookmarkEnd')); e.set(q('id'), str(bm_id))
    if text:
        add_runs(p, text, rpr)
    return p

def add_runs(p, text, rpr=None):
    """text may contain *italic* spans."""
    parts = re.split(r'(\*[^*]+\*)', text)
    for part in parts:
        if not part: continue
        r = etree.SubElement(p, q('r'))
        rp = copy.deepcopy(rpr) if rpr is not None else None
        if part.startswith('*') and part.endswith('*'):
            part = part[1:-1]
            if rp is None: rp = etree.Element(q('rPr'))
            rp.insert(0, etree.Element(q('i')))
        if rp is not None and len(rp): r.append(rp)
        t = etree.SubElement(r, q('t')); t.set(XMLSPACE, 'preserve'); t.text = part
    return p

def rpr_of(**kw):
    r = etree.Element(q('rPr'))
    if kw.get('font'):
        f = etree.SubElement(r, q('rFonts'));
        for a in ('ascii', 'hAnsi', 'cs', 'eastAsia'): f.set(q(a), kw['font'])
    if kw.get('b'): etree.SubElement(r, q('b'))
    if kw.get('i'): etree.SubElement(r, q('i'))
    if kw.get('color'):
        c = etree.SubElement(r, q('color')); c.set(q('val'), kw['color'])
    if kw.get('sz'):
        s = etree.SubElement(r, q('sz')); s.set(q('val'), str(kw['sz']))
        s = etree.SubElement(r, q('szCs')); s.set(q('val'), str(kw['sz']))
    if kw.get('u'):
        u = etree.SubElement(r, q('u')); u.set(q('val'), 'single')
    return r

class BM:
    def __init__(self, root):
        ids = [int(b.get(q('id'))) for b in root.iter(q('bookmarkStart')) if (b.get(q('id')) or '').isdigit()]
        self.n = max(ids + [0]) + 1
    def next(self):
        self.n += 1; return self.n

# ---------------------------------------------------------------- volume transform
def transform(vol, root, rooms, chaps):
    ctx = Ctx(vol, rooms, chaps)
    body = root.find(q('body'))
    bm = BM(root)
    kids = list(body)
    # locate structure
    def h1_index(pred):
        for i, el in enumerate(body):
            if etree.QName(el).localname == 'p' and style_of(el) == 'Heading1' and pred(ptext(el).strip()):
                return i
        return None
    body_tpl = None
    for el in body:
        if etree.QName(el).localname == 'p' and not style_of(el) and len(ptext(el)) > 200 and el.find('w:pPr/w:shd', NS) is None:
            body_tpl = el; break
    tpl_ppr = copy.deepcopy(body_tpl.find(q('pPr')))
    # the first long unstyled paragraph is the (centred) copyright text; new prose is justified body text
    for j in tpl_ppr.findall(q('jc')): tpl_ppr.remove(j)
    etree.SubElement(tpl_ppr, q('jc')).set(q('val'), 'both')
    def body_p(text):
        p = etree.Element(q('p')); p.append(copy.deepcopy(tpl_ppr)); add_runs(p, text); return p

    def render(items):
        fm = []
        for kind, text in items:
            if kind == 'h1': fm.append(mk_p(text, 'Heading1', page_break=True, bookmark='fm_' + re.sub(r'\W+', '_', text.lower())[:30], bm_id=bm.next()))
            elif kind == 'h2': fm.append(mk_p(text, 'Heading2'))
            elif kind == 'p': fm.append(body_p(text))
        return fm
    # 1. rename bookmarks room_X_Y -> sec_X_Y, floor_N -> ch_N; re-point anchors
    ren = {}
    for b in root.iter(q('bookmarkStart')):
        n = b.get(q('name'))
        m = re.match(r'room_(\d+)_(\d+)(_tables)?$', n)
        if m: ren[n] = f'sec_{m[1]}_{m[2]}' + (m[3] or '')
        m = re.match(r'floor_(\d+)$', n)
        if m: ren[n] = f'ch_{m[1]}'
    for b in root.iter(q('bookmarkStart')):
        if b.get(q('name')) in ren: b.set(q('name'), ren[b.get(q('name'))])
    for h in root.iter(q('hyperlink')):
        a = h.get(q('anchor'))
        if a in ren: h.set(q('anchor'), ren[a])
    # make sure every same-volume section/chapter has a bookmark on its heading
    have = set(b.get(q('name')) for b in root.iter(q('bookmarkStart')))

    # 2. find sections of the document
    toc_sdt = next((el for el in body if etree.QName(el).localname == 'sdt'), None)
    i_front_first = h1_index(lambda t: t in ('Preface', 'About This Volume'))
    i_dir = h1_index(lambda t: t == 'This Volume’s Directory')
    i_first_ch = h1_index(lambda t: t.startswith('Floor '))
    i_epi = h1_index(lambda t: t.startswith('Epilogue'))
    i_ans = h1_index(lambda t: t == 'Answer Key')
    i_gloss = h1_index(lambda t: t.startswith('Symbol'))
    i_also = h1_index(lambda t: t == 'Also in This Series')
    kids = list(body)
    i_how = h1_index(lambda t: t == 'How to Use This Book')
    i_fr = h1_index(lambda t: t == 'On Floors and Rooms')
    i_base = h1_index(lambda t: t == 'On the Basement')
    pref_old = kids[i_front_first:i_how]
    fr_old = kids[i_fr:i_base]
    base_old = kids[i_base:i_dir]
    front_old = pref_old + fr_old + base_old
    dir_old = []
    epi_old = kids[i_epi:i_ans]
    also_old = [el for el in kids[i_also:] if etree.QName(el).localname != 'sectPr']
    title_old = kids[:kids.index(toc_sdt) - 1]      # before "Table of Contents" H1
    toc_h1 = kids[kids.index(toc_sdt) - 1]
    gloss_and_after = set(id(el) for el in kids[i_gloss:])
    ans_to_gloss = set(id(el) for el in kids[i_ans:i_gloss])
    STATS['removed_blocks'] = {'front': [ptext(e)[:60] for e in front_old if style_of(e).startswith('Heading')],
                               'directory_paras': len(dir_old), 'epilogue_paras': len(epi_old), 'also_paras': len(also_old)}

    # 3. edit every remaining paragraph's text (refs + vocabulary)
    keep_out = set(id(e) for e in front_old + dir_old + epi_old + also_old + title_old + [toc_h1, toc_sdt])
    n_changed = 0
    for el in list(body):
        if id(el) in keep_out: continue
        for p in ([el] if etree.QName(el).localname == 'p' else list(el.iter(q('p')))):
            st = style_of(p)
            t = ptext(p).strip()
            if st.startswith('Heading'):
                mode = 'heading'
            elif id(el) in gloss_and_after:
                mode = 'ref'
            elif re.match(r'Floor \d+: ', t) and len(t) < 90:
                mode = 'label'
            else:
                mode = 'body'
            if st == 'Heading2' and re.match(r'Room \d+\.\d+: ', t):
                if edit_paragraph(ctx, p, 'heading', extra_rules=lambda s, _l=lit_rules(vol): [(0, 4, 'Section')] + _l(s)): n_changed += 1
                continue
            if edit_paragraph(ctx, p, mode, extra_rules=lit_rules(vol)): n_changed += 1
    STATS['paragraphs_changed'] = n_changed

    # 4. chapter openings, Physics, Actually layout
    for el in list(body):
        if etree.QName(el).localname != 'p' or style_of(el) != 'Heading1': continue
        m = re.match(r'(?:Floor|Chapter) (\d+): (.*)', ptext(el).strip())
        if not m: continue
        n = int(m.group(1)); title = chaps[n]['title']
        bms = [b for b in el if etree.QName(b).localname in ('bookmarkStart', 'bookmarkEnd')]
        series = mk_p(SERIES, style='Title', page_break=True)
        # bookmarks: ch_N on series line (as Physics puts chN on its series line)
        for b in bms:
            el.remove(b)
        idx = list(body).index(el)
        chap_no = mk_p(f'Chapter {n}', style='Heading1')
        chap_title = mk_p(title, style='Heading1')
        # put all bookmarks (ch_N and _Toc) on the series line
        ppr_end = 1
        for b in bms:
            series.insert(ppr_end, b); ppr_end += 1
        body.remove(el)
        body.insert(idx, chap_title); body.insert(idx, chap_no); body.insert(idx, series)
        if ch_bm(n) not in have:
            b1 = etree.Element(q('bookmarkStart')); i_ = bm.next(); b1.set(q('id'), str(i_)); b1.set(q('name'), ch_bm(n))
            b2 = etree.Element(q('bookmarkEnd')); b2.set(q('id'), str(i_))
            series.insert(1, b2); series.insert(1, b1)
    # section headings: drop the old Heading2 direct spacing so the style rules
    for p in body.iter(q('p')):
        if style_of(p) == 'Heading2' and ptext(p).startswith('Section '):
            ppr = p.find(q('pPr'))
            for x in ppr.findall(q('spacing')): ppr.remove(x)

    # 5. title page + copyright (Physics, Actually layout)
    v = VOLS[vol]
    new_title = [
        mk_p('', None),
        mk_p(SERIES, 'Title'),
        mk_p(f'Volume {vol} - {v["subtitle"]}', 'Heading1'),
        mk_p(f'A Volume in the {SERIES} Series', None, rpr=rpr_of(b=True, color='4F81BD', sz=26), jc='center'),
        mk_p('', None),
        mk_p(T.AUTHOR, None, rpr=rpr_of(b=True, color='4F81BD', sz=26), jc='center'),
    ]
    first = title_old[0]
    pos = list(body).index(first)
    # keep copyright paragraphs (index 5..8 in source) but rename the series line
    copyright_paras = [e for e in title_old if re.search(r'Copyright|All rights reserved|First edition|checked with care', ptext(e))]
    for e in copyright_paras:
        edit_paragraph(ctx, e, 'body', extra_rules=lit_rules(vol))
        for t in e.iter(q('t')):   # Physics, Actually wording: 'Copyright (c) 2026 Name' on its own line
            if t.text and t.text.endswith('Lothar J. Musiol. All rights reserved.') and t.text.startswith('Copyright'):
                t.text = t.text[:-len('. All rights reserved.')]
    for e in title_old:
        body.remove(e)
    for e in reversed(new_title + [mk_p('', None, page_break=True)] + copyright_paras +
                     [mk_p(f'{SERIES} series', None, rpr=rpr_of(sz=18))]):
        body.insert(pos, e)

    # 6. contents page (manual, hyperlinked, Physics style) replaces the TOC field
    pos = list(body).index(toc_h1)
    body.remove(toc_sdt); body.remove(toc_h1)
    toc = build_toc(vol, rooms, chaps, body_root=body)
    for e in reversed(toc): body.insert(pos, e)
    pos += len(toc)
    # Also in This Series moves to the front, after Contents (Physics order)
    for e in also_old: body.remove(e)
    also_new = [mk_p('Also in This Series', 'Heading1', page_break=True, bookmark='also_in_series', bm_id=bm.next())]
    for k in (1, 2, 3, 4):
        if k == vol: continue
        also_new.append(mk_p(f'Volume {k} — {VOLS[k]["subtitle"]}', None, jc='left', rpr=rpr_of(b=True)))
        also_new.append(body_p(VOLS[k]['blurb']))
    also_new.append(body_p(T.ALSO_BY))
    for e in reversed(also_new): body.insert(pos, e)

    # 7. new front matter: Preface/About, How This Book Is Organized, Where the Foundations Are
    def put(old, items):
        pos = list(body).index(old[0])
        for e in old: body.remove(e)
        new = render(items)
        for e in reversed(new): body.insert(pos, e)
    put(pref_old, T.preface(vol))
    put(fr_old, T.organized(vol))
    put(base_old, T.foundations(vol))
    # rename the directory heading
    for p in body.iter(q('p')):
        if style_of(p) == 'Heading1' and ptext(p).strip() == 'This Volume’s Directory':
            a = flatten(p); a = apply_edits(a, [(0, len(text_of(a)), [('This Volume’s Chapters', None)])]); rebuild(p, a)
            ensure_bm(p, 'fm_this_volume_s_chapters', bm)
        if style_of(p) == 'Heading1' and ptext(p).strip() == 'How to Use This Book':
            ensure_bm(p, 'fm_how_to_use_this_book', bm)
        if style_of(p) == 'Heading1' and ptext(p).strip() in ('Answer Key', 'Solutions to the Problems', 'Symbol & Notation Glossary', 'Appendix — Further Reading', 'Subject Index'):
            ensure_bm(p, 'bm_' + re.sub(r'\W+', '_', ptext(p).strip().lower())[:30], bm)
    # (old directory paragraphs are kept and were edited in step 3)

    # 8. epilogue rewritten (real close) ; closing note at the very end
    pos = list(body).index(epi_old[0])
    for e in epi_old: body.remove(e)
    ep = [mk_p(T.EPILOGUE_TITLE[vol], 'Heading1', page_break=True, bookmark='epilogue', bm_id=bm.next())]
    ep += [body_p(t) for t in T.EPILOGUE[vol]]
    for e in reversed(ep): body.insert(pos, e)
    sect = body.find(q('sectPr'))
    # Also by Lothar J. Musiol (canonical list, ma_text.ALSO_BY_LIST), just before the closing note
    also_by = [mk_p(T.ALSO_BY_HEADING, 'Heading1', page_break=True, bookmark='also_by', bm_id=bm.next())]
    for group, titles in T.ALSO_BY_LIST:
        g = mk_p('', None, jc='left')
        sp = etree.SubElement(g.find(q('pPr')), q('spacing')); sp.set(q('before'), '160'); sp.set(q('after'), '40')
        g.find(q('pPr')).insert(0, etree.Element(q('keepNext')))
        g.find(q('pPr')).append(g.find(q('pPr')).find(q('jc')))
        add_runs(g, group, rpr_of(b=True))
        also_by.append(g)
        for title in titles:
            e = mk_p('', None, jc='left')
            sp = etree.SubElement(e.find(q('pPr')), q('spacing')); sp.set(q('before'), '0'); sp.set(q('after'), '20')
            ind = etree.SubElement(e.find(q('pPr')), q('ind')); ind.set(q('left'), '360'); ind.set(q('firstLine'), '0')
            e.find(q('pPr')).append(e.find(q('pPr')).find(q('jc')))
            add_runs(e, title.replace('*', ''))
            also_by.append(e)
    for e in also_by: sect.addprevious(e)
    closing = [mk_p('A Note Before You Go', 'Heading1', page_break=True, bookmark='note_before_you_go', bm_id=bm.next())]
    closing += [body_p(t) for t in T.CLOSING[vol]] + [body_p(T.AUTHOR)]
    for e in closing: sect.addprevious(e)

    # 8b. body prose justified, as in Physics, Actually (images, display maths, captions, code left alone)
    justify_body(body)

    # 9. sanity: every hyperlink anchor resolves
    names = set(b.get(q('name')) for b in root.iter(q('bookmarkStart')))
    dangling = [h.get(q('anchor')) for h in root.iter(q('hyperlink')) if h.get(q('anchor')) and h.get(q('anchor')) not in names]
    STATS['dangling'] = dangling
    return root

M = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
def justify_body(body):
    started = False; prev = None
    for el in body:
        if etree.QName(el).localname != 'p': prev = None; continue
        if style_of(el) == 'Heading1' and ptext(el).strip() == 'Also in This Series': started = True
        t = ptext(el).strip(); ppr = el.find(q('pPr'))
        ok = (started and not style_of(el) and len(t) >= 40 and el.find('.//' + q('drawing')) is None
              and el.find('.//{%s}oMathPara' % M) is None
              and not (prev is not None and prev.find('.//' + q('drawing')) is not None)
              and not re.match(r'(Figure|Fig\.|Table)\s', t)
              and not any((rf.get(q('ascii')) or '') in ('Consolas', 'Courier New') for rf in el.iter(q('rFonts'))))
        if ok and (ppr is None or ppr.find(q('jc')) is None):
            if ppr is None: ppr = etree.Element(q('pPr')); el.insert(0, ppr)
            etree.SubElement(ppr, q('jc')).set(q('val'), 'both')
        prev = el

def ensure_bm(p, name, bm):
    for b in p.iter(q('bookmarkStart')):
        if b.get(q('name')) == name: return
    i_ = bm.next()
    b1 = etree.Element(q('bookmarkStart')); b1.set(q('id'), str(i_)); b1.set(q('name'), name)
    b2 = etree.Element(q('bookmarkEnd')); b2.set(q('id'), str(i_))
    ppr = p.find(q('pPr')); at = 1 if ppr is not None else 0
    p.insert(at, b2); p.insert(at, b1)

def build_toc(vol, rooms, chaps, body_root):
    """Physics, Actually contents: 'Table of Contents' line then hyperlinked entries
    with dot leaders and PAGEREF fields (Word refreshes the numbers)."""
    out = [mk_p('', None, page_break=True)]
    out.append(mk_p('Table of Contents', None, rpr=rpr_of(sz=28)))
    def entry(label, anchor, level=1):
        p = etree.Element(q('p')); ppr = etree.SubElement(p, q('pPr'))
        tabs = etree.SubElement(ppr, q('tabs')); tab = etree.SubElement(tabs, q('tab'))
        tab.set(q('val'), 'right'); tab.set(q('leader'), 'dot'); tab.set(q('pos'), '9000')
        if level == 2:
            sp = etree.SubElement(ppr, q('spacing')); sp.set(q('after'), '40')
            ind = etree.SubElement(ppr, q('ind')); ind.set(q('left'), '432')
        j = etree.SubElement(ppr, q('jc')); j.set(q('val'), 'left')
        hl = etree.SubElement(p, q('hyperlink')); hl.set(q('anchor'), anchor); hl.set(q('history'), '1')
        rp = rpr_of(color='0563C1', u=True, sz=(20 if level == 2 else None), b=(level == 1 and label.startswith('Chapter')))
        r = etree.SubElement(hl, q('r')); r.append(copy.deepcopy(rp)); t = etree.SubElement(r, q('t')); t.set(XMLSPACE, 'preserve'); t.text = label
        r = etree.SubElement(hl, q('r')); r.append(copy.deepcopy(rp)); etree.SubElement(r, q('tab'))
        for kind, val in (('begin', None), ('instr', f' PAGEREF {anchor} \\h '), ('separate', None), ('num', '1'), ('end', None)):
            r = etree.SubElement(hl, q('r'))
            if kind == 'instr':
                it = etree.SubElement(r, q('instrText')); it.set(XMLSPACE, 'preserve'); it.text = val
            elif kind == 'num':
                etree.SubElement(etree.SubElement(r, q('rPr')), q('noProof')); t = etree.SubElement(r, q('t')); t.text = val
            else:
                fc = etree.SubElement(r, q('fldChar')); fc.set(q('fldCharType'), kind)
                if kind == 'begin': fc.set(q('dirty'), 'true')
        return p
    lo, hi = VOLS[vol]['chapters']
    out.append(entry('Also in This Series', 'also_in_series'))
    for title in T.front_titles(vol):
        out.append(entry(title, 'fm_' + re.sub(r'\W+', '_', title.lower())[:30]))
    out.append(entry('How to Use This Book', 'fm_how_to_use_this_book'))
    out.append(entry('How This Book Is Organized', 'fm_how_this_book_is_organized'))
    out.append(entry('Where the Foundations Are', 'fm_where_the_foundations_are'))
    out.append(entry('This Volume’s Chapters', 'fm_this_volume_s_chapters'))
    for n in range(lo, hi + 1):
        out.append(entry(f'Chapter {n}: {chaps[n]["title"]}', ch_bm(n)))
        for k in sorted((k for k in rooms if rooms[k]['ch'] == n), key=lambda k: int(k.split('.')[1])):
            out.append(entry(f'Section {k}: {rooms[k]["title"]}', sec_bm(k), level=2))
    out.append(entry(T.EPILOGUE_TITLE[vol], 'epilogue'))
    for title in ('Answer Key', 'Solutions to the Problems', 'Symbol & Notation Glossary', 'Appendix — Further Reading', 'Subject Index'):
        out.append(entry(title, 'bm_' + re.sub(r'\W+', '_', title.lower())[:30]))
    out.append(entry(T.ALSO_BY_HEADING, 'also_by'))
    out.append(entry('A Note Before You Go', 'note_before_you_go'))
    return out

# ---------------------------------------------------------------- styles / properties
PHYS_STYLES = {
 'Title':   dict(font='Calibri', b=True, color='17365D', sz=40, border=True, before=0, after=300, jc='center'),
 'Heading1': dict(font='Calibri', b=True, color='0000FF', sz=36, before=480, after=0, jc='center', outline=0),
 'Heading2': dict(font='Calibri', b=True, color='0000FF', sz=36, before=200, after=0, jc='center', outline=1),
}
def restyle(styles_root):
    for s in styles_root.findall('w:style', NS):
        sid = s.get(q('styleId'))
        if sid not in PHYS_STYLES: continue
        d = PHYS_STYLES[sid]
        for x in s.findall(q('pPr')) + s.findall(q('rPr')): s.remove(x)
        ppr = etree.SubElement(s, q('pPr'))
        etree.SubElement(ppr, q('keepNext')); etree.SubElement(ppr, q('keepLines'))
        if d.get('border'):
            bd = etree.SubElement(ppr, q('pBdr')); bt = etree.SubElement(bd, q('bottom'))
            for k, v in (('val', 'single'), ('sz', '8'), ('space', '4'), ('color', '4F81BD')): bt.set(q(k), v)
        sp = etree.SubElement(ppr, q('spacing')); sp.set(q('before'), str(d['before'])); sp.set(q('after'), str(d['after']))
        if sid == 'Title': sp.set(q('line'), '240'); sp.set(q('lineRule'), 'auto')
        j = etree.SubElement(ppr, q('jc')); j.set(q('val'), d['jc'])
        if 'outline' in d:
            o = etree.SubElement(ppr, q('outlineLvl')); o.set(q('val'), str(d['outline']))
        rpr = rpr_of(font=d['font'], b=d['b'], color=d['color'], sz=d['sz'])
        if sid == 'Title':
            sp2 = etree.Element(q('spacing')); sp2.set(q('val'), '5'); rpr.insert(3, sp2)
            k = etree.Element(q('kern')); k.set(q('val'), '28'); rpr.insert(4, k)
        s.append(rpr)
        # w:style children order: name, aliases, basedOn, next, link, ..., qFormat, rsid, pPr, rPr
    return styles_root

def core_props(xml, vol):
    v = VOLS[vol]
    root = etree.fromstring(xml)
    nsmap = {'dc': 'http://purl.org/dc/elements/1.1/', 'cp': 'http://schemas.openxmlformats.org/package/2006/metadata/core-properties'}
    def setel(tag, text):
        pre, name = tag.split(':')
        el = root.find(f'{tag}', nsmap)
        if el is None:
            el = etree.SubElement(root, '{%s}%s' % (nsmap[pre], name))
        el.text = text
    setel('dc:title', f'{SERIES} — Volume {vol}: {v["subtitle"]}')
    setel('dc:subject', f'{SERIES} series, Volume {vol} of 4')
    setel('dc:creator', T.AUTHOR)
    setel('dc:description', f'Chapters {v["chapters"][0]}–{v["chapters"][1]}: {v["subtitle"]}')
    setel('cp:keywords', 'mathematics; worked examples; ' + v['keywords'])
    setel('cp:lastModifiedBy', T.AUTHOR)
    # Word wants elements in schema order only loosely; keep as is
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)

# ---------------------------------------------------------------- main
def main(src_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    srcs = {k: os.path.join(src_dir, f'The Mathematics Tower - Volume {k}.docx') for k in (1, 2, 3, 4)}
    docs = {}
    for k, path in srcs.items():
        with zipfile.ZipFile(path) as z:
            docs[k] = etree.fromstring(z.read('word/document.xml'))
    rooms, chaps = build_index(docs)
    report = {}
    for k in (1, 2, 3, 4):
        STATS.clear()
        root = transform(k, docs[k], rooms, chaps)
        out = os.path.join(out_dir, f'{SERIES} - Volume {k}.docx')
        with zipfile.ZipFile(srcs[k]) as zin, zipfile.ZipFile(out + '.tmp', 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == 'word/document.xml':
                    data = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
                elif item.filename == 'word/styles.xml':
                    data = etree.tostring(restyle(etree.fromstring(data)), xml_declaration=True, encoding='UTF-8', standalone=True)
                elif item.filename == 'docProps/core.xml':
                    data = core_props(data, k)
                zout.writestr(item, data)
        os.replace(out + '.tmp', out)
        report[k] = {kk: vv for kk, vv in STATS.items() if kk != 'skipped_paras'}
        report[k]['skipped_paras'] = len(STATS.get('skipped_paras', []))
    json.dump(report, open(os.path.join(out_dir, 'build_report.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(report, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
