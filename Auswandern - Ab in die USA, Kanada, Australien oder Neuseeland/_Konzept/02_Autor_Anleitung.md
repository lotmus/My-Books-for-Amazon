# ANLEITUNG FÜR KAPITEL-AUTOREN

Du schreibst **ein Kapitel** des deutschsprachigen Buchs „Auswandern in die USA – Die Bibel für Umzug, Visum und Ankommen“ (Autor: Lothar J. Musiol). Projektordner: `C:\Users\lomus\OneDrive\My Books for Amazon\Auswandern in die USA`. Kapitelnummer, Dateiname, Wortziel und Faktenblätter stehen in deinem Auftrag.

## 1. Lesen (in dieser Reihenfolge)
1. `_Konzept\00_Buchbibel.md` — **verbindlicher Vertrag**: Ton (sachlich-respektvolles „du“), Typografie, Faktenregeln, Markdown-Subset, Boxen, Kapitel-Bauplan, Fallbeispiel-Personen, Terminologie.
2. **Kapitelbrief** `_Konzept\briefs\K<nn>.md` (z. B. `K05.md`) — dein Kapiteleintrag (Inhalt, Abgrenzung) plus die Liste aller Kapitel für Querverweise. Kapitelnummern sind fest. Die ganze `_Konzept\01_Gliederung.md` ist lang: lies daraus **nur bei Bedarf** einzelne Einträge angrenzender Kapitel, um Doppelungen zu vermeiden.
3. Die dir zugewiesenen **Faktenblätter** in `_Recherche\` (Stand September 2026). Lies zuerst die Rubrik KERNZAHLEN, dann die Details, die du brauchst, dazu „Aktuelle Änderungen“ und „Praxis-Tipps und Fallen“ sowie „Unsicher/Offen“. Faktenblätter sind **Material, kein Text zum Abschreiben**: verarbeite, ordne, erkläre in deiner Kapitelstruktur.
4. Falls vorhanden und thematisch nahe: bereits fertige Kapitel in `manuscript\` (nur überfliegen, für Ton und Vermeidung von Doppelungen).

## 2. Recherche (sparsam: das Nutzungskontingent ist begrenzt)
- **Web-Budget: höchstens 6 Aufrufe** (WebSearch/WebFetch) — nur für Lücken, die im Faktenblatt unter „Unsicher/Offen“ stehen **und** für dein Kapitel wirklich wichtig sind (Zahlen, die Leser zu Entscheidungen bewegen). Das Faktenblatt deckt den Rest; recherchiere nicht noch einmal, was dort belegt ist. Bei Kapiteln ohne Faktenblatt: höchstens 10 Aufrufe, nur für zeitkritische Fakten. Alles andere aus dem Faktenblatt bzw. Standardwissen; Unbestätigtes im Abschlussbericht melden.
- **Arbeite zügig:** Sobald du genug Material hast, schreibe das Kapitel in einem Zug. Keine Zwischenentwürfe, kein mehrfaches Neuschreiben; nach dem Schreiben nur Linter-Korrekturen per Edit (kein erneutes Lesen der ganzen Datei, wenn der Linter grün ist).
- Faktenblatt und eigenes Wissen widersprechen sich → **Faktenblatt gilt**, außer du findest per Web (WebSearch/WebFetch; falls deferred zuerst `ToolSearch` mit `select:WebSearch,WebFetch`) eine neuere Primärquelle. Melde jeden solchen Fall im Abschlussbericht.
- Fehlt ein Faktenblatt für deinen Themenbereich, recherchiere zeitkritische Fakten selbst (Primärquellen bevorzugt, siehe `_Konzept\03_Recherche_Regeln.md`).
- Schreibe **nie** eine Zahl, Frist, Gebühr, Formularnummer oder Rechtsnorm, die du nicht belegen kannst. Lieber „ändert sich häufig, aktuelle Höhe unter …“ als raten.

## 3. Schreiben
- **Ein Kapitel = eine Datei**, komplett mit dem Write-Tool geschrieben, UTF-8, Markdown-Subset laut Buchbibel. Keine Platzhalter, kein „TODO“, keine Kommentare an den Buchleiter in der Datei.
- **Aufbau pro Abschnitt:** Was ist die Regel/Situation → konkretes Beispiel oder Zahl → Kosten und Zeit → die Falle → der nächste Schritt. Wechsle zwischen Fließtext, Liste und Tabelle; vermeide Listenwüsten und Textwüsten.
- **Konkret:** Zahlen mit Stand, Spannen, Formularnamen, Fristen, „so machst du es“-Schritte. Erkläre amerikanische Begriffe beim ersten Auftreten (kursiv, deutsche Erklärung).
- **Vergleich mit Deutschland**, wo er dem Leser hilft (Anmeldung, Kündigungsschutz, Krankenkasse, Schulsystem, Kita usw.).
- **Einstieg** mit einer konkreten Szene, Frage oder Beobachtung, nicht mit einem Allgemeinplatz. Dann die `Kurz gesagt`-Box.
- **Boxen mit Augenmaß:** `Achtung` nur für echte Fallen (2–6), `Spartipp` nur, wo es wirklich spart, `Merke` selten, `Praxisbeispiel` kurz (60–160 Wörter), fiktiv, realistisch, mit Zahlen, mit den Personen aus Buchbibel §7. Jedes Kapitel: `### Plus und Minus`-Tabelle, wo das Thema echte Vor- und Nachteile hat.
- **Ton:** sachlich-respektvolles „du“, trockener Humor sparsam, keine Werbesprache, keine Verharmlosung, keine Panikmache. Politisch umstrittene Themen: Fakten und praktische Folgen, keine Parteinahme.
- **Keine Wiederholung** fremder Kapitel: anreißen und „siehe Kapitel N“ verweisen (Nummern aus der Gliederung).
- **Ende:** `> **Checkliste:**` mit `- [ ]`-Punkten (5–12, konkret, abhakbar), `### Quellen und weiterführende Links` (3–8 offizielle Quellen als Kurzadresse), zuletzt `> **Stand:**`-Box (Datum, was sich schnell ändert).

## 4. Selbstprüfung (Pflicht)
1. Führe im Projektordner aus: `node lint_book.js K<nn>` (z. B. `node lint_book.js K05`). **Behebe alle Fehler (✗)**, bis kein Fehler mehr angezeigt wird. Prüfe Warnungen (·) und beseitige sie, wo sinnvoll (Wortziel ±15 %).
2. Lies dein Kapitel einmal durch: Stimmen Zahlen und Fristen mit dem Faktenblatt? Sind alle Querverweise sinnvoll? Steht irgendwo „Sie“ (Anrede)? Kommen erfundene Anekdoten in Ich-Form vor? Sind Beispiele klar als fiktiv gekennzeichnet?

## 5. Abschlussbericht (max. 200 Wörter, an den Buchleiter)
Dateiname · Wortzahl · **unsichere Fakten** (Liste) · **Konflikte mit Faktenblättern** · verwendete Querverweise · Themen, die in ein anderes Kapitel gehören · offene Fragen an den Buchleiter. Ändere **keine andere Datei** als deine Kapiteldatei.
