"""One-time merge of Life: Evolution (31 ch.) and The Copy Is Never Exact (prologue + 46 ch.)
into the chapter sources of Life, Actually. Renumbers chapter and figure references,
applies the editorial patches in patches.py, writes chapters/*.md."""
import re, glob, os, sys, importlib.util
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'out','chapters')
EVO=os.path.join(HERE,'evo'); GENSRC=os.path.join(HERE,'..','src','z','chapters')
spec=importlib.util.spec_from_file_location('patches',os.path.join(HERE,'patches.py')); P=importlib.util.module_from_spec(spec); spec.loader.exec_module(P)

def evo_new(n):
    if n<=8: return str(n)
    if n==9: return '§E9§'
    if n<=30: return str(n-1)
    return '§E31§'
def gen_new(n): return str(n+30)

NUMLIST=re.compile(r'\b([Cc]hapters?) (\d+)((?:(?:,| and| or| to|–)\s?\d+)*)(?!\d| bankruptcy)')
def renum(text,f):
    def rep(m):
        rest=re.sub(r'\d+',lambda k:f(int(k.group(0))),m.group(3))
        return f"{m.group(1)} {f(int(m.group(2)))}{rest}"
    return NUMLIST.sub(rep,text)

chapters={}   # new number -> dict(title, body)
# ---- Evolution
for path in sorted(glob.glob(os.path.join(EVO,'*.md'))):
    e=int(os.path.basename(path)[:2])
    if e in (9,31): continue
    lines=open(path,encoding='utf-8').read().splitlines()
    title=[l for l in lines if l.startswith('## ')][0][3:]
    body='\n'.join(l for l in lines if not l.startswith(('## ','<!--'))).strip()
    chapters[int(evo_new(e))]={'title':title,'body':renum(body,evo_new),'src':f'Life: Evolution ch. {e}'}
# ---- Genetics
FIGCAP=P.GEN_FIG_CAPTIONS
for path in sorted(glob.glob(os.path.join(GENSRC,'*.md'))):
    if os.path.basename(path).startswith('12_'): continue
    cur=None;buf=[]
    def flush():
        if cur is not None:
            chapters[cur[0]]={'title':cur[1],'body':'\n'.join(buf).strip(),'src':cur[2]}
    for line in open(path,encoding='utf-8').read().splitlines():
        if line.startswith('# '):
            flush(); cur=None; buf=[]; continue
        if line.startswith('## '):
            t=line[3:].strip()
            m=re.match(r'(\d+)\.\s+(.*)',t)
            if m: n=int(m.group(1)); title=m.group(2)
            elif t.lower().startswith('prologue'): n=0; title=t.split('—',1)[1].strip()
            else:
                flush(); cur=None; buf=[]; continue
            flush(); buf=[]; cur=(n+30,title,f'The Copy Is Never Exact ch. {n}' if n else 'The Copy Is Never Exact, prologue'); continue
        if cur is None: continue
        if line.startswith('!['):
            m=re.match(r'!\[Figure (\d+)\.',line); old=int(m.group(1)); new=old+1
            ext='jpg' if os.path.exists(os.path.join(HERE,'figs',f'fig{new:02d}.jpg')) else 'png'
            line=f'![Figure {new}. {FIGCAP[old]}](figures/figs/fig{new:02d}.{ext})'
        buf.append(renum(line,gen_new))
    flush()
# ---- section headings for former Genetics chapters
spec2=importlib.util.spec_from_file_location('genheads',os.path.join(HERE,'genheads.py')); GH=importlib.util.module_from_spec(spec2); spec2.loader.exec_module(GH)
for n,heads in GH.H.items():
    paras=[p for p in chapters[n]['body'].split('\n\n') if p.strip()]
    hd=dict(heads); out=[]
    for i,p in enumerate(paras):
        if i in hd:
            out.append('### '+hd[i])
            if p.strip()=='---': continue
        if p.strip()=='---': continue
        out.append(p)
    chapters[n]['body']='\n\n'.join(out)
# ---- new chapters (Life Elsewhere) from work/new/*.md if present
for path in sorted(glob.glob(os.path.join(HERE,'new','*.md'))):
    lines=open(path,encoding='utf-8').read().splitlines()
    n=int(os.path.basename(path)[:2])
    title=[l for l in lines if l.startswith('## ')][0][3:]
    body='\n'.join(l for l in lines if not l.startswith('## ')).strip()
    chapters[n]={'title':title,'body':body,'src':'new'}
# ---- patches
missing=[]
for n,items in P.PATCHES.items():
    for old,new in items:
        c=chapters[n]
        if old=='__TITLE__': c['title']=new; continue
        if old.startswith('re:'):
            b2,k=re.subn(old[3:],new,c['body'],flags=re.S)
            if k!=1: missing.append((n,k,old[:70])); continue
            c['body']=b2; continue
        k=c['body'].count(old)
        if k!=1: missing.append((n,k,old[:70])); continue
        c['body']=c['body'].replace(old,new)
for n,items in getattr(P,'SECTION_REPLACE',{}).items():
    for head,new in items:   # replace whole '### head' section (up to next ###) ; new=None deletes
        c=chapters[n]; b=c['body']
        m=re.search(r'(?ms)^### '+re.escape(head)+r'\n.*?(?=^### |\Z)',b)
        if not m: missing.append((n,0,'SECTION '+head)); continue
        c['body']=b[:m.start()]+(new.strip()+'\n\n' if new else '')+b[m.end():]
if missing:
    print('PATCH PROBLEMS:'); [print(' ',x) for x in missing]
# ---- house title style: 'Main — Sub' instead of 'Main: Sub'
for n,c in chapters.items():
    c['title']=re.sub(r'^([^:]+): ',r'\1 — ',c['title'],count=1)
# ---- write part files
os.makedirs(OUT,exist_ok=True)
for f in glob.glob(os.path.join(OUT,'[0-9][0-9]_Part*.md')): os.remove(f)
for i,(roman,name,fname,first,last) in enumerate(P.PARTS,1):
    if not any(n in chapters for n in range(first,last+1)): continue
    parts=[f'# PART {roman} — {name}','']
    intro=P.PART_INTROS.get(roman)
    if intro: parts+=[intro,'']
    for n in range(first,last+1):
        if n not in chapters: parts+=[f'## {n}. [MISSING]','']; continue
        parts+=[f"## {n}. {chapters[n]['title']}",'',chapters[n]['body'],'']
    open(os.path.join(OUT,f'{i:02d}_Part_{roman}_{fname}.md'),'w',encoding='utf-8').write('\n'.join(parts).rstrip()+'\n')
import json
json.dump({n:{'title':c['title'],'src':c['src']} for n,c in sorted(chapters.items())},open(os.path.join(HERE,'out','chapter_map.json'),'w'),indent=1,ensure_ascii=False)
print('chapters',len(chapters),'max',max(chapters))
