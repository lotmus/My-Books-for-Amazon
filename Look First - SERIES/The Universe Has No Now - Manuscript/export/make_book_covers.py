"""Book 1 / Book 2 front covers derived from cover_typographic_v2_clockring.jpg (split 10 Oct 2026).
Usage: python make_book_covers.py   (writes next to this script; the original cover is not changed)"""
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'cover_typographic_v2_clockring.jpg')
GOLD, CREAM, GREY = (214, 160, 72), (238, 232, 220), (170, 170, 170)
def font(names, size):
    for n in names:
        try: return ImageFont.truetype(os.path.join(r'C:\Windows\Fonts', n), size)
        except OSError: pass
    return ImageFont.load_default()
def centre(d, y, s, f, fill):
    w = d.textlength(s, font=f); d.text(((1600 - w) / 2, y), s, font=f, fill=fill)
for n, sub in ((1, 'No Now, No Centre'), (2, 'Getting There Anyway')):
    im = Image.open(SRC).convert('RGB'); d = ImageDraw.Draw(im)
    bg = im.getpixel((800, 1900))
    d.rectangle([260, 2215, 1340, 2300], fill=bg)
    centre(d, 1700, 'BOOK %d' % n, font(['arialbd.ttf'], 74), GOLD)
    centre(d, 1800, sub, font(['arial.ttf'], 92), CREAM)
    centre(d, 2228, 'Look First \u00b7 Volume 1 \u00b7 Book %d' % n, font(['arial.ttf'], 42), GREY)
    out = os.path.join(HERE, 'cover_typographic_v2_clockring - Book %d.jpg' % n); im.save(out, quality=92); print('wrote', out)