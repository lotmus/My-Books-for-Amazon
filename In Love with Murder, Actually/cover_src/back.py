import re
from PIL import Image, ImageDraw, ImageFont
F=r'C:\Windows\Fonts\\'
md=open(r'D:\My Books for Amazon\In Love with Murder, Actually\KDP_LISTING.md',encoding='utf-8-sig').read()
desc=md.split('## Description',1)[1].split('##',1)[0].strip()
paras=[p.strip() for p in desc.split('\n\n') if p.strip()]
import re as _re
def smart(t):
    t=_re.sub(r'(^|[\s(])"',lambda m:m.group(1)+'\u201c',t); t=t.replace('"','\u201d'); return t.replace("'",'\u2019')
paras=[smart(p) for p in paras]
W,H=1600,2560
BG=(46,36,72); CREAM=(255,241,220); GOLD=(255,195,107)
img=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(img)
M=150; maxw=W-2*M
def wrap(t,f):
    words=t.split(); lines=[]; cur=''
    for w in words:
        tt=(cur+' '+w).strip()
        if d.textlength(tt,font=f)<=maxw: cur=tt
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
head=ImageFont.truetype(F+'Yellowtail-Regular.ttf',110); small=ImageFont.truetype(F+'JosefinSans-Bold.ttf',44)
for sz in range(50,30,-1):
    body=ImageFont.truetype(F+'NotoSerif-Regular.ttf',sz); ital=ImageFont.truetype(F+'NotoSerif-Italic.ttf',sz)
    LH=int(sz*1.48); GAP=int(sz*0.75)
    tot=sum(len(wrap(p,ital if p.startswith(('For readers','Paris can')) else body))*LH+GAP for p in paras)
    if 330+tot<=2190: break
print('size',sz)
y0=150+(2190-330-tot)//2
tw=d.textlength('Não é só papel.',font=head); d.text(((W-tw)/2,y0),'Não é só papel.',font=head,fill=GOLD)
y=y0+190
for i,p in enumerate(paras):
    f=ital if p.startswith(('For readers','Paris can')) else body
    for ln in wrap(p,f):
        d.text((M,y),ln,font=f,fill=CREAM); y+=LH
    y+=GAP
print('text ends at',y)
d.line([(M,y+20),(W-M,y+20)],fill=GOLD,width=3)
t='IN LOVE WITH MURDER, ACTUALLY'; tw=d.textlength(t,font=small); d.text(((W-tw)/2,y+60),t,font=small,fill=CREAM)
t='Romuald Livingston'; f2=ImageFont.truetype(F+'Yellowtail-Regular.ttf',80); tw=d.textlength(t,font=f2); d.text(((W-tw)/2,y+125),t,font=f2,fill=GOLD)
img.save('back.jpg',quality=92); img.resize((800,1280),Image.LANCZOS).save('back_prev.jpg',quality=88)
