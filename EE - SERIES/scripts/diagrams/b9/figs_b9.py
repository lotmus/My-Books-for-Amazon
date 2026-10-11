"""Figures for Book 9, Test and Measurement Instruments.

Every figure is computed or drawn here from the numbers in the worked examples; CHECK lines
print (and assert) the values that the captions quote. Run: python figs_b9.py [name ...]  (output in ./fig)
Style: the series' eestyle helpers (imported read-only), 800 px wide, 64-color PNG. Needs numpy, matplotlib, PIL;
scipy only for the Bessel-function figure (b9_fm_bessel), with a pure-numpy fallback.
"""
import math
import os
import sys

import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'common'))   # series helpers, read-only
from eestyle import BLUE, RED, GREEN, GRAY, ORANGE, INK, fig, save, plt   # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle  # noqa: E402

OUT = os.path.join(HERE, 'fig')
os.makedirs(OUT, exist_ok=True)
LIGHT = {'blue': '#dce8f5', 'green': '#dff0e5', 'orange': '#f8e6d2', 'gray': '#eeeeee', 'red': '#f6d9d5'}
SCREEN = '#0b1a24'; TRACE = '#f2d43a'; TRACE2 = '#3ad1f2'; GRID = '#2c4250'
FIGS = {}
def figure(fn):
    FIGS[fn.__name__] = fn
    return fn
def check(msg, cond=True):
    print(('CHECK ' if cond else 'CHECK FAILED ') + msg)
    if not cond:
        raise SystemExit('check failed: ' + msg)
def canvas(w=8, h=4.5, xmax=100, ymax=56):
    f, ax = fig(w, h)
    ax.set_xlim(0, xmax); ax.set_ylim(0, ymax); ax.axis('off')
    return f, ax
def box(ax, x, y, w, h, text, fc=None, ec=INK, fs=10, bold=False, color=INK, ls='-'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.4,rounding_size=1.2',
                                fc=fc or 'white', ec=ec, lw=1.2, ls=ls))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs,
            fontweight='bold' if bold else 'normal', color=color)
def arrow(ax, x0, y0, x1, y1, text=None, color=INK, fs=9, off=(0, 1.2), ls='-', rad=0.0, lw=1.3):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=12,
                                 color=color, lw=lw, ls=ls, connectionstyle='arc3,rad=%g' % rad))
    if text:
        ax.text((x0 + x1) / 2 + off[0], (y0 + y1) / 2 + off[1], text, ha='center', va='bottom', fontsize=fs, color=color)
def screen(ax, xlabel='', ylabel=''):
    """Instrument-screen look: dark background, light grid."""
    ax.set_facecolor(SCREEN)
    ax.grid(True, color=GRID, lw=0.7)
    for s in ax.spines.values():
        s.set_color(INK)
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
def finish(f, name):
    path = os.path.join(OUT, name + '.png')
    save(f, path)
    from PIL import Image
    w, h = Image.open(path).size
    check('%s.png %dx%d px' % (name, w, h), w == 800)
db = lambda x: 10 * np.log10(x)

# ---------------------------------------------------------------- Part I
@figure
def b9_precision():
    rng = np.random.default_rng(9)
    cases = [('accurate and precise', 0, 0.5), ('precise, not accurate', 3, 0.5),
             ('accurate on average, not precise', 0, 2.0), ('neither', 3, 2.0)]
    f, axs = plt.subplots(2, 2, figsize=(8, 8), dpi=100)
    for ax, (t, bias, sd) in zip(axs.flat, cases):
        p = rng.normal(0, sd, (40, 2)) + bias / math.sqrt(2)
        m = p.mean(axis=0); off = math.hypot(*m); spread = p.std(axis=0, ddof=1).mean()
        check('%s: offset %.2f (design %g), spread %.2f (design %g)' % (t, off, bias, spread, sd),
              abs(off - bias) < 0.5 + 0.25 * sd and abs(spread - sd) < 0.2 * sd)
        for rr in (2, 4, 6):
            ax.add_patch(Circle((0, 0), rr, fill=False, color=GRAY, lw=0.8))
        ax.plot(p[:, 0], p[:, 1], 'o', ms=4, color=BLUE)
        ax.plot(0, 0, 'x', color=RED, ms=12, mew=2.5)
        ax.set_xlim(-7, 7); ax.set_ylim(-7, 7); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
        ax.set_title('%s\nmean offset %.1f, spread %.1f' % (t, off, spread), fontsize=10)
    finish(f, 'b9_precision')

@figure
def b9_budget():
    u = [('meter specification', 2.0003 / math.sqrt(3)), ('temperature (5 ppm/K, ±3 K)', 0.15 / math.sqrt(3)),
         ('repeatability (5 readings)', 0.08 / math.sqrt(5)), ('resolution (0.1 Ω)', 0.05 / math.sqrt(3))]
    uc = math.sqrt(sum(v * v for _, v in u))
    check('budget uc %.3f (1.159), U %.2f (2.32)' % (uc, 2 * uc), abs(uc - 1.159) < 0.001 and abs(2 * uc - 2.32) < 0.005)
    rows = u + [('combined u_c', uc), ('expanded U (k = 2)', 2 * uc)]
    f, ax = fig(8, 3.8)
    y = np.arange(len(rows))[::-1]
    cols = [BLUE] * 4 + [GREEN, RED]
    ax.barh(y, [v for _, v in rows], color=cols, height=0.6)
    for yy, (n, v) in zip(y, rows):
        ax.text(v + 0.03, yy, '%.3f Ω' % v, va='center', fontsize=9)
    ax.set_yticks(y); ax.set_yticklabels([n for n, _ in rows], fontsize=9)
    ax.set_xlim(0, 2.8); ax.set_xlabel('standard uncertainty (Ω)'); ax.grid(axis='y', visible=False)
    ax.set_title('Worked Example 2.1: 10 000.3 Ω measured four-wire')
    finish(f, 'b9_budget')

@figure
def b9_loading():
    rs = np.logspace(2, 8, 300)
    f, ax = fig(8, 4.6)
    for rin, c, lab in ((1e6, ORANGE, '1 MΩ input'), (10e6, BLUE, '10 MΩ input'), (10e9, GREEN, '10 GΩ input')):
        ax.loglog(rs, 100 * rs / (rs + rin), color=c, lw=2, label=lab)
    e = 100 * 0.5e6 / (10.5e6)
    e2 = 100 * 0.5e6 / (1e10 + 0.5e6)
    check('loading 500k/10M %.2f %% (4.76), 500k/10G %.4f %% (0.005 = 50 ppm)' % (e, e2), abs(e - 4.76) < 0.01 and abs(e2 - 0.005) < 1e-4)
    ax.plot([0.5e6], [e], 'o', color=RED, ms=8); ax.annotate('WE 3.1: 4.76 % low', (0.5e6, e), (2e3, 20), color=RED, arrowprops=dict(arrowstyle='->', color=RED))
    ax.plot([0.5e6], [e2], 'o', color=RED, ms=8); ax.annotate('same node, 10 GΩ: 50 ppm', (0.5e6, e2), (3e2, 2e-3), color=RED, arrowprops=dict(arrowstyle='->', color=RED))
    ax.set_xlabel('source Thevenin resistance (Ω)'); ax.set_ylabel('reading low by (%)'); ax.set_ylim(1e-5, 150)
    ax.legend(loc='lower right')
    finish(f, 'b9_loading')

@figure
def b9_cat():
    f, ax = canvas(8, 3.8, 100, 48)
    zones = [('CAT IV', 'utility line,\nmeter, service\nentrance', LIGHT['red'], '600 V: 8 kV\n1000 V: 12 kV'),
             ('CAT III', 'distribution\npanel, fixed\nwiring, busbars', LIGHT['orange'], '600 V: 6 kV\n1000 V: 8 kV'),
             ('CAT II', 'outlets and\nplugged-in\nequipment', LIGHT['blue'], '300 V: 2.5 kV\n600 V: 4 kV'),
             ('not mains', 'battery boards,\nisolated\nsecondaries', LIGHT['green'], 'O (formerly\nCAT I)')]
    for k, (cat, what, c, imp) in enumerate(zones):
        x = 2 + k * 25
        box(ax, x, 22, 21, 17, what, fc=c, fs=9)
        ax.text(x + 10.5, 42, cat, ha='center', fontsize=12, fontweight='bold')
        ax.text(x + 10.5, 12, imp, ha='center', va='center', fontsize=9)
        if k:
            arrow(ax, x - 3.6, 30.5, x - 0.6, 30.5)
    ax.text(50, 3, 'transient withstand (peak impulse) for each working-voltage rating, IEC 61010-2-030', ha='center', fontsize=8.5, color=GRAY)
    finish(f, 'b9_cat')

# ---------------------------------------------------------------- Part II
@figure
def b9_cvcc():
    V, I = 12.0, 1.0
    f, ax = fig(8, 4.6)
    ax.plot([0, I, I], [V, V, 0], color=INK, lw=2.5)
    ax.fill_between([0, I], 0, V, color=LIGHT['blue'])
    pts = []
    for R, c in ((8, RED), (12, ORANGE), (20, GREEN)):
        i = np.linspace(0, 1.6, 50); ax.plot(i, i * R, '--', color=c, lw=1.3)
        ip = min(V / R, I); vp = ip * R; pts.append((R, ip, vp))
        ax.plot(ip, vp, 'o', color=c, ms=9)
        ax.text(ip + 0.03, vp + 0.4, '%d Ω: %.1f V, %.2f A (%s)' % (R, vp, ip, 'CC' if V / R > I else ('crossover' if V / R == I else 'CV')), color=c, fontsize=9)
    check('cvcc 8 ohm -> %.1f V %.2f A; 20 ohm -> %.1f V %.2f A' % (pts[0][2], pts[0][1], pts[2][2], pts[2][1]),
          pts[0][2] == 8 and pts[0][1] == 1 and pts[2][2] == 12 and abs(pts[2][1] - 0.6) < 1e-9)
    ax.set_xlim(0, 1.6); ax.set_ylim(0, 14); ax.set_xlabel('output current (A)'); ax.set_ylabel('output voltage (V)')
    ax.text(0.05, 12.4, 'CV limit 12 V', fontsize=9); ax.text(1.02, 2, 'CC limit\n1 A', fontsize=9)
    finish(f, 'b9_cvcc')

@figure
def b9_quadrants():
    f, ax = fig(8, 5)
    env_v = [21, 21, 210, 210]; env_i = [1.05, 0.105, 0.105, 0]
    xs = [0, 21, 21, 210, 210]; ys = [1.05, 1.05, 0.105, 0.105, 0]
    for sx in (1, -1):
        for sy in (1, -1):
            ax.plot([sx * x for x in xs], [sy * y for y in ys], color=BLUE, lw=2)
    check('quadrant envelope 21 V x 1.05 A = %.1f W (<= 22), 210 V x 0.105 A = %.1f W' % (21 * 1.05, 210 * 0.105), 21 * 1.05 < 22.1 and 210 * 0.105 < 22.1)
    i = np.logspace(-9, -2, 50); v = 1.75 * 0.025852 * np.log(i / 2.5e-9 + 1) + 2 * i
    ax.plot(v, i * 50, color=RED, lw=2.5); ax.text(8, 0.45, 'diode forward curve\n(current ×50 for visibility)', color=RED, fontsize=9)
    ax.plot(3.7, -0.5, 's', color=GREEN, ms=10); ax.text(10, -0.55, 'battery discharged at 0.5 A\n(sink, quadrant 4)', color=GREEN, fontsize=9)
    for x, y, t in ((120, 0.6, 'I: source'), (-120, 0.6, 'II: sink'), (-120, -0.6, 'III: source'), (120, -0.85, 'IV: sink')):
        ax.text(x, y, t, ha='center', fontsize=11, color=GRAY, fontweight='bold')
    ax.axhline(0, color=INK, lw=0.8); ax.axvline(0, color=INK, lw=0.8)
    ax.set_xlim(-230, 230); ax.set_ylim(-1.25, 1.25); ax.set_xlabel('voltage (V)'); ax.set_ylabel('current (A)')
    finish(f, 'b9_quadrants')

@figure
def b9_load_modes():
    f, ax = fig(8, 4.6)
    i = np.linspace(0.01, 10.5, 400)
    ax.axvline(2, color=BLUE, lw=2, label='CC 2 A')
    ax.plot(i, 2.5 * i, color=GREEN, lw=2, label='CR 2.5 Ω')
    ax.axhline(5, color=GRAY, lw=2, label='CV 5 V')
    ax.plot(i, 10 / i, color=RED, lw=2.5, label='CP 10 W')
    ax.axvline(3, color=ORANGE, lw=1.5, ls='--', label='converter limit 3 A')
    check('CP at 1 V = %.0f A (10), at 4.5 V = %.2f A (2.22), crossing 3 A at %.2f V (3.33)' % (10 / 1, 10 / 4.5, 10 / 3),
          abs(10 / 4.5 - 2.22) < 0.005)
    ax.plot(2, 5, 'ko', ms=8); ax.text(2.15, 5.2, '10 W at 5 V', fontsize=9)
    ax.plot(3, 10 / 3, 'o', color=ORANGE, ms=8); ax.text(3.15, 3.5, '3.3 V at 3 A', fontsize=9, color=ORANGE)
    ax.set_xlim(0, 10.5); ax.set_ylim(0, 6.5); ax.set_xlabel('load current (A)'); ax.set_ylabel('voltage (V)'); ax.legend(loc='upper right', fontsize=9)
    finish(f, 'b9_load_modes')

@figure
def b9_matrix():
    f, ax = canvas(8, 4.2, 100, 52)
    rows = ['SMU force', 'SMU sense', 'DMM', 'scope']
    for r, name in enumerate(rows):
        y = 42 - r * 10
        ax.plot([20, 96], [y, y], color=INK, lw=1.3); ax.text(18, y, name, ha='right', va='center', fontsize=10)
    for c in range(8):
        x = 26 + c * 9.5
        ax.plot([x, x], [6, 46], color=GRAY, lw=1.3); ax.text(x, 2.5, 'pin %d' % (c + 1), ha='center', fontsize=9)
    closed = {(0, 2), (2, 5)}
    n = 0
    for r in range(4):
        for c in range(8):
            n += 1
            fc = RED if (r, c) in closed else 'white'
            ax.add_patch(Circle((26 + c * 9.5, 42 - r * 10), 1.3, fc=fc, ec=INK, lw=1, zorder=3))
    check('matrix crosspoints %d (32)' % n, n == 32)
    ax.text(58, 50, 'closed: SMU force to pin 3, DMM to pin 6', ha='center', fontsize=9, color=RED)
    finish(f, 'b9_matrix')

@figure
def b9_buses():
    data = [('GPIB, 1 MB/s', 10e6 / 1e6), ('USB 2.0, ~30 MB/s', 10e6 / 30e6), ('Gigabit Ethernet, ~100 MB/s', 10e6 / 100e6),
            ('PCIe Gen 3 x8, ~7.9 GB/s', 10e6 / 7.88e9)]
    check('bus times %s' % ', '.join('%.3g s' % t for _, t in data), abs(data[0][1] - 10) < 1e-9 and abs(data[3][1] - 1.27e-3) < 0.02e-3)
    f, ax = fig(8, 3.4)
    y = np.arange(4)[::-1]
    ax.barh(y, [t for _, t in data], color=[ORANGE, BLUE, GREEN, RED], height=0.55)
    ax.set_xscale('log'); ax.set_xlim(1e-3, 100)
    for yy, (n, t) in zip(y, data):
        ax.text(t * 1.15, yy, ('%.2g s' % t) if t >= 0.01 else ('%.1f ms' % (t * 1e3)), va='center', fontsize=9)
    ax.set_yticks(y); ax.set_yticklabels([n for n, _ in data]); ax.set_xlabel('time to move 10 MB (s), log scale'); ax.grid(axis='y', visible=False)
    finish(f, 'b9_buses')

# ---------------------------------------------------------------- Chapters 7 and 8 (curve tracer, datasheet, SPICE)
CTG = '#39e46b'
def ext():
    sys.path.insert(0, os.path.join(HERE, 'listings'))
    import l07_1_extract as L
    return L

@figure
def b9_ct_diode():
    L = ext()
    i = np.logspace(-9, -1, 81); v = L.diode_model(i)
    n, i_s, rs, dec = L.diode_params(v, i)
    check('diode n %.3f, Is %.2f nA, Rs %.3f, %.1f mV/dec, Vf(10 mA) %.3f' % (n, i_s * 1e9, rs, dec * 1e3, L.diode_model(10e-3)),
          abs(n - 1.836) < 0.002 and abs(dec * 1e3 - 109.3) < 0.1 and abs(rs - 0.567) < 0.002 and abs(L.diode_model(10e-3) - 0.724) < 0.0005)
    gap = (L.diode_model(0.1) - n * L.VT * math.log(0.1 / i_s + 1)) * 1e3
    check('Rs excess at 100 mA %.1f mV (56.6)' % gap, abs(gap - 56.6) < 0.2)
    f, ax = fig(8, 4.8); screen(ax, 'forward voltage (V)', 'forward current (A)')
    ax.semilogy(v, i, color=CTG, lw=2.2)
    vl = np.linspace(0, 0.85, 50); ax.semilogy(vl, i_s * np.exp(vl / (n * L.VT)), '--', color=TRACE, lw=1.3)
    ax.plot(0.724, 10e-3, 'o', color=TRACE); ax.text(0.5, 2e-2, 'Vf = 0.724 V at 10 mA', color=TRACE, fontsize=9)
    ax.text(0.05, 3e-8, 'slope 109.3 mV/decade\nn = 1.836, Is = 2.7 nA', color=TRACE, fontsize=9)
    ax.annotate('', (L.diode_model(0.1), 0.1), (L.diode_model(0.1) - gap / 1e3, 0.1), arrowprops=dict(arrowstyle='<->', color='white'))
    ax.text(0.62, 0.15, 'Rs: 56.6 mV at 100 mA', color='white', fontsize=9)
    ax.set_xlim(0, 0.9); ax.set_ylim(1e-9, 0.3)
    ins = f.add_axes([0.6, 0.22, 0.28, 0.3]); screen(ins)
    iz = np.linspace(0.1e-3, 12e-3, 50); vz = 5.1 + 15 * (iz - 5e-3)
    rz = L.zener_rz(vz, iz, 1e-3, 10e-3); check('zener rz %.1f ohm (15)' % rz, abs(rz - 15) < 1e-6)
    ins.plot(vz, iz * 1e3, color=CTG, lw=2); ins.set_title('Zener reverse: rz = 15 Ω', fontsize=8, color='white')
    ins.tick_params(labelsize=7, colors='white'); ins.set_xlabel('V', fontsize=7, color='white'); ins.set_ylabel('mA', fontsize=7, color='white')
    finish(f, 'b9_ct_diode')

@figure
def b9_ct_bjt():
    L = ext()
    vce = np.linspace(0, 20, 401)
    f, ax = fig(8, 4.6); screen(ax, 'collector-emitter voltage (V)', 'collector current (mA)')
    for k in range(1, 6):
        ic = L.bjt_ic(vce, k * 10e-6); ax.plot(vce, ic * 1e3, color=CTG, lw=2)
        va, ro = L.early_voltage(vce, ic)
        g = 1 / ro; i2 = np.interp(2.0, vce, ic)
        xl = np.linspace(-va, 2, 20); ax.plot(xl, (i2 + g * (xl - 2)) * 1e3, '--', color=TRACE, lw=0.9)
        ax.text(20.6, ic[-1] * 1e3, '%d µA' % (k * 10), color='white', fontsize=8, va='center')
        if k == 2:
            check('BJT 20 uA: Ic(5 V) %.3f mA, hFE %.0f, VA %.1f V, ro %.1f k' % (L.bjt_ic(5.0, 20e-6) * 1e3, L.bjt_ic(5.0, 20e-6) / 20e-6, va, ro / 1e3),
                  abs(va - 75) < 0.2 and abs(ro / 1e3 - 18.75) < 0.1 and round(L.bjt_ic(5.0, 20e-6) / 20e-6) == 213)
    ax.plot(-75, 0, 'o', color=RED, ms=8); ax.text(-74, 0.6, 'lines meet near −VA = −75 V', color='white', fontsize=9)
    ax.set_xlim(-80, 27); ax.set_ylim(0, 13)
    finish(f, 'b9_ct_bjt')

@figure
def b9_ct_mosfet():
    L = ext()
    vgs = np.linspace(0.5, 5, 451); sat = L.mos_id(vgs, vgs)
    v1 = L.vth_sqrt(vgs, sat); v2 = L.vth_const_current(vgs, sat); S = L.subthreshold_slope(vgs, sat)
    check('MOSFET Vth sqrt %.3f (1.654), 250 uA %.3f (1.511), S %.1f mV/dec (83.4)' % (v1, v2, S * 1e3),
          abs(v1 - 1.654) < 0.001 and abs(v2 - 1.511) < 0.001 and abs(S * 1e3 - 83.4) < 0.1)
    f, (a1, a2) = plt.subplots(1, 2, figsize=(8, 4.2), dpi=100)
    screen(a1, 'Vgs (V)', '√Id (√A)'); screen(a2, 'Vgs (V)', 'Id (A)')
    s = np.sqrt(sat); a1.plot(vgs, s, color=CTG, lw=2)
    k = np.argmax(np.gradient(s, vgs)); a, b = np.polyfit(vgs[k - 3:k + 4], s[k - 3:k + 4], 1)
    xl = np.linspace(v1, 5, 10); a1.plot(xl, a * xl + b, '--', color=TRACE); a1.plot(v1, 0, 'o', color=RED)
    a1.text(1.8, 0.2, 'Vth = 1.654 V\n(√Id extrapolation)', color=TRACE, fontsize=9); a1.set_ylim(0, 3.5)
    a2.semilogy(vgs, sat, color=CTG, lw=2); a2.axhline(250e-6, color=TRACE, ls='--', lw=1)
    a2.plot(v2, 250e-6, 'o', color=RED); a2.text(1.9, 1e-4, '250 µA: 1.511 V', color=TRACE, fontsize=9)
    a2.text(0.6, 3e-2, 'subthreshold\n83.4 mV/decade', color=TRACE, fontsize=9); a2.set_ylim(1e-9, 20)
    finish(f, 'b9_ct_mosfet')

@figure
def b9_ct_selfheat():
    L = ext()
    def dc(vgs, vds, rth=10.0):
        T = 300.0
        for _ in range(200):
            i = L.mos_id(vgs, vds, k=2.0 * (T / 300) ** -1.5, vth=1.6 - 0.004 * (T - 300)); T = 300 + rth * i * vds
        return float(i), T - 300
    vds = np.linspace(0.01, 10, 120)
    f, ax = fig(8, 4.6); screen(ax, 'drain voltage (V)', 'drain current (A)')
    res = {}
    for vg, c in ((2.6, CTG), (3.0, TRACE2), (3.5, TRACE)):
        p = L.mos_id(vg, vds); d = np.array([dc(vg, x)[0] for x in vds])
        ax.plot(vds, p, color=c, lw=2); ax.plot(vds, d, '--', color=c, lw=2)
        ax.text(10.1, p[-1], '%.1f V' % vg, color='white', fontsize=9, va='center')
        res[vg] = (float(L.mos_id(vg, 10.0)), dc(vg, 10.0))
    p35, (d35, t35) = res[3.5]; p26, (d26, _) = res[2.6]
    check('selfheat 3.5 V: pulsed %.3f DC %.3f (%.1f %%), rise %.0f K; 2.6 V: pulsed %.3f DC %.3f' % (p35, d35, (d35 / p35 - 1) * 100, t35, p26, d26),
          abs(p35 - 2.836) < 0.001 and abs(d35 - 2.664) < 0.001 and abs(t35 - 266) < 1 and abs(d26 - 1.000) < 0.001 and abs(p26 - 0.786) < 0.001)
    ax.text(0.5, 3.0, 'solid: pulsed (300 K)   dashed: DC, 10 K/W', color='white', fontsize=9)
    ax.set_xlim(0, 11); ax.set_ylim(0, 3.3)
    finish(f, 'b9_ct_selfheat')

@figure
def b9_double_pulse():
    f, (a1, a2) = plt.subplots(2, 1, figsize=(8, 5.6), dpi=100)
    t = np.linspace(0, 9e-6, 1801)
    g = ((t > 0.5e-6) & (t < 5.5e-6)) | ((t > 7e-6) & (t < 8e-6))
    il = np.zeros_like(t); dt = t[1] - t[0]
    for k in range(1, len(t)):
        il[k] = il[k - 1] + (400 / 100e-6 * dt if g[k] else 0)
    check('first pulse 5 us -> %.1f A (20)' % il[np.searchsorted(t, 5.5e-6) - 1], abs(il[np.searchsorted(t, 5.5e-6) - 1] - 20) < 0.1)
    a1.plot(t * 1e6, g * 10, color=GRAY, lw=1.5, label='gate (V)'); a1.plot(t * 1e6, il, color=BLUE, lw=2, label='inductor current (A)')
    a1.set_xlabel('time (µs)'); a1.legend(loc='upper left', fontsize=9); a1.set_ylim(-1, 26)
    a1.annotate('turn-off\nmeasured here', (5.5, 20), (6.0, 23), fontsize=8, arrowprops=dict(arrowstyle='->'))
    tt = np.linspace(-5e-9, 40e-9, 45001); d = tt[1] - tt[0]
    v = np.clip(tt / 15e-9, 0, 1) * 400; i = lambda x: 20 * np.clip(1 - (x - 15e-9) / 15e-9, 0, 1)
    E = np.sum(v * i(tt)) * d; E2 = np.sum(v * i(tt - 2e-9)) * d
    check('Eoff %.1f uJ (120), with 2 ns skew %.1f uJ (136)' % (E * 1e6, E2 * 1e6), abs(E * 1e6 - 120) < 0.3 and abs(E2 * 1e6 - 136) < 0.3)
    a2.plot(tt * 1e9, v, color=RED, lw=2, label='Vds (V)'); a2.plot(tt * 1e9, i(tt) * 20, color=BLUE, lw=2, label='Id × 20 (A)')
    a2.fill_between(tt * 1e9, v * i(tt) / 20, color=ORANGE, alpha=0.5, label='p(t)/20 (W)')
    a2.set_xlabel('time (ns), turn-off edge'); a2.legend(loc='center right', fontsize=9)
    a2.text(20, 150, 'Eoff = 120 µJ\n(136 µJ with 2 ns skew)', fontsize=9)
    finish(f, 'b9_double_pulse')

@figure
def b9_diode_fit():
    import runpy, io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        g = runpy.run_path(os.path.join(HERE, 'listings', 'l08_1_fit_diode.py'))
    i, v, res, fit = g['i_meas'], g['v_meas'], g['res'], g['fit']
    rms = math.sqrt(np.mean(res[fit] ** 2)); lo = np.max(np.abs(res[(i >= 1e-8) & (i <= 1e-7)])); hi = np.max(np.abs(res[i >= 30e-3]))
    check('fit N %.3f IS %.3g RS %.3f; rms %.2f mV, low %.1f mV, high %.1f mV' % (g['N'], g['IS'], g['RS'], rms, lo, hi),
          abs(g['N'] - 1.046) < 0.001 and abs(g['RS'] - 0.323) < 0.001 and abs(rms - 1.25) < 0.01 and abs(lo - 67.2) < 0.1 and abs(hi - 22.2) < 0.1)
    f, (a1, a2) = plt.subplots(2, 1, figsize=(8, 5.6), dpi=100, sharex=True)
    for a in (a1, a2):
        a.axvspan(1e-6, 20e-3, color=LIGHT['green'])
    a1.semilogx(i, v, 'o', ms=3.5, color=BLUE, label='measured')
    a1.semilogx(i, g['spice_v'](i, g['IS'], g['N'], g['RS']), color=RED, lw=1.6, label='fitted SPICE diode')
    a1.set_ylabel('forward voltage (V)'); a1.legend(loc='upper left', fontsize=9); a1.text(2e-6, 0.85, 'fit range 1 µA to 20 mA', fontsize=9, color=GREEN)
    a2.semilogx(i, res, 'o-', ms=3, color=INK, lw=0.8); a2.axhline(0, color=GRAY)
    a2.set_ylabel('residual (mV)'); a2.set_xlabel('forward current (A)')
    a2.text(2e-8, -60, 'up to 67 mV (not fitted)', fontsize=9, color=RED); a2.text(5e-3, 12, '22 mV', fontsize=9, color=RED)
    a2.text(1e-5, -25, 'inside: 1.25 mV rms', fontsize=9)
    finish(f, 'b9_diode_fit')

# ---------------------------------------------------------------- Part III
@figure
def b9_dmm_nmrr():
    f_ = np.linspace(10, 200, 3801)
    def rej(T):
        x = np.pi * f_ * T
        return -20 * np.log10(np.maximum(np.abs(np.sin(x) / x), 1e-3))
    r60, r50 = rej(1 / 60), rej(0.02)
    x = np.pi * 50 / 60; at50 = -20 * math.log10(abs(math.sin(x) / x))
    check('NMRR 1 PLC(60) at 50 Hz %.1f dB (14.4)' % at50, abs(at50 - 14.4) < 0.05)
    f, ax = fig(8, 4.2)
    ax.plot(f_, r60, color=BLUE, lw=1.6, label='16.67 ms (1 PLC at 60 Hz)')
    ax.plot(f_, r50, color=ORANGE, lw=1.6, label='20 ms (1 PLC at 50 Hz)')
    ax.plot(50, at50, 'o', color=RED); ax.annotate('14.4 dB at 50 Hz', (50, at50), (62, 45), arrowprops=dict(arrowstyle='->'), fontsize=9)
    ax.set_xlabel('input frequency (Hz)'); ax.set_ylabel('normal-mode rejection (dB)'); ax.set_ylim(0, 62)
    ax.legend(loc='upper right', fontsize=9)
    finish(f, 'b9_dmm_nmrr')

@figure
def b9_lcr_sweep():
    fr = np.logspace(2, 8, 600); w = 2 * np.pi * fr
    z = 0.010 + 1j * (w * 1e-9 - 1 / (w * 10e-6))
    srf = 1 / (2 * math.pi * math.sqrt(1e-9 * 10e-6))
    check('SRF %.3f MHz (1.59), |Z|min %.4f ohm' % (srf / 1e6, abs(z).min()), abs(srf / 1e6 - 1.59) < 0.005 and abs(abs(z).min() - 0.010) < 2e-4)
    f, ax = fig(8, 4.4); screen(ax, 'frequency (Hz)', '|Z| (Ω)')
    ax.loglog(fr, abs(z), color=CTG, lw=2.2)
    a2 = ax.twinx(); a2.semilogx(fr, np.degrees(np.angle(z)), color=TRACE, lw=1.4)
    a2.set_ylim(-100, 100); a2.set_ylabel('phase (°)', color=TRACE); a2.tick_params(colors=TRACE)
    ax.axvline(srf, color='white', ls=':', lw=1); ax.text(srf * 1.2, 2, 'SRF 1.59 MHz\n|Z| = ESR = 10 mΩ', color='white', fontsize=9)
    ax.text(300, 0.003, 'capacitive', color='white', fontsize=9); ax.text(2e7, 30, 'inductive', color='white', fontsize=9)
    ax.set_ylim(1e-3, 1e4)
    finish(f, 'b9_lcr_sweep')

@figure
def b9_lowlevel_settle():
    t = np.logspace(-1, math.log10(900), 500)
    t1 = math.log(1000) * 100; t2 = math.log(1000) * 1
    check('settle 0.1 %%: %.0f s unguarded (691), %.1f s guarded (6.9)' % (t1, t2), round(t1) == 691 and abs(t2 - 6.9) < 0.05)
    f, ax = fig(8, 4.2)
    ax.semilogx(t, 100 * (1 - np.exp(-t / 1.0)), color=GREEN, lw=2, label='guarded, τ = 1 s')
    ax.semilogx(t, 100 * (1 - np.exp(-t / 100.0)), color=RED, lw=2, label='unguarded 100 pF, τ = 100 s')
    for tt, c in ((t2, GREEN), (t1, RED)):
        ax.axvline(tt, color=c, ls='--', lw=1)
    ax.text(t1 * 0.55, 40, '691 s', color=RED, fontsize=9, rotation=90); ax.text(t2 * 0.6, 40, '6.9 s', color=GREEN, fontsize=9, rotation=90)
    ax.set_xlabel('time (s)'); ax.set_ylabel('reading (% of final)'); ax.legend(loc='upper left', fontsize=9); ax.set_ylim(0, 105)
    finish(f, 'b9_lowlevel_settle')

@figure
def b9_counter_res():
    fin = np.logspace(0, 9, 100)
    conv = 1 / fin
    check('counter 1 kHz conv %.0e, recip %.0e, interp %.0e' % (1 / 1e3, 10e-9 / 1, 20e-12 / 1), True)
    f, ax = fig(8, 4.2)
    ax.loglog(fin, conv, color=BLUE, lw=2, label='conventional, ±1 input cycle')
    ax.loglog(fin, np.full_like(fin, 1e-8), color=ORANGE, lw=2, label='reciprocal, 100 MHz clock')
    ax.loglog(fin, np.full_like(fin, 2e-11), color=GREEN, lw=2, label='with 20 ps interpolator')
    ax.plot(1e3, 1e-3, 'o', color=RED); ax.annotate('1 kHz: 1 × 10⁻³', (1e3, 1e-3), (3e3, 3e-2), arrowprops=dict(arrowstyle='->'), fontsize=9)
    ax.set_xlabel('input frequency (Hz)'); ax.set_ylabel('relative resolution in 1 s'); ax.set_ylim(1e-12, 2)
    ax.legend(loc='lower left', fontsize=9)
    finish(f, 'b9_counter_res')

# ---------------------------------------------------------------- Part IV
@figure
def b9_scope_risetime():
    tr = np.linspace(0.05, 6, 200)
    a = math.hypot(2.0, 3.5); b = math.hypot(2.0, 0.7)
    check('displayed 2 ns: %.2f ns on 100 MHz, %.2f ns on 500 MHz' % (a, b), abs(a - 4.03) < 0.005 and abs(b - 2.12) < 0.005)
    f, ax = fig(8, 4.4)
    for bw, c in ((100, RED), (500, ORANGE), (1000, GREEN)):
        ts = 0.35 / (bw * 1e6) * 1e9
        ax.plot(tr, np.hypot(tr, ts), color=c, lw=2, label='%s (scope %.2f ns)' % ('%d MHz' % bw if bw < 1000 else '1 GHz', ts))
    ax.plot(tr, tr, '--', color=GRAY, lw=1.2, label='true')
    ax.plot([2, 2], [a, b], 'o', color=BLUE)
    ax.annotate('4.03 ns (100 MHz)', (2, a), (2.6, 5.2), arrowprops=dict(arrowstyle='->'), fontsize=9)
    ax.annotate('2.12 ns (500 MHz)', (2, b), (3.0, 1.3), arrowprops=dict(arrowstyle='->'), fontsize=9)
    ax.set_xlabel('true rise time (ns)'); ax.set_ylabel('displayed rise time (ns)'); ax.set_ylim(0, 8); ax.legend(loc='upper left', fontsize=9)
    finish(f, 'b9_scope_risetime')

@figure
def b9_probe_ground():
    def step(L, C=11e-12, R=50.0, tr=1e-9, T=40e-9, dt=1e-12):
        n = int(T / dt); vin = np.clip(np.arange(n) * dt / tr, 0, 1)
        i = 0.0; vc = 0.0; out = np.empty(n)
        for k in range(n):                      # series R-L into the probe capacitance (semi-implicit Euler)
            i += (vin[k] - vc - R * i) / L * dt
            vc += i / C * dt
            out[k] = vc
        return np.arange(n) * dt, out
    t, a = step(150e-9); _, b = step(10e-9)
    fa = 1 / (2 * math.pi * math.sqrt(150e-9 * 11e-12)); qa = math.sqrt(150e-9 / 11e-12) / 50; qb = math.sqrt(10e-9 / 11e-12) / 50
    check('lead %.0f MHz Q %.2f; spring Q %.2f; overshoot %.0f %% vs %.1f %%' % (fa / 1e6, qa, qb, (a.max() - 1) * 100, (b.max() - 1) * 100),
          abs(fa / 1e6 - 124) < 0.5 and abs(qa - 2.3) < 0.05 and abs(qb - 0.60) < 0.01 and a.max() > 1.2 and b.max() < 1.02)
    f, ax = fig(8, 4.2); screen(ax, 'time (ns)', 'probe output (V)')
    ax.plot(t * 1e9, a, color=TRACE, lw=2, label='15 cm ground lead, 150 nH')
    ax.plot(t * 1e9, b, color=CTG, lw=2, label='ground spring, 10 nH')
    ax.text(20, 1.32, '124 MHz ringing, Q = 2.3', color=TRACE, fontsize=9); ax.text(20, 0.7, 'Q = 0.60, no ringing', color=CTG, fontsize=9)
    ax.legend(loc='lower right', fontsize=9, facecolor='#0d1b24', labelcolor='white'); ax.set_ylim(-0.1, 1.6)
    finish(f, 'b9_probe_ground')

@figure
def b9_tdr():
    v = 2.998e8 / math.sqrt(3.4)
    d = np.linspace(0, 0.25, 1000)
    z = np.where(d < 0.10, 50.0, 60.0)
    z = z - 18 * np.exp(-((d - 0.15) / 0.004) ** 2)
    z = np.where(d > 0.20, 60 + (d - 0.20) * 4000, z)
    z = np.minimum(z, 100)
    rho = (60 - 50) / 110; t = 2 * 0.10 / v
    check('TDR rho %.3f (0.091), 10 cm at %.2f ns (1.23), resolution %.1f mm' % (rho, t * 1e9, v * 35e-12 / 2 * 1e3),
          abs(rho - 0.091) < 0.0005 and abs(t * 1e9 - 1.23) < 0.005 and abs(v * 35e-12 / 2 * 1e3 - 2.8) < 0.05)
    k = 1e-3
    zz = np.convolve(z, np.ones(5) / 5, mode='same'); zz[:3] = 50; zz[-3:] = 100
    f, ax = fig(8, 4.2); screen(ax, 'distance (cm)', 'impedance (Ω)')
    ax.plot(d * 100, zz, color=CTG, lw=2)
    ax.text(1, 52, '50 Ω trace', color='white', fontsize=9); ax.text(10.5, 62, '60 Ω, ρ = +0.091 at 1.23 ns', color='white', fontsize=9)
    ax.text(15.5, 40, 'capacitive via', color='white', fontsize=9); ax.text(20.5, 90, 'open', color='white', fontsize=9)
    ax.set_ylim(30, 102)
    finish(f, 'b9_tdr')

# ---------------------------------------------------------------- Part V
@figure
def b9_awg_sinc():
    fs = 1e9; fr = np.linspace(1e6, 1.5e9, 1500)
    env = 20 * np.log10(np.maximum(np.abs(np.sinc(fr / fs)), 1e-4))
    a = 20 * math.log10(np.sinc(0.4)); b = 20 * math.log10(np.sinc(0.6))
    check('AWG 400 MHz %.2f dB (-2.42), image 600 MHz %.1f dB (-5.9)' % (a, b), abs(a + 2.42) < 0.005 and abs(b + 5.9) < 0.05)
    f, ax = fig(8, 4.2); screen(ax, 'frequency (MHz)', 'level (dB)')
    ax.plot(fr / 1e6, env, '--', color=TRACE, lw=1.3, label='sinc(f/fs) envelope')
    filt = -60 / (1 + np.exp(-(fr - 500e6) / 15e6))
    ax.plot(fr / 1e6, filt, color=GRAY, lw=1.3, label='reconstruction filter')
    ax.vlines(400, -60, a, color=CTG, lw=3); ax.vlines(600, -60, b, color=RED, lw=3)
    ax.text(300, a + 2, '400 MHz: −2.42 dB', color=CTG, fontsize=9); ax.text(620, b + 2, 'image 600 MHz: −5.9 dB', color=RED, fontsize=9)
    ax.set_ylim(-60, 6); ax.legend(loc='lower right', fontsize=8, facecolor='#0d1b24', labelcolor='white')
    finish(f, 'b9_awg_sinc')

@figure
def b9_iq_image():
    sys.path.insert(0, os.path.join(HERE, 'listings'))
    import l20_1_iq_tone as L
    i, q, fs = L.iq_tone(gain_db=0.1, phase_deg=1.0, dc=0.00398, n=200000)
    img, lo = L.levels(i, q, fs)
    check('IQ image %.1f dBc (-39.6), LO %.1f dBc (-45)' % (img, lo), abs(img + 39.6) < 0.05 and abs(lo + 45) < 0.2)
    rng = np.random.default_rng(20); z = i + 1j * q + (rng.normal(0, 1, i.size) + 1j * rng.normal(0, 1, i.size)) * 3e-3
    w = np.hanning(z.size); s = np.fft.fftshift(np.fft.fft(z * w)); fr = np.fft.fftshift(np.fft.fftfreq(z.size, 1 / fs))
    p = 20 * np.log10(np.abs(s) + 1e-30); p -= p.max()
    m = np.abs(fr) < 3e6; fr, p = fr[m], p[m]
    k = 40; nb = p.size // k
    pk = p[: nb * k].reshape(nb, k).max(axis=1); fk = fr[: nb * k].reshape(nb, k).mean(axis=1)
    f, ax = fig(8, 4.2); screen(ax, 'offset from carrier (MHz)', 'level (dBc)')
    ax.plot(fk / 1e6, pk, color=CTG, lw=1.2)
    ax.text(1.1, -5, 'wanted +1 MHz', color=CTG, fontsize=9); ax.text(-2.9, img + 3, 'image −39.6 dBc', color=RED, fontsize=9)
    ax.text(0.1, lo + 3, 'LO leakage −45 dBc', color=TRACE, fontsize=9)
    ax.set_ylim(-100, 6); ax.set_xlim(-3, 3)
    finish(f, 'b9_iq_image')

# ---------------------------------------------------------------- Part VI
def padd(*dbm):
    return 10 * math.log10(sum(10 ** (x / 10) for x in dbm))

@figure
def b9_sa_rbw():
    rng = np.random.default_rng(21); f_ = np.linspace(-0.5, 0.5, 801)
    vals = {}
    fig_, ax = fig(8, 4.4); screen(ax, 'frequency offset (MHz)', 'level (dBm)')
    for rbw, c in ((100e3, RED), (10e3, TRACE), (1e3, CTG)):
        danl = -174 + 24 + 10 * math.log10(rbw)
        shape = np.exp(-0.5 * (f_ * 1e6 / (rbw / 2.355)) ** 2)
        p = 10 * np.log10(10 ** ((danl + rng.normal(0, 0.6, f_.size)) / 10) + 10 ** (-115 / 10) * shape)
        ax.plot(f_, p, color=c, lw=1.1, label='RBW %g kHz, floor %.0f dBm' % (rbw / 1e3, danl))
        vals[rbw] = padd(-115, danl)
    check('tone -115 dBm reads %.1f / %.1f / %.1f dBm' % (vals[100e3], vals[10e3], vals[1e3]),
          abs(vals[100e3] + 99.9) < 0.05 and abs(vals[10e3] + 108.8) < 0.05 and abs(vals[1e3] + 113.8) < 0.05)
    ax.text(0.03, -117, '−113.8 dBm', color=CTG, fontsize=9)
    ax.set_ylim(-130, -90); ax.legend(loc='upper right', fontsize=8, facecolor='#0d1b24', labelcolor='white')
    finish(fig_, 'b9_sa_rbw')

@figure
def b9_emi_scan():
    rng = np.random.default_rng(22); fr = np.logspace(math.log10(30), 3, 1600)
    base = 18 + 14 * np.exp(-((np.log10(fr) - math.log10(150)) / 0.12) ** 2) + rng.normal(0, 1.5, fr.size)
    for fc, lv in ((48, 28), (96, 31), (150, 42), (300, 36), (480, 33), (720, 30)):
        base = np.maximum(base, lv - 60 * np.abs(np.log10(fr / fc)) * 40)
    lim = np.where(fr < 230, 40, 47)
    k = int(np.argmin(abs(fr - 150))); base[k] = 42.0; pk = base[k]
    check('EMI peak at 150 MHz %.1f dBuV/m (42) vs limit 40; QP 37.5 margin %.1f dB' % (pk, 40 - 37.5), abs(pk - 42) < 0.05)
    f, ax = fig(8, 4.4); screen(ax, 'frequency (MHz)', 'field strength (dBµV/m)')
    ax.semilogx(fr, base, color=CTG, lw=1.1, label='peak scan')
    ax.semilogx(fr, lim, color=RED, lw=2, label='CISPR 32 Class B, 3 m (QP)')
    ax.plot(150, 37.5, 'D', color=TRACE, ms=8, label='QP final 37.5 dBµV/m')
    ax.text(160, 44, '42 dBµV/m peak', color='white', fontsize=9)
    ax.set_xticks([30, 50, 100, 200, 300, 500, 1000]); ax.set_xticklabels(['30', '50', '100', '200', '300', '500', '1000']); ax.minorticks_off()
    ax.set_xlim(30, 1000); ax.set_ylim(0, 60); ax.legend(loc='lower right', fontsize=8, facecolor='#0d1b24', labelcolor='white')
    finish(f, 'b9_emi_scan')

@figure
def b9_mismatch():
    vs = np.linspace(1.0, 2.0, 200); gl = (vs - 1) / (vs + 1)
    f, ax = fig(8, 4.2)
    for src, c in ((1.2, GREEN), (1.5, BLUE), (2.0, RED)):
        gs = (src - 1) / (src + 1)
        ax.plot(vs, 20 * np.log10(1 + gs * gl), color=c, lw=2, label='source VSWR %.1f' % src)
        ax.plot(vs, 20 * np.log10(1 - gs * gl), color=c, lw=2)
    p = 0.2 * 0.15 / 2.15; a, b = 20 * math.log10(1 + p), 20 * math.log10(1 - p)
    check('mismatch 1.5/1.15: %+.3f / %+.3f dB' % (a, b), abs(a - 0.120) < 0.0005 and abs(b + 0.122) < 0.0005)
    ax.plot([1.15, 1.15], [a, b], 'o', color=ORANGE)
    ax.annotate('+0.120 / −0.122 dB', (1.15, a), (1.3, 0.6), arrowprops=dict(arrowstyle='->'), fontsize=9)
    ax.axhline(0, color=GRAY, lw=0.8)
    ax.set_xlabel('sensor VSWR'); ax.set_ylabel('mismatch uncertainty (dB)'); ax.set_ylim(-1, 1); ax.legend(loc='lower left', fontsize=9)
    finish(f, 'b9_mismatch')

def pn_model(fo):
    return 10 * np.log10(10 ** -8.0 * (1e3 / fo) ** 3 + 10 ** -10.5 / (1 + (fo / 1e6) ** 4) + 10 ** -15.0)

@figure
def b9_phase_noise():
    fo = np.logspace(2, 7, 1000); L = pn_model(fo)
    m = fo >= 1e3; phi = math.sqrt(2 * np.trapezoid(10 ** (L[m] / 10), fo[m]))
    jit = phi / (2 * math.pi * 1e9) * 1e15
    check('phase noise 1 kHz..10 MHz: %.2f mrad, %.0f fs at 1 GHz' % (phi * 1e3, jit), abs(phi * 1e3 - 8.95) < 0.005 and abs(jit - 1425) < 1)
    fl_chk = 10 * np.log10(10 ** -9.0 * (1e3 / fo) ** 3 + 10 ** -12.0 / (1 + (fo / 1e5) ** 2) + 10 ** -16.0)
    check('device >= 10 dB above floor everywhere: min margin %.1f dB' % (L - fl_chk).min(), (L - fl_chk).min() >= 9.9)
    fl1 = 10 * np.log10(10 ** -9.0 * (1e3 / fo) ** 3 + 10 ** -12.0 / (1 + (fo / 1e5) ** 2) + 10 ** -16.0); fl100 = fl1 - 10
    f, ax = fig(8, 4.4); screen(ax, 'offset frequency (Hz)', 'L(f) (dBc/Hz)')
    ax.semilogx(fo, L, color=CTG, lw=2, label='device, 1 GHz')
    ax.semilogx(fo, fl1, '--', color=GRAY, lw=1.2, label='analyzer floor, 1 correlation')
    ax.semilogx(fo, fl100, ':', color=GRAY, lw=1.4, label='after 100 correlations (−10 dB)')
    ax.text(2e3, -165, '1 kHz..10 MHz: φrms = %.2f mrad, jitter %.0f fs' % (phi * 1e3, jit), color='white', fontsize=9)
    ax.set_ylim(-175, -50); ax.legend(loc='upper right', fontsize=8, facecolor='#0d1b24', labelcolor='white')
    finish(f, 'b9_phase_noise')

# ---------------------------------------------------------------- Part VII
def smith_grid(ax):
    ax.set_aspect('equal'); ax.axis('off')
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color=GRAY, lw=1.2)
    for r in (0.2, 0.5, 1, 2, 5):
        c = r / (1 + r); rad = 1 / (1 + r)
        ax.plot(c + rad * np.cos(t), rad * np.sin(t), color='#b8c4cc', lw=0.7)
        ax.text(c - rad + 0.01, 0.02, '%g' % (r * 50), color=GRAY, fontsize=7)
    for x in (0.2, 0.5, 1, 2, 5):
        for sgn in (1, -1):
            xx = np.linspace(-60, 60, 4000)
            z = 1j * sgn * x + 0 * xx
            zz = np.concatenate([np.linspace(0, 50, 2000)]) + 1j * sgn * x
            g = (zz - 1) / (zz + 1)
            g = g[np.abs(g) <= 1.0001]
            ax.plot(g.real, g.imag, color='#b8c4cc', lw=0.7)
    ax.plot([-1, 1], [0, 0], color='#b8c4cc', lw=0.7)
    fig_ = ax.figure
    patch = plt.Circle((0, 0), 1.0, transform=ax.transData)
    return patch

@figure
def b9_smith():
    f0, R = 2e9, 25.0; fm = 2.3e9
    L = 25 / (2 * math.pi * fm * (1 - (f0 / fm) ** 2)); C = 1 / ((2 * math.pi * f0) ** 2 * L)
    fr = np.linspace(1e9, 3e9, 400); w = 2 * np.pi * fr
    z = R + 1j * (w * L - 1 / (w * C)); g = (z - 50) / (z + 50)
    zm = R + 1j * (2 * math.pi * fm * L - 1 / (2 * math.pi * fm * C)); gm = (zm - 50) / (zm + 50)
    rl = -20 * math.log10(abs(gm)); vs = (1 + abs(gm)) / (1 - abs(gm))
    check('Smith marker Z = %.1f%+.1fj, |G| %.3f at %.1f deg, RL %.1f dB, VSWR %.2f' % (zm.real, zm.imag, abs(gm), math.degrees(np.angle(gm)), rl, vs),
          abs(zm.imag - 25) < 1e-6 and abs(abs(gm) - 0.447) < 0.0005 and abs(math.degrees(np.angle(gm)) - 116.6) < 0.05 and abs(rl - 7.0) < 0.05 and abs(vs - 2.62) < 0.005)
    f, ax = plt.subplots(figsize=(8, 6), dpi=100); f.patch.set_facecolor('white')
    smith_grid(ax)
    ax.plot(g.real, g.imag, color=GREEN, lw=2.4)
    ax.plot(gm.real, gm.imag, 'v', color=RED, ms=10)
    ax.text(gm.real - 0.02, gm.imag + 0.08, '2.3 GHz: 25 + j25 Ω, Γ = 0.447 ∠116.6°, RL 7.0 dB, VSWR 2.62', color=INK, fontsize=9)
    ax.text(g[0].real + 0.03, g[0].imag - 0.08, '1 GHz', color=GREEN, fontsize=8); ax.text(g[-1].real + 0.03, g[-1].imag + 0.03, '3 GHz', color=GREEN, fontsize=8)
    ax.text(-1.1, -1.12, 'series RLC, R = 25 Ω, f0 = 2 GHz, swept 1 to 3 GHz', color=GRAY, fontsize=8)
    ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15)
    finish(f, 'b9_smith')

@figure
def b9_gating():
    t = np.linspace(0, 4, 800); tau = 0.1 / 2.355 * 2
    resp = 0.05 * np.exp(-0.5 * ((t - 0.4) / 0.045) ** 2) + 0.12 * np.exp(-0.5 * ((t - 1.5) / 0.045) ** 2) + 0.06 * np.exp(-0.5 * ((t - 2.6) / 0.045) ** 2)
    rng = np.random.default_rng(26); resp = resp + np.abs(rng.normal(0, 0.0015, t.size))
    gate = ((t > 1.1) & (t < 1.9)).astype(float)
    df = 10e9 / 1600; rng_ns = 1 / df * 1e9; res_ps = 1 / 10e9 * 1e12
    check('gating: range %.0f ns, resolution %.0f ps' % (rng_ns, res_ps), abs(rng_ns - 160) < 1e-6 and abs(res_ps - 100) < 1e-6)
    f, ax = fig(8, 4.2); screen(ax, 'time (ns)', 'reflection (mU)')
    ax.plot(t, resp * 1000, color=GRAY, lw=1.2, label='ungated')
    ax.plot(t, resp * gate * 1000, color=CTG, lw=2, label='gated: device only')
    ax.fill_between(t, 0, gate * 140, color=TRACE, alpha=0.12, step='mid')
    ax.text(0.25, 60, 'connector', color='white', fontsize=9); ax.text(1.35, 130, 'device', color='white', fontsize=9); ax.text(2.45, 70, 'fixture', color='white', fontsize=9)
    ax.text(1.15, 145, 'gate 1.1 to 1.9 ns', color=TRACE, fontsize=9)
    ax.set_ylim(0, 160); ax.legend(loc='upper right', fontsize=8, facecolor='#0d1b24', labelcolor='white')
    finish(f, 'b9_gating')

@figure
def b9_compression():
    pin = np.linspace(-40, 10, 300); G = 20.0; psat = 32.0
    lin = pin + G
    pout = lin - 10 * np.log10(1 + 10 ** ((lin - 21.0) / 10))
    gain = pout - pin
    k = int(np.argmin(abs(gain - (G - 1)))); p1 = pout[k]
    im3 = 3 * (pin + G) - 2 * 25.0
    d = (pin[np.argmin(abs(pin + 20))] + G) - im3[np.argmin(abs(pin + 20))]
    check('compression: P1dB %.1f dBm at Pin %.1f; at 0 dBm tones dIM3 %.1f dB; OIP3 25' % (p1, pin[k], d), abs(d - 50) < 0.2 and abs(p1 - 14.1) < 0.1)
    f, ax = fig(8, 4.6)
    ax.plot(pin, pout, color=BLUE, lw=2, label='fundamental (per tone)')
    ax.plot(pin, lin, '--', color=BLUE, lw=1)
    m = im3 < 32
    ax.plot(pin[m], im3[m], color=RED, lw=2, label='third-order product (3 dB/dB)')
    ax.plot(5, 25, 'o', color=ORANGE); ax.text(-3, 28, 'OIP3 = +25 dBm', fontsize=9)
    ax.plot(pin[k], p1, 's', color=GREEN); ax.text(pin[k] - 14, p1 + 3, 'P1dB %.1f dBm' % p1, fontsize=9, color=GREEN)
    ax.annotate('', (-20, 0), (-20, -50), arrowprops=dict(arrowstyle='<->'))
    ax.text(-19, -27, '50 dB at 0 dBm tones', fontsize=9)
    ax.set_xlabel('input power per tone (dBm)'); ax.set_ylabel('output power (dBm)'); ax.set_ylim(-80, 40); ax.legend(loc='lower right', fontsize=9)
    finish(f, 'b9_compression')

# ---------------------------------------------------------------- Part VIII
def _lst(name):
    sys.path.insert(0, os.path.join(HERE, 'listings'))
    return __import__(name)

@figure
def b9_vsa_block():
    f, ax = canvas(8, 4.2, 100, 52)
    chain = [(1, 'RF in'), (12, 'atten.'), (24, 'mixer'), (37, 'IF filter'), (50, 'ADC'), (63, 'DDC\nNCO, I/Q')]
    for x, t in chain:
        box(ax, x, 30, 9, 7, t, fs=9)
    for (x0, _), (x1, _) in zip(chain[:-1], chain[1:]):
        arrow(ax, x0 + 9.6, 33.5, x1 - 0.6, 33.5)
    box(ax, 24, 12, 9, 6, 'LO', fs=9); arrow(ax, 28.5, 18.6, 28.5, 29.4)
    box(ax, 77, 30, 10, 7, 'capture\nmemory', fs=9); arrow(ax, 72.6, 33.5, 76.4, 33.5)
    outs = [(46, 'spectrum (FFT)'), (33.5, 'analog demod: AM, FM, PM'), (21, 'digital demod: constellation, EVM')]
    for y, t in outs:
        arrow(ax, 87.6, 33.5, 90, y + 3, lw=1)
    for y, t in outs:
        ax.text(90.5, y + 3, t, fontsize=8.5, va='center', ha='left')
    ax.set_xlim(0, 125)
    ax.text(50, 4, 'sample rate set by span (about 1.25 x span); resolution about 1 / record length', ha='center', fontsize=9, color=GRAY)
    check('VSA block: %d chain stages + LO + memory, 3 analyses' % len(chain), len(chain) == 6 and len(outs) == 3)
    finish(f, 'b9_vsa_block')

@figure
def b9_am_fm():
    from scipy.special import jv
    L = _lst('l28_1_fm_deviation')
    z, fs = L.fm_iq(dev=2.405e3, n=400000, snr_db=90)
    d, m = L.demod(z, fs); c = L.carrier_dbc(z)
    check('FM: deviation %.3f kHz (2.405), carrier %.1f dBc (< -40)' % (d / 1e3, c), abs(d - 2405) < 15 and c < -40)
    am_sb = 20 * math.log10(0.5 / 2)
    check('AM m=0.5 sidebands %.2f dBc (-12.04)' % am_sb, abs(am_sb + 12.04) < 0.01)
    f, (a1, a2) = plt.subplots(1, 2, figsize=(8, 4.2), dpi=100)
    screen(a1, 'offset (kHz)', 'level (dBc)'); screen(a2, 'offset (kHz)', 'level (dB, unmodulated carrier = 0)')
    a1.vlines([-1, 0, 1], -100, [am_sb, 0, am_sb], color=CTG, lw=2)
    a1.text(1.1, am_sb + 2, '%.1f dBc' % am_sb, color=CTG, fontsize=9); a1.set_title('AM, m = 0.5', fontsize=10)
    a1.set_xlim(-3, 3); a1.set_ylim(-60, 5)
    n = np.arange(-6, 7); lv = 20 * np.log10(np.abs(jv(n, 2.405)) + 1e-12)
    a2.vlines(n, -100, lv, color=CTG, lw=2); a2.plot([0], [-58], '^', color=RED)
    a2.text(-1.5, -53, 'carrier null', color=RED, fontsize=9); a2.set_title('FM, beta = 2.405 (fm = 1 kHz)', fontsize=10)
    a2.set_xlim(-7, 7); a2.set_ylim(-60, 5)
    f.tight_layout(); finish(f, 'b9_am_fm')

@figure
def b9_constellation():
    L = _lst('l29_1_evm')
    ref = L.qam16(4000); meas = L.impair(ref, 30, 0.81, 0.2)
    pct, db, mer = L.evm(meas, ref); pred, _ = L.budget(30, 0.81, 0.2)
    check('16-QAM EVM %.2f %% vs budget %.2f %%' % (pct, pred), abs(pct - pred) < 0.15 and abs(pct - 3.65) < 0.1)
    f, (a1, a2) = plt.subplots(1, 2, figsize=(8, 4.4), dpi=100)
    screen(a1, 'I', 'Q'); a1.set_aspect('equal')
    a1.plot(meas.real, meas.imag, '.', ms=1.5, color=CTG, alpha=0.6)
    a1.plot(ref.real, ref.imag, '+', ms=8, color=RED, mew=1)
    a1.set_title('16-QAM: EVM %.2f %% (%.1f dB)' % (pct, db), fontsize=10); a1.set_xlim(-1.4, 1.4); a1.set_ylim(-1.4, 1.4)
    # eye diagram: NRZ with raised-cosine edges, noise, and jitter
    rng = np.random.default_rng(292); ui = 64; nb = 400
    bits = rng.integers(0, 2, nb) * 2 - 1
    x = np.repeat(bits, ui).astype(float)
    k = np.hanning(ui // 2); k /= k.sum(); y = np.convolve(x, k, mode='same')
    y += rng.normal(0, 0.12, y.size)
    screen(a2, 'time (UI)', 'amplitude')
    for i in range(10, nb - 2):
        j = int(rng.normal(0, 3))
        seg = y[i * ui - ui // 2 + j: i * ui + 3 * ui // 2 + j]
        a2.plot(np.linspace(-0.5, 1.5, seg.size), seg, color=CTG, lw=0.4, alpha=0.25)
    mid = y[np.arange(12, nb - 2) * ui + ui // 2]; hi, lo = mid[mid > 0], mid[mid < 0]
    q = (hi.mean() - lo.mean()) / (hi.std() + lo.std())
    from scipy.special import erfc
    ber = 0.5 * erfc(q / math.sqrt(2))
    check('eye Q %.1f, BER %.1e (< 1e-12)' % (q, ber), q > 7)
    a2.set_title('Eye: Q = %.1f, BER %.0e' % (q, ber), fontsize=10); a2.set_xlim(-0.5, 1.5)
    f.tight_layout(); finish(f, 'b9_constellation')

@figure
def b9_ccdf():
    L = _lst('l30_1_aclr_ccdf')
    x, bw = L.ofdm()
    f, (a1, a2) = plt.subplots(1, 2, figsize=(8, 4.4), dpi=100)
    screen(a1, 'frequency (channel bandwidths)', 'PSD (dB)'); screen(a2, 'power above average (dB)', 'probability')
    res = {}
    for bo, col in ((8, RED), (12, CTG)):
        y = L.rapp_pa(x, bo); fr, s = L.psd(y); s = 10 * np.log10(s / s.max())
        lo, hi = L.aclr(y, bw); res[bo] = (lo + hi) / 2
        a1.plot(fr / bw, s, color=col, lw=1, label='backoff %d dB: ACLR %.0f dB' % (bo, res[bo]))
    for c in (-1.1, 0, 1.1):
        a1.axvspan(c - 0.5, c + 0.5, color=TRACE, alpha=0.08)
    a1.set_xlim(-2.2, 2.2); a1.set_ylim(-80, 5); a1.legend(fontsize=8, loc='lower center', facecolor='#0d1b24', labelcolor='white')
    check('ACLR %.1f dB at 8 dB, %.1f dB at 12 dB backoff' % (res[8], res[12]), abs(res[8] + 37.6) < 0.3 and abs(res[12] + 50.7) < 0.3)
    xs = np.linspace(0, 12, 200)
    for sig, col, lab in ((x, CTG, 'OFDM in'), (L.rapp_pa(x, 8), RED, 'after PA, 8 dB backoff')):
        p = np.abs(sig) ** 2 / np.mean(np.abs(sig) ** 2); pdb = 10 * np.log10(p + 1e-30)
        a2.semilogy(xs, [(pdb > v).mean() + 1e-9 for v in xs], color=col, lw=1.5, label=lab)
    g = L.ccdf(x)[2]
    check('OFDM PAPR at 0.01 %% %.1f dB (9.7)' % g, abs(g - 9.7) < 0.1)
    a2.axhline(1e-4, color=GRAY, ls='--', lw=0.8); a2.text(0.3, 1.4e-4, '0.01 %', color='white', fontsize=8)
    a2.set_ylim(1e-5, 1.2); a2.legend(fontsize=8, facecolor='#0d1b24', labelcolor='white')
    f.tight_layout(); finish(f, 'b9_ccdf')

@figure
def b9_ofdm_evm():
    L = _lst('l31_1_ofdm_evm')
    k, e, tot = L.run()
    check('OFDM composite EVM %.2f %% (1.23), spur SC %.1f %%' % (tot, e[k == 900][0]), abs(tot - 1.23) < 0.05 and abs(e[k == 900][0] - 5.9) < 0.3)
    f, ax = fig(8, 4.2); screen(ax, 'subcarrier index', 'EVM (%)')
    ax.plot(k, e, '.', ms=1.5, color=CTG)
    ax.axhline(tot, color=TRACE, lw=1); ax.text(-1000, 0.45, 'composite %.2f %% (line)' % tot, color=TRACE, fontsize=9)
    ax.annotate('spur −60 dBc', (900, e[k == 900][0]), (200, 5.0), color=RED, fontsize=9, arrowprops=dict(arrowstyle='->', color=RED))
    ax.text(800, 3.0, 'edges: filter droop', color='white', fontsize=9)
    ax.set_ylim(0, 6.5); ax.set_xlim(-1700, 1700)
    finish(f, 'b9_ofdm_evm')

@figure
def b9_chirp():
    L = _lst('l32_1_chirp_linearity')
    t, z, fs = L.chirp_iq()
    S, res, m, tt = L.linearity(t, z, fs)
    rms = res[m].std()
    check('chirp slope %.3f MHz/us, residual rms %.2f MHz (2.41)' % (S / 1e12, rms / 1e6), abs(S / 1e12 - 99.97) < 0.01 and abs(rms / 1e6 - 2.41) < 0.05)
    f, ax = fig(8, 4.2); screen(ax, 'time (µs)', 'frequency error from fitted line (MHz)')
    ax.plot(tt * 1e6, res / 1e6, color=GRAY, lw=0.6)
    ax.plot(tt[m] * 1e6, res[m] / 1e6, color=CTG, lw=0.8)
    ax.axvspan(tt[m][0] * 1e6, tt[m][-1] * 1e6, color=TRACE, alpha=0.08)
    ax.text(3, 11, 'fit window 2 to 38 µs (90 %% of ramp); rms %.1f MHz = %.2f %% of 4 GHz' % (rms / 1e6, 100 * rms / 4e9), color=TRACE, fontsize=9)
    ax.set_ylim(-15, 14); ax.set_xlim(0, 40)
    finish(f, 'b9_chirp')

# ---------------------------------------------------------------- Part IX
@figure
def b9_emissivity():
    L = _lst('l33_1_thermal')
    e = np.linspace(0.3, 1.0, 36)
    tb = [L.true_temp(60, x, 25) for x in e]; t4 = [L.true_temp(60, x, 25, band=False) for x in e]
    v85, v95 = L.true_temp(60, 0.85, 25), L.true_temp(60, 0.95, 25)
    check('emissivity: 0.85 -> %.1f C (65.3), 0.95 -> %.1f C (61.6)' % (v85, v95), abs(v85 - 65.3) < 0.05 and abs(v95 - 61.6) < 0.05)
    f, ax = fig(8, 4.2)
    ax.plot(e, tb, color=RED, lw=2, label='8 to 14 µm band (what the camera computes)')
    ax.plot(e, t4, '--', color=BLUE, lw=1.5, label='T⁴ approximation')
    for x, v in ((0.85, v85), (0.95, v95)):
        ax.plot(x, v, 'o', color=INK); ax.text(x + 0.01, v - 5, 'ε %.2f: %.1f °C' % (x, v), ha='center', fontsize=9)
    ax.set_xlabel('true emissivity of the surface'); ax.set_ylabel('object temperature (°C)')
    ax.set_title('camera reads 60 °C with emissivity set to 1; reflected 25 °C', fontsize=10)
    ax.legend(fontsize=9); ax.set_ylim(50, 120)
    finish(f, 'b9_emissivity')

@figure
def b9_emc_prescan():
    L = _lst('l33_2_emc_prescan')
    import contextlib, io
    sys.argv = ['x', '--sim']
    with contextlib.redirect_stdout(io.StringIO()):
        fr, e, margin = L.main()
    i = int(np.argmin(margin))
    check('prescan worst margin %.1f dB at %.1f MHz (2.9 at 149.8)' % (margin[i], fr[i] / 1e6), abs(margin[i] - 2.9) < 0.2 and abs(fr[i] - 149.8e6) < 1e6)
    f, ax = fig(8, 4.2)
    ax.semilogx(fr / 1e6, e, color=BLUE, lw=0.8, label='peak detector, AF and cable applied')
    ax.semilogx(fr / 1e6, L.limit_3m_class_b(fr), color=RED, lw=2, label='CISPR 32 Class B, 3 m (QP)')
    ax.semilogx(fr / 1e6, L.limit_3m_class_b(fr) - 6, '--', color=ORANGE, lw=1, label='6 dB precompliance margin')
    ax.annotate('149.8 MHz: %.1f dB margin' % margin[i], (fr[i] / 1e6, e[i]), (300, 42), fontsize=9, arrowprops=dict(arrowstyle='->'))
    ax.set_xlabel('frequency (MHz)'); ax.set_ylabel('field strength (dBµV/m)'); ax.set_ylim(0, 55); ax.set_xlim(30, 1000)
    tk = [30, 50, 100, 200, 300, 500, 1000]; ax.set_xticks(tk); ax.set_xticklabels([str(t) for t in tk]); ax.minorticks_off()
    ax.legend(fontsize=8, loc='lower right')
    finish(f, 'b9_emc_prescan')

# ---------------------------------------------------------------- Part X (Chapters 34 and 36)
@figure
def b9_scpi_layers():
    f, ax = canvas(8, 4.4, 100, 56)
    layers = [('your program: Python, C#, LabVIEW, TestStand', '#e8f1fb'),
              ('driver (optional): IVI-C / IVI.NET, PyMeasure, vendor library', '#eef7ee'),
              ('VISA: NI-VISA, Keysight VISA, R&S VISA, pyvisa-py', '#fdf3e3'),
              ('transport: GPIB, USBTMC, VXI-11, HiSLIP, raw socket', '#f3eefa')]
    for i, (t, c) in enumerate(layers):
        box(ax, 3, 46 - i * 9.5, 52, 6.5, t, fc=c, fs=9)
        if i:
            arrow(ax, 29, 46 - (i - 1) * 9.5 - 0.6, 29, 46 - i * 9.5 + 7.1)
    inst = ['SCPI parser', 'input buffer and command queue', 'output queue', 'status system: STB, ESR, SRQ', 'error queue (SYST:ERR?)']
    box(ax, 63, 4, 34, 49, '', fs=9)
    ax.text(80, 50, 'instrument', ha='center', fontsize=10, fontweight='bold')
    for k, t in enumerate(inst):
        box(ax, 66, 41 - k * 8.4, 28, 5.6, t, fs=8.5)
    arrow(ax, 55.6, 18.8, 65.4, 30.2)
    ax.text(58, 12.5, 'strings and\nbinary blocks', fontsize=8, ha='center')
    check('SCPI layers: 4 host layers, %d instrument blocks' % len(inst), len(layers) == 4 and len(inst) == 5)
    finish(f, 'b9_scpi_layers')

def _thru(n=1000, rtt=2e-3, nplc=1.0, line=60.0, bytes_pt=4, rate=10e6):
    t_int = nplc / line
    single = n * (t_int + rtt)
    buffered = n * t_int + rtt + n * bytes_pt / rate
    return single, buffered

@figure
def b9_throughput():
    cases = [0.02, 0.2, 1.0, 10.0]
    res = [_thru(nplc=c) for c in cases]
    s1, b1 = _thru(nplc=1.0); s2, b2 = _thru(nplc=0.02)
    check('throughput: NPLC 1 %.2f/%.2f s, NPLC 0.02 %.2f/%.3f s' % (s1, b1, s2, b2),
          abs(s1 - 18.67) < 0.01 and abs(b1 - 16.67) < 0.01 and abs(s2 - 2.333) < 0.001 and abs(b2 - 0.336) < 0.001)
    f, ax = fig(8, 4.2)
    x = np.arange(len(cases)); w = 0.38
    ax.bar(x - w / 2, [r[0] for r in res], w, color=ORANGE, label='one query per reading (READ? each point)')
    ax.bar(x + w / 2, [r[1] for r in res], w, color=BLUE, label='buffered: trigger 1000, one binary block')
    for i, (a, b) in enumerate(res):
        ax.text(i - w / 2, a * 1.15, '%.3g s' % a, ha='center', fontsize=8); ax.text(i + w / 2, b * 1.15, '%.3g s' % b, ha='center', fontsize=8)
    ax.set_yscale('log'); ax.set_ylim(0.1, 400); ax.set_xticks(x); ax.set_xticklabels(['NPLC %g' % c for c in cases])
    ax.set_ylabel('time for 1000 readings (s), log scale'); ax.legend(fontsize=8, loc='upper left'); ax.grid(axis='x', visible=False)
    ax.set_title('2 ms round trip per query, 60 Hz line, 10 MB/s transfer', fontsize=10)
    finish(f, 'b9_throughput')

@figure
def b9_cpk():
    L = _lst('l36_1_sequencer')
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        db = L.main(500)
    q = ('SELECT value FROM result r WHERE step=? AND attempt=(SELECT MAX(attempt) FROM result '
         'WHERE serial=r.serial AND step=r.step)')
    v = np.array([r[0] for r in db.execute(q, ('vout',))]); e = np.array([r[0] for r in db.execute(q, ('eff',))])
    cv, ce = L.cpk(v, 3.201, 3.399), L.cpk(e, 88.0, 100.0)
    nf = db.execute("SELECT COUNT(DISTINCT serial) FROM result WHERE step='eff' AND pass=0").fetchone()[0]
    check('Cpk vout %.2f (1.57), eff %.2f (0.82), eff failures %d (11)' % (cv, ce, nf), abs(cv - 1.57) < 0.01 and abs(ce - 0.82) < 0.01 and nf == 11)
    f, (a1, a2) = plt.subplots(1, 2, figsize=(8, 4.2), dpi=100)
    a1.hist(v, bins=30, color=BLUE, alpha=0.8)
    for x, c, ls in ((3.201, RED, '-'), (3.399, RED, '-'), (3.211, ORANGE, '--'), (3.389, ORANGE, '--')):
        a1.axvline(x, color=c, ls=ls, lw=1.5)
    a1.set_title('Vout: Cpk %.2f' % cv, fontsize=10); a1.set_xlabel('output voltage (V)'); a1.set_ylabel('units')
    a2.hist(e, bins=30, color=BLUE, alpha=0.8)
    a2.axvline(88.0, color=RED, lw=1.5, label='spec limit'); a2.axvline(88.3, color=ORANGE, ls='--', lw=1.5, label='test limit (guard band)')
    a2.set_title('efficiency: Cpk %.2f, %d units fail' % (ce, nf), fontsize=10); a2.set_xlabel('efficiency (%)'); a2.legend(fontsize=8)
    f.tight_layout(); finish(f, 'b9_cpk')

# ---------------------------------------------------------------- Part XI
def _rl_band(true_rl, floor_db):
    g, e = 10 ** (-true_rl / 20), 10 ** (floor_db / 20)
    lo = -20 * np.log10(g + e)
    hi = np.where(g > e, -20 * np.log10(np.maximum(g - e, 1e-12)), np.inf)
    return lo, hi

@figure
def b9_vna_floor():
    t = np.linspace(5, 45, 400)
    a = _rl_band(np.array([20.0, 35.0]), -50.0); b = _rl_band(np.array([35.0]), -40.0)
    check('RL 20 dB at -50 floor: %.2f-%.2f; 35 dB: %.1f-%.1f; 35 at -40: %.1f-%.1f' % (a[0][0], a[1][0], a[0][1], a[1][1], b[0][0], b[1][0]),
          abs(a[0][0] - 19.73) < 0.01 and abs(a[1][0] - 20.28) < 0.01 and abs(a[0][1] - 33.6) < 0.05 and abs(a[1][1] - 36.7) < 0.05
          and abs(b[0][0] - 31.1) < 0.05 and abs(b[1][0] - 42.2) < 0.05)
    f, ax = fig(8, 4.2)
    for fl, c, lab in ((-30, RED, 'S11 floor −30 dB (NanoVNA-H4, 0.9 to 1.5 GHz)'), (-40, ORANGE, 'floor −40 dB (LiteVNA 64 above 3 GHz)'),
                       (-50, GREEN, 'floor −50 dB (H4 0.3 to 0.9 GHz, LiteVNA 64 below 3 GHz)')):
        lo, hi = _rl_band(t, fl)
        ax.fill_between(t, lo, np.minimum(hi, 60), color=c, alpha=0.35, lw=0, label=lab)
    ax.plot(t, t, color=INK, lw=1)
    ax.set_xlabel('true return loss (dB)'); ax.set_ylabel('possible measured return loss (dB)')
    ax.set_xlim(5, 45); ax.set_ylim(5, 60); ax.legend(fontsize=8, loc='upper left')
    finish(f, 'b9_vna_floor')

@figure
def b9_mini_tracer():
    L = _lst('l38_1_mini_tracer')
    tr = L.Tracer(L.SimBackend()); rows = tr.family([1.65, 2.65, 3.65])
    va, res, vv, ii, pred = L.early_check(rows, 2.65)
    check('mini tracer: VA %.0f V (76), check point %.3f vs %.3f mA (within 0.2 %%)' % (va, ii * 1e3, pred * 1e3),
          abs(va - 76) < 1.5 and abs(ii - pred) / pred < 0.002)
    f, ax = fig(8, 4.2); screen(ax, 'Vce (V)', 'Ic (mA)')
    for vb in (1.65, 2.65, 3.65):
        pts = [(v, i) for b, v, i, _ in rows if b == vb]
        ax.plot([p[0] for p in pts], [p[1] * 1e3 for p in pts], 'o-', ms=2.5, lw=1, color=CTG)
        ib = np.mean([r[3] for r in rows if r[0] == vb])
        ax.text(pts[-1][0] + 0.05, pts[-1][1] * 1e3, '%.0f µA' % (ib * 1e6), color='white', fontsize=8, va='center')
    ax.axvspan(1.0, 3.0, color=TRACE, alpha=0.08)
    ax.text(1.05, 70, 'fit range 1.0 to 3.0 V: VA = %.0f V' % va, color=TRACE, fontsize=9)
    ax.plot([vv], [ii * 1e3], 's', color=RED, ms=7, mfc='none')
    ax.text(vv - 0.1, ii * 1e3 + 5, 'unused point: %.2f mA, model %.2f mA' % (ii * 1e3, pred * 1e3), color=RED, fontsize=8, ha='right')
    ax.set_xlim(0, 4.3); ax.set_ylim(0, 75)
    finish(f, 'b9_mini_tracer')

if __name__ == '__main__':
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        FIGS[n]()
    print('%d figures written to %s' % (len(names), OUT))
