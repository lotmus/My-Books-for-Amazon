"""Regenerate Book 6 Chapter 9 and 11 switching-loss figures.

Run from the repository root with:
    python scripts/diagrams/b6/figs_b6_loss.py

The charts use a first-order constant-Coss model for two equal synchronous-buck
switches. Real-device estimates should use each switch's voltage-dependent Eoss.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
FIG_DIR = ROOT / "chapters" / "Book6" / "fig"

VIN = 12.0
VOUT = 1.0
ILOAD = 20.0
RHS = 5e-3
RLS = 2e-3
D = VOUT / VIN
TR_TF_SI = 20e-9
TR_TF_GAN = 4e-9
COSS_PER_SWITCH = 1e-9
VGS = 5.0
QG_SI = 20e-9
QG_GAN = 5e-9
VF_SI = 0.7
VF_GAN = 2.0
TD_SI = 20e-9
TD_GAN = 5e-9
FS_BASE = 500e3


def efficiency(output_power: np.ndarray, loss: np.ndarray) -> np.ndarray:
    return 100.0 * output_power / (output_power + loss)


def make_loss_breakdown() -> None:
    cases = [
        ("Si, 500 kHz", FS_BASE, TR_TF_SI, QG_SI, TD_SI, VF_SI),
        ("Si, 1 MHz", 2 * FS_BASE, TR_TF_SI, QG_SI, TD_SI, VF_SI),
        ("GaN, 1 MHz", 2 * FS_BASE, TR_TF_GAN, QG_GAN, TD_GAN, VF_GAN),
    ]
    names = [case[0] for case in cases]
    components = {key: [] for key in ("conduction", "switching overlap", "dead time", "gate", "Coss")}
    for _, fs, tr_tf, qg, td, vf in cases:
        pcond = ILOAD**2 * (RHS * D + RLS * (1.0 - D))
        psw = 0.5 * VIN * ILOAD * tr_tf * fs
        pcoss = 0.5 * (2.0 * COSS_PER_SWITCH) * VIN**2 * fs
        pgate = 2.0 * qg * VGS * fs
        pdead = 2.0 * vf * ILOAD * td * fs
        for key, value in zip(components, (pcond, psw, pdead, pgate, pcoss)):
            components[key].append(value)

    colors = {
        "conduction": "#3478b9",
        "switching overlap": "#c43c30",
        "dead time": "#df8124",
        "gate": "#328650",
        "Coss": "#707070",
    }
    fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
    x = np.arange(len(names))
    bottom = np.zeros(len(names))
    for key, values in components.items():
        vals = np.asarray(values)
        ax.bar(x, vals, bottom=bottom, width=0.55, color=colors[key], label=key)
        bottom += vals

    labels = [
        f"{total:.3f} W, η = {efficiency(np.array([20.0]), np.array([total]))[0]:.1f} %"
        for total in bottom
    ]
    for i, (total, label) in enumerate(zip(bottom, labels)):
        ax.text(i, total + 0.08, label, ha="center", va="bottom", fontsize=10)
    ax.set_title("Doubling frequency doubles every switching term; GaN shrinks them")
    ax.set_ylabel("Loss (W) at 1 V, 20 A")
    ax.set_xticks(x, names)
    ax.set_ylim(0, 4.8)
    ax.grid(axis="y", color="#bdbdbd", alpha=0.45)
    ax.set_axisbelow(True)
    ax.legend(loc="upper left", frameon=False)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig9_1.png", dpi=100)
    plt.close(fig)


def make_light_load_curve() -> None:
    current = np.unique(np.concatenate((np.logspace(-1.5, np.log10(20.0), 240), [0.2])))
    conduction_per_amp_squared = RHS * D + RLS * (1.0 - D)
    psw_per_amp = 0.5 * VIN * TR_TF_SI * FS_BASE
    pdead_per_amp = 2.0 * VF_SI * TD_SI * FS_BASE
    gate_at_full_rate = 2.0 * QG_SI * VGS * FS_BASE
    coss_at_full_rate = 0.5 * (2.0 * COSS_PER_SWITCH) * VIN**2 * FS_BASE
    controller = 0.010

    forced_loss = (
        conduction_per_amp_squared * current**2
        + (psw_per_amp + pdead_per_amp) * current
        + gate_at_full_rate
        + coss_at_full_rate
        + controller
    )

    # A simple pulse-frequency schedule: 50 kHz at 0.2 A, rising linearly to
    # 500 kHz at 2 A. It represents one possible controller, not a universal
    # burst-mode law. The curve then matches forced PWM above 2 A.
    burst_rate = np.minimum(FS_BASE, FS_BASE * current / 2.0)
    rate_ratio = burst_rate / FS_BASE
    burst_loss = (
        conduction_per_amp_squared * current**2
        + (psw_per_amp + pdead_per_amp) * current * rate_ratio
        + gate_at_full_rate * rate_ratio
        + coss_at_full_rate * rate_ratio
        + controller
    )
    output_power = VOUT * current
    forced_eff = efficiency(output_power, forced_loss)
    burst_eff = efficiency(output_power, burst_loss)
    current_mark = 0.2
    index = int(np.argmin(np.abs(current - current_mark)))

    fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
    ax.semilogx(current, forced_eff, color="#c43c30", lw=2.5, label="forced PWM, 500 kHz")
    ax.semilogx(
        current,
        burst_eff,
        color="#3478b9",
        lw=2.5,
        label="burst/PFM: 50 kHz at 0.2 A, rising to 500 kHz at 2 A",
    )
    ax.scatter([current[index]], [forced_eff[index]], color="#c43c30", zorder=3)
    ax.scatter([current[index]], [burst_eff[index]], color="#3478b9", zorder=3)
    ax.annotate(
        f"0.2 A: {forced_eff[index]:.1f} %",
        (current[index], forced_eff[index]),
        xytext=(12, -15),
        textcoords="offset points",
        color="#c43c30",
    )
    ax.annotate(
        f"0.2 A: {burst_eff[index]:.1f} %",
        (current[index], burst_eff[index]),
        xytext=(12, 10),
        textcoords="offset points",
        color="#3478b9",
    )
    ax.set_title("Per-cycle losses sink light-load efficiency; switching less often helps")
    ax.set_xlabel("Load current (A), 1 V output")
    ax.set_ylabel("Efficiency (%)")
    ax.set_xlim(0.025, 25.0)
    ax.set_ylim(0, 100)
    ax.grid(True, which="major", color="#bdbdbd", alpha=0.45)
    ax.set_axisbelow(True)
    ax.legend(loc="lower right", frameon=False)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig11_1.png", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    make_loss_breakdown()
    make_light_load_curve()
