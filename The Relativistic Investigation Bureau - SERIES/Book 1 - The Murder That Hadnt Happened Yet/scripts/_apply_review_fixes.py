# -*- coding: utf-8 -*-
"""Apply the review fixes to manuscript_text.txt. One-shot."""
from pathlib import Path

p = Path(__file__).resolve().parent / "manuscript_text.txt"  # build source lives in scripts\
t = p.read_text(encoding="utf-8")

reps = [
(
"""The murder had not happened yet. This would have been unremarkable, except that Derek Gent was already dead on paper—and someone had remembered to file the necessary forms.
The time of death had been entered. The location had been entered. The victim had been identified.
The victim was Derek Gent. Derek was alive. He was also the sort of man who noticed discrepancies in official paperwork. This particular discrepancy was rather difficult to ignore. 
The paperwork predicted his death a day before it was due to occur. Derek therefore did what any sensible investigator would do.
He checked the date, then the time, then the old clock.
Then the clock again, because the first check had produced a result he found professionally inconvenient. The mysterious clock had stopped.
When Derek found a murder notice announcing his own future death, he did not immediately conclude that he was being hunted by a time traveller, a quantum ghost or an unusually vindictive neighbour. He began with the evidence.
A stopped clock.
A future date. 
A murder that had not happened.
There was only one sensible response. Investigate.""",
"""A form can be finished before the event it names. Derek Gent had not learned that yet. He would, on a Tuesday, when the form used his name.
This page is the rule he should have started with. The email, the photograph, and the clock belong to the next one. They are not repeated here.
There was only one sensible response. Investigate."""
),
(
"""She was also one of those people who always appeared to have been designed specifically to make other people lose their train of thought. She was a striking brunette, though Derek had never used the word in her presence because he valued his life and had no particular desire to become the subject of a police report — or worse, a footnote. She wore a dark coat, carried a handbag, and had the calm expression of someone who had already dealt with several irritating people before breakfast and was prepared, if necessary, to deal with several more.""",
"""She wore a dark coat, carried a handbag, and had the calm expression of someone who had already dealt with several irritating people before breakfast and was prepared, if necessary, to deal with several more. Derek had learned not to describe her. Descriptions were how he lost arguments."""
),
(
"""Penny enlarged the lower-right corner of the image. She did not speak for a long time. The three lines sat there like a spell the Bureau had not meant to cast: Death. Departure. Arrival.
There was something in the lower-right corner. A piece of paper.
Penny zoomed in. It contained three lines.
11:03 - DEATH
11:17 - DEPARTURE
12:04 - ARRIVAL
Below them:
DO NOT TRUST THE CLOCKS.""",
"""Penny enlarged the lower-right corner of the image. She did not speak for a long time. Three times, and no verbs.
There was something in the lower-right corner. A piece of paper.
Penny zoomed in. It contained three lines.
11:03
11:17
12:04
Below them:
DO NOT TRUST THE CLOCKS.
She wrote in the margin, because a form with no nouns was worse than a blank. She did not pretend the file had agreed.
11:03 — if this is a death
11:17 — if this is a departure
12:04 — if this is an arrival"""
),
(
"""Everyone went quiet. The photograph.
11:03 - DEATH
11:17 - DEPARTURE
12:04 - ARRIVAL
Derek took out the photograph.""",
"""Everyone went quiet. The photograph. Three times. Penny's margin still said death, departure, arrival, and the file still had not.
11:03
11:17
12:04
Derek took out the photograph."""
),
(
"""Derek studied the photograph again.
11:03 - DEATH
11:17 - DEPARTURE
12:04 - ARRIVAL
Then he noticed something he hadn't noticed before.""",
"""Derek studied the photograph again. The three times. Her three guesses beside them, still guesses.
11:03
11:17
12:04
Then he noticed something he hadn't noticed before."""
),
(
"""Derek stared at the ancient brass clock. \"But ours stopped at eleven seventeen.\"""",
"""Derek looked at the office clock on the wall, not at the brass one, which still read eleven-oh-three and seventeen seconds. \"The wall stopped at eleven seventeen.\""""
),
(
"""What was unusual was the film she chose: Everything Everywhere All at Once. She settled into her seat with popcorn and sat upright. "Blimey." The film was the wrong kind of multiverse — drawers you could open at will, every branch kept crisp for the joke. Penny decided the question it was allowed to answer for the case wasn't "are there many worlds" but "which observables must agree — and which future of Sophie are we accidentally voting for when we pick a description?"
Real physics was ruder. A superposition didn't survive contact with air, light, a countertop, or Trevor's opinions; decoherence smeared the interference away. That, she suspected, was why nobody had ever caught the brass clock mid-superposition, dead and standing at once. By the time light left it and reached a camera, the argument was already over.""",
"""What was unusual was the film she chose: Everything Everywhere All at Once. She settled into her seat with popcorn and sat upright. "Blimey." The film was the wrong kind of multiverse — drawers you could open at will, every branch kept crisp for the joke. The question she would allow it was narrower. Which numbers have to agree, whoever is describing them? And which future of Sophie gets voted for when a description is picked?
The film wanted the brass clock dead and standing at once. Penny did not believe the room would permit it. By the time light left an object and reached a camera, the argument was already over. She did not yet know the name for that. She knew the camera had won."""
),
(
"""The canteen was serving meat with mint sauce, chocolate sauce, a third unlabelled bottle that was not soy sauce but had clearly attended the same finishing school as Maggi, and a small jar of Marmite left out for reasons nobody would take responsibility for — a combination several members of staff quietly agreed was a more serious violation of natural law than anything in Case 1047. Weinstein, calling from Munich and catching sight of a photograph Penny had unwisely sent him, wanted to know what, precisely, Marmite was, and why it was black, and why anyone would do that to toast on purpose. Nobody could produce an answer that satisfied him, largely because none of them had ever considered the question settled enough to need one. Mrs Marsh ate hers without comment, Marmite included, which everyone found more alarming than the sauces.""",
"""Mrs Marsh ate her toast with Marmite and did not explain it. Weinstein, on the phone from Munich, asked what the black substance was. Nobody answered. The case was closed. The toast was not a clue."""
),
(
"""Trevor took to walking home through Holland Park after dark, on the theory — unproven, and never to be tested again — that a man who had personally witnessed the collapse of simultaneity ought to be able to handle an unlit footpath in Notting Hill. Somewhere near the bandstand, a stranger on a bicycle whistled at him and pedalled off before Trevor could construct a suitable retort. By the time the reply arrived, fully formed and reasonably witty, the stranger had already left whatever light cone might have delivered it to him — which Trevor decided, generously, made it a problem of physics rather than wit. He settled, a full block later, for muttering it to the empty park instead. "I'm flattered, obviously," he informed a duck, "and also extremely cold." The duck did not dignify this with a response, which Trevor felt was probably fair.""",
"""Trevor walked home through Holland Park after dark. A cyclist whistled and was gone before the retort arrived. Trevor let it go. The reply had left the light cone."""
),
(
"""Rule: Pending Geometry is the correct drawer. Some cases end not with an arrest, but with a kettle.

-> Lesson for this chapter: 16 - Capstone: The Clock Was Lying

Coming Next in the Relativistic Investigation Bureau Series""",
"""Rule: Pending Geometry is the correct drawer. Some cases end not with an arrest, but with a kettle.
He listened to the kettle. Case 1047 stayed closed while it boiled.

-> Lesson for this chapter: 16 - Capstone: The Clock Was Lying

Coming Next in the Relativistic Investigation Bureau Series"""
),
(
"""For the story alone: read the chapters and stop at each Rule. No plot point lives only in the lessons.
To take the class: read each chapter, then the lesson it points to. Lesson 1 assumes nothing; Lesson 16 assumes you have been paying attention.""",
"""For the story alone: read the chapters and stop at each Rule. You will know what the Bureau filed. You will not know why the filing was possible. That reason is the course.
To take the class: read each chapter, then the lesson it points to. Chapters 1 and 2 share Lesson 1. After that, each chapter points at one lesson, and the lesson points back. A lesson may mention another chapter where the same idea appears. That mention is not a second arrow. Lesson 1 assumes nothing. Lesson 16 assumes you have been paying attention."""
),
(
"""Three interactive demos — drag simultaneity, curvature, and cosmic expansion around until they behave — live at https://lotmus.github.io/relativistic-site/""",
"""Three demos, one job each, at https://lotmus.github.io/relativistic-site/ — simultaneity for Lesson 2, curvature for Lesson 5, and expansion so that "the universe stretches" is not filed under murder. The same address is repeated under Further Reading. It is not a fourth demo."""
),
(
"""Optional detour: You do not need this chapter to understand or solve the murder. It follows a thread from relativity into more speculative territory. Treat it as context, not evidence on the same footing as the Lorentz transformation.""",
"""The murder can be closed without this lesson. The course cannot. This is where a film stops being allowed to count as evidence. Treat what follows as a drill in metaphor, not as a second Lorentz transformation."""
),
(
"""The novel flags this as "depending on sign convention." The physics does not change. The drawer label does.""",
"""The novel flags this as "depending on sign convention." The physics does not change. The drawer label does. Symptom of mixing the forks: a timelike pair suddenly looks spacelike, or the invariant comes out negative when the other convention would have made it positive. Name the fork before you interpret the sign."""
),
(
"""Drive the direct road between two towns and you burn less petrol than the driver who takes the scenic route, even though both of you started and finished in the same two places. 
Nobody finds that paradoxical. 
The twin paradox runs on the same idea, but backwards: it's the scenic-route twin — the one who peels off towards the speed of light and comes back — who logs the fewer years, the way the direct-road driver logs the less petrol. The twin who stays on the direct, unaccelerated road through spacetime is the one who arrives having racked up more time, not less.""",
"""Do not explain this with petrol. On a road, the direct driver burns less fuel. In spacetime, the straight timelike path between two events accumulates more proper time, and the path that turns around accumulates less. The analogy runs backwards, which means it is the wrong analogy. Use the paths. The twin who stays takes the straight route and ages more. The twin who turns around takes the bend and ages less."""
),
(
"""If two inertial observers disagree about simultaneity, must one of their clocks be broken? No.""",
"""If two inertial observers disagree about simultaneity, must one of their clocks be broken?
No. The disagreement is what the frames are for. A broken clock is a different fault."""
),
(
"""Can two clocks follow different paths through spacetime and accumulate different proper times?
Yes.""",
"""Can two clocks follow different paths through spacetime and accumulate different proper times?
Yes. Proper time is the time along a path. Two paths between the same events need not carry the same amount of it."""
),
(
"""If Derek travels fast and reunites with Earth, can he have aged less than someone who stayed behind?
Yes.""",
"""If Derek travels fast and reunites with Earth, can he have aged less than someone who stayed behind?
Yes, if his path is the one that turned around. The clocks are not broken. The routes are unequal."""
),
(
"""Does a film about parallel universes establish a physical multiverse?
No.""",
"""Does a film about parallel universes establish a physical multiverse?
No. A story about many worlds is not a measurement that many worlds exist."""
),
(
"""If two events are causally connected, can an inertial observer simply transform them into the opposite temporal order?
No.""",
"""If two events are causally connected, can an inertial observer simply transform them into the opposite temporal order?
No. If a signal can run from one to the other, every inertial frame keeps that order."""
),
(
"""Here is what you can now explain, presumably.""",
"""Here is the list you should be able to say without this page in front of you. Any line you cannot say is unfinished."""
),
(
"""Congratulations!
You now understand the essential ideas. You may safely discuss relativity at dinner. Or you can have another piece of cake. The second option is generally shorter and, in Derek's experience, no less illuminating.""",
"""You have met the essential ideas. Meeting them is not the same as being able to say them. If dinner still requires this page, the lesson is not finished. Cake remains available, and it will not do the drill for you."""
),
(
"""Light Cone. The boundary between lightlike directions and the timelike or spacelike directions at an event. Its future and past portions show the local limits on where signals can go and where they can come from. Cucumbers must remain within the speed limit.""",
"""Light Cone. The boundary between lightlike directions and the timelike or spacelike directions at an event. Its future and past portions show the local limits on where signals can go and where they can come from."""
),
(
"""Decoherence. The suppression of observable quantum interference as a system becomes entangled with its environment. It helps explain why everyday objects — including cucumbers — behave classically. By itself, it does not explain why a measurement yields one particular outcome.""",
"""Decoherence. The suppression of observable quantum interference as a system becomes entangled with its environment. It helps explain why everyday objects behave classically. By itself, it does not explain why a measurement yields one particular outcome."""
),
(
"""Pending Geometry. The Bureau's filing category for an event that looks like a crime only if you insist on a shared, universal "now." Not a punchline: the correct drawer for a coordinate label mistaken for a corpse.""",
"""Pending Geometry. The Bureau's name for a file whose time-label and whose measurement will not sit in the same box. Read the case before you decide what the box contained."""
),
(
"""White Hole. The time-reverse of a black hole in the equations: a region from which matter and light can only emerge, never enter. A mathematical solution, not an observed object.""",
"""White Hole. The time-reverse of a black hole in the equations: a region from which matter and light can only emerge, never enter. A mathematical solution, not an observed object. Not a clue in Case 1047."""
),
(
"""Wormhole. A hypothetical connection between otherwise separate or distant regions of spacetime. Some solutions of general relativity contain wormholes, but traversable versions typically require exotic stress-energy. Mathematical availability does not guarantee a usable passage.""",
"""Wormhole. A hypothetical connection between otherwise separate or distant regions of spacetime. Some solutions of general relativity contain wormholes, but traversable versions typically require exotic stress-energy. Mathematical availability does not guarantee a usable passage. Not a clue in Case 1047."""
),
(
"""though several of her fictitious colleagues maintain that she understands it hopefully better than she does the Special One.""",
"""though several of her fictitious colleagues maintain that she understands it, she hopes, better than she does the Special One."""
),
(
"""Interactive demos: https://lotmus.github.io/relativistic-site/""",
"""Demos, and which lesson each one serves, are listed in How to Read. Address, once more, for anyone who skipped that page: https://lotmus.github.io/relativistic-site/"""
),
(
"""Then, free and online:
Stanford Gravity Probe B — Einstein, Lorentz, and Minkowski spacetime: https://einstein.stanford.edu/SPACETIME/spacetime2.html
Relativity Questions and Answers (length contraction and the rest of the desk): https://einstein.stanford.edu/content/relativity/qanda.html
Norton, Einstein for Everyone (the lecture notes in the Bibliography): https://sites.pitt.edu/~jdnorton/teaching/HPS_0410/index.html
Demos for this book: https://lotmus.github.io/relativistic-site/
The full shelf, with difficulties, is the Bibliography.""",
"""This list is the on-ramp, in reading order. The Bibliography is the full shelf. It starts with Einstein because that is the primary source, not because it is the place to begin.

Then, free and online. Accessed 30 September 2026:
Stanford Gravity Probe B essay (2007). Use it for Einstein, Lorentz, and Minkowski. It also teaches gravity with a rubber sheet, which Lesson 13 will not let you keep: https://einstein.stanford.edu/SPACETIME/spacetime2.html
Sten Odenwald's relativity questions, reprinted by Gravity Probe B. Objections, not the length-contraction drill. That drill is Taylor and Wheeler: https://einstein.stanford.edu/content/relativity/qanda.html
Norton, Einstein for Everyone. Open the contents and start at special relativity, not at the front door: https://sites.pitt.edu/~jdnorton/teaching/HPS_0410/index.html
The three demos named in How to Read: https://lotmus.github.io/relativistic-site/
The full shelf, with difficulties, is the Bibliography."""
),
(
"""Muller, Richard A. Now: The Physics of Time. W. W. Norton, 2016. COMMENT: A working physicist's attempt to explain why "now" feels so real when relativity insists it shouldn't be universal — which is, not coincidentally, the exact problem the Bureau spent a week mis-filing. Difficulty: Medium. Argues time's flow may be more fundamental than most physicists admit, which Weinstein would have opinions about.""",
"""Muller, Richard A. Now: The Physics of Time. W. W. Norton, 2016. COMMENT: A working physicist's account of why "now" feels real when relativity refuses a universal now. Difficulty: Medium. He argues that time's flow may be more fundamental than most physicists admit. That is a different programme from Barbour's."""
),
(
"""Cox, Brian, and Jeff Forshaw. Why Does E=mc²? (And Why Should We Care?). Da Capo Press, 2009. COMMENT: A patient, readable derivation of the equation everyone quotes and almost nobody can actually get to. Difficulty: Medium. Builds the result up from the same postulates this book keeps joking about, minus the dolphin.""",
"""Cox, Brian, and Jeff Forshaw. Why Does E=mc²? (And Why Should We Care?). Faber & Faber, 2009. The US edition is Da Capo Press, 2009. COMMENT: A patient derivation of the equation, from the same two postulates as Lesson 1. Difficulty: Medium."""
),
(
"""Susskind, Leonard. The Black Hole War: My Battle with Stephen Hawking to Make the World Safe for Quantum Mechanics. Little, Brown and Company, 2008. COMMENT: The physicist who helped found the holographic principle, recounting the decades-long fight over whether information falling into a black hole is truly lost. Difficulty: Medium. Covers the area-law entropy clue and the bulk/boundary picture properly — Derek's filing cabinet is a gentler analogy than anything in this book's actual title.""",
"""Susskind, Leonard. The Black Hole War: My Battle with Stephen Hawking to Make the World Safe for Quantum Mechanics. Little, Brown and Company, 2008. COMMENT: The argument over whether information falling into a black hole is lost, and the area-law clue behind holographic duality. Difficulty: Medium. Read it after Lesson 11, not instead of it."""
),
(
"""Norton, John D. Einstein for Everyone. Online lecture notes, University of Pittsburgh. COMMENT: Honest about history and about what the equations do not say. Difficulty: Low-Medium. File next to Mermin if you want a second start-here that costs nothing.""",
"""Norton, John D. Einstein for Everyone. Online lecture notes, University of Pittsburgh. Accessed 30 September 2026. COMMENT: Honest about history and about what the equations do not say. Difficulty: Low-Medium. A second start, beside Mermin, that costs nothing."""
),
(
"""Schutz, Bernard. A First Course in General Relativity. Cambridge University Press, 1985. COMMENT: The standard next course after this Appendix. Difficulty: High. Weinstein would assign it; Matkowski would collect the problem sets.""",
"""Schutz, Bernard. A First Course in General Relativity. 3rd ed., Cambridge University Press, 2022. The 1985 first edition is a different printing. COMMENT: The standard next course after this one. Difficulty: High."""
),
(
'''Derek smiled. "We had already established that."''',
'''Derek spread his hands. "We had already established that."'''
),
(
'''Trevor smiled, pleased. "Thank you."''',
'''Trevor looked pleased. "Thank you."'''
),
(
'''Derek smiled. "Now we catch a train."''',
'''Derek reached for his coat. "Now we catch a train."'''
),
(
'''Derek smiled. "Fine. Next problem."''',
'''Derek moved on. "Fine. Next problem."'''
),
(
'''Derek smiled. "You've just agreed to everything."''',
'''Derek tapped the board. "You've just agreed to everything."'''
),
(
'''Derek smiled. "Now you're ahead of me."''',
'''"Now you're ahead of me," Derek said.'''
),
(
'''Derek smiled. "But I know where he goes."''',
'''Derek already had his coat. "But I know where he goes."'''
),
(
'''Derek smiled. "That's becoming a recurring feature."''',
'''Derek made a note of it. "That's becoming a recurring feature."'''
),
(
'''Derek smiled. "Exactly."''',
'''"Exactly," Derek said.'''
),
(
'''Trevor smiled. "Thank you."''',
'''"Thank you," Trevor said.'''
),
(
'''Trevor smiled. "If the interval is timelike, the events can be causally connected."''',
'''Trevor spoke carefully. "If the interval is timelike, the events can be causally connected."'''
),
(
'''Trevor smiled. "I'll take that as a compliment."''',
'''Trevor accepted it. "I'll take that as a compliment."'''
),
(
'''Derek smiled. "Why?"''',
'''"Why?" Derek asked.'''
),
(
'''Derek smiled. "We're not."''',
'''"We're not," Derek said.'''
),
(
'''Derek smiled. "Yes."''',
'''"Yes," Derek said.'''
),
(
'''Penny smiled. "Lovely. Next?"''',
'''Penny did not linger on it. "Lovely. Next?"'''
),
(
'''Derek smiled. "Well, that's settled."''',
'''Derek closed the notebook. "Well, that's settled."'''
),
(
'''Derek smiled. "It's London."''',
'''"It's London," Derek said.'''
),
(
'''Trevor smiled. "Well, that's one theory down."''',
'''Trevor crossed it out. "Well, that's one theory down."'''
),
(
'''Trevor smiled. "Still Special Relativity."''',
'''Trevor was not joking. "Still Special Relativity."'''
),
(
'''Derek smiled. "Would you prefer 'possibly'?"''',
'''"Would you prefer 'possibly'?" Derek asked.'''
),
(
'''He smiled. "There. Progress."''',
'''He made a tick in the margin. "There. Progress."'''
),
(
'''Derek smiled. "We're still looking for that part."''',
'''Derek left the line blank. "We're still looking for that part."'''
),
(
'''Derek smiled. "Excellent question."''',
'''Derek wrote the question down. "Excellent question."'''
),
(
'''Penny blinked slowly. Derek smiled. "He's right."''',
'''Penny blinked slowly. "He's right," Derek said.'''
),
]

for i, (a, b) in enumerate(reps):
    n = t.count(a)
    if n != 1:
        raise SystemExit(f"count {n} at pair {i}: {a[:80]!r}")
    t = t.replace(a, b, 1)

p.write_text(t, encoding="utf-8", newline="\n")
print("replacements", len(reps), "smiled", t.count("smiled"))
