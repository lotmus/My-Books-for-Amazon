# Strategy: Reading Experiments, Data and Graphs

**What you will be able to do**

- Read an experiment's design in a fixed order and spot the controls, variables and confounders.
- Interpret linear, semilog and log-log graphs, and recover exponents, half-lives and constants from them.
- Recognize ordinary and non-ordinary behavior in tables of measurements.
- Handle the research-design and ethics questions this section asks.

**Why it matters**

About one question in five asks you to reason about research or data rather than about a principle ([Chapter 1](chapter:1)): 10 percent are about the design and execution of research, and 10 percent about data-based and statistical reasoning. Many of the other questions also arrive wrapped in a table or graph. The general method is in [Core Test Skills, Chapters 17 and 18]. This chapter adds the graph types and apparatus that appear in chemistry and physics.

Praxis Tip: Treat every figure like a small contract: the axes say what is promised, the units say how much, and the legend says who is who. Read the contract before the question tries to sell you anything.

**A fixed reading order**

1. **What was done?** Name the system and the apparatus in one sentence.
2. **What was changed (independent variable) and what was measured (dependent variable)?**
3. **What was held constant?** These are the controlled variables.
4. **What is the model or equation?** Note each symbol.
5. **What do the axes show, in what units, and on what scale (linear or logarithmic)?**
6. **What is the overall pattern, and where does it break?**
7. **Only then, the question.**

**Reading the apparatus**

Chemistry and physics passages often describe equipment: a circuit with a meter, a column of liquid, a lens on a bench, a titration, a distillation, a chromatography plate. For each, ask what it is measuring and what could go wrong.

- *Circuits:* where is the voltmeter relative to the component (in parallel), and where is the ammeter (in series)?
- *Fluids:* what is the pressure at the free surface, and what is the depth?
- *Optics:* which side of the lens is the object, and which is the image?
- *Titration:* what is in the flask, and what is in the burette?
- *Chromatography and electrophoresis:* what causes the species to separate, and which moves farther?

Praxis Tip: Draw the apparatus as a simple box-and-arrow diagram on your scratch paper. Ten seconds of drawing prevents reversed connections.

**Linear, semilog and log-log graphs**

| Graph type | A straight line means | Slope or intercept gives |
|---|---|---|
| Linear (y vs x) | y = mx + b | m = slope, b = intercept |
| Semilog (log y vs x) | y = A·e^(kx) (exponential) | slope relates to the rate constant |
| Log-log (log y vs log x) | y = k·xᵖ (power law) | slope = the exponent p |

**Worked Example 1: A log-log slope**

The terminal speeds in [Strategy: The Question Method](chapter:4) were: r = 1.0, 2.0, 3.0 mm and v_t = 0.020, 0.080, 0.180 m/s.

Take logs: log r = 0, 0.301, 0.477; log v_t = −1.699, −1.097, −0.745.

Slope between the first two points: (−1.097 − (−1.699)) / (0.301 − 0) = 0.602 / 0.301 = 2.0. Between the second and third: (−0.745 − (−1.097)) / (0.477 − 0.301) = 0.352 / 0.176 = 2.0.

A straight line of slope 2 on a log-log graph means v_t ∝ r². The exponent is the slope. The answer to "what graph is a straight line?" is: v_t versus r² on a linear graph, or log v_t versus log r on a log-log graph.

*Skill used:* recovering an exponent from two data points on a log-log plot.

**Worked Example 2: A semilog decay**

A radioactive sample has an activity A measured over time:

| t (h) | A (counts/min) |
|---|---|
| 0 | 800 |
| 6 | 400 |
| 12 | 200 |
| 18 | 100 |

Each 6-hour step halves the activity, so the half-life is 6 h. A plot of ln A against t is a straight line with slope −λ, where λ = ln 2 / t½ = 0.693 / 6 = 0.116 h⁻¹. On a semilog graph, an exponential decay is a straight line, which makes the half-life easy to read: it is the time for A to fall by a factor of 2, wherever you start.

*Check.* After 18 hours (three half-lives), A = 800 × (1/2)³ = 100 ✓.

**Worked Example 3: A titration curve**

A weak acid is titrated with a strong base. The pH rises slowly, then jumps near the equivalence point. At the *half-equivalence point* (half of the acid has been converted to its conjugate base), [HA] = [A⁻], so pH = pKa. If the pH there is read from the graph as 4.8, then pKa = 4.8, and Ka = 10⁻⁴·⁸ ≈ 1.6 × 10⁻⁵.

*Reading the shape.* The flat region around the half-equivalence point is the buffer region; the steep rise is near the equivalence point. [Lesson 16](chapter:25) works this in detail.

**Worked Example 4: Ohmic and non-ohmic**

Two devices are measured at several voltages:

| Voltage (V) | Device 1 current (mA) | Device 2 current (mA) |
|---|---|---|
| 2 | 10 | 5 |
| 4 | 20 | 15 |
| 6 | 30 | 40 |
| 8 | 40 | 100 |

For Device 1, R = V/I = 2/0.010 = 200 Ω, and the same at every row (4/0.020 = 200, and so on): the current is proportional to voltage, which is ohmic behavior. For Device 2, R = V/I = 400, 267, 150 and 80 Ω: the resistance changes with voltage, so the device is non-ohmic.

*Reading the pattern.* A straight line through the origin means proportionality; a curve means the ratio changes. You can see which by dividing a row of numbers, no graph required.

**Research design and ethics**

About one question in ten asks about how research is done. The ideas:

- **Control group and variables:** a comparison needs a group that differs only in the factor under study.
- **Confounding variable:** something else that changes along with the factor and could explain the result.
- **Sample size and repeatability:** results from few measurements are less reliable; results that repeat are stronger.
- **Blinding and randomization:** methods to keep expectations and selection from tilting the result. (In animal and human studies in particular.)
- **Accuracy and precision:** accuracy is closeness to the true value; precision is closeness of repeated measurements to each other.
- **Ethics:** informed consent, minimizing harm, honest reporting, and appropriate treatment of animals and human participants.

**Worked Example 5: A design question**

*Setup.* A researcher tests whether a coating slows corrosion of steel nails. Coated nails are placed in salt water at 25 °C; uncoated nails are placed in salt water at 40 °C. After a week, the uncoated nails are more corroded.

*Question.* Why is the experiment poorly designed for this claim? Because the coating and the temperature both differ between groups. The temperature is a confounder: faster corrosion might be due to the warmer water, not the absence of the coating. A better design changes only the coating and keeps the temperature, salt concentration and time the same.

*Skill used:* identifying the confounder.

Praxis Tip: For any "which design is best" question, ask "what else differs between the groups?" The best answer removes the extra difference.

**Reading error and statistics**

Brief reminders from [Core Test Skills, Chapter 18]: a mean without a spread is half a statement; a difference smaller than the spread is rarely convincing; check what the error bars represent; a p-value is not the probability that the hypothesis is true.

**More Praxis Tips**

Praxis Tip: When a passage gives you a model equation, write which variables are proportional and which are inversely proportional. Many data questions reduce to checking that.

Praxis Tip: For a table, compute a ratio across a row or between rows before you do anything else. If the ratio is constant, you have found a proportionality.

Praxis Tip: For any log-scale axis, remember equal spacing is equal *multiplication*, not equal addition.

Praxis Tip: When a question asks what a result "suggests" or "is consistent with," pick the answer that stays closest to what was measured. Reach beyond it only if the question invites you to.

Praxis Tip: Before reading the answer choices, say aloud what the figure shows in one sentence. If you cannot, the choices will do it for you, badly.

**Common mistakes**

- Reading a log-log slope as if it were a linear slope.
- Misreading the units on an axis (mA versus A).
- Calling an experiment "controlled" when two things changed.
- Treating correlation in a table as an explanation.
- Ignoring the title and the conditions given in the caption.

**Do this today**

1. Take two graphs from your textbook or a practice passage and apply the seven-step reading order.
2. Compute ratios across the rows of a data table and name the relationship.
3. Redo Worked Examples 1 and 2 with fresh numbers.
4. Draw a diagram of the last apparatus you read about.

**Recap**

Read the design, the variables, the axes and the pattern before the question. A straight line on a log-log plot is a power law with its slope as the exponent, on a semilog plot it is an exponential, and on a linear plot it is a proportionality. Look for confounders, and stay close to the data.

---

**Author verification note (remove before publishing)**

- Verified: log values; slopes 2.0 and 2.0; ln 2/6 = 0.1155; 10^(−4.8) = 1.58 × 10⁻⁵; resistances 400, 267, 150, 80 Ω; decay 800 → 100 after three half-lives.
- Half-equivalence pH = pKa is correct for a weak acid titrated with strong base.
- All data are invented. The research design statements are general; a reviewer should confirm accuracy/precision wording.
