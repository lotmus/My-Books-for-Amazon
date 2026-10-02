import docx,re,json
d=docx.Document('src/evo.docx'); ps=d.paragraphs
CONN=('First','Second','Third','Fourth','Finally','Next','Also ','Instead','But ','And ','So ','Then ','That ','This ','It ','Which ','Or ','Yet ','Because ','Its ','They ','He ','She ','Not ','None ')
def runs_md(p):
    out=[]
    for r in p.runs:
        t=r.text
        # r.text includes \n for breaks
        if r.italic and t.strip():
            # wrap non-break parts
            parts=re.split(r'(\n+)',t)
            t=''.join(('*'+x+'*' if x.strip() and not x.startswith('\n') else x) for x in parts)
        out.append(t)
    s=''.join(out)
    s=s.replace('**','')  # bare
    return s
def reflow(text):
    lines=[l.strip() for l in text.split('\n') if l.strip()]
    paras=[];cur=[];wc=0
    for l in lines:
        n=len(l.split())
        if cur and ((wc>=60 and not l.startswith(CONN)) or wc+n>140):
            paras.append(' '.join(cur));cur=[];wc=0
        cur.append(l);wc+=n
    if cur: paras.append(' '.join(cur))
    return paras
chapters=[];cur=None;part=None
for i,p in enumerate(ps[51:749],51):
    s=p.style.name
    if s=='Part Title': part=p.text; continue
    if s=='Chapter Label': continue
    if s=='Heading 1':
        cur={'title':p.text,'part':part,'body':[]}; chapters.append(cur); continue
    if s=='Heading 2': cur['body'].append('### '+p.text); continue
    if p.text.strip():
        for para in reflow(runs_md(p)): cur['body'].append(para)
for k,c in enumerate(chapters,1):
    open(f'work/evo/{k:02d}.md','w').write(f"<!-- part: {c['part']} -->\n## {c['title']}\n\n"+'\n\n'.join(c['body'])+'\n')
print(len(chapters))
