import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
os.makedirs(gen.OUT, exist_ok=True)
REF = os.path.join(gen.OUT2, "reference_cast_sheet.jpg")
SC = ("EAR RULE: only Scally (Sparefunk) and Hopsi have pointed ears; Hal, Titch and Tabitha have round human ears. DYNAMIC COMPOSITION, nobody looks at the viewer, no row. Inside the Mirror Mill at night, a dark still pond whose black surface shows a tall pale slender figure far away, only a faint reflection with a too-wide thin smile, safe and distant, no gore, not touching anyone. In the foreground Scally (pointed ears, ONE only) crouches hugging a big dripping clinking sack tight to his chest, eyes shut, jaw set, brave. Hopsi (pointed ears, hops wreath) kneels beside him, one steady hand on his shoulder, calm and warm. Behind them Hal frowns at the water holding his slate, Titch holds Tabitha's hand, Tabitha (curly black hair in a bun, dark skin, grey coat) looks at the pond with wide eyes, Gucci the grey wolf pup stands protectively in front with hackles up. The faint translucent old miller ghost holds a small lantern whose light is just flaring back warm gold, pushing the dark away. Spooky but safe and hopeful, warm gold lantern glow against deep blue shadow.")
gen.edit_with("c09f_dark_pond", REF, gen.FIX6_RULE + SC, "3:2")
