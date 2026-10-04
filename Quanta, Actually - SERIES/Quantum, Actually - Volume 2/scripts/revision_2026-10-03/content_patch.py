# One-off content edits adapted from the Unused-from-merge notes and The Quantum Conversation (read-only source).
import sys, os
S = sys.argv[1]
def sub(fn, old, new, count=1):
    p = os.path.join(S, fn); s = open(p, encoding='utf-8').read()
    if new.strip() and new in s: print('already', fn); return
    assert old in s, (fn, old[:60]); s = s.replace(old, new, count)
    open(p, 'w', encoding='utf-8').write(s); print('ok', fn)

# P4: near-cancellation done by arithmetic
sub('prologue04.txt', "now by arithmetic.\n", """now by arithmetic.

**Near-cancellation.** Take two arrows of length 1, one pointing north, (0, 1), and one pointing south, (0, −1). They add to (0, 0): two routes, each of which looks perfectly possible, and a detector that never clicks. Now tip the south arrow 10° towards the east. It becomes (0.174, −0.985), and the sum is (0.174, 0.015), of length about 0.17. Neither arrow changed its length. Only the angle between them changed, and a dark spot now gets a faint signal, about 0.03 of what one route alone would give. This is the arithmetic of every interference pattern: outcomes are decided by adding arrows, not by adding probabilities.
""")

# P3: massive particles and stationary action
sub('prologue03.txt', "That is why a straw in a glass of water looks bent.\n", """That is why a straw in a glass of water looks bent.

The same cancellation works for things with mass. For a thrown ball, the quantity whose arrow turns along each path is not the travel time but a quantity called the action, and the path that survives is the one whose action does not change for nearby paths: the path Newton would have predicted. Least time is the special case that applies to light. In neither case does anything decide in advance. Every path contributes; only after the cancellations does one path stand out, as if it had been chosen on purpose. Lessons 5 and 80 make this exact.
""")

# P6: the vacuum is not empty (Casimir), after the loop paragraph
sub('prologue06.txt', "But they carry the theory's two most striking results: its precision and its infinities.\n", """But they carry the theory's two most striking results: its precision and its infinities.

Loops also change what "empty space" means. Even with no electron present, the theory has arrows for pairs that appear and vanish again, and for the electromagnetic field's restless lowest state. One measurable consequence: two uncharged metal plates placed a fraction of a micrometre apart in a vacuum attract each other slightly. The plates restrict which field patterns fit between them, and the energy changes with the gap. This is the Casimir effect, measured accurately since the late 1990s. (It can also be described as a sum of tiny attractions between the atoms of the two plates; both descriptions give the same force.)
""")

# Mead section 2: rewritten, more accessible, corrected phase formula
old2_start = "An electron's wave function has a phase. Transporting the electron around a loop"
p = os.path.join(S, 'interlude_mead.txt'); s = open(p, encoding='utf-8').read()
if old2_start in s:
    a = s.index(old2_start); b = s.index("\n", a)
    s = s[:a] + """Fields first, potentials later: that is the order in which almost everyone learns electromagnetism, and for classical circuits and waves it is a defensible order. It is also partly an accident of history. Maxwell gave the potentials a central place; Heaviside, compressing Maxwell's theory into today's four equations (Prologue 7), removed them wherever he could, because fields could be measured directly and potentials could not. That was a choice, not a law of nature, and quantum mechanics is where the choice stops being free.

The reason is phase. An electron's amplitude is an arrow (Prologues 1–4), and as the electron moves, the rate at which its arrow turns depends on the potentials along its path: by an extra (e/ℏ)A·dl for each small step dl. The magnetic field does not enter this rule directly. The decisive experiment is the Aharonov–Bohm effect. Split an electron beam so that the two halves pass on either side of a thin, shielded solenoid. The magnetic field is confined inside the solenoid and is zero everywhere the electrons go. Classically there is no force and nothing to notice. Yet when the halves recombine, the fringes shift as the flux Φ inside the solenoid is changed. The two routes differ in phase by (e/ℏ)∮A·dl = eΦ/ℏ. The effect was predicted in 1959 and has been observed repeatedly, most cleanly by Tonomura's group in the 1980s with a tiny magnetic ring sealed inside a superconducting shield so that no field could leak out. It is unintelligible if E and B are the only electromagnetic quantities that act on matter, and natural if A is the quantity that sets phase. Lesson 12's wave function and Lesson 8's A were waiting to be multiplied.

A useful picture: a clock in London and a clock in Tokyo can both read 3:00, and you still cannot say whether those moments match until you know the offset between the time zones. The offset belongs to neither clock; it is the rule for comparing them. The potential is that rule for phase. In geometry such a rule is called a **connection**, and Lesson 39 shows that demanding a free choice of phase convention at every point forces exactly this object into the theory.""" + s[b:]
    s = s.replace("""Does Aharonov–Bohm mean Maxwell's B=∇×A is wrong? No. ∇×A is still B, and Faraday's law still holds. It means that two potentials differing by a gradient can be physically distinguished by a loop that cannot be contracted without crossing flux, i.e. that A is not a disposable convenience.""",
    """Does Aharonov–Bohm mean Maxwell's B=∇×A is wrong? No. ∇×A is still B, and Faraday's law still holds. It means that knowing B only along the paths the electron actually travels (here B = 0 everywhere on them) does not fix the physics: two arrangements with the same B on the paths but different enclosed flux give different ∮A·dl and different fringes. Potentials that differ by the gradient of a single-valued function give the same ∮A·dl and are physically identical; that is gauge invariance.""")
    open(p, 'w', encoding='utf-8').write(s); print('ok mead s2')
else:
    print('mead s2 already')

# Mead 3.1: gauge freedom is redundancy, not fiction
sub('interlude_mead.txt', "for the phase of charged matter, and for the gauge principle of Lesson 39, A.\n", """for the phase of charged matter, and for the gauge principle of Lesson 39, A.

A second worry: if A matters so much, why can it be changed by a gauge transformation, A → A + ∇χ, without changing any prediction? Because when A shifts, the phase of every charged amplitude shifts with it in exactly the compensating way, so every measurable quantity, including every loop integral ∮A·dl, is untouched. Redundancy in a description is not the same as fiction. Latitude and longitude depend on an arbitrary choice of where to put zero, and every number changes if you move it; geography is not thereby made up. The map has freedom in how it is drawn, and the territory does not care. What is gauge-invariant about A, such as the phase it accumulates around a closed loop, is as real as anything in physics.
""")

# Mead 4: collective electrodynamics, emergence
sub('interlude_mead.txt', "the cousin of Prologue 7's many-photon Maxwell limit.\n", """the cousin of Prologue 7's many-photon Maxwell limit.

The wider picture behind Mead's programme is emergence. One electron interacting with another is quantum mechanics; a billion billion electrons sharing a phase in a wire or a ring look like a smooth current, a magnetic field, stored energy, a radiating wave. On that view Maxwell's equations are the large-scale handwriting of quantum matter, which makes them more remarkable, not less. "Fundamental" can mean two different things here. If it means describing the widest range of energies and processes, QED wins. If it means revealing a law most directly, a collective variable sometimes wins: flux quantization in units of h/2e is almost invisible electron by electron and obvious in the shared phase of the ring.
""")
