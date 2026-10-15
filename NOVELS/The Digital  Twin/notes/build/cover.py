from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, sys
W,H=1000,1600
G='/usr/share/fonts/truetype/sand-box/google/'
def font(path,size,wght=None):
    f=ImageFont.truetype(G+path,size)
    if wght:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f
# background gradient
img=Image.new('RGB',(W,H))
px=img.load()
top=(8,18,40); bot=(3,8,20); mid=(14,52,78)
for y in range(H):
    t=y/H
    # teal glow around y=0.38
    g=math.exp(-((t-0.36)/0.22)**2)
    for x in range(W):
        gx=math.exp(-((x-W/2)/(W*0.55))**2)
        k=g*gx
        r=int(top[0]*(1-t)+bot[0]*t + (mid[0]-8)*k)
        gg=int(top[1]*(1-t)+bot[1]*t + (mid[1]-14)*k)
        b=int(top[2]*(1-t)+bot[2]*t + (mid[2]-30)*k)
        px[x,y]=(r,gg,b)
art=Image.new('RGBA',(W,H),(0,0,0,0))
d=ImageDraw.Draw(art)
def person(d,cx,base,s,fill,outline=None,width=0):
    # head + shoulders
    hr=int(95*s)
    hy=base-int(330*s)
    d.ellipse([cx-hr,hy-hr,cx+hr,hy+hr],fill=fill,outline=outline,width=width)
    # neck
    d.rectangle([cx-int(38*s),hy+hr-10,cx+int(38*s),hy+hr+int(60*s)],fill=fill)
    # shoulders
    sw=int(195*s)
    d.pieslice([cx-sw,base-int(210*s),cx+sw,base+int(250*s)],180,360,fill=fill,outline=outline,width=width)
    d.rectangle([cx-sw,base,cx+sw,base+10],fill=fill)
base=800
# original: solid, warm dark grey with soft rim
sil=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sil)
person(sd,300,base,1.05,(52,66,90,255))
rim=sil.filter(ImageFilter.GaussianBlur(14))
glow=Image.new('RGBA',(W,H),(0,0,0,0))
person(ImageDraw.Draw(glow),300,base,1.07,(255,190,110,70))
glow=glow.filter(ImageFilter.GaussianBlur(22))
art=Image.alpha_composite(art,glow)
art=Image.alpha_composite(art,sil)
# twin: cyan scanline silhouette, slightly taller, offset
tw=Image.new('RGBA',(W,H),(0,0,0,0)); td=ImageDraw.Draw(tw)
person(td,705,base-20,1.12,(60,220,240,255))
mask=tw.split()[3]
lines=Image.new('L',(W,H),0); ld=ImageDraw.Draw(lines)
for y in range(0,H,9):
    ld.rectangle([0,y,W,y+4],fill=255)
from PIL import ImageChops
m2=ImageChops.multiply(mask,lines)
twl=Image.new('RGBA',(W,H),(70,225,245,0)); twl.putalpha(m2.point(lambda v:int(v*0.80)))
twglow=tw.filter(ImageFilter.GaussianBlur(26)); twglow.putalpha(twglow.split()[3].point(lambda v:int(v*0.38)))
art=Image.alpha_composite(art,twglow)
art=Image.alpha_composite(art,twl)
# glitch slices on twin
import random
random.seed(4)
ga=art.copy()
for i in range(7):
    y=random.randint(330,760); h=random.randint(8,22); dx=random.choice([-28,-18,18,30])
    strip=ga.crop((480,y,W,y+h)); art.paste(Image.new('RGBA',(W-480,h),(0,0,0,0)),(480,y))
    art.alpha_composite(strip,(480+dx,y))
img=Image.alpha_composite(img.convert('RGBA'),art)
d=ImageDraw.Draw(img)
# fruit at bottom of art: oranges and an apple on a thin shelf
def fruit(cx,cy,r,c1,c2):
    for i in range(r,0,-2):
        t=i/r
        col=tuple(int(c1[k]*t+c2[k]*(1-t)) for k in range(3))
        d.ellipse([cx-i-(r-i)*0.25,cy-i-(r-i)*0.3,cx+i-(r-i)*0.25,cy+i-(r-i)*0.3],fill=col)
for cx,cy,r in [(120,880,46),(190,905,40),(840,890,44),(905,912,36)]:
    fruit(cx,cy,r,(232,110,20),(255,175,70))
fruit(250,920,38,(170,25,25),(235,80,60))
d.ellipse([240,862,262,874],fill=(70,140,60))
# title panel
panel=Image.new('RGBA',(W,H),(0,0,0,0)); pd=ImageDraw.Draw(panel)
pd.rectangle([60,960,W-60,1395],fill=(4,10,24,225))
panel=panel.filter(ImageFilter.GaussianBlur(1.2))
img=Image.alpha_composite(img,panel)
d=ImageDraw.Draw(img)
gold=(214,176,96)
d.rectangle([60,960,W-60,1395],outline=gold,width=3)
d.rectangle([72,972,W-72,1383],outline=(214,176,96,120),width=1)
def center(text,y,f,fill,spacing=0):
    if spacing:
        w=sum(d.textlength(c,font=f)+spacing for c in text)-spacing
        x=(W-w)/2
        for c in text:
            d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+spacing
    else:
        w=d.textlength(text,font=f); d.text(((W-w)/2,y),text,font=f,fill=fill)
fT=font('Playfair Display/PlayfairDisplay-VariableFont_wght.ttf',148,800)
center('THE',1000,font('Josefin Sans/JosefinSans-VariableFont_wght.ttf',40,500),gold,spacing=18)
center('DIGITAL',1052,fT,(244,238,222))
center('TWIN',1196,fT,(244,238,222))
# author
fA=font('Josefin Sans/JosefinSans-VariableFont_wght.ttf',66,500)
center('ROB O. TAYLOR',1430,fA,(244,238,222),spacing=10)
pass
fS=font('Cormorant Garamond/CormorantGaramond-Italic-VariableFont_wght.ttf',46,600)
center('A Brave New Times novel',1345,fS,(190,205,215)) if False else None
# tagline top
fq=font('Cormorant Garamond/CormorantGaramond-Italic-VariableFont_wght.ttf',58,600)
center('One of them is a bestseller.',70,fq,(235,225,200))
center('The other one is legally his.',140,fq,(235,225,200))
d.line([400,225,600,225],fill=gold,width=2)
fS2=font('Josefin Sans/JosefinSans-VariableFont_wght.ttf',34,500)
center('A BRITISH COMEDY OF IDENTITY',1525,fS2,gold,spacing=8)
img.convert('RGB').save(sys.argv[1] if len(sys.argv)>1 else 'cover.png')
print('ok')
