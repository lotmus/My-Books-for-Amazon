# Spacetime diagrams for "The Universe Has No Now" (added 3 Oct 2026).
# Seven clean line diagrams, grayscale-safe (meaning never carried by color alone):
#   sd1 simultaneity, sd2 light cones, sd3 twin proper time, sd4 FLRW horizons (computed),
#   sd5 CTC vs ordinary delay, sd6 four kinds of elsewhere, sd7 foliation vs worldline.
#   fig46 (3 Oct 2026): Chapter 31 figure, liquid ranges of five solvents at 1 atm.
# Output: Figures/figs/sdN_*.png, 1800 x 1350 px (6 x 4.5 in at 300 dpi), RGB.
# Run:  python Figures\draw_spacetime_figs.py
import os, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyArrowPatch, Ellipse

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figs")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13, "axes.linewidth": 1.6,
                     "savefig.dpi": 300, "figure.dpi": 100})
K, G, LG = "black", "0.45", "0.85"

def fig(w=6, h=4.5):
    f = plt.figure(figsize=(w, h))
    return f

def save(f, name):
    p = os.path.join(OUT, name)
    f.savefig(p, dpi=300, facecolor="white")
    plt.close(f)
    # force RGB (Word dislikes RGBA/L PNGs in some builds)
    from PIL import Image
    im = Image.open(p).convert("RGB"); im.save(p, optimize=True)
    print("wrote", p, im.size)

def axes_st(ax, xl="space", yl="time", lim=1.0):
    ax.set_xlim(-lim, lim); ax.set_ylim(-0.12, lim * 1.02)
    ax.set_aspect("equal"); ax.axis("off")
    ax.annotate("", xy=(lim * 0.98, 0), xytext=(-lim * 0.98, 0), arrowprops=dict(arrowstyle="-|>", lw=1.6, color=K))
    ax.annotate("", xy=(0, lim * 0.98), xytext=(0, -0.08), arrowprops=dict(arrowstyle="-|>", lw=1.6, color=K))
    ax.text(lim * 0.97, -0.07, xl, ha="right", va="top", fontsize=12)
    ax.text(0.03, lim * 0.97, yl, ha="left", va="top", fontsize=12)

# ---------- SD1: relativity of simultaneity ----------
def sd1():
    f = fig(); ax = f.add_axes([0.02, 0.02, 0.96, 0.9])
    ax.set_xlim(-0.42, 1.95); ax.set_ylim(-0.55, 0.78); ax.set_aspect("equal"); ax.axis("off")
    # kitchen event at origin; Andromeda far to the right
    ax.plot([0, 0], [-0.5, 0.7], color=K, lw=3)                      # Mara: standing worldline
    v = 0.35
    ax.plot([-0.5 * v, 0.7 * v], [-0.5, 0.7], color=K, lw=3, ls=(0, (6, 3)))  # Eli: walking worldline
    ax.plot([-0.1, 1.55], [0, 0], color=K, lw=2)                      # Mara's now
    xs = np.array([-0.1, 1.55]); ax.plot(xs, v * xs, color=K, lw=2, ls=(0, (6, 3)))  # Eli's now (tilted)
    ax.plot([1.45, 1.45], [-0.5, 0.7], color=G, lw=2.5)               # Andromeda worldline
    ax.plot([0, 0.6], [0, 0.6], color=G, lw=1.5, ls=":"); ax.plot([0, 0.5], [0, -0.5], color=G, lw=1.5, ls=":")
    ax.plot(0, 0, "o", color=K, ms=9)
    ax.plot(1.45, 0, "s", color=K, ms=9); ax.plot(1.45, v * 1.45, "D", color=K, ms=9)
    ax.text(0.04, -0.06, "kitchen event\n(both here)", fontsize=11, va="top")
    ax.text(1.40, -0.04, "event on Andromeda\nin Mara's \u201cnow\u201d", ha="right", va="top", fontsize=11)
    ax.text(1.40, v * 1.45 + 0.03, "a later Andromeda event\nin Eli's \u201cnow\u201d", ha="right", va="bottom", fontsize=11)
    ax.text(-0.02, 0.66, "Mara\n(standing)", ha="right", fontsize=11)
    ax.text(0.7 * v + 0.03, 0.62, "Eli\n(walking)", ha="left", fontsize=11)
    ax.text(1.47, 0.66, "Andromeda", ha="left", fontsize=11, color=K)
    ax.text(0.47, -0.33, "light (45\u00b0)", fontsize=10, color=G, rotation=-45, ha="center", va="center")
    ax.text(0.8, -0.5, "solid line: Mara's slice of \u201cnow\u201d\ndashed line: Eli's slice of \u201cnow\u201d", fontsize=11)
    f.suptitle("Two walkers, one kitchen, two different \u201cnows\u201d far away", fontsize=14, y=0.97)
    save(f, "sd1_simultaneity.png")

# ---------- SD2: light cones ----------
def sd2():
    f = fig(); ax = f.add_axes([0.02, 0.02, 0.96, 0.92])
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.0, 1.0); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Polygon([[0, 0], [0.95, 0.95], [-0.95, 0.95]], closed=True, fc=LG, ec=K, lw=2.5))
    ax.add_patch(Polygon([[0, 0], [0.95, -0.95], [-0.95, -0.95]], closed=True, fc="white", ec=K, lw=2.5, hatch="//"))
    t = np.linspace(-0.9, 0.9, 50); ax.plot(0.18 * np.sin(2.2 * t), t, color=K, lw=3)  # a worldline inside the cones
    ax.plot(0, 0, "o", color=K, ms=10)
    ax.text(0, 0.62, "FUTURE\nyou can still affect it", ha="center", fontsize=12, weight="bold")
    ax.text(0, -0.72, "PAST\nit can have affected you", ha="center", fontsize=12, weight="bold",
            bbox=dict(fc="white", ec="none", pad=1))
    for sx in (-1, 1):
        ax.text(sx * 0.98, -0.12, "ELSEWHERE\nno signal either way;\nits order relative to\nyou depends on\nthe observer",
                ha="center", va="center", fontsize=10)
    ax.text(0.09, 0.07, "you, here, now", fontsize=11, ha="left", va="bottom")
    ax.text(0.55, 0.62, "light", rotation=45, fontsize=11)
    ax.text(0.2, -0.38, "your worldline", fontsize=10.5, bbox=dict(fc="white", ec="none", pad=1))
    f.suptitle("Light cones: the causal map every event carries", fontsize=14, y=0.98)
    save(f, "sd2_light_cones.png")

# ---------- SD3: twin proper time (v = 0.8c, 10 years home time) ----------
def sd3():
    f = fig(); ax = f.add_axes([0.03, 0.03, 0.94, 0.88])
    ax.set_xlim(-2.2, 6.5); ax.set_ylim(-0.6, 10.6); ax.axis("off")
    T, v = 10.0, 0.8; gam = 1 / math.sqrt(1 - v * v)
    ax.plot([0, 0], [0, T], color=K, lw=3)
    ax.plot([0, v * T / 2, 0], [0, T / 2, T], color=K, lw=3, ls=(0, (6, 3)))
    for k in range(1, 10):  # home ticks every year
        ax.plot([-0.12, 0.12], [k, k], color=K, lw=2)
    tau_tot = T / gam
    for k in range(1, int(round(tau_tot))):  # traveler ticks every proper year
        t = k * gam
        x = v * t if t <= T / 2 else v * (T - t)
        ax.plot([x - 0.14, x + 0.14], [t, t], color=K, lw=2)
    ax.plot(0, 0, "o", color=K, ms=9); ax.plot(0, T, "o", color=K, ms=9)
    ax.text(-0.2, 0, "parting", ha="right", va="center", fontsize=11)
    ax.text(-0.2, T, "meeting", ha="right", va="center", fontsize=11)
    ax.text(-0.25, 5.3, "stays home:\n10 ticks\n= 10 years", ha="right", fontsize=11)
    ax.text(4.25, 5.0, "travels at 0.8 c:\n6 ticks = 6 years", ha="left", fontsize=11)
    ax.text(3.0, 0.4, "each tick = one year\non that twin's own clock", fontsize=10.5, color=G)
    ax.annotate("", xy=(6.2, 10.2), xytext=(6.2, 0), arrowprops=dict(arrowstyle="-|>", lw=1.4))
    ax.text(6.05, 10.2, "time in the\nhome frame", ha="right", va="top", fontsize=10)
    f.suptitle("Same two meetings, different mileage: proper time", fontsize=14, y=0.97)
    save(f, "sd3_twin_proper_time.png")

# ---------- SD4: FLRW expansion and horizons (conformal diagram, computed) ----------
def sd4():
    H0, Om, Orad = 67.4, 0.315, 9.1e-5
    OL = 1 - Om - Orad
    c = 299792.458
    hub_gly = c / H0 * 3.2616e-3          # c/H0 in Gly (1 Mpc = 3.2616e-3 Gly)
    a = np.logspace(-8, 2.5, 200000)
    E = np.sqrt(Orad / a**4 + Om / a**3 + OL)
    deta = 1 / (a * a * E)                # d eta / da in units of c/H0
    eta = np.concatenate([[0], np.cumsum(0.5 * (deta[1:] + deta[:-1]) * np.diff(a))]) * hub_gly
    dt = 1 / (a * E)
    tcos = np.concatenate([[0], np.cumsum(0.5 * (dt[1:] + dt[:-1]) * np.diff(a))]) * hub_gly  # Gyr
    i0 = np.searchsorted(a, 1.0); eta0 = eta[i0]; eta_inf = eta[-1] + hub_gly * (1 / (a[-1] * math.sqrt(OL)))
    eh_now = eta_inf - eta0
    f = fig(); ax = f.add_axes([0.1, 0.12, 0.88, 0.8])
    ax.set_xlim(0, 70); ax.set_ylim(0, 70); ax.set_aspect("equal")
    ax.set_xlabel("comoving distance from us (billions of light-years)")
    ax.set_ylabel("conformal time (light then moves at 45\u00b0)")
    ax.plot([0, 0], [0, 66], color=K, lw=3)
    for x in (12, 24, 36, 48, 60):
        ax.plot([x, x], [0, 66], color=LG, lw=1.2)
    ax.plot([0, eta0], [eta0, 0], color=K, lw=2.5)                         # past light cone
    ax.plot([0, eh_now], [eta0, eta0 + eh_now], color=K, lw=2.5, ls=(0, (6, 3)))  # future light cone = event horizon
    ax.axhline(eta0, color=G, lw=1, ls=":")
    ax.plot([eta0], [0], "o", color=K)
    ax.plot([eh_now], [eta0], "s", color=K)
    rH = hub_gly / (a * E) * a / a          # comoving Hubble radius c/(aH) in Gly
    rH = hub_gly / (a * E)
    msk = (eta < 66)
    ax.plot(rH[msk], eta[msk], color=G, lw=2)
    # labels
    t0 = tcos[i0]
    ax.text(69, eta0 - 0.8, f"now: {t0:.1f} billion years\nafter the hot bang", fontsize=10, ha="right", va="top")
    ax.text(19.5, 28.0, "past light cone:\neverything we can see", fontsize=10, rotation=-45, ha="left", va="bottom", rotation_mode="anchor")
    ax.text(eta0 + 1.5, 1.0, f"particle horizon\n\u2248 {eta0:.0f} Gly today", fontsize=10)
    ax.text(eh_now + 1.5, eta0 + 0.5, f"dashed: our future light cone.\nEvent horizon \u2248 {eh_now:.0f} Gly today:\nlight we send now reaches\nonly galaxies inside it", fontsize=10, va="bottom")
    ax.text(9, 4, "gray curve:\nHubble distance", fontsize=10, color=K)
    ax.text(60, 28, "galaxies ride\nvertical lines", fontsize=10, ha="center", va="center", bbox=dict(fc="white", ec="none", pad=1))
    ax.text(eta_inf * 0, eta_inf + 0.0, "", fontsize=1)
    ax.axhline(eta_inf, color=K, lw=1.2, ls="--")
    ax.text(69, eta_inf + 0.8, "infinitely late cosmic time", ha="right", va="bottom", fontsize=9.5)
    f.suptitle("Expanding universe: what we see, what we can still reach", fontsize=13, y=0.985)
    save(f, "sd4_flrw_horizons.png")
    print(f"eta0={eta0:.2f} Gly, event horizon now={eh_now:.2f} Gly, eta_inf={eta_inf:.2f}, age={t0:.2f} Gyr")

# ---------- SD5: CTC vs ordinary delay ----------
def sd5():
    f = fig(); ax1 = f.add_axes([0.01, 0.02, 0.48, 0.86]); ax2 = f.add_axes([0.51, 0.02, 0.48, 0.86])
    for ax in (ax1, ax2):
        ax.set_xlim(-0.15, 1.15); ax.set_ylim(-0.3, 1.45); ax.set_aspect("equal"); ax.axis("off")
    # left: ordinary delay
    ax1.plot([0.1, 0.1], [0, 1.2], color=K, lw=3); ax1.plot([0.9, 0.9], [0, 1.2], color=K, lw=3)
    ax1.annotate("", xy=(0.9, 0.5), xytext=(0.1, 0.1 + 0.0), arrowprops=dict(arrowstyle="-|>", lw=2))
    ax1.annotate("", xy=(0.1, 0.9), xytext=(0.9, 0.5), arrowprops=dict(arrowstyle="-|>", lw=2, ls="--"))
    ax1.text(0.1, 1.24, "greenhouse", ha="center", va="bottom", fontsize=10.5)
    ax1.text(0.9, 1.24, "Earth", ha="center", va="bottom", fontsize=10.5)
    ax1.text(0.5, 0.22, "call", rotation=27, fontsize=10.5)
    ax1.text(0.5, 0.78, "answer", rotation=-27, fontsize=10.5)
    ax1.text(0.5, 1.4, "ORDINARY DELAY", ha="center", va="top", fontsize=12, weight="bold")
    ax1.text(0.5, -0.12, "every signal climbs into the\nfuture; the answer is late", ha="center", va="top", fontsize=10)
    # right: closed timelike curve in a spacetime whose top edge is glued to its bottom edge
    ax2.add_patch(Rectangle((0.05, 0.0), 0.9, 1.0, fill=False, lw=1.5, ec=G))
    for y in (0.0, 1.0):
        ax2.annotate("", xy=(0.55, y), xytext=(0.45, y), arrowprops=dict(arrowstyle="-|>", lw=1.8, color=K))
    t = np.linspace(0, 1, 200); x = 0.5 + 0.12 * np.sin(2 * np.pi * t)   # max slope 0.75 < 1: timelike everywhere
    ax2.plot(x, t, color=K, lw=3)
    ax2.plot(0.5, 0.0, "o", color=K, ms=8); ax2.plot(0.5, 1.0, "o", color=K, ms=8)
    for (cx, cy) in ((0.62, 0.25), (0.38, 0.75)):
        ax2.plot([cx - 0.07, cx, cx + 0.07], [cy + 0.07, cy, cy + 0.07], color=G, lw=1.5)
    ax2.text(0.5, 1.4, "CLOSED TIMELIKE CURVE", ha="center", va="top", fontsize=12, weight="bold")
    ax2.text(0.5, 1.2, "top edge glued to bottom edge (arrows)", ha="center", va="center", fontsize=9.5)
    ax2.text(0.5, -0.12, "the path stays inside its light\ncones yet meets its own start:\none event, met twice, not an edit", ha="center", va="top", fontsize=10)
    f.suptitle("Late is not yesterday", fontsize=14, y=0.985)
    save(f, "sd5_ctc_vs_delay.png")

# ---------- SD6: four kinds of elsewhere ----------
def sd6():
    f = fig(6, 5.2)
    pos = [[0.02, 0.5, 0.47, 0.42], [0.51, 0.5, 0.47, 0.42], [0.02, 0.03, 0.47, 0.42], [0.51, 0.03, 0.47, 0.42]]
    axs = [f.add_axes(p) for p in pos]
    for ax in axs:
        ax.set_xlim(-1.2, 1.2); ax.set_ylim(-0.25, 1.25); ax.set_aspect("equal"); ax.axis("off")
    def cone(ax, x0=0, lw=2.2):
        ax.add_patch(Polygon([[x0, 0.9], [x0 - 0.55, 0.35], [x0 + 0.55, 0.35]], closed=True, fc=LG, ec=K, lw=lw))
        ax.plot([x0, x0], [0.15, 0.9], color=K, lw=2.5); ax.plot(x0, 0.9, "o", color=K, ms=5)
    # A: more space
    a = axs[0]; cone(a)
    for x in (-0.95, 0.95):
        a.add_patch(Rectangle((x - 0.13, 0.75), 0.26, 0.2, fill=False, lw=1.8, ls="--"))
        a.text(x, 0.68, "copy?", ha="center", va="top", fontsize=9)
    for sx in (-1, 1):
        a.plot([sx * 0.62, sx * 0.62], [0.3, 1.05], color=G, lw=1.5, ls=":")
    a.text(0, 1.18, "1. MORE SPACE", ha="center", fontsize=11, weight="bold")
    a.text(0, 0.05, "same laws, far beyond\nwhat light could bring us", ha="center", va="top", fontsize=9.5)
    # B: other bubbles
    b = axs[1]
    b.add_patch(Rectangle((-1.15, 0.15), 2.3, 0.95, fc="white", ec=K, lw=1, hatch="///"))
    for x0 in (-0.5, 0.65):
        b.add_patch(Polygon([[x0 - 0.45, 1.1], [x0, 0.3], [x0 + 0.45, 1.1]], closed=True, fc="white", ec=K, lw=2.2))
    b.text(-0.5, 0.85, "ours", ha="center", fontsize=9.5); b.text(0.65, 0.85, "other\nlaws?", ha="center", fontsize=9.5)
    b.text(0, 1.18, "2. OTHER BUBBLES", ha="center", fontsize=11, weight="bold")
    b.text(0, 0.05, "separated by still-inflating\nspace (hatched); never crossed", ha="center", va="top", fontsize=9.5)
    # C: other branches
    c = axs[2]
    c.plot([0, 0], [0.15, 0.55], color=K, lw=2.5); c.plot(0, 0.55, "o", color=K, ms=6)
    c.plot([0, -0.45], [0.55, 1.05], color=K, lw=2.5)
    c.plot([0, 0.45], [0.55, 1.05], color=G, lw=2.5, ls=(0, (5, 3)))
    c.text(-0.52, 0.95, "this\nbranch", ha="right", va="center", fontsize=9.5); c.text(0.52, 0.95, "another\nterm", ha="left", va="center", fontsize=9.5)
    c.text(0.08, 0.5, "decoherence", fontsize=9.5)
    c.text(0, 1.18, "3. OTHER BRANCHES", ha="center", fontsize=11, weight="bold")
    c.text(0, 0.05, "if Everett is right: not elsewhere\nbut \u201celsehow\u201d; no signal between", ha="center", va="top", fontsize=9.5)
    # D: other mathematics
    d = axs[3]
    d.add_patch(Rectangle((-0.8, 0.3), 1.6, 0.7, fill=False, lw=2, ls=":"))
    d.text(0, 0.65, "\u2200x \u2203y \u2026", ha="center", va="center", fontsize=16)
    d.text(0, 1.18, "4. OTHER MATHEMATICS", ha="center", fontsize=11, weight="bold")
    d.text(0, 0.05, "no light cone, no distance:\nnot a place at all", ha="center", va="top", fontsize=9.5)
    save(f, "sd6_four_elsewheres.png")

# ---------- SD7: foliation vs worldline ----------
def sd7():
    f = fig(); ax = f.add_axes([0.02, 0.02, 0.96, 0.9])
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-0.42, 1.2); ax.set_aspect("equal"); ax.axis("off")
    xs = np.linspace(-1.2, 1.2, 50)
    for k in range(6):
        y = 0.1 + 0.2 * k
        ax.plot(xs, y + 0 * xs, color=G, lw=1.6)
        ax.plot(xs, y + 0.18 * xs + 0.05 * np.sin(3 * xs), color=G, lw=1.6, ls=(0, (5, 3)))
    t = np.linspace(0.02, 1.15, 200); x = 0.35 * np.sin(2.4 * t) - 0.1
    ax.plot(x, t, color=K, lw=3.5)
    # proper-time ticks along the worldline: equal arc length in Minkowski sense
    dx = np.gradient(x, t); dtau = np.sqrt(np.clip(1 - dx**2, 0, None)) * np.gradient(t)
    tau = np.cumsum(dtau)
    for k in np.arange(0.15, tau[-1], 0.15):
        i = np.searchsorted(tau, k); ax.plot([x[i] - 0.05, x[i] + 0.05], [t[i], t[i]], color=K, lw=2.5)
    ax.text(-1.25, -0.12, "gray slices, solid or dashed: two of many\nallowed ways to file events into \u201cnows\u201d", fontsize=10, va="top")
    ax.text(0.25, -0.12, "black worldline: the path you live;\nits ticks are proper time, one fact", fontsize=10, va="top")
    f.suptitle("A foliation is how you file the loaf; it is not how you travel", fontsize=13, y=0.98)
    save(f, "sd7_foliation_worldline.png")

def fig46():
    # Chapter 31 figure (added 3 Oct 2026): liquid ranges at 1 atm (melting to boiling point, kelvin).
    # Values: water 273.15-373.15; ammonia 195.4-239.8; methane 90.7-111.7; ethane 90.4-184.6;
    # sulfuric acid (98%) about 283-610 (it decomposes near its boiling point).
    rows = [("water", 273.15, 373.15, "solid"), ("ammonia", 195.4, 239.8, "hatch"),
            ("methane", 90.7, 111.7, "hatch"), ("ethane", 90.4, 184.6, "hatch"),
            ("sulfuric acid", 283.0, 610.0, "dash")]
    f = fig(); ax = f.add_axes([0.2, 0.17, 0.74, 0.66])
    for i, (name, lo, hi, sty) in enumerate(rows):
        y = len(rows) - 1 - i
        if sty == "solid":
            ax.add_patch(Rectangle((lo, y - 0.3), hi - lo, 0.6, facecolor=K, edgecolor=K))
        elif sty == "hatch":
            ax.add_patch(Rectangle((lo, y - 0.3), hi - lo, 0.6, facecolor="white", edgecolor=K, hatch="///", lw=1.6))
        else:
            ax.add_patch(Rectangle((lo, y - 0.3), hi - lo, 0.6, facecolor=LG, edgecolor=K, lw=1.6, ls="--"))
        ax.text(hi + 6, y, f"{lo:.0f}\u2013{hi:.0f} K", ha="left", va="center", fontsize=10, color=G,
                bbox=dict(facecolor="white", edgecolor="none", pad=1))
    ax.axvline(94, color=K, lw=2.2, ls=(0, (2, 2)))
    ax.text(100, -0.75, "Titan surface, 94 K", fontsize=10, va="center")
    ax.axvline(288, color=G, lw=1.4, ls=":")
    ax.text(295, len(rows) - 0.45, "Earth average, about 288 K", fontsize=10, color=G, va="bottom")
    ax.set_xlim(0, 700); ax.set_ylim(-1.0, len(rows) - 0.2)
    ax.set_yticks([len(rows) - 1 - i for i in range(len(rows))]); ax.set_yticklabels([r[0] for r in rows], fontsize=12)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("temperature (kelvin), at one atmosphere")
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    f.suptitle("Where five solvents stay liquid", fontsize=14, y=0.96)
    save(f, "fig46.png")

if __name__ == "__main__":
    for fn in (sd1, sd2, sd3, sd4, sd5, sd6, sd7, fig46):
        fn()
