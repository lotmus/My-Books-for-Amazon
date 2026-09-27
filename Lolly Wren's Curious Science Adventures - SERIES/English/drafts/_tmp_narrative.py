# -*- coding: utf-8 -*-
"""Condensed narrative summary: extract dialogue-heavy plot beats skipping equation dumps."""
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_rev9_extract")

# For each chapter, extract lines that look like plot (not pure equation)
eq_heavy = re.compile(r"^(He wrote|She wrote|Derek wrote|Weinstein wrote|Then:|INERTIAL|LORENTZ|EVENT|FRAME|TIME|PROPER|INTERVAL|gamma|γ|=|≈)")
plotish = re.compile(
    r"\"|photograph|clock|murder|Weinstein|train|station|cucumber|dolphin|Sherlock|"
    r"Mrs Marsh|Pendleton|Barbarian|Tabitha|LOCALHOST|Case|dead|killed|perpetrator|"
    r"singularity|corridor|door|apple|hologram|arrived|Platform|11:|Trevor|Penny|"
    r"Derek|message|email|computer|frame|proper time|liar|solution|explained|"
    r"other Derek|second Derek|empty station|Munich|Bureau",
    re.I,
)

order = [
    "Chapter 1 _ The Surprise in the Morning.txt",
    "Chapter 2 _ Case 1047.txt",
    "Chapter 3 _ The Lorentz Transform.txt",
    "Chapter 4 _ The Weight of Time.txt",
    "Chapter 5 _ The Man Who Had Mislaid Time.txt",
    "Chapter 6 _ The Apple Problem.txt",
    "Chapter 7 _ The Fourth Coordinate.txt",
    "Chapter 8 _ The Cold Rain.txt",
    "Chapter 9 _ The Open-Door Principle.txt",
    "Chapter 10 _ The Relativistic Ride.txt",
    "Chapter 11 _ The Ordinary Cucumber Problem.txt",
    "Chapter 12 _ The Hologram Problem.txt",
    "Chapter 13 _ Everything Everywhere All at Once.txt",
    "Chapter 14 _ The Station That Wasn_t Quite There.txt",
]

parts = []
for name in order:
    lines = (out / name).read_text(encoding="utf-8").splitlines()
    # Keep every dialogue line + key narrative; thin equation blocks
    keep = []
    for i, line in enumerate(lines):
        if eq_heavy.search(line) and not plotish.search(line):
            continue
        if plotish.search(line) or (line.startswith('"') or '"' in line[:3]):
            keep.append(f"{i+1}|{line[:180]}")
    # Downsample long chapters to ~60 lines evenly
    if len(keep) > 55:
        step = max(1, len(keep) // 55)
        keep = [keep[0]] + keep[1:-1:step] + [keep[-1]]
        keep = keep[:60]
    parts.append("=" * 70)
    parts.append(f"{name} kept={len(keep)} of {len(lines)}")
    parts.extend(keep)

dest = out / "_narrative_condensed.txt"
dest.write_text("\n".join(parts), encoding="utf-8")
print("wrote", dest.stat().st_size)
