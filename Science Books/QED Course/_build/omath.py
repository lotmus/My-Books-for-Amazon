"""Turn the course's linear display-math dialect into Office Math (OMML).

The lesson sources write fractions with /, superscripts with ^ or ², subscripts
with _ or ₀, and a slashed momentum as a letter plus U+0338. This module builds
real stacked fractions, superscripts, and subscripts so a display equation is
not one long Unicode run.

Fixed 2026-10-01 (the renderer used to drop every round bracket and every space):
- Round brackets stay visible, as a stretchy Office Math delimiter, except where
  they only group: a fraction numerator or denominator, a script argument such
  as e^(iωt), or a lone fraction at the start of a term, e.g. (1/4)Σ.
  So (Zα)⁴, (ie)², Σ(p), ((p−k)²−m²) and f(x) render as written. Square
  brackets also use the stretchy delimiter.
- A space between two operands is kept. A known function name followed by an
  argument (sinh ωτ, det A, ln Λ, sin²(θ/2)) becomes an Office Math function
  object, which Word sets upright with its own spacing.
- f(x), δ⁴(p−k), ψ_n[q] and √(2mω) are one factor, so f(x)/g(y) and
  a/√(2mω) put the whole factor over or under the bar. A fraction takes the
  whole juxtaposed term on each side, so d⁴k/(2π)⁴ has d⁴k on top.
- A bare script is one index: γ^μγ^ν is γ^μ γ^ν and ∂_μφ is ∂_μ φ (formerly
  γ^(μγ)^ν). Runs of Greek indices (μν, ρσ) and Latin labels (int, eff,
  QED) stay whole. A derivative ∂ takes a one-letter index.
- " , " (comma with a space each side) is the sources' thin space, left over
  from LaTeX \\, ; it renders as a thin space. Commas between the bracketed
  rows of a matrix, [ [a, b] , [c, d] ], stay commas.
- ⁻¹ and ⁻²² are one superscript, Eₙ⁽⁰⁾ is a superscript (0), primes stay
  on their letter, and |k|² is a squared modulus.
"""
from lxml import etree

M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

SUP_CHARS = {
    "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
    "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
    "⁺": "+", "⁻": "−",
}
SUB_CHARS = {
    "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
    "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
}
SLASH = "\u0338"
PRIMES = "′″"
# Characters that are their own math run (operators and punctuation).
OPS = set("+=−–—×÷·⋅,;:<>≤≥≈∝→←±∓|′…⋯")
# Function names that Word sets upright with function-application spacing.
FUNCS = {
    "sin", "cos", "tan", "cot", "sec", "csc",
    "sinh", "cosh", "tanh", "coth", "sech", "csch",
    "arcsin", "arccos", "arctan",
    "log", "ln", "lg", "exp", "det", "tr", "Tr", "Re", "Im",
    "lim", "max", "min", "sup", "inf", "arg", "sgn", "erf", "dim", "ker",
}
SPACE = ("space",)
THIN = ("thin",)
NARY = {"Σ", "∑", "Π", "∏", "∫", "∬", "∭", "∮", "∫∫"}


def _m(parent, tag):
    return etree.SubElement(parent, "{%s}%s" % (M_NS, tag))


def _run(parent, text):
    if text is None or text == "":
        return
    r = _m(parent, "r")
    t = _m(r, "t")
    t.set(XML_SPACE, "preserve")
    t.text = text


def _append_tree(parent, node):
    kind = node[0]
    if kind == "run":
        _run(parent, node[1])
    elif kind == "seq":
        for child in node[1]:
            _append_tree(parent, child)
    elif kind == "frac":
        f = _m(parent, "f")
        num = _m(f, "num")
        den = _m(f, "den")
        _append_tree(num, node[1])
        _append_tree(den, node[2])
    elif kind == "sup":
        el = _m(parent, "sSup")
        base = _m(el, "e")
        exp = _m(el, "sup")
        _append_tree(base, node[1])
        _append_tree(exp, node[2])
    elif kind == "sub":
        el = _m(parent, "sSub")
        base = _m(el, "e")
        sub = _m(el, "sub")
        _append_tree(base, node[1])
        _append_tree(sub, node[2])
    elif kind == "subsup":
        el = _m(parent, "sSubSup")
        base = _m(el, "e")
        sub = _m(el, "sub")
        exp = _m(el, "sup")
        _append_tree(base, node[1])
        _append_tree(sub, node[2])
        _append_tree(exp, node[3])
    elif kind == "paren":
        # node = ("paren", inner, open, close); close is "" if unclosed
        if node[3]:
            d = _m(parent, "d")
            pr = _m(d, "dPr")
            if node[2] != "(":
                _m(pr, "begChr").set("{%s}val" % M_NS, node[2])
            if node[3] != ")":
                _m(pr, "endChr").set("{%s}val" % M_NS, node[3])
            e = _m(d, "e")
            _append_tree(e, node[1])
        else:
            _run(parent, node[2])
            _append_tree(parent, node[1])
    elif kind == "space":
        _run(parent, " ")
    elif kind == "thin":
        _run(parent, "\u2009")
    elif kind == "func":
        el = _m(parent, "func")
        fn = _m(el, "fName")
        _append_tree(fn, node[1])
        e = _m(el, "e")
        _append_tree(e, node[2])
    elif kind == "acc":
        el = _m(parent, "acc")
        pr = _m(el, "accPr")
        ch = _m(pr, "chr")
        ch.set("{%s}val" % M_NS, "/")
        e = _m(el, "e")
        _append_tree(e, node[1])
    else:
        raise ValueError(kind)


def _skip(s, i):
    while i < len(s) and s[i] == " ":
        i += 1
    return i


def _parse_group(s, i, close):
    node, i = _parse_sum(s, i, close)
    if i < len(s) and s[i] == close:
        i += 1
    return node, i


def _parse_delim(s, i, open_, close):
    """Parse a bracketed group starting after open_; keep it visible."""
    inner, j = _parse_sum(s, i, close)
    closed = j < len(s) and s[j] == close
    if closed:
        j += 1
    return ("paren", inner, open_, close if closed else ""), j


def _unwrap(node):
    """A round-bracket group used only for grouping: drop the brackets."""
    if node[0] == "paren" and node[2] == "(" and node[3]:
        return node[1]
    return node


def _is_op(node):
    if node[0] == "thin":
        return True
    return node[0] == "run" and len(node[1]) == 1 and (node[1] in OPS or node[1] in "+−")


def _func_name(node):
    """The bare name of a function node, e.g. sinh, sin² or log_10."""
    if node[0] == "run":
        return node[1]
    if node[0] in ("sup", "sub", "subsup") and node[1][0] == "run":
        return node[1][1]
    return None


def _abs_end(s, i):
    """|k|², |ψ(x, t)|²: index of the closing bar of a squared modulus."""
    if i >= len(s) or s[i] != "|":
        return -1
    k = s.find("|", i + 1)
    if k <= i + 1 or any(ch in "⟨⟩" for ch in s[i + 1:k]):
        return -1
    if k + 1 < len(s) and (s[k + 1] in SUP_CHARS or s[k + 1] in SUB_CHARS or s[k + 1] in "^_"):
        return k
    return -1


def _parse_atom(s, i):
    i = _skip(s, i)
    if i >= len(s):
        return ("run", ""), i
    c = s[i]
    if c == "|" and _abs_end(s, i) > 0:
        k = _abs_end(s, i)
        inner, _ = _parse_sum(s[:k], i + 1, "")
        return ("paren", inner, "|", "|"), k + 1
    if c == "(":
        return _parse_delim(s, i + 1, "(", ")")
    if c == "[":
        return _parse_delim(s, i + 1, "[", "]")
    if c in SUP_CHARS or c in SUB_CHARS or c in "^_/" or c == SLASH:
        return ("run", ""), i
    if c in OPS or c in "()[]{}":
        j = i + 1
        return ("run", s[i:j]), j
    j = i
    while j < len(s) and s[j] not in OPS and s[j] not in " ()[]{}^_/":
        if s[j] in SUP_CHARS or s[j] in SUB_CHARS or s[j] == SLASH or s[j] == "⁽":
            break
        j += 1
    if j < len(s) and s[j] == SLASH and j - i > 1:
        # Aq̸ is A times q̸: the slash belongs to the last letter only
        j -= 1
    text = s[i:j]
    node = ("run", text)
    if j < len(s) and s[j] == SLASH:
        node = ("acc", node)
        j += 1
    if text.endswith("√") and j < len(s) and s[j] in "([":
        # √(2mω): the radical owns its bracket, so it stays whole under a /
        arg, j = _parse_delim(s, j + 1, s[j], ")" if s[j] == "(" else "]")
        node = ("seq", [node, arg])
    return node, j


INDEX_GREEK = set("μνρσαβλκδ")
MARKS = "′″†*!"


def _is_comb(ch):
    return "\u0300" <= ch <= "\u036f"


def _parse_index(s, i, single=False):
    """A bare script argument: γ^μ, Π^μν, ℒ_int, a_p†.

    The sources write γ^μγ^ν and ∂_μφ for γ^μ γ^ν and ∂_μ φ, so a bare
    argument is one index-like token: a run of Greek index letters (μν,
    ρσ), a run of digits, a lower-case or capitalised Latin label (int,
    eff, QED, Cas), or else one character, each with its primes and
    daggers. Anything after it is the next factor.
    """
    i = _skip(s, i)
    if i >= len(s) or s[i] in OPS or s[i] in "()[]{}^_/ " or s[i] in SUP_CHARS or s[i] in SUB_CHARS:
        return _parse_atom(s, i)
    node, end = _parse_atom(s, i)
    if node[0] != "run":
        return node, end
    w = node[1]
    if len(w) <= 1:
        while end < len(s) and s[end] in PRIMES:
            w += s[end]
            end += 1
        return ("run", w), end

    def grapheme(k):
        k += 1
        while k < len(w) and _is_comb(w[k]):
            k += 1
        return k

    c = w[0]
    if single:
        k = grapheme(0)
    elif c in INDEX_GREEK:
        k = 1
        while k < len(w) and w[k] in INDEX_GREEK:
            k += 1
    elif c.isdigit():
        k = 1
        while k < len(w) and w[k].isdigit():
            k += 1
    elif "a" <= c.lower() <= "z":
        followed = end < len(s) and s[end] in "^_"
        k = grapheme(0)
        if not followed and k == 1:
            upper_label = c.isupper()
            while k < len(w) and "a" <= w[k].lower() <= "z":
                if k + 1 < len(w) and _is_comb(w[k + 1]):
                    break  # zp̂: a hatted or slashed letter is a new factor
                if w[k].isupper() and not upper_label:
                    break  # pE, tD: lower then upper is two factors
                if w[k].isupper() and upper_label and w[k - 1].islower():
                    break
                k += 1
    else:
        k = grapheme(0)
    while k < len(w) and w[k] in MARKS:
        k += 1
    if k >= len(w):
        while end < len(s) and s[end] in PRIMES:
            # u_s′, δ_ss′: the prime is part of the index
            w += s[end]
            end += 1
        return ("run", w), end
    return ("run", w[:k]), i + k


def _apply_script(base, kind, arg):
    if kind == "sup" and base[0] == "sub":
        return ("subsup", base[1], base[2], arg)
    if kind == "sub" and base[0] == "sup":
        return ("subsup", base[1], arg, base[2])
    return (kind, base, arg)


def _parse_scripted(s, i):
    base, i = _parse_atom(s, i)
    while True:
        j = _skip(s, i)
        if j >= len(s):
            break
        c = s[j]
        if j > i and c in "([":
            break  # f (x): a space ends the atom
        if c in "([" and base[0] != "paren" and base != ("run", "") and not _is_op(base):
            # function application f(x), δ⁴(p−k), ψ_n[q]: the bracket belongs
            # to the atom, so f(x)/y puts all of f(x) in the numerator
            close = ")" if c == "(" else "]"
            arg, i = _parse_delim(s, j + 1, c, close)
            if _func_name(base) in FUNCS:
                base = ("func", base, arg)
            else:
                base = ("seq", [base, arg])
            continue
        if c in PRIMES and j == i:
            # y′, S_F′: a prime is a postfix of its atom
            if base[0] == "run":
                base = ("run", base[1] + c)
            else:
                base = ("seq", [base, ("run", c)])
            i = j + 1
            continue
        if c == "⁽":
            k = s.find("⁾", j)
            if k > j:
                inner = "".join(SUP_CHARS.get(ch, ch) for ch in s[j + 1:k])
                base = _apply_script(base, "sup", ("run", "(" + inner + ")"))
                i = k + 1
                continue
        if c not in SUP_CHARS and c not in SUB_CHARS and c not in "^_":
            break  # leave the space for _parse_sum to see
        i = j
        if c in SUP_CHARS or c in SUB_CHARS:
            # ⁻¹, ⁻²², ₁₂: consecutive script characters are one script
            table = SUP_CHARS if c in SUP_CHARS else SUB_CHARS
            k = i
            while k < len(s) and s[k] in table:
                k += 1
            text = "".join(table[ch] for ch in s[i:k])
            base = _apply_script(base, "sup" if table is SUP_CHARS else "sub", ("run", text))
            i = k
            continue
        if c in "^_":
            kind = "sup" if c == "^" else "sub"
            i += 1
            i = _skip(s, i)
            if i < len(s) and s[i] == "(":
                arg, i = _parse_group(s, i + 1, ")")
            elif i < len(s) and s[i] == "{":
                arg, i = _parse_group(s, i + 1, "}")
            elif _func_name(base) is not None and _func_name(base).endswith("∂"):
                # ∂_μα is ∂_μ acting on α: a derivative takes a one-letter index
                arg, i = _parse_index(s, i, single=True)
            else:
                arg, i = _parse_index(s, i)
            base = _apply_script(base, kind, arg)
            continue
        break
    return base, i


def _parse_term(s, i, stop):
    """Juxtaposed factors with no space between them: d⁴k, 2m, m(Zα)⁴.

    A fraction takes a whole term on each side, so d⁴k/(2π)⁴ puts d⁴k in
    the numerator. A space, an operator or a stop character ends the term.
    """
    node, i = _parse_scripted(s, i)
    nodes = [node]
    while i < len(s):
        c = s[i]
        if c == "|" and _abs_end(s, i) > 0:
            pass
        elif c == " " or c in OPS or c in "+−/" or c in stop or c in ")]}":
            break
        if c in SUP_CHARS or c in SUB_CHARS or c in "^_":
            break
        nxt, j = _parse_scripted(s, i)
        if j == i or nxt == ("run", ""):
            break
        nodes.append(nxt)
        i = j
    if len(nodes) == 1:
        return nodes[0], i
    return ("seq", nodes), i


def _parse_frac(s, i, stop):
    left, i = _parse_term(s, i, stop)
    while True:
        j = _skip(s, i)
        if j < len(s) and s[j] == "/" and (j + 1 >= len(s) or s[j + 1] not in stop):
            right, i = _parse_term(s, j + 1, stop)
            left = ("frac", _unwrap(left), _unwrap(right))
            continue
        return left, i


def _parse_sum(s, i, stop):
    nodes = []
    while True:
        j = _skip(s, i)
        gap = j > i
        i = j
        if i >= len(s) or s[i] in stop:
            break
        # A slash here is a fraction bar whose left side was already closed
        # by a stop in a previous call; treat a leading operator as a run.
        if s[i] == "," and gap and i + 1 < len(s) and s[i + 1] == " " and nodes:
            k = _skip(s, i + 1)
            matrix_row = (stop == "]" and nodes[-1][0] == "paren" and nodes[-1][2] == "["
                          and k < len(s) and s[k] == "[")
            if not matrix_row:
                # " , " is the sources' thin space (from LaTeX \,), not a comma
                nodes.append(THIN)
                i += 1
                continue
        if (s[i] in OPS or s[i] in "+−") and _abs_end(s, i) < 0:
            nodes.append(("run", s[i]))
            i += 1
            # spaces after an operator stay out; the next piece follows
            continue
        node, i = _parse_frac(s, i, stop)
        if node != ("run", ""):
            prev = nodes[-1] if nodes else None
            if prev is None or _is_op(prev) or (gap and _func_name(prev) in NARY):
                # (1/4)Σ, (1/2)m ẋ², Σ_k (1/2): a lone stacked fraction needs no brackets
                if node[0] == "paren" and node[1][0] == "frac":
                    node = _unwrap(node)
                elif node[0] == "seq" and node[1][0][0] == "paren" and node[1][0][1][0] == "frac":
                    node = ("seq", [_unwrap(node[1][0])] + node[1][1:])
            if prev is not None and not _is_op(prev):
                if _func_name(prev) in FUNCS and (gap or node[0] == "paren"):
                    nodes[-1] = ("func", prev, node)
                    continue
                if gap and prev[0] != "func":
                    nodes.append(SPACE)
                elif gap:
                    # sin x y: keep the space after the function's argument
                    nodes.append(SPACE)
            nodes.append(node)
        else:
            # nothing consumed: avoid an infinite loop
            if i < len(s) and s[i] not in stop:
                nodes.append(("run", s[i]))
                i += 1
            else:
                break
    if not nodes:
        return ("run", ""), i
    if len(nodes) == 1:
        return nodes[0], i
    return ("seq", nodes), i


def parse(text):
    text = text.replace("qquad", "    ")
    node, i = _parse_sum(text, 0, "")
    if i < len(text):
        rest = ("run", text[i:])
        if node[0] == "seq":
            node = ("seq", node[1] + [rest])
        else:
            node = ("seq", [node, rest])
    return node


def fill_omath(omath, text):
    _append_tree(omath, parse(text))


def describe(text):
    """Compact tree, used by the builder's self-check."""
    def rec(node):
        k = node[0]
        if k == "run":
            return node[1]
        if k == "seq":
            return "".join(rec(c) for c in node[1])
        if k == "frac":
            return "(%s)/(%s)" % (rec(node[1]), rec(node[2]))
        if k == "sup":
            return "%s^(%s)" % (rec(node[1]), rec(node[2]))
        if k == "sub":
            return "%s_(%s)" % (rec(node[1]), rec(node[2]))
        if k == "subsup":
            return "%s_(%s)^(%s)" % (rec(node[1]), rec(node[2]), rec(node[3]))
        if k == "acc":
            return "slash(%s)" % rec(node[1])
        if k == "paren":
            return "%s%s%s" % (node[2], rec(node[1]), node[3])
        if k == "space":
            return " "
        if k == "thin":
            return "\u2009"
        if k == "func":
            return "func[%s](%s)" % (rec(node[1]), rec(node[2]))
        return "?"
    return rec(parse(text))
