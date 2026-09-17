from reportlab.platypus import Flowable, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle

class Diagram(Flowable):
 def __init__(self,kind,width,height=180):
  super().__init__();self.kind=kind;self.width=width;self.height=height
 def draw(self):
  c=self.canv;w=self.width;h=self.height
  ink=colors.HexColor('#182D38');teal=colors.HexColor('#145B64');red=colors.HexColor('#9D2923');grey=colors.HexColor('#65757D')
  c.saveState();c.scale(w/520,h/200)
  def txt(x,y,t,size=10,col=ink,bold=False):
   c.saveState();c.translate(x,y);c.scale(1,(w/520)/(h/200));c.setFillColor(col);c.setFont('Bold' if bold else 'Body',size);c.drawString(0,0,t);c.restoreState()
  def line(x,y,xx,yy,col=ink,dash=False):
   c.setStrokeColor(col);c.setLineWidth(1.5);c.setDash(4,3) if dash else c.setDash();c.line(x,y,xx,yy);c.setDash()
  def box(x,y,ww,hh,labels,col=teal):
   c.setStrokeColor(col);c.setFillColor(colors.HexColor('#F1F6F6'));c.roundRect(x,y,ww,hh,5,stroke=1,fill=1)
   for i,t in enumerate(labels.split('|')):txt(x+8,y+hh-18-i*15,t,10,col,i==0)
  def dot(x,y,col=ink):c.setFillColor(col);c.circle(x,y,2.8,stroke=0,fill=1)
  def cross(x,y):line(x-5,y-5,x+5,y+5,red);line(x-5,y+5,x+5,y-5,red)
  if self.kind=='system':
   box(2,63,149,105,'MOTORKOPF|60941 + 60977|LoDi 512 ICE-M-S|Weiß / Rot + Sound')
   box(185,63,144,105,'WAGEN W1...Wn|je 1x LoDi-510|O = RT   L = GE|Innenlicht')
   box(363,63,155,105,'MOTORLOSER KOPF|60972 + Märklin-Träger|Rot / Weiß|GE endet isoliert')
   line(151,135,185,135,red);line(329,135,363,135,red);txt(158,145,'RT',9,red);txt(337,145,'RT',9,red)
   line(151,85,185,85,teal);line(329,85,348,85,teal);cross(352,85);txt(158,95,'GE',9,teal)
   line(45,63,45,31,red);line(465,63,465,31,red);line(45,31,465,31,red)
   txt(73,12,'Beide Schleifer parallel: ein gemeinsamer Digitalstromkreis',10,red,True)
   txt(2,182,'ZIEL: ein mfx-Zugeintrag, Innenlicht aus 60977-AUX4',11,teal,True)
  elif self.kind=='nets':
   for xx,ww,labels in [(4,110,['GLEIS','B: Schleifer','0: Räder']),(174,169,['EIN DECODER','U+ / GND intern','LV / LR: geschaltet']),(405,110,['FRONT-LED','U+ / Plus','Lichtausgang'])]:
    box(xx,72,ww,111,'')
    for i,label in enumerate(labels):txt(xx+8,161-i*29,label,10,teal,i==0)
   line(114,143,174,143,red);line(114,99,174,99,grey)
   line(343,143,405,143,teal);line(343,99,405,99,ink)
   txt(5,35,'B, 0, U+ und GND getrennt benennen. Kabelfarbe allein genügt nicht.',10,ink,True)
   txt(5,7,'Kein U+ / GND an Chassis; kein U+ zwischen beiden Decodern verbinden.',10,red)
  elif self.kind=='fixture':
   box(5,115,135,65,'EINE QUELLE|CS3-Ausgang|B und 0')
   box(220,119,292,61,'EINZELAUFNAHME|Passender Decoder, Lasten und Orientierung')
   line(140,153,220,153,red);line(140,132,220,132,grey)
   box(220,17,292,67,'PAARTEST: ZWEI GETRENNTE AUFNAHMEN|Eigene Lasten je Decoder, gleiche Quelle|Kein U+ / AUX / Motor-Ausgang gemeinsam')
   line(154,121,154,53,teal,True);line(154,53,220,53,teal,True)
   txt(5,77,'Quelle umstecken:',10,ink,True);txt(5,58,'vorher ausschalten',10);txt(5,39,'und vollständig trennen.',10)
  elif self.kind=='motor':
   box(5,65,109,94,'60941|M1: Bürste|M2: Bürste')
   box(407,65,109,94,'LoDi 512|MOT_L|MOT_R')
   for yy,label in [(123,'Drossel 1'),(90,'Drossel 2')]:
    line(114,yy,175,yy);box(175,yy-13,100,26,label);line(275,yy,395,yy);cross(398,yy)
   txt(289,145,'Motorlitzen jetzt frei',10,red,True)
   txt(5,34,'Jede Drossel in einen eigenen Zweig; alle Blankstellen einzeln isolieren.',10)
   txt(5,12,'An LoDi erst nach Motorprüfung und Padzuordnung anschließen.',10,red,True)
  elif self.kind=='front':
   box(180,5,166,190,'LoDi 512|60977 erst später')
   left=[('Schleifer','SW',158),('Radkontakt','MASSE',127),('Motor über Drosseln','MOT_L / MOT_R',91),('Kupplung RT / GE','RT / GE',45)]
   for label,pad,y in left:
    txt(3,y+6,label,10);line(15,y-5,180,y-5);txt(188,y-9,pad,9.2,teal,True)
   for label,pad,y in [('LED-Plus','Front-VCC',153),('LED Weiß','L_WS',119),('LED Rot','L_RT',85),('Lautsprecher','LS1 / LS2',40)]:
    txt(278,y-4,pad,9.2,teal,True);line(346,y,371,y);txt(376,y-4,label,10)
  elif self.kind=='rear':
   box(205,4,137,191,'Märklin-Träger|60972 hinten')
   txt(2,153,'Eigener Schleifer S',10);txt(2,118,'Kupplung RT',10)
   line(4,141,180,141,red);line(4,106,160,106,red);line(160,106,160,141,red);dot(160,141,red);line(180,141,205,141,red);txt(214,137,'B/GR',10,red,True)
   txt(2,76,'Eigener Radkontakt R',10);line(4,64,205,64,grey);txt(214,60,'0/GL',10,grey,True)
   txt(2,24,'Kupplung GE',10,teal);line(95,21,174,21,teal);cross(181,21);txt(109,5,'einzeln isolieren',9,red)
   for y,pad,label in [(141,'+Ub','LED-Plus'),(96,'LV','R Rot - LED Rot'),(51,'LR','R Weiß - LED Weiß')]:
    txt(280,y+6,pad,10,teal,True);line(342,y,369,y,teal);txt(375,y-4,label,10)
  elif self.kind=='led':
   box(2,70,82,97,'');txt(10,143,'60972',10,teal,True);txt(10,114,'+Ub',10,teal)
   box(425,70,92,97,'');txt(425,185,'60972',10,teal,True)
   for y,col,pad in [(140,'Rot','LV'),(92,'Weiß','LR')]:
    line(84,y,127,y,teal);box(127,y-15,91,29,'LED '+col);line(218,y,252,y);box(252,y-15,111,29,'R '+col+' separat');line(363,y,425,y);txt(468,y-6,pad,10,teal,True)
   txt(2,40,'Zwei Farbzweige, zwei eigene Widerstände. Plus bleibt am selben Decoder.',10)
   txt(2,16,'Dimmung ersetzt keine sichere Strombegrenzung.',10,red,True)
  elif self.kind=='coupler':
   box(5,71,115,106,'ENDE 1|Kontakt -> Litze|RT-1 / GE-1')
   box(397,71,118,106,'ENDE 2|Kontakt -> Litze|RT-2 / GE-2')
   line(120,147,397,147,red);txt(178,158,'RT-1 zu RT-2: leitend',10,red)
   line(120,95,397,95,teal);txt(178,78,'GE-1 zu GE-2: leitend',10,teal)
   line(150,147,370,95,grey,True);line(150,95,370,147,grey,True)
   txt(6,45,'Kreuzpfade: offen - nur am vollständig passiven, abgetrennten Abschnitt.',10,ink,True)
   txt(6,23,'Vor und nachher beide gewünschten Durchleitungen positiv kontrollieren.',10)
   txt(6,4,'Gestrichelt: Messpaare, keine zusätzlichen Drahtverbindungen.',9,grey)
  elif self.kind=='ammeter':
   box(4,80,99,81,'QUELLE|ein Ausgang')
   box(162,80,114,81,'A-METER|abgesicherter|Stromeingang')
   box(356,80,159,81,'LAST|Stufe vorher festlegen')
   line(103,131,162,131,red);line(276,131,356,131,red)
   line(51,80,51,42,grey);line(51,42,430,42,grey);line(430,42,430,80,grey)
   txt(5,17,'Nur in Reihe. Niemals A/mA direkt zwischen B und 0: Kurzschluss.',10,red,True)
  elif self.kind=='screw':
   for xx,lab,bad in [(7,'SOLL: freier Abstand',False),(276,'FEHLER: Metallkontakt',True)]:
    txt(xx,181,lab,11,red if bad else teal,True)
    c.setFillColor(colors.HexColor('#E6ECEE'));c.rect(xx+8,97,218,15,fill=1,stroke=0)
    line(xx+48,155,xx+48,42);line(xx+31,150,xx+65,150)
    line(xx+9,42,xx+226,42,grey);txt(xx+112,22,'Chassis',10,grey)
    line(xx+(48 if bad else 78),113,xx+211,113,red if bad else teal)
    txt(xx+80,132,'Signal-Kupfer',10)
    if bad:cross(xx+48,113)
    else:txt(xx+82,72,'Halter / Isolation',10)
  elif self.kind=='phases':
   for i,(a,b) in enumerate([('1','Belegen'),('2','Montieren'),('3','Messen'),('4','Einsetzen'),('5','Testen')]):
    x=3+i*104;box(x,75,95,58,a+' |'+b)
    if i<4:line(x+95,102,x+103,102)
   txt(4,43,'Eine offene Angabe stoppt den zugehörigen Anschluss oder Test.',10,red,True)
   txt(4,22,'Vorbereitung und eindeutig beschriebene unabhängige Arbeiten können weitergehen.',10)
  elif self.kind=='district':
   box(2,69,219,79,'BEREICH A|eine bestätigte CS3-Quelle|hier bleibt der ganze Zug')
   box(305,69,213,79,'BEREICH B|andere / unbekannte Einspeisung|oder Schalt-/Bremsabschnitt')
   line(258,42,258,175,red,True);cross(258,98)
   txt(210,183,'GRENZE',10,red,True)
   line(79,58,438,58,red);line(79,58,79,79,red);line(438,58,438,79,red)
   txt(128,28,'RT würde beide Schleifer und damit die Grenze verbinden.',10,red,True)
   txt(2,6,'Nur Funktionsprinzip. Die eigene Trennstelle wird im Anlagenplan zugeordnet.',9,grey)
  elif self.kind=='led_measure':
   box(2,96,94,70,'+Ub|LED-Plus')
   box(132,107,94,43,'LED-Zweig')
   box(294,107,82,43,'R separat')
   box(427,96,90,70,'LV / LR|aktiv ein')
   line(96,128,132,128,teal);line(226,128,294,128,teal);line(376,128,427,128,teal)
   line(271,128,271,63,red);line(395,128,395,63,grey);line(271,63,301,63,red);line(369,63,395,63,grey)
   box(301,43,68,41,'V DC');txt(263,34,'Rot',9,red);txt(391,34,'COM',9,grey)
   txt(3,185,'SPANNUNG: parallel über dem zugänglichen Widerstand messen',10,teal,True)
   txt(3,10,'I_mittel = U_R / R. Amperemeter wäre in Reihe; niemals hier parallel einsetzen.',9.6,red)
  elif self.kind=='current_probe':
   box(3,95,143,74,'LoDi-Motorseite|GE: isolierte Litze')
   box(377,95,140,74,'Wagenkette|O = RT, L = GE')
   line(146,129,377,129,teal)
   c.setStrokeColor(red);c.setLineWidth(3);c.ellipse(239,102,275,157,stroke=1,fill=0)
   line(258,103,258,74,red);line(258,74,117,74,red)
   box(4,34,160,48,'DC-Stromsonde|+ Speicheroszilloskop')
   txt(292,89,'Genau eine Ader',10,red,True)
   txt(4,10,'Kein elektrischer Masseanschluss am Gleis. Offset, Peak und RMS erfassen.',10,red)
  elif self.kind=='closed_access':
   c.setStrokeColor(grey);c.setLineWidth(1);c.rect(3,41,275,137,stroke=1,fill=0)
   txt(5,185,'ENDZUSTAND: GEHÄUSE ZU',10,teal,True)
   box(12,116,224,44,'Motor + Drosseln')
   box(12,54,224,44,'LoDi / Decoder')
   line(236,141,340,141,teal);line(236,125,340,125,teal)
   line(236,78,468,78,grey);line(468,78,468,125,grey);line(405,125,468,125,grey)
   line(236,60,491,60,grey);line(491,60,491,141,grey);line(405,141,491,141,grey)
   c.setStrokeColor(teal);c.rect(340,111,25,44,stroke=1,fill=0)
   c.setStrokeColor(grey);c.rect(380,111,25,44,stroke=1,fill=0)
   dot(352,141,teal);dot(352,125,teal);dot(392,141,grey);dot(392,125,grey)
   txt(308,179,'PM1 / PM2: Motorhälfte',10,teal,True)
   txt(325,94,'Service offen',10,red,True)
   txt(4,8,'Danach nur außen verbinden; Gehäuse und Innenleitungen unverändert lassen.',10,red)
  elif self.kind=='testtrack':
   txt(4,182,'GENAU EIN KABEL - IM BILD AM BETRIEBSAUSGANG',10,teal,True)
   box(4,111,176,44,'PROG: Lesen / Erstkontrolle')
   box(4,35,176,44,'BETRIEB: Funktion / Last')
   box(341,78,176,54,'FREIER PRÜFABSCHNITT')
   line(180,58,258,58,red);line(258,58,258,108,red);line(258,108,341,108,red)
   line(180,42,278,42,grey);line(278,42,278,91,grey);line(278,91,341,91,grey)
   txt(295,118,'B',9,red);txt(295,65,'0',9,grey)
   txt(4,7,'Vor Umstecken STOP; Stecker ganz abziehen. Keine Verbindung zur Anlage.',10,red)
  else:raise ValueError(self.kind)
  c.restoreState()
