"""Audit the live docx for Kindle/KDP readiness."""

from __future__ import annotations

import re
import zipfile
from collections import Counter
from pathlib import Path

DOCX = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")


def para_text(p: str) -> str:
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))


def style_of(p: str) -> str:
    m = re.search(r'<w:pStyle w:val="([^"]+)"', p)
    return m.group(1) if m else "Normal"


def main() -> None:
    assert DOCX.exists(), f"missing {DOCX}"
    with zipfile.ZipFile(DOCX) as z:
        print("size_mb", round(DOCX.stat().st_size / 1e6, 2))
        print("testzip", z.testzip())
        names = z.namelist()
        print("parts", [n for n in names if n.startswith("word/") and n.count("/") == 1][:40])
        print("headers", [n for n in names if "header" in n or "footer" in n])
        print("media", [n.split("/")[-1] for n in names if n.startswith("word/media/")])
        xml = z.read("word/document.xml").decode("utf-8")
        styles = z.read("word/styles.xml").decode("utf-8")
        rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
        try:
            settings = z.read("word/settings.xml").decode("utf-8")
        except KeyError:
            settings = ""

    print("\n=== STYLES Heading1 ===")
    m = re.search(r'<w:style w:type="paragraph" w:styleId="Heading1">.*?</w:style>', styles, re.DOTALL)
    print(m.group(0)[:800] if m else "MISSING Heading1")
    print("style_pageBreakBefore", "<w:pageBreakBefore" in (m.group(0) if m else ""))

    paras = re.findall(r"<w:p\b[^>]*>.*?</w:p>", xml, flags=re.DOTALL)
    print("\nparas", len(paras), "words", len(re.findall(r"<w:t[^>]*>([^<]+)</w:t>", xml)))
    styles_c = Counter(style_of(p) for p in paras)
    print("style_counts", styles_c.most_common(15))

    print("\n=== HEADING 1s ===")
    h1s = []
    for i, p in enumerate(paras):
        if style_of(p) == "Heading1":
            t = para_text(p)
            hard = 'w:type="page"' in p
            pbb = "pageBreakBefore" in p
            h1s.append((i, t, hard, pbb))
            print(f"{i:4d} hard={hard} pbb={pbb} {t[:90]}")
    print("h1_count", len(h1s))

    print("\n=== TOC / fields ===")
    print("TOC field", "TOC" in xml)
    print("hyperlink count", xml.count("<w:hyperlink") + xml.count("<w:instrText"))
    print("fldChar", xml.count("fldChar"))

    print("\n=== DRAWINGS ===")
    print("w:drawing", xml.count("<w:drawing"))
    print("anchor (float)", xml.count("<wp:anchor"))
    print("inline", xml.count("<wp:inline"))
    wraps = re.findall(r"<wp:wrap\w+", xml)
    print("wraps", Counter(wraps))
    extents = re.findall(r'<wp:extent cx="(\d+)" cy="(\d+)"', xml)
    print("extents", len(extents))
    for cx, cy in extents:
        print("  ", int(cx), "x", int(cy), "in", round(int(cx) / 914400, 2), "x", round(int(cy) / 914400, 2))

    print("\n=== KINDLE HAZARDS ===")
    print("textbox", "w:txbxContent" in xml or "v:textbox" in xml)
    print("smartart", "dgm:" in xml)
    print("w:sectPr count", xml.count("<w:sectPr"))
    print("lastRenderedPageBreak", xml.count("lastRenderedPageBreak"))
    print("Amazon Ember", "Amazon Ember" in xml)
    print("trackRevisions", "trackRevisions" in settings or "w:trackRevisions" in xml)
    print("comments", "word/comments.xml" in names)
    print("first para", para_text(paras[0])[:80] if paras else "")
    print("first style", style_of(paras[0]) if paras else "")
    print("page br total", xml.count('w:type="page"'))
    print("rels images", len(re.findall(r'Target="media/', rels)))

    # first heading should not force a blank opening page if it's the title
    if h1s:
        print("first h1 index", h1s[0][0], h1s[0][1][:60])


if __name__ == "__main__":
    main()
