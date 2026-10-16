"""Generate the additional quantitative figures for Foundations of Electronics REV2."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[3] / "chapters" / "Book1" / "fig"
OUT.mkdir(parents=True, exist_ok=True)
BLUE = "#326a9c"
RED = "#bd4a45"
INK = "#222222"
GRAY = "#707070"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def save(fig, name):
    fig.savefig(OUT / name, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# Two protons: both inverse-square curves are shown on one logarithmic scale.
e = 1.602176634e-19
mp = 1.67262192369e-27
k_e = 8.9875517923e9
G = 6.67430e-11
r = np.logspace(-1, 1, 200)
fe = k_e * e**2 / r**2
fg = G * mp**2 / r**2
fig, ax = plt.subplots(figsize=(7.4, 4.8), constrained_layout=True)
ax.loglog(r, fe, color=RED, lw=2.6, label="Electric repulsion")
ax.loglog(r, fg, color=BLUE, lw=2.6, label="Gravitational attraction")
ax.scatter([1, 1], [k_e * e**2, G * mp**2], color=[RED, BLUE], zorder=3)
ax.axvline(1, color=GRAY, lw=1, ls="--")
ax.set(xlabel="Separation between protons (m)", ylabel="Force magnitude (N)",
       title="Two protons: electric and gravitational force")
ax.grid(True, which="both", alpha=.2)
ax.legend(loc="upper right", frameon=False)
ax.text(.035, .38,
        "At 1 m: electric ≈ 2.3 × 10⁻²⁸ N\n"
        "gravity ≈ 1.9 × 10⁻⁶⁴ N\n"
        "ratio ≈ 1.2 × 10³⁶",
        transform=ax.transAxes, ha="left", va="bottom",
        bbox={"boxstyle": "round,pad=.45", "fc": "white", "ec": "#bbbbbb"})
save(fig, "fig1_2.png")


# The existing normalized time-constant plot, now anchored to the book's 47 kΩ / 10 µF example.
R, C = 47e3, 10e-6
tau = R * C
t = np.linspace(0, 5 * tau, 500)
charge = 1 - np.exp(-t / tau)
discharge = np.exp(-t / tau)
fig, ax = plt.subplots(figsize=(7.4, 4.6), constrained_layout=True)
ax.plot(t, charge, color=BLUE, lw=2.5, label="Charging: 1 − e⁻ᵗ⁄τ")
ax.plot(t, discharge, color=INK, lw=2.2, ls="--", label="Discharging: e⁻ᵗ⁄τ")
for n, label in ((1, "63% / 37%"), (3, "95% / 5%"), (5, "99.3% / 0.7%")):
    x = n * tau
    ax.axvline(x, color=GRAY, lw=.9, ls=":")
    ax.scatter([x, x], [1 - np.exp(-n), np.exp(-n)], color=INK, s=22, zorder=3)
    ax.text(x, 1.035, f"{label}\n{ x:.2f} s", ha="center", va="bottom", fontsize=8)
ax.set(xlim=(0, 5.55 * tau), ylim=(0, 1.12), xlabel="Time (s)", ylabel="Fraction of final or initial value",
       title="RC response: R = 47 kΩ, C = 10 µF, τ = 0.47 s")
ax.grid(True, alpha=.2)
ax.legend(loc="center right", frameon=False)
save(fig, "fig19_1.png")


# Voltage magnification in the already-solved high-Q series RLC example.
fig, (ax, bx) = plt.subplots(1, 2, figsize=(8.2, 4.7), gridspec_kw={"width_ratios": [1, 1.5]}, constrained_layout=True)
ax.axhline(0, color="#bbbbbb", lw=.9)
ax.axvline(0, color="#bbbbbb", lw=.9)
ax.annotate("", xy=(1.0, 0), xytext=(0, 0), arrowprops={"arrowstyle": "->", "lw": 2.2, "color": INK})
ax.annotate("", xy=(0, 1.0), xytext=(0, 0), arrowprops={"arrowstyle": "->", "lw": 2.2, "color": RED})
ax.annotate("", xy=(0, -1.0), xytext=(0, 0), arrowprops={"arrowstyle": "->", "lw": 2.2, "color": BLUE})
ax.text(.08, -.16, "VR = 1.0 V", color=INK)
ax.text(.08, .72, "VL = +j63.2 V", color=RED)
ax.text(.08, -.85, "VC = -j63.2 V", color=BLUE)
ax.text(0, 1.32, "Directions shown; arrow lengths not to scale", ha="center", fontsize=8, color=GRAY)
ax.set(xlim=(-.2, 1.6), ylim=(-1.5, 1.5), xlabel="In phase", ylabel="Quadrature", title="Phasors")
ax.set_aspect("equal", adjustable="box")
ax.grid(True, alpha=.2)
bx.axis("off")
bx.text(.03, .91, "At resonance, using the Worked Example 36.2 circuit:", fontsize=11, weight="bold", transform=bx.transAxes)
bx.text(.04, .73, "R = 5.0 Ω     L = 10 mH     C = 100 nF", fontsize=10, transform=bx.transAxes)
bx.text(.04, .59, "Q = ω₀L/R = 63.2", fontsize=11, transform=bx.transAxes)
bx.text(.04, .42, "VR = 1.0 V", color=INK, fontsize=12, transform=bx.transAxes)
bx.text(.04, .30, "VL = +j63.2 V", color=RED, fontsize=12, transform=bx.transAxes)
bx.text(.04, .18, "VC = -j63.2 V", color=BLUE, fontsize=12, transform=bx.transAxes)
bx.text(.04, .02, "VS = VR + VL + VC = 1.0 V RMS", fontsize=11, weight="bold", transform=bx.transAxes)
fig.suptitle("At resonance, each reactive voltage can exceed the source", fontsize=13)
save(fig, "fig36_4.png")

print("Wrote fig1_2.png, fig19_1.png, and fig36_4.png to", OUT)
