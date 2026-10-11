"""From measured diode data to a SPICE .model line: fit, residuals, validation, valid range.

The "measured" data here are synthetic: a diode with two current components (ideality 1 and 2), series
resistance, and 0.3 mV of meter noise, which a single-exponential SPICE diode can only approximate.
Steps: (1)-(2) fit Is, N and Rs together by least squares on 1 uA..20 mA, (3) show residuals in the fit range,
(4) validate on data not used in the fit, (5) fit Cjo, Vj, M to C-V data, (6) write the model and its range.
Pure NumPy; run: python l08_1_fit_diode.py
"""
import math
import numpy as np

VT = 0.025852
rng = np.random.default_rng(8)

def true_v(i, is1=2.0e-15, is2=2.0e-11, rs=0.6):
    """Solve I = Is1(exp(Vj/Vt)-1) + Is2(exp(Vj/2Vt)-1) for the junction voltage, then add I*Rs."""
    vj = np.empty_like(i)
    for k, ik in enumerate(i):
        lo, hi = 0.0, 1.2
        for _ in range(60):                          # bisection: robust and short
            mid = (lo + hi) / 2
            f = is1 * math.expm1(mid / VT) + is2 * math.expm1(mid / (2 * VT)) - ik
            lo, hi = (mid, hi) if f < 0 else (lo, mid)
        vj[k] = (lo + hi) / 2
    return vj + i * rs

i_meas = np.logspace(-8, -1, 71)                      # 10 nA .. 100 mA, 10 points per decade
v_meas = true_v(i_meas) + rng.normal(0, 0.3e-3, i_meas.size)

def spice_v(i, i_s, n, rs):
    return n * VT * np.log(i / i_s + 1) + i * rs

fit = (i_meas >= 1e-6) & (i_meas <= 20e-3)                # fit range, stated with the model
A = np.column_stack([np.log(i_meas[fit]), np.ones(fit.sum()), i_meas[fit]])
(a1, a0, RS), *_ = np.linalg.lstsq(A, v_meas[fit], rcond=None)   # V = N Vt ln I - N Vt ln Is + Rs I
N = a1 / VT
IS = math.exp(-a0 / a1)
used = fit
res = (v_meas - spice_v(i_meas, IS, N, RS)) * 1e3        # residuals in mV
print('joint fit 1 uA..20 mA: N = %.3f, IS = %.3g A, RS = %.3f ohm' % (N, IS, RS))
print('residuals in the fit ranges: rms %.2f mV, max %.2f mV' % (np.sqrt(np.mean(res[used] ** 2)), np.max(np.abs(res[used]))))
for lab, m in (('validation 10..100 nA', (i_meas >= 1e-8) & (i_meas <= 1e-7)),
               ('validation 30..100 mA', i_meas >= 30e-3)):
    print('%s: max error %.1f mV' % (lab, np.max(np.abs(res[m]))))

# C-V: Cj = Cjo / (1 + Vr/Vj)^M, measured at 1 MHz from 0 to 20 V reverse
vr = np.linspace(0, 20, 21)
c_meas = 4.0e-12 / (1 + vr / 0.60) ** 0.45 * (1 + rng.normal(0, 0.002, vr.size))
best = None
for vj in np.arange(0.30, 1.20, 0.005):                # grid over Vj, linear fit for Cjo and M
    x = np.log(1 + vr / vj)
    mm, b = np.polyfit(x, np.log(c_meas), 1)
    err = np.sum((np.log(c_meas) - (b + mm * x)) ** 2)
    if best is None or err < best[0]:
        best = (err, vj, -mm, math.exp(b))
_, VJ, M, CJO = best
print('C-V fit 0..20 V: CJO = %.2f pF, VJ = %.2f V, M = %.3f' % (CJO * 1e12, VJ, M))
print('.model DFIT D(IS=%.3g N=%.3f RS=%.3f CJO=%.3gp VJ=%.2f M=%.3f)' % (IS, N, RS, CJO * 1e12, VJ, M))
print('* valid 1 uA..20 mA forward at 25 C, 0..20 V reverse; not for leakage, breakdown, or temperature')
