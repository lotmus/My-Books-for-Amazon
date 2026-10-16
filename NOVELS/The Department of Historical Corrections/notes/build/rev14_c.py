P='../../The Department of Historical Corrections - REV14.md'
b=open(P,encoding='utf-8').read()
d="He said that seemed to involve deadlines too.\n\nShe laughed."
assert b.count(d)==1
b=b.replace(d,"She laughed.")
open(P,'w',encoding='utf-8',newline='\n').write(b)
