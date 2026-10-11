"""Spur search with a spectrum analyzer: set span, RBW, detector, and attenuation; read the trace; list the
peaks above a mask; repeat with 10 dB more attenuation and flag spurs that move (analyzer-generated).

SCPI in the common Keysight X-Series / R&S FSx style (FREQ:CENT, FREQ:SPAN, BAND, INP:ATT, DET, TRAC:DATA?);
check the programming guide. Run:  python l21_1_sa_spur_search.py --sim
"""
import argparse
import numpy as np

class SimSA:
    """NF 24 dB analyzer, TOI +15 dBm; input: carrier -10 dBm at 100 MHz, device spurs at 103 and 112 MHz."""
    def __init__(self):
        self.cf, self.span, self.rbw, self.att, self.rng = 100e6, 30e6, 10e3, 10.0, np.random.default_rng(21)
    def write(self, cmd):
        k, v = cmd.split()
        val = float(v)
        if k == 'FREQ:CENT': self.cf = val
        elif k == 'FREQ:SPAN': self.span = val
        elif k == 'BAND': self.rbw = val
        elif k == 'INP:ATT': self.att = val
    def query(self, cmd):
        if cmd == '*IDN?':
            return 'SIM,SA,0,1.0'
        f = self.cf + np.linspace(-self.span / 2, self.span / 2, 1001)
        danl = -174 + 24 + 10 * np.log10(self.rbw) + (self.att - 10)          # attenuation adds noise
        p = 10 ** ((danl + self.rng.normal(0, 1, f.size)) / 10)
        mix = -10 - self.att                                                  # carrier level at the mixer
        sigs = [(100e6, -10), (103e6, -78), (112e6, -85),
                (106e6, mix + 2 * (mix - 15) + self.att)]                     # analyzer IM3 product (tone at 103)
        for fs, lv in sigs:
            p += 10 ** (lv / 10) * np.exp(-0.5 * ((f - fs) / (self.rbw / 2.355)) ** 2)
        return ','.join('%.2f' % x for x in 10 * np.log10(p))

def peaks(f, p, limit):
    k = np.where((p[1:-1] > p[:-2]) & (p[1:-1] >= p[2:]) & (p[1:-1] > limit))[0] + 1
    return [(f[i], p[i]) for i in k]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('resource', nargs='?')
    ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    sa = SimSA() if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    print(sa.query('*IDN?'))
    cf, span, rbw, limit = 107.5e6, 15e6, 10e3, -95.0
    for cmd in ('FREQ:CENT %g' % cf, 'FREQ:SPAN %g' % span, 'BAND %g' % rbw):
        sa.write(cmd)
    if not a.sim:
        sa.write('DET POS'); sa.write('SWE:POIN 1001')
    f = cf + np.linspace(-span / 2, span / 2, 1001)
    found = {}
    for att in (10, 20):
        sa.write('INP:ATT %g' % att)
        p = np.array([float(x) for x in sa.query('TRAC:DATA? TRACE1').split(',')])
        found[att] = peaks(f, p, limit)
    print('freq (MHz)   level @10 dB   level @20 dB   verdict')
    for fr, lv in found[10]:
        other = [l2 for f2, l2 in found[20] if abs(f2 - fr) < 2 * rbw]
        l2 = other[0] if other else float('nan')
        verdict = 'device' if other and abs(l2 - lv) < 3 else 'analyzer (moved)'
        print('%9.3f   %10.1f   %12.1f   %s' % (fr / 1e6, lv, l2, verdict))

if __name__ == '__main__':
    main()
