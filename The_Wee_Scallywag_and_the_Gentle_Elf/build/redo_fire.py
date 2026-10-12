import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
os.makedirs(gen.OUT, exist_ok=True)
REF = os.path.join(gen.OUT2, "reference_cast_sheet.jpg")
BASE = re.sub(r"The ghost is always:.*?never silly or cute\. ", "", gen.FIX6_RULE, flags=re.S).replace("There is exactly ONE ghost in the picture and it is faint, never solid. ", "")
DYN = "EAR RULE: ONLY Scally and Hopsi have pointed elf ears. The miller, the two neighbours (who wear caps), Hal, Titch and Tabitha all have clearly small ROUND human ears with no points at all. DYNAMIC COMPOSITION, nobody looks at the viewer, no row, varied heights and angles. No ghost anywhere. "
SC = {
 "d18_fire_night_v8": DYN + "Night in the mill yard, a small straw fire burning low and orange beside a stone wall, throwing red light, with a safe empty space around it. Hal's father the miller (stocky, bearded, nightshirt, one bandaged leg, leaning on a crutch) stands at the front pointing firmly at the children with his free arm shouting 'back, away from it'; two neighbours in the background lay big wet sacks over the flames using long poles, faces turned away. The five children stay well back at a safe distance: they pass wooden buckets in a line from the stream hand to hand: Hopsi (pointed ears) hands one to Titch (red cap), Titch to Hal, Tabitha (curly bun) drags a heavy wet sack along the ground, and Scally (pointed ears, sooty) runs in with two buckets, face stricken. Baby wolf Gucci barks from behind them, held back by Hal's foot. The fire is far on the LEFT side of the picture; every child is on the RIGHT side at least ten big steps away from it, none of them anywhere near the flames; only the miller and neighbours stand near the fire. Scally (pointed ears) is clearly visible running in with two buckets, with his face stricken; Hopsi is clearly visible with pointed ears. Exactly the miller, two neighbours, five children and Gucci.",
}
for n, sc in SC.items():
    gen.edit_with(n, REF, BASE + sc, "3:2")
