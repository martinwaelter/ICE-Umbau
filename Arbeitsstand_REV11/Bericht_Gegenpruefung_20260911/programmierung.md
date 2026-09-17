# Unabhängige Gegenprüfung – Programmierung und Decoder-Vorabtest

Stand: 11.09.2026. Geprüft wurden V-04–V-08, V-17–V-22, V-29 und die Programmierungs-/Prüfstandsanteile von V-30. Der Prüfbericht und die REV11 wurden nicht geändert. Eigene Primärquellenabfragen und lokale PDF-Auszüge liegen in diesem Ordner. Keine reale CS3, kein Decoder und keine Windows-LokProgrammer-Installation wurden bedient.

Prüfgegenstand durch eigenes Hashen bestätigt: REV11 SHA-256 `3c67f596856f5403eac6f27f1f2512379555d3611749e4a7bd94f817cc7e41cb`. Gegenprüfung am tatsächlichen PDF-Text und an `rev11_pages.json`; REV10-Abgleich an `Arbeitsstand_REV10/REV10_LESEFASSUNG.txt`. Wörtlich vorhandene Texte allein beweisen weder die behauptete Fehlerwirkung noch die Tauglichkeit der Ersatztexte.

## Ergebnismatrix

| ID | Diagnose des Berichts | Ersatz/Empfehlung des Berichts | Konsequenz |
|---|---|---|---|
| V-04 | Teilweise bestätigt: offene Ausstattung und fehlende konkrete Bedienkarte; fehlender Besitz ist nicht bewiesen. | Überarbeiten: verlangt Lautsprecher je Decoder und setzt 53900 zu pauschal als passend voraus. | Bestand feststellen, dann genau eine passende Karte je Aufnahme; Soundlast nur am 60977. |
| V-05 | Teilweise bestätigt: zusätzliche Indexschreibungen und fehlender Versions-Grenzwert; behaupteter Widerspruch zu S. 9 widerlegt. | Optionalisierung vertretbare redaktionelle Entscheidung, keine technisch zwingende Reparatur; Wiederanlaufregel sinnvoll. | Firmware als dokumentierenden Nachweis behandeln, technische und redaktionelle Aussagen trennen. |
| V-06 | Teilweise bestätigt: Eskalationsweg fehlt; „unbegrenzte Versuchsschleifen“ nicht angeordnet. | Feste Zwei-Versuche-Regel unbelegt; 53451 kein garantierter Kompatibilitätsbeweis. | Wiederholung nur nach begründeter Änderung, sonst Diagnoseentscheidung. |
| V-07 | Bestätigt als Ausführbarkeitslücke des SID-Nachweises. | Unvollständig: Fremdsystem-SID wird durch Rückkehrdatensatz nicht bewiesen; Pflichtgate bleibt offen. | Nachweismittel vor Test klären oder ausdrücklich eingeschränkte Abnahme, keine stillschweigende Freigabe. |
| V-08 | Teilweise bestätigt: Dateiformat und API vermischt; HTTP-Unerreichbarkeit nicht belegt. | Dateifeld `.adresse` richtig; `address` ist jedoch im CS3-JSON tatsächlich vorhanden. | Datenformat und Quelle ausdrücklich zuordnen; `/config/...` nur unbestätigter Kandidat. |
| V-17 | Loklisten-Foto als früher Handgriff tatsächlich entfallen; Behandlung alter Einträge auf S. 11 erhalten. | Sinnvoll als lokale Ergänzung. | Kein vollständiger Verlust der Selbstanmeldungsabsicherung. |
| V-18 | Lokale Abbruch-/Konfigurationsregel auf S. 11 fehlt. | Sinnvoll. | Vorhandene übergreifende Regeln dort kurz wiederholen. |
| V-19 | Tatsächliche Adress-/Protokolltabelle entfallen. | Teilweise: unbenutzte Adresse des Serviceeintrags löst keine Decoderadresskollision. | Reale Decoderwerte und CS3-Bedienadresse getrennt dokumentieren. |
| V-20 | Verständlichkeitsverlust der Bit-Berechnung bestätigt; keine falsche ≥16-Regel in REV11 vorhanden. | Wertebereich 0–31 mit 16er-Fallunterscheidung sachgerecht bei passender CV-Tabelle. | Kleine Bedienpräzisierung, keine nachgewiesene falsche Ausgangseinstellung. |
| V-21 | Konkreter ESU-Auslöser CV54=0/F1 fehlt. | Sinnvoll als Sperrhinweis, keine Ausführung. | P3-Ergänzung bestätigt. |
| V-22 | Nur lokaler Querverweis-/Warnhinweis fehlt. | CV7-Lesehinweis sinnvoll; „nie zwei“ bereits durch „Nur einen ... Puffer“ abgedeckt. | Kein eigenständiger Verlust der Ein-Puffer-Regel. |
| V-29 | Eigener 5.x-Lauf fehlt; Schluss „nur für v4.4.0 belegt“ zu eng. | Reale Offline-Prüfung sinnvoll und bereits Inhalt der Karte S. 8. | Offener Ausführungsnachweis, kein nachgewiesener Fehler der Offline-Anweisung. |
| V-30 | Präzisere Quellenzuordnung berechtigt; keine falsche Zahlenformel belegt. | Primäre Implementierungsdatei und konkrete Prüfstand-Anleitung ergänzen. | Redaktionelle Nachweisverbesserung. |

## V-04 – Prüfaufnahme fehlt als konkret ausführbarer Bestandspfad

**Fundstellen:** REV11 S. 2 Geräteliste; S. 6 Tabelle mit sechs Aufnahmefeldern, „Bestand prüfen“, Schritte 1/2; S. 9 VORHER; S. 11 VORHER. S. 6 verlangt ausdrücklich zwei getrennte Aufnahmen oder gleichwertig dokumentierte Aufbauten. Ein freies Bestandsfeld beweist nicht, dass der Anwender keine Aufnahme hat. Es beweist, dass der konkrete Aufbau noch nicht festgelegt ist. „Nicht vorsorglich kaufen“ verbietet keine gezielte Beschaffung nach Kompatibilitätsprüfung.

Die Lücke für einen Anfänger ist real: Es fehlt eine auf den tatsächlich vorhandenen Tester zugeschnittene Anschluss-/Schalterkarte. Der Ersatz des Berichts wiederholt aber weitgehend die vorhandene Anforderung. Zusätzlich verlangt er **je Decoder eine Lautsprecherlast**; der 59649 ist ein LokPilot ohne Sound, seine Schnittstellenzeichnung führt Pins 9/10 als unbelegt. Ein Lautsprecher am Slave ist daher keine Testvoraussetzung. ESUs 53900-Anleitung zeigt außerdem AUX3/AUX4 an 21MTC als Logikpfade, während der 59649 diese verstärkt ausführt. Die genaue 53900-Revision darf nicht allein durch „Schalterstellung nach Anleitung“ als geklärt gelten.

**Primärbelege:** ESU LokPilot-5-Anleitung, 8. Auflage 2023, S. 10/19; [ESU 53900 Anleitung, 2. Auflage 2019](https://www.esu.eu/download/betriebsanleitungen/profi-pruefstand/?no_cache=1&tx_esudownloads_pi1%5BdownloadItem%5D=3e2cdb190091da48cc2030b2734bbd32) (lokale gesicherte Originaldatei `esu_53900_2aufl_2019.pdf`, Herkunft/Hash im Quellenmanifest); [Märklin 60970](https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf), S. 5 sowie Schalterzeichnungen. Die Produktwahl ist noch keine Freigabe am vorhandenen Gerät.

**Korrigierte Empfehlung:** Zunächst vorhandene Aufnahmen mit Artikel/Revision/Fotos erfassen; danach je Aufnahme Gleiseingang, Index, Motor-/Quittierlast, LV/LR-Anzeige und AUX3/4-Pegel festlegen. Nur am 60977 eine passende Soundlast mit begrenzter Anfangslautstärke. Ohne geeignete Aufnahme den Vorabtest offenlassen und gezielt leihen/beschaffen; den Prüfstand nicht mit einem Händlerauftrag verwechseln. Kein pauschaler Zwang zu zwei gekauften Kompletttestern, wenn gleichwertige getrennte dokumentierte Aufbauten vorhanden sind.

## V-05 – Firmwarediagnose und vermeintlicher Widerspruch

**Fundstellen:** REV11 S. 9 Titel/Ziel, Schritte 4/5; S. 10 Titel/Ziel, Firmwarekasten und Schritte 1–6; S. 29 erste Zeile. REV10 F.11.2, Lesefassung Zeilen 1853–1856, hatte den damaligen Recherchehinweis tatsächlich ausdrücklich gesperrt. REV11 ersetzt ihn durch einen begrenzten, indexgetrennten Ablauf; das ist eine bewusste inhaltliche Änderung.

S. 9 beschreibt nur das **zuerst** erfolgende Grundlesen. S. 10 heißt ausdrücklich „Firmware lesen und Einzelwerte schreiben“. Bekannte Indexwerte für eine bestimmte Bank sind keine Probierwerte. Auch der auf S. 9 vorhandene Satz verbietet nicht jede spätere vorbereitete CV-Änderung. Ein logischer Widerspruch ist deshalb nicht belegt. Der zusätzliche Schreibzugriff selbst ist real, ebenso die verbleibende K3- statt Herstellerqualität der Firmwarekarte. Die Version hat einen Nutzen als reproduzierbarer Diagnosezustand; „ohne Nutzen“ ist zu stark. Ein allgemeiner Mindeststand für die konkrete Mischherstellerkombination lässt sich aus dem ESU-LokSound-Beispiel nicht ableiten.

**Primärbelege:** [JMRI v5standardCVs.xml](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v5standardCVs.xml), Einbindung `v4decoderInfoCVs`; [JMRI Firmwaredefinition](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml#L59), Index 0/255, Build aus zwei Bytes, Minor/Major; [ESU Synchronisation](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/) behandelt LokSound 5 ab 5.1.101.

**Korrigierte Empfehlung:** Dokumentation und Funktionsfreigabe ausdrücklich trennen. Optionalisierung der K3-Diagnose ist möglich, muss jedoch auch S. 11 und S. 29 konsistent anpassen. Kein „nicht lesbar“ als Ersatz für die gesamte Decoderidentität oder Paarfunktion verwenden. Bei Unterbrechung Indexzustand zuerst frisch lesen; ursprüngliche Werte kontrolliert wiederherstellen. S. 10 kann die CV8-Sperre lokal wiederholen. Dezimale Bytes 0–255 sind dort bereits vorgeschrieben; die ausdrückliche Warnung gegen falsch übernommene Hexadezimalwerte verbessert nur die Bedienung.

## V-06 – Kein Plan B

**Fundstellen:** REV11 S. 11 STOPP/WEITER; S. 38 Eingangssatz und Zeile „Slave folgt nicht“; S. 10 STOPP. Die Anleitung untersagt bereits blindes Wiederholen und unmotivierte weitere CV-Änderungen. Der Bericht konstruiert daraus zu stark eine Anweisung zu unbegrenzten Schreibversuchen. Richtig ist, dass ein geordneter Weg nach einem korrekt dokumentierten negativen Paarversuch fehlt.

**Quellen:** ESU-Herstellerbeispiel siehe V-05; der im Bericht bezeichnete Stummiforum-Beitrag ist Erfahrungs-, kein Herstellerbeleg. Zwei Versuche sind keine aus Herstellerunterlagen oder Protokollnorm abgeleitete Grenze. 53451 kann Zugang und vollständige Einrichtung ermöglichen; sein Kauf garantiert nicht, dass jede Firmware-/Masterkombination funktioniert.

**Korrigierte Empfehlung:** Nach einem gescheiterten gültigen Versuch Ursache anhand Kennung, Export, rückgelesenen Werten, aktiven Protokollen und Ausgangsbeobachtung eingrenzen. Wiederholen nur bei neuem Nachweis oder begründet korrigierter Ursache; unveränderte Wiederholungen bringen keinen Erkenntnisgewinn. Bleibt die Ursache offen: konkrete ESU-Auskunft oder passender LokProgrammer-Zugang zur Diagnose. Architekturänderungen sind ein neues Konzept und keine stillschweigende Aufgabe der Nutzerziele.

## V-07 – SID-Wechsel ist mit dem angebotenen Bedienweg nicht belegt

**Fundstellen:** REV11 S. 11 Schritte 4/5, STOPP und WEITER. Zwei verschiedene tatsächliche SID-Werte sind ausdrücklich ein Pflichtkriterium; eine unabhängige MS/Gleisbox garantiert keine neue SID. Der Text benennt einen „konkret bestätigten passiven Datennachweis“, liefert aber keine vorhandene Hardware oder fertig ausführbare Anleitung dafür.

**Primärbelege:** [Märklin CAN 2.0](https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf), MFX Bind/Verify, S. 28/29; [Mobile Station](https://static.maerklin.de/damcontent/2a/47/2a470bed20017f68f92306725d49fca81702905959.pdf). Bind/Verify trennt dauerhafte UID und zugeteilte SID. Ein Datensatz nach Rückkehr auf die CS3 belegt den Zustand an dieser CS3, nicht rückwirkend die Betriebsadresse im unabhängigen MS-System.

**Korrigierte Empfehlung:** Vor Beginn des Wechseltests festlegen, welches tatsächlich verfügbare Mittel die zweite SID nachweist: ablesbare unabhängige Zentrale oder bestätigter passiver Mitschnitt mit UID/SID und Steuerbarkeit. Fehlt dieses Mittel, lediglich Neuanmeldung/Folgeverhalten dokumentieren; das stärkere SID-Kriterium bleibt offen. Soll eine eingeschränkte stationäre Abnahme ausreichen, diese Scope-Änderung klar benennen und S. 11/S. 29 entsprechend ändern. Der Bericht darf nicht „SID-Wechsel unbewiesen“ eintragen und anschließend das unveränderte Gesamtgate als geschlossen behandeln.

## V-08 – HTTP-Weg und `address`

**Fundstellen:** REV11 S. 7 Schritte 3/4 und Tabelle. Die Quelle Q14 ist ein CS2-Textformat mit `.adresse` und `.sid`; in diesem Format ist `address` der falsche Suchbegriff. Als allgemeine Behauptung ist „falscher Feldname“ jedoch falsch: das originale CS3-JSON-Testmaterial enthält tatsächlich `address`.

**Eigene Code-/Datenprüfung:** Im festgelegten TrainControl-Commit bietet `CS2File.java` `getLocURL()` mit `/config/lokomotive.cs2`, getrennt davon `getCS3LocDBUrl(int)` mit `/app/api/loks` vor 2.6.0 bzw. `/app/api/locos` ab 2.6.0; `parseLocomotivesCS3()` verwendet den API-Pfad. Das beweist die API-Nutzung, **nicht** die Unmöglichkeit des anderen HTTP-Pfades. Erster JSON-Testdatensatz: `uid=0x4027`, `mfxuid=0x73f1fcc5`, `address=39`; im CS2-Textdatensatz stehen entsprechende `.sid=0x27` und `.adresse=0x27`. Das sind ausschließlich fremde Testdaten.

**Primärquellen:** [TrainControl CS2File.java](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/src/org/traincontrol/marklin/file/CS2File.java), Methoden wie oben; [CS3 JSON](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/CS3_loks_v260.json); [CS2-Textformat](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/lokomotive_cs3.cs2).

**Korrigierte Empfehlung:** Sicherungskopie primär; den direkten Konfigurationspfad nur als am eigenen Gerät zu bestätigenden Lesekandidaten benennen. Formatabhängige Feldtabelle: CS2 `.mfxuid/.uid/.sid/.adresse`; CS3-JSON `mfxuid/uid/address` samt dokumentierter Versions-/Datensatzherkunft. Führende Nullen und Zahlenformat erhalten. Kein Rückschluss „API existiert, daher Dateipfad existiert nicht“.

## V-17 bis V-22 – Kürzungsverluste einzeln bewertet

- **V-17, S. 9/3 und S. 11/3:** Frühzeitiges Loklistenfoto und ausdrücklicher Hinweis auf mögliche Selbstanmeldung fehlen auf der Lesekarte. S. 11 behandelt alte gespeicherte Slave-Zeilen aber ausdrücklich. Loklistenfoto vor dem ersten ESU-Strom ist sinnvoll; dies als lokale Präzisierung statt vollständigen Verlust darstellen. Die mögliche M4-Selbstanmeldung stützt die LokPilot-5-Anleitung, Betriebs-/Anmeldeabschnitte.
- **V-18, S. 11:** Vor Ort fehlt das knappe Abschaltkriterium für Überlast/Geruch/unerwarteten Motorlauf sowie das Verbot der Konfigurationsbearbeitung im verbundenen Paar. Übergreifende Regeln stehen auf S. 27/38. Beide Sätze direkt an den Vorabtest zu setzen ist gerechtfertigt; andere Karten ersetzen bei einem Anfänger keinen gut platzierten Handgriff.
- **V-19, S. 9/10; REV10 F.11.3:** Reale DCC-/MM-Adressen und aktivierte Protokolle sind nicht mehr als Tabelle erfasst. Ersatz ergänzen: Serviceeintrag ist nur ein Bedienobjekt; dessen unbenutzte Adresse ändert keine im Decoder gespeicherte Adresse. Service-Mode ist nicht adressselektiv. Protokoll-/Adresswerte artikelgenau frisch erheben, sicherstellen, dass der Paartest mfx-Folgen und keinen DCC-/MM-Gleichlauf beobachtet. DCC als aktuellen Wartungszugang erhalten; keine pauschalen Protokollwerte neu schreiben.
- **V-20, S. 27/2–3:** REV11 schreibt keine pauschale Regel „Wert ≥16 → minus16“, sondern verlangt zuerst ein erkannt gesetztes Bit4. Es fehlt die laiengeeignete Erkennungsmethode. Die Fallunterscheidung 0–15 unverändert, 16–31 minus16, darüber stoppen ist für die aktuelle [Märklin CV-Tabelle mSD3](https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf) sachgerecht. Nur bei AUX4; Projektweg bevorzugt, übrige Bits erhalten und rücklesen. Kein Nachweis einer tatsächlich falschen CV51-Einstellung.
- **V-21, S. 9/10:** Der konkrete Auslöser ist gegenüber REV10 verloren. ESU LokPilot-5-Anleitung S. 57, §11.1.4 bestätigt CV54=0, danach F1 und eine schnelle autonome Motorbewegung. Kurzer Sperrhinweis direkt in den Programmierkarten sinnvoll; nichts davon ausführen. S. 11 enthält immerhin bereits „keine Einmessfunktion“.
- **V-22, S. 39/2:** Der Firmwarewert kann auf den Lesebeleg S. 7 zurückgeführt werden; lokaler CV7-Sperrhinweis sinnvoll. Die Ein-Puffer-Regel ist dagegen schon explizit enthalten: nur einen passend angebundenen Puffer am 60977, hinten keinen 60974 am ESU. „Nie zwei hintereinander“ als eigenständigen verlorenen Schutz zu zählen überbewertet eine bereits abgedeckte Regel. [Märklin 60974](https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf) bleibt Anschluss-/Firmwarequelle.

## V-29 – LokProgrammer ohne Hardware

**Fundstelle:** REV11 S. 8 VORHER und Schritte 1–5/STOPP. Die Originalkarte verlangt schon einen dokumentierten Lauf mit Softwareversion, genauem LP5-MKL-Projekt, Optionsbildern und vollständigem Export. Ein Bildschirmfoto am eigenen PC ist daher kein neuer Ersatz für eine fehlende Karte, sondern das noch auszuführende Ergebnis dieser Karte.

[ESU CV-Änderungen anzeigen](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/) bezeichnet die Einführung **ab** 4.4.0; das ist keine Aussage „nur Version 4.4.0“. Die aktuell abgerufene [ESU Softwareseite](https://www.esu.eu/download/software/lokprogrammer/) listet 5.2.18 für LokPilot 5. Daraus allein lässt sich kein bestandener Lauf der individuellen 5.x-Installation ableiten, aber ebenso wenig eine Hardwarepflicht für reine Projektbearbeitung. Die Karte stoppt ausdrücklich, falls Option/Eingabe/Export fehlen.

**Korrigierte Empfehlung:** Status „eigener Offline-Nachweis offen“ beibehalten und die verlangten Aus-/An-/Aus-Exporte tatsächlich durchführen, sobald ein passender Windows-Rechner zugänglich ist. Die allgemeine Softwarefähigkeit nicht als bestätigten Dokumentfehler darstellen. Kein vorsorglicher 53451-Kauf allein wegen fehlenden Screenshots.

## V-30 – Quellendeckung

**S. 8 / Byteformel:** Q13 nennt CV191 und `CV="192:4"` mit `splitHexVal`. Die explizite Gewichtung stammt aus der JMRI-Verarbeitung des Split-Wertes; deshalb `SplitVariableValue.java` zusätzlich zitieren und die Formel als aus Implementierung abgeleitet bezeichnen. Dies präzisiert die Belegkette; die Formel ist richtig. [SplitVariableValue](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/jmrit/symbolicprog/SplitVariableValue.java).

**S. 6 / 53900:** 0,5 W ist in der originalen 53900-Anleitung bestätigt. Q19 ist nur die Produktseite. Die konkrete Anleitung zusätzlich verlinken; keine Zahl entfernen und keine volle Lautstärke daraus freigeben. Der Bericht sollte Quellenmangel von materiell falschem Grenzwert trennen.

**S. 28 / RCN-216:** Diese Norm regelt DCC-Programmierung, einschließlich Quittierung. Sie begründet keine AUX-Stromgrenze oder konkrete Werkstatt-Laststufenmessung. Fußnote enger zuordnen; die elektrische Messmethode bleibt gesondert gegen V-02 zu prüfen und wird durch Umnummerieren der Quelle nicht repariert.

## Gesamturteil dieses Teilumfangs

Der Bericht findet mehrere echte lokale Ausführungs- und Verständlichkeitslücken. Er ist in diesem Umfang **keine ungeprüft übernehmbare Korrekturvorlage**: sichere offene Nachweise werden teilweise als bewiesene Mängel gezählt; S. 9/S. 10 wird ein nicht vorhandener Widerspruch zugeschrieben; Ersatztexte vereinfachen Prüfhardware und SID-Nachweis unzulässig oder führen unbegründete feste Regeln ein. Die richtige Nachbesserung ist selektiv und erhält die Trennung zwischen einer fertigen Anleitung, vorhandener Ausrüstung und erst am realen Decoder möglichen Ergebnissen.
