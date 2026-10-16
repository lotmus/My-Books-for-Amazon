from PIL import Image, ImageDraw, ImageFont
import sys
W,H=1000,1600
F='C:/Windows/Fonts/'
def f(n,s): return ImageFont.truetype(F+n,s)
img=Image.new('RGB',(W,H),(22,8,14)); d=ImageDraw.Draw(img)
gold=(214,176,96); cream=(244,238,222); red=(190,36,36)
d.rectangle([40,40,W-40,H-40],outline=gold,width=3); d.rectangle([52,52,W-52,H-52],outline=(214,176,96),width=1)
def center(t,y,fo,fill,sp=0):
    if sp:
        w=sum(d.textlength(c,font=fo)+sp for c in t)-sp; x=(W-w)/2
        for c in t: d.text((x,y),c,font=fo,fill=fill); x+=d.textlength(c,font=fo)+sp
    else:
        w=d.textlength(t,font=fo); d.text(((W-w)/2,y),t,font=fo,fill=fill)
def wrap(t,fo,maxw):
    words=t.split(); lines=[]; cur=''
    for w in words:
        c=(cur+' '+w).strip()
        if d.textlength(c,font=fo)<=maxw: cur=c
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
center('THE DEPARTMENT OF',90,f('segoeuib.ttf',34),gold,sp=8)
center('HISTORICAL CORRECTIONS',135,f('georgiab.ttf',50),cream)
d.line([360,215,640,215],fill=gold,width=2)
q=f('georgiai.ttf',48)
center('Belgium has stopped existing.',245,q,cream); center('It is Monday.',305,q,cream)
body=f('georgia.ttf',32)
y=410
for para in ["Arthur Pembroke, Grade Seven, notices because of the biscuits. The Department has seventy-two hours, a machine like a telephone exchange, and a contract that specifies London.","Quite a lot of 1815 is London."]:
    for ln in wrap(para,body,780):
        center(ln,y,body,cream); y+=45
    y+=18
d.line([360,y+4,640,y+4],fill=gold,width=2); y+=44
hook=f('georgiab.ttf',30)
for t in ["A comic thriller of forms, receipts and second copies.","Funny in the corridors; serious where it counts.","Includes five short physics lessons with diagrams, worked examples and exercises."]:
    for i,ln in enumerate(wrap(t,hook,800)):
        center(ln,y,hook,gold); y+=40
    y+=12
y+=6
bio=f('georgiai.ttf',26)
for ln in wrap("Lothar J. Musiol spent more than forty years in the semiconductor industry and now writes novels and science books between San Clemente, California, and Passau, Bavaria.",bio,760):
    center(ln,y,bio,cream); y+=36
y+=26
center('ALSO BY LOTHAR J. MUSIOL',y,f('segoeuib.ttf',24),gold,sp=5); y+=46
al=f('georgia.ttf',27)
for t in ["Physics, Actually","Math, Actually","Quantum, Actually","Life, Actually","The Dolphins' View of History"]:
    center(t,y,al,cream); y+=36
center('LOTHAR J. MUSIOL',H-120,f('segoeuib.ttf',36),cream,sp=7)
img.save(sys.argv[1]); print('ok',y)
