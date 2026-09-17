from pathlib import Path
from html import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, Flowable, KeepTogether
from reportlab.lib.pagesizes import A4
from PIL import Image as PILImage

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output/pdf/ICE_2976_Umbauanleitung_REV5.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
FONT = Path('/System/Library/Fonts/Supplemental')
for name, f in [('A','Arial.ttf'),('AB','Arial Bold.ttf'),('AI','Arial Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT/f)))
pdfmetrics.registerFontFamily('A', normal='A', bold='AB', italic='AI', boldItalic='AB')
INK=colors.HexColor('#20252A'); MUTED=colors.HexColor('#53606A'); RED=colors.HexColor('#9D2024'); GREEN=colors.HexColor('#236043')
W=A4[0]-84
ST={
 'body':ParagraphStyle('body',fontName='A',fontSize=10.1,leading=14.1,textColor=INK,spaceAfter=6),
 'small':ParagraphStyle('small',fontName='A',fontSize=8.3,leading=11.2,textColor=MUTED,spaceAfter=4),
 'h1':ParagraphStyle('h1',fontName='AB',fontSize=20,leading=24,textColor=INK,spaceAfter=12,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='AB',fontSize=12.1,leading=15.3,textColor=INK,spaceBefore=7,spaceAfter=6,keepWithNext=True),
 'cell':ParagraphStyle('cell',fontName='A',fontSize=9,leading=12,textColor=INK),
 'head':ParagraphStyle('head',fontName='AB',fontSize=9,leading=12,textColor=INK),
 'warn':ParagraphStyle('warn',fontName='A',fontSize=9.5,leading=13.4,textColor=RED),
 'step':ParagraphStyle('step',fontName='A',fontSize=10.1,leading=14.1,textColor=INK,leftIndent=20,firstLineIndent=-20,spaceAfter=7),
}
SOURCES={
1:('Märklin','Nachrüstdecoder 60975/60976/60977','Originalanleitung; S. 3-7: Grenzen, Einbau, Farben, Einmessfahrt','https://static.maerklin.de/damcontent/36/f5/36f55304fb028471e05de4762e04fada1663856051.pdf'),
2:('Märklin','Nachrüstsatz-Hochleistungsmotor 60941/60943','Stand 12/2022; Montagezeichnung S. 2','https://static.maerklin.de/damcontent/e3/bb/e3bb202fe80385cc96835d783af5e1821670919973.pdf'),
3:('LoDi','ICE 1 mit 2 Triebköpfen / LoDi-Motor WiB ICE-M(-S)','Einbau am Beispiel 33701; Widerstände, Anschlüsse, Jumper, Schleifer','https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/'),
4:('LoDi','LoDi-(Motor) WiB ICE-M','Wagenplatinen, Varianten der Anschlussbelegung, Kupplungslitzen','https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-wib-ice-m/'),
5:('LoDi','LoDi-WiB ICE-M / Front-Einsätze','Produktbeschreibung Frontmodule: ohne Vorwiderstände','https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/'),
6:('ESU','LokPilot 5 Familie','Einbau- und Betriebsanleitung; 21MTC/MKL, Motorisolation und Lichtmapping','https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e'),
7:('ESU','Master/Slave Adress-Synchronisation','Offizielles Konfigurationsbeispiel mit ESU-Decodern','https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/'),
8:('MTB-Ontour','Eigener ICE-Umbau: mSD3 mit LokPilot V5 M4 als Slave','Stummiforum, Beitrag 4, 26.02.2023; Einzelfallerfahrung, keine Herstellerfreigabe','https://www.stummiforum.de/t212683f5-Umbau-ICE-Maerklin-auf-mSD-DCC.html'),
9:('Märklin','Spannungspufferelektronik 60974','Originalanleitung; Firmware, Anschluss an Trägerplatine, Pufferverhalten','https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf'),
10:('RailCommunity','RCN-121: Decoderschnittstelle 21MTC','08.12.2024; Tabelle 1, mechanische Varianten und SUSI-Nutzung','https://normen.railcommunity.de/RCN-121.pdf'),
11:('RailCommunity','RCN-600: SUSI-Bus','27.07.2026; classicSUSI und Decoder-Schnittstelle','https://normen.railcommunity.de/RCN-600.pdf'),
12:('Märklin','Central Station 3, Artikel 60216/60226','Kurzanleitung ab Software 2.5; S. 17 sowie 22-23: Rückmeldung/Ereignisse','https://static.maerklin.de/damcontent/c1/ce/c1ce554ad6ad195c04e32ba1b4dd64511764068661.pdf'),
13:('Märklin','Ersatzteilblatt 33701/37701/39711','07/2002; verwandte Baureihe, keine vollständige 2976-Stückliste','https://www.marklinfan.com/esplosipdf/33701_explo.pdf'),
14:('Märklin','Katalog 1993/94','Gedruckte S. 25: HOBBY 2976; Abgrenzung des Ergänzungswagens 4374','https://www.nicospilt.com/marklin-catalogi/Marklin_1993_1994_Yearbook_EN_IT.pdf'),
15:('ESU','LokPilot 5','Artikel 59649: 21MTC MKL mit M4','https://www.esu.eu/produkte/lokpilot/lokpilot-5/'),
16:('Märklin','Kontaktgleis-Satz 24995','Belegtmeldung über Radsätze; Mittelleiter und Meldeabschnitt unterscheiden','https://www.marklin.com/products/details/article/24995'),
}
story=[]; sections=[]
def p(t,style='body'):
    for old,new in [('auf S. 15','in Abschnitt 15'),('auf S. 11','in Abschnitt 11'),('auf S. 16','in Abschnitt 16')]:
        t=t.replace(old,new)
    return Paragraph(t,ST[style])
def add(t,style='body'): story.append(p(t,style))
def h(t): add(t,'h2')
def step(n,title,t): story.append(p(f'<b>{n}. {title}</b> {t}','step'))
def warn(title,t):
    tab=Table([[p(title,'head')],[p(t,'warn')]],colWidths=[W-18])
    tab.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.9,RED),('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#FFF5F4')),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    story.extend([KeepTogether(tab),Spacer(1,8)])
def table(headers,rows,widths):
    data=[[p(escape(x),'head') for x in headers]]+[[p(x,'cell') for x in row] for row in rows]
    t=Table(data,colWidths=[W*x/sum(widths) for x in widths],repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E9ECEF')),('LINEBELOW',(0,0),(-1,0),0.7,MUTED),('LINEBELOW',(0,1),(-1,-1),0.35,colors.HexColor('#D1D6DA')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    story.extend([t,Spacer(1,7)])
def page(title):
    if story: story.append(PageBreak())
    sections.append(title); add(title,'h1')
def refs(*nums):
    story.append(Spacer(1,4))
    for n in nums:
        au,ti,meta,url=SOURCES[n]
        add(f'{n}. {au}: <a href="{escape(url,quote=True)}" color="#354B65">{escape(ti)}</a>. {escape(meta)}.','small')
def photo(path,width,maxh):
    im=PILImage.open(path); w,h0=im.size; s=min(width/w,maxh/h0)
    return Image(path,width=w*s,height=h0*s)

class MarkedPhoto(Flowable):
    """Unchanged source bitmap with precisely positioned PDF-vector callouts."""
    def __init__(self,path,width,marks,maxh=1000):
        Flowable.__init__(self)
        self.path=str(path); self.marks=marks
        with PILImage.open(path) as im: iw,ih=im.size
        scale=min(width/iw,maxh/ih)
        self.width=iw*scale;self.height=ih*scale
    def draw(self):
        c=self.canv;w=self.width;hh=self.height
        c.drawImage(self.path,0,0,width=w,height=hh)
        for number,px,py,lx,ly in self.marks:
            x,y=px*w,(1-py)*hh; a,b=lx*w,(1-ly)*hh
            c.setStrokeColor(colors.white);c.setLineWidth(3.7);c.line(a,b,x,y)
            c.setStrokeColor(RED);c.setLineWidth(1.1);c.line(a,b,x,y)
            c.setFillColor(colors.white);c.circle(x,y,3.2,stroke=1,fill=1)
            c.circle(a,b,8,stroke=1,fill=1)
            c.setFillColor(RED);c.setFont('AB',9);c.drawCentredString(a,b-3,str(number))

RESEARCH=ROOT/'tmp/pdfs/rev5/research'
def photocredit(title,url):
    add(f'Foto: LoDi / Lokstoredigital, Einbauserie 33701. {title} '
        f'<a href="{escape(url,quote=True)}" color="#354B65">Originalfoto</a>. '
        'Nummern und Linien sind ergänzte Prüfmarkierungen, kein Nachweis eines Defekts.','small')

class Sketch(Flowable):
    def __init__(self,kind,height=175): Flowable.__init__(self); self.width=W; self.height=height+8; self.plotheight=height; self.kind=kind
    def draw(self):
        c=self.canv
        c.translate(0,8)
        def txt(x,y,s,color=INK,size=9): c.setFillColor(color);c.setFont('A',size);c.drawString(x,y,s)
        def line(x1,y1,x2,y2,color=INK,dash=False):
            c.setStrokeColor(color);c.setLineWidth(1.3);c.setDash(3,2) if dash else c.setDash();c.line(x1,y1,x2,y2);c.setDash()
        def box(x,y,w,h0,s,color=INK):
            c.setStrokeColor(color);c.setFillColor(colors.white);c.rect(x,y,w,h0,stroke=1,fill=1)
            for i,z in enumerate(s.split('|')): txt(x+7,y+h0-16-i*12,z,color,8.8)
        def cross(x,y): line(x-5,y-5,x+5,y+5,RED);line(x-5,y+5,x+5,y-5,RED)
        c.setStrokeColor(colors.HexColor('#CED3D8')); c.rect(0,0,W,self.plotheight,stroke=1,fill=0)
        if self.kind=='grounds':
            txt(12,151,'SOLL: getrennte elektrische Netze',GREEN,10)
            box(15,45,110, seventy:=70,'Gleis B / Schleifer|Gleis 0 / Räder');box(165,45,140,70,'Decoder|Gleichrichter und|Lichtschalter');box(345,45,150,70,'LED mit Widerstand|zwischen U+ und|Lichtausgang')
            line(125,91,165,91);line(125,65,165,65);line(305,93,345,93);line(305,61,345,61)
            txt(309,99,'U+',INK,8);txt(308,67,'OUT',INK,8)
            txt(15,17,'FEHLER: U+ oder Decoder-GND mit dem Chassis / Gleis 0 verbinden.',RED,9)
        elif self.kind=='motor':
            for x,title,col,bad in [(12,'SOLL',GREEN,False),(268,'FEHLER',RED,True)]:
                txt(x,156,title,col,10);box(x+15,64,178, sixty:=60,'M1     Motor     M2|Kondensator nur M1-M2')
                line(x+35,64,x+35,39,MUTED,True);line(x+165,64,x+165,39,MUTED,True)
                line(x+8,29,x+213,29,MUTED);txt(x+14,12,'Chassis / Radmasse',MUTED,8)
                if bad: line(x+35,70,x+35,29,RED);cross(x+35,48);txt(x+5,138,'M1 am Gehäuse: Ausgang gefährdet',RED,8)
                else: txt(x+4,138,'Beide Motoranschlüsse isoliert',GREEN,8);txt(x+54, forty:=42,'OL messen',GREEN,9)
        elif self.kind=='caps':
            for x,label,col,bad in [(12,'SOLL: Quer-Kondensator',GREEN,False),(268,'FEHLER: Verbindung zur Masse',RED,True)]:
                txt(x,139,label,col,9);box(x+12,64,200, forty:=45,'')
                txt(x+28,91,'M1',INK,9);txt(x+157,91,'M2',INK,9)
                line(x+35,65,x+35,49);line(x+165,65,x+165,49);line(x+35,49,x+93,49);line(x+106,49,x+165,49)
                line(x+95,40,x+95,58);line(x+104,40,x+104,58)
                line(x+10,20,x+212,20,MUTED)
                if bad:
                    line(x+35,80,x+35,48,RED);line(x+27,47,x+43,47,RED)
                    line(x+27,39,x+43,39,RED);line(x+35,38,x+35,20,RED)
                    txt(x+53,31,'Masse-Kondensator',RED,8)
                txt(x+63,7,'Chassis',MUTED,8)
        elif self.kind=='led':
            txt(12,157,'SOLL: eigener Widerstand je Farbe',GREEN,10)
            box(12,61,80, sixty:=65,'ESU|U+');box(402,61,96,65,'ESU|Lichtausgänge')
            for y,led in [(109,'Weiß'),( seventy:=76,'Rot')]:
                line(92,y,155,y);box(155,y-10,85,20,f'LED {led}');line(240,y,271,y);box(271,y-10,71,20,'R separat');line(342,y,402,y)
            txt(12,37,'FEHLER: LED direkt ohne Widerstand oder Plus am Chassis.',RED,9)
            txt(12,18,'Dimmung allein begrenzt den Spitzenstrom nicht.',RED,9)
        elif self.kind=='bus':
            txt(12,177,'SOLL: gemeinsamer Rohstrom, getrennte Decoderausgänge',GREEN,10)
            box(12,48,134,85,'Motortriebkopf|60977 + LoDi 511|Schleifer A + Radmasse|Innenlicht schalten');box(191,48,132,85,'Mittelwagen|LoDi ICE-M|RT und GE durchgängig');box(368,48,132,85,'Motorloser Kopf|59649 + Front-LED|Schleifer B + Radmasse|kein AUX am GE-Bus')
            line(146,113,191,113);line(323,113,368,113);txt(151,119,'RT',INK,8);txt(328,119,'RT',INK,8)
            line(146,74,191,74);line(323,74,347,74);txt(150,80,'GE',INK,8);txt(330,80,'GE',INK,8);cross(354,74)
            txt(12, twenty:=21,'FEHLER: beide Decoder-U+ / AUX verbinden oder RT mit GE vertauschen.',RED,9)
        elif self.kind=='screw':
            for x,title,col,bad in [(12,'SOLL: nur vorgesehene Metallkontakte',GREEN,False),(268,'FEHLER: Schraube berührt Signalpad',RED,True)]:
                txt(x,142,title,col,8.7)
                c.setFillColor(colors.HexColor('#E2E6E9'));c.setStrokeColor(MUTED);c.rect(x+10,82,202,13,fill=1,stroke=1)
                txt(x+102,104,'Platinenträger (grau)',INK,8)
                c.setFillColor(colors.white);c.setStrokeColor(MUTED);c.rect(x+31,77,18,23,fill=1,stroke=1)
                line(x+40,127,x+40,31,INK);line(x+25,121,x+55,121,INK)
                line(x+10,31,x+212,31,MUTED);txt(x+110,15,'Chassis',MUTED,8)
                line(x+(40 if bad else 64),96,x+155,96,RED if bad else GREEN)
                txt(x+102, seventy:=70,'Signal-Kupferbahn',col,8)
                if bad:cross(x+40,96);txt(x+53,48,'Kontakt zur Schraube',RED,8)
                else:txt(x+67,48,'Freiraum zum Signal',GREEN,8)
        elif self.kind=='ammeter':
            txt(12,143,'SOLL: Strommessung in Reihe',GREEN,10);box(15,55,85,50,'Quelle');box(129,55,65,50,'A-Meter');box(225,55,85,50,'Last')
            line(100,81,129,81);line(194,81,225,81);line(55,55,55,28);line(55,28,270,28);line(270,28,270,55)
            txt(335,143,'FEHLER',RED,10);box(345,54,144,60,'A-Meter direkt|zwischen Gleis B/0');cross(415,28);txt(336,13,'Kurzschluss!',RED,10)
        elif self.kind=='brake':
            txt(12,148,'SOLL: Meldung -> Fahrbefehl; Gleis bleibt digital',GREEN,10)
            for x,w,tx in [(12,110,'Kontakt meldet|Zug erreicht Zone'),(182,140,'CS3 ordnet ICE zu|Signal / Fahrweg prüfen'),(383,115,'60977 bremst|Sound / Licht bleiben')]:box(x,64,w,53,tx)
            line(122,90,182,90);line(322,90,383,90)
            txt(12,36,'FEHLER: rotes Signal anzeigen, aber keinen Haltbefehl an den ICE senden.',RED,9)
            txt(12,16,'Eine Belegtmeldung enthält keine automatische mfx-Lokidentität.',MUTED,9)

page('ICE 2976: Umbauanleitung REV5')
add('Diese Anleitung führt durch den festgelegten Umbau auf Märklin-mfx-Sound, richtungsabhängige LoDi-Front-LEDs, LoDi-Innenbeleuchtung und gemeinsame Schleiferaufnahme. Der hintere ESU 59649 wird als mitfolgender Decoder eingerichtet. Der reguläre Signalhalt erfolgt später durch Fahrbefehle der CS3 bei weiterhin digital versorgtem Gleis.')
warn('Vor dem ersten Handgriff','Ein Foto beweist keinen elektrisch sicheren Zustand. Alle Isolationsprüfungen sind am eigenen Fahrzeug auszuführen. Keine Verbindung herstellen, deren Funktion und Gegenstelle nicht eindeutig bestimmt sind. Ein Prüfhalt betrifft den genannten Schritt; sichere vorbereitende Arbeiten können weitergehen.')
h('Arbeitsfolge')
table(['Phase','Was du ausführst'],[
('1','Bauteile und Fotos zuordnen; Arbeitsplatz und Messgerät vorbereiten.'),('2','Motortriebkopf öffnen, alte Elektrik dokumentieren und abtrennen; 60941 mechanisch montieren.'),('3','Motor und Befestigung auf versteckte Massekontakte prüfen; LoDi-Motorplatine montieren und verdrahten.'),('4','Front-LEDs und motorlosen Kopf aufbauen; Widerstände und Schnittstellen verifizieren.'),('5','Mittelwagen und Kupplungen einzeln prüfen, anschließend den gemeinsamen Bus aufbauen.'),('6','Decoder getrennt einrichten; zuerst ohne Puffer schrittweise einschalten und prüfen.'),('7','Den vorbereiteten 60974-Anschluss erst nach eigener Freigabe ergänzen; CS3-Bremsabläufe später auf der Anlage abnehmen.')],[1,5])
h('Wie Warnungen zu lesen sind')
add('<b>STOPP</b> bedeutet: am beschriebenen Teil weder weiterlöten noch Spannung einschalten. <b>SOLL</b> beschreibt den geprüften Zielzustand. <b>FEHLER</b> ist ein konkretes Schadensbeispiel. Die Schaltbilder sind funktionale Prüfzeichnungen, keine maßstäblichen Lötpunktpläne.')
add('Noch einzeln freizugeben sind die genaue Revision der roten Motorplatine samt Rückseite, die hintere LED-Strombegrenzung, die Trägerplatine des ESU sowie der 60974-Anschluss. Die sechs Wunschfunktionen sind vorgesehen; am konkreten Zug ist noch keine Abnahme dokumentiert. Ein eigener Brems-Testabschnitt wird für die ersten Arbeiten nicht vorausgesetzt.','small')

page('1. Bauteile und Werkzeuge bereitlegen')
table(['Menge im Zug','Artikel / Bezeichnung','Bestand und Arbeit'],[
('1','Märklin 60941, HLA-Motorumbausatz','Vorhanden; vollständigen Satz kontrollieren.'),('1','Märklin 60977, mSD3 mit 21MTC','Vorhanden; Decoder und Zubehör getrennt aufbewahren.'),('1','Lautsprecher aus 60977','Vorhanden, sofern Set vollständig; einen passenden auswählen.'),('1','LoDi 511, Motor WiB ICE-M','Vorhanden; genaue Revision noch dokumentieren.'),('2 Einsätze','LoDi 514, WiB ICE-M Front','Ein vorhandener Satz; je ein Einsatz pro Kopf.'),('1','ESU 59649, LokPilot 5 M4 / MKL','Vorhanden; Motoranschlüsse hinten bleiben einzeln isoliert.'),('1','21MTC-Trägerplatine aus 60977','Vorgesehen für hinten; Stecklage und Belegung prüfen.'),('1 vorgesehen','Märklin 60974, Pufferelektronik','Bestand 2; für diesen Zug nur einen am 60977 einplanen. Anschlussfreigabe auf S. 15.'),('je 1','Märklin E395640 / E395660','Kopf-Kupplungen als Teilekandidaten; Bestand und Passung prüfen.'),('je 1 pro Wagen','Märklin E374340 / E374060','Zwei Wagenenden; mechanische Passung vor Bestellung/Montage prüfen.'),('1 pro Wagen','LoDi-WiB ICE-M, passende Ausführung','Vorliegende Bilder zeigen MT-37700 V4.3; tatsächliche Wagenzahl und Bestand erfassen.'),('2 hinten','LED-Serienwiderstände Weiß / Rot','Endgültige Werte erst nach Freigabe auf S. 11.'),('nach Bedarf','Flexible Litze, Schrumpfschlauch, geeignete Isolierfolie, Befestigung','Querschnitt und Stromtragfähigkeit für Motorstrom über Kupplungen auslegen; keine starren Deichselkabel.')],[1.1,2.8,3.7])
add('Werkzeug: Multimeter mit Widerstands- und Diodenmessung, feine isolierte Messspitzen oder Prüfclips, Lupe, Schraubendreher, Pinzette, geregelte Lötstation, Elektroniklot und Entlöthilfe. Keine Säure/Lötwasser. Für ESU-Einrichtung und nicht sicher messbare Lastprüfungen Zugang zu geeignetem Programmer/Prüfstand oder einem Fachbetrieb einplanen.','small')
add('Die Kupplungsnummern stammen aus der dokumentierten verwandten Baureihe, nicht aus einer vollständigen 2976-Stückliste. Stückzahlen sind Einbauteile, keine zugesicherte Verpackungseinheit. Die LoDi-Kurznummern 511/514 folgen dem vorhandenen Bestand.','small')
refs(13)

page('2. Das Multimeter richtig vorbereiten')
warn('STOPP - nie Widerstand an einem gespeisten Aufbau messen','Alle Gleis- und Programmieranschlüsse physisch trennen. Beide Decoder und den Puffer abziehen. Ein geladener Puffer bleibt eine Spannungsquelle. Nicht kurzschließen, nicht mit dem Schraubendreher entladen. Bei unklarer Entladung zuerst Herstelleranweisung bzw. Fachbetrieb nutzen.')
step(1,'Messleitungen einstecken.','Schwarz in COM, Rot in V/Ω. Die rote Leitung darf für diese Prüfungen NICHT in A oder mA stecken. Messspitzen so isolieren, dass nur die nötige Spitze frei bleibt.')
step(2,'Nullprobe machen.','Widerstandsbereich wählen und Spitzen zusammenhalten. Den angezeigten Leitungswiderstand notieren, etwa 0,3 Ω. Das ist nur ein Beispiel, nicht der Sollwert jedes Geräts.')
step(3,'Offenprobe machen.','Spitzen trennen. Das Gerät muss seinen offenen Zustand anzeigen, oft OL oder 1. Bedeutung anhand der eigenen Geräteanleitung klären. Danach nochmals zusammenhalten: Die Anzeige muss reproduzierbar wechseln.')
step(4,'Chassis-Bezugspunkt sichern.','An zwei nachweislich leitenden, blanken Stellen desselben Chassisteils messen. Erwartet wird ein Wert nahe dem Leitungswiderstand. Lack oder Oxid kann falsches OL vortäuschen. Einen blanken Schraubenkopf nur nach dieser Gegenprobe als Bezug verwenden.')
step(5,'Isolationsmessung machen.','Für die hier geforderten Draht-/Motormessungen den zu prüfenden Teil vollständig von Decodern, Puffer und übrigen Platinen abtrennen. Nicht mit den Fingern gleichzeitig beide Metallspitzen berühren. Anzeige stabil werden lassen; vorhandene Kondensatoren können kurz einen Ladestrom verursachen.')
table(['Anzeige','Bedeutung / Reaktion'],[
('Nahe Leitungswiderstand','Leitende Verbindung. Gut nur an einer ausdrücklich gewünschten Verbindung.'),('OL / Bereichsüberlauf','Bei sicher kontaktierenden Spitzen und abgetrenntem Teil: kein mit diesem Gerät messbarer Leitungsweg. Kein Hochspannungs-Isolationsnachweis.'),('Endlicher oder schwankender Wert','Nicht pauschal freigeben. Kontakt, Feuchte/Kohlestaub, angeschlossene Bauteile oder eine ungewollte Verbindung untersuchen.'),('Piepton allein','Keine ausreichende Aussage: Schwellenwert ist geräteabhängig, Halbleiter/Kondensatoren können täuschen.')],[1.4,4.8])
add('Keinen 250-/500-V-Isolationstester an Decoder, LEDs oder Platinen anschließen. Für diese Schritte ist ein gewöhnliches, nach Anleitung verwendetes Elektronik-Multimeter vorgesehen.','small')

page('3. Die vier elektrischen Bereiche trennen')
story.append(Sketch('grounds'))
add('Gleismasse, Decoder-GND und Decoder-U+ sind nicht austauschbar. Besonders gefährlich ist das Wort „Masse“, wenn nicht gesagt wird, welcher Stromkreis gemeint ist. Die verbindlichen Anschlüsse sind funktional zu identifizieren.<super>10,11</super>')
table(['Netz','Zielzustand','Gefährlicher Fehler'],[
('Gleis B / RT','Roh-Digitalsignal vom Mittelschleifer; in REV5 zwischen beiden Köpfen durchverbunden.','Mit U+ oder einem Motor-/Lichtausgang verwechseln.'),('Gleis 0 / Radmasse','Sicherer Rückweg über Räder und dafür vorgesehene Chassiskontakte.','Alle Massekontakte entfernen und damit die Stromaufnahme zerstören.'),('Decoder-U+','Gleichgerichtete positive Funktionsversorgung innerhalb des jeweiligen Decoders.','U+ mit Chassis, Gleis 0 oder dem U+ des anderen Decoders verbinden.'),('Decoder-GND','Interne Gleichrichter-Minusleitung, z. B. für eine ausdrücklich passende Pufferverbindung.','Mit Radmasse oder einem braunen Fahrzeugkabel gleichsetzen.')],[1.25,2.3,2.8])
h('Konkrete Farbfallen')
add('Märklin verwendet häufig Orange für U+, Grün/Blau für Motor und Braun für Radmasse. In NEM-/ESU-Kabelsätzen kann Blau U+ und Orange ein Motoranschluss sein. LoDi zeigt bei alten Frontlampen sogar Braun oder Orange als gemeinsamen Plusleiter. Deshalb: Leitung beschriften und durchmessen, nicht „Braun immer Masse“ anwenden.<super>1,3</super>')
step(6,'Eigene Kennzeichnung anbringen.','Etiketten B, 0, M1, M2, U+, W, R und GE verwenden. Vorhandene Kabelfarben zusätzlich im Protokoll festhalten. W/R bezeichnen LED-Farbe, nicht die Farbe der Litze.')
refs(1,10,11)

page('4. Altzustand am Motortriebkopf erfassen')
P1='/Users/martinwaelter/ICE Umbau/Arbeitsstand_REV10/bilder/0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg'
P2='/Users/martinwaelter/ICE Umbau/Arbeitsstand_REV10/bilder/BAD231CB-B878-4D94-B5EE-CDAB1D69D455_4_5005_c.jpeg'
story.append(photo(P1,W,125));story.append(Spacer(1,5));story.append(photo(P2,W,150))
add('Bereitgestellte Originalfotos: Feldspulenmotor und alte lange Leiterplatte. Die verdeckte Unterseite, Lampenkontakte und Befestigungen sind nicht vollständig erkennbar. Die Fotos legen deshalb keine sichere Leiterbahn-Trennstelle fest.','small')
step(7,'Nur spannungslos öffnen.','Gehäuse nach der mechanischen Aufnahme lösen, ohne Leitungen zu ziehen. Alle Schrauben geordnet ablegen und ihre ursprünglichen Einbauorte fotografieren. Vor weiteren Arbeiten die gesamte Unterseite und Lampenfassung dokumentieren.')
step(8,'Leitungswege verfolgen.','Vom Schleiferblech zur Anschlusslitze, von Radkontakten zum Chassis und von beiden Motorbürsten zu alter Elektrik verfolgen. Alte Oberleitungs-/Umschaltkontakte, Federbleche und Schraubösen nur als vorhanden werten, wenn am Modell gesehen.')
step(9,'Alte Elektrik abtrennen.','Leitungen an den vorgesehenen Lötstellen lösen; alte Platine/Umschalter und die ersetzten Lampenfassungen als Baugruppen ausbauen und aufbewahren. Kein unbekanntes Leiterbahnmuster auf Verdacht auftrennen.')
warn('Kritisch - verdeckte Lampenmasse','Bei vergleichbaren Märklin-Fahrzeugen kann eine Fassung über Federblech, Halter oder Schraube am Chassis liegen. Eine neue LED-Plusleitung an derselben Kontaktzunge wäre dann ein U+-Chassisschluss. Die alte Fassung wird hier nicht elektrisch weiterverwendet; den neuen Einsatz und seine Befestigung separat prüfen.')
refs(1,14)

page('5. Motor 60941 montieren und entstören')
step(10,'Motor zerlegen.','Bürstenfedern kontrolliert entlasten und Bürsten entnehmen. Motorschild und Feldspule ausbauen. Lage von Rotor, Lagern und vorhandenen Scheiben dokumentieren. Teile nicht über dem offenen Getriebe ablegen.')
step(11,'60941 einsetzen.','Permanentmagnet, fünfpoligen Rotor und neues Motorschild in der Reihenfolge der Märklin-Zeichnung einsetzen. Originalgetriebe und Lagersitze bleiben maßgeblich. Teile müssen ohne Druck passen; sonst Passung und Lage prüfen, nicht nachfeilen oder festziehen.')
step(12,'Schrauben prüfen.','Passende Schrauben am ursprünglichen Ort einsetzen, schrittweise nur sicher anziehen. Nach jeder Schraube den Antrieb vorsichtig bewegen. Magnetische Rastung ist möglich; ein harter Anschlag oder starkes Klemmen ist nicht normal. Nicht über die Räder gewaltsam zurückdrehen.')
step(13,'Bürsten und Federn montieren.','Bürsten müssen frei sitzen; Federn dürfen weder Nachbar-Lötpunkt noch Chassis berühren. Jede mitgelieferte Entstördrossel gehört in eine Motorleitung. Eine Drossel ist kein LED-Vorwiderstand.<super>2</super>')
story.append(Sketch('caps',160))
add('Ein Kondensator zwischen M1 und M2 ist von einer Verbindung M1-Chassis oder M2-Chassis zu unterscheiden. Seitliche Entstörkondensatoren zum Gehäuse werden im vorgesehenen Decoderumbau entfernt; den Quer-Kondensator nicht blind mit abschneiden. Bauteil zuerst an beiden Enden verfolgen, dann gezielt auslöten.<super>3,6</super>')
add('<b>Ein unerwünschter Masse-Kondensator kann beim Ohmtest nach kurzer Zeit ebenfalls OL anzeigen.</b> Deshalb beide Anschlussdrähte zusätzlich mit Lupe verfolgen. Fotos und konkrete Prüfkarte: Abschnitte 21/22.','small')
warn('STOPP - Motor noch nicht an den Decoder','Ein übersehener Massekontakt an einer Bürste kann die Motorendstufe beschädigen. Die beiden Motorleitungen bleiben für die folgenden Prüfungen von der Platine getrennt. Keine Einmessfahrt und kein Versuch mit einem alten Analog-Umschaltimpuls.')
refs(2,6)

page('6. Motorisolation Schritt für Schritt messen')
story.append(Sketch('motor'))
add('Gestrichelt = Messstrecke, kein einzubauender Draht. M1/M2 bezeichnen die zwei Bürstenanschlüsse, keine feste Plus-/Minuspolung.','small')
add('Voraussetzung: Decoder/Puffer entfernt, Motorleitungen an der Platine abgetrennt. Beide Motoranschlüsse sind eindeutig benannt. Die Null-/Offenprobe des Messgeräts und der blanke Chassis-Bezugspunkt sind bereits geprüft.')
add('Vorher den Kontakt zu beiden Bürstenfahnen durch einen bleibenden endlichen Widerstand M1-M2 bestätigen; bei OL zuerst den Messkontakt und Motorpfad klären. Bildanleitung: Abschnitt 22, B2.','small')
step(14,'M1 gegen Gehäuse messen.','Schwarze Spitze mit Prüfclip am bestätigten Chassispunkt fixieren. Rote Spitze direkt an die metallische Anschlussfahne der ersten Bürste halten. Höchsten sinnvollen Widerstandsbereich verwenden und warten, bis die Anzeige stabil ist.')
step(15,'M2 genauso messen.','Nur die rote Spitze zur zweiten Bürstenfahne umsetzen. Beide Einzelwerte notieren. OL an einer Bürste ersetzt nicht die Prüfung der anderen.')
step(16,'Weitere Gegenstellen prüfen.','Jeden Motoranschluss auch gegen Motor-Metallrahmen, vorgesehene Radmasse und Schleiferleitung prüfen. Rotor vorsichtig in mehrere Positionen bringen; Motor-/Drehgestellleitungen dabei leicht bewegen. Die isolierten Messpaare müssen isoliert bleiben.')
add('Dauerhaft OL zwischen M1 und M2 trotz eingesetzter Bürsten ist kein bestandener Motortest: Bürstenkontakt, Rotor und Leitungsdurchgang müssen dann geprüft werden.','small')
table(['Messpaar am abgetrennten Motor','SOLL'],[
('M1 - Chassis; M2 - Chassis','Stabil offen / OL, keine verbleibende endliche Verbindung.'),('M1/M2 jeweils - Motorrahmen, Radmasse und Schleifer','Ebenfalls stabil offen / OL.'),('M1 - M2 mit eingesetzten Bürsten','Endlicher Motorwiderstand möglich/erwartet; kann mit Rotorstellung variieren. Hier ist OL KEIN allgemeines Isolationsziel.'),('Nach Montage von Schrauben und Leitungsführung','Alle Isolationspaare wiederholen, auch beim Ausschwenken des Drehgestells.')],[3.6,3.5])
warn('Bei Abweichung nicht „kurz probieren“','Erst nach der Fehlerlokalisierung auf der nächsten Seite weiterarbeiten. Der Decoder ist kein Kurzschlussprüfgerät. Ein niedriger Stromwert im Leerlauf beweist nicht, dass eine bewegungsabhängige Massebrücke fehlt.')

page('7. Versteckte Massekontakte finden')
story.append(Sketch('screw',160))
step(17,'Messung reproduzieren.','Bei endlichem Wert den Messbereich, Rotor- und Drehgestellstellung festhalten. Gegenprobe: Rote Spitze abheben muss OL ergeben. Bleibt die Anzeige gleich, zuerst Messgerät/Prüfclips untersuchen.')
step(18,'Leitungen ausschließen.','Motorlitzen vollständig freilegen und auf blanke Stellen, eingeklemmte Adern und einzelne abstehende Drähtchen kontrollieren. Eine elektrisch abgetrennte, bewegte Litze muss gegen Chassis offen bleiben.')
step(19,'Bürstenbereich prüfen.','Federenden, Lötfahnen und Kondensatoranschlüsse mit Lupe prüfen. Beispiel: Eine Feder liegt erst nach dem Einsetzen der Bürste auf einem Metallteil. Nur die Ursache korrigieren; nicht wahllos Massebleche entfernen.')
step(20,'Befestigung eingrenzen.','Nur spannungslos jeweils eine Befestigung kontrolliert lösen, Zustand vergleichen und danach korrekt montieren. Verschwindet die Verbindung beim Lösen einer Schraube, nach überlangem Gewinde, schiefem Abstandhalter oder Kontakt zur Lötstelle suchen. Eine lose Schraube ist keine Lösung.')
step(21,'Verschmutzung prüfen.','Kohlestaub und metallische Späne können Leiterbrücken bilden. Mit materialverträglicher Reinigung entfernen; vollständig trocknen lassen. Nicht Motorlager fluten und keine leitenden Rückstände verteilen.')
h('Drei typische Beispiele')
table(['Beobachtung','Mögliche Ursache','Gezielte Gegenprobe'],[
('Offen ohne Schraube, leitend nach Festziehen','Schraube/Unterlegscheibe berührt eine Motor- oder Plusfahne.','Lage fotografieren; Fahnenspiel und Schraubenlänge prüfen; korrekt montiert erneut messen.'),('Nur in einer Kurve leitend','Zu kurze Litze scheuert am Drehgestell oder wird gezogen.','Drehgestell in beide Endlagen bewegen; Ader und Lötstelle getrennt beobachten.'),('Offen mit abgehobenem Schild, leitend montiert','Feder, Bauteilbein oder Schildkontakt liegt am Rahmen.','Bürsten/Federn einzeln untersuchen; Bauteilenden verfolgen.')],[1.7,2.3,2.8])
add('Dieser Prüfablauf gilt auch bei vergleichbaren Märklin-Trommelkollektormotoren. Eine konkrete Trennstelle aus einem anderen Modell darf dagegen nicht ungeprüft auf den 2976 übertragen werden.','small')

page('8. Die rote Motorplatine sicher zuordnen')
redphoto='/Users/martinwaelter/ICE Umbau/Arbeitsstand_REV10/bilder/image-2.jpg'
notes=[p('<b>1 - 21MTC in der Mitte</b><br/>Die Stecklage muss am Index und an der tatsächlichen Platine bestimmt werden. Nicht allein „Bauteile oben“ als Regel verwenden.','body'),
 p('<b>2 - K1 im oberen Bereich</b><br/>Unbestücktes großes Kontaktfeld. Nicht als SUSI-/Pufferbuchse verwenden. Das Foto liefert dafür keine Freigabe.','body'),
 p('<b>3 - LS1 / LS2, rechts unter 21MTC</b><br/>Beschrifteter Lautsprecherbereich. Vor Anschluss prüfen, dass die Pads tatsächlich zum vorgesehenen Lautsprecherausgang gehören.','body'),
 p('<b>4 - Widerstände unten rechts</b><br/>Die Herstelleranleitung nennt R4/R5 für LEDs. Keine Null-Ohm-Brücke für Glühlampen übernehmen. Bestückung der eigenen Revision verifizieren.','body'),
 p('<b>5 - Beide großen Befestigungsringe</b><br/>Links oben sowie rechts unten. Ein Ring kann absichtlich ein Netz führen. Vor Montage seine Funktion messen; weder Masse noch Isolation pauschal annehmen.','body'),
 p('<b>Rückseite und Revision fehlen</b><br/>Vor dem Löten Aufdrucke sowie alle Anschlussbezeichnungen dokumentieren. Das zweite rote Bild zeigt dieselbe sichtbare Ansicht, keinen Beleg der Rückseite.','body')]
t=Table([[MarkedPhoto(redphoto,130,[(1,.45,.584,.50,.44),(2,.32,.289,.77,.32),(3,.825,.674,.66,.745),(4,.775,.827,.44,.865),(5,.126,.206,.23,.105),(5,.846,.916,.67,.967)],525),notes]],colWidths=[145,W-145]);t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),10)]));story.append(t)
add('Eigenes Foto image-2.jpg, unverändert unter den Markierungen. „Oben/unten“ meint ausschließlich diese Bildansicht; eine Einbaurichtung ist daraus nicht freigegeben.','small')
warn('STOPP - gleiche Jumpernamen können Verschiedenes bedeuten','Die sichtbare weiße Wagenplatine hat SJ2 für Türbeleuchtung. Die LoDi-Motoranleitung beschreibt bei bestimmten Motorrevisionen SJ1/SJ2 als AUX-Auswahl. Diese Angaben nicht zwischen Platinen übertragen. Keine neue Brücke setzen, bevor die konkrete Motorrevision zugeordnet ist.')
refs(3)

page('9. Motorplatine montieren und anschließen')
step(22,'Unbestückt probemontieren.','Ohne Decoder, Puffer und angeschlossene Lasten die Platine an ihren vorgesehenen Haltepunkten platzieren. Unterseite und Abstand zu Chassis, Schrauben, Metalllaschen und Dachkontakt prüfen. Nur passende isolierende Halter verwenden; keine Metallfolie als Isolation.')
step(23,'Montagekontakte messen.','Ringe der ausgebauten Platine nur zu eindeutig identifizierten, schaltplanbekannten Netzpunkten zuordnen. Ein Piepton oder endlicher Wert über Bauteile beweist keine direkte Leiterbahn. Ohne geklärte Ringfunktion keine Schraubmontage freigeben. Nach Montage auch Schraubenkopf, Unterlegscheibe und Abstandhalter auf Kontakt zu Nachbarflächen prüfen. Ungeklärte Verbindung an U+, Motor oder Ausgang: stoppen; vorgesehene Radmasse erhalten.')
step(24,'Leitungen funktional anschließen.','Erst bei eindeutig bestätigten Pads gemäß Tabelle löten. Decoder dabei abgezogen. Litze kurz abisolieren, verzinnen, ohne Zug anlöten. Kein Lötdraht unter die Platine fallen lassen; jeden Anschluss anschließend mit Lupe kontrollieren.')
table(['Funktion','Verbindung im gewählten Aufbau'],[
('Rohstrom B / RT','Vorderer Schleifer und gemeinsame RT-Kupplungsleitung an den dafür vorgesehenen Rohstrompfad.'),('Radmasse 0','Vorgesehener Radsatz-/Chassiskontakt an den Gleisrückleiter der LoDi-Platine.'),('Motor','M1/M2 über je eine Drossel an Motor L/R; keine Verbindung zu Chassis/U+.'),('Frontlicht','LoDi-Frontmodul an vorgesehenes LED-Plus, L_WS und L_RT; vorhandene LED-Vorwiderstände wirksam lassen.'),('Innenbeleuchtung GE','Nur der auf dieser Motorrevision vorgesehene Beleuchtungspfad des Hauptdecoders; AUX-Zuordnung passend konfigurieren.'),('Lautsprecher','Ein passender Lautsprecher ausschließlich zwischen LS1 und LS2, mechanisch sicher und ohne Kontakt zur Membran.')],[1.4,4.7])
warn('Kritisch - Lautsprecher und Funktionsausgänge','Keinen Lautsprecheranschluss an Chassis/U+ legen und nicht zwei Lautsprecher auf Verdacht parallel verbinden. Beide Audioanschlüsse gehören zum Audioausgang. Ein gleich aussehender freier Stecker ist kein Beleg für dieselbe Funktion.')
add('Bei Motorplatinen, auf die LoDis Jumper-Anweisung tatsächlich zutrifft, darf nur die gewählte AUX-Brücke gesetzt sein. Zwei gleichzeitig gesetzte Auswahlbrücken können Ausgänge verbinden. Auf der fotografierten roten Platine ist die dazu passende Revision nicht sicher ablesbar.','small')
refs(1,3)

page('10. Front-LEDs gefahrlos identifizieren')
story.append(Sketch('led'))
add('Die beiden ESU-Kästen zeigen Anschlüsse desselben hinteren Decoders. U+ links speist beide LED-Anoden; rechts schaltet je ein eigener Lichtausgang.','small')
add('Die LoDi-Frontmodule enthalten laut Hersteller keine Vorwiderstände. Vorne ist die vorgesehene Strombegrenzung der LoDi-Motorplatine zu verwenden. Hinten braucht jeder Farbzweig einen eigenen Serienwiderstand.<super>3,5</super>')
step(25,'Modul dokumentieren.','Vorder-/Rückseite des tatsächlichen Fronteinsatzes fotografieren; Plus, Weiß und Rot anhand Beschriftung und Herstellerplan zuordnen. Die Zahl der Lichtöffnungen ist nicht die Zahl der LEDs; Lichtleiter können Licht verteilen.')
step(26,'Polung nur begrenzt prüfen.','Eine Diodentestfunktion nur nutzen, wenn deren Prüfstrom und maximale Prüfspannung laut Geräteanleitung für die bekannten LEDs geeignet sind. Rot an dokumentierte Anode/Plus, Schwarz an die betreffende Kathode. Nicht zum Raten mit hoher Spannung umpolen.')
step(27,'Anzeige richtig deuten.','Schwaches Leuchten oder eine plausible Vorwärtsspannung kann die Polung bestätigen. OL beweist keine defekte LED: Prüfspannung kann zu klein sein oder der Zweig mehrere LEDs enthalten. Keine höhere Spannung auf Verdacht anlegen.')
step(28,'Elektrische Daten sichern.','Für die endgültige Widerstandsauslegung Zweigstruktur, zulässigen Betriebsstrom und minimale Zweigspannung klären. Eine gemessene Flussspannung sagt nichts über den erlaubten Maximalstrom aus. Bei fehlenden Daten LoDi bzw. einen Fachbetrieb die konkreten Einsätze charakterisieren lassen.')
warn('STOPP - LEDs nie unmittelbar ans Digitalgleis','Kein Test direkt an Gleis, Trafo, Decoder-U+ oder einem unbekannten LED-Tester. Decoder-Dimmung ist kein Ersatz für Strombegrenzung. Auch eine sehr kurze falsche Verbindung kann eine LED zerstören.')
add('Die neuen Fotos zeigen Wagen- und Motorplatinen, aber nicht die tatsächlichen LoDi-514-Fronteinsätze. Deshalb enthält die nächste Seite eine nachvollziehbare Berechnung, ausdrücklich keine bereits freigegebene Bestückung deines unbekannten LED-Zweigs.','small')
refs(5,6)

page('11. Hintere Vorwiderstände bestimmen')
h('Rechenweg mit gesicherten Eingabewerten')
add('<b>R mindestens = (U maximal - U LED-Zweig minimal) / I zulässig.</b> Einen Ausgangsspannungsabfall kann man für eine konservative Rechnung mit null ansetzen. Die Widerstandstoleranz muss auch beim kleinsten tatsächlichen Widerstand eingehalten werden. Verlustleistung: P = (U maximal - U LED-Zweig minimal)² / R tatsächlich.')
table(['Reines Zahlenbeispiel','Weiß','Rot'],[
('Angenommene maximale Versorgung','24 V','24 V'),('Angenommene minimale Zweigspannung','3,0 V','2,0 V'),('Angenommener freigegebener Strom','3 mA','3 mA'),('Rechnerisches R mindestens','7,0 kΩ','7,33 kΩ'),('Beispiel für Normwert mit 1 % Toleranz','7,5 kΩ','7,5 kΩ'),('Größter Strom bei R -1 %','ca. 2,83 mA','ca. 2,96 mA'),('Größte Widerstandsleistung','ca. 0,060 W','ca. 0,065 W')],[2.8,1.8,1.8])
warn('Dieses Beispiel ist KEINE Lötfreigabe','24 V, 3/2 V und 3 mA sind Beispielannahmen. Sie sind für deine Frontmodule nicht nachgewiesen. Auch ein 0,25-W-Widerstand im Beispiel ersetzt keine thermische Prüfung des realen Einbaus. Nicht einfach 7,5 kΩ übernehmen, bevor die Eingaben bestätigt sind.')
step(29,'Reale Spannung verifizieren.','Gleis-Digitalspannung und gepulste Funktionsspannung sind keine gewöhnliche Sinus-AC-Spannung. Ein einfacher AC-Multimeterwert am Gleis oder PWM-Ausgang ist nicht automatisch der Maximalwert für diese Rechnung. Geeignete Messung und eingestellte Versorgungsspannung dokumentieren.')
step(30,'Widerstände vor Einbau messen.','Beide Widerstände einzeln abgetrennt im Ohmbereich messen, Wert/Toleranz notieren. Beispielsweise 7,5 Ω und 7,5 kΩ unterscheiden sich um Faktor 1000. Farbringverwechslung nicht durch Probebetrieb klären.')
step(31,'Einlöten und isolieren.','Jeden Widerstand in seinen eigenen Weiß-/Rot-Zweig setzen. Drähte einzeln isolieren, Widerstandskörper mechanisch und thermisch geeignet befestigen; nicht direkt gegen Kunststoff oder LED drücken. Strombegrenzung prüfen, bevor der ESU eingesetzt wird.')

page('12. Motorlosen Kopf aufbauen')
step(32,'Alte Beleuchtung abtrennen.','Schleifer und Radmasse zuerst identifizieren. Alte Lampenfassung und ersetzte Elektrik abklemmen. Die neue LED-Halterung darf weder über eine Kontaktfeder noch eine Schraube ihren Pluskontakt mit dem Chassis verbinden.')
step(33,'Trägerplatine verifizieren.','Die vorgesehene Platine aus dem 60977-Set ohne Decoder begutachten. Funktions-/Gleisanschlüsse nach Herstellerplan durchmessen. Eine 21MTC-Bauform allein ist kein Freigabesiegel: MKL-Ausgänge und tatsächliche Platinenbelegung müssen zusammenpassen.')
step(34,'21MTC-Stecklage festlegen.','Fehlende Stiftposition/Index ermitteln, mit Decoder und Platinenanleitung vergleichen. Buchse und Stifte müssen deckungsgleich sein. Nicht um einen Pin versetzen, nicht schräg eindrücken und nicht mit Gewalt auf einen scheinbar fehlenden Kontakt drücken.<super>10</super>')
table(['Hintere Funktion','Anschlussziel'],[
('Decoder-Gleiseingang B','Gemeinsamer RT-Rohstrompfad; hinterer Schleifer speist ebenfalls hinein.'),('Decoder-Gleiseingang 0','Nachweislich zuverlässige örtliche Rad-/Schienenmasse.'),('LED-Plus','Nur U+ des hinteren 59649, elektrisch vom Chassis getrennt.'),('Weiße / rote LED','Jeweils über den freigegebenen Serienwiderstand an den zugeordneten Lichtausgang.'),('Nicht benötigte Motor-/AUX-Leitungen','Jede Leitung einzeln isolieren. Nicht gemeinsam verdrillen oder an Masse legen.'),('Innenlicht-GE','Nicht zusätzlich an einen ESU-Ausgang anschließen. Die Innenbeleuchtung wird vorn geschaltet.')],[1.8,4.5])
step(35,'Mechanische Endkontrolle.','Decoder noch abgezogen: Träger befestigen, Drehgestell ausschwenken, Kupplung bewegen, Gehäuse probeweise ohne Klemmen aufsetzen. Gewünschte Leitungsdurchgänge und unerwünschte Masseverbindungen erneut prüfen. Erst danach einsetzen.')
warn('Kritisch - an der hinteren Trägerbuchse','Eine mechanisch passende Pufferbuchse auf der Märklin-Trägerplatine gibt den Anschluss eines 60974 an den ESU nicht frei. Der geplante Märklin-Puffer gehört ausschließlich zum kompatiblen 60977 und bleibt hier unverbunden.')
refs(6,10,15)

page('13. Mittelwagenplatinen montieren')
story.append(photo('/Users/martinwaelter/ICE Umbau/Arbeitsstand_REV10/bilder/image-4.jpg',W, seventy:=75));story.append(Spacer(1,7))
story.append(photo('/Users/martinwaelter/ICE Umbau/Arbeitsstand_REV10/bilder/image-5.jpg',W,180))
add('Bereitgestellte Bilder: LoDi-WiB ICE1-M, MT-37700 V4.3, Anschlüsse L/O/B an beiden Enden. Das Einbaubild zeigt ein Bordrestaurant; es beweist nicht die Passung jedes Mittelwagens deines 2976. SJ2 ist auf dieser Wagenplatine als Türbeleuchtung beschriftet.','small')
step(36,'Ersten Wagen als Muster öffnen.','Endabdeckungen und Oberteil vorsichtig nach den tatsächlichen Rastungen lösen. Nicht am transparenten Fenstereinsatz hebeln. Kupplungen, Haltenasen und vorhandene Kabel vor Ausbau fotografieren.')
step(37,'Trocken einpassen.','Platine ohne Decoderstrom auflegen. Dach muss ohne Druck schließen, Litzen dürfen weder Türfenster verdecken noch unter einer Schraube liegen. Bei abweichender Passung nicht Platine oder Wagenboden auf Verdacht kürzen.')
step(38,'Kupplungen anbinden.','Flexible Litzen von jeder Kupplung zur vorgesehenen Platinenstelle führen. Kleine Bewegungsschlaufe vorsehen, sodass die Deichsel beide Endlagen erreicht, ohne an einer Lötstelle zu ziehen. Kein längs durch den Wagen zusätzliches Steuerkabel einziehen.')
table(['Nur für verifizierten LoDi-Motorplatinenbetrieb','Belegung laut LoDi'],[
('L','Geschalteter Beleuchtungspfad / GE'),('O','Roh-Mittelleiter / RT'),('B','Optionaler Radmasseanschluss; im hier gewählten zweipoligen Aufbau nicht zusätzlich verdrahten.')],[3.8,2.5])
warn('Anschlussvariante vor Löten kontrollieren','LoDi beschreibt auch eine andere Anschlussvariante mit anderer O/B-Zuordnung. Diese nicht mischen. Bei der weißen V4.3 darf SJ2 nicht als Motor-AUX-Auswahl interpretiert werden. Bestehende Radmassefedern in den Wagen nur gemäß bestätigtem zweipoligem LoDi-Aufbau entfernen; die Radkontakte der Triebköpfe bleiben erforderlich.')
refs(4)

page('14. Kupplungsbus aufbauen und durchmessen')
story.append(Sketch('bus',200))
step(39,'Kupplungen mechanisch prüfen.','E395640/E395660 an den Köpfen sowie E374340/E374060 an den Wagenenden nur nach Passprobe einsetzen. Rastung, Höhe, Endprofil und seitliches Spiel vergleichen. Nicht durch Feilen oder Drücken eine falsche Aufnahme passend machen.')
step(40,'Jedes Kabel zuerst allein messen.','Noch ohne angeschlossene Elektronik: Ende zu Ende muss nahezu Leitungswiderstand vorliegen. Jede Litze gegen Chassis und Nachbarlitze muss offen sein. Dabei knicken/bewegen, ohne mechanisch zu beschädigen.')
step(41,'Jede Kupplung und jeden Wagen messen.','Die zusammengehörigen Kontaktflächen durch Messen bestimmen, nicht nach Links/Rechtslage raten. Beide Kupplungsrichtungen fotografieren. Über jede gewünschte Durchleitung muss ein stabil niedriger Widerstand bestehen, auch bei Ausschwenken.')
table(['Prüfung des abgetrennten passiven Kabel-/Kupplungspfads','SOLL'],[
('RT vorne - RT hinten / beide Schleifer','Durchgang ist in REV5 ausdrücklich gewollt.'),('GE Wagenende A - GE Wagenende B','Gewünschte Durchleitung, aber keine zusätzliche ESU-Ausgangsverbindung.'),('RT - GE; RT - Chassis; GE - Chassis','Keine Drahtbrücke. Für eindeutige Prüfung aktive Platinen/LED-Lasten abtrennen.'),('Mit angeschlossenen LoDi-Platinen','Halbleiter können endliche Werte ergeben. Nicht pauschal OL fordern; bei Zweifeln Verbindungen wieder einzeln trennen.')],[3.7,2.6])
warn('STOPP - Stromquellen niemals über den Zug verbinden','Der lange Schleiferabstand kann Haupt-/Programmierausgänge oder Boosterabschnitte überbrücken. Den Zug nur vollständig in einem freigegebenen Stromkreis betreiben. Nicht einen Kopf auf dem Programmiergleis lassen, während der andere am Hauptgleis steht.')
refs(3,13)

page('15. Den vorhandenen 60974 vorbereiten')
warn('STOPP - dieser Anschluss ist noch nicht freigegeben','Die sichtbare rote LoDi-Motorplatine zeigt keine belegte SUSI-Buchse. K1, die drei runden Lötaugen am Frontende und die kleinen Durchkontaktierungen dürfen nicht als Pufferanschluss erraten werden. Für die folgenden ersten Funktionstests bleibt der 60974 abgesteckt.')
add('Der 60974 ist für den 60977 vorgesehen. Märklins dokumentierter Steckanschluss sitzt jedoch auf der Märklin-Trägerplatine; hier steckt der 60977 auf LoDi 511. Offen ist damit der konkrete Anschlussweg, nicht die grundsätzliche Decoderkompatibilität.<super>9</super>')
table(['Signal','21MTC-Kontakt','classicSUSI-Kontakt'],[
('Decoder-GND','20','1'),('Daten','6','2'),('Takt','5','3'),('Decoder-U+','16','4')],[3.2,1.7,1.7])
add('Diese Normzuordnung ist ein Prüfplan, keine Ansicht der Buchse am Foto. Pinzählung nur nach eindeutig bestimmter Indexlage. Pin 20 ist NICHT Gleismasse 21; Pin 16 ist NICHT Schleifer 22. Pin 12 (interne Vcc) ist ebenfalls nicht U+. Die Bezeichnung „VCC“ auf einer anderen Platine allein beweist keine Pinzuordnung.<super>10,11</super>')
step(42,'Rückseite und Revision erfassen.','Beide Seiten der roten Platine, Index und alle Aufdrucke scharf fotografieren. Stecker des Puffers unverändert lassen. Keinen Anschluss abschneiden, um ihn versuchsweise anzulöten.')
step(43,'Vier Netze fachkundig verfolgen.','An spannungsfreier, leerer LoDi-Trägerplatine Kontakte 5/6/16/20 zu dokumentierten Abgriffpunkten verfolgen. Je Punkt Pin, Fotoposition, Messwert und direkte bzw. über Bauteile geführte Verbindung notieren. Fremdbeschaltung von Takt/Daten und falsche Versorgungsnetze ausschließen. Kein Anschluss an erratene Steckstifte oder Durchkontaktierungen; ein Piepton genügt nicht.')
step(44,'Anschluss freigeben und erst dann ergänzen.','LoDi-Bestätigung für die Revision oder nachvollziehbare fachkundige Prüfung einholen. SUSI-Stecker samt Orientierung festlegen. Am 60977 Firmware 3.2.0.1 oder neuer nachweisen und SUSI nach Märklin einrichten. Takt/Daten dürfen nicht gleichzeitig andere Ausgänge bedienen. Zunächst nur Licht/Sound puffern, Motorpufferung ausgeschaltet lassen.')
add('Nur einen 60974 am kompatiblen Hauptdecoder einsetzen. Keine Puffer hintereinanderschalten. Ein gespeicherter Energievorrat ist auch nach Abschalten vorhanden; vor erneutem Löten trennen und korrekt entladen. Die Mittelwagenbeleuchtung ist durch diesen Anschluss nicht automatisch mitgepuffert.','small')
warn('Motorpufferung zuletzt testen','Motorpufferung erst mit ausreichend freier Sicherheitsstrecke und begrenztem, geprüftem Nachlauf aktivieren. CS3-STOP, Gleisabschaltung oder Abheben garantieren dann keinen sofortigen Stillstand. Werkseinstellungen sind keine geprüfte Einstellung für diesen Zug.')
refs(9,10,11)

page('16. Decoder getrennt einrichten')
step(45,'Konfiguration sichern.','Beide Decoder zunächst einzeln behandeln. Artikel, Firmware und aktuelle Einstellungen erfassen. Nur der jeweils zu programmierende Decoder darf am Programmer hängen; die gemeinsame Kupplungsversorgung dafür vollständig trennen.')
step(46,'60977 vorbereiten.','Passenden Motortyp für den 60941-HLA wählen, sinnvolle niedrige Anfangsgeschwindigkeit und Lautstärke setzen. ICE-Soundprojekt mit passendem Märklin-Werkzeug einrichten. mfx aktiv lassen. Ungewollte automatische Mess-/Fahrabläufe nicht starten.')
step(47,'59649 vorbereiten.','Mit geeignetem ESU-Programmierzugang einlesen. Ein normaler Lokdecoder ohne Motor kann beim Auslesen die Lastquittierung vermissen lassen. Dann nicht mehrfach wahllos umprogrammieren: passenden Prüfstand mit Quittierungslast bzw. Fachbetrieb verwenden.')
step(48,'Hauptdecoder-Identität bestimmen.','Für die ESU-Synchronisation Herstellerkennung und Seriennummer des 60977 eindeutig ermitteln. Keine DCC-Adresse, Artikelnummer oder Lok-Betriebsnummer einsetzen. ESUs Beispielwert 151 bezeichnet ESU, nicht den Märklin-Hauptdecoder.')
step(49,'Slave-Funktion einrichten.','Im passenden ESU-LokProgrammer unter Decoder/Sonderoptionen die Master-Decoder-Synchronisation aktivieren und die bestätigte Hauptdecoder-Identität eintragen. M4 bleibt eingeschaltet. Einstellungen speichern und erneut auslesen. Kein Hersteller-übergreifendes Soundprojekt aufspielen.')
table(['Zugrichtung bei F0 ein','Motortriebkopf','Motorloser Kopf'],[
('Motortriebkopf voraus','Weiß','Rot'),('Motorloser Kopf voraus','Rot','Weiß'),('F0 aus','Beide Farben aus','Beide Farben aus')],[3,2,2])
step(50,'Lichtmapping abstimmen.','Lichtzustände über F0 und Richtung schalten, nicht an tatsächliches Anrollen binden. Keine ungewollten Ein-/Ausblendverzögerungen. Innenlicht auf separate freie Funktion legen; vorhandene Soundbelegung dabei nicht überschreiben.')
add('ESU dokumentiert die Synchronisation am eigenen System; für mSD3 + LokPilot 5 M4 existiert ein direkter Praxisbericht. Die genaue 60977/59649/CS3-Kombination muss deshalb anschließend geprüft werden. Adresssynchronisation kopiert nicht automatisch Lichtmapping oder Helligkeit.','small')
refs(7,8)

page('17. Erstes Einschalten ohne Puffer')
warn('Vor Spannung: drei Freigaben müssen vorliegen','Motorisolation bestanden; reale Platinen-/Steckbelegung bestätigt; die jeweils angeschlossene LED-Strombegrenzung bestätigt. Nicht bestandene Baugruppen bleiben abgetrennt. Kein Dauer-Einschalten bei wiederholter Überlastmeldung.')
step(51,'Kurzes separates Gleisstück vorbereiten.','Einige vorhandene C-Gleise genügen für Prüfungen im Stand. Das Stück darf elektrisch mit keinem anderen Stromkreis verbunden sein. Genau einen Zentralenausgang verwenden; niemals CS3 und Gleisanschlussbox gleichzeitig einspeisen. Kein gesonderter Bremsabschnitt nötig.')
step(52,'Motortriebkopf allein prüfen.','Ohne Puffer und Wagenbus beginnen. Vor Spannung Fahrstufe 0 einstellen; Bewegung erst in Schritt 53. Gehäuse offen lassen, lose Leiter sichern. Nach Herstellerverfahren am getrennten Programmiergleis prüfen, danach am geeigneten Betriebsgleis mfx, F0 und leisen Sound kontrollieren. Programmierung ist kein Isolationstest.')
step(53,'Motor sehr langsam prüfen.','Nur bei gesichertem Fahrzeug und genügend Fahrweg eine kleine Fahrstufe kurz anlegen, dann auf null. Bei Brummen ohne Bewegung, Geruch, Überlast oder ungewöhnlicher Erwärmung sofort abschalten. Nicht den Rotor blockiert halten, um einen Grenzstrom zu ermitteln.')
step(54,'Slave ohne Wagenbus prüfen.','Erst nach LED-Freigabe: STOP und Fahrstufe 0 einstellen. Beide Köpfe ungekoppelt auf dasselbe isolierte, gemeinsam gespeiste Gleisstück stellen; Kupplungsleitungen getrennt und isoliert lassen. Einschalten, F0 und Richtung am angemeldeten ICE bedienen. Lichtzustände müssen Abschnitt 16 entsprechen. Eine eigene Anmeldung des Slaves ist kein Prüfkriterium.')
step(55,'Stromunterbrechung und Neustart prüfen.','Zentrale ausschalten und beide Köpfe gemeinsam neu starten. Dann den Dummy spannungsfrei abkoppeln, wieder anschließen und erneut starten. Lichtzustände und Zuordnung müssen wieder stimmen; fremde oder alte CS3-Einträge gezielt prüfen, nicht wahllos löschen.')
step(56,'Wagen schrittweise ergänzen.','Nach jedem Wagen abschalten, ankoppeln, prüfen und erst danach wieder einschalten. Den Bus nie unter Spannung stecken. Innenlicht muss unabhängig von F0 und Fahrtrichtung reagieren. Beim ersten Fehler den zuletzt hinzugefügten Abschnitt spannungsfrei isolieren.')
warn('Keine automatische Motoreinmessung auf kurzem Gleis','Der Märklin-Einmesslauf kann stark beschleunigen. Er gehört erst auf eine dafür geeignete freie Strecke gemäß Herstelleranleitung. Ein kurzer Prüfgleisabschnitt ist dafür ausdrücklich ungeeignet.')
refs(1)

page('18. Belastung und Gehäuseabschluss prüfen')
story.append(Sketch('ammeter',160))
add('Die gemeinsame Aufnahme kann den gesamten Motorstrom durch die Kupplungen schicken. Eine erfolgreiche Ohmmessung mit kleinem Prüfstrom beweist weder ausreichende Stromtragfähigkeit noch einen geringen Spannungsabfall unter Last.')
step(57,'Messverfahren vorab festlegen.','Für Strom im Digitalgleis und gepulsten Ausgängen geeignete Messtechnik verwenden. Eine einfache Multimeteranzeige ist je nach Messprinzip nur ein Mittelwert, keine sichere Spitzenstromfreigabe. Bei fehlender Erfahrung die Belastungsprüfung fachkundig durchführen lassen.')
step(58,'Keinen Mess-Kurzschluss bauen.','Ein Amperemeter wird ausschließlich in Reihe in einen vorher spannungsfrei geöffneten Strompfad eingesetzt, mit passendem abgesichertem Eingang und Bereich. Niemals im Strombereich direkt zwischen B und 0 halten. Nach der Messung Rot wieder nach V/Ω umstecken.')
step(59,'Last schrittweise steigern.','Alle vorgesehenen Wagen mit der späteren Helligkeit prüfen; Motorfahrt und Sound zusätzlich berücksichtigen. Dann bei geeigneter Sicherung die Einspeisung über jeweils nur einen Schleifer prüfen. Anschlussänderungen ausschließlich spannungslos, keine Metallstücke unter Schleifer klemmen.')
table(['Grenze des 60977','Herstellerwert'],[
('Motor-Dauerlast','höchstens 1,1 A'),('Je Lichtausgang / AUX1-AUX4','höchstens 250 mA'),('Licht und AUX zusammen','höchstens 300 mA'),('Gesamtlast','höchstens 1,6 A')],[4.4,2.1])
add('Dies sind Decodergrenzen, keine Freigabe jeder Kupplung oder Leiterbahn. Belasteten AUX-/LoDi-Pfad gesondert prüfen. Kein pauschales Maximum an Wagen ableiten. Bei unklarer Lastführung oder Erwärmung keine Freigabe.','small')
step(60,'Gehäuseabschluss zwingend prüfen.','Vor dem ersten bestromten Gehäuseschluss abschalten, abtrennen, Decoder/Puffer entfernen. Leitungen von Schraubdomen und Dachkontakten fernhalten. Passiven Aufbau mit korrekt geschlossenem Gehäuse erneut durchmessen; Drehgestelle/Kupplungen in beide Endlagen bewegen. Nur eindeutige, ggf. von Lasten abgetrennte Messpfade bewerten. Erst bei unverändertem SOLL wieder bestücken und Funktion prüfen. Vorgehen mit zugänglichen Prüfenden: Abschnitt 24.')
refs(1)

page('19. CS3-Bremsung später auf der Anlage')
story.append(Sketch('brake',170))
step(61,'Kontaktabschnitte prüfen.','An der vorhandenen Rückmeldung jeden Kontakt einzeln in der CS3 beobachten. Mit einem meldenden Radsatz belegen und räumen; Anzeige muss zuverlässig folgen. Gleis- und Rückmeldeanschlüsse nach den jeweiligen Herstellerunterlagen prüfen, nicht nur Signalbild betrachten.')
step(62,'ICE und Fahrweg eindeutig zuordnen.','Für die erste Inbetriebnahme einen fest zugeordneten ICE-Ablauf wählen. Beispielnamen wie KG-A und KG-B sind eigene Bezeichnungen, keine bereits vorhandenen Adressen. mfx-Anmeldung liefert keine automatische Identität am S88-Kontakt.')
step(63,'Brems- und Haltfolge einrichten.','Kontakt dem aktiven ICE-Ablauf zuordnen. Bei Halt am zugehörigen Signal sendet er einen langsamen Annäherungsbefehl; ein Haltemelder davor sendet Fahrstufe 0 an genau diesen ICE. Restbremsweg berücksichtigen. Bei passendem Fahrtbegriff und freiem Fahrweg darf dieser Haltablauf nicht stoppen. Unklare Freigabe ist kein Abfahrtsauftrag.')
step(64,'Beide Richtungen abnehmen.','Mit niedriger Geschwindigkeit Halt und erlaubte Durchfahrt prüfen. Erstes meldendes Rad, Zugüberhang und Bremsweg beachten. Zugspitze und Nachlauf müssen vor dem Schutzpunkt bleiben. Kontakte und Bremskurve mit tatsächlicher Zuglänge einstellen.')
step(65,'Fehlerfälle kontrolliert testen.','Belegtes Ziel, fehlende/falsche Meldung, Neustart und Signalwechsel prüfen. Erst ohne Fahrbewegung die Ereignislogik kontrollieren. Danach nur mit freiem Auslauf und erreichbarem STOP testen. Bei aktiver Motorpufferung möglichen Nachlauf trotz Gleisabschaltung berücksichtigen.')
warn('Regulärer Halt ist ein Fahrbefehl, keine Stromtrennung','Die Gleise bleiben digital versorgt. Rot allein hält einen nicht zugeordneten Zug nicht an. Ein falsch konfigurierter Ablauf kann Weiterfahrt verursachen. Der lange gemeinsame Schleiferbus darf zugleich keine fremden Booster-/Programmierabschnitte überbrücken.')
add('<b>Eine Kontaktflanke genügt nicht:</b> Beim Ablaufstart bereits belegte Kontakte und den aktuellen Signalzustand auswerten. Wechselt das Signal nach dem Bremskontakt auf Halt, muss der aktive Fahrweg erneut den richtigen ICE anhalten. Bis zur Prüfung dieser Fälle nur fest zugeordnete, beaufsichtigte Abläufe verwenden.','small')
add('Erst nach dieser Abnahme gilt die Signalbremsung als eingerichtet. Bis dahin den ICE manuell und beaufsichtigt betreiben. Rückmeldeverdrahtung unter der Anlage ist trotz fehlender Zusatzsteuerader im Zug erforderlich.','small')
refs(12,16)

page('20. Fehler gezielt eingrenzen und freigeben')
table(['Beobachtung','Spannungslos eingrenzen','Nicht tun'],[
('Kurzschluss sofort beim Einschalten','Zuletzt ergänzte Baugruppe trennen; RT/GE/0-Vertauschung, 21MTC-Lage und Metallkontakt prüfen.','Nicht wiederholt einschalten und auf Schutzschaltung vertrauen.'),('Fehler erst mit Gehäuse','Schrauben, Kabelquetschung, Dachfeder und Platinenabstand prüfen.','Nicht Gehäuse mit Kraft zuschrauben.'),('Fehler erst in Kurven','Deichsel-/Drehgestelllitzen auf Zug, Kontakt und abgescheuerte Isolation untersuchen.','Nicht starre Kabel weiter verkürzen.'),('LED dunkel','Strombegrenzung, Polung, Mapping und Versorgung getrennt prüfen.','Nicht Widerstand überbrücken oder direkt ans Gleis halten.'),('Motor brummt / wird warm','Mechanischen Freilauf, Bürsten und Motorisolation erneut prüfen.','Nicht höhere Fahrstufe geben oder blockiert testen.'),('Zwei Fahrzeugeinträge','Slave-Identität, Aktivierung und alte Einträge gezielt prüfen.','Nicht M4 pauschal ausschalten oder beliebige IDs übernehmen.'),('Innenlicht stört Frontlicht','GE-Ausgangszuordnung und unerwünschte Verbindung hinten prüfen.','Nicht Decoder-Ausgänge zusammenschalten.'),('Haltpunkt schwankt / Zug hält nicht','Rückmelder, ICE-Zuordnung, Fahrtrichtung und Restbremsweg prüfen.','Nicht allein rotes Signal als Bremsnachweis werten.')],[1.6,3.4,2.3])
h('Abnahmeblatt zum Ausfüllen')
table(['Prüfpunkt','Datum / Messwert / Ergebnis'],[
('Nullprobe / Chassis-Gegenprobe','_______________________________'),('M1/M2 gegen Chassis, Rahmen, Radmasse, B','_______________________________'),('Stecklage / Platinenrevision / Befestigung','_______________________________'),('LED-Daten / R Weiß / R Rot / Belastbarkeit','_______________________________'),('RT-/GE-Durchleitung, Bewegung und Gehäuse','_______________________________'),('mfx-Slave / Licht im Stand / Sound / Innenlicht','_______________________________'),('Last / Einzel-Schleiferbetrieb / Temperatur','_______________________________'),('60974-Anschluss separat freigegeben','_______________________________'),('CS3-Halt in beiden Richtungen','_______________________________')],[3.6,3.3])
add('Freigabe bedeutet: Prüfung tatsächlich durchgeführt und Ergebnis notiert. Nicht getestete Punkte bleiben offen. Nach Änderungen an Motor, Platinenbefestigung, Puffer oder Kupplungsverdrahtung die betroffenen Prüfungen wiederholen.','small')

page('21. Vergleichsfoto: Motor und Kondensatoren')
add('<b>Motorisierter Triebkopf, LoDi-Beispiel 33701.</b> Seitenblick auf das Motorschild. Zugnase links, Wagen-/Kupplungsende rechts außerhalb des Ausschnitts. Links/rechts meint ab hier das Bild, nicht die Fahrzeugseite. Der Vergleichsmotor hat bereits einen Permanentmagneten; dein 2976-Foto zeigt noch eine Feldspule. Übertragbar ist die Prüflogik nach dem 60941-Umbau, nicht der alte Verdrahtungsplan.')
story.append(MarkedPhoto(RESEARCH/'motor_a.jpg',W,[(1,.439,.279,.215,.08),(2,.641,.508,.865,.677),(3,.482,.442,.466,.805),(4,.523,.252,.620,.065)]))
photocredit('Motor vor der Entstörungsanpassung.', 'https://image.jimcdn.com/app/cms/image/transf/dimension%3D1920x400%3Aformat%3Djpg/path/s5b4f033edf99a04d/image/i4f43073273d15e4a/version/1635692007/image.jpg')
table(['Nr. / genaue Lage','Was prüfen und tun'],[
('1 - oberhalb der linken Bürste','Orange Scheibe neben der oberen linken Schraube. Beide dünnen Anschlussdrähte mit Lupe verfolgen. Im Herstellerbeispiel ist dies einer der zwei zu entfernenden Masse-Kondensatoren.'),
('2 - rechts neben dem Motorschild','Orange Scheibe zwischen Motor und Kabelbogen, nahe der braunen Leitung. Ebenfalls beide Enden verfolgen; nicht versehentlich die braune Radmasseleitung entfernen.'),
('3 - mittig zwischen den Bürsten','Orange Scheibe direkt über dem runden Lagerdeckel. Dieses Bauteil verbindet die beiden Bürstenanschlüsse miteinander. Nicht wegen seiner gleichen Farbe mit 1/2 verwechseln.'),
('4 - oberhalb der Bürsten','Beiges Bauteil mit Ringen in einer Motorleitung; daneben sitzt ein zweites. Das sind Entstördrosseln im Beispiel, keine LED-Vorwiderstände. Die Bauteilform allein reicht zur Identifikation nicht.')],[1.9,4.9])
warn('Die Handlung hängt an den Endpunkten, nicht an Farbe oder Position','Bauteil von Bürste zu Metallrahmen: im vorgesehenen Umbau entfernen. Bauteil zwischen beiden Bürsten: Quer-Kondensator. Bei verdecktem Ende erst freilegen oder prüfen lassen. Nie nach dem Foto blind Drähte abschneiden. OL kann auch trotz unerwünschtem Masse-Kondensator erscheinen.')
refs(2,6)

page('22. Vergleichsfoto: Messspitzen am Motor')
add('<b>Derselbe motorisierte Vergleichskopf, nach Entfernung der seitlichen Kondensatoren.</b> Zugnase links, Kupplungsende rechts außerhalb des Ausschnitts. Decoder und Motorplatine sind nicht angeschlossen. Die grüne/blaue Motorlitze und die braune Leitung sind rechts noch lose.')
story.append(MarkedPhoto(RESEARCH/'motor_c.jpg',W,[(1,.329,.334,.186,.075),(2,.367,.356,.555,.075),(3,.271,.328,.170,.674),(4,.433,.554,.554,.822)],170))
photocredit('Motor nach Abtrennen der alten Platine.', 'https://image.jimcdn.com/app/cms/image/transf/dimension%3D1920x400%3Aformat%3Djpg/path/s5b4f033edf99a04d/image/i228dda660533ed35/version/1635692091/image.jpg')
table(['Nummer / Position','Bedeutung'],[
('1 - oberhalb der linken Bürstenhülse','Metallische Lötfahne an der inneren Seite der linken Bürste. Hier liegt die rote Messspitze für M1 auf dem blanken Metall, nicht auf Isolierlack oder Kunststoff.'),
('2 - oberhalb der rechten Bürstenhülse','Metallische Lötfahne links oberhalb der rechten Hülse, am rechten Ende des Quer-Kondensators. Hier misst du M2. Die Messspitze darf nicht zwei Teile gleichzeitig überbrücken.'),
('3 - Schraube links oben','Metallkopf der Motorschildschraube. Nur nach Gegenprobe als Metall-Bezugspunkt verwenden; Lack oder Oxid können einen Kontakt vortäuschen bzw. verhindern.'),
('4 - Lötöse rechts unten','Befestigungs-/Lötpunkt mit brauner Leitung unterhalb der rechten Bürste. Im Beispiel Metall-/Rückleiterbereich. Nicht mit der rechten Bürstenfahne bei 2 verwechseln.')],[1.8,4.9])
h('Prüfkarte: exakt diese Reihenfolge')
add('<b>A.</b> Zug vom Gleis nehmen; Decoder und Puffer entfernen; beide Motorleitungen von übriger Elektronik trennen. Motor mechanisch montiert lassen. Multimeter: Schwarz COM, Rot V/Ω, Widerstand wählen. Null-/Offenprobe aus Abschnitt 2 machen.')
add('<b>B.</b> Am eigenen Motor zuerst zwischen 3 und 4 messen. Nur wenn ein Wert nahe dem Messleitungswiderstand erscheint, ist diese Metallverbindung bestätigt. Zusätzlich den Bezug zur tatsächlich identifizierten Radmasse prüfen. Sonst nicht mit einer scheinbar bestandenen OL-Prüfung fortfahren.')
add('<b>B2. Motorfahnen-Gegenprobe:</b> Zwischen 1 und 2 muss bei eingesetzten Bürsten nach einem möglichen Ladeeffekt ein bleibender endlicher Motorwiderstand messbar sein. Bei OL zuerst Messkontakt, Bürstensitz und Motorpfad klären. Das bestätigt die Kontaktierung beider Fahnen, nicht den vollständigen Motorzustand.')
add('<b>C.</b> Schwarz an bestätigtem Punkt 4 festklemmen. Rot zuerst an 1: stabil OL notieren. Rot abheben: weiterhin OL. Dann an 2: ebenfalls stabil OL. Danach beide Anschlüsse jeweils gegen Chassis, Motorrahmen, Radmasse und Schleifer prüfen; Gegenstellen nicht ungeprüft gleichsetzen.')
add('<b>D.</b> Messung bei mehreren Rotorstellungen und beim Ausschwenken wiederholen. Bei endlichem Wert stoppen und Abschnitt 7 abarbeiten. Zusätzlich die Kondensatorenden aus Abschnitt 21 prüfen: Ein Masse-Kondensator wird durch OL nicht ausgeschlossen.')

page('23. Vergleichsfoto: motorloser Triebkopf')
add('<b>Motorloser Kopf des LoDi-Beispiels 33701, alte Platine bereits ausgebaut.</b> Blick schräg von oben. Lampen-/Zugnasenende rechts, Kupplungsende links. Die eigentliche Nase liegt rechts außerhalb des Fotos. Die langen Leiterbahnen gehören zur alten Vergleichsplatine, nicht zu einem freigegebenen 2976-Schaltplan.')
story.append(MarkedPhoto(RESEARCH/'dummy_full.jpg',W,[(1,.949,.241,.929,.494),(2,.745,.048,.599,.079),(3,.205,.108,.136,.256),(4,.542,.787,.37,.618),(5,.076,.052,.405,.03)],310))
photocredit('Motorloser Kopf und ausgebaute Altplatine.', 'https://image.jimcdn.com/app/cms/image/transf/none/path/s5b4f033edf99a04d/image/i8a71bb7234a2f1cb/version/1635701141/image.jpg')
table(['Nr. / genaue Lage','Gefahr und sichere Vorgehensweise'],[
('1 - rechts am Lampenende','Schwarzer Lampenhalter mit Anschlussdrähten. Alte Fassung nicht elektrisch weiterverwenden. Vor Entfernen Anschlüsse fotografieren; nach LED-Einbau deren Plus/Kathoden und Halter getrennt gegen Chassis prüfen. Foto allein beweist keine Lampenmasse.'),
('2 und 3 - hohe graue Stützen','Gewindeträger rechts oben und links oben. Neue Platine zunächst ohne Decoder auflegen. Unterseite, Schraubenende, Ring und Nachbarlötstellen beobachten; dann wie Schritt 23 prüfen. Keine Halterhöhe aus dem Foto übernehmen.'),
('4 - grüne Platte unten','Ausgebaute Altplatine mit langen Leiterbahnen. Aufbewahren und beschriften. Keine Leiterbahn-Trennstelle daraus auf 2976 übertragen; die alte Platte ist im gewählten neuen Aufbau nicht der Decoderträger.'),
('5 - lose Enden links oben','Abgelötete Drähte. Solche Enden können Chassis oder einander berühren. Vor jeder Bestromung jede nicht angeschlossene Litze einzeln isolieren; nicht mehrere blanke Enden zusammen einwickeln.')],[1.8,4.9])
warn('Übertragung auf deinen Zug','Dieser Vergleich zeigt Gefahrenbereiche, keine versteckte elektrische Verbindung. Beim 2976 erst tatsächliche Schleiferleitung, Radmasse und Halter bestimmen. Bei anderer Anordnung nach Bauteil und Leitungsziel suchen, nicht nach einer Zentimeterangabe im fremden Foto.')

page('24. Prüfkarte: verdeckte Kontakte beim Schließen')
add('<b>Gilt für beide Triebköpfe.</b> Ein offenes Fahrzeug kann fehlerfrei erscheinen und erst beim Zuschrauben einen Kurzschluss bekommen. Beispiele: Schraubdom drückt eine Litze auf Metall; Dachfeder trifft einen Lötpunkt; zu lange Schraube berührt eine Leiterbahn. Diese Beispiele sind Prüfanlässe, keine aus Fotos bewiesenen Fehler deines Zuges.')
story.append(Sketch('screw',160))
h('So prüfst du ohne Spannung und ohne Decoder')
add('<b>1. Vorbereiten:</b> Fahrzeug abtrennen, beide Decoder und Puffer entfernen. Im zu messenden Pfad nötigenfalls LED-/Platinenelektronik abtrennen. Zuerst offen die Messwerte aus Abschnitt 6/14 notieren. Eine Liste mit Messpaar und Messwert anlegen, nicht nur „hat gepiept“.')
add('<b>2. Messpunkte erreichbar halten:</b> Isolierte Prüfclips nur bei abgenommenem Gehäuse am identifizierten Messpaar anbringen. Falls Prüfenden nach außen geführt werden müssen, ausschließlich eine vorhandene freie Öffnung benutzen; nicht zwischen Gehäusehälften, unter Schrauben oder neben Zahnrädern einklemmen. Ist das nicht möglich, diese Prüfung fachkundig durchführen lassen.')
add('<b>3. Schließen:</b> Kabel in ihrer vorgesehenen Endlage halten. Gehäuse ohne Druck aufsetzen und nur die zugehörigen Schrauben anziehen. Messspitzen bzw. Prüfclips dürfen ihre Lage nicht verändern. Nicht bei eingeschaltetem Gleis „vorsichtig zudrücken“.')
add('<b>4. Messen und bewegen:</b> Dieselben isoliert geprüften Messpaare erneut messen. Drehgestelle und Kupplungen langsam in ihre normalen Endlagen bewegen. M1/M2 gegen Metall müssen weiterhin offen bleiben; gewünschte passive Leitungen müssen stabil durchgängig bleiben. Bestückte Elektronik nicht nach einer pauschalen OL-Regel beurteilen.')
add('<b>5. Fehler lokalisieren:</b> Ändert sich ein Wert erst beim Schließen, wieder öffnen. Jeweils nur eine Ursache prüfen: Litzenlage, Schraube, Halter, Dachkontakt. Reparatur nur nach geklärter Ursache, dann geschlossene Prüfung wiederholen. Gehäuse nicht halb offen lassen, um den Fehler zu verstecken.')
add('<b>6. Abschließen:</b> Wieder öffnen, alle Hilfsprüfleitungen entfernen, ursprüngliche Anschlüsse gemäß geprüftem Plan herstellen. Decoder spannungsfrei einsetzen. Freiraum auch für den nun eingesetzten Decoder prüfen; die vorherige Leermessung prüft nicht dessen mechanischen Platzbedarf. Keine Isolierfolie ohne Prüfung über wärmeabgebende Bauteile wickeln.')
warn('Klare Grenze für Einsteiger','Wenn du die beiden Enden eines Bauteils, einen 21MTC-Kontakt oder einen Messwert nicht sicher zuordnen kannst: nicht weiterlöten und keine Probe unter Spannung. Detailfoto mit Markierung und Messwert anfertigen; genau diesen Arbeitsschritt prüfen lassen. Eine Schutzabschaltung ersetzt diese Prüfung nicht.')

page('Quellen und Geltungsbereich')
add('Diese Arbeitsanleitung verbindet Herstellerangaben mit daraus abgeleiteten Prüfschritten. Die schematischen Soll-/Fehlerbilder und Messfolgen sind eigene Prüfmethodik; sie sind keine Herstellerfotos der konkreten Lötpunkte. Mechanische Übertragung von 3370/33701 auf 2976 ist nur nach Passprüfung zulässig. Keine Anleitung kann unsichtbare Schäden oder unbekannte Umbauten durch Literaturprüfung ausschließen.')
add('Die bereitgestellten Fotos wurden unverändert eingebunden: die zwei alten Motoraufnahmen sowie image-2.jpg, image-4.jpg und image-5.jpg. image.jpg zeigt die gleiche sichtbare rote Platinenansicht; image-3.jpg zeigt die weiße V4.3-Platine. Nicht abgebildet sind die entscheidende Rückseite/Revision der roten Platine, der konkrete Fronteinsatz und die vollständige hintere Trägerbestückung.','small')
add('Die drei Internet-Vergleichsfotos in Abschnitten 21-23 stammen aus LoDis ausdrücklich als 33701 bezeichnetem Umbau. Originalbilddateien bleiben unverändert; nummerierte Linien liegen als separate PDF-Zeichenelemente darüber. Bildquelle und Originaldatei sind jeweils verlinkt. Das eigene rote Platinenfoto wurde ebenso markiert. Keine vollständige Baugleichheit mit 2976 wird daraus abgeleitet.','small')
for n in range(1,9):
    au,ti,meta,url=SOURCES[n]
    add(f'<b>{n}. {au}: {escape(ti)}</b><br/>{escape(meta)}.<br/><a href="{escape(url,quote=True)}" color="#354B65">Originalquelle öffnen</a>.','small')
page('Quellen und Prüfstand')
for n in range(9,17):
    au,ti,meta,url=SOURCES[n]
    add(f'<b>{n}. {au}: {escape(ti)}</b><br/>{escape(meta)}.<br/><a href="{escape(url,quote=True)}" color="#354B65">Originalquelle öffnen</a>.','small')
h('Abgleich und verbleibende Freigaben')
add('Dokumentstand: 10. September 2026. Unabhängig gegengeprüft wurden Decoder-/Bremsarchitektur, elektrische Einbaugefahren und Pufferanbindung. Das ist eine Literatur- und Konzeptprüfung, keine dreifache Hardwareprüfung. Die Bildprüfung darf nicht als Messung am vorhandenen Zug interpretiert werden.')
add('Für 21MTC wird die Kontaktzuordnung der Tabelle 1 der RCN-121 mit Decoderunterlagen abgeglichen. Generische Normbelegung und herstellerspezifische MKL-Ausgänge sind zu unterscheiden. Aus einer Normpin-Nummer folgt ohne Index-/Ansichtsprüfung keine sichere Position im Foto.')
warn('Verbindlicher Abschluss','Vor einer vollständigen elektrischen Freigabe müssen insbesondere die Rückseite/Revision der Motorplatine, der hintere LED-Aufbau und der konkrete 60974-Anschluss ergänzt werden. Die jeweilige Warnstelle bleibt bis dahin gültig. Keine alten Schaltpläne oder Leiterbahn-Trennanweisungen parallel zu dieser Revision anwenden.')

def foot(c,doc):
    c.saveState();c.setFont('A',8);c.setFillColor(MUTED);c.drawRightString(A4[0]-42,24,str(doc.page));c.restoreState()
class ManualDoc(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable,Paragraph) and flowable.style.name=='h1':
            key='section-'+str(self.page)
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.getPlainText(),key,level=0,closed=False)
doc=ManualDoc(str(OUT),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=40,bottomMargin=40,title='ICE 2976: Umbauanleitung REV5',author='Sicherheitsgeführte Arbeitsanleitung',subject='Märklin 2976 - Motorisolation, mfx-Sound, LoDi, ESU 59649, Prüfungen')
doc.build(story,onFirstPage=foot,onLaterPages=foot)
print(OUT)
print('Abschnitte:',len(sections))
