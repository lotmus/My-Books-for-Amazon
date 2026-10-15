"""Book 4 pass 2 (11 Oct 2026): computed figures for new sections (Ch 22, 41) and Chapters 42-52.
Every plotted number is computed here and asserted against the text."""
import sys, math, cmath; sys.path.insert(0, '../common'); sys.path.insert(0, 'scripts')
from eestyle import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
O = 'fig/'; c0 = 2.998e8
def fig2(w, h, **k): return plt.subplots(2, 1, figsize=(w, h), dpi=100, **k)
def box(ax, x, y, w, h, t, fc='#eef3fa', fs=9):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02', fc=fc, ec=INK, lw=1.1))
    ax.text(x + w / 2, y + h / 2, t, ha='center', va='center', fontsize=fs)
def arrow(ax, x1, y1, x2, y2): ax.annotate('', (x2, y2), (x1, y1), arrowprops=dict(arrowstyle='->', lw=1.2, color=INK))
def blank(ax, w, h): ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis('off')
# ---------- Figure 22.2: Ropt vs power; FET and HBT output curves
techs = [('CMOS cascode, 3.3 V', 3.3, 0.5, BLUE), ('GaAs HBT, 3.4 V', 3.4, 0.3, GREEN), ('LDMOS, 28 V', 28, 3, GRAY),
         ('GaN, 28 V', 28, 3, RED), ('GaN, 48 V', 48, 4, ORANGE)]
R = lambda V, k, P: (V - k) ** 2 / (2 * P)
assert abs(R(3.3, .5, 1) - 3.92) < .01 and abs(R(3.4, .3, 1) - 4.805) < .01 and abs(R(28, 3, 1) - 312.5) < .1 and abs(R(48, 4, 1) - 968) < .1
f, (a1, a2) = fig2(8, 8); P = np.logspace(-2, 2.7, 100)
for nm, V, k, c in techs:
    ls = '--' if 'LDMOS' in nm else '-'
    a1.loglog(P, R(V, k, P), color=c, lw=2, ls=ls, label=nm)
a1.axhline(50, color=INK, lw=1, ls=':'); a1.text(0.012, 60, '50 Ω', fontsize=9)
a1.set_xlabel('output power (W)'); a1.set_ylabel('optimum load Ropt (Ω)'); a1.legend(fontsize=8, loc='upper right')
a1.set_title('Ropt = (V − Vknee)²/(2P)', fontsize=10)
vce = np.linspace(0, 6.6, 300)
for k_, (lab, c) in enumerate([('FET', BLUE), ('HBT', GREEN)]):
    for lvl in [0.25, 0.5, 0.75, 1.0]:
        Imax = 2 * 0.5 / (3.3 - (0.5 if lab == 'FET' else 0.3)) * 2 * lvl
        knee = 0.5 if lab == 'FET' else 0.3
        i = Imax * np.tanh(vce / (knee / 2.2)) if lab == 'FET' else Imax * (1 - np.exp(-vce / (knee / 4)))
        a2.plot(vce, i, color=c, lw=1.2, alpha=0.9)
RF = R(3.3, .5, .5); RH = R(3.3, .3, .5); assert abs(RF - 7.84) < .01 and abs(RH - 9.0) < .01
for Rl, k, c, lab in [(RF, .5, BLUE, 'FET load line, %.2f Ω' % RF), (RH, .3, GREEN, 'HBT load line, %.1f Ω' % RH)]:
    a2.plot([k, 3.3, 6.6 - k], [2 * (3.3 - k) / Rl, 0, 0], color=c, lw=2.2, ls='--', label=lab)
a2.set_xlabel('drain or collector voltage (V)'); a2.set_ylabel('current (A)'); a2.legend(fontsize=8); a2.set_ylim(0, 0.9)
a2.text(3.6, 0.6, 'class B, 0.5 W from 3.3 V\nFET knee 0.5 V, HBT knee 0.3 V', fontsize=9, color=GRAY)
save(f, O + 'b4s_ropt_tech.png')
# ---------- class E time-domain simulation (used by Figures 41.2 and 43.1)
def classE(Rf=1.0, VDD=24.0, P=10.0, f0=6.78e6, QL=10.0, cycles=60, n=4000):
    R0 = 0.5768 * VDD ** 2 / P; w = 2 * np.pi * f0; C = 0.1836 / (w * R0); Lx = 1.1525 * R0 / w
    L0 = QL * R0 / w; C0 = 1 / (w ** 2 * L0); Lch = 200 * R0 / w; Rl = R0 * Rf
    dt = 1 / f0 / n; T = 1 / f0
    ich, v, il, vc0 = VDD / R0 * 0.5768 / 0.5768 * 0 + P / VDD, 0.0, 0.0, 0.0
    tt, vv, ii, sw = [], [], [], []
    for k in range(cycles * n):
        t = k * dt; on = (t % T) < T / 2
        # switch on: node shorted
        dich = (VDD - v) / Lch
        dil = (v - vc0 - il * Rl) / (L0 + Lx)
        dvc0 = il / C0
        if on: isw = ich - il; v = 0.0; dv = 0.0
        else: isw = 0.0; dv = (ich - il) / C
        ich += dich * dt; il += dil * dt; vc0 += dvc0 * dt; v = 0.0 if on else max(v + dv * dt, 0.0)
        if k >= (cycles - 2) * n: tt.append(t); vv.append(v); ii.append(isw); sw.append(on)
    tt = np.array(tt); tt -= tt[0]
    return tt * f0, np.array(vv), np.array(ii), R0, C, Lx, np.array(sw)
x, v, isw, R0, C, Lx, sw = classE()
assert abs(R0 - 33.22) < .01 and abs(C * 1e12 - 129.7) < .2 and abs(Lx * 1e6 - 0.899) < .002
vpk = v.max() / 24; i_on = np.where(np.diff(sw.astype(int)) == 1)[0]
v_close = max(v[k] for k in i_on) / 24
print('class E: vpk/VDD %.2f, v at closure/VDD %.3f' % (vpk, v_close))
assert 3.2 < vpk < 3.8 and v_close < 0.15, (vpk, v_close)
E_vpk = vpk
f, (a1, a2) = fig2(8, 7.5)
a1.plot(x, v / 24, color=BLUE, lw=2, label='switch voltage / VDD')
a1.plot(x, isw / (10 / 24), color=RED, lw=2, label='switch current / IDC')
a1.set_xlabel('time (cycles of 6.78 MHz)'); a1.set_ylabel('normalized'); a1.legend(fontsize=9, loc='upper right')
a1.set_title('10 W, 24 V: R = 33.2 Ω, C = 130 pF; peak %.2f VDD' % vpk, fontsize=10)
for Rf, c, lab in [(1.0, BLUE, 'nominal R'), (0.7, ORANGE, '0.7 R'), (1.4, GREEN, '1.4 R')]:
    xx, vv, _, _, _, _, _ = classE(Rf=Rf)
    a2.plot(xx, vv / 24, color=c, lw=1.8, label=lab)
a2.set_xlabel('time (cycles)'); a2.set_ylabel('switch voltage / VDD'); a2.legend(fontsize=9, loc='upper right')
a2.text(0.02, 3.6, 'a moving receiver changes R: zero-voltage switching is lost', fontsize=9, color=GRAY)
save(f, O + 'b4s_classE.png')
# ---------- Figure 41.2: idealized waveforms for 8 classes
th = np.linspace(0, 4 * np.pi, 800); s = np.sin(th)
cc = np.cos(np.radians(60))
W = {'A': (1 - s, 0.5 + 0.5 * s), 'B': (1 - s, np.maximum(s, 0)),
     'C (120°)': (1 - s, np.maximum(s - cc, 0) / (1 - cc)), 'D (voltage mode)': ((s > 0).astype(float), s),
     'F (2nd, 3rd)': (1 - 1.155 * s - 0.1925 * np.sin(3 * th), np.maximum(s, 0)),
     'inverse F': (np.pi * np.maximum(-s, 0), (s > 0).astype(float)),
     'J': ((1 - np.cos(th)) * (1 - np.sin(th)), np.maximum(np.cos(th), 0))}
for k in ['A', 'B', 'C (120°)', 'F (2nd, 3rd)', 'inverse F', 'J']:
    assert abs(W[k][0][:400].mean() - 1) < 0.02, k
xE, vE, iE, *_ = classE()
f, axs = plt.subplots(4, 2, figsize=(8, 9), dpi=100); axs = axs.ravel()
order = ['A', 'B', 'C (120°)', 'D (voltage mode)', 'E', 'F (2nd, 3rd)', 'inverse F', 'J']
for a, k in zip(axs, order):
    if k == 'E': a.plot(xE, vE / 24, color=BLUE, lw=1.6); a.plot(xE, iE / iE.max(), color=RED, lw=1.6)
    else: a.plot(th / (2 * np.pi), W[k][0], color=BLUE, lw=1.6); a.plot(th / (2 * np.pi), W[k][1], color=RED, lw=1.6)
    a.set_title('class ' + k, fontsize=10); a.set_xticks([0, 1, 2]); a.tick_params(labelsize=8)
axs[-1].set_xlabel('cycles'); axs[-2].set_xlabel('cycles')
f.text(0.5, 0.005, 'blue: drain voltage / VDD     red: drain current / its peak', ha='center', fontsize=9, color=GRAY)
save(f, O + 'b4s_waveforms.png')
# ---------- Figure 42.1: CMOS Wi-Fi PA block diagram
Rd = (2 * 2.8) ** 2 / (2 * 0.397); n = math.sqrt(50 / (2 * Rd)); z = 1 / (1 / (Rd / 2) - 1j * 2 * np.pi * 2.45e9 * 1.5e-12)
assert abs(Rd - 39.5) < .1 and abs(n - 0.80) < .01 and abs(z.real - 16.3) < .1 and abs(z.imag - 7.4) < .1
f, ax = fig(8, 4.6); blank(ax, 10, 6)
box(ax, 0.2, 2.6, 1.5, 0.8, 'RF in\n(differential)')
for y, lab in [(4.0, 'core 1'), (1.2, 'core 2')]:
    box(ax, 2.4, y, 2.2, 1.2, 'cascode pair %s\n+ neutralization Cn\n3.3 V, 397 mW' % lab[-1])
    box(ax, 5.3, y + 0.1, 1.5, 1.0, 'transformer\n1 : 0.8')
    arrow(ax, 1.7, 3.0, 2.4, y + 0.6); arrow(ax, 4.6, y + 0.6, 5.3, y + 0.6)
box(ax, 7.5, 2.5, 1.2, 1.0, 'series\nsecondaries')
arrow(ax, 6.8, 4.6, 7.5, 3.2); arrow(ax, 6.8, 1.8, 7.5, 2.8)
box(ax, 9.0, 2.6, 0.9, 0.8, '50 Ω\nant.', fc='#f5e9da'); arrow(ax, 8.7, 3.0, 9.0, 3.0)
box(ax, 2.4, 5.5, 2.2, 0.45, 'APT supply (buck)', fc='#e8f1e4'); arrow(ax, 3.5, 5.5, 3.5, 5.2)
ax.text(5.0, 0.35, 'each side 19.7 Ω; with 1.5 pF absorbed: 16.3 + j7.4 Ω.  28 dBm at the antenna after 1 dB combiner loss', ha='center', fontsize=8.5, color=GRAY)
save(f, O + 'b4s_cmos_pa.png')
# ---------- Figure 45.1: Doherty schematic + efficiency
r = 10 ** (8 / 20) - 1; kf = 44 / 48; xb = 1 / (1 + r)
Pk = 20 * 10 ** .8; Pm = Pk / (1 + r); Rm = 44 ** 2 / (2 * Pm); RL = Rm / (1 + r)
assert abs(r - 1.512) < .001 and abs(Rm - 19.27) < .01 and abs(RL - 7.67) < .01 and abs(RL * (1 + r) / r - 12.74) < .01
def eta_d(x): return np.where(x <= xb, np.pi / 4 * (1 + r) * x, np.pi / 4 * (1 + r) * x ** 2 / ((2 + r) * x - 1)) * kf
bo = np.linspace(-20, 0, 400); xa = 10 ** (bo / 20)
assert abs(eta_d(np.array([xb]))[0] - 0.720) < .002 and abs(eta_d(np.array([1.0]))[0] - 0.720) < .002
f, (a1, a2) = plt.subplots(1, 2, figsize=(9, 4.2), dpi=100, gridspec_kw={'width_ratios': [1.1, 1]})
blank(a1, 6, 5)
box(a1, 0.1, 3.3, 1.2, 0.8, 'splitter\n(90°)'); box(a1, 1.8, 3.5, 1.3, 0.9, 'main\nGaN, AB'); box(a1, 1.8, 0.8, 1.3, 0.9, 'peaking\nGaN, C')
box(a1, 3.5, 3.5, 1.4, 0.9, 'λ/4 inverter\nZT = 19.3 Ω', fc='#f5e9da'); box(a1, 4.7, 1.8, 1.2, 0.8, 'node\n7.67 Ω', fc='#e8f1e4')
arrow(a1, 1.3, 3.8, 1.8, 3.9); arrow(a1, 0.7, 3.3, 1.8, 1.2); arrow(a1, 3.1, 3.95, 3.5, 3.95); arrow(a1, 4.9, 3.95, 5.3, 2.6); arrow(a1, 3.1, 1.25, 4.7, 2.1)
a1.text(0.1, 0.1, 'main sees 19.3 Ω at peak, 48.4 Ω at −8 dB\npeaking sees 12.7 Ω at peak', fontsize=8.5, color=GRAY)
a2.plot(bo, 100 * eta_d(xa), color=RED, lw=2.3, label='Doherty, r = 1.512')
a2.plot(bo, 100 * np.pi / 4 * xa * kf, color=BLUE, lw=2, ls='--', label='class B')
a2.axvline(-8, color=GRAY, lw=1, ls=':'); a2.set_xlabel('output back-off (dB)'); a2.set_ylabel('ideal drain efficiency (%)')
a2.legend(fontsize=9, loc='lower right'); a2.set_ylim(0, 80); a2.text(-7.7, 5, 'average', fontsize=9, color=GRAY)
save(f, O + 'b4s_doherty.png')
# ---------- Figure 46.1: technology map (approximate)
regions = [('LDMOS', 0.3, 3.8, 10, 1500, GRAY), ('GaN on SiC', 0.5, 100, 0.5, 1000, RED), ('GaAs HBT', 0.4, 8, 0.1, 5, GREEN),
           ('GaAs pHEMT', 1, 100, 0.01, 20, '#7a5195'), ('CMOS and RF SOI', 0.1, 300, 0.001, 2, BLUE), ('SiGe', 1, 300, 0.001, 0.5, ORANGE),
           ('InP', 30, 1000, 0.0001, 0.5, '#444444')]
f, ax = fig(8, 5.2)
for nm, f1, f2, p1, p2, c in regions:
    fx = np.logspace(np.log10(f1), np.log10(f2), 50); top = p2 * (fx / f1) ** (-0.9 if nm != 'LDMOS' else -0.3)
    ax.fill_between(fx, p1, np.maximum(top, p1 * 1.5), color=c, alpha=0.18); ax.plot(fx, np.maximum(top, p1 * 1.5), color=c, lw=1.4)
    ax.text(f1 * 1.15, p1 * 1.6 if nm not in ('InP', 'GaN on SiC') else (p1 * 3 if nm == 'InP' else 200), nm, color=c, fontsize=9)
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(0.1, 1200); ax.set_ylim(1e-4, 3000)
ax.set_xlabel('frequency (GHz)'); ax.set_ylabel('saturated output per device (W)')
ax.set_title('approximate regions, 2026; boundaries overlap and move', fontsize=10)
save(f, O + 'b4s_techmap.png')
# ---------- Figure 47.1: BVD resonator and Band 7 ladder
from ladder2 import bvd, ladder
fs = 3.5e9; k2 = 0.07; rr = 4 / np.pi ** 2 * k2; fp = fs / (1 - rr); Cm = 1e-12 * ((fp / fs) ** 2 - 1); Lm = 1 / ((2 * np.pi * fs) ** 2 * Cm)
assert abs(fp / 1e9 - 3.602) < .001 and abs(Cm * 1e15 - 59.2) < .1 and abs(Lm * 1e9 - 34.9) < .1 and abs(2 * np.pi * fs * Lm / 1000 - 0.767) < .002
fr_ = np.linspace(3.3e9, 3.8e9, 4000); Zr = np.abs(bvd(fr_, fs, 1e-12, k2, 1000))
assert abs(fr_[Zr.argmin()] / 1e9 - 3.50) < .003 and abs(fr_[Zr.argmax()] / 1e9 - 3.60) < .005
fse, fsh, Cs, Cp, k2l, Ql = 2.534e9, 2.434e9, 0.81e-12, 1.74e-12, 0.09, 1500
fb = np.linspace(2.5e9, 2.57e9, 141); frx = np.linspace(2.62e9, 2.69e9, 141)
s21b, s11b = ladder(fb, fse, fsh, Cs, Cp, k2l, Ql); s21r, _ = ladder(frx, fse, fsh, Cs, Cp, k2l, Ql)
IL = -20 * np.log10(abs(s21b)); RJ = -20 * np.log10(abs(s21r)); RLs = -20 * np.log10(abs(s11b))
print('ladder IL %.3f..%.3f RL %.2f rej %.3f @2620 %.2f' % (IL.min(), IL.max(), RLs.min(), RJ.min(), RJ[0]))
assert 0.35 < IL.min() < 0.45 and 0.55 < IL.max() < 0.65 and RLs.min() > 12.5 and RJ.min() > 49.5 and 65 < RJ[0] < 69
LAD = (IL.min(), IL.max(), RLs.min(), RJ.min(), RJ[0])
f, (a1, a2) = fig2(8, 7.5)
a1.semilogy(fr_ / 1e9, Zr, color=BLUE, lw=2); a1.set_xlabel('frequency (GHz)'); a1.set_ylabel('|Z| (Ω)')
a1.text(3.51, 2, 'fs = 3.50 GHz', fontsize=9); a1.text(3.61, 2000, 'fp = 3.60 GHz', fontsize=9)
a1.set_title('BAW resonator: kt² = 7 %, C0 = 1 pF, Q = 1000', fontsize=10)
ff = np.linspace(2.35e9, 2.8e9, 3000); s21, _ = ladder(ff, fse, fsh, Cs, Cp, k2l, Ql)
a2.plot(ff / 1e9, 20 * np.log10(abs(s21)), color=RED, lw=2)
a2.axvspan(2.5, 2.57, color=GREEN, alpha=0.15); a2.axvspan(2.62, 2.69, color=BLUE, alpha=0.12)
a2.text(2.503, -75, 'Tx', color=GREEN); a2.text(2.635, -75, 'Rx', color=BLUE); a2.set_ylim(-90, 2)
a2.set_xlabel('frequency (GHz)'); a2.set_ylabel('|S21| (dB)')
a2.set_title('Band 7 Tx ladder, 4 series + 3 shunt: loss %.2f–%.2f dB, Rx rejection ≥ %.0f dB' % (LAD[0], LAD[1], LAD[3]), fontsize=10)
save(f, O + 'b4s_bvd.png')
# ---------- Figure 47.2: front-end module
f, ax = fig(8, 4.6); blank(ax, 10, 6)
box(ax, 0.2, 4.2, 1.6, 0.9, 'PA\nGaAs HBT'); box(ax, 0.2, 2.6, 1.6, 0.9, 'LNA\nSiGe or SOI'); box(ax, 0.2, 1.0, 1.6, 0.9, 'more bands')
box(ax, 2.6, 3.3, 1.9, 1.6, 'duplexer\nBAW / TC-SAW', fc='#f5e9da'); box(ax, 2.6, 1.0, 1.9, 1.3, 'multiplexer\nSAW / XBAR', fc='#f5e9da')
box(ax, 5.3, 2.2, 1.6, 1.8, 'band switch\nRF SOI stack', fc='#e8f1e4'); box(ax, 7.4, 2.5, 1.3, 1.2, 'tuner\nSOI caps', fc='#e8f1e4')
box(ax, 9.0, 2.7, 0.9, 0.8, 'ant.')
for a_, b_ in [((1.8, 4.65), (2.6, 4.4)), ((1.8, 3.05), (2.6, 3.7)), ((1.8, 1.45), (2.6, 1.65)), ((4.5, 4.1), (5.3, 3.5)), ((4.5, 1.65), (5.3, 2.7)), ((6.9, 3.1), (7.4, 3.1)), ((8.7, 3.1), (9.0, 3.1))]:
    arrow(ax, *a_, *b_)
ax.text(5, 0.3, 'one antenna path; a phone repeats it for several antennas and band groups', ha='center', fontsize=9, color=GRAY)
save(f, O + 'b4s_fem.png')
# ---------- Figure 48.1: Smith chart with ATF-54143 noise circles
from touchstone_atf import read_s2p, nf_db, noise_circle
g_opt = 0.27 * cmath.exp(1j * math.radians(120.1)); zo = 50 * (1 + g_opt) / (1 - g_opt)
assert abs(zo.real - 34.5) < .05 and abs(zo.imag - 17.4) < .05
assert abs(nf_db(0, 0.45, g_opt, 2.0) - 0.51) < .005
circ = {}
for nf in (0.6, 0.8, 1.0):
    cen, rad = noise_circle(nf, 0.45, g_opt, 2.0); circ[nf] = (cen, rad)
assert abs(circ[0.6][1] - 0.392) < .001 and abs(circ[1.0][1] - 0.641) < .001
f, ax = fig(6.4, 6.4); ax.set_aspect('equal'); ax.axis('off')
t = np.linspace(0, 2 * np.pi, 400); ax.plot(np.cos(t), np.sin(t), color=INK, lw=1.2)
for rv in [0.2, 0.5, 1, 2, 5]:
    cx, rad = rv / (1 + rv), 1 / (1 + rv); ax.plot(cx + rad * np.cos(t), rad * np.sin(t), color='#cccccc', lw=0.7)
for xv in [0.2, 0.5, 1, 2, 5]:
    for sg in (1, -1):
        pts = cx_ = None
        g = (1j * sg * xv + np.linspace(0, 50, 2000) - 1) / (1j * sg * xv + np.linspace(0, 50, 2000) + 1)
        ax.plot(g.real, g.imag, color='#cccccc', lw=0.7)
ax.plot([-1, 1], [0, 0], color='#cccccc', lw=0.7)
for nf, c in [(0.6, GREEN), (0.8, ORANGE), (1.0, RED)]:
    cen, rad = circ[nf]; ax.plot(cen.real + rad * np.cos(t), cen.imag + rad * np.sin(t), color=c, lw=1.8)
    ang_ = {0.6: 0.5, 0.8: 0.2, 1.0: -0.15}[nf]; ax.text(cen.real + rad * np.cos(ang_) + 0.02, cen.imag + rad * np.sin(ang_), '%.1f dB' % nf, color=c, fontsize=9)
ax.plot(g_opt.real, g_opt.imag, 'o', color=BLUE, ms=7); ax.text(g_opt.real - 0.45, g_opt.imag + 0.07, 'Γopt, 0.45 dB', color=BLUE, fontsize=9)
ax.plot(0, 0, 's', color=INK, ms=6); ax.text(0.04, -0.09, '50 Ω, 0.51 dB', fontsize=9)
w = 2 * np.pi * 2e9; Q = math.sqrt(50 / zo.real - 1); B = Q / 50; Xs = zo.imag + Q * zo.real
assert abs(B / w * 1e12 - 1.07) < .01 and abs(Xs / w * 1e9 - 3.22) < .01
bb = np.linspace(0, B, 100); zz = 1 / (1 / 50 + 1j * bb); gg = (zz - 50) / (zz + 50); ax.plot(gg.real, gg.imag, color=BLUE, lw=2.2)
xs = np.linspace(0, Xs, 100); zz = zz[-1] + 1j * xs; gg2 = (zz - 50) / (zz + 50); ax.plot(gg2.real, gg2.imag, color=BLUE, lw=2.2, ls='--')
assert abs(gg2[-1] - g_opt) < 1e-3
ax.text(-0.95, -0.95, 'solid: shunt 1.07 pF   dashed: series 3.22 nH', fontsize=9, color=BLUE)
ax.set_xlim(-1.08, 1.08); ax.set_ylim(-1.08, 1.08)
save(f, O + 'b4s_smith_atf.png')
# ---------- Figure 49.1: FMCW chirps and block diagram
S = 1e9 / 40e-6; Rt = 50; tau = 2 * Rt / c0; fbeat = S * tau; assert abs(fbeat / 1e6 - 8.34) < .01
f, (a1, a2) = fig2(8, 7.5)
tt = np.linspace(0, 45e-6, 500)
a1.plot(tt * 1e6, np.clip(tt, 0, 40e-6) * S / 1e9 + 77, color=BLUE, lw=2, label='transmitted')
a1.plot(tt * 1e6, np.clip(tt - tau, 0, 40e-6) * S / 1e9 + 77, color=RED, lw=2, ls='--', label='received, 50 m (τ = %.0f ns)' % (tau * 1e9))
a1.set_xlabel('time (µs)'); a1.set_ylabel('frequency (GHz)'); a1.legend(fontsize=9, loc='upper left')
a1.text(22, 77.2, 'beat = S τ = %.2f MHz' % (fbeat / 1e6), fontsize=10)
blank(a2, 10, 5)
box(a2, 0.2, 2.0, 1.8, 1.0, 'ramp synth.\n(fractional-N)'); box(a2, 2.8, 3.4, 1.8, 0.9, '3 × TX chains\n12 dBm'); box(a2, 2.8, 0.7, 1.8, 0.9, '4 × RX LNA\n+ mixer')
box(a2, 5.4, 0.7, 1.6, 0.9, 'IF filter\n≤ 10 MHz'); box(a2, 7.6, 0.7, 1.0, 0.9, 'ADC'); box(a2, 7.6, 2.4, 2.2, 0.9, 'FFT: range,\nDoppler, angle', fc='#e8f1e4')
box(a2, 5.4, 3.4, 1.6, 0.9, 'TX antennas', fc='#f5e9da'); box(a2, 0.2, 0.2, 1.8, 0.9, 'RX antennas', fc='#f5e9da')
for a_, b_ in [((2.0, 2.5), (2.8, 3.8)), ((2.0, 2.5), (2.8, 1.2)), ((4.6, 3.85), (5.4, 3.85)), ((2.0, 0.65), (2.8, 1.0)), ((4.6, 1.15), (5.4, 1.15)), ((7.0, 1.15), (7.6, 1.15)), ((8.1, 1.6), (8.5, 2.4))]:
    arrow(a2, *a_, *b_)
save(f, O + 'b4s_fmcw.png')
# ---------- Figure 50.1: beam squint vs TTD
fr2 = np.linspace(9e9, 11e9, 200); th_ph = np.degrees(np.arcsin(0.5 * 10e9 / fr2))
assert abs(th_ph[0] - 33.75) < .1 and abs(th_ph[-1] - 27.04) < .05
G = (np.pi * 0.01 * 50 / 3) ** 2; assert abs(10 * np.log10(G) + 5.62) < .01
assert abs(0.015 * 0.5 / c0 * 1e12 - 25.0) < .05 and abs(c0 * 25e-12 / 1.468 * 1e3 - 5.1) < .02
f, ax = fig(8, 4.6)
ax.plot(fr2 / 1e9, th_ph, color=RED, lw=2.3, label='phase shifters (set at 10 GHz)'); ax.plot(fr2 / 1e9, 30 + 0 * fr2, color=BLUE, lw=2.3, label='true time delay, 25 ps per element')
ax.set_xlabel('frequency (GHz)'); ax.set_ylabel('beam direction (degrees)'); ax.legend(fontsize=9, loc='lower left'); ax.set_ylim(24, 36)
ins = f.add_axes([0.55, 0.62, 0.42, 0.3]); blank(ins, 10, 3)
for k_, t_ in enumerate(['laser', 'MZM\nVπ 3 V', 'fiber', 'photo-\ndiode']):
    box(ins, 0.2 + 2.5 * k_, 0.8, 2.0, 1.4, t_, fs=8)
    if k_: arrow(ins, 2.5 * k_, 1.5, 0.2 + 2.5 * k_, 1.5)
ins.text(5, 0.1, 'G = (π Idc R / Vπ)² = −5.6 dB at 10 mA', ha='center', fontsize=8)
save(f, O + 'b4s_ttd.png')
# ---------- Figure 51.1: crystal radio tuning and LPF
Lc = 230e-6; Cc = np.linspace(30e-12, 365e-12, 300); fc_ = 1 / (2 * np.pi * np.sqrt(Lc * Cc))
assert abs(fc_[-1] / 1e3 - 549.3) < .5 and abs(fc_[0] / 1e6 - 1.916) < .002
eps2 = 10 ** 0.01 - 1
def att(fq, fcut=7.5e6, nn=7):
    Om = fq / fcut; ch = np.where(Om <= 1, np.cos(nn * np.arccos(np.minimum(Om, 1))), np.cosh(nn * np.arccosh(np.maximum(Om, 1))))
    return 10 * np.log10(1 + eps2 * ch ** 2)
assert abs(att(14.06e6) - 53.1) < .1 and abs(att(21.09e6) - 80.6) < .1
f, (a1, a2) = fig2(8, 7.5)
a1.plot(Cc * 1e12, fc_ / 1e3, color=BLUE, lw=2.3); a1.axhspan(530, 1700, color=GREEN, alpha=0.15); a1.text(250, 1500, 'AM broadcast band', color=GREEN, fontsize=9)
a1.set_xlabel('capacitance (pF)'); a1.set_ylabel('resonant frequency (kHz)'); a1.set_title('230 µH coil: 549 kHz to 1.92 MHz', fontsize=10)
fq = np.linspace(1e6, 30e6, 1000); a2.plot(fq / 1e6, -att(fq), color=RED, lw=2.3)
for fx, lab in [(7.03e6, '7.030 MHz'), (14.06e6, '2nd: −53.1 dB'), (21.09e6, '3rd: −80.6 dB')]:
    a2.axvline(fx / 1e6, color=GRAY, lw=1, ls=':'); a2.text(fx / 1e6 + 0.3, -att(fx) - 6 if fx > 8e6 else -20, lab, fontsize=9)
a2.axhline(-43, color=GREEN, lw=1, ls='--'); a2.text(24, -40, '43 dB rule', color=GREEN, fontsize=9)
a2.set_xlabel('frequency (MHz)'); a2.set_ylabel('filter response (dB)'); a2.set_ylim(-110, 5)
a2.set_title('7-element 0.1 dB Chebyshev low-pass, 7.5 MHz cutoff', fontsize=10)
save(f, O + 'b4s_sdr.png')
# ---------- Figure 52.1: satellite Doppler and radiometer
Re, h, mu = 6371e3, 420e3, 3.986e14; a_ = Re + h; vorb = math.sqrt(mu / a_); w_ = vorb / a_
t = np.linspace(-400, 400, 801); ang = w_ * t
sat = np.stack([a_ * np.sin(ang), a_ * np.cos(ang)]); vel = np.stack([vorb * np.cos(ang), -vorb * np.sin(ang)])
obs = np.array([[0], [Re]]); d = sat - obs; rng = np.linalg.norm(d, axis=0); vr = (d * vel).sum(0) / rng
el = np.degrees(np.arcsin(((d * obs).sum(0) / rng / Re))); vis = el > 0
fd = -145.8e6 * vr / c0
print('max Doppler %.2f kHz, vorb %.0f' % (fd[vis].max() / 1e3, vorb))
assert 3.4e3 < fd[vis].max() < 3.6e3
f, (a1, a2) = fig2(8, 7.5)
a1.plot(t[vis] / 60, fd[vis] / 1e3, color=BLUE, lw=2.3); a1.axhline(0, color=GRAY, lw=0.8)
a1.set_xlabel('time from closest approach (minutes)'); a1.set_ylabel('Doppler shift at 145.8 MHz (kHz)')
a1.set_title('overhead pass, 420 km altitude: ±%.1f kHz' % (fd[vis].max() / 1e3), fontsize=10)
tau_ = np.logspace(-1, 3, 100); dT = 100 / np.sqrt(2.4e6 * tau_); assert abs(100 / math.sqrt(2.4e6 * 10) - 0.0204) < .0005
a2.loglog(tau_, dT, color=RED, lw=2.3); a2.plot([10], [0.0204], 'o', color=INK); a2.text(12, 0.025, '10 s: 0.020 K', fontsize=9)
a2.set_xlabel('integration time (s)'); a2.set_ylabel('ΔTmin (K)'); a2.set_title('Tsys = 100 K, B = 2.4 MHz', fontsize=10)
save(f, O + 'b4s_sky.png')
print('figures done')
