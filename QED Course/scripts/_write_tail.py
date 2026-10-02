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
    ("diagram", "Cartoon of the three QED actions; one term in ℳ (Prologue 9, Lesson 50). Not a bubble-chamber photograph."),
    ("S-parameter", "Microwave in-to-out amplitude; laboratory cousin of ⟨f|S|i⟩ (Prologue 8)."),
    ("α", "Fine-structure constant, α=e²/4π≈1/137.036 at low energy (Lesson 44). Runs with q² (Lesson 69)."),
    ("α(q²)", "Effective coupling at momentum transfer q, Lesson 69."),
    ("β(e)", "μ de/dμ. One-loop QED, one charged fermion: e³/(12π²) (Lesson 70)."),
    ("γ^μ", "Dirac matrices, {γ^μ,γ^ν}=2g^μν (Lesson 21)."),
    ("Γ^μ", "Full vertex, γ^μ+Λ^μ (Lesson 65)."),
    ("ε_μ", "Photon polarization. Physical sum is two transverse modes; −g_μν is valid inside |ℳ|² by Lesson 72."),
    ("λ", "Infrared photon-mass regulator (Lesson 74), not the ultraviolet cutoff Λ."),
    ("Λ", "Ultraviolet momentum cutoff (Lesson 67)."),
    ("ℳ", "Invariant amplitude, ⟨f|S|i⟩=i(2π)⁴δ⁴(p_f−p_i)ℳ (Lesson 51)."),
    ("μ", "Renormalization scale (Lesson 70), or a muon when the context is scattering."),
    ("ξ", "Covariant gauge-fixing parameter (Lesson 71). ξ=1 Feynman, ξ=0 Landau."),
    ("Π^μν, Π(q²)", "Vacuum polarization (Lesson 63). Π^μν=(q²g^μν−q^μq^ν)Π(q²) by Lesson 72."),
    ("Σ(p)", "Electron self-energy, A(p²)+B(p²)p̸ (Lesson 64)."),
    ("σ^{μν}", "i[γ^μ,γ^ν]/2, enters F2 (Lesson 76)."),
    ("ψ, ψ̄", "Dirac field and adjoint (Lessons 36, 22)."),
    ("□", "∂_μ∂^μ, d'Alembertian."),
    ("a, g", "a=(g−2)/2. Tree Dirac: g=2. One loop: a=α/(2π) (Lesson 76)."),
    ("D_μν", "Photon propagator. Feynman gauge −ig_μν/(k²+iε) (Lessons 48, 71)."),
    ("e, e₀", "Measured charge versus bare charge in the Lagrangian (Lessons 44, 68, 69)."),
    ("F1, F2", "Dirac and Pauli form factors. F1(0)=1, F2(0)=a (Lesson 76)."),
    ("m, m₀", "Physical pole mass versus bare mass (Lesson 68)."),
    ("s, t, u", "Mandelstam variables (Lesson 53). Photon-exchange poles in t are Rutherford; fermion poles in s,t,u are collinear (Lesson 61)."),
    ("S_F, S_F′", "Bare and resummed electron propagators (Lessons 47, 68)."),
    ("Z₂, Z₁, Z₃", "Field, vertex, and charge renormalization constants. Gauge invariance relates Z₁=Z₂ (Lesson 73)."),
    ("metric", "This course uses g=diag(1,−1,−1,−1) as in Lesson 4."),
    ("Heaviside–Lorentz, ℏ=c=1", "Units of Lessons 3 and 7."),
    ("n, L", "Refractive index; optical path length ∫n ds, whose phase k₀L weights each light path (Lesson 9)."),
    ("ℏω, ℏk", "Energy and momentum of one photon (Lessons 9, 38)."),
]

INDEX = [
    ('Complex numbers', 'z=re^{iθ}; inner product ⟨φ|ψ⟩'),
    ('Calculus', 'Gaussian ∫dx e^{−ax²}=√(π/a); used again in Lessons 67 and 80'),
    ('Relativity', 'E²−|p|²=m²'),
    ('Optics', 'r=(n₁−n₂)/(n₁+n₂); U(P)=(1/iλ)∫U e^(ikr)/r cos χ dA; ρ_m=√(mλz); sin θ₁=1.22λ/D (Lesson 9)'),
    ('Dirac equation', '(iγ^μ∂_μ−m)ψ=0'),
    ('QED Lagrangian', 'ℒ=ψ̄(iγ^μD_μ−m)ψ−¼F_μνF^{μν}, D_μ=∂_μ+ieA_μ'),
    ('Vertex', '+ieγ^μ (Lesson 45)'),
    ('Electron propagator', 'S_F(p)=i(p̸+m)/(p²−m²+iε)'),
    ('Photon propagator, Feynman gauge', 'D_μν=−ig_μν/(k²+iε)'),
    ('Photon propagator, R_ξ', '−i[g_μν−(1−ξ)k_μk_ν/k²]/(k²+iε)'),
    ('Amplitude', '⟨f|S|i⟩=i(2π)⁴δ⁴(p_f−p_i)ℳ'),
    ('Two-body cross section', 'dσ/dΩ=|ℳ|²/(64π²s) (massless, equal masses, Lesson 59)'),
    ('Massless Compton', '(1/4)Σ|ℳ|²=−2e⁴(s/u+u/s)'),
    ('Loop count', 'L=I−V+1'),
    ('Regularization (this volume)', 'Wick rotation and a Euclidean cutoff |k_E|<Λ (Lesson 67), not dimensional regularization'),
    ('Mass renormalization', 'm=m₀+A(m₀²) at leading order (Lesson 68)'),
    ('Running coupling', 'α(Q²)=α/[1−(α/3π)(ln(Q²/m²)−5/3)] for Q²=−q²≫m², one lepton (Lesson 69)'),
    ('Vacuum polarization, small Q²', 'Π̂≈(α/15π)Q²/m² for Q²≪m² (Lessons 69, 78)'),
    ('Beta function', 'β(e)=μ de/dμ=e³/(12π²); 1/α(μ)=1/α(μ₀)−(b/2π)ln(μ/μ₀), b=(4/3)Σ_f N_c Q_f² (Lesson 70)'),
    ('Gauge fixing', 'ℒ_gf=−(∂_μA^μ)²/(2ξ); ξ=1 Feynman, ξ=0 Landau (Lesson 71)'),
    ('Ward identity', 'k_μ ℳ^μ=0; q_μΓ^μ(p+q,p)=S̃⁻¹(p+q)−S̃⁻¹(p); Z₁=Z₂ (Lesson 72)'),
    ('Gauge independence', '∂ℳ/∂ξ=0 for a physical amplitude (Lesson 73)'),
    ('Infrared cancellation', 'dσ_meas=dσ₀[1−(α/π)f_IR(q²)ln(Q²/E_l²)+finite]; the photon mass λ cancels (Lesson 74)'),
    ('Soft emission', 'iℳ≈iℳ₀·e[p·ε∗/(p·k)−p′·ε∗/(p′·k)] (Lesson 75)'),
    ('Anomalous moment', 'g=2[F₁(0)+F₂(0)]; a=F₂(0)=α/(2π) (Lesson 76)'),
    ('Lamb shift, leading log', 'ΔE_ns=(4α(Zα)⁴m/(3πn³))ln[m/k₀(n,0)]; E(2s½)−E(2p½)≈1054 MHz (Lesson 77)'),
    ('Uehling term', 'δV(r)=−(4Zα²/15m²)δ³(r); ΔE_ns=−4α(Zα)⁴m/(15πn³), about −27 MHz for hydrogen 2s (Lesson 78)'),
    ('Precision tests', 'a_e=0.00115965218059(13) (Lesson 76); f(1s–2s)=2 466 061 413 187 035(10) Hz (Lesson 79)'),
    ('Path integral', '⟨q_f|e^(−iHT)|q_i⟩=∫Dq e^(iS[q]) (Lesson 80)'),
    ('Generating functionals', 'Z[J]=∫Dφ exp(iS[φ]+i∫Jφ); W[J]=−i log Z[J] (Lesson 81)'),
    ('Effective action', 'Γ[φ]=W[J]−∫Jφ, δΓ/δφ=−J; ℒ_eff=½(E²−B²)+(2α²/45m⁴)[(E²−B²)²+7(E·B)²] (Lesson 82)'),
    ('Schwinger–Dyson, anomaly', '⟨δS/δφ(x)⟩_J=−J(x); ∂_μJ^(μ5)=−(e²/16π²)ε^(μνρσ)F_μνF_ρσ (Lesson 83)'),
    ('Feynman rules from Z', 'Z[J,η̄,η]=exp(iS_int[−iδ/δJ, −iδ/δη̄, iδ/δη]) Z₀[J,η̄,η] (Lesson 84)'),
    ('Finite temperature', 'm_D²=e²T²/3; V(r)=(α/r)e^(−m_D r); F/V=−(π²/45)T⁴ for photons (Lesson 85)'),
    ('Schwinger pair rate', 'Γ/V=(eE)²/(4π³) exp(−π m²/eE) (Lesson 86)'),
    ('Electroweak embedding', 'Z_μ=cosθ_W W³_μ−sinθ_W B_μ, A_μ=sinθ_W W³_μ+cosθ_W B_μ; 1/α(M_Z)≈128.94 (Lesson 87)'),
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
        "CODATA and the Particle Data Group are the sources for the constants in Lesson 79."
    )
    b.table(
        [
            ["Item", "Reference"],
            ["Easy QED (opening)", "R. P. Feynman, QED: The Strange Theory of Light and Matter, Princeton (1985). Physics only; this course does not reproduce the text."],
            ["S-parameters", "D. M. Pozar, Microwave Engineering, Wiley. Two-port S is the laboratory cousin of ⟨f|S|i⟩."],
            ["Optics (Lesson 9)", "E. Hecht, Optics, 5th ed., Pearson (2017); M. Born and E. Wolf, Principles of Optics, 7th ed., Cambridge (1999)."],
            ["Single-photon interference", "P. Grangier, G. Roger and A. Aspect, Europhys. Lett. 1, 173 (1986)."],
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
