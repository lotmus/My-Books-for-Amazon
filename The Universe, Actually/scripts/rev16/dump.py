import docx,sys,re
from docx.oxml.ns import qn
d=docx.Document(sys.argv[1]); body=d.element.body
def text(p): return ''.join(t.text or '' for t in p.iter(qn('w:t')))
def style(p):
    s=p.find(qn('w:pPr')); s=s.find(qn('w:pStyle')) if s is not None else None
    return s.get(qn('w:val')) if s is not None else ''
out=[];wc=0;cw=0;cur=None
kids=list(body.iterchildren())
for i,e in enumerate(kids):
    tag=e.tag.split('}')[1]
    if tag=='tbl': out.append(f'{i} TABLE'); continue
    if tag!='p': continue
    s=style(e); t=text(e); n=len(t.split())
    wc+=n
    if s.startswith('Heading') or s in('Title','Subtitle','TOC1','TOC2'):
        out.append(f'{i} [{s}] {t[:90]}  (wc_so_far={wc})')
    if e.findall('.//'+qn('w:drawing')): out.append(f'{i} IMG {t[:40]}')
print('\n'.join(out)); print('TOTAL WORDS',wc)
