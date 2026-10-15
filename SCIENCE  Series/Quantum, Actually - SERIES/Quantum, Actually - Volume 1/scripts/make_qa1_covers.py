"""Front and back covers for Quantum, Actually, Volume 1: Questions and Answers from the
Double Slit to the Superconducting Wire, by Lothar J. Musiol (10 Oct 2026).

Same trade dress as Volume 2 (its scripts/make_qed_covers.py supplies the star field, gold frame,
Cinzel gold lettering, orbits and icons): 2202 x 3520 px. No endorsement quotes, no barcode
(KDP adds its own), only claims the book itself makes.

Usage: python make_qa1_covers.py OUTDIR
"""
import math, os, random, sys, importlib.util
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
for cand in (os.path.join(HERE, '..', '..', 'Quantum, Actually - Volume 2', 'scripts', 'make_qed_covers.py'),
             os.path.join(HERE, 'make_qed_covers.py')):
    if os.path.exists(cand):
        spec = importlib.util.spec_from_file_location('qed', cand); Q = importlib.util.module_from_spec(spec); spec.loader.exec_module(Q); break
W, H, GOLD, GOLD_LT, GOLD_DK, CREAM = Q.W, Q.H, Q.GOLD, Q.GOLD_LT, Q.GOLD_DK, Q.CREAM
F, text_c, tw, ornament, gold_text, frame, wrap = Q.F, Q.text_c, Q.tw, Q.ornament, Q.gold_text, Q.frame, Q.wrap

def fringes(size, seed=5, n=9000):
    """double-slit build-up: dots landing with a cos^2 x sinc^2 distribution, blue glow"""
    w, h = size; lay = Image.new('RGBA', size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); rng = random.Random(seed)
    k = 0
    while k < n:
        x = rng.uniform(-1, 1)
        p = math.cos(9.5 * x) ** 2 * (1 if abs(x) < 1e-6 else (math.sin(2.4 * x) / (2.4 * x)) ** 2)
        if rng.random() > p: continue
        y = rng.uniform(0, 1); px, py = (x + 1) / 2 * w, y * h
        fade = 1 - abs(y - 0.5) * 1.6
        if fade <= 0: continue
        a = int(255 * fade * rng.uniform(0.45, 1)); r = rng.choice((1.2, 1.6, 2.0))
        d.ellipse((px - r, py - r, px + r, py + r), fill=(150, 205, 255, a)); k += 1
    glow = lay.filter(ImageFilter.GaussianBlur(4))
    return Image.alpha_composite(glow, lay)

FEATURES = ['31 chapters, each opening with the question it answers',
            'Entanglement, Bell tests and teleportation',
            'Quantum fields, QED and QCD side by side',
            'Four interpretations, none declared the winner',
            'Cryptography and quantum computing',
            'Part Two: from one electron\u2019s phase to a superconducting circuit']

def front():
    img = Q.starfield(41)
    img = Q.binary_column(img, 92, 140, 1500, 6, cols=2)
    Q.add_layer(img, Q.orbits((1700, 1350), 0.9), (250, 1700))
    fr = fringes((900, 480)); img.paste(fr, (660, 2600), fr)
    d = ImageDraw.Draw(img); frame(d)
    text_c(d, (W / 2, 150), 'A QUESTIONS AND ANSWERS BOOK', F('cinzel', 70), CREAM, track=10)
    ornament(d, W / 2, 262, 300)
    gold_text(img, W / 2, 360, 'QUANTUM,', F('cinzel_b', 290), track=10)
    gold_text(img, W / 2, 700, 'ACTUALLY', F('cinzel_b', 290), track=10)
    d = ImageDraw.Draw(img)
    vf = F('cinzel', 66); vw = tw(vf, 'VOLUME 1', 12)
    ornament(d, W / 2, 1100, 460)
    d.rectangle((W / 2 - vw / 2 - 30, 1064, W / 2 + vw / 2 + 30, 1144), fill=(6, 8, 20))
    text_c(d, (W / 2, 1074), 'VOLUME 1', vf, GOLD, track=12)
    sf = F('serif', 84)
    for k, s in enumerate(('Questions and Answers', 'from the Double Slit', 'to the Superconducting Wire')):
        text_c(d, (W / 2, 1210 + k * 108), s, sf, CREAM)
    from PIL import ImageFont
    eqf = None
    for pth in ('/usr/share/fonts/opentype/urw-base35/P052-Italic.otf', '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf', r'C:\Windows\Fonts\cambriai.ttf', r'C:\Windows\Fonts\timesi.ttf'):
        if os.path.exists(pth): eqf = ImageFont.truetype(pth, 92); break
    Q.glow_text(img, (150, 2050), 'i\u0127 \u2202\u03c8/\u2202t = \u0124\u03c8', eqf or F('serif_i', 96), (140, 200, 255), blur=12)
    d = ImageDraw.Draw(img)
    # feature box, right
    bx0, by0, bx1 = 1560, 1700, 2100
    hf, itf = F('cinzel_b', 46), F('serif', 40)
    rows = [wrap(d, itf, s, bx1 - bx0 - 90) for s in FEATURES]
    by1 = by0 + 40 + 2 * 58 + 30 + sum(len(r) * 50 + 46 for r in rows) + 10
    d.rectangle((bx0, by0, bx1, by1), fill=(10, 9, 14), outline=GOLD, width=5)
    d.rectangle((bx0 + 12, by0 + 12, bx1 - 12, by1 - 12), outline=GOLD_DK, width=2)
    y = by0 + 40
    for hl in ('INSIDE', 'THE BOOK:'):
        text_c(d, ((bx0 + bx1) / 2, y), hl, hf, GOLD_LT, track=3); y += 58
    y += 20
    for r in rows:
        d.line((bx0 + 30, y, bx1 - 30, y), fill=GOLD_DK, width=2); y += 16
        d.polygon([(bx0 + 40, y + 16), (bx0 + 50, y + 26), (bx0 + 40, y + 36), (bx0 + 30, y + 26)], fill=GOLD)
        for line in r: d.text((bx0 + 66, y), line, font=itf, fill=CREAM); y += 50
        y += 30
    # badge, left
    cx, cy, R = 380, 2830, 245
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill=(8, 8, 16), outline=GOLD, width=8)
    d.ellipse((cx - R + 16, cy - R + 16, cx + R - 16, cy + R - 16), outline=GOLD_DK, width=2)
    for k, s in enumerate(('Nine Free', 'Interactive', 'Simulations')):
        text_c(d, (cx, cy - 110 + k * 78), s, F('serif', 54), CREAM)
    text_c(d, (W / 2, 3300), 'LOTHAR J. MUSIOL', F('cinzel', 74), CREAM, track=16)
    ornament(d, W / 2, 3420, 160)
    return img

ITEMS = [
    ('arrows', 'WHERE CLASSICAL PHYSICS BROKE',
     'A light bulb, a stubborn equation and a confused Max Planck, then electrons building an interference pattern one dot at a time.'),
    ('xsec', 'ENTANGLEMENT, TESTED',
     'Einstein\u2019s \u201cspooky action at a distance\u201d, Bell\u2019s inequality, and the experiments that earned the 2022 Nobel Prize.'),
    ('vertex', 'FIELDS, QED AND QCD',
     'Why particles are excitations of fields, and why one force weakens at short range while the other grows stronger.'),
    ('levels', 'FOUR INTERPRETATIONS',
     'Copenhagen, many-worlds, Bohmian mechanics and objective collapse, each labeled for what it is, none declared the winner.'),
    ('path', 'CRYPTOGRAPHY AND COMPUTING',
     'Keys that expose an eavesdropper, and quantum computers that are, slowly and noisily, starting to work.'),
    ('loop', 'ONE ROAD THROUGH IT',
     'Part Two follows one question, what the electromagnetic field really is, from an electron\u2019s phase to a circuit on a bench.'),
]
BLURB = ('Nature stops behaving the way you would expect, and this book is the story of exactly where, why, and what '
         'physicists actually did about it. Every chapter opens with the question it answers, and every claim is labeled '
         'as established fact, well-tested theory, or open question.')
QUOTE = ('\u201cPhysics is not a vocabulary test. It is an argument with nature in which nature gets the final vote.\u201d')

def back():
    img = Q.starfield(43)
    img = Q.binary_column(img, 1975, 860, 1700, 11, cols=3)
    Q.add_layer(img, Q.orbits((1200, 1500), 0.8), (1000, 1560))
    d = ImageDraw.Draw(img); frame(d)
    text_c(d, (W / 2, 140), 'QUANTUM, ACTUALLY \u00b7 VOLUME 1', F('cinzel', 76), GOLD, track=10)
    ornament(d, W / 2, 255, 260)
    sf = F('serif', 70)
    text_c(d, (W / 2, 360), 'Questions and Answers from the Double Slit', sf, CREAM)
    text_c(d, (W / 2, 450), 'to the Superconducting Wire', sf, CREAM)
    x0, x1, y = 190, 1880, 620
    bf, cap = F('serif', 56), F('cinzel_b', 214)
    d.text((x0, y - 24), BLURB[0], font=cap, fill=GOLD)
    indent = cap.getlength(BLURB[0]) + 18
    lines, cur, li = [], '', 0
    for w_ in BLURB[1:].split():
        width = x1 - x0 - (indent if li < 3 else 0); t = (cur + ' ' + w_).strip()
        if cur and d.textlength(t, font=bf) > width: lines.append(cur); cur, li = w_, li + 1
        else: cur = t
    lines.append(cur)
    for k, s_ in enumerate(lines): d.text((x0 + (indent if k < 3 else 0), y + k * 78), s_, font=bf, fill=CREAM)
    y += len(lines) * 78 + 36; ornament(d, W / 2, y, 380); y += 56
    hf, tf = F('serif_b', 48), F('serif', 43)
    for kind, head, txt in ITEMS:
        Q.icon(d, kind, 270, y + 72, R=70)
        d.text((390, y), head, font=hf, fill=GOLD); ty = y + 64
        for s_ in wrap(d, tf, txt, 880): d.text((390, ty), s_, font=tf, fill=CREAM); ty += 53
        y = max(ty, y + 150) + 30
    qf = F('serif_i', 46); ql = wrap(d, qf, QUOTE, 1180); qh = len(ql) * 62 + 120; qy = 3230 - qh
    assert qy >= y, (qy, y)
    d.rectangle((180, qy, 1460, qy + qh), fill=(8, 8, 14), outline=GOLD, width=4)
    for k, s_ in enumerate(ql): d.text((225, qy + 30 + k * 62), s_, font=qf, fill=CREAM)
    rf = F('serif', 38); s_ = '\u2014 from the Prologue'
    d.text((1420 - d.textlength(s_, font=rf), qy + qh - 66), s_, font=rf, fill=GOLD)
    text_c(d, (W / 2, 3300), 'CLEAR EXPLANATIONS. REAL SCIENCE. MIND-BLOWING IDEAS.', F('cinzel', 50), GOLD, track=4)
    ornament(d, W / 2, 3420, 120)
    return img

def main():
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    stem = 'Quantum, Actually - Volume 1 - 2202 x 3520 Portrait.jpg'
    front().convert('RGB').save(os.path.join(out, 'Front Cover of ' + stem), quality=93, dpi=(300, 300))
    back().convert('RGB').save(os.path.join(out, 'Back Cover of ' + stem), quality=93, dpi=(300, 300))
    print('wrote both covers to', out)

if __name__ == '__main__':
    main()
