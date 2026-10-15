"""Two-tone intermodulation: set two generators around f0, read the tones and the third-order products
from a spectrum analyzer at several levels, compute OIP3 at each level, and check the 3:1 slope.

Run:  python l27_1_two_tone.py --sim      (an amplifier with 20 dB gain and OIP3 = +25 dBm)
With hardware, replace SimBench by PyVISA sessions to two generators and an analyzer (Chapters 20, 21).
"""
import argparse
import numpy as np

class SimBench:
    gain, oip3 = 20.0, 25.0
    def measure(self, pin_dbm):
        pout = pin_dbm + self.gain
        im3 = 3 * pout - 2 * self.oip3                    # third-order regime
        return pout, im3

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sim', action='store_true')
    ap.parse_args()
    bench = SimBench()
    rows = []
    print(' Pin/tone  Pout/tone  IM3     dIM3   OIP3')
    for pin in (-30, -25, -20):
        pout, im3 = bench.measure(pin)
        d = pout - im3
        rows.append((pout, im3))
        print('%8.1f  %8.1f  %6.1f  %5.1f  %5.1f' % (pin, pout, im3, d, pout + d / 2))
    p = np.array(rows)
    slope = np.polyfit(p[:, 0], p[:, 1], 1)[0]
    print('IM3 slope %.2f dB/dB (3.00 expected: third-order regime, not analyzer-limited)' % slope)

if __name__ == '__main__':
    main()
