import io,sys,json,re,collections
def key(t): return re.sub(r'[^a-z0-9]','',t.lower().replace('’',"'").replace("'",''))
def load_map(path='structure.txt'):
    parts=[]
    for line in open(path,encoding='utf-8'):
        line=line.rstrip('\n')
        if not line or line.startswith('#'): continue
        if line.startswith('=PART|'):
            _,t,tag=line.split('|'); parts.append({'title':t,'tag':tag,'chapters':[]})
        elif line.startswith('=='):
            t=line[2:]; lead=False
            if t.startswith('*'): lead=True; t=t[1:]
            ref=None
            if '@' in t: t,ref=t.split('@')
            parts[-1]['chapters'].append({'title':t,'lead':lead,'leadref':ref,'items':[]})
        else: parts[-1]['chapters'][-1]['items'].append(line)
    return parts
def resolve(parts,pool):
    byk=collections.defaultdict(list); byid={}
    for s in pool: byk[key(s['title'])].append(s); byid[s['id']]=s
    used=set(); problems=[]
    for p in parts:
        for c in p['chapters']:
            c['secs']=[]; c['leadsec']=None
            if c['lead']:
                ls=byid.get(int(c['leadref'])) if c['leadref'] else None
                if ls is None: problems.append(('lead',c['title']))
                else: c['leadsec']=ls; used.add(ls['id'])
            for it in c['items']:
                it,_,newt=it.partition('=')
                t,_,ref=it.partition('@')
                if ref: s=byid.get(int(ref))
                else:
                    cands=[x for x in byk.get(key(t),[]) if x['id'] not in used]
                    s=cands[0] if cands else None
                if s is None: problems.append(('missing',it)); continue
                if s['id'] in used: problems.append(('dup-use',it)); continue
                used.add(s['id']); s=dict(s)
                if newt: s['title']=newt
                c['secs'].append(s)
    un=[s for s in pool if s['id'] not in used]
    return problems,un
if __name__=='__main__':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
    parts=load_map(); pool=json.load(open('pool.json',encoding='utf-8'))
    problems,un=resolve(parts,pool)
    print('problems:',problems)
    print('unassigned',len(un))
    for s in un: print(' ',s['id'],s['origin'],'|',s['title'],'|',sum(len(t.split()) for t in s['paras']))
