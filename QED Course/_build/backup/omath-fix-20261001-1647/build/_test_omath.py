import sys
sys.path.insert(0, r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\QED Course\_build")
import omath

samples = [
    "t = − 4 p² sin²(θ/2)",
    "S_F′(p) = i / (p̸ − m₀ − Σ(p))",
    "m = m₀ + A(m₀²)",
    "(1/4) Σ|ℳ|² = − 2 e⁴ ( s/u + u/s )",
    "L = I − V + 1",
    "∫ k³ dk / k⁴ = ∫ dk/k = ln Λ",
    "q_μ Π^(μν)(q) = 0",
    "T_(AA) = 32(s/2)(s/2) − 16s(−t/2)",
    "γ^μ(p̸−k̸+m)γ_μ = − 2(p̸−k̸) + 4m",
    "F_2(0) = α/(2π)",
]
for s in samples:
    print("---")
    print(s)
    print(omath.describe(s))
