# -*- coding: utf-8 -*-
"""Aggressive combined tighten: restore-based, index edits targeting ~3000w cut."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn

ROOT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork")
SRC = ROOT / "Schrodingers_Paperwork_BOOK_1.docx"
BAK = ROOT / "Schrodingers_Paperwork_BOOK_1_BEFORE_TIGHTEN.docx"
LOG = ROOT / "_tighten_log.txt"


def set_paragraph_text(paragraph, text: str) -> None:
    for t in paragraph._p.findall(".//" + qn("w:t")):
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


def w(s: str) -> int:
    return len(s.split())


def chapter_of(idx: int) -> int | None:
    for ch, a, b in [
        (1, 109, 260), (2, 260, 459), (3, 459, 658), (4, 658, 816),
        (5, 816, 954), (6, 954, 1082), (7, 1082, 1221), (8, 1221, 1312),
        (9, 1312, 1445), (10, 1445, 1502), (11, 1502, 1599), (12, 1599, 1695),
        (13, 1695, 1799), (14, 1799, 1897), (15, 1897, 1969), (16, 1969, 1992),
        (17, 1992, 2012), (18, 2012, 2089),
    ]:
        if a <= idx < b:
            return ch
    return None


def novel_wc(doc: Document) -> int:
    return sum(len(p.text.split()) for p in doc.paragraphs[109:2089])


# Aggressive rewrites keyed by paragraph index (text from BEFORE_TIGHTEN).
# Protect: Rules, lecture links, impersonation, Phase One checklist, shadow,
# 4C-not-mine, no-view-from-nowhere, lie required electricity, assistant closer,
# Mrs Chain sister correction, accounts scarce, there is no lid.
EDITS: dict[int, str] = {}

# ---- Chapter 1 ----
EDITS[110] = (
    "There are, in the management of large and failing systems, certain sounds one learns to distrust. "
    "The metallic cough of a heating vent, which means either nothing or a catastrophe in the wall. "
    "The clerical thump of an internal memorandum, which means either lunch has moved or civilisation has. "
    "And then there was the soft clicking of the complaint terminal on Lolly Wren’s desk when it had decided, "
    "in its limited but vindictive fashion, that the morning was not going to proceed properly."
)
EDITS[111] = (
    "Lolly looked up from her tea. This was unfortunate for two reasons. The first was that she had not yet had enough of it to be tolerant. "
    "The second was that the tea itself, purchased from a machine on the fourth floor, had the colour and emotional range of varnished disappointment. "
    "The terminal clicked again. Lolly sighed in the manner of a woman who had once trained in theoretical physics and now worked in Transit Reconciliation, "
    "which is rather like studying celestial harmony only to find the stars have gone into local government."
)
EDITS[113] = (
    "Gideon Wigglesworth was one of the few people who visited Lolly there voluntarily, and one of the few she trusted to look at an impossible problem without first asking which form was required. "
    "They had shared a workbench for the better part of a decade, and had kept the habit of each other since. "
    "Gideon was very clever, painfully clumsy, and so agreeable that even the Ministry’s furniture seemed reluctant to injure him. "
    "He appeared carrying two coffees, caught his shoe on the threshold, recovered with surprising dignity, and handed Lolly one of them."
)
EDITS[124] = (
    "The Annex had been designed in the late bureaucratic style: openness in theory, fluorescent headaches in practice. "
    "People came to complain about missed connections, duplicate arrivals, incorrect departures, luggage with philosophical objections to ownership, "
    "and, increasingly, journeys that had happened in the wrong order. Lolly had processed three of those this week. She did not care for trends in metaphysics."
)
EDITS[126] = (
    "There came a brisk knock at the open office door, immediately followed by a woman entering without waiting for permission, "
    "which in Lolly’s experience generally indicated either authority or age. In this case it was age wielded with such competence that it had become authority on its own. "
    "She was in her late sixties, silver hair pinned back with no intention of adjusting it for the convenience of reality, "
    "in a dark coat and sensible shoes, with the expression of a woman who had accepted the collapse of standards in public life as regrettable "
    "but had no intention of accepting the collapse of space-time."
)
EDITS[140] = (
    "Mrs Chain did not answer immediately. Instead she removed her gloves, placed them side by side in her lap, "
    "and said, “I set out this morning to visit my sister in Whitbury-on-Sea.”"
)
EDITS[144] = (
    "“No, Ms Wren, that is rather the problem. I had not fully decided to go, but I had advanced sufficiently in the direction of deciding "
    "that I put on my coat, found my umbrella, and went to the bus stop in order, so to speak, to think transitively.”"
)
EDITS[157] = (
    "“Ms Wren,” she said, “Whitbury-on-Sea is twelve miles from my house. I had not committed to the journey. "
    "One ought not to arrive anywhere before one has properly consented to the inconvenience.”"
)
EDITS[160] = (
    "She glanced at the screen again. The file now read: STATUS: APPROVED RESOLUTION: PASSENGER DELIVERED SUCCESSFULLY "
    "Lolly frowned. Then, before her eyes, it changed. STATUS: MISROUTED RESOLUTION: PASSENGER ARRIVED WITHOUT COMPLETED INTENTION "
    "Then it changed again. STATUS: CLOSED RESOLUTION: NO TRANSIT EVENT DETECTED "
    "Lolly did not move for several seconds. The file waited, smugly."
)
EDITS[171] = (
    "Lolly reached for a pencil. Most officers in Transit Reconciliation used regulation pens because they were permanent, authoritative, and chained to the desk. "
    "Lolly preferred pencil. Pencil admitted the possibility of error, which in her view placed it morally above most institutions. "
    "In the margin of the printed complaint slip she wrote: |journey⟩ = a|not yet taken⟩ + b|already arrived⟩ "
    "She stopped, considered, and added: with a and b being annoyingly nonzero."
)
EDITS[179] = (
    "On the ceiling, the office speaker made a soft ping. A voice of cultivated female neutrality announced, "
    "“Attention staff. Due to the implementation of the Simplification Initiative, all departments are reminded that duplicate interpretations of public events create avoidable confusion. "
    "Please encourage outcomes to settle promptly. Thank you for supporting a clearer tomorrow.”"
)
EDITS[188] = (
    "That, Lolly felt, was unpleasantly fair. She turned back to the terminal and opened the transit record in detail. "
    "A route map appeared, though it was not behaving in a route-like manner. The line representing Mrs Chain’s bus journey seemed to have split in three places "
    "and doubled back through a district which, unless Lolly was badly mistaken, had been a municipal duck pond until last February."
)
EDITS[204] = (
    "Lolly printed the file. This took much longer than it should have, because the printer on her floor had been designed to detect urgency and resent it. "
    "When the sheet finally emerged, it came out warm and faintly humming. She flattened it on the desk."
)
EDITS[217] = (
    "She opened her bottom drawer and took out a thin green notebook labelled, in her own hand, PRIVATE / UNHELPFUL. "
    "She had started it on the day she accepted that Transit Reconciliation would never again require calculus. "
    "It contained several pages of equations, four pages of complaints about the new software, and one pressed bus ticket from a journey that had taken place twice but only on alternate Tuesdays."
)
EDITS[235] = (
    "As if in answer, there came from the corridor the sound of running. People did not run in the Annex unless the kitchen had reopened unexpectedly "
    "or the laws of existence were behaving in a manner likely to reflect badly on management."
)
EDITS[246] = (
    "“Premature arrivals. One man reached a funeral before the deceased had committed. A woman in Clerken Rise got off the tram and found she’d already had lunch tomorrow. "
    "And somebody in East Wexham has reported commuting home to a house listed as an equivalent residence unit.”"
)
EDITS[253] = (
    "Lolly looked from the form to the flickering complaint file, to the private notebook on her desk, to the pale messenger in the doorway, "
    "and at last back to Mrs Chain, who had arrived somewhere before deciding to go there and now seemed, quite reasonably, to require a grown woman to explain the universe. "
    "She wished very much that the tea had been better."
)
EDITS[257] = (
    "Mrs Chain picked up her handbag. “Well,” she said, “that sounds dreadful.” Lolly reached for her coat. “Yes,” she said. “I rather think it does.” "
    "Blankly, almost cheerfully, the printer produced a second sheet all by itself. Across the top it read: FOR THE AVOIDANCE OF CONFUSION "
    "Lolly shut her eyes. This, she felt, was how serious things generally began. Not with thunder. With stationery."
)

# ---- Chapter 3 ----
EDITS[460] = (
    "By half past eleven, Lolly Wren decided that watching reality subdivide before lunch had become, in a professional sense, personal. "
    "She followed Beatrix out of Queue Management with Mrs Chain beside her and Jago materialising wherever least helpful. "
    "Beatrix walked quickly — not hurriedly — and corridors cleared."
)
EDITS[466] = "Beatrix pushed through the revolving doors with the crisp violence of a woman who viewed architecture as a minor procedural obstacle. “We are going to the address.”"
EDITS[472] = (
    "Jago seemed mildly surprised by the question. “Professional curiosity. Also, the courier bag I’m carrying is now addressed to a district that no longer exists, so I feel personally included.”"
)
EDITS[477] = (
    "They took the bus because Beatrix did not trust Ministry pool cars, taxis were on strike across three boroughs for reasons no longer entirely causal, "
    "and Mrs Chain would not pay to revisit her own compromised life."
)
EDITS[478] = (
    "The bus stop opposite the Annex had changed since morning: a plaque praising Civic Flow Modernisation, and a route map showing Chain Terrace, which had not existed at breakfast."
)
EDITS[488] = "The bus arrived at once, which made everyone on the pavement suspicious. Public transport is not meant to behave efficiently without a motive."
EDITS[491] = (
    "Mrs Chain looked up at it with the silence of a woman preparing to dislike something professionally. “What,” she said at last, “is a stable residential cluster.”"
)
EDITS[493] = (
    "They boarded. The driver had the hollow expression of a man ordered all morning to carry passengers to places that had become merely adjacent to where they wanted to go."
)
EDITS[496] = (
    "Lolly sat by the window and watched the city fail to remain itself — not continuously, which would have been easier, but in small indecent increments. "
    "A barber became an orthodontist. A florist became a closed florist. A Victorian pub blurred and resolved into a branch office of the Civic Harmony Board with hanging baskets and no moral centre whatsoever."
)
EDITS[498] = (
    "Gideon Wigglesworth had made the bus by a margin that embarrassed everyone, apologised to the driver and to a pram, and folded himself into the seat across the aisle from Lolly."
)
EDITS[519] = (
    "Gideon got off at the next stop. He had worked out that the quickest way to understand the streets was not to watch them change but to read what had been ordered. "
    "“Find out who signed for it,” Lolly told him. He nodded, walked into the pole by the doors, and was gone before she could thank him."
)
EDITS[520] = (
    "When they got off at Chain Terrace, the weather had the strained brightness of something recently approved by committee. "
    "The street was neat, calm, and appalling — the shape of suburbia without the conviction."
)
EDITS[521] = (
    "Semi-detached houses stood in rows behind low hedges, each acceptable at first glance. At second glance the violations emerged: "
    "numbers fractionally out of sequence, curtains matching too well, identical stone birdbaths weathered in the same place. "
    "A cat sat on a wall with the overdetermined air of an animal generated from survey data."
)
EDITS[522] = (
    "And the clocks were wrong. Lolly noticed that first. One house displayed eleven twenty-three, another eleven nineteen, a third almost noon — "
    "not inaccurately set so much as drawn from different but administratively compatible afternoons."
)
EDITS[524] = (
    "On the far side of the street stood a modest cream-coloured house with blue trim and a small front garden. "
    "Lolly might have called it cheerful had it not looked as if someone had described cheerfulness to a machine and accepted the first draft."
)
EDITS[537] = (
    "Mrs Chain made a soft, offended noise which in another person might have been panic but in her case suggested the prelude to retaliation. “My gate,” she said."
)
EDITS[538] = (
    "Lolly turned back. The gate was there — hinges, latch, the general notion of enclosure — but its history was gone: "
    "the dent, the flake of blue paint, the droop Mrs Chain had resented for years."
)
EDITS[545] = "Lolly bent slightly. The flowers were artificial, in the careful premium manner of a procurement team instructed to provide “warmth.”"
EDITS[550] = (
    "People really living in a place, Lolly felt, introduced minor frictions into it. Shoes with opinions. Keys of varying utility. A newspaper not quite where it should be."
)
EDITS[551] = (
    "This hallway contained an umbrella stand, a narrow mirror, and a bowl for keys, all placed so correctly that none had ever been looked for in irritation."
)
EDITS[557] = (
    "In the first, Mrs Chain stood beside a short man in spectacles whom Lolly assumed had once been her husband. "
    "In the second she stood alone in a garden she did not recognise. In the third she appeared beside a dark-haired woman and a small dog."
)
EDITS[564] = (
    "Lolly followed. It was a good room: armchair, bookshelves, two lamps, a sideboard — the sort one might spend fifteen years improving by tiny, stubborn increments."
)
EDITS[565] = "Only this one had been assembled in one afternoon by an intelligence that understood comfort as a category but not as a memory."
EDITS[566] = (
    "The armchair was too symmetrical. The books were arranged by spine colour in blocks of reassuring compliance. "
    "Three identical coasters sat by the window, because no real household has ever believed in identical coasters."
)
EDITS[567] = (
    "Mrs Chain walked to the mantelpiece. “My husband hated clocks,” she said. “Said they made the room feel supervised. There is now a clock where his photograph should be.”"
)
EDITS[571] = "Lolly joined him. They were indeed books in the legal and physical sense, but not in the intimate one. Their titles were subtly wrong."
EDITS[572] = "Houseplants of Civic Value. Pleasant Soups Through the Year. A Listener’s Guide to Harp Moderation."
EDITS[576] = (
    "There, too, things were nearly right and therefore unbearable. The kettle was stainless steel instead of enamel. "
    "The tea caddy had been labelled HOT BEVERAGE INFUSION MATERIALS. Three mugs hung from hooks, each printed with a motivational saying about mornings."
)
EDITS[577] = (
    "Mrs Chain appeared in the doorway, saw the mugs, and muttered something so compressed and eloquent that Lolly felt it should be preserved for constitutional use."
)
EDITS[583] = (
    "Mrs Chain shut her eyes. “Ms Wren, if at any point it becomes necessary to break the law in order to restore my kitchen, "
    "I should like you to know in advance that I am philosophically available.”"
)
EDITS[584] = (
    "Lolly was about to reply when the wall clock in the sitting room chimed eleven. A moment later, the kitchen clock chimed ten forty-eight. "
    "Then, somewhere upstairs, another clock struck noon with irritating confidence. All four of them froze."
)
EDITS[590] = (
    "Lolly set the tea caddy down carefully. “Someone has made it choose a version before its details match,” she said. “It is trying to look finished and failing.”"
)
EDITS[600] = (
    "Beatrix was already moving again, opening cupboards and checking drawers with the brisk resolve of an auditor committed to making the world justify itself. “In here,” she said."
)
EDITS[601] = "They joined her in a small room at the back of the hall which Mrs Chain identified, with indignation, as the airing cupboard."
EDITS[604] = (
    "Mrs Chain stared at it as if she had finally found the exact point at which civilisation had given up. “It is not optional,” she said."
)
EDITS[619] = "The house, perhaps sensing that it had been discussed too accurately, made a small sound overhead. Not a creak. More a correction."
EDITS[621] = "They returned to find the rectangular mirror in the hall faintly lit. Words were appearing across its surface in blue."
EDITS[625] = (
    "Too late. She struck the mirror smartly across the middle. The text vanished. The mirror cracked in a neat diagonal line and, "
    "for the first time all day, something in the house seemed honestly itself."
)
EDITS[627] = (
    "Beatrix bent to inspect the broken frame. Behind it, fixed to the plaster, was a small grey module no larger than a cigarette case, humming very softly."
)
EDITS[633] = (
    "Lolly took the device in both hands. It was warm. Too warm. “It’s local,” she said. "
    "“The revision isn’t only happening in central records. They’re installing reality correction hardware in people’s houses.”"
)
EDITS[638] = (
    "“If this thing is part of a wider correction network, unplugging it may tell someone that Unit 7B has become ideologically restless.”"
)
EDITS[642] = (
    "The clock vanished, reappeared, and turned into a photograph of a man with spectacles. "
    "The daffodils browned into geraniums, then both at once in a manner Lolly found deeply rude. "
    "The carpet shifted from stripes to faded blue swirls to bare boards and back."
)
EDITS[645] = (
    "Lolly felt the air thicken around her, not physically but informationally, as though the house had ceased to know which version of itself it had been ordered to become."
)
EDITS[649] = (
    "She looked up. At the far end of the hall, where the front door should have shown a small rectangle of afternoon light, "
    "there was now a man in a dark coat standing just inside the threshold. No one had heard him enter."
)
EDITS[650] = (
    "He held a slim case and wore the polished smile of someone whose job consisted of describing intolerable things as procedural necessities."
)
EDITS[652] = (
    "Mrs Chain lifted the umbrella a little higher. The man’s smile remained in place with professional courage. "
    "“I’m afraid,” he said, “someone appears to have interrupted an authorised domestic convergence.”"
)
EDITS[653] = (
    "Lolly looked down at the humming module in her hands, at the cracked mirror, at the photograph that was still trying intermittently to become a clock, "
    "and then back at the man in the doorway. For the first time that day, the problem seemed almost refreshingly simple. “Oh,” she said. “Was that yours.”"
)
EDITS[654] = (
    "At the end of the corridor, a door that had been there ten minutes earlier was no longer there. Lolly wrote its number down before she could forget it. "
    "When she looked again, the number was still in the notebook. The door was not."
)
EDITS[655] = (
    "That was the first time she understood that the Ministry was no longer merely recording errors in reality. It was beginning to acquire them."
)

# ---- Chapter 5 ----
EDITS[817] = (
    "Forty minutes after the interruption of Mrs Elspeth Chain’s domestic convergence, Beatrix Sloan was in an unlicensed grey car with Lolly Wren, Jago Flint, "
    "a confiscated Civic Stability Substrate module, Mrs Chain’s umbrella, and a woman whose house was still fluctuating. "
    "This was witness selection — after documentation and containment, the third response to institutional catastrophe she considered proper, "
    "and reserved for special occasions and senior management."
)
EDITS[818] = (
    "The car belonged to Jago. Or rather, it belonged to a man in Croydon who believed it was in long-term bonded storage, "
    "which was not identical but had, Jago maintained, all the practical advantages of ownership without the correspondence."
)
EDITS[819] = (
    "Lolly sat in the back holding the grey module in both hands, as if it might otherwise begin revising her. "
    "Mrs Chain sat beside her with the umbrella across her knees. Beatrix occupied the front in concentrated disapproval. "
    "Jago drove with one hand and the fatalism of a man who trusted neither maps nor causality."
)
EDITS[826] = (
    "Lolly glanced down at the scratched inscription on the module. If found active in residential field, contact S. Fainrose. She was right. "
    "There is something uniquely disheartening about discovering that a person one has not yet met has already won an argument with the universe."
)
EDITS[828] = (
    "Beatrix was silent for a moment, which in her case meant the answer required enough accuracy to be annoying. "
    "“Former Ministry physicist,” she said at last. “Systems architecture. Interpretive dynamics. Early transition modelling.”"
)
EDITS[831] = (
    "Jago turned left through a yellow light with the lightness of conscience that comes from never recognising traffic law as binding philosophy. "
    "“She used to be very fashionable,” he said. “Brilliant, impossible, terrifying in committee. Left after some unpleasantness involving continuity theory "
    "and a minister who thought eigenstates were a minority voting bloc.”"
)
EDITS[837] = (
    "They drove west. The city thinned gradually, as though suburban planning had set out to continue and then lost conviction. "
    "Office blocks gave way to terraces, then detached houses, then stretches of overmanaged green. "
    "The morning had become one of those bright English afternoons determined to deny the possibility of disaster while helping it along socially."
)
EDITS[838] = (
    "Lolly watched the route display on the dashboard. It altered twice. The first time, their destination changed from Wetherby Lane to Wetherby Approach. "
    "The second time it became Fainrose Cottage / Pending Local Address Reconciliation. She sighed. Jago noticed. “You’ve got to stop taking road systems personally.”"
)
EDITS[841] = (
    "At length they turned off the main road and followed a narrow lane bordered by hedges and old brick walls. "
    "A wrought-iron gate appeared where Lolly would have sworn there had been no gate half a second earlier. "
    "It bore, in flaking black paint, a sign reading: THE INSTITUTE FOR UNHELPFUL CLARITY Visitors by prior argument only No refunds for conclusions Jago braked."
)
EDITS[843] = (
    "Beyond the gate stood a long, low brick house with a slate roof, tall narrow windows, and the defensive air of a property that had spent years discouraging governments. "
    "An old dish antenna had been bolted to one chimney. Three bicycles leaned against a side wall. "
    "On the lawn stood a brass armillary sphere, two folding chairs, and what looked like a weather vane but was almost certainly measuring something less forgivable."
)
EDITS[846] = (
    "Before anyone could knock, the front door opened. Stephanie Fainrose was not tall, and not young, and had the sort of stillness that makes other people feel over-articulated. "
    "She wore a dark cardigan over a pale shirt, narrow trousers, and spectacles that looked less like an accessory than a final administrative judgment upon the human face. "
    "Her hair, cut short and streaked with steel, suggested she had long ago discovered vanity could safely be ignored."
)
EDITS[852] = (
    "They entered. The house smelled of paper, tea, solder, and intellectual impatience. Books lined every wall in layers of active use. "
    "Blackboards leaned against shelves burdened by journals and notebooks labelled in a hand so precise it seemed almost vindictive. "
    "A long table beneath the window held microscopes, mugs, a brass desk lamp, and what Lolly realised with quiet alarm was half of a dismantled detector array."
)
EDITS[857] = (
    "“Yes,” said Fainrose. “A domestic projection stabiliser, third-generation civilian adaptation, vulgar casing, incompetent thermal shielding. "
    "I warned them not to deploy these into lived environments without local phase damping. They said I was being precious.”"
)
EDITS[866] = (
    "She picked up the module with thumb and forefinger, carried it to a bench at the far end of the room, and placed it inside a wire mesh box connected to several cables. "
    "A screen above the bench lit at once with graphs, matrices, and a pulsing red bar marked LOCAL COERCION FIELD."
)
EDITS[874] = (
    "Fainrose pointed at the screen. “This device is not merely enforcing one stable domestic reading. "
    "It’s selecting from multiple possible home-states and driving the property toward whichever one best satisfies central continuity metrics.”"
)
EDITS[880] = (
    "She turned from the screen and looked directly at her. “When a system evolves naturally,” she said, “it doesn’t jump from richness to paperwork. "
    "It moves through lawful change. You can dislike the law, but you may not skip it. They’re imposing an end state without understanding the dynamics that produce one.”"
)
EDITS[890] = (
    "Fainrose paused, perhaps deciding how much truth a person with an umbrella ought to receive at once. "
    "Then she said, “Imagine your home not as a place, but as a cloud of possible details held together by habit, memory, objects, routes through rooms, repeated actions, and expectation.”"
)
EDITS[893] = (
    "Jago smiled openly. Fainrose continued. “Now imagine some administrative imbecile decides this complexity is inefficient. "
    "Instead of letting that cloud develop into the version sustained by your actual life, they force it into a reduced pattern selected for stability and cost. "
    "The trouble is, they don’t understand which details support the rest. So they flatten the system before it has finished cohering.”"
)
EDITS[921] = (
    "Fainrose did not answer at once. Instead she reached for a second keyboard and called up a satellite map, then a network diagram, "
    "then what looked to Lolly like a topological model overlaid with municipal infrastructure. "
    "At the centre of one regional cluster blinked a small black icon. Next to it, in yellow: Singularity Asset 4C Status: Diminishing"
)
EDITS[926] = (
    "No one spoke. This was partly because the statement had arrived with the calm administrative weight of a tea tray "
    "and partly because each of them required a moment to resent the universe properly."
)
EDITS[928] = (
    "Fainrose’s mouth tightened. “Transport curvature, waste density management, long-range compression, several profoundly stupid infrastructure efficiencies from fifteen years ago. "
    "The Ministry likes gravity when it can invoice it.”"
)
EDITS[941] = (
    "Fainrose looked at her with almost maternal disappointment. “Oh, Lolly,” she said, and it was the first time she had used her name, which made the correction land harder, "
    "“of course it can. The only question is whether someone has been foolish enough to make it do so where the public can object.”"
)
EDITS[945] = (
    "“We will leave Mrs Chain’s house for the moment,” she said. “Not because it is unimportant. Because it is now evidence of a larger stupidity. "
    "If they have begun forcing collapse locally and interfering with gravitational anchors centrally, then the system is no longer merely rude. It is unstable.”"
)

# Save remaining edits to continue in part 2 file due to size - actually keep going in same file via second dict merge below
