import re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
t=open('The Department of Historical Corrections - REV15.md',encoding='utf-8').read().split('\n')
for i,l in enumerate(t):
    for m in re.finditer(r'[Cc]hapters? \d+(?:(?:,| and| to) \d+)*',l): print(i+1,m.group(0),'|',l[max(0,m.start()-40):m.end()+30])
for i,l in enumerate(t):
    if l.startswith('## 19') or l.startswith('## 20 ') : print('H',i+1,l)
    if l.startswith('The knock came at eleven'): print('knock',i+1)
