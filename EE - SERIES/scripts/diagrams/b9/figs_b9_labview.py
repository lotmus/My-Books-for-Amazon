"""LabVIEW/TestStand figures written for Book 8 on 11 Oct 2026 and moved to Book 9 (handoff).

Every figure is computed or drawn here from the numbers in the worked examples; CHECK lines
print the values that the captions quote. Run: python figs_b8.py [name ...]  (output in ./fig)
Style: the series' eestyle helpers (imported read-only), 800 px wide, 64-color PNG.
"""
import math
import os
import sys

import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'common'))   # series helpers, read-only
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'scripts', 'diagrams', 'common'))   # from notes\EE9_LABVIEW_handoff_*\figs
sys.path.insert(0, HERE)
from eestyle import BLUE, RED, GREEN, GRAY, ORANGE, INK, fig, save, plt   # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle  # noqa: E402

OUT = os.path.join(HERE, 'fig')
os.makedirs(OUT, exist_ok=True)
LIGHT = {'blue': '#dce8f5', 'green': '#dff0e5', 'orange': '#f8e6d2', 'gray': '#eeeeee', 'red': '#f6d9d5'}
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
            fontweight='bold' if bold else 'normal', color=color, wrap=True)

def arrow(ax, x0, y0, x1, y1, text=None, color=INK, fs=9, off=(0, 1.2), ls='-', rad=0.0, lw=1.3):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=12,
                                 color=color, lw=lw, ls=ls, connectionstyle='arc3,rad=%g' % rad))
    if text:
        ax.text((x0 + x1) / 2 + off[0], (y0 + y1) / 2 + off[1], text, ha='center', va='bottom',
                fontsize=fs, color=color)

def digital(ax, t, v, y0, h=1.0, color=BLUE, lw=1.6):
    """Step waveform: v[i] holds from t[i] to t[i+1]."""
    tt = np.repeat(t, 2)[1:]
    vv = np.repeat(v, 2)[:-1]
    ax.plot(tt, y0 + h * np.asarray(vv, float), color=color, lw=lw, drawstyle='default')

def finish(f, name):
    path = os.path.join(OUT, name + '.png')
    save(f, path)
    from PIL import Image
    w, h = Image.open(path).size
    check('%s.png %dx%d px' % (name, w, h), w == 800)

# ---------------------------------------------------------------- Chapter 23, LabVIEW
WIRE = {'dbl': ORANGE, 'int': BLUE, 'str': '#c2509a', 'bool': GREEN, 'visa': '#6f4a9e', 'err': '#9a7b1c'}

def lv_listings():
    """Import the Chapter 23 listings so the figures use the same model and extraction code."""
    p = os.path.join(HERE, 'listings')
    if not os.path.isdir(p):
        p = os.path.join(HERE, '..', 'listings')
    sys.path.insert(0, p)
    sys.dont_write_bytecode = True          # keep the listings folder free of __pycache__
    import importlib
    return importlib.import_module('l35_2_idvgs_sweep'), importlib.import_module('l35_3_lv_extract')

def lv_data():
    sw, ex = lv_listings()
    out = {}
    for t in (25.0, 75.0, 125.0):
        dut = sw.SimDut(t)
        g, d = sw.SimSmu(dut, 'gate'), sw.SimSmu(dut, 'drain')
        out[t] = {'idvgs': sw.sweep(g, d, sw.steps(0, 5, 0.05), [0.1], 0.0),
                  'vth': sw.sweep(g, d, sw.steps(0, 3, 0.01), None, 0.0),
                  'idvds': sw.sweep(g, d, [4.0, 6.0, 10.0], sw.steps(0, 0.2, 0.01), 0.0)}
    return sw, ex, out

def node(ax, x, y, w, h, text, fc='#f4f4f4', fs=8, ec=INK, bold=False):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=1.1))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, fontweight='bold' if bold else 'normal')

def wire(ax, pts, kind='dbl', lw=2.0, ls='-'):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=WIRE[kind], lw=lw, ls=ls, solid_capstyle='butt', zorder=1)

def frame(ax, x, y, w, h, label, fc='none'):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec='#7a7a7a', lw=4, zorder=0))
    ax.text(x + 0.8, y + h - 0.8, label, fontsize=7.5, color=GRAY, va='top')

@figure
def b9_lv_dataflow():
    c, f1, f2 = 25.0, 1.8, 32.0
    t_nplc, t_bus, settle, pts = 1000 / 60, 2.0, 5.0, 465
    q = t_nplc + t_bus
    ser, par = settle + 2 * q, settle + q
    check('C to F: 25 x 1.8 = %g, + 32 = %g' % (c * f1, c * f1 + f2), c * f1 == 45 and c * f1 + f2 == 77)
    check('query %.1f ms; point %.1f ms serial, %.1f ms parallel; %d points: %.1f s vs %.1f s'
          % (q, ser, par, pts, pts * ser / 1000, pts * par / 1000),
          round(q, 1) == 18.7 and round(ser, 1) == 42.3 and round(par, 1) == 23.7
          and round(pts * ser / 1000, 1) == 19.7 and round(pts * par / 1000, 1) == 11.0)
    f, ax = canvas(8, 4.8, 100, 60)
    # front panel
    ax.add_patch(Rectangle((1, 30), 34, 28, fc='#e9e9e9', ec=INK, lw=1))
    ax.add_patch(Rectangle((1, 55), 34, 3, fc='#c9d6e8', ec=INK, lw=1))
    ax.text(2, 56.5, 'Front panel', fontsize=8, va='center')
    ax.text(4, 50, 'Temperature (\u00b0C)', fontsize=8); node(ax, 4, 44.5, 14, 4, '25.0', fc='white', fs=9)
    ax.text(4, 39, 'Temperature (\u00b0F)', fontsize=8); node(ax, 4, 33.5, 14, 4, '77.0', fc='#e0e0e0', fs=9)
    ax.text(21, 46.5, 'control', fontsize=7.5, color=GRAY); ax.text(21, 35.5, 'indicator', fontsize=7.5, color=GRAY)
    # block diagram
    ax.add_patch(Rectangle((38, 30), 61, 28, fc='white', ec=INK, lw=1))
    ax.add_patch(Rectangle((38, 55), 61, 3, fc='#c9d6e8', ec=INK, lw=1))
    ax.text(39, 56.5, 'Block diagram', fontsize=8, va='center')
    node(ax, 40, 42, 8, 5, '\u00b0C\nDBL', fc='white', ec=ORANGE, fs=7)
    node(ax, 57, 41.5, 6, 6, '\u00d7', fs=12); node(ax, 72, 41.5, 6, 6, '+', fs=12)
    node(ax, 51, 33, 5, 3.5, '1.8', fc='#fff3e6', fs=7.5); node(ax, 66, 33, 5, 3.5, '32', fc='#fff3e6', fs=7.5)
    node(ax, 88, 42, 9, 5, '\u00b0F\nDBL', fc='#f0f0f0', ec=ORANGE, fs=7)
    wire(ax, [(48, 45.5), (57, 45.5)]); wire(ax, [(56, 34.75), (60, 34.75), (60, 41.5)])
    wire(ax, [(63, 44.5), (72, 44.5)]); wire(ax, [(71, 34.75), (75, 34.75), (75, 41.5)])
    wire(ax, [(78, 44.5), (88, 44.5)])
    for x, v in ((52.5, '25'), (67.5, '45'), (83, '77')):
        ax.text(x, 47, v, fontsize=8, color=RED, ha='center')
    ax.text(68.5, 50.5, 'a node runs when all its inputs have arrived (red: data on the wires)', fontsize=7.5, ha='center', color=GRAY)
    # parallelism
    ax.text(1, 25, 'Two wires with no connection between them run in parallel', fontsize=9, fontweight='bold')
    for y, who in ((15, 'drain'), (6, 'gate')):
        node(ax, 3, y, 13, 5.5, 'set Vgs,\nwait 5 ms' if who == 'drain' else '', fc='white', fs=7.5, ec='white' if who == 'gate' else INK)
        node(ax, 22, y, 20, 5.5, 'Query %s "READ?"\n%.1f ms' % (who, q), fc=LIGHT['blue'], fs=7.5)
        wire(ax, [(16, 17.75), (19, 17.75), (19, y + 2.75), (22, y + 2.75)], 'visa', lw=1.6)
        wire(ax, [(42, y + 2.75), (48, y + 2.75), (48, 12.5), (50, 12.5)])
    node(ax, 50, 10, 9, 5, 'Build\nArray', fs=7.5)
    ax.text(62, 17.5, 'dataflow (LabVIEW): %.1f ms per point,\n%d points in %.1f s' % (par, pts, pts * par / 1000), fontsize=8, color=GREEN, va='center')
    ax.text(62, 8.5, 'one call after the other (Listing 35.2):\n%.1f ms per point, %.1f s' % (ser, pts * ser / 1000), fontsize=8, color=RED, va='center')
    finish(f, 'b9_lv_dataflow')

@figure
def b9_lv_patterns():
    rate, block, stall, nbytes = 10000, 1000, 3.0, 8
    per_s = rate / block; queued = per_s * stall; kb = queued * block * nbytes / 1000
    buf = 10000; buf_s = buf / rate
    check('producer %g blocks/s; %g s stall -> %g blocks, %g kB; DAQmx default buffer %d S = %g s'
          % (per_s, stall, queued, kb, buf, buf_s), per_s == 10 and queued == 30 and kb == 240 and buf_s == 1.0)
    f, ax = canvas(8, 4.8, 100, 60)
    ax.text(1, 57, 'State machine', fontsize=9, fontweight='bold')
    frame(ax, 3, 6, 44, 47, 'While Loop')
    node(ax, 1.6, 36, 2.8, 3, '\u25b2', fs=7); node(ax, 45.6, 36, 2.8, 3, '\u25bc', fs=7)
    ax.add_patch(Rectangle((11, 12), 30, 34, fc='none', ec='#8a8a8a', lw=2.5))
    node(ax, 18, 43.5, 16, 4, '\u25c0 "Soak" \u25bc', fc='#eeeeee', fs=8)
    ax.text(26, 33, 'read temperature;\nall of the last 120 s\nwithin \u00b10.2 \u00b0C?', ha='center', fontsize=7.5, va='center')
    ax.text(26, 20, 'yes \u2192 next: "Sweep"\nno \u2192 next: "Soak"', ha='center', fontsize=7.5, va='center', color=BLUE)
    wire(ax, [(4.4, 37.5), (8, 37.5), (8, 45.5), (18, 45.5)], 'int', lw=2)
    wire(ax, [(36, 18.5), (43, 18.5), (43, 37.5), (45.6, 37.5)], 'int', lw=2)
    ax.add_patch(plt.Circle((43, 9.5), 1.6, fc=RED, ec=INK)); ax.text(39.6, 9.5, 'stop', fontsize=7, va='center', ha='right')
    node(ax, 4.5, 7.5, 3, 3, 'i', fc=LIGHT['blue'], fs=8)
    ax.text(25, 1.5, 'Init \u2192 Soak \u2192 Sweep \u2192 Save \u2192 next temperature, or Done', fontsize=7.5, ha='center')
    ax.text(17, 57, '(the shift register \u25b2\u25bc carries the state)', fontsize=7.5, color=GRAY, va='center')
    ax.text(53, 57, 'Producer\u2013consumer', fontsize=9, fontweight='bold')
    frame(ax, 53, 33, 45, 21, 'While Loop: producer')
    node(ax, 56, 38, 17, 9, 'DAQmx Read\n%d samples\n(%.1f s)' % (block, block / rate), fc=LIGHT['green'], fs=7.5)
    node(ax, 79, 38, 15, 9, 'Enqueue\nElement', fc=LIGHT['orange'], fs=7.5)
    wire(ax, [(73, 42.5), (79, 42.5)])
    frame(ax, 53, 4, 45, 21, 'While Loop: consumer')
    node(ax, 56, 9, 15, 9, 'Dequeue\nElement', fc=LIGHT['orange'], fs=7.5)
    node(ax, 77, 9, 17, 9, 'TDMS Write\n(stalls for\n%g s at times)' % stall, fc=LIGHT['blue'], fs=7.5)
    wire(ax, [(71, 13.5), (77, 13.5)])
    arrow(ax, 86.5, 37.5, 63.5, 18.5, color=ORANGE, ls='--', rad=0.0)
    ax.text(77, 27.8, 'queue: %g blocks/s; a %g s stall\nleaves %g blocks, %g kB, waiting' % (per_s, stall, queued, kb), fontsize=7.2, color=INK, ha='center',
            bbox=dict(fc='white', ec='none', pad=0.5))
    ax.text(75.5, 0.8, 'in one loop the stall would overrun the %d-sample DAQmx buffer (%g s)' % (buf, buf_s), fontsize=7, color=RED, ha='center')
    finish(f, 'b9_lv_patterns')

@figure
def b9_lv_sweep_vi():
    sw, ex = lv_listings()
    n = len(sw.steps(0, 5, 0.05))
    check('sweep VI: N = round((5 - 0)/0.05) + 1 = %d points' % n, n == 101)
    f, ax = canvas(8, 4.9, 100, 62)
    for y, name, addr, lim in ((44, 'gate', 'GPIB0::18::INSTR', '1 mA'), (30, 'drain', 'GPIB0::19::INSTR', '250 mA')):
        node(ax, 0.5, y, 13, 4.5, addr, fc='#efe6f7', ec=WIRE['visa'], fs=6.5)
        node(ax, 16, y - 0.5, 8, 5.5, 'VISA\nOpen', fs=7)
        node(ax, 26.5, y - 0.5, 9.5, 5.5, 'Configure\nSMU (%s)' % lim, fc=LIGHT['blue'], fs=6.5)
        wire(ax, [(13.5, y + 2.25), (16, y + 2.25)], 'str', lw=1.4)
        wire(ax, [(24, y + 2.25), (26.5, y + 2.25)], 'visa', lw=2)
    ax.text(18, 53, 'opened and configured\nin parallel', fontsize=7, color=GRAY, ha='center')
    node(ax, 2, 12, 15, 9, 'start 0, stop 5,\nstep 0.05 V', fc='white', ec=ORANGE, fs=7)
    node(ax, 21, 13.5, 13, 6, 'N = %d' % n, fc='#f4f4f4', fs=8, bold=True)
    wire(ax, [(17, 16.5), (21, 16.5)])
    frame(ax, 39, 8, 41, 47, 'For Loop')
    node(ax, 40.5, 49, 4, 3.5, 'N', fc=LIGHT['blue'], fs=8)
    wire(ax, [(34, 16.5), (37, 16.5), (37, 50.75), (40.5, 50.75)], 'int', lw=1.6)
    node(ax, 40.5, 9.5, 3.5, 3.5, 'i', fc=LIGHT['blue'], fs=8)
    node(ax, 47, 9, 13, 6, 'start + i\u00b7step', fs=7.5)
    wire(ax, [(44, 11.25), (47, 11.25)], 'int', lw=1.6)
    node(ax, 47, 41, 14, 7, 'SOUR:VOLT vgs\n(gate)', fc=LIGHT['orange'], fs=7)
    wire(ax, [(60, 12), (62.5, 12), (62.5, 37), (45, 37), (45, 43), (47, 43)])
    node(ax, 64, 41, 13, 7, 'READ? gate\n\u2192 Ig', fc=LIGHT['green'], fs=7)
    node(ax, 64, 25, 13, 7, 'READ? drain\n\u2192 Id', fc=LIGHT['green'], fs=7)
    wire(ax, [(36, 46.25), (47, 46.25)], 'visa'); wire(ax, [(61, 46.25), (64, 46.25)], 'visa')
    wire(ax, [(36, 32.25), (55, 32.25), (55, 28.5), (64, 28.5)], 'visa')
    wire(ax, [(56.5, 41), (56.5, 34.5), (62, 34.5), (62, 30.5), (64, 30.5)], 'err', lw=1.2, ls='--')
    for y, lab in ((44.5, 'Ig[ ]'), (28.5, 'Id[ ]'), (12, 'Vgs[ ]')):
        node(ax, 79, y - 1.5, 2.5, 3, '[ ]', fc='white', fs=5.5)
        ax.text(83, y, lab, fontsize=7.5, va='center')
    wire(ax, [(77, 44.5), (79, 44.5)]); wire(ax, [(77, 28.5), (79, 28.5)]); wire(ax, [(60, 12), (79, 12)])
    node(ax, 88, 46, 11.5, 6, 'Outputs off,\nVISA Close', fs=6.5)
    node(ax, 88, 33, 11.5, 7, 'Python Node\nvth_max_gm', fc='#fff6cc', fs=6.5)
    node(ax, 88, 21, 11.5, 6, 'Id\u2013Vgs\ngraph', fs=6.5)
    node(ax, 88, 9, 11.5, 6, 'TDMS\nWrite', fc=LIGHT['blue'], fs=6.5)
    for yy in (36.5, 24, 12):
        wire(ax, [(86.6, 28.5 if yy != 12 else 12), (86.6, yy), (88, yy)], 'dbl', lw=1.2)
    wire(ax, [(86.6, 12), (86.6, 36.5)], 'dbl', lw=1.2)
    wire(ax, [(36, 46.25), (38, 46.25), (38, 56), (93.75, 56), (93.75, 52)], 'visa', lw=1.4)
    ax.text(59.5, 59.5, 'dashed: error wire, which also orders the steps; [ ]: auto-indexing tunnel', fontsize=7, color=GRAY, ha='center')
    ax.text(59.5, 3, 'Vgs runs from 0 to 5 V in %d points at Vds = 0.1 V (Listing 35.1 is the same VI as text)' % n, fontsize=7, color=GRAY, ha='center')
    finish(f, 'b9_lv_sweep_vi')

@figure
def b9_lv_curves():
    sw, ex, D = lv_data()
    res = {}
    for t in D:
        v = [r[0] for r in D[t]['idvgs']]; i = [r[2] for r in D[t]['idvgs']]
        vth, gm, va = ex.vth_max_gm(v, i, 0.1)
        on = [r for r in D[t]['idvds'] if r[0] == 10.0]
        res[t] = (v, i, vth, gm, va, ex.vth_const_current([r[0] for r in D[t]['vth']], [r[2] for r in D[t]['vth']]),
                  ex.ron_fit([r[1] for r in on], [r[2] for r in on]))
    v25, i25, vth25, gm25, va25, vcc25, ron25 = res[25.0]
    ztc = ex.ztc_point(v25, i25, res[125.0][1])
    check('25 C: Vth(max gm) %.3f V, gm %.1f mS at %.2f V, Vth(1 mA) %.3f V, Ron %.3f ohm; 125 C: Vth %.3f V, Ron %.3f ohm; ZTC %.2f V'
          % (vth25, gm25 * 1e3, va25, vcc25, ron25, res[125.0][2], res[125.0][6], ztc),
          (round(vth25, 3), round(gm25 * 1e3, 1), va25, round(vcc25, 3), round(ron25, 3), round(res[125.0][2], 3),
           round(res[125.0][6], 3), round(ztc, 2)) == (2.084, 22.6, 2.4, 2.161, 1.113, 1.772, 1.689, 2.64))
    f, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.9), dpi=100)
    for t, c in ((25.0, BLUE), (75.0, ORANGE), (125.0, RED)):
        a1.plot(res[t][0], [x * 1e3 for x in res[t][1]], color=c, lw=1.6, label='%.0f \u00b0C' % t)
    x0 = va25 - i25[v25.index(va25)] / gm25
    a1.plot([x0, 4.0], [0, gm25 * (4.0 - x0) * 1e3], color=GRAY, ls='--', lw=1)
    a1.plot([x0], [0], 'o', color=INK, ms=4)
    a1.annotate('intercept %.3f V\nVth = %.3f V\n(minus Vds/2)' % (x0, vth25), (x0, 0), (0.15, 22), fontsize=7.5,
                arrowprops=dict(arrowstyle='-', color=GRAY, lw=0.8))
    iz = np.interp(ztc, v25, i25) * 1e3
    a1.plot([ztc], [iz], 's', color=GREEN, ms=5)
    a1.annotate('ZTC %.2f V' % ztc, (ztc, iz), (3.3, 6), fontsize=7.5, color=GREEN, arrowprops=dict(arrowstyle='-', color=GREEN, lw=0.8))
    a1.set_xlabel('Vgs (V)'); a1.set_ylabel('Id (mA) at Vds = 0.1 V'); a1.set_xlim(0, 5); a1.set_ylim(0, 55)
    a1.legend(fontsize=8, loc='upper left'); a1.set_title('(a) Id\u2013Vgs, linear region', fontsize=10)
    for vg, c in ((4.0, GREEN), (6.0, ORANGE), (10.0, BLUE)):
        rows = [r for r in D[25.0]['idvds'] if r[0] == vg]
        a2.plot([r[1] for r in rows], [r[2] * 1e3 for r in rows], 'o-', ms=2.5, color=c, lw=1.3, label='Vgs = %g V' % vg)
    a2.plot([0, 0.1], [0, 0.1 / ron25 * 1e3], color=INK, ls='--', lw=1)
    a2.text(0.098, 158, 'black dashed: fit up to 0.1 V\nat Vgs = 10 V, Ron = %.2f \u03a9' % ron25, fontsize=7.5)
    a2.set_xlabel('Vds (V)'); a2.set_ylabel('Id (mA), 25 \u00b0C'); a2.set_xlim(0, 0.2); a2.set_ylim(0, 190)
    a2.legend(fontsize=8, loc='upper left'); a2.set_title('(b) Id\u2013Vds, on-resistance', fontsize=10)
    finish(f, 'b9_lv_curves')

@figure
def b9_lv_teststand():
    sw, ex, D = lv_data()
    rows = D[25.0]
    ig5 = [r[3] for r in rows['idvgs'] if r[0] == 5.0][0]
    id5 = [r[2] for r in rows['idvgs'] if r[0] == 5.0][0]
    vcc = ex.vth_const_current([r[0] for r in rows['vth']], [r[2] for r in rows['vth']])
    on = [r for r in rows['idvds'] if r[0] == 10.0]
    ron = ex.ron_fit([r[1] for r in on], [r[2] for r in on])
    steps = [('Gate leakage at Vgs = 5 V', 'Python', 'Igss \u2264 100 nA', '%.0f pA' % (ig5 * 1e12), abs(ig5) <= 100e-9),
             ('Vth at 1 mA, Vds = Vgs', 'LabVIEW', '1.82 to 2.48 V', '%.3f V' % vcc, 1.82 <= vcc <= 2.48),
             ('Id at Vgs = 5 V, Vds = 0.1 V', 'Python', '\u2265 40 mA', '%.1f mA' % (id5 * 1e3), id5 >= 0.040),
             ('Ron at Vgs = 10 V', '.NET', '\u2264 1.49 \u03a9', '%.3f \u03a9' % ron, ron <= 1.49)]
    check('TestStand example: ' + '; '.join('%s %s' % (s[0], s[3]) for s in steps), all(s[4] for s in steps)
          and steps[0][3] == '15 pA' and steps[1][3] == '2.161 V' and steps[2][3] == '49.6 mA' and steps[3][3] == '1.113 \u03a9')
    f, ax = canvas(8, 4.9, 100, 62)
    ax.add_patch(Rectangle((1, 1), 98, 60, fc='#f7f7f7', ec=GRAY, lw=1.2, ls='--'))
    ax.text(2.5, 58.5, 'Process model (Sequential): Test UUTs, repeated for each part', fontsize=8.5, color=GRAY, va='center')
    node(ax, 3, 49, 28, 6, 'PreUUT: scan serial\nnumber "A123"', fc=LIGHT['gray'], fs=7.5)
    node(ax, 69, 49, 28, 6, 'PostUUT: report (XML, HTML,\nATML) and database', fc=LIGHT['gray'], fs=7.5)
    ax.add_patch(Rectangle((3, 4), 94, 42, fc='white', ec=INK, lw=1.2))
    ax.text(4.5, 43.5, 'MainSequence', fontsize=9, fontweight='bold', va='center')
    ax.text(4.5, 38.5, 'Setup', fontsize=8, color=BLUE, va='center')
    ax.text(16, 38.5, 'Init SMUs (VISA)  \u2022  set chuck to 25 \u00b0C and wait for soak', fontsize=7.5, va='center')
    ax.text(4.5, 33, 'Main', fontsize=8, color=BLUE, va='center')
    for k, h in enumerate(('step (Numeric Limit Test)', 'module', 'limits', 'measured', 'result')):
        ax.text((16, 50, 62, 77, 89)[k], 33, h, fontsize=7.5, color=GRAY, va='center')
    for j, (name, mod, lim, val, ok) in enumerate(steps):
        y = 28 - j * 5
        ax.add_patch(Rectangle((15, y - 2.2), 81, 4.4, fc=LIGHT['green'] if ok else LIGHT['red'], ec='none'))
        for k, txt in enumerate((name, mod, lim, val, 'PASS' if ok else 'FAIL')):
            ax.text((16, 50, 62, 77, 89)[k], y, txt, fontsize=7.5, va='center', fontweight='bold' if k == 4 else 'normal')
    ax.text(4.5, 7.5, 'Cleanup', fontsize=8, color=BLUE, va='center')
    ax.text(16, 7.5, 'outputs off  \u2022  close sessions (runs even after a failure or an abort)', fontsize=7.5, va='center')
    arrow(ax, 31, 52, 69, 52, 'the sequence runs between them', fs=7.5, off=(0, 0.8), color=GRAY)
    finish(f, 'b9_lv_teststand')

@figure
def b9_lv_choose():
    cols = ['LabVIEW', 'TestStand', 'Python\n(PyVISA, PyMeasure)', 'C# (.NET)']
    rows = [
        ('Best at', ['bench GUIs, DAQ,\nNI hardware, fast', 'production sequences,\nlimits, reports', 'scripts, analysis,\nplots, automation', 'polished Windows\ntools, large apps']),
        ('Instruments', ['VISA, DAQmx and\nmost vendor drivers', 'calls code written\nin any of the others', 'PyVISA, PyMeasure,\nnidaqmx', 'VISA for .NET,\nvendor libraries']),
        ('User interface', ['front panel comes\nwith every VI', 'operator interface\nincluded', 'more work (Qt,\nweb, notebooks)', 'WPF, WinUI, MAUI\nwith a designer']),
        ('Review, diff, CI', ['graphical diff;\nmerges are hard', 'sequence files;\nown diff tool', 'plain text: git,\nreview, CI', 'plain text: git,\nreview, CI']),
        ('Cost', ['about \u20ac3,000/yr per\nseat; free for hobby', 'development seat +\nlicense per station', 'free', 'free SDK and\nlibraries']),
        ('Weak at', ['large-team review,\ntext tooling', 'analysis and GUIs\non its own', 'operator GUIs,\npackaging', 'fewer instrument\nexamples']),
        ('Choose it when', ['the lab already\nruns NI hardware', 'a line tests many\nparts against limits', 'one engineer, data,\nCI, small budget', 'a product-grade\ntool ships to users']),
    ]
    longest = max(len(line) for _, cells in rows for c in cells for line in c.split('\n'))
    check('comparison: %d criteria x %d tools, longest cell line %d characters' % (len(rows), len(cols), longest),
          all(len(c) == 4 for _, c in rows) and longest <= 22)
    f, ax = canvas(8, 5.6, 100, 70)
    x0, cw, rh = 1, 24.5, 8.6
    xs = [x0 + 17 + k * (cw - 4) for k in range(4)]
    w = cw - 4.6
    for k, c in enumerate(cols):
        ax.add_patch(Rectangle((xs[k], 62), w, 7, fc=LIGHT['blue'], ec='white'))
        ax.text(xs[k] + w / 2, 65.5, c, ha='center', va='center', fontsize=8, fontweight='bold')
    for j, (lab, cells) in enumerate(rows):
        y = 62 - (j + 1) * rh
        ax.add_patch(Rectangle((x0, y), 16.5, rh, fc=LIGHT['gray'], ec='white'))
        ax.text(x0 + 0.8, y + rh / 2, lab, va='center', fontsize=8, fontweight='bold')
        for k, c in enumerate(cells):
            ax.add_patch(Rectangle((xs[k], y), w, rh, fc='#fafafa' if j % 2 else 'white', ec='#dddddd'))
            ax.text(xs[k] + 0.8, y + rh / 2, c, va='center', fontsize=7.5)
    finish(f, 'b9_lv_choose')

if __name__ == '__main__':
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        FIGS[n]()
    print('%d figures written to %s' % (len(names), OUT))
