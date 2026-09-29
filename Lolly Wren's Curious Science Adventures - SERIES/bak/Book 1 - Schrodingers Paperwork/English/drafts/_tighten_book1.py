# -*- coding: utf-8 -*-
"""Tighten BOOK_1: cut joke/descriptive fat in focus chapters; protect locks."""
from __future__ import annotations

import re
import shutil
from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn

ROOT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork")
SRC = ROOT / "Schrodingers_Paperwork_BOOK_1.docx"
LOG = ROOT / "_tighten_log.txt"

# Exact old -> new replacements (paragraph text must match exactly).
REPLACEMENTS: dict[str, str] = {}


def add(old: str, new: str) -> None:
    old = old.strip()
    new = new.strip()
    if old == new:
        raise ValueError("old==new")
    if old in REPLACEMENTS:
        raise ValueError(f"duplicate old key: {old[:60]!r}")
    REPLACEMENTS[old] = new


# ---------------------------------------------------------------------------
# Chapter 1 — tea / celestial-harmony overload (~10% of early long paras)
# ---------------------------------------------------------------------------
add(
    "There are, in the management of large and failing systems, certain sounds one learns to distrust. The metallic cough of a heating vent in late November, for instance, which means either nothing at all or a catastrophe in the wall. The tiny, clerical thump of an internal memorandum landing in the inbox, which means either lunch has been moved to Wednesday or civilisation has. And then there was the particular soft clicking noise made by the complaint terminal on Lolly Wren’s desk when it had decided, in its own limited but vindictive fashion, that the morning was not going to proceed properly.",
    "There are, in the management of large and failing systems, certain sounds one learns to distrust. The metallic cough of a heating vent, which means either nothing or a catastrophe in the wall. The clerical thump of an internal memorandum, which means either lunch has moved or civilisation has. And then there was the soft clicking of the complaint terminal on Lolly Wren’s desk when it had decided, in its limited but vindictive fashion, that the morning was not going to proceed properly.",
)
add(
    "Lolly looked up from her tea. This was unfortunate for two reasons. The first was that she had not yet had enough of it to be tolerant. The second was that the tea itself, purchased in a spirit of optimism from a machine on the fourth floor, had the colour and emotional range of varnished disappointment, and appeared to have taken a personal view of her. The terminal clicked again. Lolly sighed in the manner of a woman who had once trained in theoretical physics and now worked in Transit Reconciliation, which is rather like having spent one’s youth studying celestial harmony only to discover that the stars have all gone into local government.",
    "Lolly looked up from her tea. This was unfortunate for two reasons. The first was that she had not yet had enough of it to be tolerant. The second was that the tea itself, purchased from a machine on the fourth floor, had the colour and emotional range of varnished disappointment. The terminal clicked again. Lolly sighed in the manner of a woman who had once trained in theoretical physics and now worked in Transit Reconciliation, which is rather like studying celestial harmony only to find the stars have gone into local government.",
)
add(
    "Gideon Wigglesworth was one of the few people who visited Lolly there voluntarily. He was also one of the few people Lolly trusted to look at an impossible problem without first asking which form was required. They had shared a workbench for the better part of a decade, back when the problems still came with a soldering iron attached, and had kept the habit of each other since. Gideon was very clever, painfully clumsy, and so generally agreeable that even the Ministry’s furniture seemed reluctant to injure him. He appeared in the doorway carrying two coffees, caught his shoe on the threshold, recovered with surprising dignity, and handed Lolly one of them.",
    "Gideon Wigglesworth was one of the few people who visited Lolly there voluntarily, and one of the few she trusted to look at an impossible problem without first asking which form was required. They had shared a workbench for the better part of a decade, back when the problems still came with a soldering iron attached, and had kept the habit of each other since. Gideon was very clever, painfully clumsy, and so agreeable that even the Ministry’s furniture seemed reluctant to injure him. He appeared carrying two coffees, caught his shoe on the threshold, recovered with surprising dignity, and handed Lolly one of them.",
)
add(
    "The Annex itself had been designed in the late bureaucratic style, meaning that it was thought to promote openness while in fact promoting fluorescent headaches. People came there to complain about missed connections, duplicate arrivals, incorrect departures, luggage with philosophical objections to ownership, and, increasingly over the last several months, journeys that had happened in the wrong order. Lolly had processed three of those this week. She did not care for trends in metaphysics.",
    "The Annex had been designed in the late bureaucratic style: openness in theory, fluorescent headaches in practice. People came to complain about missed connections, duplicate arrivals, incorrect departures, luggage with philosophical objections to ownership, and, increasingly, journeys that had happened in the wrong order. Lolly had processed three of those this week. She did not care for trends in metaphysics.",
)
add(
    "There came a brisk knock at the open office door, immediately followed by a woman entering without waiting for permission, which in Lolly’s experience generally indicated either authority or age. In this case, it was age wielded with such competence that it had become authority on its own. She was in her late sixties, perhaps early seventies, with silver hair pinned back in a way that suggested she had no intention of adjusting it for the convenience of reality. She wore a dark coat, sensible shoes, and the expression of a woman who had once accepted the collapse of standards in public life as regrettable but had no intention of accepting the collapse of space-time.",
    "There came a brisk knock at the open office door, immediately followed by a woman entering without waiting for permission, which in Lolly’s experience generally indicated either authority or age. In this case it was age wielded with such competence that it had become authority on its own. She was in her late sixties, silver hair pinned back with no intention of adjusting it for the convenience of reality, in a dark coat and sensible shoes, with the expression of a woman who had accepted the collapse of standards in public life as regrettable but had no intention of accepting the collapse of space-time.",
)

# ---------------------------------------------------------------------------
# Chapter 3 — house-tour object gags 10–15%; keep impersonation + checklist
# ---------------------------------------------------------------------------
add(
    "Lolly sat by the window and watched the city fail to remain itself — not continuously, which would have been easier, but in small indecent increments. A barber became an orthodontist. A florist became a closed florist. A narrow Victorian pub called The Patient Meteor blurred and resolved into a branch office of the Civic Harmony Board with hanging baskets and no moral centre whatsoever.",
    "Lolly sat by the window and watched the city fail to remain itself — not continuously, which would have been easier, but in small indecent increments. A barber became an orthodontist. A florist became a closed florist. A Victorian pub blurred and resolved into a branch office of the Civic Harmony Board with hanging baskets and no moral centre whatsoever.",
)
add(
    "Semi-detached houses stood in rows behind low hedges, each one acceptable at first glance. At second glance the violations emerged: numbers fractionally out of sequence, curtains matching too well, three identical stone birdbaths weathered in the same place. A cat sat on a wall with the overdetermined air of an animal generated from survey data.",
    "Semi-detached houses stood in rows behind low hedges, each acceptable at first glance. At second glance the violations emerged: numbers fractionally out of sequence, curtains matching too well, identical stone birdbaths weathered in the same place. A cat sat on a wall with the overdetermined air of an animal generated from survey data.",
)
add(
    "And the clocks were wrong. Lolly noticed that first. Not the time itself, though that was bad enough. One house displayed eleven twenty-three in the front room, another eleven nineteen, a third almost noon. Yet all the clocks possessed the same odd quality, as though they were not inaccurately set but drawn from different but administratively compatible afternoons.",
    "And the clocks were wrong. Lolly noticed that first. One house displayed eleven twenty-three, another eleven nineteen, a third almost noon — not inaccurately set so much as drawn from different but administratively compatible afternoons.",
)
add(
    "On the far side of the street stood a modest cream-coloured house with blue trim and a small front garden bordered by white stones. Lolly might have called it cheerful had it not looked so distinctly as if someone had described cheerfulness to a machine and accepted the first draft.",
    "On the far side of the street stood a modest cream-coloured house with blue trim and a small front garden. Lolly might have called it cheerful had it not looked as if someone had described cheerfulness to a machine and accepted the first draft.",
)
add(
    "Lolly turned back. The gate was there, technically — hinges, latch, the general notion of enclosure — but its individual history was gone: the dent, the flake of blue paint, the droop Mrs Chain had resented for years.",
    "Lolly turned back. The gate was there — hinges, latch, the general notion of enclosure — but its history was gone: the dent, the flake of blue paint, the droop Mrs Chain had resented for years.",
)
add(
    "People really living in a place, Lolly felt, introduced minor frictions into it. Shoes with opinions. Hall tables burdened by keys of varying utility. A newspaper not quite where it should be. Umbrellas that remembered rain.",
    "People really living in a place, Lolly felt, introduced minor frictions into it. Shoes with opinions. Keys of varying utility. A newspaper not quite where it should be.",
)
add(
    "This hallway contained an umbrella stand, a narrow mirror, and a bowl for keys, all placed so correctly that none of them had ever once been looked for in irritation.",
    "This hallway contained an umbrella stand, a narrow mirror, and a bowl for keys, all placed so correctly that none had ever been looked for in irritation.",
)
add(
    "In the first, Mrs Chain stood beside a short man in spectacles whom Lolly assumed had once been her husband. In the second she stood alone in a garden she did not recognise. In the third she appeared beside a dark-haired woman and a small white dog.",
    "In the first, Mrs Chain stood beside a short man in spectacles whom Lolly assumed had once been her husband. In the second she stood alone in a garden she did not recognise. In the third she appeared beside a dark-haired woman and a small dog.",
)
add(
    "It was a good room. Comfortable armchair. Bookshelves. Two lamps. A sideboard. The sort of room one might spend fifteen years improving by tiny, stubborn increments.",
    "It was a good room: armchair, bookshelves, two lamps, a sideboard — the sort one might spend fifteen years improving by tiny, stubborn increments.",
)
add(
    "Only this one had clearly been assembled in one afternoon by an intelligence that understood comfort as a category but not as a memory.",
    "Only this one had been assembled in one afternoon by an intelligence that understood comfort as a category but not as a memory.",
)
add(
    "The armchair was too symmetrical. The books were arranged by spine colour in blocks of reassuring compliance. A table by the window held three coasters, each identical, because no real household has ever believed in identical coasters.",
    "The armchair was too symmetrical. The books were arranged by spine colour in blocks of reassuring compliance. Three identical coasters sat by the window, because no real household has ever believed in identical coasters.",
)
add(
    "The Collected Coasts of Sussex. Houseplants of Civic Value. Pleasant Soups Through the Year. A Listener’s Guide to Harp Moderation.",
    "Houseplants of Civic Value. Pleasant Soups Through the Year. A Listener’s Guide to Harp Moderation.",
)
add(
    "There, too, things were nearly right and therefore unbearable. The kettle was stainless steel instead of enamel. The tea caddy had been labelled HOT BEVERAGE INFUSION MATERIALS in a neat Ministry hand. Three mugs hung from hooks, each printed with a motivational saying about mornings.",
    "There, too, things were nearly right and therefore unbearable. The kettle was stainless steel instead of enamel. The tea caddy had been labelled HOT BEVERAGE INFUSION MATERIALS. Three mugs hung from hooks, each printed with a motivational saying about mornings.",
)
add(
    "Mrs Chain appeared in the doorway, saw the mugs, and muttered something so compressed and eloquent that Lolly felt it should possibly be preserved for future constitutional use.",
    "Mrs Chain appeared in the doorway, saw the mugs, and muttered something so compressed and eloquent that Lolly felt it should be preserved for constitutional use.",
)
add(
    "Lolly set the tea caddy down very carefully, as one does with explosive materials and herbal substitutes. “Someone has made it choose a version before its details match,” she said. “It is trying to look finished and failing.”",
    "Lolly set the tea caddy down carefully. “Someone has made it choose a version before its details match,” she said. “It is trying to look finished and failing.”",
)
add(
    "Beatrix was already moving again, opening cupboards, checking drawers, pulling at labels with the brisk resolve of an auditor committed to making the world justify itself. “In here,” she said.",
    "Beatrix was already moving again, opening cupboards and checking drawers with the brisk resolve of an auditor committed to making the world justify itself. “In here,” she said.",
)
add(
    "The clock vanished, reappeared, and turned into a photograph of a man with spectacles. The daffodils in the hall browned into geraniums, then back again, then both at once in a manner Lolly found deeply rude. The carpet pattern shifted underfoot from stripes to faded blue swirls to bare boards and back.",
    "The clock vanished, reappeared, and turned into a photograph of a man with spectacles. The daffodils browned into geraniums, then both at once in a manner Lolly found deeply rude. The carpet shifted from stripes to faded blue swirls to bare boards and back.",
)
add(
    "Lolly felt the air thicken around her, not physically but informationally, as though the house had ceased to know which version of itself it had most recently been ordered to become.",
    "Lolly felt the air thicken around her, not physically but informationally, as though the house had ceased to know which version of itself it had been ordered to become.",
)
add(
    "He held a slim case in one hand and wore the faint, polished smile of someone whose job consisted entirely of describing intolerable things as procedural necessities.",
    "He held a slim case and wore the polished smile of someone whose job consisted of describing intolerable things as procedural necessities.",
)
add(
    "They took the bus because Beatrix did not trust Ministry pool cars, taxis were on strike across three adjacent boroughs for reasons no longer entirely causal, and Mrs Chain maintained with some force that she would not pay to revisit her own compromised life.",
    "They took the bus because Beatrix did not trust Ministry pool cars, taxis were on strike across three boroughs for reasons no longer entirely causal, and Mrs Chain would not pay to revisit her own compromised life.",
)
add(
    "The bus stop opposite the Annex had changed since morning: timetable three inches left, a plaque praising Civic Flow Modernisation, and a route map showing Chain Terrace, which had not existed at breakfast.",
    "The bus stop opposite the Annex had changed since morning: a plaque praising Civic Flow Modernisation, and a route map showing Chain Terrace, which had not existed at breakfast.",
)
add(
    "The bus arrived at once, which made everyone on the pavement suspicious. Public transport is not meant to behave efficiently without a motive, and preferably a consultation period.",
    "The bus arrived at once, which made everyone on the pavement suspicious. Public transport is not meant to behave efficiently without a motive.",
)
add(
    "They boarded. The driver had the hollow, resigned expression of a man who had spent the morning being ordered to carry passengers to places that had become technically adjacent to where they wanted to go.",
    "They boarded. The driver had the hollow expression of a man ordered all morning to carry passengers to places that had become merely adjacent to where they wanted to go.",
)
add(
    "When they got off at Chain Terrace, the weather had acquired the strained brightness of something that had recently been approved by committee. The street itself was neat, calm, and appalling. It had the shape of suburbia but not the conviction.",
    "When they got off at Chain Terrace, the weather had the strained brightness of something recently approved by committee. The street was neat, calm, and appalling — the shape of suburbia without the conviction.",
)
add(
    "Lolly bent slightly. The flowers were, indeed, artificial, but in the careful premium manner of a procurement team that had been instructed to provide “warmth.”",
    "Lolly bent slightly. The flowers were artificial, in the careful premium manner of a procurement team instructed to provide “warmth.”",
)
add(
    "Mrs Chain made a soft, offended noise which in another person might have been panic but in her case suggested the prelude to effective retaliation. “My gate,” she said.",
    "Mrs Chain made a soft, offended noise which in another person might have been panic but in her case suggested the prelude to retaliation. “My gate,” she said.",
)
add(
    "Gideon got off at the next stop. He had worked out that the quickest way to understand the streets was not to watch them change but to read what had been ordered. “Find out who signed for it,” Lolly told him. He nodded, walked into the pole by the doors, and was gone before she could thank him. From the pavement he raised a hand a beat longer than a wave required, and then the traffic took him.",
    "Gideon got off at the next stop. He had worked out that the quickest way to understand the streets was not to watch them change but to read what had been ordered. “Find out who signed for it,” Lolly told him. He nodded, walked into the pole by the doors, and was gone before she could thank him. From the pavement he raised a hand, and then the traffic took him.",
)

# ---------------------------------------------------------------------------
# Chapter 5 — shorten overpacked car/list opener + nearby descriptive fat
# ---------------------------------------------------------------------------
add(
    "Forty minutes after the interruption of Mrs Elspeth Chain’s domestic convergence, Beatrix Sloan was in an unlicensed grey car with Lolly Wren, Jago Flint, a confiscated Civic Stability Substrate module, one morally indignant umbrella, and a woman whose house was fluctuating between several unsatisfactory versions of itself. This was, by her own private reckoning, witness selection — the third of the only three responses to institutional catastrophe she considered proper, the first being documentation and the second containment, and reserved, as a rule, for special occasions and senior management.",
    "Forty minutes after the interruption of Mrs Elspeth Chain’s domestic convergence, Beatrix Sloan was in an unlicensed grey car with Lolly Wren, Jago Flint, a confiscated Civic Stability Substrate module, Mrs Chain’s umbrella, and a woman whose house was still fluctuating. This was witness selection — after documentation and containment, the third response to institutional catastrophe she considered proper, and reserved for special occasions and senior management.",
)
add(
    "Lolly sat in the back holding the grey module in both hands, as if it might otherwise begin revising her. Mrs Chain sat beside her with the umbrella across her knees like a constitutional amendment awaiting use. Beatrix occupied the front passenger seat in a state of concentrated disapproval. Jago drove with one hand and the relaxed fatalism of a man who trusted neither maps nor causality.",
    "Lolly sat in the back holding the grey module in both hands, as if it might otherwise begin revising her. Mrs Chain sat beside her with the umbrella across her knees. Beatrix occupied the front in concentrated disapproval. Jago drove with one hand and the fatalism of a man who trusted neither maps nor causality.",
)
add(
    "Lolly glanced down at the scratched inscription on the module, though she already knew every stroke of it by heart. If found active in residential field, contact S. Fainrose. She was right. She had been trying, without great success, not to dwell on the final sentence. There is something uniquely disheartening about the discovery that a person one has not yet met has already won an argument with the universe.",
    "Lolly glanced down at the scratched inscription on the module. If found active in residential field, contact S. Fainrose. She was right. There is something uniquely disheartening about discovering that a person one has not yet met has already won an argument with the universe.",
)
add(
    "They drove west. The city thinned gradually, as though suburban planning had once set out to continue and then lost conviction. Office blocks gave way to terraces, terraces to detached houses, detached houses to stretches of overmanaged green in which municipal trees stood at intervals suggesting budget approval. The morning had developed into one of those bright English afternoons which seem determined, against all meteorological instinct, to deny the possibility of disaster while helping it along socially.",
    "They drove west. The city thinned gradually, as though suburban planning had set out to continue and then lost conviction. Office blocks gave way to terraces, then detached houses, then stretches of overmanaged green. The morning had become one of those bright English afternoons determined to deny the possibility of disaster while helping it along socially.",
)
add(
    "Beyond the gate stood a long, low brick house with a slate roof, tall narrow windows, and the defensive air of a property that had spent years discouraging governments. An old dish antenna had been bolted to one chimney. Three bicycles leaned against a side wall in ways suggesting neither sport nor leisure. On the lawn stood a brass armillary sphere, two folding chairs, and what appeared at first glance to be a weather vane but, on closer inspection, was almost certainly measuring something less forgivable.",
    "Beyond the gate stood a long, low brick house with a slate roof, tall narrow windows, and the defensive air of a property that had spent years discouraging governments. An old dish antenna had been bolted to one chimney. Three bicycles leaned against a side wall. On the lawn stood a brass armillary sphere, two folding chairs, and what looked like a weather vane but was almost certainly measuring something less forgivable.",
)
add(
    "Before anyone could knock, the front door opened. Stephanie Fainrose was not tall, and not young, and had the sort of stillness that makes other people feel physically over-articulated. She wore a dark cardigan over a pale shirt, narrow trousers, and spectacles that looked less like an accessory than a final administrative judgment upon the human face. Her hair, cut short and streaked with steel, suggested she had long ago discovered vanity to be one of several forces in the universe that could safely be ignored.",
    "Before anyone could knock, the front door opened. Stephanie Fainrose was not tall, and not young, and had the sort of stillness that makes other people feel over-articulated. She wore a dark cardigan over a pale shirt, narrow trousers, and spectacles that looked less like an accessory than a final administrative judgment upon the human face. Her hair, cut short and streaked with steel, suggested she had long ago discovered vanity could safely be ignored.",
)
add(
    "They entered. The house smelled of paper, tea, solder, and intellectual impatience. Books lined every wall, not decoratively but in layers of active use. Blackboards leaned against shelves already burdened by journals, manuals, and notebooks labelled in a hand so precise it seemed almost vindictive. A long table beneath the window held three microscopes, two mugs, several stacked crockery plates, a brass desk lamp, and what Lolly realised with quiet alarm was half of a dismantled detector array.",
    "They entered. The house smelled of paper, tea, solder, and intellectual impatience. Books lined every wall in layers of active use. Blackboards leaned against shelves burdened by journals and notebooks labelled in a hand so precise it seemed almost vindictive. A long table beneath the window held microscopes, mugs, a brass desk lamp, and what Lolly realised with quiet alarm was half of a dismantled detector array.",
)
add(
    "Jago turned left through a yellow light with the lightness of conscience that comes from never having truly recognised traffic law as binding philosophy. “She used to be very fashionable,” he said. “Brilliant, impossible, terrifying in committee. Left after some unpleasantness involving continuity theory and a minister who thought eigenstates were a minority voting bloc.”",
    "Jago turned left through a yellow light with the lightness of conscience that comes from never recognising traffic law as binding philosophy. “She used to be very fashionable,” he said. “Brilliant, impossible, terrifying in committee. Left after some unpleasantness involving continuity theory and a minister who thought eigenstates were a minority voting bloc.”",
)

# ---------------------------------------------------------------------------
# Chapter 11 — trim Keinschein monologue ~120–180w; keep shadow / 4C / nowhere
# ---------------------------------------------------------------------------
add(
    "He had a great disorganised nimbus of white hair, a moustache of magnificent indifference, a cardigan that had clearly outlived several arguments, and no shoes. His face was one that everyone in the room had seen a hundred times on posters, mugs, motivational calendars, and the walls of secondary-school physics laboratories. The resemblance was so complete, so unembarrassed, that it produced not recognition but a sort of vertigo.",
    "He had a great disorganised nimbus of white hair, a moustache of magnificent indifference, a cardigan that had outlived several arguments, and no shoes. His face was one everyone in the room had seen on posters, mugs, and the walls of secondary-school physics laboratories. The resemblance was so complete that it produced not recognition but a sort of vertigo.",
)
add(
    "“I do not drink blood, Mrs Chain. Blood is a courier. It carries the thing but it is not the thing.” He laced his old, spotted hands together. “When a question is put to the world, and the world, which had been holding several answers at once quite comfortably, is obliged to produce one, the other answers are not filed. They cease, and in ceasing they release something.” He shrugged, almost apologetically. “I take that. I have taken it since the first measurement, which was much longer ago than your people think and was not performed by anybody.”",
    "“I do not drink blood, Mrs Chain. Blood is a courier. It carries the thing but it is not the thing.” He laced his old hands together. “When a question is put to the world, and the world, which had been holding several answers at once, is obliged to produce one, the other answers are not filed. They cease, and in ceasing they release something.” He shrugged, almost apologetically. “I take that. I have taken it since the first measurement, which was much longer ago than your people think.”",
)
add(
    "“Nine thousand dwellings,” he said, “each one forced from a rich state into a thin one, tens of thousands of alternatives extinguished per address, per week, at public expense, with certificates. Do you understand what that is, from where I sit? It is not a meal. A meal is a woman deciding at last which of two men she loved and letting the other life go. Sweet. Small. I have lived on such things for aeons and been perfectly content.” He spread his hands. “This is industry. This is a national programme with a budget line.”",
    "“Nine thousand dwellings,” he said, “each forced from a rich state into a thin one, tens of thousands of alternatives extinguished per address, per week, at public expense, with certificates. Do you understand what that is, from where I sit? It is not a meal. A meal is small — a woman deciding at last which of two lives to keep. I have lived on such things for aeons and been content.” He spread his hands. “This is industry. A national programme with a budget line.”",
)
add(
    "“No,” he said. “That is not mine, and I want it understood. I did not ask them to build a sink and I did not ask them to hang a county from an evaporating hole. That is not appetite, Dr Fainrose; that is waste, and it will end with the pantry on fire.” He sat forward. “This is why I have come. Not to gloat. I could have gloated from Vienna.”",
    "“No,” he said. “That is not mine, and I want it understood. I did not ask them to build a sink or hang a county from an evaporating hole. That is not appetite, Dr Fainrose; that is waste, and it will end with the pantry on fire.” He sat forward. “This is why I have come. Not to gloat.”",
)
add(
    "“Houses I can dine on for a century. But memory is not a house. A memory is the record of which branch was taken. It is how the universe keeps its accounts.” He tapped the cover. “If you begin collapsing memory by questionnaire, you are not merely extinguishing alternatives. You are falsifying the ledger of which alternatives were extinguished. Then nobody can tell what happened, including me, including the thing that comes after me, including—and this should worry you most—the system that is currently trying to repair itself.”",
    "“Houses I can dine on for a century. But memory is not a house. A memory is the record of which branch was taken — how the universe keeps its accounts.” He tapped the cover. “If you begin collapsing memory by questionnaire, you are not merely extinguishing alternatives. You are falsifying the ledger. Then nobody can tell what happened — including me, including the thing that comes after me, including the system that is currently trying to repair itself.”",
)
add(
    "“Yes,” said Keinschein, and looked at her with real approval. “Yes, the girl has it. Your Dr Fainrose is quite right that the country can be recovered from its correlations rather than from a copy. But a correlation is a statement about what agrees with what. If you go through the population asking leading questions about what they remember, and each answer becomes true as it is given, then the agreements will be manufactured, and the syndrome will be clean, and the code will report itself intact, and it will be intact—around nothing.”",
    "“Yes,” said Keinschein, and looked at her with real approval. “Yes, the girl has it. Your Dr Fainrose is right that the country can be recovered from its correlations rather than from a copy. But a correlation is a statement about what agrees with what. If you ask leading questions about what people remember, and each answer becomes true as it is given, then the agreements will be manufactured, the syndrome will be clean, and the code will report itself intact — around nothing.”",
)
add(
    "“It would be a successful recovery,” said Keinschein. “Of the wrong state. Certified. Permanently. With no residue for anyone to appeal to, and no residue for anyone to eat.” He sat back. “I have been dining on your species’ abandoned lives since before you had knees worth mentioning, and I have never once had to explain to a government that a thing can be irrecoverable. You have made me pedagogical. I resent it.”",
    "“It would be a successful recovery,” said Keinschein. “Of the wrong state. Certified. Permanently. With no residue for anyone to appeal to, and no residue for anyone to eat.” He sat back. “I have been dining on your species’ abandoned lives for a very long time, and I have never once had to explain to a government that a thing can be irrecoverable. You have made me pedagogical. I resent it.”",
)
add(
    "“Entirely for my own reasons,” said Keinschein. “Mrs Chain, I am eleven thousand times your age and I have never once acted from virtue. But my reasons and yours are, this month, pointing in the same direction, and you are in no position to be choosy about your allies.” He glanced at the boxes. “Also, I am the only one of you who has read Phase Two, because I was invited into it at approximately half past ten this morning by a Deputy Under-Secretary who filled in a form about his mother.”",
    "“Entirely for my own reasons,” said Keinschein. “Mrs Chain, I am eleven thousand times your age and I have never once acted from virtue. But my reasons and yours are, this month, pointing the same way, and you are in no position to be choosy about allies.” He glanced at the boxes. “Also, I am the only one of you who has read Phase Two — invited into it this morning by a Deputy Under-Secretary who filled in a form about his mother.”",
)
add(
    "“You write,” said Keinschein, “as though a measurement were an event: a thing that happens at a time, after which there is one answer.” He shook his great white head gently. “That is the working assumption of every laboratory on this planet. It has served you admirably. It is not true. When your Mr Venn scanned Mrs Chain’s mantelpiece, what became definite for Mr Venn did not become definite for the mantelpiece, or the county, or me. There is no single moment at which the universe decides. There is only a widening region of agreement, spreading out at the speed of gossip, and no fact of the matter about the parts it has not reached.”",
    "“You write,” said Keinschein, “as though a measurement were an event: a thing that happens at a time, after which there is one answer.” He shook his great white head gently. “That is the working assumption of every laboratory on this planet. It has served you admirably. It is not true. When your Mr Venn scanned Mrs Chain’s mantelpiece, what became definite for Mr Venn did not become definite for the mantelpiece, or the county, or me. There is no single moment at which the universe decides — only a widening region of agreement, spreading at the speed of gossip, and no fact of the matter about the parts it has not reached.”",
)
add(
    "“He froze it for the grid,” said Keinschein. “Not for the woman remembering her sister. She was inside. Different question. Different answer. She could feel the shape of the name, could she not? She told them so, and they marked it no action required.” He rose from the chair with an old man’s effort and an entirely different creature’s economy. “There is no view from nowhere, Ms Wren. Your Ministry believes it is standing outside the room. It is not. There is no outside. When it finally asks its great national question about what everybody remembers, it will not be reading the answer.”",
    "“He froze it for the grid,” said Keinschein. “Not for the woman remembering her sister. She was inside. Different question. Different answer. She could feel the shape of the name — she told them so, and they marked it no action required.” He rose with an old man’s effort and an entirely different creature’s economy. “There is no view from nowhere, Ms Wren. Your Ministry believes it is standing outside the room. It is not. There is no outside. When it finally asks what everybody remembers, it will not be reading the answer.”",
)
add(
    "“That is the local word and I have stopped resisting it,” said Keinschein. “It is roughly as accurate as calling the sun a lamp. But yes. Approximately. Functionally. For our purposes this afternoon: yes.”",
    "“That is the local word and I have stopped resisting it,” said Keinschein. “It is roughly as accurate as calling the sun a lamp. But yes — approximately, functionally, for our purposes this afternoon.”",
)
add(
    "“On the discarded branch, yes. The road not taken, as your poet had it—though he was sentimental and I am a diner.”",
    "“On the discarded branch, yes. The road not taken — though your poet was sentimental and I am a diner.”",
)

# ---------------------------------------------------------------------------
# Chapter 12 — cut one Duc origin anecdote; shorten long speeches; keep locks
# ---------------------------------------------------------------------------
add(
    "The man standing over her was slight, elderly, and dressed with an exactness that had gone out of fashion so long ago that it had returned as a moral position: a dark suit of beautiful cut and considerable age, a stiff collar, a narrow grey tie, and gloves. He held a hat. He gave the impression of a person who had been standing there for some time, waiting to be noticed, and who considered impatience a failure of breeding.",
    "The man standing over her was slight, elderly, and dressed with an exactness that had gone out of fashion so long ago it had returned as a moral position: a dark suit of beautiful cut, a stiff collar, a narrow grey tie, and gloves. He held a hat. He gave the impression of someone who had been waiting to be noticed, and who considered impatience a failure of breeding.",
)
add(
    "“Not the object. The shape of it. Dr Fainrose quoted four of your lines to me on the telephone this morning to complain about them, which is the highest form of French compliment and, I understand, common enough in English also.” He looked at the wall. “May I sit? It is a long time since I have sat on a wall and I should like to know whether it is still possible.”",
    "“Not the object. The shape of it. Dr Fainrose quoted four of your lines to me this morning to complain about them, which is the highest form of French compliment.” He looked at the wall. “May I sit? It is a long time since I have sat on a wall and I should like to know whether it is still possible.”",
)
add(
    "“I was twenty-two years of age. I had taken my degree in history.” He said it without emphasis. “Medieval history. My family had been soldiers and diplomats for six hundred years and I was, by inclination, an archivist. I intended to spend my life on charters and legal instruments of the fourteenth century. My brother was the physicist. I was the one who read.”",
    "“I was twenty-two. I had taken my degree in history.” He said it without emphasis. “My family had been soldiers and diplomats for six hundred years and I was, by inclination, an archivist. My brother was the physicist. I was the one who read.”",
)
# Cut Einstein/thesis origin anecdote; keep outsider lesson via adjacent paras.
add(
    "“I was right,” said de Brévanne, “and it took four years to say it properly. When I said it, my examiners did not believe it, and my thesis was sent to Einstein because nobody else was willing to have an opinion. He wrote back that I had lifted a corner of the great veil.” A pause. “He also said, privately, that if I were wrong it was a very handsome error. He was always careful to leave himself the exit.”",
    "“I was right,” said de Brévanne, “and it took four years to say it properly. When I said it, my examiners did not believe it. That is usually how it goes.”",
)
add(
    "“In 1911 my brother served as secretary to a congress of physicists,” said de Brévanne, “and brought home the papers. I read them because I read everything. I did not understand them, and I could not stop.” He turned the hat over in his gloved hands. “You must understand my position. I had no laboratory. I had no mathematics beyond the ordinary. I had no standing whatever. What I had was the habit of a historian, which is this: when two authorities disagree, one does not choose. One looks for the document they have both misread.”",
    "“In 1911 my brother served as secretary to a congress of physicists,” said de Brévanne, “and brought home the papers. I read them because I read everything. I did not understand them, and I could not stop.” He turned the hat over in his gloved hands. “I had no laboratory, no standing, no mathematics beyond the ordinary. What I had was the habit of a historian: when two authorities disagree, one does not choose. One looks for the document they have both misread.”",
)
add(
    "“Light,” said de Brévanne, “which everybody knew was a wave, and which Einstein had shown behaved in some circumstances as though it were a great number of small hard things.” He shrugged very slightly. “The physicists were embarrassed by this. They spoke of it as a difficulty to be managed. I was not embarrassed, because I was not a physicist, and so I did the thing that only an ignorant man would do, which was to take it seriously in both directions at once.”",
    "“Light,” said de Brévanne, “which everybody knew was a wave, and which Einstein had shown behaved in some circumstances as though it were a great number of small hard things.” He shrugged. “The physicists were embarrassed; they spoke of it as a difficulty to be managed. I was not embarrassed, because I was not a physicist, and so I did the thing only an ignorant man would do: take it seriously in both directions at once.”",
)
add(
    "“Everyone was asking how a wave could be a particle.” He looked at Lolly. “Nobody was asking whether a particle might be a wave. It is the same question turned round, Ms Wren. Turning a question round is not a discovery; it is a manner. It required no apparatus and no genius. It required only somebody outside the room, with the wrong training, who did not know which of the two facts he was supposed to find awkward.”",
    "“Everyone was asking how a wave could be a particle.” He looked at Lolly. “Nobody was asking whether a particle might be a wave. Turning a question round is not a discovery; it is a manner. It required no apparatus and no genius — only somebody outside the room, with the wrong training, who did not know which of the two facts he was supposed to find awkward.”",
)
add(
    "“No.” De Brévanne’s voice was suddenly quite firm. “That is a comforting story and I dislike it. The outsider usually gets nothing and dies unpublished, and there is no justice in the distribution. I am telling you something narrower and more useful.” He set the hat down on the wall. “Ms Wren, you have said that every observation in your notebook has turned out to have a name already. Tell me: which of them did you write down before you were told the name?”",
    "“No.” De Brévanne’s voice was suddenly quite firm. “That is a comforting story and I dislike it. The outsider usually gets nothing and dies unpublished. I am telling you something narrower.” He set the hat down on the wall. “Ms Wren, every observation in your notebook has a name already. Which of them did you write down before you were told the name?”",
)
add(
    "“No,” said de Brévanne. “That is my point. You are treating the pre-existence of the name as evidence that the observation was worthless. It is evidence that the observation was correct.” He let that sit. “There are two ways to hold a piece of physics. One may receive it, in which case one possesses a fact and may repeat it. Or one may arrive at it, in which case one possesses the reason and may go on from there to the next thing, which has no name yet. The second is the only kind that is any use in a crisis, and it is the only kind you have. You are sitting on a wall in a car park despising yourself for it.”",
    "“No,” said de Brévanne. “That is my point. You are treating the pre-existence of the name as evidence that the observation was worthless. It is evidence that the observation was correct.” He let that sit. “One may receive a piece of physics, and possess a fact one can repeat. Or one may arrive at it, and possess the reason, and go on to the next thing, which has no name yet. The second is the only kind that is any use in a crisis, and it is the only kind you have. You are sitting on a wall despising yourself for it.”",
)
add(
    "Somewhere behind her, on the other side of the annex wall, a phone began ringing and did not stop for a long time. When it cut off, Jago’s voice carried across the car park in fragments—a district name, the word “live” repeated twice, a number she did not quite catch—and Lolly understood, without turning round, that Phase Two was still spreading while she sat on a wall discussing 1911.",
    "Somewhere behind her a phone began ringing and did not stop for a long time. When it cut off, Jago’s voice carried across the car park in fragments — a district name, the word “live” — and Lolly understood, without turning round, that Phase Two was still spreading while she sat on a wall discussing 1911.",
)
add(
    "“Dr Fainrose is formidable and will save perhaps nine thousand houses this week,” said de Brévanne. “But she cannot hear the question she was trained out of hearing. That is not a criticism. It is what training is for. It is expensive and necessary, and it costs precisely one thing.” He picked up the hat again. “Now. Keinschein told you last night that there is no view from nowhere, and that nothing is definite until agreement has spread. It frightened you.”",
    "“Dr Fainrose is formidable and will save perhaps nine thousand houses this week,” said de Brévanne. “But she cannot hear the question she was trained out of hearing. That is not a criticism; it is what training costs.” He picked up the hat again. “Now. Keinschein told you last night that there is no view from nowhere, and that nothing is definite until agreement has spread. It frightened you.”",
)
add(
    "“Good. It should. It is also not the only available account, and he did not tell you that because he is an old snob who enjoys the vertigo.” De Brévanne looked out at the car park, at the pale curve of the annex wall, at the air above the concrete that still did not quite admit to its own distances. “May I show you the other one? It is mine, unfashionable, and I have been out of favour for eighty years, which gives a man leisure to be sure.”",
    "“Good. It should. It is also not the only available account, and he did not tell you that because he is an old snob who enjoys the vertigo.” De Brévanne looked out at the car park. “May I show you the other one? It is mine, unfashionable, and I have been out of favour for eighty years, which gives a man leisure to be sure.”",
)
add(
    "“Suppose the house always had one definite configuration. One actual wallpaper. Not a haze of possibilities: an actual state, at every moment, as common sense insists and as your Ministry pretends to believe.” De Brévanne raised one gloved finger. “And suppose, in addition, there exists a wave: a real physical wave, not a bookkeeping device, spread out over every configuration the house might have had, including the ones it did not have. Suppose the actual configuration is guided by that wave. Steered. Never anywhere but somewhere, yet always told where to go next by a thing that fills the whole space of alternatives.”",
    "“Suppose the house always had one definite configuration. One actual wallpaper — not a haze of possibilities: an actual state, at every moment, as common sense insists and as your Ministry pretends to believe.” De Brévanne raised one gloved finger. “And suppose there exists a wave: a real physical wave, spread over every configuration the house might have had, including the ones it did not. Suppose the actual configuration is guided by that wave — steered, never anywhere but somewhere, yet always told where to go next by a thing that fills the whole space of alternatives.”",
)
add(
    "“He did not create a fact. There was already a fact.” De Brévanne’s voice sharpened for the first time. “He deformed the guidance. He put his apparatus into the space of alternatives and altered the shape of the wave steering a hundred years of that woman’s household. The actual configuration went where the deformed wave sent it, which was somewhere thin. When Mr Flint tore the cable out, the deformation ceased, and the guidance relaxed towards what it had always been. The flowers came back, not because they had been in storage, but because the wave that had always contained them was permitted, briefly, to matter again.”",
    "“He did not create a fact. There was already a fact.” De Brévanne’s voice sharpened for the first time. “He deformed the guidance. He put his apparatus into the space of alternatives and altered the wave steering that woman’s household. The actual configuration went where the deformed wave sent it — somewhere thin. When Mr Flint tore the cable out, the deformation ceased, and the guidance relaxed. The flowers came back not because they had been in storage, but because the wave that had always contained them was permitted, briefly, to matter again.”",
)
add(
    "“It is an entirely different crime,” said de Brévanne, “and this is my lesson, and the only thing I came to say.” He turned to face her fully. “Ms Sloan is upstairs building a case that the Ministry falsified records. That is true and it is small. Dr Fainrose is building a case that they interfered with lawful evolution. That is truer and larger. But if what I have described is so, then every single thing they have done—the queue, the scanner, the certificates, the continuous assurance, and now the memories—was not an intrusion into knowledge.”",
    "“It is an entirely different crime,” said de Brévanne, “and this is my lesson, and the only thing I came to say.” He turned to face her. “Ms Sloan is upstairs building a case that the Ministry falsified records — true, and small. Dr Fainrose is building a case that they interfered with lawful evolution — truer, and larger. But if what I have described is so, then everything they have done — the queue, the scanner, the certificates, the continuous assurance, and now the memories — was not an intrusion into knowledge.”",
)
add(
    "“But if the wave is real—if it is a physical thing out there in configuration space—then it is not information anybody has to store. It is not a bookkeeping quantity that got lost.” She looked up. “It is still there. Deformed, but there. You would not restore the country from a copy. You would restore it by taking your apparatus out of the wave and letting the guidance relax.”",
    "“But if the wave is real — a physical thing in configuration space — then it is not information anybody has to store.” She looked up. “It is still there. Deformed, but there. You would not restore the country from a copy. You would restore it by taking your apparatus out of the wave and letting the guidance relax.”",
)
add(
    "“There are people who would recognise the shape of it,” said de Brévanne. “There is no one who has said it about a country.” He rose, set his hat on his head, and adjusted it. “You will now go upstairs and say it to Dr Fainrose. She will tell you it is unfalsifiable metaphysics and a hundred years out of fashion. She will be quite right on both counts. Then she will be unable to sleep, because it also happens to specify a procedure, and hers does not.”",
    "“There are people who would recognise the shape of it,” said de Brévanne. “There is no one who has said it about a country.” He rose and set his hat on his head. “You will now go upstairs and say it to Dr Fainrose. She will tell you it is unfalsifiable metaphysics and a hundred years out of fashion — quite right on both counts. Then she will be unable to sleep, because it also specifies a procedure, and hers does not.”",
)
add(
    "“I have believed it for eighty years without being able to prove it,” said the Duc de Brévanne, “which I am told is called faith, though I maintain it is merely patience.” He put out a gloved hand. Lolly shook it. It was quite cold. “One last thing, since you asked me nothing and I shall tell you anyway.”",
    "“I have believed it for eighty years without being able to prove it,” said the Duc de Brévanne, “which I am told is called faith, though I maintain it is merely patience.” He put out a gloved hand. Lolly shook it. It was quite cold. “One last thing.”",
)
add(
    "“You said you were a physicist for eleven minutes, once.” He was already turning away. “I was a historian until twenty-two, and a physicist for sixty years afterward, and never once both. That is why I could not see what your bureaucracy was doing to those houses and you could.” He paused. “Ten years on things that must work, three days on paperwork that must be filed: you are the only person in that building who knows what an institution is as well as what a wave is. Do not stand on a wall about it.”",
    "“You said you were a physicist for eleven minutes, once.” He was already turning away. “I was a historian until twenty-two, and a physicist for sixty years afterward, and never once both. That is why I could not see what your bureaucracy was doing to those houses and you could.” He paused. “Ten years on things that must work, three days on paperwork: you are the only person in that building who knows what an institution is as well as what a wave is. Do not stand on a wall about it.”",
)
add(
    "Fainrose had a view, which she delivered to the syndrome table rather than to anyone in particular. “They have taken the one signature off the directive,” she said. “Now it has no author, and the only way it gets one again is for someone to stand up in that inquiry and say what it did — and whoever does that will be thanked for the disruption and not the truth. It is the cheapest move there is, and they will make it every time.”",
    "Fainrose had a view, which she delivered to the syndrome table rather than to anyone in particular. “They have taken the one signature off the directive,” she said. “Now it has no author, and the only way it gets one again is for someone to stand up in that inquiry and say what it did — thanked for the disruption and not the truth. The cheapest move there is, and they will make it every time.”",
)
add(
    "This was not modesty. She had checked. Fainrose needed silence and stabiliser algebra; Beatrix needed a lawyer; Gideon was in the requisition archive with fifteen years of ledgers, sending up each evening a signature, a date, a cupboard number. Jago had gone to Croydon on an errand unlikely to be relevant and almost certainly interesting. Mrs Chain had gone to Sub-District 6 to sit with another woman whose sister’s name had gone the same way, and had taken the umbrella.",
    "This was not modesty. She had checked. Fainrose needed silence and stabiliser algebra; Beatrix needed a lawyer; Gideon was in the requisition archive with fifteen years of ledgers. Jago had gone to Croydon on an errand unlikely to be relevant. Mrs Chain had gone to Sub-District 6 to sit with another woman whose sister’s name had gone the same way, and had taken the umbrella.",
)
add(
    "The woman in Sub-District 6 had a classification. Beatrix had found it that morning, deep in the operational schedules: P-9, pending status, for a citizen the survey had caught in the middle of something — a name half-said, a journey not yet agreed to, an intention still deciding itself — and then required to sign regardless. There was a box on the form for it. Beside the box, on file after file, a second field read no action required. The log stood at ninety-one that morning, and was climbing.",
    "The woman in Sub-District 6 had a classification. Beatrix had found it that morning: P-9, pending status, for a citizen the survey had caught in the middle of something — a name half-said, a journey not yet agreed to — and then required to sign regardless. Beside the box, on file after file, a second field read no action required. The log stood at ninety-one that morning, and was climbing.",
)
add(
    "“I was a physicist,” she said. “For about eleven minutes. Then electronics for ten years, then Transit Reconciliation. Three days ago I started noticing things in a notebook, and every one turns out to be a standard result with somebody’s name on it.” She did not much care how it sounded. “Fainrose is doing stabiliser codes upstairs. Keinschein has been alive since before agriculture. I write that the house is larger than the form and feel clever until somebody names it state reduction.”",
    "“I was a physicist,” she said. “For about eleven minutes. Then electronics for ten years, then Transit Reconciliation. Three days ago I started noticing things in a notebook, and every one turns out to be a standard result with somebody’s name on it.” She did not much care how it sounded. “Fainrose is doing stabiliser codes upstairs. Keinschein has been alive since before agriculture. I write that the house is larger than the form and feel clever until somebody names it.”",
)

# ---------------------------------------------------------------------------
# Chapter 13 — Tegmark first entrance ~25–30%; keep sister correction
# ---------------------------------------------------------------------------
add(
    "The second arrived talking. He was younger by decades, sandy-haired, in a jacket over a T-shirt, and he came in mid-sentence with a tablet in one hand and a coffee in the other and an air of enormous delight at being alive in a universe that had turned out to be so interesting. “-which is the thing nobody wants to say out loud, that if the equations are the ontology then this whole crisis is a bookkeeping dispute — sorry, hello, Max Tegmark, cosmology, I’ve read the Fainrose paper four times, Dr Fainrose it’s an honour, your syndrome table is gorgeous, I think it’s solving a problem that doesn’t exist but it’s gorgeous.”",
    "The second arrived talking. He was younger by decades, sandy-haired, in a jacket over a T-shirt, tablet in one hand and coffee in the other, with an air of enormous delight at being alive in so interesting a universe. “—which is the thing nobody wants to say out loud, that if the equations are the ontology then this whole crisis is a bookkeeping dispute — sorry, hello, Max Tegmark, cosmology, I’ve read the Fainrose paper, Dr Fainrose it’s an honour, your syndrome table is gorgeous.”",
)
add(
    "Tegmark had his hand half up like a schoolboy. “See, this is where I get off the bus,” he said. “Werner — may I — this is the thing. You say the question generates no numbers. But the equation generates numbers, and the equation has a mathematical structure, and my position, and I’ll be totally clear that it’s a minority position, is that the mathematical structure isn’t a description of reality, it is the reality. There’s nothing else. The universe is a mathematical object and we’re self-aware substructures inside it.”",
    "Tegmark had his hand half up like a schoolboy. “See, this is where I get off the bus,” he said. “Werner — may I — you say the question generates no numbers. But the equation generates numbers, and my position — a minority one — is that the mathematical structure isn’t a description of reality, it is the reality. The universe is a mathematical object and we’re self-aware substructures inside it.”",
)
add(
    "“Nothing was destroyed.” He said it gently, and Lolly understood he was neither stupid nor cruel, which was worse. “If the equation never stops, and there’s no collapse, the universe didn’t pick one answer and delete the rest. It branched. Photograph and clock — both real, both with a Mrs Chain.” He spread his hands, trying to offer comfort. “The alternatives weren’t extinguished. They were decohered from. Everything this Ministry allegedly destroyed still exists. It’s just not here.”",
    "“Nothing was destroyed.” He said it gently, and Lolly understood he was neither stupid nor cruel, which was worse. “If the equation never stops, and there’s no collapse, the universe didn’t pick one answer and delete the rest. It branched. Photograph and clock — both real, both with a Mrs Chain.” He spread his hands. “The alternatives weren’t extinguished. They were decohered from. Everything this Ministry allegedly destroyed still exists. It’s just not here.”",
)
add(
    "They came in at ten past. The first was tall, hollow-cheeked, immaculately grey, with the posture of a man who had spent decades being the cleverest person in rooms that were themselves dangerous. He carried nothing at all — no papers, no case — and sat down at the far end with his hands folded, and Lolly noticed that he chose the seat furthest from the window.",
    "They came in at ten past. The first was tall, hollow-cheeked, immaculately grey, with the posture of a man who had spent decades being the cleverest person in dangerous rooms. He carried nothing — no papers, no case — and sat at the far end with his hands folded, choosing the seat furthest from the window.",
)
add(
    "The third came in last and quietly, and the room’s temperature dropped about it. He was a smallish man with a red beard going white, in a jumper, with the specific bright unblinking gaze of somebody who has spent thirty years being polite to people he considers to have been sloppy. He had a Belfast voice, unhurried and precise, and he sat down without shaking hands with anyone.",
    "The third came in last and quietly, and the room’s temperature dropped about it. He was a smallish man with a red beard going white, in a jumper, with the bright unblinking gaze of somebody who has spent thirty years being polite to people he considers sloppy. He had a Belfast voice, unhurried and precise, and he sat down without shaking hands.",
)
add(
    "Everyone looked at him. Bellew had not moved. He sat with his forearms on the table and his bright pale eyes going from Heitmann to Tegmark and back. “Werner says the question has no meaning. Max says the question has too many answers, all of them real. And between the pair of you there’s not one single thing a Board of Inquiry could go and check.” He tapped the table once, softly. “You’ve both got theories in which nobody can ever be wrong. I’ve spent my career objecting to that, and I’ll object to it in a car park in a suspended county if the room-booking requires it.”",
    "Everyone looked at him. Bellew had not moved. He sat with his forearms on the table, pale eyes going from Heitmann to Tegmark and back. “Werner says the question has no meaning. Max says it has too many answers, all of them real. Between the pair of you there’s not one thing a Board of Inquiry could go and check.” He tapped the table once. “You’ve both got theories in which nobody can ever be wrong. I’ve spent my career objecting to that, and I’ll object to it in a car park in a suspended county if required.”",
)

# ---------------------------------------------------------------------------
# Chapter 14 — cut catch fat after refusal; reach holography sooner
# ---------------------------------------------------------------------------
add(
    "“There are three, and I shall not hide them.” Von Wittenberg counted them off on his fingers, mildly. “First: the strings are so small that no accelerator we could build on this planet or in this solar system could see one directly, and so there has never been a direct experimental test of it. Not one. Dr Fainrose is entirely right to say so and she says it to me every time we meet.”",
    "“There are three, and I shall not hide them.” Von Wittenberg counted them off on his fingers. “First: the strings are so small that no accelerator we could build could see one directly. There has never been a direct experimental test. Dr Fainrose is entirely right to say so.”",
)
add(
    "“The mathematics does not work in four dimensions. It requires ten.” He said this the way another man might mention that a recipe requires buttermilk. “Nine of space, one of time. And since we plainly experience three of space, the other six must be curled up small — at every point in what you think of as empty room there are six additional directions, wound so tightly that nothing you or I can do will ever push anything along them.”",
    "“The mathematics does not work in four dimensions. It requires ten.” He said this the way another man might mention that a recipe requires buttermilk. “Nine of space, one of time. Since we experience three of space, the other six must be curled up small — at every point, six additional directions, wound so tightly that nothing you or I can do will push anything along them.”",
)
add(
    "Somewhere outside, a car alarm went off, was silenced, and was not explained. Lolly glanced at her watch without meaning to — a new habit, three days old, that she had already stopped being able to switch off — and found that two hours had gone since she had sat down, with 4C still losing mass somewhere behind all of this.",
    "Somewhere outside, a car alarm went off and was silenced. Lolly glanced at her watch — a new habit, three days old — and found that two hours had gone, with 4C still losing mass somewhere behind all of this.",
)
add(
    "“It is, yes.” Von Wittenberg looked pleased. “And the third catch is the one that mattered most, and it is the reason I am in a library in Sub-District 6 rather than at home. For a long time there were five different string theories. All consistent. All beautiful. All slightly different. Which was, you understand, an embarrassment — one had set out to explain why there is only one world and had produced five candidates and a great deal of silence.”",
    "“It is, yes.” Von Wittenberg looked pleased. “And the third catch is why I am in a library in Sub-District 6 rather than at home. For a long time there were five different string theories — all consistent, all beautiful, all slightly different. An embarrassment: one had set out to explain why there is only one world and had produced five candidates.”",
)
add(
    "Lolly closed the notebook. “Professor von Wittenberg,” she said. “I will write down anything that tells me what they dumped into 4C. I will not take dictation on eleven dimensions until then. I have to say this. In three days I have been told by an extremely old vampire that nothing is definite until agreement spreads. I have been told by a French duke that everything is definite and steered by a wave over all the alternatives. I have been told by a Swede that every alternative actually happens somewhere. I have been told by a dead man from Belfast to stop picking and go and measure something. And you have now told me that everything is made of eleven-dimensional membranes that nobody can see and no experiment can reach.” She looked at the little loop on the page. “I have a woman in this district who was stopped in the middle of remembering her sister’s name. What am I supposed to do with strings?”",
    "Lolly closed the notebook. “Professor von Wittenberg,” she said. “I will write down anything that tells me what they dumped into 4C. I will not take dictation on eleven dimensions until then. In three days I have been told that nothing is definite until agreement spreads; that everything is definite and steered by a wave; that every alternative happens somewhere; that I should stop picking and go and measure something. And you have now told me everything is made of eleven-dimensional membranes nobody can see.” She looked at the little loop on the page. “I have a woman in this district who was stopped in the middle of remembering her sister’s name. What am I supposed to do with strings?”",
)
add(
    "Von Wittenberg did not take offence. He seemed, if anything, to have been waiting for it. “That is the right question and I shall answer it in the correct order,” he said. “First: nothing. You are supposed to do nothing with strings. The Bell measurement is what matters this week and I would not have you divert a single cable from it. Anyone who tells you that eleven dimensions will help you get an injunction is lying to you.”",
    "Von Wittenberg did not take offence. “That is the right question,” he said. “First: nothing. You are supposed to do nothing with strings. The Bell measurement is what matters this week. Anyone who tells you eleven dimensions will help you get an injunction is lying to you.”",
)
add(
    "“Second: I did not come here to tell you what everything is made of. Dr Bellew would rightly say that I cannot demonstrate it, and I cannot.” He shifted the three sheets of paper he had brought and turned one round. “I came because of your black hole.”",
    "“Second: I did not come here to tell you what everything is made of. I cannot demonstrate it.” He turned one sheet round. “I came because of your black hole.”",
)
add(
    "“Alfred telephoned me on Tuesday and shouted at me for eleven minutes, which at his age is a considerable investment and, I think, a form of affection.” Von Wittenberg’s mouth twitched. “His concern, as I understand it, is that your Ministry has used a small engineered black hole as a disposal channel for suppressed alternatives, and that the object is now evaporating, and that when it has gone there will be no record of what was destroyed. He calls this the falsification of the ledger. He is frightened. I have known him ninety years and I have not heard him frightened before.”",
    "“Alfred telephoned me on Tuesday and shouted at me for eleven minutes, which at his age is a form of affection.” Von Wittenberg’s mouth twitched. “His concern is that your Ministry has used a small engineered black hole as a disposal channel for suppressed alternatives, that the object is evaporating, and that when it has gone there will be no record of what was destroyed. He calls this the falsification of the ledger. I have known him ninety years and I have not heard him frightened before.”",
)
add(
    "“Ah,” said von Wittenberg, and for the first time something in his face brightened. “That is the part that persuaded me. You must understand — for fifty years the great scandal of physics was that our theory of the very small and our theory of gravity would not sit in the same room. Put them together and the answers came out infinite. Not large. Infinite, which is nature’s way of saying that the question was malformed. Every attempt failed.”",
    "“Ah,” said von Wittenberg, and for the first time something in his face brightened. “That is the part that persuaded me. For fifty years the scandal was that our theory of the very small and our theory of gravity would not sit in the same room. Put them together and the answers came out infinite — nature’s way of saying the question was malformed. Every attempt failed.”",
)
add(
    "He drew, very small, a dot. “A point particle,” he said. “It has no size and no internal structure and no way of being anything other than what it is. If you wish to explain why there are so many different particles, you must simply list them, and we have listed them, and the list is seventeen items long and nobody knows why it is that list rather than another.”",
    "He drew, very small, a dot. “A point particle,” he said. “It has no size and no internal structure. If you wish to explain why there are so many different particles, you must simply list them — seventeen items, and nobody knows why that list rather than another.”",
)
add(
    "They went into Sub-District 6 on the Thursday with two vans, a portable timing rack, four hired photodetectors, and paperwork Beatrix had signed in a hand that dared anyone to query it. Fainrose was in the primary school hall running cable. Jago had gone for a fifth detector on terms nobody had asked about. Lolly, sent out for exceeding her quota of useful questions, ended up in the Coldharrow Street library with the green notebook and eleven photocopied pages from box seven.",
    "They went into Sub-District 6 on the Thursday with two vans, a portable timing rack, four hired photodetectors, and paperwork Beatrix had signed in a hand that dared anyone to query it. Fainrose was in the primary school hall running cable. Jago had gone for a fifth detector. Lolly, sent out for exceeding her quota of useful questions, ended up in the Coldharrow Street library with the green notebook and eleven photocopied pages from box seven.",
)

# ---------------------------------------------------------------------------
# Chapter 18 — cut heat-death catalogue ~100–150w; keep scarce accounts / no lid
# ---------------------------------------------------------------------------
add(
    "“The stars are the first thing to understand. There are stars now. This is not the normal condition. Star formation peaked long ago and is declining, and the gas will run down, and in something of the order of a hundred trillion years the last star will form and the sky will begin to go out — not dramatically, one by one, the small red ones outliving all the rest with the patience of the parsimonious. And then there will be a very long time in which the galaxy is a place of embers: white dwarfs cooling, neutron stars cooling, brown dwarfs occasionally colliding and briefly lighting. That era is longer, Ms Wren, than the era of starlight by a factor you cannot usefully imagine. Almost all of history is afterwards. Then, if the protons are not eternal — and we do not know, we have looked very hard and seen nothing, which only pushes the number out — then even the embers dissolve, and matter itself is a phase that ends.",
    "“The stars are the first thing to understand. There are stars now. This is not the normal condition. Star formation peaked long ago; the gas will run down; in something of the order of a hundred trillion years the last star will form and the sky will begin to go out, one by one. And then a very long time of embers: white dwarfs cooling, neutron stars cooling. That era is longer, Ms Wren, than the era of starlight by a factor you cannot usefully imagine. Almost all of history is afterwards. Then, if the protons are not eternal — and we do not know — even the embers dissolve, and matter itself is a phase that ends.",
)
add(
    "“And then it is the age of the black holes, and they are the last structures, and they do exactly what your 4C did in a car park in Surrey: they evaporate. Slowly. Then less slowly. Then, at the very end, in a final bright indignity. The largest will take on the order of 10 to the power of 100 years, which is not a length of time so much as an insult to the concept. But they go. Everything that ever consolidated, goes. After that: a very thin, very cold, very dark space with a little radiation in it, expanding, and nothing in it that could be called an event.",
    "“And then it is the age of the black holes, and they are the last structures, and they do exactly what your 4C did in a car park in Surrey: they evaporate. Slowly, then less slowly, then in a final bright indignity. The largest will take on the order of 10 to the power of 100 years. But they go. After that: a very thin, very cold, very dark space, expanding, and nothing in it that could be called an event.",
)
add(
    "“Now,” said Erich Schrottfinger. “The interesting part, which is why I did not simply post it to you. Every physicist my age was taught that the universe runs down. Order becomes disorder; the coffee goes cold; the sun exhausts itself. Perfectly true. And when I was a younger man I looked at a living thing and thought: how does that happen. Because a living thing does the opposite. It maintains itself. It holds a pattern against the current for eighty years.",
    "“Now,” said Erich Schrottfinger. “The interesting part. Every physicist my age was taught that the universe runs down. Order becomes disorder; the coffee goes cold; the sun exhausts itself. Perfectly true. And when I was younger I looked at a living thing and thought: how does that happen. Because a living thing does the opposite — holds a pattern against the current for eighty years.",
)
add(
    "“And the answer is not that life defies the law. The answer is that a living thing survives by feeding on order — by taking in structure and excreting disorder, by paying the universe’s bill locally and passing the cost outward. It does not violate the accounts. It runs a very good scheme within them. A living thing is a place where order is temporarily concentrated because it has arranged to be paid for elsewhere. You see it, of course. You have spent a year on it.",
    "“And the answer is not that life defies the law. The answer is that a living thing survives by feeding on order — taking in structure, excreting disorder, paying the bill locally and passing the cost outward. It does not violate the accounts. It runs a very good scheme within them. A living thing is a place where order is temporarily concentrated because it has arranged to be paid for elsewhere. You have spent a year on it.",
)
add(
    "“Your Ministry, Ms Wren, was doing the same thing, badly, and without knowing it. It wished a district to be simple — that is, low in complexity, low in ambiguity, cheap to describe. And it discovered what every living system discovers, which is that you cannot simply have that. You must pay for it, and the payment is that the disorder goes somewhere else. So they built a hole and put it in there. That was not a bureaucratic peculiarity. That was thermodynamics, conducted by people who had not been told they were doing thermodynamics, and the reason it ended in a fire is that they never asked where the bill was going. Every institution that promises to make things simple is proposing to move complexity somewhere you cannot see. Every single one. Not sometimes. Always, and by law. That is the sentence I should like you to take away, and you may put it in your notebook. You need not attribute it to me. It is the second law with the politics put back in — Boltzmann did the arithmetic and had the sense to stop there.”",
    "“Your Ministry, Ms Wren, was doing the same thing, badly, and without knowing it. It wished a district to be simple — low in complexity, cheap to describe. And it discovered what every living system discovers: you cannot simply have that. You must pay for it, and the payment is that the disorder goes somewhere else. So they built a hole and put it in there. That was thermodynamics, conducted by people who had not been told they were doing thermodynamics, and it ended in a fire because they never asked where the bill was going. Every institution that promises to make things simple is proposing to move complexity somewhere you cannot see. Always, and by law. That is the sentence I should like you to take away. It is the second law with the politics put back in.”",
)
add(
    "“And so — the outlook,” said Schrottfinger. “Yes. In the long run: the embers, the holes, the dark. I shall not soften it and I dislike people who do. But consider what is between now and that. Consider the enormous middle. There is going to be an extremely long period in which there is still order left to be spent, and in which anything that can arrange to be paid for elsewhere may persist, and think, and ask questions. Life did not have to happen. Having happened, it has a very long time to work with, and the sort of thing it may become in a hundred million years does not bear guessing at and would probably not recognise us as ancestors so much as weather.",
    "“And so — the outlook,” said Schrottfinger. “Yes. In the long run: the embers, the holes, the dark. I shall not soften it. But consider the enormous middle: a very long period with order still left to be spent, in which anything that can arrange to be paid for elsewhere may persist, and think, and ask questions. Life did not have to happen. Having happened, it has a very long time to work with.",
)
add(
    "“Here is the outlook, since you want the outlook. Your Ministry believed it was managing a country. It was in fact interfering, in a small and provincial way, with something that is not finished. And I do not mean the paperwork is not finished. I mean the universe is not finished, and it is not nearly finished, and everything you have lived through this year took place in what future arrangements of matter will regard as the opening seconds.",
    "“Here is the outlook, since you want the outlook. Your Ministry believed it was managing a country. It was in fact interfering, in a small and provincial way, with something that is not finished. I do not mean the paperwork. I mean the universe is not finished, and everything you have lived through this year took place in what future arrangements of matter will regard as the opening seconds.",
)
add(
    "Schrottfinger pushed it aside. “Now. You have written four hundred pages and you have finished a thing, and you have come to a library on a Friday because you want somebody to tell you what it was all for, and Fainrose cannot tell you because she is a working physicist and von Wittenberg cannot tell you because he will start on the eleven dimensions. So it falls to me, who am not respectable.”",
    "Schrottfinger pushed it aside. “Now. You have finished a thing, and you have come to a library on a Friday because you want somebody to tell you what it was all for, and Fainrose cannot tell you because she is a working physicist and von Wittenberg cannot tell you because he will start on the eleven dimensions. So it falls to me, who am not respectable.”",
)


def words(s: str) -> int:
    return len(s.split())


def set_paragraph_text(paragraph, text: str) -> None:
    """Clear all w:t, then put full text in the first run (preserve formatting)."""
    t_elems = paragraph._p.findall(".//" + qn("w:t"))
    for t in t_elems:
        t.text = ""
    if paragraph.runs:
        paragraph.runs[0].text = text
        # ensure the first run's w:t exists
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


def chapter_of(idx: int) -> int | None:
    bounds = [
        (1, 109, 260),
        (2, 260, 459),
        (3, 459, 658),
        (4, 658, 816),
        (5, 816, 954),
        (6, 954, 1082),
        (7, 1082, 1221),
        (8, 1221, 1312),
        (9, 1312, 1445),
        (10, 1445, 1502),
        (11, 1502, 1599),
        (12, 1599, 1695),
        (13, 1695, 1799),
        (14, 1799, 1897),
        (15, 1897, 1969),
        (16, 1969, 1992),
        (17, 1992, 2012),
        (18, 2012, 2089),
    ]
    for ch, a, b in bounds:
        if a <= idx < b:
            return ch
    return None


def novel_word_count(doc: Document) -> int:
    return sum(len(p.text.split()) for p in doc.paragraphs[109:2089])


def main() -> None:
    doc = Document(str(SRC))
    before = novel_word_count(doc)

    # Build lookup of exact paragraph texts present
    text_to_indices: dict[str, list[int]] = {}
    for i, p in enumerate(doc.paragraphs):
        t = p.text
        if t:
            text_to_indices.setdefault(t, []).append(i)

    missing = []
    applied = []
    chapters_touched: set[int] = set()

    for old, new in REPLACEMENTS.items():
        idxs = text_to_indices.get(old)
        if not idxs:
            # try normalize curly quotes / nbsp variants
            missing.append(old[:100])
            continue
        for idx in idxs:
            set_paragraph_text(doc.paragraphs[idx], new)
            ch = chapter_of(idx)
            if ch:
                chapters_touched.add(ch)
            applied.append(
                {
                    "idx": idx,
                    "ch": ch,
                    "old_w": words(old),
                    "new_w": words(new),
                    "cut": words(old) - words(new),
                    "old100": old[:100],
                    "new100": new[:100],
                }
            )

    after = novel_word_count(doc)
    doc.save(str(SRC))

    # Sync KINDLE + Photo_Edition
    kindle = ROOT / "Schrodingers_Paperwork_BOOK_1_KINDLE.docx"
    photo = ROOT / "Schrodingers_Paperwork_BOOK_1_Photo_Edition.docx"
    shutil.copy2(SRC, kindle)
    shutil.copy2(SRC, photo)

    # Continuity lock smoke checks on novel body
    body = "\n".join(p.text for p in Document(str(SRC)).paragraphs[109:2089])
    locks = {
        "impersonation of my address": "impersonation of my address" in body,
        "lie required electricity": "lie required electricity" in body,
        "There is no lid": "There is no lid" in body or "there is no lid" in body.lower(),
        "no view from nowhere": "no view from nowhere" in body.lower(),
        "That is not mine": "That is not mine" in body,
        "Where exactly,” said Stephanie Fainrose, “did you get the idea that you were the assistant": (
            "did you get the idea that you were the assistant" in body
        ),
        "accounts scarce / efficiency": "accounts are the scarce" in body or "accounts, and calling it efficiency" in body,
        "Mrs Chain sister correction": "Then do not tell me nothing was destroyed" in body,
        "cast no shadow": "cast no shadow" in body.lower() or "He cast no shadow" in body,
    }

    # Best 5 cuts by words removed
    best = sorted(applied, key=lambda x: -x["cut"])[:5]

    lines = []
    lines.append("Schrödinger's Paperwork — tighten pass")
    lines.append(f"Source: {SRC.name}")
    lines.append(f"Backup: Schrodingers_Paperwork_BOOK_1_BEFORE_TIGHTEN.docx")
    lines.append(f"Novel words before: {before}")
    lines.append(f"Novel words after:  {after}")
    lines.append(f"Words removed:      {before - after}")
    lines.append(f"Paragraphs updated: {len(applied)}")
    lines.append(f"Missing matches:    {len(missing)}")
    lines.append(f"Chapters touched:   {sorted(chapters_touched)}")
    lines.append(f"Synced: KINDLE + Photo_Edition (copied from BOOK_1)")
    lines.append("")
    lines.append("Continuity locks present:")
    for k, ok in locks.items():
        lines.append(f"  [{'OK' if ok else 'MISSING'}] {k}")
    lines.append("")
    lines.append("Sample of 5 best cuts (old→new, first 100 chars):")
    for i, c in enumerate(best, 1):
        lines.append(f"{i}. Ch{c['ch']} −{c['cut']}w")
        lines.append(f"   OLD: {c['old100']}")
        lines.append(f"   NEW: {c['new100']}")
    if missing:
        lines.append("")
        lines.append("UNMATCHED (first 100 chars each):")
        for m in missing:
            lines.append(f"  - {m}")

    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
