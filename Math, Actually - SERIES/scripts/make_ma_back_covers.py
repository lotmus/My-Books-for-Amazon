"""Back covers for Math, Actually, Volumes 1-4 (10 Oct 2026).

Text only, one colour: the navy, gold Oswald lettering and thin gold frame of the 2 Oct fronts
(`Cover  Volume N.jpg`, 1600 x 2560). Every claim comes from the volume itself or KDP_Description.md
(chapters, sections and worked examples recounted from the .docx on 10 Oct 2026). No barcode
(KDP adds one for print), no outside quotes.

Usage: python make_ma_back_covers.py OUTDIR
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
W, H = 1600, 2560
NAVY, GOLD, CREAM, MUTED = (7, 14, 33), (242, 185, 61), (244, 238, 222), (176, 184, 204)
def font(paths, size, wght=None):
    for p in paths:
        if os.path.exists(p):
            f = ImageFont.truetype(p, size)
            if wght:
                try: f.set_variation_by_axes([wght])
                except Exception: pass
            return f
    raise SystemExit('font missing: ' + paths[0])
OSW = ['/usr/share/fonts/truetype/sand-box/google/Oswald/Oswald-VariableFont_wght.ttf', r'C:\Windows\Fonts\Oswald-VariableFont_wght.ttf']
SER = ['/usr/share/fonts/truetype/sand-box/custom/Source Serif Pro/SourceSerifPro-Regular.ttf', r'C:\Windows\Fonts\georgia.ttf']
SERI = ['/usr/share/fonts/truetype/sand-box/custom/Source Serif Pro/SourceSerifPro-It.ttf', r'C:\Windows\Fonts\georgiai.ttf']

VOLS = {
 1: dict(sub='FROM ARITHMETIC TO CALCULUS', hook='Mathematics is one connected subject. This is where it starts.',
         blurb='Most people meet mathematics as a list of unrelated school subjects. Math, Actually treats it as one connected story, fifty chapters long, told one section at a time. Volume 1 starts with counting and ends with the integral.',
         count='Twelve chapters \u00b7 109 sections \u00b7 430 worked examples',
         items=['Counting, number theory, and why the primes behave the way they do', 'Algebra, functions and graphs, and coordinate systems',
                'Euclidean geometry and trigonometry', 'Logarithms and powers, systems of equations, and vectors',
                'Limits, the derivative, and the integral, through the Fundamental Theorem of Calculus'],
         fit='Written for adults coming back to mathematics, students who want the reasons behind the rules, and anyone who was told they \u201cweren\u2019t a math person.\u201d Volume 1 stands on its own.'),
 2: dict(sub='FROM MULTIVARIABLE CALCULUS TO SET THEORY & LOGIC', hook='From one variable to many, and down to the foundations underneath it all.',
         blurb='Volume 2 takes the calculus of Volume 1 into several dimensions, then builds the tools that science and engineering run on.',
         count='Thirteen chapters \u00b7 118 sections \u00b7 435 worked examples',
         items=['Several variables, multivariable and vector calculus: divergence, curl, and the great integral theorems', 'Series, Fourier transforms and the FFT, and the Laplace transform',
                'Matrices and linear algebra, including eigenvalues and the SVD', 'Integral geometry, analytic geometry and complex analysis',
                'Counting carefully, then set theory and logic: the foundations the whole series rests on'],
         fit='It works best after Volume 1 or a first calculus course.'),
 3: dict(sub='FROM DIFFERENTIAL EQUATIONS TO ABSTRACT ALGEBRA', hook='Where mathematics stops being a toolkit and starts being a landscape.',
         blurb='Volume 3 covers the chapters where most university mathematics lives: the equations that describe change, the methods that compute their solutions, and the abstract structures behind both.',
         count='Twelve chapters \u00b7 105 sections \u00b7 361 worked examples',
         items=['Differential, integro-differential and partial differential equations: heat, waves, and Laplace\u2019s equation', 'Optimization, the calculus of variations, and numerical methods',
                'Differential geometry, topology, tensors and manifolds', 'Functional analysis and measure theory', 'Abstract algebra, from groups to Galois theory'],
         fit='It assumes the chapters before it: Volumes 1 and 2, or the equivalent coursework.'),
 4: dict(sub='FROM CATEGORY THEORY TO THE FRONTIER', hook='The last volume, and the view from the end of the road.',
         blurb='The last volume moves from the most abstract mathematics there is to the places where mathematics meets the world: signals, games, data, machines, and the laws of physics.',
         count='Thirteen chapters \u00b7 118 sections \u00b7 359 worked examples',
         items=['Category theory and information theory', 'Wavelets and signal analysis, game theory and decision mathematics', 'Statistics and probability, standard and advanced',
                'Computational geometry, control theory, and dynamical systems and chaos', 'Mathematical physics, advanced optimization and numerics, and where mathematics meets the world'],
         fit='It assumes the three volumes before it, and several sections reuse earlier theorems without proving them again.'),
}
METHOD = ('Every new idea starts from something you already know. You see where the old idea breaks, you work through real numbers, '
          'and only then does the idea get its name. Every chapter ends with questions and problems, with full answers and worked solutions at the back.')

def wrap(d, f, text, width):
    out, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if cur and d.textlength(t, font=f) > width: out.append(cur); cur = w
        else: cur = t
    out.append(cur); return out
def center(d, y, text, f, fill, track=0):
    if track:
        w = sum(d.textlength(c, font=f) for c in text) + track * (len(text) - 1); x = (W - w) / 2
        for c in text: d.text((x, y), c, font=f, fill=fill); x += d.textlength(c, font=f) + track
    else: d.text(((W - d.textlength(text, font=f)) / 2, y), text, font=f, fill=fill)

def back(v):
    s = VOLS[v]; img = Image.new('RGB', (W, H), NAVY); d = ImageDraw.Draw(img)
    d.rectangle((28, 28, W - 29, H - 29), outline=GOLD, width=4)
    X0, X1 = 150, W - 150
    y = 140
    center(d, y, 'MATH, ACTUALLY', font(OSW, 120, 700), GOLD, track=4); y += 170
    center(d, y, 'VOLUME %d' % v, font(OSW, 58, 600), GOLD, track=12); y += 92
    for line in wrap(d, font(OSW, 50, 500), s['sub'], X1 - X0): center(d, y, line, font(OSW, 50, 500), CREAM, track=3); y += 68
    y += 40; d.line((W / 2 - 120, y, W / 2 + 120, y), fill=GOLD, width=3); y += 60
    hf = font(SERI, 62)
    for line in wrap(d, hf, s['hook'], X1 - X0): center(d, y, line, hf, CREAM); y += 80
    y += 36
    bf = font(SER, 45)
    for line in wrap(d, bf, s['blurb'], X1 - X0): d.text((X0, y), line, font=bf, fill=CREAM); y += 63
    y += 44
    center(d, y, s['count'].upper(), font(OSW, 46, 600), GOLD, track=2); y += 96
    itf = font(SER, 44)
    for it in s['items']:
        lines = wrap(d, itf, it, X1 - X0 - 60)
        d.rectangle((X0 + 6, y + 24, X0 + 22, y + 40), fill=GOLD)
        for line in lines: d.text((X0 + 50, y), line, font=itf, fill=CREAM); y += 60
        y += 18
    y += 30
    for line in wrap(d, bf, METHOD, X1 - X0): d.text((X0, y), line, font=bf, fill=MUTED); y += 63
    y += 30
    for line in wrap(d, bf, s['fit'], X1 - X0): d.text((X0, y), line, font=bf, fill=MUTED); y += 63
    assert y < H - 300, (v, y)
    print(v, 'content ends at', y)
    d.line((W / 2 - 120, H - 270, W / 2 + 120, H - 270), fill=GOLD, width=3)
    center(d, H - 230, 'Bring a pencil.', font(SERI, 52), GOLD)
    center(d, H - 140, 'LOTHAR J. MUSIOL', font(OSW, 54, 600), CREAM, track=8)
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    for v in VOLS:
        back(v).save(os.path.join(out, 'Back Cover  Volume %d.jpg' % v), quality=92, dpi=(300, 300))
    print('wrote four back covers to', out)
