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

