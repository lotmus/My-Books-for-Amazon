"""Threshold voltage, on-resistance, and the zero-temperature-coefficient point from sweep data.
Plain lists in, plain numbers out, so the same functions run from the LabVIEW Python Node,
a TestStand Python step, or a script. Run alone, it extracts from the simulated sweeps."""
import math


def vth_max_gm(vgs, ids, vds):
    """Linear extrapolation at maximum transconductance, minus Vds/2.
    Returns (vth, gm_max, vgs_at_gm_max)."""
    gm = [(ids[k + 1] - ids[k - 1]) / (vgs[k + 1] - vgs[k - 1]) for k in range(1, len(vgs) - 1)]
    k = max(range(len(gm)), key=gm.__getitem__) + 1
    g = gm[k - 1]
    return vgs[k] - ids[k] / g - vds / 2, g, vgs[k]


def vth_const_current(vgs, ids, i_ref=1e-3):
    """Gate voltage at which Id first reaches i_ref, interpolated linearly."""
    for k in range(1, len(ids)):
        if ids[k - 1] < i_ref <= ids[k]:
            return vgs[k - 1] + (i_ref - ids[k - 1]) * (vgs[k] - vgs[k - 1]) / (ids[k] - ids[k - 1])
    return math.nan


def ron_fit(vds, ids, v_max=0.1):
    """On-resistance: 1/slope of a least-squares line through the points with Vds <= v_max."""
    pts = [(v, i) for v, i in zip(vds, ids) if v <= v_max + 1e-9]
    n = len(pts)
    mv, mi = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
    slope = sum((v - mv) * (i - mi) for v, i in pts) / sum((v - mv) ** 2 for v, _ in pts)
    return 1.0 / slope


def ztc_point(vgs, ids_cold, ids_hot):
    """Gate voltage where the cold and hot curves cross (the zero-temperature-coefficient point)."""
    for k in range(1, len(vgs)):
        d0, d1 = ids_cold[k - 1] - ids_hot[k - 1], ids_cold[k] - ids_hot[k]
        if vgs[k - 1] > 0.5 and d0 * d1 <= 0 and d0 != d1:
            return vgs[k - 1] + d0 * (vgs[k] - vgs[k - 1]) / (d0 - d1)
    return math.nan


if __name__ == "__main__":
    import os, sys, tempfile
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sweep = __import__("l35_2_idvgs_sweep")
    os.chdir(tempfile.mkdtemp())                       # the CSV files go to a scratch folder
    res = {}
    for t in (25.0, 75.0, 125.0):
        dut = sweep.SimDut(t)
        c = sweep.run(t, sweep.SimSmu(dut, "gate"), sweep.SimSmu(dut, "drain"), 0.0)
        lin = c["idvgs"]
        vgs, ids = [r[0] for r in lin], [r[2] for r in lin]
        vth, gm, vg_at = vth_max_gm(vgs, ids, 0.1)
        vcc = vth_const_current([r[0] for r in c["vth"]], [r[2] for r in c["vth"]])
        on = [r for r in c["idvds"] if r[0] == 10.0]
        ron = ron_fit([r[1] for r in on], [r[2] for r in on])
        res[t] = (vgs, ids)
        print(f"{t:5.0f} °C: Vth(max gm) = {vth:.3f} V (gm = {gm * 1e3:.1f} mS at {vg_at:.2f} V), "
              f"Vth(1 mA, Vds = Vgs) = {vcc:.3f} V, Ron(10 V) = {ron:.3f} ohm")
    print(f"ZTC point, 25 and 125 °C: Vgs = {ztc_point(res[25.0][0], res[25.0][1], res[125.0][1]):.2f} V")
