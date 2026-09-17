# REV12-Bericht: Gegenprüfung Geräteweg, Programmierung und ausgewählte Redaktion

Stand 12.09.2026. Keine Hardwaremessung. Gegenstand ist die tatsächliche REV12 mit SHA-256 `95af61083373a0755fde8ebd5ae70233952f6283b3db652b03e71c26582bcc8e`; der vorgelegte Bericht hat SHA-256 `d4f913f4c6484c94f219e23c4c610e0d9d1c08679cb93b20dc6a570e9f79a380`.

## Maßgebliche Gegenbefunde

**W-07 ist nur als fehlende Schalterangabe bestätigt.** In der originalen [ESU-LokPilot-5-Anleitung, S. 19, Abb. 3](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e) wird der Artikel 59649 ausdrücklich genannt. Pins 9 und 10 stehen beide auf „–“. Der im Bericht vorausgesetzte verstärkte Ausgang an diesen Pins ist für diesen Decoder daher widerlegt. Die allgemeine Möglichkeit der Schnittstellennorm beweist keine konkrete ESU-Belegung. Die Originalseite wurde zusätzlich als Bild kontrolliert und unter `evidenz/ESU_LP5_S19.png` dokumentiert.

**Der Ersatzvorschlag „ohne Lautsprecherlast (100 Ω)“ wäre selbst falsch.** [Märklin 60970, S. 5](https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf) nennt 8 Ω und 100 Ω als zwei Impedanzen und empfiehlt bei ungeklärter Einstellung 100 Ω. Das ist keine offene Verbindung. Die korrigierte Karte nennt 100 Ω als reale Stellung, keine externe Last und die tatsächlich unbelegten ESU-Pins. Eine spätere andere Decoderrevision muss anhand ihrer eigenen Anleitung passen.

**W-11 ist widerlegt.** Im exakt festgelegten JMRI-Stand `31e482094d472e481c1fb54f9901093c2efbfcec` gilt die vollständige Einbindungskette:

1. [ESU_LokPilot5.xml, Z. 186 und 246](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/ESU_LokPilot5.xml#L246): Modell LokPilot 5 MKL enthalten; gemeinsame V5-Register eingebunden.
2. [v5standardCVs.xml, Z. 18](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v5standardCVs.xml#L18): bindet `v4decoderInfoCVs.xml` ein.
3. [v4decoderInfoCVs.xml, Z. 60–72](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml#L60): Firmware-Build in `0.255.285:2`, Minor in `0.255.287`, Major in `0.255.288`, jeweils lesend.

Der Dateiname V4 ist kein Ausschluss von V5. Alle drei Dateien wurden live abgerufen und lokal gesichert. Das ist ein konkreter Softwarebeleg der Kategorie K3, weiterhin kein eigener Gerätetest und keine ESU-Zusage zur herstellerübergreifenden Synchronisation. Optionalen Diagnoseweg erhalten, Evidenzkette präzisieren.

## Abgleich aller zugeteilten Befunde

| ID | Urteil | Konkrete Korrektur oder Grenze |
|---|---|---|
| W-07 | Teilweise bestätigt; Schadensszenario für 59649 widerlegt; Ersatz fehlerhaft | Schalter d auf 100 Ω festlegen, reale Last erklären, Pins 9/10 mit ESU-Abbildung belegen. Kein erfundener Freischalter. In Kartenmodul umgesetzt. |
| W-08 | Bestätigt, sinnvolle explizite Sperre | „Prog.“ und „Vorlagenwerte schreiben“ ausdrücklich unbenutzt lassen. Q24 beschreibt die Gesamtliste und das Sofortschreiben; vorhandene lokale Original-PDF/Textfassung geprüft, heutiger Web-Abruf war 502. In S. 11 umgesetzt. |
| W-09 | Dokumentationsbedarf bestätigt; pauschales Kurzschlussszenario überzeichnet | Je 60970 genau ein Decoder erfüllt die Einzelgerätebegrenzung. Zwei getrennte Eingänge an derselben Quelle sind eine eigene Schaltungsfestlegung. Bloße Umpolung eines ausschließlich über seinen Eingang verbundenen zweiten Geräts beweist noch keinen direkten Quellenkurzschluss. Den passiven B/0-Verteiler vor Anschluss an Elektronik nach S. 4 prüfen. CS3 B → 60970 rt, 0 → bn laut Originalbild S. 29. Nicht die bestückten Prüfstände pauschal mit einem Ω-Grenzwert freigeben. In S. 7 umgesetzt. |
| W-11 | Widerlegt | Vollständige JMRI-Einbindungskette, siehe oben. Diagnose optional erhalten, K3 deutlich nennen. |
| W-12 | Bestätigte Evidenzgrenze | mfxuid → ESU-Seriennummer bei diesem Herstellerpaar als zu prüfende Annahme kennzeichnen. Frisches Rücklesen beweist Bytes, nicht Semantik oder Funktion. Paarprüfung prüft tatsächliche Reaktion im eigenen Aufbau; keine universelle Interoperabilitätszusage. S. 9 präzisiert. |
| W-17 | Größtenteils bereits abgedeckt, Wartungsergänzung sinnvoll | REV12 S. 6 enthält bereits Einzelarbeiten mit einem Tester und Software-/Dateivorbereitung ohne Tester. Fehlende zweite Aufnahme ist kein Grund, das zentrale Paarprüfungstor aufzuweichen. Wiederholten Leihbedarf für Wartung und Paarprüfung ergänzen. S. 6 angepasst. |
| W-18 | Sinnvolle Präzisierung | Die zwei Gegenkopf-Felder Motor und Lautsprecher dürfen „entfällt“ sein. Hintere LEDs können ausdrücklich „getrennt/isoliert“ sein, dies ist kein erledigter Lichtnachweis. Alle anderen für diesen Kopf einschlägigen Pflichtzeilen brauchen Nachweis. Root integriert. |
| W-19 | Sinnvolle Präzisierung | Vor Bit-0-Umkehr den realen Anschluss gegen S. 21 prüfen. Eine abweichende Litzenzuordnung zuerst berichtigen und betroffene Motor-/Isolationsprüfungen wiederholen. CV51 Bit 0 ist technisch zulässig, Quelle Q10 ergänzen. Root integriert. |
| W-20 | Bestätigtes Reihenfolgeproblem | S. 19 zunächst als Lesekarte/Messpunktplanung markieren; reale Versorgung erst beim Einzeltest vorn S. 35 oder hinterem gemeinsamen Lichttest S. 36. „Einzeltest hinten“ allein darf keine F0-Reaktion ohne Master fordern. Root/Elektro integriert. |
| W-21 | Sinnvolle Präzisierung | Gemeldete Updateanforderung ist unabhängig von der optionalen Diagnose vor Synchronisationsänderung zu klären. In S. 11 VORHER umgesetzt. Ein unbekannter Firmwarestand allein wird nicht pauschal zur Sperre. |
| W-22 | Sinnvolle Präzisierung | Nach tatsächlicher neuer Masteranmeldung/SID auch an der eigenen CS3 Paarprüfung wiederholen. Reset/Löschen nicht eigens zum Erzwingen einer SID-Änderung anweisen; neue SID entsteht nicht zwingend bei jedem einzelnen dieser Ereignisse. In S. 12 umgesetzt. |
| W-25 | Redaktionell sinnvoll | S. 12 „CS3-Paarprüfung“ nennen, übrige G0-Verweise einheitlich ersetzen. Titel im Modul, globale Ersetzung beim Root. |
| W-26 | Redaktionell sinnvoll | Prüfaufnahmen mit Decoderartikeln benennen, Index-/Firmwarelisten ausschreiben. Andere A/B-Namen nur ändern, wenn es die konkrete Karte erleichtert. In S. 7/11 umgesetzt. |
| W-27 | Bestätigt | Feste Buchse, Datenquellenschalter e und c-Taster getrennt aufführen. c nicht betätigen. Soundfunktion aus ist Bedienzustand, d bleibt konkrete Impedanz. In S. 7 umgesetzt. |
| W-28 | Gemischt; Q5-Unterbefund widerlegt | Q10 für Bit 0, Q24 für „Prog.“ und unmittelbares Schreiben, vollständiges CS3-Handbuch für GFP3; Q30 auf Motor-Eignungskarte ergänzen. Q5 ist die richtige Sammelseite: unten Abschnitt „LoDi-WiB ICE-M Front 2 Stück“ mit „Ohne Vorwiderstände“, kein falsches Ziel. Quellentitel wird präzisiert. S. 2 darf auf Beschaffung S. 6 und Anschluss S. 7 getrennt verweisen. |
| W-29 | Sinnvoll; behauptete feste 0,5-W-Bauform unbelegt | Widerstandsgröße, Einbauort, Leitungsisolation und Wärmeabstand vor Montage trocken prüfen. Die benötigte Nennleistung wird aus den tatsächlichen Werten ermittelt; Faktor 2 allein erzwingt nicht allgemein 0,5 W. Root integriert S. 23. |
| W-30 | Physikalische Kernaussage richtig, „unterdimensioniert“ missverständlich | Annahme U_LED,min = 0 führt bei sonst gleicher Auslegung zu größerem Widerstand und daher geringerem tatsächlichem Strom. Helligkeitsunterschied ist mögliche Folge der konservativen Auslegung. Helleres Ende dimmen, nie Widerstand allein zum Helligkeitsangleich unbegründet verkleinern. Root/Elektro integriert. |

## Unzulässige Übernahme aus dem Bericht vermeiden

- Keine Bestandsangabe aus dem Bericht als neue direkte Nutzeräußerung behandeln.
- Nicht behaupten, 100 Ω sei keine Last oder 59649 belege seine Pins 9/10 als verstärkte Ausgänge.
- Nicht aus dem Präfix einer gemeinsam verwendeten Quelldatei auf fehlende V5-Einbindung schließen.
- Nicht die „Mittelwerte plus 40 % Reserve“-These, erfundene 25 V/5 mA oder feste 0,5-W-Widerstände als freigegebene Dimensionierung übernehmen.
- Nicht das reale Paarprüfungstor aus reiner Beschaffungsbequemlichkeit überspringen.

## Implementierung und Prüfung

`programming_changes.py` verändert ausschließlich die Karten 6–12 und liefert Quellenkorrekturen separat. Das Originalfoto auf S. 7 bleibt unverändert. Die sieben Karten wurden mit dem bestehenden Layoutmaß gemessen; Mindestabstand zum erlaubten Inhaltsende nach erster Korrektur 5,4 pt auf S. 12, übrige mindestens 34,7 pt. Endgültige Seitenzählung und Sichtprüfung erfolgen im Gesamtbau durch den Hauptagenten.
