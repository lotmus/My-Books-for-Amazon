const fs = require("fs");
const JSZip = require("jszip");
const A = "\u2019";
const E = "\u2014";
const LQ = "\u201C";
const RQ = "\u201D";

function strip(block) {
  return block.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&").replace(/\s+/g, " ").trim();
}
function escapeText(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
function rebuild(block, newText) {
  const open = block.match(/^<w:p\b[^>]*>/)[0];
  const pPr = (block.match(/<w:pPr>[\s\S]*?<\/w:pPr>/) || [""])[0];
  const rPr = (block.match(/<w:rPr>[\s\S]*?<\/w:rPr>/) || [""])[0];
  return open + pPr + "<w:r>" + rPr + '<w:t xml:space="preserve">' + escapeText(newText) + "</w:t></w:r></w:p>";
}
function parse(xml) {
  const re = /<w:p\b[^>]*>[\s\S]*?<\/w:p>/g;
  const chunks = [];
  let last = 0, m;
  while ((m = re.exec(xml))) {
    if (m.index > last) chunks.push({ kind: "gap", s: xml.slice(last, m.index) });
    chunks.push({ kind: "p", s: m[0], text: strip(m[0]) });
    last = m.index + m[0].length;
  }
  if (last < xml.length) chunks.push({ kind: "gap", s: xml.slice(last) });
  return chunks;
}
function one(chunks, needle) {
  const hits = chunks.filter((c) => c.kind === "p" && c.text.includes(needle));
  if (hits.length !== 1) throw new Error("COUNT " + hits.length + " :: " + needle.slice(0, 70));
  return hits[0];
}
function paraFrom(sample, text) {
  return rebuild(sample.s, text);
}

(async () => {
  const file = "Protocol_Flamingo_Rev2.docx";
  const zip = await JSZip.loadAsync(fs.readFileSync(file));
  let xml = await zip.file("word/document.xml").async("string");
  const chunks = parse(xml);

  const lie = one(chunks, "the first lie she had told him on purpose");
  const drawer = "After he left for work she opened the drawer under the towels. The napkin from Thanksgiving was still in it, brown at the edge where his thumb had been. She put the photograph of the plate underneath the napkin and shut the drawer with her hip. She did not send Nora the picture. Nora already knew about the cars. What Nora did not know yet was that Mabs had decided to stay in the house, make the coffee, and wait for a sentence she could say to her husband without taking him apart at the sink.";
  const lieAt = chunks.indexOf(lie);
  chunks.splice(lieAt + 1, 0, { kind: "p", s: paraFrom(lie, drawer), text: drawer });

  const corridor = one(chunks, "Don" + A + "t you make me choose in a stadium");
  const corridorText = "In the morning she told him she was going to tell Mabs everything before Texas. He said Mabs had a right to a husband who was still a husband for two more days. They did not raise their voices. They also did not agree. She told Mabs anyway, in a service corridor that smelled of pretzels, three hours before totality. Mabs had flour on one cuff from a pretzel she had bought because a child in the line was watching her not buy one. She made Nora say hybrid twice. She heard the eleven seconds, the thumb, and the cars, and she did not cry where her sister could see it. " + LQ + "I know he" + A + "s different," + RQ + " she said. Then, " + LQ + "Don" + A + "t you make me choose in a stadium." + RQ + " Nora started to nod, and Mabs put a hand on her wrist, light, the way you stop a person from agreeing too fast. " + LQ + "If he comes back, he comes back as the man who carved the turkey. Not as your file." + RQ + " Nora did not make her choose. That was the cost. She went to section 114 with her sister" + A + "s permission and without her sister" + A + "s peace.";
  corridor.s = rebuild(corridor.s, corridorText);
  corridor.text = corridorText;

  const milo = one(chunks, "Milo made a full recovery");
  const miloText = milo.text.replace(
    "never once learned how close a badly timed flight schedule had come to being the whole story. ",
    "never once learned how close a badly timed flight schedule had come to being the whole story. On the Monday he went back, he told his class the hospital gravy was a crime and that a helicopter had landed for somebody else" + A + "s emergency. He did not mention his father. The teacher wrote imaginative in the margin and sent the note home. Kade laughed once, in his own kitchen, where nobody from Halo could hear it, and left the note on the refrigerator under a magnet shaped like a satellite. "
  );
  if (miloText === milo.text) throw new Error("milo splice missed");
  milo.s = rebuild(milo.s, miloText);
  milo.text = miloText;

  const no = one(chunks, "The no held.");
  const whit = "Whitcombe initialed the refusal from London on a copy that arrived after lunch, and wrote one line in the margin: a larger broadcast is just a louder way of not asking. Halvorsen left the line in the file. Buchanan did not.";
  const noAt = chunks.indexOf(no);
  chunks.splice(noAt + 1, 0, { kind: "p", s: paraFrom(no, whit), text: whit });

  xml = chunks.map((c) => c.s).join("");
  const text = strip(xml);
  for (const n of ["photograph of the plate underneath the napkin", "Not as your file", "magnet shaped like a satellite", "a louder way of not asking"]) {
    if (!text.includes(n)) throw new Error("MISSING " + n);
  }
  const lq = (text.match(/\u201C/g) || []).length;
  const rq = (text.match(/\u201D/g) || []).length;
  if (lq !== rq) throw new Error("quotes " + lq + " " + rq);
  zip.file("word/document.xml", xml);
  const buf = await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" });
  fs.writeFileSync(file, buf);
  console.log("wrote", buf.length, "words", text.split(/\s+/).length, "quotes", lq);
})().catch((e) => { console.error(e.message || e); process.exitCode = 1; });
