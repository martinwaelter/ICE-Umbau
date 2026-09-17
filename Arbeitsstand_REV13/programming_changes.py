"""Evidenzbasierte Korrekturen an den final nummerierten REV12-Karten 6–12."""

SOURCES = [
    {
        "id": "Q35",
        "title": "JMRI LokPilot 5/MKL: Einbindung der gemeinsamen Decoderinformationen",
        "url": "https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/ESU_LokPilot5.xml#L246",
    },
    {
        "id": "Q5",
        "title": "LoDi-Shop: Abschnitt „LoDi-WiB ICE-M Front 2 Stück“, ohne Vorwiderstände",
        "url": "https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/",
    },
]


def _find(page, kind, label=None):
    return next(b for b in page["blocks"] if b["type"] == kind and (label is None or b.get("label") == label))


def apply(P):
    # Der bereits vorhandene Ein-Aufnahme-Weg wird konkretisiert, kein Tor entfällt.
    _find(P[6], "step", "2.")["text"] = (
        "Für den vollständigen Ablauf <b>zwei Märklin 60970</b> samt passender Anleitung leihen oder beschaffen. "
        "Je Aufnahme genau ein Decoder. Mit einer Aufnahme sind Einzelarbeiten möglich; der Paarnachweis [[12]] bleibt offen. "
        "Ohne Aufnahme nur Dateien und Software vorbereiten. Bis zum bestandenen Paartest keinen elektrischen Zugumbau beginnen."
    )
    _find(P[6], "step", "4.")["text"] = (
        "Aufnahmen auf trockene, nicht leitende Fläche legen. Für spätere ESU-Änderungen bleibt eine geeignete Einzelaufnahme nötig, "
        "für erneute Paarprüfung wieder beide. Leihzugang entsprechend einplanen. Quellenwechsel immer ausschalten und physisch trennen; "
        "nie Programmer, Programmiergleis, Betriebsgleis oder Gleisbox zugleich anschließen."
    )
    P[6]["blocks"][-1]["text"] = (
        "<b>Jetzt schon möglich:</b> Dateien/Masterprojekt [[8]] sichern und Softwarevergleich [[9]] vorbereiten. "
        "Der Programmer allein ersetzt keine Aufnahme. Netzteil und CS3 bleiben geschlossen; Einrichtung auf [[7]]."
    )

    # Herstellerabbildung und Zuschnitt bleiben unverändert.
    P[7]["before"] = "Artikel und Beschriftung mit dem Originalbild vergleichen. Alle Kabel sind abgezogen; Schalter nur spannungslos ändern."
    _find(P[7], "small")["text"] = "Original Märklin 60970, Schalterübersicht. Bezeichnungen am eigenen Gerät abgleichen."
    t = _find(P[7], "table")
    t["headers"] = ["Bedienelement", "Aufnahme 60977", "Aufnahme 59649"]
    t["rows"] = [
        ["Feste Decoderbuchse", "MTC 21", "MTC 21"],
        ["e: Datenquelle", "Zentrale", "Zentrale"],
        ["b: Motorumschaltung", "Motor", "Motor (Prüflast)"],
        ["a: AUX3 / AUX4", "Logikpegel; nicht aktivieren", "verstärkt"],
        ["c: Reed-Simulation", "Nicht betätigen", "Nicht betätigen"],
        ["d: Impedanz", "8 Ω; Soundfunktion aus", "100 Ω; keine externe Last"],
    ]
    t["widths"] = [1.15, 1.5, 1.5]
    _find(P[7], "step", "1.")["text"] = (
        "Kontakt 1 (weißer Punkt), Index und Decoder zuordnen; gerade einsetzen. Andere Buchsen und Lastklemmen bleiben frei. "
        "ESU zeigt beim <b>59649 Pins 9/10 unbelegt</b> (Q6, S. 19, Abb. 3). 100 Ω ist eine echte Lautsprecherlast, keine Trennung. "
        "Bei anderer Decoderrevision die Belegung zuerst klären."
    )
    _find(P[7], "step", "2.")["text"] = (
        "DCC-Lesen: nur eine Aufnahme am Programmiergleisausgang. Paartest: beide Gleiseingänge an derselben getrennten "
        "Betriebsquelle. Dafür Verteiler <b>vor Anschluss an Aufnahme/CS3</b> nach [[4]] prüfen: beide B-Pfade und beide 0-Pfade "
        "durchgängig, B gegen 0 offen. CS3 B an 60970 „rt“, 0 an „bn“ (Q18, S. 29); Aufdrucke fotografieren. USB/60971 bleiben ab."
    )
    _find(P[7], "note", "NUR F0 UND RICHTUNG")["text"] = (
        "Zwei getrennte Aufnahmen an einer Quelle sind eine eigene Schaltungsfestlegung: je Gerät ein Decoder, nur die Gleiseingänge "
        "parallel, keine Ausgänge verbinden. AUX3/4 des 60977 erst nach gesicherter Projektzuordnung prüfen. "
        "Der 59649-Motor bleibt eine Prüfstandslast; im Gegenkopf wird kein Motor eingebaut."
    )
    P[7]["blocks"] = [b for b in P[7]["blocks"] if b["type"] != "p"]
    P[7]["check"] = (
        "Stecklage, Schalter und B/0 stimmen; genau eine Quelle. Vor GO: Fahrstufe 0, F0/Sound aus. "
        "Bei Geruch, Überlast oder unerwartetem Motorlauf sofort STOP und trennen. Soundprüfung später separat nach [[22]]/[[35]]."
    )

    # Explizite Evidenzgrenze verhindert, dass vier korrekt geschriebene Bytes
    # als Beweis für das geräteübergreifende Identitätsformat gelten.
    _find(P[9], "small")["text"] = (
        "JMRI-Ableitung: S = CV192 + 256 × CV193 + 65.536 × CV194 + 16.777.216 × CV195; Bytes dezimal. "
        "Die Gleichsetzung von Märklin-mfxuid und ESU-Masterseriennummer ist für dieses Paar eine zu prüfende Annahme. "
        "Rücklesen belegt nur Speicherung; erst [[12]] zeigt die tatsächliche Paarfunktion. Aktivierung zusätzlich aus dem Originalexport."
    )

    P[11]["before"] = (
        "[[8]]–[[10]] erledigt; eine ausdrücklich gemeldete Updateanforderung vor Änderungen klären. "
        "Einzelaufnahme von Master, Anlage, Zug und anderen Quellen getrennt. M4 und DCC-Wartungszugang erhalten."
    )
    _find(P[11], "step", "3.")["text"] = (
        "Zielwert als <b>dezimales Byte von 0 bis 255</b> prüfen, in die richtige Zeile eingeben. "
        "Die CS3 schreibt die bestätigte Wertänderung unmittelbar. <b>„Prog.“ und „Vorlagenwerte schreiben“ nicht benutzen</b>: "
        "Sie würden die gesamte Vorlagenliste übertragen (Q24)."
    )
    _find(P[11], "note", "OPTIONAL: FIRMWARE FÜR DIE DIAGNOSE")["text"] = (
        "Getrennte Listen „Index“ (CV31/32) und „Firmware“ (CV285–288) ohne Decoder vorbereiten. Index-Altwerte sichern. "
        "CV31 = 0, danach CV32 = 255 einzeln schreiben/rücklesen. Erst bei 0/255 Firmwareliste nur lesen: "
        "Version = CV288.CV287.(256 × CV286 + CV285). Ursprüngliche Indexwerte wiederherstellen/rücklesen. "
        "Nach Unterbrechung zuerst Indexzustand lesen. JMRI bindet die gemeinsame Datei v4decoderInfoCVs auch in LP5/MKL ein "
        "(Q13/Q23/Q35): Softwarebeleg, kein eigener Gerätetest oder Kompatibilitätsnachweis."
    )
    for source in ["Q24", "Q35"]:
        if source not in P[11]["sources"]:
            P[11]["sources"].append(source)

    P[12]["title"] = "CS3-Paarprüfung: gemeinsame Funktion nachweisen"
    P[12]["check"] = (
        "F0/Richtung, gemeinsamer Neustart und mfx-Bedienweg bestanden: Zugumbau zulässig. Erweiterte Startfolgen "
        "separat dokumentieren; vor Fremdbetrieb SID-Wechsel nachweisen. Paarprüfung nach relevanten Projektänderungen "
        "oder neuer Masteranmeldung/SID an der eigenen CS3 wiederholen."
    )
    return P
