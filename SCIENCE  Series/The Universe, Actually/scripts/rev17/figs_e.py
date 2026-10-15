from figutil import *
from matplotlib.patches import Circle, Wedge, Rectangle, FancyArrowPatch
# 33 Hardy-Weinberg + drift
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.9), dpi=100)
p = np.linspace(0, 1, 200)
a1.plot(p, p * p, color=NAVY, lw=2, label='AA'); a1.plot(p, 2 * p * (1 - p), color=GREEN, lw=2, label='Aa'); a1.plot(p, (1 - p) ** 2, color=RED, lw=2, label='aa')
a1.set_xlabel('frequency p of allele A'); a1.set_ylabel('frequency of genotype'); a1.legend(frameon=False, fontsize=8); a1.set_title('Hardy–Weinberg: p², 2pq, q²')
rng = np.random.default_rng(7)
for N, col, lab in [(20, RED, 'population of 20'), (500, NAVY, 'population of 500')]:
    for k in range(6):
        f = 0.5; tr = [f]
        for g in range(100): f = rng.binomial(2 * N, f) / (2 * N); tr.append(f)
        a2.plot(tr, color=col, lw=1, alpha=0.8, label=lab if k == 0 else None)
a2.set_xlabel('generation'); a2.set_ylabel('frequency of allele A'); a2.legend(frameon=False, fontsize=8, loc='upper left', ncol=2, bbox_to_anchor=(0.0, 1.0)); a2.set_title('Genetic drift: chance matters most\nin small populations'); a2.set_ylim(-0.02, 1.02)
save(fig, 'e01_popgen', 38, 'Population Genetics', 'Left: with random mating and no selection, genotype frequencies settle into p², 2pq and q² in one generation. Right: simulated drift with no selection. Six runs each start with allele A at 50 percent; in a population of 20 the allele soon drifts to loss or fixation, while in 500 it barely moves.', 'Left, three curves of genotype frequency against allele frequency: a rising parabola for AA, a hump peaking at one half for Aa and a falling parabola for aa. Right, six red random-walk lines in a small population wander to zero or one within a few dozen generations, while six blue lines in a large population stay near 0.5.')
# 34 Hodgkin-Huxley action potential
def hh(t, y, I):
    V, m, hh_, n = y
    am = 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10)) if abs(V + 40) > 1e-6 else 1.0; bm = 4 * np.exp(-(V + 65) / 18)
    ah = 0.07 * np.exp(-(V + 65) / 20); bh = 1 / (1 + np.exp(-(V + 35) / 10))
    an = 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10)) if abs(V + 55) > 1e-6 else 0.1; bn = 0.125 * np.exp(-(V + 65) / 80)
    INa = 120 * m ** 3 * hh_ * (V - 50); IK = 36 * n ** 4 * (V + 77); IL = 0.3 * (V + 54.387)
    return [(I(t) - INa - IK - IL), am * (1 - m) - bm * m, ah * (1 - hh_) - bh * hh_, an * (1 - n) - bn * n]
tt = np.arange(0, 30, 0.01); Ist = lambda t: 30.0 if 2 <= t < 3 else 0.0
V0 = -65.0; y0 = [V0, 0.0529, 0.5961, 0.3177]
Y = rk4(lambda t, y: hh(t, y, Ist), y0, tt)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 4.6), dpi=100, sharex=True, gridspec_kw={'height_ratios': [3, 1]})
a1.plot(tt, Y[:, 0], color=NAVY, lw=2); a1.set_ylabel('membrane voltage (mV)'); a1.set_title('One nerve impulse (Hodgkin–Huxley model of the squid giant axon)')
a1.axhline(-65, color=GREY, lw=0.5, ls=':'); a1.text(20, -60, 'resting: about −65 mV', fontsize=8, color=GREY)
ip = int(np.argmax(Y[:, 0])); im_ = ip + int(np.argmin(Y[ip:ip + 1500, 0])); ir = int(np.argmax(Y[:ip, 0] > -20))
a1.annotate('sodium channels open:\nvoltage shoots up', xy=(tt[ir], Y[ir, 0]), xytext=(tt[ir] - 1.9, 25), arrowprops=dict(arrowstyle='->', color=RED), color=RED, fontsize=8, ha='right')
a1.annotate('potassium channels open:\nvoltage falls and undershoots', xy=(tt[im_], Y[im_, 0]), xytext=(tt[im_] + 3, -45), arrowprops=dict(arrowstyle='->', color=GREEN), color=GREEN, fontsize=8)
a2.fill_between(tt, [Ist(x) for x in tt], color=GOLD, alpha=0.8, step='mid'); a2.set_ylabel('stimulus'); a2.set_xlabel('time (ms)'); a2.set_yticks([])
save(fig, 'e02_action_potential', 49, 'The Nervous System', 'A computed nerve impulse. A brief stimulus pushes the membrane past threshold; sodium channels open and the voltage spikes to about +40 mV within a millisecond, then potassium channels open and the voltage falls back, briefly undershooting the resting level. The shape is all-or-none.', 'Two panels. The upper trace of membrane voltage against time sits at minus 65 millivolts, spikes to about plus 40 shortly after a brief stimulus shown in the lower panel, falls below rest and recovers. Annotations mark sodium channel opening on the rise and potassium channel opening on the fall.')
# 35 logistic growth
fig, ax = new(8, 4.0); t = np.linspace(0, 20, 300); K = 1000; r = 0.6; N0 = 10
Nl = K / (1 + (K / N0 - 1) * np.exp(-r * t)); Ne = N0 * np.exp(r * t)
ax.plot(t, Ne, color=RED, lw=1.8, ls='--', label='unlimited growth: exponential'); ax.plot(t, Nl, color=NAVY, lw=2.4, label='limited by resources: logistic'); ax.axhline(K, color=GREY, ls=':'); ax.text(0.3, K * 1.03, 'carrying capacity K', fontsize=8, color=GREY)
ax.set_ylim(0, 1300); ax.set_xlabel('time'); ax.set_ylabel('population size'); ax.legend(frameon=False, fontsize=8, loc='center right'); ax.set_title('Population growth with and without limits')
save(fig, 'e03_logistic_growth', 61, 'Ecology', 'Population growth. With unlimited resources growth is exponential (dashed). Competition, predation and disease slow it as numbers rise, giving the S-shaped logistic curve that levels off at the carrying capacity K.', 'A blue S-shaped curve rising from about 10 to a ceiling of 1000 labelled carrying capacity, and a red dashed exponential curve that shoots upward past the ceiling.')
# 36 energy balance schematic
fig, ax = new(8, 4.6); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(0, 6)
ax.add_patch(Rectangle((0, 0), 10, 0.55, fc='#8d6e63')); ax.text(5, 0.28, 'surface (average 15 °C = 288 K)', ha='center', va='center', color='white', fontsize=8.5)
ax.add_patch(Rectangle((0, 0.55), 10, 3.2, fc='#e3f2fd', alpha=0.8)); ax.text(9.7, 3.4, 'atmosphere with\ngreenhouse gases', ha='right', fontsize=8.5, color=NAVY)
def arr(x, y0, y1, col, txt, tx=0.15, ha='left'):
    ax.annotate('', xy=(x, y1), xytext=(x, y0), arrowprops=dict(arrowstyle='-|>', color=col, lw=4, mutation_scale=18)); ax.text(x + tx, (y0 + y1) / 2, txt, color=col, fontsize=8.5, va='center', ha=ha)
ax.set_xlim(0, 12); ax.set_ylim(-0.7, 6.3)
arr(0.9, 5.4, 3.9, GOLD, '340 W/m²\nsunlight arriving'); arr(4.2, 3.9, 5.4, '#e67e22', '100 W/m²\nreflected by\nclouds, air, ice')
arr(10.6, 3.9, 5.4, RED, '240 W/m²\ninfrared\nto space', tx=-0.2, ha='right')
arr(5.4, 0.7, 3.0, RED, 'surface radiates\nabout 400 W/m²', tx=-0.2, ha='right'); arr(7.0, 3.0, 0.7, '#7b1fa2', 'greenhouse gases\nreturn about 340 W/m²')
ax.text(6, 5.95, 'In = out: 340 − 100 = 240 W/m²', ha='center', fontsize=9.5, weight='bold')
ax.text(6, -0.45, 'Without greenhouse gases the surface would average about −18 °C (255 K).', ha='center', fontsize=8, color=GREY)
save(fig, 'e04_energy_balance', 62, 'LEAD:1', 'Earth’s energy balance in round numbers (global and annual averages). The planet absorbs about 240 W/m² and must radiate the same to space. Greenhouse gases return part of the surface’s infrared radiation, so the surface is about 33 °C warmer than it would be otherwise. Adding greenhouse gas tips the balance by a few tenths of a watt per square meter at a time.', 'A diagram of the atmosphere and surface with arrows: 340 watts per square meter of sunlight arriving, 100 reflected, 240 infrared leaving to space, about 400 radiated by the surface and about 340 returned downward by greenhouse gases.')
# 37 binary entropy and channel capacity
fig, ax = new(8, 4.0); p = np.linspace(0.0001, 0.9999, 500); Hb = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
ax.plot(p, Hb, color=NAVY, lw=2.4, label='entropy of a biased coin, H(p)'); ax.plot(p, 1 - Hb, color=RED, lw=2.4, label='capacity of a noisy channel that flips bits with probability p')
ax.plot(0.5, 1, 'o', color=NAVY); ax.annotate('fair coin: 1 bit per toss', (0.5, 1), xytext=(0.58, 0.95), fontsize=8.5, color=NAVY); ax.annotate('at p = ½ the output is pure noise: capacity 0', (0.5, 0), xytext=(0.12, 0.08), fontsize=8.5, color=RED)
ax.set_xlabel('probability p'); ax.set_ylabel('bits'); ax.legend(frameon=False, fontsize=8, loc='upper center', bbox_to_anchor=(0.5, 0.9)); ax.set_title('Shannon’s two key curves')
save(fig, 'e05_shannon', 63, 'Information Theory', 'Left to right, the same function seen two ways. H(p) = −p log₂p − (1−p) log₂(1−p) is the information in a biased coin toss, largest when the outcome is most uncertain. Subtracting it from 1 gives the capacity of a channel that flips each bit with probability p; at p = ½ nothing gets through.', 'Two curves against probability from 0 to 1. The blue curve is a hump rising from 0 to 1 bit at probability one half and falling back. The red curve is its mirror image, falling from 1 to 0 at one half and rising again.')
# 38 Earth layers
fig, ax = new(6.4, 6.0); ax.set_aspect('equal'); ax.axis('off')
layers = [(6371, '#8d6e63', 'crust'), (6346, '#d84315', 'mantle'), (3480, '#ffb300', 'outer core (liquid iron)'), (1220, '#fff59d', 'inner core (solid iron)')]
for r, col, lab in layers: ax.add_patch(Circle((0, 0), r, fc=col, ec='white', lw=0.8))
ax.set_xlim(-8800, 8800); ax.set_ylim(-6800, 6800)
ax.text(0, 0, 'inner core\nsolid iron–nickel\n5400–6000 °C', ha='center', va='center', fontsize=7.5)
ax.text(0, 2350, 'outer core\nliquid iron: makes the magnetic field', ha='center', va='center', fontsize=8)
ax.text(0, 4650, 'mantle (2900 km thick):\nhot rock that flows over\nmillions of years', ha='center', va='center', fontsize=8.5, color='white')
ax.annotate('crust: 5–10 km under oceans,\n30–50 km under continents', xy=(4600, 4400), xytext=(5200, 5700), fontsize=8, arrowprops=dict(arrowstyle='->', color='#333'))
ax.set_title('The layers of the Earth, drawn to scale')
save(fig, 'e06_earth_layers', 56, 'The Structure of the Earth', 'The Earth’s interior drawn to scale. The crust is so thin it is a line at this size. Seismic waves reveal the layers: shear waves do not pass through the liquid outer core, which is how it was found.', 'A circular cross-section of the Earth with a thin crust, a thick mantle, a liquid outer core and a small solid inner core, each labelled.')
# 39 DNA double helix schematic
fig, ax = new(4.4, 5.6); y = np.linspace(0, 3 * 2 * np.pi, 400)
x1 = np.sin(y); x2 = np.sin(y + np.pi); z1 = np.cos(y); z2 = np.cos(y + np.pi)
for i in range(len(y) - 1):
    ax.plot(y[i:i + 2], x1[i:i + 2], color=NAVY, lw=2.2 + 1.3 * (z1[i] > 0), solid_capstyle='round'); ax.plot(y[i:i + 2], x2[i:i + 2], color=RED, lw=2.2 + 1.3 * (z2[i] > 0), solid_capstyle='round')
pairs = [('A', 'T', GREEN, GOLD), ('G', 'C', PURPLE, '#e67e22')]
for k, yy in enumerate(np.linspace(0.4, 3 * 2 * np.pi - 0.4, 20)):
    a_, b_, ca, cb = pairs[k % 2] if k % 3 else pairs[(k + 1) % 2]
    xa, xb = np.sin(yy), np.sin(yy + np.pi); mid = (xa + xb) / 2
    ax.plot([yy, yy], [xa, mid], color=ca, lw=3); ax.plot([yy, yy], [mid, xb], color=cb, lw=3)
ax.set_aspect('auto'); ax.axis('off'); ax.set_ylim(-1.5, 1.5); ax.set_title('DNA: two strands, base pairs as rungs')
ax.text(0.2, 1.35, 'A–T and G–C: each base pairs only with its partner', fontsize=7.8, color=GREY)
fig.set_size_inches(8, 3.4); fig.clf(); ax = fig.add_subplot(111)
y = np.linspace(0, 4 * 2 * np.pi, 800); x1 = np.sin(y); x2 = np.sin(y + np.pi); z1 = np.cos(y)
ax.plot(y, x1, color=NAVY, lw=2.4); ax.plot(y, x2, color=RED, lw=2.4)
for k, yy in enumerate(np.linspace(0.5, 4 * 2 * np.pi - 0.5, 34)):
    xa, xb = np.sin(yy), np.sin(yy + np.pi); mid = (xa + xb) / 2; ca, cb = ((GREEN, GOLD) if k % 3 else (PURPLE, '#e67e22'))
    ax.plot([yy, yy], [xa, mid], color=ca, lw=2.6); ax.plot([yy, yy], [mid, xb], color=cb, lw=2.6)
ax.axis('off'); ax.set_ylim(-1.7, 1.7); ax.set_title('DNA: two strands wound into a helix, joined by base pairs')
ax.text(0.2, 1.5, 'one full turn = about 10 base pairs = 3.4 nm', fontsize=8, color=GREY)
ax.annotate('', xy=(2 * np.pi, -1.4), xytext=(0, -1.4), arrowprops=dict(arrowstyle='<->', color=GREY)); ax.text(np.pi, -1.65, 'one turn', ha='center', fontsize=8, color=GREY)
save(fig, 'e07_dna', 39, 'The Double Helix', 'A schematic of the double helix. Two sugar–phosphate backbones wind around each other, joined by pairs of bases: A with T and G with C. About ten base pairs make one turn of 3.4 nanometres. The sequence along one strand fixes the sequence of the other, which is the copying rule.', 'Two intertwined wavy lines, one blue and one red, forming a double helix, with short colored rungs between them for the paired bases.')
# 40 carbon budget
fig, ax = new(8, 4.2); srcs = [('fossil fuels\nand cement', 9.6, '#555555'), ('land-use\nchange', 1.1, '#8d6e63')]
snk = [('stays in the\natmosphere', 5.2, RED), ('absorbed by\nthe ocean', 2.9, NAVY), ('absorbed by\nland plants', 3.2, GREEN)]
b = 0
for lab, v, col in srcs: ax.bar(0, v, bottom=b, color=col, width=0.6); ax.text(0, b + v / 2, '%s  %.1f' % (lab.replace('\n', ' '), v) if v > 2 else '%.1f' % v, ha='center', va='center', color='white', fontsize=8.5); b += v
b = 0
for lab, v, col in snk: ax.bar(1.2, v, bottom=b, color=col, width=0.6); ax.text(1.2, b + v / 2, '%s  %.1f' % (lab.replace('\n', ' '), v), ha='center', va='center', color='white', fontsize=8.5); b += v
ax.set_xticks([0, 1.2]); ax.set_xticklabels(['where it comes from', 'where it goes']); ax.set_ylabel('billion tonnes of carbon per year'); ax.set_xlim(-0.6, 1.8); ax.spines['bottom'].set_visible(False); ax.tick_params(bottom=False)
ax.set_title('The yearly carbon account, around 2020–2023 (approximate)')
save(fig, 'e08_carbon_budget', 62, 'LEAD:3', 'Where the carbon dioxide we emit goes, in round numbers for the early 2020s. Human sources of about 10.7 billion tonnes of carbon a year are matched by sinks: about half stays in the air, raising the concentration, and the rest is absorbed by the ocean and by land plants. The small mismatch is the budget imbalance. Source: Global Carbon Budget estimates, rounded.', 'Two stacked bars. The left bar, about 10.7 billion tonnes of carbon per year, is mostly fossil fuel emissions with a small land-use part. The right bar splits about 5.2 staying in the atmosphere, 2.9 absorbed by the ocean and 3.2 by land plants.')
