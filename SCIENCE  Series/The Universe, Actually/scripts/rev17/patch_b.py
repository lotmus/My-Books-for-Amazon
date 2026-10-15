import re
s = open('figs_b.py', encoding='utf-8').read()
a = s.index('# 14 periodic table layout'); b = s.index('# 15 band diagram'); c = s.index('# 16 catalysis energy profile')
periodic = r'''# 14 periodic table layout
SYM = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og'.split()
fig, ax = new(8.4, 5.0); ax.set_xlim(-0.2, 18.2); ax.set_ylim(10.3, -1.1); ax.axis('off')
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
'''
bands = r'''# 15 band diagram
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
'''
cat = r'''# 16 catalysis energy profile
fig, ax = new(8, 4.2); x = np.linspace(0, 10, 600)
sig = 1 / (1 + np.exp(-(x - 5.2) * 1.3)); Er, Ep = 3.0, 1.6
base = Er + (Ep - Er) * sig
unc = base + 3.0 * np.exp(-((x - 4.6) / 0.9) ** 2); cata = base + 1.5 * np.exp(-((x - 4.6) / 0.9) ** 2)
ax.plot(x, unc, color=NAVY, lw=2.2, label='uncatalyzed'); ax.plot(x, cata, color=GREEN, lw=2.2, label='with a catalyst')
ax.annotate('', xy=(4.6, 3.0 + 1.5 + 0.12), xytext=(4.6, 3.0 + 3.0 - 0.1), arrowprops=dict(arrowstyle='<->', color=RED)); ax.text(4.85, 5.35, 'barrier lowered by the catalyst', color=RED, fontsize=8)
ax.text(0.3, Er + 0.25, 'reactants', fontsize=8.5); ax.text(8.2, Ep + 0.25, 'products', fontsize=8.5); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('progress of the reaction →'); ax.set_ylabel('energy'); ax.set_ylim(0.8, 6.6)
ax.legend(frameon=False, loc='upper right', fontsize=8); ax.set_title('A catalyst lowers the barrier, not the destination')
save(fig, 'b07_catalysis', 16, 'Surface Chemistry and Catalysis', 'A catalyst offers a lower-energy route over the barrier. The starting and finishing energies, and therefore the equilibrium, are unchanged; the reaction simply gets there faster.', 'Two energy profiles from reactants to products. The blue uncatalyzed curve climbs over a high barrier. The green catalyzed curve climbs a lower barrier. Both start and finish at the same energies.')
'''
s = s[:a] + periodic + bands + cat
s = s.replace("ax.quiver(0, 0, 0, *p, color=RED, lw=2.5, arrow_length_ratio=0.12); ax.text(p[0] * 1.2, p[1] * 1.2, p[2] * 1.12, 'a general qubit state', color=RED, fontsize=8.5)", "ax.quiver(0, 0, 0, *p, color=RED, lw=2.5, arrow_length_ratio=0.12); ax.text2D(0.02, 0.06, 'red arrow: a general superposition', color=RED, fontsize=8.5, transform=ax.transAxes)")
open('figs_b.py', 'w', encoding='utf-8').write(s)
