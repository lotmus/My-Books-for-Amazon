"""One-shot content audit for Book 1. Not part of the Kindle build."""
from __future__ import annotations

import os
import re
import sys

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = [
    "00_Front_Matter.md",
    "01_Part_One_No_Now.md",
    "02_Part_Two_Past.md",
    "03_Part_Three_Burst.md",
    "04_Part_Four_Missing.md",
    "05_Part_Five_Horizons.md",
    "06_Part_Six_Getting_There.md",
    "07_Part_Seven_Loops.md",
    "08_Part_Eight_Copies.md",
    "09_Part_Nine_Filter.md",
    "10_Part_Ten_Future.md",
    "11_Appendix.md",
]


def main() -> int:
    chunks: list[tuple[str, str]] = []
    for name in PARTS:
        path = os.path.join(SRC, name)
        raw = open(path, encoding="utf-8").read()
        chunks.append((name, raw))
        print(f"{name}: {len(raw.split())} words")

    text = "\n\n".join(f"===== {n} =====\n\n{r}" for n, r in chunks)

    # Chapter headings (several styles)
    ch_pat = re.compile(
        r"^##\s+(?:Chapter\s+)?(\d+)[\.:\s—\-]+(.+)$", re.M
    )
    ch = ch_pat.findall(text)
    # Prefer popular-part chapters only for 1-45 presence; appendix has A-notes
    pop = "\n\n".join(r for n, r in chunks if n != "11_Appendix.md")
    ch_pop = ch_pat.findall(pop)
    nums = sorted({int(n) for n, _ in ch_pop})
    print("popular chapter nums:", len(nums), "range", (nums[0], nums[-1]) if nums else None)
    print("missing chapters 1-45:", [i for i in range(1, 46) if i not in nums])

    ax = re.findall(r"^##\s+A(\d+)[\.:\s—\-]+(.+)$", text, re.M)
    ax_nums = sorted({int(n) for n, _ in ax})
    print("appendix A notes:", len(ax_nums), "missing:", [i for i in range(0, 46) if i not in ax_nums])

    figs = [int(x) for x in re.findall(r"!\[Figure\s+(\d+)\.", text)]
    print("figure embeds in parts:", len(figs), "unique", sorted(set(figs)))
    print("missing fig embeds 0-45:", [i for i in range(0, 46) if i not in set(figs)])

    # Per-chapter body word counts (between ## headings in popular parts)
    print("\n=== popular chapter body sizes (words between ##) ===")
    thin = []
    for name, raw in chunks:
        if name in ("00_Front_Matter.md", "11_Appendix.md"):
            continue
        sections = re.split(r"(?=^##\s+)", raw, flags=re.M)
        for sec in sections:
            m = re.match(r"^##\s+(?:Chapter\s+)?(\d+)[\.:\s—\-]+(.+)$", sec, re.M)
            if not m:
                continue
            n = int(m.group(1))
            title = m.group(2).strip()
            body = re.sub(r"!\[.*?\]\(.*?\)", " ", sec)
            body = re.sub(r"^#+\s+.*$", " ", body, flags=re.M)
            words = re.findall(r"[A-Za-z0-9’']+", body)
            wc = len(words)
            flag = " THIN" if wc < 1500 and n not in (0,) else ""
            if flag:
                thin.append((n, wc, title))
            print(f"  Ch {n:02d} {wc:5d}  {title[:60]}{flag}")
    print("thin chapters (<1500 body words):", thin)

    checks = [
        ("Chapter 52 leftover", r"Chapter\s+52"),
        ("Fig 52+ leftover", r"Fig(?:ure)?\s*5[2-9]"),
        ("mojibake latin1", r"(Ã.|Â.|â€™|â€œ|â€|â€”)"),
        ("TODO/FIXME/PLACEHOLDER", r"\b(TODO|FIXME|PLACEHOLDER|lorem ipsum|\[insert)\b"),
        ("film titles", r"\b(Interstellar|Arrival|The Martian|Star Wars|Star Trek)\b"),
        ("raw html", r"<(?:div|span|br|img)\b"),
        ("stale slot talk", r"framed placeholder|drop-in JPEG|to-be-licensed"),
        ("Contact the movie", r"\bContact\b"),
        ("full brain 10%", r"10%\s+of\s+(?:the\s+)?brain|only use 10"),
        ("CRISPR fountain", r"CRISPR"),
        ("unescaped markdown leak **", r"\*\*[^*\n]{0,40}\*\*"),
        ("literal backtick fence", r"```"),
    ]
    print("\n=== pattern checks ===")
    for name, pat in checks:
        hits = list(re.finditer(pat, text, re.I))
        print(f"{name}: {len(hits)}")
        for h in hits[:6]:
            # locate file
            pos = h.start()
            file_hint = "?"
            for n, r in chunks:
                block = f"===== {n} =====\n\n{r}"
                # approximate: search within combined
            snip = text[max(0, h.start() - 35) : h.end() + 55].replace("\n", " ")
            print(f"  ...{snip}...")

    # Caption vs plan soft checks for earthly photos
    print("\n=== fig caption lines (0,1,31,32,34,42) ===")
    for n in (0, 1, 31, 32, 34, 42):
        m = re.search(rf"!\[Figure\s+{n}\.\s*([^\]]+)\]", text)
        print(f"Fig {n}: {m.group(1) if m else 'MISSING'}")

    # Front matter order markers
    front = chunks[0][1]
    print("\n=== front matter markers ===")
    for needle in (
        "Lothar J. Musiol",
        "How to Read",
        "Look First",
        "Author",
        "%%TOC%%",
        "Prologue",
    ):
        print(f"  {needle}: {'yes' if needle.lower() in front.lower() else 'NO'}")

    # Quote balance rough
    dq = text.count('"')
    print(f"\ndouble-quote count: {dq} ({'even' if dq % 2 == 0 else 'ODD'})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
