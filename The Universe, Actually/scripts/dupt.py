import io,sys,json,collections
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
kept=json.load(open('pool.json',encoding='utf-8'))
c=collections.defaultdict(list)
for s in kept: c[s['title']].append(s)
for t,v in c.items():
    if len(v)>1:
        print(t)
        for s in v: print('   ',s['id'],s['origin'],sum(len(x.split()) for x in s['paras']),'|',s['paras'][0][:110] if s['paras'] else '')
