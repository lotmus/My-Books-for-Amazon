import re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
t=open('../../The Department of Historical Corrections - REV14.md',encoding='utf-8').read()
L=t.split('\n'); end=next(i for i,l in enumerate(L) if l.startswith('## Lessons'))
idx=[i for i,l in enumerate(L[:end]) if re.match(r'## \d+ ',l)]
tot=0
for k,i in enumerate(idx):
    j=idx[k+1] if k+1<len(idx) else end
    w=sum(len(x.split()) for x in L[i+1:j]); tot+=w
    n=int(L[i].split()[1])
    if 19<=n<=25 or n>=31: print(L[i][:38],w)
print('body',tot, 'appendix', len(t[t.index('## Lessons'):t.index('## A Note to Readers')].split()))
body='\n'.join(L[:end])
for p in ['looked at him','looked at her','looked at it','looked at them','for a moment','a man who','as though','as if','like a ','like an ','very still','held still','carefully','briefly','slightly','entirely']:
    print(p,len(re.findall(p,body)))
print('banned',len(re.findall('Tr'+'ump',t,flags=re.I)),'Bell',t.count('Bell'),'triple',t.count('\n\n\n'))
