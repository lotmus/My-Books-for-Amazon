# -*- coding: utf-8 -*-
import re
from pathlib import Path
from collections import Counter

root = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\The Universe Has No Now - Manuscript")
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

chapters = []
for name in parts:
    text = (root / name).read_text(encoding="utf-8")
    bits = re.split(r"\n(?=## )", text)
    for bit in bits:
        m = re.match(r"## (.+)", bit)
        if not m:
            continue
        title = m.group(1).strip()
        body = bit.split("\n", 1)[1] if "\n" in bit else ""
        # drop image lines
        body_no_img = re.sub(r"!\[.*?\]\([^)]+\)", "", body)
        chapters.append((name, title, len(words(body_no_img)), body_no_img))

print("CHAPTERS")
total = 0
for name, title, n, _ in chapters:
    total += n
    print(f"{n:5d}  {title[:70]}")
print("TOTAL", total)

# refrain hits in popular text only (not appendix)
popular = [c for c in chapters if not c[0].startswith("11_")]
blob = "\n".join(c[3] for c in popular)
phrases = [
    "look first",
    "seed later",
    "does not have an opinion",
    "the universe still",
    "Appendix A",
    "hot",
    "warm",
    "cold",
    "Mara",
    "basil",
    "pH",
    "where ",
    "You do not need",
    "string theory",
    "Omega",
    "forever-mind",
    "Forever-mind",
    "craftsman",
    "filter",
]
print("\nPHRASES in popular+front")
low = blob.lower()
for p in phrases:
    print(f"{low.count(p.lower()):5d}  {p}")

# repeated sentences (normalized), length > 12 words
sents = re.split(r"(?<=[.!?])\s+", blob)
norm = []
for s in sents:
    s2 = re.sub(r"\s+", " ", s).strip()
    if len(words(s2)) >= 12:
        norm.append(s2)
cnt = Counter(norm)
print("\nREPEATED SENTENCES (>=12 words, count>=2)")
for s, k in cnt.most_common(25):
    if k < 2:
        break
    print(f"{k:3d}  {s[:160]}")

# closing refrain: last 80 words of each popular chapter
print("\nCLOSERS")
for name, title, n, body in popular:
    if not re.match(r"(\d+\.|Prologue)", title):
        continue
    tail = " ".join(words(body)[-40:])
    print(f"\n-- {title[:50]} ({n})")
    print(tail[:280])
