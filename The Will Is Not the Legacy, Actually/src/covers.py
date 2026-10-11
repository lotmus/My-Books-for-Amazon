"""Front and back covers for 'The Will Is Not the Legacy, Actually'.
Pure typography and drawn shapes: no photographs or third-party images.
Fonts (SIL Open Font License, Google Fonts): DM Serif Display, Lora, Inter, Caveat.
Run from the book folder:  python src/covers.py
"""
import os, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE=os.path.dirname(os.path.abspath(__file__)); BOOK=os.path.dirname(HERE)
FD='/usr/share/fonts/truetype/sand-box/google/'
F_TITLE=FD+'DM Serif Display/DMSerifDisplay-Regular.ttf'
F_TITLE_I=FD+'DM Serif Display/DMSerifDisplay-Italic.ttf'
F_SUB=FD+'Lora/Lora-Italic-VariableFont_wght.ttf'
F_BODY=FD+'Lora/Lora-VariableFont_wght.ttf'
F_SANS=FD+'Inter/Inter-VariableFont_opsz,wght.ttf'
F_HAND=FD+'Caveat/Caveat-VariableFont_wght.ttf'

W,H=1600,2560; S=2            # draw at 2x, downsample for smooth edges
PAPER=(244,239,230); NAVY=(31,42,68); RED=(158,42,43); INK=(52,58,72); GOLD=(190,150,80)

def font(path,size,wght=None):
    f=ImageFont.truetype(path,size*S)
    if wght:
        try: f.set_variation_by_axes([wght] if 'Inter' not in path else [14,wght])
        except Exception:
            try: f.set_variation_by_axes([wght])
            except Exception: pass
    return f

def paper(w,h,seed=3):
    random.seed(seed)
    im=Image.new('RGB',(w,h),PAPER)
    noise=Image.effect_noise((w//4,h//4),18).resize((w,h)).filter(ImageFilter.GaussianBlur(2))
    return Image.blend(im,Image.merge('RGB',(noise,noise,noise)),0.05)

def fit(path,text,maxw,start,wght=None):
    sz=start
    while sz>10:
        f=font(path,sz,wght)
        if f.getlength(text)<=maxw*S: return f
        sz-=2
    return font(path,10,wght)

def illustration(d,cx,cy,k=1.0):
    """A folded will with a wax seal, a phone with a play button, a checklist card."""
    u=lambda v:int(v*S*k)
    X=lambda v:int(cx*S+v*S*k); Y=lambda v:int(cy*S+v*S*k)
    # checklist card (back, left, tilted feel via offset)
    d.rounded_rectangle((X(-430),Y(-170),X(-90),Y(260)),radius=u(18),fill=(255,252,246),outline=INK,width=u(5))
    for i in range(4):
        yy=-100+i*85
        d.rounded_rectangle((X(-390),Y(yy),X(-345),Y(yy+45)),radius=u(6),outline=INK,width=u(5))
        if i<3: d.line([(X(-382),Y(yy+24)),(X(-368),Y(yy+38)),(X(-338),Y(yy+2))],fill=RED,width=u(8),joint='curve')
        d.line([(X(-320),Y(yy+22)),(X(-130),Y(yy+22))],fill=(150,150,150),width=u(5))
    # document (centre)
    d.polygon([(X(-170),Y(-300)),(X(130),Y(-300)),(X(200),Y(-230)),(X(200),Y(330)),(X(-170),Y(330))],fill=(255,253,248),outline=INK,width=u(6))
    d.polygon([(X(130),Y(-300)),(X(130),Y(-230)),(X(200),Y(-230))],fill=(230,224,212),outline=INK,width=u(5))
    hand=font(F_HAND,int(64*k),600)
    d.text((X(15),Y(-200)),'My Will',font=hand,fill=NAVY,anchor='mm')
    for i in range(6):
        y=-110+i*52; x2=150 if i%3!=2 else 60
        d.line([(X(-120),Y(y)),(X(x2),Y(y))],fill=(160,160,160),width=u(5))
    # wax seal
    d.ellipse((X(-60),Y(190),X(80),Y(330)),fill=RED)
    d.ellipse((X(-38),Y(212),X(58),Y(308)),outline=(120,28,30),width=u(6))
    # phone (front, right)
    d.rounded_rectangle((X(120),Y(-120),X(400),Y(380)),radius=u(36),fill=NAVY)
    d.rounded_rectangle((X(140),Y(-90),X(380),Y(340)),radius=u(16),fill=(238,232,220))
    d.polygon([(X(225),Y(55)),(X(225),Y(185)),(X(320),Y(120))],fill=RED)
    d.rounded_rectangle((X(225),Y(-110),X(295),Y(-100)),radius=u(4),fill=(90,100,125))

def front():
    im=paper(W*S,H*S); d=ImageDraw.Draw(im)
    # top band rule
    d.rectangle((0,0,W*S,22*S),fill=NAVY)
    lines=['The Will','Is Not the','Legacy,']
    f=fit(F_TITLE,'Is Not the',1360,330)
    y=320
    for ln in lines:
        d.text((W//2*S,y*S),ln,font=f,fill=NAVY,anchor='ms'); y+=300
    fa=font(F_TITLE_I,int(f.size/S*0.9))
    d.text((W//2*S,(y+10)*S),'Actually',font=fa,fill=RED,anchor='ms')
    illustration(d,W//2,1620,1.05)
    fs=font(F_SUB,62,500)
    for i,ln in enumerate(['Wills, the real alternatives, video messages,','and the family list that keeps it all usable']):
        d.text((W//2*S,(2120+i*84)*S),ln,font=fs,fill=INK,anchor='ms')
    d.line([(W//2*S-160*S,2260*S),(W//2*S+160*S,2260*S)],fill=GOLD,width=4*S)
    fau=fit(F_SANS,'LOTHAR J. MUSIOL',900,96,650)
    d.text((W//2*S,2430*S),'LOTHAR J. MUSIOL',font=fau,fill=NAVY,anchor='ms')
    return im.resize((W,H),Image.LANCZOS)

BLURB=[
"Most families assume the will decides who gets what. Often it does not. A retirement form signed twenty years ago, a deed, a joint account, an insurance policy that says \u201cmy heirs\u201d: these decide first, and the will gets what is left.",
"This book follows twenty-four invented families into the real rules of California and Germany: what they assumed, what actually happened, what would have prevented it, and what to do now, including what to do if it has already happened to you.",
"It also covers what a will cannot carry: powers of attorney and healthcare wishes for the long middle, one family list of every account and the safe route to every password, video messages and diaries recorded on an ordinary phone, and the letters that explain why.",
"With printable to-do lists for you and for your family, worksheets with filled examples, and California and Germany side by side.",
]
def wrap(t,f,maxw):
    out=[];line=''
    for w in t.split():
        test=(line+' '+w).strip()
        if f.getlength(test)<=maxw: line=test
        else: out.append(line); line=w
    out.append(line); return out

def back():
    im=paper(W*S,H*S,seed=5); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W*S,22*S),fill=NAVY)
    ft=font(F_TITLE,92); d.text((W//2*S,250*S),'The Will Is Not the Legacy,',font=ft,fill=NAVY,anchor='ms')
    d.text((W//2*S,355*S),'Actually',font=font(F_TITLE_I,92),fill=RED,anchor='ms')
    d.line([(W//2*S-160*S,420*S),(W//2*S+160*S,420*S)],fill=GOLD,width=4*S)
    fb=font(F_BODY,47,420); y=530
    for para in BLURB:
        for ln in wrap(para,fb,1240*S):
            d.text((180*S,y*S),ln,font=fb,fill=INK); y+=68
        y+=40
    print('blurb bottom',y)
    illustration(d,W//2,2085,0.38)
    fn=font(F_SANS,34,400)
    d.text((W//2*S,2320*S),'Educational guide, not legal advice. All families in this book are fictional.',font=fn,fill=(110,110,110),anchor='ms')
    d.text((W//2*S,2455*S),'LOTHAR J. MUSIOL',font=font(F_SANS,64,650),fill=NAVY,anchor='ms')
    return im.resize((W,H),Image.LANCZOS)

if __name__=='__main__':
    out=os.environ.get('COVER_OUT',BOOK)
    fr=front(); bk=back()
    fp=os.path.join(out,'The Will Is Not the Legacy, Actually - Front Cover (Kindle).jpg')
    bp=os.path.join(out,'The Will Is Not the Legacy, Actually - Back Cover.jpg')
    fr.save(fp,quality=93,dpi=(300,300)); bk.save(bp,quality=93,dpi=(300,300))
    print(fp, fr.size); print(bp, bk.size)
