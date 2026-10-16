# Strategy: Statistics for Test Takers

**What you will be able to do**

- Compute and interpret mean, median, mode and range, and know when each misleads.
- Calculate simple probabilities, including independent and dependent events.
- Interpret standard deviation, sampling issues, error bars and p-values without overclaiming.

**Why it matters**

Statistics turns up in places that do not announce themselves: a scientific passage with a p-value, a table of averages, a survey result. The goal here is not to make you a statistician. It is to make sure you can read the basic claims and notice when a conclusion has outrun the data. Statistics has the useful property that most people are confident about it and wrong, which gives you a small, quiet advantage if you are careful.

Praxis Tip: For any statistic, ask: what does it summarize, what does it hide, and how many observations stand behind it?

**Center and spread**

- **Mean:** the sum divided by the count. Sensitive to extreme values.
- **Median:** the middle value when sorted. Robust to extremes.
- **Mode:** the most frequent value.
- **Range:** maximum minus minimum.
- **Standard deviation (SD):** a typical distance of values from the mean. Bigger SD means more spread.

**Worked Example 1: An outlier**

Data: 2, 3, 3, 4, 18.

- Mean: (2 + 3 + 3 + 4 + 18) ÷ 5 = 30 ÷ 5 = 6.
- Median: sorted data are 2, 3, 3, 4, 18, so the median is 3.
- Mode: 3.
- Range: 18 − 2 = 16.

Four of the five values are 4 or less, yet the mean is 6. One outlier dragged it up. For skewed data (incomes, house prices, hospital stays), the median usually describes a "typical" case better than the mean.

**Worked Example 2: Standard deviation by hand**

Data: 4, 6, 8. Mean = 6. Deviations from the mean: −2, 0, 2. Squares: 4, 0, 4, which sum to 8. For a *sample* SD, divide by n − 1 = 2: variance = 4, SD = 2. 

You will rarely compute SDs by hand on an exam, but knowing the steps makes the idea concrete: it is the square root of the average squared distance from the mean.

Praxis Tip: For comparing spreads without calculating, look at the data: a group whose values are clustered tightly has a smaller SD than one whose values are scattered, even with the same mean.

**Probability**

- Probability = favorable outcomes ÷ total equally likely outcomes.
- **Independent events:** multiply. Two coin flips both heads: 1/2 × 1/2 = 1/4.
- **"At least one":** use the complement. At least one head in 3 flips = 1 − P(no heads) = 1 − (1/2)³ = 1 − 1/8 = 7/8.
- **Dependent events** (without replacement): the second probability changes. A bag has 3 red and 2 blue marbles. Drawing two red in a row: 3/5 × 2/4 = 6/20 = 3/10.
- **Two dice summing to 7:** 6 combinations out of 36, so 6/36 = 1/6.

Praxis Tip: When you see "at least one," immediately try the complement. It usually turns a long case-by-case count into a one-line calculation.

**Sampling**

A statistic is only as good as the sample behind it.

- **Representative sample:** resembles the population on the dimensions that matter. Random selection helps.
- **Bias:** a systematic tilt: surveying only volunteers, only people reachable by phone, only survivors.
- **Sample size:** larger samples reduce random noise, but do not cure bias. A million biased responses are still biased.

Praxis Tip: When a conclusion applies to a population, ask who was in the sample and who was left out.

**Error bars and confidence intervals**

Figures often show error bars. Always check what they represent: standard deviation (spread of data), standard error (uncertainty of the mean), or a confidence interval. Different things, different readings. Overlapping bars do not automatically mean "no real difference," and non-overlap is not automatically proof of one; the bars' definition matters.

Praxis Tip: If a passage does not say what the error bars are, the safest statement is about the means themselves, not about statistical significance.

**P-values, carefully**

A p-value answers a narrow question: "If there were truly no effect, how likely would we be to see results at least this extreme?" A p-value of 0.03 means: if there were no effect, results this extreme would show up about 3 percent of the time. It does **not** mean there is a 3 percent chance the finding is false, nor that the effect is large or important. Convention often treats p < 0.05 as "statistically significant," but that threshold is a convention, not a law of nature. A statistically significant result can be tiny, and a non-significant result can come from a sample too small to detect anything.

Praxis Tip: Watch for the words "significant" and "proved." Statistical significance is not the same as practical importance, and data seldom "prove" anything.

**Worked Example 3: Reading a claim**

*Claim.* "Students who ate breakfast scored 4 points higher on a test than those who did not (p = 0.02). So eating breakfast improves test scores."

- *What the p-value says:* if breakfast had no association with scores, a difference this large would be unusual (about 2 percent of the time).
- *What it does not say:* that breakfast caused the difference. Students who eat breakfast may differ in sleep, income, routine or motivation.
- *Better wording:* "Breakfast-eaters scored higher, and the difference is unlikely to be chance alone; the study design cannot establish that breakfast was the cause."

*Skill used:* separating a statistical result from a causal claim.

**More Praxis Tips**

Praxis Tip: When a question asks for a "typical" value in skewed data, think median.

Praxis Tip: For probability, write the sample space or a quick tree for small cases. It is slower than a formula and much less likely to be wrong.

Praxis Tip: Treat percentages from tiny samples skeptically: "50 percent of patients improved" means very little if n = 2.

Praxis Tip: Remember that averages of averages are not always the overall average unless the groups are the same size.

**Common mistakes**

- Using the mean for heavily skewed data.
- Adding probabilities that should be multiplied.
- Forgetting that a draw without replacement changes the odds.
- Reading p-values as the probability that a hypothesis is true.
- Treating a significant result as a large or important one.
- Ignoring the sample.

**Do this today**

1. Compute mean, median and range for a short list of numbers, with and without an outlier.
2. Work out "at least one head in four flips" by the complement method.
3. Find a news claim with a statistic and write what it does and does not show.

**Recap**

Center, spread, probability, sampling, and the careful reading of p-values. Statistics describes data; it does not decide what the data mean.

---

**Author verification note (remove before publishing)**

- Check arithmetic: mean of 2,3,3,4,18 = 30/5 = 6; median 3; range 16; SD of 4,6,8: sum of squares 8, ÷2 = 4, SD 2; 1−1/8 = 7/8; (3/5)(2/4) = 3/10; 6/36 = 1/6.
- A statistician should confirm the p-value, error-bar and sampling statements are accurately and fairly phrased.
