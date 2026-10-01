const fs = require("fs");
const JSZip = require("jszip");
const path = "C:\\Users\\lomus\\OneDrive\\My Books for Amazon\\Protocol Flamingo\\Protocol_Flamingo_Rev2.docx";
(async () => {
  const zip = await JSZip.loadAsync(fs.readFileSync(path));
  const xml = await zip.file("word/document.xml").async("string");
  const rels = await zip.file("word/_rels/document.xml.rels").async("string");
  const i = xml.indexOf("<w:sectPr");
  console.log("sect context", xml.slice(i - 200, i + 80).replace(/\n/g, ""));
  const body = xml.indexOf("<w:body");
  console.log("body start", xml.slice(body, body + 120));
  const p = xml.indexOf("Nora Calder had filmed");
  console.log("sample", xml.slice(p - 400, p + 80).replace(/\n/g, " "));
  fs.writeFileSync("_rels.txt", rels, "utf8");
  const settings = zip.file("word/settings.xml");
  if (settings) {
    const s = await settings.async("string");
    fs.writeFileSync("_settings_snip.txt", s.slice(0, 1500), "utf8");
  }
  console.log("rels bytes", rels.length);
})();
