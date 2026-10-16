from rev13_view import *
import re,sys
L,ch=chapters()
pats=sys.argv[1:]
for n,(i,j,h,ps) in ch.items():
    for k,p in enumerate(ps):
        for pat in pats:
            for m in re.finditer(pat,p,flags=re.I):
                s=max(0,m.start()-70); e=min(len(p),m.end()+70)
                print(f'{n}[{k}] {pat}: …{p[s:e]}…')
