# Rev10 (title renamed to Gravity, Actually; otherwise identical to cover9.py). Rev9 front and back covers, drawn from scratch (no AI art, no photos):
# a falling apple, strobed along a straight vertical worldline on a spacetime grid with a light cone.
import numpy as np, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1600,2560; S=2  # supersample
O='/workspace/grav10/img/'
F='/usr/share/fonts/truetype/sand-box/google/Cormorant SC/CormorantSC-Bold.ttf'
FS='/usr/share/fonts/truetype/sand-box/custom/Source Sans Pro/SourceSansPro-Semibold.ttf'
FSR='/usr/share/fonts/truetype/sand-box/custom/Source Sans Pro/SourceSansPro-Regular.ttf'
FI='/usr/share/fonts/truetype/sand-box/google/Cormorant Garamond/CormorantGaramond-Italic-VariableFont_wght.ttf'
CREAM=(250,244,230); GOLD=(236,196,110)
def background():
    y=np.linspace(0,1,H)[:,None]; x=np.linspace(0,1,W)[None,:]
    top=np.array([10,16,38]); bot=np.array([4,6,16])
    g=top[None,None,:]*(1-y[...,None])+bot[None,None,:]*y[...,None]
    r=np.sqrt((x-0.5)**2+((y-0.62)*0.7)**2); g=g+np.array([30,40,70])[None,None,:]*np.clip(0.55-r,0,1)[...,None]*0.9
    img=Image.fromarray(np.clip(g,0,255).astype('uint8')).convert('RGBA')
    rng=np.random.default_rng(11); d=ImageDraw.Draw(img)
    for _ in range(900):
        px,py=rng.integers(0,W),rng.integers(0,H); b=int(rng.uniform(60,200)); s=rng.choice([0,0,0,1])
        d.ellipse([px-s,py-s,px+s,py+s],fill=(b,b,min(255,b+20),255))
    return img
def grid(img,cx,cy):
    lay=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); d=ImageDraw.Draw(lay)
    step=120*S
    for k in range(-8,9):
        x=cx*S+k*step; a=int(70*max(0,1-abs(k)/8.5))+25
        d.line([x,0,x,H*S],fill=(140,170,230,a),width=2*S)
    for k in range(-14,14):
        y=cy*S+k*step; a=int(70*max(0,1-abs(k)/12))+20
        d.line([0,y,W*S,y],fill=(140,170,230,a),width=2*S)
    # light cone from the event at (cx,cy): straight 45-degree lines upward
    for sgn in (-1,1):
        d.line([cx*S,cy*S,cx*S+sgn*1100*S,cy*S-1100*S],fill=GOLD+(200,),width=5*S)
        d.line([cx*S,cy*S,cx*S+sgn*700*S,cy*S+700*S],fill=GOLD+(90,),width=3*S)
    lay=lay.resize((W,H),Image.LANCZOS); img.alpha_composite(lay)
def apple(size,alpha=255):
    n=size*S; A=Image.new('RGBA',(n,n),(0,0,0,0))
    yy,xx=np.mgrid[0:n,0:n]/n-0.5
    # apple body: union of two circles, notch on top
    c1=((xx+0.13)**2+(yy-0.04)**2)<0.30**2; c2=((xx-0.13)**2+(yy-0.04)**2)<0.30**2
    c3=((xx)**2+(yy-0.10)**2)<0.30**2
    notch=((xx)**2+(yy+0.36)**2)<0.10**2
    m=(c1|c2|c3)&~notch
    shade=np.clip(1.15-1.6*np.sqrt((xx+0.12)**2+(yy+0.08)**2),0.35,1.1)
    col=np.zeros((n,n,4)); col[...,0]=200*shade+20; col[...,1]=28*shade; col[...,2]=34*shade; col[...,3]=m*alpha
    hl=np.exp(-(((xx+0.16)/0.07)**2+((yy+0.06)/0.12)**2))*m
    col[...,0]+=hl*60; col[...,1]+=hl*80; col[...,2]+=hl*80
    A=Image.fromarray(np.clip(col,0,255).astype('uint8'))
    d=ImageDraw.Draw(A)
    d.line([n*0.50,n*0.25,n*0.53,n*0.08],fill=(92,58,30,alpha),width=int(n*0.035))
    leaf=Image.new('RGBA',(n,n),(0,0,0,0)); ld=ImageDraw.Draw(leaf)
    ld.ellipse([n*0.54,n*0.07,n*0.80,n*0.17],fill=(70,150,60,alpha)); ld.line([n*0.55,n*0.12,n*0.78,n*0.12],fill=(40,100,40,alpha),width=max(1,int(n*0.008)))
    leaf=leaf.rotate(18,center=(n*0.55,n*0.12),resample=Image.BICUBIC); A.alpha_composite(leaf)
    return A.resize((size,size),Image.LANCZOS)
def text_c(img,y,text,font,fill,glow=None,rad=16):
    if glow:
        lay=Image.new('RGBA',img.size,(0,0,0,0)); ImageDraw.Draw(lay).text((W//2,y),text,font=font,fill=glow,anchor='ms')
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(rad)))
    ImageDraw.Draw(img).text((W//2,y),text,font=font,fill=fill,anchor='ms')
def fit(text,font,maxw,start):
    sz=start
    while sz>20:
        f=ImageFont.truetype(font,sz)
        if f.getlength(text)<=maxw: return f
        sz-=4
def front():
    img=background(); cx,cy=800,2108
    grid(img,cx,cy)
    # strobe of the apple falling along one straight line: equal time steps, growing gaps
    lay=Image.new('RGBA',img.size,(0,0,0,0)); ImageDraw.Draw(lay).line([cx,1050,cx,2300],fill=GOLD+(110,),width=4)
    img.alpha_composite(lay)
    ys=[1100+28*(k+2)**2 for k in range(5)]
    for k,yv in enumerate(ys[:-1]):
        a=apple(150,alpha=int(60+40*k)); img.alpha_composite(a,(cx-75,yv-75))
    sh=Image.new('RGBA',img.size,(0,0,0,0)); ImageDraw.Draw(sh).ellipse([cx-140,ys[-1]-130,cx+140,ys[-1]+150],fill=(255,120,90,80))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(40)))
    a=apple(250); img.alpha_composite(a,(cx-125,ys[-1]-125))
    # darken top for the title
    grad=Image.new('RGBA',img.size,(0,0,0,0)); gd=ImageDraw.Draw(grad)
    for y in range(1150): gd.line([(0,y),(W,y)],fill=(0,0,0,int(170*(1-y/1150))))
    img.alpha_composite(grad)
    text_c(img,420,'GRAVITY,',fit('GRAVITY,',F,1460,300),CREAM+(255,),glow=(110,150,255,190))
    text_c(img,650,'ACTUALLY',fit('ACTUALLY',F,1000,250),CREAM+(255,),glow=(110,150,255,190))
    fs=ImageFont.truetype(FI,84)
    try: fs.set_variation_by_axes([600])
    except Exception: pass
    text_c(img,800,"Einstein’s Relativity in Plain Words",fs,GOLD+(255,))
    fs2=ImageFont.truetype(FI,62)
    try: fs2.set_variation_by_axes([500])
    except Exception: pass
    text_c(img,900,'Falling, Time, Black Holes,',fs2,(220,215,200,255))
    text_c(img,980,'and the Waves We Finally Heard',fs2,(220,215,200,255))
    fau=fit('LOTHAR J. MUSIOL',FS,1040,128)
    lay=Image.new('RGBA',img.size,(0,0,0,0)); ImageDraw.Draw(lay).rectangle([0,2330,W,H],fill=(0,0,0,150))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(30)))
    text_c(img,2470,'LOTHAR J. MUSIOL',fau,(255,255,255,255))
    out=img.convert('RGB'); out.save(O+'front_v4.jpg',quality=90,dpi=(300,300)); return out
def back(blurb):
    img=background(); grid(img,800,2150)
    panel=Image.new('RGBA',img.size,(0,0,0,0)); pd=ImageDraw.Draw(panel)
    pd.rounded_rectangle((110,170,1490,1690),radius=30,fill=(8,12,24,215),outline=GOLD+(180,),width=3)
    img.alpha_composite(panel); d=ImageDraw.Draw(img)
    d.text((800,320),'Gravity, Actually',font=ImageFont.truetype(F,96),fill=CREAM,anchor='ms')
    fi=ImageFont.truetype(FI,58)
    d.text((800,410),"Einstein’s Relativity in Plain Words",font=fi,fill=GOLD,anchor='ms')
    fb=ImageFont.truetype(FSR,46); y=520; lh=62
    for para in blurb:
        words=para.split(); line=''
        for w in words:
            t=(line+' '+w).strip()
            if fb.getlength(t)<=1200: line=t
            else: d.text((200,y),line,font=fb,fill=(235,235,235)); y+=lh; line=w
        d.text((200,y),line,font=fb,fill=(235,235,235)); y+=lh+26
    a=apple(220); img.alpha_composite(a,(690,1950))
    d.text((800,2330),'LOTHAR J. MUSIOL',font=ImageFont.truetype(FS,74),fill='white',anchor='ms')
    d.text((800,2420),'Physics, Actually  ·  Math, Actually  ·  Quantum, Actually',font=ImageFont.truetype(FSR,40),fill=(200,200,200),anchor='ms')
    print('back text bottom y',y)
    img.convert('RGB').save(O+'back_v4.jpg',quality=90,dpi=(300,300))
f=front()
f.resize((100,160),Image.LANCZOS).save(O+'front_v4_100px.png'); f.resize((400,640),Image.LANCZOS).save(O+'front_v4_400px.png')
back(["Let go of an apple and nothing pulls it down. It is already on the straightest path there is. The floor is what gets in the way.",
 "So why do astronauts float where gravity is still 89 percent as strong as on the ground? Why would your phone’s map be kilometers off within a day without Einstein? Why does the sea rise twice a day, and why is a black hole’s edge a door and not a wall?",
 "Gravity, Actually answers in ordinary words and brings the story up to what has been measured: clocks in orbit, the shadows of two black holes, and the ripples in spacetime first caught in 2015.",
 "Two equations, said in words. Core and Extension sections, so you choose the short road or the long one, and optional exercises with worked solutions for readers who like to check.",
 "For curious readers who want the real idea, not a slogan."])
