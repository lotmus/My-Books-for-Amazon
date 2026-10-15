import sys,re,math,collections
from model16 import load,text
d,secs=load(sys.argv[1])
P=[]
for s in secs:
    if not s['ch'] or 'Worked' in s['title']: continue
    for p in s['paras']:
        t=text(p)
        if len(t.split())>=40: P.append((s['ch'],s['title'],t))
stop=set("the a an of and to in is it that for on as with by this are be was or at from its which not but have has can more than one they their what into we our so if all there were these when how also only no would been like other about any most them out even itself much does who same each very such two where just then".split())
docs=[collections.Counter(w for w in re.findall(r"[a-z][a-z\-]+",t.lower()) if w not in stop and len(w)>2) for _,_,t in P]
df=collections.Counter(); [df.update(set(c)) for c in docs]; N=len(docs)
V=[]
for c in docs:
    v={k:(1+math.log(n))*math.log(N/df[k]) for k,n in c.items()}; nm=math.sqrt(sum(x*x for x in v.values())) or 1
    V.append({k:x/nm for k,x in v.items()})
inv=collections.defaultdict(list)
for i,v in enumerate(V):
    for k,x in v.items(): inv[k].append((i,x))
pairs=[]
for i,v in enumerate(V):
    acc=collections.Counter()
    for k,x in v.items():
        if df[k]>200: continue
        for j,y in inv[k]:
            if j>i: acc[j]+=x*y
    for j,c in acc.items():
        if c>float(sys.argv[2]): pairs.append((c,i,j))
pairs.sort(reverse=True)
for c,i,j in pairs[:int(sys.argv[3])]:
    same='SAME' if P[i][0]==P[j][0] else ''
    print(f"{c:.2f} {same} {P[i][0][:22]}/{P[i][1][:28]} || {P[j][0][:22]}/{P[j][1][:28]}")
print(len(pairs))
if len(sys.argv)>4:
    for c,i,j in pairs[:int(sys.argv[4])]:
        print('\n==',f"{c:.2f}"); print('A',P[i][1],'::',P[i][2]); print('B',P[j][1],'::',P[j][2])
