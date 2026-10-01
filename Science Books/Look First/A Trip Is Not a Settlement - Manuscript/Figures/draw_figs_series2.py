# Caption-driven revisions: the manuscript captions (newer than 00_Figure_Plan.md) win.
# Overrides selected figures from draw_figs_series.py and re-renders everything.
import math, os
import draw_figs_series as S
from draw_figs_series import canvas, text, arrow, circle, dashed, dotted, W, H, LW, LW2, rect, xmark, rocket, book, pot, house, door, save, P, B, placeholder, hatch

def figure(d, x, y, s=1.0, lw=LW2):
    circle(d, (x, y-70*s), 28*s, lw=lw); d.line([(x, y-42*s), (x, y+40*s)], fill=0, width=lw)
    d.line([(x-40*s, y+110*s), (x, y+40*s), (x+40*s, y+110*s)], fill=0, width=lw); d.line([(x-45*s, y-10*s), (x, y-25*s), (x+45*s, y-10*s)], fill=0, width=lw)
def lander(d, cx, base, w=360, h=200):
    rect(d, (cx-w/2, base-h-160, cx+w/2, base-160))
    for sx in (-1, 1): d.line([(cx+sx*w/2, base-160), (cx+sx*(w/2+120), base)], fill=0, width=LW); d.line([(cx+sx*(w/2+160), base), (cx+sx*(w/2+80), base)], fill=0, width=LW)
def flag(d, x, base, h=220):
    d.line([(x, base), (x, base-h)], fill=0, width=LW2); d.line([(x, base-h), (x+120, base-h+35), (x, base-h+70), (x, base-h)], fill=0, width=LW2)

# ---------------- A Trip Is Not a Settlement ----------------
def p01():
    im, d = canvas()
    rect(d, (150, 200, 700, 1000)); circle(d, (425, 560), 170); d.line([(425, 560), (540, 460)], fill=0, width=LW+8)
    text(d, (425, 1100), "airlock handle", 66, bold=False)
    # glove: mitten outline
    pts = [(900, 980), (900, 620), (960, 540), (1040, 560), (1060, 480), (1130, 470), (1140, 560), (1180, 560), (1180, 980)]
    d.line(pts + [pts[0]], fill=0, width=LW); text(d, (1040, 1100), "glove", 66, bold=False)
    circle(d, (1500, 600), 170); circle(d, (1500, 600), 100, lw=LW2)
    d.polygon([(1500, 430), (1560, 480), (1440, 480)], fill=0); text(d, (1500, 1100), "stuck seal", 66, bold=False)
    text(d, (900, 1250), "dirt and delay, not a downtown", 90)
    save(im, P, 1)
def p03():
    im, d = canvas()
    y = 620; d.line([(120, y), (1680, y)], fill=0, width=LW)
    for x, lab in ((330, "announced"), (900, "review"), (1470, "later year")):
        d.line([(x, y-90), (x, y+90)], fill=0, width=LW); text(d, (x, y-200), lab, 90)
    text(d, (900, 260), "how a date slips", 84, bold=False)
    text(d, (900, 1050), "invoice, not scandal", 110)
    save(im, P, 3)
def p05():
    im, d = canvas()
    d.arc([200, 300, 800, 900], 180, 360, fill=0, width=LW); d.line([(200, 600), (200, 860), (800, 860), (800, 600)], fill=0, width=LW)
    text(d, (500, 960), "sample capsule", 66, bold=False)
    lander(d, 1300, 860); text(d, (1300, 960), "small lander", 66, bold=False)
    d.line([(60, 860), (1740, 860)], fill=0, width=LW2)
    text(d, (900, 1160), "rock in a box is inventory", 96)
    save(im, P, 5)
def p06():
    im, d = canvas()
    d.ellipse([150, 250, 1650, 1000], outline=0, width=LW)
    circle(d, (520, 625), 90, lw=LW); text(d, (520, 625), "Earth", 50)
    circle(d, (1300, 625), 45, lw=LW); text(d, (1300, 720), "Moon", 50, bold=False)
    rect(d, (830, 210, 970, 290), fill=255)
    for k in range(3): circle(d, (860+k*40, 250), 10, fill=0)
    text(d, (900, 150), "seats occupied", 56, bold=False)
    text(d, (900, 1180), "sortie — a long loop, then home", 90)
    save(im, P, 6)
def p07():
    im, d = canvas()
    d.line([(60, 1000), (1740, 1000)], fill=0, width=LW2)
    lander(d, 700, 1000, w=520, h=260)
    for k in range(6): d.line([(1000, 620+k*64), (1090, 620+k*64)], fill=0, width=LW2)
    d.line([(1000, 600), (1000, 1000)], fill=0, width=LW2); d.line([(1090, 600), (1090, 1000)], fill=0, width=LW2)
    figure(d, 1250, 880, 1.1)
    text(d, (900, 1200), "attempt", 150)
    save(im, P, 7)
def p09():
    im, d = canvas()
    book(d, 250, 300, 500, 640, "precursors"); book(d, 1050, 300, 500, 640, "camp on paper")
    flag(d, 780, 300); flag(d, 1580, 300)
    text(d, (900, 1200), "two ledgers, one gray dirt", 84, bold=False)
    save(im, P, 9)
def p10():
    im, d = canvas()
    d.line([(60, 1050), (1740, 1050)], fill=0, width=LW2)
    rocket(d, 560, 1050, 260, 860); text(d, (560, 1180), "truck", 120)
    rect(d, (1000, 600, 1600, 1050)); text(d, (1300, 1180), "routine", 100, bold=False); text(d, (1300, 820), "(empty)", 60, bold=False)
    save(im, P, 10)
def p11():
    im, d = canvas()
    for k, lab in enumerate(["window", "EDL", "ISRU", "delay"]):
        text(d, (470 + (k % 2)*860, 330 + (k // 2)*380), lab, 140)
    rect(d, (150, 1120, 1650, 1180), fill=0); text(d, (900, 1260), "6 mbar — the thin air", 64, bold=False)
    save(im, P, 11)
def p12():
    im, d = canvas()
    for k, lab in enumerate(["SORTIE", "OUTPOST", "SETTLEMENT"]):
        y = 130 + k*420; rect(d, (400, y, 1400, y+260)); text(d, (900, y+130), lab, 110)
    for y in (390, 810):
        d.line([(900, y), (900, y+160)], fill=0, width=LW2); xmark(d, (900, y+80), 55, lw=LW)
    text(d, (1520, 470), "unfused", 56, bold=False)
    save(im, P, 12)
def p14():
    im, d = canvas()
    for k, (lab, n) in enumerate([("air", 1), ("ice", 2), ("plastics", 3), ("extinct", 4)]):
        y = 250 + k*290; pot(d, 450, y, 0.9)
        for j in range(n): x = 450 - 30*(n-1) + j*60; d.line([(x-18, y+140), (x, y+90), (x+18, y+140)], fill=0, width=LW2)
        text(d, (800, y), lab, 110, anchor="lm")
    save(im, P, 14)
def p15():
    im, d = canvas()
    c = (600, 800); r = 420
    d.arc([c[0]-r, c[1]-r, c[0]+r, c[1]+r], 200, 340, fill=0, width=LW); d.line([(c[0]-r*0.94, c[1]-r*0.34), (c[0]+r*0.94, c[1]-r*0.34)], fill=0, width=LW)
    d.line([c, (c[0], c[1]-r*0.9)], fill=0, width=LW+8); circle(d, c, 26, fill=0)
    text(d, (600, 1000), "the needle does not move", 60, bold=False)
    for k in range(3): figure(d, 1250 + k*110, 560, 0.9)
    arrow(d, (1240, 700), (1560, 700), lw=LW2, head=40); text(d, (1400, 800), "a tiny group steps off", 52, bold=False)
    text(d, (900, 1230), "headcount is not a thermostat", 90)
    save(im, P, 15)
def p16():
    im, d = canvas()
    d.line([(60, 1000), (1740, 1000)], fill=0, width=LW2)
    rect(d, (120, 940, 420, 1000), fill=0); rocket(d, 270, 940, 90, 280); text(d, (270, 1090), "pad", 66, bold=False)
    for x in (560, 820): d.line([(x, 1000), (x, 560)], fill=0, width=LW2); d.line([(x-50, 620), (x+50, 620)], fill=0, width=LW2)
    d.line([(510, 620), (870, 620)], fill=0, width=LW2); text(d, (690, 1090), "power line", 66, bold=False)
    d.line([(1000, 1000), (1080, 700), (1160, 1000)], fill=0, width=LW); rect(d, (1050, 1000, 1110, 1150)); text(d, (1080, 1230), "mine", 66, bold=False)
    rect(d, (1320, 560, 1700, 840)); text(d, (1510, 700), "spare", 90); text(d, (1510, 1090), "slide", 66, bold=False)
    text(d, (900, 200), "the bill of going is paid at home", 84)
    save(im, P, 16)

# ---------------- A Longer Life Is Not a New Body ----------------
def b09():
    im, d = canvas()
    x, y, step, rise = 180, 1050, 360, 200
    pts = [(x, y)]
    for k in range(4): pts += [(x + k*step, y - (k+1)*rise), (x + (k+1)*step, y - (k+1)*rise)]
    d.line(pts, fill=0, width=LW)
    for k, lab in enumerate(["vaccine", "sequence", "packet", "chip"]):
        text(d, (x + k*step + step/2 - 40, y - (k+1)*rise - 70), lab, 60)
        wx = x + (k+1)*step; rect(d, (wx-20, y - (k+1)*rise - 120, wx+20, y - (k+1)*rise), fill=0)
    text(d, (900, 1230), "a stair, not a ruler — a wall at the end of each flight", 62, bold=False)
    save(im, B, 9)
def b10():
    im, d = canvas()
    ox, oy = 220, 1100; arrow(d, (ox, oy), (1650, oy), lw=LW2, head=44); arrow(d, (ox, oy), (ox, 200), lw=LW2, head=44)
    pts = [(ox + i*12, oy - 760/(1+math.exp(-(i-55)/9))) for i in range(0, 120)]
    d.line(pts, fill=0, width=LW)
    dashed(d, [(ox, oy), (ox+1300, oy-1000)], lw=LW)
    text(d, (450, 1000), "start", 74); text(d, (1250, 850), "drunk middle", 74); text(d, (1560, 260), "wall", 74)
    text(d, (1150, 190), "not a rocket", 60, bold=False)
    save(im, B, 10)
def b12():
    im, d = canvas()
    rect(d, (150, 380, 700, 520)); d.line([(190, 520), (190, 680)], fill=0, width=LW); d.line([(660, 520), (660, 680)], fill=0, width=LW)
    for x in (230, 380, 530): rect(d, (x, 250, x+90, 330), lw=LW2)
    text(d, (425, 780), "table", 66, bold=False)
    book(d, 900, 300, 260, 340, "ledger")
    d.line([(1300, 700), (1500, 560)], fill=0, width=LW); d.line([(1600, 560), (1750, 700)], fill=0, width=LW); d.line([(1300, 700), (1300, 760)], fill=0, width=LW2); d.line([(1750, 700), (1750, 760)], fill=0, width=LW2)
    text(d, (1525, 780), "bridge", 66, bold=False)
    zig = [(150, 1080)] + [(150 + k*110, 1080 + (60 if k % 2 else -60)) for k in range(1, 15)]
    d.line(zig, fill=0, width=LW); text(d, (900, 1250), "front", 66, bold=False)
    text(d, (1300, 200), "four walls that are not chips", 66, bold=False)
    save(im, B, 12)
def b13():
    im, d = canvas()
    rect(d, (450, 120, 1350, 1230)); text(d, (900, 230), "RECEIPT", 80)
    for k, (lab, right) in enumerate((("trial", "years"), ("harm", "some"), ("zip code", "decides"))):
        y = 420 + k*200; text(d, (520, y), lab, 72, anchor="lm", bold=False); text(d, (1280, y), right, 72, anchor="rm", bold=False)
        d.line([(520, y+70), (1280, y+70)], fill=0, width=LW2)
    text(d, (520, 1080), "local fix", 80, anchor="lm"); text(d, (1280, 1080), "last line", 80, anchor="rm")
    save(im, B, 13)
def b14():
    im, d = canvas()
    xs = [300, 700, 1100, 1500]
    for k, x in enumerate(xs):
        if k == 2:
            dotted(d, [(x-100, 500), (x+100, 500), (x+100, 700), (x-100, 700), (x-100, 500)], lw=LW-4); text(d, (x, 800), "empty", 60, bold=False)
        else:
            rect(d, (x-100, 500, x+100, 700)); figure(d, x, 560, 1.0)
    arrow(d, (1000, 400), (760, 400), lw=LW2, head=44); arrow(d, (1200, 400), (1440, 400), lw=LW2, head=44)
    text(d, (1100, 300), "rerouted", 60, bold=False)
    text(d, (900, 1100), "overtime, not a hidden room", 96)
    save(im, B, 14)

if __name__ == "__main__":
    import draw_figs_series
    draw_figs_series.__dict__  # keep import
    # base set first
    for fn in (S.p01, S.p02, S.p03, S.p04, S.p05, S.p06, S.p07, S.p08, S.p09, S.p10, S.p11, S.p12, S.p13, S.p14, S.p15): fn()
    for fn in (S.b02, S.b03, S.b04, S.b05, S.b06, S.b07, S.b08, S.b09, S.b10, S.b11, S.b12, S.b13, S.b14, S.b15): fn()
    # overrides
    for fn in (p01, p03, p05, p06, p07, p09, p10, p11, p12, p14, p15, p16, b09, b10, b12, b13, b14): fn()
    placeholder(B, 1, "Working hands over a basil tray in hard light; a plain blister at the edge")
    placeholder(B, 16, "Basil, a pH notebook, the same hands; hard light")
    placeholder(P, 13, "A full Earth, bright, large in frame")
    old = os.path.join(P, "fig16.jpg")
    if os.path.exists(old): os.remove(old); print("removed stale fig16.jpg")
    old = os.path.join(P, "fig16_slot.png")
    if os.path.exists(old): os.remove(old)
