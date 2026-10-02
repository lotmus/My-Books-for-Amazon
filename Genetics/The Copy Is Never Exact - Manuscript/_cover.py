"""Composite the front cover: crop the text-free artwork to 6x9 and set the type."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\Users\lomus\.cursor\projects\c-Users-lomus-OneDrive-My-Books-for-Amazon-Science-Books-Genetics-The-Copy-Is-Never-Exact-Manuscript\assets\cover_bg.jpg"
OUT_DIR = os.path.join(ROOT, "cover")
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, "front_cover.png")

W, H = 1800, 2700
im = Image.open(SRC).convert("RGB")
sw, sh = im.size
# 6:9 is wider than 9:16, so crop height and keep the helix.
target_h = int(sw * H / W)
if target_h < sh:
    # Keep a little more room above the helix than below.
    top = max(0, int((sh - target_h) * 0.42))
    im = im.crop((0, top, sw, top + target_h))
im = im.resize((W, H), Image.Resampling.LANCZOS)

draw = ImageDraw.Draw(im)
font_dir = r"C:\Windows\Fonts"
title_font = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 92)
sub_font = ImageFont.truetype(os.path.join(font_dir, "georgia.ttf"), 36)
author_font = ImageFont.truetype(os.path.join(font_dir, "georgiai.ttf"), 44)

cream = (245, 236, 220)
sub_color = (214, 204, 184)
gold = (226, 190, 120)

def center(text, font, y, fill):
    box = draw.textbbox((0, 0), text, font=font)
    tw = box[2] - box[0]
    x = (W - tw) / 2
    draw.text((x, y), text, font=font, fill=fill)

center("The Copy Is Never Exact", title_font, 168, cream)
center("DNA, Inheritance, and the", sub_font, 300, sub_color)
center("Coming Edit of Ourselves", sub_font, 352, sub_color)
center("Lothar J. Musiol", author_font, 2460, gold)

im.save(OUT, "PNG", optimize=True)
print(OUT, im.size, os.path.getsize(OUT))
