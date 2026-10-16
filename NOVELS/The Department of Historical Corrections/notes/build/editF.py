# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/histcorr/rev3')
from lib import Doc
from n_text import *
d=Doc('/workspace/histcorr/rev3/rev2.md')
# --- continuity / history fixes
d.sub('where is Wakefield?','where is Huddersfield?')
d.sub('Arthur had spent eleven years pointing out','Arthur had spent twelve years pointing out')
d.sub('In 2019 we tested the modern stabiliser against a hospital records gap.','In 2011 we tested the modern stabiliser against a hospital records gap.')
d.sub('late at night on June the twenty-second','at ten past four on the morning of the twenty-third')
d.sub('Near dawn, Daniel fell asleep in a chair.','Towards four, Daniel fell asleep in a chair.')
d.sub('“Then there are thirty-nine more, and he has to explain why he wanted that one.”','“Then there are the forty I sent out last night, and forty more by seven, and he has to explain why he wanted that one.”')
d.sub('London continued to celebrate a victory four days old.','London was still celebrating a victory it had known about for two days.')
d.sub('It is two miles from Perrott’s back lane to the Foreign Office','It is a mile from Perrott’s back lane to the Foreign Office')
d.sub('Not me. I’d like that noted.”','Not me. For the avoidance of doubt.”')
d.sub('went onto Agnes’s drying rack.','went onto Agnes’s drying rack, where Nan Tully would find them first.')
d.sub('Bell stood beside the main switch with the officer from the ceremony.','Bell stood beside the main switch with Captain Reed.')
d.sub('The officer looked from one man to the other.\n\n“Captain Reed,” Arthur said.','Reed looked from one man to the other.\n\n“Captain Reed,” Arthur said.')
d.sub('The written consent forms had gone to pulp.','The written consent forms had gone to pulp, and Eleanor’s forearm, on which she had written every weight in marker, had run blue to the elbow; she read the total back from memory, and Miriam chalked it on the wall where it would be seen if anyone ever came to look.')
# --- new scenes
d.after('For the first time she smiled.',N1)
d.after('Real people were inconveniently specific.',N18)
d.cutp('It took two hours and ten minutes.',N16)
d.after('Ives proposed that the present copies be lodged',N3)
# Perrott
d.sub('Perrott came himself. He was small, precise and visibly annoyed at having a morning with people in it.\n\n“Mrs Crumb?”\n\n“Yes.”\n\n“Your note alleges a textual discrepancy.”','@@N4@@')
d.sub('@@N4@@',N4.strip('\n'))
# Daniel newspaper office
d.before('That evening she went back to the shop alone.',N17)
# Bell in the shop
d.after('It was not a symbol. It was how she ate.',N21.replace('The gentleman who called on you this morning. Mr Brown.','The gentleman who called on you this morning, who gave the name of Brown.'))
d.sub('On the counter lay a note from Bell’s secretary:','Beneath the card he had left a note in his secretary’s hand:')
# Pembroke File: split ch 14
d.sub('## 14 The Spare Room','## 14 A Protected Handset')
d.after('After the call, he sat with the receiver in his hand.',N2.strip('\n'))
# Garrick payoff in ch 29
d.after('The reconciliation clock showed one hour and eleven minutes.','At 08:19 Garrick telephoned from a car park in Victoria Street. For the avoidance of doubt, he said, he had countersigned the Minister’s instruction at 08:14, in the wrong ink, one minute before the van was due to leave. The van, which had a rota, had left anyway, with nothing to collect and a form saying so.')
d.save('/workspace/histcorr/rev3/rev3a.md')
print(d.fail)
