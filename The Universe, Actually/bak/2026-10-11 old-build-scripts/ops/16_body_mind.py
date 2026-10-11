# -*- coding: utf-8 -*-
OPS = [
# ---- front matter repairs (broken sentences left by an earlier redaction)
('fsub', 'note', "This book is written for the reader the earlier guides.", "This book is written for the reader of the great one-volume guides to science: an intelligent person who is not a specialist, and who would rather be told what is known than be flattered with wonder."),
('fsub', 'note', "The model is his New Guide to Science, together with the shorter guides to physics, chemistry, and biology.", "The model is a classic one-volume guide to science from the 1980s, together with the shorter guides to physics, chemistry, and biology that preceded it."),
('fsub', 'sources', "Readers who want the predecessor guides can still find them: the earlier guides.", "Readers who want those predecessors will find them listed in the bibliography below."),
('fsub', 'sources', "in the tradition of the earlier guides.", "in the tradition of the classic one-volume science guides."),
# ---- ch50 human body
('sub', 131, "Vitamins and minerals are required in smaller amounts. Some, like vitamin C and the B vitamins, are cofactors for enzymes. Deficiency diseases—scurvy, rickets, beriberi—were traced to missing vitamins in the early twentieth century. The tracing was one of the clearest demonstrations that specific molecules have specific roles in the body.", "Vitamins and minerals are required in smaller amounts, as the next section explains."),
('set', 131, "Hormones are chemical signals carried in the blood.", "Hormones are chemical signals carried in the blood, described in the next section. Together with the nervous system, they form the body’s two great communication networks."),
('set', 131, "The immune system distinguishes self from non-self", "The immune system distinguishes self from non-self and attacks the latter; its workings are described below. Autoimmune diseases occur when the distinction fails and the system attacks the body’s own tissues, and allergies when it overreacts to a harmless substance."),
('sub', 180, "The system is simple in outline and tightly regulated in practice.", "The whole arrangement is a closed loop under constant adjustment."),
# ---- ch51 nervous system
('sub', 1449, "Neurons communicate by action potentials and chemical synapses. The same ionic mechanisms found in other animals operate here. What differs", "The neurons work as described earlier. What differs"),
('sub', 1806, "No single region is sufficient. Lesions, stimulation and recording studies show that each function recruits a characteristic set of areas whose precise contribution remains under investigation.", "The precise contribution of each area remains under investigation."),
# ---- ch52 neuroscience lead: drop the short first-pass paragraphs that the detailed ones repeat
('del', 3259, "A neuron signals by electrical pulses and chemical synapses."),
('del', 3259, "The map of regions is older than the mechanism."),
('del', 3259, "The great technical change is the ability to record and to perturb."),
('del', 3259, "Disorders keep the field honest."),
('del', 3259, "Neuroscience can say, with confidence"),
('sub', 3259, "Critical periods exist, during which certain skills are acquired more readily. Deprivation during a critical period has lasting effects.", "Critical periods, taken up under plasticity below, show how much the plan depends on input."),
('delsec', 2027),
# ---- ch53 consciousness lead
('del', 3275, "Some contrasts are reliable."),
('set', 3275, "Two cautions follow.", "Two cautions follow. First, consciousness is not a license to ignore mechanism. Whatever experience is, in humans it depends on particular brain processes, and those processes can be disrupted in particular ways. Second, the unsolved problem is not evidence for a particular doctrine. It is evidence that the problem is unsolved. A guide written now should say so without embarrassment. The great guides of the twentieth century could not close this question either, and neither can this one."),
('sub', 3275, "Theories differ on which feature is decisive. Global workspace theories emphasize broadcast. Integrated information theories emphasize a structural property. Higher-order theories emphasize a representation of the representation. Each makes predictions. Adversarial collaborations", "Each of the theories above makes predictions, and adversarial collaborations"),
('delsec', 3036),
# ---- ch54 aging lead
('set', 3290, "Cells accumulate damage.", "Aging can be described as the accumulation of damage plus the decline of maintenance. Cells suffer mutations. Some mutations are harmless, some kill the cell, and some push the cell toward cancer. Proteins misfold and aggregate. Mitochondria become less efficient and more productive of damaging byproducts. Telomeres shorten in tissues that divide, limiting further division. Stem-cell pools shrink. The immune system becomes less precise and more inflammatory. Epigenetic marks, which help cells remember their identity, drift. Each of these is documented. Their relative contributions differ by tissue and by species. No single lesion is “the cause” in the way a single bacterium is the cause of tuberculosis."),
('del', 3290, "Aging can be described as the accumulation of damage"),
('sub', 3290, "The list is encouraging, because lists can be tested. Animals", "Some of these mechanisms can be tested directly. Animals"),
('del', 3290, "Senescence is a particular target."),
('del', 3290, "Human lifespan has already changed, mostly for other reasons."),
('sub', 3290, "Mutations in nutrient-sensing pathways extend life in short-lived species. Rapamycin extends life in mice even when started late. Senolytic drugs", "Senolytic drugs, which clear cells that have stopped dividing but refuse to die and secrete inflammatory signals,"),
('sub', 3290, ", which clear senescent cells, improve health measures in old mice.", " improve health measures in old mice."),
]
