"""Turn the course's linear display-math dialect into Office Math (OMML).

The lesson sources write fractions with /, superscripts with ^ or ², subscripts
with _ or ₀, and a slashed momentum as a letter plus U+0338. This module builds
real stacked fractions, superscripts, and subscripts so a display equation is
not one long Unicode run.
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
# Characters that are their own math run (operators and punctuation).
OPS = set("+=−–—×÷·⋅,;:<>≤≥≈∝→←±∓|′…⋯")


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


def _parse_atom(s, i):
    i = _skip(s, i)
    if i >= len(s):
        return ("run", ""), i
    c = s[i]
    if c == "(":
        return _parse_group(s, i + 1, ")")
    if c == "[":
        inner, i = _parse_group(s, i + 1, "]")
        return ("seq", [("run", "["), inner, ("run", "]")]), i
    if c in SUP_CHARS or c in SUB_CHARS or c in "^_/" or c == SLASH:
        return ("run", ""), i
    if c in OPS or c in "()[]{}":
        j = i + 1
        return ("run", s[i:j]), j
    j = i
    while j < len(s) and s[j] not in OPS and s[j] not in " ()[]{}^_/":
        if s[j] in SUP_CHARS or s[j] in SUB_CHARS or s[j] == SLASH:
            break
        j += 1
    text = s[i:j]
    node = ("run", text)
    if j < len(s) and s[j] == SLASH:
        node = ("acc", node)
        j += 1
    return node, j


def _apply_script(base, kind, arg):
    if kind == "sup" and base[0] == "sub":
        return ("subsup", base[1], base[2], arg)
    if kind == "sub" and base[0] == "sup":
        return ("subsup", base[1], arg, base[2])
    return (kind, base, arg)


def _parse_scripted(s, i):
    base, i = _parse_atom(s, i)
    while True:
        i = _skip(s, i)
        if i >= len(s):
            break
        c = s[i]
        if c in SUP_CHARS:
            base = _apply_script(base, "sup", ("run", SUP_CHARS[c]))
            i += 1
            continue
        if c in SUB_CHARS:
            base = _apply_script(base, "sub", ("run", SUB_CHARS[c]))
            i += 1
            continue
        if c in "^_":
            kind = "sup" if c == "^" else "sub"
            i += 1
            i = _skip(s, i)
            if i < len(s) and s[i] == "(":
                arg, i = _parse_group(s, i + 1, ")")
            elif i < len(s) and s[i] == "{":
                arg, i = _parse_group(s, i + 1, "}")
            else:
                arg, i = _parse_atom(s, i)
            base = _apply_script(base, kind, arg)
            continue
        break
    return base, i


def _parse_frac(s, i, stop):
    left, i = _parse_scripted(s, i)
    while True:
        j = _skip(s, i)
        if j < len(s) and s[j] == "/" and (j + 1 >= len(s) or s[j + 1] not in stop):
            right, i = _parse_scripted(s, j + 1)
            left = ("frac", left, right)
            continue
        return left, i


def _parse_sum(s, i, stop):
    nodes = []
    while True:
        i = _skip(s, i)
        if i >= len(s) or s[i] in stop:
            break
        # A slash here is a fraction bar whose left side was already closed
        # by a stop in a previous call; treat a leading operator as a run.
        if s[i] in OPS or s[i] in "+−":
            nodes.append(("run", s[i]))
            i += 1
            # spaces after an operator stay out; the next piece follows
            continue
        node, i = _parse_frac(s, i, stop)
        if node != ("run", ""):
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
        return "?"
    return rec(parse(text))
