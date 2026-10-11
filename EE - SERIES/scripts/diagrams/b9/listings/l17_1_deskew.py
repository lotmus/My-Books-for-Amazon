"""Deskew a voltage and a current channel: find the delay between their records of a common edge by
cross-correlating the derivatives, refine it to a fraction of a sample with a parabola, and show what
the uncorrected skew does to a switching-energy integral.

Run:  python l17_1_deskew.py      (simulation: the turn-off edge of Chapter 8, current probe 2.0 ns late)
With real data, load the two channels from the scope (Listing 16.1) instead of make_records().
"""
import numpy as np

def make_records(skew=2.0e-9, dt=0.1e-9):
    t = np.arange(-10e-9, 50e-9, dt)
    v = np.clip(t / 15e-9, 0, 1) * 400                       # drain voltage 0 -> 400 V in 15 ns
    i = lambda x: 20 * np.clip(1 - (x - 15e-9) / 15e-9, 0, 1)
    return t, v, i(t - skew), i(t)

def delay(t, a, b):
    """Delay of b relative to a, in seconds, from the cross-correlation of their derivatives."""
    da, db = np.gradient(a), np.gradient(b)
    c = np.correlate(db, da, mode='full')
    k = int(np.argmax(np.abs(c)))
    if 0 < k < c.size - 1:                                    # parabolic refinement
        y0, y1, y2 = abs(c[k - 1]), abs(c[k]), abs(c[k + 1])
        k = k + 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
    return (k - (a.size - 1)) * (t[1] - t[0])

def energy(t, v, i):
    return float(np.sum(v * i) * (t[1] - t[0]))

if __name__ == '__main__':
    t, v, i_meas, i_true = make_records()
    # the probes are deskewed on a fixture where both see the same edge: here the current edge itself
    d = delay(t, i_true, i_meas)
    print('measured skew of the current channel: %.2f ns' % (d * 1e9))
    i_fixed = np.interp(t + d, t, i_meas)
    print('Eoff uncorrected %.1f uJ, deskewed %.1f uJ, true %.1f uJ'
          % (energy(t, v, i_meas) * 1e6, energy(t, v, i_fixed) * 1e6, energy(t, v, i_true) * 1e6))
