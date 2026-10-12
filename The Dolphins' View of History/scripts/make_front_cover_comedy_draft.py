import numpy as np, math
from PIL import Image, ImageDraw, ImageFont
from dolphin import outline
import os

# Draft only: a bolder "comedy object" direction to compare against the live
# cover (KINDLE_COVER_FINAL_2560.jpg / scripts/make_front_cover.py). Writes a
# separate file and must not touch the live cover or its script.

W, H = 1600, 2560
G = os.environ.get('GOOGLE_FONTS', '/usr/share/fonts/truetype/sand-box/google/')

def font(path, size, var=None):
    f = ImageFont.truetype(G + path, size)
    if var:
        names = [n.decode() if isinstance(n, bytes) else n for n in f.get_variation_names()]
        f.set_variation_by_name(var.encode() if var in names else names[min(len(names) - 1, 2)].encode())
    return f

# Flat, saturated palette instead of the live cover's muted cream/navy/gold
CORAL = (224, 86, 60)
NAVY = (24, 42, 64)
MUSTARD = (232, 170, 40)
CREAM = (250, 244, 232)

img = Image.new('RGB', (W, H), CREAM)
d = ImageDraw.Draw(img)

def ctext(y, txt, f, fill, track=0, stroke=0, stroke_fill=None):
    if track:
        ws = [d.textlength(c, font=f) for c in txt]
        tw = sum(ws) + track * (len(txt) - 1)
        x = (W - tw) / 2
        for c, w in zip(txt, ws):
            d.text((x, y), c, font=f, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
            x += w + track
    else:
        tw = d.textlength(txt, font=f)
        d.text(((W - tw) / 2, y), txt, font=f, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)

# --- flat color block behind the title, instead of a horizon gradient
d.rectangle([0, 0, W, 980], fill=MUSTARD)

fb = font('Baloo2/Baloo2-VariableFont_wght.ttf', 190, 'Bold')
fm = font('Baloo2/Baloo2-VariableFont_wght.ttf', 100, 'Bold')
ctext(120, 'THE DOLPHINS’', fm, NAVY, track=2)
# was cream-on-mustard, the weakest-contrast line on the page at thumbnail size; now navy like the line above it
ctext(250, 'VIEW OF', fm, NAVY, track=6)
# coral with a navy stroke so HISTORY still reads at grayscale/thumbnail size, not just in full color
ctext(430, 'HISTORY', fb, CORAL, track=2, stroke=4, stroke_fill=NAVY)

fi = font('Nunito/Nunito-Italic-VariableFont_wght.ttf', 56, 'SemiBold')
ctext(760, 'Fifty Million Years of', fi, NAVY)
ctext(830, 'Watching You Mess This Up', fi, NAVY)

# --- dolphin, flat navy, same pose as the live cover, bigger and closer to camera
o = outline(); S = 4
L = 920; ang = math.radians(32)
c, s_ = math.cos(ang), math.sin(ang)
cx, cy = 800, 1620
pts = []
for x, y in o:
    X = (x - 0.5) * L; Y = y * L
    pts.append(((cx + X * c - Y * s_) * S, (cy - (X * s_ + Y * c)) * S))
lay = Image.new('L', (W * S, H * S), 0)
ImageDraw.Draw(lay).polygon(pts, fill=255)
lay = lay.resize((W, H), Image.LANCZOS)
img.paste(Image.new('RGB', (W, H), NAVY), (0, 0), lay)
d = ImageDraw.Draw(img)

# --- reading glasses on the dolphin, the visible joke at thumbnail size
ex, ey = 0.845, 0.035
X = (ex - 0.5) * L; Y = ey * L
gx, gy = cx + X * c - Y * s_, cy - (X * s_ + Y * c)
# lens centers set back along the body axis (local -x), offset slightly for a jaunty tilt
d1 = (-0.085 * L, 0.0); d2 = (-0.177 * L, 0.012 * L)
def rot(vx, vy):
    return (gx + vx * c - vy * s_, gy - (vx * s_ + vy * c))
l1 = rot(*d1); l2 = rot(*d2)
r = 47  # was 34 - too small to read as glasses at Amazon thumbnail size; scaled up ~38%
for lx, ly in (l1, l2):
    d.ellipse([lx - r, ly - r, lx + r, ly + r], outline=CREAM, width=13)
d.line([l1[0] - r, l1[1], l2[0] + r, l2[1]], fill=CREAM, width=10)

# --- author block
fa = font('Baloo2/Baloo2-VariableFont_wght.ttf', 92, 'Bold')
fn = font('Nunito/Nunito-Italic-VariableFont_wght.ttf', 46, 'Regular')
ctext(2160, 'As told by Professor Click-Click-Whoosh', fn, (90, 90, 90))
d.line([(560, 2240), (1040, 2240)], fill=CORAL, width=4)
ctext(2290, 'LOTHAR J. MUSIOL', fa, NAVY, track=4)

img.convert('RGB').save('KINDLE_COVER_COMEDY_DRAFT_2560.jpg', quality=92)
print('wrote KINDLE_COVER_COMEDY_DRAFT_2560.jpg')
