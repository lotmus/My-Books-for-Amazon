"""Convert British spelling and words to American, in place, for the Step Stories files.
Usage: python us_spelling.py file [file ...]"""
import re, sys

PAIRS = [
    (r"\bboiled sweets\b", "hard candies"), (r"\bBoiled sweets\b", "Hard candies"),
    (r"\bthe last of a sweet\b", "the last of a candy"),
    (r"\bsweeties\b", "candies"), (r"\bSweeties\b", "Candies"),
    (r"\bsweets\b", "candy"), (r"\bSweets\b", "Candy"),
    (r"\b[Tt]en pounds\b", lambda m: m.group(0).replace("pounds", "dollars")),
    (r"\bcolour", "color"), (r"\bColour", "Color"),
    (r"\bneighbour", "neighbor"), (r"\bNeighbour", "Neighbor"),
    (r"\bgrey\b", "gray"), (r"\bGrey\b", "Gray"), (r"\bgreyer\b", "grayer"),
    (r"\bmemoris", "memoriz"), (r"\brealis", "realiz"), (r"\brecognis", "recogniz"),
    (r"\borganis", "organiz"), (r"\bapologis", "apologiz"),
    (r"\bcentre\b", "center"), (r"\btowards\b", "toward"), (r"\bafterwards\b", "afterward"),
    (r"\bmum\b", "mom"), (r"\bMum\b", "Mom"),
    (r"\bjersey\b", "sweater"), (r"\bplait\b", "braid"), (r"\bPlait\b", "Braid"),
    (r"\btea towel\b", "dish towel"), (r"\bbaking paper\b", "wax paper"),
    (r"\bjam jar\b", "jelly jar"), (r"\bbiscuit crumb\b", "cookie crumb"),
    (r"\blike a biscuit somebody\b", "like a cookie somebody"),
    (r"\b(Mr|Mrs|Dr)(?=\s[A-Z])", lambda m: m.group(1) + "."),
    (r"English \(British spelling\)", "English (American spelling)"),
    (r"\ben-GB\b", "en-US"),
]

for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    n = 0
    for pat, rep in PAIRS:
        s, k = re.subn(pat, rep, s)
        n += k
    open(path, "w", encoding="utf-8").write(s)
    print(path.split("\\")[-1], n, "changes")
