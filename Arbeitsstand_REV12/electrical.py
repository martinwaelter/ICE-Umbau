from overrides import p,h,small,step,note,tab,fig,PROJECT

def apply_electrical(P):
 def page(n,title,phase,goal,before,blocks,check='',sources=[]):
  P[n]={'n':n,'title':title,'phase':phase,'goal':goal,'before':before,'blocks':blocks,'check':check,'sources':sources}
 P[3]['blocks'][0]['maxh']=110
 P[3]['blocks'][2]['text']='Vom Gleis nehmen; alle Quellen und Wagenbus trennen, Decoder und beide 60974 entfernen. Vor Ω-Messung vorhandene Wagenelkos identifizieren. Leere C1/C2-Pads brauchen keine Entladung. Den ausgebauten 60974 getrennt lassen; nicht öffnen.'
 P[3]['blocks'].insert(3,note('Nur für identifizierte Wagenelkos bis 470 µF / 35 V: COM/VΩ, V DC; Funktion vor/nach der Reihe an einer einzelnen 1,5-V-Batterie prüfen. Direkt am Elko messen; über Nennspannung oder unbekannter Speicher: stoppen. Nachgemessene 10 kΩ ≥0,5 W mit isolierten Clips eine Minute parallel anschließen. Spannung messen; Widerstand abnehmen, 10 s warten, nachmessen. Erst zu Ω wechseln, wenn mit mindestens 0,01-V-Auflösung keine Restspannung angezeigt wird und die Geräteanleitung es zulässt. Bei Wiederanstieg erneut entladen/Restquelle suchen. Kein Drahtkurzschluss.','VOR WIDERSTANDSMESSUNGEN','info'))
 P[3]['blocks'].append(small('Eigene Beispielrechnung: 35 V an 10 kΩ ergeben 0,123 W. Mit angenommenen +20 % bei 470 µF und R +5 % folgt τ =5,92 s. Eine Minute ist die erste Entladezeit; die Nachmessung entscheidet. Kein Universalweg für größere Puffer.'))
 P[3]['sources']+=['Q4','Q34']
 page(5,'Platinen: eigene Anschlüsse und Montage prüfen','Elektrische Prüfung | bestückte Teile',
  'Du prüfst deine Verbindungen und Montagestellen. Unveränderte Elektronik erhält keine erfundenen Innenwiderstände oder pauschalen OL-Sollwerte.',
  'Alles stromlos, Decoder/Puffer ab, Wagenbus getrennt. Restenergie nach [[3]]. Eigene beidseitige Platinenfotos und passende Revisionszeichnung bereitlegen.',[
  step(1,'Beschriftung und Revision mit der richtigen Herstelleransicht abgleichen. Nur die dazugehörigen Pads verwenden. Unklare Revision oder Brücke zuerst an genau diesem Anschluss klären; rote AUX-Auswahl und weißes Türlicht-SJ2 nicht verwechseln.'),
  tab(['Neue Verbindung','So wird sie geprüft'],[
  ['Vorn','Freie Leitung vor Löten nach [[4]] prüfen. Danach Schleifer→SW, Kupplung-RT→RT, Kupplung-GE→GE und Radleitung→MASSE jeweils Kontakt bis Zielpad.'],
  ['Hinten','Eigener Schleifer und RT bis S/RT/B/GR-Dreierpunkt; Radkontakt bis 0/GL. Neue LED-/Adapteradern zunächst einzeln passiv prüfen.'],
  ['Wagen','Jeder RT-Kontakt bis O, jeder GE-Kontakt bis L. Bekannte O-O- und L-L-Längspfade getrennt messen.'],
  ['Messung','COM/VΩ, Ω; Spitzen-/Kontaktkontrolle vor und nachher. Soll: stabiler Leitungswert des bekannten direkten Pfads. Bei normaler Bewegung kein Aussetzen.']],[.55,3.9]),
  step(2,'Mit Lupe jede eigene Lötstelle beidseitig prüfen: kein Zinnsteg, Drahtfaden oder abgelöstes Pad. Nachbarpads, Front-VCC, GE/RT, Schraubenflächen und Unterseite ansehen. Isolierung reicht nahe an die Lötstelle; freie Enden sind einzeln gesichert.'),
  step(3,'Befestigung nach [[18]] abgleichen: Ringrolle, Auflage und Schaftweg müssen zur Revision passen. SW-RT nur bei bestätigter direkter Herstellerbeschaltung als Durchleitung werten. Kein Messwert allein erklärt die zulässige Netz- oder Schraubenverbindung.'),
  step(4,'Verdächtige Änderung: nur die gerade hinzugefügte Litze stromlos abtrennen; nun passive Litze und Kontaktzuordnung prüfen. Bleibt der Fehler an der Platine, Bauteil-/Revisionsfrage gezielt klären. Keine Bauteile entfernen, um einen Offenwert zu erzeugen.'),
  note('Vorher-/Nachherwerte bestückter Querpfade sind nur ergänzende Diagnose: gleicher geeigneter Gerätebereich, Polung, Ausgangszustand und Verlauf. Kein fixes 5-Sekunden-Rezept. Kein Unterschied beweist keinen fehlerfreien Ausgangszustand. Wenn Geräteeignung unklar ist, diesen Zusatzvergleich auslassen; Pflicht bleiben die oben genannten Anschluss-/Sichtprüfungen.','OPTIONALER ELEKTRONIKVERGLEICH','info'),
  p('Revision/Quelle ______; geprüfte Kontakt-Pad-Paare ______; Sichtprüfung beidseitig ______; Montage/Bewegung ______; Abweichung und Korrektur ______.')
  ],'Bekannte Anschlüsse, eigene Leitungen, passive Pfade und Montage sind geprüft. Kontrollierter Einzel-Ersttest nach [[28]]; Motorisolation bleibt separat Pflicht.',sources=['Q1','Q3','Q4','Q6','Q27'])
 page(17,'Front-LEDs: jeden Farbzweig sicher begrenzen','Beleuchtung | vor dem Anschluss',
  'Vorn bleibt die passende LoDi-Beschaltung; hinten bekommt jede Farbe einen eigenen Widerstand.',
  'Eigene 514-Einsätze und Plus/Weiß/Rot anhand Beschriftung/Herstellerbild zuordnen. Keine LED ungeschützt an Gleis oder Decoder anschließen.',[
  {'type':'columns','widths':[.8,2.2],'gap':16,'columns':[[
    {'type':'figure','path':str(PROJECT/'Arbeitsstand_REV11/bilder_quellen/front_led_kabel_1.jpg'),'maxh':140},
    small('LoDi-Foto: red / VCC / white. Eigene Aufdrucke abgleichen.')
   ],[
    p('<b>Vorn:</b> Passende unveränderte LoDi-Frontkombination; R4/R5 erhalten. Front-VCC an Plus, L_WS an Weiß, L_RT an Rot. Tatsächlichen Zweig nach [[42]] prüfen; keine Grenzdaten für die passende Originalbeschaltung erfinden.'),
    p('<b>Hinten:</b> Plus an +Ub des 59649; Rot über R_Rot an LV, Weiß über R_Weiß an LR. Zulässigen Strom und höchste Versorgung samt Toleranz je Farbe belegen. Herstellerdaten des tatsächlichen Einsatzes verwenden.')
   ]]},
  fig('led',110),
  tab(['Rechenschritt je Farbe','Vorgehen'],[
   ['Konservativer Mindestwiderstand','U_LED,min darf mit 0 V angesetzt werden: R_min ≥ U_max / I_zulässig. Dadurch ist kein geratener LED-Spannungsabfall nötig.'],
   ['Normwert und Toleranz','R_nom × (1 − Toleranz) muss mindestens R_min sein. Nächstgrößeren passenden Normwert wählen.'],
   ['Verlustleistung','P_max = U_max² / R_tatsächlich,min. Für den Einbau mindestens Faktor 2 Reserve vorsehen; Datenblatt/Temperatur beachten.'],
   ['Tatsächliche Daten','Quelle LED/I_zulässig ______; U_max/Quelle ______; R_nom/Toleranz/Leistung ______; gemessener R ______.']],[1,2.5]),
  step(1,'U_max aus belegtem Ausgangs-/Versorgungsmaximum bestimmen, nicht aus einem einfachen AC-Wert am Gleis. Ein DC-Mittelwert über +Ub/LV zeigt keine sichere Spitze. Vor Einschalten Widerstände einzeln abgetrennt nachmessen; jeweils einen pro Farbe einbauen.'),
  note('R4/R5 nur abzulesen und hinten zu kopieren reicht nicht: LED-Revision, Zweigaufbau und höchste Zweigspannung müssen vergleichbar sein. Fehlen die hinteren Daten, drei LED-Leitungen einzeln isoliert lassen. Mechanik, Motorprüfung und hinterer elektrischer Ruhetest dürfen weitergehen; Lichtabnahme bleibt offen.'),
  small('Eigene konservative Auslegung; Strom in Ampere. Messpunkte und tatsächliche Prüfung auf [[42]].')
  ],'Vorderer Originalpfad passt; hintere Widerstände sind begründet oder die hinteren LEDs bleiben ausdrücklich getrennt.',sources=['Q3','Q5','Q6'])
 for block in P[17]['blocks']:block['after']=5
 page(42,'LED-Zweige mit dem Multimeter prüfen','Beleuchtung | während des Einzel-Ersttests',
  'Die Strombegrenzung muss vor dieser Messung feststehen. Es wird jeweils nur ein Farbzweig eingeschaltet; der Motor steht.',
  'Genaues Multimeter-Modell und Handbuch prüfen: abgesicherter Stromeingang, Messbereich, zulässige Dauer und Gleichspannungsmessung. Bei ungeeignetem Gerät den Widerstands-Spannungsweg verwenden.',[
  fig('led_measure',148),
  step(1,'Ohne Versorgung zugänglichen Widerstand und beide Anschlüsse markieren. Multimeter COM/VΩ, V DC. Isolierte Clips direkt über dem Serienwiderstand anbringen. Nur diese Farbe ungedimmt einschalten; Spannung U_R ablesen. Ausschalten, Clips entfernen. Mit separat gemessenem R ergibt I_mittel = U_R/R. Dies benötigt keine Strombuchse.'),
  step(2,'Direkte Strommessung: stromlos vorn die Farbader zwischen LED und L_WS/L_RT öffnen, hinten zwischen Widerstand und LV/LR. Abgesicherten Strombereich laut Handbuch wählen. Rot zur LED-/Widerstandsseite, COM zur Platinenseite; nur in Reihe. Farbe ungedimmt einschalten, Wert notieren, ausschalten. Gerät entfernen, Draht wiederherstellen; Rot zurück in V/Ω. Kein separates R-Messen nötig.'),
  note('Ein getakteter oder welliger Verlauf liefert im DC-Bereich einen Mittelwert. Er ersetzt keine obere Stromgrenze. Maßgeblich bleibt die konservative U_max/R_min-Auslegung auf [[17]]. Ein MAX-Knopf allein bestätigt keine geeignete Spitzenwerterfassung.'),
  step(3,'Beide Farben getrennt prüfen. Am gemeinsamen Kopf-Test den Master bedienen; am synchronisierten Gegenkopf ist eine Einzel-F0-Reaktion ohne Master nicht vorausgesetzt. Unter Spannung keine Klemme umsetzen. Jede wiederhergestellte Lötstelle nach [[5]] ansehen und auf richtige Verbindung prüfen.'),
  tab(['Kopf / Farbe','R separat','U_R / I_mittel','Auslegung eingehalten'],[
   ['Vorn Weiß / Rot','____ / ____','____ / ____','________'],
   ['Hinten Weiß / Rot','____ / ____','____ / ____','________']],[1.2,.8,1.1,1]),
  p('<b>Kein zugänglicher Widerstand:</b> R4/R5 nicht zum Messen auslöten; keine Spitze zwischen 21MTC-Pins. Direkte Strommessung an zugänglicher Serienleitung nach Schritt 2 verwenden: bei „R separat“ und U_R „entfällt“ eintragen. Alternativ passende Hersteller-Zweigwerte heranziehen. Hintere Widerstandsauslegung bleibt Pflicht.')
  ],'Eigene Messwerte passen zur bereits begründeten Beschaltung; keine Messleitung bleibt am Fahrzeug. Ungeklärte hintere LEDs bleiben getrennt.',sources=['Q1','Q3','Q6','Q27'])
 page(28,'Ersttest und vollständige Lastabnahme unterscheiden','Inbetriebnahme | mit deiner CS3',
  'Der kontrollierte erste Strom ist ein eigener Prüfschritt. Er benötigt die vorherigen Anschlussprüfungen, aber keine schon erfundenen späteren Messergebnisse.',
  'CS3-Programmiergleis vollständig von der Anlage getrennt. Hauptgleisstecker ab, keine andere Quelle. Einzelkopf ohne Wagen/Puffer; freie Kontakte isoliert.',[
  tab(['60977: Herstellergrenze','Maximalwert'],[['Motor dauernd','1,1 A'],['Jeder verstärkte Licht-/AUX-Ausgang','250 mA'],['Licht und AUX zusammen','300 mA'],['Gesamtlast','1,6 A']],[2.5,1]),
  step(1,'Ohne Fahrzeug GFP3-Leerwert unter System/Gleis-Einstellungen/GFP3-Daten aufrufen und notieren. STOP, einen Kopf aufsetzen, Fahrstufe 0, F0/Sound aus. STOP aufheben. Abschaltung, rasch steigender Ruhestrom, Neustarts oder unerwarteter Motorlauf: sofort STOP, physisch trennen und Ursache suchen.'),
  note('Märklin nennt maximal 1,5 A am Programmiergleis. Das ist kein eingestellter 250-mA-Schutz für einen AUX. GFP3 beobachtet den Gesamtstrom; keine Abschaltung beweist weder Motorisolation noch richtige Zweigströme. Hersteller-Ersttest und numerische Lastabnahme werden getrennt dokumentiert.','WAS DIESER ERSTTEST AUSSAGT','info'),
  step(2,'Nacheinander begrenzte Frontzweige, leisen Sound und kurze kontrollierte Motorbewegung nach [[32]] prüfen. Den Gegenkopf zuerst allein nach [[33]] testen; noch ungeklärte hintere LEDs bleiben getrennt. Danach gemeinsamer Fronttest. Unbekannte LED-Daten stoppen nur den zugehörigen Lichtzweig.'),
  step(3,'Wagen zunächst passiv nach [[23]]–[[26]] prüfen. Für jede elektrische Wagenstufe revisionspassende Lastdaten oder die begleitende qualifizierte Messung [[43]] verwenden. Mit einem Wagen beginnen; vor Umstecken immer ausschalten. Keine zusätzliche Elko-Nachrüstung in dieser Welle.'),
  step(4,'Für die endgültige Wagenzahl: höchste vorgesehene Helligkeit, gleichzeitig aktive Front-/AUX-Ausgänge, Sound und Motorbetrieb sowie Einschalten berücksichtigen. Niedrigere Kupplungs-/Litzen-/Platinengrenzen gehen vor. Ein bestandener Standtest ist keine Freigabe beliebiger Wagenzahl.'),
  tab(['Stufe','Ersttest / Funktion','Numerische Lastabnahme'],[['Motorseite / Gegenkopf','____ / ____','____ / ____'],['Wagenzahl / Konfiguration','________','[[43]]: ________']],[1.3,1,1.4]),
  small('Offene Lastdaten sperren die volle Zuglast-/Fahrabnahme, nicht bereits bestandene Montage- und Einzelprüfungen. GE ist bei O=RT nicht pauschal glatter Gleichstrom. Dafür gilt die folgende Messkarte.')
  ],'Je Kopf ist der begrenzte Ersttest geplant. Volle Zuglast wird erst mit den Nachweisen auf [[43]] freigegeben.',sources=['Q1','Q3','Q6','Q26','Q28'])
 page(43,'Wagenlast und alleinige hintere Einspeisung prüfen','Lastabnahme | tatsächliche Konfiguration',
  'GFP3 und ein gewöhnlicher DC-mA-Wert reichen für pulsierende GE-/RT-Lasten nicht allein. Es gibt zwei nachvollziehbare Nachweiswege.',
  'Anschlüsse/Motor/LEDs geprüft. Konfiguration und zulässige Herstellergrenzen notieren; vor jeder Änderung vollständig ausschalten.',[
  fig('current_probe',113),
  p('<b>Weg A:</b> Revisionspassende Herstellerdaten decken Wagenzahl, Versorgung, höchste Helligkeit und Einschaltlast ab. Die gleichzeitig genutzten vorderen Licht-/AUX-Werte summieren; weitere Leiterpfadgrenzen beachten. Eine allgemeine Angabe „mehrere Wagen“ genügt nicht.'),
  p('<b>Weg B:</b> DC-fähige Stromsonde mit nachgewiesener mA-Auflösung plus Speicheroszilloskop ausleihen. Sonde um genau eine isolierte GE-Litze; kein elektrischer Masseanschluss am Gleis. Gerätehandbuch muss Messbereich, DC/Impulsbandbreite, Spitzenaufzeichnung und Fehler im tatsächlichen Bereich abdecken. Eine übliche Auto-Stromzange reicht nicht automatisch.'),
  step(1,'Sonde geschlossen ohne Leiter nullen; nach der Reihe Nullpunkt erneut kontrollieren. Einschalten mit Vortrigger vom ersten Strom bis zum stabilen Verlauf aufzeichnen. Innenlicht aus/ein, beide Richtungen, höchste Helligkeit und spätere Protokolleinstellungen erfassen. Nach jedem weiteren Wagen dieselbe Reihe; Kurven mit Zeit-/Strommaßstab sichern.'),
  step(2,'Peak samt Messunsicherheit mit 250 mA je 60977-Ausgang vergleichen. Ohne Herstellerfreigabe keine kurze Überlast erfinden. Für 300 mA Licht/AUX konservativ obere gleichzeitige Einzelwerte summieren; hintere LEDs gehören nicht zu dieser Summe. RMS für Leitererwärmung, Peak für Ausgangsbeanspruchung beachten.'),
  step(3,'Nur hinten speisen: vordere Schleiferzuleitung stromlos an vorhandener Trennstelle öffnen und beide Enden isolieren. Für einen reinen Standversuch ist eine stabile nichtleitende Schleiferauflage möglich; vorher beweisen, dass der Schleifer B nicht berührt. Für Fahrt Zuleitung wirklich trennen; kein Papier unter fahrendem Schleifer.'),
  step(4,'Sonde um die einzelne hintere RT-Litze zur ersten Kupplung, ohne Rückleiter. Nur hinten speisen; Motor-/Sound-/Lichtlast im kontrollierten Versuch auf Strecke [[44]] erfassen, Motor nie blockieren. RT-Spannungsfall vom hinteren zum vorderen Ende differentiell messen; Kontaktunterbrechungen und Wärmeauffälligkeiten prüfen. Bestätigte Leiterpfadgrenze einhalten. Nach Wiederanschluss Anschlussprüfung wiederholen.'),
  note('Keine Nenntragfähigkeit aus Flackerfreiheit oder zehn Minuten Standlast ableiten. Kein geerdeter Oszilloskop-Masseclip an GE/RT. Ein Shunt ist nur mit passend ausgelegtem Differenz-/isoliertem Messaufbau eine Alternative; hier nicht improvisieren.'),
  small('Ergebnis: Wagen/Reihenfolge ______; Herstellerdaten oder Geräte/Fehler ______; GE Peak/RMS ______; Licht/AUX-Summe ______; RT-/Gesamtgrenze und Ist ______; zulässige Konfiguration ______. Ohne Weg A oder B bleibt nur diese numerische Lastabnahme offen.')
  ],sources=['Q1','Q3','Q6','Q26','Q28','Q33'])
 page(36,'Gehäuseprüfung: echte Isolation auch geschlossen','Gehäuseabschluss | beide Köpfe',
  'Die geschlossene Prüfung findet Druck-, Schrauben- und Lagefehler. Ein erfolgreicher Einschaltversuch ersetzt sie nicht.',
  'Alles vom Gleis/Bus, Decoder und Puffer ab. Motorleitungen von LoDi getrennt; Restenergie nach [[3]]. Offene Motor-Sechserfolge [[15]] bestanden.',[
  fig('closed_access',108),
  step(1,'PM1/PM2 an die motorseitigen freien Enden der fertig verlegten Drossel-/Litzenzweige setzen; PX/PX2 an den bestätigten Metallbezug. Im Gegenkopf nur tatsächlich passive Leitungen mit je zwei sicheren Kontaktpunkten prüfen. Kein allgemeines OL durch LEDs/Platinennetze verlangen.'),
  step(2,'Vorhandene Faltenbalg-, Kupplungs- oder Unterbodenöffnung ansehen. Dünne isolierte Hilfsleitungen müssen bei voll geschlossenem Gehäuse und jeder normalen Drehgestelllage frei bleiben. Clipkörper fern von Dach/Schrauben/Motor halten und zugentlasten. Gewählte Öffnung im eigenen Foto markieren.'),
  step(3,'Trockene Sitzprobe: schließen, passende Schrauben anziehen, normal bewegen, wieder öffnen. Keine Druck-/Scheuerspur und kein verschobener Clip. Erst dann nochmals schließen; positive Vorproben, beide Isolationswerte und positive Nachproben nach [[15]] bzw. [[4]] je Gegenstelle/Lage vollständig durchführen.'),
  note('Kein sicherer Ausgang: vor endgültiger Verdrahtung eine berührungssichere Service-Trennstelle der zwei Motorleitungen an einer tatsächlich zugänglichen Öffnung vorsehen. Steckkontakt, Motorstromtragfähigkeit und Freiraum müssen passen. Am geschlossenen Kopf werden die motorseitigen Kontakte gemessen. Nicht bohren, einklemmen oder äußere RT/GE-Punkte als Motorzugang ausgeben.','ALTERNATIVE ZUGÄNGLICHKEIT','info'),
  step(4,'Ohne passende Öffnung oder Serviceausführung bleibt diese konkrete geschlossene Messung offen. Bei Änderung der Anzeige wieder öffnen und Litzenlage, Schraube, Halter oder Dachkontakt beheben; ganze Reihe erneut. Anschließend Hilfsleitungen entfernen und den Wiederanschluss [[37]] ausführen.'),
  tab(['Kopf / Pfad / Lage','Vorprobe','Geschlossen','Nachprobe'],[['_______________','______','______','______'],['_______________','______','______','______']],[1.6,.8,.8,.8]),
  small('Messzugang/Fotos ______; sichere Sitz-/Bewegungsprobe ______; Ergebnis ______. Geänderter Endverlauf oder neue Steckstelle erfordert erneute betroffene Prüfung. Decoderfreiraum folgt zusätzlich auf [[37]].')
  ],'Die geschlossenen Messungen bestehen mit gültigen Kontaktkontrollen. Wieder öffnen; endgültige Montage und Funktionsprüfung auf [[37]].',sources=['Q1','Q6'])
