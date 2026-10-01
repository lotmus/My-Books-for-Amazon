# -*- coding: utf-8 -*-
from pathlib import Path
import os
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

BLOCKS = {
    13: (
        "04_Part_Four_The_Honest_Body.md",
        r"^## 14\.",
        (
            "Keep the receipt. Name eligible as three clocks at once. "
            "Refuse helium as a schedule for everyone. Staff cannot be downloaded. "
            "Translation from mouse to woman is unpaid. Price is delivery. "
            "Boring wins still land. That is medicine as invoice, not as downtown."
        ),
    ),
    15: (
        "04_Part_Four_The_Honest_Body.md",
        r"^## 16\.",
        (
            "A second person who thinks they remember your Tuesdays is still not travel. "
            "The first person stays in the meat. Forever-mind fuses three colds into one coat. "
            "Hang them apart until each earns a temperature. Take the local restoration if Tuesday votes. "
            "Refuse the pour. Bodies end. Copies do not travel. Coat off the bench. "
            "That is the whole chapter in a colder mouth."
        ),
    ),
    16: (
        "04_Part_Four_The_Honest_Body.md",
        r"^Do not wait for helium\.\s*$",
        (
            "Final count stands: late capsule, optimistic label, joint scored two, "
            "Tuesday worth repeating, notebook present, spare mind absent, "
            "file-that-is-her absent, year twelve thousand absent, "
            "film going alkaline when permanence gets soft. "
            "The honest body is that size. Not small. Reliably for sale. "
            "The radio will be late. Light does not care. "
            "Care about the Tuesday in this kitchen and the Tuesday that did not get the capsule. "
            "Seal it. Do not wait for helium."
        ),
    ),
}


def wc(text: str) -> int:
    body = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    body = re.sub(r"^#+\s+.*$", " ", body, flags=re.M)
    return len(re.findall(r"[A-Za-z0-9\u2019']+", body))


def sizes(text: str):
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


def main() -> None:
    for n, (fn, pat, block) in BLOCKS.items():
        p = ROOT / fn
        t = p.read_text(encoding="utf-8")
        m = re.search(pat, t, re.M)
        if not m:
            print("no", n)
            continue
        t = t[: m.start()] + "---\n\n" + block + "\n\n" + t[m.start() :]
        p.write_text(t, encoding="utf-8", newline="\n")
        print("ins", n)

    parts = [
        f
        for f in sorted(os.listdir(ROOT))
        if re.match(r"^\d{2}_", f)
        and f.endswith(".md")
        and f not in ("00_Chapter_Outline.md", "00_Figure_Plan.md", "00_Status.md")
    ]
    big = "\n\n".join((ROOT / p).read_text(encoding="utf-8") for p in parts)
    total = wc(big)
    print("TOTAL", total)
    thin = []
    for n, w in sizes(big):
        mark = " THIN" if w < 1500 else ""
        print(f"Ch {n:02d} {w:5d}{mark}")
        if w < 1500:
            thin.append((n, w))
    print("thin", thin)

    st = (ROOT / "00_Status.md").read_text(encoding="utf-8")
    st = re.sub(r"\*\*[\d,]+ words\*\*", f"**{total:,} words**", st)
    st = re.sub(
        r"Thin leftovers \(if any\):.*",
        f"Thin leftovers (if any): {thin or 'none'}.",
        st,
    )
    (ROOT / "00_Status.md").write_text(st, encoding="utf-8", newline="\n")

    r = subprocess.run(
        [sys.executable, str(ROOT / "Figures" / "build_book.py"), "body"],
        capture_output=True,
        text=True,
    )
    print(r.stdout)
    if r.returncode:
        print(r.stderr)
        raise SystemExit(r.returncode)


if __name__ == "__main__":
    main()
