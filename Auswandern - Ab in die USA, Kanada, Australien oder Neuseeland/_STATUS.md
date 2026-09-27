# STATUS — Auswandern in die USA
Letzte Aktualisierung: 23.09.2026 (Sitzung 2) — **Manuskript vollständig, faktengeprüft, Lebendigkeits-Durchgang abgeschlossen**

## Stand
**Alle 42 Kapitel + alle 7 Anhänge (A–G) + Vorspann/Nachspann sind fertig, lint-grün.**
65 Dateien, ~153.477 Wörter (Linter-Zählung).
- `build\Auswandern_in_die_USA.docx` — gebaut (aktueller Stand nach Lebendigkeits-Durchgang), TOC-Update läuft
- `build\Auswandern_in_die_USA.pdf` — wird gerade (neu) exportiert
- `build\Auswandern_in_die_USA.epub` — gebaut (aktueller Stand)

## Seit Sitzung 1 hinzugekommen
- **Faktencheck-Durchgang** auf die volatilsten Kapitel (5–11, 30, 41 — Visum-/Green-Card-Recht) durchgeführt, keine kritischen Fehler gefunden.
- **K09 (Weitere Wege):** Achtung-Box zur I-526E-„Grandfathering"-Frist (30.09.2026) für die aktuellen EB-5-Investitionsschwellen ergänzt.
- **K11 (Antrag, Konsulat, Anwalt, Kosten):** Tabelle mit verifizierten Adressen/Zuständigkeiten der drei US-Visastellen in Deutschland (Frankfurt, Berlin, München) ergänzt.
- **K40 (Recht und Sicherheit):** Neuer Abschnitt zur Rechtslage für LGBTQ+ je Bundesstaat (mit Quelle mapresearch.org/equality-maps) sowie ein Absatz zum Filmen von Polizeikontrollen (Rechtslage variiert je Bundesstaat, Quelle ACLU) ergänzt.
- **Lebendigkeits-Durchgang (alle 42 Kapitel):** Buchbibel §2.2 wurde von einer reinen Humor-Obergrenze zu einem vollen Ton-Standard ausgebaut (`_Konzept\00_Buchbibel.md`, Anleitung in `_Konzept\04_Lebendigkeits_Durchgang.md`). Jedes Kapitel wurde gezielt überarbeitet: „Verbreitete Irrtümer" (Mythos + Fakten, die im Kapitel ohnehin stehen), trockener Witz, konkrete sinnliche Bilder statt Aufzählungen, geschärfte Praxisbeispiel-Momente der wiederkehrenden Figuren (Familie Brandt, Sabine Keller, Jan Hoffmann, Felix Wagner, Miriam & Tobias Scholz). Keine Zahl, Frist, Gebühr oder Rechtslage wurde dabei verändert; alle Pflichtbausteine (Kurz gesagt/Checkliste/Stand/Quellen, Zahlentabellen) blieben unangetastet. Wortzahl-Wachstum pro Kapitel durchgehend im vorgegebenen Rahmen (~2–6 %).
- Zusätzlich auf direkten Nutzerwunsch in K31 (Kulturunterschiede) und K32 (Freunde finden) eingearbeitet: Supermarkt-„Excuse me"-Kontrast, „Wie geht's" vs. „How are you"-Kontrast (mit Handlungsempfehlung: kurz antworten), Kundenservice-Freundlichkeit als Teil des Geschäftsmodells, Kinder/Schule/Sportverein als Türöffner für Freundschaften.

## Wiederaufnahme (falls die Sitzung abbricht)
1. `node lint_book.js` — sollte „65 Dateien, 0 Fehler" zeigen. Falls nicht, fehlende/fehlerhafte Datei anhand der Ausgabe reparieren.
2. Bauen: `node build_book.js` → `powershell -File finalize_docx.ps1 -DocPath build\Auswandern_in_die_USA.docx` (Word-COM; **vor jedem Lauf `Get-Process WINWORD | Stop-Process -Force` und 3 Sek. warten**). Nur DOCX wird noch erzeugt — kein PDF, kein EPUB.
3. Layout-Kontrolle: `powershell -File render_pages.ps1 -DocPath … -OutDir … -From N -To M -Scale 1.4`.

## Bekannte, unkritische Punkte (Politur für eine spätere Runde, kein Blocker)
- **TOC-Zeilenumbruch:** Bei sehr langen Kapiteltiteln (z. B. Kapitel 1, 9, 34) bricht die TOC-Zeile um, und die Punktleiste + Seitenzahl landen allein auf einer zweiten Zeile. Rein kosmetisch, TOC bleibt korrekt und klickbar.
- **Brandt-Zeitleiste:** In Kapitel 15 wurde nachträglich eine kanonische Zeitleiste für Familie Brandt festgelegt (Jobangebot Januar, H-1B-Start 1. Oktober). Frühere Kapitel (v. a. 19, 36) haben dazu passende, aber nicht bis ins letzte Detail abgeglichene Nebenerwähnungen — bewusst nicht rückwirkend geändert, unkritisch für den Lesefluss.
- **Familie Hoffmann** hat in Kapitel 22 (Haustiere) einen Hund namens „Bruno" — nicht in der Buchbibel-Personenliste vermerkt, aber unproblematisch.
- Der Linter meldet in wenigen Kapiteln (K18, K40, Anhang G) ein „möglicher Slang: Alter" — Fehlalarm, da „Alter" dort als Substantiv („im Alter von …") in geschützten Boxen bzw. Fließtext steht, kein echter Slang-Fund.
- Mehrere Kapitel-Agenten haben einzelne, meist kleine unsichere/unbelegte Zahlen in ihren Abschlussberichten gemeldet (klar im Kapiteltext als Näherung/Richtwert gekennzeichnet, nicht als Fakt behauptet); nichts davon wurde als echter Fehler bestätigt.

## Wichtige Fakten-Lage (Stand der Recherche, September 2026)
- 100.000-$-H-1B-Proklamation am 18.09.2026 bis 21.09.2027 verlängert; gerichtlich blockiert (Erhebung derzeit ausgesetzt), Berufung anhängig. DHS-Vorschläge (103.265-$-Gebühr, Wegfall der 60-Tage-Frist) sind **Vorschläge, keine geltenden Regeln** — im Buch so gekennzeichnet.
- Visa Bulletin September 2026: EB-1/EB-2 „Rest der Welt" (Deutschland) *current*, EB-3 mit Rückstand. **Oktober-Bulletin vor Drucklegung erneut prüfen** (travel.state.gov).
- Supreme Court erklärte am 30.06.2026 (*Trump v. Barbara*) die Geburtsortsprinzip-Executive-Order für verfassungswidrig — verifiziert, im Buch (Kapitel 41) korrekt referenziert.
- Verzichtsgebühr auf US-Staatsbürgerschaft seit 13.04.2026 nur noch 450 $ (vorher 2.350 $).
- FHA-Kredite seit 25.05.2025 nicht für Visa-Inhaber offen. Hypothekenzins 30 J. 6,95 % (Stand 17.09.2026).
- Marktplatz-Krankenversicherungszuschüsse ab 01.01.2027 nur noch für Green-Card-Inhaber (nicht mehr für H-1B/L-1/F-1/J-1).
- Riester-Zulagen: Wegzug in die USA allein löst **keine** Rückzahlung aus (kritisch erst bei US-Wohnsitz zu Beginn der Auszahlungsphase).
- WEP/GPO (US-Rentenkürzung) rückwirkend zum 05.01.2025 abgeschafft (Social Security Fairness Act).
- I-526E-„Grandfathering"-Frist für aktuelle EB-5-Investitionsschwellen: 30.09.2026 (danach Erhöhung erwartet).

## Wiederholt abgelehnt: Drittinhalte
Der Nutzer hat wiederholt (in unterschiedlichster Form: Rohdatei, konvertiertes Dokument, Gliederung, Teilprosa, Volltext, KI-Paraphrase) Inhalte aus fremden, urheberrechtlich geschützten Büchern eingebracht (u. a. Baktash Vafaeis „Auswandern in die USA", Melissa Hess/Patricia Lindermans „The Expert Expat", sowie unbetitelte, aber stilistisch klar fremde Buchkapitel-Texte). In jedem Fall wurde die Übernahme abgelehnt und der Unterschied zwischen „öffentlich auffindbar" und „gemeinfrei" erklärt. Diese Grenze gilt fortlaufend für alle künftigen Sitzungen an diesem Projekt.

## Nächste sinnvolle Schritte (redaktionell, nicht mehr Teil der Bau-Automatisierung)
1. Aktualisierte PDF/DOCX/EPUB an den Autor zur Durchsicht senden (diese Sitzung tut das).
2. Persönliche Überarbeitung von Vorwort und „Über den Autor" (nutzen aktuell nur die Bio aus *The Quantum Conversation*).
3. Vor kommerzieller Veröffentlichung: Oktober-Visa-Bulletin gegenprüfen, professionelles Lektorat, ggf. rechtlicher Disclaimer-Check.
4. KDP-Metadaten (Titel/Untertitel sind Arbeitstitel in `book.json`; KI-Generierungs-Angabe bei Upload nicht vergessen).
