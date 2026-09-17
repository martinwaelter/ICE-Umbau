"""Preserve the full manual and close the concrete REV8 execution gaps."""
from reportlab.platypus import Paragraph
import rev8_cv_integration

REPLACEMENTS = [
('REV8 erhält den vollständigen Umfang der REV7 und ergänzt Kapitel F zur CS3-CV-Programmierung. Kapitel F hat eigene Quellennummern. REV7 bleibt unverändert erhalten.',
 'REV9 bewahrt den vollständigen Bauumfang und Kapitel F. Ergänzt sind konkrete Montage-, Mess- und Ausgangsprüfungen. Kapitel F hat eigene Quellennummern. Frühere Fassungen bleiben unverändert erhalten.'),
('Nur den 60977 mit passendem Märklin-Aufbau am 60971 anschließen.',
 'Am 60971 zuerst den mitgelieferten Anschlussadapter abnehmen. Nur den 60977 am abgenommenen 21MTC-Adapter nach dessen Index und Märklin-Zeichnung S. 18 einsetzen. Dann Adapter samt Decoder an den Programmer stecken. Alle anderen Adapteranschlüsse bleiben frei; ausschließlich USB versorgt diesen Aufbau, keine CS3 oder weitere Quelle. Während des Betriebs keine Kontakte/Bauteile berühren. Nach dem Lesen zuerst Adapter abnehmen, dann Decoder abziehen.<super>24</super>'),
('Eine Drossel ist kein LED-Vorwiderstand.', 'Eine Drossel ist kein LED-Vorwiderstand. Die beiden vollständigen Motor-Leitungszweige nach 5a vorbereiten und in die Isolationsprüfung einbeziehen.'),
('Prüfzustand: 60941 montiert, Motorleitungen abgelötet, Decoder draußen', 'Prüfzustand: Motorleitungen von LoDi getrennt, Decoder draußen'),
('Rot für M1-Metall an PM1, für M2-Metall an PM2 stecken; Schwarz bleibt dabei am freien PX-Ende.',
 'Nur die Messleitungen an den freien Hilfsleitungsenden umstecken, wie in 6a angegeben. Schwarz bleibt ausschließlich bei den Isolationsmessungen 3 und 4 an PX; die Fahrzeugclips bleiben auch bei den Vor-/Nachproben fest.'),
('Du setzt hier den <b>Märklin 60977</b> ein, nicht den ESU 59649. Die Anweisung gilt für die im eigenen Foto gezeigte rote LoDi 511 mit der langen freien Decoderfläche. Platinenzuordnung und Befestigungsprüfung aus 8/9 müssen zuvor abgeschlossen sein.',
 'Diese Seite zeigt die spätere Lage des <b>Märklin 60977 auf LoDi 511</b>. Jetzt noch nicht einstecken. M1-M3 erst unmittelbar vor Schritt 52 ausführen, nach allen Löt-, Montage- und Widerstandsprüfungen sowie der getrennten Konfiguration bis 16b. Vorher bleibt der Decoder nur im bestätigten Programmieraufbau.'),
('Noch nicht einschalten. Erst die übrigen Anschluss-/Konfigurationskarten bis einschließlich 16a erledigen; danach Inbetriebnahme nach 17.',
 'Danach nur nach 17 einschalten. Vor jeder erneuten Löt- oder Widerstandsmessung Versorgung trennen und Decoder wieder abziehen.'),
('Beide Köpfe mit eingesetzten Lichtleitern und Gehäusen bei gleichem Umgebungslicht farbweise vergleichen. Den helleren Ausgang mit Decoder-Dimmung passend reduzieren. Rot und Weiß getrennt bewerten. Dabei muss der ungedimmte Einschaltstrom bereits sicher begrenzt sein.',
 'Erst nach offenen Funktionstests und bestandener Gehäuseprüfung nach 60/24 vergleichen. Gehäuse nur stromlos aufsetzen/abnehmen. Mit Lichtleitern und Gehäusen Weiß und Rot getrennt bei gleichem Umgebungslicht vergleichen; den helleren Ausgang dimmen. Für ESU-Änderungen gilt die eigene Mapping-Schreibkarte aus 12a, nicht CV191-195. Strombegrenzung muss ungedimmt sicher sein. Nach Änderung der Leitungslage Gehäuseprüfung wiederholen.'),
('Danach Indexposition von Träger und 59649 vergleichen.',
 'Danach die eigene Halterprüfung 12c ausführen und Indexposition von Träger und 59649 vergleichen.'),
('Am einzeln ausgelesenen 59649 die Funktionszuordnung entsprechend der Tabelle festlegen und speichern. Mapping-CVs per CS3 rücklesen (F.6); optional ESU-Programmer nutzen. Nicht auf spätere freie M4-Mappingbearbeitung an der CS3 vertrauen. Wenn das Mapping anders ist, diese Verdrahtung nicht ungeprüft übernehmen.',
 'Passt das in G0 geprüfte LV/LR-Mapping unverändert zur Tabelle, den gesicherten Zustand übernehmen; nicht vorsorglich neu programmieren. Für Änderungen zuerst einen geprüften 59649-Export mit CV31/CV32, CV-Nummer, Alt- und Zielwert als eigene Mapping-Schreibkarte erstellen. F.6 erklärt nur deren Übertragung, nicht die Mapping-Werte. Ohne diese Karte keine CVs raten; CS3-M4-Mapping nicht als freien Editor voraussetzen.'),
('ESU 59649 nach 12b einsetzen: Buchse oben, langer Decoderkörper über der freien Fläche des Märklin-Trägers; nicht über die Lautsprecher-/SUSI-Buchsen.',
 'Einsetzen erst unmittelbar vor Schritt 54 nach 12b und bestandener Halterprüfung 12c; bis dahin 59649 abgezogen lassen.'),
('Hier wird der <b>ESU 59649 LokPilot 5 M4 MKL</b> auf die separate Trägerplatine aus deinem 60977-Satz gesetzt.',
 'Diese Seite zeigt die spätere Stecklage des <b>ESU 59649 LokPilot 5 M4 MKL</b>. E1-E3 erst unmittelbar vor Schritt 54 ausführen, nach Halterprüfung 12c und allen Löt-/Widerstandsprüfungen. Er kommt auf die separate Trägerplatine aus deinem 60977-Satz.'),
('Am 60977 für deinen eingebauten 60941', 'Am 60977 für deinen eingebauten 60941'),
('Keine Bedingungen, die Bewegung voraussetzen, keine ungewollten Fade-Zeiten. Vorhandene konkurrierende Mappingzeilen beseitigen lassen.',
 'Keine Bewegungsbedingungen oder ungewollten Fade-Zeiten. Falls Änderungen nötig sind, gilt die separate geprüfte Mapping-Schreibkarte aus 12a; Synchronisations-CVs sind kein Lichtmapping.'),
('Ausgangsmodus, Tastenverhalten und Richtungsbedingungen nach 16a festlegen.',
 'Ausgangsmodus, Tastenverhalten und Richtungsbedingungen nach 16a festlegen; elektrische AUX4-Ausgangsart zusätzlich nach 16b prüfen.'),
('Nur bei G1 und bestätigter LED-Strombegrenzung:', 'Nur bei G1, bestandener Halterprüfung 12c und bestätigter LED-Strombegrenzung:'),
('Nach bestandener Kontaktprüfung die kurze Radkontaktlitze an das mit B beschriftete Pad am zugehörigen Wagenende löten.',
 'Zuerst die B-O/B-L-Ausgangswerte nach 14e sichern. Nach Kontaktprüfung die kurze Radkontaktlitze an B am zugehörigen Wagenende löten. B-Prüfung nach 14e wiederholen; erst nach bestandenem Vergleich Kupplungslitzen anschließen.'),
('Die unveränderten Kupplungslitzen nach 14b an O/RT und L/GE anschließen.', 'Die Kupplungslitzen bleiben bis zum B-Vergleich nach 14e abgetrennt; danach nach 14b an O/RT und L/GE anschließen.'),
('Der LoDi-Pfad wird anschließend wie eine bestückte Platine nach 14b geprüft, nicht mit einer pauschalen OL-Forderung zwischen B, O und L.',
 'Die zusätzlichen B-O/B-L-Vorher-/Nachherwerte werden nach 14e geprüft. 14b allein erfasst diese B-Pfade nicht. Keine pauschale OL-Forderung zwischen B, O und L.'),
('Mit Lupe B-Lötstelle ansehen: kein Draht/Zinn zum Nachbarpad O oder L. Kontakt der Radfeder bis zur tatsächlichen B-Lötstelle prüfen; danach Drehgestell in beide Endlagen bewegen und Kontrolle wiederholen.',
 'Lupe: kein Draht/Zinn von B nach O/L. Radfeder bis B auf Durchgang prüfen. Zusätzlich B-O/B-L-Vergleich nach 14e bestehen; erst dann Kupplungslitzen anschließen. Drehgestell in beide Endlagen bewegen und Kontrollen wiederholen.'),
('Je Lichtausgang / AUX1-AUX4', 'Je verstärktem Licht-/AUX1-AUX4-Ausgang'),
('Dies sind Decodergrenzen, keine Freigabe jeder Kupplung oder Leiterbahn.',
 '250 mA gelten nicht für einen Logikausgang; AUX4-Ausgangsart nach 16b prüfen. Dies sind Decodergrenzen, keine Freigabe jeder Kupplung oder Leiterbahn.'),
('60977 sitzt nach 9c;', '60977 erst jetzt nach 9c einsetzen;'),
('Beide Köpfe ungekoppelt auf dasselbe isolierte, gemeinsam gespeiste Gleisstück stellen;',
 '59649 erst jetzt nach 12b und Halterprüfung 12c einsetzen. Beide Köpfe ungekoppelt auf dasselbe isolierte, gemeinsam gespeiste Gleisstück stellen;'),
('Physischer Ausgang', 'Physischer Ausgang'),
('C90-Motortyp am 60977 rückgelesen: ______', 'C90-Motortyp rückgelesen: ______; Motorlitzen/Drosseln nach 5a geprüft: ______'),
('+Ub / LV / LR / B/GR / 0/GL und Steckindex abgeglichen: ______', '+Ub / LV / LR / B/GR / 0/GL, Steckindex und Halter 12c: ______'),
('Innenlicht-AUX aus 8a: ______', 'Innenlicht-AUX aus 8a: ______; elektrische Ausgangsart 16b: ______'),
('Prüfblätter 14a/14b: ______', 'Prüfblätter 14a/14b; bei B zusätzlich 14e: ______'),
]

def install(ns):
    rev8_cv_integration.install(ns)
    ns['SOURCES'][24]=('Märklin','Programmer 60971','S. 2-3: Adapterfolge und ausschließlich USB; S. 18: Anschlusszeichnung','https://static.maerklin.de/damcontent/21/3e/213ee6e47c4afa9ad2282158bf7728441660728698.pdf')
    ns['SOURCES'][1]=('Märklin','Nachrüstdecoder 60975/60976/60977','Stand 10/2025; Einbau und Grenzwerte; S. 16/21: CV51, AUX3/AUX4-Ausgangsart','https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf')
    prior_p=ns['p'];hits={a:0 for a,b in REPLACEMENTS if a!=b}
    def p(text,style='body'):
        result=prior_p(text,style);updated=result.text
        for a,b in REPLACEMENTS:
            if a in updated:
                if a!=b: hits[a]+=updated.count(a)
                updated=updated.replace(a,b)
        updated=updated.replace('REV8','REV9')
        return result if updated==result.text else Paragraph(updated,result.style)
    ns['p']=p;ns['REV9_HITS']=hits
    prior_page=ns['page']
    def page(title):
        if title=='6. Motorisolation: Messaufbau': motor_leads(ns,prior_page)
        # Prior hook emits 16a before 17. Emit 16b before 17's content via p-title interception below.
        return prior_page(title)
    ns['page']=page
    prior_step=ns['step']
    def step(number,title,text):
        if number in ('AUX1','AUX2','AUX3','AUX4'):
            number='I-A'+number[-1]
        return prior_step(number,title,text)
    ns['step']=step
    prior_table=ns['table']
    def table(headers,rows,widths):
        if headers==['Reihenfolge','Messpaar','Erwartung und Handlung']:
            pairs=[('PX2','PX'),('PM1','PM2'),('PM1','PX'),('PM2','PX'),('PX2','PX'),('PM1','PM2')]
            rows=[(r[0],f'Rot: {a}<br/>Schwarz: {b}',r[2]) for r,(a,b) in zip(rows,pairs)]
            headers=['Reihenfolge','Freie Leitungsenden','Erwartung und Handlung']
        return prior_table(headers,rows,widths)
    ns['table']=table
    # This outer wrapper adds 16b AFTER the existing 16a insertion by intercepting the base page helper.
    # Find the flowable boundary just emitted for 17 and insert our card before it.
    wrapped_page=ns['page']
    def final_page(title):
        additions={'13. Mittelwagenplatinen montieren':rear_holder,
                   '15. Den vorhandenen 60974 vorbereiten':axle_bridge,
                   '17. Erstes Einschalten ohne Puffer':electrical_aux}
        if title in additions:
            result=wrapped_page(title)
            header=ns['story'].pop();separator=ns['story'].pop()
            assert header.style.name=='h1'
            additions[title](ns,prior_page)
            ns['story'].extend([separator,header])
            return result
        return wrapped_page(title)
    ns['page']=final_page
    old_warn=ns['warn']
    def warn(title,text):
        if title=='Verbindlicher Dokumentstatus':
            result=old_warn(title,text)
            ending=ns['story'][-2:]
            del ns['story'][-2:]
            ns['refs'](24)
            ns['story'].extend(ending)
            return result
        return old_warn(title,text)
    ns['warn']=warn

def motor_leads(n,page):
    page('5a. Drosseln und Motorlitzen mitprüfen')
    n['add']('Nach Motormontage, vor 6: 60977/59649 und beide 60974 bleiben abgezogen. Diese Karte konkretisiert den Leitungsaufbau; sie ist keine zusätzliche Märklin-Bauanweisung. Verwende ausschließlich die zugeordneten mitgelieferten Entstördrosseln.')
    n['table'](['Zweig','SOLL vom Motor zur späteren Platine','Jetzt offen lassen'],[
        ('M1','Erste Bürstenfahne - erste Drossel - erste Motorlitze','Freies Ende noch nicht an MOT_L/MOT_R'),
        ('M2','Zweite Bürstenfahne - zweite Drossel - zweite Motorlitze','Freies Ende noch nicht an MOT_L/MOT_R'),
        ('FEHLER','Drossel zwischen M1 und M2 oder von einer Bürste zum Chassis','Nicht bestromen; Leitung nachverfolgen')],[.6,2.9,2.1])
    n['step']('D1','Beide Zweige aufbauen.','Je eine Drossel in jede Motorleitung einfügen. Ein Drosselanschluss führt ausschließlich zur zugehörigen Bürstenfahne, der andere zur entsprechenden Motorlitze. Reihenfolge und Befestigung dürfen den mechanischen Bewegungsraum nicht einschränken. Kein Drosseldraht an eine Masselötöse.')
    n['step']('D2','Blankstellen einzeln isolieren.','Vor dem Löten passende Schrumpfschläuche aufschieben; jede freie Lötstelle und jeden blanken Anschlussdraht gegen Metallkontakt schützen. Nach dem Abkühlen an den isolierten Leitungen vorsichtig den festen Sitz prüfen. Keine Isolierung wegdrücken, um eine Schraube einzusetzen. Litzen mit kleiner Bewegungsschlaufe führen; freie Enden einzeln isolieren.')
    n['step']('D3','Zuerst an den Bürsten messen.','Nach 6/6a an den beiden Bürstenfahnen prüfen. Beide fertig aufgebauten Zweige liegen bereits an ihrem endgültigen Ort, bleiben aber von LoDi getrennt. Für jede Gegenstelle und Lage gelten sämtliche sechs Vor-, Isolations- und Nachmessungen.')
    n['step']('D4','Dann die vollständigen Leitungszweige messen.','Nach der Bürstenmessung PM1 vom Motor an das freie Ende der ersten Motorlitze setzen, PM2 an das freie Ende der zweiten. PX/PX2 bleiben die jeweils bestätigten Gegenpunkte. Die ganze Folge aus 6a für sämtliche Gegenstellen und Bewegungsstellungen wiederholen. Die positive Motorprobe umfasst jetzt auch beide Drosseln und Litzen.')
    n['warn']('Ein bestandener nackter Motor reicht nicht','Nur wenn auch die fertig verlegten Drosseln, Lötstellen und Litzen bestehen, 6b abhaken. Jede spätere Änderung an diesen Teilen verlangt eine Wiederholung. Anschluss an MOT_L/MOT_R erst nach 6b/9a; Decoder weiterhin abgezogen.')
    n['add']('Protokollzusatz 6b: Bürstenprüfung ______; komplette Leitungszweige ______; Drehgestell-/Rotorlagen ______; Foto der isolierten Drosseln ______. Bei OL in einer positiven Motorprobe zuerst den unterbrochenen Pfad klären.','small')
    n['refs'](2,6)

def rear_holder(n,page):
    page('12c. Hinteren Märklin-Träger sicher halten')
    n['warn']('Eigene Montagefreigabe für den motorlosen Kopf','Die hohen Stützen und Schrauben der langen 2976-Altplatine sind keine bestätigte Aufnahme für den kleinen Märklin-Träger. Ein loser Träger oder ein nur von Litzen gehaltener Decoder wird nicht bestromt. 59649 erst vor Schritt 54 einsetzen.')
    n['step']('R1','Die tatsächlichen Teile dokumentieren.','Leeren Märklin-Träger und mitgelieferte Halteplatte aus dem 60977-Satz bereitlegen. Beide Seiten sowie den offenen Dummy mit Maßstab fotografieren. Die LoDi-Ringprüfung aus 9 gilt hier nicht. Vorhandene lose Platinen darfst du schon fotografieren; den Dummy für diese Architektur erst nach G0 öffnen.')
    n['step']('R2','Trocken einpassen.','Ohne Decoder und ohne Versorgung Träger mit seiner vorgesehenen Halteplatte auflegen. Mögliche Position so wählen, dass Radkontakte, Drehgestell, Lampeneinsatz und Dach frei bleiben. Noch keine Löcher bohren, keinen alten Metallhalter verbiegen und keine Altplatinen-Schraube probeweise festziehen.')
    n['step']('R3','Befestigung vor Ausführung festlegen.','Die genaue Halterung ist mangels Fotos deines Trägers im Dummy noch offen. Für die Freigabe müssen Halteplatte, Befestigungspunkt, Schraubentyp/-länge, zulässiger Anzug und freie Abstände dokumentiert sein. Reicht die vorhandene Halteplatte nicht, einen passenden isolierenden Halter bestimmen lassen; keine erfundene Ersatzteilnummer bestellen.')
    n['table'](['SOLL','FEHLER - so nicht einschalten'],[
        ('Träger sicher in passender Halterung; Unterseite und Decoder frei von unerwünschtem Metallkontakt','Lötpad auf Chassis, Schraube unter Decoder, Platine nur auf losen Isolierstreifen'),
        ('Keine Zugkraft auf B/GR, 0/GL, +Ub, LV/LR','Litzen tragen die Platine oder werden vom Dach heruntergedrückt'),
        ('Freie Bewegung in beiden Drehgestell-/Kupplungslagen','Isolierung scheuert an Kante, Schraube oder bewegtem Teil')],[1,1])
    n['step']('R4','Montage und Gehäuse getrennt prüfen.','Nach bestätigter Befestigung unerwünschte Metallkontakte vor und nach Montage kontrollieren. 0/GL ist absichtlich Radmasse und darf nicht pauschal als Isolationsfehler gelten. Andere Pfade nur mit abgetrennten Lasten beziehungsweise dokumentiertem Vorherwert bewerten. Die geschlossene Prüfung nach 24 kommt zusätzlich vor dem ersten Betrieb mit Gehäuse.')
    n['add']('Montagekarte: Halteplatte/Foto ______; Befestigungsort ______; Schraube/Länge ______; Abstände oben/unten ______; offene Kontrolle ______; geschlossene Prüfung 24 ______; geprüft durch/Datum ______. Ohne diese Festlegung bleibt ausschließlich die Montage des hinteren Trägers gesperrt, nicht das Fotografieren loser Teile.','small')
    n['refs'](1,6)

def axle_bridge(n,page):
    page('14e. Nach Achsschleifer-Löten: B-Brücken prüfen')
    n['add']('Diese Zusatzkarte gehört zu A3 in 14c und zur Nachkontrolle in 14d. Am einzelnen Mittelwagen: vollständig abkuppeln und vom Gleis nehmen; alle Kupplungslitzen und Energiespeicher von der weißen LoDi-Leiste trennen. Die Leiste bleibt bestückt und unverändert. Ausgangswerte zuerst OHNE angeschlossene Radkontaktlitze aufnehmen.')
    n['step']('B-P1','Messpunkte sichern.','Multimeter in Ω, Schwarz COM und Rot V/Ω. Geräteprobe zusammen/getrennt ausführen. B, O und L am betroffenen Ende eindeutig fotografieren. Für die Kontaktkontrolle jeden verwendeten Padkontakt gegen eine zweite blanke Stelle desselben großen Pads prüfen, ohne das Nachbarpad zu berühren. Sind keine sicheren zwei Kontaktstellen erreichbar, hier nicht mit einer scheinbaren Offenmessung freigeben.')
    n['table'](['Messung am selben Wagenende','Rot','Schwarz','Vorher','Nachher'],[
        ('1','B','O','________','________'),('2','O','B','________','________'),
        ('3','B','L','________','________'),('4','L','B','________','________'),
    ],[1.65,.5,.65,1,1])
    n['step']('B-P2','Vorherwerte aufnehmen.','Vor und nach jeder Reihe alle benutzten Padkontakte positiv kontrollieren. Messbereich, Polung, Wartezeit bis zur stabilen Anzeige und Wert notieren. Bei fehlgeschlagener Kontaktprobe die ganze Reihe wiederholen. Bauteile können richtungsabhängige oder veränderliche Werte erzeugen; deshalb kein generelles OL verlangen.')
    n['step']('B-P3','Eine Radkontaktlitze anlöten.','Erst jetzt die geprüfte Radlitze an B löten, abkühlen lassen und mit Lupe auf Draht-/Zinnreste zu O und L prüfen. Kupplungslitzen bleiben ab. Die vier Messungen unter denselben Bedingungen wiederholen, einschließlich positiver Kontaktkontrollen. Radlitze bis B separat auf Durchgang prüfen; normale Drehgestellbewegung prüfen.')
    n['warn']('Neu niederohmig oder unerklärlich anders: Wagen nicht anschließen','Die gerade hinzugefügte Radlitze wieder von B ablöten und einzeln isolieren. Lötstelle und Litze kontrollieren; erneut mit den Ausgangswerten vergleichen. Bleibt eine Abweichung, Messpunkte/Fotos an LoDi geben. Keine Leiterbahn auftrennen, kein Bauteil ausbauen und B niemals mit O/RT oder L/GE brücken.')
    n['step']('B-P4','Erst danach den Bus anschließen.','Für eine zweite Radlitze am anderen Ende eine eigene Vorher-/Nachherreihe durchführen; keine B-B-Verbindung voraussetzen. Erst nach bestandenen B-Prüfungen die Kupplungslitzen nach 14b an O und L anschließen. Bei bereits verdrahteten Wagen für die getrennte B-Prüfung zuerst wieder den beschriebenen spannungslosen Einzelzustand herstellen.')
    n['add']('Wagen/Ende ______; Gerät/Bereich ______; Wartezeit ______; Kontakt-Vor-/Nachproben ______; Vergleich ______; Datum/Prüfer ______. Die Messung deckt neue Lötbrücken auf, bestätigt aber keine unbekannte Schaltungsfunktion.','small')
    n['refs'](4)

def electrical_aux(n,page):
    page('16b. 60977: AUX4 muss verstärkt arbeiten')
    n['add']('Diese Karte gilt vor Anschluss der Mittelwagen und nach jeder Übertragung eines Sound-/Decoderprojekts. AUX-Nummer, elektrische Ausgangsart und Lichteffekt sind drei verschiedene Einstellungen. Dimmer-Modus 1 allein macht aus einem Logikausgang keinen belastbaren Schaltausgang.<super>1,3</super>')
    n['table'](['Bestätigte LoDi-Zuordnung aus 8a','Was für diesen ICE gilt'],[
        ('Innenlicht über AUX4','Am 60977 CV51, Bit4 = 0: verstärkter AUX4. Bit4 = 1 wäre ein Logikausgang und ist für den hier verwendeten Lastpfad nicht freigegeben.'),
        ('Innenlicht über AUX1','Für diesen Innenlichtpfad keine Änderung an AUX4 vornehmen. AUX1 und Mapping nach 16a prüfen; LoDi-Jumper unverändert lassen.'),
        ('Zuordnung noch unbekannt','Zuerst 8a schließen. Nicht vorsorglich CV51 ändern oder einen Jumper umlöten.')],[1.8,3.7])
    n['step']('AUX1','Altwert am richtigen Decoder sichern.','Nur den 60977 im bestätigten Märklin-Programmieraufbau verwenden; nicht den 59649. Wagen/LoDi-Lasten sind dabei nicht angeschlossen. Aktuelles Decoderprojekt und CV51 sichern. Die zitierte Märklin-DCC-Tabelle S. 21 nennt Bit4 mit Wertigkeit 16. Bei abweichender Firmware-/CV-Darstellung zuerst deren Tabelle abgleichen.')
    n['step']('AUX2','Nur Bit4 ändern, falls nötig.','Bisherigen CV51-Wert durch 16 teilen, ganzzahligen Anteil betrachten: gerade bedeutet Bit4 ist 0, Wert unverändert lassen; ungerade bedeutet Bit4 ist 1, genau 16 vom Altwert abziehen. Beispiel nur zur Rechnung: 24 wird 8, 8 bleibt 8. Niemals pauschal CV51 = 0 schreiben. Die übrigen Bits für Motor/Licht/Gleis und AUX3 müssen unverändert bleiben.')
    n['step']('AUX3','Schreiben und tatsächlich rücklesen.','Bevorzugt im Märklin-Projekt nur die elektrische AUX4-Ausgangsart auf verstärkt stellen und übertragen. Bei Einzel-CV-Programmierung ausschließlich den individuell berechneten Wert am 60977 schreiben; Decoderzuordnung doppelt prüfen. Danach CV51 neu auslesen: Zielwert stimmt, Bit4 ist 0, alle anderen Bits entsprechen dem gesicherten Altwert. Fehlendes Rücklesen ist keine Freigabe.')
    n['step']('AUX4','Nach Projekttransfer nochmals prüfen.','Ein späteres ICE-Soundprojekt kann die Ausgangsart erneut ändern. Deshalb nach dem letzten Transfer CV51 und 16a erneut kontrollieren. Erst dann Wagen schrittweise nach 56 und ohne 60974 nach 17a testen. Die Belastung des konkreten LoDi-/Kupplungspfads wird zusätzlich nach 18 geprüft.')
    n['warn']('250 mA sind keine Belastbarkeit eines Logikausgangs','Die Grenzwerttabelle des 60977 gilt hier für verstärkte Schaltausgänge. Ein Logikausgang darf nicht mit derselben Last betrieben werden. Ausgangsart, Gesamtstromgrenze und tatsächlicher LoDi-Strompfad getrennt bestätigen; keine Belastbarkeit aus der AUX-Bezeichnung ableiten.')
    n['add']('Protokoll: Innenlicht-AUX ______; Decoder 60977/Projekt ______; CV51 Alt ______; Bit4 Alt ______; Ziel ______; frisch rückgelesen ______; übrige Bits gleich ______; letzter Projekttransfer/Datum ______.','small')
    n['refs'](1,3)
