from figutil import *
from matplotlib.patches import Circle, Wedge, Ellipse
# 23 Hertzsprung-Russell
fig, ax = new(7.4, 5.2)
Teff = np.linspace(2800, 30000, 200)
ms_L = 10 ** (np.interp(np.log10(Teff), np.log10([2800, 3500, 4500, 5800, 7500, 10000, 20000, 30000]), np.log10([1e-3, 0.03, 0.3, 1.0, 12.0, 80.0, 6000.0, 60000.0])))
ax.plot(Teff, ms_L, color=NAVY, lw=7, alpha=0.35, solid_capstyle='round'); ax.text(6000, 0.18, 'main sequence', color=NAVY, rotation=-37, fontsize=9, ha='center', rotation_mode='anchor')
ax.add_patch(Ellipse((4400, 150), 2200, 2.0, fc='#ef9a9a', alpha=0.6, transform=ax.transData) if False else Circle((0, 0), 0));
for (x0, y0, w, h_, col, lab) in [(4300, 120, 1700, 0.9, '#ef9a9a', 'red giants'), (4500, 25000, 3500, 0.55, '#ffab91', 'supergiants'), (13000, 0.003, 14000, 0.9, '#b3e5fc', 'white dwarfs')]:
    t = np.linspace(0, 2 * np.pi, 100); ax.fill(x0 + w * 0.5 * np.cos(t), y0 * 10 ** (h_ * np.sin(t)), color=col, alpha=0.7); ax.text(x0, y0, lab, ha='center', va='center', fontsize=8.5)
ax.plot(5772, 1, 'o', color=GOLD, ms=11, mec='black'); ax.annotate('the Sun', (5772, 1), xytext=(4300, 0.25), fontsize=8.5, arrowprops=dict(arrowstyle='->', color=GREY))
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(32000, 2400); ax.set_ylim(1e-4, 2e6); ax.set_xticks([30000, 10000, 6000, 4000, 3000]); ax.set_xticklabels(['30 000', '10 000', '6000', '4000', '3000'])
ax.set_xlabel('surface temperature (K) — hotter to the left'); ax.set_ylabel('luminosity (Sun = 1)'); ax.set_title('The Hertzsprung–Russell diagram (schematic)')
save(fig, 'd01_hr', 28, 'Stars and Nuclear Burning', 'The Hertzsprung–Russell diagram plots a star’s brightness against its surface temperature. Most stars lie on the main sequence, where mass sets both; stars that have exhausted core hydrogen move up to the giants, or end as white dwarfs below the sequence. Regions are schematic.', 'A plot with temperature increasing to the left and luminosity increasing upward, both logarithmic. A band from the upper left to the lower right is the main sequence, marked with the Sun near the middle. Red giants and supergiants form clouds above it on the right, and white dwarfs form a cloud below it on the left.')
# 24 transit + RV
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.7), dpi=100)
t = np.linspace(-0.2, 0.2, 800); depth = 0.01; ing = 0.012
f_ = 1 - depth * (0.5 * (np.tanh((t + 0.07) / ing) - np.tanh((t - 0.07) / ing)))
a1.plot(t * 24, f_, color=NAVY, lw=2); a1.set_xlabel('hours from mid-transit'); a1.set_ylabel('star’s brightness'); a1.set_ylim(0.985, 1.003); a1.set_title('Transit: a Jupiter-size planet\ncrossing a Sun-like star'); a1.annotate('dip ≈ (R_planet / R_star)² ≈ 1%', xy=(0, 0.99), xytext=(-4.7, 0.9865), fontsize=7.8, color=RED)
ph = np.linspace(0, 2, 400); a2.plot(ph, 12.5 * np.sin(2 * np.pi * ph), color=RED, lw=2); a2.axhline(0, color=GREY, lw=0.5); a2.set_xlabel('orbital phase (orbits)'); a2.set_ylabel('star’s velocity along our line of sight (m/s)'); a2.set_title('Radial velocity: Jupiter tugs\nthe Sun by 12.5 m/s')
save(fig, 'd02_exoplanet_methods', 27, 'Exoplanet Detection, Demographics and Atmospheres', 'The two classic detection methods. Left: a transit dims the star by the square of the radius ratio. Right: the star’s reflex velocity measures the planet’s pull (12.5 m/s is Jupiter’s effect on the Sun). Both curves are illustrative.', 'Two panels. Left, a flat light curve with a shallow box-shaped dip of about one percent lasting a few hours. Right, a sine wave of the star’s velocity of plus and minus 12.5 metres per second over two orbits.')
# 25 habitable zone
fig, ax = new(8, 4.3); M = np.linspace(0.2, 2.0, 300); L = np.where(M < 0.43, 0.23 * M ** 2.3, M ** 4)
inner = np.sqrt(L / 1.1); outer = np.sqrt(L / 0.36)
ax.fill_between(M, inner, outer, color='#a5d6a7', alpha=0.85, label='habitable zone (liquid water possible)')
ax.plot(M, inner, color=GREEN, lw=1); ax.plot(M, outer, color=GREEN, lw=1)
ax.set_yscale('log'); ax.set_xlabel('stellar mass (Suns)'); ax.set_ylabel('orbital distance (AU)')
for nm, a, col in [('Venus', 0.72, RED), ('Earth', 1.0, NAVY), ('Mars', 1.52, '#8d3b2a')]: ax.axhline(a, color=col, lw=0.8, ls='--'); ax.text(1.97, a * 1.04, nm, fontsize=8, ha='right', color=col)
ax.text(0.22, 0.03, 'TRAPPIST-1 (0.09 Suns): its zone is a few hundredths of an AU', fontsize=7.5, color=GREY, va='top') if False else None
ax.legend(frameon=False, loc='upper left', fontsize=8); ax.set_title('Where liquid water can last, by star (approximate)')
save(fig, 'd03_habzone', 27, 'Planetary Habitability', 'The habitable zone moves outward and widens for heavier, brighter stars and shrinks toward the star for small, dim ones. Computed from main-sequence luminosities with Kasting-style flux limits of 1.1 and 0.36 times the flux Earth receives. Venus and Mars lie near the Sun’s zone edges.', 'A green band showing orbital distance, on a logarithmic scale, against stellar mass. The band rises from about 0.1 AU for a star of 0.2 solar masses to several AU for a star twice the Sun’s mass. Dashed lines mark the orbits of Venus, Earth and Mars.')
# 26 gas retention
fig, ax = new(8, 4.6); names = {'Moon': (2.38, 250), 'Mercury': (4.25, 440), 'Mars': (5.03, 210), 'Titan': (2.64, 94), 'Venus': (10.36, 735), 'Earth': (11.19, 288), 'Neptune': (23.5, 72), 'Jupiter': (59.5, 124)}
T = np.logspace(1, 3.2, 100)
for gas, m, col in [('H₂', 2.016, RED), ('He', 4.0, '#e67e22'), ('H₂O', 18.0, GREEN), ('N₂ / CO', 28.0, NAVY), ('CO₂', 44.0, PURPLE)]:
    vr = np.sqrt(3 * kB * T / (m * 1.6605e-27)) / 1000 * 6; ax.plot(T, vr, color=col, lw=1.6); ax.text(T[-1] * 1.02, vr[-1], gas, color=col, fontsize=8, va='center')
for n, (v, Tn) in names.items(): ax.plot(Tn, v, 'o', color='black', ms=5); ax.annotate(n, (Tn, v), xytext=(Tn * 1.06, v * 1.08), fontsize=8)
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(40, 2200); ax.set_ylim(1, 90); ax.set_xlabel('temperature at the top of the atmosphere (K, rough)'); ax.set_ylabel('escape speed (km/s)')
ax.set_title('Which worlds keep which gases'); ax.text(45, 1.2, 'A world keeps a gas over billions of years if its escape speed is above the line (6 × the typical molecular speed).', fontsize=7.3, color=GREY)
save(fig, 'd04_retention', 25, 'Planetary Atmospheres', 'A planet holds a gas for billions of years if its escape speed exceeds about six times the gas molecules’ typical speed. Lines show that threshold for common gases; dots are approximate values for worlds. Earth keeps nitrogen and oxygen but has lost hydrogen; Jupiter keeps everything; the Moon keeps nothing.', 'Rising curves of the speed threshold against temperature for hydrogen, helium, water, nitrogen and carbon dioxide, with hydrogen highest. Dots mark worlds by escape speed and temperature. Jupiter lies above all lines, Earth between the hydrogen and nitrogen lines, and the Moon below nearly all of them.')
# 27 rotation curve
fig, ax = new(8, 4.2); r = np.linspace(0.3, 30, 300)
v_disk = 160 * (r / 3.5) ** 1 / (1 + (r / 3.5) ** 2) ** 0.75 * 1.28
v_halo = 160 * np.sqrt((1 - np.arctan(r / 6) * 6 / r) * 1.0) * 1.0
v_obs = np.sqrt(v_disk ** 2 + (v_halo * 0.0 + 0.0) ** 2 + (190 * np.sqrt(np.clip(1 - np.arctan(r / 4) * 4 / r, 0, None))) ** 2)
v_vis = v_disk * 1.0
ax.plot(r, v_vis, color=RED, lw=2, ls='--', label='expected from visible matter alone (falls off)'); ax.plot(r, v_obs, color=NAVY, lw=2.4, label='observed (stays flat): needs a dark halo')
ax.set_ylim(0, 260); ax.set_xlabel('distance from the galaxy’s center (kpc)'); ax.set_ylabel('orbital speed (km/s)'); ax.legend(frameon=False, fontsize=8, loc='lower right'); ax.set_title('A typical spiral galaxy’s rotation curve (illustrative)')
save(fig, 'd05_rotation', 30, 'Galaxies', 'Stars far from a spiral galaxy’s center orbit as fast as those nearer in, instead of slowing as the visible mass would predict. The flat curve was a key early piece of evidence for dark matter. The curves are illustrative, shaped like real ones, not data from one galaxy.', 'Two curves of orbital speed against distance from the galaxy center. The red dashed curve for visible matter rises and then declines. The blue curve for the observed rotation rises and then stays roughly flat near 200 kilometres per second out to 30 kiloparsecs.')
# 28 scale factor
fig, ax = new(8, 4.3); t = np.linspace(0.001, 30, 3000)  # Gyr
H0 = 67.4 / 977.8  # per Gyr
Om = 0.315; OL = 0.685
a = np.zeros_like(t); ai = 1e-3;
# integrate da/dt = a H0 sqrt(Om/a^3 + Or/a^4 + OL)
Or = 9e-5; dt = 0.0002; aa = 1e-3; tt = 0.0; ts = []; as_ = []
while tt < 42:
    ts.append(tt); as_.append(aa); aa += aa * H0 * np.sqrt(Om / aa ** 3 + Or / aa ** 4 + OL) * dt; tt += dt
ts = np.array(ts); as_ = np.array(as_); i0 = np.argmin(abs(as_ - 1)); t0 = ts[i0]
sel = ts > 0.05; ax.plot(ts[sel] - t0, as_[sel], color=NAVY, lw=2.4, label='our universe (matter + dark energy)')
tm0 = 2 / (3 * H0); xm = np.linspace(-tm0 + 0.05, 25, 400); ax.plot(xm, ((xm + tm0) / tm0) ** (2 / 3), color=RED, lw=1.6, ls='--', label='matter only (same expansion rate today): always slowing')
ax.axvline(0, color=GREY, ls=':'); ax.text(0.3, 0.1, 'today (13.8 Gyr)', fontsize=8, color=GREY); ax.set_xlim(-14, 25); ax.set_ylim(0, 4.2)
ax.set_xlabel('time from today (billions of years)'); ax.set_ylabel('size of the universe (today = 1)'); ax.legend(frameon=False, fontsize=8, loc='upper left'); ax.set_title('The scale factor: from deceleration to acceleration')
save(fig, 'd06_scale_factor', 31, 'Radiation, Matter and Vacuum Eras', 'The scale factor a(t), computed from the Friedmann equation with 31.5 percent matter and 68.5 percent dark energy (dashed: a matter-only universe). Early on the expansion slows under gravity; since roughly 5 billion years ago dark energy has made it speed up.', 'A rising curve of the size of the universe against time from 14 billion years in the past to 25 billion years in the future, equal to one at the present. The blue curve flattens then steepens upward. The red dashed matter-only curve rises more slowly and keeps flattening.')
# 29 CMB spectrum
fig, ax = new(8, 4.0); nu = np.linspace(1, 600, 600) * 1e9
B = 2 * h * nu ** 3 / c ** 2 / (np.exp(h * nu / (kB * 2.7255)) - 1) * 1e20
ax.plot(nu / 1e9, B, color=NAVY, lw=2.4, label='blackbody at 2.7255 K')
rng = np.random.default_rng(1); nus = np.linspace(60, 600, 40) * 1e9; Bs = 2 * h * nus ** 3 / c ** 2 / (np.exp(h * nus / (kB * 2.7255)) - 1) * 1e20
ax.plot(nus / 1e9, Bs, 'o', color=RED, ms=4, label='COBE FIRAS measurements (errors smaller than the dots)')
ax.set_xlabel('frequency (GHz)'); ax.set_ylabel('brightness (MJy per steradian)'); ax.legend(frameon=False, fontsize=8); ax.set_title('The cosmic microwave background is the most perfect blackbody known')
save(fig, 'd07_cmb', 32, 'The Cosmic Microwave Background', 'The spectrum of the cosmic microwave background follows the Planck curve for 2.7255 K to better than one part in ten thousand. The dots stand for the measurements made by COBE’s FIRAS instrument in 1990; they lie on the curve within the line width.', 'A smooth rising and falling curve of brightness against frequency from 0 to 600 gigahertz with a peak near 160 gigahertz. Red dots stand on the curve.')
# 30 cosmic budget donut
fig, ax = new(6.4, 4.6)
vals = [68.3, 26.8, 4.9]; labs = ['dark energy\n68%', 'dark matter\n27%', 'ordinary matter\n5%']; cols = ['#1f4e79', '#6a3d9a', '#e67e22']
w, t_ = ax.pie(vals, labels=labs, colors=cols, startangle=90, counterclock=False, wedgeprops=dict(width=0.42, edgecolor='white'), textprops=dict(fontsize=9))
ax.set_title('What the universe is made of, as a share of its energy')
ax.text(0, 0, 'ordinary matter:\nstars, gas,\nyou', ha='center', va='center', fontsize=7.5, color=GREY)
save(fig, 'd08_budget', 33, 'The Dark Sector at a Glance', 'The cosmic energy budget today, from the Planck satellite’s ΛCDM fit: about 68 percent dark energy, 27 percent dark matter and 5 percent ordinary matter. Of the ordinary 5 percent, stars and planets make up only about a tenth.', 'A donut chart in three parts: 68 percent dark energy, 27 percent dark matter and 5 percent ordinary matter.')
# 31 entropy of mixing: binomial
fig, ax = new(8, 3.9); N = 100; from math import comb, log
k = np.arange(0, N + 1); W_ = np.array([comb(N, i) for i in k], dtype=float); p = W_ / W_.sum()
ax.bar(k, p, color=NAVY, width=0.9); ax.set_xlabel('number of the 100 gas molecules found in the left half of a box'); ax.set_ylabel('probability'); ax.set_title('Why gas spreads out: the even split overwhelms everything else')
ax.annotate('all 100 on one side:\n1 chance in 10³⁰', xy=(100, 1e-30 + 0.002), xytext=(72, 0.05), arrowprops=dict(arrowstyle='->', color=RED), color=RED, fontsize=8.5)
ax.annotate('about 50 : 50\n(8% for exactly 50)', xy=(50, 0.08), xytext=(18, 0.065), arrowprops=dict(arrowstyle='->', color=GREEN), color=GREEN, fontsize=8.5)
save(fig, 'd09_entropy', 35, 'Entropy', 'Entropy as counting. For 100 molecules the number of ways of having k on the left is the binomial coefficient C(100, k). Nearly all arrangements are close to an even split, so the gas ends up there; with 10²³ molecules the peak is a spike.', 'A bar chart of probability against the number of molecules in the left half. The bars form a narrow bell shape centered on 50, with a maximum of about 8 percent. Bars near 0 and 100 are invisibly small.')
# 32 cosmic calendar clock
fig, ax = new(6.4, 6.4); ax.set_aspect('equal'); ax.axis('off')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i, m in enumerate(months):
    a0 = 90 - i * 30; ax.add_patch(Wedge((0, 0), 1.0, a0 - 30, a0, fc='#ececec' if i % 2 else '#dce6f1', ec='white', lw=1)); ang = np.radians(a0 - 15); ax.text(0.86 * np.cos(ang), 0.86 * np.sin(ang), m, ha='center', va='center', fontsize=8.5)
ev = [(0.0, 'Big Bang, 1 Jan', 70), (0.996, 'dinosaurs end, 30 Dec', 108), (0.961, 'animals with shells, ~17 Dec', 132), (0.826, 'oxygen in the air, ~29 Oct', 168), (0.725, 'earliest life, ~late Sep', 200), (0.669, 'Sun and Earth form, 1 Sep', 228)]
for fr, lab, la in ev:
    ang = np.radians(90 - fr * 360); lr = np.radians(la)
    ax.plot([np.cos(ang), 1.06 * np.cos(ang)], [np.sin(ang), 1.06 * np.sin(ang)], color=RED, lw=1.4)
    ax.annotate(lab, xy=(1.06 * np.cos(ang), 1.06 * np.sin(ang)), xytext=(1.38 * np.cos(lr), 1.38 * np.sin(lr)), ha='center', va='center', fontsize=7.6, color=RED, arrowprops=dict(arrowstyle='-', color=RED, lw=0.6))
ax.text(0, 0, 'last 11 minutes:\nHomo sapiens', ha='center', va='center', fontsize=8, color=NAVY); ax.set_xlim(-1.8, 1.8); ax.set_ylim(-1.5, 1.7)
ax.set_title('The 13.8 billion years since the Big Bang, as one calendar year')
save(fig, 'd10_calendar', 0, 'The Cosmic Calendar', 'The cosmic calendar: 13.8 billion years squeezed into one year, so that one day is about 38 million years. Dates are approximate. Our species appears about eleven minutes before midnight on 31 December, and all of recorded history fits into the final twelve seconds or so.', 'A circular calendar divided into twelve months with red markers: the Big Bang on 1 January, the Sun and Earth forming on 1 September, the earliest life in late September, oxygen in the air in late October, animals with shells in mid December and the end of the dinosaurs on 30 December.')
