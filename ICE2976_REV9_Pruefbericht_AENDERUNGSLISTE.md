# Änderungsliste - forensischer Abgleich ICE2976 REV9

**Datum:** 10.09.2026  
**Ausgangsbericht:** ICE2976_REV9_Pruefbericht.md  
**Korrigierte Fassung:** ICE2976_REV9_Pruefbericht_KORRIGIERT.md

## Umfang und Schutz der Originale

Der Originalbericht und die 69-seitige Umbauanleitung wurden nicht überschrieben. Die Korrektur betrifft den Bericht, nicht die Umsetzung am Zug. Alle 47 R-IDs und 18 W-IDs wurden in der neuen Fassung behandelt.

Originalbericht SHA-256: `efb6ba4a3f84b1519b11bf4e1e1a122f0ab910a1ff729f7b6dd09a1e1a3e0554`  
PDF SHA-256: `c1c1b1a2772f0e25385ffe911041b1cd2f7351277ada2ed5d8ecbe1be0070d29`

## Wesentliche inhaltliche Änderungen

1. Pauschale OL-Messkarte zurückgenommen; passive Leitungen und weiterhin bestückte Elektronik strikt getrennt. Vorhandene Schutzregeln korrekt mitbewertet.
2. Reale Bestandsangaben berichtigt: Gleisanschlussbox und Mobile Stations sind vorhanden; passende Artikel/Versorgung/SID-Nachweis bleiben offen. Kein automatischer Kauf einer weiteren Zentrale.
3. Signalbild/CS3-Fahrbefehl von gleisseitiger Strom- oder Bremsbeeinflussung unterschieden. Kein pauschaler ICE-M-S-Platinentausch als Lösung.
4. Hinterer Schleifer als unbestätigt, nicht als fehlend behandelt; Konsequenz für ungekuppelten Test ausdrücklich erklärt.
5. Einzel-AUX-Grenze, Licht-/AUX-Summe, Gesamtlast und Kupplungsgrenzen getrennt. „Unbekannte Last → ein Wagen erlaubt“ gestrichen.
6. Vermutete Steckerkappe nicht zur Demontage freigegeben. Bestehenden Index-Stopp der REV9 berücksichtigt.
7. Kapazitätsregel „keine nF-Anzeige“ zurückgenommen; kondensatorfreie Lieferung des 60941 nicht aus einer unvollständigen Liste abgeleitet.
8. mfx-Konfigurationsverhalten, Quittierlast, Aktivierungsregister und SID-Anzeige nicht mehr als bewiesene technische Mechanismen ausgegeben.
9. Konkreten JMRI-Firmware-Leseansatz ergänzt, ausdrücklich nur als K3-Prüfkandidat; keine freigegebene CV-Anweisung.
10. Quellenkritik aktualisiert: Märklin 10/2025 und CV-Fundstellen nun im Original bestätigt, 60941-Beilage vollständig gelesen, ESU-Mappingseite präzisiert.
11. Nachprogrammierung, Wiederherstellung nach Messung, Gate-Zirkel und Kurzfassung als zusammenhängende Ablaufkette behandelt.
12. Prüfmethodik berichtigt: 89 Links auf 67 Zielseiten; nicht 89 unterschiedliche Zielseiten. Keine Übernahme unbelegter Prozessbehauptungen oder absoluter Fehlerfreiheitszusagen.

## Vollständiger Änderungsindex

Die Ausgangspriorität ist ein historisches Zuordnungsmerkmal. Der Status beurteilt den Befund, nicht die Fertigstellung der erforderlichen Umbaukorrektur.

| ID | Ausgangspriorität | Korrigierter Status | Gegenstand |
|---|---|---|---|
| R-01 | P1 | Teilweise bestätigt | Anlagenbereich und gemeinsam verbundene Schleifer |
| R-02 | P1 | Teilweise bestätigt | Licht-/Hilfsleitungsprüfung fehlt als geschlossene Vor-Erststrom-Karte |
| R-03 | P1 | Teilweise bestätigt | Motorloser Kopf: konkrete Anschlussfolge und Versorgung nachweisen |
| R-04 | P1 | Teilweise bestätigt | Schnellanleitung: Isolation und Gleisanschlüsse lokal ergänzen |
| R-05 | P2 | Teilweise bestätigt | Vorab-Eigenanmeldung des ESU und Aussagekraft des Tests |
| R-06 | P2 | Offen | mfx-Konfiguration im synchronisierten Betrieb |
| R-07 | P2 | Teilweise bestätigt | Funktionstasten und endgültiger Soundprojektstand |
| R-08 | P2 | Teilweise bestätigt | Index-CVs: vorhandene Regeln zu einer ausführbaren Karte schließen |
| R-09 | P2 | Teilweise bestätigt | Prüfaufnahme und DCC-Quittierung |
| R-10 | P2 | Teilweise bestätigt | Firmware- und SID-Nachweis ohne Kaufzwang |
| R-11 | P2 | Teilweise bestätigt | C7: vorhandene Mobile Station/Gleisbox im Nachweisplan berücksichtigen |
| R-12 | P2 | Bestätigt | Prüftore und Fotoabhängigkeiten widerspruchsfrei ordnen |
| R-13 | P2 | Bestätigt | Anschlussstand E: Erststrom-Voraussetzungen und spätere Abnahme trennen |
| R-14 | P2 | Teilweise bestätigt | Erstes Einschalten: örtliche Trennregel und Dummy-Vorprüfung |
| R-15 | P2 | Teilweise bestätigt | Lastprüfung vor Freigabe von Wagenzahl und Fahrbetrieb |
| R-16 | P2 | Bestätigt | Physische Lichtausgänge in G0 protokollieren |
| R-17 | P2 | Teilweise bestätigt | Nachprogrammierung nur am getrennten Decoder |
| R-18 | P2 | Bestätigt | Dummy-Stützen: falschen Verweis auf LoDi-Ringprüfung ersetzen |
| R-19 | P2 | Teilweise bestätigt | Wiederanschluss und endgültiger Gehäuseschluss |
| R-20 | P2 | Teilweise bestätigt | Mehrdeutige Bezeichnungen vereinheitlichen |
| R-21 | P2 | Teilweise bestätigt | Wiederholungsprüfung nach Umreihen und Änderungen |
| R-22 | P2 | Offen | Norm-Pinrollen sind nicht automatisch gemessene LoDi-Leiterbahnen |
| R-23 | P2 | Offen | Schwarze Fläche im Steckbereich: keine ungeklärte Kappe entfernen |
| R-24 | P2 | Offen | ICE-M-Variante und gemeinsamer SW/RT-Pfad |
| R-25 | P2 | Teilweise bestätigt | Decoderadresse, Serviceeintrag und aktive Protokolle getrennt behandeln |
| R-26 | P2 | Teilweise bestätigt | Schnellanleitung: Wagen zuerst prüfen, dann anschließen |
| R-27 | P2 | Teilweise bestätigt | Schnellanleitung: Trennzustand unmittelbar vor 60977-Einsetzen |
| R-28 | P2 | Teilweise bestätigt | Schnellanleitung: Abschluss nach passiver Gehäuseprüfung |
| R-29 | P3 | Bestätigt | Seiten-, Kapitel- und Schrittnummern unterscheiden |
| R-30 | P3 | Bestätigt | Schwarze Messleitung: Widerspruch im Begleitsatz |
| R-31 | P3 | Teilweise bestätigt | Motorlitzen: kumulative Voraussetzungen einheitlich formulieren |
| R-32 | P3 | Teilweise bestätigt | Falsche Motorlaufrichtung: Korrektur mit erneuter Prüfung |
| R-33 | P3 | Bestätigt | Ungekuppelten Dummy nicht erneut ‚abkoppeln‘ |
| R-34 | P3 | Bestätigt | Widerstandstoleranz: zu schützende Stromgrenze nennen |
| R-35 | P3 | Nicht bestätigt | Kein allgemeiner Kapazitäts-Nulltest als neue Pflicht |
| R-36 | P3 | Teilweise bestätigt | Energiespeicher im Wagen-Messzustand ausdrücklich erfassen |
| R-37 | P3 | Offen | CS3: Verhalten beim Hinzufügen einer CV-Zeile |
| R-38 | P3 | Teilweise bestätigt | JMRI-Felder belegt; Aktivierungsabbildung weiterhin offen |
| R-39 | P3 | Teilweise bestätigt | 60941 und C90: Ableitung offenlegen, keinen falschen Wert behaupten |
| R-40 | P3 | Teilweise bestätigt | Programmer-Verbot artikelscharf wiederholen |
| R-41 | P3 | Teilweise bestätigt | Schnellanleitung: Reset, Einmessfahrt und Puffer getrennt warnen |
| R-42 | P3 | Teilweise bestätigt | Quellenmetadaten einzeln korrigieren |
| R-43 | P3 | Teilweise bestätigt | Bildbeschnitt und Dokumentnavigation |
| R-44 | P3 | Teilweise bestätigt | Prüfstatus aus Arbeitskarten in Änderungsvermerk verschieben |
| R-45 | P3 | Offen | 60941-Kondensator: Lieferumfang nicht aus unvollständiger Liste ableiten |
| R-46 | P3 | Teilweise bestätigt | Front-VCC und interne Vcc: vorhandene Erklärung lokal schärfen |
| R-47 | P3 | Teilweise bestätigt | Schnellanleitung: zusätzliche Direktverweise, keine vorgetäuschte G0-Freigabe |

## Ergebnis

8 bestätigt, 32 teilweise bestätigt, 6 offen, 1 nicht bestätigt als behauptete Pflichtlücke. Die historische Verteilung 4 P1 / 24 P2 / 19 P3 darf nicht als Zahl neu bestätigter Defekte gelesen werden.

Die Detailbegründungen, Gegenbelege und korrigierten Maßnahmen stehen je ID in der korrigierten Fassung. Ihre W-Tabelle behandelt sämtliche 18 Verdachtsbefunde separat.

**Nicht durchgeführt:** Änderung der Umbau-PDF, G0-Test, Decoderprogrammierung, reale Strom-/Isolationsmessung, Kauf, Herstelleranfrage oder Anlagenänderung.

**Nächste Umsetzungswelle:** Nachweise und Freigabekette konsistent in die Vollanleitung samt Schnellanleitung übertragen, anschließend alle betroffenen Übergänge und Verweise erneut prüfen. Keine isolierte Freigabe nur einzelner geänderter Seiten.

