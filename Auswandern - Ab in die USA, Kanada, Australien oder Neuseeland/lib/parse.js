"use strict";
// Shared Markdown-subset parser for the book pipeline (DOCX builder, EPUB
// preprocessor, linter). Supported subset is defined in _Konzept/00_Buchbibel.md.
//
// Block types produced:
//   {type:"h1"|"h2"|"h3"|"h4", text}
//   {type:"p", text}
//   {type:"list", items:[{kind:"ul"|"ol", level:0|1, text, check:null|" "|"x"}]}
//   {type:"table", header:[str], rows:[[str]]}
//   {type:"box", label, blocks:[...]}      // "> **Label:** ..." blockquotes
//   {type:"quote", blocks:[...]}           // unlabeled blockquote
//   {type:"directive", name}               // %%NAME%%

const fs = require("fs");
const path = require("path");

const NBSP = " ";

// Recursively collects manuscript chapter files under `dir` (which may group
// them into subfolders, e.g. 02_USA/), skipping "_"-prefixed files/folders.
// Returns paths relative to `dir`, sorted so numbered subfolders keep the
// book's front-to-back order.
function listManuscriptFiles(dir) {
  const out = [];
  (function walk(sub) {
    const abs = path.join(dir, sub);
    for (const entry of fs.readdirSync(abs, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
      if (entry.name.startsWith("_")) continue;
      const rel = sub ? path.join(sub, entry.name) : entry.name;
      if (entry.isDirectory()) walk(rel);
      else if (entry.name.endsWith(".md")) out.push(rel);
    }
  })("");
  return out.sort();
}

// ---------------------------------------------------------------- typography
// Fixes leftover straight quotes (writers are told to use typographic ones),
// and inserts non-breaking spaces where a line break would look wrong.
function typo(s) {
  let out = "";
  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    if (ch === '"') {
      const prev = i > 0 ? s[i - 1] : "";
      const open = prev === "" || /[\s(\[{–—\/‚„]/.test(prev);
      out += open ? "„" : "“";
    } else if (ch === "'") {
      const prev = i > 0 ? s[i - 1] : "";
      const next = i < s.length - 1 ? s[i + 1] : "";
      const open = (prev === "" || /[\s(\[{–—\/„]/.test(prev)) && /\S/.test(next);
      out += open ? "‚" : "’";
    } else out += ch;
  }
  out = out.replace(
    /(\d) (%|\$|€|Uhr|Prozent|Jahre|Jahren|Monate|Monaten|Wochen|Tage|Tagen|Stunden|Minuten|Mio\.|Mrd\.|km|mph|°F|°C|m²|sq ft|kg|lb)(?![A-Za-zÄÖÜäöüß])/g,
    "$1" + NBSP + "$2"
  );
  out = out.replace(/\b(z|d|u|s|i|v)\. (B|h|a|U|o|d|R|A)\./g, "$1." + NBSP + "$2.");
  out = out.replace(/\b(Kapitel|Kapiteln|Anhang|Abschnitt|Seite|Tabelle) (\d+|[A-G]\b)/g, "$1" + NBSP + "$2");
  return out;
}

// ---------------------------------------------------------------- inline
// Returns runs: {t, b, i} or {br:true} or {link, t, b, i}. Supports **bold**,
// *italic*, <br>, and [text](url) links. A link's `link` value starting with
// "#" is an internal anchor (resolved against a heading bookmark); otherwise
// it's an external URL.
function parseInline(s) {
  const runs = [];
  function walk(str, b, i) {
    let pos = 0;
    let buf = "";
    const flush = () => { if (buf) { runs.push({ t: buf, b, i }); buf = ""; } };
    while (pos < str.length) {
      if (str.startsWith("<br>", pos) || str.startsWith("<br/>", pos)) {
        flush(); runs.push({ br: true });
        pos += str.startsWith("<br>", pos) ? 4 : 5; continue;
      }
      if (str[pos] === "[") {
        const closeBracket = str.indexOf("]", pos + 1);
        if (closeBracket > pos && str[closeBracket + 1] === "(") {
          const closeParen = str.indexOf(")", closeBracket + 2);
          if (closeParen > closeBracket) {
            const linkText = str.slice(pos + 1, closeBracket);
            const url = str.slice(closeBracket + 2, closeParen);
            flush();
            runs.push({ link: url, t: linkText, b, i });
            pos = closeParen + 1; continue;
          }
        }
      }
      if (str.startsWith("**", pos)) {
        const end = str.indexOf("**", pos + 2);
        if (end > pos + 2) { flush(); walk(str.slice(pos + 2, end), true, i); pos = end + 2; continue; }
      }
      if (str[pos] === "*" && !str.startsWith("**", pos) && str[pos + 1] !== " ") {
        let end = -1;
        for (let k = pos + 1; k < str.length; k++) {
          if (str[k] === "*") { if (str[k + 1] === "*") { k++; continue; } end = k; break; }
        }
        if (end > pos + 1) { flush(); walk(str.slice(pos + 1, end), b, true); pos = end + 1; continue; }
      }
      buf += str[pos]; pos++;
    }
    flush();
  }
  walk(s, false, false);
  return runs;
}

function stripInline(s) {
  return parseInline(s).map((r) => (r.br ? " " : r.link ? r.t : r.t)).join("");
}

// ---------------------------------------------------------------- blocks
const BULLET_RE = /^(\s*)([-*•])\s+(.*)$/;
const NUM_RE = /^(\s*)(\d{1,3})[.)]\s+(.*)$/;
const SEP_RE = /^\|?[\s:|-]+\|?$/;

function splitRow(row) {
  let r = row.trim();
  if (r.startsWith("|")) r = r.slice(1);
  if (r.endsWith("|")) r = r.slice(0, -1);
  return r.split("|").map((c) => c.trim());
}

function parseLines(lines) {
  const blocks = [];
  let para = [];
  const flushPara = () => {
    if (para.length) { blocks.push({ type: "p", text: para.join(" ").trim() }); para = []; }
  };
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    const t = line.trim();
    if (t === "") { flushPara(); i++; continue; }
    let m;

    if ((m = t.match(/^%%([A-Z]+)%%$/))) { flushPara(); blocks.push({ type: "directive", name: m[1] }); i++; continue; }

    if ((m = line.match(/^(#{1,4})\s+(.*?)\s*#*\s*$/))) {
      flushPara(); blocks.push({ type: "h" + m[1].length, text: m[2] }); i++; continue;
    }

    if (t.startsWith("|") && i + 1 < lines.length && SEP_RE.test(lines[i + 1].trim()) && lines[i + 1].includes("-")) {
      flushPara();
      const header = splitRow(t);
      i += 2;
      const rows = [];
      while (i < lines.length && lines[i].trim().startsWith("|")) { rows.push(splitRow(lines[i])); i++; }
      blocks.push({ type: "table", header, rows });
      continue;
    }

    if (t.startsWith(">")) {
      flushPara();
      const inner = [];
      while (i < lines.length && lines[i].trim().startsWith(">")) {
        inner.push(lines[i].replace(/^\s*>\s?/, ""));
        i++;
      }
      let label = null;
      const firstIdx = inner.findIndex((l) => l.trim() !== "");
      if (firstIdx >= 0) {
        const lm = inner[firstIdx].trim().match(/^\*\*(.+?):\*\*\s*(.*)$/);
        if (lm) { label = lm[1].trim(); inner[firstIdx] = lm[2]; }
      }
      const sub = parseLines(inner);
      blocks.push(label ? { type: "box", label, blocks: sub } : { type: "quote", blocks: sub });
      continue;
    }

    if (BULLET_RE.test(line) || NUM_RE.test(line)) {
      flushPara();
      const items = [];
      const itemMatch = (l) => {
        let mm = l.match(BULLET_RE);
        if (mm) return { kind: "ul", indent: mm[1].length, text: mm[3] };
        mm = l.match(NUM_RE);
        if (mm) return { kind: "ol", indent: mm[1].length, text: mm[3] };
        return null;
      };
      while (i < lines.length) {
        const l = lines[i];
        if (l.trim() === "") {
          let j = i + 1;
          while (j < lines.length && lines[j].trim() === "") j++;
          if (j < lines.length && itemMatch(lines[j])) { i = j; continue; }
          break;
        }
        const im = itemMatch(l);
        if (im) {
          let text = im.text;
          let check = null;
          const cm = text.match(/^\[( |x|X)\]\s+(.*)$/);
          if (cm) { check = cm[1].toLowerCase(); text = cm[2]; }
          items.push({ kind: im.kind, level: im.indent >= 2 ? 1 : 0, text, check });
          i++;
        } else if (/^\s+\S/.test(l) && items.length) {
          items[items.length - 1].text += " " + l.trim(); i++;
        } else break;
      }
      blocks.push({ type: "list", items });
      continue;
    }

    para.push(t); i++;
  }
  flushPara();
  return blocks;
}

function parseMarkdown(text) {
  return parseLines(text.replace(/^﻿/, "").replace(/\r\n?/g, "\n").split("\n"));
}

// ---------------------------------------------------------------- utilities
function blockText(b) {
  switch (b.type) {
    case "p": case "h1": case "h2": case "h3": case "h4": return stripInline(b.text);
    case "list": return b.items.map((it) => stripInline(it.text)).join(" ");
    case "table": return [b.header, ...b.rows].map((r) => r.map(stripInline).join(" ")).join(" ");
    case "box": case "quote": return b.blocks.map(blockText).join(" ");
    default: return "";
  }
}

function countWords(blocks) {
  const text = blocks.map(blockText).join(" ");
  const m = text.match(/[\p{L}\p{N}][\p{L}\p{N}'’.,\-/%$€]*/gu);
  return m ? m.length : 0;
}

// Cross-reference pattern: "Kapitel 12", "Kapiteln 12–14", "Kapitel 12 und 13", "Anhang B".
const XREF_RE = /(Kapitel(?:n)?)[\s ]+(\d{1,2}(?:\s*(?:[–,]|und|bis)\s*\d{1,2})*)|(Anhang)[\s ]+([A-G])\b/g;

// Stable anchor/bookmark name for a "## ..." heading, shared by the DOCX
// builder (which creates the bookmark) and the linter (which validates that
// internal [text](#anchor) links resolve to a real one). `filename` is the
// source file's basename; `fallbackIdx` is a per-document running counter
// used only when neither pattern matches (so every h2 still gets a unique id).
function bookmarkFor(h2text, filename, fallbackIdx) {
  let m = h2text.match(/^Kapitel\s+(\d+)\s*:/);
  if (m) return "k" + m[1];
  m = h2text.match(/^Anhang\s+([A-G])\b/);
  if (m) return "anhang_" + m[1].toLowerCase();
  m = filename && filename.match(/^(TAU|TKA|TNZ|T00)_K(\d\d)_/);
  if (m) return (m[1] + m[2]).toLowerCase();
  return "s" + fallbackIdx;
}

module.exports = { NBSP, typo, parseInline, stripInline, parseMarkdown, parseLines, blockText, countWords, XREF_RE, bookmarkFor, listManuscriptFiles };
