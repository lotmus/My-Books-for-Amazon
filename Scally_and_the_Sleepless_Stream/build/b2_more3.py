import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b2_scenes as b
D = ("EAR RULE: only Scally and Hopsi have pointed ears; Hal, Titch, Tabitha, Pip, Walt and all villagers have round human ears. DYNAMIC COMPOSITION, a low or high camera angle, characters at different heights, mid-action, nobody facing the viewer, no row. "
     "PIP is a small solemn six-year-old boy, dark brown hair, a small red knitted cap like his sister Titch's, small ROUND ears with no points at all, grubby knees, a crust in each fist; he is clearly the youngest and smallest child. ")
BT = "Scally wears big old brown boots too large for him. "
N = {
 "b83_walnut_boats": D + "A sunny autumn picnic on a stream bank in front of a crowd of villagers. A boat race of tiny boats made of walnut shells with matchstick masts and leaf sails floats on the water: one sinks, one races ahead with a small plain brown bird perched on its mast singing. Hal crouches grinning at his slate, Titch cheers, baby wolf Gucci jumps into the shallows after a boat, Pip kneels at the edge holding a single wooden clog as his entry, about to float it (all boats are hand-sized toys, no child sits in a boat), Scally (grey socks, pointed ears) punches the air as his boat wins, Hopsi watches thoughtfully with a hop in her fingers. In the middle of the stream the pompous Mayor in a waistcoat stands knee-deep in the water looking astonished, and Old Walt sits calmly on a rock holding out his hooked pole toward him. Joyful and funny.",
 "b84_pip_homecoming": D + "Evening mill yard, golden light. Pip bolts out of a crowd of villagers like a cork from a bottle and flings his arms round his big sister Titch's middle; Titch laughs, bending down to hug him; Pip points sternly at the pompous Mayor, who stands in a plain waistcoat with a round gold medal on a crooked chain (no cross, not a priest) and a pink face, one leg lifted as if he has just been made to stand on one leg; Hal's mother hugs Hal at the side; Old Walt on the donkey watches amused. Warm and funny.",
}
for k, v in N.items():
    b.S[k] = v
if __name__ == "__main__":
    for n in (sys.argv[1:] or list(N)):
        b.gen.edit_with(n, b.REF, b.BASE + b.EXTRA + b.S[n], "3:2")
