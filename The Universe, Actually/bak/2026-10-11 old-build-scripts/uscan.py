# -*- coding: utf-8 -*-
# Scan a docx for repeated sentences (exact + near) ignoring headings. Works with unstyled paragraphs.
import io, sys, re, collections, docx
def sn(p): return p.style.name if p.style is not None else ''
def sents(text):
    parts = re.split(r'(?<=[.!?])["”’)]*\s+(?=["“‘(]?[A-Z0-9“])', text.replace('\n',' '))
    return [p.strip() for p in parts if p.strip()]
def norm(s): return re.sub(r'[^a-z0-9 ]','',re.sub(r'[’‘“”"\']','',s.lower())).strip()
def load(path, start=0):
    ps = docx.Document(path).paragraphs
    items=[]
    for i,p in enumerate(ps):
        if i<start or sn(p).startswith('Heading'): continue
        for s in sents(p.text): items.append((i,s))
    return ps, items
def scan(items, min_exact=4, min_fuzzy=7, thr=0.6):
    occ=collections.defaultdict(list)
    for i,s in items:
        n=norm(s)
        if len(n.split())>=min_exact: occ[n].append((i,s))
    exact=[(v[0][0],[i for i,_ in v],v[0][1]) for n,v in occ.items() if len(v)>1]
    grams={}; index=collections.defaultdict(set)
    for k,(i,s) in enumerate(items):
        w=norm(s).split()
        if len(w)>=min_fuzzy:
            g=set(tuple(w[j:j+4]) for j in range(len(w)-3)); grams[k]=g
            for x in g: index[x].add(k)
    near=[]
    for k,g in grams.items():
        cand=collections.Counter()
        for x in g:
            for m in index[x]:
                if m>k: cand[m]+=1
        for m,c in cand.items():
            if c<2 or norm(items[k][1])==norm(items[m][1]): continue
            h=grams[m]; cont=len(g&h)/min(len(g),len(h))
            if cont>=thr: near.append((items[k][0],cont,items[m][0],items[k][1],items[m][1]))
    return sorted(exact),sorted(near)
if __name__=='__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    ps,items=load(sys.argv[1])
    exact,near=scan(items)
    words=sum(len(s.split()) for i,s in items)
    # words in later-occurrence exact duplicates
    seen=set(); dupw=0
    for i,s in items:
        n=norm(s)
        if len(n.split())<4: continue
        if n in seen: dupw+=len(s.split())
        seen.add(n)
    print('body words',words,'| words in repeat-occurrences (exact):',dupw)
    print('EXACT repeated sentences:',len(exact),' NEAR pairs:',len(near))
    if len(sys.argv)>2:
        for first,idx,s in exact: print('  x%d %s | %s'%(len(idx),idx,s[:150]))
        for a,c,b,sa,sb in near: print('  NEAR %.2f [%d,%d]\n   A: %s\n   B: %s'%(c,a,b,sa[:160],sb[:160]))
