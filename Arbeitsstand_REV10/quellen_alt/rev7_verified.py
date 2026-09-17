import rev7_polish as prior

def install(ns):
    prior.MORE.extend([
        ('Nur bei gesichertem Fahrzeug und genügend Fahrweg eine kleine Fahrstufe kurz anlegen, dann auf null. Bei Brummen ohne Bewegung, Geruch, Überlast oder ungewöhnlicher Erwärmung sofort abschalten. Nicht den Rotor blockiert halten, um einen Grenzstrom zu ermitteln.',
         'Prüfgleis waagerecht mit ausreichend freiem Fahrweg gegen Absturz sichern. Nur kleinste Fahrstufe kurz anlegen und auf 0 zurückstellen; keine Räder festhalten. Bei Brummen ohne Fahrt oder ungewöhnlicher Wärme sofort Versorgung aus und Bürstensitz, Mechanik und 6a prüfen. Bei falscher Richtung Motorzuordnung nach 9a korrigieren, nicht das Licht umkehren. Bei Geruch/Überlast nicht erneut einschalten.'),
        ('Kontakt dem aktiven ICE-Ablauf zuordnen. Bei Halt am zugehörigen Signal sendet er einen langsamen Annäherungsbefehl; ein Haltemelder davor sendet Fahrstufe 0 an genau diesen ICE. Restbremsweg berücksichtigen. Bei passendem Fahrtbegriff und freiem Fahrweg darf dieser Haltablauf nicht stoppen. Unklare Freigabe ist kein Abfahrtsauftrag.',
         'Vor der Ereigniserstellung je Richtung Signalname/-adresse, Brems- und Haltekontaktadresse, Abstand zum Schutzpunkt und den einen ICE-Eintrag notieren. Diese Anlagendaten fehlen noch. Erst damit den Ablauf erstellen: bei Signalhalt langsame Annäherung am Bremskontakt und Fahrstufe 0 am Haltekontakt für genau diesen ICE. Bis zur Abnahme den Zug von Hand anhalten.'),
        ('Beide ESU-Kästen sind derselbe hintere 59649:', 'Im Schaltbild aus Kapitel 10 sind beide ESU-Kästen derselbe hintere 59649:'),
    ])
    prior.install(ns)
    original_page=ns['page']; original_sketch=ns['Sketch']
    current={'title':''}
    def page(title):
        current['title']=title
        return original_page(title)
    def sketch(kind,height=175):
        if current['title']=='12a. Hinteres Rot/Weiß eindeutig zuordnen' and kind=='led':
            return ns['Spacer'](1,1)
        return original_sketch(kind,height)
    ns['page']=page;ns['Sketch']=sketch
