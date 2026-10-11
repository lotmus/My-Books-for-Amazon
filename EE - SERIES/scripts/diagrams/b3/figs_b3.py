"""Book 3 (Semiconductor Physics and Devices) teaching diagrams, shared EE style. Every number is taken from,
or recomputed with, the book's declared values: VT = 26 mV, ni = 1e10 cm^-3, mun = 1000, mup = 480 cm2/Vs."""
import sys; sys.path.insert(0, '../common')
from eestyle import *
import numpy as np, schemdraw, schemdraw.elements as elm
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon
O = 'fig/'
q = 1.602e-19; eps0 = 8.854e-14; VT = 0.026; ni = 1e10
# ---- 1: bands of metal, semiconductors, insulator (gaps to scale)
f, ax = fig(8, 4.6); ax.grid(False); ax.set_xlim(0, 10.4); ax.set_ylim(-1.2, 12.2); ax.set_xticks([])
ax.set_ylabel('electron energy (eV, gaps to scale)')
cols = [('metal', None), ('Ge', 0.66), ('Si', 1.12), ('GaAs', 1.42), ('insulator\n(SiO$_2$)', 9.0)]
for k, (name, g) in enumerate(cols):
    x = 0.4 + 2.05 * k; w = 1.5
    if g is None:
        ax.add_patch(Rectangle((x, 0), w, 2.2, fc=BLUE, ec=INK, alpha=0.85)); ax.add_patch(Rectangle((x, 1.6), w, 2.2, fc='#dfe9f5', ec=INK))
        ax.text(x + w/2, 4.3, 'bands overlap:\nfree electrons', ha='center', fontsize=9.5)
    else:
        ax.add_patch(Rectangle((x, 0), w, 1.6, fc=BLUE, ec=INK, alpha=0.85)); ax.add_patch(Rectangle((x, 1.6 + g), w, 1.6, fc='#dfe9f5', ec=INK))
        ax.annotate('', xy=(x + w/2, 1.6 + g), xytext=(x + w/2, 1.6), arrowprops=dict(arrowstyle='<->', color=RED, lw=1.3))
        ax.text(x + w/2 + (0.05 if g > 2 else 0), 1.6 + g + 1.9, '%.2f eV' % g if g < 5 else 'about 9 eV', ha='center', color=RED, fontsize=10)
    ax.text(x + w/2, -0.75, name, ha='center', va='top', fontsize=10.5)
ax.text(0.4, 11.6, 'filled band (blue) and empty band (light) for each solid', fontsize=10, color=GRAY)
save(f, O + 'b3_bands.png')
# ---- 2: n and p against donor doping (mass action)
f, ax = fig(8, 4.6); ND = np.logspace(8, 18, 300)
n = ND/2 + np.sqrt(ND**2/4 + ni**2); p = ni**2 / n
ax.loglog(ND, n, color=BLUE, lw=2.2, label='electrons n'); ax.loglog(ND, p, color=RED, lw=2.2, label='holes p = n$_i^2$/n')
ax.axhline(ni, color=GRAY, ls='--', lw=1); ax.text(3e15, 2e9, 'n$_i$ = 10$^{10}$ cm$^{-3}$', color=GRAY, fontsize=10)
ax.plot([1e16, 1e16], [1e4, 1e16], 'o', color=INK, ms=5); ax.text(1.3e16, 1e16, '10$^{16}$', fontsize=10, va='center'); ax.text(1.3e16, 1e4, '10$^{4}$', fontsize=10, va='center')
ax.set_xlabel('donor doping N$_D$ (cm$^{-3}$)'); ax.set_ylabel('concentration (cm$^{-3}$)'); ax.set_ylim(1e1, 1e19); ax.legend(loc='upper left')
ax.text(1e12, 3e2, 'n × p = n$_i^2$ = 10$^{20}$ at every doping', fontsize=10.5)
save(f, O + 'b3_mass_action.png')
# ---- 3: drift velocity saturation
f, ax = fig(8, 4.5); E = np.logspace(2, 6, 300); mu = 1000; vs = 1e7
ax.loglog(E, mu * E, color=GRAY, ls='--', lw=1.5, label='μE (no saturation)')
ax.loglog(E, mu * E / np.sqrt(1 + (mu * E / vs) ** 2), color=BLUE, lw=2.4, label='electrons in silicon (saturating fit)')
ax.axhline(vs, color=RED, lw=1, ls=':'); ax.text(1.2e2, 1.25e7, 'v$_{sat}$ ≈ 1×10$^7$ cm/s', color=RED, fontsize=10)
ax.axvline(1e4, color=GREEN, lw=1, ls=':'); ax.text(1.1e4, 2.2e5, 'crossover v$_{sat}$/μ = 10$^4$ V/cm\n(1 V across 1 µm)', color=GREEN, fontsize=10)
ax.axvline(1e5, color=ORANGE, lw=1, ls=':'); ax.text(1.1e5, 1.5e6, '100 nm channel\nat 1 V', color=ORANGE, fontsize=10)
ax.set_xlim(1e2, 1e6); ax.set_ylim(1e5, 1e9); ax.set_xlabel('electric field (V/cm)'); ax.set_ylabel('drift velocity (cm/s)'); ax.legend(loc='upper left')
save(f, O + 'b3_vsat.png')
# ---- 4: symmetric abrupt junction, depletion approximation (Worked Example 4.1 / Section 4.4)
xn = xp = 0.2155; Vbi = 0.718; es = 11.7 * eps0; Em = q * 1e16 * xn * 1e-4 / es
f, axs = plt.subplots(3, 1, figsize=(8, 7.2), dpi=100, sharex=True); x = np.linspace(-0.4, 0.4, 801)
rho = np.where((x > -xp) & (x < 0), -1, 0) + np.where((x >= 0) & (x < xn), 1, 0)
axs[0].fill_between(x, rho, step='mid', color=BLUE, alpha=0.5); axs[0].plot(x, rho, color=INK, lw=1.2, drawstyle='steps-mid')
axs[0].set_ylabel('charge'); axs[0].set_yticks([-1, 0, 1]); axs[0].set_yticklabels(['−qN$_A$', '0', '+qN$_D$']); axs[0].set_ylim(-1.5, 1.5)
axs[0].text(-0.37, 0.6, 'p side', fontsize=11); axs[0].text(0.28, -0.9, 'n side', fontsize=11)
axs[0].text(-xp / 2, -1.3, 'acceptor ions', ha='center', fontsize=9.5); axs[0].text(xn / 2, 1.12, 'donor ions', ha='center', fontsize=9.5)
Ex = np.where((x > -xp) & (x < 0), -Em * (x + xp) / xp, 0) + np.where((x >= 0) & (x < xn), -Em * (xn - x) / xn, 0)
axs[1].plot(x, Ex / 1e4, color=RED, lw=2.2); axs[1].set_ylabel('field (10$^4$ V/cm)')
axs[1].text(-0.395, -2.6, 'peak 3.3×10$^4$ V/cm at the junction;\nnegative = pointing from n to p', fontsize=9.5, va='center')
V = np.where(x <= -xp, 0, 0) + np.where((x > -xp) & (x < 0), Vbi/2 * ((x + xp) / xp) ** 2, 0) + np.where((x >= 0) & (x < xn), Vbi - Vbi/2 * ((xn - x) / xn) ** 2, 0) + np.where(x >= xn, Vbi, 0)
axs[2].plot(x, V, color=GREEN, lw=2.2); axs[2].set_ylabel('potential (V)'); axs[2].set_xlabel('position (µm), junction at 0')
axs[2].text(0.22, 0.45, 'V$_{bi}$ = 0.718 V', color=GREEN, fontsize=10.5)
for a in axs: a.axvline(-xp, color=GRAY, lw=0.8, ls=':'); a.axvline(xn, color=GRAY, lw=0.8, ls=':')
axs[2].text(-0.395, 0.55, 'W = 0.431 µm\n(0.215 µm each side)', fontsize=9.5, color=GRAY)
save(f, O + 'b3_junction.png')
# ---- 5: diode law on a log scale with series resistance (Worked Examples 5.1 and 5.3)
IS = 1e-15; RS = 10
f, ax = fig(8, 4.8); I = np.logspace(-13, -0.7, 400)
Vj = VT * np.log(I / IS + 1)
ax.semilogy(Vj, I, color=GRAY, ls='--', lw=1.5, label='ideal law, I$_S$ = 1 fA'); ax.semilogy(Vj + I * RS, I, color=BLUE, lw=2.4, label='with 10 Ω series resistance')
for v, i, t in [(0.718, 1e-3, '1 mA at 0.718 V'), (0.878, 1e-2, '10 mA at 0.878 V'), (1.838, 0.1, '100 mA at 1.84 V')]:
    ax.plot(v, i, 'o', color=INK, ms=5); ax.text(v + 0.03, i, t, fontsize=9.5, va='center')
ax.annotate('', xy=(0.52, 4.6e-7), xytext=(0.46, 4.6e-7), arrowprops=dict(arrowstyle='-', color=RED, lw=1.5)); ax.annotate('', xy=(0.52, 4.6e-6), xytext=(0.52, 4.6e-7), arrowprops=dict(arrowstyle='-', color=RED, lw=1.5))
ax.text(0.535, 1.3e-6, '+60 mV gives\n×10 current', color=RED, fontsize=10, va='center')
ax.set_xlim(0.3, 2.1); ax.set_ylim(1e-10, 1.0); ax.set_xlabel('forward voltage (V)'); ax.set_ylabel('current (A)'); ax.legend(loc='lower right')
save(f, O + 'b3_diode_log.png')
# ---- 6: junction capacitance (Worked Example 6.1) and reverse recovery (illustrative)
f, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 4.0), dpi=100)
VR = np.linspace(0, 20, 300); a1.plot(VR, 10 / np.sqrt(1 + VR / 0.718), color=BLUE, lw=2.2)
a1.plot(5, 3.54, 'o', color=INK, ms=5); a1.text(5.6, 4.0, '3.54 pF at 5 V', fontsize=10)
a1.set_xlabel('reverse voltage (V)'); a1.set_ylabel('C$_j$ (pF)'); a1.set_title('Junction capacitance, C$_{j0}$ = 10 pF', fontsize=11); a1.set_ylim(0, 10.5)
t = np.linspace(-50, 300, 700); IF = 1.0; didt = 0.05; t0 = IF / didt; Irr = 0.6; ta = Irr / didt
i_pn = np.where(t < 0, IF, IF - didt * t); i_pn = np.where(t > t0 + ta, -Irr * np.exp(-(t - t0 - ta) / 25), i_pn)
i_sk = np.where(t < 0, IF, np.maximum(IF - didt * t, -0.05)); i_sk = np.where(t > t0 + 1, -0.05 * np.exp(-(t - t0 - 1) / 5), i_sk)
a2.plot(t, i_pn, color=RED, lw=2.2, label='pn diode: stored charge'); a2.plot(t, i_sk, color=GREEN, lw=2.0, ls='--', label='Schottky: almost none')
a2.axhline(0, color=INK, lw=0.8); a2.set_xlabel('time (ns)'); a2.set_ylabel('diode current (A)'); a2.set_title('Turn-off (illustrative shapes)', fontsize=11)
a2.annotate('reverse recovery', xy=(t0 + ta, -Irr), xytext=(t0 + 60, -0.85), fontsize=10, arrowprops=dict(arrowstyle='->', color=INK)); a2.set_ylim(-1.0, 1.2); a2.legend(loc='upper right', fontsize=9)
save(f, O + 'b3_diode_real.png')
# ---- 7: working ranges from Section 7.1
f, (a1, a2) = plt.subplots(1, 2, figsize=(9.4, 3.8), dpi=100)
R1 = [('GaAs', 3, 12, BLUE), ('InP HBT', 1, 3, ORANGE), ('InP HEMT', 1, 5, ORANGE), ('GaN', 20, 50, GREEN)]
for k, (n_, lo, hi, c) in enumerate(R1): a1.barh(k, hi - lo, left=lo, color=c, alpha=0.8, height=0.55); a1.text(hi + 1, k, '%g–%g V' % (lo, hi), va='center', fontsize=9.5)
a1.set_yticks(range(4)); a1.set_yticklabels([r[0] for r in R1]); a1.set_xlim(0, 62); a1.set_xlabel('RF supply voltage (V)'); a1.invert_yaxis()
R2 = [('GaAs', 0.5, 2, BLUE), ('InP', 0.3, 1.5, ORANGE), ('GaN', 5, 12, GREEN)]
for k, (n_, lo, hi, c) in enumerate(R2): a2.barh(k, hi - lo, left=lo, color=c, alpha=0.8, height=0.55); a2.text(hi + 0.3, k, '%g–%g W/mm' % (lo, hi), va='center', fontsize=9.5)
a2.set_yticks(range(3)); a2.set_yticklabels([r[0] for r in R2]); a2.set_xlim(0, 16); a2.set_xlabel('power density (W per mm of gate)'); a2.invert_yaxis()
save(f, O + 'b3_iii_v.png')
# ---- 8: the four bipolar modes
f, ax = fig(7.2, 5.6); ax.grid(False); ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.axhline(0, color=INK, lw=1.2); ax.axvline(0, color=INK, lw=1.2)
ax.set_xticks([]); ax.set_yticks([])
ax.text(0.98, -0.06, 'V$_{BE}$ > 0\n(E-B forward)', ha='right', va='top', fontsize=10); ax.text(0.03, 0.97, 'V$_{BC}$ > 0 (C-B forward)', va='top', fontsize=10)
for (x, y, t, c) in [(0.5, -0.5, 'FORWARD-ACTIVE\nE-B forward, C-B reverse\nthe amplifier: I$_C$ = β I$_B$', '#e3efd9'),
                     (0.5, 0.5, 'SATURATION\nboth junctions forward\nthe closed switch', '#f8e3d0'),
                     (-0.5, -0.5, 'CUTOFF\nboth junctions reverse\nthe open switch', '#e6e6e6'),
                     (-0.5, 0.5, 'REVERSE-ACTIVE\nE-B reverse, C-B forward\npoor gain, mostly by accident', '#dfe9f5')]:
    ax.add_patch(Rectangle((x - 0.47, y - 0.4), 0.94, 0.8, fc=c, ec='none')); ax.text(x, y, t, ha='center', va='center', fontsize=10.5)
ax.text(-0.98, -0.06, 'V$_{BE}$ < 0', va='top', fontsize=10); ax.text(0.03, -0.97, 'V$_{BC}$ < 0', fontsize=10)
save(f, O + 'b3_bjt_modes.png')
# ---- 9: Early effect, IC = IS exp(VBE/VT)(1 + VCE/VA), VA = 100 V
f, ax = fig(8, 4.6); VA = 100
for I0, c in [(0.25, GRAY), (0.5, GREEN), (0.75, ORANGE), (1.0, BLUE)]:
    v = np.linspace(0, 15, 300); ic = I0 * (1 + v / VA) * (1 - np.exp(-v / 0.06))
    ax.plot(v, ic, color=c, lw=2.2); ve = np.linspace(-VA, 0, 50); ax.plot(ve, I0 * (1 + ve / VA), color=c, lw=1, ls='--')
ax.plot(-VA, 0, 'o', color=RED, ms=7); ax.text(-VA + 2, -0.08, '−V$_A$ = −100 V: every extended line meets here', color=RED, fontsize=10)
ax.axvline(0, color=INK, lw=0.8); ax.axhline(0, color=INK, lw=0.8); ax.set_xlim(-105, 16); ax.set_ylim(-0.14, 1.25)
ax.text(1, 1.19, 'slope I$_C$/V$_A$ = 1/r$_o$; r$_o$ = 100 kΩ at 1 mA', fontsize=10)
ax.set_xlabel('V$_{CE}$ (V)'); ax.set_ylabel('I$_C$ (mA)')
save(f, O + 'b3_early.png')
# ---- 10: long-channel MOSFET output characteristics (Worked Example 10.2: k' W/L = 2 mA/V^2)
f, ax = fig(8, 4.6); k = 2e-3
for Vov, c in [(0.1, GRAY), (0.2, BLUE), (0.3, GREEN), (0.4, ORANGE)]:
    v = np.linspace(0, 0.8, 300); i = np.where(v < Vov, k * (Vov * v - v**2 / 2), k / 2 * Vov**2)
    ax.plot(v, i * 1e6, color=c, lw=2.2); ax.text(0.81, k / 2 * Vov**2 * 1e6, 'V$_{ov}$ = %.1f V' % Vov, va='center', fontsize=9.5)
v = np.linspace(0, 0.42, 100); ax.plot(v, k / 2 * v**2 * 1e6, color=RED, ls='--', lw=1.3); ax.text(0.36, 108, 'dashed: V$_{DS}$ = V$_{ov}$,\npinch-off', color=RED, fontsize=10)
ax.plot(0.5, 40, 'o', color=INK, ms=5); ax.text(0.52, 52, '40 µA at V$_{ov}$ = 0.2 V', fontsize=9.5)
ax.text(0.04, 175, 'triode', fontsize=11); ax.text(0.58, 175, 'saturation (amplifying)', fontsize=11)
ax.set_xlim(0, 0.95); ax.set_ylim(0, 190); ax.set_xlabel('V$_{DS}$ (V)'); ax.set_ylabel('I$_D$ (µA)')
save(f, O + 'b3_mos_iv.png')
# ---- 11: planar, fin, nanosheet cross-sections (not to scale)
f, ax = fig(9, 3.9); ax.axis('off'); ax.grid(False); ax.set_xlim(0, 15); ax.set_ylim(-0.9, 5.2); ax.set_aspect('equal')
G = '#c9a227'; S = '#9fb7d8'; OX = '#e9e9e9'
ax.add_patch(Rectangle((0.3, 0), 3.8, 1.2, fc=S, ec=INK)); ax.add_patch(Rectangle((0.8, 1.2), 2.8, 0.18, fc=OX, ec=INK)); ax.add_patch(Rectangle((0.8, 1.38), 2.8, 1.0, fc=G, ec=INK))
ax.text(2.2, 1.88, 'gate', ha='center', fontsize=10); ax.text(2.2, 0.55, 'channel at the top surface', ha='center', fontsize=9)
ax.text(2.2, -0.6, 'planar: gate on one side', ha='center', fontsize=10.5)
ax.add_patch(Rectangle((5.2, 0), 4.0, 0.6, fc=S, ec=INK)); ax.add_patch(Polygon([(6.3, 0.6), (6.3, 3.3), (8.1, 3.3), (8.1, 0.6)], fc=G, ec=INK))
ax.add_patch(Rectangle((6.95, 0.6), 0.5, 2.1, fc=S, ec=INK)); ax.text(7.2, 3.55, 'gate wraps three sides', ha='center', fontsize=9.5)
ax.annotate('', xy=(6.75, 2.7), xytext=(6.75, 0.6), arrowprops=dict(arrowstyle='<->', lw=1)); ax.text(6.0, 1.6, 'H$_{fin}$', fontsize=9.5)
ax.text(7.2, -0.6, 'FinFET: W$_{eff}$ = 2H + W\n50 nm × 2 + 7 nm = 107 nm per fin', ha='center', fontsize=10, va='center')
ax.add_patch(Rectangle((10.4, 0), 4.2, 0.6, fc=S, ec=INK)); ax.add_patch(Rectangle((11.0, 0.6), 3.0, 3.5, fc=G, ec=INK))
for j in range(3): ax.add_patch(Rectangle((11.35, 1.0 + j * 1.0), 2.3, 0.35, fc=S, ec=INK))
ax.text(12.5, 4.4, 'gate on all four sides of each sheet', ha='center', fontsize=9.5)
ax.text(12.5, -0.6, 'nanosheet: W$_{eff}$ = N × 2(W + T)\n3 × 2 × (30 + 5) nm = 210 nm', ha='center', fontsize=10, va='center')
save(f, O + 'b3_fin_sheet.png')
# ---- 12: simple bipolar current mirror (Worked Example 12.1)
def mirror(d):
    Q1 = d.add(elm.BjtNpn(circle=True).reverse().at((0, 0)).label('Q$_1$', 'left'))
    Q2 = d.add(elm.BjtNpn(circle=True).at((4.0, 0)).label('Q$_2$', 'right'))
    d.add(elm.Line().at(Q1.base).to(Q2.base))
    nx = (Q1.base[0] + Q2.base[0]) / 2; d.add(elm.Dot().at((nx, 0)))
    top = Q1.collector[1] + 1.0
    d.add(elm.Line().at(Q1.collector).toy(top)); d.add(elm.Dot().at((Q1.collector[0], top)))
    d.add(elm.Line().at((Q1.collector[0], top)).tox(nx)); d.add(elm.Line().toy(0))
    S = d.add(elm.SourceI().at((Q1.collector[0], top)).up(2.5).reverse())
    d.add(elm.Label().at((S.center[0] - 0.7, S.center[1])).label('I$_{REF}$ = 1 mA', halign='right'))
    d.add(elm.Vdd().label('V$_{CC}$'))
    d.add(elm.Ground().at(Q1.emitter)); d.add(elm.Ground().at(Q2.emitter))
    d.add(elm.Line().at(Q2.collector).up(2.0)); d.add(elm.Dot(open=True).label('I$_{OUT}$ = 0.980 mA\n(to the load)', 'right'))
    d.add(elm.Label().at((2.0, -2.6)).label('same V$_{BE}$, same I$_S$: same current.  I$_{OUT}$ = I$_{REF}$ / (1 + 2/β), β = 100', fontsize=12))
schem(O + 'b3_mirror.png', mirror, unit=2.5, fontsize=13, pad=0.6)
# ---- 13: two-stage op-amp open-loop gain (Worked Examples 13.1, 13.2, 13.4)
f, ax = fig(8, 4.6); fr = np.logspace(0, 8, 500); A0 = 62500; fp1 = 16; fp2 = 2.2e6
A = A0 / np.abs((1 + 1j * fr / fp1) * (1 + 1j * fr / fp2))
ax.semilogx(fr, 20 * np.log10(A), color=BLUE, lw=2.4)
ax.axhline(0, color=INK, lw=0.8); ax.axhline(95.9, color=GRAY, ls=':', lw=1)
ax.text(1.3, 98, 'A$_0$ = 62,500 (95.9 dB)', fontsize=10)
ax.plot(fp1, 95.9 - 3, 'o', color=INK, ms=5); ax.text(fp1 * 1.4, 90, 'dominant pole 16 Hz', fontsize=10)
ax.plot(1e6, 20 * np.log10(A0 / abs((1 + 1j * 1e6 / fp1) * (1 + 1j * 1e6 / fp2))), 'o', color=RED, ms=5); ax.text(1.2e6, 8, 'GBW ≈ 1 MHz\n= g$_{m1}$/(2π C$_c$)', color=RED, fontsize=10)
ax.axvline(fp2, color=ORANGE, ls='--', lw=1); ax.text(fp2 * 1.15, 50, 'second pole\n2.2 MHz\n= g$_{m6}$/(2π C$_L$)', color=ORANGE, fontsize=10)
ax.text(300, 40, '−20 dB per decade', color=BLUE, fontsize=10, rotation=-30)
ax.set_xlim(1, 1e8); ax.set_ylim(-40, 110); ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('open-loop gain (dB)')
save(f, O + 'b3_opamp_bode.png')
# ---- 14: flicker corner (Worked Example 14.4)
f, ax = fig(8, 4.5); fr = np.logspace(0, 5, 400)
ax.loglog(fr, 10 * np.sqrt(1 + 1000 / fr), color=RED, lw=2.3, label='corner 1 kHz')
ax.loglog(fr, 10 * np.sqrt(1 + 250 / fr), color=BLUE, lw=2.3, label='input devices 4× the area: corner 250 Hz')
ax.axhline(10, color=GRAY, ls=':', lw=1); ax.text(1.5e4, 11.5, 'white floor 10 nV/√Hz', color=GRAY, fontsize=10, ha='center')
ax.plot([10, 10], [100.5, 51], 'o', color=INK, ms=5); ax.text(13, 100, '100 nV/√Hz at 10 Hz', fontsize=10, va='center'); ax.text(13, 48, '51 nV/√Hz', fontsize=10, va='center')
ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('input voltage noise (nV/√Hz)'); ax.set_ylim(5, 400); ax.legend(loc='upper right')
save(f, O + 'b3_flicker.png')
# ---- 15: CMOS inverter transfer curve (square law, matched devices, VDD = 1.0 V, |Vth| = 0.3 V)
VDD = 1.0; Vt = 0.3
def In(vi, vo):
    vov = vi - Vt
    if vov <= 0: return 0.0
    return vov**2 / 2 if vo >= vov else vov * vo - vo**2 / 2
def Ip(vi, vo):
    vov = VDD - vi - Vt; vsd = VDD - vo
    if vov <= 0: return 0.0
    return vov**2 / 2 if vsd >= vov else vov * vsd - vsd**2 / 2
vin = np.linspace(0, VDD, 401); vout = []; icur = []
for vi in vin:
    lo, hi = 0.0, VDD
    for _ in range(60):
        m = (lo + hi) / 2
        if In(vi, m) > Ip(vi, m): hi = m
        else: lo = m
    vout.append((lo + hi) / 2); icur.append(In(vi, (lo + hi) / 2))
f, ax = fig(8, 4.6); ax.plot(vin, vout, color=BLUE, lw=2.4, label='output voltage')
ax.plot([0, 1], [0, 1], color=GRAY, ls=':', lw=1); ax.plot(0.5, 0.5, 'o', color=RED, ms=6); ax.text(0.53, 0.53, 'V$_M$ = V$_{DD}$/2 when the PMOS\nis sized μ$_n$/μ$_p$ ≈ 2.1× wider', color=RED, fontsize=10)
ax2 = ax.twinx(); ic = np.array(icur); ax2.plot(vin, ic / ic.max(), color=ORANGE, lw=1.6, ls='--', label='supply current (relative)'); ax2.set_ylim(0, 4); ax2.set_yticks([]); ax2.grid(False)
ax2.spines['right'].set_visible(False)
ax.text(0.02, 0.06, 'NMOS off\nPMOS pulls up', fontsize=9.5); ax.text(0.8, 0.9, 'PMOS off\nNMOS pulls down', fontsize=9.5)
ax.text(0.62, 0.2, 'current flows only\nwhile switching', color=ORANGE, fontsize=9.5)
ax.set_xlabel('input voltage (V), V$_{DD}$ = 1.0 V'); ax.set_ylabel('output voltage (V)'); ax.set_xlim(0, 1); ax.set_ylim(-0.02, 1.05)
save(f, O + 'b3_inverter.png')
# ---- 16: one-transistor DRAM cell and charge sharing (Worked Example 16.2)
def dram(d):
    T = d.add(elm.NFet().reverse().at((0, 0)))
    d.add(elm.Line().at(T.gate).left(2.0)); d.add(elm.Dot(open=True).label('word line', 'left'))
    d.add(elm.Line().at(T.drain).up(1.0)); BL = d.add(elm.Dot())
    d.add(elm.Line().at(BL.center).right(2.5)); d.add(elm.Dot(open=True).label('bit line: C$_{bl}$ = 100 fF,\nprecharged to 0.5 V', 'right'))
    d.add(elm.Line().at(BL.center).left(2.5))
    d.add(elm.Line().at(T.source).down(1.0)); C = d.add(elm.Capacitor().down())
    d.add(elm.Ground())
    d.add(elm.Label().at((C.center[0] + 0.5, C.center[1])).label('C$_s$ = 20 fF\n1.0 V stores a "1"', halign='left'))
    d.add(elm.Label().at((1.0, -7.0)).label('read: ΔV$_{bl}$ = (1.0 − 0.5) × 20 / (20 + 100) = 83 mV', fontsize=12))
schem(O + 'b3_dram.png', dram, unit=2.5, fontsize=12, pad=0.8)
# ---- 17: human-body-model ESD pulse (Section 17.1)
f, ax = fig(8, 4.4); t = np.linspace(0, 800, 600); Ip0 = 2000 / 1500
ax.plot(t, Ip0 * np.exp(-t / 150), color=RED, lw=2.4)
ax.axvline(150, color=GRAY, ls=':', lw=1); ax.text(158, 0.95, 'τ = 1.5 kΩ × 100 pF = 150 ns', fontsize=10)
ax.plot(0, Ip0, 'o', color=INK, ms=5); ax.text(15, Ip0, 'peak 2 kV / 1.5 kΩ = 1.33 A', fontsize=10, va='center')
ax.plot(150, Ip0 / np.e, 'o', color=INK, ms=4); ax.text(158, Ip0 / np.e - 0.08, '37 % of peak', fontsize=9.5)
ax.text(420, 0.6, 'human-body model:\n100 pF charged to 2 kV,\ndischarged through 1.5 kΩ\ninto the pin', fontsize=10, color=GRAY)
ax.set_xlabel('time (ns)'); ax.set_ylabel('current into the pin (A)'); ax.set_xlim(0, 800); ax.set_ylim(0, 1.5)
save(f, O + 'b3_hbm.png')
# ---- 18: solar cell I-V and power (Worked Example 18.5)
IS2 = 1e-12; IL = 35e-3; V = np.linspace(0, 0.66, 500)
f, ax = fig(8, 4.6); I1 = IL - IS2 * (np.exp(V / VT) - 1); I2 = IL / 2 - IS2 * (np.exp(V / VT) - 1)
ax.plot(V, I1 * 1e3, color=BLUE, lw=2.4, label='full sun, I$_L$ = 35 mA'); ax.plot(V, I2 * 1e3, color=BLUE, lw=1.6, ls='--', label='half the light')
P = V * I1; k = np.argmax(P); ax.plot(V[k], I1[k] * 1e3, 'o', color=RED, ms=6)
ax.text(V[k] - 0.3, I1[k] * 1e3 - 4, 'maximum power %.0f mW\nat %.2f V' % (P[k] * 1e3, V[k]), color=RED, fontsize=10)
ax.plot([0.631, 0.613], [0, 0], 'o', color=INK, ms=5); ax.text(0.5, 2, 'V$_{oc}$ 0.613 / 0.631 V', fontsize=9.5)
ax.set_xlim(0, 0.68); ax.set_ylim(0, 40); ax.set_xlabel('cell voltage (V)'); ax.set_ylabel('current delivered (mA)'); ax.legend(loc='lower left')
save(f, O + 'b3_solar.png'); print('solar MPP', V[k], P[k])
# ---- 19: drift-region trade-off, Ron,sp = 4 BV^2 / (eps mu Ec^3) (Section 19.2)
f, ax = fig(8, 4.6); BV = np.logspace(np.log10(50), np.log10(3000), 200)
def ron(BV, er, mu, Ec): return 4 * BV**2 / (er * eps0 * mu * Ec**3) * 1e3
ax.loglog(BV, ron(BV, 11.7, 1000, 3e5), color=BLUE, lw=2.4, label='silicon (E$_c$ = 3×10$^5$ V/cm)')
ax.loglog(BV, ron(BV, 9.7, 900, 2.5e6), color=GREEN, lw=2.4, label='4H-SiC (E$_c$ = 2.5×10$^6$ V/cm)')
ax.plot(600, ron(600, 11.7, 1000, 3e5), 'o', color=INK, ms=5); ax.text(640, ron(600, 11.7, 1000, 3e5) * 0.75, '600 V: 51 mΩ·cm²', fontsize=10, va='top')
ax.plot(1200, ron(1200, 9.7, 900, 2.5e6), 'o', color=INK, ms=5); ax.text(1250, ron(1200, 9.7, 900, 2.5e6) * 0.75, '1200 V: 0.48 mΩ·cm²', fontsize=10, va='top')
ax.text(60, 3e2, 'ideal drift region only;\nslope 2: double the voltage,\nfour times the resistance', fontsize=10, color=GRAY)
ax.set_xlabel('blocking voltage BV (V)'); ax.set_ylabel('specific on-resistance (mΩ·cm²)'); ax.legend(loc='lower right'); ax.set_xlim(50, 3000)
save(f, O + 'b3_ron_bv.png'); print('ron', ron(600, 11.7, 1000, 3e5), ron(1200, 11.7, 1000, 3e5), ron(1200, 9.7, 900, 2.5e6))
# ---- 20: Poisson yield (Section 20.6)
f, ax = fig(8, 4.4); A_ = np.linspace(0, 8, 300)
for D0, c in [(0.05, GREEN), (0.1, BLUE), (0.3, RED)]: ax.plot(A_, 100 * np.exp(-A_ * D0), color=c, lw=2.2, label='D$_0$ = %g per cm²' % D0)
for a_, y in [(1, 90.5), (6, 54.9)]: ax.plot(a_, y, 'o', color=INK, ms=5); ax.text(a_ + 0.15, y + 2.5, '%g cm²: %.0f %%' % (a_, y), fontsize=10)
ax.text(5.3, 92, 'Y = e$^{−A D_0}$', fontsize=12)
ax.set_xlabel('die area A (cm²)'); ax.set_ylabel('dice with no defect (%)'); ax.set_ylim(0, 105); ax.set_xlim(0, 8); ax.legend(loc='lower left')
save(f, O + 'b3_yield.png')
# ---- 21: BAW resonator impedance, Butterworth-Van Dyke (Worked Example 21.2, AlN)
fs = 2.45e9; C0 = 1.30e-12; Cm = 0.055 * C0; Lm = 1 / ((2 * np.pi * fs)**2 * Cm); Qm = 1000; Rm = 2 * np.pi * fs * Lm / Qm
fr = np.linspace(2.35e9, 2.62e9, 4000); w = 2 * np.pi * fr
Zm = Rm + 1j * w * Lm + 1 / (1j * w * Cm); Z = 1 / (1 / Zm + 1j * w * C0)
f, ax = fig(8, 4.6); ax.semilogy(fr / 1e9, np.abs(Z), color=BLUE, lw=2.2)
fp = fs * np.sqrt(1 + Cm / C0)
ax.axvline(fs / 1e9, color=GREEN, ls=':', lw=1); ax.axvline(fp / 1e9, color=RED, ls=':', lw=1)
ax.text(fs / 1e9 - 0.005, 2e3, 'f$_s$ = 2.45 GHz\nseries: |Z| minimum', ha='right', color=GREEN, fontsize=10)
ax.text(fp / 1e9 + 0.005, 0.5, 'f$_p$ = %.3f GHz\nparallel: |Z| maximum' % (fp / 1e9), color=RED, fontsize=10)
ax.text(2.355, 300, 'AlN, k$_t^2$ = 6.5 %: spacing 66 MHz\nC$_0$ = 1.30 pF; Q = 1000 assumed', fontsize=9.5, color=GRAY)
ax.set_xlabel('frequency (GHz)'); ax.set_ylabel('|Z| (Ω)'); ax.set_xlim(2.35, 2.62); ax.set_ylim(0.3, 2e4)
save(f, O + 'b3_baw.png'); print('fp', fp)
# ---- 22: process corners and a Monte Carlo cloud (Sections 22.3 and 22.4)
rng = np.random.default_rng(3); f, ax = fig(6.8, 5.6); ax.set_aspect('equal')
ax.scatter(rng.normal(0, 1, 1500), rng.normal(0, 1, 1500), s=4, color=BLUE, alpha=0.35)
for (x, y, t) in [(0, 0, 'TT'), (3, 3, 'FF'), (-3, -3, 'SS'), (3, -3, 'FS'), (-3, 3, 'SF')]:
    ax.plot(x, y, 's', color=RED, ms=8); ax.text(x + 0.25, y + 0.25, t, fontsize=12, color=RED, weight='bold')
ax.plot([-3, 3, 3, -3, -3], [-3, -3, 3, 3, -3], color=RED, lw=1, ls='--')
ax.set_xlim(-4.2, 4.2); ax.set_ylim(-4.2, 4.2); ax.set_xlabel('NMOS speed (σ from typical)'); ax.set_ylabel('PMOS speed (σ from typical)')
ax.text(-4.0, -3.95, 'blue: 1,500 simulated wafers (global spread); corners at ±3σ', fontsize=9, color=GRAY)
save(f, O + 'b3_corners.png')
print('Em', Em)
