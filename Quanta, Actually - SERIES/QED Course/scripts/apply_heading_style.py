"""Apply Amazon Ember / blue / centered / bold styling to headline styles.

Blue = RGB(0,0,255), matched from the user-supplied reference image.
Sizes: Title 30pt (unchanged), Heading 1 18pt, Heading 2 16pt, Heading 3 14pt,
Subtitle 14pt (unchanged size, restyled to match font/color family).
Modifies STYLE DEFINITIONS only (not per-run overrides), so it applies
retroactively to every paragraph already using these styles, and will
continue to apply automatically to any lesson built later by build_lesson.py,
since that script assigns heading paragraphs by style name only.
"""
import sys
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

BLUE = RGBColor(0x00, 0x00, 0xFF)
FONT_NAME = "Amazon Ember"

TARGETS = {
    "Title": {"size": Pt(30), "bold": True},
    "Subtitle": {"size": Pt(14), "bold": True},
    "Heading 1": {"size": Pt(18), "bold": True},
    "Heading 2": {"size": Pt(16), "bold": True},
    "Heading 3": {"size": Pt(14), "bold": True},
}


def set_style_font(style, size, bold):
    font = style.font
    font.name = FONT_NAME
    font.size = size
    font.bold = bold
    font.color.rgb = BLUE
    # Also set eastasia/complex-script typeface so Word doesn't substitute
    # a different font for any non-ASCII glyph (Greek letters, arrows, etc.
    # appear throughout this book's math text).
    rpr = style.element.get_or_add_rPr()
    rFonts = rpr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.insert(0, rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rFonts.set(qn(attr), FONT_NAME)
    pf = style.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.CENTER


def main(path):
    doc = docx.Document(path)
    for name, spec in TARGETS.items():
        style = doc.styles[name]
        set_style_font(style, spec["size"], spec["bold"])
        print("updated style:", name)
    doc.save(path)
    print("saved:", path)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "Quantum, Actually - Volume 2.docx")
