import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
os.makedirs(gen.OUT, exist_ok=True)
REF = os.path.join(gen.OUT2, "reference_cast_sheet.jpg")
BASE = re.sub(r"The ghost is always:.*?never silly or cute\. ", "", gen.FIX6_RULE, flags=re.S).replace("There is exactly ONE ghost in the picture and it is faint, never solid. ", "")
EAR = "EAR RULE: only Scally and Hopsi have pointed ears; Hal, Titch and Tabitha have round human ears. No ghost, no wolf unless named. DYNAMIC COMPOSITION, nobody looks at the viewer, no row, varied heights. "
S = {
 "c02e_butter_slip": EAR + "A sunny mill yard where everything has been smeared with butter. Titch (red cap, dark hair) slides on her bottom across the shiny cobbles with a crust held high above her head, mouth wide in a shriek of laughter; Hal (brown tousled hair, slate under his arm) reaches for the big wooden mill wheel and his hand skates right off the greasy rim, eyes wide; Scally (pointed ears, ONE leaf in his hair) stands buttery to the elbows with a huge empty butter crock, trying to look innocent; Hopsi (pointed ears, hops wreath) stands calmly on a dry stone, having looked first, eating one hop. Funny, warm, golden afternoon light.",
 "c08a_loft_stories": EAR + "Night in a cosy mill loft, a nest of old sacks, a lantern turned low, rain on the roof. Scally (pointed ears) sits up with the lantern held under his chin, telling a wild story with both arms spread wide, grinning; Titch (red cap) rolls on the sacks crying with laughter; Hal (slate on his knee) lies grinning at the roof beams; Hopsi (hops wreath) sits upright with a thoughtful smile; Gucci the baby wolf has lifted his head to see what the noise is; Tabitha (curly black hair in a bun, dark skin, grey coat) sits on her sacks with her chin on her knees, eyes moving from face to face, quietly watching, not laughing. Warm gold lantern light, deep shadow. Exactly Scally, Titch, Hal, Hopsi, Tabitha and Gucci.",
}
for n in (sys.argv[1:] or list(S)):
    gen.edit_with(n, REF, BASE + S[n], "3:2")
