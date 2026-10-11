from figutil import *
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch, Circle, Wedge
# 10 Bell / CHSH correlations
fig, ax = new(8, 4.2); a = np.linspace(0, 180, 361)
ax.plot(a, -np.cos(np.radians(a)), color=NAVY, lw=2.2, label='quantum prediction: −cos θ')
cl = -(1 - 2 * a / 180); ax.plot(a, cl, color=RED, lw=2, ls='--', label='a typical local hidden-variable model: a straight line')
ax.axhline(0, color=GREY, lw=0.5); ax.set_xlabel('angle between the two detector settings (degrees)'); ax.set_ylabel('correlation of the two results'); ax.legend(frameon=False, fontsize=8, loc='upper left')
ax.set_xticks([0, 45, 90, 135, 180]); ax.set_title('Spin-singlet correlations: curve against straight line')
save(fig, 'b01_bell', 7, 'How the Inequality Works', 'The quantum correlation for two entangled spins is a cosine, which bows beyond the straight line that local hidden-variable models of this kind can give. At the best angles the combination used in the CHSH inequality reaches 2√2 ≈ 2.83, above the local limit of 2.', 'Correlation against the angle between detector settings from 0 to 180 degrees. The blue quantum curve is minus the cosine of the angle. The red dashed local-model line is straight. The two agree at 0, 90 and 180 degrees and differ in between, which is where the experiments measure.')
# 11 Bloch sphere
fig = plt.figure(figsize=(6.4, 5.2), dpi=100); ax = fig.add_subplot(111, projection='3d')
u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 24))
ax.plot_wireframe(np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v), color='#bbbbbb', lw=0.35)
ph = np.linspace(0, 2 * np.pi, 200); ax.plot(np.cos(ph), np.sin(ph), 0, color=GREY, lw=0.8)
for vec, lab in [((0, 0, 1.28), '|0⟩'), ((0, 0, -1.3), '|1⟩'), ((1.3, 0, 0), '|+⟩'), ((-1.3, 0, 0), '|−⟩')]: ax.text(*vec, lab, ha='center', va='center', fontsize=11)
th, ph0 = np.radians(55), np.radians(40); p = (np.sin(th) * np.cos(ph0), np.sin(th) * np.sin(ph0), np.cos(th))
ax.quiver(0, 0, 0, *p, color=RED, lw=2.5, arrow_length_ratio=0.12); ax.text2D(0.02, 0.06, 'red arrow: a general superposition', color=RED, fontsize=8.5, transform=ax.transAxes)
ax.plot([0, 0], [0, 0], [-1, 1], color=NAVY, lw=1.2); ax.set_axis_off(); ax.set_box_aspect((1, 1, 1)); ax.view_init(22, 28)
ax.set_title('The Bloch sphere: every state of one qubit is a point')
save(fig, 'b02_bloch', 8, 'Quantum Computing', 'A single qubit’s state is a point on a sphere. The poles are the ordinary bit values 0 and 1; every other point is a superposition, with the angle around the equator giving the relative phase. Gates are rotations of the sphere.', 'A sphere with poles labelled zero and one and two equatorial points labelled plus and minus. A red arrow from the centre points to a general position on the surface, standing for an arbitrary superposition.')
# 12 binding energy per nucleon (semi-empirical mass formula, stable Z)
def BE(A, Z):
    aV, aS, aC, aA, aP = 15.75, 17.8, 0.711, 23.7, 11.18; N = A - Z
    d = aP / A ** 0.5 if (Z % 2 == 0 and N % 2 == 0) else (-aP / A ** 0.5 if (Z % 2 == 1 and N % 2 == 1) else 0)
    return aV * A - aS * A ** (2 / 3) - aC * Z * (Z - 1) / A ** (1 / 3) - aA * (A - 2 * Z) ** 2 / A + d
fig, ax = new(8, 4.4); A = np.arange(12, 261); Bn = []
for a_ in A:
    zbest = max(range(1, a_), key=lambda z: BE(a_, z)); Bn.append(BE(a_, zbest) / a_)
ax.plot(A, Bn, color=NAVY, lw=1.6, label='semi-empirical formula')
pts = {'He-4': (4, 7.07), 'C-12': (12, 7.68), 'O-16': (16, 7.98), 'Fe-56': (56, 8.79), 'Ni-62': (62, 8.79), 'U-235': (235, 7.59)}
for k, (x, y) in pts.items(): ax.plot(x, y, 'o', color=RED, ms=5); ax.annotate(k, (x, y), xytext=(x + 4, y - 0.55 if k != 'Fe-56' else y + 0.2), fontsize=8, color=RED)
ax.set_xlabel('mass number A (protons + neutrons)'); ax.set_ylabel('binding energy per nucleon (MeV)'); ax.set_ylim(0, 9.6); ax.set_xlim(0, 260)
ax.annotate('fusion releases energy\nclimbing this side', xy=(25, 8), xytext=(35, 3.8), arrowprops=dict(arrowstyle='->', color=GREY), fontsize=8)
ax.annotate('fission releases energy\nclimbing this side', xy=(200, 7.8), xytext=(150, 3.8), arrowprops=dict(arrowstyle='->', color=GREY), fontsize=8)
ax.set_title('Iron and nickel sit at the top of the nuclear hill'); ax.legend(frameon=False, loc='lower right', fontsize=8)
save(fig, 'b03_binding', 13, 'Nuclear Binding Energy', 'Binding energy per nucleon against mass number. The curve is computed from the liquid-drop (semi-empirical) mass formula; red points are measured values for selected nuclei. Nuclei near iron-56 and nickel-62 are the most tightly bound, so fusion of light nuclei and fission of heavy ones both release energy.', 'A curve of binding energy per nucleon rising steeply from helium-4 at about 7 million electronvolts to a peak of about 8.8 near iron and nickel at mass number 56 to 62, then declining slowly to about 7.6 at uranium-235. Annotations mark fusion on the rising side and fission on the falling side.')
# 13 neutrino oscillation
fig, ax = new(8, 4); LE = np.linspace(0, 40000, 2000)  # km/GeV
dm2 = 2.5e-3; th = np.radians(45)
P = 1 - np.sin(2 * th) ** 2 * np.sin(1.267 * dm2 * LE) ** 2
ax.plot(LE / 1000, P, color=NAVY, lw=2, label='muon neutrino stays a muon neutrino'); ax.plot(LE / 1000, 1 - P, color=RED, lw=2, label='it has become a tau neutrino')
ax.set_xlabel('distance travelled ÷ energy  (thousand km per GeV)'); ax.set_ylabel('probability'); ax.legend(frameon=False, fontsize=8, loc='center right'); ax.set_ylim(-0.02, 1.08)
ax.set_title('Neutrino oscillation, two-flavor approximation')
save(fig, 'b04_neutrino', 14, 'Neutrino Mass and Mixing', 'A neutrino produced as one flavor is a mixture of mass states that drift out of step as it travels, so it can be detected as another flavor. Computed from the two-flavor formula with the atmospheric mass splitting 2.5 × 10⁻³ eV² and maximal mixing.', 'Two curves of probability against distance divided by energy. The blue curve, the chance a muon neutrino stays a muon neutrino, falls from one to zero and back repeatedly. The red curve, the chance it has turned into a tau neutrino, rises and falls in the opposite pattern.')
# 14 periodic table layout
SYM = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og'.split()
fig, ax = new(8.0, 4.8); ax.set_xlim(-0.2, 18.2); ax.set_ylim(10.3, -1.1); ax.axis('off')
cols = {'s': '#f4b183', 'p': '#a9d18e', 'd': '#9dc3e6', 'f': '#d5a6e6'}
pos = {}
def put(z, row, col): pos[z] = (row, col)
put(1, 1, 1); put(2, 1, 18)
for z in range(3, 5): put(z, 2, z - 2)
for z in range(5, 11): put(z, 2, z + 8)
for z in range(11, 13): put(z, 3, z - 10)
for z in range(13, 19): put(z, 3, z)
for z in range(19, 37): put(z, 4, z - 18)
for z in range(37, 55): put(z, 5, z - 36)
put(55, 6, 1); put(56, 6, 2); put(57, 6, 3)
for z in range(72, 87): put(z, 6, z - 68)
put(87, 7, 1); put(88, 7, 2); put(89, 7, 3)
for z in range(104, 119): put(z, 7, z - 100)
for z in range(58, 72): put(z, 9, z - 54)
for z in range(90, 104): put(z, 10, z - 86)
for z, (r, cc) in pos.items():
    if r >= 9: k = 'f'
    elif cc in (1, 2): k = 's'
    elif cc >= 13: k = 'p'
    else: k = 'd'
    ax.add_patch(Rectangle((cc - 1, r - 1), 0.95, 0.95, fc=cols[k], ec='white', lw=0.8))
    ax.text(cc - 1 + 0.475, r - 1 + 0.5, SYM[z - 1], ha='center', va='center', fontsize=6.6)
ax.text(-0.15, 5.45 + 0, '', fontsize=6)
for r, lab in [(6, '57–71'), (7, '89–103')]: pass
ax.text(2.9, 8.45, 'lanthanides →', fontsize=7, color=GREY, ha='right', va='center'); ax.text(2.9, 9.45, 'actinides →', fontsize=7, color=GREY, ha='right', va='center')
import matplotlib.patches as mp
ax.legend(handles=[mp.Patch(color=cols[k], label=l) for k, l in [('s', 's subshell filling'), ('p', 'p subshell'), ('d', 'd subshell: transition metals'), ('f', 'f subshell')]], loc='lower center', ncol=4, frameon=False, fontsize=7.5, bbox_to_anchor=(0.5, -0.03))
ax.set_title('The periodic table, colored by the subshell being filled')
save(fig, 'b05_periodic', 15, 'The Periodic Table', 'The shape of the periodic table is the shape of the electron shells: two columns where an s subshell fills, six for p, ten for d and fourteen for f. Rows are periods; columns are groups with similar chemistry. (Helium, with a filled 1s shell, sits with the noble gases.)', 'A block layout of the 118 elements with symbols, in seven rows and eighteen columns with two extra rows of fourteen below. Elements are colored by the type of subshell being filled: s on the left, p on the right, d across the middle and f in the lower two rows.')
# 15 band diagram
fig, axs = plt.subplots(1, 3, figsize=(8, 3.9), dpi=100, sharey=True)
for ax, title, gap in zip(axs, ['Metal', 'Semiconductor', 'Insulator'], [0, 1.1, 5]):
    ax.set_xlim(0, 1.5); ax.set_ylim(0, 12); ax.set_xticks([]); ax.spines['bottom'].set_visible(False)
    if title == 'Metal':
        ax.add_patch(Rectangle((0.2, 1.5), 0.8, 3.5, fc=NAVY, alpha=0.85)); ax.add_patch(Rectangle((0.2, 5.0), 0.8, 3.0, fc='#9dc3e6', alpha=0.9)); ax.text(0.6, 5.0, 'one band, partly\nfilled: electrons\nmove freely', ha='center', va='center', fontsize=7.5, color='black')
    else:
        ax.add_patch(Rectangle((0.2, 1.0), 0.8, 3.0, fc=NAVY, alpha=0.85)); ax.add_patch(Rectangle((0.2, 4.0 + gap), 0.8, 2.5, fc='#9dc3e6', alpha=0.9))
        ax.text(0.6, 2.5, 'valence band\n(full)', ha='center', va='center', fontsize=7.5, color='white'); ax.text(0.6, 5.25 + gap, 'conduction band\n(empty)', ha='center', va='center', fontsize=7.5)
        ax.annotate('', xy=(1.1, 4.0 + gap), xytext=(1.1, 4.0), arrowprops=dict(arrowstyle='<->', color=RED)); ax.text(1.15, 4.0 + gap / 2, 'gap\n%s eV' % ('1.1' if title == 'Semiconductor' else '~9'), color=RED, fontsize=7.5, va='center')
    ax.set_title(title, fontsize=10)
axs[0].set_ylabel('electron energy')
fig.suptitle('Whether a solid conducts is decided by its energy bands', fontweight='bold', fontsize=10.5)
save(fig, 'b06_bands', 17, 'Semiconductors', 'Energy bands in solids. A metal has a partly filled band. A semiconductor has a full band separated from an empty one by a small gap (about 1.1 eV in silicon) that heat, light or doping can bridge. An insulator’s gap is too wide to cross.', 'Three panels of energy bands. In the metal, one band is partly filled. In the semiconductor, a full valence band sits below an empty conduction band across a gap of about 1.1 electronvolts. In the insulator the gap is much wider, about 9 electronvolts.')
# 16 catalysis energy profile
fig, ax = new(8, 4.2); x = np.linspace(0, 10, 600)
sig = 1 / (1 + np.exp(-(x - 5.2) * 1.3)); Er, Ep = 3.0, 1.6
base = Er + (Ep - Er) * sig
unc = base + 3.0 * np.exp(-((x - 4.6) / 0.9) ** 2); cata = base + 1.5 * np.exp(-((x - 4.6) / 0.9) ** 2)
ax.plot(x, unc, color=NAVY, lw=2.2, label='uncatalyzed'); ax.plot(x, cata, color=GREEN, lw=2.2, label='with a catalyst')
ax.annotate('', xy=(4.6, 3.0 + 1.5 + 0.12), xytext=(4.6, 3.0 + 3.0 - 0.1), arrowprops=dict(arrowstyle='<->', color=RED)); ax.text(4.85, 5.35, 'barrier lowered by the catalyst', color=RED, fontsize=8)
ax.text(0.3, Er + 0.25, 'reactants', fontsize=8.5); ax.text(8.2, Ep + 0.25, 'products', fontsize=8.5); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('progress of the reaction →'); ax.set_ylabel('energy'); ax.set_ylim(0.8, 6.6)
ax.legend(frameon=False, loc='upper right', fontsize=8); ax.set_title('A catalyst lowers the barrier, not the destination')
save(fig, 'b07_catalysis', 16, 'Surface Chemistry and Catalysis', 'A catalyst offers a lower-energy route over the barrier. The starting and finishing energies, and therefore the equilibrium, are unchanged; the reaction simply gets there faster.', 'Two energy profiles from reactants to products. The blue uncatalyzed curve climbs over a high barrier. The green catalyzed curve climbs a lower barrier. Both start and finish at the same energies.')
