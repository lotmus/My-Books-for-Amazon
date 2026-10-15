"""Back cover for The Universe Has No Now: single colour (the front's near-black), text only, same type as the front."""
from PIL import Image, ImageDraw, ImageFont
S=2; W,H=1600*S,2560*S
B='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'; R='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'; I='/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf'
f=lambda p,s: ImageFont.truetype(p,int(s*S))
BG=(16,16,18); CREAM=(238,234,222); GOLD=(212,160,84); GREY=(150,148,142); LINE=(80,80,84)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
d.rectangle([60*S,60*S,W-60*S,H-60*S],outline=LINE,width=2*S)
L,Rr=180*S,W-180*S; CW=Rr-L
def wrap(t,font,w):
    out=[];cur=''
    for word in t.split():
        x=(cur+' '+word).strip()
        if d.textlength(x,font=font)<=w: cur=x
        else: out.append(cur); cur=word
    out.append(cur); return out
def para(y,t,font,fill,lead,center=False,w=CW,x0=L):
    for ln in wrap(t,font,w):
        x=x0+(w-d.textlength(ln,font=font))/2 if center else x0
        d.text((x,y),ln,font=font,fill=fill); y+=lead
    return y
def rule(y): d.line([(L+120*S,y),(Rr-120*S,y)],fill=LINE,width=2*S)
y=348*S
hk=f(B,66)
y=para(y,'There is a clock on the kitchen wall, and it is lying to you.',hk,CREAM,86*S,center=True)
y=para(y+6*S,'Not by being fast or slow, but by pretending that “now” is a thing the universe shares.',f(R,40),GOLD,54*S,center=True,w=CW-80*S,x0=L+40*S)
y+=40*S; rule(y); y+=60*S
body=f(R,38); lead=56*S
for t in ['The Universe Has No Now starts where the physics starts: with events, not a solar-system tour. Two people in one kitchen can disagree about which events are simultaneous without either being wrong. Light is late on purpose, and your life is a thin thread through a four-dimensional loaf.',
          'Then the book rebuilds the past we can actually reconstruct: a hot beginning with no center, a leftover microwave glow, three minutes that forged most of the helium in your kitchen, and a cosmic inventory in which ordinary atoms are the minority. Black holes arrive as one-way facts, wormholes and warps stay on the table long enough to show the bill, and getting somewhere else looks like a greenhouse on a dead world and a radio that answers a quarter-hour late.']:
    y=para(y,t,body,CREAM,lead)+28*S
y+=10*S; rule(y); y+=60*S
t=f(B,40); y=para(y,'Every claim wears a temperature.',t,CREAM,56*S,center=True)+24*S
cols=[('HOT','Measured.'),('WARM','The best working account, with gaps.'),('COLD','Allowed by the equations, not selected by the data.')]
cw=(CW-80*S)/3; top=y
for k,(h,tx) in enumerate(cols):
    x=L+k*(cw+40*S); hw=d.textlength(h,font=f(B,42)); d.text((x+(cw-hw)/2,top),h,font=f(B,42),fill=GOLD)
    para(top+62*S,tx,f(R,34),CREAM,46*S,center=True,w=cw,x0=x)
y=top+62*S+3*46*S+40*S; rule(y); y+=60*S
y=para(y,'Short chapters, invented scenes with real numbers, and an appendix for readers who want the Friedmann equation. No physics degree required; only curiosity, and a willingness to let the clock come apart.',f(I,36),GREY,52*S,center=True,w=CW-60*S,x0=L+30*S)
y+=50*S
nm=f(B,48); s='LOTHAR J. MUSIOL'
# letter-spaced like the front
sp=8*S; tw=sum(d.textlength(c,font=nm) for c in s)+sp*(len(s)-1); x=(W-tw)/2
for c in s: d.text((x,y),c,font=nm,fill=CREAM); x+=d.textlength(c,font=nm)+sp
y+=90*S
para(y,'Look First · Volume 1. A complete book. Volume 2 is A Trip Is Not a New Life.',f(R,32),GREY,46*S,center=True)
print('bottom',y/S+60)
out=im.resize((1600,2560),Image.LANCZOS); out.save('KINDLE_BACK_COVER_2560.jpg',quality=92,subsampling=0)
t=out.copy(); t.thumbnail((640,1024)); t.save('pv_back.jpg',quality=85)
