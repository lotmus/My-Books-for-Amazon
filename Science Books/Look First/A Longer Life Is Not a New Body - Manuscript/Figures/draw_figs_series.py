# Diagrams for "A Permit Is Not a City" (figs_permit) and "The Body Keeps Its Own Clock" (figs_body).
# Same Kindle spec as draw_figs.py: 1800x1350, black on white, thick lines, big type.
import os, math, shutil
from PIL import Image, ImageDraw
from draw_figs import canvas, text, arrow, circle, dashed, dotted, W, H, LW, LW2, clock

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "figs_permit"); B = os.path.join(HERE, "figs_body")
os.makedirs(P, exist_ok=True); os.makedirs(B, exist_ok=True)

def save(im, folder, n):
    im.save(os.path.join(folder, f"fig{n:02d}.png"), optimize=True); print("wrote", folder[-6:], n)

def rect(d, box, lw=LW, fill=None): d.rectangle(box, outline=0, width=lw, fill=fill)
def hatch(im, box, spacing=46, lw=9, diag=1):
    mask = Image.new("L", (W, H), 0); ImageDraw.Draw(mask).rectangle(box, fill=255)
    h = Image.new("L", (W, H), 255); hd = ImageDraw.Draw(h)
    for k in range(-H, W+H, spacing):
        if diag > 0: hd.line([(k, 0), (k+H, H)], fill=0, width=lw)
        else: hd.line([(k, H), (k+H, 0)], fill=0, width=lw)
    im.paste(h, (0, 0), mask)
def xmark(d, c, r, lw=LW+6):
    d.line([(c[0]-r, c[1]-r), (c[0]+r, c[1]+r)], fill=0, width=lw); d.line([(c[0]-r, c[1]+r), (c[0]+r, c[1]-r)], fill=0, width=lw)
def rocket(d, cx, base_y, w, h, dotted_style=False):
    body = [(cx-w/2, base_y), (cx-w/2, base_y-h*0.75), (cx, base_y-h), (cx+w/2, base_y-h*0.75), (cx+w/2, base_y)]
    fins = [[(cx-w/2, base_y-h*0.25), (cx-w*0.85, base_y), (cx-w/2, base_y)], [(cx+w/2, base_y-h*0.25), (cx+w*0.85, base_y), (cx+w/2, base_y)]]
    if dotted_style:
        dotted(d, body + [body[0]], lw=LW-4); [dotted(d, f, lw=LW-4) for f in fins]
    else:
        d.line(body + [body[0]], fill=0, width=LW); [d.line(f, fill=0, width=LW) for f in fins]
def skyline(d, x0, x1, base_y, dotted_style=True):
    import random; random.seed(11); x = x0
    while x < x1:
        w = random.randint(90, 180); h = random.randint(200, 520)
        pts = [(x, base_y), (x, base_y-h), (x+w, base_y-h), (x+w, base_y)]
        if dotted_style: dotted(d, pts, lw=LW-6)
        else: d.line(pts, fill=0, width=LW)
        x += w + 30
def house(d, x, y, w, h):
    d.line([(x, y+h), (x, y+h*0.45), (x+w/2, y), (x+w, y+h*0.45), (x+w, y+h), (x, y+h)], fill=0, width=LW)
def door(d, x, y, w, h, state="closed", label=None, lw=LW):
    rect(d, (x, y, x+w, y+h), lw=lw)
    if state == "open": d.line([(x+w, y), (x+w+w*0.6, y-h*0.2), (x+w+w*0.6, y+h*0.8), (x+w, y+h)], fill=0, width=lw)
    if state == "stuck": xmark(d, (x+w/2, y+h/2), min(w, h)*0.3, lw=LW)
    if label: text(d, (x+w/2, y+h+70+(80 if state=="stagger" else 0)), label, 64)
def book(d, x, y, w, h, label):
    rect(d, (x, y, x+w, y+h)); d.line([(x+w*0.12, y), (x+w*0.12, y+h)], fill=0, width=LW2)
    for k in range(1, 5): d.line([(x+w*0.25, y+h*k/5), (x+w*0.85, y+h*k/5)], fill=0, width=LW2)
    text(d, (x+w/2, y+h+90), label, 90)
def pot(d, cx, cy, s=1.0):
    rect(d, (cx-120*s, cy-60*s, cx+120*s, cy+80*s)); d.line([(cx-150*s, cy-60*s), (cx+150*s, cy-60*s)], fill=0, width=LW)
    d.line([(cx-120*s, cy-90*s), (cx+120*s, cy-90*s)], fill=0, width=LW2)

# ============================ A PERMIT IS NOT A CITY ============================
def p01():
    im, d = canvas()
    # airlock door with lever handle
    rect(d, (180, 250, 780, 1000)); circle(d, (480, 620), 200, lw=LW); d.line([(480, 620), (620, 500)], fill=0, width=LW+8)
    text(d, (480, 1110), "airlock", 84, bold=False)
    # kitchen drawer with handle
    rect(d, (1000, 500, 1650, 760)); d.line([(1200, 630), (1450, 630)], fill=0, width=LW+8)
    text(d, (1325, 860), "drawer", 84, bold=False)
    d.line([(820, 620), (960, 620)], fill=0, width=LW2)
    text(d, (900, 1250), "dirt   ·   delay   ·   dates", 110)
    save(im, P, 1)
def p02():
    im, d = canvas()
    d.line([(100, 675), (1700, 675)], fill=0, width=LW2)
    rocket(d, 700, 600, 160, 480); text(d, (1000, 400), "flown stack", 90, anchor="lm")
    skyline(d, 160, 950, 1280, dotted_style=True); text(d, (1000, 1060), "rendering", 90, anchor="lm"); text(d, (1000, 1180), "cold", 90, anchor="lm", bold=False)
    save(im, P, 2)
def p03():
    im, d = canvas()
    y = 620; d.line([(120, y), (1680, y)], fill=0, width=LW)
    for x, lab in ((280, "weld"), (700, "shield"), (1120, "suit"), (1540, "vote")):
        d.line([(x, y-80), (x, y+80)], fill=0, width=LW); text(d, (x, y-190), lab, 100)
    text(d, (900, 260), "how a date slips", 90, bold=False)
    text(d, (900, 1050), "a slip is an invoice", 110)
    save(im, P, 3)
def p04():
    im, d = canvas()
    circle(d, (430, 675), 330, lw=LW); circle(d, (1420, 675), 120, lw=LW)
    text(d, (430, 675), "Earth", 100); text(d, (1420, 675), "Moon", 64)
    arrow(d, (790, 600), (1270, 600), head=60); text(d, (1030, 500), "~3 days", 90)
    arrow(d, (1270, 760), (790, 760), head=60); text(d, (1030, 870), "~1.3 s for light", 90)
    text(d, (900, 1230), "not to scale — but close is a fact, not a slogan", 66, bold=False)
    save(im, P, 4)
def p05():
    im, d = canvas()
    # capsule: dome + flat base
    d.arc([420, 350, 1080, 1010], 180, 360, fill=0, width=LW); d.line([(420, 680), (420, 900), (1080, 900), (1080, 680)], fill=0, width=LW)
    d.line([(100, 900), (1700, 900)], fill=0, width=LW2)
    d.line([(1350, 900), (1350, 380)], fill=0, width=LW); d.polygon([(1350, 380), (1620, 440), (1350, 500)], outline=0)
    d.line([(1350, 380), (1620, 440), (1350, 500)], fill=0, width=LW)
    text(d, (900, 1130), "flag  ≠  shift", 130)
    save(im, P, 5)
def p06():
    im, d = canvas()
    circle(d, (1150, 640), 260, lw=LW); text(d, (1150, 640), "Moon", 80)
    d.ellipse([650, 300, 1650, 980], outline=0, width=LW)
    rect(d, (615, 600, 705, 680), fill=255); text(d, (660, 860), "cabin", 60, bold=False)
    arrow(d, (600, 640), (250, 640), head=60); text(d, (400, 540), "home", 80); text(d, (400, 740), "days", 80, bold=False)
    text(d, (900, 1200), "sortie", 150)
    save(im, P, 6)
def p07():
    im, d = canvas()
    labs = ["refuel", "land", "leave", "suits"]
    for k, lab in enumerate(labs):
        x = 120 + k*410; rect(d, (x, 450, x+360, 850)); text(d, (x+180, 650), lab, 88)
    x = 120 + 3*410; text(d, (x+180, 960), "owed", 90); d.line([(x+40, 900), (x+320, 900)], fill=0, width=LW)
    text(d, (900, 230), "a landable year, four boxes", 84, bold=False)
    save(im, P, 7)
def p08():
    im, d = canvas()
    for x0, lab, walls in ((150, "orbit camp", [((150, 640), (600, 640)), ((450, 300), (450, 640))]),
                          (1000, "surface camp", [((1000, 500), (1300, 500)), ((1300, 500), (1300, 980)), ((1300, 760), (1650, 760))])):
        rect(d, (x0, 300, x0+650, 980))
        for a, b in walls: d.line([a, b], fill=0, width=LW)
        text(d, (x0+325, 1090), lab, 90)
    text(d, (900, 1250), "same tin, walls moved — architecture is a fight", 64, bold=False)
    save(im, P, 8)
def p09():
    im, d = canvas()
    book(d, 250, 300, 500, 640, "one flag"); book(d, 1050, 300, 500, 640, "other flag")
    text(d, (900, 150), "two ledgers, one gray dirt", 84, bold=False)
    save(im, P, 9)
def p10():
    im, d = canvas()
    rocket(d, 560, 1100, 260, 900); text(d, (560, 1230), "vehicle", 110)
    skyline(d, 1000, 1700, 1100, dotted_style=True); xmark(d, (1350, 850), 230, lw=LW+4); text(d, (1350, 1230), "city", 110)
    save(im, P, 10)
def p11():
    im, d = canvas()
    c = (900, 675); circle(d, c, 40, fill=0)
    d.ellipse([c[0]-330, c[1]-330, c[0]+330, c[1]+330], outline=0, width=LW)
    d.ellipse([c[0]-560, c[1]-450, c[0]+560, c[1]+450], outline=0, width=LW)
    d.arc([c[0]-450, c[1]-400, c[0]+450, c[1]+400], 200, 330, fill=0, width=LW2)
    text(d, (900, 1230), "window every ~26 months  ·  trip ~6–9 months", 72)
    circle(d, (c[0]+330, c[1]), 30, fill=0); circle(d, (c[0]-560, c[1]), 30, fill=0)
    text(d, (c[0]+330, c[1]+90), "Earth", 60, bold=False); text(d, (c[0]-560, c[1]+90), "Mars", 60, bold=False)
    save(im, P, 11)
def p12():
    im, d = canvas()
    for k, lab in enumerate(["SORTIE", "OUTPOST", "SETTLEMENT"]):
        y = 150 + k*400; rect(d, (400, y, 1400, y+280)); text(d, (900, y+140), lab, 110)
    d.line([(1400, 690), (1650, 690)], fill=0, width=LW+8); text(d, (1650, 600), "umbilical", 56, bold=False)
    save(im, P, 12)
def p13():
    im, d = canvas()
    rect(d, (120, 250, 1300, 1100)); rect(d, (250, 650, 700, 950)); rect(d, (820, 500, 1150, 700))
    text(d, (710, 400), "most of us", 110)
    d.polygon([(1550, 500), (1500, 640), (1600, 640)], outline=0); d.line([(1550, 500), (1500, 640), (1600, 640), (1550, 500)], fill=0, width=LW2)
    text(d, (1550, 760), "a village", 64)
    save(im, P, 13)
def p14():
    im, d = canvas()
    for k, lab in enumerate(["air", "ice", "plastics", "extinct"]):
        y = 250 + k*290; pot(d, 450, y, 0.9); text(d, (800, y), lab, 110, anchor="lm")
    save(im, P, 14)
def p15():
    im, d = canvas()
    rect(d, (300, 150, 420, 1000)); circle(d, (360, 1080), 130, lw=LW); d.line([(330, 560), (390, 560)], fill=0, width=LW+8)
    text(d, (560, 560), "no change", 70, anchor="lm", bold=False)
    d.polygon([(1250, 350), (1200, 500), (1300, 500)], outline=0); d.line([(1250, 350), (1200, 500), (1300, 500), (1250, 350)], fill=0, width=LW2)
    arrow(d, (1250, 600), (1250, 300), lw=LW2, head=40)
    text(d, (1250, 700), "a tiny ship leaves", 60, bold=False)
    text(d, (1000, 1000), "thousands  ≠  CO", 110); text(d, (1395, 1040), "2", 70)
    save(im, P, 15)

# ============================ THE BODY KEEPS ITS OWN CLOCK ============================
def b02():
    im, d = canvas()
    rect(d, (150, 350, 1650, 560)); hatch(im, (160, 360, 1640, 550), diag=1); text(d, (900, 260), "lifespan", 90)
    rect(d, (150, 800, 1250, 1010)); hatch(im, (160, 810, 1240, 1000), spacing=60, diag=-1); text(d, (700, 1110), "healthspan", 90)
    rect(d, (1250, 800, 1650, 1010)); text(d, (1450, 1110), "frail years", 66, bold=False)
    save(im, B, 2)
def b03():
    im, d = canvas()
    labs = ["DNA", "telomere", "mitochondria", "immune", "senescent", "brain"]
    for k, lab in enumerate(labs):
        cx, cy = 330 + (k % 3)*570, 330 + (k // 3)*520
        clock(d, (cx, cy), 150, 30*k+20, 60*k); text(d, (cx, cy+230), lab, 66)
    rect(d, (720, 1180, 1080, 1290)); d.line([(600, 1235), (720, 1235)], fill=0, width=LW2); d.line([(1080, 1235), (1200, 1235)], fill=0, width=LW2)
    xmark(d, (900, 1235), 90); text(d, (1320, 1235), "one fuse", 60, anchor="lm", bold=False)
    save(im, B, 3)
def b04():
    im, d = canvas()
    house(d, 250, 150, 1300, 900)
    door(d, 400, 720, 180, 300); door(d, 700, 720, 180, 300, "open"); door(d, 1150, 720, 180, 300)
    text(d, (790, 1200), "this tissue", 120)
    save(im, B, 4)
def b05():
    im, d = canvas()
    house(d, 250, 150, 1300, 900)
    door(d, 330, 720, 150, 300, "stuck"); text(d, (405, 1090), "cancer", 56)
    door(d, 610, 720, 150, 300, "stuck"); text(d, (685, 1170), "plumbing", 56)
    door(d, 890, 720, 150, 300, "stuck"); text(d, (965, 1090), "long goodbye", 56)
    door(d, 1200, 720, 150, 300, "open"); text(d, (1275, 1170), "unstuck", 56)
    save(im, B, 5)
def b06():
    im, d = canvas()
    rect(d, (200, 300, 1600, 500)); rect(d, (200, 300, 228, 500), fill=0); text(d, (900, 220), "share of body mass — brain about 2%", 70, bold=False)
    rect(d, (200, 800, 1600, 1000)); rect(d, (200, 800, 480, 1000), fill=0); text(d, (900, 720), "share of resting energy — brain about 20%", 70, bold=False)
    text(d, (900, 1200), "the organ you already use is expensive", 80)
    save(im, B, 6)
def b07():
    im, d = canvas()
    rect(d, (150, 500, 850, 1000)); d.arc([350, 380, 650, 620], 180, 360, fill=0, width=LW)
    for k, lab in enumerate(["book", "glasses", "hearing aid", "pill"]):
        text(d, (500, 600 + k*95), lab, 64, bold=False)
    text(d, (500, 1110), "tools with invoices", 66)
    rect(d, (1050, 400, 1650, 1000)); text(d, (1350, 500), "90%", 130); xmark(d, (1350, 790), 170, lw=LW+4)
    text(d, (1350, 1110), "the spare tank", 66)
    save(im, B, 7)
def b08():
    im, d = canvas()
    c = (900, 640); r = 380
    d.arc([c[0]-r, c[1]-r, c[0]+r, c[1]+r], 300, 660, fill=0, width=LW)
    arrow(d, (c[0]+r*math.cos(math.radians(298)), c[1]+r*math.sin(math.radians(298))), (c[0]+r*math.cos(math.radians(292)), c[1]+r*math.sin(math.radians(292))), head=70)
    for ang, lab in ((270, "want"), (0, "chase"), (90, "stamp"), (180, "want")):
        text(d, (c[0]+(r+150)*math.cos(math.radians(ang)), c[1]+(r+110)*math.sin(math.radians(ang))), lab, 96)
    d.line([(c[0]+r-10, c[1]-200), (c[0]+r+60, c[1]-200)], fill=0, width=LW2); text(d, (c[0]+r+320, c[1]-200), "more calendar", 56, bold=False)
    text(d, (900, 1250), "no switch on the loop", 80)
    save(im, B, 8)
def b09():
    im, d = canvas()
    x, y = 200, 1050; step = 300; rise = 190
    pts = [(x, y)]
    for k in range(4): pts += [(x + k*step, y - (k+1)*rise), (x + (k+1)*step, y - (k+1)*rise)]
    d.line(pts, fill=0, width=LW)
    for k, lab in enumerate(["vaccines", "sequence", "packets", "compute"]):
        text(d, (x + k*step + step/2 - (70 if k == 3 else 0), y - (k+1)*rise - 60), lab, 60)
    rect(d, (1330, 150, 1420, 1050), fill=0); text(d, (1450, 400), "energy", 60, anchor="lm"); text(d, (1450, 520), "war", 60, anchor="lm"); text(d, (1450, 640), "attention", 60, anchor="lm")
    text(d, (900, 1230), "a stair, not a ray — every riser meets a wall", 66, bold=False)
    save(im, B, 9)
def b10():
    im, d = canvas()
    ox, oy = 220, 1100; arrow(d, (ox, oy), (1650, oy), lw=LW2, head=44); arrow(d, (ox, oy), (ox, 200), lw=LW2, head=44)
    pts = [(ox + i*12, oy - 760/(1+math.exp(-(i-55)/9))) for i in range(0, 120)]
    d.line(pts, fill=0, width=LW)
    dashed(d, [(ox, oy), (ox+1300, oy-1000)], lw=LW)
    text(d, (450, 1000), "slow", 74); text(d, (1250, 850), "drunk middle", 74); text(d, (1560, 260), "wall", 74)
    text(d, (1150, 190), "not the kitchen", 60, bold=False)
    save(im, B, 10)
def b11():
    im, d = canvas()
    text(d, (900, 560), "10,000 / 50 = 200", 190); xmark(d, (900, 560), 330, lw=LW+10)
    text(d, (900, 1050), "arithmetic, not a method", 100)
    save(im, B, 11)
def b12():
    im, d = canvas()
    rect(d, (300, 500, 1100, 700)); d.line([(360, 700), (360, 900)], fill=0, width=LW); d.line([(1040, 700), (1040, 900)], fill=0, width=LW)
    for x in (420, 640, 860): rect(d, (x, 320, x+120, 430), lw=LW2)
    book(d, 1250, 380, 330, 420, "ledger")
    d.line([(300, 1080), (700, 1080)], fill=0, width=LW+8); d.line([(820, 1080), (1200, 1080)], fill=0, width=LW+8)
    text(d, (760, 1180), "snapped", 56, bold=False)
    text(d, (700, 200), "meeting", 130)
    save(im, B, 12)
def b13():
    im, d = canvas()
    rect(d, (450, 120, 1350, 1230)); text(d, (900, 230), "INVOICE", 80)
    for k, (lab, right) in enumerate((("trial", "years"), ("side effect", "some"), ("who pays", "you"))):
        y = 420 + k*200; text(d, (520, y), lab, 72, anchor="lm", bold=False); text(d, (1280, y), right, 72, anchor="rm", bold=False)
        d.line([(520, y+70), (1280, y+70)], fill=0, width=LW2)
    text(d, (520, 1080), "local fix", 80, anchor="lm"); text(d, (1280, 1080), "last line", 80, anchor="rm")
    save(im, B, 13)
def b14():
    im, d = canvas()
    pts = [(150, 1000), (400, 800), (650, 900), (900, 650), (1100, 720), (1250, 500)]
    d.line(pts, fill=0, width=LW+20); text(d, (500, 1150), "a practiced path", 66, bold=False)
    rect(d, (1350, 300, 1700, 800)); d.line([(1525, 300), (1525, 800)], fill=0, width=LW2); text(d, (1525, 900), "spare", 84); text(d, (1525, 1000), "(empty)", 56, bold=False)
    save(im, B, 14)
def b15():
    im, d = canvas()
    rect(d, (250, 250, 750, 1050))
    for k in range(3): rect(d, (290, 290 + k*260, 710, 500 + k*260), lw=LW2); d.line([(450, 395 + k*260), (550, 395 + k*260)], fill=0, width=LW2)
    text(d, (500, 1180), "file", 110)
    pts = [(1150, 1100), (1200, 900), (1350, 800), (1300, 600), (1450, 400), (1500, 200)]
    d.line(pts, fill=0, width=LW+10); text(d, (1350, 1180), "worldline", 110)
    save(im, B, 15)

def placeholder(folder, n, desc):
    im, d = canvas()
    rect(d, (40, 40, W-40, H-40), lw=8); rect(d, (120, 120, W-120, H-120), lw=4)
    text(d, (900, 520), "PHOTO", 150, fill=110); text(d, (900, 690), f"Figure {n}", 100, fill=110); text(d, (900, 860), desc, 56, bold=False, fill=90)
    im.save(os.path.join(folder, f"fig{n:02d}_slot.png"))

if __name__ == "__main__":
    for fn in (p01, p02, p03, p04, p05, p06, p07, p08, p09, p10, p11, p12, p13, p14, p15): fn()
    for fn in (b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12, b13, b14, b15): fn()
    placeholder(B, 1, "Working hands over a basil tray in hard light; a plain blister at the edge")
    placeholder(B, 16, "Basil, a pH notebook, the same hands; hard light")
    placeholder(P, 16, "Daylight Earth disk, high contrast")
    src = os.path.join(HERE, "figs", "fig41.jpg")
    if os.path.exists(src): shutil.copy(src, os.path.join(P, "fig16.jpg")); print("permit fig16 <- Earthrise")
