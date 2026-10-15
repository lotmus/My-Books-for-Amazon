from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, sys, random
W,H=1000,1600
G='/usr/share/fonts/truetype/sand-box/google/'
def font(path,size,wght=None):
    f=ImageFont.truetype(G+path,size)
    if wght:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f
img=Image.new('RGB',(W,H)); px=img.load()
top=(32,10,16); bot=(10,6,14); glowc=(120,40,40)
for y in range(H):
    t=y/H
    g=math.exp(-((t-0.30)/0.2)**2)
    for x in range(W):
        gx=math.exp(-((x-W/2)/(W*0.5))**2); k=g*gx
        px[x,y]=(int(top[0]*(1-t)+bot[0]*t+glowc[0]*k*0.55),int(top[1]*(1-t)+bot[1]*t+glowc[1]*k*0.35),int(top[2]*(1-t)+bot[2]*t+glowc[2]*k*0.35))
img=img.convert('RGBA')
art=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(art)
cx,cy,R=500,560,300
gold=(214,176,96)
# clock face
d.ellipse([cx-R-14,cy-R-14,cx+R+14,cy+R+14],fill=(60,28,24,255),outline=gold,width=6)
d.ellipse([cx-R,cy-R,cx+R,cy+R],fill=(236,226,200,255),outline=(120,90,50),width=4)
for i in range(60):
    a=math.radians(i*6-90); r1=R-10; r2=R-(46 if i%5==0 else 24)
    d.line([cx+r1*math.cos(a),cy+r1*math.sin(a),cx+r2*math.cos(a),cy+r2*math.sin(a)],fill=(40,28,22),width=8 if i%5==0 else 3)
fn=font('Playfair Display/PlayfairDisplay-VariableFont_wght.ttf',54,700)
for n in range(1,13):
    a=math.radians(n*30-90); r=R-88
    s=str(n); w=d.textlength(s,font=fn)
    d.text((cx+r*math.cos(a)-w/2,cy+r*math.sin(a)-34),s,font=fn,fill=(40,28,22))
# hands at 9:17
def hand(angle_deg,length,width,col):
    a=math.radians(angle_deg-90)
    d.line([cx-30*math.cos(a),cy-30*math.sin(a),cx+length*math.cos(a),cy+length*math.sin(a)],fill=col,width=width)
hand(9*30+17*0.5,R-120,16,(40,28,22)); hand(17*6,R-60,10,(40,28,22))
d.ellipse([cx-16,cy-16,cx+16,cy+16],fill=(150,30,30))
# coffee-ring style red stamp across the clock: CORRECTED
stamp=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(stamp)
fs=font('Josefin Sans/JosefinSans-VariableFont_wght.ttf',104,700)
tx='CORRECTED'; tw=sd.textlength(tx,font=fs)
x0=cx-tw/2; y0=cy-40
sd.rectangle([x0-26,y0-14,x0+tw+26,y0+130],outline=(190,36,36,235),width=9)
sd.text((x0,y0),tx,font=fs,fill=(190,36,36,235))
stamp=stamp.rotate(-11,center=(cx,cy),resample=Image.BICUBIC)
art=Image.alpha_composite(art,stamp)
# faint ink spatter
random.seed(3); sp=Image.new('RGBA',(W,H),(0,0,0,0)); pd=ImageDraw.Draw(sp)
for _ in range(60):
    x=random.randint(60,940); y=random.randint(180,900); r=random.randint(2,6)
    pd.ellipse([x-r,y-r,x+r,y+r],fill=(190,36,36,70))
art=Image.alpha_composite(art,sp.filter(ImageFilter.GaussianBlur(1)))
img=Image.alpha_composite(img,art)
d=ImageDraw.Draw(img)
# title panel
panel=Image.new('RGBA',(W,H),(0,0,0,0)); pd=ImageDraw.Draw(panel)
pd.rectangle([60,950,W-60,1400],fill=(10,6,12,232)); img=Image.alpha_composite(img,panel.filter(ImageFilter.GaussianBlur(1.2)))
d=ImageDraw.Draw(img)
d.rectangle([60,950,W-60,1400],outline=gold,width=3); d.rectangle([72,962,W-72,1388],outline=(214,176,96,120),width=1)
def center(text,y,f,fill,spacing=0):
    if spacing:
        w=sum(d.textlength(c,font=f)+spacing for c in text)-spacing; x=(W-w)/2
        for c in text:
            d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+spacing
    else:
        w=d.textlength(text,font=f); d.text(((W-w)/2,y),text,font=f,fill=fill)
fJ=font('Josefin Sans/JosefinSans-VariableFont_wght.ttf',46,500)
fT=font('Playfair Display/PlayfairDisplay-VariableFont_wght.ttf',112,800)
cream=(244,238,222)
center('THE DEPARTMENT',985,fJ,gold,spacing=14)
center('OF HISTORICAL',1050,font('Playfair Display/PlayfairDisplay-VariableFont_wght.ttf',92,800),cream)
center('CORRECTIONS',1160,fT,cream)
fA=font('Josefin Sans/JosefinSans-VariableFont_wght.ttf',62,500)
center('LOTHAR J. MUSIOL',1440,fA,cream,spacing=8)
fq=font('Cormorant Garamond/CormorantGaramond-Italic-VariableFont_wght.ttf',58,600)
center('Belgium has stopped existing.',70,fq,(235,225,200))
center('It is Monday.',140,fq,(235,225,200))
d.line([400,225,600,225],fill=gold,width=2)
fS=font('Josefin Sans/JosefinSans-VariableFont_wght.ttf',32,500)
center('A COMEDY OF CIVIL SERVICE AND TIME',1330,fS,gold,spacing=5)
img.convert('RGB').save(sys.argv[1]); print('ok')
