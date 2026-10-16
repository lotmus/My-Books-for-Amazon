import re
P='../../The Department of Historical Corrections - REV13.md'
b=open(P,encoding='utf-8').read()
def rep(a,c):
    global b
    assert b.count(a)==1,a[:60]; b=b.replace(a,c)
rep("He handed her the grey notebook for a moment. She wrote","He handed her the grey notebook. She wrote")
rep("and sat for a moment with the receiver still warm","and sat with the receiver still warm")
rep("Miriam looked at her for a moment with an expression Arthur had seen","Miriam looked at her with an expression Arthur had seen")
rep("Beatrice looked at him for a moment. “A gentleman.”","Beatrice looked at him. “A gentleman.”")
rep("looked at it for a moment, and put it in her coat pocket","looked at it, and put it in her coat pocket")
rep("The entry was initialled EV. The only EV in the building was too young to have been anywhere in 1991, and wore a watch on each wrist. I did not ask her. I traced my mother instead. She was in my kitchen.”","The entry was initialled EV. The only EV in the building wore a watch on each wrist. I did not ask her. I did not need to; I had my mother’s story, and now I had a ward, a month and a woman’s wrists.”")
rep("“Nineteen eighty-eight is closed.","“Nineteen eighty-eight is closed.")  # sanity anchor
rep("“That’s your hand.”\n\n“I was twenty-five.","“That’s your hand.”\n\n“I was twenty-five.")
rep("Beatrice took off her spectacles. “I have been very careful ever since.”","Beatrice set down her pencil. “I have been very careful ever since.”")
open(P,'w',encoding='utf-8',newline='\n').write(b)
