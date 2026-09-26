"""Insert (or refresh) a real Word Table of Contents field into
Complete QED Course.docx, right after the title page.

The TOC is a live Word field (TOC \\o "1-3" \\h \\z \\u) built from the
Heading 1-3 styles already used throughout the document. \\h makes every
entry a clickable hyperlink that jumps to the heading. Word populates the
page numbers itself; this script also sets updateFields so Word refreshes
the field automatically when the file is opened (no manual F9 needed,
though F9 / right-click > Update Field still works after edits).

Idempotent: re-running replaces the previously inserted TOC block instead
of stacking a second copy. The block is bookmarked "QEDCourseTOC" so it can
be found again. To remove the TOC entirely later, delete everything between
the "How to use this lesson" heading and the "Lesson 1" heading in Word, or
just select the TOC field and press Delete.

Usage:  python insert_toc.py
"""
import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
COMPLETE = os.path.join(ROOT, "Complete QED Course.docx")
BOOKMARK = "QEDCourseTOC"


def _run_field(paragraph, instr_text):
    """Append a TOC field (begin/instrText/separate/placeholder/end) to paragraph."""
    def el(tag):
        return OxmlElement(tag)

    r1 = paragraph.add_run()
    fld_begin = el("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    fld_begin.set(qn("w:dirty"), "true")
    r1._r.append(fld_begin)

    r2 = paragraph.add_run()
    instr = el("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instr_text
    r2._r.append(instr)

    r3 = paragraph.add_run()
    fld_sep = el("w:fldChar")
    fld_sep.set(qn("w:fldCharType"), "separate")
    r3._r.append(fld_sep)

    r4 = paragraph.add_run("Right-click and choose Update Field (or press F9) to build the table of contents.")
    r4.italic = True

    r5 = paragraph.add_run()
    fld_end = el("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    r5._r.append(fld_end)


def _bookmark_start(paragraph, name, bid):
    b = OxmlElement("w:bookmarkStart")
    b.set(qn("w:id"), str(bid))
    b.set(qn("w:name"), name)
    paragraph._p.insert(0, b)


def _bookmark_end(paragraph, bid):
    b = OxmlElement("w:bookmarkEnd")
    b.set(qn("w:id"), str(bid))
    paragraph._p.append(b)


def remove_existing_toc(doc):
    body = doc.element.body
    in_block = False
    to_remove = []
    for child in list(body):
        if child.tag == qn("w:p"):
            starts = child.findall(qn("w:bookmarkStart"))
            ends = child.findall(qn("w:bookmarkEnd"))
            if any(s.get(qn("w:name")) == BOOKMARK for s in starts):
                in_block = True
            if in_block:
                to_remove.append(child)
            if any(True for _ in ends) and in_block:
                # bookmarkEnd doesn't carry the name, so we stop after the
                # paragraph following bookmarkStart's matching end marker
                # (handled by the explicit end-marker paragraph below)
                pass
        if in_block and child.tag == qn("w:p"):
            texts = "".join(t.text or "" for t in child.iter(qn("w:t")))
            if texts == "__QEDCourseTOC_END__":
                break
    for node in to_remove:
        node.getparent().remove(node)


def find_title_page_break(doc):
    """Return the w:p element containing the first page break (end of title page)."""
    body = doc.element.body
    for child in body:
        if child.tag == qn("w:p"):
            for br in child.iter(qn("w:br")):
                if br.get(qn("w:type")) == "page":
                    return child
    raise RuntimeError("Could not find the title-page break")


def main():
    doc = Document(COMPLETE)
    remove_existing_toc(doc)
    anchor = find_title_page_break(doc)

    heading = doc.add_paragraph("Table of Contents", style="Heading 1")
    _bookmark_start(heading, BOOKMARK, 9001)

    field_p = doc.add_paragraph()
    _run_field(field_p, 'TOC \\o "1-3" \\h \\z \\u')

    end_marker = doc.add_paragraph("__QEDCourseTOC_END__")
    end_marker.runs[0].font.size = None
    end_marker.runs[0].font.hidden = True
    _bookmark_end(end_marker, 9001)

    pb = doc.add_paragraph()
    pb.add_run().add_break(WD_BREAK.PAGE)

    # Move the three new paragraphs to just after the title page break.
    for p in (heading._p, field_p._p, end_marker._p, pb._p):
        anchor.addnext(p)
        anchor = p

    # Ask Word to refresh fields automatically when the file is opened.
    settings = doc.settings.element
    uf = settings.find(qn("w:updateFields"))
    if uf is None:
        uf = OxmlElement("w:updateFields")
        settings.append(uf)
    uf.set(qn("w:val"), "true")

    doc.save(COMPLETE)
    print("Inserted/refreshed Word TOC (Heading 1-3, hyperlinked) in", os.path.basename(COMPLETE))


if __name__ == "__main__":
    main()
