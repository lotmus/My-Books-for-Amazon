"""Impedance sweep of a capacitor with an LCR meter or impedance analyzer: open and short
compensation, |Z| and phase from 100 Hz to 10 MHz, and a fit of C, ESR, and ESL.

SCPI in the style of the Keysight E4980A/E4990A family (FUNC:IMP ZTD returns |Z| and theta in degrees);
check your instrument's manual. Run:  python l13_1_lcr_sweep.py --sim
"""
import argparse
import math
import numpy as np

class SimLCR:
    """10 uF, ESR 10 mOhm, ESL 1 nH (Worked Example 13.4), 0.2 % magnitude noise."""
    C, ESR, ESL = 10e-6, 0.010, 1e-9
    def __init__(self):
        self.f, self.rng = 1e3, np.random.default_rng(13)
    def write(self, cmd):
        if cmd.startswith('FREQ '):
            self.f = float(cmd.split()[1])
    def query(self, cmd):
        if cmd == '*IDN?':
            return 'SIM,LCR,0,1.0'
        w = 2 * math.pi * self.f
        z = complex(self.ESR, w * self.ESL - 1 / (w * self.C)) * (1 + self.rng.normal(0, 0.002))
        return '%.6e,%.4f,+0' % (abs(z), math.degrees(math.atan2(z.imag, z.real)))

def fit_c_esr_esl(f, z):
    """Series R-L-C fit: Re(Z) -> ESR; Im(Z) = w L - 1/(w C) is linear in (w, -1/w)."""
    w = 2 * math.pi * f
    esr = np.median(z.real)
    (L, invC), *_ = np.linalg.lstsq(np.column_stack([w, -1 / w]), z.imag, rcond=None)
    return 1 / invC, esr, L

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('resource', nargs='?')
    ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    lcr = SimLCR() if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    print(lcr.query('*IDN?'))
    for cmd in ('*RST', 'FUNC:IMP ZTD', 'VOLT 0.5', 'APER MED'):
        lcr.write(cmd)
    if not a.sim:
        input('Open the fixture and press Enter'); lcr.write('CORR:OPEN:EXEC'); lcr.query('*OPC?')
        input('Short the fixture and press Enter'); lcr.write('CORR:SHOR:EXEC'); lcr.query('*OPC?')
        lcr.write('CORR:OPEN:STAT ON'); lcr.write('CORR:SHOR:STAT ON')
        input('Insert the part and press Enter')
    f = np.logspace(2, 7, 26)
    z = []
    for fk in f:
        lcr.write('FREQ %g' % fk)
        mag, deg = (float(x) for x in lcr.query('FETC?').split(',')[:2])
        z.append(mag * complex(math.cos(math.radians(deg)), math.sin(math.radians(deg))))
    z = np.array(z)
    c, esr, esl = fit_c_esr_esl(f, z)
    srf = 1 / (2 * math.pi * math.sqrt(esl * c))
    print('C = %.3g F, ESR = %.3g ohm, ESL = %.3g H, SRF = %.3g Hz' % (c, esr, esl, srf))
    k = int(np.argmin(abs(z)))
    print('minimum |Z| = %.3g ohm at %.3g Hz (sweep grid)' % (abs(z[k]), f[k]))

if __name__ == '__main__':
    main()
