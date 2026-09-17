"""REV13 Ablaufkorrekturen. Eingabeschlüssel/Verweise sind finale REV12-Seiten."""

SOURCES = [
    {
        'id': 'Q36',
        'title': 'Märklin CS3: vollständiges Handbuch 2017, GFP3 gedruckte S. 33; ergänzend zur aktuellen Kurzanleitung Q26, S. 26',
        'url': 'https://www.maerklin.de/fileadmin/media/produkte/pdfs/MANUAL_CS3_DE-EN_17-02.pdf',
    }
]

def p(t): return {'type': 'p', 'text': t}
def small(t): return {'type': 'small', 'text': t}
def step(n, t): return {'type': 'step', 'label': f'{n}.', 'text': t}
def note(t, label='STOPP', tone='stop'): return {'type': 'note', 'label': label, 'text': t, 'tone': tone}
def tab(head, rows, widths): return {'type': 'table', 'headers': head, 'rows': rows, 'widths': widths}
def page(n, title, phase, goal, before, blocks, check, sources):
    return dict(n=n, title=title, phase=phase, goal=goal, before=before, blocks=blocks, check=check, sources=sources, original_card=n)


def apply(P):
    P[1]['phase'] = 'Start | REV13'
    P[1]['blocks'][2]['rows'] = [
        ['Vorbereitung und eigene CS3-Paarprüfung', '[[2]]–[[12]]', 'Prüfabschnitt, Kupplungsbestand, Geräte und Decoderpaar geklärt'],
        ['Motor, Platinen und Fronten', '[[13]]–[[24]]', 'Motorprüfung, LED-Zweige, Montage und Verdrahtung'],
        ['Mittelwagen und Kupplungen', '[[25]]–[[28]]', 'Jeder Übergang und optionale Radkontakte'],
        ['Konfiguration und erste Einzelprüfungen', '[[29]]–[[36]]', 'Checkliste, Stecken, Erstkontrolle und Funktion in dieser Folge'],
        ['Bereich, Last und Zugprüfung', '[[38]]–[[39]]', 'Messung je Wagenstufe und T1–T9'],
        ['Gehäuse, Fehler, Ergänzungen, Quellen', '[[40]]–[[44]]', 'Geschlossene Endprüfung; spätere Puffer und Signalhalt'],
    ]
    P[1]['blocks'][2]['widths'] = [1.8, .9, 2.7]
    P[1]['blocks'][-2] = note('Bestätigt vorhanden: Multimeter, Märklin-Decoderprogrammer und CS3 mit laut Nutzer aktueller Firmware. Exakte Typen ablesen. Bestand eines freien Prüfabschnitts und zweier Prüfaufnahmen ist nicht bestätigt. [[45]] und [[6]] beschreiben den benötigten Aufbau.', 'DEINE AUSSTATTUNG', 'info')
    P[1]['blocks'][-1] = p('Zuerst Prüfumgebung [[45]], Kupplungen [[46]] und CS3-Paarprüfung [[12]] klären. Erst dann den Zug elektrisch umbauen. Herstellerklärung und gezieltes Ausleihen von Prüfmitteln benötigen keinen Händlerauftrag. Reale Geräte- und Bauteilnachweise bleiben an der jeweiligen Karte offen, bis sie tatsächlich vorliegen.')

    P[2]['blocks'][0]['rows'][3][2] = 'Eigene Ausführung und Anzahl; zwei getrennte Kontakte je Übergang zuerst nach [[46]] bestätigen.'
    P[2]['blocks'][3]['text'] = P[2]['blocks'][3]['text'].replace('REV12', 'REV13')
    P[2]['blocks'][4]['text'] = 'Geräte ablesen und fotografieren: CS3-Version/Netzteil ______; Multimeter-Modell/Handbuch ______; Märklin-Programmer-Artikel ______. Prüfaufnahmen nach [[6]] gezielt leihen oder beschaffen, wenn sie fehlen. Prüfabschnitt nach [[45]] vorbereiten.'
    P[2]['blocks'][5] = note('Kupplungsausführung zuerst auf [[46]] feststellen. E395640/E395660 und E374340/E374060 sind lediglich Vergleichskandidaten aus verwandten Modellen. Keine Passung oder Stromführung für deinen 2976 daraus ableiten.', 'KUPPLUNGEN', 'info')

    P[45] = page(45, 'Einen getrennten Prüfabschnitt vorbereiten', 'Vorbereitung | vor dem ersten Strom',
        '„Prüfgleis“ bedeutet hier einen eigenen, vollständig von der Anlage getrennten Aufbau. Eine leere Anlage erfüllt diese Bedingung nicht.',
        'CS3 STOP; alle Gleisstecker abgezogen. Gleise, Anschlussleitung, nichtleitende Unterlage und unbeleuchtete Endbegrenzungen bereitlegen.', [
        step(1, 'Geraden des vorhandenen passenden Gleissystems zusammenstecken. Länge nach Prüfling wählen: alle Räder und Schleifer vollständig auf dem Abschnitt; für Kleinstfahrt zusätzlich freier Auslauf. Für spätere Zugtests muss die ganze Zusammenstellung darauf passen. Nicht pauschal mit drei oder vier Gleisen planen.'),
        step(2, 'Gleis auf waagerechter, nichtleitender Fläche gegen Verrutschen sichern; Abrollen und Absturz begrenzen. Keine Schienen-, Mittelleiter- oder Kabelverbindung zur Anlage. Keine Weichen-/Signaldecoder, Beleuchtung, beleuchteten Prellböcke oder zweite Einspeisung anschließen.'),
        step(3, 'Anschluss nach Gleis- und CS3-Markierung: B an Mittelleiter, 0 an Schienen. Bei C-Gleis die Unterseitenmarkierung B/0 beachten. Nur freie passive Anschlussleitungen/Gleise nach [[3]]/[[4]] prüfen; bis dahin nicht bestromen. Beschrifteten Anschlussstecker fotografieren.'),
        tab(['Verwendung', 'Genau dieser CS3-Ausgang'], [
            ['DCC lesen/schreiben; erste Einzelkontrolle nach Decodereinbau', 'Programmiergleis; höchstens 1,5 A laut Q26. Nur der jeweilige einzelne Prüfling.'],
            ['Paar-, Licht-, Sound-, Fahr- und Wagenlasttests', 'Betriebsgleis; Anlage bleibt abgezogen. Die Lastabnahme folgt [[31]].'],
        ], [1.2, 1.7]),
        step(4, 'Den Abschnitt mit genau einem zweipoligen Stecker wahlweise an Programmier- oder Betriebsausgang anschließen. Vor jedem Wechsel STOP, Stecker vollständig abziehen, erst dann am anderen Ausgang einstecken. Keine gemeinsame 0-Verbindung und keine Umschaltung durch Überfahren einer Trennstelle.'),
        step(5, 'CS3-Netzteil am Typenschild identifizieren; Auswahl unter System → GFP3 → Einstellungen damit abgleichen. Diese Auswahl beeinflusst das Abschaltverhalten. „Max. 5 A“ am Betriebsausgang ist keine pauschale H0-Einstellung. Nur das für CS3 und H0 zugelassene Netzteil verwenden.'),
        note('Fehlt der getrennte Aufbau, bleiben Bestromung und Fahrversuche offen. Bestandsaufnahme, Softwarevorbereitung und passive Prüfungen können weitergehen. Ein ungeklärter Fehler am Programmierausgang darf nicht durch Wechsel zur stärkeren Quelle übergangen werden.'),
        small('Gleissystem/Länge ______; B/0-Foto ______; ohne Anlagenverbindung ______; CS3/Netzteil/gewählte Einstellung ______. GFP3-Daten: aktuelle Kurzanleitung Q26, S. 26; ältere Menüansicht Q36, S. 33.'),
    ], 'Die konkrete Prüfumgebung ist vorbereitet. Vor jedem Aufsetzen und Umstecken bleibt STOP gesetzt; Ausführung erst auf der zugehörigen Prüfkarte.', ['Q1', 'Q26', 'Q36'])

    P[46] = page(46, 'Kupplungsbestand vor dem Umbau prüfen', 'Vorbereitung | beide Köpfe und alle Wagen',
        'RT und GE brauchen an jedem Übergang zwei elektrisch getrennte Kontakte. Die Artikelnummer 2976 allein beweist diese Ausstattung nicht.',
        'Zug vollständig von allen Quellen getrennt. Noch keine Kabel auslöten oder abschneiden. Zugreihenfolge und beide Endorientierungen fotografieren.', [
        {'type': 'figure', 'kind': 'coupler', 'maxh': 130},
        small('Funktionsschema, kein Foto der eigenen Kupplung. RT/GE-Zuordnung wird erst anhand der tatsächlichen Kontakte gemessen.'),
        step(1, 'An beiden Köpfen und an beiden Enden jedes vorgesehenen Wagens Kupplung und Anschlussweg ansehen. Je Hälfte zwei getrennte leitende Kontaktflächen sowie deren getrennte Leitungen/Anschlüsse suchen. Je Übergang Partner, Orientierung und Kontaktansicht fotografieren.'),
        tab(['Übergang', 'Zwei Kontakte / getrennte Anschlüsse', 'Passung / Foto'], [
            ['Motorseite → erster Wagen', '________________', '________________'],
            ['Jeder weitere Wagenübergang', '________________', '________________'],
            ['Letzter Wagen → Gegenkopf', '________________', '________________'],
        ], [1.2, 1.4, 1]),
        step(2, 'Zusammenstecken und normale seitliche Auslenkung ohne Kraft prüfen: Rastung hält, Kontakte treffen sich, Leitungen werden weder gespannt noch gequetscht. Ohne erkennbare Verriegelung oder bei anderem Profil keine Verbindung erzwingen.'),
        step(3, 'Sind beide Enden eines Kontaktpfads bereits frei und rein passiv, Leitfähigkeit und Trennung nach [[3]]/[[4]] prüfen. Bei angeschlossener Elektronik keine OL-Messung durch die Schaltung verlangen. Anschlussweg anhand Aufdruck/Zeichnung klären; die vollständige Kreuzpfadprüfung folgt nach dem Freilegen auf [[26]].'),
        note('Nur ein Kontakt, kein Kontakt oder ungeklärter Anschlussweg: elektrischen Zugumbau aussetzen. Eine Nachrüstung braucht bestätigte Teile, Maße, Rastung, Beweglichkeit und zwei getrennte Strompfade. Kandidaten aus [[2]] sind noch keine Einbaufreigabe. Die CS3-Paarprüfung kann unabhängig vorbereitet werden.'),
        p('Bestandsentscheidung je Übergang: vorhanden/geklärt ______; Nachrüstung nötig ______; noch offen ______. Bei mehreren Wagen die Tabellenzeile je Übergang fortsetzen. Stromtragfähigkeit wird durch Sichtprüfung oder bloßen Durchgang nicht bewiesen.'),
    ], 'An sämtlichen Übergängen ist ein passender zweipoliger Anschluss vorhanden oder seine konkrete Nachrüstung geklärt. Erst zusammen mit bestandener CS3-Paarprüfung [[12]] beginnt der elektrische Umbau.', ['Q3', 'Q4'])

    P[30] = page(30, 'Erste Einzelprüfung und Lastabnahme planen', 'Vorbereitung der Inbetriebnahme | noch nicht einschalten',
        'Diese Karte legt die folgenden Prüfstufen fest. Ausgeführt wird erst nach Checkliste und korrekt eingesetzten Decodern auf [[35]]/[[36]].',
        'Prüfabschnitt [[45]] vorbereitet. Jetzt Kriterien lesen und dokumentieren; diese Karte gibt noch keinen Einschaltauftrag.', [
        tab(['60977: Herstellergrenze', 'Maximalwert'], [
            ['Motor dauernd', '1,1 A'], ['Jeder verstärkte Licht-/AUX-Ausgang', '250 mA'],
            ['Licht und AUX zusammen', '300 mA'], ['Gesamtlast', '1,6 A'],
        ], [2.5, 1]),
        step(1, 'Zuerst Checkliste [[32]] abschließen und Decoder nach [[33]]/[[34]] stecken. Jeder Kopf erhält seine erste Kontrolle einzeln am getrennten Programmiergleis, ohne Wagen/Puffer, Licht/Sound aus und Fahrstufe 0. Märklin verlangt diesen Ersttest ohne Gehäuse (Q1, S. 6).'),
        note('Die Quellenobergrenze 1,5 A ist kein 250-mA-Schutz für einen AUX. Die Decodergrenze 1,6 A beschreibt seine maximal zulässige Gesamtlast, keinen benötigten Mindeststrom. GFP3 zeigt Gesamtstrom; weder fehlende Abschaltung noch mfx-Anmeldung beweisen Isolation und richtige Zweigströme.', 'WAS DER ERSTTEST AUSSAGT', 'info'),
        step(2, 'Nach unauffälliger Einzelkontrolle folgt der ausdrücklich spannungsfreie Wechsel zum Betriebsausgang am selben freien Prüfabschnitt. Dort werden LED-Zweige, leiser Sound und Kleinstfahrt nach [[35]], danach der Gegenkopf und gemeinsame Fronttest nach [[36]] geprüft. Ungeklärte hintere LEDs bleiben lokal getrennt.'),
        step(3, 'Eine Abschaltung kann vom Fahrzeug, Anschluss oder von Quellengrenze/Netzteileinstellung kommen. Zeitpunkt, aktive Lasten und Meldung notieren, STOP und physisch trennen. Schon beim Aufsetzen oder ohne Fahrbefehl: Verdrahtung prüfen. Erst bei Motor-/Lastzuschaltung: auch Freilauf und Quelle untersuchen. Der Zeitpunkt allein bestimmt keine Ursache.'),
        note('Kein zweiter Versuch allein wegen vermuteter 1,5-A-Grenze. Erst nach belegter und korrigierter Ursache erneut prüfen; nicht zur stärkeren Quelle wechseln, um eine Abschaltung zu umgehen.'),
        step(4, 'Nach den Einzel-/Paarprüfungen Bereich [[38]] klären. Lastmesskarte [[31]] dann begleitend je Wagenstufe ausführen; T1–T8 nach [[37]]. Endgültige Wagenzahl benötigt höchste Helligkeit, gleichzeitig aktive Ausgänge, Sound, Motor und Einschaltlast. Niedrigere Kupplungs-/Litzen-/Platinengrenzen gehen vor.'),
        tab(['Dokumentieren', 'Ist / offen'], [
            ['Quelle/Netzteil; Motorseite/Gegenkopf Erstkontrolle', '________________'],
            ['Funktionstest; begründete Wagenstufe; Lastbeleg [[31]]', '________________'],
        ], [2.2, 1]),
    ], 'Prüfstufen sind geplant. Jetzt Checkliste [[32]], danach Stecken [[33]]/[[34]] und Einzelprüfungen [[35]]/[[36]] in dieser Reihenfolge.', ['Q1', 'Q3', 'Q6', 'Q26', 'Q36'])

    P[35]['title'] = 'Motorseite: Erstkontrolle und Funktionstest'
    P[35]['goal'] = 'Erstkontrolle am Programmiergleis; danach spannungsfrei zum Betriebsausgang wechseln und Licht, Sound und Kleinstfahrt prüfen.'
    P[35]['before'] = 'Checkliste [[32]], Motorprüfung und Stecklage [[33]] bestanden. Prüfabschnitt [[45]] und Stufen [[30]] vorbereitet. Gegenkopf/Wagen/Puffer getrennt; freie Kontakte isoliert.'
    P[35]['blocks'][0] = step(1, 'Nur Programmiergleisausgang an den freien Prüfabschnitt anschließen; Betriebsgleisstecker ab. Automatik aus, Fahrstufe 0, F0/Sound aus. Unter System → GFP3 → Daten den Leerwert ohne Fahrzeug notieren (Q26, S. 26).')
    P[35]['blocks'][1] = step(2, 'STOP, Motortriebkopf allein vollständig aufsetzen, dann STOP aufheben. Ohne Fahrbefehl beobachten und eindeutigen Märklin-mfx-Eintrag abgleichen. Bei Abschaltung, Geruch, Wärme oder unerwartetem Motorlauf sofort STOP und physisch trennen; Diagnose nach [[30]]. Noch keinen Fahrbefehl geben.')
    P[35]['blocks'][2] = step(3, 'Nur nach unauffälliger Erstkontrolle: STOP, Gleisstecker ganz abziehen und spannungsfrei an den Betriebsausgang umstecken; Anlage bleibt ab. Nach erneuter Ruhekontrolle bei Fahrstufe 0 F0 prüfen: aus → dunkel, vorwärts → Weiß, rückwärts → Rot. LED-Werte nach [[19]] messen; danach Sound leise zuschalten.')
    P[35]['blocks'][4] = step(4, 'Erst nach bestandenem Standtest am Betriebsausgang: freien Auslauf und Endbegrenzung prüfen. Kleinste Fahrstufe kurz anlegen, dann 0; Räder nie festhalten. Bei Abschaltung sofort trennen und Ursache nach [[30]] klären. Dieser Funktionsversuch ersetzt keine volle Motorlastabnahme [[31]].')
    P[35]['blocks'][5] = step(5, 'Falsche Richtung: STOP, trennen. Zuerst Verdrahtung gegen [[21]] prüfen; abweichende Motorlitzen korrigieren und [[15]]/[[16]] wiederholen. Stimmt die Verdrahtung, darf CV51 Bit 0 „Motoranschluss tauschen“ mit gesichertem Altwert geändert werden; übrige Bits erhalten und rücklesen (Q10). Dann Richtung/Licht erneut prüfen; keine zweite Umkehr über CV29 oder Licht.')
    P[35]['blocks'][-1] = p('Datum/Projekt ______; Quelle/Netzteil ______; GFP3 leer/Erstkontrolle ______; Frontstrom ______; Sound ______; Kleinstfahrt/Richtung ______. Volle Lastabnahme folgt [[31]].')
    P[35]['sources'] = ['Q1', 'Q2', 'Q3', 'Q10', 'Q26']

    P[36]['before'] = 'Gegenkopf nach [[32]]/[[34]] vorbereitet; Motorseite [[35]] bestanden. Prüfabschnitt [[45]], keine Wagen/Puffer. Beide Köpfe ungekuppelt; freie Kontakte einzeln isoliert.'
    P[36]['blocks'][0] = step(1, 'Gegenkopf zuerst allein: STOP, Motorseite abnehmen. S/R, B/GR/0/GL, Halter und Widerstände prüfen; freie RT-/GE-Kontakte isolieren. Gleisstecker vollständig abziehen und an den Programmierausgang umstecken. Gegenkopf aufsetzen, STOP aufheben; GFP3-Ruhewert notieren. Bei Abschaltung, Wärme/Geruch sofort STOP und trennen; Diagnose [[30]].')
    P[36]['blocks'][2] = step(2, 'Nur nach unauffälliger hinterer Einzelkontrolle: STOP, Gleisstecker vollständig abziehen und am Betriebsausgang einstecken. Beide Köpfe ungekuppelt und mit Abstand vollständig auf denselben freien Abschnitt setzen. Eine CS3-Quelle, Automatik aus, Fahrstufe 0. Lage und freie Kontakte prüfen, dann STOP aufheben; keine Decoderparameter ändern.')
    P[36]['sources'] = ['Q1', 'Q6', 'Q7', 'Q26']
