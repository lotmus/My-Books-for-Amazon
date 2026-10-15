# -*- coding: utf-8 -*-
"""Revision pass over the lesson/prologue txt sources (idempotent where practical).
Usage: python apply_revision.py <scripts_dir>"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from boxes import FP, PLAIN
S = sys.argv[1]
def rd(fn): return open(os.path.join(S, fn), encoding='utf-8').read()
def wr(fn, s): open(os.path.join(S, fn), 'w', encoding='utf-8').write(s)

# ---------- 1. figures ----------
FIGREPL = {  # lesson: (file, width, caption)
45: ("L45_vertex.png", 3.6, "The QED vertex. A fermion line enters with momentum p and leaves with p′; the photon carries q = p − p′. The vertex factor is ieγ^μ, one gamma matrix and one power of the charge."),
50: ("L50_rules.png", 6.2, "The momentum-space Feynman rules of QED in one chart: external legs, propagators, vertex, loop integral and the fermion-loop sign."),
54: ("L54_emu.png", 3.8, "Electron–muon scattering at lowest order: one diagram, one photon in the t-channel, q = p₁ − p₃."),
55: ("L55_moller.png", 6.0, "Møller scattering. Identical electrons give a direct (t-channel) and an exchange (u-channel) diagram with a relative minus sign."),
56: ("L56_annihilation.png", 6.0, "Electron–positron annihilation into two photons: the t-channel and u-channel diagrams with an internal electron line."),
57: ("L57_compton.png", 6.0, "Compton scattering: the s-channel (absorb, then emit) and u-channel (emit, then absorb) diagrams."),
63: ("L63_vp.png", 6.0, "Vacuum polarization. The photon briefly becomes an electron–positron pair; loop momenta k and k − q; the closed fermion loop gives a trace and a minus sign."),
64: ("L64_se.png", 6.0, "Electron self-energy: the electron emits and reabsorbs a virtual photon of momentum k."),
65: ("L65_vertex.png", 6.0, "The one-loop vertex correction: a virtual photon spans the vertex. Its magnetic part gives the anomalous moment of Lesson 76."),
69: ("L69_dyson.png", 6.2, "Dyson resummation: the dressed photon propagator is the bare one plus any number of vacuum-polarization insertions, a geometric series."),
72: ("L72_ward.png", 6.0, "The Ward identity at work. Replace a photon's polarization by its momentum k and the diagrams of a gauge-invariant set sum to zero."),
74: ("L74_ir.png", 6.0, "Infrared divergences: the virtual-photon correction and the real soft-photon emission diverge separately; only their sum, at fixed detector resolution, is finite."),
75: ("L75_soft.png", 6.0, "Soft-photon emission from external legs. The factor e(p·ε/p·k) multiplies the non-radiative amplitude, independently of the hard process."),
76: ("L76_g2.png", 5.6, "The anomalous magnetic moment. The vertex correction modifies the coupling to a static field; the Pauli form factor at zero momentum transfer gives a = α/2π."),
}
FIGADD = [  # (lesson, anchor heading line, file, width, caption)
(46, "## 2.2 The Feynman propagator", "L46_scalar.png", 4.6, "The scalar Feynman propagator: positive energy propagates forward in time, negative energy backward; the time-ordered product handles both cases."),
(46, "## 5.1 Locating the poles", "L46_poles.png", 4.6, "Poles of the propagator in the complex k⁰ plane. The iε places them at ±(ω − iε'); the Feynman contour passes below the left pole and above the right one."),
(47, "@first_section", "L47_electron.png", 4.2, "The electron propagator i(p̸ + m)/(p² − m² + iε): a solid line with an arrow that follows the flow of negative charge."),
(48, "## 4.1 The Feynman-gauge propagator", "L48_photon.png", 4.2, "The Feynman-gauge photon propagator −ig_μν/(k² + iε): a wavy line, no arrow."),
(49, "## 5.1 All six factors", "L52_external.png", 6.0, "The six external-line factors at a glance: u and ū for electrons, v̄ and v for positrons, ε and ε* for photons."),
(49, "## 6.1 The vertex does not \"know\" which legs are attached", "L49_vertices.png", 6.0, "One vertex, several processes. Rotating the same vertex gives emission, absorption, pair creation and annihilation."),
(51, "## 3.4 The complete formula", "L59_flow.png", 6.2, "From amplitude to measurement: |ℳ|², averaged and summed over spins, times flux and phase-space factors, gives the cross section."),
(52, "## 3.2 The building-block trace", "L52_trace.png", 6.2, "How a spin sum becomes a trace: the amplitude times its conjugate, summed with Σuū = p̸ + m, closes into Tr[…]."),
(53, "## 1.1 Definitions", "L51_kinematics.png", 5.6, "Two-to-two kinematics and the Mandelstam variables s = (p₁ + p₂)², t = (p₁ − p₃)², u = (p₁ − p₄)²."),
(53, "# 6 s, t, u and the diagrams", "L53_momentum.png", 5.6, "Momentum conservation at each vertex fixes every internal momentum of a tree diagram; the channel of the exchanged line names its s, t or u dependence."),
(57, "@before_connections", "L57_klein_nishina.png", 5.2, "The Klein–Nishina angular distribution for several photon energies: forward scattering dominates as the energy rises; at low energy it reduces to Thomson's 1 + cos²θ."),
(58, "## 1.2 The two amplitudes", "L58_pair.png", 6.0, "Pair production γγ → e⁺e⁻: the crossing of Lesson 56's annihilation diagrams."),
(59, "## 1.2 Choosing the center-of-momentum frame", "L59_cm.png", 5.2, "Two-body final state in the CM frame. Energy fixes |p_f|; only the direction, within dΩ, is free."),
(60, "## 1.2 Why the rest frame", "L60_decay.png", 4.6, "A two-body decay in the parent's rest frame: back-to-back daughters with equal and opposite momenta."),
(61, "## 2.4 Two singularities, two diagrams", "L61_angular.png", 5.6, "Angular distributions of three Part VIII processes in the high-energy limit (log scale). Photon exchange in the t-channel gives the steep forward peak; fermion exchange gives the collinear rises. At fixed angle every curve falls as 1/s."),
(62, "## 4.3 The three one-loop diagrams of QED", "L62_topologies.png", 6.2, "The three one-loop subdiagrams of QED: vacuum polarization, electron self-energy and vertex correction."),
(66, "## 4.3 Substituting away the internal-line counts", "L66_powercount.png", 6.0, "Power counting from external lines alone. Only a handful of amplitudes have D ≥ 0; symmetry softens their actual divergences to logarithms."),
(67, "## 3.1 The idea", "L67_wick.png", 4.6, "Wick rotation: the k⁰ contour is turned through 90° to the imaginary axis without crossing a pole, turning Minkowski into Euclidean integrals."),
(68, "## 4.3 Why this is not a problem", "L68_counterterms.png", 6.0, "Self-energy plus counterterm: the divergent part is absorbed into the bare mass, and the propagator's pole sits at the measured mass."),
(69, "@before_connections", "L69_running.png", 5.2, "The running of α. The effective coupling rises logarithmically with momentum transfer, from 1/137.036 at low Q to about 1/128 at the Z mass."),
(70, "## 5.1 Three possibilities", "L70_beta.png", 5.2, "The sign of β decides the high-energy behaviour: β > 0 (QED) grows towards a Landau pole, β < 0 (QCD) weakens, β = 0 stays fixed."),
(71, "## 1.2 An operator without an inverse", "L71_gauge_orbits.png", 5.2, "Gauge orbits. All potentials on one orbit describe the same physics; gauge fixing chooses one representative per orbit."),
(73, "# 1 Four layers of invariance", "L73_map.png", 6.0, "Four layers of gauge invariance, from the Lagrangian to the S-matrix, and what each protects."),
(77, "## 1.2 What the degeneracy means", "L77_lamb.png", 5.2, "The n = 2 levels of hydrogen: Dirac theory makes 2s₁/₂ and 2p₁/₂ degenerate; QED lifts 2s₁/₂ by about 1058 MHz."),
(78, "## 2.3 The picture", "L78_uehling.png", 5.2, "The Uehling potential. Vacuum polarization strengthens the Coulomb attraction at distances shorter than the electron Compton wavelength."),
(79, "## 1.1 Inputs and outputs", "L79_map.png", 6.0, "How precision tests interlock: measured inputs (α, masses) enter QED; outputs (g − 2, hydrogen, muonium, positronium, colliders) are compared with experiment."),
]

def fig_line(f, w, cap): return f"IMG: {f} | {w} | Figure #. {cap}"

def para_end(lines, i):
    """index after the first body paragraph following line i (a heading)."""
    j = i + 1
    while j < len(lines) and not lines[j].strip(): j += 1
    while j < len(lines) and lines[j].strip(): j += 1
    return j

def do_figures(n, s):
    if n in FIGREPL and "FIG:" in s:
        f, w, cap = FIGREPL[n]
        s = re.sub(r"(?ms)^FIG:\n.*?^ENDFIG\n", fig_line(f, w, cap) + "\n", s, count=1)
    for (ln, anchor, f, w, cap) in FIGADD:
        if ln != n or ("IMG: " + f) in s: continue
        lines = s.split("\n")
        if anchor == "@first_section":
            i = next(k for k, l in enumerate(lines) if re.match(r"# 1 ", l))
        elif anchor == "@before_connections":
            i = next(k for k, l in enumerate(lines) if re.match(r"# \d+ Connections to QED", l))
            lines[i:i] = [fig_line(f, w, cap), ""]
            s = "\n".join(lines); continue
        else:
            i = lines.index(anchor)
        j = para_end(lines, i)
        lines[j:j] = ["", fig_line(f, w, cap)]
        s = "\n".join(lines)
    # number captions
    k = [0]
    def num(m):
        k[0] += 1; return f"Figure {n}.{k[0]}."
    s = re.sub(r"Figure (?:#|\d+\.\d+)\.", num, s)
    return s

# ---------- 2. boxes ----------
def do_boxes(n, s):
    if n in PLAIN and "BOX: Plain-language start" not in s:
        txt = PLAIN[n]
        s = s.replace("## Learning objectives", f"BOX: Plain-language start\n{txt}\nENDBOX\n\n## Learning objectives", 1)
    if n in FP and "BOX: First pass" not in s:
        res, mean = FP[n]
        m = re.search(r"(?m)^# 1 ", s)
        box = f"BOX: First pass: the result before the derivation\n{res}\n{mean}\nENDBOX\n\n"
        s = s[:m.start()] + box + s[m.start():]
    return s

# ---------- 3. exercise labels ----------
HARD = re.compile(r"^(Derive|Prove|Combine|Assemble|Carry|Repeat|Starting|Show that the full|Using the full)")
def do_labels(n, s):
    if "| **Core.**" in s or "| **Extension.**" in s: return s
    ex = re.search(r"(?ms)^# Exercises\n(.*?)^# Solutions\n(.*?)(?=^# |\Z)", s)
    if not ex: return s
    tbl, sol = ex.group(1), ex.group(2)
    rows = re.findall(r"(?m)^\| (\d+) \| (.*) \|$", tbl)
    sollen = {}
    for m in re.finditer(r"(?ms)^\*\*(\d+)\.\*\*(.*?)(?=^\*\*\d+\.\*\*|\Z)", sol):
        sollen[int(m.group(1))] = len(m.group(2))
    cand = [(sollen.get(int(no), 10**6), int(no)) for no, t in rows
            if not t.startswith("Challenge") and not HARD.match(t)]
    cand.sort()
    ncore = max(5, round(0.5 * len(rows)))
    core = {no for _, no in cand[:ncore]}
    core = set(sorted(core))
    def lab(m):
        no, t = int(m.group(1)), m.group(2)
        if t.startswith("Challenge:"):
            t2 = t[len("Challenge:"):].strip(); t2 = t2[:1].upper() + t2[1:]
            return f"| {no} | **Challenge.** {t2} |"
        return f"| {no} | **{'Core' if no in core else 'Extension'}.** {t} |"
    tbl2 = re.sub(r"(?m)^\| (\d+) \| (.*) \|$", lab, tbl)
    return s[:ex.start(1)] + tbl2 + s[ex.end(1):]

# ---------- 4. try-first ----------
TRY = "*Attempt each exercise before reading its solution. If you are stuck, read only the first sentence of the solution, then try again.*"
def do_try(n, s):
    if TRY in s: return s
    return s.replace("# Solutions\n", "# Solutions\n\n" + TRY + "\n", 1)

# ---------- 5. mastery trim ----------
KEEP = {21, 39, 41, 52, 66, 67, 68, 69, 70, 71, 72, 73}
CHECK = ("# Mastery check\n\nBefore moving on, do the Core exercises without looking at the solutions and state this "
         "lesson's first-pass result from memory. If both go smoothly, continue; if not, reread the sections the "
         "missed exercises cite.\n")
def do_mastery(n, s):
    if n in KEEP: return s
    m = re.search(r"(?ms)^# Mastery checklist\n.*?(?=^# |\Z)", s)
    if not m: return s
    return s[:m.start()] + CHECK + ("\n" if m.end() < len(s) else "") + s[m.end():]

def run():
    tot = {}
    for n in range(2, 88):
        fn = f"lesson{n:02d}.txt"
        s0 = s = rd(fn)
        s = do_figures(n, s) if 45 <= n <= 79 else s
        s = do_boxes(n, s); s = do_labels(n, s); s = do_try(n, s); s = do_mastery(n, s)
        if s != s0: wr(fn, s)
        tot[n] = (s.count("IMG: "), s.count("**Core.**"), s.count("**Extension.**"), s.count("**Challenge.**"))
    for fn in ["prologue08.txt", "prologue09.txt", "interlude_mead.txt", "prologue07.txt"]:
        s0 = s = rd(fn)
        s = do_labels(0, s); s = do_try(0, s)
        if fn == "interlude_mead.txt": s = do_mastery(0, s)
        if s != s0: wr(fn, s)
        print(fn, s.count("**Core.**"), s.count("**Extension.**"), s.count("**Challenge.**"), TRY in s)
    import collections
    print("figs", sum(v[0] for v in tot.values()), "core", sum(v[1] for v in tot.values()),
          "ext", sum(v[2] for v in tot.values()), "chal", sum(v[3] for v in tot.values()))
    print([n for n, v in tot.items() if v[3] != 1])
run()
