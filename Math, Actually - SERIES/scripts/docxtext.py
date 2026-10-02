"""Run-aware text editing for WordprocessingML paragraphs (lxml).

A paragraph is flattened into atoms:
  ('c', char, rPr_xml, anchor)   one character of run text
  ('x', element)                 any other inline child kept verbatim
                                 (bookmarks, drawings, field runs, tabs...)
Edits are applied to the atom list, then the paragraph's inline content is
re-emitted, grouping consecutive characters that share rPr and anchor.
Only paragraphs that actually change are rebuilt.
"""
import copy, re
from lxml import etree
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
def q(t): return '{%s}%s' % (W, t)
XMLSPACE = '{http://www.w3.org/XML/1998/namespace}space'

def _rpr_key(rpr):
    return etree.tostring(rpr) if rpr is not None else b''

def flatten(p):
    """Return atoms or None if the paragraph has structures we don't rebuild."""
    atoms = []
    for ch in list(p):
        tag = etree.QName(ch).localname
        if tag == 'pPr':
            continue
        if tag == 'r':
            _run_atoms(ch, None, atoms)
        elif tag == 'hyperlink':
            anc = ch.get(q('anchor'))
            if anc is None:   # external link: keep verbatim
                atoms.append(('x', ch)); continue
            for sub in ch:
                st = etree.QName(sub).localname
                if st == 'r': _run_atoms(sub, anc, atoms)
                elif st in ('bookmarkStart', 'bookmarkEnd', 'proofErr'):
                    if st != 'proofErr': atoms.append(('x', sub))
                else:
                    return None
        elif tag == 'proofErr':
            continue
        elif tag in ('ins', 'del', 'smartTag', 'sdt', 'fldSimple', 'customXml'):
            return None
        else:
            atoms.append(('x', ch))
    return atoms

def _run_atoms(r, anchor, atoms):
    rpr = r.find(q('rPr'))
    kids = [k for k in r if etree.QName(k).localname != 'rPr']
    simple = all(etree.QName(k).localname in ('t', 'lastRenderedPageBreak') for k in kids)
    if not simple:
        # keep whole run (drawings, fields, tabs, breaks ...) but split out text
        if any(etree.QName(k).localname in ('t',) for k in kids) and all(
                etree.QName(k).localname in ('t', 'tab', 'br', 'lastRenderedPageBreak', 'noBreakHyphen') for k in kids):
            for k in kids:
                ln = etree.QName(k).localname
                if ln == 't':
                    for c in (k.text or ''): atoms.append(('c', c, rpr, anchor))
                elif ln == 'lastRenderedPageBreak':
                    continue
                else:
                    nr = etree.Element(q('r'))
                    if rpr is not None: nr.append(copy.deepcopy(rpr))
                    nr.append(copy.deepcopy(k))
                    atoms.append(('x', nr, anchor))
            return
        atoms.append(('x', r, anchor)); return
    for k in kids:
        if etree.QName(k).localname == 't':
            for c in (k.text or ''): atoms.append(('c', c, rpr, anchor))

def text_of(atoms):
    return ''.join(a[1] for a in atoms if a[0] == 'c')

def char_index(atoms):
    """positions of 'c' atoms in atom list, by text offset"""
    return [i for i, a in enumerate(atoms) if a[0] == 'c']

def apply_edits(atoms, edits):
    """edits: list of (start, end, pieces) in text offsets, non-overlapping.
    pieces: list of (text, mode) where mode is
      None            -> inherit rPr/anchor of first replaced char, link removed if
                         keep_link False
      ('plain',)      -> inherit rPr but no hyperlink, link colour/underline stripped
      ('link', anchor, rpr_or_None) -> hyperlink to anchor
    """
    idx = char_index(atoms)
    edits = sorted(edits, key=lambda e: e[0])
    out = []; pos_atom = 0
    for (s, e, pieces) in edits:
        a_s = idx[s]
        a_e = idx[e - 1] + 1 if e > s else a_s
        out.extend(atoms[pos_atom:a_s])
        base = atoms[a_s]
        base_rpr, base_anc = base[2], base[3]
        # keep non-char atoms inside the span (e.g. bookmarks) after replacement
        inner_x = [a for a in atoms[a_s:a_e] if a[0] == 'x']
        for text, mode in pieces:
            if mode is None:
                for c in text: out.append(('c', c, base_rpr, base_anc))
            elif mode[0] == 'plain':
                r = strip_link_look(base_rpr) if base_anc else base_rpr
                for c in text: out.append(('c', c, r, None))
            elif mode[0] == 'link':
                r = mode[2] if mode[2] is not None else (base_rpr if base_anc else link_look(base_rpr))
                for c in text: out.append(('c', c, r, mode[1]))
        out.extend(inner_x)
        pos_atom = a_e
    out.extend(atoms[pos_atom:])
    return out

def link_look(rpr):
    r = copy.deepcopy(rpr) if rpr is not None else etree.Element(q('rPr'))
    for t in ('color', 'u'):
        for x in r.findall(q(t)): r.remove(x)
    col = etree.Element(q('color')); col.set(q('val'), '1155CC')
    u = etree.Element(q('u')); u.set(q('val'), 'single')
    _insert_ordered(r, col); _insert_ordered(r, u)
    return r

def strip_link_look(rpr):
    if rpr is None: return None
    r = copy.deepcopy(rpr)
    for t in ('color', 'u', 'rStyle'):
        for x in r.findall(q(t)): r.remove(x)
    return r if len(r) else None

RPR_ORDER = ['rStyle','rFonts','b','bCs','i','iCs','caps','smallCaps','strike','dstrike','outline','shadow','emboss','imprint','noProof','snapToGrid','vanish','webHidden','color','spacing','w','kern','position','sz','szCs','highlight','u','effect','bdr','shd','fitText','vertAlign','rtl','cs','em','lang','eastAsianLayout','specVanish','oMath']
def _insert_ordered(rpr, el):
    name = etree.QName(el).localname
    k = RPR_ORDER.index(name)
    for i, ch in enumerate(rpr):
        cn = etree.QName(ch).localname
        if cn in RPR_ORDER and RPR_ORDER.index(cn) > k:
            rpr.insert(i, el); return
    rpr.append(el)

def rebuild(p, atoms):
    ppr = p.find(q('pPr'))
    for ch in list(p):
        if ch is not ppr: p.remove(ch)
    cur_link = None; cur_anchor = object(); cur_run = None; cur_key = None
    def container():
        return cur_link if cur_link is not None else p
    for a in atoms:
        if a[0] == 'x':
            el = a[1]; anc = a[2] if len(a) > 2 else None
            if anc is not None and etree.QName(el).localname == 'r':
                if cur_anchor != anc:
                    cur_link = etree.SubElement(p, q('hyperlink')); cur_link.set(q('anchor'), anc); cur_link.set(q('history'), '1'); cur_anchor = anc
                cur_link.append(el); cur_run = None; continue
            p.append(el); cur_link = None; cur_anchor = object(); cur_run = None
            continue
        _, c, rpr, anc = a
        if anc != cur_anchor if anc is not None else cur_link is not None:
            cur_run = None
            if anc is None:
                cur_link = None; cur_anchor = object()
            else:
                cur_link = etree.SubElement(p, q('hyperlink')); cur_link.set(q('anchor'), anc); cur_link.set(q('history'), '1'); cur_anchor = anc
        key = _rpr_key(rpr)
        if cur_run is None or key != cur_key:
            cur_run = etree.SubElement(container(), q('r'))
            if rpr is not None: cur_run.append(copy.deepcopy(rpr))
            t = etree.SubElement(cur_run, q('t')); t.set(XMLSPACE, 'preserve'); t.text = ''
            cur_key = key
        cur_run[-1].text += c
    return p
