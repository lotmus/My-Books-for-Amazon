const fs = require("fs");
const JSZip = require("jszip");
(async () => {
  const zip = await JSZip.loadAsync(fs.readFileSync("Protocol_Flamingo_Rev2.docx"));
  const xml = await zip.file("word/document.xml").async("string");
  const i = xml.indexOf("Bracewell");
  console.log("idx", i);
  console.log(xml.slice(i - 100, i + 400));
})();
