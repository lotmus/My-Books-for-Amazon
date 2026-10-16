# -*- coding: utf-8 -*-
import sys,re; sys.path.insert(0,'/workspace/histcorr/rev3')
from lib import Doc
d=Doc('/workspace/histcorr/rev3/rev3b.md')
K = """“Ask him,” Bell said, “why the man on the trolley signed.”

The room turned. Nobody had mentioned a trolley in public session. Arthur understood that Bell had not needed Miriam to tell him; he had been there when it was wheeled.

“Do you know what he refers to?” Dame Judith asked.

“I think so. A version of me signed an appointment in 2027. There were forty people in a room built for twenty, and he was told the appointment would get them beds.”

“And did it?”

“It did,” Arthur said. “Mr Bell is right about that. It did, for two and a half years.”

Bell inclined his head, as to a witness who has conceded a point.

“Then the question is simple. Forty people in a room. A baby. A signature. Would you have signed?”

It was a clever question. It had been built, Arthur thought, by a man who had asked himself the same thing on a staircase and not liked the answer. He had a drilled response. He found he could not use it in front of a judge.

“I don’t know,” he said. “I think I would have wanted to very much. I would like the beds to be a fact without the signature. I don’t know whether that’s possible.”

“Then you cannot condemn it.”

“I can ask to be allowed to find out. It’s all I’ve done since Monday.”

Dame Judith wrote something down, underlined it twice and said, to the transcript, “The witness has declined to claim a certainty he does not possess. We shall note it.”

For the space of a breath Bell looked as though he had been given exactly what he asked for, and found it was not what he wanted."""
C = """Dame Judith North found him in the corridor outside the registry, where he had gone to stand still. She had taken off her shoes, an act of such casual authority that nobody had remarked on it, and carried them by their straps.

“You told Mr Bell you didn’t know,” she said.

“I didn’t.”

“I should like to hear what you think, off the record, where it needn’t be evidence.”

He looked at the floor tiles. “I think I’d have signed on the Tuesday. Possibly the Wednesday. I’d have gone on telling myself it was temporary and the next one was the last.”

“Good.” She seemed satisfied. “I sat on the bench for thirty years in a country that now says I didn’t. I know what happens to a person who is told they did not do the thing they did. I would have signed anything. For about a month.” She inspected her stockinged toes. “A month is a very long time to be nobody. Do you know what saved me?”

“The file.”

“A solicitor in Leamington named Haldane, who wrote to say she had read my judgment in the Hendry case and thought paragraph forty-one was wrong.” Her face did something complicated. “It was. Nobody had told me in eleven years. I could have wept. Someone had read me.”

“And that gave you your life back?”

“It gave me paragraph forty-one,” said Dame Judith. “Be careful with evidence, Mr Pembroke. It’s only paper. But it is the only thing that arrives when you’re not there.” She stooped for her shoes. “I shall go and eat the toast. I’m told it’s an unreliable butter.”"""
R = """

“Captain Reed read the order twice and asked who had signed it. Mr Bell had. He asked under which section. I believe I said section nine before he did. He observed that section nine covers interference and not entry, and that he would like a receipt for the order, for his file.” Pelling put a hand on the wall. “Mrs Crumb’s deputy wrote it out. He took it in front of his men and put it in his breast pocket. I have not been so impressed by anyone in a long time. I was wearing a tie that had no business being so frightened.”"""
H = """

Eleanor found Miriam at the aperture afterwards and said nothing for a full second, which for her was a speech.

“You were right.”

“Yes.” Miriam did not look up from the gauge. “Don’t. I need you to be sorry later and useful now.”

“I can do both in parallel.”

“Then do the second one faster.”"""
d.after('I would stop you making the alternative illegal to describe.',K)
d.after('Pelling pushed through the lobby','') if False else None
d.sub('Dame Judith accepted one and asked whether butter had survived the revision. Nobody was certain, but the yellow substance available was serviceable.','Dame Judith accepted one and asked whether butter had survived the revision. Nobody was certain, but the yellow substance available was serviceable.\n\n'+C)
d.sub('“The officers have withdrawn pending verification of their order,” he said.','“The officers have withdrawn pending verification of their order,” he said.'+R)
d.sub('Jon read the tenth name.','Jon read the tenth name.'+H)
d.save('/workspace/histcorr/rev3/rev3c.md'); print(d.fail)
t=d.t.split('## A Note to Readers')[0]; print(len(t.split()))
