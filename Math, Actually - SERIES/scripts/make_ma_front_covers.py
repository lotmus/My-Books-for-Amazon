"""Math, Actually - Kindle front covers, Volumes 1-4 (1600x2560), drawn by script.
Navy and gold, Oswald type as on the earlier covers; the illustration band is a mathematical
motif per volume instead of the building scenes:
  1 From Arithmetic to Calculus          - a curve on a grid, Riemann rectangles and a tangent
  2 From Multivariable Calculus to Logic - a saddle surface z = x^2 - y^2 as a wire mesh
  3 From Differential Equations to Algebra - phase portrait of a damped oscillator
  4 From Category Theory to the Frontier - a commutative square with its diagonal
Fonts: Oswald, EB Garamond (Google Fonts, OFL). Set GOOGLE_FONTS to their folder if not on the box.
Usage: python make_ma_front_covers.py [out_dir]   -> "Cover  Volume N.jpg" """
import os, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
G = os.environ.get('GOOGLE_FONTS', '/usr/share/fonts/truetype/sand-box/google/')
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
W, H = 1600, 2560
NAVY = (7, 14, 33); GOLD = (243, 185, 62); CREAM = (244, 240, 228); BLUE = (120, 160, 215)
VOLS = {1: ['FROM ARITHMETIC TO CALCULUS'], 2: ['FROM MULTIVARIABLE CALCULUS', 'TO SET THEORY & LOGIC'],
        3: ['FROM DIFFERENTIAL EQUATIONS', 'TO ABSTRACT ALGEBRA'], 4: ['FROM CATEGORY THEORY', 'TO THE FRONTIER']}

def oswald(size, wght=600):
    f = ImageFont.truetype(G + 'Oswald/Oswald-VariableFont_wght.ttf', size)
    try: f.set_variation_by_axes([wght])
    except Exception: pass
    return f
def garamond(size, italic=True):
    p = G + ('EB_Garamond/EBGaramond-Italic-VariableFont_wght.ttf' if italic else 'EB_Garamond/EBGaramond-VariableFont_wght.ttf')
    return ImageFont.truetype(p, size)

def tracked(d, cx, top, text, font, track, fill, shadow=False):
    """Centre text at cx with letter spacing; top = top of the capitals."""
    widths = [d.textlength(c, font=font) for c in text]
    total = sum(widths) + track * (len(text) - 1)
    asc = font.getbbox('H')[1]
    x = cx - total / 2
    for c, w in zip(text, widths):
        if shadow: d.text((x + 3, top - asc + 4), c, font=font, fill=(0, 0, 0))
        d.text((x, top - asc), c, font=font, fill=fill); x += w + track
    return total

def fit(text, cap, width, wght):
    """font size giving this cap height, and the tracking giving this width"""
    s = 20
    while True:
        f = oswald(s, wght); b = f.getbbox('H')
        if b[3] - b[1] >= cap: break
        s += 1
    tmp = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    w0 = sum(tmp.textlength(c, font=f) for c in text)
    return f, (width - w0) / max(1, len(text) - 1)

def base(vol):
    img = Image.new('RGB', (W, H), NAVY)
    # a faint glow behind the motif
    glow = Image.new('L', (W, H), 0); gd = ImageDraw.Draw(glow)
    gd.ellipse((200, 1250, 1400, 2350), fill=60); glow = glow.filter(ImageFilter.GaussianBlur(220))
    img = Image.composite(Image.new('RGB', (W, H), (22, 38, 78)), img, glow)
    d = ImageDraw.Draw(img)
    d.rectangle((28, 28, W - 29, H - 29), outline=GOLD, width=3)
    f, t = fit('MATH,', 250, 720, 600); tracked(d, W / 2, 174, 'MATH,', f, t, GOLD)
    f, t = fit('ACTUALLY', 250, 1182, 600); tracked(d, W / 2, 565, 'ACTUALLY', f, t, GOLD)
    f, t = fit('VOLUME %d' % vol, 70, 413, 600); tracked(d, W / 2, 921, 'VOLUME %d' % vol, f, t, GOLD)
    fs, ts = fit('FROM ARITHMETIC TO CALCULUS', 58, 1013, 500)
    y = 1044
    for line in VOLS[vol]:
        tracked(d, W / 2, y, line, fs, ts, CREAM, shadow=True); y += 102
    d.line((630, 2375, 970, 2375), fill=GOLD, width=3)
    f, t = fit('LOTHAR J. MUSIOL', 65, 743, 600); tracked(d, W / 2, 2440, 'LOTHAR J. MUSIOL', f, t, CREAM, shadow=True)
    return img

S = 2  # supersampling for the line art
def layer():
    return Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0))
def P(x, y): return (x * S, y * S)

def motif1(L):
    d = ImageDraw.Draw(L)
    x0, x1, y0, y1 = 250, 1350, 1330, 2230          # plot box
    for i in range(12):
        x = x0 + i * (x1 - x0) / 11; d.line([P(x, y0), P(x, y1)], fill=BLUE + (55,), width=2 * S)
    for i in range(9):
        y = y0 + i * (y1 - y0) / 8; d.line([P(x0, y), P(x1, y)], fill=BLUE + (55,), width=2 * S)
    ax, ay = x0 + 60, y1 - 60
    d.line([P(ax, ay), P(x1, ay)], fill=CREAM + (200,), width=4 * S); d.line([P(ax, ay), P(ax, y0)], fill=CREAM + (200,), width=4 * S)
    d.polygon([P(x1 + 22, ay), P(x1 - 6, ay - 14), P(x1 - 6, ay + 14)], fill=CREAM + (200,))
    d.polygon([P(ax, y0 - 22), P(ax - 14, y0 + 6), P(ax + 14, y0 + 6)], fill=CREAM + (200,))
    f = lambda u: ay - (120 + 520 * (0.5 + 0.5 * math.tanh((u - 0.45) * 4)) + 90 * math.sin(u * 7))  # u in 0..1
    X = lambda u: ax + 40 + u * (x1 - ax - 80)
    n = 10; a, b = 0.12, 0.88
    for k in range(n):
        u = a + (b - a) * k / n; u2 = a + (b - a) * (k + 1) / n
        top = f(u)
        d.rectangle([P(X(u), top), P(X(u2), ay)], fill=GOLD + (45,), outline=GOLD + (170,), width=2 * S)
    pts = [P(X(u / 400), f(u / 400)) for u in range(0, 401)]
    d.line(pts, fill=GOLD + (255,), width=9 * S, joint='curve')
    u = 0.62; h = 1e-4; slope = (f(u + h) - f(u - h)) / (X(u + h) - X(u - h))
    px, py = X(u), f(u); dx = 330
    d.line([P(px - dx, py - slope * dx), P(px + dx, py + slope * dx)], fill=CREAM + (255,), width=5 * S)
    d.ellipse([P(px - 16, py - 16), P(px + 16, py + 16)], fill=CREAM + (255,))

def motif2(L):
    d = ImageDraw.Draw(L)
    cx, cy, sc = 800, 1800, 360
    ca, sa = math.cos(math.radians(35)), math.sin(math.radians(35))
    def proj(x, y):
        z = x * x - y * y
        az = math.radians(28); X = x * math.cos(az) - y * math.sin(az); Y = (x * math.sin(az) + y * math.cos(az)) * 0.5 - z * 0.5
        return P(cx + X * sc * 1.05, cy + Y * sc)
    N = 14; R = 1.25
    for i in range(N + 1):
        t = -R + 2 * R * i / N
        a = [proj(t, -R + 2 * R * k / 120) for k in range(121)]
        b = [proj(-R + 2 * R * k / 120, t) for k in range(121)]
        w = 6 if i in (0, N, N // 2) else 3
        d.line(a, fill=GOLD + (235 if w == 6 else 170,), width=w * S, joint='curve')
        d.line(b, fill=BLUE + (230 if w == 6 else 150,), width=w * S, joint='curve')
    # the saddle point
    x, y = proj(0, 0); d.ellipse([x - 16 * S, y - 16 * S, x + 16 * S, y + 16 * S], fill=CREAM + (255,))

def motif3(L):
    d = ImageDraw.Draw(L)
    cx, cy, sc = 800, 1790, 175
    F = lambda x, y: (y, -x - 0.35 * y)
    for i in range(-7, 8):
        for j in range(-5, 6):
            x, y = i * 0.6, j * 0.6
            u, v = F(x, y); m = math.hypot(u, v) or 1
            l = 0.22
            x2, y2 = x + u / m * l, y + v / m * l
            p1, p2 = (cx + x * sc, cy - y * sc), (cx + x2 * sc, cy - y2 * sc)
            if not (230 < p1[0] < 1370 and 1300 < p1[1] < 2270): continue
            d.line([P(*p1), P(*p2)], fill=BLUE + (120,), width=3 * S)
            ang = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
            for s in (2.6, -2.6):
                d.line([P(*p2), P(p2[0] - 12 * math.cos(ang + s), p2[1] - 12 * math.sin(ang + s))], fill=BLUE + (120,), width=3 * S)
    for (x, y) in [(3.0, 0.0), (-3.0, 0.5), (0.0, 2.6), (0.5, -2.7)]:
        pts = []
        for k in range(4000):
            if not (230 < cx + x * sc < 1370 and 1300 < cy - y * sc < 2270): break
            pts.append(P(cx + x * sc, cy - y * sc))
            u, v = F(x, y); x += u * 0.004; y += v * 0.004
        d.line(pts, fill=GOLD + (240,), width=6 * S, joint='curve')
    d.ellipse([P(cx - 15, cy - 15), P(cx + 15, cy + 15)], fill=CREAM + (255,))

def arrow(d, a, b, col, w, curve=0, dash=False, r=70):
    (x1, y1), (x2, y2) = a, b
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    sx, sy, ex, ey = x1 + ux * r, y1 + uy * r, x2 - ux * r, y2 - uy * r
    mx, my = (sx + ex) / 2 - uy * curve, (sy + ey) / 2 + ux * curve
    pts = [((1 - t) ** 2 * sx + 2 * (1 - t) * t * mx + t * t * ex, (1 - t) ** 2 * sy + 2 * (1 - t) * t * my + t * t * ey) for t in [k / 60 for k in range(61)]]
    if dash:
        for k in range(0, 60, 4): d.line([P(*pts[k]), P(*pts[k + 2])], fill=col, width=w * S)
    else: d.line([P(*p) for p in pts], fill=col, width=w * S, joint='curve')
    tx, ty = pts[-1][0] - pts[-3][0], pts[-1][1] - pts[-3][1]; ang = math.atan2(ty, tx)
    d.polygon([P(ex + 6 * math.cos(ang), ey + 6 * math.sin(ang)), P(ex - 34 * math.cos(ang - 0.42), ey - 34 * math.sin(ang - 0.42)),
               P(ex - 34 * math.cos(ang + 0.42), ey - 34 * math.sin(ang + 0.42))], fill=col)
    return pts[30]

def motif4(L):
    d = ImageDraw.Draw(L)
    # faint concentric rings and spokes behind the diagram
    cx, cy = 800, 1790
    for r in range(120, 640, 85): d.ellipse([P(cx - r, cy - r), P(cx + r, cy + r)], outline=BLUE + (45,), width=2 * S)
    A, B, C, D = (430, 1440), (1170, 1440), (430, 2140), (1170, 2140)
    fl = garamond(76 * S); fs = garamond(64 * S)
    for p, lab in ((A, 'A'), (B, 'B'), (C, 'C'), (D, 'D')):
        d.ellipse([P(p[0] - 62, p[1] - 62), P(p[0] + 62, p[1] + 62)], fill=NAVY + (255,), outline=GOLD + (255,), width=5 * S)
        d.text(P(*p), lab, font=fl, fill=CREAM + (255,), anchor='mm')
    def lab(pt, t, dx, dy): d.text(P(pt[0] + dx, pt[1] + dy), t, font=fs, fill=CREAM + (235,), anchor='mm')
    m = arrow(d, A, B, GOLD + (255,), 7); lab(m, 'f', 0, -50)
    m = arrow(d, B, D, GOLD + (255,), 7); lab(m, 'g', 45, 0)
    m = arrow(d, A, C, GOLD + (255,), 7); lab(m, 'h', -45, 0)
    m = arrow(d, C, D, GOLD + (255,), 7); lab(m, 'k', 0, 52)
    m = arrow(d, A, D, BLUE + (230,), 5, dash=True); lab(m, '', 0, 0)
    d.text(P(cx + 90, cy - 110), 'gf = kh', font=garamond(66 * S), fill=BLUE + (240,), anchor='lm')

def make(vol):
    img = base(vol)
    L = layer(); [None, motif1, motif2, motif3, motif4][vol](L)
    L = L.resize((W, H), Image.LANCZOS)
    img.paste(L, (0, 0), L)
    return img

if __name__ == '__main__':
    for v in (1, 2, 3, 4):
        im = make(v); im.save(os.path.join(OUT, 'Cover  Volume %d.jpg' % v), quality=92)
    print('done')
