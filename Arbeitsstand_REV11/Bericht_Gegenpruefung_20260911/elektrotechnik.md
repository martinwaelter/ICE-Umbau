# Forensische Gegenprüfung: Elektrotechnik und Messverfahren

Prüfdatum: 11.09.2026. Begrenzter Prüfauftrag: V-01, V-02, V-03 und V-09 bis V-16 des Berichts `ICE2976_REV11_Pruefbericht.md`. Bericht und Anleitung wurden nicht verändert. Dies ist eine Dokumentgegenprüfung, keine Hardwarefreigabe.

**Quellennachtrag 11.09.2026:** Die frühere Recherche zu V-12 war unvollständig. Die LoDi-ICE-M-Herstellerseite beschreibt unter „Einsetzen des Stützelko“ tatsächlich C1/C2, mindestens 100 µF bei 25 oder 35 V, empfiehlt 330 µF/25 V und nennt weiche Aufladung. Die frühere Aussage „Quelle nicht bestätigt“ ist hier korrigiert. Die bisherige Fassung liegt im REV12-Archiv. Der fachliche Bedarf an einem ausgelegten Entladeverfahren bleibt bestehen.

## Prüfbasis und Urteil

Die tatsächlich vorhandene REV11-PDF hat 40 Seiten und SHA-256 `3c67f596856f5403eac6f27f1f2512379555d3611749e4a7bd94f817cc7e41cb`. Die betroffenen PDF-Seiten wurden direkt extrahiert; die Seiten 28 und 30 sowie das originale Wagenfoto wurden zusätzlich visuell geprüft. Abgleich mit `Arbeitsstand_REV11/rev11_pages.json` sowie `Arbeitsstand_REV10/REV10_LESEFASSUNG.txt`, insbesondere 0a-3/0a-4, Kapitel 11 und Schritt 54. Primärquellen sind unten verlinkt; nicht auffindbare Angaben werden als unbestätigt behandelt.

**Der Bericht erkennt mehrere echte Lücken, ist aber kein unmittelbar ausführbarer Korrekturplan. Besonders V-01, V-02, V-03 und V-16 ersetzen berechtigte offene Voraussetzungen durch Verfahren, deren Aussagekraft nicht genügt. Die Ersatzfreigabe in V-16 ist technisch falsch.**

| ID | Diagnose im Bericht | Ersatztext |
|---|---|---|
| V-01 | Kern bestätigt; Aussagen über Nichtexistenz von Schaltplänen nicht bewiesen | Nicht übernehmen: Referenzvergleich wird zur absoluten Freigabe überdehnt |
| V-02 | Fehlende konkrete Messmethode bestätigt; pauschale Digitalstrom-Erklärung teilweise falsch | Nicht übernehmen: GFP3/1,5 A/kein Abschalten ersetzen keine Ausgangs- und Spitzenprüfung |
| V-03 | Kürzungsverlust bestätigt; Gefährdung an Anlagenbestand gebunden | Anlagenkarte sinnvoll; vorgeschlagene Ω-Signalprüfung und pauschales Umspeisen nicht übernehmen |
| V-09 | Fehlender eigener Erststrom des Gegenkopfes bestätigt | Sinnvoller Zusatz, aber Prüfgrenzen und Aussagekraft ergänzen |
| V-10 | Fehlende konkrete LED-Eingangsdaten und weggefallener U-max-Hinweis bestätigt | R4/R5 nur als zusätzliche Referenz; keine pauschale Übernahme/0,25-W-Freigabe |
| V-11 | Klärungsweg fehlt; Identifikation als Kappe bleibt Hypothese | Herstellerklärung mit Originalfotos sinnvoll |
| V-12 | Konkreter Restenergie-Handgriff fehlt; ICE-Elkoquelle im Nachtrag bestätigt | Entladeprinzip sinnvoll; feste Zeit/Spannung/1 kΩ ohne Auslegung nicht universell gültig |
| V-13 | „verlangt Umlöten“ und „nicht messbar“ nicht bestätigt | Kontaktisolation als mögliche Methode; neue Bestehenskriterien unzureichend |
| V-14 | Lokale Wiederholung nützlich; generelles Fehlen der Isolationsregel überzeichnet | Mit präziser Formulierung übernehmen |
| V-15 | Verweis-/Reihenfolgeunklarheit bestätigt; vorzeitige Freigabe nicht ausdrücklich erteilt | Phasen trennen; bloßes Verschieben nach S.37 kann neue Abhängigkeit erzeugen |
| V-16 | Bedingtes offenes Tor bestätigt; tatsächliche Unmöglichkeit am Fahrzeug nicht belegt | Verwerfen: Erststrom ist kein Ersatz für Motorisolation |

## V-01 – Bestückte Netze

**PDF-Befund:** S.5 verlangt einen bekannten Sollpfad, Messparameter und begründeten Soll-/Abbruchbereich. S.18 verlangt eine revisionsbezogene Ringnetzzuordnung. S.29 macht den vollständigen Elektronikplan samt Ergebnissen zur Voraussetzung. Das ist für einen Anfänger ohne tatsächliche Platinen- und Messgerätedaten nicht selbständig ausfüllbar. Diesen Ausführbarkeitsmangel trifft der Bericht. Die absolute Aussage „Einen LoDi- oder Märklin-Schaltplan gibt es nicht“ geht über die Recherche hinaus: nicht vorliegend/öffentlich nicht gefunden wäre belegt, Nichtexistenz nicht.

**Ungeeigneter Ersatz:** „Soll = Referenzwert (± Ablesestreuung)“ bestätigt nur eine unveränderte Anzeige unter den gewählten Bedingungen. Eine falsch bestückte oder bereits beschädigte Referenz bleibt falsch. Ausfall/Unterbrechung kann den Widerstand erhöhen; die Abbruchliste konzentriert sich auf sinkende Werte und OL→Zahl. Auch die Behauptung, Werksfehler fielen erst beim strombegrenzten Erststrom auf, ist kein vollständiges Fehlererkennungsversprechen: falsche Zuordnung, Unterbrechung oder erst unter Last wirksame Defekte können einen unauffälligen Erststrom haben.

Gleiches Messgerät plus Autorange plus fünf Sekunden definieren bei Halbleitern/Kondensatoren nicht automatisch denselben sicheren Arbeitspunkt. Bereichswechsel verändern den Prüfstrom; Prüfhistorie, Restladung und Temperatur wirken auf die Anzeige. Fluke beschreibt, dass die Widerstandsmessung alle parallelen Pfade erfasst und Halbleiterstrecken leitend machen kann; Keysight dokumentiert den bereichsabhängigen Prüfstrom. [Fluke 87/89, S.3-8](https://assets.fluke.com/manuals/87_89iv_umeng0200.pdf), [Keysight Low-Power-Ohm-Messung](https://docs.keysight.com/kkbopen/the-accuracy-specifications-to-low-power-resistance-measurements-using-34465a-34470a).

**Ringzuordnung:** Ein reproduzierbar sehr kleiner Wert gegen ein sicher bekanntes MASSE-Pad ist ein Indiz für eine Verbindung, aber ohne Zustands-/Pfadklärung kein alleiniger Nachweis zulässigen Schraubenkontakts. „Niedrig gegen anderes Pad = Signalnetz“ verwechselt Messverhalten mit Netzidentität; ein Widerstand oder Parallelpfad kann ebenso Ursache sein. Fehlende Quellenzuordnung wird dadurch nicht gelöst.

**Korrektur:** Vorher/Nachher als ergänzenden Änderungstest behalten. Für reine freigelegte Leiter konkrete Durchgangs-/Isolationstests vorgeben; bei bestückten Netzen nur nachgewiesene Pfade und gerätegeeignete Bedingungen verwenden. Unbekannte Ringrollen/LED-Zweige gezielt durch revisionspassende Herstellerangabe oder nachvollziehbare Leiterbahnzuordnung klären. Keine universelle Gut-Freigabe aus einer einmaligen Referenzreihe ableiten. P1 als Ausführbarkeitslücke vertretbar; Ersatz ist eine eigene wesentliche Prüflücke.

## V-02 – Digitalstrom und Lastfreigabe

**PDF-Befund:** S.28 zeigt eine allgemeine Reihenschaltung „QUELLE – A-METER – LAST“, ohne Gleis-/RT-Messpunkt oder DC-Bereich vorzuschreiben. Der Bericht macht daraus eine konkrete falsche Gleismessanweisung, die so nicht im PDF steht. Die Reihenschaltung ist grundsätzlich richtig; die fehlende Festlegung von Messpunkt, Messgröße, Bandbreite, Messbereich, Begrenzung und Abbruchgrenze ist das echte Problem. S.28 verlangt ausdrücklich getrennte Bewertung von Einzel-AUX, Licht/AUX-Summe und Gesamtstrom; die Behauptung, aus einem Gesamtstrom solle alles abgeleitet werden, trifft den Wortlaut nicht.

**Fachliche Überdehnung im Bericht:** Bipolar bedeutet nicht zwangsläufig gleichanteilsfrei. RCN-210 beschreibt DCC und erlaubt für Nullbits eine asymmetrische Verlängerung. Der konkrete Aufbau verwendet außerdem mfx/M4; ESU nennt M4- und Motorola-Pakete ausdrücklich asymmetrisch. Eine DC-Anzeige kann daher ungleich null sein und bleibt trotzdem ungeeignet, den thermischen Gesamtstrom verlässlich zu beurteilen. [RCN-210, Abschnitte 1.1 und 2.2](https://normen.railcommunity.de/RCN-210.pdf), [ESU LokPilot 5, S.29](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e).

Auch „mit einem Handmultimeter nicht messbar“ ist ohne Gerätetyp zu absolut. Normale Anzeigen verpassen schnelle Einschaltvorgänge; Geräte mit geeigneter schneller Spitzenwerterfassung können andere Fähigkeiten haben. True RMS allein genügt nicht: Bandbreite, Scheitelfaktor, AC-/DC-Kopplung und Auflösung müssen passen. [Fluke 1587-FC-Spezifikation](https://www.fluke.com/en-th/product/electrical-testing/insulation-testers/fluke-1587-fc) nennt beispielsweise nur 1 kHz AC-Bandbreite und zusätzliche Grenzen für nichtsinusförmige Signale.

**Ersatzprobleme:**

- CS3-GFP3 ist eine reale Betriebsstromanzeige. Das Handbuch nennt jedoch an dieser Stelle keine hinreichende Messgenauigkeit, zeitliche Spitzenauflösung oder Garantie der Zweigstromerfassung. Differenzen können die Lastbilanz ergänzen, aber keine feine Einzel-AUX-/Spitzenfreigabe ohne Unsicherheitsbetrachtung ersetzen.
- „Programmiergleis max. 1,5 A“ ist eine Ausgangsgrenze, kein nachgewiesener Schutz für 250-mA-Einzelausgänge, 300-mA-Summe oder unbekannte Kupplungsgrenzen. Das Abschaltverhalten/Zeitverhalten ist durch die Maximalangabe allein nicht spezifiziert. Ein Programmiergleis-Ersttest ist sinnvoll und von Märklin vorgesehen; die behauptete universelle Schutzwirkung folgt daraus nicht.
- „Einschaltspitze streichen; CS3 schaltet nicht ab“ reduziert den Prüfumfang statt das Messproblem zu lösen. Ein Ausgang kann über seinem zulässigen Bereich liegen, ohne die Gesamtstromabschaltung der Zentrale auszulösen. Decoder-Schutz kann zudem eine Last abwerfen, während die Zentrale eingeschaltet bleibt.
- GE muss nach tatsächlicher Schaltung bewertet werden. Ein geschalteter Rückpfad ist nicht automatisch glatter Gleichstrom, weil O/RT am Gleissignal hängt. Gleichgerichtete/pulsierende Ströme können einen brauchbaren DC-Mittelwert liefern, dieser ist aber kein Spitzen-/Effektivwertnachweis. Auch Messgeräte-Spannungsabfall und Eingangssicherung müssen passen.
- „Hintere LEDs aus gemessener Gleichspannung am +Ub“ braucht einen eindeutig benannten Gegenpunkt, Messzustand und den Spannungsabfall über dem tatsächlich relevanten Zweig. „Innenlicht-Differenz nahe 250 mA“ ist kein eindeutiger Abbruchwert und deckt die 300-mA-Summe nicht ab.

Quellen: [CS3-Handbuch, Anschlüsse und GFP3 auf S.33](https://www.maerklin.de/fileadmin/media/produkte/pdfs/MANUAL_CS3_DE-EN_17-02.pdf), lokal bereits vorhandenes Hersteller-PDF und Text geprüft; Live-Webabruf scheiterte. [60977-Beilage, technische Daten und Erstprüfung](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf).

**Korrektur:** Messkarte S.28 konkretisieren, Gesamtstromanzeige und Zweigstrommessung klar unterscheiden. Ausgangsgrenzen einschließlich Spitzen-/Überlastverhalten und niedrigerer Pfadgrenzen beibehalten. Erst nach Gerätetyp und realen Lastdaten eine konkret geeignete Mess-/Begrenzungsmethode festlegen. Keine Scheinlösung allein mit GFP3 und 1,5 A. P1 bleibt als Ausführbarkeitsmangel begründet, nicht als Nachweis einer bereits ausdrücklich angewiesenen DC-Gleismessung.

## V-03 – Anlagenbereich und Schleiferumschaltung

**Bestätigt:** REV10 0a-3 verlangte ausdrücklich den Abgleich der elektrischen Signalwirkung im Anschlussplan; 0a-4 dokumentierte den freigegebenen Bereich. REV11 S.6/S.39 enthalten die Überbrückungsverbote, aber keine gleichwertig konkrete Bestandskarte vor dem Fahrtest auf S.35. Der Variantenname ICE-M-S fehlt im Handlungsteil. Der Zusammenhang zur Herstellerbedingung ist belegt. [LoDi Motor-WiB ICE-M(-S)](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/).

**Einschränkung:** Fehlendes Relais ist visuelles Indiz; die tatsächliche SW–RT-Verbindung wird in REV11 S.16 ausdrücklich separat verlangt. Ohne eigenes Messprotokoll ist der tatsächliche Zustand nicht als gemessen bestätigt. Die vom Bericht aufgeführten Folgen sind mögliche Folgen bei einschlägiger Anlage, keine festgestellten Ereignisse.

**Ungeeigneter Ersatz:** Ω über zwei Mittelleiter bei angeschlossener Anlagen-/Brems-/Rückmeldeelektronik ist keine allgemeine Signaltypenprüfung. Parallelwege und Elektronik verfälschen das Ergebnis; elektronische Schalter verhalten sich spannungslos anders. Ein bistabiler oder elektronischer Signalantrieb lässt sich im stromlosen Zustand nicht notwendig wie angegeben umschalten. OL bei Rot und niederohmig bei Grün kann für einen vollständig isolierten mechanischen Kontakt passen, schließt aber andere zugbeeinflussende oder gespeiste Grenzen nicht aus. Primärmethodik: Anschlussplan und eindeutig zugeordnete Kabel/Module prüfen; Kontaktmessung nur am dafür spannungsfrei getrennten Kontaktkreis. [Fluke Widerstandsmessung](https://assets.fluke.com/manuals/87_89iv_umeng0200.pdf).

**Korrektur:** Die verlorene Bestands-/Bereichskarte vor dem ersten Fahrtest wiederherstellen. Unbekannte Bereiche gesperrt halten. „Abschnitt dauerhaft digital speisen“ ist eine Anlagenänderung, kein universeller Handgriff: insbesondere niemals Booster-/Programmiergrenzen schlicht überbrücken. ICE-M-S als alternative Architektur mit eigenem Anschluss-/Funktionsnachweis nennen; nicht als pauschale Lösung für alle Grenztypen verkaufen. P1 ist bedingt plausibel; keine P0-Freigabe-/Fehlanweisung im vorhandenen PDF festgestellt.

## V-09 – Gegenkopf-Erststrom

**Bestätigt:** S.33/1 ist vollständig stromlos; S.33/2 setzt sofort beide Köpfe auf ein Betriebsgleis. Ein eigener elektrischer Erststrom des eingebauten Gegenkopfes fehlt. REV10 Schritt54 verlangte tatsächlich „zuerst einzeln, dann gemeinsam“. Allerdings war dort auch motorloses Kommunikations-/Quittierungsverhalten problematisch; diese alte Forderung darf nicht blind wiederhergestellt werden.

**Überzeichnung:** „ungedrosselt bis 5 A“ unterschlägt S.33 VORHER („Laststufe zugelassen“) und die S.28-Voraussetzung einer festgelegten Begrenzung. Das Verfahren bleibt unkonkret, ist aber kein ausdrücklicher Auftrag zum unbeschränkten Bestromen.

**Ersatz:** Ein eigener kurzer Erststrom am geeigneten getrennten Programmiergleis ist sinnvoll. Er bestätigt zunächst Versorgung/auffällige Fehler, nicht alle Lichtzweige. GFP3 ohne Fehler und Geruch allein ist keine Isolations- oder LED-Stromfreigabe (siehe V-02). „Ohne Master reagiert F0 nicht“ zu „Im synchronisierten mfx-Betrieb ohne Master ist eine F0-Reaktion kein Bestehenskriterium“ präzisieren; nicht pauschal alle anderen Protokolle/gespeicherten Zustände ausschließen. Keine neue selbständige Anmeldung/Programmierung erzwingen. Danach gemeinsamer Lichttest. P2 plausibel.

## V-10 – Hintere LED-Widerstände

**Bestätigt:** S.17 verlangt reale LED-Daten und maximale Zweigspannung, liefert sie für die vorhandene 514 nicht. REV10 Kapitel11/Schritt29 benannte Netzteilkonfiguration, Spitzenwert am bestätigten Prüfaufbau und die Abgrenzung zu einem einfachen AC-Gleiswert konkreter. Die Formel ist korrekt, die Eingangsgrößen bleiben offen.

**Ersatz nur bedingt brauchbar:** R4/R5 des eigenen LoDi-Aufbaus können ein nützlicher Vergleich sein. Die Front-LED-Produktbeschreibung nennt keine vollständigen Grenzdaten; das Ablesen eines Widerstands ersetzt sie nicht. Vergleichbarkeit verlangt gleiche LED-Revision, korrekt zugeordneten Farbzweig, gleiche/topologisch entsprechende Beschaltung und mindestens ebenso konservative maximale Versorgung/Spannungstoleranz. „Mindestens derselbe Wert“ allein bestätigt keinen sicheren Strom im anderen Decoderaufbau. LoDi beschreibt R4/R5 als vorgesehene Vorwiderstände, keine universelle Transferregel auf Märklin-Träger + ESU. [LoDi Einbauanleitung](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/), [Front-Produktbeschreibung](https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/).

„≥ 0,25 W“ ist keine allgemeine Leistungsauslegung. Die spätere Formelkontrolle muss zwingend über diese Angabe gehen; Toleranz, Temperatur und Einbausituation bleiben relevant. Beispiel zur Widerlegung einer Universalregel, keine tatsächliche LED-Annahme: bei 20 V über 1 kΩ entstehen 0,4 W. Dass ESU einen allgemeinen Widerstandsbereich nennt, ist kein Datenblatt für jede 514-Revision.

**Korrektur:** Vorne abgelesene Werte/Zuordnung als Datenpunkt übernehmen, aber rear LED-Freigabe weiter an belegten Maximalstrom, Zweigaufbau, U-max und Verlustleistung binden. Herstelleranfrage sinnvoll, wenn die erforderlichen Daten fehlen. P2 Ausführbarkeitslücke; kein unbedingter R4/R5-Ersatz.

## V-11 – Schwarze Struktur

**Bildprüfung:** Die schwarze zentrale Fläche auf S.30 ist sichtbar. Ihre Funktion/Entfernbarkeit ist anhand dieses Fotos nicht sicher identifiziert. „Wahrscheinlich Bestückungskappe“ ist eine Hypothese, keine bestätigte Bauteilidentifikation. Die im Bericht und PDF beschriebene Steckrichtung passt zur Schnittstellenmechanik; daraus folgt aber noch keine sichere Entfernungsanweisung. [RCN-121](https://normen.railcommunity.de/RCN-121.pdf).

**Urteil/Korrektur:** Fehlenden konkreten Klärungsweg ergänzen: LoDi Herstellerkontakt, beidseitige Gesamtaufnahme, Makro von oben/seitlich, Revision und geplanten 60977 nennen; nach Bestückung, zulässiger Stecklage und gegebenenfalls Entfernung fragen. Herstellerkontakt ist mit „kein Händler verfügbar“ vereinbar. Die konkrete Herstellerantwort wurde nicht eingeholt. Der Ersatz hält die bestehende Sperre aufrecht und ist sinnvoll. P2 für reale Blockade möglich, Sachdiagnose „Kappe“ bleibt offen.

## V-12 – Restenergie

**Teilweise bestätigt:** REV11 S.3 verweist auf Bauteil-/Geräteanleitung; S.23 verlangt Erfassung vorhandener Speicher. Eine konkrete Entlademethode fehlt. Ist ein entsprechender Speicher tatsächlich eingebaut, muss dessen Entladung und Spannungsprüfung konkretisiert werden. Das vorhandene Wagenfoto zeigt nur eine Platinenansicht, keinen Nachweis aller Speicher.

**Quellenkorrektur:** Auf der [ICE-M-Herstellerseite](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-wib-ice-m/) steht unter „Einsetzen des Stützelko“: C1/C2, mindestens 100 µF bei 25 oder 35 V; empfohlen werden 330 µF/25 V, mit weicher Aufladung. Die frühere Nichtfund-Aussage war falsch. Die Übertragung auf das tatsächlich vorliegende Bauteil verlangt weiterhin die Revisions-/Bestückungszuordnung.

**Ersatz:** Entladen über geeigneten Widerstand mit isoliertem Anschluss und anschließender Spannungsprüfung ist fachlich sinnvoll. [Fluke Entladeprinzip](https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-measure-capacitance). Die exakten Zahlen 1 min, 0,5 V, 1 kΩ und 10 s sind jedoch nicht durch die genannten Bauteile/Messgeräte belegt. 0,5 V kann eine Widerstands-/Diodenmessung weiterhin deutlich beeinflussen. Bei unbekanntem C/Puffermodul bestätigt eine Wartezeit keine Entladung. Entladewiderstand benötigt Spannungs-/Impulsbelastbarkeit: bei 25 V und 1 kΩ beträgt die Anfangsleistung 0,625 W (Rechenbeispiel). Nachmessung ist erforderlich, auch auf Spannungswiederkehr achten. Nicht beliebige Speicher wie 60974 nach derselben Regel behandeln.

**Korrektur:** Nur für identifizierten Speicher konkrete Anschlusspunkte, R samt Belastbarkeit, Entladezeit und am Messverfahren orientiertes Restspannungskriterium festlegen. Keine pauschale Zusage für jede Platine. P2 nur bedingt bei vorhandenen Speichern.

## V-13 – Alleinige hintere Speisung

**Nicht bestätigt in dieser Form:** S.28/4 verlangt „stromlos trennen und einzeln isolieren“, nicht zwingend Ablöten an SW. Ein lösbarer Kontakt/Stecker oder andere dokumentierte Unterbrechung kann dies erfüllen. „Spannungseinbruch am bipolaren Signal nicht messbar“ ist ebenfalls falsch: geeignete Messgeräte/Referenzpunkte können ihn erfassen. Richtig ist nur, dass REV11 dafür kein konkretes Verfahren vorgibt.

**Ersatzprüfung:** Punktkontakte unter dem Motorkopf zu isolieren ist als reversible Methode grundsätzlich nachvollziehbar. Die Trennung muss sicher tatsächlich wirken und während des Versuchs stabil bleiben; keine Bewegung aus dem isolierten Bereich. „GFP3-Strom unverändert“ ist kein verlässliches Gutkriterium: ein höherer Serienwiderstand/Spannungsabfall kann bei Regelung/Laständerung den Strom verändern; geringe Unterschiede liegen eventuell unter Anzeigeauflösung. „Kein Flackern/Neustart“ erkennt nur grobe Funktionsfehler. Eine zehnminütige höchste Standlast enthält keinen fahrenden Motorstrom und beweist deshalb nicht die RT-Stromtragfähigkeit für Motorfahrt.

**Korrektur:** Den Befund in „Mess-/Trennverfahren unkonkret“ umbenennen. Reversible Schleiferisolation als konkret zu prüfende Möglichkeit nennen. Belastung muss den vorgesehenen realen Betrieb abdecken, einschließlich Motorlast ohne blockierten Rotor; Dauer, Temperatur-/Spannungsabfallgrenzen und Messmethode begründen. Standtest nicht zur vollen Fahrfreigabe aufblasen. P2 für fehlendes Verfahren vertretbar, die beiden Hauptbehauptungen sind nicht belegt.

## V-14 – Freie Kupplungskontakte

**Teilweise bestätigt:** S.32 fordert die Isolation der freien Motorkopf-Kupplungsenden ausdrücklich. S.29 verlangt schon für beide Köpfe einzeln isolierte unbenutzte Enden. S.33 wiederholt dies nicht ausdrücklich für RT des Gegenkopfes; S.34 nicht für das neu freie Ende beim schrittweisen Wagenaufbau. Der Bericht sollte das als lokale Präzisierung nach Zustandsänderung ausweisen, nicht als völliges Fehlen.

**Ersatz sinnvoll:** Vor jedem Einschalten alle gerade freien stromführenden Kupplungskontakte einzeln sicher abdecken/isolieren, beide Köpfe auseinander halten und metallische Fremdkörper entfernen. „Nie Metall auf dem Prüfgleis“ wörtlich ist ungenau, da Räder/Schleifer zwangsläufig Metall sind; „keine losen Metallteile/Werkzeuge an Gleis oder Kontakten“ trifft das Ziel. RT→GE-Brücke ist ein plausibler schädlicher Fehlerpfad. ESU warnt vor extern angelegter Spannung an Funktionsausgängen trotz Überlastschutz (LP5 S.28). P2/P3 je Formulierungsnähe; Zusatz ohne neue technische Architektur möglich.

## V-15 – Rückmeldetest

**Teilweise bestätigt:** S.26/6 sagt bereits ausdrücklich „Nach elektrischer Abnahme“. Ein sofortiger ungeprüfter Anlagenbetrieb wird nicht ausdrücklich freigegeben. Unklar ist, welche Abnahme gemeint ist und wie dieser spätere Test in den Ablauf eingeordnet wird.

**Ersatz hat Abhängigkeitsrisiko:** S.34 VORHER verlangt bei Radkontaktoption zusätzlich S.26; dessen WEITER umfasst auch „spätere Rückmeldung“. Wird die gesamte Karte erst nach S.37 bestanden, wäre S.34→S.37→S.26→S.34 eine neue Schleife. Nicht nur „Schritt 6 erst nach 37“ einfügen, sondern die Voraussetzungen präzise aufteilen: S.26/1–5 sind Montage-/Kontaktprüfung und vor S.34 erforderlich; S.26/6 ist gesonderte Meldefunktionsprüfung nach elektrischer Zugabnahme und Freigabe des betreffenden Anlagen-/Prüfbereichs. Ein vollständig isolierter, vorher passiv geprüfter Kontaktgleis-Meldetester kann auch ohne Zugbestromung geprüft werden; nicht alle Rückmeldetests brauchen physikalisch die komplette Endabnahme.

**Korrektur:** Zeitpunkt und zulässigen Bereich ausdrücklich verlinken, Eingangsvoraussetzungen/WEITER entsprechend teilen. P2 als Ablaufunklarheit plausibel; Berichtsaussage einer schon erteilten Erststromfreigabe ist zu stark.

## V-16 – Geschlossene Messung

**PDF-Befund:** S.36/3 lässt die geschlossene Messung bei fehlendem sicheren Leitungsaustritt offen; S.37 fordert sie bestanden. Das ist ein bedingtes Hindernis. Ob am tatsächlichen 2976 keine geeignete Öffnung/Prüfaufnahme möglich ist, ist nicht untersucht und nicht als Tatsache belegbar.

**Ersatz eindeutig verwerfen:** Externe Punkte Schleifer/Räder/RT/GE enthalten bei abgezogenem Decoder keinen vollständigen Zugang zu beiden Motoranschlüssen. Sie können den Motor-Metall-Pfad nicht gleichwertig prüfen. Erststrom am Programmiergleis ist ein Funktions-/Überlastversuch; ein unauffälliger Gesamtstrom beweist weder Isolation noch Freiheit von lageabhängigen Berührungen. Beispiel: ein hochohmiger unerwünschter Motor-Rahmen-Pfad kann weit unter jeder Zentralenabschaltung bleiben. Ein Kontakt kann nur bei bestimmter Motor-/Drehgestellbewegung auftreten. „Motorisolation geschlossen gilt über Erststrom ... als geprüft“ ist daher eine falsche Gut-Freigabe und widerspricht zusätzlich dem ausdrücklichen REV11 S.29-Hinweis, dass Leseerfolg keine Motorisolation bestätigt.

**Beleg/Herleitung:** ESU LP5 S.27 fordert potentialfreie Motoranschlüsse und eine separate Ohmmeterprüfung gegen Gleisanschlüsse; S.7 fordert Vermeidung gequetschter Kabel beim Zusammenbau. Die Folgerung, dass ein Funktionsversuch diese physikalisch andere Eigenschaft nicht beweist, ist elektrotechnische Ableitung, keine neue Herstellerbehauptung. [ESU LokPilot 5](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e).

**Korrektur:** Alternative sichere Messzugänglichkeit/Prüfaufnahme für M1/M2 und Metallbezug am realen Aufbau konkret entwickeln oder die betroffene Prüfung ehrlich offen lassen. Extern zugängliche Messungen als Teilnachweis benennen. Erststrom darf ergänzen, aber keine nicht durchgeführte Isolationsmessung als bestanden ersetzen. Der Ersatzfehler selbst ist mindestens P1 im vorgeschlagenen Korrekturplan.

## Empfohlene Verwendung dieses Gegenbefunds

Echte Lücken der REV11 priorisieren: konkrete Last-/Messmethode, Bestückungs-/LED-Daten, Anlagenkarte und separater Gegenkopf-Erststrom. Dabei keine unbekannten Werte durch pauschale Faustregeln schließen. V-01/V-02/V-03/V-16 als Ersatztexte sperren; V-10/V-12/V-13/V-15 mit den genannten Bedingungen neu formulieren. V-11 und V-14 können in präzisierter Form übernommen werden. Hardwarebesitz, Herstellerantworten und reale Messungen wurden nicht angenommen oder ausgeführt.
