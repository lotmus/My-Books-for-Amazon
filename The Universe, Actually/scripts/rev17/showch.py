import docx,sys,io,re
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
f='../../The_Universe_Actually__REV18.docx'
want=[int(x) for x in sys.argv[1:]]
d=docx.Document(f); W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
ch=None
for p in d.element.body.iter(W+'p'):
    s=p.find(W+'pPr'); s=s.find(W+'pStyle') if s is not None else None; s=s.get(W+'val') if s is not None else ''
    t=''.join((x.text or '') for x in p.iter(W+'t'))
    if s=='Heading2':
        m=re.match(r'(\d+)\. ',t); ch=int(m.group(1)) if m else None
    elif s=='Heading1': ch=None
    if ch in want and t.strip(): print(('## ' if s.startswith('Heading') else '')+t)
