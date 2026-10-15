import os, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(B, "Step_Stories_Pics_Final")
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
W, H = 1600, 2560
NAVY, RUST, INK, CREAM = (31, 58, 95), (168, 75, 42), (60, 52, 40), (246, 238, 222)
def font(n, s):
    p = {"cb": "ComicNeue-Bold.ttf", "c": "ComicNeue-Regular.ttf", "ci": "ComicNeue-Italic.ttf"}.get(n)
    if p: return ImageFont.truetype(os.path.join(FD, p), s)
    return ImageFont.truetype({"gb": r"C:\Windows\Fonts\georgiab.ttf", "g": r"C:\Windows\Fonts\georgia.ttf", "gi": r"C:\Windows\Fonts\georgiai.ttf"}[n], s)
def fit(d, text, name, size, maxw):
    while size > 24:
        f = font(name, size)
        if d.textlength(text, font=f) <= maxw: return f
        size -= 2
    return font(name, 24)
art = Image.open(os.path.join(P, "00_cover_art.jpg")).convert("RGB")
sc = W / art.width
art2 = art.resize((W, round(art.height * sc)), Image.LANCZOS)
top_pad = H - art2.height
strip = art2.crop((0, 0, W, 6)).resize((W, max(top_pad, 1)), Image.BICUBIC).filter(ImageFilter.GaussianBlur(18))
front = Image.new("RGB", (W, H)); front.paste(strip, (0, 0)); front.paste(art2, (0, top_pad))
seam = front.crop((0, top_pad - 40, W, top_pad + 40)).filter(ImageFilter.GaussianBlur(10)); front.paste(seam, (0, top_pad - 40))
front = front.filter(ImageFilter.UnsharpMask(radius=1.4, percent=40, threshold=3)).convert("RGBA")
over = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(over)
od.rounded_rectangle([140, 50, W - 140, 520], radius=56, fill=(246, 238, 222, 208))
od.rounded_rectangle([360, H - 230, W - 360, H - 55], radius=46, fill=(246, 238, 222, 208))
front = Image.alpha_composite(front, over).convert("RGB"); d = ImageDraw.Draw(front)
d.text((W // 2, 72), "The Step Stories \u00b7 Book 3", font=fit(d, "The Step Stories \u00b7 Book 3", "gi", 50, 1100), fill=(90, 80, 60), anchor="ma")
d.text((W // 2, 150), "Scally and the Hill", font=fit(d, "Scally and the Hill", "gb", 150, 1250), fill=NAVY, anchor="ma")
d.text((W // 2, 320), "with the Hanging Socks", font=fit(d, "with the Hanging Socks", "gb", 130, 1250), fill=RUST, anchor="ma")
d.text((W // 2, H - 92), "Anneliese Tauber", font=fit(d, "Anneliese Tauber", "gb", 88, 820), fill=NAVY, anchor="md")
front.save(os.path.join(B, "Cover_Front_1600x2560.jpg"), quality=90)
back = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(back); y = 190
d.text((W // 2, y), "A fantasy adventure with real science", font=font("cb", 76), fill=RUST, anchor="ma"); y += 130
for line in textwrap.wrap("Every night, the hill behind the village goes click. Gucci howls at it. Nobody else can hear it.", 36):
    d.text((W // 2, y), line, font=font("cb", 86), fill=NAVY, anchor="ma"); y += 110
y += 50
for para in ["A new doctor and her quiet son have come to town, a baby is on the way, and the Mayor has a plan to seal the cave and fill it with cheese.",
             "Seven friends follow the clicking up the hill and find hundreds of tiny sleepers hanging like socks on a line. To save them, they must look, count and test, while a blizzard rolls in and Scally tries one trick too many.",
             "Children discover how bats see with sound, how a scan pictures a baby, why ice floats and how thick it must be to hold you, and how to stay safe in the snow."]:
    for line in textwrap.wrap(para, 56):
        d.text((W // 2, y), line, font=font("c", 58), fill=INK, anchor="ma"); y += 80
    y += 46
y += 20; d.line([(300, y), (W - 300, y)], fill=RUST, width=5); y += 60
for line in ["Ice, snow and medicine safety woven in,", "plus a guide for parents and teachers."]:
    d.text((W // 2, y), line, font=font("cb", 66), fill=NAVY, anchor="ma"); y += 88
y += 30
for line in ["Ages 7 to 10", "Book 3 of The Step Stories"]:
    d.text((W // 2, y), line, font=font("c", 62), fill=INK, anchor="ma"); y += 84
d.text((W // 2, H - 100), "Anneliese Tauber", font=font("gb", 84), fill=NAVY, anchor="md")
back.save(os.path.join(B, "Cover_Back_1600x2560.jpg"), quality=92)
print("covers saved; text ended at y =", y, "of", H)
