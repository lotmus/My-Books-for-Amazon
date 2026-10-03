# ANLEITUNG FÜR KAPITEL-AUTOREN — Länder-Teile Kanada/Australien/Neuseeland und neue Universal-Kapitel

Du schreibst ein oder zwei Kapitel der erweiterten Ausgabe „Die Auswanderer-Bibel: USA, Kanada, Australien, Neuseeland" (bisher „Auswandern in die USA"). Projektordner: `D:\My Books for Amazon\Auswandern in die USA`.

## 1. Lesen (in dieser Reihenfolge)
1. `_Konzept\00_Buchbibel.md` — verbindlicher Ton-/Formatvertrag. Beachte besonders **§2.2.1** (eigener Humor-Ton für Kanada/Australien/Neuseeland: britisch geprägt — Understatement, Ironie, Sarkasmus, Selbstironie über die eigene Verwirrung; nie auf Kosten von Personen/Gruppen oder bei Visum/Gesundheit/Geld/Diskriminierung) und **§7.1** (eigene Fallbeispiel-Personen je Länder-Teil — nutze NUR die für dein Land vorgesehenen Personen, niemals die USA-Besetzung Brandt/Keller/Hoffmann/Wagner/Scholz).
2. `_Konzept\06_Gliederung_Vierlaender.md` — Gesamtstruktur, damit du weißt, wohin dein Kapitel gehört und worauf du querverweisen kannst.
3. Die dir zugewiesenen Faktenblätter (siehe dein Auftrag) in `_Recherche_Kanada\`, `_Recherche_Australien\`, `_Recherche_Neuseeland\` oder `_Recherche_Vergleich\`. Lies KERNZAHLEN zuerst, dann die Details, die du brauchst. Faktenblätter sind Material, kein Text zum Abschreiben.
4. Überflieg 1-2 thematisch verwandte, bereits fertige USA-Kapitel in `manuscript\` (z. B. `T02_K05_Das_H1B_Visum.md` für ein Arbeitsvisum-Kapitel) nur für Ton, Struktur und Boxen-Einsatz — nicht für Fakten (die USA-Regeln gelten nicht für dein Land).

## 2. Recherche (sparsam)
- **Web-Budget: höchstens 6 Aufrufe** — nur für Lücken, die im Faktenblatt unter „UNSICHER/OFFEN" stehen und für dein Kapitel wichtig sind. Der Rest kommt aus dem Faktenblatt.
- Faktenblatt und eigenes Wissen widersprechen sich → Faktenblatt gilt, außer du findest eine neuere Primärquelle.
- Schreibe nie eine Zahl/Frist/Gebühr, die du nicht belegen kannst. Lieber „ändert sich häufig, aktuelle Höhe unter …" als raten.

## 3. Schreiben
- Ein Kapitel = eine Datei, komplett mit dem Write-Tool, UTF-8, Markdown-Subset laut Buchbibel §1–§6 und §8 (Terminologie/Boxen/Struktur — identisch zum USA-Teil).
- Dateiname und Wortziel: siehe dein Auftrag unten. Überschrift im Kapitel: `## Kapitel [Name des Länder-Teils] · [Kurztitel]` (z. B. `## Australien: Wege der Einwanderung`) — noch keine feste Gesamt-Kapitelnummer, die kommt erst bei der finalen Zusammenführung.
- Aufbau: `Kurz gesagt`-Box nach einem konkreten Einstieg, Boxen mit Augenmaß (Achtung/Spartipp/Merke/Praxisbeispiel), `### Plus und Minus`-Tabelle, `> **Checkliste:**`, `### Quellen und weiterführende Links`, `> **Stand:**`-Box (23.09.2026).
- Vergleiche mit Deutschland, wo es hilft. Erkläre landesspezifische Begriffe beim ersten Auftreten kursiv + deutsche Erklärung.
- Querverweise auf andere neue Kapitel: nenne sie beim Thema, ohne feste Nummer (z. B. „siehe das Kapitel zum Gesundheitssystem in diesem Teil"), da die Nummerierung noch nicht final ist.

## 4. Selbstprüfung
1. `node lint_book.js` kennt deine neuen Dateien eventuell nicht in der Wortziel-Tabelle — das ist normal, prüfe trotzdem auf **✗-Fehler** (Sie-Form, verbotene Zeichen, fehlende Pflichtboxen etc.) und behebe sie. Eine fehlende Wortziel-Referenz ist kein Fehler.
2. Lies dein Kapitel einmal durch: „du"-Form durchgehend, keine erfundenen Zahlen, Beispiele klar fiktiv.

## 5. Abschlussbericht (max. 200 Wörter je Kapitel)
Dateiname · Wortzahl · unsichere Fakten · Konflikte mit Faktenblatt · offene Fragen. Ändere keine andere Datei als deine zugewiesenen Kapiteldateien.
