# -*- coding: utf-8 -*-
"""SP-method elevation: real craft inserts, no clone padding."""
from pathlib import Path
import os
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

# Inserted BEFORE each chapter's "Where the popular..." or "Rule:" block.
# Word targets: clear 1500 with teaching, not echo.

INSERTS = {
    10: (
        "03_Part_Three_Not_A_Straight_Line.md",
        r"^## 11\.",
        """---

Where the popular version goes wrong.

The slide draws an S and then pretends the top is a runway. It is a wall. The drunk middle is where founders photograph; the wall is where nurses, mines, and meetings live. Ask which wall was waived before you cash the middle as destiny.

""",
    ),
    13: (
        "04_Part_Four_The_Honest_Body.md",
        r"^Where the popular version goes wrong\.\s*$",
        """A morning in the clinic, without a founder’s font.

Rohan sits with a family while Mara’s capsule paperwork is still a rumor on a delay. The wall has a photograph of a win. The desk has a stack that says *not eligible* in a font designed to look neutral. He does not lie. He names the three clocks: the biology that did not match the protocol, the geography that put the trial two ferries away, the insurance word that turned a molecule into a rumor. The family wanted a downtown. They leave with a blood-pressure pill that already exists and a surgeon’s name that can still be afforded. Boring. Hot. The photograph on the wall does not get to vote.

What “local” costs when you refuse the costume.

A sickle-cell-class edit is a door. The door has a conditioning month that can kill on the way to a save, a staff that cannot be downloaded, a ledger that decides whether the door is a gift or a membership. Hot as a class of win. Cold as a default for every zip code. Warm only if you keep the receipt on the counter where helium cannot sweep it off. Delivery of the molecule was Chapter 4’s truck. Delivery of the payment is this chapter’s. Two trucks. Same rule: a molecule without a route is a press release.

Say it so a smart person does not check her phone: a trial is a meeting that can say no; a mouse paper is not a woman at an airlock; inequality is a clock; keep the receipt.

""",
    ),
    14: (
        "04_Part_Four_The_Honest_Body.md",
        r"^Where the popular version goes wrong\.\s*$",
        """A second blister of time, after the pump week.

The joint is a two. The radio is late. Rohan is on the delay teaching a valve she has never seen. She wants the learning to be free — a cupboard opening, a spare self stepping forward. It is not free. It costs the morning she would have spent on the basil log, the sleep she almost skipped, the frustration that is the method. Twelve wrong grips. A right one. No loft. Chapter 6 emptied the loft; this chapter is the invoice for using the staff you already had.

What institutions buy that skulls cannot.

A checklist is a tool. A night nurse is a tool. A school that protects sleep for the people who will walk the stroke hallway is a tool. Species-scale adjustment is not a password; it is overtime plus help plus mornings that do not come twice. Cold: selling that package as unlocking. Warm: naming tools and other people as the method without calling the skull idle. Hot: brains change, and the change costs.

Say it so she stays in the chair: plasticity is real; spare capacity was a sales word; keep the log.

""",
    ),
    15: (
        "04_Part_Four_The_Honest_Body.md",
        r"^Where the popular version goes wrong\.\s*$",
        """Kitchen picture, no incense.

Mara’s pH log is already a file. It keeps the plant alive across a delay. It is not her. If someone copied the log onto a prettier drive and called the drive Mara, the basil would still need a number from hands that age. The copy would remember Tuesdays. The remembering would be a psychology. The worldline in the meat would still be the worldline in the meat. Travel did not happen. A photocopy of a letter does not move the sender; a twin born tomorrow is not you relocated; a perfect scan — which we do not have — is still a map unless something continuous carried the walk. Continuity is what death interrupts. Naming a hard drive does not repair the interruption.

Sort the word *upload* before the carrot stacks it.

Backup for historians: a file. Useful. Not a person. Prosthesis network that returns a Tuesday: restoration. Local. Warm when the kitchen votes. Second runner who wakes sure they are you: a copy. Hot as a distinction — the first worldline did not travel. Cold as a product if sold as immortality-for-the-original. Original continues in the machine: needs a carrier for continuity we do not have. Cold.

Incompleteness is enough of a wall if you need one: a map of a mind is not obliged to *be* the mind. No sermon from a named book. No helium in a footnote. Omega-ish required last minds stay cold; they were not selected by a clinic and they are not selected by the accelerating stretch. Take the implant if hearing is what you paid for. Put the port down.

Say it so she does not reach for her phone: a file is not a worldline; a restoration is not a pour; hang the three colds apart.

""",
    ),
    16: (
        "04_Part_Four_The_Honest_Body.md",
        r"^Rule: Do not wait for helium\.",
        """One last kitchen beat before the seal, so the inventory has dirt on it.

She names the basil anyway. Sentiment does not get to vote; the log does. The capsule may buy a useful season. It will not buy helium and it will not unlock a brain she was not already using. Hands still age. Dirt still has a chemistry. Chemistry can be bullied. That was always the whole trick. Hit the airlock. Take the local win. Put the sermon down.

If you wanted a thousand-year ape, leave with a colder want: mornings worth logging. If you wanted a spare ninety percent, leave with the organ you were already using, plus a notebook, plus sleep, plus someone like Rohan who already knows the pump. If you wanted year 12,000’s kitchen, leave with the invoices that will still be due, and without a catalog this book refused to print. A destinations book can keep her seal. A loaf book already refused a cosmic now and a required last mind. You can stop here. The hands will still be the hands tomorrow.

""",
    ),
}


def wc(text: str) -> int:
    body = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    body = re.sub(r"^#+\s+.*$", " ", body, flags=re.M)
    return len(re.findall(r"[A-Za-z0-9\u2019']+", body))


def sizes(text: str):
    out = []
    for sec in re.split(r"(?=^##\s+)", text, flags=re.M):
        m = re.match(r"^##\s+(\d+)\.\s+", sec, re.M)
        if not m:
            continue
        n = int(m.group(1))
        body = re.sub(r"!\[.*?\]\(.*?\)", " ", sec)
        body = re.sub(r"^#+\s+.*$", " ", body, flags=re.M)
        out.append((n, len(re.findall(r"[A-Za-z0-9\u2019']+", body))))
    return out


def insert_once(path: Path, pat: str, block: str, needle_guard: str) -> bool:
    t = path.read_text(encoding="utf-8")
    if needle_guard in t:
        print("skip (already)", path.name, needle_guard[:40])
        return False
    m = re.search(pat, t, re.M)
    if not m:
        print("NO MATCH", path.name, pat)
        return False
    t = t[: m.start()] + block + t[m.start() :]
    path.write_text(t, encoding="utf-8", newline="\n")
    print("ins", path.name, pat[:40])
    return True


def main() -> None:
    guards = {
        10: "The slide draws an S and then pretends",
        13: "Rohan sits with a family while Mara’s capsule",
        14: "A second blister of time, after the pump week",
        15: "Mara’s pH log is already a file. It keeps the plant",
        16: "One last kitchen beat before the seal",
    }
    # Ch13-15 share the same popular-wrong header; insert before FIRST occurrence in that chapter only.
    # Process file by file with chapter-scoped search.
    for n, (fn, pat, block) in INSERTS.items():
        p = ROOT / fn
        t = p.read_text(encoding="utf-8")
        if guards[n] in t:
            print("skip", n)
            continue
        # Scope to chapter
        ch_pat = rf"(^## {n}\..*?)(?=^## |\Z)"
        cm = re.search(ch_pat, t, re.M | re.S)
        if not cm:
            print("no chapter", n)
            continue
        sec = cm.group(1)
        m = re.search(pat, sec, re.M)
        if not m:
            print("no pat in chapter", n, pat)
            continue
        # offset into full text
        abs_start = cm.start(1) + m.start()
        t = t[:abs_start] + block + t[abs_start:]
        p.write_text(t, encoding="utf-8", newline="\n")
        print("ins", n)

    parts = [
        f
        for f in sorted(os.listdir(ROOT))
        if re.match(r"^\d{2}_", f)
        and f.endswith(".md")
        and f not in ("00_Chapter_Outline.md", "00_Figure_Plan.md", "00_Status.md")
    ]
    big = "\n\n".join((ROOT / p).read_text(encoding="utf-8") for p in parts)
    total = wc(big)
    print("TOTAL", total)
    thin = []
    for n, w in sizes(big):
        mark = " THIN" if w < 1500 else ""
        print(f"Ch {n:02d} {w:5d}{mark}")
        if w < 1500:
            thin.append((n, w))
    print("thin", thin)

    st = (ROOT / "00_Status.md").read_text(encoding="utf-8")
    st = re.sub(r"\*\*[\d,]+ words\*\*", f"**{total:,} words**", st)
    st = re.sub(
        r"Thin leftovers \(if any\):.*",
        f"Thin leftovers (if any): {thin or 'none'}.",
        st,
    )
    if "SP-method" not in st:
        st += (
            "\n\n## Craft pass (Schrödinger's Paperwork method)\n\n"
            "- Stripped expand-script clone padding (`Need was N`, repeated coat/bench inventories).\n"
            "- Added popular-wrong + Rule closes on Ch13–16; dramatized clinic/pump/log beats.\n"
            "- Score by part craft, not by padding to a floor.\n"
        )
    (ROOT / "00_Status.md").write_text(st, encoding="utf-8", newline="\n")

    r = subprocess.run(
        [sys.executable, str(ROOT / "Figures" / "build_book.py"), "body"],
        capture_output=True,
        text=True,
    )
    print(r.stdout)
    if r.returncode:
        print(r.stderr)
        raise SystemExit(r.returncode)


if __name__ == "__main__":
    main()
