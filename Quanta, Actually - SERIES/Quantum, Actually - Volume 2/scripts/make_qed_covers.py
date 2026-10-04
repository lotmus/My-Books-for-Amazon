"""Front and back covers for Quanta, Actually Volume 2,
'Quantum, Actually — Volume 2: A QED Course' by Lothar J. Musiol.

Matches the series covers (The Quantum World front/back, The Quantum
Conversation back): 2202 x 3520 px portrait, black star field with blue
glow, double gold frame, Cinzel gold title, serif subtitle, a gold-ruled
feature box and a round badge on the front, icon list and quote box on the back.

Usage: python make_qed_covers.py OUTDIR
"""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H = 2202, 3520
GOLD = (222, 172, 78)
GOLD_LT = (255, 228, 150)
GOLD_DK = (150, 98, 30)
CREAM = (244, 236, 214)
BLUE = (120, 190, 255)
ORANGE = (255, 170, 70)

GOOG = '/usr/share/fonts/truetype/sand-box/google/'
FONTS = {
    'cinzel': [r'C:\Windows\Fonts\Cinzel-Regular.ttf', (GOOG + 'Cinzel/Cinzel-VariableFont_wght.ttf', b'Regular')],
    'cinzel_b': [r'C:\Windows\Fonts\Cinzel-Black.ttf', (GOOG + 'Cinzel/Cinzel-VariableFont_wght.ttf', b'Bold')],
    'serif': [r'C:\Windows\Fonts\georgia.ttf', (GOOG + 'Gelasio/Gelasio-VariableFont_wght.ttf', b'Regular')],
    'serif_i': [r'C:\Windows\Fonts\georgiai.ttf', (GOOG + 'Gelasio/Gelasio-Italic-VariableFont_wght.ttf', b'Regular')],
    'serif_b': [r'C:\Windows\Fonts\georgiab.ttf', (GOOG + 'Gelasio/Gelasio-VariableFont_wght.ttf', b'Bold')],
}


def F(kind, size):
    for c in FONTS[kind]:
        path, var = c if isinstance(c, tuple) else (c, None)
        if os.path.exists(path):
            f = ImageFont.truetype(path, size)
            if var:
                try:
                    f.set_variation_by_name(var)
                except Exception:
                    pass
            return f
    raise FileNotFoundError(kind)


def tw(font, s, track=0):
    return sum(font.getlength(c) for c in s) + track * (len(s) - 1) if track else font.getlength(s)


def text_c(d, xy, s, font, fill, track=0, anchor_top=True):
    """Centre s horizontally at x; y is the top of the capital 'H'."""
    x, y = xy
    w = tw(font, s, track)
    y0 = y - font.getbbox('H')[1]
    if not track:
        d.text((x - w / 2, y0), s, font=font, fill=fill)
        return w
    cx = x - w / 2
    for ch in s:
        d.text((cx, y0), ch, font=font, fill=fill)
        cx += font.getlength(ch) + track
    return w


# ------------------------------------------------------------ background
def starfield(seed):
    rng = random.Random(seed)
    glow = Image.new('RGB', (W // 8, H // 8), (4, 5, 12))
    gd = ImageDraw.Draw(glow)
    for cx, cy, r, col in ((0.75, 0.30, 0.22, (20, 38, 92)), (0.20, 0.62, 0.25, (15, 32, 80)),
                           (0.55, 0.62, 0.20, (42, 26, 76)), (0.85, 0.80, 0.18, (15, 44, 86)),
                           (0.30, 0.18, 0.15, (26, 26, 68))):
        X, Y, R = cx * W / 8, cy * H / 8, r * W / 8
        gd.ellipse((X - R, Y - R, X + R, Y + R), fill=col)
    base = glow.filter(ImageFilter.GaussianBlur(40)).resize((W, H), Image.BICUBIC)
    px = base.load()
    for _ in range(5200):
        x, y, v = rng.randrange(W), rng.randrange(H), rng.random() ** 3
        c = 90 + 165 * v
        t = (0.85, 0.9, 1.0) if rng.random() < 0.7 else (1.0, 0.9, 0.7)
        o = px[x, y]
        px[x, y] = tuple(max(o[i], int(c * t[i])) for i in range(3))
    halo = Image.new('RGB', (W, H))
    hd = ImageDraw.Draw(halo)
    for _ in range(70):
        x, y, r = rng.randrange(W), rng.randrange(H), rng.uniform(2, 5)
        hd.ellipse((x - r, y - r, x + r, y + r), fill=(230, 235, 255))
    base = ImageChops.add(base, halo.filter(ImageFilter.GaussianBlur(6)))
    return ImageChops.add(base, halo)


def binary_column(img, x0, y0, y1, seed, cols=3):
    lay = Image.new('RGB', img.size)
    d = ImageDraw.Draw(lay)
    f = F('serif', 34)
    rng = random.Random(seed)
    for c in range(cols):
        for y in range(y0, y1, 44):
            fade = 1 - abs((y - (y0 + y1) / 2) / ((y1 - y0) / 2)) ** 2
            v = int(140 * max(0, fade) * rng.uniform(0.4, 1))
            d.text((x0 + c * 34, y), rng.choice('01'), font=f, fill=(int(v * 0.35), int(v * 0.85), v))
    return ImageChops.add(img, ImageChops.add(lay.filter(ImageFilter.GaussianBlur(3)), lay))


def frame(d, inset=36):
    d.rectangle((inset, inset, W - inset, H - inset), outline=GOLD, width=7)
    d.rectangle((inset + 22, inset + 22, W - inset - 22, H - inset - 22), outline=GOLD_DK, width=2)
    for x, y in ((W / 2, inset), (W / 2, H - inset)):
        d.polygon([(x, y - 18), (x + 18, y), (x, y + 18), (x - 18, y)], fill=GOLD)


def ornament(d, cx, y, half=260, col=GOLD):
    d.line((cx - half, y, cx - 26, y), fill=col, width=3)
    d.line((cx + 26, y, cx + half, y), fill=col, width=3)
    d.polygon([(cx, y - 14), (cx + 14, y), (cx, y + 14), (cx - 14, y)], fill=col)


def gold_text(img, cx, top, s, font, track=0, shadow=True):
    """Metallic gold lettering: vertical gradient through a text mask, dark
    edge, soft warm glow."""
    w = int(tw(font, s, track)) + 40
    bb = font.getbbox('HÅg')
    h = bb[3] - bb[1] + 60
    mask = Image.new('L', (w, h))
    md = ImageDraw.Draw(mask)
    capt = font.getbbox('H')
    text_c(md, (w / 2, 30), s, font, 255, track)
    # gradient
    cap_top = 30
    cap_bot = 30 + capt[3] - capt[1]
    grad = Image.new('RGB', (1, h))
    stops = [(0.0, GOLD_LT), (0.45, (238, 190, 92)), (0.62, (176, 116, 38)), (0.80, (226, 172, 80)), (1.0, (255, 222, 140))]
    for y in range(h):
        t = min(1, max(0, (y - cap_top) / max(1, cap_bot - cap_top)))
        for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
            if t0 <= t <= t1:
                u = (t - t0) / (t1 - t0)
                grad.putpixel((0, y), tuple(int(c0[i] + (c1[i] - c0[i]) * u) for i in range(3)))
                break
    grad = grad.resize((w, h))
    x0, y0 = int(cx - w / 2), int(top - 30)
    if shadow:
        glow = Image.new('RGB', (w + 80, h + 80))
        glow.paste((150, 95, 25), (40, 40), mask)
        glow = glow.filter(ImageFilter.GaussianBlur(14))
        region = img.crop((x0 - 40, y0 - 40, x0 + w + 40, y0 + h + 40))
        img.paste(ImageChops.add(region, ImageChops.multiply(glow, Image.new('RGB', glow.size, (150, 150, 150)))), (x0 - 40, y0 - 40))
        edge = mask.filter(ImageFilter.MaxFilter(5))
        img.paste((40, 22, 4), (x0 + 3, y0 + 4), edge)
    img.paste(grad, (x0, y0), mask)


# ------------------------------------------------------------ Feynman art
def wavy(d, p0, p1, col, width, amp=16, period=46):
    (x0, y0), (x1, y1) = p0, p1
    L = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = -uy, ux
    pts = []
    n = int(L / 3)
    for i in range(n + 1):
        s = L * i / n
        a = amp * math.sin(2 * math.pi * s / period)
        pts.append((x0 + ux * s + nx * a, y0 + uy * s + ny * a))
    d.line(pts, fill=col, width=width, joint='curve')


def wavy_arc(d, c, r, a0, a1, col, width, amp=14, waves=11):
    pts = []
    n = 400
    for i in range(n + 1):
        t = a0 + (a1 - a0) * i / n
        rr = r + amp * math.sin(2 * math.pi * waves * i / n)
        pts.append((c[0] + rr * math.cos(t), c[1] + rr * math.sin(t)))
    d.line(pts, fill=col, width=width, joint='curve')


def arrowhead(d, p, ang, col, s=30):
    x, y = p
    pts = [(x + s * math.cos(ang), y + s * math.sin(ang)),
           (x + s * 0.8 * math.cos(ang + 2.5), y + s * 0.8 * math.sin(ang + 2.5)),
           (x + s * 0.8 * math.cos(ang - 2.5), y + s * 0.8 * math.sin(ang - 2.5))]
    d.polygon(pts, fill=col)


def vertex_diagram(size, k=1.0):
    """One-loop vertex correction: electron in, electron out, photon up,
    a virtual photon joining the two legs. Returns an RGB glow layer."""
    Wd, Hd = size
    lay = Image.new('RGB', size)
    d = ImageDraw.Draw(lay)
    V = (Wd * 0.5, Hd * 0.40)
    A_ = (Wd * 0.10, Hd * 0.95)
    B_ = (Wd * 0.90, Hd * 0.95)
    P1 = (V[0] + (A_[0] - V[0]) * 0.55, V[1] + (A_[1] - V[1]) * 0.55)
    P2 = (V[0] + (B_[0] - V[0]) * 0.55, V[1] + (B_[1] - V[1]) * 0.55)
    top = (Wd * 0.5, Hd * 0.02)

    def draw(dd, widthmul, colmul):
        def c(col):
            return tuple(int(min(255, v * colmul)) for v in col)
        ew = int(9 * k * widthmul)
        dd.line([A_, V], fill=c(BLUE), width=ew)
        dd.line([V, B_], fill=c(BLUE), width=ew)
        wavy(dd, V, top, c(ORANGE), int(8 * k * widthmul), amp=20 * k, period=60 * k)
        # virtual photon joining the legs
        mx, my = (P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2
        r = math.hypot(P2[0] - P1[0], P2[1] - P1[1]) / 2
        wavy_arc(dd, (mx, my), r, 0, math.pi, c(GOLD_LT), int(7 * k * widthmul), amp=13 * k, waves=9)
        for P in (P1, P2, V):
            R = 14 * k * widthmul
            dd.ellipse((P[0] - R, P[1] - R, P[0] + R, P[1] + R), fill=c((255, 236, 200)))

    big = Image.new('RGB', size)
    draw(ImageDraw.Draw(big), 3.2, 0.9)
    big = big.filter(ImageFilter.GaussianBlur(28 * k))
    mid = Image.new('RGB', size)
    draw(ImageDraw.Draw(mid), 1.8, 1.0)
    mid = mid.filter(ImageFilter.GaussianBlur(8 * k))
    draw(d, 1.0, 1.15)
    for P, ang in ((((A_[0] + P1[0]) / 2, (A_[1] + P1[1]) / 2), math.atan2(V[1] - A_[1], V[0] - A_[0])),
                   (((B_[0] + P2[0]) / 2, (B_[1] + P2[1]) / 2), math.atan2(B_[1] - V[1], B_[0] - V[0]))):
        arrowhead(d, P, ang, (230, 245, 255), 34 * k)
    out = ImageChops.add(ImageChops.add(big, mid), lay)
    # bright core at the vertex
    core = Image.new('RGB', size)
    cd = ImageDraw.Draw(core)
    for R, col in ((150 * k, (120, 60, 10)), (80 * k, (220, 130, 40)), (34 * k, (255, 230, 170))):
        cd.ellipse((V[0] - R, V[1] - R, V[0] + R, V[1] + R), fill=col)
    core = core.filter(ImageFilter.GaussianBlur(30 * k))
    return ImageChops.add(out, core)


def orbits(size, k=1.0):
    lay = Image.new('RGB', size)
    Wd, Hd = size
    for i, (rx, ry, rot, col) in enumerate(((0.46, 0.13, -18, (60, 120, 255)), (0.44, 0.12, 22, (255, 150, 60)),
                                             (0.40, 0.16, 70, (90, 160, 255)), (0.48, 0.10, -55, (200, 120, 255)))):
        e = Image.new('RGB', size)
        ed = ImageDraw.Draw(e)
        cx, cy = Wd / 2, Hd * 0.40
        pts = []
        for j in range(361):
            t = math.radians(j)
            x, y = rx * Wd * math.cos(t), ry * Wd * math.sin(t)
            a = math.radians(rot)
            pts.append((cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)))
        ed.line(pts, fill=tuple(int(c * 0.55) for c in col), width=int(4 * k))
        lay = ImageChops.add(lay, ImageChops.add(e.filter(ImageFilter.GaussianBlur(9 * k)), e))
    return lay


def add_layer(img, lay, xy):
    x, y = xy
    region = img.crop((x, y, x + lay.width, y + lay.height))
    img.paste(ImageChops.add(region, lay), (x, y))


def glow_text(img, xy, s, font, col, blur=10):
    bb = ImageDraw.Draw(img).textbbox(xy, s, font=font)
    pad = blur * 4
    box = (int(bb[0]) - pad, int(bb[1]) - pad, int(bb[2]) + pad, int(bb[3]) + pad)
    lay = Image.new('RGB', (box[2] - box[0], box[3] - box[1]))
    ImageDraw.Draw(lay).text((xy[0] - box[0], xy[1] - box[1]), s, font=font, fill=col)
    lay = ImageChops.add(lay.filter(ImageFilter.GaussianBlur(blur)), lay)
    add_layer(img, lay, box[:2])


def wrap(d, font, text, width):
    words, lines, cur = text.split(), [], ''
    for w_ in words:
        t = (cur + ' ' + w_).strip()
        if cur and d.textlength(t, font=font) > width:
            lines.append(cur)
            cur = w_
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


# ------------------------------------------------------------ front
FEATURES = [
    '87 lessons and 9 prologues, every exercise solved',
    'The Dirac equation, built from scratch',
    'Feynman rules derived, not assumed',
    'Renormalization and the running charge',
    "Electron g\u22122: Schwinger\u2019s \u03b1/2\u03c0",
    'The Lamb shift, from vacuum polarization',
]


def front():
    img = starfield(31)
    img = binary_column(img, 92, 140, 1700, 4, cols=2)
    add_layer(img, orbits((1900, 1500)), (150, 1650))
    add_layer(img, vertex_diagram((1250, 1100)), (476, 1880))
    d = ImageDraw.Draw(img)
    frame(d)

    f = F('cinzel', 92)
    text_c(d, (W / 2, 150), 'QUANTUM, ACTUALLY', f, CREAM, track=14)
    ornament(d, W / 2, 285, 300)

    gold_text(img, W / 2, 380, 'A', F('cinzel_b', 170), track=0)
    gold_text(img, W / 2, 590, 'QED', F('cinzel_b', 400), track=20)
    gold_text(img, W / 2, 1060, 'COURSE', F('cinzel_b', 170), track=14)
    d = ImageDraw.Draw(img)
    vf = F('cinzel', 66)
    text_c(d, (W / 2, 1330), 'VOLUME 2', vf, GOLD, track=12)
    ornament(d, W / 2, 1356, 460)
    # put the label back over the ornament line
    vw = tw(vf, 'VOLUME 2', 12)
    d.rectangle((W / 2 - vw / 2 - 30, 1320, W / 2 + vw / 2 + 30, 1400), fill=(6, 8, 20))
    text_c(d, (W / 2, 1330), 'VOLUME 2', vf, GOLD, track=12)

    sf = F('serif', 82)
    text_c(d, (W / 2, 1455), 'From Mathematical Foundations', sf, CREAM)
    text_c(d, (W / 2, 1565), 'to One-Loop QED', sf, CREAM)

    # equation, left, glowing
    ef = F('serif_i', 100)
    glow_text(img, (140, 2260), '(g \u2212 2)/2 = \u03b1/2\u03c0', ef, (140, 200, 255), blur=12)
    glow_text(img, (175, 2420), '\u03b1 \u2248 1/137.036', F('serif_i', 58), (120, 170, 230), blur=8)

    # feature box, right
    d = ImageDraw.Draw(img)
    bx0, by0, bx1 = 1600, 1960, 2100
    hf, itf = F('cinzel_b', 46), F('serif', 40)
    y = by0 + 40
    heads = ['INSIDE', 'THE COURSE:']
    rows = []
    for s in FEATURES:
        rows.append(wrap(d, itf, s, bx1 - bx0 - 90))
    by1 = by0 + 40 + 2 * 58 + 30 + sum(len(r) * 50 + 46 for r in rows) + 10
    d.rectangle((bx0, by0, bx1, by1), fill=(10, 9, 14), outline=GOLD, width=5)
    d.rectangle((bx0 + 12, by0 + 12, bx1 - 12, by1 - 12), outline=GOLD_DK, width=2)
    for hl in heads:
        text_c(d, ((bx0 + bx1) / 2, y), hl, hf, GOLD_LT, track=3)
        y += 58
    y += 20
    for r in rows:
        d.line((bx0 + 30, y, bx1 - 30, y), fill=GOLD_DK, width=2)
        y += 16
        d.polygon([(bx0 + 40, y + 16), (bx0 + 50, y + 26), (bx0 + 40, y + 36), (bx0 + 30, y + 26)], fill=GOLD)
        for line in r:
            d.text((bx0 + 66, y), line, font=itf, fill=CREAM)
            y += 50
        y += 30

    # round badge, left
    cx, cy, R = 380, 2900, 245
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill=(8, 8, 16), outline=GOLD, width=8)
    d.ellipse((cx - R + 16, cy - R + 16, cx + R - 16, cy + R - 16), outline=GOLD_DK, width=2)
    bf = F('serif', 52)
    for i, s in enumerate(('Every Step', 'Derived.', 'Every Exercise', 'Solved.')):
        text_c(d, (cx, cy - 150 + i * 78), s, bf, CREAM)

    af = F('cinzel', 74)
    text_c(d, (W / 2, 3300), 'LOTHAR J. MUSIOL', af, CREAM, track=16)
    ornament(d, W / 2, 3420, 160)
    return img


# ------------------------------------------------------------ back
ITEMS = [
    ('arrows', 'FROM ARROWS TO THE DIRAC EQUATION',
     'Nine prologues start from Feynman\u2019s arrows; 38 lessons rebuild the mathematics, quantum mechanics, and relativity that QED needs.'),
    ('vertex', 'FEYNMAN RULES, DERIVED',
     'Local U(1) symmetry gives the QED Lagrangian. The vertex and the propagators are read off it, not assumed.'),
    ('xsec', 'FIVE PROCESSES, CALCULATED',
     'Electron\u2013muon and M\u00f8ller scattering, annihilation, Compton scattering, and pair production, all the way to cross sections.'),
    ('loop', 'RENORMALIZATION',
     'Loops, divergences, regularization, the running of \u03b1, and the Ward identity that keeps it all consistent.'),
    ('levels', 'ELECTRON g\u22122 AND THE LAMB SHIFT',
     'Schwinger\u2019s a = \u03b1/2\u03c0 from one loop, and why hydrogen\u2019s 2s and 2p levels are not quite equal.'),
    ('path', 'PATH INTEGRALS AND BEYOND',
     'Generating functionals, effective actions, finite temperature, strong fields, and QED inside the Standard Model.'),
]

BLURB = ('This is where the quantum world gets calculated. Starting from complex numbers and ending at the '
         'electron\u2019s anomalous magnetic moment, this course derives quantum electrodynamics one step at a '
         'time: 87 lessons, every worked example done in full, every exercise solved.')

QUOTE = ('\u201cDo start it as a first course in QED if linear algebra and ordinary quantum mechanics '
         'are willing to be rebuilt rather than assumed.\u201d')


def icon(d, kind, cx, cy, R=78):
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill=(10, 10, 18), outline=GOLD, width=5)
    c = GOLD_LT
    if kind == 'arrows':
        for a, L in ((-0.5, 50), (0.3, 42), (1.2, 46)):
            x1, y1 = cx - 30 + L * math.cos(a), cy + 20 - L * math.sin(a)
            d.line((cx - 30, cy + 20, x1, y1), fill=c, width=5)
            arrowhead(d, (x1, y1), math.atan2(y1 - cy - 20, x1 - cx + 30), c, 14)
    elif kind == 'vertex':
        d.line((cx - 44, cy + 40, cx, cy + 4, cx + 44, cy + 40), fill=c, width=5)
        wavy(d, (cx, cy + 4), (cx, cy - 48), c, 4, amp=7, period=18)
    elif kind == 'xsec':
        d.line((cx - 50, cy - 30, cx + 50, cy + 30), fill=c, width=5)
        d.line((cx - 50, cy + 30, cx + 50, cy - 30), fill=c, width=3)
        d.ellipse((cx - 10, cy - 10, cx + 10, cy + 10), fill=c)
    elif kind == 'loop':
        d.line((cx - 56, cy, cx - 28, cy), fill=c, width=5)
        d.line((cx + 28, cy, cx + 56, cy), fill=c, width=5)
        d.ellipse((cx - 28, cy - 28, cx + 28, cy + 28), outline=c, width=5)
    elif kind == 'levels':
        d.line((cx - 46, cy + 30, cx + 46, cy + 30), fill=c, width=5)
        d.line((cx - 46, cy - 18, cx - 4, cy - 18), fill=c, width=5)
        d.line((cx + 4, cy - 30, cx + 46, cy - 30), fill=c, width=5)
        f = F('serif_i', 30)
        d.text((cx - 40, cy - 2), 'g\u22122', font=f, fill=c)
    elif kind == 'path':
        for k_ in range(3):
            pts = [(cx - 50 + i * 5, cy + (k_ - 1) * 22 * math.sin(i / 20 * math.pi)) for i in range(21)]
            d.line(pts, fill=c, width=4)
        d.ellipse((cx - 58, cy - 8, cx - 42, cy + 8), fill=c)
        d.ellipse((cx + 42, cy - 8, cx + 58, cy + 8), fill=c)


def back():
    img = starfield(37)
    img = binary_column(img, 1975, 860, 1700, 9, cols=3)
    add_layer(img, orbits((1200, 1500), 0.8), (1000, 1560))
    add_layer(img, vertex_diagram((900, 820), 0.75), (1240, 1780))
    d = ImageDraw.Draw(img)
    frame(d)
    f = F('cinzel', 76)
    text_c(d, (W / 2, 140), 'QUANTUM, ACTUALLY \u00b7 VOLUME 2', f, GOLD, track=10)
    ornament(d, W / 2, 255, 260)
    gold_text(img, W / 2, 380, 'A QED COURSE', F('cinzel_b', 170), track=8)
    d = ImageDraw.Draw(img)
    sf = F('serif', 72)
    text_c(d, (W / 2, 690), 'From Mathematical Foundations to One-Loop QED', sf, CREAM)

    # blurb with drop cap
    x0, x1, y = 190, 1880, 860
    bf = F('serif', 56)
    cap = F('cinzel_b', 214)
    d.text((x0, y - 24), BLURB[0], font=cap, fill=GOLD)
    indent = cap.getlength(BLURB[0]) + 18
    words = BLURB[1:].split()
    lines, cur, li = [], '', 0
    for w_ in words:
        width = x1 - x0 - (indent if li < 2 else 0)
        t = (cur + ' ' + w_).strip()
        if cur and d.textlength(t, font=bf) > width:
            lines.append(cur)
            cur, li = w_, li + 1
        else:
            cur = t
    lines.append(cur)
    for i, s_ in enumerate(lines):
        d.text((x0 + (indent if i < 2 else 0), y + i * 78), s_, font=bf, fill=CREAM)
    y += len(lines) * 78 + 36
    ornament(d, W / 2, y, 380)
    y += 56

    hf, tf = F('serif_b', 48), F('serif', 43)
    for kind, head, txt in ITEMS:
        icon(d, kind, 270, y + 72, R=70)
        d.text((390, y), head, font=hf, fill=GOLD)
        ty = y + 64
        for s_ in wrap(d, tf, txt, 880):
            d.text((390, ty), s_, font=tf, fill=CREAM)
            ty += 53
        y = max(ty, y + 150) + 30

    # quote box
    qf = F('serif_i', 46)
    ql = wrap(d, qf, QUOTE, 1180)
    qh = len(ql) * 62 + 120
    qy = 3230 - qh
    assert qy >= y, (qy, y)
    d.rectangle((180, qy, 1460, qy + qh), fill=(8, 8, 14), outline=GOLD, width=4)
    for i, s_ in enumerate(ql):
        d.text((225, qy + 30 + i * 62), s_, font=qf, fill=CREAM)
    rf = F('serif', 38)
    s_ = '\u2014 from How to Read This Book'
    d.text((1420 - d.textlength(s_, font=rf), qy + qh - 66), s_, font=rf, fill=GOLD)

    ff = F('cinzel', 50)
    text_c(d, (W / 2, 3300), 'CLEAR EXPLANATIONS. REAL SCIENCE. MIND-BLOWING IDEAS.', ff, GOLD, track=4)
    ornament(d, W / 2, 3420, 120)
    return img


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    stem = 'Quantum, Actually - Volume 2 - 2202 x 3520 Portrait.jpg'
    p = os.path.join(out, 'Front Cover of ' + stem)
    front().save(p, quality=93, dpi=(300, 300))
    q = os.path.join(out, 'Back Cover of ' + stem)
    back().save(q, quality=93, dpi=(300, 300))
    print('wrote', p)
    print('wrote', q)


if __name__ == '__main__':
    main()
