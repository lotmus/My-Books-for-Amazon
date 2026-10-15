"""Noise of a DMM against its aperture: DC volts on a shorted input, NPLC from 0.02 to 100,
50 readings per setting, standard deviation in ppm of range and readings per second.

SCPI as in the Keysight 34465A/34470A command set (SCPI-1999 style); check your meter's manual.
Run:  python l12_1_dmm_nplc.py --sim
      python l12_1_dmm_nplc.py TCPIP0::192.168.1.60::inst0::INSTR --line 50
"""
import argparse
import time
import numpy as np

RANGE = 10.0                                     # volts

class SimDMM:
    """Noise 0.3 ppm of range at 10 PLC, scaling as 1/sqrt(NPLC); time per reading = NPLC/line + 1 ms."""
    def __init__(self, line):
        self.nplc, self.line, self.rng, self.t, self.n = 1.0, line, np.random.default_rng(12), 0.0, 1
    def write(self, cmd):
        if cmd.startswith('VOLT:DC:NPLC '):
            self.nplc = float(cmd.split()[1])
        elif cmd.startswith('SAMP:COUN '):
            self.n = int(cmd.split()[1])
    def query(self, cmd):
        if cmd == '*IDN?':
            return 'SIM,DMM,0,1.0'
        n = self.n
        self.t += n * (self.nplc / self.line + 1e-3)
        sigma = 0.3e-6 * RANGE * np.sqrt(10 / self.nplc)
        return ','.join('%.9e' % x for x in self.rng.normal(0, sigma, n))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('resource', nargs='?')
    ap.add_argument('--sim', action='store_true')
    ap.add_argument('--line', type=float, default=60.0)
    a = ap.parse_args()
    dmm = SimDMM(a.line) if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    if not a.sim:
        dmm.timeout = 120000
    print(dmm.query('*IDN?'))
    for cmd in ('*RST', 'CONF:VOLT:DC %g' % RANGE, 'VOLT:DC:ZERO:AUTO ON', 'TRIG:SOUR IMM', 'SAMP:COUN 50'):
        dmm.write(cmd)
    print(' NPLC   noise (ppm of range)   readings/s')
    for nplc in (0.02, 0.2, 1, 10, 100):
        dmm.write('VOLT:DC:NPLC %g' % nplc)
        t0 = dmm.t if a.sim else time.perf_counter()
        r = np.array([float(x) for x in dmm.query('READ?').split(',')])
        dt = (dmm.t if a.sim else time.perf_counter()) - t0
        print('%6g   %10.2f            %8.1f' % (nplc, r.std(ddof=1) / RANGE * 1e6, r.size / dt))

if __name__ == '__main__':
    main()
