import os, re
root = os.path.dirname(os.path.abspath(__file__))
for fname in ("01_Part_One_Shape.md", "02_Part_Two_Molecule.md"):
    path = os.path.join(root, fname)
    text = open(path, encoding="utf-8").read()
    parts = re.split(r"(?=^## \d+\.)", text, flags=re.M)
    out = []
    for p in parts:
        if not re.match(r"## \d+\.", p):
            out.append(p)
            continue
        lines = p.splitlines()
        # find figure line index
        fig_i = None
        for i, l in enumerate(lines):
            if l.startswith("![Figure"):
                fig_i = i
                break
        if fig_i is None:
            out.append(p if p.endswith("\n") else p + "\n")
            continue
        last = max(i for i, l in enumerate(lines) if l.strip() and not l.startswith("![Figure") and not l.startswith("#"))
        if fig_i < last:
            out.append(p if p.endswith("\n") else p + "\n")
            continue
        fig = lines[fig_i]
        body_lines = [l for i, l in enumerate(lines) if i != fig_i]
        # drop trailing blanks then we'll rejoin
        while body_lines and not body_lines[-1].strip():
            body_lines.pop()
        # insert after first ---
        inserted = False
        new_lines = []
        for l in body_lines:
            new_lines.append(l)
            if not inserted and l.strip() == "---":
                new_lines.append("")
                new_lines.append(fig)
                inserted = True
        if not inserted:
            print("NO BREAK", fname, lines[0][:40])
            out.append(p if p.endswith("\n") else p + "\n")
            continue
        new_lines.append("")
        print("moved", lines[0][:50])
        out.append("\n".join(new_lines) + "\n")
    open(path, "w", encoding="utf-8", newline="\n").write("".join(out))
