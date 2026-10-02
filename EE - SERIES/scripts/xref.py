# -*- coding: utf-8 -*-
"""Nine-to-seven renumbering of cross-book references (2026-10-01).
old -> new: 1,2,3 same; 4 -> 4 (Part I); 6 -> 4 (Part II, chapters +19);
5 -> 5; 8 -> 6; 9 -> 7 (Part I, chapter 21 -> 29); 7 -> 7 (Part II, chapters +20).
xref(text, src_old, internal=True) rewrites 'Book N', 'Books N and M', "Book N's Chapter K",
and, for text from old 6 / old 7 / old 9, the book's own chapter numbers.
NOT idempotent: run it once, on nine-book text only. Everything under chapters/ is already converted."""
import re
MAP = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 4, 7: 7, 8: 6, 9: 7}
PART = {4: "Part I", 6: "Part II", 9: "Part I", 7: "Part II"}
def chmap(old, n):
    if old == 6: return n + 19
    if old == 7: return n + 20
    if old == 9 and n == 21: return 29
    return n
SEP = r"(?:, and |, | and | or | to |–)"
NUMS = rf"\d+(?:{SEP}\d+)*"
BOOKRE = re.compile(rf"\b(Books?) ((?:\d)(?:{SEP}\d)*)('s)?((?:,? | of )(?:Chapters?|Worked Example|Example|Section) (?:{NUMS})(?:\.\d+)?)?")
CHRE = re.compile(rf"\b(Chapters?|Worked Example|Example|Section|Figure|§) ?({NUMS})(\.\d+)?")
def _maplist(s, f):
    return re.sub(r"\d+", lambda m: str(f(int(m.group()))), s)
def _join(nums):
    nums = sorted(dict.fromkeys(nums))
    if len(nums) == 1: return "Book %d" % nums[0]
    if len(nums) == 2: return "Books %d and %d" % tuple(nums)
    return "Books " + ", ".join(map(str, nums[:-1])) + ", and %d" % nums[-1]
def xref(text, src_old, internal=True):
    toks = []
    src_new = MAP[src_old]
    def book(m):
        olds = [int(x) for x in re.findall(r"\d", m.group(2))]
        poss, chap = m.group(3) or "", m.group(4) or ""
        rng = re.search(r" to |–", m.group(2))
        if rng and len(olds) == 2:   # "Books 4 to 9": expand
            olds = list(range(olds[0], olds[1] + 1))
        tgt = olds[0]
        if chap and len(olds) == 1:
            chap = re.sub(r"(Chapters?|Worked Example|Example|Section) (" + NUMS + ")",
                          lambda c: c.group(1) + " " + _maplist(c.group(2), lambda n: chmap(tgt, n)), chap)
        news = [MAP[o] for o in olds]
        cross_self = [o for o in olds if MAP[o] == src_new and o != src_old]
        if len(olds) == 1 and cross_self:
            if chap:
                out = chap.lstrip(", ").replace("of ", "", 1).strip()
            else:
                out = PART[olds[0]] + poss
        else:
            keep = [n for o, n in zip(olds, news) if not (MAP[o] == src_new and o != src_old)] or news
            out = _join(keep) + poss + chap
        toks.append(out)
        return "\x01%d\x02" % (len(toks) - 1)
    t = BOOKRE.sub(book, text)
    if internal and src_old in (6, 7, 9):
        t = CHRE.sub(lambda m: m.group(1) + (" " if m.group(1) != "§" else "") + _maplist(m.group(2), lambda n: chmap(src_old, n)) + (m.group(3) or ""), t)
        t = re.sub(r"(?m)^(H2: )(\d+)\.", lambda m: m.group(1) + str(chmap(src_old, int(m.group(2)))) + ".", t)
    return re.sub("\x01(\\d+)\x02", lambda m: toks[int(m.group(1))], t)
if __name__ == "__main__":
    tests = [("Transmitter power is Book 6's and limits are Book 7's.", 4),
             ("By Book 6's cascade, see Book 6's Chapter 11 and Book 6's Example 11.1.", 4),
             ("A directional coupler, Book 4's Chapter 9, and Chapter 4 here; Chapters 9 to 17.", 6),
             ("Books 4 and 6 and Books 6 and 8, Books 9 and 8, Books 5 and 6, Book 8.", 9),
             ("the robot of Chapter 21; Chapters 17 to 20; Worked Example 21.2", 9),
             ("Book 6's Chapter 14 and Book 9's", 7), ("Book 7's Chapter 3", 5)]
    for s, b in tests: print(b, "|", xref(s, b))
