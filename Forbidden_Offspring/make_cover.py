"""Typographic front cover for Forbidden Offspring (1600 x 2560, KDP ratio 1:1.6).
Run from the repo root:  python Forbidden_Offspring/make_cover.py
A sound-wave helix (one strand cyan, one amber) over faint listening rings; title, tagline and byline in Georgia.
Output: Forbidden_Offspring/Forbidden_Offspring_cover_v1.jpg
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, S = 1600, 2560, 2            # final size, supersample factor
OUT = 'Forbidden_Offspring/Forbidden_Offspring_cover_v1.jpg'
F = 'C:/Windows/Fonts/'
def font(name, size): return ImageFont.truetype(F + name, size * S)

img = Image.new('RGB', (W * S, H * S))
px = ImageDraw.Draw(img)
top, bot = (13, 22, 52), (4, 6, 14)
for y in range(H * S):
    t = y / (H * S)
    px.line([(0, y), (W * S, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))

# listening rings, centered on the helix
layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
ld = ImageDraw.Draw(layer)
cx, cy = W * S // 2, 1330 * S
for k in range(1, 15):
    r = k * 120 * S
    a = max(8, int(70 - k * 4.4))
    ld.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(95, 208, 232, a), width=2 * S)
img = Image.alpha_composite(img.convert('RGBA'), layer)

# helix drawn as a waveform: amplitude swells in the middle
layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
ld = ImageDraw.Draw(layer)
x0, x1 = 110 * S, (W - 110) * S
n = 900
def amp(t): return 250 * S * (math.sin(math.pi * t) ** 0.8) + 14 * S
def pt(t, ph):
    x = x0 + (x1 - x0) * t
    return x, cy + amp(t) * math.sin(t * 15.0 * math.pi + ph)
# rungs
for i in range(0, 61):
    t = (i + 0.5) / 61
    (xa, ya), (xb, yb) = pt(t, 0), pt(t, math.pi)
    ld.line([(xa, ya), (xb, yb)], fill=(220, 230, 245, int(110 * math.sin(math.pi * t) + 20)), width=2 * S)
# strands (draw back/front by sign of cosine so they appear to cross)
for ph, col in ((math.pi, (242, 181, 90)), (0, (95, 208, 232))):
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        depth = math.cos(((t0 + t1) / 2) * 15.0 * math.pi + ph)
        w = int((5 + 4 * (depth + 1) / 2) * S)
        a = int(150 + 105 * (depth + 1) / 2)
        ld.line([pt(t0, ph), pt(t1, ph)], fill=col + (a,), width=w)
glow = layer.filter(ImageFilter.GaussianBlur(14 * S))
img = Image.alpha_composite(img, glow)
img = Image.alpha_composite(img, layer)

d = ImageDraw.Draw(img)
def centered(text, y, fnt, fill, spacing=0):
    widths = [d.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + spacing * S * (len(text) - 1)
    x = (W * S - total) / 2
    for ch, w in zip(text, widths):
        d.text((x, y * S), ch, font=fnt, fill=fill)
        x += w + spacing * S

centered('FORBIDDEN', 300, font('georgiab.ttf', 168), (244, 247, 252), 14)
centered('OFFSPRING', 500, font('georgiab.ttf', 168), (244, 247, 252), 14)
d.line([(560 * S, 760 * S), (1040 * S, 760 * S)], fill=(242, 181, 90, 255), width=3 * S)
centered('A NOVEL', 790, font('georgia.ttf', 52), (242, 181, 90), 18)

tag = font('georgiai.ttf', 58)
centered('Four minutes. Fifty-eight children.', 1840, tag, (214, 224, 238), 0)
centered('One of them is listening.', 1930, tag, (214, 224, 238), 0)

centered('Lothar J. Musiol writing as', 2230, font('georgiai.ttf', 46), (160, 176, 202), 0)
centered('GENEVIEVE CRISP', 2300, font('georgiab.ttf', 104), (244, 247, 252), 10)

img = img.convert('RGB').resize((W, H), Image.LANCZOS)
img.save(OUT, quality=92, optimize=True)
print(OUT, img.size)
