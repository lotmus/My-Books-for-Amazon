# -*- coding: utf-8 -*-
"""Splice Prologues 1–9 before Lesson 1 and the Mead interlude after Lesson 40."""
import glob
import os
import sys
import time

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lesson as bl

COMPLETE = bl.COMPLETE
ROOT = bl.ROOT


def save_complete(doc):
    tmp = COMPLETE + ".tmp.docx"
    last = None
    for attempt in range(8):
        try:
            doc.save(tmp)
            os.replace(tmp, COMPLETE)
            return
        except OSError as e:
            last = e
            time.sleep(2 + attempt)
    if last is not None:
        raise last


def find_h1(body, predicate):
    for child in body:
        text = bl.heading1_text(child)
        if text and predicate(text):
            return child, text
    return None, None


def remove_range_before(body, start_pred, end_pred):
    start, _ = find_h1(body, start_pred)
    end, _ = find_h1(body, end_pred)
    if start is None or end is None:
        return 0
    n = 0
    node = start
    while node is not None and node is not end:
        nxt = node.getnext()
        body.remove(node)
        n += 1
        node = nxt
    return n


def render_section(b, heading, blocks, next_text, bookmark=None, bid=None):
    title_p = b.heading(heading, 1)
    if bookmark:
        bl._bookmark_paragraph(title_p, bookmark, bid)
    b.render(blocks)
    if next_text:
        b.heading("Next lesson", 2)
        b.para(next_text)
    b.pagebreak()


def insert_elements_before(end, elements):
    for el in elements:
        end.addprevious(el)


def build_standalone_kind(meta, blocks, kind, out_path):
    doc = Document(bl.TEMPLATE)
    body = doc.element.body
    for child in list(body):
        if child.tag != qn("w:sectPr"):
            body.remove(child)
    hdr = doc.sections[0].header
    for p in hdr.paragraphs:
        if "QED Course" in p.text:
            for r in p.runs[1:]:
                r.text = ""
            p.runs[0].text = "QED Course   %s %s" % (kind, meta["NUM"])
    b = bl.Builder(doc)
    p = b.para(meta["TITLE"], style="Title")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = b.para("%s %s of the Complete Quantum Electrodynamics Course" % (kind, meta["NUM"]), style="Subtitle")
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
    p = b.para("First edition, 2026")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    b.pagebreak()
    b.render(blocks)
    if meta.get("NEXT"):
        b.heading("Next lesson", 2)
        b.para(meta["NEXT"])
    last = None
    tmp = out_path + ".tmp.docx"
    for attempt in range(8):
        try:
            doc.save(tmp)
            os.replace(tmp, out_path)
            last = None
            break
        except OSError as e:
            last = e
            time.sleep(2 + attempt)
    if last is not None:
        raise last


def main():
    prologues = []
    for n in range(1, 10):
        path = os.path.join(HERE, "prologue%02d.txt" % n)
        meta, blocks = bl.parse(path)
        prologues.append((meta, blocks, path))
        out = os.path.join(ROOT, "Prologue %02d %s.docx" % (int(meta["NUM"]), meta["TITLE"]))
        build_standalone_kind(meta, blocks, "Prologue", out)
        print("standalone", os.path.basename(out), "blocks", len(blocks))

    mead_path = os.path.join(HERE, "interlude_mead.txt")
    mead_meta, mead_blocks = bl.parse(mead_path)
    mead_out = os.path.join(ROOT, "Interlude Mead's View.docx")
    build_standalone_kind(mead_meta, mead_blocks, "Interlude", mead_out)
    print("standalone", os.path.basename(mead_out), "blocks", len(mead_blocks))

    doc = Document(COMPLETE)
    body = doc.element.body

    n_old = remove_range_before(
        body,
        lambda t: t.startswith("Part 0") or t.startswith("Prologue 1"),
        lambda t: t.startswith("Lesson 1 "),
    )
    print("removed opening paras", n_old)

    lesson1, t1 = find_h1(body, lambda t: t.startswith("Lesson 1 "))
    if lesson1 is None:
        raise RuntimeError("Lesson 1 heading not found")

    # Drop a leftover Part I immediately before Lesson 1 if we will keep existing parts.
    b = bl.Builder(doc)
    render_section(
        b,
        "Part 0 Light, arrows, and the S-matrix",
        [("para",
          "Start here. Prologues 1–4 are Feynman's easy QED in this course's words: photons, probability arrows, "
          "all paths, and the three actions. Prologue 5 is Maxwell as the many-photon alternative. "
          "Prologues 6–9 name bras and kets, the Schrödinger equation, S-parameters as ⟨f|S|i⟩, and Feynman diagrams "
          "slowly enough for a first reading. Then Lesson 1 begins the algebra. Mead's view waits until after Lesson 40.")],
        None,
        bookmark="Part0",
        bid=2000,
    )
    for meta, blocks, _path in prologues:
        num = int(meta["NUM"])
        render_section(
            b,
            "Prologue %d %s" % (num, meta["TITLE"]),
            blocks,
            meta.get("NEXT"),
            bookmark="Prologue%d" % num,
            bid=4000 + num,
        )
    insert_elements_before(lesson1, b.elements)
    print("inserted Part 0 + Prologues 1–9 before", t1)

    n_old_mead = remove_range_before(
        body,
        lambda t: t.startswith("Interlude Mead"),
        lambda t: t.startswith("Lesson 41 "),
    )
    print("removed old Mead paras", n_old_mead)

    lesson41, t41 = find_h1(body, lambda t: t.startswith("Lesson 41 "))
    if lesson41 is None:
        raise RuntimeError("Lesson 41 heading not found")

    b2 = bl.Builder(doc)
    render_section(
        b2,
        "Interlude Mead's View",
        mead_blocks,
        mead_meta.get("NEXT"),
        bookmark="Mead",
        bid=4010,
    )
    insert_elements_before(lesson41, b2.elements)
    print("inserted Mead interlude before", t41)

    save_complete(doc)
    print("complete saved")


if __name__ == "__main__":
    main()
