import os, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(B, "Step_Stories_Pics_Final")
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
W, H = 1600, 2560
NAVY, RUST, INK = (31, 58, 95), (168, 75, 42), (60, 52, 40)
CREAM = (246, 238, 222)


def font(name, size):
    path = {"cb": FD + r"\ComicNeue-Bold.ttf", "c": FD + r"\ComicNeue-Regular.ttf", "ci": FD + r"\ComicNeue-Italic.ttf",
            "gb": r"C:\Windows\Fonts\georgiab.ttf", "g": r"C:\Windows\Fonts\georgia.ttf", "gi": r"C:\Windows\Fonts\georgiai.ttf"}[name]
    return ImageFont.truetype(path, size)


def fit(d, text, name, size, maxw):
    while size > 24:
        f = font(name, size)
        if d.textlength(text, font=f) <= maxw:
            return f
        size -= 2
    return font(name, 24)


# ---------------- front cover 1600x2560 (action art, 2:3) ----------------
art = Image.open(os.path.join(P, "00_cover_art.jpg")).convert("RGB")
sc = W / art.width
art2 = art.resize((W, round(art.height * sc)), Image.LANCZOS)           # 1600 x 2400
top_pad = H - art2.height                                                # 160 px of extra sky on top
strip = art2.crop((0, 0, W, 6)).resize((W, top_pad), Image.BICUBIC).filter(ImageFilter.GaussianBlur(18))
front = Image.new("RGB", (W, H))
front.paste(strip, (0, 0)); front.paste(art2, (0, top_pad))
# soften the seam
seam = front.crop((0, top_pad - 40, W, top_pad + 40)).filter(ImageFilter.GaussianBlur(10))
front.paste(seam, (0, top_pad - 40))
front = front.filter(ImageFilter.UnsharpMask(radius=1.4, percent=40, threshold=3)).convert("RGBA")
over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(over)
od.rounded_rectangle([140, 50, W - 140, 460], radius=56, fill=(246, 238, 222, 208))
od.rounded_rectangle([360, H - 230, W - 360, H - 55], radius=46, fill=(246, 238, 222, 208))
front = Image.alpha_composite(front, over).convert("RGB")
d = ImageDraw.Draw(front)
d.text((W // 2, 74), "The Step Stories", font=fit(d, "The Step Stories", "gi", 50, 1100), fill=(90, 80, 60), anchor="ma")
d.text((W // 2, 150), "The Wee Scallywag", font=fit(d, "The Wee Scallywag", "gb", 142, 1250), fill=NAVY, anchor="ma")
d.text((W // 2, 305), "and the Gentle Elf", font=fit(d, "and the Gentle Elf", "gb", 126, 1250), fill=RUST, anchor="ma")
d.text((W // 2, H - 92), "Anneliese Tauber", font=fit(d, "Anneliese Tauber", "gb", 88, 820), fill=NAVY, anchor="md")
front.save(os.path.join(B, "Cover_Front_1600x2560.jpg"), quality=90)

# ---------------- back cover: text only on a single colour ----------------
back = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(back)
y = 190
d.text((W // 2, y), "A fantasy adventure with real science", font=font("cb", 76), fill=RUST, anchor="ma")
y += 130
head = "The wheel has stopped. The village has no flour. And the cheekiest boy in the valley has just stolen Hal\u2019s boots."
for line in textwrap.wrap(head, 36):
    d.text((W // 2, y), line, font=font("cb", 88), fill=NAVY, anchor="ma")
    y += 112
y += 50
body = [
    "Three days. One small bargain. One true name to guess.",
    "A gentle elf who only says what is true. A mill ghost in a flour-sack cloak. A toad that charges tolls. A wolf pup who howls at the moon. A fire that goes wrong in the night, and a stranger with sweets and a \u201cquicker way\u201d.",
    "Children see how levers work, why a fish is deeper than it looks, how genes are like a recipe, why the moon changes shape and the tides rise, and why scientists say \u201cI do not know\u201d. Every fact is true, and every bit of magic is marked.",
]
for para in body:
    for line in textwrap.wrap(para, 58):
        d.text((W // 2, y), line, font=font("c", 58), fill=INK, anchor="ma")
        y += 80
    y += 46
y += 20
d.line([(300, y), (W - 300, y)], fill=RUST, width=5)
y += 60
for line in ["51 painted pictures tell the whole story,", "so even non-readers from age 5 can follow it."]:
    d.text((W // 2, y), line, font=font("cb", 66), fill=NAVY, anchor="ma")
    y += 88
y += 30
for line in ["Experiments to try at home", "A guide for parents and teachers", "Ages 5 to 9"]:
    d.text((W // 2, y), line, font=font("c", 62), fill=INK, anchor="ma")
    y += 84
d.text((W // 2, H - 200), "Anneliese Tauber", font=font("gb", 84), fill=NAVY, anchor="ma")
d.text((W // 2, H - 100), "The Step Stories \u00b7 Book 1", font=font("gi", 54), fill=(90, 80, 60), anchor="ma")
back.save(os.path.join(B, "Cover_Back_1600x2560.jpg"), quality=92)
print("covers saved; text ended at y =", y, "of", H)
