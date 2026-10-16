# -*- coding: utf-8 -*-
import sys,re; sys.path.insert(0,'/workspace/histcorr/rev3')
from lib import Doc
d=Doc('/workspace/histcorr/rev3/rev3d.md')
F = """* * *

Mr Ferris was a law-stationer in Fetter Lane who held Daniel’s indenture, hired him out to Mrs Pike by the week and slept above his shop in a room that had been described to Daniel’s mother in 1812 as “a bed with prospects”. Daniel stood in the lane at one in the morning with the paper in his coat and threw gravel at the window, as he had once seen a man do in a play. It took three handfuls. Then the sash went up and a nightcap came out of it.

“Who is that?”

“Daniel Wren, sir.”

“It is one in the morning.”

“Yes, sir. I’m sorry. I wanted to give you something before somebody else told you about it.”

The nightcap withdrew. It took Mr Ferris four minutes to reach the door, during which Daniel counted the cracked cobbles and gave up every sentence he had practised. When it opened, the stationer stood there in a dressing gown with a candle, like a man who had been robbed of the right to be asleep and meant to send in a bill.

Daniel gave him the paper.

Ferris read it by the candle, with his lips moving, which Daniel had always thought they had in common. “This is your indenture.”

“Yes, sir. I’d like to surrender it.”

“You cannot surrender it. It is a contract. It has four years left in it. Your mother paid a premium.”

“I know. I’ll pay it back. Not tonight.”

“With what?”

“Wages. Mrs Pike will pay me outright.” It was a poor beginning, and he saw it in Ferris’s face. “She’s printing something tomorrow that will make some people angry. I wanted you to know I’d gone before you knew. That it was me. Not her. Not you.”

Ferris was silent. He was a heavy, tired man, and for the first time it occurred to Daniel that this same man had cut an hour from his own sleep, three winters running, to teach him sums. He had never said so. One didn’t.

“You were the best hand I had,” Ferris said at last. It sounded like an accusation. “You can add a column twice and not look up. I had you down to take the shop.”

“I know, sir.”

“And you want to go and print handbills.”

“I want to be the one who puts the name on them,” Daniel said. He had not practised that part.

Ferris looked at him for a long time. Then he took the indenture, folded it once and put it in the pocket of his dressing gown.

“I shall say you ran off,” he said. “I shall say it to everyone. I shall be extremely aggrieved. If anyone asks whether I knew, I was asleep.”

“Thank you, sir.”

“Don’t thank me. I shall return half the premium to your mother, and I shall have it in writing.” He raised the candle higher, so that Daniel could not see his face. “Go on. You’ll catch your death. Mind the cobbles at the corner, they’re loose.”

Daniel minded them. Behind him he heard the door close, and then not close, and then close again, much more slowly, by someone who did not want to be seen watching.

"""
old='He walked out at one in the morning to wake a man who would never forgive him, and came back at two with a sack of his belongings and no indenture, and slept on the floor beside the press as though it were the only bed in London that had not been priced.'
d.sub(old,'He walked out at one in the morning to wake a man who would never forgive him.\n\n'+F+'He came back at two with a sack of his belongings and no indenture, and slept on the floor beside the press as though it were the only bed in London that had not been priced.')
d.save('/workspace/histcorr/rev3/rev3e.md'); print(d.fail)
t=d.t.split('## A Note to Readers')[0]; print(len(t.split()))
