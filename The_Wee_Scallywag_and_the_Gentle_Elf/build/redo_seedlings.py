import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
os.makedirs(gen.OUT, exist_ok=True)
REF = os.path.join(gen.OUT2, "reference_cast_sheet.jpg")
BASE = re.sub(r"The ghost is always:.*?never silly or cute\. ", "", gen.FIX6_RULE, flags=re.S).replace("There is exactly ONE ghost in the picture and it is faint, never solid. ", "")
SC = ("EAR RULE: only Scally and Hopsi have pointed ears; Hal, Titch and Tabitha have round human ears. No ghost. DYNAMIC COMPOSITION, nobody looks at the viewer, no row, varied heights. Under a huge oak at dawn a hundred small seedlings grow, no two alike. Hopsi (pointed ears, hops wreath) kneels and writes a rhyme on a big oak leaf with her needle, tongue between her teeth. Hal (brown hair, slate) crouches comparing a tall seedling with a short one, frowning. Scally (pointed ears, ONE only) lies on his belly with his chin in his hands, nose to nose with a seedling, grinning. Titch (red cap) tears a crust in half, watching them. Tabitha (curly black hair in a bun, dark skin, grey coat, a sack of apples on the ground beside her) stands bending down, one hand cupped behind an ear, studying a moon-coloured petal with great curiosity. Exactly Hopsi, Hal, Scally, Titch and Tabitha; no wolf.")
gen.edit_with("c04a_seedlings_v9", REF, BASE + SC, "3:2")
