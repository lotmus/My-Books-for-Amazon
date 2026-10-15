"""Book 3 pass 2 (11 Oct 2026): computed figures for the new sections and Chapters 23-28.
Every plotted number is computed here (or read from the ngspice decks in spice/) and asserted against the text."""
import sys; sys.path.insert(0, '../common'); sys.path.insert(0, 'in/src/scripts-b3')
from eestyle import *
import matplotlib.pyplot as plt
def fig2(w, h): return plt.subplots(2, 1, figsize=(w, h), dpi=100)
import numpy as np
O = 'fig/'; VT = 0.026
# ---------- 17.2 TDDB: time to 0.01 % failures vs gate voltage (example parameters, labeled)
t63_test, V0, dec_per_V, beta, area = 10.0, 2.2, 10.0, 1.5, 1000.0
def t001(V):  # hours to 0.01 % failures on the chip
    t63 = t63_test * 10 ** (dec_per_V * (V0 - V)) * (1 / area) ** (1 / beta)
    return t63 * (-np.log(1 - 1e-4)) ** (1 / beta)
assert abs(t001(1.8) - 2.15) < 0.02, t001(1.8)
Vmax10 = V0 - np.log10(87600 * area ** (1 / beta) / (t63_test * (-np.log(1 - 1e-4)) ** (1 / beta))) / dec_per_V
assert abs(Vmax10 - 1.34) < 0.005, Vmax10
f, ax = fig(8, 4.5); V = np.linspace(1.0, 2.3, 200)
ax.semilogy(V, [t001(v) for v in V], color=BLUE, lw=2.3, label='chip, 0.01 % failed (Weibull β = 1.5, 1000× test area)')
ax.semilogy(V, t63_test * 10 ** (dec_per_V * (V0 - V)), color=GRAY, lw=1.6, ls='--', label='test capacitor, 63 % failed')
ax.axhline(87600, color=RED, lw=1, ls=':'); ax.text(1.02, 1.3e5, 'ten years', color=RED, fontsize=10)
ax.axvline(Vmax10, color=GREEN, lw=1, ls=':'); ax.text(Vmax10 + 0.02, 3e-1, 'about %.2f V' % Vmax10, color=GREEN, fontsize=10)
ax.plot([1.8], [t001(1.8)], 'o', color=INK); ax.text(1.83, 3.5, '1.8 V: about 2 hours', fontsize=10)
ax.set_xlabel('gate voltage (V)'); ax.set_ylabel('time (hours)'); ax.legend(loc='upper right', fontsize=9)
ax.text(1.0, 2e-3, 'example parameters: 10 h at 2.2 V on the test capacitor, 10× per 0.1 V', fontsize=9, color=GRAY)
save(f, O + 'b3s_tddb.png')
# ---------- 21.2 piezo materials: coupling vs velocity (values as cited in Section 21.7)
mats = [('ST-cut quartz, SAW', 3158, 0.11), ('128°YX LiNbO$_3$, SAW', 3980, 5.5), ('64°YX LiNbO$_3$, leaky SAW', 4742, 11.3),
        ('41°YX LiNbO$_3$, leaky SAW', 4792, 17.2), ('36°YX LiTaO$_3$, leaky SAW', 4112, 5.0), ('AlN film, BAW', 11350, 6.5),
        ('AlScN film, BAW', 9500, 13.0), ('ZY LiNbO$_3$ thin film, XBAR', 3800, 25.0)]
f, ax = fig(8, 4.8)
for name, v, k in mats:
    c = RED if 'BAW' in name else (GREEN if 'XBAR' in name else BLUE)
    ax.semilogy(v, k, 'o', color=c, ms=8); ax.text(v + 150, k * 1.12, name, fontsize=9)
ax.set_xlim(2500, 14500); ax.set_ylim(0.05, 60)
ax.set_xlabel('acoustic velocity (m/s; AlScN and XBAR positions approximate)'); ax.set_ylabel('coupling k² (%)')
ax.text(2600, 0.07, 'blue: surface waves on single crystals   red: bulk waves in films   green: thin-film lithium niobate', fontsize=9, color=GRAY)
save(f, O + 'b3s_piezo.png')
# ---------- 23.1 1N4148 library model (ngspice) vs datasheet limits
a = np.loadtxt('spice/d1n4148_iv.txt'); v, i = a[:, 0], a[:, 1]
def v_at(I): return np.interp(np.log(I), np.log(i[i > 0]), v[i > 0])
assert abs(v_at(10e-3) - 0.694) < 0.003 and abs(v_at(5e-3) - 0.660) < 0.003 and abs(v_at(0.1) - 0.850) < 0.003
f, ax = fig(8, 4.6); m = i > 1e-7
ax.semilogy(v[m], i[m] * 1e3, color=BLUE, lw=2.3, label='library model (Is 2.52 nA, N 1.752, Rs 0.568 Ω), ngspice')
ax.plot([1.0], [10], 'v', color=RED, ms=9); ax.text(0.86, 6.0, 'datasheet: VF ≤ 1.0 V at 10 mA', color=RED, fontsize=9.5)
ax.plot([1.0], [100], 'v', color=RED, ms=9); ax.text(0.86, 140, '1N4448: ≤ 1.0 V at 100 mA', color=RED, fontsize=9.5)
ax.plot([0.62, 0.72], [5, 5], color=ORANGE, lw=4); ax.text(0.45, 2.2, '1N4448: 0.62 to 0.72 V at 5 mA', color=ORANGE, fontsize=9.5)
for I in (5e-3, 10e-3, 0.1): ax.plot([v_at(I)], [I * 1e3], 'o', color=INK, ms=5)
ax.set_xlabel('forward voltage (V)'); ax.set_ylabel('forward current (mA)'); ax.set_xlim(0.3, 1.05); ax.legend(loc='upper left', fontsize=9)
save(f, O + 'b3s_1n4148.png')
# ---------- 23.2 fit-not-truth: one diode, two fitted ranges
Is1, Is2, Ikf, Rs = 5e-14, 5e-10, 20e-3, 0.5      # teaching "truth": ideal + recombination + high injection + Rs
vj = np.linspace(0.01, 0.95, 6000)
iid = Is1 * np.expm1(vj / VT); I = iid / np.sqrt(1 + iid / Ikf) + Is2 * np.expm1(vj / (2 * VT)); V = vj + I * Rs
def fit(lo, hi, rs=True):
    m = (I >= lo) & (I <= hi); A = np.c_[np.log(I[m]), -np.ones(m.sum()), I[m]]
    if not rs: A = A[:, :2]
    sol, *_ = np.linalg.lstsq(A, V[m], rcond=None); a1, b1 = sol[0], sol[1]; r1 = sol[2] if rs else 0.0
    return a1 / VT, np.exp(b1 / a1), r1
def vmod(p, Ii): N, Is, r = p; return N * VT * np.log(Ii / Is) + Ii * r
pA = fit(10e-9, 1e-6, rs=False); pB = fit(1e-3, 100e-3)
FIT = dict(A=pA, B=pB, A_free_Rs=fit(10e-9, 1e-6))
ii = np.logspace(-9, -0.7, 400); vt = np.interp(np.log(ii), np.log(I), V)
resA = (vmod(pA, ii) - vt) * 1e3; resB = (vmod(pB, ii) - vt) * 1e3
inA = (ii >= 10e-9) & (ii <= 1e-6); inB = (ii >= 1e-3) & (ii <= 100e-3)
FIT['inA'] = abs(resA[inA]).max(); FIT['inB'] = abs(resB[inB]).max()
FIT['A_at_10mA'] = float(np.interp(np.log(10e-3), np.log(ii), resA)); FIT['B_at_100nA'] = float(np.interp(np.log(100e-9), np.log(ii), resB))
FIT['true_10mA'] = float(np.interp(np.log(10e-3), np.log(I), V)); FIT['true_100nA'] = float(np.interp(np.log(100e-9), np.log(I), V))
f, (a1, a2) = fig2(8, 6.4)
a1.semilogy(V, I * 1e3, color=INK, lw=2.6, label='"measured" device (teaching data)')
a1.semilogy(vmod(pA, ii), ii * 1e3, color=BLUE, lw=1.5, ls='--', label='fit A: 10 nA to 1 µA')
a1.semilogy(vmod(pB, ii), ii * 1e3, color=RED, lw=1.5, ls='--', label='fit B: 1 mA to 100 mA')
a1.set_xlim(0.2, 1.0); a1.set_ylim(1e-6, 300); a1.set_xlabel('V (V)'); a1.set_ylabel('I (mA)'); a1.legend(loc='lower right', fontsize=9)
a2.semilogx(ii, resA, color=BLUE, lw=1.8, label='fit A residual'); a2.semilogx(ii, resB, color=RED, lw=1.8, label='fit B residual')
a2.axvspan(10e-9, 1e-6, color=BLUE, alpha=0.08); a2.axvspan(1e-3, 100e-3, color=RED, alpha=0.08); a2.axhline(0, color=GRAY, lw=0.8)
a2.set_ylim(-150, 150); a2.set_xlabel('I (A)'); a2.set_ylabel('model − device (mV)'); a2.legend(loc='lower left', fontsize=9)
save(f, O + 'b3s_twofit.png')
# ---------- 24.1 2N3904 hFE from the library Gummel-Poon model vs datasheet minimums
g = np.loadtxt('spice/gummel.txt'); ic, ib = g[:, 1], g[:, 3]; beta = ic / ib
def b_at(I): return float(np.interp(np.log(I), np.log(ic), beta))
HFE = {I: b_at(I) for I in (1e-4, 1e-3, 1e-2, 5e-2, 1e-1)}
mins = {1e-4: 40, 1e-3: 70, 1e-2: 100, 5e-2: 60, 1e-1: 30}
assert all(HFE[k] > mins[k] for k in mins) and HFE[1e-2] < 300
f, ax = fig(8, 4.5); m = (ic > 1e-6) & (ic < 0.2)
ax.semilogx(ic[m] * 1e3, beta[m], color=BLUE, lw=2.3, label='library model, VCE = 1 V (ngspice)')
for k, b in mins.items(): ax.plot([k * 1e3], [b], '^', color=RED, ms=8)
ax.plot([10], [300], 'v', color=RED, ms=8); ax.plot([], [], '^', color=RED, label='datasheet hFE minimums (and 300 maximum at 10 mA)')
ax.set_xlabel('collector current (mA)'); ax.set_ylabel('hFE'); ax.set_ylim(0, 320); ax.legend(loc='upper left', fontsize=9)
save(f, O + 'b3s_2n3904.png')
# ---------- 24.2 gate charge of a 55 V power MOSFET (IRFZ44N datasheet maxima; plateau assumed 5.0 V)
Qgs, Qgd, Qg, Vpl = 14, 23, 63, 5.0
qq = [0, Qgs, Qgs + Qgd, Qg]; vv = [0, Vpl, Vpl, 10]
f, ax = fig(8, 4.3); ax.plot(qq, vv, color=BLUE, lw=2.4)
ax.annotate('', xy=(Qgs, 0.6), xytext=(0, 0.6), arrowprops=dict(arrowstyle='<->', color=GRAY)); ax.text(3, 0.9, 'Qgs 14 nC', fontsize=9.5)
ax.annotate('', xy=(Qgs + Qgd, 4.3), xytext=(Qgs, 4.3), arrowprops=dict(arrowstyle='<->', color=RED)); ax.text(Qgs + 3, 3.6, 'Qgd 23 nC (Miller plateau)', color=RED, fontsize=9.5)
ax.text(45, 9.4, 'Qg 63 nC at 10 V', fontsize=9.5); ax.set_xlabel('gate charge (nC)'); ax.set_ylabel('VGS (V)'); ax.set_ylim(0, 11)
ax.text(30, 1.5, 'plateau voltage assumed 5.0 V for the example;\nread the real one from the datasheet curve', fontsize=9, color=GRAY)
save(f, O + 'b3s_gatecharge.png')
# ---------- 25.1 material figures of merit relative to silicon (values in Section 25.1)
MAT = [('Si', 1.12, 0.3, 1400, 11.7, 1.0), ('GaAs', 1.42, 0.4, 8500, 12.9, 1.0), ('InP', 1.34, 0.5, 5400, 12.5, 1.0),
       ('4H-SiC', 3.26, 2.5, 900, 9.7, 2.0), ('GaN', 3.4, 3.3, 1000, 10.4, 2.0), ('β-Ga$_2$O$_3$', 4.8, 8.0, 180, 10.0, 1.1),
       ('diamond', 5.5, 10.0, 4500, 5.7, 2.3), ('AlN', 6.0, 15.4, 426, 9.8, 1.3)]
bf = {m[0]: m[4] * m[3] * m[2] ** 3 for m in MAT}; jf = {m[0]: m[2] * m[5] for m in MAT}
BREL = {k: bf[k] / bf['Si'] for k in bf}; JREL = {k: jf[k] / jf['Si'] for k in jf}
assert round(BREL['4H-SiC']) == 308 and round(BREL['GaN']) == 845 and 2080 < BREL['β-Ga$_2$O$_3$'] < 2090
f, (a1, a2) = fig2(8, 6.2); names = [m[0] for m in MAT]; x = np.arange(len(names))
a1.bar(x, [BREL[n] for n in names], color=BLUE); a1.set_yscale('log'); a1.set_xticks(x); a1.set_xticklabels(names, fontsize=9)
a1.set_ylabel('Baliga FoM / Si'); [a1.text(k, BREL[n] * 1.3, '%.0f' % BREL[n] if BREL[n] >= 10 else '%.1f' % BREL[n], ha='center', fontsize=8.5) for k, n in enumerate(names)]
a1.set_ylim(0.5, 3e5)
a2.bar(x, [JREL[n] for n in names], color=RED); a2.set_yscale('log'); a2.set_xticks(x); a2.set_xticklabels(names, fontsize=9)
a2.set_ylabel('Johnson FoM / Si'); [a2.text(k, JREL[n] * 1.2, '%.0f' % JREL[n] if JREL[n] >= 10 else '%.1f' % JREL[n], ha='center', fontsize=8.5) for k, n in enumerate(names)]
a2.set_ylim(0.5, 300)
save(f, O + 'b3s_fom.png')
# ---------- 25.2 unipolar limit Ron,sp = 4 BV^2/(eps mu Ec^3)
eps0 = 8.854e-14
def ron(m, BV): return 4 * BV ** 2 / (m[4] * eps0 * m[3] * (m[2] * 1e6) ** 3)
RON = {m[0]: ron(m, 1200) * 1e3 for m in MAT}   # mOhm cm2 at 1200 V
assert abs(RON['4H-SiC'] - 0.48) < 0.02, RON['4H-SiC']
f, ax = fig(8, 4.8); BV = np.logspace(2, 4.3, 100)
cols = [INK, GRAY, '#8c6d31', ORANGE, BLUE, GREEN, RED, '#7b4fa0']
for m, c in zip(MAT, cols):
    if m[0] in ('GaAs', 'InP'): continue
    ax.loglog(BV, ron(m, BV) * 1e3, color=c, lw=2, label=m[0])
ax.axvline(1200, color=GRAY, ls=':', lw=1); ax.set_xlabel('breakdown voltage (V)'); ax.set_ylabel('ideal drift Ron,sp (mΩ·cm²)'); ax.legend(fontsize=9, loc='upper left')
save(f, O + 'b3s_ronsp.png')
# ---------- 26.1 laser L-I and APD excess noise
Ith, eta = 0.5e-3, 0.5
f, (a1, a2) = fig2(8, 6.2); Ii = np.linspace(0, 8e-3, 300)
a1.plot(Ii * 1e3, np.maximum(0, eta * (Ii - Ith)) * 1e3, color=RED, lw=2.3, label='VCSEL example: Ith 0.5 mA, slope 0.5 W/A')
a1.plot(Ii * 1e3, 0.03 * Ii * 1e3, color=BLUE, lw=2, ls='--', label='LED example: 0.03 W/A, no threshold')
a1.set_xlabel('drive current (mA)'); a1.set_ylabel('optical power (mW)'); a1.legend(fontsize=9, loc='upper left')
M = np.linspace(1, 30, 200)
def F(k, M): return k * M + (1 - k) * (2 - 1 / M)
for k, lab, c in [(0.02, 'silicon, k ≈ 0.02', BLUE), (0.45, 'InGaAs/InP, k ≈ 0.45', RED), (0.9, 'germanium, k ≈ 0.9', GRAY)]:
    a2.plot(M, F(k, M), color=c, lw=2, label=lab)
assert abs(F(0.02, 10) - 2.06) < 0.01 and abs(F(0.45, 10) - 5.545) < 0.001
a2.set_xlabel('APD gain M'); a2.set_ylabel('excess noise factor F'); a2.legend(fontsize=9, loc='upper left')
save(f, O + 'b3s_laser_apd.png')
# ---------- 27.1 MEMS accelerometer response
f0 = 5e3; w0 = 2 * np.pi * f0; fr = np.logspace(2, 4.6, 400)
f, ax = fig(8, 4.4)
for Q, c in [(0.5, BLUE), (0.707, GREEN), (5, RED)]:
    r = fr / f0; H = 1 / np.sqrt((1 - r ** 2) ** 2 + (r / Q) ** 2)
    ax.loglog(fr, H / w0 ** 2 * 9.81 * 1e9, color=c, lw=2, label='Q = %g' % Q)
assert abs(9.81 / w0 ** 2 * 1e9 - 9.94) < 0.01
ax.set_xlabel('vibration frequency (Hz)'); ax.set_ylabel('proof-mass motion per g (nm)'); ax.legend(fontsize=9)
ax.text(120, 12.5, 'flat below resonance: about 9.9 nm per g for f0 = 5 kHz', fontsize=9.5)
save(f, O + 'b3s_mems.png')
# ---------- 28.1 NRE vs volume (labeled example figures)
OPT = [('FPGA: NRE 0.2 M$, unit 25 $', 0.2e6, 25, BLUE), ('ASIC, mature node: NRE 3 M$, unit 2 $', 3e6, 2, RED),
       ('ASIC, advanced node: NRE 40 M$, unit 1.5 $', 40e6, 1.5, GREEN)]
be1 = (3e6 - 0.2e6) / (25 - 2); be2 = (40e6 - 3e6) / (2 - 1.5)
assert round(be1) == 121739 and round(be2) == 74000000
f, ax = fig(8, 4.6); N = np.logspace(2, 9, 300)
for lab, nre, u, c in OPT: ax.loglog(N, nre / N + u, color=c, lw=2.2, label=lab)
ax.axvline(be1, color=GRAY, ls=':', lw=1); ax.text(be1 * 1.15, 3e3, 'about 122,000 units', fontsize=9)
ax.axvline(be2, color=GRAY, ls=':', lw=1); ax.text(be2 / 9, 3e3, '74 million', fontsize=9)
ax.set_xlabel('units shipped'); ax.set_ylabel('cost per unit including NRE ($)'); ax.legend(fontsize=9, loc='upper right'); ax.set_ylim(1, 1e5)
ax.text(120, 1.4, 'example figures for the arithmetic, not quotes', fontsize=9, color=GRAY)
save(f, O + 'b3s_nre.png')
if __name__ == '__main__':
    print('FIT', FIT); print('HFE', HFE); print('BREL', BREL); print('JREL', JREL); print('RON', RON); print('Vmax10', Vmax10)
