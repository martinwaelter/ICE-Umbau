from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'Arbeitsstand_REV10'
IMG=OLD/'bilder'
NEW=ROOT/'bilder_quellen'
PAGES={}
def p(t):return {'type':'p','text':t}
def h(t):return {'type':'h','text':t}
def small(t):return {'type':'small','text':t}
def step(n,t):return {'type':'step','label':str(n)+'.','text':t}
def note(t,label='STOPP',tone='stop'):return {'type':'note','label':label,'text':t,'tone':tone}
def tab(headers,rows,widths=None):return {'type':'table','headers':headers,'rows':rows,'widths':widths or [1]*len(headers)}
def fig(kind,height=180):return {'type':'figure','kind':kind,'maxh':height}
def photo(path,maxh=200,crop=None,marks=None):
 d={'type':'figure','path':str(path),'maxh':maxh}
 if crop:d['crop']=crop
 if marks:d['marks']=marks
 return d
def cols(left,right,widths=[1,1],gap=16):return {'type':'columns','columns':[left,right],'widths':widths,'gap':gap}
def page(n,title,phase,goal,before,blocks,check='',sources=[]):
 PAGES[n]={'n':n,'title':title,'phase':phase,'goal':goal,'before':before,'blocks':blocks,'check':check,'sources':sources}

page(1,'ICE 2976: der Umbau Schritt für Schritt','Start | REV11',
 'Bebilderte Werkstattanleitung mit Märklin-Sound, automatisch folgendem Gegenkopf und getrennt schaltbarem Innenlicht. Überarbeitet aus deiner REV10.', '',[
 fig('system',193),
 small('Funktionsübersicht des vorgesehenen Aufbaus. RT und GE sind Funktionsnamen; Kabelfarben und Kontaktpositionen werden am Fahrzeug zugeordnet.'),
 tab(['Arbeitsabschnitt','Seiten','Abschluss'],[
 ['Vorbereiten und Decoder prüfen','2-9','Einzelaufnahmen, Masterdaten und gemeinsamer mfx-Test'],
 ['Motor, Platinen, Fronten montieren','10-20','Mechanik und eindeutige Anschlusszuordnung'],
 ['Leitungen und Wagen prüfen','21-26','Einzeladern, bestückte Netze und Kupplungen'],
 ['Konfiguration und Erststrom','27-33','Zulässige Lasten, richtiger Sitz, einzelne Köpfe'],
 ['Zug und geschlossenes Gehäuse','34-37','T1-T9, Bewegungsprüfung und Endabnahme'],
 ['Fehler, Wartung, spätere Ergänzungen','38-40','Gezielte Hilfe und Quellen']],[1.8,.45,2.7]),
 p('<b>So arbeitest du:</b> Eine Karte vollständig lesen, dann die nummerierten Handgriffe ausführen und das Ergebnis notieren. Seitenverweise sind anklickbar. „Vorwärts“ bedeutet immer: Motortriebkopf fährt voraus. „Motorloser Kopf“ bezeichnet den hinteren ESU-Kopf.'),
 note('Die gedruckte Anleitung enthält noch keine Messwerte deiner Bauteile. Offen sind insbesondere Master-/ESU-Nachweis, reale Platinen- und Halterdetails sowie LED- und Messdaten. Die betroffene Karte nennt, was zuerst festzustellen ist. Nie einen Beispielwert als eigenen Messwert übernehmen.','NOCH AM EIGENEN ZUG ZU KLÄREN'),
 p('Der Eigenweg benötigt keinen Händler. Herstellerunterlagen, eigene Fotos, definierte Messungen und protokollierte Tests entscheiden über den nächsten Schritt. Vor dem elektrischen Zugumbau den Decoder-Vorabtest auf [[9]] abschließen. Lose Teile, äußere Merkmale und Software kannst du vorher dokumentieren.')
 ],sources=['Q1','Q3','Q7'])

page(2,'Teile zuordnen und Arbeitsplatz einrichten','Vorbereitung',
 'Lege die Baugruppen getrennt nach Motorseite, Gegenkopf und Mittelwagen bereit. Diese Tabelle ist keine zusätzliche Einkaufsliste.', '',[
 tab(['Ort','Teile im gewählten Aufbau','Vor Verwendung prüfen'],[
 ['Motorseite','60941; 60977; LoDi 511; ein Lautsprecher aus 60977','Satz vollständig; rote Platinenrevision; Lautsprecher/Stecker'],
 ['Gegenkopf','59649 LokPilot 5 M4 MKL; leerer Märklin-Träger samt Halteplatte aus 60977','Artikel, beide Trägerseiten, Index und Befestigung'],
 ['Beide Fronten','Zwei LoDi-514-Einsätze; hinten zwei Serienwiderstände','Plus/Weiß/Rot; Zweigdaten und Widerstände nach [[18]]'],
 ['Mittelwagen','Je eine passende LoDi-WiB ICE-M; Originalkupplungen','Abgebildet: MT-37700 V4.3. Anzahl und Passung am eigenen Wagen'],
 ['Programmierung','CS3; Märklin 60971 für 60977; Windows mit ESU-Software','ESU nie am 60971 aufstecken. Einzelaufnahmen nach [[4]]'],
 ['Später','Zwei vorhandene 60974 bleiben jetzt abgetrennt','Ein späterer Puffer vorn braucht den Anschlussnachweis [[39]]']],[.85,2.1,1.9]),
 h('Werkzeuge griffbereit'),
 p('Nichtleitende Unterlage, helle Lampe/Lupe, Kamera, geordnete Schraubenablage, passende Schraubendreher, regelbare Elektronik-Lötstation, feine Spitze, Elektroniklot, Entlöthilfe, Pinzette, flexible Litze und passende Schrumpfschläuche. Dazu Elektronik-Multimeter mit Geräteanleitung und kleine isolierte Prüfclips. Keine unbekannte Messspannung an LEDs oder Platinen verwenden.'),
 step(1,'Fotoordner „ICE2976_REV11“ anlegen. Je Baugruppe Artikel, Revision, Anschlüsse und Schraubenlage aufnehmen. Dateien mit Karte und Bauteil benennen, z. B. „LoDi_beschriftete_Seite“. Scharfe Gesamtansicht plus Nahaufnahme sichern.'),
 step(2,'Geräteliste ausfüllen: CS3-Version/Netzteil ______; Multimeter/Handbuch ______; Märklin-Werkzeug ______; Windows/ESU-Version ______; Prüfaufnahme(n) ______; MS/Gleisbox/Netzteil ______.'),
 note('E395640/E395660 und E374340/E374060 stammen als Kupplungskandidaten aus verwandten Modellen. Aufnahme, Rastung, Endprofil und Beweglichkeit deines 2976 zuerst vergleichen; keine Passung erzwingen.','KUPPLUNGEN'),
 p('Unbekannte Stellen nur dokumentieren. Unlesbare Aufdrucke mit seitlichem Licht erneut fotografieren. Keine Abdeckung abhebeln, keinen Stecker abschneiden und keine Leiterbahn auf Verdacht trennen.')
 ],'Bauteile und Geräte sind eindeutig bezeichnet; die offenen Daten stehen bei der zugehörigen Karte.',sources=['Q1','Q2','Q3','Q4','Q6'])

page(3,'Netze unterscheiden, Multimeter vorbereiten','Vorbereitung',
 'Diese Grundregeln gelten bei jeder Messung und jedem Anschluss.', '',[
 fig('nets',149),
 tab(['Bezeichnung','Gemeint ist','Verwechslung vermeiden'],[
 ['B / RT','Roh-Digitalsignal vom Mittelschleifer','Kein U+ und kein Lichtausgang'],
 ['0 / Radmasse','Rückleiter über Räder/vorgesehene Metallkontakte','Kein Elektronik-GND'],
 ['U+ / +Ub','Gleichgerichtetes Funktionsplus des jeweiligen Decoders','Nicht mit anderem Decoder-U+ verbinden'],
 ['GND','Interner Elektronikminus','Kein braunes Fahrzeugkabel allein aufgrund der Farbe']],[.9,1.8,2.2]),
 step(1,'Fahrzeug vom Gleis nehmen; alle Versorgungen und den Wagenbus physisch trennen. Decoder und beide 60974 entfernen. Vor Ω-/Diodenmessungen Restenergie nach Geräte-/Bauteilanleitung ausschließen. Kondensatoren nicht mit Draht oder Schraubendreher kurzschließen.'),
 step(2,'Schwarz in COM, Rot in V/Ω stecken. Widerstandsbereich wählen. Spitzen zusammen: niedrigen Leitungswert notieren. Spitzen getrennt: die tatsächliche Offenanzeige des Geräts notieren (meist OL). Diese beiden Kontrollen vor und nach einer Reihe durchführen.'),
 step(3,'Kontakt zusätzlich am Bauteil prüfen: Zwei sichere Punkte desselben Leiters müssen vor und nach der Isolationsmessung verbunden sein. Ein Piepton allein genügt nicht; Lack, Kunststoff und lose Clips können scheinbar gute OL-Werte erzeugen.'),
 note('Keinen 250-/500-V-Isolationstester benutzen. Im Strombereich niemals direkt zwischen B und 0 messen. Nach einer Strommessung Rot wieder in V/Ω zurückstecken.'),
 p('<b>Beschriften:</b> B, 0, M1, M2, U+, W, R und GE sind Arbeitsnamen. W/R meint die LED-Farbe. Märklin-Orange kann U+ sein, ESU/NEM-Orange ein Motoranschluss; deshalb immer Anschlussziel und tatsächliche Litzenfarbe gemeinsam notieren.')
 ],'Gerät, Bereich, Kurz-/Offenanzeige und sichere Kontaktpunkte sind bekannt.',sources=['Q1','Q6','Q8'])

page(4,'Prüfaufnahme und genau eine Gleisquelle','Vorbereitung',
 'Die lose Decoderprüfung findet vor dem Zugumbau statt. Eine passende 21MTC-Buchse allein bestätigt die Aufnahme noch nicht.', '',[
 fig('fixture',159),
 tab(['An der tatsächlichen Aufnahme festlegen','Eintragen / abgleichen'],[
 ['Artikel, Revision, Decoder und Index','____________________________'],
 ['Quelle, Anschlüsse und Schalterstellungen','____________________________'],
 ['Motorlast / DCC-Quittierung','____________________________'],
 ['AUX3/AUX4: Logik oder verstärkt','59649 MKL: verstärkt; Monitore müssen passen'],
 ['Lautsprecher: Impedanz und Belastbarkeit','____________________________'],
 ['Zulässige Testlast / Begrenzung / Abschaltwert','____________________________']],[1.15,1.5]),
 p('<b>Bestand prüfen:</b> Märklin 60970 dokumentiert Umschalter für Logik/verstärkt, Motor/Funktion und Lautsprecher. Beim ESU 53900 unterscheiden sich Herstellerangaben zu Lautsprecher und Impedanz je Quelle/Ausführung. Keinen davon ungeprüft anschließen oder vorsorglich kaufen. Die tatsächlichen Schalterbilder mit der passenden Originalanleitung abgleichen.'),
 note('60977: bis 1,6 W an 8 Ω; die 53900-Anleitung nennt einen 0,5-W-Prüflautsprecher. Passende Impedanz gibt keine volle Lautstärke frei. AUX3/AUX4 eines MKL nicht an einen ungeklärten Logikmonitor anschließen.','LASTEN'),
 step(1,'Getrenntes Gleis/Prüfplatz vorbereiten. CS3-Automatik aus, Fahrstufe 0. Programmer, Betriebsgleis und Gleisbox dürfen nie gleichzeitig mit derselben Aufnahme verbunden sein. Zum Umstecken ausschalten und die bisherige Quelle vollständig abtrennen.'),
 step(2,'Für Einzelprogrammierung nur einen Decoder anschließen. Für den Paartest zwei geeignete getrennte Aufnahmen bzw. gleichwertig dokumentierte Aufbauten mit eigenen Lasten verwenden. Genau eine Quelle speist beide Gleiseingänge.'),
 p('<b>Im späteren Zug:</b> Der RT-Bus verbindet beide Schleifer. Der ganze Zug bleibt auf einem einzigen freigegebenen Stromkreis; keine Grenze zu Programmiergleis, anderem Booster, Brems-/Analogabschnitt überbrücken. Erst den vollständigen Zug stromlos umsetzen.')
 ],'Die sechs Felder sind für die tatsächlich verwendete Aufnahme geklärt. Ein eigener 53451 ist erst bei konkretem Kommunikations- oder Firmwarebedarf zu entscheiden.',sources=['Q1','Q6','Q17','Q18','Q19'])

# Five compact cards from the independently drafted module.
mod=json.loads((ROOT/'programming_module.json').read_text())
sm={'S01':'Q1','S02':'Q15','S03':'Q14','S04':'Q14','S05':'Q7','S06':'Q12','S07':'Q11','S08':'Q13','S09':'Q9','S10':'Q6','S11':'Q17','S12':'Q16','S13':'Q7'}
for idx,item in enumerate(mod['pages'],5):
 def fix(t):
  for n in range(1,6): t=t.replace('P'+str(n),'[['+str(n+4)+']]')
  t=t.replace('<CS3-IP>','&lt;CS3-IP&gt;')
  t=t.replace('Die tatsächliche 59649-Firmware ist dokumentiert und für die Funktion geprüft.','Der tatsächliche Firmwarestand ist dokumentiert; eine ausdrücklich gemeldete Updateanforderung muss vorher geklärt sein.')
  return t
 blocks=[step(n+1,fix(t)) for n,t in enumerate(item['steps'])]
 if idx==6:
  blocks[1]['text']+=' Zur Kontrolle der Bytefolge zusätzlich eine unsymmetrische Seriennummer ausschließlich offline verwenden; deren vier Bytewerte müssen unterscheidbar sein.'
  blocks.append(small('JMRI-Zusammensetzung: S = CV192 + 256 × CV193 + 65.536 × CV194 + 16.777.216 × CV195. Das erklärt die Bytefolge; die vollständige Aktivierung muss der Originalexport zeigen.'))
 blocks.append(tab(item['table']['headers'],item['table']['rows']))
 blocks.append(note(fix(item['stop'])))
 if idx==9:
  blocks[-2]=tab(['F0 / Richtung bei Fahrstufe 0','60977 LV / LR','59649 LV / LR'],[['aus / vorwärts','aus / aus','aus / aus'],['aus / rückwärts','aus / aus','aus / aus'],['an / vorwärts','an / aus','an / aus'],['an / rückwärts','aus / an','aus / an']],[1.4,1,1])
  blocks.append(small('Späteres Frontbild: vorwärts Motor weiß / Gegenkopf rot; rückwärts umgekehrt. Hier werden zuerst die physischen LV/LR-Ausgänge der Aufnahmen geprüft.'))
 page(idx,item['title'],'Decoder-Nachweis | vor dem Zugumbau',fix(item['goal']),fix(item['before']),blocks,fix(item['check']),list(dict.fromkeys(sm[s] for s in item['source_refs'])))

page(10,'Alte Elektrik ausbauen, 60941 montieren','Motorseite | mechanischer Aufbau',
 'Das eigene Ausgangsfoto zeigt noch Feldspule und lange Altplatine. Die Herstellerzeichnung darunter erklärt die Teile des neuen Motors.',
 'Decoder-Vorabtest [[9]] bestanden. Kopf vom Gleis und Bus getrennt; beide Decoder/Puffer entfernt.',[
 photo(IMG/'0D2DC2F3-025D-48F9-8454-50A792498AD1_4_5005_c.jpeg',94),
 small('Eigenes 2976-Ausgangsfoto aus REV10. Verdeckte Kontakte sind darauf nicht vollständig erkennbar.'),
 photo(ROOT.parent/'Pruefnachweise/REV9_Berichtsabgleich/Maerklin_60941_Zeichnung.png',180,[.10,.02,.90,.63]),
 small('Märklin 60941, Originalzeichnung: 1 Magnet, 2 Rotor, 3 Motorschild, 4 Schrauben, 5 Bürsten, 6 Drosseln. Bauteilnummern sind keine Handgriffnummern.'),
 step(1,'Gehäuse an den tatsächlichen Befestigungen lösen, ohne an Litzen zu ziehen. Schrauben mit Einbauort ablegen. Beide Seiten, Unterseite, alte Lampenfassung, Schleifer- und Radkontakte fotografieren. Jeden Draht bis zu seinem Ziel verfolgen.'),
 step(2,'Alte Platine/Umschalter und ersetzte Lampenfassungen an ihren Lötstellen abtrennen, ausbauen und beschriftet aufbewahren. Unbekannte Leiterbahnen nicht aufschneiden. Die alte Lampenfassung wird nicht als neue LED-Lötstütze verwendet.'),
 step(3,'Bürstenfedern kontrolliert entlasten, Bürsten entnehmen. Motorschild und Feldspule ausbauen; Rotor-, Lager- und Scheibenlage dokumentieren. Permanentmagnet, fünfpoligen Rotor und neues Schild passend einsetzen. Teile müssen ohne Druck in die vorhandenen Sitze passen.'),
 step(4,'Zugehörige Schrauben schrittweise sicher anziehen. Nach jeder Schraube vorsichtig Beweglichkeit prüfen; nicht über die Räder gewaltsam zurückdrehen. Bürsten frei einsetzen und Federn so auflegen, dass sie weder Nachbarfahne noch Metallrahmen berühren.')
 ],'Kein harter Anschlag oder starkes Klemmen. Keine Testfahrt, kein Analogtrafo und keine Einmessfahrt. Nächster Schritt: Entstörung und vollständig getrennte Motorprüfung.',sources=['Q1','Q2','Q6'])

motor_a_marks=[[1,.439,.279,.215,.08],[2,.641,.508,.865,.677],[3,.482,.442,.466,.805],[4,.523,.252,.62,.065]]
page(11,'Kondensatoren unterscheiden, Drosseln einbauen','Motorseite | Entstörung',
 'Die Anschlussenden entscheiden über die Funktion. Gleich aussehende Bauteile dürfen nicht gemeinsam abgeschnitten werden.',
 'Motor montiert; Motorleitungen noch nicht mit LoDi verbunden. Decoder und Puffer bleiben entfernt.',[
 photo(NEW/'motor_a_2048.jpg',188,marks=motor_a_marks),
 small('LoDi-Vergleich 33701 vor Anpassung, kein Foto deines 60941. Nase links. Originalfoto mit Prüfmarkierungen; keine gemessenen Fehler deines Zuges.'),
 tab(['Bildnummer','Prüfen und behandeln'],[
 ['1 und 2','Beide Drähte der äußeren Kondensatoren verfolgen. Bürste zu Rahmen/Masseöse: diesen Kondensator am abgetrennten Motor gezielt auslöten. Radmasseleitung erhalten.'],
 ['3','Quer-Kondensator zwischen M1 und M2: nur den tatsächlich vorhandenen, eindeutig zugeordneten und geeigneten belassen. Bei fehlendem/unklarem Bauteil keinen Wert erfinden oder blind nachrüsten.'],
 ['4','Drosseln liegen in den Motorleitungen; keine LED-Widerstände. Jeden Anschluss bis zum Motor bzw. freien Litzenende verfolgen.']],[.55,3.8]),
 step(1,'Gelieferten Motorschildzustand mit Foto festhalten: vorhandener Kondensator, beide Enden und Kennzeichnung. Die 60941-Beilage liefert keinen allgemein einzusetzenden Kondensatorwert. Verdeckte Enden zuerst sichtbar machen.'),
 step(2,'Je eine mitgelieferte Drossel in jeden Motorzweig einfügen: <b>M1 - Drossel 1 - Litze 1</b> und <b>M2 - Drossel 2 - Litze 2</b>. Kein Drosselende an Masse; keine Drossel quer zwischen beiden Bürsten.'),
 step(3,'Schrumpfschlauch vorher auffädeln. Blankstellen einzeln isolieren, nach Abkühlen festen Sitz prüfen. Beide Zweige endgültig verlegen, mit Bewegungsschlaufe; ihre freien Enden bleiben einzeln isoliert und von LoDi getrennt.'),
 note('Ein Masse-Kondensator kann nach kurzem Laden im Ohmtest OL anzeigen. Deshalb zusätzlich beide Drähte mit Lupe verfolgen. Keine allgemeine nF-Nullprüfung verwenden.')
 ],'Beide vollständigen Zweige sind montiert und noch frei. Jetzt [[12]] und [[13]] zuerst an den Bürsten, danach an den freien Litzenenden durchführen.',sources=['Q2','Q3','Q6'])

motor_c_marks=[[1,.329,.334,.186,.075],[2,.367,.356,.555,.075],[3,.271,.328,.17,.674],[4,.433,.554,.554,.822]]
page(12,'Motorprüfung: vier Clips sicher anbringen','Motorseite | Messaufbau',
 'Die Fahrzeugclips bleiben während jeder Messreihe fest. Umgesteckt wird nur an den freien Enden der Hilfsleitungen.',
 'Motor einschließlich Drosseln/Litzen vollständig von LoDi und alter Elektrik getrennt; Kopf auf nichtleitender Unterlage. Messgerät nach [[3]] geprüft.',[
 photo(NEW/'motor_c_2048.jpg',184,marks=motor_c_marks),
 small('LoDi-Vergleich 33701 nach Anpassung. 1 = Bürstenfahne M1; 2 = Bürstenfahne M2. 3/4 sind mögliche Metallbezüge; ihre Verbindung erst nachweisen. Braun beweist keine Radmasse.'),
 step(1,'Vier isolierte Hilfsleitungen einzeln Ende-zu-Ende prüfen. Widerstände notieren. <b>PM1</b> nur an Bürstenfahne M1, <b>PM2</b> nur an Bürstenfahne M2 klemmen. Kein Clip darf gleichzeitig Schildschraube, Feder oder Rahmen greifen.'),
 step(2,'Für genau eine Gegenstelle X zwei sichere Punkte desselben Pfads wählen: <b>PX</b> an den ersten, <b>PX2</b> an den zweiten. Die beiden Punkte müssen positiv als verbunden nachweisbar sein. Zu große Clips ersetzen; keine lose Spitze in den engen Bürstenbereich drücken.'),
 tab(['Gegenstelle X - jede einzeln prüfen','Geeignete Paarbildung'],[
 ['Chassis','Zwei blanke Stellen desselben Metallteils, nicht zwei unklare Schraubenköpfe'],
 ['Motor-Metallrahmen','Zwei sichere blanke Rahmenpunkte; nicht pauschal mit Chassis gleichsetzen'],
 ['Radmasse / Gleis 0','Bestätigter Anschluss und zugehörige leitende Radfläche'],
 ['Mittelschleifer / Gleis B','Blanker Schleifer und seine abgetrennte Anschlusslitze']],[1.2,2.2]),
 step(3,'PM1/PM2/PX/PX2 beschriften und freie Enden einzeln gegen Berührung sichern. Die ganze Sechserfolge auf [[13]] ausführen. Für eine neue Gegenstelle PX/PX2 neu bestimmen und wieder mit den positiven Kontrollen beginnen.'),
 note('Sind zwei zugehörige Punkte nicht eindeutig erreichbar, ist diese Messung offen. Kein scheinbares OL notieren und keine Brücke zwischen B und 0 herstellen.')
 ],'Alle vier Clips sitzen allein am vorgesehenen Punkt; Hilfsleitungen und Bezugspfad lassen sich positiv prüfen.',sources=['Q2','Q3','Q6'])

page(13,'Motorprüfung: diese sechs Messungen wiederholen','Motorseite | Messkarte',
 'Eine Messreihe umfasst immer Vorproben, beide Isolationswerte und Nachproben. Das gilt auch nach jeder Lage- oder Kontaktänderung.',
 'Aufbau [[12]]. Schwarz in COM, Rot in V/Ω; Ω-Autorange oder höchster Widerstandsbereich. Clips am Motor bleiben fest.',[
 tab(['Nr.','Rot / Schwarz am freien Ende','Erwartung'],[
 ['1','PX2 / PX','Niedriger, reproduzierbarer Wert des bestätigten Bezugspfads.'],
 ['2','PM1 / PM2','Bleibender endlicher Motorwiderstand nach möglichem Ladeeffekt. Ein kurzer Ausschlag genügt nicht.'],
 ['3','PM1 / PX','Nach stabiler Anzeige: bestätigter Offenwert/OL. Bleibende Zahl = nicht bestanden.'],
 ['4','PM2 / PX','Eigener Offenwert/OL. Eine bestandene Bürste ersetzt die andere nicht.'],
 ['5','PX2 / PX','Positive Referenzprobe aus 1 muss weiterhin stimmen.'],
 ['6','PM1 / PM2','Bleibender Motorpfad aus 2 muss weiterhin messbar sein.']],[.3,1.45,2.6]),
 step(1,'Zunächst die sechs Werte an den Bürstenfahnen erfassen. Dann PM1 und PM2 an die freien Enden der fertig verlegten Motorlitzen setzen und alles wiederholen. So werden auch beide Drosseln, Lötstellen und Litzen geprüft.'),
 step(2,'Für Chassis, Motorrahmen, Radmasse und Schleifer getrennte Reihen durchführen. Rotor vorsichtig in mehrere Stellungen bringen und Drehgestell in die normalen Endlagen bewegen. Nach jeder Änderung vollständige Sechserfolge; Getriebe nicht erzwingen.'),
 tab(['Messort / Lage / Gegenstelle','1 / 2 vorher','3 / 4 Isolation','5 / 6 nachher'],[
 ['Bürsten / __________','____ / ____','____ / ____','____ / ____'],
 ['Bürsten / __________','____ / ____','____ / ____','____ / ____'],
 ['Litzenenden / ______','____ / ____','____ / ____','____ / ____'],
 ['Litzenenden / ______','____ / ____','____ / ____','____ / ____']],[1.4,1,1,1]),
 small('Diese Karte für weitere Gegenstellen/Lagen kopieren. Gerät/Bereich ______; Datum ______; Fotos ______. Kein allgemeiner Grenzwert wie 0,3 Ω: Messleitungen und tatsächlichen Pfad berücksichtigen.'),
 note('Ist Vor-/Nachprobe offen, sind die dazwischenliegenden OL-Werte ungültig. Kontaktfehler beheben, ganze Reihe neu. OL in einer Motorstellung nicht durch Weiterdrehen als erledigt behandeln.'),
 p('<b>Bei endlichem Isolationswert:</b> Versorgung getrennt lassen. Nacheinander Litzen/Blankstellen, Bürstenfedern, Kondensatorenden und Schraubenlage prüfen. Wird der Fehler beim Lösen einer Schraube unsichtbar, Schaftlänge und Berührung korrigieren; nicht locker weiterfahren. Danach komplett wiederholen.')
 ],'Alle erforderlichen Reihen bestanden, beide Drosselzweige eingeschlossen. Hilfsleitungen entfernen. Motor erst nach eindeutiger Padzuordnung [[16]] anschließen.',sources=['Q1','Q2','Q6'])

redmarks=[[1,.45,.584,.5,.44],[2,.32,.289,.77,.32],[3,.825,.674,.66,.745],[4,.775,.827,.44,.865],[5,.126,.206,.23,.105],[5,.846,.916,.67,.967]]
page(14,'Deine rote LoDi-Platine richtig erkennen','Motorseite | Platinenzuordnung',
 'Das Originalfoto bleibt groß. Die beschriftete Gegenseite und die tatsächliche Revision müssen zusätzlich vorliegen.',
 'Lose stromlose Platine, kein Decoder. Keine Jumper verändern und keine schwarze Steckerstruktur entfernen.',[
 cols([photo(IMG/'image-2.jpg',493,marks=redmarks),small('Eigenes Foto aus REV10; ergänzte Nummern. Oben/unten gilt nur für diese Ansicht.')],[
 p('<b>1 - 21MTC:</b> Steckfeld für 60977. Die schwarze Struktur ist nicht sicher als Kappe identifiziert. Tatsächlichen Index erst auf [[30]] abgleichen.'),
 p('<b>2 - K1:</b> unbestücktes Relaisfeld. Hier weder Puffer noch vierpoligen Stecker anschließen. Fehlendes Relais beweist allein keinen SW/RT-Durchgang.'),
 p('<b>3 - LS1 / LS2:</b> ausschließlich Lautsprecheradapter. Kein Anschluss an Masse oder LED-Plus.'),
 p('<b>4 - R3 bis R6:</b> für LED-Betrieb R4/R5 nicht überbrücken. R3/R6 nicht entfernen oder nach Foto verändern; Bestückung und Zweigzuordnung dokumentieren.'),
 p('<b>5 - Befestigungsringe:</b> Ring A beim K1-Ende, Ring B beim Widerstands-/Frontende benennen. Netz und zulässige Montage je Ring auf [[15]] bestimmen.'),
 h('Rote Platine umdrehen'),
 p('Ganze beschriftete Seite senkrecht fotografieren. Revision, SW, RT, GE, MASSE, MOT_L/R, Front-VCC, L_WS/L_RT sowie vorhandene SJ1/SJ2 müssen lesbar sein. Nicht das fremde Bild auf [[16]] spiegeln.'),
 tab(['Rote Motorplatine','Innenlicht'],[
 ['V1.49, Pfad tatsächlich bestätigt','AUX4'],
 ['ab V1.50: nur SJ1 zu','AUX4'],
 ['ab V1.50: nur SJ2 zu','AUX1'],
 ['beide offen / unklar','Zuordnung offen'],
 ['beide geschlossen','Nicht bestromen']],[1.7,.9]),
 p('<b>Eintragen:</b> Revision ______; SJ1 ______; SJ2 ______; SW/RT-Pfad ______; GE-Ausgang ______. Bei unklarer Brücke Makrofoto und revisionspassende Herstellerzuordnung verwenden.')
 ],[.9,2.1]),
 note('SJ2 der <b>weißen</b> MT-37700 V4.3 ist Türbeleuchtung. Diesen Zustand erhalten; er wählt keinen Decoder-AUX. Zwei geschlossene Auswahlbrücken auf der roten Platine können Decoder-Ausgänge verbinden.')
 ],sources=['Q3','Q4','Q8'])

page(15,'LoDi befestigen: beide Haltepunkte prüfen','Motorseite | mechanische Befestigung',
 'Eine Schraube darf nur die dafür vorgesehenen Flächen berühren. Ein sichtbarer Kupferring ist nicht automatisch Radmasse.',
 'Rote Revision und Anschlussrollen [[14]] dokumentiert. Decoder, Puffer und Lasten entfernt.',[
 fig('screw',166),
 small('Befestigungsprinzip, keine maßstäbliche 2976-Zeichnung. Ringnetz, Schraubenlänge und konkrete Auflage müssen am eigenen Exemplar stimmen.'),
 step(1,'Platine zunächst lose an den vorgesehenen Auflagen positionieren. Unterseite, gesamte Schrauben-/Scheibenfläche und Schaftweg ansehen. Nur passende vorhandene Schrauben verwenden; keine längeren Schrauben probeweise einsetzen, keine Löcher aufbohren.'),
 step(2,'Ring A am K1-Ende und Ring B am Widerstands-/Frontende auf eigenen Fotos markieren. Revisionsbezogene Herstellerangabe bzw. nachvollziehbar zugeordneter Leiterbahnplan muss je Ring Sollnetz und zulässigen Metallkontakt ergeben. Farbe, Glanz oder ein Piepton allein reichen nicht.'),
 tab(['Montagekarte','Ring A','Ring B'],[
 ['Foto / elektrisches Sollnetz','________','________'],
 ['Quelle der Netzzuordnung','________','________'],
 ['Schraube / Schaftlänge / Auflage','________','________'],
 ['Unterseite / Fremdnetze frei','________','________'],
 ['Vor-/Nachprüfung gemäß [[22]]','________','________']],[1.6,1,1]),
 step(3,'Wenn die originale Montage zur bestätigten Ausführung passt: Platine plan auflegen und Schrauben gleichmäßig sicher anziehen. Nach jedem Haltepunkt auf schiefen Sitz, Berührung und gequetschte Litzen prüfen. Die festgelegten elektrischen Reihen nach [[22]] wiederholen.'),
 step(4,'Wenn die originale Aufnahme nicht passt: Haltergeometrie, Befestigung, sichere Abstände und erforderliche elektrische Ringverbindungen zuerst festlegen. Eine Scheibe unter dem Schraubenkopf isoliert weder automatisch den Schaft noch die Unterseite. Unbekannte Ringkontakte nicht ersatzlos isolieren.'),
 note('Bei ungeklärtem Ringnetz oder fehlender sicherer Befestigung bleibt die Platine unmontiert. Kein Decoder nur auf losen Isolierstreifen und keine durch Litzen gehaltene Platine bestromen.')
 ],'Die offene Montage ist mechanisch und elektrisch geprüft. Die zusätzliche geschlossene Prüfung folgt später auf [[36]]/[[37]].',sources=['Q1','Q3','Q8'])

page(16,'Motorseite: genau diese Anschlüsse benutzen','Motorseite | Verdrahtung',
 'Die Padnamen bestimmen das Anschlussziel. Das Bild zeigt eine beschriftete LoDi-V1.49-Vergleichsplatine und ersetzt den Abgleich deiner Revision nicht.',
 'Motorprüfung [[13]], Padzuordnung [[14]] und Befestigung [[15]] bestanden. Decoder bleibt draußen.',[
 photo(NEW/'lodi_motor_montiert_original.jpg',153),
 small('LoDi / Lokstoredigital, Vergleichsumbau 33701, beschriftete Seite V1.49. Keine ungeprüfte Spiegelung auf das eigene Platinenfoto.'),
 tab(['Aufdruck am eigenen Exemplar','Einzige vorgesehene Verbindung'],[
 ['SW / SCHLEIFER','Örtlicher Mittelschleifer; tatsächlichen SW/RT-Pfad vorher bestätigen.'],
 ['RT / KUPPLUNG','Rohstrompfad zur Kupplung und später zum anderen Schleifer.'],
 ['GE / KUPPLUNG','Geschalteter Wagenlichtpfad; nur hier vorn gespeist.'],
 ['MASSE','Eigene Rad-/Schienenrückleitung, nicht Decoder-GND.'],
 ['MOT_L / MOT_R','Je ein bereits geprüfter Motorzweig mit eigener Drossel.'],
 ['VCC beim Frontanschluss','Gemeinsames Plus des LoDi-514-Einsatzes. Kein Draht zu Chassis, MASSE oder 21MTC-Pin 12.'],
 ['L_WS / L_RT','Weiß / Rot der Front, mit bestätigter vorgesehener Strombegrenzung.'],
 ['LS1 / LS2','Nur die zwei Litzen des Lautsprecheradapters nach [[17]].']],[1.3,2.8]),
 step(1,'Jede freie Einzelader vor dem Anlöten nach [[21]] prüfen und beschriften. Schrumpfschlauch vorher auffädeln, nur nötige Länge abisolieren, Litze bündeln/verzinnen und ohne Zug löten. Kleine Bewegungsschlaufen freihalten.'),
 step(2,'Nach jedem Anschluss abkühlen lassen. Mit Lupe nach Zinnbrücken, Litzenfäden und Lötperlen suchen; festen Sitz vorsichtig prüfen. Betroffene Reihen des ausgefüllten Platinenplans [[22]] wiederholen. Strombegrenzung der Front muss vor LED-Anschluss geklärt sein.'),
 note('K1, PANTO, AUX3, AUX5 und S2 erhalten hier keine neue Leitung oder Brücke. Front-VCC ist der dokumentierte LED-Plusanschluss; interne 21MTC-Vcc ist eine andere Funktion. Kein freies Pin-Abzählen als Anschlussmethode.')
 ],'Jede Leitung stimmt nach Aufdruck, Funktion und Prüfung. Alle unbenutzten Enden sind einzeln isoliert; der Decoder wird erst auf [[30]] eingesetzt.',sources=['Q1','Q3','Q8'])

page(17,'Lautsprecher mit erhaltenem Stecker anschließen','Motorseite | Sound',
 'Ein Lautsprecher aus dem 60977-Satz wird über einen passenden Gegenstecker an LS1/LS2 angebunden.',
 '60977 entfernt; Puffer und Gleis getrennt. LS1/LS2 am eigenen LoDi-Träger sicher identifiziert.',[
 fig('front',187),
 small('Funktionsschema der Motorseite, keine Pad-Lagezeichnung. „Motor“ umfasst beide Drosselzweige; Frontanschlüsse gelten nur mit bestätigter Strombegrenzung.'),
 step(1,'Genau einen unveränderten Original-Lautsprecher aus dem 60977-Satz wählen. Bauform und Schallkapsel müssen druckfrei in den freien Lautsprecherbereich passen. Herkunft und Nennimpedanz aus Setunterlagen sichern; nicht aus einem Ohmmesswert auf die Nennimpedanz schließen.'),
 step(2,'Stecker von Kontaktseite und seitlich fotografieren; Kontaktabstand und Gehäusemaße notieren. Zwei Pole oder weißer Kunststoff bestimmen keinen Steckertyp. Passenden zweipoligen Gegenstecker mit isolierten Litzen eindeutig zuordnen; Originalstecker erhalten.'),
 step(3,'Adapter ohne Decoder und ohne Lautsprecher prüfen: Kontakt 1 bis Litze 1 und Kontakt 2 bis Litze 2 müssen leitend sein; zwischen den beiden getrennten Pfaden darf keine Drahtbrücke bestehen. Positive Kontaktkontrollen vor und nach der Reihe nach [[21]].'),
 step(4,'Je eine Adapterlitze an LS1 und LS2 löten, Blankstellen einzeln isolieren und zugentlasten. Fertigen Adapter und neu angeschlossene Netze nach [[21]]/[[22]] prüfen. Niemals an Membran oder dünnen Lautsprecheranschlüssen ziehen.'),
 step(5,'Schallkapsel sicher befestigen, Membran frei lassen und Dachraum prüfen. Lautsprecher erst nach elektrischer Anschlussprüfung stecken. Der erste leise Soundtest folgt mit dem Motortriebkopf auf [[32]].'),
 note('Beide Lautsprecherdrähte führen ausschließlich zu LS1 und LS2. Keiner an Chassis, U+, VCC, GND oder +5V. Keinen zweiten Lautsprecher parallel anschließen.'),
 p('Eintragen: Lautsprecher/Bauform ______; Impedanzquelle ______; Gegenstecker/Maße ______; Adapterprüfung ______; freie Membran/Schallraum ______; später leiser Funktionstest ______.')
 ],sources=['Q1','Q3'])

page(18,'Front-LEDs: Plus, Farben und Widerstände','Beide Köpfe | Frontlicht',
 'Vorn nutzt LoDi die vorgesehene Strombegrenzung. Hinten benötigt jeder Farbzweig einen eigenen berechneten Serienwiderstand.',
 'Beide Einsätze abgetrennt. Reale Artikel/Revision und sichere LED-Zweigdaten müssen vor Anschluss vorliegen.',[
 cols([photo(NEW/'front_led_kabel_1.jpg',163),small('LoDi-Vergleichsfoto: red / VCC / white. Nur in dieser Fotoansicht; eigene Aufdrucke abgleichen.')],[
 p('<b>Vorn:</b> Plus an Front-VCC; white/Weiß an L_WS; red/Rot an L_RT. Wirksame LoDi-Serienwiderstände zuerst bestätigen, R4/R5 nicht brücken.'),
 p('<b>Hinten:</b> Plus an +Ub. Rot über R Rot an LV; Weiß über R Weiß an LR. Diese Zuordnung setzt F0 vorwärts = LV und rückwärts = LR voraus. Keine zweite Richtungsumkehr einstellen.'),
 p('Diodentest nur mit nachweislich geeigneter Prüfspannung/-strom: Rot an dokumentiertes Plus, Schwarz an zugehörige Kathode. OL kann zu geringe Prüfspannung bedeuten; nicht mit höherer Spannung raten.')
 ],[.8,1.9]),
 fig('led',126),
 tab(['Vor Widerstandsauswahl bestätigen','Weiß','Rot'],[
 ['Zweigaufbau, zulässiger Strom I, Quelle','________','________'],
 ['U maximal am LED-Zweig; U LED minimal','________','________'],
 ['R Nennwert / Toleranz / Belastbarkeit','________','________']],[1.8,.9,.9]),
 p('<b>Berechnen:</b> R mindestens = (U maximal - U LED minimal) / I zulässig. Mit R klein = R Nennwert × (1 - Toleranz) muss die Stromgrenze eingehalten sein. Verlustleistung: P = (U maximal - U LED minimal)² / R klein. Belastbarkeit und Wärmeabstand passend zum realen Einbau wählen.'),
 step(1,'Beide Widerstände einzeln abgetrennt nachmessen; Ω und kΩ unterscheiden. Je Farbzweig einlöten, beide Drahtenden isolieren und Abstand des Körpers zu Kunststoff, LED und Litzen lassen. Noch keine Probe am Gleis.'),
 note('Keine festen Widerstandswerte sind für deine bisher nicht vollständig dokumentierten 514-Zweige freigegeben. Herstellerdaten/Messplan müssen Spannung, Strom und Zweigaufbau klären. PWM-Dimmung ersetzt den Widerstand nicht.')
 ],sources=['Q1','Q3','Q5','Q6'])

page(19,'Motorloser Kopf: Träger und Halter zuordnen','Gegenkopf | mechanischer Aufbau',
 'Der ESU 59649 kommt auf den leeren Märklin-Träger aus dem 60977-Satz. Die alte lange Platine wird dafür nicht weiterverwendet.',
 'Vorabtest [[9]] bestanden; Gegenkopf getrennt, stromlos, Decoder/Puffer entfernt.',[
 cols([photo(OLD/'quellen_alt/tmp/pdfs/rev5/research/dummy_full.jpg',174),small('LoDi-Vergleich 33701. Nase/Lampenende rechts, Kupplung links. Hohe Altstützen sind kein bestätigter Halter für den kleinen Träger.')],[photo(IMG/'ice2976_60977-p5-pads.jpg',174,[.045,.225,.49,.77]),small('Märklin-Originalzeichnung des Trägers, S. 5. Aufdrucke an deinem Exemplar abgleichen.')],[1.35,1]),
 step(1,'Alte Leiterplatte, Lampenfassung und jeden Anschluss vor dem Ablöten fotografieren. Schleiferleitung und Radkontakte getrennt verfolgen. Alte Elektrik/Lampenfassung ausbauen und aufbewahren; keine unbekannten Massefedern entfernen.'),
 step(2,'Leeren Träger und mitgelieferte Halteplatte in der tatsächlichen Einbausituation fotografieren. Träger ohne Decoder trocken positionieren: freier Dachraum, keine Unterseitenberührung, kein Zug an Litzen, freie Drehgestelle und Kupplungen. Nichts bohren oder alte Metallstützen verbiegen.'),
 step(3,'Befestigung vor Montage festlegen: Halteplatte, Ort, Schraubentyp/-länge, zulässiger Sitz und obere/untere Abstände. Reicht der vorhandene Halter nicht, passende isolierende Halterung anhand realer Maße bestimmen. Keine erfundene Ersatzteilnummer; Litzen dürfen den Träger nicht halten.'),
 tab(['Tatsächlicher Aufdruck','Verwendung hinten'],[
 ['B/GR; 0/GL','Schleifer/RT; örtlicher Radkontakt nach [[20]]'],
 ['+Ub; LV; LR','LED-Plus; Rot über Widerstand; Weiß über Widerstand'],
 ['MR/MV, AUX1-AUX4, GND, +5V','Nicht anschließen; vorhandene freie Litzen einzeln isolieren'],
 ['SUSI- und Lautsprecherbuchse','Beide frei lassen; keine Kurzschlussbrücke']],[1.2,2.4]),
 step(4,'Offene Montage vor/nach Befestigung nach [[21]]/[[22]] prüfen. Absichtliche 0/GL-Radmasse nicht als Isolationsfehler bewerten. Geschlossenen Dachraum zusätzlich auf [[36]]/[[37]] prüfen.')
 ],'Träger passt sicher, Aufdrucke stimmen und die Befestigung ist dokumentiert. 59649 bleibt bis [[31]] abgezogen.',sources=['Q1','Q3','Q6','Q8'])

page(20,'Gegenkopf: Schleifer, Rückleiter und LEDs verdrahten','Gegenkopf | Anschlusskarte',
 'S und R werden am tatsächlichen Kopf nachgewiesen. Ein fremdes Foto belegt keinen vorhandenen hinteren Schleifer.',
 'Halter [[19]], LED-Strombegrenzung [[18]] und Kontaktzuordnung [[24]] geklärt. Decoder/Puffer entfernt.',[
 fig('rear',172),
 small('Funktionsschema, keine Lagezeichnung des Trägers. R Rot und R Weiß bedeuten Serienwiderstände; R links bezeichnet die örtliche Radstromaufnahme.'),
 step(1,'Unterseite ansehen: Mittelschleifer zwischen den Rädern suchen. Seine Leitung bis zum Anschluss verfolgen und <b>S</b> nennen. Radstromaufnahme getrennt verfolgen und <b>R</b> nennen. RT und GE der Kupplung über die Kontaktprüfung zuordnen, nicht nach Litzenfarbe.'),
 step(2,'S und R nach dokumentierter Trennung von alter Elektronik einzeln prüfen: S zum tatsächlichen Schleifer, R zum tatsächlich genutzten leitenden Radkontakt. Positive Vor-/Nachkontrollen und normale Drehgestellbewegung nach [[21]]. Bei angeschlossener Elektronik zuerst den Plan [[22]] verwenden.'),
 step(3,'Den isolierbaren Dreiwegpunkt <b>S + RT + Leitung B/GR</b> auf eigenem Foto festlegen. Er muss mechanisch sicher liegen, von Metall frei bleiben und vollständig isolierbar sein. Nicht drei Litzen auf ein zu kleines Pad pressen. Vorher Schrumpfschlauch auffädeln; bündeln, verzinnen und zugfrei löten.'),
 step(4,'R an <b>0/GL</b> anschließen. LED-Plus direkt an <b>+Ub</b>; Rot über eigenen Widerstand an <b>LV</b>; Weiß über eigenen Widerstand an <b>LR</b>. Alte Lampenfeder, Chassisschraube, +5V oder GND nicht als LED-Zwischenanschluss nutzen.'),
 step(5,'GE endet hinten einzeln isoliert. Ebenso jede vorhandene freie Litze von MR/MV, AUX1-AUX4, GND und +5V. Schlauch auch stirnseitig geschlossen und abrutschsicher setzen; keine zwei blanken Enden in denselben Schlauch schieben. Buchsen frei lassen.'),
 step(6,'Nach jedem Anschluss/Umlegen betroffene Prüfungen [[21]]/[[22]] wiederholen. Beide Drehgestell- und Kupplungsendlagen müssen ohne Litzenzug erreichbar bleiben. Lupe: keine Zinnbrücke oder Drähtchen; alle Verbindungen dokumentieren.'),
 note('Fehlt die eigene hintere Stromaufnahme, ist der ungekuppelte Fahrzeugtest nicht möglich. Keine zufällige RT-Speisung als ihren Nachweis verbuchen. Hinten niemals einen Decoder-Ausgang auf GE legen.')
 ],sources=['Q1','Q3','Q6'])

page(21,'Einzelne freie Leitungen sicher prüfen','Elektrische Prüfung | passive Teile',
 'Diese Karte gilt für vollständig getrennte Drähte und passive Kontaktstücke. Eine Platine wird durch Abziehen des Decoders nicht automatisch zu einem Kabel.',
 'Alle Quellen/Bus/Decoder/Puffer getrennt; Restenergie ausgeschlossen. Rot in V/Ω, Schwarz in COM. Gerät nach [[3]] geprüft.',[
 tab(['Reihenfolge','Konkreter Handgriff','Ergebnis'],[
 ['1. Leiter festlegen','Zwei sichere Endpunkte L1/L2 desselben getrennten Leiters wählen. Fremdteil mit zwei Punkten X1/X2 seines bestätigten Metallpfads festlegen.','Fotos/Benennung ______'],
 ['2. Positiv vorprüfen','L1-L2 und X1-X2 messen. Beide müssen den erwarteten stabilen leitenden Pfad zeigen. Clips dann fest lassen.','L ______ / X ______'],
 ['3. Fremdkontakt prüfen','L1 gegen X1 im dokumentierten Ω-Bereich messen. Blanke Kontakte nicht mit Fingern berühren.','Offen/OL ______'],
 ['4. Positiv nachprüfen','L1-L2 und X1-X2 erneut messen. Beide müssen weiterhin stimmen.','L ______ / X ______'],
 ['5. Bewegen','Leitung/Drehgestell/Kupplung in normale Endlagen bringen. Je Lage die ganze Folge wiederholen.','Lage / Ergebnis ______']],[.65,2.4,.9]),
 step(1,'Vorn die noch freien LED-, Lautsprecher-, RT-/GE- und sonstigen neuen Einzeladern gegen Rahmen, Befestigungen und jede relevante Nachbarader prüfen. Hinten freie Plus-/Farbadern, S-/RT-/R-Kabel und GE prüfen. Beide Seiten der Messung müssen jeweils positiv kontaktierbar sein.'),
 step(2,'Gewünschte Verbindungen separat nachweisen: z. B. freie S-Litze zum Schleifer oder Radlitze zum bestätigten leitenden Radpfad. Absichtliche Radmasse nicht als zu isolierenden Fehler definieren. Der Motor erhält zusätzlich seine vollständige Sechserprüfung [[12]]/[[13]].'),
 step(3,'Ist die Ader bereits mit Widerstand, LED, Diode, einem bestückten Pad oder unbekannter Leiterbahn verbunden, diese OL-Regel nicht anwenden. Zum vorher festgelegten Elektronik-Prüfplan auf [[22]] wechseln. Keine Bauteile abtrennen, nur damit ein gewünschter Offenwert erscheint.'),
 note('Fehlgeschlagene Vor-/Nachprobe macht die Isolationsaussage ungültig. Endlicher oder wechselnder Wert am wirklich getrennten passiven Leiter: Berührung, Scheuerstelle oder Messkontakt klären; nicht freigeben.'),
 p('<b>Nach jeder Löt-/Montageänderung:</b> Betroffene Reihe wiederholen. Unbenutzte Enden einzeln isolieren, Schlauchsitz optisch und mechanisch prüfen. Versiegelte Enden nicht wieder aufstechen. Vor Strom alle Hilfsleitungen entfernen.'),
 p('Kopf/Leitung ______; Fotos L1/L2/X1/X2 ______; getrennte Bauteile ______; Gerät/Bereich ______; Datum ______. OL ist nur der Offenbefund dieses Geräts in diesem Aufbau, kein Hochspannungs-Isolationsnachweis.')
 ],sources=['Q1','Q6'])

page(22,'Bestückte Netze: die konkrete Messkarte','Elektrische Prüfung | Platinen und LEDs',
 'Für bestückte Elektronik werden Bauteilpfad, Prüfparameter und erwartetes Verhalten vor der Messung festgelegt. Eine pauschale Fachprüferpflicht wird durch diese konkreten Angaben ersetzt.',
 'Eigene beidseitige Platinenfotos, lesbare Revision, Anschlussrollen und Multimeterhandbuch bereithalten. Decoder/Puffer entfernt; übrige Restenergie ausschließen.',[
 tab(['Pro Messung vorab ausfüllen','Deine konkrete Festlegung'],[
 ['1. Zwei Kontaktstellen','Foto/Markierung und Anschlussname beider sicher zugänglicher Punkte: __________________'],
 ['2. Elektrischer Zustand','Was angeschlossen/getrennt ist; Spannungsfreiheit und Speicherzustand: __________________'],
 ['3. Bekannter Sollpfad','Kupfer / Widerstand / Halbleiter / weitere Bauteile; Quelle: __________________'],
 ['4. Messparameter','Gerät, Modus, Prüfspannung/-strom, Polung(en), Wartezeit: __________________'],
 ['5. Soll und Abbruch','Begründeter Werte-/Verhaltensbereich; eindeutige Abweichung: __________________'],
 ['6. Kontaktkontrollen','Je Messseite positive Vor-/Nachprobe ohne Nachbarnetz-Brücke: __________________']],[1.05,2.65]),
 h('Diese Bereiche müssen abgedeckt sein'),
 p('<b>Vorn:</b> SW/RT-Strompfad und Ring A/B; Motorpads; Front-VCC, L_WS/L_RT und wirksame LED-Strombegrenzung; GE/AUX-Zuordnung; LS1/LS2. Jeweils absichtliche Bauteilwege gegenüber unerwünschtem Kontakt zu Rahmen, Schrauben, Halter und Nachbarnetzen unterscheiden.'),
 p('<b>Hinten:</b> S/RT/B/GR-Verbund; 0/GL-Radkontakt; +Ub, LV und LR samt Widerständen; GE-Ende und unbenutzte Trägerlitzen. <b>Wagen:</b> O/RT, L/GE und bei Radkontaktoption B-Pfade nach [[25]]/[[26]].'),
 step(1,'Eigene Aufdrucke mit revisionspassender Herstellerzeichnung abgleichen. Unbekannte interne Pfade bleiben offen. RCN-121 erklärt Schnittstellenrollen, aber keine unsichtbare LoDi-Leiterbahn; Front-VCC ist nicht interne Pin-12-Vcc.'),
 step(2,'Erst bei sechs vollständigen Feldern messen. Sicher zugängliche Pads oder eine eindeutig zugeordnete Kontaktaufnahme benutzen. Nicht mit freien Spitzen zwischen 21MTC-Pins suchen oder direkt an Pins löten.'),
 step(3,'Vor/nach Löten, Befestigung und Bewegung die betroffenen Messreihen im gleichen dokumentierten Zustand wiederholen. Abweichung eingrenzen, beheben, vollständige Reihe erneut prüfen. Eine unveränderte Vorheranzeige allein beweist keinen richtigen Ausgangszustand.'),
 note('Fehlt ein Feld, bleibt diese Messung und die davon abhängige Bestromung offen. Niedriger Widerstand kann ein Sollpfad sein; hoher Widerstand ohne guten Kontakt beweist nichts. Keine willkürlichen Grenzwerte und kein allgemeines OL über LEDs/Platinen.')
 ],sources=['Q1','Q3','Q8'])

page(23,'Mittelwagen: Platine einpassen und Enden benennen','Mittelwagen | Montage',
 'Die vorhandene LoDi-Leiste übernimmt die Längsverbindung. Zusätzliche lange Steueradern werden nicht durch den Wagen gezogen.',
 'Wagen vollständig abgekuppelt und vom Gleis. Vorhandene Speicher erfassen und nach bestätigtem Verfahren behandeln; nicht kurzschließen.',[
 photo(IMG/'image-4.jpg',43),
 small('Eigene MT-37700 V4.3 aus REV10. Endpads L / O / B; SJ2 = Türbeleuchtung. Das Foto nicht auf volle Seitenhöhe strecken.'),
 photo(IMG/'image-5.jpg',148),
 small('Eigenes Einbaubild im Bordrestaurant: Passung für jeden tatsächlichen Wagen prüfen. Es zeigt noch keine abgenommene Kupplungsverdrahtung.'),
 step(1,'Ersten Wagen als Muster öffnen: tatsächliche Rastungen und Endabdeckungen lösen, nicht am Fenstereinsatz hebeln. Kupplung, Haltenasen, vorhandene Kabel und mögliche Achskontakte vor Ausbau fotografieren. Enden dauerhaft „1“ und „2“ nennen.'),
 step(2,'Platine ohne Strom trocken auflegen. Dach muss ohne Druck schließen; Platine und Litzen dürfen Fenster, Rastungen und Schrauben nicht stören. Bei abweichender Passung nichts auf Verdacht kürzen. SJ2/Türbeleuchtung unverändert lassen.'),
 tab(['Pad im gewählten LoDi-Motorplatinenbetrieb','Anschluss'],[
 ['O an beiden Enden','RT-Kupplungspfad / Roh-Mittelleiter'],
 ['L an beiden Enden','GE / geschalteter Innenlichtpfad'],
 ['B','Ohne örtlichen Achskontakt frei; mit geprüfter Radkontaktoption nach [[26]]']],[1.6,1.8]),
 step(3,'Vor Löten jede Kupplungshälfte und jeden Übergang nach [[24]] zuordnen. Leiste nach [[25]] vorprüfen. Dann flexible kurze Litzen von Kupplung zu bestätigtem Pad führen; die Deichsel muss beide Endlagen ohne Zug an Lötstellen erreichen.'),
 note('Diese Belegung gilt für den hier gewählten Motorplatinenbetrieb: RT an O, GE an L. O nicht nach einer anderen LoDi-Variante als Masse behandeln. Radkontakte beider Triebköpfe bleiben erhalten.')
 ],'Wagen/Endorientierung und Passung sind dokumentiert. Weiter mit der elektrischen Einzelprüfung, noch nicht einschalten.',sources=['Q3','Q4'])

page(24,'Kupplungen: jeden Übergang einzeln prüfen','Mittelwagen | RT und GE',
 'Die physische Kontaktzuordnung wird gemessen. Zwei Vertauschungen können sich am Zugende gegenseitig verdecken.',
 'Nur passive Kupplungsstücke mit freien Litzen: keine LoDi-Elektronik, Decoder oder Speicher angeschlossen.',[
 fig('coupler',150),
 step(1,'Jede Kupplung in einer eindeutigen Fotoansicht markieren: Kontakt K1/K2 als vorläufige Namen. Jede Kontaktfläche bis zur freien Litze durchmessen. Partnerhälften zusammenstecken und feststellen, welcher Kontakt welchen Partner erreicht. Nicht aus Links/Rechts im Foto raten.'),
 step(2,'Die Sollfunktion vom bestätigten vorderen LoDi-RT- und GE-Anschluss aus fortschreiben. Enden als RT-1, GE-1, RT-2, GE-2 dokumentieren. Erst jetzt werden die folgenden Sollpaare geprüft; Namen nicht nachträglich ändern, damit eine Kreuzung „passt“.'),
 tab(['Messfolge bei unveränderten vier Clips','Soll'],[
 ['RT-1 zu RT-2; GE-1 zu GE-2','Beide gewünschten Pfade stabil leitend'],
 ['RT-1 zu GE-2; GE-1 zu RT-2','Beide Kreuzpfade offen/OL'],
 ['RT-1 zu RT-2; GE-1 zu GE-2 nochmals','Beide positiven Nachproben weiterhin leitend'],
 ['Kupplung in normalen Endlagen','Je Lage gesamte Folge wiederholen']],[2,1.6]),
 step(3,'Bei falschem Partner Kontakt-/Litzenzuordnung klären. Bei zusätzlichem leitendem Kreuzpfad nach Draht-/Zinnbrücke suchen. Bei offener Nachprobe war der Messkontakt unsicher: Reihe ungültig, Clips korrigieren und wiederholen.'),
 step(4,'Jeden Übergang mit Wagen und Endorientierung notieren. Nach Drehen, Umreihen, Kupplungs- oder Platinentausch betroffene Einzelzuordnungen und anschließend die neue Ende-zu-Ende-Zuordnung erneut prüfen.'),
 note('Nach Anschluss einer bestückten LoDi-Leiste L gegen O nicht auf OL zwingen. Ab dann gilt [[25]] mit Kontakt-zu-Pad-Prüfung und begründetem Elektronikvergleich. Keine Leiterbahn zur Beseitigung eines erwartbaren Bauteilpfads trennen.'),
 p('Übergang ______; Fotoansicht ______; RT/GE-Herkunft ______; Vorproben ______; Kreuzpfade ______; Nachproben ______; Bewegung ______; Datum ______.')
 ],'Jeder einzelne Übergang stimmt. Eine Gesamtmessung allein und bloßer Durchgang beweisen noch keine Stromtragfähigkeit.',sources=['Q3','Q4'])

page(25,'Wagen: vor und nach dem Löten vergleichen','Mittelwagen | Anschlussprüfung',
 'Die weiße Leiste bleibt unverändert. Du prüfst jeden Kontakt zu seinem richtigen Pad und die vorgesehenen Längspfade.',
 'Wagen allein, ohne Gleis und Bus; Speicherzustand sicher. Passive Kupplungen [[24]] geprüft. Für bestückte Querpfade Messkarte [[22]] ausgefüllt.',[
 tab(['Vor Kupplungsanschluss','Nach Kupplungsanschluss'],[
 ['L Ende 1 zu L Ende 2: stabiler Sollpfad','L-L erneut prüfen, auch bei Deichselbewegung'],
 ['O Ende 1 zu O Ende 2: stabiler Sollpfad','O-O erneut prüfen, auch bei Deichselbewegung'],
 ['L gegen O in beiden Polungen nur nach festgelegtem Elektronikplan erfassen','Bei gleichem Zustand, Bereich, Polung und Wartezeit vergleichen'],
 ['Jede freie Kontaktlitze einzeln zugeordnet','An beiden Enden: RT-Kontakt zu O; GE-Kontakt zu L']],[1.5,1.6]),
 step(1,'Ende 1/2, Revision und vorhandene Speicher fotografieren. L-L und O-O zuerst positiv nachweisen. Je Reihe Kontaktkontrollen vor und nachher durchführen. Ist eine Soll-Durchleitung unklar, noch keine Kupplungslitze anlöten.'),
 step(2,'RT-Litzen an die vorgesehenen O-Pads und GE-Litzen an L löten. Flexibles Kabel mit Bewegungsschlaufe führen; keine zusätzliche Längsader. Für optionale Radkontakte zuerst die getrennte B-Prüfung [[26]] abschließen.'),
 step(3,'Mit Lupe jede Lötstelle auf Brücke und Einzelsträhnen prüfen. Für jedes Wagenende tatsächlichen RT-Kontakt bis O und GE-Kontakt bis L kontrollieren. L-L und O-O erneut prüfen. Deichsel in beide Endlagen schwenken; Litzen dürfen nicht spannen oder am Rad streifen.'),
 step(4,'Die vorher festgelegten L/O-Querpfade bei gleichen Bedingungen vergleichen. Neu niederohmig oder unerklärlich verändert: Kupplungslitzen wieder stromlos abtrennen, freie Litzen nach [[24]] prüfen und Lötstellen untersuchen. Bleibt die Abweichung an der Leiste, Bauteilpfad mit Quelle/Messkarte klären.'),
 note('Ein Vorher-/Nachhervergleich erkennt Änderungen, bestätigt aber allein keine fehlerfreie ursprüngliche Elektronik. Kein Bauteil entfernen und keine Leiterbahn aufschneiden, um einen Offenwert zu erhalten.'),
 tab(['Wagen / Revision / Ende','L-L / O-O','Kontakt-Pad / Bewegung','Querpfade / Ergebnis'],[
 ['________________','_____ / _____','____________','____________'],
 ['________________','_____ / _____','____________','____________'],
 ['________________','_____ / _____','____________','____________']],[1.2,.9,1.25,1.2]),
 p('<b>Weiter zur Lastprüfung:</b> Wenn der vordere Schleifer aussetzt, kann der Motorstrom über RT durch alle Wagenkupplungen fließen. Daher Wagenzahl nicht aus der Ohmmessung ableiten; zulässige Stufen auf [[28]] bestimmen.')
 ],sources=['Q3','Q4'])

page(26,'Optional: örtliche Radkontakte an Wagen-B','Mittelwagen | nur bei gewählter Radkontaktoption',
 'Eine Achskontaktfeder ergänzt die örtliche Radmasse. Beide Kupplungspole bleiben RT und GE; es entsteht kein dritter Zugbus.',
 'Ein Wagen vom Gleis, beidseitig abgekuppelt. Für diese B-Prüfung keine Kupplungslitzen oder Speicher angeschlossen. Messplan [[22]] festgelegt.',[
 step(1,'Vorhandene Feder, Befestigung und Litze fotografieren; bis zur berührten Metallachse/Radfläche verfolgen. Leitung von alter Elektronik lösen und frei isolieren. Keine Achshalterung als „Massefeder“ entfernen; nicht direkt an der Achse löten.'),
 step(2,'Zwei blanke Punkte desselben leitenden Achs-/Radpfads positiv prüfen. Freie Federlitze gegen diesen Pfad messen: stabil leitend, auch bei mehreren Radstellungen. Bezug und Leitung positiv nachprüfen. Nicht auf Lack, Haftreifen oder Kunststoff messen und keine Feder zum Kaschieren eines Fehlers stärker verbiegen.'),
 tab(['B-Pfade am selben Wagenende','Vorher','Nachher'],[
 ['Rot B / Schwarz O','________','________'],
 ['Rot O / Schwarz B','________','________'],
 ['Rot B / Schwarz L','________','________'],
 ['Rot L / Schwarz B','________','________']],[1.5,1,1]),
 step(3,'Vor dem Anlöten alle vier Werte nach ausgefülltem Elektronikplan erfassen: Bereich, Polung, Wartezeit und positive Padkontakte vor/nach jeder Reihe. Kein allgemeines OL erwarten. Dann genau eine geprüfte Radkontaktlitze an <b>B</b> des zugehörigen Endes löten.'),
 step(4,'Abkühlen lassen, mit Lupe auf Brücken zu O/L prüfen. Vier Werte unter identischen Bedingungen wiederholen; Litze bis B auf Durchgang und Drehgestellbewegung prüfen. Neu niederohmig/unerklärlich verändert: Litze wieder von B trennen, einzeln isolieren, Ursache beheben und Reihe neu.'),
 step(5,'Zweiter Radkontakt am anderen Ende erhält seine eigene Kontakt- und B-Prüfung. Keine interne B-B-Verbindung voraussetzen. Erst danach Kupplungslitzen an O/RT und L/GE nach [[25]] anschließen. SJ2 unverändert lassen.'),
 step(6,'Nach elektrischer Abnahme Belegtmeldung im tatsächlich benutzten Rückmeldeabschnitt prüfen: Wagen/Radsatz belegt und frei, in mehreren Radstellungen und beiden Orientierungen. Eine Kontaktmeldung identifiziert nicht automatisch den ICE; Anlagenhalt gesondert nach [[39]].'),
 note('Ohne passende vorhandene Feder bleibt B frei. Für Nachrüstung Unterseite, Lager und Federaufnahme mit Maßstab dokumentieren; keine Ersatzteilnummer eines anderen Modells ungeprüft kaufen. B niemals an O/RT oder L/GE brücken.')
 ],'Kontakt, vier B-Pfade, Bewegung und spätere Rückmeldung sind je Wagenende dokumentiert.',sources=['Q4','Q8'])

page(27,'Motor und Innenlicht im 60977 einstellen','Konfiguration | getrennte Decoder',
 'Motorart, Ausgangsart, Funktionstaste und Lichteffekt sind verschiedene Einstellungen. Nach dem letzten Soundprojekt erneut prüfen.',
 'Nur 60977 im bestätigten Märklin-Aufbau; 59649, Zug und Puffer physisch getrennt. Altprojekt und Firmware sichern. Änderungen nie am verbundenen Zug.',[
 tab(['Einstellung','Konkretes Soll'],[
 ['Motor','Vollständiger geprüfter 60941: technische Zuordnung HLA/C90. Märklin-Tabelle: CV52 = 3; danach rücklesen. Unklarer Motorzustand zuerst klären.'],
 ['Frontlicht','F0 vorwärts = LV / Weiß; F0 rückwärts = LR / Rot. Keine ungewollten Zusatzbedingungen.'],
 ['Innenlicht-Ausgang','Genau der bestätigte AUX aus [[14]]: AUX4 oder AUX1. Keine Jumperänderung.'],
 ['Innenlicht-Taste','Dokumentierte freie/bewusst übernommene Taste, rastend. Nicht automatisch F4 oder F6.'],
 ['Effekt und Bedingung','Dimmer, Modus 1; beide Richtungen, Stand und Fahrt, ohne zusätzliche Zustandsbeschränkung (Tabellenbedingung 0). Kein Timer/Blinken oder Dauer-an-Modus 19.'],
 ['Ausschließlich diese Taste','Kein F0, Motorlauf, Richtungsereignis oder konkurrierender Auslöser auf demselben AUX.']],[1.0,3.6]),
 step(1,'Im ausgelesenen mDecoderTool3-Projekt Motor- und Funktionszuordnung einstellen, unter neuem Namen sichern, übertragen und erneut lesen. Firmwareabhängige Tabellenwerte nicht blind als Einzel-CVs übertragen. Das Auslesen der Einstellungen sichert nicht automatisch die Sounddateien.'),
 step(2,'<b>Nur bei Innenlicht über AUX4:</b> CV51 am 60977 sichern. Bit4 (Wertigkeit 16) muss 0 sein, damit AUX4 verstärkt arbeitet. Bevorzugt im Projekt die elektrische Ausgangsart ändern. Bei Einzelwert: gesetztes Bit4 durch Abziehen von genau 16 löschen; sonst Altwert lassen. Nie pauschal CV51 = 0.'),
 step(3,'CV51 frisch rücklesen: Ziel stimmt, Bit4 = 0, alle übrigen Bits entsprechen dem Altwert. Bei Innenlicht über AUX1 keine vorsorgliche AUX4-Änderung. Nach jedem späteren Projekttransfer Ausgangsart und Mapping erneut prüfen.'),
 p('<b>ESU hinten:</b> Bestätigtes F0-Mapping aus [[9]] übernehmen: vorwärts LV, rückwärts LR. Die Farbverdrahtung auf [[20]] kehrt die sichtbaren Farben um. Nötige Mapping-/Dimmänderungen erhalten eine eigene vollständige Exportkarte mit Indexgruppen; CV191-195 sind dafür nicht die Mappingwerte.'),
 note('Keine automatische Einmessfahrt anfordern: CV7/Firmware-Feld des 60977 nicht auf 77 setzen. Nicht den ESU am Märklin 60971 verwenden. Eine AUX-Nummer ist keine Funktionstastennummer.'),
 p('Projekt ______; Motor/CV52 rückgelesen ______; Innenlicht-AUX/Taste ______; CV51 alt/ziel/neu ______; letzte Übertragung ______. Nach Änderungen betroffene Ausgangs-, Synchronisations- und T9-Tests wiederholen.')
 ],sources=['Q1','Q3','Q6','Q10'])

page(28,'Lastgrenzen vor dem Einschalten festlegen','Erststrom | zulässige Laststufen',
 'Auch der erste Standtest braucht eine begrenzte, geeignete Versorgung. Ein Ohm-Durchgangstest bestätigt keine Stromtragfähigkeit.',
 'Aufbau, Lasten, Messstellen und Strombegrenzung vor jeder Stufe dokumentieren. Keine Bestromung mit unbekanntem sicheren Grenzwert.',[
 fig('ammeter',119),
 tab(['60977: Herstellergrenze','Maximalwert','Zusätzlich beachten'],[
 ['Motor dauernd','1,1 A','Keine blockierte Motorprobe'],
 ['Je verstärktem Licht-/AUX1-AUX4','250 mA','Gilt nicht für Logikausgänge'],
 ['Licht und AUX zusammen','300 mA','Innenlicht und andere gleichzeitige Ausgänge summieren'],
 ['Gesamtlast','1,6 A','Motor, Sound und Licht; niedrigere Pfadgrenzen gelten']],[1.8,.65,1.9]),
 step(1,'Je Stufe festlegen: konkrete Verdrahtung, Last(en), Geräte/Messpunkte, abgesicherter Bereich, Begrenzung und eindeutige Abschaltwerte. Grenzen von Kupplung, Litze, LoDi-Platine und LED-Zweigen mit berücksichtigen. Fehlende Lastdaten zuerst im dafür geeigneten begrenzten Aufbau bestimmen.'),
 step(2,'Stufen getrennt planen: Motorseite im Stand; Kleinstfahrt; Gegenkopf; erster Wagen; jeder weitere Wagen; gesamte Kombination; Versorgung nur von hinten. Unbekannte Last erlaubt auch nicht automatisch einen ersten Wagen. Einschaltspitze und höchste vorgesehene Helligkeit einschließen.'),
 step(3,'Strommessung nur in einen vorher spannungslos geöffneten Pfad in Reihe einsetzen. Passenden abgesicherten Eingang und Bereich verwenden. Einzel-AUX, Licht/AUX-Summe und Gesamtstrom getrennt bewerten. Hintere ESU-LEDs zählen nicht zur 60977-AUX-Summe, belasten aber RT.'),
 step(4,'Für die alleinige hintere Speisung ausschließlich die vorher identifizierte vordere Schleiferzuleitung stromlos trennen und einzeln isolieren. Der RT-Pfad durch alle Kupplungen muss den Motorstrom sicher tragen; Spannungseinbruch/Erwärmung prüfen. Kein Metall unter den Schleifer legen. Nach Wiederanschluss betroffene Prüfungen vollständig wiederholen.'),
 tab(['Stufe / Wagenzahl / Helligkeit','Plan / Grenze vorher','Ergebnis / erlaubt'],[
 ['________________________','________________','________________'],
 ['________________________','________________','________________']],[1.6,1,1]),
 note('Amperemeter nie quer zwischen B und 0 anschließen. Nach Messung Rot wieder in V/Ω. Bei Überlast, Geruch oder unerwarteter Wärme ausschalten; keinen zweiten Versuch ohne Ursachenklärung.')
 ],sources=['Q1','Q3','Q6','Q17'])

page(29,'Vor dem ersten Strom: beide Köpfe abhaken','Erststrom | Voraussetzung je Kopf',
 'Diese Karte wird vor dem Einsetzen ausgefüllt. Sie enthält keine erst später möglichen Funktions- oder Gehäuseergebnisse.',
 'Je Kopf getrennt prüfen. Datum ______; Motorseite/Gegenkopf ______; zugehörige Fotos und Protokolle ______.',[
 tab(['Jetzt erforderlicher Nachweis','Motorseite','Gegenkopf'],[
 ['Decoder-Vorabtest [[9]] mit eigener Identität, Aktivierung, Firmware und neuer SID','________','________'],
 ['Reale Revision/Padbelegung und sichere Befestigung [[14]]-[[20]]','________','________'],
 ['Schleifer und Radkontakt; eindeutige RT/GE-Zuordnung','________','________'],
 ['Motor einschließlich Drosseln/Litzen [[12]]/[[13]]; bestätigter Motortyp','________','entfällt'],
 ['LED-Zweige und sichere Strombegrenzung [[18]]; passendes Mapping','________','________'],
 ['Ein Lautsprecher, Adapter und mechanischer Sitz [[17]]','________','entfällt'],
 ['Passive Leiter [[21]] und vollständiger Elektronikplan/Ergebnisse [[22]]','________','________'],
 ['Gesicherte Projekte; Innenlicht-AUX und Ausgangsart [[27]]','________','________'],
 ['Erste konkrete Laststufe [[28]]; Messung/Begrenzung/Abbruchwerte','________','________'],
 ['Gleis, Bus, Puffer, andere Quellen physisch getrennt; Restenergie ausgeschlossen','________','________'],
 ['Alle Hilfsleitungen entfernt; unbenutzte Enden einzeln isoliert','________','________'],
 ['Passende Indexmerkmale eindeutig sichtbar; geplante Decoderlage/Freiraum','________','________'],
 ['Prüfort: eine Quelle, Fahrstufe 0, Automatik aus; keine Einmessfahrt','________','________']],[3.5,.8,.8]),
 p('<b>Erst dann einsetzen:</b> Motorseite auf [[30]], Gegenkopf auf [[31]]. Den tatsächlichen Steckersitz anschließend noch im stromlosen Zustand seitlich prüfen. Danach der jeweils erlaubte Einzeltest auf [[32]]/[[33]].'),
 note('Eine offene Pflichtzeile nicht mit „entfällt“ schließen. Ein G0-/Vorabtest am losen Decoder bestätigt keine richtige Fahrzeugverdrahtung. Ein erfolgreicher Leseversuch bestätigt keine Motorisolation.'),
 p('<b>Später separat:</b> Ausgangs- und Fahrtests [[32]]-[[35]], geschlossene Gehäuseprüfung [[36]]/[[37]]. Keine zukünftigen Ergebnisse vorweg abhaken. Änderungen an Anschluss, Befestigung oder Projekt machen die betroffenen Nachweise erneut erforderlich.')
 ],'Alle für diesen Kopf erforderlichen Voraussetzungen sind tatsächlich erfüllt.',sources=['Q1','Q3','Q6'])

page(30,'Vorn: 60977 gerade auf LoDi einsetzen','Erststrom | Steckkarte Motorseite',
 'Der Märklin 60977 gehört auf die rote LoDi 511. Diese Karte erst unmittelbar vor dem Einzeltest der Motorseite ausführen.',
 'Karte [[29]] für Motorseite vollständig. Kopf vom Gleis, Wagen/Bus und alle Versorgungen getrennt; beide 60974 ab.',[
 cols([photo(IMG/'image-2.jpg',252,[.08,.35,.93,.76]),small('Detail aus deinem Originalfoto: lange helle Fläche Richtung K1, Steckfeld, darunter LS1/LS2. Die schwarze Struktur bleibt unberührt.')],[
 p('<b>Vorgesehene Lage:</b> Der lange Decoderkörper zeigt zur freien hellen Fläche Richtung K1, nicht über LS1/LS2. Die schwarze Buchsenleiste des Decoders zeigt nach oben und bleibt sichtbar.'),
 p('<b>Steckmechanik:</b> Stifte des Trägers treten von unten durch die Löcher der Decoderplatine in deren Buchse ein. Nicht von oben in die sichtbare Buchse drücken.'),
 note('Die fehlende Stiftposition 11 am Träger und die zugehörige geschlossene Decoderposition müssen am echten Exemplar sichtbar zusammenpassen. Das Foto zeigt diesen Abgleich noch nicht.','INDEX ZUERST')
 ],[.85,1.85]),
 step(1,'Nur an den Platinenkanten halten. Beide Stiftreihen, Fehlstelle und geschlossene Indexposition ansehen. Nicht nach einer geratenen Links-/Rechts-Zählung ausrichten. Langer Freiraum allein beweist keine richtige Stecklage.'),
 step(2,'60977 parallel über der Steckleiste halten. Beide Reihen und Index deckungsgleich setzen. Kein Stift darf auf der Decoderplatine oder an der geschlossenen Stelle stehen. Bei unklarer Sicht absetzen und Nahfotos beider Teile zur Identifikation aufnehmen.'),
 step(3,'Gleichmäßig im Bereich der Steckleiste nach unten drücken; nicht auf Chips oder das freie Decoderende. Bei Widerstand abheben und Reihenversatz prüfen. Keine Pins biegen oder das Teil testweise umdrehen.'),
 step(4,'Seitlich kontrollieren: alle Stifte eingeführt, Decoder parallel, keine Unterseiten-Metallberührung, keine Litze eingeklemmt. Tatsächlichen Platz zum späteren Dach mitprüfen. Erst danach offener Einzeltest [[32]].'),
 note('Wenn eine schwarze Struktur die Fehlstelle verdeckt, ist sie nicht automatisch eine Schutzkappe. Nichts abziehen, hebeln, anbohren oder durchdrücken. Decoder abgezogen lassen, genaue Revision und sichtbares Indexmerkmal klären.')
 ],'Index und beide Reihen stimmen; tatsächlicher Sitz und Freiraum sind im stromlosen Aufbau geprüft.',sources=['Q1','Q3','Q8'])

page(31,'Hinten: 59649 auf den Märklin-Träger setzen','Erststrom | Steckkarte Gegenkopf',
 'Der ESU sitzt auf dem separaten leeren Träger aus dem 60977-Satz. Die folgende Herstellerzeichnung zeigt dessen Steckmechanik.',
 'Karte [[29]] für Gegenkopf vollständig. Kopf abgekuppelt, vom Gleis, alle Versorgungen und Puffer getrennt.',[
 cols([photo(IMG/'ice2976_stecken-006.png',303,[.07,.205,.375,.91]),small('Märklin-Originalzeichnung S. 6: Einsteckfolge mit Warn-Seitenprofil. Im Gegenkopf wird hier der 59649 eingesetzt.')],[
 step(1,'Leeren Träger so zuordnen wie auf [[19]]: SUSI-/Lautsprecherbuchsen auf einer Seite der Stiftleiste, lange freie Decoderfläche auf der anderen. Aufdrucke und bereits geprüfte +Ub/LV/LR/B/GR/0/GL-Verbindungen abgleichen.'),
 step(2,'59649 an den Kanten halten. Seine schwarze Buchsenleiste zeigt nach oben. Der lange Decoderkörper zeigt über die freie Trägerfläche weg von den beiden Steckbuchsen. Stifte treten von unten durch die Decoderplatine ein.'),
 step(3,'Tatsächliche fehlende Stiftposition und geschlossene Indexposition 11 sichtbar deckungsgleich halten. Beide Reihen vor dem Drücken prüfen. Keine verdeckte Stelle erraten und keine unbekannte Steckerstruktur entfernen.')
 ],[.9,1.75]),
 step(4,'Decoder parallel im Steckleistenbereich nach unten setzen. Bei Widerstand wieder abheben; keinen einseitigen oder um einen Platz versetzten Sitz mit Kraft korrigieren. Von der Seite alle eingeführten Stifte, geraden Sitz und Abstand zum Rahmen prüfen.'),
 step(5,'Freiraum über dem realen Decoder prüfen. Litzen tragen weder Träger noch Decoder; GE und alle unbenutzten Trägerlitzen bleiben einzeln isoliert. Erst danach die erlaubte Fahrzeugprüfung [[33]] ausführen.'),
 note('Vorn 60977 auf LoDi; hinten 59649 auf Märklin-Träger. Zum Abziehen immer die gesamte Versorgung trennen und gleichmäßig an den Kanten abheben. Nicht mit Metall unterhebeln.'),
 p('Kopf/Datum ______; Index sichtbar ______; beide Reihen vollständig ______; seitlicher Sitz ______; Metall-/Dachfreiraum ______; Foto ______.')
 ],sources=['Q1','Q6','Q8'])

page(32,'Motorseite: erster Strom und kurze Kleinstfahrt','Erststrom | Motortriebkopf allein',
 'Zuerst Kommunikation und Licht im Stand, dann leiser Sound. Der Motor wird erst im zweiten Schritt kurz bewegt.',
 'Motorseite [[29]]/[[30]] bestanden; passende Laststufe [[28]]. Gegenkopf/Wagen/Puffer physisch getrennt. Freie Kupplungsenden einzeln isoliert.',[
 step(1,'Getrenntes Prüfgleis waagerecht und gegen Absturz sichern. Genau einen passenden CS3-Ausgang anschließen; Programmier- und Betriebsausgang nicht verbinden. Fahrstufe 0, Automatik aus, keine Einmessfahrt vorgemerkt. Hilfsleitungen vollständig entfernt.'),
 step(2,'Den ganzen Motortriebkopf auf das getrennte Programmiergleis setzen und nach dem bestätigten Märklin-Leseverfahren prüfen. Zum Wechsel auf Betriebsgleis wieder ausschalten und den Kopf vollständig stromlos umsetzen. Kein Kopf steht gleichzeitig auf verbundenen Stromkreisen.'),
 step(3,'Im Betrieb bei stehendem Motor nur den eindeutig zugeordneten mfx-Eintrag bedienen. F0 aus: Front dunkel. F0 an: vorwärts Weiß, rückwärts Rot. Tatsächliche LEDs beobachten; kein Anrollen zum Lichtwechsel. Danach den zugelassenen Sound leise testen.'),
 tab(['Offener Standtest','Ist / Ergebnis'],[
 ['Kommunikation / eindeutiger 60977','________________'],
 ['F0 aus / vorwärts / rückwärts','________________'],
 ['Leiser Sound / keine Überlast','________________'],
 ['Keine Wärme-/Geruchsauffälligkeit','________________']],[1.8,1]),
 step(4,'Nur nach bestandenem Standtest und zugelassener Motorlast: freien Fahrweg prüfen, kleinste Fahrstufe kurz anlegen, dann wieder 0. Räder nicht festhalten. Der Motortriebkopf muss bei vorwärts in die festgelegte Vorwärtsrichtung fahren.'),
 step(5,'Bei falscher Fahrtrichtung: STOP, vom Gleis nehmen, alle Verbindungen trennen, Decoder abziehen. Bestätigte Motorzuordnung gezielt korrigieren; danach komplette betroffene Motor-/Litzenprüfung [[12]]/[[13]] und Anschlussprüfung wiederholen. Keine spontane Licht- oder CV-Invertierung als Ersatz.'),
 note('Brummen ohne Bewegung, Geruch, auffällige Wärme oder Überlast: sofort Versorgung aus. Mechanik, Bürsten, Litzen und Isolation stromlos prüfen. Nicht höhere Fahrstufe geben oder wiederholt einschalten.'),
 p('<b>Einmessfahrt bleibt aus:</b> CV7/Firmware-Feld nicht auf 77 setzen. Das kurze Prüfgleis ist dafür nicht vorgesehen. Die gewöhnliche Kleinstfahrt ist ein eigener kontrollierter Handgriff.'),
 p('Datum ______; Projekt/Firmware ______; Laststufe ______; Lichtrichtung ______; Sound ______; Kleinstfahrt/Richtung ______; Auffälligkeiten ______.')
 ],'Die Motorseite besteht ihren Einzeltest. Alle Änderungen sind erneut geprüft; erst dann Gegenkopf ergänzen.',sources=['Q1','Q2','Q3'])

page(33,'Gegenkopf anschließen, beide Fronten prüfen','Erststrom | Gegenkopf und Paar',
 'Die Einzelprüfung bestätigt die hintere Stromaufnahme und Verdrahtung. Die synchronisierte Lichtreaktion wird anschließend gemeinsam mit dem Master geprüft.',
 'Gegenkopf [[29]]/[[31]] und Motorseite [[32]] bestanden; Laststufe zugelassen. Puffer ab, beide Köpfe zunächst ungekuppelt.',[
 step(1,'Hinten im stromlosen Einzelzustand eigene S-/R-Stromaufnahme, B/GR-/0/GL-Zuordnung, Halter, Widerstände und einzelne Isolation von GE/unbenutzten Litzen abschließend kontrollieren. Versorgung und Rückleiter müssen aus den Anschlussprüfungen nachgewiesen sein.'),
 note('Ein synchronisierter ESU ist ohne Master nicht automatisch als eigene mfx-Lok bedienbar. Hier keine selbständige mfx-Anmeldung erzwingen. Motorloses DCC-Rücklesen ist kein Pflichtschritt; jede DCC-Änderung erfolgt auf der quittierenden Einzelaufnahme [[7]]/[[8]].','RICHTIGER PRÜFZWECK','info'),
 step(2,'Beide Köpfe stromlos und ungekuppelt auf dasselbe getrennte Betriebsgleis setzen. Genau eine CS3-Quelle speist beide; jeder Kopf nutzt seine eigene geprüfte Aufnahme. Fahrstufe 0 und Automatik aus. Es werden keine Decoderparameter geändert.'),
 tab(['Nur den gemeinsamen ICE-Master bedienen','Motorseite','Gegenkopf'],[
 ['F0 aus, vorwärts und rückwärts','dunkel','dunkel'],
 ['F0 an, vorwärts','weiß','rot'],
 ['F0 an, rückwärts','rot','weiß']],[2,1,1]),
 step(3,'Mindestens fünf Richtungswechsel bei Fahrstufe 0 durchführen. Physische Farben und Verzögerung beobachten. Kein Anrollen nötig; keine unerwünschte Ein-/Ausblendung. Alte gespeicherte Slave-Zeile von einer aktiven, unabhängig steuerbaren Anmeldung unterscheiden.'),
 step(4,'Versorgung abschalten und physisch trennen. Gegenkopf vom Gleis nehmen; im unveränderten geprüften Zustand wieder aufstellen. Beide neu starten und Lichtfolge wiederholen. Bei abweichendem Verhalten die geprüften Einschaltreihenfolgen des Vorabtests [[9]] vergleichen.'),
 note('Aktiv eigenständig steuerbarer Slave nach eindeutiger Zuordnung: Paartest nicht bestanden. Nichts durch Löschen/Ausblenden passend machen. Keine CV- oder Mappingänderung am gemeinsamen Zug.'),
 p('Ist vorwärts ______; rückwärts ______; F0 aus ______; fünf Wechsel ______; Neustart ______; Eintragsvergleich ______; Datum/Projekt ______. Bei Fehler Versorgung trennen und nach [[38]] eingrenzen.')
 ],'Beide Fronten folgen im Stand und nach Neustart korrekt. Erst danach zulässige Wagenlasten auf [[34]] ergänzen.',sources=['Q1','Q6','Q7'])

page(34,'Wagen ergänzen: Innenlicht T1 bis T8 prüfen','Zugtest | zunächst offene Gehäuse',
 'Vor jedem zusätzlichen Wagen seine elektrische Prüfung und die neue Laststufe abschließen. Die ganze Prüfserie wird für jede zugelassene Zusammenstellung wiederholt.',
 'Beide Köpfe [[32]]/[[33]] bestanden. Wagen [[23]]-[[26]] geprüft, Last [[28]] zugelassen. Ein CS3-Stromkreis, Fahrstufe 0, Automatik aus, beide 60974 ab.',[
 step(1,'Vollständig ausschalten und Bus trennen. Nur den nächsten bereits geprüften Wagen ankoppeln; Endorientierung und Kontaktzuordnung kontrollieren. Niemals unter Spannung kuppeln. Danach im bestätigten begrenzten Prüfaufbau einschalten.'),
 tab(['Test','Du bedienst den gemeinsamen ICE-Eintrag','Bestanden, wenn'],[
 ['T1','F0, Sound und Innenlicht aus.','Alle Wagen dunkel.'],
 ['T2','Innenlicht einmal einschalten, loslassen; 30 Sekunden beobachten.','Bleibt an, kein Blinken/Timer.'],
 ['T3','F0 aus. Bei Fahrstufe 0 zehnmal vorwärts und zurück; je Zustand etwa 2 Sekunden warten.','Innenlicht unverändert, Motor steht.'],
 ['T4','F0 an. Die zehn Wechsel wiederholen.','Fronten wechseln korrekt, Innenlicht unverändert.'],
 ['T5','Nur F0 mehrfach aus/ein schalten.','Innenlicht reagiert nicht.'],
 ['T6','Zugelassenen Sound leise zuschalten; Richtungsfolge im Stand wiederholen.','Kein Lichtausfall, Sound-Neustart oder Reset.'],
 ['T7','Nur Innenlicht aus/ein schalten.','Wagen folgen; Fronten/Sound bleiben unverändert.'],
 ['T8','Nach jedem weiteren zugelassenen Wagen die Folge wiederholen.','Jede endgültige Wagen-/Endorientierung besteht; später auch geschlossen.']],[.35,2.35,1.45]),
 step(2,'Bei einem Fehler sofort trennen. Alle Wagen richtungsabhängig dunkel: Innenlichtmapping und GE prüfen. Ein Wagen/alles ab einer Kupplung: betroffenen Übergang und Kontakt-Pad-Zuordnung prüfen. Sound-Neustart zusammen mit Lichtausfall: Versorgung und Last klären.'),
 note('Keinen Puffer gegen ungeklärtes Flackern anlöten. Ein kurzer Einbruch trotz richtiger Zuordnung braucht eine Messung des tatsächlichen Ausgangs-/Versorgungsverlaufs im passenden Aufbau. Ohne Ursache keinen weiteren Einschaltversuch.'),
 p('Wagenzahl/Reihenfolge ______; Endorientierung ______; AUX/Taste ______; Laststufe ______; T1-T8 je Stufe ______; Datum ______. Zug und Kupplungen während der Standprüfung nicht berühren.')
 ],'Die vollständige vorgesehene Zusammenstellung besteht im Stand. Jetzt T9 und kontrollierten Fahrtest auf [[35]] ausführen.',sources=['Q1','Q3','Q4','Q10'])

page(35,'T9: jede Funktionstaste und die Fahrt abnehmen','Zugtest | endgültiges Projekt',
 'Ein letzter Projekttransfer kann Lichtmapping oder Ausgangsart verändern. Deshalb wird die tatsächlich gespeicherte Funktionstastenbelegung geprüft.',
 'T1-T8 bestanden; endgültige Projekte/Firmware dokumentiert. Nur zugelassene Last, Fahrstufe 0 und keine Einmessfunktion.',[
 step(1,'Für jede im Projekt belegte Taste vorher festlegen, was sich ändern darf: vordere Front, hintere Front, Innenlicht und Sound. Keine freien oder unbekannten Tasten versuchsweise betätigen. Testaufbau gegen ungewollte Bewegung sichern.'),
 step(2,'Jede belegte Taste einzeln aus/ein schalten: jeweils vorwärts und rückwärts, jeweils F0 aus und an. Soll und tatsächliche Reaktion nebeneinander notieren. Ungewolltes Frontlicht bei F0 aus oder eine fremde Innenlichtreaktion ist ein Fehler.'),
 tab(['Taste / Richtung / F0','Soll: vorn / hinten / innen / Sound','Ist / Ergebnis'],[
 ['________________','________________________','________________'],
 ['________________','________________________','________________'],
 ['________________','________________________','________________'],
 ['________________','________________________','________________'],
 ['________________','________________________','________________'],
 ['________________','________________________','________________']],[1.1,1.7,1.1]),
 small('Tabelle für sämtliche belegten Tasten und Kombinationen fortsetzen/kopieren. Projekt ______; Firmware ______; Laststufe ______; Datum ______.'),
 step(3,'Erst nach bestandenem Standtest und zugelassener Gesamt-Motorlast: bei kleinster Fahrstufe Stand-Fahrt-Stand in beiden Richtungen prüfen. Richtung ausschließlich bei stehendem Zug wechseln. Freien, waagerechten Fahrweg und Absturzschutz sicherstellen.'),
 step(4,'Vorgesehene Kurven und Weichen langsam befahren. Wagenlicht, Sound-Neustart, Beweglichkeit und Leitungslage beobachten. Bis zum geschlossenen Abschluss nur diesen kontrollierten offenen Test durchführen. Stillstand ohne Flackern beweist keine verschmutzungsfeste Fahrt.'),
 note('Abweichung: STOP, Versorgung physisch trennen. Nur den betroffenen Decoder auf dem bestätigten Einzelplatz ändern. Danach die betroffenen Ausgangs-/Synchronisationstests und T9 wiederholen; keine Änderung am verbundenen Zug.'),
 p('Stand-Fahrt-Stand vorwärts ______; rückwärts ______; Kurven/Weichen ______; auffällige Unterbrechungen ______; T9 vollständig ______. Nach Gehäuseschluss die betroffenen Funktions- und Fahrtests erneut prüfen.')
 ],'Die endgültige offene Zusammenstellung funktioniert. Geschlossenen Zustand noch nicht als bestanden eintragen.',sources=['Q1','Q6','Q7','Q10'])

page(36,'Gehäuse schließen: zuerst ohne Decoder messen','Gehäuseabschluss | beide Triebköpfe',
 'Ein Fehler kann erst durch Dach, Schraube oder Drehgestellstellung entstehen. Die geschlossene Prüfung ergänzt die offenen Messungen.',
 'Alles vom Gleis und Bus getrennt; beide Decoder/Puffer entfernt. Für den geprüften Pfad nötige Elektronik nach dokumentiertem Plan trennen, Restenergie ausschließen.',[
 step(1,'Offenen Zustand aufnehmen: Messpaare und Werte aus [[13]], [[21]]/[[22]] und betroffene Wagenpfade notieren. Schrauben und Litzen in ihrer vorgesehenen Endlage belassen. Ein pauschaler Pieptonvermerk genügt nicht.'),
 step(2,'Isolierte Hilfsclips bei offenem Kopf anbringen. Motorseite nutzt PM1/PM2/PX/PX2 nach [[12]]. Im Gegenkopf je zwei Punkte desselben getrennten Leiters und zwei Punkte des Metallbezugs wählen. Jeder Clip darf nur seine bezeichnete Kontaktstelle greifen.'),
 step(3,'Freie Hilfsleitungsenden nur durch eine vorhandene sichere Öffnung nach außen führen. Nicht zwischen Gehäusehälften, unter Schrauben oder neben Zahnrädern einklemmen. Gibt es keinen sicheren Austritt, bleibt diese geschlossene Messung offen; Gehäuse nicht auf die Leitungen drücken.'),
 step(4,'Gehäuse druckfrei aufsetzen; nur zugehörige Schrauben sicher anziehen. Fahrzeugclips dürfen sich nicht bewegen. Bei geschlossenem Gehäuse <b>positive Vorproben, Isolation und positive Nachproben</b> durchführen. Motorseite: ganze Sechserfolge [[13]]. Gegenkopf: passive Reihe [[21]], keine Motorprobe.'),
 step(5,'Drehgestelle und Kupplungen in normale Endlagen bewegen; je Lage vollständige Reihe wiederholen. Bestätigte getrennte Motor-/Signalpfade gegen Metall bleiben offen; gewünschte passive Leitungen bleiben stabil leitend. Serienwiderstände mit ihrem bekannten Sollwert beurteilen. Nicht durch LEDs auf OL prüfen.'),
 step(6,'Änderung erst beim Schließen: wieder öffnen und eine Ursache nach der anderen prüfen - Litzenlage, Schraube, Halter, Dachkontakt. Ursache beheben und geschlossene Reihe erneut durchführen. Ein halb offenes Gehäuse ist keine Lösung.'),
 tab(['Kopf / Pfad / Lage','Vorprobe','Geschlossener Wert','Nachprobe'],[
 ['________________','________','____________','________'],
 ['________________','________','____________','________'],
 ['________________','________','____________','________']],[1.4,.85,1.2,.85]),
 note('Eine misslungene Nachprobe entwertet den Offenbefund. Bestückte Netze ausschließlich nach ihrer ausgefüllten Messkarte beurteilen. Nach dieser Prüfung sind noch Wiederanschluss und Platzprüfung mit dem echten Decoder nötig.'),
 p('Messpunkte/Fotos ______; Gerät/Bereich ______; sichere Leitungsöffnung ______; Schrauben-/Drehgestelllagen ______; Ergebnis ______.')
 ],'Geschlossene passive Prüfungen bestehen. Gehäuse wieder öffnen und den Abschluss auf [[37]] vollständig ausführen.',sources=['Q1','Q3','Q6'])

page(37,'Wiederanschließen, endgültig schließen und abnehmen','Gehäuseabschluss | Endabnahme',
 'Die Prüfung ohne Decoder bestätigt nicht dessen realen Platzbedarf. Wiederanschlüsse und endgültige Montage werden deshalb nochmals kontrolliert.',
 'Geschlossene passive Prüfung [[36]] bestanden. Fahrzeug weiterhin vollständig stromlos und vom Bus getrennt.',[
 step(1,'Gehäuse öffnen und alle Hilfsprüfleitungen vollständig entfernen. Geplante Anschlüsse wiederherstellen. Sämtliche dadurch betroffenen Soll-/Fremdpfade nach [[21]]/[[22]], Motorlitzen zusätzlich nach [[12]]/[[13]], mit positiven Kontrollen erneut prüfen.'),
 step(2,'Wurde eine Leitung umgelegt oder ein Halter geändert, die zugehörige geschlossene Prüfung wiederholen. Reale Halter-/Bauteilhöhen und Dachgeometrie dokumentieren; bloßer seitlicher Blick beweist keinen verdeckten Freiraum.'),
 step(3,'Decoder stromlos nach [[30]]/[[31]] einsetzen. Tatsächlichen Freiraum, Litzenlage und Wärmeabfuhr prüfen. Decoder nicht in Isolierband/Folie einwickeln. Gefährdende Metallfläche geeignet isolieren und Abstand erhalten. Gehäuse ohne Druck schließen.'),
 step(4,'Innerhalb der zugelassenen Last F0/Richtung, Sound, T1-T9 und kontrollierten Fahrtest am geschlossenen Zug wiederholen. Bei einem neuen Fehler sofort trennen; nicht das Gehäuse unter Spannung öffnen oder drücken.'),
 step(5,'Helligkeit erst jetzt mit Lichtleitern/Gehäuse bei gleichem Umgebungslicht vergleichen. Weiß und Rot getrennt abstimmen; helleren Ausgang dimmen. ESU-Änderung nur auf Einzelaufnahme. Wagen-TRIMM jeweils stromlos minimal verstellen, Werkzeug entfernen, einschalten und vergleichen; Endanschlag nicht erzwingen.'),
 tab(['Endabnahme','Ergebnis / Nachweis'],[
 ['Endgültige Wagenzahl / Reihenfolge / Orientierung','________________________'],
 ['Geprüfte Projekte / Firmware / Innenlichttaste','________________________'],
 ['Lasten / höchste Helligkeit / alleinige hintere Speisung','________________________'],
 ['Gehäuse geschlossen / Bewegung / Wiederanschlussprüfung','________________________'],
 ['F0 / Sound / T1-T9 / Fahrt geschlossen','________________________'],
 ['Freigegebener einheitlicher Anlagenbereich','________________________'],
 ['Beide 60974 weiterhin ab; Signalhalt separat offen/geprüft','________________________']],[2.1,1.4]),
 note('Nach Dimmung oder Projektänderung betroffene Tests wiederholen; nach Leitungslageänderung zusätzlich Gehäuseprüfung. Strombegrenzung muss auch ungedimmt sicher sein.'),
 p('Datum ______; Ergebnis bestanden/offen/fehlgeschlagen ______; verbleibende Abweichung ______. Erst bei vollständig bestandenem Abschluss im bestätigten Bereich betreiben. Puffer und automatischer Signalhalt sind eigene spätere Aufgaben.')
 ],sources=['Q1','Q3','Q4','Q6'])

page(38,'Fehler eingrenzen und später sicher warten','Nachschlagen | Fehler und Wartung',
 'Erst ausschalten und physisch trennen. Die letzte Änderung und den genauen fehlgeschlagenen Test dokumentieren; keine Blindkorrektur.', '',[
 tab(['Beobachtung','Stromlos prüfen','Nicht tun'],[
 ['Sofort Überlast','RT/GE/0, 21MTC-Sitz, Metallkontakt, zuletzt ergänzte Baugruppe','Wiederholt einschalten'],
 ['Nur mit Gehäuse','Schraube, Dachkontakt, Litzenquetschung, realer Decoderraum','Mit Kraft zuschrauben'],
 ['Nur in Kurven','Deichsel-/Drehgestelllitzen, Zug, Scheuern und Kontaktkontrollen','Günstige Stellung als bestanden notieren'],
 ['LED dunkel/falsche Farbe','Plus, Serienwiderstand, Polung, Mapping getrennt','Widerstand brücken oder direkt ans Gleis'],
 ['Motor brummt/warm','Freilauf, Bürsten, Drosselzweige, Isolation','Mehr Fahrstufe oder blockiert testen'],
 ['Slave folgt nicht','Eigene Masterkennung, Originalexport, Firmware, tatsächliche Ausgangsreaktion','Gleiche DCC-Adresse als mfx-Erfolg ausgeben'],
 ['Alle Wagen richtungsabhängig dunkel','Innenlicht-Taste, Bedingung und GE-AUX-Zuordnung','F0 als zusätzliche Innenlichttaste verwenden'],
 ['Ab einer Kupplung dunkel','Jeden betroffenen Kontakt bis O/L und Einzelübergang','Nur Gesamtdurchgang messen'],
 ['Lichtausfall plus Sound-Neustart','Stromaufnahme, Last und Spannungseinbruch','Puffer auf Verdacht anschließen'],
 ['CV-Lesefehler nach Schreiben','Versorgung, Kontakt, Quittierung; tatsächlichen Zustand feststellen','Schreibbefehl blind wiederholen oder Reset']],[1.1,1.7,1.25]),
 h('Verbindlicher Wartungsweg'),
 step(1,'Zug stromlos machen, Kopf vom Gleis und Bus trennen. Decoder an den Kanten abziehen und auf die geeignete bestätigte Einzelaufnahme setzen. ESU nur dort per DCC ändern; Märklin 60977 am passenden Märklin-Werkzeug bearbeiten.'),
 step(2,'Altprojekt/Altwerte sichern, nur die begründete Änderung übertragen und frisch rücklesen. Ein fehlender ACK kann trotz ausgeführtem Schreiben auftreten. Die aus ESU-Unterlagen bekannte 150-Ω-Hilfe für andere Fx-micro-Modelle nicht auf 59649 übertragen.'),
 step(3,'Stromlos wieder einsetzen. Betroffene Anschluss-/Steck-, Funktions-/Synchronisations- und bei Lageänderung Gehäuseprüfungen wiederholen. Datum und neuer Projektstand gehören zum Zug.'),
 p('Fehlerprotokoll: Karte/Test ______; Aufbau/letzte Änderung ______; Soll/Ist ______; Messpunkte/Parameter ______; Vor-/Nachprobe ______; Ursache/Korrektur ______; Wiederholung ______.')
 ],sources=['Q1','Q6','Q17'])

page(39,'Puffer und Signalhalt erst als eigene Ergänzung','Später | Grenzen des jetzigen Umbaus',
 'Die Werkstattabnahme bestätigt den beschriebenen Grundaufbau. Pufferanschluss und anlagenspezifische Halteabläufe brauchen eigene passende Daten und Tests.', '',[
 h('60974: jetzt beide abgetrennt lassen'),
 p('Grundsätzlich ist 60974 für 60977 vorgesehen. Märklins dokumentierte Steckbuchse sitzt jedoch auf dem Märklin-Träger; der 60977 steckt hier auf LoDi 511. Der konkrete unveränderte Anschlussweg dieser Revision ist noch festzulegen. K1, S2 und Front-VCC sind dafür keine bestätigten Pufferanschlüsse.'),
 step(1,'Für eine spätere Ergänzung vorn: beide LoDi-Seiten/Revision, 60977-Firmware und unveränderten 60974-Stecker dokumentieren. Passenden classicSUSI-Abgriff samt tatsächlicher Kontaktansicht eindeutig bestätigen. Kein Steckerabschneiden oder Pin-Abzählen als Abkürzung.'),
 step(2,'Nur einen passend angebundenen Puffer am 60977 vorsehen; hinten keinen 60974 am ESU. Vorher Anschluss, Lade-/Restspannungsverhalten, Motorpufferung und Abschalt-/Nachlaufverhalten festlegen. Danach Anschluss-, Last-, Neustart- und Halteprüfungen wiederholen. Reset, Einmessfahrt und Pufferparameter sind getrennte Vorgänge.'),
 h('CS3-Signalhalt: der Zug braucht einen echten Haltbefehl'),
 step(3,'Reale Kontaktabschnitte in der CS3 auf Belegt/Frei prüfen. Je Richtung Signaladresse, Brems-/Haltekontakt, Schutzpunkt, Zuglänge und eindeutig zugeordneten ICE-Eintrag dokumentieren. Ein S88-Kontakt meldet keine automatische mfx-Identität.'),
 step(4,'Erst damit die Ereignisfolge erstellen: am Bremskontakt passende Annäherung, am Haltekontakt Fahrstufe 0 für genau diesen ICE. Ein rotes Signalbild allein hält nicht an. Gleis kann für Licht/Sound digital versorgt bleiben.'),
 step(5,'Zuerst ohne Fahrbewegung Logik prüfen. Danach langsam in beiden Richtungen mit freiem Auslauf: Halt, Durchfahrt, bereits belegter Kontakt beim Start, Signalwechsel nach Bremskontakt, fehlende/falsche Meldung und Neustart. Zugspitze und Nachlauf müssen vor dem Schutzpunkt bleiben.'),
 note('Der lange RT-Schleiferbus darf keinen fremden Booster-, Programmier-, Brems- oder Analogabschnitt überbrücken. Vor einer Bereichsgrenze den gesamten Zug anhalten. Puffer können Nachlauf trotz Gleisabschaltung verursachen.'),
 p('<b>Bis zur eigenen Anlagenabnahme:</b> ICE beaufsichtigt und von Hand anhalten. Vorhandene Rückmeldeverdrahtung unter der Anlage bleibt erforderlich. Eine bestandene Synchronisation überträgt weder Bremsabschnitterkennung noch Lichtmapping oder Helligkeit.')
 ],sources=['Q1','Q3','Q7','Q15','Q16','Q20'])

SOURCES=[
 ('Q1','Märklin 60975/60976/60977: Einbau, Träger, CV8, CV51/52, Grenzwerte','https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf'),
 ('Q2','Märklin 60941/60943: Original-Montagezeichnung, 12/2022','https://static.maerklin.de/damcontent/e3/bb/e3bb202fe80385cc96835d783af5e1821670919973.pdf'),
 ('Q3','LoDi Motor WiB ICE-M(-S): Anschlüsse, Revisionen, Bilder des 33701','https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/'),
 ('Q4','LoDi WiB ICE-M: Wagenplatinen und Anschlussvarianten','https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-wib-ice-m/'),
 ('Q5','LoDi Frontmodule: Produktangaben, ohne Vorwiderstände','https://www.lodi-shop.de/produkte/beleuchtung/lodi-wib-ice-m/'),
 ('Q6','ESU LokPilot 5: Betriebsanleitung, 21MTC/MKL, Einbau und CVs','https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e'),
 ('Q7','ESU: Master/Slave-Adress-Synchronisation','https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/'),
 ('Q8','RailCommunity RCN-121: 21MTC-Schnittstelle, 08.12.2024','https://normen.railcommunity.de/RCN-121.pdf'),
 ('Q9','Märklin CS3-Changelog 2.6.0: CV-Lesen und unmittelbares Schreiben','https://www.maerklin.de/fileadmin/media/service/cs3/Maerklin_CS3_v2.6.0_changelog.pdf'),
 ('Q10','Märklin mSD3/mLD3: CV-Tabelle, Effekte und Bedingungen','https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf'),
 ('Q11','ESU: originale LokProgrammer-Software / Versionshinweise','https://www.esu.eu/download/software/lokprogrammer/'),
 ('Q12','ESU: geänderte CVs anzeigen und vor dem Speichern sichern','https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/'),
 ('Q13','JMRI: Registerdefinition CV191/192-195, festgelegter Quellstand','https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v5standardCVs.xml#L993'),
 ('Q14','TrainControl: originale CS3-Testdaten mit uid, mfxuid und sid','https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/lokomotive_cs3.cs2#L4'),
 ('Q15','Märklin CAN-Protokoll 2.0: Decoder-UID, Bind und Verify','https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf'),
 ('Q16','Märklin Mobile Station: zulässige Anschlüsse / Gleisbox','https://static.maerklin.de/damcontent/2a/47/2a470bed20017f68f92306725d49fca81702905959.pdf'),
 ('Q17','RailCommunity RCN-216: DCC-Serviceprogrammierung und Quittierung','https://normen.railcommunity.de/RCN-216.pdf'),
 ('Q18','Märklin 60970: Prüfstand und Schalterstellungen','https://static.maerklin.de/damcontent/e3/85/e385c3c228363431569450fe58ba95481677562275.pdf'),
 ('Q19','ESU 53900: Produktangaben, echte Ausführung zusätzlich abgleichen','https://www.esu.eu/produkte/profi-pruefstand/'),
 ('Q20','Märklin 60974: Anschluss, Voraussetzungen und Pufferbetrieb','https://static.maerklin.de/damcontent/c2/76/c276c3bb1b06e89061b9588a4be1f8e41760429428.pdf')
]
page(40,'Quellen, Bilder und Geltungsbereich','Nachschlagen | Quellen',
 'Kurzbelege Q1-Q20 stehen auf den Arbeitskarten. Die verlinkten Originalquellen sind hier zusammengeführt.', '',[
 *[small(f'<b>{n}</b> <a href="{url}" color="#145B64">{label}</a>') for n,label,url in SOURCES],
 h('Bildherkunft und verbindliche Referenz'),
 p('Referenz ist die vom Nutzer benannte <b>ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf</b>, 92 Seiten. REV11 ordnet ihre Arbeitsinhalte neu, erhält notwendige Prüfungen und arbeitet die Recherchekorrekturen vom 10./11.09.2026 ein. Historische Prüfdebatten und doppelte Kurzfassungen entfallen.'),
 p('Eigene 2976-/LoDi-Fotos stammen unverändert aus REV10. Märklin-Zeichnungen stammen aus Q1/Q2. Ergänzte hochauflösende LoDi-Fotos zeigen den Vergleichsumbau 33701 (Q3), nicht deinen fertig umgebauten Zug. Nummern/Leitlinien liegen als separate Markierungen über Originalfotos. Funktionsschemata sind eigene technische Zeichnungen ohne Behauptung einer maßstäblichen Padlage.'),
 small('Die Anleitung ist redaktionell und visuell geprüft. Reale Gerätewerte, Messungen und Funktionstests sind vom Anwender einzutragen. Kein Beispielbild bestätigt unsichtbare Leiterbahnen, den vorhandenen Halter oder eine bereits bestandene Inbetriebnahme. Quellenstand: 11.09.2026.')
 ],sources=[])

# Corrections from independent coverage review, before final pagination.
PAGES[5]['blocks'].insert(0,step('A','60977-Zustand sichern: Anschlussadapter vom 60971 abnehmen. Nur den 60977 nach sichtbarem Index am abgenommenen 21MTC-Adapter einsetzen, dann Adapter am Programmer anschließen. Nur USB, alle übrigen Anschlüsse frei. Im mDecoderTool3 „Decoder / Decoder-Informationen anzeigen“: Typ/Firmware notieren; danach „Decoder / Decoder auslesen“ und Einstellungen als neues Projekt sichern. Sounds werden nicht mit ausgelesen. Keine Firmwareaktualisierung wählen. Nach Lesen zuerst Adapter abnehmen, dann Decoder abziehen; im Betrieb keine Kontakte berühren.'))
PAGES[5]['sources']+=['Q21','Q22']
PAGES[7]['blocks'][1]['text']+=' Auch den erneuten Lesebefehl für eine bereits gelesene Zeile eindeutig an deiner Version dokumentieren. Ist dessen Wirkung unklar, diesen Leseablauf noch nicht am Decoder ausführen.'
PAGES[9]['blocks'][1]['text']=PAGES[9]['blocks'][1]['text'].replace('Alle vier Tabellenzeilen durchführen','Alle vier Tabellenzeilen durchführen; mindestens fünf Richtungswechsel im Stand wiederholen')
PAGES[9]['blocks'][2]['text']+=' Danach beide Reihenfolgen prüfen: nur Master versorgen, Slave ergänzen; nur Slave versorgen, Master ergänzen. Zum Umstecken immer Gesamtversorgung trennen; getrennte Einschaltreihenfolge nur mit dafür geeigneten separat schaltbaren Aufnahmeeingängen herstellen.'
PAGES[9]['blocks'][-2]['text']+=' Nach eindeutiger Zuordnung aktiv selbständig steuerbarer Slave: Test nicht bestanden.'
PAGES[15]['before']+=' Ausgefüllter Messplan [[22]] einschließlich Vorzustand liegt vor.'
PAGES[15]['blocks'][0]['maxh']=140
PAGES[19]['before']+=' Den ausgefüllten Plan [[22]] vor Befestigung bereithalten.'
PAGES[16]['blocks'][3]['text']='Frontzweige erst nach der LED-Karte [[18]] anschließen. '+PAGES[16]['blocks'][3]['text']
PAGES[20]['blocks'][4]['text']+=' Nach Abkühlen Verbindung und Fremdpfade prüfen, dann vollständig mit Schrumpfschlauch umschließen. Beim Schrumpfen Platine, LED und Kunststoff vor Hitze schützen.'
PAGES[23]['blocks'][2]['maxh']=133
# Larger high-resolution source drawings; source bitmaps are unchanged.
from manufacturer_figures import FIGURES
for n,index,kind,maxh in [(10,2,'motor_60941',218)]:
 spec=FIGURES[kind];PAGES[n]['blocks'][index]=photo(spec['path'],maxh,list(spec['crop']))
for col,kind,maxh in [(PAGES[19]['blocks'][0]['columns'][1],'carrier_60977',190),(PAGES[31]['blocks'][0]['columns'][0],'insertion_21mtc',335)]:
 spec=FIGURES[kind];col[0]=photo(spec['path'],maxh,list(spec['crop']))
PAGES[11]['blocks'][0]['maxh']=201
PAGES[12]['blocks'][0]['maxh']=198
# Direct source pages kept compact and verifiable.
SOURCES[4]=('Q5',SOURCES[4][1],'https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/')
SOURCES.extend([
 ('Q21','Märklin Programmer 60971: Adapterfolge und ausschließlich USB','https://static.maerklin.de/damcontent/21/3e/213ee6e47c4afa9ad2282158bf7728441660728698.pdf'),
 ('Q22','Märklin mDecoderTool3 v3.60: Typ/Firmware und Einstellungen lesen','https://streaming.maerklin.de/public-media/mdt3/pdfs/D_mDecoderTool3_A5_v360.pdf')])
PAGES[40]['goal']='Kurzbelege Q1-Q22 stehen auf den Arbeitskarten. Die verlinkten Originalquellen sind hier zusammengeführt.'
PAGES[40]['blocks']=[small(f'<b>{n}</b> <a href="{url}" color="#145B64">{label}</a>') for n,label,url in SOURCES]+PAGES[40]['blocks'][20:]
# Re-reading already displayed CVs is a separate, documented CS3 action.
PAGES[7]['blocks'][1]['text']='„Bearbeiten > Loks bearbeiten“ öffnen, genau den Serviceeintrag wählen und „Konfigurieren“ öffnen. Programmiergleis verwenden, nicht PoM. CV-Nummernfeld und Wertefeld unterscheiden; fehlende Zeilen jetzt ohne Decoder vorbereiten. Für eine erneute frische Rücklesung den Menüpunkt <b>„Decoder auslesen“</b> identifizieren: Er liest die vorbereitete Liste erneut. Bildschirm und tatsächliche Version dokumentieren.'
PAGES[7]['blocks'][3]['text']='CV8 ausschließlich lesen; Wertefeld nicht ändern. Erwartung beim ESU: 151. Für die Wiederholung <b>„Decoder auslesen“</b> wählen, Abschluss abwarten und fehlerfreie Zeile prüfen. Beide Ergebnisse notieren. Antippen einer bereits gelesenen Zeile oder ein stehen gebliebener Wert beweist keine neue Lesung. CV8=151 bestätigt den Hersteller, nicht Artikel und Firmware.'
PAGES[8]['blocks'][4]['text']='Abschluss abwarten, dann im Menü <b>„Decoder auslesen“</b> die vorbereitete Liste erneut lesen. Dieselbe CV in derselben gegebenenfalls nötigen Indexgruppe fehlerfrei prüfen. Der Wert muss exakt dem Ziel entsprechen. Ergebnis notieren; erst dann nächste Kartenzeile. Bloßes erneutes Antippen eines angezeigten Wertes reicht nicht.'
PAGES[9]['blocks'][2]['text']='Versorgung unterbrechen und nach Neustart wiederholen. Danach beide Reihenfolgen mit geeigneten separat schaltbaren Gleiseingängen testen: Master vor Slave; Slave vor Master. Zum Umstecken Gesamtversorgung trennen. Alte gespeicherte Slave-Zeile von aktiver Zweitanmeldung unterscheiden; keine unbekannten Einträge probeweise fahren.'
PAGES[9]['check']='Ausgänge, Einschaltfolgen, alte/neue SID, Kennungsquelle, Projekte und Firmware dokumentieren. Ohne SID-Anzeige einen konkret bestätigten passiven Datennachweis verwenden; Bind allein genügt ohne Anmeldung/Steuerbarkeit nicht. Erst bei bestandenem Gesamtprotokoll den elektrischen Zugumbau beginnen.'
PAGES[21]['before']+=' Für passive Isolation Ω-Autorange oder höchsten Ω-Bereich verwenden.'
PAGES[27]['blocks'][1]['text']='Passendes ICE-Soundprojekt mit dem Märklin-Werkzeug öffnen, Quelle/Version/Funktionstasten dokumentieren und niedrige Anfangslautstärke einstellen. mfx aktiv lassen. Motortyp und Tabellen-Sollwerte abgleichen; keinen Glockenanker-/Sinus-Prüfstandwert übernehmen. Unter neuem Namen sichern, übertragen und Einstellungen erneut lesen. Sounddatei gesondert aufbewahren; bloßes Auslesen sichert die Sounds nicht.'
PAGES[9]['before']+=' Für Sound nur bekannte Tasten eines dokumentierten Projekts; keine Einmessfunktion.'
# Preserve optional branches and the concrete boundaries of later extensions.
PAGES[34]['before']=PAGES[34]['before'].replace('Wagen [[23]]-[[26]] geprüft','Wagen [[23]]-[[25]] geprüft; bei gewählter Radkontaktoption zusätzlich [[26]]')
PAGES[26]['blocks'][5]['text']+=' Wagen anschließend auf stromlosem Gleis von Hand rollen lassen und mit dem Vorzustand vergleichen. Bei Klemmen Federlage oder Litze korrigieren.'
PAGES[26]['blocks'][6]['text']='Nach elektrischer Abnahme darf nur der Testwagen den zugehörigen Meldeabschnitt belegen; andere Köpfe/Wagen außerhalb halten. Frei - belegt - frei in mehreren Radstellungen und beiden Orientierungen prüfen, gegebenenfalls mit Innenlicht aus und an getrennt. Eine Meldung identifiziert nicht automatisch den ICE; Signalhalt separat nach [[39]].'
PAGES[39]['blocks'][3]['text']+=' 60977-Firmware mindestens 3.2.0.1 bestätigen. Anfangs Motorpufferung ausgeschaltet lassen. Die Wagenbeleuchtung ist durch diesen Anschluss nicht automatisch gepuffert.'
PAGES[39]['blocks'][6]['text']=PAGES[39]['blocks'][6]['text'].replace('Erst damit die Ereignisfolge erstellen:','Erst damit die Ereignisfolge <b>bei Signalhalt</b> erstellen:')
# A bounded, explicitly sourced firmware diagnosis closes the software-only route
# without turning optional LokProgrammer hardware into an unstated prerequisite.
PAGES[8]['before']='Masterdaten/Originalvergleich [[5]]/[[6]] und erfolgreiches Grundlesen [[7]] vorhanden. Erst Firmwarestand unten erheben; eine ausdrücklich gemeldete Updateanforderung vor Synchronisationsänderungen klären. Die persönliche Schreibkarte nennt CV, nötigen Index sowie Alt-/Zielwert.'
PAGES[8]['blocks'].insert(0,note('Nach bestandenem Grundlesen: Altwerte CV31/CV32 sichern. Mit dem unten beschriebenen Einzelwertverfahren CV31 = 0, dann CV32 = 255 setzen und rücklesen. CV285-288 <b>nur lesen</b>. Version = CV288.CV287.(256 × CV286 + CV285). Danach CV31/CV32 auf die gesicherten Altwerte zurückstellen und rücklesen. Bei Fehler STOP, Zustand dokumentieren. Diese Diagnose folgt der JMRI-Einbindung für LP5/MKL; sie ist noch kein Test deines Decoders. CV7 allein liefert nicht diesen vollständigen Stand.','ZUERST: FIRMWARE AUSLESEN','info'))
PAGES[8]['sources']+=['Q23']
SOURCES.append(('Q23','JMRI LP5/MKL: Decoderinformationen und Firmwarebytes, definierte Quelle','https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml'))
PAGES[40]['goal']=PAGES[40]['goal'].replace('Q1-Q22','Q1-Q23')
PAGES[40]['blocks'].insert(22,small('<b>Q23</b> <a href="'+SOURCES[-1][2]+'" color="#145B64">'+SOURCES[-1][1]+'</a>'))
# Final semantic and print-quality corrections.
PAGES[7]['blocks'][4]['text']='CV191, 192, 193, 194 und 195 einzeln frisch lesen und als Altwerte eintragen. Jede Zeile braucht einen eigenen Leseerfolg. Firmware und zusätzliche indizierte Altwerte folgen erst nach [[8]]. Anschließend STOP und Versorgung trennen.'
PAGES[7]['check']='Zwei fehlerfreie CV8-Lesungen und Altwerte CV191-195 liegen vor. Artikel, Aufnahme, Lasten und CS3-Version sind dokumentiert. Firmware und indizierte Altwerte werden anschließend nach [[8]] erhoben.'
PAGES[8]['title']='CS3: Firmware lesen und Einzelwerte schreiben'
PAGES[8]['goal']='Zuerst die begrenzte Firmwarediagnose, danach die vollständige persönliche Synchronisationskarte. Keine fremden Beispielwerte übertragen.'
PAGES[8]['blocks'][0]=note('Vor Verbindung zwei Leselisten vorbereiten: <b>A nur CV31/CV32</b>, <b>B nur CV285-288</b>. Mit A beide Altwerte sichern; CV31 = 0, dann CV32 = 255 einzeln nach dem Ablauf unten setzen und rücklesen. Erst bei bestätigtem 0/255 Liste B wählen: CV285-288 <b>nur lesen</b>. Version = CV288.CV287.(256 × CV286 + CV285). Dann wieder A wählen, beide Index-Altwerte zurückstellen und rücklesen. Beim Listenwechsel niemals Vorlagenwerte schreiben. Diese Diagnose folgt JMRI für LP5/MKL; kein bereits bestandener Gerätetest. CV7 allein genügt nicht.','ZUERST: FIRMWAREDIAGNOSE','info')
PAGES[27]['blocks'][3]['text']='Nur bei Innenlicht über AUX4: CV51 frisch rücklesen; Ziel stimmt, Bit4 = 0, übrige Bits entsprechen dem Altwert. Bei Innenlicht über AUX1 keine vorsorgliche AUX4-Änderung fordern. Nach jedem späteren Projekttransfer die tatsächlich benötigte Ausgangsart und das Mapping erneut prüfen.'
PAGES[11]['blocks'][2]['headers'][0]='Bild-Nr.'
PAGES[23]['blocks'][1]['text']=PAGES[23]['blocks'][1]['text'].replace(' Das Foto nicht auf volle Seitenhöhe strecken.','')
PAGES[19]['blocks'][0]['widths']=[1,1.35]
PAGES[19]['blocks'][0]['columns'][1][0]['maxh']=235
# Keep the product copy focused on work, not the editorial process.
PAGES[22]['goal']='Für bestückte Elektronik werden Bauteilpfad, Prüfparameter und erwartetes Verhalten vor der Messung festgelegt. Diese sechs Angaben machen die Messung am eigenen Aufbau nachvollziehbar.'
PAGES[2]['blocks'][2]['text']=PAGES[2]['blocks'][2]['text']
