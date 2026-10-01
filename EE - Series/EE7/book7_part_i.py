# -*- coding: utf-8 -*-
"""Third section and shown arithmetic for each Book 7 chapter.

Book 3 Part I puts the formula on its own line and multiplies it out in the
worked example. These rows are inserted the same way. Placeholders are filled
from the builder's N dict.
"""

# Rows inserted immediately before "Worked Example n.1".
BEFORE = {}
# Rows inserted immediately after that example's answer, before Practice.
AFTER = {}

BEFORE[1] = [
    ("h2", "1.3 Sixteen is a condition, not a reading"),
    (
        "body",
        "A turnstile counts people only after you say which gate is open. The factor of sixteen counts field only after you say the current is the same. People write \"the harmonic will be 24 dB up\" the way they write \"the diode turns on at 0.7 V\": a familiar number promoted from an operating point into a law. The fourth harmonic of a symmetric square is the gate that is not open. The third harmonic is the one that is.",
    ),
    ("eq", "(100 / 25)² = 16"),
    ("eq", "20 × log10(16) = 20 × {log10_16} = {db16} dB"),
    (
        "body",
        "Key idea. Report the current condition beside the decibel, or do not report the decibel.",
    ),
]
AFTER[1] = [
    ("eq", "9 × (1/3) = {third_net}"),
    ("eq", "20 × log10(3) = {db_third} dB"),
    (
        "body",
        "Nine from the frequency ratio, one third from the ideal square, three for the field. That is the product to write in a margin before anyone types 16 into a report.",
    ),
]

BEFORE[2] = [
    ("h2", "2.3 The 1/r line is already in the field"),
    (
        "body",
        "The far-field expression divides by r once. A second division, or a second multiplication, is a different problem. The mistake is easy because the near magnetic field of a loop falls faster, closer to 1/r³, and a bench probe lives in that region. Using the far formula on the bench overstates a quiet loop. Using it twice at 3 m invents a current the layout does not have.",
    ),
    ("eq", "E = μ0 ω² I A / (4 π c r)"),
    (
        "body",
        "Hold I, A, and r fixed and ω² is the only frequency left. That is why the field ratio is the square of the frequency ratio, and why a probe an inch off the board is not this equation.",
    ),
]
AFTER[2] = [
    ("eq", "E(1 A) = {e_loop_1a_uv} μV/m at 3 m"),
    ("eq", "I = 150 / {e_loop_1a_uv} A = {i_loop_ma} mA"),
    (
        "body",
        "The 150 is the Class B row in microvolts per meter. The denominator is the same unit for one ampere. The distance was spent when that denominator was computed. It does not appear again.",
    ),
]

BEFORE[3] = [
    ("h2", "3.3 A mains cord is not ten of these wires"),
    (
        "body",
        "Length sits in the numerator of the short-dipole formula, so a careless reader multiplies the 10 cm answer by ten and calls a 1 m cord done. That step assumes the current is still uniform along the wire. At 100 MHz a meter of cord is a large piece of a wavelength, the current piles up in a shape this formula refuses, and the cord is usually a better antenna than the short model. Scaling up the length scales up a lie.",
    ),
    ("eq", "E = η k I L / (4 π r)"),
    (
        "body",
        "k is ω/c. L is the short length, 10 cm in every number this chapter computes. η is {eta} Ω, and it belongs here, in the field, not as a resistor in a netlist.",
    ),
]
AFTER[3] = [
    ("eq", "{i_loop_ma} mA / {i_wire_ua} μA = {loop_over_wire}"),
    (
        "body",
        "The loop needs {loop_over_wire} times the current of the 10 cm wire to reach the same 150 μV/m. That is the comparison. It is not a universal microampere law for every cable in the lab.",
    ),
]

BEFORE[4] = [
    ("h2", "4.3 Multiply the detour before you call it small"),
    (
        "body",
        "A slot looks narrow, so a layout review calls it a small loop. Narrow is one side. The trace that has to go around is the other side. Area is the product. The teaching square is 2 cm by 2 cm. A 5 cm trace with a 2 cm detour is not a courtesy cut in the pour. It is a larger loop than the one Chapter 2 already took seriously.",
    ),
    ("eq", "A = 5 cm × 2 cm = {slot_cm2} cm²"),
    ("eq", "{slot_cm2} / {teach_cm2} = {slot_over}"),
    (
        "body",
        "Key idea. Do not slot the ground under a return. If the return must cross a split, cross once, beside the signal.",
    ),
]
AFTER[4] = [
    (
        "body",
        "The field of a small loop scales with area when the current is the same. A slot loop {slot_over} times the teaching square is {slot_over} times the field of that square. \"Just a ground cut\" is how that factor gets onto a board.",
    ),
]

BEFORE[5] = [
    ("h2", "5.3 The foil is already several skin depths"),
    (
        "body",
        "People buy thicker copper when the chamber is a few decibels unfriendly. At 100 MHz the wave is not starving for thickness. It is looking for a seam. Write the skin depth, divide the foil by it, and turn nepers into decibels before you change the stackup. Book 8 keeps this same copper rule for magnetics. This chapter only borrows it long enough to retire the thickness argument.",
    ),
    ("eq", "δ = 66 / √f = {skin_mm} mm at 100 MHz"),
    ("eq", "0.0348 / {skin_mm} = {t_over_d}"),
    ("eq", "{t_over_d} × {neper} = {absorb} dB"),
]
AFTER[5] = [
    (
        "body",
        "One ounce is already near {absorb} dB of absorption in this estimate, before reflection. A second ounce adds skin depths to a wall that was not the leak. Spend the next drawing on the seam and on the wire that leaves the box.",
    ),
]

BEFORE[6] = [
    ("h2", "6.3 The current is V over the ohms you declared"),
    (
        "body",
        "A filter chapter in Book 2 would now draw poles. This chapter stops at the current that reaches the antenna. Declare the voltage, declare the ohms, divide. If you cannot say whether the ohms are common mode or differential mode, you do not yet have a filter. You have parts.",
    ),
    ("eq", "I = V / Z"),
    (
        "body",
        "The 20 Ω and the 200 Ω are this example's declarations. They are not the impedance of every cable. Change them and the factor changes. That is the point of writing them down.",
    ),
]
AFTER[6] = [
    ("eq", "0.010 / 20 = {i_before_ua} μA"),
    ("eq", "0.010 / 220 = {i_after_ua} μA"),
    (
        "body",
        "The builder's ratio of those two currents, before rounding the display, is {choke_ratio}. Before the choke the example is over Chapter 3's short-wire current. After it, the example is under that current. The factor belongs to these ohms, not to the next product.",
    ),
]

BEFORE[7] = [
    ("h2", "7.3 One height is not a maximum"),
    (
        "body",
        "The method's number is the largest field it can find by turning the product and moving the antenna. A single bore-sight at 1.5 m is a photograph of one pose. The limit was written against the pose that loses. Calling a fixed mast \"3 m\" because the tape says three meters keeps the distance and throws away the search. CISPR 16 and ANSI C63.4 are the documents that own that search, including the quasi-peak detector the receiver must use when the limit says quasi-peak.",
    ),
    (
        "body",
        "Key idea. Height 1 m to 4 m, a full turn, both polarizations. The recorded point is the maximum of that set.",
    ),
]
AFTER[7] = [
    (
        "body",
        "Missing the height scan and missing the turntable are two missing maxima, not one. A GTEM does not put them back. It is a different instrument, used as a rehearsal in Chapter 20.",
    ),
]

BEFORE[8] = [
    ("h2", "8.3 The detector is part of the limit"),
    (
        "body",
        "A limit written for quasi-peak is a sentence with the detector in it. Peak detect is how you find the line quickly. It reads high on a click and almost agrees with quasi-peak on a clock that never turns off. Signing the peak number against a quasi-peak row either invents a failure or, if someone later \"corrects\" it by a favorite number of decibels, hides one. The time constants live in CISPR 16. This book's snapshot is a charge near 1 ms and a discharge near 160 ms on the conducted side, near 550 ms on the radiated side. Calibrate the receiver from the edition, not from this paragraph.",
    ),
]
AFTER[8] = [
    (
        "body",
        "Six decibels of peak over a quasi-peak limit is a reason to change detectors. It is not yet a reason to respin the board. Remeasure on the detector the row names.",
    ),
]

BEFORE[9] = [
    ("h2", "9.3 Compare the classes at one distance"),
    (
        "body",
        "Class A and Class B are printed at different distances. Subtracting the raw microvolts is a comfort the standard did not offer. Move the far-field picture with 1/r, say that you did, and then compare. The move is not how you certify Class A. It is how you stop telling yourself the residential limit is the looser one.",
    ),
    ("eq", "20 × log10(10/3) = {db_dist} dB"),
    ("eq", "90 × (10/3) = {class_a_3m} μV/m"),
]
AFTER[9] = [
    ("eq", "20 × log10(150) = 43.5 dBμV/m"),
    (
        "body",
        "A reading of 46 dBμV/m at 200 MHz is about 2.5 dB over the 43.5 row. The band and the detector have to be the ones in the snapshot, or the subtraction is theater.",
    ),
]

BEFORE[10] = [
    ("h2", "10.3 A decibel-microvolt on 50 ohms is a current"),
    (
        "body",
        "The LISN is why the division is legal. Fifty ohms is the port, not a guess about the building wiring. Leave the network unnamed and the microampere is fan fiction. Write 50 Ω / 50 μH, then convert.",
    ),
    ("eq", "60 dBμV = 10^(60/20) μV = 1000 μV"),
    ("eq", "I = 1000 μV / 50 Ω = {ua60} μA"),
]
AFTER[10] = [
    (
        "body",
        "{ua60} μA at 60 dBμV sits on the 5–30 MHz quasi-peak snapshot and 4 dB over the 56 dBμV row used from 0.5 to 5 MHz. The same meter reading is a pass or a fail depending on the line of the table you are standing on.",
    ),
]

BEFORE[11] = [
    ("h2", "11.3 A quiet board can still reset"),
    (
        "body",
        "Emission asks what left the box. Immunity asks what the box does when something arrives. A product can be under 150 μV/m and still drop a USB link when the ESD gun touches a screw. The gun is 61000-4-2. The burst on a cable is 61000-4-4. The slow high-energy pulse is 61000-4-5. None of those is a quasi-peak scan run backward. The product standard names the level and the criterion. Criterion A keeps working. Criterion B hiccups and recovers. Criterion C waits for a person. Write which one you were allowed.",
    ),
]
AFTER[11] = [
    (
        "body",
        "The first question at that screw is geometric. Where does the metal go, and is the connector shell bonded at the wall or through a tour of the board? The spark uses the inductance you gave it. Chapter 6's rule is the same rule: meet the outside world at the boundary.",
    ),
]

BEFORE[12] = [
    ("h2", "12.3 Two reports, because there are two limits"),
    (
        "body",
        "A Wi-Fi gadget owes an EMC file and a radio file. The EMC file is the unintentional box: emission, immunity, the quasi-peak rows. The radio file is the intentional mask: power, bandwidth, spurious, often an error vector. OTA and SAR, when the product needs them, sit with the radio file. The LDPC decoder sits after the waveform already exists. A line in the chamber is energy at a frequency. It does not indict the code.",
    ),
    (
        "body",
        "Key idea. Ask which report failed before you ask which part to change.",
    ),
]
AFTER[12] = [
    (
        "body",
        "Twice the carrier is the radio chain, which Book 6 owns. A 48 MHz line is a clock or a supply until a measurement says otherwise. One waiver does not cover both.",
    ),
]

BEFORE[13] = [
    ("h2", "13.3 Name what the solver is allowed to ignore"),
    (
        "body",
        "SPICE may ignore radiation. A 2.5D solver may ignore a connector that stands up out of the layers. Harmonic balance may ignore a one-shot ESD event. A 3D solver may not ignore a coarse mesh across the gap that sets the field. AWR is a circuit bench. HFSS is a mesh. AWR is not HFSS. There is no free file that is Microwave Office under another name.",
    ),
    (
        "body",
        "Key idea. Write the permission on the plot. A field picture with no port and no mesh note is a poster.",
    ),
]
AFTER[13] = [
    (
        "body",
        "The buck's hot loop, while it is still a loop, is SPICE plus Chapter 2's area. The converter itself is Book 8. The barrel jack standing off the board is 3D. AXIEM does not become the right tool by being the tool you already have open.",
    ),
]

BEFORE[14] = [
    ("h2", "14.3 Multiply the inductance before you trust the ohm"),
    (
        "body",
        "The round loop with the teaching area has radius {loop_r_mm} mm. The wire radius in this example is 0.5 mm. External inductance only:",
    ),
    ("eq", "L = μ0 R (ln(8R/a) − 2)"),
    ("eq", "8R/a = {eight_over_a}"),
    ("eq", "ln(8R/a) − 2 = {ln_term}"),
    ("eq", "L = {l_nh} nH"),
    (
        "body",
        "Internal inductance is left out on purpose, in every chapter, so it cannot appear in one example and vanish in the next.",
    ),
]
AFTER[14] = [
    ("eq", "X = 2 π f L = {xl} Ω at 100 MHz"),
    (
        "body",
        "Free-space η is {eta} Ω. It is not this reactance, and it is not a radiation resistance you may paste across the inductor. The radiation resistance of a loop this small sits far below {xl} Ω. Omitting it barely moves the current. It does not excuse you from computing the field with I and A.",
    ),
]

BEFORE[15] = [
    ("h2", "15.3 A gunshot is not a harmonic"),
    (
        "body",
        "Harmonic balance balances a periodic drive. It wants a fundamental and a list of multiples. An ESD strike has no fundamental to lock to. A switching converter in steady state does. Use the tool on the second, and a transient tool or a measurement on the first. A spectrum at a transistor lead is still a conducted spectrum. The match, the feed, and the antenna, which Book 6 and Book 4 own, sit between that lead and the mask.",
    ),
]
AFTER[15] = [
    (
        "body",
        "Fifteen decibels down at the drain can be eaten, in either direction, by a match tuned for the fundamental. The simulation tells you the line exists. The report tells you what left the box.",
    ),
]

BEFORE[16] = [
    ("h2", "16.3 Stop the stackup solver at the edge of the stack"),
    (
        "body",
        "AXIEM, Momentum, and Sonnet earn their keep on traces, planes, gaps that are still gaps in a layer, and via fences. They lose it on a chassis-mounted connector, because that metal is not a layer. The honest drawing is two models and a port where each model's assumption ends. One picture that pretends to be both is the failure.",
    ),
    (
        "body",
        "Key idea. 2.5D for the board. 3D for the metal that stands up into the room.",
    ),
]
AFTER[16] = [
    (
        "body",
        "The SMA through a wall into a screened box is the 3D part. The microstrip that runs up to it can stay in the stackup solver. Say so in the review, or the review will ask AXIEM to mesh a cage it cannot see.",
    ),
]

BEFORE[17] = [
    ("h2", "17.3 The mesh note is part of the answer"),
    (
        "body",
        "A smooth color plot with two triangles across the gap that dominates the field is a drawing. Refine that gap and watch the number you intend to quote. If it moves by more than the margin you were counting on, the first plot was not evidence. HFSS, CST, and Analyst can represent the connector, the package, the cavity, and the seam. They do not owe you a true seam if you did not pay for the mesh.",
    ),
]
AFTER[17] = [
    (
        "body",
        "Ask for the mesh at the gap, the port, and the convergence, in that order, before you look at the colors. An intentional antenna's gain is still Book 4, even when the executable is the same.",
    ),
]

BEFORE[18] = [
    ("h2", "18.3 \"Debug included\" needs a number of hours"),
    (
        "body",
        "7layers, in Bureau Veritas, is the connected-product laboratory. Hermon Laboratories, in Binyamina, is the broader product laboratory. It is not Harmon. They measure. They do not design the board. A quote that folds debug into five days without saying how many hours is a greeting. Ask the standards, the edition, 3 m or 10 m, the detectors, whether immunity is in the week, and whether the radio mask is a second report.",
    ),
]
AFTER[18] = [
    (
        "body",
        "Modes are yours. The height scan is theirs. A product that is quiet only in a hidden menu, tested in that menu, is a pass you did not earn. The cables at the site are the cables you ship, because the cable is the antenna.",
    ),
]

BEFORE[19] = [
    ("h2", "19.3 Two decibels is a factor you can hold"),
    (
        "body",
        "A failure that feels like a new architecture is often a quarter of a loop. Convert the decibels before you call the meeting. Field ratios use twenty times the log, so 2 dB is not a factor of two. Six decibels is the factor of two. Two decibels is the smaller number below.",
    ),
    ("eq", "10^(2/20) = {field2}"),
    ("eq", "√{field2} = {sqrt_field2}"),
    ("eq", "2 cm / {sqrt_field2} = {side_cm} cm"),
]
AFTER[19] = [
    (
        "body",
        "If the current cannot change, the side of the square falls from 2 cm to about {side_cm} cm, because area scales with the side squared and the field scales with area. That is a via moved closer, if the loop was the radiator. If the cable was the radiator, the via does nothing. Name the frequency before you move copper.",
    ),
]

BEFORE[20] = [
    ("h2", "20.3 Do not average the rehearsal with the site"),
    (
        "body",
        "A GTEM, a clamp, and a near-field probe sort causes. The accredited 3 m or 10 m site is the number that goes in the file. If the cell says 8 dB of margin and the site says 2 dB over, the correlation is off by about ten decibels for this product. That fact is about the correlation. It is not a mean you are allowed to submit.",
    ),
]
AFTER[20] = [
    (
        "body",
        "Keep the GTEM as a before-and-after tool for the next spin. Submit the site. Dress the cables the way the method dresses them, not the way a coil on your floor hid the lobe.",
    ),
]

BEFORE[21] = [
    ("h2", "21.3 The sentence stops at the book that owns the number"),
    (
        "body",
        "A series that repeats a formula will eventually compute it two ways. This volume borrows Book 8's skin-depth rule and does not invent a second one. It names Book 6's amplifier and does not redesign the load line. It names Book 4's gain and does not rerun Friis. When a paragraph needs one of those to finish, the paragraph ends in a pointer. The pointer is the work.",
    ),
    (
        "body",
        "Key idea. One volume for the physics, the solver, and the certificate. The neighbors keep their own numbers.",
    ),
]
AFTER[21] = [
    (
        "body",
        "A 100 W GaN stage at 3.5 GHz is Book 6. The mask measurement is this book. A 400 kHz buck is Book 8. The LISN reading is Chapter 10. The copper rule is Book 8's, used here only on a wall.",
    ),
]
