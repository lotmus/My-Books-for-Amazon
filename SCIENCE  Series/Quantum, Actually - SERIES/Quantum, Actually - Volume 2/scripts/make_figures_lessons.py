# -*- coding: utf-8 -*-
"""Feynman diagrams, momentum-flow and kinematics figures, loop topologies and
concept maps for Lessons 45-79 (and the Mead Interlude). Run: python make_figures_lessons.py"""
import math
import numpy as np
from figlib import *
from matplotlib.patches import Rectangle, Circle

FIGS = {}


def fig(name):
    def deco(f):
        FIGS[name] = f
        return f
    return deco


def tchannel(ax, x0=0.0, top=("e⁻(p₁)", "e⁻(p₃)"), bot=("μ⁻(p₂)", "μ⁻(p₄)"), q="q = p₁ − p₃", cross=False):
    a, b = (x0 + 1.0, 1.4), (x0 + 1.0, 0.0)
    fermion(ax, (x0, 1.9), a); fermion(ax, a, (x0 + 2.0, 1.9))
    fermion(ax, (x0, -0.5), b); fermion(ax, b, (x0 + 2.0, -0.5))
    photon(ax, a, b)
    vertex(ax, a); vertex(ax, b)
    label(ax, (x0, 1.9), top[0], dx=-0.05, dy=0.13, ha="right")
    label(ax, (x0 + 2.0, 1.9), top[1], dx=0.05, dy=0.13, ha="left")
    label(ax, (x0, -0.5), bot[0], dx=-0.05, dy=-0.13, ha="right")
    label(ax, (x0 + 2.0, -0.5), bot[1], dx=0.05, dy=-0.13, ha="left")
    if q:
        mom(ax, a, b, q, off=-0.45)


@fig("L45_vertex.png")
def _():
    fig, ax = new(5.0, 2.6)
    v = (1.0, 0.6)
    fermion(ax, (0, 1.3), v); fermion(ax, v, (2.0, 1.3)); photon(ax, v, (1.0, -0.4)); vertex(ax, v)
    label(ax, (0, 1.3), "e⁻(p)", dx=-0.05, ha="right"); label(ax, (2.0, 1.3), "e⁻(p′)", dx=0.05, ha="left")
    label(ax, (1.0, -0.4), "γ(q),  q = p − p′", dy=-0.12, va="top")
    label(ax, v, "ieγ^μ", dx=0.15, dy=-0.12, ha="left", color=BLUE)
    mom(ax, (0, 1.3), v, "p", off=0.15); mom(ax, v, (2.0, 1.3), "p′", off=0.15)
    ax.text(2.6, 0.45, "One vertex:\ncharge flows through,\nmomentum is conserved,\nfactor ieγ^μ", fontsize=9, va="center")
    frame(ax, -0.8, 4.2, -0.75, 1.6); return fig


@fig("L46_poles.png")
def _():
    fig, ax = new(5.6, 2.8, axis=True)
    ax.axhline(0, color=GREY, lw=0.8); ax.axvline(0, color=GREY, lw=0.8)
    ax.plot([1.5], [-0.25], "x", color=RED, ms=9, mew=2); ax.plot([-1.5], [0.25], "x", color=RED, ms=9, mew=2)
    ax.text(1.5, -0.5, "+E_p − iε", ha="center", color=RED, fontsize=9)
    ax.text(-1.5, 0.5, "−E_p + iε", ha="center", color=RED, fontsize=9)
    ax.annotate("", xy=(2.8, 0.02), xytext=(-2.8, 0.02), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.6))
    ax.text(2.9, 0.12, "real p⁰ axis\n(integration)", fontsize=8.5, color=BLUE, va="bottom")
    ax.text(-2.9, -0.95, "Feynman's iε moves the positive-energy pole just below the axis and the\nnegative-energy pole just above: x⁰ > y⁰ picks +E_p, x⁰ < y⁰ picks −E_p.", fontsize=8.5)
    ax.set_xlim(-3.0, 3.6); ax.set_ylim(-1.1, 1.0); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("Re p⁰"); ax.set_ylabel("Im p⁰"); ax.set_aspect("auto"); return fig


def propagator_card(name, kind, formula, note):
    def f():
        fig, ax = new(5.2, 1.5)
        if kind == "f":
            fermion(ax, (0, 0), (2.2, 0)); mom(ax, (0, 0), (2.2, 0), "p", off=0.2)
        elif kind == "g":
            photon(ax, (0, 0), (2.2, 0)); mom(ax, (0, 0), (2.2, 0), "k", off=0.22)
            label(ax, (0, 0), "μ", dx=-0.12); label(ax, (2.2, 0), "ν", dx=0.12)
        else:
            ax.plot([0, 2.2], [0, 0], color=INK, lw=1.6, ls="--"); mom(ax, (0, 0), (2.2, 0), "p", off=0.2)
        vertex(ax, (0, 0), 0.03); vertex(ax, (2.2, 0), 0.03)
        label(ax, (0, 0), "y", dy=-0.22); label(ax, (2.2, 0), "x", dy=-0.22)
        ax.text(2.8, 0.08, formula, fontsize=12, va="center", color=BLUE)
        ax.text(2.8, -0.32, note, fontsize=8.5, va="center")
        frame(ax, -0.3, 6.6, -0.55, 0.5); return fig
    FIGS[name] = f


propagator_card("L46_scalar.png", "s", "Δ_F(p) = i / (p² − m² + iε)", "scalar line: one number per momentum")
propagator_card("L47_electron.png", "f", "S_F(p) = i(p̸ + m) / (p² − m² + iε)", "electron line: a 4×4 matrix; arrow = flow of charge")
propagator_card("L48_photon.png", "g", "D_F^μν(k) = −ig^μν / (k² + iε)", "photon line in Feynman gauge (ξ = 1)")


@fig("L49_vertices.png")
def _():
    fig, ax = new(6.2, 2.2)
    for i, (t, a, b, c) in enumerate([("e⁻ absorbs γ", "in", "out", "γ in"), ("e⁻e⁺ annihilate", "e⁻", "e⁺", "γ out"), ("γ makes a pair", "e⁻", "e⁺", "γ in")]):
        x = i * 2.2
        v = (x + 0.8, 0.5)
        if i == 0:
            fermion(ax, (x, 0), v); fermion(ax, v, (x + 1.6, 0)); photon(ax, (x + 0.8, 1.3), v)
        elif i == 1:
            fermion(ax, (x, 0), v); fermion(ax, v, (x + 1.6, 0), reverse=True); photon(ax, v, (x + 0.8, 1.3))
        else:
            fermion(ax, v, (x, 0), reverse=False); fermion(ax, (x + 1.6, 0), v); photon(ax, (x + 0.8, 1.3), v)
        vertex(ax, v); label(ax, (x + 0.8, -0.35), t, size=9)
    ax.text(0, 1.75, "One vertex, three readings (time runs left to right): every one carries the same factor ieγ^μ", fontsize=9)
    frame(ax, -0.2, 6.6, -0.55, 1.95); return fig


@fig("L50_rules.png")
def _():
    fig, ax = new(6.4, 4.2)
    rows = [("f", "incoming electron", "u(p)"), ("fr", "incoming positron", "v̄(p)"),
            ("f", "outgoing electron", "ū(p′)"), ("fr", "outgoing positron", "v(p′)"),
            ("g", "incoming / outgoing photon", "ε_μ(k)  /  ε*_μ(k)"),
            ("f", "internal electron", "i(p̸+m)/(p²−m²+iε)"), ("g", "internal photon", "−ig_μν/(k²+iε)"),
            ("v", "vertex", "ieγ^μ, with (2π)⁴δ⁴(Σp)"), ("l", "closed fermion loop", "(−1) × trace, ∫d⁴k/(2π)⁴")]
    for i, (k, name, val) in enumerate(rows):
        y = -i * 0.5
        if k == "f":
            fermion(ax, (0, y), (1.2, y))
        elif k == "fr":
            fermion(ax, (0, y), (1.2, y), reverse=True)
        elif k == "g":
            photon(ax, (0, y), (1.2, y), amp=0.05)
        elif k == "v":
            fermion(ax, (0.1, y + 0.18), (0.6, y), arrow_mid=False); fermion(ax, (0.6, y), (1.1, y + 0.18), arrow_mid=False); photon(ax, (0.6, y), (0.6, y - 0.22), amp=0.03, waves=2); vertex(ax, (0.6, y))
        else:
            fermion_arc(ax, (0.6, y), 0.17, 0, 360, arrow_at=90)
        ax.text(1.5, y, name, fontsize=9.5, va="center")
        ax.text(4.35, y, val, fontsize=10, va="center", color=BLUE)
    ax.text(0, 0.45, "Feynman rules of this course (ħ = c = 1, mostly-minus metric)", fontsize=10, weight="bold")
    frame(ax, -0.2, 7.0, -4.3, 0.65); return fig


@fig("L51_kinematics.png")
def _():
    fig, ax = new(6.2, 2.6)
    c = (1.3, 0.6)
    ax.add_patch(Circle(c, 0.35, fc="#EAF2F8", ec=INK, lw=1.4, zorder=3)); label(ax, c, "iℳ", size=11)
    for (p, s) in [((0.0, 1.4), "p₁"), ((0.0, -0.2), "p₂")]:
        fermion(ax, p, c); label(ax, p, s, dx=-0.15)
    for (p, s) in [((2.6, 1.4), "p₃"), ((2.6, -0.2), "p₄")]:
        fermion(ax, c, p); label(ax, p, s, dx=0.15)
    ax.text(3.2, 1.25, "s = (p₁ + p₂)²   total energy² in the CM frame", fontsize=9)
    ax.text(3.2, 0.75, "t = (p₁ − p₃)²   momentum transfer²", fontsize=9)
    ax.text(3.2, 0.25, "u = (p₁ − p₄)²   crossed transfer²", fontsize=9)
    ax.text(3.2, -0.25, "s + t + u = m₁² + m₂² + m₃² + m₄²", fontsize=9, color=BLUE)
    frame(ax, -0.4, 7.4, -0.5, 1.7); return fig


@fig("L52_external.png")
def _():
    fig, ax = new(6.0, 2.2)
    items = [("u(p)", "e⁻ in", False, "f"), ("ū(p′)", "e⁻ out", False, "fo"), ("v̄(p)", "e⁺ in", True, "f"),
             ("v(p′)", "e⁺ out", True, "fo"), ("ε_μ", "γ in", False, "g"), ("ε*_μ", "γ out", False, "go")]
    for i, (sym, name, rev, k) in enumerate(items):
        x = i * 1.0
        v = (x + 0.45, 0.3) if k.endswith("o") else (x + 0.45, 1.1)
        if k[0] == "f":
            if k == "f":
                fermion(ax, (x + 0.45, 1.1), (x + 0.45, 0.3), reverse=rev); vertex(ax, (x + 0.45, 0.3))
            else:
                fermion(ax, (x + 0.45, 1.1), (x + 0.45, 0.3), reverse=rev); vertex(ax, (x + 0.45, 1.1))
        else:
            photon(ax, (x + 0.45, 1.1), (x + 0.45, 0.3), amp=0.05, waves=4)
            vertex(ax, (x + 0.45, 0.3) if k == "g" else (x + 0.45, 1.1))
        label(ax, (x + 0.45, -0.05), sym, color=BLUE, size=10.5); label(ax, (x + 0.45, 1.4), name, size=9)
    ax.text(0, -0.45, "Read down the page as time; the dot is where the line meets the rest of the diagram.", fontsize=8.5)
    frame(ax, -0.1, 6.1, -0.6, 1.6); return fig


@fig("L53_momentum.png")
def _():
    fig, ax = new(6.0, 2.8)
    tchannel(ax, 0.0, q=None)
    mom(ax, (1.0, 1.4), (1.0, 0.0), "q", off=-0.25)
    ax.text(2.9, 1.5, "At each dot: momentum in = momentum out", fontsize=9.5)
    ax.text(2.9, 1.05, "upper dot:  p₁ = p₃ + q", fontsize=9.5, color=BLUE)
    ax.text(2.9, 0.65, "lower dot:  p₂ + q = p₄", fontsize=9.5, color=BLUE)
    ax.text(2.9, 0.2, "together:  p₁ + p₂ = p₃ + p₄", fontsize=9.5, color=BLUE)
    ax.text(2.9, -0.3, "A tree fixes every internal momentum;\na loop leaves one momentum k to integrate.", fontsize=9)
    frame(ax, -0.9, 6.6, -0.8, 2.15); return fig


@fig("L54_emu.png")
def _():
    fig, ax = new(6.4, 2.8)
    tchannel(ax, 0.0)
    # CM kinematics
    o = (4.6, 0.7)
    arrow(ax, o[0] - 1.1, o[1], o[0] - 0.05, o[1], color=INK, lw=1.4); arrow(ax, o[0] + 1.1, o[1], o[0] + 0.05, o[1], color=GREY, lw=1.4)
    t = math.radians(35)
    arrow(ax, o[0], o[1], o[0] + 1.1 * math.cos(t), o[1] + 1.1 * math.sin(t), color=INK, lw=1.4)
    arrow(ax, o[0], o[1], o[0] - 1.1 * math.cos(t), o[1] - 1.1 * math.sin(t), color=GREY, lw=1.4)
    ax.add_patch(Arc(o, 0.8, 0.8, theta1=0, theta2=35, color=BLUE)); label(ax, (o[0] + 0.55, o[1] + 0.15), "θ", color=BLUE)
    label(ax, (o[0] - 1.1, o[1]), "e⁻", dx=-0.12); label(ax, (o[0] + 1.1, o[1]), "μ⁻", dx=0.14)
    label(ax, (o[0], o[1] - 0.95), "CM frame: t = −2p²(1 − cos θ)", size=8.5)
    frame(ax, -0.9, 6.1, -0.8, 2.15); return fig


@fig("L55_moller.png")
def _():
    fig, ax = new(6.6, 2.7)
    tchannel(ax, 0.0, top=("e⁻(p₁)", "e⁻(p₃)"), bot=("e⁻(p₂)", "e⁻(p₄)"), q="t")
    a, b = (4.6, 1.4), (4.6, 0.0)
    fermion(ax, (3.6, 1.9), a); fermion(ax, a, (5.6, -0.5)); fermion(ax, (3.6, -0.5), b); fermion(ax, b, (5.6, 1.9))
    photon(ax, a, b); vertex(ax, a); vertex(ax, b)
    label(ax, (3.6, 1.9), "e⁻(p₁)", dx=-0.05, dy=0.13, ha="right"); label(ax, (5.6, 1.9), "e⁻(p₃)", dx=0.05, dy=0.13, ha="left")
    label(ax, (3.6, -0.5), "e⁻(p₂)", dx=-0.05, dy=-0.13, ha="right"); label(ax, (5.6, -0.5), "e⁻(p₄)", dx=0.05, dy=-0.13, ha="left")
    label(ax, (1.0, -1.0), "direct, ℳ_t", size=9); label(ax, (4.6, -1.0), "exchange, ℳ_u  (relative minus sign)", size=9)
    label(ax, (2.8, 0.7), "−", size=16)
    frame(ax, -0.9, 6.6, -1.2, 2.15); return fig


def two_photon_pair(ax, x0, swap, labels_f, labels_g, title):
    a, b = (x0 + 1.0, 1.3), (x0 + 1.0, 0.1)
    fermion(ax, (x0, 1.3), a); fermion(ax, a, b); fermion(ax, b, (x0, 0.1))
    ga, gb = ((x0 + 2.0, 1.3), (x0 + 2.0, 0.1)) if not swap else ((x0 + 2.0, 0.1), (x0 + 2.0, 1.3))
    photon(ax, a, ga); photon(ax, b, gb); vertex(ax, a); vertex(ax, b)
    label(ax, (x0, 1.3), labels_f[0], dx=-0.08, ha="right"); label(ax, (x0, 0.1), labels_f[1], dx=-0.08, ha="right")
    label(ax, (x0 + 2.0, 1.3), labels_g[0] if not swap else labels_g[1], dx=0.08, ha="left")
    label(ax, (x0 + 2.0, 0.1), labels_g[1] if not swap else labels_g[0], dx=0.08, ha="left")
    label(ax, (x0 + 1.0, -0.4), title, size=9)


@fig("L56_annihilation.png")
def _():
    fig, ax = new(6.4, 2.2)
    two_photon_pair(ax, 0.0, False, ("e⁻(p₁)", "e⁺(p₂)"), ("γ(k₁)", "γ(k₂)"), "t-channel: internal p₁ − k₁")
    two_photon_pair(ax, 3.6, True, ("e⁻(p₁)", "e⁺(p₂)"), ("γ(k₁)", "γ(k₂)"), "u-channel: internal p₁ − k₂")
    label(ax, (2.9, 0.7), "+", size=16)
    frame(ax, -0.9, 6.4, -0.6, 1.6); return fig


@fig("L57_compton.png")
def _():
    fig, ax = new(6.6, 2.3)
    for k, (x0, ch) in enumerate([(0.0, "s"), (3.7, "u")]):
        a, b = (x0 + 0.8, 0.4), (x0 + 1.8, 0.4)
        fermion(ax, (x0, 0.4), a); fermion(ax, a, b); fermion(ax, b, (x0 + 2.6, 0.4)); vertex(ax, a); vertex(ax, b)
        if ch == "s":
            photon(ax, (x0 + 0.1, 1.3), a); photon(ax, b, (x0 + 2.5, 1.3))
            label(ax, (x0 + 0.1, 1.3), "γ(k)", dy=0.13); label(ax, (x0 + 2.5, 1.3), "γ(k′)", dy=0.13)
            label(ax, (x0 + 1.3, -0.35), "s-channel: internal p + k", size=9)
        else:
            photon(ax, (x0 + 0.1, 1.3), b); photon(ax, a, (x0 + 2.5, 1.3))
            label(ax, (x0 + 0.1, 1.3), "γ(k)", dy=0.13); label(ax, (x0 + 2.5, 1.3), "γ(k′)", dy=0.13)
            label(ax, (x0 + 1.3, -0.35), "u-channel: internal p − k′", size=9)
        label(ax, (x0, 0.4), "e⁻(p)", dy=-0.18); label(ax, (x0 + 2.6, 0.4), "e⁻(p′)", dy=-0.18)
    label(ax, (3.15, 0.7), "+", size=16)
    frame(ax, -0.4, 6.6, -0.6, 1.6); return fig


@fig("L57_klein_nishina.png")
def _():
    fig, ax = plt.subplots(figsize=(5.4, 2.8))
    th = np.linspace(0, math.pi, 400)
    for eps, ls, lab in [(0.0, "-", "low energy (Thomson): ω ≪ m"), (1.0, "--", "ω = m"), (5.0, ":", "ω = 5m")]:
        r = 1 / (1 + eps * (1 - np.cos(th)))
        y = 0.5 * r ** 2 * (r + 1 / r - np.sin(th) ** 2)
        ax.plot(np.degrees(th), y, ls, color=INK, lw=1.6, label=lab)
    ax.set_xlabel("scattering angle θ (degrees)"); ax.set_ylabel("dσ/dΩ  in units of r_e²")
    ax.set_xlim(0, 180); ax.set_ylim(0, 1.05); ax.legend(frameon=False, fontsize=8.5)
    ax.set_title("Klein–Nishina: hard photons scatter forward", fontsize=10); return fig


@fig("L58_pair.png")
def _():
    fig, ax = new(6.4, 2.2)
    for k, (x0, sw) in enumerate([(0.0, False), (3.6, True)]):
        a, b = (x0 + 1.0, 1.3), (x0 + 1.0, 0.1)
        ga, gb = (x0, 1.3), (x0, 0.1)
        photon(ax, ga, a if not sw else b); photon(ax, gb, b if not sw else a)
        fermion(ax, a, (x0 + 2.0, 1.3)); fermion(ax, b, a); fermion(ax, (x0 + 2.0, 0.1), b)
        vertex(ax, a); vertex(ax, b)
        label(ax, ga, "γ(k₁)", dx=-0.08, ha="right"); label(ax, gb, "γ(k₂)", dx=-0.08, ha="right")
        label(ax, (x0 + 2.0, 1.3), "e⁻(p₁)", dx=0.08, ha="left"); label(ax, (x0 + 2.0, 0.1), "e⁺(p₂)", dx=0.08, ha="left")
        label(ax, (x0 + 1.0, -0.4), ["t-channel", "u-channel (photons crossed)"][k], size=9)
    label(ax, (2.95, 0.7), "+", size=16)
    ax.text(0, -0.85, "Threshold: s = (k₁ + k₂)² ≥ 4m², i.e. ≥ 1.022 MeV in the CM frame", fontsize=9, color=BLUE)
    frame(ax, -0.9, 6.4, -1.0, 1.6); return fig


def flow(ax, boxes, y=0.0, w=1.35, h=0.62, gap=0.32, fs=8.5):
    x = 0.0
    centers = []
    for i, t in enumerate(boxes):
        ax.add_patch(matplotlib.patches.FancyBboxPatch((x, y - h / 2), w, h, boxstyle="round,pad=0.03",
                     fc="#EAF2F8" if i % 2 == 0 else "#F7F7F7", ec=BLUE, lw=1.1))
        ax.text(x + w / 2, y, t, ha="center", va="center", fontsize=fs)
        if i:
            arrow(ax, x - gap + 0.02, y, x - 0.02, y, color=BLUE, lw=1.2, head=9)
        centers.append((x + w / 2, y))
        x += w + gap
    return centers


import matplotlib.patches  # noqa


@fig("L59_flow.png")
def _():
    fig, ax = new(6.8, 1.3)
    flow(ax, ["diagrams\n→ iℳ", "square\n|ℳ|²", "average in,\nsum out spins", "× phase space\n÷ flux", "dσ/dΩ\n(measured)"])
    frame(ax, -0.1, 8.5, -0.45, 0.45); return fig


@fig("L60_decay.png")
def _():
    fig, ax = new(5.6, 2.0)
    c = (0.8, 0.5)
    ax.add_patch(Circle(c, 0.12, color=INK)); label(ax, c, "M at rest", dy=-0.35, size=9)
    arrow(ax, c[0] + 0.14, c[1] + 0.07, c[0] + 0.8, c[1] + 0.45, lw=1.6); arrow(ax, c[0] - 0.14, c[1] - 0.07, c[0] - 0.8, c[1] - 0.45, lw=1.6)
    label(ax, (c[0] + 0.95, c[1] + 0.55), "p_f", size=9.5); label(ax, (c[0] - 0.95, c[1] - 0.55), "−p_f", size=9.5)
    ax.text(2.4, 1.2, "dΓ/dΩ = p_f |ℳ|² / (32π² M²)", fontsize=11, color=BLUE)
    ax.text(2.4, 0.25, "Two bodies leave back to back with equal\nand opposite momenta; only the direction\nis free, so phase space is one sphere.", fontsize=8.5)
    frame(ax, -0.5, 6.8, -0.3, 1.5); return fig


@fig("_unused_L61_sigma.png")
def _():
    fig, ax = plt.subplots(figsize=(5.4, 2.6))
    E = np.linspace(1, 40, 400)  # sqrt(s) in GeV
    s = E ** 2
    alpha = 1 / 137.036
    sig = 4 * math.pi * alpha ** 2 / (3 * s) * 0.3894e6  # GeV^-2 -> nb (0.3894 mb = 0.3894e6 nb)
    ax.plot(E, sig, color=INK, lw=1.8)
    ax.set_yscale("log"); ax.set_xlabel("√s  (GeV)"); ax.set_ylabel("σ(e⁺e⁻ → μ⁺μ⁻)  (nb)")
    ax.text(14, sig[100] * 2.2, "σ = 4πα²/(3s) ≈ 86.8 nb / s[GeV²]", fontsize=9, color=BLUE)
    ax.set_title("Falling with energy: the lowest-order QED prediction", fontsize=10); return fig


def loop_vp(ax, x0, y0, s=1.0, lab=True):
    c = (x0 + 1.1 * s, y0)
    photon(ax, (x0, y0), (c[0] - 0.4 * s, y0)); photon(ax, (c[0] + 0.4 * s, y0), (x0 + 2.2 * s, y0))
    fermion_arc(ax, c, 0.4 * s, 0, 180, arrow_at=90, ccw=False); fermion_arc(ax, c, 0.4 * s, 180, 360, arrow_at=270, ccw=False)
    vertex(ax, (c[0] - 0.4 * s, y0)); vertex(ax, (c[0] + 0.4 * s, y0))
    if lab:
        label(ax, (c[0], y0 + 0.55 * s), "k", size=9, color=BLUE); label(ax, (c[0], y0 - 0.58 * s), "k − q", size=9, color=BLUE)
        label(ax, (x0, y0), "q", dx=-0.12, size=9)


def loop_se(ax, x0, y0, s=1.0, lab=True):
    a, b = (x0 + 0.6 * s, y0), (x0 + 1.6 * s, y0)
    fermion(ax, (x0, y0), a); fermion(ax, a, b); fermion(ax, b, (x0 + 2.2 * s, y0))
    photon_arc(ax, ((a[0] + b[0]) / 2, y0), 0.5 * s, 0, 180, waves=7)
    vertex(ax, a); vertex(ax, b)
    if lab:
        label(ax, ((a[0] + b[0]) / 2, y0 + 0.68 * s), "k", size=9, color=BLUE); label(ax, ((a[0] + b[0]) / 2, y0 - 0.2 * s), "p − k", size=9, color=BLUE)
        label(ax, (x0, y0), "p", dx=-0.12, size=9)


def loop_vx(ax, x0, y0, s=1.0, lab=True, ext="γ(q)"):
    top = (x0 + 1.1 * s, y0 - 0.1 * s)
    a, b = (x0 + 0.55 * s, y0 + 0.75 * s), (x0 + 1.65 * s, y0 + 0.75 * s)
    fermion(ax, (x0, y0 + 1.15 * s), a); fermion(ax, a, top); fermion(ax, top, b); fermion(ax, b, (x0 + 2.2 * s, y0 + 1.15 * s))
    photon(ax, a, b, amp=0.05); photon(ax, top, (top[0], y0 - 0.8 * s), amp=0.05)
    for v in (a, b, top):
        vertex(ax, v)
    if lab:
        label(ax, ((a[0] + b[0]) / 2, a[1] + 0.2 * s), "k", size=9, color=BLUE)
        label(ax, (top[0], y0 - 0.8 * s), ext, dy=-0.15, size=9)
        label(ax, (x0, y0 + 1.15 * s), "p", dx=-0.12, size=9); label(ax, (x0 + 2.2 * s, y0 + 1.15 * s), "p′", dx=0.14, size=9)


@fig("L62_topologies.png")
def _():
    fig, ax = new(6.8, 2.3)
    loop_vp(ax, 0.0, 0.5, 0.95); loop_se(ax, 2.35, 0.3, 0.95); loop_vx(ax, 4.65, 0.0, 0.95)
    label(ax, (1.05, -0.45), "vacuum polarization Π(q²)", size=8.5); label(ax, (3.4, -0.45), "self-energy Σ(p)", size=8.5)
    label(ax, (5.7, -1.3), "vertex correction Γ^μ", size=8.5)
    frame(ax, -0.3, 7.0, -1.45, 1.4); return fig


@fig("L63_vp.png")
def _():
    fig, ax = new(5.0, 1.8)
    loop_vp(ax, 0.0, 0.0, 1.2)
    ax.text(3.0, 0.3, "iΠ^μν(q) = −e² ∫ d⁴k/(2π)⁴ ×", fontsize=8.5); ax.text(3.0, -0.05, "Tr[γ^μ(k̸+m)γ^ν(k̸−q̸+m)] / […]", fontsize=8.5)
    ax.text(3.0, -0.45, "minus sign: closed fermion loop", fontsize=8.5, color=BLUE)
    frame(ax, -0.3, 6.2, -0.75, 0.8); return fig


@fig("L64_se.png")
def _():
    fig, ax = new(5.0, 1.6)
    loop_se(ax, 0.0, 0.0, 1.2)
    ax.text(3.0, 0.3, "Σ(p) = −ie² ∫ d⁴k/(2π)⁴ ×", fontsize=8.5); ax.text(3.0, -0.05, "γ^μ(p̸−k̸+m)γ_μ / [((p−k)²−m²)k²]", fontsize=8.5)
    ax.text(3.0, -0.4, "shifts the pole: m₀ → physical m", fontsize=8.5, color=BLUE)
    frame(ax, -0.3, 6.2, -0.6, 0.9); return fig


@fig("L65_vertex.png")
def _():
    fig, ax = new(5.0, 2.4)
    loop_vx(ax, 0.0, 0.0, 1.2)
    ax.text(3.0, 1.0, "Γ^μ = γ^μ + δΓ^μ(p′, p)", fontsize=9.5, color=BLUE)
    ax.text(3.0, 0.55, "internal lines: p − k, p′ − k, k", fontsize=8.5)
    ax.text(3.0, 0.15, "on shell:", fontsize=8.5)
    ax.text(3.0, -0.25, "F₁(q²) γ^μ + F₂(q²) iσ^{μν}q_ν / 2m", fontsize=8.5)
    frame(ax, -0.4, 6.2, -1.25, 1.65); return fig


@fig("L66_powercount.png")
def _():
    fig, ax = new(6.8, 2.6)
    loop_vp(ax, 0.0, 1.4, 0.7, lab=False); loop_se(ax, 2.3, 1.3, 0.7, lab=False); loop_vx(ax, 4.6, 0.8, 0.7, lab=False, ext="")
    for x, t1, t2 in [(0.75, "E_γ = 2, E_e = 0", "D = 2"), (3.05, "E_γ = 0, E_e = 2", "D = 1"), (5.35, "E_γ = 1, E_e = 2", "D = 0")]:
        ax.text(x, 0.25, t1, ha="center", fontsize=8.5); ax.text(x, -0.15, t2, ha="center", fontsize=9, color=BLUE)
    ax.text(0, -0.65, "Superficial degree D = 4 − E_γ − (3/2)E_e; gauge and Lorentz symmetry soften the actual divergences to logarithms", fontsize=9.5, color=BLUE)
    frame(ax, -0.3, 7.2, -0.8, 2.0); return fig


@fig("L67_wick.png")
def _():
    fig, ax = new(5.6, 2.6, axis=True)
    ax.axhline(0, color=GREY, lw=0.8); ax.axvline(0, color=GREY, lw=0.8)
    ax.plot([1.2], [-0.15], "x", color=RED, ms=8, mew=2); ax.plot([-1.2], [0.15], "x", color=RED, ms=8, mew=2)
    ax.annotate("", xy=(0.05, 1.4), xytext=(1.9, 0.05), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.4, connectionstyle="arc3,rad=0.3"))
    ax.annotate("", xy=(-0.05, -1.4), xytext=(-1.9, -0.05), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.4, connectionstyle="arc3,rad=0.3"))
    ax.text(0.15, 1.2, "k⁰ = i k⁴", color=BLUE, fontsize=9)
    ax.text(-2.35, -2.35, "Rotate the k⁰ contour 90° anticlockwise without crossing a pole:\nMinkowski k² = −k_E², and 'large k' becomes an ordinary 4-sphere.", fontsize=8.5)
    ax.set_xlim(-2.4, 2.4); ax.set_ylim(-2.6, 1.6); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("Re k⁰"); ax.set_ylabel("Im k⁰"); ax.set_aspect("auto"); return fig


@fig("L68_counterterms.png")
def _():
    fig, ax = new(6.6, 1.4)
    loop_se(ax, 0.0, 0.0, 0.8, lab=False)
    label(ax, (2.05, 0.0), "+", size=15)
    fermion(ax, (2.3, 0), (3.1, 0)); fermion(ax, (3.1, 0), (3.9, 0)); cross(ax, (3.1, 0))
    label(ax, (3.1, -0.3), "δm, δ₂ counterterm", size=8.5)
    label(ax, (4.2, 0.0), "=", size=15)
    ax.text(4.45, 0.08, "finite, with the pole at\nthe measured mass m", fontsize=9, va="center", color=BLUE)
    frame(ax, -0.3, 6.6, -0.5, 0.6); return fig


@fig("L69_running.png")
def _():
    fig, ax = plt.subplots(figsize=(5.4, 2.8))
    a0 = 1 / 137.036
    me = 0.000511
    Q = np.logspace(math.log10(me * 3), 2.0, 300)  # GeV
    L = np.log(Q ** 2 / (math.exp(5 / 3) * me ** 2))
    a = a0 / (1 - a0 / (3 * math.pi) * L)
    ax.semilogx(Q, 1 / a, color=INK, lw=1.8, label="electron loop only (this course)")
    ax.axhline(137.036, color=GREY, lw=0.8, ls=":")
    ax.plot([91.19], [127.95], "o", color=RED); ax.text(0.02, 128.3, "measured 1/α(M_Z) ≈ 128 (all charged fermions; Lesson 87) →", fontsize=8.5, color=RED)
    ax.set_xlabel("momentum transfer Q (GeV)"); ax.set_ylabel("1/α_eff(Q)")
    ax.legend(frameon=False, fontsize=8.5, loc="lower left"); ax.set_ylim(126.5, 138)
    ax.set_title("The charge grows at short distance (large Q)", fontsize=10); return fig


@fig("L69_dyson.png")
def _():
    fig, ax = new(6.8, 1.0)
    x = 0.0
    photon(ax, (x, 0), (x + 0.7, 0)); x += 0.95; label(ax, (x - 0.12, 0), "+", size=13)
    photon(ax, (x, 0), (x + 0.3, 0)); ax.add_patch(Circle((x + 0.48, 0), 0.18, fc="#EAF2F8", ec=INK)); label(ax, (x + 0.48, 0), "Π", size=8)
    photon(ax, (x + 0.66, 0), (x + 0.96, 0)); x += 1.2; label(ax, (x - 0.12, 0), "+", size=13)
    photon(ax, (x, 0), (x + 0.25, 0)); ax.add_patch(Circle((x + 0.43, 0), 0.18, fc="#EAF2F8", ec=INK)); label(ax, (x + 0.43, 0), "Π", size=8)
    photon(ax, (x + 0.61, 0), (x + 0.86, 0)); ax.add_patch(Circle((x + 1.04, 0), 0.18, fc="#EAF2F8", ec=INK)); label(ax, (x + 1.04, 0), "Π", size=8)
    photon(ax, (x + 1.22, 0), (x + 1.47, 0)); x += 1.7; label(ax, (x - 0.1, 0), "+ ⋯ =", size=12, ha="left")
    ax.text(x + 0.55, 0, "−ig_μν / [q²(1 − Π̂(q²))]", fontsize=10, va="center", color=BLUE)
    frame(ax, -0.1, 7.6, -0.3, 0.3); return fig


@fig("L70_beta.png")
def _():
    fig, ax = plt.subplots(figsize=(5.4, 2.6))
    e = np.linspace(0, 1.2, 200)
    ax.plot(e, e ** 3 / (12 * math.pi ** 2), color=INK, lw=1.8)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.set_xlabel("e"); ax.set_ylabel("β(e) = μ de/dμ")
    ax.text(0.05, 0.011, "β = e³/(12π²) > 0 for one lepton:\ne grows slowly as μ rises", fontsize=9, color=BLUE)
    ax.set_title("One-loop QED beta function", fontsize=10); return fig


@fig("L71_gauge_orbits.png")
def _():
    fig, ax = new(5.6, 2.8)
    for i in range(5):
        y = i * 0.45
        xs = np.linspace(0, 3.2, 100)
        ax.plot(xs, y + 0.15 * np.sin(1.6 * xs + i), color=GREY, lw=1.2)
        ax.text(3.3, y + 0.15 * math.sin(1.6 * 3.2 + i), "A + ∂λ", fontsize=7.5, color=GREY, va="center")
    xs = np.linspace(-0.1, 2.1, 50)
    ax.plot(1.4 + 0.25 * np.sin(2 * xs), xs, color=BLUE, lw=2.2)
    ax.text(1.75, 2.15, "gauge-fixing slice ∂·A = 0\n(one representative per orbit)", fontsize=8.5, color=BLUE)
    ax.text(-0.1, -0.45, "Each grey curve is one physical field configuration (an orbit of gauge copies).", fontsize=8.5)
    frame(ax, -0.2, 5.0, -0.6, 2.6); return fig


@fig("L72_ward.png")
def _():
    fig, ax = new(6.6, 2.1)
    for x0, ch in [(0.0, "s"), (2.9, "u")]:
        a, b = (x0 + 0.6, 0.3), (x0 + 1.4, 0.3)
        fermion(ax, (x0, 0.3), a); fermion(ax, a, b); fermion(ax, b, (x0 + 2.0, 0.3)); vertex(ax, a); vertex(ax, b)
        if ch == "s":
            photon(ax, (x0 + 0.1, 1.2), a); photon(ax, b, (x0 + 1.9, 1.2))
        else:
            photon(ax, (x0 + 0.1, 1.2), b); photon(ax, a, (x0 + 1.9, 1.2))
        label(ax, (x0 + 0.1, 1.2), "ε → k", dy=0.14, size=9, color=RED)
    label(ax, (2.45, 0.6), "+", size=15); label(ax, (5.15, 0.6), "= 0", size=13, ha="left")
    ax.text(0, -0.35, "Replace one photon's polarization ε_μ(k) by k_μ: the diagrams cancel in the sum, k_μℳ^μ = 0.", fontsize=8.5)
    frame(ax, -0.2, 6.4, -0.5, 1.5); return fig


@fig("L73_map.png")
def _():
    fig, ax = new(6.8, 2.6)
    nodes = {"loc": (0.9, 1.6, "local U(1)\nphase freedom"), "cov": (3.0, 1.6, "covariant derivative\nD_μ = ∂_μ + ieA_μ"),
             "ward": (5.4, 1.6, "Ward identity\nk_μℳ^μ = 0"), "xi": (0.9, 0.0, "ξ drops out\nof the S-matrix"),
             "mass": (3.0, 0.0, "photon stays\nmassless"), "z": (5.4, 0.0, "Z₁ = Z₂: charge\nis universal")}
    for k, (x, y, t) in nodes.items():
        ax.add_patch(matplotlib.patches.FancyBboxPatch((x - 0.85, y - 0.32), 1.7, 0.64, boxstyle="round,pad=0.03", fc="#EAF2F8", ec=BLUE))
        ax.text(x, y, t, ha="center", va="center", fontsize=8)
    for a, b in [("loc", "cov"), ("cov", "ward"), ("ward", "z"), ("ward", "mass"), ("ward", "xi")]:
        xa, ya, _ = nodes[a]; xb, yb, _ = nodes[b]
        if ya == yb:
            arrow(ax, xa + 0.87, ya, xb - 0.87, yb, color=BLUE, lw=1.1, head=8)
        else:
            arrow(ax, xa, ya - 0.34, xb + (0.0 if xa == xb else (0.6 if xb < xa else -0.6)), yb + 0.34, color=BLUE, lw=1.1, head=8)
    frame(ax, -0.1, 6.4, -0.45, 2.05); return fig


@fig("L74_ir.png")
def _():
    fig, ax = new(6.6, 2.2)
    loop_vx(ax, 0.0, 0.0, 0.9, lab=False, ext="γ*")
    label(ax, (1.0, -1.05), "virtual soft photon:\n−(α/π)·log(…)·log(1/λ)", size=8.5)
    label(ax, (2.5, 0.3), "+", size=15)
    x0 = 3.0
    top = (x0 + 1.0, 0.0)
    fermion(ax, (x0, 1.0), top); fermion(ax, top, (x0 + 2.0, 1.0)); photon(ax, top, (top[0], -0.8), amp=0.05); vertex(ax, top)
    photon(ax, (x0 + 1.6, 0.7), (x0 + 2.1, 1.5), amp=0.04, waves=4); vertex(ax, (x0 + 1.6, 0.7))
    label(ax, (x0 + 2.2, 1.45), "real soft γ\n(ω < ΔE)", size=8.5, ha="left")
    label(ax, (x0 + 1.0, -1.05), "real emission:\n+(α/π)·log(…)·log(ΔE/λ)", size=8.5)
    ax.text(0.0, -1.7, "λ (photon mass regulator) cancels in the sum; only the detector resolution ΔE remains.", fontsize=8.5, color=BLUE)
    frame(ax, -0.3, 6.9, -1.85, 1.75); return fig


@fig("L75_soft.png")
def _():
    fig, ax = new(6.6, 2.0)
    for x0, after in [(0.0, True), (3.4, False)]:
        h = (x0 + 1.2, 0.5)
        ax.add_patch(Circle(h, 0.18, fc="#EAF2F8", ec=INK, zorder=4)); label(ax, h, "hard", size=7)
        fermion(ax, (x0, 0.5), (h[0] - 0.18, 0.5)); fermion(ax, (h[0] + 0.18, 0.5), (x0 + 2.6, 0.5))
        e = (x0 + 1.95, 0.5) if after else (x0 + 0.5, 0.5)
        photon(ax, e, (e[0] + 0.45, 1.25), amp=0.04, waves=4); vertex(ax, e)
        label(ax, (e[0] + 0.5, 1.4), "γ(k), k → 0", size=8.5)
        label(ax, (x0 + 1.3, -0.05), ["after the hard process: 1/(p′·k)", "before it: 1/(p·k)"][0 if after else 1], size=8.5)
    ax.text(0, -0.5, "Soft factor e(p′·ε/p′·k − p·ε/p·k): the photon sees only the charge and the direction of each leg.", fontsize=8.5, color=BLUE)
    frame(ax, -0.2, 6.6, -0.7, 1.6); return fig


@fig("L76_g2.png")
def _():
    fig, ax = new(6.4, 2.4)
    loop_vx(ax, 0.0, 0.0, 1.1, ext="B (external field)")
    ax.text(2.9, 1.2, "g = 2 (Dirac)  →  g = 2(1 + a)", fontsize=10, color=BLUE)
    ax.text(2.9, 0.75, "a = F₂(0) = α/(2π) ≈ 0.00116 (Schwinger, 1948)", fontsize=9)
    ax.text(2.9, 0.3, "measured a_e = 0.001 159 652 180 59(13)", fontsize=9)
    ax.text(2.9, -0.1, "(Harvard 2023; the full theory needs ~5 loops)", fontsize=8)
    frame(ax, -0.3, 6.8, -1.25, 1.55); return fig


@fig("L77_lamb.png")
def _():
    fig, ax = new(5.6, 2.6)
    ax.plot([0, 1.4], [1.6, 1.6], color=INK, lw=2); ax.text(0.7, 1.75, "n = 2, j = 1/2 (Dirac)", ha="center", fontsize=8.5)
    ax.plot([2.4, 3.8], [1.85, 1.85], color=INK, lw=2); ax.text(4.0, 1.85, "2s₁/₂", va="center", fontsize=9)
    ax.plot([2.4, 3.8], [1.35, 1.35], color=INK, lw=2); ax.text(4.0, 1.35, "2p₁/₂", va="center", fontsize=9)
    ax.plot([1.4, 2.4], [1.6, 1.85], color=GREY, lw=0.8, ls="--"); ax.plot([1.4, 2.4], [1.6, 1.35], color=GREY, lw=0.8, ls="--")
    arrow(ax, 3.1, 1.37, 3.1, 1.83, color=RED, lw=1.2, head=7); arrow(ax, 3.1, 1.83, 3.1, 1.37, color=RED, lw=1.2, head=7)
    ax.text(3.2, 1.6, "1057.8 MHz", color=RED, fontsize=9, va="center")
    ax.text(0, 0.75, "Self-energy (Bethe's log) ≈ +1017 MHz on 2s     vertex/anomalous moment ≈ +68 MHz", fontsize=8)
    ax.text(0, 0.4, "Vacuum polarization (Uehling) ≈ −27 MHz            (rounded; Lessons 77–78)", fontsize=8)
    ax.text(0, 0.0, "Scale not to proportion; energies grow upward.", fontsize=8, color=GREY)
    frame(ax, -0.1, 5.4, -0.15, 2.05); return fig


@fig("L78_uehling.png")
def _():
    from scipy import integrate
    fig, ax = plt.subplots(figsize=(5.4, 2.7))
    a = 1 / 137.036
    r = np.linspace(0.05, 2.0, 120)  # in units of the Compton wavelength 1/m

    def U(x):
        f = lambda t: math.exp(-2 * x * t) * (1 + 1 / (2 * t * t)) * math.sqrt(t * t - 1) / (t * t)
        v, _ = integrate.quad(f, 1, np.inf)
        return 1 + 2 * a / (3 * math.pi) * v
    y = np.array([U(x) for x in r])
    ax.plot(r, (y - 1) * 1e3, color=INK, lw=1.8)
    ax.set_xlabel("distance r  (units of the electron Compton wavelength ħ/mc)")
    ax.set_ylabel("(Q_eff(r)/Q − 1) × 10³")
    ax.set_title("Uehling: the charge looks larger inside the screening cloud", fontsize=10); return fig


@fig("L79_map.png")
def _():
    fig, ax = new(6.8, 2.8)
    left = [("vertex correction", 2.0), ("self-energy", 1.3), ("vacuum polarization", 0.6), ("hadronic & weak loops", -0.1)]
    right = [("electron g − 2", 2.0), ("hydrogen Lamb shift", 1.3), ("muonic hydrogen", 0.6), ("muon g − 2", -0.1)]
    for t, y in left:
        ax.add_patch(matplotlib.patches.FancyBboxPatch((0, y - 0.22), 1.9, 0.44, boxstyle="round,pad=0.02", fc="#EAF2F8", ec=BLUE)); ax.text(0.95, y, t, ha="center", va="center", fontsize=8.5)
    for t, y in right:
        ax.add_patch(matplotlib.patches.FancyBboxPatch((4.2, y - 0.22), 1.9, 0.44, boxstyle="round,pad=0.02", fc="#F7F7F7", ec=INK)); ax.text(5.15, y, t, ha="center", va="center", fontsize=8.5)
    links = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (0, 3), (3, 3), (3, 0)]
    for i, j in links:
        arrow(ax, 1.92, left[i][1], 4.18, right[j][1], color=GREY, lw=0.9, head=7)
    ax.text(0, -0.65, "Which loop corrections feed which precision test (dominant links only).", fontsize=8.5)
    frame(ax, -0.1, 6.3, -0.8, 2.4); return fig


@fig("Mead_AB.png")
def _():
    fig, ax = new(5.8, 2.2)
    ax.plot([0], [0.8], "o", color=INK); label(ax, (0, 0.8), "source", dx=-0.1, ha="right", size=9)
    xs = np.linspace(0, 4, 200)
    ax.plot(xs, 0.8 + 0.6 * np.sin(math.pi * xs / 4), color=INK, lw=1.6); ax.plot(xs, 0.8 - 0.6 * np.sin(math.pi * xs / 4), color=INK, lw=1.6, ls="--")
    ax.add_patch(Circle((2, 0.8), 0.22, fc="#EAF2F8", ec=BLUE, lw=1.4)); label(ax, (2, 0.8), "Φ", color=BLUE, size=10)
    ax.plot([4.2, 4.2], [0.0, 1.6], color=GREY, lw=3); label(ax, (4.35, 0.8), "screen:\nfringes shift\nby eΦ/ħ", ha="left", size=8.5)
    ax.text(0.3, -0.25, "B = 0 on both paths; only the potential A around the shielded solenoid differs.", fontsize=8.5)
    frame(ax, -0.9, 5.6, -0.45, 1.65); return fig


@fig("L52_trace.png")
def _():
    fig, ax = new(6.8, 1.3)
    flow(ax, ["ū(p′)γ^μ u(p)", "× its conjugate\nū(p)γ^ν u(p′)", "sum spins:\nΣuū = p̸ + m", "Tr[(p̸′+m)γ^μ\n(p̸+m)γ^ν]"], w=1.6)
    frame(ax, -0.1, 7.4, -0.45, 0.45); return fig


@fig("L59_cm.png")
def _():
    fig, ax = new(5.6, 2.6)
    o = (1.6, 1.0)
    ax.add_patch(Circle(o, 0.95, fill=False, ls="--", color=GREY))
    arrow(ax, o[0] - 1.5, o[1], o[0] - 0.05, o[1], lw=1.4); arrow(ax, o[0] + 1.5, o[1], o[0] + 0.05, o[1], lw=1.4, color=GREY)
    t = math.radians(40)
    arrow(ax, o[0], o[1], o[0] + 0.95 * math.cos(t), o[1] + 0.95 * math.sin(t), lw=1.6, color=BLUE)
    arrow(ax, o[0], o[1], o[0] - 0.95 * math.cos(t), o[1] - 0.95 * math.sin(t), lw=1.6, color=BLUE)
    ax.add_patch(matplotlib.patches.Wedge(o, 0.95, 34, 46, color=BLUE, alpha=0.25))
    ax.text(o[0] + 1.0, o[1] + 0.85, "dΩ", color=BLUE, fontsize=9)
    ax.text(3.4, 1.5, "CM frame: |p_f| fixed by energy,", fontsize=9)
    ax.text(3.4, 1.15, "only the direction is free", fontsize=9)
    ax.text(3.4, 0.6, "dσ/dΩ = |ℳ|² / (64π² s)", fontsize=11, color=BLUE)
    frame(ax, -0.1, 6.6, -0.1, 2.1); return fig


@fig("L61_angular.png")
def _():
    fig, ax = plt.subplots(figsize=(5.6, 2.9))
    th = np.linspace(0.05, math.pi - 0.05, 400)
    c = np.cos(th)
    emu = 8 * (1 + (1 + c) ** 2 / 4) / (1 - c) ** 2
    ann = 2 * ((1 - c) / (1 + c) + (1 + c) / (1 - c))
    comp = 4 / (1 + c) + (1 + c)
    ax.semilogy(np.degrees(th), emu, color=INK, lw=1.8, label="e⁻μ⁻ → e⁻μ⁻: 2(s² + u²)/t²")
    ax.semilogy(np.degrees(th), ann, color=INK, lw=1.6, ls="--", label="e⁺e⁻ → γγ: 2(t/u + u/t)")
    ax.semilogy(np.degrees(th), comp, color=INK, lw=1.6, ls=":", label="Compton: −2(s/u + u/s)")
    ax.set_xlabel("CM scattering angle θ (degrees)"); ax.set_ylabel("(1/4)Σ|ℳ|² / e⁴")
    ax.set_xlim(0, 180); ax.legend(frameon=False, fontsize=8)
    ax.set_title("High-energy limit: photon pole at t → 0, fermion poles at u → 0 or t → 0", fontsize=9)
    return fig


CORE_TRACK = [1, 3, 4, 5, 7, 8, 10, 12, 18, 20, 21, 22, 23, 26, 28, 33, 36, 38, 39, 42,
              45, 46, 47, 48, 50, 52, 53, 54, 57, 59, 62, 63, 67, 68, 69]
PARTS = [("0", "Prologues", 0, 0), ("I", "Prerequisites", 1, 9), ("II", "Quantum mechanics", 10, 17),
         ("III", "Relativistic QM", 18, 24), ("IV", "Classical fields", 25, 31), ("V", "Quantum fields", 32, 38),
         ("VI", "QED", 39, 45), ("VII", "Feynman diagrams", 46, 53), ("VIII", "Real calculations", 54, 61),
         ("IX", "Quantum corrections", 62, 70), ("X", "Deep QED", 71, 79), ("XI", "Beyond", 80, 87)]


@fig("Front_route.png")
def _():
    fig, ax = new(6.6, 4.4)
    y = 11.5; X0 = 6.4; DX = 0.5; SQ = 0.42
    def sq(x, y, txt, core):
        ax.add_patch(Rectangle((x, y - SQ / 2), SQ, SQ, facecolor=BLUE if core else "white", edgecolor=INK, lw=0.6))
        ax.text(x + SQ / 2, y, txt, fontsize=5.5, ha="center", va="center", color="white" if core else INK)
    for num, name, a, b in PARTS:
        ax.text(0.0, y, f"Part {num}", fontsize=7.5, weight="bold", va="center")
        ax.text(1.95, y, name, fontsize=7.5, va="center")
        if a == 0:
            for i in range(1, 10):
                sq(X0 + (i - 1) * DX, y, f"P{i}", i <= 6)
        else:
            for i in range(a, b + 1):
                sq(X0 + (i - a) * DX, y, str(i), i in CORE_TRACK)
        y -= 0.85
    sq(X0, y, "", True); ax.text(X0 + 0.6, y, "core track: Prologues 1–6 + 35 lessons", fontsize=7.5, va="center")
    sq(X0, y - 0.6, "", False); ax.text(X0 + 0.6, y - 0.6, "rest of the full course", fontsize=7.5, va="center")
    frame(ax, -0.1, 11.6, y - 1.0, 12.0); return fig


if __name__ == "__main__":
    import sys
    want = sys.argv[1:]
    for name, f in FIGS.items():
        if (want and name not in want) or name.startswith("_"):
            continue
        save(f(), name)
        print("wrote", name)
