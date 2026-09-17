"""Gezielte Leserfuehrung im bestehenden Dokument; finale Seitenzahlen."""

def step(page, label):
    return next(b for b in page['blocks'] if b.get('type') == 'step' and b.get('label') == label)

def apply(P):
    P[16]['blocks'][-1]['text'] = ('Ein Kondensator zwischen Bürste und Metallrahmen kann nach kurzem Laden im Ohmtest OL anzeigen. '
        'Deshalb zusätzlich beide Anschlussdrähte mit der Lupe verfolgen. Bei unklarem Verlauf den Anschluss vor dem weiteren Einbau klären.')
    P[22]['goal'] = ('Die elektrische Zuordnung beider Befestigungsringe muss feststehen. '
        'Eine Schraube darf nur die vorgesehenen Flächen berühren; ein sichtbarer Kupferring ist nicht automatisch Radmasse.')
    P[22]['blocks'][4]['rows'][0][0] = 'Foto / zugelassener elektrischer Anschluss'
    P[22]['blocks'][3]['text'] = P[22]['blocks'][3]['text'].replace('Ringrolle', 'elektrischer Zuordnung beider Ringe').replace('kein Sollnetz', 'keinen zulässigen Anschluss')
    P[23]['blocks'][2]['rows'][4][1] = ('MOT_L an Zweig ____; MOT_R an den anderen ____. '
        'Jeder mit eigener Drossel nach [[16]]; vor Löten notieren.')
    P[23]['blocks'][2]['after'] = 5
    step(P[23], '2.')['text'] = ('Motorzuordnung fotografieren und jede Litze nach Tabelle beschriften. '
        'Schrumpfschlauch vorher auffädeln. Kurz abisolieren, bündeln/verzinnen und zugfrei löten. '
        'Nach Abkühlen mit Lupe auf Zinnbrücken, Drahtfäden und Lötperlen prüfen; Sitz prüfen. '
        'Bewegungsschlaufen frei halten; [[7]] wiederholen.')
    step(P[25], '3.')['text'] = ('Befestigung vor Montage festlegen: Halteplatte, Ort, Schraubentyp/-länge, zulässiger Sitz und obere/untere Abstände. '
        'Reicht der vorhandene Halter nicht, passende isolierende Halterung anhand der realen Maße bestimmen. '
        'Litzen dürfen den Träger nicht halten.')
    P[26]['before'] = ('Halter [[25]] geklärt. Jetzt [[28]] für die Kupplung des Gegenkopfs ausführen, dann hier zu Schritt 1 zurückkehren. '
        'LED-Auslegung [[20]] belegt oder hintere LEDs getrennt/einzeln isoliert. Decoder/Puffer ab.')
    step(P[27], '3.')['text'] = ('Vor Anschluss jede Kupplungshälfte und jeden Übergang nach [[28]] zuordnen. '
        'Danach [[29]] vollständig ausführen: Vorprüfung, Löten und Nachprüfung. '
        'Kurze flexible Litzen so führen, dass die Deichsel beide Endlagen ohne Zug an Lötstellen erreicht.')
    P[32]['blocks'][0]['headers'][0] = '60977: elektrische Grenzwerte'
    P[33]['title'] = 'Vor dem Einsetzen: jeden Kopf prüfen'
    P[33]['goal'] = 'Vor dem ersten Einschalten im Fahrzeug: Diese Liste setzt eine bestandene Decoderpaarprüfung außerhalb des Zuges voraus.'
    step(P[36], '5.')['text'] = ('Falsche Richtung: STOP, trennen. Motorlitzen mit der auf [[23]] notierten und fotografierten Zuordnung vergleichen. '
        'Abweichung korrigieren und [[17]]/[[18]] wiederholen. Nur bei bestätigter Verdrahtung alternativ den 60977 allein bearbeiten: '
        'CV51 Bit 0 „Motoranschluss tauschen“ mit gesichertem Altwert ändern, übrige Bits erhalten und rücklesen. '
        'Danach Richtung/Licht prüfen; keine zweite Umkehr über CV29 oder Lichtmapping.')
    step(P[37], '4.')['text'] = ('STOP, Gleisstecker abziehen. Gegenkopf abnehmen und wieder aufsetzen. '
        'Beide Köpfe unverändert am Betriebsausgang anschließen, Fahrstufe 0, dann STOP aufheben und Lichtfolge wiederholen. '
        'Hintere LED-Zweige einzeln nach [[21]] prüfen und hier dokumentieren. '
        'Bei Abweichung STOP und trennen; Einschaltfolge [[14]] vergleichen und Ursache vor erneutem Versuch klären.')
