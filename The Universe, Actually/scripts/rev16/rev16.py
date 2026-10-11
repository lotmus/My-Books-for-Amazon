"""The Universe, Actually REV15 -> REV16 restructure (11 Oct 2026).
Usage: python rev16.py REV15.docx REV16.docx  (ops/*.py edit layer, then parts reorder, renumber, Contents, links)."""
import sys, re, copy, glob, importlib.util, docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from model16 import load, text, style
from engine import newpara, sub, runs_of, W
src, out = sys.argv[1], sys.argv[2]
d, secs = load(src); body = d.element.body
NE = lambda s: [p for p in s['paras'] if text(p).strip() or p.findall('.//'+W('drawing'))]
orig = [NE(s) for s in secs]
tpl = next(p for p in orig[5])  # a normal body paragraph
def last_el(k):
    s = secs[k]; ps = s['paras']
    return ps[-1] if ps else s['h']
log = []
ops = []
for f in sorted(glob.glob('ops/b*.py')):
    sp = importlib.util.spec_from_file_location('o', f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); ops += m.OPS
for op in ops:
    kind, k = op[0], op[1]; s = secs[k]
    if kind == 'sub':
        ok = any(sub(p, op[2], op[3]) for p in list(dict.fromkeys(orig[k] + s['paras'])) if p.getparent() is not None)
        if not ok: raise SystemExit('SUB FAIL [%d] %r' % (k, op[2][:80]))
    elif kind == 'delp':
        p = orig[k][op[2]]; p.getparent().remove(p); s['paras'].remove(p)
    elif kind == 'replace_p':
        p = orig[k][op[2]]; n = newpara(p, op[3]); p.addprevious(n); p.getparent().remove(p)
        for ss in secs:
            if p in ss['paras']: ss['paras'][ss['paras'].index(p)] = n; break
    elif kind == 'insert_p':   # insert new paragraph after original paragraph index op[2] (-1 = at start)
        ref = orig[k][op[2]] if op[2] >= 0 else None
        n = newpara(tpl, op[3])
        if ref is None: s['h'].addnext(n); s['paras'].insert(0, n)
        else: ref.addnext(n); s['paras'].insert(s['paras'].index(ref) + 1, n)
    elif kind == 'replace':
        t0 = orig[k][0] if orig[k] else tpl
        for p in s['paras']:
            if p.getparent() is not None: p.getparent().remove(p)
        new = [newpara(t0, m) for m in op[2]]
        a = s['h']
        for n in new: a.addnext(n); a = n
        s['paras'] = new
    elif kind == 'title':
        h = s['h']; ts = list(h.iter(W('t'))); ts[0].text = op[2]; [setattr(t, 'text', '') for t in ts[1:]]
    elif kind == 'join':
        b = secs[op[2]]; a = last_el(k)
        for p in reversed(b['paras']): a.addnext(p)
        s['paras'] += b['paras']; b['paras'] = []
        b['h'].getparent().remove(b['h']); b['dead'] = True
    elif kind == 'drop':
        for p in s['paras']:
            if p.getparent() is not None: p.getparent().remove(p)
        s['h'].getparent().remove(s['h']); s['dead'] = True; s['paras'] = []
    elif kind == 'move':
        els = [s['h']] + s['paras']; a = last_el(op[2])
        for e in reversed(els): a.addnext(e)
        # keep model consistent: section k now follows j inside j's chapter
    elif kind == 'movep':
        e = orig[k][op[2]]; a = last_el(k)
        if a is not e: a.addnext(e); s['paras'].remove(e); s['paras'].append(e)
    elif kind == 'image':
        from docx.shared import Inches
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        ref = orig[k][op[2]]
        ip = d.add_paragraph(); ip.alignment = WD_ALIGN_PARAGRAPH.CENTER
        ip.add_run().add_picture(op[3], width=Inches(6.0))
        for dp in ip._p.iter('{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr'):
            dp.set('descr', op[5]); dp.set('title', op[4])
        cp = newpara(tpl, '*' + op[4] + '*'); 
        jc = OxmlElement('w:jc'); jc.set(W('val'), 'center')
        ppr = cp.find(W('pPr'))
        if ppr is None: ppr = OxmlElement('w:pPr'); cp.insert(0, ppr)
        for x in ppr.findall(W('jc')): ppr.remove(x)
        ppr.append(jc)
        ref.addnext(ip._p); ip._p.addnext(cp)
        s['paras'] += [ip._p, cp]
    else: raise SystemExit('bad op ' + kind)
print('ops applied', len(ops))
import structure16
structure16.run(d, body, out)
