# -*- coding: utf-8 -*-
"""Audit Physics appendix Lectures 1-18 for Feynman-class teaching quality."""
from docx import Document
from pathlib import Path
import re
import json

DOC = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1.docx")
OUT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\_audit_10of10_appendix.txt")
EXTRACT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_appendix_extract.txt")

doc = Document(str(DOC))
paras = [(i, p.text) for i, p in enumerate(doc.paragraphs)]

# Appendix body starts at second "Appendix: Lectures..."
app_idx = [i for i, t in paras if "Appendix: Lectures on What the Universe" in t]
assert len(app_idx) >= 2, app_idx
APP_START = app_idx[1]  # 2167

# Lecture headers
lecture_re = re.compile(r"^Lecture\s+(\d+)\s*[—\-–]\s*(.+)$")
lecture_starts = []
for i, t in paras:
    if i < APP_START:
        continue
    m = lecture_re.match(t.strip())
    if m:
        lecture_starts.append((i, int(m.group(1)), m.group(2).strip(), t.strip()))

# End: after last lecture content — look for non-lecture end markers
END = len(paras)
for i, t in paras:
    if i <= lecture_starts[-1][0]:
        continue
    s = t.strip()
    if s.startswith("About the Author") or s.startswith("Acknowledgements") or s.startswith("Acknowledgments"):
        END = i
        break
    if s.startswith("Glossary") and i > lecture_starts[-1][0] + 5:
        END = i
        break

# Build lecture slices (include until next lecture or END)
slices = []
for idx, (start, num, title, full) in enumerate(lecture_starts):
    stop = lecture_starts[idx + 1][0] if idx + 1 < len(lecture_starts) else END
    body = [(j, txt) for j, txt in paras if start <= j < stop]
    slices.append({"start": start, "stop": stop, "num": num, "title": title, "full_header": full, "paras": body})

# Also dump full appendix extract for human review
with EXTRACT.open("w", encoding="utf-8") as f:
    for i, t in paras:
        if APP_START <= i < END:
            f.write(f"{i}|{t}\n")

# Section label patterns
SECTION_LABELS = [
    "Picture",
    "Start here",
    "Where the popular version goes wrong",
    "Where popular version goes wrong",
    "Going deeper",
    "You need first",
    "After this lecture",
    "Stop. Before you go on",
    "Hot chair",
    "Check yourself",
    "Objective:",
    "Lesson ",
    "Module",
]

# Dry / Ministry-notes heuristics (phrase patterns that smell like notes not class)
DRY_PATTERNS = [
    (r"\bIt is important to note\b", "stock academic"),
    (r"\bAs previously mentioned\b", "stock academic"),
    (r"\bIn conclusion\b", "stock academic"),
    (r"\bFurthermore\b", "stock academic"),
    (r"\bMoreover\b", "stock academic"),
    (r"\bOne can see that\b", "stock academic"),
    (r"\bIt follows that\b", "stock academic"),
    (r"\brespectively\b", "textbook dry"),
    (r"\bthe aforementioned\b", "bureaucratic"),
    (r"\bin accordance with\b", "Ministry tone (maybe intentional)"),
    (r"\bshall be\b", "Ministry tone"),
    (r"\bhereby\b", "Ministry tone"),
    (r"\bPursuant\b", "Ministry tone"),
    (r"\bObjective:\b", "leftover scaffolding"),
    (r"\bCheck yourself\b", "leftover scaffolding"),
    (r"\bLearning objective\b", "leftover scaffolding"),
    (r"\bIn this lecture we will\b", "courseware bland"),
    (r"\bThis lecture covers\b", "courseware bland"),
    (r"\bStudents should\b", "courseware bland"),
    (r"\bThe key takeaway is\b", "courseware bland"),
    (r"\bTo summarize\b", "courseware bland"),
    (r"\bSimply put,?\b", "hand-wavy hedge"),
    (r"\bin a sense\b", "hand-wavy hedge"),
    (r"\bsomehow\b", "hand-wavy hedge"),
    (r"\bessentially just\b", "hand-wavy hedge"),
    (r"\bit turns out that\b", "mild hedge — OK if followed by picture"),
    (r"\bPhysics Notes\b", "dual naming pointer"),
    (r"\bLesson\s+\d+\b", "Lesson leftover"),
]

# Scaffolding lines we should NOT score as body prose
SCAFFOLD_STARTS = (
    "Lecture ",
    "You need first",
    "After this lecture",
    "Stop. Before you go on",
    "Picture",
    "Start here",
    "Where the popular",
    "Where popular",
    "Going deeper",
    "Hot chair",
    "Module",
    "Objective:",
    "Check yourself",
    "Lesson ",
)

def is_scaffold(t: str) -> bool:
    s = t.strip()
    if not s:
        return True
    for pref in SCAFFOLD_STARTS:
        if s.startswith(pref) or s == pref.rstrip(":"):
            return True
    # short label-only lines
    if s in {"Picture", "Start here", "Going deeper", "Hot chair check", "Hot chair"}:
        return True
    if re.match(r"^Where (the )?popular version goes wrong\.?$", s):
        return True
    return False

def classify_body(text: str) -> dict:
    """Heuristic flags for Feynman vs dry notes."""
    flags = []
    # Concrete picture signals
    picture_words = len(re.findall(
        r"\b(imagine|picture|suppose|say you|think of|like a|like an|for example|e\.g\.|say a|walk into|sit|chair|coin|door|room|cat|spin|pointer|meter|clock|box)\b",
        text, re.I))
    # Honesty / admission signals
    honesty = len(re.findall(
        r"\b(we don'?t know|nobody knows|honestly|the truth is|what actually|what we mean|I mean|here'?s the thing|the catch|the trap|don'?t pretend|not magic|not mystical)\b",
        text, re.I))
    # Second person / classroom voice
    you_voice = len(re.findall(r"\b(you|your|we|let'?s)\b", text, re.I))
    # Dry noun-stack / definitional
    definitional = len(re.findall(
        r"\b(is defined as|refers to|is the process by which|consists of|is characterized by|denotes)\b",
        text, re.I))
    # Passive bureaucratic
    passive_heavy = len(re.findall(r"\b(is performed|is obtained|is measured|is described|is given by|are required|must be)\b", text, re.I))
    # Formula dump without words
    formulaish = len(re.findall(r"[=≤≥≪≫⟨⟩|ψΨħ]|\\frac|delta\s*x|sigma_", text))

    for pat, label in DRY_PATTERNS:
        if re.search(pat, text, re.I):
            flags.append(label)

    score_hint = 5
    # boosts
    if picture_words >= 2:
        score_hint += 1
    if honesty >= 1:
        score_hint += 1
    if you_voice >= 3 and len(text) > 80:
        score_hint += 1
    # penalties
    if definitional >= 1:
        score_hint -= 1
        flags.append("definitional phrasing")
    if passive_heavy >= 2:
        score_hint -= 1
        flags.append("passive/procedural")
    if formulaish >= 3 and picture_words == 0:
        score_hint -= 1
        flags.append("formula without picture")
    if "stock academic" in flags or "courseware bland" in flags:
        score_hint -= 2
    if "leftover scaffolding" in flags:
        score_hint -= 2
    if len(text) > 400 and picture_words == 0 and you_voice < 2:
        score_hint -= 1
        flags.append("long dry block")
    if re.search(r"\b(Ministry|Form|stamp|filing|paperwork|Lolly|notebook)\b", text):
        flags.append("novel/Ministry flavor present")
        score_hint += 0.5

    return {
        "picture_words": picture_words,
        "honesty": honesty,
        "you_voice": you_voice,
        "definitional": definitional,
        "passive_heavy": passive_heavy,
        "flags": flags,
        "score_hint": max(1, min(10, score_hint)),
    }

# Global inconsistency scan across whole appendix
global_flags = {
    "Lesson leftovers": [],
    "Objective leftovers": [],
    "Check yourself leftovers": [],
    "Doubled Contents": [],
    "Physics Notes pointers": [],
    "Lecture vs Lesson mix": [],
    "Inconsistent section labels": [],
}

# Scan TOC area and appendix for doubled contents
for i, t in paras:
    s = t.strip()
    if i < APP_START and "Appendix: Lectures" in s:
        # early TOC entry OK
        pass
    if "Contents" in s and APP_START <= i < END:
        global_flags["Doubled Contents"].append((i, s[:120]))
    if re.search(r"\bLesson\s+\d+", s) and i >= APP_START:
        global_flags["Lesson leftovers"].append((i, s[:120]))
    if re.search(r"\bObjective:", s, re.I) and i >= APP_START:
        global_flags["Objective leftovers"].append((i, s[:120]))
    if re.search(r"\bCheck yourself\b", s, re.I) and i >= APP_START:
        global_flags["Check yourself leftovers"].append((i, s[:120]))
    if re.search(r"\bPhysics Notes\b", s) and i >= APP_START:
        global_flags["Physics Notes pointers"].append((i, s[:120]))
    # Inconsistent labels: "Lesson" as section vs Lecture
    if s.startswith("Lesson ") and i >= APP_START:
        global_flags["Lecture vs Lesson mix"].append((i, s[:120]))

# Expected section labels (canonical)
CANONICAL = {
    "picture": "Picture",
    "start here": "Start here",
    "where popular": "Where the popular version goes wrong",
    "going deeper": "Going deeper",
}

section_variants = []
for i, t in paras:
    if i < APP_START or i >= END:
        continue
    s = t.strip()
    low = s.lower()
    if low.startswith("where popular version") and "the popular" not in low:
        section_variants.append((i, s, "missing 'the'"))
    if low.startswith("where the popular") and "goes wrong" not in low:
        section_variants.append((i, s, "truncated popular-wrong label"))
    if low in ("start here:", "start here."):
        section_variants.append((i, s, "punctuation variant"))
    if low.startswith("going deep") and low != "going deeper":
        section_variants.append((i, s, "Going deeper variant"))
    if low.startswith("the picture") or low == "a picture":
        section_variants.append((i, s, "Picture label variant"))
    if re.match(r"^module\s*\d*", low) or low.startswith("module:"):
        section_variants.append((i, s, "Module label"))

global_flags["Inconsistent section labels"] = section_variants

# Per-lecture analysis
results = []
rewrite_candidates = []  # (priority, lecture_num, para_idx, first100, reason, current_score_hint)

for lec in slices:
    body_paras = []
    sections_present = {
        "Picture": False,
        "Start here": False,
        "Where popular version goes wrong": False,
        "Going deeper": False,
        "You need first": False,
        "After this lecture": False,
        "Stop. Before you go on": False,
        "Hot chair": False,
    }
    scaffold_bits = []
    body_bits = []
    weak = []

    for j, txt in lec["paras"]:
        s = txt.strip()
        if not s:
            continue
        low = s.lower()
        if low.startswith("picture") and len(s) < 40:
            sections_present["Picture"] = True
            scaffold_bits.append((j, s))
            continue
        if low.startswith("start here"):
            sections_present["Start here"] = True
            scaffold_bits.append((j, s))
            continue
        if "popular version goes wrong" in low:
            sections_present["Where popular version goes wrong"] = True
            scaffold_bits.append((j, s))
            continue
        if low.startswith("going deeper"):
            sections_present["Going deeper"] = True
            scaffold_bits.append((j, s))
            continue
        if low.startswith("you need first"):
            sections_present["You need first"] = True
            scaffold_bits.append((j, s))
            continue
        if low.startswith("after this lecture"):
            sections_present["After this lecture"] = True
            scaffold_bits.append((j, s))
            continue
        if low.startswith("stop. before you go on"):
            sections_present["Stop. Before you go on"] = True
            scaffold_bits.append((j, s))
            continue
        if low.startswith("hot chair"):
            sections_present["Hot chair"] = True
            scaffold_bits.append((j, s))
            continue
        if is_scaffold(s) and j == lec["start"]:
            scaffold_bits.append((j, s))
            continue

        # body
        cls = classify_body(s)
        body_bits.append((j, s, cls))
        # Weak if low score_hint or long dry
        is_weak = False
        reasons = []
        if cls["score_hint"] <= 5:
            is_weak = True
            reasons.append(f"score_hint={cls['score_hint']}")
        if "long dry block" in cls["flags"]:
            is_weak = True
            reasons.append("long dry block")
        if "definitional phrasing" in cls["flags"] and cls["picture_words"] == 0:
            is_weak = True
            reasons.append("definitional, no picture")
        if "passive/procedural" in cls["flags"] and cls["you_voice"] < 2:
            is_weak = True
            reasons.append("passive procedural")
        if "stock academic" in cls["flags"] or "courseware bland" in cls["flags"]:
            is_weak = True
            reasons.append("academic/courseware tone")
        if "leftover scaffolding" in cls["flags"]:
            is_weak = True
            reasons.append("leftover scaffolding")
        # Short bullet-like Ministry notes: many sentences start with capital noun, no you/we
        if len(s) > 150 and cls["you_voice"] == 0 and cls["picture_words"] == 0:
            is_weak = True
            reasons.append("no classroom voice / no picture")
        # Enumerated note style
        if re.match(r"^(\d+[\).\]]|[A-Z]\.|[-•])\s", s) and len(s) > 80:
            # could be fine; check dryness
            if cls["picture_words"] == 0:
                is_weak = True
                reasons.append("list/note style")

        if is_weak and len(s) > 60:  # skip tiny glue
            weak.append({
                "idx": j,
                "first100": s[:100],
                "len": len(s),
                "reasons": reasons,
                "flags": cls["flags"],
                "score_hint": cls["score_hint"],
            })
            # priority: lower score = higher priority; longer dry = higher
            pri = (6 - cls["score_hint"]) * 10 + min(len(s) // 50, 10)
            if "leftover scaffolding" in cls["flags"]:
                pri += 20
            if "no classroom voice / no picture" in reasons:
                pri += 8
            rewrite_candidates.append({
                "priority": pri,
                "lecture": lec["num"],
                "title": lec["title"],
                "idx": j,
                "first100": s[:100],
                "reasons": reasons,
                "flags": cls["flags"],
                "full_len": len(s),
            })

    # Overall lecture score: average body score_hint with section completeness
    if body_bits:
        avg = sum(b[2]["score_hint"] for b in body_bits) / len(body_bits)
    else:
        avg = 3.0
    # section completeness bonus
    must = ["Picture", "Start here", "Where popular version goes wrong", "Going deeper"]
    present_must = sum(1 for k in must if sections_present[k])
    if present_must == 4:
        avg += 0.5
    elif present_must <= 2:
        avg -= 0.8
    # hot chair / stop present
    if sections_present["Stop. Before you go on"]:
        avg += 0.2
    if sections_present["Hot chair"]:
        avg += 0.2
    # weak density penalty
    if body_bits:
        weak_ratio = len(weak) / max(1, len(body_bits))
        avg -= weak_ratio * 1.5

    score = max(1, min(10, round(avg * 2) / 2))  # half points

    # Human-readable voice judgment
    novel_flavor = sum(1 for _, _, c in body_bits if "novel/Ministry flavor present" in c["flags"])
    dry_count = sum(1 for w in weak if "no classroom voice" in " ".join(w["reasons"]) or "long dry" in " ".join(w["reasons"]))
    if score >= 8.5 and dry_count == 0:
        voice = "Feynman-leaning — concrete, conversational"
    elif score >= 7:
        voice = "Mostly classroom voice; some Ministry-note patches"
    elif score >= 5.5:
        voice = "Mixed — scaffolding strong, body still often dry notes"
    else:
        voice = "Dry Ministry / textbook notes dominate body prose"

    results.append({
        "num": lec["num"],
        "title": lec["title"],
        "start": lec["start"],
        "stop": lec["stop"],
        "sections": sections_present,
        "n_body": len(body_bits),
        "n_weak": len(weak),
        "score": score,
        "voice": voice,
        "novel_flavor_paras": novel_flavor,
        "weak": weak,
        "body_preview": [(j, s[:160], c["score_hint"], c["flags"]) for j, s, c in body_bits[:8]],
        "all_body_idx": [(j, s[:80]) for j, s, _ in body_bits],
    })

# Sort rewrite candidates
rewrite_candidates.sort(key=lambda x: (-x["priority"], x["lecture"], x["idx"]))
# Dedupe by idx, keep top 30
seen = set()
top30 = []
for c in rewrite_candidates:
    if c["idx"] in seen:
        continue
    seen.add(c["idx"])
    top30.append(c)
    if len(top30) >= 30:
        break

# Manual deep-read: dump each lecture's body paragraphs fully into structured report
# Also scan for specific quality issues a human would catch

def deep_notes(lec_result, body_bits_full):
    notes = []
    # missing sections
    sec = lec_result["sections"]
    for k in ["Picture", "Start here", "Where popular version goes wrong", "Going deeper"]:
        if not sec[k]:
            notes.append(f"MISSING section label: {k}")
    # very short lecture body
    if lec_result["n_body"] < 4:
        notes.append("Very thin body — may be over-scaffolded / under-taught")
    # check first body para for hook
    if body_bits_full:
        first = body_bits_full[0][1]
        if re.match(r"^(A |An |The )?[A-Z][a-z]+ is (a |an |the )?", first) and "you" not in first.lower()[:80]:
            notes.append("Opens with definitional textbook sentence rather than a picture")
    return notes

# Rebuild body_bits map
body_map = {}
for lec in slices:
    bits = []
    for j, txt in lec["paras"]:
        s = txt.strip()
        if not s or is_scaffold(s) and not (s.startswith("Picture") and len(s) > 80):
            # Picture can be label-only OR "Picture: ..."
            if s.startswith("Picture") and len(s) > 40:
                bits.append((j, s, classify_body(s)))
            continue
        if j == lec["start"]:
            continue
        low = s.lower()
        if any(low.startswith(x) for x in [
            "you need first", "after this lecture", "stop. before you go on",
            "picture", "start here", "where the popular", "where popular",
            "going deeper", "hot chair", "module", "objective:", "check yourself"
        ]) and len(s) < 120:
            continue
        # longer lines that start with labels but include content
        bits.append((j, s, classify_body(s)))
    body_map[lec["num"]] = bits

for r in results:
    r["deep"] = deep_notes(r, body_map.get(r["num"], []))

# Write report
lines = []
W = lines.append

W("=" * 78)
W("SCHRÖDINGER'S PAPERWORK — PHYSICS APPENDIX 10/10 AUDIT")
W("Target: Feynman-class teaching (intuition, honesty, concrete picture, no hand-waving)")
W("File: Schrodingers_Paperwork_BOOK_1.docx")
W(f"Appendix start paragraph: {APP_START}")
W(f"Lectures found: {len(slices)} (headers at {[s['start'] for s in slices]})")
W(f"Appendix content end (exclusive): {END}")
W("=" * 78)
W("")
W("METHOD")
W("-" * 40)
W("Extracted Lectures 1–18 with python-docx. Scaffolding already marked done was")
W("noted but not scored as body. Body prose scored for: concrete picture language,")
W("classroom you/we voice, honesty about limits, vs definitional/passive/Ministry-")
W("note dryness and leftover courseware labels. Scores are editorial judgments")
W("aided by heuristics — treat as triage, not gospel.")
W("")
W("=" * 78)
W("GLOBAL FLAGS")
W("=" * 78)

for key, items in global_flags.items():
    W("")
    W(f"### {key} ({len(items)})")
    if not items:
        W("  (none found)")
    else:
        for item in items[:40]:
            if len(item) == 2:
                i, s = item
                W(f"  [{i}] {s}")
            else:
                i, s, note = item
                W(f"  [{i}] ({note}) {s}")
        if len(items) > 40:
            W(f"  ... and {len(items)-40} more")

W("")
W("NOTE on 'Physics Notes' pointers: If chapter text still says 'see Physics Notes'")
W("while the appendix is branded as Lectures, that dual naming may be intentional")
W("(Ministry filing name vs classroom name). Flagged for author decision, not auto-fix.")
W("")

W("=" * 78)
W("PER-LECTURE SCORECARD")
W("=" * 78)

for r in results:
    W("")
    W("-" * 78)
    W(f"LECTURE {r['num']} — {r['title']}")
    W(f"Paragraphs: {r['start']}–{r['stop']-1} | Body paras: {r['n_body']} | Weak flagged: {r['n_weak']}")
    W(f"RANK: {r['score']}/10")
    W(f"Voice: {r['voice']}")
    W(f"Novel/Ministry flavor paragraphs: {r['novel_flavor_paras']}")
    W("Sections present:")
    for k, v in r["sections"].items():
        W(f"  [{'x' if v else ' '}] {k}")
    if r["deep"]:
        W("Deep notes:")
        for n in r["deep"]:
            W(f"  - {n}")
    W("Weak paragraphs (idx | first 100 chars | reasons):")
    if not r["weak"]:
        W("  (none flagged — still spot-check Going deeper for hand-waving)")
    else:
        for w in r["weak"]:
            W(f"  [{w['idx']}] ({w['len']} chars, hint={w['score_hint']}) {w['first100']}")
            W(f"       reasons: {', '.join(w['reasons'])}")
            if w["flags"]:
                W(f"       flags: {', '.join(w['flags'])}")
    W("Body preview (first ~8 body paras):")
    for j, prev, sh, flags in r["body_preview"]:
        W(f"  [{j}] (hint={sh}) {prev}")

W("")
W("=" * 78)
W("PRIORITIZED REWRITE LIST (MAX 30)")
W("Each item: one specific paragraph to rewrite into Feynman-class body prose.")
W("Keep: accurate physics, chapter/Ministry cross-refs, Lolly notebook flavor where frame fits.")
W("Goal: feel like sitting in a brilliant class — picture first, then honesty, then precision.")
W("=" * 78)
W("")

for n, c in enumerate(top30, 1):
    W(f"{n}. L{c['lecture']} [{c['idx']}] priority={c['priority']} — {c['title']}")
    W(f"   Text: {c['first100']}…")
    W(f"   Why: {', '.join(c['reasons'])}")
    if c["flags"]:
        W(f"   Flags: {', '.join(dict.fromkeys(c['flags']))}")
    # Suggested rewrite angle
    angle = "Open with a concrete picture; say what the universe is doing in plain words; then the precise claim; one Ministry/chapter wink if natural."
    if "leftover scaffolding" in c["flags"]:
        angle = "Remove/replace leftover Objective/Check-yourself courseware; fold into Hot chair or Stop. Before you go on."
    elif "definitional" in " ".join(c["flags"]) or "definitional" in " ".join(c["reasons"]):
        angle = "Kill 'X is defined as…'. Start with what you'd see or do; name the term after the picture lands."
    elif "passive" in " ".join(c["reasons"]) or "passive" in " ".join(c["flags"]):
        angle = "Swap passive procedure for a walkthrough: you prepare, you measure, nature answers — what changed?"
    elif "no classroom voice" in " ".join(c["reasons"]):
        angle = "Restore lecture voice (you/we/let's). One vivid example beats three abstract nouns."
    W(f"   Rewrite angle: {angle}")
    W("")

W("=" * 78)
W("SUMMARY TABLE")
W("=" * 78)
W(f"{'L':>3} {'Score':>6} {'Weak':>5} {'Body':>5}  Title / Voice")
for r in results:
    W(f"{r['num']:>3} {r['score']:>6} {r['n_weak']:>5} {r['n_body']:>5}  {r['title'][:40]}")
    W(f"         {r['voice']}")

avg_all = sum(r["score"] for r in results) / len(results)
W("")
W(f"Average lecture score: {avg_all:.2f}/10")
W(f"Lectures below 7: {[r['num'] for r in results if r['score'] < 7]}")
W(f"Lectures at/above 8.5: {[r['num'] for r in results if r['score'] >= 8.5]}")
W("")
W("TOP PRIORITY LECTURES TO REWRITE FIRST (by weak density + score):")
ranked = sorted(results, key=lambda r: (r["score"], -r["n_weak"]))
for r in ranked[:8]:
    W(f"  L{r['num']} ({r['score']}/10, {r['n_weak']} weak) — {r['title']}")

W("")
W("=" * 78)
W("EDITORIAL VERDICT")
W("=" * 78)
W("Scaffolding (course frame, Feynman intro, how to sit, lecture headers, You need")
W("first / After this / Stop+hot chair / modules / hot-chair checks) is already in")
W("place. The remaining gap to 10/10 is almost entirely BODY PROSE: several lectures")
W("still read as competent Ministry physics notes — accurate, compressed, low picture.")
W("Elevate by rewriting the prioritized paragraphs: picture → honesty → precision,")
W("without undoing the classroom frame already built.")
W("")
W(f"Full paragraph dump for spot-check: {EXTRACT}")
W("=" * 78)

# Also attach FULL body text per lecture for the auditor (human) at end — condensed
W("")
W("=" * 78)
W("FULL BODY DUMP BY LECTURE (for rewrite targeting)")
W("=" * 78)
for lec in slices:
    W("")
    W(f"##### LECTURE {lec['num']} — {lec['title']} (paras {lec['start']}-{lec['stop']-1})")
    for j, txt in lec["paras"]:
        s = txt.strip()
        if not s:
            continue
        W(f"[{j}] {s}")

report = "\n".join(lines) + "\n"
OUT.write_text(report, encoding="utf-8")

# Also write a machine-readable top30 json for follow-up
meta = {
    "avg_score": avg_all,
    "scores": {r["num"]: r["score"] for r in results},
    "top30": top30,
    "global_flag_counts": {k: len(v) for k, v in global_flags.items()},
}
Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\_audit_10of10_appendix_meta.json").write_text(
    json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
)

print(f"Wrote {OUT}")
print(f"Wrote {EXTRACT}")
print(f"Avg score: {avg_all:.2f}")
print(f"Top30 count: {len(top30)}")
print("Scores:", {r['num']: r['score'] for r in results})
print("Global:", {k: len(v) for k, v in global_flags.items()})
