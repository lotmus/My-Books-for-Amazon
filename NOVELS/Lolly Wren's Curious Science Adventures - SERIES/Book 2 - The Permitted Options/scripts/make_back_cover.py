from PIL import Image, ImageDraw, ImageFont, ImageFilter
S=2; W,H=1600*S,2560*S
EB='/usr/share/fonts/truetype/sand-box/google/EB Garamond/EBGaramond-VariableFont_wght.ttf'
EBI='/usr/share/fonts/truetype/sand-box/google/EB Garamond/EBGaramond-Italic-VariableFont_wght.ttf'
LB='/workspace/fonts/LibreBaskerville.ttf'; LBI='/workspace/fonts/LibreBaskerville-Italic.ttf'
def F(p,s,w=None):
    f=ImageFont.truetype(p,int(s*S))
    if w:
        try: f.set_variation_by_axes([w])
        except Exception: pass
    return f
NAVY=(20,34,64); GOLD=(214,160,84); CREAM=(240,232,214)
im=Image.new('RGB',(W,H),NAVY)
n=Image.effect_noise((W//4,H//4),10).resize((W,H)).convert('L')
im=Image.composite(Image.new('RGB',(W,H),(26,42,76)),im,n.point(lambda v:max(0,v-125)*3))
d=ImageDraw.Draw(im)
M=60*S
d.rectangle([M,M,W-M,H-M],outline=GOLD,width=3*S); d.rectangle([M+16*S,M+16*S,W-M-16*S,H-M-16*S],outline=GOLD,width=1*S)
def star(x,y,r):
    import math
    pts=[]
    for k in range(8):
        a=k*math.pi/4; rr=r if k%2==0 else r*0.35; pts.append((x+math.sin(a)*rr,y-math.cos(a)*rr))
    d.polygon(pts,fill=GOLD)
for x,y in ((M+44*S,M+44*S),(W-M-44*S,M+44*S),(M+44*S,H-M-44*S),(W-M-44*S,H-M-44*S)): star(x,y,18*S)
L,R=170*S,W-170*S
def wrap(text,font,width):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=font)<=width: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
def para(y,text,font,fill,width,lead,center=False,x0=None):
    x0=L if x0 is None else x0
    for ln in wrap(text,font,width):
        x=x0+(width-d.textlength(ln,font=font))/2 if center else x0
        d.text((x,y),ln,font=font,fill=fill); y+=lead
    return y
def rule(y):
    m=W/2; d.line([(L-20*S,y),(m-30*S,y)],fill=GOLD,width=2*S); d.line([(m+30*S,y),(R+20*S,y)],fill=GOLD,width=2*S)
    r=10*S; d.polygon([(m,y-r),(m+r,y),(m,y+r),(m-r,y)],fill=GOLD)
y=200*S
hook=F(LB,74,700)
y=para(y,'Fourteen people are no longer where the file says they are.',hook,CREAM,R-L,104*S,center=True)
y+=40*S; rule(y); y+=70*S
body=F(EB,44,420); lead=62*S
for t in ["Lolly Wren has taken the post. The last crisis was filed. Now the Ministry of Eventualities has a new department, a new case, and a date: a travel agent in a good coat wants somewhere real for each of the fourteen to go by the ninth of February.",
          "One of them, Ellen Prosper, was meant to be on a course in Newcastle or behind the counter of her mother’s shop. She is on a survey boat out of Peterhead. The card on her file says to speak to her, not to the trace, and nobody is permitted to sign the fourteen away.",
          "Then the consultants arrive: an organ restorer who will not let a minute pretend to be a proof, a geometer who trusts nine, a man of ninety-one who grew crystals, and a lighting engineer who finds the question ludicrous and builds the bench anyway."]:
    y=para(y,t,body,CREAM,R-L,lead)+26*S
y+=10*S; rule(y); y+=50*S
comp=F(EBI,42,420)
y=para(y,'For readers of Good Omens, The Hitchhiker’s Guide to the Galaxy, and anyone who has ever been told the form would sort it out.',comp,GOLD,R-L-60*S,58*S,center=True,x0=L+30*S)
y+=30*S; rule(y); y+=60*S
# two columns
colw=(R-L-80*S)/2; cx=[L,L+colw+80*S]; top=y
hf=F(LB,40,700); bf=F(EB,40,420)
bios=[('LOLLY WREN','Head of a department whose mission statement she refused to write. Fourth notebook. Still asks the question nobody filed.'),
      ('GIDEON WIGGLESWORTH','Lolly’s friend, down at the benches with the cable and the van. Opens a knuckle on a ladder and does not mention it.')]
ys=[]
for (h,b),x in zip(bios,cx):
    w=d.textlength(h,font=hf); d.text((x+(colw-w)/2,top),h,font=hf,fill=GOLD)
    ys.append(para(top+70*S,b,bf,CREAM,colw,56*S,center=True,x0=x))
d.line([(W/2,top),(W/2,max(ys)-10*S)],fill=GOLD,width=2*S)
y=max(ys)+30*S; rule(y); y+=60*S
a1=F(LB,40,700); a2=F(EB,42,420); a2i=F(EBI,42,420)
parts=[('Q.E.D.',a1,GOLD),(' — Quentin Edmund Darling, allegedly.',a2,CREAM)]
tw=sum(d.textlength(t,font=f) for t,f,c in parts); x=(W-tw)/2
for t,f,c in parts: d.text((x,y),t,font=f,fill=c); x+=d.textlength(t,font=f)
y+=60*S
parts=[('Lothar J. Musiol, ',a2,CREAM),('obviously.',a2i,CREAM)]
tw=sum(d.textlength(t,font=f) for t,f,c in parts); x=(W-tw)/2
for t,f,c in parts: d.text((x,y),t,font=f,fill=c); x+=d.textlength(t,font=f)
y+=90*S
sn=F(EB,36,420)
y=para(y,'Book 2 of Lolly Wren’s Curious Science Adventures. It stands alone; if you have survived Schrödinger’s Paperwork, the same people are still in the building. Fifteen optional lectures follow the story.',sn,CREAM,R-L-80*S,50*S,center=True,x0=L+40*S)
print('bottom y',y/S)
out=im.resize((1600,2560),Image.LANCZOS); out.save('/workspace/po/cover/KINDLE_BACK_COVER_2560.jpg',quality=92,subsampling=0)
t=out.copy(); t.thumbnail((640,1024)); t.save('/workspace/po/cover/pv_back.jpg',quality=85)
