"""Tightening and humour pass for Book 2 (11 Oct 2026, PT): the Monday-night and Tuesday chapters (15-21).
Edits the docx master. Usage: python tighten_2026-10-11.py IN.docx OUT.docx
EDITS replace one exact phrase in one paragraph (must match exactly once).
DELETES remove one whole paragraph, found by its exact full text (must match exactly once).
Clues kept: the sum and DO NOT SEND BEFORE, the voice's register, the newspaper, MYSTERIOUS (OTHER),
note 7 on the back of PL/9, the 09:58:12 photograph, the ring and the fold."""
import sys, docx

EDITS = [
 # Ch15: shorter, and a joke in place of the explanation
 ("It annoyed her more than she could reasonably account for. He had done it upside down, in his head, in the time it took to put a ticket away, and she had done it with a biro over twenty minutes, and they had got the same number. Very smart and very lazy, Herbert called it. Weinstein quoted it about himself with something not far from pride.",
  "It annoyed her more than she could reasonably account for. He had done it upside down, in his head, in the time it took to put a ticket away; she had done it with a biro over twenty minutes; they had got the same number. Herbert called that very smart and very lazy. Weinstein had more or less had it engraved."),
 ("He rang off. She sat with the phone in her hand, and the kettle she had boiled at seven and forgotten, and the rain on the window, and a train somewhere across London in a doorway on the second floor of an old building, with Derek sitting in front of it with the face.",
  "He rang off. She sat with the phone in her hand, the kettle she had boiled at seven and forgotten, and the rain, and somewhere across London a train in a doorway with Derek sitting in front of it, doing the face at it."),
 ("She thought about ringing him. He had said he would ring if it did anything. He had said nothing about ringing if it did nothing, and she had told him to ring her if it didn’t, and he had not, which meant that it was not doing anything and he was being Derek about it. She left him alone. It was, she thought, the kind of help he was best at accepting.",
  "She thought about ringing him. He had promised to ring if it did anything. He had not rung, which meant it was doing nothing and he was being Derek about it. She left him alone. It was the kind of help he was best at accepting."),
 # Ch16: a joke for the empty evening; trims
 ("He rang out for nothing and ate nothing.",
  "He thought about ordering food, and could not face giving a delivery driver directions that ended at a railway on the second floor, so he ate nothing."),
 ("He read it three times. He found that it was, in its way, the best thing anyone had said to him all day, and that it was a report about a dog. He typed a reply and deleted it, and typed another and deleted that, and then remembered the pavement at Paddington and the sentence he had already said, and that it did not need saying again in a text message at half past ten to a woman who had already heard it.",
  "He read it three times. It was the best thing anyone had said to him all day, and it was a report about a dog. He typed a reply and deleted it, and then remembered the pavement at Paddington and the sentence he had already said there, which did not need saying again by text at half past ten."),
 ("Then he turned off the desk lamp. The office went dark, and the platform did not, and he stood for a moment in the light from a train that was going nowhere, in a room lit from the other side of a sill, and found that he was not afraid of it. He was not reconciled to it. He was simply not afraid.",
  "Then he turned off the desk lamp. The office went dark and the platform did not, and he stood for a moment in the light of a train that was going nowhere and found that he was not afraid of it. Not reconciled. Simply not afraid."),
 ("On this corridor an open door meant that nobody knew where you had gone. He had written that rule himself. He went out through the outer room, and down the stairs, past the step where Mrs Marsh had sat, and out into the street, and he walked home, because he walked; he had no licence, and there was no one on the pavement to mention it to.",
  "He went out through the outer room and down the stairs, past the step where Mrs Marsh had sat, and walked home, because he walked; he had never held a licence, and at that hour there was nobody on the pavement to explain it to."),
 # Ch17: give the scene its goal at once (without spoiling what the question is)
 ("He sat at his desk with the blotter in front of him and his jacket on, because he always had his jacket on, and he did not open any of the patent files that were waiting for him. There was a dishwasher in one of them that claimed to clean plates using sound alone. He had been looking forward to the dishwasher for a week. He found, this morning, that he could not make himself care whether it worked.",
  "He had been at his desk since six, in his jacket, because he was always in his jacket, trying to settle one question before anybody arrived to ask it for him. He had not opened the patent files. There was a dishwasher in one of them that claimed to clean plates using sound alone, and he had been looking forward to it for a week. This morning he could not make himself care whether it worked, which worried him more than the railway had."),
 ("Hawking would say the universe does not permit this kind of story at all.", "Hawking suspected the universe does not permit this kind of story at all."),
 ("Weinstein thought about it. He thought about the barrier at Paddington, and turning round once, and Derek’s face, and Penny’s face, and a little girl he had met last week and understood better this week who refused to write down headings she had not read.",
  "Weinstein thought about the barrier at Paddington, and turning round once, and a girl he had met last week who refused to write down headings she had not read."),
 # Ch18: trims and a sharper line
 ("“And then a sheet arrives before a door, and a voice comes after, and they look at the wire for the answer, and the wire says nothing. YESTERDAY. Not a date. A direction. It is the most honest railway in Europe. I should like to meet whoever designed it.”",
  "“Then a sheet arrives before a door, and they look at the wire for the answer, and the wire says nothing. YESTERDAY. Not a date; a direction. The most honest railway in Europe. It has never once promised to arrive. I should like to meet whoever designed it.”"),
 ("“Monday. He told me on the telephone that he nearly stayed. He went through the barrier at four and turned round once and did not come back. Staying would have been a tenancy. It was the cleanest act of the day, until Mr Gent’s. Do not tell him I said he was right. Tell him the hurry was. He will know the difference, and it will annoy him.”",
  "“Monday. He nearly stayed. Staying would have been a tenancy. Do not tell him I said he was right. Tell him the hurry was. He will know the difference, and it will annoy him.”"),
 ("He wrote four hundred words, and found that they explained the joke, and deleted them. He wrote two hundred, and found that they agreed with Herbert, and deleted those too.",
  "He wrote four hundred words, found that they explained the joke, and deleted them. He wrote two hundred, found that they agreed with Herbert, and deleted those faster."),
 # Ch19: the laser across the opening only reaches the platform if it is turned through the opening
 ("If you pointed it one inch further, it’d come back off the platform,", "If you turned it a few degrees, through the opening, it’d come back off the platform,"),
 # Ch20: the insurers' letters already exist by five; the laugh Ch22 remembers
 ("By five o’clock two insurance companies would think a great deal of it.", "By five o’clock it would turn out that two insurance companies had already thought a great deal of it."),
 ("“That isn’t a rule,” said Penny. “That’s a confession.”", "“That isn’t a rule,” said Penny. “That’s a confession.” Everybody laughed, Mr Pendleton last and least certainly."),
 # Ch21: ten o'clock is near the start of the interval, not the middle; speaker tags
 ("“Ten o’clock is in the middle of it,” said Mr Haskett.", "“Ten o’clock is inside it,” said Mr Haskett."),
 ("“It’s eight minutes wide and ten o’clock is in the middle.”", "“It’s eight minutes wide and ten o’clock is sitting in it like a lodger.”"),
 ("“One for each insurer.”", "“One for each insurer,” said Mr Haskett."),
 ("“Both for you. In case you read it once.”", "“Both for you,” said Mrs Marsh. “In case you read it once.”"),
 ("Trevor put the phone away. At ten past six he glanced at the window,", "At ten past six Trevor glanced at the window,"),
 # Ch15: further trims; a grammar slip
 ("She read it to him. Height, gravity, the speed of light. Speed, the speed of light. Four point three in, one and a quarter out, three and a half hours, ten and a half nanoseconds. Weinstein’s number. She read it in the voice she used for reading out flight times, so that he would not hear that it mattered.",
  "She read it to him in the voice she used for flight times, so that he would not hear that it mattered: four point three in, one and a quarter out, three and a half hours, ten and a half nanoseconds. Weinstein’s number."),
 ("Penny considered the ten and a half on the itinerary, and the x3 in the margin beside it, and at the four of them standing against the sugar bowl.",
  "Penny looked at the ten and a half on the itinerary, and the x3 beside it, and the four of them standing against the sugar bowl."),
 ("A silence came down the line. It went on long enough that she thought for a moment the call had dropped, and then she heard him breathing, slowly, as he breathed when he was standing at the edge of a thing and deciding whether to say it.",
  "A silence came down the line, long enough that she thought the call had dropped. Then she heard him breathing slowly, as he did at the edge of a thing he was deciding whether to say."),
 # Ch18: Herbert arrives with a goal, which the scene then pays off ("You may not take away the cone")
 ("He had made one anyway. He regarded the plaque as an opinion, and he had never in his life allowed an opinion on a door to alter his behaviour on the step.",
  "He had made one anyway. He regarded the plaque as an opinion, and he had never in his life allowed an opinion on a door to alter his behaviour on the step. He had also come with one purpose, written on a card in his breast pocket so that he could not be talked out of it: THE RULER MAY GO. THE CONE STAYS."),
 # Ch16, Ch18, Ch21: more slow beats cut
 ("The platform at night was not much different from the platform at ten in the morning. That was the first thing he noticed. The lamp at the far end had not got brighter. The lit windows of the carriage had not changed. The white clock on the far pillar went round at the same rate as every clock in London, as Trevor had shown it did, and told the time it had been telling all day.",
  "The platform at night was the platform at ten in the morning. The lamp had not got brighter, the lit windows had not changed, and the white clock on the far pillar went round at the same rate as every clock in London, as Trevor had shown it did."),
 ("“Of course he does. He was holding it. People always want to be the before; it is the only position in a story that cannot be blamed for arriving late.” Barbarian shook his head, slowly, with every appearance of affection. “Tell him he is in the order, and that is honour enough for anyone. He was there for the sheet. That is all.”",
  "“Of course he does. He was holding it. People always want to be the before; it is the only position in a story that cannot be blamed for arriving late.”"),
 ("Herbert let himself out. On the step he looked at the plaque again, and thought about appointments, and decided that he had kept this one, and that the keeping had been entirely his own affair.",
  "Herbert let himself out. On the step he took the card out of his breast pocket, read it, and put it back. Both halves had held."),
 ("Penny got up and came round her desk. She did not come too close; she stood beside the filing cabinet, with one hand on the top of it, in the place where she had stood on Monday when the board had flickered.",
  "Penny got up and stood by the filing cabinet, one hand on top of it, where she had stood on Monday when the board flickered."),
]

DELETES = [
 # Ch15: the Herbert/Weinstein exchange said twice
 "“He’d say it was lazy.”",
 "“Herbert would say that. Weinstein would agree with him and be pleased about it.”",
 "That was true, and she did not want it to be, and she let it go.",
 # Ch16: a slow beat after the best line of the scene
 "The phone buzzed once more. He did not turn it over. He knew roughly what it would say, and he found he did not need to know exactly; that it could wait until the morning, and be read in the morning, and be no less true for being read late.",
 # Ch21: repeats Derek's thought from a page earlier
 "Trevor sat down on the floor again by the filing cabinet and studied the photograph on his phone, the shut door behind the bottle, at nine fifty-eight and twelve seconds. “That’s the last picture of it. Before.”",
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
    for text in DELETES:
        hits = [p for p in d.paragraphs if p.text == text]
        assert len(hits) == 1, (len(hits), text[:70])
        el = hits[0]._element; el.getparent().remove(el)
    d.save(dst)
    print(len(EDITS), 'edits,', len(DELETES), 'paragraphs removed')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
