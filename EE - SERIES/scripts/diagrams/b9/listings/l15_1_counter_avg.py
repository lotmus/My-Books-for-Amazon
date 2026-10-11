"""Frequency readings from a counter and their statistics: mean, standard deviation, and the
overlapping Allan deviation for averaging times from 0.1 s to 100 s.

SCPI in the style of the Keysight 53230A (CONF:FREQ, SENS:FREQ:GATE:TIME, READ?); check your manual.
Run:  python l15_1_counter_avg.py --sim
"""
import argparse
import numpy as np

class SimCounter:
    """A 10 MHz OCXO: white frequency noise 3e-11 at 0.1 s, random walk 2e-12 per sqrt(s), offset +4.2e-9."""
    def __init__(self):
        self.rng, self.n = np.random.default_rng(15), 1
    def write(self, cmd):
        if cmd.startswith('SAMP:COUN '):
            self.n = int(cmd.split()[1])
    def query(self, cmd):
        if cmd == '*IDN?':
            return 'SIM,COUNTER,0,1.0'
        white = self.rng.normal(0, 3e-11, self.n)
        walk = np.cumsum(self.rng.normal(0, 2e-12 * np.sqrt(0.1), self.n))
        return ','.join('%.6f' % x for x in 10e6 * (1 + 4.2e-9 + white + walk))

def adev(y, m):
    """Overlapping Allan deviation of fractional-frequency samples y at averaging factor m."""
    c = np.cumsum(np.insert(y, 0, 0.0))
    avg = (c[m:] - c[:-m]) / m
    d = avg[m:] - avg[:-m]
    return np.sqrt(0.5 * np.mean(d ** 2))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('resource', nargs='?')
    ap.add_argument('--sim', action='store_true')
    ap.add_argument('--nominal', type=float, default=10e6)
    a = ap.parse_args()
    ctr = SimCounter() if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    if not a.sim:
        ctr.timeout = 600000
    print(ctr.query('*IDN?'))
    for cmd in ('*RST', 'CONF:FREQ %g' % a.nominal, 'SENS:FREQ:GATE:TIME 0.1', 'ROSC:SOUR EXT', 'SAMP:COUN 6000'):
        ctr.write(cmd)                                  # 6000 x 0.1 s = 10 minutes; external 10 MHz reference
    f = np.array([float(x) for x in ctr.query('READ?').split(',')])
    y = f / a.nominal - 1
    print('mean offset %+.3e, standard deviation %.2e (fractional)' % (y.mean(), y.std(ddof=1)))
    for m in (1, 10, 100, 1000):
        print('tau = %6.1f s   ADEV = %.2e' % (0.1 * m, adev(y, m)))

if __name__ == '__main__':
    main()
