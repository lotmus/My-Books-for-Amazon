import re, copy
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from model16 import text, style
W=lambda t: qn('w:'+t)
def runs_of(p): return [r for r in p.iter(W('r')) if r.find(W('t')) is not None]
def rtxt(r): return ''.join(t.text or '' for t in r.iter(W('t')))
def base_rpr(r):
    rp=r.find(W('rPr'))
    rp=copy.deepcopy(rp) if rp is not None else OxmlElement('w:rPr')
    for tag in ('vertAlign','i','b','iCs','bCs'):
        for x in rp.findall(W(tag)): rp.remove(x)
    return rp
TOK=re.compile(r'(\^\{[^}]*\}|_\{[^}]*\}|\*[^*]+\*|\{ch\d+\}|\{bib:[^}]+\})')
def mkrun(txt, rpr, va=None, it=False):
    r=OxmlElement('w:r'); rp=copy.deepcopy(rpr)
    if it: rp.append(OxmlElement('w:i'))
    if va:
        v=OxmlElement('w:vertAlign'); v.set(W('val'),va); rp.append(v)
    if len(rp): r.append(rp)
    t=OxmlElement('w:t'); t.text=txt; t.set('{http://www.w3.org/XML/1998/namespace}space','preserve'); r.append(t); return r
def build(markup, rpr):
    out=[]
    for tok in TOK.split(markup):
        if not tok: continue
        if tok.startswith('^{'): out.append(mkrun(tok[2:-1],rpr,'superscript'))
        elif tok.startswith('_{'): out.append(mkrun(tok[2:-1],rpr,'subscript'))
        elif tok.startswith('{ch'):
            n=tok[3:-1]; h=OxmlElement('w:hyperlink'); h.set(W('anchor'),'oldch_'+n)
            lr=copy.deepcopy(rpr); c=OxmlElement('w:color'); c.set(W('val'),'0563C1'); lr.append(c); u=OxmlElement('w:u'); u.set(W('val'),'single'); lr.append(u)
            h.append(mkrun('@@CH%s@@'%n,lr)); out.append(h)
        elif tok.startswith('{bib:'):
            h=OxmlElement('w:hyperlink'); h.set(W('anchor'),'bibref:'+tok[5:-1]); h.append(mkrun(tok[5:-1],rpr,it=True)); out.append(h)
        elif tok.startswith('*') and len(tok)>2: out.append(mkrun(tok[1:-1],rpr,it=True))
        else: out.append(mkrun(tok,rpr))
    return out
def newpara(template, markup):
    p=copy.deepcopy(template)
    rs=runs_of(template); rpr=base_rpr(rs[0]) if rs else OxmlElement('w:rPr')
    for ch in list(p):
        if ch.tag!=W('pPr'): p.remove(ch)
    for e in build(markup,rpr): p.append(e)
    return p
def sub(p, old, new):
    rs=runs_of(p); full=''.join(rtxt(r) for r in rs)
    i=full.find(old)
    if i<0: return False
    j=i+len(old); pos=0; first=None
    for r in rs:
        t=rtxt(r); a,b=pos,pos+len(t); pos=b
        if b<=i or a>=j: continue
        if first is None: first=(r,max(i,a)-a)
        ts=list(r.iter(W('t'))); s=t
        keep=s[:max(i,a)-a]+s[min(j,b)-a:]
        ts[0].text=keep; [setattr(x,'text','') for x in ts[1:]]
        if first[0] is r: first=(r,max(i,a)-a,keep)
    r,off,keep=first
    if new:
        rpr=base_rpr(r); ts=list(r.iter(W('t')))
        ts[0].text=keep[:off]
        tail=keep[off:]
        els=build(new,rpr)
        if tail:
            r2=copy.deepcopy(r); [setattr(x,'text','') for x in r2.iter(W('t'))]; list(r2.iter(W('t')))[0].text=tail
            els.append(r2)
        anchor=r if r.getparent().tag==W('p') else r.getparent()
        for e in reversed(els): anchor.addnext(e)
    for x in p.iter(W('t')): x.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    return True
