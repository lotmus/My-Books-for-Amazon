"""Book 2 teaching diagrams (shared EE style)."""
import sys; sys.path.insert(0, '../common')
from eestyle import *
import numpy as np, schemdraw, schemdraw.elements as elm, schemdraw.logic as logic
from matplotlib.patches import FancyBboxPatch, Rectangle
O = 'fig/'
def box(ax, x, y, w, h, t, fc='#eef3fa', fs=11):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle='round,pad=0.02,rounding_size=0.08', fc=fc, ec=INK, lw=1.2))
    ax.text(x, y, t, ha='center', va='center', fontsize=fs)
def arrow(ax, a, b, t=None, off=(0, 0.12), c=INK):
    ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='-|>', color=c, lw=1.4, mutation_scale=14))
    if t: ax.text((a[0]+b[0])/2 + off[0], (a[1]+b[1])/2 + off[1], t, ha='center', fontsize=10)
# ---- 3: gates with truth tables
def gates(d):
    G = [('AND', logic.And, lambda a, b: a & b), ('OR', logic.Or, lambda a, b: a | b), ('XOR', logic.Xor, lambda a, b: a ^ b),
         ('NAND', logic.Nand, lambda a, b: 1 - (a & b)), ('NOR', logic.Nor, lambda a, b: 1 - (a | b)), ('NOT', logic.Not, None)]
    for k, (name, E, f) in enumerate(G):
        x, y = (k % 3) * 6.0, -(k // 3) * 7.2
        g = d.add(E().at((x, y)).right())
        d.add(elm.Label().at((x + 1.0, y + 1.4)).label(name, fontsize=14))
        if f:
            rows = ['A B │ Y'] + ['%d %d │ %d' % (a, b, f(a, b)) for a in (0, 1) for b in (0, 1)]
        else:
            rows = ['A │ Y', '0 │ 1', '1 │ 0']
        for j, r in enumerate(rows):
            d.add(elm.Label().at((x + 1.0, y - 1.5 - 0.62 * j)).label(r, fontsize=12, font='DejaVu Sans Mono'))
schem(O + 'b2_gates.png', gates, unit=2.0, fontsize=12, pad=0.5)
# ---- 6: unity-gain Sallen-Key low-pass
def sk(d):
    d.add(elm.Dot(open=True).label('V$_{in}$', 'left'))
    d.add(elm.Resistor().right().label('R$_1$'))
    A = d.add(elm.Dot())
    d.add(elm.Resistor().right().label('R$_2$'))
    B = d.add(elm.Dot())
    d.add(elm.Line().right(1.0))
    op = d.add(elm.Opamp(leads=True).anchor('in2').right())
    Cb = d.add(elm.Capacitor().at(B.center).down()); d.add(elm.Label().at((Cb.center[0] + 0.7, Cb.center[1])).label('C$_2$'))
    d.add(elm.Ground())
    out = op.out
    d.add(elm.Line().at(out).right(0.8))
    d.add(elm.Dot(open=True).label('V$_{out}$', 'right'))
    d.add(elm.Line().at(op.in1).left(0.5))
    d.add(elm.Line().up(1.3))
    fb = d.add(elm.Line().tox(out[0] + 0.4))
    d.add(elm.Line().toy(out[1]))
    d.add(elm.Dot().at((out[0] + 0.4, out[1])))
    Ca = d.add(elm.Capacitor().at(A.center).up(3.2)); d.add(elm.Label().at((Ca.center[0] - 0.7, Ca.center[1])).label('C$_1$'))
    d.add(elm.Line().tox(out[0] + 0.4))
    d.add(elm.Line().toy(fb.end[1]))
    d.add(elm.Label().at((4.5, -3.3)).label('f$_0$ = 1 / (2π √(R$_1$R$_2$C$_1$C$_2$))      Q = √(R$_1$R$_2$C$_1$C$_2$) / (C$_2$(R$_1$ + R$_2$))', fontsize=12))
schem(O + 'b2_sallen_key.png', sk, unit=2.5, fontsize=13, pad=0.6)
# ---- 7: Kelvin (four-wire) shunt connection
f, ax = fig(8, 3.6); ax.axis('off'); ax.grid(False); ax.set_xlim(0, 10); ax.set_ylim(0, 4.4); ax.set_aspect('equal')
ax.add_patch(Rectangle((4.1, 1.6), 1.8, 0.8, fc='#333333', ec=INK)); ax.text(5, 2.0, 'R$_{shunt}$', color='white', ha='center', va='center', fontsize=11)
for x in (3.5, 5.9): ax.add_patch(Rectangle((x, 1.45), 0.6, 1.1, fc='#c9a227', ec=INK))
ax.plot([0.3, 3.5], [2.0, 2.0], color=RED, lw=7, solid_capstyle='butt'); ax.plot([6.5, 9.7], [2.0, 2.0], color=RED, lw=7, solid_capstyle='butt')
ax.text(1.9, 2.35, 'load current in (wide trace)', ha='center', color=RED, fontsize=10); ax.text(8.1, 2.35, 'load current out', ha='center', color=RED, fontsize=10)
ax.plot([3.95, 3.95, 4.6], [2.45, 3.6, 3.6], color=BLUE, lw=1.8); ax.plot([6.05, 6.05, 5.4], [2.45, 3.6, 3.6], color=BLUE, lw=1.8)
ax.annotate('', xy=(5.0, 3.6), xytext=(4.6, 3.6)); ax.text(5.0, 3.85, 'thin sense traces from the inner pad edges\nto the current-sense amplifier', ha='center', fontsize=10, color=BLUE)
ax.text(5.0, 0.8, 'The sense traces carry almost no current, so the copper of the wide traces\nand solder joints is left out of the measured voltage.', ha='center', fontsize=10, color=GRAY)
save(f, O + 'b2_kelvin.png')
# ---- 8: ceramic capacitor DC-bias derating (illustrative)
f, ax = fig(8, 4.4); v = np.linspace(0, 100, 200)
ax.plot(v, 100 + 0 * v, color=GREEN, lw=2, label='C0G (NP0): stays put')
ax.plot(v, 100 / (1 + (v / 70) ** 2.2), color=BLUE, lw=2, label='X7R / X5R, larger case: loses some')
ax.plot(v, 100 / (1 + (v / 40) ** 1.8), color=RED, lw=2, label='X5R, smallest case, high value: loses most')
ax.set_xlabel('DC bias (% of rated voltage)'); ax.set_ylabel('capacitance (% of nominal)'); ax.set_ylim(0, 110); ax.set_xlim(0, 100)
ax.legend(loc='lower left'); ax.text(98, 104, 'illustrative shapes: read the curve for your part', ha='right', fontsize=10, color=GRAY)
save(f, O + 'b2_dcbias.png')
# ---- 10: control loop block diagram
f, ax = fig(8, 3.4); ax.axis('off'); ax.grid(False); ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.set_aspect('equal')
ax.add_patch(plt.Circle((1.6, 2.6), 0.28, fc='white', ec=INK)); ax.text(1.6, 2.6, 'Σ', ha='center', va='center', fontsize=12)
ax.text(1.38, 3.0, '+', fontsize=11); ax.text(1.75, 2.0, '−', fontsize=13)
box(ax, 3.6, 2.6, 1.8, 0.9, 'controller'); box(ax, 6.2, 2.6, 1.8, 0.9, 'actuator\n+ plant'); box(ax, 6.2, 0.8, 1.8, 0.8, 'sensor', fc='#f3f3f3')
arrow(ax, (0.2, 2.6), (1.32, 2.6), 'reference', (0, 0.2)); arrow(ax, (1.88, 2.6), (2.7, 2.6), 'error', (0, 0.2)); arrow(ax, (4.5, 2.6), (5.3, 2.6), 'command', (0, 0.2))
arrow(ax, (7.1, 2.6), (9.6, 2.6), 'output', (0.4, 0.2)); ax.plot([8.4, 8.4], [2.6, 0.8], color=INK, lw=1.4); arrow(ax, (8.4, 0.8), (7.1, 0.8))
ax.plot([5.3, 1.6], [0.8, 0.8], color=INK, lw=1.4); arrow(ax, (1.6, 0.8), (1.6, 2.32)); ax.text(3.4, 0.95, 'measurement', ha='center', fontsize=10)
arrow(ax, (6.2, 3.95), (6.2, 3.05)); ax.text(6.35, 3.6, 'disturbance', fontsize=10)
save(f, O + 'b2_loop_block.png')
# ---- 12: follower with isolation resistor driving a capacitive load
def iso(d):
    d.add(elm.Dot(open=True).label('V$_{in}$', 'left'))
    d.add(elm.Line().right(1))
    op = d.add(elm.Opamp(leads=True).anchor('in2').right())
    d.add(elm.Line().at(op.out).right(0.5)); N = d.add(elm.Dot())
    d.add(elm.Resistor().right().label('R$_{iso}$ (10 to 100 Ω)'))
    L = d.add(elm.Dot())
    d.add(elm.Line().right(1)); d.add(elm.Dot(open=True).label('to load', 'right'))
    Cl = d.add(elm.Capacitor().at(L.center).down()); d.add(elm.Ground()); d.add(elm.Label().at((Cl.center[0] + 0.4, Cl.center[1])).label('C$_{load}$ (cable, ADC input)', halign='left'))
    d.add(elm.Line().at(op.in1).left(0.5)); d.add(elm.Line().up(1.3)); d.add(elm.Line().tox(N.center[0])); d.add(elm.Line().toy(N.center[1]))
schem(O + 'b2_iso_resistor.png', iso, unit=2.5, fontsize=13, pad=0.6)
# ---- 16: inverting Schmitt-trigger transfer curve
f, ax = fig(8, 4.4); Vp, Vm, Vs = 1.0, -1.0, 4.0
o = 0.07
ax.plot([-3, Vp + o, Vp + o, 3], [Vs + o, Vs + o, -Vs + o, -Vs + o], color=BLUE, lw=2.2)
ax.plot([3, Vm - o, Vm - o, -3], [-Vs - o, -Vs - o, Vs - o, Vs - o], color=RED, lw=2.2)
ax.annotate('', xy=(0.2, Vs), xytext=(-1.8, Vs), arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.5))
ax.annotate('', xy=(Vp, -1.0), xytext=(Vp, 1.0), arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.5))
ax.annotate('', xy=(-0.2, -Vs), xytext=(1.8, -Vs), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.5))
ax.annotate('', xy=(Vm, 1.0), xytext=(Vm, -1.0), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.5))
ax.text(-2.9, Vs + 0.35, 'input rising (blue): output stays high until V$_{T+}$', color=BLUE, fontsize=10)
ax.text(2.9, -Vs - 0.75, 'input falling (red): output stays low until V$_{T−}$', color=RED, fontsize=10, ha='right')
ax.text(Vp + 0.08, 0.2, 'V$_{T+}$', fontsize=11); ax.text(Vm - 0.5, 0.2, 'V$_{T−}$', fontsize=11)
ax.annotate('', xy=(Vp, -2.6), xytext=(Vm, -2.6), arrowprops=dict(arrowstyle='<->', color=GRAY)); ax.text(0, -2.4, 'hysteresis', ha='center', fontsize=10, color=GRAY)
ax.axhline(0, color=GRAY, lw=0.8); ax.axvline(0, color=GRAY, lw=0.8)
ax.set_xlim(-3, 3); ax.set_ylim(-5.2, 5.2); ax.set_xlabel('input voltage (V)'); ax.set_ylabel('output voltage (V)')
save(f, O + 'b2_hysteresis.png')
# ---- 18: P, PI and PID step responses on the same plant G = 1/((s+1)(0.2s+1))
def sim(Kp, Ki, Kd, T=6, dt=1e-4):
    n = int(T / dt); x1 = x2 = 0.0; integ = 0.0; yprev = 0.0; ys = np.empty(n)
    for i in range(n):
        y = x2; e = 1.0 - y; integ += e * dt; dy = (y - yprev) / dt if i else 0.0; yprev = y
        u = Kp * e + Ki * integ - Kd * dy          # derivative on measurement (no kick)
        x1 += dt * (-x1 + u)                        # 1/(s+1)
        x2 += dt * (-x2 + x1) / 0.2                 # 1/(0.2s+1)
        ys[i] = y
    return np.arange(n) * dt, ys
f, ax = fig(8, 4.4)
for (Kp, Ki, Kd, lab, c, ls) in ((4, 0, 0, 'P only (K$_p$ = 4): settles 20% short', GRAY, '-'), (4, 3, 0, 'PI (K$_p$ = 4, K$_i$ = 3): error removed, some overshoot', BLUE, '-'), (4, 3, 0.4, 'PID (K$_d$ = 0.4 added): overshoot damped', RED, '-')):
    t, y = sim(Kp, Ki, Kd); ax.plot(t, y, color=c, lw=2, ls=ls, label=lab)
ax.axhline(1, color=INK, lw=0.8, ls=':'); ax.text(5.9, 1.03, 'setpoint', ha='right', fontsize=10)
ax.set_xlabel('time (s)'); ax.set_ylabel('output (normalized)'); ax.set_xlim(0, 6); ax.set_ylim(0, 1.4); ax.legend(loc='lower right')
save(f, O + 'b2_pid_steps.png')
# ---- 19: zero-order hold and its half-sample delay
f, ax = fig(8, 4.0); t = np.linspace(0, 2, 800); T = 0.1
ax.plot(t, np.sin(2*np.pi*0.8*t), color=BLUE, lw=2, label='continuous signal')
ts = np.arange(0, 2 + T, T); ax.step(ts, np.sin(2*np.pi*0.8*ts), where='post', color=RED, lw=1.8, label='sampled and held (DAC output)')
ax.plot(t, np.sin(2*np.pi*0.8*(t - T/2)), color=RED, lw=1.2, ls='--', label='its average: the signal delayed by T/2')
ax.plot(ts, np.sin(2*np.pi*0.8*ts), 'o', color=RED, ms=3.5)
ax.set_xlabel('time (s), sample period T = 0.1 s'); ax.set_xlim(0, 2); ax.set_ylim(-1.35, 1.6); ax.legend(loc='upper right', fontsize=9.5, ncol=1)
save(f, O + 'b2_zoh.png')
# ---- 20: three-op-amp instrumentation amplifier
def ina(d):
    U1 = d.add(elm.Opamp(leads=True, flip=True).at((0, 5)).anchor('center').right().label('A1', 'center', fontsize=11))
    U2 = d.add(elm.Opamp(leads=True).at((0, -1)).anchor('center').right().label('A2', 'center', fontsize=11))
    d.add(elm.Line().at(U1.in2).left(1)); d.add(elm.Dot(open=True).label('V$_−$', 'left'))
    d.add(elm.Line().at(U2.in2).left(1)); d.add(elm.Dot(open=True).label('V$_+$', 'left'))
    xo = U1.out[0] + 0.8; y1, y2 = U1.out[1], U2.out[1]; n1y, n2y = y1 - (y1 - y2) / 3, y1 - 2 * (y1 - y2) / 3
    d.add(elm.Line().at(U1.out).tox(xo)); o1 = d.add(elm.Dot())
    r = d.add(elm.Resistor().down().toy(n1y)); d.add(elm.Label().at((xo + 0.5, (y1 + n1y) / 2)).label('R', halign='left'))
    n1 = d.add(elm.Dot())
    d.add(elm.Resistor().down().toy(n2y)); d.add(elm.Label().at((xo + 0.5, (n1y + n2y) / 2)).label('R$_G$', halign='left'))
    n2 = d.add(elm.Dot())
    d.add(elm.Resistor().down().toy(y2)); d.add(elm.Label().at((xo + 0.5, (n2y + y2) / 2)).label('R', halign='left'))
    o2 = d.add(elm.Dot()); d.add(elm.Line().tox(U2.out[0]))
    d.add(elm.Line().at(U1.in1).left(0.4)); d.add(elm.Line().toy(n1y)); d.add(elm.Line().tox(xo))
    d.add(elm.Line().at(U2.in1).left(0.4)); d.add(elm.Line().toy(n2y)); d.add(elm.Line().tox(xo))
    U3 = d.add(elm.Opamp(leads=True).at((xo + 6.0, 2)).anchor('center').right().label('A3', 'center', fontsize=11))
    xr = xo + 3.4
    d.add(elm.Line().at(o1.center).right(0.4)); d.add(elm.Resistor().right(2.4)); d.add(elm.Label().at((xo + 1.6, y1 + 0.5)).label('R$_2$'))
    d.add(elm.Line().toy(U3.in1[1])); k = d.add(elm.Dot()); d.add(elm.Line().tox(U3.in1[0]))
    d.add(elm.Line().at(o2.center).right(0.4)); d.add(elm.Resistor().right(2.4)); d.add(elm.Label().at((xo + 1.6, y2 - 0.6)).label('R$_2$'))
    d.add(elm.Line().toy(U3.in2[1])); a = d.add(elm.Dot()); d.add(elm.Line().tox(U3.in2[0]))
    d.add(elm.Resistor().at((a.center[0], y2)).down(2.0)); d.add(elm.Ground()); d.add(elm.Label().at((a.center[0] + 0.5, y2 - 1.0)).label('R$_3$', halign='left'))
    d.add(elm.Line().at(k.center).up(2.2)); d.add(elm.Resistor().tox(U3.out[0] + 0.6)); d.add(elm.Label().at(((k.center[0] + U3.out[0]) / 2 + 0.3, k.center[1] + 2.7)).label('R$_3$'))
    d.add(elm.Line().toy(U3.out[1])); d.add(elm.Line().tox(U3.out[0]))
    d.add(elm.Line().at((U3.out[0] + 0.6, U3.out[1])).right(1.0)); d.add(elm.Dot(open=True).label('V$_{out}$', 'right'))
    d.add(elm.Dot().at((U3.out[0] + 0.6, U3.out[1])))
    d.add(elm.Label().at((xo + 1.5, y2 - 3.6)).label('V$_{out}$ = (1 + 2R/R$_G$) · (R$_3$/R$_2$) · (V$_+$ − V$_−$)', fontsize=13))
schem(O + 'b2_inamp.png', ina, unit=2.5, fontsize=12, pad=0.6)
# ---- 22: sample-and-hold waveforms
f, (a1, a2) = plt.subplots(2, 1, figsize=(8, 4.6), dpi=100, sharex=True, gridspec_kw=dict(height_ratios=[3, 1]))
t = np.linspace(0, 4, 2000); vin = 0.8*np.sin(2*np.pi*0.45*t) + 0.15*np.sin(2*np.pi*1.7*t)
hold = ((t % 1.0) >= 0.6); vout = vin.copy()
for i in range(1, len(t)):
    if hold[i]: vout[i] = vout[i-1]
a1.plot(t, vin, color=BLUE, lw=1.6, label='input'); a1.plot(t, vout, color=RED, lw=2, label='S/H output'); a1.legend(loc='upper right', ncol=2, fontsize=10)
for k in range(4): a1.axvspan(k + 0.6, k + 1.0, color='#f2e3e3', lw=0)
a1.set_ylabel('voltage'); a1.text(0.62, -1.1, 'hold', fontsize=10, color=RED); a1.text(0.1, -1.1, 'track', fontsize=10, color=BLUE); a1.set_ylim(-1.25, 1.35)
a2.step(t, np.where(hold, 1, 0), where='post', color=INK, lw=1.6); a2.set_yticks([0, 1]); a2.set_yticklabels(['track', 'hold']); a2.set_xlabel('time (arbitrary units)'); a2.set_ylim(-0.3, 1.3)
save(f, O + 'b2_sh_wave.png')
# ---- 24: H-bridge with its two current paths
def hb(d):
    d.add(elm.Line().at((0, 6)).right(6)); d.add(elm.Dot().at((3, 6))); d.add(elm.Line().at((3, 6)).up(0.6)); d.add(elm.Label().at((3, 7.0)).label('+V$_S$'))
    d.add(elm.Line().at((0, 0)).right(6)); d.add(elm.Ground().at((3, 0)))
    d.add(elm.Switch().at((0, 6)).down().toy(3)); A = d.add(elm.Dot()); d.add(elm.Label().at((-0.6, 4.5)).label('Q1'))
    d.add(elm.Switch().at((0, 3)).down().toy(0)); d.add(elm.Label().at((-0.6, 1.5)).label('Q2'))
    d.add(elm.Switch().at((6, 6)).down().toy(3)); B = d.add(elm.Dot()); d.add(elm.Label().at((6.6, 4.5)).label('Q3'))
    d.add(elm.Switch().at((6, 3)).down().toy(0)); d.add(elm.Label().at((6.6, 1.5)).label('Q4'))
    d.add(elm.Line().at((0, 3)).right(1.5)); d.add(elm.Motor().right(3)); d.add(elm.Line().tox(6))
    d.add(elm.Label().at((3, 3.0)).label('M'))
    R, Bc = '#c0392b', '#2f6db0'
    d.add(elm.Arrow().at((0.7, 5.4)).down(1.4).color(R))
    d.add(elm.Arrow().at((1.6, 3.9)).right(2.8).color(R)); d.add(elm.Label().at((3, 4.4)).label('forward: Q1 and Q4 on', color=R, fontsize=11))
    d.add(elm.Arrow().at((5.3, 2.0)).down(1.4).color(R))
    d.add(elm.Arrow().at((5.3, 5.4)).down(1.4).color(Bc))
    d.add(elm.Arrow().at((4.4, 2.1)).left(2.8).color(Bc)); d.add(elm.Label().at((3, 1.6)).label('reverse: Q3 and Q2 on', color=Bc, fontsize=11))
    d.add(elm.Arrow().at((0.7, 2.0)).down(1.4).color(Bc))
    d.add(elm.Label().at((3, -1.5)).label('Never Q1 and Q2 (or Q3 and Q4) together: that shorts the supply (shoot-through).', fontsize=11))
schem(O + 'b2_hbridge.png', hb, unit=2.5, fontsize=12, pad=0.6)
# ---- 27: op-amp relaxation oscillator
def relax(d):
    op = d.add(elm.Opamp(leads=True).at((0, 0)).anchor('center').right())
    d.add(elm.Line().at(op.out).right(1)); O1 = d.add(elm.Dot()); d.add(elm.Line().right(1)); d.add(elm.Dot(open=True).label('V$_{out}$ (square wave)', 'right'))
    # R from out to inverting input, C from inverting input to ground
    d.add(elm.Line().at(O1.center).up(2.2)); d.add(elm.Resistor().tox(op.in1[0] - 1).label('R')); n = d.add(elm.Dot())
    d.add(elm.Line().toy(op.in1[1])); d.add(elm.Line().tox(op.in1[0]))
    d.add(elm.Capacitor().at(n.center).left(1.6).label('C')); d.add(elm.Line().down(0.6)); d.add(elm.Ground())
    # R1 from out to non-inverting, R2 to ground
    d.add(elm.Line().at(O1.center).down(2.2)); d.add(elm.Resistor().tox(op.in2[0] - 1).label('R$_1$', 'bottom')); m = d.add(elm.Dot())
    d.add(elm.Line().toy(op.in2[1])); d.add(elm.Line().tox(op.in2[0]))
    Rb = d.add(elm.Resistor().at(m.center).down(1.8)); d.add(elm.Ground()); d.add(elm.Label().at((Rb.center[0] - 0.5, Rb.center[1])).label('R$_2$', halign='right'))
    d.add(elm.Label().at((1.0, -6.3)).label('β = R$_2$/(R$_1$ + R$_2$)      period T = 2RC · ln((1 + β)/(1 − β))', fontsize=13))
schem(O + 'b2_relax_osc.png', relax, unit=2.5, fontsize=13, pad=0.6)
# ---- 28: setup and hold window
f, ax = fig(8, 3.6); ax.axis('off'); ax.grid(False); ax.set_xlim(0, 10); ax.set_ylim(-0.6, 4.4)
ck = [(0, 3), (2.5, 3), (2.5, 4), (5.0, 4), (5.0, 3), (7.5, 3), (7.5, 4), (10, 4)]
ax.plot(*zip(*ck), color=INK, lw=2); ax.text(-0.05, 3.5, 'CLK', ha='right', va='center', fontsize=11)
ax.fill_between([0, 1.4], 1, 2, color='#dddddd'); ax.fill_between([3.3, 10], 1, 2, color='#dddddd')
ax.plot([0, 1.4], [1, 1], color=INK); ax.plot([0, 1.4], [2, 2], color=INK); ax.plot([1.4, 1.7], [1, 2], color=INK); ax.plot([1.4, 1.7], [2, 1], color=INK)
ax.plot([1.7, 3.3], [1, 1], color=INK, lw=2); ax.plot([1.7, 3.3], [2, 2], color=INK, lw=2); ax.text(2.5, 1.5, 'stable', ha='center', va='center', fontsize=10)
ax.plot([3.3, 3.6], [1, 2], color=INK); ax.plot([3.3, 3.6], [2, 1], color=INK); ax.text(-0.05, 1.5, 'D', ha='right', va='center', fontsize=11)
ax.text(0.7, 1.5, 'may change', ha='center', va='center', fontsize=9, color=GRAY); ax.text(6.6, 1.5, 'may change', ha='center', va='center', fontsize=9, color=GRAY)
ax.axvline(2.5, ymin=0.05, ymax=0.95, color=RED, lw=1, ls='--')
ax.annotate('', xy=(2.5, 0.4), xytext=(1.7, 0.4), arrowprops=dict(arrowstyle='<->', color=BLUE)); ax.text(2.1, -0.15, 't$_{setup}$', ha='center', color=BLUE, fontsize=11)
ax.annotate('', xy=(3.3, 0.4), xytext=(2.5, 0.4), arrowprops=dict(arrowstyle='<->', color=GREEN)); ax.text(2.9, -0.15, 't$_{hold}$', ha='center', color=GREEN, fontsize=11)
ax.text(5.6, 0.3, 'Change D inside the window and the flip-flop\nmay go metastable.', fontsize=10, color=GRAY)
save(f, O + 'b2_setup_hold.png')
print('ok')
