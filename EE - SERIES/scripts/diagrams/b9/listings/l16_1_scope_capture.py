"""Capture one channel over SCPI as a binary block, scale it with the preamble, and measure the
10 % to 90 % rise time with linear interpolation between samples.

SCPI in the Keysight InfiniiVision style (:WAV:SOUR, :WAV:FORM BYTE, :WAV:PRE?, :WAV:DATA?); Tektronix,
R&S, Rigol, and Siglent use different command names for the same steps, so check the programming guide.
Run:  python l16_1_scope_capture.py --sim
"""
import argparse
import math
import numpy as np

class SimScope:
    """A 2.0 ns (10-90 %) edge through a Gaussian 500 MHz response, 8-bit samples at 5 GS/s."""
    def __init__(self):
        dt = 0.2e-9; t = np.arange(-50e-9, 50e-9, dt)
        sig = lambda tr: 0.5 * (1 + np.vectorize(math.erf)(t / (tr / 2.563) / math.sqrt(2)))
        tr = math.hypot(2.0e-9, 0.35 / 500e6)                 # Gaussian edges add in quadrature
        v = 3.3 * sig(tr) + np.random.default_rng(16).normal(0, 0.004, t.size)
        self.yinc, self.yorg = 4.0 / 256, -0.35
        self.codes = np.clip(np.round((v - self.yorg) / self.yinc), 0, 255).astype(np.uint8)
        self.pre = '0,0,%d,1,%.6e,%.6e,0,%.6e,%.6e,0' % (t.size, dt, t[0], self.yinc, self.yorg)
    def write(self, cmd):
        pass
    def query(self, cmd):
        return {'*IDN?': 'SIM,SCOPE,0,1.0', ':WAV:PRE?': self.pre}[cmd]
    def query_binary_values(self, cmd, datatype='B', container=np.array):
        return container(self.codes)

def rise_time(t, v, lo=0.1, hi=0.9):
    """10-90 % rise time of the first rising edge, levels from the settled bottom and top."""
    base, top = np.median(v[: v.size // 5]), np.median(v[-v.size // 5:])
    def cross(level):
        y = base + level * (top - base)
        k = int(np.argmax(v >= y))
        return t[k - 1] + (y - v[k - 1]) * (t[k] - t[k - 1]) / (v[k] - v[k - 1])
    return cross(hi) - cross(lo), base, top

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('resource', nargs='?')
    ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    sc = SimScope() if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    print(sc.query('*IDN?'))
    for cmd in (':WAV:SOUR CHAN1', ':WAV:FORM BYTE', ':WAV:POIN:MODE RAW', ':WAV:POIN 1000', ':DIG CHAN1'):
        sc.write(cmd)
    p = [float(x) for x in sc.query(':WAV:PRE?').split(',')]
    n, xinc, xorg, yinc, yorg = int(p[2]), p[4], p[5], p[7], p[8]
    codes = sc.query_binary_values(':WAV:DATA?', datatype='B', container=np.array)
    t = xorg + xinc * np.arange(n)
    v = yorg + yinc * codes.astype(float)                  # this preamble: volts = origin + increment x code
    tr, base, top = rise_time(t, v)
    print('%d points, %.3g s/pt; base %.3f V, top %.3f V' % (n, xinc, base, top))
    print('rise time 10-90 %%: %.2f ns (scope 0.70 ns removed in quadrature: %.2f ns)'
          % (tr * 1e9, math.sqrt(max(tr ** 2 - 0.7e-9 ** 2, 0)) * 1e9))

if __name__ == '__main__':
    main()
