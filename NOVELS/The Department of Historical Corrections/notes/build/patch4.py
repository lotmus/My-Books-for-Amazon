b=open('build.py',encoding='utf-8').read()
a="if s_.strip() in ('* * *','---'): para('* * *','Scene Break'); continue"
assert b.count(a)==1
b=b.replace(a,"if s_.strip() in ('* * *','---'):\n            sbp=doc.add_paragraph(style='Scene Break'); sbp.add_run('* * *'); continue")
a2="para('A Novel','Subtitle'); para('','Normal'); para('**Lothar J. Musiol**','Centered')"
assert b.count(a2)==1
b=b.replace(a2,"para('A Novel','Subtitle'); _a=para('**Lothar J. Musiol**','Centered'); _a.paragraph_format.space_before=Pt(24)")
open('build.py','w',encoding='utf-8').write(b)
