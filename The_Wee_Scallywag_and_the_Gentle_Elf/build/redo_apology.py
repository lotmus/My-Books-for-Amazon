import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
os.makedirs(gen.OUT, exist_ok=True)
REF = os.path.join(gen.OUT2, "reference_cast_sheet.jpg")
BASE = re.sub(r"The ghost is always:.*?never silly or cute\. ", "", gen.FIX6_RULE, flags=re.S).replace("There is exactly ONE ghost in the picture and it is faint, never solid. ", "")
SC = ("No ghost anywhere. NO FIRE and NO FLAMES anywhere in the picture and NO burnt or damaged building: the stone granary and its wooden door are completely intact and clean. Night in the mill yard after a small fire has been put out. In the middle ground lies only a low wet black heap of soaked straw with a little pale steam rising, and wooden buckets stand about. "
      "The wee scallywag Scally (pointed ears, messy hair with a leaf, grey socks, sooty face) sits alone on the stone step with his knees up and his head down, ashamed and sorry. Hal (brown hair, clearly round ears, patched blue jacket) sits down beside him quietly with his slate on his knee, saying nothing, a small kind look. Soft moonlight and one lantern. Exactly Scally and Hal.")
gen.edit_with("c07a_apology_v8", REF, BASE + SC, "3:2")
