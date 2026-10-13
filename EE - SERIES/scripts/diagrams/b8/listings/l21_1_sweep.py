"""Frequency sweep of a filter with a function generator and an oscilloscope over SCPI (PyVISA).

SCPI command spellings differ between vendors; the ones below follow common forms.
Run with --sim to test the script logic without instruments (an ideal RC low-pass).
"""
import argparse
import csv
import math
import time

import numpy as np

R, C = 10e3, 10e-9                      # device under test: fc = 1/(2 pi R C) = 1591.5 Hz

class SimBench:
    """Stands in for the generator and scope; answers like an RC low-pass with 1 V in."""
    def __init__(self):
        self.f = 1000.0
    def write(self, cmd):
        if cmd.startswith("FREQ"):
            self.f = float(cmd.split()[1])
    def query(self, cmd):
        if cmd == "*IDN?":
            return "SIM,Bench,0,1.0"
        h = 1 / math.sqrt(1 + (2 * math.pi * self.f * R * C) ** 2)
        vin = 2.0                                     # 2 Vpp
        return str(vin if "CHAN1" in cmd else vin * h)

def open_bench(sim):
    if sim:
        b = SimBench()
        return b, b
    import pyvisa
    rm = pyvisa.ResourceManager()
    gen = rm.open_resource("USB0::0x1AB1::0x0642::DG1ZA000000001::INSTR")   # from rm.list_resources()
    scope = rm.open_resource("TCPIP0::192.168.1.50::INSTR")
    for inst in (gen, scope):
        inst.timeout = 5000                              # ms
    gen.write("FUNC SIN"); gen.write("VOLT 2.0"); gen.write("OUTP ON")
    return gen, scope

def sweep(gen, scope, f_start=100, f_stop=100e3, per_decade=20, settle=0.3):
    n = int(round(math.log10(f_stop / f_start) * per_decade)) + 1
    rows = []
    for f in np.logspace(math.log10(f_start), math.log10(f_stop), n):
        gen.write(f"FREQ {f:.3f}")
        time.sleep(settle)                                # let the scope's measurement update
        vin = float(scope.query(":MEAS:VPP? CHAN1"))
        vout = float(scope.query(":MEAS:VPP? CHAN2"))
        rows.append((f, vin, vout, 20 * math.log10(vout / vin)))
    return rows

def corner(rows):
    """-3 dB frequency by linear interpolation in log(f)."""
    for (f1, *_, g1), (f2, *_, g2) in zip(rows, rows[1:]):
        if g1 >= -3.0103 > g2:
            x = (-3.0103 - g1) / (g2 - g1)
            return 10 ** (math.log10(f1) + x * (math.log10(f2) - math.log10(f1)))
    return None

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sim", action="store_true")
    args = ap.parse_args()
    gen, scope = open_bench(args.sim)
    print("instrument:", scope.query("*IDN?").strip())
    rows = sweep(gen, scope, settle=0 if args.sim else 0.3)
    with open("sweep.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["f_Hz", "vin_Vpp", "vout_Vpp", "gain_dB"])
        w.writerows(rows)
    print(f"{len(rows)} points, corner at {corner(rows):.1f} Hz (theory {1 / (2 * math.pi * R * C):.1f} Hz)")
