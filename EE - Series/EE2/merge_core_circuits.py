# -*- coding: utf-8 -*-
"""Grow Book 2 from the existing Core Circuits manuscript. Do not replace it."""

import math
import shutil
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

ROOT = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\EE - Series")
SRC = ROOT / "Core_Circuits_and_Components_Book2.docx"
OUT = ROOT / "EE2" / "Circuits_Components_and_Control_Book2.docx"
ROOT_COPY = ROOT / "Core_Circuits_and_Components_Book2.docx"

K = 1.380649e-23
JOHNSON = math.sqrt(4 * K * 290.0 * 100e3)
MU0 = 4.0 * math.pi * 1e-7
L_AIR = MU0 * 100**2 * 1e-4 / 0.020


def set_run(run, name="Calibri", size=11, bold=False, color=None):
    run.bold = bold
    run.font.name = name
    run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = run._element.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(a), name)


def add_after(paragraph, text, style="Normal"):
    new = paragraph.insert_paragraph_before("")
    # insert_paragraph_before puts the new para BEFORE paragraph.
    # We want AFTER, so insert before the following sibling instead.
    return new


def para_after(ref, text, style="Normal"):
    """Insert a new paragraph immediately after ref and return it."""
    new_p = ref._element.makeelement(qn("w:p"), {})
    ref._element.addnext(new_p)
    # wrap
    from docx.text.paragraph import Paragraph
    p = Paragraph(new_p, ref._parent)
    p.style = style
    run = p.add_run(text)
    if style == "Heading 1":
        set_run(run, "Amazon Ember", 18, True, RGBColor(0, 0, 255))
    elif style == "Heading 2":
        set_run(run, "Amazon Ember", 18, True, RGBColor(0, 0, 255))
    else:
        set_run(run, "Calibri", 11, False, RGBColor(0, 0, 0))
    return p


def replace_in_runs(p, old, new):
    # simple whole-paragraph replace to avoid split runs
    full = p.text
    if old not in full:
        return False
    # rebuild
    for r in list(p.runs):
        r.text = ""
    if p.runs:
        p.runs[0].text = full.replace(old, new)
    else:
        p.add_run(full.replace(old, new))
    return True


def find_heading(doc, prefix):
    for p in doc.paragraphs:
        if p.style and p.style.name == "Heading 1" and p.text.strip().startswith(prefix):
            return p
    return None


def find_following_heading2(start_para, title_prefix, stop_h1_prefix):
    seen = False
    for p in start_para._parent.paragraphs:
        if p._element is start_para._element:
            seen = True
            continue
        if not seen:
            continue
        st = p.style.name if p.style else ""
        if st == "Heading 1" and p.text.strip().startswith(stop_h1_prefix):
            return None
        if st == "Heading 2" and p.text.strip().startswith(title_prefix):
            return p
    return None


def insert_block_before(ref, items):
    """items: list of (style, text). Insert in order immediately before ref."""
    # Insert in reverse so order is preserved.
    cursor = ref
    created = []
    for style, text in reversed(items):
        p = cursor.insert_paragraph_before(text, style=style)
        if p.runs:
            if style == "Heading 1":
                set_run(p.runs[0], "Amazon Ember", 18, True, RGBColor(0, 0, 255))
            elif style == "Heading 2":
                set_run(p.runs[0], "Amazon Ember", 18, True, RGBColor(0, 0, 255))
            else:
                set_run(p.runs[0], "Calibri", 11, False, RGBColor(0, 0, 0))
        created.append(p)
        cursor = p
    created.reverse()
    return created


def main():
    if not SRC.exists():
        raise SystemExit(f"missing {SRC}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SRC, OUT)
    doc = Document(OUT)

    # --- retitle series map ---
    replacements = [
        (
            "This book is the second of twenty-one, together covering the full breadth of electrical engineering from first principles through to its specialized and emerging edges.",
            "This book is the second of nine, covering circuits, components, and the classical control loop that later sits under a robot model.",
        ),
        (
            "You do not need the other twenty books to use this one.",
            "You do not need the other eight books to use this one.",
        ),
        ("twenty-one", "nine"),
        ("twenty books", "eight books"),
        ("21-book", "nine-book"),
        ("21 books", "nine books"),
    ]
    for p in doc.paragraphs:
        t = p.text
        if not t:
            continue
        new = t
        for a, b in replacements:
            if a in new:
                new = new.replace(a, b)
        if new != t:
            if p.runs:
                p.runs[0].text = new
                for r in p.runs[1:]:
                    r.text = ""
            else:
                p.add_run(new)

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    t = p.text
                    if not t:
                        continue
                    new = t
                    for a, b in replacements:
                        if a in new:
                            new = new.replace(a, b)
                    # old 21-book titles left as historical names in a table
                    # are OK; we only rewrite counts above.
                    if new != t and p.runs:
                        p.runs[0].text = new
                        for r in p.runs[1:]:
                            r.text = ""

    # --- new sections before Chapter 5 Practice Problems ---
    ch5_practice = None
    seen_ch5 = False
    for p in doc.paragraphs:
        st = p.style.name if p.style else ""
        if st == "Heading 1" and p.text.strip().startswith("Chapter 5"):
            seen_ch5 = True
        if seen_ch5 and st == "Heading 2" and p.text.strip() == "Practice Problems":
            ch5_practice = p
            break
        if seen_ch5 and st == "Heading 1" and p.text.strip().startswith("Chapter 6"):
            break
    if ch5_practice is None:
        raise SystemExit("could not find Chapter 5 Practice Problems")

    ch5_extra = [
        ("Heading 2", "5.5 The Follower Is a Wire"),
        (
            "Normal",
            "The voltage follower, or unity-gain buffer, has no resistor in the loop at all. The output goes straight to the minus pin, and the signal is on the plus pin. That is the only configuration in which the feedback loop is a pure short. The virtual short forces the output to equal the plus input, so the gain is exactly one. The virtual open means the source sees essentially infinite impedance. The output impedance is near zero, so the stage can drive a heavy load without loading that source. That is the whole point: a high-impedance signal is buffered so the next stage does not drag it down. Because the noise gain is one, the bandwidth is the op-amp's full gain-bandwidth product, the widest bandwidth any closed-loop configuration gets.",
        ),
        (
            "Normal",
            "The inverting buffer is a different circuit, not a follower with a minus sign. The plus pin is grounded. An input resistor runs from the signal to the minus pin, and a feedback resistor runs from the output back to the minus pin. The loop still closes, but it closes through those two resistors. Equal resistors give a gain of minus one. The source sees only the input resistor, not an open circuit. Use the follower when the source cannot stand a load. Use the inverting buffer when you need the sign flip and can afford that resistor as the load.",
        ),
        ("Heading 2", "5.6 The Bode Limit, and a Declared Picture"),
        (
            "Normal",
            "The virtual short is exact only at DC. Open-loop gain falls at about twenty decibels per decade and crosses unity at the gain-bandwidth product. Closed-loop bandwidth is that product divided by the noise gain. For a non-inverting stage, noise gain and signal gain are the same number. For an inverter, the signal gain is minus Rf/Rin, but the noise gain is one plus Rf/Rin.",
        ),
        (
            "Normal",
            "Declared picture, a general-purpose shape: DC gain 100,000 (100 dB), gain-bandwidth product 1 MHz. The dominant pole then sits at 10 Hz. A noise gain of 100 leaves 10 kHz of closed-loop bandwidth. Phase margin is how far the phase still is from minus 180 degrees where loop gain crosses unity. About 60 degrees is comfortable. About 30 degrees rings. Less than that oscillates. Treat those three numbers as a design rule of thumb, not as a theorem.",
        ),
        ("Heading 2", "5.7 A Comparator Is Not a Bad Op-Amp"),
        (
            "Normal",
            "A comparator is the same input idea with the feedback loop left off on purpose. The virtual short is deliberately broken. The output slams to a rail according to which input is higher. The two ideal rules still apply at the inputs: essentially no current enters either pin. The output is a logic level, not a scaled copy of the input. Never put linear feedback around a comparator. The loop would fight the saturation the part is designed to reach. An open-collector output, the LM311 class, can only pull down; the pull-up sets the high level and may use another supply.",
        ),
        ("Heading 2", "5.8 Bias Current, Offset, and the Resistor's Own Noise"),
        (
            "Normal",
            "Bipolar inputs draw nanoampere bias currents. CMOS inputs are essentially open gates. JFET sits between them. The output stage is a separate choice. Offset is what remains when the inputs are tied together. Old parts trim it on null pins. New parts laser-trim or chop.",
        ),
        (
            "Normal",
            "Bias-current compensation puts a resistor in series with the plus input equal to the parallel combination of the two resistors on the minus side, so the DC drops match. It does not cancel that resistor's thermal noise. Johnson density is the square root of 4 k T R. Declared: k = 1.380649×10^−23 J/K, T = 290 K, R = 100 kΩ. Then √(4 k T R) = "
            f"{JOHNSON*1e9:.1f} nV/√Hz, which is 40 nV/√Hz for this book. That is why those resistors stay as small as the bias current allows. Bipolar wants them small. CMOS does not.",
        ),
        (
            "Normal",
            "Key idea. Chapter 5.1 already gave the two rules. This section is where they stop being exact, and where a comparator refuses to be an amplifier.",
        ),
    ]
    insert_block_before(ch5_practice, ch5_extra)

    # --- note at start of Chapter 9 ---
    ch9 = find_heading(doc, "Chapter 9")
    if ch9 is None:
        raise SystemExit("missing Chapter 9")
    # insert after the heading paragraph: find next paragraph after ch9
    nxt = ch9._element.getnext()
    from docx.text.paragraph import Paragraph as Pwrap
    # Use insert on the paragraph that follows heading
    follow = None
    seen = False
    for p in doc.paragraphs:
        if p._element is ch9._element:
            seen = True
            continue
        if seen:
            follow = p
            break
    if follow is not None:
        insert_block_before(
            follow,
            [
                (
                    "Normal",
                    "Book 1 already derived inductance from Faraday and Ampere: voltage is L di/dt, and a long solenoid is μ0 N² A / ℓ. This chapter does not derive that again. It sizes a catalog part. "
                    f"Declared air solenoid, 100 turns, 20 mm long, 1 cm² of area: L = {L_AIR*1e6:.1f} µH. A ferrite at relative permeability 1000, still linear, would be a thousand times that, {L_AIR*1e6:.1f} mH. "
                    "Saturation current is where the core stops being linear. Self-resonant frequency is where winding capacitance takes over and the part stops acting like an inductor. "
                    "Line-frequency iron, switch-mode ferrite, pulse transformers, and RF baluns are four shelves in Book 8. They are not this chapter.",
                )
            ],
        )

    # --- Chapter 10 before Appendix A ---
    app_a = find_heading(doc, "Appendix A")
    if app_a is None:
        raise SystemExit("missing Appendix A")
    ch10 = [
        ("Heading 1", "Chapter 10 — The Loop Under the Model"),
        (
            "Normal",
            "Book 9 names the 2026 robots and the four layers: general model, task planner, motion tracker, mechanism. This book owns the tracker. It does not repeat the product names or the success percentages.",
        ),
        (
            "Normal",
            "A joint tracker at 200 Hz has a period of 1/200 s, which is 5 ms. Five milliseconds is slow for a switching regulator and fast for a language model. It is the right speed for a joint that must not wait on a data center. The safety controller is not that model. When they disagree, the safety controller is the one allowed to move the joint. Åström and Murray, or Nise, are the books for this loop.",
        ),
        (
            "Normal",
            "The same Bode habits from Chapter 5 apply: a plant, a compensator, a phase margin. A robot policy does not replace that loop. The model proposes. The tracker and the safety layer dispose.",
        ),
        ("Normal", "Key idea. The 200 Hz tracker is a 5 ms period. That arithmetic lives only here."),
        ("Heading 2", "Practice Problems"),
        ("Normal", "1. A joint tracker runs at 200 Hz. What is the period, and why is that not the sample rate of a language model?"),
        ("Normal", "2. Name the layer that must still work when the vision-language model is wrong."),
        ("Normal", "3. A follower and an inverting unity-gain stage both have |gain| = 1. Which one loads a fragile source, and why?"),
    ]
    insert_block_before(app_a, ch10)

    # Appendix B: add Chapter 10 solutions before Glossary if possible
    app_c = find_heading(doc, "Appendix C")
    if app_c is not None:
        insert_block_before(
            app_c,
            [
                ("Heading 2", "Chapter 10 Solutions"),
                (
                    "Normal",
                    "1. Period = 1/200 s = 5 ms. A language model is not answering a joint every five milliseconds; the classical loop is. "
                    "2. The independent safety controller. Digit-class machines are built that way. "
                    "3. The inverting buffer. Its source sees Rin. The follower's source sees the op-amp input.",
                ),
            ],
        )

    # Replace the 21-row series map with the nine-book map.
    nine = [
        ("Book", "Covers"),
        ("1. Foundations", "Physics, mathematics, and circuit theory"),
        ("2. Circuits, Components, and Control (this book)", "Analog and digital, op-amps, passives, the classical loop"),
        ("3. Semiconductor Physics and Devices", "Diodes, BJTs, MOSFETs, FinFET, compound semiconductors"),
        ("4. RF, Microwave, and Antennas", "Matching, lines, microwave, mmWave, antennas"),
        ("5. Communications, Wireless, and SDR", "Modulation, band plans, DSP and software radio"),
        ("6. Transceivers and High-Power RF", "Noise, PLL, PAs, combiners, radar"),
        ("7. EMC, Simulation, and Test", "Emissions, immunity, solvers, the accredited lab"),
        ("8. Power and Energy", "Regulators, magnetics, the grid, the rack"),
        ("9. Packaging, Layout, and Emerging", "Boards, packages, 2026 compute, robots, MEMS"),
    ]
    if doc.tables:
        tbl = doc.tables[0]
        # Clear extra rows if any, rewrite first 10.
        while len(tbl.rows) > len(nine):
            tr = tbl.rows[-1]._tr
            tr.getparent().remove(tr)
        while len(tbl.rows) < len(nine):
            tbl.add_row()
        for row, (a, b) in zip(tbl.rows, nine):
            if len(row.cells) >= 2:
                row.cells[0].text = a
                row.cells[1].text = b

    doc.save(OUT)
    # Keep the series-root Book 2 filename pointing at the grown volume as well.
    shutil.copy2(OUT, ROOT / "Circuits_Components_and_Control_Book2.docx")
    words = 0
    d2 = Document(OUT)
    for p in d2.paragraphs:
        words += len(p.text.split())
    print(f"wrote {OUT}")
    print(f"paragraph words ~ {words}")
    print(f"johnson_nV {JOHNSON*1e9:.3f} L_air_uH {L_AIR*1e6:.2f}")


if __name__ == "__main__":
    raise SystemExit(
        "Old Core_Circuits_and_Components_Book2.docx was a 21-volume leftover and is gone. "
        "Canonical Book 2 is EE2/Circuits_Components_and_Control_Book2.docx"
    )
