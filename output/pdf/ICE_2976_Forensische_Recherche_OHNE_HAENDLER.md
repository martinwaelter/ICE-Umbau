# ICE 2976: Umbau ohne Händler

**Ein technisch begründeter Eigenweg ist vorhanden. Der nächste sinnvolle Schritt ist ein begrenzter CS3-/Software-Nachweis; ein eigener LokProgrammer ist noch keine notwendige Anschaffung.** Die Recherche schließt wesentliche Dokumentationslücken, ersetzt aber weder den originalen ESU-Aktivierungsexport noch den Test der vorhandenen Decoder.

Gegenstand sind REV10, das vorliegende Prüf- und Kürzungsurteil sowie der ICE aus Märklin 2976 mit 60977 mSD3 im Motortriebkopf und 59649 LokPilot 5 M4 MKL im Gegenkopf. Ziel bleiben ein automatisch nutzbarer mfx-Zugeintrag, Märklin-Sound, richtungsabhängiges Rot/Weiß im Stand, getrennt schaltbares Innenlicht und Betrieb ohne Zentralen-Traktion. Händlerleistungen stehen nicht zur Verfügung. REV10 ist die unveränderte Vergleichsbasis.[^1]

### Zentrale Ergebnisse

| Frage | Belastbarer Stand | Konsequenz |
|---|---|---|
| Herstellerkennung des Masters | 60977-Anleitung: CV8 = 131, nur lesen. | Die für 60977 dokumentierte Herstellerkennung ist geklärt. |
| Identität aus der CS3 | Originalcode und CS3-Testdaten unterscheiden mfxuid und Betriebsadresse. | Einen vollständigen eigenen Rohdatensatz sichern. |
| Synchronisationsregister | JMRI: CV191 und CV192-195; MKL eingebunden, Bytefolge geklärt. | Den Original-ESU-Schalter gezielt gegenprüfen. |
| Händlerpflicht | Keine allgemeine externe Abnahme in den geprüften Herstelleranleitungen gefunden. | Konkrete Kriterien ersetzen die Personenvorgabe. |
| Motorloses DCC-Rücklesen | Für 59649 in diesem Aufbau nicht nachgewiesen. | Wartung auf quittierender Einzelaufnahme vorsehen. |

Die technische Machbarkeit des Familien-Mischbetriebs wird durch einen Originalbericht gestützt. Er nennt jedoch keine exakten Artikel, Firmwarestände, CS3-Version oder neue SID. ESUs eigenes Beispiel verwendet zwei LokSound 5. Daraus folgt ein aussichtsreicher Versuch, keine bereits bestandene Abnahme für 60977/59649.[^2][^3]

**Bewertung:** REV10 schützt viele kritische Handgriffe, vermischt jedoch offene Gerätedaten mit pauschalen Personen- und Ablaufpflichten. Der richtige Eingriff ist die Auflösung dieser Abhängigkeiten in konkrete Nachweise. Bloßes Kürzen oder Ersetzen von „Fachprüfer“ durch „selbst prüfen“ wäre unvollständig.

Der Bericht unterscheidet Herstellerbelege, originale Softwareimplementierungen, Protokollanalyse, Erfahrungsberichte und daraus abgeleitete Empfehlungen. Ein diagnostizierter Dokumentmangel ist kein gemessener Hardwaredefekt. Die nachstehenden Zahlen sind keine individuelle CV-Schreibkarte.

## 1. Masterkennung, UID und Betriebsadresse

Die passende Märklin-Anleitung nennt auf S. 19 für CV8 die Herstellerkennung **131**. Krauß beschreibt zusätzlich das separate mfx-Herstellerfeld mit 0x83 für Märklin/Trix und 0x97 für ESU. Die in REV10 als nicht abschließend geprüft bezeichnete Fundstelle auf S. 39 ist damit geklärt. Krauß bleibt eine originale Protokollanalyse; der 60977-Modellwert ist unabhängig durch Märklin abgesichert.[^4][^5]

| Größe | Bedeutung | Verwendung |
|---|---|---|
| Hersteller-ID 131 | Herstellerkennung Märklin/Trix; für 60977 dokumentiert | Kandidat für das ESU-Herstellerfeld; keine individuelle Seriennummer. |
| mfxuid | Dauerhafte 32-Bit-Identität des konkreten Decoders | Für den Masterverweis vollständig und unverändert sichern. |
| sid / address | Von der Zentrale zugewiesene Betriebsadresse | Vorher-/Nachher-Nachweis einer Adressneuvergabe. |
| uid im Zentralendatensatz | Zentraleninterne Lokkennung | Nicht allein wegen des Namens als Decoder-UID übernehmen. |

Märklins CAN-Protokoll trennt die vier Byte lange Decoder-UID von der zugewiesenen SID. Die CS2-Dateibeschreibung allein wäre noch kein CS3-Nachweis. Diese Lücke verkleinert TrainControl: Der festgelegte Originalcode verwendet /config/lokomotive.cs2; sein CS3-Testdatensatz enthält mfxuid, uid und sid getrennt.[^6][^7][^8]

Für JSON unterscheidet derselbe Code /app/api/loks vor CS3 2.6 und /app/api/locos ab 2.6. Die vollständige 2.6-Testdatei enthält 154 Lokobjekte, 112 davon mit mfxuid. Bei diesen 112 gilt uid = 0x4000 + address. Das belegt die unterschiedliche Feldbedeutung in diesem Testmaterial, keine universelle API-Garantie für jede CS3-Version.[^7][^9]

### Konkreter eigener Datennachweis

Zuerst die tatsächliche CS3-Version und den eindeutig zugeordneten 60977-Eintrag erfassen. Eine frische Sicherung oder eine erfolgreiche reine Leseantwort des passenden lokalen Pfads wird unverändert archiviert. Benötigt werden der gesamte betreffende Datensatz, Feldnamen, Zahlenformat und Herkunft. Eine Anmeldung, die vorher noch erfolgen muss, bleibt ein eigener sicherer Hardwarevorgang; der Dateizugriff meldet keinen Decoder an.

Die stärkste technische Arbeitshypothese lautet: **ESU-Zielseriennummer = vollständige rohe mfx-UID als vorzeichenloser 32-Bit-Wert.** Eine besondere Märklin-Umrechnung wurde nicht gefunden. Noch zu bestätigen sind die originale ESU-Abbildung und das Folgen des realen Slaves. Weder ein UID-Präfix abschneiden noch Bytes invertieren oder eine Artikelnummer einsetzen. Die individuelle Kennung lässt sich aus 60977 oder 131 nicht berechnen.

## 2. Register, Bytefolge und Aktivierung

JMRI bindet die gemeinsame V5-Registerdefinition und das Synchronisationspanel auch für LokPilot 5 MKL ein. Sieben relevante Dateien wurden zwischen dem REV10-Quellstand und dem aktuell festgelegten Stand verglichen; ihre jeweiligen SHA-256-Hashes sind identisch. Eine zwischenzeitliche Änderung dieser Dateien erklärt die bisherige Unsicherheit somit nicht.[^10][^11]

| Register | In JMRI definierte Bedeutung | Beweisgrenze |
|---|---|---|
| CV191 | M4MfgId, Herstellerkennung des Masterverweises; Default 0 | Der Default beweist keine Ein-/Ausschaltregel. |
| CV192-195 | M4SerNo, 32-Bit-Seriennummer des Masterverweises | Keine Seriennummer des Slaves selbst. |
| CV31/CV32 | Für diese fünf unindizierten Register nicht erforderlich | Andere tatsächlich exportierte Register können einen Index benötigen. |

Die Notation 192:4 wird im Parser zu 192, 193, 194, 195. Die Wertklasse legt die niedrigsten Bits in das erste Register. Die belegte JMRI-Zusammensetzung lautet:

**S = CV192 + 256 × CV193 + 65.536 × CV194 + 16.777.216 × CV195.**

Die Formel erklärt eine Implementierung. Sie bestätigt nicht, dass die Firmware des vorhandenen 59649 bereits die richtige Konfiguration enthält.[^13][^14]

Im JMRI-Panel stehen ausschließlich Herstellerkennung und Seriennummer. Ein separater Aktivierungsschalter fehlt. Das passt zur Hypothese „gesetzte Kennung aktiviert“, schließt aber eine in JMRI fehlende oder implizite weitere Bedingung nicht aus. Deshalb sind weder CV191 = 0 als gesichertes Ausschalten noch ein Nichtnullwert als vollständige Aktivierung freigegeben.[^12]

### Der entscheidende Offline-Versuch

Ein passendes originales LokProgrammer-5-Projekt wird ohne Hardwareverbindung geöffnet. Bei fester synthetischer Hersteller-/Seriennummer werden die Zustände **aus, an und wieder aus** verglichen. Zusätzlich werden bei gleicher Seriennummer die Herstellerwerte 151 und 131 verglichen. Eine nicht symmetrische Testseriennummer prüft die Bytefolge; Testwerte gehören ausschließlich in das Offlineprojekt.

Zu jeder Variante werden Projekttyp, Softwareversion, sichtbare Eingaben und vollständiger Export gesichert. Die Liste geänderter CVs muss vor dem Speichern kopiert werden, weil Speichern die Merkliste löscht. Falls Ausschalten die Kennung leert, ist das selbst ein Ergebnis; ein vermeintlicher Ein-Parameter-Vergleich wäre dann falsch.[^15]

**Erfolgskriterium:** Alle Registeränderungen, gegebenenfalls Indexgruppen und die Seriennummernabbildung sind reproduzierbar erklärt. Ein solcher Originalexport wurde in diesem Lauf nicht erzeugt; ein öffentlich zugänglicher gepaarter Export wurde im untersuchten Suchraum nicht gefunden.

## 3. CS3-Bedienung und Softwaregrenzen

Der CS3-Weg ist nicht deshalb unbelegt, weil gewöhnliche CVs unerreichbar wären. Die konkrete offene Frage ist die richtige Synchronisationskonfiguration. Märklins Changelog beschreibt die DCC-Bedienung ab 2.4.0 deutlich genauer als die ältere Hilfe von 2018. Beim Eintritt wird die Liste nicht mehr automatisch gelesen; das gezielte Anwählen einer ungelesenen CV löst Lesen aus. Eine Wertänderung wird unmittelbar geschrieben.[^17][^18]

### Konsequenzen für eine ausführbare Bedienkarte

Die tatsächliche Version/Build wird zuerst notiert. Bei der Einrichtung der Ansicht bleibt der Decoder abgetrennt. CV-Nummernfeld, Wertefeld, Lesen und Übertragen einer Vorlage werden anhand der passenden Oberfläche eindeutig zugeordnet. Die Registerliste wird vorbereitet, ohne Zielwerte vorzugeben. Erst danach beginnt ein reiner Lesetest am einzeln angeschlossenen Decoder in der bestätigten Aufnahme.

Eine fertig angezeigte Tabelle beweist keine frische Rücklesung. Das Changelog weist außerdem darauf hin, dass die CS3 nach Lesefehlern weitere Zeilen abarbeitet. Jede benötigte CV braucht deshalb einen eigenen nachvollziehbaren Leseerfolg. Der Vorlagen-Schreibknopf ist kein zusätzlicher Bestätigungsknopf für Einzelwerte; Märklin dokumentiert frühere versehentliche Rücksetzungen auf Vorlagenwerte ausdrücklich.[^17]

Eine externe Person muss die Oberfläche nicht pauschal „freigeben“. Nötig ist ein versionspassender, eindeutig beobachteter Bedienablauf. Unklare Bedienelemente dürfen vor der Decoderverbindung untersucht werden. Die aktuell vorhandene CS3 wurde in dieser Recherche nicht bedient; deshalb enthält der Bericht keine vorgetäuschten Bildschirmbelege.

### Kostenlose Software und eigener Programmer

ESU bietet LokProgrammer 5.2.18 vom 01.05.2026 für LokPilot 5 an und verlangt .NET 4.8. Die Windows-Mindestangaben auf derselben Seite widersprechen sich: allgemein 8.1+, beim konkreten Download Windows 7 SP1. Ein vorhandenes Windows 11 ist daher ein sinnvoller Prüfkandidat, seine praktische Eignung bleibt festzustellen. Eine native macOS-Ausgabe wird dort nicht angeboten.[^16]

Der kostenlose Projekt-/CV-Vergleich benötigt keinen 53451. Direkte ESU-Decoderkommunikation und insbesondere ein erforderliches Firmwareupdate sind dagegen konkrete Gründe für diese Hardware. Der 53451 ist kein vollständiger mSD3-Sound-/Firmwareprogrammer; Fremddecoder sind im ESU-Katalog auf den Einzel-CV-Modus begrenzt.[^15][^28]

PC-Softwareversion, Projektversion und ausgelesene Decoderfirmware sind drei verschiedene Nachweise. JMRI trennt eigene Seriennummer und Firmwareinformationen vom Masterverweis. Ein neues Offlineprojekt weist weder die tatsächliche Firmware noch den bisherigen Zustand des 59649 nach.[^29]

## 4. Prüfaufnahmen und motorloser Decoder

**21MTC allein ist kein Eignungsnachweis für eine Prüfaufnahme.** Die Ausgangsart von AUX3/AUX4, Motorlast, Lautsprecher, Schalterstellung und Datenquelle gehören zur dokumentierten Kombination. Beim 59649 MKL sind AUX3/AUX4 verstärkt. Die 53900-Anleitung ordnet AUX3-6 am 21MTC-Anschluss Logikpegel zu. Die tatsächliche Monitorschaltung für verstärkte Signale ist damit nicht nachgewiesen.[^19][^21]

| Prüfstand | Nachgewiesene Merkmale | Entscheidung |
|---|---|---|
| ESU 53900 | Anleitung: 8/100 Ohm, 11 × 15 mm, 0,5 W. Produktseite: 16/100 Ohm, 20 mm. | Reale Ausführung und Ausgangsmonitor klären; keine pauschale Unverträglichkeit behaupten. |
| Märklin 60970 | Umschalter Logik/verstärkt, Motor/Funktion, 8/100 Ohm und Zentrale/USB. | Besser dokumentierter Kandidat für eine eigene Anschlusskarte; keine automatische Paarabnahme. |

Der Widerspruch beim 53900 besteht zwischen zwei Herstellerquellen. Die relevanten Anschluss- und Schalterabbildungen wurden visuell geprüft. Beim 60977 stehen bis 1,6 W an 8 Ohm einer in der 53900-Anleitung genannten Lautsprecherbelastbarkeit von 0,5 W gegenüber. Eine passende Impedanz allein gibt volle Soundleistung nicht frei; ein begrenzender Prüfstandpfad ist hier nicht vermessen.[^4][^21][^22][^23]

Für nacheinander ausgeführte Programmierung genügt eine geeignete Einzelaufnahme. Der gleichzeitige Funktionstest benötigt zwei getrennte Decoderaufnahmen bzw. gleichwertig dokumentierte Aufbauten, getrennte Lasten und genau eine gemeinsame Gleisquelle. Ein bestimmter Doppel-Kauf wird dadurch nicht vorausgesetzt.

### Die vermeidbare ACK-Abhängigkeit

DCC-Service-Rückmeldung erfolgt über einen Stromimpuls. Die Norm beschreibt mindestens 60 mA zusätzlich für 5-7 ms. **Ein Schreibbefehl kann ausgeführt sein, obwohl die Quittierung nicht angekommen ist.** Fehlende Antwort erlaubt daher keine Blindwiederholungen. Auch ein Programmierausgang ist wegen möglicher Stromgrenzen bis 1 A kein universeller Schutz vor Verdrahtungsfehlern.[^20]

Der häufig zitierte 150-Ohm-Hinweis gilt in ESUs Handbuch für Fx micro 59110/59120, nicht für 59649. Eine solche Last darf nicht auf dessen Anschlussbild übertragen werden.[^19]

Der Eigenweg lässt sich stattdessen verbindlich so festlegen: **Jede DCC-Änderung erfolgt auf der dokumentiert quittierenden Einzelaufnahme.** Anschließend stromloser Wiedereinbau und erneute betroffene Anschluss-/Funktionsprüfungen. Motorloses DCC-Rücklesen im Fahrzeug wird damit keine Voraussetzung des Gesamtprojekts. Das sagt noch nichts über den mfx-Lichtbetrieb des eingebauten Slaves aus.

## 5. Kapitel 16d und selbst ausführbare Prüfungen

16d enthält eine reale Lücke: Für bestückte Netze fehlen die konkreten Kontaktstellen, Geräteparameter und begründeten erwarteten Anzeigen. 16c deckt nur tatsächlich getrennte passive Leiter ab. Ein beim späteren Anschließen entstehender Fehler wird dadurch nicht automatisch erfasst. Die Endprüfung ersatzlos zu streichen wäre deshalb falsch.[^1]

Die geprüften Märklin- und ESU-Einbauanleitungen fordern Anschluss-/Funktionskontrollen, jedoch keine allgemeine externe Abnahme. REV10 macht aus fehlenden Daten eine pauschale Fachprüferpflicht. Ihre Ursache ist die Vermischung von Hersteller-Anschlussrollen, Identifikation des eigenen Exemplars und Bewertung einer konkreten Messung.[^4][^19]

### Erforderliche Ersatzstruktur

Für jede Messung muss eine kurze Karte sechs Angaben enthalten: die beiden auf eigenen Fotos markierten Kontaktstellen; angeschlossene und getrennte Teile einschließlich Restenergie; bekannter Sollpfad; Messmodus und Prüfparameter; erwartete Anzeige mit Abbruchkriterium; positive Kontaktkontrollen vor und nach der Reihe. Erst diese Angaben machen den Handgriff selbst ausführbar.

Ein niedriger Widerstand über bestückte Elektronik kann beabsichtigt sein. Ein hoher Widerstand ohne nachgewiesenen Kontakt beweist keine Isolation. Deshalb darf die neue Fassung keine pauschale OL-Forderung für sämtliche Pads oder beliebige Widerstandsgrenzen erfinden. Die 21MTC-Norm benennt Schnittstellenfunktionen; sie liefert keinen Schaltplan der konkreten LoDi-Revision.[^24]

LoDi dokumentiert Anschlussrollen, Nicht-S-/S-Unterschiede und die AUX-Auswahl ab V1.50. Bei übereinstimmender Ausführung sind diese Angaben nutzbar. Das Beispiel 33701 bestätigt jedoch nicht automatisch die Mechanik oder jeden Leiterbahnverlauf des 2976. Front-VCC, internes 21MTC-Vcc, U+, Elektronik-GND und Radmasse bleiben sorgfältig getrennt.[^25][^24]

### Fünf notwendige Datenpakete

| Paket | Konkreter Inhalt | Wofür benötigt |
|---|---|---|
| Platinen | Beidseitige lesbare Fotos, Revision, Jumper, Träger und LED-Einsätze | Anschlussrollen und reale Bauteilpfade |
| Einbau | Hinterer Schleifer/Radkontakt, Halter, Schrauben, Litzenführung | Mechanische und elektrische Anschlusskarte |
| Messgerät | Exaktes Modell und Handbuch, Prüfspannung/-strom, Bereiche | Zulässige Messmethode und Anzeige |
| Netze | Kupfer, Widerstand, Halbleiter oder noch unbekannt | Begründete Sollauswertung |
| Kontaktierung | Sichere Kontaktstellen, Hilfsleitungen, Vor-/Nachprobe | Ausschluss scheinbarer Offenmessungen |

12d bleibt als geordneter Ablauf erhalten: reale Stromaufnahme feststellen, Montagevariante festlegen, eindeutige Verbindungen herstellen, unbenutzte Litzen einzeln isolieren und nach dem Löten prüfen. Eine offene Angabe sperrt den betroffenen Anschluss und dessen Erststromtest. Sie muss nicht jede davon unabhängige Dokumentation oder bereits vollständig beschriebene passive Prüfung blockieren.

## 6. Funktionstest und neue SID

Adressgleichheit allein beweist keine funktionierende automatische Synchronisation. Der Test muss andere Erklärungen ausschließen: gleiche DCC-Adresse, Zentralen-Traktion, gespeicherte alte Betriebsadresse oder die Bedienung eines zweiten Eintrags. Ein Bildschirm-Lichtsymbol ersetzt keine beobachtete Ausgangsreaktion. Die Grundidee der Tests C und C.a bleibt deshalb richtig.[^1]

| Stufe | Beobachtung | Bestehenskriterium |
|---|---|---|
| Master allein | mfx-Eintrag, F0 und freigegebener Soundtest | Eindeutiger 60977, dokumentierte Funktion |
| Slave ergänzt | Bedienung nur über Master, beide Richtungen bei Fahrstufe 0 | Tatsächliche LV/LR-Reaktionen entsprechen dem festgelegten Mapping |
| Neustart | Gleiche Bedienfolge nach Stromunterbrechung | Verhalten bleibt reproduzierbar |
| Neue SID | Derselbe Master mit tatsächlich anderer Betriebsadresse | Slave folgt ohne neue Konfiguration |
| Rückkehr | Erneuter Test an der ursprünglichen CS3 | Funktionen und Zuordnung weiterhin richtig |

Eine gespeicherte alte Slave-Zeile ist nicht dasselbe wie eine aktive zweite Anmeldung. Vorher-/Nachher-Zustand und tatsächliche Steuerbarkeit sind zu unterscheiden. Löschen oder Ausblenden darf keinen bestandenen Ein-Zug-Test vortäuschen. Änderungen am späteren Sound-/Funktionsprojekt entwerten die jeweils betroffenen Mappingtests; T9 bleibt erforderlich.[^1]

### Datenbeleg ohne pauschales Löschen

Eine passende eigenständige MS/Gleisbox kann einen anderen Adresszustand erzeugen. Die MS als Bediengerät an derselben CS3 ist dagegen kein unabhängiger Adressgeber. Die MS-Anleitung liefert keine allgemeine eindeutige SID-Anzeige; die Seriennummer der Mobile Station ist nicht die Decoderidentität.[^26]

Ein möglicher Nachweisweg ist der **passive CAN-Mitschnitt der normalen Anmeldung** am unabhängigen System. Die Bind-Antwort dokumentiert die ausgeführte Zuweisung. Ein erfolgreicher Adresszustand erfordert zusätzlich die nachgewiesene Anmeldung und Steuerbarkeit des Masters. Besonders eindeutig ist eine passive positive MFX-Verify-Antwort für dieselbe UID und die neue SID. Der Beobachter sendet keine eigenen Verify-Kommandos. Ein geeigneter Lesezugang ist noch nicht bestätigt; gleiche SID bedeutet keinen bestandenen Wechseltest.[^6]

Der Quellenname „Get_MFX_UID“ allein genügt nicht als Unbedenklichkeitsnachweis: Das geprüfte Raildue-Beispiel sendet aktiv Neuanmeldezähler, Protokollfreigabe und GO. Es ist kein passiver Leser und wurde nicht ausgeführt.[^27]

Der nächste Berichtsschritt darf diese Restlücke daher weder mit „Fachprüfer bestätigt“ überdecken noch durch ein pauschales Datenbank-Reset lösen. Nötig ist ein konkreter beobachtbarer Adresszustand mit dokumentierter Herkunft.

## 7. Befunde und Dokumentkorrekturen

Die acht Prüfpunkte unterscheiden Fehler im vorliegenden Urteil, ergänzte Belege und bereits in REV10 ausgewiesene Restaufgaben. Sie sind keine acht neu entdeckten REV10-Fehler und bescheinigen keine Defekte am Zug. „P1“ bezeichnet eine für die nächste Programmierung oder den Erststrom wesentliche Lücke; „P2“ eine relevante Ablauf-/Dokumentverbesserung.

| ID | Befund / Ursache | Einordnung | Konsequente Korrektur |
|---|---|---|---|
| R1 | Praxisbericht als Beleg für genau das Artikelpaar überdehnt | P2; Fehler im vorliegenden Prüftext | Decoderfamilien vom konkreten 60977/59649-Paar trennen. |
| R2 | Herstellerwert bisher über allgemeine Quellen begründet | P1; passender Primärbeleg ergänzt | 60977-CV8=131 primär belegen, ESU-Abbildung separat prüfen. |
| R3 | CS3-Datenformat bislang nicht mit Original-Testdaten gestützt | P1; erheblich besser belegt | Rohdatensatz und mfxuid eindeutig sichern; uid nicht verwechseln. |
| R4 | Originale ESU-Aktivierungsabbildung fehlt | P1; bereits in REV10 ausgewiesene Restlücke | Originalvergleich aus/an/aus einschließlich sämtlicher Änderungen. |
| R5 | „Fachprüfer“ ersetzt konkrete Messparameter | P1; Ursache diagnostiziert | Sechs-Felder-Messkarten am tatsächlichen Aufbau ausfüllen. |
| R6 | Wartungsweg für motorlosen Aufbau bleibt unkonkret | P2; Ablauf lässt sich festlegen | DCC-Wartung verbindlich auf quittierender Einzelaufnahme. |
| R7 | Prüfaufnahme noch nicht ausführbar beschrieben; 53900-Daten widersprüchlich | P1; konkrete Auswahl-/Lastlücke | Ausgangsart und echte Lasten dokumentieren. |
| R8 | Umfangsziel als feste Kürzungsquote behauptet | P2; nicht nachgewiesen | Repräsentativen Satzversuch einschließlich Fotos und Messkarten. |

### Konsequenz für die neue Aufteilung

Die Aufteilung in Werkstattanleitung und Nachweisdossier bleibt sinnvoll. **A-C dürfen beim Eigenweg jedoch nicht vollständig aus dem Arbeitsablauf verschwinden:** Sie enthalten die notwendigen Handgriffe für Identität und Funktionstest. In der Werkstattanleitung bleiben die kurzen ausführbaren Karten; Herleitungen, Diskussionen und historische Quellen wandern in das Dossier.[^1]

Prüftore erhalten fortlaufende Namen in tatsächlicher Reihenfolge: Vorbereitung/Identität, Synchronisationsnachweis, Mechanik, Verdrahtung, Erststrom, Endabnahme. Eine einmalige Zuordnungstabelle zu G0-G4 erhält die Rückverfolgbarkeit. Das ist ein Redaktionsvorschlag, noch keine Änderung der geltenden REV10.

Die 92 Seiten und etwa 17.300 Wörter auf S. 14-63 sind bestätigt. Die 26 Seiten Nachweisanteil enthalten auch echte Prüfabläufe. Fotos und Gehäuseprüfung auf S. 64-67 fehlen im genannten Werkstatt-Wortumfang. Eine notwendige Textkürzung um genau 20-25 % folgt daraus nicht. Unverändert bleiben müssen die konkreten Warnungen vor gefährlichen Handgriffen, Motor-Kontaktkontrollen, 12d, 16c, Schritte 52/54 sowie T1-T9 und die geschlossene Gehäuseprüfung.[^1]

## 8. Entscheidungsweg und nächste Umsetzungswelle

**Empfohlen wird ein klar begrenzter Eigenweg mit CS3 und kostenloser ESU-Software.** Weiteres allgemeines Suchen nach „Master/Slave“ hat jetzt geringeren Nutzen als der konkret fehlende Originalexport und der eigene Rohdatensatz. Ein Kauf wird an eine bestimmte verbleibende Funktion gebunden.

| Weg | Nutzen | Entscheidungsgrenze |
|---|---|---|
| CS3 + Offline-Export | Vorhandene Zentrale und gezielte CV-Liste nutzen | Fortsetzen, wenn Export erklärt, Identität gesichert und Einzelaufnahme zuverlässig quittiert. |
| Eigener 53451 | Direkte ESU-Konfiguration und notwendige Firmwarepflege | Sinnvoll bei belegtem Updatebedarf oder wenn kontrollierter CS3-Zugriff nicht gelingt. |
| Gemeinsame DCC-Adresse | Möglicher Rückfallweg ohne Traktion | Automatische mfx-Anmeldung entfällt; gesonderte Zielentscheidung und Tests nötig. |

ESU nennt die gemeinsame manuelle DCC-Adresse als Alternative. Sie darf nicht als bereits gleichwertig erfülltes mfx-Ziel verbucht werden. Ebenso ersetzt ein 53451 weder den richtigen Masterdatensatz noch die Montage-/Messprüfung. Der vorhandene Märklin 60971 bleibt für den 60977 und seine Märklin-Konfiguration zuständig.[^2][^28][^1]

### Reihenfolge mit prüfbaren Ergebnissen

**1. Software- und Identitätsnachweis.** Tatsächliche CS3-Version, eigener 60977-Rohdatensatz und vorhandener Windows-Zugang. Danach das Offline-Vergleichsprotokoll aus Abschnitt 2 erzeugen. Abschlussprodukt: eindeutige Eingabebedeutung und vollständige Originaländerungsliste, weiterhin getrennt von realen Decoderwerten.

**2. Prüfaufnahme und Erst-Leseprotokoll.** Tatsächlichen Prüfstand mit Steckerorientierung, AUX-Ausgangsart, Motor-/Lautsprecherlast und alleiniger Datenquelle dokumentieren. Für den ESU Altzustand sowie nachvollziehbare Rücklesung sichern. Ein fehlender ACK führt zu Zustandsklärung, nicht zu wiederholtem Schreiben.

**3. Individuelle Wertekarte und Paarversuch.** Erst aus den vorherigen Ergebnissen eine auf genau diese Decoder begrenzte Karte ableiten. Einzelprogrammierung, anschließend gemeinsamer mfx-Test und dokumentierter Adresswechsel. Ergebnisprotokoll mit Fehlerstufe statt pauschalem „funktioniert nicht“.

**4. Werkstattfassung vervollständigen.** Reale Platinen-/Montagefotos und Multimeterdaten in die Messkarten einarbeiten. Synchronisationsunabhängige Motorkapitel können parallel redaktionell gestrafft werden. Vor Freigabe sämtliche Querverweise, Warnungen und die Kurzfassung gegen REV10 prüfen.

Benötigt werden: CS3-Rohdatensatz/Version; Windows-/ESU-Softwarestand; Prüfaufnahme; Platinen-/Einbaufotos; Multimeterhandbuch; Gerätedaten von MS/Gleisbox und ein bestätigter unabhängiger SID-Nachweisweg. Ein anderer nachvollziehbarer Adressnachweis kann einen CAN-Mitschnitt ersetzen. Ohne diese Daten wäre eine zahlenfertige Programmier- oder Messanleitung erfunden. **Die Recherche ist abgeschlossen; die reale Inbetriebnahme steht weiterhin aus.**

## Quellen

1. ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf. Lokale Referenz, 10.09.2026; insbesondere S. 1, 7-13, 39-40, 52-55, 74-89. Lokale Quelldatei.

2. ESU. Master/Slave Adress-Synchronisation. Undatiert; Herstellerbeispiel LokSound 5. Abruf 10.09.2026. [Originalquelle](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/).

3. MTB-Ontour. Umbau ICE 2 Märklin 36712 auf mSD3 / DCC, Beitrag 4. Stummiforum, 26.02.2023, 21:03. Erfahrungsbericht. [Originalquelle](https://www.stummiforum.de/t212683f5-Umbau-ICE-Maerklin-auf-mSD-DCC.html).

4. Märklin. Nachrüstdecoder 60975/60976/60977. Impressum 260057/1025/Sc7Ef, 10/2025; 192 PDF-Seiten. Deutscher Teil; CV8 auf S. 19. [Originalquelle](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf).

5. Stefan Krauß. Schienenformat mfx. Version 2.3, 17.06.2017; S. 22-23 und 39, §6.4.1. Originale Protokollanalyse, keine Herstellerfreigabe. [Originalquelle](https://www.skrauss.de/modellbahn/Schienenformat.pdf).

6. Märklin. CAN-Protokoll, Version 2.0. MFX Bind/Verify auf S. 28-29; lokomotive.cs2 auf S. 50-51. Herstellerprotokoll für CS2; lokale Kopie vorhanden. [Originalquelle](https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf).

7. TrainControl. CS2File.java. Commit 5f0a75e33256c4c1b4ac1998134c4bd04030fed0; Dateipfad und versionsabhängige JSON-API-Auswahl. [Originalquelle](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/src/org/traincontrol/marklin/file/CS2File.java#L184).

8. TrainControl. test/lokomotive_cs3.cs2. Derselbe Commit; Originaltestdaten mit uid, mfxuid, adresse und sid. [Originalquelle](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/lokomotive_cs3.cs2#L4).

9. TrainControl. test/CS3_loks_v260.json. Derselbe Commit; 154 Lokobjekte, 112 mit mfxuid. Vollständig ausgewertetes Software-Testmaterial. [Originalquelle](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/CS3_loks_v260.json).

10. JMRI. ESU_LokPilot5.xml. Commit 31e482094d472e481c1fb54f9901093c2efbfcec; MKL Z. 186, Einbindungen Z. 246/256. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/ESU_LokPilot5.xml#L186).

11. JMRI. esu/v5standardCVs.xml. Derselbe Commit; M4MfgId und M4SerNo, CV191 und CV192:4. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v5standardCVs.xml#L993).

12. JMRI. esu/v4advancedPane.xml. Derselbe Commit; Synchronisationsbereich mit zwei Feldern, ohne separaten Aktivierungsschalter. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4advancedPane.xml#L47).

13. JMRI. CvUtil.java. Derselbe Commit; Auflösung der CV-Listen-/Bereichsnotation. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/util/CvUtil.java#L102).

14. JMRI. SplitVariableValue.java. Derselbe Commit; Bitpositionen, Zerlegung und Zusammensetzung der mehrteiligen Variablen. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/jmrit/symbolicprog/SplitVariableValue.java#L95).

15. ESU. CV-Änderungen anzeigen. Herstellerbeispiel seit Software 4.4.0; Speicherung löscht Änderungsliste. Abruf 10.09.2026. [Originalquelle](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/).

16. ESU. LokProgrammer-Software und Versionshinweise. Download 5.2.18 vom 01.05.2026; .NET 4.8. Abruf 10.09.2026. [Originalquelle](https://www.esu.eu/download/software/lokprogrammer/).

17. Märklin. CS3-Gesamtchangelog bis Version 2.6.0. S. 12: CV-Bedienung ab 2.4.0; S. 26: Vorlagenschreiben; S. 2: Lesefehler. [Originalquelle](https://www.maerklin.de/fileadmin/media/service/cs3/Maerklin_CS3_v2.6.0_changelog.pdf).

18. Märklin. Bearbeitung von CV-Werten von DCC und MM Decodern. Hilfeexport vom 30.05.2018, 2 Seiten; ältere Bedienfassung. [Originalquelle](https://www.maerklin.de/fileadmin/media/clubs/downloads/Loks_CV_Editor.pdf).

19. ESU. LokPilot 5 Betriebsanleitung. 8. Auflage, Januar 2023, 96 Seiten. Modellvarianten, Einbau und Programmierung. [Originalquelle](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e).

20. RailCommunity. RCN-216, DCC-Programmierung. Fassung 24.11.2025, 8 Seiten. Strombegrenzung und Rückmeldeimpuls. [Originalquelle](https://normen.railcommunity.de/RCN-216.pdf).

21. ESU. Profi-Prüfstand 53900 Betriebsanleitung. 2. Auflage, 17.10.2019, 4 Seiten. Lasten und AUX-Anzeigen. [Originalquelle](https://www.esu.eu/download/betriebsanleitungen/profi-pruefstand/?no_cache=1&tx_esudownloads_pi1%5BdownloadItem%5D=3e2cdb190091da48cc2030b2734bbd32).

22. ESU. Profi-Prüfstand 53900, Produktbeschreibung. Abruf 10.09.2026; abweichende Lautsprecherangaben gegenüber Quelle 21. [Originalquelle](https://www.esu.eu/produkte/profi-pruefstand/).

23. Märklin. Decoder-Tester 60970. Herstelleranleitung, 32 Seiten; Ausgangsart-, Motor/Funktion-, Impedanz- und Quellenumschalter. [Originalquelle](https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf).

24. RailCommunity. RCN-121, 21MTC-Schnittstelle. Fassung 08.12.2024, 11 Seiten. Pinrollen und Rückmeldung. [Originalquelle](https://normen.railcommunity.de/RCN-121.pdf).

25. Lokstoredigital. Motor WiB ICE-M(-S), Hersteller-Einbauanleitung; Beispiel 33701, Varianten- und Jumperhinweise. Abruf 10.09.2026. [Originalquelle](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/).

26. Märklin. Mobile Station 60653/60657/66950/66955. Herstelleranleitung; eigenständiger Gleisboxbetrieb und Betrieb an Central Station. [Originalquelle](https://static.maerklin.de/damcontent/2a/47/2a470bed20017f68f92306725d49fca81702905959.pdf).

27. Raildue. Beispiel Get_MFX_UID.ino. Commit 4c5698ddb7332826872530fc61ee774fe9c4e82e; aktive Kommandos in SystemGo und Startablauf. [Originalquelle](https://github.com/gelit/Raildue/blob/4c5698ddb7332826872530fc61ee774fe9c4e82e/examples/Get_MFX_UID/Get_MFX_UID.ino).

28. ESU. Digitalkatalog 2025/2026, 1. Auflage. S. 62: LokProgrammer und Fremddecoder im Einzel-CV-Modus. [Originalquelle](https://www.esu.eu/fileadmin/download/brochures/2025/52984_Digitalkatalog_2025-2026_DE_1.Auflage_eBook.pdf).

29. JMRI. esu/v4decoderInfoCVs.xml. Commit 31e482094d472e481c1fb54f9901093c2efbfcec; eigene Seriennummer und Firmwarefelder getrennt vom Masterverweis. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml#L26).

30. Märklin. Central Station 3, Artikel 60216/60226. Kurzanleitung ab Software 2.5, 48 PDF-Seiten; Einrichtung, Programmierung und Sicherung. [Originalquelle](https://static.maerklin.de/damcontent/c1/ce/c1ce554ad6ad195c04e32ba1b4dd64511764068661.pdf).

## Nachweisstand

Untersuchung vom 10./11.09.2026, abgeschlossen am 11.09.2026. Grundlage sind die in diesem Zeitraum abgerufenen Quellen und die lokale REV10. REV10-SHA-256: 2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0. JMRI-Vergleich: REV10-Commit 32eca6cddc18a55f2efdfdbc970cca96b7511827 gegen 31e482094d472e481c1fb54f9901093c2efbfcec; sieben untersuchte Dateien jeweils identisch. Relevante Quellen wurden vollständig gelesen; kritische PDF-Seiten und Prüfstandabbildungen zusätzlich visuell geprüft. Originalquellen, Teilnachweise und Hash-Manifeste liegen im zugehörigen lokalen Nachweisordner. Es wurde kein Decoder oder Zug programmiert, bestromt oder vermessen und keine CS3 angesprochen. Ein originaler LokProgrammer-Aktivierungsexport liegt aus diesem Lauf nicht vor. Quellenfeststellungen, Umsetzungsvorschläge und ausstehende Geräteergebnisse sind getrennt.

[^1]: ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf. Lokale Referenz, 10.09.2026; insbesondere S. 1, 7-13, 39-40, 52-55, 74-89. Lokale Quelldatei.
[^2]: ESU. Master/Slave Adress-Synchronisation. Undatiert; Herstellerbeispiel LokSound 5. Abruf 10.09.2026. [Originalquelle](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/).
[^3]: MTB-Ontour. Umbau ICE 2 Märklin 36712 auf mSD3 / DCC, Beitrag 4. Stummiforum, 26.02.2023, 21:03. Erfahrungsbericht. [Originalquelle](https://www.stummiforum.de/t212683f5-Umbau-ICE-Maerklin-auf-mSD-DCC.html).
[^4]: Märklin. Nachrüstdecoder 60975/60976/60977. Impressum 260057/1025/Sc7Ef, 10/2025; 192 PDF-Seiten. Deutscher Teil; CV8 auf S. 19. [Originalquelle](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf).
[^5]: Stefan Krauß. Schienenformat mfx. Version 2.3, 17.06.2017; S. 22-23 und 39, §6.4.1. Originale Protokollanalyse, keine Herstellerfreigabe. [Originalquelle](https://www.skrauss.de/modellbahn/Schienenformat.pdf).
[^6]: Märklin. CAN-Protokoll, Version 2.0. MFX Bind/Verify auf S. 28-29; lokomotive.cs2 auf S. 50-51. Herstellerprotokoll für CS2; lokale Kopie vorhanden. [Originalquelle](https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf).
[^7]: TrainControl. CS2File.java. Commit 5f0a75e33256c4c1b4ac1998134c4bd04030fed0; Dateipfad und versionsabhängige JSON-API-Auswahl. [Originalquelle](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/src/org/traincontrol/marklin/file/CS2File.java#L184).
[^8]: TrainControl. test/lokomotive_cs3.cs2. Derselbe Commit; Originaltestdaten mit uid, mfxuid, adresse und sid. [Originalquelle](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/lokomotive_cs3.cs2#L4).
[^9]: TrainControl. test/CS3_loks_v260.json. Derselbe Commit; 154 Lokobjekte, 112 mit mfxuid. Vollständig ausgewertetes Software-Testmaterial. [Originalquelle](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/CS3_loks_v260.json).
[^10]: JMRI. ESU_LokPilot5.xml. Commit 31e482094d472e481c1fb54f9901093c2efbfcec; MKL Z. 186, Einbindungen Z. 246/256. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/ESU_LokPilot5.xml#L186).
[^11]: JMRI. esu/v5standardCVs.xml. Derselbe Commit; M4MfgId und M4SerNo, CV191 und CV192:4. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v5standardCVs.xml#L993).
[^12]: JMRI. esu/v4advancedPane.xml. Derselbe Commit; Synchronisationsbereich mit zwei Feldern, ohne separaten Aktivierungsschalter. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4advancedPane.xml#L47).
[^13]: JMRI. CvUtil.java. Derselbe Commit; Auflösung der CV-Listen-/Bereichsnotation. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/util/CvUtil.java#L102).
[^14]: JMRI. SplitVariableValue.java. Derselbe Commit; Bitpositionen, Zerlegung und Zusammensetzung der mehrteiligen Variablen. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/jmrit/symbolicprog/SplitVariableValue.java#L95).
[^15]: ESU. CV-Änderungen anzeigen. Herstellerbeispiel seit Software 4.4.0; Speicherung löscht Änderungsliste. Abruf 10.09.2026. [Originalquelle](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/).
[^16]: ESU. LokProgrammer-Software und Versionshinweise. Download 5.2.18 vom 01.05.2026; .NET 4.8. Abruf 10.09.2026. [Originalquelle](https://www.esu.eu/download/software/lokprogrammer/).
[^17]: Märklin. CS3-Gesamtchangelog bis Version 2.6.0. S. 12: CV-Bedienung ab 2.4.0; S. 26: Vorlagenschreiben; S. 2: Lesefehler. [Originalquelle](https://www.maerklin.de/fileadmin/media/service/cs3/Maerklin_CS3_v2.6.0_changelog.pdf).
[^18]: Märklin. Bearbeitung von CV-Werten von DCC und MM Decodern. Hilfeexport vom 30.05.2018, 2 Seiten; ältere Bedienfassung. [Originalquelle](https://www.maerklin.de/fileadmin/media/clubs/downloads/Loks_CV_Editor.pdf).
[^19]: ESU. LokPilot 5 Betriebsanleitung. 8. Auflage, Januar 2023, 96 Seiten. Modellvarianten, Einbau und Programmierung. [Originalquelle](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e).
[^20]: RailCommunity. RCN-216, DCC-Programmierung. Fassung 24.11.2025, 8 Seiten. Strombegrenzung und Rückmeldeimpuls. [Originalquelle](https://normen.railcommunity.de/RCN-216.pdf).
[^21]: ESU. Profi-Prüfstand 53900 Betriebsanleitung. 2. Auflage, 17.10.2019, 4 Seiten. Lasten und AUX-Anzeigen. [Originalquelle](https://www.esu.eu/download/betriebsanleitungen/profi-pruefstand/?no_cache=1&tx_esudownloads_pi1%5BdownloadItem%5D=3e2cdb190091da48cc2030b2734bbd32).
[^22]: ESU. Profi-Prüfstand 53900, Produktbeschreibung. Abruf 10.09.2026; abweichende Lautsprecherangaben gegenüber Quelle 21. [Originalquelle](https://www.esu.eu/produkte/profi-pruefstand/).
[^23]: Märklin. Decoder-Tester 60970. Herstelleranleitung, 32 Seiten; Ausgangsart-, Motor/Funktion-, Impedanz- und Quellenumschalter. [Originalquelle](https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf).
[^24]: RailCommunity. RCN-121, 21MTC-Schnittstelle. Fassung 08.12.2024, 11 Seiten. Pinrollen und Rückmeldung. [Originalquelle](https://normen.railcommunity.de/RCN-121.pdf).
[^25]: Lokstoredigital. Motor WiB ICE-M(-S), Hersteller-Einbauanleitung; Beispiel 33701, Varianten- und Jumperhinweise. Abruf 10.09.2026. [Originalquelle](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/).
[^26]: Märklin. Mobile Station 60653/60657/66950/66955. Herstelleranleitung; eigenständiger Gleisboxbetrieb und Betrieb an Central Station. [Originalquelle](https://static.maerklin.de/damcontent/2a/47/2a470bed20017f68f92306725d49fca81702905959.pdf).
[^27]: Raildue. Beispiel Get_MFX_UID.ino. Commit 4c5698ddb7332826872530fc61ee774fe9c4e82e; aktive Kommandos in SystemGo und Startablauf. [Originalquelle](https://github.com/gelit/Raildue/blob/4c5698ddb7332826872530fc61ee774fe9c4e82e/examples/Get_MFX_UID/Get_MFX_UID.ino).
[^28]: ESU. Digitalkatalog 2025/2026, 1. Auflage. S. 62: LokProgrammer und Fremddecoder im Einzel-CV-Modus. [Originalquelle](https://www.esu.eu/fileadmin/download/brochures/2025/52984_Digitalkatalog_2025-2026_DE_1.Auflage_eBook.pdf).
[^29]: JMRI. esu/v4decoderInfoCVs.xml. Commit 31e482094d472e481c1fb54f9901093c2efbfcec; eigene Seriennummer und Firmwarefelder getrennt vom Masterverweis. [Originalquelle](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml#L26).
[^30]: Märklin. Central Station 3, Artikel 60216/60226. Kurzanleitung ab Software 2.5, 48 PDF-Seiten; Einrichtung, Programmierung und Sicherung. [Originalquelle](https://static.maerklin.de/damcontent/c1/ce/c1ce554ad6ad195c04e32ba1b4dd64511764068661.pdf).
