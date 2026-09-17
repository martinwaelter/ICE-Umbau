# Originalplatine 62762: Decoderträger, Anschluss und Programmierübernahme

Stand 12.09.2026. Begrenzter Fachbeitrag zur separaten vollständigen Anleitung ohne LoDi-Motorplatine 511. Referenz für Seitennummern: `Arbeitsstand_REV13/rev13_pages.json`, finale 46-Seiten-Fassung. Die Hauptanleitung und ihre Dateien wurden nicht geändert.

**Verbindliche Decoderwahl nach aktueller Nutzerentscheidung:** 60941-Motor, 60977 mit Sound vorn und 59649 hinten; gemeinsamer mfx-Zugeintrag nach dem nachgewiesenen REV13-Verfahren. 60972/60982 sind vorhanden; der Nutzer hat 60977 bestellt. 59649 bleibt geplant, sein Besitz ist noch nicht bestätigt. Der Hauptaufbau nutzt die Trägerplatine aus dem vorhandenen 60972-Satz; der 60972 selbst ersetzt den Sounddecoder nicht. Vollständigkeit und Zustand des Satzes werden am Arbeitsplatz festgestellt. Es besteht keine offene Frage mehr, ob der Hauptweg auf zwei mLD3 umgestellt werden soll.

## 1. Belastbare Zuordnung der zwei Träger

**Bevorzugter Aufbau:** Der 60977 erhält vorn seine eigene originale Trägerplatine. Hinten nimmt die originale Trägerplatine aus dem 60972-Satz den 59649 auf. Damit benötigt diese Variante bei vollständigen Sätzen keine zusätzlich angenommene Adapterplatine und keinen neu identifizierten Lautsprecher-Gegenstecker. Die langen Originalplatinen können als mechanische Träger und ausschließlich mit nachgewiesenen Netzen weiterverwendet werden; sie ersetzen die kleinen 21MTC-Aufnahmen nicht.

Die aktuellen Herstellerunterlagen zeigen:

| Merkmal | 60977-Träger | 60972-Träger | Belastbare Folgerung |
|---|---|---|---|
| Grundanschlüsse | +Ub, LV/LR, MR/MV, B/GR, 0/GL, AUX1–4, GND, +5V | Dieselbe beschriftete Anordnung | Die vorgesehenen Grundfunktionen sind vergleichbar. |
| SUSI | Vierpolige Buchse in der Trägerzeichnung | Vierpolige Buchse, ausdrücklich als SUSI beschriftet | Hinten mit 59649 bleibt sie frei. |
| Lautsprecher | Zweipolige Buchse, ausdrücklich bezeichnet | Die Zeichnung zeigt ebenfalls eine zweipolige Buchse mit Lautsprechersymbol | „60972-Träger hat keine Lautsprecherbuchse“ wäre unbelegt bzw. widerspricht der Zeichnung. Eine vorhandene Buchse verleiht dem mLD3 keinen Sound. |
| Lieferumfang | Ein Träger und Halter; Satzlautsprecher vorhanden | Ein Träger und Halter; kein Sounddecoder | Ein leerer Ersatzträger aus dem Satz ist kein zweiter Decoder. |

Visuell verglichen: [Märklin 60977, S. 3–6](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf) und [Märklin 60972/60982, deutsche Fassung S. 3, 5–6](https://static.maerklin.de/damcontent/da/e4/dae4fa90473657b9466d908bd6dcfa601663856106.pdf). Die Produktseiten bestätigen jeweils einen beiliegenden 21MTC-Träger: [60977](https://www.marklin.com/products/details/article/60977), [60972](https://www.marklin.com/products/details/article/60972).

**Reichweite:** Die Zeichnungen belegen dieselbe Anschlussbauart, nicht eine verifizierte identische Ersatzteilnummer oder jede jemals ausgelieferte Revision. Für den gewählten Aufbau wird eine Soundnutzung des 60972-Trägers nicht benötigt. Im Leitfaden dürfen daher weder eine abweichende Bestückung erfunden noch sämtliche Träger allein wegen der Satznummer als identisch freigegeben werden. An den realen Teilen stimmen Beschriftung, freie 21MTC-Stiftleiste, Index, Stecker und Befestigung mit der jeweiligen Zeichnung überein; vorhandene Umbauten werden gesondert erfasst.

## 2. Anschlussmatrix für die Hauptvariante

Die Pins dienen der Gegenprüfung am **leeren**, vollständig stromlosen Träger. Sie sind keine Aufforderung, an Stifte oder Decoderkontakte zu löten. Verwenden werden die vorgesehenen Trägerleitungen bzw. Lötflächen. Die Zählrichtung wird anhand Herstelleransicht und Index 11 bestimmt, nicht aus einer frei gedrehten Fotoansicht geraten.

| 21MTC-Pin | Trägerbezeichnung / Märklin-Farbe | Vorn: 60977 | Hinten: 59649 |
|---:|---|---|---|
| 22 | B/GR / Rot | Bestätigter Gleis-Mittelleiterweg | Nur RT vom vorderen Schleifer; alte hintere Schleiferleitung vom Netz trennen und einzeln isolieren |
| 21 | 0/GL / Braun | Örtlicher Rad-/Schienenrückleiter | Örtlicher Rad-/Schienenrückleiter |
| 16 | +Ub / Orange | Eigener gemeinsamer Plusanschluss U+ vorn | Eigener U+ hinten; niemals mit vorderem U+ verbinden |
| 8 | LV / Grau | Weißer Frontzweig über eigenen Widerstand | Roter Frontzweig über eigenen Widerstand |
| 7 | LR / Gelb | Roter Frontzweig über eigenen Widerstand | Weißer Frontzweig über eigenen Widerstand |
| 19 | MV / Grün | Motorzweig 1 über Drossel; Richtung später prüfen | Unbenutzt, freie Leitung einzeln isolieren |
| 18 | MR / Blau | Motorzweig 2 über Drossel; Richtung später prüfen | Unbenutzt, freie Leitung einzeln isolieren |
| 15 | AUX1 / Braun-Rot | Ansteuerung der vorgesehenen Innenlicht-Relaisspule; Wagenlast läuft über den Relaiskontakt | Unbenutzt, freie Leitung einzeln isolieren |
| 14 / 13 / 4 | AUX2 / AUX3 / AUX4 | Nur eine tatsächlich geplante Funktion anschließen | Unbenutzt, freie Leitungen einzeln isolieren |
| 20 / 12 | GND / +5V | Kein Lampen-, Motor- oder Schienenanschluss | Frei lassen |
| 9 / 10 | Lautsprecherpfad | Ein Satzlautsprecher an die vorgesehene Trägerbuchse | Beim 59649 unbelegt; Buchse frei lassen |
| 5 / 6 | SUSI-Takt / -Daten | Für eine spätere dafür geeignete Erweiterung | SUSI-Buchse frei lassen |

Die verwendeten Anschlussnummern sind durch die [ESU-Anleitung, S. 19, Abb. 3](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e) und [RCN-121, S. 6–9](https://normen.railcommunity.de/RCN-121.pdf) gedeckt; Märklin-Farben und Padnamen durch die oben verlinkten Märklin-Zeichnungen. Der 59649 besitzt **verstärkte AUX3/AUX4**, Pins 9/10 sind bei diesem Artikel unbelegt. Eine beliebige andere 21MTC-Platine mit Zusatzverstärkern wird hiermit nicht freigegeben. Die 21MTC-Norm allein ersetzt die artikelspezifische ESU-Belegung nicht.

**Elektrische Ableitung für den gewählten hinteren Aufbau:** Er benötigt nur die beiden Gleiseingänge, U+, LV und LR; die originalen Märklin-Träger führen diese Funktionen entsprechend heraus. Die Kompatibilität für diesen begrenzten Einsatz ist damit gut begründet. Eine pauschale ESU-Herstellerfreigabe mit der konkreten Märklin-Träger-Ersatzteilnummer wurde nicht gefunden. Vor Fahrzeugstrom bleiben Kontaktzuordnung, Isolation und realer Steckversuch verpflichtend.

Die Farbmatrix gilt für die **Märklin-Trägerleitungen**. Der 60982 hat dagegen NEM-Kabelfarben; dessen blaues U+-Kabel und orange/graue Motorleitungen gehören nicht in diese Tabelle. Farbige Markierungen zusätzlich beachten.

## 3. Konkrete Ersatzhandlungen für die Montagekapitel

1. **Beide Aufnahmen vorab beschriften:** „VORN – 60977 – Träger aus 60977“ und „HINTEN – 59649 – Träger aus 60972“. Beide Decoder für Löt- und Widerstandsarbeiten abnehmen; der nicht eingesetzte 60972 bleibt geschützt aufbewahrt. Beide leeren Träger und Halter von oben, unten und seitlich dokumentieren.
2. **62762 erhalten:** Keine pauschale Demontage der langen Platine und keine angenommene aktive Bestückung auf ihr entfernen. Die separate alte Motor-Umschalteinheit gehört elektrisch aus dem neuen Motorweg. Nicht bestätigte Altleiterzüge bleiben unbenutzt; neue Motorleitungen werden direkt und isoliert geführt. Ein mechanischer Träger darf auch ohne elektrische Mitbenutzung erhalten bleiben.
3. **Beide kleinen Träger trocken montieren:** Vorhandene Halteplatten verwenden, sofern sie zur realen Einbaustelle passen. Eine passende isolierende Halterung muss Träger und Decoder halten; Litzen übernehmen keine Haltefunktion. Keine abgeleiteten Standard-Schraubenlängen oder Bohrpunkte festlegen. Unterseitenabstand, Schraubenweg, Drehgestell- und Kupplungsbewegung sowie vollständig geschlossenes Dach am wirklichen Aufbau prüfen.
4. **Stecken:** Herstellerzeichnung des jeweiligen Märklin-Trägers verwenden. Beim gezeigten kompakten Einbau treten die Stifte von unten durch die Decoderplatine; die Decoderbuchse bleibt oben. Fehlende Stiftposition und geschlossene Position 11 müssen sichtbar deckungsgleich sein. Beide Reihen parallel einsetzen und seitlich prüfen. Die bisherigen LoDi-Merkmale „K1“, „helle Fläche“ und „schwarze Struktur“ entfallen vollständig. Die allgemeine Steckmechanik ist in [RCN-121, S. 2–5](https://normen.railcommunity.de/RCN-121.pdf) beschrieben.
5. **Lautsprecher vereinfachen:** Einen passenden unveränderten Lautsprecher aus dem 60977-Satz an die vorgesehene zweipolige Buchse seines originalen Trägers stecken. Dadurch entfallen Gegenstecker-Recherche, Adapterbau und LoDi-Lötpunkte LS1/LS2. Druckfreie Befestigung, freie Membran, ausreichender Dachraum und erster leiser Soundtest bleiben erhalten. Keine Verbindung eines Lautsprecheranschlusses mit U+, GND oder Chassis.
6. **Frontlicht neu begrenzen:** Beim Entfall von LoDi 511 fehlen dessen R4/R5. Bleiben die widerstandslosen LoDi-Frontmodule, benötigen jetzt **beide Farbzweige an beiden Köpfen** eigene passend ausgelegte Widerstände. Vorn darf die bisherige Annahme eingebauter LoDi-Widerstände nicht stehenbleiben. Die konkrete Auslegung gehört in den Beleuchtungsbeitrag.
7. **Wartungszugang erhalten:** Die Motor-Service-Trennstelle muss jetzt zwischen Märklin-Träger und beiden vollständigen Motor-/Drosselzweigen liegen. Die geschlossene Motorisolationsprüfung darf weiterhin ausschließlich am vom Decoder getrennten Motorzweig erfolgen. In REV13 S. 42 bedeutet „andere Steckerhälfte zur LoDi“ künftig „andere Steckerhälfte zum Märklin-Träger“.

## 4. Haupt-Prüfweg mit den endgültigen Trägern und einem HLA

**Zwei 60970 sind kein bestätigter Bestand und keine Pflicht für diesen Hauptweg.** Stattdessen dienen die beiden endgültigen Märklin-Träger als getrennte Aufnahmen. Für das DCC-Lesen des 59649 wird der bereits vollständig umgebaute und isolationsgeprüfte 60941 vorübergehend als Motorlast angeschlossen. Beim anschließenden reinen Licht-Paarversuch bleiben beide Motoranschlüsse offen. Dieser Aufbau ist eine eigene, aus den Herstelleranschlüssen abgeleitete Prüfverschaltung; ein Erfolg wird erst am realen Aufbau nachgewiesen.

Die Norm beschreibt DCC-Bestätigung durch einen kurzen zusätzlichen Stromimpuls, ausdrücklich auch durch einen angeschlossenen Motor. Der Motor ist deshalb ein sachgerechter Lastkandidat; die Teilenummer 60941 allein garantiert keinen Leseerfolg. [RCN-216, S. 5, Abschnitt 3](https://normen.railcommunity.de/RCN-216.pdf). ESU dokumentiert einen DC-Motor an den regulären Motorkontakten und DCC-Serviceprogrammierung. Die Sonderhilfe mit 150 Ω betrifft andere Fx-micro-Artikel und wird nicht auf 59649 übertragen. [ESU LokPilot 5, S. 19, 24–25 und 41](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e).

**Reihenfolge im Gesamtleitfaden:** Projekte/Dateien sichern, 60941 mechanisch umrüsten und Motorisolation prüfen, beide leeren Träger sowie vier begrenzte Lichtzweige vorbereiten, dann Kennung/ESU-Programmierung/Paar prüfen. Wagenbus, Endmontage und Fahrabnahme erst danach. Die alte Forderung nach einer Paarprüfung vor jeglichem Motorumbau entfällt für diesen Aufbau, weil der geprüfte Motor selbst die notwendige Testlast bereitstellt.

| Zustand | Decoder und Quelle | Last / Tätigkeit |
|---|---|---|
| P0 | 60977 allein am bestätigten 60971; ausschließlich USB | Kein Fahrzeug; Märklin-Projekt und Firmware sichern. |
| P1 | 60977 auf eigenem Träger; getrennte CS3-Betriebsquelle | Motor offen, F0/Sound aus, Fahrstufe 0; eindeutige mfx-Anmeldung und CS3-Datensatz sichern. |
| P2 | 59649 allein auf 60972-Träger; ausschließlich CS3-Programmiergleisausgang | Ein HLA über seine geprüften Drosselzweige an MV/MR; lesen/schreiben/rücklesen. 60977 vollständig getrennt. |
| P3 | Beide Träger an derselben getrennten CS3-Betriebsquelle | Nur B/GR und 0/GL parallel. Je Decoder eigene begrenzte Lichtzweige und eigenes U+; beide Motoranschlüsse offen. |
| P4 | Alle Quellen physisch getrennt | HLA wieder ausschließlich vorn am 60977 anschließen. Hinten MR/MV einzeln isolieren; betroffene Prüfungen wiederholen. |

**P2, vollständige praktische Folge:**

1. STOP, ausschalten, Quellenstecker physisch abziehen. Beide Decoder abziehen. **Beide** HLA-Verbindungen zum 60977-Träger lösen; ein an zwei Decodern gleichzeitig angeschlossener Motor ist unzulässig.
2. Den vollständigen HLA-/Drosselzweig mit zwei einzeln isolierten, zuvor durchgemessenen Prüfverbindungen ausschließlich an **MV/Grün und MR/Blau des hinteren Märklin-Trägers** anschließen. Motorisolation einschließlich dieser Prüfverbindungen bei abgezogenem Decoder prüfen. Alte Motorumschaltung, Wagenbus und unbekannte Originalplatinenpfade bleiben getrennt. Motor mechanisch sicher, Räder/Getriebe frei; nie blockieren.
3. Nur 59649 korrekt einsetzen. B/GR an B und 0/GL an 0 des getrennten CS3-Programmiergleisausgangs. Anlage, Betriebsausgang, 60971 und 60977 bleiben ab. Nach Sitz-/Isolationskontrolle einschalten, Fahrstufe 0, F0 aus; GO ausschließlich zum Lesen. Der vollständige Menü-/Serviceeintragablauf aus REV13 S. 12 bleibt bestehen.
4. **CV8 zweimal frisch und fehlerfrei lesen, jeweils 151 erwarten.** Erst dies bestätigt den konkreten Leseweg. Anschließend reale Altwerte auslesen und die persönliche, bankweise Export-/Schreib-/Rücklesefolge aus REV13 S. 12–13 vollständig durchführen. Kleine Motorbewegungen können von Quittierungsimpulsen stammen; anhaltender Lauf, Überlast, auffällige Wärme oder Geruch bedeuten STOP und physische Trennung.
5. Bei Fehler zunächst stromlos Ursache prüfen. Weder Reset noch Einmessfahrt, keinen fremden Lastwiderstand und kein blindes Wiederholen. Schreiben kann trotz fehlender Quittierung erfolgt sein; nach wiederhergestelltem Leseweg zuerst tatsächliche Werte feststellen.
6. Nach allen Änderungen STOP, ausschalten, Quelle abziehen; 59649 abnehmen. Beide HLA-Prüfleitungen entfernen und die hinteren MR/MV-Adern einzeln isolieren. Neue Anschluss-/Sichtprüfung, dann 59649 wieder einsetzen. Für P3 bleibt der HLA vollständig getrennt.

**P3, vollständige praktische Folge:** Die endgültig vorgesehenen Frontmodule mit je einem eigenen Serienwiderstand pro Farbzweig dienen als sichtbare Prüflasten. Vorn: eigenes +Ub/LV/LR an Plus/Weiß/Rot. Hinten: eigenes +Ub/LV/LR an Plus/Rot/Weiß. Keine nackte LED ohne Strombegrenzung, keine Verbindung der beiden U+-Netze. Den quellenfreien B/0-Verteiler vor Einsatz prüfen: beide B-Pfade und beide 0-Pfade durchgängig, B gegen 0 offen; positive Kontaktkontrollen davor und danach.

Zuerst nur Master am Betriebsausgang anschließen, STOP aufheben und F0/Richtung prüfen. Dann STOP, ausschalten, physisch trennen und ESU über den geprüften Verteiler ergänzen. Nur Gleiseingänge parallel. Nach erneutem Anschluss STOP aufheben und allein den mfx-Mastereintrag bedienen. Fahrstufe bleibt 0, Sound aus, keine Konfigurationsfenster im Paar öffnen.

| F0 / Richtung | 60977-Front | 59649-Front |
|---|---|---|
| aus / beide Richtungen | dunkel | dunkel |
| an / vorwärts | weiß | rot |
| an / rückwärts | rot | weiß |

Mindestens fünf Richtungswechsel und die gesamte Tabelle nach gemeinsamem Ausschalten/Wiedereinschalten prüfen. Erweiterte Startreihenfolgen nur mit passenden getrennt schaltbaren Eingängen nachweisen. Quellenwechsel und sämtliche Leitungsänderungen bleiben vollständig stromlos. Diagnose und optionale SID-Prüfung aus REV13 S. 14 bleiben erhalten. Ein negativer Paarversuch sperrt Wagenbus/Endaufbau, macht aber den bereits geprüften Motorumbau nicht rückwirkend unzulässig.

**Spätere Wartung:** Motor-Servicezugang und isolierte Prüfverbindungen erhalten. Zum ESU-DCC-Lesen erneut P2 herstellen; ein zusätzlicher fertiger Prüfstand ist optional. Danach wieder Motor allein an 60977, hintere Motoradern isolieren und betroffene Anschluss-/Funktionsprüfungen wiederholen.

### Übernahme aus REV13

| Alte Seite | Beurteilung |
|---:|---|
| 8–9 | Gerätezwang ersetzen durch P0–P4. Alte 60970-Karte nur als ausdrücklich optionale Gerätealternative, nicht im Pflichtweg. |
| 10 | Sicherung und eigene Kennung erhalten; Aufnahme-/CS3-Anschluss jetzt P1. 60977 ist bestellt, die Seriennummer noch nicht abgelesen. |
| 11 | Offline-Vergleich vollständig erhalten: Testkopie getrennt, danach persönlicher Export. |
| 12 | Menüs und Lesefolge erhalten; Hardware P2 mit geprüftem HLA und zwei echten CV8-Lesungen. |
| 13 | Bankweises Verfahren, Index vor Banklisten-Laden, reale Altwerte, unmittelbare Einzelwertänderung und Rücklesen erhalten. Wiederanschluss verweist auf neue S. 12/3. |
| 14 | Beweislogik erhalten; Zeitpunkt nach HLA-/LED-Vorbereitung, Hardware P3 und sichtbare Farbtabelle statt Prüfstand-LV/LR-Anzeigen. |
| 16–18 | Motorprüfverfahren erhalten; Anschlussverweise an Märklin-Träger anpassen. |
| 24–25, 34–35 | Neue Trägerherkunft, Originalstecker und Märklin-Steckmechanik. |
| 31 | Motor-/Sound-/F0-Verfahren erhalten; AUX1 steuert neues Innenlicht-Relais, ohne Dimmung. |
| 32, 36–37 | Prüflogik erhalten; geänderte Verdrahtung und ausschließliche vordere Schleifereinspeisung berücksichtigen. |
| 44 | Diagnose erhalten; ESU-Wartung jetzt über P2. |
| 45 | LoDi-SUSI-Frage entfällt vorn; 60974 bleibt separat abgenommenes Zubehör. |

**Nicht verkürzen:** Die eigene Kennung, persönlicher Export nach dem Testvergleich, Indexzustand vor dem Laden, STOP/GO und physische Trennung, frisches Rücklesen, Zustand nach fehlender Quittierung sowie echte Paarprüfung bleiben eigenständige Schritte. [ESU Master/Slave-Verfahren](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/), [Märklin CV-Editor](https://www.maerklin.de/fileadmin/media/clubs/downloads/Loks_CV_Editor.pdf).

## 5. Innenlicht-Ausgang in S. 31 bewusst neu festlegen

Mit dem Wegfall der LoDi-Motorplatine entfällt deren Jumperwahl. **Aktueller Hauptplan: AUX1 steuert das Innenlicht-Relais; dessen Kontakt schaltet die Wagenlast.** Die Relaisspule erhält dauerhaft volle Ausgangsstärke solange die gewählte Funktion an ist; keine Dimmung, Blink-/Timer- oder Kuppler-Abschaltfunktion. Geeignete Spule und Schutzbeschaltung folgen dem Elektrikbeitrag. AUX1 ist verstärkt; eine nur für AUX4 erforderliche Ausgangstyp-Umschaltung entfällt.

Für AUX1 eine bewusst gewählte Funktionstaste setzen, in beiden Richtungen sowie Stand/Fahrt, ohne konkurrierende Bedingungen. Den tatsächlich vorgesehenen Lichtmodus und zulässige Last neu abnehmen. Ein vorhandenes ICE-Soundprojekt darf denselben Ausgang nicht unbemerkt über eine weitere Taste oder Bedingung ansteuern. Eine AUX-Nummer ist keine F-Tastennummer.

Falls der Gesamtplan **AUX4** wählt, bleiben die korrekt begrenzten CV51-Bit4-Prüfungen aus REV13 S. 31 nötig. Bei AUX1 werden diese Prüfungen nicht vorsorglich verlangt. Motorumkehr über CV51 Bit0 bleibt ein gesonderter, nur bei nachgewiesener falscher Richtung verwendeter Vorgang; übrige Bits erhalten. Nach endgültigem Soundprojekttransfer Einstellungen und betroffene Paar-/Funktionstests erneut prüfen. [Märklin mSD3/mLD3-CV-Tabelle](https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf).

## 6. SUSI / 60974: neue klare Grenze

Vorn ist der originale SUSI-Steckweg des 60977-Trägers anhand Herstellerzeichnung nutzbar; es muss kein LoDi-K1-/S2-Pad als Pufferanschluss erraten werden. 60974 bleibt bis zur gesonderten Ergänzung abgezogen. Später nur den vorgesehenen unveränderten Stecker verwenden, Firmware ab 3.2.0.1 nachweisen, keine Pufferkaskade und keinen 60974 am ESU einsetzen. Die SUSI-Buchse eines Märklin-Trägers macht den aufgesteckten 59649 nicht zu einem freigegebenen 60974-Decoder. [Märklin 60974, S. 4 und 28](https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf).

Die tatsächlich gepufferten Verbraucher hängen vom neuen Wagenkreis ab. Eine Versorgung der Wagen aus Gleis-RT wird nicht durch einen am 60977 gepufferten U+-Kreis ersetzt. Die Pufferung und der Nachlauf erhalten eine eigene Abnahme; für die Grundanleitung wird kein bereits getesteter Pufferbetrieb behauptet.

## 7. Konkrete Abnahmepunkte des neuen Trägeraufbaus

- Satzherkunft und realer Zustand beider Träger sind dokumentiert; Grundbeschriftung und Index passen zu den richtigen Herstellerbildern.
- Die benötigten Leitungen/Trägeranschlüsse werden am leeren Träger nachverfolgt; neue Lötstellen und mechanische Befestigungen sind vor und nach Montage geprüft. Keine pauschalen OL-Sollwerte über bestückte Decoderpfade.
- Beide U+-Netze, beide Motorausgänge und sämtliche Decoder-Ausgänge bleiben gegenüber dem jeweils unzulässigen Chassis-/Fremdnetz getrennt. Lediglich die ausdrücklich geplanten Gleiseingänge dürfen dieselbe Quelle erhalten.
- Vorne sind beide Motorzweige einschließlich Drosseln und endgültiger Service-Trennstelle geprüft. Hinten bleiben Motor-, AUX-, SUSI- und Lautsprecheranschlüsse unbenutzt und freie Litzen einzeln isoliert.
- Träger und Decoder passen druckfrei bei geschlossenem Gehäuse; Stecker bleiben für Wartung zugänglich. Original62762 und neue Aufnahme berühren sich nur an vorgesehenen, elektrisch sicheren Auflagen.
- Alle vier nackten LED-Farbzweige besitzen ihre eigene belegte Strombegrenzung, sofern die LoDi-Frontmodule bleiben. Vorne wird keine R4/R5-Wirkung der entfernten Platine mehr angenommen.
- Persönlicher Software-Nachweis und Paarprüfung sind abgeschlossen; danach getrennte Fahrzeug-Ersttests, reale Farben, leiser Sound, Kleinstfahrt und die neu geplante Last-/Wagenabnahme. Künftige Prüfungen werden nicht vorab als bestanden markiert.

## 8. Nur nach ausdrücklicher Wahl: mLD3-Fallback

60972 und 60982 ersetzen das Soundziel nicht durch bloße Programmierung; beide sind Lokdecoder ohne integrierten Sound. Ein Aufbau mit diesen beiden Decodern wäre ein eigener Funktions- und Bedienzweig. Die ESU-Synchronisations-CVs aus REV13 S. 11–14 dürfen nicht darauf angewendet werden. mfx meldet jeden Decoder mit seiner eigenen Identität an; ein einzelner gemeinsamer Zugeintrag ist dadurch nicht automatisch erreicht. Eine separat geplante Traktion oder gemeinsame DCC-Adresse wäre weder derselbe Nachweis noch ein unbeabsichtigt einzubauender Ersatz.

Nur bei einer künftig ausdrücklich abweichenden Nutzerentscheidung müsste die Trägerzuordnung neu beginnen: Der 60972 benötigt seine 21MTC-Aufnahme; der 60982 wird direkt verdrahtet und benötigt keine zweite 21MTC-Aufnahme. Die 60982-NEM-Farbtabelle und markierten Programmerleitungen sind dann eigenständig zu verwenden. Der dokumentierte 60974-Anwendungsbereich nennt 60972, nicht 60982. Für die aktuelle Aufgabe gilt verbindlich die bestätigte Soundvariante 60977 + 59649; dieser Fallback erzeugt keine weitere Rückfrage.

**Bewertung:** Der zusätzliche 60972-Satz schließt bei vollständigem Bestand die bisher offene zweite Aufnahme auf plausible und herstellerseitig gut belegte Weise. Der Hauptweg erhält Sound und den ausgearbeiteten REV13-Programmierablauf. Neu zu zeichnen und zu prüfen sind die beiden Trägermontagen, die direkte Motor-/Lichtverdrahtung, vier LED-Widerstandszweige und der endgültige Wagenstromkreis. Ein Einbauort, eine Schraubenlänge oder ein gemessener Platinenpfad wird dadurch noch nicht vorweggenommen.
