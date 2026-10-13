"""Extract an EE master docx into the tagged-text source mirror used in chapters/BookN:
front.txt, src/chNN.txt (one per chapter, Part headings included as PART:), src/back.txt, fig/*.png.
Tags: PART H1 H2 H3 P EQ FIG WE PROB SOL KEY MIS BENCH LI. The docx stays the master; this is a readable mirror."""
import sys, os, re, docx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eedoc import *
from docx.oxml.ns import qn
def jc(p):
    pp = p.find(W('pPr')); j = pp.find(W('jc')) if pp is not None else None
    return j.get(W('val')) if j is not None else ''
def run(src, outdir):
    d = docx.Document(src); os.makedirs(outdir + '/src', exist_ok=True); os.makedirs(outdir + '/fig', exist_ok=True)
    rels = d.part.rels; ps = body_ps(d)
    files = {}; cur = 'front'; buf = {'front': []}; pending = None; skip = False; order = ['front']
    for k, p in enumerate(ps):
        if skip: skip = False; continue
        t = ptext(p).strip(); s = sty(p)
        blips = p.findall('.//' + qn('a:blip'))
        if s == 'Heading1' and t.startswith('Part '):
            cur = 'pending_part'; buf.setdefault(cur, []).append('PART: ' + t); continue
        if s == 'Heading1':
            m = re.match(r'Chapter (\d+)', t)
            if m: name = 'ch%02d' % int(m.group(1))
            elif t.startswith(('Appendix', 'About the Author', 'Also by')) or cur.startswith('ch') or cur == 'back': name = 'back'
            else: name = 'front'
            carry = buf.pop('pending_part', []) if name.startswith('ch') else []
            if name not in buf: buf[name] = []; order.append(name)
            cur = name; buf[cur] += carry + ['H1: ' + t]; continue
        if cur == 'pending_part': cur = order[-1]
        L = buf[cur]
        if blips:
            names = []; alts = []
            docprs = p.findall('.//' + qn('wp:docPr'))
            for i, b in enumerate(blips):
                part = rels[b.get(qn('r:embed'))].target_part
                cap = ptext(ps[k+1]).strip() if k + 1 < len(ps) else ''
                m = re.match(r'Figure (\d+)\.(\d+)', cap)
                fn = 'fig%s_%s.png' % m.groups() if m else os.path.basename(part.partname)
                open(outdir + '/fig/' + fn, 'wb').write(part.blob); names.append(fn)
                alts.append((docprs[i].get('descr') or '').strip() if i < len(docprs) else '')
            cap = ptext(ps[k+1]).strip() if k + 1 < len(ps) else ''
            if cap.startswith('Figure'): skip = True
            L.append('FIG: ' + ', '.join(names) + ' | ' + cap + ' | ' + ' / '.join(alts)); continue
        if not t: continue
        if s in ('Heading2', 'Heading3'): L.append(('H2: ' if s == 'Heading2' else 'H3: ') + t); continue
        if t in ('Key Idea', 'Common Misconception', 'From the Bench'): pending = {'Key Idea': 'KEY', 'Common Misconception': 'MIS', 'From the Bench': 'BENCH'}[t]; continue
        if pending: L.append(pending + ': ' + t); pending = None; continue
        if t.startswith('Worked Example'): L.append('WE: ' + t); continue
        if t.startswith('Problem:'): L.append('PROB: ' + t[8:].strip()); continue
        if t.startswith('Solution:'): L.append('SOL: ' + t[9:].strip()); continue
        if s == 'ListParagraph' or p.find('.//' + W('numPr')) is not None: L.append('LI: ' + t); continue
        if jc(p) == 'center' and len(t) < 160: L.append('EQ: ' + t); continue
        L.append('P: ' + t)
    for name in order:
        path = outdir + ('/front.txt' if name == 'front' else '/src/%s.txt' % name)
        open(path, 'w', encoding='utf-8').write('\n'.join(buf[name]) + '\n')
    open(outdir + '/README.md', 'w').write('Tagged-text mirror of the docx master, extracted by scripts/diagrams/common/docx2src.py. The docx is the master; regenerate this folder after every change to it.\n')
    return order
if __name__ == '__main__':
    o = run(sys.argv[1], sys.argv[2]); print(len(o), 'files')
