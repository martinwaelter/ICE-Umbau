"""Knappe Bedienkorrekturen, anzuwenden auf finale REV13-Seiten 1–46.

U-P1: Vergleichsdaten und endgültigen persönlichen Export ausdrücklich trennen.
U-P2: CS3 liest Listen; indizierte Register daher bankweise vorbereiten/lesen.
U-P3: Gesicherter Altwert als Vergleichsbezug, nicht der spätere Zielwert.
U-P4: Prüfsoll nicht mit bereits bestandenem Ist-Ergebnis verwechseln.
U-P5: Geräte- und Wartungsrückverweise und wesentliche Begriffe erläutern.
Keine Hardwarevoraussetzung, Quellenbehauptung oder Freigabegrenze geändert.
"""


def _find(page, kind, label=None):
    return next(b for b in page["blocks"] if b["type"] == kind and (label is None or b.get("label") == label))


def apply(P):
    assert P[13]["title"].startswith("ESU: belegte Einzelwerte"), "Finale REV13-Seitennummern erforderlich"
    P[8]["goal"] = (
        "60977 ist der Master: Er führt den Zug und erzeugt den Sound. 59649 ist der Slave: Er soll dem Master folgen. "
        "Prüfe beide außerhalb der Fahrzeuge, bevor der elektrische Zugumbau beginnt."
    )

    _find(P[11], "step", "2.")["text"] = (
        "‚Decoder > Sonderoptionen‘ öffnen und Master/Slave-Adress-Synchronisation suchen. Persönliche Masterdaten eingeben, "
        "Ausgangszustand aus und sichtbare Felder fotografieren; diesen Ausgangsstand sichern. Sind Felder bei aus gesperrt "
        "oder leer, dieses Verhalten festhalten. Jeden Einzelvergleich mit dem gesicherten Ausgangsstand beginnen. "
        "Für die Bytefolge zusätzlich eine reine Testkopie mit vier verschiedenen Nummernbytes verwenden, z. B. "
        "0x01020304 = 16909060; erwartete Bytes 4, 3, 2, 1. <b>Testkopie nie programmieren.</b>"
    )
    _find(P[11], "step", "5.")["text"] = (
        "Vergleiche auswerten: Herstellerfeld, vier Seriennummernbytes, Aktivierung und weitere Indexgruppen müssen erklärbar sein. "
        "Danach den <b>persönlichen Ausgangsstand</b> neu öffnen: Hersteller 131 und ausschließlich die eigene Kennung aus [[10]]. "
        "Schritt 3 erneut ausführen und diesen persönlichen Export eindeutig benennen. Nur er dient zum Schreiben auf [[13]]; "
        "Testseriennummer und Hersteller-ID 151 dürfen darin nicht stehen."
    )

    _find(P[12], "step", "1.")["text"] = (
        "CS3 auf STOP; Aufnahme und Anlage physisch trennen. Vor dem ersten ESU-Strom die Lokliste fotografieren. "
        "Manuellen DCC-Eintrag „SERVICE ESU59649 – nicht fahren“ vorbereiten. DCC dient hier zum Lesen/Schreiben; "
        "die Bedienadresse dieses Eintrags ändert keine Decoderadresse. Serviceprogrammierung erreicht jeden verbundenen Decoder: "
        "Nur der 59649 darf angeschlossen sein."
    )
    _find(P[12], "step", "2.")["text"] = (
        "„Bearbeiten > Loks bearbeiten“, Serviceeintrag und „Konfigurieren“ öffnen. Programmiergleis wählen, "
        "nicht PoM (= Programmieren auf dem Hauptgleis). Fehlende CV-Zeilen ohne Decoder vorbereiten. "
        "CV bedeutet gespeicherte Decoder-Einstellung. <b>„Decoder auslesen“</b> liest die Liste frisch; "
        "ein angezeigter alter Wert ist kein neuer Leseerfolg."
    )
    p12s3 = _find(P[12], "step", "3.")
    p12s3["text"] = p12s3["text"].replace(
        "Eine mögliche neue M4-Selbstanmeldung",
        "Eine mögliche neue M4-Anmeldung (ESUs Bezeichnung für mfx)",
    )

    P[13]["before"] = (
        "[[10]]–[[12]] erledigt; eine ausdrücklich gemeldete Updateanforderung vor Änderungen klären. "
        "Zunächst Aufnahme und Quellen getrennt lassen. Listen vorbereiten; Wiederanschluss erst in Schritt 2. "
        "M4 und DCC-Wartungszugang erhalten."
    )
    _find(P[13], "step", "1.")["text"] = (
        "Für jede geänderte CV des <b>persönlichen</b> Exports eine Zeile mit Index, echtem Altwert und Zielwert anlegen. "
        "Fehlende Altwerte in Schritt 2 vor jeder Änderung lesen; Projekt-Standardwerte ersetzen sie nicht. "
        "CV191–195 benötigen keinen Index. Index/Bank bedeutet die ausgewählte Speicherseite; "
        "dieselbe CV-Nummer kann je Bank eine andere Einstellung bezeichnen."
    )
    _find(P[13], "step", "2.")["text"] = (
        "Ohne Decoder mit „CV Hinzu“ und „Speichern“ eine Vorlage pro benötigter CV-Gruppe vorbereiten; "
        "für indizierte Gruppen zusätzlich eine Vorlage nur mit CV31/32 (Q24). Die CS3 zeigt immer nur die aktuell geladene Liste. "
        "Nur 59649 nach [[12]]/3 anschließen und kontrolliert mit GO versorgen. Für indizierte CVs zuerst Indexvorlage laden; "
        "CV31, dann CV32 nach Export setzen/rücklesen. <b>Erst danach</b> die passende Bankvorlage laden: Laden startet bereits "
        "das Lesen. Ohne erforderlichen Index direkt die Liste der nicht indizierten CVs verwenden. "
        "Frische Altwerte notieren; bei Abweichung von gesicherten Altwerten Ursache klären, nicht schreiben."
    )
    _find(P[13], "step", "4.")["text"] = (
        "Schreibabschluss abwarten. Mit <b>„Decoder auslesen“</b> die Liste der gerade ausgewählten Bank frisch lesen. "
        "Die geänderte CV muss fehlerfrei exakt den Zielwert zeigen. Erst dann nächste Zeile. "
        "Am Ende jede Indexgruppe mit passender Bank und Liste erneut kontrollieren und die Rücklesewerte sichern."
    )

    _find(P[14], "step", "1.")["text"] = (
        "CS3 auf STOP, nur Master am getrennten Betriebsausgang anschließen; STOP aufheben. Vorhandenen mfx-Eintrag verwenden "
        "oder Anmeldung abwarten. F0/Richtung an LV/LR-Anzeigen prüfen. STOP, Versorgung trennen, ESU-Aufnahme parallel ergänzen, "
        "wieder anschließen und STOP aufheben. Plus-, Motor-, Licht- und Lautsprecherleitungen beider Decoder niemals verbinden."
    )
    _find(P[14], "step", "2.")["text"] = (
        "Tabelle = <b>Sollzustände</b>. Nur den mfx-Mastereintrag bedienen, jede passende Zeile abhaken. "
        "Mindestens fünf Richtungswechsel bei Fahrstufe 0; reale LV/LR-Anzeigen beobachten. "
        "Die hintere Farbvertauschung entsteht später durch Verdrahtung. CS3-Symbole allein genügen nicht."
    )

    P[31]["before"] = (
        "Nur 60977 im bestätigten Märklin-Aufbau nach [[10]]/1; 59649, Zug und Puffer getrennt. "
        "mDecoderTool3 verwenden, Altprojekt und Firmware sichern. Änderungen nie am verbundenen Zug."
    )
    table = _find(P[31], "table")
    for row in table["rows"]:
        if row[0] == "Innenlicht-Taste":
            row[1] = "Freie oder bewusst übernommene Taste dokumentieren; rastend = ein Druck ein, nächster Druck aus. Nicht automatisch F4/F6."
    for b in P[31]["blocks"]:
        if b.get("type") == "p" and b.get("text", "").startswith("<b>ESU hinten:"):
            b["text"] = (
                "<b>ESU hinten:</b> F0-Zuordnung aus [[14]] erhalten: vorwärts LV, rückwärts LR. Die Verdrahtung [[26]] "
                "kehrt die sichtbaren Farben um. Mapping bedeutet Zuordnung von Taste/Bedingung zu Ausgang. "
                "Nötige Mapping-/Dimmänderungen einzeln wie [[11]]–[[13]] exportieren, schreiben und rücklesen; "
                "CV191–195 sind keine Mappingwerte. Danach Paarprüfung wiederholen."
            )

    _find(P[44], "step", "1.")["text"] = (
        "Zug stromlos machen, Kopf vom Gleis und Bus trennen. Decoder an den Kanten abziehen. "
        "ESU auf die bestätigte Einzelaufnahme [[9]] setzen; Lesen/Ändern nach [[12]]/[[13]]. "
        "Märklin 60977 nach [[10]]/[[31]] bearbeiten. Die passende Aufnahme muss auch später erneut verfügbar sein."
    )
    _find(P[44], "step", "2.")["text"] = (
        "Altprojekt/Altwerte sichern, nur die begründete Änderung übertragen und frisch rücklesen. "
        "Eine fehlende Quittierung (ACK, Rückmeldung des Decoders) kann trotz ausgeführtem Schreiben auftreten. "
        "Die 150-Ω-Hilfe aus ESU-Unterlagen für andere Fx-micro-Modelle nicht auf 59649 übertragen."
    )
    return P
