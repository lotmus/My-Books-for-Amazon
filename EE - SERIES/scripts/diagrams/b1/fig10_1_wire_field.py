from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from zipfile import ZipFile, ZIP_DEFLATED
import math, os
out=Path(r'EE - SERIES/scripts/diagrams/b1/fig/b1_wire_field.png')
W,H,S=1000,640,2
im=Image.new('RGB',(W*S,H*S),'white'); d=ImageDraw.Draw(im)
blue='#2A5CAA'; ink='#222222'; gray='#666666'
fontpath=r'C:\Windows\Fonts\arial.ttf'
def font(size): return ImageFont.truetype(fontpath,size*S)
cx,cy=300*S,285*S
for r0 in (90,155,220):
    r=r0*S; d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=blue,width=3*S)
    # At the top of a counter-clockwise field circle, the tangent points left.
    x1,y1=cx+0.67*r,cy-r; x2,y2=cx+0.28*r,cy-r
    d.line((x1,y1,x2,y2),fill=blue,width=4*S)
    ang=math.atan2(y2-y1,x2-x1)
    tip=(x2,y2); length=13*S; half=7*S
    base=(x2-length*math.cos(ang),y2-length*math.sin(ang))
    pts=[tip,(base[0]-half*math.sin(ang),base[1]+half*math.cos(ang)),(base[0]+half*math.sin(ang),base[1]-half*math.cos(ang))]
    d.polygon(pts,fill=blue)
d.ellipse((cx-20*S,cy-20*S,cx+20*S,cy+20*S),fill='white',outline=ink,width=3*S)
d.ellipse((cx-6*S,cy-6*S,cx+6*S,cy+6*S),fill=ink)
# Outside the field circles: leader makes the current symbol and direction explicit.
d.line((cx+16*S,cy-8*S,640*S,220*S),fill=ink,width=2*S)
d.polygon([(cx+16*S,cy-8*S),(cx+29*S,cy-8*S),(cx+23*S,cy+3*S)],fill=ink)
d.text((655*S,190*S),'I (out of page)',font=font(20),fill=ink)
label='B circles the wire; magnitude falls as 1/r'
bbox=d.textbbox((0,0),label,font=font(20)); tw=bbox[2]-bbox[0]
d.text(((W*S-tw)//2,570*S),label,font=font(20),fill=gray)
im.resize((W,H),Image.Resampling.LANCZOS).save(out)
# Replace exactly the original embedded image within the DOCX package.
docx=Path(r'EE - SERIES/Foundations_Book1_REV4.docx')
old=Path(r'EE - SERIES/chapters/Book1_REV4/fig/fig10_1.png').read_bytes(); new=out.read_bytes(); tmp=docx.with_suffix('.tmp.docx'); hits=0
with ZipFile(docx,'r') as zin, ZipFile(tmp,'w',ZIP_DEFLATED) as zout:
    for info in zin.infolist():
        data=zin.read(info.filename)
        if data==old: data=new; hits+=1
        zout.writestr(info,data)
if hits!=1:
    tmp.unlink(missing_ok=True); raise RuntimeError(f'Expected one image match, found {hits}')
os.replace(tmp,docx)
Path(r'EE - SERIES/chapters/Book1_REV4/fig/fig10_1.png').write_bytes(new)
print('replaced embedded Figure 10.1')
