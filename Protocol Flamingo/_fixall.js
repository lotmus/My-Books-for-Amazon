const fs = require("fs");
const JSZip = require("jszip");
const path = "C:\\Users\\lomus\\OneDrive\\My Books for Amazon\\Protocol Flamingo\\Protocol_Flamingo_Rev2.docx";

const QO = "\u201C";
const QC = "\u201D";
const AP = "\u2019";
const EM = "\u2014";

function esc(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
function paraText(p) {
  return [...p.matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)]
    .map((m) => m[1])
    .join("")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"');
}
function setParaText(p, text) {
  if (p.includes("<w:hyperlink") || p.includes("<w:drawing")) {
    throw new Error("refusing to flatten a linked paragraph: " + paraText(p).slice(0, 80));
  }
  const open = p.match(/^<w:p\b[^>]*>/)[0];
  const pPr = (p.match(/<w:pPr>[\s\S]*?<\/w:pPr>/) || [""])[0];
  const rPr = (p.match(/<w:rPr>[\s\S]*?<\/w:rPr>/) || [""])[0];
  return `${open}${pPr}<w:r>${rPr}<w:t xml:space="preserve">${esc(text)}</w:t></w:r></w:p>`;
}
function bodyPara(model, text) {
  return setParaText(model, text);
}
function parseParas(paraXml) {
  const out = [];
  let i = 0;
  while (i < paraXml.length) {
    const a = paraXml.indexOf("<w:p ", i);
    const b = paraXml.indexOf("<w:p>", i);
    let start = -1;
    if (a < 0) start = b;
    else if (b < 0) start = a;
    else start = Math.min(a, b);
    if (start < 0) {
      if (paraXml.slice(i).trim()) throw new Error("trailing non-para " + paraXml.slice(i, i + 80));
      break;
    }
    if (paraXml.slice(i, start).trim()) throw new Error("gap " + paraXml.slice(i, i + 80));
    const end = paraXml.indexOf("</w:p>", start);
    if (end < 0) throw new Error("unclosed p");
    out.push(paraXml.slice(start, end + "</w:p>".length));
    i = end + "</w:p>".length;
  }
  return out;
}

(async () => {
  const zip = await JSZip.loadAsync(fs.readFileSync(path));
  let xml = await zip.file("word/document.xml").async("string");
  let rels = await zip.file("word/_rels/document.xml.rels").async("string");
  let settings = await zip.file("word/settings.xml").async("string");

  const bodyOpen = xml.indexOf("<w:body>");
  const bodyClose = xml.lastIndexOf("</w:body>");
  if (bodyOpen < 0 || bodyClose < 0) throw new Error("no body");
  const before = xml.slice(0, bodyOpen + "<w:body>".length);
  const body = xml.slice(bodyOpen + "<w:body>".length, bodyClose);
  const after = xml.slice(bodyClose);
  const sectAt = body.lastIndexOf("<w:sectPr");
  if (sectAt < 0) throw new Error("no sect");
  const paraXml = body.slice(0, sectAt);
  const sect = body.slice(sectAt).trim();
  if (!sect.startsWith("<w:sectPr") || !sect.endsWith("</w:sectPr>")) throw new Error("bad sect");

  const arr = [];
  let i = 0;
  while (i < paraXml.length) {
    const a = paraXml.indexOf("<w:p ", i);
    const b = paraXml.indexOf("<w:p>", i);
    let start = -1;
    if (a < 0) start = b;
    else if (b < 0) start = a;
    else start = Math.min(a, b);
    if (start < 0) {
      if (paraXml.slice(i).trim()) throw new Error("trailing non-para " + paraXml.slice(i, i + 80));
      break;
    }
    if (paraXml.slice(i, start).trim()) throw new Error("gap " + paraXml.slice(i, i + 60));
    const end = paraXml.indexOf("</w:p>", start);
    if (end < 0) throw new Error("unclosed p");
    arr.push(paraXml.slice(start, end + "</w:p>".length));
    i = end + "</w:p>".length;
  }

  const text = (n) => paraText(arr[n]);
  function hits(pred) {
    const out = [];
    arr.forEach((p, idx) => {
      if (pred(paraText(p))) out.push(idx);
    });
    return out;
  }
  function one(pred, label) {
    const h = hits(pred);
    if (h.length !== 1) throw new Error(label + " count " + h.length + (h.length ? " eg " + text(h[0]).slice(0, 60) : ""));
    return h[0];
  }
  function replaceIn(pred, label, fn) {
    const idx = one(pred, label);
    const old = text(idx);
    const neu = fn(old);
    if (neu === old) throw new Error("no change " + label);
    arr[idx] = setParaText(arr[idx], neu);
    return idx;
  }
  function remove(pred, label) {
    const idx = one(pred, label);
    arr.splice(idx, 1);
  }

  // Series name on the title page.
  {
    const idx = one((t) => t === "A STORYBOOK OF NO SERIES AT ALL", "series");
    arr[idx] = setParaText(arr[idx], "THE INVASION STORYBOOKS");
  }

  // Chapter title. The joke stays in Jesse's mouth. It leaves the contents.
  {
    const idx = one((t) => t === "Biology", "biology heading");
    arr[idx] = setParaText(arr[idx], "The Pretzel Corridor");
  }
  {
    const idx = one((t) => t === "XI. Biology", "biology contents");
    arr[idx] = setParaText(arr[idx], "XI. The Pretzel Corridor");
  }

  // The shelf does not yet contain nine other books.
  replaceIn(
    (t) => t.startsWith("This one isn") && t.includes("retelling"),
    "note open",
    () =>
      `This one is not a retelling. Nine films and television series sit behind the idea of a shelf, and none of them is this book. The prose versions of those nine are not published yet. When they are, they will be the rest of the Invasion Storybooks, and each of them will have to be careful with dialogue that is not its own. This book is the original. It has no film to stand behind. It only has cousins, which is enough to make a family and, this book would argue, already enough to make a committee.`
  );
  replaceIn(
    (t) => t === "Look up anyway. Nobody else is going to mention it.",
    "cousins close",
    () =>
      `The nine cousins named above are films and series, not books this shelf is selling. The retellings are still to come. This novel is the one that is finished. Look up anyway. Nobody else is going to mention it.`
  );

  // Dipstick glossary already states the marker. Add Steve, who reads the same one.
  replaceIn(
    (t) => t.startsWith("Dipstick. Priya"),
    "dipstick gloss",
    (t) => t.replace("A hybrid leaks it.", "A hybrid leaks it. Steve smells the same marker.")
  );

  // Collapse the briefing that says the same thing twice.
  remove((t) => t.startsWith("There was, underneath the comedy, a harder current"), "harder current");
  remove((t) => t.startsWith("Halo Systems sold the world orbital internet from a campus"), "mall summary");
  remove((t) => t.startsWith("Below the food court, past a door marked"), "second control room");
  remove((t) => t.startsWith("Someone handed her a headset"), "early survey");
  remove((t) => t.startsWith(`${QO}Proxies,${QC}`) || t.startsWith("\"Proxies,\""), "proxy repeat");
  replaceIn(
    (t) => t.startsWith("Duval") && t.includes("face suggested a great deal"),
    "feed bridge",
    () =>
      `Duval${AP}s face suggested a great deal. Halvorsen moved on to the name the building already used for the apparatus it could not see: the Feed. The briefing that mattered was not going to happen in this room.`
  );
  replaceIn(
    (t) => t.startsWith("The gift shop sold a mug"),
    "gift shop",
    (t) => t + " A cover that sold this well had already lasted eleven years without anyone official having to notice it."
  );

  // The sex scene keeps the room and loses the catalogue.
  remove((t) => t.startsWith("He was built the way work builds a person"), "sex build");
  remove((t) => t.startsWith("What followed was not a performance"), "sex follow");

  // Jesse spends Dominic's name. Nora does not clear it on the same page.
  {
    const model = arr[one((t) => t.startsWith("Nora Calder had filmed forty-one"), "body model")];
    const morning = one((t) => t.startsWith("In the morning she told him she was going to tell Mabs"), "morning");
    const memo = bodyPara(
      model,
      `Jesse${AP}s phone lit on the nightstand before either of them was dressed. A voice memo, sent from the gas station, to a producer Nora had never agreed to meet. She heard her brother-in-law${AP}s name, and Lissome, and the eleven seconds. She did not throw the phone. She also did not tell him it was all right. ${QO}You don${AP}t get to spend him,${QC} she said. ${QO}Not for a download.${QC} He deleted the file in front of her. The producer had already heard it. That part did not delete. She was still going to tell Mabs before Texas. She did not say she had forgiven the memo.`
    );
    arr.splice(morning, 0, memo);
  }
  replaceIn(
    (t) => t.startsWith("In the morning she told him she was going to tell Mabs"),
    "morning trim",
    (t) =>
      t.replace(
        "In the morning she told him she was going to tell Mabs everything before Texas. He said Mabs had a right to a husband who was still a husband for two more days. They did not raise their voices. They also did not agree. ",
        "He said Mabs had a right to a husband who was still a husband for two more days. They did not raise their voices. The memo sat between them while they did it. "
      )
  );

  // The sedation is a thing done to her.
  replaceIn(
    (t) => t.startsWith("The van smelled of warm plastic"),
    "sedative",
    (t) =>
      t.replace(
        "The Escort would tell them later that the headache was a sedative the tender used for passengers who had not consented to a burn, and that the eleven hours missing from the clock were eleven hours of an ordinary rendezvous.",
        `The headache was a sedative. Nobody had asked her. The Escort would later call it a courtesy the tender used for passengers who had not consented to a burn, and he would call the eleven missing hours an ordinary rendezvous. Ordinary was his word. She had been counting mile markers, and then she was in a place she had not agreed to enter. She did not accept the correction, then or after.`
      )
  );
  replaceIn(
    (t) => t.includes("They called Dana from the lot"),
    "hours taken",
    (t) => t + " She told Dana the hours had been taken. Dana did not argue with the verb."
  );

  // After Mabs has said it, the book does not explain it again.
  replaceIn(
    (t) => t.includes("the same lesson Feld had spent an hour"),
    "lesson gloss",
    (t) =>
      t.replace(
        ` It was the same lesson Feld had spent an hour trying to explain to a trailer full of colonels: the ship had never once been spoken to as if it might listen. Neither, really, had Dominic.`,
        ""
      )
  );

  // Contents follows the new back-matter order.
  {
    const star = one((t) => t === "XII. Starfall", "star contents");
    const expect = [
      "A Note on the Cousins",
      "Appendix: The Science This Book Didn" + AP + "t Make Up",
      "Glossary",
      "Bibliography",
    ];
    for (let k = 0; k < 4; k++) {
      if (text(star + 1 + k) !== expect[k]) {
        throw new Error("contents slot " + k + " is " + text(star + 1 + k));
      }
    }
    const appLine = arr[star + 2];
    const bibLine = arr[star + 4];
    arr[star + 1] = setParaText(arr[star + 1], "A Note to the Reader");
    arr[star + 2] = setParaText(arr[star + 2], "The People Who Looked Up");
    arr[star + 3] = setParaText(arr[star + 3], "A Note on the Cousins");
    arr[star + 4] = setParaText(arr[star + 4], "Glossary");
    const extra = [
      setParaText(appLine, "Appendix: The Science This Book Didn" + AP + "t Make Up"),
      setParaText(bibLine, "Bibliography"),
      setParaText(bibLine, "Also by George Herbert Fontaine"),
      setParaText(bibLine, "About the Author"),
    ];
    arr.splice(star + 5, 0, ...extra);
  }

  // Move the note and the cast to the back, beside the cousins, so the sample can reach the barn.
  {
    const note = one((t) => t === "A NOTE TO THE READER", "note head");
    const contents = one((t) => t === "CONTENTS", "contents head");
    if (contents <= note) throw new Error("contents before note");
    const cousins = one((t) => t === "A NOTE ON THE COUSINS", "cousins head");
    const block = arr.splice(note, contents - note);
    const cousinsNow = one((t) => t === "A NOTE ON THE COUSINS", "cousins after splice");
    if (cousinsNow === cousins) {
      // index shifted because the block sat before the cousins
    }
    arr.splice(cousinsNow, 0, ...block);
  }

  // Also by, and a short author note, after the bibliography.
  {
    const modelH = arr[one((t) => t === "GLOSSARY", "gloss head")];
    const modelB = arr[one((t) => t.startsWith("Nora Calder had filmed forty-one"), "body model 2")];
    arr.push(setParaText(modelH, "ALSO BY GEORGE HERBERT FONTAINE"));
    arr.push(
      bodyPara(
        modelB,
        `The Invasion Storybooks begin with this book. The nine cousins named in the note are films and television series, not titles you can buy under this name. Prose retellings of those nine are still to come, and each of them will have to keep its hands off dialogue that belongs to someone else. When a retelling is finished, its title will be printed on this page. Until then, this is the shelf.`
      )
    );
    arr.push(setParaText(modelH, "ABOUT THE AUTHOR"));
    arr.push(
      bodyPara(
        modelB,
        `George Herbert Fontaine writes stories in which a committee outlasts a fleet. Protocol Flamingo is the first of the Invasion Storybooks. The people in it are invented. The alpaca is invented. The science in the appendix is not.`
      )
    );
  }

  // Page 1 starts at the story. Front matter stays in roman numerals.
  {
    const photo = one((t) => t.startsWith("Nobody believes a photograph anymore"), "deposition");
    if (photo < 1) throw new Error("deposition at 0");
    const front = sect
      .replace('w:h="11880"', 'w:h="12240"')
      .replace('w:gutter="0"', 'w:gutter="720"')
      .replace("<w:titlePg/>", '<w:type w:val="nextPage"/><w:pgNumType w:fmt="lowerRoman" w:start="1"/><w:titlePg/>');
    const back = sect
      .replace('w:h="11880"', 'w:h="12240"')
      .replace('w:gutter="0"', 'w:gutter="720"')
      .replace("<w:titlePg/>", '<w:pgNumType w:fmt="decimal" w:start="1"/>');
    arr[photo - 1] = arr[photo - 1].includes("<w:pPr>")
      ? arr[photo - 1].replace("</w:pPr>", front + "</w:pPr>")
      : arr[photo - 1].replace(/^(<w:p\b[^>]*>)/, "$1<w:pPr>" + front + "</w:pPr>");
    var finalSect = back;
  }

  // Point the appendix claims at the papers. Leave the bibliography's overview links on Wikipedia.
  for (let n = 0; n < arr.length; n++) {
    if (!arr[n].includes("<w:hyperlink")) continue;
    const t = paraText(arr[n]);
    if (t.includes("Hein, Pak") && arr[n].includes('r:id="rId7"')) {
      arr[n] = arr[n].replace('r:id="rId7"', 'r:id="rId28"');
    }
    if (t.includes("minimum viable population") && t.includes("Marin") && arr[n].includes('r:id="rId10"')) {
      arr[n] = arr[n].replace('r:id="rId10"', 'r:id="rId29"');
    }
    if (t.includes("Ronald Bracewell") && arr[n].includes('r:id="rId12"')) {
      arr[n] = arr[n].replace('r:id="rId12"', 'r:id="rId32"');
    }
    if (arr[n].includes('r:id="rId11"')) {
      arr[n] = arr[n].replace(/r:id="rId11"/g, 'r:id="rId29"');
    }
  }
  {
    const braceParas = arr.filter((p) => /Bracewell|patient probe/.test(paraText(p)));
    console.log("brace debug", braceParas.map((p) => JSON.stringify(paraText(p).slice(0, 160))));
    const b = one((t) => t.includes("Bracewell, R. N."), "bracewell bib");
    if (arr[b].includes("https://en.wikipedia.org/wiki/Bracewell_probe")) {
      arr[b] = arr[b]
        .replace("https://en.wikipedia.org/wiki/Bracewell_probe", "https://doi.org/10.1038/186670a0")
        .replace("The patient probe. The name and the idea: ", `${QO}Communications from Superior Galactic Communities.${QC} Nature 186 (1960): 670. `);
      if (arr[b].includes('r:id="rId12"')) arr[b] = arr[b].replace('r:id="rId12"', 'r:id="rId32"');
    }
  }
  if (!rels.includes('Id="rId32"')) {
    rels = rels.replace(
      "</Relationships>",
      '<Relationship Id="rId32" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" Target="https://doi.org/10.1038/186670a0" TargetMode="External"/></Relationships>'
    );
  }
  rels = rels.replace(
    'Id="rId11" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" Target="https://www.sciencedirect.com/science/article/abs/pii/S0094576513004669"',
    'Id="rId11" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" Target="https://arxiv.org/abs/1806.03856"'
  );

  if (!settings.includes("<w:mirrorMargins")) {
    if (!settings.includes('<w:zoom w:percent="60"/>')) throw new Error("no zoom anchor");
    settings = settings.replace('<w:zoom w:percent="60"/>', '<w:zoom w:percent="60"/><w:mirrorMargins/>');
  }

  const joined = arr.join("");
  const openQ = (joined.match(/\u201C/g) || []).length;
  const closeQ = (joined.match(/\u201D/g) || []).length;
  if (openQ !== closeQ) throw new Error("quotes " + openQ + " " + closeQ);
  const all = joined;
  const must = [
    "THE INVASION STORYBOOKS",
    "The Pretzel Corridor",
    "You don" + AP + "t get to spend him",
    "the hours had been taken",
    "Nobody had asked her",
    "ALSO BY GEORGE HERBERT FONTAINE",
    "ABOUT THE AUTHOR",
    "The retellings are still to come",
    "Steve smells the same marker",
    "w:h=\"12240\"",
    "lowerRoman",
    'w:start="1"',
  ];
  for (const m of must) if (!all.includes(m) && !finalSect.includes(m)) throw new Error("missing " + m);
  const banned = [
    "A STORYBOOK OF NO SERIES AT ALL",
    "XI. Biology",
    "the same lesson Feld had spent an hour",
    "Jupiter" + AP + "s shadow",
    "He was built the way work builds a person",
    "Halo Systems sold the world orbital internet from a campus",
    "There was, underneath the comedy, a harder current",
  ];
  for (const m of banned) if (all.includes(m)) throw new Error("still present " + m);
  // Heading Biology must be gone. The word can remain in dialogue.
  if (arr.some((p) => paraText(p) === "Biology")) throw new Error("heading remains");

  const noteAt = arr.findIndex((p) => paraText(p) === "A NOTE TO THE READER");
  const bookAt = arr.findIndex((p) => paraText(p) === "BOOK ONE");
  const cousinsAt = arr.findIndex((p) => paraText(p) === "A NOTE ON THE COUSINS");
  if (!(bookAt < noteAt && noteAt < cousinsAt)) {
    throw new Error("order book " + bookAt + " note " + noteAt + " cousins " + cousinsAt);
  }
  const contentsAt = arr.findIndex((p) => paraText(p) === "CONTENTS");
  if (!(contentsAt < bookAt)) throw new Error("contents after book");

  xml = before + joined + finalSect + after;
  zip.file("word/document.xml", xml);
  zip.file("word/_rels/document.xml.rels", rels);
  zip.file("word/settings.xml", settings);
  const buf = await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" });
  fs.writeFileSync(path, buf);
  const words = arr.map(paraText).join(" ").split(/\s+/).filter(Boolean).length;
  console.log("wrote", buf.length, "words", words, "quotes", openQ, "paras", arr.length);
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
