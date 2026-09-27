#!/usr/bin/env python3
"""Builds the final Kindle-ready .docx manuscript.

1. Builds a reference.docx (python-docx) defining every named style the
   chapter markdown references via pandoc's `custom-style` Div attribute,
   including page_break_before on Heading 1/2 (matches the pagination fix
   already proven on the EE series -- every Part/Chapter heading forces a
   fresh page, set once on the style rather than patched per-heading later).
2. Runs pandoc (chapters/*.md -> docx) against that reference doc.
3. Sets core document properties (title/author) on the result.

Re-run this after any change to chapters/*.md or to the styles below.
"""

import subprocess
import sys
import os

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
REFERENCE = os.path.join(HERE, "reference.docx")
OUTPUT = os.path.join(HERE, "How to Publish and Make Good Money - Complete Manuscript.docx")

BLUE = RGBColor(0x2A, 0x78, 0xD6)
INK = RGBColor(0x0B, 0x0B, 0x0B)
INK_SECONDARY = RGBColor(0x52, 0x51, 0x4E)
DARK_BLUE = RGBColor(0x18, 0x4F, 0x95)
DARK_GREEN = RGBColor(0x0D, 0x6B, 0x4A)
DARK_VIOLET = RGBColor(0x3A, 0x2F, 0x86)

FONT = "Calibri"


def get_or_add_style(doc, name, style_type=WD_STYLE_TYPE.PARAGRAPH, base=None):
    styles = doc.styles
    existing = None
    for s in styles:
        if s.name == name and s.type == style_type:
            existing = s
            break
    style = existing if existing is not None else styles.add_style(name, style_type)
    if base is not None:
        style.base_style = styles[base]
    return style


def style_paragraph_font(style, size=11, bold=False, italic=False, color=INK,
                          align=None, space_before=0, space_after=8,
                          left_indent=None, right_indent=None,
                          page_break_before=False, line_spacing=1.15,
                          keep_with_next=False):
    style.font.name = FONT
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.italic = italic
    style.font.color.rgb = color
    # Ensure east-asian/complex-script font fallback matches (avoids Word
    # substituting a different default font for some glyph ranges).
    rpr = style.element.get_or_add_rPr()
    rFonts = rpr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rFonts)
    rFonts.set(qn("w:ascii"), FONT)
    rFonts.set(qn("w:hAnsi"), FONT)
    rFonts.set(qn("w:cs"), FONT)

    pf = style.paragraph_format
    if align is not None:
        pf.alignment = align
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line_spacing
    if left_indent is not None:
        pf.left_indent = Inches(left_indent)
    if right_indent is not None:
        pf.right_indent = Inches(right_indent)
    pf.page_break_before = page_break_before
    pf.keep_with_next = keep_with_next


def build_reference_doc():
    doc = Document()

    section = doc.sections[0]
    section.page_width = Inches(6)
    section.page_height = Inches(9)
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.7)
    section.gutter = Inches(0.2)

    normal = doc.styles["Normal"]
    style_paragraph_font(normal, size=11, color=INK, space_after=10, line_spacing=1.2)

    h1 = doc.styles["Heading 1"]
    style_paragraph_font(h1, size=21, bold=True, color=BLUE,
                          align=WD_ALIGN_PARAGRAPH.CENTER,
                          space_before=0, space_after=20,
                          page_break_before=True, keep_with_next=True)

    h2 = doc.styles["Heading 2"]
    style_paragraph_font(h2, size=16, bold=True, color=BLUE,
                          align=WD_ALIGN_PARAGRAPH.CENTER,
                          space_before=0, space_after=16,
                          page_break_before=True, keep_with_next=True)

    h3 = doc.styles["Heading 3"]
    style_paragraph_font(h3, size=12.5, bold=True, color=DARK_BLUE,
                          align=WD_ALIGN_PARAGRAPH.LEFT,
                          space_before=16, space_after=6,
                          page_break_before=False, keep_with_next=True)

    title_style = get_or_add_style(doc, "TitlePageTitle", base="Normal")
    style_paragraph_font(title_style, size=29, bold=True, color=BLUE,
                          align=WD_ALIGN_PARAGRAPH.CENTER,
                          space_before=40, space_after=8)

    subtitle_style = get_or_add_style(doc, "BookSubtitle", base="Normal")
    style_paragraph_font(subtitle_style, size=14.5, italic=True, color=INK_SECONDARY,
                          align=WD_ALIGN_PARAGRAPH.CENTER,
                          space_before=4, space_after=24)

    author_style = get_or_add_style(doc, "BookAuthor", base="Normal")
    style_paragraph_font(author_style, size=14, bold=True, color=INK,
                          align=WD_ALIGN_PARAGRAPH.CENTER,
                          space_before=40, space_after=8)

    copyright_style = get_or_add_style(doc, "CopyrightText", base="Normal")
    style_paragraph_font(copyright_style, size=9.5, color=INK_SECONDARY,
                          align=WD_ALIGN_PARAGRAPH.LEFT,
                          space_before=0, space_after=10, line_spacing=1.3)

    toc_style = get_or_add_style(doc, "TOCEntry", base="Normal")
    style_paragraph_font(toc_style, size=11.5, color=INK,
                          align=WD_ALIGN_PARAGRAPH.CENTER,
                          space_before=0, space_after=7)

    key_style = get_or_add_style(doc, "KeyTakeaway", base="Normal")
    style_paragraph_font(key_style, size=10.5, italic=True, color=DARK_BLUE,
                          align=WD_ALIGN_PARAGRAPH.LEFT,
                          space_before=10, space_after=12,
                          left_indent=0.35, right_indent=0.35)

    worked_style = get_or_add_style(doc, "WorkedExample", base="Normal")
    style_paragraph_font(worked_style, size=10.5, italic=False, color=DARK_GREEN,
                          align=WD_ALIGN_PARAGRAPH.LEFT,
                          space_before=10, space_after=12,
                          left_indent=0.35, right_indent=0.2)

    case_style = get_or_add_style(doc, "CaseStudy", base="Normal")
    style_paragraph_font(case_style, size=10.5, italic=True, color=DARK_VIOLET,
                          align=WD_ALIGN_PARAGRAPH.LEFT,
                          space_before=10, space_after=12,
                          left_indent=0.35, right_indent=0.2)

    caption_style = get_or_add_style(doc, "FigureCaption", base="Normal")
    style_paragraph_font(caption_style, size=9.5, italic=True, color=INK_SECONDARY,
                          align=WD_ALIGN_PARAGRAPH.CENTER,
                          space_before=4, space_after=18)

    checklist_style = get_or_add_style(doc, "ChecklistItem", base="Normal")
    style_paragraph_font(checklist_style, size=10.8, color=INK,
                          align=WD_ALIGN_PARAGRAPH.LEFT,
                          space_before=0, space_after=6,
                          left_indent=0.15)

    doc.save(REFERENCE)
    print("wrote", REFERENCE)


def run_pandoc():
    chapters_dir = os.path.join(HERE, "chapters")
    inputs = [
        "00-front-matter.md",
        "part1-the-landscape.md",
        "part2-writing-producing.md",
        "part3-getting-discovered.md",
        "part4-business-side.md",
        "part5-long-game.md",
        "99-back-matter.md",
    ]
    input_paths = [os.path.join(chapters_dir, f) for f in inputs]
    for p in input_paths:
        if not os.path.exists(p):
            sys.exit(f"missing chapter file: {p}")

    cmd = [
        "pandoc",
        *input_paths,
        "--from=markdown+raw_attribute",
        "--to=docx",
        f"--reference-doc={REFERENCE}",
        f"--resource-path={HERE}",
        "-o", OUTPUT,
    ]
    # Deliberately no --metadata title=/author= here: pandoc's docx writer
    # renders those as a SECOND, auto-generated title block (its own
    # built-in Title/Subtitle/Author styles) on top of the hand-authored
    # title page in 00-front-matter.md, duplicating it. Core document
    # properties are set directly below instead, after conversion.
    print("running:", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=HERE)
    print("wrote", OUTPUT)

    doc = Document(OUTPUT)
    doc.core_properties.title = "How to Publish and Make Good Money"
    doc.core_properties.author = "Lothar J. Musiol"
    doc.core_properties.language = "en-US"
    doc.save(OUTPUT)
    print("set core properties (title/author/language)")


if __name__ == "__main__":
    build_reference_doc()
    run_pandoc()
