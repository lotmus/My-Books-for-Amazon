from pathlib import Path

p = Path(__file__).resolve().parent / "manuscript_text.txt"  # build source lives in scripts\
t = p.read_text(encoding="utf-8")
pairs = []


def add(a, b):
    if a not in t:
        raise SystemExit("MISSING: " + a[:120])
    pairs.append((a, b))


add(
    """Weinstein recited the back of the paper from memory. "The previous warning was sent too late."
"This is the previous warning. We're standing in it."
"Then we are late."
"We are on time for being late.\"""",
    """Weinstein recited the back of the paper from memory. "The previous warning was sent too late."
"Then this sheet is not that warning," Penny said. "The back is pointing behind itself."
"The voice is the late one," Derek said. "Don't open a door that had already opened."
"The front can still be early. Nobody has boarded.\"""",
)

add(
    "He wrote: DOOR ALREADY OPEN WHEN NOTICED, 10:05. OPENING EARLIER. TIME UNKNOWN. PAPER READ 10:22. SIGN: LATE.",
    "He wrote: SHEET, THEN THE DOOR. BOTH BEFORE 10:05. TIMES UNKNOWN. VOICE AFTER THE DOOR: LATE FOR DON'T OPEN. PAPER READ 10:22. THAT IS READING. FRONT STILL EARLY FOR BOARDING.",
)

add(
    """"No," Penny said. "Sunday is a notice at 18:17 for an opening at 18:00. That gap is the warning arriving after the act. Today the door was already open at 10:05, and we finished reading at 10:22. That seventeen is how long we stood there. Same numeral. Not the same gap."
"The sign on Sunday is late," Weinstein said. "The sign today is also late, and we do not know by how much, because nobody in that room wrote down the opening. A cause after an act cannot be the cause of the act. Munich cannot vote the order backwards."
"And we are not making a signature out of being slow," Penny said. "Herbert can sort Sunday. He cannot sort an opening we do not have.\"""",
    """"No," Penny said. "Sunday is a notice at 18:17 for an opening at 18:00. That gap is the warning arriving after the act. Today we finished reading at 10:22. That seventeen is how long we stood there. Same numeral. Not the same gap. And this slip is the previous warning. The back of this morning's sheet was pointing at Sunday, not at us."
"The sign on Sunday is late," Weinstein said. "Today the voice is late for the opening, and we do not know by how much, because nobody wrote the opening down. The sheet was already in the pocket before the door. Finishing the reading at 10:22 does not move it. A cause after an act cannot be the cause of the act. Munich cannot vote the order backwards."
"And we are not making a signature out of being slow," Penny said. "Herbert can sort Sunday. He cannot give us a clock for a voice we only know came after.\"""",
)

add(
    "Rule: Sunday's notice was seventeen minutes after Sunday's opening, and that notice could not prevent it. Monday's seventeen minutes is how long the office took to read. Write the sign. Do not copy the number from one gap onto the other.",
    "Rule: Sunday's notice was seventeen minutes after Sunday's opening, and that notice could not prevent it. Monday's seventeen minutes is how long the office took to read. The voice is late for the door. The sheet is not. Do not copy the number from one gap onto the other.",
)

add(
    """"Sunday," Derek said. "An opening at eighteen hundred. A notice at eighteen seventeen. That notice is late. Today the door was already open at ten oh five. We read the paper at ten twenty-two. That interval is us. The paper is late for the opening. I cannot tell you the size."
"That is a coordinate," Herbert said. "Put the earlier event first. You have been enjoying the wrong order.\"""",
    """"Sunday," Derek said. "An opening at eighteen hundred. A notice at eighteen seventeen. That notice is late. Today the sheet was already in the pocket, then the door opened, then the voice said don't. We noticed the open door at ten oh five. We finished reading at ten twenty-two. That interval is us. The voice is late for the opening. I cannot tell you the size. The sheet is not."
"That is a coordinate," Herbert said. "The voice is after the door. The sheet is not the late one. You have stopped enjoying the wrong order.\"""",
)

add(
    """DOOR NOTICED ALREADY OPEN: 10:05. OPENING EARLIER. TIME UNKNOWN.
PAPER READ: 10:22. THAT GAP IS HOW LONG WE READ. NOT THE LATENESS OF THE OPENING.
SIGN AGAINST THE OPENING: LATE. SIZE: UNKNOWN. CANNOT BE THE CAUSE.
SUNDAY'S OPENING: 18:00. SUNDAY'S NOTICE: 18:17. THAT GAP IS A WARNING AFTER AN ACT. DIFFERENT MEASUREMENT. SAME WORD, LATE.""",
    """DOOR NOTICED ALREADY OPEN: 10:05. OPENING EARLIER. TIME UNKNOWN.
ORDER IN THE ROOM, BEFORE THAT CLOCK: SHEET, THEN THE DOOR, THEN THE VOICE.
VOICE AGAINST THE OPENING: LATE. SIZE: UNKNOWN. CANNOT HAVE KEPT THE DOOR SHUT.
SHEET AGAINST THE OPENING: EARLIER. NOT LATE. SENDER STILL UNKNOWN.
PAPER READ: 10:22. THAT GAP IS HOW LONG WE READ. NOT THE SHEET'S ARRIVAL. NOT THE LATENESS OF THE OPENING.
SUNDAY'S OPENING: 18:00. SUNDAY'S NOTICE: 18:17. THAT GAP IS A WARNING AFTER AN ACT. DIFFERENT MEASUREMENT. SAME WORD, LATE.""",
)

add(
    '"Sunday\'s is a warning after an act. Today\'s is how long we read. Four minutes of reading, or an hour, and I would still say the paper is late for a door that was already open, and still refuse the train."',
    '"Sunday\'s is a warning after an act. Today\'s seventeen is how long we read. The voice is late for a door that was already open. The paper is not. I would still refuse the train."',
)

add(
    "Rule: Late for the opening, and you do not know by how much. Early for the train. Sunday's number sizes Sunday's miss. Today's number is how long you read. The sign is the case.",
    "Rule: Late for don't open, and you do not know by how much. The sheet was earlier than the door. Early for the train. Sunday's number sizes Sunday's miss. Today's number is how long you read. The sign is the case.",
)

add(
    '"I am in the future of your door and in the past of my landing. That is all I am. The sheet in your pocket was never in the past of the opening. I am not going to tell you how to file it."',
    '"I am in the future of your door and in the past of my landing. That is all I am. The sheet was already in the pocket before the door. The voice was not. I am not going to tell you how to file it."',
)

add(
    "CASE STATUS: BOARDING REFUSED. DOOR ALREADY OPEN BEFORE THE READING.",
    "CASE STATUS: BOARDING REFUSED. SHEET BEFORE THE DOOR. VOICE AFTER THE DOOR. THE READING IS NOT THE ARRIVAL.",
)

add(
    "You should finish able to say, without this page: a cause has to sit in the past of its effect; noticing an open door is not the time it opened; being in the same room does not let you reorder what already happened; a warning can be late for one act and early for the next; a repeated numeral is not a repeated gap; a birthday is the wrong field for a record you are writing now; a loop will not explain a sheet that was already in your pocket, and neither will the refusal you type afterwards.",
    "You should finish able to say, without this page: a cause has to sit in the past of its effect; noticing an open door is not the time it opened; being in the same room does not let you reorder what already happened; the voice can be late for the door while the sheet is still early for the train; a repeated numeral is not a repeated gap; a birthday is the wrong field for a record you are writing now; a loop will not explain a sheet that was already in your pocket, and neither will the refusal you type afterwards.",
)

add(
    "The door was already open at 10:05. That is when they noticed. The opening is earlier, and nobody wrote it down. The warning was read at 10:22. The reading is not in the past of the opening. It cannot have caused the opening, and it cannot be given a precise lateness until the opening has a time. Calling 10:05 the act is how you file a noticing as an event. That was the previous case's mistake, under a different noun.",
    "The door was already open at 10:05. That is when they noticed. The opening is earlier, and nobody wrote the clock time. The sheet was already in the pocket, and the room's order is sheet, then door, then the voice that said not to open it. Finishing the reading at 10:22 is not the time the sheet arrived. The voice is after the opening, so it is late for don't open, and the size of that lateness is unknown. The reading cannot be given the sheet's arrival, and it cannot be the cause of a door that was already open. Calling 10:05 the act is how you file a noticing as an event. That was the previous case's mistake, under a different noun.",
)

add(
    "A warning is not a single moment. It is a message paired with an act. Pair it with the door: the message comes after, so the sign is late. Pair it with boarding: the message comes before, so the sign is early. Nothing in that requires the two acts to be the same event. They are not. That was the other case.",
    "A warning is not a single moment. It is a message paired with an act, and this file has two messages. Pair the voice with the door: the voice comes after, so that sign is late. Pair the front of the sheet with boarding: the sheet was already in the pocket before the door, and nobody has boarded, so that sign is early. Nothing in that requires the two acts to be the same event. They are not. That was the other case.",
)

add(
    "Learning objective: Tell a warning's lateness from the time it took you to read.",
    "Learning objective: Refuse to treat the time it took you to read as a warning's lateness.",
)

add(
    "Sunday's notice was seventeen minutes after Sunday's opening. That seventeen is the size of a miss: the warning came after the act. Monday's seventeen minutes runs from 10:05, when the open door was noticed, to 10:22, when the reading finished. That seventeen is how long the office stood there. The opening had already happened. Its lateness has the sign LATE and an unknown size. The two seventeens share a numeral. They are not the same gap, and the numeral is not a force.",
    "Sunday's notice was seventeen minutes after Sunday's opening. That seventeen is the size of a miss: the warning came after the act. Monday's seventeen minutes runs from 10:05, when the open door was noticed, to 10:22, when the reading finished. That seventeen is how long the office stood there. The opening had already happened, and the sheet had already arrived before it. The voice's lateness against the opening has the sign LATE and an unknown size. The two seventeens share a numeral. They are not the same gap, and the numeral is not a force.",
)

add(
    "Ordinary order tells you the sheet is late for the opening and early for boarding. It does not tell you who printed it.",
    "Ordinary order tells you the sheet arrived before the door, the voice came after the door, and the front of the sheet is still early for boarding. It does not tell you who printed the sheet.",
)

add(
    "Write the earlier act first, and if you do not have its time, write that the time is unknown and earlier than the noticing. Admit you are late for it. Write the later act second.",
    "Write the earlier act first, and if you do not have its time, write that the time is unknown and earlier than the noticing. Admit the voice is late for the opening, and that the sheet is not. Write the later act second.",
)

add(
    "Quick test: Say the close without looking up. Door already open before 10:05. Reading at 10:22, late, size unknown. Sunday's notice, 18:17 after an 18:00 opening, a different seventeen. Boarding refused before it happened. The record at 16:41 is the refusal. Sophie had no act. The name comes off. The morning sheet's sender does not.",
    "Quick test: Say the close without looking up. Sheet, then the door, both before 10:05. Voice after the door, late, size unknown. Reading at 10:22 is how long they read. Sunday's notice, 18:17 after an 18:00 opening, a different seventeen, and the previous warning the back of the sheet meant. Boarding refused before it happened. The record at 16:41 is the refusal. Sophie had no act. The name comes off. The morning sheet's sender does not.",
)

add(
    "The door was late. The refusal was on time.",
    "The voice was late. The sheet was earlier than the door. The refusal was on time.",
)

for a, b in pairs:
    t = t.replace(a, b, 1)

if "\r\n" in t:
    raise SystemExit("CRLF appeared")

p.write_text(t, encoding="utf-8", newline="\n")
print("ok", len(pairs))
