import re, os
from pathlib import Path
from collections import Counter

books = [
    ("B1 The Universe Has No Now", Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\The Universe Has No Now - Manuscript")),
    ("B2 A Trip Is Not a Settlement", Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\A Trip Is Not a Settlement - Manuscript")),
    ("B3 A Longer Life Is Not a New Body", Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\A Longer Life Is Not a New Body - Manuscript")),
]


def wc(text):
    body = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    body = re.sub(r"^#+\s+.*$", " ", body, flags=re.M)
    return len(re.findall(r"[A-Za-z0-9\u2019']+", body))


def ch_sizes(text):
    out = []
    for sec in re.split(r"(?=^##\s+)", text, flags=re.M):
        m = re.match(r"^##\s+(\d+)\.\s+", sec, re.M)
        if not m:
            continue
        n = int(m.group(1))
        body = re.sub(r"!\[.*?\]\(.*?\)", " ", sec)
        body = re.sub(r"^#+\s+.*$", " ", body, flags=re.M)
        out.append((n, len(re.findall(r"[A-Za-z0-9\u2019']+", body))))
    return out


obscure = re.compile(
    r"\b(Elena Voss|Dex Ortega|Pavel Grun|Nadia Okonkwo|Linh Pham|Wei Ning|"
    r"Ibrahim Sorel|Priya Nair|Owen Hale|Anjali Mehta|Nandita Rao|Tom Brennan|"
    r"Jeanne Calment|William James|Michelson|Morley|Hendrik Lorentz|Henri Poincaré|"
    r"Hermann Minkowski|Roger Penrose|is invented)\b"
)

for name, root in books:
    parts = [
        f
        for f in sorted(os.listdir(root))
        if re.match(r"^(00_Front|0[1-9]_|1[01]_)", f)
        and f.endswith(".md")
        and f not in ("00_Chapter_Outline.md", "00_Figure_Plan.md", "00_Status.md")
    ]
    texts = [(f, (root / f).read_text(encoding="utf-8")) for f in parts]
    big = "\n\n".join(t for _, t in texts)
    total = wc(big)
    sizes = []
    for _, t in texts:
        sizes.extend(ch_sizes(t))
    thin = [(n, w) for n, w in sizes if w < 1500]
    pop = "\n".join(t for f, t in texts if not f.startswith("11_"))
    hits = Counter(obscure.findall(pop))
    docx_candidates = list(root.glob("*Kindle.docx"))
    if (root / "export").exists():
        docx_candidates += list((root / "export").glob("*.docx"))
    docx_candidates += list((root / "Figures").glob("*Kindle.docx"))
    docx = None
    sz = 0
    for d in docx_candidates:
        if d.stat().st_size > sz:
            docx, sz = d, d.stat().st_size
    print("====", name, "====")
    print("TOTAL", total)
    print("chapters", len(sizes), "thin", thin if thin else "none")
    if sizes:
        ws = sorted(w for _, w in sizes)
        print("ch min/med/max", ws[0], ws[len(ws) // 2], ws[-1])
    print("obscure leftover popular", dict(hits) if hits else "none")
    print("docx", docx.name if docx else "MISSING", f"{sz / 1e6:.1f}MB" if sz else "")
    print("status", (root / "00_Status.md").exists(), "kdp", (root / "KDP_Description.md").exists())
    print()
