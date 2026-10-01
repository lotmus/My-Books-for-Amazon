const fs = require("fs");
const JSZip = require("jszip");
function strip(b) {
  return b.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&").replace(/\s+/g, " ").trim();
}
const keys = [
  "Protocol Flamingo is the Desk",
  "the first lie she had told",
  "Milo made a full recovery",
  "The no held",
  "Don\u2019t you make me choose",
  "She told Mabs anyway",
];
(async () => {
  const zip = await JSZip.loadAsync(fs.readFileSync("Protocol_Flamingo_Rev2.docx"));
  const xml = await zip.file("word/document.xml").async("string");
  const re = /<w:p\b[^>]*>[\s\S]*?<\/w:p>/g;
  let m, i = 0;
  while ((m = re.exec(xml))) {
    const t = strip(m[0]);
    for (const k of keys) {
      if (t.includes(k)) console.log("\n#" + i + " " + k + "\n" + t);
    }
    i++;
  }
})();
