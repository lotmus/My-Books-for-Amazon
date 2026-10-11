from PIL import Image, ImageDraw, ImageFont
import textwrap
F='/usr/share/fonts/truetype/sand-box/custom/Source Serif Pro/SourceSerifPro-'
W,H=1200,1600; BG=(20,33,61); FG=(244,236,220); ACC=(240,180,90)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
def font(st,sz): return ImageFont.truetype(F+st+'.ttf',sz)
def para(y,txt,f,col=FG,width=1010,lead=1.42,center=True):
    words=txt.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=f)<=width: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur)
    for l in lines:
        x=(W-d.textlength(l,font=f))/2 if center else (W-width)/2
        d.text((x,y),l,font=f,fill=col); y+=int(f.size*lead)
    return y
y=175
y=para(y,'What does humanity actually know about reality?',font('Semibold',52),ACC,width=760,lead=1.25)+40
body=font('Regular',33)
y=para(y,'From the quarks inside a proton to the edge of the observable universe, and from the first self-copying molecules to the mind reading this page, this book sets out what science currently understands, how it came to understand it, and where the understanding stops.',body)+30
y=para(y,'Eleven parts climb two ladders. The first runs from the rules of motion and the quantum world through particles, atoms, relativity, stars and galaxies to the universe as a whole. The second runs from the origin of life through the body and brain, the living Earth and modern technology to the way knowledge itself is made and tested.',body)+30
y=para(y,'Along the way: why the Higgs boson matters, what gravitational waves revealed, how CRISPR edits a genome, what climate measurements show, what machine learning can and cannot do, and which questions remain open, from dark matter to consciousness.',body)+30
y=para(y,'Every claim comes with its evidence. Every uncertainty is named.',font('It',36) if False else font('Semibold',33),width=1060)+60
d.line([(W/2-160,y),(W/2+160,y)],fill=ACC,width=3); y+=50
y=para(y,'A guide to what is known. Actually.',font('Semibold',44),ACC)+20
para(H-150,'Lothar J. Musiol',font('Semibold',46),FG)
im.save('kindle back  cover.jpg',quality=92)
print(y)
