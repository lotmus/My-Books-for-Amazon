# -*- coding: utf-8 -*-
"""Deperson B2 invented cast → roles. Keep Mara/Rohan only."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

# Order matters: longer phrases first.
REPLACEMENTS = [
    ("Wei Ning, with the box open.", "A sample scientist, with the box open."),
    ("Wei Ning", "the sample scientist"),
    ("Dex, revising the board.", "A flight planner, revising the board."),
    ("Dex’s quiet column", "the quiet column on the flight board"),
    ("Dex’s", "the planner’s"),
    ("Dex ", "the planner "),
    ("Pavel, running the numbers he does not enjoy.", "An orbital analyst, running the numbers he does not enjoy."),
    ("Pavel’s simulations", "the orbital simulations"),
    ("Pavel", "the orbital analyst"),
    ("Elena’s three cards", "Three cards on the wall"),
    ("without needing Elena in the room", "without needing the facilitator in the room"),
    ("Elena’s wall", "The wall"),
    ("Elena", "the facilitator"),
    ("Nadia, reading her own gauge.", "A tide-gauge tech, reading her own gauge."),
    ("Nadia’s gauge", "the tide gauge"),
    ("Nadia", "the gauge tech"),
    ("why Linh exists in this book", "why a glove lab exists in this book"),
    ("Linh’s box of simulant", "The glove lab’s box of simulant"),
    ("Linh, in a lab that smells of powdered basalt,", "In a lab that smells of powdered basalt, a suit tech"),
    ("Linh", "the suit tech"),
    ("Nandita’s wall of versions", "The version wall"),
    ("Nandita, at the version wall.", "An architect, at the version wall."),
    ("Nandita", "the architect"),
]

RULES = {
    10: (
        "03_Part_Three_Vehicle_Not_City.md",
        "A truck is not a downtown. Count quiet flights, not hull size. Keep the empty *routine* box empty until a planner can bet a camp on it.",
    ),
    12: (
        "03_Part_Three_Vehicle_Not_City.md",
        "Sortie, outpost, settlement are three nouns. Score the seven rows. Do not let a poster promote a camp into a city.",
    ),
    15: (
        "04_Part_Four_Who_Stays.md",
        "Leaving is not a cleanup. The ambitious are a rounding error. The planet does not know we left.",
    ),
    16: (
        "04_Part_Four_Who_Stays.md",
        "The bill is paid at home. Wash the staffed world. Do not let a spare-Earth sentence spend the tide gauge.",
    ),
}


def main() -> None:
    md_files = sorted(ROOT.glob("0*_*.md")) + sorted(ROOT.glob("1*_*.md"))
    for p in md_files:
        if p.name.startswith("00_"):
            continue
        t = p.read_text(encoding="utf-8")
        orig = t
        for a, b in REPLACEMENTS:
            t = t.replace(a, b)
        if t != orig:
            p.write_text(t, encoding="utf-8", newline="\n")
            print("deperson", p.name)

    for n, (fn, rule) in RULES.items():
        p = ROOT / fn
        t = p.read_text(encoding="utf-8")
        if f"Rule: {rule[:40]}" in t or f"Rule: {rule}" in t:
            print("rule skip", n)
            continue
        cm = re.search(rf"(^## {n}\..*?)(?=^## |\Z)", t, re.M | re.S)
        if not cm:
            print("no ch", n)
            continue
        block = (
            "\n\n---\n\nWhere the popular version goes wrong.\n\n"
            "The slide promotes the noun. Look first: ask what was measured, what still needs Earth, "
            "what the checklist still leaves empty.\n\n"
            f"Rule: {rule}\n"
        )
        # avoid double if Rule already at end
        if "\nRule: " in cm.group(1):
            print("has rule", n)
            continue
        abs_end = cm.end(1)
        t = t[:abs_end].rstrip() + block + "\n" + t[abs_end:]
        p.write_text(t, encoding="utf-8", newline="\n")
        print("rule", n)

    r = subprocess.run(
        [sys.executable, str(ROOT / "Figures" / "build_book.py"), "permit"],
        capture_output=True,
        text=True,
    )
    print(r.stdout)
    if r.returncode:
        print(r.stderr)
        raise SystemExit(r.returncode)


if __name__ == "__main__":
    main()
