"""Gezielte REV10-Korrekturen: Programmierung, Identität und G0.

Dieses Modul verändert ausschließlich die von Root zugewiesenen Abschnitte.
Es erzeugt keine Hardwarefreigabe und enthält keine individuelle CV-Zielkarte.
"""


def _paragraphs(value):
    if isinstance(value, dict):
        if value.get("type") == "p":
            yield value
        for key, child in value.items():
            if key != "text":
                yield from _paragraphs(child)
    elif isinstance(value, list):
        for child in value:
            yield from _paragraphs(child)


def _get(sections, title):
    matches = [s for s in sections if s["title"] == title]
    if len(matches) != 1:
        raise ValueError(f"Abschnitt nicht eindeutig: {title!r} ({len(matches)})")
    return matches[0]


def _replace(section, old, new, count=1):
    found = sum(p["text"].count(old) for p in _paragraphs(section))
    if found != count:
        raise ValueError(f"REV9-Anker in {section['title']!r}: {old!r}: {found} statt {count}")
    for p in _paragraphs(section):
        p["text"] = p["text"].replace(old, new)


def _p(text, style="body"):
    return {"type": "p", "style": style, "text": text}


def _table(headers, rows, weights):
    widths = [round(511.28 * w / sum(weights), 2) for w in weights]
    widths[-1] = round(511.28 - sum(widths[:-1]), 2)
    return {"type": "table", "widths": widths,
            "rows": [[_p(x, "head") for x in headers]] +
                    [[_p(x, "cell") for x in row] for row in rows]}


def _append(section, *elements):
    section["elements"].extend(elements)


def _insert_after(sections, prior, title, elements):
    if any(s["title"] == title for s in sections):
        raise ValueError(f"Ergänzung bereits vorhanden: {title}")
    index = sections.index(prior)
    sections.insert(index + 1, {"title": title, "elements": list(elements)})


MS_MANUAL = "https://static.maerklin.de/damcontent/2a/47/2a470bed20017f68f92306725d49fca81702905959.pdf"
MARKLIN_MANUAL = "https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf"
JMRI_INFO = "https://raw.githubusercontent.com/JMRI/JMRI/master/xml/decoders/esu/v4decoderInfoCVs.xml"
JMRI_V5 = "https://raw.githubusercontent.com/JMRI/JMRI/refs/heads/master/xml/decoders/esu/v5standardCVs.xml"
ESU_EXPORT = "https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/"


def apply(sections):
    """Mutiert die zugewiesenen Abschnitte und liefert dieselbe Liste zurück."""
    a = _get(sections, "A. Decoder-Nachweis: Ausstattung und Grenzen")
    _replace(a,
             "Dem Prüfenden beide Artikelnummern geben. Er muss je Aufnahme Steckschnittstelle, Motor und Lautsprecherlast benennen und die Eignung für genau diesen Decoder bestätigen; keinen ungeprüften Prüfstand kaufen.",
             "Dem Prüfenden die Artikel 60977 und 59649 nennen. Je Aufnahme Schnittstelle, tatsächlich angeschlossene Lasten und sichere Eignung bestätigen lassen. Für den 59649 ist damit weder ein Motor noch ein Lautsprecher als Pflichtlast festgelegt. DCC-Quittierung im konkreten Aufbau separat nach F.4/F.10 nachweisen; keinen ungeprüften Prüfstand kaufen.")
    _replace(a, "Nur eine CS3 speist die Gleiseingänge;",
             "Für C2-C6 speist allein die CS3 die Gleiseingänge; für C7 darf erst nach vollständiger Trennung ein bestätigter eigenständiger Aufbau mit vorhandener Mobile Station/Gleisbox übernehmen. Nie zwei Gleisausgänge verbinden;")
    _append(a,
        _p("Weitere bereits vorhandene Geräte – kein vorsorglicher Neukauf", "h2"),
        _table(["Anzahl / Artikel", "Bestand", "Konkrete Verwendung / noch zu erfassen"], [
            ["1 Gleisanschlussbox; Artikelnummer offen", "Vorhanden laut Nutzer", "Typenschild, passendes Netzteil und Kompatibilität zur kabelgebundenen MS erfassen. Kandidat für den eigenständigen C7-Aufbau; noch keine Anschlussfreigabe."],
            ["1 kabelgebundene Mobile Station; Artikelnummer offen", "Vorhanden laut Nutzer", "Generation, Artikelnummer, Software und bisherige Anmeldung des 60977 dokumentieren. Mit passender Gleisbox eventuell für C7 verwendbar."],
            ["1 Mobile Station WLAN; Artikelnummer offen", "Vorhanden laut Nutzer", "Verbindung zur steuernden Zentrale dokumentieren. Ein weiteres Bediengerät an derselben Zentrale erzeugt keinen unabhängigen mfx-Adressgeber."],
        ], [1.1, .65, 2.25]),
        _p("Die G0-Prüfaufnahme und der später motorlos eingebaute 59649 sind zwei verschiedene Aufbauten. Ein erfolgreicher Leseversuch in einer motorbestückten Prüfaufnahme beweist nicht die Quittierfähigkeit des späteren motorlosen Kopfes. Vor dessen Nachprogrammierung F.4/F.10 für genau diesen Aufbau erneut nachweisen. Einen Motor oder Lastwiderstand nicht versuchsweise an den Decoder hängen."))

    b = _get(sections, "B. Identität und Sonderoption belegen")
    _replace(b, "B4 darf nur getrennt auslesen.",
             "B4 darf nur getrennt und nach bestätigtem Leseweg gemäß F.4 auslesen.")
    _replace(b, "CS3: F.4 zuerst nur lesen, Altwerte sichern;",
             "CS3: erst Prüfaufnahme und Bedienweg in F.4 bestätigen, dann ausschließlich lesen und Altwerte sichern;")
    _append(b,
        _p("B6. Vorzustand der Anmeldungen festhalten", "h2"),
        _p("Vor dem ersten ESU-Einlesen die CS3-Lokliste sichern bzw. fotografieren. Ein noch nicht synchronisierter M4-Decoder kann zunächst selbstständig angemeldet sein; diese Vorab-Anmeldung ist nicht das gewünschte Endergebnis. Nach bestätigter Einrichtung in C3 unterscheiden: gespeicherter alter Listeneintrag oder weiterhin aktiv eigenständig steuerbarer Slave. Nicht durch Löschen, Ausblenden oder Umbenennen einen bestandenen Test vortäuschen. Ein alter Eintrag darf nur nach eindeutig bestätigter Zuordnung von Decoder und aktueller Betriebsadresse für einen gesonderten Fachtest benutzt werden; keine unbekannten Einträge probeweise fahren."),
        _p("G0 bleibt offen, bis Master-UID und Übernahmeformat, tatsächliche Firmware, vollständige Aktivierungsabbildung, bestätigter Lese-/Schreibweg und C2-C7 einschließlich neuer SID zusammen belegt sind. Weder ein gekaufter LokProgrammer noch eine zweite Zentrale allein erfüllt diese Bedingungen."))

    c = _get(sections, "C. Gemeinsamer CS3-Vorabtest")
    _replace(c,
             "Beide Eingänge an derselben Quelle. Nur der gemeinsame ICE-Eintrag wird bedient. Kein neu entstandener zweiter unabhängig zu bedienender Zug. Vorbestehende Einträge nicht blind löschen oder ausblenden. Ist der Slave weiter eigenständig angemeldet und unabhängig steuerbar, ist der Test nicht bestanden.",
             "Beide Eingänge an derselben Quelle. Nur den eindeutig zugeordneten mfx-Master bedienen; keinen DCC-Serviceeintrag. Vorher-/Nachher-Lokliste nach B6 vergleichen. Ein alter gespeicherter Slave-Eintrag ist nicht allein ein Nachweis aktiver Zweitanmeldung. Ist der Slave nach bestätigter Zuordnung weiterhin eigenständig angemeldet und unabhängig steuerbar, ist der Test nicht bestanden. Nichts löschen oder ausblenden, um das Ergebnis passend zu machen.")
    _replace(c,
             "Beide Prüfaufnahmen folgen dem Richtungsbefehl ohne Anrollen. F0 aus schaltet beide Stirnlichtfunktionen aus. Zeitverhalten protokollieren; keine Ein-/Ausblendverzögerung.",
             "Die tatsächlichen Ausgänge LV/LR beider Prüfaufnahmen nach Tabelle C.a einzeln beobachten und eintragen. Richtungswechsel bei Fahrstufe 0 ohne Anrollen; F0 aus: beide Lichtfunktionen aus. Zeitverhalten protokollieren, keine ungewollte Ein-/Ausblendverzögerung. Eine Bildschirm-Funktionsanzeige allein zählt nicht als Ausgangsnachweis.")
    _replace(c,
             "Für G0 erforderlich: An einer Testzentrale, die den Master noch nicht kennt, automatisch anmelden und Slave-Folgen prüfen; danach Rückkehr zur CS3. Eine geänderte Adresse nur bei eigenem Nachweis als geprüft markieren. Ohne Nachweis G0 offen; keine produktiven Lokdaten löschen.",
             "Für G0 eine tatsächlich andere, dokumentierte mfx-SID und erneutes Slave-Folgen ohne dessen Nachkonfiguration nachweisen. Zuerst vorhandene kabelgebundene MS und Gleisbox als eigenständigen Testaufbau nach C.a prüfen. Nur eine neue Zentrale, ein neuer Name oder ein Neustart beweist keine andere SID. Danach Rückkehr zur CS3 ebenfalls prüfen. Fehlt der belastbare SID-Nachweis, bleibt C7/G0 offen; keine produktiven Lokdaten löschen.")
    _replace(c,
             "Decoder- und Softwarestände, Herkunft/Format der Masterdaten, ausgelesene Slave-Einstellung, CS3-Eintrag und alle Ergebnisse sichern.",
             "Decoder-/Softwarestände, verwendete Projektstände, Herkunft/Format der Masterdaten, ausgelesene Slave-Einstellung, tatsächliche LV/LR-Zustände, CS3-Eintrag sowie alte/neue SID mit Nachweisquelle sichern. Sollvorgaben und gemessene Ergebnisse getrennt eintragen.")
    _append(c,
        _p("Während C2-C7 ausschließlich bereits freigegebene Fahr-/Funktionsbefehle senden, keine Decoderkonfiguration ändern. Ob die Mischkombination Konfigurationsbefehle zusätzlich übernimmt, ist nicht ausreichend belegt. Deshalb jede spätere Änderung am physisch getrennten betroffenen Decoder ausführen; dafür genügt es nicht, am Bildschirm eine andere Lok auszuwählen. Auch keinen angeblich harmlosen Konfigurationswert als Experiment schreiben."))

    ca = [
        _p("C.a.1 – Ausgangsnachweis bei Fahrstufe 0", "h2"),
        _p("Vorwärts bedeutet hier: später fährt der Motortriebkopf voraus. Die Tabelle nennt den vorgesehenen physischen Ausgangszustand nach bestätigtem Mapping; sie bescheinigt kein Werkseinstellungsergebnis. Nur geeignete, bereits bestätigte Prüflasten verwenden. Für jede Zeile tatsächliche Anzeige/Messung beider Aufnahmen sowie Verzögerung protokollieren; nicht von einem CS3-Symbol auf einen Ausgang schließen."),
        _table(["Befehl", "60977: LV / LR", "59649: LV / LR", "Späteres Frontbild / Ist-Nachweis"], [
            ["F0 aus; vorwärts", "aus / aus", "aus / aus", "Beide Köpfe dunkel. Ist: __________"],
            ["F0 aus; rückwärts", "aus / aus", "aus / aus", "Beide Köpfe dunkel. Ist: __________"],
            ["F0 an; vorwärts", "an / aus", "an / aus", "Motorseite weiß, Dummy rot. Ist: __________"],
            ["F0 an; rückwärts", "aus / an", "aus / an", "Motorseite rot, Dummy weiß. Ist: __________"],
        ], [1, 1, 1, 1.7]),
        _p("C.a.2 – C7 mit deinem vorhandenen Gerätebestand vorbereiten", "h2"),
        _p("1. Artikelnummern von Gleisbox und kabelgebundener MS, MS-Software und Netzteil notieren; die passende Märklin-Anleitung bestimmt die zulässige Kombination. Eine an der CS3 angeschlossene MS oder eine WLAN-MS am selben Zentralenhost ist kein eigenständiger Adressgeber. Ein zusätzlicher Zentralenkauf wird hier nicht vorausgesetzt.<br/>2. Anmeldehistorie des Masters in diesem unabhängigen System feststellen. Keine Lokliste löschen und keinen Werksreset ausführen, um eine unbekannte Historie zu kaschieren.<br/>3. Vor dem Quellenwechsel CS3 und Testversorgung ausschalten, deren Gleisleitungen vollständig von den Prüfaufnahmen lösen. Erst danach darf der bestätigte MS-/Gleisbox-Aufbau alleine versorgen. Programmierausgänge und Gleisausgänge niemals verbinden.<br/>4. Der Fachprüfende muss eine nachweislich andere SID belegen und ihre Quelle nennen. Ein anderer Lokname, eine DCC-Adresse oder bloße Anmeldung genügt nicht. Ist die SID auf dem vorhandenen Bediengerät nicht belegbar, bleibt dieser Teil offen; zuerst einen belastbaren Datennachweis oder geeigneten Leih-/Prüfzugang klären.<br/>5. Nach belegter Neuvergabe C4/C5 ohne Nachkonfiguration des 59649 wiederholen. Anschließend stromlos zur alleinigen CS3-Versorgung zurückwechseln und das Folgen dort erneut dokumentieren."),
        _table(["Unverwechselbar protokollieren", "Vorher / CS3", "Neue Vergabe / unabhängiges System"], [
            ["Gerät / Artikel / Software", "__________", "__________"],
            ["Dauerhafte UID desselben 60977; Quelle", "__________", "__________"],
            ["Zugewiesene SID; Zahlenformat; Quelle", "__________", "__________"],
            ["SID nachweislich verschieden? / Slave folgt?", "Ausgangszustand: __________", "Nachweisdatei / Ergebnis: __________"],
            ["Rückkehr zur CS3; Ergebnis", "__________", "Keine Nachkonfiguration am Slave: __________"],
        ], [1.8, 1.1, 1.5]),
        _p('Märklin: <a href="' + MS_MANUAL + '">Mobile-Station-Anleitung</a>. Die Eignung muss mit den tatsächlich vorhandenen Artikelnummern und ihrem Softwarestand übereinstimmen; die bekannte Gerätefamilie allein ist keine Anschlussfreigabe.', "small"),
        _p("C.a.3 – Endgültiges Soundprojekt erneut gemeinsam prüfen", "h2"),
        _p("Vor einer Funktionsprüfung muss ausgeschlossen sein, dass auf einer motorbestückten Aufnahme eine Einmessfahrt vorgemerkt ist; keine solche Fahrt starten oder hierfür Werte ausprobieren. Nach Festlegung des endgültigen 60977-Sound-/Funktionsprojekts alle belegten Funktionstasten einzeln protokollieren: gewünschter Sound, Frontlicht, Dummy-Licht und Innenlicht jeweils vorher festlegen. Bei Fahrstufe 0 beide Richtungen und F0 aus/ein prüfen. Mit F0 aus darf eine fremde Funktionstaste nicht ungewollt die Fronten einschalten. Im G0-Aufbau nur seine bestätigten Ausgänge/Lasten prüfen; tatsächliche LoDi-Innenbeleuchtung erst nach den eigenen G4-Voraussetzungen in 17a/18 testen. Freie oder nicht dokumentierte Tasten nicht blind betätigen."),
        _p("Änderungen von Projekt, Mapping, Identitäts-/Synchronisationsparametern oder Firmware machen die betroffenen Prüfergebnisse erneut prüfpflichtig, auch wenn die Artikelnummer gleich bleibt. Das endgültige Fahrzeugprojekt mit Datum sichern. Keine Firmware aktualisieren, nur um einen offenen Nachweis zu umgehen. G0 bleibt bis zum vollständigen ausgefüllten Protokoll offen."),
    ]
    _insert_after(sections, c, "C.a. Ausgangsprotokoll, neue SID und Projektabgleich", ca)

    cfg = _get(sections, "16. Konfiguration vor dem Einbau festlegen")
    _replace(cfg, "Nie beide Decoder am Programmer lassen.",
             "Am Märklin 60971 in diesem Auftrag ausschließlich den Märklin 60977 verwenden; den ESU 59649 niemals dort aufstecken. Für jede Konfiguration nur den betroffenen Decoder im bestätigten Aufbau anschließen, nicht beide über den Zugbus verbinden.")
    _replace(cfg,
             "Am 60977 für deinen eingebauten 60941 den Motortyp Hochleistungsantrieb C90 wählen; die Märklin-Tabelle ordnet ihm CV 52 = 3 zu. Einstellung rücklesen.",
             "Erst den tatsächlich vollständigen, mechanisch und elektrisch geprüften 60941-Umbau bestätigen. Dieser fünfpolige Hochleistungsantrieb wird technisch der Märklin-Einstellung C90 zugeordnet; die Hersteller-Tabelle nennt für C90 CV 52 = 3. Das ist die konkrete technische Zuordnung, keine wörtliche Modellfreigabe für jeden unbekannten Motorzustand. Bei abweichendem oder ungeklärtem Motor den Typ zuerst fachkundig klären. Am 60977 nur den bestätigten Motortyp konfigurieren und die Einstellung rücklesen.")
    _replace(cfg,
             "Falls Änderungen nötig sind, gilt die separate geprüfte Mapping-Schreibkarte aus 12a;",
             "Falls Änderungen nötig sind: den gesamten Zug stromlos machen, den Dummy von Wagenbus und anderem Kopf trennen und nur den bestätigten 59649-Prüfaufbau ohne Puffer am räumlich und elektrisch getrennten Programmiergleis verwenden. Seine Kommunikationsfähigkeit nach F.4/F.10 muss für diesen Aufbau belegt sein. Erst dann gilt die separate geprüfte Mapping-Schreibkarte aus 12a;")
    _replace(cfg,
             "Gewollte Änderungen gegenüber dem Prüfstandprojekt dokumentieren; bei unerklärter Abweichung nicht bestromen.",
             "Gewollte Änderungen gegenüber dem Prüfstandprojekt dokumentieren und die betroffenen G0-/Lichtprüfungen wiederholen; bei unerklärter Abweichung den Fahrzeugaufbau nicht bestromen. Mit endgültigem Sound-/Funktionsprojekt den gemeinsamen Funktionstastenabgleich nach C.a.3 vorsehen; eine unveränderte Firmware ersetzt diesen Abgleich nicht.")
    _replace(cfg,
             "Firmwareänderungen können einen erneuten Kombinationstest erforderlich machen.",
             "Änderungen an Firmware, Soundprojekt, Mapping oder Synchronisationsparametern erfordern erneute Prüfung der jeweils betroffenen Funktionen. Konfiguration immer am physisch getrennten Decoder ändern; Verhalten gemeinsamer mfx-Konfiguration ist hier nicht freigegeben.")
    _replace(cfg,
             "Fahrt ausschließlich Schritt 53; Innenlicht mit Wagen erst Schritt 56.",
             "Erste Motor-Kleinstfahrt nach Schritt 53; Zugfahrten erst nach den dafür erforderlichen Freigaben in 17a/18 und innerhalb der bestätigten zulässigen Last. Innenlicht mit Wagen erst Schritt 56.")
    _append(cfg, _p('Märklin: <a href="' + MARKLIN_MANUAL + '">60977-Originalanleitung, Impressum 260057/1025/Sc7Ef</a>, gedruckte S. 17 und 21: CV52/C90; S. 16 und 21: CV51. Der vorliegende mehrsprachige Download hat 192 PDF-Seiten. Gedruckte Seitenzahlen nicht mit der PDF-Zählung gleichsetzen.', "small"))

    f = _get(sections, "F. CV-Programmierung mit der CS3")
    _append(f, _p("Lesen ist erst nach zwei getrennten Bestätigungen vorgesehen: sicherer tatsächlicher Decoderaufbau und bestätigtes Verhalten der verwendeten CS3-Oberfläche. Fehlende CV-Zeilen nicht am angeschlossenen Decoder ausprobieren; Einzelheiten F.4. Diese Revision ergänzt Nachweis- und Protokollkarten, aber keine schon freigegebene individuelle Synchronisationsprogrammierung."))

    f1 = _get(sections, "F.1. Die nachgewiesenen Synchronisations-CVs")
    f1["title"] = "F.1. In JMRI implementierte Synchronisationsfelder"
    _replace(f1, "Ein zusätzlicher Aktivierungsparameter ist öffentlich noch nicht nachgewiesen.",
             "Die vollständige Aktivierungsabbildung ist noch nicht nachgewiesen. Eine Checkbox beweist kein eigenes zusätzliches Register: Die Funktion könnte auch aus vorhandenen Feldwerten abgeleitet sein. Erst der unverfälschte Offline-Differenzexport nach F.5 kann diese Varianten eingrenzen.")

    f2 = _get(sections, "F.2. Hersteller, Seriennummer und mfx-Adresse")
    _replace(f2,
             "Krauß dokumentiert 0x83 (= 131) im separaten Herstellerfeld von Märklin/Trix. Eine typische Märklin-UID mit Anfang 0x7F beginnt aber gerade nicht mit 0x83.",
             "Die bisherige Auswertung ordnete Krauß außerdem 0x83 (= 131) im separaten Märklin/Trix-Herstellerfeld zu; die genaue genannte Fundstelle ist im aktuellen Abgleich nicht abschließend bestätigt und wird nicht als Eingabefreigabe benutzt. Märklins CAN-Dokument nennt im Fast-Read-Kontext auf S. 19 hingegen ausdrücklich Märklin-UIDs beginnend mit 0x7F; das ist nicht 0x83.")
    _append(f2, _p("Für C7 die dauerhafte Master-UID und die jeweils zugewiesene SID getrennt mit Fundstelle erfassen. Der SID-Nachweis muss beide Zustände eindeutig demselben 60977 zuordnen. Ein anderer Bediener, Zentralenname oder DCC-Serviceeintrag ist kein Nachweis einer neuen mfx-Adresse."))

    f3 = _get(sections, "F.3. Die tatsächliche Masterkennung sichern")
    _append(f3, _p("Aus einer angebotenen Softwareversion folgt weder die tatsächlich installierte CS3-Version noch die Firmware eines der beiden Decoder. Die Aussagen des Nutzers zur aktuellen Software werden durch ein abgelesenes Foto/Protokoll ergänzt, nicht als exakter Build eingesetzt. Für neue Recherchehinweise zur ESU-Firmware siehe F.11; deren indizierte Register nicht in den ersten Lesetest übernehmen."))

    f4 = _get(sections, "F.4. CS3: zuerst ausschließlich lesen")
    f4["elements"].insert(0, _p("Freigabe vor der Bedienfolge", "h2"))
    f4["elements"].insert(1, _p("Die nachstehende Bildschirmfolge ist noch keine bestätigte Live-Anweisung für deine konkrete CS3-Version. Vorher Version/Build erfassen und den Bedienweg ohne angeschlossenen schreibgefährdeten Decoder prüfen lassen: CV-Nummernfeld, Wertefeld, Lesen und Vorlagenschreiben müssen eindeutig unterschieden sein. Ob allein das Hinzufügen einer Zeile bereits schreibt, ist offen; es wird weder als sicher noch als bewiesen gefährlich behauptet. Eine rein optische Prüfung ohne Decoder zeigt die Oberfläche, beweist aber noch nicht das Ausbleiben eines Schreibtelegramms. Für die Freigabe sind ein belastbarer versionspassender Nachweis oder ein fachkundig abgesicherter Test erforderlich. Bis dahin keine fehlenden Zeilen live anlegen."))
    _replace(f4,
             "Ein fehlender Motor kann das Quittieren von Programmierbefehlen beeinflussen. ESU erläutert den Stromimpulsmechanismus allgemein; die Quittierfähigkeit des konkreten motorlosen 59649-Aufbaus an CS3 ist noch nicht gemessen. Deshalb beginnt der Ablauf mit reinem Lesen, nicht mit einem Test-Schreibwert.",
             "Eine passende G0-Prüfaufnahme und der später motorlose Kopf werden getrennt bewertet. Die Quittierfähigkeit des tatsächlich verwendeten 59649-Aufbaus an der CS3 ist noch nicht gemessen; daraus folgt weder ein Pflichtmotor noch ein nachgewiesener Decoderfehler. ESUs allgemeine Erklärung von Quittier-Stromimpulsen ist keine Freigabe dieser Kombination. Nach bestätigtem Aufbau und Bedienweg zuerst ausschließlich lesen, keinen Test-Schreibwert verwenden.")
    _replace(f4, "Nach bestandener elektrischer Prüfung STOP aufheben.",
             "Nur nach bestätigter elektrischer Prüfung UND bestätigtem Bedienweg STOP aufheben.")
    _replace(f4,
             "Falls sie fehlt, eine CV-Zeile hinzufügen und ausschließlich im Feld CV-Nr. die 8 eintragen.",
             "Falls sie fehlt, hier anhalten: STOP und Decoder von der Versorgung trennen. Erst nach bestätigter Zeilenanlage gemäß obiger Freigabe darf die Zeile mit CV-Nr. 8 vorbereitet werden; die ungeprüfte Live-Anlage ist nicht erlaubt. Danach zur Aufbauprüfung am Anfang dieses Kapitels zurückkehren: denselben Decoder nur stromlos wieder anschließen, Aufbau erneut prüfen und erst bei weiterhin bestätigtem Bedienweg STOP aufheben. Anschließend mit dem vorgesehenen Lesevorgang fortfahren.")
    _replace(f4,
             "Erst nach zwei erfolgreichen Lesevorgängen die CVs 191, 192, 193, 194 und 195 ergänzen und lesen.",
             "Erst nach zwei erfolgreichen Lesevorgängen die bereits sicher vorbereiteten CVs 191, 192, 193, 194 und 195 lesen. Bei fehlenden Zeilen gilt dieselbe vorherige Freigabe; nicht live ausprobieren.")
    _replace(f4, "CV8 lesen ist ungefährlich;",
             "Ein nachweislich reiner CV8-Lesebefehl verändert keinen Parameter; die sichere Bedienung des Editors bleibt Voraussetzung;")
    _append(f4, _p("Bei ausbleibender Quittierung bleibt der Schreibweg gesperrt. Den Aufbau mit Artikel, angeschlossenen Lasten und Fehleranzeige dokumentieren; keine Ersatzlast improvisieren. Ein fachkundig bestätigter anderer Prüfaufbau oder optionaler ESU-Programmer ist erst ein möglicher Ersatzweg, keine automatisch erforderliche Anschaffung. CV8 = 151 bestätigt den Hersteller, nicht Artikel 59649, Firmware oder erfolgreiche Synchronisation."))

    f5 = _get(sections, "F.5. Kostenloser Nachweis durch CV-Export")
    _append(f5, _p("Die Offline-Checkbox kann ein separates Register, mehrere Parameter oder einen aus Hersteller-/Seriennummernfeldern abgeleiteten Zustand repräsentieren. Keine dieser Varianten vor dem Export voraussetzen. Ein Vergleich mit veränderten oder gelöschten Zielnummern ist als solcher zu benennen. PC-Softwareversion, exportierter Projekttyp und reale Decoderfirmware bleiben drei verschiedene Nachweise."))

    f6 = _get(sections, "F.6. CS3: einzelne CVs schreiben und kontrollieren")
    f6["title"] = "F.6. CS3: freigegebene Einzelwerte übertragen"
    _replace(f6,
             "Für CV191-195 fehlt diese Liste noch.",
             "Für CV191-195 fehlt diese Liste noch. Zusätzlich müssen tatsächlicher Prüfaufbau, zuverlässige Rücklesung und versionspassender Bedienweg einschließlich eventuell nötiger Zeilenanlage nach F.4 bestätigt sein. Bis dahin bleibt diese gesamte Schreibfolge gesperrt.")
    _replace(f6,
             "Fehlt sie, eine neue Zeile hinzufügen und nur das Nummernfeld ausfüllen.",
             "Fehlt sie, STOP setzen und Decoder abtrennen; eine Zeile erst mit dem nach F.4 bestätigten Verfahren vorbereiten, niemals den ungeprüften Editor am Decoder ausprobieren. Danach zur Aufbauprüfung aus F.4 zurückkehren: denselben Decoder nur stromlos wieder anschließen, Aufbau erneut prüfen und erst bei weiterhin bestätigtem Bedienweg STOP aufheben. Anschließend den vorgesehenen Lesevorgang fortsetzen; keine Schreibfreigabe überspringen.")
    _replace(f6,
             "Nach erfolgreicher gesamter Liste noch einmal alle geänderten CVs lesen, Ergebnis sichern und STOP setzen.",
             "Nach erfolgreicher gesamter Liste die geänderten nicht indizierten CVs nochmals frisch lesen, Ergebnis sichern und STOP setzen. Indizierte Register werden ausschließlich innerhalb ihrer eindeutig bestätigten Indexgruppe nach F.11 rückgelesen; kein unspezifisches Gesamtlesen als Nachweis aller Gruppen werten.")
    _replace(f6,
             "Eine zusätzliche indizierte CV aus einem echten Export benötigt zuerst genau dessen CV31- und CV32-Werte. Solche zusätzlichen Register werden erst nach separater Prüfung aufgenommen, nicht aus einem anderen Decoderprojekt ergänzt.",
             "Zusätzliche indizierte CVs aus einem echten Export gehören in die getrennte Karte F.11: Indexgruppe vor Lesen, Schreiben und Rücklesen eindeutig festlegen. Die dortige Dokumentationsvorlage enthält keine ausführbaren Index-Zielwerte. Solche Register erst nach Prüfung einer individuellen Karte aufnehmen, nicht aus einem anderen Decoderprojekt ergänzen.")

    f7 = _get(sections, "F.7. Kritische Bedienfehler und konkrete Schutzregeln")
    _append(f7,
        _p("Konfiguration und Serviceeintrag strikt trennen", "h2"),
        _p("Auch nach bestandener Synchronisation den 60977 und 59649 niemals gemeinsam konfigurieren. Gesamten Zug stromlos machen, den zu ändernden Kopf von Kupplungsbus und anderem Kopf trennen und nur den bestätigten Einzelaufbau ohne Puffer programmieren. Danach betroffene Synchronisations-/Funktionsprüfungen wiederholen. Am 60971 nur den 60977; niemals den 59649."),
        _p("Ein CS3-Eintrag SERVICE ESU59649 ist nur ein Bedien-/Wartungsdatensatz. Seine Adresse umzubenennen oder zu ändern ist nicht gleichbedeutend mit einer Änderung der im Decoder gespeicherten DCC-Adresse. DCC-Service-Mode am Programmiergleis ist außerdem nicht adressselektiv. Tatsächliche DCC-/MM-Adressen und aktivierte Protokolle beider Decoder getrennt nach F.11 erfassen; keine CV47-/CV50-Werte aus einem anderen Decoder übernehmen. DCC für einen weiterhin benötigten Wartungsweg nicht pauschal abschalten."),
        _p("Drei getrennte Sperren bleiben bestehen: keine Reset-Schreibbefehle an CV8; keine Einmessfahrt (60977: keine 77 im CV7/Firmwarefeld; 59649: keine Kombination CV54 = 0 und anschließend F1); beide 60974 bleiben bei diesen Kommunikationsprüfungen abgetrennt. Eine spätere Pufferfreigabe gilt nicht rückwirkend für den Programmieraufbau."))

    f8 = _get(sections, "F.8. Gegenprüfung und Anforderungsabdeckung")
    _append(f8, _p("Der Literaturabgleich ist abgeschlossen, der Hardware-Nachweis nicht. Besonders die aktuelle Mischkombination, ihr Verhalten nach einer belegten SID-Neuvergabe und das endgültige Funktionstasten-/Soundprojekt bleiben gemeinsam zu prüfen. Die bei C.a ergänzten Protokolle ändern den Status heute nicht zu bestanden."))

    f9 = _get(sections, "F.9. Nachweisplan bis zur Umbaufreigabe")
    _replace(f9, "Die Recherche schließt die bisherige Registerlücke.",
             "Die Recherche grenzt die Registerfrage ein; vollständige Aktivierungsabbildung und individuelle Masterübernahme sind noch offen.")
    _replace(f9,
             "Isolierter 59649: CV8 zweimal = 151; CV191-195 jeweils frisch und fehlerfrei gelesen.",
             "Tatsächliche Prüfaufnahme und CS3-Bedienweg bestätigt; isolierter 59649: CV8 zweimal = 151 und CV191-195 frisch fehlerfrei gelesen. Späteren motorlosen Aufbau nicht stillschweigend gleichsetzen.")
    _replace(f9,
             "Erneut nachweislich andere mfx-SID; Slave folgt ohne neue Konfiguration.",
             "Nachweislich andere mfx-SID mit Quelle; Slave folgt ohne Nachkonfiguration. Vorhandene MS/Gleisbox zuerst auf Eignung prüfen; Ablauf und Rückkehrtest nach C.a.")
    _replace(f9,
             "Zuerst Sicherung/Identität und reiner Lesetest, parallel ein Originalexport der ESU-Sonderoption.",
             "Zuerst Sicherung/Identität sowie bestätigten Prüfaufbau und CS3-Bedienweg klären; erst danach reiner Lesetest. Parallel Originalexport der ESU-Sonderoption und Eignung der vorhandenen MS/Gleisbox prüfen.")

    f10 = _get(sections, "F.10. Dein Leseprotokoll und fehlende Nachweise")
    _replace(f10, "Nur nach bestätigtem Prüfaufbau beginnen;",
             "Nur nach bestätigtem Prüfaufbau UND bestätigtem CS3-Bedienweg einschließlich benötigter Zeilenanlage beginnen;")
    _append(f10,
        _p("Zusätzlicher Nachweis zur konkreten Leseaufnahme", "h2"),
        _p("Aufnahme / Schnittstellenvariante / tatsächlich angeschlossene Lasten: ____________________<br/>Motor in dieser Aufnahme vorhanden? ____________________<br/>Bestätigung der Eignung, Datum und Quelle: ____________________<br/>Versionspassender Nachweis zum CS3-Editor und zur Zeilenanlage: ____________________<br/>G0-Prüfaufnahme oder späterer motorloser Kopf? ____________________<br/>Beide 60974 und alle anderen Decoder physisch abgetrennt: ____________________<br/>Eine neue SID und ihre Herkunft gehören separat in C.a; eine Firmwarezahl ist kein SID-/UID-Nachweis."))

    f11 = [
        _p("F.11.1 – Indizierte Register: Vorlage, noch keine Schreibfreigabe", "h2"),
        _p("CV191-195 benötigen keine Änderung von CV31/CV32. Die folgende Karte gilt nur, falls ein echter Export oder ein artikel-/firmwarepassender Primärnachweis zusätzliche indizierte Register verlangt. Indexwahl ist selbst ein Schreibzugriff. Deshalb keinen Index aus dieser Erläuterung ausprobieren. Erst eine vollständige individuelle Karte mit bestätigtem Originalzustand, begründeten Zielwerten, erlaubter Reihenfolge und sicherem CS3-Bedienweg freigeben."),
        _table(["Decoder / Quelle", "CV31 / CV32", "Ziel-CV", "Alt / Ziel / frisch rückgelesen"], [
            ["__________", "__________ / __________", "__________", "__________ / __________ / __________"],
            ["__________", "__________ / __________", "__________", "__________ / __________ / __________"],
        ], [1.2, 1.2, .7, 2]),
        _p("Für jede später freigegebene Indexgruppe die vorgeschriebenen CV31-/CV32-Werte in genau der bestätigten Reihenfolge einstellen und dokumentieren. Danach Zielregister frisch lesen, mit der Karte vergleichen, nur den genehmigten Wert schreiben und in derselben Gruppe frisch rücklesen. Vor jedem Gruppenwechsel die nächste vollständige Indexangabe prüfen; eine gleichlautende Ziel-CV in anderer Gruppe ist ein anderer Parameter. Nach Unterbrechung nicht auf einen vermuteten Index vertrauen. Abschlusslesen gruppenweise durchführen. Indexzustand nur auf dokumentierte, bestätigte ursprüngliche Werte zurückstellen, nicht pauschal auf null. Bei Fehler sofort STOP; letzten Schreibvorgang als möglicherweise bereits erfolgt behandeln."),
        _p('ESU: <a href="' + ESU_EXPORT + '">CV-Änderungen anzeigen</a>. Herstellerregel zur vollständigen Indexgruppe; diese leere Protokollvorlage ersetzt keinen Originalexport.', "small"),
        _p("F.11.2 – Neuer Firmware-Recherchehinweis K3: nicht ausführen", "h2"),
        _p("Die aktuell eingesehene JMRI-Definition v5standardCVs bindet v4decoderInfoCVs ein. Dort wird die A-Code-Firmware im Index 0/255 durch CV285:2 (Build), CV287 (Minor) und CV288 (Major) beschrieben. Das ist Primärevidenz für Softwaredefinitionen, nicht die ausgelesene Firmware des vorhandenen 59649 und keine von ESU bestätigte CS3-Lesekarte für diesen Aufbau. Die Bezeichnung v4 im Dateinamen allein widerlegt die Einbindung in die V5-Definition nicht. Auch eine einzelne CV7-Zahl ist nicht automatisch die vollständige Versionsangabe."),
        _p("Diese Register bleiben außerhalb von F.4/F.10. Vor einer praktischen Verwendung müssten Modell-/Firmwareeinbindung, Byteauswertung, die schreibende Indexauswahl und das Rückstellen des Originalindex separat bestätigt werden. Kein Firmwareupdate durchführen. Die angebotene LokProgrammer-Version oder eine darin genannte Decoderfirmware beweist nicht den tatsächlichen Stand deines Decoders."),
        _p('JMRI, ergänzende Live-Recherche vom 10.09.2026: <a href="' + JMRI_V5 + '">v5standardCVs.xml – Einbindung</a> und <a href="' + JMRI_INFO + '">v4decoderInfoCVs.xml – Firmwarefelder</a>. Anders als F-3 bis F-8 sind diese ergänzenden URLs nicht auf einen unveränderlichen Commit festgelegt; daraus wird keine Programmierfreigabe abgeleitet.', "small"),
        _p("F.11.3 – Protokolle, tatsächliche Adressen und Wartung", "h2"),
        _table(["Decoder / eigener Einzelaufbau", "Reale DCC-Adresse / Quelle", "Reale MM-Adresse / Quelle", "Aktive Protokolle / Quelle"], [
            ["Märklin 60977", "__________", "__________", "__________"],
            ["ESU 59649", "__________", "__________", "__________"],
        ], [1.3, 1.3, 1.3, 1.3]),
        _p("Einzutragen sind bestätigte Decoderwerte und ihre Herkunft, nicht nur die Adresse eines CS3-Symbols. Im gemeinsamen mfx-Test dürfen laufende DCC-/MM-Ereignisse kein scheinbares Folgen erzeugen. Überlagerte Betriebsadressen nicht durch Umbenennen des Serviceeintrags für gelöst erklären. Änderungen nur artikelgenau geplant, einzeln programmiert und rückgelesen; diese Karte nennt bewusst keine pauschalen Protokoll-CV-Zielwerte. Fehlende Werte bleiben offen, nicht mit null ausfüllen."),
    ]
    _insert_after(sections, f10, "F.11. Ergänzende Nachweiskarten – keine zusätzlichen Live-CVs", f11)

    src = _get(sections, "F. Quellen: Hersteller und Implementierung")
    _replace(src,
             "S. 19 und 28: UID/SID; S. 50-51: Datenfelder in lokomotive.cs2.",
             "S. 8: System-UID; S. 28: Bind mit UID/SID; S. 19: Märklin-UID-Präfix im Fast-Read-Kontext; S. 50-51: Datenfelder in lokomotive.cs2.")
    _replace(src,
             "Version 2.3, 17.06.2017; S. 22-23 und 39; originale Protokollanalyse.",
             "Version 2.3, 17.06.2017; originale Protokollanalyse. Die bislang genannten Fundstellen S. 22-23 und 39 sind im aktuellen Abgleich nicht abschließend inhaltsbezogen bestätigt; keine Decoder-Eingabewerte darauf freigeben.")
    _replace(src, "JMRI-Dateien sind auf Commit",
             "Die JMRI-Belege F-3 bis F-8 zur Identität und Bytefolge sind auf Commit")
    _replace(src,
             "08.05.2025; 131: Trix Modelleisenbahn, 151: Electronic Solutions Ulm.",
             "Historisch zitierter Quellenstand 08.05.2025; 131: Trix Modelleisenbahn, 151: Electronic Solutions Ulm. Ein späterer Stand der veränderlichen URL macht den bezeichneten früheren Stand nicht automatisch falsch; daraus folgt weiterhin keine individuelle mSD3-Masterkennung.")

    src2 = _get(sections, "F. Quellen: Bedienung und Gegenbelege")
    _replace(src2,
             "8. Auflage, 24.01.2023; S. 43, Abschnitt 8.2.6: CS2/CS3; Motor-Einmessung in Abschnitt 11.1.4.",
             "8. Auflage, Januar 2023; Deckblatt: ab Firmware 5.3.128. Gedruckte S. 43, Abschnitt 8.2.6: CS2/CS3; Standardmapping gedruckte S. 67; Motor-Einmessung Abschnitt 11.1.4. Mindeststand der Handbuchausgabe ist nicht der ausgelesene Stand des Nutzerdecoders.")
    _replace(src2,
             "S. 24-25: Programmierung und Quittierung über Stromimpulse; keine Zusage für motorlosen 59649 an CS3.",
             "Allgemeiner Hintergrund zur Programmierung/Quittierung. Die bislang angegebene genaue Fundstelle S. 24-25 ist im aktuellen Abgleich nicht abschließend bestätigt; keine spezifische Zusage für motorlosen 59649 an CS3 daraus ableiten.")
    _replace(src2,
             "Die vollständige REV9 verbindet alle Baukarten mit diesem CV-Kapitel und den zusätzlich geprüften Handgriffen.",
             "REV10 übernimmt den vollständigen Bauumfang und korrigiert Nachweisgrenzen und Bedienvoraussetzungen. G0 bleibt bis zur dokumentierten Prüfung am vorhandenen Decoderpaar offen.")
    _append(src2,
        _p('Ergänzende Märklin-Originalquelle: <a href="' + MARKLIN_MANUAL + '">mSD3/60977-Anleitung</a>. Impressum 260057/1025/Sc7Ef bestätigt den Stand 10/2025; 192 PDF-Seiten, mehrere Sprachen. CV51 gedruckt S. 16/21, CV52 gedruckt S. 17/21. Ein zuvor fehlgeschlagener Download widerlegt diese Angaben nicht.', "small"),
        _p("Ergänzende Recherchequellen und ihre Nachweisgrenzen stehen unmittelbar bei C.a und F.11. Für die praktischen CS3-Schritte bleibt der reale Versions-/Oberflächennachweis erforderlich; die Quellenprüfung hat keine Tastenbetätigung am Nutzergerät und keinen Hardwaretest ersetzt.", "small"))
    return sections


COVERED = {
    "R-05": "B6/C3: Vorab-Eigenanmeldung, gespeicherter Eintrag und aktive Zweitanmeldung unterscheiden.",
    "R-06": "C/16/F7: Konfiguration nur am physisch getrennten Decoder; gemeinsames Verhalten offen.",
    "R-07": "C.a.3/16: endgültiges Sound-/Funktionsprojekt mit allen belegten Tasten prüfen.",
    "R-08": "F6/F11: indizierte Gruppenkarte; keine unbestätigten Indexzielwerte.",
    "R-09": "A/F4/F10: Prüfaufnahme, Lasten und spätere motorlose Quittierung getrennt belegen.",
    "R-10": "F3/F10/F11: Firmware, UID und SID getrennt; neue K3-Werte nur Recherche.",
    "R-11": "A/C7/C.a: vorhandene MS und Gleisbox zuerst prüfen, keine Kaufpflicht.",
    "R-16": "C4/C.a: tatsächliche LV/LR-Ausgänge mit beiden Richtungen und F0 protokollieren.",
    "R-17": "16/F7: örtliche Trennregel vor Nachprogrammierung plus Wiederholungsprüfung.",
    "R-25": "F7/F11: Decoderadressen, Serviceeintrag und aktive Protokolle getrennt dokumentieren.",
    "R-37": "F4/F6: ungeprüfte CV-Zeilenanlage nicht live freigeben.",
    "R-38": "F1/F5/F9: Implementierungsbeleg präzisiert; Aktivierungsabbildung bleibt offen.",
    "R-39": "16: C90/CV52=3 als technische Zuordnung zum real geprüften 60941 erklären.",
    "R-40": "16/F7: 60971 ausschließlich für 60977; nie für59649.",
    "R-41": "F7: Reset, Einmessfahrt und Puffer getrennte Sperren; Kurzfassung bearbeitet Root.",
    "R-42": "F-Quellen/16: CAN, ESU-Ausgabe und Märklin10/2025 präzisiert; offene Fundstellen qualifiziert.",
}

OFFEN = [
    "G0 ist nicht bestanden: reale UID-Übernahme, Aktivierungsabbildung, Firmware und Kombinationstest fehlen.",
    "Keine bestätigte CS3-Zeilenanlage oder neue individuelle CV-Schreibfolge erzeugt.",
    "Vorhandene MS-/Gleisbox-Artikel, Software, Netzteil, Anmeldehistorie und SID-Leseweg noch belegen.",
    "DCC-Quittierung tatsächlicher G0-Aufnahme und späteren motorlosen Kopf getrennt messen.",
    "K3-Firmwareindex nur Recherche; keine operative Lesekarte und keine Hardwarefreigabe.",
    "R12/R13 und gemeinsame Gate-Reihenfolge, 16a/16b,12a,E,G sowie Layout/Navigation liegen bei Root.",
    "Nach Umsetzung durch Builder vollständige Umfangs-, Verweis- und Layoutprüfung erforderlich.",
]
