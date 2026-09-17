# Elektrischer Hauptweg: originale 62762, 60977 vorn, 59649 hinten

Arbeitsstand 12.09.2026. Dieser Vorschlag ersetzt ausschließlich die LoDi-Motorplatinen 511. LoDi-Front 514 und Wagenplatinen bleiben. Er ist eine konkrete Verdrahtungsvorlage; reale Fahrzeugmessungen wurden nicht vorgetäuscht. Die mit **Auslegung** bezeichneten Verbindungen sind unsere Schaltungsentscheidung, keine behaupteten originalen Leiterbahnfunktionen.

## 1. Originalplatine tatsächlich behalten

62762 / 03/92 / VER1.1 ist auf den untersuchten Bildern eine passive Träger-/Verteilerplatine mit Schiebeschalter. Der mechanische Fahrtrichtungsumschalter darunter ist ein eigenes Bauteil. Daraus folgt weder eine elektronische Schleiferumschaltung noch die Notwendigkeit irgendwelcher Kupferschnitte. Die daneben angebotene bestückte 62761 darf nicht als Schaltplan der 62762 verwendet werden. [Originalfotos beider Seiten](https://www.ebay.de/itm/147416253187)

1. Zug vollständig von Schienen, Oberleitung und Prüfgeräten nehmen; jeden vorhandenen Speicher einzeln entladen und direkt an seinen Anschlüssen Spannungsfreiheit prüfen. Anschlüsse fotografieren und nach ihrem tatsächlichen Ziel beschriften.
2. Den externen analogen Fahrtrichtungsumschalter samt zugehörigen Verbindungen ausbauen. Die 62762 bleibt erhalten. Schleifer, Radmasse, Motor, Frontlicht und Kupplungsadern zunächst von ihren bisherigen gemeinsamen Verbindungen lösen; freie Enden einzeln isolieren. Alte Fassungen für den LED-Umbau ausbauen.
3. Originalkupfer nur als passiven Verteiler weiterverwenden: bei vollständig abgetrennten Außenadern jedes gewünschte Lötaugenpaar im Ohmbereich prüfen; Sollwert einer Kupferverbindung nahe dem zuvor gemessenen Messleitungswiderstand. Gegenseitig getrennte Netze sowie Schrauben/Chassis in beiden Schalterstellungen prüfen. Zuordnung direkt auf dem eigenen Foto eintragen. Ein Befestigungsauge mit Kupfer kann durch die Schraube Massekontakt bekommen.
4. Nur ein solcher nachgewiesener Pfad darf beispielsweise zum neuen Verteiler **B-Zug** werden. Diese Bezeichnung wird erst nach der Messung vergeben; sie ist keine historische Padbelegung. Für U+, Licht und Motor sind direkte, isolierte Leitungen der Hauptweg. Leiterzüge bleiben ungeschnitten. Den ursprünglichen Schiebeschalter elektrisch unbenutzt lassen; Oberleitungszuleitung einzeln isolieren.
5. 21MTC-Träger und Relais auf isolierenden Abstandhaltern über/an der erhaltenen Originalplatine befestigen. Schrauben dürfen kein zusätzliches Netz verbinden. Bei ungeeignetem Kupferpfad stattdessen einen isolierten Drahtverteiler auf der 62762 befestigen; die Originalplatine wird weiterhin als Träger benutzt und nicht gegen eine Blankoplatte ausgetauscht.

## 2. Stromversorgung und zwei Kupplungspole

**Auslegung:** Einziger einspeisender Mittelschleifer ist der motorisierte Kopf. Der hintere Schleifer wird mechanisch entfernt oder sein Anschluss vollständig isoliert. Das verhindert eine leitende Verbindung zweier Mittelleiterabschnitte durch den Zug. Es ist keine fahrtrichtungsabhängige Schleiferumschaltung; signalabhängige Abschaltstrecken benötigen hierfür ein eigenes Konzept.

Zwei Kupplungsleiter bleiben: **B-Zug** führt den unveränderten Mittelleiter zum hinteren Decoder und zu den Wagen; **L-Zug** führt die durch einen potentialfreien Relaiskontakt geschaltete Beleuchtungsspannung. Rückleiter der Wagen sind deren Radmassefedern. Daher müssen für diesen Hauptweg zuvor entfernte Wagen-Massefedern wieder eingesetzt und elektrisch angeschlossen werden.

Die LoDi-Standardbelegung lautet L = Licht schalten, O = Radmasse, B = Mittelleiter. Nur mit der entfallenden LoDi-Motorplatine nennt der Hersteller O = Mittelleiter und B = optionale Radmasse. **Diese alte REV13-Belegung vollständig zurückbauen.** Farben allein identifizieren keinen Kupplungspol. [LoDi, Abschnitt Einbau und Anschlusslegenden](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-wib-ice-m/)

**Evidenzgrenze:** Die Standardlegende benennt L nicht ausdrücklich als „geschalteten Mittelleiter“. Unsere Relaisversorgung von L ist eine aus Standardanschluss und passivem Lichtschalten abgeleitete Schaltungsentscheidung. Sie wird zuerst an genau einer eigenen Wagenplatine geprüft. Sie ist kein fotografisch nachgewiesener Originalschaltplan der 2976.

## 3. Verdrahtungstabelle

Hier gelten Märklin-Farben an Märklin-Trägerplatinen. Bei einer anderen Trägerplatine zählt deren beschriftete Funktion. Insbesondere ist ESU-blau am Kabeldecoder U+, Märklin-blau dagegen Motor: Farben niemals übertragen.

| Ausgangspunkt | Ziel | Ausführung / Kontrolle |
|---|---|---|
| Vorderer Mittelschleifer | 60977-Träger rot und B-Zug | Zwei dokumentierte Abzweige; Originalkupfer nur nach Abschnitt 1 |
| Vordere Rad-/Chassismasse | 60977-Träger braun | Sicheren Radkontakt auch bei bewegtem Drehgestell prüfen |
| 60977-Träger grün / blau | Beide isolierten 60941-Motoranschlüsse | Jeweils vorgesehene Motordrossel; steckbaren Motor-Servicezugang vorsehen |
| 60977-Träger orange, U+ vorn | Plus der vorderen LoDi-Front und Relais-Eingang + | Ausschließlich Decoderplus, keine Fahrzeugmasse |
| 60977-Träger grau, Licht vorn | Eigener Serienwiderstand → weißer Frontzweig | Widerstandsauslegung Abschnitt 5 |
| 60977-Träger gelb, Licht hinten | Eigener Serienwiderstand → roter Frontzweig | Keinen gemeinsamen Widerstand im Plusdraht verwenden |
| 60977 AUX1, braun/rot | Relais-Eingang − | Ungedimmter Dauer-Ausgang; nicht an Kupplung oder Wagen-L |
| B-Zug | Relaiskontakt COM | Potentialfreier Lastkontakt, getrennt von Spuleneingang |
| Relaiskontakt NO | L-Zug | NC bleibt einzeln unbeschaltet; NO schließt nur bei eingeschaltetem Relais |
| B-Zug | Wagenplatine B, alle Wagen | Unveränderter Mittelleiter; durch alle Kupplungen verfolgen |
| L-Zug | Wagenplatine L, alle Wagen | Geschalteter Lichtbus; keine Verbindung zu irgendeinem Decoder-U+ |
| Jeweilige Wagen-Radmassefeder | Wagenplatine O | Standardbelegung, nicht mehr LoDi-511-Belegung |
| B-Zug / hintere Radmasse | Hinterer 21MTC-Träger rot / braun | Hinterer Schleifer bleibt isoliert |
| Hinterer Träger orange | Plus der hinteren LoDi-Front | U+ hinten bleibt vollständig getrennt von U+ vorn |
| Hinterer Träger grau, Licht vorn | Eigener Widerstand → roter hinterer Frontzweig | Bei gemeinsamer Zug-Vorwärtsrichtung hinten rot |
| Hinterer Träger gelb, Licht hinten | Eigener Widerstand → weißer hinterer Frontzweig | Bei gemeinsamer Zug-Rückwärtsrichtung hinten weiß |
| Alle übrigen Decoderleitungen | Keine Verbindung | Einzeln isolieren, insbesondere hintere Motoranschlüsse |

Der 59649 ist ein **LokPilot 5 MKL mit Motorendstufe**, kein LokPilot Fx. Er wird hinten nur für Funktionen eingesetzt. Seine unbenutzten Motorleitungen werden einzeln isoliert. Eine vollständige vorhandene 60972-Packung kann die zusätzliche Märklin-21MTC-Trägerplatine liefern; der 60972-Decoder wird dafür abgezogen. 60982 stellt nicht automatisch dieselbe Schnittstelle bereit. [ESU LokPilot-5-Handbuch, Typübersicht und 21MTC](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/)

## 4. Relais: praktikabler Hauptkandidat und Test

**Fertig beschalteter Hauptkandidat:** ML-Train 84002016, Originalentwickler mXion 0016. Der Hersteller nennt 10–24 V, etwa 15 mA, 2-A-Relais, Schutzdiode und ca. 32 × 15 × 15 mm. Vor Bestellung den freien Bauraum mit einer Pappschablone einschließlich Kabelabgängen prüfen. Der mXion-Katalog bestätigt Decoderanschluss und Spannungsbereich. [ML-Train Originalprodukt](https://www.ml-train.de/herzstck-relaisplatine-weichen-train-84002016-p-531.html), [mXion-Katalog, Artikel 0016](https://micron-dynamics.de/Presse/mXionProduktkatalog.pdf)

Die [mXion-LSD-Anleitung S. 35–36](https://www.micron-dynamics.de/sitecake-content/mXion%20LSD.pdf) zeigt die konkrete Lage: Blick auf Bauteilseite, zweipolige Klemme oben: **oben links U+, oben rechts Funktionsausgang**. Dreierklemme unten: **Mitte HRZ = COM an RT; links GL1 = Schließer an GE; rechts GL2 frei**. Die gelieferten Klemmen müssen zum Bild passen. Polarität der Schutzdiode beachten. Den zweiten Kontakt nicht parallel schalten.

Das Relais zuerst ohne Wagen und ohne Verbindung des Lastkontakts zu B-Zug betreiben. AUX1 auf normales Ein/Aus, 100 % Helligkeit, ohne Blinken oder Kupplungstimer einstellen. Prüfleitungen stromlos anklemmen; DC-Spannung zwischen Relais + und − bei AUX1 EIN muss im dokumentierten 10–24-V-Bereich liegen. Dabei müssen Zentralen-/Netzteilunterlagen den gewählten Betriebsbereich abdecken; ein DMM-Mittelwert allein belegt keine beliebige Spitzenspannung. Die Spulenversorgung ist gleichgerichtete Decoderspannung, nicht direkt gemessene Digitalgleisspannung.

Kontakttest ohne Ohmmessung an einem versorgten Fahrzeug: eine getrennte kleine Batterie mit geeignetem Prüflämpchen als eigenständigen Prüfkreis nur über COM/NO führen. EIN muss schließen, AUS öffnen. Danach alle Quellen entfernen und den Batterieprüfkreis vollständig abbauen; erst dann den Lastkontakt nach Tabelle verdrahten. Kontakte gegen Spuleneingang bleiben elektrisch getrennt. Das akustische Klicken allein bestätigt keinen richtigen Kontakt.

**ESU 51963 nicht ungeprüft substituieren:** Die aktuelle Produktzeile nennt 16 V, die ESU-Katalog-Anschlussgrafik bezeichnet das Relais als 24 V. Das lässt sich aus den öffentlich gelesenen Unterlagen nicht eindeutig auflösen; deshalb wird daraus keine Universal-Spulenfreigabe abgeleitet. [ESU Originalseite](https://www.esu.eu/produkte/zubehoer/miniatur-relais/)

## 5. Front-LEDs: Widerstände gehen mit 511 verloren

LoDi dokumentiert Weiß = grau, Rot = gelb und gemeinsames Plus = braun/orange. R4/R5 sitzen auf der entfallenden Motorplatine und sind die dort vorgesehenen LED-Vorwiderstände. Deshalb braucht **jeder Farbzweig an jedem Kopf** einen eigenen externen Widerstand. Front-Plus kann braun aussehen und darf trotzdem nicht an Radmasse. [LoDi ICE-1-Umbau, Front und R4/R5](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/)

**Eigene konservative Grundauslegung:** Pro Farbe einen externen **47-kΩ-Widerstand, 5 % oder besser, mindestens 0,25 W** verwenden, insgesamt vier Stück. Diese Auslegung gilt bei belegtem `U_max ≤24 V` am jeweiligen Zweig. `R_min = 47000 × 0,95 = 44650 Ω`; daraus folgt ohne LED-Flussspannungsabzug `I_max ≤24/44650 = 0,538 mA`, Widerstandsverlust höchstens 12,9 mW. Jeden Widerstand vor Einbau nachmessen: bei 5 % sind 44,65–49,35 kΩ richtig. Aufdruck 473 bedeutet 47 kΩ, nicht 4,7 kΩ.

Das ist unsere absichtlich stromarme Grundbeschaltung, **keine behauptete LoDi-Nennstromfreigabe**. Sie kann deutlich dunkler leuchten. Der Spannungsbereich muss aus der konkreten CS3-/Netzteilkonfiguration begründet sein; ein beliebiger DMM-Mittelwert bestätigt keine Spitzengrenze. Die dokumentierte LoDi-Polung wird vor Anschluss übernommen. Kein direkter LED-Test an Gleis oder Decoder.

Je Farbe separat ungedimmt einschalten und den DC-Spannungsabfall über dem zugänglichen Widerstand messen. Mit dessen zuvor gemessenem Wert gilt `I_mittel=U_R/R`; Beobachtung muss unter 0,538 mA bleiben. Das DMM kontrolliert den Betrieb, die obere Begrenzung stammt aus Widerstand und belegter Versorgung. Beide Kopfgehäuse aufsetzen und Helligkeit bewerten.

Wird helleres Licht gewünscht, **keinen Widerstand auf Verdacht verkleinern**. Dann einen belegten zulässigen LED-Zweigstrom verwenden: `R_nom ≥ U_max / (I_zul × (1−t))`; `t` ist Toleranz. Widerstandsbelastbarkeit mit Hersteller-Temperaturreserve aus `P_max=U_max²/R_min` wählen. Eine passende dokumentierte Front-/Widerstandskombination ist ebenfalls möglich. Weder 25 V noch 5 mA sind bekannte Daten der vorliegenden Front. Der begrenzte 47-kΩ-Grundaufbau kann während dieser späteren Optimierung unverändert bleiben.

## 6. DMM-Prüfung und stufenweise Inbetriebnahme

1. Ohne Decoder, Fronten und Wagenplatinen zunächst ausschließlich den Kabelbaum prüfen: B-Zug und L-Zug jeweils vom Kopf bis zum letzten Kupplungsende niederohmig; gegeneinander und gegen Radmasse offen. Prüfung bei beiden Kupplungslagen, geschwenkten Drehgestellen und später aufgesetzten Gehäusen wiederholen. Prüfleitungen vor/nachher kurzschließen, damit eine defekte Messleitung nicht als „offen“ gilt.
2. Motor von beiden Decoderleitungen abziehen. Beide Motoranschlüsse gegen Chassis/Radmasse offen; mehrere Rotorlagen prüfen. Zwischen Motoranschlüssen Wicklungswiderstand erwarten, nicht „offen“. Trennbare Motorleitung bis nach endgültigem Gehäuseschluss von außen erreichbar lassen.
3. Vordere Decoderstufe allein: Anmeldung, langsame Fahrt beider Richtungen, Licht zunächst abgeklemmt; danach Relais gemäß Abschnitt 4. Märklin-Grenzen: Motor 1,1 A; jeder verstärkte Licht-/AUX-Ausgang 250 mA, zusammen 300 mA, Decoder gesamt 1,6 A. Der Wagenstrom läuft **nicht** durch AUX1. [Märklin 60977, technische Daten](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf)
4. **Begrenzter Erstwagenversuch:** Genau einen Wagen ohne Zusatzpuffer allein auf eine isolierende Unterlage legen; sämtliche Räder bleiben fern von Gleisen/Metall, keine weitere Kupplung. B an RT, L an GE; als einzigen Rückweg O über **1 kΩ/2 W, 5 %** zur Radmasse des vorderen Kopfes führen. Bei belegter Gleisspannungsspitze ≤24 V begrenzt dies den Gesamtstrom auf höchstens 25,3 mA (Widerstandsverlust höchstens 0,607 W). AUX1 AUS/EIN/AUS muss eindeutig schalten. Dunkelheit ist wegen des Spannungsabfalls kein Beweis eines Platinenfehlers; Widerstand nicht blind überbrücken. Erst nach bestandenem Versuch stromlos alle Prüfadern und Testwiderstand abbauen, O wieder ausschließlich über die eigene Radmassefeder versorgen und den Wagen normal aufgleisen. Dann T1–T8 wiederholen. Keine Poltauschversuche unter Spannung.
5. Erst nach bestandenem Einzelwagen weitere Wagen einzeln ergänzen; jede Stufe bei CS3 STOP ankoppeln. Helligkeit am Wagenpotentiometer einstellen. Grundprüfung ohne zusätzliche Speicher; LoDi nennt eine interne sanfte Ladeschaltung. Neue Speicher erst nach erfolgreichem Grundbetrieb einzeln hinzufügen.
6. Lastprüfung im Originalbetrieb: keine Kurzschlussmeldung, kein Relaisschnarren, kein Spannungseinbruch mit flackernden Wagen; Leitungen, Kupplungen und Relais auf ungewöhnliche Erwärmung prüfen. Herstellergrenzen von Relais, Kupplungen und Leitungen gelten gemeinsam. Ein beliebiger DMM-AC/DC-Wert an Digitalgleisspannung ist kein gesicherter Wagenstrom; ein Mittelwert ist kein Einschaltspitzennachweis. Die Entlastung des AUX entsteht durch die physische Relaistrennung, nicht durch eine erfundene Prozentreserve.
7. Nach endgültigem Schließen den isolierten Motorzweig über den vorbereiteten Servicezugang nochmals gegen Masse prüfen. Erst danach außen wieder verbinden und sichern. Wird erneut geöffnet oder intern eine Leitung bewegt, die betroffenen Endprüfungen wiederholen. Schließlich beide Fahrtrichtungen, F0-Wechsel, Wagenlicht EIN/AUS und langsame Kurvenfahrt mit dem vollständig gekuppelten Zug prüfen.
