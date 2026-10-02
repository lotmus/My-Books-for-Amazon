#!/usr/bin/env python3
"""Build the single master docx for Your First Book That Sells.

Reads chapters/00_*.md ... 03_*.md in order and writes
"Your First Book That Sells.docx" at the book root. Figures come from figures/.
Docx only: this script never writes PDF or EPUB.
"""
import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = sorted((ROOT / "chapters").glob("0*.md"))
FIGURES = ROOT / "figures"
OUTPUT = ROOT / "Your First Book That Sells.docx"
TITLE = "Your First Book That Sells"
SUBTITLE = "How to Publish and Make Good Money on Kindle: Real Royalties, Honest Reviews, and a Catalog That Pays"
AUTHOR = "Lothar J. Musiol"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
IMAGE_RE = re.compile(r"^!\[([^\]]*)\]\(([^)]+\.(?:png|jpg|jpeg))\)$", re.I)
CHECK_RE = re.compile(r"^- \[[ xX]?\]\s+(.*)$")
BULLET_RE = re.compile(r"^[-*•]\s+(.*)$")
NUM_RE = re.compile(r"^(\d+)\.\s+(.*)$")
RULE_RE = re.compile(r"^-{3,}$")
INLINE_RE = re.compile(r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*[^*\s][^*]*?\*|\[[^\]]+\]\([^)]+\))")
LINK_RE = re.compile(r"^\[([^\]]+)\]\(([^)]+)\)$")
HYPERLINK_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink"


def slug(text):
    return "h_" + re.sub(r"[^a-z0-9]+", "_", text.lower())[:36].strip("_")


def run_props(color):
    rpr = OxmlElement("w:rPr")
    c = OxmlElement("w:color"); c.set(qn("w:val"), color); rpr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    return rpr


def add_link(paragraph, text, url=None, anchor=None):
    h = OxmlElement("w:hyperlink")
    if url:
        h.set(qn("r:id"), paragraph.part.relate_to(url, HYPERLINK_REL, is_external=True))
    else:
        h.set(qn("w:anchor"), anchor)
    r = OxmlElement("w:r"); r.append(run_props("0C2D5A"))
    t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t)
    h.append(r); paragraph._p.append(h)


def inline(paragraph, text):
    pos = 0
    for m in INLINE_RE.finditer(text):
        if m.start() > pos:
            paragraph.add_run(text[pos:m.start()])
        tok = m.group(0)
        lm = LINK_RE.match(tok)
        if lm:
            add_link(paragraph, lm.group(1), url=lm.group(2))
        elif tok.startswith("***"):
            r = paragraph.add_run(tok[3:-3]); r.bold = True; r.italic = True
        elif tok.startswith("**"):
            paragraph.add_run(tok[2:-2]).bold = True
        else:
            paragraph.add_run(tok[1:-1]).italic = True
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])
    # bare URLs become links
    return paragraph


BOOKMARK_ID = [1]


def bookmark(paragraph, name):
    s = OxmlElement("w:bookmarkStart"); s.set(qn("w:id"), str(BOOKMARK_ID[0])); s.set(qn("w:name"), name)
    e = OxmlElement("w:bookmarkEnd"); e.set(qn("w:id"), str(BOOKMARK_ID[0]))
    BOOKMARK_ID[0] += 1
    paragraph._p.insert(0, s); paragraph._p.append(e)


def table(doc, rows):
    t = doc.add_table(rows=0, cols=len(rows[0])); t.style = "Table Grid"
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for ci, txt in enumerate(row[:len(cells)]):
            p = inline(cells[ci].paragraphs[0], txt)
            if ri == 0:
                for r in p.runs:
                    r.bold = True
    doc.add_paragraph()


def main():
    lines = []
    for f in CHAPTERS:
        lines += f.read_text(encoding="utf-8").split("\n") + [""]
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(6), Inches(9)
    for edge in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
        setattr(sec, edge, Inches(0.75))
    st = doc.styles
    for name in ("Normal", "Title", "Subtitle", "Heading 1", "Heading 2", "Heading 3", "Heading 4", "Heading 5"):
        st[name].font.name = "Georgia"
        st[name].font.color.rgb = RGBColor(0, 0, 0)
    st["Normal"].font.size = Pt(11)
    st["Normal"].paragraph_format.space_after = Pt(6)
    st["Normal"].paragraph_format.line_spacing = 1.15
    st["Heading 1"].font.size = Pt(20)
    st["Heading 1"].paragraph_format.page_break_before = True
    st["Heading 2"].font.size = Pt(16)
    st["Heading 3"].font.size = Pt(13)
    st["Heading 4"].font.size = Pt(12)
    st["Heading 5"].font.size = Pt(11)

    # Title page from the first four lines of 00_front_matter.md
    doc.add_paragraph(TITLE, "Title").alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph(SUBTITLE, "Subtitle").alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(AUTHOR); r.bold = True; r.font.size = Pt(16)
    p = doc.add_paragraph("Updated 1 October 2026"); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_break(WD_BREAK.PAGE)
    # skip title block lines in the md (up to the copyright line)
    i = next(k for k, l in enumerate(lines) if l.startswith("Copyright"))

    # collect contents entries (H1 + chapter H2) for a linked table of contents
    toc = []
    for l in lines[i:]:
        m = HEADING_RE.match(l.strip())
        if m and (len(m.group(1)) == 1 or m.group(2).startswith("Chapter ")):
            toc.append((len(m.group(1)), m.group(2)))

    toc_done = False
    n = len(lines)
    while i < n:
        s = lines[i].strip()
        if not s:
            i += 1; continue
        hm = HEADING_RE.match(s)
        if hm:
            level, text = len(hm.group(1)), hm.group(2)
            if level == 1 and not toc_done:
                toc_done = True
                h = doc.add_heading("Contents", level=1)
                for lv, t in toc:
                    cp = doc.add_paragraph()
                    cp.paragraph_format.space_after = Pt(2)
                    if lv == 2:
                        cp.paragraph_format.left_indent = Inches(0.3)
                    add_link(cp, t, anchor=slug(t))
            h = doc.add_heading(level=min(level, 5))
            inline(h, text)
            if level == 1 or text.startswith("Chapter "):
                bookmark(h, slug(text))
            i += 1; continue
        if s.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            if rows:
                table(doc, rows)
            continue
        if RULE_RE.fullmatch(s):
            i += 1; continue
        im = IMAGE_RE.match(s)
        if im:
            path = FIGURES / Path(im.group(2)).name
            doc.add_picture(str(path), width=Inches(4.4))
            pic = doc.paragraphs[-1]
            pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
            alt = im.group(1) if im.group(1) and im.group(1) != "figure" else path.stem.replace("_", " ")
            for dp in pic._p.xpath(".//wp:docPr"):
                dp.set("descr", alt)
            i += 1; continue
        cm = CHECK_RE.match(s)
        if cm:
            p = doc.add_paragraph(); p.add_run("☐ "); inline(p, cm.group(1)); i += 1; continue
        bm = BULLET_RE.match(s)
        if bm:
            inline(doc.add_paragraph(style="List Bullet"), bm.group(1)); i += 1; continue
        nm = NUM_RE.match(s)
        if nm:
            p = doc.add_paragraph(); p.paragraph_format.left_indent = Inches(0.3)
            p.add_run(nm.group(1) + ". "); inline(p, nm.group(2)); i += 1; continue
        if s.startswith(">"):
            p = doc.add_paragraph(); p.paragraph_format.left_indent = Inches(0.35)
            p.paragraph_format.right_indent = Inches(0.2)
            inline(p, s.lstrip(">").strip()); i += 1; continue
        if re.match(r"^https?://\S+$", s):
            p = doc.add_paragraph(); add_link(p, s, url=s); i += 1; continue
        inline(doc.add_paragraph(), s)
        i += 1

    cp = doc.core_properties
    cp.title, cp.subject, cp.author, cp.last_modified_by = TITLE, SUBTITLE, AUTHOR, AUTHOR
    doc.save(str(OUTPUT))
    words = sum(len(p.text.split()) for p in doc.paragraphs)
    print(f"Wrote {OUTPUT.name}: {OUTPUT.stat().st_size:,} bytes, about {words:,} words")


if __name__ == "__main__":
    main()
