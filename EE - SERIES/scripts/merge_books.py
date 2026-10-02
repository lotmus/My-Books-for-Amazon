# -*- coding: utf-8 -*-
"""Merge EE sources nine -> seven (2026-10-01).
Book 4 = old 4 (Ch 1-19, Part I) + old 6 (Ch 20-40, Part II).
Book 7 = old 9 Ch 1-20 (Part I) + old 7 (Ch 21-28, Part II) + old 9 Robot (Ch 29, Part III).
Books 5 and 6 (= old 5, old 8) get the cross-reference pass only.
Usage: python merge_books.py <ee_root_with_EEn_new_dirs> <out_root>"""
import re, sys, shutil
from pathlib import Path
from xref import xref
root, out = Path(sys.argv[1]), Path(sys.argv[2])
def L(p): return Path(p).read_text(encoding="utf-8").splitlines()
def W(p, lines): p.parent.mkdir(parents=True, exist_ok=True); p.write_text("\n".join(lines) + "\n", encoding="utf-8")
def tagged(lines, tag): return [l for l in lines if l.startswith(tag + ":")]

# ---------- Book 4 ----------
b4 = out / "Book4"; o4, o6 = root / "EE4_new", root / "EE6_new"
for n in range(1, 20):
    lines = L(o4 / f"src/ch{n:02d}.txt")
    if n == 1:
        lines.insert(0, "PART: Part I. Passive Structures: Lines, Matching, Filters, and Antennas")
        lines = [l.replace("and switches and mixers as passive circuits.", "and RF switches. Part II, Chapters 20 to 40, turns to the active radio: amplifiers, receivers, oscillators, synthesizers, and the measurements that prove them.") for l in lines]
    if n == 19:
        cut = next(i for i, l in enumerate(lines) if l.startswith("H2: 19.3"))
        prac = next(i for i, l in enumerate(lines) if l.startswith("H2: Practice"))
        pr, an = tagged(lines, "PR")[:3], tagged(lines, "ANS")[:3]
        lines = lines[:cut] + ["H2: Practice"] + pr + an
        lines[0] = "H1: Chapter 19. RF Switches"
        lines[1] = ("P: Every radio selects paths: one antenna or another, one band filter or another, the transmit or the receive side. "
                    "The element that does it is a switch, a PIN diode, a silicon-on-insulator transistor, or a MEMS contact, and at RF it is analyzed with the impedances and reflection coefficients of this book. "
                    "This chapter computes a switch's insertion loss and isolation and shows how series and shunt elements combine. The passive mixer, which is also a switch, is treated with the other mixers in Book 6's Chapter 10.")
    lines = [xref(l, 4) for l in lines]
    W(b4 / f"src/ch{n:02d}.txt", lines)
for n in range(1, 22):
    lines = L(o6 / f"src/ch{n:02d}.txt")
    if n == 1:
        lines.insert(0, "PART: Part II. Active Circuits: Amplifiers, Receivers, Oscillators, and Synthesizers")
    if n == 10:
        i = next(i for i, l in enumerate(lines) if l.startswith("H2: 10.4"))
        lines[i] = lines[i].replace("10.4", "10.5")
        lines[i:i] = ["H2: 10.4 The passive mixer as a switch",
            "P: Multiplying a signal by a square wave at the LO frequency is the same as switching its polarity at that rate, which is what a ring of four diodes or four transistors does in a double-balanced mixer. The square wave's fundamental has an amplitude of 4/π times its peak, and the product contains the sum and difference frequencies. For an ideal commutating mixer, the fraction of the RF power that reaches the wanted IF is (2/π)², a conversion loss of 3.9 dB. Real diode mixers show 6 to 7 dB because of diode resistance, the transformers or baluns, and imperfect switching. The switches themselves are the series and shunt elements of Book 4's Chapter 19.",
            "EQ: L_conv,ideal = −20 log₁₀(2/π) = 3.92 dB",
            "P: The balance of a double-balanced mixer cancels the LO at the RF and IF ports and the RF at the IF port, so port-to-port isolation, often 30 to 40 dB, depends on how well the baluns and diodes are matched. Because the switches are driven hard by the LO, a passive mixer is quite linear; a rule of thumb for diode mixers is an input third-order intercept about 10 dB above the LO drive."]
        j = next(i for i, l in enumerate(lines) if l.startswith("ANS:"))
        lines[j:j] = ["PR: What is the ideal conversion loss of a commutating mixer?",
                      "PR: Estimate the IIP3 of a diode mixer driven with +7 dBm of LO."]
        lines += ["ANS: 3.92 dB.", "ANS: About +17 dBm."]
    if n == 15:
        lines = [l + " The ferrite circulator of Book 4's Chapter 15 is the passive starting point, and its leakage paths are worked there." if l.startswith("P: Transmitting and receiving at once on the same frequency") else l for l in lines]
    lines = [xref(l, 6) for l in lines]
    W(b4 / f"src/ch{n + 19:02d}.txt", lines)
f4, f6 = L(o4 / "front.txt"), L(o6 / "front.txt")
front = ["TITLE: RF, Microwave, and Transceivers",
 "SUB: Book 4 of the Electrical Engineering Series",
 "COPY: Copyright © 2026 Lothar J. Musiol. All rights reserved. Kindle edition.",
 "SUBTITLE: Lines, Matching, Filters, Antennas, Power Amplifiers, Receivers, and Synthesizers, from 1 GHz to Millimeter Wave",
 "HOW: Books 1 to 3 built circuits on the assumption that a wire has no length. This book drops that assumption and follows a radio from the copper to the air. Part I, Chapters 1 to 19, is the passive structure: the transmission line and reflection, lumped and distributed matching and the Smith chart, scattering parameters, resonators, filters and waveguide, the antenna and the array, couplers and dividers, microstrip and stripline, broadband matching, cavities, small antennas and horns, propagation, ferrites and circulators, antenna measurement, noise in passive networks, a filter carried from specification to layout, and RF switches.",
 "HOW: Part II, Chapters 20 to 40, is the active radio. It follows a transmitter from the device to the antenna, through the load line, the amplifier classes, the Doherty amplifier, heat and combining, and then the receiver's noise and dynamic range, the oscillator and the PLL, and radar. Chapters 28 to 40 deepen the chain: the low-noise amplifier, mixers and frequency planning, the link budget, bias and ruggedness, vacuum tubes, RF exposure, transceiver isolation, class E and F design, envelope tracking and outphasing, amplifier measurement, digital predistortion, frequency synthesis, and power detection and control.",
 "HOW: Each chapter states the question it answers, develops the picture in words, and then works it through with declared numbers. Every number in a worked example was computed, not estimated, and the answers to every practice problem are in Appendix B. The book uses one set of reference values throughout: the speed of light is 2.998 × 10⁸ m/s, the system reference impedance is 50 Ω, and the reference board has εr = 3.55. The link-budget anchor is the Friis path factor at 2.45 GHz over 100 m between isotropic antennas, 9.48 × 10⁻⁹, or −80.2 dB, and the load-line anchors for 100 W are Ropt = 10.13 Ω at 50 V with a 5 V knee and 3.13 Ω at 28 V with a 3 V knee.",
 "HOW: The series gives each subject one home. Device physics, including why gallium nitride withstands high voltage, is Book 3's. The waveform, OFDM, and the band plan are Book 5's. Power conversion, including pulse modulators for tube transmitters, is Book 6's. Laminate properties at 10 GHz, packages, emission limits, test chambers, and certification are Book 7's. Readers who want the next level of depth should turn to the texts in Appendix C; this book's explanations, examples, and problems are its own."]
front += [xref(l, 4) for l in tagged(f4, "CONST")] + [xref(l, 6) for l in tagged(f6, "CONST")]
front += [xref(l, 4) for l in tagged(f4, "SRC")] + [xref(l, 6) for l in tagged(f6, "SRC")]
W(b4 / "front.txt", front)

# ---------- Book 7 ----------
b7 = out / "Book7"; o9, o7 = root / "EE9_new", root / "EE7_new"
for n in range(1, 21):
    lines = L(o9 / f"src/ch{n:02d}.txt")
    if n == 1:
        lines.insert(0, "PART: Part I. Packages, Boards, Power, and Heat")
    lines = [xref(l, 9) for l in lines]
    W(b7 / f"src/ch{n:02d}.txt", lines)
for n in range(1, 9):
    lines = L(o7 / f"src/ch{n:02d}.txt")
    if n == 1:
        lines.insert(0, "PART: Part II. EMC, Simulation, and Test")
    lines = [xref(l, 7) for l in lines]
    W(b7 / f"src/ch{n + 20:02d}.txt", lines)
lines = L(o9 / "src/ch21.txt"); lines.insert(0, "PART: Part III. Where the Series Meets")
W(b7 / "src/ch29.txt", [xref(l, 9) for l in lines])
f9, f7 = L(o9 / "front.txt"), L(o7 / "front.txt")
front = ["TITLE: Packaging, Layout, EMC, and Test",
 "SUB: Book 7 of the Electrical Engineering Series",
 "COPY: Copyright © 2026 Lothar J. Musiol. All rights reserved. Kindle edition.",
 "SUBTITLE: Advanced Packages, Power Delivery, Board Materials, Layout, Cooling, Emissions, Immunity, and the Accredited Lab",
 "HOW: The earlier books designed circuits, devices, radios, and converters. This last book is about where they meet the physical product: the package that holds the chips, the copper that carries their current and signals, the heat that must leave, and the emissions and immunity tests every product must pass before it can be sold.",
 "HOW: Part I, Chapters 1 to 20, covers packages and boards: the 2026 compute picture, advanced packages, power delivery, board materials, layout, heat, MEMS, yield and chiplets, the package as a circuit, reliability, decoupling, stack-up, crosstalk, loss and equalization, optical interconnect, inertial sensors, the HBM stack, antenna-in-package modules, design for manufacture and test, and interconnect measurement. Part II, Chapters 21 to 28, covers EMC: why a board radiates, common mode on cables, methods and limits, detectors, the semi-anechoic chamber, conducted emissions and the LISN, immunity and the radio report, and the simulation flow and the day in the lab. Chapter 29 places the robot, which uses nearly every book at once.",
 "HOW: Each chapter states its question, develops the idea in words, and works it through with declared numbers. Every number was computed, and the answers to every practice problem are in Appendix B.",
 "HOW: The series gives each subject one home. Conversion efficiency and the regulators that make the processor's current are Book 6's. Transmission lines, matching, antennas, and the transmitter are Book 4's. The waveform and the band plan are Book 5's. This book uses those results where it needs them and does not recompute them. The texts in Appendix C go deeper; this book's explanations, examples, and problems are its own."]
front += [xref(l, 9) for l in tagged(f9, "CONST")] + [xref(l, 7) for l in tagged(f7, "CONST")]
front += [xref(l, 9) for l in tagged(f9, "SRC")] + [xref(l, 7) for l in tagged(f7, "SRC")]
W(b7 / "front.txt", front)

# ---------- Books 5 and 6 (old 5, old 8) ----------
for new, old, d in ((5, 5, "EE5_new"), (6, 8, "EE8_new")):
    dst = out / f"Book{new}"
    for p in sorted((root / d / "src").glob("ch*.txt")):
        W(dst / "src" / p.name, [xref(l, old) for l in L(p)])
    W(dst / "front.txt", [xref(l, old) for l in L(root / d / "front.txt")])
FIXES = [
 ("Book4/src/ch01.txt", "laminate properties at 10 GHz and the package belong to Book 7; emissions limits belong to Book 7", "laminate properties at 10 GHz, the package, and emissions limits belong to Book 7"),
 ("Book4/src/ch17.txt", "Part II owns the receiver's noise cascade;", "Chapter 25 develops the receiver's noise cascade;"),
 ("Book4/src/ch17.txt", "By Part II's cascade,", "By the cascade of Chapter 25,"),
 ("Book4/src/ch28.txt", "is treated in Part I;", "is treated in Chapter 5;"),
 ("Book7/src/ch29.txt", "electromagnetic compatibility to meet (Part II)", "electromagnetic compatibility to meet (Part II, Chapters 21 to 28)"),
]
for f, a, b in FIXES:
    p = out / f; t = p.read_text(encoding="utf-8"); assert a in t, (f, a); p.write_text(t.replace(a, b), encoding="utf-8")
print("done")
