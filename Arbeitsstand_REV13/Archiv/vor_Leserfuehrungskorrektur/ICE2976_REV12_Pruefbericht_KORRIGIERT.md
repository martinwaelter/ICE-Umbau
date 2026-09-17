# ICE 2976: korrigierte Bewertung des REV12-Prüfberichts und Umsetzung in REV13

Stand: 12.09.2026. Auftrag: Bericht prüfen und die Anleitung dort korrigieren, wo dies nötig oder sinnvoll ist. Die folgende Bewertung ersetzt die fachlichen Schlussfolgerungen und Reparaturvorschläge des vorgelegten Berichts; dessen Original bleibt erhalten.

**Urteil:** Der Bericht findet echte Verbesserungsmöglichkeiten bei Prüfumgebung, Kupplungsbestand, Bedienfolge und Endmontage. Mehrere als bestätigt dargestellte Erklärungen sind jedoch falsch oder überzogen. Besonders die vorgeschlagenen Freigaben mit 25 V/5 mA, 60 % Strommittelwert und „100 Ω ohne Lautsprecherlast“ dürfen nicht übernommen werden. Die sinnvollen Änderungen sind in REV13 tatsächlich umgesetzt, einschließlich der bei der Schlussprüfung gefundenen Übergangslücken.

## Gegenstand und belegter Nutzerbestand

| Eingabe | Identität |
|---|---|
| REV12-Werkstattfassung | 44 Seiten; SHA-256 `95af61083373a0755fde8ebd5ae70233952f6283b3db652b03e71c26582bcc8e` |
| Originalbericht vom 12.09.2026 | SHA-256 `d4f913f4c6484c94f219e23c4c610e0d9d1c08679cb93b20dc6a570e9f79a380` |
| Verbindliche Nutzerangaben | Multimeter, Märklin-Decoderprogrammer und CS3 mit laut Nutzer aktueller Firmware; am 12.09.2026 zusätzlich ausdrücklich bestätigt: **kein separates Prüfgleis vorhanden** |
| Nicht als vorhanden oder geprüft bestätigt | Genaue Gerätetypen/Versionsnummern, zwei Prüfaufnahmen, konkrete Kupplungsausführung, Platinen-/LED-Grenzdaten, Lastmesswerte und Fahrzeugfunktion |

Die Originaldatei des Berichts liegt unter `/Users/martinwaelter/Märklin Gleisplan/ICE2976_REV12_Pruefbericht.md`; eine unveränderte Kopie ist im REV13-Arbeitsstand gesichert. Die Berichtsaussage zu 227 internen Verknüpfungen und 34 externen Quellenverweisen der REV12 stimmt. Die erwähnten 38 Zitatprüfungen beziehungsweise 70 Behauptungsprüfungen sind ohne ihre vollständigen Auswahl- und Ergebnisdateien keine unabhängig reproduzierbare Zusatzprüfung. Eine Übereinstimmung mehrerer Modellprüfungen ersetzt keine Herstellerquelle.

Zu W-01 wurde die Angabe zunächst nur im Bericht gefunden und deshalb nicht als unmittelbare Nutzeräußerung übernommen. Die anschließende direkte Rückfrage wurde mit „Kein separates Prüfgleis vorhanden“ beantwortet. Dieser neue Beleg ist in der Anleitung berücksichtigt.

## Entscheidende Gegenprüfungen

**Die ESU-Belegung widerlegt das konkrete Schadensszenario von W-07.** Die originale LokPilot-5-Anleitung nennt in Abb. 3 auf S. 19 ausdrücklich den 59649 und weist die Pins 9 und 10 als unbelegt aus. Die allgemein von der Schnittstellennorm zugelassene alternative Belegung ist kein Beweis für ihre Nutzung durch diesen Decoder. 100 Ω am 60970 ist trotzdem eine reale Lautsprecherlast, keine elektrische Trennung. Die neue Tabelle nennt deshalb die konkrete Stellung, die tatsächliche ESU-Belegung und den getrennten Zustand der Soundfunktion. [ESU-LokPilot-5-Anleitung](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e), [Märklin 60970](https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf).

**W-11 beruht auf einer unvollständig verfolgten Dateieinbindung.** Im festgelegten JMRI-Stand bindet die LokPilot-5-Definition die gemeinsamen V5-Register ein. Diese binden wiederum ausdrücklich `v4decoderInfoCVs.xml` ein. Darin steht die Firmwarebank 0/255 mit CV285–288. Der Dateiname V4 schließt V5 also nicht aus. Der optionale Weg bleibt als belegte Softwareimplementierung erhalten; eine reale Geräteprüfung oder herstellerübergreifende Kompatibilitätszusage folgt daraus nicht. [LokPilot-5-Definition](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/ESU_LokPilot5.xml#L246), [Einbindung in v5standardCVs](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v5standardCVs.xml#L18), [Firmwaredefinition](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml#L60).

**Programmierausgang und Decodergrenze sind unterschiedlich zu bewerten.** Märklin verlangt den ersten Test des eingebauten Decoders ohne Gehäuse auf dem Programmiergleis. 1,6 A ist die maximal zulässige Decoder-Gesamtlast, kein Mindeststrombedarf. REV13 verwendet den Programmierausgang für die begrenzte Einzelkontrolle; danach erfolgt ein ausdrücklich spannungsfreier Wechsel zum Betriebsausgang für Funktion und Last. Nach einer ungeklärten Abschaltung gibt es keinen automatischen Versuch an der stärkeren Quelle. Die tatsächliche CS3-Netzteileinstellung wird am Typenschild abgeglichen. [60977-Einbauanleitung, S. 3/6](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf), [CS3-Kurzanleitung ab V2.5, S. 26](https://static.maerklin.de/damcontent/c1/ce/c1ce554ad6ad195c04e32ba1b4dd64511764068661.pdf).

**Eine Mittelwertreserve begrenzt keine unbekannten Stromspitzen.** Eigene Gegenrechnung, keine Fahrzeugmessung: 1-A-Rechteckimpulse mit 10 % Tastgrad haben 100 mA Mittelwert, rund 316 mA Effektivwert und 1 A Spitze. Der Mittelwert liegt unter 60 % von 250 mA, während die Spitze erheblich darüber liegt. Die im Bericht vorgeschlagene 40-%-Reserve kann daher keine allgemeine Freigaberegel sein. REV13 ergänzt die DMM-Reihenmessung als Betriebsbeobachtung. Die endgültige Lastabnahme benötigt weiterhin passende Herstellerdaten oder eine qualifizierte Erfassung des Stromverlaufs. Die LED-Messung ist kein Gegenbeweis: Dort wird ein bereits begründeter, strombegrenzter Zweig vorausgesetzt. [Tektronix zur Stromerfassung](https://www.tek.com/en/documents/application-note/making-accurate-current-measurements-power-supplies-oscilloscopes).

## Alle 36 Befunde und ihr Ergebnis

Die Seiten in der letzten Spalte gehören zur **neuen REV13**. „Umgesetzt“ bezeichnet die Dokumentänderung, keine ausgeführte Hardwaremessung. Ein teilweise widerlegter Befund kann dennoch eine sinnvolle Präzisierung auslösen.

| ID | Korrigierte Bewertung | Umsetzung / finale Seite |
|---|---|---|
| W-01 | Fehlendes separates Prüfgleis inzwischen direkt bestätigt. Nicht jede leere Anlage ist elektrisch getrennt. | S. 1/3: konkreter freier Prüfabschnitt mit einem B/0-Anschluss, ausreichender Länge, Trennung und Quellenwechsel. Keine feste Drei-/Vier-Gleis-Längenfreigabe. |
| W-02 | Berechtigter Bedarf an klaren Betriebsstufen; pauschale Ungeeignetheit des Programmierausgangs nicht belegt. | S. 3/32/36/37: Hersteller-Erstkontrolle am Programmierausgang; danach kontrollierter spannungsfreier Wechsel für Funktion/Last. |
| W-03 | Frühe Bestandsprüfung sinnvoll; tatsächliche Kupplungsausführung offen. | S. 4: beide Köpfe und sämtliche Wagenübergänge vor elektrischem Umbau ansehen; Kontakte, getrennte Anschlüsse, Passung und Nachrüstbedarf dokumentieren. |
| W-04 | Konkreter Klärungsweg fehlte. 25 V/5 mA als angeblich konservative Ersatzfreigabe unbelegt. | S. 20: genaue LoDi-Anfrage mit Fotos/Revision und Versorgung; Daten oder freigegebene komplette Beschaltung. Ungeklärte hintere Zweige bleiben isoliert. |
| W-05 | DMM-Zusatzmessung sinnvoll; behaupteter Widerspruch zur LED-Karte und 60-%-Regel falsch. | S. 39: konkrete batteriegespeiste DMM-Reihenmessung als Mittelwertdiagnose, ohne verdeckte Spitzenstromfreigabe. Herstelleranfrage und Stromverlauf bleiben die vollständigen Nachweiswege. |
| W-06 | Polungszuordnung war vorhanden; geeignete Vorprüfung kann klarer sein. | S. 20: Polung vor Löten bestätigen; Diodentest nur bei belegter Geräteeignung. OL ist kein Defektbeweis; keine höhere Ersatzspannung. |
| W-07 | Fehlende Stellung bestätigt; angenommene AUX-Belegung von Pins9/10 beim 59649 widerlegt. 100 Ω ist keine offene Last. | S. 9: Stellung100 Ω, Pins9/10 unbelegt laut ESU, keine externe Last; 60977-Testlast getrennt beschrieben. |
| W-08 | Explizite Bedienungssperre sinnvoll. | S. 13: „Prog.“ und „Vorlagenwerte schreiben“ bleiben unbenutzt; Q24 direkt zugeordnet. |
| W-09 | Eigene Parallelschaltung klar kennzeichnen. Bloße Eingangsumpolung des zweiten isolierten Testers beweist keinen direkten Kurzschluss. | S. 9: passiven Verteiler vor Elektronikanschluss prüfen; CS3 B→rt, 0→bn; je Gerät ein Decoder, nur Gleiseingänge gemeinsam. |
| W-10 | Vorbereitungs- und Ausführungstexte vermischt. | S. 21/32 vorbereitend; S. 33–37 zuerst Checkliste, Stecken und Einzeltests; Bereich S. 38, begleitende Last S. 39, Wagenserie S. 40. |
| W-11 | Widerlegt: gemeinsame Firmwaredatei tatsächlich über V5 eingebunden. | S. 13: optionalen Diagnoseweg erhalten, vollständige JMRI-Kette Q13/Q23/Q35 und Kategorie Softwarebeleg erläutert. |
| W-12 | Reale Evidenzgrenze bestätigt: zurückgelesene Bytes beweisen keine geräteübergreifende Identitätssemantik. | S. 11/14: mfxuid-Zuordnung als zu prüfende Annahme; reale Paarreaktion nachweisen, keine universelle Kompatibilität behaupten. |
| W-13 | Genereller B–L-Defekt unbewiesen; LoDi erlaubt optionale B-Radmasse. Live-Clip-Vorschlag ungeeignet. | S. 30/40: Grundaufbau B frei. Vergleich ohne B, ausschalten/trennen, erst dann B anschließen und Funktion/Last erneut prüfen. |
| W-14 | Richtige Belegung bereits vorhanden; zwei Herstellerlegenden können verwirren. | S. 27: Standardlegende und hier maßgebliche Motorplatinenlegende ausdrücklich unterschieden; RT→O, GE→L, B optional. |
| W-15 | Kontaktverfahren präzisieren; keine beliebigen Elektronikadern trennen. | S. 38: nur identifizierter potentialfreier Kontakt, Foto/Markierung, Quellen ab, Kontaktadern abnehmen, prüfen und anschließend wieder anschließen. Eine Ω-Messung belegt nur die aktuelle Stellung. |
| W-16 | Jeden Speicher berücksichtigen; zwei Plätze beweisen keine Parallelschaltung und keine pauschale Verdopplung von τ. | S. 5: jeden realen Elko einzeln entladen/nachmessen, zum Schluss alle nochmals prüfen. Beispielrechnung gilt für einen isolierten Elko. |
| W-17 | Einzelarbeiten mit einer und Softwarevorbereitung ohne Aufnahme waren schon möglich. Paarprüfung nicht wegen fehlender Ausrüstung überspringen. | S. 8/44: Wege klarer benannt; wiederkehrenden Zugriff auf Prüfaufnahmen für Wartung und Paarprüfung einplanen. |
| W-18 | Sinnvolle Präzisierung der Ausnahmen. | S. 33: „entfällt“ nur bei Gegenkopf-Motor/Lautsprecher. Hintere LEDs ausdrücklich „getrennt/isoliert“; andere Pflichtangaben bleiben nötig. |
| W-19 | Vor CV51-Bit0-Umkehr den tatsächlichen Anschluss prüfen. | S. 36: erst Abgleich mit Anschlusskarte, bei Abweichung reparieren; nur danach begründete Bitänderung mit Erhalt der übrigen Bits und Rücklesen. |
| W-20 | Frühe Messkarte soll keinen verfrühten Einschaltversuch auslösen. | S. 21: zunächst lesen/Messpunkte markieren; Ausführung erst bei S. 36/37. Hinten weiterhin gemeinsamer Lichttest mit Master. |
| W-21 | Gemeldete Updateanforderung unabhängig von optionaler Firmwarediagnose behandeln. | S. 13: Voraussetzung vor Änderungen ausdrücklich genannt. Unbekannte Firmware allein ist keine erfundene Kompatibilitätsaussage. |
| W-22 | Wiederholungsbedarf auch an eigener CS3 sinnvoll. | S. 14: nach neuer Masteranmeldung/SID und relevanten Projektänderungen erneut Paarfunktion prüfen. Kein Reset allein zum Erzwingen einer Änderung. |
| W-23 | Sichtbarer STOPP sinnvoll; Abdeckung vorn/hinten/Wagen war bereits in der Tabelle. | S. 7: konkrete Sperre für ungeklärte oder unzugängliche Anschlüsse; bekannte Serienwiderstände gegen Sollwert/Toleranz prüfen. |
| W-24 | Quelle als mögliche Abschaltursache nennen; Zeitpunkt allein beweist keine Ursache. | S. 32/36/37/44: Fahrzeug, Anschluss, Freilauf, Netzteil und aktive Lasten untersuchen; kein blindes zweites Einschalten. |
| W-25 | Verwechslungsrisiko G0/GO redaktionell plausibel. | S. 14 und alle Verweise heißen CS3-Paarprüfung. GO bleibt nur Bedienzustand der Zentrale. |
| W-26 | Gleichlautende Kürzel gezielt reduzieren. | S. 9 Prüfaufnahmen nach Decoderartikel; S. 13 Index-/Firmwarelisten; S. 39 Nachweis1/2. Elektrische Klemmenbezeichnungen bleiben unverändert. |
| W-27 | Feste Buchse, Schalter und Taster getrennt behandeln. | S. 9: MTC21, e, b, a, c und d einzeln; Reed-Simulation nicht betätigen; Impedanz von Soundfunktion getrennt. |
| W-28 | Gemischt: Quellenzeilen verbessern. Q5 enthält tatsächlich Frontmodule; Q26 enthält GFP3 auf S.26. Beide pauschalen Quellenvorwürfe widerlegt. | Q5/Q9/Q26 genauer bezeichnet; Q24/Q30 an passenden Karten; Q35 Einbindungskette und Q36 ältere vollständige CS3-Anleitung ergänzt. |
| W-29 | Platz-/Wärmeprüfung sinnvoll. Faktor2 bedeutet nicht generell einen 0,5-W-Widerstand. | S. 25: tatsächliche Widerstände in Trockenpositionierung aufnehmen, Bauform, Abstände und Beweglichkeit prüfen. |
| W-30 | Größerer konservativer Widerstand kann geringere Helligkeit bewirken; kein Schutzfehler. | S. 20 erläutert mögliche Folge; S. 43 helleres Ende dimmen, ungedimmte Strombegrenzung erhalten. |
| W-31 | Endverlauf darf nach Prüfung nicht durch erneutes Umlegen verändert werden. | S. 23 Zugang vorab entscheiden; S. 42/43 feste äußere Motor-Trennstelle, nach endgültigem Schließen motorseitig messen und nur außen verbinden. |
| W-32 | Reproduzierbaren Umfang nennen, keine angebliche Herstellergarantie. | S. 18: mindestens vier verteilte Rotorstellungen als eigene Stichprobe; Gegenstellen, beide Messorte und normale Endlagen weiter prüfen. |
| W-33 | Leistungsdaten wiedergeben. Interne 60970-Last und Fahrzeuglautsprecher wurden im Bericht vermischt. | S. 24: 1,6 W an8 Ω /2,75 W an4 Ω; unverändertes Satzteil verwenden. Die Testlast S.9 bestimmt nicht dessen Impedanz. |
| W-34 | Kontextabhängig sinnvolle Wiederholungen. | S. 7 bekannte Widerstände, S. 32 verstärkte Ausgänge, S. 42 geschlossenes Gehäuse, S. 31/45 getrennte Reset-/Einmess-/Puffervorgänge. |
| W-35 | Vorwärtsverweis ausdrücklich nennen. | S. 26: Kontaktprüfung S.28 jetzt vorziehen; frühe Bestandsprüfung steht bereits auf S.4. |
| W-36 | Anschlussbeschreibung näher an Herstellerbeleg. | S. 45: SUSI-Schnittstelle des Decoders; konkrete LoDi-Anbindung separat bestätigen. Keine unbewiesene Trägerbuchse oder Kaskade. |

## Umsetzung und abschließende Prüfung

REV13 hat **46 Seiten, 28 Bild-/Schemaeinsätze und 36 Quellen**. Alle 14 Foto-/Herstellerabbildungen der REV12 sind erhalten; hinzu kommen zwei Schemaeinsätze. Schriftgrößen wurden nicht zum Einpassen der Ergänzungen verkleinert. Jede Seite wurde gerendert und visuell geprüft, betroffene Seiten nach der Schlusskorrektur erneut. Die Prüfung umfasste auch die Bedienfolgen nach STOP, die Rückkehr zur Einzelaufnahme, die B-Abhängigkeiten, den Kontaktwiederanschluss sowie die Endmontage nach erneutem Öffnen.

Die automatische Dateiprüfung kontrolliert Seiten/Lesezeichen, interne Verweisziele, Verknüpfungsrechtecke, Textgrenzen, erhaltene Fotopfade und unveränderte Eingangsdokumente. Sie ist keine elektrische Hardwareprüfung. Die exakte Enddatei und Prüfergebnisse stehen in `Arbeitsstand_REV13/final_validation.json`.

**Dokumentkorrektur abgeschlossen; physischer Umbau nicht ausgeführt.** Zunächst den getrennten Prüfabschnitt nach S.3 aufbauen, Kupplungen nach S.4 bestimmen und die tatsächliche Decoderpaarfunktion nach S.14 prüfen. Bauteil-/Gerätedaten, LED-Freigabe, Lastverlauf, Servicezugang und eigene Anlage benötigen weiterhin reale Identifikation beziehungsweise Messung. Diese Anforderungen werden weder durch den korrigierten Bericht noch durch ein unauffälliges Seitenbild als bestanden ausgegeben.
