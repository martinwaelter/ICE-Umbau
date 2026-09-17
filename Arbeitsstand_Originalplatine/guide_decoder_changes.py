"""Decoder-/Prüfweg für Originalplatine; Eingabe: finale REV13-Karten vor Umnummerierung."""

BASE = '/Users/martinwaelter/ICE Umbau/'

def step(n, text):
    return {'type': 'step', 'label': f'{n}.', 'text': text}

def note(label, text, tone='info'):
    return {'type': 'note', 'label': label, 'text': text, 'tone': tone}

def table(headers, rows, widths=None):
    d = {'type': 'table', 'headers': headers, 'rows': rows}
    if widths: d['widths'] = widths
    return d

def setpage(P, n, title, goal, before, blocks, check, sources):
    p = next(x for x in P if x['n'] == n)
    p.update(title=title, goal=goal, before=before, blocks=blocks, check=check, sources=sources)

def apply(P):
    setpage(P, 8, 'Prüfaufbau mit den endgültigen Trägern',
        '60977 ist der Sound-Master, 59649 der folgende Gegenkopf-Decoder. Du verwendest die endgültigen Träger und den geprüften HLA; zwei 60970 sind keine Voraussetzung.',
        '60972/60982 vorhanden; 60977 bestellt; 59649 bisher geplant. Vor Decoderstrom die tatsächlich benötigten Teile bereitlegen. Motorumbau und Isolation [[15]]–[[18]] bereits ausgeführt.', [
        table(['Teil', 'Verwendung'], [
            ['Träger aus 60977', 'Vorn mit 60977; Original-Lautsprecherbuchse.'],
            ['Träger aus 60972', 'Hinten mit 59649. Der 60972 selbst bleibt unbenutzt.'],
            ['Ein geprüfter 60941-Motor', 'Vorübergehend nur am ESU für DCC-Quittierung; beim Licht-Paartest vollständig getrennt.'],
            ['Vier begrenzte Lichtzweige', 'Vorgesehene Frontmodule mit je eigenem Widerstand pro Farbe nach [[20]]; sichtbar mit Kopf/LV/LR markieren.']
        ], [1.1, 3.0]),
        step(1, 'Beide leeren Märklin-Träger mit den Herstelleransichten abgleichen: Index, B/GR, 0/GL, +Ub, LV/LR und MR/MV. Auf trockener isolierender Unterlage fixieren. Keine alte Fahrzeugschaltung oder Kupplungsleitung an diese Prüfverschaltung anschließen.'),
        step(2, 'Beschriftete, isolierte Prüfleitungen vorbereiten. B/GR ist Rot zum CS3-B-Anschluss, 0/GL ist Braun zum CS3-0-Anschluss. Einzelpfade und späteren B/0-Verteiler vor Anschluss an Decoder/Quelle nach [[6]] prüfen: B-Pfade durchgängig, 0-Pfade durchgängig, B gegen 0 offen.'),
        step(3, 'Märklin-Projekt nach [[10]] sichern. CS3-Anmeldung: nur 60977 auf seinem Träger, Motor offen. ESU-Lesen/Schreiben: nur 59649 mit vorübergehend angeschlossenem HLA nach [[12]]/[[13]]. Paartest [[14]]: beide Träger mit eigenen Lichtzweigen, beide Motoranschlüsse offen.'),
        note('QUELLENWECHSEL', 'Immer STOP, ausschalten und den Quellenstecker physisch abziehen. Nie USB/60971, Programmier- und Betriebsausgang zugleich verbinden. Beim DCC-Service erreicht jeder Befehl jeden angeschlossenen Decoder.'),
        step(4, 'Der HLA bleibt mechanisch sicher befestigt; Räder/Getriebe müssen frei beweglich sein. Die beiden Motorleitungen dürfen immer nur an einem Decoder hängen. Ein eigener, isolationsgeprüfter Motor ist eine reale Last; erst fehlerfreies frisches CV-Lesen bestätigt den konkreten Quittierungsweg.'),
        note('SPÄTER ERNEUT NUTZBAR', 'Träger, Motor-Serviceverbindung und geprüfte Prüfleitungen zugänglich halten. So kann der motorlose ESU auch später einzeln mit HLA gelesen werden. Ein passender fertiger Prüfstand ist eine optionale Alternative, kein behaupteter Bestand.')
        ], 'Prüfaufbau und Lichtbegrenzung sind vorbereitet. Der Paarversuch folgt vor Wagenbus, Endmontage und Fahrabnahme.', ['Q1','Q6','Q8','Q17','Q39'])

    p10 = next(x for x in P if x['n'] == 10)
    p10['before'] = 'USB-Ablauf nur für bestätigten Märklin 60971. Zuerst Artikel ablesen. 60977 ist bestellt; die eigene Kennung wird erst am tatsächlich vorliegenden Decoder ermittelt.'
    p10['blocks'][1]['text'] = ('CS3-Version und mfx-Lokeintrag notieren. Für eine neue Anmeldung ausschließlich den 60977 auf seinem Originalträger nach [[8]] anschließen: B/GR an B, 0/GL an 0 des getrennten CS3-Betriebsausgangs. Beide Motoranschlüsse offen, Fahrstufe 0, Sound/F0 aus, Automatik aus. Anlage, Programmierausgang und 60971 physisch ab. STOP aufheben; anhand des allein angeschlossenen Decoders zuordnen. Danach STOP, ausschalten und Quelle trennen. Ein passender Lokname allein genügt nicht.')
    p10['sources'] = list(dict.fromkeys(p10['sources'] + ['Q39']))

    setpage(P, 12, 'ESU einzeln mit dem geprüften HLA lesen',
        'Der vorübergehend angeschlossene Motor ermöglicht eine reale DCC-Quittierung. Zwei frische Lesungen bestätigen erst den konkreten Aufbau.',
        'Motorisolation [[18]] bestanden; Prüfaufbau [[8]] vorbereitet. Alle Quellen ab, beide Decoder zunächst abgezogen. 60977 bleibt vollständig getrennt.', [
        step(1, 'Beide Motoradern am vorderen 60977-Träger physisch trennen. Den vollständigen HLA-/Drosselzweig mit zwei geprüften isolierten Prüfverbindungen ausschließlich an MV/Grün und MR/Blau des hinteren Märklin-Trägers anschließen. Motorisolation mit diesen Verbindungen und ohne Decoder erneut prüfen. Räder frei, Kopf gegen Wegrollen sichern. Dann nur 59649 korrekt aufstecken.'),
        step(2, 'Vor erstem ESU-Strom Lokliste fotografieren. Manuellen DCC-Eintrag „SERVICE ESU59649 – nicht fahren“ vorbereiten. „Bearbeiten > Loks bearbeiten“, Serviceeintrag, „Konfigurieren“; Programmiergleis wählen, nicht PoM. Fehlende CV-Zeilen ohne Versorgung vorbereiten. Die Serviceadresse ändert keine Decoderadresse. „Decoder auslesen“ liest frisch; angezeigte Altwerte sind kein neuer Nachweis.'),
        step(3, 'CS3 ausschalten. Nur ESU-Träger B/GR an B und 0/GL an 0 des vollständig getrennten Programmiergleisausgangs anschließen. Betriebsausgang, Anlage, 60971 und 60977 bleiben ab. Sitz, Isolation und Motorpfad prüfen. Einschalten, Regler 0, F0 aus; GO nur zum Lesen. Eine mögliche neue M4-Anmeldung mit dem Vorherfoto vergleichen; nicht zusätzlich bedienen.'),
        step(4, 'CV8 ausschließlich lesen: Erwartung 151. Danach über „Decoder auslesen“ erneut frisch lesen. Beide Ergebnisse müssen fehlerfrei 151 sein. Das bestätigt Hersteller und Leseweg, nicht Artikel oder Firmware. Kurze Motorimpulse können Quittierungen begleiten; anhaltender Lauf, Wärme, Geruch oder Überlast: sofort STOP und physisch trennen.'),
        step(5, 'CV191–195 frisch lesen und sichern. Zusätzlich CV1, CV17, CV18, CV29 und CV47 nur lesen; Adresse/Protokolle und Lokliste erhalten. DCC-/MM-Adressen aus eigenem Projekt oder „unbekannt“ getrennt notieren. Nach Abschluss STOP, ausschalten und Quelle abziehen; die HLA-Prüfverschaltung bleibt für [[13]] erhalten.'),
        table(['Nachweis', 'Frisch gelesen'], [
            ['CV8 Lauf 1 / 2', '_____ / _____'],
            ['CV191 / 192 / 193 / 194 / 195', '_____ / _____ / _____ / _____ / _____'],
            ['CV1 / 17 / 18 / 29 / 47', '_____ / _____ / _____ / _____ / _____']
        ], [1.4,1.8]),
        note('KEINE SCHREIBBEFEHLE', 'CV8=8 wäre Reset; CV54=0/F1 wäre eine Einmessfolge. Beides unterlassen. Lesefehler: STOP und trennen, Anschluss/Isolation/Kontakte prüfen. Kein Lastwiderstand nach fremder Decoderanleitung und kein blindes Wiederholen.', 'stop')
        ], 'Zwei gültige CV8-Lesungen und reale Altwerte liegen vor. Spätere ESU-Servicearbeiten benutzen wieder genau diesen getrennten HLA-Aufbau.', ['Q6','Q9','Q17','Q26','Q39'])

    setpage(P, 14, 'Beide Träger: gemeinsames Frontlicht nachweisen',
        'Nur ein mfx-Zugeintrag muss beide realen Frontmodule steuern. Geprüft wird nach Motorumbau und vor Wagenbus/Endmontage.',
        '[[13]] bestanden; vier begrenzte Lichtzweige nach [[20]]. Beide Quellenanschlüsse ab, Automatik aus, Fahrstufe 0. Keine Traktion.', [
        step(1, 'Stromlos 59649 abziehen, beide HLA-Prüfverbindungen vom hinteren Träger entfernen; MR/MV einzeln isolieren. HLA auch vom 60977 getrennt lassen. Anschluss-/Sichtprüfung, dann 59649 wieder einsetzen. Für diesen F0-Test bleiben beide Motorausgänge frei. Vorn +Ub/LV/LR an Plus/Weiß/Rot, hinten an Plus/Rot/Weiß; jeder Farbzweig mit eigenem Widerstand.'),
        step(2, 'Zunächst nur 60977 auf seinem Träger am getrennten CS3-Betriebsausgang anschließen, STOP aufheben; F0/Richtung prüfen. STOP, ausschalten, Quelle physisch abziehen. Geprüften Verteiler [[8]] ergänzen: beide B/GR auf B, beide 0/GL auf 0. Nur Gleiseingänge parallel; U+, Motor-, Licht-, AUX- und Lautsprecheranschlüsse bleiben getrennt. Wieder anschließen und STOP aufheben.'),
        step(3, 'Nur den eindeutig als mfx geführten 60977-Mastereintrag bedienen. Tabelle vollständig prüfen und mindestens fünf Richtungswechsel bei Fahrstufe 0 durchführen. Physische Farben beobachten; CS3-Symbole genügen nicht. Serviceeinträge bleiben unbedient, Sound aus.'),
        table(['F0 / Richtung', '60977 vorn', '59649 hinten'], [
            ['aus / beide Richtungen', 'dunkel','dunkel'],
            ['an / vorwärts','weiß','rot'],
            ['an / rückwärts','rot','weiß']
        ], [1.5,1,1]),
        step(4, 'Beide Träger gemeinsam ausschalten, wieder einschalten und ganze Tabelle wiederholen. Nur mit geeigneten getrennt schaltbaren Gleiseingängen zusätzlich Master zuerst und ESU zuerst prüfen. Sonst beide erweiterten Startfolgen als ungeprüft kennzeichnen; keine offenen Kontakte unter Strom umstecken.'),
        step(5, 'Lokliste mit dem Vorherfoto vergleichen. Eine alte gespeicherte ESU-Zeile allein ist kein Fehler; aktive eigenständige Anmeldung oder Reaktion auf einen anderen Bedienweg klären. Kein Konfigurationsfenster im verbundenen Paar öffnen. Nach dem Test STOP, ausschalten und physisch trennen.'),
        note('BEI FEHLER', 'Kennung, persönlichen Export, frische Rücklesewerte, mfx-Bedienweg und reale Ausgänge abgleichen. Nur nach begründet korrigierter Ursache erneut prüfen. Bleibt der gültige Versuch negativ, Nachweise an ESU oder gezielte Diagnose mit geliehenem 53451; noch keinen Wagenbus/Endaufbau verbinden.', 'stop'),
        note('ZENTRALENWECHSEL SEPARAT', 'Eigene CS3-Abnahme beweist keinen SID-Wechsel. Dafür gleiche mfxuid und tatsächlich andere SID am anderen System belegen. Ohne dieses System „Zentralenwechsel nicht geprüft“. Keine produktiven Lokdaten löschen und keinen Reset erzwingen.')
        ], 'F0/Farben, gemeinsamer Neustart und mfx-Bedienweg bestanden. Erst danach Motorzweig stromlos wieder ausschließlich an 60977 anschließen und betroffene Anschlussprüfungen wiederholen.', ['Q1','Q6','Q7','Q15','Q17','Q39'])

    setpage(P, 24, 'Satzlautsprecher direkt am Originalträger',
        'Ein Lautsprecher aus dem 60977-Satz wird mit unverändertem Stecker an dessen eigenen Märklin-Träger angeschlossen.',
        '60977 abgezogen; Gleis, Puffer und andere Quellen getrennt. Originalträger aus dem 60977-Satz eindeutig zugeordnet.', [
        {'type':'figure','path':BASE+'Arbeitsstand_REV11/zeichnungsquellen/maerklin_60977_600dpi-005.png','maxh':235,'crop':[0.035,0.20,0.49,0.72]},
        {'type':'small','text':'Märklin-Originalzeichnung S. 5. Zweipolige Lautsprecherbuchse anhand Symbol zuordnen; die vierpolige SUSI-Buchse ist ein anderer Anschluss.'},
        step(1, 'Genau einen unveränderten Satzlautsprecher wählen, der druckfrei passt. Satzherkunft und Bauform dokumentieren. 60977: 1,6 W an 8 Ω, 2,75 W an 4 Ω; diese Werte bestimmen nicht die Impedanz des konkreten Satzlautsprechers. Bei Ersatz gelten dessen Nennimpedanz und Belastbarkeit. Aus einem Ohmwert keine Impedanz erraten.'),
        step(2, 'Leitungen, Originalstecker und Buchse ansehen. Gehäuseform und Kontaktzahl müssen passen. Unveränderten Stecker gerade in die dafür vorgesehene zweipolige Buchse führen; nicht am Kabel ziehen und nicht mit Kraft auf die SUSI-Buchse drücken. Bei abweichender Ausführung genau dieses Teil identifizieren.'),
        step(3, 'Schallkapsel sicher befestigen, Membran frei lassen. Leitungen zugentlasten; sie dürfen weder Drehgestell noch Kupplung berühren. Dachraum mit realem Lautsprecher und Decoder prüfen. Erster leiser Soundtest erst bei Einzelprüfung [[36]].'),
        note('ENTFÄLLT', 'Die ursprüngliche LoDi-Adapterkette wird nicht gebraucht: kein neu zu bestimmender Gegenstecker und keine Lötung an LS1/LS2. Der Originalstecker bleibt erhalten.'),
        note('NUR LAUTSPRECHERPFAD', 'Keine Lautsprecherader an Chassis, U+, GND oder +5V. Keinen zweiten Lautsprecher parallel anschließen. Am 59649 hinten bleiben Lautsprecher- und SUSI-Buchse frei.', 'stop'),
        {'type':'p','text':'Satz/Bauform ______; passende Buchse ______; Stecker/Kabel unbeschädigt ______; freie Membran/Dachraum ______; späterer leiser Test ______.'}
        ], 'Ein Satzlautsprecher sitzt mechanisch frei und am vorgesehenen Originalanschluss. Sound bleibt bis zum Einzeltest aus.', ['Q1'])

    setpage(P, 25, 'Gegenkopf: Träger aus dem 60972-Satz',
        'Der 59649 erhält den vorhandenen originalen Märklin-Träger aus dem 60972-Satz. Der 60977 behält seinen eigenen Träger vorn.',
        'Alle Quellen getrennt, Decoder und Puffer ab. Träger, Halteplatte und Schraube des vorhandenen 60972-Satzes tatsächlich bereitlegen.', [
        {'type':'figure','path':BASE+'Arbeitsstand_Originalplatine/maerklin_60972_p6.png','maxh':240,'crop':[0.045,0.235,0.495,0.705]},
        {'type':'small','text':'Märklin 60972-Anleitung S. 6: beschrifteter Originalträger. Die Zeichnung zeigt SUSI und eine zweipolige Buchse mit Lautsprechersymbol; hinten bleiben beide frei.'},
        step(1, 'Alte Leiterplatte und Anschlüsse fotografieren. Schleifer/Radkontakte getrennt verfolgen. Originalplatine erhalten; nur bestätigte passive Netze weiterverwenden. Die neue Aufnahme nicht allein an alten Lampenfedern, Litzen oder unbekannten Stützen befestigen.'),
        step(2, 'Original-Halteplatte, Träger, tatsächlichen 59649 und beide LED-Widerstände trocken positionieren. Freie Unterseite, Dachhöhe, Wärmeabstand, Drehgestelle und Kupplungen prüfen. Nichts bohren oder alte Stützen verbiegen. Fehlt ein passender Sitz, isolierende Halterung nach den realen Maßen festlegen.'),
        table(['Trägeraufdruck','Hinten verwenden'], [
            ['B/GR; 0/GL','Schleifer/RT; örtlicher Radkontakt nach [[26]].'],
            ['+Ub; LV; LR','LED-Plus; Rot mit Widerstand; Weiß mit Widerstand.'],
            ['MR/MV','Nur vorübergehend HLA bei [[12]]; im Endaufbau einzeln isolieren.'],
            ['AUX1–4, GND, +5V','Nicht anschließen; vorhandene freie Litzen einzeln isolieren.'],
            ['SUSI-/Lautsprecherbuchse','Frei lassen; keine Brücke, kein 60974 am ESU.']
        ], [1.15,2.9]),
        step(3, 'Befestigungsort, Halter, Schraube/Schaftlänge und obere/untere Freiräume dokumentieren. Litzen tragen weder Decoder noch Träger. Neue Verbindungen sowie Montage vor/nach Befestigung nach [[6]]/[[7]] prüfen. Absichtliche Radmasse an 0/GL ist kein Isolationsfehler.'),
        note('REALEN TRÄGER ABGLEICHEN', 'Die Herstellerbilder belegen passende Grundanschlüsse, keine identische Ersatzteilnummer aller Lieferrevisionen. Abweichende Bauteile/Aufdrucke gezielt identifizieren. Ein 21MTC-Sockel mit fremden Zusatzverstärkern ist kein pauschaler Ersatz.')
        ], 'Träger aus 60972 ist zugeordnet und mechanisch sicher. 59649 für alle Montage-/Lötprüfungen abgezogen lassen.', ['Q1','Q6','Q8','Q39'])

    setpage(P, 31, '60977: Motor, Sound und Innenlicht-Relais',
        'Der bestellte 60977 bleibt der Sounddecoder vorn. AUX1 steuert ausschließlich das geplante Innenlicht-Relais; Motor- und Soundeinstellungen bleiben getrennte Aufgaben.',
        'Nur 60977 am bestätigten 60971 nach [[10]]/1. Zug, 59649, Trägerlasten und Puffer getrennt. mDecoderTool3, Altprojekt und Firmware sichern.', [
        table(['Einstellung','Soll'], [
            ['Motor','Vollständiger geprüfter 60941: HLA/C90, CV52=3; frisch rücklesen.'],
            ['Frontlicht','F0 vorwärts = LV/Weiß; rückwärts = LR/Rot.'],
            ['Innenlicht','Physischer Ausgang AUX1; dieser schaltet die geeignete Relaisspule, nicht unmittelbar die Wagenlast.'],
            ['Ausgangsbetrieb','Dauerhaft eingeschaltet solange die gewählte Taste an ist; volle Ausgangsstärke. Keine Dimmung, kein Blinken, kein Timer und keine Kuppler-Abschaltung für die Relaisspule.'],
            ['Funktionstaste','Bewusst freie/übernommene Taste dokumentieren; rastend, beide Richtungen, Stand und Fahrt. AUX1 ist keine Tastennummer.']
        ], [1.0,3.35]),
        step(1, 'Passendes ICE-Soundprojekt im Märklin-Werkzeug öffnen. Quelle, Version und Funktionstasten sichern; niedrige Anfangslautstärke wählen, mfx aktiv lassen. Unter neuem Namen speichern und übertragen; Einstellungen anschließend erneut auslesen. Das bloße Auslesen sichert keine Sounds: Original-Soundprojekt zusätzlich aufbewahren.'),
        step(2, 'AUX1 genau dieser Innenlichttaste zuordnen. Dimmer-Modus 1 bei voller Ausgangsstärke verwenden; Bedingung 0 beziehungsweise keine zusätzliche Richtungs-/Bewegungsbedingung. Kein anderer Auslöser darf AUX1 ansteuern, besonders nicht F0, Fahrmotor oder eine zusätzliche Soundtaste. Volle Ausgangsstärke ist für die Spule vorgesehen; keine Helligkeitsregelung am Relais.'),
        step(3, 'AUX1 ist ein verstärkter Ausgang. Die alte LoDi-Jumperwahl AUX4/AUX1 entfällt; für dieses AUX1-Konzept keinen vorsorglichen CV51-Bit4-Eingriff ausführen. Motorumkehr über CV51 Bit0 ist ein eigener Diagnosefall auf [[36]]; nicht pauschal CV51=0 schreiben.'),
        {'type':'p','text':'<b>ESU hinten:</b> F0 vorwärts LV, rückwärts LR erhalten. Die Verdrahtung kehrt die sichtbaren Farben um. Nötige Mapping-/Dimmänderungen einzeln wie [[11]]–[[13]] mit persönlichem Export und Rücklesen ausführen. CV191–195 sind keine Mappingwerte. Danach Paarprüfung [[14]] wiederholen.'},
        note('GETRENNTE VORGÄNGE', 'Keine Einmessfahrt: CV7/Firmware-Feld nie auf 77 setzen. ESU nicht am Märklin 60971 verwenden. Reset und Pufferparameter gehören nicht zu dieser Konfiguration. Nach jedem späteren Soundprojekttransfer Ausgang, Taste und Bedingungen erneut prüfen.', 'stop'),
        {'type':'p','text':'Projekt ______; CV52 gelesen ______; AUX1/Taste ______; Relaisbetrieb ohne Dimmung ______; letzte Übertragung ______. Spule, Schutzbeschaltung, Kontaktlast und richtungsunabhängiges Schalten separat nach dem Verdrahtungsplan abnehmen.'}
        ], 'Motor, Sound, F0 und AUX1 sind gesichert. Relais-Schalt-/Lastabnahme folgt erst am fertig geprüften Aufbau.', ['Q1','Q6','Q10'])

    setpage(P, 34, 'Vorn: 60977 auf seinen Märklin-Träger setzen',
        'Der 60977 gehört auf den Träger aus seinem eigenen Satz. Die LoDi-Steckmerkmale entfallen.',
        'Einbau: Voraussetzungen [[33]] für Motorseite erfüllt. Früher Prüfaufbau: [[8]] und dessen passive Prüfungen erfüllt. In beiden Fällen alle Quellen/Puffer physisch ab.', [
        {'type':'figure','path':BASE+'Arbeitsstand_REV11/zeichnungsquellen/maerklin_60977_600dpi-006.png','maxh':275,'crop':[0.065,0.205,0.385,0.91]},
        {'type':'small','text':'Märklin-Originalzeichnung S. 6: kompakte Stecklage. Die Pins treten von unten durch die Decoderplatine; die schwarze Decoderbuchse bleibt oben.'},
        step(1, 'Trägerherkunft und Anschlüsse nach [[23]] abgleichen. SUSI-/Lautsprecherbuchsen liegen auf einer Seite der Stiftleiste, die freie Decoderfläche auf der anderen. Keine Orientierung nach LoDi-K1 oder einer hellen Fläche verwenden.'),
        step(2, '60977 an den Platinenkanten halten. Fehlende Stiftposition und geschlossene Indexposition 11 am echten Exemplar ansehen. Beide Reihen deckungsgleich ausrichten; langer Decoderkörper über der freien Trägerfläche, weg von den Zusatzbuchsen. Keine verdeckte Fehlstelle erraten.'),
        step(3, 'Parallel im Bereich der Steckleiste gleichmäßig nach unten setzen. Nicht auf Chips drücken. Bei Widerstand abheben und Versatz prüfen; keinen Pin biegen und keinen falschen Sitz mit Kraft korrigieren.'),
        step(4, 'Seitlich sämtliche eingeführten Stifte und parallelen Sitz prüfen. Keine Metallberührung, eingeklemmte Litze oder Belastung des freien Decoderendes. Tatsächlichen Dachraum kontrollieren. Einbau: danach Einzeltest [[36]]. Prüfaufbau: nur der ausdrücklich vorgesehene Schritt [[10]] oder [[14]].'),
        note('ABZIEHEN', 'Vor jedem Abziehen sämtliche Quellen und Puffer trennen; gleichmäßig an den Kanten abheben. Nicht mit Metall unterhebeln.', 'stop')
        ], 'Index, beide Reihen, seitlicher Sitz und Freiraum sind am realen Träger geprüft.', ['Q1','Q8'])

    setpage(P, 35, 'Hinten: 59649 auf den 60972-Träger setzen',
        'Der Gegenkopf verwendet den leeren originalen Märklin-Träger aus dem vorhandenen 60972-Satz.',
        'Einbau: [[33]] für Gegenkopf erfüllt. Prüfaufbau: [[8]]/[[12]] erfüllen. Alle Quellen/Puffer ab; Decoderlage stets am wirklichen Träger prüfen.', [
        {'type':'figure','path':BASE+'Arbeitsstand_Originalplatine/maerklin_60972_p6.png','maxh':265,'crop':[0.53,0.205,0.92,0.91]},
        {'type':'small','text':'Märklin-Originalzeichnung 60972, S. 6: dieselbe gezeigte Steckmechanik. In dieser Aufnahme wird hier der ESU 59649 eingesetzt.'},
        step(1, 'Träger gemäß [[25]] zuordnen: Beschriftung +Ub/LV/LR/B/GR/0/GL prüfen. Die Herstellerzeichnung zeigt Zusatzbuchsen auf einer Seite und die freie Decoderfläche auf der anderen. Träger aus 60977 bleibt vorn.'),
        step(2, '59649 an den Kanten halten, schwarze Buchse nach oben. Langer Decoderkörper zeigt über die freie Trägerfläche. Fehlende Stiftposition und geschlossene Indexposition 11 sichtbar deckungsgleich setzen; Stifte treten von unten durch die Decoderplatine.'),
        step(3, 'Beide Reihen parallel ausrichten und gleichmäßig im Steckleistenbereich nach unten drücken. Bei Widerstand abheben und Versatz prüfen. Keine Pins biegen und keine unbekannte Struktur entfernen.'),
        step(4, 'Von der Seite jeden eingeführten Stift, geraden Sitz und Abstand zu Rahmen/Originalplatine prüfen. Beim endgültigen Einbau sind MR/MV und alle übrigen unbenutzten Adern einzeln isoliert; keine HLA-Prüfleitung darf zurückbleiben. Im ausdrücklich getrennten DCC-Prüfaufbau gilt nur [[12]].'),
        step(5, 'Dachraum und zugfreie Litzenführung prüfen. Einbau: danach [[37]]. Prüfaufbau: nur kontrolliertes Lesen [[12]]/[[13]] oder Lichtpaar [[14]]. Kein 60974, Lautsprecher oder Wagenlicht-Ausgang am hinteren Träger.'),
        note('WARTUNG', 'Alle Quellen trennen, Decoder gleichmäßig an den Kanten abheben; nicht mit Metall unterhebeln. DCC-Lesen später wieder mit dem geprüften HLA-Aufbau [[12]].', 'stop')
        ], 'Herstelleransicht, Index, beide Reihen und reale Freiräume stimmen; Prüf- und Endverdrahtung sind eindeutig getrennt.', ['Q6','Q8','Q39'])
    return P
