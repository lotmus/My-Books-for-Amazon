# -*- coding: utf-8 -*-
"""One-pass fixes from the Book 2 review. Deletes itself only if asked."""
import os
import re
from pathlib import Path


def write(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp, path)

ROOT = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\A Trip Is Not a New Life - Manuscript")


def sub(text, old, new, label):
    if old in text:
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise SystemExit(f"MISSING {label}")


def main():
    p = ROOT / "05_Part_Five_The_Classroom.md"
    t = p.read_text(encoding="utf-8")
    t = sub(t,
        "It is two orders of magnitude more cycles on joints that have already shown they sand.",
        "Hundreds of hours against twenty-two is several times the wear, and about ten times if the stay runs for months. That is an order of magnitude. It is not two, and it is not three. The joints have already shown they sand.",
        "orders ch17")
    t = sub(t,
        "A lander on the far side carried a dosimeter and, from 2019 on, read a little over a thousand microsieverts a day on the open surface. Multiply a year if you want a rude sketch: on the order of six-tenths of a sievert, near or above the career limits several agencies still use, on the order of six-tenths of a sievert themselves.",
        "A lander on the far side carried a dosimeter and, in 2019, read about 1,370 microsieverts a day on the open surface. Multiply by a year: about half a sievert. Career limits several agencies still use sit near 600 millisieverts. Half a sievert is near that line.",
        "dose ch21")
    t = sub(t,
        "Apollo 13 used that refusal after the service module failed.",
        "Apollo 13 had already left that path when the service module failed. A burn put them back on a road that falls home. The kindness was reachable. It was not the road they were already on.",
        "apollo ch22")
    t = sub(t,
        "Elena would put the treaty on the table next to the three cards and ask which card it authorizes. It authorizes a sortie for certain, an outpost if the partners keep paying, and a settlement not at all. The poster that says “our crater” has picked up a card the treaty did not deal.",
        "Elena would put the treaty on the table next to the three cards and ask which card it contains. It contains none of them. It permits going and use, and it forbids a national fence. A sortie fits inside what it permits. An outpost fits only as use, for as long as someone keeps the loops closed. A settlement is not a clause from 1967. The poster that says “our crater” has picked up a card the treaty did not deal.",
        "treaty ch23")
    write(p, t)

    p = ROOT / "02_Part_Two_The_Moon_First.md"
    t = p.read_text(encoding="utf-8")
    t = sub(t,
        "came home with minimal char loss and no unusual conditions found, by the agency’s own preliminary account.",
        "came home, on the first public look, with no unusual conditions and far less char loss than the empty flight. By early September a safety-panel count put the loss at about nine sites, against more than a hundred on the empty loop. A fuller cut-up, including x-ray of the material, was still owed.",
        "shield ch6")
    write(p, t)

    p = ROOT / "06_Part_Six_The_Long_Ticket.md"
    t = p.read_text(encoding="utf-8")
    if "so this chapter does not assign another book" not in t:
        t = sub(t,
            "Sleeping flesh is a story that biochemistry has not signed.\n",
            "Sleeping flesh is a story that biochemistry has not signed.\n\n"
            "A few words, so this chapter does not assign another book. Proper time is the time a clock reads along its own path. It is the only time a body keeps. A fast trip can change the date waiting at home. It does not hand the traveler extra heartbeats. The loaf, in the cosmology book, was the claim that every clock shares one inventory of moments. It does not. The shove was the measurement that killed the claim. Leftover glow is the habit of treating that dead claim as if it still lit the room. The Omega Point was a required last mind at the end of time, as if the universe owed someone a final computation. This chapter refuses the cruise as destiny. It does not reopen that trial.\n",
            "ch25 defs")
    t = sub(t,
        "![Figure 25. A tractor on bright dirt, working a field. The photograph is patient Earth labor; the chapter’s crew that does not sleep is still a machine that can wait.](Figures/fig25.jpg)",
        "![Figure 25. A long thin craft, a grain drawn as a strike on the nose, and a box labeled library. The crew that does not sleep is a machine that can wait.](Figures/fig25.png)",
        "fig25")
    t = sub(t,
        "The other book’s one-dictionary test would then be a shipping label, not a frozen accident.",
        "A second origin with a code of its own would be a second dictionary. If the pour happened, that test becomes a shipping label, not a frozen accident. You do not need the other book’s trial to use the brake here.",
        "ch26 dictionary")
    t = sub(t,
        "The other book’s tangle lives here as dirt: meaning that is not in the parts.",
        "Meaning that is not in the parts — a loop the parts cannot see by looking only at themselves — lives here as dirt.",
        "ch26 tangle")
    t = sub(t,
        "![Figure 26. A vault door in snow, large in frame. A library is a physical object.](Figures/fig26.jpg)",
        "![Figure 26. A thin book labeled sequence, a heavy box labeled wet lab, and a closed lid labeled sea. Look first. Seed later.](Figures/fig26.png)",
        "fig26")
    write(p, t)

    p = ROOT / "07_Part_Seven_Many_Clocks.md"
    t = p.read_text(encoding="utf-8")
    t = sub(t,
        "# PART VII — Local Fixes, Not Fountains\n\n## 27. Her Hands Still Age",
        "# PART VII — Local Fixes, Not Fountains\n\n"
        "The camp has been priced. The classroom was the bills a poster skips. The long ticket was a cruise flesh will not take. What follows is the body that stays, on the world that already has a staff. The airlock in the next chapter is the same door as Chapter 1. The hands on it have been aging the whole time.\n\n"
        "## 27. Her Hands Still Age",
        "part7 bridge")
    write(p, t)

    fix_appendix()
    print("ok")


def triples_to_table(lines, renumber=None):
    """lines are the body of a glance: header 3 lines then groups of 3, no blanks."""
    if len(lines) < 3 or lines[0] != "#":
        raise SystemExit("bad glance header " + repr(lines[:5]))
    rows = [["#", "Relation", "Role"]]
    body = lines[3:]
    if len(body) % 3 != 0:
        raise SystemExit(f"glance not groups of 3: {len(body)} {body[:6]}")
    n = 0
    for i in range(0, len(body), 3):
        num, rel, role = body[i], body[i + 1], body[i + 2]
        if renumber is not None:
            n += 1
            num = f"({renumber + n - 1})"
            if rel.strip() == "Inventory in A20":
                rel = "Inventory in A46"
        rows.append([num, rel, role])
    out = []
    for r in rows:
        out.append("| " + " | ".join(c.replace("|", "/") for c in r) + " |")
    out.insert(1, "| --- | --- | --- |")
    return "\n".join(out)


def fix_appendix():
    p = ROOT / "11_Appendix.md"
    t = p.read_text(encoding="utf-8")
    t = sub(t,
        "Each note An twins popular chapter n, through A26. The body notes begin at A27 and use the same rule. Units are SI unless stated. c is the speed of light. Dates in this kitchen are September 2026; official years will move. Classes of mission are the durable objects.",
        "Each note An twins popular chapter n, through A26. The body notes begin at A27 and use the same rule. Units are SI unless stated. c is the speed of light. Dates in this kitchen are September 2026; official years will move. Classes of mission are the durable objects. Sources and the glossary are once, at the end of this appendix. Equation numbers run in one sequence: (1)–(16) are the camp, (17) on are the body.",
        "howto")
    t = sub(t,
        "Artemis III (crewed landing): announced with a 2024 target, restated for 2025, 2026, and 2027 in successive public revisions through this kitchen’s date.",
        "The crewed landing was announced as Artemis III with a 2024 target and restated for 2025, 2026, and 2027. By this kitchen the name had moved: the mission now called the rehearsal is an Earth-orbit test, and the landing attempt is a later flight. See A7. Do not read the old name as the current noun.",
        "A3")
    t = sub(t,
        "China’s Chang’e-4 lander carried a dosimeter to the far side starting January 2019; published readings averaged a little over 1,000 microsieverts per day on the unshielded surface — roughly 570–730 mSv per year extrapolated, near or above the career limits (order 600 mSv) used by several agencies for their astronaut corps.",
        "China’s Chang’e-4 lander carried a dosimeter to the far side starting January 2019. The published average dose equivalent on the unshielded surface was about 1,370 microsieverts a day (Zhang and colleagues, Science Advances, 2020). Multiplied by a year, that is about half a sievert, near career limits several agencies still use (order 600 mSv).",
        "A4 dose")
    t = sub(t,
        "Free-return trajectory: a translunar path shaped so that, absent any further burn, the spacecraft swings around the Moon and re-enters Earth’s atmosphere — the safety margin that made Apollo 13’s return possible after a service-module failure, and the same margin Artemis-II-class missions are flown to preserve.",
        "Free-return trajectory: a translunar path shaped so that, absent any further burn, the spacecraft swings around the Moon and re-enters Earth’s atmosphere. Apollo 13 had already left that path when the service module failed. A burn put the crew back onto a road that falls home. The kindness was reachable. It was not the road they were already on. Artemis-II-class missions are drawn to keep a version of the path from the start.",
        "A6 apollo")
    t = sub(t,
        "Modern polar-shift suit requirements, by comparison, are written against hundreds of hours of cumulative EVA across a multi-week or multi-month stay: two to three orders of magnitude more wear-cycles on the same class of joint.",
        "Modern polar-shift suit requirements, by comparison, are written against hundreds of hours of cumulative EVA across a multi-week or multi-month stay: several times the cycles, and about ten times if the stay runs for months. That is one order of magnitude, not two or three.",
        "A7 orders")
    t = sub(t,
        "ISS is the existence proof of a continuously staffed outpost with a cargo cult that has never been optional.",
        "The station in Earth orbit is the existence proof of a continuously staffed outpost, and the proof that the supply ships never became optional. A cargo cult, in this book’s glossary, is a copy of the form without the supply. The station is the opposite lesson: the form has lasted because the supply did not stop.",
        "A8")
    t = sub(t,
        "so nitrogen does not boil out of the blood.",
        "so dissolved nitrogen does not come out of the blood as bubbles when the pressure drops.",
        "A17 nitrogen")
    t = sub(t,
        "A polar outpost written against hundreds of hours is two orders of magnitude more cycles on the same class of joint.",
        "A polar outpost written against hundreds of hours is several times the cycles, and about ten times if the stay runs for months — one order of magnitude, not two.",
        "A17 orders")
    t = sub(t,
        "Chang’e-4’s far-side dosimeter, from 2019: a little over 1,000 microsieverts a day on the unshielded surface, order 0.6 Sv a year if you simply multiply, near or above career limits several agencies use (order 600 mSv).",
        "Chang’e-4’s far-side dosimeter, 2019: about 1,370 microsieverts a day on the unshielded surface. Multiplied by 365 that is about 0.50 Sv a year, near career limits several agencies use (order 600 mSv). A thousand microsieverts a day times a year is not six-tenths of a sievert. Do not print both.",
        "A21 dose")
    t = sub(t,
        "Apollo 13 used the kindness after the service module failed.",
        "Apollo 13 had already left a free return when the service module failed. A burn put the crew back on one.",
        "A22 apollo")
    t = sub(t,
        "The treaty authorizes a sortie, an outpost if the partners keep paying, and a settlement not at all. Courts, a tax, a child who is from there: not a clause from 1967. A kitchen that can miss a ship.",
        "The treaty does not contain this book’s three cards. It permits going and use. It forbids a national fence. It does not decide who owns extracted ice, and it does not found a school, a tax, or a child who is from the crater. A sortie fits inside what it permits. An outpost fits only as use, for as long as the partners keep the loops closed. A settlement — courts, a kitchen that can miss a ship — is not a clause from 1967.",
        "A23")
    t = sub(t,
        "A transistor does not vaccinate a neighborhood or keep a grid up. Institutions store methods; they fail; knowledge dies in fires and fronts. Famine is energy and coordination with a body count.\nGermline “enhancement” is a political and ethical front, not a SKU. Look first: do not overwrite a childhood because a slide said the year 12,000 would thank you.",
        "A transistor does not vaccinate a neighborhood or keep a grid up. A method that lives only in one laboratory dies when the laboratory does. Meetings, ledgers, and schools are how a method outlives the person who first got it to work. They are also how a method gets captured, delayed, or burned. Famine is energy plus coordination with a body count: the calories can exist in the wrong district and still be a famine.\n"
        "Hot: institutions have stored real methods (vaccines, packets, a grid) and have also lost them in fires, purges, and fronts. Warm: whether a given ledger will still be staffed in fifty years. Cold: progress as a law that fires if we wait, and a germline “enhancement” sold as a product. Germline editing is a political and ethical front, not a SKU. Look first: do not overwrite a childhood because a slide said the year 12,000 would thank you.",
        "A42")
    t = sub(t,
        "Sensitive periods make children cheaper to reroute than adults. Stroke recovery is overtime, not a hidden room. Practice thickens a map and eats mornings. Tools and other people are part of the method.\nAdjusting ≠ spare capacity.",
        "Sensitive periods — language, vision, some motor maps — are hot as developmental windows. They are cold as a license to treat a childhood as a construction site because adaptation sounded cheaper than a tool. Adult maps still change. Stroke recovery is the worked case: tissue reroutes, and the reroute is practice, sleep, a therapist, and months. It is overtime. It is not a hidden room that was waiting unlocked.\n"
        "Practice thickens a map and eats mornings. London-taxi spatial memory and musical training are the expensive versions of the same fact: the map gets larger where the hours went, and the hours are gone. Tools and other people are part of the method. A checklist, a night nurse, a colleague who has seen the pump, a school that protects sleep. None of that is a spare ninety percent. Chapter 34 already emptied that cupboard.\n"
        "Adjusting is not spare capacity. It is the staff you already had, spent, plus help you hired, plus a morning you will not get twice.",
        "A44")
    t = sub(t,
        "A map of a brain is not a walk. (A40 draws the line a walk makes.) A run of the map is, at best, a second person. The first person remains in the meat or is dead. Travel did not happen.\nRestorative chips: local, warm-to-hot as tools with scars. Uploads / forever-mind / required Omega-ish last computation: cold. Book 1 already broke the required last mind on the shove; this note does not reopen the leftover glow.",
        "A worldline is the path a body actually takes. Proper time, in A40, is the length of that path as the body’s own clock reads it. A file is a description of a state. It is not the path. Running the description, if anyone ever can, starts a new path. At best that is a second person. The first person remains in the meat, or is dead. Travel did not happen. Copying a map is not walking it.\n"
        "Restorative chips — a stimulator, a cochlear implant, a local prosthesis — are tools with scars. Warm to hot as tools. They do not pour the person into a file.\n"
        "Uploads, a forever-mind, and a required last computation are cold. The required last mind was a claim that the universe needs a final observer to finish the sum. The cosmology book already refused it. Leftover glow is the habit of keeping the refused claim in the room. This note does not reopen it. It only keeps the file from being sold as the walk.",
        "A45")

    # Chapter-number corrections in the old body bibliography.
    for a, b in (
        ("Ch 1:", "Chapter 27:"),
        ("Ch 2:", "Chapter 28:"),
        ("Ch 5:", "Chapter 31:"),
        ("Ch 7:", "Chapter 33:"),
        ("Ch 9:", "Chapter 35:"),
        ("Ch 11:", "Chapter 37:"),
        ("Ch 12:", "Chapter 38:"),
        ("Ch 16:", "Chapter 42:"),
    ):
        if a in t:
            t = t.replace(a, b, 1)
        elif b not in t:
            raise SystemExit("missing bib tag " + a)
    t = t.replace(
        "Worked numbers added in the craft pass, by chapter.",
        "Worked numbers, by the chapter they actually sit in.",
        1,
    )

    # Pull the camp further-reading and glossary out of the middle.
    marker = "\nA17. Pressure, Heat, and Why a Glove Is a Workplace\n"
    head, sep, tail = t.partition(marker)
    if not sep:
        raise SystemExit("no A17")
    fr = "\nFurther Reading (tiered)\n"
    if head.count(fr) != 1:
        raise SystemExit(f"camp further reading count {head.count(fr)}")
    before, _, camp_back = head.partition(fr)
    # camp_back is further reading + glossary, ending just before A17
    camp_back = camp_back.rstrip() + "\n"
    if "\nGlossary\n" not in camp_back:
        raise SystemExit("no camp glossary")
    camp_read, _, camp_gloss = camp_back.partition("\nGlossary\n")
    head = before.rstrip() + "\n\nSources for these camp notes are at the end of the appendix, with the body sources.\n"
    t = head + marker + tail

    # Renumber inline body equations before the glance is rebuilt.
    body_mark = "\nAPPENDIX — The Body Notes\n"
    h2, s2, tail2 = t.partition(body_mark)
    if not s2:
        raise SystemExit("no body notes")
    repls = [
        (r"\(1\)\s+Life expectancy", "(17)  Life expectancy"),
        (r"\(3\)\s+Dish-division", "(19)  Dish-division"),
        (r"\(10\)\s+hazard\(age\)", "(26)  hazard(age)"),
        (r"\(4\)\s+Local fix", "(20)  Local fix"),
        (r"\(2\)\s+Brain", "(18)  Brain"),
        (r"\(6\)\s+Logistic", "(22)  Logistic"),
        (r"\(5\)\s+Sequencing", "(21)  Sequencing"),
        (r"\(7\)\s+10,000", "(23)  10,000"),
        (r"\(8\)\s+τ", "(24)  τ"),
        (r"\(9\)\s+Δτ", "(25)  Δτ"),
    ]
    for a, b in repls:
        tail2, n = re.subn(a, b, tail2, count=1)
        if n != 1 and b not in tail2:
            raise SystemExit("missing eq " + a)

    def convert_glance(block, title, renumber):
        lines = block.splitlines()
        # find title line
        try:
            i = lines.index(title)
        except ValueError:
            raise SystemExit("no " + title)
        # body until blank line
        j = i + 1
        chunk = []
        while j < len(lines) and lines[j].strip():
            chunk.append(lines[j])
            j += 1
        table = triples_to_table(chunk, renumber=renumber)
        new_title = title if renumber is None else "Equations at a Glance, Continued"
        lines[i:j] = [new_title, table]
        return "\n".join(lines)

    h2 = convert_glance(h2, "Equations at a Glance", None)
    tail2 = convert_glance(tail2, "Equations at a Glance", 17)

    # A40 case list -> table. It sits in the body tail.
    case_start = "Case\nNumber\nNote\n"
    if case_start not in tail2:
        raise SystemExit("no A40 case header")
    pre, _, rest = tail2.partition(case_start)
    rows_src = []
    lines = rest.splitlines()
    k = 0
    while k < len(lines) and not lines[k].startswith("Temperatures."):
        if lines[k].strip() == "":
            k += 1
            continue
        rows_src.append(lines[k])
        k += 1
    if len(rows_src) % 3 != 0:
        raise SystemExit(f"A40 rows {len(rows_src)}")
    table_lines = ["| Case | Number | Note |", "| --- | --- | --- |"]
    for i in range(0, len(rows_src), 3):
        cells = [c.replace("|", "/") for c in rows_src[i:i + 3]]
        table_lines.append("| " + " | ".join(cells) + " |")
    tail2 = pre + "\n".join(table_lines) + "\n\n" + "\n".join(lines[k:])

    # Splice camp sources and one glossary.
    if tail2.count("\nFurther Reading (tiered)\n") != 1:
        raise SystemExit("body further reading count")
    if tail2.count("\nGlossary\n") != 1:
        raise SystemExit("body glossary count")
    fr_pre, _, fr_post = tail2.partition("\nFurther Reading (tiered)\n")
    gloss_pre, _, gloss_post = fr_post.partition("\nGlossary\n")
    camp_read = camp_read.strip()
    camp_gloss = camp_gloss.strip()
    extra = "\n".join([
        "Free return. A translunar path that falls home with no further burn. A path already left is not this path until a burn puts you back on it (A22).",
        "HALE. Healthy life expectancy: years with disability weighted out. Not the pulse on the wall (A28).",
        "Hallmarks. A review’s list of aging mechanisms. A list, not a fuse (A29).",
        "Helium. In this series, a cold product sold as already on the dock: a scheduled immortality, a downtown by Friday, a spare mind, a straight line to furniture nobody can name.",
        "Hot, warm, cold. Established; a working account with real gaps; speculation sold as inventory.",
        "Non-appropriation. The 1967 rule that no nation may claim the Moon as territory. Use is not title. The clause does not contain this book’s three nouns (A23).",
        "Pre-breathe. The wait on a lower-pressure oxygen suit, so dissolved nitrogen does not come out of the blood as bubbles (A17).",
        "Regolith. Broken rock and dust on a surface with no air to round it and no rain to wash the charge off (A20).",
        "Sievert. A dose weighted for biological harm. A thousandth is a millisievert. The open-surface reading in this book, about 1,370 microsieverts a day, is about half a sievert a year if you multiply (A4, A21).",
    ])
    # Drop the camp "Avoid as engineering" from sitting twice; keep it inside camp_read.
    tail2 = (
        fr_pre
        + "\nFurther Reading (tiered)\n"
        + "Camp sources. The notes through A26 use these.\n\n"
        + camp_read
        + "\n\nBody sources. The notes from A27 use these.\n\n"
        + gloss_pre
        + "\nGlossary\n"
        + "One list. The camp and the body share the book, so they share the words.\n\n"
        + camp_gloss
        + "\n"
        + extra
        + "\n"
        + gloss_post.lstrip("\n")
    )
    t = h2 + body_mark + tail2
    if "Inventory in A20" in t:
        raise SystemExit("A20 inventory survived")
    if "0.6 Sv" in t:
        raise SystemExit("0.6 Sv survived")
    if t.count("\nGlossary\n") != 1:
        raise SystemExit("glossary count " + str(t.count("\nGlossary\n")))
    if t.count("\nFurther Reading (tiered)\n") != 1:
        raise SystemExit("fr count")
    write(p, t)


if __name__ == "__main__":
    main()
