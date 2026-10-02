# -*- coding: utf-8 -*-
"""One-shot Book 1 review fixes. Deletes itself only if the caller asks."""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "manuscript_text.txt"
text = p.read_text(encoding="utf-8")

pairs = []

pairs.append((
""" "That's inconvenient," he commented, as if the matter were primarily a filing error. He did not yet know that the joke was the correct diagnosis — and that the email was not a warning so much as Exhibit Zero, delivered early.""",
""" "That's inconvenient," he commented, as if the matter were primarily a filing error."""
))

pairs.append((
"""Across the empty room, Trevor Boltzman looked up. Trevor was twenty-eight, tall in the specific way that seemed designed to make doorframes personal, with the kind of permanently rumpled sandy hair that suggested he had once owned a comb and lost the argument with it. He was highly intelligent, technically qualified, and possessed of the unfortunate tendency to think about one problem at a time — a trait that made him excellent at mathematics and intermittently disastrous at life. When thinking deeply, he carried himself like a frozen Windows system before reboot. 
His voice usually carried a rising lift to it, like someone perpetually one sentence from an interesting discovery — the same lift that vanished entirely under real strain, replaced by something quieter and more careful. He sped up when he was anxious and slowed abruptly when he was certain, the gear-change audible before he had finished a sentence.
He had a sister, Tabitha, who was generally considered the more dangerous of the two. His phone lit, face-down, with her name. He turned it over, read one line, and put it back without answering. "If this were her problem," he muttered, not quite to Derek, "she'd already be asking the question I'm still phrasing."
""",
"""Across the empty room, Trevor Boltzman looked up. He was twenty-eight, tall enough that the doorframe had opinions about it, and his sandy hair had lost an argument with a comb before breakfast. He was still on the same problem he had been on when the email arrived, which was why the pencil in his hand had not moved.
His phone lit, face-down, with his sister's name. Tabitha was generally considered the more dangerous of the two. He turned it over, read one line, and put it back without answering. "If this were her problem," he muttered, not quite to Derek, "she'd already be asking the question I'm still phrasing."
"""
))

pairs.append((
"""Then the person was in there.
Obviously. They were either working hard... or shagging, equally hard.
There was no third possibility worth discussing. 
""",
"""Then the person was in there.
Working. Leave them. An open door was the absence. A closed door was the presence, and the presence did not require an audience.
"""
))

pairs.append((
"""Derek allowed. "There we are, then."
Penny's mouth had curved. Trevor had surveyed the two of them. 
Then at the quietly closed old door.
Then at Derek. 
Then at Penny. He had wisely remained silent.
""",
"""Derek allowed. "There we are, then."
Penny's mouth had curved. "The door was shut. You could have started there."
Trevor looked at the door, then at his own notes, and decided the notes were safer.
"""
))

pairs.append((
"""She tucked the cucumber under her coat like contraband — evidence first, and if the Bureau asked awkward questions later, personal use was a perfectly respectable second description. If two descriptions could share one object, Case 1047 could share one event. If not, they were raising Sophie on a superstition.
""",
"""She tucked the cucumber under her coat. Evidence first. Lunch, if the experiment failed. If two descriptions could share one object, Case 1047 could share one event. If not, they were raising Sophie on a superstition.
"""
))

pairs.append((
"""Trevor gestured towards it. "He's in there."
"Working?"
"Probably."
Penny smirked. "Or shagging."
Trevor pinched the bridge of his nose. "Please don't."
"Why?"
"Because I know what you're going to say."
Penny smiled. "Then you have excellent predictive powers."
""",
"""Trevor gestured towards it. "He's in there."
"Working?"
"The door is shut," Trevor said. "That is the entire report."
"Convenient."
"It is the rule. I did not invent it to spare your curiosity."
"""
))

pairs.append((
"""AND?
Jamie Lee Curtis survived Halloween.
THAT'S YOUR PHYSICS CONCLUSION?
Penny typed: My physics conclusion is that if different descriptions can encode the same underlying reality, SR and GR don't need to be fundamental to be true.
NOT BAD.
Then, a moment later: ALSO, JAMIE LEE CURTIS DID NOT "SURVIVE HALLOWEEN" IN THE PHYSICS SENSE.
You know what I meant.
I don't.
Americans.
That settles it.
""",
"""AND?
Penny typed: The film keeps every version. Physics doesn't. If two descriptions are of the same events, they still have to agree on what those events can do to Sophie.
NOT BAD. WHICH NUMBERS?
The ones that survive the change of description. Interval. Causal order. Not the costume, and not the poster.
I DIDN'T SEE A POSTER.
Neither did I. That was the useful part. SR and GR can both be true without either of them being the only story.
NOW YOU'RE TALKING.
"""
))

pairs.append((
"""Penny exhaled. It was not quite relief. Relief assumed the story had ended.
"Well, Sherlock," Weinstein began.
"Yes?"
Sherlock replied:
"No."
Weinstein raised an eyebrow. "What now?"
"The sequel."
Weinstein stared at the wall. "Of course."
And somewhere in London, Penny was taking the cucumber home.
The cucumber had been purchased for personal use.
Nobody cared to ask what sort of personal use.
Mrs Marsh ate her toast with Marmite and did not explain it. Weinstein, on the phone from Munich, asked what the black substance was. Nobody answered. The case was closed. The toast was not a clue.
""",
"""Penny exhaled. It was not quite relief. Relief assumed the story had ended.
"Well, Sherlock," Weinstein began. "Is the drawer shut?"
"The drawer is."
Weinstein raised an eyebrow. "And the corridor?"
"No."
Weinstein stared at the wall. He did not ask which door.
And somewhere in London, Penny took the cucumber home. It had done its job as an analogy. It was not going to be asked to become a wound on the way.
Mrs Marsh ate her toast with Marmite and did not explain it. Weinstein, on the phone from Munich, asked what the black substance was. Nobody answered. The case was closed. The toast was not a clue.
"""
))

pairs.append((
"""Also, Case 1047 is in Pending Geometry where it always belonged — Exhibit A, not a punchline. The cucumber can remain Exhibit B. I am not asking what Exhibit C was for.""",
"""Also, Case 1047 is in Pending Geometry where it always belonged — Exhibit A, not a punchline. The cucumber can remain Exhibit B. It is still lunch."""
))

pairs.append((
"""Weinstein confirmed, with visible reluctance, that this was correct — a few tens of billionths of a second, the going rate for spending a week rather further from the ground — and complained that of all the people in his life to grasp general relativity unprompted, it had to be the one planning to spend a week doing nothing with it. "I'm not doing nothing," Penny said. "I'm doing nothing, further up than you are, which technically counts."
""",
"""Weinstein confirmed, with visible reluctance, that the flight was the part that counted — about twenty billionths of a second, for the hours she would actually spend at altitude, not for a week of sitting on a terrace — and complained that of all the people in his life to grasp general relativity unprompted, it had to be the one planning to spend the rest of that week doing nothing with it. "I'm not doing nothing," Penny said. "I'm doing nothing after being, briefly, further up than you are. The briefly is the part that counts."
"""
))

pairs.append((
"""Nobody ever worked out who had sent Tabitha that message from Trevor's number, or how they'd known to send it eleven minutes before a train that, officially, did not exist pulled into a platform that also did not exist. Trevor checked his phone's sent folder every time he picked it up, and found nothing. Penny suggested filing it under Pending Geometry, alongside the singularity and the cucumber. Derek suspected, without being able to prove it, that this particular drawer was going to need reopening sooner rather than later.
Derek never worked out how a note in his own handwriting had ended up inside Case 1047, warning him to keep Trevor away from a clock neither of them had found yet, in a hand he had no memory of using. He filed the question next to the others, on the grounds that a man who already owned one photograph of himself face-down on a floor was not obliged to go looking for a second mystery involving his own handwriting. Trevor, for his part, remained unconvinced he'd been fairly represented, and spent the rest of his professional life approaching every clock in the building with the particular caution of a man who had once been warned off one by name.
Sophie's own brass clock — the one in her father's study, permanently and precisely four minutes fast — never made it into any official filing at all, mostly because nobody thought to ask a twelve-year-old for her evidence. She kept testing it anyway, on the grounds that someone in the family should keep a proper notebook, and filed the omission under the same heading her father would have used, had he known to: Pending Geometry.
""",
"""Two questions stayed open, and he left them open. Someone had texted Tabitha from Trevor's number, eleven minutes before a train that did not exist reached a platform that did not exist. Trevor checked his sent folder every time he picked up the phone, and found nothing. A note in Derek's own handwriting had turned up inside Case 1047, warning him to keep Trevor away from a clock neither of them had found yet. Trevor, unconvinced he had been fairly represented, gave every clock in the building the caution of a man who had been warned off one by name. He did this for the rest of the week. The week was as far as either of them was willing to look.
Sophie's own brass clock — the one in her father's study, permanently and precisely four minutes fast — never made it into any official filing at all, mostly because nobody thought to ask a twelve-year-old for her evidence. She kept testing it anyway. Seventeen times already: four minutes, never more, never less. Someone in the family, she had decided, should keep a proper notebook.
"""
))

pairs.append((
"""a notebook Sophie kept for seventeen weeks.""",
"""a notebook Sophie kept, and tested seventeen times."""
))

pairs.append((
"""Module B
Gravity as Geometry (Lessons 4-7):
 GR
Free Fall
Singularities
Why SR and GR Don't Fight
Module C
Labels, Paths, Experiments (Lessons 8-10):
Coordinates
Worldlines
Length Contraction
Module D
Dual Descriptions (Lessons 11-13):
Holographic Principle
Metaphor vs. Multiverse
Tidal Force
""",
"""Module B
Gravity as Geometry (Lessons 4-7, and Lesson 13):
 GR
Free Fall
Singularities
Why SR and GR Don't Fight
Tides, taught later, when Chapter 14 needs them
Module C
Labels, Paths, Experiments (Lessons 8-10):
Coordinates
Worldlines
Length Contraction
Module D
Dual Descriptions (Lessons 11-12):
Holographic Principle
Metaphor vs. Multiverse
"""
))

pairs.append((
"""Lesson 13
Curved Corridors and Tides
Module D · Dual Descriptions
""",
"""Lesson 13
Curved Corridors and Tides
Module B · Gravity as Geometry
"""
))

pairs.append((
"""Before the harder material: Lesson 14 established that causal order - what can affect what - is frame-independent, even though simultaneity for spacelike-separated events isn't. Keep that distinction in your pocket. The equation below is what actually enforces it, mathematically.
""",
"""Before the harder material: Lesson 14 established that causal order — what can affect what — is frame-independent, even though simultaneity for spacelike-separated events isn't. Keep that distinction in your pocket. The light cones come from the metric. The equation below relates that metric to matter and energy. It does not, by itself, invent the rule that a cause stays in the past of its effect.
"""
))

pairs.append((
"""That distinction explains the case, clue by clue. 11:17 and 12:04 were departure and arrival coordinates for the mysterious train, assigned within whatever description produced the impossible station; 
Derek's own watch, ticking his own proper time throughout, read 11:18 — a completely ordinary clock doing a completely ordinary job. The record itself did not arrive from the future. It arrived through the same anomalous geometry responsible for the extra doors and the impossible station elsewhere in this book, filed according to its own event coordinate rather than Derek's local proper time.
None of this required the Bureau's computer to predict anything. It required only that it confuse two different kinds of "when" — exactly the confusion this entire investigation turned out to be.
""",
"""That distinction explains the case, clue by clue. The file printed three times and no nouns. Penny wrote death, departure, and arrival in the margin, and the team treated her guesses as the file's verdict until Chapter 16. The office and the platform stayed two places. The file had treated them as one noun, and the file was wrong about the noun. 11:03, 11:17, and 12:04 were labels in that wrong description, not three measurements of one room.
Derek's own watch, ticking his own proper time throughout, read 11:18 — a completely ordinary clock doing a completely ordinary job. The record itself did not arrive from the future. It arrived through the same anomalous geometry responsible for the extra doors and the impossible station elsewhere in this book, filed according to its own event coordinate rather than Derek's local proper time.
None of this required the Bureau's computer to predict anything. It required a label to be read as a measurement, and two places to be read as one noun. That was the confusion this entire investigation turned out to be.
"""
))

pairs.append((
"""White Hole. The time-reverse of a black hole in the equations: a region from which matter and light can only emerge, never enter. A mathematical solution, not an observed object. Not a clue in Case 1047.
""",
"""White Hole. The time-reverse of a black hole in the equations: a region from which matter and light can only emerge, never enter. A mathematical solution, not an observed object. Lesson 6 names it so the Underground's bad day is not promoted into one.
"""
))

pairs.append((
"""Wormhole. A hypothetical connection between otherwise separate or distant regions of spacetime. Some solutions of general relativity contain wormholes, but traversable versions typically require exotic stress-energy. Mathematical availability does not guarantee a usable passage. Not a clue in Case 1047.
""",
"""Wormhole. A hypothetical connection between otherwise separate or distant regions of spacetime. Some solutions of general relativity contain wormholes, but traversable versions typically require exotic stress-energy. Mathematical availability does not guarantee a usable passage. Lesson 6 names it so the impossible station is not promoted into one.
"""
))

for i, (old, new) in enumerate(pairs, 1):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"pair {i} count {n}")
    text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8", newline="\n")
print("replacements", len(pairs))
