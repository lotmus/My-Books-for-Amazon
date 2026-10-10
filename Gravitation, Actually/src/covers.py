from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import random
src=Image.open('cover.jpg').convert('RGB')   # 1152x1712, title baked in at top
W0,H0=src.size
# 1) remove baked-in lettering: rebuild rows 0..330 from the clean star band 340..670
art=src.copy()
patch=src.crop((0,522,W0,636))   # clean star band
ph=patch.height; y=0; k=0
import random
random.seed(7)
while y<522:
    t=patch
    if k%2: t=t.transpose(Image.FLIP_LEFT_RIGHT)
    if k%3==1: t=t.transpose(Image.FLIP_TOP_BOTTOM)
    off=random.randint(0,W0-1)
    t=Image.fromarray(__import__('numpy').roll(__import__('numpy').array(t),off,axis=1))
    art.paste(t,(0,y)); y+=ph; k+=1
mask=Image.new('L',(W0,40),0)
for yy in range(40): ImageDraw.Draw(mask).line([(0,yy),(W0,yy)],fill=int(255*yy/39))
art.paste(src.crop((0,522,W0,562)),(0,522),mask)
# 2) scale to 2560 high and crop to 1600 wide
s=2560/H0; art=art.resize((round(W0*s),2560),Image.LANCZOS)
x0=(art.width-1600)//2; art=art.crop((x0,0,x0+1600,2560))
art.save('cover_clean_art.jpg',quality=95)
F='/usr/share/fonts/truetype/sand-box/google/Cormorant SC/CormorantSC-Bold.ttf'
FS='/usr/share/fonts/truetype/sand-box/custom/Source Sans Pro/SourceSansPro-Semibold.ttf'
FSR='/usr/share/fonts/truetype/sand-box/custom/Source Sans Pro/SourceSansPro-Regular.ttf'
FI='/usr/share/fonts/truetype/sand-box/google/Cormorant Garamond/CormorantGaramond-Italic-VariableFont_wght.ttf'
def fit(text,font,maxw,start):
    sz=start
    while sz>20:
        f=ImageFont.truetype(font,sz); w=f.getbbox(text)[2]-f.getbbox(text)[0]
        if w<=maxw: return f
        sz-=4
def glow_text(base,xy_center,text,font,fill,glow=(120,170,255),radius=18,anchor='ms'):
    layer=Image.new('RGBA',base.size,(0,0,0,0)); d=ImageDraw.Draw(layer)
    d.text(xy_center,text,font=font,fill=glow+(200,),anchor=anchor)
    layer=layer.filter(ImageFilter.GaussianBlur(radius))
    base.alpha_composite(layer)
    d=ImageDraw.Draw(base); d.text(xy_center,text,font=font,fill=fill,anchor=anchor)
front=art.convert('RGBA')
# darken the top so letters pop
grad=Image.new('RGBA',front.size,(0,0,0,0)); gd=ImageDraw.Draw(grad)
for y in range(1000): gd.line([(0,y),(1600,y)],fill=(0,0,0,int(150*(1-y/1000))))
front.alpha_composite(grad)
ft=fit('GRAVITATION,',F,1440,260)
glow_text(front,(800,430),'GRAVITATION,',ft,(250,246,236,255))
fa=fit('ACTUALLY',F,900,200)
glow_text(front,(800,640),'ACTUALLY',fa,(250,246,236,255))
fsub=ImageFont.truetype(FI,78); fsub.set_variation_by_axes([600]) if hasattr(fsub,'set_variation_by_axes') else None
d=ImageDraw.Draw(front); d.text((800,775),'A Short Book on Gravity',font=fsub,fill=(236,201,122,255),anchor='ms')
fau=fit('LOTHAR J. MUSIOL',FS,900,96)
glow_text(front,(800,2470),'LOTHAR J. MUSIOL',fau,(255,255,255,255),glow=(0,0,0),radius=10)
front.convert('RGB').save('front_new.jpg',quality=92,dpi=(300,300))
# back cover
back=art.filter(ImageFilter.GaussianBlur(3)); back=ImageEnhance.Brightness(back).enhance(0.45).convert('RGBA')
panel=Image.new('RGBA',back.size,(0,0,0,0)); pd=ImageDraw.Draw(panel)
pd.rounded_rectangle((110,170,1490,1700),radius=30,fill=(8,12,24,205),outline=(236,201,122,180),width=3)
back.alpha_composite(panel)
d=ImageDraw.Draw(back)
fh=ImageFont.truetype(F,96); d.text((800,330),'Gravitation, Actually',font=fh,fill=(250,246,236,255),anchor='ms')
d.text((800,420),'A Short Book on Gravity',font=fsub,fill=(236,201,122,255),anchor='ms')
blurb=["Let go of an apple and nothing pulls it down. It is on the straight path. The floor is what gets in the way.",
"Gravitation, Actually tells Einstein’s picture of gravity in ordinary words and brings it up to what has actually been measured: clocks in orbit that would wreck your phone’s map without a correction, tides that show gravity is a mismatch of straight paths, stars with a last size, the shadow of a black hole, and ripples in spacetime caught in 2015.",
"Two equations, said in words. No tensors. Every chapter has an opener and a recap, Core and Extension sections, and exercises with worked solutions that show the usual mistake.",
"For curious readers who want the real idea, not a slogan."]
fb=ImageFont.truetype(FSR,50)
def wrap(t,f,maxw):
    out=[];line=''
    for w in t.split():
        test=(line+' '+w).strip()
        if f.getlength(test)<=maxw: line=test
        else: out.append(line); line=w
    out.append(line); return out
y=540
for para in blurb:
    for ln in wrap(para,fb,1200):
        d.text((200,y),ln,font=fb,fill=(240,240,240,255)); y+=66
    y+=34
print('blurb bottom',y)
d.text((800,2120),'LOTHAR J. MUSIOL',font=ImageFont.truetype(FS,70),fill=(255,255,255,255),anchor='ms')
d.text((800,2200),'Physics, Actually  ·  Math, Actually  ·  Quantum, Actually',font=ImageFont.truetype(FSR,40),fill=(200,200,200,255),anchor='ms')
back.convert('RGB').save('back_new.jpg',quality=92,dpi=(300,300))
for f in ['front_new.jpg','back_new.jpg']: im=Image.open(f); print(f,im.size)
Image.open('front_new.jpg').resize((400,640)).save('pv/grav_front_s.jpg'); Image.open('back_new.jpg').resize((400,640)).save('pv/grav_back_s.jpg')
a=Image.open('pv/grav_front_s.jpg');b=Image.open('pv/grav_back_s.jpg');c=Image.new('RGB',(800,640));c.paste(a,(0,0));c.paste(b,(400,0));c.save('pv/grav_covers.jpg')
