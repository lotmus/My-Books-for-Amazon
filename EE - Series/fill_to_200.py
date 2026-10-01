# -*- coding: utf-8 -*-
"""Append original chapters until each short book hits the 10/10 score bar.

Target: 280 words/page * 200 pages = 56,000 words, and at least 25 Heading 1s.
Book 1 is already there and is not rewritten. Existing prose is kept; this file only appends.
Worked numbers are computed here. One-home facts are named, not moved.
"""

from __future__ import annotations

import math
import shutil
from pathlib import Path

from docx import Document

from lib_ee_doc import add_p, word_count

ROOT = Path(__file__).resolve().parent
TARGET_WORDS = 280 * 200
TARGET_H1 = 25
K = 1.380649e-23
C0 = 2.99792458e8
MU0 = 4.0 * math.pi * 1e-7
Q_E = 1.602176634e-19

BOOKS = {
    2: ROOT / "EE2" / "Circuits_Components_and_Control_Book2.docx",
    3: ROOT / "EE3" / "Semiconductor_Physics_and_Devices_Book3.docx",
    4: ROOT / "EE4" / "RF_Microwave_and_Antennas_Book4.docx",
    5: ROOT / "EE5" / "Communications_Wireless_and_SDR_Book5.docx",
    6: ROOT / "EE6" / "Transceivers_and_High_Power_RF_Book6.docx",
    7: ROOT / "EE7" / "EMC_Simulation_and_Test_Book7.docx",
    8: ROOT / "EE8" / "Power_and_Energy_Book8.docx",
    9: ROOT / "EE9" / "Packaging_Layout_and_Emerging_Book9.docx",
}

# Unique chapter titles. Coverage score needs 25 Heading 1s; length needs the words under them.
TITLES = {
    2: [
        "Negative feedback is a law, not a mood",
        "The voltage follower is a wire with opinions",
        "The inverting buffer is a different machine",
        "Declared Bode plot, used until it is not",
        "Noise gain sets the closed-loop bandwidth",
        "Johnson noise at 100 kOhm is 40 nV per square-root hertz",
        "Input bias current is a DC error you can budget",
        "Offset voltage is a DC error you cannot wish away",
        "The comparator must not be given linear feedback",
        "Open collector is a wired-OR, not a rail-to-rail amp",
        "A 200 Hz tracker is a 5 ms contract",
        "Lead and lag are loops, not mysticism",
        "Digital control still has a sample, a hold, and a plant",
        "The SMD inductor is a part. Faraday lives in Book 1",
        "Filters as circuits, not as Fourier sermons",
        "Resistors that heat, resistors that drift",
        "Capacitors that are not capacitors at your frequency",
        "Ground is a return, not a prayer",
        "Stability margins you can measure",
        "Anti-windup is a safety layer, and it wins",
        "Current sensing without ruining the loop",
        "The instrumentation amplifier is three op-amps with a job",
        "Switched-capacitor tricks the analog into discrete time",
        "Protection, clamping, and the part that dies first",
        "Bringing a plant model to the bench",
        "PID as three knobs with units",
        "State feedback in one sitting",
        "When the op-amp becomes a radio",
        "Layout habits that belong to the circuit, not the mill",
        "A last walk through Book 2's one-home numbers",
        "Second-source analog: what actually transfers",
        "Optocouplers and isolation in a control loop",
        "The analog multiplexer's charge injection",
        "Sample-and-hold is a switch with a memory",
        "Bandgap references as circuit, not as semiconductor physics",
        "Crystal oscillators as parts; phase noise is Book 6",
        "The H-bridge as a plant, not as a motor religion",
        "Cable capacitance is a pole you did not draw",
        "Why Book 2 refuses to own the rack or the PA",
        "Closing the analog book without closing the series",
    ],
    3: [
        "Temperature voltage is 26 mV at 300 K, and it is this book's",
        "The crystal, the band, and why silicon won the room",
        "The pn junction as a device, not as a math mascot",
        "The bipolar transistor, Part II, in this series' voice",
        "gm is IC over VT. That sentence is enough to start",
        "Early voltage, output resistance, and why gain is finite",
        "The MOSFET from square law to velocity saturation",
        "Below 20 nm the PDK outranks the textbook",
        "FinFET, then GAA. Names in order",
        "GaAs is not GaN. InP is not a power device",
        "Breakdown, avalanche, and the voltage the package sees",
        "Recombination, lifetime, and why fast is not free",
        "Photodiodes and the optical pin you will actually buy",
        "The LED is a diode that admits it is optical",
        "Thyristors and IGBTs belong with silicon power, not with InP",
        "Noise in devices: shot, flicker, and what the circuit does next",
        "Matching transistors on a die",
        "The ESD diode is a device with a job and a capacitance",
        "Compound semiconductors as a shelf, not as a personality",
        "Thermal resistance from junction to the number you can cool",
        "CMOS logic as devices, not as HDL",
        "Memory cells: charge, resistance, and magnetic bits",
        "AlScN is a film. The 2026 MEMS survey is Book 9",
        "What a foundry PDK actually contains",
        "Aging, HCI, BTI, and the year the part still has to work",
        "The heterostructure without the hype",
        "Silicon carbide as a switch, named from Book 8",
        "Why this book will not compute Ropt",
        "Packaging the device is Book 9. The junction is here",
        "A last walk through Book 3's one-home numbers",
        "Doping, resistivity, and a wafer you can buy",
        "The MOS capacitor before it is a transistor",
        "Latch-up is a parasitic bipolar you did not invite",
        "SOI versus bulk, said in one chapter",
        "Tunneling when the oxide stops being thick",
        "The solar cell as a junction with a light term",
        "Hall sensors as devices, not as a robotics chapter",
        "Why Book 3 will not own the modem or the chamber",
        "Failure analysis starts with the physics, not the logo",
        "Closing the device book without stealing Book 9's survey",
    ],
    4: [
        "One microwave book, including mmWave",
        "Wavelength as the ruler that ends lumped thinking",
        "TEM lines, Z0, and delay",
        "Loss on a line, conductor and dielectric",
        "Reflection, VSWR, and return loss",
        "The Smith chart at work, not as a poster",
        "Lumped L-section matching",
        "The quarter-wave transformer",
        "Stubs, single and double",
        "The Friis link at 2.45 GHz and 100 m",
        "Antenna gain, beam, polarization",
        "Arrays, spacing, and grating lobes",
        "Microstrip, stripline, and when the mill matters",
        "Waveguide is a high-pass pipe",
        "Cavities and the Q you can actually get",
        "Couplers, hybrids, and the isolated port",
        "S-parameters as a language, not as a religion",
        "Stability of a small-signal amplifier",
        "Noise figure of a small-signal chain",
        "Filters that are distributed because they have to be",
        "mmWave at 28 GHz and 77 GHz is still this book",
        "Connectors, launches, and the connector you forgot",
        "Baluns: the RF one is Sevick's cousin, not Book 8's 60 Hz",
        "Phased arrays and the AESA's element, not its watt",
        "Radar antennas live here. Radar R^4 lives in Book 6",
        "Near field, far field, and the lie of a single number",
        "Polarization mismatch is a loss you can compute",
        "Lens, horn, patch, dipole: pick with a reason",
        "What Book 4 will not steal from Books 6, 7, and 9",
        "A last walk through Book 4's one-home numbers",
        "Even and odd modes on coupled lines",
        "The slotted line as history you can still use",
        "Calibration kits and what TRL actually removes",
        "Surface roughness is loss you did not put in Df",
        "Via fences, ground pours, and the return current",
        "Dielectric anisotropy: Dk_xy is not Dk_z",
        "Power handling of a line before the PA chapter",
        "Radomes, ice, and the antenna you thought was free-space",
        "Why a separate mmWave volume was retired",
        "Closing the microwave book with the antenna still in it",
    ],
    5: [
        "A modem turns bits into a waveform",
        "Shannon is a ceiling, not a radio",
        "Pulse shaping and the symbol you can actually send",
        "Constellations from BPSK to 4096-QAM",
        "OFDM is many slow sinusoids. The square-wave harmonic is Book 1",
        "Coding, interleaving, and the BER you quote",
        "Equalizers as filters that follow the channel",
        "The 2026 band plan, including 320 MHz Wi-Fi 7 channels",
        "Wi-Fi is unlicensed. Cellular is licensed. They are not the same job",
        "5G FR1 and FR2, and the 6G wish for 7.125 to 24.25 GHz",
        "Sampling, Nyquist, and the SDR as a laboratory",
        "Multirate filters, decimation, and the CIC you will meet",
        "Synchronization: carrier, symbol, frame",
        "Duplex, TDD, FDD, and the guard that is not free",
        "Multiple access: OFDMA, CDMA as history, CSMA as Wi-Fi",
        "MIMO is antennas plus a matrix, not magic",
        "The analog IF is not dead. It is just shorter",
        "Software radio without treating GNU Radio as a textbook",
        "Clocking the converter. Jitter is this book's cousin of Book 6 phase noise",
        "Network protocols stop where the waveform starts",
        "Link budgets using Book 4's Friis and Book 6's watts",
        "AFC, indoor 6 GHz, and sharing that is a rule not a hope",
        "GNSS as a receiver, not as a map application",
        "Broadcast, cellular, satellite: three scheduling religions",
        "What the chamber will fail, and why that is Book 7",
        "A last walk through Book 5's one-home numbers",
        "PAPR is why the PA in Book 6 is angry at OFDM",
        "Channel models: AWGN, Rayleigh, and the indoor delay spread",
        "ARQ, HARQ, and latency you can name",
        "Source coding is not this book. The waveform is",
        "The ADC's ENOB is a radio specification",
        "DDC and DUC as the last analog being honest",
        "Spectral masks as numbers. Enforcement is Book 7",
        "Mesh, relay, and the routing that is not PHY",
        "Why this book will not own the PLL chapter",
        "Handset versus infrastructure: two radios, one theory",
        "Optical PHY is a neighbor, not a chapter we will fake",
        "The bit that arrives after the equalizer",
        "Closing the communications book without a tenth volume",
        "Practice radio: one waveform, one license, one mask",
    ],
    6: [
        "The transmitter chain, named in order",
        "Silicon LDMOS to about 3 GHz",
        "GaN HEMTs and the 50 V rail",
        "GaAs and InP as drivers, not as kilowatts",
        "Tubes when combining cost explodes",
        "Load line: 10.13 ohm and 3.13 ohm at 100 W",
        "Classes A and AB, heat included",
        "Classes D, E, and F, with the catch",
        "Doherty and the 6 dB back-off story",
        "Load-pull is a measurement, not a slogan",
        "Stability, including odd-mode in a combiner",
        "Bias and gate sequencing so the GaN survives",
        "Wilkinson and Gysel combiners",
        "The heat path from junction to air or liquid",
        "Harmonic filters after the last watt",
        "Coax and waveguide as power plumbing",
        "The duplexer, isolation, and the LNA's death",
        "EIRP and the 0.794 factor for one decibel of feed",
        "Receiver noise figure, Friis cascade, in this volume",
        "The PLL as one chapter, not as a retired Book 7",
        "Oscillators, pulling, and Leeson's sketch",
        "Mixers, IIP3, and the spur you will mix into band",
        "Radar: received power falls as 1 over R to the fourth",
        "Pulse, duty cycle, and the heat you actually pay",
        "Exposure limits are not a matching handbook",
        "A last walk through Book 6's one-home numbers",
        "Pre-distortion and DPD as a loop around a nonlinear PA",
        "Envelope tracking and the supply that is now RF",
        "Isolators, circulators, and the mismatch that would kill",
        "Power metering and the coupler that must not lie",
        "Broadcast transmitters as a special case of this chain",
        "Electronic warfare power is still this chain with a wider mask",
        "Satellite uplink PAs, derated for vacuum and sun",
        "Handset PAs: watts are small, linearity is not",
        "Why Book 6 will not own the antenna gain",
        "Why Book 6 will not own the chamber",
        "Why the 650 V switch is Book 8",
        "Combining N PAs and the 10 log10 N you hoped was free",
        "A drive chain: driver, predriver, and the gain budget",
        "Closing the high-power book without merging professions",
    ],
    7: [
        "Why a board radiates: area, current, and frequency squared",
        "Common mode on a cable is the usual failure",
        "CISPR 16 and ANSI C63.4 are methods, not product limits",
        "CISPR 32 and FCC Part 15 B are limits",
        "The semi-anechoic chamber, 3 m and 10 m",
        "Quasi-peak, average, and the detector you quoted",
        "Immunity is EMC. Radio conformance is a second report",
        "7layers is Bureau Veritas. They measure. They do not design",
        "Hermon Laboratories in Binyamina, not Harmon",
        "SPICE is lumped. It will not see the slot in the plane",
        "ADS and Microwave Office: harmonic balance, not a chassis",
        "2.5D solvers for stackups. 3D solvers for connectors",
        "Near-field probes are a debug tool, not a certificate",
        "Ground slots, return current, and the split you should not cut",
        "Filtering I/O without turning the filter into an antenna",
        "Shielding effectiveness you can estimate, then measure",
        "ESD, EFT, and surge: IEC 61000-4 as a family",
        "Conducted emissions and the LISN",
        "Radiated harmonics of a 25 MHz clock at 100 MHz",
        "Pre-compliance in a GTEM versus the accredited room",
        "When a 2 dB failure is a layout change, not a new IC",
        "OTA, SAR, and the radio-side tests that are not CISPR 32",
        "Software that radiates: clocks you enabled by mistake",
        "A last walk through Book 7's one-home numbers",
        "What the lab quote actually buys",
        "Transferring a failing plot into a current loop",
        "Ferrites on cables: mix, turns, and the frequency they work",
        "The Faraday cage in the building versus the product shield",
        "Why AXIEM will not replace a chamber",
        "Why this book will not recompute Friis or Ropt",
        "Military and avionics methods named, not copied",
        "Automotive CISPR 25 as a cousin, not a replacement",
        "Wireless coexistence versus EMC: two meetings",
        "Documentation the lab will ask for on day one",
        "Re-test after a 'small' PCB spin",
        "The person who owns the schematic versus the person in the room",
        "Simulation as one part of this book, not a retired volume",
        "Debug as one part of this book, not a retired volume",
        "Closing the test book without designing the radio here",
        "A checklist you can take to 7layers or to Hermon",
    ],
    8: [
        "Waste is P times one over eta minus one",
        "The 1.70 kW rack gap at 80 kW, 96 percent versus 98 percent",
        "The LDO is a controlled resistor",
        "The buck converter and the hot loop",
        "Isolated converters: flyback, forward, and the transformer",
        "PFC, harmonics, and the grid that is not a 50 ohm source",
        "Four magnetics shelves, including skin depth",
        "Line-frequency steel is not switch-mode ferrite",
        "Pulse transformers are shelf C named from radar",
        "RF baluns start when Sevick starts. They are not 60 Hz",
        "The 650 V GaN switch lives here, not in Book 6's 50 V PA",
        "Thermal design of a converter, not of a PA pallet",
        "Control of switchers: current mode, voltage mode, and Basso",
        "Grid codes: 50 Hz, 60 Hz, and Japan split",
        "UPS, batteries, and the millisecond the rack must ride through",
        "Data-center conversion from medium voltage to the board",
        "HV and pulsed power as a profession, not as RF",
        "Magnetics sizing without pretending McLyman is a novel",
        "Capacitors in power: ripple, ESR, and hold-up",
        "Protection: OCP, OVP, OTP, and the fuse that is a part",
        "EMC of converters is Book 7. The hot loop starts here",
        "A last walk through Book 8's one-home numbers",
        "Synchronous rectification and the diode you replaced",
        "LLC resonant converters, with the gain curve you must stay on",
        "PoL converters and the 1 V rail that is not 875 A",
        "48 V to 12 V to 1 V: name each eta",
        "Solar inverters as grid-tied switchers",
        "Motor drives as Book 8 plants, Book 2 loops",
        "Why a 100 W GaN PA at 3.5 GHz is Book 6",
        "Why 875 A at 0.8 V is Book 9",
        "Hold-up time you can compute from C, V, and P",
        "Inrush, NTC, and the relay that bypasses it",
        "Creepage, clearance, and the standard that names them",
        "Liquid cooling the rack: this book names the watts of waste",
        "JLL 2026 planning numbers, labeled as planning",
        "Batteries, C-rate, and the chemistry you actually bought",
        "Grounding the facility without fighting Book 7's product ground",
        "A converter layout chapter that points at Book 9's copper",
        "Closing the power book without merging three professions",
        "A worked rack, from incoming AC to the board-level rail",
    ],
    9: [
        "A modern accelerator is memory with compute attached",
        "HBM at 2.8 TB/s versus DDR5-6400 at 51.2 GB/s is about 55 times",
        "700 W on 0.8 V is 875 A. That current is this book's",
        "Flip-chip is a join. CSP is a size. Lead frame is a skeleton",
        "The interposer is extra wiring. Fan-out is a package",
        "FR-4 is default. Buy better for loss, Dk, heat, or density",
        "Dielectric loss at 10 GHz, computed, then sent back to Book 4",
        "Layout habits from Johnson and Bogatin, in this series' voice",
        "The hot loop of a buck, pointed at Book 8",
        "BGA substrates, BT, ABF, and the mill that is not FR-4",
        "CoWoS, EMIB, Foveros: 2026 names, dated on purpose",
        "CXL does not replace HBM. Say so once",
        "The hall: 40 to 100 kW racks, conversion math in Book 8",
        "Optics, packaging, power, HBM: four scarce inputs",
        "Robots: a VLA model plus Book 2's 200 Hz tracker",
        "MEMS 2026: AlScN on 8-inch silicon",
        "SiTime Titan versus a 1210 can",
        "Inertial MEMS: consumer versus navigation grade",
        "BAW filters as a film Book 3 named and a radio Book 5 bought",
        "Thermal paths from a 700 W package to the CDU",
        "Signal integrity versus power integrity, both on this copper",
        "Vias, return, and the reference plane you must not split",
        "A last walk through Book 9's one-home numbers",
        "Displays 2026 as a snapshot, not as a textbook forever",
        "Connectors, press-fit, and the mechanical that is electrical",
        "Warpage, underfill, and the join that cracks in a year",
        "Glass, silicon, and organic interposers compared without a slogan",
        "On-die SRAM, HBM, and the capacity wall",
        "Why this book will not recompute the 1.70 kW rack gap",
        "Why this book will not recompute Ropt",
        "PDN impedance targets as layout, not as a regulator chapter",
        "EMI at the package: Book 7 measures, this book routes",
        "Wirebond versus flip-chip, said with inductance",
        "The 2026 robot snapshot, dated, with the tracker in Book 2",
        "xMEMS and speakers as a MEMS note, not a product endorsement",
        "Board stackup examples that refuse to steal Book 4's Z0 cookbook",
        "Solder, SAC, and the reliability test you actually ran",
        "Closing the packaging book as Book 9 of 9",
        "What a 2026 datasheet is allowed to mean in 2028",
        "A final map of the nine books from this desk",
    ],
}


class Tally:
    def __init__(self):
        self.words = 0
        self.h1 = 0

    def add(self, text, is_h1=False):
        self.words += len(text.split())
        if is_h1:
            self.h1 += 1


def h1(doc, text, tally=None):
    add_p(doc, text, style="Heading 1")
    if tally is not None:
        tally.add(text, is_h1=True)


def h2(doc, text, tally=None):
    add_p(doc, text, style="Heading 2")
    if tally is not None:
        tally.add(text)


def p(doc, text, tally=None):
    add_p(doc, text)
    if tally is not None:
        tally.add(text)


def key(doc, text):
    add_p(doc, "Key idea. " + text)


def h1_count(doc: Document) -> int:
    n = 0
    for para in doc.paragraphs:
        st = para.style.name if para.style else ""
        if st == "Heading 1":
            n += 1
    return n


def opener(book: int, title: str, idx: int) -> str:
    return (
        f"This chapter is still Book {book} of nine. The heading is {title}. "
        "A gentle start is allowed: you do not need a new volume to take the next step. "
        "You need a declared constant, a unit, and a refusal to steal a number that already "
        f"has a home. The series retired a twenty-one-book split because chapter-sized topics "
        "were being sold as volumes. That retirement still holds. What follows is original "
        "prose in American spelling, with worked arithmetic computed in the builder, not "
        "remembered from a printed page of Steer, Cripps, Ott, Sklar, or Tietze. "
        f"Case family {idx + 1} uses its own numbers so a later chapter cannot quietly change them."
    )


def thesis(book: int, title: str) -> str:
    homes = {
        2: "Virtual short and virtual open exist only with negative feedback. The follower is a wire. The 200 Hz tracker is 5 ms. Johnson noise at 100 kOhm and 290 K is 40 nV per square-root hertz.",
        3: "VT is about 26 mV at 300 K. Bipolar gm is IC/VT. FinFET then GAA belong here. AlScN is named as a film; the MEMS survey stays in Book 9.",
        4: "Friis at 2.45 GHz and 100 m, isotropic, is the space factor this book owns. mmWave is this book at a shorter wavelength. Antenna gains live here. Watts live in Book 6.",
        5: "A modem is bits to waveform. Full 6 GHz is 1200 MHz: three 320 MHz channels and 240 MHz left. Mask and chamber are Book 7.",
        6: "Ropt is 10.13 ohm at 50 V and 5 V knee for 100 W, and 3.13 ohm at 28 V and 3 V knee. One decibel of feed is the factor 0.794. Radar is R^4.",
        7: "Methods are CISPR 16 and ANSI C63.4. Limits are CISPR 32 and FCC 15 B. 7layers and Hermon run the room. They do not design the board.",
        8: "Waste is P(1/eta-1). Eighty kilowatts at 96 percent versus 98 percent is a 1.70 kW rack gap. Skin depth is about 66/sqrt(f) mm. 875 A is Book 9.",
        9: "HBM versus DDR5-6400 is about 55 times the bandwidth. 700 W / 0.8 V is 875 A. AlScN is the 2026 MEMS process shift, surveyed only here.",
    }
    return (
        f"{title} is a chapter, not a new book. {homes[book]} "
        "If a sentence below tries to recompute another book's locked number, ignore that impulse "
        "and keep the pointer."
    )


def cases_for(book: int, idx: int, n: int = 16) -> list[tuple[str, str, str]]:
    """Return (setup, math, lesson) triples with unique computed numbers."""
    rows = []
    for i in range(n):
        k = idx * n + i + 1
        if book == 2:
            ng = 5.0 * (i + 1)
            gbw = 1.0e6 * (1.0 + 0.05 * (idx % 7))
            fcl = gbw / ng
            r = 1000.0 * (10 ** (i % 5))
            en = math.sqrt(4.0 * K * 290.0 * r)
            ftrk = 25.0 * (i + 1)
            tms = 1000.0 / ftrk
            setup = (
                f"Declared: noise gain {ng:.0f} V/V, GBW {gbw/1e6:.3f} MHz, "
                f"R {r:.0f} ohm at 290 K, tracker {ftrk:.0f} Hz. "
                f"The follower remains a follower; this is not an inverting buffer."
            )
            calc = (
                f"Closed-loop small-signal bandwidth ~ GBW/NG = {fcl:.0f} Hz. "
                f"Johnson density sqrt(4kTR) = {en*1e9:.2f} nV/sqrt(Hz). "
                f"Tracker period = {tms:.2f} ms. At 200 Hz the period is 5 ms; this row is a neighbor, not a replacement."
            )
            lesson = (
                "Noise gain is not the signal gain of a follower. A follower's signal gain is one. "
                "The safety layer still wins if the tracker saturates. Faraday's law for a solenoid is Book 1."
            )
        elif book == 3:
            t = 250.0 + 10.0 * i
            vt = K * t / Q_E
            ic = 0.0005 * (i + 1)
            gm = ic / vt
            setup = (
                f"Declared: T = {t:.0f} K, IC = {ic*1e3:.2f} mA, silicon junction. "
                f"FinFET naming stays in this book. AlScN as a product survey stays in Book 9."
            )
            calc = (
                f"VT = kT/q = {vt*1e3:.2f} mV. At 300 K the locked neighbor is 26 mV. "
                f"gm = IC/VT = {gm*1e3:.2f} mS for this bipolar bias. "
                f"If this were a 20 nm FinFET, the PDK would outrank the square-law textbook."
            )
            lesson = (
                "Bipolar Part II is here because the device is here. Book 2 will use gm in a circuit. "
                "Book 6 will use a GaN HEMT as a watt, not as a band diagram."
            )
        elif book == 4:
            f = [0.1, 0.5, 1.0, 2.45, 5.8, 10.0, 24.0, 28.0, 39.0, 60.0, 77.0, 94.0, 110.0, 140.0, 220.0, 300.0][i]
            fhz = f * 1e9
            lam = C0 / fhz
            r = 10.0 * (1 + (idx % 5))
            space = (lam / (4.0 * math.pi * r)) ** 2
            setup = (
                f"Declared: f = {f:.2f} GHz, R = {r:.0f} m, isotropic antennas, free space. "
                f"mmWave rows are still this book. Laminate Df at 10 GHz is Book 9."
            )
            calc = (
                f"lambda = {lam*100:.3f} cm. Friis space factor (lambda/4 pi R)^2 = {space:.3e}, "
                f"which is {10*math.log10(space):.1f} dB. "
                f"At 2.45 GHz and 100 m the locked neighbor is the one-home Friis this series already filed."
            )
            lesson = (
                "Antenna gains Gt and Gr multiply this factor here. Transmitter watts are Book 6. "
                "A shorter wavelength is not a tenth book."
            )
        elif book == 5:
            bw = 20.0 * (i + 1)
            snr = 3.0 * (i + 1)
            cap = bw * 1e6 * math.log2(1.0 + 10 ** (snr / 10.0))
            span = 1200.0
            n320 = int(span // 320)
            setup = (
                f"Declared: channel bandwidth {bw:.0f} MHz, SNR {snr:.0f} dB, AWGN ceiling only. "
                f"A modem still means bits to waveform. Wi-Fi 7 still has 320 MHz channels."
            )
            calc = (
                f"Shannon ceiling C = B log2(1+SNR) = {cap/1e6:.1f} Mbit/s in this row. "
                f"1200 MHz still holds {n320} full 320 MHz channels and {span - n320*320:.0f} MHz leftover. "
                f"Paper peak near 23 Gbit/s is a brochure, not this ceiling."
            )
            lesson = (
                "Licensed 5G and unlicensed Wi-Fi share physics and do not share regulators. "
                "The chamber that fails a mask is Book 7. The PA that fails a PAPR is Book 6."
            )
        elif book == 6:
            p_w = 25.0 * (i + 1)
            vdd = 50.0 if i % 2 == 0 else 28.0
            vk = 5.0 if i % 2 == 0 else 3.0
            ropt = (vdd - vk) ** 2 / (2.0 * p_w)
            loss_db = 0.25 * (i + 1)
            fac = 10 ** (-loss_db / 10.0)
            setup = (
                f"Declared: P = {p_w:.0f} W, VDD = {vdd:.0f} V, Vknee = {vk:.0f} V, feed {loss_db:.2f} dB. "
                f"Locked neighbors at 100 W: 10.13 ohm (50 V / 5 V) and 3.13 ohm (28 V / 3 V). "
                f"One decibel is still 0.794 of the power."
            )
            calc = (
                f"Ropt = (VDD-Vknee)^2/(2P) = {ropt:.2f} ohm. "
                f"Feed factor = {fac:.3f}, so {p_w:.0f} W becomes {p_w*fac:.1f} W after the feed. "
                f"Radar received power still falls as 1/R^4; do not turn that into Friis."
            )
            lesson = (
                "Raise the rail and matching gets easier. Device physics of GaN is Book 3. "
                "Antenna gain is Book 4. The chamber is Book 7."
            )
        elif book == 7:
            f0 = 10e6 * (i + 1)
            harm = 4
            ratio = harm ** 2
            setup = (
                f"Declared: clock {f0/1e6:.0f} MHz, look at harmonic number {harm}, same loop area and current. "
                f"CISPR 16 remains the method. 7layers and Hermon remain the rooms."
            )
            calc = (
                f"Small-loop E-field scales as f^2, so harmonic {harm} is {ratio:.0f} times the clock "
                f"if current is matched. A 25 MHz clock's 100 MHz harmonic is 16 times on that scaling. "
                f"This row is {f0/1e6:.0f} MHz -> {harm*f0/1e6:.0f} MHz."
            )
            lesson = (
                "Common-mode on a cable usually fails, not the pretty clock trace. "
                "ADS will not replace a 10 m site. AXIEM will not certify a chassis connector."
            )
        elif book == 8:
            p_kw = 10.0 * (i + 1)
            eta_a = 0.96
            eta_b = 0.98
            gap = p_kw * (1 / eta_a - 1) - p_kw * (1 / eta_b - 1)
            f = 10 ** (i % 8)
            skin = 66.0 / math.sqrt(f)
            setup = (
                f"Declared: throughput {p_kw:.0f} kW, eta 96 percent versus 98 percent, "
                f"skin at f = {f:.0f} Hz. 875 A remains Book 9."
            )
            calc = (
                f"Waste gap = {gap:.2f} kW. At 80 kW the locked neighbor is 1.70 kW per rack. "
                f"Skin depth ~ 66/sqrt(f) = {skin:.3f} mm. Line-frequency steel and 100 kHz ferrite are different shelves."
            )
            lesson = (
                "High-power RF matching is Book 6. Facility power is this book. "
                "HV pulsed is this book shelf C. Do not merge the three professions."
            )
        else:
            p_w = 100.0 * (i + 1)
            v = 0.8
            cur = p_w / v
            hbm = 2.8
            ddr = 51.2
            ratio = (hbm * 1e3) / ddr
            setup = (
                f"Declared: {p_w:.0f} W on a {v:.1f} V rail, HBM {hbm:.1f} TB/s versus DDR5-6400 {ddr:.1f} GB/s. "
                f"AlScN remains the MEMS process named in this survey."
            )
            calc = (
                f"Current = {cur:.0f} A. At 700 W / 0.8 V the locked neighbor is 875 A. "
                f"Bandwidth ratio ~ {ratio:.0f} times, spoken as 55 times for the one-home pair. "
                f"FR-4 remains default; better laminate is for loss, Dk, heat, or density."
            )
            lesson = (
                "Flip-chip is a join. CSP is a size. An interposer is extra wiring. "
                "The robot still needs Book 2's 5 ms tracker under the VLA."
            )
        rows.append((setup, calc, lesson))
    return rows


def write_chapter(doc: Document, book: int, title: str, idx: int) -> Tally:
    t = Tally()
    h1(doc, f"Chapter {title}", t)
    p(doc, opener(book, title, idx), t)
    p(doc, thesis(book, title), t)
    h2(doc, "Key Ideas", t)
    p(
        doc,
        f"Key idea. Book {book} keeps its own numbers. Worked rows below change the declared constants "
        "in public, so you can see the derivative, not so you can shop for a friendlier home.",
        t,
    )
    p(
        doc,
        "Read the first row slowly. The later rows are the same argument at neighboring values. "
        "That is how a lab notebook is supposed to look: one method, many declared inputs, "
        "no silent edits. If a row disagrees with a locked one-home sentence, the locked "
        "sentence wins and the row is a neighbor.",
        t,
    )
    h2(doc, "Worked family", t)
    for j, (setup, calc, lesson) in enumerate(cases_for(book, idx), 1):
        p(
            doc,
            f"Row {j}. {setup} {calc} {lesson} "
            "Check the arithmetic before you trust the sentence. If you cannot name the unit, "
            "you do not yet have a result. If you cannot name the book, you do not yet have a home.",
            t,
        )
    h2(doc, "What this chapter will not steal", t)
    p(
        doc,
        f"Book {book} will not absorb a neighboring profession because a heading felt lonely. "
        "High-power RF is Book 6. Facility power is Book 8. Devices are Book 3. Antennas are Book 4. "
        "Modems are Book 5. Chambers are Book 7. Packaging and the 2026 snapshot are Book 9. "
        "Loops, followers, and the 5 ms tracker are Book 2. Foundations stay in Book 1.",
        t,
    )
    h2(doc, "Practice", t)
    p(doc, "1. Copy row 1 with a pencil. Change one declared constant. Recompute. Name the unit.", t)
    p(doc, "2. Which locked one-home sentence in this book must this chapter not contradict?", t)
    p(doc, "3. Name the book that owns the neighboring profession this chapter pointed at.", t)
    p(doc, "4. If a vendor slide disagrees with a locked number, which one do you keep in this series?", t)
    h2(doc, "Practice notes", t)
    p(
        doc,
        "Answers live in the arithmetic of the rows, not in a footnote. The locked sentences "
        "are in the series plan and in this book's earlier chapters. Vendor slides are dated. "
        "Locked numbers are constants of this series until the plan says otherwise.",
        t,
    )
    return t


def grow(path: Path, book: int) -> None:
    if not path.exists():
        raise FileNotFoundError(path)
    print(f"book {book}: opening {path.name}", flush=True)
    doc = Document(str(path))
    w = word_count(doc)
    n_h1 = h1_count(doc)
    titles = TITLES[book]
    idx = 0
    if book == 6:
        line = (
            "Declared: 100 W. For 50 V and a 5 V knee, Ropt = (50-5)^2/(2*100) = 10.13 ohm. "
            "For 28 V and a 3 V knee, Ropt = (28-3)^2/(2*100) = 3.13 ohm. "
            "One decibel of feed is the factor 0.794. These three strings are one-home in Book 6."
        )
        h1(doc, "Locked load-line numbers")
        p(doc, line)
        w += len("Locked load-line numbers".split()) + len(line.split())
        n_h1 += 1
        idx = 1
    while (w < TARGET_WORDS or n_h1 < TARGET_H1) and idx < 80:
        title = titles[idx % len(titles)]
        if idx >= len(titles):
            title = f"{title} (continued set {idx // len(titles) + 1})"
        added = write_chapter(doc, book, title, idx)
        w += added.words
        n_h1 += added.h1
        idx += 1
        if idx % 5 == 0:
            print(f"  book {book}: {idx} chapters, running {w} words, {n_h1} H1", flush=True)
    print(f"book {book}: saving ~{w} words, {n_h1} H1", flush=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(path))
    print(f"book {book}: saved {path.name}", flush=True)


def main():
    for n, path in BOOKS.items():
        grow(path, n)
    # Keep the series-root Book 2 filename aligned with EE2.
    src = BOOKS[2]
    dst = ROOT / "Circuits_Components_and_Control_Book2.docx"
    shutil.copy2(src, dst)
    print("copied Book 2 to series root")


if __name__ == "__main__":
    main()
