# -*- coding: utf-8 -*-
"""Splice the classical-optics interlude in after Lesson 8, before Part II.

Builds "Interlude Classical Optics.docx" next to the Complete file, replaces
(or first inserts) the "Interlude Classical Optics" section of the Complete
file, and adds its entries to the static Table of Contents and to the reading
routes of "How to read this book". Safe to re-run.
"""
import copy
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lesson as bl
import _insert_opening as io
from docx import Document
from docx.oxml.ns import qn

HEADING = "Interlude Classical Optics"
ANCHOR, BID = "Optics", 4011
ROUTE = ("After Lesson 8, read the Interlude on classical optics (Maxwell\u2019s waves in matter; "
         "Prologue 2\u2019s 0.2 arrow derived). Skim it if undergraduate optics is familiar.")


def _text(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


def _replace_text(p, text):
    ts = list(p.iter(qn("w:t")))
    ts[0].text = text
    for t in ts[1:]:
        t.text = ""


def main():
    src = os.path.join(HERE, "interlude_optics.txt")
    meta, blocks = bl.parse(src)
    out = os.path.join(bl.ROOT, HEADING + ".docx")
    io.build_standalone_kind(meta, blocks, "Interlude", out)
    print("standalone", os.path.basename(out), "blocks", len(blocks))

    doc = Document(bl.COMPLETE)
    body = doc.element.body
    n_old = io.remove_range_before(body, lambda t: t.startswith(HEADING),
                                   lambda t: t.startswith("Part II "))
    print("removed old optics paras", n_old)
    part2, t2 = io.find_h1(body, lambda t: t.startswith("Part II "))
    if part2 is None:
        raise RuntimeError("Part II heading not found")
    b = bl.Builder(doc)
    io.render_section(b, HEADING, blocks, meta.get("NEXT"), bookmark=ANCHOR, bid=BID)
    io.insert_elements_before(part2, b.elements)
    print("inserted optics interlude before", t2)

    # static TOC: an entry after Lesson 8, modelled on the Mead entry
    links = [h for h in body.iter(qn("w:hyperlink"))]
    if not any(h.get(qn("w:anchor")) == ANCHOR for h in links):
        mead = next(h for h in links if h.get(qn("w:anchor")) == "Mead").getparent()
        l8 = next(h for h in links if h.get(qn("w:anchor")) == "Lesson8").getparent()
        entry = copy.deepcopy(mead)
        entry.find(qn("w:hyperlink")).set(qn("w:anchor"), ANCHOR)
        _replace_text(entry, HEADING)
        l8.addnext(entry)
        print("TOC entry added")
    # reading route in "How to read this book", before the Mead route
    paras = [p for p in body.iter(qn("w:p"))]
    if not any(_text(p) == ROUTE for p in paras):
        mead_route = next(p for p in paras if _text(p).startswith("After Lesson 40, read the Interlude"))
        route = copy.deepcopy(mead_route)
        _replace_text(route, ROUTE)
        mead_route.addprevious(route)
        print("reading route added")
    io.save_complete(doc)
    print("complete saved")


if __name__ == "__main__":
    main()
