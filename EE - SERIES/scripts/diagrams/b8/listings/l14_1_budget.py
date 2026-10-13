"""Average current and battery life of a duty-cycled node (first-order; Book 6 adds the rest)."""

def average_ma(active_ma, active_s, sleep_ma, period_s):
    sleep_s = period_s - active_s
    return (active_ma * active_s + sleep_ma * sleep_s) / period_s

def life_days(capacity_mah, avg_ma):
    return capacity_mah / avg_ma / 24

CASES = [
    ("module, 3 s Wi-Fi",      80, 3.0, 0.020),
    ("dev board, 3 s Wi-Fi",   80, 3.0, 13.5),
    ("module, 0.8 s Wi-Fi",    80, 0.8, 0.020),
]
for name, a_ma, a_s, s_ma in CASES:
    avg = average_ma(a_ma, a_s, s_ma, 600)
    print(f"{name:22s} average {avg:7.3f} mA  life {life_days(3000, avg):7.1f} days")
