# Prüfbericht: ICE 2976, Umbauanleitung REV9 mit Schnellanleitung

**Prüfgegenstand:** `ICE_2976_Umbauanleitung_REV9_MIT_SCHNELLANLEITUNG.pdf`
**Prüfdatum:** 10.09.2026
**Art der Prüfung:** Dokumentprüfung, forensisch und adversarial. Das ist keine Hardwarefreigabe.

---

## 0. Datei, Umfang und Prüfmethode

| Punkt | Ergebnis |
|---|---|
| Dateiname | stimmt; zwei Uploads, byte-identisch |
| Seitenzahl | 69 (A4) – stimmt |
| SHA-256 | `c1c1b1a2772f0e25385ffe911041b1cd2f7351277ada2ed5d8ecbe1be0070d29` – **stimmt exakt** |
| PDF-Metadaten | Titel „ICE 2976 - REV9 vollständig mit Schnellanleitung“, Producer pypdf |
| Interne Links | TOC S. 2/3 (67 Links) und Schnellanleitung (22 Links), insgesamt 89 interne Sprungziele: **alle Sprungziele korrekt** (Linkrechteck-Text gegen Zielseite geprüft) |
| Externe Links | 193 URI-Annotationen (44 verschiedene Adressen) extrahiert; die kritischen Quellen wurden abgerufen (siehe Abschnitt 10) |

**Vorgehen**

- **Vollsichtung:** alle 69 Seiten als gerendertes Bild und als Text. Kritische Fotos hochauflösend vergrößert:
  - S. 18: Stiftleiste
  - S. 29: Märklin-Zeichnung
  - S. 31: Pad-Beschriftung der Wagenplatine
- **Konsil:** 3 getrennte Prüfinstanzen, jeweils als eigener Subagent mit eigenem Kontext:
  1. Hardware/Verdrahtung
  2. Programmierung/mfx/Quellen
  3. Anfängerablauf/Schnellanleitung

  Keine Instanz sah die Ergebnisse der anderen oder meine Vorab-Notizen.
- **Offenlegung:** Alle drei Instanzen sind dasselbe Sprachmodell. Das ist eine unabhängige Mehrfachprüfung mit getrennten Kontexten, **keine** Prüfung durch drei menschliche Fachleute.
- **Konsolidierung und Gegenprüfung:** Konsolidierung und adversariale Gegenprüfung aller P1-Befunde habe ich selbst gemacht: Textbelege im PDF, Gegenbelege, eigene Quellenabrufe.
- **Herkunft der Befunde:** Die Konsil-Kennungen (H-, P-, A-, S-) stehen bei jedem Befund in Klammern.

**Evidenzkategorien (wie im Auftrag)**

| Nr. | Kategorie |
|---|---|
| K1 | Herstelleranweisung |
| K2 | Ableitung aus Zeichnung/Norm |
| K3 | Softwareimplementierung (JMRI) |
| K4 | Erfahrungsbericht |
| K5 | Annahme |
| K6 | Messung am realen Bauteil |

In dieser Prüfung gibt es **keine** K6-Evidenz. Messwerte, Firmwarestände, Passungen oder Herstellerantworten wurden **nicht** erfunden. Verifikation des Berichts: 56 zitierte Textstellen maschinell gegen die angegebenen PDF-Seiten geprüft – alle gefunden.

---

## 1. Kurzurteil

**Status:** REV9 ist **als Bau- und Anschlussanleitung noch nicht freigebbar**. Als Prüf- und Nachweisplan ist sie in weiten Teilen stark.

**Stärken (bestätigt)**

- **Motorisolation:** Kap. 5a–6b ist vorbildlich: positive Vor- und Nachproben, Rotor- und Drehgestelllagen, Kondensatorverfolgung, Hinweis „Masse-C zeigt nach Aufladen OL“.
- **Richtige Warnungen zur Programmierung:** Alle geprüften Aussagen stimmen mit den Märklin-Unterlagen überein:
  - CV51 Bit 4: 0 = verstärkt, 1 = Logik
  - CV7 = 77 startet die Einmessfahrt
  - CV52 = 3 = „Hochleistungsantrieb C90“
  - Grenzwerte 1,1 A / 250 mA / 300 mA / 1,6 A
  - Werksbelegung F1/F4/F6
  - 60974 über SUSI, Firmware ≥ 3.2.0.1
- **Rechnungen:** Alle Rechnungen (S. 25, 26, 41, 56) sind richtig.
- **Wagen-Pads:** Die Belegung „RT an O, GE an L, B optional Radmasse“ entspricht der LoDi-Angabe für den Motorplatinenbetrieb. Mein anfänglicher Verdacht einer O/0-Vertauschung ist **widerlegt** (W-01).
- **Nachweisgrenzen:** Das Dokument trennt JMRI (K3), ESU/ESU-Beispiel (K1) und Forenbericht (K4) sauber. Offene Nachweise erscheinen überwiegend nicht als erledigt.

**Befundzahl**

| Priorität | Anzahl |
|---|---|
| P0 | 0 |
| P1 | 4 (3 in der Vollfassung, 1 in der Schnellanleitung) |
| P2 | 24 |
| P3 | 19 |

**Kein P0:**

- Keine wörtlich befolgte Anweisung zerstört unter benannten Bedingungen unmittelbar Hardware.
- Die Gefährdungen entstehen durch **fehlende** Prüfschritte (P1), nicht durch falsche Anweisungen.

**Blockierend für die Freigabe**

1. Es fehlt eine Isolationsmesskarte für LED-Plus, Licht-/AUX-Leitungen und freie Trägerlitzen vor dem Erststrom (R-02).
2. Der motorlose Kopf hat weder Altzustandserfassung noch konkrete Anschlusshandgriffe (R-03).
3. Die Anlage wird nicht auf Mittelleiter-Trennstellen geprüft. LoDi verlangt bei zugbeeinflussenden Signalen die Variante ICE-M-S (R-01).
4. Schnellanleitung Schritt 5 wirkt wie eine vollständige Anschlussliste, ist es aber nicht (R-04).
5. **G0 ist mit den vorhandenen Mitteln nicht abschließbar.** C7 verlangt eine zweite, den Master nicht kennende Zentrale; vorhanden ist nur eine CS3 (R-11).

**Grenzen dieser Prüfung**

- Keine Hardware gesehen oder gemessen; keine Geräte programmiert.
- **Nicht abrufbar:** mDecoderTool3-Anleitung (robots.txt), Stummiforum-Beitrag „nakott“ (Timeout), LoDi-514-Datenblatt (nicht auffindbar), Krauß S. 39.
- **Nur teilweise abrufbar:** ESU-LokPilot-5-Anleitung (Werks-Mapping S. 66 nicht gelesen), Märklin-Beilage 60941 (nur Deckblatt).
- Web-Abrufe laufen über ein zusammenfassendes Werkzeug. Das entscheidende LoDi-Zitat zu L/O/B habe ich in drei getrennten Abrufen übereinstimmend erhalten.

---

## 2. Die wichtigsten bestätigten Befunde (nach Risiko)

| Rang | ID | Prio | Kern | Folge |
|---|---|---|---|---|
| 1 | R-02 | P1 | Keine Messkarte „U+/LED/AUX/freie Litzen gegen Chassis und Radmasse“ vor dem Erststrom | U+-Chassisschluss führt zu Gleiskurzschluss über den Decoder-Gleichrichter; LV/LR/GE an Masse zu Ausgangsüberlast |
| 2 | R-03 | P1 | Motorloser Kopf: kein Altzustand, kein Nachweis „Schleifer vorhanden“, kein Handgriff für B/GR, 0/GL und GE-Litze | Hinterer Decoder unversorgt, oder ein alter GE-Schienenweg belastet AUX4 |
| 3 | R-04 | P1 | Schnellanleitung G.1-5 ohne „freie Trägerlitzen isolieren“ und ohne B/GR bzw. 0/GL | Blanke GND-/+5V-/MR-/MV-Litze an Chassis → Decoderschaden beim Einschalten (G.2-9) |
| 4 | R-01 | P1 | RT überbrückt jede Mittelleiter-Trennstelle; keine Anlagenerfassung; LoDi-Bedingung „ICE-M-S bei zugbeeinflussenden Signalen“ fehlt | Abgeschalteter Halteabschnitt wird gespeist: dort stehende Lok fährt an; Booster-Ausgleichsströme über die Kupplungen |
| 5 | R-11 | P2 | C7 „Testzentrale, die den Master nicht kennt“ ohne gangbaren Weg | G0 nicht abschließbar |
| 6 | R-05 | P2 | F.4: 59649 mit aktivem M4 meldet sich beim Lesen an der CS3 selbst als eigene Lok an | Zweiter Loksatz existiert schon vor dem Sync-Test; C3 nur eingeschränkt aussagekräftig |
| 7 | R-15 | P2 | Fahrt und volle Innenlichtlast liegen vor der Lastabnahme (Kap. 18); kein prüfbares AUX-Summenkriterium | Kupplungs- und AUX-Pfad belastet, bevor bewertet |
| 8 | R-14 | P2 | Erststrom: S. 52 ohne STOP beim Einsetzen; Dummy direkt am Betriebsgleis statt am Programmiergleis | Stecken unter Spannung möglich; Fehler trifft ungedrosselten Gleisausgang |
| 9 | R-07 | P2 | Übrige F-Tasten des Master-Soundprojekts werden nie auf Wirkung am Slave geprüft | Rückleuchte dimmt oder erlischt bei Soundtaste; G0 gilt für einen anderen Projektstand |
| 10 | R-23 | P2 | Eigenes Foto S. 18: flache schwarze Kappe auf der 21MTC-Stiftleiste | Indexkontrolle (9c-M2) nicht möglich; Aufdrücken auf Kappe |

---

## 3. Vollständige Befundtabelle

Für jeden Befund:

- **Ort:** Seite, Kapitel, Schritt
- **Zitat:** Text oder Bildposition
- **Mechanismus**
- **Bedingung**
- **Folge**
- **Quelle** mit Evidenzkategorie K1–K6
- **Status:** bestätigt / wahrscheinlich / offen / widerlegt
- **Ersatz:** Ersatztext oder Prüfschritt
- **Art:** T = Textkorrektur genügt; N = realer Bauteil- oder Messnachweis nötig

### P1

**R-01 · P1 · Mittelleiter-Trennstellen, Signalabschnitte und Booster werden nicht erfasst** (H-01)

- **Ort:**
  - S. 4, Kap. 0, Zeile „Beide Schleifer“
  - S. 32, Kap. 14, Kasten
  - S. 45, Kap. 19, Kasten
  - S. 69, G.2, Regel 1
- **Zitat:**
  - „Schleifer über RT verbinden.“
  - „darf zugleich keine fremden Booster-/Programmierabschnitte überbrücken“
  - „niemals … elektrischen Bremsabschnitt überbrücken“
- **Mechanismus:** RT verbindet beide Schleifer fest über alle Kupplungen. Jede Mittelleiter-Trennstelle wird beim Überfahren überbrückt. Das Verbot lässt sich nicht bedienen, nur durch den Zustand der Anlage einhalten. Einen Prüfschritt dafür gibt es nicht.
- **Bedingung:** Auf der befahrenen Anlage gibt es ein signalabhängig stromlos geschaltetes Gleisstück, ein Bremsmodul oder eine Boostergrenze.
- **Folge:**
  - Eine im Halteabschnitt stehende Lok bekommt über den ICE Fahrstrom und fährt an: **unkontrollierte Bewegung**.
  - An Boostergrenzen fließen Ausgleichsströme über die Kupplungen und die O-Leiterbahnen.
- **Quelle:** LoDi, Seite „LoDi-Motor WiB ICE-M“ (K1): *„Sollten Sie jedoch noch Signale verbaut haben, die den Zug beeinflussen, müssen Sie die LoDi-Motor WiB ICE-M-S verwenden. Hier muss der Schleifer von dem vorderen auf den hinteren umgeschaltet werden.“* Die Anleitung erwähnt weder die Bedingung noch die Variante.
- **Status:** Lücke bestätigt; ob deine Anlage betroffen ist, ist offen.
- **Ersatz:** Neuer Schritt **19.0 „Anlage erfassen“**, Pflicht vor jedem Anlagenbetrieb, in G.2 als Regel 1 verlinken:
  > „Liste jede Mittelleiter-Trennstelle im befahrenen Bereich auf: signalabhängig geschaltete Gleisstücke, Bremsmodule, Boostergrenzen, Programmiergleis-Anbindungen. Gibt es eines davon, darf dieser ICE mit durchverbundenem RT dort nicht fahren. Entweder den Abschnitt dauerhaft digital durchspeisen (Halt nur über CS3 nach Kap. 19) oder die LoDi-Variante ICE-M-S mit Schleiferumschaltung verwenden (eigene Anleitung, verstärkte AUX-Ausgänge nötig). Ohne diese Liste kein Betrieb außerhalb des Prüfgleises.“
- **Art:** T + N (Anlagenbestand).

---

**R-02 · P1 · Vor dem Erststrom fehlt eine Isolationsmesskarte für U+/LED/AUX und freie Trägerlitzen** (H-02, A-01; unabhängig von zwei Instanzen gefunden)

- **Ort:**
  - S. 42, Kap. 17, Kasten „Vor Schritt 52“
  - S. 28, Schritte 34/35
  - S. 30, R4
  - S. 50, Kap. 24 (liegt nach dem Erststrom)
  - S. 52, Kap. E
  - Einziger konkreter Hinweis: S. 49, Tabelle Nr. 1
- **Zitat:**
  - „reale Platinen-/Steckbelegung bestätigt; die jeweils angeschlossene LED-Strombegrenzung bestätigt“
  - S. 49: „nach LED-Einbau deren Plus/Kathoden und Halter getrennt gegen Chassis prüfen“
- **Mechanismus:** Eine vollständige Isolationsmessung mit positiven Kontrollen gibt es nur für M1/M2 (6a). Für diese Netze existiert vor Schritt 52/54 keine Messreihe mit Paaren, Sollwerten und Kontaktkontrollen:
  - VCC bzw. +Ub (= Decoder-U+)
  - L_WS, L_RT, LV, LR, GE
  - hinten: GND, +5V, MR, MV, AUX1–4
  12c-R4 bleibt allgemein. Die Suche im Text nach „gegen Chassis“ findet nur S. 17 (Motorlitze) und S. 49.
- **Bedingung:** Ein LED-Einsatz, sein Halter, eine Lampenfeder oder eine unisolierte Trägerlitze berührt Metall. Das Dokument beschreibt diesen Weg selbst: S. 11 „Kritisch – verdeckte Lampenmasse“.
- **Folge:**
  - U+ an Chassis oder Radmasse: Gleiskurzschluss über eine Gleichrichterdiode des Decoders.
  - LV/LR/GE an Masse: Kurzschlusspfad über den Ausgangstransistor.
  - GND oder +5V an Radmasse: Diode bzw. Regler überlastet.
  - In allen Fällen droht ein Decoderschaden beim ersten Einschalten (52/54).
- **Quelle:**
  - Märklin 60975/60976/60977, S. 4 (K1): „Der gemeinsame Leiter (orange) darf nicht mit der Fahrzeugmasse verbunden werden.“
  - ESU LokPilot 5, S. 28 (K1): LED-Anode an U+, Vorwiderstand nötig.
  - Dokument S. 10/11; Mechanismus nach K2.
- **Status:** Lücke bestätigt; Schadenseintritt hängt von der Hardware ab.
- **Ersatz:** Neue Karte **16c „Messkarte vor Erststrom“**. Sie gehört in den Kasten S. 42, in Kap. E und in G.2-8/9:
  > „Je Kopf, Decoder und Puffer abgezogen, Aufbau wie 6a (PX/PX2 an Chassis bzw. Radmasse, positive Vor- und Nachproben). Soll jeweils OL bzw. der dokumentierte Leerwert der unbestückten Platine:
  > Vorn: VCC, L_WS, L_RT, GE, SW/RT je gegen MASSE und gegen Chassis; zusätzlich GE gegen RT.
  > Hinten: +Ub, LV, LR, GND, +5V, MR, MV, AUX1–AUX4 je gegen 0/GL und gegen Chassis; +Ub gegen B/GR.
  > Die Reihe offen und bei geschlossenem Gehäuse wiederholen. Bei jeder Abweichung Decoder nicht einsetzen.“
- **Art:** T + N.

---

**R-03 · P1 · Motorloser Kopf: Altzustand fehlt, Schleifer nicht belegt, Anschlusshandgriffe fehlen** (H-03, A-05)

- **Ort:**
  - S. 27, Kap. 12, Tabelle und Kasten
  - S. 28, Schritte 32–35
  - S. 30, R1/R3
  - S. 32, Tabelle „Hinterer Decoder“
  - S. 68, G.1-5
- **Zitat:**
  - „Benutze hinten nur +Ub, LV, LR, B/GR und 0/GL“
  - Schritt 34 nennt nur: „Plus an +Ub, Rot … LV, Weiß … LR“
- **Mechanismus:** „B/GR“ steht nur in Tabellen, Kästen und Protokollfeldern (S. 27, 30, 32, 52), in **keinem** Arbeitsschritt. Kein Handgriff:
  - verbindet Schleiferlitze, RT-Kupplungslitze und rote Trägerlitze B/GR;
  - legt 0/GL an einen definierten Radmassepunkt;
  - isoliert die GE-Kupplungslitze im Dummy.

  Für den Dummy gibt es kein Gegenstück zu Kap. 4 (Altzustand, Leitungswege verfolgen). Dass der 2976-Dummy überhaupt einen Mittelschleifer hat, wird vorausgesetzt, aber nicht nachgewiesen. Davon hängen ab:
  - S. 32 „Schleifer B“
  - S. 44 „Einspeisung von hinten“
  - S. 69 G.2-11
- **Bedingung:** Eine alte Verbindung bleibt bestehen (Lampe, Diode, Masseöse zwischen GE-Kupplungskontakt und Schiene), oder der Dummy hat keinen Schleifer.
- **Folge:**
  - Im ersten Fall: Beim Einschalten des Innenlichts (17a T2) sinkt AUX4 direkt gegen die Schiene → Überlast.
  - Im zweiten Fall: Lastprüfung und Architekturannahmen stimmen nicht.
- **Quelle:** Ableitung (K2). Die Textsuche bestätigt die Lücke. Das LoDi-Vergleichsfoto S. 49 (33701) zeigt am Dummy Kupplungs- und Schleiferlitzen; das beweist nichts für den 2976 (K5).
- **Status:** Lücke bestätigt; Hardware offen.
- **Ersatz:** Neues **Kap. 4b „Altzustand motorloser Kopf“** (nach G0), Fotos wie Kap. 4:
  > „1. Schleifer vorhanden? Litze bis zum Schleiferblech verfolgen und fotografieren. 2. Radmassepunkt bestimmen. 3. Beide Kupplungskontakte mit Litzen zuordnen (RT/GE nach 14). 4. Altplatine und Lampe ausbauen; jede Altleitung am GE-Kontakt entfernen.“

  Neuer Schritt **34a**:
  > „Schleiferlitze + RT-Kupplungslitze + rote Trägerlitze B/GR verlöten, isolieren, Zugentlastung. Braune Litze 0/GL an den fotografierten Radmassepunkt. GE-Kupplungslitze einzeln mit Schrumpfschlauch isolieren. MR, MV, AUX1–AUX4, GND, +5V einzeln isolieren. Danach Karte 16c.“

  Ohne Schleifer im Dummy: Kap. 14, 18 und G.2-11 neu fassen.
- **Art:** T + N (Fotos Dummy).

---

**R-04 · P1 · Schnellanleitung G.1-5 wirkt vollständig, lässt aber Isolation und Gleisanschlüsse weg** (S-01)

- **Ort:** S. 68, G.1 Schritt 5; Folge in S. 69, G.2 Schritt 9.
- **Zitat:**
  - G.1-5: „Beim bestätigten Mapping: LED-Plus an +Ub, Rot über eigenen geprüften Widerstand an LV, Weiß … an LR. Keine alte Massefassung verwenden. GE hinten nicht speisen; 59649 noch nicht einsetzen.“
  - G.2-9: „Halter- und LED-Freigabe müssen vorliegen.“
- **Mechanismus:** Die Märklin-Trägerzeichnung (S. 27) zeigt farbcodierte, angelötete Litzen. G.1-5 nennt am Handgriff weder „MR, MV, AUX1–4, GND, +5V einzeln isolieren“ noch B/GR bzw. 0/GL. G.2-9 verlangt vor dem Einsetzen nicht die in 12b-E1 genannte Voraussetzung („alle übrigen Verdrahtungen nach 12/12a geprüft“).
- **Bedingung:** Die Schnellanleitung wird als Abhakliste benutzt. Der Kopf der Seite („kein Ersatz für die Detailkarten“) mildert das, beseitigt es aber nicht, weil der Schritt als Anschlussanweisung formuliert ist.
- **Folge:** Eine blanke GND- oder +5V-Litze an der Radmasse führt beim Einschalten in G.2-9 zu einem Kurzschlusspfad bzw. Rückspeisung → Decoderschaden wahrscheinlich.
- **Quelle:** Vergleich S. 27/28 ↔ S. 68 (K2).
- **Status:** bestätigt.
- **Ersatz G.1-5:**
  > „Halterung nach 12c festlegen (derzeit offen). B/GR an hinteren Schleifer und RT-Kupplungslitze, 0/GL an hintere Radmasse, LED-Plus an +Ub, Rot über eigenen Widerstand an LV, Weiß über eigenen Widerstand an LR. MR, MV, AUX1–4, GND, +5V und hintere GE-Litze einzeln mit Schrumpfschlauch isolieren. Danach Messkarte 16c. 59649 noch nicht einsetzen.“
- **Ersatz G.2-9:** „… Verdrahtung nach 12/12a, Messkarte 16c und Halter 12c bestanden …“
- **Art:** T.

### P2

Kurzform je Befund:

- **Ort**
- **Zitat**
- **Mechanismus** und Bedingung
- **Folge**
- **Quelle** mit Evidenzkategorie
- **Status**
- **Ersatz**
- **Art:** T = Textkorrektur genügt; N = realer Bauteil- oder Messnachweis nötig

---

**R-05 · P2 · F.4: 59649 meldet sich beim Lesen selbst an der CS3 an** (P-01; herabgestuft von P1)

- **Ort:** S. 59, F.4, Bedienfolge 3; zugleich S. 6 B4 und S. 68 G.1-1.
- **Zitat:**
  - „Nach bestandener elektrischer Prüfung STOP aufheben.“
  - „Dieser Werkstatteintrag ist keine zweite automatische Zuganmeldung.“
- **Mechanismus:**
  - M4 ist aktiv, der Sync noch nicht konfiguriert.
  - Die CS3 meldet mfx-Loks auch am Programmiergleis an (CS3-Kurzanleitung ab 2.5, S. 11, K1).
  - Der 59649 legt sich damit als eigene Lok an und kennt ab dann diese CS3.
  - Die Aussage des Dokuments betrifft nur den manuellen DCC-Eintrag.
- **Folge:**
  - Vor dem Sync-Test existiert bereits ein zweiter Loksatz.
  - C3 an derselben CS3 zeigt nicht, ob die Eigenanmeldung unterdrückt wird.
  - Der Laie hält den Eintrag für „vorbestehend“ und damit unkritisch.
- **Quelle:**
  - ESU Master/Slave-Seite (K1): „Beide Decoder werden sich … mit RailComPlus oder mfx automatisch an Ihrer Zentrale anlegen.“
  - LokPilot 5, S. 12 (K1).
- **Status:** wahrscheinlich.
- **Warum herabgestuft:** Das C3-Kriterium „Ist der Slave weiter eigenständig angemeldet und unabhängig steuerbar, ist der Test nicht bestanden“ deckt den Fall formal ab. Es fehlt aber der Handgriff.
- **Ersatz vor F.4-3:**
  > „Achtung: Nach Aufheben von STOP meldet sich der 59649 mit aktivem M4 voraussichtlich als eigene mfx-Lok an. Lokliste vorher fotografieren; neuen Eintrag in ‚59649-EIGEN – nicht fahren' umbenennen, nicht löschen, im C-Protokoll vermerken.“
- **Ersatz C3/54:**
  > „Diesen Eintrag aufrufen, bei Fahrstufe 0 F0 und Richtung schalten: Der hintere Kopf darf nicht reagieren. C3 ersetzt nicht C7.“
- **Art:** T + N.

---

**R-06 · P2 · mfx-Konfiguration über die gemeinsame SID ist ungeprüft** (P-02)

- **Ort:** S. 7 C; S. 42, Schritte 54/55; S. 55 F. Keine Aussage dazu.
- **Mechanismus:**
  - Nach dem Sync empfängt der Slave alle Befehle an die Master-SID, auch mfx-Lese- und Schreibbefehle (CS3 „Lok bearbeiten“).
  - Auf eine mfx-Datenabfrage darf nur ein Decoder antworten (Krauß, Schienenformat mfx 2.3, K2).
  - ESU dokumentiert nur das RailCom-Schweigen des Slaves.
- **Folge:**
  - Lesefehler oder falsche Daten an der CS3.
  - Der Slave übernimmt womöglich Schreibbefehle, die für den 60977 gedacht sind (Mapping, Licht).
- **Status:** offen.
- **Ersatz:**
  > „Bis zum Nachweis ICE-Einstellungen nicht über die CS3-mfx-Konfiguration ändern; 60977 nur ausgebaut am 60971.“
- **Prüfschritt C3b:** ICE-Konfiguration mit und ohne Slave lesen und vergleichen; eine harmlose mfx-Änderung vornehmen; danach den 59649 nach F.4 lesen und die Altwerte vergleichen.
- **Art:** N.

---

**R-07 · P2 · Nebenwirkungen der F-Tasten F1–F31 am Slave werden nie geprüft; G0 läuft mit anderem Projektstand** (P-06)

- **Ort:**
  - S. 7 C4/C5; S. 43 T1–T8 (nur F0, Richtung, Innenlicht, Sound)
  - S. 28, 12a („Keine zusätzlichen … Mappingzeilen …“)
  - S. 39, Schritt 46: ICE-Soundprojekt erst nach G0
- **Mechanismus:**
  - Der Slave folgt jedem Funktionsbefehl an die gemeinsame SID.
  - Das ESU-Werksmapping (z. B. Dimmer, Rangierlicht) wurde nie mit den belegten Tasten des ICE-Soundprojekts abgeglichen.
  - G0 prüft mit dem Werksprojekt. Ein späterer mDT3-Transfer kann Projekt und Firmware ändern.
- **Folge:**
  - Die Rückleuchte dimmt oder erlischt beim Betätigen einer Soundtaste.
  - Die G0-Freigabe bezieht sich auf einen anderen Stand.
- **Status:** offen.
- **Ersatz – Test T9 (in C5, 54 und 17a):**
  > „F0 ein, Fahrstufe 0: jede im 60977-Projekt belegte Taste F1–F31 einzeln ein/aus; Rot/Weiß beider Köpfe bleibt unverändert; je Taste protokollieren.“
- **Zusatz Schritt 49:**
  > „Nach letztem Projekttransfer Firmware des 60977 neu auslesen; bei Änderung C2–C7 wiederholen; Firmwareangebot in mDT3 ablehnen.“
- **Art:** N.

---

**R-08 · P2 · Die Schreibkarte F.6 taugt nicht für indizierte Mapping-CVs** (P-05)

- **Ort:** S. 28, Schritt 33; S. 39, Schritt 47; S. 61, F.6.
- **Zitat:** „F.6 erklärt nur deren Übertragung“.
- **Mechanismus:**
  - Das ESU-Mapping liegt oberhalb von CV 256; vor jedem Zugriff muss der Index CV31/CV32 geschrieben sein.
  - F.6 kontrolliert per „Decoder auslesen“ der Gesamtliste. Das setzt keinen Index.
  - Altwerte und Schreibziel landen dann auf einer unbekannten Indexseite.
- **Quelle:**
  - ESU „CV-Änderungen anzeigen“ (K1): Index nur für CVs > 255 relevant.
  - Märklin CV-Editor-Hilfe (K1): sofortiges Schreiben.
- **Status:** wahrscheinlich.
- **Ersatz – Abschnitt „Indizierte CVs“ in F.6:**
  > „CV31 schreiben + frisch zurücklesen, CV32 ebenso; erst dann Ziel-CV lesen (Altwert), schreiben, zurücklesen; vor jeder weiteren indizierten Zeile Index erneut schreiben und kontrollieren; nie über die Gesamtliste kontrollieren; am Ende CV31/32 auf Altwerte zurück.“
- **Art:** T. Die Werte selbst brauchen N (Export).

---

**R-09 · P2 · Widerspruch bei der Prüfaufnahme: A verlangt einen Motor, F.4 geht motorlos vor** (P-03)

- **Ort:** S. 5, Kap. A, Tabelle; S. 59, F.4.
- **Zitat:**
  - S. 5: „Er muss je Aufnahme Steckschnittstelle, Motor und Lautsprecherlast benennen“
  - S. 59: „Quittierfähigkeit des konkreten motorlosen 59649-Aufbaus … noch nicht gemessen“
- **Mechanismus:** Ob die Quittierung klappt, hängt von der Last ab. Schlägt das Lesen fehl, endet F.4 in einer Sackgasse („STOP, nichts schreiben“), und Ersatzlasten sind verboten (S. 5).
- **Status:** bestätigt.
- **Ersatz F.4:**
  > „Den 59649 ausschließlich in der nach A benannten Prüfaufnahme mit Motor lesen. Scheitert das Lesen zweimal: Aufnahme, CS3-Version, Fehlermeldung an den Prüfenden; keine Ersatzlast improvisieren.“
- **Art:** T.

---

**R-10 · P2 · Ohne LokProgrammer gibt es keinen Leseweg für die Firmware des 59649 und für die SID** (P-04)

- **Ort:**
  - S. 64, F.9, Stufen 1 und 6
  - S. 65, F.10, Feld „Firmware / verlässlicher Ausleseweg“
  - S. 7, C8
- **Mechanismus:** G0 verlangt Firmwarestände und eine „nachweislich andere SID“. Das Dokument nennt aber keinen Weg, beides ohne 53451 festzustellen. Die Mindestfirmware für den Sync am LokPilot 5 ist unbelegt: ESU nennt nur „LokSound 5 ab 5.1.101“, die LokPilot-5-Anleitung gilt „ab Firmware 5.3.128“.
- **Status:** offen.
- **Ersatz:**
  > „Firmware 59649 nur auf einem von ESU oder Fachbetrieb bestätigten Weg (z. B. LokProgrammer des Fachbetriebs) lesen; nicht aus CV7 ableiten. SID-Anzeige der CS3 vor/nach C7 am realen Bildschirm fotografieren; ohne Foto bleibt F.9-6 offen.“
- **Art:** N.

---

**R-11 · P2 · C7 hat keinen gangbaren Weg – G0 ist nicht abschließbar** (A-09)

- **Ort:** S. 7, C7; S. 5 (nur eine CS3); S. 64, F.9 Stufe 6.
- **Zitat:**
  - „An einer Testzentrale, die den Master noch nicht kennt … Ohne Nachweis G0 offen; keine produktiven Lokdaten löschen.“
  - „Keine bestehende CS3-Lokdatenbank dafür pauschal löschen“
- **Mechanismus:** Die Ausstattung umfasst genau eine CS3, und die kennt den Master nach C2. Einen konkreten Weg zu einer zweiten Zentrale oder einer kontrollierten Neuanmeldung nennt das Dokument nicht; ebenso wenig Bestehenskriterien für die delegierten Prüfungen:
  - C6 „fachkundiger Prüfaufbau“
  - Kap. 18, Schritte 57/59
  - 12c-R3
  - F.4-3 „bestandene elektrische Prüfung“
- **Folge:** G0, das Tor zu allem Weiteren, bleibt für den Anwender unentscheidbar.
- **Status:** bestätigt.
- **Ersatz C7:**
  > „Testzentrale: eine zweite mfx-fähige Zentrale, die diesen 60977 nie gesehen hat (geliehen oder beim Fachbetrieb; Eignung vorher klären). Bestanden, wenn: (a) SID alt und neu fotografisch dokumentiert und verschieden, (b) der Slave ohne Neukonfiguration F0 und Richtung folgt, (c) kein zusätzlicher Loksatz entsteht (Foto der Lokliste vor/nach).“
- **Zusatz für jede Delegation:** Liste der geforderten Ergebnisse und Grenzwerte, vorab schriftlich.
- **Art:** T + N.

---

**R-12 · P2 · Die Gate-Tabelle ist in sich unstimmig und unvollständig** (A-02, A-14)

- **Ort:** S. 1, Tabelle; S. 20, Schritt 22; S. 13, Kasten; S. 51, D „Foto 2“; S. 52, Kasten.
- **Mechanismus:**
  - G1 (1–3, 8–9b) steht vor G2 (4–7). Schritt 22 („Platine an den vorgesehenen Haltepunkten auflegen“) braucht aber den entkernten Kopf aus Kap. 4, und das Löten in 9a braucht 6b.
  - S. 52 verlangt vor G0 die „Fotos aus D“. Foto 2 („LoDi an vorgesehener Position“) erfordert Zerlegen – das ist vor G0 verboten (S. 1, 4, 11).
  - Folgende Teile sind keinem Gate zugeordnet: 0, 9c, 14c–e, 16–16b, 20, 23, D, E, F, G.
  - S. 2 sagt „Zuerst A-C und F“, die Tabelle nur „A-C“.
- **Status:** bestätigt.
- **Ersatz:**
  > „G0 (A–C, F) → G2 (4–7, 21–23) → G1 (8–9b; Löten 9a erst nach 6b) → G3 (10–14e) → G4 (16–18, 24) → eigene Freigaben (15, 19.0/19).“

  In S. 52 ergänzen: „vor G0 nur Fotos 1, 3, 4 (lose Teile); Foto 2 erst nach G0“.
- **Art:** T.

---

**R-13 · P2 · Kap. E ist ein Freigabezirkel** (A-06)

- **Ort:** S. 52.
- **Zitat:** „Vor dem ersten Einschalten diese Werte … übertragen. Ein leeres Feld ist keine Freigabe.“
- **Mechanismus:** In der Tabelle stehen Felder, die erst nach dem Einschalten entstehen: „Inbetriebnahme 52-56, Lastprüfung 57-59 und Gehäuseprüfung 24“ und „Prüfung L1-L5“ (L5 ist der Soundtest).
- **Folge:** Wörtlich befolgt wird nie eingeschaltet. Der Laie lernt dabei, Sperren zu übergehen.
- **Status:** bestätigt.
- **Ersatz:** E teilen in „E1 – vor Erststrom“ (Identität, Revision, Jumper, Ringe, 6b, 16c, R-Werte, 12c, 14a/14b) und „E2 – Abnahme“ (52–56, 57–59, 24, L5, 19).
- **Art:** T.

---

**R-14 · P2 · Die Erststrom-Reihenfolge ist unscharf; der Dummy kommt ohne Programmiergleis-Test ans Betriebsgleis** (A-07, H-07, S-03)

- **Ort:** S. 42, Schritte 52 und 54; S. 69, G.2-8.
- **Zitat:**
  - Schritt 52: „Nur den Motortriebkopf aufstellen; … 60977 erst jetzt nach 9c einsetzen“ – ohne STOP, anders als Schritt 54.
  - Schritt 54: „auf dasselbe … gemeinsam gespeiste Gleisstück“ – das ist das Betriebsgleis aus 52.
- **Mechanismus:**
  - Die Textreihenfolge in 52 lautet: aufstellen, dann einsetzen. 9c-M1 ist nur ein Zustand („sind abgetrennt“), kein Handgriff.
  - Der Dummy wird nie strombegrenzt am Programmiergleis vorgeprüft.
- **Folge:**
  - Stecken unter Spannung ist möglich (C6 verbietet es).
  - Ein Verdrahtungsfehler am Dummy trifft den vollen Gleisausgang.
- **Quelle:** Märklin-Beilage S. 6 (K1), im Dokument selbst als Bild auf S. 29 enthalten: *„Modell noch ohne Gehäuse auf dem Programmiergleis einer Prüfung unterziehen.“*
- **Status:** bestätigt.
- **Ersatz 52:**
  > „CS3 STOP; Kopf vom Gleis; Hilfsleitungen entfernt (6b); 9c M1–M3; Sichtkontrolle; Kopf aufs Programmiergleis; erst dann STOP aufheben …“
- **Neuer Schritt 53a:**
  > „Dummy allein ohne Gehäuse, Kupplung frei und isoliert, am getrennten Programmiergleis; nur CV8 lesen (F.4 Nr. 4–5, Erwartung 151). Bei Lesefehler/Überlast: STOP, 16c wiederholen. Erst dann 54.“
- **Art:** T.

---

**R-15 · P2 · Fahrt und volle Innenlichtlast liegen vor der Lastabnahme; kein prüfbares Summenkriterium** (A-08 + eigene Ergänzung)

- **Ort:**
  - S. 43, 17a, Kasten („vorhandene Weichen/Kurven langsam befahren“) und T2/T8
  - S. 39, Schritt 50 („Fahrt ausschließlich Schritt 53“)
  - S. 28, Schritt 35 (Fahrtprobe Dummy)
  - S. 44, Kap. 18, Schritte 57–59
- **Mechanismus:**
  - Der RT-Pfad kann den ganzen Motorstrom führen (S. 34/44). AUX4 trägt alle Wagen.
  - Beides wird belastet (Fahrt, T2/T8 mit allen Wagen), bevor Kap. 18 abgenommen ist. Kap. 18 delegiert ohne Grenzwerte.
  - Die Stromaufnahme je LoDi-Wagen ist nirgends angegeben (auf den LoDi-Seiten nicht gefunden).
  - Die Fahrfreigaben widersprechen sich (50 ↔ 17a ↔ 35).
- **Folge:** AUX4 (≤ 250 mA; Licht + AUX gesamt ≤ 300 mA, Märklin K1) und die Kupplungskontakte werden belastet, bevor die Belastbarkeit bewertet ist.
- **Status:** Reihenfolge bestätigt; Hardware offen.
- **Ersatz:**
  - Reihenfolge: 17a nur Standtest → Kap. 18 → erst dann Fahrtest.
  - Schritt 35: nur Standtest.
  - In 16b/18 ergänzen:
    > „Vor Schritt 56 Stromaufnahme einer Wagenplatine (LoDi-Angabe oder Messung durch Fachbetrieb) × Wagenzahl + vordere Front-LEDs berechnen; Summe AUX ≤ 250 mA, Licht + AUX ≤ 300 mA. Liegt der Wert nicht vor, höchstens einen Wagen anschließen.“
- **Art:** T + N.

---

**R-16 · P2 · Das LV/LR-Mapping wird in G0 nicht protokolliert** (A-10)

- **Ort:** S. 28, Schritt 33; S. 7, C4/C8.
- **Zitat:** „Passt das in G0 geprüfte LV/LR-Mapping …“
- **Mechanismus:** C4 prüft nur „folgen dem Richtungsbefehl“ und „F0 aus → aus“. Welcher Ausgang je Richtung an welchem Decoder aktiv ist, wird nirgends festgehalten.
- **Folge:** Es wird nach unbewiesenem Mapping verdrahtet.
- **Status:** bestätigt.
- **Ersatz C4/C8 – Tabelle:**
  > „vorwärts: Master LV an / LR aus; Slave LV an / LR aus. rückwärts: Master LR an / LV aus; Slave LR an / LV aus – je Decoder am Prüfaufbau beobachtet.“
- **Art:** T + N.

---

**R-17 · P2 · Für ESU-Änderungen nach dem Einbau fehlt die Trennregel** (A-11)

- **Ort:** S. 26, 11a-H2; S. 39, Schritt 47; S. 32, Kasten; F.7, S. 62.
- **Mechanismus:** H2 und 47 verlangen ESU-Änderungen am fertigen Zug. Dass DCC-Servicebefehle über RT beide Decoder erreichen, steht nur in F.7. S. 32 verbietet nur, dass ein Kopf am Programmiergleis und der andere auf der Anlage steht.
- **Folge:** Ein Schreibbefehl (Helligkeit, CV31/32, schlimmstenfalls CV8) wirkt auch auf den 60977.
- **Status:** bestätigt.
- **Ersatz in H2/47:**
  > „Zum Programmieren den Zug stromlos trennen; nur den Dummy ohne Kupplungsverbindung aufs Programmiergleis; ganzer Zug nie aufs Programmiergleis (G.2 Regel 1).“
- **Art:** T.

---

**R-18 · P2 · Vergleichsfoto-Tabelle S. 49 widerspricht 12c** (A-12)

- **Ort:** S. 49, Zeile „2 und 3 – hohe graue Stützen“.
- **Zitat:** „Neue Platine zunächst ohne Decoder auflegen … dann wie Schritt 23 prüfen.“
- **Widerspruch:** S. 30: „Die hohen Stützen … sind keine bestätigte Aufnahme“, „Die LoDi-Ringprüfung aus 9 gilt hier nicht“.
- **Status:** bestätigt.
- **Ersatz:**
  > „Aufnahme der Altplatine; im REV9-Aufbau keine Aufnahme für den Märklin-Träger; Befestigung ausschließlich nach 12c.“
- **Art:** T.

---

**R-19 · P2 · Kap. 24: Nachlöten ohne Nachprüfung, keine Methode für den Freiraum, zweites Schließen unkontrolliert** (A-13, H-09 + eigene Ergänzung)

- **Ort:** S. 50, Nr. 1 und Nr. 6; S. 44, Schritt 60; S. 69, G.2-11.
- **Zitat:**
  - Nr. 1: „nötigenfalls LED-/Platinenelektronik abtrennen“
  - Nr. 6: „ursprüngliche Anschlüsse … herstellen. Decoder spannungsfrei einsetzen. Freiraum … prüfen“
- **Mechanismus:**
  - Neu gelötete Anschlüsse nach der geschlossenen Prüfung werden nicht nachgeprüft.
  - Wie der Freiraum mit Decoder geprüft wird, bleibt offen; Messen mit Decoder ist ja verboten.
  - Ein kontrolliertes zweites Schließen (Litzenlage) fehlt.
  - Schritt 60 lässt offen, ob die Funktionsprüfung offen oder geschlossen erfolgt.
- **Status:** bestätigt.
- **Ersatz Nr. 6/7:**
  > „Nur tatsächlich abgetrennte Anschlüsse neu löten und je Anschluss 16c-Paar wiederholen. Decoder stromlos einsetzen. Gehäuse ohne Schrauben aufsetzen, seitlich Abstand über Decoder/Lautsprecher prüfen; es muss ohne Druck aufliegen; Druckstellen kontrollieren; bei Kontakt Metallgegenfläche isolieren, Decoder nicht einwickeln. Stromlos wie Nr. 3 schließen, Litzenlage mit Foto aus Nr. 3 vergleichen; dann 17a am geschlossenen Zug.“
- **Art:** T.

---

**R-20 · P2 · Mehrdeutige Bezeichner verfälschen Messungen** (A-04)

- **Ort:** S. 34, 14b-W1 („O-A gegen O-B“) gegenüber S. 35–37 („B-O/B-L“) auf derselben L/O/B-Platine.
- **Weitere Mehrfachbedeutungen:**
  - „B“: Gleis B, Kap. B, Ring B, Schleifer B, „Wagen-B“, Wagenende B
  - R4: Widerstand und Schritt 12c-R4
  - M1/M2: Bürsten; M1–M3: Einsetzschritte
  - K1: Relaisfeld, Kupplungsname, Prüfschritt 14a
  - C1–C8, D1–D4, E1–E3: gleichnamig mit den Kapiteln C/D/E
  - „Prüfenden“: Person und Prüfleitungsenden (S. 44/50)
- **Folge:** W1 wird am freien B-Pad gemessen (OL). Dann ist die Ausgangsbasis falsch, W5 wertlos, und eine L–O-Lötbrücke (Gleis an AUX) bleibt unerkannt.
- **Status:** bestätigt.
- **Ersatz:**
  - Wagenenden „Ende 1/Ende 2“
  - Befestigungsringe „Ring K1-seitig/Ring frontseitig“
  - Schrittpräfixe „9c-1“, „12c-1“ …
  - „Prüfleitungsenden“ statt „Prüfenden“
  - Titel 14c: „Achsschleifer an das Wagenpad B“
- **Art:** T.

---

**R-21 · P2 · Keine Wiederholungspflicht nach Umreihen, Drehen oder Tauschen von Wagen** (H-08)

- **Ort:** S. 32, Schritte 40/41; S. 33, 14a; S. 46.
- **Mechanismus:** Eine einzige RT/GE-Kreuzung legt den Dummy-Schleifer (Gleis) auf GE, also auf AUX4. Beim Einschalten des Innenlichts entsteht ein Kurzschlusspfad über AUX4 und den Gleichrichter. Zwei Kreuzungen heben sich außen auf; der betroffene Wagen läuft dann verpolt.
- **Bedingung:** Die Kupplungsgeometrie lässt eine Kreuzung zu (gedrehter Wagen, Teiletausch).
- **Status:** Mechanismus bestätigt (K2); Geometrie offen.
- **Ersatz:**
  > „Reihung und Orientierung markieren. Nach jedem Umreihen/Drehen/Teiletausch vor dem Einschalten 14a/14b der betroffenen Stellen wiederholen. Gesamtzugprüfung ohne Decoder/Puffer: vorderes RT ↔ hinteres B/GR niederohmig; vorderes GE ↔ hinteres B/GR nicht niederohmig; GE ↔ Radmasse jedes Fahrzeugs nicht niederohmig.“
- **Art:** T + N.

---

**R-22 · P2 · Netze der LoDi 511 werden nur nach Aufdruck zugeordnet; die V1.49-Zeile ist schwach belegt** (H-04)

- **Ort:** S. 19, 8a, Zeile V1.49; S. 21, 9a, Tabelle und Schritt 24.
- **Mechanismus:** Gleis 0 und Decoder-GND sind der gefährlichste Verwechslungsfall (S. 10). Trotzdem gibt es keinen Durchgangsnachweis:
  - MASSE ↔ 21MTC-Kontakt 21 (nicht 20)
  - SW/RT ↔ 22
  - VCC ↔ 16 (nicht 12)
  - GE ↔ 4 bei SJ1 bzw. 15 bei SJ2
- **Belege:**
  - LoDi nennt Jumper erst ab V1.50 (K1).
  - Die LoDi-Funktionsliste „Aux 4 = Wagenbeleuchtung“ (K1) stützt die V1.49-Annahme, belegt aber nicht den GE-Pfad.
- **Status:** offen, geringe Wahrscheinlichkeit eines Fehlers.
- **Ersatz:**
  > „An der leeren LoDi 511 von LoDi bestätigen lassen oder fachkundig messen: MASSE–21 niederohmig, kein Kontakt zu 20; SW und RT–22; VCC–16; LS1/LS2–9/10; MOT_L/MOT_R–18/19; GE–4 (SJ1) bzw. –15 (SJ2). Für V1.49 GE-Pfad nur nach Messung/LoDi-Aussage eintragen.“
- **Art:** N.

---

**R-23 · P2 · Die 21MTC-Stiftleiste auf dem eigenen Foto ist anscheinend von einer Bestückungskappe verdeckt** (H-05; eigene Vergrößerung bestätigt das Bild)

- **Ort:** S. 18, Foto, Marker 1; S. 23, Marker 1; 9c-M2/M3.
- **Bildbefund:**
  - Eine flache schwarze, quadratische Fläche verdeckt die mittleren 5 von 11 Spalten beider Reihen.
  - Sichtbar sind links 2 und rechts 4 Spalten, jeweils beide Reihen bestiftet.
  - Die Indexlücke ist nicht sichtbar.
- **Mechanismus:**
  - M2 („Indexposition 11 … deckungsgleich“) ist so nicht prüfbar.
  - M3 („nach unten drücken“) drückt womöglich auf die Kappe bzw. auf eine nur SMD-gelötete Leiste ohne Abstützung.
- **Folge:** Unvollständiger Sitz, verbogene Stifte, abgerissene Pads.
- **Status:** wahrscheinlich (Bild, K2/K5).
- **Ersatz vor M1:**
  > „Prüfen, ob auf der Stiftleiste eine flache schwarze Kappe sitzt; falls ja, nicht darauf drücken, mit LoDi klären und abnehmen; danach alle Stifte und die Indexlücke von oben fotografieren. Beim Aufstecken die rote Platine direkt unter der Leiste auf nichtleitender Unterlage abstützen.“
- **Art:** N.

---

**R-24 · P2 · Die feste Verbindung SW–RT und die Variante ICE-M vs. ICE-M-S sind nicht nachgewiesen** (H-06)

- **Ort:** S. 18, Foto oberes Drittel; Punkt 2 („K1 ist das hier unbestückte Relaisfeld“); S. 21, 9a.
- **Mechanismus:**
  - Die Architektur verlangt SW und RT dauerhaft verbunden.
  - Auf dem Foto fehlt das Relais, andere Bauteile im K1-Bereich sind aber bestückt (Transistoren, Dioden, 0-Ω-Brücken).
  - LoDi-Funktionsliste (K1): „Aux 1 = Schleiferumschaltung Triebwagen 1 / Aux 2 = … Triebwagen 2“ in der S-Variante.
  - SJ2 legt das Innenlicht auf AUX1.
- **Folge:** Ist RT je nach Bestückung nicht durchverbunden, fällt der Dummy aus. Außerdem kann das Innenlicht auf AUX1 mit einer Umschaltfunktion kollidieren.
- **Status:** offen.
- **Ersatz:**
  > „Mit LoDi die Variante (ICE-M ohne Umschaltung) bestätigen; an der leeren Platine SW–RT messen: niederohmig und stabil. Sonst nicht nach diesem Plan verdrahten.“
- **Art:** N.

---

**R-25 · P2 · DCC/MM bleiben mit Standardadressen aktiv; der Serviceeintrag bleibt bestehen** (P-07 + eigene Ergänzung)

- **Ort:** S. 59, F.4-1 („SERVICE ESU59649 - nicht fahren“); S. 61, F.6 Ende; S. 62, F.7.
- **Mechanismus:** Beide Decoder behalten DCC/MM. Märklin rät, nicht benötigte Protokolle über CV 50 abzuschalten; die Beilage S. 6 ist im Dokument auf S. 29 sichtbar (K1).
- **Bedingung:** Eine andere Lok mit gleicher DCC- oder MM-Adresse oder der Serviceeintrag wird bedient.
- **Folge:** ICE-Licht oder ICE-Motor folgen unbeabsichtigt.
- **Status:** offen. Märklins Protokollvorrang (mfx vor DCC) mindert das Risiko beim 60977.
- **Ersatz Ende F.6:**
  > „Serviceeintrag auf eine im Bestand unbenutzte DCC-Adresse setzen oder nach Sicherung löschen. Vor Anlagenbetrieb DCC-/MM-Adressen beider Decoder auslesen und mit dem Bestand abgleichen; Abschalten nicht benötigter Protokolle (60977: CV 50) erst nach G0 und nur nach separater Prüfung, da der CS3-DCC-Leseweg für den 59649 DCC voraussetzt.“
- **Art:** T + N.

---

**R-26 · P2 · Schnellanleitung G.1-6: Prüfreihenfolge umgekehrt** (S-02)

- **Ort:** S. 68, G.1-6.
- **Zitat:** „RT an O, GE an L; … Kupplungen nach 14a, bestückte Wagen nach 14b prüfen.“
- **Mechanismus:** 14a geht nur an freien Litzen. W1-Ausgangswerte müssen vor dem Anlöten stehen. Die B-Prüfung (14e) verlangt abgetrennte Kupplungslitzen.
- **Status:** bestätigt.
- **Ersatz:**
  > „Je Wagen: Passprobe → W1-Ausgangswerte der unverdrahteten Leiste → Litzen einzeln nach 14a → optional Achsschleifer 14c/14e (Kupplungslitzen ab) → erst dann RT an O, GE an L → W4/W5.“
- **Art:** T.

---

**R-27 · P2 · Schnellanleitung G.2-8: Handgriffe vor dem Stecken fehlen** (S-03)

- **Ort:** S. 69, G.2-8.
- **Zitat:** „Erst jetzt 60977 nach 9c einsetzen.“
- **Es fehlen:**
  - STOP bzw. Versorgung trennen
  - Hilfsleitungen entfernen (6b)
  - lose Litzen und Kupplungslitzen isolieren
  - „Richtung nur über 9a korrigieren“
- **Status:** bestätigt.
- **Ersatz:**
  > „CS3 STOP, Kopf vom Gleis; Hilfsleitungen entfernt; lose und Kupplungslitzen einzeln isoliert; 60977 nach 9c; gemäß Schritt 52 erst Programmiergleis, dann stromlos umsetzen …; falsche Fahrtrichtung nur über Motorlitzen nach 9a (Decoder ab, 6a wiederholen).“
- **Art:** T.

---

**R-28 · P2 · Schnellanleitung G.2-11: Hilfsleitungen entfernen und kontrolliertes Schließen fehlen** (S-04)

- **Ort:** S. 69, G.2-11.
- **Mechanismus:** Es fehlt „wieder öffnen, alle Hilfsprüfleitungen entfernen“ (24 Nr. 6; 6b). Clip-Litzen können im bestromten Fahrzeug bleiben.
- **Status:** bestätigt.
- **Ersatz:**
  > „… danach öffnen, Hilfsleitungen entfernen, Decoder stromlos einsetzen, Freiraum nach 24-6 prüfen, stromlos erneut schließen (Litzenlage wie im Passivtest) …“
- **Art:** T.

### P3

Alle P3-Befunde sind bestätigt, außer wo in der Tabelle anders angegeben. Art: T = Textkorrektur genügt; N = Nachweis nötig.

| ID | Ort | Befund und Mechanismus | Ersatz / Maßnahme | Art |
|---|---|---|---|---|
| R-29 (A-03) | S. 2, 26, 38, 49, 69 | **Nummernkollision Seite/Schritt/Kapitel:** „Decoder erst vor 52/54 stecken“ (S. 2, im selben Absatz: „Seitenzahlen = PDF-Seiten“); „nach dem in 42-44 beschriebenen Nachweis“ (S. 38); „nach 60/24“ (S. 26); „wie Schritt 23“ auf der Seite von Kap. 23 (S. 49); „Schritten 1-6“ (S. 69) | Durchgängig „Schritt 52“, „Kap. 24“, „S. 50“ schreiben; Schrittnummern mit Kapitelpräfix | T |
| R-30 (A-14) | S. 14, Schritt 15 | „Schwarz bleibt ausschließlich bei den Isolationsmessungen 3 und 4 an PX“ widerspricht 6a, Zeilen 1 und 5 (dort ebenfalls Schwarz an PX) | „Schwarz bleibt in den Zeilen 1, 3, 4 und 5 an PX; in 2 und 6 an PM2.“ | T |
| R-31 (A-14) | S. 12 / 13 / 16 | **Drei verschiedene Freigabebedingungen für die Motorlitzen:** „bis Ende Kapitel 6b“, „nach 6b/9a“, „nach G1/G2“ | Einheitlich: „MOT_L/MOT_R erst nach bestandenem 6b und abgeschlossener Padzuordnung 9a anlöten.“ | T |
| R-32 (A-14) | S. 42, Schritt 53 | „Bei falscher Richtung Motorzuordnung nach 9a korrigieren“ – ohne „stromlos, Decoder ab, danach 5a-D4/6a wiederholen“ | Ergänzen wie genannt; Richtung nie über CV29 (Slave würde nicht mitdrehen) | T |
| R-33 (A-14, H-10) | S. 42, Schritt 55 | „Dummy … abkoppeln“, obwohl die Köpfe nach 54 ungekoppelt sind | „Dummy spannungsfrei vom Gleis nehmen, wieder aufsetzen, erneut starten.“ | T |
| R-34 (H-12) | S. 25, Kap. 11 | „Die Widerstandstoleranz muss auch beim kleinsten tatsächlichen Widerstand eingehalten werden“ ist unklar formuliert | „Die Stromgrenze muss auch beim kleinsten möglichen Widerstand (Nennwert minus Toleranz) eingehalten sein.“ Rechnung selbst korrekt | T |
| R-35 (H-13) | S. 12 / 15 / 16 | Ohmtest allein übersieht einen Masse-Kondensator (sagt das Dokument selbst); ergänzende Messung fehlt | Optional: mit Kapazitätsbereich M1–Chassis und M2–Chassis messen (Motor abgetrennt): keine nF-Anzeige. Ergänzt die Sichtverfolgung, ersetzt sie nicht | T+N |
| R-36 (H-14) | S. 34, 14b-W1 | Die LoDi-Wagenplatine hat C1/C2 für einen Stützelko (LoDi K1); 14b verlangt kein Abtrennen, 14c/14e schon | W1: „Stützelko an C1/C2, falls vorhanden, abgetrennt und entladen nachgewiesen.“ | T |
| R-37 (P-08) | S. 59 F.4-4; S. 61 F.6-1 | **Offen:** Vorgabewert einer neu hinzugefügten CS3-CV-Zeile und mögliches Auto-Schreiben sind undokumentiert (Märklin K1: Schreiben beim Verlassen des Feldes) | Vor F.4 das Verhalten von „CV hinzufügen“ an der realen CS3-Version bestätigen lassen; Vorgabewert fotografieren | N |
| R-38 (P-09) | S. 56 Titel; S. 64 | „F.1. Die **nachgewiesenen** Synchronisations-CVs“ und „Die Recherche **schließt** die bisherige Registerlücke“ überzeichnen JMRI (K3). ESU (K1) beschreibt einen eigenen Aktivierungsschalter „unter Sonderoptionen“, der in JMRI fehlt | Titel: „In JMRI implementierte Synchronisationsfelder“; S. 64: „grenzt die Registerfrage ein“; S. 56: „ESU beschreibt einen eigenen Aktivierungsschalter; dessen Register ist unbekannt.“ | T |
| R-39 (P-10) | S. 39, Schritt 46 | CV52 = 3 = C90 ist Märklin-belegt; die **Zuordnung 60941 → C90** ist abgeleitet. Märklin nennt 60941/60943/60944 nur als Umrüstung für Feldspulenmotoren | „… (Zuordnung abgeleitet; beim Märklin-Service bestätigen lassen)“ | T |
| R-40 (P-11) | S. 39, Schritt 45; S. 6 B1 | „Nie beide Decoder am Programmer lassen“ legt nahe, der 59649 dürfe allein an den 60971 – S. 5 verbietet das. Die Abbau-Reihenfolge in B1 ist durch die zitierte Quelle nicht belegt | „Am 60971 ausschließlich den 60977; den 59649 nie auf den 60971.“ B1-Abbaufolge als eigene Ableitung kennzeichnen | T |
| R-41 (P-12, S-06) | S. 69, Kasten Regeln 2/4; S. 59 | Regel 2 führt den ESU-Reset (CV8 = 8) unter „Keine Einmessfahrt“; die ESU-Auslösung CV54 = 0 + F1 fehlt. Regel 4 („Beide 60974 … abgetrennt“) lässt „höchstens einer, nur vorn“ weg | „In keinem Decoder in CV8 schreiben. Keine Einmessfahrt: 60977 CV7/Firmwarefeld ≠ 77; 59649 nicht CV54 = 0 + F1.“ / „Höchstens ein 60974, nur vorn am 60977, erst nach Kap. 15.“ | T |
| R-42 (P-13) | S. 53–54, 66–67 | **Quellenmetadaten:** NMRA-Appendix-Datum veraltet (live: rev. 17-Aug-2026); CAN-Protokoll UID/SID auf S. 8/28 statt 19/28; 60977 „Stand 10/2025“ und „S. 16“ nicht bestätigt; ECoS S. 24–25 (Quittierung) nicht gefunden; LokPilot-5-Anleitung gilt ab Firmware 5.3.128 (fehlt); Krauß 0x83/0x7F-Aussagen nicht auffindbar | Angaben korrigieren oder als „nicht verifiziert“ kennzeichnen | T |
| R-43 (P-14, A-15) | S. 29, 53–67, 3 | **Layout:** Die Märklin-Zeichnung S. 29 ist oben beschnitten (Warn-„!“ und Detailkreis zur Stecklage halb abgeschnitten; im eingebetteten Bild vollständig vorhanden). S. 55–67 ohne REV9-Fußzeile. Quellennummern Hauptteil (1–24) und F (1–23) doppelt belegt. TOC-Einrückung G.1/G.2 abweichend. Quellen 23/24 hinter „Bildquellen“ | Bildrahmen korrigieren; Fußzeile ergänzen; F-Quellen „F-1 …“ | T |
| R-44 (A-15) | S. 1 unten; S. 51 Kasten | Interne Metatexte an den Anwender: „vollständige externe Findingtabelle liegt noch nicht vor“, „86 konsolidierten Findings samt adversarialer Bewertung“ | In einen Änderungsvermerk außerhalb der Arbeitskarten verschieben | T |
| R-45 (eigen) | S. 15 Kasten; S. 47 Kasten; S. 68 G.1-2 | „Am 60941 bleibt nur der Kondensator zwischen den beiden Bürstenfahnen“ setzt einen Quer-Kondensator voraus. Laut Sammlerquelle (K4) enthält der 60941-Satz Anker, Motorschild, Magnet, Bürsten, Schrauben, Lötfahne, 2 Entstördrosseln 3,9 µH – **keinen Kondensator** | „Ist ein Kondensator zwischen den Bürstenfahnen vorhanden, bleibt er; einen fehlenden nicht ohne Freigabe nachrüsten.“ Beilage 60941 im Original prüfen | T+N |
| R-46 (eigen) | S. 21, 9a, Zeile VCC; S. 10; S. 38 | Die LoDi-Beschriftung „VCC“ (= Orange = Decoder-U+) kollidiert begrifflich mit „interne Vcc“ (21MTC-Pin 12, S. 10/38). S. 21 sagt nicht ausdrücklich „= Decoder-U+, Pin 16“ | „VCC (LoDi) = Decoder-U+ (21MTC-Kontakt 16), nicht Pin 12 (Vcc intern).“ | T |
| R-47 (S-05, S-07) | S. 68/69 | **Schnellanleitung, Navigation/Wortlaut:** G.1-1 nennt die Identitätskette B1–B3/F.3, den Aktivierungsexport F.5 und „59649 nie auf den 60971“ nicht. G.2-7 „bestätigte M4-Synchronisation … erhalten“ kann als erledigt gelesen werden. Keine Links zu Kap. 2/3 (Multimeter, Netze). „S. 38 und 45“ nicht verlinkt. „Motortriebkopf voraus = CS3 vorwärts“ fehlt in der Tabelle | G.1-1 und G.2-7 umformulieren („sobald nachgewiesen …“); Links ergänzen; Gleichsetzung „vorwärts = Motortriebkopf voraus“ in die Tabellenüberschrift | T |

---

## 4. Anforderungsmatrix

Legende:

- **Dok.** = in REV9 als Ziel und Handgriff dokumentiert
- **Beleg** = technisch belegt, mit Evidenzkategorie
- **Test** = praktisch getestet
- **Status** = Gesamteinschätzung

| Nr. | Nutzerziel | Dok. | Beleg | Test | Status / Hauptlücke |
|---|---|---|---|---|---|
| 1 | Über mfx automatisch als **ein** Zug | ja (C2–C7, 54, F) | teilweise: ESU-Sync nur ESU/ESU (K1); mSD3 + LokPilot 5 M4 als Slave (K4, Stummiforum 26.02.2023); CV191–195 (K3) | nein | **offen:** Masterkennung, Umrechnung und Aktivierung unbekannt (F.3/F.5); C7 ohne Weg (R-11) |
| 2 | Kein zweiter automatisch angemeldeter Zug | ja (C3, 54) | ESU (K1): konfigurierter Slave meldet sich nicht mehr selbst an | nein | **offen:** Vorab-Anmeldung in F.4 (R-05); mfx-Konfig über gemeinsame SID ungeklärt (R-06) |
| 3 | Ohne Traktion | ja | folgt aus 1 (K2) | nein | offen, hängt an 1 |
| 4 | Märklin-Sound im Motortriebkopf | ja (9b, 46, 52) | 60977-Anleitung (K1); LS1/LS2 nur am Audioausgang | nein | offen: Lautsprecher-Passung, Adapter (L1–L5) |
| 5 | Weiß/rot an beiden Köpfen, auch im Stand | ja (12a, 17a T3/T4, G.2-Tabelle) | Mapping-Logik schlüssig (K2); Werksmapping beider Decoder passt (K1) | nein | offen: Sync (1), F-Tasten-Übersprechen (R-07), G0-Mapping nicht protokolliert (R-16) |
| 6 | LoDi-Front-LEDs | ja (10, 11, 11a) | Rechenweg korrekt (K2); LoDi: Frontmodule ohne Vorwiderstand (Aussage des Dokuments, auf den LoDi-Seiten nicht wiedergefunden) | nein | **offen:** LED-Daten LoDi 514 (Uf, If, Topologie) fehlen, daher keine R-Werte |
| 7 | Innenlicht ohne konstruktive Unterbrechung | ja (16a, 17a) | RT (Gleis) + AUX richtungsunabhängig (K2); LoDi: Aux 4 = Wagenbeleuchtung (K1) | nein | Konstruktion schlüssig; offen: Last (R-15), Kontaktflackern, Kreuzung (R-21) |
| 8 | Originale Märklin-Kupplungen | ja (14, 39) | nur Teilekandidaten aus 33701-Ersatzteilblatt (K1, andere Baureihe) | nein | **offen:** Passung am 2976 |
| 9 | Keine zusätzliche durchgehende Steuerleitung | ja (0, 13, 14) | Zweipoliger LoDi-Kupplungsweg, Adresszuordnung übers Gleissignal (K1/K2) | nein | erfüllt im Konzept; setzt Anlagenbedingung R-01 voraus |

**Querbedingung:** Nutzerziel 9 (RT durchverbunden) ist nur unter der Anlagenbedingung aus R-01 zulässig. Gibt es zugbeeinflussende Signale, ist nach LoDi die ICE-M-S-Variante nötig.

---

## 5. Ablaufprüfung der entscheidenden Übergänge

| Übergang | Was wirksam ist | Was fehlt oder bricht |
|---|---|---|
| **Vorabtest → Montage** | G0-Sperren auf S. 1, 4, 11, 20 (Schritt 22), 30 (R1); C mit Abbruchkasten; getrennte Prüfaufnahmen | C7 ohne gangbaren Weg (R-11); Gate-Reihenfolge G1/G2 und „Foto 2 vor G0“ widersprüchlich (R-12); Selbstanmeldung des 59649 in F.4 unerwähnt (R-05); Prüfaufnahme mit oder ohne Motor unklar (R-09) |
| **Montage → Messung** | Motor: 5a/6/6a/6b vorbildlich (4 Hilfsleitungen, Klemmen bleiben fest, Vor-/Nachproben, Rotor- und Drehgestelllagen, Kondensatorverfolgung). Kupplungen: 14a/14b/14e mit positiven Kontrollen | Keine gleichwertige Messkarte für U+/LED/AUX/Trägerlitzen (R-02); motorloser Kopf ohne Altzustand und Handgriffe (R-03); Bezeichner-Mehrdeutigkeit gefährdet W1 (R-20) |
| **Messung → Programmierung** | Kap. 16 hinter G0; 60971 nur USB, nur 60977; CV51 mit Altwert, Rechnung, Rücklesen; F.4 „nur lesen“; CV8/CV7-Warnungen korrekt | LV/LR-Mapping in G0 nicht protokolliert (R-16); Index-CVs (R-08); Firmware/SID nicht lesbar (R-10); mfx-Konfiguration über gemeinsame SID (R-06) |
| **Programmierung → Einsetzen** | 9c/12b: Index 11, Buchse oben, Seitenkontrolle, „nicht mit Druck korrigieren“ | Mögliche Kappe auf der Stiftleiste verhindert die Indexkontrolle (R-23); Schritt 52 ohne STOP beim Einsetzen (R-14) |
| **Einsetzen → Erststrom** | Stufen: Motorkopf allein → beide Köpfe ungekoppelt → Wagen einzeln; 60974 abgesteckt; eine Quelle; Automatik aus | Messkarte vor Erststrom fehlt (R-02); Dummy ohne Programmiergleis-Vorprüfung (R-14); Kap. E als Freigabezirkel (R-13); SW–RT nicht nachgewiesen (R-24) |
| **Erststrom → Last/Fahrt** | 17a T1–T8 mit klaren Bestehenskriterien; Standtest vor Fahrtest | Fahrt und Innenlicht-Volllast vor Kap. 18 (R-15); keine F-Tasten-Prüfung am Slave (R-07); keine Wiederholpflicht nach Umreihen (R-21) |
| **→ Gehäuseabschluss** | Schritt 60 / Kap. 24: passive Prüfung ohne Decoder im geschlossenen Gehäuse, mit Kontaktkontrollen; Freiraum mit Decoder ausdrücklich gefordert | Keine Methode für den Freiraum; Neulötungen ungeprüft; zweites Schließen unkontrolliert (R-19) |

**Positive Kontaktkontrollen, die ein OL absichern:** vorhanden und wirksam in 2 (Null-/Offenprobe), 6a (Zeilen 1/2/5/6), 14a (K1/K2), 14b (W1), 14d (1/2/5), 14e (B-P1/B-P2) und 24 (Nr. 4). **Es fehlen** sie für LED-, Träger- und AUX-Netze (R-02).

---

## 6. Separates Votum zur Schnellanleitung (S. 68/69)

**Votum:** In der jetzigen Form **nicht freigabefähig**. Als Navigationsblatt ist sie gut aufgebaut:

- alle 22 Sprungziele korrekt;
- G0 ausdrücklich als offen markiert;
- Fußzeile „Freigaben der Vollfassung bleiben verbindlich“;
- Artikelnummern und Anschlussnamen identisch mit der Vollfassung.

**Durch die Kürzung sind aber neue Gefährdungen entstanden:**

- **G.1-5 (R-04, P1):** wirkt wie eine vollständige Anschlussliste, ohne Isolation der freien Trägerlitzen und ohne B/GR bzw. 0/GL.
- **G.1-6 (R-26):** kehrt die Prüfreihenfolge um.
- **G.2-8 und G.2-11 (R-27, R-28):** Handgriffe unmittelbar vor dem Stecken bzw. Schließen fehlen.

**Offene Nachweise:** Keiner wird ausdrücklich als erledigt dargestellt. Nur G.2-7 („bestätigte M4-Synchronisation … erhalten“) ist missverständlich (R-47).

**Missbrauchsrisiko:** Die Kurzfassung taugt derzeit nicht als alleinige Anschlussfreigabe und könnte dafür gehalten werden.

**Nach Korrektur von R-04 und R-26 bis R-28** und mit folgendem Zusatz an jedem Schritt ist sie als Begleitblatt vertretbar:

> „Nur zusammen mit der verlinkten Karte gültig; dieses Kästchen ist keine Anschlussfreigabe.“

| G-Schritt | Vollfassung | Bewertung |
|---|---|---|
| 1 | A–C, F.3–F.6, F.10 | verkürzt, unkritisch (Kasten fängt ab); R-47 |
| 2 | 4, 5, 5a, 21–23 | verkürzt, unkritisch |
| 3 | 5a-D3/D4, 6–7 | verkürzt, unkritisch („Hilfsleitungen entfernen“ fehlt, steht in 6b) |
| 4 | 8–9c, 10, 11a | verkürzt, unkritisch (R3/R6, K1, Pin 12, PANTO nicht genannt) |
| 5 | 12–12c | **verkürzt, kritisch** (R-04) |
| 6 | 13–14e | **verkürzt, kritisch** (R-26) |
| 7 | 16–16b, 12a | verkürzt, unkritisch (R-47) |
| 8 | 9c, 51–53 | **verkürzt, kritisch** (R-27) |
| 9 | 12b, 12c, 54–55 | **verkürzt, kritisch** (E1-Bedingung und 16c fehlen; R-04) |
| 10 | 56, 17a | verkürzt, unkritisch; übernimmt R-15 |
| 11 | 18, 24, E | **verkürzt, kritisch** (R-28) |

---

## 7. Widerlegte oder nicht bestätigte Verdachtsbefunde

| ID | Verdacht | Ergebnis | Beleg |
|---|---|---|---|
| W-01 | Wagenpad „O“ ist Märklin-Masse „0“; RT→O und Radmasse→B wären vertauscht (mein eigener Anfangsverdacht, Glyphe auf S. 31 wirkt ziffernartig) | **widerlegt** – O und B **nicht** tauschen | LoDi WiB ICE-M (K1), drei getrennte Abrufe übereinstimmend, zusätzlich unabhängig von dir bzw. deiner zweiten Prüfinstanz bestätigt. Ursprüngliche Verdrahtung: L = Gelb (Licht schalten), O = Braun (Masse, Radschleifer), B = Rot (Mittelleiter). **Mit LoDi-Motor WiB ICE-M(-S):** L = Gelb, **O = Rot (Mittelleiter)**, **B = Braun (Masse/Radschleifer, kann entfallen)**. LoDi: weiße Platinen ab Mai 2025 – „Die Anschlüsse bleiben unverändert“. Maßgeblich ist die dokumentierte Betriebsvariante, nicht die Zeichenform. S. 31/35/68 sind korrekt. Redaktionelle Empfehlung (keine Verdrahtungsänderung): auf S. 35 beide LoDi-Fälle als Zweispalten-Tabelle direkt nebeneinander zeigen, mit Quellenlink |
| W-02 | CV51 Bit 4 invertiert (P0-Kandidat) | widerlegt | Märklin 60977 (K1): Bit 4 = 1 Logik, = 0 verstärkt, Vorgabe 0 |
| W-03 | „CV7 = 77 startet Einmessfahrt“ unbelegt | widerlegt | Märklin 60977 (K1): Einmessfahrt über 77, Lok beschleunigt auf Höchstgeschwindigkeit |
| W-04 | CV52 = 3 falsch | widerlegt | Märklin (K1): CV52 = 3 = „Hochleistungsantrieb C90“ (Zuordnung zum 60941 siehe R-39) |
| W-05 | Grenzwerte S. 44 erfunden | widerlegt | Märklin (K1): 1,1 A / 250 mA / 300 mA / 1,6 A |
| W-06 | Werksbelegung F1/F4/F6 falsch | widerlegt | Märklin (K1) |
| W-07 | 60974 nicht über SUSI bzw. Firmware erfunden | widerlegt | Märklin 60974 (K1): SUSI; mSD3 ≥ 3.2.0.1; nicht mehrere hintereinander |
| W-08 | SUSI/21MTC-Pintabelle S. 38 falsch | widerlegt | RCN-600 (27.07.2026) classicSUSI 1 GND / 2 Daten / 3 Takt / 4 Plus; RCN-121 20/6/5/16 (K2) |
| W-09 | CV191–195 und Bytefolge erfunden | widerlegt als K3 | JMRI Commit 32eca6c: CV191 M4MfgId, CV192:4 M4SerNo, little-endian, eingeführt 10.04.2020. Aktivierungswirkung weiterhin offen, wie im Dokument angegeben |
| W-10 | Rechenfehler | widerlegt | S. 25 (7,0 / 7,33 kΩ; 2,83 / 2,96 mA; 0,060 / 0,065 W), S. 26 (3,41; 9,55 / 2,80 mA), S. 41 (24 → 8), S. 56 (0x12345678 → 120/86/52/18) nachgerechnet |
| W-11 | Rot/Weiß-Zuordnung hinten vertauscht | widerlegt | Richtungslogik S. 4/27/28/39/64/69 widerspruchsfrei (K2) |
| W-12 | 21MTC-Stecklage falsch | nicht bestätigt | Buchse oben, Stifte durch die Decoderplatine: passt zu Märklin-Beilage S. 6 (im PDF S. 29) und RCN-121 |
| W-13 | Fehlerhafte Sprungziele | widerlegt | alle 89 internen Links geprüft (Linktext gegen Zielseite) |
| W-14 | Versionsangaben erfunden | widerlegt | CS3 2.6.2 (18.08.2026), LokProgrammer-SW 5.2.18, NMRA 131 = Trix / 151 = ESU bestätigt |
| W-15 | Forenbeleg existiert nicht bzw. ist falsch eingeordnet | widerlegt | Stummiforum MTB-Ontour, Beitrag 4, 26.02.2023: mSD3 + LokPilot V5 M4 als Slave, per ESU-Programmer eingerichtet (K4, ohne Werte) – im Dokument korrekt als Machbarkeitshinweis eingestuft |
| W-16 | LoDi-Jumperlogik falsch | widerlegt | LoDi (K1): ab V1.50 SJ1 → AUX4, SJ2 → AUX1, „Es darf immer nur ein Jumper gesetzt sein“; R4/R5 nur für Glühlampen brücken; „3 Kondensatoren … zwei entfernen“ |
| W-17 | Helle Fläche unter dem 60977 (S. 18) ist blankes Kupfer | eher widerlegt | Vergrößerung: Bestückungsdruck auf Lötstopplack (Konsil 1) |
| W-18 | Schnellanleitung stellt G0 als erledigt dar | widerlegt | G.1-Kasten „G0 ist noch offen“; nur Wortlaut G.2-7 missverständlich (R-47) |

---

## 8. Korrekturreihenfolge mit Ersatztexten

Die Ersatztexte stehen vollständig bei den jeweiligen Befunden in Abschnitt 3.

| Welle | Befunde | Inhalt | Art |
|---|---|---|---|
| **1 – Schutz vor Erststrom** | R-02, R-03, R-04, R-14 | Neue Messkarte 16c; neues Kap. 4b und Schritt 34a (Dummy); G.1-5/G.2-9 ersetzen; Schritt 52 mit STOP; neuer Schritt 53a (Dummy am Programmiergleis) | T, danach N |
| **2 – Anlagenbedingung** | R-01 | Neuer Schritt 19.0 „Anlage erfassen“; ICE-M-S-Bedingung nach LoDi; G.2 Regel 1 verlinken | T + Bestandsaufnahme |
| **3 – Last- und Gehäusereihenfolge** | R-15, R-19, R-21 | 17a nur Stand → Kap. 18 → Fahrt; AUX-Summenregel; Kap. 24 Nr. 6/7 neu; Wiederholpflicht nach Umreihen | T |
| **4 – Programmierung und Synchronisation** | R-05, R-06, R-07, R-08, R-09, R-10, R-11, R-16, R-17, R-25 | F.4-Warnung Selbstanmeldung; mfx-Konfig-Verbot bis Nachweis; T9 F-Tasten; Index-CV-Karte; Prüfaufnahme mit Motor; C7-Methode mit Kriterien; Mapping-Tabelle in C4/C8; Trennregel für Nachprogrammierung; Adress-/Protokollabgleich | T + N |
| **5 – Freigabelogik** | R-12, R-13, R-20 | Gate-Tabelle neu; E1/E2 teilen; eindeutige Bezeichner | T |
| **6 – Bauteilnachweise** | R-22, R-23, R-24 | LoDi-511-Netzmessung, Kappe/Index, SW–RT, Variante | N |
| **7 – Schnellanleitung Rest** | R-26, R-27, R-28, R-47 | Reihenfolge G.1-6; Handgriffe G.2-8/11; Zusatz „keine Anschlussfreigabe“ je Schritt | T |
| **8 – Redaktion** | R-29 bis R-46 | Nummern, Widersprüche, Quellen, Layout, Metatexte | T |

**Empfehlung:** Die Wellen 1 und 2 zuerst als REV10-Teilrevision umsetzen und nur diese Seiten erneut prüfen lassen. An der Hardware darf erst nach bestandenem G0 gearbeitet werden – und G0 hängt an R-11.

---

## 9. Was zur Schließung wirklich noch fehlt

**Fotos (scharf, beide Seiten, mit Maßstab)**

1. Motorloser 2976-Kopf geöffnet: Schleifer vorhanden? Alle Litzen, Kupplungskontakte, Altplatine, Lampenhalter, Stützen (R-03, 12c).
2. Rote LoDi 511 Rückseite mit Revision, SJ1/SJ2 als Makro mit Streiflicht, Stiftleiste von oben ohne Kappe mit Indexlücke (R-22, R-23, R-24).
3. Beide LoDi-514-Einsätze Vorder- und Rückseite, Märklin-Träger beide Seiten, Kupplungskontakte Kopf und Wagen (R-03, 10/11, 14).

**Messwerte (spannungslos, Decoder draußen)**

4. Leere LoDi 511: SW–RT, MASSE–21 bzw. –20, VCC–16, GE–4/15 (R-22, R-24).
5. Messkarte 16c je Kopf, offen und geschlossen (R-02).
6. 14a/14b-Ausgangswerte je Wagen; 6a-Protokoll (bereits geplant).

**Herstellerantworten (schriftlich)**

7. **ESU zum 59649:**
   - Ist die Adress-Synchronisation mit einem **Märklin-mfx-Master (60977)** unterstützt?
   - Aktivierungsregister und -wert, Mindestfirmware.
   - Wie wird die Märklin-UID ins Seriennummernfeld übertragen (Format, Bytefolge)?
   - Unterdrückt der Slave mfx-Rückmeldungen und -Schreibbefehle (R-06)?
8. **LoDi:**
   - Variante der Platine (ICE-M ohne Umschaltung, SW–RT fest?).
   - GE-Pfad bei V1.49.
   - Elektrische Daten LoDi 514 (Uf, If, Zweigtopologie).
   - Stromaufnahme je Wagenplatine V4.3.
   - Kappe auf der Stiftleiste.
9. **Märklin-Service:**
   - 60941 ↔ Motortyp C90 bestätigen.
   - Verhalten „CV hinzufügen“ im CS3-CV-Editor (Vorgabewert, Auto-Schreiben).
10. **Zweite mfx-fähige Testzentrale** für C7 (Leihgerät oder Fachbetrieb) – sonst bleibt G0 offen (R-11).
11. **Anlagenliste:** Mittelleiter-Trennstellen, signalabhängige Abschnitte, Booster (R-01).

**Hinweis:** Die Wagenzahl bestimmt die AUX4-Last (R-15). Falls dein 2976 dieselbe Zusammenstellung wie in deinem eigenen Platinenprojekt hat (3 Mittelwagen + Bordrestaurant), sind das 4 Wagenplatinen an einem Ausgang.

---

## 10. Quellen (in dieser Prüfung abgerufen oder geprüft)

**Hersteller (K1)**

- LoDi: [LoDi-Motor WiB ICE-M(-S)](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/) – Pads, Jumper, Funktionsliste, ICE-M-S-Bedingung
- LoDi: [LoDi-WiB ICE-M](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-wib-ice-m/) – L/O/B-Belegung Standard und Motorplatinenbetrieb, C1/C2
- ESU: [Master/Slave Adress-Synchronisation](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/)
- ESU: [LokPilot 5](https://www.esu.eu/produkte/lokpilot/lokpilot-5/) · [LokPilot-5-Anleitung](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e) · [CV-Änderungen anzeigen](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/) · [LokProgrammer-Software](https://www.esu.eu/download/software/lokprogrammer/)
- Märklin: [Nachrüstdecoder 60975/60976/60977](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf) · [CV-Tabelle mSD3](https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf) · [60974](https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf) · [60941/60943](https://static.maerklin.de/damcontent/e3/bb/e3bb202fe80385cc96835d783af5e1821670919973.pdf) · [60941 Produktseite](https://www.maerklin.de/de/produkte/details/article/60941) · [CS3-Kurzanleitung](https://static.maerklin.de/damcontent/c1/ce/c1ce554ad6ad195c04e32ba1b4dd64511764068661.pdf) · [CS3-Changelog 2.6.0](https://www.maerklin.de/fileadmin/media/service/cs3/Maerklin_CS3_v2.6.0_changelog.pdf) · [CV-Editor-Hilfe](https://www.maerklin.de/fileadmin/media/clubs/downloads/Loks_CV_Editor.pdf) · [CAN-Protokoll 2.0](https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf) · [CS3-Updates (NL)](https://www.marklin.nl/service/downloads/cs3-updates)

**Normen (K2)**

- [RCN-121 21MTC](https://normen.railcommunity.de/RCN-121.pdf) · [RCN-600 SUSI](https://normen.railcommunity.de/RCN-600.pdf) · [NMRA S-9.2.2 Appendix A](https://www.nmra.org/sites/default/files/standards/sandrp/DCC/S/appendix_a_s-9_2_2.pdf)

**Implementierung (K3)**

- [JMRI v5standardCVs.xml](https://github.com/JMRI/JMRI/blob/32eca6cddc18a55f2efdfdbc970cca96b7511827/xml/decoders/esu/v5standardCVs.xml#L994) · [JMRI Commit 7d14c27](https://github.com/JMRI/JMRI/commit/7d14c2747c788c1cf49eb599ddea0fd15d4b58fa)

**Erfahrung/Sekundär (K4)**

- [Stummiforum MTB-Ontour (mSD3 + LokPilot 5 M4)](https://www.stummiforum.de/t212683f5-Umbau-ICE-Maerklin-auf-mSD-DCC.html) · [Stummiforum „ERLEDIGT“](https://www.stummiforum.de/t242098f5-ERLEDIGT-ESU-LokPilot-RailComPlus-Master-Decoder-Synchronisation-geht-nicht.html) · [Märklin-Sammler-Infos 60941](http://maerklin-sammler-infos.de/maerklin/zubehoer/60941/60941_mz.htm) · [Krauß, Schienenformat mfx](https://www.skrauss.de/modellbahn/Schienenformat.pdf)

**Nicht abrufbar**

- [mDecoderTool3-Anleitung](https://streaming.maerklin.de/public-media/mdt3/pdfs/D_mDecoderTool3_A5_v360.pdf) (robots.txt)
- [Stummiforum nakott](https://www.stummiforum.de/t147582f7-Wo-finde-ich-die-UID-eines-Lokdecoders.html) (Timeout)
- LoDi-514-Datenblatt (nicht gefunden)

Umgehungswege (curl, Archive, Mirrors) wurden bewusst nicht genutzt.
