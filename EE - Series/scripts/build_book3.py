# -*- coding: utf-8 -*-
"""Rebuild EE Book 3 (Semiconductor Physics and Devices) from its full chapter sources (2026-10-01).

Sources: chapters/Book3/front.txt (HOW, CONST, HANDOFF, SRC lines; "SRC: ## x" = sub-heading)
and chapters/Book3/src/chNN.txt with tags PART, H1, H2, P, EQ (centered), KEY, PR (numbered
practice problem), ANS (answer, collected into Appendix B). Paragraph formatting is cloned from
chapters/Book3/template_book3.docx; its first five paragraphs (title block) are kept.
Usage: python build_book3.py <bookdir> <out.docx>     (DOCX only)
"""
import copy, re, sys
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def lines(path):
    out = []
    for ln in Path(path).read_text(encoding="utf-8").splitlines():
        if ln.strip():
            t, _, b = ln.partition(":"); out.append((t.strip(), b.strip()))
    return out

def make_p(tpl, text):
    p = copy.deepcopy(tpl)
    for c in list(p):
        if c.tag != qn("w:pPr"):
            p.remove(c)
    for a in list(p.attrib):
        if a.endswith("paraId") or a.endswith("textId"):
            del p.attrib[a]
    r0 = next((r for r in tpl.findall(qn("w:r")) if r.find(qn("w:t")) is not None), None)
    r = OxmlElement("w:r")
    if r0 is not None and r0.find(qn("w:rPr")) is not None:
        r.append(copy.deepcopy(r0.find(qn("w:rPr"))))
    t = OxmlElement("w:t"); t.set(qn("xml:space"), "preserve"); t.text = text
    r.append(t); p.append(r)
    return p

def main(bookdir, outp):
    bd = Path(bookdir)
    doc = Document(str(bd / "template_book3.docx"))
    P = doc.paragraphs
    st = lambda p: p.style.name if p.style is not None else ""
    T = {
        "H1": next(p for p in P if st(p) == "Heading 1" and not p.text.startswith("Part "))._p,
        "PART": next(p for p in P if st(p) == "Heading 1" and p.text.startswith("Part "))._p,
        "H2": next(p for p in P if st(p) == "Heading 2")._p,
        "EQ": next(p for i, p in enumerate(P) if i > 5 and st(p) == "Normal" and p.alignment is not None)._p,
        "P": next(p for i, p in enumerate(P) if i > 5 and st(p) == "Normal" and p.alignment is None and p.text)._p,
    }
    T = {k: copy.deepcopy(v) for k, v in T.items()}
    body = doc.element.body
    keep = [p._p for p in P[:5]]
    for el in list(body):
        if el.tag == qn("w:sectPr") or any(el is k for k in keep):
            continue
        body.remove(el)
    sect = body.find(qn("w:sectPr"))
    def add(tag, text):
        el = make_p(T[tag], text)
        if sect is not None: sect.addprevious(el)
        else: body.append(el)
    F = {}
    for t, b in lines(bd / "front.txt"):
        F.setdefault(t, []).append(b)
    chapters = sorted(bd.glob("src/ch*.txt"))
    APPS = ["Appendix A. Constants Used in This Book", "Appendix B. Answers to the Practice Problems",
            "Appendix C. Where This Book Hands Off", "Appendix D. Sources and Further Reading"]
    add("H1", "How to Use This Book")
    for h in F["HOW"]: add("P", h)
    add("H1", "Contents")
    for c in chapters:
        for t, b in lines(c):
            if t in ("PART", "H1"): add("P", b)
    for a in APPS: add("P", a)
    answers = []
    for c in chapters:
        items = lines(c); prn = 0; ans = []
        for t, b in items:
            if t in ("PART", "H1", "H2", "P", "EQ"): add(t, b)
            elif t == "KEY":
                assert b.startswith("Key idea."), c; add("P", b)
            elif t == "PR":
                prn += 1; add("P", f"{prn}. {b}")
            elif t == "ANS": ans.append(b)
            else: raise ValueError(f"{c.name}: unknown tag {t}")
        assert prn == len(ans), (c.name, prn, len(ans))
        num = re.match(r"Chapter (\d+)", next(b for t, b in items if t == "H1")).group(1)
        answers.append((num, ans))
    add("H1", APPS[0])
    for x in F["CONST"]: add("P", x)
    add("H1", APPS[1])
    for num, ans in answers:
        add("H2", f"Chapter {num}")
        for k, a in enumerate(ans, 1): add("P", f"{k}. {a}")
    add("H1", APPS[2])
    for x in F["HANDOFF"]: add("P", x)
    add("H1", APPS[3])
    for x in F["SRC"]:
        if x.startswith("## "): add("H2", x[3:])
        else: add("P", x)
    doc.core_properties.title = "Semiconductor Physics and Devices"
    doc.core_properties.author = "Lothar J. Musiol"
    doc.save(outp)
    print("saved", outp, len(chapters), "chapters")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
