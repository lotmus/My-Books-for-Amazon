"""Front and back covers for EE Series Books 3-7, in the design of cover_book2.png.

Canvas 1600 x 2560 px (KDP Kindle ideal, 1:1.6), same as cover_book2.png.
Measured from cover_book2.png: gold band 0-169, title cap height 93 px with a
143 px line pitch, gold rule y 803-808 x 317-1282, subtitle caps 28 px at y 865,
"Book N of the / Electrical Engineering Series" at y 2217 / 2274, gold foot
band from y 2524. Back covers follow "book1 back cover.png" scaled to 1600 x 2560.

Fonts: Bahnschrift (title) and Segoe UI / Segoe UI Bold, as on Book 2.
Usage: python make_ee_covers.py OUTDIR [book numbers...]
Author: Lothar J. Musiol
"""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2560
NAVY_EDGE = (12, 28, 52)
NAVY_MID = (16, 36, 67)
GOLD = (215, 161, 59)
WHITE = (245, 247, 251)
BODY = (232, 236, 243)
MUTED = (159, 176, 200)
TRACE = (64, 78, 98)

FONTS = {
    'title': [r'C:\Windows\Fonts\bahnschrift.ttf',
              '/usr/share/fonts/truetype/sand-box/google/Barlow/Barlow-Medium.ttf'],
    'bold': [r'C:\Windows\Fonts\segoeuib.ttf',
             ('/usr/share/fonts/truetype/sand-box/google/Open Sans/OpenSans-VariableFont_wdth,wght.ttf', b'Bold')],
    'reg': [r'C:\Windows\Fonts\segoeui.ttf',
            ('/usr/share/fonts/truetype/sand-box/google/Open Sans/OpenSans-VariableFont_wdth,wght.ttf', b'Regular')],
}

SERIES = 'ELECTRICAL ENGINEERING SERIES'
SERIES_MIXED = 'Electrical Engineering Series'

BOOKS = {
    3: dict(title=['SEMICONDUCTOR', 'PHYSICS AND', 'DEVICES'],
            tags='CARRIERS · JUNCTIONS · TRANSISTORS',
            accent=(96, 190, 204), motif='semi',
            back=[
                "Why does a diode \u201cturn on\u201d at 0.7 V, and why is that a useful sketch but a bad physical claim? This book opens the blocks that Book 2 dropped into schematics and explains, with numbers, why devices behave the way their data sheets say.",
                "It starts with the silicon crystal, doping, and the pn junction, then the diode you can actually buy, and on to GaAs, GaN, and InP. From there: the bipolar transistor, the MOSFET from the capacitor up to FinFET and gate-all-around, an op-amp built from its own transistors, CMOS as a chip, LEDs and power devices, and finally how a transistor is made and modeled.",
                "Twenty-two chapters. More than 80 worked examples. Over 150 practice problems, every answer in the back of the book.",
            ]),
    4: dict(title=['RF, MICROWAVE,', 'AND TRANSCEIVERS'],
            tags='LINES · ANTENNAS · THE ACTIVE RADIO',
            accent=(232, 122, 98), motif='rf',
            back=[
                "This book follows a radio from the copper to the air.",
                "Part I is the passive structure: transmission lines, the Smith chart, S-parameters, filters, cavities, antennas and arrays, couplers, circulators, and propagation. Part II is the active radio: load lines, amplifier classes and the Doherty, receiver noise, the LNA, mixers, the PLL and synthesizers, radar, the link budget, and digital predistortion.",
                "The last chapter sets the power amplifier classes side by side and shows how envelope tracking and supply modulation raise average efficiency with real OFDM signals.",
                "Forty-one chapters, from 1 GHz to millimeter wave. More than 120 worked examples, every practice answer in the back of the book.",
            ]),
    5: dict(title=['COMMUNICATIONS,', 'WIRELESS, AND SDR'],
            tags='MODULATION · OFDM · MIMO · SDR',
            accent=(112, 172, 236), motif='comms',
            back=[
                "How many bits can a radio channel carry, and how does a receiver written largely in software pull them back out of noise, echoes, and Doppler? This book answers with numbers, from Shannon's limit to a sensor on a coin cell.",
                "Part I builds a complete link: modulation, sampling and complex baseband, pulse shaping, constellations and EVM, fading, OFDM, coding, MIMO, and the SDR hardware you can buy. Part II opens the modem: filters, synchronization, equalization, pilots, and scheduling. Part III applies it to positioning, massive MIMO, cellular interference, satellites, and IoT radios.",
                "Twenty-one chapters. More than 120 worked examples. Over 200 practice problems, every answer in the back of the book.",
            ]),
    6: dict(title=['POWER AND', 'ENERGY'],
            tags='CONVERTERS · MAGNETICS · THE GRID',
            accent=(238, 128, 66), motif='power',
            back=[
                "Every conversion wastes power. This book follows electrical energy from the grid to the processor and the battery, and shows, with numbers, where each watt goes and how to keep it.",
                "Part I builds the converters: linear regulators, buck, boost, flyback, and LLC, magnetics, power-factor correction, and high voltage. Part II goes inside: losses, loop compensation, light load, batteries, and motor drives. Part III covers the data center, UPS, and the grid. Part IV treats multiphase regulators, gate drivers, pulsed power, solar MPPT, and wireless power.",
                "Twenty-two chapters. More than 120 worked examples. Nearly 200 practice problems, every answer in the back of the book.",
            ]),
    7: dict(title=['PACKAGING, LAYOUT,', 'EMC, AND TEST'],
            tags='PACKAGES · BOARDS · EMC · TEST',
            accent=(110, 192, 134), motif='pkg',
            back=[
                "This is where the series meets the physical product.",
                "Part I covers packages, chiplets, and HBM, power delivery at 875 amperes, board materials and stack-up, decoupling, crosstalk, loss and the eye, optical interconnect, heat, MEMS, reliability, antenna-in-package, design for test, and TDR and VNA measurement. Part II covers EMC: why boards and cables radiate, limits and detectors, chambers and LISNs, filters, immunity, and the day in the lab.",
                "The book closes with a robot that uses nearly every book in the series at once. Twenty-nine chapters, 110 worked examples, and 221 practice problems, every answer in the back of the book.",
            ]),
}


# ---------------------------------------------------------------- fonts
def _load(kind, size):
    for c in FONTS[kind]:
        path, var = (c if isinstance(c, tuple) else (c, None))
        if os.path.exists(path):
            f = ImageFont.truetype(path, size)
            if var:
                try:
                    f.set_variation_by_name(var)
                except Exception:
                    pass
            return f
    raise FileNotFoundError(kind)


def font_for_cap(kind, cap):
    best = None
    for s in range(8, 400):
        f = _load(kind, s)
        b = f.getbbox('H')
        h = b[3] - b[1]
        if best is None or abs(h - cap) < best[0]:
            best = (abs(h - cap), s)
        if h > cap:
            break
    return _load(kind, best[1])


def tracked_width(font, text, track):
    return sum(font.getlength(ch) for ch in text) + track * (len(text) - 1)


def track_for(font, text, target):
    nat = tracked_width(font, text, 0)
    return (target - nat) / (len(text) - 1)


def draw_tracked(d, font, text, cx, cap_top, track, fill):
    """Center text on cx with its cap top (top of 'H') at cap_top."""
    w = tracked_width(font, text, track)
    x = cx - w / 2
    y = cap_top - font.getbbox('H')[1]
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + track
    return w


# ---------------------------------------------------------------- line art
class Art:
    """Supersampled RGBA layer for a region; motif coordinates can be
    mapped (scaled about a source centre to a destination centre)."""

    def __init__(self, box, S=2):
        self.x0, self.y0, self.x1, self.y1 = box
        self.S = S
        self.im = Image.new('RGBA', ((self.x1 - self.x0) * S, (self.y1 - self.y0) * S), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.im)
        self.map = (0, 0, 1.0, 0, 0)

    def set_map(self, src, dst, k):
        self.map = (src[0], src[1], k, dst[0], dst[1])

    def P(self, x, y):
        sx, sy, k, dx, dy = self.map
        if k != 1.0 or sx or dx:
            x, y = dx + (x - sx) * k, dy + (y - sy) * k
        return ((x - self.x0) * self.S, (y - self.y0) * self.S)

    def w(self, w):
        return max(1, int(round(w * self.S * max(self.map[2], 0.55))))

    def rgba(self, col, a):
        return tuple(col) + (int(255 * a),)

    def line(self, pts, col=GOLD, w=4, a=0.85):
        self.d.line([self.P(*p) for p in pts], fill=self.rgba(col, a), width=self.w(w), joint='curve')

    def circle(self, cx, cy, r, col=GOLD, w=4, a=0.85, fill=None):
        k = self.map[2]
        x, y = self.P(cx, cy)
        R = r * self.S * k
        self.d.ellipse((x - R, y - R, x + R, y + R),
                       fill=None if fill is None else self.rgba(fill, a),
                       outline=None if w == 0 else self.rgba(col, a),
                       width=0 if w == 0 else self.w(w))

    def rect(self, x0, y0, x1, y1, col=GOLD, w=4, a=0.85, fill=None):
        p0, p1 = self.P(x0, y0), self.P(x1, y1)
        self.d.rectangle((p0, p1), outline=self.rgba(col, a), width=self.w(w),
                         fill=None if fill is None else self.rgba(fill, a))

    def poly(self, pts, col=GOLD, w=4, a=0.85, fill=None):
        self.d.polygon([self.P(*p) for p in pts], outline=self.rgba(col, a),
                       fill=None if fill is None else self.rgba(fill, a), width=self.w(w))

    def compose(self, base):
        small = self.im.resize((self.x1 - self.x0, self.y1 - self.y0), Image.LANCZOS)
        base.alpha_composite(small, (self.x0, self.y0))


# components (horizontal, signal flows left to right)
def zigzag(A, x0, x1, y, amp=13, n=6, **kw):
    pts = [(x0, y)]
    step = (x1 - x0) / (n * 2)
    for i in range(1, n * 2):
        pts.append((x0 + i * step, y + (amp if i % 2 else -amp) * (1 if (i // 2) % 2 == 0 else 1) * (1 if i % 2 else 1)))
    pts = [(x0, y)] + [(x0 + (i + 0.5) * (x1 - x0) / (2 * n), y - amp if i % 2 == 0 else y + amp) for i in range(2 * n)] + [(x1, y)]
    A.line(pts, **kw)


def zigzag_v(A, x, y0, y1, amp=13, n=6, **kw):
    pts = [(x, y0)] + [(x - amp if i % 2 == 0 else x + amp, y0 + (i + 0.5) * (y1 - y0) / (2 * n)) for i in range(2 * n)] + [(x, y1)]
    A.line(pts, **kw)


def coil(A, x0, x1, y, loops=4, **kw):
    r = (x1 - x0) / loops / 2
    for i in range(loops):
        cx = x0 + r + i * 2 * r
        pts = [(cx + r * math.cos(t), y - r * math.sin(t)) for t in [math.pi - j * math.pi / 24 for j in range(25)]]
        A.line(pts, **kw)


def cap_v(A, x, y, gap=10, half=26, **kw):
    """capacitor across a horizontal wire at x (plates vertical)"""
    A.line([(x - gap, y - half), (x - gap, y + half)], **kw)
    A.line([(x + gap, y - half), (x + gap, y + half)], **kw)


def cap_h(A, x, y, gap=10, half=26, **kw):
    """capacitor in a vertical wire at y (plates horizontal)"""
    A.line([(x - half, y - gap), (x + half, y - gap)], **kw)
    A.line([(x - half, y + gap), (x + half, y + gap)], **kw)


def diode(A, x, y, s=26, **kw):
    A.poly([(x - s, y - s), (x - s, y + s), (x + s * 0.9, y)], **kw)
    A.line([(x + s * 0.9, y - s), (x + s * 0.9, y + s)], **kw)


def diode_up(A, x, y, s=24, **kw):
    """vertical diode, cathode at top"""
    A.poly([(x - s, y + s), (x + s, y + s), (x, y - s * 0.9)], **kw)
    A.line([(x - s, y - s * 0.9), (x + s, y - s * 0.9)], **kw)


def amp(A, x0, y, w=80, h=72, **kw):
    A.poly([(x0, y - h), (x0, y + h), (x0 + w * 1.15, y)], **kw)


def ground(A, x, y, **kw):
    for i, hw in enumerate((26, 17, 8)):
        A.line([(x - hw, y + i * 10), (x + hw, y + i * 10)], **kw)


def arrow_end(A, x, y, **kw):
    A.line([(x - 18, y - 8), (x, y), (x - 18, y + 8)], **kw)


def node(A, x, y, r=6, col=GOLD, a=0.85):
    A.circle(x, y, r, col=col, w=0, a=a, fill=col)


def traces(A, rng, rows, x0=55, x1=1545, stop=None):
    """faint PCB-like traces with gold resistor zigzags, as on Books 1-2"""
    for i, y in enumerate(rows):
        xe = x1 if stop is None or stop[i] is None else stop[i]
        A.line([(x0, y), (xe, y)], col=TRACE, w=3, a=0.9)
        node(A, x0, y, 5, TRACE, 0.9)
        node(A, xe, y, 5, TRACE, 0.9)
        third = (xe - x0 - 300) / 3
        slot = rng.choice((0, 1, 2))
        for zx in [x0 + 150 + slot * third + rng.uniform(0, third - 130)]:
            A.line([(zx - 6, y), (zx + 128, y)], col=NAVY_MID, w=6, a=1.0)
            zigzag(A, zx, zx + 120, y, amp=11, n=5, col=GOLD, w=3, a=0.6)


# ---------------------------------------------------------------- motifs
# All motifs are drawn around the band y ~ 1150-1560, centre (800, 1360).
def motif_semi(A, acc):
    # equilibrium pn-junction band diagram
    def ec(x):
        return 1150 + 95 * (0.5 + 0.5 * math.tanh((x - 800) / 70))
    xs = [380 + i * 4 for i in range(211)]
    A.line([(x, ec(x)) for x in xs], w=4)
    A.line([(x, ec(x) + 150) for x in xs], w=4)
    for x in range(380, 1220, 34):  # dashed Fermi level
        A.line([(x, 1267), (min(x + 18, 1220), 1267)], w=3, a=0.7)
    rng = random.Random(3)
    for _ in range(14):  # electrons above Ec on the n side
        x = rng.uniform(900, 1200)
        node(A, x, ec(x) - rng.uniform(14, 34), 7, acc, 0.95)
    for _ in range(14):  # holes below Ev on the p side
        x = rng.uniform(390, 690)
        A.circle(x, ec(x) + 150 + rng.uniform(14, 34), 7, col=acc, w=3, a=0.95)
    # device row: diode -> MOSFET
    y = 1540
    A.line([(250, y), (520, y)], w=4)
    diode(A, 548, y)
    A.line([(572, y), (840, y)], w=4)
    A.line([(840, y - 40), (840, y + 40)], w=4)          # gate plate
    for yy in (y - 44, y - 10, y + 24):                  # channel segments
        A.line([(862, yy), (862, yy + 22)], w=4)
    A.line([(862, y - 33), (930, y - 33), (930, y - 70)], w=4)   # drain
    A.line([(862, y + 35), (930, y + 35), (930, y + 70)], w=4)   # source
    A.line([(862, y), (896, y)], w=4)
    ground(A, 930, y + 70, w=4)
    A.line([(930, y - 70), (1350, y - 70)], w=4)
    arrow_end(A, 1350, y - 70, w=4)


def motif_rf(A, acc):
    cx, cy, R = 560, 1350, 205
    A.circle(cx, cy, R, w=4)
    A.line([(cx - R, cy), (cx + R, cy)], w=3, a=0.7)
    for r in (0.33, 1.0, 3.0):
        A.circle(cx + R * r / (1 + r), cy, R / (1 + r), w=3, a=0.7)
    for xv in (0.5, 1.0, 2.0, -0.5, -1.0, -2.0):
        c = (1.0, 1.0 / xv)
        rad = 1.0 / abs(xv)
        pts = []
        for i in range(721):
            t = i * math.pi / 360
            u, v = c[0] + rad * math.cos(t), c[1] + rad * math.sin(t)
            if u * u + v * v <= 1.0005:
                pts.append((cx + R * u, cy - R * v))
            elif len(pts) > 1:
                A.line(pts, w=3, a=0.7)
                pts = []
            else:
                pts = []
        if len(pts) > 1:
            A.line(pts, w=3, a=0.7)
    node(A, cx + R * 0.2, cy - R * 0.38, 9, acc, 0.95)   # a matched point
    A.line([(150, cy), (cx - R, cy)], w=4)
    zigzag(A, 220, 320, cy, col=GOLD, w=4, a=0.85)
    A.line([(cx + R, cy), (860, cy)], w=4)
    amp(A, 860, cy)
    A.line([(952, cy), (1150, cy), (1150, 1190)], w=4)
    A.line([(1110, 1150), (1150, 1190), (1190, 1150)], w=4)
    for r in (45, 85, 125, 165):
        A.d.arc(None or (A.P(1150 - r, 1190 - r) + A.P(1150 + r, 1190 + r)), -50, 50, fill=A.rgba(acc, 0.9), width=A.w(4))
        A.d.arc(A.P(1150 - r, 1190 - r) + A.P(1150 + r, 1190 + r), 130, 230, fill=A.rgba(acc, 0.9), width=A.w(4))


def motif_comms(A, acc):
    cx, cy = 520, 1350
    A.line([(cx - 200, cy), (cx + 200, cy)], w=3, a=0.7)
    A.line([(cx, cy - 200), (cx, cy + 200)], w=3, a=0.7)
    arrow_end(A, cx + 200, cy, w=3, a=0.7)
    for i in (-3, -1, 1, 3):
        for j in (-3, -1, 1, 3):
            node(A, cx + i * 50, cy + j * 50, 10, acc, 0.95)
    A.circle(cx + 50, cy - 150, 20, w=3)       # one symbol picked out
    rng = random.Random(5)
    for _ in range(26):                          # noisy received samples
        i, j = rng.choice((-3, -1, 1, 3)), rng.choice((-3, -1, 1, 3))
        node(A, cx + i * 50 + rng.gauss(0, 9), cy + j * 50 + rng.gauss(0, 9), 3, GOLD, 0.7)
    # OFDM subcarriers
    base = 1460
    A.line([(780, base), (1440, base)], w=3, a=0.7)
    for k in range(7):
        fc = 900 + k * 70
        pts = []
        for i in range(-61, 62):
            x = fc + i * 2
            u = (x - fc) / 70.0
            s = 1.0 if abs(u) < 1e-9 else math.sin(math.pi * u) / (math.pi * u)
            pts.append((x, base - 230 * s))
        A.line(pts, col=(acc if k % 2 else GOLD), w=3, a=0.9)


def motif_power(A, acc):
    top, gnd = 1300, 1470
    A.circle(300, (top + gnd) / 2, 46, w=4)
    A.line([(282, 1385), (318, 1385)], w=3); A.line([(300, 1367), (300, 1403)], w=3)
    A.line([(282, 1425), (318, 1425)], w=3) if False else None
    A.line([(300, (top + gnd) / 2 - 46), (300, top), (470, top)], w=4)
    node(A, 470, top); A.line([(474, top), (556, top - 44)], w=4); node(A, 560, top)   # switch
    A.line([(560, top), (720, top)], w=4)
    node(A, 640, top)
    A.line([(640, top), (640, 1360)], w=4); diode_up(A, 640, 1384); A.line([(640, 1408), (640, gnd)], w=4)
    coil(A, 720, 880, top, loops=4, w=4)
    A.line([(880, top), (1180, top)], w=4)
    node(A, 960, top)
    A.line([(960, top), (960, 1375)], w=4); cap_h(A, 960, 1385); A.line([(960, 1395), (960, gnd)], w=4)
    A.line([(1180, top), (1180, 1330)], w=4); zigzag_v(A, 1180, 1330, 1440, w=4); A.line([(1180, 1440), (1180, gnd)], w=4)
    A.line([(300, (top + gnd) / 2 + 46), (300, gnd), (1180, gnd)], w=4)
    ground(A, 740, gnd, w=4)
    # waveforms: switch node square wave -> filtered DC with ripple
    y0, y1 = 1210, 1150
    pts = []
    x = 420
    while x < 700:
        pts += [(x, y0), (x, y1), (x + 40, y1), (x + 40, y0), (x + 70, y0)]
        x += 70
    A.line(pts, col=acc, w=3, a=0.95)
    A.line([(890 + i * 4, 1180 + 6 * math.sin(i * 4 / 70 * 2 * math.pi)) for i in range(80)], col=acc, w=3, a=0.95)
    arrow_end(A, 1215, 1180, col=acc, w=3, a=0.95)
    A.line([(1215, 1180), (1250, 1180)], col=acc, w=3, a=0.95) if False else None


def motif_pkg(A, acc):
    # package cross-section: lid, die, micro-bumps, substrate, BGA, board
    A.line([(400, 1355), (400, 1250), (720, 1250), (720, 1355)], w=4)
    A.rect(450, 1285, 670, 1325, w=4)
    for x in range(465, 660, 24):
        node(A, x, 1336, 6, GOLD, 0.85)
    A.rect(330, 1347, 790, 1380, w=4)
    for x in range(355, 780, 48):
        A.circle(x, 1398, 15, col=acc, w=4, a=0.95)
    A.rect(260, 1416, 860, 1450, w=4)
    for x in range(290, 840, 60):
        A.line([(x, 1433), (x + 30, 1433)], w=2, a=0.6)
    # eye diagram: one unit interval, crossings at both edges
    ex0, ex1, ym, ah = 960, 1380, 1340, 95
    rng = random.Random(7)
    def ramp(u):
        return 0.5 - 0.5 * math.cos(math.pi * min(1.0, max(0.0, u)))
    def level(t, a, b, c):
        if t < 0.3:
            return a + (b - a) * ramp((t + 0.3) / 0.6)
        return b + (c - b) * ramp((t - 0.7) / 0.6)
    for a_ in (-1, 1):
        for b_ in (-1, 1):
            for c_ in (-1, 1):
                for _ in range(2):
                    j = rng.uniform(-0.02, 0.02)
                    pts = []
                    for i in range(0, 161):
                        t = -0.3 + i / 160 * 1.6
                        pts.append((ex0 + (t + 0.3) / 1.6 * (ex1 - ex0), ym - ah * level(t + j, a_, b_, c_) + rng.uniform(-0.6, 0.6)))
                    A.line(pts, col=acc, w=3, a=0.8)
    A.line([(860, 1433), (910, 1433), (910, ym), (ex0, ym)], w=4)


MOTIFS = dict(semi=motif_semi, rf=motif_rf, comms=motif_comms, power=motif_power, pkg=motif_pkg)


# ---------------------------------------------------------------- canvases
def background():
    col = Image.new('RGB', (1, H))
    for y in range(H):
        t = math.sin(math.pi * y / H) ** 1.5
        col.putpixel((0, y), tuple(int(round(NAVY_EDGE[i] + (NAVY_MID[i] - NAVY_EDGE[i]) * t)) for i in range(3)))
    return col.resize((W, H)).convert('RGBA')


def band_text(d, n, band_h):
    f = font_for_cap('bold', 28)
    tr = track_for(f, SERIES + ' · BOOK 02', 1232)
    draw_tracked(d, f, f'{SERIES} · BOOK {n:02d}', W / 2, 67, tr, NAVY_EDGE)


def front(n, b):
    im = background()
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W - 1, 169), fill=GOLD)
    band_text(d, n, 170)
    d.rectangle((0, 2524, W - 1, H - 1), fill=GOLD)

    # title, calibrated to Book 2 (cap 93 px, "AND COMPONENTS" 1101 px wide)
    tf = font_for_cap('title', 93)
    ttr = track_for(tf, 'AND COMPONENTS', 1101)
    lines = b['title']
    widest = max(tracked_width(tf, s, ttr) for s in lines)
    cap, pitch = 93, 143
    if widest > 1340:
        k = 1340 / widest
        cap, pitch = int(93 * k), int(143 * k)
        tf = font_for_cap('title', cap)
        ttr = ttr * k
    block = cap + pitch * (len(lines) - 1)
    top = int(511.5 - block / 2)
    if len(lines) > 2:
        top = max(top, 300)
    for i, s in enumerate(lines):
        draw_tracked(d, tf, s, W / 2, top + i * pitch, ttr, WHITE)

    d.rectangle((317, 803, 1282, 808), fill=GOLD)
    sf = font_for_cap('bold', 28)
    s_tr = track_for(sf, 'ANALOG · DIGITAL · REAL COMPONENTS', 750)
    draw_tracked(d, sf, b['tags'], W / 2, 865, s_tr, GOLD)

    rng = random.Random(100 + n)
    A = Art((0, 880, W, 1800))
    traces(A, rng, [915, 940, 985])
    traces(A, rng, [1665, 1732, 1760])
    MOTIFS[b['motif']](A, b['accent'])
    A.compose(im)

    rf = _load('reg', 46)
    k = 571 / rf.getlength(SERIES_MIXED)
    rf = _load('reg', max(10, int(round(46 * k))))
    for text, yt in ((f'Book {n} of the', 2217), (SERIES_MIXED, 2274)):
        bb = d.textbbox((0, 0), text, font=rf)
        d.text((W / 2 - (bb[2] - bb[0]) / 2 - bb[0], yt - bb[1]), text, font=rf, fill=MUTED)
    return im.convert('RGB')


def wrap(d, font, text, width):
    words, lines, cur = text.split(), [], []
    for w_ in words:
        trial = ' '.join(cur + [w_])
        if cur and d.textlength(trial, font=font) > width:
            lines.append(cur)
            cur = [w_]
        else:
            cur.append(w_)
    if cur:
        lines.append(cur)
    return lines


def back(n, b):
    im = background()
    d = ImageDraw.Draw(im)
    band_h = 122
    d.rectangle((0, 0, W - 1, band_h - 1), fill=GOLD)
    f = font_for_cap('bold', 28)
    tr = track_for(f, SERIES + ' · BOOK 02', 1232)
    draw_tracked(d, f, f'{SERIES} · BOOK {n:02d}', W / 2, band_h / 2 - 14, tr, NAVY_EDGE)

    # top decoration: the front motif, small and faint, plus the series wave
    A = Art((0, band_h, W, 660))
    A.set_map((800, 1360), (430, 360), 0.5)
    MOTIFS[b['motif']](A, b['accent'])
    A.set_map((0, 0), (0, 0), 1.0)
    A.map = (0, 0, 1.0, 0, 0)
    pts = [(x, 470 - 110 * math.sin((x - 120) / 1480 * 2 * math.pi * 0.75 + 0.3)) for x in range(0, W + 1, 8)]
    A.line(pts, col=GOLD, w=4, a=0.55)
    A.compose(im)

    # blurb, justified, auto-fit between y 700 and 1880
    x0, width, y_top, y_max = 265, 1070, 700, 1880
    for size in range(46, 33, -1):
        bf = _load('reg', size)
        pitch = int(size * 1.56)
        paras = [wrap(d, bf, p, width) for p in b['back']]
        total = sum(len(p) for p in paras) * pitch + (len(paras) - 1) * int(pitch * 0.62)
        if y_top + total <= y_max:
            break
    y = y_top + max(0, (y_max - y_top - total) // 3)
    for p in paras:
        for li, words in enumerate(p):
            last = li == len(p) - 1
            wsum = sum(d.textlength(w_, font=bf) for w_ in words)
            gap = (width - wsum) / max(1, len(words) - 1)
            if last or len(words) == 1 or gap > 2.2 * d.textlength(' ', font=bf):
                d.text((x0, y), ' '.join(words), font=bf, fill=BODY)
            else:
                x = x0
                for w_ in words:
                    d.text((x, y), w_, font=bf, fill=BODY)
                    x += d.textlength(w_, font=bf) + gap
            y += pitch
        y += int(pitch * 0.62)

    d.rectangle((480, 1940, 1090, 1945), fill=GOLD)
    mf = _load('reg', 40)
    for text, yt in ((f'Book {n} of 7 in the', 2005), (SERIES_MIXED, 2057)):
        bb = d.textbbox((0, 0), text, font=mf)
        d.text((785 - (bb[2] - bb[0]) / 2 - bb[0], yt - bb[1]), text, font=mf, fill=MUTED)
    A = Art((0, 2100, W, H))
    oy = 2137
    A.line([(612, oy), (680, oy)], w=4)
    A.line([(890, oy), (958, oy)], w=4)
    for cx in (720, 785, 850):
        A.rect(cx - 13, oy - 13, cx + 13, oy + 13, w=4)
    rng = random.Random(200 + n)
    traces(A, rng, [2207, 2262, 2320, 2375], stop=[None, None, 1090, 1090])
    A.compose(im)
    d.rectangle((1133, 2307, 1567, 2532), fill=(255, 255, 255))   # barcode area, as on Book 1
    return im.convert('RGB')


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    nums = [int(a) for a in sys.argv[2:]] or sorted(BOOKS)
    for n in nums:
        b = BOOKS[n]
        f = front(n, b)
        p = os.path.join(out, f'cover_book{n}.jpg')
        f.save(p, quality=95, dpi=(200, 200))
        del f
        bk = back(n, b)
        q = os.path.join(out, f'cover_book{n}_back.jpg')
        bk.save(q, quality=95, dpi=(200, 200))
        del bk
        print('wrote', p, q)


if __name__ == '__main__':
    main()
