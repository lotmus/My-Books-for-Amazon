# -*- coding: utf-8 -*-
"""Extract plot-critical passages from late chapters and character beats."""
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_rev9_extract")

# Full prologue + epilogue
for name in ["PROLOGUE.txt", "EPILOGUE.txt"]:
    t = (out / name).read_text(encoding="utf-8")
    print("=" * 60, name)
    print(t)
    print()

# Chapter 16 full - solution
print("=" * 60, "CH16 FULL")
print((out / "Chapter 16 _ Sherlock and the Final Geometry.txt").read_text(encoding="utf-8"))
