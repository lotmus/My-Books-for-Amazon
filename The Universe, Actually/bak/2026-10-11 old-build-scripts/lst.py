import io,sys,json
from secs import norm
from uscan import sents
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
kept=json.load(open('pool.json',encoding='utf-8'))
def ss(p): return set(norm(x) for t in p for x in sents(t) if len(norm(x).split())>=4)
seen=set()
for sec in kept:
    s=ss(sec['paras']); o=len(s&seen)/len(s) if s else 0
    if sec['origin'].startswith('block') or o>=0.25:
        print(sec['id'],sec['origin'],'|',sec['title'],'| words',sum(len(t.split()) for t in sec['paras']),'| overlap %.2f'%o)
    seen|=s
