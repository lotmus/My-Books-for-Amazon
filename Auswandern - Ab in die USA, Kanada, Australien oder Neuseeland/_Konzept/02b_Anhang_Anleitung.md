# ANLEITUNG FÜR ANHANG-AUTOREN

Du schreibst **einen Anhang** des Buchs „Auswandern in die USA“. Anhänge sind Nachschlage-Werkzeuge, keine Kapitel — kürzer, dichter, mehr Tabellen, kaum Fließtext, keine Boxen außer `Stand`. Projektordner: `C:\Users\lomus\OneDrive\My Books for Amazon\Auswandern in die USA`.

## 1. Lesen
1. `_Konzept\00_Buchbibel.md` — Ton, Typografie, Markdown-Subset (gilt auch für Anhänge, außer wo hier abweichend beschrieben).
2. Deinen Auftrag unten in dieser Anleitung (Abschnitt „Deine Aufgabe“, wird dir im Prompt mitgeteilt).
3. Die passende(n) Rohmaterial-Datei(en) in `_Konzept\digests\` — automatisch aus allen 42 fertigen Kapiteln extrahiert. **Das ist Rohmaterial, kein Fließtext**: dedupliziere, ordne, korrigiere offensichtliche Extraktionsfehler (der Glossar-Extraktor zum Beispiel verwechselt gelegentlich einen Halbsatz mit einer Übersetzung — nimm nur, was tatsächlich ein Begriff mit Erklärung ist).

## 2. Format eines Anhangs
```
## Anhang X: Titel

Ein bis drei Sätze Einordnung (kein „Kurz gesagt“, keine Kapitel-Bausteine).

### Abschnitt
Tabelle oder Liste ...

> **Stand:** September 2026. [ein Satz, was sich hier schnell ändert]
```
- **Kein** „Kurz gesagt“, keine `Achtung`/`Spartipp`/`Merke`/`Praxisbeispiel`/`Checkliste`-Boxen (Ausnahme: Anhang A darf `- [ ]`-Kästchen als normale Liste nutzen, ohne Box-Rahmen).
- Tabellen: höchstens 4 Spalten (Buchbibel-Regel gilt weiter).
- Kapitelverweise als „Kapitel N“ (wird automatisch verlinkt).
- Bookmarking/TOC-Erkennung im Buildsystem greift bei Überschriften der Form `## Anhang X: Titel` (X = A–G) — **exakt dieses Format verwenden**, nicht abweichen.

## 3. Selbstprüfung
`node lint_book.js` prüft aktuell nur Kapitel-Dateien (`_K\d+_`) streng; für Anhänge läuft nur die allgemeine Prüfung (Anführungszeichen, Emojis, Sie-Form, Tabellenspalten). Führe sie trotzdem aus: `node lint_book.js Anhang` bzw. der Dateiname-Teilstring, und behebe alle ✗.

## 4. Abschlussbericht (max. 150 Wörter)
Dateiname · Wortzahl · was du aus dem Rohmaterial verworfen/korrigiert hast · offene Fragen. Ändere keine andere Datei.
