import numpy as np, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from dolphin import outline
W,H=1600,2560
import os
G=os.environ.get('GOOGLE_FONTS','/usr/share/fonts/truetype/sand-box/google/')  # Cinzel, EB Garamond, Marcellus SC (Google Fonts, OFL)
def font(path,size,var=None):
    f=ImageFont.truetype(G+path,size)
    if var:
        names=[n.decode() if isinstance(n,bytes) else n for n in f.get_variation_names()]
        f.set_variation_by_name(var.encode() if var in names else names[min(len(names)-1,2)].encode())
    return f
NAVY=(20,48,74); GOLD=(176,138,62); CREAM=(244,236,216); TEAL1=(30,92,115); TEAL2=(10,36,54)
img=Image.new('RGB',(W,H))
px=np.zeros((H,W,3),float)
HZ=1640  # horizon
top=np.array([243,235,214]); mid=np.array([229,214,180])
for y in range(HZ):
    px[y]=top+(mid-top)*(y/HZ)**1.4
for y in range(HZ,H):
    t=(y-HZ)/(H-HZ); px[y]=np.array(TEAL1)+(np.array(TEAL2)-np.array(TEAL1))*t**0.8
rng=np.random.default_rng(7); px+=rng.normal(0,2.2,(H,W,1))
img=Image.fromarray(np.clip(px,0,255).astype('uint8'))
d=ImageDraw.Draw(img)
# --- title
def ctext(y,txt,f,fill,track=0):
    if track:
        ws=[d.textlength(c,font=f) for c in txt]; tw=sum(ws)+track*(len(txt)-1); x=(W-tw)/2
        for c,w in zip(txt,ws): d.text((x,y),c,font=f,fill=fill); x+=w+track
    else:
        tw=d.textlength(txt,font=f); d.text(((W-tw)/2,y),txt,font=f,fill=fill)
fs=font('Cinzel/Cinzel-VariableFont_wght.ttf',86,'SemiBold')
fb=font('Cinzel/Cinzel-VariableFont_wght.ttf',250,'Bold')
fm=font('Cinzel/Cinzel-VariableFont_wght.ttf',120,'SemiBold')
d.line([(300,250),(1300,250)],fill=GOLD,width=4); d.line([(300,262),(1300,262)],fill=GOLD,width=1)
ctext(310,'THE DOLPHINS\u2019',fm,NAVY,track=8)
ctext(480,'VIEW OF',fs,GOLD,track=22)
ctext(590,'HISTORY',fb,NAVY,track=6)
d.line([(300,900),(1300,900)],fill=GOLD,width=1); d.line([(300,912),(1300,912)],fill=GOLD,width=4)
fi=font('EB Garamond/EBGaramond-Italic-VariableFont_wght.ttf',66)
ctext(960,'A Non-Human, Non-Building Species',fi,NAVY)
ctext(1040,'Delivers Its Verdicts',fi,NAVY)
# --- timeline along the horizon
ft=font('Marcellus SC/MarcellusSC-Regular.ttf',38)
marks=[(150,'3200 BCE'),(390,'776 BCE'),(940,'1492'),(1135,'1789'),(1300,'1969'),(1470,'2026')]
d.line([(80,HZ-6),(W-80,HZ-6)],fill=GOLD,width=3)
for x,l in marks:
    d.ellipse([x-9,HZ-15,x+9,HZ+3],fill=GOLD)
    tw=d.textlength(l,font=ft); d.text((x-tw/2,HZ-78),l,font=ft,fill=NAVY)
# --- dolphin leaping (navy silhouette), drawn at 4x and downsampled for smooth edges
o=outline(); S=4
L=680; ang=math.radians(40)
c,s_=math.cos(ang),math.sin(ang)
cx,cy=850,1500
pts=[]
for x,y in o:
    X=(x-0.5)*L; Y=y*L
    pts.append(((cx+X*c-Y*s_)*S,(cy-(X*s_+Y*c))*S))
lay=Image.new('L',(W*S,H*S),0); ImageDraw.Draw(lay).polygon(pts,fill=255)
lay=lay.resize((W,H),Image.LANCZOS)
img.paste(Image.new('RGB',(W,H),NAVY),(0,0),lay)
water=Image.fromarray(np.clip(px,0,255).astype('uint8')).crop((0,HZ,W,H)); img.paste(Image.blend(img.crop((0,HZ,W,H)),water,0.7),(0,HZ))
d=ImageDraw.Draw(img)
# eye
ex,ey=0.845,0.035; X=(ex-0.5)*L; Y=ey*L
d.ellipse([cx+X*c-Y*s_-5,cy-(X*s_+Y*c)-5,cx+X*c-Y*s_+5,cy-(X*s_+Y*c)+5],fill=CREAM)
# splash and ripples where the tail leaves the water
tx=cx-190
for i,(rw,rh,a) in enumerate([(260,26,170),(400,40,110),(560,56,60)]):
    r=Image.new('L',(W,H),0); ImageDraw.Draw(r).ellipse([tx-rw/2,HZ+40-rh/2+i*30,tx+rw/2,HZ+40+rh/2+i*30],outline=a,width=5)
    img.paste(Image.new('RGB',(W,H),CREAM),(0,0),r)
# --- author block on the sea
fa=font('Marcellus SC/MarcellusSC-Regular.ttf',96)
fn=font('EB Garamond/EBGaramond-Italic-VariableFont_wght.ttf',50)
ctext(2120,'As told by Professor Click-Click-Whoosh',fn,(214,200,166))
d.line([(560,2215),(1040,2215)],fill=GOLD,width=2)
ctext(2260,'LOTHAR J. MUSIOL',fa,CREAM,track=6)
img.convert('RGB').save('KINDLE_COVER_FINAL_2560.jpg',quality=92)

