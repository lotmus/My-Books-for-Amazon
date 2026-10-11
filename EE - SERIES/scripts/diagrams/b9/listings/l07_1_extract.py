"""Device parameters from curve-tracer data: diode, BJT, and MOSFET.

The functions take measured arrays (from a curve tracer's CSV export or an SMU sweep) and return the
parameters of Chapter 7. Run without arguments to test them on synthetic curves from known models.
"""
import math
import numpy as np

VT = 0.025852                                   # kT/q at 300 K (V)

def diode_params(v, i, lo=1e-6, hi=1e-4):
    """Ideality n and Is from the straight part of log(I) vs V; Rs from the excess drop at the top point."""
    m = (i >= lo) & (i <= hi)
    slope, icept = np.polyfit(v[m], np.log(i[m]), 1)
    n, i_s = 1 / (slope * VT), math.exp(icept)
    rs = (v[-1] - n * VT * math.log(i[-1] / i_s + 1)) / i[-1]
    return n, i_s, rs, n * VT * math.log(10)    # last: mV per decade (in V)

def zener_rz(v, i, i1, i2):
    """Dynamic resistance between two currents on the reverse curve."""
    return (np.interp(i2, i, v) - np.interp(i1, i, v)) / (i2 - i1)

def early_voltage(vce, ic, v1=2.0, v2=10.0):
    """Extrapolate the active-region line of one output curve back to Ic = 0."""
    i1, i2 = np.interp(v1, vce, ic), np.interp(v2, vce, ic)
    g = (i2 - i1) / (v2 - v1)
    return -(v1 - i1 / g), 1 / g                # VA (positive number), output resistance

def vth_sqrt(vgs, idd, frac=(0.3, 0.7)):
    """Saturation (Vds = Vgs) method: extrapolate sqrt(Id) at its steepest region to zero."""
    s = np.sqrt(idd)
    k = np.argmax(np.gradient(s, vgs))
    a, b = np.polyfit(vgs[k - 3:k + 4], s[k - 3:k + 4], 1)
    return -b / a

def vth_const_current(vgs, idd, i_ref=250e-6):
    """Constant-current method: Vgs at which Id reaches i_ref (datasheet style)."""
    return float(np.interp(math.log(i_ref), np.log(idd), vgs))

def subthreshold_slope(vgs, idd, lo=1e-9, hi=1e-7):
    m = (idd >= lo) & (idd <= hi)
    slope = np.polyfit(np.log10(idd[m]), vgs[m], 1)[0]
    return slope                                 # V per decade

# ------------------------------------------------------------- synthetic test devices
def diode_model(i, i_s=2.682e-9, n=1.836, rs=0.5664):
    return n * VT * np.log(i / i_s + 1) + rs * i

def bjt_ic(vce, ib, beta=200.0, va=75.0, vsat=0.08):
    return beta * ib * (1 + vce / va) * (1 - np.exp(-vce / vsat))

def mos_id(vgs, vds, k=2.0, vth=1.6, n=1.4, lam=0.01):
    """EKV-style smooth model: square law above Vth, exponential below, saturation with lambda."""
    f = lambda v: np.log1p(np.exp(v / (2 * n * VT))) ** 2
    ispec = 2 * n * k * VT ** 2
    return ispec * (f(vgs - vth) - f(vgs - vth - n * vds)) * (1 + lam * vds)

if __name__ == '__main__':
    i = np.logspace(-9, -1, 81)
    n, i_s, rs, dec = diode_params(diode_model(i), i)
    print('diode: n = %.3f, Is = %.2f nA, Rs = %.3f ohm, %.1f mV/decade, Vf(10 mA) = %.3f V'
          % (n, i_s * 1e9, rs, dec * 1e3, diode_model(10e-3)))
    iz = np.linspace(0.1e-3, 20e-3, 200)
    vz = 5.1 + 15.0 * (iz - 5e-3)
    print('zener: Vz(5 mA) = %.3f V, rz(1..10 mA) = %.1f ohm' % (np.interp(5e-3, iz, vz), zener_rz(vz, iz, 1e-3, 10e-3)))
    vce = np.linspace(0, 20, 401)
    va, ro = early_voltage(vce, bjt_ic(vce, 20e-6))
    print('bjt: Ic(Ib 20 uA, 5 V) = %.3f mA, VA = %.1f V, ro = %.1f kohm' % (bjt_ic(5.0, 20e-6) * 1e3, va, ro / 1e3))
    vgs = np.linspace(0.5, 5, 451)
    sat = mos_id(vgs, vgs)
    print('mosfet: Vth(sqrt) = %.3f V, Vth(250 uA) = %.3f V, S = %.1f mV/decade'
          % (vth_sqrt(vgs, sat), vth_const_current(vgs, sat), subthreshold_slope(vgs, sat) * 1e3))
    for vg in (4.5, 10.0):
        print('mosfet: Rds(on) at Vgs %.1f V = %.1f mohm' % (vg, 0.1 / mos_id(vg, 0.1) * 1e3))
    idd = mos_id(np.array([3.0, 3.01]), 10.0)
    print('mosfet: Id(Vgs 3 V, Vds 10 V) = %.3f A, gm = %.2f S' % (idd[0], (idd[1] - idd[0]) / 0.01))
