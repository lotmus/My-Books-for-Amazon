from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import importlib.util

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / 'cover_concept_v2'
OUT.mkdir(exist_ok=True)
BG = OUT / 'cover_background_day_v2.png'
W, H = 1600, 2560
CREAM = (243, 232, 208)
GOLD = (224, 172, 82)
SHADOW = (8, 12, 26, 190)
FONT = Path(r'C:\Windows\Fonts\georgiab.ttf')
FONT_REG = Path(r'C:\Windows\Fonts\georgia.ttf')
FONT_ITALIC = Path(r'C:\Windows\Fonts\georgiai.ttf')

def fit_font(text, max_width, start_size, path=FONT):
    size = start_size
    while size > 20:
        f = ImageFont.truetype(str(path), size)
        if ImageDraw.Draw(Image.new('RGB',(1,1))).textbbox((0,0), text, font=f)[2] <= max_width:
            return f
        size -= 2
    return ImageFont.truetype(str(path), size)

def center_text(draw, text, y, font, fill, stroke=0):
    box = draw.textbbox((0,0), text, font=font, stroke_width=stroke)
    x = (W - (box[2]-box[0])) // 2
    draw.text((x+3,y+5), text, font=font, fill=SHADOW, stroke_width=stroke+1, stroke_fill=SHADOW)
    draw.text((x,y), text, font=font, fill=fill, stroke_width=stroke, stroke_fill=(22,20,29,230))

def create_front():
    im=Image.open(BG).convert('RGB')
    target_ratio=5/8
    w,h=im.size
    crop_w=int(h*target_ratio)
    left=(w-crop_w)//2
    im=im.crop((left,0,left+crop_w,h)).resize((W,H),Image.Resampling.LANCZOS).convert('RGBA')
    # Gentle darkening at the top and bottom protects type while leaving the scene luminous.
    shade=Image.new('RGBA',(W,H),(0,0,0,0)); px=shade.load()
    for y in range(H):
        a=int(46*max(0,1-y/1000)**1.5 + 115*max(0,(y-2250)/310))
        if a:
            for x in range(W): px[x,y]=(4,8,20,a)
    im=Image.alpha_composite(im,shade)
    d=ImageDraw.Draw(im)
    # Brand rule and monogram echo Book 1's gold detailing.
    brand='THE RELATIVISTIC INVESTIGATION BUREAU  •  BOOK 2'
    bf=fit_font(brand,1460,39)
    center_text(d,brand,37,bf,GOLD,0)
    d.line((145,112,702,112),fill=GOLD,width=3); d.line((898,112,1455,112),fill=GOLD,width=3)
    d.ellipse((748,82,852,142),outline=GOLD,width=3)
    center_text(d,'RIB',89,ImageFont.truetype(str(FONT),35),GOLD,0)
    center_text(d,'The warning came before it was written.',153,fit_font('The warning came before it was written.',1400,47,FONT_ITALIC),CREAM,0)
    # Large, exact title lettering, kept entirely in the open wall area.
    center_text(d,'THE WARNING',244,fit_font('THE WARNING',1460,151),CREAM,2)
    center_text(d,'THAT WAS',411,fit_font('THAT WAS',1360,142),CREAM,2)
    center_text(d,'SENT TOO LATE',570,fit_font('SENT TOO LATE',1480,136),GOLD,2)
    # Byline follows Book 1's two-line hierarchy.
    center_text(d,'Lothar J. Musiol',2432,ImageFont.truetype(str(FONT),68),CREAM,1)
    center_text(d,'writing as Spezala Genara Relavi (S.G.R.)',2502,fit_font('writing as Spezala Genara Relavi (S.G.R.)',1480,48,FONT_ITALIC),GOLD,0)
    out=OUT/'Kindle Front Cover - Concept v2.jpg'
    im.convert('RGB').save(out,quality=94,subsampling=0)
    print(out)

def create_back():
    # Reuse the established back-cover copy and hierarchy, changing only its flat fill
    # to a restrained series-matched navy/indigo ground with a soft amber light bloom.
    src=HERE/'scripts'/'make_covers.py'
    spec=importlib.util.spec_from_file_location('original_cover_generator',src)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    m.OUT=str(OUT)
    m.TITLE=str(FONT); m.CINZEL=str(FONT); m.LB=str(FONT_REG); m.EB=str(FONT_REG); m.EBI=str(FONT_ITALIC)
    base_font=m.F
    def compact_font(path,size,wght=None):
        size={46:38,44:40,42:35,38:33}.get(size,size)
        return base_font(path,size,wght)
    m.F=compact_font
    original_new=Image.new
    def themed_new(mode,size,color=0,*args,**kwargs):
        if mode=='RGB' and size==(m.W,m.H) and color==(14,22,44):
            small=original_new('RGB',(400,640),(0,0,0)); p=small.load()
            for y in range(640):
                t=y/639
                if t<.55:
                    k=t/.55; c=tuple(round(a+(b-a)*k) for a,b in zip((12,22,48),(25,31,58)))
                else:
                    k=(t-.55)/.45; c=tuple(round(a+(b-a)*k) for a,b in zip((25,31,58),(48,30,38)))
                for x in range(400): p[x,y]=c
            small=small.resize(size,Image.Resampling.LANCZOS).convert('RGBA')
            bloom=original_new('RGBA',size,(0,0,0,0)); bd=ImageDraw.Draw(bloom)
            bd.ellipse((1800,700,3700,2800),fill=(192,111,56,34))
            bd.ellipse((-1300,2500,950,5000),fill=(43,75,135,37))
            bloom=bloom.filter(ImageFilter.GaussianBlur(360))
            return Image.alpha_composite(small,bloom).convert('RGB')
        return original_new(mode,size,color,*args,**kwargs)
    Image.new=themed_new
    try: m.back()
    finally: Image.new=original_new
    generated=OUT/'Kindle Back Cover.jpg'
    final=OUT/'Kindle Back Cover - Concept v2.jpg'
    generated.replace(final)
    print(final)

if __name__=='__main__':
    import shutil
    create_front(); create_back()
    shutil.copy2(OUT/'Kindle Front Cover - Concept v2.jpg', HERE/'Kindle Front Cover.jpg')
    shutil.copy2(OUT/'Kindle Back Cover - Concept v2.jpg', HERE/'Kindle Back Cover.jpg')



