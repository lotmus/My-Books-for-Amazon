# -*- coding: utf-8 -*-
"""Replace the capstone and formula index in Complete QED Course.docx
with text that matches the written lessons, and insert a glossary."""
import os
import sys

from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lesson as bl

COMPLETE = bl.COMPLETE


def heading1_text(child):
    if child.tag != qn("w:p"):
        return None
    p_style = child.find(qn("w:pPr") + "/" + qn("w:pStyle"))
    if p_style is None or p_style.get(qn("w:val")) != "Heading1":
        return None
    return "".join(t.text or "" for t in child.iter(qn("w:t")))


def find_start(body, prefix):
    for child in body:
        text = heading1_text(child)
        if text and text.startswith(prefix):
            return child
    return None


GLOSSARY = [
    ("arrow", "Prologue 1 amplitude: a length and a direction in a plane. Probability = (length)²."),
    ("diagram", "Cartoon of the three QED actions; one term in ℳ (Prologue 9, Lesson 49). Not a bubble-chamber photograph."),
    ("S-parameter", "Microwave in-to-out amplitude; laboratory cousin of ⟨f|S|i⟩ (Prologue 8)."),
    ("α", "Fine-structure constant, α=e²/4π≈1/137.036 at low energy (Lesson 43). Runs with q² (Lesson 68)."),
    ("α(q²)", "Effective coupling at momentum transfer q, Lesson 68."),
    ("β(e)", "μ de/dμ. One-loop QED, one charged fermion: e³/(12π²) (Lesson 69)."),
    ("γ^μ", "Dirac matrices, {γ^μ,γ^ν}=2g^μν (Lesson 20)."),
    ("Γ^μ", "Full vertex, γ^μ+Λ^μ (Lesson 64)."),
    ("ε_μ", "Photon polarization. Physical sum is two transverse modes; −g_μν is valid inside |ℳ|² by Lesson 71."),
    ("λ", "Infrared photon-mass regulator (Lesson 73), not the ultraviolet cutoff Λ."),
    ("Λ", "Ultraviolet momentum cutoff (Lesson 66)."),
    ("ℳ", "Invariant amplitude, ⟨f|S|i⟩=i(2π)⁴δ⁴(p_f−p_i)ℳ (Lesson 50)."),
    ("μ", "Renormalization scale (Lesson 69), or a muon when the context is scattering."),
    ("ξ", "Covariant gauge-fixing parameter (Lesson 70). ξ=1 Feynman, ξ=0 Landau."),
    ("Π^μν, Π(q²)", "Vacuum polarization (Lesson 62). Π^μν=(q²g^μν−q^μq^ν)Π(q²) by Lesson 71."),
    ("Σ(p)", "Electron self-energy, A(p²)+B(p²)p̸ (Lesson 63)."),
    ("σ^{μν}", "i[γ^μ,γ^ν]/2, enters F2 (Lesson 75)."),
    ("ψ, ψ̄", "Dirac field and adjoint (Lessons 35, 21)."),
    ("□", "∂_μ∂^μ, d'Alembertian."),
    ("a, g", "a=(g−2)/2. Tree Dirac: g=2. One loop: a=α/(2π) (Lesson 75)."),
    ("D_μν", "Photon propagator. Feynman gauge −ig_μν/(k²+iε) (Lessons 47, 70)."),
    ("e, e₀", "Measured charge versus bare charge in the Lagrangian (Lessons 43, 67, 68)."),
    ("F1, F2", "Dirac and Pauli form factors. F1(0)=1, F2(0)=a (Lesson 75)."),
    ("m, m₀", "Physical pole mass versus bare mass (Lesson 67)."),
    ("s, t, u", "Mandelstam variables (Lesson 52). Photon-exchange poles in t are Rutherford; fermion poles in s,t,u are collinear (Lesson 60)."),
    ("S_F, S_F′", "Bare and resummed electron propagators (Lessons 46, 67)."),
    ("Z₂, Z₁, Z₃", "Field, vertex, and charge renormalization constants. Gauge invariance relates Z₁=Z₂ (Lesson 72)."),
    ("metric", "This course uses g=diag(1,−1,−1,−1) as in Lesson 4."),
    ("Heaviside-Lorentz, ℏ=c=1", "Units of Lessons 3 and 7."),
]

INDEX = [
    ("Complex numbers", "z=re^{iθ}; inner product ⟨φ|ψ⟩"),
    ("Calculus", "Gaussian ∫dx e^{−ax²}=√(π/a); used again in Lessons 66 and 79"),
    ("Relativity", "E²−|p|²=m²"),
    ("Dirac equation", "(iγ^μ∂_μ−m)ψ=0"),
    ("QED Lagrangian", "ℒ=ψ̄(iγ^μD_μ−m)ψ−¼F_μνF^{μν}, D_μ=∂_μ+ieA_μ"),
    ("Vertex", "+ieγ^μ (Lesson 44)"),
    ("Electron propagator", "S_F(p)=i(p̸+m)/(p²−m²+iε)"),
    ("Photon propagator, Feynman gauge", "D_μν=−ig_μν/(k²+iε)"),
    ("Photon propagator, R_ξ", "−i[g_μν−(1−ξ)k_μk_ν/k²]/(k²+iε)"),
    ("Amplitude", "⟨f|S|i⟩=i(2π)⁴δ⁴(p_f−p_i)ℳ"),
    ("Two-body cross section", "dσ/dΩ=|ℳ|²/(64π²s) (massless, equal masses, Lesson 58)"),
    ("Massless Compton", "(1/4)Σ|ℳ|²=−2e⁴(s/u+u/s)"),
    ("Loop count", "L=I−V+1"),
    ("Regularization (this volume)", "Wick rotation and a Euclidean cutoff |k_E|<Λ (Lesson 66), not dimensional regularization"),
    ("Mass renormalization", "m=m₀+A(m₀²) at leading order (Lesson 67)"),
    ("Running coupling", "α(q²)=α/[1−(α/3π)log(|q²|/m²)] at one loop, one flavor (Lesson 68)"),
    ("Beta function", "β(e)=e³/(12π²) (Lesson 69)"),
    ("Ward identity", "k_μ ℳ^μ=0 (Lesson 71)"),
    ("Soft emission", "ℳ_soft=e(p·ε/p·k)ℳ_tree (Lesson 74)"),
    ("Anomalous moment", "a=F₂(0)=α/(2π) (Lesson 75)"),
    ("Lamb contact / Bethe log", "ΔE_ns=(4α/(3π m²))|ψ(0)|² log(m/⟨ΔE⟩) (Lesson 76)"),
    ("Uehling at small q²", "Π̂(q²)≈(α/15π)(q²/m²); δE_U(2s)≈−27 MHz (Lesson 77)"),
    ("Schwinger pair rate", "Γ/V=(eE)²/(4π³) exp(−π m²/eE) (Lesson 85)"),
    ("Path integral", "Z=∫Dφ exp(iS[φ]) (Lesson 79)"),
]


def replace_from(doc, start_prefix, blocks_builder):
    body = doc.element.body
    start = find_start(body, start_prefix)
    if start is None:
        raise RuntimeError("missing " + start_prefix)
    node = start
    while node is not None:
        nxt = node.getnext()
        body.remove(node)
        node = nxt
    b = bl.Builder(doc)
    blocks_builder(b)
    # elements already appended to body by Builder


def build_tail(b):
    b.heading("Glossary of symbols", 1)
    b.para("Compiled from the lesson notation tables. When a symbol changes meaning, both uses are listed.")
    b.table([["Symbol", "Meaning"]] + [list(row) for row in GLOSSARY], [2160, 7632])
    b.pagebreak()
    b.heading("Course capstone", 1)
    b.para(
        "Starting from a free Dirac field, impose local U(1) phase invariance, introduce the covariant derivative "
        "and the electromagnetic field, derive the QED Lagrangian, quantize the free fields, read off the vertex +ieγ^μ "
        "and the propagators, construct the five tree-level processes of Part VIII, convert |ℳ|² to a cross section, "
        "and distinguish Rutherford's photon-exchange pole from a collinear fermion pole. Then, at one loop, regularize "
        "with a cutoff, absorb the ultraviolet divergence of the self-energy into m₀, run the charge with vacuum "
        "polarization, state the Ward identity that justifies Feynman gauge, cancel infrared logarithms in an inclusive "
        "rate, and derive a=α/(2π). The capstone is complete when each arrow is justified with an equation from this volume."
    )
    b.pagebreak()
    b.heading("Consolidated formula index", 1)
    b.para("Working formulae as they appear in the written lessons, not slogans from a skeleton outline.")
    b.table([["Topic", "Formula"]] + [list(row) for row in INDEX], [2880, 6912])
    b.pagebreak()
    b.heading("Bibliography", 1)
    b.para(
        "Papers and books named at the moment this course uses them. "
        "CODATA and the Particle Data Group are the sources for the constants in Lesson 78."
    )
    b.table(
        [
            ["Item", "Reference"],
            ["Easy QED (opening)", "R. P. Feynman, QED: The Strange Theory of Light and Matter, Princeton (1985). Physics only; this course does not reproduce the text."],
            ["S-parameters", "D. M. Pozar, Microwave Engineering, Wiley. Two-port S is the laboratory cousin of ⟨f|S|i⟩."],
            ["Mead’s view (Interlude)", "C. A. Mead, Collective Electrodynamics: Quantum Foundations of Electromagnetism, MIT Press (2000)."],
            ["Dirac equation and g=2", "P. A. M. Dirac, Proc. Roy. Soc. A 117, 610 (1928)."],
            ["Schwinger a=α/(2π)", "J. Schwinger, Phys. Rev. 73, 416 (1948)."],
            ["Lamb–Retherford interval", "W. E. Lamb and R. C. Retherford, Phys. Rev. 72, 241 (1947)."],
            ["Bethe logarithm", "H. A. Bethe, Phys. Rev. 72, 339 (1947)."],
            ["Uehling potential", "E. A. Uehling, Phys. Rev. 48, 55 (1935)."],
            ["Bloch–Nordsieck IR", "F. Bloch and A. Nordsieck, Phys. Rev. 52, 54 (1937)."],
            ["Schwinger pair production", "J. Schwinger, Phys. Rev. 82, 664 (1951)."],
            ["Constants", "CODATA recommended values; Particle Data Group Review of Particle Physics."],
            ["QED textbook (traces)", "M. D. Schwartz, Quantum Field Theory and the Standard Model, Cambridge (2014)."],
            ["QED textbook (loops)", "M. E. Peskin and D. V. Schroeder, An Introduction to Quantum Field Theory, Westview (1995)."],
            ["QED textbook (canonical)", "F. Mandl and G. Shaw, Quantum Field Theory, Wiley, 2nd ed. (2010)."],
            ["External fields", "C. Itzykson and J.-B. Zuber, Quantum Field Theory, McGraw-Hill (1980), ch. 4."],
        ],
        [2880, 6912],
    )


def main():
    doc = Document(COMPLETE)
    body = doc.element.body
    start = find_start(body, "Glossary")
    if start is None:
        start = find_start(body, "Course capstone")
    if start is None:
        raise RuntimeError("could not find capstone or glossary")
    node = start
    while node is not None:
        nxt = node.getnext()
        if node.tag != qn("w:sectPr"):
            body.remove(node)
        node = nxt
    b = bl.Builder(doc)
    build_tail(b)
    doc.save(COMPLETE)
    print("glossary + capstone + index written")


if __name__ == "__main__":
    main()
