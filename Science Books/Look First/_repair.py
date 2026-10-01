# -*- coding: utf-8 -*-
"""Restore capital-Where sentences. Keep lowercase definition lines as real sentences."""
import os
import re
import subprocess

REPO = r"C:\Users\lomus\OneDrive\My Books for Amazon"
REL = "Science Books/Look First/A Trip Is Not a New Life - Manuscript"
MAN = os.path.join(REPO, "Science Books", "Look First", "A Trip Is Not a New Life - Manuscript")


def git_text(name):
    p = subprocess.run(
        ["git", "show", f"HEAD:{REL}/{name}"],
        cwd=REPO,
        capture_output=True,
    )
    if p.returncode != 0:
        raise SystemExit(p.stderr.decode("utf-8", "replace"))
    return p.stdout.decode("utf-8")


def bad_body(body):
    if body.startswith("t is "):
        sent = "In that line, " + body
    else:
        body = re.sub(r"[“\"]([^”\"]+)[”\"]", r"\1", body)
        if re.match(r"^\d", body):
            sent = "The sum " + body
        elif body[:1].islower():
            sent = body[0].upper() + body[1:]
        else:
            sent = body
    if sent and sent[-1] not in ".!?":
        sent += "."
    return sent


def safer_body(body):
    if body.startswith("t is "):
        sent = "In that line, " + body
    else:
        m = re.match(r"^[“\"]([A-Za-z][^”\"]*)[”\"]", body)
        if m:
            word = m.group(1)
            if word[:1].islower():
                word = word[0].upper() + word[1:]
            body = word + body[m.end():]
        if re.match(r"^\d", body):
            sent = "The sum " + body
        elif body[:1].islower():
            sent = body[0].upper() + body[1:]
        else:
            sent = body
    if sent and sent[-1] not in ".!?":
        sent += "."
    return sent


def cut_after(text, start, end, label):
    i = text.find(start)
    if i < 0:
        print("MISS", label, "start")
        return text
    j = text.find(end, i)
    if j < 0:
        print("MISS", label, "end")
        return text
    j = j + len(end)
    while text[j:j + 1] == "\n":
        j += 1
        if text[j - 2:j] == "\n\n":
            break
    print("CUT", label, j - i)
    return text[:i] + text[j:]


def main():
    restored = 0
    refined = 0
    missing = 0
    for fn in sorted(os.listdir(MAN)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(MAN, fn)
        with open(path, encoding="utf-8") as f:
            working = f.read()
        try:
            original = git_text(fn)
        except SystemExit as e:
            print("no head", fn, e)
            continue
        repl = {}
        for line in original.splitlines():
            s = line.strip()
            low = s.lower()
            if not low.startswith("where "):
                continue
            body = s[6:].strip()
            bad = bad_body(body)
            if s.startswith("Where "):
                repl[bad] = s
            else:
                repl[bad] = safer_body(body)
        lines = working.splitlines()
        out = []
        for line in lines:
            s = line.strip()
            if s in repl and repl[s] != s:
                if repl[s].startswith("Where "):
                    restored += 1
                else:
                    refined += 1
                out.append(repl[s])
            else:
                out.append(line)
        # report where-lines from HEAD we failed to match
        for bad, good in repl.items():
            if bad != good and bad not in working and good not in "\n".join(out):
                missing += 1
                print("UNMATCHED", fn, bad[:80])
        text = "\n".join(out) + ("\n" if working.endswith("\n") else "")
        if fn == "05_Part_Five_The_Classroom.md":
            text = cut_after(
                text,
                "Kindness has a shape on a chart.",
                "If the drink is gone, home is no longer a mood you can select.",
                "ch22",
            )
        if fn == "09_Part_Nine_Not_A_Straight_Line.md":
            old = "Founders photograph the middle. the napkin keeps the shoulders."
            new = "Founders photograph the middle. The napkin keeps the shoulders."
            if old in text:
                text = text.replace(old, new)
                print("fixed napkin")
        if text != working:
            tmp = path + ".tmp"
            with open(tmp, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
            os.replace(tmp, path)
            print("saved", fn)
    print("restored", restored, "refined", refined, "unmatched", missing)
    # leftover damage
    for fn in sorted(os.listdir(MAN)):
        if not fn.endswith(".md"):
            continue
        with open(os.path.join(MAN, fn), encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                s = line.strip()
                if s == "The popular version goes wrong." or s.startswith("Did it come from") or s.startswith("Does the money sit"):
                    print("STILL", fn, n, s[:80])


if __name__ == "__main__":
    main()
