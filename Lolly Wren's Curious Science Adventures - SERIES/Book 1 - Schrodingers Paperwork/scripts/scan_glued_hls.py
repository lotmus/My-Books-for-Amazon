# -*- coding: utf-8 -*-
from pathlib import Path
from lxml import etree
import zipfile
import re

LIVE = Path(
    r"D:\My Books for Amazon"
    r"\Lolly Wren's Curious Science Adventures - SERIES"
    r"\Book 1 - Schrodingers Paperwork"
    r"\Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx"
)
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

with zipfile.ZipFile(LIVE) as z:
    root = etree.fromstring(z.read("word/document.xml"))

print("=== mid-word / missing-space hyperlink wraps ===")
for i, p in enumerate(root.findall(f".//{W}p")):
    # sequential text nodes with parent info
    nodes = []
    for el in p.iter():
        if el.tag == f"{W}t":
            nodes.append(el)
    full = "".join(t.text or "" for t in nodes)
    for h in p.findall(f"{W}hyperlink"):
        vis = "".join(t.text or "" for t in h.findall(f".//{W}t"))
        if not vis:
            continue
        # previous tail: text before this hyperlink in paragraph
        # get first w:t in hyperlink
        first = h.find(f".//{W}t")
        last = h.findall(f".//{W}t")[-1]
        # preceding sibling text
        prev = h.getprevious()
        prev_txt = ""
        if prev is not None:
            prev_txt = "".join(t.text or "" for t in prev.findall(f".//{W}t")) if prev.tag != f"{W}t" else (prev.text or "")
            if prev.tag == f"{W}r":
                prev_txt = "".join(t.text or "" for t in prev.findall(f"{W}t"))
        nxt = h.getnext()
        next_txt = ""
        if nxt is not None and nxt.tag == f"{W}r":
            next_txt = "".join(t.text or "" for t in nxt.findall(f"{W}t"))
        joined_prev = (prev_txt[-1:] if prev_txt else "") + vis[:1]
        joined_next = vis[-1:] + (next_txt[:1] if next_txt else "")
        bad = False
        reasons = []
        if prev_txt and prev_txt[-1].isalpha() and vis[0].isalpha():
            bad = True
            reasons.append("glued-to-prev")
        if next_txt and vis[-1].isalpha() and next_txt[0].isalpha():
            bad = True
            reasons.append("glued-to-next")
        if vis[0].islower() and vis.split()[0] not in (
            "the", "a", "an", "of", "and", "or", "to", "in", "on", "for", "with",
            "you", "it", "is", "as", "my", "no"
        ) and len(vis.split()[0]) < 8 and vis[0] != vis[0].upper():
            # short lowercase start might be a fragment
            if vis[0] in "staeiou" and not vis.startswith((
                "the ", "a ", "an ", "einselection", "decoherence", "entanglement",
                "superposition", "negentropic", "error-correcting", "counted",
                "evaporate", "only ", "you cannot", "an inequality", "pilot"
            )):
                pass
        if bad:
            print(f"p{i} vis={vis!r} prev_end={prev_txt[-20:]!r} next_start={next_txt[:20]!r} {reasons}")
            print(f"   full={full[:140]!r}")
