import io,sys,re,collections
from secs import sections,norm
from uscan import sents
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
secs=sections('../The_Universe_Actually__REV11.docx')
blocks=['Arrow of Time','Black Holes','Quantum Foundations','Dark Sector','Earth Climate History','Human Evolution']
flat={}
for k,s in enumerate(secs):
    if s['i']<2442 and s['lvl']==2: flat.setdefault(norm(s['title']),[]).append(k)
def ssent(s): return set(norm(x) for i,t in s['paras'] for x in sents(t) if len(norm(x).split())>=4)
for k,s in enumerate(secs):
    if s['title'] in blocks and s['i']>=2442:
        print('=== BLOCK',s['title'],s['i'])
        subs=[]; cur=None
        for i,t in s['paras']:
            m=re.fullmatch(r'\*\*(.+)\*\*',t.strip())
            if m: cur=[m.group(1),[]]; subs.append(cur)
            elif cur and t.strip(): cur[1].append(t)
        for name,ps in subs:
            ss=set(norm(x) for t in ps for x in sents(t) if len(norm(x).split())>=4)
            cands=flat.get(norm(name),[])
            best=None
            for c in cands:
                o=len(ss&ssent(secs[c]))
                best=(c,o) if best is None or o>best[1] else best
            # any section containing them
            print('  %-50s sents %2d  flat match: %s'%(name[:50],len(ss),('%d overlap %d (%s)'%(secs[best[0]]['i'],best[1],secs[best[0]]['title'][:25])) if best else 'NONE'))
