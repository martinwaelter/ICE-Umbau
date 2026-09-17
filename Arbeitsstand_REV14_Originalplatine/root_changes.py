from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def p(t):return {'type':'p','text':t}
def small(t):return {'type':'small','text':t}
def step(n,t):return {'type':'step','label':str(n)+'.','text':t}
def note(t,label='BEACHTEN',tone='info'):return {'type':'note','label':label,'text':t,'tone':tone}
def table(h,r,w=None):return {'type':'table','headers':h,'rows':r,**({'widths':w} if w else {})}
def fig(k,h=170):return {'type':'figure','kind':k,'maxh':h}
def setpage(P,n,title,goal,blocks,before='',check='',sources=None,phase='Umbau | Originalplatine 62762'):
 P[n]={'n':n,'title':title,'phase':phase,'goal':goal,'before':before,'blocks':blocks,'check':check,'sources':sources or []}

def apply(P):
 setpage(P,1,'ICE 2976 mit Originalplatine 62762','Vollständige bebilderte Werkstattanleitung · REV14 · ohne LoDi-Motorplatine. Motorumbau, Sound, Frontlicht, Wagenbeleuchtung, CS3 und Endprüfung in einer Ausgabe.',[
 fig('system',155),
 note('60972 und 60982 vorhanden; 60977 am 12.09.2026 als bestellt bestätigt. Multimeter, Märklin-Programmer und aktuelle CS3 vorhanden. Kein separates Prüfgleis: Aufbau auf [[3]].','DEIN BESTAND'),
 p('<b>Gewählter Aufbau:</b> 60977 mit Sound vorn, ESU 59649 für das hintere Licht. Die originale 62762 bleibt als Träger erhalten; ihre alten Stromwege werden vollständig abgetrennt. Die neuen Anschlüsse liegen auf der kleinen Märklin-Aufnahme. Das ist eine bewusst elektrisch unabhängige Weiterverwendung der Originalplatine.'),
 p('<b>Welche LoDi-Teile bleiben?</b> Die Front-LED-Einsätze und die weißen Wagen-Lichtleisten aus dem bisherigen Plan. Nur die lange LoDi-Motorplatine 511 entfällt. Die Wagen erhalten deshalb die Standardbeschaltung mit Radkontakten und einem eigenen Lichtrelais.'),
 table(['Abschnitt','Direkt zu'],[['Arbeitsplatz, Bilder und Originalplatine','[[2]]–[[19]]'],['Motor, Träger, Anschlüsse und LED-Auslegung','[[15]]–[[20]]'],['Prüfaufbau, Programmieren und Einzeltests','[[8]]–[[14]]'],['Wagen, Last und vollständige Endabnahme','[[27]]–[[43]]'],['Fehlersuche, Ergänzungen und Quellen','[[44]]–[[46]]']],[3,1]),
 small('Nummerierte Schritte der Reihe nach abarbeiten. Ein Verweis zu einer Messkarte nennt den Rückkehrpunkt. „Vorwärts“ heißt Motortriebkopf voraus. Fotos fremder Fahrzeuge sind als Vergleich gekennzeichnet. Keine eigene Messung oder bestandene Hardwareabnahme wird vorweggenommen.')],sources=['Q1','Q4','Q6','Q39'],phase='Start | REV14')
 setpage(P,2,'Vorhandene Teile und benötigte Baugruppen','Vor Löten den tatsächlichen Bestand prüfen. „Geplant“ bedeutet nicht „bereits vorhanden“.',[
 table(['Status / Ort','Bauteil','Verwendung'],[
 ['Bestellt · vorn','Märklin 60977 mSD3','Sounddecoder, eigener 21MTC-Träger und ein Satzlautsprecher.'],
 ['Vorhanden','Märklin 60972 und 60982','Beide ohne Sound. Der freie originale 60972-Träger ist hinten vorgesehen; Decoder geschützt lagern.'],
 ['Geplant · Motor','Märklin 60941','Vollständiger HLA-Satz für die bestätigte Trommelkollektor-Bauart.'],
 ['Geplant · hinten','ESU 59649 LokPilot 5 MKL','Lichtdecoder auf dem 60972-Träger; Teilbestand prüfen.'],
 ['Erhalten','Originalplatine 62762','Alte Verbindungen entfernen; isolierter Aufbau [[19]]/[[22]].'],
 ['Beide Fronten','2 × LoDi 514, 4 Serienwiderstände','Je Farbe ein eigener Widerstand; vorn fehlen jetzt R4/R5 der LoDi 511. Auslegung [[20]].'],
 ['Wagen / Innenlicht','Weiße LoDi ICE-M; Lichtrelais [[32]]','Wagen-Radkontakte erforderlich; O = Rad, B = RT, L = GE.'],
 ['Vorhandene Geräte','CS3, Multimeter, Märklin-Programmer','Exakte Artikel/Anleitung ablesen. 60971 nur verwenden, wenn tatsächlich bestätigt.']],[.95,1.3,2.15]),
 p('<b>Arbeitsplatz:</b> Nichtleitende Unterlage, Kamera/Lupe, Schraubenablage, passende Schraubendreher, regelbare Elektronik-Lötstation, Elektroniklot, Entlöthilfe, flexible Litze, Schrumpfschlauch, isolierte Prüfclips und zugentlastete Steckverbindungen. Eine passende isolierende Halterung für die kleinen Aufnahmen einplanen.'),
 step(1,'Artikel, beide Platinenseiten und vorhandene Halter fotografieren. Decoder-/Trägerherkunft beschriften. Fotoordner „ICE2976_REV14_Originalplatine“ anlegen.'),
 step(2,'CS3/Netzteil ______; Multimeter/Handbuch ______; Programmerartikel ______. Den getrennten Prüfabschnitt [[3]] vorbereiten. Der Prüfweg [[8]] nutzt die Endträger und den geprüften HLA; zwei zusätzliche Prüfstände sind keine Pflicht.'),
 note('Kein alter Analog-Umschalter bleibt mit Motor oder Digitalversorgung verbunden. Puffer 60974 während des Grundumbaus abgetrennt lassen. Keine Leiterbahn auf Verdacht durchschneiden.','GRUNDREGEL')],sources=['Q1','Q2','Q4','Q6','Q39'])
 # Prepare before mechanics, not an impossible precondition on the later pair test.
 P[4]['check']='Zwei getrennte Kontakte je Übergang sind vorhanden oder ihre konkrete Nachrüstung ist geklärt. Mit den Messgrundlagen fortfahren. Die Decoderpaarprüfung folgt nach dem Motorumbau; jetzt nichts bestromen.'
 P[7]['blocks'][0]['text']='Beschriftung mit der richtigen Herstelleransicht abgleichen. Bei der Originalplatine 62762 gelten die neutral markierten Altanschlüsse nach [[19]]. Die kleinen Märklin-Träger erhalten neue Anschlüsse nach [[23]]/[[26]]. Weißes Wagen-SJ2 bleibt unverändert.'
 P[15]['title']='Den 60941-Motor vollständig montieren'
 P[15]['before']='Originalverkabelung und 62762 nach [[19]] dokumentiert und abgelöst; alle Quellen getrennt. Trommelkollektormotor anhand Satz und eigenem Aufbau bestätigt. Die spätere Paarprüfung ist jetzt noch nicht erforderlich.'
 for b in P[15]['blocks']:
  if b.get('label')=='1.':b['text']='Den auf [[19]] geöffneten Kopf bereitlegen. Lange 62762 und separate alte Umschalteinheit sind ausgebaut und beschriftet gesichert. Motor, alte Feldspule, Bürsten und Befestigungen nochmals mit dem Ausgangsfoto vergleichen.'
  if b.get('label')=='2.':b['text']='Letzte alte Motor-/Lampenverbindungen einzeln an ihren Lötstellen lösen. Die alte Lampenfassung nicht als LED-Lötstütze benutzen. Originalplatine aufbewahren: Sie wird auf [[22]] wieder eingesetzt.'
 setpage(P,23,'Vorn: direkt am Märklin-Träger verdrahten','Die neue Elektrik benutzt die beschrifteten Leitungen des 60977-Trägers. Unbekannte Kupferbahnen der 62762 führen keinen neuen Decoderstrom.',[
 fig('front',166),small('Funktionsschema, keine maßstäbliche Padansicht. Märklin-Farben gelten für diesen Träger; 60982-Kabelfarben sind anders.'),
 table(['Träger / Märklin-Litze','Anschluss'],[['B/GR · rot','Eigener Schleifer plus RT-Kupplungspfad; isolierter Dreiwegpunkt.'],['0/GL · braun','Örtlicher Rad-/Schienenkontakt.'],['MV · grün / MR · blau','Je ein Motorzweig mit eigener Drossel und Motor-Service-Trennstelle.'],['+Ub · orange','LED-Plus vorn; gesonderter Abzweig zur Relaisspule [[32]].'],['LV · grau / LR · gelb','Weiß / Rot, jeweils über eigenen Widerstand [[20]].'],['AUX1 · braun-rot','Nur Relaisspule über Modulanschluss [[32]], nicht unmittelbar GE.'],['Lautsprecherbuchse','Ein unveränderter Satzlautsprecher nach [[24]].']],[1.2,2.5]),
 step(1,'Die spätere außen erreichbare Motor-Service-Trennstelle nach [[42]] jetzt einplanen. Steckverbinder müssen zum Motorstrom passen, eindeutig gepolt, isoliert und zugentlastet sein. Keine Messleitung unter dem Dach einklemmen.'),
 step(2,'Freie Adern nach [[6]] prüfen. Neue Leitungen beschriften, Schrumpfschlauch auffädeln, kurz abisolieren und zugfrei verlöten. Dreiwegpunkte außerhalb kleiner Pads sicher bündeln und vollständig isolieren. Lupe, Anschlussprüfung [[7]] und beide Drehgestellendlagen prüfen.'),
 note('Decoder bleibt beim Löten abgezogen. Motor-Service-Stecker für die Programmierfolge [[8]] zunächst offen. LED-Zweige erst nach [[20]] anschließen. RT/GE zum Wagenbus und Relaisspule vorerst einzeln isoliert lassen; Anschluss später auf [[32]].','JETZIGER ZUSTAND')],before='Motorprüfung [[18]] und Haltermontage [[22]] bestanden. Beide Träger ohne Decoder, keine Quelle angeschlossen.',sources=['Q1','Q8','Q39'])
 P[26]['sources']=['Q1','Q6','Q39'];P[26]['blocks'][-1]['text']='Fehlt die hintere Stromaufnahme, ist der ungekuppelte Fahrzeugtest über die eigenen Räder/den eigenen Schleifer noch nicht möglich. Den Endträger-Prüfaufbau [[8]] kann man unabhängig benutzen. Hinten niemals einen Decoder-Ausgang auf GE legen.'
 P[33]['goal']='Vor der ersten Bestromung und jedem erneuten Einsetzen am aufgebauten Kopf prüfen. Die gemeinsame mfx-Paarprüfung folgt erst nach den Einzelkontrollen.'
 rows=P[33]['blocks'][0]['rows']
 rows[0][0]='Persönliche Decoderwerte gesichert und Programmierfolge [[8]]–[[13]] ausgeführt; spätere Paarprüfung [[14]] noch nicht abhaken.'
 rows[4][0]='Beide LED-Farbzweige dieses Kopfes nach [[20]] begrenzt oder einzeln abgetrennt; Messung [[21]] folgt beim Ersttest.'
 rows[5][0]='Ein Satzlautsprecher direkt am vorgesehenen 60977-Trägeranschluss [[24]].'
 rows[8][0]='Getrennter Prüfabschnitt [[3]], Erstkontrolle [[36]]/[[37]] vorbereitet; Wagen, Relaiskontaktlast und Puffer getrennt.'
 P[33]['blocks'][2]['text']='Nicht ausgeführte Hardwareprüfungen bleiben offen. Für die erste Ruhestromkontrolle dürfen beide LED-Zweige abgetrennt sein; vor Licht-/Paarabnahme müssen sie nach [[20]]/[[21]] angeschlossen und geprüft werden.'
 P[36]['before']='Checkliste [[33]], Motorprüfung und Stecklage [[34]] bestanden. HLA nach [[8]] stromlos vom ESU getrennt und wieder ausschließlich vorn angeschlossen. Prüfabschnitt [[3]] frei; Gegenkopf, Wagen, Relaislast und Puffer getrennt.'
 for b in P[36]['blocks']:
  if b.get('label')=='3.':b['text']='Nur nach unauffälliger Erstkontrolle: STOP, Gleisstecker abziehen und am Betriebsausgang anschließen. Erneut Ruhe prüfen. Sind LED-Zweige nach [[20]] vorbereitet, die Messfolge [[21]] ausführen, dann hierher zurückkehren: F0 aus → dunkel, vorwärts → Weiß, rückwärts → Rot. Danach Sound leise zuschalten. Keine ungeschützte LED direkt anschließen.'
  if b.get('label')=='4.':b['text']='Erst nach bestandenem Standtest: freien Auslauf und Endbegrenzung prüfen. Kleinste Fahrstufe kurz anlegen, dann 0; Räder nie festhalten. Abschaltung: sofort trennen und Ursache nach [[44]] klären. Dieser Versuch ersetzt keine Lastabnahme [[39]].'
 P[36]['blocks']=[{**b,'text':b.get('text','').replace('Diagnose nach [[32]]','Diagnose nach [[44]]').replace('Ursache nach [[32]]','Ursache nach [[44]]')} if 'text' in b else b for b in P[36]['blocks']]
 # The following source upper bounds are not output protection settings.
 P[36]['blocks'].insert(0,small('60977: Motor maximal 1,1 A; ein Licht-/AUX-Ausgang 250 mA; Licht/AUX zusammen 300 mA; Gesamtlast 1,6 A. Programmierausgang maximal 1,5 A nach CS3-Anleitung: kein Schutzgrenzwert für eine einzelne LED.'))
 P[37]['title']='Gegenkopf: Einzelkontrolle und Licht vorbereiten'
 P[37]['goal']='Zuerst die eigene Stromaufnahme des Gegenkopfs prüfen. Dann die beiden Fronten und ihre begrenzten LED-Zweige gemeinsam prüfen; die abschließende Synchronisationsabnahme folgt auf [[14]].'
 for b in P[37]['blocks']:
  if 'text' in b:b['text']=b['text'].replace('DCC-Wartung nur auf [[9]]','DCC-Wartung nur mit Motor-Prüflast nach [[8]]/[[12]]').replace('Diagnose [[32]]','Diagnose [[44]]')
 P[37]['check']='Einzelkontrolle und tatsächliche LED-Zweige sind geprüft. Jetzt die vollständige mfx-Paarabnahme [[14]] durchführen. Erst danach Wagenbus anschließen.'
 P[42]['blocks'][3]['text']=P[42]['blocks'][3]['text'].replace('zur LoDi','zum Märklin-Träger') if 'text' in P[42]['blocks'][3] else ''
 # Replace every residual reference in existing closure and fault prose precisely later.
 P[43]['blocks'][-1]['text']='Datum ______; elektrischer Abschluss ______; freigegebener Bereich ______. Radkontakte und Meldefunktion nach [[30]] getrennt bewerten. Erst im bestätigten Bereich fahren. Puffer und automatischer Signalhalt benötigen die Ergänzung [[45]].'
 for b in P[44]['blocks']:
  if b.get('type')=='table':
   for row in b['rows']:
    row[:]=[x.replace('GE-AUX-Zuordnung','AUX1-/Relaiszuordnung').replace('bis O/L','bis B/L sowie örtliche O-Radkontakte') for x in row]
  if b.get('label')=='1.':b['text']='Zug stromlos machen; Gleis/Bus, Decoder und Puffer trennen. ESU-Wartung über Endträger plus geprüfte Motorlast nach [[8]]/[[12]]; alternativ dokumentierter geeigneter Prüfstand. 60977 nach [[10]]/[[31]] bearbeiten. Beide Motorendstufen niemals gleichzeitig an denselben Motor anschließen.'
 P[45]['blocks'][1]['text']='60974 ist für Märklin mLD3/mSD3 vorgesehen. Vorn sitzt der 60977 jetzt auf seinem originalen Träger mit dokumentierter vierpoliger SUSI-Buchse. Nur den unveränderten vorgesehenen Stecker dort einsetzen. Die ähnliche Buchse des hinteren Trägers gibt den ESU nicht für 60974 frei.'
 P[45]['blocks'][2]['text']='Vor der Ergänzung Platz für Modul und Kabel bei geschlossenem Dach prüfen. Artikel und Firmware des 60977 sichern, SUSI-Buchse mit Q1 abgleichen. Der bisher erforderliche LoDi-Sondernachweis entfällt; keine Verbindung an GND, +5V oder beliebige Altplatinenpads herstellen.'
 P[45]['sources']=['Q1','Q7','Q15','Q20','Q39']

def finish(P):
 # Single front pickup is deliberate: no motor current through the train couplers.
 P[26]['goal']='Nur der vordere Schleifer speist den Zug. Hinten kommt B/GR ausschließlich von RT; der alte hintere Schleifer bleibt elektrisch getrennt. Radkontakte versorgen weiterhin 0/GL.'
 for b in P[26]['blocks']:
  if b.get('label')=='1.':b['text']='Hinteren Schleifer und seinen bisherigen Anschluss aufnehmen. Diese Leitung vollständig vom neuen B/RT-Netz trennen und ihr freies Ende einzeln sicher isolieren; auch alte Verbindungen über 62762 lösen. Der Schleifer darf mechanisch bleiben. Radkontakt getrennt als R kennzeichnen; Kupplung RT/GE nach [[28]] zuordnen.'
  if b.get('label')=='2.':b['text']='Die abgelöste Schleiferleitung bleibt unbenutzt. Radlitze R zum tatsächlich benutzten leitenden Radpfad prüfen, RT zum richtigen Kupplungskontakt. Positive Vor-/Nachkontrollen und normale Bewegung nach [[6]]. Vor Elektronikanschluss RT gegen den nun abgetrennten Schleiferpfad prüfen: keine Verbindung.'
  if b.get('label')=='3.':b['text']='Nur <b>RT an B/GR</b> anschließen. Den früher vorgesehenen Dreiwegpunkt aus Schleifer + RT + B/GR gibt es hier nicht. Leitung kurz, flexibel, zugentlastet und vollständig isoliert ausführen; [[7]] nach dem Löten wiederholen.'
  if b.get('label')=='6.':b['text']='Nach jedem Anschluss oder Umlegen betroffene Prüfungen [[6]]/[[7]] wiederholen. Beide Drehgestell-/Kupplungsendlagen müssen ohne Litzenzug erreichbar sein. RT hat jetzt keinen Kontakt zum hinteren Schleifer; GE endet ebenfalls isoliert. Beide freien Enden getrennt halten.'
  if b.get('label')=='STOPP':b['text']='Der Gegenkopf bekommt absichtlich keinen Strom über seinen alten Schleifer. Seine Einzelprüfung erfolgt über den Endträger-Aufbau [[8]]; die spätere Fahrzeugprüfung [[37]] speist RT über eine isolierte Prüfverbindung. Hinteren Schleifer nicht als scheinbare Fehlerbehebung wieder anschließen.'
 P[37]['before']='Gegenkopf nach [[33]]/[[35]] vorbereitet; Motorseite [[36]] bestanden. Kein Wagen/Puffer. Beide Köpfe auf demselben freien Prüfabschnitt. Für die vorübergehende RT-Verbindung eine isolierte, passende und zugentlastete Prüfleitung bereitlegen.'
 for b in P[37]['blocks']:
  if b.get('label')=='1.':b['text']='Gegenkopf zunächst allein außerhalb des Gleises über die Endträger-Aufnahme [[8]] speisen: nur CS3-Programmierausgang an B/GR und 0/GL, Motoradern offen, kein hinterer Schleiferanschluss. STOP vor jedem An-/Abklemmen; dann GO, Ruhe beobachten. Bei Abschaltung/Wärme/Geruch STOP, trennen und [[44]]. Für diese Ruhekontrolle kein DCC-Lesen ohne Motorlast fordern.'
  if b.get('label')=='2.':b['text']='Nach unauffälliger Einzelkontrolle STOP und Quelle vollständig trennen; Prüfversorgung am hinteren Träger entfernen. Beide Köpfe mit Abstand auf den freien Prüfabschnitt stellen. RT der beiden Köpfe vorübergehend durch die vorbereitete isolierte Leitung verbinden; GE bleibt getrennt. So versorgt der vordere Schleifer beide Köpfe, jeder nutzt seine eigenen Radkontakte. Betriebsausgang anschließen; Automatik aus, Fahrstufe 0, GO. Mit dieser Prüfleitung keine Fahrt durchführen.'
  if b.get('label')=='4.':b['text']='STOP, Gleisstecker abziehen. Köpfe abnehmen/wieder aufsetzen, RT-Prüfverbindung stromlos kontrollieren. GO und Lichtfolge wiederholen. Beide hinteren LED-Zweige nach [[21]] messen. Danach vollständig trennen und RT-Prüfleitung entfernen. Jetzt vollständige Synchronisationsprüfung [[14]] auf den Endträgern ausführen.'
 setpage(P,38,'Ein Schleifer: Fahrbereich und Signalhalt','Im Grundaufbau speist ausschließlich der vordere Schleifer. Das beseitigt die alte Verbindung zweier Mittelschleifer über RT; Motorstrom bleibt außerhalb der Wagenkupplungen.',[
 table(['Netz','Festlegung dieses Umbaus'],[['Vorderer Schleifer','Speist den 60977 und RT / B-Zug.'],['Hinterer Schleifer','Elektrisch abgetrennt und einzeln isoliert. Kein Anschluss an B/GR, RT, GE oder alte Kupferpfade.'],['Wagenkupplungen','RT trägt den hinteren Decoder und Wagenzweige. GE trägt geschalteten Wagenlichtstrom.'],['Radkontakte','Jeder Kopf und jeder Wagen erhält seinen örtlichen Schienenrückleiter.']],[1.2,3]),
 step(1,'Vor dem ersten kompletten Zugbetrieb hinten erneut prüfen: freie Schleiferleitung am eigenen Schleifer leitend, gegen den vollständig getrennten RT-Kabelbaum offen; positive Vor-/Nachprobe. Bei bestücktem Träger keine pauschale OL-Messung durch Elektronik, sondern den passiven RT-Zweig für diese Prüfung lösen.'),
 step(2,'Einen eigenen Fahrbereich mit einer bestätigten Digitalquelle wählen. Programmier-, Analog- und unbekannte Einspeisungen abgrenzen. Nur den wirklich vorbereiteten Bereich befahren; passende Kurvenradien, Übergänge und Wagenüberhänge zunächst von Hand und stromlos prüfen.'),
 step(3,'Beide Richtungen bewusst betrachten: Fährt der Gegenkopf voraus, liegt der aktive Schleifer weit hinten. Eine vorhandene stromlose Haltestrecke kann dadurch erst reagieren, wenn die Zugspitze bereits zu weit gefahren ist. Vorhandene Haltstellen deshalb nicht ungeprüft verwenden.'),
 step(4,'Bis zur eigenen Signalhaltabnahme [[45]] beaufsichtigt von Hand anhalten. Für einen späteren automatischen Halt Zuglänge, führenden Kopf, Kontaktpositionen und Bremsweg erfassen. Das Relais und die mfx-Synchronisation sind keine Schleiferumschaltung.'),
 note('Den hinteren Schleifer später einfach wieder anzuschließen würde das Strom- und Abschnittskonzept ändern. Dafür wären eine neue Schaltung und eine neue Last-/Bereichsprüfung nötig.','ÄNDERUNG AM AUFBAU'),
 small('Geprüfter Bereich ______; aktive Quelle ______; hinterer Schleifer getrennt ______; Fahrweg beider Richtungen ______; Signalhalt noch offen / gesondert geprüft ______.')],sources=['Q1','Q4','Q6','Q26'],phase='Vor Fahrt | Stromversorgung und Anlage')
 # Source diagrams are not physical pad maps; do not retain obsolete overload instructions.
 for n in [5,6,7,16,17,18,28,33,36,41,42,43,44,45]:
  def change(v):
   if isinstance(v,str):
    return v.replace('zur LoDi','zum Märklin-Träger').replace('an die LoDi','an den Märklin-Träger').replace('LoDi-Platine','Märklin-Aufnahme').replace('LoDi / Decoder','Märklin-Träger / Decoder').replace('DCC-Wartung nur auf [[9]]','DCC-Wartung nach [[8]]/[[12]]')
   if isinstance(v,list):return [change(z) for z in v]
   if isinstance(v,dict):return {k:change(z) for k,z in v.items()}
   return v
  P[n]=change(P[n])
 # Relay is tested on the already checked front decoder, with its contact load still absent.
 for b in P[36]['blocks']:
  if b.get('label')=='3.':b['text']+=' Anschließend die kontaktseitig noch unbelastete Relaisprüfung [[32]] ausführen und hierher zurückkehren.'
 # Disable a stale requirement for the earlier two-pickup arrangement.
 for b in P[43]['blocks']:
  if b.get('type')=='table':
   for row in b['rows']:
    row[:]=[x.replace('alleinige hintere Speisung','hinterer Schleifer getrennt').replace('Lasten / höchste Helligkeit /','Lasten / höchste geprüfte Helligkeit /') for x in row]
 for b in P[45]['blocks']:
  if b.get('label')=='STOPP':b['text']='Der hintere Schleifer bleibt elektrisch getrennt. Bei Gegenkopf voraus liegt die aktive Stromaufnahme hinten; vorhandene Abschaltstrecken können dann zu spät wirken. Puffer können weiteren Nachlauf verursachen. Haltpunkt mit ganzer Zuglänge neu abnehmen.'

def compact_and_correct(P):
 P[25]['blocks'][0]['maxh']=180
 for b in P[25]['blocks']:
  if b.get('label')=='1.':b['text']='Alte Leiterplatte und Anschlüsse fotografieren. Originalplatine auch hinten erhalten, alle alten Außenverbindungen lösen und die isolierte Halterung wie auf [[19]]/[[22]] ausführen. Kein alter Kupferpfad führt neue Decoderströme. Schleiferleitung getrennt aufbewahren; Radkontakt bleibt erforderlich.'
  if b.get('type')=='table':
   for row in b['rows']:
    row[:]=[x.replace('Schleifer/RT; örtlicher Radkontakt','Nur RT; örtlicher Radkontakt') for x in row]
 # Passive end-to-end RT bus carries the rear decoder and wagon load only.
 for b in P[28]['blocks']:
  if 'text' in b:b['text']=b['text'].replace('beide Schleifer','vordere Einspeisung und hinterer Decodereingang')
 # Remove the inherited LoDi-specific connection verification table.
 P[7]['title']='Neue Leitungen und Trägermontage prüfen'
 P[7]['blocks']=[
  step(1,'Nur leere, stromlose Träger prüfen. Beschriftung anhand Q1/Q39 übernehmen. Die unbenutzten Altleiterzüge der 62762 und deren Schraubringe sind fremde Metallflächen gegenüber dem neuen Kabelbaum.'),
  table(['Verbindung','Konkreter Prüfweg'],[
   ['Vorn B/GR','Eigener Schleifer und RT-Abzweig zur vorgesehenen B/GR-Leitung; jeder Abzweig einzeln prüfen.'],
   ['Vorn Motor','MV und MR zu jeweils einem Drossel-/Motorzweig. Motor für die Sechserprüfung vollständig vom Träger trennen.'],
   ['Vorn Front / Relais','+Ub zum lokalen LED-Plus; LV/LR über je R zum Farbzweig. AUX1 nur zum Relais-Steuereingang. GE allein vom Schließerkontakt.'],
   ['Hinten','RT zu B/GR, Radkontakt zu 0/GL; lokales +Ub zur Front, LV→Rot und LR→Weiß jeweils über R. Alter Schleifer ohne neue Verbindung.'],
   ['Wagen','RT-Kontakt zu B, GE-Kontakt zu L, örtliche Radfeder zu O. B-B und L-L an beiden Enden prüfen.'],
   ['Unbenutzte Leitungen','Jede freie Ader einzeln isolieren. Kein gemeinsamer Blankpunkt in einem Schrumpfschlauch.']],[1,3]),
  step(2,'Neue freie Adern zuerst nach [[6]] prüfen. Nach Löten direkte Kontakt-zu-Anschluss-Verbindung messen; Kontaktprobe vor und nach der Reihe. Bei LEDs/Widerständen oder Elektronik im Pfad keine einfache Kabelmessung unterstellen.'),
  step(3,'Lupe: keine Zinnbrücke, Litzenfäden, lose Lötperlen, gequetschte Isolation oder Kontakt zur alten 62762. Halter, Befestigungsstellen und vollständig geschlossenen Dachraum berücksichtigen. Drehgestelle und Deichseln in alle normalen Endlagen bringen.'),
  note('Durchgang ist nur zwischen den ausdrücklich vorgesehenen Endpunkten verlangt. Ein bestückter Querpfad kann über Dioden/Kondensatoren leiten; dafür keinen erfundenen OL-Sollwert verwenden. Unklare Messung durch Abtrennen der eigenen neuen Litze auf den passiven Teil eingrenzen.','MESSGRENZE'),
  small('Kopf/Wagen ______; Verbindung/Fotos ______; Kontaktkontrolle vorher/nachher ______; Montage und Bewegung ______; Abweichung/Korrektur ______.')]
 for n in [16,17]:
  for k in ['before','goal','check']:
   if k in P[n]:P[n][k]=P[n][k].replace('mit LoDi verbunden','mit dem Decoderträger verbunden').replace('von LoDi','vom Decoderträger')
  for b in P[n]['blocks']:
   if 'text' in b:b['text']=b['text'].replace('von LoDi getrennt','vom Decoderträger getrennt')
 for b in P[28]['blocks']:
  if b.get('label')=='2.':b['text']='Die Sollfunktion vom vorderen B/RT-Abzweig und vom GE-Schließerkontakt des Lichtrelais fortschreiben. Enden als RT-1, GE-1, RT-2, GE-2 dokumentieren. Dafür müssen die Kupplungsteile vollständig von Platinen und Relais getrennt sein.'
  if b.get('label')=='STOPP':b['text']=b['text'].replace('L gegen O','L gegen B/O')
 # A sources footer must point to both actual source pages.
 P[30]['blocks'][1]['text']='Vorhandene Feder in ihre dokumentierte, passende Originalaufnahme einsetzen und mit der vorgesehenen Befestigung sichern. Sie muss die vorgesehene Achs-/Radfläche berühren; freie Radbewegung prüfen. Nicht direkt an der Achse löten und die Feder nicht zum Kaschieren eines Kontaktfehlers verbiegen. Anschließend die positiven Kontaktmessungen durchführen.'
 P[39]['before']='Paarabnahme [[14]] bestanden. Relaiskarte [[32]] vorbereitet und deren Betriebskontrolle bestanden. Wagen [[27]]–[[30]] stromlos geprüft. Jetzt zuerst den begrenzten Erstwagenversuch, anschließend jede reale Laststufe nach dieser Karte prüfen.'
 P[40]['before']='Einzeltests [[36]]/[[37]] und Paarabnahme [[14]] bestanden; Wagen [[27]]–[[30]] passiv geprüft, örtliche Radkontakte an O. Begrenzter Erstwagenversuch [[39]] bestanden; Prüfbereich [[38]] geklärt. Betriebsausgang, Fahrstufe 0, Puffer ab.'
 P[7]['check']='Neue Verbindungen und Halterung sind geprüft. Programmieraufbau [[8]], Checkliste [[33]] sowie spätere Einzeltests [[36]]/[[37]] in der angegebenen Folge ausführen; keine Prüfung vorweg als bestanden markieren.'
 for b in P[1]['blocks']:
  if b.get('type')=='table':b['rows'][-1][1]='[[44]]–[[47]]'
 for b in P[3]['blocks']:
  if b.get('type')=='small':b['text']=b['text'].replace('GFP3-Daten:','<br/>GFP3-Daten:')
 P[33]['blocks'][0]['rows'][2][0]='Vorn Schleifer/RT zu B/GR; hinten nur RT zu B/GR und alter Schleifer isoliert; beide Köpfe Radkontakt zu 0/GL.'
 for n in [10,11,12,13]:P[n]['phase']='Programmierung | vor Wagenanschluss'
 for b in P[2]['blocks']:
  if b.get('type')=='p' and b['text'].startswith('<b>Arbeitsplatz:'):
   b['text'] += ' Für die Prüfungen: 1 kΩ/2 W (5 %), 10 kΩ/0,5 W sowie eine getrennte kleine Batterie mit dazu passendem Prüflämpchen.'
 for b in P[31]['blocks']:
  if b.get('label')=='1.':b['text']='Auf dem Windows-PC in mDT3 <b>Sound → Soundbibliothek → vom Märklin-Server laden…</b> ausführen [Q22]. Einstellungen des 60977 sichern; sie enthalten keine Audiodaten. Arbeitsprojekt <b>mSD3 – Spur H0</b> anlegen. Unter <b>Sound-Auswahl</b> einen Fahrsound anlegen und links einen ausdrücklich als <b>ICE 1 / BR 401</b> beschriebenen Eintrag suchen; per Drag-and-drop zuordnen. Namen/Bibliotheksstand notieren. Zusatzgeräusche hinzufügen, Funktionen zuordnen. Die Tabelle und Schritt 2 vor Übertragung einstellen; mfx aktiv, Anfangslautstärke niedrig. Projekt speichern, dann bewusst Sounds/Einstellungen/beides übertragen und Einstellungen kontrollieren. Fehlt der passende Eintrag, Download prüfen; der allgemeine 60977-Werkssound dient vorläufig nur dem Lautsprechertest, nicht als bestätigter ICE-1-Sound.'
  if b.get('label')=='3.':b['text']='AUX1 ist verstärkt; dafür keinen CV51-Bit4-Eingriff vornehmen. Eine Motorumkehr über CV51 Bit 0 bleibt ausschließlich der Diagnosefall auf [[36]]. Bei späterer reiner Klangänderung „nur Sounds“ übertragen, Motorwahl und Mapping danach kontrollieren.'
 P[31]['sources']=list(dict.fromkeys(P[31]['sources']+['Q22']))
 for b in P[32]['blocks']:
  if 'text' in b:b['text']=b['text'].replace('<b>Hauptkandidat:</b>','<b>Vorgesehenes Modul:</b>')
 for b in P[38]['blocks']:
  if b.get('label')=='1.':b['text']+=' Danach RT stromlos wiederanschließen und die Verbindung prüfen; die hintere Schleiferlitze bleibt isoliert.'
