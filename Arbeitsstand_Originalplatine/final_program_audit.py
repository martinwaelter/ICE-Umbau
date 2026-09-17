"""Ablaufkorrekturen nach Konvertierung auf die endgültigen Seiten 1–47.

Keine neue Hardwareentscheidung: Quellenwechsel, Motor-Rückkehr und die
Rücksprünge aus den Prüfunterfolgen werden ausdrücklich beschrieben.
"""


def apply(P):
    D = {int(p['n']): p for p in P} if isinstance(P, list) else {int(k): v for k, v in P.items()}

    def step(n, label, text):
        matches = [b for b in D[n]['blocks'] if b.get('type') == 'step' and b.get('label') == f'{label}.']
        assert len(matches) == 1, (n, label)
        matches[0]['text'] = text

    def append_step(n, label, text):
        D[n]['blocks'] = [b for b in D[n]['blocks'] if not (b.get('type') == 'step' and b.get('label') == f'{label}.')]
        D[n]['blocks'].append({'type': 'step', 'label': f'{label}.', 'text': text})

    D[14]['check'] = ('62762 und kleine Aufnahme sitzen fest und isoliert; Originalschrauben berühren keine neue Leitung. '
                      'Jetzt Kabelbaum [[15]]. Für die getrennte Programmieraufnahme gelten [[20]]–[[24]]; '
                      'vor den anschließenden Fahrzeugtests gilt die Checkliste [[27]].')

    step(20, 1, 'Leere Märklin-Träger mit den Herstelleransichten abgleichen: Index, B/GR, 0/GL, +Ub, LV/LR und MR/MV. '
         'Auf trockener isolierender Unterlage fixieren; sie dürfen sicher im geöffneten Kopf montiert bleiben. '
         'Keine alte Fahrzeugschaltung oder verbundene Kupplung im Prüfkreis. Bereits montierte freie Kupplungsadern einzeln isolieren; Wagenbus bleibt ab.')
    step(20, 3, 'Märklin-Projekt nach [[21]] sichern. Vor CS3-Anmeldung stromlos die vordere Motor-Serviceverbindung öffnen; nur 60977 auf seinem Träger versorgen. '
         'ESU-Lesen/Schreiben: nur 59649 mit vorübergehend angeschlossenem HLA nach [[23]]/[[24]]. '
         'Nach [[24]]/5 Motor wieder vorn anschließen, [[25]]–[[32]] ausführen. Erst dann Paartest [[33]] mit beiden Motoranschlüssen offen.')

    step(21, 3, 'CS3 mit weiterhin abgezogenen Gleissteckern wieder einschalten. In den Systemeinstellungen eine neue Sicherung auf USB anlegen. '
         'Nicht „Wiederherstellen“ wählen. Am Computer zusätzlich kopieren. Nur die Kopie mit einem Archivprogramm öffnen; nach lokomotive.cs2 suchen. '
         'Vollständigen zugehörigen Lokdatensatz samt Dateiname sichern, nicht bloß eine abgeschriebene Zahl.')

    append_step(24, 5, 'Nach der letzten Rücklesung: STOP, CS3 ausschalten, Quellenstecker abziehen; beide Decoder abziehen. '
                'HLA-Prüfleitungen am hinteren Träger entfernen, dessen MR/MV einzeln isolieren. '
                'HLA ausschließlich über die vordere Motor-Serviceverbindung wieder mit MV/MR des 60977-Trägers verbinden. '
                'Stecksitz, Zuordnung und Zugentlastung prüfen; alle Prüfleitungen entfernen. Bei geänderten Motorlitzen vorher den freien Motorzweig nach [[12]]/[[13]] prüfen. '
                'Decoder bleiben für [[25]] abgezogen.')
    D[24]['check'] = ('Zielwerte frisch bestätigt; HLA wieder ausschließlich vorn, MR/MV hinten frei. '
                      'Optionale Firmwarediagnose darf offen bleiben. Weiter [[25]], Paarabnahme erst [[33]].')

    D[25]['check'] = ('Abschließend den gesamten geänderten Stand mit Motor, Sound, F0 und AUX1 neu speichern/übertragen und Einstellungen frisch rücklesen. '
                      'Dann USB trennen, Adapter abnehmen, 60977 abziehen. Relais-Schalt-/Lastabnahme folgt am geprüften Aufbau.')

    # Die elektrische Relaisauslegung bleibt beim verantwortlichen Elektrikmodul.
    D[26]['before'] = D[26]['before'].replace('RT/GE nach [[34]]–[[37]] zuordnen;',
        'RT/GE am Kopf nach [[35]] zuordnen; Wagenaufbau [[34]]–[[37]] folgt später;')
    D[26]['check'] = ('Nach der Vorbereitung weiter [[27]]. Beim späteren Aufruf aus [[30]] erst die Relais-Prüfschritte ausführen, '
                      'danach stromlos zu [[30]]/4 zurückkehren. Vor dem ersten Wagen müssen EIN/AUS und Anschlusszuordnung bestanden sein.')

    D[27]['goal'] = ('Prüfliste für die aufgebauten Köpfe vor [[30]]/[[32]] und nach späterem Wiedereinsetzen. '
                     'Die zuvor getrennte Programmieraufnahme [[20]]–[[24]] benutzt ihre eigenen Anschlussprüfungen; diese Liste ist dafür kein Vorab-Gate.')
    D[27]['before'] = ('Programmierung beendet und Prüfabbau [[24]]/5 erfolgt. Je Kopf getrennt prüfen. '
                       'Datum ______; Motorseite/Gegenkopf ______; Fotos/Protokolle ______.')
    for b in D[27]['blocks']:
        if b.get('type') == 'table':
            for row in b['rows']:
                if row[0].startswith('Alle Hilfsleitungen entfernt'):
                    row[0] = 'Prüfleitungen entfernt; Motor-Serviceverbindung vorn geschlossen, MR/MV hinten einzeln isoliert; übrige freie Enden isoliert.'

    D[30]['before'] = ('[[27]], Motorprüfung und Stecklage [[28]] bestanden. HLA nach [[24]]/5 wieder ausschließlich vorn angeschlossen. '
                       'Prüfabschnitt [[3]] frei; Gegenkopf, Wagen, Relaislast und Puffer getrennt.')
    step(30, 3, 'Nach unauffälliger Erstkontrolle: STOP, CS3 ausschalten, Gleisstecker abziehen und am Betriebsausgang anschließen. '
         'Einschalten, STOP aufheben, erneut Ruhe prüfen. Begrenzte LED-Zweige vorausgesetzt: [[31]] nur für diesen vorderen Kopf ausführen. '
         'Danach hier fortsetzen: Messclips entfernt, Betriebsausgang wieder anschließen, einschalten und STOP aufheben. '
         'F0 aus → dunkel, vorwärts → Weiß, rückwärts → Rot; Sound leise zuschalten. '
         'Dann unbelastete Relaisprüfung [[26]] ausführen und zu Schritt 4 zurückkehren.')
    step(30, 4, 'Nach bestandenem Stand-/Relaistest: Batterie-Prüfkreis entfernt und Relaisanschlüsse kontrolliert. '
         'Betriebsausgang bei ausgeschalteter CS3 wieder anschließen, einschalten, STOP aufheben. Freien Auslauf und Endbegrenzung prüfen. '
         'Kleinste Fahrstufe kurz anlegen, dann 0; Räder nie festhalten. Abschaltung: sofort trennen und [[44]]. Kein Ersatz für Lastabnahme [[39]].')

    D[31]['title'] = 'Frontzweige je Kopf mit dem Multimeter prüfen'
    D[31]['goal'] = 'Beim Aufruf aus [[30]] nur vorn, aus [[32]] nur hinten messen. Je Kopf beide Farben dokumentieren; alle vier Zweige müssen vor [[33]] bestanden sein.'
    D[31]['before'] = ('Versorgungsaufbau aus [[30]] beziehungsweise [[32]]; [[27]] und [[19]] erfüllt. '
                       'Fahrstufe 0, Motor steht. Multimeter COM/VΩ, DC-Spannungsbereich; Strombuchse frei.')
    step(31, 2, 'Nach Kontrolle der Clips den zuvor getrennten Betriebsausgang wieder anschließen, CS3 einschalten und STOP aufheben. '
         'Nur diese Farbe ungedimmt einschalten. U_R am Widerstand ablesen; I_mittel = U_R / R_gemessen. '
         'Bedienbeispiel: 18 V über 47 kΩ ergeben rund 0,383 mA; kein Fahrzeugmesswert.')
    step(31, 3, 'STOP, ausschalten und Quellenstecker abziehen, erst danach Clips umsetzen. '
         'Zweite Farbe desselben Kopfes mit Schritt 2 prüfen. Andere Tabellenzeilen bleiben bis zum späteren Kopfaufruf leer. '
         'Bei [[32]] nur den gemeinsamen ICE-Eintrag bedienen: hinten Rot bei Zug-Vorwärtsrichtung, Weiß bei Rückwärtsrichtung.')
    step(31, 4, 'Farbe und offene Ausleuchtung bewerten; geschlossene Helligkeit erst auf [[43]]. '
         'Keine direkte LED-Verbindung zum Helligkeitsvergleich. STOP, ausschalten, Quellenstecker abziehen, dann alle Messclips entfernen. '
         'Leitungen und Widerstände gegen Quetschen sichern.')
    D[31]['check'] = ('Beide Farben des aufgerufenen Kopfes protokolliert; Messclips entfernt, Versorgung ab. '
                      'Vorn zurück zu [[30]]/3; hinten zurück zu [[32]]/4. Alle vier Ergebnisse vor [[33]] vollständig.')

    D[32]['before'] = ('[[27]]/[[29]] vorbereitet, Motorseite [[30]] bestanden. Kein Wagen/Puffer. '
                       'Erst Gegenkopf allein außerhalb des Gleises; beide Köpfe erst in Schritt 2 aufgleisen. '
                       'Isolierte, passende und zugentlastete RT-Prüfleitung bereitlegen.')
    step(32, 1, 'STOP, CS3 ausschalten und alle Quellenstecker abziehen. Gegenkopf allein außerhalb des Gleises über [[20]] verbinden: '
         'nur Programmierausgang an B/GR und 0/GL, MR/MV offen, hinterer Schleifer getrennt. Einschalten, STOP aufheben, Ruhe beobachten. '
         'Bei Abschaltung/Wärme/Geruch STOP, trennen und [[44]]. Kein DCC-Lesen ohne Motorlast fordern.')
    for b in D[32]['blocks']:
        if b.get('label') == 'RICHTIGER PRÜFZWECK':
            b['text'] = b['text'].replace('DCC-Wartung nur auf [[20]].', 'DCC-Wartung nur einzeln nach [[23]]/[[24]].')
    step(32, 4, 'STOP, CS3 ausschalten, Gleisstecker abziehen. Köpfe abnehmen/wieder aufsetzen, RT-Prüfverbindung kontrollieren. '
         'Betriebsausgang wieder anschließen, einschalten, STOP aufheben; Lichtfolge wiederholen. '
         '[[31]] nur für die beiden hinteren Farbzweige ausführen. Danach hier fortsetzen: Versorgung bleibt physisch ab, '
         'Messclips und RT-Prüfleitung vollständig entfernen. Weiter zur vollständigen Paarabnahme [[33]].')

    D[33]['before'] = ('[[24]]/[[25]] und Einzeltests [[30]]/[[32]] bestanden; alle vier LED-Ergebnisse [[31]] vollständig. '
                       'Quellen physisch ab, Automatik aus, Fahrstufe 0; Wagenbus/Puffer getrennt. Keine Traktion.')
    step(33, 1, 'Stromlos beide Decoder abziehen. Die seit [[30]] angeschlossene vordere Motor-Serviceverbindung jetzt ausdrücklich öffnen. '
         'Hintere MR/MV müssen einzeln isoliert, HLA-Prüfleitungen entfernt sein. Anschluss-/Sichtprüfung, beide Decoder wieder einsetzen. '
         'Beide Motorausgänge bleiben frei. Vorn +Ub/LV/LR an Plus/Weiß/Rot, hinten an Plus/Rot/Weiß; jede Farbe mit eigenem Widerstand.')
    append_step(33, 6, 'Nach STOP, Ausschalten und physischem Trennen den B/0-Prüfverteiler an beiden Trägern vollständig entfernen. '
                'Keine Prüfversorgung oder RT-Brücke bleibt angeschlossen. Bei abgezogenen Decodern vordere Motor-Serviceverbindung schließen; '
                'Zuordnung, Stecksitz und Zugentlastung kontrollieren. Hinten MR/MV weiter einzeln isoliert. '
                'Bei neu verlegten Motorlitzen vorher [[12]]/[[13]] am freien Motorzweig wiederholen. '
                'Decoder korrekt wieder einsetzen. Für den Wagenaufbau bleibt alles stromlos.')
    D[33]['check'] = ('F0/Farben, Neustart und mfx-Bedienweg bestanden. Prüfverteiler entfernt ______; Motor ausschließlich vorn angeschlossen ______; '
                      'hintere MR/MV frei ______. Erst dann Wagenaufbau [[34]].')

    for n in (39, 40):
        D[n]['before'] = D[n]['before'].replace('Paarabnahme [[33]] bestanden', 'Paarabnahme einschließlich Prüfabbau/Motor-Wiederanschluss [[33]]/6 bestanden')

    step(43, 5, 'Helligkeit jetzt mit Lichtleitern/Gehäuse bei gleichem Umgebungslicht vergleichen. Weiß/Rot getrennt abstimmen; helleren Ausgang dimmen. '
         'ESU nur einzeln nach [[23]]/[[24]] ändern, einschließlich Motor-Rückkehr [[24]]/5; danach betroffene Tests und erneute Gehäuseprüfung. '
         'Wagen-TRIMM jeweils stromlos minimal verstellen, Werkzeug entfernen, einschalten und vergleichen; keinen Endanschlag erzwingen.')
    step(44, 3, 'Vor Wiedereinsetzen alle Quellen physisch trennen und Prüfversorgung entfernen. '
         'Nach ESU-Arbeit HLA-Rückkehr [[24]]/5: Motor nur vorn, hintere MR/MV einzeln isoliert. '
         'Nach erneuter Paarprüfung deren Prüfabbau [[33]]/6 vollständig ausführen. '
         'Betroffene Anschluss-/Steck-, Funktions-/Synchronisationsprüfungen wiederholen; bei erneutem Öffnen auch [[42]]/[[43]]. '
         'Datum und neuer Projektstand gehören zum Zug.')
    return P


CHANGED_PAGES = (14, 20, 21, 24, 25, 26, 27, 30, 31, 32, 33, 39, 40, 43, 44)
