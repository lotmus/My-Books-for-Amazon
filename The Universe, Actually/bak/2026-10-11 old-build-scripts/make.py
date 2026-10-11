# -*- coding: utf-8 -*-
# Build REV12 from REV11 pool + structure.txt + edits.py. Usage: python make.py [out.docx]
import io, sys, os, re, json, zipfile, shutil, importlib
from lxml import etree
import render as R
from build_map import load_map, resolve
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
SRC = '../bak/The_Universe_Actually__REV11.docx' if os.path.exists('../bak/The_Universe_Actually__REV11.docx') else '../The_Universe_Actually__REV11.docx'
OUT = sys.argv[1] if len(sys.argv) > 1 else '../The_Universe_Actually__REV12.docx'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

# ---------- content model ----------
pool = json.load(open('pool.json', encoding='utf-8'))
parts = load_map()
problems, unassigned = resolve(parts, pool)
assert not problems, problems
front = json.load(open('frontback.json', encoding='utf-8'))   # note, preface, epilogue, sources, bibliography, resources, appendix...

import edits
importlib.reload(edits)
log = edits.apply(parts, front)
for l in log: print(l)

# ---------- paragraph pre-processing ----------
def prep(t):
    t = t.strip()
    if t.startswith('**Topics in this chapter**'):
        items = [x.strip() for x in t[len('**Topics in this chapter**'):].split('·') if x.strip()]
        return 'TOPICS:' + '; '.join(items) + '.'
    return t

def render_paras(paras):
    out = []
    for t in paras:
        t = prep(t)
        if not t: continue
        if t.startswith('TOPICS:'):
            out.append(R.para('**In this section:** ' + t[7:], i=True, color='5C6B73'))
        else:
            out.append(R.body(t))
    return out

# ---------- body ----------
body = []; toc = []
roman = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
chn = 0
for pi, p in enumerate(parts):
    anchor = 'part_%d' % (pi + 1)
    ptitle = 'Part %s: %s' % (roman[pi], p['title'])
    body.append(R.part_title(ptitle, anchor)); body.append(R.tagline(p['tag']))
    toc.append(('part', ptitle, anchor))
    for ci, c in enumerate(p['chapters']):
        chn += 1
        canchor = 'ch_%d' % chn
        ctitle = '%d. %s' % (chn, c['title'])
        body.append(R.h2(ctitle, canchor, pagebreak=(ci > 0))); toc.append(('chapter', ctitle, canchor))
        if c['leadsec']:
            paras = [prep(t) for t in c['leadsec']['paras'] if t.strip()]
            if len(paras) > 1 and len(paras[0].split()) < 30 and not paras[0].startswith('TOPICS'):
                body.append(R.lead_italic(paras[0])); paras = paras[1:]
            body.extend(render_paras(paras))
        for si, s in enumerate(c['secs']):
            same = (si == 0 and not c['leadsec'] and re.sub(r'\W', '', s['title'].lower()) == re.sub(r'\W', '', c['title'].lower()))
            if not same: body.append(R.h3(s['title']))
            body.extend(render_paras(s['paras']))

# ---------- front / back matter ----------
def special(key, title, bm, center=False):
    d = front[key]
    out = [R.h1(d.get('title', title), bm, center=center)]
    out.extend(render_paras(d['paras']))
    return out

note = special('note', 'A Note on This Book', 'fm_note')
pref = special('preface', 'Preface', 'fm_preface')
epil = special('epilogue', 'Epilogue: Actually', 'bm_epilogue')
srcs = special('sources', 'A Note on Sources', 'bm_sources')
bibl = [R.h1('Bibliography', 'bm_bibliography', center=True, after=280, sz=32)]
bibl += [R.para(t) if not t.startswith('Reading') else R.small_heading(t) for t in front['bibliography']['paras']]
res = [R.h1('External Resources', 'bm_resources')]
res += render_paras(front['resources']['paras'])
app = [R.h1('Appendix', 'bm_appendix')]
app += [R.para(front['appendix']['review'], i=True)]
app += [R.small_heading('About the Author')] + render_paras(front['appendix']['author'])
alsoby = front['alsoby_xml']

# ---------- contents ----------
cont = [R.h1('Contents', 'fm_contents')]
cont.append(R.para('Eight parts, each divided into chapters. Select a title to jump to it.', i=True, color='5C6B73', sz=18))
cont.append(R.toc_plain('A Note on This Book', 'fm_note')); cont.append(R.toc_plain('Preface', 'fm_preface'))
for kind, text, anc in toc:
    cont.append(R.toc_part(text, anc) if kind == 'part' else R.toc_chapter(text, anc))
for text, anc in [('Epilogue: Actually', 'bm_epilogue'), ('A Note on Sources', 'bm_sources'), ('Bibliography', 'bm_bibliography'),
                  ('External Resources', 'bm_resources'), ('Appendix', 'bm_appendix')]:
    cont.append(R.toc_plain(text, anc))

# ---------- assemble ----------
zin = zipfile.ZipFile(SRC)
doc = zin.read('word/document.xml').decode('utf-8')
head = doc[:doc.index('<w:body>') + len('<w:body>')]
sect = doc[doc.index('<w:sectPr'):]
title_xml = front['title_xml']
xml = head + ''.join(title_xml) + ''.join(note) + ''.join(pref) + ''.join(cont) + ''.join(body) + ''.join(epil) + ''.join(srcs) \
      + ''.join(bibl) + ''.join(res) + ''.join(app) + ''.join(alsoby) + sect
etree.fromstring(xml.encode('utf-8'))   # well-formedness check

tmp = OUT + '.tmp'
with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == 'word/document.xml': data = xml.encode('utf-8')
        zout.writestr(item, data)
if os.path.exists(OUT): os.remove(OUT)
os.rename(tmp, OUT)
words = len(re.sub(r'<[^>]+>', ' ', xml).split())
print('wrote', OUT, '| parts', len(parts), 'chapters', chn, 'sections', sum(len(c['secs']) for p in parts for c in p['chapters']), '| ~words', words)
