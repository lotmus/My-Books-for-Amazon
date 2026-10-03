"""One-off fix on 'book1 back cover.png' (992 x 1586): the series line
'Book 1 of 21 in the' becomes 'Book 1 of 7 in the'. Only that text line is
repainted; the rest of the image is untouched. Original kept in
D:\\bak\\2026-10-02 EE covers\\.
Usage: python patch_book1_back_count.py "book1 back cover.png"
"""
import sys
from PIL import Image, ImageDraw, ImageFont

FONT = r'C:\Windows\Fonts\segoeui.ttf'
COLOR = (126, 152, 185)          # measured from the line below it
BOX = (368, 1232, 610, 1263)     # old text 'Book 1 of 21 in the' sits at x 381-595, y 1238-1256
REF_WIDTH = 316                  # 'Electrical Engineering Series' on the line below, x 333-648
CX, TOP = 490.5, 1238

path = sys.argv[1]
im = Image.open(path).convert('RGB')
px = im.load()
x0, y0, x1, y1 = BOX
for y in range(y0, y1):          # fill by interpolating the background at both sides of the box
    l, r = px[x0 - 1, y], px[x1, y]
    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        px[x, y] = tuple(int(l[i] + (r[i] - l[i]) * t) for i in range(3))
best = None
for s in range(10, 60):
    f = ImageFont.truetype(FONT, s)
    w = f.getlength('Electrical Engineering Series')
    if best is None or abs(w - REF_WIDTH) < best[0]:
        best = (abs(w - REF_WIDTH), s)
f = ImageFont.truetype(FONT, best[1])
d = ImageDraw.Draw(im)
text = 'Book 1 of 7 in the'
bb = d.textbbox((0, 0), text, font=f)
d.text((CX - (bb[2] - bb[0]) / 2 - bb[0], TOP - bb[1]), text, font=f, fill=COLOR)
im.save(path)
print('patched', path, 'font size', best[1])
