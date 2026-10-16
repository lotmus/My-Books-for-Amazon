from rev13_view13 import *
import collections,re
L,ch=chapters()
text=[]
for n,(i,j,h,ps) in ch.items():
    for p in ps: text.append((n,p))
def toks(s): return re.findall(r"[A-Za-z’']+",s.lower())
# n-grams
for N in (6,5):
    c=collections.defaultdict(list)
    for n,p in text:
        t=toks(p)
        seen=set()
        for k in range(len(t)-N+1):
            g=' '.join(t[k:k+N])
            if g not in seen: seen.add(g); c[g].append(n)
    rep=[(g,v) for g,v in c.items() if len(v)>=3]
    rep.sort(key=lambda x:-len(x[1]))
    print('N=',N,len(rep))
    for g,v in rep[:45]: print(len(v),g,v[:8])

