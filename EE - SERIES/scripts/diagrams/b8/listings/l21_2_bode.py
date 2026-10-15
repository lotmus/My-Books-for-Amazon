"""Plot sweep.csv as a Bode magnitude plot and mark the -3 dB point."""
import csv
import matplotlib.pyplot as plt

with open("sweep.csv", newline="") as f:
    rows = [tuple(map(float, r)) for r in list(csv.reader(f))[1:]]
freq = [r[0] for r in rows]
gain = [r[3] for r in rows]

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.semilogx(freq, gain, "o-", ms=3)
ax.axhline(-3.01, ls="--", color="gray")
ax.set_xlabel("frequency (Hz)")
ax.set_ylabel("gain (dB)")
ax.grid(True, which="both", alpha=0.3)
fig.tight_layout()
fig.savefig("bode.png", dpi=100)
print("saved bode.png with", len(rows), "points")
