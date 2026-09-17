from pathlib import Path
import json, hashlib
from xml.sax.saxutils import escape
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT

BASE = Path('/Users/martinwaelter/ICE Umbau')
WORK = BASE / 'Arbeitsstand_Originalplatine'
EVID = WORK / 'belege_62762'
OUT = BASE / 'output/pdf/ICE_2976_Originalplatine_62762_Bildbefund_und_Umbaugrundlage.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
for name, file in [('Arial','Arial.ttf'),('ArialB','Arial Bold.ttf'),('ArialI','Arial Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/System/Library/Fonts/Supplemental/'+file))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='ArialB',italic='ArialI',boldItalic='ArialB')
W,H=595.276,841.89
M=43
CW=W-2*M
INK=HexColor('#202020'); GREY=HexColor('#555555'); TEAL=HexColor('#135A64')
ST=ParagraphStyle('body',fontName='Arial',fontSize=10.6,leading=14.2,textColor=INK,spaceAfter=0)
SM=ParagraphStyle('small',parent=ST,fontSize=8.6,leading=11.4,textColor=GREY)
HD=ParagraphStyle('head',parent=ST,fontName='ArialB',fontSize=13.2,leading=17)
TT=ParagraphStyle('title',parent=ST,fontName='ArialB',fontSize=23,leading=27)
TS=ParagraphStyle('table',parent=ST,fontSize=9.1,leading=12.2)
C=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
C.setTitle('Märklin 62762 - Bildbefund und Umbaugrundlage')
C.setAuthor('Dokumentation zum ICE 2976')
C.setSubject('Beidseitige Bildprüfung, Abgrenzung 62761/62762 und Folgen für die Originalplatinen-Variante')
qa=[]; records=[]; page=0; y=0

SOURCES={
 'Q1':('komo35 / eBay','627610 und 627620, Artikel 147416253187','https://www.ebay.de/itm/147416253187'),
 'Q2':('Frank Liedke / Kleinanzeigen','3370 ICE, drei Leiterplatten; 20.02.2026','https://www.kleinanzeigen.de/s-anzeige/maerklin-h0-3370-ice-3x-leiterplatten/3331585671-249-611'),
 'Q3':('Lokstoredigital','ICE 1 mit zwei Triebköpfen; Vergleichsfahrzeug 33701','https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/'),
 'Q4':('Märklin','Explosionszeichnung und Ersatzteilliste 3370, S. 1-2, Pos. 27','https://static.maerklin.de/damcontent/ac/29/ac29ce530a37bf0a5e5e04986eed4c3a1434542471.pdf'),
 'Q5':('Märklin','Ersatzteilblatt 33701/37701/39711, S. 3, Position 27','https://static.maerklin.de/damcontent/c7/9c/c79c321455edb84f118a74a9c58838611434542615.pdf'),
 'Q6':('Märklin','Einbauanleitung 60972/60982, deutsche Fassung, S. 3-9','https://static.maerklin.de/damcontent/da/e4/dae4fa90473657b9466d908bd6dcfa601663856106.pdf'),
 'Q7':('Märklin','60972: mLD3 mit 21MTC-Schnittstellenplatine','https://www.marklin.com/products/details/article/60972'),
 'Q8':('Märklin','60982: mLD3 mit Kabelbaum und losem NEM-Stecker','https://www.marklin.com/products/details/article/60982'),
 'Q9':('Hagi / Stummiforum','TAMS W11 in TEE und ICE; Originalbericht 02.03.2008','https://www.stummiforum.de/t21783f5-TAMS-W-in-TEE-und-ICE-einbauen-gt-Was-beachten.html'),
 'Q10':('Roloand62 / H0-Modellbahnforum','Märklin 3750 Schaltplan; Beiträge 6-7, 19.03.2007','https://www.h0-modellbahnforum.de/t299058f54885-Maerklin-Schaltplan.html'),
 'Q11':('ICEbeamter / H0-Modellbahnforum','ICE 1 fährt nicht; Originalbericht 01.02.2019','https://www.h0-modellbahnforum.de/t341874f19606-ICE-faehrt-nicht.html'),
 'Q12':('Schönwitz','E627620: Ersatzteilseite mit Bildplatzhalter','https://modellbau-schoenwitz.de/ersatzteilfinder/maerklin/teil/E627620'),
}

def p(text,style=ST,x=M,width=CW,top=None,gap=9):
    global y
    pos=y if top is None else top
    para=Paragraph(text,style); _,hh=para.wrap(width,H)
    if pos-hh<43: raise ValueError(f'Überlauf S.{page}: {text[:90]} bis {pos-hh}')
    para.drawOn(C,x,pos-hh)
    qa.append({'page':page,'type':'text','bottom':pos-hh,'top':pos})
    records.append({'page':page,'text':text})
    if top is None: y=pos-hh-gap
    return hh

def ref(k):
    return f'<super><link href="{escape(SOURCES[k][2])}" color="#135A64">[{k}]</link></super>'

def begin(title):
    global page,y
    if page: C.showPage()
    page+=1; y=H-45
    C.bookmarkPage(f'p{page}');C.addOutlineEntry(title,f'p{page}',0,False)
    C.setFillColor(GREY);C.setFont('Arial',8);C.drawRightString(W-M,25,str(page))
    p(title,TT,gap=17)

def section(title): p(title,HD,gap=8)

def picture(path,box,height,caption=None):
    # Preserve source pixels. Crops use a PDF clipping path; no generated/repainted PCB details.
    global y
    im=Image.open(path); iw,ih=im.size
    if box is None: box=(0,0,iw,ih)
    x0,t0,x1,t1=box; bw=x1-x0; bh=t1-t0
    scale=min(CW/bw,height/bh); dw=bw*scale;dh=bh*scale
    left=M+(CW-dw)/2; bot=y-dh
    C.saveState();clip=C.beginPath();clip.rect(left,bot,dw,dh);C.clipPath(clip,stroke=0)
    C.drawImage(ImageReader(str(path)),left-x0*scale,bot-(ih-t1)*scale,iw*scale,ih*scale)
    C.restoreState();qa.append({'page':page,'type':'image','bottom':bot,'top':y})
    meta=(left,bot,scale,x0,t0,x1,t1)
    y=bot-7
    if caption:p(caption,SM,gap=12)
    return meta

def side_picture(path,box,left,top,width,height):
    im=Image.open(path);iw,ih=im.size;x0,t0,x1,t1=box
    scale=min(width/(x1-x0),height/(t1-t0));dw=(x1-x0)*scale;dh=(t1-t0)*scale
    xx=left+(width-dw)/2;bot=top-dh
    C.saveState();clip=C.beginPath();clip.rect(xx,bot,dw,dh);C.clipPath(clip,stroke=0)
    C.drawImage(ImageReader(str(path)),xx-x0*scale,bot-(ih-t1)*scale,iw*scale,ih*scale);C.restoreState()
    qa.append({'page':page,'type':'image','bottom':bot,'top':top})

def table(headers,rows,widths):
    global y
    vals=[[Paragraph(f'<b>{escape(z)}</b>',TS) for z in headers]]
    vals += [[Paragraph(z,TS) for z in row] for row in rows]
    tab=Table(vals,colWidths=widths,hAlign='LEFT')
    tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#EDEDED')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),.6,HexColor('#888888')),('LINEBELOW',(0,1),(-1,-1),.3,HexColor('#D6D6D6'))]))
    _,hh=tab.wrap(CW,H)
    if y-hh<45:raise ValueError(f'Tabelle läuft über S.{page}: {y-hh}')
    tab.drawOn(C,M,y-hh);qa.append({'page':page,'type':'table','bottom':y-hh,'top':y});y-=hh+13
    records.append({'page':page,'headers':headers,'rows':rows})

def marker(meta,n,pixel,label_offset):
    left,bot,s,x0,t0,x1,t1=meta
    xx=left+(pixel[0]-x0)*s; yy=bot+(t1-pixel[1])*s
    lx=xx+label_offset[0];ly=yy+label_offset[1]
    C.saveState();C.setStrokeColor(TEAL);C.setLineWidth(1)
    C.line(xx,yy,lx,ly);C.setFillColor(white);C.circle(lx,ly,8,stroke=1,fill=1)
    C.setFont('ArialB',9);C.setFillColor(TEAL);C.drawCentredString(lx,ly-3,str(n));C.restoreState()

begin('Märklin 62762: Bildbefund und Umbaugrundlage')
p('<b>Beide Seiten gefunden.</b> Zwei getrennte Angebote zeigen die Leiterbahnseite und die gegenüberliegende Schalterseite derselben Platinenbauart. Aufdruck: <b>62762 / 03/92 / VER 1.1</b>. Die Bilder liefern eine konkrete Grundlage für den Erhalt der Originalplatine. Die elektrische Zuordnung des eigenen Fahrzeugs bleibt davon getrennt.'+ref('Q1')+ref('Q2'))
section('Leiterbahnseite - im vorhandenen Fahrzeugfoto oben')
picture(EVID/'kleinanzeigen_3331585671_bild1.jpg',(55,260,735,437),170,'Abb. 1: 62762, Ausschnitt aus Foto 1 des Angebots Q2. Nummer und Revision sind lesbar; keine nachgezeichneten Leiterzüge.')
section('Gegenseite - Schiebeschalter am U-förmigen Ende')
picture(EVID/'kleinanzeigen_3331585671_bild2.jpg',(125,365,747,530),168,'Abb. 2: Dasselbe Exemplar, Foto 2 aus Q2. Die versetzten Randkerben und vier Bohrungen passen bei Seitenwechsel spiegelbildlich.')
p('<b>Ergebnis für den Umbau:</b> Die gezeigte 62762 ist ein passiver Verbindungsträger mit mechanischem Schalter. Das Foto begründet weder den Ausbau vermeintlicher Leistungselektronik auf dieser Platine noch einen pauschalen Leiterbahnschnitt. Die dicht bestückte Nachbarplatine in den Angeboten ist die <b>62761</b>.')
p('Umfang: forensische Bild- und Quellenprüfung als Grundlage der separaten Anleitung ohne LoDi-Motorplatine. Keine am Fahrzeug ausgeführten Messungen oder Umbauten. Quellenabruf und Auswertung: 12.09.2026.',SM)

begin('Zweites Bildpaar und Teileidentität')
p('Das zweite Angebot bestätigt die Gegenansichten unabhängig vom ersten. Hier steht die <b>62762 jeweils rechts</b>; links liegt eine 62761. Die Ausschnitte unten zeigen nur die rechte Platine.'+ref('Q1'))
top=y
p('Leiterbahnseite',HD,x=M,width=240,top=top)
p('Schalterseite',HD,x=M+267,width=240,top=top)
side_picture(EVID/'ebay_147416253187_bild2.webp',(810,12,1100,1010),M,top-27,240,330)
side_picture(EVID/'ebay_147416253187_bild1.webp',(875,50,1180,1090),M+267,top-27,240,330)
y=top-369
p('Abb. 3 und 4: Ausschnitte aus Q1, Galerie Bilder 2 und 1. Originaldateien jeweils 1600 × 1200 Pixel; Vergleich ohne künstliche Schärfung.',SM)
table(['Nachweis','Aussage und Grenze'],[
 ['Fotoaufdruck','62762 / 03/92 / VER 1.1 auf der Leiterbahnseite. Das ist eine Platinenkennung, kein Beleg für einen integrierten Digitaldecoder.'],
 ['Märklin-Ersatzteilblätter','627620 ist als Leiterplatte, Position 27, dokumentiert. Im Blatt 3370 liegt sie beim motorlosen Kopf; der Motorwagen hat dort 627610. Auch das spätere Blatt führt 627620 hinten.'+ref('Q4')+ref('Q5')],
 ['Übertragbarkeit auf 2976','Die Standardbestückung eines 3370/33701 beweist nicht die komplette Verdrahtung eines 2976. Ein gleicher Träger kann in einem anders aufgebauten Fahrzeug verwendet sein.']
],[120,CW-120])

begin('Abgleich mit dem vorhandenen ICE')
picture(BASE/'Arbeitsstand_REV10/bilder/0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg',None,130,'Abb. 5: Persönliche Ausgangsaufnahme, 842 × 204 Pixel. Der Motor befindet sich links. Die Nummer ist darin nicht sicher lesbar.')
p('<b>Sehr starke geometrische Übereinstimmung:</b> lange parallele Leiterzüge, versetzte Kantenkerben, Befestigungsbohrungen, Dreier-Lötgruppe, Zwischenpads und breite Endkontaktfläche passen zum 62762-Vergleich. Diese Kombination stützt die Zuordnung deutlich stärker als die bloße Farbe oder Länge der Platine.')
section('Hochauflösender Vergleich mit markierten Prüfbereichen')
meta=picture(BASE/'Arbeitsstand_REV10/quellen_alt/tmp/pdfs/rev5/research/dummy_full.jpg',(245,1320,3935,2600),188)
marker(meta,1,(390,2160),(-4,22))
marker(meta,2,(3410,1730),(23,19))
marker(meta,3,(2660,1600),(-10,23))
marker(meta,4,(1080,1740),(-18,-21))
marker(meta,5,(2575,2025),(25,-25))
p('Abb. 6: Unveränderte Bildpixel mit Vektormarkierungen. LoDi-Foto des motorlosen Kopfes aus dem Beispiel 33701, nicht das persönliche Fahrzeug. Die Bildnummern sind Prüfbereiche, keine Hersteller-Padnamen.'+ref('Q3'),SM)
table(['Nr.','Erkennbarer Bereich','Bedeutung'],[
 ['1','Endkontakte am geschlossenen Ende','Vier Kontakt-/Lötflächen; ihre Funktionen zuerst über angeschlossene Leitungen und Messung zuordnen.'],
 ['2','Drei Schalterlötstellen am U-Ende','Schaltverhalten in beiden Stellungen erfassen; keine Annahme über die Kontaktfolge.'],
 ['3','Kleine Zwischenpads','Vorhandene Anschlussmöglichkeiten; kein automatischer Masse- oder Plusanschluss.'],
 ['4','Befestigungsauge mit Kupferumgebung','Verbindung zum Chassis kann durch Montage entstehen. Ausgebaut und montiert vergleichen.'],
 ['5','Kennung / lange Leiterzüge','Layout identifizieren; Sichtverfolgung ist noch keine gemessene Netzliste.']
],[36,164,CW-200])

begin('Technische Folgerungen für den Erhalt')
table(['Bisher zu pauschal','Korrigierte Grundlage'],[
 ['„Alte aktive Schaltung auf der langen Platine entfernen“','Auf der fotografierten 62762 sitzen keine Relais, Elkos oder Leistungshalbleiter. Die separate alte Umschalteinheit und ihre Verdrahtung müssen eigenständig erfasst werden.'],
 ['„Leiterbahnen müssen getrennt werden“','Es ist bislang kein konkreter notwendiger Leiterbahnschnitt belegt. Vorhandene Verbindungen zuerst zuordnen; externe Drahtbrücken und Verbraucher können Messungen verfälschen.'],
 ['„Der Schalter wählt den vorderen Schleifer“','Sichtbar ist ein mechanischer Schiebeschalter. Ein Umbauer nennt die Erhaltung der Ober-/Unterleitungswahl. Das ist kein Beleg für eine fahrtrichtungsabhängige Schleiferumschaltung.'+ref('Q10')],
 ['„LoDi-Pads und Widerstände lassen sich übertragen“','62762 hat keine LoDi-Padbezeichnung, keine bestätigte 21MTC-Aufnahme und keine abgebildeten R4/R5. LED-Strombegrenzung und Decoderaufnahme gehören in den neuen Anschlussplan.'+ref('Q3')]
],[188,CW-188])
section('Vorgesehene Aufgabenteilung')
p('<b>62762:</b> vorhandener mechanischer Träger und nach Zuordnung gegebenenfalls passiver Verteiler. <b>Neuer Decoder:</b> Motorregelung, Richtungsinformation und Funktionsausgänge. <b>Separate LED-Widerstände:</b> Strombegrenzung, wenn die vorgesehenen Leuchteinsätze diese nicht selbst enthalten. <b>Alte Umschalteinheit:</b> gehört nicht parallel an den neuen Motorausgang.'+ref('Q6'))
section('Bevorzugter Aufbau als Planungsentscheidung')
p('Die Originalplatine zunächst vollständig erhalten. Neue Motorleitungen und nicht eindeutig zuordenbare Funktionsleitungen direkt und isoliert führen. Nur nachgewiesene, benötigte Kupfernetze weiterverwenden. Ein Leiterbahnschnitt kommt erst in Betracht, wenn der endgültige Plan die Trennung eines tatsächlich gemessenen Kupferverbunds verlangt und sich dieser Verbund nicht über externe Anschlüsse auflösen lässt.')
p('Diese Lösung erhält die Originalplatine tatsächlich als Bauteil des Aufbaus. Sie behauptet aber weder eine bereits ausreichende Stromtragfähigkeit aller alten Leiterzüge noch einen schon geprüften Einbauplatz für Decoder und Anschlussplatine.',SM)

begin('Prüfreihenfolge vor der Platinenbearbeitung')
p('Die folgende Reihenfolge ist aus den Bildbefunden und den Decoderanschlussbedingungen abgeleitet. Sie beschreibt die noch erforderliche Prüfung am eigenen Exemplar. <b>Alle Widerstandsprüfungen erfolgen ohne jede Versorgung (auch Oberleitung), Decoder und angeschlossenen Puffer.</b> Vor dem Umschalten auf Ω zuerst Spannungsfreiheit prüfen; vorhandene Energiespeicher nach ihrer Anleitung entladen.'+ref('Q6'))
table(['Nr.','Konkrete Arbeit','Auswertung'],[
 ['1','Leitungen vor jedem Ablöten an beiden Enden beschriften und fotografieren. U-Ende, geschlossenes Ende, Vorder-/Rückseite eindeutig benennen.','Aus Drahtfarbe und Nachbarfoto allein folgt keine elektrische Funktion.'],
 ['2','Stromlos Schleifer, Radsätze/Chassis, Dachkontakt falls vorhanden, Motor und Leuchten bis zu ihren Anschlussstellen verfolgen. Externe Verbindungen getrennt notieren.','Eine Netzliste erhält bestätigte Funktionen. Unzugängliche Endpunkte bleiben offen.'],
 ['3','Für zu prüfende Platinennetze angeschlossene Verbraucher oder Brücken nach Dokumentation so abtrennen, dass keine Parallelpfade bleiben. Messspitzen-Kurzschlusswert notieren.','Nahe am Eigenwert der Messleitungen: niederohmiger Pfad. Der Summerton allein ist kein Isolationsnachweis.'],
 ['4','Jeden der drei Schalteranschlüsse gegen die beiden anderen in beiden Stellungen messen. Zusätzlich zugehörige Endkontakte und Dachkontakt prüfen.','Erst die gemessene Kontaktmatrix erklärt die tatsächliche Schalterfunktion.'],
 ['5','Im höchsten Ω-Bereich beziehungsweise Autorange unerwünschte Verbindungen prüfen. Kupfernetze gegen Chassis und Befestigungen ausgebaut und montiert vergleichen.','OL bedeutet nur: oberhalb des Messbereichs. Es ist kein unbegrenzter Isolations- oder Hochspannungsnachweis.'],
 ['6','Neuen Netzplan mit Märklin-Funktionen erstellen. U+ und beide Motoranschlüsse müssen vom Chassis getrennt sein. Erst danach Anschluss- oder Schnittbedarf festlegen.','Bleibt eine Verbindung unklar, bleibt das betroffene Netz unbenutzt. Kein Schnitt aus einer bloßen Bildvermutung.']
],[43,266,CW-309])
section('Wann ein Schnitt überhaupt begründet wäre')
p('Ein geplanter Anschluss müsste zwei bisher leitend verbundene Punkte elektrisch trennen. Diese Verbindung ist am freigelegten Träger gemessen, die betroffene Leiterbahn eindeutig identifiziert und es gibt keine einfachere Trennung an einer äußeren Leitung. Erst dann wird eine konkrete Bearbeitungsstelle festgelegt und nach der Arbeit erneut gemessen. Für die vorliegenden Fotos ist ein solcher Fall <b>noch nicht nachgewiesen</b>.')

begin('60972 und 60982: Folgen für die neue Anleitung')
p('Bestätigter Bestand: 060972 und 060982, entsprechend Märklin 60972 und 60982. Die Besitzangabe legt noch nicht fest, ob sie die bisher geplanten 60977/59649 ersetzen oder zusätzlich vorhanden sind.')
table(['Teil','Belegter Anschlussweg','Folge'],[
 ['60972','mLD3 ohne Sound; 21MTC-Decoder mit beiliegender Schnittstellenplatine, Halterung und Schraube.'+ref('Q7'),'Bei vollständigem Satz ist eine Aufnahme vorhanden. Montagehöhe, Isolation und Zugänglichkeit am ICE prüfen.'],
 ['60982','mLD3 ohne Sound; fest angelöteter Kabelbaum, loser achtpoliger NEM-Stecker zum Selbstanlöten.'+ref('Q8'),'Direkte Verdrahtung möglich; dafür keine zweite 21MTC-Aufnahme nötig. Kein integrierter Sound durch Software nachrüstbar.']
],[60,224,CW-284])
section('Kabelfarben unbedingt getrennt behandeln')
table(['Funktion','60972, Märklin-Farben','60982, NEM-Farben'],[
 ['Gemeinsamer Plusanschluss U+','Orange','Blau, ohne Markierung'],
 ['Motoranschlüsse','Grün / Blau','Orange / Grau'],
 ['Außenschiene / Fahrzeugmasse','Braun','Schwarz'],
 ['Mittelschleifer','Rot','Rot'],
 ['Licht vorn / hinten','Grau / Gelb','Weiß / Gelb'],
],[196,155,CW-351])
p('Herstellerzuordnung nach deutscher Anleitung, S. 5-6. Markierte blaue Leitungen des 60982 (IN1/IN2/GND) sind andere Anschlüsse als U+. „Motoranschlüsse“ legt noch nicht die Fahrzeug-Fahrtrichtung fest. U+ darf nie mit Fahrzeugmasse verbunden werden. Beide Decoder setzen beim alten Feldspulenmotor einen geeigneten Motorumbau voraus.'+ref('Q6'),SM)
section('Welche Entscheidungen die Bildsuche nicht ersetzt')
p('Bei Verwendung von zwei mLD3 müssen Soundziel, Bedienung der beiden Köpfe und Programmierung neu festgelegt werden. Die ESU-spezifischen CV- und Master/Slave-Schritte aus REV13 gelten dafür nicht. Auch die Frage, ob außer der LoDi-Motorplatine die Front- und Wagenmodule entfallen, ist noch offen. Die 62762-Bildbasis lässt sich für beide Entscheidungen verwenden.')
p('<b>Gesamtbewertung:</b> Die beidseitige Bildlücke ist geschlossen. Der Erhalt der 62762 ist technisch plausibel und besser begründet als zuvor. Offen sind die tatsächlichen Netze und Lasten des eigenen Fahrzeugs sowie die endgültige Decoder- und Beleuchtungswahl. Eine fertige Lötfreigabe wäre mit dem bisherigen Nachweisstand zu weitgehend.')

begin('Quellen und Beweisgrenzen')
p('Abruf: 12.09.2026. Bildausschnitte dienen dem Vergleich und der technischen Analyse. Es wurden keine Platinenmerkmale ergänzt oder durch KI erzeugt. Die unveränderten Bilddateien sind mit Ursprungs-URL, Auflösung und SHA-256 in der lokalen Belegsammlung gesichert.',SM)
for key,(owner,title,url) in SOURCES.items():
    p(f'<b>{key}</b> {escape(owner)}. <link href="{escape(url)}" color="#135A64">{escape(title)}</link>.',SM,gap=8)
section('Gewichtung der Belege')
p('<b>Direkte Bildbelege:</b> Q1 und Q2 liefern zwei voneinander getrennte Bildpaare. Q3 enthält zusätzlich das bereits vorhandene hochauflösende Vergleichsfoto der losen 62762 im 33701-Kontext. Die eigenen Ausgangsfotos dokumentieren den vorhandenen ICE, jedoch keinen sicher lesbaren Platinenaufdruck.',SM)
p('<b>Herstellerbelege:</b> Q4/Q5 bestätigen die Ersatzteilnummer 627620 und deren Position im jeweiligen Modell. Sie sind keine vollständigen Schaltpläne. Q6-Q8 belegen Eigenschaften und Anschlüsse der neuen Decoder. Bei Q6 wurde die deutsche Fassung verwendet; ein widersprüchlicher Sound-Absatz in der englischen Fassung wird nicht als Produkteigenschaft übernommen.',SM)
p('<b>Originalberichte:</b> Q9 nennt 62762 in beiden Köpfen eines analogen ICE. Q10 beschreibt den Einbau einer Steuerwagenplatine zusammen mit einem separaten Decoder in einem Motorwagen. Beide Berichte stützen Variantenvielfalt, aber keinen universellen Lötplan. Q11 erschien auch im Stummiforum; derselbe Autor und Vorgang zählen nur einmal.',SM)
p('<b>Ausgeschlossene Fehlbelege:</b> Q12 verwendet einen Bildplatzhalter. Die Benennung „Leiterplatte (Decoder)“ beweist keine Digitalfunktion. Unpassende Bildsuchtreffer zu Weichendecodern, Roco-Artikelnummern und die bestückte 62761 wurden nicht als 62762 verwendet.',SM)
p('Bildnachweise: Q1, Bilder 1/2; Q2, Bilder 1/2; Q3, loses Originalteil im Abschnitt motorloser Triebkopf. Eigene Bilder: 0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg und BAD231CB-B878-4D94-B5EE-CDAB1D69D455_4_5005_c.jpeg aus dem vorhandenen Arbeitsbestand.',SM)
C.save()
(WORK/'62762_pdf_layout.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2))
(WORK/'62762_pdf_inhalt.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
print(json.dumps({'pdf':str(OUT),'pages':page,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'min_content_bottom':min(q['bottom'] for q in qa)},ensure_ascii=False))
