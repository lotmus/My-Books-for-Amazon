"""Deperson pass: obscure names -> roles; major players keep a nod; Mara/Rohan stay."""
from pathlib import Path
import re

BOOKS = [
    Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\A Trip Is Not a Settlement - Manuscript"),
    Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\A Longer Life Is Not a New Body - Manuscript"),
    Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\The Universe Has No Now - Manuscript"),
]

# Order matters: longer / more specific first
REPLACEMENTS = [
    # --- Book 2 invented cast ---
    ("Dex Ortega writes cadence boards. He is invented. His board",
     "A cadence board"),
    ("Dex’s", "the cadence board’s"),
    ("Dex's", "the cadence board’s"),
    ("Pavel Grun writes EDL sims. He is invented. His sims",
     "EDL sims"),
    ("Pavel’s sims", "the EDL sims"),
    ("Pavel's sims", "the EDL sims"),
    ("Pavel’s", "the sim writer’s"),
    ("Pavel's", "the sim writer’s"),
    ("Elena Voss, from Chapter 2, puts the three nouns on the wall of the review and will not let the slide use two in one sentence. She is invented. The wall is a kindness.",
     "A review wall puts the three nouns up and will not let the slide use two in one sentence. The wall is a kindness."),
    ("Steal Elena’s meeting.", "Steal the review meeting."),
    ("Steal Elena's meeting.", "Steal the review meeting."),
    ("Elena’s meeting", "the review meeting"),
    ("Elena's meeting", "the review meeting"),
    ("Elena’s cards", "the three cards"),
    ("Elena's cards", "the three cards"),
    ("Elena’s", "the review lead’s"),
    ("Elena's", "the review lead’s"),
    ("Nadia Okonkwo runs a tide gauge and a patience. She is invented. The gauge is not.",
     "A tide gauge runs on patience. The gauge is not invented."),
    ("Nadia’s gauge", "the tide gauge"),
    ("Nadia's gauge", "the tide gauge"),
    ("Nadia’s", "the gauge tech’s"),
    ("Nadia's", "the gauge tech’s"),
    ("Linh Pham designs suit gloves. She is invented. The dust is not.",
     "Suit gloves have a designer who is invented. The dust is not."),
    ("Linh’s glove", "the suit glove"),
    ("Linh's glove", "the suit glove"),
    ("Linh’s", "the glove designer’s"),
    ("Linh's", "the glove designer’s"),
    ("Wei Ning’s", "a far-side operator’s"),
    ("Wei Ning's", "a far-side operator’s"),
    ("Wei Ning", "a far-side operator"),

    # --- Book 3 invented cast ---
    ("Ibrahim Sorel teaches a history of techniques, not a history of posters. He is invented. His board has two columns: *what got cheaper* and *what did not*. Vaccines, sequences, packets, transistors: cheaper, then slower, then a wall. Hospital cleaning, a night nurse, a peace, a grid that stays up in a heat wave: not cheaper in the same way, and sometimes dearer. He will not let a student draw a line from 1975 to 12,000 and write *therefore*. Therefore is a smuggle.",
     "A techniques board has two columns: *what got cheaper* and *what did not*. Vaccines, sequences, packets, transistors: cheaper, then slower, then a wall. Hospital cleaning, a night nurse, a peace, a grid that stays up in a heat wave: not cheaper in the same way, and sometimes dearer. The board will not let a student draw a line from 1975 to 12,000 and write *therefore*. Therefore is a smuggle."),
    ("Ibrahim will not let", "The board will not let"),
    ("Ibrahim’s", "the techniques board’s"),
    ("Ibrahim's", "the techniques board’s"),
    ("Priya Nair draws S-curves on napkins for people who arrived with rockets. She is invented. The napkin is a kindness. She has watched a sequencing lab go from a cathedral to a bench and then stall on a variant of unknown significance. She has watched a chip shop go from a miracle to a diplomacy. She likes both. She will not extend either with a ruler to a year that has no furniture.",
     "S-curves get drawn on napkins for people who arrived with rockets. The napkin is a kindness. It has watched a sequencing lab go from a cathedral to a bench and then stall on a variant of unknown significance — and a chip shop go from a miracle to a diplomacy. Keep both. Do not extend either with a ruler to a year that has no furniture."),
    ("Priya’s napkin", "the napkin"),
    ("Priya's napkin", "the napkin"),
    ("Priya’s", "the napkin’s"),
    ("Priya's", "the napkin’s"),
    ("Owen Hale chairs a board that decides which local fix a hospital can afford this year. He is invented. The board is real in a thousand towns. He has a sickle-cell-class win on the table and a line of other doors, and a budget that is a political weather. The transistor that made the win possible is not in the room. The ledger is. The meeting is. A war two seas away is in the room as a price. He does not feel like a villain. He feels like a kitchen. The kitchen is the limit more often than the enzyme.",
     "A hospital board decides which local fix it can afford this year. The board is real in a thousand towns. It has a sickle-cell-class win on the table and a line of other doors, and a budget that is a political weather. The transistor that made the win possible is not in the room. The ledger is. The meeting is. A war two seas away is in the room as a price. Nobody on that board feels like a villain. They feel like a kitchen. The kitchen is the limit more often than the enzyme."),
    ("Owen’s board", "the hospital board"),
    ("Owen's board", "the hospital board"),
    ("Owen’s", "the board’s"),
    ("Owen's", "the board’s"),
    ("Dr. Anjali Mehta enrolls people in a trial and then sits with the ones the trial did not choose. She is invented. The sitting is the job. She has a win on her wall and a stack of letters that say *not eligible*. Eligible is a biological word and a geographic word and an insurance word. She will not let a founder use her wall as a downtown. The wall is a door that opened for some. Chapter 5 already said the house has other doors. This chapter says some houses do not get a carpenter.",
     "A trial doctor enrolls people and then sits with the ones the trial did not choose. The sitting is the job. There is a win on the wall and a stack of letters that say *not eligible*. Eligible is a biological word and a geographic word and an insurance word. Do not let a founder use that wall as a downtown. The wall is a door that opened for some. Chapter 5 already said the house has other doors. This chapter says some houses do not get a carpenter."),
    ("Anjali’s wall", "the trial wall"),
    ("Anjali's wall", "the trial wall"),
    ("Anjali’s", "the trial doctor’s"),
    ("Anjali's", "the trial doctor’s"),

    # --- Longevity / biology name noise ---
    ("Jeanne Calment died at 122.",
     "The longest well-documented human life ended at 122."),
    ("We did not double Jeanne Calment.",
     "We did not double the right-hand fence."),
    ("A tail like Calment is a warning",
     "A 122-year tail is a warning"),
    ("A Calment-length tail is a warning",
     "A 122-year tail is a warning"),
    ("Jeanne Calment: documented ~122 years (1875–1997). Tail, not a mean, not a protocol.",
     "Longest documented human life: ~122 years. Tail, not a mean, not a protocol."),
    ("William James wrote, more than a century ago, that we live below our limits. That is a moral sentence about effort.",
     "A century-old moral sentence said we live below our limits. That is effort-talk."),
    ("where the Hayflick limit is the observation that many human cell types in a dish divide about forty to sixty times and then stop.",
     "where the cell-division fence is the observation that many human cell types in a dish divide about forty to sixty times and then stop."),
    ("Hayflick is not a mystic number.",
     "The dish fence is not a mystic number."),
    ("Hayflick’s range", "the dish-division range"),
    ("Hayflick's range", "the dish-division range"),
    ("Hallmarks, Hayflick, and Why One Switch Is Not on the Counter",
     "Hallmarks, the Dish Fence, and Why One Switch Is Not on the Counter"),

    # --- Book 1 historical: keep Newton/Einstein/Maxwell; nod others away ---
    ("In 1887 Albert A. Michelson and Edward W. Morley sent light up and down an interferometer in Cleveland, expecting the Earth’s motion around the Sun to change the time of the trip.",
     "In 1887 an interferometer in Cleveland sent light up and down, expecting the Earth’s motion around the Sun to change the time of the trip."),
    ("Hendrik Lorentz and Henri Poincaré patched the books: lengths contract, clocks disagree, the ether becomes a ghost that cannot be found. Their algebra is close to Einstein’s. Their ontology is not. They were saving a stage.",
     "Others patched the books: lengths contract, clocks disagree, the ether becomes a ghost that cannot be found. Their algebra is close to Einstein’s. Their ontology is not. They were saving a stage."),
    ("Poincaré saw the relativity of simultaneity as a convention about how to set distant clocks. Einstein treated the convention as a fact about the world.",
     "Some treated the relativity of simultaneity as a convention about how to set distant clocks. Einstein treated the convention as a fact about the world."),
    ("Michelson’s null result", "the Cleveland null result"),
    ("Michelson's null result", "the Cleveland null result"),
    ("Michelson’s interferometer", "the Cleveland interferometer"),
    ("Michelson's interferometer", "the Cleveland interferometer"),
    ("It is often called the Andromeda paradox, and Roger Penrose gave it the version physicists still use.",
     "It is often called the Andromeda paradox — the version physicists still use."),
    ("Penrose’s point does not need the upgrade.",
     "The paradox does not need the upgrade."),
    ("Penrose's point does not need the upgrade.",
     "The paradox does not need the upgrade."),
    ("Penrose’s yard", "the yard thought-experiment"),
    ("Penrose's yard", "the yard thought-experiment"),
    ("Poincaré had already seen the hinge, years before Penrose named a galaxy.",
     "The hinge was already visible years before anyone named a galaxy for the paradox."),
    ("the years when Lorentz was still patching the ether",
     "the years when the ether was still being patched"),
    ("the same arithmetic Poincaré used on clocks and Einstein used on trains",
     "the same arithmetic Einstein used on trains"),
    ("The Lorentz tilt is hot.",
     "The relativity tilt is hot."),
    ("Minkowski, who taught Einstein the geometry of this, put it in a line that still startles: henceforth space by itself, and time by itself, are doomed to fade into mere shadows.",
     "The geometry of this got a line that still startles: henceforth space by itself, and time by itself, are doomed to fade into mere shadows."),
    ("Hermann Minkowski had been Einstein’s teacher in Zurich and had not, at first, been impressed. Then he saw that the 1905 paper was not a trick with clocks. It was a geometry.",
     "Einstein’s own teacher had not, at first, been impressed. Then the 1905 paper stopped looking like a trick with clocks. It was a geometry."),
    ("every later test that has distinguished “space plus time” from spacetime has come down on Minkowski’s side.",
     "every later test that has distinguished “space plus time” from spacetime has come down on that side."),
    ("Minkowski’s point was that the two tricks are one trick.",
     "The point was that the two tricks are one trick."),
    ("Minkowski's point was that the two tricks are one trick.",
     "The point was that the two tricks are one trick."),
    ("the geometry Einstein and Minkowski handed us",
     "the geometry Einstein handed us"),
]

# Soft cleanups after role swaps that may leave grammar lumps
POST = [
    (r"A cadence board has a column", "A cadence board has a column"),
    (r"EDL sims have killed", "EDL sims have killed"),
    (r"A history board of techniques, not posters, has two columns",
     "A history board of techniques, not posters, has two columns"),
]


def process(text: str) -> tuple[str, int]:
    n = 0
    for a, b in REPLACEMENTS:
        if a in text:
            c = text.count(a)
            text = text.replace(a, b)
            n += c
    for a, b in POST:
        text2, c = re.subn(a, b, text)
        text = text2
        n += c
    return text, n


def main():
    total = 0
    for root in BOOKS:
        files = sorted(root.glob("*.md"))
        for p in files:
            if p.name.startswith("00_Chapter") or p.name.startswith("00_Figure") or p.name.startswith("00_Status"):
                continue
            if not re.match(r"^(00_Front|0[1-9]_|1[01]_|KDP)", p.name):
                if p.name not in ("KDP_Description.md",):
                    continue
            t = p.read_text(encoding="utf-8")
            nt, n = process(t)
            if n:
                p.write_text(nt, encoding="utf-8", newline="\n")
                print(f"{n:3d}  {p.parent.name[:28]} / {p.name}")
                total += n
    print("TOTAL replacements", total)


if __name__ == "__main__":
    main()
