import math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(7)
S=2; W,H=1600*S,2560*S
F=r'C:\Windows\Fonts\\'
def font(n,sz): return ImageFont.truetype(F+n, int(sz*S))
def lerp(a,b,t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
def hexc(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def grad(img,y0,y1,stops,x0=0,x1=None):
    d=ImageDraw.Draw(img); x1=x1 or img.width
    for y in range(int(y0*S),int(y1*S)):
        t=(y/S-y0)/(y1-y0)
        for k in range(len(stops)-1):
            if stops[k][0]<=t<=stops[k+1][0]:
                u=(t-stops[k][0])/(stops[k+1][0]-stops[k][0]); c=lerp(hexc(stops[k][1]),hexc(stops[k+1][1]),u); break
        d.line([(x0,y),(x1,y)],fill=c)
P=lambda pts:[(x*S,y*S) for x,y in pts]
img=Image.new('RGB',(W,H))
HZ=1440
grad(img,0,HZ,[(0,'#231f4d'),(0.38,'#4a3a78'),(0.62,'#9a5a8c'),(0.82,'#e8846a'),(1,'#fbcf8e')])
d=ImageDraw.Draw(img)
# stars
for i in range(70):
    x=random.uniform(0,1600); y=random.uniform(0,900); r=random.choice([1.5,2,2.5])
    d.ellipse(P([(x-r,y-r),(x+r,y+r)]),fill=(255,240,220))
for (x,y) in [(170,1010),(250,975),(330,940)]:
    glow=Image.new('L',(W,H)); gd=ImageDraw.Draw(glow); gd.ellipse(P([(x-22,y-22),(x+22,y+22)]),fill=150); glow=glow.filter(ImageFilter.GaussianBlur(14*S))
    img.paste((255,236,200),(0,0),glow); d=ImageDraw.Draw(img)
    d.polygon(P([(x,y-16),(x+4,y-4),(x+16,y),(x+4,y+4),(x,y+16),(x-4,y+4),(x-16,y),(x-4,y-4)]),fill=(255,248,230))
# sun glow + sun
sx,sy,sr=1060,1395,150
glow=Image.new('L',(W,H)); gd=ImageDraw.Draw(glow); gd.ellipse(P([(sx-330,sy-330),(sx+330,sy+330)]),fill=170); glow=glow.filter(ImageFilter.GaussianBlur(90*S))
img.paste((255,214,150),(0,0),glow); d=ImageDraw.Draw(img)
d.ellipse(P([(sx-sr,sy-sr),(sx+sr,sy+sr)]),fill=hexc('#ffe6b0'))
# hills
def ridge(y,amp,seed,col,step=20):
    random.seed(seed); pts=[(0,1600)]; ph=random.random()*6
    for x in range(0,1601,step):
        yy=y-amp*(0.6*math.sin(x/260+ph)+0.4*math.sin(x/97+ph*2))-amp*0.3*math.sin(x/600)
        pts.append((x,yy))
    pts.append((1600,1600)); d.polygon(P(pts),fill=hexc(col))
ridge(1350,45,3,'#b07a9a'); ridge(1395,35,5,'#7d5a8e'); ridge(1440,18,9,'#4e3c6e')
# cypresses on left bank
def cypress(x,base,h,w,col='#2a2442'):
    pts=[]
    for i in range(41):
        t=i/40; yy=base-h*t; ww=w*(math.sin(math.pi*min(1,t*1.15))**0.8)*(1-t*0.35)
        pts.append((x-ww/2,yy))
    pts2=[(2*x-px,py) for px,py in pts[::-1]]
    d.polygon(P(pts+pts2),fill=hexc(col))
# lake
grad(img,HZ,1830,[(0,'#f3b98a'),(0.25,'#d98478'),(0.7,'#8e5a8a'),(1,'#5a4478')])
d=ImageDraw.Draw(img)
random.seed(11)
for i in range(60):
    y=random.uniform(HZ+8,1820); wdt=random.uniform(30,190)*(0.4+(y-HZ)/400); x=sx+random.gauss(0,60+(y-HZ)*0.25)
    c=(255,226,170) if y<1650 else (240,190,160)
    d.rounded_rectangle(P([(x-wdt/2,y),(x+wdt/2,y+random.uniform(3,6))]),radius=3*S,fill=c)
for i in range(40):
    y=random.uniform(HZ+20,1820); x=random.uniform(0,1600); wdt=random.uniform(40,120)
    d.line(P([(x,y),(x+wdt,y)]),fill=(250,205,175),width=2*S)
# left bank with house
d.polygon(P([(0,1420),(120,1415),(420,1430),(700,1462),(760,1500),(600,1530),(0,1545)]),fill=hexc('#3b2f55'))
for x,h,w in [(70,300,52),(120,240,44),(690,250,46),(735,190,38)]:
    cypress(x,1470,h,w)
# house
hx,hb=230,1470
wall=hexc('#efc89a'); shade=hexc('#d39f7c'); roof=hexc('#b9533c'); roofd=hexc('#8f3b2e'); shut=hexc('#5c7cab'); lit=hexc('#ffd57a')
d.polygon(P([(hx,hb),(hx,hb-200),(hx+300,hb-200),(hx+300,hb)]),fill=wall)
d.polygon(P([(hx+300,hb),(hx+300,hb-150),(hx+420,hb-150),(hx+420,hb)]),fill=shade)
d.polygon(P([(hx-20,hb-195),(hx+150,hb-265),(hx+320,hb-195)]),fill=roof)
d.polygon(P([(hx+290,hb-148),(hx+360,hb-190),(hx+440,hb-148)]),fill=roofd)
for i in range(9):
    xx=hx-10+i*37; d.line(P([(xx,hb-197),(xx+8,hb-203)]),fill=roofd,width=3*S)
d.rectangle(P([(hx+200,hb-290),(hx+222,hb-245)]),fill=shade)  # chimney
for (wx,wy,on) in [(hx+40,hb-170,True),(hx+125,hb-170,False),(hx+210,hb-170,True),(hx+40,hb-85,False),(hx+210,hb-85,True)]:
    d.rectangle(P([(wx,wy),(wx+40,wy+55)]),fill=lit if on else hexc('#6b5470'))
    d.rectangle(P([(wx-16,wy),(wx-2,wy+55)]),fill=shut); d.rectangle(P([(wx+42,wy),(wx+56,wy+55)]),fill=shut)
d.rectangle(P([(hx+125,hb-90),(hx+165,hb)]),fill=hexc('#7a4b3a'))
d.rectangle(P([(hx+335,hb-110),(hx+375,hb-55)]),fill=lit)
# house reflection
ref=img.crop((int((hx-30)*S),int((hb-300)*S),int((hx+450)*S),int(hb*S))).transpose(Image.FLIP_TOP_BOTTOM)
mask=Image.new('L',ref.size,0); md=ImageDraw.Draw(mask)
for y in range(ref.size[1]):
    md.line([(0,y),(ref.size[0],y)],fill=int(70*(1-y/ref.size[1])**1.5))
img.paste(ref,(int((hx-30)*S),int((hb+62)*S)),mask); d=ImageDraw.Draw(img)
random.seed(13)
for i in range(30):
    y=random.uniform(hb+70,hb+300); x=random.uniform(hx-20,hx+430); d.line(P([(x,y),(x+random.uniform(40,120),y)]),fill=(214,140,140),width=3*S)
# jetty in perspective
JX,JY=1010,1560
d.polygon(P([(JX-30,JY),(JX+40,JY),(1520,1900),(1180,1900)]),fill=hexc('#3a2638'))
for i in range(1,14):
    t=i/14; y=JY+(1900-JY)*t**1.6; xl=(JX-30)+(1180-(JX-30))*t**1.6; xr=(JX+40)+(1520-(JX+40))*t**1.6
    d.line(P([(xl,y),(xr,y)]),fill=hexc('#5a3a4a'),width=max(2,int(2+4*t))*S)
for t in [0.0,0.35,0.7]:
    tt=t**1.6; xl=(JX-30)+(1180-(JX-30))*tt; xr=(JX+40)+(1520-(JX+40))*tt; y=JY+(1900-JY)*tt; ph=30+90*tt; pw=6+14*tt
    d.rectangle(P([(xl-pw,y-ph*0.3),(xl,y+ph)]),fill=hexc('#2c1c2c')); d.rectangle(P([(xr,y-ph*0.3),(xr+pw,y+ph)]),fill=hexc('#2c1c2c'))
# pelican silhouette at jetty end, facing left
pc=hexc('#24192e')
def pelican(fx,fy,k):
    Q=lambda pts:[(S*(fx+x*k),S*(fy+y*k)) for x,y in pts]
    for x0,x1 in ((-6,-2),(12,10)): d.line(Q([(x0,0),(x1,-44)]),fill=pc,width=max(2,int(7*k*S)))
    d.polygon(Q([(-16,0),(6,0),(-4,-6)]),fill=pc); d.polygon(Q([(2,0),(24,0),(12,-6)]),fill=pc)
    d.ellipse(Q([(-62,-118),(72,-36)]),fill=pc)
    d.polygon(Q([(52,-96),(108,-62),(104,-54),(58,-52)]),fill=pc)
    front=[(-56,-92),(-46,-140),(-60,-185),(-50,-228)]; back=[(-16,-106),(-8,-148),(-24,-188),(-14,-232)]
    d.polygon(Q(front+back[::-1]),fill=pc)
    d.ellipse(Q([(-54,-262),(-10,-224)]),fill=pc)
    d.polygon(Q([(-48,-252),(-196,-190),(-198,-180),(-50,-236)]),fill=pc)
    d.polygon(Q([(-198,-190),(-206,-176),(-196,-178)]),fill=pc)
    d.polygon(Q([(-50,-236),(-194,-181),(-160,-168),(-112,-168),(-74,-182),(-50,-206)]),fill=pc)
pelican(JX+6,JY+2,0.6)
# flying pages
random.seed(4)
pages=[(760,1180,-18,1.0),(905,1160,12,0.85),(640,1320,25,0.9),(1240,1150,-30,0.8),(1370,1290,8,0.7),(560,1640,-8,0.8),(830,1700,15,0.9),(1380,1580,-20,0.7)]
for (x,y,a,s) in pages:
    pw,ph=int(70*s*S),int(92*s*S)
    pg=Image.new('RGBA',(pw,ph),(255,248,236,255)); pd=ImageDraw.Draw(pg)
    for k in range(6): pd.line([(int(8*s*S),int((14+12*k)*s*S)),(int((62 if k<5 else 40)*s*S),int((14+12*k)*s*S))],fill=(150,130,140,255),width=max(1,int(2*s)))
    pg=pg.rotate(a,expand=True,resample=Image.BICUBIC)
    if y>1500:
        sh=Image.new('RGBA',pg.size,(0,0,0,0)); 
    img.paste(pg,(int(x*S-pg.width/2),int(y*S-pg.height/2)),pg)
d=ImageDraw.Draw(img)
# lavender field
FT=1830
grad(img,FT,2560,[(0,'#4a3c6a'),(1,'#2a2040')])
d=ImageDraw.Draw(img)
random.seed(5)
pts=[(0,FT+10)]+[(x,FT-6+random.uniform(-6,6)) for x in range(0,1601,40)]+[(1600,FT+10)]
d.polygon(P(pts),fill=hexc('#2f2546'))
for i in range(180):
    x=random.uniform(0,1600); hh=random.uniform(10,34); d.line(P([(x,FT+8),(x+random.uniform(-8,8),FT-hh)]),fill=hexc('#2f2546'),width=2*S)
VX,VY=800,1760
random.seed(21)
rows=15
for r in range(-rows,rows+1):
    xb=800+r*240
    for j in range(0,90):
        t=j/90; y=FT+(2560-FT)*t**1.25
        x=VX+(xb-VX)*((y-VY)/(2560-VY))
        sz=(3+26*((y-FT)/(2560-FT)))
        col=random.choice(['#8d6cc9','#9f80da','#7a58b8','#b296e6'])
        for k in range(3):
            xx=x+random.uniform(-sz,sz)*1.1; yy=y+random.uniform(-sz*0.6,sz*0.3)
            d.ellipse(P([(xx-sz*0.45,yy-sz),(xx+sz*0.45,yy+sz*0.2)]),fill=hexc(col))
# darken bottom for byline
ov=Image.new('L',(W,H),0); od=ImageDraw.Draw(ov)
for y in range(int(2150*S),H):
    od.line([(0,y),(W,y)],fill=int(200*min(1,(y/S-2150)/300)))
img.paste((32,24,52),(0,0),ov)
# darken top for title
ov=Image.new('L',(W,H),0); od=ImageDraw.Draw(ov)
for y in range(0,int(900*S)):
    od.line([(0,y),(W,y)],fill=int(90*(1-y/S/900)))
img.paste((20,16,45),(0,0),ov)
d=ImageDraw.Draw(img)
CREAM=hexc('#fff1dc'); GOLD=hexc('#ffc36b'); PLUM=hexc('#2a1838')
def ctext(y,s,f,fill,shadow=PLUM,sh=6,spacing=0,stroke=0):
    if spacing:
        ws=[d.textlength(c,font=f)+spacing*S for c in s]; tw=sum(ws)-spacing*S; x=(W-tw)/2
        for c,wc in zip(s,ws):
            if shadow: d.text((x+sh*S,y*S+sh*S),c,font=f,fill=shadow)
            d.text((x,y*S),c,font=f,fill=fill); x+=wc
        return
    tw=d.textlength(s,font=f); x=(W-tw)/2
    if shadow: d.text((x+sh*S,y*S+sh*S),s,font=f,fill=shadow,stroke_width=stroke*S,stroke_fill=shadow)
    d.text((x,y*S),s,font=f,fill=fill,stroke_width=stroke*S,stroke_fill=PLUM)
ctext(95,'IN LOVE WITH',font('JosefinSans-Bold.ttf',118),CREAM,spacing=14,sh=5)
ctext(205,'MURDER,',font('Shrikhand-Regular.ttf',300),CREAM,sh=12,stroke=4)
ctext(500,'Actually',font('Yellowtail-Regular.ttf',290),GOLD,sh=9)
# subtitle with rules
f=font('JosefinSans-Bold.ttf',62); s='A DERAILED MYSTERY IN PROVENCE'
ctext(845,s,f,CREAM,spacing=6,sh=3)
d.line(P([(330,935),(1270,935)]),fill=GOLD,width=3*S)
ctext(958,'Paris can wait. Aix can\u2019t.',font('NotoSerif-Italic.ttf',54),CREAM,sh=3)
ctext(2205,'LOTHAR J. MUSIOL',font('JosefinSans-Bold.ttf',58),CREAM,spacing=8,sh=3)
ctext(2272,'writing as',font('Yellowtail-Regular.ttf',70),GOLD,sh=3)
ctext(2385,'ROMUALD LIVINGSTON',font('JosefinSans-Bold.ttf',112),CREAM,spacing=6,sh=5)
out=img.resize((1600,2560),Image.LANCZOS)
out.save('front.jpg',quality=92)
out.resize((300,480),Image.LANCZOS).save('thumb300.jpg'); out.resize((120,192),Image.LANCZOS).save('thumb120.jpg')
out.resize((800,1280),Image.LANCZOS).save('preview.jpg',quality=88)
print('ok')

