# -*- coding: utf-8 -*-
"""Book 5 pass 2 (11 Oct 2026), part 1: fact fixes, additions to existing chapters, pointers to Part IV, Book 4, Book 8
and Book 9 by title, analog-first notes, On the Job notes, new practice problems, Appendix A and C additions.
Block kinds: H2, P, PL (bold lead + text), EQ, WE (title, problem, solution), FIG (file, caption, alt), B (bullet).
NEW is a list of (chapter, anchor, blocks); anchor None = before the chapter's closing paragraph (the one before
From the Bench), else (style, text-prefix) of the paragraph to insert before."""
B1 = 'Book 1, Foundations of Electronics'
B4 = 'Book 4, RF, Microwave, and Transceivers'
B8 = 'Book 8, Firmware and Software for Electronics'
B9 = 'Book 9, Test and Measurement Instruments'
B2 = 'Book 2, Circuits, Components, and Control'
B3 = 'Book 3, Semiconductor Physics and Devices'
def q(t): return '"' + t + '"'
FIX = [
# front matter
("Part III, Chapters 16 to 21, applies the modem to whole systems: ranging and positioning, interleaving and error detection, massive MIMO and beamforming, interference and the cellular SINR, satellite links and non-terrestrial networks, and the low-energy IoT radios.",
 "Part III, Chapters 16 to 21, applies the modem to whole systems: ranging and positioning, interleaving and error detection, massive MIMO and beamforming, interference and the cellular SINR, satellite links and non-terrestrial networks, and the low-energy IoT radios. Part IV, Chapters 22 to 25, follows the same arithmetic into hardware and out to new uses: the modem in FPGA and ASIC logic, signal processing for radar, microphone arrays, and sensor fusion, communication over fiber and through the air on light, and a network of LoRa, BLE, and Wi-Fi nodes the reader can build."),
("and the answers to every practice problem are in Appendix B.",
 "and every practice problem is worked in full in Appendix B, with the idea, the numbers, a check, and the usual mistake."),
("This book uses those results where it needs them and does not recompute them.",
 "This book uses those results where it needs them and does not recompute them. Readers who want the firmware that runs these radios on a microcontroller will find it in " + B8 + "."),
("so the reader can redo the arithmetic when the next release changes it.",
 "so the reader can redo the arithmetic when the next release changes it. Where a circuit can do a job without a processor, the book shows that version first: an FM receiver built around an IF strip, an FSK tone decoder, a Costas loop as it was first built, an infrared link keyed by a 555 timer. Those are mostly hobby and education builds today, and the text says so where they appear; they are taught because they make the integrated chips of real products understandable. Learn it here, buy the IC at work."),
# Chapter 7: the coding-gain example counted the rate loss twice
("Solution. Doubling the bandwidth to keep the rate doubles the noise, a 3 dB loss, so the net improvement is 9 − 3 = 6 dB. In free space, range scales as 10^(6/20) = 2.0: the code doubles the range at the same transmitter power and bit rate, at the cost of twice the spectrum.",
 "Solution. Coding gain is measured in Eb/N0, with Eb the energy per information bit, and that bookkeeping already includes the rate loss. Keeping the information rate means keeping the same received power per information bit; the noise density N0 does not change when the band widens. The received power needed therefore falls by the full 9 dB. The SNR in the doubled band does fall by 3 dB, but the code is designed to work at that lower SNR. In free space range scales as 10^(9/20) = 2.8: the code nearly triples the range at the same transmitter power and bit rate, at the cost of twice the spectrum. Subtracting another 3 dB for the wider band would count the rate loss twice."),
# hinge words and soft quantities
("the tuner's gain control has to keep the strongest station just below full scale,", "the tuner's gain control has to keep the strongest station a little below full scale,"),
("so the loop must track continuously, not just once at the start.", "so the loop must track continuously, not only once at the start."),
("still just above the cap, so the cell edge is set here.", "still 2 dB above the cap, so the cell edge is set here."),
("The scheduler would pick the MCS whose efficiency is just below 4.07,", "The scheduler would pick the MCS whose efficiency is the highest below 4.07,"),
("DL-TDOA, just as a GNSS receiver does", "DL-TDOA, as a GNSS receiver does"),
("not just the battery life of the devices it moves?", "not only the battery life of the devices it moves?"),
# Chapter 21: tag-chip sensitivity (Impinj M830/M850 data sheet: -25.5 dBm read sensitivity)
("a modern tag chip such as the Impinj M800 series wakes at about −24 dBm,", "a modern tag chip such as the Impinj M830 reads at about −25.5 dBm,"),
("a −24 dBm chip adds about 60 % to the free-space figure.", "a −25.5 dBm chip such as the M830, 5.5 dB better, multiplies the free-space figure by 10^(5.5/20) = 1.9."),
# Chapter 21 closing: Part III ends here now
("The IoT radios close the book's tour from Shannon's bound to a sensor on a coin cell.", "The IoT radios close Part III's tour from Shannon's bound to a sensor on a coin cell."),
("the boards, packages, and the emission tests that every one of them must pass are Book 7's.",
 "the boards, packages, and the emission tests that every one of them must pass are Book 7's. Part IV follows the modem into FPGA and ASIC logic, turns the same signal processing toward sensing and toward light, and ends with a network of the reader's own nodes."),
]
NEW = []
# ---------------- Chapter 1
NEW.append((1, None, [
('PL', 'Measure it yourself. ', "A PAM4 eye, its three openings, and the instruments that measure them are described in " + B9 + ", in its chapter " + q("Digital Modulation Quality: Constellations, EVM, MER, and Eyes") + ". Chapter 24 of this book follows PAM4 onto optical fiber, where the same three eyes cost less than 9.5 dB because a photodiode turns optical power into current."),
]))
# ---------------- Chapter 3
NEW.append((3, None, [
('PL', 'Measure it yourself. ', "ACLR, occupied bandwidth, and the complementary cumulative distribution of a signal's peaks are measured as " + B9 + ", describes in " + q("Transmitter Spectrum: Channel Power, ACLR, Emission Masks, and CCDF") + "."),
]))
# ---------------- Chapter 4
NEW.append((4, None, [
('PL', 'Measure it yourself. ', "How a vector signal analyzer computes EVM, and why its reading depends on the reference filter and the equalizer setting, is in " + B9 + ", chapter " + q("Digital Modulation Quality: Constellations, EVM, MER, and Eyes") + "."),
]))
# ---------------- Chapter 6
NEW.append((6, None, [
('PL', 'Measure it yourself. ', "Demodulating a Wi-Fi 6 or 5G NR signal on an analyzer, with per-subcarrier EVM and the spectral flatness this chapter predicts, is the subject of " + B9 + ", chapter " + q("OFDM Systems: Wi-Fi 6 and 7, LTE, and 5G NR") + "."),
]))
# ---------------- Chapter 8: analog first, the duplexer in the system
NEW.append((8, ('H2', '8.8 '), [
('PL', 'Analog first. ', "Before the software receiver, the hardware one. A classic broadcast FM receiver is a superheterodyne: an RF stage, a mixer to a 10.7 MHz intermediate frequency, a ceramic filter about 180 to 280 kHz wide that sets the selectivity, a limiting amplifier that strips off amplitude noise, and a quadrature detector whose output is the audio. No line of code is involved, and every stage can be probed with an oscilloscope. Building one is hobby and education work today, and " + B4 + ", builds receivers of this kind in " + q("Receivers and Transmitters You Can Build") + ". A 2026 product uses a single-chip receiver such as the Silicon Labs Si47xx family instead, and inside that chip is a digital chain much like the one below: learn the stages here, buy the IC at work."),
]))
NEW.append((8, None, [
('H2', '8.9 Filters and duplexers in the system'),
('P', "Everything in this chapter assumed that the receiver hears only the band it wants. A phone breaks that assumption with its own transmitter. In frequency-division duplex the handset transmits and receives at the same moment on two frequencies: in LTE Band 7 and NR n7 the uplink is 2500 to 2570 MHz and the downlink 2620 to 2690 MHz, a duplex gap of only 50 MHz. The transmitter delivers about 23 dBm at the antenna, so its power amplifier puts out about 26 dBm, while the receiver must find a signal near −100 dBm. Two things leak across. The transmit carrier itself, 50 MHz or more away, can drive the low-noise amplifier into compression or mix with other signals; the receive filter must suppress it. And the amplifier's own wideband noise, which falls inside the receive band, adds directly to the receiver's noise floor; only the transmit filter can remove that, because once it is in the receive band no later filter can separate it from the wanted signal."),
('P', "The two filters together are the duplexer, and its isolation in each band is a system number that follows from the sensitivity budget of Section 8.5. Time-division duplex, the 3.5 GHz band n78 for example, avoids the duplexer by switching between transmit and receive, but it still needs a filter against the neighbors. Coexistence inside one phone adds more cases: Wi-Fi at 2.4 GHz sits directly against LTE Band 40 below it and within 13 MHz of Band 41 above it, so a phone that runs both at once needs filters with steep skirts in both radios. Carrier aggregation multiplies the problem, because several bands must be received at once through one antenna, and the duplexer becomes a quadplexer or a multiplexer. A 2026 flagship phone carries dozens of such filters. Their technology, the surface- and bulk-acoustic-wave resonators that make the steep skirts possible in a few square millimeters, is " + B4 + ", in its chapter " + q("Acoustic and Micro-Mechanical Filters: SAW, BAW, XBAR, and the Smartphone Front End") + "; what this section adds is where the isolation requirement comes from."),
('EQ', "allowed noise = floor + 10 log₁₀(10^(D/10) − 1),   isolation = PA noise density − allowed noise"),
('WE', 'Worked Example 8.6', "Problem. A Band 7 handset receiver has a 4 dB noise figure and may lose at most 0.5 dB of sensitivity to its own transmitter. The power amplifier's output noise in the receive band is −128 dBm/Hz, and its carrier leaves the amplifier at +26 dBm. The low-noise amplifier tolerates a blocker of −30 dBm at its input. Find the receive-band isolation the duplexer's transmit filter must provide, and the transmit-band rejection its receive filter must provide.",
 "Solution. The receiver's noise floor is −174 + 4 = −170 dBm/Hz. A 0.5 dB desense allows added noise of 10 log₁₀(10^0.05 − 1) = −9.1 dB relative to the floor, −179.1 dBm/Hz. The transmit filter must therefore attenuate the amplifier's −128 dBm/Hz in the receive band by 51.1 dB. The carrier must fall from +26 dBm to −30 dBm at the low-noise amplifier, 56 dB of rejection at the transmit frequency in the receive path. Both figures are in the range a good acoustic duplexer delivers, 50 to 60 dB, and neither leaves much margin, which is why the antenna, the duplexer, and the amplifier's noise are specified together."),
('FIG', 'b5n_duplexer.png', "Figure 8.3 — A Band 7 duplexer in the system (Worked Example 8.6). The transmit filter must push the amplifier's −128 dBm/Hz of receive-band noise 51.1 dB down, below the −179.1 dBm/Hz that costs the receiver 0.5 dB; the receive filter must take the +26 dBm carrier 56 dB down to the −30 dBm the low-noise amplifier tolerates. The filter curves are illustrative.",
 "Two panels. Top: frequency axis from 2450 to 2740 MHz with the uplink band 2500-2570 MHz and the downlink band 2620-2690 MHz shaded, the transmit and receive filter responses as two passbands, and arrows marking 51.1 dB of transmit-filter isolation in the receive band and 56 dB of receive-filter rejection at the transmit carrier. Bottom: a level ladder in dBm per hertz showing the amplifier noise at −128, the receiver floor at −170, and the allowed added noise at −179.1."),
('PL', 'Where this continues. ', "Chapter 19 meets the same arithmetic between operators, as adjacent-channel selectivity, and Chapter 25 between the radios of one gadget, where a LoRa node, a GPS receiver, and a Wi-Fi module share a board."),
('PL', 'Measure it yourself. ', "Software-defined radios used as instruments, with their limits, are in " + B9 + ", chapter " + q("The Budget Bench: NanoVNA, tinySA, SDRs, and Low-Cost Scopes and Supplies") + ", and the Python that drives them in " + B8 + ", chapter " + q("Python on the Bench") + "."),
]))
# ---------------- Chapter 9: analog first; fixed point pointer
NEW.append((9, ('H2', '9.1 '), [
('PL', 'Analog first. ', "Every digital filter in this chapter sits behind an analog one. Before the converter, only an analog filter can stop a signal from folding onto the wanted band, and its order sets how much the digital filters can relax: a fourth-order Butterworth falls 24 dB per octave beyond its corner, so a converter sampling at four times the corner frequency sees the band that folds onto its passband, which starts at three times the corner, 38 dB down from that filter alone. The active filters themselves, Sallen-Key and multiple-feedback stages built with an op-amp, are the subject of " + B2 + "."),
]))
NEW.append((9, None, [
('PL', 'Where this continues. ', "Chapter 22 puts these filters into FPGA and ASIC logic, where the word lengths of Section 9.5 become numbers of DSP slices and milliwatts. The firmware view, fixed-point formats and filters on a microcontroller, is " + B8 + ", chapter " + q("Fixed-Point Math and DSP") + "."),
]))
# ---------------- Chapter 10
NEW.append((10, ('H2', '10.3 '), [
('PL', 'Analog first. ', "The Costas loop was first an analog circuit: John Costas described it in 1956, with two multipliers, two low-pass filters, a third multiplier forming the phase error, and a voltage-controlled oscillator. A hobbyist can still build a phase-locked loop from a CD4046 chip and a handful of resistors and capacitors, and watch it lock on an oscilloscope. Every loop in this chapter keeps that structure; only the multipliers have become arithmetic."),
]))
NEW.append((10, None, [
('PL', 'Measure it yourself. ', "Crystal offsets in parts per million, and the references that measure them, are in " + B9 + ", chapter " + q("Counters, Timers, and Frequency References") + "."),
]))
# ---------------- Chapter 12
NEW.append((12, ('H2', '12.2 '), [
('PL', 'Analog first. ', "FSK needs no processor at either end. The Bell 202 standard sends 1200 baud with tones of 1200 and 2200 Hz, which amateur packet radio and APRS still use over ordinary FM voice radios; a function-generator chip such as the XR-2206 can key between the two tones, and a phase-locked tone decoder such as the XR-2211 turns them back into bits. The modulation index of Section 12.1 applies unchanged: 1000 Hz of tone spacing at 1200 baud is h = 0.83. A sound card and a few lines of software do the same job today, which is how most APRS receivers work; the chips remain an education build."),
]))
NEW.append((12, None, [
('PL', 'Where this continues. ', "Chapter 25 builds a LoRa mesh on these chirps, with its airtime and channel load. The firmware that drives the radio chips is in " + B8 + ", chapter " + q("BLE, LoRa, and GPS Firmware") + ", and the measurement of chirps and bursts in " + B9 + ", chapter " + q("Bursts, Chirps, and Pulses: BLE, LoRa, FMCW Radar, and Pulsed RF") + "."),
]))
# ---------------- Chapter 15
NEW.append((15, None, [
('PL', 'Where this continues. ', "On the firmware side, a Wi-Fi client that publishes small messages lives in the one-packet corner of Figure 15.1; " + B8 + ", chapter " + q("Wi-Fi and MQTT") + ", shows the code, and Chapter 25 of this book counts the energy of each wake-up."),
]))
# ---------------- Chapter 16: FMCW radar processing
NEW.append((16, None, [
('H2', '16.8 FMCW radar: from beat tones to a range-Doppler map'),
('P', "Radar measures range with the same arithmetic as the rest of this chapter, but it times its own echo. A frequency-modulated continuous-wave radar sweeps its carrier linearly by a bandwidth B in a time Tr, a slope S = B/Tr, and mixes the echo with the sweep still being transmitted. An echo from range R arrives 2R/c late, so it differs from the transmitted sweep by a constant beat frequency fb = 2RS/c. One FFT of the samples of each chirp turns range into frequency, and its bin spacing gives a range resolution of c/(2B), set by the swept bandwidth alone, the same bandwidth rule as Section 16.1. The largest range is set by the highest beat frequency the receiver's intermediate-frequency chain passes."),
('P', "Velocity comes from a second FFT across chirps. A target moving at radial velocity v changes its round-trip phase by 4πvTc/λ from one chirp to the next, so the phase of its range bin rotates at the Doppler rate. Taking an FFT along the slow-time axis, chirp by chirp, gives the velocity, with a resolution of λ/(2NTc) for N chirps of period Tc and an unambiguous span of ±λ/(4Tc). The result is a range-Doppler map, and a third FFT across the receive antennas adds angle, Chapter 23. The front end that makes the chirp, at 24, 60, and 77 GHz, is " + B4 + ", in " + q("FMCW Radar Front Ends at 24, 60, and 77 GHz") + "; the processing is this book's."),
('EQ', "fb = 2RS/c,   ΔR = c/(2B),   vmax = λ/(4Tc),   Δv = λ/(2N Tc)"),
('WE', 'Worked Example 16.8', "Problem. A Texas Instruments IWR6843 radar at 62 GHz sweeps 4 GHz in 40 µs, repeats a chirp every 50 µs, and sends 128 chirps per frame. Its intermediate-frequency chain passes up to 10 MHz. Find the range resolution, the maximum range, the beat frequency of a target at 6 m, the velocity resolution and span, and the raw data per frame for four receivers with 512 complex samples per chirp of 4 bytes each.",
 "Solution. ΔR = 2.998 × 10⁸/(2 × 4 × 10⁹) = 3.75 cm. The slope is 4 GHz/40 µs = 10¹⁴ Hz/s, so the 10 MHz limit corresponds to Rmax = 10⁷ × 2.998 × 10⁸/(2 × 10¹⁴) = 15.0 m, and a target at 6 m beats at 2 × 6 × 10¹⁴/2.998 × 10⁸ = 4.00 MHz. At 62 GHz, λ = 4.84 mm, so vmax = 4.84 mm/(4 × 50 µs) = ±24.2 m/s and Δv = 4.84 mm/(2 × 128 × 50 µs) = 0.38 m/s over a 6.4 ms frame. The raw data are 4 × 128 × 512 × 4 bytes = 1.05 MB per frame, 164 MB/s at a frame every 6.4 ms, which is why the chip carries its own DSP and a hardware FFT accelerator and sends only a list of detected points to the host."),
('FIG', 'b5n_rangedoppler.png', "Figure 16.2 — A range-Doppler map computed from simulated IWR6843 chirps (Worked Example 16.8): 3.75 cm range bins and 0.38 m/s velocity bins. Two targets, at 3.0 m moving toward the radar at 1.0 m/s and at 7.5 m moving away at 2.0 m/s, appear as two peaks, approach plotted as negative velocity, after a range FFT on each chirp and a Doppler FFT across 128 chirps.",
 "A heat map with range from 0 to 15 m on the horizontal axis and radial velocity from −24 to +24 m/s on the vertical axis. Two bright peaks stand out from a dark noise floor, one at 3.0 m and −1.0 m/s, the other at 7.5 m and +2.0 m/s, each labeled."),
('PL', 'Where this continues. ', "Chapter 23 detects the peaks with a constant-false-alarm-rate threshold and adds angle from a virtual antenna array. GPS and LoRa firmware are in " + B8 + ", chapter " + q("BLE, LoRa, and GPS Firmware") + ", and the point clouds a radar produces are fused with other sensors in its chapter " + q("Sensor Fusion: IMU Filters, Kalman, and SLAM Basics") + "."),
]))
# ---------------- Chapter 19
NEW.append((19, None, [
('PL', 'Where this continues. ', "Section 8.9 applies the ACLR and ACS arithmetic of Section 19.4 inside one handset, where the neighbor is the phone's own transmitter."),
]))
# ---------------- Chapter 21
NEW.append((21, None, [
('PL', 'Where this continues. ', "Chapter 25 builds a network of these radios, with LoRa, BLE, Thread, and Wi-Fi nodes and the energy of each report. Sleep modes in firmware are " + B8 + ", chapter " + q("Low Power and Sleep") + ", and measuring a current that jumps from microamperes to milliamperes in a microsecond is " + B9 + ", chapter " + q("Electronic Loads and Battery Simulators") + "."),
]))
RENAME = []
PNEW = {
8: ["A handset receiver with a 5 dB noise figure may lose at most 1 dB of sensitivity to its own transmitter. The power amplifier's noise in the receive band is −130 dBm/Hz. How much receive-band isolation must the duplexer provide?"],
12: ["Bell 202 AFSK sends 1200 baud with tones of 1200 and 2200 Hz. Find the modulation index h."],
16: ["An FMCW radar sweeps 4 GHz in 40 µs. Find its range resolution and the beat frequency of a target at 6 m."],
}
JOB = {
8: "Who uses this: wireless system engineers at phone, router, and module makers; SDR and test engineers at instrument companies; and the developers of open-source receivers. Typical chips are the AD9361-class transceivers, Qualcomm, MediaTek, and Broadcom Wi-Fi and cellular chipsets, and RTL-SDR, HackRF, ADALM-Pluto, and USRP boards in the lab. The tools are GNU Radio, Python with NumPy, MATLAB, and a vector signal analyzer. A realistic task: a new Wi-Fi 7 router fails its 4096-QAM rate at 3 m; capture its signal with a USRP, compute EVM against the −38 dB requirement of Chapter 4, and find which term of the EVM budget, phase noise, amplifier, or I/Q imbalance, is over its share.",
15: "Who uses this: modem firmware and physical-layer software engineers at chipset vendors, network performance engineers at operators, and the Wi-Fi engineers who answer every complaint that a link is slower than its label. They work with Qualcomm, MediaTek, Broadcom, and Espressif chipsets, drive tests and packet captures, iperf, Wireshark, and the log tools of each vendor. A realistic task: a customer's ESP32-S3 camera node streams at 3 Mbit/s over a link that reports a 72 Mbit/s PHY rate; show from the airtime arithmetic of Section 15.8 that small unaggregated packets, not the radio, set the limit, and fix the firmware's buffer size.",
19: "Who uses this: radio network planning and optimization engineers at operators and their contractors, and coexistence engineers who set guard bands between operators and between radios in one product. The tools are planning software with propagation models, drive-test receivers, and spreadsheets of exactly the SINR and noise-rise arithmetic of this chapter. A realistic task: decide whether adding four small cells to a stadium raises capacity or only interference, by computing the SIR at the seats for each site before anyone climbs a pole.",
21: "Who uses this: embedded and IoT product engineers, a large and growing share of the profession, at makers of meters, locks, sensors, wearables, and smart-home devices. Typical parts are the Nordic nRF52840 and nRF54 series, the Espressif ESP32-C6 and ESP32-H2 for Thread and Zigbee, the Semtech SX1262 for LoRa, and NB-IoT modules from Quectel or u-blox. The tools are a power profiler, a current probe or source-measure unit, the vendor's radio test firmware, and a spreadsheet battery model. A realistic task: a smart thermostat's battery-backed room sensor must last two years on two AA cells; measure the charge of one report on a power profiler, compute the life at the chosen interval, and find the sleep-current leak that the model exposes.",
}
APPA = [
"Duplexer budget: allowed added noise = floor + 10 log₁₀(10^(D/10) − 1) for a desense of D dB; 0.5 dB allows −9.1 dB, 1 dB allows −5.9 dB.",
"FMCW radar: fb = 2RS/c with slope S = B/Tr; ΔR = c/(2B); vmax = λ/(4Tc); Δv = λ/(2NTc). Detection threshold for exponential noise T = −ln(Pfa) × mean; cell-averaging CFAR T = N(Pfa^(−1/N) − 1).",
"Arrays: phase step between elements 2π(d/λ) sin θ; virtual array Ntx × Nrx; resolution ≈ 2/N rad at broadside; no spatial aliasing for d ≤ λ/2. Delay-and-sum gain 10 log₁₀M in uncorrelated noise. Fusion: 1/σ² = 1/σ1² + 1/σ2²; complementary filter α = τ/(τ + Δt).",
"Fixed point: SQNR ≈ 6.02B + 1.76 − (PAPR − 3) dB; FFT word growth log₂N bits; CORDIC gain 1.6468 (scale by 0.6073), about one bit of angle per iteration. ASIC versus FPGA break-even volume = NRE/(FPGA unit cost − ASIC unit cost).",
"Optics: received power = launch − α L − connector and splice losses; photocurrent I = R P; 1 dB of optical power is 2 dB of electrical SNR in a thermal-noise-limited receiver. Spectral width Δλ ≈ λ²B/c; dispersion spread Δτ = D L Δλ, D ≈ 17 ps/(nm·km) at 1550 nm; reach for one symbol of spread L ≈ c/(D λ² B²). DP-16QAM carries 8 bits per symbol; PAM4 eyes cost 4.8 dB in optical power.",
"LoRa airtime: Tsym = 2^SF/B; payload symbols = 8 + ⌈(8PL − 4SF + 28 + 16 CRC − 20 IH)/(4(SF − 2DE))⌉ × (CR + 4); time on air = (preamble + 4.25 + payload symbols) Tsym. Radio horizon ≈ 4.12(√h1 + √h2) km with h in meters; first Fresnel radius at midpoint ≈ 17.32 √(d/(4f)) m with d in km and f in GHz. RSSI distance d = d0 × 10^((P0 − RSSI)/(10n)).",
]
APPB_INTRO = "Each answer below is worked in full: the idea that unlocks the problem, the numbers, a check by a second route or an order of magnitude, and the mistake most often made. Values are rounded at the end, not at each step."
APPC = [
"Mark Horowitz, \"Computing's Energy Problem (and What We Can Do About It),\" ISSCC 2014, for energy per operation (Chapter 22); AMD UltraScale+ DSP48E2 and Zynq RFSoC documentation; Ray Andraka, \"A Survey of CORDIC Algorithms for FPGA Based Computers,\" 1998 (Chapter 22).",
"Mark A. Richards, Fundamentals of Radar Signal Processing, for FMCW processing and CFAR (Chapters 16 and 23); Texas Instruments IWR6843 data sheet and \"The Fundamentals of Millimeter Wave Sensors\"; STMicroelectronics VL53L1X data sheet; Jacob Benesty, Jingdong Chen, and Yiteng Huang, Microphone Array Signal Processing; Bluetooth Core Specification 5.1 direction finding (Chapters 16, 23, and 25).",
"Govind P. Agrawal, Fiber-Optic Communication Systems, for link budgets and dispersion; OIF 400ZR Implementation Agreement; IEEE 802.3bs for 400GBASE-DR4; IEEE 802.11bb for light communication; C. H. Bennett and G. Brassard, \"Quantum Cryptography: Public Key Distribution and Coin Tossing,\" 1984; NIST FIPS 203 (Chapter 24).",
"Meshtastic documentation for modem presets and hop limits; Semtech SX1262 data sheet and LoRa airtime application note AN1200.13; Espressif ESP32-S3 and ESP32-C6 data sheets; ISO 11898 for CAN; NEC infrared remote protocol documentation (Chapters 24 and 25).",
]
