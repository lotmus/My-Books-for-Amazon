import collections,re,sys,io
from rev15_view import *
L,ch=chapters()
touched=['19','20','21','23','24','25','26']
text=[(n,p) for n,(i,j,h,ps) in ch.items() if n in touched for p in ps]
def toks(s): return re.findall(r"[A-Za-z'’]+",s.lower())
for N in (5,4):
    c=collections.defaultdict(list)
    for n,p in text:
        t=toks(p); seen=set()
        for k in range(len(t)-N+1):
            g=' '.join(t[k:k+N])
            if g not in seen: seen.add(g); c[g].append(n)
    rep=[(g,v) for g,v in c.items() if len(v)>=2]; rep.sort(key=lambda x:-len(x[1]))
    print('N',N,len(rep))
    for g,v in rep[:18]: print(len(v),g,v)
body='\n'.join(p for n,p in text)
for w in ['looked at','for a moment','as though','a man who','very','quite','rather','carefully']:
    print(w,len(re.findall(w,body)))
