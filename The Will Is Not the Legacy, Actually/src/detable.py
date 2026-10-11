"""Kindle rule: no Word tables. Convert every markdown table in md/ into label-then-text lists."""
import re,glob
def cells(l): return [c.strip() for c in l.strip().strip('|').split('|')]
def conv(rows):
    H=rows[0]; data=[r for r in rows[1:] if any(c for c in r)]
    out=[]
    if not data:
        out.append('For each item, note:')
        out.append('')
        for h in H: out.append(f'- {h}: ______')
        return out
    for r in data:
        r=r+['']*(len(H)-len(r))
        lab=r[0].replace('**','')
        if len(H)==2:
            out.append(f'- **{lab}:** {r[1]}')
        else:
            parts=[f'{H[k]}: {r[k]}' for k in range(1,len(H)) if r[k]]
            out.append(f'- **{lab}.** '+'; '.join(parts)+('.' if parts and not parts[-1].endswith(('.','?','!')) else ''))
    return out
for f in sorted(glob.glob('md/*.md')):
    L=open(f).read().split('\n'); o=[]; i=0; n=0
    while i<len(L):
        if L[i].startswith('|'):
            rows=[]
            while i<len(L) and L[i].startswith('|'):
                c=cells(L[i])
                if not all(re.fullmatch(r':?-+:?',x) for x in c if x): rows.append(c)
                i+=1
            o+=conv(rows); n+=1
        else: o.append(L[i]); i+=1
    if n: open(f,'w').write('\n'.join(o)); print(f,n,'tables converted')
