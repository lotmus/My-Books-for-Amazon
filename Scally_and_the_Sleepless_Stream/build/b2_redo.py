import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b2_scenes as b
D = ("EAR RULE: only Scally and Hopsi have pointed ears; Hal, Titch, Tabitha, Walt have round human ears. DYNAMIC COMPOSITION, a low camera angle, mid-action, nobody facing the viewer, no row. ")
N = {
 "b27_whirlpool": D + "Dusk at the head of a grey misty bog. A great slow whirlpool turns in a wide dark natural pool among reeds and wet stones, a real spiralling funnel of dark water with pale foam, not a basin or fountain, no man-made rim. Above it rises a tall thin pale mist shaped like a very tall man in a long coat, faint and sad, not solid, no face. On the bank in the foreground the children and Gucci stand back from the edge, tense, Walt holding out his hooked pole as a barrier, Hal clutching his slate, Hopsi pale and still, Dumpling behind. Scally (grey socks, pointed ears) stares at the whirl. Eerie but safe.",
 "b33_mist_bows": D + "Dusk at a calm black bog pool as the whirlpool stops. The pale tall mist has thinned into long soft rags lifting away into the dark, and in it for a moment appears a thin pale tired face with a gentle relieved expression, bowing its head toward Scally; no body, only the mist and the faint face. Scally (pointed ears, grey socks) stands in the foreground looking up in awe with his mouth slightly open; Hopsi, Hal, Titch, Tabitha and Gucci watch from the bank, hushed. First star in the sky. Peaceful, hopeful, not scary.",
}
for k, v in N.items():
    b.S[k] = v
for n in (sys.argv[1:] or list(N)):
    b.gen.edit_with(n, b.REF, b.BASE + b.EXTRA + b.S[n], "3:2")
