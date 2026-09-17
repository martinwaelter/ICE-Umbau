# ICE 2976 - Änderungen und verbleibende Nachweise in REV10

Stand: 10.09.2026. Bezug: vollständige Umbauanleitung REV10, 92 Seiten.

**Ergebnis:** Die dokumentarischen Korrekturaufträge des berichtigten REV9-Prüfberichts sind in die vollständige Anleitung eingearbeitet. Das ist keine Bestätigung eines bereits umgebauten oder geprüften Zuges. Insbesondere die gemeinsame mfx-Funktion von 60977 und 59649 ist am vorhandenen Decoderpaar weiterhin nicht nachgewiesen.

PDF-SHA-256: `2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0`.

## 1. Die wichtigsten Änderungen

- Vollfassung erhalten und erweitert: 92 statt 69 Seiten, 78 Kapitel-/Abschnittsziele, alle bisherigen Kapitelbereiche und alle elf Bildvorkommen übernommen. Die Anzahl allein beweist keine unveränderte Formulierung; die betroffenen Texte wurden bewusst korrigiert.
- Motorprüfung konkretisiert: vollständige Motorlitzen und Drosseln, richtige schwarze Messleitung je Tabellenzeile, positive Kontaktkontrollen vor und nach der Messreihe, Wiederholungsprüfung nach Korrekturen.
- Neue getrennte Prüfkarten: 16c für tatsächlich abgetrennte passive Leitungen; 16d für bestückte Netze mit noch festzulegenden realen Messpunkten, Prüfgerät und zulässiger Auswertung. Kein pauschales „OL = sicher“ auf bestückten Platinen.
- Hinterer Kopf ausführlicher: tatsächlichen Schleifer und Radkontakt nachweisen; gemeinsamer Schleifer-/RT-/B/GR-Punkt, getrenntes 0/GL, isoliertes GE und einzeln isolierte unbenutzte Trägerlitzen.
- Konkrete Bauteilzuordnung: 60977 vorn auf LoDi 511, 59649 hinten auf Märklin-Träger. Warnungen stehen vor den Einsetzhandlungen; unbekannte schwarze Steckstruktur nicht auf Verdacht entfernen.
- Erststrom und Endabnahme zeitlich getrennt: E1 enthält nur vorher erfüllbare Voraussetzungen; E2 die offenen Funktionstests; E3 Last-, Gehäuse- und Bereichsabnahme. Keine gegenseitig unmöglich erfüllbaren Voraussetzungen.
- Innenbeleuchtung und optionale Achskontakte erhalten: richtungsunabhängiger Ausgang, korrekte LoDi-Betriebsart, Kontakt-/Padprüfung, Rückmeldetest, Laststufen und F0-/Richtungswechseltests. Kein pauschales Flackerfrei-Versprechen.
- CS3-Kapitel korrigiert: Leseweg, Einzeldecoder-Trennung, Master-UID/SID/Firmware, Indexgruppen, CV-Export und Rücklesung auseinandergehalten. Nach Vorbereitung einer fehlenden CV-Zeile steht nun ausdrücklich die Rückkehr zur Aufbauprüfung und der stromlose Wiederanschluss.
- Bestehende Geräte berücksichtigt: Gleisbox und Mobile Stations sind mögliche Prüfmittel nach Eignungsnachweis. Kein automatischer Kaufzwang für zweite Zentrale oder ESU LokProgrammer.
- Schnellanleitung am Ende neu mit den vollständigen örtlichen Trenn-, Isolierungs- und Prüfregeln sowie direkten Verweisen auf die Detailkarten.

## 2. Rückverfolgung aller 47 R-Befunde

„Eingearbeitet“ bedeutet hier: Der Korrekturauftrag ist im Dokument behandelt, soweit er ohne neue reale Daten bearbeitbar ist. Eine dokumentierte Voraussetzung oder Sperre ist **kein bestandener Hardware-Nachweis**. Die ursprüngliche Bewertung jedes Befunds bleibt im [korrigierten Prüfbericht](</Users/martinwaelter/ICE Umbau/ICE2976_REV9_Pruefbericht_KORRIGIERT.md>) nachvollziehbar: 8 bestätigt, 32 teilweise bestätigt, 6 offen, 1 nicht bestätigt als behauptete Pflichtlücke.

Alle Seitenangaben beziehen sich auf die PDF-Seitenzählung der oben bezeichneten REV10, nicht auf frühere Fassungen oder gedruckte Herstellerseiten.

| ID | Konkrete Behandlung in REV10 | Fundstelle | Grenze / noch real nachzuweisen |
|---|---|---|---|
| R-01 | Prüfbereich mit genau einer Quelle; CS3-Fahrbefehl von elektrischer Gleisbeeinflussung unterschieden. | 0a, S. 6; 19, S. 62 | Tatsächlicher Anlagenplan und Bereichsabnahme. |
| R-02 | Vollständige passive Vor-/Nachkontrollen; bestückte Netze erhalten eigene Nachweiskarte statt pauschalem OL. | 16c/16d, S. 52–55; E1, S. 69 | Reale Platinenrevision, sichere Messpunkte, Geräteparameter und zulässige Anzeigen fehlen noch. |
| R-03 | Hinteren Schleifer/Radkontakt zuerst feststellen; B/GR, 0/GL und GE in eigener Handgriffreihe. | 12d, S. 39–40 | Hintere Stromaufnahme, Verbindungspunkt und Montage am eigenen 2976. |
| R-04 | GE und jede unbenutzte Trägerlitze ausdrücklich einzeln isolieren; auch in Kurzschritt 5. | 12d, S. 39–40; G.2, S. 91 | Tatsächliche Einzelisolation und Prüfung. |
| R-05 | Vorab-Eigenanmeldung, alter Listeneintrag und aktive Zweitanmeldung unterschieden. | B6, S. 9; C, S. 10–11 | Reales Verhalten nach Einrichtung und Neustart. |
| R-06 | Keine gemeinsame Konfiguration beider Decoder; physische Trennung vorgeschrieben. | C, S. 10–11; 16, S. 49; F.7, S. 82 | Internes Verhalten gemeinsamer mfx-Konfiguration weiterhin nicht belegt. |
| R-07 | Soll-/Ist-Prüfung sämtlicher belegter Funktionstasten nach letztem Sound-/Mappingtransfer. | C.a, S. 12–13; 17b, S. 59 | Endgültiges Projekt und ausgefüllte Funktionsmatrix. |
| R-08 | Karte mit Decoder, Indexgruppe, Ziel-CV, Alt-/Ziel-/Rücklesewert; Abschlusslesen gruppenweise. | F.6, S. 81; F.11, S. 86 | Keine geratenen Index-/Aktivierungswerte freigegeben. |
| R-09 | Vorab-Prüfaufnahme von späterem motorlosem Aufbau unterschieden; fehlende Quittierung nicht als Defekt ausgegeben. | A, S. 7–8; F.4, S. 78–79; F.10, S. 85 | Geeignete Aufnahme und zuverlässiger Leseweg am wirklichen Aufbau. |
| R-10 | Firmware, dauerhafte UID und zugewiesene SID getrennt dokumentiert. | F.3, S. 77; F.10/F.11, S. 85–86 | Exakte Gerätewerte; neue Implementierungsregister nur Recherchehinweis. |
| R-11 | Vorhandene Gleisbox und Mobile Stations vor zusätzlichem Kauf berücksichtigen; tatsächlich neue SID nachweisen. | A, S. 7–8; C/C.a, S. 10–13 | Artikel-/Softwarestand und verwertbarer SID-Nachweis. |
| R-12 | Zeitliche Abfolge von G0, Motorarbeit, Montage, Verdrahtung und Erststrom entwirrt. | Titelseite; D, S. 68 | G0 ist weiterhin offen; lose Fotos sind keine Montagefreigabe. |
| R-13 | Frühere Sammelabnahme in E1/E2/E3 aufgeteilt. | S. 69–71 | Karten erst bei wirklich erfüllten Voraussetzungen bzw. Ergebnissen ausfüllen. |
| R-14 | Vor jedem Einsetzen örtliche physische Trennung; hinterer Kopf zuerst passender Einzeltest. | 17, S. 56–57 | Eigene hintere Stromaufnahme und bestätigter Kommunikationsweg. |
| R-15 | Lastplan vor Erststrom und jeder höheren Laststufe; Einzel-, Summen- und Kontaktgrenzen getrennt. | 18, S. 60–61; E1, S. 69 | Ströme, Einschaltspitzen, Spannungsabfall und zulässige Wagenzahl. |
| R-16 | Physische LV/LR-Zustände in beiden Richtungen und bei F0 aus protokollieren. | C.a, S. 12–13 | Anzeige in der CS3 allein ist kein Ausgangsnachweis. |
| R-17 | Nachprogrammierung ausschließlich am physisch getrennten Einzeldecoder; Wiederholung betroffener Tests. | 11a, S. 33; 16, S. 49; F.7, S. 82 | Bestätigter Einzelprogrammieraufbau. |
| R-18 | Hintere Stützen nicht mit LoDi-Ringprüfung gleichgesetzt; eigener Halter-/Freiraumnachweis. | 12c, S. 38; 23, S. 66 | Tatsächliche Halterung und geschlossenes Gehäuse. |
| R-19 | Nach Wiederanschluss vollständige betroffene Prüfungen; bei Lageänderung erneut geschlossene Prüfung. | 16c/16d, S. 52–55; 24, S. 67; E3, S. 71 | Mess- und Gehäuseergebnisse am Endzustand. |
| R-20 | Kupplungsenden heißen Ende 1/2; Einsetzschritte 9c-1 bzw. 12b-1; Prüfleitungsenden klar von Prüfpersonen getrennt. | 9c/12b/14a/24 | Redaktionelle Korrektur; keine elektrische Wirkung behauptet. |
| R-21 | Nach Umreihen, Drehen, Teile- oder Konfigurationsänderung betroffene Zuordnungen und Prüfungen wiederholen. | 14b, S. 44; E3, S. 71; G.3, S. 92 | Tatsächliche neue Reihung/Endorientierung dokumentieren. |
| R-22 | Normative Pinrolle ausdrücklich von realer LoDi-Leiterbahn getrennt. | 9a, S. 27; 16d, S. 54–55 | Revisionsbezogener Netz-/Messnachweis. |
| R-23 | Keine vermutete Schutzkappe abnehmen; Index am tatsächlichen Träger und Decoder identifizieren. | 8, S. 24; 9c, S. 29–30; 12b, S. 36–37 | Schwarze Steckstruktur und reale Indexlage unbestätigt. |
| R-24 | Fehlendes Relais nicht als ausreichender ICE-M-/SW–RT-Nachweis behandelt. | 8/8a, S. 24–25; 9a, S. 27; 16d, S. 54–55 | Reale Variante, Revision, SW/RT-Pfad und GE-Auswahl. |
| R-25 | CS3-Serviceeintrag, gespeicherte Decoderadresse und aktivierte Protokolle getrennt erfasst. | F.7, S. 82; F.11, S. 86 | Tatsächliche Werte; keine pauschalen Abschalt-CVs. |
| R-26 | Kurzschritt 6 prüft Kupplungen und Wagenplatine vor dem Löten. | G.2, S. 91; 14a/14b, S. 43–44 | Reale Vorprüfung bleibt erforderlich. |
| R-27 | Kurzschritt 8 verlangt physische Trennung und Einzelisolation unmittelbar vor 60977-Einsetzen. | G.3, S. 92 | E1 und tatsächlicher Sitz vor Bestromung. |
| R-28 | Kurzschritt 11 ergänzt Entfernen der Hilfsleitungen, Wiederanschluss, Nachprüfung und Endabnahme. | G.3, S. 92 | Geschlossener Endzustand real zu prüfen. |
| R-29 | Kapitel, Schritte und PDF-Seiten eindeutiger bezeichnet; Navigation neu aufgebaut. | Dokumentweit; G.1–G.3 | Alle 230 internen Linkannotation-Ziele zusätzlich maschinell geprüft. |
| R-30 | Schwarze Messleitung passend zu jeder Tabellenzeile an PX bzw. PM2 zugeordnet. | 6/6a, S. 20–21 | Positive Kontaktkontrollen bleiben zwingend. |
| R-31 | Motoranschluss setzt vollständige Motor-/Litzenprüfung und Padzuordnung voraus, nicht einen sich selbst voraussetzenden Anschluss. | 5/6b/9a, S. 18/22/27 | Tatsächliche Prüfung einschließlich Drosseln/Litzen. |
| R-32 | Falsche Motorlaufrichtung nur stromlos korrigieren, danach vollständige betroffene Prüfung erneut. | Schritt 53, S. 56–57 | Keine spontane CV-/Lichtinvertierung als Ersatz. |
| R-33 | Ungekuppelten Dummy zur Versorgungsunterbrechung vom stromlosen Gleis nehmen, nicht erneut „abkoppeln“. | Schritt 55, S. 57 | Neustartergebnis real protokollieren. |
| R-34 | Toleranzregel schützt den maximal zulässigen LED-Strom beim kleinsten Widerstandswert. | 11, S. 32 | Reale LED-Daten und maximale Versorgung bleiben offen. |
| R-35 | Kein allgemeiner Kapazitäts-Nulltest eingeführt; Sicht-/Leitungsverfolgung und Isolation getrennt. | 21, S. 64 | Kondensatoranschlüsse tatsächlich identifizieren. |
| R-36 | Vor Wagenmessung reale Speicher und Spannungszustand erfassen; keine Kurzschlussentladung. | 14b, S. 44 | Tatsächliche Speicherbestückung und zulässiges Prüfverfahren. |
| R-37 | Unbestätigte CV-Zeilenanlage nicht live ausprobieren; bestätigten Bedienweg und Rückkehr zum Aufbau verlangen. | F.4/F.6, S. 78–79/81 | CS3-Version und Verhalten der Zeilenanlage weiterhin nachzuweisen. |
| R-38 | JMRI-Implementierung nicht mit vollständiger Aktivierungsfolge gleichgesetzt; Offline-Differenzexport erforderlich. | F.1/F.5/F.9, S. 75/80/84 | Aktivierungsabbildung für das tatsächliche Projekt fehlt noch. |
| R-39 | C90/CV52=3 als technische Zuordnung zum vollständig geprüften 60941 erläutert. | 16, S. 49 | Kein Freibrief für einen unbekannten oder anders aufgebauten Motor. |
| R-40 | Programmer-Zuordnung lokal wiederholt: 60971 nur für 60977, niemals für 59649. | 16/F.7, S. 49/82; G.2, S. 91 | Optionaler ESU-Weg benötigt ebenfalls geeigneten Aufbau. |
| R-41 | Reset, Einmessfahrt und Puffer als drei getrennte Sperren. | F.7, S. 82; G.2, S. 91 | Beide 60974 bleiben bei den Erstprüfungen abgetrennt. |
| R-42 | Herstellerbelege und Metadaten präzisiert; offene Fundstellen nicht als bestätigte Eingabewerte verwendet. | Quellen, S. 72–73/87–88; 16, S. 49 | Kein vollständiger neuer Erreichbarkeitstest jedes externen Links behauptet. |
| R-43 | Vollständiger Warnrahmen im Hersteller-Steckbild; Inhaltsverzeichnis und Kurzverweise neu erzeugt. | 12b, S. 36; Inhaltsverzeichnis; G.1–G.3 | Bildbeschnitt ist Darstellung, kein veränderter Originalbildinhalt. |
| R-44 | Historischer Prüfstatus aus Arbeitskarte in Versionskapitel ausgelagert. | D, S. 68; H, S. 89 | Keine nicht vorliegende 86-Finding-Rohliste als geprüft ausgegeben. |
| R-45 | Kondensator-Lieferzustand dokumentieren; keinen Wert aus einer unvollständigen Teileliste ableiten. | 5, S. 18; 21, S. 64 | Tatsächliches Motorschild und beide Kondensatoranschlüsse. |
| R-46 | LoDi-Front-VCC konkret als LED-Plus benannt, von interner 21MTC-Vcc an Pin 12 abgegrenzt. | 9a, S. 27; 16d, S. 54–55 | Normrolle ersetzt keine reale Netzzuteilung. |
| R-47 | Schnellanleitung um örtliche Voraussetzungen und zusätzliche echte Detailverweise erweitert. | G.1–G.3, S. 90–92 | G0 ausdrücklich weiterhin offen; Kurzfassung keine unabhängige Bauanweisung. |

## 3. Die 18 W-Verdachtsbefunde: keine falschen „Reparaturen“

Die Ergebnisse der vorherigen forensischen Gegenprüfung bleiben in [Abschnitt 5 des korrigierten Prüfberichts](</Users/martinwaelter/ICE Umbau/ICE2976_REV9_Pruefbericht_KORRIGIERT.md:587>) erhalten. Insbesondere werden nicht vorsorglich richtige Anschlüsse, Bits oder Berechnungen umgedreht.

| ID | Behandlung in REV10 |
|---|---|
| W-01 | Motorplatinen-Betriebsart der weißen Leiste beibehalten: RT an O, GE an L, optional örtlicher Radkontakt an B. |
| W-02 | AUX4-Ausgangsart gemäß Märklin; übrige CV51-Bits nicht pauschal überschreiben. |
| W-03 | Einmessfahrt-Warnung präzise erhalten, nun vor den Erststrom-Handgriffen. |
| W-04 | CV52=3/C90 erhalten, reale Motorzuordnung ausdrücklich Voraussetzung. |
| W-05 | Decodergrenzen erhalten; keine Kupplungs-/Wagenfreigabe daraus abgeleitet. |
| W-06 | Werksfunktionen nicht als tatsächliches unverändertes Soundprojekt ausgegeben; vollständige Tastenmatrix hinzugefügt. |
| W-07 | 60974-Firmware-/Anschlussgrenzen erhalten; beide Speicher zunächst abgetrennt. |
| W-08 | Normative SUSI-Zuordnung erhalten; reale Stecker-/LoDi-Zuordnung weiterhin gesondert. |
| W-09 | JMRI-Registerbeleg erhalten, nicht zur freigegebenen Mischdecoder-Schreibfolge hochgestuft. |
| W-10 | Korrekte Rechenbeispiele erhalten; reale Bauteil-/Stromfreigabe nicht daraus abgeleitet. |
| W-11 | Hintere Farbverdrahtung Rot an LV, Weiß an LR unter dem festgelegten Mapping erhalten. |
| W-12 | Dokumentierte kompakte Steckmechanik erhalten; tatsächliche Indexlage weiter nachweispflichtig. |
| W-13 | Für REV10 neu gemessene Navigationszahlen statt alter, widersprüchlicher Linkzahlen. |
| W-14 | Veröffentlichte Softwarestände nicht mit dem ausgelesenen Gerätebestand verwechselt. |
| W-15 | Erfahrungsbericht bleibt Erfahrungsbericht, kein Herstellerfreigabebeleg für genaue Artikel/Firmware/CVs. |
| W-16 | Hersteller-Jumperregeln versionsbezogen erhalten; keine Widerstandsbrücken für diesen LED-Umbau freigegeben. |
| W-17 | Helle Platinenfläche weder als sicheres Blankkupfer noch als nachgewiesene Isolation bezeichnet. |
| W-18 | Offenen G0-Status der Schnellanleitung erhalten und an den kritischen Kurzschritten verstärkt. |

## 4. Zusätzliche Fehler aus der erneuten REV10-Gegenprüfung behoben

Diese Punkte entstanden bzw. wurden sichtbar beim Zusammenführen und Prüfen der neuen Fassung. Sie sind keine 47 zusätzlichen Befunde.

1. **E1-/Einsetz-Zirkel:** Vor Einsetzen nur Indexzuordnung und geplante Lage prüfen; tatsächlichen Sitz erst danach, aber zwingend vor Strom.
2. **Mehrdeutiges „gespiegeltes Mapping“:** gleiche Richtungs-/Ausgangslogik, gegenläufige LED-Farbverdrahtung präzise benannt.
3. **Kollidierende Schrittnamen:** Einsetzschritte heißen 9c-1 bis 9c-3 bzw. 12b-1 bis 12b-3; E1/E2/E3 bleiben Abnahmekarten.
4. **Vorzeitige Fahrprüfung:** Schritt 35 ist rein stromlose Montagekontrolle; Schritt 50 ist Sollzustandsvorbereitung. Erstfahrt und spätere Zugfahrten besitzen getrennte Voraussetzungen.
5. **Unklare G1-Voraussetzungen:** G1 fordert nicht bereits alle Anschlüsse oder den erst nach Strom möglichen Lautsprechertest L5.
6. **Falsche Herkunftsfassung durch globale Textersetzung:** Quellenkapitel nennt wieder richtig die vollständige REV9 als Ausgangsbasis.
7. **Fehlende Rückkehr nach CV-Zeilenanlage:** F.4/F.6 nennen stromlosen Wiederanschluss, erneute Aufbauprüfung und erst danach Freigeben des Prüfstroms.
8. **Verbleibende Wortverwechslung:** „Prüfenden“ als Leitungsende durch „Prüfleitungsenden“ ersetzt; Prüfpersonen bleiben sprachlich getrennt.
9. **Ausgelagerte Sicherheitskästen:** Warnungen in 9c, 12b und 17 vor die zugehörigen Handgriffe verschoben.
10. **Fast leere Nachläuferseiten:** Kapitel B, 8, 9, 9a, 12 und 16 ohne Textverlust kompakter gesetzt; die erste 98-seitige Prüfversion auf 92 Seiten bereinigt.
11. **Fortsetzungen leichter auffindbar:** Folgeseiten tragen einen passenden Kapitel-Fortsetzungsheader.
12. **T9 ausgebaut:** vollständige Funktionstastenmatrix mit Soll-/Ist-Feldern statt einzelner ausgelagerter Schlusszeile.

## 5. Projektstand und nächste sinnvolle Umsetzungswelle

**Die Dokumentüberarbeitung ist erledigt; der praktische Umbau ist nicht freigegeben.** Es wurde kein Decoder programmiert, kein Bauteil elektrisch vermessen und kein Bauteil gekauft oder verändert.

Die nächste Welle muss vor dem Löten den G0-Nachweis für das tatsächlich vorhandene Decoderpaar schließen: Masterkennung und ESU-Übernahmeformat, vollständige Aktivierungsabbildung, echte Firmwarestände, sicherer CS3-Lese-/Schreibweg sowie physische Lichtausgänge und Wiederanmeldung mit tatsächlich neuer SID. Der dokumentierte kostenlose Offline-Export ist ein sinnvoller erster Teilschritt, ersetzt aber den Hardwaretest nicht.

Parallel ohne Zerlegen: lose Bauteile beidseitig fotografieren, LoDi-Revision/Steckstruktur erfassen, vorhandene Prüfgeräte und Geräteartikel dokumentieren. Reale Netz-, Halter-, LED- und Kupplungsnachweise dürfen danach nicht durch vermeintlich universelle Beispielwerte ersetzt werden.

Die genauen Endprüfergebnisse der Datei stehen in [Abschlussprüfung REV10](</Users/martinwaelter/ICE Umbau/ICE2976_REV10_ABSCHLUSSPRUEFUNG.md>).
