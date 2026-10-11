"""Five simple diagrams for The Will Is Not the Legacy, Actually.
Lines, shapes and text on coloured backgrounds. No names, no brands, no photos.
Output: 800 px wide palette PNGs in src/diagrams/. Run: python3 src/diagrams.py"""
from PIL import Image, ImageDraw, ImageFont
import os, textwrap
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'diagrams')
FD='/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf'
def F(sz,w=400):
    f=ImageFont.truetype(FD,sz)
    try: f.set_variation_by_axes([14 if sz<20 else 24, w])
    except Exception: pass
    return f
BG=(250,246,238); INK=(33,44,66); TEAL=(42,120,122); TEAL_L=(214,234,232)
RUST=(184,92,56); RUST_L=(245,224,212); GOLD=(214,168,74); GOLD_L=(248,236,206); GREY=(120,124,132); GREY_L=(230,230,228); WHITE=(255,255,255)
W=800
def wrap(d,xy,text,font,fill,width_px,align='left',spacing=4):
    x,y=xy; words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=font)<=width_px: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    h=font.size+spacing
    for i,l in enumerate(lines):
        lx=x if align=='left' else x+(width_px-d.textlength(l,font=font))/2
        d.text((lx,y+i*h),l,font=font,fill=fill)
    return y+len(lines)*h
def box(d,x0,y0,x1,y1,fill,outline,title,body=None,tf=None,bf=None,tcol=INK,r=12,center=True):
    d.rounded_rectangle((x0,y0,x1,y1),radius=r,fill=fill,outline=outline,width=3)
    tf=tf or F(20,700); bf=bf or F(16)
    y=wrap(d,(x0+12,y0+10),title,tf,tcol,x1-x0-24,'center' if center else 'left')
    if body: wrap(d,(x0+12,y+4),body,bf,INK,x1-x0-24,'center' if center else 'left')
def arrow(d,p0,p1,col=INK,w=3):
    d.line([p0,p1],fill=col,width=w)
    import math
    a=math.atan2(p1[1]-p0[1],p1[0]-p0[0]); L=12
    d.polygon([p1,(p1[0]-L*math.cos(a-0.45),p1[1]-L*math.sin(a-0.45)),(p1[0]-L*math.cos(a+0.45),p1[1]-L*math.sin(a+0.45))],fill=col)
def title(d,t,sub=None):
    d.text((30,22),t,font=F(28,700),fill=INK)
    if sub: wrap(d,(30,62),sub,F(17),GREY,W-60)
def save(img,name):
    p=os.path.join(OUT,name); img.convert('RGB').quantize(colors=24,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE).save(p,optimize=True); print(p,os.path.getsize(p))

def fig1():
    H=830; im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    title(d,'What passes outside the will','Each asset asks its own question first. Only what is left goes through the will.')
    box(d,250,105,550,165,INK,INK,'An asset at death',tcol=WHITE)
    qs=[('Does it have a beneficiary form or a POD/TOD designation?','Life insurance, retirement accounts, POD bank accounts, TOD securities'),
        ('Is the title held jointly with right of survivorship?','Joint tenancy, survivorship accounts and titles'),
        ('Is it recorded with a transfer-on-death deed?','California real estate with a recorded, valid TOD deed'),
        ('Is it owned by a living trust?','Anything retitled to the trustee during life')]
    y=195
    for i,(q,ex) in enumerate(qs):
        arrow(d,(400,y-30),(400,y))
        box(d,90,y,520,y+95,GOLD_L,GOLD,q,tf=F(17,600))
        arrow(d,(520,y+47),(575,y+47),TEAL)
        d.text((528,y+20),'yes',font=F(15,700),fill=TEAL)
        box(d,575,y,775,y+95,TEAL_L,TEAL,'Outside the will',ex,tf=F(16,700),bf=F(12))
        d.text((410,y+101),'no',font=F(15,700),fill=RUST)
        y+=128
    arrow(d,(400,y-30),(400,y))
    box(d,170,y,630,y+95,RUST_L,RUST,'Through the will (or the default rules)','Probate in California; certificate of inheritance or notarial will in Germany. Germany has no TOD deed; land passes through the heirs.',tf=F(19,700),bf=F(15))
    save(im,'fig1_outside_the_will.png')

def fig2():
    H=830; im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    title(d,'TOD deed or life estate deed?','California, simplified. Check every point with a lawyer before you sign.')
    cols=[(30,'Revocable TOD deed',TEAL,TEAL_L),(415,'Life estate deed',RUST,RUST_L)]
    rows=[('Child owns something now?','No. Nothing passes until death.','Yes. The remainder is the child\'s from the day it is recorded.'),
          ('Can you change your mind?','Yes, until death. There is no irrevocable form.','Only with the child\'s signature.'),
          ('Sell or refinance alone?','Yes.','No. The child must sign.'),
          ('Child\'s creditors, divorce, early death','Cannot reach what the child does not own yet.','Can reach or affect the remainder.'),
          ('Signing and recording','Two neutral witnesses, notary, record within 60 days of notarising.','Ordinary deed formalities; ask about consent under any recorded agreement.'),
          ('Gift tax return','No (nothing given during life).','Yes: Form 709 for a future-interest gift, whatever its value.'),
          ('Basis at death','New basis at death.','New basis at death (house is in the estate).'),
          ('Mortgage and equity investor','Death is usually a settlement event under a home equity investment contract.','The deed itself may be a transfer that needs consent or triggers settlement.')]
    y=105
    for x,t,c,cl in cols:
        d.rounded_rectangle((x,y,x+355,y+42),radius=10,fill=c); d.text((x+178-d.textlength(t,font=F(20,700))/2,y+9),t,font=F(20,700),fill=WHITE)
    y=158
    for lab,a,b in rows:
        d.text((30,y),lab,font=F(18,700),fill=INK)
        y2=y+26
        ya=wrap(d,(40,y2),a,F(17),INK,345); yb=wrap(d,(425,y2),b,F(17),INK,345)
        yy=max(ya,yb)+8
        d.line([(30,yy),(770,yy)],fill=GREY_L,width=2)
        y=yy+8
    save(im,'fig2_tod_vs_life_estate.png')

def fig3():
    H=560; im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    title(d,'The first ninety days after a death','Very little must be decided in the first forty-eight hours.')
    x0,x1,ly=60,740,200
    d.line([(x0,ly),(x1,ly)],fill=INK,width=5)
    marks=[(0,'Day 1-2'),(14,'Week 2'),(42,'Week 6'),(90,'Day 90')]
    for dd,t in marks:
        x=x0+(x1-x0)*dd/90; d.ellipse((x-9,ly-9,x+9,ly+9),fill=GOLD,outline=INK,width=2)
        d.text((x-d.textlength(t,font=F(16,700))/2,ly-40),t,font=F(16,700),fill=INK)
    blocks=[(40,'First 48 hours',TEAL_L,TEAL,'Death certificate. Wishes about the body. Secure home, car and pets. Tell close family. Find the documents.'),
            (225,'First two weeks',GOLD_L,GOLD,'Original will to the court (California: within 30 days). Funeral, keep receipts. Call the lawyer or notary. Notify benefits and pensions.'),
            (410,'By week six',RUST_L,RUST,'Germany: decide within six weeks whether to disclaim. California: work out what passes outside probate.'),
            (595,'By day ninety',TEAL_L,TEAL,'Inventory. Estate account once you have authority. Notify institutions. Taxes. Do not distribute too early.')]
    for x,t,cl,c,body in blocks:
        d.line([(x+82,ly+12),(x+82,ly+40)],fill=c,width=3)
        box(d,x,ly+40,x+165,ly+300,cl,c,t,body,tf=F(17,700),bf=F(14))
    wrap(d,(30,H-48),'Do not cancel cloud storage until photos and recordings have been downloaded.',F(15,600),RUST,W-60)
    save(im,'fig3_first_ninety_days.png')

def fig4():
    H=640; im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    title(d,'The Family List: what it points to','The list says what exists and where it is kept. Passwords stay in the password manager.')
    cx,cy=400,350
    items=[(130,170,'Bank accounts','Institution, last 4 digits, statements: binder section 2'),
           (400,145,'Insurance','Policy numbers, beneficiaries: binder section 5'),
           (670,170,'Investments and pensions','Provider, account type, beneficiary form copy'),
           (130,520,'Passwords','Password manager with emergency access; device codes sealed with the will'),
           (400,560,'Documents','Original will, powers of attorney, deeds: where each original is'),
           (670,520,'Property and debts','Deeds, mortgage, anything recorded against the house')]
    for x,y,t,b in items: d.line([(cx,cy),(x,y)],fill=GREY,width=3)
    d.ellipse((cx-115,cy-62,cx+115,cy+62),fill=INK)
    wrap(d,(cx-100,cy-30),'The Family List',F(24,700),WHITE,200,'center'); wrap(d,(cx-100,cy+4),'one record, kept current',F(15),GOLD_L,200,'center')
    for i,(x,y,t,b) in enumerate(items):
        cl,c=[(TEAL_L,TEAL),(GOLD_L,GOLD),(RUST_L,RUST)][i%3]
        box(d,x-120,y-48,x+120,y+52,cl,c,t,b,tf=F(17,700),bf=F(13))
    save(im,'fig4_family_list_map.png')

def fig5():
    H=560; im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    title(d,'A simple video-diary setup','Seen from above. A window, a propped phone, a quiet room.')
    # room
    d.rectangle((60,110,520,520),outline=INK,width=4,fill=WHITE)
    d.rectangle((150,100,430,120),fill=TEAL_L,outline=TEAL,width=3); d.text((235,124),'window: light on your face',font=F(14,600),fill=TEAL)
    # phone on tripod
    d.rounded_rectangle((268,215,312,240),radius=6,fill=INK); d.text((322,212),'phone, landscape,',font=F(14),fill=INK); d.text((322,230),'lens at eye level',font=F(14),fill=INK)
    for dx in (-18,0,18): d.line([(290,240),(290+dx,262)],fill=GREY,width=3)
    # person in chair
    d.rounded_rectangle((235,380,345,470),radius=18,fill=GOLD_L,outline=GOLD,width=3); d.ellipse((265,340,315,390),fill=RUST_L,outline=RUST,width=3)
    d.text((235,476),'you, chest up in frame',font=F(14,600),fill=INK)
    # distance
    arrow(d,(290,330),(290,270),RUST); arrow(d,(290,270),(290,330),RUST)
    d.text((300,288),'about an arm\'s length',font=F(14),fill=RUST)
    # soft furnishings
    d.rectangle((75,300,135,500),fill=GREY_L,outline=GREY,width=2); d.text((80,505),'sofa, books',font=F(12),fill=GREY)
    d.rectangle((395,420,480,505),fill=GREY_L,outline=GREY,width=2); d.text((392,398),'lamp for evenings',font=F(12),fill=GREY); d.ellipse((425,450,450,475),fill=GOLD)
    tips=[('Light','Face the window. No window behind you. Evening: a lamp in front, slightly to one side.'),
          ('Sound','Quiet room, soft furnishings. A clip-on microphone is the best upgrade. Test with headphones.'),
          ('Camera','Propped, never hand-held. 1080p is plenty. Look at the lens, not the screen.'),
          ('Start','Say your name, the date, where you are, and who the message is for.')]
    y=115
    for t,b in tips:
        d.text((545,y),t,font=F(18,700),fill=TEAL); y=wrap(d,(545,y+24),b,F(14),INK,230)+14
    save(im,'fig5_video_diary_setup.png')

if __name__=='__main__':
    os.makedirs(OUT,exist_ok=True)
    for f in (fig1,fig2,fig3,fig4,fig5): f()
