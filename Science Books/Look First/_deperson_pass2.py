"""Second deperson pass: remaining first names + popular-text Penrose noise."""
from pathlib import Path
import re

ROOTS = [
    Path(r"D:\My Books for Amazon\Science Books\Look First\A Trip Is Not a Settlement - Manuscript"),
    Path(r"D:\My Books for Amazon\Science Books\Look First\A Longer Life Is Not a New Body - Manuscript"),
    Path(r"D:\My Books for Amazon\Science Books\Look First\The Universe Has No Now - Manuscript"),
]

REPLACEMENTS = [
    # Elena — full intro + leftovers
    ("Elena Voss runs reviews for a living. She is invented. The room she sits in is not. Fluorescent light, a table that has heard too many dates, a wall with a patch that used to be last year’s milestone and is now this year’s “replan.” She has a rule she does not write on the slides: if it has not flown, it is a story with a purchase order. If it has flown once, it is a dare. If it has flown until the news stopped covering it, it is beginning to be a truck.",
     "Reviews run for a living. The room is not invented. Fluorescent light, a table that has heard too many dates, a wall with a patch that used to be last year’s milestone and is now this year’s “replan.” The rule that does not get written on the slides: if it has not flown, it is a story with a purchase order. If it has flown once, it is a dare. If it has flown until the news stopped covering it, it is beginning to be a truck."),
    ("Elena keeps a rule for the room that photographs badly:",
     "The review keeps a rule for the room that photographs badly:"),
    ("Elena keeps a slide of her own for this, and it is the only one she shows in every review. It has two columns. On the left: *awarded*. On the right: *flown*. The left column is long and has good logos on it. The right column is short and has scorch marks. She does not say the left column is a lie. She says it is a list of ovens that have been switched on. The roast is in the right column, when it is anywhere.",
     "Every review keeps one slide of its own. It has two columns. On the left: *awarded*. On the right: *flown*. The left column is long and has good logos on it. The right column is short and has scorch marks. The left column is not a lie. It is a list of ovens that have been switched on. The roast is in the right column, when it is anywhere."),
    ("Elena asks for the card. The vendor says *flight*. The room waits. The vendor says *test*. Elena nods, and moves the ladder and the flag and the dirt to a different slide, the one labeled *what this would be if the tank held for a season*. Then she asks about the engines that have to light in a well with no air, about the leg that has to find a slope, about the pour that has to happen in orbit before any of this is a landing, and the vendor answers each honestly: article, contract, rendering. Nobody is fired. The year goes from a landing gear to a mood. The lander is still worth building. It is just not yet a lander.",
     "The review asks for the card. The vendor says *flight*. The room waits. The vendor says *test*. The ladder and the flag and the dirt move to a different slide, the one labeled *what this would be if the tank held for a season*. Then the engines that have to light in a well with no air, the leg that has to find a slope, the pour that has to happen in orbit before any of this is a landing — and the vendor answers each honestly: article, contract, rendering. Nobody is fired. The year goes from a landing gear to a mood. The lander is still worth building. It is just not yet a lander."),
    ("Elena puts three cards on the table. SORTIE. OUTPOST. SETTLEMENT. She asks the room to point at the hardware on the slide and pick one card. If two fingers twitch, she waits. If someone says “it’s a journey,” she asks them to put the journey down and pick a card. Journeys are how nouns get married in the dark.",
     "Three cards on the table. SORTIE. OUTPOST. SETTLEMENT. Point at the hardware on the slide and pick one card. If two fingers twitch, wait. If someone says “it’s a journey,” put the journey down and pick a card. Journeys are how nouns get married in the dark."),
    ("She is glad for Dex, whom she has not met.",
     "She is glad for whoever keeps the cadence board, whom she has not met."),
    ("Pavel will not put a kettle on a slide that also has a child. He will put the kettle on a slide that has a dosimeter and a mass.",
     "The EDL sims will not put a kettle on a slide that also has a child. They will put the kettle on a slide that has a dosimeter and a mass."),
    ("Nadia keeps the gauge.",
     "The tide gauge stays on."),
    ("She thinks of Linh, whom she has never met,",
     "She thinks of a glove designer she has never met,"),
    ("Linh is not paid to invent a childhood. She is paid to keep a hand from becoming a failure mode.",
     "The glove desk is not paid to invent a childhood. It is paid to keep a hand from becoming a failure mode."),
    ("the suit glove box sits under a lamp",
     "The suit glove box sits under a lamp"),

    # napkin grammar
    ("The napkin is a kindness. It has watched a sequencing lab",
     "The napkin is a kindness. Someone has watched a sequencing lab"),

    # appendix Hayflick leftovers
    ("Hayflick range:", "Dish-division range:"),
    ("| Hayflick ~40–60 |", "| Dish fence ~40–60 |"),

    # popular Penrose — keep Hawking as major nod; soft-pedal Penrose
    ("that let Penrose and Hawking prove their theorems",
     "that let Hawking and company prove their theorems"),
    ("That is why Penrose and Hawking could prove that",
     "That is why Hawking and company could prove that"),
    ("Penrose’s conformal cyclic cosmology — CCC, a cold idea with a serious author — tries to glue a remote, empty future to a next bang with a conformal trick.",
     "Conformal cyclic cosmology — CCC, a cold idea — tries to glue a remote, empty future to a next bang with a conformal trick."),
    ("Penrose has looked for rings in the leftover glow, scars of previous aeons.",
     "Its advocates have looked for rings in the leftover glow, scars of previous aeons."),
    ("Minkowski spacetime is a flat block.",
     "Flat spacetime is a flat block."),
]

# Only touch popular parts for these; skip appendix technical labels via file filter in main


def process(text: str) -> tuple[str, int]:
    n = 0
    for a, b in REPLACEMENTS:
        if a in text:
            c = text.count(a)
            text = text.replace(a, b)
            n += c
    return text, n


def main():
    total = 0
    for root in ROOTS:
        for p in sorted(root.glob("*.md")):
            if not re.match(r"^(00_Front|0[1-9]_|1[01]_|KDP)", p.name):
                continue
            t = p.read_text(encoding="utf-8")
            nt, n = process(t)
            if n:
                p.write_text(nt, encoding="utf-8", newline="\n")
                print(f"{n:3d}  {root.name[:30]} / {p.name}")
                total += n
    print("TOTAL", total)


if __name__ == "__main__":
    main()
