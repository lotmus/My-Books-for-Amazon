"""Thermal camera emissivity and reflected-temperature correction, in the camera's own band (8 to 14 um,
Planck radiance integrated numerically) and in the total-radiation (T^4) approximation for comparison.

The camera measures radiance W = e*W(T_obj) + (1 - e)*W(T_refl) (atmosphere neglected at short range) and
inverts it. Run:  python l33_1_thermal.py  [apparent_C emissivity reflected_C]
"""
import math
import sys
import numpy as np

H, C, K = 6.62607015e-34, 299792458.0, 1.380649e-23
LAM = np.linspace(8e-6, 14e-6, 600)

def band_radiance(t_k):
    """Planck spectral radiance integrated over 8-14 um (W m^-2 sr^-1)."""
    b = 2 * H * C ** 2 / LAM ** 5 / (np.exp(H * C / (LAM * K * t_k)) - 1)
    return float(np.sum(b) * (LAM[1] - LAM[0]))

def invert(w, lo=150.0, hi=1500.0):
    for _ in range(80):                                                    # bisection on temperature
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if band_radiance(mid) < w else (lo, mid)
    return (lo + hi) / 2

def true_temp(apparent_c, eps, refl_c, band=True):
    """Object temperature (C) from a reading taken with emissivity set to 1."""
    ta, tr = apparent_c + 273.15, refl_c + 273.15
    if band:
        w = (band_radiance(ta) - (1 - eps) * band_radiance(tr)) / eps
        return invert(w) - 273.15
    return ((ta ** 4 - (1 - eps) * tr ** 4) / eps) ** 0.25 - 273.15

if __name__ == '__main__':
    app, eps, refl = (float(x) for x in sys.argv[1:4]) if len(sys.argv) > 3 else (60.0, 0.85, 25.0)
    print('reading %.1f C at e = 1, true e = %.2f, reflected %.1f C:' % (app, eps, refl))
    print('  8-14 um band: object %.1f C; T^4 approximation: %.1f C' % (true_temp(app, eps, refl), true_temp(app, eps, refl, band=False)))
