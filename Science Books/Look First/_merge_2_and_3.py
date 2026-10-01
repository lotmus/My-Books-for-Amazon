# -*- coding: utf-8 -*-
"""Merge Look First books 2 and 3, and move Book 1 chapters 31–32 into the result.

Idempotent: re-running rebuilds the merged folder and will not double-insert
Book 1 bridges.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First")
B1 = ROOT / "The Universe Has No Now - Manuscript"
B2 = ROOT / "A Trip Is Not a Settlement - Manuscript"
B3 = ROOT / "A Longer Life Is Not a New Body - Manuscript"
OUT = ROOT / "A Trip Is Not a New Life - Manuscript"

APOS = "\u2019"
EM = "\u2014"

FRONT = f"""# A Trip Is Not a New Life

*Camps, the Body, and the Earth You Do Not Abandon*

*by Lothar J. Musiol*

---

%%TOC%%

## How to Read This Book

Every claim in these pages wears one of three temperatures. The difference matters more than any date on a slide, and more than any slogan on a capsule.

**Hot {EM} established.** Measured, repeated, and used to predict new measurements. Light to the Moon takes about a second and a third. Light to Mars takes minutes. A Hohmann path between the two planets is a season, not a weekend. Most humans will stay on Earth for any leaving we can actually staff. A few thousand settlers do almost nothing to the air. Lifespan and healthspan are different pots. The sentence that we only use ten percent of the brain is false. A sickle-cell-class gene edit can correct a broken instruction in a lineage of cells that will keep the correction. The last half-century produced real, uneven gains: vaccines, a genome you can read, packets, cheaper compute.

**Warm {EM} working account, real gaps.** A crew around the Moon this decade is a class of mission, not a month. A landing *attempt* in the 2030s is the honest noun for a cabin that still owes a demonstration of the ugly parts. If industry collapsed, emissions would fall fast; so would the industrial haze that has been quietly blocking some sunlight. Aging is many clocks, not one fuse. Modest further gains in healthy years this century, in rich-country medicine, if institutions hold. Progress that is more often an S-curve than a ray.

**Cold {EM} speculation sold as inventory.** A city on the Moon or Mars this decade. Settlement as something you can buy by Friday. Leaving as a cleanup. A body-wide rewind. A scheduled 150-year or thousand-year ape. A hidden ninety percent of mind. Last fifty years times two hundred as the furniture of the year 12,000. A file that is you, forever. A required last mind at the end of time.

A temperature can change. A stack that has flown is hotter than a rendering. A local gene fix that was a paper can become a clinic. A fountain does not get warmer because the local fix did. A slipped date is not, by itself, a con, and it is not destiny. It is an invoice the slide did not want to show.

On one standing rule. **String theory, if it is named in this book, cannot currently be tested.** It will barely be named. Camps need dirt, delay, and dates. Bodies need clocks you can already count. Neither needs an extra dimension.

A few scenes are stories: a woman on a Mars-like dead world, an airlock that sticks, basil under an LED, a radio that answers late, a capsule with an optimistic label, a meeting that tries to fuse three nouns. They are thought experiments with dirt on them. The numbers in them are real. The people are invented.

The main chapters keep the math in the sentence. Numbered relations live in the Appendix. If you want the scaffolding, it is there. If you want the argument, you can finish the book without opening the back.

You do not need a physics degree or a medical degree. You need a willingness to let a downtown wait, and to let a miracle come apart into pots.

---

## This Book Stands Alone

This is Volume 2 of *Look First*. It is a complete book. You are not being assigned homework.

It used to be two later kitchens: a trip that is not a settlement, and a longer life that is not a new body. They are one book now, because they are one invoice. You do not get a new world by boarding, and you do not get a new body by waiting. The Earth you already staff does not get cleaner because the ambitious have a poster. The hands on the airlock still age after a useful dose.

A longer book already retired a cosmic {APOS}now{APOS} and treated elsewhere as a *permit*: *The Universe Has No Now*. You do not need it. The permit here is simpler. A world you can weigh. A delay you can time. A date that will slip. A morning you would vote to repeat.

Two chapters in the middle {EM} a crew that does not sleep, and a library of Earth {EM} used to sit in that cosmology book, because they were the far ticket. They sit here now, after the near ticket has been priced. Ice oceans, leftover glow, and a second dictionary stay in the other book. This one points at them once and does not assign them.

You can stop here. The airlock will still stick tomorrow. Her hands will still age.

---

## Author{APOS}s Note

Most people meet leaving, and the future of the body, in the wrong order.

First comes a poster. Then a year. Then a city. Then a headline about a gene, a chart that goes up and to the right, and a sentence that says the other ninety percent of the mind is a tank. Earth is treated as a kitchen you can abandon. DNA is treated as a fountain. Time is treated as a fuse a founder can name.

That order sells a downtown and a species upgrade in the same afternoon. It is not the order that makes the invoices easiest to see.

This book runs a different sequence on purpose. It starts with dirt, delay, and dates, because those are what a program actually is. It keeps three nouns unfused {EM} *sortie*, *outpost*, *settlement* {EM} because fusing them is how a flyby becomes a school district. It prices the Moon, the vehicle, Mars, the people who stay, and the classroom the posters skip. Only then does it take up the far ticket: a crew that can wait, and a library you do not pour into a sea you have not tasted. The second half is the body on the same invoice. Lifespan is not healthspan. A gene fix is local. The organ is already in use. Ten thousand years is not a straight line. A file is not a worldline.

John D. Barrow{APOS}s short books are still the formal model: brief chapters, no swagger, a clean line between a measurement and an idea for ideas. Neighbors in this lane treated a camp as a bill, a biosphere as a clock, a gene as a local object, and a brain as an energy bill. They are used. They are not copied. Where a year will move, the year is written as a *kind of clock*. This kitchen is dated September 2026.

A book like this should succeed if a sequence of recognitions arrives and stays:

that a program is not a poster, and a slipped date is an invoice;  
that the Moon is first because it is close, not because it is a spare Earth;  
that a landable year is not a town, and a large cheap stack is a vehicle;  
that sortie, outpost, and settlement must not be fused;  
that most of us stay, and leaving is not a cleanup;  
that flesh will not take a century cruise, and a library is not a flag;  
that you look first and seed later;  
that years on a wall clock are not years you would vote to repeat;  
that a gene fix is this tissue, this invoice, not a fountain;  
that the ten-percent sentence is false;  
that the last fifty years were real and are not a method;  
that a file is not a worldline;  
and that the world which already has a staff, and the morning which is still worth logging, are the product.

That last recognition is not a counsel against going, and it is not a counsel of despair. It is the opposite of a write-off. Look first. Seed later. The basil still has to live. The joint, if you paid for the joint, is allowed to be the win.

---
"""

OUTLINE = f"""# A Trip Is Not a New Life {EM} Headlines

Each popular chapter has a matching appendix note where a note exists. Chapters 17{EM}24 are taught in the main text and do not yet have twin notes.

No film titles. Stories are invented scenes. String theory, if named: cannot currently be tested.

**Length:** 42 chapters. Two former books, one invoice. Neighbors that taught the same sentence were already merged inside each half. This pass did not merge them again.

**Series:** Volume 2 of *Look First*. Stands alone. Volume 1: *The Universe Has No Now* (time, origins, elsewhere as a permit). Folder on disk: `A Trip Is Not a New Life - Manuscript`.

Former display titles, absorbed 29 September 2026: *A Trip Is Not a Settlement*; *A Longer Life Is Not a New Body* (earlier still: *A Permit Is Not a City*; *The Body Keeps Its Own Clock*; *The Body{APOS}s Honest Invoice*).

**Date hygiene:** written from a 2026 kitchen. Official years will move. Write *kinds of clocks*.

---

## Front

| Popular | Appendix |
|---|---|
| **How to Read** (temperatures; stands alone) | **A0. Three Temperatures of Claim** *(in A1{APOS}s doorway)* |

---

## Part I {EM} Dirt, Delay, Dates

| Ch | Popular | Appendix |
|---:|---|---|
| 1 | **The Airlock Still Sticks** | **A1** |
| 2 | **A Program Is Not a Poster** | **A2** |
| 3 | **How Dates Slip** | **A3** |

## Part II {EM} The Moon First

| Ch | Popular | Appendix |
|---:|---|---|
| 4 | **The Moon First, Because It Is Close** | **A4** |
| 5 | **What Has Already Flown** | **A5** |
| 6 | **The Next Crew Around the Moon** | **A6** |
| 7 | **A Landable Year Is Not a Town** | **A7** |
| 8 | **Gateway and the Architecture Fights** | **A8** |
| 9 | **Other Flags, Other Ledgers** | **A9** |

## Part III {EM} Vehicle, Not City

| Ch | Popular | Appendix |
|---:|---|---|
| 10 | **Starship as a Vehicle, Not a City** | **A10** |
| 11 | **Mars Rhetoric vs Mars Engineering** | **A11** |
| 12 | **Three Nouns: Sortie, Outpost, Settlement** | **A12** |

## Part IV {EM} Who Stays

| Ch | Popular | Appendix |
|---:|---|---|
| 13 | **Who Stays** | **A13** |
| 14 | **The Clocks of Recovery** | **A14** |
| 15 | **Leaving Is Not a Cleanup** | **A15** |
| 16 | **The Bill of Going** | **A16** |

## Part V {EM} The Classroom on the Close Rock

| Ch | Popular | Appendix |
|---:|---|---|
| 17 | **A Suit Is a Spacecraft** | *(in the chapter)* |
| 18 | **Two Weeks of Night** | *(in the chapter)* |
| 19 | **The Ice Has to Pay for Itself** | *(in the chapter)* |
| 20 | **Dust Is Not Dirt** | *(in the chapter)* |
| 21 | **The Dose** | *(in the chapter)* |
| 22 | **Abort Is a Path** | *(in the chapter)* |
| 23 | **Nobody Owns the Crater** | *(in the chapter)* |
| 24 | **What a Program Costs** | *(in the chapter)* |

## Part VI {EM} The Long Ticket

Moved here from *The Universe Has No Now*, Chapters 31 and 32. Book 1 keeps a short bridge under the old numbers, so its later chapters still have a chapter to point at. The greenhouse morning stays in Book 1. It is the scale of a near ticket. This part is the far one.

| Ch | Popular | Appendix |
|---:|---|---|
| 25 | **Crews That Do Not Sleep** | **A25** |
| 26 | **A Library of Earth** | **A26** |

## Part VII {EM} Many Clocks

| Ch | Popular | Was | Appendix |
|---:|---|---:|---|
| 27 | **Her Hands Still Age** | 1 | **A27** |
| 28 | **Lifespan Is Not Healthspan** | 2 | **A28** |
| 29 | **Many Clocks, Not One Fuse** | 3 | **A29** |
| 30 | **Local Fixes** | 4 | **A30** |
| 31 | **Not a Fountain** | 5 | **A31** |

## Part VIII {EM} The Organ You Already Use

| Ch | Popular | Was | Appendix |
|---:|---|---:|---|
| 32 | **We Already Use the Organ** | 6 | **A32** |
| 33 | **Cognitive Enhancement, Two Temperatures** | 7 | **A33** |
| 34 | **The Carrot Has No Off-Switch** | 8 | **A34** |

## Part IX {EM} Not a Straight Line

| Ch | Popular | Was | Appendix |
|---:|---|---:|---|
| 35 | **The Last Fifty Years Were Not a Straight Line** | 9 | **A35** |
| 36 | **S-Curves and Invoices** | 10 | **A36** |
| 37 | **Ten Thousand Years Is Not {EM}200** | 11 | **A37** |
| 38 | **Coordination, Wars, Institutions** | 12 | **A38** |

## Part X {EM} The Honest Body

| Ch | Popular | Was | Appendix |
|---:|---|---:|---|
| 39 | **Medicine{APOS}s Invoices** | 13 | **A39** |
| 40 | **Adjusting Is Not Spare Capacity** | 14 | **A40** |
| 41 | **Copies, Uploads, and Cold Immortality** | 15 | **A41** |
| 42 | **The Honest Body** | 16 | **A42** |

---

## What stayed in Book 1

The greenhouse morning (Book 1, Chapter 25), the exoplanet census, habitable-zone permits, ice oceans, and the second-origin courtroom stay there. They are the cosmology book{APOS}s question: whether {APOS}somewhere else{APOS} is even a legal sentence. Proper time as the death of a shared now stays there too. This book spends proper time once, as a skip that is not a longer life, in Chapter 37.

---

## What a finished reader can say

*A trip is not a settlement. Leaving does not clean the Earth. A longer life is not a new body. Look first. Seed later.*

If they wanted helium, or a downtown by Friday, they should leave with a colder, better want: a kitchen that still has a staff, and a morning still worth logging.
"""

STATUS = f"""# Status {EM} *A Trip Is Not a New Life*

**Kitchen date:** 29 September 2026.
**Author:** Lothar J. Musiol.
**Title:** A Trip Is Not a New Life.
**Subtitle:** Camps, the Body, and the Earth You Do Not Abandon.
**Series:** Volume 2 of *Look First*. Volume 1 was not reopened except to move two chapters out and leave bridges.

## What this file is

One manuscript. Former Volume 2 (*A Trip Is Not a Settlement*, 24 chapters) and former Volume 3 (*A Longer Life Is Not a New Body*, 16 chapters), plus two chapters that fit this kitchen better than the cosmology book.

Those two, from *The Universe Has No Now*:

- Chapter 31, **Crews That Do Not Sleep** {EM} now Chapter 25.
- Chapter 32, **A Library of Earth** {EM} now Chapter 26.

Book 1 still has short bridges under the old numbers, so its ice-ocean and handle chapters can keep pointing. The greenhouse morning stayed in Book 1. The operational camp, the Earth who stays, and the aging hands were already this book.

Source folders were not deleted. They are marked absorbed. Edit this folder.

## Shape

42 chapters. Parts I{EM}V are the trip. Part VI is the long ticket. Parts VII{EM}X are the body. Appendix notes A1{EM}A16 and A25{EM}A42. Chapters 17{EM}24 still have no twin notes. Body-half equations were renumbered (9){EM}(16) so they do not collide with the trip-half (1){EM}(8).

Internal {APOS}Chapter N{APOS} pointers inside the body half were shifted by 26. Two cross-book pointers were turned into local ones: the three nouns are Chapter 12 of this book; a slipped date is Chapter 3 of this book.

## Not done

No new Kindle file. The old `.docx` files in the absorbed folders are the previous separate editions. Figures for Chapters 25 and 26 were copied when the files were on disk. A date pass on Artemis / Starship years is still owed before upload, as it was for the trip half alone.
"""

KDP = f"""# Amazon KDP product description {EM} *A Trip Is Not a New Life*

Paste the **Sell copy** into the KDP description field, then the **Credits** block at the bottom. Credits are not printed inside the Kindle book.

---

## Sell copy

The airlock still sticks. The radio answers minutes late. A slide on Earth is still selling a year as if a year were a landing gear, and a capsule label is still more optimistic than the hands that open it.

*A Trip Is Not a New Life* is a popular book about camps, healthspan, and the Earth you do not get to abandon. A trip is not a settlement. A longer life is not a new body. They are one invoice.

It starts with dirt, delay, and dates, and refuses to fuse three nouns posters love to marry: *sortie*, *outpost*, *settlement*. The Moon comes first because it is close. Mars is where the posters breed. Most humans stay. A few thousand settlers do almost nothing to the air. Leaving is not a cleanup.

Flesh will not take a century cruise. A crew that does not sleep can wait, and waiting is not wisdom. If you send that crew, send a library, not a flag, and do not pour it into a sea you have not tasted. Look first. Seed later.

Then the same hands. Lifespan is not healthspan. Aging is many clocks, not one fuse. A gene fix is a local repair, not a fountain. The ten-percent sentence is false. The last fifty years of real, uneven progress are not a method for drawing a straight line to the year 12,000. A file is not a worldline.

Every claim wears a temperature. Hot means measured. Warm means a working account with gaps. Cold means a downtown, or a fountain, sold as inventory. You do not need a physics degree or a medical degree.

This is Volume 2 of *Look First*. It is a complete book. You can stop here.

---

## Credits

**A Trip Is Not a New Life**
*Camps, the Body, and the Earth You Do Not Abandon*
Look First, Volume 2
Copyright {EM} 2026 Lothar J. Musiol. All rights reserved.

Absorbed editions, same author, same year: *A Trip Is Not a Settlement*; *A Longer Life Is Not a New Body*.

**Figures.** Line diagrams are original. The Earth still in the trip half is a NASA/DSCOVR EPIC-class frame (Credit: NASA/DSCOVR EPIC), cropped for grayscale e-ink. Body-half stills, where present, are camera photographs, not AI stand-ins. The long-ticket figures are the ones that traveled with those chapters from *The Universe Has No Now*. None of the photographs is an AI stand-in for a mission frame.

If a later printing replaces a still, update the photographer and license on this page only {EM} not as a chapter in the book.
"""

BRIDGE_31 = f"""## 31. Crews That Do Not Sleep

A trip to Mars is a year of your proper time if you are lucky and the window is kind. A trip past that, at speeds we do not own, is a career for a machine, or a story biochemistry has not signed. At a hundredth of light speed, the nearest other sun is four centuries away. At a tenth, it is forty years, plus the problem of slowing down, plus a grain of dust that has become an energy rumor. Unshielded flesh in deep space collects a career-limiting dose in a handful of years. A machine can wait. Waiting is not wisdom.

![Figure 31. A tractor on bright dirt, working a field. The photograph is patient Earth labor; the chapter{APOS}s crew that does not sleep is still a machine that can wait.](Figures/figs/fig31.jpg)

The full classroom now lives in *A Trip Is Not a New Life*, Chapter 25: travel time, dose, a control system that must not go mad in the quiet, and why a pattern engine that completes a sentence is not yet that crew. This book keeps the facts the later chapters spend.

A crew that does not sleep can, in principle, coast, wake for a correction, and arrive still knowing the job. That project has a failure rate. It is not the Omega Point, and it is not a destiny. Present {APOS}AI{APOS} is a pattern engine. A century cruise needs a control loop that still makes sense after decades of bit flips. We own the beginnings of the first. We do not yet own the second. Keep the plug in reach. Do not ask the tool to be better than a person at being a person.

Chapter 32 is the box that crew would carry. Chapter 29{APOS}s melt-probe is the same kind of object on a shorter commute. The greenhouse in Chapter 25 of this book is the near ticket: a jammed door, a late radio, a potato. The century cruise is the far ticket, and it is billed in the other kitchen.

Appendix A31 points there.

---
"""

BRIDGE_32 = f"""## 32. A Library of Earth

If you send a crew that does not sleep, send more than a flag. Iron is common. The interesting inventory is a trick of carbon and water that learned to copy, then to remember, then to write the memory down. A human genome is a novella. A biosphere is a literature. Sequence without a kitchen is a book no one left standing can cook.

![Figure 32. A vault door in snow, large in frame. A library is a physical object.](Figures/figs/fig32.png)

Look first. Seed later. Taste the plume before you pour. If the sea is already taken, the library stays shut. If the exam was already empty, a greenhouse is a small farm, not a genesis. A nest of ants is the scale worth keeping: a city that farms and wars is impressive at its own size, and it is not a colleague. A printer that can make a cell can also make a plague. The box is as dangerous as it is precious.

The full invoice {EM} genome size, synthesis, planetary-protection categories, directed seeding as a project rather than a detection {EM} is *A Trip Is Not a New Life*, Chapter 26. This book keeps the rule, because Chapter 29 already hired it and Chapter 34 will spend it. A mountain outlasts a ministry. A cruise outlasts a body. Neither outlasts a mistake poured into a sea that already copies.

Appendix A32 points there.

---
"""

NOTE_A31 = f"""## A31. Travel Time, Dose, and Autonomous Systems

The numbers moved with the chapter. Cruise time at *0.01 c* and *0.1 c*, deep-space dose of order a few tenths of a sievert per year, and the distinction between a present pattern engine and a century-stable control loop are in *A Trip Is Not a New Life*, Appendix A25.

This book keeps the use the later chapters make of the fact: long travel is a project with a failure rate, not an Omega Point, and flesh is a bad hire for a four-century commute.

---
"""

NOTE_A32 = f"""## A32. Genome Information, Synthesis, and Planetary Protection

The numbers moved with the chapter. Genome size, COSPAR-class protection, and why a printed organism is logistics plus a library are in *A Trip Is Not a New Life*, Appendix A26.

This book keeps the rule: look first, seed later. A library poured into a sea that already copies is a conquistador. The same library, on a world whose exam has already been graded empty, is a greenhouse.

---
"""

CH25_POINTER = (
    f"\n\nThe staff for this morning {EM} programs, slips, who stays when she leaves, "
    f"and whether her hands get a new body because she waited {EM} is the next book, "
    f"*A Trip Is Not a New Life*. This chapter keeps the scale. It does not keep the "
    f"Gantt chart, and it does not keep the fountain.\n"
)

SERIES_OLD = (
    "If you liked the greenhouse and wanted a downtown, that want has a later kitchen: "
    "*A Trip Is Not a Settlement* — the Moon, Mars, and why leaving does not clean the Earth you already staff. "
    "If you liked the carrot and wanted helium, that want has a later kitchen: "
    "*A Longer Life Is Not a New Body* — healthspan, the brain you already use, and why ten thousand years is not a straight line."
)
SERIES_NEW = (
    "If you liked the greenhouse and wanted a downtown, or a fountain, that want has one later kitchen: "
    "*A Trip Is Not a New Life* — camps, the body, and the Earth you do not abandon. "
    "A trip is not a settlement. A longer life is not a new body. They are the same invoice."
)

OUTLINE_OLD = (
    "**Series:** Volume 1 of *Look First*. Later volumes, written as their own books: "
    "*A Trip Is Not a Settlement* (the Moon, Mars, and the Earth you do not abandon); "
    "*A Longer Life Is Not a New Body* (healthspan, local gene fixes, no spare-brain unlock). "
    "Do not add those rooms here."
)
OUTLINE_NEW = (
    "**Series:** Volume 1 of *Look First*. The later volume, written as its own book: "
    "*A Trip Is Not a New Life* (camps, healthspan, and the Earth you do not abandon). "
    "Chapters 31 and 32 keep a bridge. The classrooms themselves moved there. "
    "Do not add settlement Gantt charts or fountain medicine back into this book."
)

PROLOGUE = f"""## The Capsule and the Hands

A capsule arrives on the same delay as the orbiter{APOS}s voice. The label is optimistic. Her hands are not.

She works a greenhouse on a dead world {EM} wet soil under LEDs the color of an overcast noon, a tray of basil that does not belong to this dirt, a radio that answers a quarter-hour late, or four minutes, depending on the week. There is no conversation. There is a stack of monologues that eventually, if everyone lives, amount to a plan.

The capsule is a local win in a blister pack. A joint that still works. A season she can still hit an airlock for. She takes the dose because local wins are the only kind biology has ever reliably sold. She does not become a different species. She names the basil, which is sentimental, and logs the pH, which is not.

The first half of this book priced the camp and the Earth she did not get to abandon by leaving. This half is about what the capsule is allowed to mean, and what a slide deck is not allowed to sell on the back of it.

The short version, before it has been earned:

Lifespan is not healthspan. Aging is many clocks, not one fuse. A gene fix is a local repair {EM} this instruction, this tissue, this invoice {EM} not a fountain. The sentence *we only use ten percent of our brain* is false. You do not have a spare ninety percent in the cupboard waiting for a password. You have the organ you already use, plus sleep, plus practice, plus tools, plus other people. The carrot that makes a body chase a cue has no off-switch. A long life does not install one. And the last fifty years of real, uneven progress are not a method for drawing a straight line to the year 12,000.

Those are recognitions, not moods. They wear temperatures. If you came for helium, you will not get helium. You may leave with a colder, better want: more mornings that are still worth logging.

---
"""

BANNER = (
    "> **Absorbed 29 September 2026.** This folder is a source half. "
    "The live book is `A Trip Is Not a New Life - Manuscript`. "
    "Do not extend this manuscript on its own.\n\n"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")


def newline_of(path: Path) -> str:
    sample = path.read_bytes()[:4000]
    return "\r\n" if b"\r\n" in sample else "\n"


def write(path: Path, text: str, nl: str = "\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if nl == "\r\n":
        text = text.replace("\n", "\r\n")
    path.write_text(text, encoding="utf-8", newline="")


def replace_between(text: str, start: str, end: str, new_body: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"missing start: {start[:60]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"missing end after {start[:60]}: {end[:60]}")
    return text[:i] + new_body.rstrip() + "\n\n" + text[j:]


def shift_body_half(text: str) -> str:
    text = re.sub(
        r"Chapter 12 of the other book.s three nouns",
        f"Chapter 12{APOS}s three nouns",
        text,
    )
    text = text.replace(
        "The slip is Chapter 3 of the destinations book, if you have it; you do not need it.",
        "The slip is Chapter 3; a moved year is a meeting, not a destiny.",
    )
    text = text.replace("## A0 / A1. ", "## A27. ")

    def headings(m: re.Match) -> str:
        n = int(m.group(1))
        if 1 <= n <= 16:
            return f"## {n + 26}. "
        return m.group(0)

    text = re.sub(r"^## (\d+)\. ", headings, text, flags=re.M)

    def chapters(m: re.Match) -> str:
        n = int(m.group(1))
        if 1 <= n <= 16:
            return f"Chapter {n + 26}"
        return m.group(0)

    text = re.sub(r"Chapter (\d+)", chapters, text)

    def notes(m: re.Match) -> str:
        n = int(m.group(1))
        if 1 <= n <= 16:
            return f"A{n + 26}"
        return m.group(0)

    text = re.sub(r"A(\d+)", notes, text)

    def eqs(m: re.Match) -> str:
        n = int(m.group(1))
        if 1 <= n <= 8:
            return f"**({n + 8})**"
        return m.group(0)

    text = re.sub(r"\*\*\((\d+)\)\*\*", eqs, text)

    def rows(m: re.Match) -> str:
        n = int(m.group(1))
        if 1 <= n <= 8:
            return f"| ({n + 8}) |"
        return m.group(0)

    text = re.sub(r"\| \((\d+)\) \|", rows, text)
    return text


def patch_trip(text: str) -> str:
    text = text.replace(
        "Chapter 31 of the longer book already said a crew that does not sleep can wait. This book says a crew that does not sleep can also fetch a box",
        "Chapter 25 says a crew that does not sleep can wait. The same crew can also fetch a box",
    )
    text = text.replace(
        "The longer book already said a library is not a seed unless you look first.",
        "Chapter 26 says a library is not a seed unless you look first.",
    )
    text = text.replace(
        f"The longer book{APOS}s rule — look first, seed later —",
        f"Chapter 26{APOS}s rule — look first, seed later —",
    )
    text = text.replace(
        "The longer book’s rule — look first, seed later —",
        f"Chapter 26{APOS}s rule — look first, seed later —",
    )
    text = text.replace(
        "That rule, in the longer book, meant",
        "That rule, in *The Universe Has No Now*, meant",
    )
    return text


def retarget_long_ticket(chapter_31: str, chapter_32: str) -> tuple[str, str]:
    a = chapter_31
    a = a.replace("## 31. Crews That Do Not Sleep", "## 25. Crews That Do Not Sleep")
    a = a.replace("Chapter 32", "Chapter 26")
    a = a.replace("Appendix A31", "Appendix A25")
    a = a.replace("Figure 31.", "Figure 25.")
    a = a.replace("(Figures/figs/fig31.jpg)", "(Figures/fig25.jpg)")
    a = a.replace("(Figures/figs/fig31.png)", "(Figures/fig25.jpg)")
    a = a.replace(
        "Chapter 29\u2019s melt-probe is the same object with a shorter commute.",
        "A melt-probe under the ice, in *The Universe Has No Now*, is the same object with a shorter commute.",
    )
    a = a.replace(
        "the observer Chapter 6 actually needed",
        "the observer the other book actually needed",
    )
    a = a.replace(
        "The path of Chapter 45 does not end",
        "The path in the other book does not end",
    )
    a = a.replace(
        "Chapter 29\u2019s hole",
        "the hole under the ice, in the other book",
    )
    # curly or straight apostrophe variants already handled if the file uses U+2019
    a = a.replace(
        "Chapter 29's melt-probe is the same object with a shorter commute.",
        "A melt-probe under the ice, in *The Universe Has No Now*, is the same object with a shorter commute.",
    )
    a = a.replace("Chapter 29's hole", "the hole under the ice, in the other book")

    b = chapter_32
    b = b.replace("## 32. A Library of Earth", "## 26. A Library of Earth")
    b = b.replace("Chapter 31", "Chapter 25")
    b = b.replace("Appendix A32", "Appendix A26")
    b = b.replace("Figure 32.", "Figure 26.")
    b = b.replace("(Figures/figs/fig32.png)", "(Figures/fig26.png)")
    b = b.replace("(Figures/figs/fig32.jpg)", "(Figures/fig26.png)")
    b = b.replace("The woman in Chapter 25", "The woman in Chapter 1")
    b = b.replace(
        "Chapter 30\u2019s one dictionary",
        "the other book\u2019s one-dictionary test",
    )
    b = b.replace("Chapter 30's one dictionary", "the other book\u2019s one-dictionary test")
    b = b.replace(
        "the rule in Chapter 29 was look first",
        "the ice chapter of the other book already said look first",
    )
    b = b.replace(
        "Chapter 6\u2019s tangle lives here as dirt",
        "The other book\u2019s tangle lives here as dirt",
    )
    b = b.replace("Chapter 6's tangle lives here as dirt", "The other book\u2019s tangle lives here as dirt")
    b = b.replace("the way Chapter 30 already warned", "the way the other book already warned")
    b = b.replace(
        "Chapter 30 already said what a second dictionary would mean.",
        "The other book already said what a second dictionary would mean.",
    )
    return a, b


def retarget_notes(a31: str, a32: str) -> tuple[str, str]:
    a = a31.replace("## A31. Travel Time, Dose, and Autonomous Systems", "## A25. Travel Time, Dose, and Autonomous Systems")
    a = a.replace("(A25)", "(the Mars-surface dose, Appendix A11 of this book and Book 1\u2019s old A25)")
    a = a.replace("(A29)", "(*The Universe Has No Now*, the ice-ocean note)")
    b = a32.replace(
        "## A32. Genome Information, Synthesis, and Planetary Protection",
        "## A26. Genome Information, Synthesis, and Planetary Protection",
    )
    b = b.replace("erase A29\u2019s look-first measurement", "erase the ice-ocean look-first measurement in the other book")
    b = b.replace("erase A29's look-first measurement", "erase the ice-ocean look-first measurement in the other book")
    b = b.replace("handles still owe (17)", "handles still owe the exotic bill, which the other book prices")
    return a, b


def slice_chapter(text: str, start: str, end: str) -> str:
    i = text.find(start)
    j = text.find(end, i + len(start))
    if i < 0 or j < 0:
        raise SystemExit(f"cannot slice {start}")
    return text[i:j].strip() + "\n"


def split_appendix(text: str) -> tuple[str, str, str, str]:
    eq = text.find("\n## Equations at a Glance")
    fr = text.find("\n## Further Reading")
    gl = text.find("\n## Glossary")
    if min(eq, fr, gl) < 0:
        raise SystemExit("appendix tails missing")
    return text[:eq], text[eq:fr], text[fr:gl], text[gl:]


def copy_figures() -> None:
    dest = OUT / "Figures"
    dest.mkdir(parents=True, exist_ok=True)
    wanted = {
        "fig31.jpg": "fig25.jpg",
        "fig31.png": "fig25.png",
        "fig32.png": "fig26.png",
        "fig32.jpg": "fig26.jpg",
    }
    found = {p.name: p for p in B1.rglob("fig3*") if p.is_file()}
    for src_name, dst_name in wanted.items():
        src = found.get(src_name)
        if src:
            shutil.copy2(src, dest / dst_name)


def banner(path: Path) -> None:
    text = read(path)
    if "Absorbed 29 September 2026" in text:
        return
    write(path, BANNER + text, newline_of(path))


def splice_book1() -> None:
    part = B1 / "06_Part_Six_Getting_There.md"
    assembled = B1 / "The_Universe_Has_No_Now.md"
    appendix = B1 / "11_Appendix.md"
    for path in (part, assembled):
        nl = newline_of(path)
        text = read(path)
        if "The staff for this morning" not in text:
            anchor = "The morning is how you spend it.\n"
            if anchor not in text:
                raise SystemExit(f"ch 25 anchor missing in {path.name}")
            text = text.replace(anchor, anchor + CH25_POINTER, 1)
        text = replace_between(text, "## 31. Crews That Do Not Sleep", "## 32. A Library of Earth", BRIDGE_31)
        text = replace_between(text, "## 32. A Library of Earth", "## 33. Handles, and the Bill", BRIDGE_32)
        text = text.replace(SERIES_OLD, SERIES_NEW)
        if SERIES_OLD in read(path) and SERIES_NEW not in text:
            raise SystemExit(f"series sentence did not match in {path.name}")
        write(path, text, nl)
    nl = newline_of(appendix)
    app = read(appendix)
    app = replace_between(app, "## A31. Travel Time, Dose, and Autonomous Systems", "## A32. Genome Information, Synthesis, and Planetary Protection", NOTE_A31)
    app = replace_between(app, "## A32. Genome Information, Synthesis, and Planetary Protection", "## A33. Einstein", NOTE_A32)
    write(appendix, app, nl)
    front_path = B1 / "00_Front_Matter.md"
    nl = newline_of(front_path)
    front = read(front_path)
    if SERIES_OLD not in front:
        raise SystemExit("series sentence did not match in front matter")
    front = front.replace(SERIES_OLD, SERIES_NEW)
    front = front.replace("Those books stand alone.", "That book stands alone.")
    write(front_path, front, nl)
    assembled_text = read(assembled)
    assembled_text = assembled_text.replace("Those books stand alone.", "That book stands alone.")
    write(assembled, assembled_text, newline_of(assembled))
    outline_path = B1 / "00_Chapter_Outline.md"
    outline = read(outline_path)
    if OUTLINE_OLD not in outline:
        raise SystemExit("outline series line did not match")
    outline = outline.replace(OUTLINE_OLD, OUTLINE_NEW)
    write(outline_path, outline, newline_of(outline_path))


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / "Figures").mkdir()

    trip_files = [
        "01_Part_One_Dirt_Delay_Dates.md",
        "02_Part_Two_The_Moon_First.md",
        "03_Part_Three_Vehicle_Not_City.md",
        "04_Part_Four_Who_Stays.md",
        "05_Part_Five_The_Classroom.md",
    ]
    for name in trip_files:
        write(OUT / name, patch_trip(read(B2 / name)))

    part6_src = read(B1 / "06_Part_Six_Getting_There.md")
    # If bridges were already applied, pull the long text from git? First run uses full chapters.
    # This script splices Book 1 AFTER building, so the source here is still the full chapter
    # only if we read it before splice. build() is called before splice_book1().
    ch31 = slice_chapter(part6_src, "## 31. Crews That Do Not Sleep", "## 32. A Library of Earth")
    ch32 = slice_chapter(part6_src, "## 32. A Library of Earth", "## 33. Handles, and the Bill")
    ch31, ch32 = retarget_long_ticket(ch31, ch32)
    part6 = (
        "# PART VI — The Long Ticket\n\n"
        "The near ticket was a camp. This part is the far one: a crew that can wait, and the box it should carry. "
        "Ice oceans and a second dictionary stay in *The Universe Has No Now*. The rule does not.\n\n---\n\n"
        + ch31
        + "\n"
        + ch32
    )
    write(OUT / "06_Part_Six_The_Long_Ticket.md", part6)

    body_map = [
        ("01_Part_One_Many_Clocks.md", "07_Part_Seven_Many_Clocks.md", "# PART I — Many Clocks", "# PART VII — Many Clocks", True),
        ("02_Part_Two_The_Organ_You_Already_Use.md", "08_Part_Eight_The_Organ.md", "# PART II — The Organ You Already Use", "# PART VIII — The Organ You Already Use", False),
        ("03_Part_Three_Not_A_Straight_Line.md", "09_Part_Nine_Not_A_Straight_Line.md", "# PART III — Not a Straight Line", "# PART IX — Not a Straight Line", False),
        ("04_Part_Four_The_Honest_Body.md", "10_Part_Ten_The_Honest_Body.md", "# PART IV — The Honest Body", "# PART X — The Honest Body", False),
    ]
    for src_name, dst_name, old_h, new_h, prologue in body_map:
        text = read(B3 / src_name).replace(old_h, new_h, 1)
        text = shift_body_half(text)
        if prologue:
            needle = new_h + "\n\n---\n\n"
            if needle not in text:
                raise SystemExit("part VII doorway missing")
            text = text.replace(needle, needle + PROLOGUE + "\n", 1)
        write(OUT / dst_name, text)

    b2_body, b2_eq, b2_fr, b2_gl = split_appendix(read(B2 / "11_Appendix.md"))
    b3_body, b3_eq, b3_fr, b3_gl = split_appendix(read(B3 / "11_Appendix.md"))
    # drop Book 3's own appendix title and how-to-read; keep from the first note
    cut = b3_body.find("## A0 / A1.")
    if cut < 0:
        raise SystemExit("book 3 A0 missing")
    b3_notes = shift_body_half(b3_body[cut:])
    b3_eq = shift_body_half(b3_eq)
    b3_fr = shift_body_half(b3_fr)
    b3_gl = shift_body_half(b3_gl)

    app_src = read(B1 / "11_Appendix.md")
    a31 = slice_chapter(app_src, "## A31. Travel Time, Dose, and Autonomous Systems", "## A32. Genome Information, Synthesis, and Planetary Protection")
    a32 = slice_chapter(app_src, "## A32. Genome Information, Synthesis, and Planetary Protection", "## A33. Einstein")
    a31, a32 = retarget_notes(a31, a32)

    gap = (
        "\n\n## A17–A24. The Classroom Has No Separate Notes Yet\n\n"
        "Chapters 17 through 24 teach the suit, the lunar night, ice, dust, dose, abort, ownership, and what a program costs. "
        "The bills are in the chapters. They do not yet have twin notes.\n\n---\n\n"
    )
    body_intro = (
        "\n\n## Notes for the Body Half\n\n"
        "From here the note numbers match the body chapters. "
        "A local edit that reaches a clinic can warm. A fountain does not warm because the local edit did. "
        "String theory, if named: **cannot currently be tested**.\n\n---\n\n"
    )
    # Book 3 further-reading and glossary headings would duplicate. Demote them.
    b3_fr = b3_fr.replace("## Further Reading (tiered)", "## Further Reading — the Body", 1)
    b3_gl = b3_gl.replace("## Glossary", "## Glossary — the Body", 1)
    b3_eq = b3_eq.replace("## Equations at a Glance", "## Equations at a Glance — the Body", 1)

    appendix = b2_body + gap + a31 + "\n" + a32 + body_intro + b3_notes + b2_eq + b3_eq + b2_fr + b3_fr + b2_gl + b3_gl
    write(OUT / "11_Appendix.md", appendix)
    write(OUT / "00_Front_Matter.md", FRONT)
    write(OUT / "00_Chapter_Outline.md", OUTLINE)
    write(OUT / "00_Status.md", STATUS)
    write(OUT / "KDP_Description.md", KDP)
    copy_figures()

    for folder in (B2, B3):
        banner(folder / "00_Status.md")
        banner(folder / "00_Chapter_Outline.md")


def words() -> None:
    n = 0
    for p in sorted(OUT.glob("*.md")):
        if p.name.startswith("00_") or p.name.startswith("KDP"):
            continue
        n += len(re.findall(r"\S+", read(p)))
    print(f"reader-text words (parts + appendix): {n}")
    headings = []
    for p in sorted(OUT.glob("*.md")):
        for line in read(p).splitlines():
            if line.startswith("## ") and re.match(r"## \d+\. ", line):
                headings.append(line)
    print(f"numbered chapters: {len(headings)}")
    print(headings[0], "...", headings[-1])


if __name__ == "__main__":
    marker = B1 / "06_Part_Six_Getting_There.md"
    if "The full classroom now lives" in marker.read_text(encoding="utf-8"):
        raise SystemExit(
            "Book 1 is already bridged. Re-running would rebuild the merged book "
            "from the short bridges and wipe the hand fixes. Stop."
        )
    build()
    splice_book1()
    words()
