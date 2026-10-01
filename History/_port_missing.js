const fs = require("fs");
const path = require("path");
const dir = path.join(__dirname, "chapters");

function norm(s) {
  return s
    .replace(/[“”]/g, '"')
    .replace(/[‘’]/g, "'")
    .replace(/[—–]/g, "-")
    .replace(/\*\*/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}
function jsString(s) {
  return '"' + s.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"';
}
function blockNorm(block) {
  let t = block;
  if (t.startsWith("### ")) t = t.replace(/^###\s*/, "");
  else if (t.startsWith("*") && t.endsWith("*")) t = t.slice(1, -1);
  return norm(t);
}
function toCall(block) {
  if (block.startsWith("### ")) return `  subhead(${jsString(block.replace(/^###\s*/, ""))}),`;
  if (block.startsWith("*") && block.endsWith("*")) return `  italic(${jsString(block.slice(1, -1))}),`;
  return `  body(${jsString(block)}),`;
}
function quotedSet(src) {
  const set = new Set();
  let i = 0;
  while (i < src.length) {
    if (src[i] === '"') {
      let j = i + 1, s = "";
      while (j < src.length) {
        if (src[j] === "\\") { s += src[j + 1] || ""; j += 2; continue; }
        if (src[j] === '"') break;
        s += src[j];
        j++;
      }
      if (s.length > 12) set.add(norm(s));
      i = j + 1;
    } else i++;
  }
  return set;
}

let js = fs.readFileSync(path.join(__dirname, "_generate.js"), "utf8");
let set = quotedSet(js);
const files = fs.readdirSync(dir).filter((f) => f.endsWith(".md")).sort((a, b) => a.localeCompare(b, "en"));
let total = 0;

for (const f of files) {
  const md = fs.readFileSync(path.join(dir, f), "utf8");
  const headLine = (md.split(/\n/).find((l) => l.startsWith("## ")) || "").replace(/^##\s*/, "").trim();
  const headIdx = headLine ? js.indexOf('heading("' + headLine.slice(0, 24)) : 0;
  const start = headIdx < 0 ? 0 : headIdx;
  const body = md.split("**Dolphin verdict:**")[0];
  const blocks = body.split(/\n\n+/).map((b) => b.trim()).filter((b) => b && !b.startsWith("## "));
  let i = 0;
  while (i < blocks.length) {
    if (set.has(blockNorm(blocks[i]))) { i++; continue; }
    let j = i;
    while (j < blocks.length && !set.has(blockNorm(blocks[j]))) j++;
    const calls = blocks.slice(i, j).map(toCall).join("\n") + "\n";
    let insertAt = -1;
    if (j < blocks.length) {
      const key = blockNorm(blocks[j]).slice(0, 60);
      const region = js.slice(start);
      const lines = region.split("\n");
      let acc = 0;
      for (const line of lines) {
        if (norm(line).includes(key.slice(0, 45))) { insertAt = start + acc; break; }
        acc += line.length + 1;
      }
    }
    if (insertAt < 0) {
      const v = js.indexOf("...verdict(", start);
      insertAt = v;
    }
    if (insertAt < 0) {
      console.log("NO ANCHOR", f);
      break;
    }
    js = js.slice(0, insertAt) + calls + js.slice(insertAt);
    for (const b of blocks.slice(i, j)) set.add(blockNorm(b));
    console.log(f, j - i);
    total += j - i;
    i = j;
  }
}
fs.writeFileSync(path.join(__dirname, "_generate.js"), js);
console.log("INSERTED", total);

const manPath = path.join(__dirname, "The Dolphins' View of History - Complete Manuscript.md");
const old = fs.readFileSync(manPath, "utf8");
const nl = old.includes("\r\n") ? "\r\n" : "\n";
const splitAt = old.indexOf(nl + "## ");
const front = old.slice(0, splitAt + nl.length);
const bodies = files.map((f) => fs.readFileSync(path.join(dir, f), "utf8").replace(/\r\n/g, "\n").replace(/\n+$/, ""));
let joined = front.replace(/\r\n/g, "\n") + bodies.join("\n\n") + "\n";
if (nl === "\r\n") joined = joined.replace(/\n/g, "\r\n");
fs.writeFileSync(manPath, joined);
console.log("MANUSCRIPT", joined.length);
