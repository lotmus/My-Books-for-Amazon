# -*- coding: utf-8 -*-
"""Build the complete Book 4 Kindle textbook. Worked numbers come from this file."""

from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from lib_ee_doc import add_p, new_book, word_count  # noqa: E402

OUT = Path(__file__).resolve().parent / "RF_Microwave_and_Antennas_Book4.docx"

# Locked geometry and constants. Do not silently change them in one chapter.
C = 2.99792458e8
MU0 = 4.0 * math.pi * 1e-7
EPS0 = 8.854187817e-12
ETA0 = 120.0 * math.pi
F245 = 2.45e9
R100 = 100.0
LAM245 = C / F245
SPACE = (LAM245 / (4.0 * math.pi * R100)) ** 2
SPACE_DB = 10.0 * math.log10(SPACE)
# Series spoken pair from the one-home note (decade form). The computed pair above is the one to carry.
SPACE_SPOKEN = 9.5e-8
SPACE_SPOKEN_DB = -70.2
ZQ = math.sqrt(25.0 * 50.0)
ER_RF = 3.55  # RO4000-class working value; 10 GHz mill table is Book 9
H_M = 0.001524  # 60 mil
SIG_CU = 5.8e7
DF_RF = 0.0027
Z0 = 50.0


def h1(doc, text):
    add_p(doc, text, style="Heading 1")


def h2(doc, text):
    add_p(doc, text, style="Heading 2")


def p(doc, text, italic=False, center=False):
    add_p(doc, text, italic=italic, center=center)


def key(doc, text):
    add_p(doc, "Key idea. " + text)


def db10(x):
    return 10.0 * math.log10(x)


def db20(x):
    return 20.0 * math.log10(x)


SOLS: list[tuple[str, list[str]]] = []


def practice(doc, title: str, items: list[str], answers: list[str]):
    h2(doc, "Practice")
    for i, q in enumerate(items, 1):
        p(doc, f"{i}. {q}")
    SOLS.append((title, [f"{i}. {a}" for i, a in enumerate(answers, 1)]))


def front(doc):
    p(
        doc,
        "Book 4 of 9. This volume is the radio-frequency, microwave, and antenna book. "
        "It absorbs what used to be four thin radio books in an older twenty-one-book split: "
        "matching and lines, microwave networks, antennas, and millimeter-wave hardware. "
        "Millimeter wave is not a tenth book. It is this book at a shorter wavelength.",
        italic=True,
        center=True,
    )
    h1(doc, "How to Use This Book")
    p(
        doc,
        "Bowick is the on-ramp. A first matching network, a first glance at the Smith chart, "
        "a first lumped filter, and a first small-signal amplifier are his territory, rewritten "
        "here in this series' voice. Pozar, or Steer volumes 1 to 3, is the microwave text you "
        "keep on the desk when a cavity, a waveguide mode, or a coupled-line coupler stops "
        "being a cartoon. This book cites those names. It does not paste their pages. Book 1 "
        "already taught complex numbers, phasors, and a first Smith-chart walk. This book uses "
        "that chart. It does not teach j again.",
    )
    p(
        doc,
        "A TEM line is a delay and an impedance. Matching is the craft of sitting between two "
        "resistances, or between a resistance and a complex load, without throwing power back "
        "at the generator. Antennas turn a guided wave into a free-space wave and back. Arrays "
        "point that wave. Friis multiplies the two antenna gains by a space factor that this "
        "file computes once, at 2.45 GHz and 100 m, and then refuses to recompute with a "
        "different story. Radar range to the fourth power, with pulse width and duty cycle, "
        "is Book 6. This book only supplies the antenna gains that go into that equation.",
    )
    p(
        doc,
        "Power amplifiers, load lines, and the statement that one decibel after the last PA "
        "is one decibel of EIRP live in Book 6. The legal mask and the chamber live in Book 7. "
        "Dielectric constants and dissipation factors quoted at 10 GHz, and the mill-to-mill "
        "scatter of those numbers, live in Book 9. This book will say RO4000-class and will "
        "use εr = 3.55 as a working value. It will not reprint Book 9's 10 GHz table.",
    )
    p(
        doc,
        "Each chapter has two numerical worked examples. The arithmetic is computed in the "
        "builder that wrote this file, so a later chapter cannot quietly adopt a different "
        "speed of light or a different 2.45 GHz wavelength. Four practice problems close each "
        "chapter. Solutions sit in the appendix, not in a footnote you will skip.",
    )
    p(
        doc,
        "American spelling. Original prose. Kindle typography: Heading 1 and Heading 2 in "
        "Amazon Ember, body in Calibri. Author: Lothar J. Musiol, 2026. Nine books, not twenty-one.",
    )
    key(
        doc,
        "One microwave book. Antennas live here. Watts live in Book 6. The chamber lives in Book 7. "
        "The 10 GHz laminate table lives in Book 9.",
    )

    h2(doc, "The nine-book map, from this desk")
    p(
        doc,
        "Book 1 is foundations: laws, passives, phasors, Fourier, the solenoid law, and a first "
        "Smith chart. Book 2 is circuits, parts, the op-amp, and the control loop. Book 3 is "
        "devices, from the crystal through FinFET and GAA, with GaN named as a film and a HEMT, "
        "not as a load-line. Book 4, this volume, is the guided wave and the antenna. Book 5 is "
        "the modem and the 2026 band plan. Book 6 is the transmitter chain and high-power RF. "
        "Book 7 is EMC, simulation, and the test lab. Book 8 is power and energy. Book 9 is "
        "packaging, layout, and the 2026 systems snapshot.",
    )
    p(
        doc,
        "If you came here from a phone schematic, you will want Book 5 for the waveform and "
        "Book 6 for the PA. If you came here from a radar proposal, you will want this book's "
        "array chapter for grating lobes and Book 6 for the R^4 budget. If you came here from "
        "a board stackup meeting, you will want Book 9 for the mill data and this book for "
        "what a 0.0027 dissipation factor does to a 2.45 GHz line.",
    )


def ch01(doc):
    h1(doc, "Chapter 1. One Microwave Book")
    p(
        doc,
        "Radio frequency is a frequency. Microwave is a wavelength that has become comparable "
        "to the hardware. The split is cultural, not physical. A 2.45 GHz Wi-Fi trace on a "
        "phone is already a microwave circuit even if the marketing slide says RF. A 60 Hz "
        "busbar is not, even if it carries a megawatt. The Maxwell equations do not change "
        "their names at 1 GHz. What changes is whether you may still treat a copper run as "
        "a lumped resistor, or whether you must treat it as a delay with a characteristic "
        "impedance.",
    )
    p(
        doc,
        "Bowick wrote the book that lets a working engineer match a transistor, read a Smith "
        "chart without fear, and cut a first low-pass filter before lunch. That is the right "
        "on-ramp. It is not the last word. Pozar's microwave engineering text, or Steer's three "
        "open volumes, take the same reader into waveguide, coupled lines, cavities, and the "
        "network theory that makes a coupler a matrix instead of a guess. This series uses "
        "both layers. The early chapters talk like Bowick. The later chapters talk like a "
        "microwave desk. Neither layer is a paste.",
    )
    h2(doc, "1.1 Lumped until it is not")
    p(
        doc,
        "A part is lumped when the voltage at one end of it is the voltage at the other end "
        "at the same instant, to the accuracy you care about. That fails when the physical "
        "length is a meaningful fraction of a wavelength. A useful shop rule, not a law, is "
        "to start worrying at about a twelfth of a wavelength and to stop pretending at a "
        "quarter. At 2.45 GHz the free-space wavelength is "
        f"{LAM245 * 100:.2f} cm. A twelfth of that is {LAM245 / 12 * 1000:.1f} mm. A 15 mm "
        "trace is already a piece of line. On a board with εr = 3.55 the guided wavelength "
        f"is shorter by √3.55 = {math.sqrt(ER_RF):.3f}, so the same 15 mm is a larger "
        "fraction still.",
    )
    p(
        doc,
        "Lumped matching still works at 2.45 GHz. It works less well at 28 GHz, and it is "
        "usually the wrong first drawing at 77 GHz. Distributed matching — stubs, quarter-wave "
        "transformers, coupled lines — takes over because the parts you would have soldered "
        "have become the copper itself. That is not a new subject. It is the same matching "
        "problem with the inductor drawn as a length.",
    )
    h2(doc, "1.2 Millimeter wave is a shorter λ")
    p(
        doc,
        "Millimeter wave means, roughly, 30 GHz to 300 GHz, wavelengths from a centimeter "
        "down to a millimeter. Automotive radar at 77 GHz, a 28 GHz 5G panel, and a 60 GHz "
        "indoor link are all this book. What changes is the loss per millimeter, the size of "
        "a waveguide, the beamwidth of a given aperture, and how much a bond wire or an etch "
        "tolerance counts. The equations are the same. There is no second mmWave volume in "
        "this series, and there will not be one later as a surprise.",
    )
    p(
        doc,
        "Packaging becomes the circuit. A bond wire that was a nuisance at 2 GHz is an "
        "inductor you must budget at 28 GHz. A 50 μm etch error that was nothing on a "
        "2.45 GHz 50 Ω microstrip is a real fraction of a 77 GHz patch. Book 9 owns the "
        "laminate call-out and the 10 GHz Df/Dk table. This book owns the electrical "
        "consequence: thinner copper, tighter etch, PTFE or RO3003-class material when the "
        "hydrocarbon resin starts to cost you decibels you do not have.",
    )
    h2(doc, "1.3 What this book will not steal")
    p(
        doc,
        "A small-signal RF amplifier, its S-parameters, and the Rollett K factor plus the μ "
        "stability tests live here, because they are network questions. The power amplifier, "
        "its load line, its class, and its heat live in Book 6. If you came here for watts, "
        "you are in the wrong room. If you came here to know whether a pHEMT oscillator will "
        "take off when you present it with a long cable, you are in the right room.",
    )
    key(
        doc,
        "Shorter wavelength is not a new subject. It is the same subject with less forgiveness.",
    )
    h2(doc, "Worked Example 1.1")
    lam12 = LAM245 / 12
    lam12_g = (LAM245 / math.sqrt(ER_RF)) / 12
    p(
        doc,
        "At 2.45 GHz, compute the free-space wavelength and one-twelfth of it. Repeat "
        "one-twelfth on a guided wave in εr = 3.55, using v = c/√εr. Report millimeters.",
    )
    p(
        doc,
        f"λ0 = c/f = {C:.8e}/{F245:.2e} = {LAM245:.4f} m = {LAM245 * 100:.2f} cm. "
        f"λ0/12 = {lam12 * 1000:.2f} mm. Guided λg = λ0/√εr = {LAM245 / math.sqrt(ER_RF):.4f} m, "
        f"so λg/12 = {lam12_g * 1000:.2f} mm. A 10 mm chip inductor is already a distributed "
        "object on that board.",
    )
    h2(doc, "Worked Example 1.2")
    lam28 = C / 28e9
    lam77 = C / 77e9
    p(
        doc,
        "Compute free-space wavelength at 28 GHz and at 77 GHz. Compare each to the 2.45 GHz "
        "wavelength as a ratio. This is the whole mmWave argument in two numbers.",
    )
    p(
        doc,
        f"λ(28 GHz) = {lam28 * 1000:.2f} mm. λ(77 GHz) = {lam77 * 1000:.2f} mm. "
        f"2.45 GHz / 28 GHz = {F245 / 28e9:.3f}, so the 28 GHz wave is "
        f"{LAM245 / lam28:.2f} times shorter. 2.45 GHz / 77 GHz = {F245 / 77e9:.3f}, "
        f"so the 77 GHz wave is {LAM245 / lam77:.2f} times shorter. A structure that was "
        "λ/20 at Wi-Fi is more than half a wave on the radar bumper.",
    )
    practice(
        doc,
        "Chapter 1",
        [
            "A 20 mm trace lives on εr = 3.55 at 2.45 GHz. What fraction of a guided wavelength is it?",
            "Repeat the fraction at 10 GHz on the same εr. Do not quote a 10 GHz Df. That table is Book 9.",
            "Why does this series refuse a separate millimeter-wave book?",
            "Name the book that owns PA watts, the book that owns the chamber, and the book that owns 10 GHz laminate Df/Dk.",
        ],
        [
            f"λg = {LAM245 / math.sqrt(ER_RF):.4f} m = {LAM245 / math.sqrt(ER_RF) * 1000:.1f} mm. 20 / {LAM245 / math.sqrt(ER_RF) * 1000:.1f} = {0.020 / (LAM245 / math.sqrt(ER_RF)):.3f} of a guided wave (about {0.020 / (LAM245 / math.sqrt(ER_RF)) * 360:.0f} electrical degrees).",
            f"λg(10 GHz) = {C / 10e9 / math.sqrt(ER_RF) * 1000:.1f} mm. 20 / that is {0.020 / (C / 10e9 / math.sqrt(ER_RF)):.3f} of a guided wave.",
            "Maxwell's equations do not change. Loss, size, beamwidth, and fabrication tolerance change. Those are chapters, not a new volume.",
            "Book 6 owns watts. Book 7 owns the chamber. Book 9 owns the 10 GHz Df/Dk mill table.",
        ],
    )


def ch02(doc):
    h1(doc, "Chapter 2. TEM Lines")
    p(
        doc,
        "A transmission line is two conductors and a field that fits between them so that "
        "the same voltage and current pattern can slide along the length. TEM means the "
        "electric and magnetic fields in the cross-section are transverse: no E or H along "
        "the direction of travel, in the ideal picture. Coax is the clean TEM example. "
        "A stripline, a trace buried between two planes, is TEM to a very good approximation. "
        "Microstrip, a trace on top of a dielectric over a plane, is quasi-TEM. A little "
        "field lives in air, a little lives in the board, so the effective dielectric "
        "constant sits between 1 and εr. Waveguide is not TEM. It gets its own chapter.",
    )
    p(
        doc,
        "Two numbers characterize a lossless TEM line for circuit work: the characteristic "
        "impedance Z0 and the delay per meter, or equivalently the phase velocity. "
        "Z0 = √(L/C) and v = 1/√(LC), where L and C are the series inductance and shunt "
        "capacitance per meter. The product LC is set by the dielectric if the conductors "
        "are perfect. The ratio L/C is set by the geometry. That is why a fatter trace over "
        "the same height is a lower-impedance line: more C, about the same or slightly less L.",
    )
    h2(doc, "2.1 Fifty ohms is a convention")
    p(
        doc,
        "Fifty ohms won because it sits near a compromise between power handling and loss "
        "in coax, and because the industry standardized connectors and instruments there. "
        "Seventy-five ohms won television and some long runs because it is closer to the "
        "minimum-loss coax impedance in polyethylene. Ninety-three ohms appears in older "
        "computer cabling. None of these is a law of nature. A power-amplifier drain line "
        "in Book 6 may be 10 Ω or 25 Ω on purpose. A 50 Ω system is what you join to a "
        "network analyzer. It is not what every millimeter of copper must be.",
    )
    p(
        doc,
        "On a board, you choose Z0 by width, height, and dielectric. A working RO4000-class "
        "stack with εr = 3.55 and 60 mil of dielectric is a common teaching stack in this "
        "book. The exact closed-form microstrip equations have more terms than a Kindle "
        "page wants. The fact you need is that a 50 Ω microstrip on that stack is a specific "
        "width, and that width scales almost with height. Halve the dielectric thickness and "
        "you roughly halve the width that holds 50 Ω.",
    )
    h2(doc, "2.2 Coax as the clean picture")
    p(
        doc,
        "A coaxial line with inner radius a, outer radius b, and dielectric εr has "
        "Z0 = (60/√εr) ln(b/a) ohms, and velocity v = c/√εr. The 60 is 120π / 2π, the "
        "free-space impedance divided by 2π. You can derive it from capacitance per meter "
        "C = 2πε/ln(b/a) and v = 1/√(LC) with L = μ ln(b/a) / 2π. This book uses the 60 "
        "form for hand work. A 50 Ω polyethylene coax (εr ≈ 2.25) needs b/a ≈ 3.3. Air "
        "dielectric needs b/a ≈ e^(50/60) ≈ 2.3, which is why air lines look tight.",
    )
    h2(doc, "2.3 Delay is the other half")
    p(
        doc,
        "A line of length ℓ has electrical length θ = βℓ = 2π ℓ / λg. At a quarter-wave, "
        "θ = 90°. At an eighth-wave, θ = 45°, and a shorted eighth-wave looks like an "
        "inductor. Time delay is ℓ / v. A nanosecond is about 30 cm in air and about "
        f"{0.30 / math.sqrt(ER_RF) * 100:.1f} cm in εr = 3.55. Digital people quote delay "
        "in picoseconds per inch. Microwave people quote degrees at a frequency. Both are "
        "the same number if you keep λg honest.",
    )
    key(
        doc,
        "A TEM line is Z0 and delay. Fifty ohms is a connector habit, not a commandment.",
    )
    h2(doc, "Worked Example 2.1")
    ba = 3.5
    er_pe = 2.10
    z_coax = (60.0 / math.sqrt(er_pe)) * math.log(ba)
    p(
        doc,
        f"A PTFE coax has εr = {er_pe:.2f} and b/a = {ba:.1f}. Find Z0 and the one-way "
        "delay of a 20 cm length.",
    )
    p(
        doc,
        f"Z0 = (60/√{er_pe:.2f}) ln({ba:.1f}) = {60.0 / math.sqrt(er_pe):.3f} × {math.log(ba):.4f} "
        f"= {z_coax:.2f} Ω. v = c/√εr = {C / math.sqrt(er_pe):.3e} m/s. "
        f"Delay = 0.20 / v = {0.20 / (C / math.sqrt(er_pe)) * 1e9:.3f} ns. "
        "That is a cable you can buy, not a mystery.",
    )
    h2(doc, "Worked Example 2.2")
    vg = C / math.sqrt(ER_RF)
    theta = 2 * math.pi * 0.020 / (LAM245 / math.sqrt(ER_RF))
    p(
        doc,
        "A 20 mm microstrip on εr = 3.55 is used at 2.45 GHz. Treating it as TEM with "
        "εeff = εr (a slightly pessimistic bound; real microstrip εeff is lower), find "
        "the electrical length in degrees.",
    )
    p(
        doc,
        f"λg = c/(f √εr) = {LAM245 / math.sqrt(ER_RF) * 1000:.2f} mm. "
        f"θ = 360 × 20 / {LAM245 / math.sqrt(ER_RF) * 1000:.2f} = {math.degrees(theta):.1f}°. "
        "Real microstrip, with some field in air, is a few degrees shorter. The point stands: "
        "this is not a pad, it is a line.",
    )
    practice(
        doc,
        "Chapter 2",
        [
            "Air coax, b/a = 2.30. Find Z0 from (60/√εr) ln(b/a).",
            "How long is 90° on εr = 3.55 at 2.45 GHz, in millimeters?",
            "A 75 Ω system meets a 50 Ω analyzer through an ideal transformer. What turns ratio n = V75/V50 matches power, from n² = 75/50?",
            "Why is microstrip called quasi-TEM instead of TEM?",
        ],
        [
            f"Z0 = 60 ln(2.30) = {60.0 * math.log(2.30):.2f} Ω, essentially 50 Ω.",
            f"λg/4 = {LAM245 / math.sqrt(ER_RF) / 4 * 1000:.2f} mm.",
            f"n = √(75/50) = {math.sqrt(75 / 50):.3f}.",
            "Part of the field is in air, part in the board, so a longitudinal E component exists and εeff is not exactly εr.",
        ],
    )


def ch03(doc):
    h1(doc, "Chapter 3. Loss on a Line")
    p(
        doc,
        "A lossless line is a teaching tool. A real line has conductor loss and dielectric "
        "loss, and at some frequencies radiation and leakage. Conductor loss comes from "
        "skin effect: current crowds into a thin sheet, the sheet resistance rises as √f, "
        "and the series resistance per meter rises with it. Dielectric loss comes from the "
        "imaginary part of ε. Vendors quote it as Df, the dissipation factor, also called "
        "tan δ. Book 9 owns the 10 GHz mill table. This chapter owns what you do with a Df "
        "once you have it.",
    )
    p(
        doc,
        "Attenuation in nepers per meter from dielectric loss, for a TEM or quasi-TEM line, "
        "is αd = (π f √εr tan δ) / c, which is also π tan δ / λg. Convert to decibels per "
        "meter by multiplying by 8.686. Conductor attenuation needs a geometry. For coax it "
        "has a closed form in a and b and the skin resistances. For microstrip it is a "
        "model. The shop fact is that conductor loss usually dominates below a few gigahertz "
        "on a decent hydrocarbon board, and dielectric loss catches up as frequency and Df "
        "rise.",
    )
    h2(doc, "3.1 Skin depth")
    p(
        doc,
        "Skin depth in a good conductor is δ = 1 / √(π f μ σ). For copper at room temperature "
        f"this book's σ is {SIG_CU:.1e} S/m. At 2.45 GHz, δ = "
        f"{1.0 / math.sqrt(math.pi * F245 * MU0 * SIG_CU) * 1e6:.2f} μm. "
        "At 10 GHz it is smaller by √(2.45/10). If your copper is thinner than about two "
        "skin depths, the simple bulk-copper formula is already a little kind. Plating, "
        "roughness, and a nickel barrier under gold can more than double the effective "
        "resistance. Roughness is why two boards with the same Df do not measure the same "
        "loss.",
    )
    h2(doc, "3.2 Dielectric attenuation you can compute")
    p(
        doc,
        "This book uses Df = 0.0027 as a working RO4000-class number at a few gigahertz. "
        "It is not Book 9's 10 GHz row. Plug it in and you get a number you can feel. A "
        "cheap FR-4 Df around 0.020 is seven times worse, which is why this book will not "
        "route a 2.45 GHz matching network on mystery FR-4 and then blame the transistor.",
    )
    h2(doc, "3.3 Why loss is not only heat")
    p(
        doc,
        "Loss on a matching network is insertion loss you will not get back. Loss after a "
        "low-noise amplifier is almost free. Loss before a low-noise amplifier is noise "
        "figure, and the cascade formula for that is Book 6. Loss after a PA is EIRP, and "
        "that one-decibel statement is also Book 6. This chapter only computes the line. "
        "Where you drop that line in a chain decides whether the same 0.3 dB is a shrug "
        "or a program delay.",
    )
    key(
        doc,
        "Dielectric loss scales with f and Df. Conductor loss scales with √f and roughness. "
        "Book 9 quotes the mill. This book spends the decibel.",
    )
    alpha_d_np = (math.pi * F245 * math.sqrt(ER_RF) * DF_RF) / C
    alpha_d_dbm = 8.685889 * alpha_d_np
    delta = 1.0 / math.sqrt(math.pi * F245 * MU0 * SIG_CU)
    h2(doc, "Worked Example 3.1")
    p(
        doc,
        f"Compute dielectric attenuation in dB/m at 2.45 GHz for εr = {ER_RF:.2f} and "
        f"Df = {DF_RF:.4f}. Then give dB per 10 cm.",
    )
    p(
        doc,
        f"αd = π f √εr Df / c = {alpha_d_np:.4f} Np/m = {alpha_d_dbm:.3f} dB/m. "
        f"Over 10 cm that is {alpha_d_dbm * 0.10:.3f} dB. A short matching run is not "
        "where this board spends its life. A 30 cm feeder would.",
    )
    h2(doc, "Worked Example 3.2")
    delta10 = 1.0 / math.sqrt(math.pi * 10e9 * MU0 * SIG_CU)
    p(
        doc,
        "Copper skin depth at 2.45 GHz and at 10 GHz, using σ = 5.8×10^7 S/m. "
        "The 10 GHz figure is a conductor number, not a laminate Df.",
    )
    p(
        doc,
        f"δ(2.45 GHz) = {delta * 1e6:.2f} μm. δ(10 GHz) = {delta10 * 1e6:.2f} μm. "
        f"Ratio √(10/2.45) = {math.sqrt(10e9 / F245):.2f}, and "
        f"{delta * 1e6:.2f} / {delta10 * 1e6:.2f} = {delta / delta10:.2f}. "
        "One-ounce copper is 35 μm. You still have several skin depths at 2.45 GHz. "
        "You have fewer at 77 GHz, and the roughness of the foil then is the circuit.",
    )
    alpha_fr4 = 8.685889 * (math.pi * F245 * math.sqrt(4.5) * 0.020) / C
    practice(
        doc,
        "Chapter 3",
        [
            f"Repeat Example 3.1 with Df = 0.020 and εr = 4.5 at 2.45 GHz. This is a shop FR-4 warning, not Book 9's 10 GHz row.",
            "Skin depth in copper at 77 GHz.",
            "Why does nickel-gold over copper often measure worse than the copper skin-depth formula?",
            "A 0.40 dB feeder sits after a PA. Which book owns the EIRP consequence?",
        ],
        [
            f"{alpha_fr4:.2f} dB/m, about {alpha_fr4 * 0.10:.3f} dB per 10 cm, several times the RO4000-class run.",
            f"{1.0 / math.sqrt(math.pi * 77e9 * MU0 * SIG_CU) * 1e6:.2f} μm.",
            "Nickel is a poor RF conductor; the current sits in the plating. Roughness adds path length.",
            "Book 6. This book computed the feeder. Book 6 spends it as EIRP.",
        ],
    )


def ch04(doc):
    h1(doc, "Chapter 4. Reflection, VSWR, and Return Loss")
    p(
        doc,
        "A wave on a line of impedance Z0 that meets a load ZL launches a reflected wave. "
        "The voltage reflection coefficient is Γ = (ZL − Z0) / (ZL + Z0). If ZL = Z0, Γ = 0 "
        "and the load takes everything the line offered. If ZL is a short, Γ = −1. If ZL is "
        "open, Γ = +1. If ZL is real and larger than Z0, Γ is real and positive. If ZL is "
        "real and smaller, Γ is real and negative. Complex loads put Γ somewhere inside the "
        "unit circle, which is the Smith chart of the next chapter.",
    )
    p(
        doc,
        "The standing-wave ratio is VSWR = (1 + |Γ|) / (1 − |Γ|). Return loss in decibels "
        "is RL = −20 log10 |Γ|. Mismatch loss, the fraction of available power that is not "
        "accepted, is 1 − |Γ|², or −10 log10(1 − |Γ|²) decibels of 'you did not get this.' "
        "A 10 dB return loss is |Γ| = 0.316 and VSWR = 1.93, and you still accepted 90 percent "
        "of the power. A 20 dB return loss is |Γ| = 0.1 and VSWR = 1.22. Instrument people "
        "argue about 20 versus 25. Antenna people are often happy with 10 if the pattern is "
        "right. Power-amplifier people in Book 6 are not happy with 10 at the wrong phase.",
    )
    h2(doc, "4.1 Why phase matters")
    p(
        doc,
        "A length of line rotates Γ. Moving away from the load toward the generator, on a "
        "lossless line, Γ(d) = ΓL exp(−j 2 β d). The factor of two is the round trip. A "
        "half-wave of line brings Γ right back where it started. A quarter-wave of line "
        "sends a low resistance toward a high one, which is the next matching chapter. "
        "You cannot read a load from a VSWR number alone. VSWR is |Γ|. The match you need "
        "is Γ, with an angle.",
    )
    h2(doc, "4.2 The generator has a Γ too")
    p(
        doc,
        "If the source is not Z0, a wave that reflects off the load reflects again off the "
        "source, and you have a series. In a Z0 system with a well-leveled generator and a "
        "pad, you may ignore that. In a transistor output, you may not. Small-signal "
        "stability in Chapter 14 is exactly this conversation with S-parameters. High-power "
        "pull in Book 6 is this conversation with a load-pull tuner.",
    )
    h2(doc, "4.3 Time domain is the same Γ")
    p(
        doc,
        "A TDR launches a step and watches the bounce. An open rises. A short falls. A "
        "capacitive bump is a dip that recovers. An inductive bump is a peak that recovers. "
        "The size of the step, relative to the launched step, is Γ at that discontinuity "
        "for the frequencies in the step. Lyons would tell you the step's spectrum. This "
        "chapter only needs that the number you read on the TDR is the same Γ the VNA "
        "quotes at a swept frequency, after you have calibrated.",
    )
    key(
        doc,
        "VSWR is the magnitude. The match is the complex Γ. A quarter-wave of line is a "
        "rotation of 180° on the Γ plane.",
    )
    g75 = (75 - 50) / (75 + 50)
    vswr75 = (1 + abs(g75)) / (1 - abs(g75))
    rl75 = -db20(abs(g75))
    ml75 = -db10(1 - g75 ** 2)
    h2(doc, "Worked Example 4.1")
    p(
        doc,
        "A 75 Ω resistor terminates a 50 Ω line. Find Γ, VSWR, return loss, and mismatch loss.",
    )
    p(
        doc,
        f"Γ = (75−50)/(75+50) = {g75:.3f}. VSWR = {vswr75:.3f}. "
        f"RL = {rl75:.2f} dB. Mismatch loss = {ml75:.3f} dB, which is "
        f"{(1 - g75 ** 2) * 100:.1f} percent of available power accepted. "
        "A 75-to-50 pad or a transformer is how you stop arguing with this number.",
    )
    g25 = (25 - 50) / (25 + 50)
    h2(doc, "Worked Example 4.2")
    p(
        doc,
        "A 25 Ω resistor terminates the same 50 Ω line. Find Γ and compare |Γ| with Example 4.1.",
    )
    p(
        doc,
        f"Γ = (25−50)/(25+50) = {g25:.3f}. |Γ| = {abs(g25):.3f}, identical to the 75 Ω case. "
        "VSWR and return loss are therefore the same. The angle of Γ is 180° instead of 0°. "
        "A quarter-wave transformer that matches 25 Ω to 50 Ω is Chapter 8. Its Zq is the "
        f"locked {ZQ:.2f} Ω.",
    )
    g10 = (100 - 50) / (100 + 50)
    practice(
        doc,
        "Chapter 4",
        [
            "ZL = 100 Ω on 50 Ω. Γ, VSWR, RL.",
            "What load on 50 Ω gives VSWR = 2 with Γ real and positive?",
            "A lossless 90° line sits in front of a short. What impedance do you see at the input?",
            "Return loss is 6 dB. What fraction of available power is accepted?",
        ],
        [
            f"Γ = {g10:.3f}, VSWR = {(1 + g10) / (1 - g10):.3f}, RL = {-db20(g10):.2f} dB.",
            "VSWR = 2 ⇒ |Γ| = 1/3. Real positive ⇒ ZL = Z0 (1+|Γ|)/(1−|Γ|) = 100 Ω.",
            "A short through 90° is an open. Zin = ∞ in the lossless ideal.",
            f"|Γ| = 10^(−6/20) = {10 ** (-6 / 20):.3f}. Accepted = 1−|Γ|² = {1 - 10 ** (-0.6):.3f} ({(1 - 10 ** (-0.6)) * 100:.1f} percent).",
        ],
    )


def ch05(doc):
    h1(doc, "Chapter 5. The Smith Chart at Work")
    p(
        doc,
        "Book 1 taught the Smith chart as a map of complex Γ. This chapter uses it as a "
        "shop tool. Normalized impedance z = Z / Z0 = r + j x. The chart's circles of "
        "constant r and arcs of constant x are the image of the right-half Z plane under "
        "Γ = (z − 1) / (z + 1). The outside of the chart is |Γ| = 1, the rim of lossless "
        "reactances. The center is Z0. The right tip is an open. The left tip is a short.",
    )
    p(
        doc,
        "Admittance y = 1/z lives on the same paper after a 180° rotation. A Smith chart "
        "with both families printed is an impedance-admittance chart. Open-stub matching "
        "is easier on the admittance family because a shunt stub adds susceptance. Series "
        "transmission-line matching is easier on the impedance family because a series line "
        "walks you along a constant-|\Γ| circle.",
    )
    h2(doc, "5.1 Walks you actually take")
    p(
        doc,
        "Toward the generator on a lossless Z0 line, you walk clockwise on a constant-|\Γ| "
        "circle. A full lap is λ/2. A quarter lap is λ/8. A half lap is λ/4 and swaps z "
        "with 1/z. Adding a series inductor walks you up a constant-r circle. Adding a "
        "series capacitor walks you down. Adding a shunt capacitor walks you along a "
        "constant-g circle toward more positive susceptance. Adding a shunt inductor walks "
        "the other way. That is the entire L-section vocabulary of the next chapter, drawn.",
    )
    h2(doc, "5.2 What the chart will not do for you")
    p(
        doc,
        "The chart does not know about loss unless you draw a spiral. It does not know "
        "about power. It does not know about Book 6's load-pull contours. It will happily "
        "show you a conjugate match that would melt a device. It is a map of impedances, "
        "not a permit. Used that way, it is the fastest hand tool in microwave work. "
        "Used as a substitute for a large-signal model, it is how people burn parts.",
    )
    h2(doc, "5.3 Calibration is part of the chart")
    p(
        doc,
        "A VNA plot is a Smith chart only at the plane you calibrated. A fixture, a probe, "
        "or 12 mm of 50 Ω after the cal kit, and you are reading a rotated Γ. Port extension "
        "and TRL exist because the chart is honest and the connectors are not. This is not "
        "a software chapter. It is a reminder that the point you plot is only as good as "
        "the plane you named.",
    )
    key(
        doc,
        "The chart is Γ-paper. Clockwise toward the generator. A quarter-wave is a half-turn "
        "and swaps z with 1/z.",
    )
    z_l = 25 / 50
    g = (z_l - 1) / (z_l + 1)
    h2(doc, "Worked Example 5.1")
    p(
        doc,
        "Normalize 25 Ω to 50 Ω and compute Γ. Where does this point sit on the chart? "
        "After a lossless 90° line, what impedance do you see?",
    )
    p(
        doc,
        f"z = 25/50 = {z_l:.2f}. Γ = (0.50−1)/(0.50+1) = {g:.3f}, real, left of center. "
        "A 90° line sends z to 1/z = 2.00, which is 100 Ω. That is the quarter-wave "
        "transformer idea, drawn. Zq of a 25-to-50 match is not this 90° of 50 Ω line. "
        f"Zq is {ZQ:.2f} Ω, Chapter 8.",
    )
    zc = 50 + 1j * 2 * math.pi * F245 * 2e-9
    gc = (zc / 50 - 1) / (zc / 50 + 1)
    h2(doc, "Worked Example 5.2")
    p(
        doc,
        "A 50 Ω resistor in series with 2.0 nH is the load at 2.45 GHz on a 50 Ω line. "
        "Find z and Γ.",
    )
    p(
        doc,
        f"XL = 2π f L = {2 * math.pi * F245 * 2e-9:.2f} Ω. ZL = 50 + j{2 * math.pi * F245 * 2e-9:.2f} Ω. "
        f"z = 1 + j{(2 * math.pi * F245 * 2e-9) / 50:.3f}. "
        f"Γ = {gc.real:.3f} + j{gc.imag:.3f}, |Γ| = {abs(gc):.3f}. "
        "On the chart you sit on the r = 1 circle, above the real axis, not far from the center. "
        "A small series C would walk you back to the center.",
    )
    practice(
        doc,
        "Chapter 5",
        [
            "A shorted 50 Ω stub is 45° long. What normalized impedance is at its input?",
            "An open 50 Ω stub is 45° long. What normalized admittance is at its input?",
            "You measure Γ = 0.4 at 30°. What is z?",
            "Why does a half-wave of 50 Ω line disappear on the chart?",
        ],
        [
            "A short through 45° is j tan(45°) = j1.00, so z = j1. An inductor of 50 Ω reactance.",
            "An open through 45° is y = j tan(45°) = j1. A capacitor of 50 Ω susceptance.",
            f"z = (1+Γ)/(1−Γ). Γ = 0.4∠30° = {0.4 * math.cos(math.radians(30)):.3f}+j{0.4 * math.sin(math.radians(30)):.3f}. z = (1+Γ)/(1−Γ) ≈ 1.69 + j0.94.",
            "A 180° walk on the Γ plane is a full lap. You return to the same point. Zin = ZL for a lossless half-wave.",
        ],
    )
