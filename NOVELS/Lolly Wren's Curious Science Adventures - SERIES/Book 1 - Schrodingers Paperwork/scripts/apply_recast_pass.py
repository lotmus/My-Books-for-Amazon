# -*- coding: utf-8 -*-
"""Recast-not-cut pass on the live Kindle manuscript."""
from __future__ import annotations

import shutil
from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

SERIES = Path(
    r"D:\My Books for Amazon"
    r"\Lolly Wren's Curious Science Adventures - SERIES"
    r"\Book 1 - Schrodingers Paperwork"
)
LIVE = SERIES / "Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx"
SCRATCH = Path(
    r"D:\My Books for Amazon"
    r"\Lolly Wren's Curious Science Adventures - SERIES"
    r"\Book 1 - Schrodingers Paperwork\bak\_repo_import\_gh_latest"
    r"\Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.scratch.docx"
)
OUT = SERIES / "bak" / "Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx.next"
GUIDE = SERIES / "notes" / "MANUSCRIPT_GUIDE.md"
WS = Path(
    r"D:\My Books for Amazon"
    r"\Schrodingers_Paperwork"
    r"\Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx"
)

LDQ = "\u201c"
RDQ = "\u201d"
LSQ = "\u2018"
RSQ = "\u2019"
EM = "\u2014"
EN = "\u2013"


def set_text(p, new: str) -> None:
    runs = p.runs
    if not runs:
        p.add_run(new)
        return
    runs[0].text = new
    for r in runs[1:]:
        r.text = ""
    # leftover hyperlink text nodes
    for t in p._p.findall(".//" + qn("w:t")):
        if t.text and t.text not in new and "".join(x.text or "" for x in p._p.findall(".//" + qn("w:t"))) != new:
            pass
    # If hyperlink remnants still pollute .text, force via first w:t only after wipe
    texts = p._p.findall(".//" + qn("w:t"))
    joined = "".join(t.text or "" for t in texts)
    if joined != new:
        for i, t in enumerate(texts):
            t.text = new if i == 0 else ""


def replace_once(p, old: str, new: str) -> bool:
    full = p.text
    if old not in full:
        return False
    for r in p.runs:
        if old in (r.text or ""):
            r.text = (r.text or "").replace(old, new, 1)
            return True
    set_text(p, full.replace(old, new, 1))
    return True


def insert_after(paragraph, text: str) -> Paragraph:
    new_el = deepcopy(paragraph._p)
    for child in list(new_el):
        if child.tag != qn("w:pPr"):
            new_el.remove(child)
    paragraph._p.addnext(new_el)
    new_p = Paragraph(new_el, paragraph._parent)
    run = new_p.add_run(text)
    if paragraph.runs:
        src = paragraph.runs[0]
        if src.font.name:
            run.font.name = src.font.name
        if src.font.size:
            run.font.size = src.font.size
    return new_p


def delete_p(p) -> None:
    el = p._element
    parent = el.getparent()
    if parent is not None:
        parent.remove(el)


def must(cond, msg):
    if not cond:
        raise SystemExit(msg)


def main() -> None:
    if not LIVE.exists():
        raise SystemExit(f"missing {LIVE}")
    shutil.copy2(LIVE, SCRATCH)
    doc = Document(str(SCRATCH))
    paras = doc.paragraphs
    n0 = len(paras)
    log = []

    def P(i):
        return doc.paragraphs[i]

    # --- in-place replacements (indices stable) ---
    must("18 lectures in four parts" in P(84).text, "p84 four parts")
    set_text(
        P(84),
        "The lectures live together in the Appendix as a real class, 18 lectures in five parts, one per chapter.",
    )
    log.append("p84 four parts -> five parts")

    must(P(87).text.startswith("In one breath"), "p87 layout")
    set_text(P(87), "You need first: what this lecture assumes, named in one line.")
    set_text(P(88), "When you walk out, you should be able to: the skill the lecture is for.")
    set_text(P(89), "Start here: an everyday analogy, no jargon.")
    set_text(P(90), "The idea, step by step: the argument assembled in order.")
    set_text(P(91), "In one breath: the whole idea in a sentence or two.")
    set_text(P(92), "What this chapter was actually showing you: the story and the science locked together.")
    set_text(P(93), "Where the popular version goes wrong: the misconception you have probably been taught, corrected.")
    set_text(P(94), "Going deeper: the real machinery, the equations, the named experiments. Explicitly skippable.")
    log.append("p87-94 How to Read layout order matched to lectures")

    must("Physics Notes" in P(110).text, "p110 Physics Notes")
    replace_once(P(110), "Physics Notes", "Physics Prologue")
    log.append("p110 Physics Notes -> Physics Prologue")

    must("whose number matches the chapter" in P(111).text, "p111 companion")
    set_text(
        P(111),
        "Demos exist for Lectures 1, 2, 4 and 13. The others are lectures on purpose. "
        "If a demonstration is mentioned in a lecture"
        + RSQ
        + "s Going-deeper block, the companion page is the one whose number matches that lecture. Lecture 1"
        + RSQ
        + "s superposition toy is not a plot device. It is the thing Lolly wrote in pencil and then covered with her hand.",
    )
    log.append("p111 companion honesty")

    must("If a demo is down" in P(112).text, "p112 demos")
    replace_once(
        P(112),
        "If a demo is down, the lecture still stands. The universe is not hosted on GitHub.",
        "If a demo is down, the lecture still stands. The universe is not hosted on GitHub. "
        "The remaining lectures have no toy on purpose: they are the class, not the arcade.",
    )
    log.append("p112 remaining lectures are lectures")

    must("The ones from yesterday" in P(1025).text, "p1025 yesterday")
    replace_once(P(1025), "The ones from yesterday.", "The ones from this morning.")
    log.append("p1025 yesterday -> this morning")

    must("and I don" in P(1247).text and "Downstairs" in P(1247).text, "p1247 downstairs")
    set_text(
        P(1247),
        LDQ
        + "Downstairs,"
        + RDQ
        + " Lolly replied. "
        + LDQ
        + "Gideon found something odd about the second page of 11-C this morning, and I don"
        + RSQ
        + "t think anyone"
        + RSQ
        + "s asked him about it since."
        + RDQ,
    )
    log.append("p1247 kept (insert follows)")

    must("The complaint came in from Outer Fenwick" in P(1251).text, "p1251 Fenwick")
    set_text(
        P(1251),
        "She did go downstairs. Gideon would not show her the page until morning: different folder, different year, and he wanted the ledgers finished first. "
        "By half past seven the moon complaint had arrived from Outer Fenwick, and the second page had to wait. "
        "Outer Fenwick did not officially exist until the moon came up, and the moon did not officially come up until enough people had filled in the form saying they had seen it.",
    )
    log.append("p1251 downstairs-to-moon bridge")

    must("Monday week. Nine days." in P(1320).text, "p1320 memo")
    set_text(
        P(1320),
        "The covering memorandum gave a start date. Monday week. Nine days. "
        "It was a memo date. Reality, Lolly was beginning to notice, did not wait for memo dates.",
    )
    log.append("p1320 memo vs reality")

    must("nine days early" in P(1431).text, "p1431 live early")
    set_text(
        P(1431),
        "Phase Two went live at seven the next morning in four sub-districts"
        + EM
        + "nine days ahead of the memo, and nowhere near the whole country Beatrix had been warned about"
        + EM
        + "because Vale had been suspended at midnight and the Board had discovered, on reading his file, that they preferred the version of him that had signed things.",
    )
    log.append("p1431 nine days ahead of the memo")

    must("unlikely to be relevant" in P(1435).text, "p1435 Croydon")
    replace_once(
        P(1435),
        "Jago had gone to Croydon on an errand unlikely to be relevant.",
        "Jago had gone to Croydon for a car battery and a van that, on paper, was still in bonded storage "
        + EM
        + " an errand that would matter when the Bell rack needed a heartbeat that was not the Ministry"
        + RSQ
        + "s.",
    )
    log.append("p1435 Croydon errand employed")

    must("four hundred and eleven P-9" in P(1790).text, "p1790 411")
    # insert after, not replace
    must("Twenty-Two Elm Grove" in P(1909).text, "p1909 Elm Grove")
    replace_once(P(1909), "Twenty-Two Elm Grove", "Twenty-Two Coldharrow Rise")
    log.append("p1909 photograph address = Coldharrow Rise")

    must("Three weeks after the incident" in P(1971).text, "p1971 incident")
    replace_once(P(1971), "Three weeks after the incident,", "Three weeks after the coupling was cut,")
    log.append("p1971 dated epilogue opener")

    must("reference number stamped on Heisenburger" in P(1989).text, "p1989 137")
    set_text(
        P(1989),
        "When the acknowledgment came back, the reference number stamped on Heisenburger"
        + RSQ
        + "s two lines was 137. Lolly recognised the number from a hospital door, not from Pauli, and did not say so. "
        "He wrote to ask whether this meant anything, was told it did not, and wrote again the following week, to be sure.",
    )
    log.append("p1989 Room 137 employed")

    must("checked the box marked CONTINUE" in P(2000).text, "p2000 CONTINUE")
    replace_once(
        P(2000),
        "by a clerk who had long since stopped reading the file and simply checked the box marked CONTINUE",
        "by a clerk who still would not give his name, who still would not confirm that any meeting had taken place, and who simply checked the box marked CONTINUE",
    )
    log.append("p2000 Form 6/G clerk")

    must("Priddy" in P(2002).text and "incident" in P(2002).text, "p2002 incident file")
    replace_once(P(2002), "file on the incident remained", "file on the coupling cut remained")
    log.append("p2002 Priddy file dated")

    must("Principal Officer, Relational Integrity" in P(2003).text, "p2003 post")
    # insert after

    must("Lessons 1" in P(2350).text and "5" in P(2350).text, "p2350 L6 prereq")
    set_text(P(2350), "You need first: Lessons 1 and 5. Lesson 3 if you want records.")
    log.append("p2350 Lesson 6 prereq")

    must("Lessons 1" in P(2721).text, "p2721 L15 prereq")
    set_text(
        P(2721),
        "You need first: Lessons 8 and 14b. Lessons 12"
        + EN
        + "13 if you care why the plan did not pick a church.",
    )
    log.append("p2721 Lesson 15 prereq")

    must("Fainrose" in P(2736).text and "Bell run" in P(2736).text, "p2736 story lock")
    set_text(
        P(2736),
        "What this chapter was actually showing you. The first Bell run measured the Ministry"
        + RSQ
        + "s clock. The Sunday number did not. Lolly"
        + RSQ
        + "s plan used all four interpretations as a repair manual, not a religion; Mrs Chain was refused a comforting percentage. Recoverable is not unharmed. The scanners were still on.",
    )
    log.append("p2736 Lesson 15 story lock slimmed")

    must("Here ρ and σ" in P(2742).text or "Here" in P(2742).text, "p2742 fidelity")
    if "Mrs Chain" not in P(2742).text:
        set_text(
            P(2742),
            P(2742).text.rstrip()
            + " This graded score is not Mrs Chain"
            + RSQ
            + "s seventy-eight per cent: a code threshold is a repair limit, not a person rendered as a fraction.",
        )
        log.append("p2742 fidelity vs 78%")

    must("Lessons 8 and 16" in P(2794).text, "p2794 L17 prereq")
    set_text(P(2794), "You need first: Lesson 16; Lesson 15 if you have it.")
    log.append("p2794 Lesson 17 prereq")

    must("Noticing, professionally" in P(2806).text, "p2806 job title")
    set_text(
        P(2806),
        "What this chapter was actually showing you. Lolly delivers Mrs Chain a figure"
        + EM
        + "seventy-eight per cent of her sister, as much of the pattern as survived the listening"
        + EM
        + "and Mrs Chain names it correctly: a very good obituary, not a resurrection. "
        "What can be honestly said about a recovered life is the pattern that still holds, not a forged completeness; "
        "a certificate of perfection would conceal the exported cost, where an itemised gap keeps the ledger readable. "
        "The photograph a burglar has the decency to return is worth more than a government signature because it is a remaining correlation, not a claimed whole.",
    )
    log.append("p2806 job title moved out of Lesson 17")

    must("Lessons 11 and 16" in P(2830).text, "p2830 L18 prereq")
    set_text(P(2830), "You need first: Lessons 6, 16" + EN + "17; Lesson 11 for the cat.")
    log.append("p2830 Lesson 18 prereq")

    must("wooden box is empty" in P(2843).text, "p2843 L18 lock")
    set_text(
        P(2843),
        "What this chapter was actually showing you. The scene has already done the box and the lid. "
        "What remains for the class is the timescale: the 308 recovered items were pending, not memories, and they are still not finished. "
        "Noticing is what remains worth doing in the middle.",
    )
    log.append("p2843 Lesson 18 story lock slimmed")

    must("Curious Science Adventures, a series" in P(3162).text, "p3162 series")
    set_text(
        P(3162),
        "Schrödinger"
        + RSQ
        + "s Paperwork is Book 1 of Lolly Wren"
        + RSQ
        + "s Curious Science Adventures: adult satirical science fiction in which large institutions attempt to administer physics, and physics declines to cooperate.",
    )
    log.append("p3162 series line adult")

    must("next Lolly Wren adventure" in P(3165).text, "p3165 adventure")
    replace_once(P(3165), "next Lolly Wren adventure", "next Lolly Wren novel")
    log.append("p3165 adventure -> novel")

    # --- insertions, high index to low ---
    insert_after(
        P(2006),
        "Gideon, who had been standing in the doorway with the usual half-inch to spare, said nothing about private habits, and she filed that, too.",
    )
    log.append("insert after p2006 Gideon/Lolly ethic")

    insert_after(
        P(2003),
        "The desk, when she found it, was at the Institute for Unhelpful Clarity: Fainrose"
        + RSQ
        + "s house, one extra chair, the noticing budget moved somewhere a Ministry cubicle could not reach.",
    )
    log.append("insert after p2003 Institute desk")

    insert_after(
        P(1867),
        "A Deputy Under-Secretary"
        + RSQ
        + "s recollection of his mother was on one of the two lists. Nobody in Certification was permitted to say which.",
    )
    log.append("insert after p1867 mother-form cost")

    insert_after(
        P(1790),
        LDQ
        + "It was ninety-one the morning the Inquiry sat,"
        + RDQ
        + " Beatrix said, still not looking up. "
        + LDQ
        + "The log climbed while we argued about what the number meant."
        + RDQ,
    )
    log.append("insert after p1790 91 to 411")

    insert_after(
        P(1774),
        "Nine thousand houses, four sub-districts, and a Ministry that needed it to be a country so the liability would belong to everybody. Beatrix filed the mismatch without comment. The evidence she could swear to did not require a tour of Britain.",
    )
    log.append("insert after p1774 national vs local")

    insert_after(
        P(1063),
        LDQ
        + "That"
        + RSQ
        + "s the hours-clock paused, not cancelled,"
        + RDQ
        + " Fainrose said, without looking up. "
        + LDQ
        + "It was a feed-rate clock. Cut the feed, the hours stop counting. The hole is still evaporating. Just not on the timetable I gave you over tea."
        + RDQ,
    )
    log.append("insert after p1063 feed-rate clock named")

    insert_after(
        P(126),
        "Nelson"
        + EM
        + "Mr Pilbeam"
        + RSQ
        + "s terrier. Not permitted in the building. Attends anyway. Achieves, on balance, more clarity per sitting than the Board itself.",
    )
    log.append("insert Cast Nelson")

    insert_after(
        P(125),
        "Miss Dorothy Kell"
        + EM
        + "wrote to the inquiry every week after the freeze. Her brother"
        + RSQ
        + "s apprenticeship is among the unrecovered. Brought flowers to the list, and did not explain herself, which was correct.",
    )
    log.append("insert Cast Dorothy Kell")

    # --- delete duplicate mid-appendix banners, high to low ---
    # Re-find after insertions by text, not stale indices
    to_delete = []
    seen_shape = set()
    shape_titles = {
        "What happens when you file the world (Lessons 6–10)",
        "What the experts still fight about (Lessons 11, 12 and 14)",
        "What they can still measure (Lesson 13)",
        "What can be recovered (Lessons 15–17)",
    }
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if t in shape_titles:
            if t in seen_shape:
                to_delete.append(i)
                nxt = doc.paragraphs[i + 1] if i + 1 < len(doc.paragraphs) else None
                if nxt is not None:
                    nt = nxt.text.strip()
                    if nxt.style and nxt.style.name == "List Paragraph":
                        to_delete.append(i + 1)
                    elif nt.startswith("—") or nt.startswith("-") or nt.startswith(EM) or "planning without" in nt or "Bell" in nt and len(nt) < 80:
                        to_delete.append(i + 1)
                    # two list paras after experts banner
                    nxt2 = doc.paragraphs[i + 2] if i + 2 < len(doc.paragraphs) else None
                    if nxt2 is not None and nxt2.style and nxt2.style.name == "List Paragraph":
                        to_delete.append(i + 2)
            else:
                seen_shape.add(t)

    for i in sorted(set(to_delete), reverse=True):
        delete_p(doc.paragraphs[i])
    log.append(f"deleted duplicate appendix banners: {sorted(set(to_delete))}")

    if OUT.exists():
        OUT.unlink()
    doc.save(str(OUT))

    check = Document(str(OUT))
    texts = [p.text for p in check.paragraphs]
    blob = "\n".join(texts)
    checks = {
        "five parts": "18 lectures in five parts" in blob,
        "You need first layout": any(t.startswith("You need first: what this lecture assumes") for t in texts),
        "Physics Prologue companion": "experiments described in the Physics Prologue" in blob,
        "this morning arrows": "The ones from this morning." in blob,
        "no yesterday arrows": "The ones from yesterday." not in blob,
        "feed-rate clock": "feed-rate clock" in blob,
        "downstairs bridge": "She did go downstairs." in blob,
        "Croydon battery": "car battery and a van" in blob,
        "Coldharrow Rise photo": "mantelpiece at Twenty-Two Coldharrow Rise" in blob,
        "no Elm Grove mantel": "mantelpiece at Twenty-Two Elm Grove" not in blob,
        "coupling cut opener": "Three weeks after the coupling was cut" in blob,
        "hospital door 137": "hospital door, not from Pauli" in blob,
        "6/G clerk": "would not confirm that any meeting had taken place" in blob,
        "Institute desk": "Institute for Unhelpful Clarity" in blob and "one extra chair" in blob,
        "Dorothy Kell cast": "Miss Dorothy Kell" in blob and "among the unrecovered" in blob,
        "Nelson cast": "Mr Pilbeam" in blob and "terrier" in blob,
        "91 climbed": "The log climbed while we argued" in blob,
        "mother-form lists": "recollection of his mother was on one of the two lists" in blob,
        "fidelity not 78": "not Mrs Chain" in blob and "seventy-eight per cent" in blob,
        "L18 slim": "The scene has already done the box and the lid." in blob,
        "no job title in L17": "Lolly’s new work" not in blob and "Lolly" + RSQ + "s new work" not in blob,
    }
    failed = [k for k, v in checks.items() if not v]
    print("paragraphs", n0, "->", len(check.paragraphs))
    for line in log:
        print(" ", line)
    if failed:
        raise SystemExit("VERIFY FAILED: " + ", ".join(failed))
    print("VERIFY OK")

    try:
        if LIVE.exists():
            LIVE.unlink()
        shutil.move(str(OUT), str(LIVE))
    except PermissionError:
        print("LOCKED: patched copy waiting at", OUT)
        return
    print("wrote", LIVE, "mb", round(LIVE.stat().st_size / 1e6, 2))
    if WS.exists():
        try:
            shutil.copy2(LIVE, WS)
            print("copied to workspace KINDLE file")
        except PermissionError:
            print("workspace KINDLE locked; series copy is live")


if __name__ == "__main__":
    main()
