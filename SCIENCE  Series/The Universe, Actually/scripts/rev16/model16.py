import docx,re
from docx.oxml.ns import qn
def text(p): return ''.join(t.text or '' for t in p.iter(qn('w:t')))
def style(p):
    s=p.find(qn('w:pPr')); s=s.find(qn('w:pStyle')) if s is not None else None
    return s.get(qn('w:val')) if s is not None else ''
def load(path):
    d=docx.Document(path); body=d.element.body
    kids=[e for e in body.iterchildren() if e.tag==qn('w:p')]
    secs=[]; ch=None; part=None
    for e in kids:
        s=style(e); t=text(e)
        if s=='Heading1': part=t; ch=None; secs.append({'part':t,'ch':None,'title':t,'paras':[],'h':e,'lvl':1}); continue
        if s=='Heading2': ch=t; secs.append({'part':part,'ch':t,'title':'(intro)','paras':[],'h':e,'lvl':2}); continue
        if s=='Heading3': secs.append({'part':part,'ch':ch,'title':t,'paras':[],'h':e,'lvl':3}); continue
        if secs: secs[-1]['paras'].append(e)
    return d,secs
