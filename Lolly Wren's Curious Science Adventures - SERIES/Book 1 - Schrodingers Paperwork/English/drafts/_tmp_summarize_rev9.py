# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_rev9_extract")

gags = [
    r"cucumber", r"dolphin", r"singularit", r"bureaucracy|bureaucratic|Inland Revenue|forms?\b|appointment",
    r"tea\b", r"Tuesday", r"11:03|11:17|seventeen", r"Weinstein", r"LGV", r"clock",
    r"murder", r"photograph", r"frame", r"proper time", r"Lorentz", r"apple",
    r"hologram", r"train", r"station", r"Sherlock", r"causality",
]

# Per-chapter: first 40 lines + last 25 lines + gag hits
files = sorted(out.glob("*.txt"), key=lambda p: p.stat().st_mtime)
# Better order by name list
order = [
    "PROLOGUE.txt",
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
    "Chapter 15 _ The Distant Train That Arrived Before It Left.txt",
    "Chapter 16 _ Sherlock and the Final Geometry.txt",
    "EPILOGUE.txt",
]

summary_path = out / "_summary_heads.txt"
parts = []
for name in order:
    f = out / name
    if not f.exists():
        parts.append(f"MISSING {name}\n")
        continue
    text = f.read_text(encoding="utf-8")
    lines = text.splitlines()
    parts.append("=" * 70)
    parts.append(name)
    parts.append(f"lines={len(lines)} chars={len(text)}")
    parts.append("--- HEAD ---")
    parts.append("\n".join(lines[:45]))
    parts.append("--- TAIL ---")
    parts.append("\n".join(lines[-30:]))
    parts.append("--- GAG/KEY HITS ---")
    for pat in gags:
        hits = []
        for i, line in enumerate(lines):
            if re.search(pat, line, re.I):
                hits.append(f"  L{i+1}: {line[:140]}")
                if len(hits) >= 4:
                    break
        if hits:
            parts.append(f"[{pat}] ({sum(1 for l in lines if re.search(pat,l,re.I))} hits)")
            parts.extend(hits)
    parts.append("")

summary_path.write_text("\n".join(parts), encoding="utf-8")
print("Wrote", summary_path, "size", summary_path.stat().st_size)
