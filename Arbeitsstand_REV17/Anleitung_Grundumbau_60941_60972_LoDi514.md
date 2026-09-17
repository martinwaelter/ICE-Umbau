# ICE aus Märklin 2976 – Grundumbau mit 60941, 60972 und LoDi-514

**Arbeitsstand REV17 · 17. September 2026**

## 1. Auftrag und Ausführungsstand

Diese Anleitung beschreibt den Umbau des motorisierten Triebkopfes auf den Hochleistungsantrieb 60941 und den mfx-Lokdecoder 60972 ohne Sound. An beiden Zugenden werden ausschließlich die LoDi-514-Frontlichtmodule verwendet, keine LoDi-Motor-, Decoderträger- oder Innenbeleuchtungsplatinen. Der mit dem 60972 gelieferte Märklin-Schnittstellenträger wird benötigt und ist ausdrücklich Bestandteil dieses Aufbaus.

Der motorlose Kopf erhält nach dem aktuellen Auftrag eine vollständige, von der Radbewegung betätigte Lichtwechsel-Drehgestellbaugruppe. Seine Beleuchtung arbeitet örtlich, ohne zweiten Decoder und ohne neue elektrische Verbindung durch die Mittelwagen. Deren vorhandene Beleuchtung soll erhalten bleiben.

**Status:** Motor-, Decoder- und vorderer LED-Anschluss sind als Arbeitsfolge beschrieben. Die hintere Schaltung ist nach der tatsächlichen Kontaktart der Austauschbaugruppe auszuwählen. Ihre konkreten Lötpads, die mechanische Passung und die Kontaktfunktion sind am gewählten Ersatzteil noch nicht bestätigt. Auch die U/O-Anschlüsse des eigenen Motorträgers müssen vor dem Ablöten zugeordnet werden. Es wurden für REV17 keine Arbeiten am Fahrzeug, Hardwaretests oder Schaltungssimulationen durchgeführt. Eine endgültige Widerstandsauslegung für die gewünschte LED-Helligkeit setzt weitere LED-Daten voraus.

### Das gilt im Grundumbau

| Anforderung | Umsetzung und Grenze |
|---|---|
| Weiß/Rot an beiden Zugenden | Vorn elektronisch aus dem 60972; hinten mechanisch aus der tatsächlichen Radbewegung. |
| Automatische Anmeldung | Ein 60972 meldet sich über mfx an. Der gewünschte Fahrzeugname und die Einstellungen werden kontrolliert. |
| Kein Sound | Kein Sounddecoder, kein Lautsprecher, kein Soundmodul. |
| Keine Zugdurchverdrahtung | Keine neue Licht- oder Steuerleitung zwischen den Fahrzeugen. |
| Motorloser Kopf ohne Decoder | Vollständige Lichtwechselbaugruppe und örtliche LED-Versorgung. |
| Bestehendes Wagenlicht | Vorhandene Leuchtmittel, Achskontakte und deren funktionierende Versorgung erhalten. |
| Keine zusätzlichen LoDi-Platinen | Nur die beiden Frontmodule; nötige Widerstände/Dioden sind diskrete Bauteile. |
| Keine CS3-Traktion | Nur ein angetriebener Kopf und ein Decoder. |
| Pantograph bleibt anschließbar | Vorhandene Unter-/Oberleitungswahl bleibt vor dem Versorgungseingang des jeweiligen Kopfes erhalten. Keine Überbrückung der beiden Quellen. |

**Zwei Betriebsgrenzen gehören zum Aufbau:** Ein mechanischer Richtungsschalter kann einen Richtungsbefehl im Stillstand nicht erkennen. Er schaltet erst nach einer kleinen tatsächlichen Radbewegung. Außerdem kann F0 des 60972 ohne zusätzliche Steuerverbindung nicht die unabhängig versorgten hinteren und mittleren Lichter ausschalten. Im Grundumbau schaltet F0 nur das Licht des motorisierten Kopfes. Die gemeinsame Abschaltung ist eine separate Option in Abschnitt 15.

### Abgrenzung zu REV16 und REV16.1

Die dort beschriebene Zweipol-Kupplungsschaltung mit Sender und Empfänger ist **nicht** Bestandteil dieses Grundumbaus. Insbesondere werden ihre AUX1/AUX2-Zuordnung, Kupplungsverdrahtung und Anweisung zur vollständigen elektrischen Stilllegung der alten Kopfplatine nicht übernommen. Letzteres würde ohne weitere Maßnahmen die gewünschte U/O-Wahl verlieren. Die alten Dateien bleiben als alternative/historische Ausführungen unverändert erhalten. Einzelne Schritte aus verschiedenen Varianten dürfen nicht ungeprüft kombiniert werden. [Q7, Q8]

## 2. Was am vorhandenen Zug bereits bekannt ist

Der vorhandene Befund dokumentiert im motorlosen Kopf eine lange passive Platine **62762** und eine klare Glühlampe. Die separate Lichtwechsel-Schalterplatine ist nicht montiert. Der vorhandene U/O-Schieber ersetzt diese fehlende Richtungserkennung nicht. Am nasenseitigen Drehgestell sind Zahnräder beziehungsweise Zahnkränze erkennbar; deshalb ist die Behauptung, dort fehle grundsätzlich jede Betätigungsmechanik, nicht gerechtfertigt. Der aktuelle Auftrag wählt dennoch ausdrücklich den Austausch gegen eine vollständige Lichtwechselbaugruppe. [Q7]

Der eigene Mittelschleifer des motorlosen Kopfes am kupplungsseitigen Drehgestell ist durch IMG_0644 und IMG_0646 dokumentiert. Auch die gesamte Unterseite und die U/O-Markierung wurden bereits gezeigt. Diese Aufnahmen müssen nicht nochmals angefordert werden. Offen ist die Zuordnung des **konkret gewählten Ersatzdrehgestells**, nicht das Vorhandensein der genannten Bestandsbilder. [Q7]

Die übermittelten Durchgangsprüfungen sprechen für einen richtungsunabhängigen alten Lampenanschluss. Die im Befund dokumentierte Einschränkung zur nicht nochmals bestätigten Lampenentnahme bleibt bestehen. Aus diesen Messungen ergibt sich kein fertiger Lötplan für eine neue Schalterplatine. [Q7]

## 3. Bezeichnungen, Material und Arbeitsplatz

**TK-A** bezeichnet den motorisierten Kopf, **TK-B** den motorlosen Kopf. „Vorwärts“ bedeutet hier: TK-A fährt mit seiner Nase voraus. Die Buchstaben der Kopfbezeichnung sind nicht mit dem Gleisanschluss B zu verwechseln.

| Bezeichnung | Bedeutung |
|---|---|
| B | Digitaler Versorgungsleiter vom Mittelschleifer oder von der ausgewählten Oberleitung. |
| 0 | Außenschienenanschluss über Räder/Achskontakte. |
| S-A / S-B | Gemeinsamer Ausgang der jeweiligen geprüften U/O-Wahl. |
| U+ / +Ub | Gemeinsames Decoderplus des 60972; Märklin-Farbe orange. Nicht Gleismasse. |
| VCC, white, red | Beschriftete Anschlüsse des hier vorgesehenen LoDi-Frontmoduls. |
| C, W, R | Erst durch Messung zugeordnete Kontakte des hinteren Richtungsschalters: gemeinsamer Kontakt, Weiß, Rot. Keine behaupteten Hersteller-Padnamen. |
| P, N | Örtliche gleichgerichtete Anschlüsse im hinteren Schaltungsentwurf, keine Verbindung zum vorderen Decoder. |

Bereitlegen: ein vollständiger 60941-Satz einschließlich der zugehörigen Entstörteile, ein 60972 mit Schnittstellenträger und Halter, zwei passende LoDi-514-Frontmodule, vier Widerstände **47 kOhm / 0,25 W / 5 % oder besser** als stromarme Startbestückung, geeignete Feinlitze, Schrumpfschlauch und isolierende Befestigung. Für die hintere Versorgung kommen je nach Kontaktart drei oder sechs Dioden 1N4148 hinzu; diese Auswahl erfolgt erst nach Abschnitt 10. Die Widerstände sind keine bestätigte LoDi-Nennbestückung, siehe Abschnitt 8.

Hinzu kommt die vollständige mechanische Lichtwechselbaugruppe einschließlich Betätigung und Befestigung. Nicht allein aufgrund einer passenden Artikelbeschreibung bestellen: Befestigung, Rad-/Getriebeausführung, Höhe, Schwenkraum, Schalter und Lieferumfang müssen zusammenpassen. Eine bloße 638930 ist kein nachgewiesener vollständiger Umrüstsatz.

Werkzeug: passende Schraubendreher, Pinzette, feine Lötstation, Entlötlitze, Multimeter mit Widerstands- und Diodenmessung, Lupe, Beschriftungsmaterial und nichtleitende Unterlage. Widerstands- und Durchgangsmessungen ausschließlich spannungslos durchführen. Für alle Lötarbeiten am neuen Träger wird der Decoder abgezogen.

## 4. Öffnen und Bestand sichern

1. Den vollständigen Zug von allen versorgten Gleisen nehmen, Fahrzeuge trennen und TK-A/TK-B innen kennzeichnen. Vor jeder Demontage Ober- und Unterseite fotografieren.
2. Die Befestigung des eigenen Gehäuses ansehen. Beim verwandten ICE beschreibt LoDi das Abziehen der kupplungsseitigen Abdeckung und das Lösen der unteren Gehäusebefestigung. Dies ist eine Orientierung, kein Auftrag, die U/O-Betätigung herauszuschrauben. Bei Widerstand nicht am Gehäuse reißen. [Q3]
3. Gehäuse vorsichtig abheben. Eventuelle Pantographen-Kontaktfedern und deren Lage dokumentieren. Keine Feder verbiegen, keine Leitung straffziehen.
4. Vor dem Ablöten Leitungen bis zum Verbraucher verfolgen und beschriften: Mittelschleifer, Radkontakt, Pantographenabgriff, U/O-Ausgang, alte Motoranschlüsse, alte Lampenanschlüsse und gegebenenfalls vorhandene Wagenlichtversorgung. Farben allein genügen nicht.
5. Alte Motorsteuerung beziehungsweise alten Fahrtrichtungsumschalter identifizieren. Dessen Verbindungen zu Motor und neuem Kopflicht werden entfernt. Die passive U/O-Stromwahl wird dagegen zunächst erhalten und separat durchgemessen.
6. Unklare Enden einzeln isolieren. Keine Leitungen oder Leiterbahnen auf Verdacht verbinden oder schneiden. Insbesondere die Originalplatine nicht pauschal elektrisch stilllegen, solange die dort liegende U/O-Funktion noch gebraucht wird.

**Zwischenergebnis:** Die zu entfernende alte Motorsteuerung und die zu erhaltende Stromquellenwahl sind eindeutig voneinander abgegrenzt.

## 5. U/O unter dem Kopf: Funktion erhalten

### Bedeutung und Anschlussprinzip

Die U/O-Markierung und der dokumentierte Schieber sprechen für **Unterleitung/Mittelschleifer** und **Oberleitung/Pantograph**. Sie bezeichnen nicht den automatischen Fahrtrichtungswechsel. Die sichtbare Betätigung ist nicht ohne Prüfung als gewöhnliche Gehäuseschraube zu behandeln. Eine bestimmte Schraubendrehrichtung, Anzahl von Umdrehungen oder Vierteldrehung ist für das eigene Exemplar nicht verifiziert. Zum Prüfen den tatsächlichen Schieber von innen beobachten. [Q7]

Für den Umbau ist folgendes Quellenwahl-Prinzip vorgesehen:

```text
Mittelschleifer -------- Eingang U --\
                                     U/O-Wahl --- S-A --- ROT / B des 60972
Pantographenkontakt ---- Eingang O --/

Rad-/Achskontakt --------------------------------------- BRAUN / 0 des 60972
```

**Rot kommt an den gemeinsamen Ausgang S-A, nicht einfach direkt an den Schleifer.** Andernfalls würde die Quellenwahl umgangen. Die U/O-Funktion wird nicht an einen Motor- oder Lichtausgang gelegt.

### Stromlos zuordnen

Zuerst Verbraucher und alte Elektronik so abtrennen, dass nicht über Lampen, Wicklungen oder Halbleiter rückwärts gemessen wird. Die mechanische Auswahl selbst bleibt montiert. Messspitzen kurzschließen und ihren Eigenwiderstand prüfen. Dann den gemeinsamen Kontakt und die beiden Eingänge identifizieren:

| Geprüfte Stellung | S zum Mittelschleifer | S zum Pantographenkontakt |
|---|---|---|
| U | Niederohmige Verbindung | Keine direkte Verbindung |
| O | Keine direkte Verbindung | Niederohmige Verbindung |

Zusätzlich müssen S und beide Quelleneingänge gegenüber dem Außenschienenanschluss 0 ohne direkten Kurzschluss bleiben. Den Pantographenweg gegebenenfalls mit vorsichtig aufgesetztem Gehäuse prüfen, wenn erst dann die Kontaktfeder anliegt. Nicht allein am isolierten Dachteil messen und daraus auf den zusammengebauten Kopf schließen.

Ist keine eindeutige Wechselauswahl messbar, **noch nicht anschließen**: Kontaktweg und eventuell parallel vorhandene Leiterzüge zuerst klären. Es werden keine unbekannten Pads überbrückt. Nach erfolgreicher Messung die realen Anschlüsse mit U, O und S kennzeichnen und fotografieren. Für TK-B dieselbe Prüfung separat durchführen, soweit dessen Oberleitungswahl erhalten werden soll.

### Grenzen des Oberleitungsbetriebs

Der erhaltene Leitungsweg ist keine pauschale Herstellerfreigabe eines vollständig umgebauten 2976 für störungsfreien digitalen Oberleitungsbetrieb. Kontaktqualität, Isolation, Stromtragfähigkeit und die Anmeldung über diesen Weg müssen am Fahrzeug geprüft werden. Die Erstinbetriebnahme erfolgt in U-Stellung über den Mittelschleifer.

Die Oberleitung darf nicht von einem zusätzlichen Analogtrafo oder einem unabhängigen Digitalausgang gespeist werden, während der Zug über Räder, Schleifer oder Kupplungen die Stromkreise verbinden könnte. Für den späteren Einzeltest nur eine geeignete gemeinsame Digitalquelle verwenden. Das bloße Berühren einer zufällig versorgten Oberleitung ist kein zulässiger Test. U/O grundsätzlich spannungslos umstellen.

Ohne Verbindung durch den Zug speist der Pantograph eines Kopfes nicht automatisch den anderen Kopf oder die Mittelwagen. Jede örtliche Quellenwahl wirkt nur auf den eigenen Stromkreis.

## 6. 60941 mechanisch einbauen

Der Satz ersetzt beim passenden Trommelkollektorantrieb Feldmagnet, Anker und Motorschild. Fahrwerk und Getriebe bleiben erhalten. Die Herstellerzeichnung zeigt die Teilefolge; sie ist keine fotografische Montagefreigabe jeder ICE-Variante. [Q2, Q4]

1. Den alten Motor aus mehreren Richtungen fotografieren. Lage von Leitungen, Federn, Bürsten, Schrauben und vorhandenen Entstörteilen festhalten. Ablage für Kleinteile vorbereiten.
2. Bürstenfedern vorsichtig entlasten, alte Bürsten herausnehmen und die Motorleitungen ablöten. Nicht mit eingelegten Bürsten am Motorschild ziehen.
3. Die Motorschildschrauben lösen und geordnet ablegen. Schild abnehmen, Anker vorsichtig herausziehen und alten Feldmagneten ausbauen. Vorhandene zusätzliche Scheiben oder Distanzteile nicht verlieren; ihre ursprüngliche Lage festhalten und die neue Passung prüfen.
4. Lose Ablagerungen entfernen. Das Getriebe ohne Motoranker prüfen. Es muss sich ohne hartes Klemmen bewegen lassen. Ein bereits klemmendes Getriebe wird nicht durch stärker angezogene neue Motorschrauben repariert.
5. Den Permanentmagneten des 60941 in seine Aufnahme setzen. Er muss plan sitzen und darf keine Leitung einklemmen. Den neuen Anker so einsetzen, dass sein Ritzel sauber mit dem Getriebe kämmt.
6. Neues Motorschild aufsetzen und das Lager über die Ankerwelle führen. Schrauben zunächst nur leicht eindrehen, abwechselnd anziehen und dazwischen den freien Lauf kontrollieren. Zu lange Ersatzschrauben dürfen keine Zahnräder oder Wicklungen erreichen. Nicht durch Kraft einen schief sitzenden Schild oder Magneten zurechtziehen.
7. Neue Bürsten einsetzen und die Federn korrekt auflegen. Bürsten müssen sich in ihren Führungen bewegen können. Die Federn dürfen das Metallfahrwerk nicht berühren.
8. Motor/Getriebe vorsichtig von Hand prüfen. Magnetisches Rasten ist von einem festen mechanischen Anschlag zu unterscheiden. Wird der Lauf erst beim Festziehen schwergängig, Montage unterbrechen und Lager-/Schraubensitz korrigieren.
9. Keine Schmiermittel an Kollektor, Bürsten oder elektrischen Kontaktflächen aufbringen. Schmierung an den dafür vorgesehenen Lagerstellen nach der Fahrzeugwartung durchführen; keine pauschale Ölzugabe in den Motorraum.

**Entstörung:** Ein vorhandener Kondensator ausschließlich zwischen den beiden Bürstenanschlüssen kann bestehen bleiben. Kondensatoren von einem Bürstenanschluss zum Metallfahrwerk werden für diese Decoderverdrahtung entfernt. Bauteile anhand ihrer tatsächlichen Anschlüsse identifizieren, nicht anhand einer bloßen Bildähnlichkeit. Das LoDi-Herstellerbeispiel zeigt diese Unterscheidung an einem verwandten ICE. [Q3]

## 7. Motor und 60972 verdrahten

### Vorher die Motorisolation prüfen

Beide Motorzuleitungen müssen vom Decoder getrennt sein. Jede Bürste gegen blankes Metallfahrwerk und gegen die Stromabnehmer messen. Es darf keine dauerhafte niederohmige Verbindung bestehen. In mehreren Ankerstellungen wiederholen. Ein kurzer Ladeeffekt eines Kondensators ist nicht mit dauerhaftem Durchgang gleichzusetzen.

Zwischen den beiden Bürsten ist ein endlicher, von der Ankerstellung abhängiger Wicklungswiderstand zu erwarten. „Überall kein Durchgang“ wäre daher ebenfalls keine richtige Abnahme. Bei unklarem Ergebnis vor dem Decoderanschluss Ursache ermitteln.

### Träger befestigen

Den gelieferten 21MTC-Träger mit seiner Halterung so montieren, dass Decoder, Lötstellen und Rückseite gegen alte Leiterzüge, Metallfahrwerk und Schrauben isoliert sind. Ein vorhandener mechanischer Träger darf genutzt werden, sofern die Isolation und der Platz genügen. Die alte U/O-Funktion bleibt dabei funktionsfähig. Keine unbestimmten alten Leiterzüge als neue Verteiler benutzen.

Drehgestelle bis zu beiden Anschlägen schwenken. Leitungen dürfen weder auf Zahnrädern liegen noch von Drehgestell, Gehäuse oder Pantographenfeder gequetscht werden. Lötstellen mit Schrumpfschlauch sichern; ungenutzte Leitungen einzeln isolieren.

### Verbindliche Anschlussliste für TK-A

| 60972-Anschluss | Märklin-Farbe | Ziel im neuen Aufbau |
|---|---|---|
| B / G rechts | Rot | Geprüfter gemeinsamer Ausgang S-A der U/O-Wahl. |
| 0 / G links | Braun | Zuverlässiger örtlicher Rad-/Achskontakt beziehungsweise geprüfter Chassisanschluss. |
| MV | Grün | Über eine zum Motorsatz gehörende Drossel zu Bürste 1. |
| MR | Blau | Über die zweite Drossel zu Bürste 2. |
| +Ub | Orange | VCC des vorderen LoDi-514. |
| LV | Grau | Über eigenen Widerstand R-A-W zum Anschluss white. |
| LR | Gelb | Über eigenen Widerstand R-A-R zum Anschluss red. |
| AUX1 bis AUX4 | Nach Trägerbeschriftung | Im Grundumbau unbenutzt. |
| GND, +5V, SUSI | Nach Trägerbeschriftung | Im Grundumbau ohne Anschluss. |

Die Bezeichnungen der tatsächlichen Märklin-Trägerplatine haben Vorrang. Die NEM-Farben eines anderen Decoders nicht übertragen: Insbesondere ist **orange hier Decoderplus**, während **blau hier eine Motorleitung** ist. [Q1]

```text
60972 MV / grün ---- Drossel ---- Bürste 1
60972 MR / blau ---- Drossel ---- Bürste 2

                Bürste 1 --- Entstörkondensator --- Bürste 2

Kein Bürstenanschluss an das Metallfahrwerk.
```

Erst nach Abschluss aller Löt- und Isolationsprüfungen den Decoder einsetzen. Kodierung und Steckrichtung kontrollieren; weder um eine Position noch um eine Reihe versetzt aufstecken. Nicht am eingesteckten Decoder löten.

## 8. LoDi-514 im motorisierten Kopf anschließen

### Modul und Einbauposition prüfen

Vorgesehen ist das ICE-1-Frontmodul mit den Anschlüssen **VCC, white und red**. Die ebenfalls angebotenen ICE-2-Varianten dürfen nicht allein wegen ähnlicher Form gleichgesetzt werden. Vor dem Einbau Beschriftung des tatsächlich gelieferten Moduls mit dem Herstellerbeispiel abgleichen. Die ICE-1-Frontmodule werden ohne integrierte Vorwiderstände beschrieben. [Q3, Q5]

Alte Kopfglühlampe beziehungsweise Lampen und die nicht mehr verwendeten Fassungsanschlüsse elektrisch entfernen. Lichtleiter und Gehäuseöffnungen erhalten. Neues Modul zunächst ohne Klebstoff positionieren und das Gehäuse vorsichtig probeweise aufsetzen. Das Modul muss zu den Lichtleitern ausgerichtet sein und darf weder verspannt werden noch mit seinen Kontakten Metall berühren. Eine geänderte Halterform ist kein Anlass, den Lichtleiter auf Verdacht abzuschneiden.

### Anschluss

```text
60972 orange / +Ub ---------------------------- VCC

60972 grau / LV ---- R-A-W 47 kOhm ------------ white

60972 gelb / LR ---- R-A-R 47 kOhm ------------ red
```

Die beiden Widerstände sind getrennt erforderlich. LV und LR werden nicht zusammengelötet. VCC wird nicht an braune Radmasse, GND oder +5V gelegt. Kein alter Lampen-Masseanschluss bleibt am neuen Modul angeschlossen.

Vor dem Löten jeden Widerstand messen. Bei 47 kOhm und 5 % sind etwa 44,65 bis 49,35 kOhm zulässig. Widerstände und Anschlussstellen so montieren, dass weder Gehäuse noch Drehgestell an ihnen scheuern. Die Strombegrenzung muss auch bei maximaler Decoderhelligkeit wirksam sein; Dimmen ersetzt sie nicht.

### Warum zunächst 47 kOhm?

Diese Wahl ist eine **stromarme Start- und Prüfbestückung**, keine vom LED-Hersteller bestätigte Auslegung für die endgültige Helligkeit. Unter der hier festgelegten Auslegungsannahme von höchstens 24 V am jeweiligen Lichtkreis ergibt sich selbst ohne Abzug einer LED-Flussspannung:

```text
R_min = 47.000 Ohm × 0,95 = 44.650 Ohm
I_max <= 24 V / 44.650 Ohm = 0,538 mA
P_R   <= (24 V)^2 / 44.650 Ohm = 0,0129 W
```

Die konkrete Versorgung muss diese Spannungsannahme erfüllen. Ein beliebiger AC-Multimeterwert am Digitalgleis beweist keine maximale Spitzenspannung. 24 V sind außerdem kein allgemeiner Sollwert für die Anlage. Die zulässige höhere Decoderspannung aus dessen Datenblatt ist keine Freigabe für die LEDs.

Das Licht kann mit dieser Bestückung zu schwach sein. Vor einer Verringerung werden zulässiger Strom und interne Verschaltung des gelieferten LED-Farbzweiges benötigt. Für einen bekannten Serienzweig gilt als Auslegungsansatz `R >= (U_max − Summe der LED-Flussspannungen) / zulässiger Zweigstrom`, mit Toleranz- und Leistungsreserve. Bei mehreren parallelen LED-Pfaden ist deren Stromaufteilung zusätzlich zu berücksichtigen. Ein pauschales „jede LED verträgt 20 mA“ wird nicht unterstellt. [Q5; Rechnung: eigene Auslegung]

## 9. Mechanischen Lichtwechsel im motorlosen Kopf nachrüsten

### Vollständige Baugruppe statt unklarer Einzelplatine

Die Märklin-Zeichnung für **33701/37701/39711** nennt unter anderem die motorlose vordere Drehgestellbaugruppe **374320**, die separate Leiterplatte **638930** und deren Schraube **785030**. Die lange 627620 ist eine andere Baugruppe. Diese Herstellerzeichnung dokumentiert verwandte Modelle, aber keine ausdrückliche Nachrüstfreigabe für den Hobby-2976. [Q6]

Als Austausch vorgesehen ist eine zusammengehörige und funktionsfähige Baugruppe mit Rädern, Betätigung, Richtungskontakten und Befestigung. Ein nacktes Drehgestell ohne den betätigten Schalter erfüllt den Zweck nicht. Ein Händlerfoto oder die Nummer 374320 allein beweist nicht, dass die Schalterplatine mitgeliefert wird.

### Mechanische Arbeitsfolge

1. TK-B öffnen und die örtliche Versorgung spannungslos lassen. Alte Lampenleitungen sowie U/O-Weg dokumentieren. Der kupplungsseitige Mittelschleifer bleibt erhalten.
2. Vor dem Ausbau die Befestigung des nasenseitigen Drehgestells sowie dessen Höhe, Schwenkbereich, Radstellung und Haltebauteile dokumentieren. Die Gehäusebefestigung und die U/O-Betätigung davon unterscheiden.
3. Die vollständige Spenderbaugruppe danebenlegen und Befestigung, Rad-/Getriebeausführung, Raum für den aufragenden Schalter und die Gehäusefreiheit vergleichen. Bei abweichender Aufnahme nicht durch Bohren, Feilen oder Schraubenzwang eine vermeintliche Passung herstellen.
4. Die tatsächliche Drehgestellhalterung lösen, Teile in Reihenfolge ablegen und das einfache Drehgestell entnehmen. Keine Leiterbahn oder Kontaktfeder als mechanischen Halter verbiegen.
5. Ersatzbaugruppe mit der zu ihr und zum Fahrwerk passenden Halterung einsetzen. Freies Schwenken und Rollen prüfen. Halteschrauben dürfen Räder, Achsen, Getriebe oder Schalter nicht blockieren.
6. Radbewegung in beide Richtungen beobachten. Die vollständige Betätigungskette muss den Richtungsschalter bewegen. Ein nur montiertes, aber nicht mitgenommenes Schaltteil ist keine funktionierende Nachrüstung.
7. Elektrische Kontaktprüfung nach Abschnitt 10 durchführen. Erst danach die LED-Versorgung anschließen und den Gehäuseschluss prüfen.

**Noch offen:** Der konkrete Spender beziehungsweise Ersatzteilsatz wurde für REV17 nicht am Nutzerfahrzeug montiert. Eine garantiert passende Kaufempfehlung oder fotoexakte Schrauben-/Lötpadzuordnung wird deshalb nicht behauptet.

## 10. Hinteren Schalter messen – vor der Schaltungswahl

Alle alten Lampenleitungen und fremden Versorgungszweige vom zu untersuchenden Schalter abgrenzen. Über noch angeschlossene Glühlampen oder Elektronik darf keine Kontaktbelegung abgeleitet werden. Die Prüfung erfolgt auch im montierten Zustand, weil Befestigungsteile einen vorher isolierten Kontakt mit dem Chassis verbinden können.

1. Den gemeinsamen Kontakt suchen, der bei Radbewegung abwechselnd mit zwei unterschiedlichen Abgängen verbunden wird. Diese Kontakte zunächst C, X und Y nennen.
2. TK-B mit der Nase voraus rollen: festhalten, welcher Abgang mit C verbunden ist. Dieser Abgang soll später W werden. In Gegenrichtung rollen: der andere Abgang soll R werden.
3. Jeweils anhalten. Prüfen, ob die zuletzt gewählte Stellung erhalten bleibt. Mehrfach in beiden Richtungen wiederholen. Der Umschaltweg wird gemessen, nicht als feste Zahl angenommen.
4. C, W und R einzeln gegen Radkontakt 0, Mittelschleifer, U/O-Ausgang und Metallfahrwerk messen. Nicht nur den losen, sondern auch den eingebauten Schalter prüfen.
5. Ergebnisse und ein scharfes Foto mit den tatsächlich identifizierten Kontaktstellen festhalten. Es gibt in REV17 noch keine erfundenen Padnummern für 638930.

| Ergebnis | Folgerung |
|---|---|
| Ein vollständig potentialfreier Umschaltkontakt C/W/R, ohne direkte Verbindung zu Gleis oder Chassis | Schaltungsentwurf 11A ist anwendbar, vorbehaltlich der weiteren Prüfungen. |
| C liegt nachweislich an Radkontakt 0; W und R werden nur gegen diesen Kontakt geschaltet | Schaltungsentwurf 11B ist anwendbar, vorbehaltlich der weiteren Prüfungen. |
| C liegt an B, mehrere anders verschaltete Kontakte oder zusätzliche unbekannte Bauteile | Keine der beiden Schaltungen unverändert anschließen. Zunächst konkrete Schaltung aufnehmen. |
| Keine reproduzierbare Umschaltung durch Radbewegung | Mechanik beziehungsweise Teileumfang korrigieren; LED-Einbau ersetzt die fehlende Richtungserkennung nicht. |

## 11. Örtliche LED-Versorgung hinten

**Die folgenden Schaltungen sind eigene, noch nicht am realen Drehgestell geprüfte Anschlussentwürfe. Die Messung in Abschnitt 10 entscheidet; sie sind keine zwei beliebig austauschbaren Herstellerbelegungen.** Die nötigen diskreten Bauteile können auf isolierten Lötstützpunkten montiert werden. Eine LoDi-Trägerplatine ist nicht erforderlich. Keine Verbindung zum 60972 oder zu den Kupplungen herstellen.

### 11A. Potentialfreier Richtungsschalter: örtliche Vollweggleichrichtung

X ist hier ausschließlich der Versorgungseingang S-B und Y der örtliche Radanschluss 0; diese Bezeichnungen sind nicht mit den vorläufigen Kontaktbezeichnungen aus Abschnitt 10 zu verwechseln.

Eine Gleichrichterbrücke aus vier 1N4148 wird wie folgt aufgebaut. Der Gehäusering bezeichnet die Kathode. [Q9]

| Diode | Anode, ohne Ring | Kathode, mit Ring |
|---|---|---|
| D1 | S-B | P |
| D2 | Radanschluss 0 | P |
| D3 | N | S-B |
| D4 | N | Radanschluss 0 |

Damit ist P die Verbindung der beiden Kathoden D1/D2, N die Verbindung der beiden Anoden D3/D4. Anschließend:

```text
Brücke P ------------------------------- LoDi VCC
Brücke N ------------------------------- Schalter C

LoDi white ---- R-B-W 47 kOhm ----------- Schalter W
LoDi red ------ R-B-R 47 kOhm ----------- Schalter R
```

Zusätzlich je eine Schutzdiode entgegen der LED-Durchlassrichtung: D5 mit Anode an white und Kathodenring an VCC; D6 mit Anode an red und Kathodenring an VCC. Die Schutzdioden liegen nicht über den Vorwiderständen. Kein Pufferkondensator ist vorgesehen.

**P und N dürfen nicht zusätzlich mit Radmasse oder Chassis verbunden werden.** Insbesondere ein nachträglich an 0 liegender Schalterkontakt C kann die Brücke in einer Halbwelle kurzschließen. Die Gleichrichtung stellt keine galvanische Trennung vom Gleis her. Diese Variante setzt deshalb den nachweislich potentialfreien Schalter einschließlich seiner Befestigung voraus.

### 11B. Schalter mit gemeinsamem Rad-/Massekontakt: örtliche Einweggleichrichtung

Nur wenn C tatsächlich an 0 liegt und die beiden Abgänge ausschließlich gegen C schalten, wird folgender Entwurf verwendet:

```text
S-B ---- D0, Anode links / Ring rechts ---- P ---- LoDi VCC

Radkontakt 0 ---------------------------------- Schalter C
LoDi white ---- R-B-W 47 kOhm ------------------ Schalter W
LoDi red ------ R-B-R 47 kOhm ------------------ Schalter R
```

D0 ist eine 1N4148. Dazu D-W mit Anode an white und Kathodenring an VCC sowie D-R mit Anode an red und Kathodenring an VCC. Diese beiden Dioden begrenzen eine umgekehrte Spannung an den LED-Zweigen. Auch hier kein Pufferkondensator und keine Verbindung zum vorderen Decoder.

Die Beleuchtung nutzt nur eine Polarität der Digitalspannung. Ihre mittlere Helligkeit kann daher vom vorderen Decoderlicht abweichen und mit dem Digitalsignal variieren. Flackerfreiheit wird nicht zugesagt. Bei störendem Verhalten wird der reale Schalteranschluss neu bewertet; **nicht** einfach eine Gleichrichterbrücke ergänzen und deren Minus mit 0 verbinden.

### Prüfung beider Entwürfe

Widerstände vor Einbau einzeln messen. Diodenrichtung mit Diodentest kontrollieren; nicht allein vom Aussehen einer alten Leitung ausgehen. Die komplette Schaltung zunächst spannungslos auf offensichtliche Kurzschlüsse prüfen. Alte Lampenanschlüsse dürfen die neuen Zweige nicht überbrücken.

TK-B zuerst getrennt vom Zug auf einem abgesicherten Prüfabschnitt und in U-Stellung versorgen. Strom sofort abschalten, wenn unerwartet beide Farben dauerhaft leuchten, eine Quelle kurzgeschlossen wird oder Bauteile warm werden. Die Versorgungsspannungsannahme aus Abschnitt 8 gilt auch hier.

Beim Rollen mit TK-B voraus muss nur white, in Gegenrichtung nur red leuchten. Sind ausschließlich die Farben vertauscht, W/R-Zuordnung korrigieren; nicht die Versorgungsdiode umpolen. Ein kurzzeitiger Kontaktübergang ist von einem dauerhaften Fehlschalten zu unterscheiden. Nach Gehäusemontage alle Prüfungen wiederholen.

## 12. Bestehende Mittelwagenbeleuchtung erhalten

Die Mittelwagen werden in dieser Stufe nicht auf LoDi-Platinen und nicht auf Decoderbetrieb umgebaut. Vorhandene Achskontakte bleiben erhalten. **Ein Achsschleifer beziehungsweise Radkontakt liefert beim Märklin-Dreileitersystem nur den Außenschienenanschluss 0.** Für Licht muss zusätzlich der Versorgungsleiter B ankommen, zum Beispiel über einen eigenen Mittelschleifer oder einen bereits vorhandenen Versorgungsweg.

Die Aussage „Beleuchtung über Schleiferachsen“ wird deshalb nicht als Nachweis eines eigenen Mittelschleifers an jedem Wagen behandelt. Zunächst die tatsächlich funktionierende Versorgung verfolgen. Bestehende Leuchtmittel, Kontakte und Leitungen nicht vorsorglich entfernen. Ebenso wenig einen vorhandenen Versorgungsweg in TK-A ablöten, ohne festzustellen, ob er Wagenlicht speist.

Falls ein Wagen bereits vollständig örtlich versorgt ist, bleibt dieser Lichtkreis unabhängig vom neuen Decoder. Hängt er dagegen an einem bisherigen Zug-Versorgungsweg, wird genau dieser Bestand dokumentiert und erhalten oder die Versorgung ausdrücklich neu entschieden. Der Grundumbau führt selbst keine neue Zugleitung ein. Eine erst noch fehlende Stromversorgung wird nicht durch die Annahme ersetzt, Achskontakte allein reichten aus.

Vor dauerndem Digitalbetrieb Nennspannung und Zustand der vorhandenen Beleuchtung prüfen. Alte analoge Lampen nicht ohne diese Prüfung als dauerhaft digitaltauglich erklären. Wagen einzeln zusetzen und Kontakte sowie Erwärmung kontrollieren. Helligkeitsregelung, LED-Tausch und gemeinsame Abschaltung bleiben außerhalb dieser Stufe. [Q7, Q8]

## 13. CS3: ein mfx-Eintrag, kein Sound, keine Traktion

### Anmeldung und Motor

1. Einen losen, vollständig von Anlage und Booster getrennten Gleisabschnitt benutzen. Bei ausgeschalteter CS3 ausschließlich den vorgesehenen Prüfausgang anschließen. TK-A allein aufsetzen; TK-B und Wagen bleiben zunächst abgestellt.
2. U/O auf die geprüfte Stellung U setzen. Decoder erst nach bestandener Isolation einstecken. Dann einschalten und die mfx-Anmeldung abwarten. Nur dieser eine Decoder wird neu eingebaut. [Q1]
3. Den angemeldeten Datensatz prüfen und sinnvoll als ICE 2976 benennen. Die mfx-Anmeldung erkennt den Decoder, nicht automatisch das umgebaute Gehäuse, den tatsächlichen Motorsatz oder eine passende Höchstgeschwindigkeit.
4. Decodereinstellungen auslesen und sichern. Für den 60941 das HLA-/C90-Motorprofil verwenden. In der DCC-Tabelle des 60972 entspricht dies Motortyp 3 in CV52; unter mfx die entsprechende Motoreinstellung wählen. Keine fremden kompletten CV-Sätze blind übernehmen. [Q1]
5. Höchstgeschwindigkeit für die erste Fahrt begrenzen. Mit kleiner Fahrstufe die tatsächliche Bewegungsrichtung prüfen. Läuft TK-A entgegen der hier definierten Vorwärtsrichtung, ausschließlich die Motorzuordnung korrigieren: entweder die Motor-Invertierung passend einstellen oder bei abgeschalteter Versorgung grün/blau an den Motorzweigen vertauschen. Nicht gleichzeitig mehrere Richtungsparameter ändern.
6. Im vorgesehenen rein digitalen Betrieb kann die Analogerkennung dieses Decoders deaktiviert werden. mfx bleibt eingeschaltet. Keine globalen CS3-Protokolle abschalten, die andere Fahrzeuge benötigen.

Menübezeichnungen können vom Softwarestand abhängen. Verbindlich sind das gewählte Motorprofil und die nachfolgenden Schaltbedingungen, nicht eine erfundene feste Klickfolge.

### F0-Mapping am motorisierten Kopf

| F0 | Gewählte Zugrichtung | LV grau | LR gelb | Licht an TK-A |
|---|---|---|---|---|
| Aus | Beliebig | Aus | Aus | Dunkel |
| Ein | TK-A voraus | Ein | Aus | Weiß |
| Ein | TK-B voraus | Aus | Ein | Rot |

Beide Richtungszuordnungen gelten im Stand und in Fahrt. Ausgänge als normales Licht konfigurieren, ohne Blink-, Kupplungs- oder Timerfunktion. AUX1/AUX2 werden nicht wie in REV16 zur hinteren Beleuchtung gemappt. Kein zweiter Decoder und keine Traktion werden angelegt.

### Einmessfahrt erst später

Eine automatische Motor-Einmessfahrt gehört nicht auf einen kurzen Tischabschnitt. Sie kann stark beschleunigen. Für den späteren Abgleich muss eine ausreichend freie Strecke beziehungsweise ein geeignetes Oval vorbereitet werden; Märklin nennt dafür Radien über 430 mm. Erst nach fehlerfreiem mechanischem und elektrischem Grundtest erwägen. [Q1]

## 14. Abnahme in getrennten Stufen

| Prüfung | Sollverhalten / Dokumentation |
|---|---|
| Motor ohne Decoder | Freier Lauf, keine Bürste direkt mit Chassis oder Stromabnehmer verbunden. |
| U/O, Verbraucher abgetrennt | Genau ein ausgewählter Versorgungseingang mit S verbunden; keine unbeabsichtigte Quellenbrücke. |
| TK-A allein | Ein mfx-Datensatz, ruhiger langsamer Lauf, keine ungewöhnliche Erwärmung oder Abschaltung. |
| F0 aus | TK-A dunkel. Dies ist noch keine Abschaltung von TK-B oder Mittelwagen. |
| F0 ein, TK-A voraus | TK-A weiß; nach entsprechender Radbewegung TK-B rot. |
| F0 ein, TK-B voraus | TK-A rot; nach entsprechender Radbewegung TK-B weiß. |
| Richtungsbefehl im Stillstand | TK-A wechselt sofort; TK-B hält bis zur Radbewegung seinen mechanischen Zustand. |
| TK-B von Hand verschoben | Licht folgt der tatsächlichen Bewegung, nicht einer CS3-Adresse. |
| Versorgung aus/ein | TK-B-Zustand nachhalten und bei Bedarf durch kurze Bewegung korrekt setzen; keinen elektronischen Richtungsspeicher unterstellen. |
| Mittelwagen einzeln ergänzen | Vorhandenes Licht bleibt versorgt; keine neue elektrische Verbindung zu Decoderausgängen. |
| Kurven/Gegenkurven | Alle Drehgestelle schwenken frei, keine gequetschten Leitungen oder Kontaktkurzschlüsse. |
| Gehäuse montiert | Sämtliche Isolations- und Funktionsprüfungen wiederholen; Lichtleiter richtig ausgerichtet. |
| Pantograph, separater kontrollierter Test | Funktion in O-Stellung aus nur einer geeigneten Digitalquelle; nicht mit fremdem Trafo parallel. |

Die erste Fahrprobe erfolgt langsam und unter Aufsicht. Bei Brummen ohne Bewegung, stockendem Lauf, Geruch, ungewöhnlicher Erwärmung oder Kurzschlussmeldung sofort abschalten. Eine Decoder-Schutzschaltung ist kein Ersatz für die vorherige Prüfung.

**Wichtig für Signal-/Halteabschnitte:** Der Motor wird im Grundumbau von TK-A versorgt, nicht automatisch vom jeweils führenden Kopf. Der mechanische hintere Lichtwechsel ist keine Schleiferumschaltung. Bei geschobenem Zug kann der motorlose führende Kopf deshalb in einen Abschnitt gelangen, bevor der motorseitige Stromabnehmer ihn erreicht. Abschnittsgrenzen und Haltepunkte entsprechend prüfen; eine zusätzliche automatische Schleiferwahl ist hier nicht eingebaut.

Abgeschlossen ist der Umbau erst nach protokollierter Prüfung am Fahrzeug. Offene Messstellen dürfen nicht durch einen pauschalen Vermerk „geprüft“ ersetzt werden.

## 15. Option: eine Taste schaltet den ganzen Zug dunkel

Diese Option ist **nicht im Grundumbau enthalten**. Sie kann mit einem Decoder und ohne CS3-Traktion entworfen werden, setzt aber einen gemeinsamen elektrischen Steuer- oder Versorgungsweg voraus. Stromführende Kupplungen können äußere Kabel ersetzen; sie ersetzen nicht die elektrische Durchleitung innerhalb jedes beteiligten Fahrzeugs.

Ein möglicher Ausbauweg ist ein geeigneter, vom 60972-AUX-Ausgang betätigter Relaiskontakt, der einen vom Decoder-Ausgang getrennten Licht-Versorgungsleiter schaltet. Dieser Leiter versorgt über geeignete Kupplungen die Wagenbeleuchtung und die örtliche hintere LED-Schaltung. Die vorhandenen Achskontakte können weiterhin die Rückleitung 0 liefern. Der Relaisantrieb wäre für gemeinsame Abschaltung auf F0 in beiden Richtungen zu legen; LV/LR bleiben getrennt richtungsabhängig. Eine Freilaufbeschaltung und die Auslegung von Relais, Kontaktstrom und Gesamtlampenlast gehören dann in einen eigenen Schaltplan.

**Dabei dürfen örtliche Dauer-B-Einspeisungen den geschalteten Lichtleiter nicht parallel weiter speisen.** Solche Anschlüsse müssten entsprechend getrennt oder umgeschaltet werden. Sonst bleiben Lichter trotz ausgeschaltetem Relais an und es drohen unerwünschte Verbindungen zwischen Gleisabschnitten. Achskontakte erhalten und sämtliche lokalen Mittelschleifer unverändert auf dieselbe Lichtleitung schalten sind zwei verschiedene Forderungen.

Sollen alle bisherigen örtlichen Stromquellen unverändert aktiv bleiben, wären stattdessen örtliche Schaltelemente mit einem gemeinsamen Steuersignal erforderlich. Das ist ein anderer, aufwendigerer Ausbau. Keine der Varianten wird als vollständig verbindungslos verkauft. Direkte Wagenlast an einen AUX-Ausgang oder das Zusammenlöten von LV und LR ist kein Ersatz für die Auslegung.

Ein zweiter mfx-Decoder besitzt eine eigene Identität. Gleiche DCC-Adressen machen daraus keinen gemeinsamen mfx-Teilnehmer. Ein nur auf DCC konfigurierter Decoder reagiert außerdem nicht automatisch auf die mfx-Befehle des ersten. Deshalb wird hier keine angeblich automatische Zweidecoder-Synchronisation zugesagt. Für den gewünschten Hauptweg ist ein zweiter Decoder weder vorgesehen noch erforderlich. [Q1; Ausbaukonzept: eigene Ableitung]

## 16. Noch gezielt zu schließen

| Offener Punkt | Benötigter Nachweis | Was nicht nochmals fehlt |
|---|---|---|
| Austausch-Lichtwechselbaugruppe | Konkreter Lieferumfang, Vergleich der Aufnahme und reproduzierbare Betätigung am eigenen TK-B. | Gesamtunterseite des vorhandenen TK-B ist bereits dokumentiert. |
| C/W/R und Massebezug | Messwerte und markierte Kontaktstellen der tatsächlich eingebauten Ersatzbaugruppe. | Die lange Bestandsplatine 62762 allein liefert diesen Nachweis nicht. |
| U/O im eigenen Motorträger | Gemessene Eingänge U/O und gemeinsamer Ausgang S-A, einschließlich Pantographenkontakt bei montiertem Gehäuse. | Bedeutung der Markierung wird nicht mit Lichtwechsel verwechselt. |
| Endgültige LED-Helligkeit | Belastbare Daten des gelieferten Farbzweiges und daraus abgeleitete Widerstände. | Vorwiderstände sind bereits vorgesehen; 47 kOhm ist ausdrücklich die Startbestückung. |
| Wagenversorgung bei Erhaltung | Tatsächlichen zweiten Versorgungsleiter neben den Achskontakten verfolgen, bevor alte Kopfanschlüsse entfallen. | Kein Auftrag zum vollständigen Mittelwagen-Neubau. |

Diese Punkte sind Prüfstellen innerhalb der Anleitung, keine Begründung für einen erneuten allgemeinen Systemwechsel zu LoDi-Motorplatinen, Sound oder einer CS3-Traktion.

## 17. Quellen und Aussagegrenzen

Abruf und Abgleich: 17.09.2026. Herstellerzeichnungen und relevante Tabellen wurden einschließlich der Abbildungen geprüft. Eigene Anschlussentwürfe, Widerstandsrechnung und Prüfabläufe sind von Herstellerbelegen zu unterscheiden.

- **Q1 – Märklin 60972/60982:** [Herstelleranleitung](https://static.maerklin.de/damcontent/93/1d/931db48faf5660916556d5172c598cdf1663856135.pdf). Relevant: Anschlüsse/Farben auf Druckseiten 5–6, mfx und Einmessen auf 7–8, Motorprofil in der DCC-Tabelle auf 17. Keine fahrzeugspezifische 2976-U/O-Padbelegung.
- **Q2 – Märklin 60941/60943:** [Montagezeichnung](https://static.maerklin.de/damcontent/e3/bb/e3bb202fe80385cc96835d783af5e1821670919973.pdf). Teilefolge des Motorumbaus; keine eigene Fahrzeugfotografie.
- **Q3 – Lokstoredigital:** [ICE-1-Umbau am Beispiel 33701](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/). Vergleich für mechanische Arbeit, Entstörung und LED-Anschlüsse. Die dortige LoDi-Gesamtplatinenlösung wird hier ausdrücklich nicht übernommen.
- **Q4 – Märklin:** [60941-Produktbeschreibung](https://www.marklin.nl/producten/details/article/60941). Trommelkollektor-Umrüstung mit fünfpoligem Antrieb.
- **Q5 – Lokstoredigital:** [Frontmodule im Herstellershop](https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/), Abschnitt „LoDi-WiB ICE-M Front 2 Stück“. Frontmodule ohne Vorwiderstände; dort keine vollständigen zulässigen Zweigstromdaten gefunden.
- **Q6 – Märklin:** [Ersatzteilzeichnung 33701/37701/39711](https://static.maerklin.de/damcontent/c7/9c/c79c321455edb84f118a74a9c58838611434542615.pdf), insbesondere PDF-Seiten 2–3. Belegt Baugruppen des Vergleichsmodells, nicht die unmittelbare Nachrüstpassung am 2976.
- **Q7 – Projektbefund:** [Befund_2976_Originalzustand.md](../Arbeitsstand_Hobby_Befund/Befund_2976_Originalzustand.md), einschließlich Originalfotos IMG_0636–IMG_0646 und dokumentierter Messberichte. Aussagen über den Nutzerzug stammen aus diesem Befund; keine neue physische Begutachtung behauptet.
- **Q8 – Historische Alternative:** [REV16-Anleitung](../Arbeitsstand_REV16/Anleitung_Inhalt.md) und [REV16.1-Detailgenerator](../Arbeitsstand_REV16_1/build_detail.py). Elektrische Zweipol-Kupplungsvariante; nicht der aktuelle verbindungslose Grundumbau.
- **Q9 – Vishay:** [1N4148-Datenblatt](https://www.vishay.com/docs/81857/1n4148.pdf). Kathodenkennzeichnung und Diodeneigenschaften. Die hier beschriebenen LED-/Schalterschaltungen sind keine vom Diodenhersteller geprüfte Fahrzeuganwendung.
