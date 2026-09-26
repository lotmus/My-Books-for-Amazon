"""Typographic KDP cover for The Universe Has No Now.

Concept: the book's own picture. A light cone (which also reads as an hourglass)
with two different "nows" tilted through the same event. Ochre marks the now.
No NASA, no photo sky. Drawn at 2x and downsampled so every edge is smooth.

Final size 1600x2560 (1:1.6), RGB JPEG. Title must read at a 160x256 tile.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "export", "cover_typographic.jpg")
W, H = 1600, 2560
S = 2                                    # supersample factor
CW, CH = W * S, H * S

BG_EDGE = (9, 9, 12)
BG_MID = (24, 24, 33)
CREAM = (240, 234, 220)
MUTE = (170, 165, 154)
OCHRE = (222, 160, 78)
DIM = (128, 124, 114)


def font(name, size, variation=None):
    f = ImageFont.truetype(f"C:/Windows/Fonts/{name}", size * S)
    if variation:
        try:
            f.set_variation_by_name(variation)
        except Exception:
            pass
    return f


def text_w(f, s, tracking):
    return sum(f.getlength(ch) for ch in s) + tracking * S * (len(s) - 1)


def draw_tracked(d, cx, y, s, f, fill, tracking=0):
    """Centered, letter-spaced text. y is the vertical middle."""
    x = cx * S - text_w(f, s, tracking) / 2
    for ch in s:
        d.text((x, y * S), ch, font=f, fill=fill, anchor="lm")
        x += f.getlength(ch) + tracking * S


def draw_line_runs(d, cx, y, runs, f, tracking):
    """One centered line made of (text, colour) runs separated by a word gap."""
    gap = f.getlength(" ") + tracking * S
    total = sum(text_w(f, t, tracking) for t, _ in runs) + gap * (len(runs) - 1)
    x = cx * S - total / 2
    for t, col in runs:
        for ch in t:
            d.text((x, y * S), ch, font=f, fill=col, anchor="lm")
            x += f.getlength(ch) + tracking * S
        x += gap - tracking * S


# ---------- background: soft glow behind the event, near-black at the edges
CX, CY = W // 2, 1400                    # the event, in final pixels
bg = Image.new("RGB", (CW, CH), BG_EDGE)
glow = Image.new("L", (CW, CH), 0)
gd = ImageDraw.Draw(glow)
R0 = 1400 * S
for r in range(R0, 0, -10 * S):
    v = int(255 * (1 - r / R0) ** 2.2)
    gd.ellipse([CX * S - r, CY * S - r, CX * S + r, CY * S + r], fill=v)
glow = glow.filter(ImageFilter.GaussianBlur(40 * S))
bg = Image.composite(Image.new("RGB", (CW, CH), BG_MID), bg, glow)

# ---------- the light cone / hourglass
HALF = 590                               # arm length in x and y (45 degree arms)
layer = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
ld = ImageDraw.Draw(layer)

# faint filled cones: brighter at the event, fading outward
for k in range(0, HALF * S):
    t = k / (HALF * S)
    a = int(52 * (1 - t) ** 1.6 + 5)
    for sign in (-1, 1):
        y = CY * S + sign * k
        ld.line([(CX * S - k, y), (CX * S + k, y)], fill=(255, 245, 225, a), width=1)

# the cone edges, fading toward their ends
segs = 240
for sx, sy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
    for i in range(segs):
        t0, t1 = i / segs, (i + 1) / segs
        a = int(235 * (1 - t0) ** 0.9 + 20)
        p0 = (CX * S + sx * t0 * HALF * S, CY * S + sy * t0 * HALF * S)
        p1 = (CX * S + sx * t1 * HALF * S, CY * S + sy * t1 * HALF * S)
        ld.line([p0, p1], fill=(*CREAM, a), width=5 * S)

# the two nows. Both pass through the event and both lie outside the cones.
reach = 680 * S
ld.line([(CX * S - reach, CY * S), (CX * S + reach, CY * S)], fill=(*DIM, 215), width=4 * S)
ang = math.radians(-13)
dx, dy = math.cos(ang) * reach, math.sin(ang) * reach
ld.line([(CX * S - dx, CY * S - dy), (CX * S + dx, CY * S + dy)], fill=(*OCHRE, 255), width=8 * S)

# the event: a dot with a soft halo
halo = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
hd = ImageDraw.Draw(halo)
for r, a in ((70, 40), (46, 70), (30, 120)):
    hd.ellipse([CX * S - r * S, CY * S - r * S, CX * S + r * S, CY * S + r * S], fill=(*OCHRE, a))
halo = halo.filter(ImageFilter.GaussianBlur(14 * S))
layer = Image.alpha_composite(layer, halo)
ld = ImageDraw.Draw(layer)
ld.ellipse([CX * S - 20 * S, CY * S - 20 * S, CX * S + 20 * S, CY * S + 20 * S], fill=(255, 226, 170, 255))
ld.ellipse([CX * S - 12 * S, CY * S - 12 * S, CX * S + 12 * S, CY * S + 12 * S], fill=(255, 250, 235, 255))

im = Image.alpha_composite(bg.convert("RGBA"), layer)
d = ImageDraw.Draw(im)

# ---------- title (top): two lines, NOW in ochre, auto-fit within a safe margin
TR = 10
MARGIN = 110                              # final-px side margin the title must respect
max_w = (W - 2 * MARGIN) * S
size = 250
while True:
    tf = font("bahnschrift.ttf", size, "Bold")
    w1 = text_w(tf, "THE UNIVERSE", TR)
    w2 = text_w(tf, "HAS NO", TR) + tf.getlength(" ") + TR * S + text_w(tf, "NOW", TR)
    if max(w1, w2) <= max_w or size <= 60:
        break
    size -= 2
draw_tracked(d, W / 2, 330, "THE UNIVERSE", tf, CREAM, TR)
draw_line_runs(d, W / 2, 590, [("HAS NO", CREAM), ("NOW", OCHRE)], tf, TR)

# ---------- subtitle, author, series (bottom)
sf = font("segoeui.ttf", 58)
draw_tracked(d, W / 2, 2150, "Time, Origins, and Whether", sf, MUTE, 3)
draw_tracked(d, W / 2, 2226, "We Can Get Somewhere Else", sf, MUTE, 3)

d.line([(W // 2 * S - 90 * S, 2296 * S), (W // 2 * S + 90 * S, 2296 * S)], fill=(*DIM, 255), width=3 * S)

af = font("bahnschrift.ttf", 104, "SemiBold")
draw_tracked(d, W / 2, 2380, "LOTHAR J. MUSIOL", af, CREAM, 14)

vf = font("segoeui.ttf", 40)
draw_tracked(d, W / 2, 2470, "LOOK FIRST  \u00b7  VOLUME 1", vf, DIM, 8)

out = im.convert("RGB").resize((W, H), Image.LANCZOS)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
out.save(OUT, "JPEG", quality=94, subsampling=0)
print("wrote", os.path.abspath(OUT), out.size, os.path.getsize(OUT))
