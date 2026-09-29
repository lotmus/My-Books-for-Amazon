# Draws the diagram figures for "The Universe Has No Now" (Kindle, grayscale-proof)
# Spec: 4:3 landscape, 1800x1350 px, black strokes on white, lines >= 16 px (3 pt at page width),
# type >= 78 px (14 pt at page width). One figure per chapter. PNG for line art.
import os, math, sys
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
os.makedirs(OUT, exist_ok=True)
W, H = 1800, 1350
LW = 18            # main stroke
LW2 = 12           # secondary stroke (still > 3 pt)
FONT_B = "C:/Windows/Fonts/arialbd.ttf"
FONT_R = "C:/Windows/Fonts/arial.ttf"
FONT_I = "C:/Windows/Fonts/ariali.ttf"

def font(size=90, bold=True, italic=False):
    return ImageFont.truetype(FONT_I if italic else (FONT_B if bold else FONT_R), size)

def canvas():
    im = Image.new("L", (W, H), 255)
    return im, ImageDraw.Draw(im)

def text(d, xy, s, size=90, bold=True, anchor="mm", italic=False, fill=0):
    d.text(xy, s, font=font(size, bold, italic), fill=fill, anchor=anchor)

def arrow(d, p0, p1, lw=LW, head=48):
    d.line([p0, p1], fill=0, width=lw)
    ang = math.atan2(p1[1]-p0[1], p1[0]-p0[0])
    for s in (+1, -1):
        a = ang + math.pi + s*math.radians(28)
        d.line([p1, (p1[0]+head*math.cos(a), p1[1]+head*math.sin(a))], fill=0, width=lw)

def circle(d, c, r, lw=LW, fill=None):
    d.ellipse([c[0]-r, c[1]-r, c[0]+r, c[1]+r], outline=0, width=lw, fill=fill)

def dashed(d, pts, lw=LW, dash=40, gap=30):
    # polyline dashed
    for i in range(len(pts)-1):
        (x0,y0),(x1,y1) = pts[i], pts[i+1]
        L = math.hypot(x1-x0, y1-y0)
        if L == 0: continue
        ux, uy = (x1-x0)/L, (y1-y0)/L
        t = 0
        while t < L:
            t2 = min(t+dash, L)
            d.line([(x0+ux*t, y0+uy*t), (x0+ux*t2, y0+uy*t2)], fill=0, width=lw)
            t = t2 + gap

def dotted(d, pts, lw=LW, gap=44):
    for i in range(len(pts)-1):
        (x0,y0),(x1,y1) = pts[i], pts[i+1]
        L = math.hypot(x1-x0, y1-y0)
        n = max(1, int(L/gap))
        for k in range(n+1):
            x, y = x0+(x1-x0)*k/n, y0+(y1-y0)*k/n
            d.ellipse([x-lw/2, y-lw/2, x+lw/2, y+lw/2], fill=0)

def save(im, name):
    im.save(os.path.join(OUT, name), optimize=True)
    print("wrote", name)

def hatch_polygon_mask(im, poly, spacing=46, lw=10):
    """Diagonal hatch inside polygon."""
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon(poly, fill=255)
    hatch = Image.new("L", (W, H), 255)
    hd = ImageDraw.Draw(hatch)
    for k in range(-H, W+H, spacing):
        hd.line([(k, 0), (k+H, H)], fill=0, width=lw)
    im.paste(hatch, (0, 0), mask)

# ---------------- Fig 2: one event ----------------
def fig02():
    im, d = canvas()
    circle(d, (900, 675), 110, fill=0)
    text(d, (900, 340), "x", 200); text(d, (900, 1010), "t", 200)
    text(d, (470, 675), "y", 200); text(d, (1330, 675), "z", 200)
    text(d, (900, 1230), "one event: four numbers", 84, bold=False)
    save(im, "fig02.png")

# ---------------- Fig 5: two worldlines ----------------
def fig05():
    im, d = canvas()
    x0, ytop, ybot = 900, 180, 1200
    # stay-at-home: straight
    d.line([(x0, ybot), (x0, ytop)], fill=0, width=LW)
    # traveller: out and back
    d.line([(x0, ybot), (x0+430, 690), (x0, ytop)], fill=0, width=LW)
    arrow(d, (x0, 420), (x0, ytop-2), head=60)
    arrow(d, (x0+430, 690), (x0+30, ytop+20), head=60)
    circle(d, (x0, ybot), 34, fill=0); circle(d, (x0, ytop), 34, fill=0)
    text(d, (x0-300, 690), "older", 130, anchor="mm")
    text(d, (x0+430, 1010), "younger", 130, anchor="mm")
    text(d, (x0, 1290), "meet  ·  split  ·  meet again", 80, bold=False)
    text(d, (140, 700), "time", 80, bold=False, anchor="mm")
    arrow(d, (140, 900), (140, 500), lw=LW2, head=40)
    save(im, "fig05.png")

# ---------------- Fig 6: the loaf ----------------
def loaf_outline(d, x, y, w, h, depth):
    # front rectangle + top/side parallelograms
    d.rectangle([x, y, x+w, y+h], outline=0, width=LW)
    d.polygon([(x, y), (x+depth, y-depth), (x+w+depth, y-depth), (x+w, y)], outline=0)
    d.line([(x, y), (x+depth, y-depth), (x+w+depth, y-depth), (x+w, y)], fill=0, width=LW)
    d.line([(x+w+depth, y-depth), (x+w+depth, y+h-depth), (x+w, y+h)], fill=0, width=LW)

def fig06():
    im, d = canvas()
    loaf_outline(d, 260, 380, 1150, 650, 160)
    # thread
    pts = [(300, 900), (520, 760), (700, 820), (930, 620), (1120, 700), (1360, 480)]
    d.line(pts, fill=0, width=LW+6)
    circle(d, pts[-1], 26, fill=0)
    text(d, (420, 1180), "past", 140)
    text(d, (1300, 1180), "future", 140)
    arrow(d, (620, 1180), (1050, 1180), lw=LW2, head=44)
    text(d, (900, 130), "the block: all events, one thread is you", 78, bold=False)
    save(im, "fig06.png")

# ---------------- Fig 7: growing grid ----------------
def fig07():
    im, d = canvas()
    def grid(cx, cy, sp, r):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                circle(d, (cx+i*sp, cy+j*sp), r, fill=0)
    grid(470, 620, 150, 34)
    grid(1330, 620, 300, 34)
    arrow(d, (720, 620), (960, 620), head=60)
    text(d, (470, 1130), "earlier", 110)
    text(d, (1330, 1130), "later", 110)
    text(d, (900, 1270), "every dot sees the others recede — no center", 76, bold=False)
    save(im, "fig07.png")

# ---------------- Fig 10: timeline ----------------
def fig10():
    im, d = canvas()
    y = 600
    d.line([(120, y), (1680, y)], fill=0, width=LW)
    ticks = [(230, "1 second", "10 billion K"), (680, "3 minutes", "1 billion K"),
             (1160, "380,000 years", "3,000 K"), (1600, "now", "2.7 K")]
    for x, top, bot in ticks:
        d.line([(x, y-70), (x, y+70)], fill=0, width=LW)
        text(d, (x, y-190), top, 74)
        text(d, (x, y+190), bot, 74, bold=False)
    text(d, (900, 170), "the hot past, in four ticks", 90)
    text(d, (900, 1000), "temperature falls as the stretch grows", 76, bold=False)
    save(im, "fig10.png")

# ---------------- Fig 11: cube with one dot ----------------
def fig11():
    im, d = canvas()
    x, y, s, dp = 480, 420, 760, 260
    d.rectangle([x, y, x+s, y+s], outline=0, width=LW)
    d.line([(x, y), (x+dp, y-dp), (x+s+dp, y-dp), (x+s, y)], fill=0, width=LW)
    d.line([(x+s+dp, y-dp), (x+s+dp, y+s-dp), (x+s, y+s)], fill=0, width=LW)
    circle(d, (x+s*0.55, y+s*0.5), 30, fill=0)
    text(d, (900, 1270), "one cubic meter of smoothed universe: about one atom", 62, bold=False)
    save(im, "fig11.png")

# ---------------- Fig 12: last-scattering circle ----------------
def fig12():
    im, d = canvas()
    c, r = (900, 640), 470
    circle(d, c, r)
    circle(d, c, 26, fill=0); text(d, (900, 720), "us", 80, bold=False)
    # patches A and B
    for ang, lab, dx in ((180, "A", -1), (0, "B", 1)):
        px, py = c[0]+r*math.cos(math.radians(ang)), c[1]+r*math.sin(math.radians(ang))
        d.arc([c[0]-r, c[1]-r, c[0]+r, c[1]+r], ang-14, ang+14, fill=0, width=LW*3)
        text(d, (px+dx*150, py), lab, 170)
    text(d, (900, 1230), "A and B never met in the plain bang — yet they match", 64, bold=False)
    text(d, (900, 110), "the last-scattering sky", 84)
    save(im, "fig12.png")

# ---------------- Fig 13: burst then after ----------------
def fig13():
    im, d = canvas()
    ox, oy = 260, 1100
    arrow(d, (ox, oy), (1650, oy), lw=LW2, head=44); arrow(d, (ox, oy), (ox, 200), lw=LW2, head=44)
    text(d, (1560, 1200), "time", 76, bold=False); text(d, (ox, 130), "size", 76, bold=False)
    pts = [(ox, oy)] + [(ox+ i*3, oy - (1 - math.exp(-i/40))*620) for i in range(0, 120)]
    last = pts[-1]
    pts += [(last[0] + i*10, last[1] - i*1.6) for i in range(0, 120)]
    d.line(pts, fill=0, width=LW)
    text(d, (760, 760), "burst", 130); text(d, (1250, 620), "after", 130)
    save(im, "fig13.png")

# ---------------- Fig 15: three bubbles in a spreading field ----------------
def fig15():
    im, d = canvas()
    import random
    random.seed(7)
    for _ in range(220):
        x, y = random.randint(80, 1720), random.randint(80, 1270)
        circle(d, (x, y), 5, fill=0, lw=1)
    for c, r in (((520, 560), 260), ((1180, 420), 200), ((1220, 950), 240)):
        circle(d, c, r, lw=LW, fill=255)
    text(d, (900, 1290), "bubbles in a field that keeps stretching — a maybe", 72, bold=False)
    save(im, "fig15.png")

# ---------------- Fig 19: three futures ----------------
def fig19():
    im, d = canvas()
    ox, oy = 260, 1100
    arrow(d, (ox, oy), (1650, oy), lw=LW2, head=44); arrow(d, (ox, oy), (ox, 200), lw=LW2, head=44)
    text(d, (1560, 1200), "time", 76, bold=False); text(d, (ox, 130), "size", 76, bold=False)
    N = 130
    accel = [(ox+i*10, oy - (i*3.2 + (i/40)**3*22)) for i in range(N)]
    coast = [(ox+i*10, oy - i*4.6) for i in range(N)]
    recol = [(ox+i*10, oy - (14*i - 0.14*i*i)) for i in range(N) if 14*i - 0.14*i*i >= 0]
    d.line(accel, fill=0, width=LW)
    dashed(d, coast, lw=LW)
    dotted(d, recol, lw=LW-2)
    text(d, (560, 300), "accelerate  = data", 78, anchor="lm")
    text(d, (560, 410), "coast", 78, anchor="lm")
    text(d, (560, 520), "recollapse", 78, anchor="lm")
    d.line([(400, 300), (530, 300)], fill=0, width=LW)
    dashed(d, [(400, 410), (530, 410)], lw=LW)
    dotted(d, [(400, 520), (530, 520)], lw=LW-2)
    save(im, "fig19.png")

# ---------------- Fig 21: two clocks ----------------
def clock(d, c, r, hour_ang, min_ang):
    circle(d, c, r)
    for k in range(12):
        a = math.radians(k*30)
        d.line([(c[0]+(r-60)*math.sin(a), c[1]-(r-60)*math.cos(a)), (c[0]+(r-20)*math.sin(a), c[1]-(r-20)*math.cos(a))], fill=0, width=LW2)
    a = math.radians(hour_ang); d.line([c, (c[0]+r*0.5*math.sin(a), c[1]-r*0.5*math.cos(a))], fill=0, width=LW+6)
    a = math.radians(min_ang);  d.line([c, (c[0]+r*0.78*math.sin(a), c[1]-r*0.78*math.cos(a))], fill=0, width=LW)
    circle(d, c, 18, fill=0)

def fig21():
    im, d = canvas()
    clock(d, (480, 520), 300, 60, 180)
    clock(d, (1320, 760), 300, 45, 90)
    text(d, (480, 920), "high, far away", 84, bold=False)
    text(d, (1200, 1160), "low, near the mass: slow", 78)
    save(im, "fig21.png")

# ---------------- Fig 22: Kruskal rooms ----------------
def fig22():
    im, d = canvas()
    x0, y0, s = 350, 120, 1100
    d.rectangle([x0, y0, x0+s, y0+s], outline=0, width=LW)
    d.line([(x0, y0), (x0+s, y0+s)], fill=0, width=LW)
    d.line([(x0+s, y0), (x0, y0+s)], fill=0, width=LW)
    cx, cy = x0+s/2, y0+s/2
    text(d, (cx, y0+230), "black hole", 96)
    text(d, (cx, y0+s-230), "white hole", 96)
    text(d, (x0+200, cy), "outside", 96)
    text(d, (x0+s-200, cy), "outside", 96)
    text(d, (x0+200, cy+110), "(our side)", 56, bold=False)
    save(im, "fig22.png")

# ---------------- Fig 23: sphere, hash on the skin ----------------
def fig23():
    im, d = canvas()
    c, r = (900, 620), 430
    circle(d, c, r, lw=LW)
    for k in range(48):
        a = math.radians(k*7.5)
        p0 = (c[0]+(r-40)*math.cos(a), c[1]+(r-40)*math.sin(a))
        p1 = (c[0]+(r+40)*math.cos(a), c[1]+(r+40)*math.sin(a))
        d.line([p0, p1], fill=0, width=LW2)
    text(d, (900, 1200), "count the area, not the volume", 96)
    save(im, "fig23.png")

# ---------------- Fig 26: two horizons ----------------
def fig26():
    im, d = canvas()
    ox, oy = 260, 1100
    arrow(d, (ox, oy), (1650, oy), lw=LW2, head=44); arrow(d, (ox, oy), (ox, 200), lw=LW2, head=44)
    text(d, (1520, 1200), "distance", 76, bold=False); text(d, (ox, 130), "time", 76, bold=False)
    N = 120
    particle = [(ox + i*11, oy - i*7) for i in range(N)]
    event = [(ox + 900 - i*5.5, oy - i*7) for i in range(N)]
    d.line(particle, fill=0, width=LW)
    dashed(d, event, lw=LW)
    text(d, (1250, 760), "particle horizon", 66, anchor="lm")
    text(d, (1250, 880), "event horizon", 66, anchor="lm")
    d.line([(1120, 760), (1230, 760)], fill=0, width=LW)
    dashed(d, [(1120, 880), (1230, 880)], lw=LW)
    text(d, (900, 1290), "what we can see  /  what can still reach us", 72, bold=False)
    save(im, "fig26.png")

# ---------------- Fig 27: transit ----------------
def fig27():
    im, d = canvas()
    circle(d, (900, 380), 260, lw=LW)
    circle(d, (960, 380), 50, fill=0)
    text(d, (1290, 380), "planet", 84, anchor="lm")
    ox, oy = 260, 1180
    d.line([(ox, oy-260), (700, oy-260), (700, oy-160), (1100, oy-160), (1100, oy-260), (1600, oy-260)], fill=0, width=LW)
    text(d, (400, 850), "brightness", 72, bold=False, anchor="lm")
    text(d, (900, 1290), "a square bite: the planet is the dip, not a painting", 70, bold=False)
    save(im, "fig27.png")

# ---------------- Fig 28: habitable band ----------------
def fig28():
    im, d = canvas()
    c = (900, 675)
    # hatched annulus
    outer, inner = 560, 380
    poly_o = [(c[0]+outer*math.cos(math.radians(a)), c[1]+outer*math.sin(math.radians(a))) for a in range(0, 360, 3)]
    mask = Image.new("L", (W, H), 0); md = ImageDraw.Draw(mask)
    md.ellipse([c[0]-outer, c[1]-outer, c[0]+outer, c[1]+outer], fill=255)
    md.ellipse([c[0]-inner, c[1]-inner, c[0]+inner, c[1]+inner], fill=0)
    hatch = Image.new("L", (W, H), 255); hd = ImageDraw.Draw(hatch)
    for k in range(-H, W+H, 44): hd.line([(k, 0), (k+H, H)], fill=0, width=8)
    im.paste(hatch, (0, 0), mask)
    circle(d, c, outer, lw=LW); circle(d, c, inner, lw=LW)
    circle(d, c, 90, fill=0)
    text(d, (c[0], c[1]+170), "star", 72, bold=False)
    # Earth in band, Mars on rim
    e = (c[0]+470*math.cos(math.radians(160)), c[1]+470*math.sin(math.radians(160)))
    m = (c[0]+560*math.cos(math.radians(330)), c[1]+560*math.sin(math.radians(330)))
    circle(d, e, 40, fill=255, lw=LW); text(d, (300, 980), "Earth", 90)
    circle(d, m, 30, fill=255, lw=LW); text(d, (m[0]+60, m[1]-110), "Mars", 90)
    text(d, (900, 80), "where liquid water can last", 84)
    save(im, "fig28.png")

# ---------------- Fig 30: two trunks ----------------
def tree(d, base, h, dotted_style=False, label=None):
    x, y = base
    seg = [(x, y), (x, y-h*0.55)]
    br = [[(x, y-h*0.55), (x-260, y-h*0.95)], [(x, y-h*0.55), (x+240, y-h*0.98)],
          [(x, y-h*0.35), (x-330, y-h*0.62)], [(x, y-h*0.40), (x+330, y-h*0.70)]]
    if dotted_style:
        dotted(d, seg, lw=LW)
        for b in br: dotted(d, b, lw=LW)
    else:
        d.line(seg, fill=0, width=LW+8)
        for b in br: d.line(b, fill=0, width=LW)
    if label: text(d, (x, y+90), label, 110)

def fig30():
    im, d = canvas()
    d.line([(100, 1130), (1700, 1130)], fill=0, width=LW2)
    tree(d, (520, 1130), 900, label="Earth")
    tree(d, (1300, 1130), 900, dotted_style=True, label="?")
    text(d, (900, 80), "sample size: one", 90)
    save(im, "fig30.png")

# ---------------- Fig 33: handle on the block ----------------
def fig33():
    im, d = canvas()
    circle(d, (500, 675), 330, lw=LW); circle(d, (1300, 675), 330, lw=LW)
    d.rectangle([830, 585, 970, 765], outline=0, width=LW, fill=255)
    d.line([(830, 585), (970, 585)], fill=0, width=LW); d.line([(830, 765), (970, 765)], fill=0, width=LW)
    text(d, (500, 675), "here", 130); text(d, (1300, 675), "there", 130)
    text(d, (900, 1200), "a short, fat handle — and a bill", 84, bold=False)
    save(im, "fig33.png")

# ---------------- Fig 35: loop worldline ----------------
def fig35():
    im, d = canvas()
    pts = []
    for i in range(0, 361, 3):
        t = math.radians(i)
        pts.append((900 + 330*math.sin(t) + i*0.9, 1050 - i*2.3 + 120*math.sin(2*t)))
    # a path that comes back to meet itself
    path = [(700, 1200), (760, 980), (900, 860)] + \
           [(900+300*math.cos(math.radians(a)), 600-260*math.sin(math.radians(a))) for a in range(-90, 271, 4)] + \
           [(900, 860), (1000, 640), (1080, 300)]
    d.line(path, fill=0, width=LW)
    arrow(d, (1050, 430), (1080, 300), head=60)
    circle(d, (900, 860), 34, fill=0)
    text(d, (900, 130), "a worldline that meets itself", 88)
    text(d, (900, 1290), "same events — not a rewrite", 96)
    save(im, "fig35.png")

# ---------------- Fig 36: loaf in slices ----------------
def fig36():
    im, d = canvas()
    n, x0, y, w, h, dp, gap = 6, 200, 420, 150, 600, 120, 60
    for k in range(n):
        x = x0 + k*(w+gap)
        d.rectangle([x, y, x+w, y+h], outline=0, width=LW)
        d.line([(x, y), (x+dp, y-dp), (x+w+dp, y-dp), (x+w, y)], fill=0, width=LW)
        d.line([(x+w+dp, y-dp), (x+w+dp, y+h-dp), (x+w, y+h)], fill=0, width=LW)
    text(d, (900, 1220), "slices of when — no one walks between them", 80, bold=False)
    save(im, "fig36.png")

# ---------------- Fig 37: 2x2 ----------------
def fig37():
    im, d = canvas()
    labels = [("more space", 380, 400), ("other bubbles", 1420, 400), ("other branches", 380, 950), ("other math", 1420, 950)]
    for lab, cx, cy in labels:
        d.rectangle([cx-460, cy-230, cx+460, cy+230], outline=0, width=LW)
        text(d, (cx, cy), lab, 100)
    save(im, "fig37.png")

# ---------------- Fig 38: rooms receding ----------------
def fig38():
    im, d = canvas()
    cx, cy = 900, 620
    for k in range(7):
        s = 1.0 - k*0.13
        w, h = 1500*s, 1000*s
        d.rectangle([cx-w/2, cy-h/2, cx+w/2, cy+h/2], outline=0, width=max(6, int(LW*s)))
    for sx in (-1, 1):
        for sy in (-1, 1):
            d.line([(cx+sx*750, cy+sy*500), (cx+sx*750*0.22, cy+sy*500*0.22)], fill=0, width=LW2)
    text(d, (900, 1270), "identical rooms, receding — a possibility, not a photograph", 66, bold=False)
    save(im, "fig38.png")

# ---------------- Fig 39: three bubbles, three icons ----------------
def fig39():
    im, d = canvas()
    cs = [(420, 640), (900, 640), (1380, 640)]
    for c in cs: circle(d, c, 210, lw=LW)
    # icon 1: circle
    circle(d, cs[0], 80, lw=LW)
    # icon 2: triangle
    x, y = cs[1]; d.polygon([(x, y-95), (x-95, y+70), (x+95, y+70)], outline=0)
    d.line([(x, y-95), (x-95, y+70), (x+95, y+70), (x, y-95)], fill=0, width=LW)
    # icon 3: square
    x, y = cs[2]; d.rectangle([x-80, y-80, x+80, y+80], outline=0, width=LW)
    text(d, (900, 1100), "other rooms, other rules — unphotographed", 84, bold=False)
    save(im, "fig39.png")

# ---------------- Fig 40: a line that splits ----------------
def fig40():
    im, d = canvas()
    d.line([(200, 675), (760, 675)], fill=0, width=LW)
    d.line([(760, 675), (1600, 300)], fill=0, width=LW)
    d.line([(760, 675), (1600, 1050)], fill=0, width=LW)
    circle(d, (760, 675), 34, fill=0)
    text(d, (900, 1250), "two branches that never rejoin", 90)
    save(im, "fig40.png")

# ---------------- Fig 43: five endings ----------------
def fig43():
    im, d = canvas()
    rows = ["Freeze", "Rip", "Crunch", "Decay", "Bounce"]
    y0, dy = 200, 235
    for i, r in enumerate(rows):
        y = y0 + i*dy
        text(d, (330, y), r, 110, anchor="mm")
        x = 700
        if r == "Freeze":
            d.line([(x, y), (x+800, y)], fill=0, width=LW)
        elif r == "Rip":
            d.line([(x, y), (x+300, y), (x+340, y-70), (x+380, y+70), (x+420, y-70), (x+460, y+70), (x+500, y)], fill=0, width=LW)
            d.line([(x+560, y), (x+800, y)], fill=0, width=LW)
        elif r == "Crunch":
            d.line([(x, y-70), (x+800, y)], fill=0, width=LW); d.line([(x, y+70), (x+800, y)], fill=0, width=LW)
        elif r == "Decay":
            dotted(d, [(x, y), (x+800, y)], lw=LW, gap=60)
        else:
            d.line([(x, y-80), (x+400, y+80), (x+800, y-80)], fill=0, width=LW)
    save(im, "fig43.png")

# ---------------- Fig 44: clock dissolving ----------------
def fig44():
    im, d = canvas()
    clock(d, (430, 640), 320, 300, 60)
    arrow(d, (800, 640), (1000, 640), head=60)
    import random
    random.seed(3)
    for _ in range(70):
        x, y = random.randint(1080, 1700), random.randint(300, 1000)
        a = random.uniform(0, math.pi)
        d.line([(x-30*math.cos(a), y-30*math.sin(a)), (x+30*math.cos(a), y+30*math.sin(a))], fill=0, width=LW2)
    text(d, (900, 1230), "a clock is a habit of events, not a river", 80, bold=False)
    save(im, "fig44.png")

# ---------------- photo slots (placeholders until real photos land) ----------------
PHOTOS = {
    0: "A kitchen clock in a bright window, daylight outside",
    1: "Two people in a bright kitchen, one walking, one still",
    3: "The Sun, disk filling the frame (SOHO / SDO)",
    4: "Andromeda, cropped to the bright disk",
    8: "Deep-field crop: a handful of sharp galaxies",
    9: "The microwave sky in grayscale (Planck)",
    14: "One nearby spiral galaxy, disk filling the frame",
    16: "Galaxy survey map, thresholded so filaments read",
    17: "Bullet Cluster: X-ray gas above, mass contours below",
    18: "Supernova remnant with a bright rim",
    20: "EHT image of M87*, enlarged, contrast boosted",
    24: "Bright high-contrast host galaxy",
    25: "Perseverance or Curiosity, large in frame, hard daylight",
    29: "Europa, disk filling the frame; ice cracks read in gray",
    31: "A machine on bright dirt: the crew that can wait",
    32: "Svalbard Global Seed Vault door in snow",
    34: "A radio dish filling the frame, with ground",
    41: "Earthrise (Apollo 8) or DSCOVR full Earth",
    42: "Two or three finches on a light ground, beaks readable",
    45: "Rover tracks toward a near horizon",
}

def placeholder(n, desc):
    im, d = canvas()
    d.rectangle([40, 40, W-40, H-40], outline=0, width=8)
    d.rectangle([120, 120, W-120, H-120], outline=120, width=4)
    text(d, (900, 520), "PHOTO", 150, fill=110)
    text(d, (900, 690), f"Figure {n}", 100, fill=110)
    text(d, (900, 860), desc, 56, bold=False, fill=90)
    save(im, f"fig{n:02d}_slot.png")

if __name__ == "__main__":
    for fn in (fig02, fig05, fig06, fig07, fig10, fig11, fig12, fig13, fig15, fig19, fig21, fig22,
               fig23, fig26, fig27, fig28, fig30, fig33, fig35, fig36, fig37, fig38, fig39, fig40, fig43, fig44):
        fn()
    for n, desc in PHOTOS.items():
        placeholder(n, desc)
