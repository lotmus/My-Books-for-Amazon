import docx,re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
ps=docx.Document('../The_Universe_Actually__REV11.docx').paragraphs
t=[p.text for p in ps]
print('latex paras',sum('\(' in x or '\[' in x for x in t),'; ** paras',sum('**' in x for x in t),'; urls',sum('http' in x for x in t))
print([x[:150] for x in t if '\(' in x][:5])
print(sum(1 for x in t if re.fullmatch(r'\*\*[^*]+\*\*',x.strip())),'bold-only paras')
print([x[:110] for x in t if '**' in x and not re.fullmatch(r'\*\*[^*]+\*\*',x.strip())][:8])
