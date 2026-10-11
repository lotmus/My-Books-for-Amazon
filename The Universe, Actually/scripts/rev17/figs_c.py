from figutil import *
from matplotlib.patches import Circle, Polygon
# 17 Minkowski light cone
fig, ax = new(6.6, 4.8); ax.set_xlim(-4, 4); ax.set_ylim(-4, 4); ax.set_aspect('equal')
ax.fill([0, 4, -4], [0, 4, 4], color='#c9e2f5', alpha=0.9, lw=0); ax.fill([0, 4, -4], [0, -4, -4], color='#f5d9c9', alpha=0.9, lw=0)
ax.fill([0, 4, 4], [0, 4, -4], color='#eeeeee', lw=0); ax.fill([0, -4, -4], [0, 4, -4], color='#eeeeee', lw=0)
ax.plot([-4, 4], [-4, 4], color=GOLD, lw=2); ax.plot([-4, 4], [4, -4], color=GOLD, lw=2)
ax.annotate('', xy=(0, 3.9), xytext=(0, -3.9), arrowprops=dict(arrowstyle='->', color='#333')); ax.annotate('', xy=(3.9, 0), xytext=(-3.9, 0), arrowprops=dict(arrowstyle='->', color='#333'))
ax.text(0.12, 3.8, 'time (ct)', fontsize=8.5); ax.text(3.0, -0.3, 'space (x)', fontsize=8.5)
ax.text(0, 2.4, 'absolute future\n(can be influenced from here)', ha='center', fontsize=8.5); ax.text(0, -2.6, 'absolute past\n(can have influenced here)', ha='center', fontsize=8.5)
ax.text(2.7, 0.6, '“elsewhere”:\nno cause or effect', ha='center', fontsize=8, color=GREY); ax.text(-2.7, 0.6, '“elsewhere”', ha='center', fontsize=8, color=GREY)
ax.text(3.1, 3.5, 'light', color='#8a6a00', fontsize=8.5, rotation=45, ha='center'); tt = np.linspace(-3.6, 3.6, 100); ax.plot(0.35 * np.sin(tt * 0.9) * 1.2 + 0.0 * tt, tt, color=RED, lw=2, label='a possible worldline'); ax.legend(frameon=False, loc='lower left', fontsize=8)
ax.plot(0, 0, 'ko'); ax.text(0.15, -0.35, 'here, now', fontsize=8.5); ax.axis('off'); ax.set_title('The light cone of an event')
save(fig, 'c01_lightcone', 18, 'The Speed of Light and the Structure of Spacetime', 'The light cone divides spacetime around an event into the future and past that can be causally connected to it and the “elsewhere” that cannot. Any possible worldline stays inside the cone.', 'A spacetime diagram with space horizontal and time vertical. Two diagonal lines through the central event, drawn at 45 degrees for light, bound a blue upper region labelled absolute future and an orange lower region labelled absolute past. The left and right regions are labelled elsewhere. A red wavy line stays inside the cone.')
# 18 gamma vs v
fig, ax = new(8, 4.2); v = np.linspace(0, 0.9995, 2000); g_ = 1 / np.sqrt(1 - v * v)
ax.plot(v, g_, color=NAVY, lw=2); ax.set_yscale('log'); ax.set_xlim(0, 1); ax.set_ylim(0.9, 80)
for vv, lab in [(0.1, 'a jet fighter would be\ntoo slow to see'), (0.6, ''), (0.9, ''), (0.99, ''), (0.998, 'a cosmic-ray muon')]:
    gg = 1 / np.sqrt(1 - vv * vv)
    if lab != 'a jet fighter would be\ntoo slow to see': ax.plot(vv, gg, 'o', color=RED); ax.annotate('%.2f' % gg if gg < 10 else '%.1f' % gg, (vv, gg), xytext=(vv - 0.07, gg * 1.25), fontsize=8, color=RED)
ax.text(0.5, 1.02, '≈ 1 up to about 10% of c', fontsize=8, color=GREY); ax.set_xlabel('speed as a fraction of the speed of light'); ax.set_ylabel('time-dilation factor γ (log scale)')
ax.set_title('How strongly clocks slow and lengths shrink: γ = 1/√(1 − v²/c²)')
save(fig, 'c02_gamma', 18, 'Length Contraction and Time Dilation', 'The Lorentz factor γ against speed. It is negligible in everyday life and climbs without limit as v approaches c. At 0.6c a moving clock runs 25 percent slow; at 0.998c, the speed of the muons in the worked example, γ ≈ 16.', 'A curve of the Lorentz factor on a logarithmic vertical axis against speed from zero to almost the speed of light. It stays near one until about 0.5 of c, then rises steeply. Marked points show 1.25 at 0.6c, 2.3 at 0.9c, 7.1 at 0.99c and about 16 at 0.998c.')
# 19 GPS clock drift
fig, ax = new(8, 4.4); GM = 3.986004e14; R = 6.371e6; r = np.linspace(R, 4.4e7, 800)
sr = -0.5 * GM / r / c ** 2 * 86400e6; gr = GM * (1 / R - 1 / r) / c ** 2 * 86400e6
ax.plot((r - R) / 1e3, gr, color=RED, lw=2, label='gravity: higher clocks run fast'); ax.plot((r - R) / 1e3, sr, color=NAVY, lw=2, label='motion: orbiting clocks run slow'); ax.plot((r - R) / 1e3, gr + sr, color='black', lw=2.4, label='net drift')
ax.axvline(20200, color=GREY, ls=':'); ax.text(20700, -12, 'GPS orbit\n20 200 km\nnet ≈ +38 µs/day', fontsize=8, color=GREY)
ax.axhline(0, color=GREY, lw=0.6); ax.set_xlabel('altitude above the surface (km)'); ax.set_ylabel('clock rate relative to the ground (µs per day)'); ax.legend(frameon=False, fontsize=8, loc='upper left'); ax.set_title('Relativity and the clocks of a navigation satellite')
save(fig, 'c03_gps', 20, 'GPS and Relativity', 'Computed rate difference between an orbiting clock and a clock on the ground (ignoring Earth’s rotation). At GPS altitude the gravitational gain of about 46 µs per day outweighs the 7 µs lost to speed, leaving a net gain near 38 µs per day, which would build into kilometres of positioning error if left uncorrected.', 'Three curves against altitude. A red curve for the gravitational effect rises steadily to about plus 50 microseconds per day at high altitude. A blue curve for orbital speed falls to about minus 12 and flattens. The black net curve crosses zero at roughly 3000 kilometres, and a dotted line marks the GPS orbit at 20,200 kilometres where the net is about plus 38.')
# 20 chirp
fig, ax = new(8, 4.0); Msun = 4.925491e-6; m1 = m2 = 30.0; Mc = (m1 * m2) ** 0.6 / (m1 + m2) ** 0.2 * Msun
tc = 0.0; tau = np.linspace(0.38, 0.0035, 60000)
f = (1 / np.pi) * (5 / (256 * tau)) ** (3 / 8) * Mc ** (-5 / 8)
dt = tau[0] - tau[1]; phase = 2 * np.pi * np.cumsum(f) * dt
A = (f / 35) ** (2 / 3)
keep = f < 230; t = -tau[keep]; h = A[keep] * np.cos(phase[keep]);
ring_t = np.linspace(0, 0.03, 600); ring = h[-1:] * 0 + A[keep][-1] * np.exp(-ring_t / 0.004) * np.cos(2 * np.pi * 250 * ring_t + phase[keep][-1])
ax.plot(np.r_[t + 0.0, ring_t + t[-1]], np.r_[h, ring] * 1.0, color=NAVY, lw=0.9)
ax.set_xlabel('time before the merger (s)'); ax.set_ylabel('strain (relative)'); ax.set_yticks([]); ax.set_title('The chirp of two 30-solar-mass black holes merging')
ax.annotate('frequency and amplitude\nrise together', xy=(-0.05, 0.55), xytext=(-0.32, 0.9), arrowprops=dict(arrowstyle='->', color=RED), color=RED, fontsize=8)
ax.annotate('merger and ringdown', xy=(0.004, -0.3), xytext=(-0.13, -1.05), arrowprops=dict(arrowstyle='->', color=RED), color=RED, fontsize=8)
save(fig, 'c04_chirp', 21, 'The Signal That Traveled for a Billion Years', 'A simulated gravitational-wave chirp from two black holes of 30 solar masses, drawn from the leading-order inspiral formula with a damped ringing tail attached by hand. Frequency and strength rise together as the holes spiral in; the real GW150914 signal swept from 35 to 250 Hz in about 0.2 seconds.', 'A wave trace against time that begins with slow, small oscillations and grows steadily in both frequency and height over a third of a second, ending in a short burst and a quickly fading ringing.')
# 21 black hole radii
fig, ax = new(6.4, 5.0); ax.set_xlim(-4.2, 4.2); ax.set_ylim(-4.2, 4.2); ax.set_aspect('equal'); ax.axis('off')
for rad, col, lab, ang in [(3.0, '#d6eaf8', 'innermost stable circular orbit: 3 Rₛ', 135), (1.5, '#aed6f1', 'photon sphere: 1.5 Rₛ', 45)]:
    ax.add_patch(Circle((0, 0), rad, fc=col, ec=NAVY, lw=1, ls='--'))
ax.add_patch(Circle((0, 0), 1.0, fc='black', ec=RED, lw=2)); ax.text(0, 0, 'event\nhorizon\nRₛ = 2GM/c²', ha='center', va='center', color='white', fontsize=8)
ax.annotate('photon sphere, 1.5 Rₛ: light can orbit\n(unstable)', xy=(1.06, 1.06), xytext=(1.9, 3.3), arrowprops=dict(arrowstyle='->', color=NAVY), fontsize=8.5, color=NAVY)
ax.annotate('innermost stable circular orbit, 3 Rₛ:\nclosest steady orbit for matter', xy=(-2.12, -2.12), xytext=(-4.1, -3.55), arrowprops=dict(arrowstyle='->', color=NAVY), fontsize=8.5, color=NAVY)
ax.text(0, -3.05, '', fontsize=8); ax.set_title('Three radii around a non-rotating black hole')
ax.text(0, -4.15, 'for a 10-solar-mass hole, Rₛ ≈ 30 km', ha='center', fontsize=8.5, color=GREY)
save(fig, 'c05_bh_radii', 22, 'What a Black Hole Is', 'The geometry outside a non-rotating black hole, in units of the Schwarzschild radius Rₛ = 2GM/c². Light can circle the hole at 1.5 Rₛ; gas can orbit steadily only outside 3 Rₛ, so accretion disks end there and then plunge inward.', 'Concentric circles around a black disk. The black disk is the event horizon of radius Rs. A circle at one and a half Rs marks the photon sphere. A larger circle at three Rs marks the innermost stable circular orbit.')
# 22 Page curve
fig, ax = new(8, 4.2); t = np.linspace(0, 1, 400); tp = 0.5
Sh = np.sin(np.pi * t / 2) ** 1.0 * 1.0 * 1.0
S_hawk = 2 * t * (1 - 0.45 * t) / 1.1; S_page = np.where(t < tp, S_hawk, S_hawk[np.searchsorted(t, tp)] * (1 - (t - tp) / (1 - tp)) ** 1.0)
ax.plot(t, S_hawk, color=RED, lw=2, ls='--', label='thermal radiation (Hawking’s calculation): keeps rising'); ax.plot(t, S_page, color=NAVY, lw=2.4, label='unitary evaporation (Page curve): rises, then falls to zero')
ax.axvline(tp, color=GREY, ls=':'); ax.text(tp + 0.01, 0.05, 'Page time:\nhalf the entropy radiated', fontsize=8, color=GREY)
ax.set_xlabel('time, from formation to complete evaporation →'); ax.set_ylabel('entanglement entropy of the radiation'); ax.set_xticks([]); ax.set_yticks([]); ax.legend(frameon=False, fontsize=8, loc='upper left'); ax.set_title('The Page curve (schematic)')
save(fig, 'c06_page', 24, 'The Page Curve and the Paradox', 'A schematic of the information puzzle. If Hawking radiation were exactly thermal, the radiation’s entanglement would grow for ever (dashed). If evaporation is unitary, it must peak at the Page time and fall to zero (solid). Island calculations reproduce the solid curve.', 'Two curves of entanglement entropy against time. A red dashed curve rises throughout. A blue curve rises until the Page time, marked by a dotted vertical line at the middle, then falls back to zero at the end of evaporation.')
