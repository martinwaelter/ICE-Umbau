# Vollständige Umbauanleitung mit Originalträger 62762 – Inhalt und Arbeitsfolge

Redaktionsgrundlage vom 12.09.2026. **Zielumfang: 44 gut lesbare Seiten.** Alle folgenden neuen Seitenzahlen beziehen sich auf diese Folge; die Spalte REV13 nennt die alten finalen Seiten 1–46 aus `Arbeitsstand_REV13/rev13_pages.json`.

Arbeitsannahme für diese Ausgabe: **60977 mit Sound vorn, ESU 59649 hinten; LoDi-Motorplatine 511 entfällt. LoDi-Fronten und Wagenmodule bleiben wie REV13.** Der 60977 nutzt vorn seinen originalen Märklin-21MTC-Träger; der zusätzliche leere Träger/Halter des vorhandenen 60972-Satzes wird hinten verwendet. Der 60972-Decoder und der 60982 werden in diesem Aufbau nicht angeschlossen. Diese Decoderwahl ist eine ausdrücklich benannte Ausgabeannahme, bis die bereits gestellte Nutzerfrage beantwortet ist. Farbtabellen des 60982 dürfen in diese Ausgabe nicht geraten.

**Konstruktionsprinzip:** Die originale lange 62762 bleibt im motorisierten Kopf als mechanischer Träger erhalten. Neue Motor-, Licht- und Gleisleitungen werden elektrisch unabhängig von ihren alten Leiterzügen geführt. Der alte Schalter und etwaige über Schrauben mit Metall verbundene Kupferflächen bleiben ohne Funktion für die neue Elektrik. Damit benötigt der Grundaufbau weder eine erfundene Leiterbahntrennung noch eine ungeprüfte Belastbarkeit alter Kupferpfade. Das ist eine bearbeitete und weiterverwendete Originalplatine, keine Austausch-Leerplatine.

## 1. Seite-für-Seite-Zusammenstellung

| Neu | Titel / praktisches Ergebnis | REV13 und konkrete Bearbeitung | Bild / Schema |
|---:|---|---|---|
| 1 | **ICE 2976 mit erhaltener Märklin-Platine** – Ausgabeannahme, Funktionsziel, sechs Arbeitsabschnitte | 1 neu formulieren. Originalträger, zusätzliche kleine Aufnahme und Decoder sichtbar auseinanderhalten. | Neues Systembild: 62762 als Träger, darüber 21MTC, Motor/Front/Wagen als getrennte Kreise. |
| 2 | **Vorhandene Baugruppen zuordnen** | 2: 511 entfernen; 60977-Träger vorn, leerer 60972-Träger hinten; Isolier-/Befestigungsmaterial, Serienwiderstände beider Fronten und neu bestätigte GE-Schaltstufe ergänzen. Keine pauschale neue Adapterbestellung. | Zwei reale kleine Träger mit Zuordnungsfeld; Originalplatine getrennt benennen. |
| 3 | **Aus vorhandenen Gleisen den freien Prüfabschnitt aufbauen** | 3 weitgehend übernehmen. Kein vorhandenes separates Prüfgleis behaupten. Physisch von der Anlage getrennte Geraden, ausreichende Länge je Stufe, ein abziehbarer zweipoliger Anschluss. Noch kein Einschalten. | Getrennter Abschnitt und alternativ belegte Prog-/Betriebsbuchse. |
| 4 | **Kupplungen früh prüfen und Enden markieren** | 4 übernehmen: jedes Fahrzeugende, tatsächliche Kontakte, Orientierung. Fehlender Kontakt betrifft dessen spätere Verbindung, nicht mechanische Arbeiten am Motor. | Kontaktfoto plus nummerierte Fahrzeugenden. |
| 5 | **Netze und Messgerät verstehen** | 5 übernehmen; alle LoDi-Motorpadnamen entfernen. B, 0, U+, GND, M1/M2 und GE erklären; beide Decoder-U+ getrennt. Speicherentladung für Wagen bleibt vollständig. | Netztabelle und COM/VΩ. |
| 6 | **Freie Leiter und eigene Lötverbindungen prüfen** | 6 + Kern aus 7 verdichten: positive Vor-/Nachprobe, Endlagen, direkte Pfade. Die bisherigen front-/hinten-/wagenspezifischen Zeilen entfallen hier, weil sie auf 23/26/29 konkret stehen. Bestückte Querpfade erhalten kein pauschales OL-Soll. | Eine gemeinsame Fünfschrittfolge und ein kleines Feld „Leiter / Widerstand / Elektronik“. |
| 7 | **Decoderaufnahmen und Geräteweg** | 8 anpassen: zusätzliche nackte Träger sind keine kompletten Prüfstände. Bestätigte geeignete Prüfaufnahmen samt Lasten bleiben für den dokumentierten Geräteweg erforderlich; Einzelarbeiten und Softwarevorbereitung trennen. | Geräteweg mit expliziter Quellenumschaltung. |
| 8 | **60970 richtig anschließen** | 9 übernehmen, neue Verweise. Keine Änderung der AUX-Pegelregeln. | Märklin-Originalbild Schalterübersicht. |
| 9 | **Masterprojekt und Kennung sichern** | 10 übernehmen. 60977 bleibt der Master; tatsächlicher Programmerartikel muss zum 60971-Ablauf passen. | Originalansichten und Datenfelder. |
| 10 | **Persönliche Synchronisation offline vorbereiten** | 11 übernehmen. Kein fertiger fremder CV-Satz. | Nachvollziehbarer Export-/Vergleichsweg. |
| 11 | **ESU allein lesen und Ausgangszustand sichern** | 12 übernehmen. Passende externe Motorprüflast erhalten. | Einzelaufbau. |
| 12 | **Belegte Werte schreiben und rücklesen** | 13 übernehmen. Decoderwahl 60972/60982 ist keine stille Ersatzoption für diesen ESU-Schritt. | Wertetabelle und Rücklesekette. |
| 13 | **Decoderpaar vor dem Fahrzeugumbau prüfen** | 14 übernehmen. Gemeinsamer mfx-Eintrag, Zustandswechsel und gespeicherte Projekte real nachweisen. | Paaraufbau; nur Gleiseingänge gemeinsam. |
| 14 | **62762 erkennen und jeden alten Anschluss markieren** | Neu; eigenes Foto aus 15 und neue verifizierte Vergleichsbilder. Arbeitsanweisung A unten. | Eigenes 0D2DC-Foto groß; rechte 62762 aus Vergleich daneben. Keine Anschlussfunktionspfeile aus Fremdfoto. |
| 15 | **Originalplatine ausbauen, alte Elektrik trennen und passiv aufnehmen** | Neu; alter Ausbauanteil aus 15 hierher. Arbeitsanweisung B unten. Platine aufbewahren und wiederverwenden. | Beide belegten 62762-Seiten mit neutralen Orientierungspunkten plus kleine Aufnahmetabelle. |
| 16 | **60941 im freien Motorraum montieren** | HLA-Anteil aus 15. Die aufbewahrte lange Platine jetzt noch nicht wieder einsetzen; erst freier Motoraufbau und Prüfung. | Eigenes BAD231-Motorbild + Märklin-60941-Explosionszeichnung. |
| 17 | **Kondensatoren unterscheiden und Drosseln einbauen** | 16 übernehmen; „LoDi“ durch „neue Decoderaufnahme“ ersetzen. | Geprüfte Motorvergleichsbilder, jeweils ausdrücklich 33701. |
| 18 | **Vier Messclips richtig setzen** | 17 übernehmen. Motor vollständig von alter und neuer Elektrik getrennt. | Unveränderte detaillierte Messpunktabbildung. |
| 19 | **Motorisolation mit Vor- und Nachproben prüfen** | 18 vollständig erhalten; keine Zusammenlegung mit Clips oder HLA. | Sechserfolge und Ergebnistabelle. |
| 20 | **62762 wieder einsetzen und 21MTC isoliert befestigen** | Neu, Montageprinzip aus 22 übernehmen; Arbeitsanweisung C unten. Jetzt ist der Motor geprüft und der Träger kann zurück. | Eigenes Geometriebild, Original-Halteplatte und neues beschriftetes Schnittschema. |
| 21 | **Beide Fronten mit eigenen Serienwiderständen aufbauen** | 20 neu: nun vorn **und** hinten je Weiß und Rot begrenzen. R4/R5 der entfallenen 511 sind nicht vorhanden. Stromdaten/konservative Auslegung je wirklichem Einsatz. | Zwei gleiche Zweigschemata, vier getrennte Widerstände. |
| 22 | **Frontmessungen vorbereiten** | 21: jetzt nur Messpunkte/Wege. Ausführen erst auf 34/35. Alle Hinweise auf unzugängliche 511-R4/R5 löschen. | Spannungs- oder alternative Serien-Strommessung; nicht beides gleichzeitig verlangen. |
| 23 | **Motorseite nach der neuen Netzliste verdrahten** | 23 vollständig neu: Märklin-Träger-Anschlussnamen; durchgehend isolierte neue Leitungen; GE über bestätigte neue Schaltung. Arbeitsanweisung D unten. Motor-Servicezugang vor endgültigem Löten festlegen. | Neues Gesamtstromlaufschema und belegte Märklin-Trägerzeichnung; 62762-Kupfer bewusst ohne neue elektrische Anschlusslinien. |
| 24 | **Satzlautsprecher direkt am Märklin-Träger stecken** | 24 vereinfachen. Original-Satzstecker bleibt erhalten und passt an die vorgesehene Lautsprecherbuchse; bisheriger LoDi-Gegenstecker-/LS1-/LS2-Umbau entfällt. Ein Lautsprecher, freie Membran, sichere Schallkapsel. | Originalbuchse mit LS-Beschriftung, realer Satzlautsprecher. |
| 25 | **Zusätzlichen Märklin-Träger im Gegenkopf montieren** | 25 neu zuordnen: Träger aus zusätzlichem 60972-Satz. Tatsächlichen Halter/Platz und isolierte Befestigung prüfen. Die eigene 62762 im Motorkopf nicht mit der entfernten Vergleichsplatine hinten verwechseln. | Märklin-Trägerzeichnung; fremdes 33701-Gegenkopffoto nur als mechanischer Vergleich. |
| 26 | **Gegenkopf getrennt verdrahten** | 26 erhalten: S/RT/B-Dreiwegpunkt, eigener Radkontakt, U+ hinten, Rot über R an LV und Weiß über R an LR; GE hinten einzeln isoliert. | Geprüftes Rückkopfschema mit Herkunft des Trägers korrigiert. |
| 27 | **Wagenmodule erkennen und einbauen** | 27 übernehmen: eigene Revision und O/L-Längspfade. | Originalbilder weißer Wagenleiste, lesbare Pads. |
| 28 | **Jeden Kupplungsübergang prüfen** | 28 vollständig erhalten. Bei Aufruf von 23/26 danach zum jeweiligen Lötpunkt zurückkehren. | Kontakt-für-Kontakt-Zeichnung. |
| 29 | **RT an O und GE an L löten und prüfen** | 29 übernehmen. Tatsächlichen Lötauftrag ausdrücklich erhalten; Passive Prüfung vor und nachher. | Wagenbild plus Vorher-/Nachher-Tabelle. |
| 30 | **Optionalen Wagen-B-Radkontakt vorbereiten** | 30 übernehmen; jetzt ausschließlich passive Schritte 1–3. Aktive Schritte später begleitend zur ersten Wagenstufe 38. | Reale Kontaktoption, kein ungeprüftes Nachrüstteil. |
| 31 | **Mastermotor und Innenlichtausgang einstellen** | 31 an neue GE-Schaltung anpassen. Keine SJ1/SJ2-Auswahl mehr. Finales Soundprojekt und tatsächlicher AUX müssen zusammenpassen. | Einstellungen getrennt nach Motor, Ausgangsart und Funktionstaste. |
| 32 | **Vor dem Einsetzen beide Köpfe abgleichen** | 33 als vollständige Checkliste behalten. Aus alter 32 nur kurze Prüfreihenfolge hinzufügen; elektrische Grenzen auf 37 und Ersttestlogik auf 34. | Zweispaltige Pflichtnachweistabelle vorn/hinten. |
| 33 | **Beide Decoder korrekt auf ihre Märklin-Träger setzen** | 34 + 35 auf gemeinsame Steckmechanik kürzen. Je Kopf getrennt arbeiten: vorn 60977, hinten 59649. Keine LoDi-Steckorientierung/K1-Richtung mehr. | Große Märklin-Originalzeichnung mit Index und Seitenprofil; zwei Zuordnungslabels. |
| 34 | **Motorseite erstmals kontrollieren und testen** | 36 + Ersttestkern aus 32. Zuerst einzeln am Programmierausgang, dann nur nach unauffälliger Kontrolle spannungsfrei zum Betriebsausgang. Front, Sound, Kleinstfahrt in Stufen. | Nummerierte Handgriffe, Strom-/Reaktionsfelder. |
| 35 | **Gegenkopf allein und danach beide Fronten prüfen** | 37 übernehmen. Ruhetest allein; aktiv synchrones Licht zusammen mit dem Master. Keine motorlose DCC-Wartung im Wagen. | Dreizeilige F0-/Richtungstabelle. |
| 36 | **Den späteren Anlagenbereich prüfen** | 38 übernehmen. Beide Schleifer gemeinsam überbrücken Abschnitte; auch beim erhaltenen Originalträger. Noch kein unerlaubter Anlagen-Fahrtest. | Schleiferabstand und Bereichsgrenzen. |
| 37 | **Lastgrenzen und Messung je Wagenstufe** | 39 + kompakte 60977-Grenzwerttabelle aus 32. Neue GE-Schaltstufe und deren eigene Grenzen zusätzlich berücksichtigen. Motor-/Rohstrompfad nutzt neue Litzen, keine unbekannte 62762-Leiterbahn. | Lastbilanz und Messeinschleifung; 1,5 A als Quellenobergrenze klar von Ausgangsgrenzen trennen. |
| 38 | **Wagen stufenweise ergänzen, T1–T8** | 40 übernehmen und neue GE-Schaltung berücksichtigen. Messkarte 37 begleitet jede Stufe. Aktive B-Option nur hier. | Reale Wagenfolge mit steigender Last. |
| 39 | **T9: alle Funktionstasten und Fahrt** | 41 übernehmen; eigener Projektstand zählt. | Abnahmematrix. |
| 40 | **Sitzprobe und Zugang für die geschlossene Motorprüfung** | 42 übernehmen. „LoDi-Seite“ durch „Seite zum Märklin-Träger“ ersetzen. Erst Sitzprobe 1–2, dann weiter 41. | Serviceverbindung außen, keine provisorisch herausgequetschten Drähte. |
| 41 | **Endgültig schließen und geschlossen abnehmen** | 43 übernehmen. Verbindliche Rückkehr zu 40/3–4 nach dem Schließen; anschließend Serviceverbindung von außen schließen. | Mechanischer Abschluss + letzte Funktionsfelder. |
| 42 | **Fehler eingrenzen und warten** | 44 anpassen; 62762-Träger, neue Litzen und GE-Schaltstufe als getrennte Fehlersuche. Keine Leiterbahntrennung als Standardreparatur. | Kurze Fehler-/Prüfzuordnung. |
| 43 | **Puffer und Signalhalt als Ergänzung** | 45 neu vereinfachen: 60977 besitzt nun den vorgesehenen Märklin-SUSI-Trägeranschluss; Firmware und Originalsteckrichtung prüfen. Kein 60974 am ESU. Die Grundabnahme bleibt ohne Puffer. | Märklin-SUSI-Zuordnung statt unbekannter LoDi-Pufferstelle. |
| 44 | **Quellen und Bildlegenden** | 46 ergänzen: alte Quellen behalten, 62762-Originalersatzteillisten und eindeutig als Fremdfotos gekennzeichnete Bildbelege hinzufügen. Nur tatsächlich genutzte Quellen abdrucken; Detailarchiv verlinken. | Quellen in ausreichend großer Schrift, direkte Links. |

Die Kürzung entsteht durch **einheitliche Steckmechanik**, **Wegfall der 511-Identifikations-/Montagekarte**, **Verteilung der doppelten Ersttestübersicht** und **eine gemeinsame Grundlagenkarte für direkte Leiter**. Motorprüfung, hintere Verdrahtung, Wagenlast und Gehäuseabschluss bleiben jeweils eigenständige Karten. Keine Schriftverkleinerung zur Erreichung der 44 Seiten.

## 2. Druckfertiger Arbeitskern für die neuen Originalplatinen-Karten

### A – Seite 14: Erkennen und vor dem Ablöten markieren

**Ziel:** Du behältst deine lange Originalplatine. Jede alte Leitung bleibt nach dem Ausbau ihrem bisherigen Ziel zuordenbar.

**Vorher:** Zug vom Gleis nehmen und alle Fahrzeuge abkuppeln. CS3-Gleisstecker, Programmer, externe Versorgungen, Decoder und Puffer physisch trennen. Speicherzustand nach Seite 5 prüfen. Noch nichts ablöten.

1. Gehäuse an seinen vorhandenen Befestigungen lösen; Schrauben mit ihrem Einbauort ablegen. Gehäuse ohne Zug an Litzen abheben. Das eigene Übersichtsbild dient zur Wiedererkennung; das Vergleichsbild zeigt eine 62762 und keine Anschlussbelegung deines Zuges.
2. Platine so fotografieren, dass Motor, beide Enden und Befestigungen gemeinsam sichtbar sind. Im Foto „Motorseite“ und „gegenüberliegendes Ende“ eintragen. Den Aufdruck am realen Teil ablesen; zusätzlich Datum/Version abschreiben. Bei schlechter Lesbarkeit die geometrischen Merkmale vergleichen. Die Nummer allein entscheidet über keinen Lötpunkt.
3. Jede Leitung **an beiden Enden mit derselben neutralen Nummer** kennzeichnen, beispielsweise A01/A01. Farbe und tatsächlich sichtbares Ziel daneben notieren: Schleifer, Radkontakt, Bürstenfahne, alte Umschalteinheit, Lampenfassung, Dachkontakt oder Kupplung. Ein unbekanntes Ziel heißt zunächst „offen“, nicht „Masse“.
4. Die beiden tatsächlich verwendeten Befestigungsstellen als **Ring A / Ring B** markieren; Reihenfolge und Lage eventueller Scheiben dokumentieren. Diese Namen unterscheiden sich bewusst von M1/M2 des Motors.
5. Schalterstellung fotografieren. Bewegt sich die Platine nach Lösen der Schrauben nicht ohne Litzenzug, zunächst nur die erreichbaren Leitungen aufnehmen. Sie wird auf Seite 15 durch Ablösen der bereits markierten Leitungen zugfrei; nicht an Kabeln umklappen.

**Prüffeld:** Leitung A__ · tatsächliche Farbe __ · sichtbares Ziel __ · altes Pad im Foto __. Für jede Leitung wiederholen.

**Weiter:** Alle zu lösenden Leitungen sind eindeutig markiert. Fehlende alte Funktionsnamen werden durch die passive Zuordnung auf Seite 15 geklärt; sie werden nicht aus Kabelfarben geraten.

### B – Seite 15: Ausbauen und neue Elektrik vom Altträger trennen

**Ziel:** Die 62762 bleibt vollständig als Träger erhalten. Keine alte Verbindung kann unbeabsichtigt einen neuen Decoderanschluss erreichen.

1. Eine markierte Leitung nach der anderen **an ihrer bisherigen Lötstelle** lösen. Mit einer Pinzette nur die freigegebene Litze abheben; nicht am kalten Lötpad ziehen. Das freie Ende weiter mit seiner Nummer kennzeichnen. Bis zur erneuten Verwendung jedes blanke Ende einzeln isolieren. Platine bei Bedarf auf nichtleitender Unterlage abstützen.
2. Originalschrauben lösen und die Platine abheben. Verdeckte Seite jetzt ohne Kabelzug ansehen und fotografieren. Auch dort noch angeschlossene Leitungen markieren und ablösen. Die alte Umschalteinheit und ersetzte Lampenfassung separat ausbauen und beschriftet aufbewahren. **Die 62762 selbst wird nicht entsorgt; den mechanischen Schalter nicht allein auf Verdacht auslöten.**
3. An der frei liegenden Platine jede alte Lötfläche im Foto neutral P1, P2 usw. nennen. Mit geeigneter Ω-Messung den direkten Kontakt zwischen den Pads, Ring A/Ring B und den Schalteranschlüssen aufnehmen. Je Schalterstellung einen eigenen Eintrag. Ein durchgehender Kupferpfad muss einen reproduzierbaren Leitungswert liefern; offene und wechselnde Pfade gesondert notieren. Messspitzenkontakt vor und nach jeder Reihe prüfen.
4. Die abgelösten Fahrzeugleitungen getrennt prüfen: Leitung zum Schleifer gegen den **wirklichen Schleifer**, Radleitung gegen den **wirklich genutzten Radkontakt**, Kupplungsadern nach Seite 28. So entstehen die neuen Arbeitsnamen B, 0, RT und GE. Motorleitungen erst im Zuge des HLA-Aufbaus neu festlegen. Keine Funktionszuweisung nur aufgrund des alten Platinenschalters.
5. Für den Grundaufbau bleiben **alle alten Kupfernetze ohne neue Decoderleitung**. Anschluss der neuen Elektrik erfolgt später direkt am kleinen Märklin-Träger beziehungsweise an vollständig isolierten Leitungsverbindungen. Alte Dach-/Schalter-/Lampenleitungen werden nicht versehentlich wieder angeschlossen. Für diesen Weg ist kein Leiterbahnschnitt erforderlich.

**Sichtprüfung:** Platine sauber, keine losen Zinnperlen oder verbliebenen blanken Drahtreste; Schalter mechanisch fest; keine eingerissenen Befestigungsstellen. Gelöste Baugruppen sind beschriftet verwahrt.

**Weiter:** Originalträger beiseitelegen. Erst Motor aufbauen und nach Seiten 16–19 prüfen; danach Originalträger wieder einsetzen. Ein unklarer alter Schalterpfad verhindert seine elektrische Weiterverwendung, nicht den beschriebenen mechanischen Erhalt mit unabhängigem Kabelbaum.

### C – Seite 20: Originalträger und isolierte 21MTC-Aufnahme montieren

**Vorher:** Motorprüfung Seite 19 bestanden. Alle alten Leitungen von der 62762 getrennt, neue Decoder noch nicht angeschlossen. Originalschrauben, vorgesehene Märklin-Halteplatte und geeignete nichtleitende Befestigung bereitlegen.

1. Die 62762 in ihrer ursprünglichen Lage auf ihre vorhandenen Auflagen setzen. Nur die zugeordneten Originalschrauben und Scheiben verwenden. Zuerst beide Schrauben leicht ansetzen, dann gleichmäßig sicher anziehen. Nach jeder Schraube planliegenden Sitz, freien Motorraum und gequetschte Litzen ausschließen. Keine neuen Löcher in Leiterplatte oder Chassis bohren.
2. Nach dem Verschrauben messen, welche alten Kupferflächen über Ring A oder Ring B zum Chassis führen. Dies dokumentiert den tatsächlichen Einbauzustand. Ein solcher alter Metallpfad wird **nicht** als U+ oder als neuer Motor-/Lichtleiter benutzt; im Grundaufbau bleibt er elektrisch ungenutzt.
3. Den kleinen **Märklin-Träger samt zugehöriger Halteplatte** auf einer freien Stelle der langen Platine positionieren. 21MTC-Steckrichtung, Steckerzugang, Lautsprecher/SUSI und spätere Decoderhöhe berücksichtigen. Kein Gehäusedruck, kein Kontakt zu Bürstenfedern, Motor, Schraubköpfen oder blankem Altkupfer.
4. Die elektrische Aufnahme bleibt in ihrer vorgesehenen Halteplatte. Zwischen dieser Halteplatte und gefährdenden alten Metall-/Kupferflächen eine mechanisch festliegende, temperaturgeeignete Isolierunterlage vorsehen. **Isolierung allein ist keine Befestigung.** Den Halter an vorhandenen freien Trägerbereichen mit nichtleitenden Befestigungsmitteln gegen Verschieben und Abheben sichern; keine Bindung über Decoder, Steckleiste, Bauteile, Kabel oder Lötstellen führen. Eine Befestigung muss sich setzen lassen, ohne Litzen einzuklemmen oder die lange Platine zu biegen.
5. Den realen Haltesitz von Hand vorsichtig in Längs-, Quer- und Hubrichtung prüfen. Er darf sich beim späteren Decoderstecken nicht bewegen. Die gewählte Befestigung und Unterseite fotografieren. Ein loser Isolierstreifen, Litzen als Halter oder das geschlossene Gehäuse als Klemmvorrichtung genügen nicht.
6. Beide Drehgestelle und Kupplungen in ihre normalen Endlagen bewegen. Die noch folgende Verkabelung benötigt freie Bewegungsschlaufen. Die elektrische Endkontrolle und der tatsächliche Decodersitz folgen auf Seiten 23/32/33; geschlossener Freiraum auf 40/41.

**Konkrete Montageentscheidung für die Produktion:** Das Schema soll **Original-62762 → festliegende Isolierung → originaler Märklin-Halter → kleine 21MTC-Platine → Decoder** zeigen. Bei der schematischen nichtleitenden Sicherung kann eine um vorhandenen freien Träger und Halter geführte Kunststoffbindung dargestellt werden, aber nur außerhalb der Bauteil-/Lötbereiche. Die Einbaumaße werden am Modell geprüft; keine erfundene Millimeterposition oder neue Bohrstelle. Sollte die tatsächliche Halteplatte eine andere Sicherung benötigen, ist genau diese mechanische Ausführung zu ersetzen, nicht die elektrische Architektur.

### D – Seite 23: Elektrisch unabhängige Neuverkabelung

**Vorher:** Motorprüfung, Trägermontage und beide Frontwiderstände vorbereitet. 60977 noch abgezogen. Alle neuen freien Litzen nach Seite 6 geprüft.

1. Vor dem Löten den bei geschlossenem Gehäuse erreichbaren, zweipoligen Motor-Servicezugang festlegen. Die Motorseite dieser Trennstelle führt zu den beiden Drosseln; die Decoderseite zum Märklin-Träger. Beide Seiten dauerhaft unterscheiden. Die Verbindung muss zum Motorstrom passen, berührungssicher und gegen Zug gesichert sein.
2. Die neuen Netze werden nach ihrem Ziel am **kleinen** Träger geführt: örtlicher Schleifer und RT-Verbindung an den bestätigten B/GR-Gleiseingang; wirklicher Radkontakt an 0/GL; Motorzweige an die beiden dokumentierten Motoranschlüsse; beide Frontzweige jeweils mit eigenem Serienwiderstand an LV/LR, gemeinsames Frontplus an +Ub. Die genaue Motor-Drehrichtung wird erst bei der kontrollierten Kleinstfahrt bewertet.
3. Das Wagenlicht erhält die vom Elektrikteil dieser Ausgabe festgelegte neue Schaltstufe. **GE ist kein alter 62762-Padname.** Die Schaltung muss Rohstrom-/Rückleiterbezug, tatsächlichen AUX, Lastgrenze und Abschaltzustand erklären. Hier keine pauschale direkte AUX→GE-Verbindung einsetzen und keine SJ1/SJ2-Brücke beschreiben; beide gehörten zur weggefallenen 511-Architektur.
4. Kurze blanke Stellen, vorab aufgefädelter Schrumpfschlauch und zugfreie Lötstellen verwenden. Jede neue Verbindung nach dem Abkühlen zuerst auf Durchgang bis zum tatsächlichen Ziel, dann auf ungewollten Kontakt zu Nachbarleitungen und sämtlichen erreichbaren alten Kupfer-/Ringflächen prüfen. Für direkte freie Leitungen gelten die Vor-/Nachproben von Seite 6. Durch angeschlossene Elektronik wird kein pauschales OL gefordert.
5. Leitungsbündel auf dem erhaltenen Träger befestigen; Kontakt mit seinen Kanten, Schraubköpfen, Schalter und alten Lötstellen vermeiden. Unbenutzte Leitungen einzeln isolieren. Nach Bewegung beider Drehgestelle und Kupplung die betroffenen Pfade erneut prüfen.

**Ergebnis:** Die originale Platine trägt den Aufbau, die neue elektrische Funktion liegt in dem eindeutig beschrifteten Kabelbaum und den vorgesehenen modernen Baugruppen. Kein elektrischer Schritt setzt eine vermutete Strombelastbarkeit oder verdeckte Verbindung der 62762 voraus.

## 3. Durchgehende Leserführung ohne Zirkel

- **3 → 5/6 → zurück zu 3:** Grundlagen vor der ersten passiven Gleisprüfung. Der CS3-Stecker bleibt abgezogen.
- **7–13:** Programmer-/Prüfaufnahmenweg und echter Decoderpaarnachweis. Eine nackte 60972-Schnittstellenplatine ist kein Ersatz für Motorlast und Funktionsanzeigen.
- **14 → 15 → 16–19 → 20:** Erst markieren und den Träger entfernen, dann frei am Motor arbeiten und messen, danach den Originalträger samt neuer Aufnahme montieren.
- **21/22:** Fronten auslegen und Messzugänge vorbereiten. Die aktive Zweigmessung wird erst bei **34/35** ausgeführt.
- **23 beziehungsweise 26 → 28 → zurück:** Kupplungsbelegung vor dem konkreten Löten erheben. **28 ist rein passiv.**
- **30:** B-Option jetzt nur Schritte 1–3; aktive Prüfung erst bei **38**, begleitet von **37**.
- **32 → 33 → 34 → 35:** Nachweise, tatsächlicher Steckersitz, einzelne Erstkontrollen, danach gemeinsame Frontprüfung. Erstkontrolle am Programmierausgang, Funktionsprüfung nach physischem Quellenwechsel. Eine Abschaltung wird nicht durch einen Versuch an einer stärkeren Quelle übergangen.
- **36 → 37/38 → 39:** Zuerst Anlagenbereich klären; Lastkarte begleitet jede Wagenstufe; vollständige Funktionstastenabnahme zuletzt.
- **40/1–2 → 41/1–3 → 40/3–4 → 41/4–5:** Sitzprobe, endgültiger Aufbau und Schließen, äußere Motorisolation, außen wieder verbinden und abschließend testen. Die Anleitung muss diese Teilnummern ausdrücklich beibehalten.

## 4. Bilder, die tatsächlich passen

**Eigene Bilder:** 0D2DC… für den originalen Gesamteinbau; BAD231… für alten Motor und verdeckt liegenden Raum unter dem langen Träger. Sie dürfen keine hochauflösenden Anschlussfakten vortäuschen.

**62762-Vergleich:** `belege_62762/ebay_147416253187_bild2.webp` rechts für Leiterzugseite; Bild 1 rechts für Gegenseite mit Schalter. Beschriftung „Fremdexemplar 62762 / 03/92 / VER1.1“. Das dicht bestückte linke 62761-Exemplar aus dem sichtbaren Detailrahmen halten beziehungsweise ausdrücklich abgrenzen.

**Herstellerbild:** `Arbeitsstand_REV10/quellen_alt/tmp/pdfs/rev5/research/dummy_full.jpg` enthält einen scharf lesbaren 62762-Aufdruck, zeigt jedoch einen **motorlosen 33701-Vergleichskopf**. Es eignet sich für Identifikation und Trägergeometrie, nicht als Schaltplan des eigenen Motors.

**Weiterverwenden:** Märklin-60941-Explosionszeichnung, Märklin-Träger-/Steckzeichnung, detaillierte Motorprüfbilder, Original-Front-/Wagenbilder. **Entfernen/ersetzen:** rote 511 als zukünftiges Einbaubild, K1-/LS1-/LS2-/SJ1-/SJ2-Detailpfeile, 511-Montageringzeichnung sowie alter Front-Gesamtstromlauf mit 511.

## 5. Noch im Hauptentwurf konkret zu setzen

Diese Inhaltsfolge ist vollständig. Vor dem fertigen Satz müssen die parallel erarbeiteten **neue GE-Schaltung und deren Lastgrenzen** auf Seiten 2/23/31/37/38 einheitlich eingesetzt werden. Ebenso müssen die Seiten 20/25 dieselbe tatsächlich darstellbare Befestigungsart verwenden. Das sind abgegrenzte Umsetzungsdetails innerhalb dieser Anleitung; kein weiterer Prüfbericht und keine pauschale Aufforderung zu zusätzlichen Fremdfotos.

Die endgültige Decoderwahl bleibt sichtbar als Ausgabeannahme, bis die bereits gestellte Frage beantwortet ist. Eine spätere Wahl 60972 oder 60982 **anstelle** 60977/59649 würde mehr als die Teileliste verändern: Soundziel, Farbschema und ESU-Master/Slave-Teil müssten dann tatsächlich neu geschrieben werden.
