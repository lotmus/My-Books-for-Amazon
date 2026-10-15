"""Figure 9 (colour): Planck CMB map, ESA and the Planck Collaboration, CC BY 4.0 (Wikimedia Commons
'Cosmic Microwave Background (CMB).jpeg'). Cropped to the sky oval, 800x600 with a labelled cooler/warmer bar."""
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
src=Image.open('cmb.jpg').convert('RGB').crop((50,27,2599,1297))
W,H=800,600; c=Image.new('RGB',(W,H),'white')
m=ImageEnhance.Color(src.resize((780,389),Image.LANCZOS)).enhance(1.08)
mask=Image.new('L',(m.size[0]*4,m.size[1]*4),0); ImageDraw.Draw(mask).ellipse([0,0,mask.size[0]-1,mask.size[1]-1],fill=255); mask=mask.resize(m.size,Image.LANCZOS)
c.paste(m,(10,40),mask)
dr=ImageDraw.Draw(c)
B='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'; R='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
x0,x1,y=200,600,480
stops=[(0,(20,50,190)),(0.35,(110,170,230)),(0.5,(235,232,200)),(0.7,(240,170,70)),(1,(190,40,25))]
for x in range(x0,x1):
    t=(x-x0)/(x1-x0)
    for (t0,c0),(t1,c1) in zip(stops,stops[1:]):
        if t0<=t<=t1: s=(t-t0)/(t1-t0); col=tuple(int(c0[k]+s*(c1[k]-c0[k])) for k in range(3))
    dr.line([(x,y),(x,y+26)],fill=col)
dr.rectangle([x0,y,x1-1,y+26],outline=(90,90,90))
f=ImageFont.truetype(B,24); fr=ImageFont.truetype(R,20)
dr.text((x0-12-dr.textlength('cooler',font=f),y-1),'cooler',font=f,fill=(30,30,30)); dr.text((x1+12,y-1),'warmer',font=f,fill=(30,30,30))
s='differences of about one part in 100,000'; dr.text(((W-dr.textlength(s,font=fr))/2,y+40),s,font=fr,fill=(70,70,70))
c.save('fig09.jpg',quality=85)
