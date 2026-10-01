# -*- coding: utf-8 -*-
"""29 Sep 2026 lengthening pass. Insert one new movement per chapter. Idempotent."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def insert_before(fname, anchor, block):
    path = os.path.join(ROOT, fname)
    raw = open(path, encoding="utf-8").read()
    key = block.strip().splitlines()[0][:70]
    if key in raw:
        print("skip", fname, key[:40])
        return
    i = raw.find(anchor)
    if i < 0:
        raise SystemExit("missing anchor in %s: %s" % (fname, anchor[:60]))
    line_start = raw.rfind("\n", 0, i) + 1
    nl = "\r\n" if "\r\n" in raw else "\n"
    piece = block.strip("\n").replace("\n", nl)
    raw = raw[:line_start] + piece + nl + nl + raw[line_start:]
    open(path, "w", encoding="utf-8", newline="").write(raw)
    print("ok", fname, anchor[:36])

P1 = r"""A joint is a surface with almost no staff and almost no road.

Cartilage is the slick on the end of the bone. It has almost no blood of its own. The few cells in it eat what seeps in from the neighboring tissue, a slow pantry, not a hose. That is why a hopeful capsule in the bloodstream is a rude delivery problem. The road to the surface is a seep. A drug that quiets inflammation in the lining, or a lubricant a surgeon can place where the seep cannot carry it, can still be a local win. A label that says the seep will grow the hands back to twenty is the fountain, early, wearing a blister pack.

The hands are not a rare story. Osteoarthritis — the wearing and the inflammation of a joint, not the kind of arthritis that sets a whole immune system on fire — is one of the common ways a morning gets smaller. A global ledger for 2020 counted nearly six hundred million people living with it, nearly eight in a hundred people alive that year. Not all of them in the hands. Not all of them unable to work. Knees, hips, a spine, a thumb. The airlock does not care which joint the ledger used. It cares whether the glove can close.

where six hundred million is a count of people, not a count of cures.

She times the jar. Yesterday the lid took one swear. Today it takes two, and a cloth. She writes the number in the margin of the pH log, because a mood is not a measurement and the margin has room. The capsule is for this surface, this season. It will not hire cartilage a blood supply the tissue never had. If the lid takes one swear again next month, the dose earned its keep. If it takes three, the label was optimistic and the log will say so.

Rohan asked for the number, not the story. He is the life-support lead on the orbiter. He is not in the greenhouse. He will not be. His note left before her jar did, and it will meet her answer late, the way every note meets her. He has the procedure for the pump and, now, a column labeled *lid*. A column is not a new body. It is how you notice a clock without letting it make a speech."""

P2 = r"""Put the two pots in a year a ledger will still recognize.

Around 2019, before a pandemic knocked the chalk off the board, the world’s life expectancy at birth sat in the low seventies. Healthy life expectancy sat about a decade lower. The decade is the hatch on the figure: years the wall clock counted and a vote would have argued with. Rich kitchens show a higher pair of numbers and a smaller hatch. They do not show a hatch of zero. A country can be proud of the first number and still be billing people for the second.

The United States is the warning already named, with a recent scar on it. Life expectancy there fell into the mid-seventies in the worst pandemic year and climbed back toward the high seventies afterward. The fall was not a new fuse in the species. It was a virus, and under the virus the older invoices: opioids, metabolic disease, violence, a bill that is also a maze. Institutions moved a national average in both directions inside five years. Biology did not issue a new body either time. That is hot as a lesson about kitchens, and cold as a prophecy about the next virus. The next virus will have its own meeting.

Jeanne Calment’s tail has been accused, which is what a tail is for.

A paper argued that the woman who died at 122 was not Jeanne but her daughter, living on under the mother’s name. The demographers who had walked the archives answered with the records: a census, a marriage, a life that does not collapse into the swap if you actually open the files. Take the episode as a method, not as gossip. Extraordinary ages need extraordinary paperwork. On the best public answers, the paperwork held. The number is still a tail. A defended tail is not a product. Nobody left that argument with a protocol that prints 122, and nobody left it with a protocol that prints 150.

Compression of morbidity is the hope that the hatch stays short and sits against the end. A physician named it, as a hope, in 1980. The decades since did not promote the hope into a law. Some diseases were shoved toward the last years. Others stretched, because a kitchen got better at keeping a pulse in a room that had already narrowed. Both can be true in one country in one decade. Ask which pot moved. Then ask who was in the room when it moved."""

P3 = r"""One broken clock is a disease. It is not a diagram of the whole kitchen.

There are children who age, in some tissues, far too fast. In one of those diseases a single wrong splice in the gene for lamin A — a structural protein of the cell’s nucleus — makes the cell build a poisonous stub of the protein. Skin, vessels, and a child’s face take on a look people call old. Many of those children die of disease in the arteries and the heart, often in their teens. They do not arrive with every hallmark checked off. They do not, as a rule, get the brain’s long goodbye at twelve. Another disease, in adults, breaks a helicase, a protein that helps unwind DNA so the cell can copy it and repair it. Those adults get cancers, a look of age, and a short life. They still do not demonstrate that an ordinary seventy-year-old failed at that one enzyme and at nothing else.

where a progeria is a named disease of one mechanism, and ordinary aging is the house with the other clocks still running.

The fountain slide loves these children and these adults, because one gene looks like one fuse. Look first. A rare poison in the nucleus is a tragedy and a research door. It is not evidence that a neighbor’s stiff hands, crowded immune library, and lost names are the same door with a different paint. Repair the splice, if a clinic ever can, and you have done a local, extraordinary thing for a rare disease. You have not been handed the knob for the species. The cousin drawer said this from the other side. A mole rat’s hazard curve is not a prescription. A child’s lamin is not a prescription either. Both are clocks you can point at. Pointing is not a rewind.

She can hold both ideas in one morning, which is the test. The capsule is for a joint. The joint is not lamin, and it is not a shark, and it is not a fuse. Rohan’s column will record the swear-count. It will not record a species. The basil, which has no nucleus arranged like hers, will die of a pH long before it dies of a philosophy. That is allowed. Plants are a different invoice. The refusal to launder them into a human fountain is the same refusal as the refusal to launder the mole rat."""

P4 = r"""The wilderness had a body count. The clinic has a fraction. Both belong on the receipt.

In 1999 a young man died in a trial that was trying to deliver a missing metabolic instruction with an early viral truck. The truck set off an immune storm. The letter never got its hour. A few years later, children born without a working immune system were given a different truck. Some of them were freed from the immunodeficiency and then developed a leukemia, because the truck had parked its cargo in the genome near a gene that tells cells to multiply. The field did not get to call that a footnote. It changed the truck. Those deaths and those leukemias are why delivery is not a cheerful sentence under the word *scissors*. The truck is the procedure. The immune system is a bouncer with a long memory. A second dose of a truck the bouncer already remembers can be a different disease from the one you came to treat.

The sickle-cell-class win is what the paperwork looks like when it has finally become mean enough.

In the pivotal set for the edit that wakes fetal hemoglobin, nearly all of the patients with enough months on the clock — on the order of twenty-nine out of thirty — went at least a year without a severe crisis, the kind that jams a vessel and wrecks a week or a life. Hot as a result in a small, watched group. Not a neighborhood. The conditioning still empties a marrow. The list price still sits in the low millions per person. Cousin therapies for other rare failures of blood, muscle, or liver have sat in that band or above it. Name the band, not the halo. A local fix a ministry can buy for a few people, after a hospital month that can kill, with a result you can count in crises that did not happen.

She will not be in that set. Her hands are not a single letter in hemoglobin. Her sister, on the coast, is not in that set either. The sister can say *phase* and *exclusion* without a pamphlet, and the pamphlet would not have her in it anyway. The radio can carry the number twenty-nine out of thirty. It cannot carry a marrow across a delay and make the marrow cheap. Who sits outside the set is Chapter 13. Here the number is only the proof that local is allowed to be real and is still not a species."""

P5 = r"""The brain’s long goodbye has a number now. The number is small on purpose.

A drug that clears one amyloid — one of the clumping waste proteins in one of the dementias — was tested against a placebo for a year and a half. The score that moved is an eighteen-point scale of how a person is managing. The difference at the end was less than half a point. In the trial’s own relative framing, the drug group declined about a quarter less than the placebo group. The entry fee has a short name, ARIA: swelling and small bleeds in the brain. It showed up in a little more than one person in eight on the drug, and almost never on the placebo. A cousin drug, aimed at the same waste, moved its own scores by a similar modest slice. About one person in four on that cousin paid the swelling-and-bleeding fee.

where half a point is on a scale that runs to eighteen, over eighteen months, not the return of a Tuesday that had already been lost.

That is a local, expensive, argued result. Warm-to-hot as a class of measurement. Cold as a resurrection. A family can decide the half point is worth the fee. A slide cannot honestly draw the half point as a new skull. The names still leave. In some people they leave more slowly, for a while, at a price and a risk the receipt has to show in the same size type as the hope.

The eviction drugs have a failed receipt of their own. A senolytic — a drug meant to clear cells that refuse to die and then spoil the tissue around them — was put into osteoarthritic knees in a human trial around 2020. The pain did not move enough to justify the story the mouse graphs had told. The sponsor does not get a name in this kitchen. The temperature does. Pretty in a dish and a rodent. Cold as a knee you can put on a calendar and sell.

Two older drugs get recruited into the same costume, and they have not earned it. Metformin is already licensed for diabetes. Rapamycin is a transplant drug that shouts at a nutrient-sensing clock. One has a proposed trial that would ask whether it delays a bundle of age-related diseases in people who do not have diabetes. As of late summer 2026 that trial was still a story about funding and startup, not a result you can mark on the two bars. The other is being given, in a serious veterinary trial, to pet dogs, because a dog’s life is short enough for a grant to watch and a person should not be the first casual experiment. A trial in a dog is a trial. It is not your morning. If either drug ever moves a human healthspan by a slice you would vote for, the slice will arrive as a receipt: a number, a harm, a zip code. It will not arrive as a fuse."""

P6 = r"""Count the staff. The cupboard story does not survive a census.

A human brain has on the order of eighty-six billion neurons, the cells that carry the signals. About four in five of them sit in the cerebellum, the hind loaf that times the body. They were not a spare tank of philosophy. Damage them and the philosophy cannot keep its feet, its reach, or a beat. The cortex — the sheet the ten-percent story is vaguely pointing at when it says *the brain* — is the minority of the neurons and is still an enormous, expensive organ. The glia, which are not the celebrities of a wiring diagram, are a comparable crowd. They feed, insulate, and tidy. A census that ignores them, and then ignores the cerebellum, can invent a dark warehouse. A census that counts both cannot.

where eighty-six billion is a count of nerve cells, not a count of unused rooms.

The energy bill is about twenty watts in a body at rest. A dim light bulb, running the organ that is two percent of your mass. A bulb that was ninety percent idle at that wattage would be the first thing a miser mesh fired, and it would also be a heater you could feel. You notice this heater when the sugar drops and the bulb flickers: the faint, the irritability, the sentence that will not finish. Those are not the symptoms of a warehouse coming online. They are the symptoms of a furnace that was already the job.

Sometimes the false sentence arrives wearing a dead physicist’s name, as if the man had measured the ten percent and signed the floor plan. He did not. The attribution is a costume on a costume. William James wrote that we live below our limits. That was a sentence about effort and attention, more than a century ago, and it had no volume and no percentage. Effort is real. You can pay more attention than you paid this morning. Paying attention is overtime on a staff that was already hired. It is not a door into eighty-six billion cells that had been waiting in the dark with the meter running."""

P7 = r"""Hearing is the tool people skip. A commission finally priced the skip, and a trial then made the price honest.

A standing review of dementia risk, updated in the middle of this decade, set a long list of changeable risks next to the diseases of the long goodbye. In their model, nearly half of cases traced in part to that list. Less schooling. Hearing loss. High blood pressure. Smoking. Depression. A blow to the head. Dirty air. A life with too few people in it. Diabetes. Extra weight. And more, as the list grew from one edition to the next. Hearing loss was one of the larger slices. Not because the ear is the dementia. Because a social primate who cannot hear the room starts to leave the room, and the organ that was using the room loses the practice.

Then a trial did the ruder thing. It offered some people a real hearing intervention and some people a health-education program, and it watched cognition for three years. In the whole crowd, the hearing program did not beat the education program on the trial’s own primary test. In the subgroup already carrying more years and more risks, it did. That is a tool, caught in the act of not being helium. It is not a cure. It is a channel. It helps some kitchens more than others. Average a mild loss together with a life that was already narrowing, and the benefit can vanish into the design of the test. Take the aid anyway if the room has started to smear. The trial did not find a spare tank behind the ear. It found a door you can still open, with a result small enough that a slide would be ashamed to lead with it. Shame, in that direction, is a sign the result might be honest.

Education remains the slower and larger tool. The same commission’s spirit begins with whether a child was in the room at all. A headset sold to a parent as a substitute for that room is the carrot aimed at a construction site. The room is the technology. Its invoice is in years, in teachers, and in a state that decided who got a chair. No capsule on Mara’s radio replaces a childhood she has already finished. The checklist in her pocket is the adult, smaller version: a tool that holds a step the organ would otherwise have to hold alone, at twenty watts, while also holding the basil."""

P8 = r"""The loop has a laboratory version of the moment the cue outruns the stamp.

Wanting can be driven up while liking stays put. An animal will work for a stimulation in a circuit that pushes the seek, and the work will not look like pleasure if you score the face and the taste test the field actually uses, rather than the romantic story about a pleasure center. A person will chase a notification that has not made them glad in months. The chase updated. The stamp did not. The careful split — wanting is not liking — is the fake egg with the feathers counted. The egg is larger. The bird sits it. The sitting is not proof of gladness. The sitting is proof the cue hired the body.

A slot machine is the same hire with a pay table a kitchen can see.

The reward arrives on purpose without a rhythm you can finish: a variable ratio, wins rare enough and irregular enough that the seek never gets to conclude that the night is over. Hot as a design. The design is older than the cabinet. A bush that sometimes has berries trains the same staff. The cabinet removed the walk, the season, and the full stomach, and kept the sometimes. A longer life hands the cabinet more nights. It does not install the conclusion. The tools against it, if you want tools and not a sermon, are rude and small. Leave the room. Put a person who is not the cabinet in the next room. Sleep, so the night actually ends. None of those is an off-switch in the wiring. They are ways of starving a cue that will not starve itself.

Rohan’s joke arrives after the jar is already open.

She had written the swear-count in the margin. He had not heard it. His message was composed against an older morning. It congratulates her for a lid she has already finished and asks a question she answered yesterday. She laughs once, late, at a joke that is now about a different stiffness. The delay is not a symbol of their affection. The delay is the speed of light and the week’s geometry, four minutes or twenty. Wanting would like the joke to land in the minute it was made. Liking, if it comes, comes in the minute it is received. A long life on a short radio is more of these missed landings, not fewer. The helium slide says the extra years will make the landings wise. The radio says the landings stay late, and the loop keeps reaching for a cue that has already moved on."""

P9 = r"""One stair ended while the posters were still being printed.

Most of the antibiotic classes still sitting in a pharmacy were found before the early nineteen-sixties. The decades after were not a blank. They were a wall with a few new doors in it: adjustments of old scaffolds, a short list of genuinely new classes, and a soil that had been easy to mine and then was not. Resistance rose in the same years, because a drunk middle of prescriptions is how a kitchen trains the bacteria that remain. A child in 1975 and a child in 2025 do not share an infection room. They also do not share a room that discovered a new miracle class every five years on a schedule. The stair was real. The ruler laid on the stair — next decade, the bacteria politely gone — is the cropped curve the next chapter will refuse by name.

The genome stair has dollars on it, so the word *cheaper* cannot hide the shape.

This chapter already said the first human draft was on the order of a billion dollars and a decade. The cost of a later read, on the chart the field itself publishes, then fell through a hundred million, through a million, through ten thousand, and into the neighborhood of a thousand dollars, and in some kitchens below that. Hot as a drop. The drop is why a coastal bench can exist without a national cathedral. It is also why that bench can be full of letters nobody is yet allowed to act on. Cheaper reading was the steep middle. Meaning is the shoulder after it. Multiply the dollar drop by two hundred and you do not get a staff that understands two hundred times more. You get a cheaper pile, and a meeting about what the pile means, and a zip code that still cannot afford the meeting.

Polio is the stair and the wall in one disease, and it is not finished.

The vaccines are hot. Two of the three wild types are certified gone. The third was still living in Afghanistan and Pakistan in the middle of this decade, and people hired to carry the vaccine have been attacked and killed for carrying it. That is not a molecule failing a test. It is a meeting, a rumor, a war, and a ledger with a hole. Ibrahim writes it under *what did not get cheaper*: trust. Trust is not on a transistor curve. A species that can read a genome in an afternoon and cannot finish a vaccine it has owned for generations is not waiting on helium. It is waiting on a Tuesday in which the walk to the next house is allowed."""

P10 = r"""The speed of a passenger jet is an S-curve you can tell without a napkin, and Priya uses it when the napkin fails.

For a short drunk middle in the middle of the last century, airliners got faster every few seasons. Then the cruise of an ordinary long flight sat down near the same number and stayed, for longer than most careers. The spectacular next machine, a supersonic liner, was loud and thirsty and was parked. What kept changing was not the velocity. It was the price of a ticket, the safety of the hour, and how many people could buy the hour. Physics set a wall near the speed of sound for a machine that has to be polite to the towns under it. A meeting decided the tickets mattered more than the spectacle. You are living in the flat part. It is still a marvel: morning in one kitchen, evening in another. It is not a method for crossing an ocean in ten minutes. Photograph only the years labeled *faster*, rule them out to year 12,000, and you have the chip sermon with wings. The shoulders were the part that told the truth.

She puts the pen down and says the part the drawing was avoiding. Priya Nair is Mara’s sister. The sister’s clinic was not a second woman kept on the board for symmetry. It is this woman, on the days the sequencer waits for a part and the patient list is longer than any trial. She believes in steep middles. She has stopped believing a steep middle is a personality. The coast is a real coast. The delay to the greenhouse is the long one. They do not have a conversation. They have a stack of monologues. The prologue’s word is still the right word. A monologue can carry an S-curve. It cannot carry a hug, and the book will not pretend the radio invented one.

The invoice under the jet is the same short list as the invoice under the chip, which is why she bothers with the drawing at all. Fuel. Noise. A metal that survives the hour. A crew. A politics that will let the machine land. Leave any of those off the napkin and the napkin becomes a rocket. She has watched men turn the napkin over and draw the rocket anyway. She lets them. Then she turns it back. The flat part is still a flight. The flight is not a law."""

P11 = r"""Give the skip a number a kitchen can hold without a poster.

Take a cabin at ninety-nine and a half percent of the speed of light. The factor by which the stay-at-home clock outruns the cabin clock is about ten. One year of proper time aboard is about ten years in the kitchen you left. You are younger than the twin who stayed, by about nine years. You did not live those nine years. You were not wise inside them. You were in transit. Your joints are the joints of the year you left, plus whatever the radiation charged and did not refund.

where the factor is gamma: one divided by the square root of one minus the speed squared, in units where the speed of light is one.

That trip is not the year 12,000. To skip centuries you need a factor of hundreds, which is a speed even closer to light, which is an energy bill that stops being a vehicle and becomes a civilization’s output. For a cabin with the mass of a small truck, already at this modest factor of about ten, the kinetic energy is more than a decade of everything humanity currently generates and burns. You pay a similar bill to stop. If you do not stop, you do not arrive. You pass. Appendix A11 sits the arithmetic down where it cannot be waved through. The shape is the lesson. The body’s clock did not speed up to meet the catalog. A faster path ticks less. Less is the opposite of a longer life.

The engineers already pay a tiny version so a map will not lie.

Clocks flown around the world on airliners in 1972, with the care of a physics lab, disagreed with the clocks that stayed home by tens and hundreds of billionths of a second. The satellites that tell a phone where it is must be corrected by about thirty-eight millionths of a second a day, or the map walks off by kilometers. The gravitational part of that correction and the speed part do not even point the same way. They nearly cancel, and the remainder is still enough to ruin a position. Muons, particles that should have died in the upper air, reach the ground in numbers a stay-at-home lifetime does not allow. Hot, all three. None of them is a healthspan. They are the proof that the skip is real physics and a ridiculous medicine.

Mara’s delay is the same family at a walking pace. Minutes, not a new birthday. She will not buy the cabin. Nobody has the cabin for sale. The poster has a cabin. The poster does not have a decade of planetary energy, and it does not have the stop. She spends the minutes logging a film. The film will not become younger because a twin in a story did."""

P12 = r"""A cloth and a ledger finished a disease that never got a vaccine.

Guinea worm is a parasite caught from water. It leaves through the skin, which is as much detail as a kitchen needs. There is no shot that ended it. The work that drove it from millions of cases in the nineteen-eighties to a handful of cases in a year, in the middle of this decade, was a filter on a jug, a person kept away from the pond, a volunteer with a book, and a meeting that did not get bored. Hot as a result. Instructive as a wall. The missing piece was not a molecule. The missing piece was a Tuesday that kept happening. A transistor did not carry the jug. A neighbor did. When the neighbor cannot walk, the worm keeps a calendar. Different pathogen from polio, same invoice: a tool the species already understands, and a street the tool is not allowed to finish.

The vials of the last pandemic made the same point in a richer ledger.

A sequence became a vaccine faster than a monastery would have dared, which the stair chapter already counted as real. The shipping of that stair was a meeting. High-income kitchens had doses in arms while many low-income kitchens were still waiting on a promise with a logo on it. The molecule did not ennoble the queue. For a year, the queue was the product a body could actually catch or miss. That is not a reason to sneer at the stair. It is a reason a ×200 catalog cannot assume the queue will abolish itself because the chart was steep. Owen’s board is a small, fluorescent version of the same queue. One win on the table. A line of other doors. A budget that is political weather. Multiply his Tuesday by every hospital that does not have his table. That product is the next chapter. The cause of the product is this one. A meeting moved, or did not.

Mara’s spare part slips a date for the reason a filter slips a village. Someone did not walk. She cannot radio the pond. She melts the ice she has, which is a walk available to her hands, and she logs the pH afterward. The log will not eradicate anything. It will keep one tray honest while a larger ledger, elsewhere, decides whether the next pump ships. Both ledgers are institutions. Only one of them smells like basil."""

P13 = r"""Priya’s letter is a no, and the no is doing its job.

She asked about a trial that might quiet a knee the way a mouse paper had implied a knee could be quieted. The answer came back eligible on the biology and closed on the calendar. The site had the number of people it was built to hold. Her name was a row past the number. Dr. Mehta keeps a drawer of those letters. Priya has one of them on a table that also holds a sequencer’s maintenance log. Two ledgers, one coast. Neither ledger is a fountain. The science did not declare her joint unworthy of a question. The question had already spent its seats.

What she got instead is the boring list, which is the healthspan this century will actually sell to most bodies. A pressure pill she can name. A vaccine she already trusted and still had to go and get. A surgeon for a problem that will not be in a keynote and is, this month, the problem that was going to take the corridor away from her. The surgeon’s bill is an argument with an insurer. The argument is not a low-millions gene truck. It is still an argument, and arguments slip. Boring is hot when it works. It does not photograph. A slide would like Priya to be a before-and-after of a species. She is a woman on a coast waiting for a date a meeting set, with a knee that keeps its own clock while the date approaches.

Most candidates never become even that argument.

Of the drugs that enter human testing, fewer than one in ten are eventually approved. The rest die in a first look at safety, or in a middle trial that was mostly hope, or in a large comparison that is finally allowed to disappoint. The price of the vial that lives includes the price of the dead ones. That is why a molecule that is cheap to print can still cost what a house costs. You are paying for years, for nos, for a cemetery of trials. A founder who shows you the surviving vial and hides the cemetery is cropping the curve again. Ask for the cemetery. If the answer is that the cemetery is confidential, you are not in a kitchen. You are in a costume.

Mara reads the letter on a delay long enough that the knee in it has already had two further bad weeks. She cannot redirect the capsule. The capsule is not for that knee, and it is not hers to mail. She writes back the only numbers she trusts: the jar, the swear-count, the pH. It is a poor gift and the same currency. A local fact, logged, instead of a sermon about what the trial would have meant if the row had been one line shorter."""

P14 = r"""The mark in the tissue has been measured. It was a renovation, not a loft.

Adults who spent years holding an entire city in their heads — London’s taxi drivers, in the years when the map had to be the person — grew a larger posterior hippocampus. That is a structure the brain already uses to lay down maps of places, not a room behind a locked door. The size tracked the years on the job. A neighboring part of the same structure ran smaller. The scan did not find empty apartments filling with unused genius. It found a wall thickened and a wall giving way, a bill in the shape of a city. Leave the job and the renovation has less reason to stay. The mornings were the price. A phone that holds the city now does not refund those mornings to the people who paid them. It changes what the next person will thicken instead. A tool can retire a map. It cannot retire the fact that the map was overtime.

Children meet a different rate, and only while the construction site is open.

There is a window in which an eye, a language, or a hemisphere can be rerouted at a discount you will not be offered again at forty. The window is a sensitive period: biology’s own price list, cheaper early, brutal later. A child who loses a hemisphere and learns to talk has not revealed a second brain in the wrappings. The remaining hemisphere is doing two jobs. The body keeps the receipt in a weak side and in a childhood that was about rehabilitation as much as it was about ordinary school. A slide that says *therefore we may enhance the child* has stolen the receipt and kept the heroism. Look first. The window is a reason to teach, to protect hearing, to leave a construction site alone. It is not a reason to install a species project in a person who cannot consent to the bill.

Rohan is on the orbiter. He is not at her shoulder, and the earlier sentence about his voice should be heard that way.

He certified this class of pump before she launched. That is why the procedure already knows the valve. He sends steps with numbers. She is still bleeding a fitting on step two when step four arrives, because the light-time does not wait for a glove. The wrong tries are hers. The try that holds is hers. His knowing is a recording that left earlier than her question. Plasticity, at this distance, is a woman, a late note, and a machine that does not care which of them feels proud. No cupboard opens. The water melts or it does not. She logs the pH with the same hands as the first chapter, plus a new bruise, minus nothing a sermon is allowed to claim."""

P15 = r"""The drawing we actually have is a fly. The fly is the honest scale. Praise it, and then refuse the costume pinned to it.

In the middle of this decade a collaboration published a wiring diagram of an adult fruit fly’s whole brain. On the order of a hundred and forty thousand neurons. On the order of fifty million synapses, the junctions where one cell signals the next. Years of stubborn work, and the kind of result a kitchen should be glad exists. It is a fly. A human brain has on the order of eighty-six billion neurons. The connections are not a thicker copy of the diagram. They are a weather of chemistry that changes while you read this, plus a body sending blood, hormone, pain, and the angle of a wrist. We do not have that drawing. If we fixed a person in order to get one, we would have a picture of a stopped state. We would not have the Tuesday, which was a walk.

where a synapse is a junction, not a soul, and a diagram of junctions is not the person who used them.

Running the fly is a second job wearing the first job’s coat. A library of wires does not twitch. A twitch needs the physics of the membrane and of the chemicals that bias it. Pieces of the library are being loaded into simulations. A simulation that behaves like a piece of a fly is a magnificent instrument for studying flies. It is not a fly’s biography, and the fly did not move house into the computer. Scale the boast to a human and the unsolved physics is multiplied by hundreds of thousands in cell count alone, before the body, before the years, before the question of who would own the copy. The file-story skips this. It has to skip it. This is the invoice, and the invoice does not fit on the poster.

Cooling a person does not smuggle the file in through a nap.

After cardiac arrest, hospitals spent years on how cold a survivor should be made. One large trial compared a colder target with a milder one and found no bonus for the colder plan. A later trial compared deliberate hypothermia — a controlled drop of core temperature — with a plan that refused fever and did not chase the cold. The colder plan did not buy better survival. It bought a protocol whose harms are real: bleeding, infection, a metabolism that is not a hibernator’s metabolism. Arctic ground squirrels do take their temperature down and rebuild connections afterward. Hot as zoology. Cold as a dose you can hand a crew. Their proteins tolerate a pause that human proteins treat as an emergency. Space agencies have paid for animal-torpor studies because a sleeping animal uses less food, less air, and starts fewer quarrels. That is logistics. Logistics are allowed to be interesting. They are not a longer thread. You wake as the same worldline, weaker, and the many clocks did not punch out while you were cold.

Her outbound leg, if a manifest ever calls it outbound, will be awake. She has already declined the freezer in a note Rohan will read late. The note says she will spend the stores and keep the hands, because the hands are what have logged the chemistry without lying. A sleeping bag with a product name would arrive as a poster and would still require an airlock at the other end. She would be older by the proper time of the trip, not by the year printed on the poster. The distinction is Chapter 11. It does not get softer because someone offered a blanket."""

P16 = r"""The letter from the coast arrives in the same hour as a lid that only takes one swear.

Priya’s surgery went the boring way. A date, a surgeon, a problem that was not a letter in hemoglobin and not a graph from a mouse. She can walk the clinic corridor without the negotiation the corridor had become. She is not young. She is a woman who received a local win a ministry could understand, after a letter that said no to the trial and yes, later, to the ordinary knife. Mara reads it twice. The delay means the walk has already happened. She is glad about a Tuesday she was not in. She puts the printout in the margin of the pH log, beside the swear-count. Two invoices, paid in the same currency. A joint. A corridor. Neither of them helium.

Rohan’s note, crossing hers in the queue, is about the pump. He congratulates the wrong morning again, which she has decided to treat as a private joke rather than a fault in the man. At the bottom he adds that the ground team has stopped calling the freezer a medical plan. They call it a mass budget now. She is glad the noun moved. A mass budget is an invoice with kilograms on it. A medical plan would have been a costume with a temperature dial. He remains the life-support lead on the orbiter, where the geometry makes him late to her and closer to the factory than she is. He certified the pump class. He does not watch the seal except on a camera that is already behind the moment. A colleague. A recording. A body running the same many clocks, not a spare mind in her cupboard and not a file.

She would vote for this hour. The vote is not a speech. It is the lid, the letter, the late joke, the film that will go alkaline if she gets sentimental about any of them. Sentiment may name the basil. Sentiment may be glad Priya walked. Sentiment does not get to change the number she writes down."""

INSERTS = [
    ("01_Part_One_Many_Clocks.md", "Appendix A1 writes what", P1),
    ("01_Part_One_Many_Clocks.md", "Appendix A2 writes the ledgers", P2),
    ("01_Part_One_Many_Clocks.md", "Appendix A3 writes Hayflick", P3),
    ("01_Part_One_Many_Clocks.md", "Appendix A4 writes the sickle-cell-class", P4),
    ("01_Part_One_Many_Clocks.md", "Appendix A5 writes cancer", P5),
    ("02_Part_Two_The_Organ_You_Already_Use.md", "Appendix A6 writes the energy", P6),
    ("02_Part_Two_The_Organ_You_Already_Use.md", "Appendix A7 writes sleep", P7),
    ("02_Part_Two_The_Organ_You_Already_Use.md", "Appendix A8 writes wanting", P8),
    ("03_Part_Three_Not_A_Straight_Line.md", "Appendix A9 writes the class", P9),
    ("03_Part_Three_Not_A_Straight_Line.md", "Appendix A10 writes logistic", P10),
    ("03_Part_Three_Not_A_Straight_Line.md", "Appendix A11 writes the ratio", P11),
    ("03_Part_Three_Not_A_Straight_Line.md", "Appendix A12 writes institutions", P12),
    ("04_Part_Four_The_Honest_Body.md", "Appendix A13 writes trial", P13),
    ("04_Part_Four_The_Honest_Body.md", "Appendix A14 writes stroke", P14),
    ("04_Part_Four_The_Honest_Body.md", "Appendix A15 writes copy-versus-travel", P15),
    ("04_Part_Four_The_Honest_Body.md", "She does not have year 12,000. She has a film that will go alkaline if she gets sentimental.\n\nThat is the honest body.", P16),
]

if __name__ == "__main__":
    for fname, anchor, block in INSERTS:
        insert_before(fname, anchor, block)
