# -*- coding: utf-8 -*-
import sys,re; sys.path.insert(0,'/workspace/histcorr/rev3')
from lib import Doc
d=Doc('/workspace/histcorr/rev3/rev3a.md')
SJ = """* * *

He gave up on sleep at four, took the copy of the file and went down to Operations. The lights were at their night setting, and Miriam was sitting on the floor in front of the console with her back against the yellow line.

“You’ve been told,” she said, without turning round. “Everyone has been told something at this hour. It’s an old department habit.”

“I’ve been told I was looked after.”

“You were.” She patted the floor. “I was going to say more. I decided it wasn’t mine to say. Then I decided that was exactly what everyone here says.”

He sat. The linoleum was cold through his trousers.

“Tell me what he signed,” Arthur said. “I know he signed.”

“You know because you’ve got his face.”

“Because Bell says I wasn’t unhappy at first. Nobody says that about a man who was dragged in.”

Miriam was quiet long enough for the machine to tick twice. “It was a Tuesday,” she said. “They’d had forty people in the custody rooms for nine months and the lower archive was meant to hold twenty. They slept in shifts. A woman had a baby on a table in the sanitation store. Bell came down with a clipboard and a sandwich and said he could have them all in proper housing by evening. Not as a bargain. As a fact. He needed one signature on an administrative post, and the housing would follow, because the post controlled the budget.”

“And he believed that.”

“For two and a half years. It was true, mostly. People got beds. You got a signature on everything else, one at a time, each of them small. I was in the archive. Jon brought me tea. You came down every night with your hands full of things people had asked you for, and you looked—” She stopped, and chose. “You looked like someone doing the one job he’d ever been good at.”

“Which was?”

“Making things happen on forms.” She smiled with half her mouth. “It’s not an insult. It’s the most useful thing anyone could be. That was the trouble.”

“And then?”

“And then the register. A man called Evans was refused a transfer because his name was on a list that couldn’t be shown to him. You asked who kept the list. Somebody told you there wasn’t a list; there was a rule. So you asked for the rule.” She looked at her hands. “That’s when Bell started asking me what you were like in the mornings. As if I’d know.”

“Did you?”

“By then. Yes.”

The console ticked. Somewhere above them the ventilation changed key.

“I’m not him,” Arthur said.

“No. You’re better at the start, and you’ve a worse haircut.” She wiped her face with the heel of her hand. “I keep waiting for you to do something he did, so I’ll know what to say. Then you do something he never did. You went and read your own file.”

“I don’t think that’s an achievement.”

“It’s the first thing he should have done,” said Miriam, “and he didn’t, and it killed him. Go to bed, Arthur.”

“Is that an order?”

“It’s a suggestion from someone who hasn’t had any.” She leaned her head back against the console. “Take the blanket. It’s Fanshawe’s. He won’t miss it. He has others, in the shape of his reputation.”

He took the blanket.

"""
SA = """Before the briefing, Eleanor took Miriam to the coil store on B3, and Arthur went with them because nobody told him not to.

It was a steel cage in a room that smelled of warm copper. The coils lay in padded cradles, each the size of a drum, each tagged with a date, a mass rating and the initials of whoever had last signed it off. Eleanor ran a finger along the labels the way other people check a bookshelf.

“Left and right,” she said. “Both rated two hundred. Both tested Friday.”

Miriam squatted beside the left cradle and read the tag without touching it. “This is the replacement.”

“Yes.”

“It’s the same part number.”

“It’s the same specification. Part numbers don’t change when you replace like for like.”

“They do when you replace like with better. And it overheated on Monday.”

“At nine thirty-two I was putting a second adult through the booth on a reserve I’d stripped. Anything overheats.” Eleanor lifted the lamp from its hook. “I replaced it in the spring. I signed the job card.”

“Have you looked at the coil, or the card?”

There was a short silence in which Arthur learned that it is possible to hear somebody decide not to be offended.

“The card,” said Eleanor. “Because I wrote it.” She shone the lamp along the housing, and her face did a small calculation and closed again. “It’s fine. There’s a mark on the casing from the old repair. It ran hot because it was loaded unevenly. I fixed the load.”

“All right.”

“It’s fine.”

“I said all right.”

“You said it in a way that meant something else.” Eleanor hung the lamp back on its hook with some care. “I do check, you know. It’s the only thing I do.”

“You check what you’re worried about,” said Miriam. “You taught me that. You also taught me the other thing, and I can’t tell which of them you’d forgotten.”

Arthur, who had been studying a shelf of fuses with great attention, understood that he had been allowed to witness something he would not be asked about afterwards.

“We’re going to be late,” said Eleanor. They went up."""
d.sub('He took the copy to bed. It was not what the registry had intended the file to be used for.\n\n## 99 The Spare Room','He took the copy to bed. It was not what the registry had intended the file to be used for.\n\n'+SJ+'## 99 The Spare Room')
d.after('Tuesday morning began with a departmental breakfast',SA)
# similes / clipboard pile-up
d.sub('Garrick had stood through all of it with his clipboard against his chest like a hymn book.','Garrick had stood through all of it with his clipboard held across his chest.')
d.sub('He consulted the clipboard, as though it might have changed its mind.','He consulted the clipboard.')
d.sub('had come up from the hearing room with her handbag held in front of her like a shield, looked at him with the interest of a woman who has been handed a rare specimen.','had come up from the hearing room with her handbag held in front of her, looked at him with frank interest.')
d.sub('Pelling’s telephone rang. He looked at the screen and then, with a quick wrenching decency, put it on the table and pressed speaker.','Pelling’s telephone rang. He looked at the screen and then, with a quick decency, put it on the table and pressed speaker.')
# explainers
d.sub(' Procedure had injured people. It could also prevent a man from deciding privately which injuries counted.','')
d.cutp('It had not helped in the ordinary sense.')
d.sub(' Arthur did not romanticise the inconvenience. Good oversight could also be badly designed. He filed suggestions after the message had gone.',' He filed suggestions after the message had gone.')
d.sub(' The child was already asking the right person, and the teacher was allowing the question to remain difficult.','')
d.sub(' That would have made it solemn, and they had earned something less demanding.','')
d.t=re.sub(r'The Bells were being investigated under ordinary offences.*?events they could prove\.','The Bells were being investigated for fraud, unlawful detention, assault and conspiracy. Their different ages complicated attribution but did not prevent it.',d.t,flags=re.S)
d.t=re.sub(r'The Bells remained in custody under separate case numbers\..*?permanent centre of his life\.','The Bells remained in custody under separate case numbers, and their lawyers disagreed about whether the later man’s admissions could be used against the earlier one. The court asked for evidence of each act. Arthur answered requests to clarify his notebook, carefully, and did not follow every hearing.',d.t,flags=re.S)
# ending echo
d.after('On a cold Monday, Arthur arrived at work with a bag of pastries','In the corridor outside Records the duty board said MONDAY, and Monday it was. The analyst who had once changed it to Tuesday now held a post in which she kept her own chalk. In the bottom corner, small, she had added WE CHECKED.')
d.sub('Arthur took a fresh sheet of paper.\n\nFor once, he knew exactly how to begin.\n\nReceived, he wrote.\n\nThen he added the date.','Arthur took a fresh sheet of paper. He considered several openings that began with the word impossible. Mrs Crumb had once advised him, about people who remember lives you don’t, not to begin by telling them they are wrong, and it seemed to extend to correspondence.\n\nReceived, he wrote.\n\nThen the date and, after some consideration, AS OBSERVED.')
d.save('/workspace/histcorr/rev3/rev3b.md')
print(d.fail)
t=d.t.split('## A Note to Readers')[0]; print(len(t.split()))
