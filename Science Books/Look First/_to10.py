# -*- coding: utf-8 -*-
"""Close every scored defect in Book 2. Delete this file after it runs."""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
MAN = os.path.join(ROOT, "A Trip Is Not a New Life - Manuscript")


def load(name):
    path = os.path.join(MAN, name)
    with open(path, encoding="utf-8") as f:
        return path, f.read()


def save(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)


def cut_block(text, start, end, label):
    i = text.find(start)
    j = text.find(end)
    if i < 0 or j < 0 or j < i:
        print("MISS", label)
        return text
    j = j + len(end)
    while text[j:j + 1] == "\n":
        j += 1
        if text[j - 2:j] == "\n\n":
            break
    print("CUT", label, j - i)
    return text[:i] + text[j:]


def rewrite_where(line):
    if not line.strip().lower().startswith("where "):
        return line, False
    nl = "\n" if line.endswith("\n") else ""
    body = line.strip()[6:].strip()
    if body.startswith("t is "):
        sent = "In that line, " + body
    else:
        body = re.sub(r"[“\"]([^”\"]+)[”\"]", r"\1", body)
        if re.match(r"^\d", body):
            sent = "The sum " + body
        elif body[:1].islower():
            sent = body[0].upper() + body[1:]
        else:
            sent = body
    if sent and sent[-1] not in ".!?":
        sent += "."
    return sent + nl, True


def apply_where(text):
    out = []
    n = 0
    for line in text.splitlines(keepends=True):
        new, hit = rewrite_where(line)
        if hit:
            n += 1
        out.append(new)
    return "".join(out), n


def insert_before(text, marker, paragraph, label):
    paragraph = paragraph.strip()
    if paragraph in text:
        print("HAVE", label)
        return text
    i = text.find(marker)
    if i < 0:
        print("MISS", label)
        return text
    print("ADD", label)
    return text[:i] + paragraph + "\n\n" + text[i:]


def main():
    # where-lines in every manuscript file
    for fn in sorted(os.listdir(MAN)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(MAN, fn)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        new, n = apply_where(text)
        if n:
            save(path, new)
        print("where", fn, n)

    path, text = load("05_Part_Five_The_Classroom.md")
    text = cut_block(
        text,
        "The ground will not store the afternoon for her.",
        "the crew spends the fortnight deciding who sleeps.",
        "ch18-after",
    )
    text = cut_block(
        text,
        "A boot print that is still sharp after fifty years is not a charm.",
        "The poster is the claim that a porch and a slogan are the year.",
        "ch20",
    )
    text = cut_block(
        text,
        "Two weathers, and they do not send the same invoice.",
        "The Sun in the corner is the shower you do not get to reschedule.",
        "ch21-retell",
    )
    text = cut_block(
        text,
        "Jules puts the shelter on the same card as the valve, because a valve you cannot reach during a storm is a valve you do not have.",
        "Ugly is how you buy the rest of the shift.",
        "ch21-echo",
    )
    text = cut_block(
        text,
        "Kindness has a shape on a chart.",
        "If the drink is gone, home is no longer a mood you can select.",
        "ch22-retell",
    )
    text = cut_block(
        text,
        "Write the window on the checklist in days, not in courage.",
        "A crew that cannot point to it is a crew that has been given a lullaby and told it was navigation.",
        "ch22-echo",
    )
    text = cut_block(
        text,
        "The sentence that governs this is old enough to have grandchildren",
        "A good measurement does not promote the flag.",
        "ch23",
    )
    text = cut_block(
        text,
        "Orders, so a hearing cannot choose a prettier coin. A heavy government launch in this era is often a billion-class event once you count the stack, the cadence you do not yet have",
        "The hearing is not allowed to buy the loop and call it the sea wall, or to cancel the loop and call the gauge moved.",
        "ch24",
    )
    text = text.replace("\n\n\n", "\n\n")
    save(path, text)

    path, text = load("09_Part_Nine_Not_A_Straight_Line.md")
    old = (
        "If you had multiplied that fifty by two hundred, you would have printed "
        "a 3900s kitchen that was all steam and no transistor, or all transistor "
        "and no steam, depending on which drunk middle you photographed."
    )
    new = (
        "If you had multiplied that fifty by two hundred, the calendar would have "
        "jumped ten thousand years. The sum later in this chapter names the year. "
        "It does not let you pack furniture from a century you have not reached."
    )
    if old not in text:
        print("MISS 3900s")
    else:
        text = text.replace(old, new)
        print("fixed 3900s", "3900s" in text)
    save(path, text)

    path, text = load("11_Appendix.md")
    text = insert_before(
        text,
        "\nA18. The Fortnight",
        "An eight-hour suit day is not eight hours at the valve. Pre-breathe, donning, "
        "the airlock, and the walk back are part of the shift, so the useful work is a "
        "few hours. That overhead is already priced in the chapter. It is not a new "
        "physiological constant.",
        "A17",
    )
    text = insert_before(
        text,
        "\nA19. The Ratio",
        "One kilowatt through fourteen days is 14 \u00d7 24 = 336 kilowatt-hours. Several "
        "kilowatts through the same fortnight is a few thousand kilowatt-hours. That is "
        "why the chapter calls the battery a cargo shipment rather than a lamp. The "
        "second shipment is the margin.",
        "A18",
    )
    text = insert_before(
        text,
        "\nA20. Charge",
        "Warming a tonne of ice from tens of kelvin is on the order of a hundred "
        "kilowatt-hours before the melt. The specific heat of ice is about 2 kilojoules "
        "per kilogram per kelvin; about 200 kelvin of warming is about 400 kilojoules "
        "per kilogram, about 110 kilowatt-hours per tonne. The melt itself is 334 "
        "kilojoules per kilogram, about 93 kilowatt-hours per tonne. Together that is "
        "hundreds of kilowatt-hours per tonne before anyone has cleaned it. Cracking "
        "the water is the larger bill. An electrolyzer is on the order of 50 "
        "kilowatt-hours per kilogram of hydrogen, and a tonne of water holds about "
        "110 kilograms of hydrogen (the 2/18 mass fraction), so the crack is several "
        "thousand kilowatt-hours per tonne before the liquefier. Losses make both bills "
        "larger. The chapter\u2019s hundreds and thousands are these orders.",
        "A19",
    )
    text = insert_before(
        text,
        "\nA29. Hallmarks",
        "Life expectancy at birth is not the years left to a woman already at eighty. "
        "In the period tables for the lucky kitchens named above, remaining life "
        "expectancy at eighty for women is on the order of a decade: about nine to ten "
        "years in recent United States tables, a little higher in Japan. The chapter\u2019s "
        "\u201cabout another decade\u201d is that order. It is not forty years, it is not 122, and "
        "it is not a promise written for one woman.",
        "A28",
    )
    text = insert_before(
        text,
        "\nA38. Logistic",
        "Smallpox was certified eradicated by the World Health Assembly in 1980. Measles "
        "is the same class of shot and is unfinished, because a program can be skipped. "
        "The chapter uses that pair so a finished vaccine is not told as if every vaccine "
        "finished itself. The human genome draft closed around 2003 at a cost on the "
        "order of three billion dollars. A read now, on the order of a few hundred dollars "
        "in a day, is the stair. The nurse did not get cheaper on that curve.",
        "A37",
    )
    text = insert_before(
        text,
        "\nA40. Proper Time",
        "Ten thousand divided by fifty is 200 exactly. A fifty-year window that ends in "
        "1900, stretched by ten thousand years, lands on the year 11900 (1900 + 10,000), "
        "not in any nearer century a photograph of steam or of transistors might suggest. "
        "The only honest claim for that year, read from a kitchen in 1900, is more engines "
        "and more wire. The method is not allowed to import antibiotics, the transistor, "
        "or the wars. The chapter has to say the year.",
        "A39",
    )
    text = insert_before(
        text,
        "\nA42. Meetings",
        "Food aboard is on the order of a kilogram per person per day. Four people through "
        "about 180 days is 4 \u00d7 180 = 720 kilograms of food, the better part of a tonne, "
        "before water. Water is the larger tank if it is not recycled. The chapter\u2019s tonne "
        "is that product. A torpor saving on the spreadsheet is logistics. It is not fewer "
        "heartbeats.",
        "A41",
    )
    gloss = (
        "Light-time. Delay at the speed of light. About 1.3 seconds to the Moon. Minutes to Mars (A1).\n"
        "Synodic period. How long you wait for the next cheap lineup. Earth and Mars, about 780 days.\n"
        "Hohmann transfer. The cheap ellipse between two orbits. Earth to Mars is on the order of six to nine months.\n"
        "Permanently shadowed region. A hollow the Sun does not reach. Cold enough for ice to persist. Not a well (A19).\n"
        "Solar particle event. A shove of protons on a scale of hours. Not the slow drizzle of galactic cosmic rays (A21).\n"
    )
    if "Light-time." not in text:
        anchor = "Torpor. A real, reversible drop in body temperature and metabolic rate. A slower clock, not a paused one."
        if anchor not in text:
            print("MISS glossary")
        else:
            text = text.replace(anchor, anchor + "\n" + gloss.strip())
            print("ADD glossary")
    src = (
        "Worked orders added with the classroom and body sums. A18\u2019s 336 kilowatt-hours "
        "is 1 kW \u00d7 14 \u00d7 24 h. A19\u2019s heat uses the specific heat of ice, about "
        "2 kJ kg\u207b\u00b9 K\u207b\u00b9, through about 200 K, plus the enthalpy of fusion, 334 kJ kg\u207b\u00b9. "
        "The crack uses an electrolyzer on the order of 50 kWh per kilogram of hydrogen and "
        "the 2/18 mass fraction of hydrogen in water. A28\u2019s decade at eighty is remaining "
        "life expectancy in the same period tables the note already uses for life expectancy "
        "at birth. A37\u2019s smallpox date is the World Health Assembly certification in 1980. "
        "A39\u2019s year 11900 is 1900 + 10,000. A41\u2019s food mass is on the order of 1 kg per "
        "person per day. These are orders, not a bid."
    )
    if "Worked orders added with the classroom" not in text:
        needle = "Global Polio Eradication Initiative situation reports (2026)."
        if needle not in text:
            print("MISS sources")
        else:
            text = text.replace(needle, needle + " " + src)
            print("ADD sources")
    save(path, text)

    path, text = load("00_Status.md")
    sentence = (
        " The same day, the second telling in the classroom chapters was cut, the rearview "
        "no longer hides the ratio in a nearer century, definition lines that began with "
        "\u201cwhere\u201d were turned into sentences, and the new sums were written into A17, A18, "
        "A19, A28, A37, A39, and A41."
    )
    if "definition lines that began" not in text:
        text = text.rstrip() + sentence + "\n"
        save(path, text)
        print("ADD status")
    else:
        print("HAVE status")

    print("--- leftovers ---")
    for fn in sorted(os.listdir(MAN)):
        if not fn.endswith(".md"):
            continue
        with open(os.path.join(MAN, fn), encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                s = line.strip()
                if s.lower().startswith("where ") or s.lower().startswith("*where"):
                    print(fn, n, s[:140])
    # confirm the bad year is gone
    with open(os.path.join(MAN, "09_Part_Nine_Not_A_Straight_Line.md"), encoding="utf-8") as f:
        body = f.read()
    print("3900s left", "3900s" in body)
    print("11900 present", "11900" in body)


if __name__ == "__main__":
    main()
