"""Regenerate Book 6 Chapter 17 transformer thermal-aging figure.

Run from the repository root with:
    python scripts/diagrams/b6/figs_b6_transformer_aging.py

This plots the historical IEEE C57.91-2011 Arrhenius teaching model used in
the chapter. It is not an overload capability or remaining-life calculator.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "chapters" / "Book6" / "fig" / "fig17_2.png"


def aging_factor(hotspot_c: np.ndarray) -> np.ndarray:
    """Relative aging factor for the 2011 model, referenced to 110 deg C."""
    return np.exp(15_000 / 383 - 15_000 / (hotspot_c + 273))


def main() -> None:
    temperatures = np.linspace(80, 150, 400)
    samples = np.array([98.0, 110.0, 120.0, 130.0])
    factors = aging_factor(samples)

    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=100)
    ax.plot(temperatures, aging_factor(temperatures), color="#3478b9", linewidth=2)
    ax.axhline(1, color="#888888", linestyle=":", linewidth=1)
    ax.scatter(samples, factors, color="#c43c30", zorder=3)
    ax.set_yscale("log")
    ax.set_xlim(80, 150)
    ax.set_ylim(0.03, 50)
    ax.set_title("IEEE C57.91-2011 teaching model: relative thermal-aging factor")
    ax.set_xlabel("Winding hot-spot temperature (°C)")
    ax.set_ylabel("Relative aging factor")
    ax.grid(True, which="both", alpha=0.25)

    offsets = [(-16, 10), (-22, 10), (-22, 10), (-22, 10)]
    for temp, factor, offset in zip(samples, factors, offsets):
        ax.annotate(
            f"{temp:.0f} °C: {factor:.2f}×",
            xy=(temp, factor),
            xytext=offset,
            textcoords="offset points",
            ha="right",
            fontsize=9,
        )

    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=100)
    plt.close(fig)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
