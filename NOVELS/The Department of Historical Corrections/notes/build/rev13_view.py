import re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
P='../../The Department of Historical Corrections - REV12.md'
def chapters(path=P):
    t=open(path,encoding='utf-8').read()
    L=t.split('\n')
    idx=[i for i,l in enumerate(L) if re.match(r'## \d+[ab]? ',l)]
    out={}
    for k,i in enumerate(idx):
        j=idx[k+1] if k+1<len(idx) else next(m for m in range(i,len(L)) if L[m].startswith('## Lessons'))
        out[L[i].split()[1]]=(i,j,L[i],[p for p in L[i+1:j] if p.strip()])
    return L,out
if __name__=='__main__':
    L,ch=chapters()
    for n in sys.argv[1:]:
        i,j,h,ps=ch[n]
        print(h, sum(len(p.split()) for p in ps),'words')
        for k,p in enumerate(ps): print(f'[{k}] {p}')
