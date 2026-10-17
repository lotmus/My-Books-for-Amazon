# Strategy: The Quantitative Toolkit

**What you will be able to do**

- Apply the estimation habits from the companion book to the exact math this section lists.
- Estimate square roots and logarithms without a calculator, and move between pH and concentration.
- Use the handful of trigonometric values the section expects.
- Handle units, significant digits and weighted averages cleanly.

**Why it matters**

The companion book ([Core Test Skills, Chapters 13, 14 and 18]) teaches the general habits: estimate first, choose the right base for percentages, track units, and sanity-check answers. This chapter fits those habits to the specific list of math techniques that the exam owner publishes for the science sections ([Chapter 1](chapter:1) summarizes the list). If the list is the syllabus, this is the revision guide for its arithmetic.

No calculator is provided in the materials this book relies on. [VERIFY in the current test-day rules] So the aim is not to compute fast; it is to compute *enough*. Most answer choices are spaced widely apart for exactly that reason.

Praxis Tip: Before computing anything, look at the answer choices. If they differ by a factor of ten or more, an estimate to one significant figure finishes the question.

**Estimation values worth memorizing**

| Quantity | Value to carry |
|---|---|
| g (for estimation) | 10 m/s² (9.8 for care) |
| √2, √3, √5, √10 | 1.4, 1.7, 2.2, 3.2 |
| log 2, log 3, log 5 | 0.30, 0.48, 0.70 |
| ln 2, ln 10 | 0.69, 2.3 |
| sin 30° = cos 60° | 1/2 |
| cos 30° = sin 60° | √3/2 ≈ 0.87 |
| sin 45° = cos 45° | √2/2 ≈ 0.71 |
| tan 30°, tan 45°, tan 60° | 0.58, 1, 1.73 |
| sin 0°, sin 90°, sin 180° | 0, 1, 0 |
| cos 0°, cos 90°, cos 180° | 1, 0, −1 |

[VERIFY any constant against the fact sheet in the companion book ([Core Test Skills, Chapter 2]) before relying on it.]

Praxis Tip: Put this table on a flashcard deck ([Chapter 3](chapter:3), deck 2) and drill it until you do not need to think. The values are small, and they come up everywhere.

**Square roots**

To estimate √N, bracket it between squares you know. For √50: 7² = 49, so √50 ≈ 7.1. For a number written in scientific notation, make the exponent even first: √(1.8 × 10⁻⁶) = √1.8 × 10⁻³ ≈ 1.3 × 10⁻³.

**Logarithms, pH and concentration**

The base-10 log is the tool for pH. If [H⁺] = a × 10⁻ⁿ with 1 ≤ a < 10, then

pH = n − log a.

Since log 1 = 0 and log 10 = 1, a lies between 1 and 10 and its log is between 0 and 1. Using log 2 = 0.30 and log 3 = 0.48: [H⁺] = 2 × 10⁻⁴ gives pH = 4 − 0.30 = 3.70; [H⁺] = 3 × 10⁻⁵ gives pH = 5 − 0.48 = 4.52. Going the other way, a pH of 4.5 is halfway between 4 and 5, so [H⁺] is halfway on the log scale, about 3 × 10⁻⁵ (because log 3 ≈ 0.5).

Praxis Tip: A pH change of 1 is a factor of 10 in [H⁺]. A change of 0.3 is a factor of 2. A change of 0.5 is about a factor of 3. Commit those three to memory.

**Trigonometry and vectors**

Break a vector into components with a right triangle. For an angle θ measured from the horizontal axis:

- horizontal component = magnitude × cos θ
- vertical component = magnitude × sin θ

Add vectors by adding components. For a direction, use the right-hand rule, which comes up with magnetic forces ([Lesson 5](chapter:12)): point your fingers along the first vector, curl them toward the second, and your thumb points along the cross product.

**Scales and slopes**

On a linear plot, a straight line means y = mx + b, and the slope is Δy/Δx. On a semilog plot (one axis logarithmic), a straight line means exponential behavior, such as radioactive decay or a first-order reaction. On a log-log plot (both axes logarithmic), a straight line means a power law, y = k xᵖ, and the slope is the exponent p. [Strategy: Reading Experiments, Data and Graphs](chapter:6) works examples.

**Units, dimensional analysis and significant digits**

Treat units like algebra: write the conversion as a fraction equal to 1 with the unit you want on top. For significant digits: in multiplication and division, the answer carries as many significant digits as the least precise factor; in addition and subtraction, round to the least precise decimal place.

**Worked Example 1: A weak-acid pH with a square root**

*Question.* What is the pH of 0.10 M weak acid HA with Ka = 1.8 × 10⁻⁵?

*Setup.* For a weak acid with x ≪ C, Ka = x²/C, so x = [H⁺] = √(Ka × C).

*Work.* Ka × C = 1.8 × 10⁻⁵ × 0.10 = 1.8 × 10⁻⁶. x = √(1.8 × 10⁻⁶) = √1.8 × 10⁻³ ≈ 1.34 × 10⁻³ M.

pH = 3 − log 1.34 ≈ 3 − 0.13 = 2.87, about 2.9.

*Check.* The approximation needs x ≪ C: x/C = 1.34 × 10⁻³/0.10 = 1.3 percent, which is under 5 percent, so it holds. A quick mental route: √1.8 is about 1.3, log 1.3 is about 0.11, so pH ≈ 2.9.

*Skill used:* a square root with an even exponent, a log, and a check on the approximation.

**Worked Example 2: Components of a force**

*Question.* A 50 N force acts at 30° above the horizontal. What are its horizontal and vertical components?

Horizontal: 50 cos 30° ≈ 50 × 0.87 = 43.5 N (exact 43.3 N). Vertical: 50 sin 30° = 25 N.

*Check.* The components must satisfy Pythagoras: √(43.3² + 25²) = √(1875 + 625) = √2500 = 50 ✓.

**Worked Example 3: Units and significant digits**

*Question.* A rectangle measures 2.50 cm by 3.1 cm. What is its area in m², with the right number of significant digits?

The product is 2.50 × 3.1 = 7.75 cm². The less precise factor, 3.1, has two significant digits, so the answer is 7.8 cm² (rounding 7.75 up).

Convert: 7.8 cm² × (1 m / 100 cm)² = 7.8 × 10⁻⁴ m². Squaring the conversion fraction is the step people forget.

*Second conversion.* A pump delivers 5.0 mL/s. In liters per minute: 5.0 mL/s × (60 s / 1 min) × (1 L / 1000 mL) = 0.30 L/min.

**Worked Example 4: A weighted average**

*Question.* A chlorine sample is 75 percent ³⁵Cl (mass 35) and 25 percent ³⁷Cl (mass 37). What is the average atomic mass?

0.75 × 35 + 0.25 × 37 = 26.25 + 9.25 = 35.5.

*Shortcut.* The average sits between 35 and 37, a quarter of the way up: 35 + 0.25 × 2 = 35.5. No arithmetic needed beyond that.

*Skill used:* seeing a weighted average as a position on a line.

**Simultaneous equations**

When two unknowns appear, add or subtract the equations to remove one. For 2x + y = 7 and x − y = 2: adding gives 3x = 9, so x = 3, and then y = 1. Check in both: 2(3) + 1 = 7 ✓ and 3 − 1 = 2 ✓.

**More Praxis Tips**

Praxis Tip: Round to one significant figure first. If the choices are 2.8, 28, 280 and 2,800, the first estimate settles the question and the second digit is a luxury.

Praxis Tip: Write down the power of ten separately from the coefficient whenever you multiply or divide. Dropped zeros are the most common arithmetic error in this section.

Praxis Tip: Check that an answer has sensible units and a sensible size. A 70 kg person who weighs 7 N should alarm you.

Praxis Tip: When you must take a square root of something like 1.8 × 10⁻⁵, adjust the exponent to be even (18 × 10⁻⁶) before taking the root: √18 ≈ 4.2, so the answer is about 4.2 × 10⁻³.

Praxis Tip: Keep a running list of the values you had to look up. Each one is a flashcard you have not made yet.

**Common mistakes**

- Taking √ of an odd exponent directly.
- Forgetting that a log of a number between 1 and 10 is between 0 and 1.
- Squaring the units wrongly in an area or volume conversion.
- Using degrees where the formula needs radians, or vice versa.
- Over-computing when the choices are far apart.

**Do this today**

1. Make the values table into 10 flashcards (one per row) and review it daily this week.
2. Do 5 pH-to-concentration conversions without a calculator.
3. Do 5 component problems at 30°, 45° and 60°.
4. Find the last numerical question you got wrong and redo it with an estimate first.

**Recap**

Estimate first, memorize the small table, use pH = n − log a, treat units as algebra, and check every answer for size and sign. The goal is enough arithmetic, not fast arithmetic.

---

**Author verification note (remove before publishing)**

- Verified: √1.8 = 1.342; 3 − log 1.342 = 2.87; 10^(−4.5) = 3.16 × 10⁻⁵; 50 cos 30° = 43.30; 5.0 mL/s × 60 s/min = 300 mL/min = 0.30 L/min; 0.75 × 35 + 0.25 × 37 = 35.5; log 2 = 0.301, log 3 = 0.477, log 5 = 0.699; ln 2 = 0.693; ln 10 = 2.303.
- Check: 7.75 rounds to 7.8 (round-half-up convention). Mention that a rounding convention is a convention.
- The math list paraphrases the exam owner's published list; do not copy its text.
- Resolve [VERIFY] flags (calculator rule; constants vs the companion book's fact sheet).
