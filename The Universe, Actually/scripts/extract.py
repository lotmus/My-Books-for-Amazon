# Build pool of unique sections from REV11 -> pool.json
import io,sys,re,json,collections
from secs import sections,norm
from uscan import sents
SRC='../The_Universe_Actually__REV11.docx'
secs=sections(SRC)
BLOCKS={'Arrow of Time','Black Holes','Quantum Foundations','Dark Sector','Earth Climate History','Human Evolution'}
def sset(paras): return set(norm(x) for t in paras for x in sents(t) if len(norm(x).split())>=4)
pool=[]   # dicts: id,title,paras,origin
# first pass: flat H2 sections (not block containers, not block-trailing copies)
blockidx=[k for k,s in enumerate(secs) if s['lvl']==2 and s['title'] in BLOCKS and s['i']>=2442]
for k,s in enumerate(secs):
    if s['lvl']!=2 or k in blockidx: continue
    pool.append({'id':s['i'],'title':s['title'],'paras':[t for _,t in s['paras'] if t.strip()],'origin':'flat' if s['i']<3015 else 'tail'})
# block subsections
for k in blockidx:
    s=secs[k]; cur=None
    for i,t in s['paras']:
        m=re.fullmatch(r'\*\*(.+)\*\*',t.strip())
        if m: cur={'id':i,'title':m.group(1),'paras':[],'origin':'block:'+s['title']}; pool.append(cur)
        elif cur is not None and t.strip(): cur['paras'].append(t)
        elif t.strip(): print('orphan',s['title'],t[:60])
json.dump(pool,open('pool_raw.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(pool),'sections in raw pool')
# dedupe: a later section is dropped if >=80% of its sentences already occur in earlier kept sections
seen=set(); kept=[]; dropped=[]
for sec in pool:
    ss=sset(sec['paras'])
    if ss and len(ss&seen)/len(ss)>=0.8 and sec['title'] not in ('Contents',):
        dropped.append(sec); continue
    kept.append(sec); seen|=ss
print('kept',len(kept),'dropped',len(dropped), 'dropped words',sum(len(t.split()) for d in dropped for t in d['paras']))
json.dump(kept,open('pool.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
json.dump(dropped,open('dropped.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
cnt=collections.Counter(d['origin'].split(':')[0] for d in dropped); print(cnt)
