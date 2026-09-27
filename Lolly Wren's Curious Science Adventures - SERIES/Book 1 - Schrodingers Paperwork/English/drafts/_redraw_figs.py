"""Redraw appendix figures with labels kept off the drawing, then re-embed."""

from __future__ import annotations

import re
import shutil
import tempfile
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from PIL import Image

DOCX = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")
ASSETS = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\English\_fig_out")

INK = "#111111"
MUTED = "#555555"
LIGHT = "#888888"
FILL = "#D8D8D8"
PAPER = "#FFFFFF"
DARK = "#2A2A2A"
FONT = "DejaVu Sans"

RID_TO_MEDIA = {
    "rId5": "image1.png",
    "rId6": "image2.jpeg",
    "rId7": "image3.png",
    "rId8": "image4.jpeg",
    "rId9": "image5.jpeg",
    "rId10": "image6.png",
    "rId11": "image7.jpeg",
    "rId12": "image8.jpeg",
    "rId13": "image9.jpeg",
    "rId14": "image10.jpeg",
    "rId15": "image11.jpeg",
    "rId16": "image12.png",
    "rId17": "image13.png",
    "rId18": "image14.png",
    "rId19": "image15.png",
    "rId20": "image16.png",
    "rId21": "image17.png",
}

ALTS = {
    "image1.png": "Diagram: a double-slit experiment forming an interference pattern on a screen.",
    "image2.jpeg": "Diagram: two differently oriented measuring devices, each asking a different question.",
    "image3.png": "Two-panel diagram: two-slit interference, then the same setup with a which-path detector and no fringes.",
    "image4.jpeg": "Diagram of the quantum Zeno effect: a pointer reset by repeated checks.",
    "image5.jpeg": "Diagram: a wave packet spreading smoothly at three later times.",
    "image6.png": "Graph: black-hole mass falling and Hawking temperature rising as the hole shrinks.",
    "image7.jpeg": "Diagram: two distant entangled stations. No signal travels between them.",
    "image8.jpeg": "Two-panel diagram: an unknown state cannot be copied; a spread-out pattern can still be repaired.",
    "image9.jpeg": "Diagram of the uncertainty principle: narrow position with broad momentum, and the reverse.",
    "image10.jpeg": "Two-panel diagram: an isolated system versus the moon in constant contact with the sky.",
    "image11.jpeg": "Diagram of Wigner's friend: a definite record inside, still open from outside.",
    "image12.png": "Diagram: one actual path through two slits, empty paths that do not cross it, and a guiding wave.",
    "image13.png": "Diagram: two Bell-test stations beside bars for the local limit of 2 and the quantum ceiling of 2.83.",
    "image14.png": "Diagram: five named string theories around a central M-theory hub.",
    "image15.png": "Diagram: a volume of space whose dotted boundary carries the full account.",
    "image16.png": "Diagram: tiles marked recovered, inferred, or named gone.",
    "image17.png": "Timeline of the stelliferous, degenerate, black-hole and dark eras.",
}


def _fig(w=7.6, h=4.8):
    fig, ax = plt.subplots(figsize=(w, h), dpi=180)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    return fig, ax


def title(ax, text, size=12.0):
    ax.text(0.5, 0.97, text, ha="center", va="top", fontsize=size, color=INK, fontname=FONT, zorder=20)


def caption(ax, text, y=0.06, size=9.0):
    ax.text(0.5, y, text, ha="center", va="center", fontsize=size, color=MUTED, fontname=FONT, zorder=20)


def lab(ax, x, y, text, size=9.0, color=MUTED, ha="center", va="center", **kw):
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color, fontname=FONT, zorder=20, **kw)


def save(fig, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".tmp.png")
    fig.savefig(tmp, dpi=180, facecolor=PAPER, bbox_inches="tight", pad_inches=0.22)
    plt.close(fig)
    im = Image.open(tmp).convert("L").convert("RGB")
    if dest.suffix.lower() in {".jpg", ".jpeg"}:
        im.save(dest, "JPEG", quality=90, optimize=True)
    else:
        im.save(dest, "PNG", optimize=True)
    tmp.unlink(missing_ok=True)
    return im.size


def fig1(path: Path):
    fig, ax = _fig(7.6, 4.9)
    title(ax, "Superposition: both paths, until one is asked")
    y0 = 0.52
    ax.plot(0.10, y0, "o", color=INK, ms=8, zorder=5)
    ax.plot([0.44, 0.44], [0.30, 0.42], color=INK, lw=8, solid_capstyle="butt")
    ax.plot([0.44, 0.44], [0.62, 0.74], color=INK, lw=8, solid_capstyle="butt")
    ax.plot([0.44, 0.44], [0.48, 0.56], color=INK, lw=8, solid_capstyle="butt")
    ax.plot([0.10, 0.44], [y0, 0.45], color=DARK, lw=1.3)
    ax.plot([0.10, 0.44], [y0, 0.59], color=DARK, lw=1.3)
    ax.plot([0.44, 0.80], [0.45, y0], color=LIGHT, lw=0.9)
    ax.plot([0.44, 0.80], [0.59, y0], color=LIGHT, lw=0.9)
    ax.plot([0.80, 0.80], [0.28, 0.76], color=INK, lw=6, solid_capstyle="butt")
    ys = np.linspace(0.30, 0.74, 360)
    env = np.exp(-((ys - y0) / 0.18) ** 2)
    fr = env * (np.cos(2 * np.pi * (ys - y0) / 0.05) ** 2)
    for y, amp in zip(ys[::7], fr[::7]):
        ax.plot([0.80, 0.80 + 0.08 * amp], [y, y], color=INK, lw=2.0)
    lab(ax, 0.10, 0.22, "source")
    lab(ax, 0.44, 0.22, "two slits")
    lab(ax, 0.88, 0.22, "screen")
    caption(ax, "Both paths contribute. The stripes are the evidence.")
    return save(fig, path)


def fig2(path: Path):
    fig, ax = _fig(7.6, 4.9)
    title(ax, "Measurement basis: the apparatus decides which question is asked")

    def unit(cx, name, angle, out_a, out_b):
        lab(ax, cx + 0.06, 0.80, name, color=INK, size=11)
        ax.annotate("", xy=(cx - 0.02, 0.52), xytext=(cx - 0.16, 0.52),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
        box = mpatches.FancyBboxPatch((cx - 0.01, 0.42), 0.14, 0.20,
                                      boxstyle="round,pad=0.012", facecolor=FILL, edgecolor=INK, lw=1.3)
        ax.add_patch(box)
        rad = np.deg2rad(angle)
        ax.plot([cx + 0.06, cx + 0.06 + 0.05 * np.sin(rad)],
                [0.52, 0.52 + 0.05 * np.cos(rad)], color=INK, lw=2.4)
        ax.annotate("", xy=(cx + 0.28, 0.62), xytext=(cx + 0.14, 0.56),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
        ax.annotate("", xy=(cx + 0.28, 0.42), xytext=(cx + 0.14, 0.48),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
        lab(ax, cx + 0.30, 0.62, out_a, ha="left", color=INK)
        lab(ax, cx + 0.30, 0.42, out_b, ha="left", color=INK)

    lab(ax, 0.10, 0.44, "incoming", size=8.4)
    unit(0.22, "Basis A", 0, "up", "down")
    unit(0.66, "Basis B", 45, "this way", "that way")
    caption(ax, "Same particle. Different magnet. Different question.")
    return save(fig, path)


def fig3(path: Path):
    fig = plt.figure(figsize=(7.6, 6.0), dpi=180)
    fig.patch.set_facecolor(PAPER)
    fig.suptitle("Ask which path, and the pattern that needed both is gone",
                 fontsize=12.0, color=INK, fontname=FONT, y=0.97)
    axes = fig.subplots(2, 1)
    fig.subplots_adjust(hspace=0.38, left=0.06, right=0.96, top=0.88, bottom=0.08)

    def panel(ax, detector=False, foot=""):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_axis_off()
        ax.set_facecolor(PAPER)
        ax.plot(0.08, 0.52, "o", color=INK, ms=7)
        ax.plot([0.38, 0.38], [0.18, 0.40], color=INK, lw=7)
        ax.plot([0.38, 0.38], [0.64, 0.86], color=INK, lw=7)
        ax.plot([0.38, 0.38], [0.48, 0.56], color=INK, lw=7)
        ax.plot([0.08, 0.38], [0.52, 0.44], color=DARK, lw=1.1)
        ax.plot([0.08, 0.38], [0.52, 0.60], color=DARK, lw=1.1)
        ax.plot([0.82, 0.82], [0.16, 0.88], color=INK, lw=5)
        if detector:
            ax.add_patch(mpatches.FancyBboxPatch((0.46, 0.56), 0.14, 0.10,
                                                 boxstyle="round,pad=0.01", facecolor=FILL, edgecolor=INK, lw=1.2))
            lab(ax, 0.53, 0.78, "which-path\ndetector", size=8.4)
            ys = np.linspace(0.28, 0.76, 180)
            clump = np.exp(-((ys - 0.52) / 0.08) ** 2)
            for y, amp in zip(ys[::4], clump[::4]):
                ax.plot([0.82, 0.82 + 0.10 * amp], [y, y], color=INK, lw=1.8)
        else:
            ys = np.linspace(0.20, 0.84, 320)
            env = np.exp(-((ys - 0.52) / 0.22) ** 2)
            fr = env * (np.cos(2 * np.pi * (ys - 0.52) / 0.055) ** 2)
            for y, amp in zip(ys[::6], fr[::6]):
                ax.plot([0.82, 0.82 + 0.10 * amp], [y, y], color=INK, lw=1.8)
        ax.text(0.50, -0.06, foot, ha="center", va="top", fontsize=9.0, color=MUTED, fontname=FONT, clip_on=False)

    panel(axes[0], False, "Interference: both slits used")
    panel(axes[1], True, "One clump: the stripes are gone")
    return save(fig, path)


def fig4(path: Path):
    fig, ax = _fig(7.6, 5.0)
    title(ax, "Quantum Zeno effect: checked often enough, it barely moves")
    cx, cy, r = 0.42, 0.52, 0.24
    ax.add_patch(plt.Circle((cx, cy), r, fill=False, ec=INK, lw=1.6))
    for ang in np.linspace(8, 72, 6):
        rad = np.deg2rad(90 - ang)
        ax.plot(cx + 0.86 * r * np.cos(rad), cy + 0.86 * r * np.sin(rad),
                "o", color=FILL, ms=6, markeredgecolor=LIGHT)
    ax.plot([cx, cx + r], [cy, cy], color=INK, lw=3.0, solid_capstyle="round")
    ax.plot(cx + r, cy, "o", color=INK, ms=7)
    lab(ax, 0.78, 0.78, "if left alone", ha="left")
    lab(ax, 0.78, 0.52, "confirmed\nstate", ha="left", color=INK)
    caption(ax, "Each check measures again, and resets the drift.")
    return save(fig, path)


def fig5(path: Path):
    fig, ax = plt.subplots(figsize=(7.6, 5.0), dpi=180)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    x = np.linspace(-6, 6, 500)
    for sig, y0, tlabel in ((0.45, 2.6, "t = 0"), (0.90, 1.35, "t = 1"), (1.60, 0.10, "t = 2")):
        y = np.exp(-(x**2) / (2 * sig**2))
        y = y / y.max() * 0.80
        ax.plot(x, y + y0, color=INK, lw=1.8)
        ax.text(-5.85, y0 + 0.42, tlabel, fontsize=10, color=INK, fontname=FONT, zorder=20)
    ax.set_xlim(-6.3, 6.3)
    ax.set_ylim(-0.55, 3.85)
    ax.set_axis_off()
    ax.set_title("Lawful evolution: smooth and predictable, no measurement in sight",
                 fontsize=12.0, color=INK, fontname=FONT, pad=12)
    ax.text(0, -0.42, "A wave packet spreads. Run the law backwards and it gathers again.",
            ha="center", fontsize=9.0, color=MUTED, fontname=FONT)
    return save(fig, path)


def fig6(path: Path):
    fig, ax = plt.subplots(figsize=(7.6, 5.0), dpi=180)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    t = np.linspace(0.0, 0.93, 400)
    mass = (1.0 - t) ** (1.0 / 3.0)
    temp = (1.0 / mass)
    temp = temp / temp.max() * 0.95
    ax.plot(t, mass, color=INK, lw=2.2, label="mass (solid)")
    ax.plot(t, temp, color=INK, lw=2.0, ls=(0, (5, 3)), label="temperature (dashed)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.15)
    ax.set_xlabel("time", fontsize=10, color=INK, fontname=FONT)
    ax.set_ylabel("relative value", fontsize=10, color=INK, fontname=FONT)
    for spine in ax.spines.values():
        spine.set_color(INK)
    ax.tick_params(colors=INK, labelbottom=False, labelleft=False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.10), frameon=False, fontsize=9,
              ncol=2, prop={"family": FONT})
    ax.set_title("Hawking radiation: smaller means hotter, hotter means faster",
                 fontsize=12.0, color=INK, fontname=FONT, pad=12)
    fig.subplots_adjust(bottom=0.22, top=0.86, left=0.12, right=0.96)
    return save(fig, path)


def fig7(path: Path):
    fig, ax = _fig(7.6, 5.0)
    title(ax, "Entanglement: a shared fact, not a message")
    for cx, name, dy in ((0.20, "Station A", 0.09), (0.80, "Station B", -0.09)):
        ax.add_patch(mpatches.Ellipse((cx, 0.55), 0.22, 0.16, fill=False, ec=INK, lw=1.5))
        ax.annotate("", xy=(cx, 0.55 + dy), xytext=(cx, 0.55 - dy),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
        lab(ax, cx, 0.38, name, color=INK, size=10)
    ax.plot(0.50, 0.55, marker="*", markersize=16, color=INK, zorder=5)
    lab(ax, 0.50, 0.70, "shared origin", color=INK)
    ax.plot([0.31, 0.69], [0.55, 0.55], ls=(0, (2.5, 2.5)), color=LIGHT, lw=1.2)
    ax.annotate("", xy=(0.72, 0.24), xytext=(0.28, 0.24),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
    ax.plot(0.50, 0.24, marker="x", markersize=14, color=INK, markeredgewidth=2)
    caption(ax, "No signal travels this way.")
    return save(fig, path)


def fig8(path: Path):
    fig, ax = _fig(7.6, 5.0)
    title(ax, "No perfect copy. A spread-out pattern can still be repaired.")
    lab(ax, 0.26, 0.82, "Unknown state", color=INK, size=10.5)
    lab(ax, 0.74, 0.82, "Distributed pattern", color=INK, size=10.5)
    ax.plot(0.10, 0.54, "o", color=INK, ms=7)
    ax.plot([0.12, 0.17], [0.54, 0.54], color=INK, lw=1.2)
    ax.add_patch(mpatches.FancyBboxPatch((0.17, 0.44), 0.18, 0.20,
                                         boxstyle="round,pad=0.01", facecolor=FILL, edgecolor=INK, lw=1.3))
    ax.plot(0.26, 0.54, marker="x", markersize=20, color=INK, markeredgewidth=2.2)
    lab(ax, 0.26, 0.70, "copier?", color=INK)
    ax.plot([0.35, 0.42], [0.60, 0.66], color=INK, lw=1.2)
    ax.plot([0.35, 0.42], [0.48, 0.42], color=INK, lw=1.2)
    ax.plot(0.43, 0.66, "s", color=INK, ms=8)
    ax.plot(0.43, 0.42, "s", color=INK, ms=8)
    lab(ax, 0.26, 0.30, "no perfect copy of\nan unknown state", size=8.6)
    pts = [(0.62, 0.64), (0.86, 0.64), (0.74, 0.40)]
    for a, b in ((0, 1), (1, 2), (2, 0)):
        ax.plot([pts[a][0], pts[b][0]], [pts[a][1], pts[b][1]], color=INK, lw=1.3)
    for i, (x, y) in enumerate(pts):
        ax.plot(x, y, "o", color=PAPER if i else FILL, ms=14, markeredgecolor=INK, markeredgewidth=1.4)
        if i == 0:
            ax.plot(x, y, marker="x", markersize=12, color=INK, markeredgewidth=1.8)
    lab(ax, 0.74, 0.30, "one damaged node —\nthe pattern still holds", size=8.6)
    caption(ax, "You cannot copy the unknown. You can repair a pattern.")
    return save(fig, path)


def fig9(path: Path):
    fig, axes = plt.subplots(2, 2, figsize=(7.6, 5.4), dpi=180)
    fig.patch.set_facecolor(PAPER)
    fig.suptitle("Uncertainty: pin one down, and the other spreads out",
                 fontsize=12.0, color=INK, fontname=FONT, y=0.98)
    x = np.linspace(-6, 6, 400)

    def panel(ax, sig, name):
        ax.set_facecolor(PAPER)
        y = np.exp(-(x**2) / (2 * sig**2))
        ax.plot(x, y, color=INK, lw=1.8)
        ax.set_xlim(-6, 6)
        ax.set_ylim(0, 1.2)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(LIGHT)
        ax.set_title(name, fontsize=9.4, color=INK, fontname=FONT, pad=8)

    panel(axes[0, 0], 0.35, "narrow in position")
    panel(axes[1, 0], 1.80, "broad in momentum")
    panel(axes[0, 1], 1.80, "broad in position")
    panel(axes[1, 1], 0.35, "narrow in momentum")
    axes[0, 0].set_ylabel("position", fontsize=8.6, color=MUTED, fontname=FONT)
    axes[1, 0].set_ylabel("momentum", fontsize=8.6, color=MUTED, fontname=FONT)
    fig.text(0.28, 0.03, "Column 1", ha="center", fontsize=8.6, color=MUTED, fontname=FONT)
    fig.text(0.74, 0.03, "Column 2", ha="center", fontsize=8.6, color=MUTED, fontname=FONT)
    fig.subplots_adjust(hspace=0.42, wspace=0.22, left=0.12, right=0.97, top=0.86, bottom=0.10)
    return save(fig, path)


def fig10(path: Path):
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 5.0), dpi=180)
    fig.patch.set_facecolor(PAPER)
    fig.suptitle("Decoherence: the world is already looking, on nobody's authority",
                 fontsize=12.0, color=INK, fontname=FONT, y=0.96)
    ax = axes[0]
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.set_facecolor(PAPER)
    ax.set_title("Isolated, in principle", fontsize=10.4, color=INK, fontname=FONT, pad=10)
    ax.add_patch(plt.Circle((0.50, 0.52), 0.16, fill=False, ec=INK, lw=1.6))
    ax.text(0.50, 0.12, "Few records in the surroundings.\nInterference can still survive.",
            ha="center", va="center", fontsize=8.6, color=MUTED, fontname=FONT)
    ax = axes[1]
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.set_facecolor(PAPER)
    ax.set_title("The moon, in contact with the sky", fontsize=10.4, color=INK, fontname=FONT, pad=10)
    ax.add_patch(plt.Circle((0.50, 0.52), 0.13, facecolor=FILL, edgecolor=INK, lw=1.4))
    for ang in np.linspace(0, 360, 16, endpoint=False):
        rad = np.deg2rad(ang)
        ax.plot([0.50 + 0.16 * np.cos(rad), 0.50 + 0.30 * np.cos(rad)],
                [0.52 + 0.16 * np.sin(rad), 0.52 + 0.30 * np.sin(rad)], color=INK, lw=1.0)
    ax.text(0.50, 0.12, "Air, light and warmth notice it constantly.\nNo rota required.",
            ha="center", va="center", fontsize=8.6, color=MUTED, fontname=FONT)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.80, bottom=0.10, wspace=0.10)
    return save(fig, path)


def fig11(path: Path):
    fig, ax = _fig(7.6, 5.2)
    title(ax, "Wigner's friend: definite inside, still open from outside")
    ax.add_patch(mpatches.FancyBboxPatch((0.08, 0.20), 0.84, 0.62,
                                         boxstyle="round,pad=0.01", facecolor=PAPER, edgecolor=INK, lw=1.6))
    ax.add_patch(mpatches.FancyBboxPatch((0.14, 0.38), 0.38, 0.34,
                                         boxstyle="round,pad=0.01", facecolor=FILL, edgecolor=INK, lw=1.4))
    ax.add_patch(plt.Circle((0.24, 0.55), 0.05, fill=False, ec=INK, lw=1.3))
    lab(ax, 0.24, 0.55, "S", color=INK, size=9)
    lab(ax, 0.40, 0.55, "Friend has a record\n(yes or no)", color=INK, size=8.4)
    lab(ax, 0.33, 0.30, "Inside the lab", color=INK, size=9)
    lab(ax, 0.72, 0.55, "Wigner, outside, must still\ndescribe the whole room as\none unresolved system",
        color=INK, size=8.4)
    caption(ax, "There is no view from nowhere.")
    return save(fig, path)


def fig12(path: Path):
    fig, ax = _fig(7.6, 5.1)
    title(ax, "Pilot-wave theory: one path taken, guided by all the others")
    x0, xb, xs = 0.10, 0.50, 0.86
    y0, y_up, y_lo = 0.50, 0.58, 0.42

    def wave(cx, cy, radii, x_lo, x_hi, y_lo_b, y_hi_b):
        th = np.linspace(0, 2 * np.pi, 800)
        for r in radii:
            x = cx + r * np.cos(th)
            y = cy + r * np.sin(th)
            m = (x >= x_lo) & (x <= x_hi) & (y >= y_lo_b) & (y <= y_hi_b)
            if m.sum() < 10:
                continue
            idx = np.where(m)[0]
            gaps = np.where(np.diff(idx) > 1)[0]
            bounds = np.r_[0, gaps + 1, len(idx)]
            for a, b in zip(bounds[:-1], bounds[1:]):
                sl = idx[a:b]
                if len(sl) > 8:
                    ax.plot(x[sl], y[sl], color="#C8C8C8", lw=0.55, alpha=0.55, zorder=1)

    wave(x0, y0, np.arange(0.06, 0.40, 0.045), x0, xb - 0.01, 0.22, 0.78)
    wave(xb, y_up, np.arange(0.05, 0.42, 0.045), xb + 0.01, xs - 0.01, 0.22, 0.78)
    wave(xb, y_lo, np.arange(0.05, 0.42, 0.045), xb + 0.01, xs - 0.01, 0.22, 0.78)
    ax.plot([x0, xb], [y0, y_lo], color="#BFBFBF", lw=1.05, zorder=3)
    for y_end in (0.46, 0.40, 0.34, 0.28):
        ax.plot([xb, xs], [y_lo, y_end], color="#BFBFBF", lw=1.05, zorder=3)
    for y_end in (0.72, 0.66, 0.60):
        ax.plot([xb, xs], [y_up, y_end], color="#BFBFBF", lw=1.05, zorder=3)
    ax.plot([x0, xb], [y0, y_up], color=INK, lw=2.15, zorder=5)
    bx = np.linspace(xb, xs, 80)
    by = y_up + 0.05 * ((bx - xb) / (xs - xb)) ** 1.15
    ax.plot(bx, by, color=INK, lw=2.15, zorder=5)
    ax.plot(x0, y0, "o", color=INK, ms=6.2, zorder=6)
    ax.plot(xs, by[-1], "o", color=INK, ms=5.2, zorder=6)
    ax.plot([xb, xb], [0.61, 0.74], color=INK, lw=5.0, zorder=7)
    ax.plot([xb, xb], [0.26, 0.39], color=INK, lw=5.0, zorder=7)
    ax.plot([xs, xs], [0.22, 0.78], color=INK, lw=5.0, zorder=7)
    lab(ax, 0.10, 0.20, "source")
    lab(ax, 0.86, 0.20, "screen")
    pad = dict(facecolor=PAPER, edgecolor="none", pad=1.6)
    lab(ax, 0.08, 0.84, "actual path (solid)", color=INK, size=8.4, ha="left", bbox=pad)
    lab(ax, 0.08, 0.78, "empty paths (pale)", size=8.4, ha="left", bbox=pad)
    caption(ax, "The empty paths do not cross the one that is taken.")
    return save(fig, path)


def fig13(path: Path):
    fig, ax = plt.subplots(figsize=(7.6, 4.8), dpi=180)
    fig.patch.set_facecolor(PAPER)
    ax.set_xlim(0, 7.6)
    ax.set_ylim(0, 4.8)
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.set_facecolor(PAPER)
    ax.text(3.8, 4.55, "Bell / CHSH: measured correlations exceed the local ceiling",
            ha="center", va="center", fontsize=11.6, color=INK, fontname=FONT, zorder=20)
    ax.text(1.85, 3.85, "A number, not an interpretation", ha="center", fontsize=10.4, color=INK, fontname=FONT)
    ax.text(6.35, 3.85, "S", ha="center", fontsize=12.2, color=INK, fontname=FONT)
    for cx, name in ((0.95, "a / a'"), (2.75, "b / b'")):
        ax.add_patch(plt.Circle((cx, 2.35), 0.40, fill=False, ec=INK, lw=1.4))
        ax.text(cx, 2.35, name, ha="center", va="center", fontsize=9.2, color=INK, fontname=FONT, zorder=20)
        ax.text(cx, 1.55, "setting chosen\nafter separation", ha="center", va="top",
                fontsize=8.2, color=MUTED, fontname=FONT)
    ax.plot([1.35, 2.35], [2.35, 2.35], ls=(0, (2.4, 2.6)), color=INK, lw=1.2)
    ax.plot(1.85, 2.35, marker="*", markersize=12, color=INK)
    ax.add_patch(plt.Rectangle((4.55, 1.05), 0.72, 1.15, facecolor="#B0B0B0", edgecolor=INK, lw=0.8))
    ax.add_patch(plt.Rectangle((5.85, 1.05), 0.72, 1.62, facecolor=DARK, edgecolor=INK, lw=0.8))
    ax.plot([4.38, 6.74], [1.05, 1.05], color=INK, lw=1.1)
    ax.text(4.91, 2.30, "2", ha="center", va="bottom", fontsize=10.2, color=INK, fontname=FONT)
    ax.text(6.21, 2.78, "2.83", ha="center", va="bottom", fontsize=10.2, color=INK, fontname=FONT)
    ax.text(4.91, 0.70, "local limit", ha="center", fontsize=8.6, color=MUTED, fontname=FONT)
    ax.text(6.21, 0.70, "quantum ceiling", ha="center", fontsize=8.6, color=MUTED, fontname=FONT)
    fig.subplots_adjust(left=0.03, right=0.97, top=0.96, bottom=0.06)
    return save(fig, path)


def fig14(path: Path):
    fig, ax = _fig(6.0, 6.4)
    title(ax, "Five theories, seen from five sides")
    ax.add_patch(plt.Circle((0.50, 0.50), 0.10, facecolor=DARK, edgecolor=INK, lw=1.2, zorder=4))
    lab(ax, 0.50, 0.36, "M-theory", color=INK, size=10)
    names = [
        (0.50, 0.78, "Type I"),
        (0.16, 0.64, "Type IIA"),
        (0.16, 0.32, "Type IIB"),
        (0.84, 0.64, "Heterotic\nE8 x E8"),
        (0.84, 0.32, "Heterotic\nSO(32)"),
    ]
    for x, y, name in names:
        ax.plot([0.50, x], [0.50, y], color=LIGHT, lw=1.1, zorder=1)
        ax.add_patch(plt.Circle((x, y), 0.075, facecolor=PAPER, edgecolor=INK, lw=1.3, zorder=3))
        if x < 0.50:
            lab(ax, x - 0.11, y, name, color=INK, size=8.0, ha="right")
        elif x > 0.50:
            lab(ax, x + 0.11, y, name, color=INK, size=8.0, ha="left")
        else:
            lab(ax, x + 0.12, y, name, color=INK, size=8.0, ha="left")
    caption(ax, "Same structure. Five limited views.")
    return save(fig, path)


def fig15(path: Path):
    fig, ax = _fig(6.0, 6.4)
    title(ax, "Holography: the boundary carries the account")
    ax.add_patch(plt.Circle((0.50, 0.46), 0.24, facecolor="#F0F0F0", edgecolor=INK, lw=2.0))
    th = np.linspace(0, 2 * np.pi, 36, endpoint=False)
    ax.plot(0.50 + 0.24 * np.cos(th), 0.46 + 0.24 * np.sin(th), "o", color=INK, ms=3.4)
    lab(ax, 0.50, 0.50, "volume", color=INK, size=11)
    lab(ax, 0.50, 0.42, "(the interior)", size=8.6)
    ax.annotate("all of it, in principle,\nreadable on this edge",
                xy=(0.50 + 0.24 * np.cos(np.pi / 5), 0.46 + 0.24 * np.sin(np.pi / 5)),
                xytext=(0.78, 0.78), fontsize=8.6, color=INK, fontname=FONT, ha="left",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.0),
                zorder=20)
    caption(ax, "The account is kept on the surface, not lost inside.")
    return save(fig, path)


def fig16(path: Path):
    fig, ax = _fig(7.6, 4.0)
    title(ax, "Honest recovery: repaired, inferred, and named as gone")
    pattern = list("RRGIRRRRIRGRIRRG")
    x0, y1, y0, s, gap = 0.10, 0.58, 0.36, 0.075, 0.025
    for i, kind in enumerate(pattern):
        r, c = divmod(i, 8)
        x = x0 + c * (s + gap)
        y = y1 if r == 0 else y0
        if kind == "R":
            ax.add_patch(plt.Rectangle((x, y), s, s, facecolor=DARK, edgecolor=INK, lw=0.8))
        elif kind == "I":
            ax.add_patch(plt.Rectangle((x, y), s, s, facecolor=PAPER, edgecolor=INK, lw=0.8))
            for k in range(1, 4):
                ax.plot([x + k * s / 4, x + k * s / 4], [y, y + s], color=INK, lw=0.6)
        else:
            ax.add_patch(plt.Rectangle((x, y), s, s, facecolor="#E6E6E6", edgecolor=INK, lw=0.8))
            ax.plot([x + 0.012, x + s - 0.012], [y + 0.012, y + s - 0.012], color=INK, lw=1.4)
            ax.plot([x + 0.012, x + s - 0.012], [y + s - 0.012, y + 0.012], color=INK, lw=1.4)
    caption(ax, "solid = recovered     hatched = inferred     cross = named gone", y=0.10)
    return save(fig, path)


def fig17(path: Path):
    fig, ax = _fig(7.6, 4.6)
    title(ax, "The long future: an enormous middle, and then very little")
    ax.annotate("", xy=(0.94, 0.72), xytext=(0.06, 0.72),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    lab(ax, 0.08, 0.80, "now", size=8.2, ha="left")
    lab(ax, 0.70, 0.80, "an unreasonably long time from now", size=8.2, ha="left")
    eras = [
        (0.08, "stelliferous\nera", "10^0 - 10^14 yr", "#222222", "#FFFFFF"),
        (0.32, "degenerate\nera", "10^14 - 10^37 yr", "#666666", "#FFFFFF"),
        (0.56, "black-hole\nera", "10^37 - 10^100 yr", "#A0A0A0", "#111111"),
        (0.80, "dark\nera", "beyond 10^100 yr", "#E0E0E0", "#111111"),
    ]
    for x, name, years, g, tc in eras:
        ax.add_patch(plt.Rectangle((x, 0.32), 0.16, 0.28, facecolor=g, edgecolor=INK, lw=1.1))
        ax.text(x + 0.08, 0.46, name, ha="center", va="center", fontsize=8.0, color=tc, fontname=FONT, zorder=20)
        lab(ax, x + 0.08, 0.22, years, size=7.6)
    caption(ax, "The boxes are not to scale. Almost all of history is afterwards.")
    return save(fig, path)


FIGURES = [
    ("image1.png", fig1),
    ("image2.jpeg", fig2),
    ("image3.png", fig3),
    ("image4.jpeg", fig4),
    ("image5.jpeg", fig5),
    ("image6.png", fig6),
    ("image7.jpeg", fig7),
    ("image8.jpeg", fig8),
    ("image9.jpeg", fig9),
    ("image10.jpeg", fig10),
    ("image11.jpeg", fig11),
    ("image12.png", fig12),
    ("image13.png", fig13),
    ("image14.png", fig14),
    ("image15.png", fig15),
    ("image16.png", fig16),
    ("image17.png", fig17),
]


def update_extents(xml: str, sizes: dict[str, tuple[int, int]]) -> str:
    max_cx = 5486400

    def repl(match: re.Match) -> str:
        block = match.group(0)
        rid_m = re.search(r'r:embed="(rId\d+)"', block)
        if not rid_m:
            return block
        media = RID_TO_MEDIA.get(rid_m.group(1))
        if not media or media not in sizes:
            return block
        w, h = sizes[media]
        cx = max_cx
        cy = int(max_cx * (h / w))
        block = re.sub(r'<wp:extent cx="\d+" cy="\d+"/>', f'<wp:extent cx="{cx}" cy="{cy}"/>', block, count=1)
        block = re.sub(r'(<a:ext cx=")\d+(" cy=")\d+("/>)', rf"\g<1>{cx}\g<2>{cy}\g<3>", block, count=1)
        alt = ALTS.get(media, "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        if alt:
            if 'descr="' in block:
                block = re.sub(r'descr="[^"]*"', f'descr="{alt}"', block, count=1)
            else:
                block = block.replace("<wp:docPr ", f'<wp:docPr descr="{alt}" ', 1)
        return block

    return re.sub(r"<w:drawing>.*?</w:drawing>", repl, xml, flags=re.DOTALL)


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    sizes = {}
    for name, fn in FIGURES:
        dest = ASSETS / name
        w, h = fn(dest)
        sizes[name] = (w, h)
        print(f"drew {name:14s} {w}x{h}")

    source = DOCX if DOCX.exists() else None
    for fallback in (DOCX.with_suffix(".docx.next"), DOCX.with_suffix(".docx.repack")):
        if source is None and fallback.exists():
            source = fallback
    if source is None:
        raise SystemExit(f"No book file found at {DOCX}")

    tmp = Path(tempfile.mkdtemp(prefix="sp_redraw_"))
    with zipfile.ZipFile(source) as z:
        z.extractall(tmp)
    media = tmp / "word" / "media"
    for name in sizes:
        shutil.copyfile(ASSETS / name, media / name)
    xml_path = tmp / "word" / "document.xml"
    xml_path.write_text(update_extents(xml_path.read_text(encoding="utf-8"), sizes), encoding="utf-8")
    out = DOCX.with_suffix(".docx.next")
    if out.exists() and out.resolve() != source.resolve():
        out.unlink()
    packed = out if out.resolve() != source.resolve() else DOCX.with_suffix(".docx.ready")
    if packed.exists():
        packed.unlink()
    with zipfile.ZipFile(packed, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(tmp.rglob("*")):
            if path.is_file():
                z.write(path, path.relative_to(tmp).as_posix())
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        if DOCX.exists():
            DOCX.unlink()
        shutil.copyfile(packed, DOCX)
        print("updated", DOCX, "mb", round(DOCX.stat().st_size / 1e6, 2))
    except PermissionError as e:
        print("Word has the live file open. Updated copy saved as", packed)
        print(e)


if __name__ == "__main__":
    main()
