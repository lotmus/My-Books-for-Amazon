"""Reader-lab mini curve tracer (Chapter 7, Section 7.6): a Raspberry Pi Pico or ESP32-S3 in MicroPython drives
an MCP4728 DAC (0 to 4.095 V, two channels used) and reads an ADS1115 16-bit ADC (+/-4.096 V, 125 uV LSB).
Power the MCP4728, ADS1115, and U1 from a regulated 5.0 V rail (4.75 to 5.25 V). Use a bidirectional I2C level shifter to the
3.3 V MCU. Keep ADS1115 analog inputs between GND and VDD; +/-4.096 V is differential PGA range, not the pin limit.

  MCP4728 VOUTA -> U1 OPA310-Q1 DBV: IN+ pin 3; OUT pin 1 -> IN- pin 4 (unity buffer). V+ pin 5 -> 5 V; V- pin 2 -> GND; 100 nF bypass at U1.
  U1 OUT -> Rlim1 = 120 ohm, 1 W -> Rlim2 = 120 ohm, 1 W -> Rs = 47 ohm, 1 W -> DUT collector; DUT emitter -> GND. MCP4728 VOUTB -> Rb = 100 kohm -> base. ADS1115 AIN0/AIN1 tap the high/low sides of Rs; AIN1-GND measures Vce and AIN2-GND measures Vbe. All analog grounds are common.
  With both 120 ohm resistors and the sense resistor at minimum tolerance, a 5.25 V stuck output is limited to 18.5 mA. If either limiter shorts, the other and sense resistor limit current to 31.8 mA. Normal maximum DAC command into a shorted DUT is limited to 14.4 mA. These passive bounds do not establish DUT pulse SOA or safe temperature. Check the selected DUT data sheet and validate the pulse waveform; MOSFET drain tests require a separate fixture.

The simulator uses an ideal collector-drive voltage and omits U1 headroom/settling, analog errors, wiring, and device variation. Board execution is disabled by default. Validate the assembled circuit with a dummy load before enabling HARDWARE_MODE or connecting a DUT. Run on a PC:
python l38_1_mini_tracer.py
"""
import math
import os
import sys
import time

RS, R_LIMIT1, R_LIMIT2, RB, LSB = 47.0, 120.0, 120.0, 100_000.0, 4.096 / 32768
R_SERIES = R_LIMIT1 + R_LIMIT2 + RS
HARDWARE_MODE = False  # Enable only after complete circuit and bench checks.

class HwBackend:
    """MicroPython on the board: MCP4728 at 0x60 (internal 2.048 V reference, gain 2: 1 mV per code, needs a
    5 V supply) and ADS1115 at 0x48 (PGA +-4.096 V, 860 SPS, single shot). Rs between AIN0 and AIN1, the
    collector on AIN1, the base on AIN2."""
    def __init__(self, i2c):
        self.i2c = i2c
    def set_dac(self, ch, volts):
        code = max(0, min(4095, int(round(volts * 1000))))
        self.i2c.writeto(0x60, bytes([0x40 | (ch << 1), 0x90 | (code >> 8), code & 0xFF]))
    def sleep_ms(self, ms):
        time.sleep_ms(ms)                                             # MicroPython
    def _conv(self, mux):
        cfg = 0x8000 | (mux << 12) | (0b001 << 9) | 0x0100 | (0b111 << 5) | 0b11
        self.i2c.writeto_mem(0x48, 0x01, bytes([cfg >> 8, cfg & 0xFF]))
        time.sleep_ms(2)                                              # 860 SPS: 1.2 ms per conversion
        b = self.i2c.readfrom_mem(0x48, 0x00, 2)
        v = (b[0] << 8) | b[1]
        return (v - 65536 if v > 32767 else v) * LSB
    def read(self):
        # AIN0-AIN1 = shunt drop; AIN1-GND = Vce; AIN2-GND = Vbe.
        muxes = (0b000, 0b110, 0b111)
        return tuple(sum(self._conv(mux) for _ in range(5)) / 5 for mux in muxes)

class SimBackend:
    """Transistor model from Listing 7.1 (beta 200, VA 75 V), ADS1115 quantization and 2-LSB noise."""
    def __init__(self, seed=38):
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import random
        import l07_1_extract as m
        self.m, self.rnd = m, random.Random(seed)
        self.va = self.vb = 0.0
    def set_dac(self, ch, volts):
        if ch == 0: self.va = volts
        else: self.vb = volts
    def sleep_ms(self, ms):
        pass
    def _solve(self):
        vbe = 0.65 if self.vb > 0.65 else self.vb
        ib = max(self.vb - vbe, 0.0) / RB
        lo, hi = 0.0, self.va                                          # Vce from Va = Vce + Ic(Vce) * R_SERIES
        for _ in range(60):
            mid = (lo + hi) / 2
            ic = float(self.m.bjt_ic(mid, ib)) if ib > 0 else 0.0
            lo, hi = (mid, hi) if mid + ic * R_SERIES < self.va else (lo, mid)
        return lo, ib, vbe
    def read(self):
        measurements = []
        for _ in range(5):
            vce, ib, vbe = self._solve()
            ic = float(self.m.bjt_ic(vce, ib)) if ib > 0 else 0.0
            q = lambda v: round((v + self.rnd.gauss(0, 2 * LSB)) / LSB) * LSB
            measurements.append((q(ic * RS), q(vce), q(vbe)))
        return tuple(sum(row[i] for row in measurements) / 5 for i in range(3))

class Tracer:
    def __init__(self, hw):
        self.hw = hw
        try:
            self.hw.set_dac(1, 0.0)                                    # clear base drive at startup
        finally:
            self.hw.set_dac(0, 0.0)                                    # then clear collector drive
    def point(self, va, vb):
        try:
            self.hw.set_dac(0, va); self.hw.set_dac(1, vb); self.hw.sleep_ms(1)
            vrs, vce, vbe = self.hw.read()
        finally:
            try:
                self.hw.set_dac(1, 0.0)                                # remove base drive first
            finally:
                self.hw.set_dac(0, 0.0)                                # then zero collector drive
        self.hw.sleep_ms(150)  # both outputs off
        return vce, vrs / RS, (vb - vbe) / RB
    def family(self, vb_steps, va_max=4.0, n=41):
        rows = []
        for vb in vb_steps:
            for k in range(n):
                vce, ic, ib = self.point(va_max * k / (n - 1), vb)
                rows.append((vb, vce, ic, ib))
        self.hw.set_dac(1, 0.0)
        return rows

def early_check(rows, vb, fit=(1.0, 2.0), check_v=2.2):
    """Early voltage from a straight line over the stated fit range; validate on a point outside it."""
    pts = [(v, i) for b, v, i, _ in rows if b == vb]
    fit_pts = [(v, i) for v, i in pts if fit[0] <= v <= fit[1]]
    n = len(fit_pts); sx = sum(v for v, _ in fit_pts); sy = sum(i for _, i in fit_pts)
    sxx = sum(v * v for v, _ in fit_pts); sxy = sum(v * i for v, i in fit_pts)
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx); icpt = (sy - slope * sx) / n
    resid = max(abs(i - (slope * v + icpt)) for v, i in fit_pts)
    unused = [(v, i) for v, i in pts if v > fit[1]]
    vv, ii = min(unused, key=lambda p: abs(p[0] - check_v))
    return icpt / slope, resid, vv, ii, slope * vv + icpt

if __name__ == '__main__':
    if sys.platform in ('rp2', 'esp32'):
        if not HARDWARE_MODE:
            raise RuntimeError('Enable hardware only after circuit and bench validation.')
        from machine import I2C, Pin
        tr = Tracer(HwBackend(I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)))
    else:
        tr = Tracer(SimBackend())
    rows = tr.family([1.65, 2.65, 3.65, 4.0])                          # Ib about 10, 20, 30, 33.5 uA
    with open('mini_tracer.csv', 'w') as f:
        f.write('vb_set,vce,ic,ib\n')
        for r in rows:
            f.write('%.3f,%.5f,%.7f,%.8f\n' % r)
    for vb in (1.65, 2.65, 3.65):
        ib = sum(r[3] for r in rows if r[0] == vb) / sum(1 for r in rows if r[0] == vb)
        va, res, vv, ii, pred = early_check(rows, vb)
        print('Ib %.1f uA: VA %.0f V (fit Vce 1.0 to 2.0 V, max residual %.1f uA); check at %.2f V: %.3f mA measured, %.3f mA predicted'
              % (ib * 1e6, va, res * 1e6, vv, ii * 1e3, pred * 1e3))
    print('current LSB %.1f uA; wrote mini_tracer.csv (%d points)' % (LSB / RS * 1e6, len(rows)))
