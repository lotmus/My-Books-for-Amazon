"""Regenerate appendix figures and patch Schrodingers_Paperwork_BOOK_1_2.docx."""

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
BACKUP = Path(
    r"D:\My Books for Amazon\Schrodingers_Paperwork\English"
    r"\Schrodingers_Paperwork_BOOK_1_2_BEFORE_FIGURE_FIX_BACKUP.docx"
)
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
    "image1.png": "Diagram: a double-slit experiment. Light or particles pass through two slits and form an interference pattern of many stripes on a screen.",
    "image2.jpeg": "Diagram: the same incoming particle sent into two differently oriented measuring devices, showing that the apparatus chooses which question is asked.",
    "image3.png": "Two-panel diagram: two-slit interference on top; the same setup below with a which-path detector on one slit, leaving only a single clump on the screen.",
    "image4.jpeg": "Diagram of the quantum Zeno effect: a pointer that would drift if left alone is repeatedly reset to its starting position by checks.",
    "image5.jpeg": "Diagram: a wave packet spreading smoothly and reversibly at three later times, with no measurement interrupting it.",
    "image6.png": "Graph: black-hole mass falling and Hawking temperature rising as one over mass, so the loss accelerates as the hole shrinks.",
    "image7.jpeg": "Diagram: two distant stations sharing one entangled origin. A barred line between them is labelled 'no signal travels this way'.",
    "image8.jpeg": "Two-panel diagram: an unknown state cannot be copied; a pattern spread across several nodes can still be repaired if one node is damaged.",
    "image9.jpeg": "Diagram of the uncertainty principle: a narrow peak in position goes with a wide spread in momentum, and the reverse.",
    "image10.jpeg": "Two-panel diagram: an isolated system on the left; on the right a moon constantly interacting with air, light and warmth, which is enough to keep it ordinary.",
    "image11.jpeg": "Diagram of Wigner's friend: an inner box where a friend has already recorded a definite result, inside an outer description that is still unresolved.",
    "image12.png": "Diagram: one actual particle path through a two-slit barrier, with empty trajectories that do not cross it and a guiding wave through both slits.",
    "image13.png": "Diagram: two Bell-test stations with settings chosen after separation, beside bars for the local limit of 2 and the quantum ceiling of 2.83.",
    "image14.png": "Diagram: five named string theories connected to a central hub labelled M-theory.",
    "image15.png": "Diagram: a disk representing a volume of space, with its dotted boundary marked as carrying the region's full information.",
    "image16.png": "Diagram: sixteen tiles marked as recovered, recovered by inference, or named as permanently gone, kept distinct by fill and a cross.",
    "image17.png": "Timeline: the universe's long future divided into the stelliferous, degenerate, black-hole and dark eras.",
}


def _fig(w=7.4, h=4.3):
    fig, ax = plt.subplots(figsize=(w, h), dpi=180)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    return fig, ax


def title(ax, text, y=0.94, size=12.2):
    ax.text(0.5, y, text, ha="center", va="center", fontsize=size, color=INK, fontname=FONT, fontweight="medium")


def label(ax, x, y, text, size=9.2, color=MUTED, ha="center", va="center", **kw):
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color, fontname=FONT, **kw)


def save(fig, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".tmp.png")
    fig.savefig(tmp, dpi=180, facecolor=PAPER, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)
    im = Image.open(tmp).convert("RGB")
    # force true grayscale for e-ink, then save in the package's existing format
    im = im.convert("L").convert("RGB")
    if dest.suffix.lower() in {".jpg", ".jpeg"}:
        im.save(dest, "JPEG", quality=88, optimize=True)
    else:
        im.save(dest, "PNG", optimize=True)
    tmp.unlink(missing_ok=True)
    return im.size


def fig1_superposition(path: Path):
    fig, ax = _fig(7.4, 4.2)
    title(ax, "Superposition: both paths, until one is asked")
    # source
    ax.plot(0.08, 0.48, "o", color=INK, ms=8, zorder=5)
    label(ax, 0.08, 0.18, "source")
    # barrier: two slits
    ax.plot([0.42, 0.42], [0.12, 0.36], color=INK, lw=7, solid_capstyle="butt")
    ax.plot([0.42, 0.42], [0.60, 0.84], color=INK, lw=7, solid_capstyle="butt")
    ax.plot([0.42, 0.42], [0.44, 0.52], color=INK, lw=7, solid_capstyle="butt")
    label(ax, 0.42, 0.18, "two slits")
    # rays
    ax.plot([0.08, 0.42], [0.48, 0.40], color=DARK, lw=1.2)
    ax.plot([0.08, 0.42], [0.48, 0.56], color=DARK, lw=1.2)
    # screen
    ax.plot([0.88, 0.88], [0.16, 0.80], color=INK, lw=6, solid_capstyle="butt")
    label(ax, 0.88, 0.10, "screen")
    # interference stripes on screen
    ys = np.linspace(0.20, 0.76, 400)
    envelope = np.exp(-((ys - 0.48) / 0.22) ** 2)
    fringes = envelope * (np.cos(2 * np.pi * (ys - 0.48) / 0.055) ** 2)
    for y, amp in zip(ys[::8], fringes[::8]):
        ax.plot([0.88, 0.88 + 0.07 * amp], [y, y], color=INK, lw=2.0)
    # faint paths to screen
    ax.plot([0.42, 0.88], [0.40, 0.48], color=LIGHT, lw=0.8)
    ax.plot([0.42, 0.88], [0.56, 0.48], color=LIGHT, lw=0.8)
    label(ax, 0.66, 0.18, "both paths contribute;\nthe stripes are the evidence", size=8.6)
    return save(fig, path)


def fig2_basis(path: Path):
    fig, ax = _fig(7.4, 4.3)
    title(ax, "Measurement basis: the apparatus decides which question is asked")

    def apparatus(cx, cy, angle_deg, name, out_a, out_b):
        label(ax, cx, 0.82, name, size=11, color=INK)
        # incoming
        ax.annotate(
            "",
            xy=(cx - 0.04, cy),
            xytext=(cx - 0.20, cy),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
        )
        label(ax, cx - 0.20, cy - 0.08, "incoming", size=8)
        # magnet box
        box = mpatches.FancyBboxPatch(
            (cx - 0.04, cy - 0.10),
            0.14,
            0.20,
            boxstyle="round,pad=0.01,rounding_size=0.02",
            facecolor=FILL,
            edgecolor=INK,
            lw=1.3,
            transform=ax.transData,
        )
        ax.add_patch(box)
        # orientation mark
        rad = np.deg2rad(angle_deg)
        ax.plot(
            [cx + 0.03, cx + 0.03 + 0.07 * np.sin(rad)],
            [cy, cy + 0.07 * np.cos(rad)],
            color=INK,
            lw=2.2,
        )
        # outputs
        ax.annotate(
            "",
            xy=(cx + 0.28, cy + 0.10),
            xytext=(cx + 0.11, cy + 0.04),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
        )
        ax.annotate(
            "",
            xy=(cx + 0.28, cy - 0.10),
            xytext=(cx + 0.11, cy - 0.04),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
        )
        label(ax, cx + 0.30, cy + 0.10, out_a, size=8.4, ha="left")
        label(ax, cx + 0.30, cy - 0.10, out_b, size=8.4, ha="left")

    apparatus(0.28, 0.48, 0, "Basis A", "up", "down")
    apparatus(0.72, 0.48, 45, "Basis B", "this way", "that way")
    label(ax, 0.50, 0.10, "Same particle. Different magnet. Different question.", size=9.4, color=INK)
    return save(fig, path)


def fig3_which_path(path: Path):
    fig, axes = plt.subplots(2, 1, figsize=(7.4, 5.2), dpi=180)
    fig.patch.set_facecolor(PAPER)

    def slits(ax, detector=False):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_axis_off()
        ax.set_facecolor(PAPER)
        ax.plot(0.08, 0.50, "o", color=INK, ms=7)
        ax.plot([0.40, 0.40], [0.08, 0.38], color=INK, lw=6)
        ax.plot([0.40, 0.40], [0.62, 0.92], color=INK, lw=6)
        ax.plot([0.40, 0.40], [0.46, 0.54], color=INK, lw=6)
        ax.plot([0.08, 0.40], [0.50, 0.42], color=DARK, lw=1.1)
        ax.plot([0.08, 0.40], [0.50, 0.58], color=DARK, lw=1.1)
        ax.plot([0.86, 0.86], [0.12, 0.88], color=INK, lw=5)
        if detector:
            det = mpatches.FancyBboxPatch(
                (0.43, 0.54), 0.12, 0.12, boxstyle="round,pad=0.01", facecolor=FILL, edgecolor=INK, lw=1.2
            )
            ax.add_patch(det)
            label(ax, 0.49, 0.72, "which-path\ndetector", size=8)
            # single clump
            ys = np.linspace(0.22, 0.78, 200)
            clump = np.exp(-((ys - 0.50) / 0.09) ** 2)
            for y, amp in zip(ys[::4], clump[::4]):
                ax.plot([0.86, 0.86 + 0.10 * amp], [y, y], color=INK, lw=1.8)
            label(ax, 0.68, 0.16, "one clump: the stripes are gone")
        else:
            ys = np.linspace(0.16, 0.84, 400)
            env = np.exp(-((ys - 0.50) / 0.24) ** 2)
            fr = env * (np.cos(2 * np.pi * (ys - 0.50) / 0.06) ** 2)
            for y, amp in zip(ys[::7], fr[::7]):
                ax.plot([0.86, 0.86 + 0.10 * amp], [y, y], color=INK, lw=1.8)
            label(ax, 0.68, 0.16, "interference: both slits used")

    title(axes[0], "Ask which path, and the pattern that needed both is gone", y=0.92, size=12)
    slits(axes[0], detector=False)
    slits(axes[1], detector=True)
    fig.subplots_adjust(hspace=0.08, left=0.04, right=0.98, top=0.93, bottom=0.04)
    return save(fig, path)


def fig4_zeno(path: Path):
    fig, ax = _fig(7.4, 4.4)
    title(ax, "Quantum Zeno effect: checked often enough, it barely moves")
    cx, cy, r = 0.50, 0.46, 0.28
    circ = plt.Circle((cx, cy), r, fill=False, ec=INK, lw=1.5)
    ax.add_patch(circ)
    # free-evolution ticks along an arc
    for ang in np.linspace(0, 70, 6):
        rad = np.deg2rad(90 - ang)
        ax.plot(
            cx + 0.92 * r * np.cos(rad),
            cy + 0.92 * r * np.sin(rad),
            "o",
            color=FILL,
            ms=6,
            markeredgecolor=LIGHT,
        )
    label(ax, 0.78, 0.72, "if left alone", size=9)
    # confirmed state: horizontal pointer
    ax.plot([cx, cx + r], [cy, cy], color=INK, lw=3.0, solid_capstyle="round")
    ax.plot(cx + r, cy, "o", color=INK, ms=7)
    label(ax, 0.78, 0.46, "confirmed\nstate", size=9, ha="left")
    label(ax, 0.50, 0.10, "Each check measures again, and resets the drift.", size=9.6, color=INK)
    return save(fig, path)


def fig5_evolution(path: Path):
    fig, ax = plt.subplots(figsize=(7.4, 4.2), dpi=180)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    x = np.linspace(-6, 6, 500)
    for i, (sig, y0, tlabel) in enumerate(((0.45, 2.4, "t = 0"), (0.90, 1.2, "t = 1"), (1.60, 0.0, "t = 2"))):
        y = np.exp(-(x**2) / (2 * sig**2)) / (sig * np.sqrt(2 * np.pi))
        y = y / y.max() * 0.85
        ax.plot(x, y + y0, color=INK, lw=1.8)
        ax.text(-5.7, y0 + 0.55, tlabel, fontsize=10, color=INK, fontname=FONT)
    ax.set_xlim(-6.2, 6.2)
    ax.set_ylim(-0.2, 3.6)
    ax.set_axis_off()
    ax.set_title(
        "Lawful evolution: smooth and predictable, no measurement in sight",
        fontsize=12.2,
        color=INK,
        fontname=FONT,
        pad=10,
    )
    ax.text(
        0,
        -0.08,
        "A wave packet spreads. Run the law backwards and it gathers again.",
        ha="center",
        fontsize=9.2,
        color=MUTED,
        fontname=FONT,
    )
    return save(fig, path)


def fig6_hawking(path: Path):
    fig, ax = plt.subplots(figsize=(7.4, 4.4), dpi=180)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    t = np.linspace(0.0, 0.93, 400)
    mass = (1.0 - t) ** (1.0 / 3.0)
    temp = (1.0 / mass) / (1.0 / mass[0])
    temp = temp / temp.max() * 0.95
    ax.plot(t, mass, color=INK, lw=2.2, label="mass (solid)")
    ax.plot(t, temp, color=INK, lw=2.0, ls=(0, (5, 3)), label="temperature (dashed)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("time", fontsize=10, color=INK, fontname=FONT)
    ax.set_ylabel("relative value", fontsize=10, color=INK, fontname=FONT)
    for spine in ax.spines.values():
        spine.set_color(INK)
    ax.tick_params(colors=INK, labelsize=8)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend(loc="center left", frameon=False, fontsize=9, prop={"family": FONT})
    ax.set_title(
        "Hawking radiation: smaller means hotter, hotter means faster",
        fontsize=12.2,
        color=INK,
        fontname=FONT,
        pad=10,
    )
    return save(fig, path)


def fig7_entanglement(path: Path):
    fig, ax = _fig(7.4, 4.2)
    title(ax, "Entanglement: a shared fact, not a message")
    for cx, name, dy in ((0.18, "Station A", 0.10), (0.82, "Station B", -0.10)):
        circ = plt.Circle((cx, 0.48), 0.10, fill=False, ec=INK, lw=1.6)
        ax.add_patch(circ)
        ax.annotate(
            "",
            xy=(cx, 0.48 + dy + 0.02),
            xytext=(cx, 0.48 - dy),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
        )
        label(ax, cx, 0.28, name, color=INK, size=10)
    ax.plot(0.50, 0.48, marker="*", markersize=16, color=INK)
    label(ax, 0.50, 0.62, "shared origin", color=INK)
    ax.plot([0.28, 0.72], [0.48, 0.48], ls=(0, (2.5, 2.5)), color=LIGHT, lw=1.2)
    # barred 'no signal' between stations, lower
    ax.annotate(
        "",
        xy=(0.72, 0.16),
        xytext=(0.28, 0.16),
        arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3),
    )
    ax.plot([0.48, 0.52], [0.12, 0.20], color=INK, lw=1.8)
    label(ax, 0.50, 0.08, "no signal travels this way", color=INK, size=9.4)
    return save(fig, path)


def fig8_noclone(path: Path):
    fig, ax = _fig(7.4, 4.3)
    title(ax, "No perfect copy. A spread-out pattern can still be repaired.")
    # left: forbidden copy
    label(ax, 0.24, 0.78, "Unknown state", color=INK, size=10)
    box = mpatches.FancyBboxPatch((0.16, 0.42), 0.16, 0.18, boxstyle="round,pad=0.01", facecolor=FILL, edgecolor=INK, lw=1.3)
    ax.add_patch(box)
    label(ax, 0.24, 0.51, "copier?", color=INK)
    ax.plot(0.10, 0.51, "o", color=INK, ms=7)
    ax.plot([0.11, 0.16], [0.51, 0.51], color=INK, lw=1.2)
    ax.plot([0.32, 0.40], [0.58, 0.64], color=INK, lw=1.2)
    ax.plot([0.32, 0.40], [0.44, 0.38], color=INK, lw=1.2)
    ax.plot(0.42, 0.64, "s", color=INK, ms=8)
    ax.plot(0.42, 0.38, "s", color=INK, ms=8)
    ax.plot(0.24, 0.51, marker="x", markersize=22, color=INK, markeredgewidth=2.2)
    label(ax, 0.24, 0.22, "no perfect copy of\nan unknown state", size=8.8)
    # right: triangle code
    label(ax, 0.74, 0.78, "Distributed pattern", color=INK, size=10)
    pts = [(0.62, 0.62), (0.86, 0.62), (0.74, 0.38)]
    for a, b in ((0, 1), (1, 2), (2, 0)):
        ax.plot([pts[a][0], pts[b][0]], [pts[a][1], pts[b][1]], color=INK, lw=1.3)
    for i, (x, y) in enumerate(pts):
        face = PAPER if i else FILL
        ax.plot(x, y, "o", color=face, ms=14, markeredgecolor=INK, markeredgewidth=1.4)
        if i == 0:
            ax.plot(x, y, marker="x", markersize=12, color=INK, markeredgewidth=1.8)
    label(ax, 0.74, 0.22, "one damaged node —\nthe pattern still holds", size=8.8)
    return save(fig, path)


def fig9_uncertainty(path: Path):
    fig, axes = plt.subplots(2, 2, figsize=(7.4, 4.6), dpi=180)
    fig.patch.set_facecolor(PAPER)
    fig.suptitle(
        "Uncertainty: pin one down, and the other spreads out",
        fontsize=12.2,
        color=INK,
        fontname=FONT,
        y=0.98,
    )
    x = np.linspace(-6, 6, 400)

    def panel(ax, sig, name):
        ax.set_facecolor(PAPER)
        y = np.exp(-(x**2) / (2 * sig**2))
        ax.plot(x, y, color=INK, lw=1.8)
        ax.set_xlim(-6, 6)
        ax.set_ylim(0, 1.15)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(LIGHT)
        ax.set_title(name, fontsize=9.4, color=INK, fontname=FONT, pad=4)

    panel(axes[0, 0], 0.35, "narrow in position")
    panel(axes[1, 0], 1.80, "broad in momentum")
    panel(axes[0, 1], 1.80, "broad in position")
    panel(axes[1, 1], 0.35, "narrow in momentum")
    axes[0, 0].set_ylabel("position", fontsize=8.6, color=MUTED, fontname=FONT)
    axes[1, 0].set_ylabel("momentum", fontsize=8.6, color=MUTED, fontname=FONT)
    fig.text(0.27, 0.02, "Column 1", ha="center", fontsize=8.6, color=MUTED, fontname=FONT)
    fig.text(0.75, 0.02, "Column 2", ha="center", fontsize=8.6, color=MUTED, fontname=FONT)
    fig.subplots_adjust(hspace=0.35, wspace=0.22, left=0.10, right=0.97, top=0.88, bottom=0.08)
    return save(fig, path)


def fig10_decoherence(path: Path):
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 4.3), dpi=180)
    fig.patch.set_facecolor(PAPER)
    fig.suptitle(
        "Decoherence: the world is already looking, on nobody's authority",
        fontsize=12.0,
        color=INK,
        fontname=FONT,
        y=0.96,
    )
    # isolated
    ax = axes[0]
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.set_facecolor(PAPER)
    ax.add_patch(plt.Circle((0.50, 0.48), 0.16, fill=False, ec=INK, lw=1.6))
    ax.set_title("Isolated, in principle", fontsize=10.2, color=INK, fontname=FONT)
    label(ax, 0.50, 0.14, "Few records in the surroundings.\nInterference can still survive.", size=8.4)
    # embedded / moon
    ax = axes[1]
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.set_facecolor(PAPER)
    ax.add_patch(plt.Circle((0.50, 0.48), 0.14, facecolor=FILL, edgecolor=INK, lw=1.4))
    for ang in np.linspace(0, 360, 16, endpoint=False):
        rad = np.deg2rad(ang)
        ax.plot(
            [0.50 + 0.16 * np.cos(rad), 0.50 + 0.34 * np.cos(rad)],
            [0.48 + 0.16 * np.sin(rad), 0.48 + 0.34 * np.sin(rad)],
            color=INK,
            lw=1.0,
        )
    ax.set_title("The moon, in contact with the sky", fontsize=10.2, color=INK, fontname=FONT)
    label(ax, 0.50, 0.14, "Air, light and warmth notice it constantly.\nNo rota required.", size=8.4)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.82, bottom=0.06, wspace=0.08)
    return save(fig, path)


def fig11_wigner(path: Path):
    fig, ax = _fig(7.4, 4.6)
    title(ax, "Wigner's friend: definite inside, still open from outside")
    outer = mpatches.FancyBboxPatch((0.08, 0.12), 0.84, 0.70, boxstyle="round,pad=0.01", facecolor=PAPER, edgecolor=INK, lw=1.6)
    inner = mpatches.FancyBboxPatch((0.16, 0.28), 0.40, 0.42, boxstyle="round,pad=0.01", facecolor=FILL, edgecolor=INK, lw=1.4)
    ax.add_patch(outer)
    ax.add_patch(inner)
    ax.add_patch(plt.Circle((0.28, 0.48), 0.055, fill=False, ec=INK, lw=1.3))
    label(ax, 0.28, 0.48, "S", color=INK, size=9)
    label(ax, 0.44, 0.50, "Friend\nhas a record\n(yes or no)", color=INK, size=8.6)
    label(ax, 0.36, 0.22, "Inside the lab", color=INK, size=9)
    label(ax, 0.72, 0.52, "Wigner, outside,\nmust still describe\nthe whole room as\none unresolved system", color=INK, size=8.6, ha="center")
    label(ax, 0.50, 0.06, "There is no view from nowhere.", size=9.4, color=INK)
    return save(fig, path)


def fig12_pilot(path: Path):
    fig, ax = _fig(7.42, 4.32)
    title(ax, "Pilot-wave theory: one path taken, guided by all the others")
    x0, xb, xs = 0.08, 0.52, 0.92
    y0, y_up, y_lo = 0.48, 0.545, 0.42

    def wave(cx, cy, radii, x_lo, x_hi, y_lo_b, y_hi_b, lw=0.55, alpha=0.55):
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
                    ax.plot(x[sl], y[sl], color="#C8C8C8", lw=lw, alpha=alpha, zorder=1)

    wave(x0, y0, np.arange(0.06, 0.44, 0.045), x0, xb - 0.008, 0.16, 0.86)
    wave(xb, y_up, np.arange(0.05, 0.48, 0.045), xb + 0.008, xs - 0.006, 0.16, 0.86)
    wave(xb, y_lo, np.arange(0.05, 0.48, 0.045), xb + 0.008, xs - 0.006, 0.16, 0.86)
    ax.plot([x0, xb], [y0, y_lo], color="#BFBFBF", lw=1.05, zorder=3)
    for y_end in (0.455, 0.39, 0.33, 0.27, 0.205):
        ax.plot([xb, xs], [y_lo, y_end], color="#BFBFBF", lw=1.05, zorder=3)
    for y_end in (0.72, 0.655, 0.60):
        ax.plot([xb, xs], [y_up, y_end], color="#BFBFBF", lw=1.05, zorder=3)
    ax.plot([x0, xb], [y0, y_up], color=INK, lw=2.15, solid_capstyle="round", zorder=5)
    bx = np.linspace(xb, xs, 80)
    by = y_up + 0.055 * ((bx - xb) / (xs - xb)) ** 1.15
    ax.plot(bx, by, color=INK, lw=2.15, solid_capstyle="round", zorder=5)
    ax.plot(x0, y0, "o", color=INK, ms=6.2, zorder=6)
    ax.plot(xs, by[-1], "o", color=INK, ms=5.2, zorder=6)
    ax.plot([xb, xb], [0.575, 0.72], color=INK, lw=5.0, solid_capstyle="butt", zorder=7)
    ax.plot([xb, xb], [0.24, 0.385], color=INK, lw=5.0, solid_capstyle="butt", zorder=7)
    ax.plot([xs, xs], [0.18, 0.82], color=INK, lw=5.0, solid_capstyle="butt", zorder=7)
    label(ax, x0, 0.08, "source")
    label(ax, xs, 0.08, "screen")
    label(ax, 0.28, 0.78, "actual path (solid)", size=8.2, color=INK)
    label(ax, 0.28, 0.72, "empty paths (pale)", size=8.2)
    return save(fig, path)


def fig13_bell(path: Path):
    fig_w, fig_h = 7.42, 4.18
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=180)
    fig.patch.set_facecolor(PAPER)
    ax.set_xlim(0, fig_w)
    ax.set_ylim(0, fig_h)
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.set_facecolor(PAPER)
    ax.text(fig_w / 2, 3.90, "Bell / CHSH: measured correlations exceed the local ceiling", ha="center", va="center", fontsize=11.4, color=INK, fontname=FONT)
    ax.text(1.85, 3.28, "A number, not an interpretation", ha="center", va="center", fontsize=10.6, color=INK, fontname=FONT)
    ax.text(6.42, 3.28, "S", ha="center", va="center", fontsize=12.5, color=INK, fontname=FONT)
    for cx, lab in ((0.92, "a / a'"), (2.78, "b / b'")):
        ax.add_patch(plt.Circle((cx, 2.15), 0.42, fill=False, ec=INK, lw=1.4, zorder=4))
        ax.text(cx, 2.15, lab, ha="center", va="center", fontsize=9.4, color=INK, fontname=FONT)
        ax.text(cx, 1.48, "setting chosen\nafter separation", ha="center", va="top", fontsize=8.3, color=MUTED, fontname=FONT, linespacing=1.35)
    ax.plot([1.34, 2.36], [2.15, 2.15], ls=(0, (2.4, 2.6)), color=INK, lw=1.2, zorder=3)
    ax.plot(1.85, 2.15, marker="*", markersize=12, color=INK, zorder=5)
    ax.add_patch(plt.Rectangle((4.55, 0.92), 0.72, 1.18, facecolor="#B0B0B0", edgecolor=INK, lw=0.8, zorder=3))
    ax.add_patch(plt.Rectangle((5.85, 0.92), 0.72, 1.67, facecolor=DARK, edgecolor=INK, lw=0.8, zorder=3))
    ax.plot([4.38, 6.74], [0.92, 0.92], color=INK, lw=1.1, zorder=4)
    ax.text(4.91, 2.16, "2", ha="center", va="bottom", fontsize=10.2, color=INK, fontname=FONT)
    ax.text(6.21, 2.65, "2.83", ha="center", va="bottom", fontsize=10.2, color=INK, fontname=FONT)
    ax.text(4.91, 0.58, "local limit", ha="center", va="center", fontsize=8.7, color=MUTED, fontname=FONT)
    ax.text(6.21, 0.58, "quantum ceiling", ha="center", va="center", fontsize=8.7, color=MUTED, fontname=FONT)
    fig.subplots_adjust(left=0.03, right=0.97, top=0.96, bottom=0.05)
    return save(fig, path)


def fig14_mtheory(path: Path):
    fig, ax = _fig(5.6, 6.0)
    title(ax, "Five theories, seen from five sides", y=0.96)
    ax.add_patch(plt.Circle((0.50, 0.48), 0.11, facecolor=DARK, edgecolor=INK, lw=1.2, zorder=4))
    label(ax, 0.50, 0.48, "M-theory", color="#FFFFFF", size=9.2)
    names = [
        (0.50, 0.82, "Type I"),
        (0.16, 0.64, "Type IIA"),
        (0.16, 0.30, "Type IIB"),
        (0.84, 0.64, "Heterotic\nE8 x E8"),
        (0.84, 0.30, "Heterotic\nSO(32)"),
    ]
    for x, y, name in names:
        ax.plot([0.50, x], [0.48, y], color=LIGHT, lw=1.1, zorder=1)
        ax.add_patch(plt.Circle((x, y), 0.105, facecolor=PAPER, edgecolor=INK, lw=1.3, zorder=3))
        label(ax, x, y, name, color=INK, size=8.0)
    label(ax, 0.50, 0.08, "Same structure. Five limited views.", size=9.2, color=INK)
    return save(fig, path)


def fig15_holography(path: Path):
    fig, ax = _fig(5.6, 6.0)
    title(ax, "Holography: the boundary carries the account", y=0.94)
    ax.add_patch(plt.Circle((0.50, 0.46), 0.28, facecolor="#F0F0F0", edgecolor=INK, lw=2.0))
    th = np.linspace(0, 2 * np.pi, 36, endpoint=False)
    ax.plot(0.50 + 0.28 * np.cos(th), 0.46 + 0.28 * np.sin(th), "o", color=INK, ms=3.5)
    label(ax, 0.50, 0.50, "volume", color=INK, size=11)
    label(ax, 0.50, 0.42, "(the interior)", size=8.6)
    ax.annotate(
        "all of it, in principle,\nreadable on this edge",
        xy=(0.50 + 0.28 * np.cos(np.pi / 5), 0.46 + 0.28 * np.sin(np.pi / 5)),
        xytext=(0.78, 0.78),
        fontsize=8.6,
        color=INK,
        fontname=FONT,
        ha="left",
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.0),
    )
    return save(fig, path)


def fig16_recovery(path: Path):
    fig, ax = _fig(7.4, 3.2)
    title(ax, "Honest recovery: repaired, inferred, and named as gone", y=0.90, size=12)
    # 2x8 schematic: patterns not colour
    pattern = [
        "R", "R", "G", "I", "R", "R", "R", "R",
        "I", "R", "G", "R", "I", "R", "R", "G",
    ]
    x0, y1, y0, s, gap = 0.08, 0.58, 0.34, 0.08, 0.02
    for i, kind in enumerate(pattern):
        r, c = divmod(i, 8)
        x = x0 + c * (s + gap)
        y = y1 if r == 0 else y0
        if kind == "R":
            ax.add_patch(plt.Rectangle((x, y), s, s, facecolor=DARK, edgecolor=INK, lw=0.8))
        elif kind == "I":
            rec = plt.Rectangle((x, y), s, s, facecolor=PAPER, edgecolor=INK, lw=0.8)
            ax.add_patch(rec)
            # hatch via lines
            for k in range(1, 4):
                ax.plot([x + k * s / 4, x + k * s / 4], [y, y + s], color=INK, lw=0.6)
        else:
            ax.add_patch(plt.Rectangle((x, y), s, s, facecolor="#E6E6E6", edgecolor=INK, lw=0.8))
            ax.plot([x + 0.015, x + s - 0.015], [y + 0.015, y + s - 0.015], color=INK, lw=1.4)
            ax.plot([x + 0.015, x + s - 0.015], [y + s - 0.015, y + 0.015], color=INK, lw=1.4)
    label(ax, 0.18, 0.16, "solid = recovered", size=8.4, ha="left")
    label(ax, 0.46, 0.16, "hatched = inferred", size=8.4, ha="left")
    label(ax, 0.74, 0.16, "cross = named gone", size=8.4, ha="left")
    return save(fig, path)


def fig17_eras(path: Path):
    fig, ax = _fig(7.4, 3.6)
    title(ax, "The long future: an enormous middle, and then very little", y=0.90, size=12)
    ax.annotate("", xy=(0.96, 0.70), xytext=(0.04, 0.70), arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    label(ax, 0.08, 0.76, "now", size=8.2, ha="left")
    label(ax, 0.72, 0.76, "an unreasonably long time from now", size=8.2, ha="left")
    eras = [
        (0.06, "stelliferous\nera", "10^0 - 10^14 yr"),
        (0.28, "degenerate\nera", "10^14 - 10^37 yr"),
        (0.52, "black-hole\nera", "10^37 - 10^100 yr"),
        (0.76, "dark\nera", "beyond 10^100 yr"),
    ]
    grays = ["#222222", "#666666", "#A0A0A0", "#E0E0E0"]
    texts = ["#FFFFFF", "#FFFFFF", "#111111", "#111111"]
    for (x, name, years), g, tc in zip(eras, grays, texts):
        ax.add_patch(plt.Rectangle((x, 0.32), 0.20, 0.28, facecolor=g, edgecolor=INK, lw=1.1))
        ax.text(x + 0.10, 0.46, name, ha="center", va="center", fontsize=8.2, color=tc, fontname=FONT)
        label(ax, x + 0.10, 0.22, years, size=7.6)
    return save(fig, path)


FIGURES = [
    ("image1.png", fig1_superposition),
    ("image2.jpeg", fig2_basis),
    ("image3.png", fig3_which_path),
    ("image4.jpeg", fig4_zeno),
    ("image5.jpeg", fig5_evolution),
    ("image6.png", fig6_hawking),
    ("image7.jpeg", fig7_entanglement),
    ("image8.jpeg", fig8_noclone),
    ("image9.jpeg", fig9_uncertainty),
    ("image10.jpeg", fig10_decoherence),
    ("image11.jpeg", fig11_wigner),
    ("image12.png", fig12_pilot),
    ("image13.png", fig13_bell),
    ("image14.png", fig14_mtheory),
    ("image15.png", fig15_holography),
    ("image16.png", fig16_recovery),
    ("image17.png", fig17_eras),
]


def wt(text: str, bold=False, size=None, center=False, before=160, after=160) -> str:
    jc = "center" if center else "both"
    rpr = "<w:rPr><w:rFonts w:ascii='Amazon Ember' w:hAnsi='Amazon Ember'/>"
    if bold:
        rpr += "<w:b/><w:bCs/>"
    if size:
        rpr += f"<w:sz w:val='{size}'/><w:szCs w:val='{size}'/>"
    rpr += "</w:rPr>"
    # escape XML
    text = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return (
        f'<w:p><w:pPr><w:spacing w:before="{before}" w:after="{after}"/>'
        f'<w:jc w:val="{jc}"/></w:pPr><w:r>{rpr}<w:t xml:space="preserve">{text}</w:t></w:r></w:p>'
    )


BACK_COVER_PARAS = "".join(
    [
        wt("Somewhere in a government basement, there is a black hole. It has a filing number.", bold=True, size=28, center=True, before=240, after=240),
        wt(
            "The Ministry of Eventualities has been making reality simpler by pushing the difficult parts of it into a black hole in regional infrastructure. Lolly Wren, Transit Reconciliation Officer, Third Grade, is the person who notices."
        ),
        wt(
            "What follows is equal parts bureaucratic farce and a crash course in real quantum mechanics — taught not by lecture, but by a cast of thinly disguised, badly behaved geniuses, each convinced they alone know how reality actually works."
        ),
        wt(
            "For readers of Good Omens, The Hitchhiker's Guide to the Galaxy, and anyone who has ever suspected the paperwork was hiding something.",
            center=True,
            before=200,
            after=240,
        ),
        wt("Lolly Wren — Ten years in electronics. Eleven minutes as a working physicist. Promoted to Principal Officer, Relational Integrity — allegedly.", before=80, after=80),
        wt("Gideon Wigglesworth — Lolly's friend. Reads requisition forms for fun. Knows where the actual switch is. Collides with inanimate objects, regularly.", before=80, after=80),
        wt("Q.E.D. — Quentin Edmund Darling, allegedly. Lothar J. Musiol, obviously.", center=True, before=200, after=80),
        wt(
            "Book 1 of Lolly Wren's Curious Science Adventures — each volume stands alone, in a different Ministry, with a different piece of real physics hidden in the walls.",
            center=True,
            before=80,
            after=240,
        ),
    ]
)


def update_extents(xml: str, sizes: dict[str, tuple[int, int]]) -> str:
    """Set each drawing's EMU size from pixel aspect ratio. Max width 6.0 in."""
    max_cx = 5486400  # 6 inches

    def repl(match: re.Match) -> str:
        block = match.group(0)
        rid_m = re.search(r'r:embed="(rId\d+)"', block)
        if not rid_m:
            return block
        rid = rid_m.group(1)
        media = RID_TO_MEDIA.get(rid)
        if not media or media not in sizes:
            return block
        w, h = sizes[media]
        cx = max_cx
        cy = int(max_cx * (h / w))
        block = re.sub(r'<wp:extent cx="\d+" cy="\d+"/>', f'<wp:extent cx="{cx}" cy="{cy}"/>', block, count=1)
        block = re.sub(r'(<a:ext cx=")\d+(" cy=")\d+("/>)', rf"\g<1>{cx}\g<2>{cy}\g<3>", block, count=1)
        # alt text
        alt = ALTS.get(media, "")
        if alt:
            alt_xml = (
                alt.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
            )
            if 'descr="' in block:
                block = re.sub(r'descr="[^"]*"', f'descr="{alt_xml}"', block, count=1)
            else:
                block = block.replace("<wp:docPr ", f'<wp:docPr descr="{alt_xml}" ', 1)
        return block

    return re.sub(r"<w:drawing>.*?</w:drawing>", repl, xml, flags=re.DOTALL)


def patch_text(xml: str) -> str:
    xml = xml.replace(
        "→ and: Black-Hole Entropy and Holography",
        "→ Physics Notes (continued): Black-Hole Entropy and Holography",
    )
    old = (
        "The injunction itself was granted on the Tuesday, once the plan the Board "
        "had demanded on the Monday — as the price of losing the argument — was on "
        "the judge’s desk. He understood none of the physics and all of the paperwork, "
        "which turned out to be sufficient. "
    )
    new = (
        "The plan reached the judge the next morning. He understood none of the physics "
        "and all of the paperwork, which turned out to be sufficient. "
    )
    if old not in xml:
        # try ASCII apostrophe
        old_a = old.replace("’", "'")
        if old_a in xml:
            xml = xml.replace(old_a, new)
        else:
            print("WARNING: Chapter 16 opening not found exactly")
    else:
        xml = xml.replace(old, new, 1)
    return xml


def replace_back_cover(xml: str) -> str:
    # Replace the paragraph that embeds rId22 (image18) with live text.
    pattern = re.compile(
        r"<w:p[^>]*>(?:(?!<w:p[ >]).)*?r:embed=\"rId22\".*?</w:p>",
        re.DOTALL,
    )
    new_xml, n = pattern.subn(BACK_COVER_PARAS, xml, count=1)
    if n != 1:
        raise SystemExit(f"back-cover paragraph replace failed, n={n}")
    return new_xml


def drop_image18(rels: str) -> str:
    return re.sub(
        r'<Relationship Id="rId22" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image18.png"/>',
        "",
        rels,
    )


def main() -> None:
    if not DOCX.exists():
        raise SystemExit(f"missing {DOCX}")
    if not BACKUP.exists():
        shutil.copy2(DOCX, BACKUP)
        print("backup", BACKUP)

    ASSETS.mkdir(parents=True, exist_ok=True)
    sizes: dict[str, tuple[int, int]] = {}
    for name, fn in FIGURES:
        dest = ASSETS / name
        w, h = fn(dest)
        sizes[name] = (w, h)
        print(f"drew {name:14s} {w}x{h} {dest.stat().st_size // 1024} KB")

    tmp = Path(tempfile.mkdtemp(prefix="sp_fix_"))
    with zipfile.ZipFile(DOCX, "r") as zin:
        zin.extractall(tmp)

    media = tmp / "word" / "media"
    for name in sizes:
        shutil.copyfile(ASSETS / name, media / name)
    img18 = media / "image18.png"
    if img18.exists():
        img18.unlink()

    xml_path = tmp / "word" / "document.xml"
    rels_path = tmp / "word" / "_rels" / "document.xml.rels"
    xml = xml_path.read_text(encoding="utf-8")
    rels = rels_path.read_text(encoding="utf-8")
    xml = update_extents(xml, sizes)
    xml = patch_text(xml)
    xml = replace_back_cover(xml)
    rels = drop_image18(rels)
    xml_path.write_text(xml, encoding="utf-8")
    rels_path.write_text(rels, encoding="utf-8")

    out_tmp = DOCX.with_suffix(".docx.repack")
    if out_tmp.exists():
        out_tmp.unlink()
    with zipfile.ZipFile(out_tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for path in sorted(tmp.rglob("*")):
            if path.is_file():
                zout.write(path, path.relative_to(tmp).as_posix())
    try:
        DOCX.unlink()
    except PermissionError:
        shutil.rmtree(tmp, ignore_errors=True)
        raise SystemExit("Close the Word document and run again.")
    shutil.move(out_tmp, DOCX)
    shutil.rmtree(tmp, ignore_errors=True)
    print("updated", DOCX, "size_mb", round(DOCX.stat().st_size / 1e6, 2))


if __name__ == "__main__":
    main()
