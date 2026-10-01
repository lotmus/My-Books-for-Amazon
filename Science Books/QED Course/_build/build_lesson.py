"""Build a QED Course lesson from a lightweight text markup.

Usage:  python build_lesson.py lessonNN.txt [--no-complete]
Produces "Lesson NN Title.docx" next to the Complete file and replaces the
matching lesson section inside "Complete QED Course.docx".

Markup (one block per line, blank lines separate blocks):
  TITLE: ...      TAGLINE: ...      NUM: 2      NEXT: text for "Next lesson"
  # / ## / ###    headings 1-3
  - text          bullet (ListBullet)
  1. text         numbered item (ListNumber, numbering restarts per list)
  $$ text         centred display equation (Unicode text in an OMML run)
  | a | b |       table row (first row of a block is the header)
  @widths 2160 7632   column widths in twips for the following table
  **N.** text     solution paragraph (bold lead)
  \\pagebreak      page break
  anything else   Normal paragraph
"""
import os
import re
import sys

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Twips
from lxml import etree

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
TEMPLATE = os.path.join(ROOT, "Lesson 01 Complex Numbers and Linear Algebra.docx")
COMPLETE = os.path.join(ROOT, "Complete QED Course.docx")
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
PAGE_WIDTH = 9792  # twips of text width (12240 - 1296 - 1152)
HEADER_FILL, BAND_FILL = "1F4E78", "EAF2F8"


# ---------------------------------------------------------------- parsing
def parse(path):
    meta, blocks = {}, []
    with open(path, encoding="utf-8") as fh:
        lines = [l.rstrip("\n") for l in fh]
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = re.match(r"^(TITLE|TAGLINE|NUM|NEXT):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
            i += 1
            continue
        widths = None
        if line.startswith("@widths"):
            widths = [int(w) for w in line.split()[1:]]
            i += 1
            line = lines[i]
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip().replace("\\|", "|")
                             for c in re.split(r"(?<!\\)\|", lines[i].strip().strip("|"))])
                i += 1
            blocks.append(("table", widths, rows))
            continue
        if re.match(r"^\d+\.\s", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i]):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i]))
                i += 1
                # blank lines between items keep the same list
                j = i
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and re.match(r"^\d+\.\s", lines[j]):
                    i = j
            blocks.append(("numbered", items))
            continue
        if line.startswith("FIG:"):
            fig = []
            i += 1
            while i < len(lines) and lines[i].strip() != "ENDFIG":
                fig.append(lines[i][1:] if lines[i].startswith(" ") else lines[i])
                i += 1
            if i < len(lines) and lines[i].strip() == "ENDFIG":
                i += 1
            blocks.append(("figure", fig))
            continue
        if line.startswith("### "):
            blocks.append(("h3", line[4:]))
        elif line.startswith("## "):
            blocks.append(("h2", line[3:]))
        elif line.startswith("# "):
            blocks.append(("h1", line[2:]))
        elif line.startswith("- "):
            blocks.append(("bullet", line[2:]))
        elif line.startswith("$$"):
            blocks.append(("math", line[2:].strip()))
        elif line.strip() == "\\pagebreak":
            blocks.append(("pagebreak",))
        elif re.match(r"^\*\*[^*]+\*\*\s", line):
            m = re.match(r"^\*\*([^*]+)\*\*\s+(.*)$", line)
            blocks.append(("solution", m.group(1), m.group(2)))
        else:
            blocks.append(("para", line))
        i += 1
    return meta, blocks


# ---------------------------------------------------------------- docx helpers
def _shade(tc_pr, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def _cell_margins(tc_pr, w=100):
    mar = OxmlElement("w:tcMar")
    for side in ("top", "start", "bottom", "end"):
        el = OxmlElement("w:" + side)
        el.set(qn("w:w"), str(w))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tc_pr.append(mar)


def add_rich_text(paragraph, text):
    """Tiny inline markup: **bold** and *italic*."""
    pos = 0
    for m in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*", text):
        if m.start() > pos:
            paragraph.add_run(text[pos:m.start()])
        if m.group(1) is not None:
            paragraph.add_run(m.group(1)).bold = True
        else:
            paragraph.add_run(m.group(2)).italic = True
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])


class Builder:
    def __init__(self, doc):
        self.doc = doc
        self.elements = []  # body elements created, in order
        self._list_abstract = self._find_list_abstract()

    # numbering ------------------------------------------------------------
    def _find_list_abstract(self):
        styles = self.doc.styles.element
        num_id = None
        for st in styles.findall(qn("w:style")):
            if st.get(qn("w:styleId")) == "ListNumber":
                el = st.find(".//" + qn("w:numId"))
                num_id = el.get(qn("w:val"))
        numbering = self.doc.part.numbering_part.element
        for num in numbering.findall(qn("w:num")):
            if num.get(qn("w:numId")) == num_id:
                return num.find(qn("w:abstractNumId")).get(qn("w:val"))
        raise RuntimeError("ListNumber numbering not found")

    def _new_num(self):
        numbering = self.doc.part.numbering_part.element
        nums = numbering.findall(qn("w:num"))
        new_id = max(int(n.get(qn("w:numId"))) for n in nums) + 1
        num = OxmlElement("w:num")
        num.set(qn("w:numId"), str(new_id))
        an = OxmlElement("w:abstractNumId")
        an.set(qn("w:val"), self._list_abstract)
        num.append(an)
        lo = OxmlElement("w:lvlOverride")
        lo.set(qn("w:ilvl"), "0")
        so = OxmlElement("w:startOverride")
        so.set(qn("w:val"), "1")
        lo.append(so)
        num.append(lo)
        nums[-1].addnext(num)
        return new_id

    # primitives -----------------------------------------------------------
    def para(self, text="", style=None):
        p = self.doc.add_paragraph(style=style)
        if text:
            add_rich_text(p, text)
        self.elements.append(p._p)
        return p

    def heading(self, text, level):
        return self.para(text, style="Heading %d" % level)

    def bullet(self, text):
        return self.para(text, style="List Bullet")

    def numbered(self, items):
        num_id = self._new_num()
        for it in items:
            p = self.para(it, style="List Number")
            num_pr = p._p.get_or_add_pPr().get_or_add_numPr()
            num_pr.get_or_add_ilvl().val = 0
            num_pr.get_or_add_numId().val = num_id

    def math(self, text):
        parts = [p.strip() for p in re.split(r"\s*,?\s*qquad\s*", text) if p.strip()]
        if not parts:
            parts = [text]
        for i, part in enumerate(parts):
            p = self.doc.add_paragraph()
            p.paragraph_format.space_before = Pt(5 if i == 0 else 2)
            p.paragraph_format.space_after = Pt(8 if i == len(parts) - 1 else 2)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            omp = etree.SubElement(p._p, "{%s}oMathPara" % M_NS)
            om = etree.SubElement(omp, "{%s}oMath" % M_NS)
            try:
                from omath import fill_omath
                fill_omath(om, part)
            except Exception:
                r = etree.SubElement(om, "{%s}r" % M_NS)
                t = etree.SubElement(r, "{%s}t" % M_NS)
                t.set(XML_SPACE, "preserve")
                t.text = part
            self.elements.append(p._p)

    def figure(self, lines):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(8)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for i, line in enumerate(lines):
            run = p.add_run(("" if i == 0 else "\n") + line)
            run.font.name = "Consolas"
            run.font.size = Pt(10)
            rpr = run._element.get_or_add_rPr()
            rfonts = rpr.find(qn("w:rFonts"))
            if rfonts is None:
                rfonts = OxmlElement("w:rFonts")
                rpr.append(rfonts)
            for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
                rfonts.set(qn(a), "Consolas")
        self.elements.append(p._p)

    def solution(self, lead, text):
        p = self.doc.add_paragraph()
        p.add_run(lead).bold = True
        p.add_run(" ")
        add_rich_text(p, text)
        self.elements.append(p._p)

    def pagebreak(self):
        p = self.doc.add_paragraph()
        p.add_run().add_break(WD_BREAK.PAGE)
        self.elements.append(p._p)

    def table(self, rows, widths=None):
        ncols = max(len(r) for r in rows)
        if not widths or len(widths) != ncols:
            widths = [PAGE_WIDTH // ncols] * ncols
        tbl = self.doc.add_table(rows=len(rows), cols=ncols)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl_pr = tbl._tbl.tblPr
        for child in list(tbl_pr):
            if child.tag == qn("w:tblStyle"):
                tbl_pr.remove(child)
        layout = OxmlElement("w:tblLayout")
        layout.set(qn("w:type"), "fixed")
        tbl_pr.append(layout)
        look = OxmlElement("w:tblLook")
        for k, v in (("firstColumn", "1"), ("firstRow", "1"), ("lastColumn", "0"),
                     ("lastRow", "0"), ("noHBand", "0"), ("noVBand", "1"), ("val", "04A0")):
            look.set(qn("w:" + k), v)
        tbl_pr.append(look)
        grid = tbl._tbl.tblGrid
        for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
            gc.set(qn("w:w"), str(w))
        for ri, row in enumerate(rows):
            for ci in range(ncols):
                cell = tbl.cell(ri, ci)
                cell.width = Twips(widths[ci])
                tc_pr = cell._tc.get_or_add_tcPr()
                if ri == 0:
                    _shade(tc_pr, HEADER_FILL)
                cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
                if ri > 0 and ri % 2 == 0:
                    _shade(tc_pr, BAND_FILL)
                _cell_margins(tc_pr)
                text = row[ci] if ci < len(row) else ""
                p = cell.paragraphs[0]
                if ri == 0:
                    run = p.add_run(text)
                    run.bold = True
                    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                else:
                    add_rich_text(p, text)
        self.elements.append(tbl._tbl)

    # driver ---------------------------------------------------------------
    def render(self, blocks):
        for b in blocks:
            kind = b[0]
            if kind == "h1":
                # Lesson titles are Heading 1; intra-lesson # sections are Heading 2
                # so the TOC lists lessons, not every "How to use this lesson".
                self.heading(b[1], 2)
            elif kind == "h2":
                self.heading(b[1], 3)
            elif kind == "h3":
                p = self.para(style=None)
                run = p.add_run(b[1])
                run.bold = True
                run.italic = True
            elif kind == "bullet":
                self.bullet(b[1])
            elif kind == "numbered":
                self.numbered(b[1])
            elif kind == "math":
                self.math(b[1])
            elif kind == "table":
                self.table(b[2], b[1])
            elif kind == "solution":
                self.solution(b[1], b[2])
            elif kind == "figure":
                self.figure(b[1])
            elif kind == "pagebreak":
                self.pagebreak()
            elif kind == "para":
                self.para(b[1])
            else:
                raise ValueError(kind)


def _bookmark_paragraph(paragraph, name, bid):
    """Attach a Word bookmark to an existing paragraph."""
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(bid))
    start.set(qn("w:name"), name)
    paragraph._p.insert(0, start)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), str(bid))
    paragraph._p.append(end)
    return paragraph


def build_standalone(meta, blocks, out_path):
    doc = Document(TEMPLATE)
    body = doc.element.body
    for child in list(body):
        if child.tag != qn("w:sectPr"):
            body.remove(child)
    hdr = doc.sections[0].header
    for p in hdr.paragraphs:
        if "QED Course" in p.text:
            for r in p.runs[1:]:
                r.text = ""
            p.runs[0].text = "QED Course   Lesson %s" % meta["NUM"]
    b = Builder(doc)
    p = b.para(meta["TITLE"], style="Title")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = b.para("Lesson %s of the Complete Quantum Electrodynamics Course" % meta["NUM"], style="Subtitle")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = b.para()
    p.add_run().add_break(WD_BREAK.LINE)
    p = b.para()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(meta["TAGLINE"])
    r.bold = True
    r.font.size = Pt(13)
    p = b.para()
    r = p.add_run()
    r.add_break(WD_BREAK.LINE)
    r.add_break(WD_BREAK.LINE)
    p = b.para("Course edition 1.0")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    b.pagebreak()
    b.render(blocks)
    if meta.get("NEXT"):
        b.heading("Next lesson", 2)
        b.para(meta["NEXT"])
    doc.save(out_path)


LESSON_RE = re.compile(
    r"^(Lesson \d+ |Part [IVX]+ |Course capstone|Consolidated formula index|"
    r"Glossary of symbols|Bibliography)"
)


def heading1_text(child):
    if child.tag != qn("w:p"):
        return None
    p_style = child.find(qn("w:pPr") + "/" + qn("w:pStyle"))
    if p_style is None or p_style.get(qn("w:val")) != "Heading1":
        return None
    return "".join(t.text or "" for t in child.iter(qn("w:t")))


def splice_into_complete(meta, blocks):
    doc = Document(COMPLETE)
    body = doc.element.body
    num = int(meta["NUM"])
    start = end = None
    for child in body:
        text = heading1_text(child)
        if text is None:
            continue
        if start is None and text.startswith("Lesson %d " % num):
            start = child
        elif start is not None and LESSON_RE.match(text):
            end = child
            break
    if start is None or end is None:
        raise RuntimeError("Could not locate Lesson %d in the Complete document" % num)
    node = start
    while node is not end:
        nxt = node.getnext()
        body.remove(node)
        node = nxt
    b = Builder(doc)
    title_p = b.heading("Lesson %d %s" % (num, meta["TITLE"]), 1)
    _bookmark_paragraph(title_p, "Lesson%d" % num, 1000 + num)
    b.render(blocks)
    if meta.get("NEXT"):
        b.heading("Next lesson", 2)
        b.para(meta["NEXT"])
    b.pagebreak()
    for el in b.elements:  # move the new elements in front of the next section
        end.addprevious(el)
    doc.save(COMPLETE)


def main():
    src = sys.argv[1]
    meta, blocks = parse(src)
    for k in ("TITLE", "NUM"):
        if k not in meta:
            sys.exit("missing %s: in %s" % (k, src))
    out = os.path.join(ROOT, "Lesson %02d %s.docx" % (int(meta["NUM"]), meta["TITLE"]))
    build_standalone(meta, blocks, out)
    if "--no-complete" not in sys.argv:
        splice_into_complete(meta, blocks)
    print("built %s (%d blocks)" % (os.path.basename(out), len(blocks)))


if __name__ == "__main__":
    main()
