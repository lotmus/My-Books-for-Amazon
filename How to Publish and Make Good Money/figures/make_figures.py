#!/usr/bin/env python3
"""Generates every illustration for "How to Publish and Make Good Money".

Single source of truth for the book's figures -- re-run this script to
regenerate all PNGs after any content or style change, rather than hand-
editing images with no source (matches this repo's existing convention of a
checked-in generator script, e.g. History/_generate.js).

Palette: the validated categorical/sequential/status palette from the
`dataviz` skill (light-mode instance), shared with nothing else in this
project so the whole book's charts and body-text accent color speak one
consistent color language.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Polygon, Circle, Rectangle
import numpy as np
import os

# ---------------------------------------------------------------------------
# Palette (light mode, dataviz skill reference instance)
# ---------------------------------------------------------------------------
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
CATEGORICAL = [BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED]

SEQ_BLUE = {
    100: "#cde2fb", 150: "#b7d3f6", 200: "#9ec5f4", 250: "#86b6ef",
    300: "#6da7ec", 350: "#5598e7", 400: "#3987e5", 450: "#2a78d6",
    500: "#256abf", 550: "#1c5cab", 600: "#184f95", 650: "#104281", 700: "#0d366b",
}

STATUS = {"good": "#0ca30c", "warning": "#fab219", "serious": "#ec835a", "critical": "#d03b3b"}

SURFACE = "#fcfcfb"
PAGE = "#f9f9f7"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "text.color": INK,
    "axes.edgecolor": BASELINE,
    "axes.labelcolor": INK_SECONDARY,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.titlesize": 15,
    "axes.titleweight": "bold",
    "font.size": 11,
})


def new_fig(w=10, h=6.2, surface=SURFACE):
    fig, ax = plt.subplots(figsize=(w, h), dpi=160)
    fig.patch.set_facecolor(PAGE)
    ax.set_facecolor(surface)
    return fig, ax


def clean_axes(ax, left=True, bottom=True):
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    if not left:
        ax.spines["left"].set_visible(False)
    if not bottom:
        ax.spines["bottom"].set_visible(False)
    for spine in ["left", "bottom"]:
        if ax.spines[spine].get_visible():
            ax.spines[spine].set_color(BASELINE)
            ax.spines[spine].set_linewidth(1.1)


def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print("wrote", path)


def draw_check(ax, x, y, s=0.09, color=STATUS["good"], lw=3.2):
    ax.plot([x - s, x - s * 0.25, x + s * 1.1], [y, y - s * 0.9, y + s * 0.9],
             color=color, lw=lw, solid_capstyle="round", solid_joinstyle="round",
             transform=ax.transAxes, clip_on=False)


def draw_x(ax, x, y, s=0.075, color=MUTED, lw=3.0):
    ax.plot([x - s, x + s], [y - s, y + s], color=color, lw=lw,
             solid_capstyle="round", transform=ax.transAxes, clip_on=False)
    ax.plot([x - s, x + s], [y + s, y - s], color=color, lw=lw,
             solid_capstyle="round", transform=ax.transAxes, clip_on=False)


def draw_warning(ax, x, y, s=0.11, color=STATUS["critical"]):
    tri = Polygon([[x, y + s], [x - s * 0.98, y - s * 0.85], [x + s * 0.98, y - s * 0.85]],
                  closed=True, facecolor=color, edgecolor="none",
                  transform=ax.transAxes, clip_on=False, zorder=5)
    ax.add_patch(tri)
    ax.text(x, y - s * 0.12, "!", transform=ax.transAxes, ha="center", va="center",
            color="white", fontsize=13, fontweight="bold", zorder=6)


# ---------------------------------------------------------------------------
# Cover
# ---------------------------------------------------------------------------
def fig_cover():
    fig, ax = plt.subplots(figsize=(10, 16), dpi=160)
    fig.patch.set_facecolor(BLUE)
    ax.set_xlim(0, 10); ax.set_ylim(0, 16)
    ax.axis("off")

    # Soft diagonal band for depth
    band = Polygon([[0, 0], [10, 3.6], [10, 0]], closed=True, facecolor="#184f95", edgecolor="none", zorder=1)
    ax.add_patch(band)
    band2 = Polygon([[0, 16], [0, 12.8], [10, 16]], closed=True, facecolor="#3987e5", edgecolor="none", zorder=1)
    ax.add_patch(band2)

    # Growth bars motif (categorical colors, ascending) sitting above the base band
    bar_colors = [ORANGE, YELLOW, AQUA, "#ffffff"]
    heights = [1.1, 1.7, 2.35, 3.1]
    xs = [2.0, 3.5, 5.0, 6.5]
    for x, h, c in zip(xs, heights, bar_colors):
        ax.add_patch(FancyBboxPatch((x, 2.9), 1.05, h, boxstyle="round,pad=0,rounding_size=0.12",
                                     facecolor=c, edgecolor="none", zorder=3))
    # small upward arrow over the bars (tip at top, shaft below)
    ax.add_patch(Polygon([[8.2, 6.3], [8.85, 4.9], [8.38, 4.9], [8.38, 2.9],
                           [8.02, 2.9], [8.02, 4.9], [7.55, 4.9]],
                          closed=True, facecolor="#ffffff", edgecolor="none", zorder=3, alpha=0.95))

    ax.text(5, 10.35, "HOW TO PUBLISH", transform=ax.transData, ha="center", va="center",
            color="white", fontsize=46, fontweight="bold", family="DejaVu Sans")
    ax.text(5, 9.35, "AND MAKE GOOD MONEY", transform=ax.transData, ha="center", va="center",
            color="white", fontsize=33, fontweight="bold", family="DejaVu Sans")

    ax.add_patch(Rectangle((3.6, 8.75), 2.8, 0.045, facecolor=YELLOW, edgecolor="none"))

    ax.text(5, 8.05, "A Straight, Show-Your-Work Guide to", transform=ax.transData,
            ha="center", va="center", color="#eaf1fb", fontsize=17)
    ax.text(5, 7.55, "Self-Publishing Profitable Books on Amazon", transform=ax.transData,
            ha="center", va="center", color="#eaf1fb", fontsize=17)

    ax.text(5, 1.55, "LOTHAR J. MUSIOL", transform=ax.transData, ha="center", va="center",
            color="white", fontsize=22, fontweight="bold", family="DejaVu Sans")

    save(fig, "cover.png")


# ---------------------------------------------------------------------------
# Figure 2.1 -- Royalty cliff
# ---------------------------------------------------------------------------
def fig_royalty_cliff():
    fig, ax = new_fig(10, 6.4)
    prices = np.linspace(0.99, 14.99, 300)
    delivery_fee = 0.18  # matches the ~1.2MB / $4.99 worked example in Chapter 2
    r35 = prices * 0.35
    band = (prices >= 2.99) & (prices <= 9.99)
    r70 = np.where(band, prices * 0.70 - delivery_fee, np.nan)

    ax.plot(prices, r35, color=ORANGE, lw=3, label="35% plan (any price)", zorder=3)
    ax.plot(prices, r70, color=BLUE, lw=3.4, label="70% plan ($2.99–$9.99 band)", zorder=4)

    for edge in (2.99, 9.99):
        ax.axvline(edge, color=BASELINE, lw=1.2, ls=(0, (4, 3)), zorder=1)
    ax.axvspan(2.99, 9.99, color=BLUE, alpha=0.06, zorder=0)

    # Worked-example marker at $4.99 -> $3.31 (Chapter 2)
    ax.scatter([4.99], [4.99 * 0.70 - delivery_fee], s=70, color=BLUE, zorder=5, edgecolor="white", linewidth=1.5)
    ax.annotate("$4.99 → $3.31 net\n(70% plan)", xy=(4.99, 4.99 * 0.70 - delivery_fee),
                xytext=(6.3, 2.15), color=INK, fontsize=10.5, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=1.1))

    ax.scatter([2.49], [2.49 * 0.35], s=70, color=ORANGE, zorder=5, edgecolor="white", linewidth=1.5)
    ax.annotate("$2.49 → $0.87 net\n(35% plan, below the band)", xy=(2.49, 2.49 * 0.35),
                xytext=(0.55, 3.55), color=INK, fontsize=10.5, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=1.1))

    ax.text(2.99, 0.32, " $2.99", color=INK_SECONDARY, fontsize=9.5, rotation=0)
    ax.text(9.99, 0.32, " $9.99", color=INK_SECONDARY, fontsize=9.5, rotation=0)

    ax.set_xlim(0, 15); ax.set_ylim(0, 8)
    ax.set_xlabel("List price (USD)"); ax.set_ylabel("Net royalty per copy (USD)")
    ax.set_title("The 70%/35% Royalty Cliff")
    ax.grid(axis="y", color=GRID, lw=0.9, zorder=0)
    ax.legend(frameon=False, loc="upper left", fontsize=10.5)
    clean_axes(ax)
    save(fig, "fig02_royalty_cliff.png")


# ---------------------------------------------------------------------------
# Figure 5.1 -- Ebook vs print needs
# ---------------------------------------------------------------------------
def fig_ebook_vs_print():
    fig, ax = plt.subplots(figsize=(10, 7.4), dpi=160)
    fig.patch.set_facecolor(PAGE)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.axis("off")

    col_w, gap = 4.55, 0.3
    left_x, right_x = 0.3, 0.3 + col_w + gap

    ax.add_patch(FancyBboxPatch((left_x, 0.4), col_w, 9.2, boxstyle="round,pad=0,rounding_size=0.18",
                                 facecolor="#eaf3fc", edgecolor=BLUE, linewidth=1.6))
    ax.add_patch(FancyBboxPatch((right_x, 0.4), col_w, 9.2, boxstyle="round,pad=0,rounding_size=0.18",
                                 facecolor="#fdece3", edgecolor=ORANGE, linewidth=1.6))

    ax.text(left_x + col_w / 2, 9.15, "EBOOK (KINDLE)", ha="center", fontsize=14.5, fontweight="bold", color=BLUE)
    ax.text(right_x + col_w / 2, 9.15, "PRINT (PAPERBACK/HARDCOVER)", ha="center", fontsize=11.8, fontweight="bold", color=ORANGE)

    ebook_rows = [
        ("Heading 1/2 styles for Kindle nav", True),
        ("Reflowable, device-width-safe images", True),
        ("Plain-text contents listing (optional)", True),
        ("Page-numbered table of contents", False),
        ("Index", False),
        ("Fixed page-number references", False),
    ]
    print_rows = [
        ("Page-numbered table of contents", True),
        ("Page numbers + running headers", True),
        ("Trim size & gutter-aware margins", True),
        ("Spine width from KDP's calculator", True),
        ("Bleed (only if art touches the edge)", True),
        ("Physical proof ordered & read", True),
    ]

    def render_rows(rows, col_x):
        y = 8.15
        for label, ok in rows:
            cx = col_x + 0.55
            if ok:
                ax.plot([cx - 0.16, cx - 0.02, cx + 0.22], [y, y - 0.16, y + 0.18],
                        color=STATUS["good"], lw=3.4, solid_capstyle="round", solid_joinstyle="round")
            else:
                ax.plot([cx - 0.16, cx + 0.16], [y - 0.16, y + 0.16], color=MUTED, lw=3.0, solid_capstyle="round")
                ax.plot([cx - 0.16, cx + 0.16], [y + 0.16, y - 0.16], color=MUTED, lw=3.0, solid_capstyle="round")
            ax.text(col_x + 1.0, y, label, fontsize=10, va="center", color=INK)
            y -= 1.28

    render_rows(ebook_rows, left_x)
    render_rows(print_rows, right_x)

    ax.set_title("What Each Format Needs — and What It Doesn't", fontsize=15, fontweight="bold", pad=14)
    save(fig, "fig05_ebook_vs_print.png")


# ---------------------------------------------------------------------------
# Figure 6.1 -- Thumbnail test
# ---------------------------------------------------------------------------
def _draw_sample_cover(ax, x0, y0, w, h, title_size, sub_size, name_size):
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=VIOLET, edgecolor="none"))
    ax.add_patch(Rectangle((x0, y0), w, h * 0.34, facecolor="#3a2f86", edgecolor="none"))
    # focal motif: a simple upward chevron
    cx = x0 + w * 0.5
    ax.add_patch(Polygon([[cx - w * 0.16, y0 + h * 0.16], [cx, y0 + h * 0.30], [cx + w * 0.16, y0 + h * 0.16],
                           [cx + w * 0.16, y0 + h * 0.10], [cx, y0 + h * 0.24], [cx - w * 0.16, y0 + h * 0.10]],
                          closed=True, facecolor=YELLOW, edgecolor="none"))
    ax.text(cx, y0 + h * 0.82, "MONEY", ha="center", va="center", color="white",
            fontsize=title_size, fontweight="bold", family="DejaVu Sans")
    ax.text(cx, y0 + h * 0.68, "MOVES", ha="center", va="center", color="white",
            fontsize=title_size, fontweight="bold", family="DejaVu Sans")
    ax.text(cx, y0 + h * 0.545, "a field guide", ha="center", va="center", color="#e9e4fb",
            fontsize=sub_size, style="italic")
    ax.text(cx, y0 + h * 0.045, "J. RIVERA", ha="center", va="center", color="white",
            fontsize=name_size, fontweight="bold")


def fig_thumbnail_test():
    fig, ax = plt.subplots(figsize=(10, 6.8), dpi=160)
    fig.patch.set_facecolor(PAGE)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.axis("off")

    _draw_sample_cover(ax, 0.6, 1.1, 3.6, 7.2, 21, 11, 11)
    ax.text(2.4, 8.75, "FULL SIZE", ha="center", fontsize=13, fontweight="bold", color=INK_SECONDARY)

    ax.annotate("", xy=(5.75, 4.9), xytext=(4.5, 4.9),
                arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=2))
    ax.text(5.1, 5.35, "shrink to\nactual size", ha="center", fontsize=9, color=MUTED)

    tx, ty, tw, th = 6.55, 3.1, 1.45, 2.9
    ax.text(tx + tw / 2, ty + th + 0.55, "ACTUAL THUMBNAIL", ha="center", fontsize=12.5,
            fontweight="bold", color=INK_SECONDARY)
    ax.text(tx + tw / 2, ty + th + 0.22, "(~150px wide)", ha="center", fontsize=10.5, color=INK_SECONDARY)
    _draw_sample_cover(ax, tx, ty, tw, th, 8.2, 4.4, 4.4)
    ax.add_patch(FancyBboxPatch((tx, ty), tw, th, boxstyle="round,pad=0.04,rounding_size=0.05",
                                 facecolor="none", edgecolor=STATUS["good"], linewidth=2.4))
    ax.text(tx + tw / 2, ty - 0.5, "still legible —", ha="center", fontsize=10,
            color=STATUS["good"], fontweight="bold")
    ax.text(tx + tw / 2, ty - 0.85, "title reads at a glance", ha="center", fontsize=10,
            color=STATUS["good"], fontweight="bold")

    ax.set_title("The Thumbnail Test", fontsize=16, fontweight="bold")
    save(fig, "fig06_thumbnail_test.png")


# ---------------------------------------------------------------------------
# Figure 7.1 -- Keyword funnel
# ---------------------------------------------------------------------------
def fig_keyword_funnel():
    fig, ax = plt.subplots(figsize=(9, 8.4), dpi=160)
    fig.patch.set_facecolor(PAGE)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.axis("off")

    stages = [
        ("Title & Subtitle Words", "auto-indexed by Amazon", SEQ_BLUE[250]),
        ("7 Backend Keyword Slots", "phrases the title doesn't cover", SEQ_BLUE[400]),
        ("Categories (3 + requested)", "the shelf a browser finds you on", SEQ_BLUE[600]),
        ("A Reader's Search", "the moment it all has to line up", "#0d366b"),
    ]
    n = len(stages)
    top_w, bot_w = 8.6, 3.4
    y_top, y_bot = 9.0, 1.4
    row_h = (y_top - y_bot) / n

    for i, (title, sub, color) in enumerate(stages):
        y1 = y_top - i * row_h
        y0 = y1 - row_h
        w1 = top_w - (top_w - bot_w) * (i / n)
        w0 = top_w - (top_w - bot_w) * ((i + 1) / n)
        x1a, x1b = 5 - w1 / 2, 5 + w1 / 2
        x0a, x0b = 5 - w0 / 2, 5 + w0 / 2
        text_color = "white" if i >= 1 else INK
        ax.add_patch(Polygon([[x1a, y1], [x1b, y1], [x0b, y0], [x0a, y0]], closed=True,
                              facecolor=color, edgecolor=PAGE, linewidth=2))
        ax.text(5, (y0 + y1) / 2 + 0.20, title, ha="center", va="center", fontsize=11.5,
                fontweight="bold", color=text_color)
        ax.text(5, (y0 + y1) / 2 - 0.38, sub, ha="center", va="center", fontsize=9,
                color=("#eef4fc" if i >= 1 else INK_SECONDARY))

    ax.set_title("The Keyword & Category Funnel", fontsize=15, fontweight="bold", pad=6)
    save(fig, "fig07_keyword_funnel.png")


# ---------------------------------------------------------------------------
# Figure 8.1 -- Pricing sweet spot (illustrative)
# ---------------------------------------------------------------------------
def fig_pricing_sweet_spot():
    fig, ax = new_fig(10, 6.2)
    price = np.linspace(0.99, 14.99, 300)
    # Illustrative hump: conversion falls roughly exponentially with price;
    # take-home = price * conversion. Shape-only, explicitly labeled as such.
    conversion = np.exp(-0.26 * (price - 0.99))
    takehome = price * conversion
    takehome = takehome / takehome.max()

    ax.plot(price, takehome, color=BLUE, lw=3.4, zorder=4)
    ax.fill_between(price, 0, takehome, color=BLUE, alpha=0.08, zorder=1)
    ax.axvspan(3.99, 6.99, color=AQUA, alpha=0.14, zorder=0)
    ax.text(5.49, 0.06, "sweet spot\n$3.99–$6.99", ha="center", color="#0d6b4a", fontsize=10.5, fontweight="bold")

    for edge in (2.99, 9.99):
        ax.axvline(edge, color=BASELINE, lw=1.1, ls=(0, (4, 3)))
    ax.text(2.99 + 0.2, 1.04, "$2.99", color=INK_SECONDARY, fontsize=9, ha="left")
    ax.text(9.99 + 0.2, 1.04, "$9.99", color=INK_SECONDARY, fontsize=9, ha="left")

    ax.set_xlim(0, 15); ax.set_ylim(0, 1.12)
    ax.set_xlabel("List price (USD)"); ax.set_ylabel("Relative take-home (illustrative index)")
    ax.set_title("Pricing Sweet Spot — ILLUSTRATIVE MODEL, not measured Amazon data")
    ax.grid(axis="y", color=GRID, lw=0.9, zorder=0)
    clean_axes(ax)
    save(fig, "fig08_pricing_sweet_spot.png")


# ---------------------------------------------------------------------------
# Figure 9.1 -- Launch concentration (illustrative)
# ---------------------------------------------------------------------------
def fig_launch_concentration():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.6), dpi=160, sharey=True)
    fig.patch.set_facecolor(PAGE)

    days_spread = np.arange(1, 31)
    spread = np.full(30, 10 / 30)
    axes[0].bar(days_spread, spread, color=ORANGE, width=0.8)
    axes[0].set_title("Spread Over 30 Days", fontsize=13, fontweight="bold", color=ORANGE)
    axes[0].set_xlabel("Day"); axes[0].set_ylabel("Units sold that day")

    days_conc = np.arange(1, 31)
    conc = np.zeros(30)
    conc[:7] = [3.0, 2.2, 1.6, 1.1, 0.8, 0.7, 0.6]
    axes[1].bar(days_conc, conc, color=BLUE, width=0.8)
    axes[1].set_title("Concentrated Launch Week", fontsize=13, fontweight="bold", color=BLUE)
    axes[1].set_xlabel("Day")

    for ax in axes:
        ax.set_facecolor(SURFACE)
        ax.grid(axis="y", color=GRID, lw=0.9, zorder=0)
        clean_axes(ax)
        ax.set_ylim(0, 3.4)

    fig.suptitle("Same 10 Units, Two Launch Shapes — ILLUSTRATIVE, qualitative effect only",
                 fontsize=14, fontweight="bold", y=1.02)
    save(fig, "fig09_launch_concentration.png")


# ---------------------------------------------------------------------------
# Figure 10.1 -- ACOS break-even
# ---------------------------------------------------------------------------
def fig_acos_breakeven():
    fig, ax = new_fig(10, 6.4)
    acos = np.linspace(0, 140, 300)
    breakeven = 66.3  # 3.31 / 4.99 * 100, matches Chapter 2/10 worked example
    profit_per_10 = 10 * (breakeven / acos.clip(min=1e-6) - 1)
    profit_per_10 = np.clip(profit_per_10, -10, 14)

    ax.axvspan(0, breakeven, color=STATUS["good"], alpha=0.10, zorder=0)
    ax.axvspan(breakeven, 140, color=STATUS["critical"], alpha=0.08, zorder=0)
    ax.plot(acos, profit_per_10, color=INK, lw=2.6, zorder=4)
    ax.axhline(0, color=BASELINE, lw=1.2)
    ax.axvline(breakeven, color=MUTED, lw=1.3, ls=(0, (4, 3)))

    ax.text(12, 12.6, "PROFITABLE", color=STATUS["good"], fontsize=13, fontweight="bold")
    ax.text(95, 12.6, "LOSING MONEY", color=STATUS["critical"], fontsize=13, fontweight="bold")
    ax.text(breakeven + 2, -9.2, f"break-even ACOS ≈ {breakeven:.0f}%", color=INK, fontsize=10.5, fontweight="bold")

    ax.scatter([101], [10 * (breakeven / 101 - 1)], s=70, color=STATUS["critical"], zorder=5, edgecolor="white", linewidth=1.4)
    ax.annotate("$10 spend → 3 sales\n(101% ACOS)", xy=(101, 10 * (breakeven / 101 - 1)),
                xytext=(103, -3.0), fontsize=9.5, color=INK, fontweight="bold")
    ax.scatter([60], [10 * (breakeven / 60 - 1)], s=70, color=STATUS["good"], zorder=5, edgecolor="white", linewidth=1.4)
    ax.annotate("$10 spend → 5 sales\n(60% ACOS)", xy=(60, 10 * (breakeven / 60 - 1)),
                xytext=(15, 6.0), fontsize=9.5, color=INK, fontweight="bold")

    ax.set_xlim(0, 140); ax.set_ylim(-10, 14)
    ax.set_xlabel("ACOS (%) — ad spend ÷ ad-attributed sales")
    ax.set_ylabel("Profit per $10 ad spend (USD)")
    ax.set_title("Break-Even ACOS, $4.99 Ebook Example")
    ax.grid(axis="y", color=GRID, lw=0.9, zorder=0)
    clean_axes(ax)
    save(fig, "fig10_acos_breakeven.png")


# ---------------------------------------------------------------------------
# Figure 12.1 -- Select vs Wide
# ---------------------------------------------------------------------------
def fig_select_vs_wide():
    fig, ax = plt.subplots(figsize=(10, 7.2), dpi=160)
    fig.patch.set_facecolor(PAGE)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.axis("off")

    col_w, gap = 4.55, 0.3
    left_x, right_x = 0.3, 0.3 + col_w + gap
    ax.add_patch(FancyBboxPatch((left_x, 0.4), col_w, 9.2, boxstyle="round,pad=0,rounding_size=0.18",
                                 facecolor="#eaf3fc", edgecolor=BLUE, linewidth=1.6))
    ax.add_patch(FancyBboxPatch((right_x, 0.4), col_w, 9.2, boxstyle="round,pad=0,rounding_size=0.18",
                                 facecolor="#fdece3", edgecolor=ORANGE, linewidth=1.6))
    ax.text(left_x + col_w / 2, 9.15, "KDP SELECT", ha="center", fontsize=15.5, fontweight="bold", color=BLUE)
    ax.text(right_x + col_w / 2, 9.15, "GOING WIDE", ha="center", fontsize=15.5, fontweight="bold", color=ORANGE)

    select_rows = ["90-day rolling ebook exclusivity", "Kindle Unlimited page-read income",
                   "Free Book Promotion days", "Print editions unaffected either way"]
    wide_rows = ["Apple, Kobo, B&N, Google, libraries", "No single platform's algorithm risk",
                 "No Kindle Unlimited page-read income", "Aggregator takes a small cut (optional)"]

    def render(rows, col_x):
        y = 8.0
        for label in rows:
            ax.add_patch(Circle((col_x + 0.5, y), 0.07, facecolor=INK_SECONDARY, edgecolor="none"))
            ax.text(col_x + 0.85, y, label, fontsize=10.3, va="center", color=INK)
            y -= 1.55

    render(select_rows, left_x)
    render(wide_rows, right_x)

    ax.set_title("Exclusivity vs. Reach", fontsize=16, fontweight="bold", pad=10)
    save(fig, "fig12_select_vs_wide.png")


# ---------------------------------------------------------------------------
# Figure 13.1 -- Red flags
# ---------------------------------------------------------------------------
def fig_red_flags():
    fig, ax = plt.subplots(figsize=(10, 8), dpi=160)
    fig.patch.set_facecolor(PAGE)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.axis("off")

    flags = [
        "Unsolicited “we love your manuscript” contact",
        "An upfront fee for something KDP gives free",
        "Guaranteed bestseller or ranking promises",
        "Pressure to sign or pay quickly",
        "Paid, swapped, or incentivized reviews",
        "Mass AI-flooded, minimally reviewed volume",
        "Stock images with no commercial license",
    ]
    y = 9.0
    for f in flags:
        ax.add_patch(Rectangle((0.4, y - 0.42), 9.2, 0.86, facecolor="#fbe9e7",
                                edgecolor=STATUS["critical"], linewidth=0, zorder=1))
        ax.add_patch(Rectangle((0.4, y - 0.42), 0.12, 0.86, facecolor=STATUS["critical"], edgecolor="none", zorder=2))
        draw_warning(ax, 0.10, y / 10, s=0.026)
        ax.text(1.9, y, f, fontsize=12, va="center", color=INK, zorder=2)
        y -= 1.18

    ax.set_title("Red Flags: When “Publishing Help” Is a Trap", fontsize=15.5, fontweight="bold", pad=8)
    save(fig, "fig13_red_flags.png")


# ---------------------------------------------------------------------------
# Figure 14.1 -- Catalog compounding (illustrative)
# ---------------------------------------------------------------------------
def fig_catalog_compounding():
    fig, ax = new_fig(10, 6.4)
    months = np.arange(0, 25)
    books_launch = [0, 6, 12, 17, 21]
    colors = [BLUE, ORANGE, AQUA, YELLOW, MAGENTA]
    layers = []
    for launch in books_launch:
        base = np.where(months >= launch, 1 - np.exp(-(months - launch) / 5.0), 0)
        layers.append(np.clip(base, 0, None))
    layers = np.array(layers)

    ax.stackplot(months, layers, colors=colors, alpha=0.92,
                 labels=[f"Book {i+1}" for i in range(len(books_launch))])
    total = layers.sum(axis=0)
    ax.plot(months, total, color=INK, lw=2.0, ls=(0, (1, 1)), alpha=0.55)

    for i, launch in enumerate(books_launch):
        ax.axvline(launch, color=PAGE, lw=1)
        ax.text(launch + 0.3, layers.sum(axis=0).max() * 1.02 - i * 0.001, "", fontsize=1)

    ax.set_xlim(0, 24); ax.set_ylim(0, layers.sum(axis=0).max() * 1.15)
    ax.set_xlabel("Months since first launch"); ax.set_ylabel("Cumulative catalog income (illustrative index)")
    ax.set_title("From One Book to a Catalog — ILLUSTRATIVE MODEL, not a disclosed statistic")
    ax.legend(loc="upper left", frameon=False, fontsize=9.5, ncol=2)
    ax.grid(axis="y", color=GRID, lw=0.9, zorder=0)
    clean_axes(ax)
    save(fig, "fig14_catalog_compounding.png")


# ---------------------------------------------------------------------------
# Figure 15.1 -- First-year roadmap (Gantt-style)
# ---------------------------------------------------------------------------
def fig_first_year_roadmap():
    fig, ax = new_fig(10.8, 5.8)
    phases = [
        ("Write & Research", 1, 2, BLUE),
        ("Revise, Design, Recruit", 3, 3, ORANGE),
        ("Format, List, Launch", 4, 4, AQUA),
        ("Read Data & Run Ads", 5, 6, YELLOW),
        ("Next Book & List-Building", 7, 12, MAGENTA),
    ]
    n = len(phases)
    for i, (label, start, end, color) in enumerate(phases):
        y = n - 1 - i
        width = end - start + 1
        ax.barh(y, width, left=start - 1, height=0.58, color=color, zorder=3,
                edgecolor=PAGE, linewidth=1.5)

    ax.set_xlim(0, 12)
    ax.set_ylim(-0.65, n - 0.35)
    ax.set_yticks(range(n))
    ax.set_yticklabels([p[0] for p in phases][::-1], fontsize=12, fontweight="bold", color=INK)
    ax.set_xticks([i + 0.5 for i in range(12)])
    ax.set_xticklabels([f"M{i+1}" for i in range(12)], fontsize=9.5)
    ax.tick_params(axis="y", length=0)
    ax.set_title("A Default First-Year Shape")
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    clean_axes(ax, left=False)
    save(fig, "fig15_first_year_roadmap.png")


if __name__ == "__main__":
    fig_cover()
    fig_royalty_cliff()
    fig_ebook_vs_print()
    fig_thumbnail_test()
    fig_keyword_funnel()
    fig_pricing_sweet_spot()
    fig_launch_concentration()
    fig_acos_breakeven()
    fig_select_vs_wide()
    fig_red_flags()
    fig_catalog_compounding()
    fig_first_year_roadmap()
    print("done")
