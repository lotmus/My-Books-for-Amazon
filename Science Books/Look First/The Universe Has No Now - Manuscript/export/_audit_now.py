# -*- coding: utf-8 -*-
"""Book 1 audit against the part files, the assembled markdown, and the Kindle docx."""
import os
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
parts = [
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


def words(s):
    return re.findall(r"[A-Za-z0-9’']+", s)


chunks = [(n, (root / n).read_text(encoding="utf-8")) for n in parts]
text = "\n".join(t for _, t in chunks)
print("SOURCE WORDS", len(words(text)))

nums = []
print("--- chapter sizes ---")
for name, raw in chunks:
    if name.startswith("00") or name.startswith("11"):
        continue
    for sec in re.split(r"(?=^##\s+)", raw, flags=re.M):
        m = re.match(r"^##\s+(\d+)\.\s+(.+)$", sec)
        if not m:
            continue
        n = int(m.group(1))
        title = m.group(2).strip()
        body = re.sub(r"!\[.*?\]\(.*?\)", " ", sec)
        wc = len(words(body))
        nums.append(n)
        flag = " BRIDGE" if wc < 400 else (" SHORT" if wc < 1500 else "")
        print(f"  {n:02d} {wc:5d}{flag}  {title[:60]}")
print("missing 1-45", [i for i in range(1, 46) if i not in nums])
print("dups", sorted({i for i in nums if nums.count(i) > 1}))

ax = sorted({int(n) for n in re.findall(r"^##\s+A(\d+)\.", text, re.M)})
print("appendix", len(ax), "missing", [i for i in range(0, 46) if i not in ax])

figs = [int(x) for x in re.findall(r"!\[Figure\s+(\d+)\.", text)]
print("fig embeds", len(figs), "missing", [i for i in range(0, 46) if i not in set(figs)])

missing_files = []
for i in range(0, 46):
    hits = list((root / "Figures" / "figs").glob(f"fig{i:02d}.*"))
    hits += list((root / "Figures").glob(f"fig{i:02d}.*"))
    real = [p for p in hits if "_slot" not in p.name]
    if not real:
        missing_files.append(i)
print("missing figure files", missing_files)

chap_set = set(range(1, 46))
print("--- chapter refs outside 1-45 ---")
for n, raw in chunks:
    for m in re.finditer(r"Chapter\s+(\d+)", raw):
        k = int(m.group(1))
        if k not in chap_set:
            line = raw[: m.start()].count("\n") + 1
            snip = raw[max(0, m.start() - 40) : m.end() + 30].replace("\n", " ")
            print(f"  {n}:{line} ch{k}  {snip}")

print("--- appendix refs with no note ---")
for n, raw in chunks:
    for m in re.finditer(r"\bA(\d+)\b", raw):
        k = int(m.group(1))
        if k > 45:
            line = raw[: m.start()].count("\n") + 1
            print(f"  {n}:{line} A{k}")

for name, pat in (
    ("film", r"\b(Interstellar|The Martian|Star Wars|Star Trek)\b"),
    ("todo", r"\b(TODO|FIXME|PLACEHOLDER)\b"),
    ("mojibake", r"Ã.|Â[\x80-\xbf]|â€™|â€œ|â€”"),
):
    print(name, len(re.findall(pat, text)))

asm = root / "The_Universe_Has_No_Now.md"
src6 = (root / "06_Part_Six_Getting_There.md").read_text(encoding="utf-8")


def grab(s, n):
    m = re.search(rf"^##\s+{n}\.\s+.+?(?=^##\s+\d+\.|\Z)", s, re.M | re.S)
    return len(words(m.group(0))) if m else -1


if asm.is_file():
    a = asm.read_text(encoding="utf-8")
    print("ASSEMBLED words", len(words(a)))
    for n in (31, 32):
        print(f"  ch{n} source {grab(src6, n)} assembled {grab(a, n)}")
else:
    print("no assembled md")

# promises that Chapter 31/32 will teach something the bridge may not hold
print("--- pointers at 31 or 32 ---")
for n, raw in chunks:
    if n.startswith("11"):
        continue
    for m in re.finditer(r".{0,80}Chapter 3[12].{0,80}", raw):
        line = raw[: m.start()].count("\n") + 1
        snip = re.sub(r"\s+", " ", m.group(0))
        print(f"  {n}:{line}  {snip[:160]}")
