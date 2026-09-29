# -*- coding: utf-8 -*-
"""Second tighten pass: deepen cuts in focus chapters by paragraph index."""
from __future__ import annotations

import shutil
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn

ROOT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork")
SRC = ROOT / "Schrodingers_Paperwork_BOOK_1.docx"
LOG = ROOT / "_tighten_log.txt"

# index -> new text (verified against current doc in main)
EDITS: dict[int, str] = {
    # Ch1 more
    124: "The Annex had been designed in the late bureaucratic style: openness in theory, fluorescent headaches in practice. People came to complain about missed connections, duplicate arrivals, incorrect departures, luggage with philosophical objections to ownership, and, increasingly, journeys that had happened in the wrong order. Lolly had processed three of those this week. She did not care for trends in metaphysics.",
    171: "Lolly reached for a pencil. Most officers in Transit Reconciliation used regulation pens because they were permanent, authoritative, and chained to the desk. Lolly preferred pencil. Pencil admitted the possibility of error, which in her view placed it morally above most institutions. In the margin of the printed complaint slip she wrote: |journey⟩ = a|not yet taken⟩ + b|already arrived⟩ She stopped, considered, and added: with a and b being annoyingly nonzero.",
    217: "She opened her bottom drawer and took out a thin green notebook labelled, in her own hand, PRIVATE / UNHELPFUL. She had started it on the day she accepted that Transit Reconciliation would never again require calculus. It contained several pages of equations, four pages of complaints about the new software, and one pressed bus ticket from a journey that had taken place twice but only on alternate Tuesdays.",
    235: "As if in answer, there came from the corridor the sound of running. People did not run in the Annex unless the kitchen had reopened unexpectedly or the laws of existence were behaving in a manner likely to reflect badly on management.",
    253: "Lolly looked from the form to the flickering complaint file, to the private notebook on her desk, to the pale messenger in the doorway, and at last back to Mrs Chain, who had arrived somewhere before deciding to go there and now seemed, quite reasonably, to require a grown woman to explain the universe. She wished very much that the tea had been better.",
    257: "Mrs Chain picked up her handbag. “Well,” she said, “that sounds dreadful.” Lolly reached for her coat. “Yes,” she said. “I rather think it does.” Blankly, almost cheerfully, the printer produced a second sheet all by itself. Across the top it read: FOR THE AVOIDANCE OF CONFUSION Lolly shut her eyes. This, she felt, was how serious things generally began. Not with thunder. With stationery.",
    179: "On the ceiling, the office speaker made a soft ping. A voice of cultivated female neutrality announced, “Attention staff. Due to the implementation of the Simplification Initiative, all departments are reminded that duplicate interpretations of public events create avoidable confusion. Please encourage outcomes to settle promptly. Thank you for supporting a clearer tomorrow.”",
    188: "That, Lolly felt, was unpleasantly fair. She turned back to the terminal and opened the transit record in detail. A route map appeared, though it was not behaving in a route-like manner. The line representing Mrs Chain’s bus journey seemed to have split in three places and doubled back through a district which, unless Lolly was badly mistaken, had been a municipal duck pond until last February.",
    204: "Lolly printed the file. This took much longer than it should have, because the printer on her floor had been designed to detect urgency and resent it. When the sheet finally emerged, it came out warm and faintly humming. She flattened it on the desk.",

    # Ch3 more — house tour / object gags (keep impersonation + checklist)
    460: "By half past eleven, Lolly Wren decided that watching reality subdivide before lunch had become, in a professional sense, personal. She followed Beatrix out of Queue Management with Mrs Chain beside her and Jago materialising wherever least helpful. Beatrix walked quickly — not hurriedly — and corridors cleared.",
    477: "They took the bus because Beatrix did not trust Ministry pool cars, taxis were on strike across three boroughs for reasons no longer entirely causal, and Mrs Chain would not pay to revisit her own compromised life.",
    519: "Gideon got off at the next stop. He had worked out that the quickest way to understand the streets was not to watch them change but to read what had been ordered. “Find out who signed for it,” Lolly told him. He nodded, walked into the pole by the doors, and was gone before she could thank him.",
    564: "Lolly followed. It was a good room: armchair, bookshelves, two lamps, a sideboard — the sort one might spend fifteen years improving by tiny, stubborn increments.",
    567: "Mrs Chain walked to the mantelpiece. “My husband hated clocks,” she said. “Said they made the room feel supervised. There is now a clock where his photograph should be.”",
    571: "Lolly joined him. They were indeed books in the legal and physical sense, but not in the intimate one. Their titles were subtly wrong.",
    583: "Mrs Chain shut her eyes. “Ms Wren, if at any point it becomes necessary to break the law in order to restore my kitchen, I should like you to know in advance that I am philosophically available.”",
    590: "Lolly set the tea caddy down carefully. “Someone has made it choose a version before its details match,” she said. “It is trying to look finished and failing.”",
    609: "Remove low-value uniqueness markers. Standardise navigational cues. Replace emotionally dense objects with compliant equivalents. Align photographs to nearest stable kinship model. Ensure clocks converge within tolerated interpretive spread. Install replacement beverage protocol.",
    613: "Unit 7B resisting final set. Memory adhesion unusually high. Recommend secondary review before identity trimming.",
    622: "WELCOME, RESIDENT. YOUR DOMESTIC EXPERIENCE HAS BEEN UPDATED FOR GREATER CONSISTENCY. PLEASE REPORT ANY REMAINING ATTACHMENT TO PREVIOUS LAYOUTS.",
    625: "Too late. She struck the mirror smartly across the middle. The text vanished. The mirror cracked in a neat diagonal line and, for the first time all day, something in the house seemed honestly itself.",
    633: "Lolly took the device in both hands. It was warm. Too warm. “It’s local,” she said. “The revision isn’t only happening in central records. They’re installing reality correction hardware in people’s houses.”",
    642: "The clock vanished, reappeared, and turned into a photograph of a man with spectacles. The daffodils browned into geraniums, then both at once in a manner Lolly found deeply rude. The carpet shifted from stripes to faded blue swirls to bare boards and back.",
    649: "She looked up. At the far end of the hall, where the front door should have shown a small rectangle of afternoon light, there was now a man in a dark coat standing just inside the threshold. No one had heard him enter.",
    653: "Lolly looked down at the humming module in her hands, at the cracked mirror, at the photograph that was still trying intermittently to become a clock, and then back at the man in the doorway. For the first time that day, the problem seemed almost refreshingly simple. “Oh,” she said. “Was that yours.”",
    521: "Semi-detached houses stood in rows behind low hedges, each acceptable at first glance. At second glance the violations emerged: numbers fractionally out of sequence, curtains matching too well, identical stone birdbaths weathered in the same place. A cat sat on a wall with the overdetermined air of an animal generated from survey data.",
    496: "Lolly sat by the window and watched the city fail to remain itself — not continuously, which would have been easier, but in small indecent increments. A barber became an orthodontist. A florist became a closed florist. A Victorian pub blurred and resolved into a branch office of the Civic Harmony Board with hanging baskets and no moral centre whatsoever.",
    536: "Equivalent Residence Unit 7A. Equivalent Residence Unit 7B. Equivalent Residence Unit 7B (Revised). Equivalent Residence Unit 8. Equivalent Residence Unit 8A / Provisional.",
    550: "People really living in a place, Lolly felt, introduced minor frictions into it. Shoes with opinions. Keys of varying utility. A newspaper not quite where it should be.",
    576: "There, too, things were nearly right and therefore unbearable. The kettle was stainless steel instead of enamel. The tea caddy had been labelled HOT BEVERAGE INFUSION MATERIALS. Three mugs hung from hooks, each printed with a motivational saying about mornings.",

    # Ch5 more
    831: "Jago turned left through a yellow light with the lightness of conscience that comes from never recognising traffic law as binding philosophy. “She used to be very fashionable,” he said. “Brilliant, impossible, terrifying in committee. Left after some unpleasantness involving continuity theory and a minister who thought eigenstates were a minority voting bloc.”",
    841: "At length they turned off the main road and followed a narrow lane bordered by hedges and old brick walls. A wrought-iron gate appeared where Lolly would have sworn there had been no gate half a second earlier. It bore, in flaking black paint, a sign reading: THE INSTITUTE FOR UNHELPFUL CLARITY Visitors by prior argument only No refunds for conclusions Jago braked.",
    852: "They entered. The house smelled of paper, tea, solder, and intellectual impatience. Books lined every wall in layers of active use. Blackboards leaned against shelves burdened by journals and notebooks labelled in a hand so precise it seemed almost vindictive. A long table beneath the window held microscopes, mugs, a brass desk lamp, and what Lolly realised with quiet alarm was half of a dismantled detector array.",
    857: "“Yes,” said Fainrose. “A domestic projection stabiliser, third-generation civilian adaptation, vulgar casing, incompetent thermal shielding. I warned them not to deploy these into lived environments without local phase damping. They said I was being precious.”",
    880: "She turned from the screen and looked directly at her. “When a system evolves naturally,” she said, “it doesn’t jump from richness to paperwork. It moves through lawful change. You can dislike the law, but you may not skip it. They’re imposing an end state without understanding the dynamics that produce one.”",
    890: "Fainrose paused, perhaps deciding how much truth a person with an umbrella ought to receive at once. Then she said, “Imagine your home not as a place, but as a cloud of possible details held together by habit, memory, objects, routes through rooms, repeated actions, and expectation.”",
    893: "Jago smiled openly. Fainrose continued. “Now imagine some administrative imbecile decides this complexity is inefficient. Instead of letting that cloud develop into the version sustained by your actual life, they force it into a reduced pattern selected for stability and cost. The trouble is, they don’t understand which details support the rest. So they flatten the system before it has finished cohering.”",
    921: "Fainrose did not answer at once. Instead she reached for a second keyboard and called up a satellite map, then a network diagram, then what looked to Lolly like a topological model overlaid with municipal infrastructure. At the centre of one regional cluster blinked a small black icon. Next to it, in yellow: Singularity Asset 4C Status: Diminishing",
    928: "Fainrose’s mouth tightened. “Transport curvature, waste density management, long-range compression, several profoundly stupid infrastructure efficiencies from fifteen years ago. The Ministry likes gravity when it can invoice it.”",
    941: "Fainrose looked at her with almost maternal disappointment. “Oh, Lolly,” she said, and it was the first time she had used her name, which made the correction land harder, “of course it can. The only question is whether someone has been foolish enough to make it do so where the public can object.”",
    945: "“We will leave Mrs Chain’s house for the moment,” she said. “Not because it is unimportant. Because it is now evidence of a larger stupidity. If they have begun forcing collapse locally and interfering with gravitational anchors centrally, then the system is no longer merely rude. It is unstable.”",
    837: "They drove west. The city thinned gradually, as though suburban planning had set out to continue and then lost conviction. Office blocks gave way to terraces, then detached houses, then stretches of overmanaged green. The morning had become one of those bright English afternoons determined to deny the possibility of disaster while helping it along socially.",
    843: "Beyond the gate stood a long, low brick house with a slate roof, tall narrow windows, and the defensive air of a property that had spent years discouraging governments. An old dish antenna had been bolted to one chimney. Three bicycles leaned against a side wall. On the lawn stood a brass armillary sphere, two folding chairs, and what looked like a weather vane but was almost certainly measuring something less forgivable.",
    846: "Before anyone could knock, the front door opened. Stephanie Fainrose was not tall, and not young, and had the sort of stillness that makes other people feel over-articulated. She wore a dark cardigan over a pale shirt, narrow trousers, and spectacles that looked less like an accessory than a final administrative judgment upon the human face. Her hair, cut short and streaked with steel, suggested she had long ago discovered vanity could safely be ignored.",
    817: "Forty minutes after the interruption of Mrs Elspeth Chain’s domestic convergence, Beatrix Sloan was in an unlicensed grey car with Lolly Wren, Jago Flint, a confiscated Civic Stability Substrate module, Mrs Chain’s umbrella, and a woman whose house was still fluctuating. This was witness selection — after documentation and containment, the third response to institutional catastrophe she considered proper, and reserved for special occasions and senior management.",

    # Ch11 more Keinschein compress (keep shadow / 4C / nowhere)
    1507: "“Phase Two doesn’t take memories.” She put the folder on the table and opened it at the tab she had turned down. “It can’t. Not directly. There’s an entire volume here on why not — some poor devil in Legal wrote it in 2019 and nobody read it. A memory cannot be read out by external survey. It only becomes definite when the person is asked.”",
    1509: "“So they ask,” said Lolly. “And the asking is the whole mechanism. The Ministry cannot reach in. But if a citizen fills in a form, describes the memory, selects from options, signs the declaration — then the memory becomes whatever the form says, because the form was the measurement.” She turned the folder round. “Look at the title of the volume.”",
    1518: "He had a great disorganised nimbus of white hair, a moustache of magnificent indifference, a cardigan that had outlived several arguments, and no shoes. His face was one everyone in the room had seen on posters, mugs, and the walls of secondary-school physics laboratories. The resemblance was so complete that it produced not recognition but a sort of vertigo.",
    1522: "“Say it. Everybody says it. I have had eleven decades of it and it was tiresome by 1931.” He came in without hurrying, and Lolly noticed that the doorframe appeared to accommodate him rather than the reverse. “No relation. Well. Not in the sense you mean by relation.”",
    1526: "“Later. You will enjoy it more when you are frightened.” He looked round the room with enormous, benevolent interest. “Ms Sloan. Mr Flint. Mrs Chain — my condolences on your sister and my congratulations on your umbrella. Ms Wren.” He stopped. “Ms Wren, you have found the invitation clause.”",
    1548: "“I do not drink blood, Mrs Chain. Blood is a courier. It carries the thing but it is not the thing.” He laced his old hands together. “When a question is put to the world, and the world, which had been holding several answers at once, is obliged to produce one, the other answers are not filed. They cease, and in ceasing they release something.” He shrugged. “I take that. I have taken it since the first measurement, which was much longer ago than your people think.”",
    1554: "“Nine thousand dwellings,” he said, “each forced from a rich state into a thin one, tens of thousands of alternatives extinguished per address, per week, at public expense, with certificates. Do you understand what that is, from where I sit? It is not a meal. A meal is small — a woman deciding at last which of two lives to keep. I have lived on such things for aeons and been content.” He spread his hands. “This is industry. A national programme with a budget line.”",
    1557: "“No,” he said. “That is not mine, and I want it understood. I did not ask them to build a sink or hang a county from an evaporating hole. That is not appetite, Dr Fainrose; that is waste, and it will end with the pantry on fire.” He sat forward. “This is why I have come. Not to gloat.”",
    1561: "“Houses I can dine on for a century. But memory is not a house. A memory is the record of which branch was taken — how the universe keeps its accounts.” He tapped the cover. “If you begin collapsing memory by questionnaire, you are not merely extinguishing alternatives. You are falsifying the ledger. Then nobody can tell what happened — including me, including the thing that comes after me, including the system that is currently trying to repair itself.”",
    1563: "“Yes,” said Keinschein, and looked at her with real approval. “Yes, the girl has it. Your Dr Fainrose is right that the country can be recovered from its correlations rather than from a copy. But a correlation is a statement about what agrees with what. If you ask leading questions about what people remember, and each answer becomes true as it is given, then the agreements will be manufactured, the syndrome will be clean, and the code will report itself intact — around nothing.”",
    1565: "“It would be a successful recovery,” said Keinschein. “Of the wrong state. Certified. Permanently. With no residue for anyone to appeal to, and no residue for anyone to eat.” He sat back. “I have been dining on your species’ abandoned lives for a very long time, and I have never once had to explain to a government that a thing can be irrecoverable. You have made me pedagogical. I resent it.”",
    1569: "“Entirely for my own reasons,” said Keinschein. “Mrs Chain, I am eleven thousand times your age and I have never once acted from virtue. But my reasons and yours are, this month, pointing the same way, and you are in no position to be choosy about allies.” He glanced at the boxes. “Also, I am the only one of you who has read Phase Two — invited into it this morning by a Deputy Under-Secretary who filled in a form about his mother.”",
    1574: "“You write,” said Keinschein, “as though a measurement were an event: a thing that happens at a time, after which there is one answer.” He shook his great white head gently. “That is the working assumption of every laboratory on this planet. It has served you admirably. It is not true. When your Mr Venn scanned Mrs Chain’s mantelpiece, what became definite for Mr Venn did not become definite for the mantelpiece, or the county, or me. There is no single moment at which the universe decides — only a widening region of agreement, spreading at the speed of gossip, and no fact of the matter about the parts it has not reached.”",
    1576: "“He froze it for the grid,” said Keinschein. “Not for the woman remembering her sister. She was inside. Different question. Different answer. She could feel the shape of the name — she told them so, and they marked it no action required.” He rose with an old man’s effort and an entirely different creature’s economy. “There is no view from nowhere, Ms Wren. Your Ministry believes it is standing outside the room. It is not. There is no outside. When it finally asks what everybody remembers, it will not be reading the answer.”",
    1583: "“He eats the offcuts of the thing we are trying to save,” said Fainrose. “Which is worse, because it means he is telling the truth about wanting the rest intact.” She was staring at the cabinet where his reflection had not been. “And he is right about the paper.”",
    1536: "Lolly looked at the floor for a considerable time. The chairs had shadows. The table had a shadow. The old man in the cardigan stood in full August light, and the floor beneath him was as bright as the floor beside him.",

    # Ch12 more — shorten after long speeches; keep electricity + assistant
    1600: "Phase Two went live at seven the next morning in four sub-districts, because Vale had been suspended at midnight and the Board had discovered, on reading his file, that they preferred the version of him that had signed things.",
    1601: "Fainrose had a view, which she delivered to the syndrome table rather than to anyone in particular. “They have taken the one signature off the directive,” she said. “Now it has no author, and the only way it gets one again is for someone to stand up in that inquiry and say what it did — thanked for the disruption and not the truth. The cheapest move there is, and they will make it every time.”",
    1602: "By eight, Beatrix Sloan had established that the suspension had been proposed by a committee none of whose members would consent to be named. By nine she had stopped shouting at telephones and started drafting, which Lolly Wren had learned to recognise as the more dangerous phase.",
    1604: "This was not modesty. She had checked. Fainrose needed silence and stabiliser algebra; Beatrix needed a lawyer; Gideon was in the requisition archive with fifteen years of ledgers. Jago had gone to Croydon on an errand unlikely to be relevant. Mrs Chain had gone to Sub-District 6 to sit with another woman whose sister’s name had gone the same way, and had taken the umbrella.",
    1605: "The woman in Sub-District 6 had a classification. Beatrix had found it that morning: P-9, pending status, for a citizen the survey had caught in the middle of something — a name half-said, a journey not yet agreed to — and then required to sign regardless. Beside the box, on file after file, a second field read no action required. The log stood at ninety-one that morning, and was climbing.",
    1610: "The man standing over her was slight, elderly, and dressed with an exactness that had gone out of fashion so long ago it had returned as a moral position: a dark suit of beautiful cut, a stiff collar, a narrow grey tie, and gloves. He held a hat. He gave the impression of someone who had been waiting to be noticed, and who considered impatience a failure of breeding.",
    1616: "“Not the object. The shape of it. Dr Fainrose quoted four of your lines to me this morning to complain about them, which is the highest form of French compliment.” He looked at the wall. “May I sit? It is a long time since I have sat on a wall and I should like to know whether it is still possible.”",
    1622: "“I have known Alfred Keinschein,” he said, “for ninety-one years, and I have never once forgiven him. I would trust him with my life and nothing smaller. He telephoned me last night. He said: Louis, they have a clerk who has understood four things by herself, and she is about to stop.” He turned his head. “He was correct?”",
    1624: "“I was a physicist,” she said. “For about eleven minutes. Then electronics for ten years, then Transit Reconciliation. Three days ago I started noticing things in a notebook, and every one turns out to be a standard result with somebody’s name on it.” She did not much care how it sounded. “Fainrose is doing stabiliser codes upstairs. Keinschein has been alive since before agriculture. I write that the house is larger than the form and feel clever until somebody names it.”",
    1628: "“I was twenty-two. I had taken my degree in history.” He said it without emphasis. “My family had been soldiers and diplomats for six hundred years and I was, by inclination, an archivist. My brother was the physicist. I was the one who read.”",
    1630: "“In 1911 my brother served as secretary to a congress of physicists,” said de Brévanne, “and brought home the papers. I read them because I read everything. I did not understand them, and I could not stop.” He turned the hat over in his gloved hands. “I had no laboratory, no standing, no mathematics beyond the ordinary. What I had was the habit of a historian: when two authorities disagree, one does not choose. One looks for the document they have both misread.”",
    1632: "“Light,” said de Brévanne, “which everybody knew was a wave, and which Einstein had shown behaved in some circumstances as though it were a great number of small hard things.” He shrugged. “The physicists were embarrassed; they spoke of it as a difficulty to be managed. I was not embarrassed, because I was not a physicist, and so I did the thing only an ignorant man would do: take it seriously in both directions at once.”",
    1634: "“Everyone was asking how a wave could be a particle.” He looked at Lolly. “Nobody was asking whether a particle might be a wave. Turning a question round is not a discovery; it is a manner. It required no apparatus and no genius — only somebody outside the room, with the wrong training, who did not know which of the two facts he was supposed to find awkward.”",
    1636: "“I was right,” said de Brévanne, “and it took four years to say it properly. When I said it, my examiners did not believe it. That is usually how it goes.”",
    1638: "“No.” De Brévanne’s voice was suddenly quite firm. “That is a comforting story and I dislike it. The outsider usually gets nothing and dies unpublished. I am telling you something narrower.” He set the hat down on the wall. “Ms Wren, every observation in your notebook has a name already. Which of them did you write down before you were told the name?”",
    1640: "“No,” said de Brévanne. “That is my point. You are treating the pre-existence of the name as evidence that the observation was worthless. It is evidence that the observation was correct.” He let that sit. “One may receive a piece of physics, and possess a fact one can repeat. Or one may arrive at it, and possess the reason, and go on to the next thing, which has no name yet. The second is the only kind that is any use in a crisis, and it is the only kind you have. You are sitting on a wall despising yourself for it.”",
    1642: "Somewhere behind her a phone began ringing and did not stop for a long time. When it cut off, Jago’s voice carried across the car park in fragments — a district name, the word “live” — and Lolly understood, without turning round, that Phase Two was still spreading while she sat on a wall discussing 1911.",
    1644: "“Dr Fainrose is formidable and will save perhaps nine thousand houses this week,” said de Brévanne. “But she cannot hear the question she was trained out of hearing. That is not a criticism; it is what training costs.” He picked up the hat again. “Now. Keinschein told you last night that there is no view from nowhere, and that nothing is definite until agreement has spread. It frightened you.”",
    1646: "“Good. It should. It is also not the only available account, and he did not tell you that because he is an old snob who enjoys the vertigo.” De Brévanne looked out at the car park. “May I show you the other one? It is mine, unfashionable, and I have been out of favour for eighty years, which gives a man leisure to be sure.”",
    1652: "“Yes,” said de Brévanne quietly. “On Keinschein’s account, that is loose talk. On his account there was no fact about the flowers until agreement reached them, and what you felt in that room was a metaphor.” He turned. “But you did not write down a metaphor, Ms Wren. You wrote down a mechanism. You said the lie required electricity.”",
    1656: "“Suppose the house always had one definite configuration. One actual wallpaper — not a haze of possibilities: an actual state, at every moment, as common sense insists and as your Ministry pretends to believe.” De Brévanne raised one gloved finger. “And suppose there exists a wave: a real physical wave, spread over every configuration the house might have had, including the ones it did not. Suppose the actual configuration is guided by that wave — steered, never anywhere but somewhere, yet always told where to go next by a thing that fills the whole space of alternatives.”",
    1659: "“Real, and empty, and effective,” said de Brévanne. “That is the whole of it. The branch nobody took is not a ghost and not an accounting error. It is part of the object that decides where you go. Interference is what it feels like when an empty possibility pushes.”",
    1661: "“He did not create a fact. There was already a fact.” De Brévanne’s voice sharpened for the first time. “He deformed the guidance. He put his apparatus into the space of alternatives and altered the wave steering that woman’s household. The actual configuration went where the deformed wave sent it — somewhere thin. When Mr Flint tore the cable out, the deformation ceased, and the guidance relaxed. The flowers came back not because they had been in storage, but because the wave that had always contained them was permitted, briefly, to matter again.”",
    1664: "“It is an entirely different crime,” said de Brévanne, “and this is my lesson, and the only thing I came to say.” He turned to face her. “Ms Sloan is upstairs building a case that the Ministry falsified records — true, and small. Dr Fainrose is building a case that they interfered with lawful evolution — truer, and larger. But if what I have described is so, then everything they have done — the queue, the scanner, the certificates, the continuous assurance, and now the memories — was not an intrusion into knowledge.”",
    1672: "“But if the wave is real — a physical thing in configuration space — then it is not information anybody has to store.” She looked up. “It is still there. Deformed, but there. You would not restore the country from a copy. You would restore it by taking your apparatus out of the wave and letting the guidance relax.”",
    1679: "“There are people who would recognise the shape of it,” said de Brévanne. “There is no one who has said it about a country.” He rose and set his hat on his head. “You will now go upstairs and say it to Dr Fainrose. She will tell you it is unfalsifiable metaphysics and a hundred years out of fashion — quite right on both counts. Then she will be unable to sleep, because it also specifies a procedure, and hers does not.”",
    1681: "“I have believed it for eighty years without being able to prove it,” said the Duc de Brévanne, “which I am told is called faith, though I maintain it is merely patience.” He put out a gloved hand. Lolly shook it. It was quite cold. “One last thing.”",
    1683: "“You said you were a physicist for eleven minutes, once.” He was already turning away. “I was a historian until twenty-two, and a physicist for sixty years afterward, and never once both. That is why I could not see what your bureaucracy was doing to those houses and you could.” He paused. “Ten years on things that must work, three days on paperwork: you are the only person in that building who knows what an institution is as well as what a wave is. Do not stand on a wall about it.”",

    # Ch13 more (keep sister correction 1731-1735)
    1697: "“We are not here to adjudicate physics,” said the chair, a Mr Pilbeam, who had been brought in from Transport on the grounds that he had once managed a bridge, although the bridge had not supplied a reference.",
    1701: "“They have designed it,” said Beatrix, “so that nothing is ever anybody’s fault. It is the same instrument every time. Convene the ones who cannot agree and call the noise a lack of evidence.”",
    1704: "“Oh, that’s marvellous,” she said. “That’s genuinely inspired. They’ve picked three men who have spent their entire lives disagreeing about exactly this, and one of them is dead.”",
    1707: "They came in at ten past. The first was tall, hollow-cheeked, immaculately grey, with the posture of a man who had spent decades being the cleverest person in dangerous rooms. He carried nothing — no papers, no case — and sat at the far end with his hands folded, choosing the seat furthest from the window.",
    1710: "The second arrived talking. He was younger by decades, sandy-haired, in a jacket over a T-shirt, tablet in one hand and coffee in the other, with an air of enormous delight at being alive in so interesting a universe. “—which is the thing nobody wants to say out loud, that if the equations are the ontology then this whole crisis is a bookkeeping dispute — sorry, hello, Max Tegmark, cosmology, I’ve read the Fainrose paper, Dr Fainrose it’s an honour, your syndrome table is gorgeous.”",
    1713: "The third came in last and quietly, and the room’s temperature dropped about it. He was a smallish man with a red beard going white, in a jumper, with the bright unblinking gaze of somebody who has spent thirty years being polite to people he considers sloppy. He had a Belfast voice, unhurried and precise, and he sat down without shaking hands.",
    1718: "Nobody pursued it. Pilbeam distributed the question. It had been drafted by a committee and ran to a paragraph, but stripped of its clothing it asked this: does the Ministry’s programme of civic simplification cause damage to physical reality that is not captured by the loss of records?",
    1721: "“I find no meaning.” Heitmann’s hands stayed folded. “The formalism relates preparations to observations. It tells you what your instruments will report. It says nothing about what the electron is doing when nobody asks, because that question generates no numbers.” He turned his head slightly. “Your survey teams asked; they received answers; the answers were correct. Unkindness is politics. A hidden state of the house is a fiction.”",
    1723: "Heitmann looked at her with no unkindness at all, which was worse. “Then she was harmed,” he said. “I do not dispute the harm. I dispute the ontology of the harm. She was harmed as a citizen, by a procedure, and you should prosecute the procedure. Do not ask me to certify that a wave function was injured. I have spent my life declining to say what the wave function is and I decline again this morning.”",
    1724: "Tegmark had his hand half up like a schoolboy. “See, this is where I get off the bus,” he said. “Werner — may I — you say the question generates no numbers. But the equation generates numbers, and my position — a minority one — is that the mathematical structure isn’t a description of reality, it is the reality. The universe is a mathematical object and we’re self-aware substructures inside it.”",
    1730: "“Nothing was destroyed.” He said it gently, and Lolly understood he was neither stupid nor cruel, which was worse. “If the equation never stops, and there’s no collapse, the universe didn’t pick one answer and delete the rest. It branched. Photograph and clock — both real, both with a Mrs Chain.” He spread his hands. “The alternatives weren’t extinguished. They were decohered from. Everything this Ministry allegedly destroyed still exists. It’s just not here.”",
    1740: "“That would be the defence,” said Beatrix. “That is what they convened him for. Not to disagree with Professor Heitmann. To supply Vale’s successors with a physics under which the harm is relocated rather than caused. You will see it in the Board’s response within a fortnight and it will say: no alternative is ever lost, and therefore no citizen has suffered a loss, and therefore Phase Two may proceed as a matter of record-keeping.”",
    1745: "Everyone looked at him. Bellew had not moved. He sat with his forearms on the table, pale eyes going from Heitmann to Tegmark and back. “Werner says the question has no meaning. Max says it has too many answers, all of them real. Between the pair of you there’s not one thing a Board of Inquiry could go and check.” He tapped the table once. “You’ve both got theories in which nobody can ever be wrong. I’ve spent my career objecting to that, and I’ll object to it in a car park in a suspended county if required.”",
    1747: "“The formalism is grand,” said Bellew. “I’m talking about the word.” He looked round the table. “Measurement. The Ministry’s directives say it four hundred times. It is the most disastrous word in the vocabulary of physics, because it sounds like a special class of event the rest of nature is exempt from. There isn’t. A surveyor is a physical system. A form is a physical system. There is no magic in a clipboard.”",
    1754: "He held up two fingers. “There are two things a reasonable person wants to believe. One: things have properties whether or not anybody’s asking — the wallpaper is some colour when the room’s empty. Call that realism. Two: what you do here cannot instantly affect what’s true over there — no influence outrunning light. Call that locality.”",
    1755: "He lowered the fingers. “Every sensible person in this room wants both. Werner avoids the problem by giving up the first. Max keeps both by multiplying the worlds until the question dissolves. And in 1964 I sat down and did a small piece of arithmetic, and the arithmetic said: you cannot have both. Not as a matter of taste. As a matter of measurable numbers.”",
    1757: "“That’s the point of it, Mr Chairman. That’s the whole point of it.” Bellew leaned forward. “If both things were true — properties in advance, no influence at a distance — then certain correlations between distant events have a ceiling. A definite number. You can work it out with school algebra in an afternoon. And if nature ever exceeds that ceiling, then one of your two comfortable beliefs is finished, and no amount of interpretation gets it back.”",
    1759: "“It’s been done for sixty years,” said Bellew, “in Berkeley and Orsay and Innsbruck and Delft and Vienna, tighter and tighter, and every hole anybody found in it has been plugged, and they gave a Nobel Prize for it in 2022, and the answer is the same every time and it isn’t close.”",
    1762: "“You’ve been told it’s metaphysics,” said Bellew, “and that her guiding wave is unfalsifiable, and both dismissals are true and both are beside the point.” He nodded toward Lolly. “You don’t need to win the interpretation. You need one thing in front of Mr Pilbeam — the one thing tested to death: that a change made in one place can alter what is true in another, with no signal between them.”",
    1765: "“They tied nine thousand dwellings to one anchor. Fainrose’s correlation lattice.” She was standing now, without having decided to. “The Board’s position is that each dwelling was surveyed separately, so each certificate is separately defensible. Local decisions. Local harms. Nine thousand small administrative matters, each too small to be worth an inquiry.”",
    1767: "“And if the correlations exceed Bellew’s ceiling,” said Lolly, “then they weren’t separate. It’s not an interpretation that they weren’t separate. It’s a number. You can go and measure it in Sub-District 6 this afternoon and get a figure that no committee can call metaphysics, because the arithmetic doesn’t mention wave functions or branches or guidance at all. It just says: if these were independent systems being independently surveyed, this correlation is impossible.”",
    1770: "“It does not,” Bellew agreed. “It tells you what is not permitted. That’s a smaller claim and it’s the reason it can’t be argued with. Werner, you spent your life saying we should confine ourselves to what can be checked. I took you at your word and went and checked something, and you’ve never forgiven me for it.”",
    1775: "“No,” said Tegmark, with real cheerfulness, “but I’ll take it. And for what it’s worth—” he turned to Mrs Chain, and did it properly, and looked at her while he said it — “you were right and I was glib. Nothing being destroyed globally doesn’t buy anybody anything locally. Somebody in this branch lost her sister. I’ll put that in the minutes.”",
    1780: "“But we’re agreed on a measurement,” said Bellew. “Which is worth ten unanimous opinions and you may minute that too. Werner will accept it because it’s an instrument reading. Max will accept it because his branch has instruments in it. I’ll accept it because I designed it. And whatever number comes back, none of the three of us can wriggle.”",
    1781: "Beatrix laid down her pen. “Chair,” she said. “The panel proposes a test with a pre-agreed threshold and three incompatible experts bound in advance to accept the result. Refusing that is not caution. It is obstruction, and I will write it up as obstruction, and I will name the committee that would not give its members’ names.”",
    1785: "“Your Duc’s account and Max’s account and Werner’s silence — you’ll be tempted to pick one, because you’ve a tidy mind and you’re ten years in electronics and you want to know what the circuit is.” The pale eyes were unblinking. “Don’t pick yet. Pick when something forces you. Until then hold all three, and use whichever one tells you where to put the probe. That’s not cowardice, that’s method.”",

    # Ch14 more — reach holography sooner
    1800: "They went into Sub-District 6 on the Thursday with two vans, a portable timing rack, four hired photodetectors, and paperwork Beatrix had signed in a hand that dared anyone to query it. Fainrose was in the primary school hall running cable. Jago had gone for a fifth detector. Lolly, sent out for exceeding her quota of useful questions, ended up in the Coldharrow Street library with the green notebook and eleven photocopied pages from box seven.",
    1801: "There was one other person in the reading room: a slight man in his seventies, entirely bald, papers colonising two additional tables. He wrote in pencil, continuously, pausing every twenty minutes to look at the shut-down carpet showroom. The librarian had given up asking him to consolidate, and simply reshelved around him.",
    1804: "“Dr Bellew mentioned it.” The man turned. He had a pleasant, unemphatic face and the mildest possible manner, and he spoke so softly that Lolly found herself leaning forward. “I think it is an excellent idea. It is the correct instinct — to find the one claim that does not depend on taste. Forgive me. Leonhard von Wittenberg.”",
    1814: "Von Wittenberg smiled very slightly and looked out at the carpet showroom. “That is the standard answer and it is the best-tested answer in the history of thought,” he said. “It is also, I believe, wrong, and I have believed it for about fifty years and been unable to prove it, which is a condition your Duc de Brévanne has described to you rather well.”",
    1817: "He drew, very small, a dot. “A point particle,” he said. “It has no size and no internal structure. If you wish to explain why there are so many different particles, you must simply list them — seventeen items, and nobody knows why that list rather than another.”",
    1824: "“Ah,” said von Wittenberg, and for the first time something in his face brightened. “That is the part that persuaded me. For fifty years the scandal was that our theory of the very small and our theory of gravity would not sit in the same room. Put them together and the answers came out infinite — nature’s way of saying the question was malformed. Every attempt failed.”",
    1829: "“There are three, and I shall not hide them.” Von Wittenberg counted them off on his fingers. “First: the strings are so small that no accelerator we could build could see one directly. There has never been a direct experimental test. Dr Fainrose is entirely right to say so.”",
    1831: "“The mathematics does not work in four dimensions. It requires ten.” He said this the way another man might mention that a recipe requires buttermilk. “Nine of space, one of time. Since we experience three of space, the other six must be curled up small — at every point, six additional directions, wound so tightly that nothing you or I can do will push anything along them.”",
    1833: "Somewhere outside, a car alarm went off and was silenced. Lolly glanced at her watch — a new habit, three days old — and found that two hours had gone, with 4C still losing mass somewhere behind all of this.",
    1834: "“It is, yes.” Von Wittenberg looked pleased. “And the third catch is why I am in a library in Sub-District 6 rather than at home. For a long time there were five different string theories — all consistent, all beautiful, all slightly different. An embarrassment: one had set out to explain why there is only one world and had produced five candidates.”",
    1842: "Lolly closed the notebook. “Professor von Wittenberg,” she said. “I will write down anything that tells me what they dumped into 4C. I will not take dictation on eleven dimensions until then. In three days I have been told that nothing is definite until agreement spreads; that everything is definite and steered by a wave; that every alternative happens somewhere; that I should stop picking and go and measure something. And you have now told me everything is made of eleven-dimensional membranes nobody can see.” She looked at the little loop on the page. “I have a woman in this district who was stopped in the middle of remembering her sister’s name. What am I supposed to do with strings?”",
    1843: "Von Wittenberg did not take offence. “That is the right question,” he said. “First: nothing. You are supposed to do nothing with strings. The Bell measurement is what matters this week. Anyone who tells you eleven dimensions will help you get an injunction is lying to you.”",
    1845: "“Second: I did not come here to tell you what everything is made of. I cannot demonstrate it.” He turned one sheet round. “I came because of your black hole.”",
    1848: "“Alfred telephoned me on Tuesday and shouted at me for eleven minutes, which at his age is a form of affection.” Von Wittenberg’s mouth twitched. “His concern is that your Ministry has used a small engineered black hole as a disposal channel for suppressed alternatives, that the object is evaporating, and that when it has gone there will be no record of what was destroyed. He calls this the falsification of the ledger. I have known him ninety years and I have not heard him frightened before.”",
    1850: "“No,” said von Wittenberg. “But I can tell you why he may be wrong, and it is the one thing my subject has actually achieved.” He turned the sheet over. “A black hole has an entropy,” he said. “Bekenstein saw it and Hawking made it precise: the entropy is proportional to the area of the horizon. Not to the volume inside. To the area of the surface.”",
    1853: "“In 1996 two colleagues took a particular class of black hole in string theory, built it out of membranes and strings, counted the possible configurations — an ordinary counting problem, tedious but honest — and found that the number of states gave exactly the Bekenstein-Hawking entropy. Exactly. With the correct factor.” He said it very quietly. “That is the first time anyone counted the microscopic states of a black hole and got the entropy formula back exactly, and it came out of strings.”",
    1857: "“Then the question becomes whether the radiation carries them out,” said von Wittenberg. “The area law suggests something outrageous: that everything inside a region can be encoded on its boundary. The interior is not the fundamental description — the account is on the surface. There is a precise version in which gravity in a certain space is equivalent to a theory without gravity on its edge. Two descriptions. Same physics.”",
    1861: "“Yes,” said Leonhard von Wittenberg. “And so the current view — not proven, not settled, but the view — is that evaporation does not destroy the information. It is scrambled almost beyond recovery, it emerges in correlations so subtle that no practical measurement could unpick them, but it is not annihilated. Unitarity survives. The books balance.”",
    1865: "He gathered his papers. “This is the difficulty with being in my line of work. We have produced, I think, the most beautiful structure in the history of physics, and we have not produced a single number a committee could check. Your Bell test will produce one in two days. I am aware which of us is more useful this week.”",
    1868: "“You told Dr Bellew you were a physicist for eleven minutes, once.” Von Wittenberg looked faintly embarrassed. “I was a history major. I intended to be a journalist. I came to physics late and by an unusual road, as did de Brévanne, as did — in his fashion — Alfred, who came by no road at all.”",
    1869: "He picked up his pencil. “I mention it only because I notice that everybody who has come to talk to you this week arrived from somewhere else, and I do not think that is a coincidence. It is simply that the people who ask what a thing is are usually people who were not trained to take it for granted.”",
    1879: "“Because if the information is on the horizon, then it comes out in the radiation, in the correlations, over the entire remaining lifetime of the object.” She was already up, sandwich abandoned. “Which means there is a window. And the window closes when 4C does. And the smaller it gets, the hotter and faster it goes.” She looked at her. “Lolly. How long have we been treating the evaporation as the catastrophe?”",

    # Ch18 more heat-death / setup compress; keep scarce accounts + no lid
    2013: "And on a Friday in March, in the reading room of the branch library on Coldharrow Street, at the table by the window overlooking the shut-down carpet showroom, she found a very old Austrian gentleman waiting for her with a wooden box on the table and two cups of coffee already going cold.",
    2014: "“Sit,” said the old man. “I have ordered you a coffee and it is already unpleasant, which is the most reliable thing in this building. Erich Schrottfinger. You have been sent to me by a dead Irishman, a French duke, and a vampire, which is a referral pattern I have not had since 1953.”",
    2017: "“Don’t,” said Schrottfinger. “It is empty. It has always been empty. It was always a joke, Ms Wren — I invented it to be ridiculous, to show my colleagues that their position led somewhere absurd, and within twenty years it was on coffee mugs. You cannot win. You make one sarcastic remark about a cat and it outlives your equation.”",
    2020: "Schrottfinger pushed it aside. “Now. You have finished a thing, and you have come to a library on a Friday because you want somebody to tell you what it was all for, and Fainrose cannot tell you because she is a working physicist and von Wittenberg cannot tell you because he will start on the eleven dimensions. So it falls to me, who am not respectable.”",
    2025: "“Here is the outlook, since you want the outlook. Your Ministry believed it was managing a country. It was in fact interfering, in a small and provincial way, with something that is not finished. I do not mean the paperwork. I mean the universe is not finished, and everything you have lived through this year took place in what future arrangements of matter will regard as the opening seconds.",
    2026: "“The stars are the first thing to understand. There are stars now. This is not the normal condition. Star formation peaked long ago; the gas will run down; in something of the order of a hundred trillion years the last star will form and the sky will begin to go out, one by one. And then a very long time of embers: white dwarfs cooling, neutron stars cooling. That era is longer, Ms Wren, than the era of starlight by a factor you cannot usefully imagine. Almost all of history is afterwards. Then, if the protons are not eternal — and we do not know — even the embers dissolve, and matter itself is a phase that ends.",
    2027: "“And then it is the age of the black holes, and they are the last structures, and they do exactly what your 4C did in a car park in Surrey: they evaporate. Slowly, then less slowly, then in a final bright indignity. The largest will take on the order of 10 to the power of 100 years. But they go. After that: a very thin, very cold, very dark space, expanding, and nothing in it that could be called an event.",
    2030: "“Now,” said Erich Schrottfinger. “The interesting part. Every physicist my age was taught that the universe runs down. Order becomes disorder; the coffee goes cold; the sun exhausts itself. Perfectly true. And when I was younger I looked at a living thing and thought: how does that happen. Because a living thing does the opposite — holds a pattern against the current for eighty years.",
    2031: "“And the answer is not that life defies the law. The answer is that a living thing survives by feeding on order — taking in structure, excreting disorder, paying the bill locally and passing the cost outward. It does not violate the accounts. It runs a very good scheme within them. A living thing is a place where order is temporarily concentrated because it has arranged to be paid for elsewhere. You have spent a year on it.",
    2032: "“Your Ministry, Ms Wren, was doing the same thing, badly, and without knowing it. It wished a district to be simple — low in complexity, cheap to describe. And it discovered what every living system discovers: you cannot simply have that. You must pay for it, and the payment is that the disorder goes somewhere else. So they built a hole and put it in there. That was thermodynamics, conducted by people who had not been told they were doing thermodynamics, and it ended in a fire because they never asked where the bill was going. Every institution that promises to make things simple is proposing to move complexity somewhere you cannot see. Always, and by law. That is the sentence I should like you to take away. It is the second law with the politics put back in.”",
    2034: "“And so — the outlook,” said Schrottfinger. “Yes. In the long run: the embers, the holes, the dark. I shall not soften it. But consider the enormous middle: a very long period with order still left to be spent, in which anything that can arrange to be paid for elsewhere may persist, and think, and ask questions. Life did not have to happen. Having happened, it has a very long time to work with.",
    2035: "“And here is what I think, and I am one hundred and fourteen and entitled to think it. The universe does not contain many places where it is described. Almost everywhere, things simply proceed. But wherever something has assembled itself into an arrangement that can hold a model of the rest — a bird, a mathematician, a green notebook — the universe acquires, locally and temporarily, an account of itself. That is not nothing. That may be the rarest thing in it. It is certainly rarer than gravity.",
    2036: "“Your Ministry was engaged in reducing the number of such accounts, and calling it efficiency, and the reason that was a crime and not merely a mistake is that the accounts are the scarce commodity and the simplicity was not. Anyone can have simplicity. You can have all the simplicity you want at the end of time, and it will be perfect, and there will be nobody in it. So: what is next in the universe. More of this, for a very long while, and then less, and then none. And in the meantime, an unreasonably interesting middle, in which the correct posture is neither optimism nor despair but attention — which is your job title, I understand, and which somebody has finally thought to fund.”",
    2040: "“The whole trouble with my cat was that everybody read it as a story about a box. It is not. It is a story about the lid. The absurdity I was pointing at is the belief that there exists a moment at which the matter is settled — that reality performs a closing act, once, cleanly, and then the fact is a fact and may be filed. There is no such moment. Your friend Keinschein was right about that much and it is the only thing he and I agree on. There is only the widening business of things becoming correlated with other things, indefinitely, forever, at the speed of gossip, and a state that has not yet finished resolving is not a mystery awaiting a verdict. It is the ordinary condition of everything.",
    2041: "“Three hundred and eight of your recovered items were pending. Not memories. Things that had not finished happening. You gave them back to people, and they are still not finished, and they will go on not being finished, which is what it means to be alive rather than certified. So this is not the end of your book. It is the front matter of what those three hundred and eight are going to do. It is a Prologue, and it is at the back, and if that offends the printers they may take it up with the second law.”",
    2043: "“One last thing, since you have been polite and have not once mentioned the cat’s welfare. You will be tempted, in your new post, to find out which of them was right. De Brévanne and his wave, Keinschein and his agreement, Tegmark and his branches, von Wittenberg and his strings. You will want the answer, because you spent ten years in electronics and you want to know what the circuit is.”",
    2044: "Schrottfinger put on his hat. “You will not get it. Not from me, not this century, possibly not ever. And you must not let that stop you from noticing things, because the noticing is the part that turned out to matter and the interpretation was never what saved the district. What saved the district was a clerk who wrote down that a lie required electricity.",
}


def set_paragraph_text(paragraph, text: str) -> None:
    t_elems = paragraph._p.findall(".//" + qn("w:t"))
    for t in t_elems:
        t.text = ""
    if paragraph.runs:
        paragraph.runs[0].text = text
        r0 = paragraph.runs[0]._r
        t0 = r0.find(qn("w:t"))
        if t0 is None:
            t0 = r0.makeelement(qn("w:t"), {})
            r0.append(t0)
        t0.text = text
        if text.startswith(" ") or text.endswith(" "):
            t0.set(qn("xml:space"), "preserve")
    else:
        paragraph.add_run(text)


def words(s: str) -> int:
    return len(s.split())


def chapter_of(idx: int) -> int | None:
    bounds = [
        (1, 109, 260), (2, 260, 459), (3, 459, 658), (4, 658, 816),
        (5, 816, 954), (6, 954, 1082), (7, 1082, 1221), (8, 1221, 1312),
        (9, 1312, 1445), (10, 1445, 1502), (11, 1502, 1599), (12, 1599, 1695),
        (13, 1695, 1799), (14, 1799, 1897), (15, 1897, 1969), (16, 1969, 1992),
        (17, 1992, 2012), (18, 2012, 2089),
    ]
    for ch, a, b in bounds:
        if a <= idx < b:
            return ch
    return None


def novel_wc(doc: Document) -> int:
    return sum(len(p.text.split()) for p in doc.paragraphs[109:2089])


def main() -> None:
    # baseline from BEFORE backup for total reporting
    before_doc = Document(str(ROOT / "Schrodingers_Paperwork_BOOK_1_BEFORE_TIGHTEN.docx"))
    before_total = novel_wc(before_doc)

    doc = Document(str(SRC))
    mid = novel_wc(doc)

    applied = []
    skipped = []
    chapters: set[int] = set()
    for idx, new in EDITS.items():
        old = doc.paragraphs[idx].text
        if old == new:
            skipped.append((idx, "unchanged"))
            continue
        # only apply if we're shortening or fixing the unmatched room para
        if words(new) > words(old) + 2:
            skipped.append((idx, f"would lengthen {words(old)}->{words(new)}"))
            continue
        set_paragraph_text(doc.paragraphs[idx], new)
        ch = chapter_of(idx)
        if ch:
            chapters.add(ch)
        applied.append({
            "idx": idx,
            "ch": ch,
            "old_w": words(old),
            "new_w": words(new),
            "cut": words(old) - words(new),
            "old100": old[:100],
            "new100": new[:100],
        })

    after = novel_wc(doc)
    doc.save(str(SRC))

    kindle = ROOT / "Schrodingers_Paperwork_BOOK_1_KINDLE.docx"
    photo = ROOT / "Schrodingers_Paperwork_BOOK_1_Photo_Edition.docx"
    shutil.copy2(SRC, kindle)
    shutil.copy2(SRC, photo)

    body = "\n".join(p.text for p in Document(str(SRC)).paragraphs[109:2089])
    locks = {
        "impersonation of my address": "impersonation of my address" in body,
        "Phase One / checklist Domestic Consolidation": "DOMESTIC CONSOLIDATION VISIT" in body,
        "lie required electricity": "lie required electricity" in body,
        "Fainrose assistant closer": "did you get the idea that you were the assistant" in body,
        "no view from nowhere": "no view from nowhere" in body.lower(),
        "4C not mine": "That is not mine" in body,
        "cast no shadow": "cast no shadow" in body or "He cast no shadow" in body,
        "Mrs Chain sister correction": "Then do not tell me nothing was destroyed" in body,
        "accounts are the scarce": "accounts are the scarce" in body,
        "There is no lid": "There is no lid" in body,
    }

    # Combined best cuts: use before_doc vs after for sample of biggest absolute cuts
    # Recompute against BEFORE for the 5 best samples across both passes by comparing BEFORE text at applied idxs
    samples = []
    for a in applied:
        idx = a["idx"]
        old_b = before_doc.paragraphs[idx].text
        new_a = Document(str(SRC)).paragraphs[idx].text
        cut = words(old_b) - words(new_a)
        if cut > 0:
            samples.append({
                "ch": a["ch"],
                "cut": cut,
                "old100": old_b[:100],
                "new100": new_a[:100],
            })
    # also include pass1-only paragraphs that weren't in EDITS but changed vs before
    # (approximate: scan focus chapters for any shortened vs before)
    focus_ranges = [(109, 260), (459, 658), (816, 954), (1502, 1599), (1599, 1695), (1695, 1799), (1799, 1897), (2012, 2089)]
    after_doc = Document(str(SRC))
    for a, b in focus_ranges:
        for i in range(a, b):
            ob = before_doc.paragraphs[i].text
            na = after_doc.paragraphs[i].text
            if ob != na:
                cut = words(ob) - words(na)
                if cut >= 20:
                    samples.append({
                        "ch": chapter_of(i),
                        "cut": cut,
                        "old100": ob[:100],
                        "new100": na[:100],
                    })
    # unique by old100
    seen = set()
    uniq = []
    for s in sorted(samples, key=lambda x: -x["cut"]):
        key = s["old100"]
        if key in seen:
            continue
        seen.add(key)
        uniq.append(s)
    best = uniq[:5]

    ch_counts = {}
    for a, b in [
        (1, 109, 260), (3, 459, 658), (5, 816, 954), (11, 1502, 1599),
        (12, 1599, 1695), (13, 1695, 1799), (14, 1799, 1897), (18, 2012, 2089),
    ]:
        # fix unpacking
        pass
    ch_after = {}
    for ch, a, b in [
        (1, 109, 260), (3, 459, 658), (5, 816, 954), (11, 1502, 1599),
        (12, 1599, 1695), (13, 1695, 1799), (14, 1799, 1897), (18, 2012, 2089),
    ]:
        bw = sum(len(before_doc.paragraphs[i].text.split()) for i in range(a, b))
        aw = sum(len(after_doc.paragraphs[i].text.split()) for i in range(a, b))
        ch_after[ch] = (bw, aw, bw - aw)

    lines = []
    lines.append("Schrodinger's Paperwork — tighten pass (combined)")
    lines.append(f"Source: {SRC.name}")
    lines.append("Backup: Schrodingers_Paperwork_BOOK_1_BEFORE_TIGHTEN.docx")
    lines.append(f"Novel words before: {before_total}")
    lines.append(f"Novel words after pass1: {mid}")
    lines.append(f"Novel words after pass2: {after}")
    lines.append(f"Words removed total: {before_total - after}")
    lines.append(f"Pass2 paragraphs updated: {len(applied)} (skipped {len(skipped)})")
    lines.append(f"Chapters touched: {sorted(chapters)}")
    lines.append("Synced: KINDLE + Photo_Edition (copied from BOOK_1)")
    lines.append("")
    lines.append("Per-chapter (before -> after, cut):")
    for ch in sorted(ch_after):
        bw, aw, c = ch_after[ch]
        lines.append(f"  Ch{ch}: {bw} -> {aw} (-{c}w)")
    lines.append("")
    lines.append("Continuity locks present:")
    for k, ok in locks.items():
        lines.append(f"  [{'OK' if ok else 'MISSING'}] {k}")
    lines.append("")
    lines.append("Sample of 5 best cuts (old->new, first 100 chars):")
    for i, c in enumerate(best, 1):
        lines.append(f"{i}. Ch{c['ch']} -{c['cut']}w")
        lines.append(f"   OLD: {c['old100']}")
        lines.append(f"   NEW: {c['new100']}")
    if skipped:
        lines.append("")
        lines.append(f"Skipped ({len(skipped)}):")
        for idx, why in skipped[:20]:
            lines.append(f"  {idx}: {why}")

    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    # ASCII-safe console
    print(LOG.read_text(encoding="utf-8").encode("ascii", "replace").decode("ascii"))


if __name__ == "__main__":
    main()
