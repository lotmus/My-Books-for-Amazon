import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b2_more2 as m
b = m.b
fix = {
 "b71_counting_storm": m.D + "ONLY these seven: Hal, Titch, Tabitha, Hopsi, Scally, baby wolf Gucci and Old Walt with Dumpling the donkey. No other person, no adult elf, no tall woman. Scally is fully dressed in his ragged olive-brown hooded tunic. Dark storm light in a hollow of purple heather. The five children crouch low with feet together, hands over ears; Titch holds up fingers counting, face lit white by a distant violet flash; Hal and Tabitha watch the horizon; Hopsi shields Gucci; Walt holds Dumpling's halter; the great oak on the skyline. " + m.SK,
 "b77_village_sleeps": m.D + "A night view of a sleepy mill village under a huge moon. Every window is dark except one small attic window of the mill where Hal and baby wolf Gucci can be seen asleep in bed. Smoke curls from chimneys, the mill wheel turns very slowly in the stream, a small plain brown bird sleeps with its head under its wing on the mill roof, a cockerel sleeps on a wall, a cat curls on a sill. NO people outside, no children standing, empty peaceful lanes. Silvery blue night.",
 "b81_launch_raft": m.D + "Every child fully dressed, normal skin tones. A raft of six tied logs with a plank deck sits on a green pool; baby wolf Gucci has one paw on and is falling off with a splash; Hal on board with a long pole; Titch with a rope looped over her shoulder, the other end tied to a tree; Hopsi holding her bowl of hops high; on the bank Scally in grey socks shoves the raft, effort on his face, wearing his ragged olive-brown hooded tunic fully dressed; Tabitha watches the water; Old Walt on shore waves orders with his pole.",
}
for k, v in fix.items():
    b.S[k] = v
for n in (sys.argv[1:] or list(fix)):
    b.gen.edit_with(n, b.REF, b.BASE + b.EXTRA + b.S[n], "3:2")
