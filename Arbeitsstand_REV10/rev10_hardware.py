"""Gezielte REV10-Hardwarekorrekturen; keine technische Freigabe realer Teile.

Der Eingang ist die rekonstruierte REV9-Liste aus rev9_sections.json.
Nur die ausdrücklich zugewiesenen Abschnitte werden verändert. Abbildungen
und nicht betroffene Texte bleiben erhalten. apply() verändert die Liste
und gibt sie zusätzlich zurück.
"""

from copy import deepcopy
import re


WIDTH = 511.28

COVERED = {
    "R-01": "Karte 0a: ein getrennter Prüfbereich, genau eine Quelle; Signalwirkung und Kontaktgleis unterscheiden.",
    "R-02": "16c/16d: passive Einzeladern getrennt von bestückten Netzen; positive Kontaktkontrollen vor/nachher; keine pauschale OL-Freigabe.",
    "R-03": "12d: tatsächlichen hinteren Schleifer und Radkontakt nachweisen; konkrete B/GR-, 0/GL- und GE-Anschlussfolge.",
    "R-04": "12/12d: jede freie Trägerlitze sowie GE einzeln isolieren; Übernahme in Schnellanleitung erfolgt durch Hauptmodul.",
    "R-18": "12c: realen hinteren Halter nicht als vorhanden/passend behaupten; offene und spätere geschlossene Montageprüfung trennen.",
    "R-19": "16c/16d: jede betroffene Verbindung nach Löten, Befestigen oder Umlegen erneut prüfen; Baseline allein reicht nicht.",
    "R-22": "9a/16d: Normrollen und tatsächliche Leiterbahnzuordnung auseinanderhalten; revisions- und messgerätebezogenen Prüfplan verlangen.",
    "R-23": "8/9c/12b: reale Indexerkennung vor Stecken; unbekannte schwarze Struktur nicht als abziehbare Kappe behandeln.",
    "R-24": "8a/9a/16d: Relaisabwesenheit beweist SW/RT-Pfad nicht; tatsächliche Nicht-S-Variante und GE-Zuordnung offen nachweisen.",
    "R-46": "9a/16d: Front-VCC ist laut LoDi der LED-Plus-Anschluss; nicht interne 21MTC-Vcc an Pin 12; tatsächliche Zuordnung nicht als gemessen ausgeben.",
}

OFFEN = (
    "Tatsächliche LoDi-511-Revision, beschriftete Rückseite, SW/RT-Pfad, GE-Auswahl und Befestigungsring-Netze fehlen weiterhin als Hardwarebeleg.",
    "Die schwarze Struktur am 21MTC-Feld ist nicht als abnehmbare Schutzkappe identifiziert; reale Indexposition muss ohne Gewalt erkennbar sein.",
    "Hinterer Schleifer, originale Radmasseführung, Trägerhalter und isolierte Dreifachverbindung sind am realen 2976 noch nicht dokumentiert.",
    "16d ist eine auszufüllende Nachweiskarte, keine bereits ausführbare Messanweisung: Geräteparameter, zugängliche Messpunkte und zulässige Anzeigen fehlen.",
    "LED-Zweigparameter, Widerstandsauswahl, G0 und die reale Anlagen-/Prüfgleiskonfiguration werden durch diese Textkorrektur nicht freigegeben.",
)


def p(text, style="body"):
    return {"type": "p", "style": style, "text": text}


def table(rows, widths):
    assert abs(sum(widths) - WIDTH) < 0.001, widths
    assert rows and all(len(row) == len(widths) for row in rows)
    return {
        "type": "table",
        "widths": list(widths),
        "rows": [
            [cell if isinstance(cell, dict) else p(cell, "head" if i == 0 else "cell")
             for cell in row]
            for i, row in enumerate(rows)
        ],
    }


def warn(title, text):
    return {"type": "keep", "items": [table([
        [p(title, "head")], [p(text, "warn")],
    ], [WIDTH])]}


def source(label, url, note):
    return p('<a href="' + url + '" color="#354B65">' + label + '</a>. ' + note, "small")


LODI = source("LoDi: Motor WiB ICE-M(-S)",
              "https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/",
              "Hersteller-Anschlussnamen und Varianten; Einbaubeispiel 33701, kein Einzelnachweis des vorhandenen 2976.")
MARKLIN = source("Märklin: Nachrüstdecoder 60975/60976/60977",
                 "https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf",
                 "Einbauwarnungen, Anschlusszeichnung des Trägers und Erstprüfung. Nicht mit einer Messung am eigenen Träger gleichsetzen.")
RCN = source("RailCommunity: RCN-121, 21MTC",
             "https://normen.railcommunity.de/RCN-121.pdf",
             "08.12.2024; Tabelle 1 beschreibt Schnittstellenrollen, nicht die Leiterbahnen der konkreten LoDi-Platine.")


def _section(sections, title):
    matches = [s for s in sections if s["title"] == title]
    if len(matches) != 1:
        raise ValueError("Abschnitt nicht eindeutig: " + title)
    return matches[0]


def _replace(section, old, new):
    """Replace one exact text fragment anywhere inside a section's nodes."""
    count = 0

    def visit(node):
        nonlocal count
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "text" and isinstance(value, str) and old in value:
                    count += value.count(old)
                    node[key] = value.replace(old, new)
                elif isinstance(value, (dict, list)):
                    visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)

    visit(section["elements"])
    if count != 1:
        raise ValueError(f"Erwartete genau einen Treffer in {section['title']}: {count}: {old[:100]}")


def _before_sources(section, elements):
    index = next((i for i, item in enumerate(section["elements"])
                  if item.get("type") == "p" and item.get("style") == "small"
                  and re.match(r"^\d+\. (Märklin|LoDi|RailCommunity|ESU):", item.get("text", ""))),
                 len(section["elements"]))
    section["elements"][index:index] = elements


def _insert_after(sections, anchor, title, elements):
    if any(s["title"] == title for s in sections):
        raise ValueError("REV10-Ergänzung bereits vorhanden: " + title)
    index = sections.index(_section(sections, anchor))
    sections.insert(index + 1, {"title": title, "elements": elements})


def _card_0a():
    return [
        warn("Vorerst ausschließlich getrenntes Prüfgleis mit einer Quelle",
             "Der geplante RT-Bus verbindet beide Mittelschleifer elektrisch. Deshalb darf der ICE keinen Übergang zwischen verschiedenen Ausgängen, Stromkreisen oder anders versorgten Abschnitten überbrücken. Bis der Anlagenplan dazu geprüft ist, findet jeder erlaubte Vorab- und Ersttest nur auf einem physisch getrennten Prüfgleis bzw. einer bestätigten Decoder-Prüfaufnahme mit genau einer Quelle statt. Die beiden 60974 bleiben bei den ersten Tests ausgebaut/abgetrennt. G0 und die übrigen Voraussetzungen bleiben erforderlich."),
        p("<b>0a-1. Prüfbereich festlegen.</b> Nimm einen getrennten Gleisaufbau ohne Gleisverbindung zur Anlage. Lege die Enden so, dass ein Fahrzeug nicht auf die Anlage rollen kann. Länge, sichere Endbegrenzung und Testgeschwindigkeit müssen zum jeweiligen Test passen; ein kurzes Gleis ist keine Strecke für eine Einmessfahrt. Decoder-Vorabtests nach A-C erfolgen nur in den dort verlangten bestätigten Prüfaufnahmen."),
        p("<b>0a-2. Quellen ausschließen, bevor etwas verbunden wird.</b> CS3 auf STOP stellen, ausschalten und die Versorgungen trennen. Alle Speiseleitungen des Prüfgleises verfolgen. Es darf nur ein einziges Ausgangspaar angeschlossen werden: entweder der für den betreffenden Schritt vorgeschriebene CS3-Ausgang oder eine andere dort ausdrücklich bestätigte Prüfquelle. Anschlussbox, weiterer Booster, Programmiergerät und ein zweiter CS3-Ausgang dürfen nicht zusätzlich mit diesem Gleis verbunden sein. Auch ein ausgeschaltetes Zweitgerät wird physisch abgetrennt. B und 0 nur entsprechend der tatsächlichen CS3-/Gleis-Anleitung anschließen; keine Farbe allein als Beleg verwenden."),
        table([
            ["SOLL", "FEHLER: nicht einschalten"],
            ["Ein Ausgangspaar → genau ein getrennter Prüfbereich. Keine Verbindung zu einem zweiten Bereich.",
             "Vorderer Schleifer steht im Fahrstromkreis, hinterer im Programmiergleis oder anderen Boosterbereich; RT verbindet die Quellen."],
            ["Normale Kontaktgleismeldung ist identifiziert; Gleisspeisung bleibt unverändert.",
             "Eine Kontaktgleisbezeichnung wird als Beweis benutzt, dass dort nie Spannung abgeschaltet oder umgeschaltet wird."],
            ["CS3 veranlasst später einen digitalen Fahrbefehl bei unverändert gespeistem Gleis; gesonderter Anlagen-/Bremsnachweis folgt.",
             "Ein Signal-/Bremsmodul schaltet die Gleisspannung um oder ab, der ICE überbrückt die Trennstelle über beide Schleifer."],
        ], [255.64, 255.64]),
        p("<b>0a-3. Signale nach ihrer elektrischen Wirkung eintragen.</b> Du planst Märklin-Signale und digitale Bremsung durch die CS3, ohne stromlose Halteabschnitte. Das allein beweist noch keine Eignung. Im Anschlussplan prüfen: Ändert ausschließlich ein Digitalbefehl die Fahrstufe, oder beeinflusst ein Signal-/Bremsmodul die Spannung des Gleisabschnitts? LoDi unterscheidet genau diese Fälle. Eine ICE-M-S-Platine wird hier nicht automatisch als Ersatz vorgeschrieben; deren Einbau würde einen gesondert geprüften Aufbau erfordern. Bei unbekannter Wirkung bleibt der Anlagenbetrieb gesperrt, nicht die Dokumentation oder der bestätigte getrennte Prüfaufbau."),
        p("<b>0a-4. Freigabebereich aufschreiben.</b> Prüfgleis/Foto ______; verwendetes Gerät und genau ein Ausgang ______; alle übrigen Einspeisungen abgetrennt ______; keine Gleisverbindung zur Anlage ______; zulässiger Test und Begrenzung ______; geprüft durch/Datum ______. Vor jedem Quellenwechsel spannungslos trennen und die Kontrolle wiederholen. Ein bestandener Prüfgleistest gibt weder Boostergrenzen noch spätere Signalabschnitte frei."),
        deepcopy(LODI),
    ]


def _card_12d():
    return [
        warn("Hinten noch keinen Schleifer als vorhanden voraussetzen",
             "Die alten Fotos belegen den hinteren Mittelschleifer dieses 2976 nicht. Vor jeder Verdrahtung muss der tatsächliche motorlose Kopf dokumentiert werden. Fehlt sein eigener Schleifer oder die bestätigte Rückleitung, ist der ungekuppelte hintere Einzeltest aus 54 nicht möglich. Den fehlenden Nachweis weder durch ein Fremdmodellfoto noch durch eine zufällige Versorgung über RT ersetzen."),
        p("<b>12d-1. Hinten sicher spannungslos machen.</b> Außenansicht und Unterseite dürfen vor G0 fotografiert werden; für die Umbauarbeiten den Kopf erst nach G0 öffnen. Kopf von allen Wagen und dem Motortriebkopf abkuppeln, vom Gleis nehmen und auf eine nichtleitende Unterlage legen. 59649 und 60974 bleiben abgezogen; alle weiteren Prüf-/Versorgungsleitungen entfernen. Alte Leiterplatte, Lampenfassung und jeden Draht vor dem Ablöten von beiden Seiten fotografieren. Nicht allein nach Drahtfarben arbeiten."),
        p("<b>12d-2. Drei Funktionen am wirklichen Kopf unterscheiden.</b> Suche unten den metallischen Mittelschleifer zwischen den Rädern. Seine Leitung bis zum Anschluss verfolgen und mit S beschriften. Die Radstromaufnahme getrennt verfolgen und R nennen. Kupplungskontakte erst nach 14/14a eindeutig als RT und GE bestimmen; bei noch nicht nachgerüsteten leitenden Kupplungen gibt es diesen Pfad noch nicht. Einen Kontakt nicht RT nennen, nur weil eine rote Litze daran sitzt. Verlauf, Lötpunkte und mechanische Befestigung fotografieren."),
        p("<b>12d-3. Leitung und Kontakt nachweisen.</b> Wenn S beziehungsweise R für eine rein passive Prüfung sicher von alter Elektronik getrennt werden können, vorher den Anschluss markieren und fotografieren. Danach mit dem Ablauf aus 16c den zugehörigen Draht und die identifizierte passive Stromaufnahme prüfen: S muss zum tatsächlichen Schleifer führen, R zum tatsächlich benutzten leitenden Radkontakt. Je Messreihe Kontaktkontrollen an beiden Seiten ausführen und das Drehgestell vorsichtig bewegen. Sind alte Elektronik, Bauteile oder ein unbekannter Metallpfad noch angeschlossen, nicht einfach einen Piepton auswerten: erst deren Trennung oder einen fachkundigen Prüfplan nach 16d klären. Keine unbekannte Massefeder abschneiden."),
        table([
            ["Am hinteren Kopf", "Konkretes Ziel", "Was dort nicht hinkommt"],
            ["S vom eigenen Mittelschleifer und RT der Kupplung", "Gemeinsam an die Leitung des Trägeranschlusses B/GR; isolierter bestätigter Verbindungspunkt.", "GE, 0/GL, +Ub oder ein Lichtausgang."],
            ["R der eigenen Radstromaufnahme", "An 0/GL des Märklin-Trägers.", "+Ub, +5V oder Decoder-GND als vermeintliche Radmasse."],
            ["GE der Kupplung", "Endet hier einzeln isoliert. Kein hinterer Decoder-Ausgang daran.", "LV, LR, AUX1-AUX4, B/GR oder 0/GL."],
            ["LoDi 514 hinten", "Gemeinsames Plus an +Ub; Rot über eigenen geprüften Widerstand an LV; Weiß über eigenen geprüften Widerstand an LR.", "Alte Lampenfassung, Chassis, GND oder +5V als Plus-/Zwischenanschluss."],
        ], [118.0, 221.28, 172.0]),
        p("<b>12d-4. B/GR-Verbindung herstellen.</b> Erst nach G1, bestätigter Halterung 12c und eindeutigen S/RT/R-Pfaden arbeiten. Die konkrete Stelle für den Dreiwegverbund S–RT–B/GR mit Foto festlegen: alle drei Leiter müssen mechanisch sicher, getrennt von Metall und beweglichen Teilen, vollständig isolierbar sein. Ohne geeigneten Platz den Verbindungspunkt durch den Fachbetrieb festlegen lassen. Nicht drei Litzen auf ein zu kleines Pad pressen. Für eine bestätigte Lötverbindung vor dem Löten passende Schrumpfschläuche auffädeln, nur die nötige Länge abisolieren, alle Einzeldrähte bündeln/verzinnen und ohne Zug löten. Mit Lupe auf einzelne abstehende Drähtchen prüfen. Erst nach Anschlussprüfung die Verbindung vollständig umschließen; beim Schrumpfen Platine, LED und Kunststoff vor Hitze schützen."),
        p("<b>12d-5. R, Licht und freie Litzen nacheinander bearbeiten.</b> Zuerst die bestätigte R-Leitung an 0/GL anschließen. Dann die LED-Verbindungen nur mit den in 11/11a bestätigten Werten nach 12a herstellen. Altlicht elektrisch entfernen und nicht als Lötstütze weiterverwenden. Jede unbenutzte Trägerlitze MR, MV, AUX1 bis AUX4, GND und +5V einzeln isolieren, sofern sie als Litze vorhanden ist. Jeden Schrumpfschlauch so wählen und setzen, dass auch stirnseitig kein Draht hervorschaut und er nicht abrutschen kann. GE ebenfalls einzeln isolieren. Keine freien Enden zusammen in einen gemeinsamen Schlauch schieben. Freie SUSI- und Lautsprecherbuchse nicht beschalten; keine Kurzschlussbrücke einsetzen."),
        p("<b>12d-6. Vor dem Decoder noch einmal prüfen.</b> Bei jeder umgelegten oder neu gelöteten Leitung die betroffenen passiven Prüfungen aus 16c und den bestätigten Prüfplan für bestückte Netze aus 16d wiederholen. Beide Drehgestell-/Kupplungsendlagen ohne Zug an den Lötstellen erreichen. Lose Litzen nicht unter den Träger oder gegen Schrauben legen. Erst nach diesen Ergebnissen 59649 unmittelbar vor dem erlaubten Einzeltest nach 12b einsetzen. Eine Messung vor dem Löten ersetzt die Anschlussprüfung danach nicht."),
        p("Nachweis hinten: eigenes Schleiferfoto ______; S-Pfad ______; R-Kontakt/Rückleitung ______; RT/GE-Kontaktplan ______; isolierter S–RT–B/GR-Punkt ______; jede freie Litze und GE isoliert ______; Montage/Prüfprotokolle ______; geprüft durch/Datum ______.", "small"),
        deepcopy(MARKLIN), deepcopy(LODI),
    ]


def _card_16c():
    return [
        warn("Vor-Erststrom-Karte: nur wirklich passive, getrennte Leiter",
             "Diese Karte prüft einzelne Leitungen und eindeutig passive Kontaktstücke gegen unerwünschte Berührung. Sie ist für beide Triebköpfe abzuarbeiten, soweit solche Teile sicher separat zugänglich sind. Ein abgezogener Decoder macht die LoDi- oder Märklin-Platine nicht automatisch zu einem leeren Kabel. Sobald LEDs, Widerstände, Dioden, andere Bauteile oder unbekannte Leiterbahnen mit dem Prüfpunkt verbunden sind, gilt 16d. Keinen Bauteilpfad zum Erzwingen einer OL-Anzeige auftrennen."),
        p("<b>16c-1. Sicheren Messzustand herstellen.</b> Beide Köpfe von Wagen und Gleis abtrennen. Alle Strom-/Programmieranschlüsse entfernen, beide Decoder und beide 60974 abziehen. Vor Widerstandsmessungen Spannungsfreiheit einschließlich eventuell verbliebener Speicherbauteile nach dem bestätigten Prüfverfahren sicherstellen; Kondensatoren niemals mit Schraubendreher oder Draht kurzschließen. Messleitungen am Multimeter in COM und V/Ω stecken, nicht in A/mA. Gerät, Ohm-Bereich und Anzeige für offene Leitungen nach Kapitel 2 prüfen. Für diese Karte keine Hochspannungs-Isolationsmessung verwenden."),
        p("<b>16c-2. Genau eine isoliert prüfbare Leitung wählen.</b> Ihr beide Enden sind von Elektronik und allen anderen Leitungen abgetrennt; eine reine passive Kontaktstrecke darf nach eindeutiger Zuordnung einbezogen werden. Ein Ende heißt L1, das andere L2. Für den zu prüfenden Fremdleiter bzw. das Metallteil zwei blanke, miteinander leitend verbundene Kontaktstellen X1 und X2 bestimmen. Nicht voraussetzen, dass zwei verschiedene Metallteile des Kopfes miteinander verbunden sind. Rahmen, Schraube, Halter und fremde Litze deshalb bei Bedarf separat prüfen. Zugängliche Anschlussstellen nutzen; keine Isolierung mit Nadeln durchstechen."),
        p("<b>16c-3. Prüfkontakte befestigen.</b> Kleine isolierte Messklemmen so an L1/L2/X1/X2 setzen, dass sie keinen Nachbarpunkt berühren. Freie Metallspitzen dürfen nicht zwischen benachbarte Pads geraten. Den metallischen Kontakt nicht mit den Fingern überbrücken. Sind an einem Leiter keine zwei sicher zugänglichen Kontrollstellen vorhanden, ist diese Messreihe so nicht ausführbar: passende Messaufnahme oder eine dokumentierte Kontaktkontrolle vom Prüfenden vorgeben lassen, nicht die Gegenprobe auslassen."),
        table([
            ["Reihenfolge für jede Leitung/Fremdteil-Paarung", "Anzeige und Entscheidung"],
            ["1. L1 gegen L2 messen; Ergebnis notieren.", "Geschlossener passiver Pfad muss zum Leitungs-/Kontaktwiderstand und zuvor bestimmten Messleitungswert passen. Keine bloße Pieptonbewertung."],
            ["2. X1 gegen X2 messen, ohne die Klemmenlage zu verändern.", "Positiver Nachweis, dass die Kontakte auf demselben leitenden Metallteil sitzen. Bei OL auf Lack oder Kontaktfehler prüfen; noch kein Isolationstest gültig."],
            ["3. L1 gegen X1 messen; Hände weg von blanken Kontakten.", "Nur für diese tatsächlich getrennten passiven Leiter: offener Stromkreis/OL im dokumentierten Ohm-Bereich erwartet. Endlicher oder wechselnder Wert: nicht freigeben, Berührung und Messaufbau prüfen."],
            ["4. L1–L2 und X1–X2 erneut positiv prüfen.", "Beide Kontrollen müssen wieder passen. Scheitert eine, ist die vorangegangene OL-Messung ungültig; Ursache beseitigen und ganze Reihe neu beginnen."],
            ["5. Leitung bzw. Drehgestell spannungslos vorsichtig in beide zulässigen Endlagen bringen; Reihe 1–4 wiederholen.", "Kein Ziehen an Lötstellen. Ein wechselnder Kontakt ist ein Fehler; nicht nur die günstigste Stellung dokumentieren."],
        ], [266.0, 245.28]),
        p("<b>16c-4. Konkret an den Köpfen anwenden.</b> Vorn: freies Kabel zum LED-Plus, einzelne freie Licht-/Lautsprecherleitungen, RT/GE-Kabel und weitere neu verlegte Einzeladern im getrennten Zustand gegen Rahmen, Befestigungsteile und ihre jeweiligen Nachbaradern prüfen. Motorpfade zusätzlich vollständig nach 5a bis 7 prüfen. Hinten: freie Zuleitung zu LED-Plus, Rot/Weiß-Leitungen, S/RT- und R-Kabel sowie GE im getrennten Zustand prüfen. Eine schon an +Ub, VCC oder einem anderen Platinenpad hängende Ader gehört nicht mehr zu diesem passiven Test. Absichtliche Radmassekontakte dürfen nicht als zu isolierende Fehler definiert werden."),
        p("<b>16c-5. Freie Enden und Gültigkeit abschließen.</b> Jede nicht benutzte Trägerlitze und GE hinten einzeln isolieren, dann optisch prüfen und vorsichtig auf sicheren Sitz des Schlauchs kontrollieren. Versiegelte Enden nicht zur Messung wieder aufstechen. Angeschlossene freie Trägerlitzen werden zusätzlich nur nach 16d elektrisch bewertet. Nach Löten, Befestigen, Umlegen oder Ersatz einer Leitung alle dadurch betroffenen Prüfungen wiederholen; eine alte Messreihe nicht ungeprüft übernehmen."),
        p("Pro Messreihe notieren: Kopf ______; Leitung/Fotos von L1/L2 ______; Fremdteil/X1/X2 ______; vollständig passiv und getrennt ______; Gerät/Bereich ______; L- und X-Kontrollen vorher ______; Isolation/Bewegung ______; beide Kontrollen nachher ______; spätere Verbindung/zugehörige Karte 16d ______; geprüft durch/Datum ______. OL bedeutet nur: Das Gerät erkennt in diesem Aufbau keinen leitenden Pfad. Es bescheinigt keine Spannungsfestigkeit und keine Fehlerfreiheit des vollständigen Zuges.", "small"),
        deepcopy(MARKLIN),
    ]


def _card_16d():
    return [
        warn("Bestückte Elektronik: derzeit keine ausführbare Messfreigabe",
             "Für die tatsächlich vorhandenen Platinen fehlen noch die revisionsbezogene Netzzuteilung, geeignete zugängliche Messpunkte, Geräte-Prüfspannung/-strom und eine begründete Sollauswertung. Die folgende Karte benennt die zu schließenden Nachweise; sie ist keine Aufforderung, die Platinen jetzt auf Verdacht durchzumessen. Ohne ausgefüllten und fachkundig bestätigten Prüfplan nicht messen, keinen Decoder einsetzen und nicht bestromen. Eine fertig redigierte Anleitung oder vollständig gedruckte Tabelle ersetzt keines dieser realen Ergebnisse."),
        p("<b>16d-1. Herstellerrollen vom tatsächlichen Platinenpfad trennen.</b> Die Tabelle nennt die vorgesehene Funktion. Sie behauptet keine bereits gemessene direkte Verbindung zwischen einem LoDi-Pad und einem 21MTC-Pin. Zwischen den Punkten können Widerstände, Dioden oder andere Bauteile liegen. Ein niedriger Widerstand kann beabsichtigt sein; ein endlicher Wert ist nicht automatisch Kurzschluss. Umgekehrt beweist ein hoher Wert ohne sichere Kontaktkontrolle keine Isolation."),
        table([
            ["Konkreter Anschluss", "Vorgesehene Funktion", "Abgrenzung / noch benötigter Nachweis"],
            ["LoDi Front-VCC", "Gemeinsames Plus des LoDi-514-Frontmoduls laut LoDi.", "Nicht interne 21MTC-Vcc: Pin 12 ist eine andere Funktion. U+ liegt nach RCN-121 an Pin 16. Der tatsächliche LoDi-Pfad bleibt revisionsbezogen nachzuweisen."],
            ["LoDi MASSE / hinten 0/GL", "Rad-/Schienenrückleiter; Schnittstellenrolle Pin 21.", "Nicht Elektronik-GND an Pin 20. Absichtlich vorhandene Rad-/Rahmenkontakte nicht auf OL prüfen lassen."],
            ["LoDi SW und RT / hinten B/GR", "Mittelleiter-/Schleiferpfad; Schnittstellenrolle Pin 22.", "Beide Schleifer sollen im geprüften Nicht-S-Aufbau denselben RT-Pfad versorgen. Fehlendes Relais allein beweist diese Verbindung nicht."],
            ["LoDi GE", "Geschaltete Wagenbeleuchtung; AUX-Auswahl laut 8a.", "Ab V1.50 nur eine zulässige Auswahlbrücke. Ältere Variante und tatsächlicher Pfad gesondert bestätigen. Kein zweiter Ausgang hinten."],
            ["Hinten +Ub", "Gemeinsames LED-Plus am Märklin-Träger.", "Nicht +5V, GND, 0/GL oder Metallrahmen. Zwei Front-Farbzweige jeweils nach 11/12a strombegrenzt."],
            ["Hinten LV / LR", "LV versorgt über Widerstand Rot; LR über Widerstand Weiß.", "Schaltende Lichtausgänge, keine Radmasse. Diese Zuordnung setzt das festgelegte Mapping aus 12a voraus."],
            ["LoDi LS1 / LS2", "Beide Anschlüsse ausschließlich zum einen bestätigten Lautsprecheradapter.", "Keiner an Chassis, LED-Plus oder Radmasse. Über bestückte Netze keine pauschale OL-Auswertung."],
        ], [115.0, 177.0, 219.28]),
        p("<b>16d-2. Den Prüfauftrag mit genau diesen Fotos stellen.</b> LoDi-511-Vorder-/Rückseite mit lesbarer Revision und den Feldern SW, RT, GE, MASSE, VCC, L_WS/L_RT, Widerständen und Ring A/B; Märklin-Träger beidseitig mit B/GR, 0/GL, +Ub, LV/LR und Halterung; beide LoDi-514-Einsätze; Anschlusslage in beiden offenen Köpfen. Dazu Multimeter-Modell und Geräteanleitung sowie den genauen Zustand aller abgetrennten Teile angeben. Die Herstellerzuordnung kann LoDi bestätigen; die geeigneten Messpunkte und Auswertung muss der fachkundige Prüfende für den realen Aufbau festlegen."),
        p("<b>16d-3. Für jede Messung vorab sechs Felder ausfüllen lassen.</b> (1) Zwei auf den eigenen Fotos markierte, sicher zugängliche Messpunkte mit Anschlussnamen. (2) Alle angeschlossenen/abgetrennten Bauteile, Decoder und Puffer; Verfahren zum Nachweis der Spannungsfreiheit. (3) Sollpfad samt Bauteilen und Quelle der Zuordnung. (4) Geeignetes Messgerät, Modus, Prüfspannung/-strom und gegebenenfalls beide Messpolungen sowie zulässige Wartezeit. (5) Konkrete erwartete Anzeige bzw. begründeter Werte-/Verhaltensbereich und eindeutiges Abbruchkriterium. (6) Positive Kontaktkontrolle an beiden Messseiten vor und nach der Reihe, die selbst keine benachbarten Netze verbindet. Fehlt ein Feld, ist genau diese Messung nicht ausführbar."),
        table([
            ["Prüfbereich, keine Sollwerttabelle", "Was der reale Prüfplan unterscheiden muss"],
            ["Vorn: Front-VCC, L_WS/L_RT, GE, LS1/LS2, Motoranschlüsse und neu verlegte Leitungen", "Beabsichtigter Bauteilpfad gegenüber unbeabsichtigtem Kontakt zu Radmasse, Rahmen, Halter/Schrauben und benachbarten Netzen; für LED-Zweige wirksame Strombegrenzung nach 11a."],
            ["Vorn: SW/RT und beide Befestigungsringe", "Tatsächliche Nicht-S-Stromverbindung bzw. andere Variante; Ring-Netze und zulässige Montage nach 9. Eine Fotointerpretation ersetzt den elektrischen Nachweis nicht."],
            ["Hinten: B/GR, 0/GL, +Ub, LV/LR und angeschlossene freie Trägerlitzen", "S/RT/B/GR-Verbund richtig; 0/GL echte Radmasse; GE ohne hinteren Ausgang; LED-Plus nicht unerwünscht am Rahmen; unbenutzte Litzen einzeln isoliert."],
            ["Beide Köpfe vor/nach Montage, Bewegung oder nachträglichem Löten", "Gleicher dokumentierter Messzustand. Keine neue unerwünschte Verbindung; eine unveränderte Vorheranzeige ist allein kein Beleg, dass schon der Ausgangszustand richtig war."],
        ], [201.0, 310.28]),
        p("<b>16d-4. Nicht an engen 21MTC-Pins improvisieren.</b> Der Anfänger misst nur an den im bestätigten Plan bezeichneten sicher zugänglichen Lötpads/Kontaktaufnahmen. Falls ein Normpin als Referenz nötig ist, muss der Prüfende eine eindeutig zugeordnete, berührungssichere Aufnahme bereitstellen. Nicht selbst Pinpositionen nach Foto abzählen, mit einer freien Spitze zwischen Pins suchen oder ein Kabel direkt an Pin 12/16 anlöten. Keine unbekannte schwarze Abdeckung am Stecker entfernen."),
        p("<b>16d-5. Die elektrische Endprüfung im realen Montagezustand protokollieren.</b> Erst nach Bestätigung des Plans die beschriebenen Messungen ausführen. Decoder und Puffer bleiben für diese Widerstandsprüfungen entfernt; sonstige Restenergie muss sicher ausgeschlossen sein. Nach Löten, Schraubenmontage und Bewegung die betroffenen Reihen wiederholen. Abweichung → Versorgung weiterhin getrennt, Ursache eingrenzen, korrigieren und komplette betroffene Reihe wiederholen. Erst anschließend dürfen die Einsetzfolgen 9c/12b und der jeweils erlaubte offene Ersttest aus 17 folgen. Nach einem späteren Gehäuseeinbau folgt zusätzlich 24; diese spätere Prüfung wird nicht rückwirkend als schon bestanden eingetragen."),
        p("Realer Nachweis: Platinen/Revisionen ______; Fotos/Messpunkte ______; Netzzuteilung und Quelle ______; Geräteparameter/Sollauswertung ______; Kontaktkontrollen ______; LED-Strombegrenzung ______; Ergebnisse vor/nach Montage ______; offene Abweichungen ______; fachkundig geprüft durch/Datum ______. <b>Fehlende Angaben bleiben OFFEN. Dieser Dokumentstand erteilt keine Hardwarefreigabe.</b>", "small"),
        deepcopy(LODI), deepcopy(MARKLIN), deepcopy(RCN),
    ]


def apply(sections):
    s = _section(sections, "8. Die rote Motorplatine sicher zuordnen")
    _replace(s,
             "Hier kommt ausschließlich der Märklin 60977 hin. Sein langer Körper liegt über der freien hellen Fläche in Richtung K1, nicht über LS1/LS2. Die Decoderbuchse bleibt oben sichtbar; die Stifte gehen von unten durch den Decoder. Vollständige Einsetzfolge und Indexkontrolle: 9c.",
             "Hier ist der Märklin 60977 vorgesehen. Zielansicht: langer Körper zur hellen Fläche Richtung K1, Buchse sichtbar oben, Stifte von unten durch die Decoderplatine. Das Foto allein gibt die Stecklage nicht frei: tatsächlichen Index nach 9c bestätigen. Eine unbekannte schwarze Struktur nicht abziehen.")
    _replace(s,
             "Für das Innenlicht zählt nur die Jumperstellung der roten LoDi 511: lies sie nach 8a ab und notiere AUX4 oder AUX1.",
             "Für das Innenlicht gilt die bestätigte Revision/Zuordnung der roten LoDi 511 nach 8a; erst dann AUX4 oder AUX1 notieren.")
    _before_sources(s, [p("<b>K1 ist kein Varianten-Nachweis.</b> Das unbestückte Relaisfeld wird in diesem Umbau weder bestückt noch beschaltet. Aus dem fehlenden Relais allein folgt aber nicht, dass SW und RT auf deiner tatsächlichen Platine wie für die Nicht-S-Variante vorgesehen verbunden sind. Vor Verdrahtung diesen Pfad zusammen mit Revision und GE-Zuordnung nach 16d bestätigen. Bei unlesbarem 21MTC-Index gilt 9c; keine vermutete Schutzkappe entfernen.")])

    s = _section(sections, "8a. Deine LoDi-Jumper: ablesen, nicht umbauen")
    _replace(s,
             "Aufdruck und Layout mit Herstellerbeispiel abgleichen; bei bestätigter Übereinstimmung AUX4 notieren. Keine Brücke nachrüsten.",
             "Aufdruck/Layout dokumentieren und die AUX4→GE-Zuordnung für diese tatsächliche ältere Revision bestätigen lassen (16d). Erst nach diesem Nachweis AUX4 notieren. Keine Brücke nachrüsten.")
    _before_sources(s, [p("<b>Für deine rote Platine zusätzlich festhalten:</b> Artikel/Variante ______; Revision ______; tatsächlicher SW/RT-Pfad und Nachweis ______; GE-Ausgang und Nachweis ______. Die AUX4-Angabe der älteren Herstellerbeschreibung ist ein Anhaltspunkt, kein bereits gemessener V1.49-Pfad. Die V1.50-Jumperregel nur bei eindeutig dieser Ausführung verwenden. Weißes Wagen-SJ2 bleibt unverändert.")])

    s = _section(sections, "9. Platinenbefestigung: sichere Freigabe")
    _replace(s, "Gehäuse geschlossen / Bewegung ebenfalls geprüft", "Später ergänzen: Gehäuseprüfung nach 24 / Bewegung")
    _replace(s,
             "Falls LoDi die originale Schraubmontage für deine Revision nicht bestätigt: Dem Fachbetrieb die unveränderte Platine und das 2976-Chassis geben. Auftrag: Halterung mit isolierter Schraubenführung herstellen; Ring A/B vor Verdrahtung gegen den positiv geprüften Metallrahmen isoliert nachweisen, jeweils mit Vor-/Nachprobe. Danach Radmasse separat am MASSE-Pad anschließen. Nur eine Unterlegscheibe unter dem Schraubenkopf genügt nicht, wenn Schaft oder Unterseite weiter Kontakt haben. Keine unbekannten Halter kaufen oder die Platine aufbohren.",
             "Falls LoDi die originale Schraubmontage für deine Revision nicht bestätigt: Dem Fachbetrieb unveränderte Platine und 2976-Chassis geben. Auftrag: revisionsgeeigneten isolierenden Halter einschließlich Schraubenschaft-/Unterseiten-Abstand festlegen, zugleich notwendige elektrische Ring-/Masseverbindungen klären. Nur eine Unterlegscheibe unter dem Schraubenkopf genügt nicht, wenn Schaft oder Unterseite weiter unerwünscht Kontakt haben. Der Radanschluss erfolgt am bestätigten MASSE-Pad; keine unbekannte Ringfunktion ersatzlos isolieren. Vor/nach Montage die festgelegten Messungen nach 16d mit positiven Kontaktkontrollen ausführen. Nicht pauschal OL für jeden bestückten Ring verlangen. Keine unbekannten Halter kaufen oder Platine aufbohren.")
    _before_sources(s, [p("<b>Zwei getrennte Freigaben eintragen.</b> Jetzt: zulässige Befestigung und elektrische offene Montageprüfung nach 16c/16d. Später: Gehäuseprüfung nach 24. Das noch fehlende spätere Gehäuseergebnis darf nicht als bereits bestanden eingetragen werden; es ist keine Voraussetzung für das Fotografieren oder den ausdrücklich erlaubten offenen Test aus 17. Ein dokumentierter Vorherwert allein beweist weder richtige Netzzuteilung noch fehlerfreie Montage.")])

    s = _section(sections, "9a. Anschlussnamen: Motortriebkopf")
    _replace(s, "Nur bestätigter Rohstrompfad.", "Schleiferleitung an SW; tatsächlichen SW/RT-Pfad der vorhandenen Nicht-S-Platine zuvor nach 16d bestätigen.")
    _replace(s,
             "An diesen Front-VCC-Punkt kommt ausschließlich das bestätigte gemeinsame Plus des LoDi-514-Einsatzes. Kein Draht von dort zu MASSE oder Chassis.",
             "Gemeinsames Plus des LoDi-514-Einsatzes an dieses Front-VCC-Pad. Kein Draht zu MASSE/Chassis. Hier bedeutet VCC laut LoDi LED-Plus, nicht interne 21MTC-Vcc an Pin 12.")
    _replace(s,
             "Nach jedem Anschluss Sollpfad prüfen, nicht erst nach der gesamten Verdrahtung.",
             "Vor Anschluss freie Einzeladern nach 16c prüfen; nach jedem Anschluss die betroffenen Reihen des zuvor bestätigten Platinen-Prüfplans 16d ausführen. Kein unbekanntes Netz allein mit dem Piepton bewerten.")
    _before_sources(s, [p("<b>Konkrete Anschlussregel und Nachweisgrenze.</b> VCC am LoDi-Frontanschluss ist der vom Hersteller benannte gemeinsame LED-Plus-Anschluss. Deshalb wird dort nicht ersatzweise MASSE, GND oder +5V verwendet. Die RCN-121-Rolle U+ an Pin 16 erklärt die Abgrenzung zu Pin 12; sie belegt aber noch keine direkte Leiterbahn dieses Exemplars. Die sichere Zuordnung der realen Pads und die Endprüfung werden nach 16d abgeschlossen, bevor ein Decoder aufgesteckt wird.")])

    s = _section(sections, "9c. Vorn: Märklin 60977 auf LoDi 511 einsetzen")
    _replace(s, "M1-M3 erst unmittelbar vor Schritt 52 ausführen", "9c-1 bis 9c-3 erst unmittelbar vor Schritt 52 ausführen")
    _replace(s, "nach allen Löt-, Montage- und Widerstandsprüfungen", "nach bestätigter offener Montageprüfung 9 sowie den tatsächlich bestandenen Prüfungen 16c/16d")
    _replace(s, "Dorthin zeigt der lange Körper des 60977. Er liegt über dieser Fläche, nicht über dem Lautsprecherbereich.",
             "So ist der lange Körper vorgesehen, nicht über LS1/LS2. Am echten Index bestätigen; die freie Fläche allein beweist die Stecklage nicht.")
    _replace(s,
             "<b>M1. 60977 ausrichten.</b> Alle Versorgungen und der 60974 sind abgetrennt.",
             "<b>9c-1. 60977 ausrichten.</b> Kopf vom Gleis nehmen, alle Wagen/anderen Köpfe abkuppeln und alle Versorgungs-/Programmierleitungen physisch entfernen. Beide 60974 bleiben abgetrennt; Spannungsfreiheit nach bestätigtem Prüfplan sicherstellen.")
    _replace(s,
             "<b>M2. Fehlstelle vor dem Drücken abgleichen.</b> An der 21MTC-Stiftleiste fehlt genau die Indexposition 11; an der Decoderseite ist diese Position geschlossen.",
             "<b>9c-2. Fehlstelle vor dem Drücken abgleichen.</b> Die Norm verlangt die fehlende Stiftposition 11 und die dazu geschlossene Decoderposition. Beides am tatsächlichen 60977 und LoDi-Träger sichtbar identifizieren; das vorhandene Foto bestätigt diesen Abgleich noch nicht.")
    _replace(s, "<b>M3. Gerade aufstecken.</b>", "<b>9c-3. Gerade aufstecken.</b>")
    _before_sources(s, [warn("Am eigenen 21MTC-Feld ist eine schwarze Struktur nicht als Kappe identifiziert",
                             "Wenn die Fehlstelle deshalb nicht erkennbar ist: 60977 abgezogen lassen, Nahfotos der roten Platine von oben und schräg seitlich sowie beider Decoderseiten aufnehmen und LoDi die genaue Revision nennen. Erfragen, was das schwarze Teil ist und wie die Indexposition dieser Ausführung freiliegt. Nicht abziehen, heraushebeln, anbohren oder Stifte durchdrücken. Erst die eindeutige Identifikation erlaubt die oben beschriebene Steckkontrolle; ein Foto eines ähnlich aussehenden Trägers reicht nicht.")])

    s = _section(sections, "12. Märklin-Träger im motorlosen Kopf")
    _replace(s, "RT-Rohstrompfad mit hinterem Schleifer.", "Bestätigter RT-Rohstrompfad zusammen mit dem tatsächlich nachgewiesenen hinteren Schleifer; Handgriffe 12d.")
    _before_sources(s, [p("<b>Jetzt nicht aus der Tabelle allein verdrahten.</b> Zuerst reale Beschriftung mit dieser Zeichnung abgleichen, hinteren Schleifer und Radkontakt nach 12d-1 bis 12d-3 nachweisen und Halterung 12c bestätigen. Danach in der Anschlussfolge 12d B/GR, 0/GL und die begrenzten LED-Zweige verbinden. GE endet hinten einzeln isoliert; jede freie Trägerlitze ebenfalls einzeln isolieren. Der reale Zustand wird vor Einsetzen des 59649 nach 16c/16d geprüft.")])

    s = _section(sections, "12b. Hinten: ESU 59649 auf Märklin-Träger")
    _replace(s, "E1-E3 erst unmittelbar vor Schritt 54 ausführen, nach Halterprüfung 12c und allen Löt-/Widerstandsprüfungen.",
             "12b-1 bis 12b-3 erst unmittelbar vor Schritt 54 ausführen, nach offener Halterprüfung 12c, Anschlussfolge 12d und tatsächlich bestandenen Prüfungen 16c/16d.")
    _replace(s,
             "<b>E1. Träger hinlegen.</b> Richte den leeren Märklin-Träger",
             "<b>12b-1. Träger spannungslos ausrichten.</b> Kopf vom Gleis nehmen und von allen Wagen abkuppeln; alle Versorgungs-/Programmierleitungen und 60974 entfernen. Spannungsfreiheit nach bestätigtem Prüfplan sicherstellen. Richte den leeren Märklin-Träger")
    _replace(s, "<b>E2. 59649 halten.</b>", "<b>12b-2. 59649 halten.</b>")
    _replace(s,
             "<b>E3. Index und Sitz kontrollieren.</b> Geschlossene Indexposition 11 am Decoder genau über die fehlende Stiftposition legen.",
             "<b>12b-3. Index und Sitz kontrollieren.</b> Die geschlossene Indexposition 11 am tatsächlichen 59649 und die fehlende Stiftposition am tatsächlichen Träger sichtbar abgleichen und deckungsgleich halten. Ist eine Position verdeckt oder unklar, nicht einstecken: Nahfotos zur Identifizierung beschaffen. Keine unbekannte Kappe/Steckerstruktur entfernen.")

    s = _section(sections, "12c. Hinteren Märklin-Träger sicher halten")
    _replace(s,
             "Andere Pfade nur mit abgetrennten Lasten beziehungsweise dokumentiertem Vorherwert bewerten.",
             "Passive, vollständig getrennte Leiter nach 16c bewerten. Für bestückte Netze gilt ausschließlich der vorher bestätigte Prüfplan 16d; weder abgetrennte Lasten allein noch ein gleich gebliebener Vorherwert erlauben eine pauschale Freigabe.")
    _replace(s,
             "offene Kontrolle ______; geschlossene Prüfung 24 ______;",
             "jetzt: offene mechanische/elektrische Kontrolle ______; später separat: geschlossene Prüfung 24 ______;")
    _before_sources(s, [p("<b>Was hier offen bleibt.</b> Das Dokument bestätigt keine konkrete Halterpassung am vorhandenen Dummy. Die fehlende Fotodokumentation ist aber auch kein Beweis, dass der mitgelieferte Halter ungeeignet wäre. Zuerst tatsächliche Einbausituation aufnehmen und bestätigen; erst danach montieren. Für die offene Erstprüfung müssen die offenen Montage-/Messnachweise vorliegen. Die spätere geschlossene Prüfung wird separat ergänzt und nicht vorweggenommen.")])

    _insert_after(sections, "0. Diese Teile kommen an diese Stelle",
                  "0a. Anlagen-Eignung und getrenntes Prüfgleis", _card_0a())
    _insert_after(sections, "12c. Hinteren Märklin-Träger sicher halten",
                  "12d. Hinten: Stromaufnahme, Anschlüsse und Einzelisolation", _card_12d())
    _insert_after(sections, "16b. 60977: AUX4 muss verstärkt arbeiten",
                  "16c. Vor Erststrom: passive Leitungen beider Köpfe", _card_16c())
    _insert_after(sections, "16c. Vor Erststrom: passive Leitungen beider Köpfe",
                  "16d. Bestückte Netze: Nachweisplan vor der Messung", _card_16d())
    return sections
