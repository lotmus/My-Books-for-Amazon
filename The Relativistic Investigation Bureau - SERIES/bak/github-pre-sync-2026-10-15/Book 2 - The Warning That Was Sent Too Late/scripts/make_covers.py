"""Kindle covers for The Warning That Was Sent Too Late (RIB Book 2), in Book 1's trade dress:
night-blue sky with a dusk-orange horizon, cream and gold slab-serif title, gold rules and RIB monogram,
byline 'Lothar J. Musiol / writing as Spezala Genara Relavi (S.G.R.)'.
Everything is drawn by this script (no photographs, no real people, no third-party art).
Fonts: Google Fonts (SIL Open Font License): Coustard, Cinzel, Libre Baskerville, EB Garamond.
Usage: python make_covers.py OUTDIR  ->  Kindle Front Cover.jpg (1600x2560), Kindle Back Cover.jpg (1600x2560)"""
import sys, os, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
G = os.environ.get('FONT_DIR', '/usr/share/fonts/truetype/sand-box/google/').rstrip('/\\') + '/'  # folder holding the Google Fonts subfolders
TITLE = G + 'Coustard/Coustard-Black.ttf'
CINZEL = G + 'Cinzel/Cinzel-VariableFont_wght.ttf'
LB = G + 'Libre Baskerville/LibreBaskerville-VariableFont_wght.ttf'
EB = G + 'EB Garamond/EBGaramond-VariableFont_wght.ttf'
EBI = G + 'EB Garamond/EBGaramond-Italic-VariableFont_wght.ttf'
S = 2
W, H = 1600 * S, 2560 * S
CREAM = (243, 232, 208); GOLD = (224, 172, 82); AMBER = (255, 168, 38)

def F(path, size, wght=None):
    f = ImageFont.truetype(path, int(size * S))
    if wght:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f

def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def gradient(im, stops):
    d = ImageDraw.Draw(im)
    for y in range(im.size[1]):
        yy = y / S
        for (y0, c0), (y1, c1) in zip(stops, stops[1:]):
            if y0 <= yy <= y1:
                d.line([(0, y), (im.size[0], y)], fill=lerp(c0, c1, (yy - y0) / (y1 - y0))); break

def spaced(d, xy, text, font, fill, track=0, anchor_center=True):
    widths = [d.textlength(ch, font=font) for ch in text]
    total = sum(widths) + track * S * (len(text) - 1)
    x, y = xy
    if anchor_center: x -= total / 2
    for ch, w in zip(text, widths):
        d.text((x, y), ch, font=font, fill=fill); x += w + track * S
    return total

def glow(base, shape_fn, radius, alpha=255):
    layer = Image.new('RGBA', base.size, (0, 0, 0, 0))
    shape_fn(ImageDraw.Draw(layer))
    layer = layer.filter(ImageFilter.GaussianBlur(radius * S))
    if alpha < 255:
        a = layer.split()[3].point(lambda v: v * alpha // 255); layer.putalpha(a)
    base.alpha_composite(layer)

def P(*pts): return [(x * S, y * S) for x, y in pts]

# 5x7 dot-matrix glyphs for the destination board
DOTS = {
 'Y': ["10001","10001","01010","00100","00100","00100","00100"],
 'E': ["11111","10000","10000","11110","10000","10000","11111"],
 'S': ["01111","10000","10000","01110","00001","00001","11110"],
 'T': ["11111","00100","00100","00100","00100","00100","00100"],
 'R': ["11110","10001","10001","11110","10100","10010","10001"],
 'D': ["11100","10010","10001","10001","10001","10010","11100"],
 'A': ["01110","10001","10001","11111","10001","10001","10001"],
}

def front():
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    gradient(im, [(0, (7, 12, 30)), (650, (20, 32, 66)), (980, (58, 56, 92)), (1150, (168, 88, 62)), (1260, (226, 128, 56))])
    d = ImageDraw.Draw(im)
    rnd = random.Random(1047)
    for _ in range(170):
        x, y = rnd.uniform(0, 1600), rnd.uniform(0, 900); r = rnd.choice([1, 1, 1.5, 2])
        c = lerp((150, 160, 200), CREAM, rnd.random())
        d.ellipse(P((x - r, y - r), (x + r, y + r)), fill=c)
    # generic London rooftops (no specific building)
    sil = (13, 15, 27)
    base = 1262
    x = 0
    while x < 1600:
        w = rnd.randint(60, 150); h = rnd.randint(40, 150)
        d.rectangle(P((x, base - h), (x + w, base + 5)), fill=sil)
        if rnd.random() < 0.6:
            for k in range(rnd.randint(1, 3)):
                cx = x + rnd.randint(8, max(10, w - 20))
                d.rectangle(P((cx, base - h - 26), (cx + 14, base - h)), fill=sil)
                d.rectangle(P((cx - 2, base - h - 30), (cx + 16, base - h - 25)), fill=sil)
        for k in range(rnd.randint(0, 3)):
            wx = x + rnd.randint(6, max(8, w - 14)); wy = base - rnd.randint(14, max(16, h - 10))
            d.rectangle(P((wx, wy), (wx + 7, wy + 10)), fill=(250, 196, 110))
        x += w
    # a dome on the left and a clock tower on the right, both generic
    d.pieslice(P((150, 1060), (330, 1240)), 180, 360, fill=sil)
    d.rectangle(P((150, 1148), (330, 1262)), fill=sil)
    d.rectangle(P((234, 1028), (246, 1062)), fill=sil)
    d.rectangle(P((1300, 1010), (1372, 1262)), fill=sil)
    d.polygon(P((1292, 1012), (1380, 1012), (1336, 935)), fill=sil)
    d.ellipse(P((1316, 1040), (1356, 1080)), fill=(250, 214, 140))
    d.line(P((1336, 1060), (1336, 1046)), fill=sil, width=3 * S); d.line(P((1336, 1060), (1347, 1063)), fill=sil, width=3 * S)
    # the office wall
    gradient_wall = Image.new('RGBA', (W, H - 1262 * S), (0, 0, 0, 255))
    gradient(gradient_wall, [(0, (30, 26, 36)), (1298, (18, 16, 24))])
    im.alpha_composite(gradient_wall, (0, 1262 * S))
    d = ImageDraw.Draw(im)
    for xx in range(40, 1600, 120):
        d.line(P((xx, 1262), (xx, 2300)), fill=(36, 31, 42), width=2 * S)
    d.rectangle(P((0, 1262), (1600, 1272)), fill=(48, 38, 40))
    # floor (carpet) and skirting
    d.rectangle(P((0, 2300), (1600, 2560)), fill=(46, 20, 24))
    d.rectangle(P((0, 2290), (1600, 2302)), fill=(58, 42, 34))
    # doorway: scene beyond the sill
    ox0, oy0, ox1, oy1 = 520, 1360, 1080, 2296
    scene = Image.new('RGBA', ((ox1 - ox0) * S, (oy1 - oy0) * S), (0, 0, 0, 255))
    gradient(scene, [(0, (10, 16, 22)), (936, (26, 32, 38))])
    sd = ImageDraw.Draw(scene)
    def Q(*pts): return [((x - ox0) * S, (y - oy0) * S) for x, y in pts]
    # train body
    sd.rectangle(Q((ox0, 1690), (ox1, 2150)), fill=(44, 52, 66))
    sd.rectangle(Q((ox0, 1675), (ox1, 1700)), fill=(60, 70, 86))
    sd.rectangle(Q((ox0, 2120), (ox1, 2150)), fill=(28, 32, 40))
    # windows and the open door of the carriage
    for wx0, wx1 in ((ox0 - 20, 640), (700, 830), (960, ox1 + 20)):
        sd.rectangle(Q((wx0, 1760), (wx1, 1900)), fill=(255, 226, 156))
    sd.rectangle(Q((842, 1730), (948, 2150)), fill=(255, 236, 182))   # open doorway, lit
    sd.rectangle(Q((842, 1730), (948, 1738)), fill=(70, 80, 96))
    # seats seen through the windows (blue moquette)
    for sx in (560, 742, 990):
        sd.rounded_rectangle(Q((sx, 1830), (sx + 70, 1900)), radius=10 * S, fill=(52, 78, 140))
    sd.rounded_rectangle(Q((868, 1960), (938, 2050)), radius=10 * S, fill=(52, 78, 140))  # first seat
    # platform
    sd.rectangle(Q((ox0, 2150), (ox1, oy1)), fill=(92, 94, 100))
    sd.rectangle(Q((ox0, 2160), (ox1, 2178)), fill=(236, 200, 40))   # yellow line
    for xx in range(ox0 - 40, ox1 + 60, 90):
        sd.line(Q((xx, 2180), (xx - 30, oy1)), fill=(78, 80, 86), width=2 * S)
    sd.line(Q((ox0, 2236), (ox1, 2236)), fill=(78, 80, 86), width=2 * S)
    # destination board with amber dots
    bx0, by0, bx1, by1 = 556, 1420, 1044, 1540
    sd.rectangle(Q((bx0 - 8, by0 - 8), (bx1 + 8, by1 + 8)), fill=(40, 42, 48))
    sd.rectangle(Q((bx0, by0), (bx1, by1)), fill=(6, 6, 8))
    sd.line(Q((700, 1360), (700, by0 - 8)), fill=(40, 42, 48), width=4 * S)
    sd.line(Q((900, 1360), (900, by0 - 8)), fill=(40, 42, 48), width=4 * S)
    word = 'YESTERDAY'; pitch = 7.8; gap = 2
    cols = len(word) * 5 + (len(word) - 1) * gap
    x0 = (bx0 + bx1) / 2 - cols * pitch / 2 + pitch / 2; y0 = (by0 + by1) / 2 - 3 * pitch
    dots = []
    for i, ch in enumerate(word):
        for r, row in enumerate(DOTS[ch]):
            for c, v in enumerate(row):
                if v == '1':
                    dots.append((x0 + (i * (5 + gap) + c) * pitch, y0 + r * pitch))
    glowl = Image.new('RGBA', scene.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(glowl)
    for (x, y) in dots: gd.ellipse(Q((x - 5, y - 5), (x + 5, y + 5)), fill=AMBER + (200,))
    scene.alpha_composite(glowl.filter(ImageFilter.GaussianBlur(6 * S)))
    for (x, y) in dots: sd.ellipse(Q((x - 2.9, y - 2.9), (x + 2.9, y + 2.9)), fill=(255, 196, 80))
    # station clock on a pillar, right
    sd.rectangle(Q((1018, 1560), (1034, 2150)), fill=(34, 38, 46))
    sd.ellipse(Q((990, 1580), (1062, 1652)), fill=(238, 238, 230), outline=(30, 30, 34), width=4 * S)
    sd.line(Q((1026, 1616), (1026, 1592)), fill=(20, 20, 20), width=4 * S)
    sd.line(Q((1026, 1616), (1006, 1626)), fill=(20, 20, 20), width=4 * S)
    # lamp, left
    sd.rectangle(Q((588, 1590), (598, 2160)), fill=(28, 30, 36))
    sd.rectangle(Q((572, 1572), (614, 1594)), fill=(28, 30, 36))
    lampl = Image.new('RGBA', scene.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lampl)
    ld.ellipse(Q((543, 1545), (643, 1645)), fill=(255, 230, 170, 150))
    scene.alpha_composite(lampl.filter(ImageFilter.GaussianBlur(22 * S)))
    sd.ellipse(Q((580, 1590), (606, 1608)), fill=(255, 244, 210))
    # bench nobody would choose
    sd.rectangle(Q((640, 2190), (780, 2204)), fill=(70, 54, 40))
    sd.rectangle(Q((650, 2204), (658, 2236)), fill=(40, 40, 44)); sd.rectangle(Q((762, 2204), (770, 2236)), fill=(40, 40, 44))
    im.alpha_composite(scene, (ox0 * S, oy0 * S))
    d = ImageDraw.Draw(im)
    # light spill onto the office floor
    glow(im, lambda g: g.polygon(P((ox0, 2300), (ox1, 2300), (1250, 2560), (350, 2560)), fill=(255, 214, 140, 70)), 18)
    glow(im, lambda g: g.rectangle(P((ox0 - 30, oy0 - 30), (ox1 + 30, oy1)), outline=(255, 210, 140, 90), width=40 * S), 30)
    d = ImageDraw.Draw(im)
    # door frame
    fr = (66, 44, 30)
    d.rectangle(P((ox0 - 34, oy0 - 34), (ox0, oy1)), fill=fr)
    d.rectangle(P((ox1, oy0 - 34), (ox1 + 34, oy1)), fill=fr)
    d.rectangle(P((ox0 - 34, oy0 - 34), (ox1 + 34, oy0)), fill=fr)
    d.rectangle(P((ox0 - 6, oy1 - 4), (ox1 + 6, oy1 + 6)), fill=(84, 64, 46))   # sill
    # the door leaf, open into the office (hinge on the left)
    leaf = P((ox0 - 34, oy0 - 30), (330, oy0 - 96), (330, oy1 + 70), (ox0 - 34, oy1 + 4))
    d.polygon(leaf, fill=(84, 56, 38))
    d.polygon(P((468, oy0 + 20), (360, oy0 - 26), (360, 1760), (468, 1770)), fill=(70, 46, 32))
    d.polygon(P((468, 1840), (360, 1836), (360, oy1 + 20), (468, oy1 - 40)), fill=(70, 46, 32))
    d.ellipse(P((346, 1800), (366, 1824)), fill=GOLD)
    # tape measure across the sill
    d.polygon(P((950, 2236), (966, 2236), (1020, 2340), (1000, 2344)), fill=(236, 196, 40))
    for k in range(6):
        yy = 2250 + k * 15
        d.line(P((954 + k * 7.5, yy), (962 + k * 7.5, yy)), fill=(40, 30, 10), width=2 * S)
    d.rounded_rectangle(P((990, 2330), (1060, 2380)), radius=8 * S, fill=(200, 40, 36))
    d.ellipse(P((1014, 2344), (1036, 2366)), fill=(150, 26, 24))
    # the warning, pinned to the wall right of the door
    sheet = Image.new('RGBA', (300 * S, 380 * S), (0, 0, 0, 0)); sh = ImageDraw.Draw(sheet)
    sh.rectangle([0, 0, 300 * S, 380 * S], fill=(236, 230, 214))
    sh.line([(150 * S, 0), (150 * S, 380 * S)], fill=(210, 202, 184), width=2 * S)
    sh.line([(0, 190 * S), (300 * S, 190 * S)], fill=(210, 202, 184), width=2 * S)
    sh.rectangle([10 * S, 0, 14 * S, 380 * S], fill=(196, 196, 196))      # the printer's grey stripe
    tf = F(CINZEL, 15, 700); bf = F(TITLE, 17); sf = F(EB, 15, 500)
    sh.text((26 * S, 22 * S), 'RELATIVISTIC INVESTIGATION', font=tf, fill=(40, 40, 50))
    sh.text((26 * S, 42 * S), 'BUREAU', font=tf, fill=(40, 40, 50))
    sh.text((26 * S, 70 * S), 'CASE STATUS: NOT YET OCCURRED', font=sf, fill=(60, 60, 70))
    yy = 118
    for ln in ['DO NOT ALLOW', 'DEREK GENT', 'TO BOARD THE', 'MYSTERIOUS', 'TRAIN.']:
        sh.text((26 * S, yy * S), ln, font=bf, fill=(30, 30, 36)); yy += 30
    sh.text((26 * S, 300 * S), 'SENDER D.O.B.: NOT YET', font=sf, fill=(60, 60, 70))
    sh.ellipse([196 * S, 296 * S, 280 * S, 372 * S], outline=(150, 104, 60), width=6 * S)   # the tea ring
    sh.rectangle([192 * S, 318 * S, 204 * S, 332 * S], fill=(236, 230, 214))                 # its bite
    sheet = sheet.rotate(4, resample=Image.BICUBIC, expand=True)
    shadow = Image.new('RGBA', sheet.size, (0, 0, 0, 0)); shadow.putalpha(sheet.split()[3].point(lambda v: v // 2))
    im.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(8 * S)), (1176 * S, 1586 * S))
    im.alpha_composite(sheet, (1164 * S, 1570 * S))
    d = ImageDraw.Draw(im)
    d.ellipse(P((1306, 1572), (1326, 1592)), fill=GOLD)
    # Mrs Marsh's ruling, on a sticky note left of the door (Ch19: 'It is not decorative. It is a platform.')
    note = Image.new('RGBA', (230 * S, 200 * S), (0, 0, 0, 0)); nd = ImageDraw.Draw(note)
    nd.rectangle([0, 0, 230 * S, 200 * S], fill=(246, 214, 92))
    nd.rectangle([0, 0, 230 * S, 26 * S], fill=(236, 200, 74))
    nf = F(TITLE, 22); y_ = 40
    for ln in ['IT IS NOT', 'DECORATIVE.', 'IT IS A', 'PLATFORM.']:
        nd.text((16 * S, y_ * S), ln, font=nf, fill=(40, 34, 30)); y_ += 30
    nd.text((16 * S, 166 * S), '– Mgmt', font=F(EBI, 22, 500), fill=(60, 50, 40))
    note = note.rotate(-6, resample=Image.BICUBIC, expand=True)
    sh2 = Image.new('RGBA', note.size, (0, 0, 0, 0)); sh2.putalpha(note.split()[3].point(lambda v: v // 2))
    im.alpha_composite(sh2.filter(ImageFilter.GaussianBlur(6 * S)), (76 * S, 1610 * S))
    im.alpha_composite(note, (66 * S, 1598 * S))
    d = ImageDraw.Draw(im)
    # Derek's mug on the carpet, right of the light (its chipped base made the ring)
    mx0, my0, mx1, my1 = 1290, 2318, 1420, 2448
    d.ellipse(P((mx0 - 16, my1 - 14), (mx1 + 16, my1 + 14)), fill=(30, 12, 16))
    d.rounded_rectangle(P((mx0, my0), (mx1, my1)), radius=12 * S, fill=(236, 232, 222))
    d.arc(P((mx1 - 24, my0 + 26), (mx1 + 40, my0 + 96)), 270, 90, fill=(236, 232, 222), width=12 * S)
    d.ellipse(P((mx0, my0 - 12), (mx1, my0 + 12)), fill=(214, 208, 196))
    d.ellipse(P((mx0 + 8, my0 - 6), (mx1 - 8, my0 + 8)), fill=(120, 76, 44))
    mf = F(TITLE, 19)
    for k, ln in enumerate(['MIND', 'THE', 'ORDER']):
        tw = d.textlength(ln, font=mf)
        d.text((((mx0 + mx1) / 2) * S - tw / 2, (my0 + 26 + k * 28) * S), ln, font=mf, fill=(30, 40, 70))
    # --- type ---
    sl = F(CINZEL, 40, 700)
    w = spaced(d, (800 * S, 66 * S), 'RELATIVISTIC INVESTIGATION BUREAU, BOOK 2', sl, GOLD, track=3)
    d.line(P((40, 92), (800 - w / S / 2 - 20, 92)), fill=GOLD, width=3 * S)
    d.line(P((800 + w / S / 2 + 20, 92), (1560, 92)), fill=GOLD, width=3 * S)
    # the hook: true to the plot (the sheet arrives on Monday and is printed on Tuesday)
    spaced(d, (800 * S, 124 * S), 'The warning came before it was written.', F(EBI, 50, 520), CREAM)
    # ornament with RIB monogram
    yo = 228
    d.line(P((260, yo), (730, yo)), fill=GOLD, width=2 * S); d.line(P((870, yo), (1340, yo)), fill=GOLD, width=2 * S)
    for xx in (250, 1350):
        d.polygon(P((xx - 10, yo), (xx, yo - 10), (xx + 10, yo), (xx, yo + 10)), fill=GOLD)
    d.ellipse(P((744, yo - 46), (856, yo + 46)), outline=GOLD, width=3 * S)
    spaced(d, (800 * S, (yo - 24) * S), 'RIB', F(CINZEL, 40, 700), GOLD, track=2)
    def title_line(text, y, size, fill, track=0):
        f = F(TITLE, size)
        spaced(d, (800 * S, y * S), text, f, (0, 0, 0), track=track)  # shadow pass below
    # draw with a soft shadow
    tl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); td = ImageDraw.Draw(tl)
    lines = [('THE WARNING', 304, 156, CREAM, 2), ('THAT WAS', 528, 118, CREAM, 6), ('SENT TOO', 690, 190, GOLD, 2), ('LATE', 900, 236, GOLD, 10)]
    for text, y, size, fill, tr in lines:
        spaced(td, (800 * S + 6 * S, y * S + 8 * S), text, F(TITLE, size), (0, 0, 0, 200), track=tr)
    im.alpha_composite(tl.filter(ImageFilter.GaussianBlur(7 * S)))
    d = ImageDraw.Draw(im)
    widths = {}
    for text, y, size, fill, tr in lines:
        widths[text] = spaced(d, (800 * S, y * S), text, F(TITLE, size), fill, track=tr)
    wt = widths['THAT WAS'] / S
    d.line(P((300, 600), (800 - wt / 2 - 30, 600)), fill=GOLD, width=3 * S)
    d.line(P((800 + wt / 2 + 30, 600), (1300, 600)), fill=GOLD, width=3 * S)
    # byline
    spaced(d, (800 * S, 2404 * S), 'Lothar J. Musiol', F(LB, 66, 700), CREAM)
    spaced(d, (800 * S, 2492 * S), 'writing as Spezala Genara Relavi (S.G.R.)', F(EBI, 50, 500), GOLD)
    out = im.convert('RGB').resize((1600, 2560), Image.LANCZOS)
    out.save(f'{OUT}/Kindle Front Cover.jpg', quality=92, subsampling=0)
    return out

def back():
    NAVY = (14, 22, 44)
    im = Image.new('RGB', (W, H), NAVY); d = ImageDraw.Draw(im)
    L, R = 170, 1430
    def wrap(text, font, width):
        words = text.split(); out = []; cur = ''
        for w_ in words:
            t = (cur + ' ' + w_).strip()
            if d.textlength(t, font=font) <= width * S: cur = t
            else: out.append(cur); cur = w_
        out.append(cur); return out
    def para(y, text, font, fill, lead, center=False, x0=L, width=R - L):
        for ln in wrap(text, font, width):
            x = x0 * S + ((width * S - d.textlength(ln, font=font)) / 2 if center else 0)
            d.text((x, y * S), ln, font=font, fill=fill); y += lead
        return y
    def rule(y, label=None):
        if label:
            f = F(CINZEL, 40, 700); w = spaced(d, (800 * S, (y - 26) * S), label, f, GOLD, track=4) / S
            d.line(P((L, y), (800 - w / 2 - 40, y)), fill=GOLD, width=2 * S); d.line(P((800 + w / 2 + 40, y), (R, y)), fill=GOLD, width=2 * S)
        else:
            d.line(P((L + 120, y), (780, y)), fill=GOLD, width=2 * S); d.line(P((820, y), (R - 120, y)), fill=GOLD, width=2 * S)
            d.polygon(P((800, y - 9), (809, y), (800, y + 9), (791, y)), fill=GOLD)
    hook = F(CINZEL, 58, 700)
    y = 120
    for ln in ['A WARNING DATED TOMORROW.', 'A DOOR THAT OPENS ONTO A RAILWAY.', 'AND HIS OWN VOICE SAYING', '“DON’T OPEN THE DOOR.”']:
        spaced(d, (800 * S, y * S), ln, hook, GOLD, track=2); y += 82
    spaced(d, (800 * S, (y + 4) * S), 'Afterwards.', F(EBI, 60, 520), CREAM); y += 84
    y += 30; rule(y); y += 60
    body = F(EB, 46, 420); lead = 64
    for t in ["On the Monday morning that Derek Gent closes the Bureau’s previous case, a sheet of paper appears on his desk where the folder lay a second before. It is on the Bureau’s own form. It is dated tomorrow. The box for the sender’s date of birth says NOT YET. And it says, in flat capitals: DO NOT ALLOW DEREK GENT TO BOARD THE MYSTERIOUS TRAIN.",
              "Then the office door opens onto a station platform that has no business being on the second floor of a London office building. An empty train stands waiting. Its board says YESTERDAY. And from somewhere inside it comes Derek’s own voice, telling him not to open the door.",
              "The door is already open.",
              "With his cousin Penny, Trevor and his tape measure, a visiting patent attorney from Munich and a building superintendent who regards the platform as a breach of the lease, Derek has until Wednesday to put one morning in the right order, before a landlord, two insurance companies and a very patient train do it for him."]:
        y = para(y, t, body, CREAM, lead) + 24
    y += 10; rule(y); y += 54
    y = para(y, 'A British mystery where the physics is real, the jokes are dry, and the hardest thing to do with a train is not get on it.', F(EBI, 44, 420), GOLD, 60, center=True, x0=L + 40, width=R - L - 80)
    y += 40; rule(y + 26, 'ABOUT THE AUTHOR'); y += 70
    y = para(y, 'Lothar J. Musiol is German by birth and American by choice, and writes in British because Love Actually’s Colin Frissell made it look worth the trouble. He divides his time between San Clemente and Passau with a grumpy Teacup Pomeranian named Gucci and eleven chickens.', F(EB, 42, 420), CREAM, 58, center=True, x0=L + 20, width=R - L - 40)
    y += 40
    y = para(y, 'Book 2 of the Relativistic Investigation Bureau. No previous case or physics background needed. Six optional lessons follow the story.', F(EB, 38, 420), CREAM, 52, center=True, x0=L + 60, width=R - L - 120)
    print('back cover text ends at y =', y)
    assert y < 2480, 'back cover text overflows'
    out = im.resize((1600, 2560), Image.LANCZOS)
    out.save(f'{OUT}/Kindle Back Cover.jpg', quality=92, subsampling=0)
    return out

if __name__ == '__main__':
    f = front(); b = back()
    for name, im in (('front', f), ('back', b)):
        t = im.copy(); t.thumbnail((800, 1280)); t.save(f'{OUT}/preview_{name}.jpg', quality=85)
