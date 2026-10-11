"""Power up a three-rail board in sequence with current limits and OVP, then check the rails (PyVISA, SCPI).

Commands follow the common SCPI power-supply subset (INST:NSEL, VOLT, CURR, VOLT:PROT, OUTP, MEAS);
spellings differ between models, so check your supply's programming manual.
Run:  python l05_1_psu_sequence.py --sim          (no hardware)
      python l05_1_psu_sequence.py TCPIP0::192.168.1.30::INSTR
"""
import argparse
import time

RAILS = [  # channel, volts, current limit (A), OVP (V), wait after turn-on (s)
    (1, 3.3, 0.50, 3.6, 0.010),
    (2, 1.8, 0.30, 2.0, 0.010),
    (3, 5.0, 1.00, 5.5, 0.000),
]

class SimPSU:
    """Stand-in for a three-channel supply driving a resistive load on each channel."""
    LOAD = {1: 11.0, 2: 9.0, 3: 10.0}   # ohms
    def __init__(self):
        self.ch, self.set, self.on = 1, {}, {}
    def write(self, cmd):
        key, _, val = cmd.partition(' ')
        if key == 'INST:NSEL':
            self.ch = int(val)
        elif key in ('VOLT', 'CURR', 'VOLT:PROT'):
            self.set[(self.ch, key)] = float(val)
        elif key == 'OUTP':
            self.on[self.ch] = (val == 'ON')
    def query(self, cmd):
        if cmd == '*IDN?':
            return 'SIM,PSU3,0,1.0'
        if cmd == 'SYST:ERR?':
            return '+0,"No error"'
        v = self.set.get((self.ch, 'VOLT'), 0.0) if self.on.get(self.ch) else 0.0
        i = min(v / self.LOAD[self.ch], self.set.get((self.ch, 'CURR'), 0.0))   # CV, or CC at the limit
        v = i * self.LOAD[self.ch]
        return '%.4f' % (v if cmd == 'MEAS:VOLT?' else i)

def check_error(psu):
    err = psu.query('SYST:ERR?')
    if not err.startswith('+0') and not err.startswith('0'):
        raise RuntimeError('instrument error: ' + err)

def all_off(psu):
    for ch, *_ in reversed(RAILS):          # reverse order on the way down
        psu.write('INST:NSEL %d' % ch)
        psu.write('OUTP OFF')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('resource', nargs='?')
    ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    if a.sim:
        psu = SimPSU()
    else:
        import pyvisa
        psu = pyvisa.ResourceManager().open_resource(a.resource)
        psu.timeout = 5000
    print(psu.query('*IDN?'))
    all_off(psu)
    for ch, volts, ilim, ovp, _ in RAILS:     # program everything with outputs off
        psu.write('INST:NSEL %d' % ch)
        psu.write('VOLT %.3f' % volts)
        psu.write('CURR %.3f' % ilim)
        psu.write('VOLT:PROT %.3f' % ovp)
        check_error(psu)
    try:
        for ch, volts, ilim, _, wait in RAILS:
            psu.write('INST:NSEL %d' % ch)
            psu.write('OUTP ON')
            time.sleep(wait)
            v = float(psu.query('MEAS:VOLT?'))
            i = float(psu.query('MEAS:CURR?'))
            ok = abs(v - volts) <= 0.05 * volts and i < 0.98 * ilim
            print('rail %d: %.3f V  %.3f A  %s' % (ch, v, i, 'ok' if ok else 'FAIL'))
            if not ok:
                raise RuntimeError('rail %d out of limits (current limit reached?)' % ch)
    except Exception:
        all_off(psu)
        raise

if __name__ == '__main__':
    main()
