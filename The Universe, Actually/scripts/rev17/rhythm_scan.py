"""List paragraphs with a run of three or more consecutive short sentences (<= 9 words each). Usage: python rhythm_scan.py docx [show]"""
import docx,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
d=docx.Document(sys.argv[1]); W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
hits=[];ch=None
for i,p in enumerate(d.element.body.iter(W+'p')):
    s=p.find(W+'pPr'); s=s.find(W+'pStyle') if s is not None else None; s=s.get(W+'val') if s is not None else ''
    t=''.join((x.text or '') for x in p.iter(W+'t'))
    if s=='Heading2':
        m=re.match(r'(\d+)\. ',t); ch=int(m.group(1)) if m else None
    if s or len(t.split())<25: continue
    ss=[x for x in re.split(r'(?<=[.!?])\s+',t.strip()) if x]
    run=best=0
    for x in ss:
        if len(x.split())<=9: run+=1; best=max(best,run)
        else: run=0
    if best>=3: hits.append((ch,i,best,t))
print(len(hits),'paragraphs with a run of 3+ short sentences')
import collections
c=collections.Counter(h[0] for h in hits); print(sorted(c.items(),key=lambda x:-x[1])[:25])
if len(sys.argv)>2:
    for ch,i,b,t in hits[:int(sys.argv[2])]: print('\n[ch %s #%d run %d]'%(ch,i,b),t)
