"""Self-test for omath.py: python _test_omath.py (prints the trees, asserts the cases)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import omath

CASES = [
    # brackets that must stay visible
    ("(Zα)⁴", "(Zα)^(4)"),
    ("(ie)²", "(ie)^(2)"),
    ("((p−k)²−m²) k²", "((p−k)^(2)−m^(2)) k^(2)"),
    ("f(x)", "f(x)"),
    ("f(x)/g(y)", "(f(x))/(g(y))"),
    ("S_F′(p) = i / (p̸ − m₀ − Σ(p))", "S_(F′)(p)=(i)/(slash(p)−m_(0)−Σ(p))"),
    ("m = m₀ + A(m₀²)", "m=m_(0)+A(m_(0)^(2))"),
    ("q_μ Π^(μν)(q) = 0", "q_(μ) Π^(μν)(q)=0"),
    # brackets that only group
    ("F_2(0) = α/(2π)", "F_(2)(0)=(α)/(2π)"),
    ("(1/4) Σ|ℳ|² = − 2 e⁴ ( s/u + u/s )", "(1)/(4) Σ|ℳ|^(2)=−2 e^(4) ((s)/(u)+(u)/(s))"),
    ("e^(iωt)", "e^(iωt)"),
    ("d⁴k/(2π)⁴", "(d^(4)k)/((2π)^(4))"),
    # spaces and function names
    ("sinh ωτ", "func[sinh](ωτ)"),
    ("x(τ) = A cosh ωτ + B sinh ωτ", "x(τ)=A func[cosh](ωτ)+B func[sinh](ωτ)"),
    ("det A", "func[det](A)"),
    ("t = − 4 p² sin²(θ/2)", "t=−4 p^(2) func[sin^(2)](((θ)/(2)))"),
    ("ℏc = 197.327 MeV fm", "ℏc=197.327 MeV fm"),
    # indices
    ("iγ^μ∂_μψ", "iγ^(μ)∂_(μ)ψ"),
    ("Tr[γ^μγ^ν] = 4g^μν", "func[Tr]([γ^(μ)γ^(ν)])=4g^(μν)"),
    ("ℒ_int", "ℒ_(int)"),
    ("(Λ⁻¹)^ν_μ", "(Λ^(−1))_(μ)^(ν)"),
    ("a = (m ω q + i p)/√(2 m ω)", "a=(m ω q+i p)/(√(2 m ω))"),
    ("ℏ²|k|²/2m", "(ℏ^(2)|k|^(2))/(2m)"),
]

failed = 0
for src, want in CASES:
    got = omath.describe(src)
    ok = got == want
    failed += not ok
    print("ok  " if ok else "FAIL", src, " => ", got, "" if ok else "   wanted " + want)
print("all passed" if not failed else "%d failed" % failed)
sys.exit(1 if failed else 0)
