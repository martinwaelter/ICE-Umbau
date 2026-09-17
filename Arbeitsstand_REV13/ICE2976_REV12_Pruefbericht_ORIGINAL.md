# Prüfbericht ICE 2976 – REV12 Werkstattfassung

**Prüfgegenstand:** `ICE_2976_Umbauanleitung_REV12_WERKSTATTFASSUNG.pdf`
**Prüfdatum:** 12.09.2026
**Art:** forensische, adversariale Dokumentprüfung; keine Hardwarefreigabe. Es wurden keine Messwerte, Firmwarestände, Passungen oder Herstellerantworten erfunden.

---

## 0. Datei und Methode

| Punkt | Ergebnis |
|---|---|
| Umfang | 44 Seiten A4, 44 Arbeitskarten |
| Erzeugung | ReportLab, 11.09.2026 07:17 UTC |
| SHA-256 | `95af61083373a0755fde8ebd5ae70233952f6283b3db652b03e71c26582bcc8e` |
| Links | 227 interne Sprungziele; 34 Quellen Q1–Q34 (11 davon neu gegenüber REV11) |
| Sichtung | alle 44 Seiten als Bild und als Text |
| Konsil | 3 getrennte Subagenten (Quellen / Hardware und Messtechnik / Vergleich REV11→REV12), jeweils eigener Kontext, ohne Kenntnis voneinander. Dasselbe Sprachmodell, also Mehrfachprüfung, **keine** drei menschlichen Fachleute. |
| Eigene Gegenprüfung | CS3-Handbuch, Märklin-CV-Tabelle, 60970/60971/60974, ESU, LoDi, RailCommunity, JMRI, TrainControl |
| Verifikation | 38 zitierte Textstellen maschinell gegen die angegebenen Seiten geprüft; alle gefunden |

**Evidenzkategorien:** K1 Herstelleranweisung · K2 Ableitung aus Norm/Zeichnung/Physik · K3 Softwareimplementierung · K4 Drittanbieter/Erfahrungsbericht · K5 Annahme.

---

## 1. Kurzurteil

**REV12 ist die bisher technisch beste Fassung. Zwei Dinge stehen der Freigabe entgegen: die Anleitung setzt ein getrenntes Prüfgleis voraus, das es bei dir nicht gibt, und zwei ihrer Nachweiswege sind für dich nicht gangbar. Kein P0.**

**Was in REV12 nachweislich besser ist**

- **Meine vier P1-Punkte aus REV11 sind bearbeitet:** Geräteweg mit zwei Märklin 60970 (S. 6/7), ausführbare Anschluss- und Sichtprüfung statt unausfüllbarer Messkarte (S. 5), Trennung von Ersttest und numerischer Lastabnahme (S. 30/31), eigene Anlagenkarte mit ICE-M-S-Hinweis (S. 38).
- **Auch die kleineren Punkte:** CV51 Bit 0 statt Umlöten (S. 35), Elko-Entladung mit nachvollziehbarer Rechnung (S. 3), Protokoll- und Adresserfassung CV1/17/18/29/47 (S. 10), Kohlestaub (S. 16), Service-Trennstelle am Gehäuse (S. 40), CV54 = 0 + F1 wieder gesperrt (S. 10/11).
- **Fachlich stark und nicht selbstverständlich:** der Kasten „Was dieser Ersttest aussagt" (S. 30), die Einsicht, dass GE bei O = RT kein glatter Gleichstrom ist (S. 31), das Verbot eines geerdeten Oszilloskop-Masseclips, die Zweifachmessung der Motor-Sechserfolge an Bürstenfahnen und Litzenenden, die Kreuzpfadprüfung jeder Kupplung.
- **Geprüfte Herstellerzahlen stimmen:** 1,1 A / 250 mA / 300 mA / 1,6 A; CV52 = 3; CV51 Bit 4 (0 = verstärkt) und Bit 0 (Motoranschluss tauschen); CV7 = 77; 60941 nur für Trommelkollektormotoren; 60970-Schalter und „Kontakt 1 = weißer Punkt"; 53900 mit 0,5 W und Logikpfaden an AUX3/AUX4; 60974 ab 3.2.0.1; LoDi-Belegung und Jumperlogik; RCN-121/210/216.

**Was der Freigabe entgegensteht**

| ID | Prio | Kern |
|---|---|---|
| W-01 | P1 | Die Anleitung setzt ein **elektrisch getrenntes Prüfgleis** voraus. Nach deiner Angabe gibt es das nicht; „Prüfgleis" heißt bei dir „keine Züge auf der Anlage". Damit ist das gesamte Schutzkonzept nicht erfüllt. |
| W-02 | P1 | Der **CS3-Programmiergleisausgang** trägt Ersttest, Kleinstfahrt, Paartest und Wagentests. Märklin beschreibt diesen Ausgang aber für Auslesen und Programmieren, verlangt „keine weiteren Verbraucher" und nennt 1,5 A – unter der 1,6-A-Gesamtgrenze des 60977. Ein Ausweichweg fehlt. |
| W-03 | P1 | Es fehlt ein frühes **Kupplungstor**: Ob dein 2976 überhaupt zweipolig stromführende Kupplungen hat, wird erst auf S. 26 relevant, also nach dem vollständigen Umbau beider Köpfe. |
| W-04 | P1 | Die **hinteren LED-Daten** (U_max, zulässiger Strom) sind mit den erlaubten Mitteln nicht bestimmbar; anders als auf S. 17, 20, 22 und 33 fordert S. 18 keine LoDi-Anfrage. Ziel „weiß/rot an beiden Köpfen" bleibt gesperrt. |
| W-05 | P1 | Die **Lastabnahme S. 31** bietet nur Weg A (LoDi-Daten, die es nicht gibt) und Weg B (Stromsonde plus Speicheroszilloskop). Den realistischen Mittelweg – Multimeter in Reihe in der geöffneten GE-Ader, genau wie auf S. 19 erlaubt – sperrt die Karte selbst. Ziel „Innenlicht mit endgültiger Wagenzahl" bleibt gesperrt. |
| W-07 | P1 | **60970, Schalter d bei der ESU-Aufnahme:** Die Tabelle legt keine Stellung fest. Bleibt die 8-Ω-Last gesteckt und belegt der 59649 die 21MTC-Pins 9/10 als verstärkte Ausgänge, kann der Ausgang zerstört werden. |

**Grenzen dieser Prüfung**

- Nicht abrufbar: mDecoderTool3 v3.60 (robots.txt), Fluke 87/89 Handbuch (403), ESU-LokPilot-5-Anleitung nur bis S. 34, 60941-Beilage nur als Bild.
- Weiterhin unbelegt: dass ein **LokPilot 5 M4 MKL** einem **Märklin-mfx-Master** folgt. ESU dokumentiert die Funktion nur für LokSound 5 ab 5.1.101 mit ESU-Master. REV12 kennzeichnet das korrekt als offen und hat auf S. 12 erstmals einen sauberen Abbruch- und Diagnoseweg.

---

## 2. Befunde

Schema je Befund: **Ort** · **Zitat** · **Mechanismus/Folge** · **Quelle (Kategorie)** · **Status** · **Ersatz** · **Art** (T = Textkorrektur genügt, N = realer Nachweis nötig). In Klammern die Konsil-Kennungen.

### P1

**W-01 · Das vorausgesetzte getrennte Prüfgleis existiert nicht** (eigener Befund nach deiner Angabe)

- **Ort:** S. 30 VORHER; S. 35 Schritt 1; S. 36 Schritt 2; S. 37 VORHER; S. 12 VORHER.
- **Zitat:** „CS3-Programmiergleis vollständig von der Anlage getrennt. Hauptgleisstecker ab, keine andere Quelle." / „Nur den CS3-Programmiergleisausgang an ein vollständig getrenntes Prüfgleis anschließen."
- **Mechanismus:** Deine Angabe: kein separates Gleisstück; „Prüfgleis" bedeutet „keine anderen Züge auf der Anlage". Das erfüllt keine der drei Schutzfunktionen, die die Anleitung dem Prüfgleis zuweist:
  1. **Keine Bereichsgrenze im Fahrweg.** RT verbindet beide Schleifer; auf der Anlage überbrückt der Zug ab dem ersten Einschalten jede Mittelleiter-Trennstelle, jede zweite Einspeisung und jeden Schalt- oder Bremsabschnitt. Genau das soll S. 38 vorher ausschließen – S. 38 liegt aber hinter dem Erststrom.
  2. **Begrenzte Energie.** Am Hauptgleisausgang stehen bis 5 A zur Verfügung; ein Verdrahtungsfehler wird dort erheblich energiereicher ausgetragen.
  3. **Auswertbare Stromanzeige.** Der GFP3-Wert ist ein Summenwert. Mit angeschlossener Anlage (Beleuchtung, Decoder, Weichen) ist der Anteil des Zuges daraus nicht bestimmbar; der auf S. 30/35 verlangte „Leerwert" wird unbrauchbar.
- **Folge:** Die Ersttest-, Last- und Paartestkarten sind in deiner Umgebung entweder nicht ausführbar oder ohne die zugesagte Schutzwirkung.
- **Quelle:** Dokumenttext (K1 des Dokuments) gegen deine Bestandsangabe; Märklin CS3-Handbuch S. 3 (K1): „Das Programmiergleis darf keinen direkten elektrischen Kontakt zur Anlage haben und es dürfen keine weiteren Verbraucher … angeschlossen sein."
- **Status:** bestätigt.
- **Ersatz – zwei zulässige Wege, einer muss in REV13 stehen:**
  > **Weg 1 (empfohlen):** „Baue einen getrennten Prüfabschnitt: 3–4 C-Gleise plus ein Anschlussgleis, ohne jede Gleis- oder Kabelverbindung zur Anlage, auf nichtleitender Unterlage, mit Endbegrenzung gegen Abrollen. Dieser Abschnitt wird wahlweise an den Programmiergleisausgang (Lesen/Schreiben) oder an den Hauptgleisausgang (Fahr- und Lasttests) angeschlossen – nie an beide, Umstecken nur spannungslos. Alle Karten, die ‚Prüfgleis' nennen, gelten für diesen Abschnitt."
  > **Weg 2 (nur falls Weg 1 ausscheidet):** „Ohne getrennten Abschnitt darf kein Erststrom stattfinden, bevor Karte 38 vollständig ausgefüllt ist und der gesamte befahrene Bereich als eine Quelle ohne Schalt-, Brems- oder Boostergrenze nachgewiesen wurde. Zusätzlich: alle übrigen Verbraucher der Anlage abtrennen, damit der GFP3-Leerwert aussagefähig bleibt. Die Energie des Hauptgleisausgangs bleibt dabei unbegrenzt; jeder Verdrahtungsfehler trifft den Zug mit voller Leistung."
- **Art:** T + N (Aufbau bzw. Anlagenerfassung).

---

**W-02 · Der Programmiergleisausgang trägt Aufgaben, für die Märklin ihn nicht beschreibt** (C-05, A-17, B-08, eigene Prüfung)

- **Ort:** S. 30 VORHER und Schritt 1; S. 35 Schritte 1–4; S. 36 Schritte 1–2; S. 37; dagegen S. 7 Schritt 2 und S. 12 Schritt 1 („getrennter CS3-**Betriebs**ausgang").
- **Mechanismus:**
  - Märklin beschreibt den Programmiergleisanschluss als Anschluss „zum Auslesen, Programmieren und Bearbeiten von Fahrzeugen im DCC- oder Motorola(MM2)-Format" und verlangt „keine weiteren Verbraucher" (CS3-Handbuch S. 3, K1). Dass dort normaler mfx-Fahrbetrieb mit Sound und Fahrstufen möglich ist, steht nirgends; belegt ist nur, dass die **Anmeldung** von mfx-Loks „sowohl auf dem Haupt- als auch auf dem Programmiergleis möglich" ist (S. 5) und dass GFP3 den Strom beider Ausgänge anzeigt.
  - 1,5 A Grenze am Programmiergleis liegen **unter** der 60977-Gesamtgrenze von 1,6 A und nur 0,4 A über dem Motordauerstrom. Eine Abschaltung beim Anfahren kann also die Quelle sein, nicht der Zug – die Karte kennt diese Ursache nicht und verbietet einen zweiten Versuch.
  - REV12 verlangt denselben Nachweis (mfx-Paarreaktion) einmal am Betriebsausgang (S. 12) und einmal am Programmiergleisausgang (S. 36).
- **Folge:** Scheitert der Fahrbetrieb an diesem Ausgang, steht der Anwender ohne dokumentierten Ausweichweg da – an genau der Stelle, an der er sonst improvisiert.
- **Status:** nicht belegt (Fahrbetrieb); Gegenindiz: Anwenderberichte und die GFP3-Anzeige sprechen dafür, dass der Ausgang dauerhaft versorgt ist.
- **Ersatz (S. 30 VORHER und S. 35 VORHER):**
  > „Prüfe zuerst an deiner CS3, ob der Programmiergleisausgang mfx-Anmeldung **und** Fahrbetrieb liefert, und notiere das Ergebnis. Wenn ja: Ersttest dort, Grenze 1,5 A. Wenn nein: Kopf spannungslos auf den getrennten Prüfabschnitt am Hauptgleisausgang umsetzen; dann gilt die 5-A-Quelle, deshalb vorher Karte 32 vollständig und Sichtprüfung wiederholen. **Abschaltung unterscheiden:** beim Aufsetzen oder ohne Fahrbefehl = Fehler, trennen, Ursache suchen; erst beim Anlegen der kleinsten Fahrstufe = möglicherweise die 1,5-A-Grenze, dann genau ein weiterer Versuch nach Freilaufkontrolle."
- **Art:** T + N (Gerätefeststellung).

---

**W-03 · Kein frühes Kupplungstor: stromführende Kupplungen sind unbelegte Voraussetzung** (B-04)

- **Ort:** S. 2 Tabelle „Mittelwagen" und Kasten „KUPPLUNGEN"; S. 26 VORHER.
- **Zitat:** „Je eine passende LoDi-WiB ICE-M; Originalkupplungen" (S. 2, Zeile Mittelwagen) / „Nur passive Kupplungsstücke mit freien Litzen".
- **Mechanismus:** Das gesamte RT/GE-Konzept setzt an **jedem** Übergang zwei getrennte, stromführende Kontakte mit eigener Litze voraus – auch Kopf zu Wagen. Ob die Wagen der analogen Startpackung 2976 das haben, prüft keine Karte. S. 26 setzt „freie Litzen" bereits voraus; S. 2 nennt Kupplungen aus verwandten Modellen als Kandidaten, während das Ziel „originale Märklin-Kupplungen" lautet.
- **Folge:** Der Mangel fällt erst nach dem vollständigen elektrischen Umbau beider Köpfe auf (S. 13–24). Dann ist der Zug zerlegt und das Konzept nicht realisierbar.
- **Status:** bestätigt (fehlende Karte); die Hardware selbst ist offen.
- **Ersatz – neue Karte vor S. 13:**
  > „Kupplungstor. An einem Wagen und an beiden Köpfen die vorhandene Kupplung fotografieren und auf zwei getrennte Kontaktflächen mit je eigener Litze prüfen (Messung nach S. 4). Zwei Pfade an allen Übergängen → weiter. Ein Pfad oder keiner → hier endet der beschriebene Aufbau; eine Nachrüstung stromführender Kupplungen ist eine eigene Entscheidung mit eigener Maß- und Passungsprüfung. Bis zur Klärung den Zug nicht elektrisch umbauen."
- **Art:** T + N (Sichtprüfung am Fahrzeug, sofort möglich).

---

**W-04 · Hintere LED-Daten nicht bestimmbar, ohne Weg zur Klärung** (B-01)

- **Ort:** S. 18, Zeile „Tatsächliche Daten" und Schritt 1; STOPP.
- **Zitat:** „U_max aus belegtem Ausgangs-/Versorgungsmaximum bestimmen, nicht aus einem einfachen AC-Wert am Gleis. Ein DC-Mittelwert über +Ub/LV zeigt keine sichere Spitze." / „Fehlen die hinteren Daten, drei LED-Leitungen einzeln isoliert lassen."
- **Mechanismus:** Die Auslegung hängt an U_max und I_zulässig. Die Karte verbietet beide Verfahren, die der Anwender besitzt, und nennt keinen Ersatz; die LoDi-Seiten veröffentlichen weder zulässigen LED-Strom noch Zweigspannung. Anders als S. 17, 20, 22 und 33 fordert S. 18 **keine** Herstelleranfrage.
- **Folge:** Das Nutzerziel „beide Köpfe richtungsabhängig weiß/rot" ist nach dem Buchstaben der Anleitung nicht erreichbar.
- **Status:** bestätigt.
- **Ersatz:**
  > „Fehlende Daten so beschaffen: LoDi mit beidseitigem Foto des 514-Einsatzes und der Revision fragen – ‚Welcher Dauerstrom je Farbe ist zulässig, welche Flussspannung haben die Zweige, wie sind sie aufgebaut?' Bis zur Antwort gilt konservativ: U_max = höchster selbst gemessener Scheitelwert am eigenen Prüfabschnitt, ersatzweise 25 V; I_zulässig = 5 mA. Die Auslegung nach diesem Schema ist zulässig, die Helligkeit wird dann nach S. 41 abgeglichen. Herstellerkontakt ist kein Händlerauftrag."
- **Art:** T + N (eine Anfrage).

---

**W-05 · Lastabnahme: beide Wege unerreichbar, der praktikable Weg wird selbst gesperrt** (B-02, B-10)

- **Ort:** S. 31, Weg A und Weg B, STOPP; Auswirkung auf S. 30 Schritt 4 und S. 37 VORHER.
- **Zitat:** „Weg A: Revisionspassende Herstellerdaten decken Wagenzahl, Versorgung, höchste Helligkeit und Einschaltlast ab." / „Weg B: DC-fähige Stromsonde mit nachgewiesener mA-Auflösung plus Speicheroszilloskop ausleihen." / STOPP: „Ein Shunt ist nur mit passend ausgelegtem Differenz-/isoliertem Messaufbau eine Alternative; hier nicht improvisieren."
- **Mechanismus:** Weg A existiert nicht: LoDi veröffentlicht weder Stromaufnahme je Wagen noch zulässige Wagenzahl. Weg B ist für einen Nicht-Elektrotechniker praktisch nicht beschaffbar. Gleichzeitig erlaubt die Anleitung auf S. 19 Schritt 2 genau die Topologie, die hier fehlt: Multimeter im abgesicherten mA-Bereich in Reihe in einer geöffneten Einzelader. Ein Handmultimeter in einer aufgetrennten GE-Ader ist potenzialfrei; die Erdungsfrage betrifft nur den Oszilloskop-Masseclip, der im selben STOPP schon getrennt behandelt wird.
- **Folge:** Jede Wagenstufe bleibt gesperrt; das Nutzerziel „Innenlicht mit der endgültigen Wagenzahl" ist nicht erreichbar.
- **Status:** bestätigt (innerer Widerspruch und Quellenlage geprüft).
- **Ersatz – „Weg C" als Regelweg:**
  > „Mittelwertmessung: stromlos die einzelne GE-Ader an der vorhandenen Trennstelle öffnen, Multimeter im abgesicherten mA-Bereich in Reihe einsetzen (Topologie wie S. 19/2, potenzialfrei), je Wagen einzeln bei höchster Helligkeit messen. Summe der Einzelmittelwerte gegen 250 mA (AUX4) und 300 mA (Licht + AUX) mit 40 % Reserve prüfen. Peak-Nachweis nach Weg B nur verlangen, wenn die Summe 60 % der Grenze überschreitet. Unzulässig bleiben: Shunt mit erdbezogener Messmasse und jeder geerdete Oszilloskop-Masseclip an GE oder RT."
- **Art:** T.

---

**W-07 · 60970: Schalterstellung „Impedanz" für die ESU-Aufnahme nicht festgelegt** (B-05)

- **Ort:** S. 7, Tabelle, Zeile „d: Impedanz / Sound", Spalte „Aufnahme B: 59649 MKL".
- **Zitat:** „Kein Soundtest; keine externe Soundlast".
- **Mechanismus:** Der 60970 hat einen physischen Umschalter für die Lautsprecherimpedanz (8 Ω / 100 Ω); er steht immer in einer Stellung. Für Aufnahme A ist 8 Ω vorgeschrieben, für Aufnahme B keine Stellung genannt; „keine externe Soundlast" adressiert nur einen zusätzlichen Lautsprecher. Nach RCN-121 können die 21MTC-Pins 9/10 statt Lautsprecher auch **verstärkte Funktionsausgänge** führen.
- **Bedingung:** Schalter bleibt nach Aufnahme A auf 8 Ω, der 59649 belegt Pin 9/10 als verstärkten Ausgang und dieser wird aktiv.
- **Folge:** 8 Ω an einem verstärkten Ausgang bei rund 20 V zerstört den Ausgang – noch vor jedem Fahrzeugumbau.
- **Status:** wahrscheinlich; die Pinbelegung des 59649 war aus den abrufbaren ESU-Unterlagen nicht zu klären.
- **Ersatz:**
  > „Aufnahme B, Schalter d: vor dem Einsetzen des 59649 auf die Stellung ohne Lautsprecherlast (100 Ω) bringen. Vorher in der Papieranleitung des 59649 nachschlagen, ob die 21MTC-Pins 9/10 belegt sind. Solange das offen ist, gilt: keine Lautsprecherlast an Aufnahme B. Stellung ins Protokoll eintragen."
- **Art:** T + N.

### P2

| ID | Ort | Befund und Mechanismus | Ersatz | Art |
|---|---|---|---|---|
| **W-06** (C-03) | S. 18 | Die **Polaritätsprüfung der LEDs vor dem Anschluss** (REV11: Diodentest mit geeigneter Prüfspannung) ist ersatzlos entfallen. Verpolt liegt die volle Versorgungsspannung als Sperrspannung an der LED. Die Zuordnung erfolgt jetzt nur noch nach Aufdruck/Herstellerbild. | Punkt ergänzen: „Vor dem Löten jeden Farbzweig auf Polung prüfen; Diodenfunktion nur mit laut Handbuch geeigneter Prüfspannung. OL beweist keinen Defekt – nicht mit höherer Spannung gegenprüfen. Ohne geeignete Prüffunktion Zweig getrennt lassen." | T |
| **W-08** (C-04) | S. 11/3 | Die namentliche Sperre der CS3-Schaltfläche **„Prog."** ist entfallen; es bleibt nur „keine Vorlagenwerte gesammelt schreiben". Die zugehörige Quelle Q24 wurde neu aufgenommen, aber nirgends zitiert. Wer „Prog." drückt, überträgt die ganze Vorlagenliste – inklusive Adresse, CV29 und der eben geschriebenen Synchronisationswerte. | „Die Schaltflächen ‚Prog.' und ‚Vorlagenwerte schreiben' bleiben in diesem Ablauf unbenutzt (Q24)." | T |
| **W-09** (A-06, B-06) | S. 7/2 | **Zwei Prüfstände parallel an einer Quelle**: Märklin dokumentiert nur den Einzelbetrieb („nur ein Decoder gleichzeitig", Versorgung ausschließlich über den Gleisanschluss). Zusätzlich fehlt vor dem Parallelschalten jede Polaritätskontrolle von B und 0; bei zwei gleich aussehenden Geräten ein naheliegender Fehler mit direktem Kurzschluss am 5-A-Ausgang. | Parallelbetrieb als eigene Festlegung kennzeichnen; davor: „B und 0 je Aufnahme nach Aufdruck bestimmen und fotografieren, verbinden, Quelle noch nicht anschließen, Ω zwischen gemeinsamem B- und 0-Knoten messen – der Kurzschlusswert darf nicht erscheinen. Erst dann CS3 anschließen." | T + N |
| **W-10** (C-01, C-02) | S. 30/1, S. 31 | **Reihenfolge:** Karte 30 enthält einen ausführbaren Bestromungssatz („STOPP, einen Kopf aufsetzen … STOP aufheben"), steht aber vor der Pflichtcheckliste S. 32 und den Steckkarten S. 33/34. Karte 31 beschreibt vollständigen Zugbetrieb, steht aber vor S. 32–38 und verweist selbst auf S. 38. Beide Karten sind nach VORHER/WEITER als vorbereitend gemeint. | S. 30/1: „Diese Karte legt Kriterien fest; ausgeführt wird der Ersttest bei S. 35/S. 36." S. 31 VORHER: „Diese Messkarte wird begleitend ab S. 37 je Wagenstufe ausgeführt und setzt S. 32–36 sowie den freigegebenen Bereich S. 38 voraus." | T |
| **W-11** (A-02) | S. 11, optionale Firmwarebox | Die Registerlage **CV31 = 0 / CV32 = 255 mit CV285–288** stammt in JMRI aus der **V4**-Definition; die LokPilot-5-Definition bindet sie nicht ein (dort CV31 = 16, CV32 = 0–4). Schreiben eines für V5 nicht dokumentierten Indexpaars. | „In JMRI ist diese Registerlage nur für die V4-Generation hinterlegt; für den LokPilot 5 ist sie nicht belegt. Diagnose deshalb entfallen lassen oder Firmware über ESU klären." | T |
| **W-12** (A-15) | S. 8/9 | Dass die von der CS3 gespeicherte **mfxuid** byteweise dem ESU-Feld „Seriennummer" (CV192–195) entspricht, ist nirgends dokumentiert. Vier korrekt zurückgelesene Bytes können die falsche Identität beschreiben. | „Diese Zuordnung ist eine Annahme; sie wird durch den Funktionstest S. 12 bestätigt oder widerlegt, nicht durch das Rücklesen." | T |
| **W-13** (B-07) | S. 28 | **Radkontakt an B** kann das geschaltete Innenlicht aushebeln: Im Motorplatinenbetrieb ist B die Radmasse, der Lastrückweg läuft aber über L/GE zum AUX. Verbindet die Platine beide Knoten intern, entsteht ein ständiger zweiter Rückweg. Kein Prüfkriterium vor dem Löten; auffallen würde es erst bei T5/T7. | Vor dem Anlöten: „Wagen mit O/RT und L/GE, aber loser isolierter Federlitze aufs Prüfgleis; Innenlicht aus/ein. Dann die Federlitze nur mit isoliertem Clip an B halten und wiederholen. Bleibt das Licht dauerhaft an, wird B nicht angeschlossen." | T |
| **W-14** (B-03) | S. 25 | Die **Pad-Belegung RT an O / GE an L ist richtig**, aber ohne Zitat. LoDi führt auf derselben Seite zwei Legenden; wer Q4 nachschlägt, trifft zuerst die Standardlegende („O = Masse, B = Mittelleiter"). | Beide LoDi-Zeilen wörtlich abdrucken und die zweite als maßgeblich markieren. | T |
| **W-15** (B-12) | S. 38/2 | Die Regel „Kontaktmessung nur am eindeutig spannungsfreien, von Parallelpfaden getrennten Schaltkontakt" ist richtig, nennt aber kein ausführbares Verfahren (welche Ader abklemmen, Reihenfolge, Kennzeichnung, Vor-/Nachkontrolle). | „Je Schaltkontakt: Anlage aus, Modulversorgung physisch trennen, beide Adern am Modul abklemmen und beschriften, Klemmstellen fotografieren, Vor-/Nachkontrolle wie S. 4, dann Ω messen. Nicht abklemmbar → Abschnitt bleibt ‚unbekannt' und außerhalb der Teststrecke." | T |
| **W-16** (B-09) | S. 3 | Die **Elko-Rechnung ist korrekt**, gilt aber je Speicher. Sind C1 und C2 bestückt, verdoppelt sich τ; eine Minute reicht dann nicht (Restspannung über dem eigenen Kriterium). Die Nachmessung fängt es ab. | Satz anfügen: „Rechnung gilt je Speicher; Zahl und Wert vorher notieren, Entladezeit auf mindestens 10 τ der Summe einstellen." | N |
| **W-17** (B-11, C-19) | S. 6/2, S. 12 WEITER, S. 42 | **Beschaffungstor ohne Alternativpfad:** Zwei 60970 sind laut S. 1 nicht als vorhanden bestätigt; ohne sie bleibt S. 12 offen, und S. 12 ist das einzige Tor zum Umbau. Zusätzlich: geliehene Aufnahmen werden für jede spätere ESU-Änderung (S. 42) erneut gebraucht. | Entscheidungskarte mit drei Ausgängen (zwei Aufnahmen → Regelweg; eine Aufnahme → Einzelarbeiten, Paartest später mit benanntem Risiko; keine → Projekt endet hier) und Hinweis auf den späteren Wartungsbedarf. | T |
| **W-18** (C-06) | S. 32 | Der REV11-STOPP „Eine offene Pflichtzeile nicht mit ‚entfällt' schließen" ist entfallen, obwohl die Tabelle „entfällt"-Felder enthält und mit S. 18/19 eine legitim aufschiebbare Zeile hinzugekommen ist. | „‚entfällt' ist nur in den beiden Gegenkopf-Zeilen zulässig; jede andere offene Pflichtzeile sperrt die Bestromung dieses Kopfes." | T |
| **W-19** (C-07) | S. 35/5 | **CV51 Bit 0** ist jetzt gleichwertige Alternative zum Umlöten, ohne vorherige Bestätigung, dass MOT_L/MOT_R der dokumentierten Padzuordnung S. 21 entsprechen. Eine reale Vertauschung würde dauerhaft kaschiert. | „CV51 Bit 0 erst nach bestätigter Verdrahtung gegen S. 21; weicht sie ab, zuerst mechanisch korrigieren und S. 15/16 wiederholen. Keine zweite Umkehr über Licht oder CV29." | T |
| **W-20** (C-11) | S. 19 | Die Messkarte setzt eingebauten, bestromten Decoder voraus, steht aber zwischen den mechanischen Karten 18 und 20. Risiko: improvisierte LED-Bestromung, die S. 18 gerade verbietet. | VORHER ergänzen: „Diese Karte erst bei S. 35 (vorn) bzw. S. 36 (hinten) ausführen; jetzt nur lesen und Messpunkte markieren." | T |
| **W-21** (C-10) | S. 11 | Die Bedingung „gemeldete Updateanforderung vor Synchronisationsänderungen klären" steht nur noch **innerhalb** der optionalen Firmwarebox. | In VORHER hochziehen, unabhängig von der optionalen Diagnose. | T |
| **W-22** (C-08) | S. 12 WEITER | Der SID-Wechsel ist zulässig als optional gekennzeichnet. Offen bleibt, dass auch die **eigene CS3** nach Reset, Löschen oder Neuanmeldung eine neue SID vergibt. | „G0 zusätzlich wiederholen, wenn die CS3 dem Master eine neue Anmeldung/SID zuweist." | T |
| **W-23** (C-12) | S. 5 | Karte 5 hat **keinen STOPP-Block mehr**; die REV11-Regel „fehlt ein Feld, bleibt die davon abhängige Bestromung offen" und die Abdeckungsliste sind entfallen. Die Umstellung selbst ist eine echte Verbesserung. | STOPP neu: „Ist ein geplantes Kontakt-Pad-Paar nicht sicher zugänglich oder die Revision ungeklärt, bleibt diese Verbindung und die davon abhängige Bestromung offen." plus Abdeckungsliste vorn/hinten/Wagen. | T |
| **W-24** (B-08) | S. 30 Kasten, S. 35/2 | Die **1,5-A-Grenze** des Programmiergleises wird nicht als eigene Fehlerursache benannt; jede Abschaltung gilt als Fahrzeugfehler. | Abschaltung unterscheiden (siehe W-02). | T |

### P3

| ID | Ort | Befund | Ersatz |
|---|---|---|---|
| W-25 (C-13) | S. 12, 32, 42 | Kartenname **„G0"** (Null) kollidiert mit der CS3-Taste **„GO"** (S. 7, S. 10) | Karte 12 „CS3-Paarprüfung" nennen |
| W-26 (C-18) | S. 7, 11, 17/20, 31, 38 | Bezeichnerinflation A/B: Aufnahme A/B, Liste A/B, Ring A/B, Weg A/B, Bereich A/B – dazu Gleis B und Wagenpad B | „Weg A/B" → „Nachweis 1/2"; „Aufnahme A/B" → „Aufnahme 60977/59649" |
| W-27 (A-07/A-08) | S. 7 | Schalterzeile vermischt feste Buchsen und Schalter e (Datenquelle); Schalter **c** (Reed-Taster-Simulation) fehlt; „Sound aus" ist keine Schalterstellung | Zeilen trennen, c ergänzen („nicht betätigen"), d als 8 Ω/100 Ω führen |
| W-28 (A-09..A-12, C-14, C-16) | S. 2, 11, 13, 18, 29, 35, 44 | Quellenzuordnungen: CV51 Bit 0 steht in Q10 (nicht Q1); Q9 belegt nur die Lesefehlerbehandlung, das Sofortschreiben steht im CS3-Handbuch; Q26 ist die Kurzanleitung, der GFP3-Pfad steht im vollständigen Handbuch S. 33; Q5 zeigt auf die Wagenplatine statt auf die Frontmodule; Q24/Q30 sind auf keiner Karte zitiert; S. 2 verweist für die Beschaffung auf S. 7 statt S. 6 | Quellenzeilen korrigieren |
| W-29 (B-13) | S. 18/23 | Bauform und Einbauort der beiden hinteren Widerstände (bei Faktor-2-Reserve ein 0,5-W-Typ) werden in der Trockenpositionierung nicht geprüft | In S. 23 aufnehmen |
| W-30 (B-14) | S. 18/41 | Die Annahme U_LED = 0 unterdimensioniert den Strom systematisch; die Helligkeitsdifferenz zur unveränderten Front ist Verfahrensfolge, kein Fehler | Satz ergänzen |
| W-31 (B-15) | S. 40/41 | Der **Endzustand** wird nie isolationsgeprüft: S. 40 misst mit von LoDi getrenntem Motor, S. 41 stellt danach alles wieder her. Die Service-Trennstelle ist nur Option | Service-Trennstelle auf S. 21 als Ja/Nein-Pflichtentscheidung vorziehen |
| W-32 (B-16) | S. 15/16 | Messumfang unbeziffert (4 Gegenstellen × „mehrere" Rotorstellungen × 2 Endlagen × 2 Messorte) | „Mindestens vier gleichmäßig verteilte Rotorstellungen je Gegenstelle" |
| W-33 (B-17, C-15) | S. 7/22 | Die 8 Ω auf S. 7 sind für den Originallautsprecher unbelegt; die Leistungsangabe „1,6 W an 8 Ω" ist gegenüber REV11 entfallen | Impedanz als offen kennzeichnen; Leistungsangabe auf S. 22 zurückholen |
| W-34 (C-17) | div. | Entfallene Einzelsätze ohne Ersatz: „gilt nicht für Logikausgänge"; „Serienwiderstände mit bekanntem Sollwert beurteilen"; „ein halb offenes Gehäuse ist keine Lösung"; „Reset, Einmessfahrt und Pufferparameter sind getrennte Vorgänge" | Je Karte wieder aufnehmen |
| W-35 (C-20) | S. 24 | Vorwärtsverweis: VORHER verlangt „Kontaktzuordnung S. 26 geklärt" | Als Vorwärtsverweis kennzeichnen |
| W-36 (A-16) | S. 43 | „classicSUSI-Abgriff" und die Trägerbuchse stehen so nicht in der 60974-Anleitung (dort: SUSI-Schnittstelle des Decoders) | Formulierung angleichen |

---

## 3. Quellen- und Behauptungsprüfung (verdichtet)

70 Behauptungen geprüft; Auswahl.

| Ergebnis | Behauptungen |
|---|---|
| **Bestätigt (K1)** | 60977-Grenzwerte 1,1 A/250 mA/300 mA/1,6 A; CV51 Bit 0 „Motoranschluss tauschen" und Bit 4 „1 = logischer, 0 = verstärkter Ausgang"; CV52 = 3 (C90); CV7 = 77; CV8 des 60977 = 131; 60941 nur für Trommelkollektormotoren; 60970-Schalter und „Kontakt 1 = weißer Punkt"; „nur ein Decoder gleichzeitig am 60970"; 53900 mit 0,5 W und AUX3/AUX4 als Logikpfade; 59649 MKL mit verstärkten AUX3/AUX4; 60971 ausschließlich USB, nur Märklin-Decoder; 60974 ab 3.2.0.1, nur an Märklin-Decoder; CS3 max. 5 A Gleis / 1,5 A Programmiergleis, GFP3-Daten, mfx-Anmeldung auf beiden Ausgängen, sofortiges Schreiben im CV-Editor, kein Lesen bei PoM; LoDi O = RT / L = GE / B = Radmasse im Motorplatinenbetrieb, SJ1 → AUX4, SJ2 → AUX1; ESU 150 Ω nur für Fx micro; ESU-Menüpfad „Decoder > Sonderoptionen"; RCN-121 Index Pin 11, Pin 12 = Vcc; RCN-216 Quittung 60 mA / 5–7 ms und Ausführung unabhängig von der Quittung |
| **Bestätigt als K2/K3** | Elko-Rechnungen (0,123 W; τ = 5,92 s; 60 s ≈ 10 τ); konservative LED-Auslegung R_min ≥ U_max/I und P_max = U_max²/R_min; I = U_R/R; CV191/CV192–195 in JMRI mit LSB zuerst; CS2-Felder .mfxuid/.uid/.sid/.adresse und CS3-JSON mfxuid/uid/address; „Serviceprogrammierung nicht adressselektiv" |
| **Teilweise / abgeleitet** | „Extras > Geänderte CVs anzeigen" (ESU-Beleg für Software 4.4.0+, verlangt wird 5.x); 10 kΩ/0,5 W/1 min (eigene Auslegung, Fluke nennt andere Werte); „kein geerdeter Oszilloskop-Masseclip" (sachlich richtig, steht nicht in Q33); RCN-210 betrifft das Gleissignal, nicht den geschalteten AUX-Ausgang |
| **Nicht belegt** | LokPilot 5 M4 MKL folgt einem Märklin-mfx-Master (nur LokSound 5 ab 5.1.101 mit ESU-Master dokumentiert); LokProgrammer-5-Software ohne 53451-Hardware; CV31 = 0/CV32 = 255 mit CV285–288 für den LokPilot 5; mfxuid = ESU-Seriennummernfeld; Parallelbetrieb zweier 60970; Fahrbetrieb am Programmiergleisausgang |
| **Nicht prüfbar** | mDecoderTool3 v3.60 (robots.txt), Fluke 87/89 (403), ESU-Anleitung ab S. 34, 60941-Beilage (Bild-PDF), LoDi-514-Daten, Revision und schwarze Struktur der eigenen LoDi, Kupplungsausführung am 2976 |

---

## 4. Widerlegte oder entschärfte Verdachtsbefunde

| Verdacht | Ergebnis |
|---|---|
| Erststrom am Programmiergleisausgang generell nicht ausführbar | **teilweise widerlegt:** mfx-Anmeldung ist dort laut CS3-Handbuch möglich, GFP3 zeigt den Strom beider Ausgänge, Anwenderberichte melden Fahrbetrieb. Der **Fahrbetrieb** bleibt aber undokumentiert und ist am eigenen Gerät zu prüfen (W-02) |
| CV51 Bit 4: Polarität unbelegt (Konsil A) | **widerlegt:** Die 60977-Anleitung schreibt „Bit 4: Aux 4 (1 = logischer, 0 = verstärkter Ausgang)". Die Rechenregel „0–15 unverändert, 16–31 genau 16 abziehen, über 31 klären" ist arithmetisch korrekt und an der richtigen Stelle begrenzt |
| Karte 30 löst eine Bestromung vor den Steckkarten aus (Konsil C: P0) | **herabgestuft auf P2:** Zum Zeitpunkt von Karte 30 ist noch kein Decoder gesteckt; VORHER/WEITER und die Zeile auf S. 32 weisen die Karte als vorbereitend aus. Es bleibt eine Formulierungs- und Reihenfolgefrage (W-10) |
| O/B-Vertauschung an der Wagenplatine | **widerlegt** (wie schon in REV9/REV11): LoDi nennt für den Motorplatinenbetrieb ausdrücklich O = Mittelleiter, B = Radmasse. Es fehlt nur das Zitat (W-14) |
| Quer-Kondensator müsste ebenfalls entfernt werden | **widerlegt:** Nur die beiden Kondensatoren Bürste–Gehäuse müssen weg; der Querkondensator gehört zur Herstellerentstörung des 60941-Motorschilds |
| Elko-Verfahren fehlerhaft | **widerlegt:** Verfahren und alle drei Zahlen stimmen; nur der Geltungsbereich bei zwei Speichern fehlt (W-16) |
| Verzicht auf einfache DC-mA-Messung an GE/RT sei falsch | **teilweise widerlegt:** Die Begründung ist richtig (GE ist bei O = RT kein glatter Gleichstrom). Falsch ist nur, deshalb **gar keine** Mittelwertmessung zuzulassen (W-05) |

---

## 5. Anforderungsmatrix

| Nr. | Nutzerziel | Dokumentiert | Belegt | Getestet | Status |
|---|---|---|---|---|---|
| 1 | Ein automatisch angemeldeter mfx-Zug | S. 8–12 | ESU/ESU (K1); Forenbericht mit LokProgrammer (K4); CS3-Weg unerprobt | nein | **offen**, mit sauberem Abbruch- und Diagnoseweg (S. 12) |
| 2 | Kein zweiter Loksatz | S. 10/12/36 | ESU (K1) | nein | offen; SID-Wechsel bewusst optional |
| 3 | Keine Traktion | ja | folgt aus 1 | nein | offen |
| 4 | Märklin-Sound | S. 22/35 | K1 | nein | offen (Lautsprecher, Adapter, Impedanz W-33) |
| 5 | Weiß/rot an beiden Köpfen im Stand | S. 12/18/19/24/36 | Mapping schlüssig (K2) | nein | **gesperrt durch W-04** |
| 6 | LoDi-Front-LEDs | S. 18/19/21 | Rechenweg korrekt (K2) | nein | vorn nutzbar; hinten gesperrt (W-04) |
| 7 | Innenlicht ohne Richtungsunterbrechung | S. 29/37 | RT + AUX richtungsunabhängig (K2) | nein | **Wagenzahl gesperrt durch W-05**; zusätzlich W-13 |
| 8 | Originale Märklin-Kupplungen | S. 2/26 | nur Kandidaten aus verwandten Modellen | nein | **offen, Tor fehlt (W-03)** |
| 9 | Keine zusätzliche Steuerleitung | S. 1/25/27 | K1/K2 | nein | erfüllt im Konzept; Anlagenbedingung S. 38 |

---

## 6. Ablaufübergänge

| Übergang | Wirksam | Lücke |
|---|---|---|
| Vorabtest → Montage (12 → 13) | hartes Tor: ohne bestandene Paarprüfung kein elektrischer Umbau – richtig platziert, weil ein negatives Ergebnis den Zug unzerlegt lässt | Beschaffungstor ohne Alternativpfad (W-17); Kupplungsfrage fehlt davor (W-03) |
| Montage → Messung (14 → 15/16) | vorbildlich: Motor von LoDi getrennt, Sechserfolge zweimal, Vor-/Nachproben | Umfang unbeziffert (W-32) |
| Messung → Programmierung (16 → 29) | Motorisolation bleibt eigenständige Pflicht und wird in S. 32 erneut abgefragt | – |
| Programmierung → Einsetzen (29/32 → 33/34) | stark: Ausgangsart CV51 Bit 4 **vor** dem ersten Strom; Index-Erstregel; kein Stecken bei ungeklärter schwarzer Struktur | – |
| Einsetzen → Erststrom (34 → 35/36) | konsistent: Motorseite allein, Gegenkopf allein, dann Paar, dazwischen STOP und physische Trennung | Quelle nicht belegt (W-02); Prüfgleis fehlt (W-01); Abschaltursache (W-24) |
| Erststrom → Last (35 → 30/31) | begriffliche Trennung Ersttest/Lastabnahme ist richtig und gut begründet | beide Nachweiswege unerreichbar (W-05); Kartenreihenfolge (W-10) |
| Last → Zug/Anlage (31 → 37/38) | S. 38 ist der inhaltlich stärkste Übergang: RT-Bus und Anlagengrenzen **vor** der ersten Fahrt | Verfahren am Schaltkontakt fehlt (W-15); erbt W-05 |
| Zug → Gehäuse (39 → 40/41) | richtig gestuft; Service-Trennstelle neu | Endzustand nie isolationsgeprüft (W-31) |

---

## 7. Korrekturreihenfolge

| Welle | Befunde | Inhalt |
|---|---|---|
| **1 – Prüfumgebung klären** | W-01, W-02, W-24 | Getrennten Prüfabschnitt festlegen oder Weg 2 aufnehmen; Quelleneigenschaft der CS3 feststellen; Abschaltursachen trennen |
| **2 – Tore und Sperren** | W-03, W-07, W-09, W-18, W-23 | Kupplungstor vor S. 13; Schalterstellung der ESU-Aufnahme; Polaritätskontrolle vor dem Parallelschalten; „entfällt"-Regel und Karte-5-STOPP zurück |
| **3 – Ziele entsperren** | W-04, W-05, W-13 | LoDi-Anfrage für die 514-Zweige mit konservativem Zwischenweg; „Weg C" für die Lastabnahme; B-Kontakt-Vorprobe |
| **4 – Reihenfolge und Wiederherstellungen** | W-06, W-08, W-10, W-11, W-12, W-19 bis W-22 | Polaritätsprüfung, „Prog."-Sperre, Kartenreihenfolge 30/31 und 19, Firmwarebox, SID-Wiederholung |
| **5 – Redaktion** | W-14, W-15, W-16, W-25 bis W-36 | Zitate, Bezeichner, Quellenzuordnung, Restsätze |

---

## 8. Was wirklich noch fehlt

1. **Entscheidung zum Prüfabschnitt** (W-01): getrennte Gleisstücke plus Anschlussgleis – oder ausdrücklich Weg 2 mit allen Folgen.
2. **Feststellung an deiner CS3** (W-02): Liefert der Programmiergleisausgang mfx-Anmeldung und Fahrbetrieb? Ergebnis notieren.
3. **Kupplungen ansehen** (W-03): zwei getrennte Kontaktflächen mit eigener Litze an Wagen und Köpfen – ja oder nein.
4. **Prüfaufnahmen** (W-17): zwei Märklin 60970 vorhanden, leihbar oder nicht – davon hängt der Startzeitpunkt ab.
5. **Anfrage an LoDi** (W-04, W-13, plus die schon vorbereiteten Fragen auf S. 17/33): zulässiger LED-Strom und Zweigaufbau des 514-Einsatzes; Stromaufnahme je Wagenplatine; Rolle des B-Knotens im Motorplatinenbetrieb; schwarze Struktur auf der Stiftleiste; GE-AUX und SW/RT bei V1.49.
6. **Anfrage an ESU** (unverändert offen): Folgt ein LokPilot 5 M4 MKL einem Märklin-mfx-Master? Welches Aktivierungsregister, welche Firmware, welches Format der Seriennummer?
7. **Papieranleitung des 59649** (W-07): Sind die 21MTC-Pins 9/10 belegt?

---

## 9. Quellen (in dieser Prüfung abgerufen)

**Märklin:** [60975/60976/60977](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf) · [CV-Tabelle mSD3](https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf) · [CS3-Handbuch](https://www.maerklin.de/fileadmin/media/produkte/pdfs/MANUAL_CS3_DE-EN_17-02.pdf) · [CS3-Changelog 2.6.0](https://www.maerklin.de/fileadmin/media/service/cs3/Maerklin_CS3_v2.6.0_changelog.pdf) · [60970](https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf) · [60971](https://static.maerklin.de/damcontent/21/3e/213ee6e47c4afa9ad2282158bf7728441660728698.pdf) · [60974](https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf) · [60941](https://www.maerklin.de/de/produkte/details/article/60941) · [CAN-Protokoll 2.0](https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf)

**ESU:** [LokPilot 5 Anleitung](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e) · [Master/Slave-Synchronisation](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/) · [Geänderte CVs anzeigen](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/) · [LokProgrammer-Software](https://www.esu.eu/download/software/lokprogrammer/) · [53900 Profi-Prüfstand](https://www.esu.eu/produkte/profi-pruefstand/)

**LoDi:** [Motor WiB ICE-M(-S)](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/) · [WiB ICE-M](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-wib-ice-m/)

**Normen:** [RCN-121](https://normen.railcommunity.de/RCN-121.pdf) · [RCN-210](https://normen.railcommunity.de/RCN-210.pdf) · [RCN-216](https://normen.railcommunity.de/RCN-216.pdf)

**Implementierung/Drittanbieter:** [JMRI](https://github.com/JMRI/JMRI) · [TrainControl](https://github.com/bob123456678/TrainControl) · [Stummiforum MTB-Ontour](https://www.stummiforum.de/t212683f5-Umbau-ICE-Maerklin-auf-mSD-DCC.html)

**Nicht abrufbar:** mDecoderTool3 v3.60 (robots.txt), Fluke 87/89 Handbuch (403), ESU-Anleitung ab S. 34, 60941-Beilage (Bild-PDF). Umgehungswege wurden nicht genutzt.
