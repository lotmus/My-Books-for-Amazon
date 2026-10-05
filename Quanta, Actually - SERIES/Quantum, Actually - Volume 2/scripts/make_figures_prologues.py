# -*- coding: utf-8 -*-
"""Arrow diagrams and experiment sketches for Prologues 1-9."""
import math
import numpy as np
import matplotlib.patches as mp
from figlib import *
from make_figures_lessons import loop_vx, loop_se, loop_vp

FIGS = {}


def fig(name):
    def deco(f):
        FIGS[name] = f
        return f
    return deco


def box(ax, x, y, w, h, text="", fc="#EAF2F8", ec=BLUE, fs=8.5):
    ax.add_patch(mp.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", fc=fc, ec=ec, lw=1.1))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs)


def lamp(ax, x, y, s=0.18):
    ax.add_patch(Circle((x, y), s, fc="#FFE9A8", ec=INK, lw=1.1, zorder=4))
    for k in range(8):
        t = k * math.pi / 4
        ax.plot([x + 1.3 * s * math.cos(t), x + 1.7 * s * math.cos(t)], [y + 1.3 * s * math.sin(t), y + 1.7 * s * math.sin(t)], color=INK, lw=0.8)


def detector(ax, x, y, lab, w=0.32, h=0.26):
    ax.add_patch(mp.Rectangle((x - w / 2, y - h / 2), w, h, fc="#DDDDDD", ec=INK, lw=1.1, zorder=4))
    ax.text(x, y, lab, ha="center", va="center", fontsize=9, zorder=5)


# ---------------------------------------------------------------- Prologue 1
@fig("P1_clicks.png")
def _():
    fig, ax = new(6.0, 1.9)
    rng = np.random.default_rng(3)
    for row, (rate, name) in enumerate([(60, "brighter source"), (14, "dimmer source")]):
        y = 1.0 - row * 0.8
        ax.plot([0, 5], [y, y], color=GREY, lw=0.8)
        ts = np.sort(rng.uniform(0, 5, rate))
        for t in ts:
            ax.plot([t, t], [y, y + 0.35], color=INK, lw=1.3)
        ax.text(-0.1, y + 0.15, name, ha="right", va="center", fontsize=9)
    ax.text(5.05, 0.2, "time →", fontsize=8.5, va="center")
    ax.text(2.5, -0.05, "every click is the same height", ha="center", fontsize=8.5, color=BLUE)
    frame(ax, -1.6, 5.6, -0.2, 1.5); return fig


@fig("P1_stopwatch.png")
def _():
    fig, ax = new(6.2, 2.4)
    lamp(ax, 0, 0.6); ax.text(0, 0.15, "source", ha="center", fontsize=8.5)
    detector(ax, 5.6, 0.6, "D")
    ax.plot([0.3, 5.4], [0.6, 0.6], color=INK, lw=1.0, ls="--")
    arrow(ax, 2.6, 0.75, 3.2, 0.75, color=BLUE, lw=1.0, head=8)
    ax.text(2.9, 0.88, "photon travels", ha="center", fontsize=8, color=BLUE)
    for i, (x, ang) in enumerate([(0.9, 0), (2.3, 130), (3.7, 260), (5.0, 35)]):
        stopwatch(ax, x, 1.55, 0.33, ang, label=["start", "", "", "arrives"][i])
    ax.annotate("", xy=(5.6, 1.15), xytext=(5.2, 1.4), arrowprops=dict(arrowstyle="->", color=GREY))
    polar_arrow(ax, 6.4, 0.25, 0.7, 90 - 35, color=BLUE, lw=2.4)
    ax.text(6.55, 1.05, "arrow for\nthis way", fontsize=8.5, color=BLUE)
    frame(ax, -0.4, 7.4, -0.1, 2.1); return fig


@fig("P1_add.png")
def _():
    fig, ax = new(6.4, 2.2)
    L = 0.9
    cases = [(0, "same direction", "length 0.4,  P = 0.16"), (90, "right angle", "length ≈ 0.28,  P = 0.08"), (180, "opposite", "length 0,  P = 0")]
    for i, (ang, t, r) in enumerate(cases):
        x0 = i * 2.3
        p = arrow(ax, x0, 0.4, x0 + L, 0.4, lw=2.2)
        q = polar_arrow(ax, p[0], p[1], L, ang, lw=2.2, color=GREY if ang else INK)
        if ang != 180:
            arrow(ax, x0, 0.4 - 0.08 if ang == 0 else 0.4, q[0], (q[1] - 0.08) if ang == 0 else q[1], color=BLUE, lw=1.6, ls="-")
        else:
            ax.plot([x0], [0.4], "o", color=BLUE, ms=5)
        ax.text(x0 + 0.9, -0.15, t, ha="center", fontsize=9)
        ax.text(x0 + 0.9, -0.45, r, ha="center", fontsize=8.5, color=BLUE)
    ax.text(0, 1.55, "Each arrow has length 0.2. Black and grey: the two ways. Blue: the final arrow.", fontsize=8.5)
    frame(ax, -0.2, 6.6, -0.6, 1.7); return fig


# ---------------------------------------------------------------- Prologue 2
def glass_block(ax, x, y, w, h):
    ax.add_patch(mp.Rectangle((x, y), w, h, fc="#DCEBF5", ec=INK, lw=1.1))


@fig("P2_one_surface.png")
def _():
    fig, ax = new(5.8, 2.6)
    glass_block(ax, 2.2, -0.6, 2.4, 2.4)
    ax.text(3.4, -0.4, "thick glass (back surface blackened)", ha="center", fontsize=8)
    lamp(ax, 0, 1.4)
    arrow(ax, 0.25, 1.3, 2.18, 0.65, lw=1.4)
    arrow(ax, 2.2, 0.62, 0.6, 0.0, lw=1.2, color=GREY)
    arrow(ax, 2.22, 0.62, 3.9, 0.15, lw=1.2, color=GREY)
    detector(ax, 0.45, -0.1, "A"); detector(ax, 4.05, 0.1, "B")
    ax.text(0.45, -0.5, "4 in 100", ha="center", fontsize=9, color=BLUE); ax.text(4.05, 0.55, "96 in 100", ha="center", fontsize=9, color=BLUE)
    frame(ax, -0.5, 5.0, -0.7, 1.9); return fig


@fig("P2_thickness.png")
def _():
    fig, ax = plt.subplots(figsize=(5.8, 2.6))
    d = np.linspace(0, 700, 600)
    P = 0.08 * (1 - np.cos(4 * math.pi * 1.5 * d / 650))
    ax.plot(d, 100 * P, color=INK, lw=1.8)
    ax.axhline(8, color=GREY, ls="--", lw=1); ax.text(705, 8, "8 %  (\"4 % per surface\")", va="center", fontsize=8.5, color=GREY)
    ax.set_xlabel("thickness of the glass sheet (nanometres)"); ax.set_ylabel("reflected (%)")
    ax.set_ylim(0, 17.5); ax.set_xlim(0, 700)
    return fig


@fig("P2_two_surfaces.png")
def _():
    fig, ax = new(6.4, 2.6)
    glass_block(ax, 2.0, -0.7, 0.55, 2.6)
    lamp(ax, 0, 1.5)
    arrow(ax, 0.22, 1.42, 1.98, 0.75, lw=1.4)
    arrow(ax, 2.0, 0.75, 0.55, 0.12, lw=1.2, color=INK)
    ax.plot([2.0, 2.55], [0.75, 0.55], color=GREY, lw=1.2); arrow(ax, 2.55, 0.55, 2.0, 0.35, color=GREY, lw=1.2)
    arrow(ax, 2.0, 0.35, 0.6, -0.15, color=GREY, lw=1.2, ls="--")
    detector(ax, 0.42, -0.05, "A")
    ax.text(1.0, 0.65, "front", fontsize=8, ); ax.text(2.6, 0.75, "back", fontsize=8)
    # arrows
    o = (4.2, 0.6)
    polar_arrow(ax, o[0], o[1], 0.9, 180, lw=2.2, ls="--")
    ax.text(o[0] - 0.5, o[1] + 0.2, "front, reversed", fontsize=8, ha="center")
    p = (o[0] - 0.9, o[1])
    q = polar_arrow(ax, p[0], p[1], 0.9, 50, lw=2.2, color=GREY)
    ax.text(q[0] + 0.1, q[1], "back", fontsize=8)
    arrow(ax, o[0], o[1], q[0], q[1], color=BLUE, lw=1.8)
    ax.text(o[0] + 0.05, o[1] + 0.55, "final", color=BLUE, fontsize=8.5)
    frame(ax, -0.4, 5.6, -0.8, 1.9); return fig


@fig("P2_cycle.png")
def _():
    fig, ax = new(6.4, 1.9)
    for i, extra in enumerate([0, 60, 120, 180, 240, 300]):
        x0 = i * 1.1 + 0.6
        L = 0.42
        tip = polar_arrow(ax, x0, 0.4, L, 180, lw=1.8, ls="--")
        q = polar_arrow(ax, tip[0], tip[1], L, extra, lw=1.8, color=GREY)
        if extra % 360:
            arrow(ax, x0, 0.4, q[0], q[1], color=BLUE, lw=1.5)
        else:
            ax.plot([x0], [0.4], "o", color=BLUE, ms=4)
        P = 0.08 * (1 - math.cos(math.radians(extra)))
        ax.text(x0 - 0.2, -0.25, "%d°" % extra, ha="center", fontsize=8.5)
        ax.text(x0 - 0.2, -0.55, "P = %.2f" % P, ha="center", fontsize=8.5, color=BLUE)
    ax.text(-0.1, 1.05, "extra turn of the back arrow as the sheet thickens:", fontsize=8.5)
    frame(ax, -0.2, 6.6, -0.7, 1.2); return fig


@fig("P2_soap.png")
def _():
    fig, ax = plt.subplots(figsize=(5.6, 2.4))
    lam = np.linspace(400, 700, 400)
    r2 = ((1 - 1.33) / (1 + 1.33)) ** 2
    phi = 4 * math.pi * 1.33 * 400 / lam
    P = 2 * r2 * (1 - np.cos(phi))
    import matplotlib.cm as cm
    for i in range(len(lam) - 1):
        ax.fill_between(lam[i:i + 2], 0, 100 * P[i:i + 2], color=cm.nipy_spectral((lam[i] - 380) / 360 * 0.9 + 0.05), lw=0)
    ax.plot(lam, 100 * P, color=INK, lw=1.4)
    ax.set_xlabel("wavelength of the light (nm):  violet 400 … red 700"); ax.set_ylabel("reflected (%)")
    ax.set_xlim(400, 700); ax.set_ylim(0, 9)
    return fig


# ---------------------------------------------------------------- Prologue 3
def mirror_geometry(N=25):
    S, P = (-2.0, 1.6), (2.0, 1.6)
    xs = np.linspace(-3.0, 3.0, N)
    T = np.hypot(xs - S[0], S[1]) + np.hypot(xs - P[0], P[1])
    return S, P, xs, T


@fig("P3_mirror.png")
def _():
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(3, 1, figsize=(6.0, 5.6), gridspec_kw=dict(height_ratios=[1.3, 1.0, 1.0]))
    S, P, xs, T = mirror_geometry(13)
    ax = axs[0]; ax.set_aspect("equal"); ax.axis("off")
    ax.plot([-3.2, 3.2], [0, 0], color=INK, lw=3)
    for x in xs:
        ax.plot([S[0], x, P[0]], [S[1], 0, P[1]], color=GREY, lw=0.6)
    ax.plot([S[0], 0, P[0]], [S[1], 0, P[1]], color=BLUE, lw=1.6)
    ax.plot([0, 0], [0.6, 2.0], color=INK, lw=3); ax.text(0.1, 2.0, "screen", fontsize=8)
    ax.plot(*S, "o", color=INK); ax.text(S[0] - 0.15, S[1] + 0.15, "S", fontsize=10)
    ax.plot(*P, "s", color=INK); ax.text(P[0] + 0.1, P[1] + 0.15, "P", fontsize=10)
    ax.text(-3.2, -0.35, "mirror", fontsize=8)
    ax.set_xlim(-3.4, 3.4); ax.set_ylim(-0.5, 2.3)
    ax = axs[1]
    S, P, xs2, T2 = mirror_geometry(200)
    ax.plot(xs2, T2, color=INK, lw=1.6); ax.set_ylabel("travel time"); ax.set_xticks([]); ax.set_yticks([])
    ax.text(-3.0, T2.max() * 0.97, "long, changing fast", fontsize=8); ax.text(-0.9, T2.min() * 1.03, "shortest, flat", fontsize=8, color=BLUE)
    ax.set_xlim(-3.4, 3.4)
    ax = axs[2]; ax.set_aspect("equal"); ax.axis("off")
    S, P, xs, T = mirror_geometry(13)
    k = 2 * math.pi / 0.45
    for x, t in zip(xs, T):
        ang = -k * (t - T.min()) + math.pi / 2
        arrow(ax, x, 0, x + 0.4 * math.cos(ang), 0.4 * math.sin(ang), lw=1.6, color=BLUE if abs(x) < 0.8 else INK, head=9)
    ax.set_xlim(-3.4, 3.4); ax.set_ylim(-0.55, 0.55)
    ax.text(-3.3, -0.62, "one arrow per strip of mirror (directions from the stopwatch)", fontsize=8)
    fig.tight_layout()
    return fig


@fig("P3_mirror_sum.png")
def _():
    fig, ax = new(4.8, 3.6)
    S, P, xs, T = mirror_geometry(400)
    k = 2 * math.pi / 0.45
    z = 0j
    pts = [z]
    for t in T:
        z += 0.02 * np.exp(-1j * k * (t - T.min()))
        pts.append(z)
    pts = np.array(pts)
    mid = (np.abs(xs) < 0.8)
    ax.plot(pts.real, pts.imag, color=INK, lw=1.1)
    idx = np.where(mid)[0]
    ax.plot(pts.real[idx[0]:idx[-1] + 1], pts.imag[idx[0]:idx[-1] + 1], color=BLUE, lw=2.6)
    arrow(ax, pts[0].real, pts[0].imag, pts[-1].real, pts[-1].imag, color=BLUE, lw=1.4, ls="--")
    ax.text(pts[-1].real, pts[-1].imag - 0.12, "end of mirror", fontsize=8, ha="center", va="top")
    ax.text(pts[0].real, pts[0].imag + 0.12, "start of mirror", fontsize=8, ha="center")
    ax.text(pts[idx[len(idx) // 2]].real + 0.15, pts[idx[len(idx) // 2]].imag, "middle strips", fontsize=8.5, color=BLUE)
    return fig


@fig("P3_grating.png")
def _():
    fig, ax = new(6.2, 2.4)
    angs = np.arange(0, 12) * 50.0
    for panel, keep in enumerate([lambda a: True, lambda a: math.cos(math.radians(a)) > 0]):
        x0 = panel * 3.2
        z = complex(x0, 0.6)
        ax.plot([x0 + 0.1, x0 + 2.7], [-0.3, -0.3], color=INK, lw=3)
        for i, a in enumerate(angs):
            xm = x0 + 0.15 + i * 0.21
            if not keep(a):
                ax.add_patch(mp.Rectangle((xm - 0.09, -0.36), 0.18, 0.12, fc="white", ec="white", zorder=5))
                continue
            dz = 0.32 * complex(math.cos(math.radians(a)), math.sin(math.radians(a)))
            arrow(ax, z.real, z.imag, (z + dz).real, (z + dz).imag, lw=1.4, head=8)
            z += dz
        start = complex(x0, 0.6)
        if abs(z - start) > 0.05:
            arrow(ax, start.real, start.imag, z.real, z.imag, color=BLUE, lw=1.6, ls="--")
        ax.text(x0 + 1.3, -0.45, ["plain mirror end:\narrows curl, little left", "every other zone removed:\nthe rest add up"][panel], ha="center", va="top", fontsize=8.5)
    frame(ax, -0.3, 6.3, -1.05, 1.9); return fig


@fig("P3_lens.png")
def _():
    fig, ax = new(6.2, 2.6)
    S, P = (0.0, 0.0), (6.0, 0.0)
    ax.plot(*S, "o", color=INK); ax.text(-0.2, 0.15, "S", fontsize=10)
    ax.plot(*P, "s", color=INK); ax.text(6.1, 0.15, "P", fontsize=10)
    y = np.linspace(-1.0, 1.0, 100)
    th = 0.38 * (1 - y ** 2)
    ax.fill_betweenx(y, 3.0 - th, 3.0 + th, color="#DCEBF5", ec=INK, lw=1.1)
    for yy in np.linspace(-0.9, 0.9, 7):
        ax.plot([S[0], 3.0, P[0]], [S[1], yy, P[1]], color=GREY, lw=0.8)
    ax.plot([S[0], P[0]], [0, 0], color=BLUE, lw=1.2)
    ax.text(3.0, 1.15, "more glass where the path is short", ha="center", fontsize=8.5)
    for i, yy in enumerate(np.linspace(-0.9, 0.9, 7)):
        arrow(ax, 6.5 + 0.0, 0.9 - i * 0.3, 6.5 + 0.35, 0.9 - i * 0.3, lw=1.3, head=7, color=BLUE)
    ax.text(6.7, 1.2, "all arrows\nagree at P", ha="center", fontsize=8.5, color=BLUE)
    frame(ax, -0.4, 7.4, -1.15, 1.6); return fig


# ---------------------------------------------------------------- Prologue 4
def grid(ax, n=4, s=0.1):
    for k in range(-1, n + 1):
        ax.plot([k * s, k * s], [-s, n * s], color="#E3E3E3", lw=0.6, zorder=0)
        ax.plot([-s, n * s], [k * s, k * s], color="#E3E3E3", lw=0.6, zorder=0)


@fig("P4_components.png")
def _():
    fig, ax = new(4.6, 3.0)
    grid(ax, 5, 0.1)
    arrow(ax, 0, 0, 0.3, 0.4, lw=2.2)
    ax.plot([0, 0.3], [0, 0], color=BLUE, lw=1.6, ls="--"); ax.plot([0.3, 0.3], [0, 0.4], color=BLUE, lw=1.6, ls="--")
    ax.text(0.15, -0.04, "east part x = 0.3", ha="center", va="top", fontsize=8.5, color=BLUE)
    ax.text(0.32, 0.2, "north part\ny = 0.4", ha="left", va="center", fontsize=8.5, color=BLUE)
    ax.text(0.03, 0.3, "length 0.5", fontsize=8.5, rotation=53)
    ax.text(0.55, 0.42, "length² = x² + y²\n= 0.09 + 0.16 = 0.25", fontsize=9)
    frame(ax, -0.12, 0.95, -0.12, 0.52); return fig


@fig("P4_multiply.png")
def _():
    fig, ax = new(6.2, 2.3)
    def unit(ax, x0, t):
        ax.text(x0 + 0.5, -0.25, t, ha="center", fontsize=8.5)
    for i, (L, a, t) in enumerate([(0.5, 30, "first: 0.5, 30°"), (0.4, 60, "second: 0.4, 60°"), (0.2, 90, "combined: 0.2, 90°")]):
        x0 = i * 2.1
        ax.plot([x0, x0 + 1.2], [0, 0], color="#CCCCCC", lw=0.8)
        polar_arrow(ax, x0, 0, 2.2 * L, a, lw=2.2, color=BLUE if i == 2 else INK)
        ax.add_patch(Arc((x0, 0), 0.5, 0.5, theta1=0, theta2=a, color=GREY))
        unit(ax, x0, t)
    ax.text(1.65, 0.6, "×", fontsize=16, ha="center"); ax.text(3.75, 0.6, "=", fontsize=16, ha="center")
    ax.text(0, 1.35, "lengths multiply: 0.5 × 0.4 = 0.2      angles add: 30° + 60° = 90°", fontsize=9)
    frame(ax, -0.2, 6.0, -0.45, 1.5); return fig


@fig("P4_quarter_turns.png")
def _():
    fig, ax = new(3.8, 3.4)
    ax.add_patch(Circle((0, 0), 1, fill=False, color="#CCCCCC"))
    for a, t, pos in [(0, "1", (1.12, 0)), (90, "i", (0, 1.15)), (180, "−1 = i × i", (-1.15, 0.15)), (270, "−i = i × i × i", (0, -1.2))]:
        polar_arrow(ax, 0, 0, 1, a, lw=2.0, color=BLUE if a == 90 else INK)
        ax.text(pos[0], pos[1], t, ha="center", va="center", fontsize=9)
    ax.add_patch(Arc((0, 0), 0.6, 0.6, theta1=0, theta2=90, color=GREY)); ax.text(0.33, 0.33, "×i", fontsize=8.5, color=GREY)
    frame(ax, -1.9, 1.6, -1.45, 1.35); return fig


@fig("P4_unit_circle.png")
def _():
    fig, ax = new(4.0, 3.6)
    ax.add_patch(Circle((0, 0), 1, fill=False, color=GREY))
    ax.plot([-1.25, 1.25], [0, 0], color="#BBBBBB", lw=0.8); ax.plot([0, 0], [-1.25, 1.25], color="#BBBBBB", lw=0.8)
    t = math.radians(40)
    arrow(ax, 0, 0, math.cos(t), math.sin(t), lw=2.2, color=BLUE)
    ax.plot([math.cos(t), math.cos(t)], [0, math.sin(t)], color=INK, ls="--", lw=1)
    ax.text(math.cos(t) / 2, -0.1, "cos θ", ha="center", va="top", fontsize=9)
    ax.text(math.cos(t) + 0.05, math.sin(t) / 2, "sin θ", fontsize=9)
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=0, theta2=40, color=INK)); ax.text(0.3, 0.1, "θ", fontsize=9)
    ax.annotate("", xy=(0.95, -0.55), xytext=(0.55, -0.95), arrowprops=dict(arrowstyle="<-", color=RED, connectionstyle="arc3,rad=-0.3"))
    ax.text(0.95, -0.95, "stopwatch:\nclockwise, e$^{−iωt}$", fontsize=8, color=RED)
    ax.text(-1.2, 1.15, "e$^{iθ}$ = cos θ + i sin θ", fontsize=9.5, color=BLUE)
    frame(ax, -1.35, 1.75, -1.3, 1.35); return fig


@fig("P4_glass_formula.png")
def _():
    fig, ax = plt.subplots(figsize=(5.4, 2.6))
    phi = np.linspace(0, 720, 500)
    ax.plot(phi, 0.08 * (1 - np.cos(np.radians(phi))), color=INK, lw=1.8)
    for p in (0, 90, 180):
        ax.plot([p], [0.08 * (1 - math.cos(math.radians(p)))], "o", color=BLUE)
    ax.set_xlabel("extra turn φ of the back arrow (degrees)"); ax.set_ylabel("P = 0.08(1 − cos φ)")
    ax.set_xticks([0, 90, 180, 270, 360, 540, 720]); ax.set_ylim(0, 0.175)
    ax.text(185, 0.163, "0.16", fontsize=8.5, color=BLUE); ax.text(95, 0.074, "0.08", fontsize=8.5, color=BLUE); ax.text(8, 0.006, "0", fontsize=8.5, color=BLUE)
    return fig


# ---------------------------------------------------------------- Prologue 5
def st_axes(ax, x0, y0, w, h):
    arrow(ax, x0, y0, x0 + w, y0, color=GREY, lw=1, head=8); arrow(ax, x0, y0, x0, y0 + h, color=GREY, lw=1, head=8)
    ax.text(x0 + w + 0.05, y0 + 0.02, "space", ha="left", va="center", fontsize=8); ax.text(x0 - 0.08, y0 + h, "time", ha="right", va="top", fontsize=8)


@fig("P5_spacetime.png")
def _():
    fig, ax = new(5.0, 3.0)
    st_axes(ax, 0, 0, 4.2, 2.6)
    ax.plot([0.8, 0.8], [0.1, 2.4], color=INK, lw=1.8); ax.text(0.8, 2.48, "electron at rest", ha="center", fontsize=8)
    ax.plot([1.8, 2.8], [0.1, 2.4], color=INK, lw=1.8); ax.text(2.85, 2.48, "moving electron", ha="center", fontsize=8)
    photon(ax, (2.0, 0.2), (4.0, 2.2), amp=0.05); ax.text(3.9, 1.6, "photon\n(45°)", fontsize=8)
    ax.plot([1.3], [1.2], "o", color=BLUE); ax.text(1.38, 1.2, "a point: here, now", fontsize=8, color=BLUE, va="center")
    frame(ax, -0.4, 4.6, -0.3, 2.7); return fig


@fig("P5_three_actions.png")
def _():
    fig, ax = new(6.4, 2.5)
    st_axes(ax, 0, 0, 1.6, 1.9); photon(ax, (0.3, 0.3), (1.4, 1.4), amp=0.05)
    ax.plot([0.3], [0.3], "o", color=INK, ms=3); ax.plot([1.4], [1.4], "o", color=INK, ms=3)
    ax.text(0.85, -0.5, "1: photon goes\nfrom point to point", ha="center", fontsize=8.5)
    st_axes(ax, 2.3, 0, 1.6, 1.9); fermion(ax, (2.7, 0.3), (3.3, 1.5))
    ax.plot([2.7], [0.3], "o", color=INK, ms=3); ax.plot([3.3], [1.5], "o", color=INK, ms=3)
    ax.text(3.15, -0.5, "2: electron goes\nfrom point to point", ha="center", fontsize=8.5)
    st_axes(ax, 4.6, 0, 1.6, 1.9); v = (5.3, 0.95)
    fermion(ax, (5.2, 0.2), v); fermion(ax, v, (5.5, 1.7)); photon(ax, v, (6.1, 1.6), amp=0.04); vertex(ax, v)
    ax.text(v[0] - 0.1, v[1], "j", fontsize=10, color=BLUE, ha="right")
    ax.text(5.45, -0.5, "3: electron emits or\nabsorbs a photon (j)", ha="center", fontsize=8.5)
    frame(ax, -0.3, 6.5, -0.85, 2.1); return fig


@fig("P5_exchange.png")
def _():
    fig, ax = new(6.4, 2.9)
    for k, swap in enumerate([False, True]):
        x0 = k * 3.4
        p1, p2 = (x0 + 0.4, 0.1), (x0 + 2.0, 0.1)
        p3, p4 = (x0 + 0.4, 2.3), (x0 + 2.0, 2.3)
        p5, p6 = (x0 + 0.55, 1.0), (x0 + 1.85, 1.3)
        fermion(ax, p1, p5); fermion(ax, p2, p6)
        if not swap:
            fermion(ax, p5, p3); fermion(ax, p6, p4)
        else:
            fermion(ax, p5, p4); fermion(ax, p6, p3)
        photon(ax, p5, p6, amp=0.05); vertex(ax, p5); vertex(ax, p6)
        for p, s in [(p1, "1"), (p2, "2"), (p3, "3"), (p4, "4")]:
            ax.text(p[0], p[1] - 0.12 if p[1] < 1 else p[1] + 0.12, s, ha="center", va="top" if p[1] < 1 else "bottom", fontsize=9)
        ax.text(p5[0] - 0.12, p5[1], "5", ha="right", fontsize=9, color=BLUE); ax.text(p6[0] + 0.12, p6[1], "6", ha="left", fontsize=9, color=BLUE)
        ax.text(x0 + 1.2, -0.4, ["1 → 3, 2 → 4", "1 → 4, 2 → 3: arrow reversed"][k], ha="center", fontsize=8.5)
    ax.text(3.0, 1.2, "−", fontsize=18, ha="center")
    frame(ax, -0.1, 6.3, -0.6, 2.7); return fig


@fig("P5_glass.png")
def _():
    fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.0), gridspec_kw=dict(width_ratios=[1.0, 1.0]))
    ax = axs[0]; ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(mp.Rectangle((1.0, 0), 1.6, 2.0, fc="#DCEBF5", ec=INK))
    for i in range(8):
        for j in range(5):
            ax.plot(1.1 + i * 0.2, 0.2 + j * 0.4, "o", color=INK, ms=2)
    arrow(ax, 0.0, 1.0, 0.95, 1.0, lw=1.4); ax.text(0.0, 1.15, "light in", fontsize=9.5)
    for i in range(0, 8, 2):
        arrow(ax, 1.1 + i * 0.2, 0.8, 0.2, 0.5, lw=0.6, color=GREY, head=5)
    ax.text(-0.1, -0.05, "every electron\nscatters a little back", fontsize=9.5)
    ax.set_xlim(-0.1, 2.8); ax.set_ylim(-0.1, 2.1)
    ax = axs[1]; ax.set_aspect("equal"); ax.axis("off")
    z = 0j; pts = [z]
    for n in range(60):
        z += 0.1 * np.exp(-1j * 2 * math.pi * n / 24)
        pts.append(z)
    pts = np.array(pts)
    ax.plot(pts.real, pts.imag, color=INK, lw=1.0)
    for n in range(0, 60, 3):
        arrow(ax, pts[n].real, pts[n].imag, pts[n + 1].real, pts[n + 1].imag, lw=0.9, head=6)
    arrow(ax, 0, 0, pts[-1].real, pts[-1].imag, color=BLUE, lw=1.8)
    ax.text(0.2, -1.1, "layers deeper and deeper:\narrows curl round a circle", fontsize=9.5, ha="center")
    ax.text(pts[-1].real + 0.05, pts[-1].imag + 0.08, "net", fontsize=8, color=BLUE)
    ax.set_xlim(-0.9, 1.3); ax.set_ylim(-1.4, 0.5)
    fig.tight_layout(); return fig


@fig("P5_positron.png")
def _():
    fig, ax = new(5.0, 2.8)
    st_axes(ax, 0, 0, 3.6, 2.6)
    A, B = (2.4, 0.8), (1.4, 1.7)
    fermion(ax, (0.7, 0.2), B)
    fermion(ax, B, A)  # backward in time
    fermion(ax, A, (3.0, 2.4))
    photon(ax, (3.4, 0.2), A, amp=0.05); photon(ax, B, (0.7, 2.5), amp=0.05)
    vertex(ax, A); vertex(ax, B)
    ax.text(A[0] + 0.12, A[1] - 0.05, "A", fontsize=9); ax.text(B[0] - 0.15, B[1] + 0.05, "B", fontsize=9, ha="right")
    ax.text(2.05, 1.05, "runs back in time:\na positron", fontsize=8, color=BLUE)
    frame(ax, -0.4, 4.0, -0.3, 2.7); return fig


# ---------------------------------------------------------------- Prologue 6
@fig("P6_corrections.png")
def _():
    fig, ax = new(6.6, 2.2)
    top = (0.8, 0.7)
    fermion(ax, (0.0, 1.5), top); fermion(ax, top, (1.6, 1.5)); photon(ax, top, (0.8, -0.2), amp=0.05); vertex(ax, top)
    ax.text(0.8, -0.8, "simplest\n(g = 2)", ha="center", va="top", fontsize=8.5)
    ax.text(1.95, 0.8, "+", fontsize=15)
    loop_vx(ax, 2.2, -0.1, 0.75, lab=False, ext="")
    ax.text(3.0, -0.8, "one loop\n(× ~1/137)", ha="center", va="top", fontsize=8.5)
    ax.text(4.1, 0.8, "+", fontsize=15)
    loop_se(ax, 4.4, 1.2, 0.5, lab=False)
    loop_vp(ax, 5.55, 1.2, 0.5, lab=False)
    ax.text(5.3, 0.55, "…", fontsize=14)
    ax.text(5.6, -0.8, "pieces of two-loop\npictures (× ~1/137²)", ha="center", va="top", fontsize=8.5)
    frame(ax, -0.2, 6.8, -1.35, 1.8); return fig


@fig("P6_digits.png")
def _():
    fig, ax = new(6.0, 2.0)
    digits = "1.001159652180"
    groups = [(0, 1, "Dirac: 1"), (1, 6, "+ one loop"), (6, 9, "+ two, three loops"), (9, 14, "+ four, five loops")]
    x = 0
    cols = ["#1F4E78", "#4F81BD", "#8DB3E2", "#C6D9F0"]
    for gi, (a, b, t) in enumerate(groups):
        for ch in digits[a:b]:
            ax.add_patch(mp.Rectangle((x, 0.5), 0.36, 0.5, fc=cols[gi], ec="white"))
            ax.text(x + 0.18, 0.75, ch, ha="center", va="center", fontsize=12, color="white" if gi < 2 else INK)
            x += 0.38
        ax.text((x - 0.38 * (b - a)) + 0.19 * (b - a), 0.38 - 0.28 * (gi % 2), t, ha="center", va="top", fontsize=8)
    ax.text(x + 0.1, 0.75, "59 (13)", fontsize=10, va="center", color=GREY)
    ax.text(0, 1.3, "g/2 of the electron: which pictures fix which digits (schematic)", fontsize=9)
    frame(ax, -0.1, 6.6, -0.35, 1.5); return fig


@fig("P6_screening.png")
def _():
    fig, ax = new(5.0, 3.0)
    ax.add_patch(Circle((0, 0), 0.14, color=INK)); ax.text(0, 0, "−", color="white", ha="center", va="center", fontsize=11)
    rng = np.random.default_rng(1)
    for k in range(14):
        r = rng.uniform(0.5, 1.3); t = rng.uniform(0, 2 * math.pi)
        c = (r * math.cos(t), r * math.sin(t))
        u = (-math.cos(t) * 0.13, -math.sin(t) * 0.13)
        ax.text(c[0] + u[0], c[1] + u[1], "+", ha="center", va="center", fontsize=9, color=RED)
        ax.text(c[0] - u[0], c[1] - u[1], "−", ha="center", va="center", fontsize=9, color=BLUE)
    for r, t in [(0.45, "close probe:\nsees more charge"), (1.6, "distant probe: sees\nthe screened charge e")]:
        ax.add_patch(Circle((0, 0), r, fill=False, ls="--", color=GREY))
    ax.text(0.5, -0.3, "close", fontsize=8); ax.text(1.65, -1.0, "far", fontsize=8)
    frame(ax, -1.8, 2.6, -1.7, 1.7); return fig


# ---------------------------------------------------------------- Prologue 7
@fig("P7_maxwell.png")
def _():
    fig, ax = new(6.6, 2.2)
    # Gauss E
    ax.add_patch(Circle((0.6, 0.9), 0.12, color=RED)); ax.text(0.6, 0.9, "+", color="white", ha="center", va="center")
    for k in range(8):
        t = k * math.pi / 4
        arrow(ax, 0.6 + 0.16 * math.cos(t), 0.9 + 0.16 * math.sin(t), 0.6 + 0.55 * math.cos(t), 0.9 + 0.55 * math.sin(t), lw=1, head=6)
    ax.text(0.6, 0.05, "E lines start\non charges", ha="center", fontsize=8)
    # Gauss B
    ax.add_patch(mp.Rectangle((1.55, 0.8), 0.5, 0.2, fc="#DDDDDD", ec=INK))
    for r in (0.3, 0.45):
        ax.add_patch(mp.Ellipse((1.8, 0.9), 2 * r + 0.4, 2 * r, fill=False, color=INK, lw=0.9))
    ax.text(1.8, 0.05, "B lines\nnever end", ha="center", fontsize=8)
    # Faraday
    arrow(ax, 3.2, 0.55, 3.2, 1.35, color=BLUE, lw=1.6, head=9); ax.text(3.28, 1.3, "B changing", fontsize=7.5, color=BLUE)
    ax.add_patch(Arc((3.2, 0.95), 0.9, 0.35, theta1=200, theta2=340, color=INK, lw=1.3))
    ax.add_patch(Arc((3.2, 0.95), 0.9, 0.35, theta1=20, theta2=160, color=INK, lw=1.3, ls="--"))
    ax.text(3.2, 0.05, "changing B\n→ loop of E", ha="center", fontsize=8)
    # Ampere
    ax.plot([4.6, 4.6], [0.5, 1.4], color=INK, lw=2.2); ax.text(4.68, 1.35, "I", fontsize=9)
    ax.add_patch(Arc((4.6, 0.95), 0.9, 0.35, theta1=200, theta2=340, color=BLUE, lw=1.3))
    ax.text(4.6, 0.05, "current, changing E\n→ loop of B", ha="center", fontsize=8)
    # wave
    xs = np.linspace(5.5, 6.9, 200)
    ax.plot(xs, 0.95 + 0.3 * np.sin(2 * math.pi * (xs - 5.5) / 0.7), color=RED, lw=1.3)
    ax.plot(xs, 0.95 + 0.15 * np.sin(2 * math.pi * (xs - 5.5) / 0.7), color=BLUE, lw=1.0, ls="--")
    ax.text(6.2, 0.05, "together: a wave\nmoving at c", ha="center", fontsize=8)
    frame(ax, -0.1, 7.0, -0.3, 1.6); return fig


# ---------------------------------------------------------------- Prologues 8 and 9
@fig("P8_braket.png")
def _():
    fig, ax = new(6.4, 1.6)
    box(ax, 0.0, 0.3, 1.3, 0.6, "|ψ⟩\nthe situation")
    box(ax, 1.8, 0.3, 1.3, 0.6, "⟨φ|\nthe question", fc="#F7F7F7", ec=INK)
    box(ax, 3.6, 0.3, 1.2, 0.6, "⟨φ|ψ⟩\nan arrow")
    box(ax, 5.3, 0.3, 1.3, 0.6, "|⟨φ|ψ⟩|²\nwhat clicks", fc="#F7F7F7", ec=INK)
    for x in (1.35, 3.15, 4.85):
        arrow(ax, x, 0.6, x + 0.4, 0.6, color=BLUE, lw=1.2, head=8)
    frame(ax, -0.1, 6.7, 0.1, 1.1); return fig


@fig("P9_twoport.png")
def _():
    fig, ax = new(5.4, 1.8)
    box(ax, 1.8, 0.2, 1.8, 1.0, "network\n(S-matrix)")
    arrow(ax, 0.3, 0.95, 1.75, 0.95, lw=1.4); ax.text(0.3, 1.08, "a₁ in", fontsize=9)
    arrow(ax, 1.75, 0.45, 0.3, 0.45, lw=1.4, color=GREY); ax.text(0.3, 0.25, "b₁ out", fontsize=9)
    arrow(ax, 3.65, 0.95, 5.1, 0.95, lw=1.4, color=GREY); ax.text(4.6, 1.08, "b₂ out", fontsize=9)
    arrow(ax, 5.1, 0.45, 3.65, 0.45, lw=1.4); ax.text(4.6, 0.25, "a₂ in", fontsize=9)
    frame(ax, 0.1, 5.3, 0.0, 1.35); return fig


@fig("P9_marks.png")
def _():
    fig, ax = new(6.0, 1.4)
    fermion(ax, (0, 0.5), (1.3, 0.5)); ax.text(0.65, 0.1, "electron goes", ha="center", fontsize=9)
    photon(ax, (2.1, 0.5), (3.4, 0.5)); ax.text(2.75, 0.1, "photon goes", ha="center", fontsize=9)
    v = (4.9, 0.6)
    fermion(ax, (4.2, 0.95), v); fermion(ax, v, (5.6, 0.95)); photon(ax, v, (4.9, 0.25), amp=0.04, waves=3); vertex(ax, v)
    ax.text(4.9, 0.0, "vertex: emit or absorb", ha="center", fontsize=9)
    frame(ax, -0.2, 6.0, -0.15, 1.1); return fig


if __name__ == "__main__":
    import sys
    want = sys.argv[1:]
    for name, f in FIGS.items():
        if want and name not in want:
            continue
        save(f(), name)
        print("wrote", name)
