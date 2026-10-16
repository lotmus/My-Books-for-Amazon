s=open('rev13_edit.py',encoding='utf-8').read()
a="The receipt was Glock’s, in his small upright hand, with Beatrice’s signature under it."
assert s.count(a)==1
s=s.replace(a,"The receipt was Glock’s, in his small upright hand, for the pages he had taken; the box for the reason was in hers.")
open('rev13_edit.py','w',encoding='utf-8').write(s)
b=open('build.py',encoding='utf-8').read()
b=b.replace("BLUE=RGBColor(0x1F,0x4E,0x79)","BLUE=RGBColor(0x2A,0x5C,0xAA)").replace("c.set(qn('w:val'),'1F4E79')","c.set(qn('w:val'),'2A5CAA')")
b=b.replace("h2=st['Heading 2']; setfont(h2,11,True,False,BLUE)\nh2.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT","h2=st['Heading 2']; setfont(h2,12.5,True,False,BLUE)\nh2.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.CENTER")
open('build.py','w',encoding='utf-8').write(b)
print(b.count('2A5CAA'), 'CENTER' in b)
