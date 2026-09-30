# APPENDIX — The Scientific Detail

## How to Read These Notes

Each note A*n* twins popular chapter *n*. Units are SI unless stated. *c* is the speed of light, *G* Newton’s constant, *ħ* the reduced Planck constant, *k* Boltzmann’s constant. A scale factor *a(t)* is dimensionless; today *a₀ = 1*. Redshift *z* obeys *1 + z = 1/a* for light emitted at *a*.

String theory, whenever it appears: a mathematical framework that **cannot currently be tested**. It has not produced a unique, risky prediction that would kill the whole idea if the experiment came out otherwise.

These notes are denser than the chapters they twin. They are still this book: short sentences, named measurements, temperatures on the claim. They are not a textbook. If a formula is numbered (1)–(18), the number is a handle, not a homework set.

---


## A0. Three Temperatures of Claim

**Hot:** repeated measurement, used to predict new ones. **Warm:** best model, real gaps. **Cold:** allowed by the equations, not selected by the data. A claim can change temperature. The oven is the sky, not the seminar.

Inflation is the cleanest change-of-temperature in this book. In 1981 Guth’s paper was a proposal: a brief early burst of repulsive stretch that could solve the horizon, flatness, and monopole problems the hot bang, taken alone, cannot. The first (“old”) inflation stalled on how to end the burst without emptying the universe of matter. In 1982 Albrecht–Steinhardt and Linde supplied slow-roll exits. That was still a model. What warmed the *local* burst was later data: a sky that is spatially flat to a percent; a primordial spectrum with *n_s* a few percent below 1 (A14); acoustic peaks in the leftover glow that match a nearly scale-invariant twitch stretched outside the Hubble radius and then brought back. Those are not proofs that a particular inflaton exists in a detector. They are reasons the local burst is no longer a 1981 maybe.

A claim can also cool. In March 2014 BICEP2 announced *B*-mode polarization at degree scales and offered a tensor-to-scalar ratio *r ~ 0.2*. Primordial gravitational waves from a high-scale burst would have been a trophy. Within a year Planck’s dust maps and the joint BICEP/Keck–Planck analyses showed that Galactic dust, not a primordial tensor background, carried the signal. The measurement was real. The interpretation was not. Current combinations (BICEP/Keck plus Planck) put *r ≲ 0.03–0.04* at 95% confidence, depending on the data cut. High-scale inflation of the 2014 headline is colder than it was on announcement day. The local burst is still warm. Eternal inflation — self-reproducing pocket nucleations, a measure problem, no unique risky number — did not inherit the warming. It stays allowed and unselected.

Temperature is a discipline, not a mood. “We have a picture of a black-hole shadow” is hot. “The interior is a bounce into a baby universe” is cold. String landscapes, when named, inherit equation (18). Use the labels in that spirit for the rest of these notes.

---

## A1. Relativity of Simultaneity

Einstein synchronization: a clock at spatial coordinate *x* is set by a light signal from a master clock, assuming the one-way speed is *c*. That assumption is a convention that special relativity makes consistent. Observers with relative velocity *v* along *x* then disagree on which events with Δ*x* ≠ 0 are simultaneous. The desynchronization is, to first order in *v/c*,

*Δt = v Δx / c²*.

This is not a signal. Nothing travels from here to Andromeda in the instant you take a step. It is a fact about how two inertial frames slice the same loaf.

Worked numbers, Andromeda at Δ*x*/c ≈ 2.5 × 10⁶ yr. Walking, *v ≈ 1.4 m/s*, so *v/c ≈ 4.7 × 10⁻⁹*. Then *Δt ≈ 4.7 × 10⁻⁹ × 2.5 × 10⁶ yr ≈ 0.012 yr ≈ 4 days*. The kitchen walker and the kitchen stander do not share a “now” on Andromeda to better than a long weekend. An airliner, *v ≈ 250 m/s*, tilts the same slice by *~2 yr*. Earth’s orbital speed, *v ≈ 30 km/s*, tilts it by *~250 yr*. None of those numbers is a photograph of Andromeda’s navy. Light from M31 is 2.5 million years late for everyone in the kitchen. The disagreement is about which events on that galaxy you *label* simultaneous with the casserole, not about which photons you receive.

At laboratory distances the same formula is tiny. Across a 10 m kitchen at walking speed, *Δt ~ 5 × 10⁻¹⁷ s* — below any clock you own. Relativity of simultaneity is therefore easy to miss and easy to oversell. It is a convention-plus-Lorentz fact. It becomes a plot point only when *Δx* is huge or *v* is not small. Chapter 1’s kitchen is the first case.

---

## A2. Minkowski Coordinates and the Interval

An event is a point in a 4-manifold. In inertial coordinates the interval is

**(1)**  *ds² = −c² dt² + dx² + dy² + dz²*

*(signature convention −+++).*

*ds² < 0* timelike, *= 0* lightlike, *> 0* spacelike. *ds²* is invariant: every inertial observer computes the same number. The split into *dt* and *dℓ* is not. That is the entire content of “the loaf has a geometry; the slices are ours.”

Signature is a convention. Particle physicists often write *+−−−*, so the inequality for “timelike” flips. The physics does not. This book keeps −+++ so that spatial distances look like school geometry and proper time satisfies *c² dτ² = −ds²* along a worldline.

A number. Two sparks in a lab: Δ*t* = 5.00 μs, Δ*x* = 1.00 km, Δ*y* = Δ*z* = 0. Light would need 3.34 μs to cover that kilometer, so the pair is timelike. Equation (1) gives *ds² / c² = −(5.00 × 10⁻⁶)² + (10³ / c)² ≈ −1.38 × 10⁻¹¹ s²*. The proper time between them, for the inertial traveler who visits both, is *Δτ = √(−ds²)/c ≈ 3.72 μs*. A different inertial frame can assign 6 μs and a shorter Δ*x*; it cannot change *Δτ*. Swap the numbers to Δ*t* = 2.00 μs and the same kilometer and *ds² > 0*: spacelike. No traveler visits both. Different frames can disagree on order.

Null intervals are the paths of light in vacuum. They are the boundary of A3’s cones. If you take nothing else from this note, take invariance: the interval is the thing the universe keeps. Your clock and your ruler are how you spend it.

---

## A3. Light Cones and Lookback Time

**(2)**  *ds² = 0*  ⇒  *dℓ = c dt*

The past light cone of an event *p* is the set of events that can signal to *p*. The future cone is the set *p* can signal to. Everything else is elsewhere: real, and unavailable as a cause or an effect of *p*. Equation (2) is the generators of those cones in inertial coordinates. In a curved, expanding cosmology the same idea survives: null geodesics still bound causal contact; the scale factor *a(t)* changes how far a null ray gets.

Lookback time to redshift *z* is the integral of *dt = da / (a H(a))* from *a = 1/(1+z)* to *a = 1*. It is not “distance over *c*” except as a slogan. In a matter-plus-Λ fit with *H₀ ≈ 67–73 km s⁻¹ Mpc⁻¹*, light emitted at *z = 1* has been traveling *~7.8 Gyr*; at *z = 2*, *~10.5 Gyr*; at last scattering *z_* ≈ 1090, the travel time is the age of the universe minus *~3.8 × 10⁵ yr*. The leftover glow is a baby picture with the baby long gone. The Sun in your sky is eight minutes old; Jupiter tonight is *~30–50 min* old depending on opposition; M31 is 2.5 Myr old in photons.

The night sky is the past cone, sampled. Astronomy is the only time travel we have: we receive news that already lies to our past. You cannot answer the news. You can wait for later news from a later event on the same worldline. Chapter 3’s lateness is geometry, not an instrument limit.

---

## A4. Tilting the Simultaneity Slice

**(3)**  *t′ = γ (t − v x / c²)*

*where γ = 1 / √(1 − v²/c²).*

A plane *t′ = const* is tilted in *(t, x)*. The slope is *v/c²*. At kitchen *v* the tilt is invisible on kitchen *x* and enormous on megaparsec *x* (A1). The Andromeda paradox is this tilt: two people who meet in a kitchen, one walking, assign different “present” events to a galaxy 2.5 million light-years away. They do not assign different photons in the eyepiece.

Reality-transfer arguments (Rietdijk 1966; Putnam 1967) take the tilt as a metaphysical conveyor: if event *A* is present-for-me and event *B* is present-for-you-when-you-share-*A*, then *B* is already real-for-me. The chain is then run around the loaf until every event is “already real.” The Lorentz transformation in (3) is not on trial. The extra premise is: “present ⇒ real,” plus transitivity of that privilege across observers who do not share a global plane. This book rejects the privilege of the plane. The manifold plus metric is the inventory. A slice is a bookkeeping surface. Calling the slice “the now” does not promote it to a moving spotlight.

At *v* not small, *γ* matters. Equation (3) is the exact boost, not the first-order slogan. For GPS satellites (*v ≈ 3.9 km/s*, *γ − 1 ≈ 8.5 × 10⁻¹¹*) the *vx/c²* term is a daily desynchronization you must correct or the navigation solution drifts by kilometers (A5). For a *0.1 c* cruise, *γ ≈ 1.005*; for *0.9 c*, *γ ≈ 2.3*. The twin effect (A5) is the integral of proper time along two different worldlines that meet twice. The Andromeda tilt is what those worldlines do to *distant* labels between the meetings.

---

## A5. Proper Time and the Twin Effect

Proper time along a timelike worldline: *c² dτ² = −ds²*. Between two meetings, the inertial path maximizes *τ*. That is the twin “paradox”: the accelerated twin has the smaller elapsed proper time. There is no paradox in the geometry. The worldlines are different lengths. The traveling twin is not inertial for the whole trip; the stay-at-home twin is (idealized). They meet twice and compare wristwatches. The comparison is a scalar. Everyone agrees.

Hafele–Keating (October 1971; *Science* 1972) flew commercial airliners around the world with cesium clocks and compared them to a ground set. Eastbound, Earth-rotation velocity adds to the jet; westbound it subtracts. Predicted: eastbound *−40 ± 23 ns*, westbound *+275 ± 21 ns* (special-relativistic plus gravitational pieces together). Measured: *−59 ± 10 ns* and *+273 ± 7 ns*. The signs and the hundreds of nanoseconds are the result. A classroom “clocks are metaphysical” speech does not survive that table.

Muons. Mean proper lifetime *τ₀ ≈ 2.20 μs*. Atmospheric muons are born *~10–20 km* up at *v* so close to *c* that *γ* is typically *~10–20*. Without dilation they would decay in a few hundred meters of flight; they reach the basement. Storage-ring measurements (CERN muon storage ring; later *g−2* rings) hold *γ ≈ 29.3* and find the lab lifetime *γ τ₀* to parts in a thousand. That is the twin effect with a particle that does not file a flight plan.

GPS. Orbit *v ≈ 3.9 km/s* gives a special-relativistic slowing *~7 μs/day*. The weaker gravitational potential at altitude gives a general-relativistic speeding *~46 μs/day*. Net: the satellite clock runs *~38–39 μs/day* fast versus a geoid clock if you do not correct. Light travels 11 km in 38 μs. Uncorrected, the navigation solution is junk in hours. Both corrections are tens of microseconds per day and opposite in sign, as the chapter said. The system is an industrial twin-plus-well clock.

---

## A6. Causal Structure: Past, Future, Elsewhere

At an event *p*, *I⁻(p)* is the chronological past (events that can reach *p* on a future-timelike curve), *I⁺(p)* the chronological future, and the remainder of the manifold, minus the light-cone boundary, is spacelike-separated “elsewhere.” Causal past and future *J±(p)* include the null generators. These are the verbs the loaf actually has. “Now” is not among them.

A Cauchy surface is a spacelike 3-surface that intersects every inextendible causal curve exactly once. Data on a Cauchy surface determine the solution in the domain of dependence. Presentism, as a physics claim rather than a mood, wants a preferred Cauchy surface that is “the present,” advancing. General relativity does not supply a preferred one. Different foliations are different bookkeeping. In Minkowski space every inertial *t = const* is a Cauchy surface; none is privileged by the metric. In generic GR, global hyperbolicity may fail (Cauchy horizons; A35). Where it holds, you still have a stack of surfaces, not a glowing edge.

The block — the 4-manifold plus metric as the inventory — is the default reading once you accept (1) and the Einstein equation as the dynamics of that metric. It is not a proof that “the future is already filmed” in a fatalist sense. It is a refusal to add a moving spotlight the equations do not contain. Local becoming, if you want the word, is along a worldline: proper time (A5). It is not a cosmic weather front.

---

## A7. FLRW: No Center, No Edge

The Friedmann–Lemaître–Robertson–Walker metric assumes homogeneity and isotropy on spatial slices: the same density and the same expansion rate at every comoving point, no preferred direction. In coordinates comoving with the cosmic fluid,

*ds² = −c² dt² + a(t)² [dχ² + f_K(χ)² dΩ²]*,

where *K = +1, 0, −1* labels spatial slices that are *S³*, *E³*, or *H³* (closed, flat, open), and *f_K* is *sin χ*, *χ*, or *sinh χ*. There is no privileged center on those slices any more than there is a center of the Earth’s surface. Every galaxy can think of itself as at rest in the Hubble flow. “Expansion into what?” is a category error: *a(t)* rescales proper distances *between comoving observers* on the slices. The manifold is not required to sit in a higher-dimensional room with a spare radial direction labeled “outside.”

Observationally, the leftover glow is isotropic to *~10⁻⁵* after the dipole is removed (A9). Galaxy surveys (2dF, SDSS, DESI) find homogeneity on scales *≳ 100–300 Mpc*, with the usual argument about whether a given catalog is large enough. Spatial curvature *Ω_k* is consistent with 0 at the percent level or better in Planck-like fits (A11). Flat and infinite is allowed. Flat and finite (a 3-torus) is allowed and not selected. Closed with a large radius is allowed. None of those options puts you at the middle of a bomb.

The “bang” is a hot, dense *state* of the slices in the past, not a point in a pre-existing box. At *a → 0* the classical description fails (A44). That failure is not a location you can visit.

---

## A8. Hubble–Lemaître Law and Redshift

**(4)**  *v = H₀ d*  (low *z*);  *1 + z = 1/a_emit*

*H₀* is *ȧ/a* today. Equation (4)’s velocity form is a local linearization: recession *v ≈ H₀ d* for *z ≪ 1*, where *d* is proper distance now and *v* is not a rocket velocity through a box. The exact observable is redshift. Photons stretch with the slice: a feature emitted at wavelength *λ_em* when the scale factor was *a_emit* arrives at *λ_obs = λ_em / a_emit*, hence *1 + z = 1/a_emit*. At *z = 1* the universe was half its present scale. At *z = 9* it was a tenth. At *z_* ≈ 1090 it was about a thousandth. Do not confuse *z* with lookback time; A3’s integral is the conversion, and it depends on the whole *H(z)* (A18).

Measured *H₀* still tensions. Planck-like early-universe fits (CMB acoustic scale plus the working ΛCDM inventory) give *H₀ ≈ 67.4 ± 0.5 km s⁻¹ Mpc⁻¹*. Late-universe distance ladders (Cepheids to Type Ia; SH0ES) give *H₀ ≈ 73 ± 1 km s⁻¹ Mpc⁻¹*. The gap is several times the quoted errors and has persisted through independent rungs and through *Gaia* parallaxes. That is a real problem for the working model, not a reason to deny expansion. Tip-of-the-red-giant-branch ladders and some strong-lens time delays sit in between or on one side or the other; they have not closed the case. This book treats *H₀* as measured twice, in tension, both measurements hot as measurements, the reconciliation warm-to-open.

Hubble’s original 1929 slope was *~500 km s⁻¹ Mpc⁻¹* and a universe too young for the rocks. The law was right; the calibration was not. The present tension is not that story again until someone shows which calibration, or which early-universe assumption, is the 1929 error. The law is not a center. It is *a(t)* made local.

---

## A9. The CMB as a Blackbody

FIRAS on COBE (Mather et al.; Fixsen 2009 compilation) measured the sky-averaged spectrum as a blackbody at

*T₀ = 2.72548 ± 0.00057 K*.

Residuals from a Planck function are at the level of tens of parts per million. That is the most precise blackbody in nature we have ever taken apart. A blackbody needs a thermal history: the photons were in equilibrium with a charged plasma, then decoupled, then free-streamed while *T ∝ 1/a* (8). A “tired light” or “stars in a fog” story does not produce this spectrum plus the acoustic-peak pattern.

The dipole, *ΔT ≈ 3.4 mK*, is our motion relative to the rest frame of the glow: *v ≈ 370 km/s* toward Leo (more carefully, toward galactic coordinates near *l ≈ 264°, b ≈ 48°*). Subtract that and the intrinsic anisotropies are *ΔT/T ~ 10⁻⁵* — tens to hundreds of microkelvin. Those are the seeds of A14, printed on the last-scattering surface.

Last scattering: hydrogen recombination drops the free-electron fraction and the Thomson optical depth *τ* falls through 1. Planck-like fits put the peak of the visibility function at *z_* ≈ 1090 (1089.80 ± 0.23 in the 2018 TT,TE,EE+lowE+lensing chain; the chapter’s 1090 is the right digit). The temperature then was *T_* = *T₀ (1 + z_*) ≈ 2970 K*, which this book rounds to *3000 K*. Age at last scattering: *≈ 380,000 yr*. Helium recombination is earlier and less visible. Reionization at *z ~ 6–9* puts a small extra *τ* on the large-scale polarization; it is not a second fireball.

Hot: the spectrum, the dipole as motion, the *10⁻⁵* map, last scattering at *z ~ 10³*. Warm: the detailed recombination code and the optical-depth tail. Cold: a craftsman who painted the blackbody (A34).

---

## A10. Thermal History, Minute by Minute

**(8)**  *T ∝ 1/a*  (photon temperature after e⁺e⁻ annihilation)

Equation (8) is the leftover glow’s thermometer once electron–positron annihilation has dumped its entropy into the photons (a factor *~ (11/4)^{1/3}* relative to the neutrinos). Before that, *T* still tracks *1/a* up to *g_** changes when species drop out of the bath. A radiation-dominated clock reads *t ~ 1 / T²* in natural units: hotter is younger.

A prose timeline, not a wallpaper. *t ~ 10⁻⁴³ s*, *T* at the Planck energy *~10³² K*: not a measurement; the classical metric is not to be trusted. A local inflationary burst, if it happened, ends somewhere around *t ~ 10⁻³⁶–10⁻³² s* in textbook sketches; *T_rh* after reheating is model-dependent (A13) and only required to sit above BBN. At *t ~ 10⁻⁶ s*, *T ~ 10¹³ K ~ 1 GeV*, the quark–gluon plasma hadronizes — inferred from heavy-ion experiments plus the cosmic expansion, not from a cosmic photograph. At *t ~ 0.01 s*, *T ~ 10¹¹ K ~ 10 MeV*: the chapter’s first rough mark; weak interactions still keep neutrinos and the *n/p* ratio in step. Neutrino decoupling: *t ~ 1 s*, *T ~ 1 MeV*. Electron–positron annihilation follows as *T* falls through *~0.5 MeV*, reheating the photons relative to the already-decoupled neutrinos. Big-Bang nucleosynthesis: *t ~ 1–3 min*, *T ~ 0.1–1 MeV* (below). Recess. Then a long wait. Recombination and last scattering: *t ~ 3.8 × 10⁵ yr*, *T ~ 3000 K*, *z_* ≈ 1090 (A9). The glow has been free-streaming since. Reionization by the first stars and nuclei: *z ~ 6–9*, a few hundred million years. Today: *T₀ = 2.725 K*, *t₀ ≈ 13.8 Gyr*.

Those marks are the working thermal history. They are not a filmed minute log. The ones with spectral or abundance teeth (BBN; the CMB) are hotter than the ones that are interpolation plus accelerator physics.

---

*Big-Bang Nucleosynthesis*

Neutron-to-proton freeze-out *n/p ≈ 1/6* when the weak rates fall behind the expansion at *T ~ 0.8 MeV*, then free decay (*τ_n ≈ 880 s*) toward *~1/7* by the time the deuterium bottleneck opens.

**(9)**  *Y_p ≈ 2 (n/p) / (1 + n/p) ≈ 0.25*

**(10)**  Deuterium bottleneck: D photodissociates until *T ≲ 0.1 MeV*.

Almost every neutron that survives is cooked into ⁴He. Equation (9) is why the helium mass fraction is a quarter and not a cosmic accident. Equation (10) is why the cooking waits three minutes: the bath is still full of gamma rays that break deuterium until *T* is low enough that *η × exp(−B_D / T)* drops, with baryon-to-photon ratio *η ≈ 6 × 10⁻¹⁰* from the CMB.

Observed *Y_p ≈ 0.24–0.25* (H II regions; primordial intercept). Deuterium, the most fragile useful thermometer, sits at *D/H ≈ 2.5 × 10⁻⁵* in high-*z* quasar absorbers, matching CMB *ω_b* at the ~10% level or better. ³He is messier (stars both make and destroy it). Lithium-7 remains in tension: Spite-plateau Population II stars show *A(Li)* a factor *~2–3* below the CMB-plus-BBN prediction. That is a real gap — stellar depletion, new physics, or both — not a reason to throw out *Y_p* and D/H. No detector has photographed the third minute. The abundances plus the expansion plus the weak rates are the courtroom.

---

## A11. Critical Density and the Cosmic Inventory

**(5)**  *ρ_c = 3 H₀² / (8π G)*

*Ω_i = ρ_i / ρ_c*. For *H₀ = 67.4 km s⁻¹ Mpc⁻¹*, *ρ_c ≈ 8.5 × 10⁻²⁷ kg m⁻³* — a few hydrogen atoms per cubic meter if it were all hydrogen, which it is not. For *H₀ = 73* the critical density is ~17% higher; *Ω* values quoted from the CMB are usually reported in combinations like *Ω_i h²* that do not care which *H₀* you prefer until you convert.

Planck-like inventory (round numbers this book uses): *Ω_b ≈ 0.05*, *Ω_c ≈ 0.27*, *Ω_Λ ≈ 0.68*, *Ω_k ≈ 0*, photons *Ω_γ ~ 5 × 10⁻⁵*, neutrinos a comparable few × *10⁻⁵* if masses are small. Mean baryon number density *n_b ~ 0.2 m⁻³* (one proton in a box a bit more than a meter on a side). Stars and the gas you can photograph are a fraction of *Ω_b*; most baryons are in the warm–hot intergalactic medium and other faint phases. Dark matter *Ω_c* is the extra pull (A17). Dark energy *Ω_Λ* is the shove (A18). They do not trade costumes.

Spatial curvature: *|Ω_k| ≲ 0.01* in standard fits, tighter if you assume the working model. That is “flat for practical purposes,” not a proof the 3-space is infinite (A38). Critical density is the density that would make a matter-only universe spatially flat. With *Λ*, the Friedmann equation still uses (5) as the unit; the geometry is *Ω_k = 1 − Σ Ω_i*.

---

## A12. Horizon, Flatness, and Relic Problems

Particle horizon in a radiation-dominated era grows as *~ ct*, more carefully *χ_p ~ 2ct / a* in comoving coordinates for *a ∝ t^{1/2}*. Opposite patches on the last-scattering surface, separated by ~1° or more on the sky today, had not been in causal contact in a pure hot-bang history. Yet the leftover glow agrees in temperature to *~10⁻⁵*. That is the horizon problem: a thermal agreement without a prior chance to thermalize.

Flatness: *|Ω − 1| ∝ 1/(a² H²)*. In decelerating eras (*radiation, matter*) this quantity *grows* toward the past, so *Ω ≈ 1* today to a percent requires *|Ω − 1| ≲ 10⁻¹⁶* at BBN and *~10⁻⁶⁰* near the Planck scale if you run the clock that far. That is a tuning if the bang is just a bang. It is automatic if a prior burst drives *aH* up exponentially and parks *Ω* near 1.

GUT-scale monopoles, if produced at a phase transition with *T ~ 10¹⁶ GeV*, freeze out with *n_M / s* large enough to overclose the universe by many orders unless they are never produced after a burst or are diluted by *≳ 10²⁵* in entropy. Other relics (domain walls, some moduli) tell similar stories. Inflation’s original sale was these three puzzles. The sale does not identify the inflaton (A13). It explains why a local burst was proposed, and why a burst that lasts *N ~ 50–60* e-folds (11) is the size of the proposal.

---

## A13. Slow-Roll and E-Folds

**(11)**  *N = ∫ H dt ≈ 50–60* needed to solve A12.

An e-fold is a factor *e* in *a*. Fifty e-folds is a stretch of *e⁵⁰ ~ 5 × 10²¹*; sixty is *~10²⁶*. That is the dilution that flattens, homogenizes, and hides relics. Exact *N* depends on the reheating temperature and the scales you care about; 50–60 is the working window, not a sacred integer.

Slow-roll parameters *ε = −Ḣ/H²*, *η = ε̇/(Hε)* ≪ 1 (or the potential versions *ε_V = (M_Pl²/2)(V′/V)²*, *η_V = M_Pl² V″/V*). While they stay small the burst continues; when *ε* reaches 1, inflation ends. Reheating converts vacuum-like energy (*w ≈ −1*) into a radiation bath. *T_rh* can sit anywhere from a few MeV (below that, BBN is wrecked) up toward GUT scales in optimistic models. No inflaton has been identified in a detector. No laboratory field has been shown to be the one.

What warmed the *idea* is A14’s spectrum plus A9’s flatness, not a named particle. High-scale models that predicted *r* large enough for BICEP2’s first claim cooled when the dust was subtracted (A0). Starobinsky-like *R²* and a range of plateau potentials remain compatible with *n_s ≈ 0.96–0.97* and *r* below present bounds. The Lyth bound roughly says *r ~ 0.01* already implies a super-Planckian field range; that is a theoretical discomfort, not a kill-shot. Compatibility is not a detection. String theory sometimes offers inflatons as a catalog. **The catalog cannot currently be tested.**

---

## A14. The Primordial Spectrum

**(12)**  *P_R(k) ∝ k^{n_s − 1}*

**(13)**  *n_s ≈ 0.96–0.97* (Planck)

Amplitude *A_s ≈ 2.1 × 10⁻⁹* at the pivot *k = 0.05 Mpc⁻¹*. A scale-invariant Harrison–Zeldovich spectrum is *n_s = 1*. The measured tilt a few percent below 1 is a slow-roll success: *n_s − 1 ≈ −2ε − η* (sign conventions as usual). Planck 2018: *n_s = 0.9649 ± 0.0042* in the baseline combination; later ACT/SPT/Planck combinations move the digit inside 0.96–0.97. Tensor-to-scalar ratio *r = P_T / P_R* is bounded: *r ≲ 0.036* (95%) from BICEP/Keck 2018 plus Planck, with the exact ceiling depending on the likelihood. That kills the 2014 *r ~ 0.2* headline. It does not kill a local burst.

The Mukhanov–Sasaki variable *v = z ℛ* quantizes the curvature twitch *ℛ* on a rigid expanding background. Modes freeze when they exit the Hubble radius (*k = aH*) and re-enter later as density seeds *δρ/ρ ~ 10⁻⁵* — the same order as *ΔT/T* on the leftover glow. Acoustic peaks in the CMB and the baryon acoustic feature in galaxy surveys (A18) are that twitch, oscillated and projected. Non-Gaussianity *f_NL* is consistent with 0 at the level slow-roll predicts (*f_NL ~ n_s − 1*). A large local *f_NL* would have been a different, colder story.

Hot: *A_s*, *n_s < 1*, acoustic physics. Warm: a slow-roll burst as the source. Cold: a named inflaton, a detected tensor background.

---

## A15. Eternal Inflation and the Measure Problem

If the quantum kick *δφ ~ H/2π* per Hubble time exceeds the classical roll down the potential, inflation self-reproduces: volume that is still inflating grows faster than volume that has exited. Pocket nucleations in a false-vacuum sea (Coleman–De Luccia) are a related picture with bubbles instead of a slowly rolling field. Both produce a multiverse of the Level II kind (A37). Neither is a detection.

The measure problem is that “most” is not defined. Volume-weighted measures favor pockets that inflate longest. Pocket-weighted measures count nucleations. Observer-weighted measures try to condition on galaxies or on Boltzmann brains. They disagree, sometimes by infinite factors. Anthropic cuts on *Λ* (A41) inherit this fog: Weinberg’s upper bound is a real inequality; turning it into a probability needs a measure you do not have.

Borde–Guth–Vilenkin (BGV): if the average Hubble rate along a past-directed geodesic is positive, that geodesic is past-incomplete. Eternal inflation, on this theorem, is not a past-eternal block. It does not prove a kitchen-time “before.” It proves that the inflating congruence cannot be extended indefinitely into the past as a regular, expanding spacetime. What replaces the incompleteness is A44’s problem, not a filmed first tick.

Temperature: local burst, warm (A13–A14). Eternal froth and a predictive measure, cold-to-warm at best. A landscape of string vacua as the menu, untestable by (18).

---

## A16. Sensitivity: From Quantum Noise to BKL Chaos

Inflationary *δφ* is chaotic in the colloquial sense: a *10⁻⁵* twitch, stretched across the sky, becomes the difference between a void and a cluster. It is not always chaotic in the formal attractor sense. Slow-roll backgrounds are often attractors in field space; the *noise* on top of them is what gets amplified into *δρ/ρ*. Do not sell “chaos” as a single noun for both.

BKL (Belinski–Khalatnikov–Lifshitz): generic spacelike singularities in classical GR show Mixmaster behavior — chaotic Bianchi IX oscillations, a sequence of Kasner epochs with exponents that bounce in a deterministic but exponentially sensitive map. Nearby spatial points lose correlation as *t → 0* (or toward a crunch). That is a theorem-level expectation of the classical theory, not a photograph of the bang.

A steered crunch — the Omega Point demand that intelligence control the geometry all the way to a single *c*-boundary point — requires control of that chaos. Barrow-type results make the demand measure-zero unless extra structure is imposed: you would need to fine-tune the approach on successively smaller scales without a horizon-free handle (A23, A42). Lyapunov exponents of the Mixmaster map are positive; each Kasner epoch shrinks the set of successful steerings. Sensitivity is an engine for structure in the expanding era. It is a veto on a required final mind in a recollapse.

---

## A17. What “Non-Baryonic” Means

Baryons: protons and neutrons (plus electrons when the popular chapters say “ordinary matter”). CMB acoustic peaks plus BBN fix *Ω_b ≈ 0.05* (*ω_b = Ω_b h² ≈ 0.0224*). Dynamical masses (clusters; large-scale flows), weak lensing, and the CMB peak *positions* give *Ω_m ≈ 0.3*. The difference *Ω_c ≈ 0.26–0.27* does not couple electromagnetically at the level that would have shown up as extra light, extra damping, or extra BBN catalysts. Collisionless cold dark matter (CDM) is the working fluid: it clumps, it does not shine, it does not collide with itself or with baryons at rates that would erase A17’s offsets. WIMP, axion, sterile neutrino, primordial black hole (in a narrow mass window) are candidate nouns, not detections.

Rotation curves: *v² ≈ G M(<r)/r* in a disk. Flat *v(r)* at tens to hundreds of km/s implies *M ∝ r* well outside the starlight. That is the original “missing mass” in spirals (Rubin; Bosma). It is not, by itself, a proof of a new particle — MOND still has friends here — but it is the everyday face of the extra pull.

Weak and strong lensing map surface density *Σ*. The Bullet Cluster, 1E 0657−56 at *z ≈ 0.3* (Clowe, Markevitch, et al., 2006), is a merger in which the X-ray gas (Chandra) lagged the collisionless mass reconstructed from weak lensing. The offset is the point: collisional baryons were stripped; the majority of the gravitating mass was not. Modified-gravity stories that tie the extra pull strictly to the visible gas have to work around that photograph. They have not done so in a way this book treats as competitive.

CMB acoustic peaks: the odd/even peak-height ratio is sensitive to *Ω_b*; the spacing and the third-peak height help fix *Ω_m h²* and the late-time inventory. That is why the leftover glow, not only the Bullet, is a dark-matter courtroom.

Direct detection: LZ, XENON1T/nT, PandaX, and predecessors have not found a WIMP. Spin-independent cross-section limits sit near *10⁻⁴⁷–10⁻⁴⁸ cm²* at *~30–40 GeV/c²*, with neutrino fog approaching. Axion haloscopes (ADMX and cousins) have closed slices of *g_{aγγ}–m_a* space, not the whole QCD-axion band. Nulls are data. They are not a proof CDM is a mistake. They are a proof the first popular noun was not sitting on the first shelf.

---

## A18. Vacuum Energy and the Cosmological Constant

**(6)**  *ρ_Λ = Λ c² / (8π G)*  (constant)

Naive QFT zero-point *~ M⁴* with *M* at the Planck scale (*~10¹⁹ GeV*) overshoots *ρ_Λ,obs* by ~120 orders of magnitude; even a TeV cutoff overshoots by ~60. Observed *ρ_Λ ~ (2.3 × 10⁻³ eV)⁴*, or about *6 × 10⁻²⁷ kg m⁻³* — the same order as *ρ_c* today, which is the coincidence problem. Weinberg 1987: if *ρ_Λ* is too large and positive, galaxies do not form before the shove wins; that anthropic upper bound sits within one or two decades of the measured value. A bound is not a derivation. It becomes an explanation only if an ensemble of vacua exists and a measure can be defined (A15, A41). String landscapes offered as that ensemble inherit (18).

---

*Supernovae, BAO, and H(z)*

**(7)**  *H²(z)/H₀² = Ω_m (1+z)³ + Ω_r (1+z)⁴ + Ω_Λ + Ω_k (1+z)²*

(for *w = −1*). Type Ia supernovae as standardizable candles (Riess et al. 1998; Perlmutter et al. 1999; Schmidt’s team sharing the 2011 Nobel) showed that luminosity distance at *z ~ 0.5–1* is too large for a matter-only decelerating universe. The leftover glow and a baryon acoustic oscillation standard ruler together prefer the same fit. BAO: the sound horizon at the drag epoch is *r_d ≈ 147 Mpc* comoving in Planck-like physics; galaxy and Lyman-*α* surveys (SDSS, BOSS, eBOSS, DESI) recover a feature at *~150 Mpc* comoving. That is a meter stick, not a metaphor.

Equation (7) with *Ω_m ≈ 0.3*, *Ω_Λ ≈ 0.7*, *Ω_k ≈ 0* is the working *H(z)*. Acceleration (*q₀ < 0*) begins near *z ~ 0.6* in that fit — a few billion years ago, not at the bang. DESI’s latest BAO, combined with supernovae, has opened a conversation about *w(z) ≠ −1* at the edge of the errors. That is a possible warming of “not exactly Λ.” It is not a detection of a Big Rip, a bounce, or a required recollapse (A19, A43). *w ≈ −1* remains the number this book writes unless a named survey forces the digit.

Hot: acceleration; *Ω_Λ ~ 0.7*; BAO ruler. Warm: Λ as a true constant rather than a slow field. Cold: we know *why* the zero-point is small.

---

## A19. Why Recollapse Is Not in the Data

Closed matter-only recollapse needs *Ω_m > 1* and no lasting shove. Observed *Ω_m ≈ 0.3*, *Ω_Λ ≈ 0.7*, *q₀ < 0*. The working Friedmann equation (7) expands forever. The expansion *accelerates*. A recollapse remains possible in a different vacuum or a *w(z)* that turns around later — a cold option, not the fit.

FAP and the Omega Point, as a *requirement* of the laws plus data, fail here first: they need a crunch. They fail again on horizons (A23, A26): a de Sitter-like late phase has an event horizon and a finite entropy budget, not an infinite computational resource in a vanishing 3-volume. They fail a third time on BKL chaos (A16) if you grant a crunch anyway. This book keeps that failure. A poetic crunch is not a measurement.

What would reopen recollapse: a measured *w(z)* that climbs through *−1/3* and stays there with *Ω_m* high enough, or a vacuum decay (A43) into a negative-*Λ* phase on a timescale shorter than the remaining expansion. Neither is in the data. The first is a research program. The second is a lifetime *Γ* that is not measured (and, in the Standard Model metastability calculation, is usually quoted as vastly longer than *t₀*, with large theoretical fog). A closed universe with *Ω_k* slightly negative and *Ω_Λ ≈ 0.7* still expands forever in the working fit; curvature does not buy you a crunch once the shove is on.

---

## A20. The Schwarzschild Radius

**(14)**  *r_s = 2 G M / c²*

The horizon is the null surface *r = r_s* in Schwarzschild coordinates. That coordinate is bad at the surface: *g_{tt} → 0*, *g_{rr} → ∞*. Curvature invariants (*Kretschmann scalar ~ M²/r⁶*) are finite at *r_s* and blow up at *r = 0*. The horizon is a fact about events — which worldlines can still reach future null infinity — not a painted brick wall.

Numbers. Sun: *r_s ≈ 2.95 km*. Earth: *≈ 8.9 mm*. A 10 *M_⊙* stellar hole: *≈ 30 km*. Sagittarius A*: *M ≈ 4.3 × 10⁶ M_⊙* (stellar orbits; GRAVITY; S0-2 periapsis), *r_s ≈ 1.3 × 10¹⁰ m ≈ 0.08 AU*. M87*: *M ≈ 6.5 × 10⁹ M_⊙*, *r_s ≈ 1.9 × 10¹³ m ≈ 130 AU*. The Event Horizon Telescope’s 2019 M87* ring and 2022 Sgr A* ring are images of photon-orbit scale (*~2.5–5.5 r_s* depending on spin and inclination), not snapshots of *r = 0*. The 1.3 mm M87* ring diameter is *~42 μas*, matching a 6.5-billion-solar-mass hole at 16.8 Mpc. LIGO/Virgo/KAGRA hear mergers: GW150914 was *36 + 29 → 62 M_⊙* with *~3 M_⊙ c²* in gravitational waves, peak strain *~10⁻²¹*, ringdown frequencies matching Kerr quasi-normals at the masses implied by the inspiral. Thousands of solar-mass events later, the catalog is a population, not a one-off. Hot: horizons of this kind exist. Warm: the interior continues as classical GR until a singularity. Cold: we know what replaces *r = 0*.

---

## A21. Gravitational Time Dilation and Kerr Orbits

**(15)**  *dτ = dt √(1 − r_s/r)*  (static observer, Schwarzschild)

A clock at rest at radius *r* runs slow versus a clock at infinity by that factor. On Earth’s geoid versus a GPS orbit the gravitational piece is *~+46 μs/day* for the higher clock (A5). At the surface of a neutron star (*r ~ 3–5 r_s*) the factor is tens of percent. At a static station hovering near *r_s* the factor goes to 0 — and the station needs a rocket that goes to infinity. Hovering is not free.

Kerr: spin parameter *a/M* between 0 and 1 in geometric units. The innermost stable circular orbit (ISCO) sits at *6 GM/c²* for Schwarzschild and moves in to *GM/c²* for prograde extremal spin. That is why thin-disk efficiency can reach *~40%* of rest mass for high spin versus *~6%* for a non-spinning hole. Extreme “hour versus years” ratios for a *person* beside a supermassive hole need a station near ISCO *and* *a/M* within *~10⁻¹⁴* of extremal so that the redshift factor is huge while the orbit remains stable. Allowed by the metric. Not generic. Astrophysical spins measured from iron lines and continuum fitting are high (*a/M ~ 0.7–0.98* for some AGN) and nowhere near that engineering tolerance.

Frame dragging (Lense–Thirring) is measured around Earth (Gravity Probe B; LAGEOS) at the milliarcsecond-per-year level. Around a hole it is the reason the ergosphere exists (*r < 2GM/c²* at the equator for Kerr). Penrose processes and Blandford–Znajek jets can tap spin. They are not time machines (A35).

---

## A22. White Holes and the Kruskal Diagram

Maximal analytic extension of Schwarzschild (Kruskal–Szekeres coordinates): two exterior regions, a black-hole region (*r < r_s*, future), a white-hole region (*r < r_s*, past), and an Einstein–Rosen throat connecting the exteriors. A white hole is a past horizon: matter can exit, not enter. The time-reverse of collapse is not the same as a film of a hole run backward in an astrophysical sky. Forming a white hole from regular initial data in our exterior is not what stars do. The white-hole region in the eternal diagram is as eternal and as unphysical as the second exterior: a boundary condition, not a collapse.

Unstable: any infalling perturbation (and the quantum flux) destroys the idealized extension. No astrophysical candidate has been named that survived a measurement. Fast radio bursts, gamma-ray bursts, and odd transients have all been offered and re-offered; none is a white hole in the data.

A white hole is not the FLRW bang. The bang is a hot, dense spatial slice in the past of *every* comoving worldline. A white hole is a local causal structure with an exterior. Confusing them is a diagram accident (both have a past singularity in some drawings). It is not a theory of the leftover glow. Planck’s blackbody plus *z_* ≈ 1090 last scattering (A9) is the bang’s photograph. No analogous spectrum has been offered for an astrophysical white hole.

---

## A23. The Bekenstein–Hawking Bound

**(16)**  *S = k A / (4 ℓ_P²)*  *ℓ_P = √(ħ G / c³)*

Entropy scales with area, not with the 3-volume inside. For a solar-mass hole, *A = 4π r_s²* gives *S/k ~ 10⁷⁷*, enormous compared with a star of the same mass. This is the seed of holography: the number of states a region can hold is bounded by the area of a surrounding lightsheet (Bousso’s covariant version of Bekenstein). AdS/CFT makes a precise dual in negatively curved space with a conformal boundary. **That dual is not a tested description of our cosmology.** We do not live in AdS. String theory’s most precise holography inherits (18) when offered as a fact about the leftover glow.

Tipler-style infinite information in a vanishing 3-volume fights this counting. Unless horizons are removed by hand and the area theorem is evaded, a crunch does not give you infinite bits. The late universe we have, with *Λ > 0*, gives you a cosmological horizon of radius *~16 Gly* (A26) and a finite Gibbons–Hawking entropy *~ 10¹²² k*. That is a budget, not an infinity.

---

*Hawking Temperature and Evaporation Time*

*T_H = ħ c³ / (8π G M k)*. Solar-mass hole: *T_H ≈ 6 × 10⁻⁸ K*, far below *T_CMB = 2.725 K*, so a stellar hole in today’s sky accretes more from the leftover glow (and from the interstellar medium) than it evaporates. A hole lighter than *~10¹¹ kg* would be hotter than the CMB and could be losing mass now; none is observed. Evaporation time *t_ev ~ 5120 π G² M³ / (ħ c⁴) ~ 10⁶⁷ (M/M_⊙)³ yr*. For *M = 10¹² kg* (a sometimes-quoted primordial window), *t_ev* can sit near the age of the universe; Fermi and cousins have not confirmed a Hawking photosphere. Information paradox: a thermal Hawking spectrum versus unitary evaporation. Unfinished. Not a door (A24).

---

## A24. Geodesics, Singularities, and Why You Do Not Come Out

In classical GR, timelike geodesics that cross *r_s* reach *r = 0* in finite proper time. For Schwarzschild, *τ ~ π GM/c³* from horizon to crunch — about 10 μs for a 10 *M_⊙* hole, about 20 s for Sgr A*, about 9 h for M87*. They cannot return to the exterior. The horizon is not a hallway. Outgoing light at *r = r_s* stays at *r = r_s*; inside, the *r* coordinate is timelike and decreasing *r* is as compulsory as tomorrow. The photon sphere (*r = 1.5 r_s* for Schwarzschild; the EHT ring sits near that projected scale) is still *outside*. Orbiting there is not visiting the interior.

The singularity theorems (Penrose 1965; Hawking–Penrose) give geodesic incompleteness under energy conditions plus a trapped surface, not a map of what the incomplete edge “is.” Tidal forces at the horizon of a supermassive hole can be small (the curvature scale is *GM/c²*); at *r → 0* they are not. No-hair: a classical hole is characterized by *M*, *J*, and *Q*. That is a statement about the exterior, not a door code.

Inflation and *Λ* violate the strong energy condition. That is why a burst and a late shove can exist without recollapse. They do not violate the null energy condition in the working stress-energy, and they do not turn a trapped surface into a transit system. Quantum replacements (bounces, fuzzballs, firewalls, baby universes) are research programs. String replacements, when offered, **cannot currently be tested**. A baby universe you cannot call is not a destination. You do not come out.

---

## A25. Mars Numbers: Δv, Delay, Life Support

These are *permit* numbers. They are not a colony plan, a city budget, or a sequel.

Earth–Mars light time: *~4 min* at closest approach, *~21–24 min* near solar conjunction; one-way. You do not converse. You send, and wait. Hohmann-like transfers: *~6–9 months* (a standard 145-day-class fast transfer costs more Δv; a 259-day textbook Hohmann is the cheap ellipse). Synodic window: *~26 months*. Miss it and you wait two years.

Δv: LEO to trans-Mars injection *~3.6 km/s*; Mars capture and circularization *~2 km/s* class for a propulsive orbit, plus a lander budget of several more km/s if you do not aerobrake. Aerobraking and aerocapture trade heat shield for propellant. Surface gravity *0.38 g*. Solar constant *~43%* of Earth’s. Atmosphere *~6 mbar* (6.1 mbar mean), *~95% CO₂*, argon and nitrogen in the remainder — a vacuum by kitchen standards, a resource by ISRU standards. Mean surface *T* near *−60 °C*; equatorial summer afternoons can sit near 0 °C. Water ice is mapped at mid and high latitudes (Phoenix; SHARAD; neutron spectroscopy); equatorial “dry” is not globally dry at depth.

Perchlorates: Phoenix wet chemistry found *~0.5–1%* by mass in the soil, mostly as Mg/Na perchlorate. That is a toxic oxidizer and a hygroscopic brine ingredient, not a mood and not automatically a nutrient. Plant growth needs imported or generated O₂/N₂ buffers, water that has been scrubbed, and radiation shielding. GCR plus solar protons at the surface are lower than in cruise (A31) because of the planet’s bulk, higher than under Earth’s atmosphere and magnetosphere. A greenhouse on a dead world is an engineering permit. It is not a biosphere, not a city, and not a reason to treat Earth as optional.

---

## A26. Particle Horizon vs Cosmic Event Horizon

Particle horizon: comoving integral *χ_p = ∫_0^{t₀} c dt / a*. It is how far a photon has been able to travel since *a = 0* (or since the end of a burst, if you cut the integral there). In working ΛCDM, the proper radius of the particle horizon *today* is *~46 billion light-years* — larger than *c t₀ ≈ 13.8 Gly* because the universe expanded while the light was in flight. That is the radius of the observable universe.

Event horizon (ΛCDM with *Λ > 0*): *χ_e = ∫_{t₀}^{∞} c dt / a*, finite when *a ~ exp(H_Λ t)* at late times, *H_Λ = c √(Λ/3)*. Galaxies with comoving distance *χ > χ_e* will never receive a signal we send *today*. The current proper radius of that event horizon is *~16 billion light-years*. The Hubble radius *c/H₀* is *~14 Gly* for *H₀ ≈ 70*. Three different lengths; three different questions. Do not swap them.

The leftover glow comes from *χ* just inside the particle horizon (last scattering is not *a = 0*). Most galaxies we photograph already lie outside today’s event horizon in the sense that *our* “hello,” sent now, will never arrive — even though *their* ancient light is still arriving here. That is Chapter 26’s leaving. It is not a door closing on the past cone. It is a door closing on the future cone of *this* event.

---

## A27. Finding Worlds You Cannot See

Transit depth *δ ≈ (R_p / R_★)²*. An Earth–Sun transit is *(R_⊕ / R_⊙)² ≈ 84 ppm*; a Jupiter–Sun transit is *~1.1%*. Kepler, TESS, and ground surveys have turned that percent and that 84 ppm into a census. Radial-velocity semi-amplitude *K ∝ M_p sin i / (M_★^{2/3} P^{1/3} √(1−e²))*. An Earth at 1 AU on a Sun analog is *K ≈ 9 cm/s* — at the edge of the best spectrographs. A hot Jupiter is *K ~ 50–200 m/s*, which is why the first detections were massive and close.

Occurrence: most FGK stars host planets; Kepler’s conservative yield is more than one planet per star on average. Mini-Neptunes (*R ~ 2–3 R_⊕*) are common; a radius valley near *1.8 R_⊕* separates stripped cores from those that kept envelopes. Earth-size planets in conservative habitable zones of GK dwarfs sit at occurrence *~0.1–0.2* depending on the paper — a rate, not a biosphere count. Direct imaging (GPI, SPHERE, JWST) and microlensing (OGLE; Roman in the future) are rare, complementary, and biased to wide, young, or unaligned systems. Timing of transits and TTVs give densities when you have both *R* and *M*; a 5 *M_⊕*, 1.6 *R_⊕* world is not Earth.

Atmospheric transmission spectroscopy measures molecular bands during transit. H₂O, CO₂, CH₄, CO appear in giant and sub-Neptune atmospheres; O₂, O₃, CH₄ as a *set* are candidate biosignatures, not proofs. Photolysis makes O₂; geology and haze fake CH₄; abiotic CH₄–CO₂ pairs exist. JWST has smelled CO₂ on a transiting sub-Neptune and water on giants. That is chemistry. It is not a second origin. Look first, then name the gas.

---

## A28. Circumstellar Habitable Zones

Kopparapu et al. (approximate, Sun): conservative moist-greenhouse to maximum-greenhouse limits *~0.99–1.7 AU*; recent-Venus to early-Mars optimistic limits wider (*~0.75–1.8 AU*). Insolation *S ∝ L / d²*; *L* depends on spectral type and age. A G star at 4.5 Gyr is the hired case. An M dwarf’s HZ sits at *≲ 0.2 AU* (TRAPPIST-1’s temperate planets are *~0.03–0.06 AU*). Tidal lock is likely; flare and XUV stripping of atmospheres are the invoice; M-dwarf habitability is a research program, not a yes.

HZ is a *permit for surface liquid water*, given an Earth-like atmosphere and a carbonate–silicate thermostat you should not take for granted. It is not a biosphere detector. The inner edge is a moist-greenhouse runaway: stratospheric water, UV photolysis, hydrogen escape. The outer edge is the maximum greenhouse: CO₂ condenses and the warming saturates. Both edges move if you change surface gravity, N₂ inventory, or rotation. Venus is in a generous optimistic zone and is a 90-bar CO₂ oven at *~735 K*. Mars is near the outer edge and is a 6 mbar desert (A25). Moons of giants can sit outside a stellar HZ and still host liquid water on tidal heat (A29). A K dwarf’s HZ is closer in than the Sun’s and quieter than an M dwarf’s; that is why some occurrence papers prefer it. Do not use the cartoon ring as a census of life.

---

## A29. Tidal Heat, Ice Shells, and Dark Seas

Tidal power scales roughly *Ė ∝ (G M_p)² R⁵ e² / (a⁶ μ Q)* (order-of-magnitude; *e* eccentricity, *μ* rigidity, *Q* dissipation). Io–Europa–Ganymede 1:2:4 Laplace resonance maintains *e*. Io’s *Ė* is measured as heat (*~10¹⁴ W*); Europa’s is inferred. Europa: ice shell perhaps 10–30 km (thicker in some gravity/induction models), ocean *O(100) km*. Induced magnetic field (Galileo) already implies a global conductor; Hubble and JWST have argued for plumes and then argued with themselves — plumes remain warm as a claim, not a scheduled geyser. Surface in Jovian belts: *O(10²–10³) rem/day* (*~1–10 Sv/day*) — lethal; the ocean is shielded by ice and water column.

Enceladus: south-polar plume (Cassini), salinity, silica nanoparticles (hydrothermal hint), H₂, organics. The plume is a sample without a landing. Ganymede: intrinsic field; possible stacked oceans separated by high-pressure ices. Titan: surface lakes are methane (A30); a deep water–ammonia ocean is a gravity/shape inference, not a beach. High-pressure ices (VI, VII) on larger worlds may limit water–rock exchange — open problem. Rogue planets: radiogenic plus primordial heat under a thick ice blanket can maintain a sea (Stevenson-type thermos). Look-first rule: induced field and plumes before slogans. Oceans are warm-to-hot. Life in them is not a detection.

---

## A30. Second Origins, Other Chemistries, Missing Body Plans

Sample size *N = 1*. Operational life: Darwinian replication plus a metabolism on a gradient. Viking LR (1976): labeled-release gas at *~15 °C* that did not repeat after a *160 °C* heat control, contested then and now as abiotic soil chemistry (peroxides; perchlorates, later measured) versus a metabolism. Biosignature *pair* O₂+CH₄ is a disequilibrium test, not a verdict.

Universal genetic code on Earth is a LUCA signature (frozen accident ± modest error-minimization), not a cosmic typesetter. Same codon table on a second world: contamination or panspermia, not independent invention. Pairing polymers warm; exact DNA alphabet cold. LUCA, as a node, sits before *~3.5–3.8 Ga* on the terrestrial clock; that is a date for *this* tree, not a cosmic requirement.

Alternative solvents are papers, not zoos. A solvent must dissolve reactants, permit transport, allow a compartment, spare the polymers, and host a gradient. Water is the hired case, not a cosmic sacrament.

Titan (Cassini; Huygens, 2005): surface *T ≈ 94 K*, *P ≈ 1.45 bar*, N₂ air with CH₄ weather; lakes/seas of CH₄/C₂H₆ (radar-dark, north-polar concentration). No biosphere detection. Liquid-methane relative permittivity *ε_r ≈ 1.7* vs water *ε_r ≈ 80* at kitchen *T* — ions poorly solvated; Earth-like acid–base metabolism is mute. Kinetics: Arrhenius suppression at 94 K makes uncatalyzed lake chemistry a statue; upper-atmosphere photochemistry (CH₄ → haze) can still run. Warm papers, not detections: azotosomes (acrylonitrile vesicles in liquid CH₄; acrylonitrile seen in Titan’s air; stability contested); H₂ + C₂H₂ metabolism (McKay–Smith-type fingerprint: depleted H₂ / acetylene). Dragonfly-class in situ is the next measurement, not a verdict in this note.

Ammonia: 1 atm liquid range *≈ 195–240 K* (narrower than water unless mixed or pressurized). Polar, H-bonding; NH₃–H₂O eutectics stay liquid colder. Different acid–base inventory; hostile to Earth proteins. Still a paper.

Concentrated H₂SO₄ cloud decks (Venus-class): liquid in a probe-accessible *T* band; dehydrating to Earth organics. Tougher aromatics get papers. Phosphine claims were a courtroom, not a census. Colder paper than Titan: we have tasted the lakes; we have argued the mist.

Silicon chains as *flesh*: weak in water (prefer silica / mountains). Silica *scaffolds* already exist (diatoms, radiolarians) as coating, not metabolism. Homochirality: a second origin may be mirror-life; terrestrial enzymes would fail on it. “Nitrogen-breathing” as a *primary* metabolism is not an Earth pathway; N₂ fixation is costly (nitrogenase). Rapid *morphological* ascent through Earth’s taxa in days is fiction. Rapid *radiation* given short generation time and empty ecospace is ordinary (microbes; post-extinction recoveries). Contingency: Burgess-type body plans show many fired experiments; convergence (eyes, wings, torpedo bodies, cursorial hunters) shows some re-hiring.

Independent *humanoid* sophonts: cold (ape bauplan is historical). Independent *cetacean* sophonts as a default: cold; aquatic nervous systems warm. “Colleague with different ears” is a cultural wish, not a morphology forecast. Planetary-scale hyphal/root nets: Earth has sketches (mycelia; plant-mycorrhizal signalling — do not oversell a global brain). Remote-worn local bodies are engineering (Ch. 31), not a second origin.

Brain *volume* is a weak predictor once you leave a clade. Cetacean brains are large; corvid and parrot pallia are small, dense, and capable (Herculano-Houzel-type neuron counts beat cubic centimeters). Packing, wiring length, the body the wires serve, cumulative culture, and clock time matter more. A ~30 cm soma is neither a law nor a ban. Warm: a small, fast, dense nervous system can outrun a human-scale skull. Whale-scale tissue without that invoice can fail to. Eusocial colonies are distributed-control sketches, not a proof of a planetary hive-person. Miniaturized humanoids remain cold as morphology.

Parasitoid / host-as-nursery specialists: warm (ichneumonids; *Ophiocordyceps*); “evil” is the host’s word. Large terrestrial bipedal predators: warm convergence (theropod solution). Saurian *intelligence*: warm (avian dinosaurs already; troodontid EQ). Saurian *civilization*: extra filters (surplus, cumulative culture, manipulation, often fire) — not forbidden, not an ape downtown. Russell-style “dinosauroid” humanoid: cold as morphology. Alien cities as non-rectilinear lasting rearrangements (rookery, reef, mound, hyphal net, breathing burrow): the search problem is recognition, not physics. Cave/vent/endolith towns: hot as Earth fact (Movile; black smokers; Naica fluid inclusions). Walking photosynthetic macrofauna: warm permission, no Earth hire.

Endo- vs exoskeleton: both hired (vertebrate bone/cartilage; arthropod/mollusc cuticle). Molting vs fracture-healing are the invoices. Fur/pelage as a boundary layer can dump or block heat (camel coats); “no fur on a hot world” is too crude. Husbandry predates humans: ant–aphid trophobiosis; leafcutter fungal agriculture. Technosignature category error: night lights / vehicle herds misread as the organism, organisms as parasites of the machines — a scale mistake symmetric to missing the ant nest.

Missing on Earth as *macro* habits: wheels with axial blood supply; silicon endoskeletons as *default vertebrate* habit; photosynthetic herds; terrestrial coleoid dominance; radial large terrestrial predators; several simultaneous intelligent bauplans from one radiation.

Cannibalism: common in metazoa (not a zoological ban). Human near-taboo is a filter, not a field equation. Leading meshes: species-specific pathogens/prions (kuru; BSE from intra-species feed); kin selection; retaliation in social species. Inter-trunk predation (them eating us) is not cannibalism; chirality/code mismatch still makes us a poor default lunch.

Sex is not immortality: soma dies; lineage continues (Weismann). Asexual fission/clones are the common terrestrial default by time and census; sex is costly (two-fold cost of males) and still common in large parasite-exposed taxa. Warm accounts: Red Queen, Muller’s ratchet, recombinational repair — not a unique cosmic requirement. HGT is mixing without meiosis. Individual biological immortality is rare and still mutates. Expect *some* genome mixing where parasites + time exist; do not expect two sexes and a child-as-afterlife.

Reward, not pamphlet: sexual pleasure as a selected carrot for an expensive shuffle (wanting/seeking vs liking/completion; pair-bond peptides as a warm extra where young are costly). Asexuality and drive variation are lottery outcomes, not cosmic defects. Pornography as supernormal stimulus (Tinbergen): cue louder than the costly act; watchfulness plus cheap infinite images is Pleistocene wiring against an industrial supply (same family as refined sugar, intermittent-reward machines). Not a universal sophont law; warm that any reward loop can be spoofed once recording is cheap. No off-switch labeled “depiction only.”

Population structure (ecotypes, subspecies, island morphs): hot as a pattern after isolation + selection. Human folk “races” as discrete biological kinds: a poor map of a recently expanded, highly admixed species (most variation within groups; clines). Exobiology should expect local editions, not Earth’s census boxes. Native/non-native is a timestamp, not an essence; introductions can be polite or invasive. Directed seed into an occupied biosphere = invasion (look first). Humans are range-expanders on Earth and would be the non-native on any other world.

---

## A31. Travel Time, Dose, and Autonomous Systems

The numbers moved with the chapter. Cruise time at *0.01 c* and *0.1 c*, deep-space dose of order a few tenths of a sievert per year, and the distinction between a present pattern engine and a century-stable control loop are in *A Trip Is Not a New Life*, Appendix A25.

This book keeps the use the later chapters make of the fact: long travel is a project with a failure rate, not an Omega Point, and flesh is a bad hire for a four-century commute.

---

## A32. Genome Information, Synthesis, and Planetary Protection

The numbers moved with the chapter. Genome size, COSPAR-class protection, and why a printed organism is logistics plus a library are in *A Trip Is Not a New Life*, Appendix A26.

This book keeps the rule: look first, seed later. A library poured into a sea that already copies is a conquistador. The same library, on a world whose exam has already been graded empty, is a greenhouse.

---

## A33. Einstein–Rosen vs Traversable Throats

ER bridge: Kruskal throat, non-traversable, pinches in finite proper time (A22). Morris–Thorne (1988): static, spherically symmetric, flaring-out condition at the throat requires *ρ + p_r < 0* in the appropriate frame (exotic). Mouths appear as spheres, not holes in a floor. A traversable throat is a metric you write down, not a tunnel you have dug.

---

*Energy Conditions and Quantum Inequalities*

**(17)**  NEC: *T_μν k^μ k^ν ≥ 0* for all null *k*. Traversable throats need NEC violation near the throat. Ford–Roman inequalities bound the magnitude × duration of negative energy in a given volume. Macroscopic, long-lived throats are likely forbidden; not a theorem covering every QFT-on-curved-space loophole.

Alcubierre (1994): a shift vector that contracts the loaf ahead and expands it behind; the cabin can have small tidal forces; the ship’s *local* four-velocity stays timelike and subluminal. Effective superluminal *arrival* vs a long-way light signal is a global, not a local, fact. The bubble wall requires *T_μν* that violates the WEC/NEC (exotic). Energy estimates have been reduced by wall-shaping (van den Broeck; Natário; later “warp shells”); they remain enormous and still exotic. The forward wall is typically outside the cabin’s causal past — you do not control or ignite the geometry from inside without pre-arranging the path (or a receiver). Krasnikov tube: modify *g_μν* along an outbound worldline so the return is short; still exotic, still paving. Superluminal effective travel in GR can be arranged to yield CTCs; chronology protection (A35) is the same unpaid insurance as for wormhole mouths. No laboratory metric-engineering. “Warp” laboratory claims to date are not an Alcubierre drive.

---

## A34. What Would Count as Evidence of Intervention

A message in a channel nature does not use (narrowband, prime-modulated, a sightline that is not geochemistry). A correlation in the CMB that is not a Gaussian twitch plus foregrounds. “It looks pretty” is not a test. Absence of such signatures is not a proof of absence; it is why the craftsman stays cold.

Old Kingdom Egypt: cardinal alignment of Khufu’s pyramid to true north at the few-arcminute level; Sirius/Sopdet heliacal rising tied to the civil/flood year; decanal star clocks; surveyed cubit architecture (seked slopes). Worker villages, quarry logistics, Wadi el-Jarf papyri: terrestrial workforce, not a missing physics. Orion-correlation / “encoded π as a telegram” claims are selection plus later reading; not a testable intervention channel. Precession as a *named* phenomenon is Greek (Hipparchus); Egyptian sky-work does not imply a forgotten FLRW cosmology. The obvious residual is competence. The visitor is the sermon.

UAP residuals (public): 2004 Nimitz / Princeton — the stubborn file: Aegis radar tracks + two-pilot visual + ATFLIR on a wingless, plume-less object; 2014–15 Roosevelt “Gimbal” / “GoFast” (single-sensor IR; prosaic accounts exist and may be right); 2017 reporting; 2020 DoD authentication of the tapes; 2021 ODNI (most cases data-poor; a minority unusual); NASA UAP study (2023) and AARO historical record (2024): no *confirmed* extraterrestrial technology, some later-identified U.S. programs, no verified exotic wreckage in the public record. That is not the same sentence as “nothing was there.”

Single-sensor IR without range cannot fix size or speed; camera rotation and parallax mimic miracles. Multi-platform leftovers still require a prior: classified terrestrial (own or adversary) is the least-new-physics fit and is already an admission of remarkable hardware if true. “I don’t know” is the correct residual for the best public cases. What would *name* the residual: range-complete multi-sensor kinematics that exceed on-board energy; physical samples with non-terrestrial isotopic/microstructural signatures; a communicative channel that can be missed.

Visitor hypotheses vs this book’s physics: future-us requires CTCs or a sideways foliation (A35–A36; chronology protection warm-to-cold). Everett branches do not admit hops or signals (A40). Interstellar arrival is a Chapter 31 project, not a dogfight. Traversable “beam-in” still owes the exotic-matter bill (A33) or a local assembler (A32). Telepathy: no established extra information channel; still bounded by carriers we already have.

Congressional UAP sequence (public): 2017 reporting on AATIP; 2020 DoD video authentication; FY2021 intelligence authorization → 2021 ODNI preliminary assessment; 2022–24 hearings; Schumer–Rounds UAP disclosure language (thinned). Institutional motives that do not require an extraterrestrial conclusion: air-domain awareness (UAS, adversary systems), SAP/oversight ambiguity, stigma as an operational defect, reports near strategic sites. Witness claims of non-terrestrial retrieval remain claims until the hardware tests above are met.

---

*Light-Travel Contact and Information Bounds*

Round-trip time *2d/c*: 8.7 yr for α Cen, *~4,000 yr* for a star on the far side of the Galaxy’s disk, *~5 Myr* for M31. Drake’s equation *N = R_* × f_p × n_e × f_l × f_i × f_c × L* is a parameterization of ignorance, not a measurement; several factors are still *N = 1* or an occurrence rate from A27, not a communication census. Information capacity of a noisy channel is Shannon’s *C = B log₂(1 + S/N)*. A 1 Hz carrier with a miserable signal-to-noise still needs photons, a dish, and a time slot; a biosphere under ice (A29) may have no EM leakage at all. SETI is a search in a thin slice of the habitable map — radio and some optical, a fraction of the sky, a fraction of the duty cycle. That thinness is why a null is not a proof of emptiness. It is also why a headline “we heard them” owes a channel nature does not already use.

---

## A35. Worldlines and Self-Consistency

Novikov principle: the probability of events on a closed timelike curve (CTC) is consistent; paradoxical histories have measure zero. This is a consistency condition on the block, not a dynamics that “prevents” edits. There are no edits. If a CTC exists, the solution of the field equations plus matter is already a loop. You do not climb into it and change Tuesday. You discover that Tuesday was always the loop.

---

*Metrics That Admit CTCs*

Gödel (1949): a rotating dust universe with *Λ < 0* (or an equivalent tension) and vorticity *ω* tied to the density so that *4πGρ = ω²* in the original normalization. Every event lies on CTCs. Angular velocity of the matter is not a small Lense–Thirring twist; it is the geometry. Our universe is not Gödel’s. Planck-scale vorticity limits and the leftover glow’s isotropy (*10⁻⁵*) do not permit a Gödel rotation at cosmological scale. The metric is an existence proof in GR, not a map.

Kerr: CTCs appear inside the inner (Cauchy) horizon in the analytic extension, in the *r < 0* region through the ring. The inner horizon is unstable (Poisson–Israel mass inflation): infalling radiation blueshifts and the idealized extension does not survive. Traversable wormhole plus time-shifted mouths (Morris–Thorne plus a twin-paradox boost of one mouth): after a finite operation the mouths become a CTC. Alcubierre and Krasnikov shortcuts can be arranged to the same end (A33). None of these are observational geometries. None are a visitor hypothesis that this book will cash (A34).

---

*Chronology Protection and Cauchy Horizons*

Hawking 1992 (*Phys. Rev. D* **46**, 603): as a chronology horizon forms — the first closed null curve, the Cauchy horizon that would become a CTC factory — vacuum stress-energy of quantum fields diverges. The back-reaction is expected to destroy the would-be time machine. That is a conjecture, not a theorem. It has been checked in 2D models and in some 4D examples; loopholes (cut-and-paste, compact extra dimensions, trans-Planckian excuses) get papers. A Cauchy horizon is already a loss of global predictability: the future of the surface is not determined by data on it. Chronology protection, if true, keeps the popular “edit” dead and the “consistent loop” unbuilt. If false, the block can contain loops and still contain no edits. Either way, Tuesday is not a hallway (A36).

---

## A36. Foliations: Why a Stack Is Not a Hallway

A foliation is a stack of 3-surfaces: a time function *t* whose level sets are the leaves. CMC slices, Gaussian-normal slices, cosmic-time slices in FLRW — different jobs, different stacks. A foliation is bookkeeping. It is not a dimension you can walk with a rocket. Proper time is along a worldline, tangent to the 4-velocity, not along the normal from leaf to leaf as if the normal were a corridor.

“Walking the time direction” is a category error unless new structure is added: a fifth direction, a CTC (A35), a traversable handle (A33), or a second copy of the manifold. Each of those additions brings instabilities or exotic stress-energy or both. Gödel’s CTCs are not a walk *across* the leaves of a cosmic time; they are worldlines that are already closed, *inside* the manifold. Hawking 1992’s chronology horizon is what you meet if you try to *build* a closed worldline from a previously causal stack. FLRW cosmic time *t* is a convenient foliation because the slices are homogeneous; it is still not a hallway, and a rocket that “goes back to recombination” is a rocket that aims at our past light cone, not at a previous leaf. The popular picture of pages in a book that you flip at will is a picture of a foliation plus a privilege this book does not grant (A4, A6). You may choose a stack to write *H(z)*. You may not treat the stack as a transit system.

---

## A37. Four Claims That Must Not Be Fused

Tegmark’s levels, as a filing cabinet this book will use and then distrust:

**Level I:** more FLRW volume than our particle horizon — more of the same laws, same *a(t)*, beyond *χ_p* (A26, A38). **Level II:** other post-inflation vacua, other low-energy constants, pocket universes (A15, A39). **Level III:** Everett branches of a universal wavefunction (A40). **Level IV:** other mathematical structures as equally real worlds.

I and II are cosmological hypotheses. They can, in principle, leave fossils (a bubble wall in the leftover glow; a curvature or *Λ* we can bound). They have not. A bubble collision would be a disk-like temperature or polarization feature with a specific profile; Planck searches have not named one that survived foregrounds. III is an interpretation of quantum mechanics. It does not add new constants and it does not let you hop (A40). Calling III “a parallel universe you could visit” is a Level I sentence in the wrong filing cabinet. IV is metaphysics: if every consistent math is a world, no measurement selects. Dark matter and dark energy are not levels. They are ingredients in *this* FLRW inventory (A17–A18). Fusing “the extra pull” with “a branch” or “a landscape vacuum” is a category error that makes every noun unfalsifiable at once. Give the levels separate temperatures, or do not use the cabinet.

---

## A38. Infinite FLRW and Repeated Hubble Volumes

If the spatial slice is infinite and conditions are ergodic — the same statistical ensemble of Hubble-volume states realized over infinite 3-volume — then a finite Hubble-volume configuration recurs. A Hubble volume has a finite number of modes below a cutoff. Holographic finite-state counting (area of the de Sitter horizon; A23) makes “finite” precise: *~exp(10¹²²)* states is still finite. Recurrence of a volume as detailed as “you, reading this sentence” is then a Level I expectation at distances so large they are not a travel plan.

Whether the slice *is* infinite is unproven. *Ω_k* consistent with 0 does not prove infinite extent: a 3-torus can be flat and finite; a closed 3-sphere can have radius far larger than *c/H₀* and look flat. Planck-like *|Ω_k| ≲ 0.01* still allows a 3-sphere with radius tens of Hubble lengths. Topology searches in the leftover glow (matched circles; Cornish–Spergel–Starkman) have not found a small universe; the fundamental domain, if finite, is at least of order the diameter of the last-scattering surface (*~20–30 Gpc* comoving). That is a lower bound, not an infinity. Ergodicity can fail: inflation can leave residual gradients; a landscape (A39) can make distant volumes *not* the same ensemble. Level I is a maybe that follows from infinity plus sameness. Both premises are unproved. Recurrence, if it happens, is not a destination and not a copy you can greet (A26, A31).

---

## A39. Landscapes, Measures, and Untestable Frameworks

String compactifications are often said to yield *~10⁵⁰⁰* vacua (and larger numbers in later counts). **This is not a tested census.** It is a report about the size of a construction in a framework that **cannot currently be tested** (18). A framework that can accommodate any low-energy constants after the fact is not, so far, falsifiable. Extra dimensions and a “landscape” of possible laws inherit that status. They may be mentioned because popular physics mentions them. They are not results.

Eternal inflation’s measure problem (A15) blocks quantitative “prediction” of *Λ* beyond order-of-magnitude anthropic cuts (A41). Even if you grant the landscape as a menu, you do not have a way to take attendance. Volume weighting, pocket weighting, and observer weighting disagree; some produce Boltzmann-brain domination that no one treats as a success. Other frameworks offer other menus, or one valley. The leftover glow has not chosen. Compactification moduli, if they exist, have not been seen as light scalars in the Solar System or as extra damping in the CMB. Until a unique, risky, framework-level prediction exists — a number that would kill the *whole* construction, not one vacuum — this book will not pay rent with a catalog. Equation (18) is the standing rule, not a footnote.

---

## A40. Decoherence and Why Branches Are Not Destinations

Decoherence: entanglement with an environment suppresses interference between pointer states on a calculable timescale; no mind is required. A dust grain at room temperature decoheres its center-of-mass superposition in *~10⁻¹³ s* or faster once photons and air molecules correlate with position. “Observer,” operationally: any degree of freedom that holds an effectively irreversible record (pointer–environment correlation). Conscious observers are a late subset: a *strange loop* / tangled hierarchy (self-referential symbol system; meaning as inter-level isomorphism). Colony-as-mind vs worker-as-neuron is the eusocial sketch. Incompleteness has two morals in this book: (a) as a wedge that minds are not algorithms; (b) as the mechanism by which a formal system talks about itself and an “I” appears. Neither moral is a thermal-history-grade fact. A duplicate loop is a second person, not travel.

Consciousness-causes-collapse (von Neumann–Wigner) is an extra postulate without a distinct kill-shot; this book does not use it. EPR/Bell: spacelike correlations violate local hidden-variable bounds (Aspect et al.; later loophole-closing runs). The no-signaling theorem still forbids using the pairing as a channel. Relativity already denies a frame-independent “at once.” Participatory creation of a pre-biotic chemistry by later minds is not a mechanism; weak anthropic selection explains why chemists inhabit a worked chemistry, not how nucleotides polymerized.

Everett: the global state remains a superposition; each decohered term includes observers who see one outcome. No-signaling: local operations cannot send messages between terms. There is no hop. Branches are not destinations. They are terms in a decomposition you do not climb.

---

## A41. Dimensionless Coincidences and Weinberg’s Λ Bound

Fine-structure *α ≈ 1/137.036*; proton-to-electron mass *m_p/m_e ≈ 1836*; the primordial amplitude *δ_Q ~ 10⁻⁵* (*A_s* in A14); *ρ_Λ / ρ_Planck ~ 10⁻¹²³*. Many “coincidences” are selection-biased: you notice the numbers that look tuned and ignore the ones that do not. Some are genuine sensitivity: if *α* or the light-quark masses move by tens of percent, nuclear binding and chemistry change. How much they *may* move is a model of an ensemble you do not possess.

Weinberg’s galaxy-formation bound (1987) is the cleanest anthropic *number*: *ρ_Λ* cannot sit much more than an order of magnitude or two above the matter density at the epoch when the first galaxies collapse, or linear growth freezes too soon. Observed *ρ_Λ* is within that window. It still needs an ensemble to be an explanation rather than a consistency check. WAP (below) is that check, done honestly. SAP and FAP (A42) are the check, promoted to a purpose.

---

*The Weak Anthropic Principle as Selection*

WAP (Carter; Barrow–Tipler’s wording): observed constants are restricted by the requirement that carbon-based life can evolve and that the universe is old enough that it has. This is a likelihood cut, not a cause. You do not observe from a universe that cooked no chemists. Useful only once priors over an ensemble exist. Without an ensemble, WAP is a reminder not to be surprised that the numbers permit you. With an ensemble, it is how you weight the menu. This book keeps WAP. It does not promote it to a designer.

---

## A42. Why Strong and Final Anthropic Claims Fail

SAP — “the universe *must* permit life” — is either tautological (it did, so it must have been able to), ensemble-selection (WAP with a capital letter), or teleology (a purpose in the laws). The first is empty. The second is WAP again. The third is not a physical model. This book does not hire SAP.

FAP — “intelligence must arise and never die out” — plus the Omega Point (Tipler) requires a recollapse, horizon-free control of the geometry, and infinite computation in finite proper time. Each requirement fails a measurement or a theorem this book already has: *Ω_Λ > 0* and *q₀ < 0* (A18–A19); Bekenstein / de Sitter area counting (A23, A26); BKL chaos on the approach to a crunch (A16). The Omega Point as *required law* stays failed. Anthroposophy is not a physical model. A late mind that computes forever is a wish the shove will not sign.

What remains: WAP as a cut *if* an ensemble exists (warm as a method, not as a proof the ensemble is real). A future that stays habitable in pockets (stars for 10¹² yr; white-dwarf cooling; tidal seas) is allowed and unpromised. Destiny is not a Friedmann equation.

---

## A43. *w*, Vacuum Decay, and Bounce Conditions

*w = p/ρ*. A cosmological constant: *w = −1* exactly, *ρ* fixed, *p = −ρ*. Acceleration of the scale factor requires *w < −1/3* for the dominant component (Raychaudhuri / second Friedmann). Phantom energy: *w < −1* with no decay of the field; *ρ* grows as the universe expands and a Big Rip can form in finite time. Planck-like combinations give *w = −1.03 ± 0.03* or a number statistically compatible with −1; DESI BAO plus supernovae have opened a conversation about *w(z)* drifting above −1 at low *z*. That is a possible warming of “not exactly Λ.” It is not a Rip, and it is not a recollapse.

Metastable vacuum: a field trapped in a false minimum decays by bubble nucleation. Decay rate per four-volume *Γ ~ A exp(−S_E)*, where *S_E* is the Euclidean bounce action. Expected lifetime of a Hubble volume *~ 1/(Γ V)*. The Standard Model Higgs potential, taken at face value with the measured *m_H ≈ 125 GeV* and *m_t ≈ 173 GeV*, appears to sit near a metastability boundary; published lifetimes are typically *≫ t₀* (sometimes quoted as *10^{10^{86}} yr*-class, with huge theory error from Planck-scale operators you do not know). That is not a clock you can set. It is a reminder that *w = −1* today does not prove the vacuum is the final one. A decay into a negative-*Λ* phase would eventually recollapse; a decay into a deeper positive well would shove harder. Neither is a detection.

Bounce: a passage from contraction to expansion requires NEC violation (17) or a new high-curvature theory that invalidates the singularity theorems. Loop-quantum-cosmology bounces and ekpyrotic scenarios get papers. No established CMB signature has been named that this book will call a detection: a specific *B*-mode shape, a specific non-Gaussian template, a specific relic gravitational-wave spectrum, all remain optional. A bounce is allowed by some equations. It is not selected by the leftover glow.

---

## A44. The Problem of Time in Quantum Gravity

Wheeler–DeWitt: *Ĥ Ψ = 0* — the Hamiltonian constraint of canonical GR, imposed as an operator on a wavefunctional of 3-geometries. There is no external *t* in the equation. The Schrödinger equation *iħ ∂_t Ψ = Ĥ Ψ* is what you write when a background time already exists. Here the background *is* the thing being quantized. That is the problem of time: the fundamental equation does not contain the variable the chapters used for *H(z)*.

Recovered time is always extra structure. Semiclassical WKB: when *Ψ* peaks on a family of classical 3-geometries, a phase gradient can play the role of *t* and matter can obey an approximate Schrödinger equation. Relational clocks: a degree of freedom (a scalar field; a dust; the leftover glow’s temperature) is promoted to a clock, and the rest of the universe is “changing with respect to” it. Thermal time (Rovelli): a state plus the Hamiltonian defines a flow; equilibrium is special. Configuration-space geodesics (Barbour): best-matching of 3-geometries, duration as a derived length. None of these is a laboratory selection. All are attempts to get *t* back out of a timeless constraint.

Hartle–Hawking no-boundary: a path integral over compact 4-geometries with no past boundary; time as we use it emerges for large 3-geometries when the wavefunction becomes oscillatory. Vilenko’s tunneling proposal is a cousin with a different contour. Both are cold-to-warm. They do not restore a kitchen-time “before” the bang, and they do not pick an inflaton. Loop quantum gravity and string cosmology offer other recoveries. String recoveries inherit (18). The mismatch between QM and GR is a real gap. It is not a permit for a first tick you can stand in, a hop between branches, or a craftsman.

---

## A45. Inventory of Claims, by Temperature

**Hot:** expansion, including the Hubble–Lemaître linearization at low *z*; CMB blackbody at *T₀ = 2.72548 K* plus *ΔT/T ~ 10⁻⁵* anisotropies and acoustic peaks; BBN light elements (*Y_p*, D/H) at the order the third minute predicts; *Ω_b*, *Ω_c*, *Ω_Λ* to tens of percent; horizons of the Schwarzschild/Kerr kind (orbits, shadows, ringdowns); no universal now (Hafele–Keating; GPS; muon *γ*); accelerating expansion (Type Ia; BAO; CMB).

**Warm:** a local inflationary burst as the source of the tilt and the flatness; CDM as a collisionless fluid whose particle is unspecified (LZ/XENON nulls); *Λ* as the shove rather than a slow field; Hawking radiation as a calculation not yet photographed; WAP as a cut *if* an ensemble exists; tidal oceans on icy moons (Europa/Enceladus evidence strong for *oceans*, not for *life*); *H₀* tension as a real discrepancy without a named winner; chronology protection as a conjecture that keeps edits dead.

**Cold:** required Omega Point; SAP/FAP as physics; traversable wormholes or Alcubierre bubbles as engineering; hops between Everett branches; string landscape as an explanation (18); anthroposophy; a proven beginning “before” which there was kitchen-time; BICEP2’s *r ~ 0.2* as primordial tensors; a white hole in the catalog of the sky; a craftsman in the leftover glow.

A claim can change temperature (A0). This list is the book’s oven reading on publication day, not a creed. New digits — a tensor background, a WIMP, a *w(z)* that refuses −1, a vacuum-decay product — would move lines. They would not restore a universal now, a required final mind, or a hallway through a horizon.

---

## Equations at a Glance

| # | Relation | Role |
|---|---|---|
| (1) | *ds² = −c² dt² + dℓ²* | Interval |
| (2) | *ds² = 0* | Light |
| (3) | *t′ = γ (t − v x/c²)* | Slice tilt |
| (4) | *v = H₀ d*, *1+z = 1/a* | Stretch |
| (5) | *ρ_c = 3H₀²/8πG* | Critical density |
| (6) | *ρ_Λ = Λ c²/8πG* | Shove as constant |
| (7) | *H(z)* Friedmann | History of the stretch |
| (8) | *T ∝ 1/a* | Cooling |
| (9) | *Y_p ≈ 2(n/p)/(1+n/p)* | Helium mass fraction |
| (10) | D bottleneck *T ≲ 0.1 MeV* | Why three minutes |
| (11) | *N = ∫ H dt ~ 50–60* | E-folds |
| (12)–(13) | *P_R(k)*, *n_s ≈ 0.97* | Seeds |
| (14) | *r_s = 2GM/c²* | Horizon scale |
| (15) | *dτ = dt √(1−r_s/r)* | Well clocks |
| (16) | *S = kA/4ℓ_P²* | Area counting |
| (17) | NEC; *ρ + p_r < 0* at throat | Wormhole bill |
| (18) | A string-theory *test* would be a unique, risky, framework-level prediction that experiment could kill. None is in hand. | Untestable |

---

## Further Reading (tiered)

**Start here:** Weinberg, *The First Three Minutes*; Barrow, *The Origin of the Universe*; Ryden, *Introduction to Cosmology*; Mack, *The End of Everything*.

**Next:** Guth, *The Inflationary Universe*; Carroll, *From Eternity to Here*; Singh, *Big Bang*; Liddle, *An Introduction to Modern Cosmology*.

**Heavier:** Peebles, *Principles of Physical Cosmology*; Mukhanov, *Physical Foundations of Cosmology*; Kolb & Turner, *The Early Universe*; Weinberg, *Cosmology*.

**Icy worlds:** Nimmo & Pappalardo reviews on Europa; Spencer et al. on Enceladus; COSPAR planetary protection policy.

**Loops and selves (ideas used, not copied):** Hofstadter, *Gödel, Escher, Bach* and *I Am a Strange Loop* — tangled hierarchies, the nest as a mind, incompleteness as self-reference rather than as a proof that minds float free. The opposite incompleteness moral is the non-algorithmic camp in Chapter 31.

**Avoid as physics:** Tipler’s Omega Point as required law; any string text that forgets equation (18).

---

## Glossary

**Event.** A happening with a location in spacetime.

**Worldline.** An object’s chain of events.

**Proper time.** Length of a timelike worldline.

**Interval.** Invariant *ds²* in (1). The split into space and time is not invariant.

**Horizon (black hole).** One-way null surface.

**Horizon (cosmic).** Particle or event edge of causal contact.

**Scale factor *a*.** Dimensionless stretch of FLRW slices; *a₀ = 1* today.

**Redshift *z*.** *1 + z = 1/a* for light emitted at *a*.

**Inflation.** Brief early repulsive stretch. Local burst: warm. Eternal froth: colder.

**E-fold.** Factor *e* in *a*. Some 50–60 e-folds are the working burst.

**Dark matter.** Extra pull; not atoms; not the shove.

**Dark energy.** Extra shove; not the pull.

***w*.** Pressure over density. Λ sits at *w = −1*.

**Habitable zone (stellar).** Band where starlight *permits* surface liquid water.

**Tidal habitable environment.** Liquid water under ice, heated by flex or trapped heat.

**WAP.** Selection effect, not a purpose.

**SAP / FAP.** Strong and final anthropic claims. Not hired.

**CTC.** Closed timelike curve. A loop in the block, not an edit.

**FIRAS.** COBE spectrometer that made the leftover glow a blackbody to parts in *10⁵*.
