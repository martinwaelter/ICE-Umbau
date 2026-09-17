from pathlib import Path
p=Path(__file__).with_name('build_rev16.py')
s=p.read_text()
s=s.replace('ICE_2976_REV16_KUPPLUNGEN_HLA_OHNE_SOUND.pdf','ICE_2976_REV16_MFX_EIN_DECODER_KUPPLUNGSLICHT.pdf')
s=s.replace("self.kind=='system'", "self.kind=='system'")
start=s.index("        if self.kind=='system':")
end=s.index("        elif self.kind in ('front','rear'):")
s=s[:start]+'''        if self.kind=='system':
            box(0,78,142,96,'Kopf A / Motor');txt(8,135,'60972 + HLA 60941');txt(8,114,'LoDi-514 lokal');txt(8,94,'AUX1/AUX2-Adapter')
            box(179,78,125,96,'Mittelwagen');txt(187,135,'Licht lokal versorgt');txt(187,114,'K1/K2 nur durchleiten')
            box(342,78,145,96,'Kopf B / motorlos');txt(350,135,'Dioden + Widerstände');txt(350,114,'LoDi-514');txt(350,94,'kein Decoder')
            for x,xx in [(142,179),(304,342)]:
                line(x,153,xx,153,RED);line(x,92,xx,92,TEAL);txt(x+3,158,'K1',7);txt(x+3,79,'K2',7)
            txt(0,55,'K1/K2: ausschließlich Kopflicht; kein Gleisstrombus RT/GE.',9)
            txt(0,36,'Ein mfx-Decoder steuert Motor, Frontlicht und hinteres Licht.',9)
            txt(0,17,'Wagenlicht braucht eigene Versorgung: Mittelschleifer und Radkontakte.',9)
        elif self.kind=='sender':
            txt(0,228,'Kopf A: zwei gleiche Zweige, voneinander getrennt',11)
            for yy,name,pull,series,k in [(175,'AUX1 / braun-rot','RP1','RS1','K1'),(65,'AUX2 / braun-grün','RP2','RS2','K2')]:
                txt(0,yy+48,'U+ / orange');line(117,yy+50,171,yy+50,RED)
                c.setStrokeColor(TEAL);c.rect(171,yy+45,64,10);txt(173,yy+65,pull+' 4,7 k',8)
                line(235,yy+50,272,yy+50);line(272,yy+50,272,yy)
                txt(0,yy+5,name);line(145,yy,316,yy)
                c.setFillColor(TEAL);c.circle(272,yy,2.7,fill=1,stroke=0)
                c.rect(316,yy-5,64,10,fill=0,stroke=1);txt(317,yy+15,series+' 1 k',8)
                line(380,yy,445,yy);txt(452,yy-3,k,10)
            txt(0,12,'RP: 0,5 W. RS: 1 W. U+ wird nur innerhalb von Kopf A angeschlossen.',9)
        elif self.kind=='receiver':
            txt(0,248,'Kopf B: Versorgung aus K1/K2; ohne Schleiferanschluss',10)
            # D1 and D2: both cathode bands join P; conventional triangle-like diode glyph avoided.
            for yy,label,d in [(211,'K1','D1'),(158,'K2','D2')]:
                txt(0,yy-3,label,10);line(28,yy,96,yy)
                c.setStrokeColor(TEAL);c.rect(96,yy-7,50,14,fill=0);line(137,yy-7,137,yy+7)
                txt(99,yy+14,d+' 1N4148',8);line(146,yy,210,yy);line(210,yy,210,185)
            line(210,185,350,185,RED);txt(218,199,'P = beide Ringseiten',9);txt(359,182,'VCC',10)
            box(350,39,137,130,'LoDi-514');txt(359,132,'red');txt(359,72,'white')
            for yy,label,r in [(128,'K1','RR'),(68,'K2','RW')]:
                txt(0,yy-3,label,10);line(28,yy,110,yy);c.rect(110,yy-5,64,10);txt(110,yy+12,r+' 47 k',8);line(174,yy,350,yy)
            txt(0,17,'D3/D4 zusätzlich direkt an LED-Pads: Anode red/white, Ringseite VCC.',9)
''' +s[end:]
# Retain inspected common pages 3-7; replace every architecture-dependent page.
def block(n):
    a=s.index(f'page({n},'); b=s.index(f'page({n+1},') if n<16 else s.index('def footer(')
    return s[a:b]
common={n:block(n) for n in range(3,8)}
common[5]=common[5].replace("note('Der hintere 60982 erhält keinen Motor. Seine orange und graue Motorleitung bleiben voneinander getrennt isoliert. Das ist ein anderer Farbcode als am 60972-Träger.')", "note('Im Kopf B wird kein Motor und kein Decoder eingebaut. Sein LoDi-514-Kopflicht ist gegenüber Fahrwerk, Schleifer und Wagenbeleuchtung vollständig isoliert.')")
common[6]=common[6].replace("('Rot, B/G rechts','Mittelschleifer A bzw. geprüfter B-Zug-Verteiler.')","('Rot, B/G rechts','Nur Mittelschleifer A; kein B-Zug über die Kupplungen.')")
common[6]=common[6].replace("('AUX1-4, GND, +5V, SUSI','In dieser Ausbaustufe ohne Anschluss; einzeln isolieren.')","('AUX1 / AUX2','Zum Zweileiter-Adapter auf Seite 8.'),('AUX3/4, GND, +5V, SUSI','Unbenutzt; einzeln isolieren.')")
common[7]=common[7].replace('einen 47-kOhm-Widerstand','den Widerstand RFw mit 47 kOhm').replace('einen zweiten an red','RFr mit 47 kOhm an red')
head=s[:s.index('page(1,')]
tail=s[s.index('def footer('):]
tail=tail.replace('vereinfachte Variante','ein Decoder / mfx').replace("'scope':'Vereinfachte Empfehlung, 60972/60982, DCC; Nutzerwahl offen'","'scope':'Nutzer bestätigt: mfx, keine Traktion, ein 60972, HLA 60941, LoDi-514, nur leitende Kupplungen; lokale Wagenversorgung zu prüfen'")
pages={}
pages[1]='''page(1,'ICE 2976: ein Decoder, mfx','Werkstattanleitung REV16, 16.09.2026. Deine gewählte Ausstattung: HLA-Motor 60941, ein 60972 ohne Sound und zwei LoDi-514. Keine LoDi-Motorplatinen, keine Traktion, keine zusätzlichen Kabel zwischen den Fahrzeugen.')
diagram('system')
table(['Parameter','Festlegung'],[('Motor / Decoder','60941 und 60972 im motorisierten Kopf A.'),('Anmeldung','Genau ein mfx-Decoder und ein CS3-Lokeintrag.'),('Kopflicht','F0 schaltet beide Köpfe; automatisch Weiß/Rot nach Fahrtrichtung.'),('Hinterer Kopf','Passiver Dioden-/Widerstandsadapter, keine Decoderanmeldung.'),('Kupplungen','Zwei Kontakte ausschließlich für die hintere Kopfbeleuchtung.'),('Wagenlicht','Bestehende Beleuchtung lokal aus Mittelschleifer + Radkontakten.'),('Motorstrom','Nur Schleifer A; beide Schleifer sind nicht parallel verbunden.')],[112,375])
note('<b>Voraussetzung für diese konkrete Ausführung:</b> Die zwei Kupplungspole sind vom Wagenlicht und Gleisstrom frei. Jeder beleuchtete Mittelwagen benötigt seine eigene vollständige Stromaufnahme. Nur Achskontakte genügen nicht. Fehlen Mittelschleifer, ist die Material-/Versorgungsfrage auf Seite 11 vor Einbau zu lösen.')
p('Die Zweileiterschaltung ist eine eigene Auslegung. Ihre Zustände sind rechnerisch und mit SPICE geprüft; die Abnahme am echten Decoder und Zug folgt auf den Seiten 14-15. Das ist keine Herstellerfreigabe und kein vorgetäuschter Hardwaretest.',True)

'''
pages[2]='''page(2,'Bauteile und Werkzeug bereitlegen','Bestellnachweise und tatsächlichen Besitz getrennt behandeln. Der 60972 wurde von dir als vorhanden genannt. Alles Weitere vor Arbeitsbeginn auf den Tisch legen.')
table(['Bauteil','Menge / Verwendung','Bestand'],[('Märklin 60972','1 mit 21MTC-Träger','Vorhanden laut Nutzer.'),('Märklin 60941','1 vollständiger HLA-Satz','Bestellt; Vollständigkeit prüfen.'),('LoDi-514','1 Set mit zwei Frontmodulen','Bestellt; geliefert bereitlegen.'),('E395640','2 für Triebköpfe','Versand angegeben; Passung prüfen.'),('E374060 / E374340','4 bestellte Paare; Bedarf nach Wagenzahl','Als zugestellt angegeben.'),('RFw, RFr, RR, RW','4 x 47 kOhm, 0,25 W, 5 % oder besser','Zusätzlich erforderlich.'),('RP1, RP2','2 x 4,7 kOhm, 0,5 W, 5 % oder besser','Zusätzlich erforderlich.'),('RS1, RS2','2 x 1 kOhm, 1 W, 5 % oder besser','Zusätzlich erforderlich.'),('D1-D4','4 x 1N4148, bedrahtet','Zusätzlich erforderlich.'),('Isolierende Montage','Lötstützpunkte, Schrumpfschlauch, Feinlitze','Bestand nicht belegt.')],[120,205,162])
p('Die kleine Adapterschaltung benötigt keine LoDi-Platine. Sie wird auf isolierten Lötstützpunkten oder einem kleinen Stück Lochraster befestigt. Ein ESU-Decoder ist in dieser Ausführung nicht erforderlich. 60977, 60982, LoDi-511/512 und LoDi-510 bleiben ungenutzt.')
p('Werkzeug: Multimeter, feine Lötstation, Entlötlitze, Schraubendreher, Pinzette, Lupe und isolierende Unterlage. Die CS3 übernimmt Anmeldung und Einrichtung über mfx; ein Windows-PC oder ESU-LokProgrammer ist für diesen Hauptweg nicht nötig.')
note('Für die Startauslegung muss die verwendete CS3-/Netzteilkonfiguration eine maximale Spannung von 24 V am Lichtkreis einhalten. Den Netzteiltyp und die passende CS3-Einstellung prüfen. Ein beliebiger Multimeterwert am Digitalgleis belegt keine Spitzenspannung.')

'''
pages.update(common)
pages[8]='''page(8,'Adapter vorn: zwei Steuerleitungen','Für das hintere Kopflicht werden die verstärkten AUX1/AUX2 benutzt. Die vorderen LEDs bleiben getrennt an LV/LR. Das verhindert, dass ihre LED-Zweige als ungewollte Versorgung des hinteren Kopfes mitwirken.')
diagram('sender',245)
steps(['RP1 (4,7 kOhm / 0,5 W) zwischen U+ orange und AUX1 braun/rot löten. RP2 gleichartig zwischen U+ und AUX2 braun/grün löten. Das sind absichtliche Widerstandsverbindungen, keine Drahtbrücken.',
'Von AUX1 über RS1 (1 kOhm / 1 W) zum Kupplungskontakt K1 gehen. Von AUX2 über RS2 zum Kontakt K2 gehen. Die Reihenfolge ist wichtig: RP am AUX-Knoten, RS zwischen diesem Knoten und Kupplung.',
'Alle Bauteile zugentlastet und isoliert befestigen. Widerstände nicht in engen Kontakt zu Gehäusekunststoff oder Decoder legen. Im normalen Betrieb entstehen an einem RP bei 24 V höchstens etwa 0,13 W.',
'An K1/K2 darf kein bisheriger RT-, GE-, Mittelschleifer- oder Innenlichtanschluss mehr hängen. Beide Leitungen bis zur nächsten Kupplung durchmessen.'])
note('<b>Funktion:</b> Ein eingeschalteter AUX zieht seinen Zweig nach Decoder-Minus. Der Widerstand RP hält den ausgeschalteten anderen Zweig auf Plus. Dadurch liegt zwischen K1 und K2 eine richtungsabhängige Spannung. Bei beiden AUX AUS verschwindet die Spannungsdifferenz und das hintere Licht erlischt.')

'''
pages[9]='''page(9,'Adapter hinten: Dioden und LoDi-514','Kopf B braucht für sein Kopflicht weder Radkontakt noch Schleifer. Die Energie kommt zusammen mit der Farbauswahl über K1/K2. VCC hier ist der lokale Punkt P des Adapters, nicht Fahrzeugmasse.')
diagram('receiver',265)
table(['Bauteil / Punkt','Verbindung'],[('D1','Anode ohne Ring an K1; Kathode mit Ring an P.'),('D2','Anode ohne Ring an K2; Kathode mit Ring ebenfalls an P.'),('P','An VCC der LoDi-514; keine weitere Verbindung.'),('RR, 47 kOhm','Zwischen LoDi red und K1.'),('RW, 47 kOhm','Zwischen LoDi white und K2.'),('D3, Sperrspannungsschutz','Anode an red-Pad; Ringseite direkt an VCC/P.'),('D4, Sperrspannungsschutz','Anode an white-Pad; Ringseite direkt an VCC/P.')],[179,308])
p('D1 und D2 müssen mit ihren Ringseiten zusammenlaufen. D3/D4 liegen direkt parallel zu den jeweiligen LED-Zweigen in Gegenrichtung: alle vier Ringseiten gehören an P. Die Schutzdioden begrenzen die negative LED-Spannung. Den Ring vor Einbau mit Lupe prüfen; im Diodentest leitet eine lose 1N4148 von roter Prüfspitze an der Anode zur schwarzen an der Ringseite.')
note('K1/K2 nur an diese passive Schaltung anschließen. Die bisherigen elektrischen Anschlüsse der alten hinteren Lichtumschaltung werden getrennt und isoliert. Ein vorhandener hinterer Schleifer kann mechanisch bleiben, sein Kopflichtanschluss bleibt isoliert.')

'''
pages[10]='''page(10,'Kupplungen als Lichtverbindung','Die beiden Kupplungspole erhalten neue Funktionen: K1 und K2. Alte Farbbezeichnungen RT/GE dürfen nicht als elektrische Belegung übernommen werden. In den Wagen wird nur kontaktgleich durchgeleitet.')
diagram('coupling')
steps(['Alle Fahrzeugübergänge zählen und die mechanisch passenden Kupplungen trocken einsetzen. Männliche/weibliche Gegenseite, Halterhöhe und seitliche Beweglichkeit prüfen. Unpassende Teile nicht unter Spannung mit Gewalt einpassen.',
'Alle bisherigen Verbraucher und Schleiferverbindungen von den beiden Durchgangsleitungen trennen. Die örtliche Wagenbeleuchtung bleibt ein eigener Stromkreis, Seite 11. Keine Kupplung darf die neuen Lichtsignale mit Gleisspannung verbinden.',
'Am noch von Adaptern und LEDs getrennten Kabelbaum K1 vom ersten bis zum letzten Fahrzeug niederohmig messen; anschließend K2. Jeden Wagen einzeln ergänzen und dieselbe Zuordnung erhalten.',
'K1 gegen K2, gegen alle Radkontakte und gegen jeden Mittelschleifer messen: kein Durchgang. Kupplungen und Drehgestelle dabei bewegen. Die Messung gilt für den unbestückten Kabelbaum, nicht für angeschlossene Halbleiter.',
'Erst nach bestandenem Test Adapter A und B verbinden. Wagenübergänge bei ausgeschalteter Gleisspannung kuppeln. Kein zusätzliches Kabel außen neben den Kupplungen führen.'])
note('K1 und K2 sind vollständig für das Kopflicht belegt. Ein paralleler Motor-Strombus beider Schleifer oder eine neue Wagenlichtversorgung über dieselben Pole ist in dieser Schaltung nicht enthalten. Das erklärt den Unterschied zur früheren RT/GE-Planung.')

'''
pages[11]='''page(11,'Mittelwagen versorgen ihr Licht selbst','Du möchtest die vorhandene Wagenbeleuchtung über die eigenen Stromabnehmer weiterbetreiben. Dafür braucht jeder Wagen eine vollständige Versorgung. Rad-/Achsschleifer allein liefern bei Märklin nur den Außenschienenanschluss.')
table(['Versorgung im Wagen','Erforderlicher Anschluss'],[('Mittelschleifer unter dem Wagen','Gleismitte B zum vorhandenen Lichtkreis.'),('Rad-/Achskontakte','Außenschienen 0 zum vorhandenen Lichtkreis.'),('Kupplung K1/K2','Nur Kopflicht durchleiten, keine Verbindung zum Wagenlicht.'),('Vorhandene Lampen/Platine','Für dauernde Digitalspannung geeignet; Polung und Nennspannung prüfen.')],[188,299])
steps(['Unter jeden beleuchteten Wagen schauen: Ist ein eigener Mittelschleifer vorhanden? Danach die Rad-/Achskontakte prüfen. Beides fotografieren und mit dem Multimeter bis zum Lichtkreis verfolgen.',
'Wenn der Lichtkreis bereits unabhängig aus diesen beiden Anschlüssen gespeist wird, bleibt er so bestehen. Eventuelle zusätzliche Verbindungen zur Kupplung trennen, damit die zwei neuen Lichtleitungen frei sind.',
'Wenn der Mittelschleifer fehlt, ist die lokale Versorgung noch nicht vollständig. Einen zum konkreten Wagen passenden Schleifer mit Halter nachrüsten oder das Versorgungskonzept neu festlegen. Keine Artikelnummer ohne Zuordnung zum Wagen bestellen.',
'Nennspannung der bestehenden Lampen bzw. Platine feststellen. Einen Wagen kurz allein auf Digitalgleis testen, ausschalten und die Lampensitze auf ungewöhnliche Erwärmung prüfen. Wagen danach einzeln ergänzen.'])
note('<b>Noch nicht belegt:</b> Aus deiner Angabe zu den Achsschleifern geht die Existenz eigener Mittelschleifer nicht sicher hervor. Die Zweileiter-Kopflichtschaltung ist deshalb an diese Vorprüfung gebunden. Fehlen sie, ist die vollständige Materialliste noch offen. Die Anleitung behauptet nicht, dass Radkontakte allein Licht erzeugen können.')
p('Vorteil der örtlichen Versorgung: unabhängige Stromkreise und freie Kupplungspole. Nachteile: mögliche Kontaktflackerer, Schleiferreibung und Wagenlicht ohne neue gemeinsame F-Tasten-Schaltung. Dafür bleiben die vorhandenen Leuchtmittel und ihre Innenverkabelung weitgehend erhalten.',True)

'''
pages[12]='''page(12,'60972 anmelden und einrichten','Nur ein Decoder wird eingebaut. Deshalb genügt die normale mfx-Anmeldung an deiner CS3. Weder eine gemeinsame DCC-Adresse noch ein ESU-Slave oder eine Traktion ist erforderlich.')
steps(['Kopf A nach bestandenem Motor-/Isolationscheck allein auf einen vollständig isolierten Prüfabschnitt stellen. Hinteren Adapter zunächst abgekoppelt lassen. CS3 einschalten und mfx-Anmeldung abwarten.',
'Die neue Lok eindeutig ICE 2976 nennen. Firmware-/Decoderdaten und Ausgangseinstellungen sichern. In der CS3-Lokbearbeitung die Konfiguration des angemeldeten Decoders vollständig lesen.',
'Den Motorbereich auf HLA/C90 einstellen. Für den 60972 nennt die DCC-Tabelle dazu Motortyp 3; unter mfx die entsprechende Motorprofil-Auswahl benutzen. Einen fremden CV-Satz nicht blind laden.',
'Anfahrzeit zunächst etwa 7 Sekunden, Bremszeit etwa 5 Sekunden einstellen. Höchstgeschwindigkeit zunächst begrenzen und erst nach einem sauberen Fahrtest erhöhen. Feinabgleich des Motors ist individuell.',
'mfx aktiviert lassen. Analogbetrieb für diese digitale Ausführung ausschalten. Die beiden Lichtausgänge und AUX1/AUX2 nach der nächsten Seite einrichten.'])
table(['Parameter','Ziel'],[('Decoderanzahl','1: Märklin 60972.'),('Aktives Fahrprotokoll','mfx; automatische Anmeldung.'),('Traktion / Slave','Keine.'),('Motor','60941, HLA/C90-Startprofil.'),('Frontausgänge','LV und LR, richtungsabhängig mit F0.'),('Hintere Lichtsteuerung','AUX1 und AUX2, ebenfalls F0-richtungsabhängig.'),('AUX3/4','Frei, unbeschaltet.'),('Lichteffekt / Dimmen AUX1/2','Normales Dauerlicht, 100 %, kein Blinken, kein Timer.')],[184,303])
note('Die Widerstände begrenzen den LED-Strom. Dimmen ersetzt keine Vorwiderstände. AUX1/AUX2 für die Zweileiterschaltung nicht als Kupplungsimpuls, Blinklicht oder unabhängig schaltbare Zusatzfunktion betreiben.')

'''
pages[13]='''page(13,'F0 und Fahrtrichtung zuordnen','Alle vier Ausgänge reagieren auf dieselbe Funktion F0. Die Auswahl hängt von der Richtung ab, nicht von der Geschwindigkeit. Die Bedingung muss deshalb jeweils im Stand und während der Fahrt gelten.')
table(['F0','Zugrichtung','Ausgänge EIN','Resultat'],[('AUS','beliebig','keine','Beide Köpfe dunkel.'),('EIN','A voraus / vorwärts','LV und AUX1','A weiß, B rot.'),('EIN','B voraus / rückwärts','LR und AUX2','A rot, B weiß.')],[48,143,117,179])
steps(['In der Funktionszuordnung von F0 die vorhandenen LV/LR-Einträge kontrollieren. LV darf nur bei Vorwärts aktiv sein; LR nur bei Rückwärts. Beide müssen auch im Stand schalten.',
'Zu F0 einen Ausgang AUX1 mit Bedingung Vorwärts ergänzen. AUX2 mit Bedingung Rückwärts ergänzen. Wenn die Oberfläche getrennte Bedingungen für Stand/Fahrt anbietet, beide Zustände aktivieren.',
'Werkseitige oder frühere unabhängige Zuweisungen von F1 zu AUX1 und F2 zu AUX2 entfernen. Sonst kann eine zusätzliche Taste das hintere Licht ungewollt übersteuern.',
'Bei AUX1/AUX2 den normalen verstärkten Lichtausgang mit voller Helligkeit, ohne Timer und ohne Sonderwirkung einstellen. Die sichtbaren Menünamen können mit Firmware und Decoderprojekt variieren; maßgeblich ist die obige Zustandstabelle.',
'Bei stehendem Kopf A zunächst am Sender prüfen: F0 AUS ergibt zwischen K1/K2 nahezu 0 V. F0 EIN vorwärts macht K2 gegenüber K1 positiv; rückwärts macht K1 gegenüber K2 positiv.'])
h('Messung ohne LED-Last')
p('Multimeter auf Gleichspannung stellen, rote Spitze K2, schwarze K1. Vorwärts wird ein positiver, rückwärts ein negativer Wert erwartet. AUS liegt nahe 0 V. Die Messspitzen vorher stromlos anklemmen. Zeigt AUS eine dauerhafte Spannung, zuerst Mapping und Verdrahtung korrigieren; Kopf B noch nicht anschließen.')
note('AUX1/AUX2 sind hier eigene Ausgänge für den hinteren Adapter. Sie werden nicht mit LV/LR zusammengelötet. Das hintere Rot/Weiß wird durch K1/K2 und den passiven Adapter bestimmt, nicht durch einen zweiten Decoder.')

'''
pages[14]='''page(14,'In kleinen Stufen einschalten','Die folgenden Tests sind Bestandteil des Einbaus. Eine Simulation belegt die Logik der Schaltung, kann aber falsche Lötstellen, unpassende Bauteile und reale Decoder-Effekte nicht ausschließen.')
diagram('test')
steps(['Lose C-Gleise vollständig von der Anlage trennen. CS3 ausschalten und nur den Programmierausgang anschließen: B an Mittelleiter, 0 an Außenschienen. Keine Verbindung zu Booster oder zweiter Versorgung.',
'Kopf A allein prüfen: mfx, vorderes Licht und langsame Motorbewegung. Danach den Sender ohne hinteren Adapter gemäß Seite 13 messen.',
'Strom aus. Hinteren Adapter zuerst außerhalb des Fahrzeugs über die vorbereiteten K1/K2-Leitungen anschließen. F0 AUS sowie beide Richtungen testen. Vorwärts nur red, rückwärts nur white.',
'LED-Ströme durch Gleichspannungsmessung über RR und RW prüfen: I = U/R. Bei 47 kOhm entsprechen 10 V etwa 0,21 mA. Der jeweils ausgeschaltete Farbzweig darf nicht sichtbar leuchten. Bei falschem Verhalten ausschalten und Diodenrichtung prüfen.',
'Adapter isoliert in Kopf B einbauen. Danach jeden Wagenübergang einzeln ergänzen und alle drei Lichtzustände wiederholen. Wagenlicht bleibt elektrisch separat.',
'Für Fahrtests ein ausreichend langes freies Gleis/Oval am Hauptgleisausgang benutzen. Vor dem Umstecken ausschalten und Programmiergleisanschluss vollständig lösen.'])
note('Eine automatische Motor-Einmessfahrt ist erst auf einem freien geeigneten Oval zulässig; Märklin empfiehlt Radien über 430 mm. Sie kann stark beschleunigen. Für die erste kurze Prüfung ist sie nicht nötig. Kein dauerhaftes Fahren auf dem kurzen Tisch-Prüfabschnitt.')

'''
pages[15]='''page(15,'Abnahme, Vorteile und Grenzen','Nach dem Gehäuseschluss sämtliche Lichtzustände und die langsame Fahrt erneut prüfen. Nicht eingeschaltete Farbzweige müssen dunkel bleiben; die Farben beider Köpfe müssen zur tatsächlichen Fahrtrichtung passen.')
table(['Abnahme','Soll / Eintrag'],[('F0 AUS','Beide Köpfe dunkel: __________'),('F0 EIN / A voraus','A weiß, B rot: __________'),('F0 EIN / B voraus','A rot, B weiß: __________'),('STOP, aus/ein, Richtungswechsel','Licht reagiert wieder korrekt: __________'),('Kurven / Gegenkurven langsam','Kein Kontaktabbruch/Kurzschluss: __________'),('5-10 Minuten Probefahrt','Motor, Widerstände und Lampensitze unauffällig: __________'),('Wagenlicht unabhängig','Mittelschleifer und Radkontakte vorhanden/geprüft: __________')],[239,248])
table(['Vorteil','Nachteil / praktische Grenze'],[('Ein mfx-Eintrag ohne Traktion','Nur der vordere Schleifer speist den Motor.'),('Ein Decoder statt komplexer Synchronisation','Kleine selbst zu lötende Adapterschaltung nötig.'),('Zwei vorhandene Kupplungspole genügen','Beide Pole sind vollständig durch Kopflicht belegt.'),('Keine zusätzliche Leitung zwischen Wagen','Mittelwagen brauchen ihre eigene komplette Lichtversorgung.'),('Hochleistungsmotor und automatischer Lichtwechsel','Motorabgleich und tatsächliche Probefahrt bleiben nötig.'),('Keine LoDi-Motorplatinen, kein Sound','Kein zentral geschaltetes neues Wagenlicht in dieser Stufe.')],[239,248])
p('Bei zu schwachem Licht: zuerst Gehäuse/Lichtleiter prüfen. Die 47-kOhm-Widerstände sind eine stromarme Startauslegung; hellere Einstellung braucht den zulässigen LED-Zweigstrom. Bei falscher hinterer Farbe: K1/K2-Zuordnung und Mapping prüfen. Bei Flackern hinten: Kupplungskontakte prüfen. Bei Flackern im Wagen: seine eigenen Stromabnehmer prüfen.',True)
note('<b>Bewertung:</b> Diese Ausführung erfüllt mfx, keine Traktion und möglichst wenig Elektronik am besten, sofern die Wagen lokal vollständig versorgt sind. Eine optimale gemeinsame Motor-Stromaufnahme aus beiden Schleifern ist damit nicht umgesetzt. Das ist der konkrete Preis dafür, beide vorhandenen Kupplungspole für das Kopflicht zu nutzen.')

'''
pages[16]='''page(16,'Nachweise und klare Ausführungsgrenzen','Die Schaltung wurde als eigene Auslegung erstellt. Motor-/Decoderanschlüsse und LED-Polarität stützen sich auf die Herstellerunterlagen. Referenzbilder sind als eigene Fotos oder Herstellervergleich gekennzeichnet.')
sources=[
('Q1','Märklin 60972/60982: Anschlüsse, Ausgänge, Motorprofil, mfx','https://static.maerklin.de/damcontent/93/1d/931db48faf5660916556d5172c598cdf1663856135.pdf'),
('Q2','Märklin 60941/60943: Original-Montagezeichnung','https://static.maerklin.de/damcontent/e3/bb/e3bb202fe80385cc96835d783af5e1821670919973.pdf'),
('Q3','LoDi ICE 1: Frontanschlüsse und Motorvergleichsfoto','https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/'),
('Q4','Märklin 60941: Trommelkollektor-Umrüstung','https://www.marklin.nl/producten/details/article/60941'),
('Q5','LoDi Front: ohne integrierte Vorwiderstände','https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/'),
('Q6','Vishay 1N4148: Polaritätsring und elektrische Daten','https://www.vishay.com/docs/81857/1n4148.pdf')]
for ident,title,url in sources:p(f'<b>{ident}</b> <link href="{escape(url)}" color="#087F86">{escape(title)}</link>',True)
h('Rechnung und Simulation')
p('Vier 47-kOhm-LED-Widerstände, 5 %: bei höchstens 24 V maximal 0,54 mA je Zweig ohne LED-Spannungsabzug. Hinterer Strom fällt durch Senderwiderstände und Diode kleiner aus. Je RP 4,7 kOhm: maximal etwa 0,13 W bei 24 V; gewählt 0,5 W. Je RS 1 kOhm: gewählt 1 W. Die Bauteile sind dennoch gegen Kunststoffkontakt und Kurzschluss zu isolieren.')
p('SPICE-Prüfung: 144 statische Fälle mit 12/18/24 V, vier AUX-Zuständen, drei gemeinsam variierten Widerstandstoleranzen und normal/offen/Kurzschluss K1-K2. Alle geprüften Zustände bestanden. Modellmaximum hinterer LED-Strom 0,421 mA; negative LED-Spannung unter 0,35 V. Repräsentative LED- und Schaltermodelle; keine Messdaten der echten LoDi-LEDs, keine vollständige transiente EMV- oder Temperaturprüfung.')
h('Noch am realen Modell zu prüfen')
p('Mittelschleifer der Mittelwagen, Kupplungspoltrennung, mechanische Passung, LED-Helligkeit, tatsächliches AUX-Verhalten und die endgültig geschlossenen Fahrzeuge. Die Seite 11 ist eine konkrete Bestandsprüfung, keine bereits bestätigte lokale Wagenversorgung. Ein fehlender Mittelschleifer macht einen zusätzlichen Versorgungsschritt notwendig.')
note('Die Dokumentfassung ist fertig. Ein vollständig nachgebauter und betrieblich freigegebener Zug wird damit nicht behauptet. Die Referenzfotos geben keine ungemessenen Lötpads der Originalplatine frei. Ein ESU-Slave bleibt eine andere, zusätzlich zu prüfende Architektur und ist nicht heimlich Voraussetzung dieser Anleitung.')

'''
p.write_text(head+''.join(pages[n] for n in range(1,17))+tail)
print('Updated final scope to one-decoder mfx with passive coupling adapter')
