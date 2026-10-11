import sys,re
from docx.oxml.ns import qn
from model16 import load
def rtext(p):
    out=''
    for r in p.iter(qn('w:r')):
        t=''.join(x.text or '' for x in r.iter(qn('w:t')))
        if not t: continue
        rp=r.find(qn('w:rPr')); va=None; it=False; bo=False
        if rp is not None:
            v=rp.find(qn('w:vertAlign')); va=v.get(qn('w:val')) if v is not None else None
            i=rp.find(qn('w:i')); it=i is not None and i.get(qn('w:val')) not in ('0','false')
            b=rp.find(qn('w:b')); bo=b is not None and b.get(qn('w:val')) not in ('0','false')
        if va=='superscript': t='^{'+t+'}'
        elif va=='subscript': t='_{'+t+'}'
        if it: t='*'+t+'*'
        if bo: t='**'+t+'**'
        out+=t
    return out.replace('**','\x00').replace('*\x00','\x00').replace('\x00','**') if False else out
if __name__=='__main__':
    d,secs=load(sys.argv[1]); out=open(sys.argv[2],'w')
    for k,s in enumerate(secs):
        out.write(f"\n### [{k}] {s['ch'] or ''} :: {s['title']}\n")
        for p in s['paras']:
            t=rtext(p)
            if t.strip(): out.write(t+"\n")
