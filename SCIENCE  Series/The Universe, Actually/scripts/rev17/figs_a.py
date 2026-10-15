from figutil import *
# 1 projectile with and without drag
fig, ax = new()
g = 9.81; v0 = 30; th = np.radians(45)
t = np.linspace(0, 2 * v0 * np.sin(th) / g, 200)
ax.plot(v0 * np.cos(th) * t, v0 * np.sin(th) * t - 0.5 * g * t * t, color=NAVY, lw=2, label='no air: a parabola')
def f(t, s, k=0.012):
    x, y, vx, vy = s; v = np.hypot(vx, vy); return [vx, vy, -k * v * vx, -g - k * v * vy]
tt = np.arange(0, 5, 0.005); S = rk4(f, [0, 0, v0 * np.cos(th), v0 * np.sin(th)], tt)
i = np.argmax(S[:, 1] < 0) if (S[1:, 1] < 0).any() else len(tt); i = np.where(S[1:, 1] < 0)[0][0] + 1
ax.plot(S[:i, 0], S[:i, 1], color=RED, lw=2, label='with air drag: shorter, steeper on the way down')
ax.set_xlabel('distance (m)'); ax.set_ylabel('height (m)'); ax.set_aspect('equal'); ax.legend(frameon=False, loc='upper center', bbox_to_anchor=(0.5, -0.22), ncol=1)
ax.set_title('A ball thrown at 45° and 30 m/s')
save(fig, 'a01_projectile', 1, 'Motion and Newton’s Laws', 'Newton’s second law at work. Without air a thrown ball follows a parabola; with air resistance the same throw falls short and descends more steeply.', 'Two curves of height against distance for a ball thrown at 45 degrees and 30 metres per second. The blue curve, without air, is a symmetric parabola about 92 metres long. The red curve, with moderate air drag, is lower, shorter and steeper on the way down.')
# 2 damped oscillator
fig, ax = new(); t = np.linspace(0, 12, 600); w0 = 2 * np.pi * 0.5
for z, col, l in [(0.05, NAVY, 'light damping: rings down'), (1.0, GREEN, 'critical damping: fastest return, no overshoot'), (2.5, RED, 'heavy damping: slow creep back')]:
    if z < 1: wd = w0 * np.sqrt(1 - z * z); x = np.exp(-z * w0 * t) * (np.cos(wd * t) + z * w0 / wd * np.sin(wd * t))
    elif z == 1: x = (1 + w0 * t) * np.exp(-w0 * t)
    else:
        s = np.sqrt(z * z - 1); a = w0 * (-z + s); b = w0 * (-z - s); x = (b * np.exp(a * t) - a * np.exp(b * t)) / (b - a)
    ax.plot(t, x, color=col, lw=2, label=l)
ax.axhline(0, color=GREY, lw=0.6); ax.set_xlabel('time (s)'); ax.set_ylabel('displacement (relative)'); ax.legend(frameon=False, fontsize=8)
ax.set_title('A released oscillator under three amounts of friction')
save(fig, 'a02_damping', 1, 'Oscillations', 'The three regimes of damped oscillation. Shock absorbers and door closers are tuned to the green curve.', 'Three curves of displacement against time for an oscillator released from rest. With light damping the blue curve oscillates with shrinking amplitude. With critical damping the green curve returns to zero fastest without crossing it. With heavy damping the red curve returns slowly.')
# 3 Maxwell-Boltzmann
fig, ax = new(); v = np.linspace(0, 2500, 600); m = 28.0 * 1.6605e-27
for T, col in [(100, NAVY), (300, GREEN), (1000, RED)]:
    f_ = 4 * np.pi * (m / (2 * np.pi * kB * T)) ** 1.5 * v * v * np.exp(-m * v * v / (2 * kB * T)); ax.plot(v, f_ * 1000, color=col, lw=2, label='%d K' % T)
ax.set_xlabel('molecular speed (m/s)'); ax.set_ylabel('share of molecules per km/s'); ax.legend(frameon=False)
ax.set_title('Nitrogen molecules: speeds spread out as the gas warms')
save(fig, 'a03_maxwell', 2, 'Temperature, Gas Laws and Phases', 'Temperature is a statement about a distribution. Hotter gas has a lower, broader hump of molecular speeds and a long tail of very fast molecules. At 300 K the most common nitrogen speed is about 420 m/s.', 'Three curves of the distribution of speeds of nitrogen molecules at 100, 300 and 1000 kelvin. The curve for 100 kelvin is tall and narrow near 230 metres per second. The curve for 1000 kelvin is low and broad, peaking near 770 metres per second.')
# 4 logistic bifurcation
fig, ax = new(8, 4.6); rs = np.linspace(2.9, 4.0, 1100); X = []; R = []
for r in rs:
    x = 0.5
    for _ in range(300): x = r * x * (1 - x)
    for _ in range(60): x = r * x * (1 - x); X.append(x); R.append(r)
ax.plot(R, X, ',', color=NAVY, alpha=0.6)
ax.set_xlabel('growth parameter r'); ax.set_ylabel('long-run values of x'); ax.set_title('The logistic map: from steady, to cycles, to chaos')
for r, s in [(3.0, 'period 2'), (3.449, 'period 4'), (3.57, 'chaos begins')]: ax.axvline(r, color=RED, lw=0.7, ls=':'); ax.text(r + 0.01, 0.03, s, fontsize=7.5, color=RED, rotation=90, va='bottom')
save(fig, 'a04_logistic', 2, 'Chaos', 'The logistic map, x → r x (1 − x), computed for 1,100 values of r. Each vertical slice shows where the sequence settles. Doubling of the period leads to chaos near r = 3.57, with a window of order near r = 3.83.', 'A bifurcation diagram. For r below 3 the long-run value is a single point. Between 3 and about 3.45 it splits into two, then four, eight and so on, until at about 3.57 the points fill bands and the behaviour is chaotic. A narrow window of order appears near 3.83.')
# 5 Lorenz
fig = plt.figure(figsize=(8, 4.2), dpi=100)
def lor(t, s, sg=10, rho=28, b=8 / 3): x, y, z = s; return [sg * (y - x), x * (rho - z) - y, x * y - b * z]
tt = np.linspace(0, 50, 25001)
s1 = rk4(lor, [1, 1, 1], tt); s2 = rk4(lor, [1 + 1e-6, 1, 1], tt)
ax = fig.add_subplot(1, 2, 1); ax.plot(s1[:, 0], s1[:, 2], color=NAVY, lw=0.4); ax.set_xlabel('x'); ax.set_ylabel('z'); ax.set_title('The Lorenz attractor')
ax2 = fig.add_subplot(1, 2, 2); ax2.plot(tt, s1[:, 0], color=NAVY, lw=1, label='start x = 1'); ax2.plot(tt, s2[:, 0], color=RED, lw=1, label='start x = 1.000001'); ax2.set_xlim(0, 50); ax2.set_xlabel('time'); ax2.set_ylabel('x'); ax2.legend(frameon=False, fontsize=7.5, loc='upper left'); ax2.set_title('A millionth apart, then unrelated')
save(fig, 'a05_lorenz', 2, 'Lyapunov Exponents and Predictability', 'Left: the path of Lorenz’s convection model, a strange attractor. Right: two runs that start one part in a million apart agree for a while, then diverge completely. That is the practical meaning of a positive Lyapunov exponent.', 'Two panels. Left, a butterfly-shaped curve of z against x with two lobes. Right, two traces of x against time, one blue and one red, that overlap closely at first and then drift apart into unrelated oscillations.')
# 6 double slit
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.8), dpi=100, gridspec_kw={'width_ratios': [1.6, 1]})
th = np.linspace(-0.004, 0.004, 4000); lam = 600e-9; d = 0.2e-3; a = 0.05e-3
beta = np.pi * a * np.sin(th) / lam; alpha = np.pi * d * np.sin(th) / lam
I = np.cos(alpha) ** 2 * (np.sinc(beta / np.pi)) ** 2
a1.plot(th * 2000, I, color=NAVY, lw=1.5); a1.fill_between(th * 2000, 0, I, color=NAVY, alpha=0.15); a1.set_xlabel('position on a screen 2 m away (mm)'); a1.set_ylabel('relative brightness'); a1.set_title('Two slits, one wavelength')
rng = np.random.default_rng(3); xs = rng.choice(th, 1500, p=I / I.sum())
a2.hist(xs * 2000, bins=90, color=NAVY, alpha=0.85); a2.set_title('1,500 single detections'); a2.set_xlabel('position (mm)'); a2.set_yticks([])
save(fig, 'a06_double_slit', 3, 'Optics and Quantum Mechanics', 'Interference from two slits 0.2 mm apart with light of wavelength 600 nm, on a screen 2 m away. Right: the same pattern builds up when particles arrive one at a time, shown as a simulated tally of detections.', 'Left, a curve of brightness against position with evenly spaced peaks about 6 millimetres apart under a broad envelope. Right, a histogram of 1,500 simulated single-particle detections that follows the same banded pattern.')
# 7 dipole field
fig, ax = new(7.2, 4.4); x = np.linspace(-3, 3, 300); y = np.linspace(-2, 2, 220); X, Y = np.meshgrid(x, y)
def E(q, x0):
    dx, dy = X - x0, Y; r = np.hypot(dx, dy) + 1e-9; return q * dx / r ** 3, q * dy / r ** 3
e1 = E(1, -1); e2 = E(-1, 1); Ex = e1[0] + e2[0]; Ey = e1[1] + e2[1]
ax.streamplot(X, Y, Ex, Ey, color=NAVY, density=1.6, linewidth=0.8, arrowsize=0.9)
ax.plot(-1, 0, 'o', color=RED, ms=14); ax.plot(1, 0, 'o', color=NAVY, ms=14); ax.text(-1, 0, '+', color='white', ha='center', va='center', fontsize=12, weight='bold'); ax.text(1, 0, '−', color='white', ha='center', va='center', fontsize=12, weight='bold')
ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-3, 3); ax.set_ylim(-2, 2); ax.set_title('Electric field of a positive and a negative charge')
save(fig, 'a07_dipole', 4, 'The Electromagnetic Field', 'Field lines leave positive charge and end on negative charge. The lines are densest where the field is strongest, near the charges.', 'Curved field lines running from a positive charge on the left to a negative charge on the right, crowded near each charge and spreading out in between and around them.')
# 8 blackbody
fig, ax = new(); lam = np.linspace(50e-9, 3000e-9, 1500)
for T, col in [(5800, GOLD), (4500, RED), (3500, '#8d3b2a')]:
    B = 2 * h * c * c / lam ** 5 / (np.exp(h * c / (lam * kB * T)) - 1); ax.plot(lam * 1e9, B / 1e13, color=col, lw=2, label='%d K' % T)
T = 5800; rj = 2 * c * kB * T / lam ** 4; ax.plot(lam * 1e9, rj / 1e13, color=NAVY, lw=1.3, ls='--', label='classical prediction (5800 K)')
ax.set_ylim(0, 8); ax.set_xlim(0, 3000); ax.set_xlabel('wavelength (nm)'); ax.set_ylabel('brightness (relative)'); ax.legend(frameon=False, fontsize=8)
ax.axvspan(400, 700, color='#fff6c0', alpha=0.5, zorder=0); ax.text(550, 7.3, 'visible', ha='center', fontsize=8)
ax.set_title('Planck’s law and the failure of the classical curve')
save(fig, 'a08_blackbody', 5, 'LEAD:1', 'Thermal radiation computed from Planck’s law (solid) against the classical prediction for 5800 K (dashed), which rises without limit toward short wavelengths. Planck’s assumption that energy comes in quanta removes the divergence and fits the observed curve.', 'Three solid curves of brightness against wavelength for temperatures of 3500, 4500 and 5800 kelvin, each with a single peak. The hotter curves peak at shorter wavelengths. A dashed classical curve for 5800 kelvin climbs steeply at short wavelengths without limit.')
# 9 hydrogen levels
fig, ax = new(8, 4.6); En = lambda n: -13.6 / n ** 2
for n in range(1, 8): ax.hlines(En(n), 0.2, 3.8, color=NAVY, lw=1.6); ax.text(3.9, En(n), ('n = %d' % n) if n < 4 else '', va='center', fontsize=8)
ax.hlines(0, 0.2, 3.8, color=GREY, lw=0.8, ls=':'); ax.text(3.9, 0, 'ionized (n → ∞)', va='center', fontsize=8); ax.text(3.9, -0.65, 'n = 4, 5, 6 …', va='center', fontsize=7.5, color=GREY)
cols = {'Lyman': PURPLE, 'Balmer': GREEN, 'Paschen': RED}; xs = {'Lyman': 0.7, 'Balmer': 1.7, 'Paschen': 2.7}
for ser, nl in [('Lyman', 1), ('Balmer', 2), ('Paschen', 3)]:
    for k, nu in enumerate(range(nl + 1, nl + 4)):
        ax.annotate('', xy=(xs[ser] + 0.15 * k, En(nl)), xytext=(xs[ser] + 0.15 * k, En(nu)), arrowprops=dict(arrowstyle='->', color=cols[ser], lw=1.3))
    ax.text(xs[ser] + 0.15, En(nl) - 1.3 if nl > 1 else -15.3, ser + ' series', color=cols[ser], ha='center', fontsize=8)
ax.set_ylim(-16, 1); ax.set_xlim(0, 4.6); ax.set_xticks([]); ax.set_ylabel('energy (eV)'); ax.set_title('Hydrogen’s energy levels, E = −13.6 eV / n²'); ax.spines['bottom'].set_visible(False)
save(fig, 'a09_hydrogen', 15, 'Quantum Mechanics of the Atom', 'The energy levels of hydrogen and the three best-known series of spectral lines. Each arrow is one photon, with energy equal to the drop between levels. The Balmer series, ending on n = 2, is the visible one: 656, 486 and 434 nm.', 'A ladder of horizontal lines for hydrogen’s energy levels from n equals 1 at minus 13.6 electronvolts up to zero at ionization. Downward arrows group into three series ending on levels 1, 2 and 3, named Lyman, Balmer and Paschen.')
