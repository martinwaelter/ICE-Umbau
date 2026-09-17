from pathlib import Path
from xml.sax.saxutils import escape
import json, hashlib
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, Flowable, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'output/pdf/ICE_2976_REV16_MFX_EIN_DECODER_KUPPLUNGSLICHT.pdf'
NAVY=colors.HexColor('#17354B'); TEAL=colors.HexColor('#087F86'); RED=colors.HexColor('#B4343C'); LIGHT=colors.HexColor('#EAF2F5')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Body16',fontName='Helvetica',fontSize=10.2,leading=14.3,spaceAfter=8,textColor=NAVY))
styles.add(ParagraphStyle(name='Small16',fontName='Helvetica',fontSize=8.2,leading=10.5,spaceAfter=5,textColor=NAVY))
styles.add(ParagraphStyle(name='Head16',fontName='Helvetica-Bold',fontSize=22,leading=26,spaceAfter=14,textColor=NAVY))
styles.add(ParagraphStyle(name='Sub16',fontName='Helvetica-Bold',fontSize=12,leading=15,spaceBefore=6,spaceAfter=7,textColor=TEAL))
story=[]; content=[]
def p(t,small=False):
    story.append(Paragraph(t,styles['Small16' if small else 'Body16']))
    content.append(t)
def h(t): story.append(Paragraph(t,styles['Sub16']));content.append(t)
def page(n,title,intro):
    if n>1: story.append(PageBreak())
    p(f'REV16  /  {n:02d}  /  WERKSTATT',True)
    story.append(Paragraph(title,styles['Head16']));content.append('\n## '+str(n)+' '+title)
    p(intro)
def steps(rows):
    for i,t in enumerate(rows,1): p(f'<b>{i}.</b> {t}')
def table(head,rows,widths=None):
    vals=[[Paragraph(escape(str(t)),styles['Small16']) for t in row] for row in [head]+rows]
    tb=Table(vals,colWidths=widths or [487/len(head)]*len(head),hAlign='LEFT')
    tb.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),LIGHT),('VALIGN',(0,0),(-1,-1),'TOP'),('BOX',(0,0),(-1,-1),.6,colors.HexColor('#BCD0D8')),('INNERGRID',(0,0),(-1,-1),.3,colors.HexColor('#D3DFE4')),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    story.extend([tb,Spacer(1,10)]);content.append(str([head]+rows))
def note(t):
    tb=Table([[Paragraph(t,styles['Body16'])]],colWidths=[487]);tb.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT),('LEFTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story.extend([tb,Spacer(1,8)]);content.append(t)
def photo(path,cap,maxh=180):
    path=ROOT/path; w,hh=ImageReader(str(path)).getSize(); fac=min(487/w,maxh/hh)
    story.append(Image(str(path),width=w*fac,height=hh*fac,hAlign='LEFT'));p(cap,True)
class Diagram(Flowable):
    def __init__(self,kind,height=190): super().__init__();self.kind=kind;self.width=487;self.height=height
    def draw(self):
        c=self.canv
        def txt(x,y,t,size=9,col=NAVY): c.setFillColor(col);c.setFont('Helvetica',size);c.drawString(x,y,t)
        def line(x,y,xx,yy,col=TEAL): c.setStrokeColor(col);c.setLineWidth(1.5);c.line(x,y,xx,yy)
        def box(x,y,w,hh,t): c.setFillColor(LIGHT);c.setStrokeColor(TEAL);c.roundRect(x,y,w,hh,5,fill=1,stroke=1);txt(x+8,y+hh-18,t,10)
        if self.kind=='system':
            box(0,78,142,96,'Kopf A / Motor');txt(8,135,'60972 + HLA 60941');txt(8,114,'LoDi-514 lokal');txt(8,94,'AUX1/AUX2-Adapter')
            box(179,78,125,96,'Mittelwagen');txt(187,135,'Licht lokal versorgt');txt(187,114,'K1/K2 nur durchleiten')
            box(342,78,145,96,'Kopf B / motorlos');txt(350,135,'Dioden + Widerstände');txt(350,114,'LoDi-514');txt(350,94,'kein Decoder')
            for x,xx in [(142,179),(304,342)]:
                line(x,153,xx,153,RED);line(x,92,xx,92,TEAL);txt(x+3,158,'K1',7);txt(x+3,79,'K2',7)
            txt(0,55,'K1/K2: ausschließlich Kopflicht; kein Gleisstrombus RT/GE.',9)
            txt(0,36,'Ein mfx-Decoder steuert Motor, Frontlicht und hinteres Licht.',9)
            txt(0,17,'Wagenlicht braucht eigene Versorgung: Mittelschleifer und Radkontakte.',9)
        elif self.kind=='sender':
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
            c.saveState();c.translate(0,55)
            txt(0,248,'Kopf B: Versorgung aus K1/K2; ohne Schleiferanschluss',10)
            # D1 and D2: both cathode bands join P; conventional triangle-like diode glyph avoided.
            for yy,label,d in [(211,'K1','D1'),(158,'K2','D2')]:
                txt(0,yy-3,label,10);line(28,yy,96,yy)
                c.setStrokeColor(TEAL);c.rect(96,yy-7,50,14,fill=0);line(137,yy-7,137,yy+7)
                txt(99,yy+14,d+' 1N4148',8);line(146,yy,210,yy);line(210,yy,210,185)
            line(210,185,350,185,RED);txt(218,199,'P = beide Ringseiten',9);txt(359,182,'VCC',10)
            box(350,39,137,185,'LoDi-514');txt(359,182,'VCC');txt(359,132,'red');txt(359,72,'white')
            for yy,label,r in [(128,'K1','RR'),(68,'K2','RW')]:
                txt(0,yy-3,label,10);line(28,yy,110,yy);c.rect(110,yy-5,64,10);txt(110,yy+12,r+' 47 k',8);line(174,yy,350,yy)
            c.restoreState()
            for xx,label,di in [(0,'red','D3'),(249,'white','D4')]:
                txt(xx,34,label,9);line(xx+37,37,xx+71,37)
                c.setStrokeColor(TEAL);c.rect(xx+71,30,50,14);line(xx+112,30,xx+112,44)
                txt(xx+75,50,di+' 1N4148',8);line(xx+121,37,xx+153,37);txt(xx+159,34,'P / VCC',9)
            txt(0,10,'D3/D4: Anode am Farbpad, Ringseite an P. Keine Verbindung zum Chassis.',9)
        elif self.kind in ('front','rear'):
            rear=self.kind=='rear';box(0,35,151,145,'60982 hinten' if rear else '60972 vorn')
            box(338,35,149,145,'LoDi-514')
            rows=[(142,'U+ blau' if rear else 'U+ orange','VCC / Plus',None),(101,'LV weiß' if rear else 'LV grau','red' if rear else 'white','R1'),(60,'LR gelb','white' if rear else 'red','R2')]
            for y,left,right,r in rows:
                txt(9,y+5,left);txt(347,y+5,right)
                if r:
                    line(151,y,214,y);c.setStrokeColor(TEAL);c.rect(214,y-5,58,10);line(272,y,338,y);txt(216,y+12,'47 kOhm',8)
                else: line(151,y,338,y,RED)
            txt(0,13,'Je Farbzweig ein eigener Widerstand. U+ niemals an Radmasse.',9)
        elif self.kind=='motor':
            box(0,45,129,120,'60972');box(340,45,147,120,'60941 HLA')
            txt(8,124,'grün / MV');txt(8,76,'blau / MR')
            for y in (118,70):
                line(129,y,198,y);c.setStrokeColor(TEAL);c.rect(198,y-5,55,10);txt(194,y+13,'Drossel',8);line(253,y,340,y)
            txt(350,123,'Bürstenanschluss 1');txt(350,74,'Bürstenanschluss 2')
            line(375,118,375,103);line(375,85,375,70);line(365,103,385,103);line(365,97,385,97);line(375,97,375,85)
            txt(388,96,'C',8);txt(0,19,'C nur zwischen den Bürsten; keine Bürstenverbindung zum Chassis.',9)
        elif self.kind=='test':
            box(0,100,130,66,'CS3');txt(8,117,'Programmierausgang')
            box(268,100,219,66,'lose C-Gleise auf dem Tisch');txt(277,117,'nur ein Triebkopf aufsetzen')
            line(130,141,268,141,RED);line(130,117,268,117)
            txt(152,148,'B / Mittelleiter',8);txt(152,104,'0 / Außenschienen',8)
            box(0,18,487,52,'Anlage elektrisch vollständig abgetrennt');txt(8,31,'Keine Verbindung zu Hauptgleis, Booster, Gleisbox oder anderem Netzteil.',9)
        elif self.kind=='coupling':
            for x,t in [(0,'Kupplung links'),(335,'Kupplung rechts')]: box(x,35,152,130,t)
            line(152,124,335,124,RED);line(152,74,335,74)
            txt(8,122,'K1 Kontakt');txt(343,122,'K1 Kontakt');txt(8,72,'K2 Kontakt');txt(343,72,'K2 Kontakt')
            txt(177,137,'Durchgang K1',9);txt(177,87,'Durchgang K2',9);txt(165,47,'K1 gegen K2: offen',9)
            txt(0,13,'Unbestückten Leitungsweg messen; Lampen/Elektronik vorher abtrennen.',9)
def diagram(kind,hh=190):story.append(Diagram(kind,hh));story.append(Spacer(1,8));content.append('[Schema '+kind+']')

page(1,'ICE 2976: ein Decoder, mfx','Werkstattanleitung REV16, 16.09.2026. Deine gewählte Ausstattung: HLA-Motor 60941, ein 60972 ohne Sound und zwei LoDi-514. Keine LoDi-Motorplatinen, keine Traktion, keine zusätzlichen Kabel zwischen den Fahrzeugen.')
diagram('system')
table(['Parameter','Festlegung'],[('Motor / Decoder','60941 und 60972 im motorisierten Kopf A.'),('Anmeldung','Genau ein mfx-Decoder und ein CS3-Lokeintrag.'),('Kopflicht','F0 schaltet beide Köpfe; automatisch Weiß/Rot nach Fahrtrichtung.'),('Hinterer Kopf','Passiver Dioden-/Widerstandsadapter, keine Decoderanmeldung.'),('Kupplungen','Zwei Kontakte ausschließlich für die hintere Kopfbeleuchtung.'),('Wagenlicht','Bestehende Beleuchtung lokal aus Mittelschleifer + Radkontakten.'),('Motorstrom','Nur Schleifer A; beide Schleifer sind nicht parallel verbunden.')],[112,375])
note('<b>Voraussetzung für diese konkrete Ausführung:</b> Die zwei Kupplungspole sind vom Wagenlicht und Gleisstrom frei. Jeder beleuchtete Mittelwagen benötigt seine eigene vollständige Stromaufnahme. Nur Achskontakte genügen nicht. Fehlen Mittelschleifer, ist die Material-/Versorgungsfrage auf Seite 11 vor Einbau zu lösen.')
p('Die Zweileiterschaltung ist eine eigene Auslegung. Ihre Zustände sind rechnerisch und mit SPICE geprüft; die Abnahme am echten Decoder und Zug folgt auf den Seiten 14-15. Das ist keine Herstellerfreigabe und kein vorgetäuschter Hardwaretest.',True)

page(2,'Bauteile und Werkzeug bereitlegen','Bestellnachweise und tatsächlichen Besitz getrennt behandeln. Der 60972 wurde von dir als vorhanden genannt. Alles Weitere vor Arbeitsbeginn auf den Tisch legen.')
table(['Bauteil','Menge / Verwendung','Bestand'],[('Märklin 60972','1 mit 21MTC-Träger','Vorhanden laut Nutzer.'),('Märklin 60941','1 vollständiger HLA-Satz','Bestellt; Vollständigkeit prüfen.'),('LoDi-514','1 Set mit zwei Frontmodulen','Bestellt; geliefert bereitlegen.'),('E395640','2 für Triebköpfe','Versand angegeben; Passung prüfen.'),('E374060 / E374340','4 bestellte Paare; Bedarf nach Wagenzahl','Als zugestellt angegeben.'),('RFw, RFr, RR, RW','4 x 47 kOhm, 0,25 W, 5 % oder besser','Zusätzlich erforderlich.'),('RP1, RP2','2 x 4,7 kOhm, 0,5 W, 5 % oder besser','Zusätzlich erforderlich.'),('RS1, RS2','2 x 1 kOhm, 1 W, 5 % oder besser','Zusätzlich erforderlich.'),('D1-D4','4 x 1N4148, bedrahtet','Zusätzlich erforderlich.'),('Isolierende Montage','Lötstützpunkte, Schrumpfschlauch, Feinlitze','Bestand nicht belegt.')],[120,205,162])
p('Die kleine Adapterschaltung benötigt keine LoDi-Platine. Sie wird auf isolierten Lötstützpunkten oder einem kleinen Stück Lochraster befestigt. Ein ESU-Decoder ist in dieser Ausführung nicht erforderlich. 60977, 60982, LoDi-511/512 und LoDi-510 bleiben ungenutzt.')
p('Werkzeug: Multimeter, feine Lötstation, Entlötlitze, Schraubendreher, Pinzette, Lupe und isolierende Unterlage. Die CS3 übernimmt Anmeldung und Einrichtung über mfx; ein Windows-PC oder ESU-LokProgrammer ist für diesen Hauptweg nicht nötig.')
note('Für die Startauslegung muss die verwendete CS3-/Netzteilkonfiguration eine maximale Spannung von 24 V am Lichtkreis einhalten. Den Netzteiltyp und die passende CS3-Einstellung prüfen. Ein beliebiger Multimeterwert am Digitalgleis belegt keine Spitzenspannung.')

page(3,'Öffnen und Leitungen zuordnen','Kopf A ist der motorisierte Triebkopf. Markiere ihn dauerhaft innen mit A, den motorlosen Kopf mit B. Die Richtung A voraus heißt in dieser Anleitung vorwärts.')
photo(Path('Arbeitsstand_REV10/bilder/0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg'),'Eigenes Referenzfoto aus REV10: Motor links, lange Originalplatine rechts. Kein verifizierter Lötstellenplan.',125)
photo(Path('Arbeitsstand_REV10/bilder/BAD231CB-B878-4D94-B5EE-CDAB1D69D455_4_5005_c.jpeg'),'Eigenes Referenzfoto: alte Feldwicklung am Motor sichtbar. Die Padfunktionen sind im Bild nicht vollständig erkennbar.',145)
steps(['Zug vom Gleis nehmen. Kupplungsabdeckung vorsichtig abziehen und die passende untere Gehäuseschraube lösen. Gehäuse anheben; bei Widerstand zuerst nach einer weiteren Haltestelle suchen.',
'Alle vorhandenen Leitungen vor dem Ablöten fotografieren. Schleifer, Radmasse, Motorbürsten, Frontlicht und beide Kupplungskontakte durch Verfolgen zuordnen; Etiketten anbringen.',
'Alten Fahrtrichtungsumschalter bzw. alten Decoder elektrisch vollständig vom neuen Motor- und Kopflichtkreis trennen. Neue Decoderausgänge werden nie an dessen Ausgänge angeschlossen.',
'Originalplatine kann als mechanischer Träger bleiben. Nur durchgemessene passive Leiterzüge als Verteiler nutzen. Keine Leiterbahn anhand eines fremden Fotos schneiden. Prüfe Schraubaugen und Schalter in beiden Stellungen gegen die geplanten Netze.'])
note('<b>Ergebnis:</b> Jede neue Leitung hat ein bekanntes Ziel. Vorhandene Wagenlichtleitungen sind separat dokumentiert. Ein noch unklarer Anschluss bleibt isoliert.')

page(4,'Hochleistungsmotor einbauen','Der 60941 ersetzt Feldmagnet, Anker und Motorschild des passenden Trommelkollektormotors. Getriebe und Fahrwerk bleiben bestehen. Die mechanische Passung am eigenen Fahrzeug ist vor dem Festziehen zu prüfen.')
photo(Path('Pruefnachweise/REV9_Berichtsabgleich/Maerklin_60941_Zeichnung.png'),'Märklin 60941/60943, Original-Montagezeichnung [Q2]. Gezeigtes Fahrwerk ist schematisch, kein ICE-Foto.',270)
steps(['Bürstenfedern entlasten und alte Bürsten entnehmen. Motorleitungen ablöten. Beide Motorschildschrauben lösen; Schild, Anker und Feldmagnet entnehmen. Reihenfolge der Teile fotografieren.',
'Lose Verschmutzung aus dem Getriebe entfernen. Räder und Zahnräder von Hand bewegen. Ein klemmendes Getriebe vor dem Motorumbau instand setzen.',
'Permanentmagnet (1), fünfpoligen Anker (2) und passendes Motorschild (3) einsetzen. Ritzel sauber ins Getriebe eingreifen lassen. Schrauben (4) gleichmäßig anziehen; sie dürfen kein Zahnrad berühren.',
'Neue Bürsten (5) einsetzen und Federn auflegen. Drosseln (6) nach Anschlusszeichnung anbringen. Rotor/Getriebe nochmals drehen. Magnetisches Rasten ist normal; hartes Klemmen ist es nicht.'])

page(5,'Motor verdrahten und isolieren','Beide Bürstenanschlüsse müssen elektrisch vom Metallfahrwerk getrennt sein. Das ist vor dem Anschluss des Decoders zu messen.')
diagram('motor')
photo(Path('Arbeitsstand_REV10/quellen_alt/tmp/pdfs/rev5/research/motor_b.png'),'LoDi-Herstellerbeispiel 33701 [Q3]: Pfeile zeigen Entstörkondensatoren zur Masse. Nur als Vergleich verwenden.',150)
steps(['Je eine vorgesehene Motordrossel in jede Motorleitung einfügen: 60972 grün/MV zur ersten Bürste, blau/MR zur zweiten Bürste. Lötstellen isolieren.',
'Kondensatoren von den Bürsten zum Chassis entfernen, sofern vorhanden. Ein Kondensator ausschließlich zwischen beiden Bürsten darf bleiben. Keine Entstörteile auf Verdacht entfernen.',
'Decoder und beide Motorzuleitungen für die Messung abtrennen. Multimeter zunächst mit kurzgeschlossenen Spitzen prüfen. Danach jede Bürste gegen blankes Chassis messen: kein dauerhafter Durchgang. Mehrere Rotorstellungen prüfen.',
'Zwischen den Bürsten ist ein endlicher, rotorabhängiger Wicklungswiderstand zu erwarten. Vor dem ersten Einschalten nochmals prüfen, dass Schrauben und Bürstenfedern das Gehäuse nicht berühren.'])
note('Im Kopf B wird kein Motor und kein Decoder eingebaut. Sein LoDi-514-Kopflicht ist gegenüber Fahrwerk, Schleifer und Wagenbeleuchtung vollständig isoliert.')

page(6,'60972 im Kopf A anschließen','Den mitgelieferten 21MTC-Träger des 60972 isoliert befestigen. Der Decoder bleibt während aller Lötarbeiten abgezogen. Anschlussnamen haben Vorrang vor Farben.')
photo(Path('Arbeitsstand_Originalplatine/maerklin_60972_p6.png'),'Märklin 60972, Träger und Steckrichtung [Q1]. +Ub entspricht hier dem gemeinsamen Decoderplus U+.',265)
table(['60972-Träger','Verbindung'],[('Rot, B/G rechts','Nur Mittelschleifer A; kein B-Zug über die Kupplungen.'),('Braun, 0/G links','Sichere örtliche Rad-/Chassismasse.'),('Grün / Blau, MV / MR','Über je eine Drossel zum 60941; siehe Seite 5.'),('Orange, +Ub / U+','VCC der vorderen LoDi-514 sowie RP1/RP2 im Sender.'),('Grau LV / Gelb LR','Jeweils über eigenen Widerstand zur Front, Seite 7.'),('AUX1 / AUX2','Zum Zweileiter-Adapter auf Seite 8.'),('AUX3/4, GND, +5V, SUSI','Unbenutzt; einzeln isolieren.')],[158,329])
p('Träger so befestigen, dass weder Kupferflächen noch Decoderbauteile die Originalplatine oder Schrauben berühren. Die durch den fehlenden Stift kodierte Steckposition prüfen; niemals um eine Reihe versetzt stecken. Vor dem Gehäuseschluss Kabelschlaufen aus dem Bereich der Zahnräder entfernen.')

page(7,'LoDi-514 vorn: Weiß und Rot','Die Frontmodule besitzen keine Vorwiderstände [Q5]. Ohne LoDi-511/512 kommen deshalb externe Widerstände direkt in die beiden Farbzweige.')
photo(Path('Arbeitsstand_REV10/quellen_alt/tmp/pdfs/rev5/research/lamp.jpg'),'LoDi-Herstellerfoto [Q3]: Anschlussfelder red, VCC und white. Die Lage am eigenen Modul anhand der Beschriftung prüfen.',145)
diagram('front')
steps(['Alte Frontlampen samt Fassungen ausbauen; Lichtleiter sauber lassen. LoDi-514 zuerst ohne Kleber einpassen. Halter darf Gehäuse und Lichtleiter nicht verspannen.',
'VCC mit orange/U+ des 60972 verbinden. Grau/LV über den Widerstand RFw mit 47 kOhm an white, gelb/LR über RFr mit 47 kOhm an red anschließen.',
'Beide Widerstände einzeln nachmessen und isolieren. Bei 5 % Toleranz: 44,65 bis 49,35 kOhm. Keine Verbindung von VCC zur Radmasse herstellen.'])
note('<b>Stromarme Startauslegung, kein LoDi-Nennwert:</b> 47 kOhm / 0,25 W begrenzt bei höchstens 24 V und 5 % Toleranz den Strom selbst ohne LED-Spannungsabzug auf 0,54 mA. Das Licht kann schwach ausfallen. Die Versorgungskonfiguration muss diese Spannungsgrenze einhalten; kleinere Widerstände erst nach belegtem zulässigem LED-Zweigstrom einsetzen. Die zuvor genannten 3,3 kOhm waren dafür nicht ausreichend belegt.')

page(8,'Adapter vorn: zwei Steuerleitungen','Für das hintere Kopflicht werden die verstärkten AUX1/AUX2 benutzt. Die vorderen LEDs bleiben getrennt an LV/LR. Das verhindert, dass ihre LED-Zweige als ungewollte Versorgung des hinteren Kopfes mitwirken.')
diagram('sender',245)
steps(['RP1 (4,7 kOhm / 0,5 W) zwischen U+ orange und AUX1 braun/rot löten. RP2 gleichartig zwischen U+ und AUX2 braun/grün löten. Das sind absichtliche Widerstandsverbindungen, keine Drahtbrücken.',
'Von AUX1 über RS1 (1 kOhm / 1 W) zum Kupplungskontakt K1 gehen. Von AUX2 über RS2 zum Kontakt K2 gehen. Die Reihenfolge ist wichtig: RP am AUX-Knoten, RS zwischen diesem Knoten und Kupplung.',
'Alle Bauteile zugentlastet und isoliert befestigen. Widerstände nicht in engen Kontakt zu Gehäusekunststoff oder Decoder legen. Im normalen Betrieb entstehen an einem RP bei 24 V höchstens etwa 0,13 W.',
'An K1/K2 darf kein bisheriger RT-, GE-, Mittelschleifer- oder Innenlichtanschluss mehr hängen. Beide Leitungen bis zur nächsten Kupplung durchmessen.'])
note('<b>Funktion:</b> Ein eingeschalteter AUX zieht seinen Zweig nach Decoder-Minus. Der Widerstand RP hält den ausgeschalteten anderen Zweig auf Plus. Dadurch liegt zwischen K1 und K2 eine richtungsabhängige Spannung. Bei beiden AUX AUS verschwindet die Spannungsdifferenz und das hintere Licht erlischt.')

page(9,'Adapter hinten: Dioden und LoDi-514','Kopf B braucht für sein Kopflicht weder Radkontakt noch Schleifer. Die Energie kommt zusammen mit der Farbauswahl über K1/K2. VCC hier ist der lokale Punkt P des Adapters, nicht Fahrzeugmasse.')
diagram('receiver',320)
table(['Bauteil / Punkt','Verbindung'],[('D1','Anode ohne Ring an K1; Kathode mit Ring an P.'),('D2','Anode ohne Ring an K2; Kathode mit Ring ebenfalls an P.'),('P','An VCC und Ringseiten D1-D4; isoliert von Gleis/Chassis.'),('RR, 47 kOhm','Zwischen LoDi red und K1.'),('RW, 47 kOhm','Zwischen LoDi white und K2.'),('D3, Sperrspannungsschutz','Anode an red-Pad; Ringseite direkt an VCC/P.'),('D4, Sperrspannungsschutz','Anode an white-Pad; Ringseite direkt an VCC/P.')],[179,308])
p('Alle vier Dioden-Ringseiten gehören an P. D3/D4 begrenzen die negative LED-Spannung. Lose Diode vor Einbau prüfen: roter Messkontakt an Anode, schwarzer an Ringseite ergibt Durchlass; umgekehrt sperrt sie. Alten Lichtumschalter und Schleiferanschluss vollständig vom neuen Lichtkreis trennen.',True)


page(10,'Kupplungen als Lichtverbindung','Die beiden Kupplungspole erhalten neue Funktionen: K1 und K2. Alte Farbbezeichnungen RT/GE dürfen nicht als elektrische Belegung übernommen werden. In den Wagen wird nur kontaktgleich durchgeleitet.')
diagram('coupling')
steps(['Alle Fahrzeugübergänge zählen und die mechanisch passenden Kupplungen trocken einsetzen. Männliche/weibliche Gegenseite, Halterhöhe und seitliche Beweglichkeit prüfen. Unpassende Teile nicht unter Spannung mit Gewalt einpassen.',
'Alle bisherigen Verbraucher und Schleiferverbindungen von den beiden Durchgangsleitungen trennen. Die örtliche Wagenbeleuchtung bleibt ein eigener Stromkreis, Seite 11. Keine Kupplung darf die neuen Lichtsignale mit Gleisspannung verbinden.',
'Am noch von Adaptern und LEDs getrennten Kabelbaum K1 vom ersten bis zum letzten Fahrzeug niederohmig messen; anschließend K2. Jeden Wagen einzeln ergänzen und dieselbe Zuordnung erhalten.',
'K1 gegen K2, gegen alle Radkontakte und gegen jeden Mittelschleifer messen: kein Durchgang. Kupplungen und Drehgestelle dabei bewegen. Die Messung gilt für den unbestückten Kabelbaum, nicht für angeschlossene Halbleiter.',
'Erst nach bestandenem Test Adapter A und B verbinden. Wagenübergänge bei ausgeschalteter Gleisspannung kuppeln. Kein zusätzliches Kabel außen neben den Kupplungen führen.'])
note('K1 und K2 sind vollständig für das Kopflicht belegt. Ein paralleler Motor-Strombus beider Schleifer oder eine neue Wagenlichtversorgung über dieselben Pole ist in dieser Schaltung nicht enthalten. Das erklärt den Unterschied zur früheren RT/GE-Planung.')

page(11,'Mittelwagen versorgen ihr Licht selbst','Du möchtest die vorhandene Wagenbeleuchtung über die eigenen Stromabnehmer weiterbetreiben. Dafür braucht jeder Wagen eine vollständige Versorgung. Rad-/Achsschleifer allein liefern bei Märklin nur den Außenschienenanschluss.')
table(['Versorgung im Wagen','Erforderlicher Anschluss'],[('Mittelschleifer unter dem Wagen','Gleismitte B zum vorhandenen Lichtkreis.'),('Rad-/Achskontakte','Außenschienen 0 zum vorhandenen Lichtkreis.'),('Kupplung K1/K2','Nur Kopflicht durchleiten, keine Verbindung zum Wagenlicht.'),('Vorhandene Lampen/Platine','Für dauernde Digitalspannung geeignet; Polung und Nennspannung prüfen.')],[188,299])
steps(['Unter jeden beleuchteten Wagen schauen: Ist ein eigener Mittelschleifer vorhanden? Danach die Rad-/Achskontakte prüfen. Beides fotografieren und mit dem Multimeter bis zum Lichtkreis verfolgen.',
'Wenn der Lichtkreis bereits unabhängig aus diesen beiden Anschlüssen gespeist wird, bleibt er so bestehen. Eventuelle zusätzliche Verbindungen zur Kupplung trennen, damit die zwei neuen Lichtleitungen frei sind.',
'Wenn der Mittelschleifer fehlt, ist die lokale Versorgung noch nicht vollständig. Einen zum konkreten Wagen passenden Schleifer mit Halter nachrüsten oder das Versorgungskonzept neu festlegen. Keine Artikelnummer ohne Zuordnung zum Wagen bestellen.',
'Nennspannung der bestehenden Lampen bzw. Platine feststellen. Einen Wagen kurz allein auf Digitalgleis testen, ausschalten und die Lampensitze auf ungewöhnliche Erwärmung prüfen. Wagen danach einzeln ergänzen.'])
note('<b>Noch nicht belegt:</b> Aus deiner Angabe zu den Achsschleifern geht die Existenz eigener Mittelschleifer nicht sicher hervor. Die Zweileiter-Kopflichtschaltung ist deshalb an diese Vorprüfung gebunden. Fehlen sie, ist die vollständige Materialliste noch offen. Die Anleitung behauptet nicht, dass Radkontakte allein Licht erzeugen können.')
p('Vorteil der örtlichen Versorgung: unabhängige Stromkreise und freie Kupplungspole. Nachteile: mögliche Kontaktflackerer, Schleiferreibung und Wagenlicht ohne neue gemeinsame F-Tasten-Schaltung. Dafür bleiben die vorhandenen Leuchtmittel und ihre Innenverkabelung weitgehend erhalten.',True)

page(12,'60972 anmelden und einrichten','Nur ein Decoder wird eingebaut. Deshalb genügt die normale mfx-Anmeldung an deiner CS3. Weder eine gemeinsame DCC-Adresse noch ein ESU-Slave oder eine Traktion ist erforderlich.')
steps(['Kopf A nach bestandenem Motor-/Isolationscheck allein auf einen vollständig isolierten Prüfabschnitt stellen. Hinteren Adapter zunächst abgekoppelt lassen. CS3 einschalten und mfx-Anmeldung abwarten.',
'Die neue Lok eindeutig ICE 2976 nennen. Firmware-/Decoderdaten und Ausgangseinstellungen sichern. In der CS3-Lokbearbeitung die Konfiguration des angemeldeten Decoders vollständig lesen.',
'Den Motorbereich auf HLA/C90 einstellen. Für den 60972 nennt die DCC-Tabelle dazu Motortyp 3; unter mfx die entsprechende Motorprofil-Auswahl benutzen. Einen fremden CV-Satz nicht blind laden.',
'Anfahrzeit zunächst etwa 7 Sekunden, Bremszeit etwa 5 Sekunden einstellen. Höchstgeschwindigkeit zunächst begrenzen und erst nach einem sauberen Fahrtest erhöhen. Feinabgleich des Motors ist individuell.',
'mfx aktiviert lassen. Analogbetrieb für diese digitale Ausführung ausschalten. Die beiden Lichtausgänge und AUX1/AUX2 nach der nächsten Seite einrichten.'])
table(['Parameter','Ziel'],[('Decoderanzahl','1: Märklin 60972.'),('Aktives Fahrprotokoll','mfx; automatische Anmeldung.'),('Traktion / Slave','Keine.'),('Motor','60941, HLA/C90-Startprofil.'),('Frontausgänge','LV und LR, richtungsabhängig mit F0.'),('Hintere Lichtsteuerung','AUX1 und AUX2, ebenfalls F0-richtungsabhängig.'),('AUX3/4','Frei, unbeschaltet.'),('Lichteffekt / Dimmen AUX1/2','Normales Dauerlicht, 100 %, kein Blinken, kein Timer.')],[184,303])
note('Die Widerstände begrenzen den LED-Strom. Dimmen ersetzt keine Vorwiderstände. AUX1/AUX2 für die Zweileiterschaltung nicht als Kupplungsimpuls, Blinklicht oder unabhängig schaltbare Zusatzfunktion betreiben.')

page(13,'F0 und Fahrtrichtung zuordnen','Alle vier Ausgänge reagieren auf dieselbe Funktion F0. Die Auswahl hängt von der Richtung ab, nicht von der Geschwindigkeit. Die Bedingung muss deshalb jeweils im Stand und während der Fahrt gelten.')
table(['F0','Zugrichtung','Ausgänge EIN','Resultat'],[('AUS','beliebig','keine','Beide Köpfe dunkel.'),('EIN','A voraus / vorwärts','LV und AUX1','A weiß, B rot.'),('EIN','B voraus / rückwärts','LR und AUX2','A rot, B weiß.')],[48,143,117,179])
steps(['In der Funktionszuordnung von F0 die vorhandenen LV/LR-Einträge kontrollieren. LV darf nur bei Vorwärts aktiv sein; LR nur bei Rückwärts. Beide müssen auch im Stand schalten.',
'Zu F0 einen Ausgang AUX1 mit Bedingung Vorwärts ergänzen. AUX2 mit Bedingung Rückwärts ergänzen. Wenn die Oberfläche getrennte Bedingungen für Stand/Fahrt anbietet, beide Zustände aktivieren.',
'Werkseitige oder frühere unabhängige Zuweisungen von F1 zu AUX1 und F2 zu AUX2 entfernen. Sonst kann eine zusätzliche Taste das hintere Licht ungewollt übersteuern.',
'Bei AUX1/AUX2 den normalen verstärkten Lichtausgang mit voller Helligkeit, ohne Timer und ohne Sonderwirkung einstellen. Die sichtbaren Menünamen können mit Firmware und Decoderprojekt variieren; maßgeblich ist die obige Zustandstabelle.',
'Bei stehendem Kopf A zunächst am Sender prüfen: F0 AUS ergibt zwischen K1/K2 nahezu 0 V. F0 EIN vorwärts macht K2 gegenüber K1 positiv; rückwärts macht K1 gegenüber K2 positiv.'])
h('Messung ohne LED-Last')
p('Multimeter auf Gleichspannung stellen, rote Spitze K2, schwarze K1. Vorwärts wird ein positiver, rückwärts ein negativer Wert erwartet. AUS liegt nahe 0 V. Die Messspitzen vorher stromlos anklemmen. Zeigt AUS eine dauerhafte Spannung, zuerst Mapping und Verdrahtung korrigieren; Kopf B noch nicht anschließen.')
note('AUX1/AUX2 sind hier eigene Ausgänge für den hinteren Adapter. Sie werden nicht mit LV/LR zusammengelötet. Das hintere Rot/Weiß wird durch K1/K2 und den passiven Adapter bestimmt, nicht durch einen zweiten Decoder.')

page(14,'In kleinen Stufen einschalten','Die folgenden Tests sind Bestandteil des Einbaus. Eine Simulation belegt die Logik der Schaltung, kann aber falsche Lötstellen, unpassende Bauteile und reale Decoder-Effekte nicht ausschließen.')
diagram('test')
steps(['Lose C-Gleise vollständig von der Anlage trennen. CS3 ausschalten und nur den Programmierausgang anschließen: B an Mittelleiter, 0 an Außenschienen. Keine Verbindung zu Booster oder zweiter Versorgung.',
'Kopf A allein prüfen: mfx, vorderes Licht und langsame Motorbewegung. Danach den Sender ohne hinteren Adapter gemäß Seite 13 messen.',
'Strom aus. Hinteren Adapter zuerst außerhalb des Fahrzeugs über die vorbereiteten K1/K2-Leitungen anschließen. F0 AUS sowie beide Richtungen testen. Vorwärts nur red, rückwärts nur white.',
'LED-Ströme durch Gleichspannungsmessung über RR und RW prüfen: I = U/R. Bei 47 kOhm entsprechen 10 V etwa 0,21 mA. Der jeweils ausgeschaltete Farbzweig darf nicht sichtbar leuchten. Bei falschem Verhalten ausschalten und Diodenrichtung prüfen.',
'Adapter isoliert in Kopf B einbauen. Danach jeden Wagenübergang einzeln ergänzen und alle drei Lichtzustände wiederholen. Wagenlicht bleibt elektrisch separat.',
'Für Fahrtests ein ausreichend langes freies Gleis/Oval am Hauptgleisausgang benutzen. Vor dem Umstecken ausschalten und Programmiergleisanschluss vollständig lösen.'])
note('Eine automatische Motor-Einmessfahrt ist erst auf einem freien geeigneten Oval zulässig; Märklin empfiehlt Radien über 430 mm. Sie kann stark beschleunigen. Für die erste kurze Prüfung ist sie nicht nötig. Kein dauerhaftes Fahren auf dem kurzen Tisch-Prüfabschnitt.')

page(15,'Abnahme, Vorteile und Grenzen','Nach dem Gehäuseschluss sämtliche Lichtzustände und die langsame Fahrt erneut prüfen. Nicht eingeschaltete Farbzweige müssen dunkel bleiben; die Farben beider Köpfe müssen zur tatsächlichen Fahrtrichtung passen.')
table(['Abnahme','Soll / Eintrag'],[('F0 AUS','Beide Köpfe dunkel: __________'),('F0 EIN / A voraus','A weiß, B rot: __________'),('F0 EIN / B voraus','A rot, B weiß: __________'),('STOP, aus/ein, Richtungswechsel','Licht reagiert wieder korrekt: __________'),('Kurven / Gegenkurven langsam','Kein Kontaktabbruch/Kurzschluss: __________'),('5-10 Minuten Probefahrt','Motor, Widerstände und Lampensitze unauffällig: __________'),('Wagenlicht unabhängig','Mittelschleifer und Radkontakte vorhanden/geprüft: __________')],[239,248])
table(['Vorteil','Nachteil / praktische Grenze'],[('Ein mfx-Eintrag ohne Traktion','Nur der vordere Schleifer speist den Motor.'),('Ein Decoder statt komplexer Synchronisation','Kleine selbst zu lötende Adapterschaltung nötig.'),('Zwei vorhandene Kupplungspole genügen','Beide Pole sind vollständig durch Kopflicht belegt.'),('Keine zusätzliche Leitung zwischen Wagen','Mittelwagen brauchen ihre eigene komplette Lichtversorgung.'),('Hochleistungsmotor und automatischer Lichtwechsel','Motorabgleich und tatsächliche Probefahrt bleiben nötig.'),('Keine LoDi-Motorplatinen, kein Sound','Kein zentral geschaltetes neues Wagenlicht in dieser Stufe.')],[239,248])
p('Bei zu schwachem Licht: zuerst Gehäuse/Lichtleiter prüfen. Die 47-kOhm-Widerstände sind eine stromarme Startauslegung; hellere Einstellung braucht den zulässigen LED-Zweigstrom. Bei falscher hinterer Farbe: K1/K2-Zuordnung und Mapping prüfen. Bei Flackern hinten: Kupplungskontakte prüfen. Bei Flackern im Wagen: seine eigenen Stromabnehmer prüfen.',True)
note('<b>Bewertung:</b> Diese Ausführung erfüllt mfx, keine Traktion und möglichst wenig Elektronik am besten, sofern die Wagen lokal vollständig versorgt sind. Eine optimale gemeinsame Motor-Stromaufnahme aus beiden Schleifern ist damit nicht umgesetzt. Das ist der konkrete Preis dafür, beide vorhandenen Kupplungspole für das Kopflicht zu nutzen.')

page(16,'Nachweise und klare Ausführungsgrenzen','Die Schaltung wurde als eigene Auslegung erstellt. Motor-/Decoderanschlüsse und LED-Polarität stützen sich auf die Herstellerunterlagen. Referenzbilder sind als eigene Fotos oder Herstellervergleich gekennzeichnet.')
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

def footer(c,doc):
    c.setStrokeColor(TEAL);c.line(54,42,541,42)
    c.setFont('Helvetica',8);c.setFillColor(NAVY);c.drawString(54,29,'ICE 2976 | REV16 | ein Decoder / mfx | 16.09.2026');c.drawRightString(541,29,str(doc.page))
doc=SimpleDocTemplate(str(OUT),pagesize=(595.28,841.89),leftMargin=54,rightMargin=54.28,topMargin=43,bottomMargin=55,title='ICE 2976 REV16 - HLA, LoDi-514 und leitende Kupplungen',author='Werkstattdokumentation für Martin Waelter')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
r=PdfReader(str(OUT)); report={'output':str(OUT),'pages':len(r.pages),'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'physical_test':False,'scope':'Nutzer bestätigt: mfx, keine Traktion, ein 60972, HLA 60941, LoDi-514, nur leitende Kupplungen; lokale Wagenversorgung zu prüfen'}
(ROOT/'Arbeitsstand_REV16/build_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
(ROOT/'Arbeitsstand_REV16/Anleitung_Inhalt.md').write_text('\n\n'.join(content))
print(json.dumps(report,ensure_ascii=False))
assert len(r.pages)==16, f'Unexpected pagination: {len(r.pages)}'
