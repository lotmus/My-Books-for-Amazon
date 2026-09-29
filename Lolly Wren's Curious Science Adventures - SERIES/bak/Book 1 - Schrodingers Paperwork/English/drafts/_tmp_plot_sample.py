# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_rev9_extract")

order = [
    ("Ch1", "Chapter 1 _ The Surprise in the Morning.txt"),
    ("Ch2", "Chapter 2 _ Case 1047.txt"),
    ("Ch3", "Chapter 3 _ The Lorentz Transform.txt"),
    ("Ch4", "Chapter 4 _ The Weight of Time.txt"),
    ("Ch5", "Chapter 5 _ The Man Who Had Mislaid Time.txt"),
    ("Ch6", "Chapter 6 _ The Apple Problem.txt"),
    ("Ch7", "Chapter 7 _ The Fourth Coordinate.txt"),
    ("Ch8", "Chapter 8 _ The Cold Rain.txt"),
    ("Ch9", "Chapter 9 _ The Open-Door Principle.txt"),
    ("Ch10", "Chapter 10 _ The Relativistic Ride.txt"),
    ("Ch11", "Chapter 11 _ The Ordinary Cucumber Problem.txt"),
    ("Ch12", "Chapter 12 _ The Hologram Problem.txt"),
    ("Ch13", "Chapter 13 _ Everything Everywhere All at Once.txt"),
    ("Ch14", "Chapter 14 _ The Station That Wasn_t Quite There.txt"),
    ("Ch15", "Chapter 15 _ The Distant Train That Arrived Before It Left.txt"),
]

# Keywords for plot extraction
keys = re.compile(
    r"murder|victim|perpetrator|Weinstein|photograph|clock|train|station|Platform|"
    r"LOCALHOST|Case 1047|11:03|11:17|cucumber|dolphin|Sherlock|Mrs Marsh|Pendleton|"
    r"Barbarian|dead|killed|frame|proper time|singularity|corridor|geodesic|"
    r"hologram|apple|door|arrived before|other Derek|himself|suicide|"
    r"solution|explained|liar|filed|future",
    re.I,
)

parts = []
for label, name in order:
    lines = (out / name).read_text(encoding="utf-8").splitlines()
    parts.append("=" * 70)
    parts.append(f"{label}: {name} ({len(lines)} lines)")
    # sample every Nth dialogue-ish line that matches keys, plus first/last
    hits = []
    for i, line in enumerate(lines):
        if keys.search(line) and len(line) > 20:
            hits.append(f"{i+1}: {line[:200]}")
    # take evenly spaced hits if too many
    if len(hits) > 40:
        step = len(hits) // 40
        hits = hits[::step][:40]
    parts.extend(hits)
    parts.append("--- END SAMPLE ---")
    parts.extend(f"TAIL {i}: {l[:200]}" for i, l in enumerate(lines[-15:], start=len(lines)-14))

dest = out / "_plot_samples.txt"
dest.write_text("\n".join(parts), encoding="utf-8")
print("wrote", dest, dest.stat().st_size)
