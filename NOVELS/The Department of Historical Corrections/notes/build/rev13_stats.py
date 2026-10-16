import re,sys,io
import rev13_view as v
L,ch=v.chapters(sys.argv[1])
tot=0
for n,(i,j,h,ps) in ch.items():
    w=sum(len(p.split()) for p in ps); tot+=w
    if n in ('1','6','7','9','12','15','22','23','31','32','34','35','36','37','38','39') : print(n,h[3:45],w)
print('body',tot,'chapters',len(ch))
t=open(sys.argv[1],encoding='utf-8').read()
i=t.index('## Lessons'); j=t.index('## A Note to Readers')
print('appendix words',len(t[i:j].split()))
bad='Tr'+'ump'
print('banned hits',len(re.findall(bad,t,flags=re.I)))
body='\n'.join(p for n,(a,b,h,ps) in ch.items() for p in ps)
for p in ['as though','as if','a man who','with the air of','for a moment','like a ','like an ','Bell','a woman who','very still']:
    print(p,len(re.findall(re.escape(p),body)), 'whole', len(re.findall(re.escape(p),t)))

