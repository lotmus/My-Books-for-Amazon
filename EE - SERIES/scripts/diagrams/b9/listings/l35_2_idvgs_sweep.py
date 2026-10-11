"""MOSFET Id-Vgs and Id-Vds sweeps with two 2450-class SMUs over VISA, the same sweep
as the LabVIEW VI of Figure 35.3. With --sim, a simulated transistor answers instead.
Usage: python l35_2_idvgs_sweep.py --sim
       python l35_2_idvgs_sweep.py --gate GPIB0::18::INSTR --drain GPIB0::19::INSTR --temp 25"""
import argparse, csv, datetime, math, random, time


def model_id(vgs, vds, t_c=25.0, vt0=2.10, beta0=0.25, theta=0.15, n=1.5):
    """Simulated N-MOSFET drain current in A: smooth square law with mobility degradation."""
    tk = t_c + 273.15
    vt = vt0 - 0.003 * (t_c - 25.0)              # threshold falls about 3 mV/K
    beta = beta0 * (tk / 298.15) ** -1.5         # mobility falls with temperature
    phi = 8.617e-5 * tk                          # thermal voltage kT/q
    vov = 2 * n * phi * math.log1p(math.exp((vgs - vt) / (2 * n * phi)))
    vd = min(vds, vov)                           # linear region, or saturation
    return beta * (vov * vd - vd * vd / 2) / (1 + theta * vov)


class SimDut:
    def __init__(self, t_c, seed=8):
        self.v = {"gate": 0.0, "drain": 0.0}
        self.t_c, self.rng = t_c, random.Random(seed)


class SimSmu:
    def __init__(self, dut, terminal):
        self.dut, self.term = dut, terminal

    def set_v(self, v):
        self.dut.v[self.term] = v

    def read_i(self):
        vg, vd = self.dut.v["gate"], self.dut.v["drain"]
        gate = self.term == "gate"
        i = 1e-11 + 1e-12 * vg if gate else model_id(vg, vd, self.dut.t_c)   # gate: leakage only
        noise = 1e-12 if gate else 1e-9                                       # A, range dependent
        return i * (1 + 2e-4 * self.dut.rng.gauss(0, 1)) + noise * self.dut.rng.gauss(0, 1)

    def off(self):
        self.set_v(0.0)


class Smu:
    """One 2450-class SMU, SCPI command set: source voltage, measure current."""
    def __init__(self, rm, resource, ilimit):
        self.inst = rm.open_resource(resource, read_termination="\n", write_termination="\n")
        self.inst.timeout = 10000                                     # ms
        for cmd in ("*RST", 'SENS:FUNC "CURR"', "SENS:CURR:RANG:AUTO ON", "SENS:CURR:NPLC 1",
                    "SOUR:FUNC VOLT", "SOUR:VOLT:RANG 20", f"SOUR:VOLT:ILIM {ilimit}",
                    "SOUR:VOLT 0", "OUTP ON"):
            self.inst.write(cmd)

    def set_v(self, v):
        self.inst.write(f"SOUR:VOLT {v:.4f}")

    def read_i(self):
        return float(self.inst.query("READ?"))

    def off(self):
        self.inst.write("SOUR:VOLT 0")
        self.inst.write("OUTP OFF")
        self.inst.close()


def steps(start, stop, step):
    n = round((stop - start) / step) + 1
    return [round(start + k * step, 6) for k in range(n)]


def sweep(gate, drain, vgs_list, vds_list=None, settle=0.005):
    """Rows of (Vgs, Vds, Id, Ig). vds_list=None ties the drain to the gate (Vds = Vgs)."""
    rows = []
    for vgs in vgs_list:
        gate.set_v(vgs)
        for vds in (vds_list or [vgs]):
            drain.set_v(vds)
            time.sleep(settle)
            rows.append((vgs, vds, drain.read_i(), gate.read_i()))
    drain.set_v(0.0)
    gate.set_v(0.0)
    return rows


def write_csv(path, rows, meta):
    with open(path, "w", newline="") as f:
        for k, v in meta.items():
            f.write(f"# {k}: {v}\n")
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["vgs_V", "vds_V", "id_A", "ig_A"])
        w.writerows(rows)


def run(t_c, gate, drain, settle, prefix="mosfet"):
    """The three measurements of Section 35.5 at one temperature; returns the rows."""
    curves = {
        "idvgs": sweep(gate, drain, steps(0, 5, 0.05), [0.1], settle),           # linear region
        "vth": sweep(gate, drain, steps(0, 3, 0.01), None, settle),              # Vds = Vgs
        "idvds": sweep(gate, drain, [4.0, 6.0, 10.0], steps(0, 0.2, 0.01), settle),
    }
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    for name, rows in curves.items():
        write_csv(f"{prefix}_{name}_{t_c:.0f}C.csv", rows,
                  {"device": "N-MOSFET sample 1", "temperature_C": t_c, "nplc": 1, "utc": stamp})
    return curves


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sim", action="store_true")
    ap.add_argument("--gate", default="GPIB0::18::INSTR")
    ap.add_argument("--drain", default="GPIB0::19::INSTR")
    ap.add_argument("--temp", type=float, nargs="+", default=[25.0, 75.0, 125.0])
    a = ap.parse_args()
    for t in a.temp:
        if a.sim:
            dut = SimDut(t)
            gate, drain, settle = SimSmu(dut, "gate"), SimSmu(dut, "drain"), 0.0
        else:
            import pyvisa
            input(f"Set the chuck to {t:.0f} °C, wait for the soak, then press Enter: ")
            rm = pyvisa.ResourceManager()
            gate, drain, settle = Smu(rm, a.gate, 0.001), Smu(rm, a.drain, 0.25), 0.005
        try:
            c = run(t, gate, drain, settle)
        finally:
            gate.off()
            drain.off()
        at5 = [r[2] for r in c["idvgs"] if r[0] == 5.0][0]
        print(f"{t:5.0f} °C: {sum(len(r) for r in c.values())} points, Id(Vgs = 5 V, Vds = 0.1 V) = {at5 * 1e3:.2f} mA")
