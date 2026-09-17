> **Fortschreibung 12.09.2026:** Die später gezielt recherchierte Platine 62762 ist jetzt aus zwei unabhängigen Quellen beidseitig fotografisch belegt. Frühere Aussagen dieses Arbeitsentwurfs über fehlende Vergleichsseiten oder aktive Bestückung der langen Platine sind entsprechend überholt. Maßgeblich sind die Dateien `recherche_62762_*.md`, der neue Bildbefund und `eingangsstand.json`. Die tatsächliche Netzzuordnung des eigenen Exemplars bleibt offen; 60972/60982 sind inzwischen als vorhanden genannt.

# Abhängigkeiten: separate Anleitung mit ursprünglicher Märklin-Platine

Stand: 12.09.2026. Reiner Dokumentabgleich; keine Schaltung erfunden, keine Hardware verändert und keine PDF bearbeitet.

Ausgewertet: `Arbeitsstand_REV13/rev13_pages.json` (46 finale Seiten; SHA-256 `127afa35bcbb0234a5042c98ea14610ffe74d147e2d2191ac502d78e21ed9fab`), aktuelle REV13-PDF (SHA-256 `6a4afec36193952fa0a7040fc230c9c37356e71968e5b3dcd6244347d4308bce`), `Arbeitsstand_REV10/source_manifest.json`, `Arbeitsstand_REV11/bilder_quellen/manifest.json` sowie die Bildlegenden und Herkunftseinträge der vorhandenen Erzeugungsquellen. Alle Seitenangaben unten sind **finale REV13-Seiten**, keine alten Kartenschlüssel.

## Entscheidender Unterschied zur REV13

REV13 ersetzt die ursprüngliche lange Platine im Motortriebkopf durch LoDi 511. Die LoDi stellt dabei Anschlussstellen, 21MTC-Aufnahme, Frontbeschaltung, Montagebezüge und den zugeordneten Wagenlichtpfad bereit. Beim Erhalt der Märklin-Altplatine entfallen diese bereits beschriebenen Zuordnungen. Ein Austausch des Namens „LoDi“ gegen „Märklin“ reicht deshalb nicht.

Noch nicht entschieden ist, ob nur die **Motorplatine 511** entfällt oder auch die **LoDi-514-Fronten und weißen Wagenplatinen**. Die nachfolgenden Übernahmen setzen zunächst nur den Entfall der 511 voraus und nennen die zusätzlichen Abhängigkeiten ausdrücklich. Die Decoder 60977/59649, der Motorumbausatz60941 sowie das Zweiaderkonzept RT/GE werden hier nicht als neue Nutzerentscheidung ausgegeben; sie sind der bisherige REV13-Aufbau.

## 1. Seiten, die zwingend neue fahrzeugbezogene Inhalte brauchen

| REV13 | Bisheriger Inhalt | Konsequenz für die neue Anleitung |
|---|---|---|
| 1 | Systemübersicht: Motorseite60977 auf LoDi511 | Neues Gesamtschema mit tatsächlicher Decoderaufnahme, erhaltener Altplatine, Frontbeschaltung und Wagenlichtversorgung. Erst nach geklärter Architektur beschriften. |
| 2 | Teileverteilung: LoDi511 vorn, mit60977 gelieferter Märklin-Träger hinten | Stückliste und Verteilung der vorhandenen Träger neu auflösen. Der bisher hinten eingeplante einzelne Träger darf nicht gleichzeitig vorn verplant werden. |
| 7 | Kontakt-zu-Pad-Prüfung SW/RT/GE/MASSE; Ringmontage und bestätigte SW–RT-Durchleitung | Eine konkrete Kontaktkarte für die bearbeitete Originalplatine erstellen. Allgemeine Sichtprüfung und passive Leitungsprüfung bleiben verwendbar; die LoDi-Padnamen und Ringannahmen nicht. |
| 15 | Alte Platine/Umschalter abtrennen und ausbauen | Den pauschalen Entfernungsauftrag ersetzen. Motorumbau und Herstellerzeichnung können bleiben, wenn60941 weiter vorgesehen ist. Welche Teile der alten Elektrik erhalten, abgelötet oder getrennt werden, muss ein belegter Arbeitsplan am realen Platinenstand bestimmen. |
| 19 | Rote LoDi identifizieren; K1, R3–R6, SJ1/SJ2, SW/RT, GE-AUX | Vollständig ersetzen durch Identifikation der tatsächlichen Märklin-Altplatine: beide Seiten, Komponenten, Leitungspfade, Befestigungen und eindeutig identifizierte Anschlüsse. Keine LoDi-Nummer auf die alte Leiterplatte übertragen. |
| 20 | Vorn passende LoDi-Beschaltung und R4/R5 erhalten; hinten eigene Widerstände | Vordere Strombegrenzung neu auslegen oder eine passende komplette Beschaltung belegen. Allgemeine Rechnung und Polungsprüfung bleiben verwendbar. Falls514 bleibt, gilt diese Datenanforderung nun auch vorn; wenn514 entfällt, ändern sich beide Fronten. |
| 22 | LoDi-Ringe, Haltepunkte und Schraubverbindungen | Neue Montagekarte am Original: tatsächliche Halter, Schrauben, Kupferflächen und Abstände. Das allgemeine Bild zum unerwünschten Schraubkontakt ist nur als Prinzip übertragbar. |
| 23 | Verbindliche LoDi-Padkarte SW/MASSE/MOT_L/R/RT/GE/VCC/L_WS/L_RT/LS1/2 | Vollständig neue Anschlusskarte und Nahaufnahmen. Keines dieser LoDi-Pads darf als vorhandener Anschluss auf der alten Märklin-Platine vorausgesetzt werden. Servicezugang als Methode erhalten. |
| 24 | Lautsprecheradapter an LoDi-LS1/LS2; LoDi-Systemschema | Lautsprecheranschluss entsprechend der tatsächlich eingesetzten Decoderaufnahme neu zeigen. Satzlautsprecher-, Adapterprüfungs- und Einbauhinweise können bleiben; die LoDi-Anschlussziele nicht. |
| 31 | Innenlichtausgang folgt LoDi GE-/SJ1-/SJ2-Zuordnung | Motorart60941/60977 grundsätzlich übertragbar; Innenlicht-Ausgang, Ausgangsart und Mapping erst nach realem neuen Versorgungsweg festlegen. AUX4 nicht allein aus REV13 übernehmen. |
| 33 | Checkliste mit LoDi-Revisions-/Pad-/Ring-/Frontbedingungen | Alle abhängigen Zeilen auf die Originalplatinenbearbeitung umstellen. Geforderte Trennungen, eigene Leiterbahnen und Wiederholungsprüfungen konkret aufnehmen. |
| 34 | 60977 auf rote LoDi511 stecken; Freifläche RichtungK1 | Vollständig ersetzen. Benötigt die tatsächlich verwendete21MTC-Aufnahme mit Index, Einbaulage, mechanischer Befestigung und geprüftem Dachraum. |
| 45 | 60974-Anbindung des auf LoDi gesteckten60977; K1/S2/VCC-Abgrenzung | Pufferkarte auf tatsächliche Decoderaufnahme umstellen. Märklin-SUSI-/Firmwarebedingungen bleiben grundsätzlich relevant, beweisen aber keinen Anschluss auf der alten Platine. Signalhalt-Teil bleibt nur unter derselben RT-Architektur übertragbar. |
| 46 | Quellen- und Bildgültigkeit für LoDi-Umbau | Quellen neu zuordnen, alte Vergleichsbilder klar begrenzen und tatsächliche neue Anschluss-/Bearbeitungsbilder aufnehmen. Keine bestehende LoDi-Quelle als Freigabe eines Märklin-Leiterbahnschnitts angeben. |

## 2. Inhaltlich nutzbare Karten mit gezielten Anpassungen

| REV13 | Übernehmbarer Kern | Zu ändern oder vorher zu entscheiden |
|---|---|---|
| 4 | Frühe Prüfung aller Kupplungsübergänge | Zwei getrennte Kontakte sind nur dann unverändert nötig, wenn RT/GE weiter das gewählte Zugkonzept bleibt. |
| 5–6 | Netze auseinanderhalten, Multimeter vorbereiten, freie Leitungen prüfen | Bezeichnungen an neue Kontaktkarte anbinden. Die Entladevorschrift für identifizierte Wagenelkos gilt nicht pauschal für unbekannte alte Platinenspeicher; tatsächliche Bestückung entscheidet. |
| 16–18 | Entstörung und Motorisolation für60941 | LoDi-Abtrenntexte durch Trennung von der neuen Originalplatinenbeschaltung ersetzen. Anschlussrückverweis auf neue Motorzielpunkte; Vergleichsfotos nicht zu2976-Schaltbildern erklären. |
| 21 | LED-Zweigstrom per Widerstandsspannung beziehungsweise geeigneter Reihenmessung | Messpunkte und Eingangsgrößen auf die neue Beschaltung beider Fronten abgleichen. Keine bisherige vordere LoDi-Strombegrenzung weiter voraussetzen. |
| 25–26 | Gegenkopf auf Märklin-Träger; eigener Schleifer/Radkontakt und getrennte Lichtadern | Nur übertragbar, wenn der bisher dafür vorgesehene Träger hinten verfügbar bleibt und die LED-/RT-Architektur bleibt. Die Anweisung, hinten die alte lange Platine auszubauen, widerspricht einer möglichen Vorgabe „beide Originalplatinen erhalten“ und wäre dann neu zu schreiben. |
| 27,29–30 | Wagenmontage, Kontakte bis Pad prüfen, optionale Radmasse | Bei weiterverwendeter weißer LoDi-Wagenplatine: O/L/B-Rollen müssen zum neuen vorderen Versorgungsweg passen. Die bisherige zweite Herstellerlegende „bei Verwendung der LoDi-Motorplatine“ darf ohne511 nicht automatisch als Freigabe angeführt werden. Entfallen alle LoDi-Teile, sind diese Karten komplett neu. |
| 28 | Passive Einzel-/Kreuzpfadprüfung der Kupplungen | Endbenennung und RT/GE-Herkunft an neue Motorseite anbinden. Mechanikmethode kann bleiben. |
| 32 | Quellenfolge, Einzelkontrolle, Lastkategorien und Abbruchregeln | Zahlen des60977 gelten weiterhin für diesen Decoder, nicht automatisch für neue Bauteile/Altleiterbahnen. Tatsächliche LED-/Wagenpfade und Montagevoraussetzungen aktualisieren. |
| 35 | Steckmechanik59649 auf Märklin-Träger | Nur wenn dieser Träger hinten bleibt. Nicht als zweite vorhandene Trägerplatine mitzählen. |
| 36–37 | Getrennte Erstkontrollen, spannungsfreier Quellenwechsel, Fronttest | Anschlusssichtprüfung, Motorzielpunkte, LED-Messpunkte und Steckkarten auf neue Hardware umstellen. Bestehende F0-Farbfolge nur bei beibehaltenem Gesamtziel verwenden. |
| 38 | Prüfung von Versorgungs-/Signal-/Boostergrenzen | Der lange RT-Bus überbrückt Grenzen nur, wenn er im neuen Konzept beide Schleifer weiterhin verbindet. LoDi-ICE-M-S als mögliche Fertiglösung nicht zum Bestandteil des neuen Originalplatinenwegs machen. |
| 39 | Ausgangslast, Stromverlauf und alleinige hintere Einspeisung | Neue GE-Erzeugung und tatsächliche Stromtragfähigkeit aller verbleibenden Leiterbahnen/Anschlüsse einbeziehen. AUX-/Lichtsumme des60977 allein gibt weder Altplatine noch Kupplungen frei. Bei anderer Schleiferarchitektur fällt der hintere Speisetest anders aus. |
| 40–41 | Gestufte Wagenprüfung T1–T9 und endgültige Funktionstasten | Konkrete Innenlichtansteuerung, Wagenplatinen, Lastbelege und Quellenverweise austauschen. Die Prüfziele sind übertragbar, ihre bisherige LoDi-Zuordnung nicht. |
| 42–43 | Geschlossene Montage, außen zugängliche Motor-Trennung und Endprüfung | Neue Halter-/Decoder-/Leitungsräume; neue Steckkarten. Wagen-TRIMM nur bei tatsächlich weiterverwendeten LoDi-Wagenleisten. |
| 44 | Fehler systematisch eingrenzen; Decoder außerhalb des Zuges warten | LoDi-GE-AUX-, O/L- und Stecklagenverweise auf reale Anschlüsse ersetzen. |

## 3. Inhaltlich weitgehend unabhängig vom Erhalt der Altplatine

**S.3 und8–14** können als methodische Grundlage übernommen werden, sofern die bisherigen Decoder60977/59649 und die gemeinsame mfx-Paarfunktion weiter gewollt sind. Diese Arbeiten erfolgen am freien Prüfgleis oder außerhalb der Fahrzeuge. Es bleiben redaktionelle Verweise auf neue Montage-/Soundseiten und der Abgleich des tatsächlichen Gerätewegs. Die externe Paarprüfung ist kein Nachweis einer sicheren bearbeiteten Fahrzeugplatine.

Damit sind alle46 bestehenden Seiten erfasst:14 mit zwingend neuen fahrzeugbezogenen Inhalten,24 mit angepasstem Inhalt und8 weitgehend übernehmbare Grundlagen. Diese Einstufung ist eine Redaktionsplanung, keine Aussage über eine sinnvolle Endseitenzahl der neuen Anleitung.

## 4. Vorhandene Bilder der ursprünglichen Elektrik

### Persönliche Bilder des2976 – vorrangige Ausgangsreferenzen

1. `Arbeitsstand_REV10/bilder/0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg` –842×204Pixel; aktuell REV13 S.15. Übersicht der eingebauten langen grünlichen Originalplatine mit Leiterbahnseite, Feldspule und Motorbereich. Herkunft laut Quellmanifest aus der persönlichen Fotobibliothek. **Zeigt nicht beide Platinenseiten und keine vollständig sichtbare Anschluss-/Bauteilbelegung.** Nicht ausreichend für beschriftete Schnittstellen oder präzise Leiterbahntrennungen.
2. `Arbeitsstand_REV10/bilder/BAD231CB-B878-4D94-B5EE-CDAB1D69D455_4_5005_c.jpeg` –662×260Pixel; im REV10-Quellmanifest enthalten, derzeit nicht in REV13 eingebaut. Seitlicher Blick auf Originalmotor mit Feldspule, Leitungen und Bereich unter der langen Platine. Hilfreich für Lageverständnis und Vorher-Dokumentation. **Kein Leiterbahnschaltplan; verdeckte Ziele nicht ablesbar.**

Die Dateinamen `image.jpg` und `image-2.jpg` sind dagegen Fotos der **roten LoDi-Platine**, nicht der ursprünglichen Märklin-Platine. `image-3.jpg`/`image-4.jpg` zeigen die weiße LoDi-Wagenleiste; `image-5.jpg` deren Einbau. Diese dürfen trotz Herkunft aus den Benutzerdateien nicht als Märklin-Originalelektrik etikettiert werden.

### Hersteller-/Vergleichsbilder – nutzbar mit Modellgrenze

- `Arbeitsstand_REV10/quellen_alt/tmp/pdfs/rev5/research/dummy_full.jpg` –4032×2614Pixel; aktuell REV13 S.25. Motorloser Kopf und ausgebaute lange Altplatine aus dem **LoDi-Vergleichsumbau33701**. Herstellerherkunft ist in `build_ice2976_rev5.py` S.23 mit Original-URL dokumentiert. Nicht der persönliche2976 und kein freigegebener Trennplan dafür.
- `Arbeitsstand_REV11/bilder_quellen/motor_a_2048.jpg` – REV13 S.16; LoDi-Vergleich33701 vor Entstörungsanpassung. Zeigt Motor/Altentstörung, nicht die vollständige persönliche2976-Platine.
- `Arbeitsstand_REV11/bilder_quellen/motor_c_2048.jpg` – REV13 S.17; Vergleich33701 nach Anpassung. Für Messclip-Prinzip geeignet, aber kein unbehandelter2976-Ausgangszustand.
- `Arbeitsstand_REV11/bilder_quellen/lampe_alt_original.jpg` –914×868Pixel, derzeit nicht in REV13; Herstellerfoto der alten Lampenfassung im Vergleich33701. Für Bauformvergleich, nicht als Nachweis der eigenen Verdrahtung.
- `Arbeitsstand_REV11/zeichnungsquellen/maerklin_60977_600dpi-005.png` und `...-006.png` – Originalzeichnungen des **mit60977 gelieferten modernen Trägers**, keine Zeichnungen der alten2976-Längsplatine. Diese Unterscheidung ist für die neue Teileverteilung besonders wichtig.

## 5. Fünf Punkte, die vor konkreten Bearbeitungsbildern aufgelöst werden müssen

1. **Wagenlicht GE:** Die aktuelle Anleitung leitet GE aus der LoDi-GE-/Jumperfunktion ab. Bei erhaltener Originalplatine sind Ursprung, Rückweg, Schaltart und Verhältnis zu RT/Radmasse neu zu bestimmen. Weder eine Leiterbahnfarbe noch ein ähnliches Bauteil beweist diese Funktion. Bei weiterverwendeten LoDi-Wagenleisten muss deren Anschlussmodus zum neuen tatsächlichen Signal passen.
2. **Frontwiderstände:** REV13s vordere Freigabe lautet „passende LoDi-Frontkombination, R4/R5 erhalten“. Diese Begründung entfällt mit511. Die alten Lampen-/Umschaltbauteile sind kein belegter Ersatz. Ohne neue Zuordnung dürfen R4/R5-Werte oder Anschlussnamen nicht in die alte Platine eingezeichnet werden.
3. **Befestigungen:** LoDi-RingA/RingB sind Bezeichner der ausgetauschten Platine. Der alte Märklin-Halter samt Schraubkontakten muss unabhängig betrachtet werden; ein sichtbarer Schraubring beweist auch hier keine erlaubte Masse- oder Decoderverbindung.
4. **Decoderträger vorn/hinten:** REV13 verwendet vorn die LoDi-Aufnahme und hinten die einzige im60977-Satz enthaltene Märklin-Trägerplatine. Wird dieser Träger nun vorn gebraucht, ist der bisherige hintere Aufbau damit nicht mehr gedeckt. Die erhaltene lange Platine ist anhand der vorhandenen Originalbilder keine nachgewiesene21MTC-Aufnahme. Anzahl, Einbauort und kompatible Stecklage müssen im neuen Gesamtkonzept eindeutig sein.
5. **Puffer:** Ein erhaltener Original-Leiterbahnzug schafft keinen SUSI-Anschluss. Der60974 bleibt nach Decoder-/Schnittstellenbeleg anzubinden; der genaue Anschluss hängt von der tatsächlich gewählten60977-Aufnahme ab. Ein nutzbarer moderner Träger kann diesen Punkt verändern, darf aber nicht gleichzeitig hinten als weiterhin frei vorausgesetzt werden.

Die vorhandenen Bilder tragen eine ehrliche Vorher-Übersicht und viele übernehmbare Motor-/Messprinzipien. Sie tragen derzeit **keine vollständig zuordnungsfähige Schritt-für-Schritt-Bearbeitung der persönlichen alten Märklin-Platine**. Eine neue Anleitung muss deshalb belegte Leiterbahn-/Bauteilzuordnungen ergänzen; sie darf keine LoDi-Ansicht als vermeintliche Originalplatine weiterverwenden.

## 6. Sinnvolle Folge der separaten bebilderten Anleitung

Noch keine endgültige Seitenzählung, sondern eine Reihenfolge der Arbeitsabschnitte:

1. **Geltungsbereich und tatsächliche Teileverteilung:** Welche ursprüngliche Platine bleibt; welche LoDi-Front-/Wagenbauteile bleiben; wo sitzen60977,59649 und die verfügbaren21MTC-Träger? Daraus neue Übersicht und Teilekarte.
2. **Originalplatine erkennen und ursprüngliche Anschlüsse aufnehmen:** Persönliches Übersichtsbild plus scharfe beidseitige Detailbilder; unverwechselbare Platinenorientierung, Bauteile, Lötstellen, vorhandene Halter und freie Einbauräume. Hier nur tatsächlich belegte Zuordnungen eintragen.
3. **Prüfumgebung, Kupplungen und Messgrundlagen:** Aus REV13 S.3–7 übernehmen; nur die neue Kontakt-/Platinentabelle austauschen.
4. **Decoder außerhalb der Fahrzeuge vorbereiten und Paarfunktion prüfen:** REV13 S.8–14 als weitgehend unabhängigen Abschnitt verwenden, falls dieselben Decoder weiter gelten.
5. **60941 und Motorprüfung:** Herstellerzeichnung und Messclipbilder aus REV13 S.15–18; Ausbauanweisungen auf die zu erhaltende Originalplatine anpassen.
6. **Originalplatine konkret bearbeiten, prüfen und befestigen:** Neuer bebilderter Arbeitskern. Erhaltene und abzutrennende Funktionen müssen nach gesicherter Originalbelegung einzeln zugeordnet sein. Ein Schnitt-/Lötschema ist mit dem jetzigen Bildstand noch nicht belegbar.
7. **Decoderaufnahme, Fronten, Lautsprecher und Wagenlicht anschließen:** Neue Zielpunkte auf die persönliche Ansicht beziehen; GE-Erzeugung, Frontbegrenzung und getrennte Decoderanschlüsse erklären. Hier die Service-Trennstelle einplanen.
8. **Gegenkopf und Wagen:** Aus REV13 S.25–30 übernehmen oder neu schreiben, abhängig von Trägerverteilung und LoDi-Umfang. Kupplungsprüfung bleibt vor dem Anschluss.
9. **Mapping, Checkliste, Stecken, Einzel- und Paarprüfung:** Grundfolge REV13 S.31–37; Anschlüsse und Grenzwerte am neuen realen Aufbau verankern.
10. **Anlagenbereich, Wagenlast, T1–T9, Gehäuse und Wartung:** Methoden REV13 S.38–44 übernehmen; neue Stromwege und Bauteile berücksichtigen. Puffer erst anschließend als passende Ergänzung.

**Offener Bildbedarf des Arbeitskerns:** Die zwei persönlichen vorhandenen Bilder sind klein und zeigen keine vollständige beidseitige Bauteil-/Leiterbahnzuordnung. Dafür benötigt die exakte bebilderte Variante scharfe beidseitige Originalplatinenansichten und eindeutig erkennbare Anschluss-/Befestigungsdetails. Bis dahin können Struktur, unveränderte Motor-/Prüfkapitel und Bildherkunft vorbereitet werden; ein vermeintlich fertiger Schnitt-/Lötplan wäre unbelegt.
