"""Drei Inhaltskarten der 62762-Anleitung.

apply(P): Dictionary mit alten finalen REV13-Seitennummern.
Nur 9, 19 und 22 werden ersetzt; [[n]] bleiben in diesem Nummernraum.
"""
from pathlib import Path

ROOT = Path('/Users/martinwaelter/ICE Umbau')
OWN = ROOT / 'Arbeitsstand_REV10/bilder'
BELEGE = ROOT / 'Arbeitsstand_Originalplatine/belege_62762'


def step(n, text):
    return {'type': 'step', 'label': f'{n}.', 'text': text, 'after': 6}


def photo(path, maxh, crop=None):
    b = {'type': 'figure', 'path': str(path), 'maxh': maxh, 'after': 4}
    if crop:
        b['crop'] = crop
    return b


def caption(text):
    return {'type': 'small', 'text': text, 'after': 7}


def replace(P, n, **fields):
    old = P[n]
    old.update(fields)
    old.pop('image_source', None)


def apply(P):
    replace(P, 9,
        title='Deine Originalplatine 62762 erkennen',
        phase='Originalträger | Bilder und Orientierung',
        goal='Die lange Märklin-Platine bleibt erhalten. Sie trägt später die kleine, isoliert befestigte 21MTC-Aufnahme; ihre alten Leiterzüge bleiben im Grundaufbau elektrisch unbenutzt.',
        before='',
        blocks=[
            photo(OWN / '0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg', 115),
            caption('<b>1 – Dein 2976:</b> Motor links, lange Originalplatine darüber/rechts. Der Aufdruck ist hier zu klein für eine sichere Lesung. Leiterzüge, versetzte Kantenkerben und Befestigungen passen sehr deutlich zur 62762.'),
            photo(BELEGE / 'kleinanzeigen_3331585671_bild1.jpg', 115, [0.05, 0.37, 0.77, 0.60]),
            caption('<b>2 – Fremdexemplar, Leiterzugseite:</b> 62762 / 03/92 / VER1.1 ist lesbar. Das gabelförmige Ende liegt rechts. Lange parallele Leiterzüge, zwei versetzte Randkerben und die Bohrungen sind die Vergleichsmerkmale.'),
            photo(BELEGE / 'kleinanzeigen_3331585671_bild2.jpg', 115, [0.12, 0.51, 0.78, 0.75]),
            caption('<b>3 – Gegenseite desselben Fremdexemplars:</b> rechts der mechanische Schalter; keine aktive Decoderbestückung wie auf der anderen Platine 62761. Die Ausschnitte 2/3 zeigen die 62762, nicht die daneben angebotenen Baugruppen.'),
            {'type': 'p', 'text': '<b>Am eigenen Teil:</b> Aufdruck und beide Seiten ansehen; Motorende und anderes Ende im Foto markieren. Fremdfotos 2/3 sind gegenüber deiner Einbaulage anders ausgerichtet. Vor allem keine Kabelposition durch bloßes Links-/Rechts-Ablesen übertragen.'},
            {'type': 'note', 'label': 'WAS DIE BILDER BELEGEN', 'text': 'Form und Leiterplattenfamilie sind gut eingegrenzt. Die Funktion eines eigenen Kabels, das Netz eines Schraubrings und die Schalterkontakte werden auf [[19]] gemessen. Diese Bilder enthalten keine Schnitt- oder Lötmarken.', 'tone': 'info', 'after': 5},
        ],
        check='Die eigene Platine ist wiedererkannt und orientiert. Du brauchst keinen Händler und keine weiteren Fremdfotos: Anschlüsse vor dem Ablöten auf [[19]] markieren und am eigenen Teil prüfen.',
        sources=['Q37', 'Q38'])

    replace(P, 19,
        title='62762 ausbauen und Anschlüsse aufnehmen',
        phase='Originalträger | stromlose Demontage',
        goal='Die Platine wird freigelegt und danach wiederverwendet. Alte Umschaltung und Lampenverdrahtung bleiben vom neuen Decoder elektrisch getrennt.',
        before='Vom Gleis nehmen, abkuppeln; alle Quellen, Programmer und Puffer physisch trennen. Restenergie nach [[5]] ausschließen. Noch nichts ablöten. Papieretiketten, Kamera und Ablage für Originalschrauben bereitlegen.',
        blocks=[
            photo(OWN / 'BAD231CB-B878-4D94-B5EE-CDAB1D69D455_4_5005_c.jpeg', 90),
            caption('Eigenes Seitenfoto: alter Motor links, lange Platine darüber/rechts. Verdeckte Anschlüsse erst nach zugfreiem Freilegen aufnehmen; dieses Foto gibt keine einzelnen Lötpunkte frei.'),
            step(1, 'Gehäuse an den vorhandenen Befestigungen öffnen. Jede zu lösende Leitung <b>an beiden Enden gleich</b> markieren: A01/A01, A02/A02 usw. Farbe, altes Pad und sichtbares Ziel im Foto notieren. Unbekanntes Ziel zunächst „offen“ nennen. Beide Befestigungen als <b>Ring A / Ring B</b> markieren; Schrauben und Scheiben nach Einbauort ablegen.'),
            step(2, 'Eine markierte Litze nach der anderen an ihrer bisherigen Lötstelle lösen. Nur bei flüssigem Lot abheben; nicht am kalten Pad ziehen. Freie Enden beschriftet halten und einzeln isolieren. Platine abstützen, Schrauben lösen und ohne Kabelzug abheben. Verdeckte Leitungen jetzt ebenfalls markieren und ablösen.'),
            step(3, 'Alte Umschalteinheit und ersetzte Lampenfassung getrennt ausbauen und aufbewahren. <b>62762 und ihr Schalter bleiben erhalten.</b> Alle alten Anschlussdrähte von der Platine lösen; keine Leiterbahn schneiden. Auch Dach-/Schalterleitungen nicht ungeprüft wieder anschließen.'),
            step(4, 'Freie Lötflächen im eigenen Foto P1, P2 usw. nennen. Ω-Messung nach [[6]]: eine Spitze an P1 festhalten, die andere nacheinander an die übrigen Pads und Ring A/B; danach P2 gegen die noch ungeprüften Punkte usw. In beiden Schalterstellungen wiederholen. Kontaktprobe vor/nach jeder Reihe; leitend, offen oder wechselnd notieren. Keine Spannung einspeisen.'),
            step(5, 'Abgelöste Fahrzeugleitungen direkt zum wirklichen Schleifer, Radkontakt und Kupplungskontakt prüfen. Erst diese Messung erlaubt B, 0, RT oder GE als neuen Namen. Kupplungen nach [[28]], danach hierher zurück. Keine Zuordnung aus der Litzenfarbe und kein Kurzschluss zwischen B und 0.'),
            {'type': 'table', 'headers': ['Leitung / alter Punkt', 'Tatsächliches Ziel / Messung', 'Neuer Name'], 'rows': [['A___ / P___', '________________________', '________'], ['A___ / P___', '________________________', '________']], 'widths': [1.1, 2.1, 0.8], 'after': 6},
            {'type': 'p', 'text': '<b>Grundaufbau:</b> Kein alter Kupferpfad erhält eine neue Decoderleitung. Die 62762 dient als Träger für unabhängig isolierte Neuverkabelung. Ein ungeklärter Altpfad bleibt elektrisch unbenutzt; er verlangt keinen geratenen Schnitt.'},
        ],
        check='Alle alten Leitungen sind gelöst und zugeordnet; Platine und Originalschrauben aufbewahrt. Erst HLA/Entstörung und Motorprüfung [[15]]–[[18]] ausführen, danach 62762 auf [[22]] wieder einsetzen.',
        sources=['Q1', 'Q2', 'Q37', 'Q38'])

    replace(P, 22,
        title='Originalträger und 21MTC sicher befestigen',
        phase='Motorseite | Wiedermontage nach Motorprüfung',
        goal='Die 62762 bleibt an ihren originalen Auflagen. Der kleine Märklin-Träger sitzt in seiner Halteplatte elektrisch isoliert darüber; keine Decoderleitung nutzt altes Kupfer.',
        before='Motorprüfung [[18]] bestanden. Alte Leitungen nach [[19]] vollständig abgelöst. Alle Quellen/Puffer getrennt; Decoder abgezogen. Originalschrauben und vorgesehene Märklin-Halteplatte bereitlegen.',
        blocks=[
            photo(ROOT / 'Arbeitsstand_REV11/zeichnungsquellen/maerklin_60977_600dpi-005.png', 160, [0.045, 0.225, 0.478, 0.695]),
            caption('Märklin-Originalzeichnung: die kleine elektrische Anschlussplatine. Sie ist eine zusätzliche Baugruppe auf der erhaltenen 62762; ihre Anschlussnamen sind keine Aufdrucke der Altplatine.'),
            step(1, '62762 in ihrer ursprünglichen Lage plan auf die originalen Auflagen setzen. Nur die zugeordneten Originalschrauben/Scheiben benutzen. Beide Schrauben zunächst leicht ansetzen, dann gleichmäßig sicher anziehen. Nach jeder Schraube Schiefstand, eingeklemmte Litzen und Kontakt zum Motor ausschließen. Keine neuen Löcher bohren.'),
            step(2, 'Nach Verschrauben feststellen, welche alten Pads oder Ringflächen zum Chassis leitend sind; Ω-Kontaktprüfung nach [[6]]. Ergebnis eintragen. Dieser alte Metallpfad bleibt ohne neue elektrische Funktion. Er darf insbesondere nicht mit U+, Motor- oder Lichtausgängen verbunden werden.'),
            step(3, 'Kleine Märklin-Anschlussplatine in ihre vorgesehene Kunststoff-Halteplatte setzen. Auf freier Stelle der 62762 positionieren: Stecker erreichbar, Platz für den langen Decoderkörper, Abstand zu Schraubköpfen, Schalter, Motor und Dach. Die Höhe des vollständigen Steckpakets berücksichtigen; der Decoder bleibt vor den Lötarbeiten abgezogen.'),
            step(4, 'Zwischen Halteplatte und gefährdenden Kupfer-/Metallflächen eine festliegende, temperaturgeeignete Isolierunterlage einsetzen. Die Halteplatte an zwei freien Haltebereichen mit nichtleitenden Befestigungen sichern, z. B. Kunststoffbindern um Originalträger und Halter. Bindungen nur über den Halter führen, <b>nie über Decoder, Bauteile, Stiftleiste, Litzen oder Lötstellen</b>. 62762 dabei nicht durchbiegen.'),
            step(5, 'Halter vorsichtig längs, quer und nach oben belasten: Er darf sich beim späteren Stecken nicht verschieben oder abheben. Unterseite und Befestigung ansehen. Fehlt ein freier sicherer Befestigungsweg, diesen Halter anpassen; nicht mit dem Gehäuse einklemmen. Litzen und lose Isolierstreifen sind keine Halterung.'),
            step(6, 'Drehgestelle und Kupplung in beide normalen Endlagen bewegen; Freiraum und spätere Litzenwege prüfen. Montage fotografieren. Nach der Verkabelung [[23]] die neuen Leiter gegen alte Kupferflächen/Ringe prüfen. Geschlossenen Dachfreiraum und Servicezugang später auf [[42]]/[[43]] abnehmen.'),
        ],
        check='62762 sitzt plan; kleine Aufnahme ist isoliert und fest. Die Originalschrauben berühren keine neue Leitung. Erst jetzt den unabhängigen Kabelbaum nach [[23]] anschließen; Decoder erst nach der Checkliste einsetzen.',
        sources=['Q1', 'Q37', 'Q38'])
