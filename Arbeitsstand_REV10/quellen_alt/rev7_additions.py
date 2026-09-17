"""Additional concrete case instructions; passive axle return remains an explicit option."""
import rev7_content as base

EXTRA = [
('60977 abgezogen lassen. Am Steckfeld die fehlende Pinposition suchen und mit der blockierten Position der Decoderbuchse vergleichen. Beide müssen übereinander liegen; keine Stiftreihe seitlich versetzt ansetzen. Fehlt diese eindeutige Zuordnung, Nahfoto beider Steckseiten für den Abgleich aufnehmen.', 'Hier kommt ausschließlich der Märklin 60977 hin. Sein langer Körper liegt über der freien hellen Fläche in Richtung K1, nicht über LS1/LS2. Die Decoderbuchse bleibt oben sichtbar; die Stifte gehen von unten durch den Decoder. Vollständige Einsetzfolge und Indexkontrolle: 9c.'),
('21MTC-Index mit Decoderunterlagen vergleichen; nicht versetzt oder umgedreht aufstecken.', 'ESU 59649 nach 12b einsetzen: Buchse oben, langer Decoderkörper über der freien Fläche des Märklin-Trägers; nicht über die Lautsprecher-/SUSI-Buchsen.'),
('Vorgesehen für hinten; Stecklage und Belegung prüfen.', 'Für ESU 59649 hinten: Anschlüsse nach 12 und konkrete Steckfolge nach 12b.'),
('Anschlussfreigabe in Abschnitt 15.', 'Bis zum Anschlussnachweis in Kapitel 15 abgesteckt lassen.'),
('Im hinteren Aufbau unbenutzt; vorhandene lose Litzen jeweils einzeln isolieren.', 'Hinten nicht anschließen. Jede freie Litze einzeln mit Schrumpfschlauch isolieren, sodass kein blankes Ende mehr zugänglich ist; keine zwei Enden zusammenfassen.'),
('B bleibt an beiden Enden ohne Anschluss.', 'Ohne Achsschleifer bleibt B an beiden Enden frei. Mit optionaler Radmasseleitung nur B benutzen, siehe 14c.'),
('B bleibt an beiden Enden frei.', 'Ohne Achsschleifer bleibt B frei; optional Radkontakt an B nach 14c.'),
('B-Pads frei.', 'B-Pads ohne Achsschleifer frei; optionale Radmasse nach 14c.'),
('B leer;', 'B ohne Achsschleifer leer, optional Radmasse nach 14c;'),
('B leer.', 'B ohne Achsschleifer leer, optional Radmasse nach 14c.'),
('In dieser zweipoligen Variante kein zusätzlicher Radmasseanschluss.', 'Grundaufbau: B frei. Option nach 14c: örtliche Achskontaktleitung an B; kein dritter Kupplungsleiter.'),
('In dieser zweipoligen Variante kein zusätzlicher Radmasseanschluss', 'Ohne Achsschleifer frei; mit Option 14c örtliche Radmasse'),
('Optionaler Radmasseanschluss; im hier gewählten zweipoligen Aufbau nicht zusätzlich verdrahten.', 'Optionaler örtlicher Radmasseanschluss nach 14c. Ohne Achsschleifer B frei lassen.'),
('LoDi beschreibt auch eine andere Anschlussvariante mit anderer O/B-Zuordnung. Diese nicht mischen. Bei der weißen V4.3 darf SJ2 nicht als Motor-AUX-Auswahl interpretiert werden. Bestehende Radmassefedern in den Wagen nur gemäß bestätigtem zweipoligem LoDi-Aufbau entfernen; die Radkontakte der Triebköpfe bleiben erforderlich.', 'Für deine MT-37700 V4.3 gilt mit LoDi 511: RT an O, GE an L. Ohne Achsschleifer bleibt B frei. Willst du örtliche Radkontakte ergänzen oder erhalten, diese nach 14c an B anschließen; vorhandene Achskontaktfedern dafür nicht entfernen. SJ2/Türbeleuchtung unverändert lassen. Die Radkontakte beider Triebköpfe bleiben angeschlossen.'),
('Vorhandene Kontaktgleisbereiche melden Belegung.', 'Vorhandene Kontaktgleisbereiche melden Belegung.'),
('Der Märklin-Einmesslauf kann stark beschleunigen. Er gehört erst auf eine dafür geeignete freie Strecke gemäß Herstelleranleitung. Ein kurzer Prüfgleisabschnitt ist dafür ausdrücklich ungeeignet.', 'Für die Prüfungen 52-56 keine Einmessfahrt anfordern. Den 60977 mit dem eingestellten C90-Motortyp erst in Schritt 53 bei kleinster Fahrstufe bewegen. CV 7/Firmware-Feld nicht auf 77 setzen. Einen Richtungswechsel für den Lichttest nur bei stehendem Motor auslösen.'),
('Wenn du die beiden Enden eines Bauteils, einen 21MTC-Kontakt oder einen Messwert nicht sicher zuordnen kannst: nicht weiterlöten und keine Probe unter Spannung. Detailfoto mit Markierung und Messwert anfertigen; genau diesen Arbeitsschritt prüfen lassen. Eine Schutzabschaltung ersetzt diese Prüfung nicht.', 'Lass den 60977 beziehungsweise 59649 abgezogen. Markiere auf einem scharfen Foto beide Messpunkte; schreibe Schrittnummer, Messbereich, Vorprobe, Messwert und Nachprobe dazu. Gib genau diese Angaben zur Prüfung. Nach bestätigter Zuordnung die ganze Messreihe wiederholen; nicht am Gleis ausprobieren.'),
('Schleiferfläche und eigener Schleiferanschluss. PX2 ist hier NICHT das Chassis.', 'PX an die blanke Schleiferfläche, PX2 an deren abgetrennte Anschlusslitze; nicht am Chassis lassen. Ganze Sechserfolge neu beginnen.'),
('Zwei blanke, leitend zusammengehörige Stellen desselben Chassisteils.', 'PX und PX2 an zwei blanke Stellen desselben Metallchassisteils klemmen. Nicht beide an denselben möglicherweise isolierten Schraubenkopf setzen.'),
('Die vier Clips bleiben während einer Messreihe am Fahrzeug fest. Nur die Multimeterleitungen an den beschrifteten freien Enden umstecken.', 'Kleine Schilder PM1, PM2, PX und PX2 an die Hilfsleitungen kleben. Die vier Fahrzeugclips bleiben fest. Rot für M1-Metall an PM1, für M2-Metall an PM2 stecken; Schwarz bleibt dabei am freien PX-Ende.'),
('Nur bei gesichertem Fahrzeug und genügend Fahrweg eine kleine Fahrstufe kurz anlegen, dann auf Null.', 'Prüfgleis waagerecht mit ausreichend freiem Fahrweg und gegen Absturz sichern. Nicht an Motor oder Rädern festhalten. Nur die kleinste Fahrstufe anlegen, tatsächliche Richtung ansehen und auf 0 zurückstellen.'),
('Eine freie Funktion wählen, die keinen benötigten Sound überschreibt.', 'Die Innenlichttaste im vorhandenen Soundprojekt eindeutig festlegen.'),
('Die Jumper bleiben unverändert.', 'Die Jumper bleiben unverändert. Ausgangsmodus, Tastenverhalten und Richtungsbedingungen nach 16a festlegen.'),
('Den Bus nie unter Spannung stecken. Innenlicht muss unabhängig von F0 und Fahrtrichtung reagieren.', 'Den Bus nie unter Spannung stecken. Innenlicht nach 16a konfigurieren und den Standtest 17a ausführen: F0 und Richtungswechsel dürfen das Wagenlicht nicht ausschalten.'),
]

def install(ns):
    # The source stream first receives the earlier precise edits, then these latest requirements.
    base.REPLACEMENTS.extend(EXTRA)
    base.install(ns)
    old_page=ns['page']

    def page(title):
        if title=='10. Front-LEDs gefahrlos identifizieren':
            front_insertion(ns,old_page)
        if title=='13. Mittelwagenplatinen montieren':
            rear_insertion(ns,old_page)
        if title=='15. Den vorhandenen 60974 vorbereiten':
            axle_page(ns,old_page)
            axle_test_page(ns,old_page)
        if title=='17. Erstes Einschalten ohne Puffer':
            light_mapping(ns,old_page)
        if title=='18. Belastung und Gehäuseabschluss prüfen':
            flicker_test(ns,old_page)
        return old_page(title)
    ns['page']=page
    ns['SOURCES'][23]=('Märklin','Daten und Werte mSD3/mLD3','Stand mSD3/1222/Sm2; S. 2-3: Auslöser, Dimmer-Modus und Bedingungen; Firmwarebezug beachten','https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf')
    old_refs=ns['refs']
    def refs(*nums):
        old_refs(*nums)
    ns['refs']=refs
    # Add the new primary source to the appendix as well as beside its instruction.
    old_warn=ns['warn']
    def warn(title,text):
        if title=='Verbindlicher Dokumentstatus':
            ns['add']('23. Märklin: <a href="https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf">Daten und Werte mSD3/mLD3</a>. S. 2-3, Stand mSD3/1222/Sm2: Dimmer-Modus, Auslöser und Bedingungen.','small')
        old_warn(title,text)
    ns['warn']=warn

def front_insertion(ns,page):
    page('9c. Vorn: Märklin 60977 auf LoDi 511 einsetzen')
    ns['add']('Du setzt hier den <b>Märklin 60977</b> ein, nicht den ESU 59649. Die Anweisung gilt für die im eigenen Foto gezeigte rote LoDi 511 mit der langen freien Decoderfläche. Platinenzuordnung und Befestigungsprüfung aus 8/9 müssen zuvor abgeschlossen sein.')
    ns['story'].append(ns['MarkedPhoto']('/Users/martinwaelter/ICE Umbau/Arbeitsstand_REV10/bilder/image-2.jpg',110,[(1,.48,.584,.05,.56),(2,.55,.45,.92,.39),(3,.82,.674,.10,.72)],320))
    ns['table'](['Markierung im eigenen Foto','Konkrete Einbaulage'],[
        ('1: Steckleiste in der Mitte','Die Stifte dieser Leiste treten von unten durch die Löcher der Decoderplatine in deren Buchse ein.'),
        ('2: lange helle Fläche Richtung K1','Dorthin zeigt der lange Körper des 60977. Er liegt über dieser Fläche, nicht über dem Lautsprecherbereich.'),
        ('3: LS1/LS2 unterhalb der Steckleiste','Dieses Ende ist nicht die Auflage für den langen Decoderkörper. Die Lautsprecherlitzen nicht unter den Decoder klemmen.')],[2.0,4.6])
    ns['step']('M1','60977 ausrichten.','Alle Versorgungen und der 60974 sind abgetrennt. Halte den 60977 nur an seinen Platinenkanten. Seine schwarze Buchsenleiste bleibt nach oben sichtbar, also von der roten Trägerplatine abgewandt. Führe die Stifte nicht von oben in diese Buchse ein.')
    ns['step']('M2','Fehlstelle vor dem Drücken abgleichen.','An der 21MTC-Stiftleiste fehlt genau die Indexposition 11; an der Decoderseite ist diese Position geschlossen. Bringe beides deckungsgleich über die beiden vollständigen Stiftreihen. Nicht nach einer geratenen Links-/Rechtsposition zählen. Ein Stift darf nirgends auf der Decoderplatine oder auf der geschlossenen Indexstelle stehen.')
    ns['step']('M3','Gerade aufstecken.','Den 60977 parallel zur LoDi-Platine halten und gleichmäßig im Bereich der Steckleiste nach unten drücken, nicht auf einen Chip oder das freie Decoderende. Bei Widerstand absetzen und Reihenversatz prüfen; keine Pins biegen. Danach seitlich kontrollieren: alle Stifte eingeführt, Decoder gerade, keine Metallberührung und keine Litze darunter. Noch nicht einschalten; weiter nach 17.')
    ns['add']('Beleggrenze: Die Richtung des langen Körpers folgt der sichtbaren Freifläche deines Fotos; die Buchse-oben-Steckweise entspricht der kompakten 21MTC-Mechanik und der Märklin-Einbauzeichnung. Das Foto zeigt keinen bereits eingesteckten 60977. Ist an deinem Exemplar die Indexfehlstelle nicht erkennbar oder passt diese Lage nicht druckfrei, Makrofoto von Stiftleiste und beiden Decoderseiten beschaffen; nicht testweise umdrehen.','small')
    ns['refs'](1,10)

def rear_insertion(ns,page):
    page('12b. Hinten: ESU 59649 auf Märklin-Träger')
    ns['add']('Hier wird der <b>ESU 59649 LokPilot 5 M4 MKL</b> auf die separate Trägerplatine aus deinem 60977-Satz gesetzt. Der 60977 bleibt im Motortriebkopf auf LoDi. Die Originalzeichnung unten zeigt die Steckmechanik des Märklin-Trägers; der darauf einzusetzende Decoder ist in unserem hinteren Kopf der 59649.')
    class ClipDiagram(ns['Flowable']):
        def __init__(self):
            super().__init__(); self.width=290;self.height=300
        def draw(self):
            path='/Users/martinwaelter/ICE Umbau/Arbeitsstand_REV10/bilder/ice2976_stecken-006.png'
            with ns['PILImage'].open(path) as im: iw,ih=im.size
            l,t,r,b=.075,.265,.405,.925
            s=min(self.width/((r-l)*iw),self.height/((b-t)*ih))
            c=self.canv;c.saveState();p=c.beginPath();p.rect(0,0,(r-l)*iw*s,(b-t)*ih*s);c.clipPath(p,stroke=0)
            c.drawImage(path,-l*iw*s,-(1-b)*ih*s,width=iw*s,height=ih*s);c.restoreState()
    ns['story'].append(ClipDiagram())
    ns['add']('Vergrößerter Ausschnitt aus Märklin 60977-Beilage S. 6, unveränderte Herstellerzeichnung. ESU beschreibt dieselbe kompakte Einsetzweise für die 21MTC-Ausführung einschließlich 59649.','small')
    ns['step']('E1','Träger hinlegen.','Richte den leeren Märklin-Träger wie in Kapitel 12 aus: Lautsprecher-/SUSI-Buchsen links, die lange freie Decoderfläche auf der anderen Seite der Stiftleiste. +Ub/LV/LR und alle übrigen Verdrahtungen nach 12/12a sind geprüft; kein Puffer angeschlossen.')
    ns['step']('E2','59649 halten.','Die schwarze Buchsenleiste des 59649 zeigt nach oben und bleibt nach dem Aufstecken sichtbar. Der lange Decoderkörper zeigt von der Stiftleiste über die freie Trägerfläche weg von Lautsprecher-/SUSI-Buchsen. Die Stifte treten von unten durch die Decoderplatine ein.')
    ns['step']('E3','Index und Sitz kontrollieren.','Geschlossene Indexposition 11 am Decoder genau über die fehlende Stiftposition legen. Beide Reihen vor dem Drücken ansehen. Den Decoder an der Steckleiste parallel nach unten setzen. Bei Widerstand abheben und Lage prüfen; nicht drücken, bis es passt. Von der Seite alle eingeführten Stifte, geraden Sitz und Abstand zum Chassis kontrollieren. Erst nach den übrigen Freigaben in 54 einschalten.')
    ns['warn']('Die Decoder nicht zwischen den Köpfen vertauschen','Vorn 60977 auf LoDi 511; hinten 59649 auf Märklin-Träger. Einseitiger oder um eine Position versetzter Sitz ist kein Kontaktproblem, das durch mehr Druck behoben wird. Vor dem Abziehen immer die gesamte Versorgung trennen; gerade und gleichmäßig an den Kanten abheben, nicht mit Metall unterhebeln.')
    ns['refs'](1,6,10,15)

def axle_page(ns,page):
    page('14c. Optional: Achsschleifer an Wagen-B anschließen')
    ns['add']('Mit Achsschleifer ist eine Kontaktfeder an Metallachse/Rädern gemeint, kein Mittelschleifer. Diese Option lässt sich je Mittelwagen ergänzen; die LoDi-Platine bleibt unverändert. Sie ergänzt nur die örtliche Radmasse. Die beiden Kupplungspole bleiben RT und GE.')
    ns['table'](['An deiner weißen MT-37700 V4.3','Anschluss in diesem Zug'],[
        ('O an beiden Wagenenden','RT-Kupplungslitze / Mittelleiter. Niemals die Achskontaktlitze hier anlöten.'),
        ('L an beiden Wagenenden','GE-Kupplungslitze / Innenlicht-Schaltpfad. Achskontakt nicht hier anschließen.'),
        ('B am Ende mit Achskontakt','Optionale kurze Radkontaktlitze. Ohne Achsschleifer bleibt B frei.'),
        ('SJ2 / Türbeleuchtung','Bestehenden Zustand erhalten. Für den Achsschleifer keine Brücke setzen.')],[2.3,4.3])
    ns['step']('A1','Wagen trennen.','Wagen vollständig vom Gleis nehmen und an beiden Enden abkuppeln. Vorhandene Achskontaktfeder zunächst eingebaut lassen. Fotografiere Kontaktfeder, Befestigung und Leitung. An der LoDi-Leiste sind für diese Arbeit keine Kupplungslitzen oder Energiespeicher angeschlossen.')
    ns['step']('A2','Vorhandenen Kontakt identifizieren.','Folge der Feder bis zu der metallischen Achse/Radfläche, die sie berührt. Löse ihre Leitung von alter Beleuchtung, falls noch angeschlossen; das freie Ende darf keine Elektronik berühren. Prüfe die Radaufnahme nach 14d. Eine Achshalterung ist keine zu entfernende Massefeder.')
    ns['step']('A3','An B löten.','Nach bestandener Kontaktprüfung die kurze Radkontaktlitze an das mit B beschriftete Pad am zugehörigen Wagenende löten. Nicht an O, obwohl O in einer anderen LoDi-Anschlussvariante als Masse bezeichnet wird. Hier führt O den Mittelleiter. Die unveränderten Kupplungslitzen nach 14b an O/RT und L/GE anschließen.')
    ns['step']('A4','Leitung führen.','Vom Drehgestell eine kleine Bewegungsschlaufe zum B-Pad lassen. Drehgestell stromlos in beide Endlagen schwenken: Litze darf nicht spannen, am Rad streifen oder zwischen Boden und Gehäuse geraten. Nicht direkt an der Metallachse löten und keine neue Längsader durch den Wagen legen.')
    ns['step']('A5','Zweiten Kontakt getrennt behandeln.','Wenn am anderen Wagenende eine zweite vorhandene Radkontaktfeder genutzt wird, deren eigene kurze Litze nach Einzelprüfung an das dortige B-Pad führen. Keine interne B-B-Durchleitung und keinen dritten Zugbus voraussetzen; keine Brücke von B nach O oder L setzen.')
    ns['warn']('Für einen 2976-Wagen ohne vorhandene Feder noch keine Ersatzteilnummer bestellen','Fotografiere Unterseite, Drehgestell innen, Achslager und mögliche Federaufnahme mit Maßstab. Damit die passende originale Märklin-Kontaktfeder bestimmen lassen; eine Nummer aus 33701 ist für deinen 2976 nicht automatisch passend. Bis dahin B frei lassen. Vorhandene Federn bleiben bei gewählter Radmasseoption erhalten.')
    ns['refs'](4)

def axle_test_page(ns,page):
    page('14d. Achskontakt prüfen und Rückmeldung testen')
    ns['add']('Die Kontaktmessung erfolgt vor dem Anschluss an B, ohne Elektronik. Sie prüft nur, ob die Feder die Achse/Räder zuverlässig erreicht. Der LoDi-Pfad wird anschließend wie eine bestückte Platine nach 14b geprüft, nicht mit einer pauschalen OL-Forderung zwischen B, O und L.')
    ns['table'](['Reihenfolge','Handgriff und Ergebnis'],[
        ('1. Messgerät kontrollieren','Schwarz COM, Rot V/Ω. Ω-Bereich wählen, Spitzen zusammenhalten und trennen; beide Zustände müssen klar unterscheidbar sein.'),
        ('2. Bezugspunkte am Radsatz','Zwei zugängliche, blanke Metallstellen desselben leitenden Achs-/Radpfads wählen und den Durchgang zwischen ihnen vorprüfen. Nicht an Kunststoff, Haftreifen oder Lack messen.'),
        ('3. Radkontakt messen','Freies Ende der abgetrennten Federlitze gegen den positiv bestätigten Metallpfad messen. Niedrigen stabilen Wert notieren. Klemmen müssen sicheren Kontakt haben.'),
        ('4. Mehrere Radstellungen','Achse vorsichtig drehen, erneut Kontakt und Messwert prüfen. Nicht das Drehgestell unter Spannung bewegen. Bei offenem oder springendem Wert Kontaktfläche/Federsitz prüfen; nicht stärker anpressen oder verbiegen, um einen Fehler zu verdecken.'),
        ('5. Nachprobe','Die positive Verbindung der Metall-Bezugspunkte und Geräteprobe wiederholen. Miss die Federlitze außerdem getrennt Ende-zu-Ende, wenn beide Enden zugänglich sind. Fehlgeschlagene Kontaktprobe: Reihe wiederholen, nicht als bestanden notieren.'),
        ('6. Nach Anschluss an B','Mit Lupe B-Lötstelle ansehen: kein Draht/Zinn zum Nachbarpad O oder L. Kontakt der Radfeder bis zur tatsächlichen B-Lötstelle prüfen; danach Drehgestell in beide Endlagen bewegen und Kontrolle wiederholen.')],[1.5,5.1])
    ns['warn']('Zusatznutzen prüfen, nicht unterstellen','Ein Achsschleifer verbessert nur die örtliche Radstromaufnahme. Er ersetzt weder RT über die Kupplung noch das Einschalten von GE. Die Feder kann den Rollwiderstand erhöhen. Wagen nach Einbau von Hand auf einem stromlosen geraden Gleis rollen lassen und mit dem vorherigen Zustand vergleichen; klemmt er, Federsitz und Litzenführung korrigieren.')
    ns['h']('Mit deinen Kontaktgleisen nach dem Fahrzeugumbau')
    ns['add']('Den tatsächlich verwendeten Kontaktabschnitt zuerst leer in der CS3 beobachten: frei. Dann den Wagen aufstellen: erwartete Belegtmeldung prüfen. Innenlicht aus und ein testen; danach den Wagen vollständig entfernen: wieder frei. Mit beiden Wagenorientierungen wiederholen. Eine zusätzliche Kontaktfeder macht isolierte Radsätze nicht automatisch rückmeldefähig. Bei einer unerwarteten Meldung erst Radsatztyp, Trennstellen und Leitungsziel B prüfen; nicht B mit O verbinden.')
    ns['refs'](4,12,16)

def light_mapping(ns,page):
    page('16a. Innenlicht ohne Richtungs-Unterbrechung')
    ns['add']('Der Richtungswechsel schaltet hier nur die beiden Stirnlichter um. RT wird nicht umgepolt und nicht zwischen den Schleifern umgeschaltet. Die weiße Wagenplatine erhält RT an O und den eigenständig geschalteten GE-Pfad an L. Deshalb ist kein konstruktives Umschaltloch für das Wagenlicht vorgesehen. Ob dein fertiger Zug tatsächlich ohne sichtbare Unterbrechung leuchtet, wird in 17a geprüft.')
    ns['table'](['Im ausgelesenen 60977-Fahrzeugprojekt','Für diesen Zug festlegen'],[
        ('Physischer Ausgang','Genau AUX4 oder AUX1 aus deinem Eintrag in 8a. Eine AUX-Nummer ist nicht die Nummer der Funktionstaste.'),
        ('Bedientaste in der CS3','Eine dokumentierte freie beziehungsweise bewusst übernommene Taste mit Namen Innenlicht. Rastend: nach Loslassen bleibt sie ein. Keine Moment-/Zeittaste.'),
        ('Ausgangsmodus','Dimmer, Modus 1 gemäß Märklin-Tabelle. Nicht Modus 19 dauerhaft einschalten: Dort wäre Ausschalten nur über STOP vorgesehen.'),
        ('Bedingungen','Mit eingeschalteter Taste, beide Richtungen, Stand und Fahrt. In der dokumentierten Tabelle entspricht keine zusätzliche Zustands-/Richtungsbeschränkung dem Bedingungswert 0. Nicht beide Einzelrichtungsbedingungen unklar kombinieren.'),
        ('Nicht zuordnen','Kein F0, Licht-vorne/Licht-hinten, Motorlauf, Richtungswechsel-Ereignis oder Timer als zusätzlicher Auslöser dieses AUX. Keine zweite konkurrierende Aktion auf denselben Ausgang.'),
        ('Helligkeit','Zunächst voll eingeschaltete, zulässige AUX-Stufe; Strom-/Lastgrenzen aus 18 beachten. Wagenhelligkeit am TRIMM-Potentiometer jeder LoDi-Leiste einstellen, nicht durch einen Blink-/Neon-/Zeitmodus.'),
    ],[2.2,4.4])
    ns['step']('I1','Projekt bearbeiten und rücklesen.','Nur den 60977 am Märklin-Werkzeug bearbeiten. Die Tabelle als Sollkarte neben das ausgelesene Funktionsmapping legen und Zeile für Zeile abgleichen. Firmwareabhängige CV-Tabellenwerte nicht blind als einzelne CVs schreiben. Projekt speichern, übertragen und erneut auslesen; den tatsächlich verwendeten AUX und die Tastennummer notieren. Die Jumper nicht verändern.')
    ns['step']('I2','Wagenhelligkeit einstellen.','Erst nach freigegebenem Erstbetrieb den Wagen wieder stromlos nehmen und die anfängliche TRIMM-Stellung fotografieren. Den Trimmer mit passender kleiner Spitze minimal verstellen, Werkzeug entfernen, wieder einschalten und vergleichen. Richtung/Endanschlag nicht erzwingen. Für jede weitere Korrektur erneut ausschalten. Danach Prüfung 17a durchführen.')
    ns['warn']('Nicht F4 mit AUX4 verwechseln','Die Werksbelegung des 60977 nennt F6 für AUX4 und F1 für AUX1; F4 schaltet die Anfahr-/Bremsverzögerung. Dein ICE-Soundprojekt kann abweichen. Verwende deshalb die im ausgelesenen Projekt festgelegte Innenlichttaste, nicht automatisch F4 oder F6.')
    ns['refs'](1,3,4,23)

def flicker_test(ns,page):
    page('17a. Abnahme: Wagenlicht beim Richtungswechsel')
    ns['add']('Nach den elektrischen Prüfungen und den Schritten 52-56: Zug auf einem einzigen zusammenhängenden CS3-Digitalstromkreis, Motor steht, Fahrstufe 0, automatische Ereignisse aus. Für den ersten Test beide 60974 abgesteckt lassen. Wagen und Kupplungen während der Standprüfung nicht berühren. Die ersten Tests mit offenem Gehäuse durchführen; nach Kapitel 24 am geschlossenen Zug wiederholen.')
    ns['table'](['Test','Du bedienst nur den gemeinsamen ICE-Eintrag','Bestanden, wenn'],[
        ('F1: Ausgangszustand','F0 aus, Sound aus, Innenlicht aus.','Alle Wagen dunkel.'),
        ('F2: Innenlicht einschalten','Innenlichttaste einmal ein, Finger weg; 30 Sekunden beobachten.','Alle Wagen leuchten weiter; kein Blinken oder zeitgesteuertes Erlöschen.'),
        ('F3: Richtung ohne Frontlicht','Bei Fahrstufe 0 zehnmal vorwärts und zurück schalten; je Zustand etwa 2 Sekunden warten.','Wagenlicht bleibt sichtbar unverändert; Motor steht.'),
        ('F4: Richtung mit Frontlicht','F0 ein und dieselben zehn Zyklen wiederholen.','Vorn/hinten Rot-Weiß wechselt korrekt; Wagenlicht bleibt unverändert.'),
        ('F5: F0 unabhängig','Nur F0 mehrfach aus/ein schalten; Innenlicht nicht bedienen.','Innenlicht reagiert nicht auf F0.'),
        ('F6: Sound als Zusatzlast','Zulässigen Sound leise einschalten; Richtungsprüfung im Stand wiederholen.','Kein Lichtausfall und kein Sound-Neustart/Decoder-Reset.'),
        ('F7: Innenlicht ausschalten','Nur die Innenlichttaste aus, danach wieder ein.','Alle Wagen gehen aus/ein; Frontlicht und Sound werden nicht mitgeschaltet.'),
        ('F8: Vollständiger Zug','Nach jedem weiteren Wagen wiederholen; endgültige Wagenzahl protokollieren.','Alle Wagen bestehen die Folge; nach Gehäuseschluss ebenfalls.')],[.7,3.1,2.8])
    ns['add']('<b>Bei einem Fehler:</b> Alle Wagen richtungsabhängig dunkel: 16a und GE-Anschluss prüfen. Nur ein Wagen oder alle ab einer Kupplung betroffen: stromlos nach 14a/14b eingrenzen. Lichtausfall mit Sound-Neustart: Stromaufnahme und Überlast untersuchen. Nur kurzer Einbruch trotz richtiger Zuordnung: tatsächlichen AUX-/Versorgungsverlauf fachkundig messen lassen; keinen Puffer auf Verdacht anlöten.')
    ns['warn']('Erst nach bestandenem Standtest den Fahrtest ergänzen','Bei kleinster Fahrstufe in beiden Richtungen zusätzlich Stand-Fahrt-Stand prüfen; erst bei stillstehendem Zug die Richtung wechseln. Danach vorhandene Weichen/Kurven langsam befahren. Das Ergebnis getrennt notieren: störungsfrei im Stand ist noch kein Nachweis für verschmutzte Kontakte während der Fahrt. Bis alle vorgesehenen Wagen bestehen, keine Flackerfreiheitsfreigabe eintragen.')
    ns['add']('Protokoll: Datum ______; Wagenzahl ______; AUX ______; Taste ______; ohne/mit optionalen Achskontakten ______; F1-F8 bestanden ______; Fahrtest ______. Ein bestandener Test bedeutet keine Garantie gegen jede spätere Verschmutzung oder Kontaktunterbrechung.','small')
    ns['refs'](1,3,4,23)
