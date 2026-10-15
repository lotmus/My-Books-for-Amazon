from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random, math
S=2; W,H=1600*S,2560*S
FD='/workspace/fonts/'
def F(name,size,w=None):
    f=ImageFont.truetype(name if name.startswith('/') else FD+name,int(size*S))
    if w: f.set_variation_by_axes([w])
    return f
GAR='/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Regular.ttf'
import glob
def find(pat):
    g=glob.glob('/usr/share/fonts/**/'+pat,recursive=True); return g[0] if g else None
GAR='/usr/share/fonts/truetype/sand-box/google/EB Garamond/EBGaramond-VariableFont_wght.ttf'; GARI='/usr/share/fonts/truetype/sand-box/google/EB Garamond/EBGaramond-Italic-VariableFont_wght.ttf'
GOLD=(236,182,86); GOLD2=(201,140,52); DARK=(28,25,22); CREAM=(244,232,204); NAVY=(24,42,66); TEAL=(28,70,78)
random.seed(7)
im=Image.new('RGB',(W,H),DARK); d=ImageDraw.Draw(im)
# subtle texture
noise=Image.effect_noise((W//4,H//4),18).resize((W,H)).convert('L')
im=Image.composite(Image.new('RGB',(W,H),(40,36,31)),im,noise.point(lambda v:max(0,v-120)))
d=ImageDraw.Draw(im)
def cx_text(y,txt,font,fill,stroke=0,sfill=None,draw=None):
    draw=draw or d; w=draw.textlength(txt,font=font); draw.text(((W-w)/2,y),txt,font=font,fill=fill,stroke_width=stroke,stroke_fill=sfill); return w
def rule(y,x0,x1,diamond=True):
    d.line([(x0,y),(x1,y)],fill=GOLD2,width=3*S)
    if diamond:
        m=(x0+x1)/2; r=11*S; d.polygon([(m,y-r),(m+r,y),(m,y+r),(m-r,y)],fill=GOLD)
# ---- title
rule(60*S,240*S,1360*S)
def gold_title(y,txt,size,maxw):
    f=F('Cinzel.ttf',size,900)
    while d.textlength(txt,font=f)>maxw*S: size-=4; f=F('Cinzel.ttf',size,900)
    w=d.textlength(txt,font=f); x=(W-w)/2
    mask=Image.new('L',(W,H),0); ImageDraw.Draw(mask).text((x,y),txt,font=f,fill=255)
    # shadow + outline
    sh=mask.filter(ImageFilter.GaussianBlur(6*S)); im.paste((8,6,4),(0,0),sh.point(lambda v:int(v*0.9)))
    ol=mask.filter(ImageFilter.MaxFilter(2*(3*S)+1)); im.paste((58,34,12),(0,0),ol)
    # gold gradient fill with speckles
    bb=mask.getbbox(); grad=Image.new('RGB',(W,H),GOLD); gd=ImageDraw.Draw(grad)
    for yy in range(bb[1],bb[3]):
        t=(yy-bb[1])/max(1,bb[3]-bb[1]); c=tuple(int(GOLD[i]*(1-t)*1.05+GOLD2[i]*t) for i in range(3)); gd.line([(bb[0],yy),(bb[2],yy)],fill=tuple(min(255,v) for v in c))
    sp=Image.new('L',(W,H),0); spd=ImageDraw.Draw(sp)
    for _ in range(int((bb[2]-bb[0])*(bb[3]-bb[1])/(900*S*S))):
        px=random.randint(bb[0],bb[2]); py=random.randint(bb[1],bb[3]); r=random.choice([1,1,2])*S; spd.ellipse([px-r,py-r,px+r,py+r],fill=random.randint(120,220))
    grad.paste((92,60,20),(0,0),sp)
    im.paste(grad,(0,0),mask)
    return f.size, bb
gold_title(95*S,'THE PERMITTED',176,1470)
gold_title(300*S,'OPTIONS',250,1470)
d=ImageDraw.Draw(im)
# subtitle
sub=F('Cinzel.ttf',44,700); txt='A NOVEL OF QUANTUM BUREAUCRACY'
w=d.textlength(txt,font=sub); y=585*S
d.text(((W-w)/2,y),txt,font=sub,fill=CREAM)
d.line([((W-w)/2-170*S,y+28*S),((W-w)/2-30*S,y+28*S)],fill=GOLD2,width=3*S); d.line([((W+w)/2+30*S,y+28*S),((W+w)/2+170*S,y+28*S)],fill=GOLD2,width=3*S)
for xx in ((W-w)/2-180*S,(W+w)/2+180*S):
    r=8*S; d.polygon([(xx,y+28*S-r),(xx+r,y+28*S),(xx,y+28*S+r),(xx-r,y+28*S)],fill=GOLD)
# ---- illustration panel
P0,P1=680*S,2130*S
panel=Image.new('RGB',(W,P1-P0),TEAL); pd=ImageDraw.Draw(panel)
# wall gradient: warm lamp glow centre-top
glow=Image.new('L',(W,P1-P0),0); ImageDraw.Draw(glow).ellipse([W*0.1,-500*S,W*0.9,900*S],fill=255); glow=glow.filter(ImageFilter.GaussianBlur(160*S))
panel=Image.composite(Image.new('RGB',panel.size,(196,130,64)),panel,glow.point(lambda v:int(v*0.55)))
pd=ImageDraw.Draw(panel)
# wall panelling lines
for x in range(0,W,200*S): pd.line([(x,0),(x,820*S)],fill=(22,58,64),width=4*S)
pd.rectangle([0,820*S,W,840*S],fill=(98,62,34))
# departures board
bx0,by0,bx1,by1=150*S,90*S,1450*S,800*S
pd.rounded_rectangle([bx0-18*S,by0-18*S,bx1+18*S,by1+18*S],radius=26*S,fill=(70,48,26))
pd.rounded_rectangle([bx0,by0,bx1,by1],radius=14*S,fill=(16,16,18))
hf=F('Cinzel.ttf',40,800); pd.text((bx0+40*S,by0+26*S),'PERMITTED DESTINATIONS',font=hf,fill=GOLD)
sf=F(GAR,26); pd.text((bx0+42*S,by0+80*S),'Department of Remaining Possibilities  ·  Marsham Street',font=sf,fill=(190,170,140))
# clock
ccx,ccy,cr=bx1-95*S,by0+70*S,52*S
pd.ellipse([ccx-cr,ccy-cr,ccx+cr,ccy+cr],fill=CREAM,outline=GOLD2,width=5*S)
for k in range(12):
    a=k*math.pi/6; pd.line([(ccx+math.sin(a)*cr*0.78,ccy-math.cos(a)*cr*0.78),(ccx+math.sin(a)*cr*0.92,ccy-math.cos(a)*cr*0.92)],fill=DARK,width=3*S)
for a,l,wd in ((math.radians(355),0.55,6),(math.radians(-6+330),0.8,4)):
    pd.line([(ccx,ccy),(ccx+math.sin(a)*cr*l,ccy-math.cos(a)*cr*l)],fill=DARK,width=wd*S)
rows=[('NEWCASTLE  (COURSE)','NOT TAKEN',(230,120,90)),("MOTHER'S SHOP",'NOT TAKEN',(230,120,90)),('PETERHEAD (SURVEY BOAT)','ON BOARD',(140,215,150)),
      ('THIRTEEN OTHERS','ELSEWHERE',GOLD),('VIENNA (FOURTH FLOOR)','PENDING',GOLD),('ANYWHERE ELSE','ASK AT DESK',CREAM)]
ff=F('/workspace/fonts/SpecialElite-Regular.ttf',36)
ry=by0+150*S
for dest,stat,col in rows:
    # split-flap tiles
    x=bx0+40*S
    for ch in dest.ljust(23)[:23]:
        pd.rectangle([x,ry,x+36*S,ry+62*S],fill=(32,32,36)); pd.line([(x,ry+31*S),(x+36*S,ry+31*S)],fill=(12,12,14),width=2*S)
        if ch!=' ': tw=pd.textlength(ch,font=ff); pd.text((x+(36*S-tw)/2,ry+8*S),ch,font=ff,fill=(240,200,110))
        x+=39*S
    x=bx0+40*S+23*39*S+20*S
    pd.rectangle([x,ry,bx1-40*S,ry+62*S],fill=(32,32,36)); pd.line([(x,ry+31*S),(bx1-40*S,ry+31*S)],fill=(12,12,14),width=2*S)
    tw=pd.textlength(stat,font=ff); pd.text((x+((bx1-40*S-x)-tw)/2,ry+8*S),stat,font=ff,fill=col)
    ry+=98*S
# desk
pd.polygon([(0,1110*S),(W,1040*S),(W,P1-P0),(0,P1-P0)],fill=(120,74,40))
for k in range(9):
    yy=1080*S+k*45*S; pd.line([(0,yy+30*S),(W,yy-40*S)],fill=(108,66,34),width=3*S)
panel=panel.convert('RGBA'); pd=ImageDraw.Draw(panel)
def rot_card(img,ang,pos):
    r=img.rotate(ang,expand=True,resample=Image.BICUBIC)
    sh=Image.new('RGBA',r.size,(0,0,0,0)); sh.putalpha(r.split()[3].point(lambda v:int(v*0.45))); sh=sh.filter(ImageFilter.GaussianBlur(10*S))
    panel.alpha_composite(sh,(pos[0]+14*S,pos[1]+16*S)); panel.alpha_composite(r,pos)
# file folder with card
fo=Image.new('RGBA',(700*S,420*S),(0,0,0,0)); fd=ImageDraw.Draw(fo)
fd.rounded_rectangle([0,40*S,700*S,420*S],radius=10*S,fill=(222,196,140)); fd.rounded_rectangle([40*S,0,300*S,70*S],radius=10*S,fill=(222,196,140))
fd.rectangle([0,40*S,700*S,52*S],fill=(205,176,118))
fd.text((70*S,90*S),'FILE: THE FOURTEEN',font=F('Cinzel.ttf',44,800),fill=(60,40,22))
fd.text((70*S,150*S),'Breach of permitted options · 14 March',font=F(GAR,30),fill=(80,58,36))
card=Image.new('RGBA',(450*S,180*S),(250,244,226,255)); cd=ImageDraw.Draw(card)
cd.rectangle([0,0,450*S-1,180*S-1],outline=(150,120,80),width=3*S)
cd.text((24*S,18*S),'Speak to her,',font=F('Caveat.ttf',56,700),fill=(30,52,110)); cd.text((24*S,88*S),'not to the trace.',font=F('Caveat.ttf',56,700),fill=(30,52,110))
fo.alpha_composite(card.rotate(3,expand=True,resample=Image.BICUBIC),(50*S,190*S))
fd.rectangle([300*S,190*S,330*S,260*S],fill=(160,160,170))  # clip
rot_card(fo,3,(390*S,1020*S))
# green notebook
nb=Image.new('RGBA',(330*S,430*S),(0,0,0,0)); nd=ImageDraw.Draw(nb)
nd.rounded_rectangle([0,0,330*S,430*S],radius=18*S,fill=(46,92,58)); nd.rectangle([0,0,26*S,430*S],fill=(34,70,44))
for k in range(12): nd.ellipse([6*S,20*S+k*34*S,20*S,34*S+k*34*S],fill=(200,200,205))
nd.rectangle([70*S,60*S,290*S,150*S],fill=(236,226,196)); nd.text((86*S,68*S),'PRIVATE',font=F('Cinzel.ttf',34,800),fill=(46,92,58)); nd.text((86*S,108*S),'UNHELPFUL',font=F('Cinzel.ttf',26,700),fill=(46,92,58))
nd.line([(300*S,30*S),(300*S,400*S)],fill=(30,30,30),width=12*S)
rot_card(nb,-10,(40*S,1000*S))
# mug
mg=Image.new('RGBA',(300*S,330*S),(0,0,0,0)); md=ImageDraw.Draw(mg)
md.ellipse([210*S,90*S,300*S,220*S],outline=(240,236,226),width=22*S)
md.rounded_rectangle([0,30*S,240*S,330*S],radius=24*S,fill=(240,236,226)); md.ellipse([0,10*S,240*S,60*S],fill=(220,214,200)); md.ellipse([14*S,18*S,226*S,52*S],fill=(80,48,26))
mf=F('Cinzel.ttf',30,900)
for k,t in enumerate(['KEEP','CALM','AND','TUNNEL','THROUGH']):
    tw=md.textlength(t,font=mf); md.text(((240*S-tw)/2,92*S+k*42*S),t,font=mf,fill=(28,40,70))
rot_card(mg,0,(1250*S,900*S))
# sticky note
st=Image.new('RGBA',(300*S,270*S),(246,214,92,255)); sd=ImageDraw.Draw(st)
sd.text((26*S,30*S),'Ask for',font=F('Caveat.ttf',70,700),fill=(40,34,30)); sd.text((26*S,120*S),'Ellen.',font=F('Caveat.ttf',84,700),fill=(40,34,30))
st=st.resize((250*S,225*S),Image.LANCZOS); rot_card(st,-6,(985*S,850*S))
# stamp
stp=Image.new('RGBA',(560*S,150*S),(0,0,0,0)); STP=True; stdw=ImageDraw.Draw(stp)
stdw.rounded_rectangle([6*S,6*S,554*S,144*S],radius=14*S,outline=(186,40,36,215),width=9*S)
stdw.text((30*S,22*S),'PERMITTED',font=F('Cinzel.ttf',60,900),fill=(186,40,36,215)); stdw.text((38*S,92*S),'(PROVISIONALLY)',font=F('Cinzel.ttf',32,800),fill=(186,40,36,215))
stp=stp.resize((450*S,120*S),Image.LANCZOS); panel.alpha_composite(stp.rotate(-8,expand=True,resample=Image.BICUBIC),(840*S,1250*S))
panel=panel.convert('RGB')
# panel frame
im.paste(panel,(0,P0)); d=ImageDraw.Draw(im)
d.line([(0,P0),(W,P0)],fill=GOLD2,width=4*S); d.line([(0,P1),(W,P1)],fill=GOLD2,width=4*S)
# roundel
rcx,rcy,rr=215*S,P0+40*S+0,0
rcx,rcy,rr=1330*S,P0+975*S,0
rcx,rcy,rr=1390*S,P1+20*S,150*S
d.ellipse([rcx-rr-10*S,rcy-rr-10*S,rcx+rr+10*S,rcy+rr+10*S],fill=GOLD2); d.ellipse([rcx-rr,rcy-rr,rcx+rr,rcy+rr],fill=(22,54,64)); d.ellipse([rcx-rr+14*S,rcy-rr+14*S,rcx+rr-14*S,rcy+rr-14*S],outline=GOLD,width=3*S)
rf=F('Cinzel.ttf',30,800)
for t,yy,f in (("LOLLY WREN'S",rcy-112*S,rf),('CURIOUS SCIENCE',rcy+6*S,F('Cinzel.ttf',27,800)),('ADVENTURES',rcy+42*S,F('Cinzel.ttf',27,800)),('BOOK 2',rcy+92*S,F('Cinzel.ttf',32,900))):
    tw=d.textlength(t,font=f); d.text((rcx-tw/2,yy),t,font=f,fill=CREAM if 'BOOK' not in t else GOLD)
# small wren
bx,by=rcx,rcy-40*S
d.ellipse([bx-38*S,by-20*S,bx+28*S,by+24*S],fill=CREAM); d.ellipse([bx+12*S,by-34*S,bx+44*S,by-4*S],fill=CREAM)
d.polygon([(bx+42*S,by-22*S),(bx+60*S,by-18*S),(bx+42*S,by-14*S)],fill=GOLD); d.polygon([(bx-30*S,by-6*S),(bx-62*S,by-44*S),(bx-50*S,by-2*S)],fill=CREAM)
d.line([(bx-6*S,by+22*S),(bx-10*S,by+36*S)],fill=CREAM,width=3*S); d.line([(bx+8*S,by+22*S),(bx+6*S,by+36*S)],fill=CREAM,width=3*S)
d.ellipse([bx+28*S,by-24*S,bx+34*S,by-18*S],fill=(22,54,64))
# ---- bottom: Q.E.D. and byline
gold_title(2185*S,'Q.E.D.',150,800); d=ImageDraw.Draw(im)
bf=F(GAR,52); bi=F(GARI,52)
parts=[('Lothar J. Musiol ',bf,CREAM),('writing as',bi,GOLD),(' Quentin Edmund Darling',bf,CREAM)]
tw=sum(d.textlength(t,font=f) for t,f,c in parts); x=(W-tw)/2
for t,f,c in parts: d.text((x,2420*S),t,font=f,fill=c); x+=d.textlength(t,font=f)
rule(2510*S,420*S,1180*S)
out=im.resize((1600,2560),Image.LANCZOS)
from PIL import ImageEnhance
out=ImageEnhance.Color(out).enhance(1.05)
out.save('/workspace/po/cover/KINDLE_COVER_FINAL_2560.jpg',quality=92,subsampling=0)
t=out.copy(); t.thumbnail((640,1024)); t.save('/workspace/po/cover/preview_front.jpg',quality=85)
print('ok')
