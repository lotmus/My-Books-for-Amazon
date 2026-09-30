"""Build Your First YouTube Channel That Sells.docx in the same shape as the Kindle book."""
import re
from pathlib import Path

from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor, Twips
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).parent
FIG = ROOT / "figures"
ORDER = [
    (1, ROOT / "manuscript" / "The Click Is the Whole Business.md"),
    (2, ROOT / "manuscript" / "Nobody Can Tell What It Cost.md"),
    (3, ROOT / "manuscript" / "Where the Money Actually Comes From.md"),
]
SERIES = "A working guide for creators who want a channel, not a hobby."
TOKEN = re.compile(r"(\*\*[^*]+?\*\*|\*[^*]+?\*|`[^`]+`|\[[^\]]+?\]\([^)]+?\))")


def shade(cell, fill):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def set_cell_width(cell, inches):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcW = OxmlElement("w:tcW")
    dxa = str(int(inches * 1440))
    tcW.set(qn("w:w"), dxa)
    tcW.set(qn("w:type"), "dxa")
    tcPr.append(tcW)


def add_hyperlink(paragraph, text, url):
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rStyle = OxmlElement("w:rStyle")
    rStyle.set(qn("w:val"), "Hyperlink")
    rPr.append(rStyle)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "22")
    rPr.append(sz)
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Calibri")
    rFonts.set(qn("w:hAnsi"), "Calibri")
    rPr.append(rFonts)
    run.append(rPr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    run.append(t)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def add_inlines(paragraph, text):
    for part in TOKEN.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
            run.font.name = "Calibri"
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            run.font.name = "Calibri"
        elif part.startswith("*") and part.endswith("*"):
            run = paragraph.add_run(part[1:-1])
            run.italic = True
            run.font.name = "Calibri"
        elif part.startswith("["):
            match = re.match(r"\[([^\]]+)\]\(([^)]+)\)", part)
            if match:
                add_hyperlink(paragraph, match.group(1), match.group(2))
            else:
                run = paragraph.add_run(part)
                run.font.name = "Calibri"
        else:
            run = paragraph.add_run(part)
            run.font.name = "Calibri"


def is_italic_block(text):
    return text.startswith("*") and text.endswith("*") and not text.startswith("**")


def add_picture(doc, rel, alt, base):
    src = (base / rel).resolve()
    png = src.with_suffix(".png")
    path = png if png.exists() else src
    if path.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        paragraph = doc.add_paragraph()
        run = paragraph.add_run(alt)
        run.italic = True
        return
    paragraph = doc.add_paragraph()
    paragraph.alignment = 1
    run = paragraph.add_run()
    run.add_picture(str(path), width=Inches(5.6))
    doc_pr = run._r.xpath(".//wp:docPr")
    if doc_pr:
        doc_pr[0].set("descr", alt)


def add_table(doc, rows):
    cols = max(len(row) for row in rows)
    widths = column_widths(cols)
    table = doc.add_table(rows=len(rows), cols=cols)
    table.autofit = False
    table.allow_autofit = False
    table.style = "Table Grid"
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement("w:tblPr")
    tblW = OxmlElement("w:tblW")
    total = int(sum(widths) * 1440)
    tblW.set(qn("w:w"), str(total))
    tblW.set(qn("w:type"), "dxa")
    tblPr.append(tblW)
    for i, row in enumerate(rows):
        for j in range(cols):
            cell = table.rows[i].cells[j]
            set_cell_width(cell, widths[j])
            cell.text = ""
            paragraph = cell.paragraphs[0]
            paragraph.paragraph_format.space_after = Pt(2)
            paragraph.paragraph_format.space_before = Pt(2)
            text = row[j] if j < len(row) else ""
            add_inlines(paragraph, text)
            for run in paragraph.runs:
                run.font.size = Pt(10)
                run.font.name = "Calibri"
                if i == 0:
                    run.bold = True
            if i == 0:
                shade(cell, "F3F1EA")
    doc.add_paragraph()


def column_widths(cols):
    if cols == 4:
        return [1.15, 1.35, 1.9, 1.2]
    if cols == 3:
        return [1.5, 1.5, 2.6]
    share = 5.6 / cols
    return [share] * cols


def parse_blocks(text):
    lines = text.replace("\r\n", "\n").split("\n")
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.strip() == "---":
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                raw = lines[i].strip().strip("|")
                cells = [cell.strip() for cell in raw.split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                    rows.append(cells)
                i += 1
            blocks.append(("table", rows))
            continue
        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:].strip())
                i += 1
            blocks.append(("bullets", items))
            continue
        if re.match(r"\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"\d+\. ", lines[i]):
                items.append(re.sub(r"^\d+\. ", "", lines[i]).strip())
                i += 1
            blocks.append(("numbers", items))
            continue
        if line.startswith("!["):
            match = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", line.strip())
            if match:
                blocks.append(("image", match.group(2), match.group(1)))
                i += 1
                continue
        paragraph = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "|", "- ", "!")) and not re.match(r"\d+\. ", lines[i]) and lines[i].strip() != "---":
            paragraph.append(lines[i].rstrip())
            i += 1
        blocks.append(("p", " ".join(paragraph).strip()))
    return blocks


def add_body(doc, blocks, number, base):
    skipped_series = False
    for block in blocks:
        kind = block[0]
        if kind == "p":
            text = block[1]
            if text.startswith("# "):
                title = text[2:].strip()
                doc.add_paragraph(f"{number} {title}", "Heading 1")
                continue
            if text.startswith("## "):
                doc.add_paragraph(text[3:].strip(), "Heading 2")
                continue
            if not skipped_series and text.strip("*") == SERIES.strip("."):
                skipped_series = True
                continue
            if not skipped_series and "working guide for creators" in text:
                skipped_series = True
                continue
            paragraph = doc.add_paragraph()
            if is_italic_block(text):
                run = paragraph.add_run(text[1:-1])
                run.italic = True
                run.font.name = "Calibri"
            else:
                add_inlines(paragraph, text)
        elif kind == "bullets":
            for item in block[1]:
                paragraph = doc.add_paragraph(style="List Bullet")
                add_inlines(paragraph, item)
        elif kind == "numbers":
            for item in block[1]:
                paragraph = doc.add_paragraph(style="List Number")
                add_inlines(paragraph, item)
        elif kind == "table":
            add_table(doc, block[1])
        elif kind == "image":
            add_picture(doc, block[1], block[2], base)


def insert_contents(doc):
    headings = [p for p in doc.paragraphs if p.style.name == "Heading 1"]
    first = headings[0]
    contents_el = OxmlElement("w:p")
    first._p.addprevious(contents_el)
    contents = Paragraph(contents_el, first._parent)
    contents.style = doc.styles["Heading 1"]
    contents.add_run("Contents")
    last = contents
    for i, heading in enumerate(headings):
        start = OxmlElement("w:bookmarkStart")
        start.set(qn("w:id"), str(i + 1))
        start.set(qn("w:name"), f"ch{i}")
        heading._p.insert(0, start)
        end = OxmlElement("w:bookmarkEnd")
        end.set(qn("w:id"), str(i + 1))
        heading._p.append(end)
        p_el = OxmlElement("w:p")
        last._p.addnext(p_el)
        last = Paragraph(p_el, first._parent)
        last.style = doc.styles["Normal"]
        link = OxmlElement("w:hyperlink")
        link.set(qn("w:anchor"), f"ch{i}")
        run = OxmlElement("w:r")
        rPr = OxmlElement("w:rPr")
        rFonts = OxmlElement("w:rFonts")
        rFonts.set(qn("w:ascii"), "Calibri")
        rFonts.set(qn("w:hAnsi"), "Calibri")
        rPr.append(rFonts)
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), "22")
        rPr.append(sz)
        color = OxmlElement("w:color")
        color.set(qn("w:val"), "1F4E79")
        rPr.append(color)
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "single")
        rPr.append(u)
        run.append(rPr)
        t = OxmlElement("w:t")
        t.text = heading.text
        run.append(t)
        link.append(run)
        p_el.append(link)


def main():
    doc = Document()
    section = doc.sections[0]
    section.page_width = Inches(7)
    section.page_height = Inches(10)
    section.top_margin = section.bottom_margin = Inches(0.7)
    section.left_margin = section.right_margin = Inches(0.7)
    for name in ["Normal", "Title", "Subtitle", "Heading 1", "Heading 2"]:
        doc.styles[name].font.name = "Calibri"
        doc.styles[name].font.color.rgb = RGBColor(0, 0, 0)
    doc.styles["Normal"].font.size = Pt(11)
    doc.styles["Normal"].paragraph_format.space_after = Pt(7)
    doc.styles["Normal"].paragraph_format.line_spacing = 1.08
    doc.styles["Title"].font.size = Pt(32)
    doc.styles["Heading 1"].font.size = Pt(21)
    doc.styles["Heading 1"].paragraph_format.page_break_before = True
    doc.styles["Heading 2"].font.size = Pt(14)

    doc.add_paragraph("Your First YouTube\nChannel That Sells", "Title")
    doc.add_paragraph(
        "How to Make Videos Cheaply, Win the Click, and Build a Channel That Can Pay",
        "Subtitle",
    )
    doc.add_paragraph(SERIES)
    doc.add_paragraph("Updated September 2026")

    doc.add_paragraph("Start here", "Heading 1")
    for text in START:
        paragraph = doc.add_paragraph()
        add_inlines(paragraph, text)

    for number, path in ORDER:
        add_body(doc, parse_blocks(path.read_text(encoding="utf-8")), number, path.parent)

    doc.add_paragraph("Official sources and updates", "Heading 1")
    for text in SOURCES:
        paragraph = doc.add_paragraph()
        if text.startswith("*") and text.endswith("*"):
            run = paragraph.add_run(text[1:-1])
            run.italic = True
            run.font.name = "Calibri"
        else:
            add_inlines(paragraph, text)

    insert_contents(doc)
    doc.core_properties.title = "Your First YouTube Channel That Sells"
    doc.core_properties.author = "Kevin Drew Peters"
    doc.core_properties.subject = "A working guide for creators who want a channel, not a hobby"
    out = ROOT / "Your First YouTube Channel That Sells.docx"
    doc.save(out)
    words = sum(len(p.text.split()) for p in doc.paragraphs)
    print(out)
    print("Words", words)


START = [
    "A channel starts when a stranger can find a video, tell what it offers, and decide it is worth their time. This guide is the process for doing that on a small budget: make the video cheaply, win the click honestly, and know which numbers a platform requires before it pays you.",
    "Read the chapters in order if you are starting. If you already post, open the chapter that matches the problem you can see.",
    "Chapter 1 is the click. A thumbnail and a title win or lose the viewer before a second of the video plays. The chapter covers the title, description, and tag limits you can count in the upload form, the words that can suppress reach, captions, retention as creator consensus rather than a published formula, and a short-form to long-form posting rhythm.",
    "Chapter 2 is production. Footage, music, a voice, and an export each have a free or near-free tool. None of those tools tell you what you are allowed to publish. The license check is yours.",
    "Chapter 3 is the money. A subscriber count is not a monetized channel. YouTube’s Partner Program has two gates, a second channel starts back at zero, other platforms pay on different terms that change quickly, and an affiliate link does not depend on any one of those programs surviving.",
    "Character limits, export settings, and eligibility rules are stated as facts because they are checkable in the product. Ranking behavior and retention percentages are labeled as inference or creator consensus. Tool prices and platform thresholds move. Recheck the upload form and the linked help pages before you build a plan on a specific number.",
    "This is a companion to a Kindle publishing guide, not a chapter of it. It does not tell you what your videos should be about, and it is not legal, tax, or official platform advice.",
]

SOURCES = [
    "These notes support the claims in the chapters. Planning methods and creator-consensus tactics are editorial guidance, not platform requirements. Accessed September 2026.",
    "*Chapter 1. YouTube Studio’s own upload interface (title, description, and tag character limits, and the captions workflow). YouTube’s advertiser-friendly content guidelines, for the existence of a sensitive-content category. Retention benchmarks and posting-cadence figures are creator consensus, not published platform figures.*",
    "*Chapter 2. Tool names and URLs come from working bookmark lists of video, footage, music, and voice tools. A few transferable techniques — reference-image consistency, mixing ratios, export settings, and the fully original workflow — were taken from saved research and rewritten. Specific personal projects were not used. Pricing, licenses, and features change.*",
    "*Chapter 3. YouTube Partner Program requirements were checked against YouTube’s own monetization guidance. Other platforms were checked against their own creator or help pages. Dailymotion’s requirements could not be confirmed to the same standard and are flagged in the chapter. Subscriber-conversion tactics and affiliate-link placement are creator consensus, not published policy.*",
    "Independent guide. Not affiliated with or endorsed by YouTube or any other platform named here. Not legal or tax advice. Check current official terms before acting.",
]


if __name__ == "__main__":
    main()
