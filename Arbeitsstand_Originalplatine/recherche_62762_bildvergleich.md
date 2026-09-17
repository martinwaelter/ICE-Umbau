# Bildvergleich der Märklin-Altplatine mit 62762

Stand: 12.09.2026. Begrenzte Untersuchung von Bildidentität und Geometrie; keine Schnitt-, Löt- oder Anschlussfreigabe. Die Haupt-PDF wurde nicht geändert.

**Ergebnis:** Die lange Platine im eigenen Foto `0D2DC…` ist ein **sehr starker geometrischer Kandidat für 62762, Layout 03/92 VER1.1**. Mehrere voneinander unabhängige Form- und Leiterzugmerkmale stimmen mit den ausdrücklich beschrifteten Vergleichsplatinen überein. Der Aufdruck am eigenen Exemplar ist in der verfügbaren kleinen Aufnahme jedoch nicht zweifelsfrei lesbar. Deshalb bleibt die konkrete Typzuordnung eine begründete Bildinferenz. Eine identische Verdrahtung des eigenen 2976 folgt daraus nicht.

## Bildnachweise und Herkunft

| Kürzel | Datei / Herkunft | Auflösung | Aussagegrenze |
|---|---|---:|---|
| E1 | `Arbeitsstand_REV10/bilder/0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg` | 842 × 204 | Eigenes vollständiges offenes Fahrzeug, Leiterzugseite der eingebauten Altplatine. Aufdruck zu klein für sichere Lesung. |
| E2 | `Arbeitsstand_REV10/bilder/BAD231CB-B878-4D94-B5EE-CDAB1D69D455_4_5005_c.jpeg` | 662 × 260 | Eigener Motor und seitlicher Blick unter die lange Platine. Keine vollständige Gegenansicht der Platine. |
| V1 | `Arbeitsstand_REV10/quellen_alt/tmp/pdfs/rev5/research/dummy_full.jpg` | 4032 × 2614 | Herstellervergleich: motorloser Kopf des Beispiels **33701**, Altplatine daneben; Aufdruck **62762 / 03/92 / VER1.1** klar sichtbar. |
| V2 | `Arbeitsstand_Originalplatine/belege_62762/ebay_147416253187_bild2.webp` | 1600 × 1200 | Verkäuferfoto: linke Platine 62761, rechte Platine 62762; rechte Leiterzugseite eigenständig visuell geprüft. |
| V3 | `Arbeitsstand_Originalplatine/belege_62762/ebay_147416253187_bild1.webp` | 1600 × 1200 | Gegenansicht desselben angebotenen Paares; rechts lange weitgehend unbestückte Platine mit Schiebeschalter. |

Die Herkunft von E1/E2 aus der persönlichen Fotos-Mediathek steht in `Arbeitsstand_REV10/source_manifest.json`, Zeilen 29–30. Die Bildverwendung von V1 einschließlich ursprünglicher Bild-URL steht in `Arbeitsstand_REV10/quellen_alt/build_ice2976_rev5.py`, Zeilen 436–439. [LoDi-Herstellerseite zum ausdrücklich genannten Beispiel 33701](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/) und [Originalfoto V1](https://image.jimcdn.com/app/cms/image/transf/none/path/s5b4f033edf99a04d/image/i8a71bb7234a2f1cb/version/1635701141/image.jpg).

V2/V3 sind **Bildbelege eines Fremdexemplars**, keine Herstellerbestätigung für die elektrische Funktion des Nutzerexemplars. Die angebotene Bezeichnung 627610/627620 allein wurde nicht als Identitätsbeweis benutzt. [Angebot mit fünf Bildern](https://www.ebay.de/itm/147416253187), [Bild 2 mit lesbarer 62762](https://i.ebayimg.com/images/g/ia4AAeSwbg9qSUlk/s-l1600.webp). Die Bilddateien wurden im Team bereits als Evidenz archiviert und hier anschließend lokal angesehen.

## Geometrischer Abgleich

Orientierung: **E1 unverändert**, Motor links. **V2 rechte Platine gedanklich 90° gegen den Uhrzeigersinn**, V1 lose Platine gedanklich 180°. Keine Spiegelung der Leiterzugseite vornehmen. Alle Positionsangaben betreffen diese gemeinsame Blickrichtung; sie sind keine Fahrzeuganschlussbezeichnungen.

| Prüfmerkmal | Beobachtung am eigenen E1 | Bedeutung für den Vergleich |
|---|---|---|
| Befestigung / Bohrungen | Links oben dunkler Schraubkopf, links unten kleine freie Bohrung; rechts unten große Bohrung. Die entsprechende Stelle rechts oben ist nur schwach sichtbar. | Drei deutlichere Positionen und die schwächere vierte liegen passend zum 62762-Muster. Kein zuverlässiges Maß oder elektrisch geprüfter Schraubkontakt. |
| Kantenkerben | Obere Kerbe etwas rechts der Mitte, untere Kerbe weiter rechts. | Auffällige, gleichgerichtete Längsversetzung passt zu V1/V2. |
| Leiterzugmuster | Mehrere lange parallele Züge mit gemeinsamem schrägem Versatz an beiden Enden; breite Randflächen. | Passt zum vergleichsweise einfachen 62762-Muster; klar anders als das dichte kleinteilige 62761-Muster in V2 links. |
| Innere Lötstellen | Kleine Dreiergruppe nahe dem linken Ende; weiter innen ein einzelnes rundes Pad und zwei eng benachbarte Pads am unteren Teil des Leiterbündels. | Die Kombination aus Dreiergruppe, Einzelpad und Padpaar passt in Lage und Reihenfolge zu V1/V2. Keine Funktion aus den Padpositionen abgeleitet. |
| Endkontakte | Rechts ein auffällig breites verzinntes Feld und schmalere Randkontakte; links Kabel-/Lötstellen teilweise verdeckt. | Passende Kontaktgeometrie. Anzahl und elektrische Belegung der angeschlossenen Drähte bleiben am eigenen Foto unvollständig. |
| Aufdruck | Schwacher Schriftbereich oberhalb der mittleren Leiterzüge, in E1 auf dem Kopf stehend. | Lage passt; **die Ziffernfolge wird am eigenen Bild nicht als sicher abgelesen ausgegeben**. |

E2 bestätigt die räumliche Situation: alter Motor mit sichtbarer Feldwicklung links, lange Platine darüber/rechts, mehrere Kabel und ein dunkles Bauteil darunter. E2 zeigt weder einen vollständig lesbaren alten Decoderaufdruck noch alle Lötendpunkte. Das dunkle Bauteil wird aus diesem Foto allein nicht als konkreter Decoder oder Umschaltertyp identifiziert.

V3 zeigt an der rechten Vergleichsplatine den Schiebeschalter und die zu V2 spiegelbildlich passenden Kerben/Bohrungen. Das stützt die Zuordnung der beiden **Fremdansichten** zueinander. Es liefert noch keine eigene Gegenansicht von E1 und keinen Beleg für dessen unveränderte Schalterverdrahtung.

## Lokale und zusätzliche Suche

- Textsuche nach `62762`, `627620`, `6276` und Varianten `62 762` / `62.762` / `62-762` in lokalen Markdown-, Text-, JSON-, Python- und CSV-Dateien: zu Beginn dieser Untersuchung keine einschlägige Nennung; lediglich numerische Layout-Falschpositive. Später erstellte Recherchedateien sind keine unabhängigen Altbelege.
- Textschichten der Haupt-PDFs REV9–REV13 und `ICE_2976_Forensische_Recherche_OHNE_HAENDLER.pdf`: keine entsprechende Nummernfundstelle. Das ist **keine** Widerlegung des sichtbaren Bildaufdrucks in V1; Bildtexte werden von der Textsuche nicht zuverlässig erfasst.
- Breite Web-Bildsuche nach 62762/627620 plus Unterseite/bottom/solder side lieferte überwiegend unpassende Decoderbilder. Der direkte Paar-Bildfund V2/V3 ist erheblich aussagekräftiger als diese Suchtreffer.
- Historische Foren nennen ebenfalls `62762 03/92 Ver1.1`, teils dieselbe wiederveröffentlichte Anfrage. Diese wurden nur als Suchhinweis eingeordnet, nicht als Schaltplan oder unabhängiger Funktionsbeleg: [Stummiforum 2019](https://www.stummiforum.de/t166791f29-M-rklin-ICE-f-hrt-nicht.html), [gleichartige Anfrage im H0-Modellbahnforum](https://www.h0-modellbahnforum.de/t341874f19606-ICE-faehrt-nicht.html).

## Verwendbare Schlussfolgerung für die weitere Anleitung

Die Recherche kann nun konkret auf **62762 / 03/92 / VER1.1 als sehr wahrscheinliche vorhandene Leiterplattenausführung** aufbauen. Es wäre falsch, weiterhin jede Altplatine nur als beliebiges unbekanntes grünes Bauteil zu behandeln. Ebenso falsch wäre die Aussage „62762 am Nutzerexemplar sicher abgelesen“ oder „alle Anschlüsse entsprechen dem 33701-Foto“.

Für eine exakte bebilderte Anschlussdarstellung bleiben am eigenen Exemplar insbesondere vollständiger Aufdruck, Gegenansicht mit Schalter und eventuell verdeckten Bauteilen, sämtliche Kabelendpunkte sowie elektrische Verbindungen der Schraubringe offen. Die Übereinstimmung der Leiterplattengeometrie ersetzt diese Zuordnung nicht. Keine der hier untersuchten Aufnahmen belegt für das eigene Exemplar bereits einen zulässigen Trennpunkt, einen neuen LED-Vorwiderstandswert, einen Pufferanschluss oder die Freigabe des GE-Wagenlichtnetzes.

## Prüfsummen der unmittelbar verglichenen Bilder

```text
E1  4e69d2084c348f60762c73788e1a327764fc2d79a317d4c2a63500f04967c8f2
E2  73612a13554c5dd8dfd1cb3a21b3232fdfadfa6b78716e8053742476085b53cb
V1  505888c7965e458927145843589dc0aa86bb6b6e7b24f9c054d33ecae43ee9da
V2  b6ede1c1b29fd6974453681f13451bba06e84ed58d854398a5e88e8624c09bf1
V3  214be318f0bc3dc68c7c183fcbc331a4d8eea32a3cfdf0d120ae3d6a338ac6a6
```
