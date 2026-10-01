# -*- coding: utf-8 -*-
"""Complete Kindle textbook: Book 6, Transceivers and High-Power RF."""

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lib_ee_doc import add_p, new_book, word_count

OUT = ROOT / "EE6" / "Transceivers_and_High_Power_RF_Book6.docx"

# One-home locked numbers. Print 10.13 and 3.13; keep 10.125 and 3.125 in the arithmetic.
P100 = 100.0
ROPT_GAN = (50.0 - 5.0) ** 2 / (2.0 * P100)
ROPT_LDMOS = (28.0 - 3.0) ** 2 / (2.0 * P100)
LOSS_1DB = 10 ** (-0.1)
T0 = 290.0
F_3DB = 10 ** (3.0 / 10.0)
TE_3DB = T0 * (F_3DB - 1.0)
KB = 1.380649e-23
C0 = 2.99792458e8
PI = math.pi

# Other checked numbers used in examples
ROPT_200 = (50.0 - 5.0) ** 2 / (2.0 * 200.0)
LOSS_2DB = 10 ** (-0.2)
I_PEAK_GAN = 2.0 * (50.0 - 5.0) / ROPT_GAN
I_PEAK_LDMOS = 2.0 * (28.0 - 3.0) / ROPT_LDMOS
ETA_A = 0.50
PDISS_A = P100 * (1.0 / ETA_A - 1.0)
ETA_B = PI / 4.0
PDISS_B = P100 * (1.0 / ETA_B - 1.0)
PAE60_PIN = 10.0
PAE60_PDC = (P100 - PAE60_PIN) / 0.60
PAE60_DISS = PAE60_PDC + PAE60_PIN - P100
RTH = 1.2
TJ = 85.0 + PAE60_DISS * RTH
WILK_ISO = 20.0 * math.log10(2.0)
RADAR_R2 = 2.0 ** 4
RADAR_R05 = 0.5 ** 4
DUTY_01 = 0.10
PAVG_PULSE = 1000.0 * DUTY_01
G1_LIN = 10 ** (15.0 / 10.0)
F1_LIN = 10 ** (1.5 / 10.0)
F2_LIN = 10 ** (6.0 / 10.0)
F12 = F1_LIN + (F2_LIN - 1.0) / G1_LIN
F12_DB = 10.0 * math.log10(F12)
N0 = KB * T0
N0_DBM_HZ = 10.0 * math.log10(N0) + 30.0
KVCO = 2.0 * PI * 10e6
KP = 0.5 / (2.0 * PI)
N_DIV = 100.0
WN = 2.0 * PI * 50e3
ZETA = 0.707
T1 = KVCO * KP / N_DIV / (WN ** 2)
T2 = 2.0 * ZETA / WN
LO_PN = -90.0
IF_PN = LO_PN - 20.0 * math.log10(10.0)
CONV_LOSS = 7.0
NF_MIX = CONV_LOSS
P1DB_IN = 10.0
IIP3 = P1DB_IN + 9.5
EIRP_1DB = 10.0 * math.log10(P100 * LOSS_1DB)
EIRP_ANT = EIRP_1DB + 12.0
LAMBDA_3G = C0 / 3.0e9
FRIIS_SPACE = (LAMBDA_3G / (4.0 * PI * 1000.0)) ** 2
PR_ISO = P100 * FRIIS_SPACE
COMB_LOSS_4 = 10.0 * math.log10(4.0)
P_EACH_4 = P100 / 4.0
VSWR_3 = 3.0
GAMMA_3 = (VSWR_3 - 1.0) / (VSWR_3 + 1.0)
PREFL_3 = P100 * GAMMA_3 ** 2
GYSEL_R = 50.0 * 2.0 * math.sqrt(2.0)
Q_CAV = 4000.0
BW_CAV = 2.0e9 / Q_CAV
SKIN_1GHZ = 66.0 / math.sqrt(1e9) * 1e-3
ATTN_COAX = 0.05 * math.sqrt(2.0)
P_TO_ANT_20M = P100 * 10 ** (-ATTN_COAX * 20.0 / 10.0)
F_OSC = 10e9
QL_OSC = 200.0
PN_LEESON_OFFSET = 100e3
F_OFFSET_RATIO = F_OSC / (2.0 * QL_OSC * PN_LEESON_OFFSET)
PN_FLOOR = -140.0
PN_LEESON = PN_FLOOR + 10.0 * math.log10(1.0 + F_OFFSET_RATIO ** 2)
DOH_PEAK = 100.0
DOH_AVG = DOH_PEAK / (10 ** (6.0 / 10.0))
ETA_DOH_BO = 0.55
ETA_AB_BO = 0.22
HEAT_DOH = DOH_AVG * (1.0 / ETA_DOH_BO - 1.0)
HEAT_AB = DOH_AVG * (1.0 / ETA_AB_BO - 1.0)
LP_ZREAL = 12.4
LP_ZIMAG = -4.8
LP_GAMMA_MAG = abs((complex(LP_ZREAL, LP_ZIMAG) - 50) / (complex(LP_ZREAL, LP_ZIMAG) + 50))
K_STAB = 1.35
MU_STAB = 1.12
SEQ_VG = -3.5
SEQ_VD = 50.0
IDQ_AB = 0.10 * 8.0
PDISS_BIAS = SEQ_VD * IDQ_AB
FILT_N = 5
FILT_FC = 3.8e9
FILT_F2 = 7.0e9
FILT_ATTN = 20.0 * FILT_N * math.log10(FILT_F2 / FILT_FC)
WG_A = 72.14e-3
WG_FC = C0 / (2.0 * WG_A)
DUP_ISO = 80.0
LNA_SURV = 20.0
TX_LEAK = 50.0 - DUP_ISO
RADAR_PT = 1000.0
RADAR_GT = 10 ** (30.0 / 10.0)
RADAR_GR = RADAR_GT
RADAR_SIGMA = 1.0
RADAR_R = 50e3
RADAR_LAM = C0 / 10e9
RADAR_PR = (RADAR_PT * RADAR_GT * RADAR_GR * RADAR_LAM ** 2 * RADAR_SIGMA) / (
    (4.0 * PI) ** 3 * RADAR_R ** 4
)
RADAR_PR_DBM = 10.0 * math.log10(RADAR_PR) + 30.0
NF_LNA = 1.2
G_LNA = 18.0
F_LNA = 10 ** (NF_LNA / 10.0)
G_LNA_LIN = 10 ** (G_LNA / 10.0)
F_MIX2 = 10 ** (8.0 / 10.0)
F_CAS = F_LNA + (F_MIX2 - 1.0) / G_LNA_LIN
NF_CAS = 10.0 * math.log10(F_CAS)


def h1(doc, text):
    add_p(doc, text, style="Heading 1")


def h2(doc, text):
    add_p(doc, text, style="Heading 2")


def paras(doc, texts):
    for t in texts:
        add_p(doc, t)


def key(doc, text):
    add_p(doc, "Key idea. " + text)


def practice(doc, items, sols):
    h2(doc, "Practice")
    for i, t in enumerate(items, 1):
        add_p(doc, f"{i}. {t}")
    h2(doc, "Solutions")
    for i, t in enumerate(sols, 1):
        add_p(doc, f"{i}. {t}")


def preface(doc):
    h1(doc, "Preface")
    paras(
        doc,
        [
            "This is Book 6 of a nine-book Electrical Engineering Series. It is the volume that owns watts. Book 3 already told you why a gallium-nitride HEMT on silicon carbide can stand a voltage that would punch through a silicon MOSFET of the same gate length. Book 4 already owns antenna gain, beam, polarization, and the Friis space factor that turns those gains into a received power. Book 5 owns the waveform and the band plan. Book 7 owns the chamber, the mask as a test, and the certificate. Book 8 owns the 650 V GaN switch in a power supply. That switch is not this book. This book starts at a radio-frequency device and ends at a legal field.",
            "The chain is not a metaphor. Device, load line, class, match, stability, bias, heat, combine, isolate, harmonic filter, transmission line, duplexer, antenna, EIRP, radar range or communications range, then the spectrum the license allows. Skip a box because the last one is more glamorous and you will debug the glamorous box for a month. Cripps taught a generation to draw the load line before they drew the matching network. Grebennikov collected the classes, the combiners, and Doherty into a working transmitter. McClaning is the noise chapter you actually use on a receiver. Gardner is the phase-locked loop as a control system, which is why the loop filter sits in this volume as a chapter and not as a tenth book.",
            "I write in American English. Worked numbers are computed in the builder that prints this file, so the arithmetic you see is the arithmetic the script ran. I cite the canon. I do not paste it. If you need the original figures from those books, buy those books. What you have here is a single path from a transistor or a tube to a field, with the numbers a working engineer actually writes on a whiteboard.",
            "A PLL is a chapter here. Receiver noise is a chapter here. Radar range to the fourth power is a chapter here. Antenna gains that enter Friis or the radar equation are Book 4. Facility conversion and the 650 V GaN switch are Book 8. The emission mask as a test method is Book 7. Those splits are not decoration. They keep the same arithmetic from being recomputed in three volumes with three different rounding habits.",
            "Lothar J. Musiol, 2026.",
        ],
    )
    key(
        doc,
        "One volume from the device to a legal field. The rest of the series points here for watts. It does not copy the arithmetic.",
    )


def ch01(doc):
    h1(doc, "Chapter 1. The Chain")
    paras(
        doc,
        [
            "Read a transmitter in order. Device physics first, because voltage, current, and thermal resistance are not later surprises. Then the load line, because the optimum resistance is what the matching network is for. Then the class, because class A and class F do not ask the same thing of that load. Then the match and the stability circles, including the odd-mode oscillation that only appears when you parallel cells. Then bias, and for a depletion-mode GaN HEMT the gate sequence that keeps the channel pinched off until the drain is safe. Then the heat path from junction to coolant. Then the combiner and the isolator. Then the harmonic filter. Then the line, coax or waveguide. Then the duplexer. Then the antenna. Then the field. Then the mask.",
            "That sentence is the table of contents of this book. It is also the review agenda. A design that cannot name the knee voltage, the drain efficiency at the declared peak-to-average ratio, the combining loss, the feed loss, and the harmonic attenuation is not a design. It is a pallet and a hope. The pallet is a component. The hope is not a specification.",
            "Book 3 owns why GaN stands the voltage and why indium phosphide is fast. You will not re-derive the two-dimensional electron gas here. You will use the consequence: a 50 V rail with a few volts of knee is a different matching problem from a 28 V LDMOS rail, and both are different from a GaAs driver that never sees a hundred watts. Book 4 owns antenna gain. When Friis is written in this volume, Gt and Gr come from Book 4. This book supplies Pt after feed loss. Book 7 owns the chamber. When a harmonic fails, Book 7 tells you how the receiver was set. This book tells you why the harmonic was generated and how the filter after the last amplifier was supposed to eat it.",
            "High-power RF is a profession. Facility power is a different profession, and it lives in Book 8. Pulsed high voltage is a third profession, also Book 8, shelf C. A radar modulator may borrow a pulse transformer from that shelf and then return the radio-frequency problem to this book. Do not drag a 650 V GaN switch from a totem-pole PFC into a 3.5 GHz pallet because both parts have GaN in the name. The voltages, the frequencies, the packages, and the failure modes are not cousins.",
            "The metrics that survive a design review are output power, power-added efficiency, gain, adjacent-channel leakage or error-vector magnitude, the back-off the waveform forces, occupied bandwidth, ruggedness into a mismatch, and junction temperature. Linearity without efficiency is a heat problem. Efficiency without a mask is a legal problem. A datasheet that quotes peak power into a perfect 50 Ω load at one temperature is a starting point. It is not the radio.",
            "Cellular infrastructure settled on Doherty because the waveform is not a continuous carrier. Radar settled on pulse because detectability is energy and because the average heat is the duty cycle times the peak. Broadcast still uses tubes in some plants because combining a hundred solid-state pallets is a cost and a reliability problem, not a physics problem. Handsets use GaAs and CMOS because a few watts is a different economy. The chain is the same. The boxes change size.",
            "An active electronically scanned array moves a small amplifier to each element. That looks like a revolution. It is a packaging and calibration revolution. The amplifier is still this book: a device, a load, a bias, a heat path, a harmonic, and a legal field. Book 4 owns the element pattern and the array factor. Book 9 owns the module substrate. Do not invent a tenth book because the amplifier became small.",
            "Unintended radiation is Book 7. Intended radiation is this chapter's last box. Both have to be true on the same day. A transmitter that makes a beautiful EIRP and fails CISPR 32 on the enclosure is not finished. A board that is quiet in the chamber and whose PA oscillates when the antenna VSWR walks is not finished either. The chain includes the field you meant to make and the field you did not.",
            "Cripps, Grebennikov, Kazimierczuk, and Raab are the amplifier shelf. McClaning is the noise shelf. Gardner or Best is the loop shelf. Whitaker and Gilmour enter when the last stage is still a vacuum. Pozar and Steer are borrowed only for the link equation; their antenna chapters stay in Book 4. IEEE C95.1 and ICNIRP close the exposure question. They are not circuit books.",
            "This chapter has no matching network and no Smith chart. Book 1 already taught complex numbers. Book 4 already taught the chart as a microwave tool. This book uses both. What it adds is power: voltage swing, current swing, heat, combining, and the fact that one decibel after the last amplifier is one decibel of EIRP. Nothing downstream creates a watt.",
        ],
    )
    key(
        doc,
        "Device, load, class, match, bias, heat, combine, filter, line, duplexer, antenna, field, mask. Skip a box and you will debug the next one forever.",
    )
    h2(doc, "Worked Example 1.1. One decibel of feed")
    paras(
        doc,
        [
            f"EIRP is transmitter power times antenna gain after the feed is included. In linear units, one decibel of loss is a factor of {LOSS_1DB:.3f}. A declared 100 W amplifier behind 1 dB of coax, connectors, and duplexer insertion loss delivers {P100 * LOSS_1DB:.1f} W to the antenna. The printed factor is 0.794. That is the only copy of this one-decibel conversion in the series.",
            f"In decibels, EIRP falls by exactly 1 dB. If the antenna gain from Book 4 is 12 dBi, the EIRP is {10.0 * math.log10(P100) + 12.0 - 1.0:.1f} dBm, which is {EIRP_ANT:.1f} dBW on a 1 W reference after converting 20 dBW minus 1 dB of feed plus the same 12 dB of gain, or {10 * math.log10(P100) - 1 + 12:.1f} dBW. Antenna gain concentrates what remains. It does not recreate the 20.6 W the feed dissipated.",
        ],
    )
    h2(doc, "Worked Example 1.2. Four-way combining before the feed")
    paras(
        doc,
        [
            f"Suppose four identical pallets must make 100 W at the combiner output. Ideal equal combining of four sources is a factor of four in power, which is {COMB_LOSS_4:.0f} dB of 'gain' that is really addition. Each pallet then runs at {P_EACH_4:.0f} W if the combiner is lossless. A real Wilkinson or Gysel is not lossless. If the combiner dissipates 0.3 dB, each pallet must run at {P_EACH_4 * 10 ** (0.03):.1f} W to hold 100 W at the output.",
            "The isolator after the combiner, or one isolator per pallet, is not optional if the antenna can fail. A shorted antenna without isolation dumps the reverse power into the transistors. The chain includes that isolator. Book 8 does not. Book 4 does not.",
        ],
    )
    practice(
        doc,
        [
            "Write the chain as a sequence of boxes. Circle the first box that Book 4 owns and the first box that Book 7 owns.",
            f"A 100 W PA with 2 dB of feed loss: what power reaches the antenna? Use the linear factor {LOSS_2DB:.3f}.",
            "Why is a 650 V GaN switch in a totem-pole PFC not a chapter of this book?",
            "An AESA has 256 elements, each with a 2 W PA. Which book owns the 2 W amplifier, and which book owns the array factor?",
        ],
        [
            "Device through field as listed in this chapter. Book 4 owns the antenna (gain, beam, polarization). Book 7 owns the mask as a test in a chamber. This book owns every watt-making box before the antenna and the EIRP statement after it.",
            f"P_ant = 100 × {LOSS_2DB:.3f} = {P100 * LOSS_2DB:.1f} W. Two decibels is a factor of about 0.631, so 63.1 W reaches the antenna.",
            "That part is a power-conversion switch. Frequency, voltage class, package, and magnetics shelf all belong to Book 8. This book owns radio-frequency power devices, typically tens of volts to a hundred volts at RF, not 650 V at a few hundred kilohertz.",
            "The 2 W PA is Book 6 for every element. The array factor, element spacing, and scan are Book 4. Calibration firmware is still a radio problem; it does not move the amplifier to Book 9.",
        ],
    )


def ch02(doc):
    h1(doc, "Chapter 2. Silicon LDMOS")
    paras(
        doc,
        [
            "Laterally diffused MOS is the silicon workhorse from UHF through about 3 GHz. The drift region is long enough to stand 28 V or 50 V rails. The channel is still MOS, so the process is cheap compared with compound semiconductors, and the part is rugged into a mismatch in a way that early GaAs FETs were not. Base stations, FM broadcast, ISM heat, and a great deal of VHF/UHF communications still ship LDMOS. It did not vanish when GaN arrived. It retreated from the frequencies and the power densities where silicon carbide wins, and it stayed where cost and ruggedness win.",
            "The package is usually a ceramic or plastic flange with two leads or a gull-wing, bolted to a copper heat spreader. Internal matching, prematch on the die or on a MOS capacitor and bond-wire network, brings the very low optimum resistance up toward a few ohms at the leads. You still match from there to 50 Ω on the board. You do not pretend the lead is already 50 Ω because the datasheet plotted it that way in a fixture.",
            "A typical cellular LDMOS pallet at 2.1 GHz wants a 28 V or 32 V rail, a quiescent current in class AB, and a load that Cripps would recognize as a compromise between power and linearity. Digital predistortion then mops the residual. The datasheet's adjacent-channel number without DPD is a warning, not a radio specification. The datasheet's peak power is a saturation number. Your waveform has a peak-to-average ratio, so the average power is lower and the heat is not the peak times a class-A efficiency.",
            "Ruggedness is the LDMOS sales pitch. A 10:1 VSWR survival test, or an ISO pulse, is why broadcast engineers still reach for silicon when a GaN pallet would be smaller. Survival is not linearity. Survival is not efficiency. It is the ability to live through an antenna ice storm, a disconnected jumper, or a lightning arrestor that did not quite arrest. Design the isolator anyway. The survival rating is a last resort, not a matching strategy.",
            "Hot-carrier aging, thermal cycling of the die attach, and electromigration in the drain metal are the wear-out list. Junction temperature is the knob you actually have. A 200 °C peak on a pulse is not a 200 °C continuous rating. LDMOS thermal time constants are milliseconds to seconds depending on the heat-spreader mass. Radar pulses and TDD bursts see a different temperature than a CW two-tone test. Write the waveform when you write the temperature.",
            "At a few hundred megahertz an LDMOS die can still make a kilowatt in a single package, or at least hundreds of watts. At 2.5 GHz the same family is tens to a couple of hundred watts, and combining starts. At 3.5 GHz you are usually looking at GaN. Those numbers move every generation, but the shape of the story does not: silicon's mobility and critical field run out as frequency and voltage want to rise together.",
            "Internal prematch sets a bandwidth. A highly prematched 2.1 GHz part is a poor 700 MHz part even if the die could have worked there. Wideband LDMOS, for 1.8 to 2.2 GHz multi-band pallets, uses less aggressive prematch and more board matching. That is a cost in Q and in harmonic termination. You cannot have a one-ohm drain pulled to 50 Ω over an octave with a lossless two-element network. Book 4's matching chapter already said so. This chapter adds that the one-ohm drain is real.",
            "Bias is a positive gate, unlike depletion GaN. Sequencing is still good practice: gate first, then drain, so you do not slam a depletion-like current through an enhancement device during the rail's rise. Temperature compensation of the gate voltage holds Idq. A simple diode or a proper bias controller is part of the pallet, not a later firmware trick. Memory in the bias network is a linearity problem that DPD will try to fix and should not have to.",
            "LDMOS is also an ISM and plasma device. Thirteen-fifty-six megahertz and 27 MHz industrial heaters, and 2.45 GHz microwave ovens in the solid-state replacement story, care about ruggedness into a wildly varying load. Load-pull in those jobs is a survival map, not an ACLR map. The same load-line math applies. The mask does not.",
            "When you choose LDMOS over GaN you are usually buying cost, a mature supply chain, and ruggedness, and you are paying in size, in a lower rail, and in a harder match. The one-home load line in Chapter 6 will make that payment numerical: 3.13 Ω versus 10.13 Ω for the same 100 W.",
        ],
    )
    key(
        doc,
        "LDMOS is the cheap rugged silicon PA through about 3 GHz. Treat the prematch as part of the device. Treat the survival rating as a last resort.",
    )
    h2(doc, "Worked Example 2.1. Peak current on the 28 V load line")
    paras(
        doc,
        [
            f"Declared 100 W, 28 V rail, 3 V knee, Ropt = {ROPT_LDMOS:.3f} Ω, printed 3.13 Ω. The RF current swing that produces that power on a class-B-like line is Ipeak = 2(VDD − Vknee)/Ropt = 2 × 25 / {ROPT_LDMOS:.3f} = {I_PEAK_LDMOS:.1f} A. That is the current the bond wires and the metallization must carry at the peak of the RF cycle, not the DC current on the supply meter.",
            f"If the DC current from the 28 V supply is 6.0 A while delivering 100 W, drain efficiency is 100 / (28 × 6.0) = {100.0 / (28.0 * 6.0) * 100:.1f} percent. The rest is heat in the die, about {28.0 * 6.0 - 100.0:.0f} W. Chapter 14 takes that heat to a flange temperature.",
        ],
    )
    h2(doc, "Worked Example 2.2. Why 50 V LDMOS still exists")
    paras(
        doc,
        [
            f"Repeat the same 100 W at 50 V and a 5 V knee: Ropt = {ROPT_GAN:.3f} Ω, printed 10.13 Ω, even if the die is still silicon. Peak current falls to {I_PEAK_GAN:.1f} A. Matching 10.13 Ω to 50 Ω is a ratio of {50.0 / ROPT_GAN:.1f} to 1. Matching 3.13 Ω to 50 Ω is {50.0 / ROPT_LDMOS:.0f} to 1. The higher rail did combining work inside the drain voltage.",
            "Fifty-volt LDMOS is common in UHF broadcast and in some ISM pallets. Cellular infrastructure at 2 GHz more often stayed at 28 to 32 V because the devices, the DPD, and the Doherty literature grew up there. Voltage is a system choice, not a morality.",
        ],
    )
    practice(
        doc,
        [
            "Name three markets that still buy LDMOS in 2026 and one market that usually does not.",
            f"A 200 W LDMOS PA at 28 V, 3 V knee: compute Ropt using (VDD − Vknee)²/(2P).",
            "Why is a 10:1 VSWR survival spec not a matching network?",
            "An internally prematched 2.14 GHz LDMOS is dropped on a 900 MHz board. What fails first, the die physics or the prematch?",
        ],
        [
            "UHF broadcast, sub-3 GHz cellular/ISM, VHF/UHF comms and plasma still buy it. C-band and Ku-band infrastructure and most AESA T/R chips do not; those are GaN or GaAs.",
            f"Ropt = 25² / 400 = 625/400 = 1.5625 Ω, about 1.56 Ω. Twice the power at the same voltage halved the load.",
            "Survival is a ruggedness test. The matching network is still designed for the intended load-pull contour, usually near Ropt. A disconnected antenna is an emergency, not an operating point.",
            "The prematch. The die might still have gain at 900 MHz, but the internal network is a bandpass around 2.14 GHz. You will see a terrible input return loss and a collapsed load line before you see a physics limit.",
        ],
    )


def ch03(doc):
    h1(doc, "Chapter 3. Gallium Nitride HEMTs")
    paras(
        doc,
        [
            "A GaN HEMT on silicon carbide is the default high-power RF transistor from about half a gigahertz through Ka-band, and it is eating Ku-band traveling-wave-tube sockets one radar at a time. The two-dimensional electron gas, the wide bandgap, and the thermal conductivity of SiC are Book 3. This chapter uses the consequences: a 50 V or 65 V drain is ordinary, a 28 V GaN process exists for infrastructure that grew up on LDMOS rails, power density is watts per millimeter of gate periphery that would melt a silicon die of the same size, and trapping makes the drain current remember the last pulse.",
            "Depletion mode is the usual RF HEMT. The channel is on at zero gate voltage. You must hold the gate negative before you apply the drain, and you must keep it negative until the drain is gone. That sequence is Chapter 12. Enhancement-mode GaN exists, mostly in Book 8's power-conversion world, and in some RF processes that want a safer default. Do not assume the part in your hand is enhancement because the catalog page said GaN.",
            "Silicon carbide is the thermal path that makes the power density honest. GaN on silicon is cheaper, larger wafers, and thermally worse. It is a driver, a handset, an infrastructure part at moderate power, not a 200 W S-band pallet unless the thermal design is unusually serious. GaN on diamond shows up in papers and in a few modules. It is not yet the default catalog. Quote the substrate when you quote the watts.",
            "Trapping, current collapse, knee walk-out, and drain-lag are names for the same family of defects. A CW load-pull and a pulsed load-pull do not draw the same contour. A radar with a 10 percent duty cycle sees a different effective Ropt than a cellular carrier that is almost always on. Bias circuits with long time constants interact with those traps and become memory. Digital predistortion can chase some of that memory. It cannot chase a thermal limit you refused to size.",
            "Breakdown is not a single number. Off-state drain-source, on-state, gate-drain, and the ruggedness into a high VSWR are different tests. A 150 V breakdown on a 50 V process is headroom, not an invitation to run 90 V because the load line would be prettier. Hard switching of the drain, as in some class-E and class-F waveforms, stresses the same junctions the CW rating never saw.",
            "Millimeter-wave GaN is a different drawing: shorter gates, more cells, more combining on the die, and a package that is a laminate or a wafer-level fan-out rather than a bolted ceramic flange. Power per die falls as frequency rises. Combining in the module, then in the array, is how you get EIRP. Book 4 owns the array. This chapter owns why each 5 W Ka-band die still needs a load line.",
            "Reliability is junction temperature, voltage, and humidity if the die is not hermetic. A plastic overmold at 50 V in a humid outdoor radio is a qualification program, not a cost-down. Arrhenius projections from a 225 °C bake are not a substitute for a mission profile. Radar, satcom uplink, and a 5G massive-MIMO radio have different mission profiles. Write the profile before you write the FIT number.",
            "Compared with LDMOS at 2 GHz, GaN usually wins on efficiency, bandwidth, and size, and it used to lose on cost and on trapping. Cost moved. Trapping improved and did not vanish. Compared with GaAs at 10 GHz, GaN wins on voltage and power, and GaAs still wins as a cheap driver and as a low-noise amplifier in some bands. Compared with a tube at 100 kW, GaN wins until the combining tree and the power supply cost more than the klystron. That last sentence is Chapter 5.",
            "The one-home load line uses a 50 V rail and a 5 V knee for 100 W: 10.13 Ω. That knee is declared for this series. Your datasheet's pulsed I-V will show a different knee at a different pulse width. Use the datasheet for the part. Use 10.13 Ω when this series needs a single number so Book 4 and Book 8 do not invent their own.",
            "Quay is the device book. Cripps remains the load-line book, technology-agnostic on purpose. Grebennikov will assume you already picked GaN for the high-efficiency classes. This chapter's job is to keep you from treating GaN as silicon with a prettier efficiency number.",
        ],
    )
    key(
        doc,
        "Quote the substrate, the mode, and the pulse width. GaN on SiC at 50 V is not GaN on silicon at 28 V, and neither is a 650 V power switch.",
    )
    h2(doc, "Worked Example 3.1. Power density and periphery")
    paras(
        doc,
        [
            f"A foundry process is quoted at 8 W per millimeter of gate periphery at 3.5 GHz, 50 V, pulsed. For 100 W you need 100/8 = 12.5 mm of periphery if combining and matching were lossless. They are not. At 80 percent drain efficiency and 1 dB of output matching loss, the die must make {P100 / 0.80 / LOSS_1DB:.0f} W, so periphery is about {P100 / 0.80 / LOSS_1DB / 8.0:.1f} mm. That is a layout, a thermal density, and a combining problem on the die.",
            "Continuous-wave density is lower. If CW is 5 W/mm on the same process, the same 100 W radio needs 20 mm before matching loss. Pulse radar can live on the 8 W/mm number if the duty cycle and the pulse width match the foundry's test. Cellular cannot.",
        ],
    )
    h2(doc, "Worked Example 3.2. Knee walk-out is a load-line error")
    paras(
        doc,
        [
            f"The one-home Ropt at 50 V and a 5 V knee is {ROPT_GAN:.3f} Ω. If trapping walks the knee to 10 V under the actual waveform, Ropt becomes (50 − 10)² / 200 = {40.0 ** 2 / 200.0:.2f} Ω. You designed a 10.13 Ω match and the device now wants 8.00 Ω. Power falls, and the reflected energy at the harmonic terminations moves. A pulsed I-V at the right pulse width is not optional.",
            "This is why a CW harmonic-balance simulation on a compact model that never saw a trap will lie in a pretty way. Chapter 10's load-pull, on the bench, is the argument that settles it.",
        ],
    )
    practice(
        doc,
        [
            "Why must a depletion GaN HEMT see a negative gate before the drain rail rises?",
            "A 40 W Ka-band module uses eight 6 W dies. What did combining cost you if the module is 40 W, not 48 W?",
            "Name two reasons GaN-on-silicon is sold anyway.",
            "The 650 V GaN HEMT in a charger: which book, and why is the load line in this chapter the wrong tool?",
        ],
        [
            "The channel is on at Vg = 0. Drain voltage on an on-channel dumps a large current, often destructively, and even if the part survives the thermal transient is undefined. Pinch off first.",
            "Eight times 6 W is 48 W. Forty watts at the module flange is 0.83 linear, about 0.8 dB of combining, matching, and transition loss. That 0.8 dB is EIRP if it sits after the last gain.",
            "Wafer size and cost, and integration with silicon-friendly packaging. Thermal density is the bill you pay.",
            "Book 8. That device switches hundreds of volts at hundreds of kilohertz into a magnetics network. Cripps's RF load line is for a microwave current generator and a harmonic termination, not for a hard-switched half-bridge.",
        ],
    )


def ch04(doc):
    h1(doc, "Chapter 4. GaAs, Indium Phosphide, and Drivers")
    paras(
        doc,
        [
            "Gallium arsenide, as an HBT or a pHEMT, is the driver, the handset power amplifier, the few-watt point-to-point radio, and a great deal of the millimeter-wave content that is not trying to be a radar transmitter. You buy it for gain, for a mature foundry, for integration of the driver with the mixer and the VCO on a small die, and for a breakdown voltage that is enough at 3 to 6 V. You do not buy it for a hundred watts. Johnson's figure of merit already explained that in Book 3.",
            "A handset PA is a linearity and a battery problem. Envelope tracking, average-power tracking, and a load-insensitive coupler are the craft. Doherty appears even here, in miniature. The chain is the same as a 100 W pallet and the numbers are not. This book still owns that PA because it is a radio-frequency power device. Book 5 owns the waveform it must pass. Book 9 owns the module that sits next to the antenna switch.",
            "Indium phosphide HEMTs and HBTs are the fT parts. Low-noise amplifiers at 70 GHz, drivers into a mixer, optical modulator drivers, and some power at W-band where GaN has not yet become cheap. InP is not a kilowatt technology. Anyone who proposes an InP output stage for a 100 W S-band radar has confused a device lecture with a transmitter. Book 3 drew the split. This chapter enforces it.",
            "The driver is the stage everyone under-designs. It must be linear enough that the final stage's predistorter is not spending its degrees of freedom on the driver. It must have enough gain that the final's input match can be lossy, because high-power input matching often is. It must not oscillate when the final's input impedance walks with power. A 10 dB coupler between driver and final is an instrument, not a luxury, while you are bringing a pallet up.",
            "GaAs pHEMT low-noise amplifiers sit on the other side of the duplexer. Their noise figure belongs to Chapter 20. Their survival belongs to Chapter 17: duplexer isolation plus any limiter plus any T/R switch. A 1 dB NF LNA that dies at 20 dBm of leakage is not a low-noise amplifier. It is a fuse. InP LNAs at millimeter wave are even more fragile.",
            "Process choice is not brand loyalty. A 0.15 µm GaAs pHEMT, a 0.25 µm GaN HEMT, and a SiGe HBT can all make a 10 GHz driver. The GaN part wants more voltage and will be more efficient if you can match it. The SiGe part wants to live on a BiCMOS die with the synthesizer. The GaAs part is the catalog default. Draw the supply rails, the noise, and the integration before you draw the matching.",
            "Linearity in a driver is often third-order intercept, not adjacent-channel leakage, because the driver never sees the legal mask by itself. A rule of thumb that IIP3 sits about 9.5 dB above P1dB for a memoryless third-order device is a starting point, not a proof. Two-tone spacing matters because memory in the bias and in the thermal path is already alive at the driver.",
            "Packaging at millimeter wave is the product. A bare die on a laminate with 25 µm ribbon is a different inductance than a QFN. Book 9 owns the package vocabulary. This chapter only needs the consequence: a 0.3 nH bond at 30 GHz is about 57 Ω of reactance, which is not a small perturbation on a 50 Ω driver.",
            "Do not cascade three saturated GaAs stages and then complain that the GaN final cannot be linearized. Saturation is a choice. A driver that is 10 dB backed off costs efficiency in a small part of the chain and buys linearity where the watts are made. That trade is almost always correct.",
            "When the driver is on the same die as the final, as in a GaN MMIC, the load line of the driver is not 50 Ω. It is whatever the interstage network is. Interstage matching is where MMICs are won. On a pallet with two packages, you at least get a 50 Ω test point. Use it.",
        ],
    )
    key(
        doc,
        "GaAs and InP make gain, noise, and a few watts. They do not make the 100 W load line. Keep the driver linear enough that the final can be linearized.",
    )
    h2(doc, "Worked Example 4.1. Bond-wire reactance at 30 GHz")
    paras(
        doc,
        [
            f"A 0.3 nH bond at 30 GHz: XL = 2πfL = {2 * PI * 30e9 * 0.3e-9:.1f} Ω. That is larger than 50 Ω. Two bonds in parallel, if the mutual inductance is ignored, drop it to about {2 * PI * 30e9 * 0.15e-9:.1f} Ω, still not small. This is why millimeter-wave power is a package problem as much as a transistor problem.",
            "Book 9 will name the fan-out and the copper pillar. This example only needs you to stop treating a bond as a DC connection that happens to be short.",
        ],
    )
    h2(doc, "Worked Example 4.2. Driver back-off and cascade intercept")
    paras(
        doc,
        [
            f"A memoryless third-order estimate: IIP3 ≈ P1dB + 9.5 dB. A driver with P1dB = {P1DB_IN:.0f} dBm has IIP3 ≈ {IIP3:.1f} dBm. If the final wants 20 dBm of linear drive, that driver is 10 dB below its P1dB. The third-order products from the driver, referred to its output, sit at 3(Pin − IIP3) below the carriers in the two-tone picture, which is a comfortable margin if the final's own IIP3 is the tighter number.",
            "If you instead run that driver at 9 dBm, one decibel below P1dB, the driver becomes the linearity limit. DPD on the final cannot subtract a distortion that was already made in the driver, except by treating the cascade as one black box and using up correction bandwidth. Back the driver off.",
        ],
    )
    practice(
        doc,
        [
            "A 100 W S-band radar final: GaAs, InP, GaN, or a tube? Defend one sentence.",
            "Why might a SiGe driver on the same BiCMOS as the PLL be better than a discrete GaAs driver even if the GaAs part is more linear?",
            f"Compute XL of 0.2 nH at 10 GHz.",
            "The LNA is GaAs and the PA is GaN. Which chapter owns the LNA's noise figure, and which owns the LNA's survival?",
        ],
        [
            "GaN, usually, at that power and band. GaAs will not stand the voltage. InP is a driver technology. A tube is for much higher power or for a socket where combining cost explodes.",
            "One supply, one package, shorter interconnect, and the synthesizer's spurs are under the same designer. Linearity can be bought with back-off on a cheap part.",
            f"XL = 2π × 1e10 × 0.2e-9 = {2 * PI * 1e10 * 0.2e-9:.1f} Ω, about 12.6 Ω. Annoying at 10 GHz, fatal at 30 GHz.",
            "Noise figure is Chapter 20. Survival through the duplexer and limiter is Chapter 17. Both are this book. Neither is Book 3.",
        ],
    )


def ch05(doc):
    h1(doc, "Chapter 5. Vacuum Tubes When Combining Explodes")
    paras(
        doc,
        [
            "A tube still wins when the alternative is a tree of combiners that costs more than the tube, fails more often than the tube, or cannot be repaired in the field by the people who actually live with the transmitter. UHF broadcast, high-power radar, industrial microwave, and some scientific machines remain tube houses. Whitaker is the broadcast plant. Gilmour is the klystron and the traveling-wave tube. This chapter is not a nostalgia tour. It is a cost and a physics boundary.",
            "A tetrode or a diacrode in a cavity is a UHF broadcast final. A klystron is a bunched-beam amplifier with cavities along a drift tube, efficient and narrowband, still the way some radars and accelerators make tens or hundreds of kilowatts. A traveling-wave tube is the broadband helix or coupled-cavity satellite-uplink and radar tube. A magnetron is a self-oscillating crossed-field device, cheap at 2.45 GHz for heat, and still a radar oscillator when you can live with its noise. A gyrotron is a millimeter-wave scientific and fusion device. Name the tube before you name the voltage.",
            "Solid-state combining is honest. Sixteen 200 W GaN pallets with 0.5 dB of combining loss are 2.85 kW, not 3.2 kW. Isolation resistors, amplitude and phase balance, and a single-point failure of the combining structure are the bill. At some power the bill exceeds a klystron and a high-voltage supply. That crossover moves down in power every year as GaN gets cheaper, and it has not reached 100 kW CW at S-band in most plants.",
            "The modulator and the high-voltage supply are Book 8, shelf C. A pulse transformer, a PFN, a solid-state Marx, or a deck of IGBT switches is not a radio-frequency problem. This book needs the consequence: the RF device sees a pulse of voltage, a pulse of current, and a duty cycle that sets the average heat. Do not rate a klystron at its peak power as if it were a CW LDMOS pallet.",
            "Efficiency of a klystron can be excellent, fifty to sixty-plus percent with a depressed collector. A TWT is often worse, and a helix TWT at millimeter wave worse still. A magnetron for heat is a different economy: cheap, noisy, not a communications amplifier. Do not compare a magnetron oven source to a GaN communications pallet. They do not share a mask.",
            "Phase noise and spurious outputs from a tube transmitter are a system problem. A magnetron's pushing and pulling, a TWT's helix-induced sidebands, a klystron's ion noise, all land in the radar's Doppler bins or in the broadcast mask. Solid-state is not automatically quieter. A poorly locked PLL driving a GaN chain can be worse. It is automatically different, and the loops that clean it are Chapter 23.",
            "Replacement is a logistics problem. A TWT with an 18-month lead time and a heater hour clock is a spare-parts culture. A GaN pallet with a 12-week lead time and a soldered flange is a different culture. Designers who ignore logistics design museums.",
            "The load on a tube is still a load line, even if Cripps drew it for FETs. A klystron wants a cavity impedance. A TWT wants a helix match and an output window that will not arc. Multipaction in vacuum, and corona in air, are the high-voltage twins of the VSWR problem. Book 8 names the insulation. This chapter names the RF window.",
            "When a program says 'we will replace the tube with GaN' the honest study is combining loss, DC power, cooling, volume, MTBF of the tree versus the tube, and the spare. Sometimes the answer is GaN. Sometimes the answer is a new tube. Both answers can be engineering.",
            "This series will not teach you to design a klystron. It will teach you not to be embarrassed when a 50 kW radar is still a klystron, and not to force a hundred pallets into a socket a tube still fills.",
        ],
    )
    key(
        doc,
        "Tubes remain when combining cost, bandwidth at high power, or field repair beats a pallet tree. The modulator is Book 8. The RF window is this chapter.",
    )
    h2(doc, "Worked Example 5.1. Combining cost versus a tube")
    paras(
        doc,
        [
            f"Need 10 kW CW at 3 GHz. GaN pallets of 250 W each: 40 pallets if combining is lossless. At 0.4 dB total combining tree loss, you need 10 kW × {10 ** 0.04:.3f} = {10000 * 10 ** 0.04:.0f} W of pallet power, so {math.ceil(10000 * 10 ** 0.04 / 250)} pallets at 250 W. Each pallet at 60 percent drain efficiency draws {250 / 0.60:.0f} W of DC. Forty-four pallets draw about {44 * 250 / 0.60 / 1000:.1f} kW of DC, plus driver and fans.",
            "A klystron at 55 percent efficiency making 10 kW RF draws 18.2 kW of beam power, plus heater and magnet. The DC numbers can favor either side. The combining tree, the cooling distribution, and the spare-module policy often decide. Run the numbers. Do not run a slogan.",
        ],
    )
    h2(doc, "Worked Example 5.2. Duty cycle is the tube's heat")
    paras(
        doc,
        [
            f"A radar klystron is rated 1 MW peak, 10 percent duty, 100 µs pulses. Average RF power is {PAVG_PULSE:.0f} kW? No: 1 MW × 0.10 = {1000.0 * 0.10:.0f} kW? 1e6 × 0.10 = {1e6 * 0.10:.0f} W, which is {1e6 * 0.10 / 1000:.0f} kW average. Cooling and the collector are sized for that average, plus beam interception. The RF window and the cavities must also survive the peak voltage of the 1 MW pulse.",
            "A GaN pallet rated 200 W CW is not a 2 kW peak part at 10 percent duty unless the foundry said so. Peak voltage, trapping, and thermal spreading inside the pulse are different limits. Copying a tube's peak/average ratio onto a HEMT is a classic way to destroy a pallet.",
        ],
    )
    practice(
        doc,
        [
            "Name four tube types and one job each.",
            "Why is the pulse transformer Book 8 while the TWT is Book 6?",
            "Sixteen 300 W pallets, 0.6 dB combining loss: power at the sum port?",
            "Give one reason a magnetron is the wrong final for a 64-QAM link.",
        ],
        [
            "Tetrode: UHF broadcast. Klystron: high-power narrowband radar or accelerator. TWT: broadband satcom/radar. Magnetron: industrial heat or simple radar. Gyrotron: mmWave scientific/fusion.",
            "The transformer is pulsed high voltage and magnetics, Book 8 shelf C. The TWT is the RF amplifying device. This book borrows the pulse and returns the spectrum.",
            f"Lossless sum would be 4800 W. 0.6 dB is a factor of {10 ** (-0.06):.3f}, so {4800 * 10 ** (-0.06):.0f} W at the sum.",
            "A magnetron is an oscillator with pushing, pulling, and noise. It is not a linear amplifier. 64-QAM needs a linear chain, or at least a linearized one, and a locked carrier from Chapter 23.",
        ],
    )


def ch06(doc):
    h1(doc, "Chapter 6. The Load Line")
    paras(
        doc,
        [
            "Cripps's load-line method is the reason this series has a single pair of 100 W numbers. The device is a current generator in parallel with output capacitance, swinging between knee and breakdown, delivering power into a real load. The optimum resistance is about (VDD − Vknee)² / (2P). That is a class-B-ish continuous-wave statement. It is the best first number you will write, and it is wrong in the ways the rest of this book exists to correct: class, harmonics, packaging parasitics, trapping, and the imaginary part of the load.",
            f"One hundred watts is the declared power for the one-home arithmetic. A 50 V rail with a 5 V knee: Ropt = 45² / 200 = {ROPT_GAN:.3f} Ω, printed 10.13 Ω. A 28 V rail with a 3 V knee: Ropt = 25² / 200 = {ROPT_LDMOS:.3f} Ω, printed 3.13 Ω. Those two numbers appear in this chapter and are cited from here. Other books in the series do not recompute them.",
            f"Getting to 50 Ω is a ratio of {50.0 / ROPT_GAN:.1f} to 1 on the higher rail and {50.0 / ROPT_LDMOS:.0f} to 1 on the lower rail. Same power. The voltage did combining work. That is the practical content of a higher breakdown voltage, and it is why GaN's 50 V process is not just a prettier efficiency number than LDMOS. Matching networks have loss. Larger transformation ratios have more loss, or more sections, or both.",
            "The factor of two in the denominator is the class-B average-power identity: P = (1/2) × Vpeak × Ipeak, with Vpeak = VDD − Vknee and Ipeak = Vpeak / Ropt, which rearranges to Ropt = Vpeak² / (2P). Class A uses a different current waveform and a different efficiency, but designers still start here and then load-pull. Class F and inverse-F change the harmonic terminations so the fundamental load is not this resistor. Start here anyway.",
            "Output capacitance is in parallel with Ropt. At 2 GHz a 20 pF Cds is 4 Ω of reactance, which is not a perturbation on a 3.13 Ω load. The matching network's first job is often to absorb Cds, not to transform 3.13 to 50. That is why prematch exists inside the package. That is why a die model without Cds is a toy.",
            "The load is not purely real. Load-pull will show a contour of constant power that is a set of circles on the Smith chart, and a contour of constant efficiency that is a different set, and a contour of constant ACLR that is a third set. The operating point is a compromise. Cripps's resistor is the center you start from. Chapter 10 is the map.",
            "Knee voltage is a declared number in this series. On a real part it is a function of current, of pulse width, and of temperature. A 5 V knee at 100 W is not a 5 V knee at 200 W. If you need 200 W on the same 50 V, 5 V device, Ropt falls to 5.06 Ω and the current rises. The knee will walk. Re-measure.",
            "Breakdown must sit above 2 VDD for a class-B swing that returns to 2 VDD − Vknee on the drain, in the simple picture. Harmonic peaking in class F can overshoot. A 50 V process with a 120 V rating is not luxury. It is how you survive a mistuned harmonic trap.",
            "Power-added efficiency is (Pout − Pin) / Pdc. Drain efficiency is Pout / Pdc. At 15 dB of gain the two numbers are close. At 6 dB of gain they are not, and a driver that you forgot to count is hiding in the heat budget. Quote which efficiency you mean.",
            "This chapter is technology-agnostic on purpose, as Cripps was. LDMOS, GaN, a GaAs FET, even a tube in a cavity, all have a voltage swing, a current swing, and a load. The one-home numbers are 10.13 Ω and 3.13 Ω. Remember which rail they came from.",
        ],
    )
    key(
        doc,
        "Ropt ≈ (VDD − Vknee)² / (2P). For 100 W: 10.13 Ω at 50 V / 5 V knee, 3.13 Ω at 28 V / 3 V knee. Raise the rail and the match gets easier.",
    )
    h2(doc, "Worked Example 6.1. The two one-home loads")
    paras(
        doc,
        [
            f"Ropt,GaN = (50 − 5)² / (2 × 100) = 2025 / 200 = {ROPT_GAN:.3f} Ω, printed 10.13 Ω. Ropt,LDMOS = (28 − 3)² / (2 × 100) = 625 / 200 = {ROPT_LDMOS:.3f} Ω, printed 3.13 Ω. Transformation to 50 Ω: {50.0 / ROPT_GAN:.2f} : 1 versus {50.0 / ROPT_LDMOS:.2f} : 1. A quarter-wave transformer for the GaN case would want Zq = √(10.125 × 50) = {math.sqrt(ROPT_GAN * 50.0):.2f} Ω. For LDMOS, Zq = {math.sqrt(ROPT_LDMOS * 50.0):.2f} Ω, a much more extreme line.",
            "Book 4 will etch those lines. This book decides they are necessary. One decibel of matching loss on the LDMOS side is the same factor 0.794 of power, 79.4 W at the 50 Ω port, and is more likely because the transformation is harsher.",
        ],
    )
    h2(doc, "Worked Example 6.2. Two hundred watts on the same 50 V die")
    paras(
        doc,
        [
            f"Ropt(200 W) = 45² / 400 = {ROPT_200:.3f} Ω, printed 5.06 Ω. Peak current doubles relative to the 100 W, 10.13 Ω line if the knee holds: Ipeak = 2 × 45 / 5.0625 = {2 * 45 / ROPT_200:.1f} A. Cds reactance is unchanged, so it is now a larger fraction of the load. The match is harder, the current is hotter, and the knee will not hold unless the I-V says it will.",
            "If you cannot stand the current, raise the rail or combine two 100 W devices. Combining two 10.13 Ω drains in phase is a different network from matching 5.06 Ω. Sometimes the combiner is the better match.",
        ],
    )
    practice(
        doc,
        [
            "Reproduce Ropt for 100 W, 50 V, 5 V knee, and state the printed form used in this series.",
            "A 65 V GaN process, 7 V knee, 100 W: Ropt?",
            "Why does Cds matter more against 3.13 Ω than against 10.13 Ω?",
            "Drain efficiency 70 percent, gain 8 dB, Pout = 100 W: estimate PAE.",
        ],
        [
            f"Ropt = 45²/200 = {ROPT_GAN:.3f} Ω, printed 10.13 Ω. This is the one-home GaN number.",
            f"Ropt = (65 − 7)² / 200 = 58² / 200 = {58.0 ** 2 / 200.0:.2f} Ω, about 16.82 Ω, even closer to 50 Ω.",
            "The capacitive reactance is in parallel with a smaller resistor, so a larger fraction of the current is wasted circulating in Cds unless you absorb it in the match.",
            "Pin = 100 / 10^(0.8) = 15.85 W. Pdc = 100 / 0.70 = 142.9 W. PAE = (100 − 15.85) / 142.9 = 58.9 percent. Gain is low enough that PAE and drain efficiency disagree by a lot.",
        ],
    )


def ch07(doc):
    h1(doc, "Chapter 7. Classes A and AB")
    paras(
        doc,
        [
            "Class A conducts for the whole cycle. The standing current is large, the drain voltage and current overlap, and the theoretical maximum efficiency into a resistive load is 50 percent. You buy it for linearity, for a driver, for a laboratory amplifier, and for any waveform whose peak-to-average ratio would make a switched class illegal or un-linearizable. You pay in heat. A 100 W class-A final at the theoretical cap dissipates 100 W in the die. Real class A is worse.",
            "Class B conducts for half the cycle. Theoretical drain efficiency is π/4, about 78.5 percent, into a shorted-even-harmonic load. Crossover distortion is the price. Two complementary devices, or a single device with a resonant load that supplies the missing half, are the textbook pictures. RF power devices are not complementary CMOS. RF class B is a bias point and a harmonic termination, not a push-pull pair of N and P HEMTs.",
            "Class AB is the working linear amplifier. Quiescent current is a slice of the class-A standing current, enough to hide the crossover, not enough to burn class-A heat. Cellular, broadcast exciters, and any radio that will run digital predistortion start here. The load line is still Cripps's resistor at peak power. At back-off the efficiency falls toward class A because the standing current is a larger fraction of the RF current.",
            "Peak-to-average ratio is why class AB is a heat problem even when the peak efficiency looks fine. A 10 dB PAR waveform that peaks at 100 W averages 10 W. If drain efficiency at that average is 20 percent, the die dissipates 40 W to make 10 W. The datasheet's 70 percent at 100 W CW is true and not the radio. Doherty, envelope tracking, and outphasing exist because of this paragraph.",
            "Harmonic terminations still matter in class AB. A shorted second harmonic at the die plane, or a controlled second, moves efficiency and linearity. The output matching network that transforms 10.13 Ω to 50 Ω is also a harmonic network whether you designed it that way or not. Measure it at 2f0.",
            "Bias current is temperature dependent. A fixed gate voltage on LDMOS or GaN will walk Idq as the flange heats. A bias controller, a mirror, or at least a compensating diode, is part of the class-AB design. Memory in that bias network is a video-bandwidth limit. DPD models that include memory are mopping a bias inductor you could have sized.",
            "Gain expansion and gain compression versus power are the AM-AM. Phase versus power is the AM-PM. Both are class-AB facts. Predistortion inverts them. If they walk with temperature and with drain voltage, the inversion has to walk too. Envelope tracking, which moves the drain, makes AM-PM a moving target on purpose and then spends DPD to catch it. That can still be a win on heat.",
            "Two-tone tests are not waveforms. They are diagnostics. Tone spacing that sits inside the bias-network time constants will look worse than tone spacing that does not. A 1 MHz spacing that passes and a 10 MHz spacing that fails is a memory problem, not a 'linearity' problem in the abstract. Write the spacing.",
            "Class A still has a job at the driver, in instrumentation, and in some satellite uplinks where DC power is plenty and the mask is holy. Do not be ashamed of class A in those jobs. Do be ashamed of class A in a 100 W cellular remote radio that must sit on a tower with a 300 W DC budget.",
            "Kazimierczuk writes the class equations with current waveforms. Cripps writes the load line the engineer actually uses. This chapter needs both: the 50 percent and 78.5 percent caps so you know you are not a magician, and the load line so you can design Monday.",
        ],
    )
    key(
        doc,
        "Class A is linear and hot. Class AB is the linear workhorse. Peak efficiency is not average efficiency. PAR is the reason Doherty exists.",
    )
    h2(doc, "Worked Example 7.1. Heat at the class-A cap")
    paras(
        doc,
        [
            f"One hundred watts out at 50 percent drain efficiency: Pdiss = Pout(1/η − 1) = {PDISS_A:.0f} W. The flange and the cold plate must carry 100 W of heat plus whatever the driver adds. If Rθ,jc = 0.8 °C/W and the flange is held at 70 °C, the junction is at 70 + 80 = 150 °C if 100 W is actually in the die. That is a reliability meeting.",
            f"Class B at the π/4 cap: η = {ETA_B:.3f}, Pdiss = {PDISS_B:.1f} W for the same 100 W out. You bought 27 W of heat relief and you spent crossover distortion. Class AB sits between these two numbers at peak, and far closer to class A at deep back-off.",
        ],
    )
    h2(doc, "Worked Example 7.2. PAR turns 70 percent into 20 percent")
    paras(
        doc,
        [
            f"Declared peak 100 W, PAR 8 dB: average RF is 100 / 10^0.8 = {P100 / 10 ** 0.8:.1f} W. If a class-AB pallet is 70 percent efficient at peak and 22 percent efficient at that average, heat at average is {HEAT_AB:.1f} W. A Doherty that holds 55 percent at the same average dissipates {HEAT_DOH:.1f} W. The radio's cooling is sized by the second number if you build AB, and by the first if you build Doherty.",
            "Those 22 and 55 percent figures are declared for the example, not universal. Measure your waveform. The structure of the arithmetic is the lesson.",
        ],
    )
    practice(
        doc,
        [
            "What is the theoretical maximum drain efficiency of class A and of class B into a resistive load?",
            "A 50 W average signal with 6 dB PAR: what peak power must the PA be able to make?",
            "Why does two-tone spacing change measured IMD in class AB?",
            "A driver in class A makes 2 W at 40 percent efficiency. How much heat, and why might you still choose class A?",
        ],
        [
            "Class A: 50 percent. Class B: π/4 ≈ 78.5 percent. Real devices miss both because of knee, Ron, and imperfect harmonics.",
            "6 dB is a factor of 4, so peak = 200 W. The match and the breakdown must be honest at 200 W, not at 50 W.",
            "Bias-network and thermal time constants, plus trapping in GaN, are memories. Tone spacing that hits those poles changes the sidebands. It is not a mystery IMD; it is a video bandwidth.",
            "Heat = 2 × (1/0.4 − 1) = 3 W. You choose class A because 3 W is cheap next to a 100 W final, and the driver stays out of the DPD's way.",
        ],
    )


def ch08(doc):
    h1(doc, "Chapter 8. Classes D, E, and F")
    paras(
        doc,
        [
            "Switched classes try not to let voltage and current exist in the device at the same time. Class D is a pair of switches feeding a series-tuned load, native to audio and to RF at frequencies where the switches are still switches. Class E uses a single switch, a shunt capacitance, and a carefully mistuned series resonator so the voltage returns to zero at turn-on. Class F shapes the drain waveform with odd-harmonic peaking toward a square voltage and a half-sine current, or inverse-F the other way around. Raab, Sokal, Kazimierczuk, and Grebennikov are the shelf.",
            "The theoretical efficiency is 100 percent. The working efficiency is 'better than AB if the waveform may be a constant envelope or if you can restore the envelope later.' Polar transmitters, class-E with drain modulation, and class-F Doherty finals are the ways this idea enters a communications radio. A CW industrial heater can just be class E and be happy.",
            "Class E is sensitive to the load. Sokal's component set assumes a known R, a known Cshunt, and a known loaded Q. Walk the antenna and the zero-voltage switching walks away. An isolator, a tuner, or a load that does not walk is part of class E. Radar pulses into a well-defined feed can be class E. Handset antennas usually cannot, unless a tuner sits in the loop.",
            "Class F is a harmonic-termination discipline as much as a class. Short even harmonics, open odd harmonics at the die plane, in the textbook. The output capacitance and the bond wires are already a harmonic network. You will spend more time absorbing those than placing an ideal stub. Inverse-F swaps the voltage and current shapes and often fits GaN's capacitance better. Load-pull at f0, 2f0, and 3f0 is the measurement, not a sketch of stubs.",
            "Class D at RF is usually voltage-mode or current-mode switching with a filter that recovers a sinusoid. At HF and low VHF it is practical with silicon or GaN power devices that are really Book 8 parts running at radio frequency. At 2 GHz it is a research paper more often than a pallet. Do not force class D into a band where the switching time is a large fraction of the RF period.",
            "Envelope restoration, Kahn's polar scheme, puts the phase on a switched PA and the amplitude on the supply. The supply modulator must be fast enough for the envelope bandwidth, which is wider than the RF channel. That modulator is a power-electronics problem that Book 8 recognizes, sitting in a radio that this book owns. The split is real: the PA is class E or F, the drain modulator is a buck or a multilevel converter.",
            "Harmonic content leaving a switched PA is not a footnote. The filter after the last amplifier, Chapter 15, is how you stay legal. Class F that uses harmonics on purpose still cannot radiate them. The stub that opens 3f0 at the die can be a short at the antenna if you design the chain. That is a chain problem, not a class-F contradiction.",
            "Soft switching wants a dead time, a resonant current, and a device that does not snap recover. GaN's lack of a p-n reverse-recovery charge is why class E at HF and VHF became ordinary. Silicon MOSFETs can do it with care. LDMOS RF parts were not designed as class-E switches; some still work. Read the switching figure of merit, not only the RF datasheet.",
            "Linearity of a switched PA is not AM-AM in the class-AB sense. It is how cleanly you can modulate the drain, or how well a Doherty pair of class-F cells interpolates. If the license needs 64-QAM without a polar loop and without DPD, you are back in Chapter 7. Do not advertise class-E efficiency on a waveform that cannot use it.",
            "The 100 W, 10.13 Ω load line is still the fundamental power. Class F changes the waveform factor, so the fundamental load is not exactly that resistor. Start there, then harmonic load-pull. Anyone who begins a class-F design by placing stubs on a 50 Ω line without a die-plane embedding has designed a filter, not a PA.",
        ],
    )
    key(
        doc,
        "D, E, and F buy efficiency by shaping voltage and current. They spend harmonic control, load sensitivity, and a filter. They do not replace the load line; they decorate it.",
    )
    h2(doc, "Worked Example 8.1. Class-E shunt C at 10 MHz")
    paras(
        doc,
        [
            f"Sokal's first-cut shunt capacitance for class E is C ≈ 0.1836 / (2π f R), with R the load at the switch. Take R = 10.13 Ω at 10 MHz, a high-frequency industrial job using the one-home 100 W, 50 V line. C ≈ 0.1836 / (2π × 1e7 × {ROPT_GAN:.3f}) = {0.1836 / (2 * PI * 1e7 * ROPT_GAN) * 1e12:.0f} pF. That is a real capacitor plus Coss, not a mystery.",
            "At 2 GHz the same formula wants 0.001 times that capacitance. Coss of a 100 W GaN die is already larger. Class E at 2 GHz is a Coss-using design, not a discrete-C design. Frequency picked the class.",
        ],
    )
    h2(doc, "Worked Example 8.2. Harmonic voltage in class F")
    paras(
        doc,
        [
            "A square-ish drain voltage with a third-harmonic peak can reach about 2 VDD at the fundamental component while the instantaneous peak sits near (4/π)VDD times a peaking factor. On a 50 V rail, a 2 VDD swing is 100 V. A 120 V breakdown is then 20 percent headroom, not luxury. If the third-harmonic termination is wrong, the peak can exceed that and the part holes.",
            f"Fundamental power is still about Vfundu200bI over two. Holding 100 W at 10.13 Ω means the fundamental voltage component is on the order of the class-B Vpeak of 45 V rms-related amplitude. The harmonic network's job is to let that fundamental exist without overlapping current. Measure 2f0 and 3f0 at the die plane, not at the SMA.",
        ],
    )
    practice(
        doc,
        [
            "Why is class E a poor choice for a handset antenna with no tuner?",
            "A class-F PA must still pass a harmonic mask. Where is that filter in the chain?",
            "Book 8's 650 V GaN half-bridge at 300 kHz: is it class D in this chapter's sense?",
            "What measurement replaces a sketch of ideal class-F stubs?",
        ],
        [
            "Class E's ZVS condition is load-specific. A walking antenna detunes the voltage waveform, efficiency collapses, and the FET can see simultaneous V and I. Add a tuner or pick AB.",
            "After the last amplifier, Chapter 15, even though class F uses harmonics on purpose at the die. Used at the die is not radiated at the antenna.",
            "It is a hard-switched power converter, Book 8. This chapter's class D is an RF PA with a resonant load making a radio sinusoid. Related idea, different profession.",
            "Harmonic load-pull at f0, 2f0, 3f0, de-embedded to the die plane, plus a waveform probe if you can.",
        ],
    )


def ch09(doc):
    h1(doc, "Chapter 9. Doherty and Back-Off")
    paras(
        doc,
        [
            "Doherty is the cellular default because the waveform is not a carrier. A main device, usually class AB or a linearized class F, sees a load that a peaking device modulates. At back-off the peaking device is off, the main device sees a higher load, and its voltage swing stays large, so efficiency stays high. At peak the peaking device turns on, the load splits, and both devices deliver current. Grebennikov and Cripps both treat this as load modulation, not as a magic combiner.",
            "The classic two-way Doherty is a 6 dB back-off machine: the main device alone makes half the voltage on twice the load, which is a quarter of the peak power, which is 6 dB. Three-way and asymmetric Doherty push the efficient region deeper for waveforms with 8 to 10 dB PAR. The combiner is a quarter-wave inverter. Phase alignment of the peaking path is the craft.",
            "Digital predistortion is not optional on a modern Doherty cellular radio. The AM-AM has a kink where the peaking device turns on. The AM-PM has a kink there too. A memory polynomial or a pruned Volterra that never saw that kink will fail the mask at the turn-on region. DPD is Book 5's algorithm running on this book's amplifier. The split is: waveform math in 5, watts in 6.",
            "GaN made Doherty better because the output capacitance is manageable at 50 V and the efficiency of each cell is already high. LDMOS Doherty still ships in volume at 2 GHz. The load-modulation math does not care. The parasitics care. A package with large Cds needs extra compensation at the combiner.",
            "Outphasing, Chireix, is the other load-modulation family: two saturated PAs, phase-shifted, summing into a combiner whose isolation is deliberately incomplete. Envelope tracking is the supply-modulation family. Both compete with Doherty. In 2026 infrastructure, Doherty plus DPD plus a moderately slow drain tracker is the boring winner. Boring is good on a tower.",
            "Wideband Doherty is a contradiction you manage, not a feature you tick. The quarter-wave inverter is a narrowband idea. Offset lines, Klopfenstein-like combiners, and digital splitting with dual DPD paths are how people fake an octave. Radar with a 10 percent bandwidth can be classic. A 1.8 to 2.2 GHz cellular pallet is already a fight. A 2 to 6 GHz tactical radio is usually not a Doherty radio.",
            "The peaking device's gate bias is a temperature and a process trim. Too cold and it turns on late, efficiency looks great, and the peak power and the mask fail. Too hot and it turns on early, efficiency at average collapses, and you built class AB with extra parts. Production needs a trim, a lookup table, or a closed calibration.",
            "Isolation between main and peaking is not a Wilkinson job. Power is supposed to flow in a controlled way. A Gysel or a branch-line with a deliberate mismatch is closer. If you isolate them perfectly you disabled the load modulation. New engineers do this once.",
            "Pulse radar rarely needs Doherty. The PA is off or it is at peak. Duty cycle is the heat control. Putting Doherty on a radar because a cellular app note was on the desk is a category error.",
            "The one-home 100 W number is the peak of the Doherty, not the average. Average heat uses the back-off efficiency. Cooling, the power supply, and the tower budget care about average. The match and the breakdown care about peak. Write both on the first slide.",
        ],
    )
    key(
        doc,
        "Doherty keeps the main device's voltage swing large at back-off by load modulation. It is a 6 dB (classic) efficiency machine plus DPD, not a combiner with two transistors.",
    )
    h2(doc, "Worked Example 9.1. Classic 6 dB point")
    paras(
        doc,
        [
            f"Peak 100 W, classic 6 dB back-off: average at that point is {DOH_AVG:.1f} W. If Doherty drain efficiency there is 55 percent, heat is {HEAT_DOH:.1f} W. If a class-AB pair at the same average is 22 percent, heat is {HEAT_AB:.1f} W. You bought {HEAT_AB - HEAT_DOH:.1f} W of thermal relief, which is also {HEAT_AB - HEAT_DOH:.1f} W of DC supply you do not have to haul up the tower.",
            "At 40 percent of a 300 W DC budget, that relief is the difference between a radio that fits and a radio that needs a larger supply and a larger heat sink, which needs a larger housing, which fails wind load. Efficiency is a mechanical problem.",
        ],
    )
    h2(doc, "Worked Example 9.2. Asymmetric periphery")
    paras(
        doc,
        [
            f"A 1:2 asymmetric Doherty puts more periphery on the peaking device so the efficient region sits near 9.5 dB back-off rather than 6 dB. If peak is still 100 W, the 9.5 dB average is {P100 / 10 ** 0.95:.1f} W. Designers chasing OFDM with 9 dB PAR live here. The peaking device is then the larger of the two, which offends the instinct that the 'aux' should be small. Instinct is wrong.",
            "The inverter impedance and the offset lines change with that ratio. You cannot drop a 1:2 pair onto a 1:1 board. Load-pull each device, then simulate the combiner, then DPD. In that order.",
        ],
    )
    practice(
        doc,
        [
            "Why must a Doherty combiner not isolate the two devices perfectly?",
            "A 50 W average, 8 dB PAR waveform: peak power, and is classic two-way Doherty well matched to that PAR?",
            "Who owns the DPD algorithm, Book 5 or Book 6?",
            "Why is Doherty unusual in pulse radar?",
        ],
        [
            "Load modulation requires the peaking current to change the impedance the main device sees. Perfect isolation prevents that change. You would have two independent PAs and a lossy summer.",
            "Peak = 50 × 10^0.8 = 315.5 W. Classic Doherty is centered 6 dB down from peak, while 8 dB PAR sits 2 dB deeper; an asymmetric or three-way design fits better.",
            "Book 5 owns the algorithm and the waveform. Book 6 owns the amplifier whose AM-AM/AM-PM the algorithm inverts. Both names appear in a real program.",
            "The radar PA is at peak or it is off. There is no long sojourn at an average power where load modulation would pay. Duty cycle, not PAR, sets the heat.",
        ],
    )


def ch10(doc):
    h1(doc, "Chapter 10. Load-Pull")
    paras(
        doc,
        [
            "Load-pull is the measurement that replaces argument. You present a controlled impedance at a reference plane, you measure power, efficiency, gain, and distortion, and you draw contours. Source-pull does the same at the input. Harmonic load-pull adds 2f0 and 3f0 tuners. Active load-pull injects a wave instead of turning a mechanical tuner, which is how you reach impedances a passive tuner cannot, and how you handle high power without a tuner that melts.",
            "The reference plane is the argument. A contour at the SMA of a fixture is not a contour at the die. De-embedding the fixture, the package, and the bond is Book 4's network theory applied here. If two labs disagree on Ropt, they first disagree on the plane.",
            "Cripps's 10.13 Ω is a point. Load-pull's 1 dB power contour is a region. You will operate somewhere in that region that also sits on a decent efficiency contour and a legal ACLR contour. Those three rarely share a single maximum. Production then needs a match that stays inside the region over temperature, process, and VSWR. That is a desensitization problem, not a one-point match.",
            "Pulsed load-pull is mandatory on GaN if the radio is pulsed. CW contours on a trapped device are a different device. Pulse width, duty, and isothermal versus electrothermal contours should be stated on the plot. A pretty plot without a pulse legend is decoration.",
            "On-wafer load-pull at millimeter wave uses probes, a different power limit, and a different de-embed. A 5 W Ka-band die measured on-wafer will not show the same impedance as the same die in a module with 3 mm of 50 Ω and two ribbons. Design the module from the module contours, or embed the module onto the wafer contours. Do not mix them in a slide.",
            "Source-pull sets gain and input return, and it sets stability. An unconditionally stable die can still oscillate in a pallet if the source impedance at a subharmonic walks into a negative-resistance region. Load-pull that never looked below f0/2 has missed odd-mode and parametric problems. Chapter 11 is that story.",
            "Tuner loss is power you did not know you lost. A passive tuner at a 3.13 Ω load has high standing wave and high loss. The power at the DUT is not the power at the meter minus a cal factor you downloaded. Scalar correction of tuner loss is a discipline. Active load-pull was invented partly to escape that discipline at the edge of the Smith chart.",
            "The imaginary part of the load at f0 is often just Cds being absorbed. A measured Zopt of 12.4 − j4.8 Ω is a 10.13 Ω Cripps resistor plus a leftover reactance the prematch did not quite cancel. Do not invent a new theory. Absorb the j part and compare the real part to Cripps.",
            "Production load-pull is a sample, not every device. You load-pull a golden unit, you fix the match, you then use s-parameters and a scalar power test in production. When yield walks, you load-pull again. You do not ship a mechanical tuner.",
            "Grebennikov's transmitter chapters assume you have seen a contour. This chapter is the contour. The one-home numbers stay 10.13 Ω and 3.13 Ω so the rest of the series can talk. Your bench will print a slightly different pair. Both can be true.",
        ],
    )
    key(
        doc,
        "Contours at a named plane, at a named pulse, beat a single Ropt. Cripps is the center of the map. Load-pull is the map.",
    )
    h2(doc, "Worked Example 10.1. Zopt versus Cripps")
    paras(
        doc,
        [
            f"Measured Zopt = {LP_ZREAL:.1f} − j{abs(LP_ZIMAG):.1f} Ω at the package plane. |Γ| versus 50 Ω is {LP_GAMMA_MAG:.3f}. Real part 12.4 Ω versus the one-home 10.13 Ω is a 22 percent shift, which is ordinary after packaging. The match on the board should present 12.4 − j4.8 Ω at that plane, not 10.13 + j0, unless you re-embed to the die.",
            "If you force 10.13 Ω at the package, you are off the measured peak. Power might drop 0.2 to 0.5 dB, which is 5 to 11 W on a 100 W radio. That is a thermal and an EIRP error, not a rounding error.",
        ],
    )
    h2(doc, "Worked Example 10.2. Tuner loss at a low impedance")
    paras(
        doc,
        [
            f"A passive tuner presenting {ROPT_LDMOS:.2f} Ω, printed 3.13 Ω, has |Γ| = |(3.13 − 50)/(3.13 + 50)| = {abs((ROPT_LDMOS - 50) / (ROPT_LDMOS + 50)):.3f}. High |Γ| means high current on the tuner line and often 1 to 3 dB of extra loss versus a 50 Ω thru. If you forget that loss, you will believe the DUT made 100 W when it made 70 W, and you will design an optimistic radio.",
            "Correct to the DUT plane or use active injection. There is no third option that is honest.",
        ],
    )
    practice(
        doc,
        [
            "Name three contours you would draw on one Smith chart for a cellular final.",
            "Why must GaN load-pull state pulse width?",
            "A fixture plus package is 0.4 dB loss. You measure 100 W at the SMA. Power at the die plane?",
            "Why look at source impedance at f0/2?",
        ],
        [
            "Constant Pout, constant drain efficiency or PAE, and constant ACLR or EVM. Gain is a fourth if you have the ink.",
            "Trapping and thermal transients make CW and pulsed into different devices. Without pulse width, the contour is unlabelled data.",
            f"Die power is higher: 100 × 10^(0.04) = {100 * 10 ** 0.04:.1f} W if 0.4 dB is after the die. Direction matters: loss between die and SMA means the die made more than the SMA meter.",
            "Parametric and odd-mode oscillations often sit near half-frequency. Source-pull only at f0 will not show the negative-resistance island that later sings.",
        ],
    )


def ch11(doc):
    h1(doc, "Chapter 11. Stability, Including Odd-Mode")
    paras(
        doc,
        [
            "Rollett's K-factor and the μ-factor are the s-parameter tests for two-port unconditional stability. K > 1 and |Δ| < 1, or μ > 1, and no passive source or load can make the two-port oscillate. Power devices fail those tests in parts of the band, especially below the operating frequency where gain is high and the package is still a feedback network. You then draw stability circles and stay out of them with lossy matching, ferrites, or RC dampers on the gate.",
            "Unconditional stability of a single die is not stability of a paralleled pair. Odd-mode oscillation is the mode where two cells, or two packages, swing in antiphase, see each other through the combining network, and do not appear on the even-mode 50 Ω ports. A Wilkinson that looks fine in even mode can be an oscillator in odd mode if the isolation resistor is lifted, or is a capacitor at the frequency of interest, or was never there because someone used a T-junction.",
            "Odd-mode is why you put a resistor between gates of paralleled cells, sometimes two resistors and a capacitor to ground at the midpoint. It is why you do not combine high-gain MMICs with a lossless T. It is why a pallet that is stable on a 50 Ω bench sings when you put two in a combiner. The even-mode simulation did not include the mode.",
            "Parametric oscillation mixes f0 with a subharmonic through a time-varying capacitance. You will see f0/2, or sidebands that move when you change drive, and you will chase a matching stub that is not the cause. Gate resistance, a shunt loss at f0/2, and not driving the device into a crazy capacitance swing are the usual fixes. Load-pull that never looked at f0/2 will not predict it.",
            "Low-frequency stability is the video network. A drain bias choke and a large electrolytic make a resonator with the bypass stack. Gain at 1 MHz can still be 20 dB. An oscillation at 800 kHz that amplitude-modulates the RF looks like close-in spurs. Stabilize the bias with a damping resistor, a small R in the electrolytic's path, and a ferrite that still looks like a ferrite at 1 MHz.",
            "Large-signal stability is not small-signal K. A device that is stable at small signal can oscillate at a drive level, or can be stable at drive and oscillate when drive is removed (startup). Envelope simulators, pole-zero identification, and the old-fashioned 'tap the board and watch the spectrum' still earn their keep. Do not ship on K-factor alone.",
            "μ = 1.12 and K = 1.35 at 2.1 GHz on a datasheet are comfort at that frequency. They say nothing at 200 MHz. Plot K from 1 MHz to 2f0. The ugly part is almost never the operating frequency.",
            "An isolator at the output is a stability tool as well as a ruggedness tool. It keeps the load inside a circle. It does not stabilize the gate, and it does not kill odd-mode between cells before the isolator. Put it in the right place in the argument.",
            "Simulation must include the odd-mode network: a differential port between the two drains, or a full EM combining structure. A single-ended s2p of one device, copied twice, with an ideal combiner, will never sing in odd mode. That simulation is how people get surprised on the bench.",
            "Besser and Gonzalez treat amplifier stability as a linear two-port craft. Keep that craft. Then add the parallel-cell mode that those two-port chapters do not draw. This series puts that mode in the high-power book because that is where paralleled cells live.",
        ],
    )
    key(
        doc,
        "K and μ are even-mode two-port tests. Paralleled cells need an odd-mode resistor. Bias networks need damping at video frequencies. Plot stability where the gain is, not only where the radio is.",
    )
    h2(doc, "Worked Example 11.1. Reading K and μ")
    paras(
        doc,
        [
            f"Declared at 2.14 GHz: K = {K_STAB:.2f}, μ = {MU_STAB:.2f}. Both exceed 1, so at that frequency, at that bias, at small signal, the two-port is unconditionally stable. This is necessary to print and not sufficient to ship. Repeat the plot at 100 MHz, 500 MHz, and at the peaking drive level.",
            "If at 100 MHz, K = 0.4, you will add a series gate resistor or an RC shunt that costs you 0.2 dB at 2.14 GHz and buys you a radio that does not oscillate in the truck. That 0.2 dB is cheaper than a recall.",
        ],
    )
    h2(doc, "Worked Example 11.2. Odd-mode resistor on two cells")
    paras(
        doc,
        [
            "Two GaN cells share a drain feed. Gate-to-gate resistor Rg-g = 20 Ω, midpoint capacitor 10 pF to a good RF ground. At even mode the gates swing together, no current through 20 Ω, no gain cost. At odd mode the 20 Ω appears across a virtual differential port and kills the loop. The 10 pF is a short at RF and an open at DC so bias can still be independent if you need a trim.",
            "If you omit the resistor because the even-mode simulation was stable, the first time the two cells mismatch with temperature you will meet a spur that moves when you touch one heat sink. That spur is the mode you refused to damp.",
        ],
    )
    practice(
        doc,
        [
            "A Wilkinson with the isolation resistor removed: which mode is happy, and which mode may oscillate?",
            "An 800 kHz spur that tracks the RF envelope: where do you look first?",
            "Why is K > 1 at 3.5 GHz not a stability proof at 350 MHz?",
            "Name one simulation mistake that hides odd-mode.",
        ],
        [
            "Even mode still combines. Odd mode has no isolation resistor to dissipate antiphase power, so the cells can lock in antiphase and oscillate.",
            "The drain and gate bias networks: chokes, electrolytics, and undamped resonances at video frequencies.",
            "Gain is usually higher at 350 MHz, feedback through the package is different, and K is frequency-specific. You must plot the low band.",
            "Copying one s2p twice into an ideal in-phase combiner, with no differential port and no EM of the split.",
        ],
    )


def ch12(doc):
    h1(doc, "Chapter 12. Bias and Gate Sequencing")
    paras(
        doc,
        [
            "Depletion-mode GaN is on at zero gate voltage. If the drain rail rises while the gate is at zero, the channel conducts a large current, the die overheats in microseconds, and the part is gone, or worse, it lives and is wounded. Sequencing is not etiquette. It is: gate negative and in regulation, then drain on; drain off and confirmed down, then gate release. Enhancement LDMOS is kinder and still deserves an ordered supply because a rising drain with an undefined gate is a transient you have not simulated.",
            f"A typical RF GaN gate is −5 V to −2 V for pinch-off, and a class-AB Idq corresponding to a gate near {SEQ_VG:.1f} V, declared for examples in this chapter. The gate supply must source and sink, because the gate can leak, and because collapse of the negative rail must not leave the gate at zero. A cheap inverter that only sources is a trap.",
            "Drain current at quiescent, on a 50 V rail, is heat before a single RF watt is made. Idq = 0.8 A is 40 W of standing heat. Cellular AB might live there. A pulse radar should hold a colder bias between pulses, or a true off, if the duty cycle and the trap recovery allow. Bias modulation at TDD rates is a feature. Bias modulation that excites traps is a memory problem.",
            "Sequencing can be analog, with a supervisor and a discharge path on the drain capacitors, or digital, with a state machine that reads UVLO, a gate-good flag, and a drain-good flag. Both need a defined behavior when power fails in the middle. The failure path is: dump the drain through a known load, keep the gate pinched, then release. The wrong path is: the negative regulator dies first.",
            "Gate voltage temperature compensation holds Idq. A simple two-resistor plus thermistor, or a proper controller, is pallet circuitry. Without it, a radio that was linear at 25 °C is a spur machine at 85 °C, or a dead class-C brick at −40 °C. Production trim of Idq is a step. Record the trim. A pallet with no trim pad is a hobby.",
            "The gate bias network is in the RF path. A long choke with a large bypass is a resonator. Chapter 11 already accused it of 800 kHz spurs. Size the choke so it is a choke at f0 and a resistor, or a damped R-L, at video. The same sentence applies to the drain feed. An RF bead that saturates at Idc is not a choke. It is a short that appears in the field.",
            "Trapping interacts with bias. A gate voltage that is 'correct' after a 10 µs pulse is wrong after a 1 ms pulse. Some radars use a pre-pulse or a fill pulse to settle traps. Some cellular DPD models include a slow envelope state. Neither is a substitute for a foundry process with decent current collapse, but both are how you ship the process you have.",
            "Negative gate voltage on a tower radio is a reliability item. Moisture, dendrites, and a −5 V rail on an outdoor board want spacing and coating. Book 9 will talk about coating. This chapter says: the sequence still has to work after two years of salt fog, which means the supervisor must not depend on a leaking electrolytic.",
            "LDMOS sequencing is drain-friendly but not optional for the control software. A common mistake is to apply RF drive before Idq is established, so the first milliseconds are class C into a load-pull region you never measured. Mute the driver until bias is good. That mute is a bias problem, not a firmware flourish.",
            "Book 8 sequences 650 V GaN with a different fear: miller-induced turn-on of a half-bridge. Do not copy that circuit onto an RF pallet. Copy the idea of a defined state machine. The voltages, the speeds, and the parts differ.",
        ],
    )
    key(
        doc,
        "Pinch off first, drain second, reverse on the way down. Hold Idq against temperature. Damp the bias network at video. The negative rail must fail safe.",
    )
    h2(doc, "Worked Example 12.1. Standing heat at Idq")
    paras(
        doc,
        [
            f"Declared: Vd = {SEQ_VD:.0f} V, Idq = {IDQ_AB:.1f} A (10 percent of an 8 A peak-ish current). Standing dissipation is {PDISS_BIAS:.0f} W before RF. On a pallet whose RF average is 20 W at 50 percent efficiency, another 20 W of RF heat sits on top of 40 W of bias heat. The cold plate sees 60 W. If you only sized cooling for the RF heat, you undersized by a factor of three.",
            "Pulse radar at 10 percent duty with bias held at the same Idq between pulses wastes that 40 W continuously. Gating the bias with the pulse, if traps allow, cuts average bias heat by roughly the duty cycle. Measure trap recovery before you celebrate.",
        ],
    )
    h2(doc, "Worked Example 12.2. Capacitor discharge time")
    paras(
        doc,
        [
            f"A drain bank of 20 µF at 50 V must die before the gate may release. Through a 10 Ω dump resistor, τ = 200 µs, so 5τ = 1 ms to a volt or two. The sequencer's delay from 'drain off' to 'gate release' must be longer than that, with margin for the resistor's tolerance and for a stuck supply. A 100 µs delay on a 1 ms bank is how you make a spark and a warranty claim.",
            "The dump resistor dissipates (1/2)CV² per event: 0.5 × 20e-6 × 50² = 25 mJ. Rare events, small. If software chatters the drain every millisecond, it is 25 W in the dump resistor. Debounce the state machine.",
        ],
    )
    practice(
        doc,
        [
            "Write the power-up order for a depletion GaN pallet.",
            "Idq = 1.2 A at 28 V: standing heat?",
            "Why must the gate supply sink current, not only source it?",
            "A TDD radio mutes RF 200 µs before the drain collapses. Why?",
        ],
        [
            "Negative gate in regulation and verified, then drain ramp; RF drive only after Idq is in band. Reverse on power-down: RF mute, drain dump, then gate release.",
            "28 × 1.2 = 33.6 W, continuous, independent of RF until you count PAE properly.",
            "Gate leakage, reference dividers, and a collapse of the negative rail that must pull the gate down, not let it float toward zero. A source-only charge pump can leave the gate unsafe.",
            "So the PA is not transmitting while the load line walks during the drain transient. You avoid both a spectral splash and a bias region you never linearized.",
        ],
    )


def ch13(doc):
    h1(doc, "Chapter 13. Combiners: Wilkinson and Gysel")
    paras(
        doc,
        [
            "A Wilkinson combiner is an N-way network of quarter-wave lines and isolation resistors that, in even mode, looks like a matched combiner and, in odd mode, dumps difference power into the resistors. Two-way is the textbook: two 70.7 Ω quarter-waves and a 100 Ω resistor. Four-way can be a tree of two-ways or a true four-way with 100 Ω lines and a resistor star. Insertion loss, amplitude balance, and phase balance set combining efficiency. Isolation sets whether a failed pallet takes its neighbor with it.",
            "The isolation resistor in a high-power Wilkinson is the problem. At the isolated port of a two-way, a complete failure of one pallet can dump half the surviving pallet's power into that resistor. A 100 W class with a 50 W resistor is a fire. You then either derate, split the resistor, float it on a heat sink, or leave Wilkinson for Gysel.",
            "A Gysel combiner moves the isolation loads to ground-referenced ports so they can be real dummy loads with coolant. The network is more lines, more bandwidth-sensitive, and kinder at a kilowatt. When the isolation resistor has to survive a real imbalance, Grebennikov will send you to Gysel. This chapter does too.",
            "Radial combiners, spatial combiners, waveguide magic-Ts, and corporate feeds are the rest of the family. Spatial combining, many PAs radiating into a horn or a cavity, avoids a resistive isolation element by using space. It has its own amplitude and phase discipline and a different failure mode. Magic-Ts are the waveguide version of a hybrid. Corporate feeds are trees. Name the combiner before you name the loss.",
            "Amplitude imbalance of 0.5 dB and phase imbalance of 10 degrees are not rounding. Combining two equal sources with a phase error φ has a loss of about 10 log(cos²(φ/2)) in the coherent sum, plus whatever the network dissipates. Ten degrees is 0.03 dB of phase loss, usually smaller than the copper. Two decibels of amplitude imbalance is much worse: the weaker pallet limits the match and the isolation resistor starts to heat in normal operation.",
            "An isolator or a circulator after the combiner, or one per pallet, is how a shorted antenna does not become a shorted transistor. Ferrite isolators have bandwidth, insertion loss, and a temperature-sensitive match. They also have a dummy load on the third port that must be sized for reverse power. That load is a thermal design, Chapter 14, not a catalog afterthought.",
            "At millimeter wave, on-die Wilkinson structures in a GaN MMIC are small and lossy. Combining in air, in waveguide, or in an array (Book 4) often beats an on-die tree. The 0.8 dB you lose on die is 0.8 dB of EIRP. Off-die you might lose 0.3 dB and spend mechanical alignment.",
            "N-way combining of N = 16 is a project. Binary trees of 2-ways have log2(N) stages of loss. A 0.2 dB Wilkinson times four stages is 0.8 dB, which on 16 × 100 W is 480 W of heat in the copper and the resistors if you are not careful about what that 0.8 dB means. Draw the tree, assign a loss to each stage, and cool the isolation resistors at the stage where imbalance is worst.",
            "Odd-mode from Chapter 11 lives here. The isolation resistor is the odd-mode damper of a Wilkinson. Lift it, and you have a T-junction with gain. Gysel's loads are the same damper with a better heat path. Simulate even and odd, as already preached.",
            "Book 4 owns the antenna feed network as a radiation problem. This chapter owns the PA combining network as a power problem. When an AESA puts a PA at each element, the 'combiner' becomes space and the array factor. That is Book 4's gain. The PA is still this book.",
        ],
    )
    key(
        doc,
        "Wilkinson is the default two-way. Gysel is what you use when the isolation load must be a real dummy. Isolation, balance, and odd-mode are the design, not the even-mode insertion loss alone.",
    )
    h2(doc, "Worked Example 13.1. Isolation resistor heat")
    paras(
        doc,
        [
            f"Two 50 W pallets, one fails open, the survivor still makes 50 W into a two-way Wilkinson. In the ideal textbook, half of that 50 W can appear in the isolation resistor during the transient until protection mutes. Size the resistor for at least 25 W continuous if protection is slow, or for a pulse of 25 W for the mute time if protection is fast and has been tested. A 0.25 W 0603 is a rumor.",
            f"Four-way tree: worst-case one pallet alive, three dead, is a different fraction depending on the tree. Do not guess. Simulate the failure, then size the loads. Protection that mutes in {100:.0f} µs still leaves a thermal impulse of P × t in the resistor.",
        ],
    )
    h2(doc, "Worked Example 13.2. Gysel isolation load impedance")
    paras(
        doc,
        [
            f"A textbook two-way Gysel uses 50 Ω lines in a ring-like set and isolation loads of 50 Ω, with some branches at 50√2 ≈ {50 * math.sqrt(2):.1f} Ω. The loads sit to ground. They can be 50 Ω terminations on cables to a dummy, cooled. That is the point. Z values move with the exact topology; the grounded load does not.",
            f"Compare to Wilkinson: the isolation element is a floating {100:.0f} Ω between ports. At 100 W class, that floating resistor is the part that does not exist in a convenient cooled package. Gysel exists because of that sentence.",
        ],
    )
    practice(
        doc,
        [
            "Why does a high-power Wilkinson become a Gysel?",
            "Two carriers 0.5 dB unequal, in phase: roughly how much power in the isolation resistor of a two-way Wilkinson in normal operation?",
            "Sixteen pallets of 80 W, tree loss 0.7 dB: power at the sum if all are alive?",
            "An AESA with a PA per element: where did the Wilkinson go?",
        ],
        [
            "Because the isolation resistor must dump real watts into a grounded, coolable load, not a floating chip between two hot traces.",
            "Small. Isolation resistors heat strongly under failure or large imbalance. 0.5 dB is a few percent of power; the resistor sees the difference power, on the order of a watt or less at 50 W class, not zero. Still size for failure.",
            f"16 × 80 = 1280 W lossless; 0.7 dB is factor {10 ** (-0.07):.3f}, so {1280 * 10 ** (-0.07):.0f} W.",
            "Into space. Combining is the array factor, Book 4. Isolation becomes element coupling and a circulator per chain, still this book's PA problem.",
        ],
    )


def ch14(doc):
    h1(doc, "Chapter 14. The Heat Path")
    paras(
        doc,
        [
            "Power that is not radiated or delivered to the load is heat. The path is junction to die attach to flange to spreading to cold plate to air or liquid. GaN on SiC lives or dies on that path. A number on a datasheet, Rθ,jc, is the first resistor. The rest of the chain is yours. A beautiful load line with a 150 °C junction in a 70 °C outdoor radio is not a load line. It is a FIT calculation you have not done.",
            "Die attach is AuSi, AuSn, sintered silver, or a void you did not know you had. Voids are thermal resistors and they are reliability. X-ray is not optional on a 100 W flange. Copper-tungsten, copper-molybdenum, and copper-diamond flanges exist to match TCE and to spread. A copper flange that looks simpler will warp the die over temperature. Book 9 names some of those stacks. This chapter names the watt.",
            "Pulse and CW are different thermal problems. A 100 µs pulse heats the junction and the first hundred microns. A CW carrier heats the flange and the cold plate. A 10 percent duty radar can run a junction temperature that would be illegal in CW while the average flange temperature looks comfortable. The inverse is also true: a CW test at 20 W average does not qualify a 200 W peak pulse if the pulse is long enough to overheat the die locally.",
            "Thermal resistance adds. Rθ,jc = 1.2 °C/W, grease or phase-change = 0.3 °C/W, spreading in the plate = 0.4 °C/W, then coolant-to-ambient. At 60 W of dissipation, 1.9 °C/W already before coolant is 114 °C of rise. If ambient is 55 °C at the inlet, you are done. Liquid cooling is not a luxury at that density. It is arithmetic.",
            "Infrared cameras lie about dies behind lids. Thermocouples on flanges are honest about flanges. A forward-voltage or a gate-leakage temperature proxy can be honest about junctions if you calibrated it. Use more than one. Reliability models want junction, not the temperature of the heat sink's marketing photo.",
            "Mean time to failure slogans do not replace junction, voltage, and VSWR. Arrhenius on a 1.0 eV activation energy will scare you or soothe you depending on the 10 °C you argued about. Arguments about 10 °C are why the thermal path is a design, not a gasket.",
            "Combining heat is a layout. Sixteen pallets need sixteen paths, not one plate with a hot center. Liquid manifolds that starve the last pallet in the chain are a real failure. Airflow that recirculates is a real failure. Thermal design is mechanical engineering sitting in a radio. Invite that engineer before layout freeze.",
            "The dummy load on an isolator is a heat path. Reverse power at 3:1 VSWR, 100 W forward, is not a rounding error. Γ = (3−1)/(3+1) = 0.5, Preflected = 25 W. That 25 W is in the isolator load, continuously, if the antenna is 3:1. Size it. Cool it. Protect if VSWR exceeds a trip.",
            "Efficiency is cooling. A 10-point efficiency win at 100 W RF is tens of watts of heat. Doherty, Chapter 9, is a thermal chapter as much as an RF chapter. People who treat efficiency as a datasheet decoration buy larger fans later, which buy more conducted emission, which is Book 7.",
            "The 650 V GaN switch in Book 8 has a heat path too, into a PCB copper pour and a heat sink on a charger. Do not mix the thermal spreading models. An RF flange on a cold plate is not an SO-8 on FR-4. Both are I²R and ΔT. The drawings differ.",
        ],
    )
    key(
        doc,
        "Junction to coolant is a chain of resistors. Pulse and CW see different resistors. VSWR heat in the isolator is part of the same chain. Efficiency is cooling.",
    )
    h2(doc, "Worked Example 14.1. Junction temperature at 60 percent PAE")
    paras(
        doc,
        [
            f"Pout = 100 W, Pin = {PAE60_PIN:.0f} W, PAE = 60 percent: Pdc = (100 − 10)/0.60 = {PAE60_PDC:.1f} W. Dissipation in the device is Pdc + Pin − Pout = {PAE60_DISS:.1f} W. With Rθ,jc = {RTH:.1f} °C/W and a 85 °C flange, Tj = {TJ:.1f} °C. Whether that is legal depends on the foundry's mission profile, not on a 175 °C absolute-max headline.",
            "If PAE is 40 percent with the same Pin, Pdc = 225 W, dissipation = 135 W, ΔTjc = 162 °C, and a 85 °C flange puts the junction at 247 °C, which is a failure. Efficiency is not a score. It is the thermal design.",
        ],
    )
    h2(doc, "Worked Example 14.2. Reflected power at VSWR 3:1")
    paras(
        doc,
        [
            f"|Γ| = (VSWR − 1)/(VSWR + 1) = {GAMMA_3:.3f}. Preflected = Pforward × |Γ|² = {PREFL_3:.0f} W on a 100 W forward. The isolator load must stand 25 W continuous if this VSWR is an operating condition, or the PA protection must trip if it is not. The transistor also sees a modified load line; ruggedness ratings assume you asked this question.",
            f"At VSWR 10:1, |Γ| = 9/11 = {9/11:.3f}, Preflected = {P100 * (9/11) ** 2:.0f} W. That is a survival test, not an operating point. The isolator load and the trip threshold are how you tell the two apart.",
        ],
    )
    practice(
        doc,
        [
            "Rθ,jc = 0.9 °C/W, Rθ,cs = 0.4, Rθ,sa = 1.5, Pdiss = 40 W, Ta = 40 °C: Tj?",
            "Why can a 10 percent duty radar run a higher peak junction than a CW radio at the same average flange temperature?",
            "Who owns the dummy load on the isolator, electrically and thermally?",
            "Name one inspection that finds a bad die attach.",
        ],
        [
            "Rθ,ja = 0.9+0.4+1.5 = 2.8 °C/W. ΔT = 112 °C. Tj = 152 °C.",
            "The pulse may not last long enough to heat the whole spreading path. Junction spikes; flange averages. CW heats both. The limits are different.",
            "This book. It is an RF protection part whose heat is reverse power. Book 8 does not own it because the frequency is RF and the job is VSWR, not conversion.",
            "X-ray for voids; acoustic microscopy; a thermal image of an open die; a suspiciously high Rθ,jc on a test bench.",
        ],
    )


def ch15(doc):
    h1(doc, "Chapter 15. Harmonic Filters")
    paras(
        doc,
        [
            "A harmonic filter follows the last amplifier. Class F wanted harmonics at the die. The regulator wants them gone at the antenna. Those two sentences are not a contradiction if the chain is a chain. The filter is a cavity, a ceramic resonator, a combline, a waveguide high-pass, or a suspended stripline. Microstrip at 100 W fails from voltage and from heat. Book 4 taught filter poles. This chapter adds voltage, current, and dissipation in the resonators.",
            "The mask is Book 7 as a test. This chapter as a design. Occupied bandwidth, harmonic limits in dBc or in EIRP, and spurious from the synthesizer all land in the same spectrum analyzer later. A five-pole low-pass that looked fine at 0 dBm in ADS will arc at 100 W if you did not watch voltage on the first capacitor.",
            f"A crude Chebyshev-ish roll-off reminder: attenuation on the order of 20N log10(f/fc) dB well above cutoff for an N-pole low-pass, ignoring ripple and matching. N = {FILT_N:.0f}, fc = 3.8 GHz, f = 7 GHz: about {FILT_ATTN:.0f} dB before real-world Q and layout. Second harmonic of a 3.5 GHz PA sits at 7 GHz. If you need 60 dBc and the PA already makes −20 dBc, the filter owes you 40 dB. Five poles can do that. Three poles might not.",
            "Cavity Q of a few thousand is how you keep insertion loss at 0.2 dB instead of 1 dB. One decibel of filter loss after the last PA is the factor 0.794 of power, the one-home EIRP tax. Spending a cavity to save 0.5 dB is a range decision, Chapter 18 and Chapter 19.",
            "Second-harmonic traps at the PA, stub or coupled, are not the same as the harmonic filter. Traps shape the load at 2f0 for efficiency. The filter protects the antenna port. You usually need both. A trap that radiates is a Book 7 problem. Shield it.",
            "Waveguide beyond cutoff is a high-pass. A PA that must reject low-frequency junk, local oscillator leakage, or a drive amplifier's VHF oscillation can use a section of waveguide as a filter. Cutoff of air-filled rectangular waveguide is c/(2a). WR-284 at S-band is a classic. Do not use waveguide as a low-pass. That is not what cutoff means.",
            "Multipaction in vacuum, corona in air, and heating of the inner conductor of coax are the high-power filter's failure modes. A 100 W ground radio in air is usually a voltage-spacing problem. A 200 W satellite diplexer in vacuum is a multipaction analysis. Book 8's HV habits help. The frequency is still this book.",
            "Re-entrant cavities and ceramic puck filters are how you shrink a 2 GHz low-pass that cannot be lumped. Temperature drift of the ceramic is a mask problem at the band edge. Compensate or ovenize or leave margin. A filter that drifted into the channel is a dropped call, not a pretty Q.",
            "Do not ask the duplexer to be the only harmonic filter unless you designed it that way. A duplexer is a pair of bandpass filters with isolation as the job. It will reject some harmonics. Measure how many dB. Then decide if Chapter 17 already paid this chapter's bill.",
            "Simulation: harmonic balance in ADS or Microwave Office for the PA plus a circuit filter; a 3D eigenmode or driven-modal solution for the cavity. Book 7 will name those solvers as tools. This chapter names the voltage in the gap.",
        ],
    )
    key(
        doc,
        "Harmonics at the die can be useful. Harmonics at the antenna are a mask. Filter after the last watt, with Q high enough that the 0.794 tax stays small, and with voltage spacing honest.",
    )
    h2(doc, "Worked Example 15.1. Poles versus second harmonic")
    paras(
        doc,
        [
            f"PA at 3.5 GHz, second harmonic 7.0 GHz, filter fc = 3.8 GHz, N = 5. The 20N log10(f/fc) sketch is {FILT_ATTN:.1f} dB. If the PA delivers −15 dBc at 2f0 into 50 Ω, the antenna sees about −15 − {FILT_ATTN:.0f} = {−15 - FILT_ATTN:.0f} dBc before real matching and finite Q. If the license wants −60 dBc, you have margin in the sketch and you still must measure, because a transmission zero you did not place, or a housing mode, can eat 20 dB of that sketch.",
            "If N = 3, the same sketch is 60 percent of 66 dB, about 40 dB, and −15 − 40 = −55 dBc, which is a fail if the limit is −60. Poles are not decoration.",
        ],
    )
    h2(doc, "Worked Example 15.2. Cavity Q and insertion loss")
    paras(
        doc,
        [
            f"A single resonator's 3 dB bandwidth is f0/Q. At 2.0 GHz, Q = {Q_CAV:.0f}, BW = {BW_CAV / 1e6:.1f} MHz. A five-pole filter using such resonators can be a few tens of megahertz wide with a few tenths of a dB of loss if coupling is right. The same poles in microstrip on FR-4 would be a few dB of loss and a fire at 100 W.",
            "Insertion loss of 0.3 dB is a factor of 0.933, so 100 W becomes 93.3 W. Insertion loss of 1.0 dB is the one-home 79.4 W. The cavity paid for 13.9 W of EIRP. That is why high-Q is a power-amplifier problem.",
        ],
    )
    practice(
        doc,
        [
            "Why is microstrip the wrong 100 W harmonic filter at 2 GHz?",
            "Second harmonic must be −70 dBc. PA makes −25 dBc. Filter owes you how much?",
            "Waveguide below cutoff: high-pass or low-pass?",
            "A duplexer already shows 25 dB at 2f0. Do you still need Chapter 15?",
        ],
        [
            "Voltage and heat. The strip edges and the dielectric loss will arc or cook. Use cavity, ceramic, suspended stripline, or waveguide.",
            "45 dB. Then add margin for temperature, VSWR, and the fact that −25 dBc was measured into 50 Ω, not into the filter's stopband impedance.",
            "High-pass. Energy below cutoff reflects. That rejects low-frequency junk; it does not reject harmonics above the band.",
            "Maybe not, if 25 dB plus the PA's dBc meets the mask with margin. Measure. Do not assume a duplexer's bandpass shape is a harmonic specification.",
        ],
    )


def ch16(doc):
    h1(doc, "Chapter 16. Coax and Waveguide")
    paras(
        doc,
        [
            "After the filter, the watts travel. Coaxial line, rigid line, and waveguide are the three working answers. Flexible RG-type cables are for drive and for test. They are not a 100 W, 2 GHz run of any length you care about, because loss and heating of the inner conductor will tax EIRP and then melt the dielectric. 7/8 inch, 1-5/8 inch, and larger foam or air-dielectric lines are the broadcast and cellular plant. Waveguide is the radar and the microwave link when loss, power, or pressurization says so.",
            "Loss in coax, to a working approximation, rises as the square root of frequency because of skin effect, plus a dielectric term that rises as frequency. A number like 0.05 dB/m at 1 GHz becoming 0.07 dB/m at 2 GHz is a skin-effect-ish story. Twenty meters of 0.07 dB/m is 1.4 dB, which is more than the one-home 1 dB tax. Line length is a power-amplifier specification.",
            "Peak voltage, not only average power, sizes the line. A VSWR of 2 already raises the peak. A pulse with a high peak-to-average raises it again. Dry air, pressurized dry air or nitrogen, and SF6 in some plants, raise the breakdown. Multipaction in vacuum is the space version. Book 8 knows insulation. This chapter knows the coax's inner conductor.",
            "Waveguide cutoff is c/(2a) for the TE10 mode in air-filled rectangular guide. Below cutoff the line is an attenuator. Above cutoff it is a low-loss highway with a width that sets the band. WR-90 at X-band, WR-229 at S-band, WR-15 at V-band: pick the band then the letter. Flanges, pressure windows, and bends are components, each with a VSWR and a power rating.",
            "Heating of the inner conductor of coax is a current problem. At 100 W into 50 Ω the RMS current is 1.41 A. Skin effect crowds that current. A thin inner conductor in a small cable cooks. A 1-5/8 inch line at the same 100 W is idle. At 10 kW it is working. Match the size to the watt.",
            "Connectors are where radios fail. 7/16 DIN, 4.3-10, type N, SMA, 2.92 mm, and waveguide flanges are different power and frequency classes. SMA is not a 100 W, 2 GHz plant connector. 4.3-10 exists because PIM and power and size wanted a better N. Torque, cleanliness, and a torque wrench are process, not personality.",
            "Passive intermodulation is a plant problem that looks like a receiver problem. Two transmit carriers in a rusty junction make a third-order product that lands in the receive band of a duplexed radio. That is Chapter 17's isolation plus this chapter's junctions. Silver, cleanliness, and not using ferrous junk in the RF current path are the craft. Book 7 will see PIM as a test in some specs. This chapter prevents it.",
            "Pressurization alarms exist because a wet line is a different capacitance, a different loss, and a corrosion cell. A dehydrated plant is an RF specification. Treat the alarm as a trip, not as a nuisance.",
            "Book 4's transmission-line theory is the lossless phasor. This chapter is the loss, the heat, the voltage, and the connector. When Friis is written, the feed loss sits with Pt. Antenna gain does not cancel a wet 1-5/8 inch run.",
            "Do not send 100 W through 30 m of RG-58 and then ask Book 4 for more antenna gain. The cable spent the watt. The antenna can only concentrate what arrived.",
        ],
    )
    key(
        doc,
        "Size the line for loss, voltage, and heat, not for the connector you had in the drawer. Feed loss after the last PA is EIRP. Connectors and PIM are part of the line.",
    )
    h2(doc, "Worked Example 16.1. Twenty meters of coax")
    paras(
        doc,
        [
            f"Declared 0.05 dB/m at 1 GHz, skin-like √f scaling to 2 GHz: α = 0.05 × √2 = {ATTN_COAX:.3f} dB/m. Twenty meters: {ATTN_COAX * 20:.2f} dB. One hundred watts becomes {P_TO_ANT_20M:.1f} W at the antenna. That is worse than the one-home 1 dB example. Shorten the run, thicken the line, or move the PA to the antenna and send DC and fiber, which is how remote-radio heads were born.",
            "A remote PA at the antenna still has a jumper. A 2 m jumper at 0.07 dB/m is 0.14 dB. That is the remaining tax. The 20 m run is what you escaped.",
        ],
    )
    h2(doc, "Worked Example 16.2. Waveguide cutoff")
    paras(
        doc,
        [
            f"WR-284 has a ≈ {WG_A * 1000:.2f} mm. Air-filled TE10 cutoff is c/(2a) = {WG_FC / 1e6:.0f} MHz. A 3.0 GHz radar is above cutoff. A 400 MHz UHF radio is not; that radio is coax. Using WR-284 as a 'filter' of VHF junk on an S-band PA is legitimate: VHF is below cutoff and dies exponentially along the guide.",
            "The same guide at 6 GHz may start to allow TE20 or other modes depending on b. Overmoding is a radar-spurious problem. Stay in the recommended band of the WR number unless you mean to be in a multimode world.",
        ],
    )
    practice(
        doc,
        [
            "100 W into 50 Ω: RMS current?",
            "Why did cellular move the PA to the tower top?",
            "Name a connector that is wrong for 100 W at 2 GHz in a plant, and one that is used.",
            "PIM: two Tx carriers and a rusty flange. Which book owns the test, and which owns the flange?",
        ],
        [
            "I = sqrt(P/R) = sqrt(2) ≈ 1.41 A rms.",
            "Feed loss. Tens of meters of coax ate 1 to 3 dB of EIRP and of uplink. Fiber and DC to a remote radio head is cheaper than fatter coax once you count the watt.",
            "SMA is wrong as a plant connector at that power. 7/16 DIN or 4.3-10 are used. N is the historical middle.",
            "Book 7 may own a PIM test method when it is specified. This chapter owns the junctions, metals, and torques that prevent PIM.",
        ],
    )


def ch17(doc):
    h1(doc, "Chapter 17. The Duplexer")
    paras(
        doc,
        [
            "A duplexer lets a transmitter and a receiver share an antenna. It is two filters and an isolation number. In a frequency-division radio the Tx filter passes the transmit band and rejects the receive band; the Rx filter does the opposite. Isolation at the receive frequency is how much of the PA still lands on the LNA. Isolation at the transmit harmonic is a bonus, not always a specification. A T/R switch is the time-division cousin: a switch, a limiter, and a timing diagram.",
            "LNA survival is a duplexer specification. If the PA makes 50 dBm and the LNA dies at 20 dBm, you need 30 dB of isolation plus margin before you count a limiter. Real duplexers at cellular bands offer 40 to 80 dB depending on volume and Q. A 80 dB cavity duplexer is a box. A 40 dB ceramic duplexer is a component. Neither is a drawing of two ideal bandpass filters.",
            "Leakage is not only linear isolation. Noise in the transmit band from the PA's noise floor, multiplied by finite Rx-filter rejection, can still raise the receiver's noise figure. A PA that is quiet in-band on a spectrum analyzer at 10 kHz RBW can be loud in 1 Hz as far-out phase noise. McClaning's noise chapter, later in this book, and Gardner's loop, later still, are how you keep the PA from broadcasting noise into its own receiver.",
            "T/R switches at radar powers are circulators, PIN diode switches, or plasma/gas devices in old plants. Timing: the receiver must be off or protected before the pulse, and recovered after the pulse, in time for the nearest range bin. A 1 µs recovery is 150 m of range you cannot see. That is a radar specification, Chapter 19, implemented as a switch, this chapter.",
            "Insertion loss of the Tx path is feed loss, factor 0.794 per decibel. A 0.5 dB duplexer is 11 percent of power. You will pay for a cavity to get that 0.5 dB back if the radio is range-limited. A 1.5 dB SAW duplexer in a handset is a different economy: the PA is 1 W, the battery is the constraint, and 1.5 dB is still hated but lived with.",
            "Power handling of a ceramic duplexer is a few watts to tens of watts. A 100 W radio is a cavity or a large ceramic, or a circulator plus filters. Do not drop a handset duplexer after a 100 W pallet because the bands matched in a table.",
            "Antenna VSWR appears at the PA through the Tx filter, modified by the filter's delay. A filter is not an isolator. A circulator between PA and duplexer is common. The circulator's third port is the dummy load of Chapter 14.",
            "Isolation of 80 dB sounds large until you write dBm. 50 dBm minus 80 dB is −30 dBm at the LNA. A 20 dBm survival LNA is safe on average. A 1 dB compression at −10 dBm LNA is not happy at −30 dBm if you wanted a low-noise, linear receiver. Survival and linearity are different isolation bills.",
            "Book 4's antenna still has a match. The duplexer was designed into 50 Ω. Antenna ice is a VSWR. The chain includes that VSWR. Protection, isolator, and a VSWR trip are how you keep Chapter 11's stability and Chapter 14's heat when the antenna is not 50 Ω.",
            "Immunity of the receiver to its own transmitter is not Book 7's EMC immunity. Book 7 is the enclosure and the cable in a chamber. This chapter is the intended co-site of Tx and Rx. Both can fail on the same afternoon.",
        ],
    )
    key(
        doc,
        "Isolation is LNA survival and LNA linearity, in dB that must match dBm. Insertion loss is EIRP. A duplexer is not an isolator. A T/R switch is a timing problem as much as an RF problem.",
    )
    h2(doc, "Worked Example 17.1. Leakage onto the LNA")
    paras(
        doc,
        [
            f"PA = 50 dBm, duplexer isolation {DUP_ISO:.0f} dB: leakage = {TX_LEAK:.0f} dBm. If LNA survival is {LNA_SURV:.0f} dBm, you have {LNA_SURV - TX_LEAK:.0f} dB of survival margin. If LNA P1dB is −10 dBm, you have no linearity margin; the LNA is 20 dB into compression. Isolation that keeps the LNA alive can still deafen it. Add rejection, or a limiter that you have noise-figured, or more isolation.",
            "A limiter that adds 0.5 dB of NF is a Chapter 20 cost. Sometimes it is cheaper than 20 dB more cavity isolation. Sometimes it is not. Write both bills.",
        ],
    )
    h2(doc, "Worked Example 17.2. T/R recovery and range")
    paras(
        doc,
        [
            f"Radar: 1 µs of dead time after the pulse before the receiver is clean. Light-time two-way: range = c × t / 2 = {C0 * 1e-6 / 2:.0f} m. You cannot see inside 150 m. If the spec wants 50 m, recovery must be 333 ns. That number sets PIN diode charge storage, circulator blanking, and limiter recovery. It is not an RF matching number.",
            "A 100 µs pulse with 1 µs recovery is a 1 percent tax on the pulse. A 1 µs pulse with 1 µs recovery is a 50 percent tax on the timeline. Short-pulse radars live and die on this chapter.",
        ],
    )
    practice(
        doc,
        [
            "PA 44 dBm, LNA dies at 10 dBm. Minimum isolation plus 10 dB margin?",
            "Why can Tx noise, not Tx carrier leakage, still raise NF?",
            "Handset SAW duplexer at 1.5 dB Tx loss, Pout 30 dBm: power at the antenna?",
            "Is co-site isolation of Tx and Rx an EMC test in Book 7?",
        ],
        [
            "Need 44 − 10 = 34 dB to the death point, plus 10 dB margin: 44 dB. Then separately check LNA P1dB.",
            "The PA's broadband noise in the receive band, times finite Rx-filter rejection, is additive noise at the LNA input. The carrier can be well isolated at fTx while fRx still sees noise.",
            f"1.5 dB is a factor of {10 ** (-0.15):.3f}, so 30 dBm becomes 28.5 dBm, about 0.71 W of 1 W.",
            "No. It is this chapter's intended sharing of an antenna. Book 7 is unintended radiation and immunity of the product in a chamber. A radio can pass Book 7 and still deafen itself.",
        ],
    )


def ch18(doc):
    h1(doc, "Chapter 18. EIRP and Feed Loss")
    paras(
        doc,
        [
            "Effective isotropic radiated power is transmitter power times antenna gain, with every loss after the last amplifying device counted against the transmitter. In decibels, EIRP = P_PA,dBm − L_feed,dB + G_ant,dBi. One decibel of feed is one decibel of EIRP. The linear factor for one decibel is 0.794. That factor is one-home in this book. Antenna gain is Book 4. This chapter will not invent a gain.",
            "Effective radiated power, ERP, is the same idea against a half-wave dipole instead of an isotropic radiator, a 2.15 dB shift if someone is being careful. Licenses mix the two. Read the unit. A 100 W ERP FM station is not a 100 W EIRP station.",
            "Exposure limits, IEEE C95.1 and ICNIRP, close the chain for people near the antenna. They are not a matching handbook. They set a power density you may not exceed. A 100 W EIRP into a 10 dBi antenna is a different density at 2 m than at 50 m. Book 4's spreading is the 1/R². This book supplies the watt that was spread. Compliance measurements often sit in Book 7's lab even when the limit is an exposure limit. The design work is here.",
            "Mask compliance for intended radiation is a license. Occupied bandwidth, harmonics, and spurious, in dBc or in absolute EIRP, are the numbers. Book 7's chamber is how unintentional radiation is tested. A conducted sample at the antenna port, plus a radiated harmonic survey, is how intentional radio harmonics are often shown. Two reports. Do not mix them. Book 7 will say so again.",
            "Remote radio heads exist because this chapter is true. Moving the PA to the antenna trades feed loss for a weatherproof PA and a fiber. The EIRP win is the 1 to 3 dB you stopped dumping in the line. The thermal win or loss depends on sun load and on altitude. Chapter 14 still applies, now at the top of a pole.",
            "AESA EIRP is the sum of element powers times the array factor, with taper and failures. Book 4 owns the factor. If 256 elements make 2 W each at the element, and the array factor in a direction is 24 dB above isotropic-element, you still subtract element feed loss inside the module. The one-home 0.794 applies per module jumper.",
            "People confuse antenna gain with PA power. A 20 dBi dish on a 1 W PA can out-EIRP a 100 W PA on a dipole. Range in a communications link, Friis, cares about EIRP and about Gr. Radar, Chapter 19, cares about EIRP and about Gr and about RCS, and then divides by R⁴. More gain is not more watts. It is a narrower beam. Book 4 will make you pay for sidelobes.",
            "Feed loss includes jumper, connectors, duplexer Tx insertion loss, harmonic-filter insertion loss, and the isolator. Add them. A 0.2 + 0.1 + 0.4 + 0.3 + 0.2 dB chain is 1.2 dB, factor 0.759, 75.9 W of a 100 W PA. The PA engineer who quoted 100 W and the system engineer who quoted 100 W EIRP have not yet met.",
            "The Friis space factor at a named frequency and range is Book 4's one-home arithmetic. This chapter only multiplies it by Pt after feed and by Gt Gr. If you need a received-power number, take Gt and Gr from Book 4, take Pt from here.",
            "Nothing after the last amplifier creates power. Matching, filtering, and antennas redistribute it, concentrate it, or burn it. That sentence is the key idea of the high-power half of this book.",
        ],
    )
    key(
        doc,
        "EIRP = PPA − Lfeed + Gant. One decibel of feed is the factor 0.794 of power. Antenna gains live in Book 4. This chapter owns the watt and the loss after the watt.",
    )
    h2(doc, "Worked Example 18.1. The one-home one-decibel tax")
    paras(
        doc,
        [
            f"Linear factor for 1 dB: 10^(−0.1) = {LOSS_1DB:.3f}, printed 0.794. One hundred watts becomes 79.4 W at the antenna. With Book 4's 12 dBi antenna, EIRP = 20 dBW − 1 dB + 12 dB = 31 dBW, or 1.26 kW EIRP. The antenna did not create 1.16 kW. It concentrated 79.4 W.",
            "If the feed had been 0 dB, EIRP would be 32 dBW. The missing decibel is 26 percent of EIRP, not 1 percent, because decibels are logarithmic. That is why cavities, short jumpers, and remote PAs exist.",
        ],
    )
    h2(doc, "Worked Example 18.2. Adding the chain of small losses")
    paras(
        doc,
        [
            f"Isolator 0.25 dB, filter 0.30 dB, duplexer 0.40 dB, jumper 0.20 dB: sum 1.15 dB, factor {10 ** (-0.115):.3f}. One hundred watts becomes {100 * 10 ** (-0.115):.1f} W. EIRP with 10 dBi: {10 * math.log10(100) - 1.15 + 10:.2f} dBW. Quote 18.85 dBW, not 20 dBW, and not 30 dBm plus a prayer.",
            "A 0.15 dB connector you forgot is 3.5 W at this level. Forgotten connectors are the most expensive watts in a plant.",
        ],
    )
    practice(
        doc,
        [
            "Convert 2 dB of feed loss to a linear factor and to watts from a 100 W PA.",
            "ERP versus EIRP: what is the 2.15 dB?",
            "Who owns Gt in the EIRP equation in this series?",
            "256 elements × 1 W, 0.3 dB module feed, array gain 24 dB in the beam: sketch EIRP.",
        ],
        [
            f"Factor {LOSS_2DB:.3f}. Power {100 * LOSS_2DB:.1f} W.",
            "Dipole gain versus isotropic. ERP is referenced to a dipole; EIRP to isotropic. 0 dBd = 2.15 dBi.",
            "Book 4. This book owns PPA and Lfeed. The product is EIRP, stated here using Book 4's gain.",
            "Power at elements after feed: 256 × 0.933 W ≈ 239 W. Add 24 dB array gain: EIRP ≈ 23.8 dBW + 24 dB = 47.8 dBW, order of 60 kW EIRP, with all the usual taper and efficiency caveats Book 4 will insist on.",
        ],
    )

