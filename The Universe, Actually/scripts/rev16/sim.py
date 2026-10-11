import sys,re,math,collections
from model16 import load,text
d,secs=load(sys.argv[1])
S=[s for s in secs if s['ch']]
docs=[]
stop=set("the a an of and to in is it that for on as with by this are be was or at from its which not but have has can more than one they their what into we our you so if all there were these when how also only no would been like other about any most them out even itself much does who same each very such two where just then".split())
for s in S:
    w=[x for x in re.findall(r"[a-z][a-z\-]+",' '.join(text(p) for p in s['paras']).lower()) if x not in stop and len(x)>2]
    docs.append(collections.Counter(w))
df=collections.Counter(); [df.update(set(c)) for c in docs]
N=len(docs)
vec=[]
for c in docs:
    v={k:(1+math.log(n))*math.log(N/df[k]) for k,n in c.items()}
    norm=math.sqrt(sum(x*x for x in v.values())) or 1
    vec.append({k:x/norm for k,x in v.items()})
pairs=[]
for i in range(N):
    for j in range(i+1,N):
        if S[i]['ch']==S[j]['ch']: continue
        a,b=vec[i],vec[j]
        if len(a)>len(b): a,b=b,a
        c=sum(x*b.get(k,0) for k,x in a.items())
        if c>0.30: pairs.append((c,i,j))
pairs.sort(reverse=True)
for c,i,j in pairs[:int(sys.argv[2]) if len(sys.argv)>2 else 80]:
    wi=sum(len(text(p).split()) for p in S[i]['paras']); wj=sum(len(text(p).split()) for p in S[j]['paras'])
    print(f"{c:.2f} | {S[i]['ch'][:30]} / {S[i]['title'][:40]} ({wi}) || {S[j]['ch'][:30]} / {S[j]['title'][:40]} ({wj})")
