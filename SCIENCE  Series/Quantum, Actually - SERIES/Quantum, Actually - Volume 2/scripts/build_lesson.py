"""Build a QED Course lesson from a lightweight text markup.

Usage:  python build_lesson.py lessonNN.txt [--no-complete]
Produces "chapters/Lesson NN Title.docx" and replaces the
matching lesson section inside "Quantum, Actually - Volume 2.docx".

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
  IMG: file.png | width_inches | caption   figure from ../figures (centred, captioned)
  BOX: Title      shaded box; following lines until ENDBOX are its paragraphs
                  ("- " bullets and "$$ " display lines allowed inside)
  anything else   Normal paragraph
"""
import os
import re
import unicodedata
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
CHAPTERS = os.path.join(ROOT, "chapters")
TEMPLATE = os.path.join(CHAPTERS, "Lesson 01 Complex Numbers and Linear Algebra.docx")
AUTHOR = "Lothar J. Musiol"
# Quantum, Actually series (Volume 2: A QED Course). Heading numbering follows the Physics,
# Actually books ("Chapter N: Title"): "Lesson N: Title", "Prologue N: Title",
# "Part I — Title", "Interlude: Title". Matchers accept the old space form too.
SERIES = "Quantum, Actually"
SERIES_VOLUME = 2
VOLUME_TITLE = "A QED Course"
FULL_TITLE = "%s — Volume %d: %s" % (SERIES, SERIES_VOLUME, VOLUME_TITLE)
RUNNING_HEAD = FULL_TITLE
CHAPTER_HEAD = "A QED Course   %s %s"  # standalone chapter files


def lesson_heading(num, title):
    return "Lesson %d: %s" % (int(num), title)


def is_lesson_heading(text, num):
    return re.match(r"^Lesson %d[: ]" % int(num), text or "") is not None
EDITION = "First edition, 2026"
COMPLETE = os.path.join(ROOT, "Quantum, Actually - Volume 2.docx")
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
PAGE_WIDTH = 9792  # twips of text width (12240 - 1296 - 1152)
HEADER_FILL, BAND_FILL = "1F4E78", "EAF2F8"
BOX_FILL, BOX_LINE = "F3F7FB", "7FA7CF"
FIGURES = os.path.join(ROOT, "figures")


# ---------------------------------------------------------------- parsing
def _split_row(line):
    """Cells of a | a | b | row. A cell separator has white space on both
    sides, so |ℳ|², ⟨φ|ψ⟩ and |ψ⟩ inside a cell stay in that cell; \\| is
    an explicit bar."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells = re.split(r"(?<!\\)(?<=\s)\|(?=\s)", s)
    return [c.strip().replace("\\|", "|") for c in cells]


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
                rows.append(_split_row(lines[i]))
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
        if line.startswith("IMG:"):
            parts = [x.strip() for x in line[4:].split("|", 2)]
            while len(parts) < 3:
                parts.append("")
            blocks.append(("image", parts[0], float(parts[1] or 5.5), parts[2]))
            i += 1
            continue
        if line.startswith("BOX:"):
            title = line[4:].strip()
            body = []
            i += 1
            while i < len(lines) and lines[i].strip() != "ENDBOX":
                if lines[i].strip():
                    body.append(lines[i].strip())
                i += 1
            if i < len(lines):
                i += 1
            blocks.append(("box", title, body))
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


_GREEK_IDX = "μνρσαβλκτ"
_LATIN_LO = "abcdefghijklmnopqrstuvwxyz"
_SUB_WORDS = {"int", "eff", "sym", "ext", "max", "min", "cl", "gf", "fi", "if", "tot", "phys", "ren",
              "kin", "em", "out", "in", "obs", "rad", "th", "free", "bare", "exp", "lab", "cm", "rel", "loc", "ij", "ik", "jk"}
_SCRIPT_RE = re.compile(r"(?<=[^\s^_])([\^_])(?=[^\s,.;:)\]}|])")


def _script_token(text, i):
    """Return (content, end) for the index starting at text[i] (just after ^ or _)."""
    c = text[i]
    pairs = {"(": ")", "{": "}"}
    if c in pairs:
        depth, j = 0, i
        while j < len(text):
            if text[j] == c:
                depth += 1
            elif text[j] == pairs[c]:
                depth -= 1
                if depth == 0:
                    inner = text[i + 1:j]
                    # S^(2), x^(n): a perturbative order keeps its brackets
                    if c == "(" and re.fullmatch(r"\d+|[a-zA-Z]", inner):
                        return text[i:j + 1], j + 1
                    return inner, j + 1
            j += 1
        return None, i
    j = i + 1
    if c in _GREEK_IDX:
        while j < len(text) and text[j] in _GREEK_IDX:
            j += 1
    elif c.isdigit():
        while j < len(text) and (text[j].isdigit() or text[j] in "ijk"):
            j += 1
    elif c in "+−-":
        while j < len(text) and text[j].isdigit():
            j += 1
    elif c in _LATIN_LO:
        k = j
        while k < len(text) and text[k] in _LATIN_LO:
            k += 1
        word = text[i:k]
        if k < len(text) and unicodedata.category(text[k]) == "Mn" and len(word) > 1:
            word = word[:-1]; k -= 1  # k̂ after an index letter belongs to the base
        if word in _SUB_WORDS or (len(word) <= 3 and set(word) <= set("ijkl0")):
            j = k
        elif len(word) > 4 and not any(word.startswith(w) for w in _SUB_WORDS):
            return None, i  # an ordinary word joined by an underscore
    elif c.isupper():
        k = j
        while k < len(text) and text[k].isupper() and text[k].isascii():
            k += 1
        if k - i >= 2 and (k >= len(text) or not text[k].isalpha()):
            j = k
    elif c in "*†′" or c.isalpha():
        pass
    else:
        return None, i
    while j < len(text) and unicodedata.category(text[j]) == "Mn":
        j += 1
    while j < len(text) and text[j] in "*†′":
        j += 1
    return text[i:j], j


_UNI_SUB = dict(zip("0123456789+−-=()aeoxhklmnpstijruvβγρφχ", "₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜᵢⱼᵣᵤᵥᵦᵧᵨᵩᵪ"))
_UNI_SUP = dict(zip("0123456789+−-=()inabcdefghjklmoprstuvwxyzβγδθφχ", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ⁱⁿᵃᵇᶜᵈᵉᶠᵍʰʲᵏˡᵐᵒᵖʳˢᵗᵘᵛʷˣʸᶻᵝᵞᵟᶿᵠᵡ"))


def _flatten_nested(content):
    """Inside a super/subscript, a nested index is written with Unicode
    sub/superscript letters where they exist; otherwise the markup is kept."""
    out = []
    for seg, vert in _script_segments(content, nested=True):
        if vert is None:
            out.append(seg)
        else:
            table = _UNI_SUB if vert == "subscript" else _UNI_SUP
            if all(ch in table for ch in seg):
                out.append("".join(table[ch] for ch in seg))
            else:
                out.append(("_" if vert == "subscript" else "^") + (seg if len(seg) == 1 else "(" + seg + ")"))
    return "".join(out)


def _script_segments(text, nested=False):
    """Split plain text into (string, vert) pieces: inline x^μ, A_μ, e^(ipx), S_{fi}
    become superscript/subscript runs instead of raw markup."""
    out, buf, i = [], [], 0
    while i < len(text):
        ch = text[i]
        if ch in "^_" and i > 0 and not text[i - 1].isspace() and i + 1 < len(text) \
                and not text[i + 1].isspace() and text[i - 1] not in "^_" and not text[i-1].isdigit() or \
                (ch in "^_" and i > 0 and text[i - 1].isdigit() and ch == "^"):
            content, j = _script_token(text, i + 1)
            if content:
                if buf:
                    out.append(("".join(buf), None)); buf = []
                if not nested and ("^" in content or "_" in content):
                    content = _flatten_nested(content)
                out.append((content, "superscript" if ch == "^" else "subscript"))
                i = j
                continue
        buf.append(ch)
        i += 1
    if buf:
        out.append(("".join(buf), None))
    return out


def _add_runs(paragraph, text, bold=False, italic=False):
    for seg, vert in _script_segments(text):
        r = paragraph.add_run(seg)
        if bold:
            r.bold = True
        if italic:
            r.italic = True
        if vert == "superscript":
            r.font.superscript = True
        elif vert == "subscript":
            r.font.subscript = True


def add_rich_text(paragraph, text):
    """Tiny inline markup: **bold** and *italic*; inline ^ and _ indices become
    real superscripts and subscripts."""
    # \| is the table escape for a literal bar; outside a table it is a bar.
    # A lone * is complex conjugation (φ*, ε*, ℳ_u^*), so *italic* needs a
    # space or opening bracket before it and a space or punctuation after.
    text = text.replace("\\|", "|")
    pos = 0
    for m in re.finditer(r"\*\*(.+?)\*\*|(?<![^\s(“\"])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?=[\s.,;:!?)”\"]|$)", text):
        if m.start() > pos:
            _add_runs(paragraph, text[pos:m.start()])
        if m.group(1) is not None:
            _add_runs(paragraph, m.group(1), bold=True)
        else:
            _add_runs(paragraph, m.group(2), italic=True)
        pos = m.end()
    if pos < len(text):
        _add_runs(paragraph, text[pos:])


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

    def image(self, name, width, caption):
        from docx.shared import Inches
        path = os.path.join(FIGURES, name)
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        p.add_run().add_picture(path, width=Inches(width))
        self.elements.append(p._p)
        if caption:
            c = self.doc.add_paragraph()
            c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            c.paragraph_format.space_after = Pt(10)
            add_rich_text(c, caption)
            for r in c.runs:
                r.italic = True
                r.font.size = Pt(9.5)
            self.elements.append(c._p)

    def box(self, title, body):
        tbl = self.doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl_pr = tbl._tbl.tblPr
        for child in list(tbl_pr):
            if child.tag == qn("w:tblStyle"):
                tbl_pr.remove(child)
        borders = OxmlElement("w:tblBorders")
        for side in ("top", "left", "bottom", "right"):
            el = OxmlElement("w:" + side)
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "8")
            el.set(qn("w:color"), BOX_LINE)
            borders.append(el)
        tbl_pr.append(borders)
        for gc in tbl._tbl.tblGrid.findall(qn("w:gridCol")):
            gc.set(qn("w:w"), str(PAGE_WIDTH - 400))
        cell = tbl.cell(0, 0)
        cell.width = Twips(PAGE_WIDTH - 400)
        tc_pr = cell._tc.get_or_add_tcPr()
        _shade(tc_pr, BOX_FILL)
        _cell_margins(tc_pr, 140)
        p = cell.paragraphs[0]
        r = p.add_run(title)
        r.bold = True
        r.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)
        for line in body:
            if line.startswith("- "):
                q = cell.add_paragraph(style="List Bullet")
                add_rich_text(q, line[2:])
            elif line.startswith("$$"):
                q = cell.add_paragraph()
                q.alignment = WD_ALIGN_PARAGRAPH.CENTER
                omp = etree.SubElement(q._p, "{%s}oMathPara" % M_NS)
                om = etree.SubElement(omp, "{%s}oMath" % M_NS)
                try:
                    from omath import fill_omath
                    fill_omath(om, line[2:].strip())
                except Exception:
                    rr = etree.SubElement(om, "{%s}r" % M_NS)
                    t = etree.SubElement(rr, "{%s}t" % M_NS)
                    t.text = line[2:].strip()
            else:
                q = cell.add_paragraph()
                add_rich_text(q, line)
            q.paragraph_format.space_after = Pt(3)
        self.elements.append(tbl._tbl)
        spacer = self.doc.add_paragraph()
        spacer.paragraph_format.space_after = Pt(4)
        self.elements.append(spacer._p)

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
            elif kind == "image":
                self.image(b[1], b[2], b[3])
            elif kind == "box":
                self.box(b[1], b[2])
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


def set_core(doc, title=None):
    doc.core_properties.author = AUTHOR
    if title:
        doc.core_properties.title = title


def build_standalone(meta, blocks, out_path):
    doc = Document(TEMPLATE)
    body = doc.element.body
    for child in list(body):
        if child.tag != qn("w:sectPr"):
            body.remove(child)
    hdr = doc.sections[0].header
    for p in hdr.paragraphs:
        if "QED Course" in p.text or "Lesson" in p.text:
            for r in p.runs[1:]:
                r.text = ""
            p.runs[0].text = CHAPTER_HEAD % ("Lesson", meta["NUM"])
    b = Builder(doc)
    p = b.para(meta["TITLE"], style="Title")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = b.para("Lesson %s of %s, Volume %d: %s" % (meta["NUM"], SERIES, SERIES_VOLUME, VOLUME_TITLE), style="Subtitle")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = b.para(AUTHOR)
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
    p = b.para(EDITION)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    b.pagebreak()
    b.render(blocks)
    if meta.get("NEXT"):
        b.heading("Next lesson", 2)
        b.para(meta["NEXT"])
    set_core(doc, meta["TITLE"])
    doc.save(out_path)


LESSON_RE = re.compile(
    r"^(Lesson \d+[: ]|Part [IVX0]|Prologue \d+|Interlude[: ]|"
    r"Course capstone|Consolidated formula index|"
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
        if start is None and is_lesson_heading(text, num):
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
    title_p = b.heading(lesson_heading(num, meta["TITLE"]), 1)
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
    out = os.path.join(CHAPTERS, "Lesson %02d %s.docx" % (int(meta["NUM"]), meta["TITLE"]))
    build_standalone(meta, blocks, out)
    if "--no-complete" not in sys.argv:
        splice_into_complete(meta, blocks)
    print("built %s (%d blocks)" % (os.path.basename(out), len(blocks)))


if __name__ == "__main__":
    main()
