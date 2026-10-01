# -*- coding: utf-8 -*-
"""Fix the critical-review defects in Book 2. Delete this file after it runs."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
MAN = os.path.join(ROOT, "A Trip Is Not a New Life - Manuscript")
STAMP = (
    "The slide promotes the noun and crops the receipt. Look first: ask what was measured, "
    "what still needs Earth or a body, what the checklist still leaves empty."
)

CLOSERS = {
    "01_Part_One_Dirt_Delay_Dates.md": [
        "The slide shows a clean glove and a hero who is already outside. Look first: the heel on the seal, and the hour a station-class suit actually takes to put on.",
        "The slide shows a skyline and calls it a program. Look first: which panel has flown, which date moved, which loop still needs Earth.",
        "The slide prints a year and calls the gap beside it a scandal, or a destiny. Look first: announced, review, later. The work is the gap.",
    ],
    "02_Part_Two_The_Moon_First.md": [
        "The slide calls close a romance. Look first: a little over a second of light-time, a few days of coast, and the cargo that delay still invoices.",
        "The slide promotes a logo into a downtown. Look first: the capsule, the tip-over, the box of rock. Inventory is the rock.",
        "The slide puts a feeling in the window. Look first: occupied seats, a radio, and a splashdown the architecture was allowed to call a success.",
        "The slide prints a landable year and rents it a town. Look first: the suit, the dust, the leave, and the wrist that still has to bend.",
        "The slide draws one floor plan and calls the fight finished. Look first: which porch, which dirt, and which invoice the meeting still owes.",
        "The slide counts flags and calls the sum a biosphere. Look first: the sample that came home, and the station that is still a name.",
    ],
    "03_Part_Three_Vehicle_Not_City.md": [
        "The slide sells a decade and a dome. Look first: the window, the seven minutes, the six millibars, and the delay that has already finished the landing before the cheer arrives.",
    ],
    "04_Part_Four_Who_Stays.md": [
        "The slide crops the disk until the camp looks like the world. Look first: who stays, who waters the basil, and who is not on the ship.",
        "The slide offers a launch as a reset of the clocks. Look first: which pot the leaving does not touch.",
    ],
    "07_Part_Seven_Many_Clocks.md": [
        "The slide sells a dose as a new body. Look first: the hands, after the useful repair, still aging.",
        "The slide stretches the wall clock and calls the stretch health. Look first: the decade left at eighty, and how many of those mornings she would vote to repeat.",
        "The slide offers one knob for the kitchen. Look first: which five clocks stayed in the drawer.",
        "The slide says the name of a cutter and means everyone. Look first: this gene, this tissue, this invoice.",
    ],
    "08_Part_Eight_The_Organ.md": [
        "The slide offers a password to an unused ninety percent. Look first: the energy bill of an organ that is already on duty.",
        "The slide sells a spare mind. Look first: which tool gives back a lost function, and which tool promises a tank that was never there.",
        "The slide calls more years a wiser life. Look first: the same seek loop, on a longer calendar.",
    ],
    "09_Part_Nine_Not_A_Straight_Line.md": [
        "The slide lays a ruler on a stair. Look first: which flight finished, which nurse did not get cheaper, and which wall has a name.",
        "The slide multiplies fifty years by two hundred and prints a kitchen. Look first: the year 11900, and the furniture that method is not allowed to import.",
        "The slide waits, and calls the waiting a law of progress. Look first: the meeting, the ledger, and the door that did not open.",
    ],
}


def load(name):
    path = os.path.join(MAN, name)
    with open(path, encoding="utf-8") as f:
        return path, f.read()


def save(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)


def replace_para(text, start, new, label):
    i = text.find(start)
    if i < 0:
        print("MISS", label)
        return text
    j = text.find("\n\n", i)
    if j < 0:
        j = len(text)
    print("PARA", label)
    return text[:i] + new.strip() + text[j:]


def apply_closers(name, text):
    lines = CLOSERS.get(name)
    if not lines:
        return text
    n = text.count(STAMP)
    if n != len(lines):
        print("COUNT", name, "stamps", n, "closers", len(lines))
        return text
    for line in lines:
        text = text.replace(STAMP, line, 1)
    print("CLOSERS", name, len(lines))
    return text


def main():
    # phantom ending after chapter 33
    path, text = load("07_Part_Seven_Many_Clocks.md")
    phantom = (
        "Part II is the other cartoon: the cupboard in the skull. The hands still age. "
        "The organ was already on duty.\n"
        "Where the popular version goes wrong.\n"
        + STAMP + "\n"
        "Rule: Not a fountain. Modest further healthy years are warm; everyone shares them on a schedule is cold.\n"
    )
    if phantom not in text:
        print("MISS phantom")
    else:
        text = text.replace(phantom, "")
        print("CUT phantom")
    text = apply_closers("07_Part_Seven_Many_Clocks.md", text)
    save(path, text)

    for name in (
        "01_Part_One_Dirt_Delay_Dates.md",
        "02_Part_Two_The_Moon_First.md",
        "03_Part_Three_Vehicle_Not_City.md",
        "04_Part_Four_Who_Stays.md",
        "08_Part_Eight_The_Organ.md",
        "09_Part_Nine_Not_A_Straight_Line.md",
    ):
        path, text = load(name)
        text = apply_closers(name, text)
        if name.startswith("01"):
            text = replace_para(
                text,
                "The invented world Mara stands on",
                "The invented world Mara stands on is described in enough weighable detail "
                "\u2014 a butterscotch sky, a pressure you cannot breathe, a dead crust with an ice vein "
                "\u2014 that a careful reader could ask which real planet it is. This book will not answer, "
                "on purpose. Naming it would turn every detail into a claim about one survey. One-sixth of "
                "Earth\u2019s gravity is the Moon, and the Moon is named when this book is on the Moon. This camp "
                "does not get to borrow that number. The details here are the class of a close, dead, "
                "weighable world, not whichever site a program has circled this year.",
                "world",
            )
            text = replace_para(
                text,
                "The published record for actual suited egress times",
                "The published timeline for a station-class suit is not a hero\u2019s minute. Suit donning and "
                "the leak check, in NASA\u2019s EVA operations account, run on the order of an hour. Airlock "
                "egress, once the suit is already on, is about fifteen minutes. Pre-breathe is a separate "
                "clock and often longer. A poster shows a person already outside. Appendix A17 keeps the "
                "hour. Mara\u2019s single-minute target is what a fire wants. The suit we have actually flown "
                "does not grant it.",
                "egress",
            )
        if name.startswith("09"):
            old = "the squirrel clears it completely, and its neurons, which had pulled back their connections to survive the cold, regrow them past where they started."
            new = "a substantial part of that marker comes back down, site by site. It does not clear as one switch, and the connections the cold pulled back are not a therapy with a human dose."
            if old not in text:
                print("MISS squirrel clause")
            else:
                text = text.replace(old, new)
                print("fixed squirrel clause")
            old = "Hot: hibernating mammals genuinely reverse, within hours, brain changes that would read as severe disease in a human; targeted cooling has a real, narrow, evidence-supported role in specific acute injuries like cardiac arrest."
            new = "Hot: hibernating mammals raise, in torpor, a brain marker that would read as severe disease in a human, and bring a substantial part of it back down after arousal. That reversal is the squirrel\u2019s. Targeted cooling has a real, narrow role in specific acute injuries like cardiac arrest."
            if old not in text:
                print("MISS hot squirrel")
            else:
                text = text.replace(old, new)
                print("fixed hot squirrel")
        save(path, text)

    path, text = load("05_Part_Five_The_Classroom.md")
    text = text.replace(
        "That habitat wants several kilowatts if the crew is to stay warm, breathe, and keep a radio that can still call the ridge. Several kilowatts through the same fortnight is thousands of kilowatt-hours.",
        "She writes several kilowatts in pencil, for a habitat that would stay warm, breathe, and keep a radio that can still call the ridge. Pencil is not a measurement of a habitat she has weighed. Several kilowatts through the same fortnight, if the hearing accepts the pencil, is thousands of kilowatt-hours.",
    )
    text = replace_para(
        text,
        "Getting a tonne of ice from tens of kelvin",
        "Getting a tonne of ice from tens of kelvin up to a liquid is not the warm-kitchen product. "
        "Ice near melting holds about 2 kilojoules per kilogram per kelvin. Ice at tens of kelvin holds "
        "much less, so charging the whole climb at the warm number overstates the warming. The melt is "
        "the part she can write without that cheat: 334 kilojoules per kilogram, about 90 kilowatt-hours "
        "a tonne. Warming plus melt, with the cold heat capacity respected and the losses still unpaid, "
        "stays on the order of a hundred to a few hundred kilowatt-hours a tonne before anyone has cleaned "
        "it. The crack is the bill that shrinks the harbor: thousands of kilowatt-hours a tonne, then a "
        "liquefier that wants to be cold while the cracker wants to be hot, in a vacuum that will take "
        "whichever seal she neglects. The night in Chapter 18 has to supply those kilowatt-hours, or the "
        "drill is a sculpture. She writes both bills in the margin and watches the harbor shrink.",
        "ice",
    )
    if "Divided by 200, that is on the order of 1,700 kilograms" not in text:
        text = text.replace(
            "Appendix A18 writes the fortnight",
            "She prices the mass, because a kilowatt-hour is still a drawing until it has a weight.\n\n"
            "A battery pack of the class flown in this decade stores on the order of 200 watt-hours per "
            "kilogram once the cells sit in a box that can survive a launch. Three hundred and thirty-six "
            "kilowatt-hours is 336,000 watt-hours. Divided by 200, that is on the order of 1,700 kilograms "
            "for a single kilowatt through the fortnight, before the radiator and the spare. If the pencil "
            "says three kilowatts, the battery is several tonnes. Those tonnes are the spare pump and the "
            "drill Wei is still waiting to fly, unless the hearing chooses the reactor or the cable instead. "
            "She makes them write the displaced line on the same page as 336. A number with no mass beside "
            "it is the lamp again.\n\n"
            "Appendix A18 writes the fortnight",
        )
        print("ADD mass")
    if "divided by 1.37, is on the order of 440 days" not in text:
        text = text.replace(
            "Appendix A21 writes drizzle versus storm",
            "Jules writes the division where they eat, under the daily number.\n\n"
            "About 1,370 microsieverts a day is 1.37 millisieverts a day. A career line of order 600 "
            "millisieverts, divided by 1.37, is on the order of 440 days. An open-surface year is already "
            "most of that line, and the year has not yet included a storm. The 1,370 is the Chang\u2019e-4 "
            "far-side dosimeter from 2019, the reading Appendix A21 keeps. He will not let a slide say "
            "low when the division says a little over fourteen months to a line several agencies already "
            "treat as a career.\n\n"
            "The hat is not a vest and not a visor. A meter to a few meters of the dirt itself is mass "
            "that has to be piled before the weather. He times the walk from the valve to the bags. If "
            "that walk is longer than the warning the Sun actually gives, which can be a handful of hours "
            "and can be less, the bags are a caption on the far rim. He moves the bags. The move is a "
            "suit shift, spent on a quiet day.\n\n"
            "Appendix A21 writes drizzle versus storm",
        )
        print("ADD dose division")
    if "The ship is not on a road" not in text:
        text = text.replace(
            "Appendix A22 writes free return",
            "A U-turn is a word from a road. The ship is not on a road. It is on an ellipse the engines "
            "already paid for. Turning around means killing that ellipse and buying another, and the new "
            "one can drink more than finishing the fall already under way. That is why always is a lullaby "
            "once the ship is weeks toward Mars, and a checklist item only while the lunar path still falls "
            "home by itself. Jules draws the ellipse on the back of the card. He will not hear the word "
            "always until someone can point at the day the ellipse stops being the cheap path.\n\n"
            "Appendix A22 writes free return",
        )
        print("ADD ellipse")
    save(path, text)

    path, text = load("11_Appendix.md")
    text = replace_para(
        text,
        "Warming a tonne of ice from tens of kelvin",
        "The enthalpy of fusion of ice is 334 kilojoules per kilogram, about 93 kilowatt-hours per tonne. "
        "That number does not depend on pretending the ice was already warm. The specific heat near the "
        "melting point is about 2 kilojoules per kilogram per kelvin. It falls as the temperature falls, "
        "so a floor at tens of kelvin must not be warmed with 2 times 200 kelvin. That product, about "
        "110 kilowatt-hours per tonne, is a ceiling, not the integral. Warming plus melt, with the cold "
        "heat capacity respected, is on the order of a hundred to a few hundred kilowatt-hours per tonne "
        "before cleaning. Losses make it larger. Cracking the water is the bill that dominates. An "
        "electrolyzer is on the order of 50 kilowatt-hours per kilogram of hydrogen, and a tonne of water "
        "holds about 110 kilograms of hydrogen, so the crack is several thousand kilowatt-hours per tonne "
        "before the liquefier. The chapter\u2019s \u201chundreds\u201d are the heat with the cheat removed. The "
        "\u201cthousands\u201d are the crack.",
        "A19",
    )
    if "Suit donning and the leak check" not in text:
        text = text.replace(
            "\nA18. The Fortnight",
            "\nSuit donning and the leak check, in NASA\u2019s published EVA operations timeline for the "
            "station-class suit, run on the order of an hour. Airlock egress after the suit is on is "
            "about fifteen minutes. A camp drill that wants single minutes from alarm to a cycling airlock "
            "is wishing for a fire. It is not the overhead of the suit that has actually flown.\n\n"
            "A18. The Fortnight",
        )
        print("ADD donning")
    if "1,700 kilograms" not in text:
        text = text.replace(
            "\nA19. The Ratio",
            "\nAt a pack on the order of 200 watt-hours per kilogram, 336 kilowatt-hours is on the order "
            "of 1,700 kilograms of battery for one kilowatt through the fortnight, before structure and "
            "spares. A pencil assumption of several kilowatts is several tonnes. The tonnes are whatever "
            "else the ship does not get to carry. The several kilowatts are an assumption, not a weighed habitat.\n\n"
            "A19. The Ratio",
        )
        print("ADD A18 mass")
    text = replace_para(
        text,
        "Life expectancy at birth is not the years left",
        "Life expectancy at birth is not the years left to a woman already at eighty. The Social Security "
        "Administration\u2019s 2023 period life table, as used in the 2026 Trustees Report, gives a woman at "
        "exact age 80 about 9.8 years remaining. Japan\u2019s published life tables sit higher. The chapter\u2019s "
        "\u201cabout another decade\u201d is that order. It is not forty years, it is not 122, and it is not a "
        "promise written for one woman.",
        "A28",
    )
    text = replace_para(
        text,
        "Hibernator neuroscience:",
        "Hibernator neuroscience: in torpid arctic ground squirrels, brain tau protein is "
        "hyperphosphorylated at the sites Su and colleagues measured (Journal of Neurochemistry, 2008). "
        "On arousal, some of those sites come back down and some do not. That is a partial reversal in "
        "an animal built for the winter, not a complete clearance on a human clock, and not a result in "
        "a human. Dendritic change in hibernators is the same class of fact: the animal\u2019s, unfinished "
        "as a prescription. No human data exist on transfer. Humans are not adapted hibernators.",
        "tau",
    )
    old = "hibernators fully reverse, in hours, a brain change that would read as severe disease in a human."
    new = "hibernators raise that marker in torpor and bring only a substantial part of it down after arousal."
    if old not in text:
        print("MISS hot-list tau")
    else:
        text = text.replace(old, new)
        print("fixed hot-list tau")
    old = (
        "For Chapter 41 (torpor and slowed metabolism): the NASA-funded Studying Torpor in Animals for "
        "Space-Health in Humans (STASH) program, for the current state of induced-torpor research. "
        "H. Nielsen and colleagues, \u201cTargeted Temperature Management for Cardiac Arrest with Nonshockable "
        "Rhythm,\u201d New England Journal of Medicine 381 (2019). The TTM2 trial, NEJM Evidence 1 (2022), for "
        "the largest and most recent reappraisal. Any review of arctic ground squirrel tau-protein "
        "reversibility during hibernation, for the hibernator-neuroscience result."
    )
    new = (
        "For Chapter 41 (torpor and slowed metabolism): the NASA-funded Studying Torpor in Animals for "
        "Space-Health in Humans (STASH) program, for the current state of induced-torpor research. "
        "J. Lascarrou and colleagues, \u201cTargeted Temperature Management for Cardiac Arrest with Nonshockable "
        "Rhythm,\u201d New England Journal of Medicine 381 (2019), 2327\u20132337. J. Dankiewicz and colleagues, "
        "\u201cHypothermia versus Normothermia after Out-of-Hospital Cardiac Arrest,\u201d New England Journal of "
        "Medicine 384 (2021), 2283\u20132294, the TTM2 trial, intention-to-treat population 1,861. B. Su and "
        "colleagues, \u201cPhysiological regulation of tau phosphorylation during hibernation,\u201d Journal of "
        "Neurochemistry 105 (2008), for the arctic-ground-squirrel sites that rise in torpor and only "
        "partly come down on arousal."
    )
    if old not in text:
        print("MISS sources 41")
    else:
        text = text.replace(old, new)
        print("fixed sources 41")
    if "9.8 years" not in text.split("Worked orders")[-1]:
        needle = "A28\u2019s decade at eighty is remaining life expectancy in the same period tables the note already uses for life expectancy at birth."
        repl = (
            "A28\u2019s decade at eighty is the Social Security Administration 2023 period life table "
            "(2026 Trustees Report): about 9.8 years remaining for a woman at exact age 80. Japan\u2019s "
            "published tables sit higher."
        )
        if needle not in text:
            print("MISS worked A28")
        else:
            text = text.replace(needle, repl)
            print("fixed worked A28")
    if "station-class suit donning" not in text:
        needle = "These are orders, not a bid."
        repl = (
            "A17\u2019s hour is NASA\u2019s published EVA operations timeline: station-class suit donning and "
            "leak check on the order of 60 minutes, airlock egress about 15 minutes once the suit is on. "
            "These are orders, not a bid."
        )
        if needle not in text:
            print("MISS orders closer")
        else:
            text = text.replace(needle, repl, 1)
            print("fixed orders closer")

    gloss = """Glossary
One list, alphabetical after the three nouns the book is built on. The camp and the body share the words.

Sortie. Go, work, come home \u2014 or die on a schedule Earth still owns.
Outpost. A season with an umbilical.
Settlement. The umbilical can fail and the babies still eat.

Additionality. In carbon-offset accounting, whether a credited reduction would have happened anyway without the payment. A large share of audited forest-offset credits have failed this test (A15).
Anchoring. A cognitive bias in which a first-guessed number, often an arbitrary round one, distorts every later estimate even after everyone involved knows the first number was arbitrary (A3). A useful lens for reading any year that ends in a zero.
Avcoat. The ablative heat-shield material flown on Apollo and on the current crew capsule; it protects by charring and shedding material, on purpose, which is why char loss is data, not automatically a defect (A2, A6).
Cargo-cult test. Seven loops \u2014 air, water, calories, power, medicine, spares, law \u2014 scored separately. Headcount is not a loop. Borrowed, narrowly, from a mid-twentieth-century anthropological term describing Pacific Island communities that mimicked the form of a wartime supply operation after it departed; this book uses only the later engineering sense \u2014 a system that copies a working system\u2019s appearance without its actual supply \u2014 not the anthropology, which is a more complicated and more respectful conversation than a glossary entry can hold.
Carrot. A seek loop with no off-switch labeled picture only. More calendar does not install the switch (A36).
EDL. Entry, descent, landing \u2014 the seven-minutes-of-terror span (A11) during which a spacecraft is on its own, because light-time makes real-time control from Earth physically impossible.
File. A map. Not a worldline.
Free return. A translunar path that falls home with no further burn. A path already left is not this path until a burn puts you back on it (A22).
HALE. Healthy life expectancy: years with disability weighted out. Not the pulse on the wall. Healthspan, below, is the plain-language twin of the same idea (A28).
Hallmarks. A review\u2019s list of aging mechanisms. A list, not a fuse (A29).
Healthspan. Years you would vote to repeat. HALE is the demographer\u2019s weighted version of this sentence (A28).
Helium. In this series, a cold product sold as already on the dock: a scheduled immortality, a downtown by Friday, a spare mind, a straight line to furniture nobody can name.
Hohmann transfer. The cheap ellipse between two orbits. Earth to Mars is on the order of six to nine months.
Hot, warm, cold. Established; a working account with real gaps; speculation sold as inventory.
ISRU. In-situ resource utilization. Make the kitchen there. Not a city charter.
Kessler cascade. A chain reaction in which orbital debris from one collision causes further collisions, producing more debris, first described in a 1978 paper and increasingly cited as launch cadence rises (A16).
Light-time. Delay at the speed of light. About 1.3 seconds to the Moon. Minutes to Mars (A1).
Local fix. This gene, this tissue, this bill.
Maximal aging. Between two events, the unpushed path reads the most; a bend reads less.
Methalox. Liquid methane and liquid oxygen, the propellant pair behind the reuse economics and the in-situ-fuel ambitions this book\u2019s Part III keeps returning to (A10).
Negligible senescence. A hazard of death that stays flat past maturity. Not zero. Not immortal.
Non-appropriation. The 1967 rule that no nation may claim the Moon as territory. Use is not title. The clause does not contain this book\u2019s three nouns (A23).
Normalization of deviance. A pattern in which a program that survives ignoring a warning sign once begins treating that sign as acceptable risk, repeatedly, until the accumulated acceptances produce a failure nobody individually chose (A2).
NRHO. Near-rectilinear halo orbit. A porch, not a law.
Partial reprogramming. A nudge back toward a cell\u2019s younger markings, stopped short of the door marked identity lost.
Permanently shadowed region. A hollow the Sun does not reach. Cold enough for ice to persist. Not a well (A19).
Pre-breathe. The wait on a lower-pressure oxygen suit, so dissolved nitrogen does not come out of the blood as bubbles (A17).
Proper time. The time a clock reads along its own path. The only clock a body ever keeps.
Regolith. Broken rock and dust on a surface with no air to round it and no rain to wash the charge off (A20).
S-curve. Slow, drunk, wall.
Sievert. A dose weighted for biological harm. A thousandth is a millisievert. The open-surface reading in this book, about 1,370 microsieverts a day, is about half a sievert a year if you multiply (A4, A21).
Slip. A moved official date. Invoice, not destiny, not automatically fraud.
Solar particle event. A shove of protons on a scale of hours. Not the slow drizzle of galactic cosmic rays (A21).
Synodic period. How long you wait for the next cheap lineup. Earth and Mars, about 780 days.
Torpor. A real, reversible drop in body temperature and metabolic rate. A slower clock, not a paused one. Not a longer life (A41).
Window. An alignment you do not vote off.
"""
    i = text.find("\nGlossary\n")
    if i < 0:
        print("MISS glossary")
    else:
        text = text[:i + 1] + gloss
        print("WROTE glossary")
    save(path, text)

    path, text = load("00_Status.md")
    sentence = (
        " On 30 September 2026 the repeated chapter-exit paragraph was rewritten for each chapter, "
        "the stray ending after Chapter 33 was removed, the ice warming sum stopped using warm-ice "
        "heat capacity at tens of kelvin, the station-class suit donning hour replaced the unsourced "
        "several minutes, remaining life at eighty was tied to the Social Security Administration 2023 "
        "period life table, and the torpor note now cites Dankiewicz 2021, Lascarrou 2019, and Su 2008."
    )
    if "stray ending after Chapter 33" not in text:
        text = text.rstrip() + sentence + "\n"
        save(path, text)
        print("ADD status")

    print("--- stamp left ---", end=" ")
    n = 0
    for fn in os.listdir(MAN):
        if not fn.endswith(".md"):
            continue
        with open(os.path.join(MAN, fn), encoding="utf-8") as f:
            c = f.read().count(STAMP)
        if c:
            print(fn, c)
            n += c
    print("total", n)
    with open(os.path.join(MAN, "07_Part_Seven_Many_Clocks.md"), encoding="utf-8") as f:
        body = f.read()
    print("phantom left", "Part II is the other cartoon" in body)


if __name__ == "__main__":
    main()
