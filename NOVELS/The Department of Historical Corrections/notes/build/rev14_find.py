import re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
t=open('../../The Department of Historical Corrections - REV14.md',encoding='utf-8').read().split('\n')
end=next(i for i,l in enumerate(t) if l.startswith('## Lessons'))
pat=sys.argv[1]
for i,l in enumerate(t[:end]):
    for m in re.finditer(pat,l):
        print(i+1,'|',l[max(0,m.start()-80):m.end()+50])
