from pathlib import Path
from copy import deepcopy
import json

ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parent
PAGES={x['n']:deepcopy(x) for x in json.loads((PROJECT/'Arbeitsstand_REV11/rev11_pages.json').read_text())}
def p(t):return {'type':'p','text':t}
def h(t):return {'type':'h','text':t}
def small(t):return {'type':'small','text':t}
def step(n,t):return {'type':'step','label':str(n)+'.','text':t}
def note(t,label='STOPP',tone='stop'):return {'type':'note','label':label,'text':t,'tone':tone}
def tab(headers,rows,widths=None):return {'type':'table','headers':headers,'rows':rows,'widths':widths or [1]*len(headers)}
def fig(kind,height=180):return {'type':'figure','kind':kind,'maxh':height}
def page(n,title,phase,goal,before,blocks,check='',sources=[]):
 PAGES[n]={'n':n,'title':title,'phase':phase,'goal':goal,'before':before,'blocks':blocks,'check':check,'sources':sources}

PAGES[1]['phase']='Start | REV12'
PAGES[1]['goal']='Bebilderte Anleitung für deinen ICE 2976 mit Märklin-Sound, gemeinsamem mfx-Zugeintrag und getrennt schaltbarem Innenlicht. Korrigierte Werkstattfassung auf Grundlage deiner REV10.'
PAGES[1]['blocks'][-2]=note('Bestätigt vorhanden: Multimeter, Märklin-Decoderprogrammer und CS3 mit laut Nutzer aktueller Firmware. Genaue Typen und Versionsnummern am Gerät ablesen. Zusätzliche Prüfaufnahmen und ein Zweitsystem sind bisher nicht als vorhanden bestätigt. [[6]] zeigt den konkreten Prüfplatzweg.','DEINE AUSSTATTUNG','info')
PAGES[1]['blocks'][-1]=p('Arbeite zuerst bis zur eigenen CS3-Paarprüfung [[11]]. Erst nach deren Erfolg den Zug elektrisch umbauen. Ein zusätzlicher SID-Wechseltest erweitert die Abnahme auf einen geänderten mfx-Systemzustand; er wird ohne Messbeleg nicht behauptet. Geräte- und Bauteildaten werden am passenden Handgriff erhoben. Herstellerklärung und gezieltes Ausleihen von Prüfmitteln benötigen keinen Händlerauftrag.')
PAGES[2]['blocks'][0]['rows'][4]=['Vorhanden','CS3, Multimeter, Märklin-Decoderprogrammer','Typaufdruck/Version notieren; 60971 nur für Märklin. Zusätzliche Aufnahmen [[6]]/[[41]].']
PAGES[2]['blocks'][3]['text']=PAGES[2]['blocks'][3]['text'].replace('ICE2976_REV11','ICE2976_REV12')
PAGES[2]['blocks'][4]['text']='Geräte ablesen und fotografieren: CS3-Version/Netzteil ______; Multimeter-Modell/Handbuch ______; Märklin-Programmer-Artikel ______. Aufnahmen nach [[41]] gezielt leihen oder beschaffen, wenn sie fehlen. Keine LokProgrammer-Hardware nur für den Offline-Export kaufen.'
PAGES[4]['blocks'][3]['text']='Ist die Ader bereits mit Widerstand, LED, Diode, bestücktem Pad oder unbekannter Leiterbahn verbunden, diese OL-Regel nicht anwenden. Anschluss- und Sichtprüfung nach [[5]] durchführen. Keine Bauteile abtrennen, nur damit ein gewünschter Offenwert erscheint.'

PAGES[12]['before']='CS3-Paarprüfung [[11]] bestanden; alles getrennt, Decoder/Puffer ab. Motorbauart fotografieren: 60941 verlangt den passenden Trommelkollektormotor. Bei Scheibenkollektor/abweichendem Sitz keinen Einbau erzwingen.'
PAGES[13]['title']='Kondensatoren prüfen, Drosseln einbauen'
PAGES[13]['blocks'][2]['rows'][1][1]='Quer-Kondensator am unveränderten passenden 60941-Motorschild zwischen M1 und M2 belassen. Beide Enden verfolgen. Fremdbestückung oder fehlendes Bauteil separat klären; keinen Kapazitätswert raten.'
PAGES[15]['blocks'][-1]['text']='<b>Bei endlichem Isolationswert:</b> Strom getrennt lassen. Litzen, Bürstenfedern, Kondensatorenden, Schrauben sowie Kohlestaub und Metallspäne prüfen. Verunreinigung materialverträglich entfernen; vor Nachmessung vollständig trocknen lassen. Ein beim Schraubenlösen verschwindender Fehler verlangt passende Schaftlänge/Abstände, keine lose Schraube. Ganze Reihe wiederholen.'
PAGES[16]['blocks'][0]['columns'][1][-1]['text']='<b>Eintragen:</b> Revision ______; SJ1/SJ2 ______; SW/RT ______; GE-AUX ______. Bei V1.49 oder unklarer Bestückung an LoDi eine beidseitige Aufnahme senden lassen/selbst vorbereiten: „Welche GE-AUX-Zuordnung und SW/RT-Verbindung gelten genau für diese Revision?“ Vor Anschluss Antwort bzw. eindeutig passende Herstellerzeichnung dem Foto zuordnen.'
PAGES[16]['blocks'][0]['columns'][1][-1]['text']=PAGES[16]['blocks'][0]['columns'][1][-1]['text'].replace('an LoDi eine beidseitige Aufnahme senden lassen/selbst vorbereiten','eine beidseitige Aufnahme für LoDi vorbereiten')
PAGES[16]['goal']='Die beschriftete Gegenseite und die tatsächliche Revision müssen zusätzlich vorliegen. Brücken und Netze werden nur nach passender Herstellerzuordnung verwendet.'
PAGES[18]['before']='Revision [[16]] zugeordnet; Decoder/Puffer/Lasten ab. Anschlusskontrolle [[5]] und passende Montagezeichnung bereitlegen.'
PAGES[18]['blocks'][0]['maxh']=128
PAGES[18]['blocks'][3]['text']='Ring A am K1-Ende und Ring B am Frontende im eigenen Foto markieren. Originalhalter, Schrauben und Auflagen mit der zugehörigen LoDi-Revisionszeichnung abgleichen. Unklarer Metallkontakt: LoDi konkret nach Ringrolle und zulässiger Schraub-/Chassisverbindung fragen. Eine niederohmige Messung allein bestimmt kein Sollnetz.'
PAGES[18]['blocks'][4]['rows'][-1]=['Anschluss-/Sichtprüfung nach [[5]]','________','________']
PAGES[19]['blocks'][4]['text']='Nach jedem Anschluss abkühlen lassen. Mit Lupe Zinnbrücken, Litzenfäden und Lötperlen suchen; festen Sitz vorsichtig prüfen. Betroffene Anschluss-/Sichtprüfungen [[5]] wiederholen. Strombegrenzung der Front muss vor LED-Anschluss geklärt sein.'
PAGES[21]['before']='Vorabtest [[11]] bestanden; Gegenkopf getrennt, stromlos, Decoder/Puffer entfernt. Anschlusszuordnung und Sichtprüfung [[5]] vor Befestigung vorbereiten.'

PAGES[20]['blocks'][2]['text']='Genau einen unveränderten Lautsprecher aus deinem 60977-Satz verwenden. Satzherkunft fotografisch sichern; Bauform/Schallkapsel müssen druckfrei passen. Für diesen Original-Lautsprecher ist kein aus einer Ohmmessung erratener Impedanzwert nötig. Bei Ersatzlautsprecher gelten dagegen dessen Nennimpedanz und die Märklin-Leistungsangaben.'
PAGES[20]['blocks'][3]['text']='Originalstecker erhalten: von Kontaktseite und seitlich fotografieren, Kontaktabstand und Gehäusemaße notieren. Diese Daten mit der Maßzeichnung eines zweipoligen Gegensteckers vergleichen; Rastung und Pinform müssen passen. Falls die Serie unklar bleibt, genau dieses Foto samt Maßen beim Hersteller/Steckeranbieter klären. Nicht durch Aufdrücken probieren.'
PAGES[20]['blocks'][-1]['text']='Satzherkunft/Bauform ______; Gegenstecker/Maßzeichnung ______; Adapterprüfung ______; freie Membran/Schallraum ______; späterer leiser Funktionstest ______.'
PAGES[22]['before']='Halter [[21]] und Kontaktzuordnung [[24]] geklärt. LED-Auslegung [[17]] belegt oder hintere LEDs getrennt/einzeln isoliert. Decoder/Puffer entfernt.'
PAGES[22]['blocks'][3]['text']=PAGES[22]['blocks'][3]['text'].replace('zuerst den Plan [[5]] verwenden','nach [[5]] prüfen')
PAGES[22]['blocks'][5]['text']='R an <b>0/GL</b>. Nur mit belegter LED-Auslegung: Plus an <b>+Ub</b>, Rot über eigenen Widerstand an <b>LV</b>, Weiß über eigenen Widerstand an <b>LR</b>. Sonst alle drei LED-Adern getrennt und einzeln isoliert lassen. Lampenfeder, Chassisschraube, +5V oder GND sind keine LED-Anschlüsse.'

# Separate assembly checks from the later optional feedback test.
PAGES[25]['before']='Wagen allein, ohne Gleis/Bus. Speicherzustand nach [[3]] prüfen. Passive Kupplungen [[24]] bestanden; eigene Leiste/Anschlusspads nach [[5]] zugeordnet.'
PAGES[25]['blocks'][0]['rows'][2]=['L gegen O: nur optionaler Diagnosevergleich nach [[5]]','Bei gleichen belegten Geräte-/Bauteilbedingungen vergleichen; kein pauschales OL-Soll']
PAGES[25]['blocks'][4]['text']='Nach Löten jeden tatsächlichen Kupplungskontakt bis zu seinem Pad prüfen; bekannte L-L-/O-O-Leiterpfade erneut messen. Ein optional protokollierter Elektronikvergleich nach [[5]] kann Änderungen anzeigen. Neue Brücke/unerklärliche Abweichung: Litzen stromlos trennen, passive Stücke prüfen und Lötstelle untersuchen; nicht nach Wunschwert umbauen.'
PAGES[26]['goal']='Eine Achskontaktfeder ergänzt die örtliche Radmasse. Ein leitender, nicht isolierter Radsatz meldet im Kontaktgleis bereits ohne B-Litze. Zweck und Radsatzart deshalb zuerst feststellen.'
PAGES[26]['before']='Wagen vollständig getrennt; keine Kupplungslitzen/Speicher angeschlossen. Anschlussrollen nach [[5]] geklärt. B ist eine Option, kein dritter Kupplungsbus.'
PAGES[26]['blocks'][2]['headers']=['Optionale Diagnosepaare nach [[5]]','Vorher','Nachher']
PAGES[26]['blocks'][3]['text']='B-Pad vom O-/L-Nachbarpad im Foto unterscheiden. Vor Anlöten die vier B-Querpfade nur dann diagnostisch erfassen, wenn Gerät und Bauteilpfade nach [[5]] geeignet sind. Kein allgemeines OL-Soll. Genau eine positiv geprüfte freie Radkontaktlitze an das eindeutig bezeichnete B-Pad löten.'
PAGES[26]['blocks'][4]['text']='Abkühlen lassen; B/O/L mit Lupe auf Zinn- oder Drahtbrücken ansehen. Federlitze bis B muss leitend bleiben, auch bei Bewegung. Optionalen Vorhervergleich nur unter gleichen Bedingungen wiederholen. Auffälligkeit: Litze wieder von B trennen, einzeln isolieren, Ursache klären und Anschlussprüfung wiederholen.'
PAGES[26]['blocks'][6]['text']='Späterer Meldefunktionstest, getrennt von dieser Montageabnahme: erst nach elektrischer Zugabnahme [[37]] im freigegebenen Bereich [[44]]. Nur der Testwagen belegt den Meldeabschnitt. Frei-belegt-frei in mehreren Radlagen und beiden Orientierungen, ggf. Innenlicht aus/an getrennt prüfen. Ein S88-Kontakt erkennt keinen bestimmten ICE.'
PAGES[26]['check']='Montageabnahme: Schritte 1–5 bestanden (oder B bleibt bewusst frei). Schritt 6 ist ein späterer, separat protokollierter Rückmeldetest und keine Vorbedingung der Wagen-Erstinbetriebnahme.'
PAGES[27]['blocks'][2]['text']='<b>Nur bei Innenlicht über AUX4:</b> CV51 sichern; Bit 4 muss 0 sein. Bevorzugt im Märklin-Projekt „verstärkt“ wählen. Für die dokumentierte CV51-Tabelle: Altwert 0–15 unverändert; 16–31 genau 16 abziehen; über 31 erst klären. Nie pauschal CV51 = 0. Nur dieses Bit ändern.'

rows=PAGES[29]['blocks'][0]['rows']
rows[0][0]='Eigene CS3-Paarprüfung [[11]]; Identität/Projekt und Aktivierung dokumentiert; SID-Erweiterung separat'
rows[4][0]='LED-Auslegung [[17]] belegt; alternativ hintere LEDs getrennt/einzeln isoliert. Messung [[42]] folgt beim Ersttest'
rows[6][0]='Passive Leiter/Motorprüfung bestanden; Anschluss- und Sichtprüfung bestückter Platinen [[5]]'
rows[8][0]='Kontrollierter Einzel-Ersttest [[28]] vorbereitet: CS3-Programmiergleis, keine Wagen/Puffer; Abschaltkriterien'
PAGES[29]['blocks'][2]['text']='Keine unbekannte Verdrahtung oder fehlende Motorisolation einschalten. Ein Prüfstandtest bestätigt keine Fahrzeugverdrahtung. Ein ausstehender späterer Lastmesswert ist hingegen kein erfundenes Vorab-Ergebnis: der eindeutig abgegrenzte Einzel-Ersttest nach [[28]] dient gerade seiner Ermittlung.'

PAGES[30]['blocks'][-1]['text']='Unklare schwarze Struktur oder verdeckter Index: nicht aufstecken und nichts abziehen. LoDi anhand Gesamtfoto, Makro von oben/seitlich und Revision konkret fragen: „Was ist die schwarze Struktur, wie wird 60977 hier korrekt gesteckt, muss etwas entfernt werden und wie?“ Antwort am eigenen Teil abgleichen. Herstellerkontakt ist kein Händlerauftrag.'

PAGES[32]['before']='Anschluss-/Motorprüfungen [[29]] und Stecklage [[30]] bestanden; Einzel-Ersttest [[28]] vorbereitet. Gegenkopf/Wagen/Puffer getrennt, freie Kontakte einzeln isoliert.'
PAGES[32]['goal']='Zuerst Kommunikation und Licht im Stand, dann leiser Sound. Der Motor wird erst nach dem Standtest kurz bewegt.'
PAGES[32]['blocks'][0]['text']='Nur den CS3-Programmiergleisausgang an ein vollständig getrenntes Prüfgleis anschließen; Hauptgleisstecker abziehen. Automatik aus, Fahrstufe 0. Ohne Fahrzeug GFP3-Leerwert aufrufen und notieren. Die Anzeige beobachtet den Gesamtstrom; sie ersetzt keine Isolations-/Zweigstromprüfung.'
PAGES[32]['blocks'][1]['text']='CS3 STOP, Motortriebkopf allein aufsetzen, dann STOP aufheben. Zuerst ohne Licht/Sound und Fahrbefehl beobachten; eindeutigen Märklin-mfx-Eintrag abgleichen. Bei Abschaltung, Geruch, ungewöhnlicher Wärme oder Motorlauf sofort wieder STOP und physisch trennen. Kein wiederholtes Einschalten ohne Ursache.'
PAGES[32]['blocks'][2]['text']='Am selben getrennten Prüfgleis bei Fahrstufe 0: F0 aus → dunkel; F0 vorwärts → Weiß; rückwärts → Rot. LED-Zweigwerte nach [[42]] prüfen. Danach Sound leise einschalten, Gesamtstrombeobachtung notieren. Werte und tatsächliche Reaktion zählen, nicht allein CS3-Symbole.'
PAGES[32]['blocks'][4]['text']='Erst nach bestandenem Standtest: freie kurze Strecke und Absturzschutz prüfen. Kleinste Fahrstufe kurz anlegen, dann 0; Räder nie festhalten. Dies ist ein kontrollierter Funktionsversuch, keine Abnahme voller Motorlast. Weiterer Fahrbetrieb benötigt die Lastprüfung [[43]].'
PAGES[32]['blocks'][5]['text']='Falsche Richtung: STOP, trennen. Entweder Motorlitzen gezielt korrigieren und [[14]]/[[15]] wiederholen; oder 60977 allein im Märklin-Werkzeug bearbeiten: CV51 Bit 0 „Motoranschluss tauschen“ mit gesichertem Altwert ändern, übrige Bits erhalten, rücklesen. Danach Richtung/Licht erneut prüfen. CV29-/Lichtumkehr nicht als Abkürzung verwenden.'
PAGES[32]['blocks'][-1]['text']='Datum/Projekt ______; GFP3 leer/Stand ______; Frontstromprüfung ______; leiser Sound ______; Kleinstfahrt/Richtung ______; Auffälligkeit ______. Vollständige Lastabnahme folgt [[43]].'

PAGES[33]['before']='Gegenkopf [[29]]/[[31]] vorbereitet; Motorseite [[32]] bestanden. Nur die in [[28]] beschriebene erste Prüfung, keine Wagen/Puffer. Beide Köpfe ungekuppelt; offene Kontakte einzeln isoliert.'
PAGES[33]['blocks'][0]['text']='Gegenkopf zunächst allein: CS3 STOP, Motorseite vollständig vom Gleis nehmen. S/R, B/GR/0/GL, Halter und Widerstände kontrollieren; freie RT-/GE-Kontakte isolieren. Kopf auf das getrennte Programmiergleis setzen, STOP aufheben und GFP3-Wert notieren. Abschaltung, Wärme/Geruch: sofort STOP und trennen.'
PAGES[33]['blocks'][1]['text']='Ohne Master keine eigene F0-Reaktion fordern; keine Neuanmeldung oder motorlose DCC-Programmierung. DCC-Wartung nur auf [[41]]. Sind hintere LEDs noch getrennt, Schritte 2–4 auslassen: Ruhetest dokumentieren, Licht bleibt offen. Unabhängige Montageprüfungen dürfen weitergehen; keine volle Wagen-/Fahrendabnahme.'
PAGES[33]['blocks'][2]['text']='STOP, dann beide Köpfe ungekuppelt auf dasselbe vollständig getrennte Programmiergleis setzen. Nur diese CS3-Quelle, Fahrstufe 0, Automatik aus. Zwischen den Köpfen Abstand und keine losen Metallteile. Keine Decoderparameter ändern. Ein höherer Ausgang ist kein Ausweg aus einer Überlastmeldung.'
PAGES[33]['blocks'][5]['text']='STOP und physisch trennen. Gegenkopf abnehmen, wieder aufsetzen, dann beide neu starten und Lichtfolge wiederholen. Hintere LED-Zweigströme nach [[42]] einzeln prüfen. Bei Abweichung Einschaltfolge aus [[11]] vergleichen; erst nach Ursachenklärung erneut versuchen.'
PAGES[33]['check']='Ruhetest bestanden: ______; Frontlicht/LED-Zweige bestanden oder offen: ______. Volle Wagen-/Fahrabnahme erst mit geprüftem Licht und Lastnachweisen [[28]]/[[43]].'

PAGES[34]['before']='Einzelköpfe [[32]]/[[33]] bestanden. Wagen [[23]]–[[25]] geprüft; optionaler B-Anschluss nur Schritte 1–5 aus [[26]]. Jede neue Laststufe gemäß [[28]]/[[43]] begründet. Eine CS3-Quelle, Fahrstufe 0, Puffer ab.'
PAGES[34]['blocks'][0]['text']='STOP, physisch trennen. Nur den nächsten geprüften Wagen ankoppeln und Orientierung/Kontaktzuordnung prüfen. Freie Kontakte beider Köpfe und des jeweils letzten Wagens einzeln isolieren. Erst dann den für diese Stufe bestätigten Prüfaufbau einschalten; niemals unter Spannung kuppeln.'
PAGES[34]['check']='Die vorgesehene Zusammenstellung besteht im Stand. Jetzt Anlagenbereich [[44]] prüfen; danach T9 und kontrollierten Fahrtest [[35]] ausführen.'
PAGES[35]['before']='T1–T8 bestanden; endgültige Projekte dokumentiert. Lastabnahme [[43]] und Bereich [[44]] abgeschlossen. Nur dieser freigegebene Aufbau, Fahrstufe 0, keine Einmessfunktion.'
PAGES[35]['blocks'][5]['text']='Nur die nach [[44]] erfassten Kurven/Weichen im zulässigen Bereich langsam befahren. Vor gesperrten Abschnittsgrenzen den ganzen Zug anhalten. Wagenlicht, Sound, Beweglichkeit und Leitungslage beobachten. Bis Gehäuseabschluss bleibt dies ein beaufsichtigter offener Fahrtest.'
PAGES[37]['blocks'][0]['text']='Gehäuse öffnen, Hilfsleitungen entfernen. Motorlitzen noch von LoDi getrennt lassen und Sechserfolge [[14]]/[[15]] erneut prüfen. Erst danach Motor und übrige geplante Anschlüsse wiederherstellen; betroffene passive Pfade [[4]] und Anschlüsse [[5]] prüfen. Keine Motor-OL-Messung durch die Platine.'
PAGES[37]['blocks'][5]['rows'][1][0]='CS3-Paarabnahme / Projekte / Innenlichttaste; Firmwarestatus und SID-Erweiterung getrennt'
PAGES[37]['blocks'][5]['rows'][5][0]='Begrenzter eigener Anlagenbereich nach [[44]]'
PAGES[37]['blocks'][7]['text']='Datum ______; elektrischer Abschluss bestanden/offen ______; freigegebener Bereich ______. Danach optionalen Rückmeldetest [[26]]/6 ausführen. Erst bei abgeschlossenem Grundaufbau in diesem Bereich fahren. Geänderter mfx-Systemzustand, Puffer und automatischer Signalhalt benötigen die jeweils getrennten Ergänzungsprüfungen.'
PAGES[38]['blocks'][0]['rows'][4][1]='Freilauf, Bürsten, Drosseln, Isolation; Kohlestaub/Späne'
PAGES[38]['blocks'][0]['rows'][5][1]='Kennung, Export, Rücklesewerte, Protokolle; Diagnoseentscheid [[11]]'
PAGES[39]['blocks'][3]['text']='Nur einen passend angebundenen Puffer vorn am 60977, keinen 60974 am ESU. Firmwarewert aus dem Lesebeleg [[7]]: mindestens 3.2.0.1; CV7 nicht beschreiben. Anschluss, Lade-/Restenergie- und Nachlaufverhalten vorher festlegen. Motorpufferung anfangs aus. Nach Änderung Anschluss-, Last-, Neustart- und Halteprüfungen wiederholen. Wagenlicht wird dadurch nicht automatisch gepuffert.'
PAGES[39]['blocks'][-1]['text']='Bis zur gesonderten Signalhaltabnahme nur im bestätigten Bereich [[44]] beaufsichtigt und von Hand anhalten. Kontaktverdrahtung bleibt nötig. Eine bestandene Synchronisation bestätigt weder Bremsabschnitterkennung noch eine sichere Anhaltekurve.'

page(44,'Anlagenbereich vor dem ersten Fahrtest prüfen','Anlage | vor jeder neuen Strecke',
 'RT verbindet beide Schleifer. Der Abstand zwischen ihnen wird elektrisch überbrückt – auch wenn der ICE selbst vor dem Signal stehen bleibt.',
 'Zug zunächst vom Gleis. Anschlussunterlagen, Gleis-/Signalplan und Fotos bereitlegen. Eine unbekannte Grenze bleibt außerhalb der Teststrecke.',[
 fig('district',132),
 step(1,'Den gesamten vorgesehenen Fahrweg im Plan markieren. Jede Mittelleiter-Trennstelle, Einspeisung, Signalstelle und jeden Übergang verfolgen; auch verdeckte Anschlusskabel und Abstellgleise berücksichtigen. Signalbegriff „Rot“ allein sagt nichts über die elektrische Wirkung.'),
 tab(['Abschnitt / tatsächlicher Aufbau','Entscheidung für den langen RT-Bus'],[
 ['Gleiche digitale CS3-Quelle; keine schaltende/bremsende Mittelleitertrennung','Für diesen Gesichtspunkt geeignet; restliche Last-/Fahrtests bleiben erforderlich.'],
 ['Signal schaltet Gleis stromlos / Bremsmodul speist Sonderstrom','Mit direktem RT-Bus hier nicht fahren. LoDi nennt ICE-M-S für zugbeeinflussende Signale; deren Umbau braucht eigene Prüfung.'],
 ['Anderer Booster, Programmiergleis, Analogversorgung oder unklare Einspeisung','Kein Übergang und keine Überbrückung; getrenntes Prüfgleis verwenden.'],
 ['Rückmeldekontakt ohne Änderung der Mittelleiterversorgung','Schaltung prüfen; Kontaktgleis-Signal und Signalhalt sind unterschiedliche Funktionen.']],[1.2,1.7]),
 step(2,'Je Signal/Modul Hersteller, Artikel und Anschlussplan notieren. Kabel bis zum Gleis verfolgen. Kontaktmessung nur am eindeutig spannungsfreien, von Elektronik/Parallelpfaden getrennten Schaltkontakt; keine Ohmmessung quer durch eine unbekannte Anlage. Elektronische Signale nach ihrer Anleitung klassifizieren.'),
 step(3,'Nur den vollständig geklärten zusammenhängenden Bereich freigeben. Grenzen im Plan und am Gleis markieren. Der ganze Zug einschließlich beider Schleifer muss vor jeder gesperrten Grenze bleiben. Eine bestandene Werkstattprüfung gilt nicht automatisch für andere Anlagenbereiche.'),
 note('Halteabschnitte nicht beiläufig dauerhaft einspeisen und keine Booster-/Programmiertrennung überbrücken. Ein Wechsel auf ICE-M-S oder reine CS3-Ereignissteuerung ist eine eigenständige Anlagen-/Umbauentscheidung.'),
 p('Plan/Quelle ______; geprüfte Strecke ______; Signal-/Modulliste ______; gesperrte Grenzen ______; Datum ______. Nur dieser Bereich ist anschließend für [[35]] und [[37]] freigegeben.')
 ],'Alle Streckenabschnitte sind elektrisch zugeordnet; keine unbekannte oder unzulässig überbrückte Grenze liegt im Fahrweg.',sources=['Q3','Q4','Q26'])
