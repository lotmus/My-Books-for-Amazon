s=open('rev13_edit.py',encoding='utf-8').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:60],s.count(a)); s=s.replace(a,b)
rep("“I never asked what Schedule 14 was,” Beatrice said.","“I have been doing my dots,” Beatrice said. “A name or nothing, Arthur said, so I have been giving each of them a name. I started with the newest, because it was easiest, and worked backwards. I reached the oldest at half past nine.” She laid a finger on the green volume. “Then I looked across at the receipt, and the receipt said Schedule 14. So does the line.\n\n“I never asked what Schedule 14 was,” she said.")
rep("I had read the report. It said","I had read the report. It said",1) if False else None
rep("There isn’t one. He lets people sign.”","There isn’t one. He lets people sign.”\n\n“I am not going to tell you it’s all right.”\n\n“I would think less of you.”\n\n“I’m not going to tell you it isn’t, either. I haven’t worked out the proportions.”")
rep("“That was a clerk like me.”","“That was a clerk like me.”\n\n“Will you write to him?”\n\n“As a letter or as a correction?”\n\n“Which is the difference?”\n\n“I am told a letter can be declined.”")
rep("You would have been moved, and I needed you signing.”","You would have been moved, and I needed you signing.”\n\nCole had stopped writing. He moved his pen to the far side of the notebook, the way one moves a glass out of someone else’s reach.\n\n")
open('rev13_edit.py','w',encoding='utf-8').write(s)
