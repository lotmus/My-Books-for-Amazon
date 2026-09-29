# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_rev9_extract")

# Print condensed first/last thirds of Ch12-14 for plot
for name in [
    "Chapter 12 _ The Hologram Problem.txt",
    "Chapter 13 _ Everything Everywhere All at Once.txt",
    "Chapter 14 _ The Station That Wasn_t Quite There.txt",
]:
    lines = (out / name).read_text(encoding="utf-8").splitlines()
    print("=" * 60, name, len(lines))
    n = len(lines)
    for i in list(range(0, min(40, n))) + list(range(n // 2 - 15, n // 2 + 15)) + list(range(max(0, n - 40), n)):
        if 0 <= i < n:
            print(f"{i+1}: {lines[i][:180]}")
    print()
