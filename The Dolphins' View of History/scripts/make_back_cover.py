from PIL import Image, ImageDraw, ImageFont
W,H=1600,2560
import os
G=os.environ.get('GOOGLE_FONTS','/usr/share/fonts/truetype/sand-box/google/')  # Cinzel, EB Garamond, Marcellus SC (Google Fonts, OFL)
def font(p,s,var=None):
    f=ImageFont.truetype(G+p,s)
    if var: f.set_variation_by_name(var)
    return f
NAVY=(20,48,74); GOLD=(196,160,88); CREAM=(244,236,216)
img=Image.new('RGB',(W,H),NAVY); d=ImageDraw.Draw(img)
ft=font('Cinzel/Cinzel-VariableFont_wght.ttf',64,b'Bold')
fb=font('EB Garamond/EBGaramond-VariableFont_wght.ttf',50)
fi=font('EB Garamond/EBGaramond-Italic-VariableFont_wght.ttf',54)
fa=font('Marcellus SC/MarcellusSC-Regular.ttf',58)
def wrap(txt,f,maxw):
    out=[];line=''
    for w in txt.split():
        t=(line+' '+w).strip()
        if d.textlength(t,font=f)<=maxw: line=t
        else: out.append(line); line=w
    out.append(line); return out
def ctext(y,t,f,fill):
    d.text(((W-d.textlength(t,font=f))/2,y),t,font=f,fill=fill)
paras=[
 ("i","For millions of years, Earth belonged to sensible creatures. Then came the land apes."),
 ("b","Dolphins have no libraries. They have coastlines, and coastlines are where humans do their loudest talking. For several thousand years they have listened to sailors read aloud, harbors gossip, and, lately, radios playing on deck. Now the International Dolphin Historical Society has written the whole thing up."),
 ("b","From the first kept flame to the humanoid robots now being built with hands: Sumer and Egypt, China and India, Greece and Rome, the Silk Roads and the Black Death, the kingdoms of Africa, the Americas before Columbus, empires and revolutions, two world wars, the Cold War, the Moon, medicine, climate, and a present that cannot agree on what is true. Most chapters end with a dolphin verdict."),
 ("b","The jokes are the dolphins\u2019. The history is real. Where the record is thin, the dolphins say so; where it is disputed, they say that too. Notes and sources for every date and number are at the back."),
 ("i","A dry, funny, and unexpectedly fair history of us, told by the neighbors."),
]
y=320
ctext(y,"THE DOLPHINS\u2019 VIEW OF HISTORY",ft,CREAM); y+=110
d.line([(560,y),(1040,y)],fill=GOLD,width=3); y+=80
MAXW=1180
for k,t in paras:
    f=fi if k=='i' else fb
    for l in wrap(t,f,MAXW):
        if k=='i': ctext(y,l,f,GOLD)
        else: d.text(((W-MAXW)/2,y),l,font=f,fill=CREAM)
        y+=int(f.size*1.36)
    y+=44
print('text ends',y)
d.line([(560,2250),(1040,2250)],fill=GOLD,width=3)
ctext(2300,"LOTHAR J. MUSIOL",fa,CREAM)
img.save('KINDLE_BACK_COVER_2560.jpg',quality=92)
