# ICE 2976 - korrigierter forensischer Prüfbericht zu REV9

**Stand:** 10.09.2026  
**Prüfgegenstand:** ICE_2976_Umbauanleitung_REV9_MIT_SCHNELLANLEITUNG.pdf  
**Zusätzlich geprüfter Ausgangsbericht:** ICE2976_REV9_Pruefbericht.md  
**Ergebnis:** Korrigierter Dokumentprüfbericht, keine Hardware-, Anschluss- oder Betriebsfreigabe.

## 0. Auftrag, gesicherte Dateien und Methode

Der Nutzerauftrag ist die forensische Prüfung und Korrektur des Prüfberichts. Die Umbauanleitung selbst wird in diesem Auftrag **nicht geändert**. Auch ihre 69 Seiten werden weder gekürzt noch als REV10 neu veröffentlicht. Originalbericht und PDF bleiben unverändert erhalten. Diese Datei ersetzt die Bewertung und Korrekturvorschläge des Ausgangsberichts; dessen frühere Ersatztexte dürfen nicht parallel als Bauanweisung verwendet werden.

| Nachweis | Ergebnis dieses Abgleichs |
|---|---|
| PDF SHA-256 | `c1c1b1a2772f0e25385ffe911041b1cd2f7351277ada2ed5d8ecbe1be0070d29` |
| Ausgangsbericht SHA-256 | `efb6ba4a3f84b1519b11bf4e1e1a122f0ab910a1ff729f7b6dd09a1e1a3e0554` |
| PDF | 69 A4-Seiten; Titel „ICE 2976 - REV9 vollständig mit Schnellanleitung“; Producer pypdf |
| Interne Navigation | 89 Link-Annotationen auf 67 unterschiedliche Zielseiten: 67 im Inhaltsverzeichnis, 22 in der Schnellanleitung; Zielauflösung und sichtbare Linktexte gegen Zielseiten geprüft |
| Externe Verweise | 193 URI-Annotationen, 44 unterschiedliche Adressen; die Anzahl ist kein Erreichbarkeitsnachweis aller Adressen |
| Ausgangsbericht | Vollständig gelesen, 878 Zeilen; alle R-01 bis R-47 und W-01 bis W-18 behandelt |
| Praktische Hardwaretests | Keine; keine Decoder programmiert, keine Ströme/Isolation am Zug gemessen |

**Arbeitsweise:** Vollständige Lektüre des Ausgangsberichts; Textabgleich der betroffenen PDF-Kapitel; gezielte visuelle Prüfung insbesondere S. 3, 13, 18, 29, 68 und 69. Die Märklin-60941-Zeichnung wurde zusätzlich im Herstelleroriginal visuell geprüft. Das ist **keine erneut behauptete vollständige visuelle Abnahme sämtlicher 69 Seiten**.

Drei getrennte KI-Teilprüfungen bearbeiteten Hardware/Elektrik, Programmierung/Quellen sowie Anfängerablauf/Schnellanleitung. Sie arbeiteten im gemeinsamen Projektkontext; dies war keine Blindprüfung durch drei menschliche Sachverständige. Die Hauptinstanz konsolidierte die Ergebnisse und prüfte strittige Kernbelege nach. Ein KI-Konsil erhöht die Prüftiefe, ersetzt aber keine Messung am Modell.

Die Angaben des Ausgangsberichts zu seinen eigenen drei Instanzen, zwei bytegleichen Uploads und „56 maschinell verifizierten Zitaten“ sind ohne dessen Rohprotokolle nicht vollständig rekonstruierbar. Sie werden nicht als in diesem Lauf nachgewiesene Tatsachen übernommen. Die gegenwärtig vorliegenden Dateien wurden stattdessen eigenständig identifiziert.

**Evidenzkennzeichnung:** K1 = Herstellerangabe; K2 = Norm/Zeichnung oder ausdrücklich bezeichnete technische Ableitung; K3 = Softwareimplementierung; K4 = konkreter Erfahrungsbericht; K5 = Hypothese; K6 = Messung am realen Nutzerbauteil. Eine Norm-Pinrolle ist nicht automatisch eine gemessene Leiterbahn der LoDi-Platine. In diesem Abgleich liegt keine neue K6-Evidenz vor.

## 1. Kurzurteil und korrigierte Zählung

Der Ausgangsbericht erkennt wichtige Ausführungs- und Nachweislücken. Seine **Ersatztexte sind jedoch selbst teilweise fehlerhaft oder nicht ausreichend belegt**. Besonders pauschale Messgrenzen, vermutete Bauteildemontage und vermeintliche Kaufzwänge dürfen nicht übernommen werden.

Die sinnvollen Schutzmechanismen der REV9 bleiben erhalten: Decoder vor Löt-/Widerstandsarbeiten entfernen, passive Leitungen von bestückter Elektronik unterscheiden, echte positive Kontaktkontrollen, ursprüngliche Werte sichern, keine geratenen Synchronisationswerte und keine automatische Einmessfahrt.

| Bewertung des jeweiligen R-Befunds | Anzahl |
|---|---:|
| Bestätigt | 8 |
| Teilweise bestätigt - Kern oder Verbesserungsbedarf nachvollziehbar, Begründung/Umfang/Ersatz zu korrigieren | 32 |
| Offen - weiterer Nachweis erforderlich | 6 |
| Nicht bestätigt als behauptete Pflichtlücke | 1 |
| **Gesamt** | **47** |

Die Ausgangsprioritäten **4×P1, 24×P2, 19×P3** bleiben je ID zur Rückverfolgung sichtbar. Sie sind keine neue Statistik von 47 bewiesenen Defekten. „Teilweise bestätigt“ bedeutet insbesondere nicht „behoben“. Die sicherheitsrelevanten Checklisten-/Handgriffslücken R-01 bis R-04 bleiben vor einer späteren Bau-/Betriebsfreigabe zu bearbeiten.

**P0-Aussage präzisiert:** In den geprüften Anweisungen wurde kein eindeutig belegter unmittelbarer Zerstörungsschritt unter Einhaltung aller genannten Voraussetzungen identifiziert. Daraus folgt weder Fehlerfreiheit noch Sicherheit des realen Aufbaus. Die Aussage „keine wörtliche Befolgung kann Hardware zerstören“ wäre mit dieser Evidenz zu weitgehend.

**Die wichtigsten Korrekturen am Bericht:**

- R-02: Fehlende vollständige Vor-Erststrom-Karte ja; allgemeines „OL an allen decoderlosen Platinenpfaden“ nein.
- R-11: Vorhandene Gleisbox und Mobile Stations berücksichtigen. Zusätzlicher Zentralenkauf nicht automatisch erforderlich.
- R-01: CS3-Fahrbefehl bei unverändertem Digitalgleis von elektrischer Gleisbeeinflussung unterscheiden. LoDi 512 nicht als universellen Platinentausch freigeben.
- R-15: Einzel-Ausgangsgrenze, Summengrenze und Kupplungsbelastbarkeit trennen. Unbekannte Last wird nicht dadurch sicher, dass nur ein Wagen angeschlossen wird.
- R-23/R-35/R-45: Keine vermutete Kappe entfernen, kein allgemeiner Kapazitäts-Nulltest und keine Lieferumfangsbehauptung aus unvollständiger Stückliste.
- R-42: Inzwischen erreichbare Originalquellen verwenden; fehlender Abruf ist kein Beweis einer falschen Fundstelle.

## 2. Was dieser Bericht nicht freigibt

G0 für **Märklin 60977 + ESU 59649** bleibt offen: reale Masteridentität, Aktivierungsabbildung, Firmware, sicherer Lese-/Schreibweg und reproduzierbare Synchronisation müssen zusammen nachgewiesen werden. R-11 ist nur ein Teil davon. Weder eine zweite Zentrale noch der Kauf eines LokProgrammers allein schließt G0.

Ebenso offen bleiben tatsächliche Platinenrevisionen, hinterer Schleifer/Radkontakt, Halterung und Pinlage, LED-Zweig-/Stromdaten, 2976-Kupplungspassung und die reale Lastfreigabe. Für den künftigen Signalhalt ist eine eigene Anlagenabnahme nötig. Beide vorhandenen 60974 bleiben in dieser Phase unverbunden.

Die folgenden Texte sind **Korrekturaufträge für die nächste Anleitung**, keine sofortige Erlaubnis zum Löten, Abnehmen unbekannter Teile oder Schreiben genannter CVs. Jede reale Durchführung bleibt an ihre benannten Voraussetzungen gebunden.

## 3. Vollständiger Abgleich R-01 bis R-47

Die Nummern entsprechen unverändert dem Ausgangsbericht. „Ausgangspriorität“ bewahrt dessen Zuordnung; „Status“ ist das Ergebnis dieser Gegenprüfung.

### R-01 - Anlagenbereich und gemeinsam verbundene Schleifer

**Status: Teilweise bestätigt. Ausgangspriorität: P1.**

**Beleg:** REV9 S. 4/32 sieht den gemeinsamen RT-Pfad vor; S. 32/45/69 enthält bereits Verbote zum Überbrücken fremder Versorgungs- und elektrischer Bremsabschnitte. LoDi unterscheidet ausdrücklich zwischen unverändert versorgtem Gleis bei Computersteuerung und gleisseitiger Zugbeeinflussung. [LoDi-Motoranleitung](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/)

**Korrektur des Befunds:** Es fehlt eine früh platzierte, ausführbare Bestandsprüfung; die Verbote fehlen nicht vollständig. Die Aussage „Signale vorhanden → ICE-M-S zwingend“ ist für die geplante CS3-Fahrbefehlslösung zu pauschal. Auch „jede Mittelleiter-Trennstelle“ ist zu weit: Entscheidend ist, ob die beiden Schleifer unterschiedlich versorgte, abgeschaltete oder mit Bremsinformation beaufschlagte Bereiche verbinden. Zwei Einspeisungen desselben unveränderten CS3-Ausgangs sind keine zwei Zentralen.

**Korrekturauftrag:** Vor Betriebsfreigabe einen begrenzten Fahrbereich samt sämtlichen Einspeisungen, Signal-Fahrstromkontakten, Relais, Bremsmodulen und Grenzen erfassen. Zunächst genügt ein räumlich getrenntes Prüfgleis mit genau einer Quelle. Die zukünftige Bahnhofssteuerung muss dafür noch nicht fertig sein. CS3, Gleisbox, Booster und Programmierausgang nicht über den Zug verbinden. Bei gleisseitiger Beeinflussung ist diese Architektur dort gesperrt; weder ein Platinentausch auf 512 noch das dauerhafte Durchspeisen eines Haltabschnitts ist eine freigegebene Einzelkorrektur. Beides verlangt einen eigenen Systementwurf.

**Risiko/Schließung:** Ein gespeister Haltabschnitt kann eine dort stehende Lok anfahren lassen, wenn deren aktuelle Betriebsbedingungen das zulassen; das ist kein zwangsläufiges Ereignis. Fremde Ausgangsstufen können über den Zug verbunden werden. Schließen durch nachvollziehbaren Anlagenplan und getrennte Betriebsprüfung, nicht durch einen absichtlichen Überbrückungsversuch.

### R-02 - Licht-/Hilfsleitungsprüfung fehlt als geschlossene Vor-Erststrom-Karte

**Status: Teilweise bestätigt. Ausgangspriorität: P1.**

**Beleg:** S. 9/10/21/27/28/49 enthalten bereits Trenn-, Plus-/Masse- und Einzelisolierungsregeln. S. 49 Nr. 1 verlangt ausdrücklich eine Prüfung von LED-Plus, Kathoden und Halter gegen Chassis. S. 50 verlangt positive Kontaktkontrollen und verbietet pauschale OL-Bewertung bestückter Elektronik. Unvollständig bleibt die konkrete, je Kopf auszuführende Mess- und Sichtkarte unmittelbar vor Schritt 52/54.

**Der Ersatztext des Ausgangsberichts wird zurückgenommen.** „Decoder/Puffer abgezogen“ bedeutet nicht „unbestückte Platine“. LoDi-Transistoren, Dioden, Widerstände und gegebenenfalls Kondensatoren bleiben vorhanden. Deshalb darf für VCC, GE, SW/RT, LV/LR, GND usw. nicht pauschal OL oder ein undefinierter Leerwert verlangt werden. Auch ein alter Vergleichswert beweist nicht allein Fehlerfreiheit.

**Korrekturauftrag für die neue Karte:**

1. Jeden Kopf vom Gleis und Wagenbus trennen; alle Versorgungen und beide 60974 abgetrennt. Decoder nur spannungslos abziehen. Keine Hochspannungs-Isolationsprüfung und keinen Kurzschluss zum Entladen verwenden.
2. Chassis und Radstromaufnahme als getrennte Bezugspfade behandeln, solange ihre Verbindung nicht positiv nachgewiesen ist.
3. Für vollständig von Elektronik und Verbrauchern abgetrennte passive Leitungen: beide Enden identifizieren; End-zu-End-Durchgang positiv prüfen; zwei blanke Punkte desselben Metallbezugs positiv prüfen; Leitung gegen diesen Bezug prüfen; anschließend beide positiven Prüfungen wiederholen. Vor-/Nachkontrollen müssen den tatsächlich benutzten Kontakt erfassen. Eine misslungene Nachkontrolle entwertet die Reihe.
4. Leitungen in späterer Einbaulage und bei normaler Bewegung kontrollieren. Nicht durch Isolierungen stechen.
5. Für noch mit einer Platine oder LED verbundene Pfade müssen vor der Messung Revision, Netzzuteilung, Abtrennstellen, Prüfgerät und zulässige Auswertung feststehen. Ein abgezogener Decoder macht diese Pfade nicht automatisch passiv. Ohne diesen Nachweis keine geratenen Sollwerte einsetzen.
6. Vorn insbesondere LED-Plus/VCC, beide Frontzweige und GE; hinten +Ub, LV/LR, freie Trägerlitzen und das GE-Ende erfassen. Vorgesehene Gleisanschlüsse B/GR und 0/GL nicht mit Funktionsplus oder Elektronik-GND verwechseln.
7. Jede unbenutzte Litze einzeln vollständig isolieren und sichern. Neue Lötung oder Montageänderung verlangt Wiederholung der betroffenen vollständigen Prüfserie samt Kontaktkontrollen.

**Schadensmechanismus:** U+ an Radmasse kann einen Strompfad über den Decodergleichrichter erzeugen. Ein Funktionsausgang an Radmasse kann Ausgangsstufe und Gleichrichter belasten. Für eine Berührung mit beliebigem Chassismetall ist zusätzlich dessen elektrische Verbindung maßgeblich. Ein bestimmtes Bauteilversagen oder „in allen Fällen“ ein Schaden ist ohne Schaltung und Schutzverhalten nicht bewiesen.

**Schließung:** Die Korrektur ist erst vollständig, wenn die tatsächlichen Messpunkte und zulässigen Verfahren für diese Bauteile feststehen. Diese Dokumentprüfung liefert keine ausgefüllte Hardware-Messkarte.

### R-03 - Motorloser Kopf: konkrete Anschlussfolge und Versorgung nachweisen

**Status: Teilweise bestätigt. Ausgangspriorität: P1.**

**Beleg:** Die Funktionszuordnung steht auf S. 27/32: B/GR an RT samt hinterem Schleifer, 0/GL an örtliche Radstromaufnahme. S. 28 nennt die LED-Anschlüsse, verbietet eine hintere GE-Speisung und verlangt Einzelisolation. Ein ausgeführter Altzustands-/Schleifernachweis am eigenen 2976 fehlt.

**Korrektur:** Nicht „der Dummy hat keinen Schleifer“ und nicht „kein Altzustandshinweis überhaupt“ behaupten. Der eigene Schleifer ist unbestätigt; S. 49 verlangt seine Identifikation bereits allgemein. Schritt 54 testet beide Köpfe ungekuppelt: Dafür braucht der hintere Kopf tatsächlich eine eigene geprüfte Stromaufnahme.

**Korrekturauftrag:** Vor dem Entfernen alter Leitungen den wirklichen Schleifer, seinen Anschluss und den Radkontakt fotografieren und elektrisch getrennt zuordnen. Für den bestätigten Zielzustand ist der Verbindungspunkt hinterer Schleifer + RT + B/GR zu dokumentieren; 0/GL erhält ausschließlich den vorgesehenen örtlichen Radpfad. GE endet hinten einzeln isoliert und gesichert, ohne Verbindung zu einem hinteren Ausgang, +Ub oder Radmasse. Unbenutzte Trägerlitzen ebenfalls einzeln isolieren. Ein geeigneter dreifacher Löt-/Verbindungspunkt, Zugentlastung und Freiraum müssen am realen Kopf festgelegt werden; „drei Litzen irgendwie verlöten“ reicht nicht.

**Schließung:** Fehlt ein hinterer Schleifer tatsächlich, bleiben der ungekuppelte Test und die Zwei-Schleifer-Lastprüfung gesperrt. Dann benötigt der Plan eine geprüfte Stromaufnahme-Nachrüstung oder eine gesonderte Architekturänderung; keine ungeprüfte Ersatzteilnummer aus 33701 übernehmen.

### R-04 - Schnellanleitung: Isolation und Gleisanschlüsse lokal ergänzen

**Status: Teilweise bestätigt. Ausgangspriorität: P1.**

**Beleg:** S. 68 Schritt 5 nennt +Ub/LV/LR und „GE hinten nicht speisen“, aber nicht die vollständigen B/GR-/0/GL-Handgriffe und die ausdrückliche Isolation aller unbenutzten Litzen. Die Vollfassung S. 27/28/49 enthält Einzelisolierungsregeln; der Warnkopf der Schnellanleitung erklärt die Detailkarten verbindlich.

**Korrektur:** Es handelt sich um eine sicherheitsrelevante Verkürzung am Arbeitsort, nicht um den Nachweis, dass bei vollständiger Befolgung der Anleitung blanke Litzen zulässig wären. Die behauptete Schadenswahrscheinlichkeit ist nicht quantifiziert.

**Ersatz für Schritt 5:** „Nur nach bestätigtem hinterem Schleifer/Radkontakt und Halter: B/GR an den dokumentierten gemeinsamen Schleifer-/RT-Punkt, 0/GL an die bestätigte Radstromaufnahme; +Ub an LED-Plus, Rot über seinen geprüften Widerstand an LV, Weiß über seinen geprüften Widerstand an LR. GE sowie MR/MV, AUX1–4, GND/+5V und weitere tatsächlich unbenutzte Trägerlitzen jeweils einzeln isolieren und sichern. Vor-Erststrom-Karte und Detailkarten vollständig bestehen; 59649 noch nicht einsetzen.“

**Schließung:** In Schritt 9 dieselben Voraussetzungen ausdrücklich referenzieren. Der neue Satz ersetzt nicht die noch zu konkretisierenden Montage- und Messkarten.

### R-05 - Vorab-Eigenanmeldung des ESU und Aussagekraft des Tests

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** F.4 S. 59 unterscheidet korrekt einen manuell angelegten DCC-Serviceeintrag von einer automatischen Anmeldung. Das schließt eine zusätzliche M4-Eigenanmeldung des noch nicht synchronisierten 59649 nicht aus. C3 enthält bereits ein Abbruchkriterium für einen weiter unabhängig steuerbaren Slave.

**Korrektur:** Eine Vorab-Anmeldung ist ein zu prüfendes Verhalten, kein am vorhandenen Decoder beobachtetes Ereignis. Die Lokliste vor und nach jedem Test dokumentieren und Serviceeintrag, alten M4-Eintrag und aktuellen Master unterscheiden. Nicht allein aus einem verbliebenen Datenbankeintrag auf einen aktuell zweiten angemeldeten Decoder schließen.

**Korrekturauftrag:** Testablauf um getrennte Identifikation und Funktionsprüfung ergänzen; keine spontane Lösch-, Reset- oder Umbenennungsaktion als notwendige Reparatur vorgeben. Bei alter Adresse muss festgestellt werden, ob der hintere Decoder darüber tatsächlich noch unabhängig reagiert. Die Aussage „kein zweiter Zug im späteren Betrieb“ gilt erst nach dem Wiederanmeldetest mit kontrolliertem Ausgangszustand. Eine bloß ruhende alte Loklistenkarte widerlegt sie nicht.

### R-06 - mfx-Konfiguration im synchronisierten Betrieb

**Status: Offen. Ausgangspriorität: P2.**

**Befundkorrektur:** „Der Slave empfängt alle mfx-Lese- und Schreibbefehle und übernimmt sie“ ist nicht nachgewiesen. Gemeinsame Betriebsadresse bedeutet nicht automatisch identische interne Behandlung jeder Paketklasse. ESU beschreibt auf seiner Synchronisationsseite das Ausbleiben von RailCom-Antworten; daraus folgt keine vollständige Beschreibung des mfx-Konfigurationsverhaltens. [ESU-Synchronisation](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/)

**Korrekturauftrag:** Bis zur Klärung beide Decoder einzeln und elektrisch getrennt konfigurieren. Einstellungen am gesamten synchronisierten Zug nicht als sicheren Weg voraussetzen. Zuerst Herstellerantwort oder einen kontrollierten, zunächst nur lesenden Vergleich mit gesicherten Einzelzuständen vorsehen.

**Zurückgenommen:** Der Vorschlag einer beliebigen „harmlosen mfx-Änderung“ ohne benannten Parameter, Rückleseweg und Rückfallplan. Ein Schreibtest darf erst nach eigenständiger Freigabe seines genauen Umfangs erfolgen. Die offene Frage bleibt bestehen; eine Rückmeldekollision oder Konfigurationsüberschreibung wird nicht als beobachteter Defekt ausgegeben.

### R-07 - Funktionstasten und endgültiger Soundprojektstand

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 7 und 43 prüfen F0, Richtung, Innenlicht und Sound, aber keine lückenlose Funktionstastenmatrix. S. 39 sieht weitere Projekt-/Konfigurationsarbeiten nach G0 vor.

**Korrektur:** Die Beispiele „ESU-Werksdimmer“ und „Werks-Rangierlicht“ sind hier nicht belegt. Die aktuelle LokPilot-5-Tabelle nennt unter anderem Rangiermodus und ABV-Abschaltung; das sind nicht automatisch veränderte Frontlichter. Der reale Mappingstand bleibt zu prüfen. [ESU-Handbuch, gedruckte S. 67](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e)

**Korrekturauftrag:** Nach dem letzten Projekttransfer Artikel, Firmware und Mappingstände sichern. Alle im endgültigen 60977-Projekt belegten Funktionen bei Fahrstufe 0 einzeln schalten: beide Richtungen, F0 an und aus; erlaubte Wirkung vorn/hinten/Innenlicht/Sound vorher in einer Solltabelle festlegen. Keine ungewollte Rückleuchte bei F0 aus zulassen. Relevante Projekt-, Firmware- oder Mappingänderungen entwerten die betroffenen G0-/Regressionstests auch dann, wenn die Firmwarezahl gleich bleibt.

**Schließung:** Originalexport und ausgefülltes Testprotokoll; nicht nur eine pauschale Aussage „Sound getestet“. Unbestellte Firmwareupdates während der Prüfung nicht mitlaufen lassen.

### R-08 - Index-CVs: vorhandene Regeln zu einer ausführbaren Karte schließen

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 28 sowie F.6/F.7 S. 61/62 verlangen bereits die passende CV31-/CV32-Gruppe für indizierte Register. F.6 ist primär für die noch nicht freigegebenen CV191–195 geschrieben. Diese liegen außerhalb des betreffenden Indexbereichs. Die Behauptung, die Indexvoraussetzung fehle völlig, ist falsch.

**Restlücke:** Eine abschließende Gesamtauslesung über mehrere Indexgruppen ist nicht hinreichend beschrieben. Dieselbe CV-Nummer kann bei anderem Index einen anderen Inhalt bedeuten.

**Korrekturauftrag:** Für jedes tatsächlich benötigte indizierte Register eine Zeile mit Decoder, CV31, CV32, Ziel-CV, Altwert, freigegebenem Zielwert und frischem Rücklesewert erstellen. Index setzen und kontrollieren, dann Altwert lesen, einzeln schreiben und unter unverändertem Index zurücklesen. Bei Gruppenwechsel und abschließender Kontrolle Index erneut zuordnen. Kein pauschaler Gesamtlistenvergleich über verschiedene Gruppen. Rückstellen der Indexwerte nur nach dokumentierter Ausgangslage.

**Grenze:** Die Karte darf keine geratenen Aktivierungsregister enthalten. Die allgemeine Indexmethode ist durch [ESUs CV-Exportbeschreibung](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/) gestützt, ihre konkrete Anwendung auf die Sonderoption bleibt nachzuweisen.

### R-09 - Prüfaufnahme und DCC-Quittierung

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 5 verlangt die Benennung und Eignungsprüfung der Lasten einer Prüfaufnahme. F.4 S. 59 benennt ausdrücklich die ungeprüfte Quittierfähigkeit des motorlosen 59649-Aufbaus und sperrt Schreiben nach Lesefehlern.

**Korrektur:** Aus „Motor und Lautsprecherlast benennen“ folgt nicht zwingend, dass jede Aufnahme einen Motor und Lautsprecher angeschlossen haben muss. Der Ersatz „59649 ausschließlich mit Motor lesen“ ist ohne konkreten Eignungsnachweis zu eng. Der 59649 ist außerdem kein Sounddecoder.

**Korrekturauftrag:** Zwei Verwendungsfälle unterscheiden: geeignete lose Decoder-Prüfaufnahme für G0 und spätere Prüfung des eingebauten motorlosen Kopfes. Für beide den DCC-Lese-/Quittierweg dokumentieren. Fehlerfrei wiederholtes Lesen ist ein Kommunikationsnachweis, kein vollständiger Isolationstest.

**Bei Lesefehler:** STOP, keine Schreibversuche und kein Reset. Versorgung, Kontakt, Protokoll und Quittierlast getrennt eingrenzen; keine selbst erfundene LED-/Widerstands-Ersatzlast einsetzen. Eine fehlende Quittierung beweist weder einen Kurzschluss noch einen defekten Decoder. Ein bestätigter Fachprüfaufbau ist ein zulässiger Rückfallweg.

### R-10 - Firmware- und SID-Nachweis ohne Kaufzwang

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Befundkorrektur:** Das Fehlen einer fertigen CS3-Lesefolge beweist nicht „ohne 53451 kein Leseweg“. Firmware, dauerhafte Decoderkennung und zugewiesene mfx-SID sind unterschiedliche Größen.

**Zusätzliche Recherche:** JMRI bindet für LokPilot 5 eine gemeinsame Informationsdefinition ein. Darin stehen Firmwarefelder unter Index 0/255: CV285:2 als Build sowie CV287/288 als Minor/Major. Das ist ein Implementierungsbeleg K3 und ein konkreter Kandidat für weitere Prüfung, noch keine herstellerbestätigte oder am 59649 getestete Schreib-/Lesekarte. Indexwahl verursacht selbst Schreibzugriffe; die Zahlen hier sind ausdrücklich keine auszuführende Anweisung. [JMRI v5standardCVs](https://raw.githubusercontent.com/JMRI/JMRI/master/xml/decoders/esu/v5standardCVs.xml), [eingebundene Informationsfelder](https://raw.githubusercontent.com/JMRI/JMRI/master/xml/decoders/esu/v4decoderInfoCVs.xml)

**Korrekturauftrag:** Firmware über einen für genau den 59649 bestätigten Weg feststellen; Fachbetrieb/LokProgrammer bleibt eine Option, nicht automatisch ein Kaufbedarf. SID alt/neu getrennt nachweisen. Ein Screenshot mit Lokname, DCC-Adresse oder bloßer Versionsnummer ist kein SID-Nachweis. G0 bleibt bis zur tatsächlichen Identifikation und Prüfung offen.

### R-11 - C7: vorhandene Mobile Station/Gleisbox im Nachweisplan berücksichtigen

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Kontextkorrektur:** Der Nutzer hat neben der CS3 eine Gleisanschlussbox, eine kabelgebundene Mobile Station und eine Mobile Station WLAN genannt. „Es ist nur eine CS3 vorhanden, daher ist G0 nicht abschließbar“ ist als Bestandsaussage falsch. Die genaue Artikelgeneration, passende Versorgung, Software und Anmeldehistorie wurden allerdings nicht nachgewiesen.

**Beleg:** Märklin beschreibt beispielsweise MS2 60653/60657 mit H0-Gleisbox 60113/60116 als eigenständiges mfx-System. Eine an der CS3 betriebene Mobile Station ist dagegen nur ein weiteres Bediengerät desselben Systems. [Märklin-MS2-Anleitung, S. 4/6/23](https://static.maerklin.de/damcontent/2a/47/2a470bed20017f68f92306725d49fca81702905959.pdf)

**Korrekturauftrag:** Zuerst die vorhandenen Artikel und ihre Eignung erfassen. Bei passendem Bestand ein vollständig von CS3, Anlagen- und Programmiergleis getrenntes Gleisbox/MS-System als C7-Kandidat prüfen. Keinen Gleisausgang parallel anschließen. Mobile Station WLAN allein nicht als selbständige Gleisversorgung zählen.

**Bestehenskriterien:** Neue Anmeldung ohne Neukonfiguration des Slaves, nur gewünschter aktiver Zugeintrag, F0/Richtung folgen; zusätzlich tatsächlich andere SID nachweisen. Eine zweite Zentrale kann zufällig dieselbe Zahl vergeben. Ohne belastbaren SID-Nachweis ist der Funktionstest nützlich, aber C7 noch offen. Ein Leihgerät/Fachbetrieb wird erst erforderlich, wenn der vorhandene Bestand den Nachweis nicht ermöglicht. Keinen Zentralenreset anordnen.

### R-12 - Prüftore und Fotoabhängigkeiten widerspruchsfrei ordnen

**Status: Bestätigt. Ausgangspriorität: P2.**

**Beleg:** Die Tabelle S. 1 führt G1 mit Befestigung vor dem Motor-/Altzustandsumbau G2. S. 20/21 benötigt jedoch den vorbereiteten Kopf und einen abgeschlossenen Motorprüfstand. S. 52 fordert vor G0 pauschal Fotos aus D; Foto 2 auf S. 51 setzt bereits die Montageposition im Kopf voraus.

**Korrekturauftrag:** Vor G0 nur zerstörungsfreie Bestandsaufnahme und Fotos loser Teile; keine Demontage allein zur Erfüllung der Fotoliste. G0 umfasst A–C und die tatsächlich benötigten Teile von F. Nach G0: Altzustand/Motorvorbereitung, vollständige Motorprüfung, revisionsbezogene Platinen-/Halterfreigabe, anschließende Leitungs- und Lichtmontage, Vor-Erststrom-Freigabe, gestufte Funktions-/Lastprüfung, Gehäuseabnahme. Die Lagebeschreibung 9c/12b darf früh gelesen werden; tatsächliches Einsetzen erfolgt erst am freigegebenen späten Schritt.

**Korrektur des ursprünglichen Ersatzes:** Nicht lediglich „G2 → G1“ einsetzen und damit alle Vorbedingungen der Bauteilidentifikation nach hinten schieben. Die Tabelle muss Vorprüfung loser Teile von Montage-/Einsetzfreigabe unterscheiden und jedes Ergänzungskapitel eindeutig verorten. Anlagenbereichsprüfung gehört vor ersten Betrieb in diesem Bereich; 60974 bleibt ein separater späterer Auftrag.

### R-13 - Anschlussstand E: Erststrom-Voraussetzungen und spätere Abnahme trennen

**Status: Bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 52 fordert vor dem ersten Einschalten alle Felder, enthält jedoch Inbetriebnahme 52–56, Lastprüfung 57–59, Gehäuseabnahme und Lautsprecherprüfung einschließlich Soundtest. Diese Ergebnisse können vor dem jeweiligen Funktionstest noch nicht vorliegen.

**Korrekturauftrag:** E in zeitlich eindeutige Karten aufteilen: E1 vor dem ersten Einschalten des umgebauten Kopfes; E2 nach offenen Funktionstests; E3 nach Last- und geschlossenem Gehäusetest. G0-Prüfaufnahmen ausdrücklich vom ersten Einschalten im Fahrzeug unterscheiden. Bei E1 dürfen notwendige zukünftige Ergebnisfelder nicht als schon auszufüllende Sperre erscheinen.

**Schließung:** Jede Zeile erhält einen Erfüllungszeitpunkt und verweist auf den genauen Nachweis. Ein übersprungenes Prüftor darf nicht zur normalen Arbeitsweise werden. Die vorgeschlagene Teilung ist eine redaktionelle Reparatur, keine Aufhebung der offenen elektrischen Freigaben.

### R-14 - Erstes Einschalten: örtliche Trennregel und Dummy-Vorprüfung

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 23 fordert vor dem Einsetzen abgetrennte Versorgung; S. 42 Schritt 52 verweist darauf, formuliert aber zuerst „aufstellen“ und dann „einsetzen“. Das ist lokal missverständlich, keine ausdrückliche Erlaubnis zum Stecken unter Spannung. Für den hinteren Kopf fehlt eine gleichwertig konkret beschriebene erste Einzelprüfung vor dem gemeinsamen Fahrgleistest.

**Korrekturauftrag:** Vor jedem Einsetzen ausdrücklich: STOP, Kopf vom Gleis nehmen, sämtliche Verbindungen/Puffer getrennt, Hilfsleitungen entfernt, freie Enden isoliert; dann Index-/Sitzkontrolle, anschließend geprüfter Einzeltest am getrennten Programmierplatz. Eine Programmiergleisempfehlung ist in der [Märklin-Beilage S. 6](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf) vorhanden; die Eignung für den ESU-Aufbau ist zusätzlich zu prüfen.

**Korrektur des Ersatzes:** CV8-Lesen mit erwarteten 151 ist nur ein ESU-Kommunikationstest. Scheitert es beim motorlosen Kopf, sind Quittierlast, Versorgung und Kontakt gesondert zu prüfen; nicht pauschal „Isolationsfehler“ folgern. Der Programmierausgang ist keine Garantie gegen Decoderschäden und ersetzt R-02 nicht. Beide Köpfe erst nach bestandenem jeweils passendem Einzeltest zusammen prüfen.

### R-15 - Lastprüfung vor Freigabe von Wagenzahl und Fahrbetrieb

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** REV9 S. 44 enthält bereits die Decodergrenzen und verlangt einen gesonderten Kupplungs-/Spannungsabfalltest. S. 34 warnt, dass ein kleiner Ohmwert keine Stromtragfähigkeit beweist. Der Bericht behauptet daher zu viel mit „Kap. 18 ohne Grenzwerte“. Richtig ist: Wagenverbrauch, zulässige Kupplungs-/Leiterbahnlast und exakte Messreihenfolge sind nicht vollständig festgelegt; S. 43 sieht Fahr-/Volllastschritte vor der abschließenden Lastabnahme vor.

**Zurückgenommene Ersatzregeln:** „Last unbekannt → höchstens einen Wagen anschließen“ ist keine belegte Freigabe. „Summe AUX ≤250 mA“ verwechselt die Einzelgrenze mit der Gesamtgrenze.

**Korrekturauftrag:** Für den konkret verwendeten Innenlichtausgang dessen gesamte Last, für jeden weiteren Licht-/AUX-Ausgang seine eigene Last und für den 60977 die Summe aller gleichzeitig aktiven Licht-/AUX-Lasten bestimmen. Herstellerwerte: verstärkter AUX1–4-Ausgang jeweils höchstens 250 mA; Licht+AUX zusammen höchstens 300 mA; Motordauerlast höchstens 1,1 A; Gesamtlast höchstens 1,6 A. Maßgeblich bleiben zusätzlich niedrigere Grenzen von Steckkontakt, Leitung, Kupplung und Platine. [Märklin-Beilage S. 3](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf)

Die hinteren LEDs am 59649 gehören nicht zur 60977-AUX-Summe; ihre Versorgung kann trotzdem den gemeinsamen RT-Strom beeinflussen. Einschaltspitzen, höchste geplante Helligkeit und alleinige hintere Einspeisung berücksichtigen. Lasttest mit vorab festgelegtem, begrenztem Fachprüfaufbau schrittweise durchführen; erst danach die betreffende Wagenzahl/Fahrt freigeben. Keine garantiert zulässige Wagenzahl aus einem Multimeterwert errechnen.

### R-16 - Physische Lichtausgänge in G0 protokollieren

**Status: Bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 28 beruft sich auf ein in G0 geprüftes LV/LR-Mapping. C4/C8 auf S. 7 nennt das Folgen der Richtung, protokolliert jedoch nicht eindeutig den jeweils tatsächlich aktiven physischen Ausgang.

**Korrekturauftrag:** Für Master und Slave getrennt bei Fahrstufe 0 dokumentieren: F0 aus, vorwärts mit F0 an, rückwärts mit F0 an; jeweils LV/LR aktiv oder inaktiv. Die in REV9 angenommene Zuordnung lautet für beide Decoder vorwärts LV und rückwärts LR. Vorn wird daran Weiß/Rot angeschlossen, hinten Rot/Weiß. „Motortriebkopf voraus“ als Referenzrichtung ausdrücklich festlegen.

**Schließung:** Reale Ausgänge am geeigneten Prüfaufbau beobachten, keine Brücke oder improvisierte Prüflast anschließen. Abweichendes Mapping entweder vor der Verdrahtung geprüft korrigieren oder den gesamten Anschlussplan konsistent ändern. Eine Fahrtrichtung allein aus Bildschirm-Pfeilen ist kein Nachweis der späteren Zugrichtung.

### R-17 - Nachprogrammierung nur am getrennten Decoder

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 26/39 fordert spätere ESU-Änderungen, ohne dort die physische Trennung erneut auszuschreiben. F.7 S. 62 enthält diese Regel bereits ausdrücklich: DCC-Servicebefehle wählen nicht anhand des Loklisteneintrags einen Decoder aus.

**Korrekturauftrag:** An jeder solchen Änderungsstelle ergänzen: gesamten Zug stromlos machen, Dummy vom Wagenbus und vom anderen Kopf trennen; nur den bestätigten ESU-Prüfaufbau am räumlich und elektrisch getrennten Programmiergleis verwenden. Puffer bleiben abgetrennt. Kommunikationsfähigkeit nach R-09 bestätigen. Die Auswahl einer anderen DCC-Adresse in der CS3 ersetzt die Trennung nicht. Nach der Änderung betroffene Licht-/Synchronisationsprüfungen erneut durchführen.

**Schließung:** Lokale Verweise plus nachvollziehbares Einzeldecoderprotokoll; keine neue pauschale CV-Schreibfolge.

### R-18 - Dummy-Stützen: falschen Verweis auf LoDi-Ringprüfung ersetzen

**Status: Bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 49 Nr. 2/3 empfiehlt das Auflegen der neuen Platine auf den hohen Stützen und verweist auf Schritt 23. S. 30 sagt dagegen, die alten Stützen seien keine bestätigte Aufnahme für den kleinen Märklin-Träger und die LoDi-Ringprüfung gelte dort nicht.

**Ersatz:** „Diese Stützen trugen die alte Platine. Für den neuen Märklin-Träger sind sie keine bestätigte Aufnahme. Keine Montage allein nach diesem Vergleichsfoto; konkrete Befestigung nach Kapitel 12c nachweisen.“

**Korrektur gegenüber dem Bericht:** Nicht „keine Aufnahme“ oder „unpassend“ schreiben: Fehlende Freigabe beweist keine mechanische Unbrauchbarkeit. Benötigt werden reale Befestigung, Unterseitenabstand, Schraubenlänge und Prüfung möglicher Kontakte.

### R-19 - Wiederanschluss und endgültiger Gehäuseschluss

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 50 verlangt nach dem passiven geschlossenen Test erneutes Öffnen, Entfernen aller Hilfsleitungen, Wiederherstellung der Anschlüsse und spannungsloses Einsetzen. Es fehlt die ausdrückliche vollständige Nachprüfung der dabei wiederhergestellten Verbindungen; der tatsächliche Freiraumnachweis mit Decoder bleibt methodisch offen.

**Korrekturauftrag:** Nach jedem Wiederanschluss alle davon betroffenen Soll-/Fremdpfade mit gültigen positiven Kontrollen erneut prüfen. Nicht nur „das eine 16c-Messpaar“ abhaken. Wenn Nachlöten oder Leitungsumlegen die geschlossene Lage beeinflusst, die einschlägige Gehäuseprüfung wiederholen. Hilfsleitungen vollständig entfernen und endgültige Lage dokumentieren.

**Zurückgenommen:** „Seitlich Abstand ansehen“ ist allein kein Nachweis für einen verdeckten Dachkontakt. Keinen beliebigen Isolierstoff oder Schraubenersatz freigeben. Abstand, Halter, geeignetes Isoliermaterial und Wärmeabfuhr am realen Einbau bestimmen; Decoder nicht einwickeln. Nach kontrolliertem spannungslosem Schließen Funktion im geschlossenen Zustand prüfen. Eine bestandene Prüfung ohne eingesteckten Decoder beweist nicht dessen mechanischen Platzbedarf.

### R-20 - Mehrdeutige Bezeichnungen vereinheitlichen

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 34 verwendet Ende A/B und zugleich L/O/B-Pads. Andere Kapitel benutzen B, R4, M1 und K1 für weitere Dinge. Das ist unnötig fehleranfällig.

**Korrektur:** Die konkrete Fehlerkette „Benutzer misst deshalb am falschen B-Pad und übersieht einen Kurzschluss“ ist eine Hypothese. W1 fordert bereits positive und stabile Durchleitungen; diese Gegenprobe darf im Bericht nicht verschwinden.

**Korrekturauftrag:** Wagenenden Ende 1/Ende 2 nennen; Pads immer als „Pad B“, „Pad O“, „Pad L“; R4 als „Bauteil R4“ oder „Prüfschritt 12c-4“ unterscheiden. Einsetzschritte mit Kapitelpräfix, Motoranschlüsse mit M1/M2 bezeichnen. „Prüfleitungsenden“ statt mehrdeutig „Prüfenden“ verwenden. Keine elektrische Funktion allein wegen einer neuen Benennung ändern.

### R-21 - Wiederholungsprüfung nach Umreihen und Änderungen

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 46 verlangt bereits erneute Prüfung nach Änderungen an Kupplungsverdrahtung; S. 33 behandelt zwei sich gegenseitig verdeckende Kreuzungen. Vollständig fehlende Wiederholpflicht ist daher widerlegt. Eine ausdrückliche Regel für Drehen, Umreihen und Teiletausch fehlt.

**Korrekturauftrag:** Zugreihung und Orientierung dokumentieren. Nach Veränderung vor erneutem Einschalten die betroffenen Kontakt-/Padzuordnungen sowie die neue End-zu-End-Zuordnung prüfen; bei möglicher Fehlpaarung die vorgesehenen Einzelkupplungsprüfungen wiederholen. Nicht aus einem richtigen Gesamt-Durchgang auf jede einzelne Kupplungsstelle schließen.

**Korrektur des Ersatzes:** Der vollständige Zug mit bestückten LoDi-Leisten darf nicht anhand allgemeiner „GE gegen Radmasse nicht niederohmig“-Grenzen freigegeben werden. Messzustand und legitime Bauteilpfade müssen berücksichtigt werden. Eine Vertauschung kann Gleisspannung auf den Schaltpfad bringen; tatsächliche elektrische Folgen und mechanische Drehbarkeit sind am Aufbau offen. „Im Zwischenabschnitt falsch zugeordnet“ ist präziser als ein pauschales „Wagen verpolt“.

### R-22 - Norm-Pinrollen sind nicht automatisch gemessene LoDi-Leiterbahnen

**Status: Offen. Ausgangspriorität: P2.**

**Beleg:** RCN-121 Tabelle 1 unterscheidet Gleisaufnahme 21/22, GND 20, U+ 16, interne Vcc 12, AUX4 4 und AUX1 15. LoDi veröffentlicht Pads und eine revisionsabhängige Jumperfunktion. Das ist mehr als eine bloße geratene Beschriftung, aber kein vollständiger Schaltplan des Nutzerexemplars. [RCN-121](https://normen.railcommunity.de/RCN-121.pdf)

**Korrekturauftrag:** Für die tatsächliche LoDi-511-Revision die Netzzuteilung von MASSE, SW/RT, Front-VCC, Motor, LS1/LS2 und GE bestätigen. Dabei unterscheiden, ob eine Verbindung direkt oder über Bauteile verläuft. V1.49 nicht unbesehen nach der SJ1/SJ2-Regel ab V1.50 bewerten.

**Zurückgenommen:** Eine pauschale Prüfanweisung „leere LoDi → alle genannten Paare niederohmig“ ist nicht belegt. Decoderlos heißt weiterhin bestückt. Die Norm bestimmt Kontaktfunktionen, nicht die konkrete Leiterbahnführung. Feine 21MTC-Pins ohne festgelegte Indexansicht und geeignete kontaktierende Prüfvorrichtung sind kein freigegebenes Anfänger-Messfeld. Schließen durch Herstellerzuordnung oder fachkundig dokumentierte revisionsbezogene Netzprüfung.

### R-23 - Schwarze Fläche im Steckbereich: keine ungeklärte Kappe entfernen

**Status: Offen. Ausgangspriorität: P2.**

**Bildbeleg:** Auf S. 18 ist eine schwarze Fläche im mittleren Steckbereich sichtbar. Das Foto beweist nicht sicher, dass es sich um eine abnehmbare Bestückungskappe handelt. Die Indexlücke ist darauf nicht zuverlässig beurteilt.

**Gegenbeleg zur behaupteten Schutzlücke:** S. 23 sperrt das Einsetzen bereits ausdrücklich, wenn die Indexfehlstelle nicht erkennbar oder die Lage nicht druckfrei passend ist, und verlangt zusätzliche Makrofotos.

**Korrekturauftrag:** Steckleiste und beide Decoderseiten bei ausgeschalteten, getrennten Teilen klar dokumentieren; LoDi identifiziert die schwarze Struktur und gibt gegebenenfalls ein konkretes Abnahmeverfahren vor. Bis dahin weder abhebeln, abziehen noch darauf drücken. „Foto ohne Kappe“ nicht als bereits ausführbaren Auftrag formulieren.

**Schließung:** Tatsächliche Indexlage und mechanischer Sitz müssen am realen Bauteil bestätigt werden. Eine plausible Interpretation des Bildes oder die genormte Steckweise genügt nicht zur Freigabe dieses Exemplars.

### R-24 - ICE-M-Variante und gemeinsamer SW/RT-Pfad

**Status: Offen. Ausgangspriorität: P2.**

**Beleg:** Das Relaisfeld erscheint auf S. 18 unbestückt. Daraus folgt nicht die vollständige Bestückungsvariante oder der direkte Strompfad zwischen SW und RT.

**Korrekturauftrag:** Artikel/Revision und vorgesehene Durchverbindung ohne Schleiferumschaltung bestätigen lassen; fachkundige Messung mit festgelegter Topologie dokumentieren. Eine einzelne statische Durchgangsanzeige ersetzt die Variantenbestimmung nicht. Keine Brücke setzen, um den Sollzustand zu erzwingen.

**Korrektur der Folgebehauptung:** Ein nicht durchverbundener SW/RT-Pfad macht den Dummy nicht zwangsläufig stromlos, wenn dieser einen eigenen funktionsfähigen Schleifer hat. Er widerlegt jedoch die angenommene gemeinsame Einspeisung und damit Redundanz-/Lastannahmen. Bei abweichender Variante sind auch AUX-Zuordnung und Umschaltfunktionen separat neu zu prüfen; die S-Variante ist keine automatisch passende Austauschlösung.

### R-25 - Decoderadresse, Serviceeintrag und aktive Protokolle getrennt behandeln

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** F.4/F.7 unterscheidet DCC-Serviceprogrammierung von mfx-Fahrbetrieb. Ein Inventar der wirklich aktiven DCC-/MM-Adressen und Protokolle fehlt jedoch.

**Korrektur:** Einen CS3-Serviceeintrag löschen oder umadressieren verändert nicht automatisch die im Decoder gespeicherte Adresse. Das ist kein ausreichender Schutz vor späteren Adresskollisionen. Beim beschriebenen DCC-Serviceverfahren selektiert die eingestellte Lokadresse ohnehin nicht den Empfänger.

**Korrekturauftrag:** Für beide Decoder die tatsächlich ausgelesenen Adressen und aktiven Protokolle dokumentieren und mit dem Anlagenbestand abgleichen. Wartungseintrag eindeutig getrennt vom Fahrbetrieb behandeln. Änderungen an Decoderadressen oder Protokollen nur mit Einzeldecoder- und Rückleseplan; der gewählte DCC-Wartungsweg darf nicht versehentlich abgeschaltet werden. mfx-Priorität kann bestimmte Kollisionen vermeiden, ersetzt aber kein dokumentiertes Konfigurationskonzept.

### R-26 - Schnellanleitung: Wagen zuerst prüfen, dann anschließen

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 68 Schritt 6 nennt die Lötzuordnung vor den Prüfverweisen. Der Seitenkopf verlangt zwar zuerst die Detailkarte; die Reihenfolge im Kurzschritt bleibt verbesserungsbedürftig.

**Korrigierter Ersatz:** „Je Wagen zuerst Passung prüfen; Ausgangswerte der unverdrahteten Leiste nach 14b-W1 sichern; jeden Kontakt samt freier Litze nach 14b-W2 identifizieren; zusammengesteckte passive Kupplungspaare nach 14a prüfen. Optionalen Radkontakt nach 14c–14e mit abgetrennten Kupplungslitzen prüfen/anschließen. Erst danach RT an O und GE an L; anschließend Kontakt-/Padzuordnung und Vorher-/Nachhervergleich W4/W5.“

**Zusatzkorrektur am Bericht:** „Litzen einzeln nach 14a“ ist ungenau: 14a prüft Kupplungspaare mit vier freien Enden; die Einzelzuordnung steht in W2. Bestehende Elektronik nicht durch beliebige Offenwertforderungen beschädigen oder verändern.

### R-27 - Schnellanleitung: Trennzustand unmittelbar vor 60977-Einsetzen

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 69 Schritt 8 verweist auf 9c; dessen M1 verlangt getrennte Versorgung. Im Kurzschritt fehlen der physische Handgriff, Hilfsleitungsentfernung und vollständige Endisolierung.

**Ersatz:** „STOP; Kopf vom Gleis nehmen; Versorgungen, Puffer und übrigen Zug physisch trennen. Hilfsprüfleitungen entfernen und alle freien Anschluss-/Kupplungsenden einzeln sichern. Vor-Erststrom-Karte bestanden? Erst dann 60977 nach 9c einsetzen und nach dem geprüften Einzeltestplan aufstellen.“

**Schließung:** Einsetzen unter Spannung ist durch REV9 nicht erlaubt. Die Wiederholung am Arbeitsort soll Fehlbedienung verhindern. Bei späterer Richtungskorrektur die Regeln aus R-32 verwenden; kein Eingriff am bestromten Motor.

### R-28 - Schnellanleitung: Abschluss nach passiver Gehäuseprüfung

**Status: Teilweise bestätigt. Ausgangspriorität: P2.**

**Beleg:** S. 69 Schritt 11 lässt das erneute Öffnen und Entfernen der Hilfsleitungen aus; die verlinkte Vollfassung S. 50 Schritt 6 enthält beides.

**Korrekturauftrag:** Kurzschritt ergänzen: nach passiver geschlossener Prüfung wieder öffnen; alle Hilfsleitungen entfernen; nur die vorgesehenen Anschlüsse wiederherstellen; sämtliche durch Wiederanschluss betroffenen Prüfungen wiederholen. Decoder spannungslos einsetzen, tatsächlichen Freiraum bestätigen, kontrolliert spannungslos schließen; abschließend geschlossenen Funktionstest durchführen.

**Grenze:** „Litzenlage wie im Passivtest“ ist eine Hilfe, kein Ersatz für die Nachprüfung nach Nachlöten oder Umlegen. R-19 gilt vollständig. Die Vollfassung wird nicht fälschlich als frei von diesen Schutzregeln beschrieben.

### R-29 - Seiten-, Kapitel- und Schrittnummern unterscheiden

**Status: Bestätigt. Ausgangspriorität: P3.**

**Beleg:** Formulierungen wie „vor 52/54“ (S. 2), „in 42–44“ (S. 38) und „nach 60/24“ (S. 26) sind unnötig mehrdeutig.

**Korrekturauftrag:** Durchgehend „Schritt 52“, „Kapitel 24“ und „PDF-S. 50“ schreiben; Kurzschritte mit G.1/G.2 präzisieren. „Schritte 1–6“ auf S. 69 ist im unmittelbaren Kontext verständlich, kann aber zu „G.1, Schritte 1–6“ verbessert werden. Verweise nach jeder Umnummerierung automatisch und inhaltlich kontrollieren.

### R-30 - Schwarze Messleitung: Widerspruch im Begleitsatz

**Status: Bestätigt. Ausgangspriorität: P3.**

**Beleg:** S. 14 Schritt 15 nennt PX „ausschließlich“ für Messungen 3/4, während die Tabelle auf S. 15 PX auch in 1/5 verwendet.

**Ersatz:** „Die Fahrzeugclips bleiben unverändert. Schwarz liegt in den Zeilen 1, 3, 4 und 5 an PX; in den Zeilen 2 und 6 an PM2. Nur die freien Hilfsleitungsenden nach Tabelle umstecken.“

**Schließung:** Begleitsatz korrigieren, nicht die bereits richtige sechszeilige Vor-/Isolations-/Nachprüfungsfolge ändern. Diese echte redaktionelle Kollision relativiert das pauschale Lob ‚Motorprüfung vorbildlich‘, hebt ihre grundsätzlich sinnvollen Kontaktkontrollen aber nicht auf.

### R-31 - Motorlitzen: kumulative Voraussetzungen einheitlich formulieren

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Beleg:** S. 12/13/16 nennt „bis Ende 6b“, „nach 6b/9a“ und „nach G1/G2“. Das sind unterschiedlich genaue, teilweise kumulative Bedingungen, nicht zwingend drei konkurrierende Freigaben.

**Ersatz:** „Motorlitzen erst an MOT_L/MOT_R anlöten, wenn die vollständige Motor-/Leitungsprüfung nach 6b bestanden und die revisionsbezogene Padzuordnung nach 9a geklärt ist; Decoder bleibt abgezogen.“

**Schließung:** Mit dem überarbeiteten Gate-Plan R-12 abgleichen. Keine Bedingung verwenden, die wiederum bereits denselben Lötanschluss voraussetzt.

### R-32 - Falsche Motorlaufrichtung: Korrektur mit erneuter Prüfung

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Beleg:** S. 42 Schritt 53 verweist zur Richtungskorrektur auf 9a, nennt lokal aber keine Wiederholungsprüfung. Globale Stromlosregeln sind vorhanden.

**Korrekturauftrag:** Für die festgelegte Anschluss-/Mappingvariante bei falscher Motorzuordnung: STOP, vom Gleis nehmen, alles physisch trennen, Decoder abziehen; erst dann bestätigte Motoranschlusszuordnung korrigieren. Danach vollständige betroffene Motor-/Leitungsprüfung samt positiven Kontrollen wiederholen und Richtung neu abnehmen.

**Korrektur am Bericht:** „Nie CV29, weil der Slave sonst nicht mitdreht“ nicht als allgemeingültige Decoderregel darstellen. Hier soll ein Verdrahtungsfehler nicht durch zusätzliche, ungeprüfte Invertierungen verdeckt werden; das genügt als Begründung.

### R-33 - Ungekuppelten Dummy nicht erneut ‚abkoppeln‘

**Status: Bestätigt. Ausgangspriorität: P3.**

**Beleg:** Schritt 54 auf S. 42 prüft ungekuppelte Köpfe, Schritt 55 spricht anschließend vom Abkoppeln.

**Ersatz:** „Den motorlosen Kopf bei abgeschalteter und getrennter Versorgung vom Gleis nehmen. Anschließend im unveränderten geprüften Aufbau wieder aufstellen und den Wiederanlauf erneut prüfen.“ Zweck ist eine echte Versorgungsunterbrechung des Kopfes, nicht ein noch nicht vorhandener Kupplungsanschluss.

### R-34 - Widerstandstoleranz: zu schützende Stromgrenze nennen

**Status: Bestätigt. Ausgangspriorität: P3.**

**Beleg:** S. 25 formuliert, die Widerstandstoleranz müsse beim kleinsten Widerstand eingehalten werden.

**Ersatz:** „Die zulässige LED-Stromgrenze muss auch beim kleinsten möglichen Widerstand, also Nennwert abzüglich Toleranz, eingehalten sein.“

**Grenze:** Die Rechenbeispiele sind mathematisch konsistent, aber keine Freigabe eines Vorwiderstands für die noch nicht vollständig identifizierte LoDi-514-Zweigstruktur. Rechenrichtigkeit und reale Bauteileignung getrennt halten.

### R-35 - Kein allgemeiner Kapazitäts-Nulltest als neue Pflicht

**Status: Nicht bestätigt. Ausgangspriorität: P3.**

**Gegenbeleg:** S. 12/15/47 verlangt bereits, beide Kondensatoranschlüsse zu verfolgen, weil ein geladener Massekondensator im Ohmtest offen erscheinen kann. Die Lücke „Ohmtest allein, ergänzende Kontrolle fehlt“ besteht so nicht.

**Zurückgenommen:** „Mit Kapazitätsbereich messen: keine nF-Anzeige“ ist kein gültiges allgemeines Freigabekriterium. Messgerät, Leitungs-/Motoranteile, Auflösung, Restladung und zulässige parasitäre Kapazität sind nicht definiert.

**Korrekturauftrag:** Bestehende Sicht-/Leitungsverfolgung vollständig ausführen. Bei Unklarheit fachkundig diagnostizieren; ein zusätzlicher Kapazitätstest darf erst nach Validierung seines konkreten Aufbaus aufgenommen werden. Kein Kondensator aufgrund einer ungeprüften Zahlenanzeige entfernen oder ergänzen.

### R-36 - Energiespeicher im Wagen-Messzustand ausdrücklich erfassen

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Beleg:** W1 S. 34 erwähnt Speicher nicht ausdrücklich; S. 9 und die ergänzten Wagenkarten verlangen bereits Trennung beziehungsweise sicheren Restspannungszustand. LoDi beschreibt Speicheranschlüsse bei Wagenplatinen; ihre tatsächliche Ausführung/Bestückung am Nutzerexemplar ist nicht durch den Text belegt.

**Korrekturauftrag:** Vor W1 dokumentieren, ob überhaupt ein Energiespeicher angeschlossen ist. Falls ja, nach dem bestätigten Verfahren trennen und Spannungsfreiheit herstellen. Keine Durchgangs-/Widerstandsmessung an geladenem Aufbau. Kein Kurzschließen zum Entladen, keine neue Speicher-Nachrüstung als Nebenauftrag.

**Schließung:** Tatsächliche Platinenrevision, Speicherbestückung und definierter Vorher-/Nachher-Messzustand. Nicht automatisch C1/C2 einer anderen Revision voraussetzen.

### R-37 - CS3: Verhalten beim Hinzufügen einer CV-Zeile

**Status: Offen. Ausgangspriorität: P3.**

**Beleg:** F.4/F.6 S. 59/61 beschreibt das Anlegen einer fehlenden CV-Zeile ohne Änderung des Wertefeldes. Der Ausgangsbericht hat keinen praktischen Nachweis dafür, dass allein das Hinzufügen einen Schreibbefehl auslöst.

**Korrektur:** „Werteänderungen werden sofort geschrieben“ und „das Anlegen einer Zeile schreibt automatisch“ sind verschiedene Behauptungen. Die zweite bleibt offen.

**Korrekturauftrag:** Verhalten der tatsächlichen CS3-Version kontrolliert nachweisen, zunächst ohne schreibgefährdeten Decoder. Vor der Freigabe des CV8-Leseablaufs exakt zwischen Nummernfeld, Wertefeld, Lesen und Vorlage-Schreiben unterscheiden. Kein Reset oder ungeschützter Live-Versuch an der Lok, um die Oberfläche auszuprobieren.

### R-38 - JMRI-Felder belegt; Aktivierungsabbildung weiterhin offen

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Beleg:** Die gepinnte JMRI-Datei enthält tatsächlich CV191/M4MfgId sowie CV192:4/M4SerNo. REV9 S. 56 erklärt den Implementierungsstatus bereits, überschreibt ihn aber mit einem zu endgültigen Titel; S. 64 „schließt die Registerlücke“ ist zu stark. [JMRI, festgelegter Commit, ab Zeile 994](https://github.com/JMRI/JMRI/blob/32eca6cddc18a55f2efdfdbc970cca96b7511827/xml/decoders/esu/v5standardCVs.xml#L994)

**Ersatz:** „In JMRI implementierte Synchronisationsfelder“ und „Die Recherche grenzt die Registerfrage ein; vollständige Aktivierungsabbildung und individuelle Masterübernahme sind noch offen.“

**Zusatzkorrektur am Bericht:** Eine eigene Checkbox in ESUs Oberfläche beweist kein eigenes zusätzliches Aktivierungsregister. Aktivierung könnte auch über vorhandene Feldwerte umgesetzt sein. Ob separates Register, mehrere Parameter oder abgeleiteter Zustand: durch unverfälschten Offline-Differenzexport klären. Keine unbestätigten Zielwerte in die Decoder schreiben.

### R-39 - 60941 und C90: Ableitung offenlegen, keinen falschen Wert behaupten

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Beleg:** Märklin nennt in der Originalbeilage CV52=3 als C90-Motortyp; das ist bestätigt. Der Bericht hat keinen Beleg gefunden, dass die Wahl für den korrekt umgerüsteten 60941 sachlich falsch sei.

**Korrekturauftrag:** Die konkrete Zuordnung zum eingebauten Motor als technische Zuordnung transparent machen und den tatsächlichen 60941-Umbau verifizieren. Bei unklarem Motorzustand fachkundige oder Herstellerbestätigung einholen. Nicht allein wegen fehlender wortgleicher Herstellerformulierung einen neuen Motor, eine andere CV oder eine zwingende kostenpflichtige Dienstleistung verlangen.

**Schließung:** Mechanischer und elektrischer Motorzustand, zutreffender Motortyp und rückgelesene Einstellung; keine automatische Einmessfahrt während dieser Prüfung.

### R-40 - Programmer-Verbot artikelscharf wiederholen

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Beleg:** S. 5 verbietet den ESU 59649 auf Märklin 60971 ausdrücklich. S. 39 „nie beide Decoder am Programmer“ ist lokal unscharf, erlaubt den ESU aber nicht positiv.

**Ersatz:** „Am Märklin 60971 in diesem Auftrag ausschließlich den Märklin 60977 verwenden; 59649 niemals dort aufstecken.“

**Nachweisgrenze:** Herstelleranleitung des 60971 und eigene sichere Montage-/Abziehreihenfolge getrennt belegen. Ein nicht erreichbarer mDecoderTool-Link beweist nicht, dass eine andere Herstellerquelle den Handgriff nicht enthält. Der Bericht soll die Herkunft als Herstellerangabe oder eigene stromlose Arbeitsfolge kennzeichnen, statt unbelegte Unsicherheit als nachgewiesenen Fehler auszugeben.

### R-41 - Schnellanleitung: Reset, Einmessfahrt und Puffer getrennt warnen

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Beleg:** S. 69 verbindet Reset- und Einmesswarnung in einem Absatz. Die ESU-Auslösung ist bereits auf S. 62 vorhanden; die Beschränkung auf höchstens einen späteren 60974 vorn steht auf S. 4/38.

**Korrekturauftrag:** Drei getrennte Regeln in der Kurzfassung: (1) Für diesen Arbeitsplan keine Reset-Schreibbefehle an CV8. (2) Keine Einmessfahrt: beim 60977 nicht 77 in CV7/Firmwarefeld schreiben; beim 59649 keine Kombination CV54=0 mit anschließendem F1. (3) Beide 60974 bleiben jetzt abgetrennt; später höchstens einer am vorderen 60977 nach eigener Anschlussfreigabe.

**Grenze:** Im motorlosen Kopf fehlt zwar der Antrieb für eine Fahrt, eine Motor-Prüfaufnahme kann aber vorhanden sein. Keine der Warnungen erklärt den Pufferanschluss oder eine zukünftige Einmessfahrt als freigegeben.

### R-42 - Quellenmetadaten einzeln korrigieren

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Jetzt widerlegt:** „Märklin-Stand 10/2025 nicht bestätigt“ ist überholt. Die geladene Originaldatei enthält das Impressum 260057/1025/Sc7Ef; CV51 steht auf gedruckter S. 16/21, CV52 auf S. 17/21. Die aktuelle Datei hat 192 PDF-Seiten mit mehreren Sprachfassungen. [Märklin-Original](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf)

**Präzisieren:** CAN-Protokoll 2.0 behandelt System-UID auf S. 8 und Bind UID/SID auf S. 28; S. 19 enthält außerdem den Märklin-UID-Präfix im Fast-Read-Kontext und ist dafür nicht irrelevant. [CAN-Dokument](https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf)

**Ergänzen:** ESU-LokPilot-5-Handbuch: 8. Auflage, Januar 2023, laut Deckblatt ab Firmware 5.3.128; Standardmapping in dieser Ausgabe gedruckt S. 67. Das ist nicht der abgelesene Firmwarestand des Nutzerdecoders.

**Weiter offen:** Nicht konkret nachgewiesene ECoS-/Krauß-Fundstellen einzeln als unbestätigt behandeln. Ein neueres Live-Datum bei einer Norm macht einen korrekt bezeichneten älteren Quellenstand nicht automatisch falsch. Titel, Ausgabe, Seite und tatsächlicher Inhalt müssen gemeinsam stimmen; ein Abruffehler allein ist kein Widerlegungsbeleg.

### R-43 - Bildbeschnitt und Dokumentnavigation

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Visuell bestätigt:** Auf S. 29 sind der obere Warnhinweis und ein Teil des Detailkreises der Herstellerzeichnung abgeschnitten. Dieser Bildrahmen muss beim nächsten PDF-Export korrigiert werden. Die textliche Indexwarnung darunter bleibt vorhanden.

**Weitere redaktionelle Punkte:** S. 55–67 besitzt Seitenzahlen, aber keine REV9-Fußzeile; G.1/G.2 ist im Inhaltsverzeichnis anders eingerückt. Quellen 23/24 stehen hinter den Bildquellen.

**Gegenbeleg:** Eigene Quellennummern für Kapitel F werden auf S. 1/55 ausdrücklich erklärt. Daher kein nachgewiesener unaufgelöster Quellenkonflikt, wohl aber Verbesserungspotenzial durch Präfixe.

**Schließung:** Geänderte Seiten rendern und visuell prüfen; zusätzlich Inhaltsverzeichnis, Quellennummern und alle geänderten Sprungziele regressionsprüfen. Die derzeitigen 89 internen Links sind inhaltlich korrekt; Bildkorrektur und Linkkorrektur nicht verwechseln.

### R-44 - Prüfstatus aus Arbeitskarten in Änderungsvermerk verschieben

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Beleg:** S. 1/51 erwähnt noch einen ausstehenden externen Bericht und frühere 86 Findings. Das dokumentiert eine damalige Nachweisgrenze, ist aber für die Handgriffe störend und inzwischen zu aktualisieren.

**Korrekturauftrag:** In einen datierten Versions-/Prüfstatus verschieben: Welcher Bericht lag tatsächlich vor, welche Datei wurde geprüft, welche Korrekturen sind übernommen und welche Hardwaretests stehen aus? Nicht ersatzlos alle Nachweisgrenzen löschen. Der jetzt geprüfte Bericht enthält 47 R-Befunde; eine vollständige ursprüngliche 86-Finding-Liste liegt damit nicht automatisch vor.

### R-45 - 60941-Kondensator: Lieferumfang nicht aus unvollständiger Liste ableiten

**Status: Offen. Ausgangspriorität: P3.**

**Korrektur des Berichtsarguments:** Eine Sammlerliste ohne separate Kondensatorposition beweist nicht, dass am Motorschild kein Kondensator vormontiert ist. Die Märklin-Beilage ist vollständig abrufbar; auf S. 2 ist am neuen Motorschild, Teil 3, ein scheibenförmiges Bauteil eingezeichnet. Das Bild liefert keinen Wert-/Topologienachweis am Nutzerexemplar. [Märklin 60941/60943](https://static.maerklin.de/damcontent/e3/bb/e3bb202fe80385cc96835d783af5e1821670919973.pdf)

**Korrekturauftrag:** Den tatsächlich vorhandenen/vormontierten Zustand beschreiben. Nur einen eindeutig zwischen den beiden Bürstenanschlüssen liegenden und für diesen Aufbau bestätigten Entstörkondensator als solchen behandeln; beide Anschlüsse verfolgen. Einen nicht vorhandenen oder nicht identifizierten Kondensator nicht aufgrund des Textes eigenmächtig nachrüsten.

**Schließung:** Reales Motorschild und Anschlussverlauf prüfen. Weder „im Satz sicher kein Kondensator“ noch „auf jedem Motorschild derselbe Kondensator“ ist hier nachgewiesen.

### R-46 - Front-VCC und interne Vcc: vorhandene Erklärung lokal schärfen

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Gegenbeleg:** S. 21 benennt das LoDi-Front-VCC bereits als gemeinsames LED-Plus; S. 38 erklärt ausdrücklich den Unterschied zur internen Pin-12-Vcc und die entsprechende Märklin-Bezeichnung +Ub. Ein ungelöster vollständiger Begriffsfehler liegt daher nicht vor.

**Korrekturauftrag:** Direkt in der Anschlusszeile „Front-VCC: gemeinsamer LED-Plus im bestätigten LoDi-Anschlusskonzept“ ergänzen. Normatives Decoder-U+ gehört zu 21MTC-Kontakt 16; diese Normrolle nicht mit einer bereits gemessenen Leiterbahnverbindung des Nutzerexemplars verwechseln. Pin-12-Vcc, +5V, GND und Gleismasse bleiben verschieden.

**Schließung:** Redaktionell eindeutige Benennung plus gegebenenfalls revisionsbezogene Netzprüfung nach R-22. Keine neue SUSI-Abgriffsstelle oder Brücke aus dem Namen VCC ableiten.

### R-47 - Schnellanleitung: zusätzliche Direktverweise, keine vorgetäuschte G0-Freigabe

**Status: Teilweise bestätigt. Ausgangspriorität: P3.**

**Gegenbeleg:** S. 68 nennt G0 ausdrücklich offen und verlangt den Vorabtest. S. 69 ist die Fortsetzung nach bestandenen Schritten 1–6. „Bestätigte M4-Synchronisation erhalten“ ist in diesem Ablauf logisch bedingt; eine vorweggenommene erfolgreiche G0-Prüfung ist nicht nachgewiesen.

**Korrekturauftrag:** Dennoch klarer „Nach tatsächlich bestandenem G0 die geprüfte Synchronisation unverändert lassen“ schreiben. Definition „vorwärts = Motortriebkopf voraus“ in die Lichttabelle aufnehmen. Wichtige Verbote und Links zur Identität, zum Export und zu Netzen/Messgerät direkt erreichbar machen; die vorhandenen Pflichtverweise bleiben gültig.

**Schließung:** Kurzfassung erneut gegen alle Detailkarten lesen, ohne sie als eigenständige Anschlussfreigabe zu vermarkten. Zusätzliche Links sind Bedienkomfort, nicht Ersatz für offene technische Nachweise.


## 4. Anforderungsabdeckung nach dem korrigierten Kenntnisstand

| Nutzerziel | Was das Konzept leisten soll | Was tatsächlich noch nachzuweisen ist |
|---|---|---|
| Ein automatisch gefundener mfx-Zug | 60977 als Master, 59649 folgt seiner Betriebsadresse | Individuelle Identitätsübernahme/Aktivierung, Firmware, G0 einschließlich wirklich anderer SID; nicht als bereits erfüllt markieren |
| Kein zweiter aktiver Zugeintrag, keine Traktion | Keine eigenständige Bedienung des hinteren Decoders im normalen Betrieb | Alte Datenbankeinträge von aktueller Anmeldung unterscheiden; keine DCC-Befehle, die das Ergebnis vortäuschen |
| Sound | Vorhandener 60977 mit geeignetem ICE-Projekt | Bestätigter Lautsprecher/Adapter, realer Sitz, Projekt- und Soundtest |
| Rot/Weiß an beiden Enden sofort bei Richtungsbefehl, auch im Stand | Synchronisation plus gespiegelte Farbzuordnung am hinteren Kopf | Physisches LV/LR-Mapping beider Decoder, LED-Daten, F0-an/aus- und Funktionstastenmatrix am endgültigen Projektstand |
| Vorhandene LoDi-Fronten verwenden | Je Kopf ein passender Fronteinsatz | Reale Zweigstruktur, sichere Strombegrenzung und Halter-/Massefreiheit; keine Beispielwiderstände als freigegebene Bauteile ausgeben |
| Schaltbare Innenbeleuchtung ohne konstruktive Richtungspause | Getrennter, richtungsunabhängiger Schaltpfad statt Versorgung aus abwechselnden Frontlichtausgängen | Revisionsbezogene LoDi-/AUX-Zuordnung, Last und Tests bei F0 an/aus, beiden Richtungen, Neustart und realer Bewegung |
| Keine absolute Flackerzusage | Der Richtungswechsel soll die Versorgung nicht absichtlich unterbrechen | Kontaktstörungen, Schleifer-/Radkontakte und echte Unterbrechungen sind getrennte Probleme. „Absolut flackerfrei“ ist nicht nachgewiesen |
| Originale Märklin-Kupplungen, kein zusätzliches Längskabel | Längsdurchleitung über die Wagenplatinen, kurze Anschlusslitzen | Passende Originalteile für den tatsächlichen 2976 und Stromtragfähigkeit; 33701 ist ein Vergleich, kein mechanischer Vollbeleg |
| Optionale Achskontakte | Örtliche Radstromaufnahme in der bestätigten LoDi-Betriebsart | Passende Feder/Mechanik, reale Rückmeldefähigkeit und Einzelprüfung; keine Gleichsetzung mit Mittelschleifer oder drittem Zugbus |
| Signalhalt mit CS3 | Kontaktmeldung und gezielter Fahr-/Haltebefehl bei unverändertem Gleissignal | Zug-/Richtungszuordnung im Ereignis, Bremsweg, besetzte/übersprungene Kontakte und Neustarts; kein automatischer Identitätsnachweis durch ein Kontaktgleis |
| Zwei Schleifer | Gemeinsam nutzbare Mittelleiteraufnahme im freigegebenen Ein-Kreis-Bereich | Tatsächlicher hinterer Schleifer, SW/RT-Verbindung, Kupplungs-/Leiterbahnlast; keine Erlaubnis zum Überbrücken verschiedener Quellen |
| Spätere Pufferung | Allenfalls gesonderte Ergänzung vorn | Konkreter SUSI-Anschluss an realer LoDi-Revision, Firmware und Nachlauf; kein bereits freigegebener Anschluss und keine automatische Wagenpufferung |

Die bestehende Anschlusszuordnung der weißen Wagenplatine wird **nicht umgedreht**. Der namensgleiche Anschluss in einer anderen Betriebsvariante darf nicht unbesehen übertragen werden; maßgeblich ist der dokumentierte Motorplatinenbetrieb. Siehe W-01.

## 5. Abgleich der Verdachtsbefunde W-01 bis W-18

„Widerlegt“ bezieht sich auf den jeweiligen Verdacht, nicht auf eine gesamte Bau-/Betriebsfreigabe.

| ID | Korrigiertes Votum | Beleg und Grenze |
|---|---|---|
| W-01 | Vertauschungsverdacht widerlegt | LoDi unterscheidet die ursprüngliche Wagenverdrahtung von der Motorplatinen-Betriebsart. Für letztere ist die REV9-Zuordnung korrekt. Keine vorsorgliche O/B-Umverdrahtung. [LoDi-Wagenanleitung](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-wib-ice-m/) |
| W-02 | Verdacht invertiertes CV51-Bit widerlegt | Märklin belegt AUX4: Bit 4 = 0 verstärkter, = 1 logischer Ausgang. Übrige Bits unverändert erhalten. [mSD3-Original, S. 16/21](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf) |
| W-03 | Warnung zur Märklin-Einmessfahrt bestätigt | 77 aktiviert den Vorgang, ein nachfolgender Fahrbefehl startet ihn. Kein sofortiger Bewegungsnachweis allein aus dem Lesen von CV7. Original S. 7. |
| W-04 | CV52=3 bezeichnet C90 | Belegt auf S. 17/21. Konkrete Motorzuordnung bleibt von realem Umbau abhängig, siehe R-39. |
| W-05 | Genannte Decodergrenzen belegt | Original S. 3; keine Kupplungs- oder Wagenfreigabe daraus ableiten. Siehe R-15. |
| W-06 | Genannte 60977-Werksfunktionen belegt | Original S. 13: F1 AUX1/Führerstandslicht, F4 ABV aus, F6 AUX4. Der reale Soundprojektstand kann abweichen. |
| W-07 | 60974-Grundanschluss und Firmwareforderung belegt | SUSI, mSD3 ab 3.2.0.1, kein Hintereinanderschalten mehrerer 60974. Daraus folgt kein konkreter LoDi-Abgriff. [60974-Anleitung](https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf) |
| W-08 | Normative SUSI-Zuordnung belegt | classicSUSI GND/Daten/Takt/Plus entspricht 21MTC 20/6/5/16. Orientierung des wirklichen Steckers separat prüfen. [RCN-600 S. 3/4](https://normen.railcommunity.de/RCN-600.pdf), [RCN-121](https://normen.railcommunity.de/RCN-121.pdf) |
| W-09 | JMRI-Felder existieren; Wirkung nicht vollständig bewiesen | Gepinnte Datei enthält 191 und 192:4. Die Implementierungsdeutung ist nicht automatisch eine freigegebene Hersteller-Schreibfolge für 60977/59649. Die gesamte historische Java-/Commit-Kette wurde in diesem Lauf nicht erneut vollständig ausgeführt. |
| W-10 | Kein Rechenfehler in den geprüften Beispielen | S. 25: 21/0,003=7000 Ω; 22/0,003≈7333 Ω; bei 7425 Ω etwa 2,83/2,96 mA und 0,060/0,065 W. S. 26: 7500/2200≈3,41; S. 41: Bit-4-Löschen aus 24 ergibt 8; S. 56: 0x12345678 zerlegt in 120/86/52/18. Keine reale LED-Freigabe. |
| W-11 | Kein logischer Farbtauschfehler unter dem festgelegten Mapping | Hinterer Kopf bewusst Rot an LV, Weiß an LR. Erst reale Ausgangszuordnung prüfen; danach optisch abnehmen. |
| W-12 | Falsche Stecklage nicht nachgewiesen | Normative kompakte Buchse-oben-Mechanik passt; reale Indexlage/Steckstruktur bleiben offen. R-23 beachten. |
| W-13 | Fehlerhafte interne Sprungziele nicht gefunden | 89 Link-Annotationen korrekt, verteilt auf 67 unterschiedliche Zielseiten; nicht 89 unterschiedliche Zielseiten und nicht die früher genannten 125 Links. |
| W-14 | Veröffentlichte Versionsstände nicht mit Gerätebestand verwechseln | CS3 2.6.2 Build 0 und LokProgrammer 5.2.18 sind durch Herstellerseiten gestützt. NMRA listet ESU 151 und Trix 131. Kein gemessener CS3-/Decoderstand; keine automatische UID-/Masterfeldzuordnung. [CS3-Updates](https://www.marklin.nl/service/downloads/cs3-updates), [ESU-Software](https://www.esu.eu/download/software/lokprogrammer/), [NMRA Appendix A, Revision 17.08.2026](https://www.nmra.org/sites/default/files/standards/sandrp/DCC/S/appendix_a_s-9_2_2.pdf) |
| W-15 | Erfahrungsbericht existiert | MTB-Ontour, Beitrag 4 vom 26.02.2023, beschreibt mSD3 plus LokPilot V5 M4 als Slave, Einrichtung mit ESU-Programmer. Er nennt keine übertragbare CV-/Firmware-/Artikelkette für genau dieses Paar. K4, kein Herstellerfreigabebeleg. [Originaldiskussion](https://www.stummiforum.de/t212683f5-Umbau-ICE-Maerklin-auf-mSD-DCC.html) |
| W-16 | Veröffentlichte LoDi-Jumperregel bestätigt, reale Revision offen | Herstellerregeln gelten nur für die zugehörige Version/Betriebsart. Keine zusätzliche Freigabe zum Brücken von Widerständen für den hier geplanten LED-Betrieb. R-22/R-24 beachten. |
| W-17 | Blankkupfer-Verdacht fotografisch nicht bestätigt | Aus der hellen Fläche folgt weder blankes Kupfer noch eine elektrische Isolationsfreigabe. Keine Werkstoff-/Netzgarantie aus Bildfarbe. |
| W-18 | G0 wird in der Schnellanleitung nicht als bestanden ausgegeben | S. 68 nennt G0 offen; S. 69 setzt bestandene vorhergehende Schritte voraus. R-47 ist überwiegend eine Klarheitsverbesserung. |

## 6. Korrigierte Reihenfolge für die nächste Überarbeitung

Die nächste Welle darf nicht nur einzelne Fehlertexte austauschen. Neue Messkarten verändern die Übergänge zu Erststrom, Nachprogrammierung und Gehäuseabschluss.

1. **Prüfbericht als korrigierte Basis festlegen.** Die zurückgenommenen Ersatzregeln nicht übernehmen. Status und Ausgangspriorität getrennt halten.
2. **G0-Voraussetzungen konkretisieren, parallel zu gefahrloser Bestandsaufnahme.** Vorhandene Mobile-Station-/Gleisbox-Artikel, geeignete Prüfaufnahmen, Firmware-/SID-Zugang und Offline-Export klären. Nicht automatisch neue Geräte kaufen. Weiterhin keine Zugdemontage zur Erfüllung einer widersprüchlichen Fotoliste.
3. **Zeitliche Freigabelogik reparieren.** Lose Bauteilidentifikation, Motor-/Montagearbeiten, G0-Testaufnahme und endgültiger Einsetzzeitpunkt sauber trennen; E in Vorbedingungen und Ergebnisabnahme aufteilen.
4. **Elektrische Handgriffe ausarbeiten.** R-02/R-03/R-04/R-14 mit tatsächlichen Pad-, Halter- und Messzuständen schließen. Passive Leitungsprüfung und bestückte Elektronik strikt getrennt halten.
5. **Last-/Gehäuse- und Nachprogrammierungsübergänge ordnen.** Lastgrenzen vor zulässiger Wagenzahl/Fahrt bewerten; Wiederherstellen einer Verbindung verlangt erneute Prüfung; Lichtmatrix am endgültigen Projektstand prüfen.
6. **Anlagenfreigabe auf den befahrenen Bereich begrenzen.** Für erste Prüfungen ein getrenntes Tischgleis. Später jede zusätzliche Strecke und die CS3-Signalautomatik gesondert abnehmen. Puffer bleiben außerhalb dieser ersten Freigabe.
7. **Vollfassung und Kurzfassung gemeinsam regressionsprüfen.** Nicht nur die geänderten Seiten: auch Verweise, Tabellen, Vorbedingungen, Mess-/Schreibzustände, Protokollfelder und Rückfallwege. Danach PDF rendern und Bildbeschnitt/Navigation kontrollieren.

**Korrektur der ursprünglichen Empfehlung:** „Wellen 1/2 umsetzen und nur diese Seiten erneut prüfen“ reicht bei verschobenen Freigaben nicht. Ebenso hängt G0 nicht allein an R-11.

## 7. Noch benötigte reale Daten - ohne verfrühten Bauauftrag

| Nachweis | Jetzt zulässige Vorbereitung | Was dadurch noch nicht bewiesen ist |
|---|---|---|
| Mobile Station/Gleisbox | Artikelnummern, Netzteil und echte Softwarestände ablesen; bisherige Nutzung dokumentieren | Unabhängiger Betrieb, neue SID und erfolgreicher C7-Test |
| Rote LoDi 511 | Lose, spannungsfreie Platine beidseitig fotografieren; Revision, Pads, Jumper und Steckstruktur dokumentieren; nichts an unbekannter schwarzer Struktur abnehmen | Leiterbahnwege, Stromtragfähigkeit oder konkrete Decoderlage |
| Motorloser 2976-Kopf | Zuerst zugängliche Unterseite/Schleifer ohne Zerlegung dokumentieren; weitergehende Öffnung erst nach passend korrigiertem Gate-Plan | Elektrische Verbindung Schleifer/Radkontakt/Träger |
| LoDi-514-Fronten und Träger | Lose Teile beidseitig fotografieren, Beschriftung/Maße erfassen | Reale LED-Ströme, Uf-Minimum, zulässiges If oder Massefreiheit nach Montage |
| Messgerät | Hersteller, Modell, verfügbare Bereiche und Anleitung erfassen | Eignung eines beliebigen Dioden-/Kapazitätsbereichs für bestückte Elektronik |
| LED-/Wagenlast | Herstellerdaten zu tatsächlicher Revision oder festgelegter Fachmessung anfordern | Beliebige Wagenzahl oder absolute Flackerfreiheit |
| Decoderidentität/Export | Eindeutig zugeordnetes Backup/Ausleseprotokoll und unbearbeiteten Offline-Differenzexport sichern | Aktivierung des realen Paars ohne anschließenden G0-Funktionstest |
| Anlage | Beabsichtigten ersten Fahrbereich, Quellen und elektrische Abschnittsgrenzen aufzeichnen | Zuverlässiger automatischer Signalhalt oder Zugidentifikation |

Keine Wagenzahl wird aus einem fremden Foto oder einem anderen ICE-Projekt übernommen. Keine Herstelleranfrage wurde in diesem Auftrag versendet und keine Antwort erfunden.

## 8. Quellenstatus und nachvollziehbare Belege

Die relevanten Aussagen sind unmittelbar bei den Befunden verlinkt. Zu unterscheiden sind erfolgreich gelesene Herstellerunterlagen, Interpretationen, Erfahrungsberichte und weiterhin offene Punkte.

**Neu gesicherte lokale Originalquellen im Unterordner Pruefnachweise/REV9_Berichtsabgleich:**

- Märklin 60977, offizielles 192-seitiges Sammel-PDF: Originaldatei und Textauszug. Der vorherige Webabruf scheiterte an der Dateigröße, nicht an fehlendem Inhalt. Direktdownload vom gleichen offiziellen Link erfolgreich.
- Märklin 60941/60943: vollständige zweiseitige Beilage und Prüfrender von S. 2.
- Märklin CAN-Protokoll 2.0: Original-PDF und Text.
- JMRI v5standardCVs.xml: festgelegter Commit 32eca6cddc18a55f2efdfdbc970cca96b7511827.

Zusätzlich wurden die relevanten LoDi-Seiten, ESU-Synchronisations-/Exportunterlagen, LokPilot-5-Handbuch, MS2-Anleitung, RCN-121/600, 60974-Anleitung, NMRA-Herstellerliste und der konkrete K4-Erfahrungsbeitrag abgeglichen. Für dynamische Softwarestände gilt Abrufdatum 10.09.2026, nicht ein behaupteter installierter Stand.

Nicht erneut vollständig geklärte ältere Spezialfundstellen - insbesondere einzelne Krauß-/ECoS-/mDecoderTool- und weitere historische Quellenketten - tragen keine neue technische Freigabe. Ein nicht gefundener oder nicht vollständig gelesener Beleg wird nicht zu „widerlegt“ umetikettiert. Das Originalquellenverzeichnis bleibt im unveränderten Ausgangsbericht erhalten.

## 9. Schlussbewertung

**Der Prüfbericht ist in dieser Fassung berichtsseitig korrigiert und für die weitere Dokumentüberarbeitung nutzbar.** Alle 47 R-IDs bleiben nachvollziehbar; die W-Bewertungen sind präzisiert. Wertvolle Sicherheitskritik wurde erhalten, überzogene Negativbehauptungen und ungeprüfte Ersatzanweisungen wurden entfernt oder ausdrücklich als offen begrenzt.

**Der ICE-Umbau selbst ist damit nicht freigegeben.** Die 69-seitige REV9 wurde nicht geändert, G0 nicht ausgeführt und kein elektrischer Nachweis am Modell erbracht. Der nächste sinnvolle Auftrag ist die konsistente Überarbeitung der gesamten Freigabe-/Mess-/Inbetriebnahmekette anhand dieser Korrekturen, parallel zur realen Identifikation des vorhandenen Prüfbestands.

