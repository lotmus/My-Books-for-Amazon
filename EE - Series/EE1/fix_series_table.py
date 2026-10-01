# -*- coding: utf-8 -*-
"""Fix Foundations' stale 21-book table. Do not regenerate the book."""

from pathlib import Path
from docx import Document

ROOT = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\EE - Series")
PATHS = [
    ROOT / "Foundations_Book1.docx",
    ROOT / "EE1" / "Foundations_Book1.docx",
]

NINE = [
    ("Book", "Covers"),
    ("1. Foundations (this book)", "Physics, mathematics, and circuit theory"),
    ("2. Circuits, Components, and Control", "Analog and digital, op-amps, passives, the classical loop"),
    ("3. Semiconductor Physics and Devices", "Diodes, BJTs, MOSFETs, FinFET, compound semiconductors"),
    ("4. RF, Microwave, and Antennas", "Matching, lines, microwave, mmWave, antennas"),
    ("5. Communications, Wireless, and SDR", "Modulation, band plans, DSP and software radio"),
    ("6. Transceivers and High-Power RF", "Noise, PLL, PAs, combiners, radar"),
    ("7. EMC, Simulation, and Test", "Emissions, immunity, solvers, the accredited lab"),
    ("8. Power and Energy", "Regulators, magnetics, the grid, the rack"),
    ("9. Packaging, Layout, and Emerging", "Boards, packages, 2026 compute, robots, MEMS"),
]

REPL = [
    ("twenty-one", "nine"),
    ("Twenty-one", "Nine"),
    ("21-book", "nine-book"),
    ("21 books", "nine books"),
    ("other twenty books", "other eight books"),
    ("other twenty-one", "other nine"),
]


def rewrite_table(tbl):
    while len(tbl.rows) > len(NINE):
        tbl.rows[-1]._tr.getparent().remove(tbl.rows[-1]._tr)
    while len(tbl.rows) < len(NINE):
        tbl.add_row()
    for row, (a, b) in zip(tbl.rows, NINE):
        if len(row.cells) >= 2:
            row.cells[0].text = a
            row.cells[1].text = b


def fix_doc(path: Path) -> str:
    if not path.exists():
        return f"missing {path}"
    doc = Document(path)
    n_para = 0
    for p in doc.paragraphs:
        t = p.text
        new = t
        for a, b in REPL:
            new = new.replace(a, b)
        if new != t and p.runs:
            p.runs[0].text = new
            for r in p.runs[1:]:
                r.text = ""
            n_para += 1
    n_tbl = 0
    for tbl in doc.tables:
        head = tbl.rows[0].cells[0].text.strip().lower() if tbl.rows else ""
        n_rows = len(tbl.rows)
        if head.startswith("book") and n_rows >= 10:
            rewrite_table(tbl)
            n_tbl += 1
        else:
            for row in tbl.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        t = p.text
                        new = t
                        for a, b in REPL:
                            new = new.replace(a, b)
                        if new != t and p.runs:
                            p.runs[0].text = new
                            for r in p.runs[1:]:
                                r.text = ""
    doc.save(path)
    return f"{path.name}: {n_para} paragraphs, {n_tbl} series tables"


def main():
    for p in PATHS:
        print(fix_doc(p))


if __name__ == "__main__":
    main()
