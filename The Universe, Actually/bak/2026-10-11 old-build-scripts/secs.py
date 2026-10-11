import docx,io,sys,re,collections
def sn(p): return p.style.name if p.style is not None else ''
def sections(path):
    ps=docx.Document(path).paragraphs
    secs=[];cur={'i':-1,'lvl':0,'title':'<front>','paras':[]}
    for i,p in enumerate(ps):
        if sn(p).startswith('Heading'):
            cur={'i':i,'lvl':int(sn(p)[-1]),'title':p.text,'paras':[]};secs.append(cur)
        else: cur['paras'].append((i,p.text))
    return secs
def norm(s): return re.sub(r'[^a-z0-9 ]','',re.sub(r'[’‘“”"\']','',s.lower())).strip()
if __name__=='__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    secs=sections(sys.argv[1])
    by=collections.defaultdict(list)
    for s in secs: by[s['title']].append(s)
    for t,v in by.items():
        if len(v)>1 and v[0]['lvl']==2:
            a=[norm(x[1]) for x in v[0]['paras'] if x[1].strip()]
            for o in v[1:]:
                b=[norm(x[1]) for x in o['paras'] if x[1].strip()]
                same=sum(1 for x in b if x in set(a))
                print('%-55s at %d,%d  paras %d/%d identical %d'%(t[:55],v[0]['i'],o['i'],len(a),len(b),same))
