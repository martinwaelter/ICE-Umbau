"""Leserführung für finale REV13-Seiten 1–4; keine neuen Prüfanforderungen.

P: Seiten als Dictionary, Schlüssel und [[Verweise]] sind finale Seiten 1–46.
"""


def _step(page, number, text):
    next(b for b in page['blocks'] if b.get('type') == 'step' and b.get('label') == f'{number}.')['text'] = text


def apply(P):
    P[1]['blocks'][1]['text'] = (
        'Funktionsübersicht: RT verbindet die Schleifer, GE führt das geschaltete Innenlicht. '
        'Diese Namen bestimmen noch keine Kabelfarbe oder Kontaktposition am Fahrzeug.'
    )
    P[1]['blocks'][3]['text'] = (
        '<b>So benutzt du die Karten:</b> Erst ganz lesen. VORHER nennt die Voraussetzungen; '
        'dann die nummerierten Handgriffe ausführen und Ergebnisse notieren. STOPP nennt den '
        'Abbruchgrund, WEITER die Bedingung für den nächsten Schritt. Anklickbare Seitenverweise '
        'führen zur benötigten Detailkarte; danach zum aufrufenden Schritt zurückkehren. '
        '„Vorwärts“ bedeutet: Motortriebkopf voraus. „Gegenkopf“ ist der motorlose ESU-Kopf.'
    )
    P[1]['blocks'][-1]['text'] = (
        '<b>Die Arbeitsfolge:</b> [[2]]–[[7]] bereiten Arbeitsplatz, Kupplungen und Messungen vor. '
        'Auf [[8]]–[[14]] werden die Decoder außerhalb des Zuges eingerichtet, programmiert und '
        'gemeinsam geprüft. Erst nach bestandener Paarprüfung beginnt der Fahrzeugumbau ab [[15]]. '
        'Messkarten, die „später ausführen“ angeben, zunächst nur vorbereiten. '
        'Offene Angaben am zugehörigen Schritt dokumentieren; kein Händlerauftrag erforderlich.'
    )

    rows = P[2]['blocks'][0]['rows']
    rows[0][1] = '60941 Motorumbausatz; 60977 Sounddecoder mit Lautsprecher; LoDi 511 Motorplatine'
    rows[1][1] = '59649 LokPilot 5 M4 MKL; kleine Märklin-Anschlussplatine und Halteplatte aus dem 60977-Satz'
    rows[1][2] = 'Artikel, beide Platinenseiten, Stecklage und Befestigung'
    rows[2][1] = 'Zwei LoDi-514-LED-Einsätze; hinten je Farbe ein eigener Serienwiderstand'
    _step(P[2], 1,
        'Fotoordner „ICE2976_REV13“ anlegen. Artikel und Platinen-Version (Revision) direkt vom '
        'Aufdruck übernehmen. Je Teil eine Gesamtansicht und ein scharfes Anschlussfoto sichern; '
        'Dateien nach Seite und Teil benennen. Befestigungen vor dem späteren Ausbau fotografieren.')

    P[3]['before'] = (
        'Jetzt den freien Abschnitt vorbereiten; alle Gleisstecker bleiben abgezogen. '
        'Eine ausgeschaltete CS3 bleibt aus; läuft sie bereits, STOP setzen. '
        'Gleise, Anschlussleitung, nichtleitende Unterlage und unbeleuchtete Endbegrenzung bereitlegen.'
    )
    _step(P[3], 3,
        'Anschlussstellen fotografieren: B führt zum Mittelleiter, 0 zu den Schienen. Bei C-Gleis '
        'B/0 an der Unterseite ablesen. Vor der ersten Messung [[5]]/[[6]] lesen, danach hierher '
        'zurückkehren. Nur freie passive Anschlussleitung/Gleise prüfen; den Stecker zur CS3 '
        'weiterhin abgezogen lassen.')
    _step(P[3], 4,
        '<b>Für die späteren Prüfungen:</b> Derselbe zweipolige Stecker kommt jeweils an genau '
        'einen der beiden Ausgänge aus der Tabelle. Quellenwechsel: STOP, Stecker ganz abziehen, '
        'erst dann am anderen Ausgang einstecken. Keine gemeinsame 0-Verbindung und kein '
        'Wechsel durch Überfahren einer Gleistrennung. Jetzt noch nicht anschließen.')
    _step(P[3], 5,
        'Netzteilartikel am geschlossenen Gehäuse ablesen. Vor dem späteren ersten Anschluss '
        'unter System → GFP3 → Einstellungen die Netzteilauswahl damit abgleichen; sie '
        'bestimmt das Abschaltverhalten. „Max. 5 A“ ist keine pauschale H0-Einstellung. '
        'Nur ein für CS3 und H0 zugelassenes Netzteil verwenden.')
    P[3]['check'] = (
        'Der freie Abschnitt ist vorbereitet und die Anschlusszuordnung geprüft; '
        'der CS3-Stecker bleibt abgezogen. Weiter zur Kupplungsaufnahme [[4]]. '
        'Bestromen erst auf der jeweiligen späteren Prüfkarte.'
    )

    P[4]['goal'] = (
        'RT und GE brauchen zwei getrennte Kontakte. Ein „Übergang“ besteht aus den beiden '
        'miteinander gekuppelten Fahrzeugenden. Die Artikelnummer 2976 beweist deren Ausstattung nicht.'
    )
    P[4]['before'] = (
        'Zug vom Gleis und von allen Quellen getrennt. Keine Kabel auslöten oder abschneiden. '
        'Reihenfolge fotografieren: Motorseite – W1 – W2 usw. – Gegenkopf; '
        'jedes Wagenende im Foto eindeutig bezeichnen.'
    )
    _step(P[4], 1,
        'Beide Köpfe und beide Enden jedes vorgesehenen Wagens ansehen. Pro Kupplungshälfte '
        'zwei voneinander getrennte Kontaktflächen suchen und ihre jeweiligen Leitungen/Anschlüsse '
        'verfolgen. In der Tabelle je Übergang Foto, Partner und Orientierung zuordnen. '
        'Verdeckte Wege als ungeklärt notieren; nichts dafür aufhebeln.')
    _step(P[4], 3,
        'Sind Kontakt und zugehöriges Leitungsende schon frei und rein passiv, nach [[5]]/[[6]] '
        'Leitfähigkeit und Trennung prüfen; danach diese Tabelle ergänzen. Bei angeschlossener '
        'Elektronik keine Offenanzeige OL erzwingen. Die vollständige Kontakt- und Kreuzpfadzuordnung '
        'wird beim späteren Freilegen auf [[28]] geprüft.')
    P[4]['check'] = (
        'An jedem Übergang ist der zweipolige Anschluss vorhanden oder die konkrete Nachrüstung '
        'geklärt. Jetzt Messgrundlagen [[5]]–[[7]], anschließend Decoderfolge [[8]]–[[14]] bearbeiten. '
        'Fahrzeugumbau erst nach bestandener Paarprüfung.'
    )

