> **Fortschreibung 12.09.2026:** Die später gezielt recherchierte Platine 62762 ist jetzt aus zwei unabhängigen Quellen beidseitig fotografisch belegt. Frühere Aussagen dieses Arbeitsentwurfs über fehlende Vergleichsseiten oder aktive Bestückung der langen Platine sind entsprechend überholt. Maßgeblich sind die Dateien `recherche_62762_*.md`, der neue Bildbefund und `eingangsstand.json`. Die tatsächliche Netzzuordnung des eigenen Exemplars bleibt offen; 60972/60982 sind inzwischen als vorhanden genannt.

# ICE 2976: Originalplatine behalten, LoDi-Motorplatine entfällt

Recherchebefund vom 12.09.2026. Begrenzte Prüfung für die separate Umbauanleitung; keine Ausführungsfreigabe für noch unbekannte Leiterbahntrennungen. Originale Nutzermotive haben Vorrang vor Vergleichsfahrzeugen. Ob auch Front- und Wagenmodule von LoDi entfallen, ist noch offen.

## Ergebnis

**60941 und 60977 bilden einen technisch passenden Grundweg für einen tatsächlich vorhandenen Trommelkollektormotor mit Feldspule. Die originale lange Märklin-Platine kann grundsätzlich als mechanischer Träger und als überprüfte passive Löt-/Verteilerplatine weiterverwendet werden. Ein belastbarer, veröffentlichter Trennstellenplan für genau Martins Platine wurde nicht gefunden.** Der Umbau darf daher derzeit als Architektur beschrieben werden; konkrete Auslötpunkte und Leiterbahntrennungen benötigen die Bauteilseite und eine Durchgangskarte des tatsächlichen Exemplars.

Das ist keine Empfehlung, die Originalplatine heimlich gegen eine neue Leerplatine zu ersetzen. Auch ihre alte aktive Analogschaltung darf aber nicht unbesehen als Teil der neuen Decoderschaltung weiterarbeiten.

## Was die vorhandenen Originalbilder tatsächlich zeigen

Beide Dateien wurden visuell geprüft:

- [Gesamtansicht, 842 × 204 Pixel](../Arbeitsstand_REV10/bilder/0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg): lange Platine mit sichtbaren Leiterzügen/Lötstellen, Befestigungen und Leitungen; Motor links. Die gegenüberliegende Bestückungsseite ist verdeckt. Eine vermeintliche Platinenkennung lässt sich nicht zuverlässig lesen.
- [Seitliche Nahansicht](../Arbeitsstand_REV10/bilder/BAD231CB-B878-4D94-B5EE-CDAB1D69D455_4_5005_c.jpeg): Feldspule am Motor, Motorkontakte und mechanische Relaisbaugruppe unter dem Originalträger sichtbar. Die verdeckten Anschlüsse/Komponenten bleiben unbestimmt.

**Nicht aus den Fotos ableitbar:** vollständige Netzliste, genaue Relaiskontakte, elektrische Kupplungspole, Bauteilwerte, verborgene Brücken, Potential der Schraubpunkte, zulässige Belastbarkeit einzelner wiederzuverwendender Leiterzüge. Deshalb keine Markierung „hier schneiden“, kein nacherfundenes Padlabel und keine Übernahme der LoDi-Bezeichnungen GE/O/RT auf alte Kupferflächen.

## Abgrenzung: Fahrtrichtungsumschalter und Schleiferumschaltung

Ein mechanischer **Fahrtrichtungsumschalter** verändert die analoge Motorbeschaltung. Eine **Schleiferumschaltung** wählt zwischen zwei räumlich getrennten Stromabnehmern. Ein sichtbares Relais allein beweist die zweite Funktion nicht. Sie wäre nur über nachvollzogene Anschlüsse zu beiden Schleifern und die Kontaktfunktion nachgewiesen.

Ein exakter 2976-Originalautor beschreibt DCM und mechanischen Fahrtrichtungsumschalter, zunächst dauerndes weißes Licht und erst nachzurüstende stromführende Kupplungen. Er meldet später den erfolgreichen HLA-/Decoderumbau samt Lichtwechsel; verwendet wurde das einfache Märklin-Set, nicht nachweislich 60977. Ein beibehaltener Originalträger oder ein Kupferplan werden nicht dokumentiert. Das ist ein Machbarkeitsbeleg für den Digitalumbau, kein nachbaubarer Platinenplan. [KleenerMug, Beiträge 1, 3, 7 und 14, 03.–18.02.2017](https://www.stummiforum.de/t146166f5-Digitalisierung-analoger-M-rklin-ICE.html)

Ein zweiter Besitzer beschreibt ein analoges Exemplar mit einem Motor, einem analogen Umschalter, einzelnen Glühlampen, fehlenden elektrischen Kupplungen und eigenem hinterem Lichtschleifer. Andere Teilnehmer identifizieren es anhand der Betriebsnummer als 2976 und sehen keine Schleiferumschaltung. Diese Identifizierung ist ein Besitzer-/Forenbefund, keine Märklin-Werkszeichnung. Die damaligen Bestückungsfotos sind als Abload-Verweise vorhanden, heute aber nicht verlässlich abrufbar; sie wurden deshalb **nicht** als visuell verifizierte Platinenbelege verwendet. [Mephistopeles, Beiträge 1–6, 14.06.2018](https://www.stummiforum.de/t160284f29-Welcher-M-rklin-ICE-ist-das.html)

Die niederländische Diskussion mit dem Titel „3370“ korrigiert gerade diese anfängliche Modellzuordnung anhand eines geöffneten vereinfachten Zuges. Sie enthält reale Fotoanhänge, aber widersprüchliche Variantenvermutungen und nur ein zitiertes Fremdverzeichnis für 2976. Ihre Anhangbilder waren im verwendeten Zugriff nicht sichtbar. **Kein Beleg für Martins Platinenrevision.** [Herman H und Diskussion, insbesondere Beiträge 10, 13, 14 und 17, Dezember 2019](https://forum.3rail.nl/index.php?topic=77772.0)

Folgerung: Eine werksseitige Schleiferumschaltung wird für diesen Umbau nicht unterstellt. 3370, 3770, 33701 sowie ICE Experimental 3371/3671 liefern keinen automatisch passenden 2976-Schaltplan.

## Herstellerdaten für den neuen Antrieb

Märklin beschreibt **60941** als Umrüstsatz für die meisten H0-Trommelkollektormotoren zum fünfpoligen Hochleistungsantrieb. Das bestätigt die Motorfamilie, keine pauschale mechanische Freigabe jeder Einzelmontage. [Märklin 60941](https://www.marklin.com/products/details/article/60941), [Original-Montageblatt 60941/60943](https://static.maerklin.de/damcontent/e3/bb/e3bb202fe80385cc96835d783af5e1821670919973.pdf)

**60977** ist für Hochleistungs-/Gleichstrommotoren vorgesehen und enthält eine eigene 21-polige Schnittstellenplatine. Deren zusätzliche Verwendung ersetzt nicht zwangsläufig den langen Originalträger; Einbauhöhe, Befestigung und Isolierung müssen am Modell geprüft werden. [Märklin 60977](https://www.marklin.com/products/details/article/60977)

Die Originalanleitung verlangt bei Feldspulenmotoren einen passenden Motorumbau und den Ausbau der alten Umschalteinheit. Sie nennt für den Märklin-Kabelbaum: rot = Mittelleiter, braun = Schienenaußenleiter, grün/blau = Motor, grau/gelb = Licht, orange = gemeinsamer positiver Funktionsleiter. Orange darf nicht mit Fahrzeugmasse verbunden sein. LED-Betrieb verlangt einen Vorwiderstand. Relevante Grenzen: Motor 1,1 A, einzelner verstärkter Ausgang 250 mA, Licht und AUX zusammen 300 mA. **Das sind Decodergrenzen, keine Freigabe für unbekannte alte Leiterzüge.** [Märklin Originalanleitung 60975/60976/60977, S. 3–5](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf); lokal geprüft: `Pruefnachweise/Forschung_ohne_Haendler_20260910/hardware_quellen/maerklin_60977.pdf`.

## Weiterverwendung der Originalplatine: belastbarer Arbeitsweg

Die folgende Reihenfolge ist ein aus Herstelleranschlussregeln und dem konkreten Sichtbefund abgeleiteter Arbeitsentwurf, kein bereits erprobter 2976-Kupferplan:

1. Originalzustand beidseitig fotografieren und jede Leitung an beiden Enden kennzeichnen. Relais, Platine, Motor, Schleifer, Radmasse und Front getrennt erfassen; unbekannte Anschlüsse zunächst neutral nummerieren.
2. Spannungsfrei die Verbindungen aufnehmen. Verbraucher und alte Elektronik können Durchgangs-/Widerstandsanzeigen verfälschen; ein vermeintlich gemeinsames Netz deshalb nicht allein aus einem Piepton ableiten. Prüfspitzen-Eigenwiderstand als Vergleich notieren.
3. Die alte aktive Analogelektrik einschließlich ihrer Motor-/Lichtverbindungen elektrisch aus dem neuen Netz entfernen. Wo zugänglich, dokumentierte Drahtanschlüsse oder Bauteilanschlüsse ablöten. Erst nach vollständiger Zuordnung beurteilen, ob eine Leiterbahntrennung überhaupt nötig ist. Keine Schnittposition aus dem kleinen Unterseitenfoto erfinden.
4. Die **vorhandene Originalplatine** mechanisch weiterverwenden. Nur eindeutig nachverfolgte, bauteilfreie und voneinander isolierte Kupfernetze als neue Löt-/Verteilerpunkte nutzen. Gewünschte Verbindungen durch Messung bestätigen; ungewollte Verbindungen einschließlich Befestigung/Chassis ausschließen. Die Karte muss vor Einbau des Decoders feststehen.
5. 60977 mit seiner vorgesehenen Schnittstelle isoliert montieren. HLA-Motorleitungen, Gleisanschlüsse und Lichtnetze gemäß neuer Netzliste anschließen. Ein dort nicht benötigter alter Kupferpfad bleibt elektrisch unbenutzt. Für Motor-/Schleiferströme keinen unbekannten dünnen Altpfad als ausreichend belastbar erklären; bei Bedarf nachvollziehbare isolierte Leitungsführung vorsehen und am erhaltenen Träger befestigen.
6. Erst danach stufenweise Inbetriebnahme mit der bereits bewährten Prüf-/Montagereihenfolge aus REV13. Ein fertiger Schaltplan muss elektrische Netze und originale Lötpunkte getrennt zeigen. Stromloser Durchgangstest und späterer Funktionstest sind unterschiedliche Nachweise.

## Welche LoDi-Abhängigkeiten zwingend neu geplant werden müssen

LoDi erklärt seine Motorplatine am Beispiel **33701** und platziert dort die LED-Vorwiderstände **R4/R5**; beim Einsatz alter Glühlampen werden diese gebrückt. Außerdem befinden sich dort 21MTC-Schnittstelle, Funktionsverteilung und je nach Revision Umschalt-/Jumperfunktionen. Ohne diese Platine stehen diese Bauteile und Funktionen nicht mehr zur Verfügung. Insbesondere ist das Weglassen ihrer Frontwiderstände **keine Erlaubnis**, einen eventuell weiterverwendeten LoDi-LED-Einsatz direkt an 60977 anzuschließen. Für die tatsächliche Frontrevision müssen Strombegrenzung und Rückleiter neu dokumentiert werden. Die ursprüngliche GE-/Kupplungsbeschaltung und SJ1/SJ2-Logik sind ebenfalls nicht automatisch auf der Märklin-Platine vorhanden. [LoDi Herstelleranleitung, Abschnitte Frontbeleuchtung und Motorplatinenanschluss](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/)

Offene, für die separate Anleitung entscheidende Auswahl: Entfällt nur die LoDi-Platine des motorisierten Kopfes oder auch die des hinteren Kopfes; bleiben LoDi-Fronten und LoDi-Wagenbeleuchtungen? Davon hängen Frontwiderstände, hintere Decoderaufnahme, Kupplungsnetze und Innenlichtschaltung ab. Diese Auswahl darf nicht stillschweigend getroffen werden.

## Benötigte Eingabe und aktueller Freigabestand

Für genaue Bilder mit Pfeilen und Lötpunkten fehlen eine scharfe Gesamtaufnahme der **Bauteilseite**, die passende **Lötseite** in gleicher Orientierung sowie Nahaufnahmen von Relaisanschlüssen, Platinenenden/Kupplungsanschlüssen und Frontfassungen. Die eigentliche Durchgangszuordnung ist am vollständig spannungsfreien Modell vorzunehmen. Das Umklappen der Platine muss ohne Zug auf angeschlossene Drähte möglich sein; das Foto allein ersetzt keine Messung.

**Fazit:** Grundweg und fehlende LoDi-Funktionen sind eingegrenzt; die separate Anleitung kann strukturell vorbereitet werden. Konkrete Trennstellen und ein endgültiges Lötbild bleiben bis zur originalen beidseitigen Zuordnung offen. Das ist eine präzise begrenzte Eingabelücke, kein technischer Beweis, dass der Erhalt der Originalplatine unmöglich wäre.
