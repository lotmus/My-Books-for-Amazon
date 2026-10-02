# -*- coding: utf-8 -*-
"""Vocabulary rules: floors -> chapters, rooms -> sections, Tower -> series.
Each rule: (compiled regex, replacement str or function(match)->str).
Protected patterns mark spans where 'floor'/'room' is ordinary English or
mathematics (floor function, noise floor, room temperature ...)."""
import re

PROTECT = [r"floor function", r"floor’s verdict", r"⌊", r"floor-division", r"noise floor", r"ramp noise floor",
    r"positive floor", r"hard floor", r"Heisenberg floor", r"Cramér–Rao floor", r"individually-rational floor",
    r"absolute floor", r"local floor", r"theoretical floor", r"valley floor", r"flat floor", r"rectangular floor",
    r"true floor area", r"bathroom floors", r"U’s floor", r"sorting’s floor", r"‘floor’ of the region",
    r"floors to [12]\b", r"floor never", r"rigorous floor", r"floor poured", r"floor of 1\b", r"floor of zero",
    r"the floor of the region", r"floor under", r"floor sits above", r"\bfloor\(", r"floor(?:s)? and ceiling", r"ceiling",
    r"room temperature", r"room for\b", r"room to (?:spare|shade|move|pass|touch|round)", r"no empty room", r"no free room",
    r"guest in room", r"room n\b", r"room n\+1", r"wiggle-room", r"dark room", r"machine room", r"engine room",
    r"physical room", r"seminar[- ]room", r"spare room", r"cold room", r"circular room", r"rectangular room",
    r"12 m room", r"manufacture room", r"save room", r"enough room", r"much room", r"particular room", r"°C room",
    r"than the room", r"two-dimensional room", r"have room", r"had room", r"less room", r"more room", r"room’s corner",
    r"corner of (?:a|the) room", r"the room you", r"a room’s", r"room is \d", r"elbow room", r"leg ?room",
    r"in the room\b", r"[Tt]owers? of Hanoi", r"[Pp]ower tower", r"tower of (?:exponents|powers|fields|extensions)", r"across the room", r"living room", r"waiting room", r"room-sized", r"tower (?:law|property)", r"[Tt]he tower problem", r"[Tt]he tower’s height", r"How tall is the tower", r"the tower is \d", r"Build the tower", r"whole tower’s supremum", r"whole tower is generated", r"infinitely many rooms", r"finitely many rooms", r"out of the room", r"tower of difficulty", r"building block",
]
PROTECT_RE = re.compile('|'.join(PROTECT))

def cap(src, rep):
    if src[:1].isupper() and rep[:1].islower():
        return rep[:1].upper() + rep[1:]
    return rep

def simple(rep):
    return lambda m: cap(m.group(0), rep)

RULES = [
    # structural metaphors of the old building (source wording; first match wins)
    (re.compile(r"\b(several|many|a few|two|three) floors below\b"), lambda m: cap(m.group(0), m.group(1).lower() + " chapters back")),
    (re.compile(r"\b[Tt]he top floor\b"), simple("the last chapter")),
    (re.compile(r"\b[Tt]he (?:upper|higher) floors\b"), simple("the later chapters")),
    (re.compile(r"\b[Tt]he lower floors\b"), simple("the earlier chapters")),
    (re.compile(r"\b(Volume 4), [Tt]he Penthouse\b"), lambda m: m.group(1)),
    (re.compile(r"\bThe Penthouse(?= —)"), "Volume 4"),
    (re.compile(r"\b[Tt]ower continues upward\b"), "series continues"),
    (re.compile(r"\b(Volume \d), [Tt]he (?:Lower|Middle|Upper|Top|Highest) Floors\b"), lambda m: m.group(1)),
    (re.compile(r"\bThe (Lower|Middle|Upper|Top) Floors(?= —)"), lambda m: "Volume " + {"Lower": "1", "Middle": "2", "Upper": "3", "Top": "4"}[m.group(1)]),
    (re.compile(r"\bThe View [Ff]rom the Top Floor\b(?! of)"), "The View From the Last Chapter"),
    (re.compile(r"\bThe View ([Ff]rom) the Top(?: Floor)? of This(?: Particular)? (?:Floor|Staircase)\b"), lambda m: f"The View {m.group(1)} the End of This Chapter"),
    (re.compile(r"\bfrom here upward\b"), "from here on"),
    (re.compile(r"\b[Tt]he natural next floor up from this one\b"), simple("the natural next chapter after this one")),
    (re.compile(r"\b[Tt]he next floor up\b"), simple("the next chapter")),
    (re.compile(r"\b[Oo]ne floor (?:up|ahead|above this one)\b(?! the)"), simple("in the next chapter")),
    (re.compile(r"\b[Oo]ne floor (?:down|ago|below this one)\b"), simple("in the previous chapter")),
    (re.compile(r"\bthe floor just below this one\b"), simple("the chapter just before this one")),
    (re.compile(r"\b(many|several|two|three|a few) floors up\b(?: the [Tt]ower)?"), lambda m: cap(m.group(0), m.group(1).lower() + " chapters later")),
    (re.compile(r"\b(?:the |this )?Tower’s climb\b"), simple("the series")),
    (re.compile(r"\bbefore we (?:start climbing|start the climb)\b"), simple("before we begin")),
    (re.compile(r"\bbefore we climb further\b"), simple("before we go further")),
    (re.compile(r"\bbefore we climb on\b"), simple("before we move on")),
    (re.compile(r"\bbefore the (?:ascent begins|climb begins)\b"), simple("before we begin")),
    (re.compile(r"\bbefore the climb resumes\b"), simple("before we move on")),
    (re.compile(r"\bthe climb ahead\b"), simple("what lies ahead")),
    (re.compile(r"\bthe (whole|entire) climb\b"), lambda m: cap(m.group(0), f"the {m.group(1)} journey")),
    (re.compile(r"\bthe climb so far\b"), simple("the journey so far")),
    (re.compile(r"\b(?:a|the) long (?:climb|ascent)\b"), lambda m: cap(m.group(0), m.group(0).split()[0].lower() + " long road")),
    (re.compile(r"\b(?:the|a) climb\b(?! (?:rate|of|divided|is zero))"), lambda m: cap(m.group(0), m.group(0).split()[0].lower() + " journey")),
    (re.compile(r"\b(?:several |many |a few |two |three )?floors further up the Tower\b"), lambda m: m.group(0).replace("floors further up the Tower", "chapters later in the series")),
    (re.compile(r"\b(?:several |many |a few |two |three |one )floors? further up\b"), lambda m: m.group(0).replace("floors further up", "chapters later").replace("floor further up", "chapter later")),
    (re.compile(r"\bfurther up the Tower still\b"), simple("later in the series still")),
    (re.compile(r"\b[Ff]urther up (?:the|this) Tower\b|\b[Hh]igher up (?:the|this) Tower\b"), simple("later in the series")),
    (re.compile(r"\b[Ff]urther up still\b"), simple("later still")),
    (re.compile(r"\bfurther up\b(?! the (?:hill|slope|curve|page|graph))"), simple("later")),
    (re.compile(r"\bfurther down (?:the|this) Tower\b"), simple("earlier in the series")),
    (re.compile(r"\bfloors further down\b"), simple("chapters earlier")),
    (re.compile(r"\bthe Tower above us\b"), simple("the series ahead")),
    (re.compile(r"\beverything above us\b"), simple("everything that follows")),
    (re.compile(r"\bDirectly above us:"), simple("Next:")),
    (re.compile(r"\bImmediately above us waits\b"), simple("Next comes")),
    (re.compile(r"\b[Nn]ot too far above us\b"), simple("not far ahead")),
    (re.compile(r"\bfloors above us\b"), simple("chapters ahead")),
    (re.compile(r"\bfloor above us\b"), simple("chapter ahead")),
    (re.compile(r"\babove us\b"), simple("ahead")),
    (re.compile(r"\bfloors? below us\b"), lambda m: "chapters behind us" if m.group(0).startswith("floors") else "chapter back"),
    (re.compile(r"\bbelow us\b"), simple("behind us")),
    (re.compile(r"\bthe (whole|entire) building\b"), lambda m: cap(m.group(0), f"the {m.group(1)} book")),
    (re.compile(r"\bthis building\b"), simple("this book")),
    (re.compile(r"\bsame building\b"), simple("same book")),
    (re.compile(r"\b(throughout|across|in|of) the building\b(?! (?:block|committee))"), lambda m: m.group(1) + " the book"),
    (re.compile(r"\bthe building’s\b"), simple("the book’s")),
    # book name
    (re.compile(r"\b[Tt]he Mathematics Tower(’s)?"), lambda m: "Math, Actually" + ("’s" if m.group(1) else "")),
    (re.compile(r"\bMathematics Tower\b"), simple("Math, Actually")),
    (re.compile(r"\bground floor of (?:the |this )?(?:Tower|tower|building)\b"), simple("first chapter of the series")),
    (re.compile(r"\b[Tt]he ground floor\b"), simple("the first chapter")),
    (re.compile(r"\bground floor\b"), simple("first chapter")),
    (re.compile(r"\b(floor|room) by (?:floor|room)\b"), lambda m: cap(m.group(0), "chapter by chapter" if m.group(1).lower()=="floor" else "section by section")),
    (re.compile(r"\broom-by-room\b"), simple("section-by-section")),
    (re.compile(r"\bfloor after floor\b"), simple("chapter after chapter")),
    (re.compile(r"\b[Tt]his (?:very )?[Tt]ower’s\b"), simple("this series’")),
    (re.compile(r"\b[Tt]he [Tt]ower’s\b"), simple("the series’")),
    (re.compile(r"\b[Tt]his (?:very )?[Tt]ower\b"), simple("this series")),
    (re.compile(r"\b[Tt]he whole [Tt]ower\b"), simple("the whole series")),
    (re.compile(r"\b[Tt]he [Tt]ower\b(?! of)"), simple("the series")),
    (re.compile(r"\bTower’s\b"), "series’"),
    (re.compile(r"(?<![Pp]ower )\bTower\b"), "series"),
    (re.compile(r"\bstoreys?\b", re.I), lambda m: cap(m.group(0), "chapters" if m.group(0).lower().endswith('s') else "chapter")),
    (re.compile(r"\bfloors’"), simple("chapters’")),
    (re.compile(r"\bfloor’s\b"), simple("chapter’s")),
    (re.compile(r"\bFloors\b(?! \d)"), simple("Chapters")),
    (re.compile(r"\bfloors\b"), simple("chapters")),
    (re.compile(r"\bFloor\b(?! \d)"), simple("Chapter")),
    (re.compile(r"\bfloor\b"), simple("chapter")),
    (re.compile(r"\brooms’"), simple("sections’")),
    (re.compile(r"\broom’s\b"), simple("section’s")),
    (re.compile(r"\bRooms\b(?! \d)"), simple("Sections")),
    (re.compile(r"\brooms\b"), simple("sections")),
    (re.compile(r"\bRoom\b(?! \d)"), simple("Section")),
    (re.compile(r"\broom\b(?! \d)"), simple("section")),
]

def vocab_edits(text):
    """Return list of (start, end, replacement) for vocabulary rules."""
    prot = [(m.start(), m.end()) for m in PROTECT_RE.finditer(text)]
    taken = []
    edits = []
    def free(s, e):
        for a, b in prot + taken:
            if s < b and a < e: return False
        return True
    for rx, rep in RULES:
        for m in rx.finditer(text):
            if not free(m.start(), m.end()): continue
            r = rep(m) if callable(rep) else rep
            if r != m.group(0):
                edits.append((m.start(), m.end(), r))
            taken.append((m.start(), m.end()))
    return edits
