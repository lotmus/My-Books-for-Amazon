# -*- coding: utf-8 -*-
"""Document-level finish: retitle, copyright, map, heading surgery,
static hyperlinked TOC, bookmarks, lesson links, gutter, bibliography.
Run after lessons have been spliced into Complete QED Course.docx.
"""
import os
import re
import sys
import time

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.shared import Inches, Pt, Twips
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lesson as bl

COMPLETE = bl.COMPLETE
BOOKMARK_TOC = "QEDCourseTOC"

KEEP_H1 = re.compile(
    r"^(Lesson \d+ |Part [IVX0]|Prologue \d+|Interlude |Table of Contents|Copyright|"
    r"How to read this book|Glossary of symbols|Course capstone|"
    r"Consolidated formula index|Bibliography)"
)
LESSON_H1 = re.compile(r"^Lesson (\d+) ")
LESSON_MENTION = re.compile(r"Lesson (\d+)")


def _is_body_start(text):
    t = text or ""
    return (
        t.startswith("Lesson 1 ")
        or t.startswith("Part 0")
        or t.startswith("Prologue 1")
    )


def _text(child):
    if child.tag != qn("w:p"):
        return ""
    return "".join(t.text or "" for t in child.iter(qn("w:t")))


def _p_style(child):
    if child.tag != qn("w:p"):
        return None
    el = child.find(qn("w:pPr") + "/" + qn("w:pStyle"))
    if el is None:
        return None
    return el.get(qn("w:val"))


def _set_p_style(child, style_id):
    pPr = child.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr")
        child.insert(0, pPr)
    el = pPr.find(qn("w:pStyle"))
    if el is None:
        el = OxmlElement("w:pStyle")
        pPr.insert(0, el)
    el.set(qn("w:val"), style_id)


def _bookmark_p(child, name, bid):
    for s in child.findall(qn("w:bookmarkStart")):
        if s.get(qn("w:name")) == name:
            return
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(bid))
    start.set(qn("w:name"), name)
    child.insert(0, start)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), str(bid))
    child.append(end)


def _hyperlink_run(paragraph, text, anchor):
    hl = OxmlElement("w:hyperlink")
    hl.set(qn("w:anchor"), anchor)
    r = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    st = OxmlElement("w:rStyle")
    st.set(qn("w:val"), "Hyperlink")
    rPr.append(st)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rPr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)
    r.append(rPr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    r.append(t)
    hl.append(r)
    paragraph._p.append(hl)


def find_first_pagebreak(doc):
    body = doc.element.body
    for child in body:
        if child.tag == qn("w:p"):
            for br in child.iter(qn("w:br")):
                if br.get(qn("w:type")) == "page":
                    return child
    raise RuntimeError("no title-page break")


def remove_old_toc(doc):
    body = doc.element.body
    in_block = False
    to_remove = []
    for child in list(body):
        text = _text(child)
        style = _p_style(child)
        starts = child.findall(qn("w:bookmarkStart")) if child.tag == qn("w:p") else []
        if any(s.get(qn("w:name")) == BOOKMARK_TOC for s in starts) or (
            style == "Heading1" and text == "Table of Contents"
        ):
            in_block = True
        if in_block:
            to_remove.append(child)
        if in_block and (
            text == "__QEDCourseTOC_END__"
            or (style == "Heading1" and _is_body_start(text))
        ):
            if _is_body_start(text):
                to_remove.pop()  # keep Part 0 / Prologue 1 / Lesson 1
            break
    for node in to_remove:
        parent = node.getparent()
        if parent is not None:
            parent.remove(node)


def remove_old_front(doc):
    """Remove previously inserted copyright / how-to-read blocks if re-run."""
    body = doc.element.body
    markers = {"Copyright", "How to read this book"}
    in_block = False
    to_remove = []
    for child in list(body):
        text = _text(child)
        style = _p_style(child)
        if style == "Heading1" and text in markers:
            in_block = True
        if in_block:
            to_remove.append(child)
        if in_block and style == "Heading1" and text not in markers and text:
            to_remove.pop()
            break
        if in_block and style == "Heading1" and _is_body_start(text):
            to_remove.pop()
            break
    for node in to_remove:
        parent = node.getparent()
        if parent is not None:
            parent.remove(node)


def retitle(doc):
    for p in doc.paragraphs[:12]:
        if p.style and p.style.name == "Subtitle":
            if "precision QED" in p.text or "mathematical foundations" in p.text.lower():
                for r in p.runs:
                    r.text = ""
                if p.runs:
                    p.runs[0].text = "From mathematical foundations to one-loop QED"
                else:
                    p.add_run("From mathematical foundations to one-loop QED")
        if p.text.strip() == "Mathematical foundations for quantum states, operators, spinors, and fields":
            for r in p.runs:
                r.text = ""
            if p.runs:
                p.runs[0].text = (
                    "A calculation course from complex numbers to a=α/(2π), "
                    "the running of α, and the Lamb and Schwinger mechanisms"
                )
            else:
                p.add_run(
                    "A calculation course from complex numbers to a=α/(2π), "
                    "the running of α, and the Lamb and Schwinger mechanisms"
                )
        if p.text.strip() == "Course edition 1.0":
            for r in p.runs:
                r.text = ""
            if p.runs:
                p.runs[0].text = "First edition, 2026"
            else:
                p.add_run("First edition, 2026")


def set_gutter(doc):
    for sec in doc.sections:
        sec.left_margin = Inches(1.15)
        sec.right_margin = Inches(0.95)
        sec.top_margin = Inches(0.95)
        sec.bottom_margin = Inches(0.9)
        pgMar = sec._sectPr.find(qn("w:pgMar"))
        if pgMar is not None:
            pgMar.set(qn("w:gutter"), str(int(Inches(0.3))))


def demote_headings(doc):
    n = 0
    for child in doc.element.body:
        if _p_style(child) != "Heading1":
            continue
        text = _text(child)
        if KEEP_H1.match(text or ""):
            continue
        _set_p_style(child, "Heading2")
        n += 1
    return n


def bookmark_lessons(doc):
    n = 0
    for child in doc.element.body:
        if _p_style(child) != "Heading1":
            continue
        m = LESSON_H1.match(_text(child) or "")
        if not m:
            continue
        num = int(m.group(1))
        _bookmark_p(child, "Lesson%d" % num, 1000 + num)
        n += 1
    for child in doc.element.body:
        if _p_style(child) != "Heading1":
            continue
        text = _text(child) or ""
        if text.startswith("Part "):
            token = text.split()[1] if len(text.split()) > 1 else ""
            if token.startswith("0"):
                slug = "Part0"
            else:
                slug = "Part" + re.sub(r"[^IVX]", "", token)
            _bookmark_p(child, slug or "Part", 2000 + hash(text) % 500)
        elif text == "Glossary of symbols":
            _bookmark_p(child, "Glossary", 3001)
        elif text == "Course capstone":
            _bookmark_p(child, "Capstone", 3002)
        elif text.startswith("Consolidated formula"):
            _bookmark_p(child, "FormulaIndex", 3003)
        elif text == "Bibliography":
            _bookmark_p(child, "Bibliography", 3004)
        elif text.startswith("Prologue "):
            pm = re.match(r"^Prologue (\d+)", text)
            if pm:
                _bookmark_p(child, "Prologue%s" % pm.group(1), 4000 + int(pm.group(1)))
        elif text.startswith("Interlude Classical Optics"):
            _bookmark_p(child, "Optics", 4011)
        elif text.startswith("Interlude "):
            _bookmark_p(child, "Mead", 4010)
        elif text == "How to read this book":
            _bookmark_p(child, "HowToRead", 3005)
        elif text == "Copyright":
            _bookmark_p(child, "Copyright", 3006)
    return n


def collect_toc_entries(doc):
    entries = []
    for child in doc.element.body:
        if _p_style(child) != "Heading1":
            continue
        text = _text(child).strip()
        if not text or text in ("Table of Contents", "Copyright"):
            continue
        m = LESSON_H1.match(text)
        if m:
            entries.append(("Lesson%d" % int(m.group(1)), text, False))
            continue
        pm = re.match(r"^Prologue (\d+)", text)
        if pm:
            entries.append(("Prologue%s" % pm.group(1), text, False))
            continue
        if text.startswith("Interlude Classical Optics"):
            entries.append(("Optics", text, False))
            continue
        if text.startswith("Interlude "):
            entries.append(("Mead", text, False))
            continue
        if text.startswith("Part "):
            token = text.split()[1] if len(text.split()) > 1 else ""
            if token.startswith("0"):
                slug = "Part0"
            else:
                slug = "Part" + re.sub(r"[^IVX]", "", token)
            entries.append((slug or "Part", text, True))
        elif text == "How to read this book":
            entries.append(("HowToRead", text, False))
        elif text == "Glossary of symbols":
            entries.append(("Glossary", text, False))
        elif text == "Course capstone":
            entries.append(("Capstone", text, False))
        elif text.startswith("Consolidated formula"):
            entries.append(("FormulaIndex", text, False))
        elif text == "Bibliography":
            entries.append(("Bibliography", text, False))
    return entries


def insert_static_toc(doc, entries):
    remove_old_toc(doc)
    # Place TOC after How to read this book if present, else after first page break
    body = doc.element.body
    anchor = None
    for child in body:
        if _p_style(child) == "Heading1" and _text(child) == "How to read this book":
            # find the page break after this section, or the Lesson 1 heading
            node = child
            last = child
            while node is not None:
                nxt = node.getnext()
                if nxt is not None and _p_style(nxt) == "Heading1" and _is_body_start(_text(nxt)):
                    anchor = last
                    break
                last = nxt if nxt is not None else last
                node = nxt
            break
    if anchor is None:
        anchor = find_first_pagebreak(doc)

    heading = doc.add_paragraph("Table of Contents", style="Heading 1")
    _bookmark_p(heading._p, BOOKMARK_TOC, 9001)
    intro = doc.add_paragraph(
        "Click any entry to jump. Page numbers appear in a printed copy; this table lists the course in reading order."
    )

    created = [heading._p, intro._p]
    for anchor_name, label, is_part in entries:
        p = doc.add_paragraph()
        if is_part:
            p.paragraph_format.space_before = Pt(8)
            run = p.add_run(label)
            run.bold = True
        else:
            p.paragraph_format.left_indent = Inches(0.2)
            _hyperlink_run(p, label, anchor_name)
        created.append(p._p)

    pb = doc.add_paragraph()
    pb.add_run().add_break(WD_BREAK.PAGE)
    created.append(pb._p)

    for el in created:
        anchor.addnext(el)
        anchor = el


def insert_front_matter(doc):
    remove_old_front(doc)
    anchor = find_first_pagebreak(doc)
    b = bl.Builder(doc)

    h = b.heading("Copyright", 1)
    _bookmark_p(h._p, "Copyright", 3006)
    b.para("Complete Quantum Electrodynamics Course")
    b.para("From mathematical foundations to one-loop QED")
    b.para("First edition, 2026")
    b.para(
        "© 2026 the author. All rights reserved. Independently published. "
        "No ISBN has been assigned to this file. Permission is granted to the purchaser "
        "to print one copy for personal study. Redistribution of the digital file is not granted."
    )
    b.para(
        "Units throughout: ℏ = c = 1, Heaviside–Lorentz, mostly-minus metric g = diag(1, −1, −1, −1). "
        "The electron charge in the vertex is +ieγ^μ as derived in Lesson 44. "
        "α = e²/4π ≈ 1/137.036 at vanishing momentum transfer."
    )
    b.para(
        "This book derives tree-level QED processes, one-loop mass and charge renormalization, "
        "the running of α for one lepton, the Ward identity, infrared cancellation, Dirac g = 2, "
        "Schwinger’s a = α/(2π), the leading Lamb mechanism, the Uehling −27 MHz piece, "
        "and the Schwinger pair-production exponent and prefactor. It does not compute two-loop g−2, "
        "a complete Lamb shift to kHz, α(M_Z) including quarks, weak decays, QCD, or gravity."
    )
    b.pagebreak()

    h2 = b.heading("How to read this book", 1)
    _bookmark_p(h2._p, "HowToRead", 3005)
    b.para(
        "Work with pencil and paper. Attempt each worked example before reading its answer, "
        "and the exercises before the solutions. Solutions sit at the end of the lesson that posed them."
    )
    b.para("Four routes:")
    b.bullet(
        "Prologues 1–9 first, always. Feynman’s easy QED in this course’s words (photons, arrows, all paths, three actions), "
        "Maxwell as the many-photon alternative, bras and kets, the Schrödinger equation, S-parameters as ⟨f|S|i⟩, "
        "and Feynman diagrams with no assumed background. Plan on 30–50 hours. Then Lesson 1."
    )
    b.bullet(
        "Lessons 1–37, the foundation, if complex numbers, Dirac matrices, or canonical quantization are not yet automatic. "
        "Plan on 150–250 hours."
    )
    b.bullet(
        "After Lesson 40, read the Interlude on Mead’s view (A as the phase standard; E and B derived). Do not move it to the front."
    )
    b.bullet(
        "Lessons 38–60, the QED spine, if the foundation is already in hand. Start at Lesson 38. "
        "The last tree-level result is Compton’s (1/4)Σ|ℳ|² = −2e⁴(s/u+u/s) and the conversion to a cross section. "
        "Plan on 80–120 hours."
    )
    b.bullet(
        "Lessons 61–86, one-loop QED and the path-integral language. Do not skip 53–57; later chapters use those amplitudes. "
        "Plan on 80–120 hours. The last derived numbers are a = α/(2π), the Lamb mechanism at ~10³ MHz, "
        "and Γ/V = (eE)²/(4π³) exp(−πm²/eE)."
    )
    b.para(
        "A reader who wants only the Feynman rules and tree processes can stop after Lesson 60. "
        "A reader who wants renormalization can stop after Lesson 69. "
        "Lessons 79–86 re-derive the same rules in the path integral and place QED inside the Standard Model; they are optional for computing a cross section."
    )
    b.para(
        "Do not start this book as a first course in calculus. Do start it as a first course in QED if linear algebra "
        "and ordinary quantum mechanics are willing to be rebuilt rather than assumed."
    )
    b.pagebreak()

    for el in b.elements:
        anchor.addnext(el)
        anchor = el


def link_lesson_mentions(doc):
    """Hyperlink 'Lesson N' only in short, single-run Normal paragraphs (Next-lesson lines)."""
    n = 0
    for p in doc.paragraphs:
        style = p.style.name if p.style is not None else ""
        if style != "Normal":
            continue
        if p._p.findall(qn("w:hyperlink")):
            continue
        runs = p.runs
        if len(runs) != 1:
            continue
        text = p.text
        if "Lesson " not in text or len(text) > 280:
            continue
        matches = list(LESSON_MENTION.finditer(text))
        if not matches:
            continue
        parts = []
        pos = 0
        for m in matches:
            num = int(m.group(1))
            if num < 1 or num > 86:
                continue
            if m.start() > pos:
                parts.append(("t", text[pos:m.start()]))
            parts.append(("h", m.group(0), "Lesson%d" % num))
            pos = m.end()
        if pos < len(text):
            parts.append(("t", text[pos:]))
        if not any(x[0] == "h" for x in parts):
            continue
        r = runs[0]
        r.text = ""
        r._r.getparent().remove(r._r)
        for item in parts:
            if item[0] == "t":
                p.add_run(item[1])
            else:
                _hyperlink_run(p, item[1], item[2])
                n += 1
    return n


def main():
    doc = Document(COMPLETE)
    retitle(doc)
    set_gutter(doc)
    demoted = demote_headings(doc)
    insert_front_matter(doc)
    # demote again in case front matter used H1 correctly (keep those)
    demoted += 0
    n_bm = bookmark_lessons(doc)
    entries = collect_toc_entries(doc)
    insert_static_toc(doc, entries)
    n_links = link_lesson_mentions(doc)
    # Do not ask Word for F9 field updates
    settings = doc.settings.element
    uf = settings.find(qn("w:updateFields"))
    if uf is not None:
        settings.remove(uf)
    last = None
    tmp = COMPLETE + ".tmp.docx"
    for attempt in range(8):
        try:
            doc.save(tmp)
            os.replace(tmp, COMPLETE)
            last = None
            break
        except OSError as e:
            last = e
            time.sleep(2 + attempt)
    if last is not None:
        raise last
    print(
        "finish_book: demoted %d headings, bookmarks %d, TOC %d, links %d"
        % (demoted, n_bm, len(entries), n_links)
    )


if __name__ == "__main__":
    main()
