import io,sys
from model import build_model
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
parts,front,log=build_model()
want=[int(x) for x in sys.argv[1:]]
n=0
for p in parts:
    for c in p['chapters']:
        n+=1
        if n not in want: continue
        print('#### CH',n,c['title'],'(part %s)'%p['title'])
        if c['leadsec']:
            print('[LEAD %s]'%c['leadsec']['id'])
            for i,t in enumerate(c['leadsec']['paras']): print('  %d. %s'%(i,t))
        for s in c['secs']:
            print('== [%s] %s'%(s['id'],s['title']))
            for i,t in enumerate(s['paras']): print('  %d. %s'%(i,t))
