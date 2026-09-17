# Prüfbericht ICE 2976 – REV11, korrigierte Fassung

**Stand: 11.09.2026.** Dieser Bericht ersetzt die fachlichen Bewertungen und Reparaturvorschläge des ursprünglichen Prüfberichts. Alle 33 Befundnummern bleiben nachvollziehbar erhalten. Grundlage ist die abgeschlossene [forensische Gegenprüfung](</Users/martinwaelter/ICE Umbau/ICE2976_REV11_Pruefbericht_GEGENPRUEFUNG.md>). Die hier bewertete REV11 wurde für diese Berichtskorrektur nicht verändert. Der Bericht sagt nichts über den Fertigstellungs- oder Prüfstatus einer nachfolgenden REV12 aus.

**Urteil:** REV11 enthält eine brauchbare, überwiegend schlüssige Auswahl von Bildern, Anschlüssen und Prüfsequenzen. Mehrere verpflichtende Prüfungen sind jedoch für einen Einsteiger noch nicht konkret genug ausführbar. Diese Lücken müssen geschlossen werden. Pauschale Referenzwerte, eine nicht abschaltende Zentrale oder ein erfolgreicher Einschaltversuch sind dafür keine allgemeinen Ersatznachweise.

## Prüfgegenstand und Methode

| Gegenstand | Festgestellte Identität |
|---|---|
| [REV11 Werkstattfassung](</Users/martinwaelter/ICE Umbau/output/pdf/ICE_2976_Umbauanleitung_REV11_WERKSTATTFASSUNG.pdf>) | 40 Seiten; SHA-256 `3c67f596856f5403eac6f27f1f2512379555d3611749e4a7bd94f817cc7e41cb` |
| [Originalprüfbericht](</Users/martinwaelter/ICE Umbau/ICE2976_REV11_Pruefbericht.md>) | SHA-256 `f817607b44f7c37ac91ad15840532d05f6ba98c1816615a2c37d01f4e82a83a6` |
| [Gegenprüfung mit V-12-Nachtrag](</Users/martinwaelter/ICE Umbau/ICE2976_REV11_Pruefbericht_GEGENPRUEFUNG.md>) | SHA-256 `1eaf68ed2804c8e88f1f2d83c4e01146019124c92369b29554d7e4ccafdf6af2` |
| [REV10, ursprüngliche Referenz](</Users/martinwaelter/ICE Umbau/ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf>) | 92 Seiten; SHA-256 `2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0` |

Die Gegenprüfung gleicht alle 33 Diagnosen und ihre vorgeschlagenen Behebungen getrennt gegen die tatsächlichen PDF-Seiten ab; Kürzungsvorwürfe werden zusätzlich an REV10 geprüft. Bildseiten und Herstellerzeichnungen wurden visuell kontrolliert. Die Angaben zu 40 Lesezeichen und 199 Verknüpfungen der REV11 sind bestätigt. Eine bestandene Layout- oder Linkprüfung belegt keine elektrische Funktionsfähigkeit.

Die im Originalbericht erwähnte Prüfung von 40 Zitaten ist ohne zugehörige Auswahl und Prüfdatei nicht vollständig reproduzierbar. Sie wird deshalb nicht als zusätzlicher unabhängiger Nachweis verwendet. Ebenso ist die Übereinstimmung mehrerer Modellprüfungen keine höhere Quellenkategorie.

**Evidenz:** H = Herstellerangabe; N = Norm; I = dokumentierte Softwareimplementierung; A = nachvollziehbare Ableitung; E = Erfahrungsbericht; O = am tatsächlichen Material offen. Eine Implementierung kann Registerbelegungen erklären, ohne damit die Funktion des konkreten Decoderpaares zu bestätigen. Fehlende persönliche Messwerte sind nicht automatisch Dokumentfehler; fehlende Handgriffe zu zwingend benötigten Werten sind dagegen eine Ausführungslücke.

**Prioritäten beziehen sich auf die Dokumentkorrektur:** P1 = betrifft einen zwingenden elektrischen Nachweis oder eine für die vorgesehene Nutzung erforderliche Anlagenbedingung; P2 = wesentliche Ablauf-, Konfigurations- oder Diagnosepräzisierung; P3 = lokale Verständlichkeit oder Quellenpflege. „O“ bezeichnet einen tatsächlichen Nachweisbedarf und darf nicht als bestanden gelten. „Kein bestätigter Fehler“ erhält keine Fehlerpriorität. Aus der Prüfung ergibt sich keine belegte P0-Anweisung; dies ist keine allgemeine Hardwarefreigabe.

## Vollständige Befundliste

### V-01 · P1 · Bestückte Netze: Prüfplan unvollständig

**Fundstelle:** S. 5, 18, 25–26, 29. **Befund bestätigt:** Der Einsteiger muss begründete Sollbereiche selbst festlegen, obwohl diese vor dem Erststrom verpflichtend sind. Dass generell kein Schaltplan existiert, ist nicht nachgewiesen.

**Korrektur:** Für jede tatsächliche Platinenrevision Messpunkte, Netzzuordnung, Geräteeinstellung, Polung und bauteilbezogene Aussage festlegen. Vorher-/Nachherwerte ergänzen diesen Nachweis. Sie ersetzen ihn nicht. Kein universelles „5 Sekunden, Autorange, Soll = Vorherwert“; „vorher OL, nachher Zahl“ beweist bei bestückten Schaltungen nicht allgemein einen Fehler. Ein niedriger Ring-Pad-Wert allein erlaubt keine Zuordnung des zulässigen Ringnetzes. [Fluke: Widerstandsmessung](https://assets.fluke.com/manuals/87_89iv_umeng0200.pdf)

### V-02 · P1 · Lastprüfung: Messverfahren und Begrenzung fehlen

**Fundstelle:** S. 28–29, 33–34. **Kern bestätigt:** Geeignete Messgeräte, konkrete Messstellen und eine passende Begrenzung für die jeweilige Last bleiben unbestimmt. „DC zeigt immer ungefähr null“ ist zu pauschal; die Karte ordnet diesen Bereich außerdem nicht ausdrücklich an.

**Korrektur:** Gesamtstrombeobachtung, Ausgangs-/Zweigstrommessung und Einschaltverhalten getrennt prüfen. Geräteeignung für Signalform und Messbereich muss belegt sein. Weder ein Ausgangsmaximum von 1,5 A noch „CS3 schaltet nicht ab“ bestätigt die kleineren Grenzen einzelner Decoder-Ausgänge, deren Summe oder der Kupplungen. RCN-216 trägt keine Lastmessung. [Märklin 60977](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf), [RCN-210](https://normen.railcommunity.de/RCN-210.pdf)

### V-03 · P1 · Anlagenaufnahme beim Kürzen entfallen

**Fundstelle:** S. 6, 35, 37, 39. **Bestätigt:** Die konkrete Aufnahme von Signal-, Brems-, Booster- und Versorgungsabschnitten sowie die ausdrückliche ICE-M-S-Bedingung fehlen. Das Verbot, Trennstellen mit der verbundenen RT-Leitung zu überbrücken, ist weiterhin vorhanden. Ob die eigene Anlage betroffen ist, bleibt offen.

**Korrektur:** Vor der Fahrt den vorgesehenen Anlagenbereich anhand tatsächlicher Verdrahtung und Modulunterlagen klassifizieren. Keine universelle Ohmprüfung über angeschlossene Elektronik. ICE-M-S oder eine geänderte Anlagensteuerung sind gesondert zu prüfende technische Entscheidungen. [LoDi Motor-WiB ICE-M](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/)

### V-04 · P2/O · Tatsächliche Prüfaufnahme konkretisieren

**Fundstelle:** S. 2, 6, 9, 11. **Bedingt berechtigt:** Bestand, Revision und Bedienkarte der Prüfaufnahme sind offen. Dass keine Aufnahme vorhanden ist, wurde nicht festgestellt. „Nicht vorsorglich kaufen“ verbietet keine begründete Beschaffung oder Leihe.

**Korrektur:** Für das tatsächlich eingesetzte Gerät 21MTC-Index, erforderliche Lasten, Ausgangsausführung und Anschlussfolge festlegen. Soundlast betrifft hier den 60977. Den 53900 nicht allein wegen seines Artikelnamens freigeben. [Märklin 60970](https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf), [ESU 53900-Anleitung](https://www.esu.eu/download/betriebsanleitungen/profi-pruefstand/?no_cache=1&tx_esudownloads_pi1%5BdownloadItem%5D=3e2cdb190091da48cc2030b2734bbd32)

### V-05 · P2 · Firmwarediagnose: Umfang und Unterbrechung klären

**Fundstelle:** S. 9–10, 29. **Widerspruchsvorwurf widerlegt:** Grundlesen und anschließend vorbereitete Indexschreibungen sind getrennte Arbeitskarten. Dokumentierte Indexwerte sind keine Probierwerte. Die Firmwareangabe hat einen Dokumentationsnutzen, auch ohne nachgewiesene Mindestversion für das Paar.

**Korrektur:** Pflicht oder optionale Diagnose konsistent festlegen und die Folgebedingungen entsprechend anpassen. Bei Abbruch den letzten bestätigten Indexzustand dokumentieren; keinen Erfolg erfinden. Eine nicht lesbare Firmware ist kein bestandener Kompatibilitätsnachweis. [JMRI Firmwaredefinition](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml)

### V-06 · P2 · Negativer Paartest braucht einen Diagnoseentscheid

**Fundstelle:** S. 11, 38. **Verbesserung bestätigt:** Nach einem gültigen negativen Test fehlt ein klarer nächster Diagnoseweg. Unbegrenztes blindes Wiederholen wird jedoch nicht vorgeschrieben.

**Korrektur:** Ergebnisse sichern und Ursache nach Versorgung, Identität, Konfiguration und Protokollbetrieb eingrenzen. Ein neuer Versuch braucht eine begründete Änderung oder neue Evidenz. Eine feste Zwei-Versuche-Regel ist unbegründet. Zugang zum LokProgrammer kann weitere Diagnose ermöglichen, garantiert aber keine Funktion dieses Decoderpaares. Ein Händler ist keine Voraussetzung.

### V-07 · P2/O · SID-Wechsel nicht hinreichend nachweisbar

**Fundstelle:** S. 11. **Bestätigt:** Die angebotene Mobile-Station-Folge belegt ohne weiteres Nachweismittel nicht die geforderte tatsächlich andere SID. Die CS3-Daten nach Rückkehr belegen keine SID während des Betriebs am anderen System.

**Korrektur:** Ein für das zweite System geeignetes SID-Nachweismittel benennen oder den Test ausdrücklich auf „Betrieb nach Neuanmeldung am zweiten System“ begrenzen. Alle Abnahmekriterien müssen denselben tatsächlich belegten Umfang verwenden. [Märklin CAN-Protokoll: Bind/Verify](https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf)

### V-08 · P2 · Datenformat und Datenweg sauber trennen

**Fundstelle:** S. 7. **Teilweise bestätigt:** CS2-Textformat und CS3-JSON sowie der Beleg für den direkten HTTP-Pfad sind nicht sauber getrennt. Ein grundsätzlich falsches Feld `address` ist nicht bewiesen.

**Korrektur:** Primär eine Sicherungskopie verwenden. Im CS2-Textformat lautet das Feld `.adresse`, in CS3-JSON `address`. Den direkten Dateipfad nur als am eigenen Gerät zu bestätigenden Lesekandidaten behandeln. Rohkennung, Bedienobjekt-ID, SID und Adresse nicht verwechseln. [TrainControl Dateiverarbeitung](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/src/org/traincontrol/marklin/file/CS2File.java)

### V-09 · P1 · Gegenkopf-Einzel-Erststrom fehlt

**Fundstelle:** S. 28, 33. **Bestätigt:** Der eingebaute Gegenkopf hat keinen eigenen tatsächlichen Erststromschritt. Die Beschreibung „ungedrosselt bis 5 A“ war überzogen, weil S. 28 eine Begrenzung voraussetzt.

**Korrektur:** Den Gegenkopf vor dem gemeinsamen Test einzeln mit geeignetem begrenztem Prüfaufbau und gesicherten freien Kontakten prüfen. Das Programmiergleis allein löst die Mess- und Begrenzungsfrage nicht. Fehlende F0-Reaktion ohne Master ist bei synchronisiertem Slave kein selbständiger Fehlernachweis.

### V-10 · P1/O · Hintere LED-Widerstände brauchen einen Eigenweg

**Fundstelle:** S. 17, 29. **Kern bestätigt:** Für die hinteren LED-Zweige fehlt ein vollständiger Weg zur Bestimmung passender Widerstände. Auch REV10 überließ einen Teil der Ermittlung einem Prüfenden.

**Korrektur:** Tatsächliche Zweigstruktur, maximale vorgesehene Betriebsspannung, LED-Spannung und zulässiger Zielstrom feststellen; daraus Widerstand und Verlustleistung bestimmen. R4/R5 sind Hinweise zur Identifikation, kein allgemeiner Ersatznachweis. „Mindestens gleicher Widerstand, mindestens 0,25 W“ ist ohne diese Daten keine Freigabe.

### V-11 · P2/O · Schwarze Struktur und Stecklage offen

**Fundstelle:** S. 16, 30. **Tatsächlicher Detailnachweis offen:** Die Struktur ist nicht abschließend identifiziert. Eine Bestückungskappe ist lediglich eine Hypothese.

**Korrektur:** Makrofotos von oben und seitlich, Platinenrevision und Maße der Steckverbindung zusammenführen; erforderlichenfalls präzise beim Hersteller nachfragen. Keine Anweisung zum Entfernen einer vermeintlichen Kappe, solange Identität und Zweck nicht feststehen.

### V-12 · P1/O · Restenergiefreiheit nicht konkretisiert

**Fundstelle:** S. 3–5, 23, 29, 36. **Kern bestätigt:** Ein ausführbarer Ablauf für die tatsächlich verbauten Speicher fehlt. **Korrektur auch gegenüber der ersten Gegenprüfung:** Die allgemeine LoDi-WiB-ICE-M-Herstellerseite nennt C1/C2, empfiehlt 330 µF/25 V und beschreibt eine Ladeschaltung. Diese Quellenangaben sind bestätigt; die tatsächliche Revision und Bestückung des eigenen Wagens bleiben zu identifizieren. [LoDi: Einsetzen eines Stützelkos](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-wib-ice-m/)

**Korrektur:** Vorhandene Speicher identifizieren; zugängliche Messpunkte, zulässige Messbedingungen und gegebenenfalls passende Entladebauteile festlegen. Ein universelles Rezept mit Wartezeit, 1 kΩ, zehn Sekunden oder 0,5 V darf nicht ohne Bauteil-/Gerätebezug als Nachweis gelten. Kein Drahtkurzschluss zum Entladen.

### V-13 · P2 · Prüfung alleiniger hinterer Einspeisung präzisieren

**Fundstelle:** S. 28. **Teilweise widerlegt:** REV11 verlangt stromloses Trennen, nicht zwingend Ablöten. Ein Spannungseinbruch kann mit einem geeigneten Verfahren gemessen werden.

**Korrektur:** Eine praktikable Trennstelle benennen. Eine mechanische Unterbrechung der vorderen Schleiferzufuhr ist nur dann geeignet, wenn andere Einspeisungen ausgeschlossen und der Aufbau eindeutig sind. Flackerfreiheit, unveränderte Gesamtstromanzeige oder zehn Minuten Standlast beweisen nicht allein die maximale RT-Tragfähigkeit im Fahrbetrieb.

### V-14 · P2 · Freie Kontakte bei jedem Ausbauzustand sichern

**Fundstelle:** S. 29, 32–34. **Lokale Präzisierung bestätigt:** Beide Köpfe sind auf S. 29 bereits berücksichtigt. Das freie Ende des jeweils letzten Wagens ist bei späteren Teststufen weniger deutlich benannt.

**Korrektur:** Unmittelbar vor jedem Einschalten freie Kontakte beider Köpfe und des letzten Wagens einzeln sichern. Die übergreifende Isolationsregel beibehalten; nicht behaupten, sie habe vollständig gefehlt.

### V-15 · P2 · Radkontaktprüfung und Rückmeldetest entflechten

**Fundstelle:** S. 26, 34, 37. **Ablaufunschärfe bestätigt:** „Nach elektrischer Abnahme“ steht bereits auf S. 26. Vorzeitige Bestromung wird nicht ausdrücklich erlaubt. Ein bloßes Verschieben hinter S. 37 erzeugte aber eine Abhängigkeit zurück zu S. 34.

**Korrektur:** Stromlose Montage-/Anschlussprüfung auf S. 26 von einem späteren bestromten Rückmeldetest trennen. S. 34 darf nur die vorher ausführbaren Prüfungen voraussetzen. Den Funktionstest dem bereits elektrisch geprüften Zug und einem geeignet bestätigten Anlagenbereich zuordnen.

### V-16 · P1/O · Geschlossene Motorisolation braucht passenden Zugang

**Fundstelle:** S. 36–37. **Bedingtes Ausführungsproblem bestätigt:** Ohne sicheren Leitungsaustritt bleibt die geforderte Prüfung offen. Dass dies beim tatsächlichen Gehäuse unvermeidbar ist, steht nicht fest.

**Korrektur:** Zugängliche Messpunkte müssen den tatsächlichen Motorpfad gegen den Rahmen erfassen, ohne ihn für die Prüfung elektrisch zu verändern. Ein geeignetes gleichwertiges Verfahren ist möglich, aber nachzuweisen. **Ein Einschaltversuch ersetzt keine Isolationsprüfung.** Außenmesspunkte an Schleifer, Rädern und Kupplung allein decken den Motorpfad nicht ab. [ESU LokPilot 5, Motoranschluss](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e)

### V-17 · P3 · Frühe Selbstanmeldung dokumentieren

**Fundstelle:** S. 9, 11. **Kleiner Kürzungsverlust bestätigt:** Frühes Loklistenfoto und Hinweis zur Selbstanmeldung fehlen lokal; alte Slave-Einträge werden auf S. 11 weiterhin behandelt.

**Korrektur:** Vor dem ersten Aktivieren die Lokliste sichern. Eine mögliche selbständige M4-Anmeldung dokumentieren und vom DCC-Serviceeintrag unterscheiden. Den Eintrag beim Paartest gezielt vergleichen.

### V-18 · P2 · Abbruch und Konfigurationsverbot an den Paartest setzen

**Fundstelle:** S. 11, 27, 38. **Lokale Lücke bestätigt:** Übergreifende Regeln bestehen, sind beim Vorabtest aber nicht vollständig wiederholt.

**Korrektur:** Bei Überlastanzeige, Geruch oder unerwartetem Motorlauf abschalten. Während des verbundenen Paartests keine Decoderkonfiguration bearbeiten, auch nicht am mfx-Mastereintrag. Diagnose und Schreiben auf die getrennte Prüfaufnahme zurückführen.

### V-19 · P2 · Decoderadressen getrennt von Bedienobjekten erfassen

**Fundstelle:** S. 9–10. **Dokumentationsverlust bestätigt:** Tatsächliche DCC-/MM-Adressen und aktive Protokolle werden nicht systematisch erfasst.

**Korrektur:** Decoderwerte und CS3-Serviceeinträge getrennt dokumentieren. Eine freie Adresse im Bedienobjekt ändert nicht automatisch den Decoder. DCC-/MM-Gleichlauf darf nicht als mfx-Folgen gewertet werden. Den vorgesehenen DCC-Wartungsweg des 59649 erhalten.

### V-20 · P3 · CV51 Bit 4 praktisch erklären

**Fundstelle:** S. 27. **Verständlichkeitslücke bestätigt:** REV11 verlangt die Erkennung des gesetzten Bits, erklärt sie aber nicht praktisch.

**Korrektur:** Nur wenn AUX4 tatsächlich benötigt wird und die dokumentierte CV51-Ausführung passt: 0–15 unverändert lassen; bei 16–31 genau 16 abziehen; andere Werte vor Änderung klären. Andere Bits erhalten, Ergebnis rücklesen. [Märklin CV-Tabelle](https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf)

### V-21 · P3 · ESU-Einmessfahrt ausdrücklich ausschließen

**Fundstelle:** S. 9–10. **Kleiner Kürzungsverlust bestätigt:** Der konkrete Auslöser fehlt.

**Korrektur:** Den Hinweis ergänzen, keine ESU-Einmessfahrt durchzuführen: nicht CV54 = 0 mit anschließendem F1 auslösen. Die Grundregel „keine Einmessfahrt“ bleibt bestehen.

### V-22 · P3 · Puffer-Firmwareverweis lokal ergänzen

**Fundstelle:** S. 39. **Teilweise bestätigt:** Ein Verweis auf den bereits erhobenen Firmwarewert ist sinnvoll. Die Ein-Puffer-Regel steht bereits ausdrücklich dort.

**Korrektur:** Den Lesebeleg von S. 7 heranziehen und CV7 nicht beschreiben. Die vorhandene Ein-Puffer-Regel erhalten; sie nicht als verlorene Schutzregel zählen. [Märklin 60974](https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf)

### V-23 · Optionale Verbesserung · Motoralternative über CV51 Bit 0

**Fundstelle:** S. 32. **Fehlervorwurf überzeichnet:** REV11 verbietet spontane Invertierung, nicht jede begründete spätere Korrektur. Mechanische Motorzuordnung ist keine falsche Anweisung.

**Korrektur:** Die herstellerseitig dokumentierte Bit-0-Alternative kann mit Erhalt aller anderen Bits und erneuter Richtungs-/Lichtprüfung ergänzt werden. CV29-Richtungsinversion nicht als gleichartige Änderung darstellen. [Märklin CV-Tabelle](https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf)

### V-24 · P2/O · Lautsprecherherkunft und Adapter konkretisieren

**Fundstelle:** S. 20. **Teilweise bestätigt:** Satzherkunft, Eignung und zusätzlicher Impedanzbeleg werden nicht klar zusammengeführt. Foto-/Maßaufnahme zur Steckerklärung ist bereits vorgesehen.

**Korrektur:** Tatsächlich verwendeten Satzlautsprecher beziehungsweise belegten Ersatz und mechanisch passenden Adapter eindeutig zuordnen. Ein grundsätzlich für Laien unbestimmbarer Stecker ist nicht nachgewiesen. Umlöten an empfindlichen Lautsprecheranschlüssen bleibt eine zusätzlich zu bewertende Option, kein risikofreier Standardersatz.

### V-25 · P3 · Standardmotorschild vom Sonderfall unterscheiden

**Fundstelle:** S. 13. **Präzisierung sinnvoll:** Motor-Rahmen-Kondensatoren und Querkondensator sind bereits unterschieden; eine falsche Zuordnung ist nicht belegt.

**Korrektur:** Das unveränderte passende Motorschild als Standardfall beschreiben und Fremdbestückungen ausdrücklich identifizieren lassen. Keine beliebige nF-Vergleichsmessung ohne geeignete Messbedingungen und Sollkriterium als Freigabe ergänzen. [ESU LokPilot 5](https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e)

### V-26 · P3 · Verschmutzung in die Fehlerdiagnose zurücknehmen

**Fundstelle:** S. 15, 38; Vergleich REV10 S. 23. **Kleiner Kürzungsverlust bestätigt:** Kohlestaub und Metallspäne fehlen als ausdrückliche Fehlerursachen.

**Korrektur:** Bei unerwartetem Motor-Rahmen-Pfad auch diese Ursachen prüfen; geeignet reinigen, vollständig trocknen und die vollständige Messfolge wiederholen.

### V-27 · Offene Bedienfrage · Zwischenwertschreiben nicht belegt

**Fundstelle:** S. 9–10. **Kein bestätigter UI-Fehler:** Dass Pfeile oder Regler unerwünschte Zwischenwerte schreiben, wurde nicht am tatsächlichen Versionsstand nachgewiesen. CV8 ist bereits ausschließlich zum Lesen vorgesehen.

**Korrektur:** Zifferneingabe und getrennte Leseliste können den Ablauf eindeutiger machen. Eine konkrete Fehlfunktion erst nach reproduzierbarer Beobachtung behaupten. Das bestehende Schreibverbot für CV8 erhalten.

### V-28 · P3 · Quellenbehauptung berichtigen

**Fundstelle:** S. 9–10. **Hauptvorwurf widerlegt:** „Decoder auslesen“ steht auf PDF-Seite 12 des als Q9 verlinkten Changelogs. Fehlerprüfung je Zeile und Bildschirmdokumentation sind in REV11 bereits vorhanden.

**Korrektur:** Falls der historische Name „Prog.“ verwendet wird, die zusätzliche offizielle CV-Editor-Hilfe zitieren. Kein fehlendes Menü oder fehlendes Fehlerprüfverfahren behaupten. [CS3-Changelog 2.6.0](https://www.maerklin.de/fileadmin/media/service/cs3/Maerklin_CS3_v2.6.0_changelog.pdf), [CV-Editor-Hilfe](https://www.maerklin.de/fileadmin/media/clubs/downloads/Loks_CV_Editor.pdf)

### V-29 · O · Eigener Softwareexport noch auszuführen

**Fundstelle:** S. 8. **Kein bestätigter Dokumentfehler:** ESU beschreibt die Funktion ab Version 4.4.0, nicht ausschließlich für diese Version. Der eigene Softwarelauf ist in REV11 bereits vorgeschrieben.

**Maßnahme:** Den vorgesehenen Aus-/An-/Aus-Vergleich mit realer LokProgrammer-Software ausführen und sichern. Ein fehlendes eigenes Bildschirmfoto begründet keinen vorsorglichen Hardwarekauf. [ESU: geänderte CVs anzeigen](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/)

### V-30 · P3 · Ableitungen und Primärbelege richtig zuordnen

**Fundstelle:** S. 6, 8, 28. **Quellenpräzisierung bestätigt:** Die JMRI-Verarbeitung und konkrete 53900-Anleitung fehlen als direkte Zusatzbelege. RCN-216 trägt Serviceprogrammierung und Quittierung, keine Laststufenmessung.

**Korrektur:** Die Zahlenformel als Implementierungsableitung mit Bytezuordnung und Verarbeitung belegen; die 0,5-W-Angabe der konkreten 53900-Anleitung zuordnen. V-02 erfordert weiterhin eine Messmethodik und ist nicht durch eine Fußnote erledigt. [JMRI SplitVariableValue](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/jmrit/symbolicprog/SplitVariableValue.java), [RCN-216](https://normen.railcommunity.de/RCN-216.pdf)

### V-31 · P2/O · Motorbauart am eigenen Fahrzeug identifizieren

**Fundstelle:** S. 2, 12. **Explizite Zuordnung fehlt:** Der 60941 ist dem passenden Trommelkollektormotor zuzuordnen. Ein tatsächlich ungeeigneter Motor wurde nicht festgestellt.

**Korrektur:** Eigenes Motorbild und Satzzuordnung vor Montage dokumentieren. Die 60941-Beilage ist als Bild-PDF visuell prüfbar; fehlende Textauslesbarkeit ist kein Grund, sie für unprüfbar zu erklären. [Märklin 60941](https://www.marklin.com/products/details/article/60941), [60941/60943-Originalzeichnung](https://static.maerklin.de/damcontent/e3/bb/e3bb202fe80385cc96835d783af5e1821670919973.pdf)

### V-32 · Optionale Präzisierung · Zweck der B-Litze

**Fundstelle:** S. 26. **Kein bestätigter Belegungsfehler:** REV11 beschreibt B als optionale örtliche Radmasse, nicht als Voraussetzung jeder Kontaktgleismeldung. Leitende Radsätze können ein geeignetes Kontaktgleis bereits selbst überbrücken.

**Korrektur:** Radsatzart, Rückmelderprinzip und Zweck der zusätzlichen Litze unterscheiden. Weder eine pauschale B-Pflicht für Kontaktgleise noch eine pauschale Eignung für alle Stromfühler behaupten. [Märklin Kontaktgleise](https://static.maerklin.de/damcontent/39/ed/39edd7421aab46bad800327e21f8b51a1738043640.pdf)

### V-33 · P2/O · Revisionspassenden GE-Pfad belegen

**Fundstelle:** S. 16. **Teilweise Detailoffenheit:** Eine revisionspassende Herstellerzuordnung ist bereits verlangt; ein konkreter persönlicher Nachweis fehlt noch.

**Korrektur:** Platinenrevision und Gesamt-/Detailfotos mit einer klaren Frage zur Zuordnung GE–AUX4 beziehungsweise zur tatsächlich vorhandenen Ausführung verbinden. Ein eindeutiger Herstellerbeleg kann genügen; Messungen an engen 21MTC-Pins sind nicht zwingend die einzige Methode. Die Zuordnung nicht aus einer ähnlichen Fotoversion übertragen.

## Korrigierte Umsetzungsreihenfolge

1. **Elektrische Pflichtnachweise ausarbeiten:** bestückte Netze, Lastmessung und geeignete Begrenzung, LED-Zweige, Restenergie, Gegenkopf-Einzel-Erststrom und geschlossene Motorisolation. Wo reale Bauteildaten benötigt werden, muss der Weg zu diesen Daten konkret beschrieben sein. Eine unbekannte Eigenschaft darf durch Textänderung nicht zu einer bestandenen Prüfung werden.
2. **Arbeitsfolge schließen:** tatsächliche Prüfaufnahme festlegen, Anlagenbereich vor Fahrt aufnehmen, Radkontakt-Montageprüfung vom Rückmeldetest trennen. Paartest und SID-Nachweis müssen genau den belegten Funktionsumfang abnehmen.
3. **Bedienung und Quellen schärfen:** Diagnoseweg bei negativem Paartest, eindeutige Datenformate, lokale Abschaltregeln, reale Decoderadressen, CV51-Fallunterscheidung und Einmesssperren ergänzen. Die widerlegten Vorwürfe sind keine zusätzlichen Bauaufgaben.

Der überarbeitete Ablauf soll die vorhandenen guten Originalbilder, Herstellerzeichnungen, Motor-Sechserfolge, Kontaktproben, Kreuzpfadprüfungen, T1–T9 und Wiederanschlusskontrollen erhalten. Die bestätigten Ergänzungen verlangen keine Rückkehr zur 92-seitigen Darstellung.

## Stand des tatsächlichen Umbaus und Nachweisgrenzen

Die Funktion des konkreten Märklin-60977/ESU-59649-Paares über den vorgesehenen Eigenweg ist weiter am vorhandenen Material zu belegen. Ebenso offen sind persönliche Geräteausführung und Softwarestand, bestimmte Platinen-/Steckdetails, LED-Daten, Motorbauart, Messwerte und der Anlagenbereich. Diese Angaben wurden im Rahmen der Berichtskorrektur weder gemessen noch programmiert.

Für erforderliche Herstellerklärungen kommt ein direkter Herstellerkontakt infrage; der nicht verfügbare Händlerweg wird nicht wieder zur Voraussetzung gemacht. Eine Herstellerantwort wird nicht vorweggenommen. Tatsächliche Bauteilklärung, Softwarediagnose und ein Anlagenumbau sind jeweils eigene Handlungen; die bloße Erwähnung im Bericht bestätigt ihre Durchführung nicht.

Die fachlichen Quellen oben stammen aus der abgeschlossenen Gegenprüfung; die LoDi-Angaben zu V-12 wurden am 11.09.2026 zusätzlich direkt auf der Herstellerseite nachgeprüft und berichtigt. Bei zuvor nicht frisch abrufbaren Herstellerseiten wurden in der Gegenprüfung bereits vorhandene Originaldateien mit Herkunftsnachweis herangezogen. Für diese übrigen Quellen behauptet der Korrekturlauf keinen neuen Webabruf. Ausführliche Fundstellen stehen in den Nachweisunterlagen [Elektrik](</Users/martinwaelter/ICE Umbau/Arbeitsstand_REV11/Bericht_Gegenpruefung_20260911/elektrotechnik.md>), [Programmierung](</Users/martinwaelter/ICE Umbau/Arbeitsstand_REV11/Bericht_Gegenpruefung_20260911/programmierung.md>) und [Redaktion/Kürzung](</Users/martinwaelter/ICE Umbau/Arbeitsstand_REV11/Bericht_Gegenpruefung_20260911/redaktion.md>). Bei abweichender Bewertung zu V-12 gilt die hier dokumentierte ergänzende Primärquellenprüfung.

**Abschlussbewertung:** Der Prüfbericht ist fachlich bereinigt. Seine berechtigten Ausführungslücken bleiben erhalten; widerlegte Diagnosen, unbegründete Zahlenrezepte und ungleichwertige Ersatzprüfungen sind korrigiert. Der nächste Umsetzungsschritt ist die gezielte Behebung dieser Lücken in der Anleitung. Dieser Bericht bewertet ausschließlich die oben eindeutig identifizierte REV11 und ist keine Abnahme einer späteren Fassung.
