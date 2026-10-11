"""Full read-through fixes for Book 2 (11 Oct 2026, PT). Edits the docx master in place.
Usage: python readthrough_2026-10-11.py IN.docx OUT.docx
Each edit replaces one exact phrase inside one paragraph and must match exactly once."""
import sys, docx
from docx.oxml.ns import qn

EDITS = [
 # Prologue: the mug on the folder was Derek's (Penny poured it)
 ("He lifted Penny’s mug off it first.", "He lifted the mug off it first."),
 # Ch1: Penny's tea was poured before ten; a kettle cannot click off at 10:22
 ("The kettle clicked off in the corner. Somebody had boiled it for a closed file, out of habit, sometime before the sheet had appeared; it had taken this long to notice. Derek did not pour it. A kettle was for tea and for cases that had finished. He was not prepared to tell it which this was.",
  "The kettle ticked in the corner as it cooled. Penny had boiled it for a closed file before the sheet appeared, and the four mugs she had poured were going cold where she had left them. Derek did not touch his. A kettle was for tea and for cases that had finished. He was not prepared to tell it which this was."),
 # Ch1: Book 1 has the revocation at SUN 01:33, the second one
 ("Its share was revoked at half past one on Sunday morning,", "Its share was revoked at 01:33 on Sunday morning, in the second of the two one o’clocks,"),
 # Ch1: sets up Ch10's "the sum about the other side of the Sun"
 ("light would cover about three hundred and six million kilometres in it.”", "light would cover about three hundred and six million kilometres in it. That’s past the far side of the Sun.”"),
 # Ch1: Tabitha is a solicitor (Book 1); why she is at home on a Monday
 ("She answered on the third ring, from home, already on a different subject.", "She answered on the third ring, from home, where she had a brief to read and was not reading it, already on a different subject."),
 # Ch4: the order was dictated in the office at 10:22, not on the stairs at ten
 ("He had what Penny had taught him on the stairs at ten o’clock: the order things were in.", "He had what Penny had made Trevor write on an envelope at twenty past ten: the order things were in."),
 # Ch4: Sophie's text never said she would not write it down
 ("She’s said she won’t write it down, and she’s right not to.", "She hasn’t fetched it back, and she’s right not to."),
 ("Twice in a morning.", "Twice in one day."),
 # Ch5: the Sunday-morning photograph cannot have lived in the bag since the old Tuesday
 ("put the itinerary back in her handbag under the face-down photograph, where it had lived since the old Tuesday.", "put the itinerary back in her handbag, under the face-down photograph."),
 # Ch6: Weinstein leaves on Monday, so not "a week"
 ("Alfred told me on Saturday that he was staying in London to be polite for a week, and I told him he had never in his life been polite for a week,",
  "Alfred told me on Saturday that he was staying in London until Monday to be polite, and I told him he had never in his life been polite for three days together,"),
 # Ch9: Tuppence says the hangers are in Sophie's room
 ("Julian’s hangers are in the hall, in case you were about to ask whose life is whose.", "Julian’s hangers are in my wardrobe, in case you were about to ask whose life is whose."),
 # Ch12: the printed back of the sheet must match this note word for word (Ch22)
 ("PLEASE NOTE. THE PREVIOUS WARNING ARRIVED AFTER THE ACT.", "PLEASE NOTE. THE PREVIOUS WARNING WAS SENT TOO LATE."),
 # Ch12: show the recipient line before Penny deletes it (clue fairness)
 ("The train, behind it, held its breath, if trains had breath, which this one appeared to.",
  "The train, behind it, held its breath, if trains had breath, which this one appeared to. Under the new sentence, on the line Trevor had filled at lunch because the Bureau wrote down whatever a board said, the recipient field still read SOPHIE."),
 # Ch12: the kettle is in the office corner
 ("said nothing useful, and went to the kitchen. They heard the kettle go on.", "said nothing useful, and went to the kettle in the corner and switched it on."),
 # Ch13: Mrs Marsh's kettle is in the lodge (Book 1)
 ("I was in the kitchen downstairs with the kettle on.", "I was in the lodge downstairs with the kettle on."),
 # Ch14: she rings him on Tuesday evening (Epilogue)
 ("“Tomorrow. In the daytime. When it’s not the same day as the railway.", "“Tomorrow. When it’s not the same day as the railway."),
 # Ch15: Hafele and Keating published two short papers (Science 177, 166-170)
 ("It’s two pages. It’s the best two pages in the world.", "It’s two short papers. The best few pages in the world."),
 # Ch15: in at seven, up at about ten
 ("got up for the first time in two and a half hours,", "got up for the first time in nearly three hours,"),
 # Ch16: Sherlock's "No." came at Paddington, after lunch
 ("It was the word Sherlock had sent at lunch, he realised,", "It was the word Sherlock had sent that afternoon, he realised,"),
 # Ch17: the sum is done in ink
 ("Then he got out his phone and did Penny’s sum again,", "Then he got out his pen and did Penny’s sum again,"),
 # Ch19: grammar
 ("the manner of someone sent to look at a great many damp patches and has never yet found one that was his fault.", "the manner of someone who has been sent to look at a great many damp patches and has never yet found one that was his fault."),
 # Ch21: the guidebook is new here; Mrs Marsh collects the paper at 18:35 (Epilogue)
 ("Penny, at her desk, put down the guidebook.", "Penny, at her desk, put down her guidebook to Greece."),
 ("before I lock that drawer at half past six.", "before I lock that drawer at a quarter to seven."),
 # Ch22: the printout must match the Prologue heading word for word
 ("RELATIVISTIC INVESTIGATION BUREAU. STATUS OF CASE: NOT YET OCCURRED.", "RELATIVISTIC INVESTIGATION BUREAU. CASE STATUS: NOT YET OCCURRED."),
 # Ch22: Penny left four minutes earlier; she is not home yet; the BR form is in the basement
 ("She answered with the sound of a cupboard shutting.", "She answered over the sound of a bus pulling away."),
 ("He checked. Then she stayed on the line while he read the British Rail delivery instruction aloud. Neither of them called it an instruction to board.",
  "He checked. Nothing was left over. She stayed on the line a moment longer than either of them needed, and rang off."),
 # Ch22: on Monday he stood on the yellow line on his own carpet; the sill was not crossed
 ("He had crossed onto it to refuse on Monday.", "On Monday he had stood on its yellow line, on his own carpet, to refuse."),
 ("He walked past it to the yellow line. Three paces. It felt much further.", "He walked past it, along the yellow line, towards the leading carriage. Three paces. It felt much further."),
 ("The three paces were along the platform, towards the leading carriage, not out across its width. The bench stood beside that route. Between the yellow line and the open doorway there was only the narrow strip he had faced on Monday. From here he could reach the end of the first seat. Reaching it would put his hand and shoulder inside. Boarding would put his feet there too.",
  "Between the yellow line and the carriage there was only the narrow gap he had faced across his own carpet on Monday. From here, with both feet on the slabs, he could reach the first seat. Reaching was not boarding. Boarding would put his feet in there too."),
 # Ch22: the sheet's arrival is unobserved; it was under the folder
 ("THIS DESK, MONDAY, BETWEEN 09:58:12 AND THE OPENING OF THE DOOR. ONCE.", "THIS DESK, MONDAY MORNING, UNDER THE 1047 FOLDER, BEFORE THE DOOR OPENED. TIME UNKNOWN. ONCE."),
 # Epilogue: Trevor had gone down to move the Mini
 ("He went the long way, through the park, and did not look at any clocks,", "He drove the long way, round the park, and did not look at any clocks, the one on the dashboard included,"),
 # Epilogue: Sophie does not know the Bureau's "nearest name" jargon, and must not learn her name was on the board
 ("She thought about that for the length of a lamp-post. “That’s the worst answer I’ve ever heard. And you didn’t put the nearest name in.”", "She thought about that for the length of a lamp-post. “That’s the worst answer I’ve ever heard.”"),
 ("“Not even mine.”", "“It’s the true one.”"),
 ("“Good. I’d hate to be the nearest name.”", "“Mr Okafor says the true ones usually are.”"),
 # Lessons: at the opening the sheet was in Derek's hand, not yet in his pocket
 ("The sheet was already in the pocket, and the room’s order is sheet,", "The sheet was already in Derek’s hand, and the room’s order is sheet,"),
 ("the sheet was already in the pocket before the door,", "the sheet was already in Derek’s hand before the door,"),
 ("The morning sheet was already in the pocket. Acts have times.", "The morning sheet was already in Derek’s hand before the door opened. Acts have times."),
 ("Hawking’s chronology protection conjecture says the laws of physics forbid them.", "Hawking’s chronology protection conjecture proposes that the laws of physics forbid them."),
]

def replace_in_par(p, old, new):
    runs = p.runs
    text = ''.join(r.text for r in runs)
    i = text.find(old)
    if i < 0: return False
    # locate runs covering [i, i+len(old))
    pos = 0; first = last = None; starts = []
    for k, r in enumerate(runs):
        starts.append(pos); pos += len(r.text)
    j = i + len(old)
    for k, r in enumerate(runs):
        s, e = starts[k], starts[k] + len(r.text)
        if first is None and e > i: first = k
        if s < j: last = k
    fr = runs[first]; off = i - starts[first]
    if first == last:
        fr.text = fr.text[:off] + new + fr.text[off + len(old):]
    else:
        lr = runs[last]; loff = j - starts[last]
        fr.text = fr.text[:off] + new
        lr.text = lr.text[loff:]
        for k in range(first + 1, last): runs[k].text = ''
    return True

def main(src, dst):
    d = docx.Document(src)
    for old, new in EDITS:
        hits = [p for p in d.paragraphs if old in ''.join(r.text for r in p.runs)]
        full = [p for p in d.paragraphs if old in p.text]
        assert len(hits) == 1 and len(full) == 1, (len(hits), len(full), old[:70])
        assert replace_in_par(hits[0], old, new)
    d.save(dst)
    print(len(EDITS), 'edits applied')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
