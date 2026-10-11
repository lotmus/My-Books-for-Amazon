"""Radiated-emissions precompliance scan: read a peak-detector sweep from a spectrum analyzer, convert to
field strength with the antenna factor and cable loss, compare with the CISPR 32 Class B limit at 3 m, and
list the frequencies that need a quasi-peak remeasurement (margin below 6 dB).

SCPI in the common Keysight X-Series / R&S FSx style (FREQ:STAR, FREQ:STOP, BAND, DET, TRAC:DATA?); the
antenna factor table comes from your antenna's calibration certificate. Run:  python l33_2_emc_prescan.py --sim
"""
import argparse
import numpy as np

AF_TABLE = [(30e6, 18.0), (100e6, 10.0), (200e6, 11.0), (300e6, 14.0), (500e6, 18.0), (1000e6, 24.0)]  # dB/m, example biconilog
CABLE = [(30e6, 0.5), (1000e6, 3.0)]                                                                   # dB

def interp(table, f):
    fs, vs = zip(*table)
    return np.interp(np.log10(f), np.log10(fs), vs)

def limit_3m_class_b(f):
    """CISPR 32 Class B radiated, 3 m quasi-peak: 40 dBuV/m 30-230 MHz, 47 dBuV/m 230-1000 MHz."""
    return np.where(f <= 230e6, 40.0, 47.0)

class SimSA:
    """Analyzer with a device radiating a 48 MHz clock comb and a 150 MHz harmonic; input in dBm."""
    def __init__(self):
        self.start, self.stop, self.rng = 30e6, 1e9, np.random.default_rng(33)
    def write(self, cmd):
        k, v = cmd.split()
        if k == 'FREQ:STAR': self.start = float(v)
        elif k == 'FREQ:STOP': self.stop = float(v)
    def query(self, cmd):
        if cmd == '*IDN?':
            return 'SIM,SA,0,1.0'
        f = np.linspace(self.start, self.stop, 2001)
        p = -100 + self.rng.normal(0, 1.5, f.size)                                   # dBm floor with preamp
        for fc, dbuv in ((48e6, 15), (96e6, 20), (144e6, 18), (150e6, 25), (240e6, 22), (480e6, 17)):
            p = np.maximum(p, dbuv - 107 - ((f - fc) / 0.6e6) ** 2)                # dBuV at the input -> dBm
        return ','.join('%.2f' % x for x in p)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('resource', nargs='?'); ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    sa = SimSA() if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    print(sa.query('*IDN?'))
    for c in ('FREQ:STAR 30e6', 'FREQ:STOP 1e9', 'BAND 120e3'):
        sa.write(c)
    if not a.sim:
        sa.write('DET POS'); sa.write('SWE:POIN 2001')
    f = np.linspace(30e6, 1e9, 2001)
    dbm = np.array([float(x) for x in sa.query('TRAC:DATA? TRACE1').split(',')])
    e = dbm + 107 + interp(AF_TABLE, f) + interp(CABLE, f)                          # dBuV/m
    margin = limit_3m_class_b(f) - e
    k = np.where((margin[1:-1] < margin[:-2]) & (margin[1:-1] <= margin[2:]) & (margin[1:-1] < 6))[0] + 1
    print('freq (MHz)  field (dBuV/m)  limit  margin (dB)  -> remeasure with QP')
    for i in k:
        print('%9.2f  %13.1f  %6.0f  %10.1f' % (f[i] / 1e6, e[i], limit_3m_class_b(f[i]), margin[i]))
    return f, e, margin

if __name__ == '__main__':
    main()
