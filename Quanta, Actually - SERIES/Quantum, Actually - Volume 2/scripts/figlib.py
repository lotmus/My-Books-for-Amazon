# -*- coding: utf-8 -*-
"""Drawing primitives for the QED Course figures (matplotlib, 300 dpi PNG).
Arrows ("stopwatch hands"), Feynman-diagram lines, and small helpers.
Lines are dark and distinguished by style as well as colour, so the figures
survive black-and-white print."""
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, Arc
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "figures")
INK = "#1a1a1a"
BLUE = "#1F4E78"
RED = "#B03030"
GREEN = "#2E7D32"
GREY = "#777777"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "mathtext.fontset": "dejavusans",
    "axes.linewidth": 0.8, "savefig.dpi": 300,
})


import re as _re
from matplotlib.axes import Axes as _Axes

_SUBSUP = _re.compile(r"([_^])(\{[^}]*\}|[A-Za-z0-9μνρσαβλκγ*′]+)")


def mt(text):
    """Turn X_ab and Y^μν into real sub/superscripts (mathtext), unless the
    string already uses $...$."""
    if not isinstance(text, str) or "$" in text or ("_" not in text and "^" not in text):
        return text
    def rep(m):
        body = m.group(2).strip("{}")
        body = body.replace("*", r"\ast").replace("′", r"\prime")
        return "$%s{\\mathregular{%s}}$" % (m.group(1), body)
    return _SUBSUP.sub(rep, text)


_orig_text = _Axes.text


def _text(self, x, y, s, *a, **k):
    return _orig_text(self, x, y, mt(s), *a, **k)


_Axes.text = _text


def new(w=6.0, h=3.0, axis=False):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_aspect("equal")
    if not axis:
        ax.axis("off")
    return fig, ax


def save(fig, name):
    os.makedirs(OUT, exist_ok=True)
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", pad_inches=0.06, facecolor="white")
    plt.close(fig)
    return name


# ------------------------------------------------------------ arrows
def arrow(ax, x0, y0, x1, y1, color=INK, lw=2.0, ls="-", head=12, alpha=1.0, z=3):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=head,
                        color=color, lw=lw, ls=ls, alpha=alpha, zorder=z, shrinkA=0, shrinkB=0)
    ax.add_patch(a)
    return x1, y1


def polar_arrow(ax, x0, y0, length, angle_deg, **kw):
    t = math.radians(angle_deg)
    return arrow(ax, x0, y0, x0 + length * math.cos(t), y0 + length * math.sin(t), **kw)


def stopwatch(ax, cx, cy, r, angle_deg, label=None, color=INK, hand=0.85):
    """A clock face with one hand; angle measured like a clock (0 = 12 o'clock, clockwise)."""
    ax.add_patch(Circle((cx, cy), r, fill=False, lw=1.2, color=GREY))
    for k in range(12):
        t = math.radians(90 - 30 * k)
        ax.plot([cx + 0.86 * r * math.cos(t), cx + r * math.cos(t)],
                [cy + 0.86 * r * math.sin(t), cy + r * math.sin(t)], color=GREY, lw=0.8)
    t = math.radians(90 - angle_deg)
    arrow(ax, cx, cy, cx + hand * r * math.cos(t), cy + hand * r * math.sin(t), color=color, lw=2.2)
    ax.add_patch(Circle((cx, cy), 0.04 * r + 0.01, color=INK, zorder=4))
    if label:
        ax.text(cx, cy - r - 0.12, label, ha="center", va="top", fontsize=9)


# ------------------------------------------------------------ Feynman lines
def fermion(ax, p, q, arrow_mid=True, color=INK, lw=1.6, reverse=False):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, solid_capstyle="round", zorder=2)
    if arrow_mid:
        a, b = (q, p) if reverse else (p, q)
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        dx, dy = b[0] - a[0], b[1] - a[1]
        n = math.hypot(dx, dy)
        dx, dy = dx / n * 0.001, dy / n * 0.001
        ax.annotate("", xy=(mx + dx * 60, my + dy * 60), xytext=(mx - dx * 60, my - dy * 60),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=13, shrinkA=0, shrinkB=0), zorder=3)


def photon(ax, p, q, amp=0.06, waves=None, color=INK, lw=1.4):
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    if waves is None:
        waves = max(3, int(L / 0.16))
    t = np.linspace(0, 1, 400)
    nx, ny = -dy / L, dx / L
    s = amp * np.sin(2 * math.pi * waves * t)
    ax.plot(p[0] + dx * t + nx * s, p[1] + dy * t + ny * s, color=color, lw=lw, zorder=2)


def photon_arc(ax, c, r, t0, t1, amp=0.05, waves=8, color=INK, lw=1.4):
    t = np.linspace(math.radians(t0), math.radians(t1), 500)
    rr = r + amp * np.sin(waves * 2 * math.pi * (t - t[0]) / (t[-1] - t[0]))
    ax.plot(c[0] + rr * np.cos(t), c[1] + rr * np.sin(t), color=color, lw=lw, zorder=2)


def fermion_arc(ax, c, r, t0, t1, color=INK, lw=1.6, arrow_at=None, ccw=True):
    t = np.linspace(math.radians(t0), math.radians(t1), 300)
    ax.plot(c[0] + r * np.cos(t), c[1] + r * np.sin(t), color=color, lw=lw, zorder=2)
    if arrow_at is not None:
        a = math.radians(arrow_at)
        d = 0.02 if ccw else -0.02
        p0 = (c[0] + r * math.cos(a - d), c[1] + r * math.sin(a - d))
        p1 = (c[0] + r * math.cos(a + d), c[1] + r * math.sin(a + d))
        ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                    mutation_scale=13, shrinkA=0, shrinkB=0), zorder=3)


def vertex(ax, p, r=0.035, color=INK):
    ax.add_patch(Circle(p, r, color=color, zorder=5))


def cross(ax, p, s=0.07, color=INK):
    ax.plot([p[0] - s, p[0] + s], [p[1] - s, p[1] + s], color=color, lw=1.8, zorder=5)
    ax.plot([p[0] - s, p[0] + s], [p[1] + s, p[1] - s], color=color, lw=1.8, zorder=5)


def label(ax, p, s, dx=0, dy=0, size=10, color=INK, **kw):
    ax.text(p[0] + dx, p[1] + dy, s, fontsize=size, color=color, ha=kw.pop("ha", "center"),
            va=kw.pop("va", "center"), **kw)


def mom(ax, p, q, s, off=0.14, color=BLUE, size=9):
    """Momentum-flow arrow drawn beside a line from p to q, labelled s."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    nx, ny = -dy / L * off, dx / L * off
    a = (p[0] + 0.3 * dx + nx, p[1] + 0.3 * dy + ny)
    b = (p[0] + 0.7 * dx + nx, p[1] + 0.7 * dy + ny)
    arrow(ax, a[0], a[1], b[0], b[1], color=color, lw=1.0, head=8)
    ax.text((a[0] + b[0]) / 2 + nx * 1.1, (a[1] + b[1]) / 2 + ny * 1.1, s, color=color,
            fontsize=size, ha="center", va="center")


def frame(ax, x0, x1, y0, y1):
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
