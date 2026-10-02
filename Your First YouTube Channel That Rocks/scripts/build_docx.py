"""Build Your First YouTube Channel That Rocks.docx in the same shape as the Kindle book."""
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor, Twips
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parent.parent  # scripts\ -> book root
FIG = ROOT / "figures"
ORDER = [
    (1, ROOT / "chapters" / "Name the Viewer.md"),
    (2, ROOT / "chapters" / "The Click Is the Whole Business.md"),
    (3, ROOT / "chapters" / "Nobody Can Tell What It Cost.md"),
    (4, ROOT / "chapters" / "Record It So They Stay.md"),
    (5, ROOT / "chapters" / "Eight Videos, Each With One Job.md"),
    (6, ROOT / "chapters" / "Six Weeks to a Working Channel.md"),
    (7, ROOT / "chapters" / "Read the Count.md"),
    (8, ROOT / "chapters" / "Grow Toward the Gate.md"),
    (9, ROOT / "chapters" / "The Gates and the Review.md"),
    (10, ROOT / "chapters" / "The Rules That Can Switch Off the Money.md"),
    (11, ROOT / "chapters" / "Ads, RPM, and the Shorts Pool.md"),
    (12, ROOT / "chapters" / "Money From the People Who Watch.md"),
    (13, ROOT / "chapters" / "Sponsors and Affiliate Links.md"),
    (14, ROOT / "chapters" / "Keep It Paying.md"),
    (15, ROOT / "chapters" / "The Channel Workbook.md"),
]
TITLE = "Your First YouTube Channel That Rocks"
SUBTITLE = "Grow Watch Time and Subscribers, Reach the Partner Program, and Earn From Ads, Fans, and Sponsors"
SERIES = "A working guide for creators who want a channel, not a hobby."
# Back matter: the canonical "Also by Lothar J. Musiol" list (same in every book; see
# notes/ALSO_BY - canonical list.md at the repo root). Titles as on each master's title page.
ALSO_BY_HEADING = "Also by Lothar J. Musiol"
ALSO_BY = [
    ('Physics, Actually', [
        'Physics, Actually, Volume 1: Motion, Forces, Time, and Relativity',
        'Physics, Actually, Volume 2: Gravity, Cosmology, and the Limits of Spacetime',
        'Physics, Actually, Volume 3: The Standard Model, Chaos, and the Edge of Knowledge',
        'Life, Actually: From the First Cell to the Edited Genome and the Search for Life Elsewhere',
    ]),
    ('Math, Actually', [
        'Math, Actually, Volume 1: From Arithmetic to Calculus',
        'Math, Actually, Volume 2: From Multivariable Calculus to Set Theory & Logic',
        'Math, Actually, Volume 3: From Differential Equations to Abstract Algebra',
        'Math, Actually, Volume 4: From Category Theory to the Frontier',
    ]),
    ('Quanta, Actually', [
        'Quanta, Actually, Volume 1: The Quantum World',
        'Quanta, Actually, Volume 2: The Quantum Conversation',
        'Quanta, Actually, Volume 3: Complete Quantum Electrodynamics Course',
    ]),
    ('Science Sparks', [
        'Science Sparks: Physics, Life, and Mathematics — The Same Few Rules, Told in Highlights',
    ]),
    ('Look First', [
        'Look First, Volume 1: The Universe Has No Now',
        'Look First, Volume 2: A Trip Is Not a New Life',
    ]),
    ('Electrical Engineering Series', [
        'Foundations of Electronics (Book 1)',
        'Circuits, Components, and Control (Book 2)',
        'Semiconductor Physics and Devices (Book 3)',
        'RF, Microwave, and Transceivers (Book 4)',
        'Communications, Wireless, and SDR (Book 5)',
        'Power and Energy (Book 6)',
        'Packaging, Layout, EMC, and Test (Book 7)',
    ]),
    ('History', [
        "The Dolphins' View of History",
    ]),
    ('Fiction', [
        "The Murder That Hadn't Happened Yet (The Relativistic Investigation Bureau, Book 1)",
        'The Warning That Was Sent Too Late (The Relativistic Investigation Bureau, Book 2)',
        'Schrödinger’s Paperwork (Lolly Wren’s Curious Science Adventures, Book 1)',
        'The Permitted Options (Lolly Wren’s Curious Science Adventures, Book 2)',
        'Protocol Flamingo (The Invasion Storybooks, Book 1), as George Herbert Fontaine',
    ]),
    ('How-To', [
        'Your First Book That Sells',
        'Your First YouTube Channel That Rocks',
    ]),
]
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
            inner = part[2:-2]
            if "](" in inner:
                before = len(paragraph.runs)
                add_inlines(paragraph, inner)
                for run in paragraph.runs[before:]:
                    run.bold = True
                continue
            run = paragraph.add_run(inner)
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
                run.font.size = Pt(10.5)
                run.font.name = "Calibri"
                if i == 0:
                    run.bold = True
            if i == 0:
                shade(cell, "F3F1EA")
    doc.add_paragraph()


def column_widths(cols):
    if cols == 4:
        return [1.05, 1.2, 2.2, 1.15]
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
        if line.startswith(">"):
            blocks.append(("callout", line.lstrip(">").strip()))
            i += 1
            continue
        paragraph = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "|", "- ", "!", ">")) and not re.match(r"\d+\. ", lines[i]) and lines[i].strip() != "---":
            paragraph.append(lines[i].rstrip())
            i += 1
        blocks.append(("p", " ".join(paragraph).strip()))
    return blocks


def apply_page(section):
    section.page_width = Inches(7)
    section.page_height = Inches(10)
    section.top_margin = section.bottom_margin = Inches(0.7)
    section.left_margin = section.right_margin = Inches(0.7)
    section.header_distance = Inches(0.35)
    section.footer_distance = Inches(0.35)


def set_running_head(section, text):
    apply_page(section)
    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False
    header = section.header.paragraphs[0]
    header.clear()
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = header.add_run(text)
    run.italic = True
    run.font.name = "Calibri"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    footer = section.footer.paragraphs[0]
    footer.clear()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    footer.add_run()._r.append(begin)
    footer.add_run()._r.append(instr)
    footer.add_run()._r.append(end)
    for item in footer.runs:
        item.font.name = "Calibri"
        item.font.size = Pt(9)


def add_body(doc, blocks, number, base):
    skipped_series = False
    for block in blocks:
        kind = block[0]
        if kind == "p":
            text = block[1]
            if text.startswith("# "):
                title = text[2:].strip()
                section = doc.add_section(WD_SECTION.NEW_PAGE)
                set_running_head(section, f"{number}  {title}")
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
                add_inlines(paragraph, text[1:-1])
                for run in paragraph.runs:
                    run.italic = True
            else:
                add_inlines(paragraph, text)
        elif kind == "bullets":
            for item in block[1]:
                paragraph = doc.add_paragraph(style="List Bullet")
                add_inlines(paragraph, item)
        elif kind == "numbers":
            num_id = new_restarted_num(doc)
            for item in block[1]:
                paragraph = doc.add_paragraph(style="List Number")
                if num_id:
                    force_num(paragraph, num_id)
                add_inlines(paragraph, item)
        elif kind == "callout":
            add_callout(doc, block[1])
        elif kind == "table":
            add_table(doc, block[1])
        elif kind == "image":
            add_picture(doc, block[1], block[2], base)


def add_callout(doc, text):
    table = doc.add_table(rows=1, cols=1)
    table.autofit = False
    table.allow_autofit = False
    cell = table.cell(0, 0)
    set_cell_width(cell, 5.6)
    shade(cell, "F3F1EA")
    cell.text = ""
    paragraph = cell.paragraphs[0]
    paragraph.paragraph_format.space_after = Pt(2)
    paragraph.paragraph_format.space_before = Pt(2)
    add_inlines(paragraph, text)
    for run in paragraph.runs:
        run.font.size = Pt(11)
        run.font.name = "Calibri"
    doc.add_paragraph()


def new_restarted_num(doc):
    numbering = doc.part.numbering_part._element
    nums = numbering.findall(qn("w:num"))
    if not nums:
        return None
    source = next((n for n in nums if n.get(qn("w:numId")) == "5"), nums[-1])
    abstract = source.find(qn("w:abstractNumId"))
    if abstract is None:
        return None
    new_id = max(int(n.get(qn("w:numId"))) for n in nums) + 1
    num = OxmlElement("w:num")
    num.set(qn("w:numId"), str(new_id))
    abs_el = OxmlElement("w:abstractNumId")
    abs_el.set(qn("w:val"), abstract.get(qn("w:val")))
    num.append(abs_el)
    override = OxmlElement("w:lvlOverride")
    override.set(qn("w:ilvl"), "0")
    start = OxmlElement("w:startOverride")
    start.set(qn("w:val"), "1")
    override.append(start)
    num.append(override)
    numbering.append(num)
    return str(new_id)


def force_num(paragraph, num_id):
    pPr = paragraph._p.get_or_add_pPr()
    existing = pPr.find(qn("w:numPr"))
    if existing is not None:
        pPr.remove(existing)
    numPr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), "0")
    nid = OxmlElement("w:numId")
    nid.set(qn("w:val"), num_id)
    numPr.append(ilvl)
    numPr.append(nid)
    pPr.append(numPr)


def insert_contents(doc):
    headings = [p for p in doc.paragraphs if p.style.name in ("Heading 1", "Heading 2")]
    first = next(p for p in headings if p.style.name == "Heading 1")
    contents_el = OxmlElement("w:p")
    first._p.addprevious(contents_el)
    contents = Paragraph(contents_el, first._parent)
    contents.style = doc.styles["Heading 1"]
    contents.add_run("Contents")
    last = contents
    for i, heading in enumerate(headings):
        start = OxmlElement("w:bookmarkStart")
        start.set(qn("w:id"), str(i + 1))
        start.set(qn("w:name"), f"toc{i}")
        heading._p.insert(0, start)
        end = OxmlElement("w:bookmarkEnd")
        end.set(qn("w:id"), str(i + 1))
        heading._p.append(end)
        p_el = OxmlElement("w:p")
        last._p.addnext(p_el)
        last = Paragraph(p_el, first._parent)
        last.style = doc.styles["Normal"]
        if heading.style.name == "Heading 2":
            last.paragraph_format.left_indent = Inches(0.3)
        link = OxmlElement("w:hyperlink")
        link.set(qn("w:anchor"), f"toc{i}")
        run = OxmlElement("w:r")
        rPr = OxmlElement("w:rPr")
        rFonts = OxmlElement("w:rFonts")
        rFonts.set(qn("w:ascii"), "Calibri")
        rFonts.set(qn("w:hAnsi"), "Calibri")
        rPr.append(rFonts)
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), "20" if heading.style.name == "Heading 2" else "22")
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
    doc.styles["Normal"].paragraph_format.space_after = Pt(8)
    doc.styles["Normal"].paragraph_format.line_spacing = 1.15
    doc.styles["Title"].font.size = Pt(32)
    doc.styles["Heading 1"].font.size = Pt(21)
    doc.styles["Heading 1"].paragraph_format.page_break_before = False
    doc.styles["Heading 2"].font.size = Pt(16)
    doc.styles["Heading 2"].paragraph_format.space_before = Pt(16)
    doc.styles["Heading 2"].paragraph_format.space_after = Pt(8)
    section.different_first_page_header_footer = True
    set_running_head(section, "Start here")

    doc.add_paragraph("Your First YouTube\nChannel That Rocks", "Title")
    doc.add_paragraph(
        SUBTITLE,
        "Subtitle",
    )
    doc.add_paragraph(SERIES)
    author_line = doc.add_paragraph()
    author_line.add_run("Lothar J. Musiol").bold = True
    doc.add_paragraph("Updated October 2026")
    doc.add_paragraph("Copyright \u00a9 2026 Lothar J. Musiol. All rights reserved.")

    doc.add_paragraph("Start here", "Heading 1")
    for text in START:
        paragraph = doc.add_paragraph()
        add_inlines(paragraph, text)

    for number, path in ORDER:
        add_body(doc, parse_blocks(path.read_text(encoding="utf-8")), number, path.parent)

    last = doc.add_section(WD_SECTION.NEW_PAGE)
    set_running_head(last, "The last word")
    doc.add_paragraph("The last word", "Heading 1")
    for text in CLOSE:
        paragraph = doc.add_paragraph()
        add_inlines(paragraph, text)

    gloss = doc.add_section(WD_SECTION.NEW_PAGE)
    set_running_head(gloss, "Glossary")
    doc.add_paragraph("Glossary", "Heading 1")
    glossary_intro = doc.add_paragraph()
    add_inlines(
        glossary_intro,
        "Short definitions for terms this book uses. A definition here is not a substitute for the platform page cited in the chapter.",
    )
    for term, definition in GLOSSARY:
        paragraph = doc.add_paragraph()
        run = paragraph.add_run(term + ". ")
        run.bold = True
        run.font.name = "Calibri"
        add_inlines(paragraph, definition)

    sources = doc.add_section(WD_SECTION.NEW_PAGE)
    set_running_head(sources, "Sources")
    doc.add_paragraph("Official sources and updates", "Heading 1")
    for text in SOURCES:
        paragraph = doc.add_paragraph()
        if text.startswith("*") and text.endswith("*"):
            run = paragraph.add_run(text[1:-1])
            run.italic = True
            run.font.name = "Calibri"
        else:
            add_inlines(paragraph, text)

    also = doc.add_section(WD_SECTION.NEW_PAGE)
    set_running_head(also, "Also by")
    doc.add_paragraph(ALSO_BY_HEADING, "Heading 1")
    for group, titles in ALSO_BY:
        paragraph = doc.add_paragraph()
        paragraph.paragraph_format.space_before = Pt(8)
        paragraph.paragraph_format.space_after = Pt(2)
        paragraph.paragraph_format.keep_with_next = True
        run = paragraph.add_run(group)
        run.bold = True
        run.font.name = "Calibri"
        for title in titles:
            paragraph = doc.add_paragraph()
            paragraph.paragraph_format.left_indent = Inches(0.25)
            paragraph.paragraph_format.space_after = Pt(1)
            paragraph.add_run(title).font.name = "Calibri"

    insert_contents(doc)
    doc.core_properties.title = TITLE
    doc.core_properties.author = "Lothar J. Musiol"
    doc.core_properties.subject = SUBTITLE
    doc.core_properties.keywords = "YouTube Partner Program; monetization; RPM; channel memberships; Super Thanks; sponsorships"
    out = ROOT / f"{TITLE}.docx"
    doc.save(out)
    words = sum(len(p.text.split()) for p in doc.paragraphs)
    print(out)
    print("Words", words)


START = [
    "A channel that rocks is one a stranger chooses, finishes, and comes back to. YouTube pays for exactly that behavior, through programs with published gates: subscribers, public watch hours, and qualified Shorts views, counted in rolling windows. This book is the path from an empty channel to a channel that clears those gates and then earns from every stream YouTube and its partners offer.",
    "It runs in five stages. Chapters 1 to 4 set up the channel and the quality of each video: naming the viewer, winning the click, making videos cheaply, and recording them so people stay. Chapters 5 to 8 grow the audience: eight videos with one job each, a six-week calendar, reading Studio’s counts, and the arithmetic of the gate. Chapters 9 and 10 are eligibility: the Partner Program’s thresholds for 2026 and 2027, the review, and the rules that can switch the money off. Chapters 11 to 13 are the monetization streams: ads, RPM, and the Shorts pool; memberships, Super Chat, Super Stickers, and Super Thanks; sponsorships and affiliate links. Chapters 14 and 15 are scaling and sustainability: what to fix when the counts stall, how to spread the income, and the workbook that keeps the record.",
    "Read it in order if you are starting. If you already post, use chapter 14 to find the earliest break, then go to the chapter that fixes it.",
    "One fact shapes the whole plan. On 10 August 2026 YouTube announced that channels applying to the Partner Program on or after 1 February 2027 need 8,000 qualified watch hours in a year, or 20 million qualified Shorts views in 90 days, alongside 1,000 subscribers. Chapter 9 has the details. A new channel should plan for the new numbers.",
    "Character limits, export settings, eligibility rules, and revenue shares are facts you can check in the product, and every one is tied to YouTube’s own help pages or blog. They move. Anything about the algorithm is labeled as creator consensus. The planning numbers in this book are arithmetic, not promises of income. This is not legal, tax, or official platform advice.",
]

CLOSE = [
    "The channel in this book does not start with money. It starts with one viewer and a question they would type, and it earns the right to be paid one finished minute at a time: a title that names the problem, an opening that keeps the promise, a method given away, a next video named inside the last one.",
    "The gates are arithmetic. Subscribers, plus hours or Shorts views, inside a window that rolls. Once you can work out how many views a day your channel needs at its own view duration, the gate stops being a mystery and becomes a distance, and chapter 4’s work on the opening becomes the cheapest way to shorten it.",
    "Past the gate, the money comes in five kinds, and each one pays for something different. Ads pay for reach. Memberships pay for loyalty. Supers pay for presence. Sponsors pay for a precise viewer. Affiliate commissions pay for recommendations people act on. A channel that keeps all five small and honest survives the next rule change. A channel that bets on one does not.",
    "The numbers will move again before the next edition of this book. Check the Earn tab, read the help page, write the date in the decision log. Then make the next video for the same person you named on the first page.",
]

SOURCES = [
    "These notes support the claims in the chapters. Planning methods, worksheets, and creator-consensus tactics are editorial guidance, not platform requirements. All dollar figures in worked examples are invented arithmetic. Pages accessed September and October 2026. YouTube’s monetization, fan-funding, Shorts, and AI-disclosure pages were rechecked in October 2026.",
    "*Chapter 1. The money map, the rule that a channel outside the Partner Program does not share in ad revenue, the inactivity rule, clickable links, and posts are cited to YouTube’s own help pages in the chapter.*",
    "*Chapter 2. Title, description, and tag limits, captions, thumbnails, the title-and-thumbnail test, audience retention, recommendation signals, the recommendation system, Shorts discovery, Shorts analytics, and series playlists are cited to YouTube’s own help pages in the chapter. The eight jobs are the only production load in this book. YouTube does not publish that set as a quota. Advertiser-friendly guidelines are cited for the existence of a sensitive-content category. The exact words that trigger it are not published.*",
    "*Chapter 3. Tool names and URLs come from working bookmark lists. Export bitrates, codec, and sample rate are YouTube’s recommended upload encoding settings. The Audio Library location is YouTube’s own help page. The rights statement made when ads are turned on is from YouTube’s monetization page. A higher-resolution upload getting a better playback encode is creator talk, and the chapter says so. Pricing, licenses, and features change. Specific personal projects were not used.*",
    "*Chapter 4. Video chapter rules, end screen timing, and the eight-minute mid-roll rule are cited to YouTube’s own help pages in the chapter. The speaking-rate range is a planning guess to replace with your own timed reading. That viewers forgive picture before sound is creator consensus, and the chapter says so.*",
    "*Chapters 5 and 6 are a growth path: eight videos with one job each and a six-week calendar. They state no ranking formula. The creator interviews in chapter 5 are not evidence for the eight-video set.*",
    "*Chapter 7. Qualified counts, impression counting, the 2%–10% click-through band, traffic source definitions, and the August 24, 2026 change to when a view is counted are cited to YouTube’s help pages. The worked example is invented arithmetic.*",
    "*Chapter 8. Thresholds, the live-stream rule, and the rule that paid campaign views do not count are cited to YouTube’s help pages and the August 2026 announcement. Subscribe wording, the subscribe link, sub-for-sub effects, and collaborations are creator consensus, labeled as tests.*",
    "*Chapter 9. YouTube Partner Program requirements, including the changes that take effect on 1 February 2027, were checked against YouTube’s eligibility page, its monetization overview, and its 10 August 2026 announcement in October 2026. The 2027 activity definition is from trade reporting and is labeled as such.*",
    "*Chapter 10. Warnings, strikes, copyright removal, Content ID claims, limited ads and self-certification, paid promotion, AI use disclosure, made-for-kids features, the spam, fake engagement, and external links policies, and the reused, inauthentic-content, and AI-persona monetization rules are cited to YouTube’s own help pages and blog in the chapter. Not legal advice.*",
    "*Chapter 11. Ad formats, mid-rolls, CPM, playback-based CPM, RPM, the 55% and 45% shares, the Premium and Premium Lite pools, the Shorts Creator Pool, and the February 2027 Shorts floor are cited to YouTube’s help pages and blog. The worked example is invented arithmetic.*",
    "*Chapter 12. Fan-funding minimums, the 70% shares, membership levels, US price points, banned perks, paused mode, and where Super Chat, Super Stickers, and Super Thanks are unavailable are cited to YouTube’s help pages. Live-stream engagement advice is creator consensus.*",
    "*Chapter 13. Creator Partnerships eligibility, the paid promotion box, clickable links, and the YouTube Shopping affiliate program’s 500-subscriber threshold are cited to YouTube’s help pages and blog. The FTC pages are US guidance. The media kit, pricing method, and contract terms are editorial practice.*",
    "*Chapter 14. Other platforms were checked against the linked help page in September 2026. Instagram, Dailymotion, and Vimeo have no number in the chapter. The diagnostic order is editorial.*",
    "Independent guide. Not affiliated with or endorsed by YouTube or any other platform named here. Not legal or tax advice. Check current official terms before acting.",
    "Pages cited in the chapters, so you can open them:",
    "[YouTube recommended upload encoding settings](https://support.google.com/youtube/answer/1722171) — bitrate, H.264, AAC-LC, 48 kHz.",
    "[YouTube Audio Library](https://support.google.com/youtube/answer/3376882) — where the library lives, and that its tracks are the ones YouTube calls copyright-safe.",
    "[YouTube Partner Program eligibility](https://support.google.com/youtube/answer/72851), [2027 Partner Program changes](https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/), [monetization overview](https://support.google.com/youtube/answer/94522), [how to earn money on YouTube](https://support.google.com/youtube/answer/72857), [channel monetization policies](https://support.google.com/youtube/answer/1311392), [which links are clickable](https://support.google.com/youtube/answer/13748639), [cards](https://support.google.com/youtube/answer/6140493), [end screens](https://support.google.com/youtube/answer/6388789).",
    "[Ad revenue analytics: RPM and CPM](https://support.google.com/youtube/answer/9314357), [partner earnings overview](https://support.google.com/youtube/answer/72902), [ad formats](https://support.google.com/youtube/answer/2467968), [mid-roll ads](https://support.google.com/youtube/answer/6175006), [Shorts monetization policies](https://support.google.com/youtube/answer/12504220), [advertiser-friendly content guidelines](https://support.google.com/youtube/answer/6162278).",
    "[Commerce Products monetization policies](https://support.google.com/youtube/answer/13195878), [channel memberships](https://support.google.com/youtube/answer/7636690), [membership levels and perks](https://support.google.com/youtube/answer/7544492), [US membership prices](https://support.google.com/youtube/answer/10119895), [Super Chat and Super Stickers](https://support.google.com/youtube/answer/7288782), [Super Chat eligibility](https://support.google.com/youtube/answer/9277801), [Super Thanks eligibility](https://support.google.com/youtube/answer/10879035), [Super Thanks tips](https://support.google.com/youtube/answer/13615971).",
    "[YouTube Creator Partnerships](https://support.google.com/youtube/answer/9385307), [YouTube Shopping affiliate program](https://support.google.com/youtube/answer/13376398), [Shopping expansion to 500 subscribers, March 2026](https://blog.youtube/creator-and-artist-stories/youtube-shopping-expansion-500-subscribers/).",
    "[Instagram, editing your profile](https://help.instagram.com/936495066470190/) and [Instagram link sticker](https://help.instagram.com/192168966243613). [TikTok, adding a website to your profile](https://support.tiktok.com/en/getting-started/setting-up-your-profile/adding-a-website-to-your-profile).",
    "[FTC Endorsement Guides, 16 CFR Part 255](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255) and [Disclosures 101 for Social Media Influencers](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers).",
    "[Video chapters](https://support.google.com/youtube/answer/9884579). [Impressions and watch time](https://support.google.com/youtube/answer/9314486), [impressions and click-through rate FAQ](https://support.google.com/youtube/answer/7628154), [reach reports](https://support.google.com/youtube/answer/9314355), [content performance](https://support.google.com/youtube/answer/12220281).",
    "[Community Guidelines strike basics](https://support.google.com/youtube/answer/2802032), [copyright strikes](https://support.google.com/youtube/answer/2814000), [copyright claims](https://support.google.com/youtube/answer/6013276), [paid promotion](https://support.google.com/youtube/answer/154235), [disclosing AI use](https://support.google.com/youtube/answer/14328491), [audience setting and made for kids](https://support.google.com/youtube/answer/9527654), [spam policy](https://support.google.com/youtube/answer/2801973), [fake engagement policy](https://support.google.com/youtube/answer/3399767), [external links policy](https://support.google.com/youtube/answer/9054257).",
    "[Decoder interview with Marques Brownlee, The Verge, January 2021](https://www.theverge.com/22231657/mkbhd-marques-brownlee-interview-youtube-creator-influencer-decoder). [Recode Media transcript, April 2018](https://www.vox.com/2018/4/16/17241282/transcript-youtube-creator-marques-brownlee-mkbhd). [Andrew Rea, Mashed](https://www.mashed.com/612523/andrew-rea-tells-us-how-binging-with-babish-got-started-exclusive-interview/). [Hannah Hart, The Verge, 19 October 2016](https://www.theverge.com/2016/10/19/13315924/hannah-hart-interview-youtube-buffering-my-drunk-kitchen).",
]

GLOSSARY = [
    ("Eight jobs", "The only set of videos this book asks you to finish: who it is for, the problem in their words, the method, proof, the comparison, one objection, the deep dive, and which video to watch next. Chapters 2, 5, and 6 use this same set."),
    ("Deep dive", "The long, complete video in the eight jobs, built to be watched for a long time. The video that fills the hour bar, and the one that can honestly pass eight minutes for mid-roll ads."),
    ("Expanded program", "In countries where YouTube has opened it, the earlier gate: 500 subscribers, three public uploads in 90 days, and either 3,000 long-form hours in a year or 3 million Shorts views in 90 days. Fan funding and Shopping. Not a share of watch-page ads."),
    ("YouTube Partner Program", "The higher gate: 1,000 subscribers and either 4,000 long-form hours in 12 months or 10 million qualified Shorts views in 90 days. For channels that apply from 1 February 2027: 8,000 hours in 365 days or 20 million Shorts views in 90 days. This is the gate that adds watch-page ads, Shorts Feed ads, and YouTube Premium revenue. The follower-floor chart’s YouTube bar is this gate."),
    ("Qualified watch hours", "Public long-form viewing that YouTube counts toward the hour bars. Hours watched in the Shorts feed do not count. Private, unlisted, deleted, and ad-campaign views do not count."),
    ("Qualified Shorts views", "Public views of Shorts in the Shorts feed that YouTube counts toward the Shorts bars: 3 million in 90 days for the expanded program, or 10 million in 90 days for the Partner Program (20 million for channels applying from 1 February 2027). They do not fill the long-form hour bars."),
    ("Follow-on views", "Organic views from people who watch more of your videos after seeing a promoted one. The only part of a paid campaign that counts toward the Partner Program."),
    ("Advanced features", "The Studio status that makes an address in a long-form description, and in a long-form comment, clickable. Phone verification comes first. A Short’s description and comments stay unclickable after it is on. The Partner Program requires it."),
    ("AdSense", "AdSense for YouTube, the Google account YouTube uses to pay a channel it has accepted. Meeting a subscriber number does not open it. You apply, and YouTube reviews the channel."),
    ("Modules", "The separate sets of terms you accept in Studio’s Earn tab once inside the program: Watch Page Monetization for long-form ads and Premium, Shorts Monetization for the Shorts feed, and the Commerce Product Module for fan funding."),
    ("CPM", "What advertisers paid per 1,000 ad impressions on your videos, before YouTube’s share. Ads and Premium only, monetized views only."),
    ("Playback-based CPM", "What advertisers paid per 1,000 playbacks that showed at least one ad. Often higher than CPM, because one playback can carry two ads."),
    ("RPM", "Your total revenue after YouTube’s share, per 1,000 views, including views with no ad. Includes ads, Premium, memberships, Super Chat, and Super Stickers. Always lower than CPM."),
    ("Mid-roll", "An ad break during a video. Available on monetized videos eight minutes or longer, placed automatically, by hand, or both. Breaks at natural pauses are more likely to serve an ad."),
    ("Limited ads", "The monetization status of a video that does not fully meet the advertiser-friendly guidelines: fewer advertisers, or none. Not a strike. You can request a human review."),
    ("Shorts Creator Pool", "The monthly pot of Shorts Feed ad revenue that YouTube shares out by each monetizing channel’s share of engaged Shorts views, after a share for music licensing. The channel keeps 45% of its allocation. From 1 February 2027, a month counts only if the channel had 10 million qualified Shorts views in the previous 90 days."),
    ("YouTube Premium revenue", "A share of Premium and Premium Lite subscription fees, pooled and paid by members’ watch time and views: 55% for long-form, 45% for Shorts, of the pool allocated to creators."),
    ("Channel memberships", "Monthly payments from viewers for perks you choose, in up to six levels. The channel receives 70% after taxes and fees. Downloads of YouTube content, in-person one-to-one meetings, and random prizes are not allowed as perks."),
    ("Super Chat and Super Stickers", "Paid, highlighted messages and animated stickers in the live chat of a live stream or premiere. The channel receives 70% after taxes and fees. YouTube says they are not donation tools."),
    ("Super Thanks", "A one-time paid animation and highlighted comment on a long-form video or a Short. Not available on claimed, unlisted, made-for-kids, or comments-off videos, or while a stream is live. The channel receives 70% after taxes and fees."),
    ("Sponsor", "One company paying you for one video or segment. Tick the paid promotion box, say so in the video, and say so next to the link. One sponsor per video."),
    ("Creator Partnerships", "YouTube’s matching tool between brands and creators, the successor to BrandConnect. Open to partners eligible for ad revenue sharing, 18 or older, in supported countries, with no active strikes."),
    ("Affiliate link", "A link that pays you a commission if the viewer buys a product you recommended. Say so next to the link. The FTC pages in the sources list are the US disclosure guidance this book points at."),
    ("Shopping affiliate program", "YouTube’s own affiliate program for tagging other brands’ products in Shorts, long videos, and live streams. Open to partners with at least 500 subscribers in listed countries since March 2026."),
    ("Inauthentic content", "YouTube’s monetization name, since July 2025, for templated, repetitive, or mass-produced videos, including generic AI-made ones. It can keep a whole channel out of the Partner Program."),
    ("Reused content", "Someone else’s material republished without significant original commentary, modification, or educational value. A monetization policy that applies to the whole channel."),
    ("End screen", "An element in the last 5 to 20 seconds of a video at least 25 seconds long. One that opens a site outside YouTube requires the Partner Program."),
    ("Info card", "A small panel attached to the video. One that opens a site outside YouTube also requires the Partner Program."),
    ("Series playlist", "A playlist YouTube can feature as the next video while someone is watching one of yours. The account has to be verified, the videos have to be yours, and a video can sit in only one series playlist."),
    ("Short", "A vertical video, 1080 by 1920. On YouTube, an address in a Short’s description or comments is not clickable. A Short can point at a long video. Its hours in the Shorts feed do not fill the hour bar."),
    ("H.264", "The video codec named in YouTube’s recommended upload settings for an MP4. The audio codec named beside it is AAC-LC."),
    ("9:16", "The vertical frame for a Short: 1080 pixels wide by 1920 tall. A horizontal video is 16:9, 1920 by 1080."),
    ("Closed captions", "A text track the viewer can turn on or off. The words can be searched. They are not burned into the picture."),
    ("Burned-in captions", "Words that are part of the picture. They stay on. They are a different choice from closed captions."),
    ("Fader", "The volume slider in an editor. A music fader at about a tenth to a fifth of the way up is a position on that slider, not a measurement of loudness."),
    ("Text-to-speech", "A tool that reads a script aloud. Usable when the voice is not a clone of someone else. Cloning someone else’s voice is a consent question the tool does not answer for you."),
    ("Stock license", "The terms on one clip or track. “Free” and “free to use commercially” are different sentences. Read the line on that file before you publish it, including on a second site."),
    ("Impression", "In Studio, a thumbnail shown on YouTube for more than one second with at least half of it visible. Thumbnails on other websites, in end screens, and in notifications are not counted."),
    ("Impressions click-through rate", "How often a counted impression became a view. YouTube says half of channels and videos fall between 2% and 10%. It is a band, not a target."),
    ("Traffic source", "Studio’s label for how a viewer reached a video: search, suggested videos, browse features, playlists, external, and others. Views from links in video descriptions are filed under suggested videos."),
    ("Video chapters", "Timestamps in the description that split a video into named parts. The first is 00:00, there are at least three, and each part is at least ten seconds."),
    ("Community Guidelines warning", "What a first violation typically gets. An optional policy training lets it expire 90 days after the training. A further violation of the same policy in that window can become a strike."),
    ("Copyright strike", "The result of a valid legal removal request. The video comes down. It expires 90 days after it was applied once Copyright School is done, or it can be resolved by a retraction or a counter notification."),
    ("Content ID claim", "An automatic match against a rights holder’s file. It affects that video: monetize, track, or block. It is not a strike, unless a dispute without a valid reason leads to a removal request."),
    ("Paid promotion box", "The Studio setting you tick when a company paid you or gave you the product for a video. YouTube then shows a disclosure. Say it in the video as well."),
    ("AI use", "The upload setting for realistic content that generative AI made or meaningfully altered, including AI-generated music. Scripts, ideas, captions, thumbnails, and a clone of your own voice do not need it."),
    ("Made for kids", "The audience setting for videos directed to children, required under US law. It turns off comments, end screens, personalized ads, memberships, Supers, and more on those videos."),
]


if __name__ == "__main__":
    main()
