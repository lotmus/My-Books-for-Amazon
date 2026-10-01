# -*- coding: utf-8 -*-
"""Build Book 3, Part I. Numbers in the prose come from this file."""

import math
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

OUT = Path(__file__).resolve().parent / "Semiconductor_Physics_and_Devices_Book3.docx"

# Working constants declared in the book. Do not "improve" them in one
# chapter and leave the others behind.
VT = 0.026  # V at room temperature, this book's hand value
NI = 1.0e10  # cm^-3, silicon, this book's hand value
Q = 1.602176634e-19  # C
EPS0 = 8.854187817e-14  # F/cm
EPS_R = 11.7
EPS_S = EPS_R * EPS0
MU_N = 1000.0  # cm^2/V/s, working value
MU_P = 480.0
IS_A = 1.0e-15  # A, the diode used in the worked examples


def fexp(x):
    return math.exp(x)


def diode_i(v, is_=IS_A, vt=VT):
    return is_ * (fexp(v / vt) - 1.0)


def vbi(na, nd, ni=NI, vt=VT):
    return vt * math.log((na * nd) / (ni * ni))


def rho_ntype(nd, mu_n=MU_N):
    sigma = Q * nd * mu_n
    return 1.0 / sigma


def fmt(x, sig=3):
    return f"{x:.{sig}g}"


def sci(x, sig=2):
    return f"{x:.{sig}e}"


# Locked examples
ND16 = 1.0e16
P_MIN = NI * NI / ND16
RHO16 = rho_ntype(ND16)
VBI_SYM = vbi(ND16, ND16)
DECADE_V = VT * math.log(10.0)
I_05 = diode_i(0.50)
I_06 = diode_i(0.60)
I_07 = diode_i(0.70)
V_1MA = VT * math.log(1.0e-3 / IS_A + 1.0)

# One-sided abrupt junction, light side ND = 1e16, V = 0
W0 = math.sqrt(2.0 * EPS_S * VBI_SYM / (Q * ND16))  # cm
# Capacitance: Cj0 = 10 pF, Vbi = VBI_SYM, VR = 5
CJ0 = 10.0e-12
CJ_5 = CJ0 / math.sqrt(1.0 - (-5.0) / VBI_SYM)

# Practice-problem answers
P1_ND = 1.0e15
P1_P = NI * NI / P1_ND
P1_RHO = rho_ntype(P1_ND)
P2_NA = 1.0e17
P2_N = NI * NI / P2_NA
P3_DN = MU_N * VT
# diffusion: n falls by 9e15 cm^-3 across 1 um = 1e-4 cm
DN_DX = -9.0e15 / 1.0e-4
J_DIFF = Q * P3_DN * abs(DN_DX)  # magnitude, A/cm^2
P4_VBI = vbi(1.0e18, 1.0e16)
P5_I = diode_i(0.65)
P6_CJ0 = 20.0e-12
P6_CJ = P6_CJ0 / math.sqrt(1.0 - (-2.0) / VBI_SYM)


def set_run_font(run, name, size_pt, bold=False, color=None):
    run.bold = bold
    run.font.name = name
    run.font.size = Pt(size_pt)
    if color is not None:
        run.font.color.rgb = color
    r = run._element
    rpr = r.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = r.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(a), name)


def shade_style(style, font, size, bold, color, align, before=0, after=8, page_break=False):
    style.font.name = font
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = color
    pf = style.paragraph_format
    pf.alignment = align
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.page_break_before = page_break
    pf.line_spacing = 1.15
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = style.element.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(a), font)


def add_p(doc, text, *, italic=False, center=False, space_after=8):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    set_run_font(run, "Calibri", 11, bold=False, color=RGBColor(0, 0, 0))
    run.italic = italic
    return p


def add_h(doc, text, level):
    doc.add_heading(text, level=level)


def build():
    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = Inches(1)
    sec.bottom_margin = Inches(1)
    sec.left_margin = Inches(1)
    sec.right_margin = Inches(1)

    normal = doc.styles["Normal"]
    shade_style(normal, "Calibri", 11, False, RGBColor(0, 0, 0), WD_ALIGN_PARAGRAPH.LEFT, after=8)
    blue = RGBColor(0x00, 0x00, 0xFF)
    shade_style(doc.styles["Heading 1"], "Amazon Ember", 18, True, blue, WD_ALIGN_PARAGRAPH.CENTER, before=0, after=12, page_break=True)
    shade_style(doc.styles["Heading 2"], "Amazon Ember", 18, True, blue, WD_ALIGN_PARAGRAPH.CENTER, before=14, after=8, page_break=False)

    # Title page has no forced break on the first heading: clear it after.
    add_p(doc, "Semiconductor Physics and Devices", center=True, space_after=4)
    # restyle that paragraph as a title
    title = doc.paragraphs[-1]
    title.runs[0].font.size = Pt(28)
    title.runs[0].bold = True
    title.runs[0].font.color.rgb = blue
    set_run_font(title.runs[0], "Amazon Ember", 28, bold=True, color=blue)

    add_p(doc, "Book 3 of the Electrical Engineering Series", center=True)
    add_p(doc, "Part I  —  The Crystal and the Diode", center=True)
    add_p(doc, "Lothar J. Musiol", center=True, space_after=18)
    add_p(
        doc,
        "Copyright © 2026 Lothar J. Musiol. Kindle edition. "
        "This file is Part I of a longer book. Parts II through VI are not in it yet.",
        center=True,
        italic=True,
    )

    add_h(doc, "How to Use This Part", 1)
    # first real chapter should page-break; the title block already used Normal.
    # Heading 1 style has page_break_before, so this heading starts a new page. Good.

    add_p(
        doc,
        "Book 1 taught the circuit laws and the passive parts. Book 2 treated a diode, "
        "a transistor, and an op-amp as blocks you could drop into a schematic. This part "
        "opens those blocks. By the end of it you can say, with a number, how many free "
        "carriers a piece of doped silicon has, why a pn junction grows a built-in voltage "
        "with nobody applying a battery, and why the phrase \"the diode turns on at 0.7 volts\" "
        "is a useful sketch and a bad physical claim.",
    )
    add_p(
        doc,
        "Two numbers are fixed for the whole part, so that a later chapter cannot quietly "
        "adopt a different room temperature. Thermal voltage VT is 26 mV. The intrinsic "
        "carrier concentration of silicon, ni, is 1.0×10^10 per cubic centimeter. Real tables "
        "scatter a little around both of those, because the bandgap model and the exact "
        "temperature move them. Hand work in this book uses the declared pair. When a vendor "
        "model quotes a different ni, use the vendor number for that part and keep this pair "
        "for the teaching problems.",
    )
    add_p(
        doc,
        "Electron and hole mobilities depend on doping and temperature. Whenever a problem "
        "in this part does not hand you a mobility, use μn = 1000 cm²/V·s and μp = 480 cm²/V·s. "
        "Those are round working values for lightly doped silicon near room temperature, not "
        "a promise about a particular wafer.",
    )
    add_p(
        doc,
        "Later parts of this book take up the bipolar transistor, the MOSFET, the inside of "
        "an op-amp, and CMOS gates. The circuit check for those parts is Tietze, Schenk, and "
        "Gamm, Halbleiter-Schaltungstechnik, 16th edition (2019), whose op-amp chapter was "
        "rewritten for that edition. High-speed boards, radio layout, switching regulators, "
        "and software-defined radio are later books in this series. They are named in the "
        "series plan so this part does not pretend to cover them.",
    )

    add_h(doc, "Chapter 1. A Crystal That Can Be Talked Into Conducting", 1)
    add_p(
        doc,
        "Window glass and a processor die both contain silicon. One of them sits in a wall "
        "and refuses to carry a current you would bother to measure. The other switches "
        "billions of times a second because a small voltage was allowed to decide how many "
        "charges are free to move. The difference is not a mystery metal. It is how pure the "
        "crystal is, and which few atoms you deliberately put in.",
    )
    add_h(doc, "1.1 Three ways a solid treats its electrons", 2)
    add_p(
        doc,
        "A useful picture, good enough for every circuit in this series, sorts solids by the "
        "energy gap between the last filled band of electron states and the next empty one. "
        "In a metal the bands overlap, so a tiny electric field finds electrons already free "
        "to drift. In a good insulator the gap is several electron-volts wide, and ordinary "
        "voltages do not lift electrons across it. Silicon sits in between. Its gap is about "
        "1.12 eV at room temperature. Germanium is narrower, about 0.66 eV, which is why a "
        "germanium junction leaks more when the board gets warm. Gallium arsenide is wider, "
        "about 1.42 eV. Silicon carbide, used where the voltage and the heat are both high, "
        "is wider still, a few electron-volts depending on the crystal form. Silicon won the "
        "ordinary chip not because its gap is magical, but because the industry learned to "
        "grow it as a nearly perfect crystal and to put an excellent insulator, silicon dioxide, "
        "on top of it.",
    )
    add_h(doc, "1.2 Intrinsic means almost empty", 2)
    add_p(
        doc,
        "In a perfect silicon crystal at absolute zero, every bond is full and no charge "
        "moves. At room temperature a few electrons have enough thermal energy to break a "
        "bond. Each broken bond leaves an electron in the conduction band and a hole, a missing "
        "bond, in the valence band. They are created in pairs, so in pure material their "
        "concentrations are equal. That common value is ni, and this book takes it as "
        "1.0×10^10 cm⁻³.",
    )
    add_p(
        doc,
        "A cubic centimeter of silicon holds about 5×10^22 atoms. Ten billion free electrons "
        "in that same volume is a very small fraction. Intrinsic silicon is a poor conductor. "
        "The whole point of doping, in the next chapter, is to raise one of those two "
        "populations by many orders of magnitude while the other falls.",
    )
    add_h(doc, "1.3 Conductivity is charge times speed per field", 2)
    add_p(
        doc,
        "Drift current density is conductivity times electric field. For a semiconductor that "
        "still has both electrons and holes,",
    )
    add_p(doc, "σ = q (n μn + p μp)", center=True)
    add_p(
        doc,
        "where q is the elementary charge, n and p are the electron and hole concentrations, "
        "and μn and μp are the mobilities. Resistivity is 1/σ. In doped material one term "
        "usually swamps the other, which is why a resistor formula and a doped-silicon formula "
        "can look alike: both say \"lots of carriers, easy current.\"",
    )
    add_p(doc, "Key idea. Pure silicon at room temperature has very few free charges. Doping, not the word \"semiconductor\" by itself, is what makes a useful current.", italic=False)
    add_h(doc, "Worked Example 1.1", 2)
    add_p(
        doc,
        "A piece of n-type silicon is doped so that n = 1.0×10^16 cm⁻³. The hole population "
        "has already fallen to the value required by the mass-action law in Chapter 2, "
        f"p = ni²/n = {P_MIN:.1e} cm⁻³. Using this book's μn, find the resistivity. The hole "
        "term is negligible next to the electron term.",
    )
    add_p(
        doc,
        f"σ = q n μn = (1.602×10⁻¹⁹)(1.0×10^16)(1000) = {Q * ND16 * MU_N:.3f} (Ω·cm)⁻¹. "
        f"ρ = 1/σ = {RHO16:.3f} Ω·cm. A metal is a million times more conductive. This doped "
        "slice is already a practical semiconductor, and it is still nothing like copper.",
    )
    add_h(doc, "Practice", 2)
    add_p(doc, "1. Repeat Worked Example 1.1 with n = 1.0×10^15 cm⁻³ and the same mobility. Find p and ρ.")
    add_p(doc, "2. Why does a wider bandgap, all else equal, mean a smaller ni and a junction that leaks less when hot?")
    add_p(doc, "3. Intrinsic silicon has n = p = ni. Estimate σ with both mobilities. Is the hole term ignorable here, the way it was in the worked example?")

    add_h(doc, "Chapter 2. Doping, and the Partner That Gets Scarce", 1)
    add_p(
        doc,
        "Soup tastes salty after a pinch of salt, not after you have replaced the water. A "
        "semiconductor is the same kind of trick. You leave the crystal almost entirely silicon, "
        "and you swap in about one foreign atom per million, or per billion. That pinch decides "
        "whether the free charges are electrons or holes, and about how many of them there are.",
    )
    add_h(doc, "2.1 Donors and acceptors", 2)
    add_p(
        doc,
        "A column-V atom such as phosphorus has one more valence electron than silicon. Sitting "
        "on a silicon site, it completes the four bonds and has one electron left, loosely held. "
        "A little thermal energy frees that electron into the conduction band. The phosphorus "
        "atom, now positive, stays put. It donated an electron. Call its concentration ND. "
        "The material is n-type, and the electrons are the majority carriers.",
    )
    add_p(
        doc,
        "A column-III atom such as boron has one valence electron too few. It completes three "
        "bonds and borrows an electron from a neighboring bond, leaving a hole that can hop. "
        "The boron atom, now negative, stays put. Call its concentration NA. The material is "
        "p-type, and the holes are the majority carriers.",
    )
    add_h(doc, "2.2 Mass action", 2)
    add_p(
        doc,
        "In equilibrium, generation and recombination balance. The product of the two carrier "
        "concentrations is fixed by the crystal and the temperature, not by how you doped it:",
    )
    add_p(doc, "n p = ni²", center=True)
    add_p(
        doc,
        "Add donors and you raise n. The product cannot rise with it, so p falls. Add acceptors "
        "and the mirror happens. This is why a heavily doped n-type region is full of electrons "
        "and starved of holes. The starved population is still real, and it will matter as soon "
        "as a junction sweeps those minorities across a boundary.",
    )
    add_h(doc, "2.3 Charge neutrality, the short form", 2)
    add_p(
        doc,
        "A lump of semiconductor on the bench is not charged up like a capacitor plate. In the "
        "bulk, away from surfaces,",
    )
    add_p(doc, "n + NA = p + ND", center=True)
    add_p(
        doc,
        "for ionized donors and acceptors, which is the right assumption at room temperature "
        "for ordinary silicon doping. If donors dominate and ND is far above ni, then n ≈ ND "
        f"and p ≈ ni²/ND. For the 10^16 cm⁻³ example, p falls to {P_MIN:.1e} cm⁻³, six decades "
        "below the majority population. The same arithmetic with acceptors swaps the names.",
    )
    add_p(doc, "Key idea. Doping sets the majority. Mass action sets the minority. You do not choose them independently.")
    add_h(doc, "Worked Example 2.1", 2)
    add_p(
        doc,
        "Boron is added to silicon at NA = 1.0×10^17 cm⁻³. Donors are negligible. Find the "
        "majority and minority concentrations.",
    )
    add_p(
        doc,
        f"Holes are the majority: p ≈ NA = 1.0×10^17 cm⁻³. Electrons are the minority: "
        f"n = ni²/NA = {P2_N:.1e} cm⁻³. There is one free electron for every ten million holes.",
    )
    add_h(doc, "Practice", 2)
    add_p(doc, "1. Phosphorus at 1.0×10^15 cm⁻³, acceptors negligible. Find n and p.")
    add_p(doc, "2. Someone says \"n-type means there are no holes.\" Answer with the mass-action law and one number from this chapter.")
    add_p(doc, "3. Both ND = 1.0×10^16 cm⁻³ and NA = 1.0×10^15 cm⁻³ are present. Who wins, and what is the approximate majority concentration? Use n + NA = p + ND and n p = ni², and drop the small term only after you have named it.")

    add_h(doc, "Chapter 3. Two Ways Charge Moves", 1)
    add_p(
        doc,
        "A crowd leaves a stadium two ways. People walk downhill because the ground slopes, and "
        "people also spread from the packed gate into the empty street even if the street is flat. "
        "Electrons do both. The slope is the electric field. The packed gate is a concentration "
        "gradient. Circuits need both pictures, because a diode uses diffusion at the junction "
        "and drift in the bulk.",
    )
    add_h(doc, "3.1 Drift", 2)
    add_p(
        doc,
        "An electric field pulls electrons one way and holes the other. The drift speeds are "
        "μn E and μp E, in opposite directions, but both movements carry positive current in the "
        "direction of the field. Holes moving with the field are a positive current. Electrons "
        "moving against the field are also a positive current, because negative charge moving "
        "backward is the same as positive charge moving forward. That is why the conductivity "
        "formula adds the two terms instead of subtracting them.",
    )
    add_h(doc, "3.2 Diffusion and the Einstein relation", 2)
    add_p(
        doc,
        "Where the concentration changes with position, carriers spread from crowded toward "
        "empty. The diffusion constants Dn and Dp have units of cm²/s. In equilibrium they are "
        "not a second independent property of the crystal. Einstein's relation ties them to the "
        "mobilities and to VT:",
    )
    add_p(doc, "Dn = μn VT,    Dp = μp VT", center=True)
    add_p(
        doc,
        f"with VT in volts. This book's μn and VT give Dn = {P3_DN:.1f} cm²/s. "
        f"Dp = μp VT = {MU_P * VT:.2f} cm²/s. The electron diffusion current density along x is "
        "q Dn dn/dx, and the sign is fixed by the fact that electrons diffusing toward +x carry "
        "negative charge that way, which is a negative current in the +x direction. Holes "
        "diffusing toward +x are a positive current. The formulas used below take magnitudes "
        "when the question is \"how large,\" and they keep the sign when the question is \"which way.\"",
    )
    add_h(doc, "3.3 Drift and diffusion together", 2)
    add_p(
        doc,
        "In the bulk of a uniformly doped resistor, the gradient is about zero and drift does "
        "the work. At a pn junction in equilibrium, a large diffusion current wants to pour "
        "carriers across the boundary, and a drift current from the built-in field cancels it. "
        "Net current is zero. The cancellation is exact in equilibrium and is the reason the "
        "next chapter can compute a voltage without ever connecting a battery.",
    )
    add_p(doc, "Key idea. Field moves carriers as drift. A crowd moving into an empty region is diffusion. Equilibrium at a junction is those two currents canceling.")
    add_h(doc, "Worked Example 3.1", 2)
    add_p(
        doc,
        "Electron concentration falls from 1.0×10^16 cm⁻³ to 1.0×10^15 cm⁻³ across 1 μm "
        "(1×10⁻⁴ cm). Using this book's Dn, find the magnitude of the diffusion current density.",
    )
    add_p(
        doc,
        f"|dn/dx| = 9.0×10^15 / 1×10⁻⁴ = 9.0×10^19 cm⁻⁴. "
        f"|Jn| = q Dn |dn/dx| = (1.602×10⁻¹⁹)({P3_DN:.1f})(9.0×10^19) = {J_DIFF:.3f} A/cm². "
        "That is a serious current density for a gradient only a micron long, which is why "
        "junctions, whose gradients are even steeper, care so much about diffusion.",
    )
    add_h(doc, "Practice", 2)
    add_p(doc, "1. Compute Dn and Dp from this book's mobilities and VT. Give both in cm²/s.")
    add_p(doc, "2. A hole gradient of 1.0×10^20 cm⁻⁴ drives hole diffusion. Find the magnitude of Jp. Which way does conventional current point, relative to the direction the holes are spreading?")
    add_p(doc, "3. In a long uniformly doped bar, dn/dx = 0 and E = 10 V/cm, n = 1.0×10^16 cm⁻³. Find the drift current density and compare it with Worked Example 3.1.")

    add_h(doc, "Chapter 4. The Junction Sits There with a Voltage Already On It", 1)
    add_p(
        doc,
        "Push a crowded room against an empty hall and leave the door open. People spill through "
        "until a jam at the doorway, people pressed shoulder to shoulder, makes further spilling "
        "as hard as the crowding that caused it. A pn junction does that with electrons and holes. "
        "Nobody has to apply a battery. The voltage is the jam.",
    )
    add_h(doc, "4.1 What crosses, and what is left behind", 2)
    add_p(
        doc,
        "On the n-side, electrons are many and holes are few. On the p-side, the reverse. "
        "Electrons diffuse into the p-side. Holes diffuse into the n-side. Each electron that "
        "leaves the n-side leaves a positive donor ion behind. Each hole that leaves the p-side "
        "leaves a negative acceptor ion behind. Those ions cannot wander off. They are stuck in "
        "the crystal. A sheet of positive charge therefore faces a sheet of negative charge, "
        "with a region between them that has been emptied of mobile carriers. That region is "
        "the depletion layer, or space-charge region.",
    )
    add_h(doc, "4.2 Built-in voltage", 2)
    add_p(
        doc,
        "The field of those two sheets points from the positive donor ions toward the negative "
        "acceptor ions, which is from n toward p. It pushes electrons back toward the n-side "
        "and holes back toward the p-side, opposing the diffusion that created it. Equilibrium "
        "is the balance. The potential difference that belongs to that balance is the built-in "
        "voltage,",
    )
    add_p(doc, "Vbi = VT ln(NA ND / ni²)", center=True)
    add_p(
        doc,
        "for an abrupt junction with both sides doped well above ni. Notice what raises Vbi: "
        "heavier doping on either side, or a smaller ni. Notice what does not appear: the "
        "applied voltage. Vbi is a property of the two dopings and the temperature. Applying "
        "a battery changes the barrier the carriers actually face, which is Vbi minus the "
        "applied forward voltage, but it does not rewrite this formula.",
    )
    add_h(doc, "4.3 How wide the empty region is", 2)
    add_p(
        doc,
        "For a one-sided abrupt junction, almost all of the depletion width sits on the lightly "
        "doped side. If that side is n-type with doping ND and the applied voltage is V "
        "(positive V means forward),",
    )
    add_p(doc, "W = sqrt( 2 εs (Vbi − V) / (q ND) )", center=True)
    add_p(
        doc,
        "εs is the permittivity of silicon, 11.7 times the permittivity of free space. Forward "
        "bias shrinks W. Reverse bias grows it. The square root is why doubling the reverse "
        "voltage does not double the width.",
    )
    add_p(doc, "Key idea. A pn junction in a drawer already has a built-in voltage. The battery later adds to that story. It does not start it.")
    add_h(doc, "Worked Example 4.1", 2)
    add_p(
        doc,
        "Both sides are doped at 1.0×10^16 cm⁻³. Find Vbi. Then treat the junction as one-sided "
        "on an n-type side of that same doping, at zero applied volts, and find W. This is a "
        "teaching idealization of a symmetric junction, used so the arithmetic stays visible.",
    )
    add_p(
        doc,
        f"NA ND / ni² = 1.0×10^32 / 1.0×10^20 = 1.0×10^12. "
        f"ln(10^12) = {math.log(1e12):.3f}. "
        f"Vbi = (0.026)({math.log(1e12):.3f}) = {VBI_SYM:.3f} V. "
        f"W = {W0:.3e} cm = {W0 * 1e4:.3f} μm. "
        "A few tenths of a micron of emptied crystal is enough to hold about seven-tenths of a volt.",
    )
    add_h(doc, "Practice", 2)
    add_p(doc, "1. NA = 1.0×10^18 cm⁻³ and ND = 1.0×10^16 cm⁻³. Find Vbi with this book's constants.")
    add_p(doc, "2. Using the W of Worked Example 4.1 as the zero-bias width, does a reverse bias of a few volts make W several times larger, or only somewhat larger? Argue from the square root before you compute.")
    add_p(doc, "3. Why does heating the crystal, which raises ni, lower Vbi?")

    add_h(doc, "Chapter 5. The Diode Law Is a Crowd Crossing a Barrier", 1)
    add_p(
        doc,
        "A turnstile at a stadium lets a few people through when the bar is high, and a great "
        "many when someone lowers it by a hand's width. The diode is that turnstile for the "
        "minority carriers waiting at the edge of the depletion layer. Lower the barrier a "
        "little and the forward current multiplies. Raise it and the forward crowd disappears, "
        "leaving only a small reverse trickle.",
    )
    add_h(doc, "5.1 The equation", 2)
    add_p(
        doc,
        "For an ideal diode the current is",
    )
    add_p(doc, "I = IS ( e^(V / VT) − 1 )", center=True)
    add_p(
        doc,
        "V is the applied voltage, positive when the p-side is positive, which is forward bias. "
        "IS is the saturation current, set by the area, the doping, and the lifetime of the "
        "minorities. This chapter's worked diode uses IS = 1 fA = 10⁻¹⁵ A, a small-junction "
        "teaching value, not a claim about a particular part number. VT is 26 mV. The \"− 1\" "
        "matters near zero and in reverse. A few tenths of a volt forward, the exponential is "
        "so large that I ≈ IS e^(V/VT).",
    )
    add_h(doc, "5.2 Sixty millivolts per decade", 2)
    add_p(
        doc,
        "Ask how much extra forward voltage multiplies the current by ten, once you are well "
        "above VT. The exponential must grow by 10, so the added voltage is VT ln(10).",
    )
    add_p(
        doc,
        f"VT ln(10) = 0.026 × {math.log(10):.4f} = {DECADE_V * 1000:.1f} mV.",
        center=True,
    )
    add_p(
        doc,
        "Call it 60 mV per decade of current at this book's room temperature. A real silicon "
        "diode is often closer to 60 mV only in a mid-current window. At very low current, "
        "recombination in the depletion layer makes the effective step larger. At high current, "
        "series resistance steals voltage. The ideal law is the spine. The part on the bench "
        "wears extra clothes, which is Chapter 6.",
    )
    add_h(doc, "5.3 There is no switch at 0.7 V", 2)
    add_p(
        doc,
        "A forward drop near 0.7 V is what you see when a small silicon diode is carrying a "
        "current of a good fraction of a milliamp, with an IS on the order of a femtoamp. It "
        "is an operating point, not a threshold the device crosses. Below that voltage the "
        "diode is already conducting. It is conducting less. Circuit sketches that draw an "
        "ideal switch plus a 0.7 V battery are welcome in Book 1 problems. They are the wrong "
        "picture if you are asking how leakage, a photodiode, or a low-current bias network "
        "behaves.",
    )
    add_p(doc, "Key idea. Forward current is exponential in voltage. A \"turn-on voltage\" is a current you chose to care about, read back through that exponential.")
    add_h(doc, "Worked Example 5.1", 2)
    add_p(
        doc,
        "IS = 1.0×10⁻¹⁵ A and VT = 26 mV. Find I at 0.50 V, 0.60 V, and 0.70 V. Then find the "
        "forward voltage that produces 1.0 mA.",
    )
    add_p(
        doc,
        f"At 0.50 V, I = {I_05:.3e} A = {I_05 * 1e6:.3f} μA. "
        f"At 0.60 V, I = {I_06:.3e} A = {I_06 * 1e6:.2f} μA. "
        f"At 0.70 V, I = {I_07:.3e} A = {I_07 * 1e3:.3f} mA. "
        f"From 0.60 V to 0.70 V the current rises by a factor of {I_07 / I_06:.1f}, "
        f"close to the decade-and-a-half that 100 mV predicts (100/60 ≈ 1.7 decades, and "
        f"10^1.67 ≈ 47). "
        f"For 1.0 mA, V = VT ln(I/IS + 1) = {V_1MA:.3f} V. "
        "The familiar seven-tenths of a volt showed up because we asked for about a milliamp, "
        "not because the silicon changed state.",
    )
    add_h(doc, "Practice", 2)
    add_p(doc, "1. Same diode. Find I at 0.65 V.")
    add_p(doc, "2. How much must V rise to take this diode from 0.1 mA to 1 mA, using the 60 mV/decade rule? Check it against the exact formula.")
    add_p(doc, "3. Reverse bias of 0.2 V. Compute I from the full equation. Why is the result about −IS, and why is a real reverse current often larger than this ideal?")

    add_h(doc, "Chapter 6. The Diode You Can Buy", 1)
    add_p(
        doc,
        "The part in the drawer has a glass or plastic body, two leads, a junction area someone "
        "chose, and a data sheet with a curve that only roughly matches Chapter 5. The law is "
        "still in there. Three extras decide whether a circuit works: the junction behaves as "
        "a capacitor, a large reverse voltage eventually breaks the crystal down, and a forward "
        "current does not stop the instant you reverse the voltage.",
    )
    add_h(doc, "6.1 Junction capacitance", 2)
    add_p(
        doc,
        "The depletion layer is an insulator between two conducting regions, which is a "
        "capacitor. Its value falls as reverse bias widens the layer. For an abrupt junction "
        "a serviceable model is",
    )
    add_p(doc, "Cj = Cj0 / sqrt(1 − V/Vbi)", center=True)
    add_p(
        doc,
        "with V negative in reverse, and Cj0 the zero-bias value set by area and doping. "
        "Varactor diodes are ordinary junctions used on purpose as voltage-controlled "
        "capacitors. Rectifier diodes carry the same capacitance whether you asked for it "
        "or not. At radio frequency that capacitance is part of the matching network. At "
        "audio it is often ignorable. The frequency, not the part's name, decides.",
    )
    add_h(doc, "6.2 Breakdown", 2)
    add_p(
        doc,
        "Push reverse bias high enough and the field in the depletion layer rips bonds apart "
        "or gives carriers enough energy between collisions to create more carriers. Current "
        "then rises steeply at nearly constant voltage. A Zener diode is a junction designed "
        "so that this knee sits at a useful, specified voltage, and so that the part can "
        "survive the current you intend to run through that knee. A signal diode's breakdown "
        "voltage is a limit, not a feature. Exceed it without a current limit and the junction "
        "overheats.",
    )
    add_p(
        doc,
        "Two microscopic stories share that knee. Zener tunneling dominates at low breakdown "
        "voltages. Avalanche, the carrier-multiplication story, dominates at higher ones. "
        "Data sheets still say \"Zener\" for both. The circuit fact is the steep reverse knee. "
        "The name on the bag is older than the distinction.",
    )
    add_h(doc, "6.3 Reverse recovery", 2)
    add_p(
        doc,
        "Forward current stores minority charge on both sides of the junction. When the circuit "
        "reverses the voltage, that stored charge has to come back out, or recombine, before "
        "the diode can block. For a interval on the order of the storage delay the diode still "
        "conducts backward. Fast-recovery and Schottky diodes exist because that interval is "
        "expensive in a switching supply. A Schottky diode is a metal-semiconductor junction. "
        "It has a lower forward drop and almost no stored minority charge, and it generally "
        "leaks more and breaks down sooner than a pn diode of similar size. Choose it when "
        "the switching edge is the problem. Choose a pn diode when the reverse voltage and "
        "the leakage are the problem.",
    )
    add_p(doc, "Key idea. The exponential law is the junction. Capacitance, breakdown, and stored charge are why the data sheet is thicker than the equation.")
    add_h(doc, "Worked Example 6.1", 2)
    add_p(
        doc,
        f"An abrupt-junction diode has Cj0 = 10 pF and the Vbi of Worked Example 4.1, "
        f"{VBI_SYM:.3f} V. Find Cj at a reverse bias of 5 V.",
    )
    add_p(
        doc,
        f"V/Vbi = −5 / {VBI_SYM:.3f} = {-5 / VBI_SYM:.3f}. "
        f"1 − V/Vbi = {1 - (-5) / VBI_SYM:.3f}. "
        f"The square root is {math.sqrt(1 - (-5) / VBI_SYM):.3f}. "
        f"Cj = 10 pF / {math.sqrt(1 - (-5) / VBI_SYM):.3f} = {CJ_5 * 1e12:.2f} pF. "
        "Five volts of reverse bias cut the capacitance to about a third. A tuner that "
        "expects a wide capacitance range is using this same square root, over whatever "
        "bias its varactor is allowed.",
    )
    add_h(doc, "Practice", 2)
    add_p(doc, "1. Cj0 = 20 pF, same Vbi, reverse bias 2 V. Find Cj.")
    add_p(doc, "2. A rectifier data sheet lists a reverse-recovery time. What stored thing is that time waiting on, and why does a Schottky diode largely skip it?")
    add_p(doc, "3. A 5.1 V Zener is used as a reference with a series resistor from a 12 V rail. In one sentence, what does the resistor do that the junction itself does not?")

    add_h(doc, "Appendix A. Constants Used in This Part", 1)
    add_p(doc, "Thermal voltage VT: 26 mV. Declared room-temperature hand value.")
    add_p(doc, "Intrinsic concentration ni of silicon: 1.0×10^10 cm⁻³. Declared hand value.")
    add_p(doc, "Elementary charge q: 1.602×10⁻¹⁹ C.")
    add_p(doc, "Relative permittivity of silicon: 11.7.")
    add_p(doc, "Working mobilities, when a problem states none: μn = 1000 cm²/V·s, μp = 480 cm²/V·s.")
    add_p(doc, f"Einstein, from those values: Dn = {P3_DN:.1f} cm²/s, Dp = {MU_P * VT:.2f} cm²/s.")
    add_p(doc, f"Voltage per decade of ideal forward current: {DECADE_V * 1000:.1f} mV.")
    add_p(doc, "Worked-diode saturation current: IS = 1.0×10⁻¹⁵ A.")
    add_p(
        doc,
        "Silicon bandgap cited in Chapter 1 is about 1.12 eV. Germanium about 0.66 eV. "
        "Gallium arsenide about 1.42 eV. Those three are orientation numbers, not inputs to "
        "the worked arithmetic.",
    )

    add_h(doc, "Appendix B. Answers to the Practice Problems", 1)
    add_h(doc, "Chapter 1", 2)
    add_p(
        doc,
        f"1. p = ni²/n = {P1_P:.1e} cm⁻³. σ = q n μn = {Q * P1_ND * MU_N:.4f} (Ω·cm)⁻¹. "
        f"ρ = {P1_RHO:.3f} Ω·cm. Ten times fewer electrons, ten times the resistivity.",
    )
    add_p(
        doc,
        "2. A wider gap means fewer bonds broken at a given temperature, so ni is smaller. "
        "Reverse current of a junction tracks that minority population, so the leakage falls.",
    )
    sigma_i = Q * NI * (MU_N + MU_P)
    add_p(
        doc,
        f"3. σ = q ni (μn + μp) = {sigma_i:.3e} (Ω·cm)⁻¹. "
        f"The hole term is μp/(μn+μp) = {MU_P / (MU_N + MU_P):.2f} of the total, about a third. "
        "It is not ignorable. It was ignorable in the worked example only because doping had "
        "made n huge and p tiny.",
    )
    add_h(doc, "Chapter 2", 2)
    add_p(doc, f"1. n ≈ 1.0×10^15 cm⁻³. p = ni²/n = {P1_P:.1e} cm⁻³.")
    add_p(
        doc,
        f"2. The hole concentration is ni²/ND, not zero. At ND = 10^16 cm⁻³ it is {P_MIN:.1e} cm⁻³.",
    )
    add_p(
        doc,
        "3. Donors exceed acceptors by 9.0×10^15 cm⁻³, so the material is n-type. "
        "The majority electron concentration is approximately ND − NA = 9.0×10^15 cm⁻³. "
        "The minority hole concentration is ni² divided by that majority, about 1.1×10^4 cm⁻³. "
        "The subtraction is charge neutrality with the small carrier terms dropped. Dropping "
        "them is fair here because both are far below the doping difference.",
    )
    add_h(doc, "Chapter 3", 2)
    add_p(doc, f"1. Dn = {P3_DN:.1f} cm²/s. Dp = {MU_P * VT:.2f} cm²/s.")
    jp = Q * (MU_P * VT) * 1.0e20
    add_p(
        doc,
        f"2. |Jp| = q Dp |dp/dx| = {jp:.3f} A/cm². Conventional current points the same way "
        "the holes are spreading.",
    )
    j_drift = Q * MU_N * ND16 * 10.0
    add_p(
        doc,
        f"3. Jn,drift = q n μn E = {j_drift:.3f} A/cm². "
        f"The diffusion example was {J_DIFF:.3f} A/cm². "
        "A modest field of 10 V/cm in this doping already beats that particular one-micron gradient. "
        "Steeper gradients, the kind inside a junction, put diffusion back in front.",
    )
    add_h(doc, "Chapter 4", 2)
    add_p(
        doc,
        f"1. NA ND / ni² = 1.0×10^34 / 1.0×10^20 = 1.0×10^14. "
        f"Vbi = 0.026 × ln(10^14) = 0.026 × {math.log(1e14):.3f} = {P4_VBI:.3f} V.",
    )
    add_p(
        doc,
        "2. Only somewhat larger. Width follows the square root of (Vbi − V). A few volts of "
        "reverse bias increases the term inside the root by a factor of several, and the width "
        "by the square root of that factor, not by the factor itself.",
    )
    add_p(
        doc,
        "3. Vbi depends on ln(1/ni²). A larger ni shrinks the argument of the logarithm, so Vbi falls.",
    )
    add_h(doc, "Chapter 5", 2)
    add_p(doc, f"1. I(0.65 V) = {P5_I:.3e} A = {P5_I * 1e6:.2f} μA.")
    v_0_1 = VT * math.log(0.1e-3 / IS_A + 1)
    v_1 = V_1MA
    add_p(
        doc,
        f"2. One decade is {DECADE_V * 1000:.1f} mV, so the rule says {DECADE_V * 1000:.1f} mV. "
        f"Exact voltages: {v_0_1:.4f} V at 0.1 mA and {v_1:.4f} V at 1 mA, "
        f"a difference of {(v_1 - v_0_1) * 1000:.1f} mV. The rule is the exact ideal-diode result "
        "once I is far above IS, which it is.",
    )
    i_rev = diode_i(-0.2)
    add_p(
        doc,
        f"3. I(−0.2 V) = {i_rev:.3e} A, which is −IS times (1 − e^(−0.2/VT)). "
        f"e^(−0.2/VT) is about {fexp(-0.2 / VT):.2e}, so the factor in parentheses is already "
        "indistinguishable from 1 at three significant figures, and I ≈ −IS. A real diode adds "
        "surface leakage and generation inside the depletion layer, both missing from the ideal law.",
    )
    add_h(doc, "Chapter 6", 2)
    add_p(
        doc,
        f"1. 1 − V/Vbi = {1 - (-2) / VBI_SYM:.3f}. "
        f"Cj = 20 / {math.sqrt(1 - (-2) / VBI_SYM):.3f} = {P6_CJ * 1e12:.2f} pF.",
    )
    add_p(
        doc,
        "2. The time is waiting on minority charge stored by the forward current. A Schottky "
        "junction does not store that minority population in the same way, so the recovery "
        "tail is largely absent.",
    )
    add_p(
        doc,
        "3. The resistor sets the current through the knee. The junction sets the voltage. "
        "Without the resistor the supply would try to hold 12 V across a 5.1 V knee.",
    )

    add_h(doc, "Appendix C. What This Part Does Not Yet Cover", 1)
    add_p(
        doc,
        "Part II is the bipolar transistor. Part III is the MOSFET and the CMOS gate. "
        "Part IV is the inside of the amplifiers Book 2 treated as ideal blocks, checked "
        "against the 16th edition of Tietze, Schenk, and Gamm, whose op-amp chapter was "
        "the one rewritten for that edition. Part V is CMOS as a chip: sizing, delay, "
        "and the path from a gate to a placed design. Part VI is the handoff to the rest "
        "of the series.",
    )
    add_p(
        doc,
        "Those later books already have their source shelves in the series plan. Radio "
        "matching and lines belong to Book 4. Noise figures and receiver cascades belong "
        "to Book 5. Modulation belongs to Book 6. Phase-locked loops belong to Book 7. "
        "Microwave lines and the historical Radiation Laboratory volumes belong to Book 8. "
        "Antennas belong to Book 10. Emissions and grounding belong to Book 11. "
        "Sampling, multirate filters, and a receiver you can code belong to Book 14. "
        "Linear regulators and switch-mode supplies belong to Book 15. Bode plots as a "
        "general language belong to Book 16. High-speed copper, the hot loop of a buck "
        "converter, and the feedback divider of an LDO belong to Books 15 and 18 together. "
        "None of that is smuggled into the diode chapters above.",
    )

    # The Heading 1 style page-breaks before the first heading, which is what we want
    # after the title block. Confirm no empty first heading.
    doc.save(OUT)
    print(f"wrote {OUT}")
    print(f"Vbi {VBI_SYM:.4f} V")
    print(f"rho {RHO16:.4f}")
    print(f"I0.7 {I_07:.6e} A")
    print(f"W {W0*1e4:.4f} um")
    print(f"Cj5 {CJ_5*1e12:.3f} pF")
    print(f"decade {DECADE_V*1000:.2f} mV")


if __name__ == "__main__":
    build()
