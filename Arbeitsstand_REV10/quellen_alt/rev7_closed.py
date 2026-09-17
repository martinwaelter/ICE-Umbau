"""Close the independent review's final usability and test-supply findings."""
import rev7_verified as verified

def install(ns):
    verified.prior.MORE.extend([
        ('Noch nicht einschalten; weiter nach 17.', 'Noch nicht einschalten. Erst die übrigen Anschluss-/Konfigurationskarten bis einschließlich 16a erledigen; danach Inbetriebnahme nach 17.'),
        ('Nach den elektrischen Prüfungen und den Schritten 52-56:', 'Im Rahmen von Schritt 56, nach bestandenen Schritten 52-55 und den elektrischen Prüfungen des jeweils ergänzten Wagens:'),
        ('F1-F8 bestanden', 'T1-T8 bestanden'),
        ('Den tatsächlich verwendeten Kontaktabschnitt zuerst leer in der CS3 beobachten: frei. Dann den Wagen aufstellen: erwartete Belegtmeldung prüfen. Innenlicht aus und ein testen; danach den Wagen vollständig entfernen: wieder frei. Mit beiden Wagenorientierungen wiederholen. Eine zusätzliche Kontaktfeder macht isolierte Radsätze nicht automatisch rückmeldefähig. Bei einer unerwarteten Meldung erst Radsatztyp, Trennstellen und Leitungsziel B prüfen; nicht B mit O verbinden.',
         'Zuerst den einzelnen Wagen ohne Lichtversorgung aufstellen und entfernen: frei - belegt - frei prüfen. Danach im nach Kapitel 17 freigegebenen Zug einkuppeln: RT und GE kommen jetzt über die Kupplungen. Nur die Räder des Testwagens dürfen den geprüften Meldeabschnitt belegen; andere Wagen/Köpfe bleiben außerhalb, aber auf demselben CS3-Stromkreis. Innenlicht aus/ein und Meldung vergleichen, dann Abschnitt vollständig räumen: frei. Ist diese Einzelbelegung nicht möglich, Licht und Achsmeldung getrennt prüfen; den gemeinsamen Test offen lassen. Beide Wagenorientierungen prüfen. Eine Kontaktfeder macht isolierte Radsätze nicht automatisch rückmeldefähig; B niemals mit O verbinden.'),
    ])
    verified.install(ns)
    original_table=ns['table']
    def table(headers,rows,widths):
        if headers==['Test','Du bedienst nur den gemeinsamen ICE-Eintrag','Bestanden, wenn']:
            revised=[]
            for i,row in enumerate(rows,1):
                name=row[0].split(': ',1)[1]
                revised.append((f'T{i}',f'<b>{name}:</b> {row[1]}',row[2]))
            rows=revised
        return original_table(headers,rows,widths)
    ns['table']=table
