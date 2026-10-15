import re, sys, os, json, base64, urllib.request, urllib.error

CFG = r"D:\My_C#_Apps\MediaStar.GPT\config\asset_api.ini"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Step_Stories_Pics_New")
os.makedirs(OUT, exist_ok=True)


def key():
    for l in open(CFG, encoding="utf-8", errors="ignore"):
        m = re.match(r"\s*xai_key\s*=\s*(\S+)", l)
        if m:
            return m.group(1)
    raise SystemExit("no xai_key")


STYLE = ("Detailed painterly children's book illustration, warm natural light, soft textures, "
         "rich greens and golds, gentle storybook fantasy, ages 6 to 9, no text, no lettering, no watermark. ")
CAST = (
    "Characters, always drawn exactly like this: "
    "HAL, an 8-year-old human boy with tousled brown hair, freckles, round ears, patched blue jacket, brown trousers, sturdy boots, carries a small slate. "
    "TITCH, an 8-year-old human girl with dark brown shoulder-length hair under a red knitted cap, round ears, green patched coat, yellow scarf. "
    "SPAREFUNK, an 8-year-old little devil boy with short sharp pointed ears, black spiky hair, blue-grey hooded jacket, red neckerchief, big muddy boots, a cheeky friendly grin with no fangs and no scary expression. "
    "HOPSI, a 9-year-old elf girl with long soft pointed ears, long wavy light-brown hair with a wreath of green hops, green dress with a purple scarf. "
    "TABITHA, an 8-year-old Black girl with dark brown skin and curly black hair in a bun tied with a rust-coloured band, round ears, grey coat over a brown dress. "
    "GUCCI, a grey wolf pup with blue eyes, a darker saddle on its back and one floppy ear. "
    "Only Sparefunk and Hopsi have pointed ears; Hal, Titch and Tabitha have clearly normal round human ears. Any paper tag on boots is completely blank with no writing on it. ")


def gen(name, scene, aspect="3:2"):
    k = key()
    body = {"model": "grok-imagine-image-quality", "prompt": STYLE + CAST + scene,
            "aspect_ratio": aspect, "resolution": "1k"}
    req = urllib.request.Request("https://api.x.ai/v1/images/generations", data=json.dumps(body).encode(),
                                 headers={"Authorization": "Bearer " + k, "Content-Type": "application/json",
                                          "User-Agent": "StepStories/1.0"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=240))
    except urllib.error.HTTPError as e:
        print(name, "HTTP", e.code, e.read()[:300].decode("utf-8", "ignore"))
        return False
    item = r["data"][0]
    open(os.path.join(OUT, name + ".url.txt"), "w").write(str(item.get("url", "")))
    path = os.path.join(OUT, name + ".jpg")
    if item.get("b64_json"):
        open(path, "wb").write(base64.b64decode(item["b64_json"]))
    else:
        open(path, "wb").write(urllib.request.urlopen(urllib.request.Request(item["url"], headers={"User-Agent": "Mozilla/5.0"}), timeout=240).read())
    print(name, "ok", os.path.getsize(path) // 1024, "KB")
    return True


SCENES = {
    "cover_art": ("portrait", "2:3",
        "Front cover art for a children's book, portrait, no title text. Hal, Titch, Sparefunk, Hopsi and Tabitha sit together on the worn stone step of an old ivy-covered stone mill with a mossy water wheel and a stream, "
        "Gucci the wolf pup at their feet, a pair of spare boots with a blank paper tag beside Sparefunk, three white stones in a row in the grass, a faint green glow in the air, a small pale friendly ghost in a flour-sack cloak and dusty hat peeking from an upper window. "
        "Leave empty sky at the top and bottom for the title and author name."),
}

SCENES.update({
 "s01_step_bargain": ("ch1","3:2","Hal sits on the worn stone step of an old ivy-covered mill with an empty sack and a bowl of porridge, holding his boots and looking worried. Sparefunk is dropping from the mossy water wheel above with a cheeky grin. A spare pair of boots with a blank tag stands on the step. Hopsi sits two steps down, mending with a needle and eating a hop."),
 "s02_wall_run": ("ch1","3:2","Sparefunk running straight up the stone wall of the mill like a squirrel, a crack of bright green magic light spreading across the yard and up the wall behind him. Hal and Hopsi stand below, staring up. Hal holds an empty porridge bowl."),
 "s03_log_launch": ("ch2","3:2","Hal flying through the air off a tipping fallen log over a stream, arms out, startled. Sparefunk grins as he lands on the high end of the log. Two king's messengers in blue and purple coats and feathered tricorn hats stare with open mouths. Dark storm clouds gather and the first hail falls. Titch runs in the background carrying two crusts."),
 "s04_ghost_wheel": ("ch3","3:2","Night. A small pale friendly ghost in a flour-sack cloak and dusty hat sits on top of the slowly turning mill wheel under a bright moon. Hal sits on the step watching. Hopsi pours hop tea into four cups. Sparefunk chases the ghost, laughing. Little glowing lights drift in the air."),
 "s05_toad_ford": ("ch4","3:2","A giant moss-green warty toad with a moustache of pondweed sits on a flat stone in a shallow ford and shoots out its long tongue to snatch Sparefunk's boot off his foot. Sparefunk tumbles backwards. A bright green cloud of grasshoppers rises from the grass. Hal slips into the water, Titch holds up a cloth like a net, Hopsi holds her bowl of hops high."),
 "s06_pike_gucci": ("ch5","3:2","An enormous old pike with a head like a hatchet leaps from a brown mill pond under a willow, snapping at the water. Gucci the wolf pup scrambles back on the bank. Hopsi pulls Gucci back by the scruff. Titch holds a cloth like a net, Hal holds a long thin wooden stick (not an axe), Sparefunk slides in the mud."),
 "s07_fog_stranger": ("ch6","3:2","Thick white fog rolls up from the stream. A tall thin figure in a coat the colour of dusk, with a smile too wide and a clinking bag, stands at the end of the road, its shadow stretching far across the grass toward the mill. All five children stand together on the mill step with Gucci growling, Tabitha holding apples, a small pale ghost peeking from the roof."),
 "s08_culvert": ("ch7","3:2","The children and baby Gucci scramble and duck at a run into a low black stone culvert tunnel under a road, led by the ghost holding a glowing lantern, hail and fog whipping behind them. Three white stones glow at the entrance. Willows and reeds bend in the wind."),
 "s09_mirror_mill": ("ch7","3:2","The children and baby Gucci tumble out of a tunnel, gasping with wonder, into a mirror-image mill in which everything is reversed: the water wheel turns backwards, the stream flows uphill, the sign above the door shows only abstract scribbles. A spare pair of boots with a clean blank tag stands by the door. A silver pond beside it reflects another mill."),
 "s10_pull_bag": ("ch7","3:2","Sparefunk climbs out backwards from a dark open sluice gate soaked and black with mud, holding a dripping clinking sack, tied to a long thread. Hal, Titch, Hopsi and Tabitha haul on the thread, Gucci tugs Titch's coat, and a small pale ghost holds a lantern high."),
 "s11_stranger_flour": ("ch7","3:2","Seen as if reflected in a silver pond, with the children caught mid-cheer on the bank and Sparefunk pointing and laughing: a tall thin stranger in a dusk-coloured coat is stuck in a bog up to his knees, a burst sack raining white flour like snow over him, small grey pebbles and shattered little jars falling around him, the fog thinning and his long shadow letting go of the ground."),
 "s12_stay_step": ("ch8","3:2","Night on the mill step. Five exhausted children sit together, wet and muddy, with Gucci across their feet. Hal holds up a slate. Sparefunk sits with a pair of empty boots shining softly beside him, looking astonished. Warm lantern light, the mill wheel turning in the dark behind, stars."),
 "s13_ghost_sunrise": ("ch9","3:2","Dawn. A small pale ghost in a flour-sack cloak and dusty hat stands on top of the mill wheel in the first sunbeams, his hat turning into golden light. Five children and Gucci sleep in a heap on the step, Gucci across Sparefunk's foot. Behind the mill in the long grass, one rectangular egg rocks."),
})

SCENES["cast_sheet"] = ("ref","3:2","Character reference sheet. The five children and the wolf pup stand in a row facing the viewer, full body, evenly lit, on a plain warm cream background, each one clearly visible with a clear face. From left: Hal, Titch, Sparefunk, Hopsi, Tabitha, with Gucci the wolf pup sitting in front. Keep every face friendly, distinct and easy to recognise. Titch and Tabitha and Hal show clearly round human ears.")

EARS = " IMPORTANT EAR RULES: Sparefunk has small sharp pointed elf-style ears on the SIDES of his head at normal ear height, like a pixie, never animal ears on top of his head. Hopsi has long slender elf ears on the sides of her head swept up and back into elegant points, not floppy, not rabbit ears. Hal, Titch and Tabitha have small ordinary round human ears on the sides of their heads. "
BASE = "Character reference sheet. The five children and the wolf pup stand in a row facing the viewer, full body, evenly lit, on a plain warm cream background, each clearly visible with a clear friendly face. From left: Hal, Titch, Sparefunk, Hopsi, Tabitha, with Gucci the wolf pup sitting in front."
SCENES["cast_sheet_b"] = ("ref","3:2",BASE+EARS)
SCENES["cast_sheet_c"] = ("ref","3:2",BASE+EARS+" Sparefunk is slightly shorter and wiry with a sharp chin and a sly, cheeky half-smile; Hal is taller and gentler with a calm serious face.")

if __name__ == "__main__" and sys.argv[1:2] not in (["EDIT"], ["SHEET"], ["PAINT"], ["FIXSHEET"], ["FIX"], ["FIXSHEET2"], ["FIX2"], ["FIXSHEET3"], ["FIX3"], ["FIXSHEET4"], ["FIX4"], ["GHOSTSHEET"], ["FIX5"], ["FIX6"], ["FIX7"]):
    names = sys.argv[1:] or list(SCENES)
    for n in names:
        _, asp, sc = SCENES[n]
        gen(n, sc, asp)


REF = os.path.join(OUT, "cast_sheet_b.jpg")
EDIT_RULE = ("Use the characters in the reference image EXACTLY: keep every character's face, hair, ears, skin tone and clothes identical to the reference "
             "(Hal brown tousled hair and slate; Titch dark hair, red bobble cap, yellow scarf, green patched coat; Sparefunk black spiky hair, small sharp pointed elf ears at the sides of his head, red neckerchief, blue-grey hooded jacket; "
             "Hopsi long light-brown hair with a hops wreath, long elven ears, green dress, purple scarf; Tabitha curly black hair in a bun, grey coat, brown dress; Gucci the grey wolf pup). "
             "Hal, Titch and Tabitha and all other humans (messengers, the stranger) have clearly round ears. Sparefunk always has a cheeky, friendly, mischievous grin, never angry or scary eyebrows. Show exactly and only the characters named in the scene below, plus the creatures named; do not add any other child or elf. Create a new full-scene children's book illustration, painterly, warm natural light, no text, no lettering. Scene: ")


def edit(name, scene, aspect="3:2"):
    k = key()
    b64 = base64.b64encode(open(REF, "rb").read()).decode()
    body = {"model": "grok-imagine-image-quality", "prompt": EDIT_RULE + scene,
            "image": {"url": "data:image/jpeg;base64," + b64}, "resolution": "1k",
            "response_format": "url", "aspect_ratio": aspect}
    req = urllib.request.Request("https://api.x.ai/v1/images/edits", data=json.dumps(body).encode(),
                                 headers={"Authorization": "Bearer " + k, "Content-Type": "application/json",
                                          "User-Agent": "StepStories/1.0"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=300))
    except urllib.error.HTTPError as e:
        print(name, "HTTP", e.code, e.read()[:300].decode("utf-8", "ignore"))
        return False
    item = r["data"][0]
    path = os.path.join(OUT, name + ".jpg")
    if item.get("b64_json"):
        open(path, "wb").write(base64.b64decode(item["b64_json"]))
    else:
        open(path, "wb").write(urllib.request.urlopen(urllib.request.Request(item["url"], headers={"User-Agent": "Mozilla/5.0"}), timeout=240).read())
    print(name, "ok", os.path.getsize(path) // 1024, "KB")
    return True


if __name__ == "__main__" and sys.argv[1:2] == ["EDIT"]:
    for n in sys.argv[2:]:
        _, asp, sc = SCENES[n]
        edit(n if n.endswith("_r") else n + "_r", sc, asp)


def edit_with(name, ref, prompt, aspect="3:2"):
    k = key()
    b64 = base64.b64encode(open(ref, "rb").read()).decode()
    body = {"model": "grok-imagine-image-quality", "prompt": prompt,
            "image": {"url": "data:image/jpeg;base64," + b64}, "resolution": "1k",
            "response_format": "url", "aspect_ratio": aspect}
    req = urllib.request.Request("https://api.x.ai/v1/images/edits", data=json.dumps(body).encode(),
                                 headers={"Authorization": "Bearer " + k, "Content-Type": "application/json", "User-Agent": "StepStories/1.0"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=300))
    except urllib.error.HTTPError as e:
        print(name, "HTTP", e.code, e.read()[:300].decode("utf-8", "ignore")); return False
    item = r["data"][0]
    path = os.path.join(OUT, name + ".jpg")
    open(path, "wb").write(urllib.request.urlopen(urllib.request.Request(item["url"], headers={"User-Agent": "Mozilla/5.0"}), timeout=240).read())
    print(name, "ok", os.path.getsize(path) // 1024, "KB"); return True

PAINT = ("Rich, highly detailed oil-painting style classic fantasy storybook illustration, textured brushwork, moody natural light, expressive characterful faces with real personality, "
         "realistic child proportions, ragged earthy handmade clothing with visible texture, dirt under the fingernails, nothing flat or cartoonish, no text. ")
SHEET = ("Painted character reference sheet in exactly the same rich painterly style as the reference image. The five children and a wolf pup stand in a row facing the viewer, full body, on a plain dark mossy woodland background. "
 "The boy from the reference image is SPAREFUNK, the little devil: copy his face, messy brown hair with a leaf sprig, large sharp pointed elf ears at the sides of his head, torn mossy olive-brown hooded tunic, grubby hands and cheeky grin exactly. "
 "HAL: 8-year-old human boy, tousled brown hair, freckles, thoughtful steady eyes, round ears, patched blue wool jacket, a slate under his arm, mended boots. "
 "TITCH: 8-year-old human girl, dark brown hair, quick bright eyes and a knowing half-smile, round ears, red knitted cap, yellow scarf, green patched coat, crumbs and thread on her sleeves. "
 "HOPSI: 9-year-old elf girl, calm grave expression, long wavy light-brown hair with a wreath of hops, long slender swept-back elf ears, moss-green dress and purple scarf, a needle in her hand. "
 "TABITHA: 8-year-old Black girl, dark brown skin, curly black hair in a bun with a rust band, round ears, watchful warm eyes, grey coat over a brown dress, an apple in her hand. "
 "GUCCI: a grey wolf pup with blue eyes, a darker saddle, one floppy ear and a grumpy little duchess face. Every child has a distinct face, age, build and personality. ")
if __name__ == "__main__" and sys.argv[1:2] == ["SHEET"]:
    ref = os.path.join(OUT, "ref_sparefunk.jpg")
    for n in sys.argv[2:]:
        edit_with(n, ref, PAINT + SHEET)


PAINT_RULE = ("Rich, highly detailed oil-painting style classic fantasy storybook illustration, textured brushwork, warm magical light with adventure and a little danger, never gloomy, no text, no lettering. "
 "Use the six characters in the reference painting EXACTLY, keeping each one's face, hair, ears, skin tone and clothes identical: "
 "Sparefunk (messy brown hair with a leaf sprig, large sharp pointed elf ears, ragged mossy olive-brown hooded tunic, grubby hands, cheeky grin, big muddy boots on his feet); "
 "Hal (tousled brown hair, freckles, steady grave eyes, round ears, patched blue jacket, slate); "
 "Titch (dark hair, red knitted cap, yellow scarf, green patched coat, knowing half-smile, round ears hidden by hair); "
 "Hopsi (long wavy light-brown hair, hops wreath, long swept-back elf ears, green dress, purple scarf, calm face); "
 "Tabitha (curly black hair in a bun with a rust band, round ears, grey coat, brown dress, watchful warm eyes); "
 "Gucci (grey wolf pup, blue eyes, grumpy little duchess face). All other people (messengers, the stranger) have round human ears. "
 "Show exactly and only the characters named in this scene, plus the creatures named; add no other child or elf. Keep expressions lively and fitting the action. Scene: ")
if __name__ == "__main__" and sys.argv[1:2] == ["PAINT"]:
    ref = os.path.join(OUT, "paint_sheet_b.jpg")
    for n in sys.argv[2:]:
        _, asp, sc = SCENES[n]
        edit_with(n + "_p", ref, PAINT_RULE + sc, asp)


SHEETFIX = ("Keep this painting exactly as it is: the same five children with identical faces, hair, ears, clothes and poses, the same painterly style and background. "
            "Change only the wolf: make Gucci a much younger and smaller baby wolf pup, tiny, about knee height to the children, with a round fluffy head, oversized paws, short muzzle, big blue eyes, one floppy ear and a grumpy little duchess expression, clearly a baby.")
if __name__ == "__main__" and sys.argv[1:2] == ["FIXSHEET"]:
    edit_with("paint_sheet_c", os.path.join(OUT, "paint_sheet_b.jpg"), SHEETFIX)


FIX_RULE = (PAINT_RULE.replace("Gucci (grey wolf pup, blue eyes, grumpy little duchess face)",
    "Gucci (a tiny BABY grey wolf pup, knee height to the children, round fluffy head, oversized paws, blue eyes, grumpy little duchess face)")
  + "Hal's slate is a small old black chalkboard in a plain wooden frame with chalk marks, never a tablet or screen. "
    "The ghost is always the same: a pale milky-white translucent old miller with a flour-sack cloak, a dusty floppy hat and a friendly, slightly worried smile. "
    "Any sign, tag or paper shows only abstract scribbles, never readable letters. Nobody holds an axe or any weapon. "
    "COMPOSITION: dynamic and active, characters caught mid-action, in motion, interacting with each other and the setting, varied poses and camera angles, never lined up in a row facing the viewer. Scene: ")
if __name__ == "__main__" and sys.argv[1:2] == ["FIX"]:
    ref = os.path.join(OUT, "paint_sheet_c.jpg")
    for n in sys.argv[2:]:
        _, asp, sc = SCENES[n]
        sc = sc.replace("Hal holds a stick", "Hal holds a long thin wooden stick")
        edit_with(n + "_q", ref, FIX_RULE.split("Scene: ")[0] + "Scene: " + sc, asp)


if __name__ == "__main__" and sys.argv[1:2] == ["FIXSHEET2"]:
    edit_with("paint_sheet_d", os.path.join(OUT, "paint_sheet_c.jpg"),
      "Keep this painting exactly as it is, with identical faces, hair, ears, clothes, poses, wolf pup and background. Change only one thing: the grey rectangular object Hal holds under his arm must become an old black chalkboard slate in a rough wooden frame with a few white chalk marks and a bit of string, clearly an old-fashioned school slate and not a tablet or screen.")


FIX2_RULE = (FIX_RULE.split("Scene: ")[0].replace("Hal's slate is a small old black chalkboard in a plain wooden frame with chalk marks, never a tablet or screen.",
    "Hal's slate is a SMALL old black chalkboard in a rough wooden frame, about the size of a school book, with chalk marks, never a tablet or screen.")
  + "The stranger and all adults are thin pale human beings with ordinary ROUND human ears, never pointed ears. Sparefunk has no tail. Nobody holds an axe or any blade. Scene: ")
FIX2_EDITS = {
 "s02_wall_run": ("running straight up the stone wall of the mill like a squirrel", "running straight up the vertical stone wall of the mill with his hands and feet pressed to the stones, no tail"),
 "s06_pike_gucci": ("Hal holds a long thin wooden stick (not an axe)", "Hal points with his empty hand at the pike"),
 "s05_toad_ford": ("Hal slips into the water, Titch holds up a cloth like a net, Hopsi holds her bowl of hops high.",
                   "Hal wades and slips into the water splashing, Titch swings a cloth like a net at the grasshoppers, Hopsi holds her bowl of hops high above her head, Tabitha ducks laughing and Gucci leaps at the grasshoppers."),
 "s10_pull_bag": ("Hal, Titch, Hopsi and Tabitha haul on the thread, Gucci tugs Titch's coat, and a small pale ghost holds a lantern high.",
                  "Hal, Titch, Hopsi and Tabitha lean backwards hauling hard on the thread with straining faces, Gucci tugs Titch's coat with his teeth, and the ghost holds a lantern high and cheers."),
 "s12_stay_step": ("Five exhausted children sit together, wet and muddy, with Gucci across their feet.",
                   "Five exhausted children slump together on the step, wet and muddy, Titch leaning on Tabitha, Hopsi smiling at Sparefunk, baby Gucci curled across their feet."),
}
if __name__ == "__main__" and sys.argv[1:2] == ["FIX2"]:
    ref = os.path.join(OUT, "paint_sheet_d.jpg")
    for n in sys.argv[2:]:
        _, asp, sc = SCENES[n]
        if n in FIX2_EDITS:
            a, b = FIX2_EDITS[n]
            sc = sc.replace(a, b)
        edit_with(n + "_v", ref, FIX2_RULE + sc, asp)


if __name__ == "__main__" and sys.argv[1:2] == ["FIXSHEET3"]:
    edit_with("paint_sheet_e", os.path.join(OUT, "paint_sheet_d.jpg"),
      "Keep this painting exactly as it is, with identical children, faces, hair, ears, clothes, slate, poses and background. Change only the wolf pup Gucci: his head is far too big and too wide. Redraw him as a realistic baby wolf cub with correct proportions: a small narrow head, a longer slim pointed muzzle, small rounded ears held up, a slender neck, a body larger than the head, long thin legs and big paws, grey fur with a darker saddle, blue eyes and a grumpy expression. Same size as before, sitting at the right.")


if __name__ == "__main__" and sys.argv[1:2] == ["FIXSHEET4"]:
    edit_with("paint_sheet_f", os.path.join(OUT, "paint_sheet_d.jpg"),
      "Keep this painting exactly as it is: all five children fully visible including Tabitha at the far right holding her apple, with identical faces, hair, ears, clothes, slate, poses and background. Change only the baby wolf pup Gucci sitting on the ground in front of Tabitha's feet at the bottom right: redraw him SMALL, no taller than Tabitha's knee, as a realistic baby wolf cub with correct proportions: a narrow small head, a slim pointed muzzle, small rounded upright ears, a body bigger than the head, big paws, grey fur with a darker saddle, blue eyes and a grumpy expression. His head must be small and narrow, not big or wide.")


FIX3_RULE = (FIX2_RULE.split("Scene: ")[0].replace("a tiny BABY grey wolf pup, knee height to the children, round fluffy head, oversized paws, blue eyes, grumpy little duchess face",
    "a small BABY grey wolf cub, knee height to the children, with a SMALL NARROW head, slim pointed muzzle, small upright rounded ears, big paws, blue eyes and a grumpy expression, exactly as in the reference")
  + "The ghost is always clearly a see-through, softly glowing, pale blue-white ghost with no legs, floating, never a solid man. The stranger is a tall thin pale man with long dark hair covering his ears, drawn larger than the children. Scene: ")
FIX3_EDITS = dict(FIX2_EDITS)
FIX3_EDITS["s10_pull_bag"] = (FIX2_EDITS["s10_pull_bag"][0], "Hal, Titch, Hopsi and Tabitha lean backwards hauling hard on the thread with straining faces, Gucci tugs Titch's coat with his teeth, and the translucent floating ghost holds a lantern high and cheers.")
if __name__ == "__main__" and sys.argv[1:2] == ["FIX3"]:
    ref = os.path.join(OUT, "paint_sheet_f.jpg")
    for n in sys.argv[2:]:
        _, asp, sc = SCENES[n]
        if n in FIX3_EDITS:
            a, b = FIX3_EDITS[n]
            sc = sc.replace(a, b)
        edit_with(n + "_w", ref, FIX3_RULE + sc, asp)


SCENES.update({
 "s14_howl_moon": ("ch6","3:2","Night at the mill. A huge full moon over willows. Baby Gucci stands on the top mill step with his head tilted back, howling at the moon. Sparefunk beside him howls with his head thrown back and hands cupped around his mouth, Titch lies on the step laughing with her hands over her ears, Hal grins surprised, Hopsi sits calmly with her needle, and the ghost on the roof cups a hand to his ear. Warm lantern light. No other people."),
 "s15_moon_model": ("ch6","3:2","Night in the mill yard. Hal stands in the middle holding an apple out at arm's length with a serious scientist's frown, his small chalkboard slate under his other arm. A lantern hangs on a post across the yard glowing like a little sun, lighting exactly one half of the apple with a clear bright half and dark half. Titch, Hopsi and Sparefunk crouch around watching with fascination, baby Gucci sniffs the apple. A full moon in the sky. No other people."),
 "s16_parents_dawn": ("ch10","3:2","Dawn at the mill. The water wheel turns and fifty flour sacks are stacked on the step. Hal's father, a stocky tired miller with a grey-brown beard and a bandaged leg on a crutch, has sat down heavily on the step looking astonished. Hal's mother, a warm weathered woman with brown hair under a kerchief, holds a basket and laughs. Mrs Crumb the plump baker in a floury apron hugs a sack, and villagers with empty sacks crowd behind. The five children and baby Gucci sit in a happy tired heap at the front. All the adults have ordinary round human ears."),
 "s17_ghost_trap": ("ch3","3:2","Night by the mill under a bright moon. Sparefunk grins as he slams the lid on a jam jar with the small see-through ghost sitting politely inside, looking mildly bored with his hat on. Titch holds up her cloth like a net, Hal and Hopsi watch with a teapot and cups. No other people."),
})
FIX4_RULE = FIX3_RULE.split("Scene: ")[0].replace("The stranger is a tall thin pale man","The stranger appears ONLY when the scene text names him; otherwise there is no adult or stranger in the picture. Exactly one Gucci appears and exactly the people named. When he appears the stranger is a tall thin pale man") + "Scene: "
FIX4_EDITS = {
 "s13_ghost_sunrise": ("Five children and Gucci sleep in a heap on the step, Gucci across Sparefunk's foot.", "Five children sleep in a heap on the step with exactly one baby wolf cub Gucci asleep across Sparefunk's foot."),
}
if __name__ == "__main__" and sys.argv[1:2] == ["FIX4"]:
    ref = os.path.join(OUT, "paint_sheet_f.jpg")
    for n in sys.argv[2:]:
        _, asp, sc = SCENES[n]
        if n in FIX4_EDITS:
            a, b = FIX4_EDITS[n]; sc = sc.replace(a, b)
        edit_with(n + "_x", ref, FIX4_RULE + sc, asp)


GHOST = ("an old miller's ghost with real character: a lined, weathered, kindly but world-weary face, bushy grey mutton-chop whiskers and a drooping moustache, deep-set tired humorous eyes, a battered floppy dusty hat, "
         "a flour-sack cloak over an old waistcoat and rolled shirtsleeves, flour dust drifting off him, pale blue-white translucent glowing body that fades into mist below the knees, dignified, a little sad, never cute, never cartoonish, never a bedsheet ghost")
OUT2 = os.path.join(os.path.dirname(OUT), "Step_Stories_Pics_Final")
if __name__ == "__main__" and sys.argv[1:2] == ["GHOSTSHEET"]:
    edit_with("ghost_sheet_a", os.path.join(OUT2, "reference_cast_sheet.jpg"),
      "Keep this painting exactly as it is: the same five children and baby wolf, identical faces, hair, ears, clothes, slate and poses, the same painterly style and background. Add one more figure: " + GHOST + ". He floats above and slightly behind the children, at the upper centre, drawn at the same painterly quality, looking down at them with a faint fond smile.")


import re as _re
GHOST_SENT = "The ghost is always: " + GHOST + ". He is drawn at the scale of a grown man, much taller than the children, and is never silly or cute. "
FIX5_RULE = _re.sub(r"The ghost is always clearly.*?never a solid man\. ", GHOST_SENT, FIX4_RULE, flags=_re.S)
def ghostify(sc):
    sc = _re.sub(r"(an? |the )?(small |tiny )?((pale|see-through|translucent|friendly|milky-white) ?,? ?)*ghost( in a flour-sack cloak and dusty hat)?", "the old miller ghost", sc)
    sc = sc.replace("the the old miller ghost", "the old miller ghost")
    return sc
FIX5_EDITS = {"s17_ghost_trap": ("slams the lid on a jam jar with the old miller ghost sitting politely inside, looking mildly bored with his hat on", "slams the lid on a big glass jam jar with the old miller ghost, magically shrunk small enough to sit inside it, sitting politely with his arms folded, looking mildly bored and dignified in his hat")}
if __name__ == "__main__" and sys.argv[1:2] == ["FIX5"]:
    ref = os.path.join(OUT2, "reference_cast_sheet.jpg")
    for n in sys.argv[2:]:
        _, asp, sc = SCENES[n]
        sc = ghostify(sc)
        if n in FIX5_EDITS:
            a, b = FIX5_EDITS[n]; sc = sc.replace(a, b)
        edit_with(n + "_y", ref, FIX5_RULE + sc, asp)


FAINT = ("very faint, delicate and mostly transparent, only about a third visible, painted in thin pale washes so the background shows clearly through his body, glowing softly and fading into wisps of mist from the chest down, with a gentle, fond, slightly wistful expression")
FIX6_RULE = FIX5_RULE.replace("pale blue-white translucent glowing body that fades into mist below the knees", FAINT).replace("dignified, a little sad,", "dignified, warm,") + "There is exactly ONE ghost in the picture and it is faint, never solid. "
if __name__ == "__main__" and sys.argv[1:2] == ["FIX6"]:
    ref = os.path.join(OUT2, "reference_cast_sheet.jpg")
    for n in sys.argv[2:]:
        _, asp, sc = SCENES[n]
        sc = ghostify(sc)
        if n in FIX5_EDITS:
            a, b = FIX5_EDITS[n]; sc = sc.replace(a, b)
        if n == "s14_howl_moon":
            sc = sc.replace("and the old miller ghost on the roof cups a hand to his ear", "and a single faint old miller ghost floats above the roof cupping a hand to his ear")
        edit_with(n + "_z", ref, FIX6_RULE + sc, asp)


SCENES.update({
 "s18_fire_night": ("ch7","3:2","IMPORTANT: exactly five children are visible: Sparefunk and Hopsi have pointed ears; Hal, Titch and Tabitha have clearly ROUND human ears with no points at all. Night in the mill yard. A small heap of straw burns with a bright orange fire beside the stone granary door, throwing red light. Hal and Tabitha swing big soaked wet sacks down onto the flames to smother them, steam and smoke rising. Titch and Hopsi pass wooden buckets along a line from the stream with Hopsi clearly visible, Sparefunk runs with two buckets, baby Gucci barks, the faint old miller ghost coughs and waves smoke away, and in the doorway of the mill Hal's father, a stocky bearded miller in a nightshirt on a crutch, is hurrying out. Everyone safe, nobody too close to the flames."),
 "s19_flour_flash": ("ch9","3:2","Seen as if through a silver mirror pond: far off over a foggy bog a huge soft ball of yellow-orange flame blooms inside a thick white cloud of flour, lighting the fog gold, with a thin dark stranger in a dusk-coloured coat thrown back off his feet into the reeds, his lantern in pieces. In the foreground at the edge of the pond, Hal, Titch, Hopsi, Tabitha and Sparefunk shield their eyes with their arms and flinch away, baby Gucci ducking behind them, the faint old miller ghost holding his cold lantern. Only the named characters."),
})
if __name__ == "__main__" and sys.argv[1:2] == ["FIX7"]:
    ref = os.path.join(OUT2, "reference_cast_sheet.jpg")
    for n in sys.argv[2:]:
        _, asp, sc = SCENES[n]
        edit_with(n + "_n", ref, FIX6_RULE + sc, asp)


SCENES["s18a"] = ("ch7","3:2","Night in the mill yard, wide view so all five children fit. A small bonfire and a heap of straw burn beside a stone wall, orange glow. LEFT TO RIGHT: Sparefunk (pointed ears) runs in with two wooden buckets; Titch (red cap, round ears) passes a bucket; Hopsi (hops wreath, pointed ears) passes a bucket; Hal (brown hair, round ears) and Tabitha (curly bun, round ears) lay big wet sacks onto the straw with long poles, faces turned away from the heat. Baby wolf Gucci barks beside them. In the far background a miller in a nightshirt on a crutch hurries out of a door, and a faint old ghost in a hat waves smoke away. Everyone stays a safe distance. All five children are fully visible.")
SCENES["s18b"] = ("ch7","3:2","Night in the mill yard, medium wide view. In the centre a heap of straw and a bonfire burn low and orange. Close to the viewer, Hal and Tabitha swing wet dark sacks down onto the flames, steam hissing. Behind them Titch, Hopsi and Sparefunk stand in a line passing buckets from the stream, all five children clearly in the picture, Hopsi and Sparefunk with pointed ears and the other three with round ears. Baby wolf Gucci barks. At the right edge a faint ghost in a hat coughs into a sleeve. No adult in the picture.")
