import io,sys,json,re,collections,random
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
pool=json.load(open('pool.json',encoding='utf-8'))
BS=chr(92)
MATH=re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]',re.S)
cmds=collections.Counter(); ex=[]; n=0
for s in pool:
    for t in s['paras']:
        for m in MATH.finditer(t):
            n+=1; body=m.group(1) or m.group(2)
            for c in re.findall(r'\\[A-Za-z]+',body): cmds[c]+=1
            ex.append(body)
print(n,'math spans'); print(cmds.most_common(100))
random.seed(1)
for e in random.sample(ex,45): print('  ',e)
st=0
for s in pool:
    for t in s['paras']:
        r=MATH.sub('',t)
        if BS in r or '$' in r:
            st+=1; print('STRAY',r[:140])
print(st)
