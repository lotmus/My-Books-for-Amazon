"""Draw the line-art diagram figures for 'The Copy Is Never Exact' as clean,
labeled PNGs using matplotlib. Photographic figures are handled separately
(fetch_photos.py) or left as framed placeholders by build_docx.py.
Run: python draw_figs.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle, Rectangle, Wedge
import numpy as np

HERE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")  # book root/figures
FIGS = os.path.join(HERE, "figs")
os.makedirs(FIGS, exist_ok=True)

INK = "#1a1a1a"
GREY = "#555555"
LIGHT = "#e8e8e8"
A_COL = "#c0392b"   # A - red
T_COL = "#2980b9"   # T - blue
G_COL = "#27ae60"   # G - green
C_COL = "#8e44ad"   # C - purple

plt.rcParams["font.family"] = "DejaVu Sans"


def new_fig(w=6, h=4.5):
    fig, ax = plt.subplots(figsize=(w, h), dpi=200)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    return fig, ax


def save(fig, n):
    path = os.path.join(FIGS, f"fig{n:02d}.png")
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", path)


def label(ax, x, y, text, size=10, weight="normal", color=INK, ha="center", va="center", **kw):
    ax.text(x, y, text, fontsize=size, weight=weight, color=color, ha=ha, va=va, **kw)


# ---------- fig02: X-shaped diffraction pattern ----------
def fig02():
    fig, ax = new_fig(5, 5)
    ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)
    ax.add_patch(Rectangle((-2.5, -2.5), 5, 5, facecolor="black"))
    rng = np.random.default_rng(7)
    for arm_sign in (1, -1):
        for i in range(1, 9):
            r = i * 0.26
            for s in (1, -1):
                x = s * r * 0.55
                y = arm_sign * r
                ax.add_patch(Circle((x, y), 0.05 + 0.01 * (9 - i), color="white"))
    ax.add_patch(Circle((0, 0), 0.09, color="white"))
    for yy in (-2.1, 2.1):
        ax.add_patch(Rectangle((-2.3, yy - 0.08), 4.6, 0.16, color="white", alpha=0.55))
    label(ax, 0, -2.35, "Figure 2. X-shaped diffraction pattern of a helix", size=8, color="white")
    save(fig, 2)


# ---------- fig03: the ladder A-T, G-C ----------
def fig03():
    fig, ax = new_fig(6, 5)
    rails_x = [1.2, 4.8]
    y0, y1 = 0.6, 4.2
    for rx in rails_x:
        ax.plot([rx, rx], [y0, y1], color=INK, lw=4)
    rungs = [("A", "T", A_COL, T_COL, 2), ("G", "C", G_COL, C_COL, 3),
             ("T", "A", T_COL, A_COL, 2), ("C", "G", C_COL, G_COL, 3),
             ("G", "C", G_COL, C_COL, 3)]
    ys = np.linspace(y1 - 0.3, y0 + 0.3, len(rungs))
    for (b1, b2, c1, c2, bonds), y in zip(rungs, ys):
        ax.plot([rails_x[0], rails_x[1]], [y, y], color=GREY, lw=1.2, ls=(0, (1, 1)))
        ax.add_patch(Circle((rails_x[0] + 0.35, y), 0.28, color=c1))
        ax.add_patch(Circle((rails_x[1] - 0.35, y), 0.28, color=c2))
        label(ax, rails_x[0] + 0.35, y, b1, color="white", weight="bold")
        label(ax, rails_x[1] - 0.35, y, b2, color="white", weight="bold")
        label(ax, 3.0, y + 0.32, f"{bonds} H-bonds", size=7, color=GREY)
    label(ax, 3.0, 4.5, "The ladder: A with T, G with C", size=11, weight="bold")
    label(ax, 1.2, 0.35, "backbone", size=8, color=GREY)
    label(ax, 4.8, 0.35, "backbone", size=8, color=GREY)
    save(fig, 3)


# ---------- fig05: a nucleotide and the four bases ----------
def fig05():
    fig, ax = new_fig(6, 4.5)
    # nucleotide schematic: phosphate - sugar - base
    ax.add_patch(Circle((1.0, 3.4), 0.35, facecolor=LIGHT, edgecolor=INK))
    label(ax, 1.0, 3.4, "P", weight="bold")
    ax.add_patch(mpatches.RegularPolygon((2.1, 3.4), 5, radius=0.42, facecolor="#f5e6c8", edgecolor=INK))
    label(ax, 2.1, 3.4, "sugar", size=7)
    ax.plot([1.35, 1.75], [3.4, 3.4], color=INK, lw=2)
    ax.plot([2.5, 3.0], [3.4, 3.4], color=INK, lw=2)
    ax.add_patch(FancyBboxPatch((3.0, 3.05), 1.6, 0.7, boxstyle="round,pad=0.02", facecolor=A_COL, edgecolor=INK))
    label(ax, 3.8, 3.4, "base", color="white", weight="bold")
    label(ax, 2.1, 2.55, "nucleotide = phosphate + sugar + base", size=8, color=GREY)

    bases = [("A", A_COL, "adenine"), ("T", T_COL, "thymine"), ("G", G_COL, "guanine"), ("C", C_COL, "cytosine")]
    for i, (letter, col, name) in enumerate(bases):
        x = 0.9 + i * 1.35
        ax.add_patch(Circle((x, 1.3), 0.45, color=col))
        label(ax, x, 1.3, letter, color="white", weight="bold", size=14)
        label(ax, x, 0.6, name, size=8)
    label(ax, 3.0, 4.15, "A nucleotide, and the four bases", size=11, weight="bold")
    save(fig, 5)


# ---------- fig06: protein folding ----------
def fig06():
    fig, ax = new_fig(6, 4.5)
    # unfolded chain
    xs = np.linspace(0.6, 5.4, 14)
    ys = 3.6 + 0.15 * np.sin(np.linspace(0, 6, 14))
    ax.plot(xs, ys, color=GREY, lw=2)
    for x, y in zip(xs, ys):
        ax.add_patch(Circle((x, y), 0.09, color=INK))
    label(ax, 3.0, 4.05, "unfolded chain of amino acids", size=8, color=GREY)
    ax.annotate("", xy=(3.0, 2.55), xytext=(3.0, 3.1),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.5))
    label(ax, 3.5, 2.85, "folds", size=8, style="italic")
    # folded blob
    t = np.linspace(0, 2 * np.pi, 200)
    r = 0.9 + 0.12 * np.sin(5 * t) + 0.06 * np.cos(3 * t)
    bx = 3.0 + r * np.cos(t)
    by = 1.4 + r * np.sin(t) * 0.8
    ax.fill(bx, by, color="#f5cba7", edgecolor=INK, lw=1.5)
    ax.add_patch(Wedge((3.0, 1.4), 0.35, 0, 360, facecolor="white", edgecolor=INK))
    label(ax, 3.0, 1.4, "active\nsite", size=6.5)
    label(ax, 3.0, 0.35, "folded protein: the shape is the function", size=8, color=GREY)
    label(ax, 3.0, 4.35, "A chain folds into a working shape", size=11, weight="bold")
    save(fig, 6)


# ---------- fig07: replication fork ----------
def fig07():
    fig, ax = new_fig(6.5, 4.5)
    ax.plot([0.6, 3.2], [3.6, 3.6], color=T_COL, lw=3)
    ax.plot([0.6, 3.2], [1.2, 1.2], color=T_COL, lw=3)
    ax.plot([3.2, 5.8], [3.9, 2.4], color=A_COL, lw=3)
    ax.plot([3.2, 5.8], [0.9, 2.4], color=A_COL, lw=3)
    ax.add_patch(mpatches.Ellipse((3.2, 2.4), 0.55, 1.9, angle=0, facecolor="none", edgecolor=INK, lw=2))
    label(ax, 3.2, 2.4, "helicase", size=7, rotation=90)
    ax.plot([3.5, 5.7], [3.75, 2.55], color=GREY, lw=1.5, ls="--")
    label(ax, 4.7, 3.5, "leading strand\n(continuous)", size=7.5, color=GREY)
    for i, xx in enumerate(np.linspace(3.5, 5.5, 4)):
        yy = 0.95 + 0.05 * i
        ax.plot([xx, xx + 0.35], [yy, yy + 0.35], color=GREY, lw=1.5, ls="--")
    label(ax, 4.7, 0.55, "lagging strand\n(Okazaki fragments)", size=7.5, color=GREY)
    label(ax, 1.9, 3.95, "parent strand", size=7.5, color=GREY)
    label(ax, 1.9, 0.85, "parent strand", size=7.5, color=GREY)
    label(ax, 3.25, 4.3, "A replication fork", size=11, weight="bold")
    save(fig, 7)


# ---------- fig08: codon table (simplified grid) ----------
def fig08():
    fig, ax = new_fig(6.5, 5.5)
    bases = ["U", "C", "A", "G"]
    codon_aa = {
        "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met*",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
        "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
        "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
        "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
        "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
        "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    }
    cell = 1.4
    x0, y0 = 0.6, 0.6
    for i, b1 in enumerate(bases):
        for j, b2 in enumerate(bases):
            x = x0 + j * cell
            y = y0 + (3 - i) * cell
            ax.add_patch(Rectangle((x, y), cell, cell, facecolor="white", edgecolor=GREY, lw=0.8))
            for k, b3 in enumerate(bases):
                codon = b1 + b2 + b3
                aa = codon_aa[codon]
                col = "#eeeeee" if aa == "Stop" else ("#fde3d0" if "*" in aa else "white")
                sx = x + 0.05 + (k % 2) * 0.65
                sy = y + 0.95 - (k // 2) * 0.5
                label(ax, sx, sy, f"{codon}\n{aa}", size=5.4)
            label(ax, x + 0.08, y + cell - 0.12, b1 + b2, size=6.5, weight="bold", color=GREY, ha="left")
    label(ax, x0 + 2 * cell, y0 + 4 * cell + 0.35, "The codon table (first two letters as rows/cols)",
          size=10, weight="bold")
    save(fig, 8)


# ---------- fig09: genome budget bar ----------
def fig09():
    fig, ax = new_fig(6.5, 4)
    segs = [("protein-coding", 1.5, A_COL), ("introns / gene-associated", 23.5, "#e67e22"),
            ("repeats / transposons", 45, G_COL), ("regulatory & other", 30, GREY)]
    x = 0.6
    total_w = 5.4
    for name, pct, col in segs:
        w = total_w * pct / 100
        ax.add_patch(Rectangle((x, 2.0), w, 1.0, facecolor=col, edgecolor="white"))
        if w > 0.5:
            label(ax, x + w / 2, 2.5, f"{pct:.1f}%", color="white", size=8, weight="bold")
        label(ax, x + w / 2, 1.55, name, size=7, rotation=0)
        x += w
    label(ax, 3.3, 3.4, "The genome's budget", size=11, weight="bold")
    save(fig, 9)


# ---------- fig10: proton tunnelling tautomer ----------
def fig10():
    fig, ax = new_fig(6.5, 4.5)
    for i, (title, shift) in enumerate([("ordinary pair", 0.0), ("tautomeric pair", 1.0)]):
        cx = 1.8 + i * 3.2
        ax.add_patch(Circle((cx - 0.7, 2.4), 0.4, color=G_COL))
        label(ax, cx - 0.7, 2.4, "G", color="white", weight="bold")
        ax.add_patch(Circle((cx + 0.7, 2.4), 0.4, color=C_COL))
        label(ax, cx + 0.7, 2.4, "C", color="white", weight="bold")
        hx = cx - 0.15 + shift * 0.3
        ax.plot([cx - 0.3, cx + 0.3], [2.4, 2.4], color=GREY, lw=1, ls=":")
        ax.add_patch(Circle((hx, 2.4), 0.08, color="#f39c12"))
        label(ax, cx, 1.7, title, size=8)
        if i == 0:
            ax.annotate("", xy=(3.9, 2.4), xytext=(2.9, 2.4),
                        arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2))
            label(ax, 3.4, 2.75, "proton\nhops", size=6.5)
    label(ax, 3.3, 3.5, "A proton hopping across a hydrogen bond", size=10.5, weight="bold")
    save(fig, 10)


# ---------- fig11: meiosis with crossover ----------
def fig11():
    fig, ax = new_fig(6.5, 4.5)
    for i, (y, col) in enumerate([(3.3, A_COL), (2.7, T_COL)]):
        ax.plot([0.8, 2.6], [y, y], color=col, lw=4)
    ax.plot([0.8, 1.6], [3.3, 3.3], color=A_COL, lw=4)
    ax.plot([1.6, 2.6], [3.3, 2.7], color=T_COL, lw=4)
    ax.plot([0.8, 1.6], [2.7, 2.7], color=T_COL, lw=4)
    ax.plot([1.6, 2.6], [2.7, 3.3], color=A_COL, lw=4)
    ax.add_patch(Circle((1.6, 3.0), 0.08, color=INK))
    label(ax, 1.7, 1.9, "crossover point", size=7.5)
    ax.annotate("", xy=(4.8, 3.0), xytext=(3.0, 3.0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
    label(ax, 3.9, 3.25, "meiosis", size=8, style="italic")
    for i, y in enumerate([3.9, 3.5, 3.1, 2.7, 2.3]):
        pass
    outs = [("mat/pat", 3.9), ("mixed A", 3.5), ("mixed B", 3.1), ("pat/mat", 2.7)]
    for label_txt, y in outs:
        colA = A_COL if "mat" == label_txt[:3] or label_txt == "mixed A" else T_COL
        colB = T_COL if "mat" == label_txt[:3] else A_COL
        ax.plot([5.0, 5.5], [y, y], color=colA, lw=3)
        ax.plot([5.5, 6.0], [y, y], color=colB, lw=3)
    label(ax, 5.5, 4.25, "four recombined chromatids", size=7.5)
    label(ax, 3.3, 4.35, "Meiosis with one crossover", size=10.5, weight="bold")
    save(fig, 11)


# ---------- fig12: pedigree of X-linked trait ----------
def fig12():
    fig, ax = new_fig(6.5, 5)
    def square(x, y, filled):
        ax.add_patch(Rectangle((x - 0.2, y - 0.2), 0.4, 0.4, facecolor=(INK if filled else "white"), edgecolor=INK))
    def circle(x, y, filled):
        ax.add_patch(Circle((x, y), 0.22, facecolor=(INK if filled else "white"), edgecolor=INK))
    gen1 = [(1.5, 4.2, "circle", False, True), (3.0, 4.2, "square", False, False)]
    for x, y, shape, filled, carrier in gen1:
        (circle if shape == "circle" else square)(x, y, filled)
        if carrier:
            ax.add_patch(Circle((x, y), 0.08, facecolor="white", edgecolor=INK))
    ax.plot([1.5, 3.0], [4.2, 4.2], color=INK, lw=1)
    gen2 = [(1.0, 3.0, "square", True), (2.0, 3.0, "circle", False), (3.0, 3.0, "square", False), (4.0, 3.0, "circle", False)]
    ax.plot([2.25, 2.25], [4.2, 3.35], color=INK, lw=1)
    for x, y, shape, filled in gen2:
        (circle if shape == "circle" else square)(x, y, filled)
        ax.plot([x, 2.25], [y + 0.3, 3.35], color=INK, lw=0.8)
    gen3 = [(1.5, 1.8, "square", True), (3.5, 1.8, "square", False)]
    ax.plot([1.0, 2.0], [3.0, 3.0], color=INK, lw=1)
    ax.plot([3.0, 4.0], [3.0, 3.0], color=INK, lw=1)
    for x, y, shape, filled in gen3:
        (circle if shape == "circle" else square)(x, y, filled)
    ax.plot([1.5, 2.0], [1.8, 2.8], color=INK, lw=0.8)
    ax.plot([3.5, 4.0], [1.8, 2.8], color=INK, lw=0.8)
    label(ax, 3.3, 0.9, "filled = affected   square = male   circle = female", size=7.5, color=GREY)
    label(ax, 2.5, 4.7, "Pedigree of an X-linked recessive trait", size=10.5, weight="bold")
    save(fig, 12)


# ---------- fig13: Punnett square + bell curve ----------
def fig13():
    fig, ax = new_fig(6.5, 4.5)
    x0, y0, cell = 0.6, 2.0, 0.7
    alleles = ["F", "f"]
    for i, a in enumerate(alleles):
        label(ax, x0 + cell * (i + 1.5), y0 + 2 * cell + 0.3, a, weight="bold")
        label(ax, x0 + 0.3, y0 + cell * (1.5 - i), a, weight="bold")
    combos = [["FF", "Ff"], ["Ff", "ff"]]
    for i in range(2):
        for j in range(2):
            x = x0 + cell * (j + 1)
            y = y0 + cell * (1 - i)
            col = A_COL if "ff" != combos[i][j] else LIGHT
            ax.add_patch(Rectangle((x, y), cell, cell, facecolor=col if combos[i][j] != "ff" else LIGHT,
                                    edgecolor=INK, alpha=0.5))
            label(ax, x + cell / 2, y + cell / 2, combos[i][j])
    label(ax, x0 + cell * 2, y0 - 0.4, "one gene: a Punnett square", size=8, color=GREY)

    ax2 = fig.add_axes([0.58, 0.15, 0.38, 0.6])
    xs = np.linspace(-3, 3, 200)
    ys = np.exp(-xs**2 / 2)
    ax2.plot(xs, ys, color=T_COL, lw=2)
    ax2.fill_between(xs, ys, color=T_COL, alpha=0.15)
    ax2.axis("off")
    ax2.text(0, -0.15, "many genes: a bell curve", fontsize=8, color=GREY, ha="center")
    label(ax, 3.3, 4.3, "One gene versus many", size=10.5, weight="bold")
    save(fig, 13)


# ---------- fig16: two-generation cross with counts ----------
def fig16():
    fig, ax = new_fig(6.5, 4.5)
    ax.add_patch(Circle((1.5, 3.6), 0.4, color=G_COL))
    label(ax, 1.5, 3.6, "RR", color="white", weight="bold")
    ax.add_patch(Circle((4.5, 3.6), 0.4, color="#a5d6a7"))
    label(ax, 4.5, 3.6, "rr", weight="bold")
    label(ax, 3.0, 3.9, "×", size=14)
    ax.annotate("", xy=(3.0, 2.7), xytext=(3.0, 3.2), arrowprops=dict(arrowstyle="-|>", color=INK))
    ax.add_patch(Circle((3.0, 2.2), 0.4, color=G_COL))
    label(ax, 3.0, 2.2, "Rr", color="white", weight="bold")
    label(ax, 3.0, 1.6, "all round (F1 hybrids)", size=8, color=GREY)
    ax.annotate("self-fertilise", xy=(3.0, 1.0), xytext=(3.0, 1.35), ha="center",
                arrowprops=dict(arrowstyle="-|>", color=INK), fontsize=7.5)
    xs = [1.2, 2.4, 3.6, 4.8]
    labs = ["RR\nround", "Rr\nround", "Rr\nround", "rr\nwrinkled"]
    cols = [G_COL, G_COL, G_COL, "#a5d6a7"]
    for x, l, c in zip(xs, labs, cols):
        ax.add_patch(Circle((x, 0.25), 0.32, color=c))
        label(ax, x, 0.25, "", size=1)
        ax.text(x, -0.35, l, fontsize=7, ha="center")
    label(ax, 3.0, 4.3, "5,474 round to 1,850 wrinkled: about 3 to 1", size=9.5, weight="bold")
    ax.set_ylim(-0.8, 4.6)
    save(fig, 16)


# ---------- fig20: plasmid cut and pasted ----------
def fig20():
    fig, ax = new_fig(6.5, 4.8)
    t = np.linspace(0.15, 2 * np.pi - 0.15, 100)
    r = 1.3
    cx, cy = 2.0, 2.6
    ax.plot(cx + r * np.cos(t), cy + r * np.sin(t), color=G_COL, lw=3)
    label(ax, cx, cy, "plasmid", size=8, color=GREY)
    x0, y0 = cx + r, cy
    label(ax, x0 + 0.3, y0, "cut here\n(restriction site)", size=6.5, ha="left")
    ax.add_patch(FancyBboxPatch((4.3, 2.3), 1.6, 0.6, boxstyle="round,pad=0.05", facecolor=A_COL, edgecolor=INK))
    label(ax, 5.1, 2.6, "foreign gene", color="white", size=8)
    ax.annotate("", xy=(3.3, 2.6), xytext=(4.3, 2.6), arrowprops=dict(arrowstyle="<|-", color=INK, lw=1.4))
    label(ax, 3.0, 4.3, "A plasmid cut and pasted", size=10.5, weight="bold")
    save(fig, 20)


# ---------- fig21: sequencing gel ladder ----------
def fig21():
    fig, ax = new_fig(5.5, 5.5)
    rng = np.random.default_rng(3)
    lanes = ["A", "C", "G", "T"]
    colors = [A_COL, C_COL, G_COL, T_COL]
    for i, (lane, col) in enumerate(zip(lanes, colors)):
        x = 1.0 + i * 1.0
        label(ax, x, 4.9, lane, weight="bold", color=col)
        n_bands = rng.integers(6, 10)
        ys = sorted(rng.uniform(0.5, 4.5, n_bands))
        for y in ys:
            ax.add_patch(Rectangle((x - 0.35, y - 0.04), 0.7, 0.08, color=INK))
    label(ax, 2.5, 5.2, "Read bottom to top for the sequence", size=8, color=GREY)
    save(fig, 21)


# ---------- fig22: PCR doubling cascade ----------
def fig22():
    fig, ax = new_fig(6.5, 4.5)
    counts = [1, 2, 4, 8]
    for i, n in enumerate(counts):
        x = 0.9 + i * 1.5
        for j in range(n):
            yy = 2.3 + (j - (n - 1) / 2) * 0.35
            ax.plot([x - 0.3, x + 0.3], [yy, yy], color=T_COL, lw=2)
        label(ax, x, 0.6, f"cycle {i}\n{n} copies", size=7.5)
        if i < 3:
            ax.annotate("", xy=(x + 0.75, 2.3), xytext=(x + 0.45, 2.3),
                        arrowprops=dict(arrowstyle="-|>", color=INK))
    label(ax, 5.6, 0.6, "...\ncycle 30\n~1 billion", size=7.5)
    label(ax, 3.3, 4.1, "The doubling cascade of PCR", size=10.5, weight="bold")
    save(fig, 22)


# ---------- fig23: STR profile peaks ----------
def fig23():
    fig, ax = new_fig(6.5, 4)
    rng = np.random.default_rng(11)
    positions = sorted(rng.uniform(0.5, 6.0, 6))
    for row, (y0, col, label_txt) in enumerate([(2.6, T_COL, "sample A"), (0.8, A_COL, "sample B")]):
        for x in positions:
            h = rng.uniform(0.5, 1.1)
            ax.plot([x, x], [y0, y0 + h], color=col, lw=2.5)
        label(ax, 0.3, y0 + 0.5, label_txt, size=8, ha="right")
    label(ax, 3.3, 3.85, "Same peaks, same positions: a match", size=10, weight="bold")
    save(fig, 23)


# ---------- fig24: cost per genome log curve ----------
def fig24():
    fig, ax = new_fig(6.5, 4.5)
    years = [2001, 2003, 2007, 2010, 2014, 2020, 2025]
    cost = [95_000_000, 50_000_000, 1_000_000, 30_000, 1000, 600, 200]
    ax2 = fig.add_axes([0.15, 0.15, 0.75, 0.7])
    ax2.plot(years, cost, marker="o", color=A_COL, lw=2)
    ax2.set_yscale("log")
    ax2.set_ylabel("US dollars per genome (log scale)", fontsize=8)
    ax2.tick_params(labelsize=8)
    ax2.spines[["top", "right"]].set_visible(False)
    ax2.set_title("Cost per human genome, 2001-2025", fontsize=10, weight="bold")
    save(fig, 24)


# ---------- fig25: Cas9 guided by RNA ----------
def fig25():
    fig, ax = new_fig(6, 4.8)
    ax.plot([0.8, 5.2], [2.6, 2.6], color=T_COL, lw=3)
    ax.plot([0.8, 5.2], [2.3, 2.3], color=A_COL, lw=3)
    ax.add_patch(mpatches.Ellipse((3.0, 2.9), 1.6, 1.4, facecolor="#f5cba7", edgecolor=INK, alpha=0.85))
    label(ax, 3.0, 3.5, "Cas9", weight="bold")
    ax.plot([2.6, 3.4], [2.45, 2.45], color="#e67e22", lw=3)
    label(ax, 3.0, 2.05, "guide RNA pairs the target", size=7.5, color=GREY)
    ax.annotate("", xy=(2.6, 2.45), xytext=(2.6, 2.9), arrowprops=dict(arrowstyle="-", color=INK, lw=0.8))
    ax.annotate("", xy=(3.4, 2.45), xytext=(3.4, 2.9), arrowprops=dict(arrowstyle="-", color=INK, lw=0.8))
    label(ax, 4.4, 2.9, "cut site", size=7.5)
    ax.plot([2.75, 2.75], [2.15, 2.75], color=INK, lw=1, ls=":")
    ax.plot([3.25, 3.25], [2.15, 2.75], color=INK, lw=1, ls=":")
    label(ax, 3.0, 4.2, "Cas9 guided to a target by RNA", size=10.5, weight="bold")
    save(fig, 25)


# ---------- fig27: designed protein next to sequence ----------
def fig27():
    fig, ax = new_fig(6.5, 4.5)
    seq = "MK VLA TG..."
    label(ax, 1.6, 3.7, seq, size=11, family="monospace")
    label(ax, 1.6, 3.2, "amino-acid sequence", size=7.5, color=GREY)
    ax.annotate("", xy=(3.4, 2.4), xytext=(2.6, 3.4), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
    t = np.linspace(0, 2 * np.pi, 150)
    r = 0.9 + 0.15 * np.sin(4 * t)
    bx = 4.6 + r * np.cos(t)
    by = 2.0 + r * np.sin(t) * 0.75
    ax.fill(bx, by, color="#aed6f1", edgecolor=INK, lw=1.5)
    label(ax, 4.6, 2.0, "predicted\nfold", size=8)
    label(ax, 3.3, 4.2, "A designed protein next to its sequence", size=10, weight="bold")
    save(fig, 27)


# ---------- fig37: chromosome ideogram ----------
def fig37():
    fig, ax = new_fig(4, 6)
    ax.add_patch(FancyBboxPatch((1.2, 0.6), 1.6, 4.8, boxstyle="round,pad=0.1", facecolor=LIGHT, edgecolor=INK, lw=1.5))
    ax.add_patch(Circle((2.0, 3.0), 0.35, facecolor="white", edgecolor=INK, lw=1.5))
    rng = np.random.default_rng(5)
    for y in np.arange(0.9, 5.2, 0.35):
        if abs(y - 3.0) < 0.4:
            continue
        ax.add_patch(Rectangle((1.2, y), 1.6, 0.12, facecolor=rng.choice(["#bdbdbd", "#9e9e9e"])))
    for y0, y1 in [(0.9, 1.15), (4.9, 5.15)]:
        ax.add_patch(Rectangle((1.2, y0), 1.6, y1 - y0, facecolor="#e67e22", alpha=0.7))
    label(ax, 2.0, 0.7, "telomere-to-telomere\nregions finished after 2003", size=7.5, color=GREY)
    label(ax, 2.0, 5.7, "A finished chromosome", size=10.5, weight="bold")
    save(fig, 37)


# ---------- fig38: Manhattan plot sketch ----------
def fig38():
    fig, ax = new_fig(6.5, 4)
    rng = np.random.default_rng(9)
    n_chr = 10
    x_off = 0
    colors = [GREY, "#999999"]
    for c in range(n_chr):
        n = rng.integers(40, 80)
        x = x_off + np.arange(n) * 0.02
        y = -np.log10(rng.uniform(1e-4, 1, n))
        ax.scatter(x, y, s=3, color=colors[c % 2])
        x_off += n * 0.02 + 0.1
    hit_x = x_off * 0.42
    ax.scatter([hit_x], [7.2], s=30, color=A_COL, zorder=5)
    label(ax, hit_x, 7.6, "genome-wide\nsignificant hit", size=7, color=A_COL)
    ax.axhline(5.0, color=T_COL, lw=1, ls="--")
    ax.set_ylim(0, 8.5)
    ax.set_xlim(-0.2, x_off + 0.2)
    ax.set_xticks([])
    ax.set_ylabel("-log10(p)", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("A Manhattan plot, sketched", fontsize=10.5, weight="bold")
    save(fig, 38)


# ---------- fig40: risk vs penetrance ----------
def fig40():
    fig, ax = new_fig(6.5, 4.5)
    ax2 = fig.add_axes([0.18, 0.18, 0.7, 0.65])
    xs = np.linspace(0, 1, 100)
    ax2.plot(xs, xs, color=GREY, lw=1, ls="--")
    pts = [("Huntington's\n(CAG repeat)", 0.98, 0.97, A_COL),
           ("BRCA1", 0.65, 0.6, "#e67e22"),
           ("APOE e4\n(one copy)", 0.3, 0.28, T_COL),
           ("common SNP", 0.05, 0.06, G_COL)]
    for name, x, y, col in pts:
        ax2.scatter([x], [y], color=col, s=60, zorder=5)
        ax2.annotate(name, (x, y), textcoords="offset points", xytext=(8, 5), fontsize=7)
    ax2.set_xlabel("how strongly the variant acts", fontsize=8)
    ax2.set_ylabel("penetrance (chance of disease)", fontsize=8)
    ax2.set_xlim(0, 1.1); ax2.set_ylim(0, 1.1)
    ax2.spines[["top", "right"]].set_visible(False)
    ax2.tick_params(labelsize=7)
    ax2.set_title("Risk against penetrance", fontsize=10.5, weight="bold")
    save(fig, 40)


# ---------- fig41: two overlapping bell curves ----------
def fig41():
    fig, ax = new_fig(6.5, 4)
    ax2 = fig.add_axes([0.12, 0.2, 0.76, 0.6])
    xs = np.linspace(-4, 6, 300)
    y1 = np.exp(-xs**2 / 4.5)
    y2 = np.exp(-(xs - 1.2)**2 / 4.5)
    ax2.plot(xs, y1, color=T_COL, lw=2, label="low polygenic score")
    ax2.fill_between(xs, y1, color=T_COL, alpha=0.15)
    ax2.plot(xs, y2, color=A_COL, lw=2, label="high polygenic score")
    ax2.fill_between(xs, y2, color=A_COL, alpha=0.15)
    ax2.legend(fontsize=7, frameon=False)
    ax2.axis("off")
    ax2.set_title("A shifted average, a weak individual prediction", fontsize=10, weight="bold")
    save(fig, 41)


# ---------- fig43: ex vivo vs in vivo editing ----------
def fig43():
    fig, ax = new_fig(6.5, 4.5)
    label(ax, 1.6, 4.0, "Ex vivo", weight="bold", size=10)
    steps = ["remove cells", "edit in dish", "infuse back"]
    for i, s in enumerate(steps):
        y = 3.3 - i * 0.7
        ax.add_patch(FancyBboxPatch((0.6, y - 0.22), 2.0, 0.44, boxstyle="round,pad=0.03",
                                     facecolor="#aed6f1", edgecolor=INK))
        label(ax, 1.6, y, s, size=8)
        if i < 2:
            ax.annotate("", xy=(1.6, y - 0.55), xytext=(1.6, y - 0.25),
                        arrowprops=dict(arrowstyle="-|>", color=INK))
    label(ax, 4.9, 4.0, "In vivo", weight="bold", size=10)
    steps2 = ["package editor", "inject patient", "editor finds tissue"]
    for i, s in enumerate(steps2):
        y = 3.3 - i * 0.7
        ax.add_patch(FancyBboxPatch((3.9, y - 0.22), 2.0, 0.44, boxstyle="round,pad=0.03",
                                     facecolor="#f5cba7", edgecolor=INK))
        label(ax, 4.9, y, s, size=8)
        if i < 2:
            ax.annotate("", xy=(4.9, y - 0.55), xytext=(4.9, y - 0.25),
                        arrowprops=dict(arrowstyle="-|>", color=INK))
    label(ax, 3.3, 4.35, "Two editing routes", size=11, weight="bold")
    save(fig, 43)


# ---------- fig44: embryo-selection decision tree ----------
def fig44():
    fig, ax = new_fig(6.5, 5)
    label(ax, 3.3, 4.5, "embryos created", size=9, weight="bold")
    ax.add_patch(FancyBboxPatch((2.5, 4.15), 1.6, 0.4, boxstyle="round,pad=0.03", facecolor=LIGHT, edgecolor=INK))
    branches = [("test for one\nknown mutation\n(PGT-M)", 1.3, 3.0),
                ("polygenic risk\nscoring", 3.3, 3.0),
                ("no testing", 5.3, 3.0)]
    for name, x, y in branches:
        ax.annotate("", xy=(x, y + 0.3), xytext=(3.3, 4.15), arrowprops=dict(arrowstyle="-", color=GREY))
        ax.add_patch(FancyBboxPatch((x - 0.8, y - 0.25), 1.6, 0.55, boxstyle="round,pad=0.03",
                                     facecolor="#d5f5e3", edgecolor=INK))
        label(ax, x, y, name, size=7.5)
    label(ax, 3.3, 1.9, "each branch: which embryo is transferred, and why", size=7.5, color=GREY)
    label(ax, 3.3, 4.9, "An embryo-selection decision tree", size=10.5, weight="bold")
    save(fig, 44)


ALL = [fig02, fig03, fig05, fig06, fig07, fig08, fig09, fig10, fig11, fig12,
       fig13, fig16, fig20, fig21, fig22, fig23, fig24, fig25, fig27, fig37,
       fig38, fig40, fig41, fig43, fig44]

if __name__ == "__main__":
    for f in ALL:
        f()
    print(f"\nDone: {len(ALL)} diagrams drawn.")
