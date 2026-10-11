"""Forward I-V of a diode with an SMU: logarithmic current sweep, voltage compliance, four-wire sensing,
then a fit of the ideality factor n, saturation current Is, and series resistance Rs.

SCPI as in the Keithley 2450 SCPI command set; other SMUs differ, so check the manual.
Run:  python l06_1_smu_sweep.py --sim
      python l06_1_smu_sweep.py USB0::0x05E6::0x2450::04412345::INSTR
"""
import argparse
import math
import numpy as np

VT = 0.025852                    # thermal voltage kT/q at 300 K (V)

class SimSMU:
    """A diode with Is = 2.5 nA, n = 1.75, Rs = 2 ohm, plus 20 uV of measurement noise."""
    def __init__(self):
        self.i = 0.0
        self.rng = np.random.default_rng(6)
    def write(self, cmd):
        if cmd.startswith(':SOUR:CURR '):
            self.i = float(cmd.split()[1])
    def query(self, cmd):
        if cmd == '*IDN?':
            return 'SIM,SMU,0,1.0'
        v = 1.75 * VT * math.log(self.i / 2.5e-9 + 1) + 2.0 * self.i
        return '%.7e' % (min(v, 2.0) + self.rng.normal(0, 20e-6))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('resource', nargs='?')
    ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    smu = SimSMU() if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    print(smu.query('*IDN?'))
    for cmd in ('*RST', ':SOUR:FUNC CURR', ':SOUR:CURR:VLIM 2', ':SENS:FUNC "VOLT"',
                ':SENS:VOLT:RSEN ON', ':SENS:VOLT:NPLC 1', ':OUTP ON'):
        smu.write(cmd)
    currents = np.logspace(-9, -2, 36)        # 1 nA to 10 mA, 5 points per decade
    volts = []
    for i in currents:
        smu.write(':SOUR:CURR %.4e' % i)
        volts.append(float(smu.query(':MEAS:VOLT?')))
    smu.write(':OUTP OFF')
    v = np.array(volts)
    fit = (currents >= 1e-7) & (currents <= 1e-4)    # ideal region: above leakage, below Rs
    slope, icept = np.polyfit(v[fit], np.log(currents[fit]), 1)
    n = 1 / (slope * VT)
    i_s = math.exp(icept)
    v_ideal = n * VT * math.log(currents[-1] / i_s + 1)
    rs = (v[-1] - v_ideal) / currents[-1]
    print('points %d, V(10 mA) = %.4f V' % (len(v), v[-1]))
    print('n = %.3f, Is = %.2f nA, Rs = %.2f ohm' % (n, i_s * 1e9, rs))
    print('slope %.1f mV per decade' % (n * VT * math.log(10) * 1e3))

if __name__ == '__main__':
    main()
