# Lesson 12: The Gas Phase

**What you will be able to do**

- Use the ideal gas law and its special cases (Boyle's, Charles's, Avogadro's) for single-state and before-and-after problems.
- Apply Dalton's law, mole fractions and partial pressures, including to the gases of respiration.
- Describe the kinetic molecular theory of gases and what it predicts about speed, temperature and mass.
- Use Graham's law for effusion and diffusion.
- Explain how and why real gases depart from ideal behavior.

**Why it matters for the exam**

Gases belong to category 4B, alongside fluids, because a body moves gases as well as liquids: air into the lungs, oxygen into the blood, carbon dioxide out. The ideal gas law connects four measurable quantities (pressure, volume, amount and temperature), and Dalton's law explains why the partial pressure of oxygen, not its percentage, drives gas exchange. This lesson is nearly all ratio reasoning: if the pressure doubles and the temperature is held constant, what happens to the volume? The exam rewards answering that without a calculator.

Praxis Tip: Always convert to kelvin. Temperature in Celsius makes every gas law give the wrong answer, and exams know it. Add 273 to the Celsius temperature (273.15 if you are being formal).

**Concept Review**

**Pressure and temperature.** Gas pressure is the force per unit area exerted by molecules colliding with the walls of a container. Common units: 1 atm = 760 mmHg = 760 torr = 101.3 kPa. A simple mercury barometer measures atmospheric pressure from the height of a column of mercury. Temperature must be in kelvin (K = °C + 273) in all gas-law work.

**The ideal gas law.**

    P V = n R T

where n is the moles of gas and R is the gas constant: 0.0821 L·atm/(mol·K), or 8.31 J/(mol·K). An **ideal gas** is a model in which molecules have negligible volume and no attractions. At **STP** (0 °C and 1 atm), one mole of ideal gas occupies 22.4 L (the molar volume).

**Special cases (each law holds the quantities listed in the middle column constant):**

| Law | Held constant | Relationship |
|---|---|---|
| Boyle's | T, n | P V = constant (P and V inversely proportional) |
| Charles's | P, n | V / T = constant (V and T directly proportional) |
| Gay-Lussac's | V, n | P / T = constant |
| Avogadro's | P, T | V / n = constant |
| Combined | n | P₁V₁ / T₁ = P₂V₂ / T₂ |

Praxis Tip: For a before-and-after problem, write the ratio of what changes: "V₂ / V₁ equals the pressure factor times the temperature factor." Do each factor by reasoning (pressure halves, so volume doubles) and multiply. It rarely needs a calculator.

**Dalton's law of partial pressures.** In a mixture of ideal gases, each gas exerts the pressure it would exert alone, and the total pressure is the sum:

    P_total = P₁ + P₂ + ...,    P_i = X_i × P_total

where X_i, the **mole fraction**, is the moles of gas i divided by the total moles. The partial pressure of a gas is its mole fraction times the total pressure.

**Kinetic molecular theory (KMT).** The ideal gas model rests on these assumptions: gas molecules are in constant, random motion; they are very small compared with the distances between them; they exert no forces on each other except in collisions; and collisions are perfectly elastic. The key consequences:

- The average kinetic energy of the molecules is proportional to the absolute temperature, KE_avg = (3/2) k_B T, with the Boltzmann constant k_B = 1.38 × 10⁻²³ J/K. At the same temperature, *all* ideal gases have the same average kinetic energy, regardless of their mass.
- Since KE = ½ m v², lighter molecules move faster at the same temperature. The root-mean-square speed is v_rms = √(3 R T / M), where M is the molar mass.
- Temperature is therefore a measure of average molecular kinetic energy.

**Graham's law.** At the same temperature, the rate of **effusion** (escape through a tiny hole) or diffusion of a gas is inversely proportional to the square root of its molar mass:

    rate₁ / rate₂ = √(M₂ / M₁)

Lighter gases effuse faster.

**Real gases.** Real gases deviate from ideal behavior when the model's assumptions fail: at **high pressure** (molecules are crowded, so their own volume matters) and at **low temperature** (molecules move slowly enough that attractions matter). The van der Waals equation corrects for both:

    (P + a n² / V²)(V − n b) = n R T

The term b corrects for the volume the molecules occupy; the term a corrects for the attractions between them. Gases with strong intermolecular forces (large a) deviate more from ideality.

Qualitatively, real gases behave most ideally at **low pressure and high temperature**.

**Heat capacity.** The heat capacity at constant volume (C_v) and at constant pressure (C_p) describe how much heat is needed to raise a gas's temperature. C_p is larger than C_v because, at constant pressure, some of the heat goes into doing work as the gas expands.

**Gas exchange in the body.** Air is about 21 percent oxygen by mole fraction. At sea level (760 mmHg), the partial pressure of oxygen is 0.21 × 760 ≈ 160 mmHg. In the lungs, inhaled air is humidified and mixed with gas already there, so the alveolar partial pressure of oxygen is lower, around 100 mmHg. Gases diffuse from regions of higher partial pressure to lower, which is why oxygen enters the blood and carbon dioxide leaves it.

**Worked Example 1: The ideal gas law (skill: choosing R)**

Two moles of an ideal gas occupy 10 L at 300 K. What is the pressure?

P = n R T / V = (2.0)(0.0821)(300) / 10 = 49.3 / 10 = 4.9 atm.

*Estimate check.* 2 × 0.08 × 300 / 10 ≈ 4.8 atm ✓. At STP (273 K), 2 mol would occupy 44.8 L at 1 atm, so squeezing it into 10 L (about a quarter) at slightly higher temperature should give about 4.5 to 5 atm ✓.

**Worked Example 2: A before-and-after problem (skill: factor reasoning)**

A balloon holds 2.0 L of gas at 1.0 atm and 300 K. It is taken to a place where the pressure is 0.50 atm and the temperature 250 K. What is the new volume?

Pressure halves, so the volume factor is ×2. Temperature goes from 300 K to 250 K, so the volume factor is ×(250/300) = ×0.833. V₂ = 2.0 × 2 × 0.833 = 3.3 L.

*Check.* The pressure drop dominates, so the balloon expands ✓.

**Worked Example 3: Dalton and respiration (skill: mole fraction)**

(a) A flask contains 2.0 mol N₂, 1.0 mol O₂ and 1.0 mol Ar at a total pressure of 2.0 atm. Find each partial pressure. (b) What is the partial pressure of O₂ in dry air at 760 mmHg?

(a) Total moles 4.0. Mole fractions: N₂ 0.50, O₂ 0.25, Ar 0.25. Partial pressures: N₂ 1.0 atm, O₂ 0.50 atm, Ar 0.50 atm, summing to 2.0 atm ✓.

(b) P_O₂ = 0.21 × 760 ≈ 160 mmHg.

**Worked Example 4: Graham's law and KMT (skill: ratios of square roots)**

(a) How much faster does helium (M = 4) effuse than oxygen (M = 32)? (b) How do the rms speeds of H₂ (M = 2) and O₂ (M = 32) compare at the same temperature? (c) What happens to v_rms if T quadruples?

(a) Rate ratio = √(32 / 4) = √8 ≈ 2.8. (b) √(32 / 2) = √16 = 4: hydrogen molecules are 4 times faster. (c) v_rms ∝ √T, so quadrupling T doubles v_rms.

**Worked Example 5: Molar mass from density (skill: molar volume)**

A gas has a density of 1.96 g/L at STP. What is its molar mass, and what gas might it be?

One mole occupies 22.4 L, so the mass of 22.4 L = 1.96 × 22.4 = 43.9 g. Molar mass ≈ 44 g/mol: consistent with CO₂ (or propane, C₃H₈, so more information would be needed to be certain).

**Worked Example 6: Gas stoichiometry (skill: connecting moles to volume)**

Heating 12.25 g of KClO₃ (molar mass 122.5 g/mol) decomposes it: 2 KClO₃ → 2 KCl + 3 O₂. What volume of O₂ at STP forms?

Moles KClO₃ = 12.25 / 122.5 = 0.100 mol. Moles O₂ = 0.100 × (3/2) = 0.150 mol. Volume = 0.150 × 22.4 = 3.36 L.

*Skill used:* the mole bridge from [Lesson 10](chapter:18), finishing with the molar volume.

**More Praxis Tips**

Praxis Tip: Write the units next to R. Which R you need is decided by the units of P and V in the problem. If P is in atm and V in liters, use 0.0821.

Praxis Tip: For gases collected over water, subtract the water vapor's partial pressure from the total to find the dry gas's pressure. The question will supply the vapor pressure.

Praxis Tip: To compare partial pressures, compare mole fractions. The total pressure scales them all by the same number.

Praxis Tip: A heavier gas at the same temperature has the same average kinetic energy but is slower. Say both halves of that sentence aloud and the common mistake disappears.

Praxis Tip: When a question says "deviates most from ideal behavior," think of molecules that are large, polar, or cold, at high pressure.

**Common Mistakes**

- Using Celsius in a gas law.
- Using the wrong R for the units given.
- Saying heavier gases have more kinetic energy at the same temperature.
- Treating the percent composition of air as a partial pressure without multiplying by the total pressure.
- Forgetting to square-root the molar-mass ratio in Graham's law.
- Applying 22.4 L/mol at conditions other than STP.

**Checkpoint Questions**

1. At constant temperature, the pressure on a fixed amount of an ideal gas is doubled. The volume of the gas
   A. doubles
   B. is unchanged
   C. is multiplied by four
   D. is halved

2. What volume does 0.50 mol of an ideal gas occupy at STP (0 °C and 1 atm)?
   A. 22.4 L
   B. 44.8 L
   C. 11.2 L
   D. 5.6 L

3. A rigid sealed container holds a gas at 300 K. The temperature is raised to 600 K. The pressure
   A. doubles
   B. is halved
   C. is unchanged
   D. increases by a factor of √2

4. A mixture of 3.0 mol H₂ and 1.0 mol He has a total pressure of 8.0 atm. The partial pressure of He is
   A. 1.0 atm
   B. 2.0 atm
   C. 6.0 atm
   D. 8.0 atm

5. Which of the following gases effuses fastest at a given temperature?
   A. H₂
   B. He
   C. CH₄
   D. CO₂

6. A real gas is most likely to deviate from ideal behavior at
   A. low pressure and high temperature
   B. low pressure and low temperature
   C. high pressure and high temperature
   D. high pressure and low temperature

7. At the same temperature, the average kinetic energy of the molecules of an ideal gas
   A. is greater for gases with greater molar mass
   B. is the same for all gases, regardless of molar mass
   C. is greater for gases with smaller molar mass
   D. depends on the pressure but not the temperature

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **D.** Boyle's law: P V is constant at fixed T and n, so doubling P halves V. (A treats pressure and volume as directly proportional; B ignores the effect of pressure; C squares the relationship.)
2. **C.** One mole occupies 22.4 L at STP, so 0.50 mol occupies 11.2 L. (A is the volume of one mole, not half a mole; B is the volume of two moles; D is the volume of a quarter of a mole.)
3. **A.** At constant V and n, P / T is constant (Gay-Lussac), so doubling the absolute temperature doubles the pressure. (B inverts the dependence on temperature; C forgets that pressure depends on temperature at fixed volume; D applies the square root that belongs to the molecular speed, not to the pressure.)
4. **B.** The mole fraction of He is 1.0 / 4.0 = 0.25, so P_He = 0.25 × 8.0 = 2.0 atm. (A uses the moles instead of the mole fraction; C is the partial pressure of H₂; D is the total pressure.)
5. **A.** By Graham's law, the effusion rate is inversely proportional to the square root of the molar mass, and H₂ is the lightest. (B is heavier than H₂; C is much heavier than H₂; D is the heaviest of the choices.)
6. **D.** At high pressure the molecules' own volume matters, and at low temperature the attractions between them matter; both break the ideal-gas assumptions. (A is where real gases behave most ideally; B fixes the pressure at the ideal end; C fixes the temperature at the ideal end.)
7. **B.** KE_avg = (3/2) k_B T depends only on the absolute temperature. Lighter molecules move faster, but the average kinetic energy is the same. (A assumes heavier molecules must carry more energy; C confuses speed with kinetic energy; D reverses the dependence.)

Praxis Tip: After the checkpoint questions, look at each wrong choice and name the slip (Celsius used, wrong direction of proportionality, forgotten square root). Log it in your error log ([Strategy: The Question Method](chapter:4)).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "P V equals n R T, with temperature in kelvin; at fixed amount, volume goes inversely with pressure and directly with temperature; each gas in a mixture contributes its mole fraction times the total pressure; at the same temperature all gases have the same average kinetic energy so lighter ones are faster, with rates going as one over the square root of the molar mass; and real gases misbehave at high pressure and low temperature."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 2 and 3 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set that includes [Lesson 4](chapter:11) fluids and [Lesson 10](chapter:18) stoichiometry), and after 21 days (explain the lesson aloud).

*Interleave:* alternate a gas problem with a fluids problem and a stoichiometry problem. [Lesson 13](chapter:21) moves from gases to solutions.

Praxis Tip: End each study session by writing, from memory, P V = n R T, the combined gas law, Dalton's law with mole fractions, v_rms ∝ √(T/M), Graham's law, and the molar volume at STP.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Verified: 4.9 atm; V₂ = 3.3 L; mole fractions and partial pressures; √8 = 2.83, √16 = 4; 1.96 × 22.4 = 43.9 g; 0.100 mol KClO₃ → 0.150 mol O₂ → 3.36 L; 0.21 × 760 = 160 mmHg.
- Answer key positions: D, C, A, B, A, D, B.
- Resolve [VERIFY]: alveolar partial pressure of oxygen (about 100 mmHg); statements about heat capacity; R values.
- Category 4B gas-phase topics covered: absolute temperature (K), pressure and barometer, molar volume at 0 °C and 1 atm (22.4 L/mol), ideal gas and gas laws (Boyle, Charles, Avogadro), kinetic molecular theory, heat capacity at constant volume and pressure, Boltzmann's constant, real gas deviations (qualitative and quantitative, van der Waals), partial pressure and mole fraction, Dalton's law.
