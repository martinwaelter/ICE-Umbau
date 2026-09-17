# Bild- und Zeichnungsinventar für REV11

Stand: 11.09.2026. Unabhängige Sichtung von `Arbeitsstand_REV10/figure_namespace.py`, `build_rev10.py`, `rev10_document.py`, `rev10_sections.json`, den alten Quellbuildern und den tatsächlichen Bilddateien. Originaldateien und REV10 wurden nicht geändert. Alle nachfolgend empfohlenen Fotos wurden visuell betrachtet. Die neu gesicherten LoDi-Dateien sind unveränderte Originalbilder aus den in der archivierten Herstellerseite angegebenen Galerie-URLs; Manifest mit Quell-URL, Pixelmaßen und SHA-256: `Arbeitsstand_REV11/bilder_quellen/manifest.json`.

## Redaktionelle Entscheidung

Eine kompakte, dennoch verständliche Werkstattanleitung braucht die Bilder direkt beim Handgriff. Die bisherigen separaten Bildkapitel 21–23 mit ihrer Textwiederholung sollten in die Arbeitsfolge aufgehen. Ein Foto darf Bauteile identifizieren, aber keine unsichtbare elektrische Verbindung oder die Passung eines anderen Modells behaupten. Empfohlen sind etwa 12–15 gezielt gesetzte Foto-/Herstellerabbildungen und 5–7 lesbare Funktionsschemata innerhalb des Hauptdokuments; keine eigene Bildgalerie als Anhang.

Der stärkste Gewinn ist nicht eine künstliche Schärfung: Für die Motorfotos sind jetzt echte 2048-Pixel-Dateien vorhanden, für die Frontmodule echte Detailfotos der drei Pads. Diese ersetzen die bisher kleinen Webvorschauen.

## Bereits in REV10 verwendete Fotos

Alle Pfade in dieser Tabelle sind relativ zu `/Users/martinwaelter/ICE Umbau/`.

| Asset / Auflösung | Tatsächlich sichtbarer Inhalt | Auswahl und konkrete Nutzung | Grenzen / Korrektur |
|---|---|---|---|
| `Arbeitsstand_REV10/bilder/0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg`, 842×204 | Eigenes Fahrzeug im alten Zustand, Feldspulenmotor links, lange grüne Altplatine | Behalten: schmale Übersicht beim ersten Öffnen und Dokumentieren, ca. 155–170 mm breit | Kein Montagebild des 60941. Nur ca. 126 dpi bei 170 mm; nicht stärker aufblasen. |
| `Arbeitsstand_REV10/bilder/BAD231CB-B878-4D94-B5EE-CDAB1D69D455_4_5005_c.jpeg`, 662×260 | Eigener alter Motor seitlich, Feldspule und alte Litzen | Optional neben der Übersicht oder zugunsten Montagezeichnung weglassen | Geringe Auflösung und dunkle Anschlussstellen; nicht als Messpunktfoto benutzen. Der Zugriff auf mutmaßliche größere Originale in der macOS-Fotomediathek wurde vom Betriebssystem verweigert; nicht verfügbar. |
| `Arbeitsstand_REV10/bilder/image-2.jpg`, 322×1280 | Eigene rote Platine: K1, schwarze 21MTC-Struktur, LS1/LS2, R3–R6, beide Befestigungsringe | Zwingend behalten: etwa 45–50 mm breiter, 180–200 mm hoher Streifen mit Erklärung daneben; nur einmal vollständig zeigen | Sichtbare Seite bestätigt nicht die Revision oder Padbeschriftung der Rückseite. Schwarze Struktur ist nicht als Schutzkappe identifiziert. Keine zusätzliche winzige Wiederholung auf der Steckseite. |
| `Arbeitsstand_REV10/bilder/image-4.jpg`, 1820×137 | Eigene weiße MT-37700 V4.3 als flache Draufsicht, an beiden Enden L/O/B; TRIMM und SJ2/Türbeleuchtung | Zwingend behalten: volle Breite, zusätzliche vektorielle Endmarkierung mit L/O/B; nachfolgend kurze Anschlussliste RT→O, GE→L | Bild ist sehr flach; nicht in einen hohen Rahmen strecken. SJ2 ist Türbeleuchtung, keine Auswahl AUX1/AUX4. |
| `Arbeitsstand_REV10/bilder/image-5.jpg`, 1820×606 | Eigene weiße V4.3 in Bordrestaurant-Wagen, Gehäuse dahinter; Endpads erkennbar | Behalten: zeigt Lage und Raum für Litzen, unmittelbar bei Wagenmontage, ca. 165–175 mm breit | Zeigt noch keine vollständig validierte Kupplungsverdrahtung. Kein Foto einer fertigen Zugabnahme. |
| `Arbeitsstand_REV10/quellen_alt/tmp/pdfs/rev5/research/motor_a.jpg`, 957×400 | LoDi-Vergleich 33701: Permanentmagnet, drei orange Kondensatoren, zwei Drosseln | Durch `Arbeitsstand_REV11/bilder_quellen/motor_a_2048.jpg` ersetzen | Vergleich enthält bereits Permanentmagnet. Kein Foto des alten Nutzermotors. |
| `Arbeitsstand_REV10/quellen_alt/tmp/pdfs/rev5/research/motor_c.jpg`, 1004×400 | LoDi-Vergleich nach Entfernen der beiden Massekondensatoren / Abtrennen der Altplatine | Durch `Arbeitsstand_REV11/bilder_quellen/motor_c_2048.jpg` ersetzen; direkt bei Messkarte | Keine vorhandenen Prüfclips, kein Messgerät; zeigt identifizierbare Punkte, keinen bestandenen Test. |
| `Arbeitsstand_REV10/quellen_alt/tmp/pdfs/rev5/research/dummy_full.jpg`, 4032×2614 | LoDi-Vergleich 33701: motorloses Chassis und ausgebaute grüne Altplatine | Behalten, aber einmal im Kapitel Gegenkopf; 140–170 mm breit, maximal halbe Seite | Bildnase/Lampenende rechts, Kupplungsende links. Stützen trugen Altplatine; kein Passungsbeleg für kleinen Märklin-Träger. Lose Litzen sind Altzustand. |

`image.jpg` ist dieselbe sichtbare rote Platinenansicht wie `image-2.jpg`; keine zweite Perspektive. `image-3.jpg` ist eine niedrig aufgelöste, gedrehte Darstellung der weißen V4.3 (94×1280) und bietet gegenüber `image-4.jpg` keinen Zusatznutzen.

## Neu gesicherte, visuell geprüfte Originale

Gemeinsamer Ordner: `/Users/martinwaelter/ICE Umbau/Arbeitsstand_REV11/bilder_quellen/`. Alle sind LoDi-Herstellerbilder vom Vergleichsumbau 33701; keine Fotos des tatsächlichen 2976-Umbaus.

| Datei / Auflösung | Inhalt | Empfehlung |
|---|---|---|
| `motor_a_2048.jpg`, 2048×856 | Genau derselbe Bildausschnitt wie REV10 Motorfoto vor Anpassung, deutlich schärfere Kondensatorenden | Zwingend einsetzen. Vorhandene normierte Markierungen aus REV10 können übernommen und visuell gegenkontrolliert werden. |
| `motor_c_2048.jpg`, 2048×816 | Genau derselbe Bildausschnitt wie REV10 Motor-Messpunktfoto | Zwingend einsetzen. Eine gemeinsame Doppelseite Montage/Entstörung/Messen ist sinnvoller als spätere Bildanlage. |
| `front_led_2048.jpg`, 2048×1216 | LoDi-Frontmodul von beiden Seiten: schwarzer Halter, rote Rückseitenplatine, sichtbare LED | Behalten, etwa halbe Breite. Zeigt den Unterschied zwischen Halterfront und Lötseite. |
| `front_led_kabel_1.jpg`, 1276×1414 | Senkrechte Detailansicht der drei Lötpads: links `red`, Mitte `VCC`, rechts `white` in genau dieser Bildorientierung | Höchste Priorität; neben den Anschlussregeln platzieren. Labels in Vektorzeile außen ergänzen, nicht die Platinenaufschrift übermalen. Orientierung am Aufdruck, nie pauschal am Fahrzeug-Links/Rechts. |
| `front_led_kabel_2.jpg`, 2048×1682 | Eingebauter LoDi-LED-Einsatz im Vergleichsmotor: gelb an red, braun an VCC, grau an white | Optional als zweite Teilansicht zur mechanischen Lage/Litzenführung. Direkt erläutern: Braun ist hier LED-Plus des Vergleichs, nicht automatisch Radmasse. Die neue Anleitung soll nach Funktion statt nach fremder Kabelfarbe arbeiten. |
| `front_led_kabel_3.jpg`, 2048×1470 | Trotz Dateiname: ALTE GLÜHLAMPENFASSUNG mit alten Kabeln, keine LED-Platine | Nicht als LED-Anschlussfoto einsetzen. Nur bei explizitem Vorher/Nachher-Paar geeignet; sonst weglassen. |
| `lodi_motor_montiert_original.jpg`, 2959×924 | Beschriftete rote Motorplatine V1.49 im Vergleichskopf: SW, RT, GE links; MASSE, MOT_L/R, VCC, AUX3, L_RT/L_WS rechts | Sehr wertvoll als große beschriftete Vergleichsübersicht zur Pad-Namenstabelle. Nicht als eigene Rückseite ausgeben und nicht auf eigene Platinenansicht spiegeln. Kein SJ1/SJ2 vorhanden; niemals V1.50-Jumperlage daraus ableiten. |
| `lampe_alt_original.jpg`, 914×868 | Ausgebauter alter Glühlampenhalter | Für kompakte Anleitung weglassen, wenn alte Fassung bereits im eigenen Foto eindeutig angesprochen wird. |

## Herstellerzeichnungen und verlustfreie Quellen

| Quelle | Wiederverwendung | Nutzen / Einschränkung |
|---|---|---|
| `/Users/martinwaelter/ICE Umbau/Pruefnachweise/REV9_Berichtsabgleich/Maerklin_60941_Original.pdf`, Seite 2 (0-basiert 1) | Original-Montagezeichnung, ideal als PDF-Vektor oder sauber gerenderter Ausschnitt des oberen Montagebereichs | In REV10 nicht als Abbildung sichtbar, obwohl als Quelle genannt. Für REV11 zentral: Ausbau-/Einbaufolge Magnet, Anker, Motorschild, Schrauben, Bürsten, Drosseln. Bildnummern 1–6 anhand der Herstellerstückliste erklären. Unterer Recycling-/Adressblock ist für Arbeitsschritt nicht erforderlich. Die Zeichnung zeigt keinen zugesicherten Quer-Kondensator. |
| `/Users/martinwaelter/ICE Umbau/Pruefnachweise/REV9_Berichtsabgleich/Maerklin_60941_Zeichnung.png`, 1700×1207 | Vorhandener Gesamtseitenrender als schnelle Alternative | Bei 170 mm Gesamtbreite immer noch lesbar, aber unnötiger Recyclingbereich nimmt Platz. |
| `/Users/martinwaelter/ICE Umbau/Pruefnachweise/REV9_Berichtsabgleich/Maerklin_60977_Original.pdf`, Seite 5 (0-basiert 4) | Trägerzeichnung links, als Vektor/hochauflösender Originalausschnitt | Verbindliche Padnamen LR, +Ub, LV, MR/MV, 0/GL, B/GR sowie AUX1–4. Im Gegenkopf steht vor der Grafik ausdrücklich: ESU 59649 auf Märklin-Träger, nicht 60977-Soundbelegung. Farbvergleichstabelle besser als kleine aufgabenspezifische Texttabelle daneben statt ganze Herstellerseite. |
| Dieselbe PDF, Seite 6 (0-basiert 5) | Linke Einsteckzeichnung einschließlich kleinem Warn-Seitenprofil | Unbedingt Warn-Seitenprofil behalten. Die vorhandene PNG-Datei `Arbeitsstand_REV10/bilder/ice2976_stecken-006.png` (845×600) ist für starkes Vergrößern schwach; Original-PDF erlaubt bessere Ausgabe. Grafik ist Herstellermechanik, nicht Foto des bereits montierten 59649. |
| `Arbeitsstand_REV10/bilder/ice2976_60977-p5-pads.jpg`, 2200×1561 | Vorhandener Render der Seite 5 | Sauberer Ersatz, falls Vektorimport unpraktisch. REV10 `SourceView('SourceDiagram')` zeigt Ausschnitt `(0.045,0.225,0.49,0.77)` und erhält die Platine. |

## Vorhandene Funktionen und Skizzen

`Arbeitsstand_REV10/figure_namespace.py` enthält `MarkedPhoto(path, width, marks, maxh)` mit getrennten PDF-Vektorlinien und Nummern auf unverändertem Bild sowie `Sketch(kind, height)`. Die Koordinaten der Markierungen stehen vollständig in `Arbeitsstand_REV10/rev10_sections.json`; deshalb nicht anhand der gedruckten PDF neu erraten.

| Sketch-Kind | Inhalt | Empfehlung für REV11 |
|---|---|---|
| `grounds` | Gleis B/0 → Decoder → U+/Lichtausgang | Behalten, aber mit tatsächlicher Gesamtübersicht kombinieren. U+, Decoder-GND, Gleis 0 sprachlich eindeutig trennen. |
| `motor` | Soll isolierter Motor / Fehler Massekontakt | Behalten, direkt an die Messkarte. `OL messen` gilt hier nur für geeigneten vollständig getrennten Motoraufbau mit den vor-/nachgelagerten Kontaktkontrollen; nicht als universelle Regel für bestückte Platinen. |
| `caps` | Quer-Kondensator und unerlaubter Bezug zum Chassis | Mit Motorfoto zusammenführen; keine Behauptung, ein Quer-Kondensator sei im 60941 immer enthalten. Foto entscheidet über Vorhandensein, Nachweis über Eignung. |
| `screw` | Gewollte Auflage versus Signalbahnkontakt | Einmal bei Befestigung einsetzen. REV10 wiederholt es in Kapitel 7 und 9; Doppelung streichen. Skizze ist nur Prinzip, keine Ringnetz- oder Schraubenlängenfreigabe. |
| `led` | Je Farbe eigener Vorwiderstand; gemeinsames U+ | Behalten, vorzugsweise durch konkretes vorderes und hinteres Funktionsschema nebeneinander präzisieren: hinten gegenläufige Zuordnung von Weiß/Rot zu LR/LV. Keine LED-Grenzwerte erfinden. |
| `bus` | RT durch gesamten Zug, GE nur vorn gespeist und hinten isoliert | Zwingend behalten und besser auszeichnen: RT bedeutet Gleis B, GE bedeutet geschalteter Wagenlichtpfad, jede weiße Leiste RT→O und GE→L; örtliches B-Pad nur bestätigter Radkontakt. Eindeutige Quellen-/Rückleiterdarstellung, keine Verbindung von Decoder-U+ untereinander. |
| `ammeter` | Strommessung in Reihe, A-Meter quer als Kurzschluss | Nur zusammen mit definiertem geeigneten Mess-/Begrenzungsaufbau. Allein zu simpel für eine ausführbare Lastprüfung. |
| `brake` | Kontakt → CS3-Zuordnung → Fahrbefehl | Im aktuellen Kernumbau streichen oder auf einer halben Schlussseite spätere Erweiterung. Signalsteuerung wird nicht durch Umbauabnahme miterledigt. |

`Arbeitsstand_REV10/build_rev10.py` enthält `SourceView('ClipDiagram')`; sein Ausschnitt `(0.04,0.055,0.47,0.925)` umfasst den deutschen Kurztext und alle linken Steck-Warngrafiken. Importieren des gesamten Builders würde REV10 neu erzeugen; nur die vorhandenen Figurenklassen gezielt verwenden oder in REV11 nachbilden.

## Zu übernehmende normierte Markierungen

Koordinatenformat wie `MarkedPhoto`: Nummer, Ziel-x, Ziel-y, Nummer-x, Nummer-y; y von oben. Mit den neuen 2048-Motorbildern bleiben die normalisierten Bildbezüge gültig (leichte 1-Pixel-Rundung der Seitenverhältnisse ohne inhaltlichen Ausschnittwechsel).

```python
motor_a_marks = [(1,.439,.279,.215,.08), (2,.641,.508,.865,.677),
                 (3,.482,.442,.466,.805), (4,.523,.252,.620,.065)]
# 1 oberer linker Massekondensator, 2 rechter Massekondensator,
# 3 mittiger Querkondensator, 4 Drossel im Motorzweig.
motor_c_marks = [(1,.329,.334,.186,.075), (2,.367,.356,.555,.075),
                 (3,.271,.328,.170,.674), (4,.433,.554,.554,.822)]
# 1/2 Motorfahnen; 3 Schraube links oben, 4 Öse rechts unten:
# 3/4 sind mögliche Referenzpunkte, erst elektrisch bestätigen.
red_board_marks = [(1,.45,.584,.50,.44), (2,.32,.289,.77,.32),
                   (3,.825,.674,.66,.745), (4,.775,.827,.44,.865),
                   (5,.126,.206,.23,.105), (5,.846,.916,.67,.967)]
dummy_marks = [(1,.949,.241,.929,.494), (2,.745,.048,.599,.079),
               (3,.205,.108,.136,.256), (4,.542,.787,.37,.618),
               (5,.076,.052,.405,.03)]
```

## Nicht verwenden / offene reale Bildnachweise

- `motor_overview.png`, `dummy.png`, `wiring.png`, `dummy_bare.png` im alten Researchordner sind identische 794×2-Pixel-Dateien. Die archivierte Herstellerseite belegt hier horizontale 4206×8-Zierlinien. Es sind keine tatsächlichen Übersichtsfotos oder Schaltpläne; Dateinamen waren irreführend.
- `motor_b.png` enthält eine bereits auf der Herstellerseite bearbeitete Variante des Motorfotos; gegenüber dem unveränderten `motor_a` mit eigenen getrennten Vektormarkierungen kein Vorteil.
- `jumper.png` zeigt eine echte V1.50-Platine und eine bereits vorhandene blaue Handmarkierung. Nur als eindeutig fremde V1.50-Referenz sinnvoll; nicht die eigene Revision behaupten. Für kompakte REV11 genügt meist die Zustands-/AUX-Tabelle plus Foto des eigenen Aufdrucks, sobald vorhanden.
- Eigene Rückseite/Revision der roten Platine, tatsächliche schwarze 21MTC-Struktur/Indexposition, realer hinterer Schleifer-/Radkontakt, tatsächliche Halterung und Dachfreiheit sowie konkreter Lautsprecheradapter sind noch nicht bildlich bestätigt. Keine KI-generierten oder schematischen Ersatzbilder als Beweis ausgeben.
- Keine fiktiven CS3-Bildschirmfotos erzeugen. Für den momentanen Eigenweg reichen präzise Bedienfolge und eine beschriftete Daten-/CV-Karte. Echte Screenshots erst nach tatsächlichem Lesen der Software-/Geräteansicht.

## Empfohlene Bildfolge im kompakten Dokument

1. Eine echte alte Fahrzeugübersicht neben Teile-/Arbeitsfolge; keine großformatige dekorative Titelseite.
2. Ein Gesamtschema mit Motortriebkopf, RT/GE-Bus, Wagen und Gegenkopf; vollständige Netznamen und örtliche Rückleiter.
3. Märklin-60941-Montagezeichnung bei Ausbau-/Einbauschritten.
4. Hochauflösendes Kondensatorfoto und kleines richtig/falsch-Schema unmittelbar bei Entstörung.
5. Hochauflösendes Messpunktfoto mit echter Sechs-Messungs-Karte, keine spätere Fotosammlung.
6. Eigene rote Platine groß + nummerierte Funktionslegende; V1.49-Beschriftungsfoto als klarer Vergleich zur Padliste.
7. Frontmodul-Detailfoto `red/VCC/white` + tatsächlich geplante Anschlusszeichnung; mechanische LED-Seitenansicht nur wenn Platz sinnvoll.
8. Hersteller-Trägerzeichnung + hinteres Farbschema + Steck-Warnzeichnung direkt vor jeweiligem Handgriff.
9. Ein Gegenkopf-Vergleichsfoto neben Halter-/Freiraumprüfung, keine daraus abgeleitete Schraubenlänge.
10. Weiße V4.3 als Draufsicht und im Wagen; daneben RT→O/GE→L und Kupplungsprüfreihenfolge.
11. Eine kleine Prüfstands-/Einzelquellenzeichnung bei Erstinbetriebnahme und ein klarer Ablauf für Gehäuseabschluss.

Damit enthält die Anleitung sowohl echte Detailerkennung als auch lesbare Funktionslogik, ohne durch doppelte Vollfotos und ausgelagerte Bildkapitel wieder auf 90 Seiten zu wachsen.
