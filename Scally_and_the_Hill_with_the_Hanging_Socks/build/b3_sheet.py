import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
REF = os.path.join(gen.OUT2, "reference_cast_sheet.jpg")
P = ("Painted character reference sheet in exactly the same rich oil-painting style as the reference image. "
     "Keep the original characters from the reference with identical faces, hair, ears, skin tones and clothes: Hal, Titch, Tabitha and Gucci look about one year older and slightly taller; Scally (messy brown hair with a leaf sprig, large pointed elf ears, mossy olive-brown hooded tunic) and Hopsi (long wavy light-brown hair with a hops wreath, pointed elf ears, green dress, purple scarf) look exactly the same age as before; Gucci is now a bigger young wolf, size of a large dog, grey with blue eyes and one floppy ear. "
     "Add three new characters in the same style, standing among them, full body: "
     "WEN, a thin careful 9-year-old boy of East Asian heritage, straight black hair cut neatly, calm watchful dark eyes, round ears, a slightly oversized dark blue wool coat, a leather tool roll on his belt and a small screwdriver in his hand, serious expression with a hint of a smile; "
     "PIP, a small solemn 7-year-old human boy, dark brown hair, a small red knitted cap like Titch's, round ears, grubby knees, a crust in each fist, clearly the smallest child; "
     "DR LIANG, Wen's mother, a small brisk woman of East Asian heritage in her thirties, black hair in a bun with a pencil in it, kind amused eyes, a long blue coat, a black leather doctor's bag, round human ears. "
     "Nine characters on a plain dark mossy woodland background, all facing the viewer, each with a distinct face and personality. Only Scally and Hopsi have pointed ears.")
for n in (sys.argv[1:] or ["sheet_b3_a", "sheet_b3_b"]):
    gen.edit_with(n, REF, P, "3:2")
