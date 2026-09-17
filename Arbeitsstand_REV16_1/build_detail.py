from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader,PdfWriter
import json,hashlib
ROOT=Path(__file__).resolve().parent.parent
TMP=ROOT/'tmp/pdfs/rev16_1/details.pdf'
OUT=ROOT/'output/pdf/ICE_2976_REV16_1_MFX_MIT_PLATINENDETAILS.pdf'
C=canvas.Canvas(str(TMP),pagesize=(595.28,841.89))
NAV=HexColor('#17354B'); TEAL=HexColor('#087F86'); RED=HexColor('#B4343C'); LIGHT=HexColor('#EAF2F5'); GREY=HexColor('#92AAB6')
body=ParagraphStyle('body',fontName='Helvetica',fontSize=10,leading=13,textColor=NAV)
small=ParagraphStyle('small',fontName='Helvetica',fontSize=8.4,leading=10.5,textColor=NAV)
def text(x,y,t,size=10,color=NAV,bold=False):
 C.setFont('Helvetica-Bold' if bold else 'Helvetica',size);C.setFillColor(color);C.drawString(x,y,t)
def para(x,y,t,w=487,sm=False):
 p=Paragraph(t,small if sm else body);_,h=p.wrap(w,800);p.drawOn(C,x,y-h);return y-h-8
def table(x,y,heads,rows,widths):
 vals=[[Paragraph(str(t),small) for t in r] for r in [heads]+rows]
 tb=Table(vals,colWidths=widths);tb.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),LIGHT),('GRID',(0,0),(-1,-1),.35,GREY),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]));_,hh=tb.wrap(sum(widths),800);tb.drawOn(C,x,y-hh);return y-hh-8
def header(n,t,sub):
 text(54,795,f'REV16.1 / DETAILSEITE {n}',9,TEAL,True);text(54,763,t,21,NAV,True);para(54,743,sub)
 C.setStrokeColor(TEAL);C.line(54,42,541,42);text(54,29,'ICE 2976 | REV16.1 | Platinen- und Lötpunktdetails',8);text(527,29,str(n),8)
def picture(path,x,y,w,h,crop=None):
 """Clip the unchanged source image inside PDF; no synthesis or raster retouching."""
 src=ImageReader(str(ROOT/path));iw,ih=src.getSize()
 if not crop: crop=(0,0,iw,ih)
 l,t,r,b=crop;f=min(w/(r-l),h/(b-t));dw=(r-l)*f;dh=(b-t)*f
 C.saveState();clip=C.beginPath();clip.rect(x,y-dh,dw,dh);C.clipPath(clip,stroke=0)
 C.drawImage(src,x-l*f,y-dh-(ih-b)*f,width=iw*f,height=ih*f)
 C.restoreState();return dw,dh
def ring(x,y,label):
 C.setStrokeColor(RED);C.setFillColor(white);C.circle(x,y,8,fill=1);text(x-3,y-3,label,8,RED,True)
def line(x,y,xx,yy,col=TEAL):C.setStrokeColor(col);C.setLineWidth(1.4);C.line(x,y,xx,yy)

header(17,'Originalplatine: keine Schnitte','Konkretisierung zu Seite 3: Die alte Platine wird in dieser Ausführung nur mechanisch genutzt. Ihre Leiterzüge werden nicht als neue elektrische Verteiler verwendet.')
picture(Path('Arbeitsstand_Originalplatine/belege_62762/ebay_147416253187_bild2.webp'),66,685,190,430,(805,10,1090,1000))
picture(Path('Arbeitsstand_Originalplatine/belege_62762/ebay_147416253187_bild1.webp'),320,685,190,430,(880,45,1165,1080))
text(57,239,'Leiterzug-/Lötseite, 62762',10,TEAL,True);text(311,239,'Gegenseite mit Schiebeschalter',10,TEAL,True)
para(54,222,'Beide Aufnahmen zeigen dasselbe fremde Vergleichspaar: jeweils die rechte Platine 62762. Die danebenliegende bestückte 62761 wurde ausgeblendet. Kein Foto des eigenen fertig umgebauten ICE. Quelle: archivierte Bilder des Angebots ebay.de/itm/147416253187.',sm=True)
y=table(54,175,['Arbeit','Konkrete Ausführung'],[
['Durchtrennen','Keine Leiterbahn schneiden. Keine Schalterkontakte überbrücken.'],
['Ablöten','Vorher jedes Kabel bis zum Verbraucher verfolgen und beschriften. Danach sämtliche externen elektrischen Leitungen der jeweiligen alten Kopfplatine lösen; Enden einzeln isolieren.'],
['Neu verbinden','Schleifer, Radmasse, Motor und Frontlicht direkt nach Seiten 5-9 anschließen. Neue Träger/Adapter gegen das gesamte alte Kupfer isolieren.'],
],[100,387])
assert y>50,y
C.showPage()

header(18,'60972: wo die neuen Leitungen hinführen','Vergrößerte Herstellerzeichnung des mitgelieferten Trägers. Nur die beschrifteten Anschlüsse verwenden. Am 60972-Träger und an den LoDi-514 sind keine Leiterbahnschnitte vorgesehen.')
picture(Path('Arbeitsstand_Originalplatine/maerklin_60972_p6.png'),70,679,448,348,(140,410,1040,1130))
y=table(54,315,['Aufdruck / Märklin-Farbe','Neues Ziel'],[
['B/G rechts - rot','Vorderer Mittelschleifer.'],['0/G links - braun','Örtliche Rad-/Chassismasse.'],['MV grün / MR blau','Jeweils über eine Motordrossel zu den isolierten Bürsten des 60941.'],['+Ub orange (= U+)','VCC der vorderen LoDi-514 und U-Punkt des Senderadapters. Nicht GND oder +5V verwenden.'],['LV grau / LR gelb','Je eigener 47-kOhm-Widerstand zu white / red der vorderen LoDi-514.'],['AUX1 braun/rot','X1-Punkt des Senderadapters.'],['AUX2 braun/grün','X2-Punkt des Senderadapters.'],['GND, +5V, AUX3/4, SUSI','Für diese Schaltung ohne Anschluss.']],[181,306])
y=para(54,y,'Quelle: Märklin 60972/60982, Herstelleranleitung, Anschlussbild Seite 6. Bild ist ein unveränderter Ausschnitt. Vor dem Löten den Decoder abziehen; vorhandene Litzen können statt der Pads benutzt werden.',sm=True)
assert y>46,y
C.showPage()

def board(x,top,cols,rows,pitch=19):
 w=(cols-1)*pitch;h=(rows-1)*pitch
 C.setFillColor(LIGHT);C.setStrokeColor(GREY);C.roundRect(x-13,top-h-14,w+26,h+28,5,fill=1)
 for col in range(cols):text(x+col*pitch-3,top+21,chr(65+col),8,NAV)
 for row in range(rows):
  text(x-31,top-row*pitch-3,str(row+1),8,NAV)
  for col in range(cols):
   C.setStrokeColor(GREY);C.setFillColor(white);C.circle(x+col*pitch,top-row*pitch,2.1,fill=1)
 def pt(addr):return x+(ord(addr[0])-65)*pitch,top-(int(addr[1:])-1)*pitch
 return pt
def component(pt,a,b,name,diode=False):
 x,y=pt(a);xx,yy=pt(b);line(x,y,xx,yy)
 C.setFillColor(white);C.setStrokeColor(NAV);C.rect(x+14,y-5,xx-x-28,10,fill=1)
 if diode:line(xx-19,y-5,xx-19,y+5,RED)
 text(x+17,y+10,name,8,NAV,True)
 for u,v in [(x,y),(xx,yy)]: C.setFillColor(TEAL);C.circle(u,v,3,fill=1)
def jumper(pt,a,b,col=RED):
 x,y=pt(a);xx,yy=pt(b);line(x,y,xx,yy,col)
 for u,v in [(x,y),(xx,yy)]:C.setFillColor(col);C.circle(u,v,3,fill=1)

header(19,'Sender: nummerierte Lötpunkte','Eigener Montagevorschlag auf Einzellötaugenraster, Rastermaß 2,54 mm. Jedes Lötauge ist einzeln isoliert. KEIN Streifenraster verwenden: Der Plan sieht keinerlei Kupferschnitte vor.')
pt=board(85,666,10,11,19)
component(pt,'B3','F3','RP1 4,7 k');component(pt,'F3','J3','RS1 1 k')
component(pt,'B9','F9','RP2 4,7 k');component(pt,'F9','J9','RS2 1 k')
jumper(pt,'B3','B9')
text(320,656,'Ansicht: Bauteilseite',12,TEAL,True)
para(320,636,'RP1/RP2: 0,5 W<br/>RS1/RS2: 1 W<br/><br/>Kupferseite beim Löten spiegelverkehrt: Koordinaten vorher auf den Rand schreiben.<br/><br/>Farbige Verbindung = isolierte Drahtbrücke. Kontakt entsteht nur am markierten Endpunkt.',w=209)
y=table(54,409,['Punkt','Anschluss / Drahtbrücke'],[
['B3 = U','U+ orange vom 60972. B3 mit B9 durch isolierten Draht verbinden.'],['F3 = X1','AUX1 braun/rot vom 60972. Gemeinsamer Lötpunkt von RP1 und RS1.'],['J3 = K1','Zum durchgehenden Kupplungspol K1.'],['F9 = X2','AUX2 braun/grün vom 60972. Gemeinsamer Lötpunkt von RP2 und RS2.'],['J9 = K2','Zum durchgehenden Kupplungspol K2.']],[99,388])
y=para(54,y,'<b>Montage:</b> Erst Bauteilgehäuse trocken auflegen. Vier Lochabstände entsprechen 10,16 mm Anschlussabstand; passt ein gekauftes Gehäuse nicht, mehr Rasterabstand vorsehen und die gleichen elektrischen Netze beibehalten. Keine Bauteile oder Lötstellen gegen die Originalplatine drücken.')
y=para(54,y,'<b>Prüfung ohne Decoder/Kupplungen:</b> U gegen X1 und X2 jeweils etwa 4,7 kOhm; X1 gegen K1 sowie X2 gegen K2 jeweils etwa 1 kOhm. B3 gegen B9 direkter Durchgang. Andere indirekte Widerstandspfade sind durch die Schaltung möglich; keine pauschale Offenprüfung des bestückten Adapters.',sm=True)
assert y>48,y
C.showPage()

header(20,'Empfänger: Ringseiten und Lötpunkte','Eigener Montagevorschlag, Bauteilseite eines Einzellötaugenrasters. Der rote Strich am Diodengehäuse im Plan bezeichnet dessen tatsächlichen Kathodenring. Der hintere Adapter hat keinen Gleisanschluss.')
pt=board(85,665,10,15,16.5)
component(pt,'B3','F3','D1',True);component(pt,'B7','F7','D2',True)
component(pt,'B11','F11','RR 47 k');component(pt,'B15','F15','RW 47 k')
component(pt,'F11','J11','D3',True);component(pt,'F15','J15','D4',True)
text(313,652,'Brücken separat verdrahten',12,TEAL,True)
para(313,633,'K1: B3 mit B11<br/>K2: B7 mit B15<br/>P: F3, F7, J11, J15 verbinden<br/><br/>Alle Brücken mit isolierter Litze legen. Zwischenliegende oder gekreuzte Lötaugen nicht anschließen.<br/><br/>Keine Kupferstreifen und keine Verbindung zum Fahrwerk.',w=218)
y=table(54,397,['Bauteil / Außenleitung','Lötpunkte'],[
['D1 / D2 - 1N4148','D1 B3-F3, Ring F3. D2 B7-F7, Ring F7.'],['RR / RW - 47 kOhm','RR B11-F11. RW B15-F15. Je 0,25 W.'],['D3 / D4 - 1N4148','D3 F11-J11, Ring J11. D4 F15-J15, Ring J15.'],['Kupplung K1 / K2','K1 an B3. K2 an B7.'],['LoDi-514 VCC','An das gemeinsame P-Netz, z. B. J11.'],['LoDi-514 red / white','red an F11. white an F15.']],[194,293])
y=para(54,y,'<b>Prüfung:</b> Alle vier Ringseiten müssen direkten Durchgang miteinander haben. B3-B11 und B7-B15 ebenfalls. Jeden Widerstand vor Einbau nachmessen. Den LED-/Diodentest nicht aus einer beliebigen Widerstandsmessung des bestückten Adapters ableiten. Versorgung und Funktion stufenweise nach Seite 14 prüfen.')
y=para(54,y,'<b>Eigene Originalplatinen:</b> Für fotoexakte Ablötmarkierungen werden pro Kopf eine scharfe Gesamtaufnahme beider Platinenseiten und Nahaufnahmen der angeschlossenen Kabel benötigt. Die alten Fotos zeigen verdeckte Endpunkte und zu wenig Detail. Die Netzliste dieses Adapters ist eindeutig; eine unbekannte Altplatinen-Padbelegung wird daraus nicht erfunden.',sm=True)
assert y>48,y
C.showPage();C.save()

# Netlist check of the new physical pad plans, independently of the visual positions.
sender={'RP1':('U','X1',4700),'RP2':('U','X2',4700),'RS1':('X1','K1',1000),'RS2':('X2','K2',1000)}
receiver={'D1':('K1','P'),'D2':('K2','P'),'RR':('K1','red',47000),'RW':('K2','white',47000),'D3':('red','P'),'D4':('white','P')}
assert sender['RP1'][1]==sender['RS1'][0] and sender['RP2'][1]==sender['RS2'][0]
assert all(receiver[k][1]=='P' for k in ['D1','D2','D3','D4'])
w=PdfWriter();w.append(str(ROOT/'output/pdf/ICE_2976_REV16_MFX_EIN_DECODER_KUPPLUNGSLICHT.pdf'));w.append(str(TMP))
w.add_metadata({'/Title':'ICE 2976 REV16.1 - mit Platinen- und Lötpunktdetails'})
with OUT.open('wb') as f:w.write(f)
r=PdfReader(OUT);assert len(r.pages)==20
report={'output':str(OUT),'pages':20,'cuts_required':0,'source_photo_mapping':'62762 foreign specimen only; own exact wire endpoint mapping remains unknown','pad_netlists':{'sender':sender,'receiver':receiver},'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()}
(Path(__file__).parent/'build_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps(report,ensure_ascii=False))
