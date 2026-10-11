"""Sweep S11 and S21 on a VNA, read complex data, and compute return loss, VSWR, impedance, insertion
loss, and group delay.

SCPI in the Keysight ENA/PNA style (CALC:PAR:DEF, CALC:DATA? SDATA returns re,im pairs); R&S ZNx and
others differ in names. Run:  python l25_1_vna_sweep.py --sim
"""
import argparse
import numpy as np

Z0 = 50.0

class SimVNA:
    """A second-order band-pass at 2 GHz (Q = 20) with 0.2 dB of loss and a small mismatch at the center."""
    def __init__(self):
        self.f = np.linspace(1.8e9, 2.2e9, 401); self.par = 'S21'
    def write(self, cmd):
        if cmd.startswith('CALC:PAR:DEF'):
            self.par = cmd.split()[-1]
    def query(self, cmd):
        if cmd == '*IDN?':
            return 'SIM,VNA,0,1.0'
        if cmd.startswith('SENS:FREQ:DATA?'):
            return ','.join('%.6e' % x for x in self.f)
        x = 20 * (self.f / 2e9 - 2e9 / self.f)
        s21 = 0.977 / (1 + 1j * x)                        # 0.2 dB of loss in the passband
        s11 = (0.03 + 1j * x) / (1 + 1j * x)              # 30 dB return loss at the center
        s = s21 if self.par == 'S21' else s11
        return ','.join('%.8e,%.8e' % (z.real, z.imag) for z in s)

def complex_trace(txt):
    v = np.array([float(x) for x in txt.split(',')])
    return v[0::2] + 1j * v[1::2]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('resource', nargs='?')
    ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    vna = SimVNA() if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    print(vna.query('*IDN?'))
    if not a.sim:
        for cmd in ('SENS:FREQ:STAR 1.8E9', 'SENS:FREQ:STOP 2.2E9', 'SENS:SWE:POIN 401', 'SENS:BAND 1E3'):
            vna.write(cmd)
    f = np.array([float(x) for x in vna.query('SENS:FREQ:DATA?').split(',')])
    data = {}
    for par in ('S11', 'S21'):
        vna.write('CALC:PAR:DEF %s' % par)
        if not a.sim:
            vna.write('INIT:IMM'); vna.query('*OPC?')
        data[par] = complex_trace(vna.query('CALC:DATA? SDATA'))
    s11, s21 = data['S11'], data['S21']
    rl = -20 * np.log10(np.abs(s11)); vswr = (1 + np.abs(s11)) / (1 - np.abs(s11) + 1e-12)
    z = Z0 * (1 + s11) / (1 - s11)
    phase = np.unwrap(np.angle(s21))
    gd = -np.gradient(phase, 2 * np.pi * f)
    k = int(np.argmin(abs(f - 2e9)))
    print('at %.3f GHz: IL %.2f dB, RL %.1f dB, VSWR %.2f, Z = %.1f%+.1fj ohm, group delay %.1f ns'
          % (f[k] / 1e9, -20 * np.log10(abs(s21[k])), rl[k], vswr[k], z[k].real, z[k].imag, gd[k] * 1e9))
    lo, hi = f[np.where(20 * np.log10(np.abs(s21)) >= -3)[0][[0, -1]]]
    print('-3 dB band %.1f .. %.1f MHz (bandwidth %.1f MHz)' % (lo / 1e6, hi / 1e6, (hi - lo) / 1e6))

if __name__ == '__main__':
    main()
