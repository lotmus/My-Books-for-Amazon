import re, sys, subprocess
def old(n):
    return subprocess.run(['git','show','HEAD:scripts/prologue%02d.txt'%n],capture_output=True,text=True,cwd=sys.argv[1]).stdout
def sections(txt):
    meta={}; secs=[]; cur=None
    for line in txt.split('\n'):
        m=re.match(r'^(TITLE|TAGLINE|NUM|NEXT):\s*(.*)$',line)
        if m and cur is None: meta[m.group(1)]=m.group(2); continue
        if line.startswith('# '):
            cur=[line[2:].strip(),[]]; secs.append(cur); continue
        if cur is not None: cur[1].append(line)
    return meta,secs
def body(lines): return '\n'.join(lines).strip('\n')
def sub_section(howto,name):
    # return dict of ## subsections in howto
    out={'_intro':[]}; key='_intro'
    for l in howto:
        if l.startswith('## '): key=l[3:].strip(); out[key]=[]; continue
        out[key].append(l)
    return out
def rows(lines): return [l for l in lines if l.startswith('|')]
def shift_refs(text, sec_off, we_off, ex_off):
    text=re.sub(r'Section (\d+)(\.\d+)?', lambda m:'Section %d%s'%(int(m.group(1))+sec_off,m.group(2) or ''), text)
    text=re.sub(r'Worked example (\d+)', lambda m:'Worked example %d'%(int(m.group(1))+we_off), text)
    text=re.sub(r'Exercise (\d+)', lambda m:'Exercise %d'%(int(m.group(1))+ex_off), text)
    text=re.sub(r'Exercises (\d+)[–-](\d+)', lambda m:'Exercises %d–%d'%(int(m.group(1))+ex_off,int(m.group(2))+ex_off), text)
    return text
def merge(A,B,head,drop_b=(),figs={},intro=None,refmap=()):
    ma,sa=sections(A); mb,sb=sections(B)
    def split(secs):
        d={'body':[],'conn':None,'sum':None,'ex':None,'sol':None,'how':None}
        for t,l in secs:
            if t.startswith('How to use'): d['how']=l
            elif t.startswith('Connections'): d['conn']=l
            elif t=='Summary': d['sum']=l
            elif t=='Exercises': d['ex']=l
            elif t=='Solutions': d['sol']=l
            elif t=='Mastery checklist': pass
            else: d['body'].append([t,l])
        return d
    da,db=split(sa),split(sb)
    nsec_a=len(da['body']); nwe_a=sum(body(l).count('### Worked example') for _,l in da['body'])
    nex_a=len(rows(da['ex']))-1
    out=[head.strip(),'','# How to use this prologue','',intro.strip(),'','## Learning objectives','']
    for d in (da,db):
        h=sub_section(d['how'],'')
        for l in h.get('Learning objectives',[]):
            if l.startswith('- '): out+= [l,'']
    out+=['## Notation and conventions','','@widths 2160 7632','| Symbol | Meaning |']
    seen=set()
    for d in (da,db):
        h=sub_section(d['how'],'')
        for r in rows(h.get('Notation and conventions',[]))[1:]:
            if r not in seen: seen.add(r); out.append(r)
    out.append('')
    k=0
    for which,d in (('a',da),('b',db)):
        for t,l in d['body']:
            num=re.match(r'^(\d+)\s+(.*)$',t)
            title=num.group(2) if num else t
            if which=='b' and title in drop_b: continue
            k+=1
            txt=body(l)
            if which=='b': txt=shift_refs(txt,nsec_a,nwe_a,nex_a)
            txt=re.sub(r'^## (\d+)\.(\d+)', lambda m:'## %d.%s'%(k,m.group(2)), txt, flags=re.M)
            # worked example renumber in b
            if which=='b':
                txt=re.sub(r'^### Worked example (\d+)', lambda m:'### Worked example %d'%(int(m.group(1))+nwe_a), txt, flags=re.M)
            out+=['# %d %s'%(k,title),'',txt,'']
    # connections
    out+=['# Connections to QED','','@widths 3264 6528']
    cr=rows(da['conn']); out.append(cr[0]); out+=cr[1:]+rows(db['conn'])[1:]; out.append('')
    # summary
    out+=['# Summary','']
    items=[re.sub(r'^\d+\.\s+','',l) for d in (da,db) for l in d['sum'] if re.match(r'^\d+\.\s',l)]
    for i,it in enumerate(items): out+=['%d. %s'%(i+1,it),'']
    # exercises
    out+=['# Exercises','','@widths 720 9072','| No | Problem |']
    exs=rows(da['ex'])[1:]+[shift_refs(r,nsec_a,nwe_a,nex_a) for r in rows(db['ex'])[1:]]
    for i,r in enumerate(exs):
        out.append(re.sub(r'^\|\s*\d+\s*\|','| %d |'%(i+1),r))
    out+=['','# Solutions','']
    sols=[l for l in da['sol'] if re.match(r'^\*\*\d+\.\*\*',l)]
    solb=[shift_refs(l,nsec_a,nwe_a,nex_a) for l in db['sol'] if re.match(r'^\*\*\d+\.\*\*',l)]
    for i,l in enumerate(sols+solb):
        out+=[re.sub(r'^\*\*\d+\.\*\*','**%d.**'%(i+1),l),'']
    s='\n'.join(out)
    for a,b in refmap: s=s.replace(a,b)
    # figures
    def figrep(m):
        idx=figrep.i; figrep.i+=1
        return figs.get(idx,'')
    figrep.i=0
    s=re.sub(r'FIG:\n.*?\nENDFIG',figrep,s,flags=re.S)
    return re.sub(r'\n{3,}','\n\n',s)
