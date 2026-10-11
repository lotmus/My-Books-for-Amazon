"""Book 5 pass 2 new figures. Every marked number is recomputed and asserted against the text."""
import sys; sys.path.insert(0, '/workspace/ee1/common')
from eestyle import *
import numpy as np, json
from math import ceil, log10, sqrt, atan, exp
O = 'fig/'; c0 = 2.998e8; CHECK = {}
def near(a, b, tol): assert abs(a - b) <= tol, (a, b); return a
# ---- 8.3 duplexer
f, (a1, a2) = plt.subplots(2, 1, figsize=(8, 5.6), dpi=100, gridspec_kw=dict(height_ratios=[1.4, 1]))
fr = np.linspace(2450, 2740, 1200)
def bpf(f0, bw, n, edge):  # illustrative Chebyshev-like skirt
    x = np.abs(fr - f0)/(bw/2); return -np.where(x < 1, 0.5*x**8, 10*n*np.log10(x) + edge*np.clip(x - 1, 0, None)**0.5)
tx = np.maximum(bpf(2535, 72, 6, 30), -80); rx = np.maximum(bpf(2655, 72, 6, 30), -80)
a1.axvspan(2500, 2570, color=ORANGE, alpha=0.12); a1.axvspan(2620, 2690, color=GREEN, alpha=0.12)
a1.plot(fr, tx, color=ORANGE, lw=2, label='transmit filter'); a1.plot(fr, rx, color=GREEN, lw=2, label='receive filter')
iso_need = 26 - 4 - (-174 + 4 + 10*log10(10**0.05 - 1)) - 26 + 0  # placeholder replaced below
fl = -174 + 4; allowed = fl + 10*log10(10**0.05 - 1); iso = -128 - allowed; txrej = 26 - (-30)
CHECK['iso'] = near(iso, 51.1, 0.05); CHECK['txrej'] = txrej; assert txrej == 56
a1.annotate('', xy=(2655, -iso), xytext=(2655, 0), arrowprops=dict(arrowstyle='<->', color=INK))
a1.text(2660, -iso/2, 'TX filter in RX band:\n%.1f dB needed' % iso, fontsize=9)
a1.annotate('', xy=(2535, -txrej), xytext=(2535, 0), arrowprops=dict(arrowstyle='<->', color=INK))
a1.text(2470, -txrej/2 - 6, 'RX filter at TX\ncarrier: %d dB' % txrej, fontsize=9)
a1.text(2503, 3, 'uplink 2500-2570', fontsize=8.5, color=ORANGE); a1.text(2623, 3, 'downlink 2620-2690', fontsize=8.5, color=GREEN)
a1.set_ylim(-85, 10); a1.set_xlabel('frequency (MHz)'); a1.set_ylabel('response (dB)'); a1.legend(loc='lower left', fontsize=8.5)
for y, lab, col in [(-128, 'PA noise in RX band  -128', ORANGE), (-170, 'receiver floor  -170', BLUE), (allowed, 'allowed added noise  %.1f' % allowed, RED)]:
    a2.axhline(y, color=col, lw=2); a2.text(0.02, y + 1.5, lab + ' dBm/Hz', fontsize=9, color=col, transform=a2.get_yaxis_transform())
a2.annotate('', xy=(0.8, allowed), xytext=(0.8, -128), xycoords=('axes fraction', 'data'), arrowprops=dict(arrowstyle='<->', color=INK))
a2.text(0.82, (allowed - 128)/2, '%.1f dB' % iso, transform=a2.get_yaxis_transform(), fontsize=9)
a2.set_ylim(-185, -120); a2.set_xticks([]); a2.set_ylabel('dBm/Hz')
save(f, O + 'b5n_duplexer.png')
# ---- 16.2 range-Doppler
B = 4e9; Tr = 40e-6; S = B/Tr; fs = 12.8e6; Ns = 512; Nc = 128; Tc = 50e-6; lam = c0/62e9
rng = np.random.default_rng(5); t = np.arange(Ns)/fs; k = np.arange(Nc)[:, None]
sig = np.zeros((Nc, Ns), complex)
for R, v, a in [(3.0, -1.0, 1.0), (7.5, 2.0, 0.6)]:
    fb = 2*R*S/c0; ph = 4*np.pi*v*k*Tc/lam
    sig += a*np.exp(1j*(2*np.pi*fb*t[None, :] + ph))
sig += 0.3*(rng.standard_normal(sig.shape) + 1j*rng.standard_normal(sig.shape))
rd = np.fft.fftshift(np.fft.fft(np.fft.fft(sig*np.hanning(Ns)[None, :], axis=1)*np.hanning(Nc)[:, None], axis=0), axes=0)
P = 20*np.log10(np.abs(rd) + 1e-9); P -= P.max()
dR = c0/(2*B); dv = lam/(2*Nc*Tc); CHECK['dR'] = near(dR, 0.0375, 1e-4); CHECK['dv'] = near(dv, 0.378, 1e-3)
rax = np.arange(Ns)*fs/Ns*c0/(2*S); vax = (np.arange(Nc) - Nc//2)*dv
f, ax = fig(8, 4.6); m = rax <= 15
im = ax.pcolormesh(rax[m], vax, P[:, m], vmin=-50, vmax=0, cmap='viridis', shading='auto')
plt.colorbar(im, ax=ax, label='dB')
for R, v in [(3.0, -1.0), (7.5, 2.0)]:
    i, j = np.unravel_index(np.argmax(np.where((np.abs(rax[None, :] - R) < 0.3) & (np.abs(vax[:, None] - v) < 1), P, -999)), P.shape)
    near(rax[j], R, 0.05); near(vax[i], v, 0.4)
    ax.annotate('%.1f m, %+.1f m/s' % (R, v), xy=(R, v), xytext=(R + 1, v + 6), color='white', fontsize=9.5, arrowprops=dict(arrowstyle='->', color='white'))
ax.set_xlabel('range (m)'); ax.set_ylabel('radial velocity (m/s), negative = approaching'); ax.set_ylim(-24.2, 24.2)
save(f, O + 'b5n_rangedoppler.png')
# ---- 22.1 CORDIC
def cordic_err(n):
    th = np.linspace(-np.pi/2*0.99, np.pi/2*0.99, 4001); z = th.copy()
    for i in range(n):
        d = np.where(z >= 0, 1, -1); z = z - d*np.arctan(2.0**-i)
    return np.max(np.abs(z))
ns = np.arange(1, 21); err = np.array([cordic_err(n) for n in ns])
K = np.cumprod([sqrt(1 + 2.0**(-2*i)) for i in range(20)])
CHECK['K'] = near(K[-1], 1.6468, 1e-4); CHECK['err16'] = near(err[15], atan(2**-15), 2e-5)
CHECK['err1'] = near(err[0], np.pi/4, 0.02)
f, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.8), dpi=100)
a1.semilogy(ns, err, 'o-', color=BLUE, ms=4); a1.semilogy(ns, 2.0**-(ns - 1), '--', color=GRAY, lw=1, label='one bit per iteration')
a1.plot(16, err[15], 'o', color=RED, ms=7); a1.text(10.5, err[15]*0.15, '16 iterations: %.1e rad' % err[15], fontsize=9, color=RED)
a1.set_xlabel('iterations'); a1.set_ylabel('worst-case angle error (rad)'); a1.legend(fontsize=8.5)
a2.plot(np.arange(1, 21), K, 'o-', color=GREEN, ms=4); a2.axhline(1.6468, color=GRAY, ls='--', lw=1); a2.text(8, 1.62, 'K = 1.6468 (scale by 0.6073)', fontsize=9)
a2.set_xlabel('iterations'); a2.set_ylabel('CORDIC gain')
save(f, O + 'b5c_cordic.png')
# ---- 22.2 break-even
v = np.logspace(3, 6, 300); fp = 80*v; asic = 3e6 + 8*v; be = 3e6/72; CHECK['be'] = near(be, 41667, 1)
f, ax = fig(8, 4.3); ax.loglog(v, fp, color=ORANGE, lw=2.2, label='FPGA, 80 $/unit'); ax.loglog(v, asic, color=BLUE, lw=2.2, label='ASIC, 3 M$ NRE + 8 $/unit')
ax.axvline(be, color=GRAY, ls='--'); ax.text(be*1.1, 1.2e5, 'break-even\n41 667 units', fontsize=9.5)
ax.set_xlabel('volume (units)'); ax.set_ylabel('total cost ($)'); ax.legend(fontsize=9)
save(f, O + 'b5c_breakeven.png')
# ---- 23.1 microphone array
th = np.radians(np.linspace(-90, 90, 3601)); d = 0.04; M = 4; cs = 343
def resp(fq):
    k = 2*np.pi*fq/cs; a = np.exp(1j*k*d*np.arange(M)[:, None]*np.sin(th)[None, :]).sum(0)/M; return 20*np.log10(np.abs(a) + 1e-12)
def hpbw(r):
    ok = th[r >= -3]; return np.degrees(ok.max() - ok.min())
BW = {fq: hpbw(resp(fq)) for fq in (1000, 2000, 4000)}; CHECK['mic_bw'] = BW
f, ax = fig(8, 4.2)
for fq, col in [(1000, ORANGE), (2000, GREEN), (4000, BLUE)]:
    ax.plot(np.degrees(th), resp(fq), color=col, lw=2, label='%d kHz: %.0f° half-power width' % (fq/1000, BW[fq]))
ax.axhline(-3, color=GRAY, ls=':', lw=1); ax.set_ylim(-30, 2); ax.set_xlabel('arrival angle from broadside (°)'); ax.set_ylabel('array response (dB)'); ax.legend(fontsize=9, loc='lower center')
save(f, O + 'b5c_micarray.png')
# ---- 23.2 Kalman fusion
rng = np.random.default_rng(11); T = 600; dt = 1.0
vtrue = 2 + 0.5*np.sin(np.arange(T)/40); x = np.cumsum(vtrue)*dt
bias = np.cumsum(rng.normal(0, 0.01, T)) + 0.05; vmeas = vtrue + bias + rng.normal(0, 0.1, T)
gps = x + rng.normal(0, 3, T); dr = np.cumsum(vmeas)*dt
xe = np.zeros(T); X = np.array([gps[0], 0.0]); Pm = np.diag([9.0, 0.1]); Fm = np.array([[1, -dt], [0, 1]]); Qm = np.diag([0.1**2, 0.01**2]); Hm = np.array([1.0, 0])
for i in range(T):
    if i: X = Fm @ X + np.array([vmeas[i]*dt, 0]); Pm = Fm @ Pm @ Fm.T + Qm
    Kg = Pm @ Hm/(Hm @ Pm @ Hm + 9); X = X + Kg*(gps[i] - X[0]); Pm = Pm - np.outer(Kg, Hm @ Pm); xe[i] = X[0]
rms = lambda e: float(np.sqrt(np.mean(e**2)))
CHECK['kal'] = dict(gps=rms(gps - x), dr_end=float(abs(dr[-1] - x[-1])), dr=rms(dr - x), kf=rms(xe - x))
f, ax = fig(8, 4.3); tt = np.arange(T)
ax.plot(tt, gps - x, '.', color=GRAY, ms=2.5, label='GNSS alone, RMS %.1f m' % CHECK['kal']['gps'])
ax.plot(tt, dr - x, color=ORANGE, lw=1.8, label='dead reckoning alone, RMS %.0f m' % CHECK['kal']['dr'])
ax.plot(tt, xe - x, color=BLUE, lw=1.8, label='Kalman fusion (position and velocity bias), RMS %.2f m' % CHECK['kal']['kf'])
ax.set_ylim(-12, max(12, (dr - x).max()*1.05)); ax.set_xlabel('time (s)'); ax.set_ylabel('position error (m)'); ax.legend(fontsize=9, loc='upper left')
save(f, O + 'b5c_fusion.png')
# ---- 24.1 fiber budget staircase
pts = [(0, 0), (0, -0.5), (10, -4.0), (10, -4.2), (10, -4.4), (10, -4.9)]
CHECK['rx'] = near(-0.5 - 3.5 - 0.2 - 0.2 - 0.5, -4.9, 1e-9)
f, ax = fig(8, 4.2)
xs = [0, 0.15, 0.15, 3.5, 3.5, 7.0, 7.0, 10.15, 10.15, 10.3]; ys = [0, 0, -0.5, -0.5 - 0.35*3.35, -0.7 - 0.35*3.35, -0.7 - 0.35*6.85, -0.9 - 0.35*6.85, -0.9 - 0.35*10, -1.4 - 0.35*10, -1.4 - 0.35*10]
near(ys[-1], -4.9, 1e-9)
ax.plot(xs, ys, color=BLUE, lw=2.4); ax.axhline(-14, color=RED, ls='--'); ax.text(0.3, -13.4, 'receiver sensitivity -14 dBm', color=RED, fontsize=9.5)
for xx, lab in [(0.15, 'connector 0.5'), (3.5, 'splice 0.2'), (7.0, 'splice 0.2'), (10.15, 'connector 0.5')]:
    ax.text(xx, 0.6, lab, fontsize=8.5, ha='center')
ax.annotate('', xy=(10.3, -14), xytext=(10.3, -4.9), arrowprops=dict(arrowstyle='<->', color=INK)); ax.text(9.0, -9.5, 'margin\n9.1 dB', fontsize=9.5)
ax.text(4.5, -2.2, '10 km fiber at 0.35 dB/km = 3.5 dB', fontsize=9, color=BLUE); ax.text(8.3, -4.5, '-4.9 dBm', fontsize=9.5)
ax.set_xlim(-0.3, 11); ax.set_ylim(-16, 1.5); ax.set_xlabel('position along link (km)'); ax.set_ylabel('optical power (dBm)')
save(f, O + 'b5c_fiberbudget.png')
# ---- 24.2 dispersion reach
lam = 1550e-9; D = 17e-6
reach = lambda Bd: (1/Bd)/(D*lam**2*Bd/c0)/1e3
R = {b: reach(b*1e9) for b in (10, 25, 53.125, 59.84375)}; CHECK['reach'] = R
for b, r in zip((10, 25, 53.125, 59.84375), (73.4, 11.7, 2.6, 2.0)): near(R[b], r, 0.06)
spread = D*80e3*lam**2*59.84375e9/c0; CHECK['zr_sym'] = near(spread*59.84375e9, 39, 0.5)
bb = np.logspace(np.log10(5), 2, 200); f, ax = fig(8, 4.3)
ax.loglog(bb, [reach(b*1e9) for b in bb], color=BLUE, lw=2.2, label='one-symbol spread, 17 ps/(nm km)')
for b in R: ax.plot(b, R[b], 'o', color=INK, ms=5); ax.text(b*1.06, R[b]*1.15, '%g GBd: %.1f km' % (round(b, 2), R[b]), fontsize=9)
ax.plot(59.84, 80, 's', color=RED, ms=7); ax.text(21, 95, '400ZR: 80 km, 39 symbols, DSP equalized', color=RED, fontsize=9)
ax.set_xlabel('symbol rate (GBd)'); ax.set_ylabel('reach (km)'); ax.legend(fontsize=9, loc='lower left')
save(f, O + 'b5c_dispersion.png')
# ---- 25.1 LoRa airtime
def toa(sf, bw, pl, pre=8, cr=1):
    Ts = 2**sf/bw; de = 1 if Ts > 16e-3 else 0
    ps = 8 + max(ceil((8*pl - 4*sf + 28 + 16)/(4*(sf - 2*de)))*(cr + 4), 0); return (pre + 4.25 + ps)*Ts
CHECK['longfast'] = near(toa(11, 250e3, 50)*1e3, 575.5, 0.1); CHECK['sf7'] = near(toa(7, 250e3, 20)*1e3, 28.3, 0.05)
sfs = np.arange(7, 13); f, ax = fig(8, 4.2)
for bw, col in [(125e3, ORANGE), (250e3, BLUE)]:
    ax.semilogy(sfs, [toa(s, bw, 50)*1e3 for s in sfs], 'o-', color=col, lw=2, label='%d kHz' % (bw/1e3))
ax.plot(11, 575.5, 's', color=RED, ms=8); ax.text(9.2, 900, 'LongFast: 575.5 ms', color=RED, fontsize=9.5)
ax.set_xlabel('spreading factor'); ax.set_ylabel('airtime of 50 bytes (ms)'); ax.legend(fontsize=9)
save(f, O + 'b5c_loraairtime.png')
# ---- 25.2 BLE trilateration
rng = np.random.default_rng(3); W, H = 10.0, 8.0; bx = np.array([[0, 0], [W, 0], [W, H], [0, H]]); n = 2.5; sig = 4.0
def estimate(p, navg=1):
    dtrue = np.linalg.norm(bx - p, axis=1)
    rs = -10*n*np.log10(dtrue) + rng.normal(0, sig/np.sqrt(navg), 4)
    dd = 10**(-rs/(10*n))
    A = 2*(bx[1:] - bx[0]); b = (dd[0]**2 - dd[1:]**2) + (bx[1:]**2).sum(1) - (bx[0]**2).sum()
    e = np.linalg.lstsq(A, b, rcond=None)[0]; return np.clip(e, [0, 0], [W, H])
P0 = np.array([3.0, 5.0]); cloud = np.array([estimate(P0) for _ in range(200)])
pos = rng.uniform([0.5, 0.5], [W - 0.5, H - 0.5], (5000, 2))
e1 = np.array([np.linalg.norm(estimate(p) - p) for p in pos]); e10 = np.array([np.linalg.norm(estimate(p, 10) - p) for p in pos])
CHECK['ble'] = dict(med=float(np.median(e1)), p90=float(np.percentile(e1, 90)), med10=float(np.median(e10)))
f, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.9), dpi=100)
a1.add_patch(plt.Rectangle((0, 0), W, H, fill=False, ec=INK)); a1.plot(bx[:, 0], bx[:, 1], 's', color=BLUE, ms=8, label='beacons')
a1.plot(cloud[:, 0], cloud[:, 1], '.', color=ORANGE, ms=3, label='estimates'); a1.plot(*P0, 'x', color=RED, ms=10, mew=2.5, label='true')
a1.set_aspect('equal'); a1.set_xlim(-0.5, W + 0.5); a1.set_ylim(-0.5, H + 0.5); a1.set_xlabel('x (m)'); a1.set_ylabel('y (m)'); a1.legend(fontsize=7.5, loc='upper right')
for e, col, lab in [(e1, ORANGE, 'single reading'), (e10, BLUE, '10-reading average')]:
    s = np.sort(e); a2.plot(s, np.arange(1, len(s) + 1)/len(s), color=col, lw=2, label=lab + ', median %.1f m' % np.median(e))
a2.set_xlabel('position error (m)'); a2.set_ylabel('fraction of trials'); a2.legend(fontsize=8.5, loc='lower right'); a2.set_xlim(0, 8)
save(f, O + 'b5c_blepos.png')
json.dump(CHECK, open('figs_check.json', 'w'), indent=1, default=float); print(json.dumps(CHECK, indent=1, default=float))
