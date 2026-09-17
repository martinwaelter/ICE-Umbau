from legacy_diagrams import Diagram as Base
from reportlab.lib import colors
class Diagram(Base):
 def draw(self):
  if self.kind not in ['system','front','rear','led','relay','current_probe']:
   return super().draw()
  c=self.canv;w=self.width;h=self.height
  teal=colors.HexColor('#145B64');red=colors.HexColor('#9D2923');ink=colors.HexColor('#182D38');grey=colors.HexColor('#65757D')
  c.saveState();c.scale(w/520,h/200)
  def txt(x,y,t,size=10,col=ink,bold=False):
   c.saveState();c.translate(x,y);c.scale(1,(w/520)/(h/200));c.setFillColor(col);c.setFont('Bold' if bold else 'Body',size);c.drawString(0,0,t);c.restoreState()
  def line(x,y,xx,yy,col=ink,dash=False):
   c.setStrokeColor(col);c.setLineWidth(1.5);c.setDash(4,3) if dash else c.setDash();c.line(x,y,xx,yy);c.setDash()
  def box(x,y,ww,hh,labels,col=teal):
   c.setStrokeColor(col);c.setFillColor(colors.HexColor('#F1F6F6'));c.roundRect(x,y,ww,hh,5,stroke=1,fill=1)
   for i,t in enumerate(labels.split('|')):txt(x+8,y+hh-18-i*18,t,10,col,i==0)
  def cross(x,y):line(x-5,y-5,x+5,y+5,red);line(x-5,y+5,x+5,y-5,red)
  if self.kind=='system':
   box(2,75,154,110,'VORN: 60977|62762 + Märklin-Träger|60941-Motor + Sound|AUX1 steuert Relais')
   box(192,75,132,110,'WAGEN: LoDi ICE-M|B = RT / L = GE|O = örtliche Räder|Massefedern nötig')
   box(360,75,157,110,'HINTEN: 59649|Träger aus 60972|Rot / Weiß mit R|Alter Schleifer isoliert')
   line(156,145,192,145,red);line(324,145,360,145,red);txt(162,155,'RT',9,red);txt(334,155,'RT',9,red)
   line(156,100,192,100,teal);line(324,100,345,100,teal);cross(350,100);txt(162,110,'GE',9,teal)
   txt(3,45,'Nur der vordere Schleifer speist RT. Motorstrom bleibt im Motorkopf.',10,red,True)
   txt(3,15,'Die alte 62762 trägt den Aufbau; neue Anschlüsse bleiben elektrisch unabhängig.',10,ink)
  elif self.kind=='front':
   box(173,13,170,180,'60977-Träger|Beschriftete Leitungen')
   for y,label,pad in [(137,'Schleifer + RT','B/GR'),(105,'Örtliche Räder','0/GL'),(71,'Motor + Drosseln','MV / MR'),(35,'Relais-Steuereingang','AUX1')]:
    txt(2,y+8,label,9.5);line(2,y-3,173,y-3);txt(181,y-7,pad,10,teal,True)
   for y,label,pad in [(139,'LED-Plus / Relais +','+Ub'),(105,'R - Weiß','LV'),(71,'R - Rot','LR'),(35,'Satzlautsprecher','LS')]:
    txt(305,y+6,pad,10,teal,True);line(343,y,366,y,teal);txt(371,y-4,label,9.4)
  elif self.kind=='rear':
   box(183,10,158,182,'Träger aus 60972|ESU 59649 hinten')
   txt(2,142,'Kupplung RT',10);line(2,129,183,129,red);txt(193,125,'B/GR',10,red,True)
   txt(2,95,'Örtlicher Radkontakt',10);line(2,82,183,82,grey);txt(193,78,'0/GL',10,grey,True)
   txt(2,46,'Schleifer und GE:',10,red);txt(2,25,'jeweils einzeln isoliert',10,red)
   for y,pad,label in [(135,'+Ub','LED-Plus'),(93,'LV','R Rot - LED Rot'),(51,'LR','R Weiß - LED Weiß')]:
    txt(279,y+6,pad,10,teal,True);line(341,y,366,y,teal);txt(371,y-4,label,9.6)
  elif self.kind=='led':
   box(2,66,82,107,'EIN Kopf|+Ub')
   box(425,66,92,107,'Ausgang')
   for y,col,pad in [(132,'Weiß','LV / LR'),(89,'Rot','LR / LV')]:
    line(84,y,114,y,teal);box(114,y-15,93,30,'LED '+col);line(207,y,235,y);box(235,y-15,156,30,'47 kOhm je Zweig');line(391,y,425,y);txt(435,y-5,pad,10,teal,True)
   txt(2,40,'Vorn Weiß an LV; hinten Rot an LV. Jeder Kopf hat sein eigenes +Ub.',10)
   txt(2,13,'Vier Widerstände insgesamt. 47 kOhm ist der konservative Startwert.',10,red,True)
  elif self.kind=='relay':
   box(8,99,126,84,'60977|+Ub / orange|AUX1 / braun-rot')
   box(229,99,121,84,'RELAISMODUL|Spule + / -|mit Schutzdiode')
   line(134,147,229,147,teal);txt(169,158,'+',11,teal,True)
   line(134,117,229,117,teal);txt(169,123,'-',11,teal,True)
   txt(384,149,'Steuerkreis',10,teal,True);txt(376,121,'Kein GE am AUX',10,red)
   line(33,51,213,51,red);txt(6,64,'RT / B-Zug',10,red,True)
   line(213,51,272,74,red);line(282,51,482,51,red);txt(383,64,'GE / L-Zug',10,red,True)
   line(267,99,267,82,grey,True);txt(167,27,'COM',9);txt(278,27,'NO',9)
   txt(7,6,'Potentialfreier Kontakt: RT wird auf GE geschaltet; O der Wagen führt zu den Rädern.',9.8)
  elif self.kind=='current_probe':
   box(3,94,144,90,'AUX1-STEUERKREIS|nur Relaisspule|plus eigene Front-LEDs')
   box(199,94,134,90,'RELAISKONTAKT|RT -> GE|Wagenstrom separat')
   box(382,94,136,90,'WAGEN|B / L vom Bus|O über Radkontakte')
   line(147,133,199,133,teal);line(333,133,382,133,red)
   txt(3,59,'DC-Messung an der Spule: 10-24 V im eingeschalteten Zustand.',10)
   txt(3,31,'Digitaler Wagenstrom braucht einen dafür geeigneten Messbereich.',10)
   txt(3,7,'Keine pauschale Wagenzahl aus einem DC-Mittelwert oder aus „kein Kurzschluss“.',9.8,red)
  c.restoreState()
