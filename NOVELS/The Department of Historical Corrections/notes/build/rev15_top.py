import re
t=open('The Department of Historical Corrections - REV15.md',encoding='utf-8').read().split('\n')
end=next(i for i,l in enumerate(t) if l.startswith('## Lessons'))
idx=[i for i,l in enumerate(t[:end]) if re.match(r'## \d+ ',l)]
r=[]
for k,i in enumerate(idx):
    j=idx[k+1] if k+1<len(idx) else end
    r.append((sum(len(x.split()) for x in t[i+1:j]),t[i][:30]))
print(sorted(r,reverse=True)[:5])
