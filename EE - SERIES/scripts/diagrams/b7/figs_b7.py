"""Recreate Book 7 Figure 20.1: PCB TDR response to a 30 mm narrow section."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "chapters" / "Book7" / "fig" / "fig20_1.png"

# A 50-ohm step has a +0.10 reflection at the 61.1-ohm section. The
# round-trip time across 30 mm at epsilon_r=3.55 is about 0.377 ns.
t = np.linspace(0.0, 2.5, 1200)  # ns

def edge(x, t0, rise=0.018):
    return 0.5 * (1.0 + np.tanh((x - t0) / rise))

voltage = 0.5 * edge(t, 0.20) + 0.05 * (edge(t, 0.85) - edge(t, 1.23))
fig, ax = plt.subplots(figsize=(8, 3.9), dpi=100)
ax.plot(t, voltage, color="#2878b5", linewidth=2.2)
ax.set_title("TDR: time is distance (12.6 ps per mm round trip)", fontsize=12)
ax.set_xlabel("Time (ns)")
ax.set_ylabel("Voltage at the TDR port (V, 1 V step)")
ax.set_xlim(0, 2.5)
ax.set_ylim(0, 0.62)
ax.grid(True, color="#d0d0d0", linewidth=0.6)
ax.text(0.85, 0.565, "3 cm etched narrow: rho = +0.10, Z = 61.1 ohm",
        color="#d33b2f", fontsize=9, va="bottom")
fig.tight_layout()
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=100)
plt.close(fig)
print(f"Wrote {OUT}")
