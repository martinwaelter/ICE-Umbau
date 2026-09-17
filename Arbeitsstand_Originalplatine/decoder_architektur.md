> **Fortschreibung 12.09.2026:** Die später gezielt recherchierte Platine 62762 ist jetzt aus zwei unabhängigen Quellen beidseitig fotografisch belegt. Frühere Aussagen dieses Arbeitsentwurfs über fehlende Vergleichsseiten oder aktive Bestückung der langen Platine sind entsprechend überholt. Maßgeblich sind die Dateien `recherche_62762_*.md`, der neue Bildbefund und `eingangsstand.json`. Die tatsächliche Netzzuordnung des eigenen Exemplars bleibt offen; 60972/60982 sind inzwischen als vorhanden genannt.

# ICE 2976: Decoderarchitektur mit Originalplatine

Prüfstand: 12.09.2026. Separate Architekturprüfung; REV13 bleibt unverändert. Zielannahme: Motorumbau 60941, Sounddecoder 60977 vorn, LokPilot 5 MKL 59649 hinten; Bedienung grundsätzlich wie REV13. Noch offen ist, ob nur LoDi Motor 511 oder sämtliche LoDi-Bauteile entfallen sollen.

**Befund:** Das Weiterverwenden der langen Originalplatine kann mechanisch sinnvoll sein. Es ersetzt aber keine der zwei benötigten 21MTC-Aufnahmen. Der derzeit am besten begründbare Plan ist, die vorhandene Märklin-Trägerplatine zum 60977 nach vorn umzusetzen und hinten eine einfache 21MTC-Adapterplatine zu prüfen. Das ist eine Planungsempfehlung, keine bereits geprüfte Einbau- oder Bestellfreigabe. Eine zweite, einzeln bestellbare Original-Trägerplatine mit belastbarer Märklin-Ersatzteilnummer konnte nicht belegt werden.

## 1. Belastbare Möglichkeiten für die zwei Decoder

| Möglichkeit | Elektrischer Nutzen | Vor einer konkreten Bauanweisung noch zu belegen |
|---|---|---|
| **A: Vorhandene Märklin-Trägerplatine vorn; einfache ESU 51967 hinten** | Sounddecoder bleibt auf der vorgesehenen Trägerplatine mit Lautsprecher- und SUSI-Steckanschluss. Hinten werden Gleiseingänge, U+ und benötigte Lichtausgänge auf getrennte Lötstützpunkte geführt. | Pin-zu-Lötpunkt-Zuordnung der tatsächlich vorliegenden 51967; passiver Durchgang ohne zusätzliche Ausgangsverstärker; isolierte Befestigung und Höhe mit aufgestecktem 59649. Dies ist der bevorzugte Prüfkandidat. |
| **B: Märklin-Trägerplatine bleibt hinten; einfache 21MTC-Aufnahme wie 51967 vorn** | Der vorhandene hintere Aufbau kann grundsätzlich erhalten werden. Vorn entsteht eine separate Verbindung zwischen 60977 und den belegten Fahrzeugleitungen. | Zusätzlich zum Pin-/Einbautest: Lautsprecheranschluss und passende zweipolige Verbindung; für 60974 zusätzlich vollständig belegter vierpoliger SUSI-Steckweg. Keine direkte Lötung an Decoderbuchse oder Kontaktstiften vorsehen. |
| **C: Zweite originale Märklin-Trägerplatine** | Könnte die dokumentierte Steckerbelegung auch vorn bereitstellen. | Konkrete elektrische Trägerplatine, Artikelnummer, Revision und Lieferumfang sind bisher nicht primär belegt. Eine reine Halteplatte ist kein elektrischer Adapter. Daher keine Ersatzteilnummer in Stückliste eintragen. |
| **D: Lose 21MTC-Kabelaufnahme** | Denkbar als platzsparender Kabelbaum mit gesicherter Aufnahme. | Bisher kein konkreter Herstellerartikel mit vollständiger Pinbelegung, Isolation, Zugentlastung und Abmessungen verifiziert. Nicht als fertige Lösung ausgeben; Next18-Kabeladapter passen nicht. |

Märklin beschreibt 60977 mit einer 21-poligen Schnittstelle und **einer** beiliegenden Trägerplatine. ESU beschreibt 51967 als einfache Aufnahme mit 21 Lötaugen; Außenmaß 22 × 17 mm, mit Befestigungszunge 27 × 17 mm. ESUs LokPilot-5-Anleitung, Abschnitt 19.4, unterscheidet diesen Adapter ausdrücklich von den Platinen mit Ausgangsverstärkung. Die Produktbeschreibung ersetzt allerdings noch keine dokumentierte Pinprüfung am verwendeten Bauteil. [Märklin 60977](https://www.marklin.com/products/details/article/60977), [ESU 51967](https://www.esu.eu/produkte/zubehoer/adapterplatinen/21mtc-adapterplatine/), [ESU LokPilot 5, Abschnitt 19.4](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e)

**51968 und 51957 sind hier kein austauschbarer Ersatz für 51967.** Ihre eigene Anleitung nennt Ausgangsverstärker und untersagt die Verwendung verstärkter AUX3/AUX4, wie sie bei der MKL-Ausführung vorkommen. Eine pauschale Empfehlung „beliebiger 21MTC-Adapter“ wäre deshalb falsch. [ESU Adapteranleitung, S. 2–3](https://www.esu.eu/download/betriebsanleitungen/zubehoer/?no_cache=1&tx_esudownloads_pi1%5BdownloadItem%5D=abf543f8aa750a868694130ca2ccee05)

## 2. Was die Originalplatine übernehmen darf

Die vorhandenen kleinen Fotos zeigen keine vollständig nachvollziehbare Bauteil- und Leiterbahnseite. Daher sind weder Schnittstellenpads noch Trennstellen, Gleichrichterpfade oder Lampenrückleiter des konkreten 2976 belastbar zugeordnet. Die veröffentlichten LoDi-Umbaufotos zeigen ausdrücklich einen **33701**; sie sind kein Schaltplan der Originalplatine des 2976. [LoDi: Varianten und Beispielzug](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/)

Für die neue Variante sind drei Fälle getrennt zu behandeln:

- **Mechanischer Träger:** Die alte Platine kann erhalten bleiben, während neue Decoderleitungen elektrisch unabhängig geführt werden. Auch dann müssen Bauteilhöhe, Isolation und vollständig geschlossener Wagenkasten passen.
- **Verifizierte passive Verteilung:** Einzelne nachverfolgte Leiterbahnen dürfen als Verbindungen dienen. Dazu gehören eine dokumentierte Zuordnung beider Enden und der Nachweis, dass kein unerwünschter Abzweig bestehen bleibt.
- **Alte Steuerung oder Umschaltung:** Eine aktive Analog-/Delta-Motorsteuerung darf nicht parallel am neuen Motorausgang verbleiben. Die Märklin-Einbaufolge verlangt das Ablösen der alten Anschlussleitungen und den Ausbau des alten Decoders/Umschalters. Eine bewusst erhaltene Restplatine benötigt deshalb einen gesonderten Plan, der die elektrische Trennung nachweist. [Märklin 60977, S. 4](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf)

## 3. Innenlicht, U+ und Stromaufnahme

**U+ ist der gemeinsame positive Decoderanschluss für Funktionen. Es ist weder Schienenmasse noch Motoranschluss.** Bei einem Wagenkreis aus dem 60977 darf ein vorhandener Rückleiter über Radsätze, Fahrzeugmasse oder eine alte Lichtschaltung nicht unbemerkt erhalten bleiben. Märklin verbietet die Verbindung des gemeinsamen orangefarbenen Leiters mit Fahrzeugmasse; bei massebezogenen Glühlampen beschreibt Märklin die Umstellung auf isolierte Fassungen. [Märklin 60977, S. 4–5](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf)

Damit ergeben sich folgende **Planungszweige**, keine bereits ausgeführten Messungen:

| Gewünschte Innenbeleuchtung | Konsequenz |
|---|---|
| LoDi-Wagenlicht bleibt | Tatsächlich vorhandene Wagenrevision und Versorgungsart beibehalten bzw. neu zuordnen. Ein „Motorplatine entfällt“ erlaubt nicht, Anschlussbezeichnungen oder Brücken ihrer Ersatzplatine unverändert auf die Märklin-Platine zu übertragen. |
| Originales Wagenlicht bleibt | Lampenzahl, Nennspannung, Kalt-/Betriebsstrom, Masseverbindungen und Kupplungswege ermitteln. Erst dann entscheiden, ob ein Decoder-AUX die Gesamtlast tragen kann oder ein getrennt ausgelegter Schaltweg benötigt wird. |
| Wagen erhalten neue andere LEDs | Je LED-Zweig Strombegrenzung, Polarität, Gesamtlast und Rückleiter neu auslegen; kein universeller Widerstandswert ohne Zweigdaten. |

60977 erlaubt am Motor dauerhaft höchstens 1,1 A, je Licht-/AUX1–4-Ausgang höchstens 250 mA, für Licht plus AUX zusammen höchstens 300 mA und insgesamt höchstens 1,6 A. Einschaltlast und übrige Verbraucher gehören in dieselbe Bilanz. Ein erhaltenes Glühlampensystem ist deshalb nicht automatisch eine zulässige AUX-Last. [Märklin 60977, S. 3](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf)

Die Gleiseingänge beider Decoder können nach dem geprüften REV13-Prinzip versorgt werden; die U+-Ausgänge beider Decoder bleiben getrennt. Eine ursprüngliche Schleiferumschaltung oder ein dauerhaft verbundener zweiter Schleifer ist gesondert nachzuweisen. LoDi erklärt selbst, dass seine Variante ohne Umschaltung die Schleifer verbindet und dass signalabhängige stromlose Abschnitte eine andere Lösung erfordern. Welche Funktion die Originalplatine tatsächlich erfüllt, folgt daraus nicht. [LoDi: Schleiferumschaltung](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/)

## 4. Frontlicht: Entfall von Motor 511 verändert die Widerstandsfrage

Falls LoDi-Front-LEDs bleiben, benötigen **jetzt auch vorn** beide Farbzweige ihre eigene belegte Strombegrenzung. Der Hersteller verkauft diese Einsätze ohne Vorwiderstände; in der LoDi-Motorplatine liegen die zugehörigen Widerstände R4/R5. Diese Widerstände verschwinden mit der Platine. Eine passive Decoderaufnahme stellt sie nicht wieder her. Hinten bleibt die bereits erforderliche getrennte Auslegung je Farbe bestehen. [LoDi Front: ohne Vorwiderstände](https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/), [LoDi Motor: R4/R5](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/)

Bleiben dagegen die Originalglühlampen, gelten deren reale Nenn- und Rückleiterdaten. LED-Widerstandswerte sind dann nicht übertragbar. PWM-Dimmung ersetzt bei einer nackten LED keinen Serienwiderstand; der Spitzenstrom während der Einschaltphase muss begrenzt werden.

## 5. Sound, SUSI und Bedienung

Der Sound entsteht im 60977. Die alte Märklin-Platine muss dafür kein SUSI besitzen. SUSI wird für den optionalen 60974 relevant: Märklin verlangt mLD3/mSD3-Firmware ab 3.2.0.1 und den vorgesehenen SUSI-Steckanschluss; die Steckverbindung und Einbaulage müssen frei zugänglich bleiben. Eine einfache 21MTC-Aufnahme mit herausgeführten Pins ist noch kein steckfertiger vierpoliger Anschluss. 60974 ist nicht als Puffer für 59649 ausgewiesen und puffert nicht automatisch einen außerhalb des Masterkreises versorgten Wagenkreis. [Märklin 60974, S. 4 und 28](https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf)

Ein Wechsel der Trägerplatine ändert nicht die Softwarevoraussetzungen der vorgesehenen Master-/Slave-Bedienung. Die persönliche Kennung, der belegte CV-Export, der Wartungszugang und die tatsächliche Paarprüfung aus REV13 bleiben erforderlich. Der mechanische Umbau allein beweist keinen funktionierenden gemeinsamen Zugeintrag.

**Nächste belastbare Arbeitsstufe:** Umfang der entfallenden LoDi-Teile festlegen; Originalplatine beidseitig samt Anschlüssen identifizieren; Versorgung, Motor- und Lichtkreise nachvollziehen; zwei Aufnahmen samt Einbaumaßen auswählen; danach einen konkreten Anschluss- und gegebenenfalls Trennstellenplan sowie die neue Lastbilanz erstellen. Erst dieser Plan ermöglicht eine detailgetreue separate Bauanleitung. Es wurde nichts gekauft, bestellt oder an der Hauptanleitung geändert.

Abrufgrenze: Der über die offizielle 60977-Produktseite verlinkte Märklin-Ersatzteilaufruf war am Prüfdatum nicht abrufbar. Daraus folgt keine Aussage über tatsächliche Lieferbarkeit; eine zusätzliche Original-Träger-Ersatzteilnummer bleibt unbestätigt.
