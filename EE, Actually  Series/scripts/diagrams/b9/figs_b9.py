"""Regenerate the Book 9 mini-tracer teaching figure from its checked simulator."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
LISTINGS = ROOT / "scripts" / "diagrams" / "b9" / "listings"
OUTPUT = ROOT / "chapters" / "Book9" / "fig" / "fig38_1.png"
sys.path.insert(0, str(LISTINGS))

from l38_1_mini_tracer import SimBackend, Tracer, early_check  # noqa: E402


def main():
    rows = Tracer(SimBackend(seed=38)).family([1.65, 2.65, 3.65, 4.0])
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=100)
    fig.patch.set_facecolor("#0b1720")
    ax.set_facecolor("#0b1720")
    ax.axvspan(1.0, 2.0, color="#a98b00", alpha=0.15, zorder=0)
    palette = ["#25e675", "#25e675", "#25e675"]
    bases = [1.65, 2.65, 3.65]
    for vb, color in zip(bases, palette):
        pts = sorted((vce, ic * 1e3) for b, vce, ic, _ in rows if b == vb)
        ax.plot([x for x, _ in pts], [y for _, y in pts], "o-", ms=2.8,
                lw=1.2, color=color)
        ax.text(3.55, pts[-1][1], f"{(vb - 0.65) / 100000 * 1e6:.0f} uA",
                color="#e6edf3", fontsize=8, va="center")

    vb = 3.65
    va, residual, check_v, measured, predicted = early_check(rows, vb)
    fit_pts = sorted((vce, ic) for b, vce, ic, _ in rows if b == vb and 1.0 <= vce <= 2.0)
    n = len(fit_pts)
    sx = sum(x for x, _ in fit_pts); sy = sum(y for _, y in fit_pts)
    sxx = sum(x*x for x, _ in fit_pts); sxy = sum(x*y for x, y in fit_pts)
    slope = (n*sxy - sx*sy) / (n*sxx - sx*sx)
    intercept = (sy - slope*sx) / n
    xs = [1.0 + i * 1.0 / 40 for i in range(41)]
    fit_line, = ax.plot(xs, [(slope*x + intercept)*1e3 for x in xs], "--", color="#ffd166",
                        lw=1.1, label="linear fit (30 uA curve)")
    ax.plot([check_v], [measured*1e3], "s", ms=6, mfc="none", mec="#ff6363", mew=1.5)
    ax.annotate(f"unused point {check_v:.2f} V\nmeasured {measured*1e3:.2f} mA; fit {predicted*1e3:.2f} mA",
                xy=(check_v, measured*1e3), xytext=(1.25, 7.0),
                arrowprops={"arrowstyle": "->", "color": "#ff6363"},
                color="#ff7777", fontsize=8)
    ax.text(1.05, 7.75, f"fit range 1.0 to 2.0 V; Early voltage about {va:.0f} V",
            color="#ffd166", fontsize=9)
    ax.text(0.99, 0.02, "Synthetic model output; not a hardware measurement",
            transform=ax.transAxes, color="#b8c7d1", fontsize=8, ha="right")
    ax.set(xlim=(0, 4.0), ylim=(0, 8.5), xlabel="Vce (V)", ylabel="Ic (mA)")
    ax.grid(True, color="#344955", lw=0.6)
    ax.tick_params(colors="#e6edf3")
    ax.xaxis.label.set_color("#e6edf3"); ax.yaxis.label.set_color("#e6edf3")
    for spine in ax.spines.values(): spine.set_color("#607482")
    ax.legend(handles=[fit_line], loc="upper right", frameon=False,
              labelcolor="#e6edf3", fontsize=8)
    fig.tight_layout(pad=1.0)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
