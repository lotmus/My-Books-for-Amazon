import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
REF = os.path.join(gen.OUT2, "reference_cast_sheet_b3.jpg")
P = ("Rich, highly detailed oil-painting style classic fantasy storybook COVER illustration, portrait, textured brushwork, magical dusk light, warm and adventurous, no text, no lettering. "
     "Dusk on a snowy hill at the mouth of a dark cave among gray rocks. Across the cave mouth, strung between two rocks, runs a washing line, and from it hang dozens of tiny sleeping bats upside down, folded like little brown socks on a clothesline; a few bats are flying out against a violet sky with the first stars. "
     "Below, the children react candidly, none looking at the viewer: Scally (pointed ears, big old brown boots) stands on tiptoe reaching up to touch a hanging bat-sock, grinning; Wen (East Asian boy, dark blue coat) holds a strange copper funnel listener up to the cave; Pip (small, red cap) points up wide-eyed; Hopsi (hops wreath, pointed ears) watches thoughtfully; Hal (brown tousled hair, NOT red, slate under his arm) crouches taking notes; Titch (red cap) and Tabitha (a dark-brown-skinned girl with curly black hair in a bun and a rust headband) stand close; Gucci the young gray wolf sniffs the snow. Exactly seven children and one wolf and absolutely no adults. Arrange them loosely at different heights and distances, some seen from behind, in a natural cluster, not in a line. "
     "Use the reference painting only for how the characters look; every human except Scally and Hopsi has round ears. Leave the top fifth of the picture as calm sky for a title. ")
for n in (sys.argv[1:] or ["cover_a", "cover_b"]):
    gen.edit_with(n, REF, P, "2:3")
