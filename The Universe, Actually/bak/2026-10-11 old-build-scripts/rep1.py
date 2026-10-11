import io,sys,re,collections
from secs import sections,norm
from uscan import sents
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
secs=sections('../The_Universe_Actually__REV11.docx')
drop=set(); by={}
for k,s in enumerate(secs):
    if s['lvl']==2:
        key=(s['title'],tuple(norm(t) for _,t in s['paras'] if t.strip()))
        if key in by: drop.add(k)
        else: by[key]=k
print('identical dup sections dropped:',len(drop), sum(len(t.split()) for k in drop for _,t in secs[k]['paras']))
occ=collections.defaultdict(list)
for k,s in enumerate(secs):
    if k in drop: continue
    for i,t in s['paras']:
        for st in sents(t):
            n=norm(st)
            if len(n.split())>=4: occ[n].append((k,st))
rep=collections.Counter(); words=collections.Counter(); tot=0
for n,v in occ.items():
    if len(v)>1:
        for k,st in v[1:]:
            rep[secs[k]['title']]+=1; words[secs[k]['title']]+=len(st.split()); tot+=len(st.split())
print('remaining repeat-occurrence words',tot,'sentences',sum(rep.values()))
for t,w in words.most_common(30): print(w,rep[t],t)
