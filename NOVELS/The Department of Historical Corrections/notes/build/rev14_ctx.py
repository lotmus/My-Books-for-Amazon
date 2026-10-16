import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
t=open('../../The Department of Historical Corrections - REV14.md',encoding='utf-8').read().split('\n')
for n in map(int,sys.argv[1:]):
    print('---',n); 
    for k in (n-2,n-1,n,n+1,n+2): print(k+0, t[k-1][:230] if k-1<len(t) else '')
