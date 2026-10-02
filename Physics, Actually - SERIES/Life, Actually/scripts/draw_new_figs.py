"""Draw the new line-art figures for Part XI of 'Life, Actually' (Figures 48-50).
Same palette and font as the Genetics figures. Run: python draw_new_figs.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Wedge, FancyArrowPatch
import numpy as np

FIGS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures", "figs")
os.makedirs(FIGS, exist_ok=True)
INK = "#1a1a1a"; GREY = "#555555"; LIGHT = "#e8e8e8"
GREEN = "#27ae60"; LGREEN = "#bfe6cc"; BLUE = "#2980b9"; RED = "#c0392b"; ORANGE = "#e67e22"
plt.rcParams["font.family"] = "DejaVu Sans"

def save(fig, n):
    p = os.path.join(FIGS, f"fig{n:02d}.png")
    fig.savefig(p, bbox_inches="tight", facecolor="white", dpi=200); plt.close(fig); print("wrote", p)

def fig48():
    fig, axs = plt.subplots(2, 1, figsize=(7, 4.6))
    panels = [
        ("The Sun", 2.0, (0.75, 1.77), (0.95, 1.67),
         [("Mercury", 0.39), ("Venus", 0.72), ("Earth", 1.00), ("Mars", 1.52)], "#f5b041"),
        ("TRAPPIST-1 (a red dwarf about 40 light-years away)", 0.066, (0.019, 0.050), (0.0255, 0.048),
         [("b", .0115), ("c", .0158), ("d", .0223), ("e", .0293), ("f", .0385), ("g", .0469), ("h", .0619)], RED),
    ]
    for ax, (name, xmax, opt, cons, planets, starcol) in zip(axs, panels):
        ax.set_xlim(-0.04 * xmax, xmax); ax.set_ylim(-1, 1.3); ax.set_yticks([])
        for s in ("left", "right", "top"): ax.spines[s].set_visible(False)
        ax.add_patch(Rectangle((opt[0], -0.6), opt[1] - opt[0], 1.2, color=LGREEN, lw=0))
        ax.add_patch(Rectangle((cons[0], -0.6), cons[1] - cons[0], 1.2, color=GREEN, alpha=0.55, lw=0))
        ax.plot([-0.04 * xmax], [0], "o", ms=16, color=starcol, clip_on=False)
        for lab, a in planets:
            ax.plot([a], [0], "o", ms=6, color=BLUE if lab in ("Earth",) else INK)
            ax.text(a, 0.32, lab, ha="center", fontsize=8, color=INK)
        ax.text(0, 1.05, name, fontsize=10, weight="bold", color=INK, ha="left")
        ax.set_xlabel("distance from the star (astronomical units; 1 AU = Earth-Sun distance)", fontsize=8, color=GREY)
        ax.tick_params(labelsize=8, colors=GREY)
    axs[0].text(1.31, -0.85, "dark green: conservative zone    light green: optimistic zone", fontsize=7.5, color=GREY, ha="center")
    axs[1].text(0.033, -0.85, "Mercury's orbit (0.39 AU) would lie about six times farther out than the right edge of this panel", fontsize=7.5, color=GREY, ha="center")
    fig.tight_layout(h_pad=1.6)
    save(fig, 48)

def fig49():
    fig, ax = plt.subplots(figsize=(6.5, 4.6)); ax.set_xlim(-1.05, 2.7); ax.set_ylim(-1.15, 1.05); ax.set_aspect("equal"); ax.axis("off")
    layers = [(1.0, "#eaf2f8"), (0.90, "#5dade2"), (0.70, "#a0522d"), (0.32, "#7b3f1e")]
    for r, c in layers:
        ax.add_patch(Wedge((0, 0), r, -60, 60, color=c, ec=INK, lw=0.8))
    ax.add_patch(Wedge((0, 0), 1.0, 60, 300, color=LIGHT, ec=INK, lw=0.8))
    labels = [("ice shell", 0.95, 50, 0.92), ("global salty ocean", 0.80, 32, 0.62), ("rocky interior", 0.52, 18, 0.32), ("metal core (if any)", 0.16, 5, 0.06)]
    for lab, rr, ang, ty in labels:
        a = np.radians(ang)
        ax.annotate(lab, xy=(rr * np.cos(a), rr * np.sin(a)), xytext=(1.25, ty), fontsize=9, color=INK, va="center",
                    arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
    for ang in (-25, 0, 22):
        a = np.radians(ang); x, y = 0.70 * np.cos(a), 0.70 * np.sin(a)
        ax.add_patch(FancyArrowPatch((x, y), (x + 0.13 * np.cos(a), y + 0.13 * np.sin(a)), arrowstyle="-|>", mutation_scale=8, color=ORANGE, lw=1.2))
    a = np.radians(-25)
    ax.annotate("hydrothermal activity: hot water reacts with rock,\nreleasing hydrogen and other energy-rich chemicals", xy=(0.76 * np.cos(a), 0.76 * np.sin(a)), xytext=(1.25, -0.30), fontsize=8, color=GREY, va="center", arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
    a = np.radians(-45)
    ax.annotate("oxidants made by radiation at the surface\nmay be carried down through the ice", xy=(0.95 * np.cos(a), 0.95 * np.sin(a)), xytext=(1.25, -0.75), fontsize=8, color=GREY, va="center", arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
    ax.text(0, -1.12, "schematic, not to scale", fontsize=7.5, color=GREY, ha="center")
    save(fig, 49)

def fig50():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.2), gridspec_kw=dict(width_ratios=[1.1, 1]))
    a1.set_xlim(-1.9, 3.3); a1.set_ylim(-1.4, 1.4); a1.set_aspect("equal"); a1.axis("off")
    a1.add_patch(Circle((-0.6, 0), 1.2, color="#f8c471"))
    a1.text(-0.6, -1.32, "star", ha="center", fontsize=8, color=GREY)
    a1.add_patch(Circle((-0.2, 0.25), 0.36, color="#aed6f1", alpha=0.8))
    a1.add_patch(Circle((-0.2, 0.25), 0.28, color="#1b2631"))
    a1.text(-0.2, 0.25, "planet", ha="center", va="center", fontsize=7, color="white")
    for dy in (0.25 + 0.32, 0.25 - 0.32):
        a1.add_patch(FancyArrowPatch((-0.2, dy), (2.6, dy), arrowstyle="-|>", mutation_scale=9, color=BLUE, lw=1))
    a1.text(1.35, 1.0, "starlight filtered through\nthe ring of atmosphere", ha="center", fontsize=8, color=INK)
    a1.text(2.95, 0.25, "to\ntelescope", ha="center", va="center", fontsize=8, color=GREY)
    wl = np.linspace(0.6, 5.2, 600)
    depth = 1.0 + 0.10 * np.exp(-((wl - 1.4) / 0.08) ** 2) + 0.18 * np.exp(-((wl - 3.3) / 0.15) ** 2) + 0.28 * np.exp(-((wl - 4.3) / 0.12) ** 2)
    a2.plot(wl, depth, color=INK, lw=1.4)
    for x, lab in ((3.3, "methane"), (4.3, "carbon\ndioxide"), (1.4, "water")):
        a2.annotate(lab, xy=(x, 1.0 + (0.28 if x == 4.3 else 0.18 if x == 3.3 else 0.10)), xytext=(x, 1.42 if x != 1.4 else 1.25), ha="center", fontsize=7.5, color=GREY, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    a2.set_ylim(0.95, 1.55); a2.set_yticks([]); a2.set_xlabel("wavelength (micrometers)", fontsize=8, color=GREY)
    a2.set_ylabel("apparent size of planet", fontsize=8, color=GREY); a2.tick_params(labelsize=8, colors=GREY)
    for s in ("right", "top"): a2.spines[s].set_visible(False)
    a2.text(0.62, 1.50, "illustrative spectrum", fontsize=7.5, color=GREY)
    fig.tight_layout(); save(fig, 50)

if __name__ == "__main__":
    fig48(); fig49(); fig50()
