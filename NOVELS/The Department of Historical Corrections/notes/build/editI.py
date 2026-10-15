# -*- coding: utf-8 -*-
import sys,re; sys.path.insert(0,'/workspace/histcorr/rev3')
from lib import Doc
d=Doc('/workspace/histcorr/rev3/rev3c.md')
O = """The back stair let them out behind the registration hall, and the quickest way to the lower door was twenty yards along the wall behind the counters. Jon walked it with the slow, absorbed gait of a man whose bucket was heavy. Arthur held the clipboard up to his face in the manner of someone reading.

The clerk at the end counter was writing on a pad she kept below the edge, out of the camera’s angle. Ms Okafor looked up once, at the clipboard rather than at the face, and said to the middle distance, in the voice of someone reading out a number:

“Page seven.”

She slid the pad six inches along the shelf. Arthur did not stop. He took it as he passed, the way one takes a leaflet, and slid it under the clipboard. Page seven was a list in a small upright hand: names, the word *Sunday* and an address, *Camberwell District Hall, Hall B*. The fourth line read *Aliyah Rahimi (mother of K., 13)*.

“I wasn’t asked to give you anything,” Ms Okafor said, still to the room. “For the record. I write down what is said to me. It’s the only protest I can afford on this grade.”

“Thank you.”

“Don’t. It isn’t a rescue. It’s an address.” Her pen had not paused. “If you get anyone out, tell them somebody wrote them down.”"""
d.after('“Nobody asks a man with one why he’s walking slowly.”',O)
d.sub('Miriam knelt in front of him.\n\n“We haven’t found a route to her.”','Miriam knelt in front of him.\n\n“We know where she was held,” she said, because she could not bear to be less than exact. “Camberwell District Hall. A clerk wrote it down. We haven’t found a way to reach it.”')
d.t=re.sub(r'Karim’s mother remained unlocated\. The inquiry had preserved her name, Miriam’s last sighting and the future transport schedule\.','Karim’s mother remained out of reach. The inquiry had preserved her name and the page from Ms Okafor’s pad, with its address in Camberwell, in a branch that no longer had a door to it.',d.t)
d.save('/workspace/histcorr/rev3/rev3d.md'); print(d.fail)
t=d.t.split('## A Note to Readers')[0]; print(len(t.split()))
