# -*- coding: utf-8 -*-
"""Build Book 7, EMC, Simulation, and Test.

The four chapter titles from the stub stay. The prose around them is this
book's teaching text. Worked numbers are computed below and printed into
the manuscript. Do not paste Ott, Montrose, or Bogatin.

Running grow_4_9.py must not overwrite this file. That script skips Book 7.
"""

import math
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "EMC_Simulation_and_Test_Book7.docx"
STUB_TEMPLATE = OUT  # styles, theme, and section come from the file we replace

C = 299792458.0
MU0 = 4.0 * math.pi * 1e-7
ETA = MU0 * C  # free-space impedance, ohms
NEPER_DB = 20.0 * math.log10(math.e)  # 8.685889 dB per neper of field


def e_loop(f_hz, i_a, area_m2, r_m):
    """Far-field electric field of a small loop, sin(theta)=1, volts/meter.

    E = mu0 * omega^2 * I * A / (4 * pi * c * r).
    """
    omega = 2.0 * math.pi * f_hz
    return (MU0 * omega * omega * i_a * area_m2) / (4.0 * math.pi * C * r_m)


def e_short_dipole(f_hz, i_a, length_m, r_m):
    """Far-field electric field of a Hertzian dipole, sin(theta)=1, V/m.

    E = eta * k * I * L / (4 * pi * r), with k = omega/c.
    Valid only while the wire is short beside a wavelength.
    """
    k = 2.0 * math.pi * f_hz / C
    return (ETA * k * i_a * length_m) / (4.0 * math.pi * r_m)


def dbuv_per_m(e_v_m):
    return 20.0 * math.log10(e_v_m * 1.0e6)


def uv_from_dbuv(db):
    return 10.0 ** (db / 20.0)


def skin_mm(f_hz):
    """Copper skin depth in millimeters. Same 66/sqrt(f) hand rule as Book 8."""
    return 66.0 / math.sqrt(f_hz)


def loop_inductance_h(radius_m, wire_radius_m):
    """External inductance of a round loop. Internal inductance omitted."""
    return MU0 * radius_m * (math.log(8.0 * radius_m / wire_radius_m) - 2.0)


# --- declared teaching numbers -------------------------------------------------
F_CLK = 25.0e6
F_HARM = 100.0e6
F_THIRD = 75.0e6
RATIO_F = F_HARM / F_CLK  # 4
RATIO_E = RATIO_F ** 2  # 16
DB_16 = 20.0 * math.log10(RATIO_E)
THIRD_F_RATIO = F_THIRD / F_CLK  # 3
THIRD_E_IF_I_FIXED = THIRD_F_RATIO ** 2  # 9
THIRD_I_FACTOR = 1.0 / 3.0  # ideal square, 1/n
THIRD_E_NET = THIRD_E_IF_I_FIXED * THIRD_I_FACTOR  # 3
DB_THIRD = 20.0 * math.log10(THIRD_E_NET)

R_MEAS = 3.0  # m, Class B distance in this book's FCC snapshot
LOOP_SIDE = 0.02  # m
LOOP_AREA = LOOP_SIDE * LOOP_SIDE
E_LIMIT_100 = 150.0e-6  # V/m, FCC 15.109 Class B, 88-216 MHz, 3 m
I_LOOP_FOR_LIMIT = E_LIMIT_100 * R_MEAS / e_loop(F_HARM, 1.0, LOOP_AREA, R_MEAS)

WIRE_L = 0.10  # m, short beside lambda at 100 MHz
I_WIRE_FOR_LIMIT = E_LIMIT_100 * (4.0 * math.pi * R_MEAS) / (
    ETA * (2.0 * math.pi * F_HARM / C) * WIRE_L
)
# equivalent: I = E / (the per-amp field)
E_PER_AMP_WIRE = e_short_dipole(F_HARM, 1.0, WIRE_L, R_MEAS)
I_WIRE_CHECK = E_LIMIT_100 / E_PER_AMP_WIRE

LAM_100 = C / F_HARM
LAM_25 = C / F_CLK
FAR_BOUNDARY_100 = LAM_100 / (2.0 * math.pi)

# Class A comparison. 90 uV/m at 10 m, extrapolated as 1/r.
CLASS_A_10M_UV = 90.0
CLASS_A_AT_3M_UV = CLASS_A_10M_UV * (10.0 / 3.0)
DB_10_TO_3 = 20.0 * math.log10(10.0 / 3.0)
CLASS_B_LOW_UV = 100.0
TIGHTER_DB = dbuv_per_m(CLASS_A_AT_3M_UV * 1e-6) - dbuv_per_m(CLASS_B_LOW_UV * 1e-6)

# 1 oz copper, this book's hand thickness
COPPER_OZ_MM = 0.0348
SKIN_100_MM = skin_mm(F_HARM)
ABSORB_100_DB = NEPER_DB * (COPPER_OZ_MM / SKIN_100_MM)

# 2 dB failure
FIELD_RATIO_2DB = 10.0 ** (2.0 / 20.0)

# LISN example: 60 dBuV across 50 ohm
LISN_OHM = 50.0
DBUV_60 = 60.0
UV_60 = uv_from_dbuv(DBUV_60)
UA_60 = UV_60 / LISN_OHM

# round loop of the same area as the 2 cm square, for the inductance example
LOOP_R = math.sqrt(LOOP_AREA / math.pi)
WIRE_A = 0.5e-3  # m
L_LOOP = loop_inductance_h(LOOP_R, WIRE_A)
XL_100 = 2.0 * math.pi * F_HARM * L_LOOP
XL_50 = XL_100 / 2.0

# choke example, declared impedances, not a universal cable model
Z_BEFORE = 20.0  # ohm
Z_CHOKE = 200.0  # ohm at 100 MHz, this example
V_CM = 0.010  # V, declared noise voltage
I_BEFORE = V_CM / Z_BEFORE
I_AFTER = V_CM / (Z_BEFORE + Z_CHOKE)
I_RATIO_CHOKE = I_BEFORE / I_AFTER

# sanity
assert abs(RATIO_E - 16.0) < 1e-9
assert abs(I_WIRE_FOR_LIMIT - I_WIRE_CHECK) / I_WIRE_CHECK < 1e-9
# 1 A on a 1 m short dipole at 3 m is tens of volts per meter, not a product current.
_e_one_amp = e_short_dipole(F_HARM, 1.0, 1.0, R_MEAS)
assert 10.0 < _e_one_amp < 40.0


def f2(x):
    return f"{x:.2f}"


def f1(x):
    return f"{x:.1f}"


def f0(x):
    return f"{x:.0f}"


def sci_ua(i_a):
    return f"{i_a * 1e6:.2f}"


N = {
    "ratio_e": f0(RATIO_E),
    "db16": f1(DB_16),
    "third_net": f0(THIRD_E_NET),
    "db_third": f1(DB_THIRD),
    "i_loop_ma": f1(I_LOOP_FOR_LIMIT * 1e3),
    "i_wire_ua": sci_ua(I_WIRE_FOR_LIMIT),
    "lam100": f2(LAM_100),
    "lam25": f2(LAM_25),
    "far100": f2(FAR_BOUNDARY_100),
    "db_dist": f1(DB_10_TO_3),
    "class_a_3m": f0(CLASS_A_AT_3M_UV),
    "tighter": f1(TIGHTER_DB),
    "skin_um": f1(SKIN_100_MM * 1000.0),
    "absorb": f0(ABSORB_100_DB),
    "field2": f2(FIELD_RATIO_2DB),
    "ua60": f0(UA_60),
    "l_nh": f1(L_LOOP * 1e9),
    "xl": f1(XL_100),
    "xl_half": f1(XL_50),
    "loop_r_mm": f2(LOOP_R * 1e3),
    "i_before_ua": f0(I_BEFORE * 1e6),
    "i_after_ua": f1(I_AFTER * 1e6),
    "choke_ratio": f1(I_RATIO_CHOKE),
    "eta": f1(ETA),
    "e_const": f"{e_loop(1.0, 1.0, 1.0, 1.0):.3e}",
}


def blocks():
    """Return (kind, text) rows. kind is title, center, italic, h1, h2, body."""
    b = []

    def add(kind, text):
        b.append((kind, text.format(**N)))

    add("title", "EMC, Simulation, and Test")
    add("center", "Book 7 of 9")
    add("center", "Lothar J. Musiol")
    add(
        "italic",
        "Copyright © 2026 Lothar J. Musiol. Nine-book series. Worked numbers are computed in the builder. "
        "Book 2 is a separate manuscript. Do not paste Ott, Montrose, Bogatin, Cripps, Pozar, or Sklar. "
        "American spelling. Original prose.",
    )
    add(
        "italic",
        "Book 7 of 9. Old books 11, 19, and 20 of the retired split. One volume for the physics, the solver, and the certificate.",
    )

    add("h1", "How to Use This Book")
    add(
        "body",
        "A product fails electromagnetic compatibility in one of two ways. It sends out more than the limit allows, or it falls over when the world sends something in. This book is those two failures, the room where they are measured, and the solvers you run before you rent the room. It is not a second book on antennas, and it is not a power-supply book.",
    )
    add(
        "body",
        "Read it with a calculator. Every worked number comes from a constant declared in the next section, and the same constant is used again later. If a vendor datasheet quotes a different skin depth or a different limit table, use the datasheet for that part and keep these constants for the teaching problems. A certificate is written against the edition of the standard named in the test plan. The tables here are this book's snapshot so the arithmetic can be checked. They are not a substitute for that edition.",
    )
    add(
        "body",
        "Four ideas from the short draft are kept on purpose, and the rest of the book is there to make them earn their keep. A small loop's far field scales with area, current, and frequency squared. Sixteen is the scaling from 25 MHz to 100 MHz if the current matched, and it is not a prediction. Common-mode current on a cable is usually what fails, not the clock trace. The people who run the chamber measure. They do not design the board.",
    )

    add("h1", "Declared Constants")
    add(
        "body",
        "Free-space impedance is η = μ0 c = {eta} Ω. The speed used for a wavelength is c = 2.99792458×10^8 m/s. Copper skin depth is the hand rule δ = 66/√f millimeters with f in hertz, the same rule Book 8 uses for its magnetics shelves. This book borrows it only for a shield wall. One ounce of copper is taken as 0.0348 mm. One neper of field is 8.686 dB. Absorption through a wall, in decibels, is 8.686 times the thickness divided by δ.",
    )
    add(
        "body",
        "The small-loop far field, with sin θ = 1, is E = μ0 ω² I A / (4 π c r). At one ampere, one square meter, one meter, and one hertz, that expression is {e_const} V/m, which is the constant 1.317×10^−14 when it is written as E = (constant) f² I A / r. The short-dipole far field is E = η k I L / (4 π r), and it is used only while the wire is short beside a wavelength. Neither formula is a chamber prediction. Both are the models the worked examples are allowed to use.",
    )
    add(
        "body",
        "Distances and limits that the examples freeze: the Class B measuring distance in the FCC snapshot is 3 m. The Class B field limit used at 100 MHz is 150 μV/m, which is the 88–216 MHz row. The teaching loop is a square 2 cm on a side. The teaching wire for the dipole formula is 10 cm long, short beside the 3.0 m wavelength at 100 MHz. A 1 m cable is discussed in words and is not pushed through the short-dipole formula.",
    )

    add("h1", "Where This Book Stops")
    add(
        "body",
        "Book 1 owns the circuit laws, the field pictures, and the fact that a square wave's odd harmonics fall as 1/n. Book 2 owns op-amps, filters as circuits, and the inductor as a catalog part. Book 4 owns antenna gain, beam, and the Friis factor. Book 6 owns transmitter watts, feed loss, EIRP, and the radio's own mask. Book 8 owns the rack, the buck converter, and the four magnetics shelves. Book 9 owns layout habits, laminate loss, and the package. When this book names one of those, it is pointing, not re-deriving.",
    )
    add(
        "body",
        "What stays here is the unintentional antenna, the method that measures it, the limit that judges it, the immunity test that hits it, and the solver you pick before you book a day. A passing radio conformance report does not close an EMC file. A passing EMC file does not close a radio mask. The two reports are Chapter 12.",
    )

    # ----- Chapter 1 -----
    add("h1", "Chapter 1. Why a Board Radiates")
    add(
        "body",
        "A board can be quiet on the bench and loud in the chamber. The bench has a short ground clip and no cable long enough to matter. The chamber has a mains cord, a turntable, and a limit written in microvolts per meter. The silicon did not change on the drive over. The antenna did. You built it when a loop of current closed on the board, or when a wire left the box carrying current that did not come back on a neighbor.",
    )
    add("h2", "1.1 Two antennas that are not on the schematic")
    add(
        "body",
        "A small loop of current is a magnetic dipole. The go and the return sit next to each other, the area between them is the area that counts, and the far electric field of that loop grows with frequency squared if you hold the current fixed. A wire that leaves the box, with the return somewhere in the room rather than on a paired conductor, is an electric dipole. The first case is what people mean by differential mode. The second is common mode. Both radiate. They do not radiate on the same budget of amperes, which is why a tidy clock trace can be innocent and a USB cable can be the whole failure.",
    )
    add("h2", "1.2 Sixteen, if the current matched")
    add(
        "body",
        "Take a 25 MHz clock and a spectral line at 100 MHz. The frequency ratio is 4. For a small loop in the far field, the electric-field ratio is the square of that, which is 16, provided the current at 100 MHz equals the current at 25 MHz and the area has not changed. In decibels of field, 20 log10(16) is {db16} dB. Sixteen is the scaling if the current matched. It is not a prediction of the marker on the analyzer.",
    )
    add(
        "body",
        "A symmetric square wave has odd harmonics. The fourth harmonic of 25 MHz is 100 MHz, and a perfect 50 percent square has no even harmonic to give you. The current at 100 MHz is then whatever asymmetry, ringing, or rise time left behind. It can be almost nothing. The line a square wave actually owes is the third harmonic, at 75 MHz. The frequency ratio is 3, so frequency alone would multiply the field by 9. The harmonic current of an ideal square falls as 1/n, and n is 3, so the current is about one third of the fundamental. Nine times one third is 3. The field at that harmonic is about three times the fundamental's field, which is {db_third} dB, and only inside this ideal picture. Book 1 already derived the 1/n fall. This chapter only multiplies it by the f² of the loop.",
    )
    add(
        "body",
        "Key idea. Common-mode current on a cable usually fails the limit, not the clock trace. The factor of 16 is a scaling under a stated condition. It is not a forecast.",
    )
    add("h2", "Worked Example 1.1")
    add(
        "body",
        "A designer reads a 25 MHz clock and expects the 100 MHz line to be 16 times louder. Write the condition that would make that true, and the condition a square wave actually meets.",
    )
    add(
        "body",
        "The factor 16 holds when the current at 100 MHz equals the current at 25 MHz and the radiator is still a small loop in the far field. A symmetric square does not meet the current condition at the fourth harmonic. At the third harmonic the ideal scaling is {third_net}, not 16. If the measured 100 MHz line really is 16 times the fundamental, the current did not fall, and the cause is not the square-wave series. Look for ringing, a duty cycle that is not one half, or a different radiator.",
    )
    add("h2", "Practice")
    add("body", "1. A 10 MHz clock has a line at 30 MHz with the same loop current. What is the field ratio from frequency alone, and what is it if the line is an ideal third harmonic whose current fell as 1/n?")
    add("body", "2. Why is \"the fourth harmonic will be 24 dB up\" a bad sentence to put in a test report?")
    add("body", "3. Name the two unintentional antennas this chapter allows, in one sentence each.")

    # ----- Chapter 2 -----
    add("h1", "Chapter 2. The Small Loop")
    add(
        "body",
        "The clock trace is not innocent because it is digital. It is often innocent because its area is small and its return is close. This chapter writes the far-field expression, uses it once on the teaching loop, and then says where the expression stops being allowed.",
    )
    add("h2", "2.1 The expression")
    add(
        "body",
        "A loop small beside a wavelength, carrying a current I, has a magnetic moment I times A. Far away, on the axis of strongest radiation, the electric field is E = μ0 ω² I A / (4 π c r). Frequency enters twice: once because the moment's radiation grows with k², and k is ω/c, and once you have already squared it. Area and current enter once each. Distance enters as 1/r, which is the far-field fall, not the 1/r³ fall of the near magnetic field. If you are still in the near field, this expression is the wrong tool, and a bigger number from it is not a bigger failure.",
    )
    add(
        "body",
        "At 100 MHz the wavelength is {lam100} m. A rough boundary between near and far is λ/2π, which is {far100} m. A 3 m measurement is several of those boundaries, so the far-field picture is the one this book uses at 100 MHz. At 25 MHz the wavelength is {lam25} m and the same boundary is four times farther. A 3 m site at 30 MHz is not deep in the far field. The standard still measures there. The formula is a teaching model, not the site's correction factor.",
    )
    add("h2", "2.2 The teaching loop")
    add(
        "body",
        "The loop in every example that does not say otherwise is a square 2 cm on a side. Its area is 4×10^−4 m². That is a small decoupling loop or a tight clock loop, not a board outline. Ask how much current at 100 MHz produces the 150 μV/m Class B row at 3 m, using the far-field expression and nothing else.",
    )
    add(
        "body",
        "Key idea. Keep high di/dt loops small. Area is the one factor a layout can change after the clock frequency has already been chosen.",
    )
    add("h2", "Worked Example 2.1")
    add(
        "body",
        "Find the 100 MHz current in the 2 cm loop that produces 150 μV/m at 3 m.",
    )
    add(
        "body",
        "E scales with I, so I = E × r / (the field of one ampere at that r). The result is {i_loop_ma} mA. Tens of milliamperes in a tight loop, not microamperes. A logic edge can source that much into a bad return. A tight return makes the area smaller than 4 cm² and the same current falls short of the limit. The number is the model's number. A real board has more than one loop, a ground plane, and a cable, and the cable is the next chapter.",
    )
    add("h2", "Practice")
    add("body", "1. The same loop at the same current, at 50 MHz instead of 100 MHz. By what factor does the far field drop?")
    add("body", "2. You cut the side from 2 cm to 1 cm and keep the current. By what factor does the area, and therefore the field, drop?")
    add("body", "3. Why is a near-field probe reading on the bench not the 3 m limit?")

    # ----- Chapter 3 -----
    add("h1", "Chapter 3. The Cable You Did Not Call an Antenna")
    add(
        "body",
        "A cable becomes an antenna when the current on it is common mode: the same direction on the signal and on its return, or on the shield, with the true return somewhere else. The loop in Chapter 2 needed tens of milliamperes. A wire needs far less, which is the whole reason chambers are full of ferrite placed on cables at the last hour.",
    )
    add("h2", "3.1 A short wire, on purpose")
    add(
        "body",
        "The short-dipole field is E = η k I L / (4 π r). It assumes the wire is short beside a wavelength, so the current is about the same all along it. At 100 MHz, λ is {lam100} m. A 10 cm wire is short enough for the assumption to be a teaching assumption. A 1 m mains cord is about a third of a wavelength and is a better antenna than this formula describes. Using the short formula on a long cord would understate the radiation. This book refuses that shortcut. The 10 cm wire is the calculated case. The long cord is the warning beside it.",
    )
    add("h2", "3.2 Microamperes, not milliamperes")
    add(
        "body",
        "Set E to 150 μV/m, r to 3 m, L to 10 cm, f to 100 MHz. The current that meets the Class B row in this model is {i_wire_ua} μA. The 2 cm loop needed {i_loop_ma} mA for the same field. The wire is worse by about three orders of magnitude of current, and it is only 10 cm long. A meter of cable, no longer inside the short-dipole assumption, is not going to need more current than that. It will need less. That is what the draft meant by saying the cable usually fails, not the clock trace.",
    )
    add(
        "body",
        "Key idea. Hunt common mode before you hunt the clock. The clock matters when its return spreads out and drives that common mode.",
    )
    add("h2", "Worked Example 3.1")
    add(
        "body",
        "A 10 cm pigtail past a connector carries 20 μA at 100 MHz. Is it over the 150 μV/m row in the short-dipole model at 3 m?",
    )
    add(
        "body",
        "The limit current was {i_wire_ua} μA. Twenty microamperes is below that. The same 20 μA on a 1 m cord is not this example, and it is not cleared by this paragraph. Measure it, or model it as a longer antenna in a solver from Part III. Do not multiply the short-dipole answer by ten and call the cord innocent or guilty.",
    )
    add("h2", "Practice")
    add("body", "1. The teaching wire is doubled to 20 cm, still short at 100 MHz, same current. What happens to E?")
    add("body", "2. Why does this book not quote a single microampere number for a 1 m mains cord?")
    add("body", "3. A ferrite on a cable reduces common-mode current. Which factor in the short-dipole expression did it change?")

    # ----- Chapter 4 -----
    add("h1", "Chapter 4. Return Current and the Slot")
    add(
        "body",
        "Return current takes the lowest impedance path, not the shortest geometric path you hoped for, and not the ground symbol. At low frequency that path is the least resistance. At high frequency it is the least inductance, which for a trace over a plane is the route directly under the trace. Break that plane and the return detours. The detour is a loop. The loop is Chapter 2.",
    )
    add("h2", "4.1 Do not slot the ground under a return")
    add(
        "body",
        "A slot under a trace forces the return out to the end of the slot and back. The area is about the length of the trace times the extra width of the detour. That area, times the signal current, is the moment you just built. A split between analog and digital ground, cut all the way across the board and crossed by a clock, is this mistake with a philosophy attached. If the two regions must be split, cross the split at one point, with the signal and its return in the same place. Book 9 owns the habit of a continuous reference under a fast trace. This chapter owns the radiation that appears when the habit is skipped.",
    )
    add("h2", "4.2 A plane is not a zero-volt spell")
    add(
        "body",
        "A ground plane has inductance. A current in it has a voltage along it. Two circuits that share a neck of plane share that voltage, and the victim circuit can drive a cable with it. That is one ordinary way a quiet loop becomes common mode on a connector. The fix is geometry: separate the necks, or give the victim its own return at the connector, or filter the connector. It is not a thicker paragraph in the schematic that says \"star ground\" without drawing the star.",
    )
    add(
        "body",
        "Key idea. The return is part of the antenna. Slotting it open is a layout change that the chamber will measure.",
    )
    add("h2", "Worked Example 4.1")
    add(
        "body",
        "A trace 5 cm long crosses a slot, and the return must travel 2 cm extra out and 2 cm back. Estimate the extra loop area and compare it with the 2 cm square of Chapter 2.",
    )
    add(
        "body",
        "A rough rectangle 5 cm by 2 cm has area 1 cm². The teaching square has area 4 cm². The slot loop is smaller than the teaching square, not free. If the current in the trace is larger than the {i_loop_ma} mA of Worked Example 2.1, even this smaller area can meet the same field. The estimate ignores the frequency and the plane's real current spread. It is enough to stop a layout review from calling the slot \"just a ground cut.\"",
    )
    add("h2", "Practice")
    add("body", "1. At 1 kHz, does return current hug the trace or spread through the copper? Which impedance won?")
    add("body", "2. Why is a single-point connection between two ground regions different from a slot crossed in three places?")
    add("body", "3. A cable fails only when a certain chip's bus is active. Where do you look first, the bus amplitude or the path from that bus to the connector?")

    # ----- Chapter 5 -----
    add("h1", "Chapter 5. A Shield Is a Box")
    add(
        "body",
        "A shield works when it is a closed conducting box, the seam is continuous at the frequency you care about, and the cables that leave it are dealt with at the wall. A painted plastic lid, a gasket that does not touch, and a slot the length of a screwdriver are not a box. They are a new antenna with a metal costume.",
    )
    add("h2", "5.1 Skin depth is not the usual problem")
    add(
        "body",
        "Copper skin depth at 100 MHz, by this book's rule, is {skin_um} μm. One ounce of copper is 0.0348 mm, which is several skin depths. Field transmission through a thickness of that many skin depths is about {absorb} dB of absorption, before you even count the reflection at the surface. Solid copper foil is already a fine wall at 100 MHz. If a product fails by a few decibels, the wave is not coming through the copper. It is coming through a hole, a seam, or a wire.",
    )
    add(
        "body",
        "Book 8 owns skin depth as a magnetics fact: line-frequency steel, switch-mode ferrite, and the rest of those shelves. The number here is the same copper rule, used once, so this book does not invent a second formula.",
    )
    add("h2", "5.2 A slot is an antenna")
    add(
        "body",
        "A slot in a shield radiates as a dipole of about the slot's length, driven by the voltage across the slot. A slot near a half-wavelength is an efficient radiator. At 100 MHz, half of {lam100} m is about 1.5 m, so a small seam is a poor antenna at that frequency and a better one at a higher harmonic. The practical rule is still to close the seam, because the product does not get to choose which harmonic the chamber will find. A gasket, a finger stock, or a screw pitch that is a small fraction of the wavelength keeps the slot from being one long opening. Spacing screws a hand's width apart and calling it shielded is a hope.",
    )
    add(
        "body",
        "Key idea. Spend the shield budget on the seams and the cable entries. The foil is already thick enough.",
    )
    add("h2", "Worked Example 5.1")
    add(
        "body",
        "Someone proposes a thicker wall, two ounces instead of one, to fix a 6 dB failure at 100 MHz. What does the absorption number say?",
    )
    add(
        "body",
        "One ounce already sits near {absorb} dB of absorption in this estimate. Doubling the thickness adds skin depths; it does not close a seam. A 6 dB failure is a factor of two in field. That is a hole, a cable, or a loop, and Chapter 19 is the size of a small failure. Change the copper weight when the wall is actually thin at the frequency, which at 100 MHz it is not.",
    )
    add("h2", "Practice")
    add("body", "1. Compute the copper skin depth at 10 MHz with δ = 66/√f millimeters. Is one ounce still many skin depths?")
    add("body", "2. A display aperture is 15 cm across. Why might it matter more at 1 GHz than at 100 MHz, without doing a full slot calculation?")
    add("body", "3. A shield cable enters a box and the shield is tied 5 cm inside. What did those 5 cm become?")

    # ----- Chapter 6 -----
    add("h1", "Chapter 6. The Filter Lives at the Boundary")
    add(
        "body",
        "A filter stops a current from reaching an antenna, or stops an incoming current from reaching a victim. It has to sit where that choice is still available. Midway along a trace, with the cable already past it, it is a circuit in Book 2's sense and not a fix in this book's sense.",
    )
    add("h2", "6.1 Differential mode and common mode want different parts")
    add(
        "body",
        "A capacitor from a signal to its return, at the connector, shunts differential noise. It does very little to a current that is in the same direction on both wires. A common-mode choke, two windings on one core, presents inductance to that shared current and almost none to equal-and-opposite signal current. A capacitor from each line to the chassis, at the wall, is the shunt for what the choke did not stop. The order is choke then shunt as you leave the box, so the noise source sees a high series impedance and then a low path that is not the cable.",
    )
    add(
        "body",
        "Book 2 designs the filter as a transfer function, with poles and a passband. This chapter only insists on the location and on which current each part is allowed to touch. A perfect Butterworth response on the wrong current is a passing simulation and a failing cable.",
    )
    add("h2", "6.2 A declared choke, not a universal cable")
    add(
        "body",
        "There is no single impedance for \"a cable\" that this book will pretend is a law. For one example, declare a noise voltage of 10 mV at 100 MHz, a path of 20 Ω before the choke, and a choke of 200 Ω at that frequency. The current is V/Z.",
    )
    add(
        "body",
        "Key idea. Filter the current that reaches the antenna. Put the parts at the boundary, and name whether they see differential mode or common mode.",
    )
    add("h2", "Worked Example 6.1")
    add(
        "body",
        "Compute the common-mode current before and after the declared choke.",
    )
    add(
        "body",
        "Before: 10 mV / 20 Ω = {i_before_ua} μA. After: 10 mV / 220 Ω = {i_after_ua} μA. The current falls by a factor of {choke_ratio}. Chapter 3's short wire met the 150 μV/m row near {i_wire_ua} μA. This example's \"after\" current is under that, and the \"before\" current is over it. The choke mattered. Change the declared 20 Ω and the factor changes. Do not carry {choke_ratio} into a different product as a measured result.",
    )
    add("h2", "Practice")
    add("body", "1. A capacitor across a differential pair does not change the common-mode current. Why?")
    add("body", "2. You move the same choke from the connector to the middle of a 20 cm internal trace, and the cable is still past the connector. What antenna did you leave unfiltered?")
    add("body", "3. Why does this book refuse to quote one radiation resistance for every mains cord?")

    # ----- Chapter 7 -----
    add("h1", "Chapter 7. The Room With a Metal Floor")
    add(
        "body",
        "Radiated emission for an ordinary product is measured in a semi-anechoic chamber. The walls and the ceiling are lined with absorber. The floor is metal on purpose. The floor is part of the method, not a leftover of the building.",
    )
    add("h2", "7.1 What the method actually does")
    add(
        "body",
        "The product sits on a turntable and is rotated through a full turn. An antenna moves from 1 m to 4 m in height. Both polarizations are taken. The recorded point is the maximum. A 3 m site and a 10 m site are both legal geometries; they are not the same number read at a different zoom. Below 1 GHz the site proves itself with normalized site attenuation. Above 1 GHz the site proves itself with site voltage standing-wave ratio. Those checks are what make the room a measuring instrument rather than a quiet warehouse. The method standards this book names for that work are CISPR 16 and ANSI C63.4. CISPR 16 is the international method family, including the receiver. C63.4 is the United States method for unintentional radiators.",
    )
    add("h2", "7.2 A GTEM is a rehearsal")
    add(
        "body",
        "A GTEM cell is a tapered line you can put a small product in. It is fast, it is indoor, and it is pre-compliance. Correlation to a 3 m or 10 m site is a project, not a theorem. A number from a GTEM that has not been tied to the site you will certify on is a hint. Chapter 20 is the difference between a hint and a certificate.",
    )
    add(
        "body",
        "Key idea. The metal floor, the height scan, and the turntable are the measurement. Skipping one of them is a different experiment.",
    )
    add("h2", "Worked Example 7.1")
    add(
        "body",
        "A lab offers a fixed antenna height of 1.5 m and no turntable, and calls it \"3 m equivalent.\" Which parts of the method are missing?",
    )
    add(
        "body",
        "The height scan from 1 m to 4 m is missing, and the rotation is missing. The maximum this book cares about is the maximum over both. A fixed bore-sight can miss the lobe that the real site will find. The distance being 3 m does not repair that.",
    )
    add("h2", "Practice")
    add("body", "1. Name the method standard that owns antenna height and the quasi-peak detector.")
    add("body", "2. Why is the metal floor not replaced with absorber for a standard radiated-emission run below 1 GHz?")
    add("body", "3. NSA and SVSWR divide the band where? What is each one for?")

    # ----- Chapter 8 -----
    add("h1", "Chapter 8. Peak, Quasi-Peak, and Average")
    add(
        "body",
        "A receiver can report the same signal three ways. Peak is the highest the envelope got. Average is the mean. Quasi-peak is a weighted detector that charges quickly and discharges slowly, so a rare click reads lower than a continuous tone at the same peak. The limit has to say which one it means. A peak reading compared with a quasi-peak limit is a conservative scare, not a failure, until you remeasure.",
    )
    add("h2", "8.1 The weighting this book freezes")
    add(
        "body",
        "CISPR 16-1-1 is the document that defines the quasi-peak detector. This book's snapshot of the time constants, for the teaching discussion and not as a copied table of the standard, is: in the band that covers conducted work up through 30 MHz, charge about 1 ms and discharge about 160 ms; in the radiated bands from 30 MHz to 1 GHz, charge about 1 ms and discharge about 550 ms. A click much shorter than the discharge time does not hold the meter up. A continuous carrier does. If you need the meter constants for a calibration, read the edition your receiver was built to. Do not calibrate a receiver from this paragraph.",
    )
    add("h2", "8.2 Why the three numbers disagree")
    add(
        "body",
        "A switching supply that hiccups, a bus that bursts, and a clock that runs forever will not sit in the same relation of peak to quasi-peak to average. The clock, being always on, makes the three detectors nearly agree. The burst makes peak high and average low, with quasi-peak somewhere between, depending on how often the burst comes back before the detector has discharged. Spread-spectrum clocks and dithered supplies are attempts to move energy around in a way the detector and the bandwidth care about. They are not a license to ignore a narrowband spike. If the energy is still inside one resolution bandwidth all the time, the detector will find it.",
    )
    add(
        "body",
        "Key idea. Match the detector to the limit. Peak is a search tool. Quasi-peak and average are how the published rows are written.",
    )
    add("h2", "Worked Example 8.1")
    add(
        "body",
        "A product shows 6 dB over a quasi-peak limit when the receiver is left in peak detect. What do you know, and what do you not know?",
    )
    add(
        "body",
        "You know the peak is 6 dB over a number that was written for a slower detector. You do not know the quasi-peak. If the source is a continuous clock, the two detectors will be close, and you are probably over. If the source is a rare click, quasi-peak can fall back under the line. Remeasure on the detector the limit names before you respin the board, and before you tell the lab the product fails.",
    )
    add("h2", "Practice")
    add("body", "1. Why can a peak scan be used to find candidates, and not to sign the report?")
    add("body", "2. A continuous 100 MHz clock and a 100 MHz burst that is on 1 percent of the time have the same peak. Which one does quasi-peak punish more?")
    add("body", "3. Who defines the quasi-peak time constants, the limit standard or the method standard?")

    # ----- Chapter 9 -----
    add("h1", "Chapter 9. Limits Are Not Methods")
    add(
        "body",
        "A method says how you measure. A limit says what number fails. Mixing them up produces a report that cites a document and does not say whether the product passed. CISPR 16 and ANSI C63.4 are methods. CISPR 32, and FCC Part 15 Subpart B, are limits for unintentional radiators. EN 55032 is the European adoption of the CISPR 32 limit. Radio conformance, in Chapter 12, is a different limit on a radiator you built on purpose.",
    )
    add("h2", "9.1 The FCC snapshot this book will calculate with")
    add(
        "body",
        "FCC 15.109 Class B, measured at 3 m, quasi-peak, this book's snapshot: 30–88 MHz, 100 μV/m; 88–216 MHz, 150 μV/m; 216–960 MHz, 200 μV/m; above 960 MHz, 500 μV/m. In decibels above a microvolt per meter those rows are 40.0, 43.5, 46.0, and 54.0. Class A in the same section is a commercial limit measured at 10 m: 90, 150, 210, and 300 μV/m in the same four bands. The raw Class A numbers are not \"higher so they are easier\" until you move them to the same distance.",
    )
    add("h2", "9.2 Class B is tighter, after you move the ruler")
    add(
        "body",
        "A far-field 1/r extrapolation from 10 m to 3 m is 20 log10(10/3) = {db_dist} dB. The Class A row of 90 μV/m at 10 m becomes {class_a_3m} μV/m at 3 m under that extrapolation. Class B at the low end is 100 μV/m at 3 m. The residential limit is tighter by {tighter} dB on that row. The extrapolation is not exact in the near field, and the standard does not tell you to certify Class A by measuring at 3 m and dividing. It tells you the distance. The comparison is only there so the draft's sentence, that Class B is tighter than Class A, has a number under it.",
    )
    add(
        "body",
        "CISPR 32 Class B at 3 m, below 1 GHz, is the familiar pair 40 dBμV/m from 30 to 230 MHz and 47 dBμV/m from 230 to 1000 MHz, quasi-peak. Above 1 GHz the same family switches to peak and average limits. This book does not freeze those upper rows. The edition in the test plan does. Below 1 GHz, 40 dBμV/m is 100 μV/m, the same field as the low FCC Class B row, over a different frequency split. The two standards are neighbors. They are not the same sentence.",
    )
    add(
        "body",
        "Key idea. Cite the method and the limit as two documents. Class B is the tighter residential row once distance is honest.",
    )
    add("h2", "Worked Example 9.1")
    add(
        "body",
        "A reading is 46 dBμV/m at 200 MHz at 3 m, quasi-peak. Does it pass the FCC Class B snapshot?",
    )
    add(
        "body",
        "200 MHz sits in 88–216 MHz, whose row is 150 μV/m, which is 43.5 dBμV/m. The reading is about 2.5 dB over. It does not pass that snapshot. It might pass a Class A measurement at 10 m; that is a different setup, not a second opinion on this one. Confirm the detector was quasi-peak before you believe the 2.5.",
    )
    add("h2", "Practice")
    add("body", "1. Convert 200 μV/m to dBμV/m. Which FCC Class B band uses that row?")
    add("body", "2. Why is comparing 90 μV/m Class A with 100 μV/m Class B, without a distance, a false comfort?")
    add("body", "3. Name one method document and one limit document from this chapter.")

    # ----- Chapter 10 -----
    add("h1", "Chapter 10. What Comes Back Down the Cord")
    add(
        "body",
        "Conducted emission is the noise the product pushes onto the mains, measured in voltage across a defined network, not in field strength across the room. A product can pass one and fail the other. The cord is still Chapter 3's antenna. This chapter is the part of that cord the conducted test claims to see, which is the differential and common-mode voltage at the plug, inside a stated band, usually 150 kHz to 30 MHz.",
    )
    add("h2", "10.1 The network is part of the answer")
    add(
        "body",
        "A line impedance stabilization network, the LISN of CISPR 16, presents a defined impedance to the product and a port to the receiver. The classic mains network is 50 Ω in parallel with 50 μH, with a high-pass path into the meter. The 50 Ω is why a voltage reading turns into a current with one division. Change the network and you change the number, even if the product did not change. Always write which LISN.",
    )
    add("h2", "10.2 The Class B voltage snapshot")
    add(
        "body",
        "CISPR 32 Class B mains terminal voltage, this book's snapshot and not a photocopy of the table: from 150 to 500 kHz the quasi-peak limit falls from 66 to 56 dBμV and the average from 56 to 46; from 0.5 to 5 MHz, 56 dBμV quasi-peak and 46 average; from 5 to 30 MHz, 60 quasi-peak and 50 average. The fall from 66 to 56 is with the logarithm of frequency. A single number \"56 dBμV\" is not the limit at 200 kHz. FCC conducted limits for unintentional radiators are a cousin of this table and are not copied here. Use the section the grant actually cites.",
    )
    add(
        "body",
        "Key idea. Conducted is a voltage on a defined impedance. Do not call it a field, and do not call a 3 m failure a conducted failure without looking.",
    )
    add("h2", "Worked Example 10.1")
    add(
        "body",
        "A quasi-peak reading is 60 dBμV on a 50 Ω LISN port. What current is that, and how does it sit against the 5–30 MHz Class B snapshot?",
    )
    add(
        "body",
        "60 dBμV is 1000 μV, which is 1 mV. Into 50 Ω that is {ua60} μA. The snapshot row from 5 to 30 MHz is 60 dBμV quasi-peak, so this reading is exactly on the line in that band. On the line is not a margin. In the 0.5–5 MHz band the quasi-peak row is 56, and the same reading would be 4 dB over. The band is part of the answer.",
    )
    add("h2", "Practice")
    add("body", "1. Convert 46 dBμV into microvolts, then into microamperes on 50 Ω.")
    add("body", "2. Why can a ferrite on the mains cord fix a radiated failure and leave the conducted number almost alone, or the reverse?")
    add("body", "3. A 150 kHz reading of 60 dBμV quasi-peak: pass or fail on the snapshot, and why the band edges matter?")

    # ----- Chapter 11 -----
    add("h1", "Chapter 11. Immunity Is a Different Appointment")
    add(
        "body",
        "Emission asks what the product sends out. Immunity asks what it does when something arrives. A quiet board can still reset when a finger sparks the connector. Passing CISPR 32 does not answer IEC 61000-4-2. They are different days, often the same laboratory, and different lines in the quote.",
    )
    add("h2", "11.1 The family, in this book's words")
    add(
        "body",
        "The IEC 61000-4 series is the method family for immunity. This book will not reproduce its level tables. It will name what each common part is trying to do, so a test plan is readable. 61000-4-2 is electrostatic discharge: a charged human or a charged object, into a connector or through the air. 61000-4-3 is radiated radiofrequency immunity: a field in the room, modulated, while the product does its job. 61000-4-4 is electrical fast transient, the burst from relay contacts and switching, coupled onto cables. 61000-4-5 is surge, the slow high-energy pulse from lightning and power faults. 61000-4-6 is conducted radiofrequency, the same kind of energy as 4-3 but injected on a cable when the wavelength makes a radiating antenna awkward. 61000-4-11 is dips and interruptions of the mains. There are others. A product standard picks the parts and the levels. This series does not invent a level and call it the law.",
    )
    add("h2", "11.2 What \"pass\" means")
    add(
        "body",
        "Immunity criteria are about performance, not about a microvolt. Criterion A, in the ordinary commercial speech, means the product kept working with no upset. Criterion B means it upset and recovered by itself. Criterion C means the operator had to intervene. The product standard says which criterion applies to which test. A reboot can be a pass if the standard allowed it, and a scandal if it did not. Write the criterion next to the level or the report is a diary.",
    )
    add(
        "body",
        "Key idea. Immunity is EMC. It is not the emission scan run backward. Book the tests the product standard names, and record the criterion.",
    )
    add("h2", "Worked Example 11.1")
    add(
        "body",
        "A product passes radiated emission and resets when the ESD gun is applied to a screw near the USB shell. Which document are you failing, and what is the first geometric question?",
    )
    add(
        "body",
        "You are in 61000-4-2 territory, not in the emission limit. The first geometric question is where that screw's metal goes, and whether the USB shell is bonded to the same chassis at the connector or through a long scenic path across the board. The spark current will take the inductance it is given. A short bond at the wall is the same idea as Chapter 6: deal with the outside world at the boundary.",
    )
    add("h2", "Practice")
    add("body", "1. Which 61000-4 part is a burst on a cable, and which is a surge?")
    add("body", "2. Why is a radiated-immunity failure not automatically a radiated-emission failure?")
    add("body", "3. A product blinks and recovers during a dip test. Which question does the report still have to answer?")

    # ----- Chapter 12 -----
    add("h1", "Chapter 12. The Radio Report Is Not the EMC Report")
    add(
        "body",
        "A Wi-Fi radio, a Bluetooth module, or a cellular modem is an intentional radiator. It has a mask: power, occupied bandwidth, out-of-band spurious, often an error-vector magnitude. That mask is radio conformance. The same product, as a box with a processor and a supply, is also an unintentional radiator and an immunity victim. That is the EMC report. One gadget, two reports. OTA performance and SAR sit on the radio side. They are not the quasi-peak scan.",
    )
    add("h2", "12.1 Who owns the watts")
    add(
        "body",
        "Book 6 owns the transmitter chain and the statement that a decibel after the last amplifier is a decibel of EIRP. Book 4 owns the antenna gain that turns conducted power into that EIRP. Book 5 owns the waveform and the band plan. This book owns the legal measurement of what was not supposed to leave, and the separate measurement of the intentional mask when the product is a radio. The chamber time feels similar. The detector, the distance, the limit line, and the pass criterion do not.",
    )
    add("h2", "12.2 A decoder is not the mask")
    add(
        "body",
        "A chamber failure on a Wi-Fi product is usually the box, the cable, the supply, or a spur from the radio's own synthesizer. It is rarely the LDPC decoder. The decoder sits in bits, after the waveform has already been decided. If the emission is at the clock of the processor, look at Chapter 3. If it is an integer multiple of the carrier, look at Book 6's chain and at the radio conformance spurious limit, and do not \"fix\" it with a software retry of the code.",
    )
    add(
        "body",
        "Key idea. Two reports. Emission and immunity on one. The intentional mask, and OTA or SAR when they apply, on the other.",
    )
    add("h2", "Worked Example 12.1")
    add(
        "body",
        "A Wi-Fi gadget fails a spurious line at 2 times the carrier in the radio report, and also fails a 48 MHz line in the unintentional scan. Are these one defect?",
    )
    add(
        "body",
        "No. Twice the carrier is the radio. 48 MHz is a clock or a supply, unless someone has built a bizarre divider that this example does not assume. Two fixes, two reports, possibly one lab day if you planned it. Writing one waiver for both is how a file comes back.",
    )
    add("h2", "Practice")
    add("body", "1. A Wi-Fi gadget: which two reports?")
    add("body", "2. Why does a chamber failure on a Wi-Fi gadget usually not implicate the LDPC decoder?")
    add("body", "3. Where do SAR and OTA sit in this split, and where does quasi-peak sit?")

    # ----- Chapter 13 -----
    add("h1", "Chapter 13. Compute First")
    add(
        "body",
        "The chamber is the expensive place to be surprised. A solver is the cheap place, if you ask it a question it is built to answer. This part is one part of one book, not a second series on numerical methods. The tools named here are the ones a working RF and EMC bench actually meets. There is no open-source Microwave Office hiding under another name. AWR is not HFSS.",
    )
    add("h2", "13.1 Sort the problem before you sort the vendor")
    add(
        "body",
        "Lumped circuits, with dimensions small beside a wavelength and no radiation you care about, are SPICE. Steady-state nonlinear RF, mixers and amplifiers and the spectrum they shed, is harmonic balance in a tool such as ADS or Microwave Office. A planar stackup, traces and planes on known dielectrics, is a 2.5D method-of-moments solver: Momentum, AXIEM, or Sonnet. A connector, a package, a cavity, an antenna with real metal thickness, or a chassis seam is 3D: HFSS, CST, or Analyst. Picking a 2.5D solver for a chassis-mounted connector is the mistake the draft warned about, and Chapter 16 is why.",
    )
    add("h2", "13.2 A model is a set of permissions")
    add(
        "body",
        "Every solver is allowed to ignore something. SPICE is allowed to ignore retardation and radiation. A 2.5D solver is allowed to ignore currents that leave the layers and run up a vertical connector body. A 3D solver is not allowed to invent the mesh you forgot to refine at a gap. Write the permission down next to the plot. A picture of a field with no port definition and no mesh note is a poster. Book 4 may use the same 3D solver for an antenna you meant to build. The antenna's gain still belongs to Book 4. The decision that the connector needs 3D belongs here.",
    )
    add(
        "body",
        "Key idea. One volume for the physics, the solver, and the certificate. Match the solver to the geometry, then book the room.",
    )
    add("h2", "Worked Example 13.1")
    add(
        "body",
        "You have a buck converter's hot loop on a four-layer board, and a separate question about the barrel jack's plastic shell and the metal sleeve. Which solver class for each?",
    )
    add(
        "body",
        "The hot loop, if it is still small and you want the current and the voltage, is SPICE plus a look at the layout area from Chapter 2. The buck as a power circuit is Book 8. If you need the planes' current spread, the stackup solver can see it. The barrel jack is a 3D metal object standing out of the board. That is HFSS or CST, not AXIEM. Two questions, two tools.",
    )
    add("h2", "Practice")
    add("body", "1. Why is AXIEM the wrong tool for a chassis-mounted connector?")
    add("body", "2. Name a harmonic-balance tool and a 3D tool from this chapter, and one job you will not swap between them.")
    add("body", "3. What does \"no open-source Microwave Office\" mean for a lab that hoped to skip the license?")

    # ----- Chapter 14 -----
    add("h1", "Chapter 14. SPICE Knows the Loop, Not the Room")
    add(
        "body",
        "SPICE will tell you the current in a loop you drew, including the parasitic inductance you remembered to draw. It will not tell you the microvolts per meter at 3 m unless you bolt on an antenna model and accept that you have left SPICE's real job. Use it for the current. Hand the current to Chapter 2 or Chapter 3 if you want a first field estimate. Hand the geometry to Chapter 16 if the shape is no longer a loop.",
    )
    add("h2", "14.1 Inductance of the teaching loop")
    add(
        "body",
        "The 2 cm square has area 4×10^−4 m². A round loop with that area has radius {loop_r_mm} mm. Take a wire radius of 0.5 mm, and use only the external inductance L = μ0 R (ln(8R/a) − 2). Internal inductance is omitted on purpose, so a later chapter cannot quietly add it in one example and not another.",
    )
    add(
        "body",
        "That inductance is {l_nh} nH. At 100 MHz its reactance is {xl} Ω. A SPICE run of this loop is a voltage and a current with that L in series, plus the resistance of the copper, plus whatever capacitor you put across it. The radiation resistance of a small loop is a tiny series resistor beside that reactance. Ignoring it in SPICE does not change the current at the level this book is teaching. Ignoring the loop area when you estimate the field does.",
    )
    add(
        "body",
        "Key idea. SPICE is how you get I. The far-field expression is how you turn I and A into a first E. The chamber is how you find out the model missed a cable.",
    )
    add("h2", "Worked Example 14.1")
    add(
        "body",
        "You add the radiation of the loop by attaching a 377 Ω resistor in SPICE, because free space is 377 Ω. What is wrong?",
    )
    add(
        "body",
        "Free-space impedance is the ratio of E to H in a traveling wave. It is not the resistance a small loop presents to its driver. The loop's radiation resistance is a small number set by its area and by frequency, far below {xl} Ω at 100 MHz for this size. A 377 Ω resistor would fake a current that the real loop does not draw, and the field estimate built on that current would be fiction. Keep η in the field formula, where it already sits for the dipole. Do not paste it into the netlist as a load.",
    )
    add("h2", "Practice")
    add("body", "1. Reactance scales with frequency. What is the reactance of this {l_nh} nH at 50 MHz?")
    add("body", "2. Why is omitting radiation resistance acceptable for the current, and not acceptable for the field?")
    add("body", "3. A SPICE deck has no cable. What failure mode of Chapter 3 is the deck blind to?")

    # ----- Chapter 15 -----
    add("h1", "Chapter 15. Harmonic Balance")
    add(
        "body",
        "A clock or a power amplifier in periodic steady state is a spectrum, not a one-time transient. Harmonic balance solves the circuit at a set of harmonics and balances the linear parts in frequency against the nonlinear parts in time. It is the right tool when you already know the drive is periodic and you want the lines. It is the wrong tool for a one-shot ESD event. That event is a transient, and Chapter 11's gun is not a harmonic.",
    )
    add("h2", "15.1 ADS, Microwave Office, and what they are not")
    add(
        "body",
        "ADS and Microwave Office (AWR) are the harmonic-balance benches this series expects you to recognize. They also grow 2.5D and system tools beside that engine. The engine is not a 3D field solver. AWR is not HFSS. Sending a chassis seam to harmonic balance, with no geometry, answers a circuit you drew, not the slot you built. There is no open-source Microwave Office that reproduces that bench. Open SPICE exists. An open harmonic-balance code exists in places. The licensed RF workbench, with its libraries and its layout tie-in, is a different object. Plan on it or plan around it. Do not plan on a free file that has the same name.",
    )
    add("h2", "15.2 What you still owe the chamber")
    add(
        "body",
        "A harmonic-balance spectrum at a transistor lead is a conducted spectrum. The path from that lead to a cable is Chapters 4 through 6. The legal number is Chapters 7 through 10. A beautiful simulated spur at −80 dBm inside a chip does not tell you the 3 m field. It tells you the spur exists, so you know which line to look for when the receiver stops.",
    )
    add(
        "body",
        "Key idea. Harmonic balance is for a periodic spectrum in a circuit. Geometry still has to be someone else's solver, or a measurement.",
    )
    add("h2", "Worked Example 15.1")
    add(
        "body",
        "A PA simulation shows a second harmonic 15 dB under the fundamental at the drain. The radio report fails that harmonic as radiated spurious. What did the simulation not include?",
    )
    add(
        "body",
        "It did not include the match, the feed, the antenna, and the box, unless you added them. Book 6 owns that chain. Fifteen decibels at the drain can be eaten by a match that was tuned for the fundamental and is accidental at the second harmonic, in either direction. The simulation is a clue. The report is the measurement of the clue after the chain.",
    )
    add("h2", "Practice")
    add("body", "1. Why is harmonic balance a poor fit for an ESD strike?")
    add("body", "2. Name one thing AWR will not do that HFSS will.")
    add("body", "3. A simulated line is 40 dB down at the pin. Why is that not yet a pass against a radiated spurious mask?")

    # ----- Chapter 16 -----
    add("h1", "Chapter 16. A Board Is a Stack")
    add(
        "body",
        "A printed board is a set of copper layers in a dielectric whose thickness and constant you can write down. A 2.5D solver takes that stack seriously. It assumes the currents live on those layers, the dielectrics are infinite or at least wide beside the structure, and the vertical direction is vias and ports rather than a forest of arbitrary metal. Momentum, AXIEM, and Sonnet are the names. They disagree in the details of the Green's function and the mesher. They agree about the kind of object they are for.",
    )
    add("h2", "16.1 What a stackup solver is good at")
    add(
        "body",
        "A trace over a plane, a coupled pair, a power-plane gap that is still a gap in a layer, a via fence, a filter printed in copper: these are stackup problems. You get impedance, coupling, and a radiation estimate that knows the board's dielectric. Book 9's laminate loss, the decibels per meter of FR-4 versus a better resin, is that book's number. This solver is where you would notice that loss if you put the right dielectric in. Do not type \"FR-4\" and walk away. Two mills' FR-4 do not share one loss tangent. Book 9 already said so.",
    )
    add("h2", "16.2 What it is not allowed to see")
    add(
        "body",
        "A chassis-mounted connector is a three-dimensional piece of metal, often taller than the board is thick, opening into a cage that is not a dielectric layer. AXIEM, and any solver built on the same layered-media assumption, does not have that cage in its model unless you have abused a port to fake it. The fake will produce a plot. The plot will not be the connector. Use a 3D solver for that part, and a stackup solver for the traces that run up to it. You are allowed to use two tools on one product.",
    )
    add(
        "body",
        "Key idea. 2.5D is for layers. The moment the metal stands up into the room, you have left the assumption.",
    )
    add("h2", "Worked Example 16.1")
    add(
        "body",
        "A reviewer asks for an AXIEM run of an SMA connector bolted through a wall into a screened box. What do you run instead, and what might you still run in AXIEM?",
    )
    add(
        "body",
        "The connector, the wall, and the box are a 3D solve. The microstrip that feeds the connector, in the stackup, on the board, can stay in AXIEM or Momentum or Sonnet. The handoff is a port at the edge of each model's honesty. One picture that pretends to be both is the failure mode.",
    )
    add("h2", "Practice")
    add("body", "1. Why is AXIEM the wrong tool for a chassis-mounted connector? Answer in terms of the assumption, not the brand.")
    add("body", "2. A via fence around a trace is still a stackup problem. Why?")
    add("body", "3. You set Df = 0.020 for every \"FR-4\" board. What did Book 9 warn you about?")

    # ----- Chapter 17 -----
    add("h1", "Chapter 17. When the Metal Is the Problem")
    add(
        "body",
        "HFSS, CST, and Analyst solve Maxwell's equations on a mesh that can describe a connector body, a package lead, a cavity, and an antenna. They are slow, they are licensed, and they are the right expense when the shape is the problem. They are a waste when the problem was the common-mode current on a cable you could have measured with a current probe in an afternoon.",
    )
    add("h2", "17.1 Mesh and ports")
    add(
        "body",
        "A 3D result is only as good as the mesh at the gap that sets the field, and as good as the port you used to excite it. A default mesh that looks smooth and a port that is not the mode the connector actually launches will give you a confident wrong S-parameter. Ask for the mesh at the seam, the port impedance, and the convergence, in that order, before you look at the color plot. The color plot is what people paste into a review. The convergence is what decides whether the paste is allowed.",
    )
    add("h2", "17.2 Antennas you meant, and antennas you did not")
    add(
        "body",
        "An intentional antenna's gain, pattern, and match are Book 4's subject, even if the solver is the same executable. An unintentional antenna, the seam and the pigtail and the display aperture, is this chapter. Do not file a Book 4 gain number as an EMC pass. Do not file an EMC seam study as an antenna datasheet. Same mesh engine, different question, different book.",
    )
    add(
        "body",
        "Key idea. 3D is for metal whose shape you cannot flatten into layers. The mesh note is part of the result.",
    )
    add("h2", "Worked Example 17.1")
    add(
        "body",
        "A simulation of a USB shell shows a strong field at a gap, and the mesh picture shows two triangles across that gap. What do you do before you believe the field number?",
    )
    add(
        "body",
        "Refine the mesh at the gap and rerun until the field, or the S-parameter you actually care about, stops moving. Two triangles across a gap that dominates the capacitance is a drawing, not a solution. If the refined run moves the result by more than the margin you were counting on, the first plot was not evidence.",
    )
    add("h2", "Practice")
    add("body", "1. Name two 3D solvers from this chapter and one structure each is aimed at.")
    add("body", "2. Why is a current-probe measurement of a cable sometimes the better spend than a 3D model of the same cable?")
    add("body", "3. A gain plot from HFSS is handed to you as proof the product passes CISPR 32. What is missing?")

    # ----- Chapter 18 -----
    add("h1", "Chapter 18. The Day in the Lab")
    add(
        "body",
        "Somebody has to run the method, on a site that has been shown to meet it, and sign a report a regulator will accept. That somebody is not the person who drew the board, unless that person also happens to work at the laboratory. This chapter names two laboratories the series already decided to name, and then describes the day so the names are not trivia.",
    )
    add("h2", "18.1 7layers and Hermon")
    add(
        "body",
        "7layers, part of Bureau Veritas, is the connected-product laboratory: radios, approvals, the stack of reports a wireless product collects. Hermon Laboratories, in Binyamina, is the broader product laboratory. It is not Harmon, the audio company, and it is not a typo for one. Hermon's accreditations in this book's snapshot include A2LA and an FCC designation under IL1001, with military and RTCA work in the same building. Accreditations move. The sentence that does not move is the job split. They measure. They do not design the board. Debug time, if they offer it, is a separate line on the quote, with an engineer and a current probe, and it is still your schematic at the end of the day.",
    )
    add("h2", "18.2 What you owe them before you arrive")
    add(
        "body",
        "A working product, a way to exercise the modes that emit, cables that are the cables you will ship, and a test plan that names the standards. A product that only emits when a hidden menu is on, tested in the quiet menu, is a pass you did not earn. The laboratory will not know the menu exists. Modes are your job. The height scan is theirs.",
    )
    add(
        "body",
        "Key idea. The laboratory measures against the method. Design stays with the people who can change the layout.",
    )
    add("h2", "Worked Example 18.1")
    add(
        "body",
        "A quote from a lab says \"EMC and radio, five days, debug included.\" What questions do you still ask?",
    )
    add(
        "body",
        "Which standards, which editions, 3 m or 10 m, which detectors, whether immunity is in the five days or only emission, whether the radio mask is in the same week, and how many hours of debug are actually included before it becomes an engineering rate. \"Debug included\" without a number of hours is a greeting. 7layers is the right kind of place for the radio half. A general product lab such as Hermon is the right kind of place for a box that is not a radio at all. A product that is both may need both kinds of report, and sometimes one organization can issue them. Ask which reports, not which logo.",
    )
    add("h2", "Practice")
    add("body", "1. Spell the laboratory in Binyamina, and name the audio company it is not.")
    add("body", "2. What do 7layers and Hermon not do, even on a day you are paying for debug?")
    add("body", "3. Why must the cables at the site be the cables you intend to ship?")

    # ----- Chapter 19 -----
    add("h1", "Chapter 19. A Failure of Two Decibels")
    add(
        "body",
        "Two decibels over a limit feels like a tragedy in the room and like a layout problem on the flight home. It is a layout problem. The theory is Chapter 1. You do not need a new Maxwell equation. You need a smaller area, less common-mode current, or a better bond at the wall.",
    )
    add("h2", "19.1 What two decibels is, as a factor")
    add(
        "body",
        "A field ratio of 2 dB is 10^(2/20) = {field2}. The field is about 26 percent high. The current, if it is the only thing you change, needs to fall by that same factor. The area, if it is the only thing you change, needs to fall by that same factor. You are not looking for a tenfold redesign. You are looking for the last quarter of a loop or the last quarter of a cable current. That is why a ferrite, a shorter pigtail, or a return via next to a signal via fixes a 2 dB failure, and a new chip often does not.",
    )
    add("h2", "19.2 Do not spend the 2 dB on the wrong radiator")
    add(
        "body",
        "Find the frequency first. If it is the clock or an odd harmonic, look at the loop and then at the cable the clock's return might be driving. If it is the switcher, look at the hot loop Book 8 already told you to keep small, and at the input cord. If it is the carrier, you are in Chapter 12's radio report and Book 6's chain, not in a ferrite on the debug UART. A 2 dB fix on the wrong line is a new failure at the original line.",
    )
    add(
        "body",
        "Key idea. Failing by 2 dB is a layout change. The physics was Chapter 1. The factor is {field2}, not an order of magnitude.",
    )
    add("h2", "Worked Example 19.1")
    add(
        "body",
        "The 2 cm loop of Chapter 2 is 2 dB over at 100 MHz. You cannot change the current. What side length brings the area down by the factor {field2}?",
    )
    add(
        "body",
        "Area scales with the side squared, so the side scales with the square root of {field2}, which is about 1.12. The side should become 2 cm / 1.12, about 1.8 cm, if the loop was square and the current truly stayed put. That is a via moved closer, not a new architecture. If the real radiator was the cable, shrinking the loop does nothing, and this example was the wrong example. Identify the radiator before you move the via.",
    )
    add("h2", "Practice")
    add("body", "1. A failure of 6 dB is what field ratio? How many times more current is that, if current is the only cause?")
    add("body", "2. Why is \"add a shield can over the crystal\" not automatically the 2 dB fix?")
    add("body", "3. The reading is 2 dB over in peak detect and 1 dB under in quasi-peak. Did you pass the quasi-peak limit?")

    # ----- Chapter 20 -----
    add("h1", "Chapter 20. Pre-compliance Is a Rehearsal")
    add(
        "body",
        "A near-field probe, a current clamp, a GTEM, and a rented afternoon on a chamber that is not the accredited site are rehearsals. They tell you which cable, which mode, which harmonic. They do not sign the declaration. The certificate is the accredited method, the right detector, the right distance, and the report number.",
    )
    add("h2", "20.1 What a rehearsal is for")
    add(
        "body",
        "Use it to rank causes. Clamp the mains, the USB, the HDMI, one at a time. The cable whose clamp reading tracks the failure is Chapter 3. The cable that does nothing is not your antenna today. A probe over the switcher node finds Chapter 2's loop if the loop is the source, and finds nothing useful if the source is the slot in the shield. Rehearsal is a sorting tool. Write down what you unplugged, or the sort is a memory.",
    )
    add("h2", "20.2 What you still buy")
    add(
        "body",
        "You buy the day at a laboratory that can issue the report your market asks for. For a connected product that is 7layers' kind of work. For a broader box it may be Hermon's kind of work. Bring the fixes from the rehearsal already installed, on the cables you ship, in the mode that emits. A rehearsal that passed because the noisy cable was coiled on the floor will be exposed by a technician who drapes the cable the way the method requires. Let them.",
    )
    add(
        "body",
        "Key idea. Pre-compliance chooses the layout change. The accredited site is the measurement that counts.",
    )
    add("h2", "Worked Example 20.1")
    add(
        "body",
        "A GTEM says you have 8 dB of margin. The 3 m site says you are 2 dB over. Which number goes in the file?",
    )
    add(
        "body",
        "The 3 m site, if that is the method the limit was written for. The GTEM correlation was off by about 10 dB for this product, which is a fact about the correlation, not a fact you get to average. Fix the 2 dB as in Chapter 19, and keep the GTEM as a before-and-after tool for the next spin. Do not submit the GTEM plot as the record.",
    )
    add("h2", "Practice")
    add("body", "1. Name two rehearsal tools and one thing they cannot sign.")
    add("body", "2. A current clamp on the HDMI cable tracks the failing line, and a clamp on the mains does not. Where is the antenna?")
    add("body", "3. Why must the final cable dressing match the method rather than the dressing that passed in your lab?")

    # ----- Chapter 21 -----
    add("h1", "Chapter 21. What This Volume Refuses to Own")
    add(
        "body",
        "A series that repeats itself becomes a place to hide. This chapter is the list of refusals, so a later edit cannot smuggle Book 6's watts or Book 8's magnetics back in under an EMC heading.",
    )
    add("h2", "21.1 The list")
    add(
        "body",
        "Antenna gain, beamwidth, and the Friis transmission factor stay in Book 4. Transmitter power, the load line, feed loss, EIRP, and the intentional radio's chain stay in Book 6. The buck converter, the grid, and the four magnetics shelves stay in Book 8. The hot loop of that buck is named from here only as a loop area. Laminate loss, the package, and the layout habits of a fast digital board stay in Book 9. Filter transfer functions and op-amp circuits stay in Book 2. The square-wave series stays in Book 1. Band plans and modems stay in Book 5. If a problem needs one of those to finish, point at the book and stop.",
    )
    add("h2", "21.2 What remains, on one page")
    add(
        "body",
        "This volume keeps the unintentional radiator, the f² scaling and its square-wave caveat, the common-mode cable, the slot in the return, the shield as a box, the filter at the boundary, the semi-anechoic method, the three detectors, the split between CISPR 16 or C63.4 and CISPR 32 or FCC 15 B, the conducted voltage on a LISN, the immunity family, the second report for a radio, the solver sorted by geometry, the laboratories that measure, the 2 dB layout fix, and the difference between a rehearsal and a certificate.",
    )
    add(
        "body",
        "Key idea. One volume for the physics, the solver, and the certificate. The neighboring volumes keep their own numbers.",
    )
    add("h2", "Practice")
    add("body", "1. A 100 W GaN amplifier at 3.5 GHz fails a harmonic mask. Which book owns the amplifier, and which book owns the mask measurement?")
    add("body", "2. A buck at 400 kHz fails conducted emission. Which book owns the converter, and which chapter of this book owns the LISN reading?")
    add("body", "3. Why does this book use Book 8's skin-depth rule instead of writing a second one?")

    # ----- Appendix -----
    add("h1", "Appendix A. Answers to the Practice")
    add(
        "body",
        "The arithmetic uses the constants declared at the front. A reason answer is a reason, not a second worked example.",
    )
    add("h2", "Chapter 1")
    add("body", "1. Frequency ratio 3, field ratio 9 if the current matched. If the current fell as 1/n, the field ratio is 9 × 1/3 = 3. Same pattern as the 25 MHz third harmonic.")
    add("body", "2. Because the fourth harmonic of a symmetric square is an even harmonic the series does not owe, and because 24 dB is the field ratio only when the currents match. A report that states it as a fact has invented a current.")
    add("body", "3. A small current loop, which is a magnetic dipole. A wire with common-mode current, which is an electric dipole.")
    add("h2", "Chapter 2")
    add("body", "1. Frequency halved, field falls as f², so the field drops by a factor of 4.")
    add("body", "2. Side halved, area drops by a factor of 4, and the far field drops by that same factor.")
    add("body", "3. A near-field probe is near, often magnetically near, at a distance where the 1/r far-field expression is not the limit. The limit is a calibrated antenna at the method's distance and height.")
    add("h2", "Chapter 3")
    add("body", "1. E scales with L in the short-dipole expression, so the field doubles.")
    add("body", "2. A 1 m cord at 100 MHz is not short beside the wavelength, so the formula would lie. The book gives the 10 cm case and warns that the long cord radiates at least as easily.")
    add("body", "3. It changed I, the common-mode current. Length, frequency, and distance stayed.")
    add("h2", "Chapter 4")
    add("body", "1. At 1 kHz the return spreads. Resistance, not inductance, is the smaller impedance, so the current uses the wide copper.")
    add("body", "2. One connection point gives the return a single place to cross with the signal. Three crossings are three loops, and the signal will use all of them in some proportion.")
    add("body", "3. Look at the path from that bus to the connector first. The amplitude is Book 2's or the silicon's concern. The antenna is the path.")
    add("h2", "Chapter 5")
    add(
        "body",
        "1. δ = 66/√(10^7) = 66/3162 = 0.0209 mm, about 21 μm. One ounce is 0.0348 mm, so the foil is only a little over one skin depth. Absorption is much less than the {absorb} dB you had at 100 MHz. Thickness can matter at 10 MHz even though it did not matter at 100 MHz.",
    )
    add("body", "2. A 15 cm aperture is a small fraction of a 3 m wavelength and a large fraction of a 30 cm wavelength. The same hole is a better antenna at 1 GHz.")
    add("body", "3. The 5 cm became a pigtail, which is Chapter 3's wire, inside the shield, where the shield cannot help it.")
    add("h2", "Chapter 6")
    add("body", "1. The capacitor is across the pair. Common-mode current does not put a voltage across it. There is no shunt path for that current.")
    add("body", "2. The cable past the connector. The choke is no longer between the noise and that antenna.")
    add("body", "3. Because a cord's geometry, dressing, and length change the impedance. A single radiation resistance would be a fake constant.")
    add("h2", "Chapter 7")
    add("body", "1. CISPR 16 owns the quasi-peak detector and, with ANSI C63.4 for the United States unintentional method, the antenna-height scan. The short answer the draft expected is CISPR 16.")
    add("body", "2. Because the method is semi-anechoic. The metal floor is part of the site the limits were written against. Covering it makes a different site.")
    add("body", "3. NSA below 1 GHz, SVSWR above 1 GHz. Each is how the room proves it is allowed to measure that band.")
    add("h2", "Chapter 8")
    add("body", "1. Peak finds the lines quickly and reads high. The limit is usually quasi-peak or average. Signing with the wrong detector invents a failure or hides one.")
    add("body", "2. The continuous clock. Quasi-peak stays up if the signal is always there. The 1 percent burst is gone for most of the discharge time.")
    add("body", "3. The method standard, CISPR 16. The limit standard only points at it.")
    add("h2", "Chapter 9")
    add("body", "1. 200 μV/m is 46.0 dBμV/m. FCC Class B uses it from 216 to 960 MHz.")
    add("body", "2. They are measured at different distances. Moved to 3 m by a 1/r picture, 90 μV/m at 10 m becomes 300 μV/m, and Class B's 100 μV/m is tighter by about {tighter} dB.")
    add("body", "3. Method: CISPR 16 or ANSI C63.4. Limit: CISPR 32 or FCC Part 15 B.")
    add("h2", "Chapter 10")
    add("body", "1. 46 dBμV is 199.5 μV. On 50 Ω that is 3.99 μA.")
    add("body", "2. Radiated failure is often common-mode current on the cord as an antenna, which a ferrite can cut. Conducted failure is the voltage the LISN sees at the plug, which can be differential and can ignore a choke placed for the other current. The reverse happens when the ferrite is the wrong impedance for the radiated band and the right one for the conducted band. They are different measurements.")
    add("body", "3. From 150 to 500 kHz the quasi-peak snapshot starts at 66 dBμV and falls toward 56. At the 150 kHz edge, 60 is under 66, so it passes that edge. It would not pass as a blanket claim everywhere in the band. Read the limit at the frequency you measured.")
    add("h2", "Chapter 11")
    add("body", "1. 61000-4-4 is the burst. 61000-4-5 is the surge.")
    add("body", "2. Emission is what you send, measured against a microvolt limit. Immunity is what a field does to your function, judged by a performance criterion. A sensitive reset line can fail immunity on a product that emits almost nothing.")
    add("body", "3. Whether the product standard's criterion allowed a self-recovering blink, or required uninterrupted operation.")
    add("h2", "Chapter 12")
    add("body", "1. The EMC report, emission and immunity. The radio-conformance report, the intentional mask. OTA and SAR ride with the radio report when the product needs them.")
    add("body", "2. The LDPC decoder runs on bits after the waveform exists. A chamber line is analog energy at a frequency. Look at the clock, the supply, the cable, or the radio's spur, not at the code.")
    add("body", "3. SAR and OTA sit with the radio report. Quasi-peak sits with the EMC emission limit.")
    add("h2", "Chapter 13")
    add("body", "1. AXIEM is a layered-media solver. A chassis-mounted connector is three-dimensional metal outside that assumption. The plot would be a different object from the connector you built.")
    add("body", "2. Harmonic balance: ADS or Microwave Office, for a periodic circuit spectrum. 3D: HFSS, CST, or Analyst, for a connector or a seam. Do not ask harmonic balance to mesh a chassis, and do not ask HFSS to replace a transistor model you never drew.")
    add("body", "3. It means the licensed RF workbench is not a free substitute you can download under that name. Plan a real tool or a different method.")
    add("h2", "Chapter 14")
    add("body", "1. Half the frequency, so half of {xl} Ω, which is {xl_half} Ω.")
    add("body", "2. Radiation resistance is negligible beside the reactance, so the current hardly changes if you omit it. The field is exactly the thing that resistor was a bad model of. You still compute the field from I and A, or you measure it.")
    add("body", "3. Common-mode current on a cable that was never in the deck. SPICE cannot fail a radiator it does not contain.")
    add("h2", "Chapter 15")
    add("body", "1. An ESD strike is a one-shot transient, not a periodic steady state. Harmonic balance has no fundamental to lock to.")
    add("body", "2. HFSS will mesh a three-dimensional connector or seam. AWR's harmonic balance will not, because it is a circuit engine. AWR is not HFSS.")
    add("body", "3. The mask is a radiated or conducted limit at a defined port or distance, after the match, the feed, and the antenna. A pin voltage is upstream of all three.")
    add("h2", "Chapter 16")
    add("body", "1. The solver assumes currents in a layered stack. The connector and the chassis are not layers. Use a 3D solver for that metal.")
    add("body", "2. The vias and the traces are still features of the stackup. Nothing has left the layers for a tall piece of hardware.")
    add("body", "3. That two mills' FR-4 do not share one dissipation factor. Spec the material at the frequency you care about.")
    add("h2", "Chapter 17")
    add("body", "1. HFSS or CST or Analyst. A connector, a package, a cavity, or a seam. Any two of those structures are enough.")
    add("body", "2. A clamp measures the current that Chapter 3 says is the usual cause, in an hour, on the real cable. A 3D model of a cable over a table is easy to get wrong and slow to mesh.")
    add("body", "3. The limit, the distance, the detector, and the site validation. A gain is Book 4. CISPR 32 is a field limit on a method.")
    add("h2", "Chapter 18")
    add("body", "1. Hermon Laboratories, Binyamina. Not Harmon.")
    add("body", "2. They do not design the board. Debug, if purchased, finds a cause. The layout change is still yours.")
    add("body", "3. Because the cable is the antenna. A shorter or quieter cable is a different product from the one you will ship.")
    add("h2", "Chapter 19")
    add("body", "1. 6 dB is a field ratio of two, because 20 log10(2) is 6.02. Twice the current, if current is the only cause.")
    add("body", "2. The can does nothing if the radiator is the cable or a seam outside the can. Identify the frequency and the cable first.")
    add("body", "3. Yes, if the limit is quasi-peak and the quasi-peak reading is 1 dB under, and you trust the site. The peak reading was the search, not the verdict.")
    add("h2", "Chapter 20")
    add("body", "1. A near-field probe, a current clamp, or a GTEM. None of them signs an accredited 3 m or 10 m report.")
    add("body", "2. On the HDMI cable. The mains is not today's radiator.")
    add("body", "3. The method specifies the arrangement that finds the maximum. A coil that hides the lobe will not be the arrangement in the report.")
    add("h2", "Chapter 21")
    add("body", "1. Book 6 owns the amplifier. This book owns the mask measurement as a report. Book 4 owns the antenna gain if the mask is in field strength.")
    add("body", "2. Book 8 owns the converter. Chapter 10 owns the LISN reading.")
    add("body", "3. So the series has one copper rule. Book 8 keeps the magnetics shelves. This book only borrows the rule for a wall.")

    add("h1", "Appendix B. The Snapshot Tables")
    add(
        "body",
        "These are the numbers the worked examples use. A test plan cites the edition. If the edition disagrees with this page, the edition wins and these examples are redone.",
    )
    add("h2", "FCC 15.109 Class B at 3 m, quasi-peak")
    add("body", "30–88 MHz: 100 μV/m, 40.0 dBμV/m. 88–216 MHz: 150 μV/m, 43.5 dBμV/m. 216–960 MHz: 200 μV/m, 46.0 dBμV/m. Above 960 MHz: 500 μV/m, 54.0 dBμV/m.")
    add("h2", "FCC 15.109 Class A at 10 m, quasi-peak")
    add("body", "30–88 MHz: 90 μV/m. 88–216 MHz: 150 μV/m. 216–960 MHz: 210 μV/m. Above 960 MHz: 300 μV/m. Do not compare these with Class B until the distance is the same. Under a 1/r move to 3 m, the 90 μV/m row becomes {class_a_3m} μV/m.")
    add("h2", "CISPR 32 Class B, this book's partial snapshot")
    add("body", "Radiated, 3 m, quasi-peak, below 1 GHz: 40 dBμV/m from 30 to 230 MHz, 47 dBμV/m from 230 to 1000 MHz. Above 1 GHz the standard uses peak and average. Those rows are not frozen here.")
    add("body", "Mains conducted, quasi-peak and average: 150–500 kHz, 66 falling to 56 dBμV quasi-peak and 56 falling to 46 average; 0.5–5 MHz, 56 and 46; 5–30 MHz, 60 and 50. The LISN in the worked example is 50 Ω.")
    add("h2", "Methods, not limits")
    add("body", "CISPR 16 for the receiver, the quasi-peak detector, the LISN, and site validation. ANSI C63.4 for the United States unintentional radiated and conducted method. IEC 61000-4-2, 4-3, 4-4, 4-5, 4-6, and 4-11 for the immunity appointments named in Chapter 11. Levels and criteria come from the product standard, not from this appendix.")

    add("h1", "Appendix C. Symbols Used in the Examples")
    add("body", "A, loop area, m². The teaching square is 2 cm on a side.")
    add("body", "E, electric field, V/m, far-field model unless a chapter says otherwise.")
    add("body", "I, current. Loop current and common-mode current are different objects and are not added.")
    add("body", "L, length of a short wire, or inductance, and the chapter says which. The teaching wire is 10 cm. The teaching round-loop inductance is {l_nh} nH.")
    add("body", "f, frequency, hertz. The clock example is 25 MHz. The harmonic example is 100 MHz.")
    add("body", "r, distance, meters. Class B examples use 3 m.")
    add("body", "δ, copper skin depth, 66/√f millimeters. Book 8 owns the magnetics use of this rule.")
    add("body", "η, 376.7 Ω, free-space E/H. Not a load resistor in SPICE.")

    return b


def paragraph_xml(kind, text):
    safe = escape(text)
    if kind == "title":
        return (
            "<w:p><w:pPr><w:spacing w:after=\"160\" w:line=\"276\" w:lineRule=\"auto\"/>"
            "<w:jc w:val=\"center\"/></w:pPr><w:r><w:rPr>"
            "<w:rFonts w:ascii=\"Amazon Ember\" w:hAnsi=\"Amazon Ember\" w:cs=\"Amazon Ember\"/>"
            "<w:b/><w:i w:val=\"0\"/><w:color w:val=\"0000FF\"/><w:sz w:val=\"56\"/>"
            f"</w:rPr><w:t xml:space=\"preserve\">{safe}</w:t></w:r></w:p>"
        )
    if kind in ("center", "italic"):
        italic = "<w:i/>" if kind == "italic" else "<w:i w:val=\"0\"/>"
        return (
            "<w:p><w:pPr><w:spacing w:after=\"160\" w:line=\"276\" w:lineRule=\"auto\"/>"
            "<w:jc w:val=\"center\"/></w:pPr><w:r><w:rPr>"
            "<w:rFonts w:ascii=\"Calibri\" w:hAnsi=\"Calibri\" w:cs=\"Calibri\"/>"
            f"<w:b w:val=\"0\"/>{italic}<w:color w:val=\"000000\"/><w:sz w:val=\"22\"/>"
            f"</w:rPr><w:t xml:space=\"preserve\">{safe}</w:t></w:r></w:p>"
        )
    if kind == "h1":
        return (
            "<w:p><w:pPr><w:pStyle w:val=\"Heading1\"/></w:pPr>"
            f"<w:r><w:t xml:space=\"preserve\">{safe}</w:t></w:r></w:p>"
        )
    if kind == "h2":
        return (
            "<w:p><w:pPr><w:pStyle w:val=\"Heading2\"/></w:pPr>"
            f"<w:r><w:t xml:space=\"preserve\">{safe}</w:t></w:r></w:p>"
        )
    return (
        "<w:p><w:pPr><w:spacing w:after=\"160\" w:line=\"276\" w:lineRule=\"auto\"/></w:pPr>"
        "<w:r><w:rPr>"
        "<w:rFonts w:ascii=\"Calibri\" w:hAnsi=\"Calibri\" w:cs=\"Calibri\"/>"
        "<w:b w:val=\"0\"/><w:i w:val=\"0\"/><w:color w:val=\"000000\"/><w:sz w:val=\"22\"/>"
        f"</w:rPr><w:t xml:space=\"preserve\">{safe}</w:t></w:r></w:p>"
    )


DOCUMENT_HEAD = (
    "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
    "<w:document xmlns:wpc=\"http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas\" "
    "xmlns:mo=\"http://schemas.microsoft.com/office/mac/office/2008/main\" "
    "xmlns:mc=\"http://schemas.openxmlformats.org/markup-compatibility/2006\" "
    "xmlns:mv=\"urn:schemas-microsoft-com:mac:vml\" "
    "xmlns:o=\"urn:schemas-microsoft-com:office:office\" "
    "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" "
    "xmlns:m=\"http://schemas.openxmlformats.org/officeDocument/2006/math\" "
    "xmlns:v=\"urn:schemas-microsoft-com:vml\" "
    "xmlns:wp14=\"http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing\" "
    "xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" "
    "xmlns:w10=\"urn:schemas-microsoft-com:office:word\" "
    "xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" "
    "xmlns:w14=\"http://schemas.microsoft.com/office/word/2010/wordml\" "
    "xmlns:wpg=\"http://schemas.microsoft.com/office/word/2010/wordprocessingGroup\" "
    "xmlns:wpi=\"http://schemas.microsoft.com/office/word/2010/wordprocessingInk\" "
    "xmlns:wne=\"http://schemas.microsoft.com/office/word/2006/wordml\" "
    "xmlns:wps=\"http://schemas.microsoft.com/office/word/2010/wordprocessingShape\" "
    "mc:Ignorable=\"w14 wp14\"><w:body>"
)

SECT = (
    "<w:sectPr>"
    "<w:pgSz w:w=\"12240\" w:h=\"15840\"/>"
    "<w:pgMar w:top=\"1440\" w:right=\"1440\" w:bottom=\"1440\" w:left=\"1440\" "
    "w:header=\"720\" w:footer=\"720\" w:gutter=\"0\"/>"
    "<w:cols w:space=\"720\"/>"
    "<w:docGrid w:linePitch=\"360\"/>"
    "</w:sectPr>"
)


def build_document_xml():
    parts = [DOCUMENT_HEAD]
    for kind, text in blocks():
        parts.append(paragraph_xml(kind, text))
    parts.append(SECT)
    parts.append("</w:body></w:document>")
    return "".join(parts)


def words_in_blocks():
    return sum(len(text.split()) for _, text in blocks())


def main():
    xml = build_document_xml()
    # Rebuild the docx from the previous package so styles stay Amazon Ember blue.
    # If this is a fresh tree, the file we are about to overwrite must already exist
    # as the styled stub. Read it first.
    if not OUT.exists():
        raise SystemExit(f"missing styled template {OUT}")
    original = OUT.read_bytes()
    tmp = OUT.with_suffix(".docx.tmp")
    with zipfile.ZipFile(OUT, "r") as zin, zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = xml.encode("utf-8")
            # store document uncompressed? deflated is fine
            zout.writestr(item, data)
    tmp.replace(OUT)
    n = words_in_blocks()
    print(f"wrote {OUT}")
    print(f"words {n}")
    print(f"loop current mA {N['i_loop_ma']}")
    print(f"wire current uA {N['i_wire_ua']}")
    print(f"absorb dB {N['absorb']}")
    # keep a copy of the pre-build bytes only if we failed the home-phrase check
    blob = " ".join(text for _, text in blocks())
    for phrase in ("CISPR", "7layers", "Hermon", "sixteen", "AXIEM", "quasi-peak"):
        if phrase.lower() not in blob.lower() and phrase not in blob:
            original_path = OUT.with_suffix(".docx.pre-fill")
            original_path.write_bytes(original)
            raise SystemExit(f"missing phrase {phrase}")
    if n < 8000:
        raise SystemExit(f"book still short: {n} words")


if __name__ == "__main__":
    main()
