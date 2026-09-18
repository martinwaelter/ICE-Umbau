# ICE 2976 – Originalplatine 62762 erhalten und LokPilot 5 Fx prüfen

**REV18 · 18.09.2026 · Elektrischer Arbeitsentwurf, keine bestätigte vollständige Leiterbahn-Netzliste.**

## Auftrag und Stand

Der Nutzer möchte die lange Originalplatine 62762 nicht nur als Halter, sondern als elektrischen Verteiler weiterverwenden, vorhandene Lampenleitungen für die LoDi-514-LED nutzen und einen Plan einschließlich Masse, Kontaktstellen und Trennungen erhalten. Zusätzlich soll geprüft werden, ob ein ESU LokPilot Fx einen sanften Lichtwechsel ohne Händler oder spezielles Programmiergerät übernehmen kann.

Der eingebaute Richtungsschalter bleibt der Grundweg. Der Nutzer hat Grau gegen Fahrgestell bei Nase voraus und Gelb gegen Fahrgestell bei Kupplung voraus gemessen. Braun ist bislang nur als gemeinsamer Masseanschluss vermutet. Die offenen Gegenstellungen und der dauerhafte Braun-/Radkontakt sind noch zu bestätigen. Dieser Stand ersetzt keine am Fahrzeug durchgeführte Abnahme. [Q1]

Es wurde kein zweiter Decoder zum Einbau freigegeben. Der 60941 und 60972 bleiben im motorisierten Kopf, ohne Sound. Die nachstehenden Schaltungen betreffen den motorlosen Kopf. Der Gesamtzug erhält keine neue elektrische Durchleitung. U/O und vorhandene Wagenversorgung werden nicht auf Verdacht abgetrennt.

## 1. Die 62762 kann elektrisch weiterverwendet werden

Der vorhandene Bildbefund beschreibt die 62762 als passiven Verbindungsträger mit mechanischem U/O-Schalter, nicht als fertigen LED-Treiber. Vorhandene Versorgungs- und Massebahnen dürfen nach Zuordnung ihre bisherige Funktion behalten. Zusätzliche Widerstände und Dioden können isoliert auf derselben Platine befestigt werden. Eine zusätzliche LoDi-Trägerplatine ist dafür nicht nötig. [Q1, Q2]

Die zwei Anschlüsse der bisherigen einzelnen Glühlampe sind dagegen kein unverändert ausreichender Anschluss für die drei Anschlüsse VCC, white und red des vorgesehenen ICE-1-Frontmoduls. Insbesondere darf ein umgenutzter Farbanschluss nicht weiterhin dauerhaft mit Fahrgestellmasse verbunden sein. Die LED-Frontmodule werden ohne Vorwiderstände angeboten. [Q3]

## 2. Funktionale Netze des gesamten motorlosen Kopfes

Diese Namen sind Arbeitsbezeichnungen, keine Hersteller-Padnummern:

| Netz | Funktion |
|---|---|
| U | Örtlicher Mittelschleifer zur Unterleitungsseite der vorhandenen Quellenwahl. |
| O | Pantographen-/Dachkontakt zur Oberleitungsseite. |
| S | Gemeinsamer ausgewählter Ausgang der U/O-Wahl; bisherige Lampeneinspeisung erst durch Messung bestätigen. |
| M | Örtlicher Rückleiter über Radkontakte und leitendes Fahrgestell. Nicht Schutzleiter/Erde und nicht Decoderplus. |
| P | Gleichgerichtete LED-Versorgung nach D0, verbunden mit LoDi VCC. |
| W | LoDi white. |
| R | LoDi red. |
| SW-GRAU | Neue graue Drehgestelllitze, aktiv bei Nase voraus. |
| SW-GELB | Neue gelbe Drehgestelllitze, aktiv bei Kupplung voraus. |

```text
Mittelschleifer ---- U --\
                         U/O-Auswahl ---- S ---- D0 ---- P ---- LoDi VCC
Pantograph -------- O --/

LoDi white ---- RW ---- neue GRAUE Schalterlitze
LoDi red ------ RR ---- neue GELBE Schalterlitze

Radkontakt 0 / M ------ gemeinsamer Schalterkontakt
                       (neue braune Litze erst nach Bestätigung)
```

Zum vollständigen Plan gehören die beiden Schutzdioden DW und DR aus der folgenden Netzliste. Gleiche Netznamen bedeuten dieselbe elektrische Verbindung.

| Bauteil | Anschluss 1 | Anschluss 2 | Orientierung / Wert |
|---|---|---|---|
| D0 | S | P | 1N4148: Anode an S, Kathodenring an P. |
| DW | W | P | 1N4148: Anode an white, Kathodenring an VCC. |
| DR | R | P | 1N4148: Anode an red, Kathodenring an VCC. |
| RW | W | SW-GRAU | Eigener Widerstand, zunächst 47 kOhm / 0,25 W / 5 % oder besser. |
| RR | R | SW-GELB | Eigener Widerstand, zunächst 47 kOhm / 0,25 W / 5 % oder besser. |

DW und DR liegen direkt zwischen dem jeweiligen Farbanschluss und VCC, auf der **LED-Seite** des Widerstands. Sie liegen entgegen der LED-Durchlassrichtung; sie sind nicht parallel zu RW beziehungsweise RR zu schalten. Bei der verwendeten 1N4148 bezeichnet der Ring die Kathode. [Q4]

Die Strombegrenzung bleibt eine eigene stromarme Prüfbestückung. Unter der Auslegungsannahme von höchstens 24 V gilt bei R_min = 47.000 Ohm × 0,95 = 44.650 Ohm: I höchstens 0,538 mA und P_R höchstens 0,013 W, jeweils konservativ ohne LED-/Diodenspannungsabzug. Die reale Versorgung muss diese Annahme erfüllen. 24 V sind kein Sollwert für die Anlage. Es liegt keine bestätigte endgültige LoDi-Zweigstrom-/Helligkeitsauslegung vor. Ein Pufferkondensator ist nicht vorgesehen.

Der Schaltungsentwurf nutzt eine Polarität der Digitalspannung. Er garantiert weder vollständige Flackerfreiheit noch einen sanften Lichtwechsel. Eine Gleichrichterbrücke darf nicht so ergänzt werden, dass ihr Minusausgang und gleichzeitig ein Wechselspannungseingang direkt über das Fahrgestell an M liegen; in einer Polarität entstünde dadurch ein Kurzschlusspfad.

## 3. Rückbaubarer Umbau der alten Lampenverdrahtung

Der folgende Weg nutzt beide alten Lampenlitzen und den bisherigen Versorgungsabgriff. Er braucht keine pauschale Durchtrennung der vorhandenen Versorgungstrassen.

1. Fahrzeug von jeder Versorgung trennen. Alte Lampenleitungen bis zu ihren tatsächlichen Anschlüssen verfolgen und kennzeichnen. U/O-Funktion und Massebezug nach Abschnitt 5 prüfen. Glühlampe entfernen und ihre Anschlussleitungen von der nicht mehr benötigten Fassung lösen.
2. Die **alte gelbe Lampenlitze** von ihrem bisherigen Versorgungsabgriff S lösen. D0 dazwischensetzen: Anode an das erhaltene S-Netz, Kathodenring an die nun mit P gekennzeichnete alte gelbe Litze. Deren Lampenende geht an LoDi VCC. D0 darf nicht durch einen noch bestehenden Kupfer-/Drahtpfad überbrückt werden.
3. Die **alte braune Lampenlitze** von ihrem fahrzeugseitigen dauerhaften Masseanschluss lösen. Dieser Anschluss kann am Fahrgestell liegen und ist nicht automatisch ein Pad auf der 62762. Die Litze als W/white neu kennzeichnen. Ihr Lampenende geht an LoDi white, ihr anderes Ende über RW zur **neuen grauen** Drehgestelllitze. Der ehemalige Masseanschluss selbst bleibt als M erhalten.
4. Eine zusätzliche isolierte Litze für R/red zur LED ergänzen; über RR mit der **neuen gelben** Drehgestelllitze verbinden.
5. DW von W nach P und DR von R nach P entsprechend der Netzliste ergänzen. Die neuen Lötverbindungen isolieren und zugentlastet auf der alten Platine befestigen. Drehgestellschwenkraum und Gehäusefreiheit erhalten.
6. Die **neue braune** Schalterlitze erst nach bestätigter Funktion an einen verifizierten M-Anschluss legen. Nicht an VCC und nicht wegen gleicher Farbe automatisch an irgendeine alte braune Leitung löten.

### Welche Trennungen sind damit vorgesehen?

| Stelle | Maßnahme | Was erhalten bleibt |
|---|---|---|
| Alte Glühlampe/Fassung | Lampenanschlüsse vom neuen LED-Kreis abtrennen. | Lichtleiter und benötigte Halterungen. |
| Alte gelbe Litze am S-Abgriff | Ablöten, D0 in Reihe einfügen. | S-Leiterbahn, U/O und deren Einspeisung. |
| Alte braune Litze am Masseabgriff | Dauerhafte Masseverbindung dieser Litze lösen. | Das gesamte weiterhin benötigte M-Netz. |
| Drei neue Netze P, W, R | Gegeneinander und gegen M/S gemäß Schaltung abgrenzen. | Originalbahnen, die weiterhin ihre ursprüngliche Funktion haben. |

**Bisher ist keine konkrete Kupfer-Trennstelle als notwendig belegt oder freigegeben.** Der beschriebene Weg erreicht die nötige elektrische Trennung durch Ablöten und Neuanschließen der Litzen. Das ist eine konkrete Trennungsstrategie und keine Behauptung, dass sämtliche Originalbahnen bereits gemessen seien.

Neue Bauteile können an isolierten Lötverbindungen auf der 62762 sitzen. Sollen dafür unbedingt vorhandene Leiterzüge als P/W/R-Netze dienen, ist vorher deren vollständige Verbindung zu Schalter, Endkontakten, Schrauben und Gegenseite zu erfassen. Erst daraus lässt sich eine bestimmte freie Bahn oder ein abgetrenntes Lötinselchen auswählen. Ein unbestücktes Lötpad ist nicht automatisch elektrisch frei.

## 4. Sichtbare Messbereiche auf dem aktuellen Nutzerfoto

Das Foto wird mit Nase links und Kupplung rechts betrachtet. Die folgenden Kennzeichen sind eigene Bildreferenzen, keine Werkspadnamen. Das neue Foto wird nicht automatisch in das öffentliche Repository hochgeladen.

| Kennzeichen | Sichtbarer Bereich | Zu prüfen |
|---|---|---|
| S1–S3 | Drei senkrecht angeordnete Lötpunkte am vorderen Platinenende, von oben nach unten. | Kontaktmatrix in U/O, gemeinsamer Kontakt und Eingänge. |
| H1 | Sichtbare vordere obere Befestigungsschraube. | Tatsächlicher Bezug zu M, S und umliegenden Leiterzügen. |
| H2 | Sichtbare hintere untere Befestigungsschraube. | Separat prüfen; gleiche Funktion wie H1 nicht unterstellen. |
| K | Schwarze Litze am hinteren unteren Platinenende. | Bis zum Mittelschleifer verfolgen und elektrisch bestätigen. |
| E | Hintere Endkontaktflächen. | Jede Fläche einzeln; auch vermeintlich unbenutzte Kontakte. |
| L | Vorderer Lampen-/Kontaktbereich. | Alte gelbe und braune Lampe getrennt zurückverfolgen; unterseitige Anschlüsse einbeziehen. |
| Z | Zwischenpads im mittleren Bereich. | Anschlussnetze und eventuelle Durchkontaktierung/Unterseitenbauteile erfassen. |

Der erzeugte siebenblättrige PDF-Arbeitsplan enthält eine Fotomarkierung dieser Bereiche, den elektrischen Gesamtplan, die LED-Netzliste, die Trennungsstrategie, ein Messblatt sowie die Fx-Prüfung. Er ist ausdrücklich kein bereits verifizierter Schnittplan aller Leiterbahnen der 62762.

## 5. Messungen vor Anschlussfreigabe

Spannungslos arbeiten. Lampe entfernen und Parallelpfade berücksichtigen. Vor der Messreihe den Eigenwiderstand der kurzgeschlossenen Messleitungen notieren.

| Messung | Erwartung |
|---|---|
| Neue Schalterlitze Braun gegen Radkontakt/Fahrgestell | Dauerhaft niederohmig in beiden Richtungsstellungen; noch offen. |
| Grau/Braun und Gelb/Braun nach Bewegung Nase voraus | Grau niederohmig, Gelb offen. |
| Grau/Braun und Gelb/Braun nach Bewegung Kupplung voraus | Grau offen, Gelb niederohmig. |
| Alte gelbe Lampenleitung gegen Schleifer/Pantograph, vor Umnutzung | U wählt Schleifer, O wählt Pantograph; nicht gewählte Quelle nicht direkt verbunden. |
| Alte braune Lampenleitung gegen Radkontakt, vor Ablöten | Dauerhafte M-Verbindung und deren Anschlusspunkt festhalten. |
| S1–S3 gegeneinander | Je drei Paarmessungen in beiden U/O-Stellungen. |
| H1/H2 und Endkontakte gegen M/S | Tatsächliche Verbindungen einzeln notieren, montiert und bei Bedarf ohne Schraubkontakt vergleichen. |
| Umgenutzte W-/R-Litze gegen M nach Trennung | Ohne angeschlossene Schalterleitungen kein direkter Massepfad. Mit Schalter wäre ein richtungsabhängiger Pfad dagegen beabsichtigt. |

Für eine fotoexakte Bahnzuordnung fehlen neben diesen Werten gegebenenfalls senkrechte Nahaufnahmen des vorderen Platinenendes und seiner Schalterseite. Die bereits vorhandenen allgemeinen Unterseitenbilder, der dokumentierte Mittelschleifer und der bereits erledigte Drehgestelleinbau werden nicht erneut als fehlend behandelt.

## 6. Was der ESU LokPilot 5 Fx tatsächlich zusätzlich bietet

Geprüft ist der **aktuelle LokPilot 5 Fx**, beispielsweise die Kabelausführung 59210. Ältere Fx-Versionen dürfen nicht automatisch mit denselben CVs konfiguriert werden.

Der LokPilot 5 Fx ist ein Funktionsdecoder ohne Motorausgang und ohne Sound. Er empfängt digitale Fahrtrichtungs- und Funktionsbefehle; damit lässt sich hinteres Licht bereits im Stand umschalten und digital ein-/ausschalten. Die Ausgangssteuerung erlaubt Helligkeitseinstellung und Lichteffekte. [Q5]

Die LokPilot-5-Anleitung dokumentiert ein richtungsabhängiges F0-Standardmapping und als auswählbaren Effekt ein dimmbares Licht mit Auf-/Abblenden. Die Funktion ist in der Decoderfamilie vorhanden; daraus folgt keine Zusage, dass sie im konkret gekauften Decoder bereits unverändert ab Werk aktiviert ist. Eine neue Software oder ein selbst geschriebenes Programm wird für diesen Effekt nicht benötigt. [Q6a, Q6b]

**Kein Händler oder spezielles Programmiergerät nötig:** Die erforderlichen Einstellungen können über DCC-CVs mit einer geeigneten Zentrale erfolgen. Die CS3 bietet das Konfigurieren und Hinzufügen einzelner CVs. Der ESU-LokProgrammer ist hierfür eine Komfortoption, keine zwingende Voraussetzung. Das ändert nichts daran, dass eine einmalige Einstellung nötig sein kann. [Q5, Q7]

### Beispiel für den dokumentierten Lichteffekt

Nur für einen passenden LokPilot 5 Fx und die normale Ausgangskonfiguration 1, nicht für den 60972:

| Reihenfolge | CV | Wert | Zweck |
|---|---:|---:|---|
| 1 | 31 | 16 | Index einstellen. |
| 2 | 32 | 0 | Ausgangskonfiguration auswählen. |
| 3 | 259 | 2 | Licht vorne: Auf-/Abblenden. |
| 4 | 267 | 2 | Licht hinten: Auf-/Abblenden. |

Nur den betreffenden Fx auf dem getrennten Programmiergleis bearbeiten. Aktuelle Werte sichern, einzeln schreiben und zurücklesen. Dazu Adresse, F0-Richtung, Helligkeit und LED-Modus prüfen. Der LED-Modus liegt für diese Ausgänge in CV263/CV271, Bit 7 (Wert 128); bestehende andere Bits erhalten. Bei ansonsten leerem Spezialfunktionswert ergibt sich 128. Vorwiderstände bleiben auch mit Decoder erforderlich. [Q6c–e, Q7]

Die angeführten CV-Seiten wurden in der zugänglichen Herstelleranleitung, 4. Auflage von 2020, geprüft, die bei ManualsLib gespiegelt ist. ESU stellt inzwischen eine 8. Auflage bereit. Vor dem Schreiben sind Version und Anleitung des tatsächlich gewählten Fx abzugleichen. Es wurde kein realer Fx an der CS3 programmiert.

### Warum dies den bisherigen Aufbau nicht einfach ersetzt

Der aktuelle LokPilot 5 Fx beherrscht DCC, Motorola und Selectrix, **aber kein mfx/M4**. RailComPlus ist nicht mfx. Die Bezeichnung Fx bedeutet hier Funktionsdecoder und macht ihn nicht zum mfx-Partner des Märklin-Decoders. [Q5]

Eine gleiche DCC-Zahlenadresse allein lässt ihn die mfx-Befehle des 60972 nicht mithören. Zudem priorisiert der 60972 mfx gegenüber DCC. Für den einfachen gemeinsamen Betrieb ohne Traktion könnten beide auf derselben DCC-Adresse gefahren werden; dazu wären der DCC-Betrieb und die Protokolle des 60972 passend einzustellen. Das wäre ein einzelner DCC-Bedieneintrag, nicht der geforderte unveränderte gemeinsame mfx-Betrieb. [Q5, Q8; Folgerung aus den Protokollfunktionen]

Der Fx ist außerdem kein dokumentiertes, ab Werk betriebsbereites Sanftwechselmodul für die zwei masseschaltenden Leitungen des neuen Bogies. Seine Lichtausgänge dürfen nicht einfach an Grau/Gelb des mechanischen Schalters gelegt werden. Ein eigener Sensoreingangs-/Mapping-Entwurf wäre gesondert zu prüfen; er wäre nicht mehr die ungeänderte Werkskonfiguration.

**Entscheidungsgrundlage:** Für weich schaltbares und digital abschaltbares Hecklicht kann der Fx einen Mehrwert bieten. Für die aktuell priorisierte Kombination aus einem 60972-mfx-Eintrag, keinem Zugkabel und mechanisch autonomem hinterem Licht ist er nicht erforderlich und beseitigt die gemeinsame Bedienfrage nicht automatisch. Der vorhandene mechanische Grundweg bleibt deshalb in diesem Arbeitsstand bestehen. Ein sanfter Lichtwechsel müsste bei Beibehaltung dieses Grundwegs durch eine separat auszulegende örtliche Elektronik ergänzt werden; die hier gezeichnete passive Schaltung enthält sie nicht.

## Quellen

Abruf: 18.09.2026. Herstellerangaben sind von der eigenen Verdrahtungsplanung und dem noch nicht gemessenen Nutzerfahrzeug zu unterscheiden.

- Q1: [REV17-Drehgestellnachtrag](../Arbeitsstand_REV17/Nachtrag_Drehgestell_2026-09-18.md) und Nutzerfoto/Messbericht im Gespräch.
- Q2: [62762-Bildbefund](../Arbeitsstand_Originalplatine/62762_pdf_inhalt.json), [ursprünglicher Hobby-Befund](../Arbeitsstand_Hobby_Befund/Befund_2976_Originalzustand.md). Historische Angaben zum fehlenden Richtungsschalter sind durch Q1 überholt.
- Q3: [Lokstoredigital: ICE-M-Frontmodule ohne Vorwiderstände](https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/).
- Q4: [Vishay 1N4148](https://www.vishay.com/docs/81857/1n4148.pdf), insbesondere Seite 1, Kathodenmarkierung.
- Q5: [ESU: LokPilot 5 Fx](https://www.esu.eu/produkte/lokpilot/lokpilot-5-fx/).
- Q6a: [ESU-Herstelleranleitung, Standardmapping, Seite 67](https://www.manualslib.de/manual/749436/Esu-Lokpilot-5.html?page=67).
- Q6b: [ESU-Herstelleranleitung, Lichteffekte, Seite 69](https://www.manualslib.de/manual/749436/Esu-Lokpilot-5.html?page=69).
- Q6c: [ESU-Herstelleranleitung, Ausgangs-CVs, Seite 68](https://www.manualslib.de/manual/749436/Esu-Lokpilot-5.html?page=68).
- Q6d: [ESU-Herstelleranleitung, Effektwerte, Seite 72](https://www.manualslib.de/manual/749436/Esu-Lokpilot-5.html?page=72).
- Q6e: [ESU-Herstelleranleitung, LED-Modus, Seite 70](https://www.manualslib.de/manual/749436/Esu-Lokpilot-5.html?page=70).
- Q7: [Märklin-CS3-Anleitung, CV-Konfiguration, Seite 14](https://www.manualslib.de/manual/89725/M%C3%A4rklin-Central-Station-3.html?page=14).
- Q8: [Märklin 60972/60982](https://static.maerklin.de/damcontent/93/1d/931db48faf5660916556d5172c598cdf1663856135.pdf), Seiten 7–8, Protokollpriorität/mfx.
