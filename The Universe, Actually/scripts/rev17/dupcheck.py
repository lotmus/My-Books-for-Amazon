import docx,re,collections,sys
d=docx.Document(sys.argv[1])
t=[p.text for p in d.paragraphs]
sents=collections.Counter()
for x in t:
    for s in re.split(r'(?<=[.!?])\s+',x):
        s=s.strip()
        if len(s.split())>=5 and s[-1] in '.!?': sents[s]+=1
rep=[s for s,c in sents.items() if c>1]
print('words',sum(len(x.split()) for x in t),'repeated sentences (5+ words):',len(rep))
for s in rep[:15]: print(' -',s[:140])
