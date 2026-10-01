# -*- coding: utf-8 -*-
"""Apply the 30 Sep 2026 critical-review repairs to Book 2. One-shot."""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
MAN = os.path.join(ROOT, "A Trip Is Not a New Life - Manuscript")
A = "\u2019"  # curly apostrophe
KEEP_RULE = {3, 9, 12, 16, 33, 36, 42, 46}
misses = []

def load(name):
    path = os.path.join(MAN, name)
    with open(path, encoding="utf-8") as f:
        return path, f.read()

def save(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)

def sub(text, pattern, repl, label, flags=re.S, count=1):
    new, n = re.subn(pattern, repl, text, count=count, flags=flags)
    if n != count:
        misses.append(f"{label} ({n}/{count})")
        print("MISS", label, n)
    else:
        print("OK", label)
    return new

def strip_hymns(text, fname):
    parts = re.split(r"(?=^## \d+\.)", text, flags=re.M)
    out = []
    for part in parts:
        m = re.match(r"## (\d+)\.", part)
        if not m or "Where the popular version goes wrong." not in part:
            out.append(part)
            continue
        n = int(m.group(1))
        if n in KEEP_RULE:
            part2, k = re.subn(
                r"\n*Where the popular version goes wrong\.\n.*?(?=Rule:)",
                "\n",
                part,
                count=1,
                flags=re.S,
            )
            print(f"RULE-KEEP {fname} ch{n}" if k else f"MISS rule-keep {fname} ch{n}")
            if not k:
                misses.append(f"rule-keep {fname} ch{n}")
            out.append(part2)
        else:
            part2, k = re.subn(
                r"\n*Where the popular version goes wrong\.\n*?Rule:[^\n]*\n?",
                "\n",
                part,
                count=1,
                flags=re.S,
            )
            # the regex above is wrong if I typed \n*? — fix below if miss
            if not k:
                part2, k = re.subn(
                    r"\n*Where the popular version goes wrong\.\n.*?Rule:[^\n]*\n?",
                    "\n",
                    part,
                    count=1,
                    flags=re.S,
                )
            print(f"HYMN-CUT {fname} ch{n}" if k else f"MISS hymn {fname} ch{n}")
            if not k:
                misses.append(f"hymn {fname} ch{n}")
            out.append(part2)
    return "".join(out)

# ---------- front matter ----------
path, text = load("00_Front_Matter.md")
text = sub(
    text,
    r"A temperature can change\.",
    "Helium, in this book, is a cold product sold as if it were already on the dock: a scheduled immortality, a downtown by Friday, a spare mind, a straight line to furniture nobody can name. A hearing aid is not helium. A vaccine is not helium. A sickle-cell-class edit is not helium. Those are tools, and tools have invoices. Helium is what a slide asks you to wait for instead.\n\nA temperature can change.",
    "helium-front",
)
text = sub(
    text,
    r"a woman on a Mars-like dead world",
    "a woman on Mars",
    "mars-like",
    flags=0,
)
save(path, text)

# ---------- chapter 1 ----------
path, text = load("01_Part_One_Dirt_Delay_Dates.md")
text = sub(
    text,
    r"This is the only honest picture of .somewhere else. this book will allow in the near term\. A dead world,",
    "This is the only honest picture of somewhere else this book will allow in the near term. The world is Mars. A dead world,",
    "name-mars-early",
)
text = sub(
    text,
    r"Light to this world:",
    "Light to Mars:",
    "light-mars",
    flags=0,
    count=1,
)
text = sub(
    text,
    r"She has a sister in a real kitchen, on a genuine coast, who still thinks .we. includes a ticket\. The sister will not get a ticket\. Almost no one will\.",
    "She has a sister, Priya, who runs a clinic on a genuine coast and still thinks \u201cwe\u201d includes a ticket. Priya will not get a ticket. Almost no one will. What Priya wants is smaller than a species-move: a fridge that holds its temperature, a surgeon who shows up for the operation already on her board, and a Tuesday in which her own hands can still open a jar. She has written Mara about the date. The answer has not come back.",
    "priya-ch1",
)
text = sub(
    text,
    r"A word on why the kitchen never gets a name\.\nThe invented world Mara stands on.*?circled this year\.",
    "The kitchen has a name. It is Mars.\n\nA butterscotch sky, a pressure you cannot breathe, a sol of about twenty-four hours and forty minutes, a cheap path home about every twenty-six months, perchlorate in the fines, a one-way radio between about three minutes and about twenty-two: those are Mars measurements. This book will not peel the label off to sound more general. Sites and official years will move. The class will not. One-sixth of Earth" + A + "s gravity is the Moon, and the Moon is named when this book is on the Moon. This camp does not borrow that number. Mara is invented. Mars is not.",
    "name-mars-late",
)
save(path, text)

# ---------- who stays: second tellings, Priya, lowercase ----------
path, text = load("04_Part_Four_Who_Stays.md")
text = sub(
    text,
    r"Mara" + A + r"s sister, in the real kitchen, uses we",
    "Priya, Mara" + A + "s sister, runs a clinic on the coast and uses we",
    "priya-ch13",
    flags=0,
)
text = sub(
    text,
    r"They are Rohan" + A + r"s mother" + A + r"s street, and the tide gauge, and the sister who still says we\.",
    "They are Rohan" + A + "s mother" + A + "s street, and the tide gauge, and Priya, who still says we.",
    "priya-dead",
    flags=0,
)
text = sub(
    text,
    r"Mara" + A + r"s sister asked, in a message that took the long way, whether the planet would be nicer when the ambitious had gone\. Mara did not vote\. She wrote the only sentence that is allowed to be hot: most of us are still there, and the clocks do not care about the ship\.\n",
    "",
    "cut-early-sister",
    flags=0,
)
text = sub(
    text,
    r"Collapse is not a broom\..*?(?=The arithmetic, run with real numbers)",
    "",
    "cut-ch15-echo",
)
text = sub(
    text,
    r"Mara" + A + r"s sister, and the sentence that is allowed to be hot\.\nThe message that took the long way to reach her asks, in essence, whether the planet will be nicer once the ambitious have gone\. Mara has run the arithmetic in this chapter in her own head, on slower nights, with the numbers she can remember from her training\. She does not have the tide gauge or the orbital simulations\. She has enough of the shape of the answer to write one honest sentence back, and she writes it: the ambitious are a rounding error, and the planet does not know we left\. Her sister does not entirely believe her, at first\. The sentence is true regardless of whether it is believed\. That is what makes it hot\.",
    "Priya, and the sentence that is allowed to be hot.\n\nThe message that took the long way asks whether the planet will be nicer once the ambitious have gone. Mara has the shape of the answer and not the tide gauge. She writes one sentence: the ambitious are a rounding error, and the planet does not know we left. Priya does not entirely believe her. The sentence is true whether it is believed. That is what makes it hot. Priya will not get a ticket. She still has a clinic, a fridge, and a surgery date that has not yet answered.",
    "priya-scene-15",
)
text = sub(
    text,
    r"What a finished reader keeps, one more time, so the spine can close without a downtown:.*?The orbits will not vote for a downtown\.\n",
    "",
    "cut-ch16-echo",
)
text = sub(
    text,
    r"the tide gauge, Rohan" + A + r"s mother" + A + r"s street, Mara" + A + r"s sister" + A + r"s oven:",
    "The tide gauge, Rohan" + A + "s mother" + A + "s street, Priya" + A + "s oven:",
    "lowercase-tide",
    flags=0,
)
text = sub(
    text,
    r"A later book, if you want it, will keep her hands and refuse helium\. You do not need it\. You can stop here\.",
    "The next chapters keep her hands and refuse helium. You can also stop here.",
    "later-book",
    flags=0,
)
save(path, text)

# ---------- long ticket ----------
path, text = load("06_Part_Six_The_Long_Ticket.md")
text = sub(
    text,
    r"\nWill the first eat the species that built it\?.*?(?=\nThe greenhouse woman)",
    "\n",
    "cut-mind-seminar",
)
text = sub(
    text,
    r"The nest is also a picture of a mind that is not in the worker\..*?already warned\.\n",
    "The nest is the scale, not a theory of mind. To a crew that crossed a century, an ape city may be that nest: organized at its own size, not a colleague. You meet it by being the wrong size, or by pouring. Whether a machine can be a someone is the other book" + A + "s unfinished fight. This chapter keeps the box shut until the sea has been tasted.\n",
    "trim-nest",
)
save(path, text)

# ---------- chapter 27 ----------
path, text = load("07_Part_Seven_Many_Clocks.md")
new27 = """## 27. Her Hands Still Age

The same glove. A new invoice.

Mara""" + A + """s airlock still sticks. She already hit it, in Chapter 1, and the seal already sighed. What arrives on the delay this morning is a capsule. The label is optimistic. A small paragraph about support and maintenance and a season that can still be used. Her hands are not optimistic. The knuckles have begun to look like a map of a place she has already walked. The joint that used to open a jar without a thought now asks for a meeting.

She takes the dose because a joint that still works is a local win, and local wins are the only kind biology has ever reliably sold. She does not become a different species. She names the basil, which is sentimental, and logs the pH, which is not. On Mars, sentiment is allowed as long as it does not get to vote.

Figure 27. Working hands over a basil tray in hard light; a plain blister at the edge. The dose is local. The hands are still the hands.

Worldwide, on the most recent count anyone has bothered to run properly, something like 595 million people carry osteoarthritis in some joint, and roughly 194 million of those cases sit in the hands specifically. Hers is not a rare complaint. It is one of the most common diagnoses a human body ever files. A human joint is cartilage, bone, a little sac of fluid, a staff of cells that keep a surface honest. The staff gets worse at the job. Inflammation writes graffiti. The surface pits. Pain is not a metaphor. Pain is a measurement the nervous system makes and will not stop making because a label was optimistic. A drug that lowers the graffiti, or a lubricant the body will accept, or a replacement that a surgeon can bolt in, is a local win. Local is the word that has to sit still.

Local means this tissue, this season, this invoice. It does not mean a reset of the house.

The same woman still copies DNA with a small error rate. She still shortens the little caps on the ends of chromosomes, the long strands of coiled DNA inside a cell, in the lineages that divide. She still runs mitochondria that leak and forget. She still keeps an immune system that has learned too many grudges and forgotten some of its tact. She still accumulates cells that refuse to die and then spoil the room. She still wears grooves in a brain that has been on duty since the first language she learned. Chapter 29 is those clocks. This chapter is the refusal to let one useful dose pretend it wound them all back.

Temperatures, and the word helium, are already in How to Read. Use them on the capsule. A useful season is not helium. A sermon that calls the dose the first day of a new species is helium. Put the sermon down and keep the joint, if the joint is what she paid for. Priya""" + A + """s hands, on the coast, are starting to ask for the same kind of meeting. The letter about that meeting is still ahead of her.

Appendix A27 writes what \u201clocal\u201d has to mean when a pharmacist and a marketer share a noun. Here, keep the hands. They still age. That is the first hot fact. Everything colder will have to walk past it.

"""
text2, n = re.subn(
    r"## 27\. Her Hands Still Age\n.*?Rule: Hands still age after a useful dose\. Take the local win\. Put helium down\.\n",
    new27,
    text,
    count=1,
    flags=re.S,
)
print("OK ch27" if n == 1 else "MISS ch27")
if n != 1:
    misses.append("ch27")
else:
    text = text2
save(path, text)

# ---------- ch 38 and 42 ----------
path, text = load("09_Part_Nine_Not_A_Straight_Line.md")
text = sub(
    text,
    r"\nA drug that worked in Phase 3 is a drunk middle for the people who got it\. The leftover — not eligible, rare harm in Phase 4, a zip code without a trial site — is the shoulder of the curve\. Founders photograph the middle\. Keep the shoulders\. Middles are temporary\. Name the wall or you bought a ray\. Sequencing dollars collapsed while the act — this letter, this tissue, this trial — kept invoices\. Moore" + A + r"s middle was a factory calendar and a voltage that behaved; when the voltage stopped, the sermon did not apologize\. Compute bent when watts stopped being polite; parallelism is a new S, not the old ray in a hat\. Ask for the wall" + A + r"s address, cost, energy, regulation, attention, war\. Keep the S\. Cash the middle only as a middle\.\n",
    "\n",
    "cut-ch38-echo",
    flags=0,
)
text = sub(
    text,
    r"A loop is Chapter 38" + A + r"s three nouns, and this chapter" + A + r"s meeting\.",
    "A loop is Chapter 12" + A + "s seven rows, and this chapter" + A + "s meeting.",
    "ptr-38",
    flags=0,
)
text = sub(
    text,
    r"The slip is Chapter 29; a moved year is a meeting, not a destiny\.",
    "The slip is Chapter 3; a moved year is a meeting, not a destiny.",
    "ptr-29",
    flags=0,
)
text = sub(
    text,
    r"Four walls that are not chips, spoken slowly enough to keep\..*?(?=Appendix A42)",
    "",
    "cut-ch42-echo",
)
text = sub(
    text,
    r"Part IV is the invoices on the body itself:",
    "Part X is what is still on the counter:",
    "ptr-part",
    flags=0,
)
save(path, text)

# ---------- ch 43 and 45 ----------
path, text = load("10_Part_Ten_The_Honest_Body.md")
text = sub(
    text,
    r"and she does not become a proof that her sister will get the same dose\.\nHer sister" + A + r"s name is Priya, and the letter that comes in on the same downlink as everything else says the trial two ferries from her clinic closed enrollment before her scans came back\. Not a villain\. A number: the study needed a narrower biology than hers, and narrower biology fills faster in a city with three hospitals feeding it than in a coastal clinic with one\. Priya will get, if she is lucky, the boring wins instead: a blood-pressure pill that has existed since before Mara was born, a vaccine that already exists, a surgeon who can still be afforded because the operation is not the one on the poster\. Mara reads the letter twice before she answers it, because the honest answer is that a local fix bought for a joint on a dead world and a local fix that closed enrollment on a coast are two ends of the same invoice, and the ledger did not ask either of them what they would have voted for\. Boring is hot\. Helium is cold\. She writes back the only true thing she has: that she is glad Priya still has the surgeon, and sorry that gladness is the whole of what she can send on a fifteen-minute delay\.",
    "and she does not become a proof that Priya will get the same dose.\nPriya already has a name. The letter on this downlink says the trial two ferries from her clinic closed enrollment before her scans came back. Not a villain. A number: the study needed a narrower biology than hers, and narrower biology fills faster in a city with three hospitals than in a clinic with one. What remains on her board is the boring operation, the one for the hands, still scheduled, still waiting on a surgeon who can be afforded because the operation is not the one on the poster. Mara writes back that she is glad the surgeon is still on the board, and sorry that gladness is the whole of what a late radio can send.",
    "priya-letter-43",
)
text = sub(
    text,
    r"A morning in the clinic, without a founder" + A + r"s font\.\nRohan sits with a family while Mara" + A + r"s capsule paperwork is still a rumor on a delay\. The wall has a photograph of a win\. The desk has a stack that says not eligible in a font designed to look neutral\. He does not lie\. He names the three clocks: the biology that did not match the protocol, the geography that put the trial two ferries away, the insurance word that turned a molecule into a rumor\. The family wanted a downtown\. They leave with a blood-pressure pill that already exists and a surgeon" + A + r"s name that can still be afforded\. Boring\. Hot\. The photograph on the wall does not get to vote\.",
    "A morning in the clinic, without a founder" + A + "s font.\nPriya opens the fridge before she opens the mail. The vaccine that already exists is only a vaccine if the temperature log stayed inside its band overnight. She writes the number. Then she sits with the family the trial did not choose. The wall has a photograph of a win. The desk has a stack that says not eligible. She does not lie. She names the three clocks: the biology that did not match the protocol, the geography that put the trial two ferries away, the insurance word that turned a molecule into a rumor. The family wanted a downtown. They leave with a blood-pressure pill that already exists. Priya" + A + "s own hands stay on the desk after they go. The knuckles have started to look like her sister" + A + "s. The boring surgery is still on the board. She wants the surgeon to show up, the anesthesia to hold, and a hallway she can walk. She does not want a fountain. She writes Mara anyway. The letter will take its day and a half. Chapter 46 is the answer, if the surgeon comes.",
    "priya-morning",
)
text = sub(
    text,
    r"already emptied in Part II",
    "already emptied in Chapter 34",
    "part-ii-mind",
    flags=0,
)
text = sub(
    text,
    r"Mara" + A + r"s kindness to herself is practical\..*?(?=Appendix A45)",
    "",
    "cut-ch45-echo",
)
save(path, text)

# ---------- appendix ----------
path, text = load("11_Appendix.md")
text = sub(
    text,
    r"A19" + A + r"s heat uses the specific heat of ice, about 2 kJ kg⁻¹ K⁻¹, through about 200 K, plus the enthalpy of fusion, 334 kJ kg⁻¹\.",
    "A19" + A + "s heat does not charge ice at tens of kelvin with the warm specific heat. The enthalpy of fusion is 334 kJ kg⁻¹, about 93 kilowatt-hours per tonne. Specific heat near melting, about 2 kJ kg⁻¹ K⁻¹, times about 200 K is a ceiling of about 110 kilowatt-hours per tonne, not the integral, because heat capacity falls as the ice gets colder.",
    "ice-blurb",
    flags=0,
)
camp = (
    "Start here, as entries a reader can find.\n\n"
    "S. Zhang and colleagues, \u201cFirst measurements of the radiation dose on the lunar surface,\u201d Science Advances 6 (2020), eaaz1334. Chang"
    + A + "e-4" + A + "s lunar dosimeter: about 1,369 microsieverts a day.\n"
    "NASA, Artemis II: launched 1 April 2026, splashdown 10 April 2026. Crew: Reid Wiseman, Victor Glover, Christina Koch, Jeremy Hansen. A status page will move. The flown class will not.\n"
    "NASA EVA operations timelines for a station-class suit: donning and leak check on the order of 60 minutes; airlock egress about 15 minutes once the suit is on. Pre-breathe is a separate, often longer clock (A17).\n"
    "Social Security Administration, 2023 period life table, published with the 2026 Trustees Report: a woman at exact age 80 has about 9.8 years remaining (table value 9.82). Japan"
    + A + "s published tables sit higher (A28).\n"
    "Rogers Commission, Report of the Presidential Commission on the Space Shuttle Challenger Accident (1986).\n"
    "Diane Vaughan, The Challenger Launch Decision (University of Chicago Press, 1996), for normalization of deviance.\n"
    "Treaty on Principles Governing the Activities of States in the Exploration and Use of Outer Space, including the Moon and Other Celestial Bodies (1967), Article II: no national appropriation. The clause does not contain sortie, outpost, or settlement (A23).\n"
    "IPCC assessment reports, carbon-cycle chapters, for the pulse and the tail (A14). NASA GRACE and GRACE-FO, for ice-sheet mass.\n"
    "Biosphere 2, the 1991\u20131993 closed-ecosystem test. Read the oxygen and soil-microbe failure, not only the summary (A12).\n"
    "Donald J. Kessler and Burton G. Cour-Palais, \u201cCollision frequency of artificial satellites: The creation of a debris belt,\u201d Journal of Geophysical Research 83 (1978), 2637\u20132646.\n"
    "The torpor papers (Dankiewicz 2021, Lascarrou 2019, Su 2008) are cited in full under the body sources below, so a reader checking the life-table and the squirrel claim can find them without panning a paragraph.\n\n"
)

text = sub(
    text,
    r"Start here\. A current public NASA/Artemis or CNSA status page.*?because the pattern is not specific to rockets\.\n",
    camp,
    "camp-bib",
)
text = sub(
    text,
    r"S-curve\. Slow, drunk, wall\.",
    "S-curve. A slow start, a steep middle, and a wall where the next gain costs more than the last. The steep middle is not a law (A38).",
    "gloss-s",
    flags=0,
)
text = sub(
    text,
    r"Carrot\. A seek loop with no off-switch labeled picture only\. More calendar does not install the switch \(A36\)\.",
    "Carrot. The seek loop that treats a cue as a feast and has no off-switch on the hiring plan. More years on the calendar do not install the switch (A36).",
    "gloss-carrot",
    flags=0,
)
text = sub(
    text,
    r"File\. A map\. Not a worldline\.",
    "File. A record. A map of a walk is not the walk, and a copy that wakes sure it is you did not travel (A45).",
    "gloss-file",
    flags=0,
)
text = sub(
    text,
    r"Helium\. In this series, a cold product sold as already on the dock: a scheduled immortality, a downtown by Friday, a spare mind, a straight line to furniture nobody can name\.",
    "Helium. A cold product sold as already on the dock: a scheduled immortality, a downtown by Friday, a spare mind, a straight line to furniture nobody can name. Defined in How to Read. Tools with invoices are not helium.",
    "gloss-he",
    flags=0,
)
save(path, text)

# ---------- hymns on every popular part ----------
for fname in [
    "01_Part_One_Dirt_Delay_Dates.md",
    "02_Part_Two_The_Moon_First.md",
    "03_Part_Three_Vehicle_Not_City.md",
    "04_Part_Four_Who_Stays.md",
    "07_Part_Seven_Many_Clocks.md",
    "08_Part_Eight_The_Organ.md",
    "09_Part_Nine_Not_A_Straight_Line.md",
    "10_Part_Ten_The_Honest_Body.md",
]:
    path, text = load(fname)
    text = strip_hymns(text, fname)
    save(path, text)

# ---------- status ----------
path, text = load("00_Status.md")
note = " On 30 September 2026 a later pass named Mara" + A + "s camp as Mars, named her sister Priya in Chapter 1 and gave Priya a clinic morning in Chapter 43, retired the repeated chapter-exit hymn except one Rule at the end of each part that had one, cut the mind seminar out of Chapter 25, removed the second tellings in Chapters 15, 16, 27, 38, 42, and 45, corrected the Chapter 42 pointers, and made the worked-numbers ice line obey A19."
if "named Mara" not in text and "named her sister Priya" not in text:
    if not text.endswith("\n"):
        text += "\n"
    # append to the Not done paragraph (last paragraph)
    text = text.rstrip() + note + "\n"
    print("OK status")
else:
    print("SKIP status already")
save(path, text)

print("---")
print("MISSES", len(misses))
for m in misses:
    print(" -", m)
