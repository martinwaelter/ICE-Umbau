# Hardware-Audit: Eigenweg ohne Händler, Stand 10.09.2026

## Gegenstand und Ergebnis

Read-only-Prüfung der bestehenden REV10, insbesondere A (S. 7–8), 12d (S. 39–40), 16c/16d (S. 52–55), gegen die unten genannten Primärquellen. Geprüfte REV10: 92 Seiten, SHA-256 `2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0`. Keine Hardware bedient, keine vorhandene Anleitung geändert, kein Händler kontaktiert. Dieser Text diagnostiziert Dokumentations- und Nachweislücken, keinen gemessenen Hardwaredefekt.

**Ergebnis:** Ein Händler ist keine technisch belegte Voraussetzung. REV10 ersetzt jedoch bislang fehlende Prüfparameter durch die pauschale Personenvorgabe „fachkundig bestätigt“. Diese Personenvorgabe kann entfallen, sobald konkrete, reproduzierbare Kriterien an ihre Stelle treten. Die unbekannte reale Bestückung und das unbekannte Messgerät lassen sich nicht durch redaktionelle Freigabe ersetzen. Der ESU 53900 darf weiterhin nicht pauschal als fertig geeignete Aufnahme für beide Decoder behandelt werden; der Märklin 60970 ist wegen seiner dokumentierten Umschalter der besser belegte Kandidat. Motorlose DCC-Rücklesbarkeit muss nicht zur Voraussetzung des Gesamtprojekts werden, wenn die spätere Wartung verbindlich auf der getrennten Prüfaufnahme erfolgt.

## H1 — 16d: reale Prüflücke, unnötig pauschale Personenabhängigkeit

**Befund und Ursache.** 16d verlangt vor jeglicher Messung und jedem Einsetzen einen fremdbestätigten Plan, lässt aber Messpunkte, Messgeräteparameter und erwartete Anzeigen offen. 12d-6 verweist darauf zurück. So bleibt die Endprüfung auch nach gelungener Synchronisation nicht ausführbar. Die Ursache ist die Vermischung von drei unterschiedlichen Fragen: Herstelleranschluss zuordnen, eigenes Exemplar identifizieren und konkrete Messung bewerten. Aus fehlender Evidenz wird dadurch eine unbegrenzte Prüferpflicht.

**Primärevidenz.** Märklin beschreibt den Selbsteinbau, fordert die mechanische/elektrische Prüfung vor dem Umbau sowie einen offenen Ersttest am Programmiergleis. Eine allgemeine externe Abnahme wird dabei nicht verlangt. LED-Plus ist vom Fahrzeugrahmen zu trennen. ESU fordert nach dem Anschluss eine Ohmmeterkontrolle besonders auf Motor-/Schienenkurzschlüsse, ebenfalls ohne generelle Fremdabnahme. Diese Hinweise sind keine universelle Sollwerttabelle für eine fremde LoDi-Platine. [Märklin 60977, gedruckte S. 3–6][M77]; [ESU LokPilot 5, S. 27][E5].

LoDi benennt die Anschlussrollen selbst und unterscheidet Nicht-S/S sowie die Jumpervariante ab V1.50. Die Nicht-S-Lösung verbindet die beiden Schleifer; ab V1.50 wählt SJ1 AUX4, SJ2 AUX1, beide gleichzeitig sind verboten. VCC am Frontanschluss bezeichnet im Einbauablauf den LED-Plus-Anschluss. Die Seite ist ein Einbaubeispiel für 33701, kein vollständiger Schaltplan sämtlicher Revisionen. Eine erneute externe Bestätigung jedes bereits passend identifizierten Anschlussnamens ist deshalb unnötig; unbekannte Innenpfade bleiben unbekannt. [LoDi, Abschnitte 1 und Jumperhinweis][L].

Die Schnittstellennorm trennt Pin 12 Vcc (interne 1,8–5,7 V), Pin 16 U+ und Pin 20 GND von Pin 21/22 Stromabnahme. Die Norm definiert Funktionen und mechanische Anforderungen, keine konkreten Leiterbahnen oder Widerstandsanzeigen der LoDi-Platine. Die begriffliche Trennung in REV10 ist richtig. [RCN-121, S. 6–8][R121].

**Konsequenz.** Der Satz „Anleitung von dir allein nicht ausführbar“ beschreibt den aktuellen Textzustand. Er beweist weder eine prinzipielle Unmöglichkeit des Selbsteinbaus noch eine notwendige Händlerleistung. Umgekehrt wäre ersatzloses Streichen von 16d falsch: 16c prüft abgetrennte Leiter und kann einen erst beim Anschließen entstandenen Fehler nicht ausschließen.

**Konkreter Ersatz für den pauschalen 16d-Einstieg:**

> Diese Karte wird erst mit den Fotos deiner tatsächlichen Platinen und der Anleitung deines Multimeters vervollständigt. Für jede vorgesehene Messung werden die beiden zugänglichen Kontaktstellen, der vollständig spannungsfreie Aufbau, der bekannte Sollpfad, Messmodus und Prüfparameter sowie die erwartete Anzeige mit Abbruchkriterium angegeben. Du kannst die ausgefüllte Karte selbst abarbeiten. Nicht dokumentierte Messungen entfallen nicht, sondern bleiben mit der genau fehlenden Angabe offen. Eine offene Messung sperrt die betroffene Verbindung und deren Erststromtest. Bereits eindeutig identifizierte, getrennte passive Leitungen dürfen nach 16c geprüft werden. Erst nach der dokumentierten Anschluss- und Montageprüfung folgt das Einsetzen des jeweiligen Decoders.

Dieser Ersatz ist ein Redaktionsvorschlag, noch keine Messfreigabe. Er muss mit ausgefüllten Einzelkarten umgesetzt werden. „Von Fachprüfer freigegeben“ lediglich in „selbst freigeben“ umzubenennen würde die Ursache nicht beseitigen.

**Minimaler Restdatensatz für ausführbare Einzelkarten:**

1. Lesbare Vorder-/Rückseiten der tatsächlichen LoDi 511 und Märklin-Trägerplatine, Revision/Artikel, Jumperzustände, Ring A/B und vorhandene Bauteile; beide LED-Einsätze mit zugehörigen Widerständen.
2. Tatsächlicher Anschluss-/Montagezustand pro Kopf: vorhandener hinterer Schleifer, Radkontakt, S/RT/B/GR-Verbindung, Halter und Schrauben, Führung jeder neuen Litze. Ein nicht vorhandener Schleifer ist eine Bauentscheidung, keine Messaufgabe.
3. Multimeter-Modell samt Handbuch: Ohmbereiche, Prüfspannung/-strom, Messbuchsen und Offenanzeige. Fehlen dafür Angaben, wird ein nachweislich geeignetes Gerät/Verfahren gewählt; keine Eigenschaften aus der Gerätegattung ableiten.
4. Je Prüfpunkt nachvollziehbare Netzzuteilung: reine Kupferverbindung, Widerstand, LED/Halbleiterpfad oder unbekannt. Für unbekannte Pfade keine OL-Forderung und keine Probeverdrahtung; zuerst Dokumentation/Identifikation vervollständigen.
5. Berührungssichere Kontaktierung und positive Kontaktkontrollen vor/nach der Messung; festgelegter Zustand aller Decoder, Puffer, sonstiger Speicher und angeschlossener Lasten.

Für 12d genügt anschließend eine eindeutige Foto-/Anschlusskarte mit Abnahmekriterien für den realen S/RT/B/GR-Verbund. „Ohne geeigneten Platz Fachbetrieb“ kann durch „Montagevariante vor Fortsetzung konkret festlegen“ ersetzt werden. Kein Platz bleibt ein reales Problem; ein Händlername löst es nicht. Schrumpfschlauch, Zugentlastung, Bewegungsfreiheit und Anschlussprüfung aus 12d bleiben erhalten.

## H2 — 53900: dokumentierte Variantenunsicherheit; 60970 besser belegbar

**Tatsächlich geprüft.** Die derzeit angebotene ESU-Anleitung ist die 2. Auflage vom 17.10.2019. Ihre S. 2/4 zeigen 8/100 Ohm und OFF; S. 4 nennt 11×15 mm/0,5 W. Die Produktseite nennt dagegen 20 mm und 16/100 Ohm. S. 3 der Anleitung bezeichnet AUX3–6 am 21MTC-Anschluss als Logikpegel. Die vollständige S. 4 wurde zusätzlich gerendert und visuell geprüft. Das ist ein echter Dokumentwiderspruch; welche Variante ein vorhandenes oder geliefertes Exemplar besitzt, bleibt offen. [ESU 53900, S. 2–4][E539]; [ESU Produktseite][E539P].

Der 59649 besitzt dagegen verstärkte AUX3/AUX4 an der Schnittstelle. Die 53900-Unterlagen liefern keinen gesonderten Nachweis des Monitor-Eingangs für diese Variante. Das belegt eine fehlende Kombinationsevidenz, nicht einen zwingenden Defekt beim Stecken. Ein ausgebliebener AUX3/4-LED-Nachweis dürfte insbesondere nicht als kaputter Decoder bewertet werden. [ESU LokPilot 5, S. 15/19][E5].

Der 60977 unterstützt Glockenankermotoren und spezifiziert 4/8-Ohm-Soundlasten; bei 8 Ohm beträgt seine mögliche Soundleistung 1,6 W. Ein mit 0,5 W angegebener Prüflautsprecher ist damit keine belegte Freigabe für volle Decoderleistung. Ein möglicher begrenzender Prüfstandpfad ist hier nicht vermessen; ein Schaden ist nicht beobachtet. Passender Testpegel, Testdauer und tatsächlicher Lautsprecher müssen festgelegt werden; „8 Ohm passt“ genügt allein nicht. Die automatische Motoreinmessung bleibt auf der Prüfaufnahme ausgeschlossen. [Märklin 60977, S. 3–4/7][M77].

**Belastbarere Beschaffungs-/Leihspezifikation.** Der Märklin 60970 beschreibt AUX3/AUX4-Umschaltung zwischen Logikpegel und verstärkt, Motor/Funktion-Umschaltung, 8/100-Ohm-Impedanz und die Datenquelle Zentrale/USB ausdrücklich. Ein Decoder je Aufnahme, spannungsloses Stecken, Zentrale am Gleisanschluss sind dokumentiert. S. 24 wurde visuell geprüft. Damit lassen sich die Unterschiede beider Decoder ausdrücklich einstellen. Der gemeinsame mfx-Test benötigt zwei getrennte Decoderaufnahmen mit getrennten Lasten und gemeinsamer Gleisversorgung; für nacheinander ausgeführte Programmierung genügt eine. [Märklin 60970, S. 4–5, 21, 24–25][M70].

**Zu erstellende Eigenbedienkarte:** pro Exemplar Foto der Steckerorientierung, tatsächliche Ausgangsart, Lasten und Schalterstellungen; Datenquelle für diesen Versuch Zentrale, Programmeranschluss frei; getrennte Einzelprogrammierung und anschließender reiner Funktionstest beider Aufnahmen aus derselben Quelle. Für 59649 ist AUX3/4 „verstärkt“ durch die Typangabe belegt. Beim 60977 ist der ausgelesene Ausgangsmodus maßgeblich. Diese Karte bleibt von der Synchronisations-Wertekarte getrennt. Ein Prüfstandkauf bestätigt noch keine Programmierwerte, reale Firmware oder bestandenen C-Test.

## H3 — Motorloser DCC-ACK: echte Grenze, aber vermeidbare Projektabhängigkeit

RCN-216 beschreibt den DCC-Service-ACK als zusätzliche Stromaufnahme von mindestens 60 mA für 5–7 ms. Ein Motor kann den Impuls erzeugen, ist normativ aber nicht die einzig mögliche Realisierung. Besonders wichtig: Die Ausführung eines Schreibbefehls ist unabhängig davon, ob die Rückmeldung beim Programmiergerät erfolgreich ankommt. Fehlende Quittierung bedeutet daher nicht sicher „nichts geändert“. [RCN-216, S. 5][R216].

Der im ESU-Handbuch gezeigte 150-Ohm-Widerstand an AUX1 ist eine Anweisung für **59110/59120 LokPilot 5 Fx micro**, nicht für den **59649**. Seine Übernahme wäre eine unzulässige Modellverallgemeinerung. Die eingesehenen aktuellen Unterlagen belegen für den konkreten 59649 ohne Motor keine universelle ACK-Lastschaltung. [ESU LokPilot 5, S. 24][E5].

RCN-121 verlangt für Funktionsdecoder im motorlosen Einsatz interne Maßnahmen zur Service-Rückmeldung. Der 59649 ist ein Lokdecoder in MKL-Ausführung; diese Normpassage beweist dessen reale Implementierung nicht. [RCN-121, S. 8, Abschnitt 3.5][R121].

**Konsequenter Eigenweg:** Alle DCC-Lese-/Schreibarbeiten einschließlich späterer Änderungen erfolgen auf der einmal dokumentierten, getrennten Decoderaufnahme. Danach wird der Decoder stromlos wieder eingebaut; die betroffenen Anschluss-/Funktionsprüfungen werden wiederholt. Ein ungekuppelter Licht-/mfx-Betriebstest im hinteren Kopf ist von DCC-Service-Rücklesen zu unterscheiden. Es muss kein Motor oder Widerstand dauerhaft in den Kopf eingebaut werden, um diesen Wartungsweg zu ermöglichen. Das ist eine Ablaufentscheidung; sie behauptet weder, dass der reale motorlose Aufbau nicht lesen kann, noch dass ein bestimmter Prüfstand automatisch zuverlässig quittiert.

Die Anleitung sollte bei fehlender Rückmeldung abbrechen, erhaltene Ergebnisse sichern und vor weiterem Schreiben den tatsächlich gespeicherten Zustand auf der bestätigten Aufnahme neu lesen. Keine Wiederholungsserie vermeintlich wirkungsloser Schreibbefehle. Eine erfolgreiche Vorab-Leseprüfung bleibt erforderlich; sie darf jedoch am Wartungsaufbau stattfinden.

Zusätzlich ist „Programmiergleis“ kein Ersatz für die Anschlussprüfung: Die aktuelle RCN-216 erlaubt abweichende Strombegrenzungen bis 1 A und bei einstellbaren höheren Grenzen warnt sie vor Verdrahtungsschäden. Konkrete CS3-Schutzwirkung und Prüfstufe sind deshalb gerätebezogen zu bestimmen. [RCN-216, S. 4–5][R216].

## Grenzen und Abschluss

Keine der vorliegenden Unterlagen ersetzt die Fotos, Messwerte und Typangaben der realen Teile. Nicht diagnostiziert sind Kurzschluss, falsche Bestückung oder defekter Decoder. Für 53900 ist weder vollständige Eignung noch pauschale Unverträglichkeit nachgewiesen. Für 60970 ist die elektrische Anpassbarkeit besser dokumentiert, aber keine individuelle Kombination praktisch getestet. Eine fertig ausgefüllte Eigenprüfkarte ist der nächste konkrete Umsetzungsschritt; Händler- oder Kaufzwang folgt aus diesem Audit nicht.

Quellen sind frisch vom Hersteller/Normgeber abgerufen; vollständige lokale Kopien und SHA-256 stehen in `hardware_quellen/manifest.json`. Relevant gelesen: REV10 genannte Seiten vollständig; 53900 alle vier Seiten; LokPilot-5 Einbau-/Betriebs-/Programmierabschnitte und spezifische Anschlussbilder; Märklin 60977 deutscher Teil; 60970 deutscher Teil und Anschluss-/Schalterbilder; beide Normen sowie vollständiger LoDi-Einbautext. Keine Forenbehauptung trägt ein technisches Urteil dieses Audits.

[M77]: https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf
[M70]: https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf
[E539]: https://www.esu.eu/download/betriebsanleitungen/profi-pruefstand/?no_cache=1&tx_esudownloads_pi1%5BdownloadItem%5D=3e2cdb190091da48cc2030b2734bbd32
[E539P]: https://www.esu.eu/produkte/profi-pruefstand/
[E5]: https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e
[L]: https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/
[R121]: https://normen.railcommunity.de/RCN-121.pdf
[R216]: https://normen.railcommunity.de/RCN-216.pdf
