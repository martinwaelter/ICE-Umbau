# Abschlussprüfung REV13

Stand: 12.09.2026. Auftrag: den vorgelegten REV12-Prüfbericht forensisch prüfen und notwendige beziehungsweise sinnvolle Korrekturen tatsächlich in die Anleitung übernehmen. Verbindliche Referenz bleibt die vom Nutzer benannte REV10; unmittelbare Arbeitsgrundlage war die abgeschlossene REV12.

## Ergebnis

[REV13-Werkstattfassung](</Users/martinwaelter/ICE Umbau/output/pdf/ICE_2976_Umbauanleitung_REV13_WERKSTATTFASSUNG.pdf>) ist die aktuelle Anleitung. Sie enthält **46 Seiten, 14 Foto-/Herstellerabbildungen, 14 Funktionsschemata und 36 Quellen**. Alle in REV12 verwendeten Fotoquellen sind erhalten. Die Ergänzungen wurden ohne Verkleinerung der vorgesehenen Schriftgrößen eingepasst.

[Der korrigierte Prüfbericht](</Users/martinwaelter/ICE Umbau/ICE2976_REV12_Pruefbericht_KORRIGIERT.md>) bewertet alle 36 Befunde einzeln und verweist auf die endgültigen Seiten der REV13. Das Original des Berichts und die Referenz-PDFs sind unverändert geblieben.

## Wesentliche inhaltliche Änderungen

- Nutzerbestand übernommen: Multimeter, Märklin-Decoderprogrammer, CS3 mit laut Nutzer aktueller Firmware; ausdrücklich kein separates Prüfgleis. Neuer konkreter Aufbau des getrennten Prüfabschnitts und frühe Prüfung aller Kupplungsübergänge.
- Prüfaufnahmen und Quellenwechsel präzisiert: reale 60970-Schalterstellungen, ESU-Belegung, begrenzte Einzelkontrolle, anschließender spannungsfreier Wechsel, Aufheben von STOP und erneuter Einzelanschluss nach dem Paartest.
- Programmierbehauptungen nachverfolgt: vollständige JMRI-Einbindungskette für die optionale Firmwarediagnose; reale Identitäts- und Paarprüfung bleibt nötig. Unbeabsichtigtes Sammelschreiben und unklare Updatevoraussetzungen sind ausdrücklich behandelt.
- Unbelegte LED- und Stromfreigaben verworfen. Statt pauschaler 25-V-/5-mA-Werte und einer Freigabe über 60 % DMM-Mittelwert stehen konkrete Datenanforderungen, geeignete Messung und deren Aussagegrenzen in der Anleitung.
- Mess- und Montagefolge geschlossen: alle realen Elkos, optionale B-Radmasse, Wiederanschluss nach Kontaktprüfung, tatsächliches Löten der Wagenlitzen, Bereichsprüfung vor Wagenserie und feste äußere Motor-Trennstelle für die Prüfung nach dem endgültigen Schließen.
- Bestehende Foto-/Herstellerdetails und die Prüfserie T1–T9 erhalten; zusätzliche Schemaeinsätze für Prüfabschnitt und frühe Kupplungsaufnahme. Das Schema für die Endmontage zeigt beide getrennten Hälften des Serviceanschlusses.

## Prüfung der Enddatei

| Merkmal | Ergebnis |
|---|---|
| Seiten / Lesezeichen | 46 / 46 |
| Verknüpfungen | 330 insgesamt: 294 intern, 36 extern |
| Ungültige interne Ziele | 0 |
| Ungültige Verknüpfungsrechtecke | 0 |
| Textzeichen außerhalb des Blatts | 0 |
| Unerledigte technische Platzhalter | 0 |
| Foto-/Herstellerabbildungen aus REV12 | vollständig erhalten |
| Visuelle Kontrolle | alle 46 Seiten; betroffene Seiten nach Schlusskorrekturen erneut |
| Dateigröße | 7.148.384 Byte |
| SHA-256 | `29e84c6ecfc1ef7841da704618e2d9d3cb96f516552318b9f2d3dec194f1b131` |

Die visuelle Kontrolle umfasste Lesbarkeit, Tabellen, Bild-/Text-Zuordnung, Schaltungsbeschriftungen, Seitenfuß und Platzierung der Hinweise. Zusätzlich wurden Bedienfolgen und Verweise quer über die Karten geprüft. Programmierung, Elektrik und Ablauf wurden unabhängig gegengeprüft; daraus entstandene Korrekturen wurden in Text und gerenderten Seiten erneut kontrolliert.

Die technische Dateiprüfung ist in `final_validation.json` dokumentiert. Sie überprüft interne Ziele, aber belegt nicht die dauerhafte Verfügbarkeit aller externen Webseiten. Ausfüllfelder für reale Mess- und Gerätedaten sind beabsichtigt und keine vergessenen Textplatzhalter.

## Stand und nächster praktischer Schritt

**Die beauftragte Dokumentprüfung und Dokumentkorrektur sind abgeschlossen.** Es wurde kein Decoder beschrieben, kein Bauteil vermessen und kein Fahrzeug physisch umgebaut. Die Anleitung ist deshalb keine Bestätigung einer bereits bestandenen elektrischen Abnahme.

Als Nächstes: getrennten Prüfabschnitt nach S. 3 aufbauen, reale Kupplungen nach S. 4 bestimmen und den Geräte-/Prüfaufnahmenweg nach S. 8–14 durchlaufen. Danach folgen die jeweiligen Anschluss- und Messkarten. Genaue Platinen-/LED-Daten, Lastverlauf, Servicezugang und die konkrete Anlage benötigen die in der Anleitung benannten realen Nachweise. Offene, davon abhängige Schritte sind ausdrücklich gekennzeichnet; es gibt keine Freigabe durch Annahme und keinen erforderlichen Händlerweg.
