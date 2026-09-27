"use strict";
// One-off generator for the ten part-divider files (manuscript/T##_00_Teil_*.md).
// Edit taglines here and re-run: node lib/gen_parts.js
const fs = require("fs");
const path = require("path");
const parts = [
  ["01", "I", "Die Entscheidung", "Bevor du Kisten packst, rechnest du. Dieser Teil zeigt beide Seiten der Medaille, die häufigsten Fallen und einen Weg, mit Zahlen statt Bauchgefühl zu entscheiden."],
  ["02", "II", "Visum und Green Card", "Ohne das richtige Papier geht nichts. Wie H-1B, Green Card, Studium und die anderen Wege funktionieren, was sie unterscheidet und wo sie teuer oder riskant werden."],
  ["03", "III", "Wohnort und Wohnen", "Wo du lebst, entscheidet über Gehalt, Schule, Steuern und Freundeskreis. Und ob du mietest oder kaufst, über einen großen Teil deines Vermögens."],
  ["04", "IV", "Vorbereitung in Deutschland", "Was du erledigst, solange du noch einen deutschen Briefkasten hast: Behörden, Verträge, Steuern, Rente, Krankenversicherung und Dokumente."],
  ["05", "V", "Der Umzug", "Container, Koffer oder Neuanfang? Wie du Umzugskosten senkst, was in den Container gehört und was du drüben günstiger kaufst."],
  ["06", "VI", "Ankommen", "Die ersten Tage und Wochen: Einreise, Sozialversicherungsnummer, Bank, Krankenversicherung, Führerschein und Steuern."],
  ["07", "VII", "Arbeiten in den USA", "Anderes Arbeitsrecht, andere Regeln, anderes Selbstverständnis. Was du wissen musst, wenn du Karriere machst und wenn der Job wechselt."],
  ["08", "VIII", "Leben und Menschen", "Kultur, Freundschaft, Heimweh, Kleidung und Essen: die Dinge, die im Alltag über Zufriedenheit entscheiden."],
  ["09", "IX", "Kinder und Schule", "Schulsystem, Englisch als Zweitsprache, Babys, Teenager und College: was Eltern wissen müssen."],
  ["10", "X", "Langfristig", "Vorsorge, Erbe, Recht, Staatsbürgerschaft und der Plan B für den Fall, dass du zurückkehrst."],
];
const dir = path.join(__dirname, "..", "manuscript");
parts.forEach(([num, roman, title, tag]) => {
  fs.writeFileSync(path.join(dir, `T${num}_00_Teil_${roman}.md`), `# TEIL ${roman} — ${title}\n\n${tag}\n`, "utf-8");
});
console.log("wrote " + parts.length + " part files");
