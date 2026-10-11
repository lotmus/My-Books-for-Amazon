"""Scan an antenna's S11 with a NanoVNA or LiteVNA over USB serial, then report the resonance, the return
loss, the VSWR, and the 2:1 VSWR bandwidth, with the uncertainty set by the analyzer's S11 noise floor.

The NanoVNA-H/-H4 and LiteVNA firmwares accept 'scan <start> <stop> <points> <outmask>' (outmask 1 =
frequency, 2 = S11, 4 = S21) and answer one line per point; type 'help' in a terminal to check yours.
Calibrate (open, short, load) on the device at the cable end first. Run:  python l37_1_nanovna_scan.py --sim
"""
import argparse
import math
import numpy as np

class SimVNA:
    """A 435 MHz quarter-wave antenna: series RLC, 36 ohm at resonance, Q 12, seen through a calibrated cable."""
    def __init__(self, seed=37):
        self.rng = np.random.default_rng(seed)
    def command(self, line):
        _, a, b, n, mask = line.split()
        f = np.linspace(float(a), float(b), int(n)); f0, r, q = 435e6, 36.0, 12.0
        x = r * q * (f / f0 - f0 / f)
        g = (r + 1j * x - 50) / (r + 1j * x + 50)
        g = g + 10 ** (-50 / 20) * np.exp(2j * np.pi * self.rng.random(f.size))     # residual: -50 dB floor
        return ['%d %.6f %.6f' % (fk, gk.real, gk.imag) for fk, gk in zip(f, g)]

class SerialVNA:
    def __init__(self, port):
        import serial                                                               # pip install pyserial
        self.s = serial.Serial(port, 115200, timeout=5)
    def command(self, line):
        self.s.reset_input_buffer(); self.s.write((line + '\r').encode())
        out = self.s.read_until(b'ch> ').decode(errors='replace').splitlines()
        return [l for l in out[1:] if l and not l.startswith('ch>')]                # drop echo and prompt

def analyze(lines, floor_db=-50.0):
    d = np.array([[float(x) for x in l.split()] for l in lines])
    f, g = d[:, 0], d[:, 1] + 1j * d[:, 2]
    rl = -20 * np.log10(np.abs(g)); vswr = (1 + np.abs(g)) / (1 - np.abs(g))
    k = int(np.argmax(rl)); e = 10 ** (floor_db / 20)
    lo_g, hi_g = abs(g[k]) + e, max(abs(g[k]) - e, 1e-6)
    band = f[vswr <= 2.0]
    return f[k], rl[k], vswr[k], (-20 * math.log10(lo_g), -20 * math.log10(hi_g)), (band.min(), band.max()) if band.size else None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('port', nargs='?'); ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    vna = SimVNA() if a.sim else SerialVNA(a.port)
    f0, rl, sw, (rmin, rmax), band = analyze(vna.command('scan 400000000 470000000 201 3'))
    print('resonance %.1f MHz: RL %.1f dB (true value %.1f to %.1f dB with a -50 dB floor), VSWR %.2f'
          % (f0 / 1e6, rl, rmin, rmax, sw))
    if band:
        print('VSWR <= 2 from %.1f to %.1f MHz (%.1f MHz)' % (band[0] / 1e6, band[1] / 1e6, (band[1] - band[0]) / 1e6))

if __name__ == '__main__':
    main()
