# Prüfbericht ICE 2976 – REV11 Werkstattfassung

**Prüfgegenstand:** `ICE_2976_Umbauanleitung_REV11_WERKSTATTFASSUNG.pdf`
**Prüfdatum:** 11.09.2026
**Art:** forensische, adversariale Dokumentprüfung. Das ist keine Hardwarefreigabe. Es wurden keine Messwerte erfunden, keine Firmwarestände angenommen und keine Herstellerantworten unterstellt.

---

## 0. Datei und Methode

| Punkt | Ergebnis |
|---|---|
| Umfang | 40 Seiten A4, 40 Arbeitskarten |
| Erzeugung | ReportLab, 10.09.2026 22:47 UTC |
| SHA-256 | `3c67f596856f5403eac6f27f1f2512379555d3611749e4a7bd94f817cc7e41cb` |
| Titel | „Bebilderte Werkstattanleitung ohne Händler“ |
| Links | 176 interne Sprungziele, alle korrekt (Linktext gegen Zielseite geprüft); 23 externe Quellen Q1–Q23 |
| Sichtung | alle 40 Seiten als Bild und als Text; Fotos S. 16, 19, 21, 30 vergrößert |

**Konsil**

Drei getrennte Subagenten mit eigenem Kontext; keiner kannte die Ergebnisse der anderen:

- **A:** Quellen- und Behauptungsprüfung, 46 Behauptungen
- **B:** Hardware, Messmethoden, Ausführbarkeit
- **C:** Kürzungsvergleich REV10 → REV11

Alle drei sind dasselbe Sprachmodell. Das ist eine Mehrfachprüfung, **keine** Prüfung durch drei menschliche Fachleute.

**Eigene Gegenprüfung**

Die P1-Befunde habe ich selbst nachgeprüft: Textsuche im PDF sowie CS3-Anleitung, Märklin-CV-Tabelle, JMRI, TrainControl, LoDi und Stummiforum.

**Verifikation des Berichts**

40 zitierte Textstellen wurden maschinell gegen die angegebenen PDF-Seiten geprüft; alle wurden gefunden.

**Evidenzkategorien**

| Kürzel | Bedeutung |
|---|---|
| K1 | Herstelleranweisung |
| K2 | Ableitung aus Norm oder Zeichnung |
| K3 | Softwareimplementierung |
| K4 | Erfahrungsbericht |
| K5 | Annahme |

---

## 1. Kurzurteil

**Die Werkstattfassung ist gut gegliedert und inhaltlich weit überwiegend korrekt, aber mit dem vorgesehenen Eigenweg noch nicht vollständig ausführbar. Kein P0.**

**Stärken (bestätigt)**

- **Aufbau:** 40 Karten mit VORHER / Handgriff / STOPP / WEITER. Quellen stehen in der Fußzeile, die Sprungziele stimmen.
- **Offene REV9-Befunde behoben:** Gegenkopf-Handgriffe mit Dreiwegpunkt (S. 22), Einzelisolation der Trägerlitzen (S. 21/22), Wiederholpflicht nach Umreihen (S. 24), E1-Liste vor dem Erststrom (S. 29), T9-Tastenmatrix (S. 35), Gehäuse-Wiederanschluss (S. 37). Die Märklin-Zeichnung ist jetzt vollständig (S. 31), die Meta-Texte sind entfernt.
- **Herstellerzahlen stimmen:**
  - 60977: 1,1 A / 250 mA / 300 mA / 1,6 A; Sound 1,6 W an 8 Ω
  - CV8 = 131
  - CV52 = 3 (C90)
  - CV51 Bit 4: 0 = verstärkt
  - CV7 = 77 startet die Einmessfahrt
  - Dimmer-Modus 1 / Modus 19
  - 60974 ab Firmware 3.2.0.1
  - LoDi-Belegung O = RT, L = GE, B optional; SJ1 → AUX4, SJ2 → AUX1
  - RCN-121 und RCN-216
  - 60970-Schalter; 150-Ω-Hinweis für Fx micro
- **Kürzung:** Sie ist überwiegend sauber. Motor-Sechserfolge, positive Kontaktproben, Kreuzpfad-Prüfung, CS3-Schreibfallen, E1, T1–T9 und der Gehäuseabschluss sind erhalten.

**Blockierend (P1)**

| ID | Lücke |
|---|---|
| **V-01** | Die Messkarte S. 5 (bestückte Netze) ist für einen Laien nicht ausfüllbar. S. 29 macht sie aber zur Pflicht vor dem Erststrom. Folge: Sackgasse oder Scheinsicherheit. |
| **V-02** | Die Strommessung S. 28 mit Multimeter in der Gleisleitung ist am bipolaren Digitalgleis nicht aussagekräftig. „Begrenzte Versorgung“ ist nirgends festgelegt. Folge: Laststufen können fälschlich freigegeben werden. |
| **V-03** | Die Prüfung der Anlage auf Signal-, Brems- und Boostergrenzen ist beim Kürzen entfallen. Die LoDi-Bedingung „ICE-M-S bei zugbeeinflussenden Signalen“ fehlt. **Das ist ein Rückschritt gegenüber REV10.** |
| **V-04** | Die für S. 6–S. 11 nötigen Decoder-Prüfaufnahmen sind weder im Bestand noch beschrieben. „Ohne Händler“, „nicht vorsorglich kaufen“ und „nicht improvisieren“ zusammen führen dazu, dass G0 nicht erreichbar ist, solange keine passende Aufnahme vorhanden ist. |

**Grenzen dieser Prüfung**

- **Nicht abrufbar:**
  - mDecoderTool3 v3.60 (robots.txt; ersatzweise GB-Handbuch v3.40)
  - die 60941-Beilage als Text (reines Bild-PDF)
  - LoDi-514-Datenblatt
- **Unbelegt, ob der LokPilot 5 M4 MKL einem Märklin-Master folgt:**
  - K1 gibt es nur für ESU/ESU (LokSound 5 ab 5.1.101).
  - K4 gibt es nur mit ESU-LokProgrammer eingerichtet.
  - Der händlerfreie CS3-Weg ist unerprobt. Das Dokument benennt das ehrlich als offen (S. 1).

---

## 2. Die wichtigsten Befunde nach Risiko

| Rang | ID | Prio | Kern |
|---|---|---|---|
| 1 | V-02 | P1 | Strommessung in der Gleis-/RT-Leitung zeigt im DC-Bereich etwa 0; AC ist bandbreitenabhängig → Fehlabnahme der Laststufen |
| 2 | V-01 | P1 | S. 5 verlangt „begründete Sollbereiche“ ohne Schaltplan; die Pflichtzeile S. 29 ist nicht ehrlich abhakbar |
| 3 | V-03 | P1 | Anlagen-Eignung ohne Verfahren; ICE-M-S-Bedingung fehlt; S. 35 lässt schon vor der Anlagenfreigabe Weichen und Kurven befahren |
| 4 | V-04 | P1 | Keine Prüfaufnahme → Vorabtest S. 9–S. 11 nicht ausführbar |
| 5 | V-06 | P2 | Kein Entscheidungspunkt und kein Plan B, falls der Slave auf S. 11 nicht folgt |
| 6 | V-05 | P2 | Pflicht-Firmwarediagnose schreibt CV31/CV32 (widerspricht „kein Probierwert“ S. 9), ohne Bestehenskriterium; ein Update ist ohne Programmer nicht möglich |
| 7 | V-10 | P2 | Hintere LED-Widerstände: Sackgasse; der Weg zur Bestimmung von U max ist beim Kürzen entfallen |
| 8 | V-09 | P2 | Der Gegenkopf wird nie allein bestromt; sein erster Strom erfolgt gemeinsam am Betriebsgleis |
| 9 | V-07 | P2 | SID-Nachweis mit der Mobile Station nicht ausführbar (keine SID-Anzeige) |
| 10 | V-11 | P2 | „Schwarze Struktur“ auf der Stiftleiste: „klären“ ohne Weg. Hersteller LoDi ≠ Händler |

---

## 3. Befunde

Jeder Befund nennt:

- **Ort:** Seite / Karte / Schritt
- **Zitat**
- **Mechanismus** → **Folge**
- **Quelle** mit Evidenzkategorie
- **Status**
- **Ersatz:** Ersatztext oder Prüfschritt
- **Art:** T = Textkorrektur genügt; N = realer Nachweis nötig

In Klammern stehen die Konsil-Kennungen (A-, B-, C-).

### P1

**V-01 · P1 · Messkarte „Bestückte Netze“ ist für einen Laien nicht ausfüllbar** (B-03, C-02, eigene Prüfung)

- **Ort:** S. 5, Felder 3–5 und STOPP; S. 18, VORHER und Schritt 2 (Ringnetz); S. 25/26; S. 29, Zeile „vollständiger Elektronikplan/Ergebnisse S. 5“.
- **Zitat:** „Messparameter: Gerät, Modus, Prüfspannung/-strom …“, „Soll und Abbruch: Begründeter Werte-/Verhaltensbereich“, „Fehlt ein Feld, bleibt diese Messung und die davon abhängige Bestromung offen.“ S. 18: „Revisionsbezogene Herstellerangabe bzw. nachvollziehbar zugeordneter Leiterbahnplan muss je Ring Sollnetz … ergeben.“
- **Mechanismus:**
  - Einen LoDi- oder Märklin-Schaltplan gibt es nicht.
  - Die Ω-Prüfspannung steht selten im Multimeter-Handbuch.
  - REV10 hatte das an einen „fachkundig bestätigten Prüfplan“ gebunden. REV11 legt dieselben Felder dem Anwender selbst vor, ohne Vorgaben.
- **Folge:** Entweder dauerhafter Stillstand vor dem Erststrom, oder geratene Einträge. Dann wird S. 29 abgehakt, obwohl nichts wirksam geprüft ist; etwa ein Schluss Front-VCC gegen MASSE oder Ring bleibt unentdeckt.
- **Status:** bestätigt, drei Instanzen unabhängig.
- **Ersatz – S. 5 als Referenzvergleich:**
  > „**Messparameter fest:** eigenes Multimeter, Ω-Autorange, beide Polungen, Ablesen nach 5 s, immer dasselbe Gerät. **Referenz vor dem ersten Löten** an der losen, unveränderten Platine (LoDi 511 ohne Decoder und Litzen; Märklin-Träger an den freien Litzen; eine unveränderte Wagenleiste gleicher Revision): SW, MASSE, Ring A, Ring B jeweils gegen alle Pads; dazu die Nachbarpaare MOT_L–MOT_R, L_WS–L_RT, LS1–LS2, RT–GE, VCC–L_RT; hinten B/GR, 0/GL, +Ub, LV, LR, GND, +5V, MR, MV, AUX1–4 paarweise; Wagen O–O, L–L, O–L, O–B, L–B. **Soll = Referenzwert** (± Ablesestreuung). **Abbruch:** vorher OL, jetzt Zahl; deutlich kleiner als die Referenz; oder etwa gleich ‚Spitzen zusammen‘ zwischen verschiedenen Netzen. **Kupfer als Soll** nur mit Quelle (z. B. SW–RT bei ICE-M ohne -S). **Ringnetz S. 18:** Ring gegen jedes Pad messen; ‚wie Spitzen zusammen‘ gegen MASSE = Massering; niedrig gegen ein anderes Pad = Signalnetz, darf kein Metall berühren.“

  Dazu ehrlich benennen: Werksfehler der Platine erkennt der Vergleich nicht. Sie fallen erst beim strombegrenzten Erststrom auf (V-02). Die Zeile S. 29 lautet dann: „Referenz- und Nachher-Reihe vollständig, ohne Abweichung.“
- **Art:** T + N.

---

**V-02 · P1 · Strommessung am Digitalgleis ungültig; „begrenzte Versorgung“ undefiniert** (A-01, B-02, C-02, eigene Prüfung)

- **Ort:** S. 28, Grafik „QUELLE – A-METER – LAST“, Schritte 1–4; S. 29, Zeile „Erste konkrete Laststufe“; S. 33/34 „begrenzter Prüfaufbau“.
- **Zitat:** „Strommessung nur in einen vorher spannungslos geöffneten Pfad in Reihe … Einzel-AUX, Licht/AUX-Summe und Gesamtstrom getrennt bewerten.“ / „Auch der erste Standtest braucht eine begrenzte, geeignete Versorgung.“
- **Mechanismus:**
  - Das Gleissignal ist bipolar und gleichanteilsfrei (RCN-210). Der Laststrom in der Gleis- oder RT-Zuleitung wechselt jede Halbperiode die Richtung.
  - Im DC-A-Bereich zeigt das Multimeter deshalb etwa 0, egal wie groß die Last ist.
  - Im AC-Bereich misst es nur mit Echt-Effektivwert und ausreichender Bandbreite (Grundwelle im kHz-Bereich) richtig; das kann ein Laie nicht feststellen.
  - Aus dem Gesamtstrom lassen sich Einzel-AUX und Licht-Summe nicht trennen.
  - Die geforderte „Einschaltspitze“ ist mit einem Handmultimeter nicht messbar.
- **Folge:** Scheinbar niedrige Werte führen zur Freigabe von Laststufen und Wagenzahl, obwohl 300 mA (Licht + AUX) oder 1,6 A überschritten sein können.
- **Quelle:** RCN-210 (K2). Märklin CS3-Anleitung 17-02 (K1):
  - „Gleisanschluss (max. 5 A)“, „Programmiergleis-Anschluss (max. 1,5 A)“
  - „GFP3 – Daten: Aktuell an Haupt- und Programmiergleis anliegende Stromstärke“ (S. 33; Systemeinstellungen → Gleis-Einstellungen → GFP3-Daten)
  - Märklin 60977-Beilage S. 6 (K1): „Modell noch ohne Gehäuse auf dem Programmiergleis einer Prüfung unterziehen.“
- **Status:** bestätigt für den DC-Bereich; für den AC-Bereich geräteabhängig und wahrscheinlich unzuverlässig.
- **Ersatz S. 28:**
  > „**Kein Multimeter in die Gleis-, B- oder RT-Zuleitung.** Gesamtstrom an der CS3 unter Systemeinstellungen → Gleis-Einstellungen → GFP3-Daten ablesen: zuerst Leerwert ohne Fahrzeug, dann je Stufe; Differenz notieren. **Begrenzte Versorgung = CS3-Programmiergleisausgang** (Märklin: max. 1,5 A) für den ersten Strom jedes Kopfes. **Innenlicht/AUX:** Multimeter im DC-mA-Bereich in Reihe in die GE-Litze hinter dem Decoder (dort fließt Gleichstrom); Ausgang ungedimmt, sonst Mittelwert. **Hintere LEDs:** rechnerisch aus gemessener Gleichspannung am +Ub und dem Widerstand. ‚Einschaltspitze‘ streichen; Kriterium: CS3 schaltet beim Einschalten nicht ab. **Abbruch:** Kurzschlussmeldung; Strom steigt ohne Bedienung; Innenlicht-Differenz nahe 250 mA.“
- **Art:** T.

---

**V-03 · P1 · Anlagen-Eignung ohne Verfahren, ICE-M-S-Bedingung fehlt – Rückschritt gegenüber REV10** (B-01 als P0 unter Bedingung, C-01)

- **Ort:** S. 6 („Im späteren Zug“), S. 35 Schritt 4, S. 37 Zeile „Freigegebener einheitlicher Anlagenbereich“, S. 39 STOPP und „Bis zur eigenen Anlagenabnahme“.
- **Zitat:** „keine Grenze zu Programmiergleis, anderem Booster, Brems-/Analogabschnitt überbrücken“ / „Vorgesehene Kurven und Weichen langsam befahren“ / „ICE beaufsichtigt und von Hand anhalten“.
- **Mechanismus:**
  - RT verbindet beide Schleifer fest; jede Mittelleiter-Trennstelle wird überbrückt.
  - REV10 0a-3/0a-4 hatte ein Verfahren („Signale nach ihrer elektrischen Wirkung eintragen … bei unbekannter Wirkung gesperrt“). In REV11 ist es entfallen; „ICE-M-S“ steht nur noch im Quellentitel S. 40.
  - Die vorhandene Platine ist ohne Relais, also die Variante ohne Schleiferumschaltung (S. 16 „K1: unbestücktes Relaisfeld“).
- **Bedingung:** Auf der befahrenen Anlage gibt es ein signalabhängig stromloses Halteabschnittsstück, ein Bremsmodul, einen Booster oder ein angebundenes Programmiergleis.
- **Folge:** Eine im abgeschalteten Abschnitt stehende Lok fährt unbeaufsichtigt an, der ICE überfährt Rot, und über Kupplungen und O-Bahnen fließen Querströme.
- **Quelle:** LoDi Motor-WiB ICE-M (K1): „Sollten Sie jedoch noch Signale verbaut haben, die den Zug beeinflussen, müssen Sie die LoDi-Motor WiB ICE-M-S verwenden.“
- **Status:** Verlust bestätigt; ob die Anlage betroffen ist, ist offen. Deine geplante CS3-Bremsung ohne stromlose Abschnitte wäre zulässig.
- **Priorität P1 statt P0:** Das Verbot steht im Text (S. 6/39). Die Gefahr entsteht durch das fehlende Verfahren, nicht durch eine falsche Anweisung.
- **Ersatz – neue Karte „Anlage vor dem ersten Zugbetrieb“:** Sie liegt vor S. 35 Schritt 4, und S. 37 verweist auf sie.
  > „1. Je Signal Anschlusskabel verfolgen; Mittelleiter-Trennstellen am Standort suchen. 2. Anlage stromlos; Signal Rot: Ω zwischen Mittelleiter des Halteabschnitts und davor; Signal Grün: wiederholen. OL bei Rot und niedrig bei Grün = zugbeeinflussend. 3. Programmiergleis als Anlagenteil? Booster? Bremsmodule? eintragen. 4. Gibt es einen zugbeeinflussenden Abschnitt oder eine Grenze: dort nicht fahren; entweder Abschnitt dauerhaft digital speisen (Halt nur über CS3 nach S. 39) oder LoDi ICE-M-S (eigener geprüfter Aufbau). Bis dahin nur getrenntes Prüfgleis. S. 35 Schritt 4 nur auf dem Prüfgleis oder in dem nach dieser Karte freigegebenen Bereich.“
- **Art:** T + N (Anlagenbestand).

---

**V-04 · P1 (bedingt) · Die Decoder-Prüfaufnahmen fehlen; G0 ist mit dem Eigenweg nicht erreichbar** (B-04)

- **Ort:** S. 1 („Vor dem elektrischen Zugumbau den Decoder-Vorabtest auf S. 11 abschließen“); S. 2, Geräteliste „Prüfaufnahme(n) ______“; S. 6; S. 9, VORHER; S. 11, VORHER.
- **Zitat:** „Keinen davon ungeprüft anschließen oder vorsorglich kaufen.“ / „Keine Widerstands-Ersatzlast improvisieren.“ / „zwei geeignete getrennte Aufnahmen mit getrennten Lasten“.
- **Mechanismus:**
  - Der 60971 hat nur USB und keinen Gleiseingang.
  - 60970 und 53900 werden nur als „Bestand prüfen“ erwähnt.
  - Keine Karte sagt, wie der ESU ohne Motorlast quittiert (RCN-216: mindestens 60 mA für 5–7 ms) oder wie zwei gleisgespeiste Aufnahmen entstehen.
- **Bedingung:** Weder ein Märklin 60970 noch ein ESU 53900 noch ein gleichwertiger Prüfaufbau ist vorhanden (dein Bestand ist hier nicht dokumentiert).
- **Folge:** Sackgasse an der ersten Pflichtschwelle, oder improvisierte Aufbauten mit Kurzschlussrisiko am Decoder.
- **Quelle:** Q18 Märklin 60970 (K1, S. 24–25: Umschalter AUX3/AUX4 Logik/verstärkt, Motor/Funktion, Lautsprecher 8/100 Ω); Q19 ESU 53900; RCN-216 (K2).
- **Status:** bestätigt als Textlücke; der Bestand ist offen.
- **Ersatz auf S. 2/S. 6:**
  > „Für S. 9–S. 11 brauchst du je Decoder eine gleisgespeiste 21MTC-Prüfaufnahme mit Motor-, Licht- und Lautsprecherlast (z. B. Märklin 60970 oder ESU 53900, jeweils Schalterstellung nach Anleitung). **Ist keine vorhanden, beginnt der Zugumbau nicht** – dann ist eine bewusste Beschaffungsentscheidung nötig; das ist kein Händlerauftrag.“
- **Art:** T + Bestandsfeststellung.

### P2

**V-05 · P2 · Pflicht-Firmwarediagnose ohne Nutzen und im Widerspruch zu S. 9** (A-03, C-06)

- **Ort:** S. 10, Kasten „ZUERST: FIRMWAREDIAGNOSE“; S. 9, Untertitel „Es wird kein Probierwert geschrieben“; S. 29, Zeile „Firmware“.
- **Mechanismus:**
  - Um die Firmware zu lesen, müssen CV31 = 0 und CV32 = 255 geschrieben werden. Das sind zusätzliche Schreibvorgänge im sofort schreibenden CS3-Editor; REV10 F.11.2 hatte das ausdrücklich „nicht ausführen“.
  - Das Ergebnis hat kein Bestehenskriterium: Für LokPilot 5 plus Märklin-Master gibt es keine Mindestfirmware (ESU K1 nennt nur LokSound 5 ab 5.1.101).
  - Eine „gemeldete Updateanforderung“ ist ohne LokProgrammer-Hardware nicht umsetzbar.
  - Auf der Schreibkarte fehlen die CV8-Warnung und „Hex nicht dezimal eintippen“.
- **Quelle:** JMRI v4decoderInfoCVs.xml (K3): 0.255.285:2 Build, 0.255.287 Minor, 0.255.288 Major. Kein ESU-K1-Beleg.
- **Status:** bestätigt.
- **Ersatz:**
  > „Firmwarediagnose optional, nur dokumentierend; kein Bestehenskriterium. Maßgeblich ist der Funktionsnachweis S. 11. Liste A enthält ausschließlich CV31/CV32 (keine CV8-Zeile), Werte nur per Zifferneingabe; nach Unterbrechung CV31/32 zuerst frisch lesen; zurückstellen und rücklesen vor jeder anderen Aktion. ‚Firmware nicht lesbar‘ = offen, kein Reset, kein Update.“

  S. 29 bekommt für die Firmware die Zeile „dokumentiert oder ‚nicht lesbar‘“. Den Untertitel auf S. 9 behalten, S. 10 als Ausnahme kennzeichnen.
- **Art:** T.

---

**V-06 · P2 · Kein Entscheidungspunkt und kein Plan B, wenn der Slave nicht folgt** (eigene Prüfung)

- **Ort:** S. 11 STOPP; S. 38, Zeile „Slave folgt nicht“.
- **Mechanismus:**
  - Die Ziele 1–3 (ein Zug, kein zweiter Eintrag, keine Traktion) hängen vollständig an der Synchronisation.
  - Belegt ist nur ESU/ESU (K1) und, für genau dieses Paar, eine Einrichtung per ESU-LokProgrammer (K4, Stummiforum MTB-Ontour: „mit dem ESU-Programmer als Slave zum msd3 eingerichtet“).
  - Der händlerfreie CS3-Weg ist unerprobt. Scheitert S. 11, bietet die Anleitung nur Fehlersuche an.
- **Folge:** Unbegrenzte Versuchsschleifen am Decoderpaar, jeweils mit CV-Schreibvorgängen.
- **Status:** bestätigt.
- **Ersatz S. 11 und S. 38:**
  > „Folgt der Slave nach zwei vollständig dokumentierten Versuchen (Originalexport S. 8, frisch rückgelesene Werte S. 10) nicht: Eigenweg beenden. Optionen: (a) LokProgrammer 53451 für Auslesen/Einrichtung (einzig praxisbelegter Weg, K4); (b) schriftliche ESU-Auskunft zu LP5 + Märklin-Master; (c) Architektur ändern. Kein weiteres Probieren am Paar.“
- **Art:** T.

---

**V-07 · P2 · Der SID-Nachweis ist mit der Mobile Station nicht ausführbar** (A-13, eigene Prüfung)

- **Ort:** S. 11, Schritte 4 und 5; WEITER.
- **Zitat:** „Nachweisen: gleiche mfxuid, tatsächlich andere SID“ / „Ohne SID-Anzeige einen konkret bestätigten passiven Datennachweis verwenden“.
- **Mechanismus:**
  - Die Mobile Station zeigt keine SID. Welcher „passive Datennachweis“ gemeint ist, bleibt offen.
  - Dass eine andere Zentrale eine andere SID vergibt, ist nicht belegt (Q15 belegt nur Bind/Verify).
  - Die Gleisbox mit Mobile Station als eigenständiges System ist dagegen belegt (Q16 K1).
- **Folge:** G0 bleibt formal offen, oder der Anwender hakt „anders“ ohne Beleg ab.
- **Status:** bestätigt.
- **Ersatz:**
  > „SID alt: aus der CS3-Sicherung/Datensatz (Feld `.sid`). Nach Rückkehr zur CS3 den Datensatz erneut sichern und vergleichen. Ist die SID am Zweitsystem nicht ablesbar, gilt der Wechseltest als ‚Slave folgt nach Neuanmeldung an Fremdsystem – SID-Wechsel nicht belegt‘ und wird so dokumentiert; kein erfundener Nachweis.“
- **Art:** T + N.

---

**V-08 · P2 · CS3-Datenzugang per HTTP unbelegt; falscher Feldname** (A-02)

- **Ort:** S. 7, Schritte 3 und 4.
- **Zitat:** „Alternativ im Browser … http://<CS3-IP>/config/lokomotive.cs2 öffnen … reiner Lesezugriff“ / „sid beziehungsweise address“.
- **Mechanismus:**
  - Q14 ist nur eine Testdatei; sie zeigt `.uid=0x4027`, `.mfxuid=0x73f1fcc5`, `.adresse=0x27`, `.sid=0x27` (von mir eingesehen).
  - Laut Konsil A (K3, TrainControl-Quellcode) liest TrainControl an der CS3 die Web-API `/app/api/loks` (vor 2.6.0) bzw. `/app/api/locos` (ab 2.6.0), nicht `/config/lokomotive.cs2`. Den Quellcode habe ich selbst nicht nachgelesen.
  - Der Feldname heißt `.adresse`, nicht „address“.
- **Folge:** Fehlerseite oder vergebliche Suche; kein Hardwarerisiko.
- **Status:** Aussage nicht belegt.
- **Ersatz:**
  > „Primärweg: CS3-Sicherung (S. 7/2) als Kopie auswerten. Ob die CS3 /config/lokomotive.cs2 per HTTP ausliefert, ist nicht belegt. Feldnamen im CS2-Format: `.mfxuid`, `.uid`, `.sid`, `.adresse` (Hex mit 0x; nichts kürzen).“
- **Art:** T.

---

**V-09 · P2 · Der Gegenkopf wird nie allein bestromt** (C-04, B-02)

- **Ort:** S. 33, Schritt 1 (stromlos) → Schritt 2 (beide Köpfe gemeinsam am Betriebsgleis); Laststufe „Gegenkopf“ S. 28/2 wird nicht eingelöst.
- **Mechanismus:** Anders als REV10 (17/54: „zuerst einzeln, dann gemeinsam“) bekommt der Gegenkopf seinen ersten Strom gleich zusammen mit dem Master und am ungedrosselten Gleisausgang (bis 5 A).
- **Folge:** Ein Verdrahtungsfehler hinten lässt sich nicht getrennt eingrenzen und trifft den vollen Ausgang.
- **Status:** bestätigt.
- **Ersatz – neuer Schritt S. 33/1a:**
  > „Gegenkopf allein (Motorseite vom Gleis) auf den CS3-Programmiergleisausgang, Fahrstufe 0, STOP aufheben. GFP3-Strom notieren (Differenz zum Leerwert), keine Wärme/Geruch, CS3 schaltet nicht ab. Ohne Master reagiert F0 nicht – kein Fehler. Erst danach Schritt 2.“
- **Art:** T.

---

**V-10 · P2 · Hintere LED-Widerstände führen in eine Sackgasse** (B-06, C-07, A-12)

- **Ort:** S. 17, Tabelle „U maximal am LED-Zweig“ und STOPP „Keine festen Widerstandswerte … freigegeben“.
- **Mechanismus:**
  - Zulässiger Strom und Flussspannung des LoDi-514 sind für den Anwender nicht belegbar (Q5 nennt nur „ohne Vorwiderstände“).
  - Der REV10-Hinweis zu U max ist entfallen: „kein AC-Wert am Gleis; O/RT-Spannung ≠ LED-Zweig; nicht an 21MTC-Pins messen“.
  - Ohne Widerstand kann S. 29 nicht abgehakt werden.
- **Quelle:** LoDi betreibt denselben 514-Einsatz vorn über R4/R5 an Decoder-U+ (K1/K2). ESU-Richtbereich 470 Ω–2,2 kΩ (Q6 S. 28–29, K1).
- **Status:** bestätigt.
- **Ersatz:**
  > „Referenz: Aufdruck von R4/R5 der eigenen LoDi 511 ablesen (z. B. 2201 = 2,2 kΩ) und Zweig L_WS/L_RT zuordnen. Hinten je Farbe mindestens denselben Wert, Belastbarkeit ≥ 0,25 W. Kontrolle mit S. 17-Formel, U max = dokumentierter Höchstwert der Versorgung (kein AC-Gleiswert). Unleserlich: bei LoDi erfragen.“
- **Art:** T + N (Aufdruck).

---

**V-11 · P2 · „Schwarze Struktur“ auf der Stiftleiste: Sackgasse ohne Klärungsweg** (B-05; eigene Vergrößerung bestätigt das Bild)

- **Ort:** S. 16 Nr. 1; S. 30, Bild und STOPP.
- **Zitat:** „Nichts abziehen … Decoder abgezogen lassen, genaue Revision und sichtbares Indexmerkmal klären.“
- **Mechanismus:**
  - Eine flache schwarze Fläche verdeckt die mittleren 5 von 11 Spalten, wahrscheinlich eine Bestückungskappe.
  - Mit Kappe kann der Decoder nicht aufgesteckt werden; die Stifte müssen von unten durch die Decoderplatine (RCN-121).
  - Wer klären soll, steht nicht da. Der Hersteller LoDi ist kein Händler.
- **Status:** wahrscheinlich.
- **Ersatz:**
  > „Makrofotos von oben und seitlich an den Hersteller LoDi senden (Kontakt auf lokstoredigital.de). Frage: Bestückungskappe? Entfernen wie? Erst nach Herstellerantwort weiter.“
- **Art:** T + N.

---

**V-12 · P2 · „Restenergie ausschließen“ ohne Handgriff** (B-07)

- **Ort:** S. 3 Schritt 1; S. 4/S. 5 VORHER; S. 23 VORHER; S. 29; S. 36.
- **Mechanismus:** LoDi sieht an der Wagenplatine C1/C2 für einen Stützelko vor („ab 100 µF … optimal 330 µF 25 Volt“, K1). Einen Entladehandgriff gibt es nicht. Eine Restspannung verfälscht Ω-Werte.
- **Ersatz:**
  > „Nach dem Abschalten 1 min warten; Multimeter V DC direkt an beiden Elko-Anschlüssen; über 0,5 V: 1-kΩ-Widerstand mit zwei isolierten Clips 10 s parallel, nachmessen. Nie mit Draht kurzschließen.“
- **Art:** T.

---

**V-13 · P2 · „Alleinige hintere Speisung“ verlangt Umlöten, das Kriterium ist nicht messbar** (B-10)

- **Ort:** S. 28, Schritt 4.
- **Mechanismus:** Die SW-Zuleitung an der LoDi abzulöten riskiert, dass sich das Pad löst, und erzwingt die volle Wiederholprüfung. „Spannungseinbruch“ ist am bipolaren Signal nicht messbar (V-02).
- **Ersatz:**
  > „Nicht umlöten: Mittelleiter-Punktkontakte des Gleisstücks unter dem Motorkopf mit Isolierband abdecken (Außenschienen bleiben). Kriterien: kein Flackern, kein Sound-Neustart, GFP3-Strom unverändert; nach 10 min höchster Standlast stromlos Kupplungen/Wagenleisten auf Erwärmung prüfen.“
- **Art:** T + N.

---

**V-14 · P2 · Freie, spannungsführende Kupplungskontakte ab S. 33/34** (B-13)

- **Ort:** S. 33, Schritt 2; S. 34, Schritt 1.
- **Mechanismus:** S. 32 isoliert die freien Kupplungsenden des Motorkopfs. S. 33 sagt nichts zu RT am Gegenkopf (rohes Gleissignal). S. 34 sagt nichts zum freien Wagenende, wo O (RT) und L (GE) nebeneinander liegen. Eine Metallbrücke zwischen beiden legt Gleisspannung auf AUX4.
- **Ersatz:**
  > „Freie Kupplungskontakte beider Köpfe und des jeweils letzten Wagens einzeln isolieren; ungekuppelte Köpfe mit Abstand; nie Metall auf dem Prüfgleis.“
- **Art:** T.

---

**V-15 · P2 · Rückmeldetest S. 26/6 steht vor der Erststromfreigabe** (C-08)

- **Ort:** S. 26, Schritt 6.
- **Zitat:** „Nach elektrischer Abnahme darf nur der Testwagen den zugehörigen Meldeabschnitt belegen“.
- **Mechanismus:** Die Karte liegt vor S. 28–S. 33. Der REV10-Zusatz „im nach Kapitel 17 freigegebenen Zug … auf demselben CS3-Stromkreis“ fehlt. Der bestromte Zug kann so auf Kontaktgleisen der Anlage stehen, bevor Laststufen und Anlagenbereich freigegeben sind.
- **Ersatz:**
  > „Schritt 6 erst nach S. 37 und nur im nach der Anlagenkarte (V-03) freigegebenen Bereich …“
- **Art:** T.

---

**V-16 · P2 · Sackgasse von S. 36 nach S. 37** (B-11)

- **Ort:** S. 36, Schritt 3 („Gibt es keinen sicheren Austritt, bleibt diese geschlossene Messung offen“) gegenüber S. 37 VORHER („S. 36 bestanden“).
- **Ersatz:**
  > „Ohne sicheren Leitungsaustritt: geschlossene Reihe an außen zugänglichen Punkten (Schleifer B, Rad 0, Kupplungskontakte RT/GE) gegen die Referenz V-01; Motorisolation geschlossen gilt über Erststrom am Programmiergleis (V-02) als geprüft; so dokumentieren.“
- **Art:** T.

### P3

| ID | Ort | Befund | Ersatz / Maßnahme | Art |
|---|---|---|---|---|
| V-17 (C-10) | S. 9/3 | Beim Aufheben von STOP kann sich der noch nicht synchronisierte 59649 per M4 selbst an der CS3 anmelden. Die REV10-Warnung und das Loklisten-Foto sind entfallen. | „Vor STOP-Aufheben Lokliste fotografieren; Selbstanmeldung erwartbar; Eintrag nicht fahren, nicht löschen, auf S. 11/33 als ‚alter Eintrag‘ vergleichen.“ | T |
| V-18 (C-12) | S. 11 STOPP | Die Abbruchregel „Überlast/Geruch/unerwarteter Motorlauf“ und „keine Konfiguration im Paartest (auch keine CS3-mfx-Konfiguration am Mastereintrag)“ fehlen hier; sie stehen erst auf S. 33/35/38. | Beide Sätze auf S. 11 übernehmen. | T |
| V-19 (C-11) | S. 9/10 | Tabelle „reale DCC/MM-Adressen und Protokolle“ (REV10 F.11.3) entfallen; Serviceeintrag bleibt stehen. | „DCC-/MM-Adressen beider Decoder notieren und mit Bestand abgleichen; Serviceeintrag auf unbenutzte Adresse; DCC am 59649 nicht abschalten (einziger Wartungsweg).“ | T |
| V-20 (C-03, entschärft) | S. 27/2–3 | Die ÷16-Methode für Bit 4 ist entfallen. Laut Märklin-CV-Tabelle hat CV51 nur Bits 0–4 (Werte 0–31); dann gilt „Wert ≥ 16 ⇔ Bit 4 gesetzt“. Ein Fehlgriff ist nur bei undokumentiertem Wert > 31 möglich. | „CV51 = 16–31 → 16 abziehen; 0–15 → unverändert; > 31 → STOP (undokumentiert).“ Vorzugsweg über das mDT3-Projekt bleibt. | T |
| V-21 (C-09) | S. 9/10 | ESU-Einmessfahrt „CV54 = 0 und danach F1“ nicht mehr genannt. | In beiden STOPP-Kästen ergänzen. | T |
| V-22 (C-05) | S. 39/2 | „60977-Firmware … bestätigen“ ohne „nur auslesen (Wert von S. 7); CV7 nie beschreiben“; „nie zwei Puffer hintereinander“ fehlt. | Ergänzen. | T |
| V-23 (B-14, eigene Prüfung) | S. 32/5 | Bei falscher Richtung wird Umlöten vorgeschrieben. Märklin-CV-Tabelle: **CV51 Bit 0 „Motoranschluss tauschen“** betrifft nur den Motor, nicht Licht oder Richtung, und damit auch nicht die Synchronisation. Die Karte verbietet „CV-Invertierung“ pauschal. | Als dokumentierte Alternative zulassen: im mDT3-Projekt setzen, rücklesen; CV29 Bit 0 bleibt verboten (würde Licht und Slave-Bezug umkehren). | T |
| V-24 (A-09, B-12) | S. 20/1–2 | „Nennimpedanz aus Setunterlagen“: Q1 nennt für die Satz-Lautsprecher keine Impedanz. Der Gegensteckertyp ist für Laien nicht bestimmbar. | Herkunft aus 60977-Satz genügt (Decoder für 4/8 Ω). Alternativ Litzen an den Lötfahnen des Lautsprechers tauschen (reversibel). | T |
| V-25 (B-09) | S. 13 | „Nur den … geeigneten [Quer-Kondensator] belassen“ ist undefiniert. ESU S. 27 (K1): die beiden Kondensatoren von Motoranschluss zu Gehäuse müssen weg, der Querkondensator bleibt. | Präzisieren; optional nF-**Vergleich** (Leerwert gegen PM1–Rahmen) statt der verbotenen Nullprüfung. | T |
| V-26 (C-13) | S. 15/S. 38 | Kohlestaub und Späne als Fehlerursache fehlen. | Zeile ergänzen. | T |
| V-27 (A-07) | S. 9/10 | Offen ist, ob die CS3 bei Eingabe über Regler oder Pfeile Zwischenwerte schreibt; kritisch nur bei CV8. | „Werte nur per Zifferneingabe; CV8 nur in einer reinen Leseliste.“ | T/N |
| V-28 (A-06) | S. 9/10 | Die Menübezeichnungen „Decoder auslesen“ und „Prog.“ stehen nicht in Q9. Ab CS3 2.6.0 bricht ein Listenlesen bei Fehlern nicht ab. | „Menü am eigenen Bildschirm fotografieren; jede Zeile einzeln auf Fehlermarkierung prüfen.“ | T |
| V-29 (A-05) | S. 8 VORHER | „Kein 53451 erforderlich“ ist nur für Software v4.4.0 belegt (Q12). | Am eigenen PC mit LokProgrammer 5.x nachweisen (Bildschirmfoto: LP5-MKL-Projekt, Sonderoptionen, Geänderte CVs). | N |
| V-30 (A-04, A-14, A-08) | S. 6/8/28 | Quellendeckung: Formel S. 8 steht nicht in Q13 (abgeleitet aus JMRI-SplitVariableValue); 0,5 W steht in der 53900-Anleitung, nicht auf Q19; Q17 (RCN-216) trägt keine Laststufen auf S. 28. | Kennzeichnung „abgeleitet (K3)“; Quellenverweise korrigieren. | T |
| V-31 (A-10) | S. 2/12 | 60941 ist laut Märklin für Trommelkollektormotoren; die Motorbauart des eigenen Kopfes wird nicht festgestellt. | „Motorbauart vor Einbau dokumentieren.“ | N |
| V-32 (B-15) | S. 26 | Kontaktgleise melden über Metallradsätze auch ohne B. Die Option ist nur bei Stromfühlern oder für die Lichtmasse sinnvoll. | Zweck und Radsatzart vorher klären. | T/N |
| V-33 (B-16) | S. 16 | „V1.49, Pfad tatsächlich bestätigt → AUX4“: Ohne Messung an den 21MTC-Pins hat der Laie keine Methode. | Bei V1.49 LoDi fragen. | T |

---

## 4. Behauptungs- und Quellenprüfung

Konsil A hat 46 Behauptungen geprüft; die Ergebnisse hier verdichtet und von mir stichprobenartig gegengeprüft.

| Ergebnis | Behauptungen (Seite) |
|---|---|
| **Bestätigt (K1)** | 60970-Schalter (S. 6); 60977 1,6 W an 8 Ω (S. 6, Q1 S. 3 „2,75 W / 1,6 W an 4/8 Ω“); 59649 MKL AUX3/4 verstärkt; CV8 60977 = 131 (Q1 S. 19); 60971 Adapterfolge/nur USB; CS3 schreibt Werte sofort und liest angewählte Zeilen (Q9); ESU CV8 = 151, 8 = Reset; RCN-216 Quittung, Ausführung unabhängig von der Quittung; Mobile Station mit eigener Gleisbox eigenständig; Bind/Verify; LoDi SJ1/SJ2; LoDi-Frontmodule ohne Vorwiderstände (Q5); O = RT / L = GE / B optional (Q4); CV52 = 3 C90; CV51 Bit 4; Dimmer 1 / Modus 19; Grenzwerte; 60974 ≥ 3.2.0.1; Halteplatte im 60977-Satz; 150 Ω nur Fx micro (Q6 S. 25); RCN-121 Pin 11/12/16 |
| **Bestätigt nur als K3** | CV191 = M4 Manufacturer ID, CV192–195 = M4 Seriennummer (JMRI); Firmware-CVs 0.255.285–288 (JMRI v4decoderInfoCVs, von mir eingesehen); Felder `.mfxuid/.uid/.sid/.adresse` (TrainControl-Testdatei, von mir eingesehen) |
| **Teilweise / abgeleitet** | Formel CV192–195 (S. 8); LokProgrammer ohne Hardware (S. 8, nur v4.4.0 belegt); mDT3-Menüs (nur GB v3.40 geprüft); 60941 → C90 (K2); Auswahl der Kondensatoren (LoDi ohne Zuordnung, ESU S. 27 stützt sie) |
| **Nicht belegt** | HTTP-Pfad `/config/lokomotive.cs2` an der CS3 (V-08); Menübezeichnungen „Decoder auslesen“/„Prog.“ in Q9; SID-Wechsel an Fremdzentrale; **LokPilot 5 M4 MKL folgt einem Märklin-Master über CS3-geschriebene CVs** (nur ESU/ESU K1, nur LokProgrammer-Einrichtung K4) |
| **Nicht prüfbar** | 60941-Beilage (Bild-PDF); mDT3 v3.60 (robots.txt); LoDi-514-Daten; Kupplungspassung; alle Messwerte am realen Zug |

---

## 5. Kürzung REV10 (92 S.) → REV11 (40 S.)

**Ergebnis:** überwiegend sichere Kürzung. Die Schnellanleitung G, Kapitel F.8/F.9 und die historischen Debatten waren redundant.

| Status | Regeln |
|---|---|
| **Erhalten** | eine Quelle / getrenntes Prüfgleis; RT-Überbrückungsverbot; G0 vor Zerlegen; 60971 nur 60977, nur USB; CS3-Sicherung nie „Wiederherstellen“; Masterkennung ohne DCC-Adresse/SID; Offline-Differenzexport; Serviceeintrag, PoM aus; CV8 nur lesen; keine Vorlagenwerte; Multimeter COM/V-Ω, nie A zwischen B und 0; Vierpunktfolge; Motor-Sechserfolge; Kappe nicht entfernen; Front-VCC ≠ Pin 12; LED je Farbe mit Widerstand; Dreiwegpunkt hinten; Kreuzpfade je Übergang; B-Pfade; 60974 ab; CV52/CV51/Modus 1; E1; Motorkopf erst am Programmiergleis; T1–T9; geschlossene Prüfung und Wiederanschluss |
| **Entfallen oder abgeschwächt (kritisch)** | Anlagen-Eignung 0a-3/0a-4 (V-03); fachkundige Prüfplanfreigabe ohne ausführbaren Ersatz (V-01); Gegenkopf-Einzelstrom (V-09); U-max-Ermittlung LED (V-10); Rückmeldetest-Zeitpunkt (V-15) |
| **Entfallen (gering)** | Lokliste/Selbstanmeldung (V-17); Paartest-Abbruch- und Konfigurationsregel (V-18); DCC/MM-Adressen (V-19); ÷16-Methode (V-20); CV54 + F1 (V-21); CV7-Hinweis bei 60974 (V-22); Kohlestaub (V-26) |
| **Neu, sinnverändert** | Firmwarediagnose mit Pflicht-Schreibzugriff (V-05); HTTP-Datenzugang (V-08); „131 – Herstellerangabe“ (korrekt als CV8 des 60977; ob ESU-CV191 genau diesen Wert erwartet, zeigt erst S. 8/S. 11) |

---

## 6. Status der REV9-Befunde in REV11

| REV9 | Thema | REV11 |
|---|---|---|
| R-01 | Anlagen-Trennstellen / ICE-M-S | **zurückgefallen** → V-03 |
| R-02 | Messkarte vor Erststrom | S. 4 gut; S. 5 nicht ausführbar → V-01 |
| R-03 | Gegenkopf-Handgriffe | erledigt (S. 21/22) |
| R-04 | Schnellanleitung Isolation | entfallen mit der Schnellanleitung; S. 21/22 erledigt |
| R-05 | Selbstanmeldung 59649 | in REV10 erledigt, in REV11 wieder entfallen → V-17 |
| R-06 | mfx-Konfiguration über SID | teilweise (S. 33/35/38) → V-18 |
| R-07 | F-Tasten am Slave | erledigt (S. 11 Tabelle, S. 35 T9) |
| R-08 | Index-CVs | erledigt (S. 10/2) |
| R-09 | Prüfaufnahme mit Last | erledigt (S. 9 VORHER); Bestand offen → V-04 |
| R-10/R-11 | Firmware / C7 | umgesetzt, aber V-05 / V-07 |
| R-12/R-13 | Gates / E | erledigt (VORHER/WEITER, S. 29) |
| R-14 | Erststrom-Reihenfolge | Motorkopf erledigt; Gegenkopf → V-09 |
| R-15 | Last vor Fahrt | Reihenfolge erledigt (S. 34/35); Methode → V-02 |
| R-16 bis R-21, R-26 bis R-28 | Mapping, Trennregel, Foto-Widerspruch, Kap. 24, Bezeichner, Umreihen, Schnellanleitung | erledigt |
| R-22/R-24 | LoDi-Netze, SW–RT | als Feld vorhanden (S. 5/16); Methode → V-01 |
| R-23 | Kappe | vorsichtiger formuliert; Klärungsweg fehlt → V-11 |
| R-25 | DCC-Adressen | entfallen → V-19 |

---

## 7. Anforderungsmatrix

| Nr. | Nutzerziel | Dokumentiert | Technisch belegt | Getestet | Status |
|---|---|---|---|---|---|
| 1 | Ein automatisch angemeldeter mfx-Zug | S. 7–11, 33 | ESU/ESU (K1); mSD3 + LP5 per LokProgrammer (K4); CS3-Weg unbelegt | nein | **offen** (V-06) |
| 2 | Kein zweiter Loksatz | S. 11, 33 | ESU: konfigurierter Slave meldet sich nicht selbst (K1) | nein | offen (V-17) |
| 3 | Keine Traktion | ja | folgt aus 1 | nein | offen |
| 4 | Märklin-Sound | S. 20, 27, 32 | K1 | nein | offen (Lautsprecher/Adapter) |
| 5 | Weiß/rot an beiden Köpfen im Stand | S. 11, 22, 33, 35 | Mapping schlüssig (K2) | nein | offen (hängt an 1) |
| 6 | LoDi-Front-LEDs | S. 17, 19, 22 | Rechenweg korrekt; hintere Werte gesperrt | nein | offen (V-10) |
| 7 | Innenlicht ohne Richtungsunterbrechung | S. 27, 34 | RT + AUX richtungsunabhängig (K2); LoDi „Aux 4 = Wagenbeleuchtung“ (K1) | nein | Konstruktion schlüssig |
| 8 | Originale Märklin-Kupplungen | S. 2, 24 | nur Teilekandidaten | nein | offen |
| 9 | Keine zusätzliche Steuerleitung | S. 1, 23, 25 | K1/K2 | nein | erfüllt im Konzept; Anlagenbedingung V-03 |

---

## 8. Ablaufübergänge

| Übergang | Wirksam | Lücke |
|---|---|---|
| Vorabtest → Montage | S. 11 als Pflichttor; stromlos, Decoder ab | Prüfaufnahme (V-04); Plan B (V-06); SID (V-07) |
| Montage → Messung | Motor S. 12–15 vorbildlich; S. 4 passive Leiter | Referenz der bestückten Netze vor dem ersten Löten fehlt (V-01) |
| Messung → Programmierung | S. 27 vor Wagenlast; CV51 vor AUX4-Last | Firmwarediagnose (V-05); LED-Werte hinten (V-10) |
| Programmierung → Einsetzen | S. 29 E1, S. 30/31 Index und Sitz | S. 29 wegen V-01/V-02 nicht ehrlich abhakbar; Kappe (V-11) |
| Einsetzen → Erststrom | Motorkopf zuerst am Programmiergleis (S. 32) | Gegenkopf nie allein (V-09); keine Stromanzeige oder Abbruchwerte (V-02); freie Kontakte (V-14) |
| Erststrom → Gehäuseabschluss | T1–T9 klar; Fahrt erst nach Standtest und zugelassener Last | Anlagenbereich ohne Verfahren (V-03); Sackgasse S. 36/37 (V-16) |

---

## 9. Widerlegte oder nicht bestätigte Verdachtsbefunde

| Verdacht | Ergebnis |
|---|---|
| „60977: 1,6 W an 8 Ω“ falsch (Verwechslung mit 1,6 A) | widerlegt – Q1 S. 3: Sound 2,75 W / 1,6 W an 4/8 Ω |
| 150-Ω-Hinweis ohne Quelle | widerlegt – Q6 S. 25 (Fx micro); Fundstelle nur ergänzen |
| Märklin 60970 hat keine solchen Schalter | widerlegt – Q18 S. 24–25 |
| Firmware-CV-Formel erfunden | widerlegt als K3 – JMRI 0.255.285:2 / 287 / 288 |
| CV51-Rechenregel „≥ 16 → minus 16“ gefährlich | weitgehend entschärft – CV51 hat laut Märklin nur Bits 0–4 (V-20) |
| Die schwarze Struktur verdeckt den Index | eher nein – Pin 11 liegt am Leistenende; das Problem ist der Sitz (V-11) |
| O/B-Vertauschung Wagenplatine | widerlegt (bereits REV9 W-01; S. 23 korrekt) |
| Quer-Kondensator müsste auch weg | widerlegt – ESU S. 27: nur die zwei Motor-Gehäuse-Kondensatoren |

---

## 10. Korrekturreihenfolge und fehlende Nachweise

| Welle | Befunde | Inhalt |
|---|---|---|
| **1 – Ausführbar machen** | V-01, V-02, V-04, V-09, V-10 | S. 5 als Referenzvergleich; S. 28 mit CS3-GFP3 und Programmiergleis als „begrenzte Versorgung“; Prüfaufnahme als Voraussetzung auf S. 2/6; Gegenkopf-Einzelstrom; R4/R5-Referenz für hintere LEDs |
| **2 – Schutz wiederherstellen** | V-03, V-14, V-15 | Anlagenkarte mit Signalprüfung und ICE-M-S-Hinweis; freie Kontakte isolieren; Zeitpunkt des Rückmeldetests |
| **3 – Programmierung straffen** | V-05, V-06, V-07, V-08, V-17 bis V-22 | Firmwarediagnose optional; Plan B nach zwei Versuchen; SID-Dokumentation; Datenweg korrigieren; verlorene Warnungen zurück |
| **4 – Redaktion** | V-23 bis V-33 | ebenso V-12, V-13, V-16 |

**Was wirklich noch fehlt**

1. **Bestand:** Welche 21MTC-Prüfaufnahme ist vorhanden (60970, 53900 oder keine)? Davon hängt ab, ob S. 9–S. 11 überhaupt beginnen können.
2. **Anlage:** Gibt es Signale, die den Mittelleiter stromlos schalten, sowie Bremsmodule, Booster oder ein angebundenes Programmiergleis?
3. **Fotos:**
   - LoDi 511 Rückseite mit Revision und SJ1/SJ2
   - Stiftleiste von oben und seitlich
   - Aufdruck von R4/R5
   - motorloser 2976-Kopf geöffnet (Schleifer vorhanden?)
   - Motorbauart vorn
4. **Herstelleranfragen (keine Händler):**
   - **LoDi:** Kappe, Platinenvariante und SW–RT, V1.49-GE-Pfad, LED-Daten 514, Stromaufnahme je Wagenplatine.
   - **ESU:** Folgt der LokPilot 5 M4 MKL einem Märklin-mfx-Master? Welche Register, welche Firmware?
5. **Nachweis am eigenen PC:** LokProgrammer 5.x ohne 53451 – LP5-MKL-Projekt, Sonderoptionen und „Geänderte CVs anzeigen“ funktionieren (Bildschirmfoto).

---

## Quellen (in dieser Prüfung abgerufen)

**Hersteller**

- [Märklin 60975/60976/60977](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf) · [Märklin CV-Tabelle mSD3](https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf) · [Märklin CS3-Anleitung 17-02](https://www.maerklin.de/fileadmin/media/produkte/pdfs/MANUAL_CS3_DE-EN_17-02.pdf) · [Märklin CS3-Changelog 2.6.0](https://www.maerklin.de/fileadmin/media/service/cs3/Maerklin_CS3_v2.6.0_changelog.pdf) · [Märklin 60970](https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf) · [Märklin Mobile Station](https://static.maerklin.de/damcontent/2a/47/2a470bed20017f68f92306725d49fca81702905959.pdf) · [Märklin 60974](https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf) · [Märklin 60971](https://static.maerklin.de/damcontent/21/3e/213ee6e47c4afa9ad2282158bf7728441660728698.pdf) · [Märklin CAN-Protokoll 2.0](https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf)
- [ESU LokPilot 5 Anleitung](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e) · [ESU Master/Slave](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/) · [ESU CV-Änderungen anzeigen](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/) · [ESU Profi-Prüfstand](https://www.esu.eu/produkte/profi-pruefstand/)
- [LoDi Motor-WiB ICE-M](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/) · [LoDi WiB ICE-M](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-wib-ice-m/) · [LoDi-Shop](https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/)

**Normen**

- [RCN-121](https://normen.railcommunity.de/RCN-121.pdf) · [RCN-210](https://normen.railcommunity.de/RCN-210.pdf) · [RCN-216](https://normen.railcommunity.de/RCN-216.pdf)

**Implementierung und Erfahrung**

- [JMRI v4decoderInfoCVs.xml](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml) · [JMRI v5standardCVs.xml](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v5standardCVs.xml#L993) · [TrainControl lokomotive_cs3.cs2](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/lokomotive_cs3.cs2#L4) · [Stummiforum MTB-Ontour](https://www.stummiforum.de/t212683f5-Umbau-ICE-Maerklin-auf-mSD-DCC.html)

**Nicht abrufbar**

- [mDecoderTool3 v3.60](https://streaming.maerklin.de/public-media/mdt3/pdfs/D_mDecoderTool3_A5_v360.pdf) (robots.txt)
- 60941-Beilage (nur als Bild-PDF, Text nicht lesbar)

Es wurden keine Umgehungswege genutzt.
