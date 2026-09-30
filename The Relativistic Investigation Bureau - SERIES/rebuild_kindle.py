# -*- coding: utf-8 -*-
"""Rebuild KINDLE_READY.docx from manuscript_text.txt."""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "manuscript_text.txt"
OUT = ROOT / "FINAL_REV10_The_Murder_That_Hadnt_Happened_Yet_KINDLE_READY.docx"
NAVY = RGBColor(0x0C, 0x44, 0x7C)
URL_RE = re.compile(r"(https://[^\s]+)")

HEAD_START = (
    "Chapter ",
    "Lesson ",
    "PROLOGUE",
    "EPILOGUE",
    "COURSE",
    "WORKSHOP",
    "SUMMARY",
    "GLOSSARY",
    "BIBLIOGRAPHY",
    "ACKNOWLEDGEMENTS",
    "FURTHER READING",
    "How to Read",
    "Author's Note",
    "Copyright Stuff",
    "Reality Check",
    "Coming Next",
    "Table of Contents",
    "One Last Thing",
    "Syllabus Map",
    "About the Author",
    "Interlude",
)

FIGURES = [
    ("Drag the velocity yourself", ROOT / "coordinates.png"),
    ("Watch a particle trace its geodesic", ROOT / "formula.jpg"),
    ("Lesson 8\nThe Door", ROOT / "newDoor.png"),
    ("Lesson 11\nThe Hologram", ROOT / "Appendix_11_Holographic_Principle_REVISED.png"),
    ("Mrs Marsh keeps a form for Pending Geometry", ROOT / "cabinet hole.png"),
]


def set_run_font(run, name="Georgia", size=11, bold=False, color=None, heading=False):
    run.font.size = Pt(size)
    run.bold = bold
    run.font.name = name
    r = run._element
    rPr = r.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    prefer = "Amazon Ember" if heading else name
    rFonts.set(qn("w:ascii"), prefer)
    rFonts.set(qn("w:hAnsi"), prefer)
    rFonts.set(qn("w:eastAsia"), prefer)
    if color is not None:
        run.font.color.rgb = color


def add_hyperlink(paragraph, url, text):
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(color)
    rPr.append(u)
    new_run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def is_heading(line: str, nxt: str) -> bool:
    if not line or line.startswith("->") or line.startswith("<-") or line.startswith("→"):
        return False
    if line.startswith(HEAD_START):
        return True
    if line in {
        "The Murder That Hadn't Happened Yet",
        "A Relativistic Investigation Bureau Mystery",
        "The Surprise in the Morning",
        "Sophie",
        "Spacetime for Investigators",
        "The Twin Paradox",
        "In Which the Universe Refuses to Behave",
        "The Relativistic Investigation Bureau Discovers That",
        "Solving One Mystery Is Merely an Invitation to Acquire Another",
        "The Wrong Kind of Multiverse",
    }:
        return True
    return False


def add_body(doc, text: str):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    pos = 0
    for m in URL_RE.finditer(text):
        if m.start() > pos:
            run = p.add_run(text[pos : m.start()])
            set_run_font(run)
        add_hyperlink(p, m.group(1).rstrip(").,;"), m.group(1).rstrip(").,;"))
        pos = m.end()
    if pos == 0:
        run = p.add_run(text)
        set_run_font(run)
    elif pos < len(text):
        run = p.add_run(text[pos:])
        set_run_font(run)
    return p


def add_heading_line(doc, text: str, first=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6 if first else 16)
    p.paragraph_format.space_after = Pt(10)
    run = p.add_run(text)
    size = 26 if first else 18
    set_run_font(run, name="Amazon Ember", size=size, bold=True, color=NAVY, heading=True)
    return p


def maybe_figure(doc, joined_tail: str, used: set):
    for key, path in FIGURES:
        if key in used or not path.exists():
            continue
        if key in joined_tail:
            try:
                doc.add_picture(str(path), width=Inches(5.2))
                last = doc.paragraphs[-1]
                last.alignment = WD_ALIGN_PARAGRAPH.CENTER
                used.add(key)
            except Exception:
                pass


def main():
    lines = SRC.read_text(encoding="utf-8").splitlines()
    doc = Document()
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)

    used = set()
    i = 0
    first = True
    while i < len(lines):
        line = lines[i].rstrip()
        nxt = lines[i + 1].rstrip() if i + 1 < len(lines) else ""
        if not line:
            i += 1
            continue
        if is_heading(line, nxt):
            add_heading_line(doc, line, first=first)
            first = False
            tail = "\n".join(lines[i : i + 4])
            maybe_figure(doc, tail, used)
        else:
            add_body(doc, line)
            maybe_figure(doc, "\n".join(lines[max(0, i - 2) : i + 3]), used)
        i += 1

    doc.save(OUT)
    print("Wrote", OUT, "paragraphs", len(doc.paragraphs))


if __name__ == "__main__":
    main()
