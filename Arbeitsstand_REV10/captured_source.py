"""REV9: preserve the previous artifact; reuse only inspected layout/chapters."""
from pathlib import Path
import ast
import hashlib

ROOT = Path(__file__).resolve().parent
previous = ROOT / 'build_ice2976_rev5.py'
old = previous.read_text()
prefix = old[:old.index("page('ICE 2976: Umbauanleitung REV5')")]
prefix = prefix.replace("ICE_2976_Umbauanleitung_REV5.pdf", "ICE_2976_Umbauanleitung_REV9_KONKRET.pdf")
exec(compile(prefix, str(previous), 'exec'))

ST['body'].fontSize=9.8; ST['body'].leading=13.5
ST['step'].fontSize=9.8; ST['step'].leading=13.5
ST['h1'].fontSize=18; ST['h1'].leading=22
ST['cell'].fontSize=8.7; ST['cell'].leading=11.6
nodes=ast.parse(old).body
starts=[(n.lineno,n.value.args[0].value) for n in nodes if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Name) and n.value.func.id=='page']
lines=old.splitlines(keepends=True)
end=next(n.lineno for n in nodes if isinstance(n,ast.FunctionDef) and n.name=='foot')
chapters={title:''.join(lines[start-1:(starts[i+1][0]-1 if i+1<len(starts) else end-1)]) for i,(start,title) in enumerate(starts)}
def original(title, replacements=()):
    chunk=chapters[title]
    for before,after in replacements:
        assert before in chunk, (title,before)
        chunk=chunk.replace(before,after)
    chunk=chunk.replace('REV5','REV9')
    exec(compile(chunk,str(previous),'exec'),globals())

SOURCES[1]=('Märklin','Nachrüstdecoder 60975/60976/60977','Stand 10/2025; S. 3-7 und 19; funktionierender Ersatzlink, identisch mit geprüfter lokaler Kopie','https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf')
SOURCES[22]=('Märklin','mDecoderTool3 Anleitung v3.60','S. 3: Informationen anzeigen und Einstellungen auslesen; keine garantierte UID-Anzeige','https://streaming.maerklin.de/public-media/mdt3/pdfs/D_mDecoderTool3_A5_v360.pdf')
SOURCES[17]=('ESU','LokProgrammer 53451','Hardware, Windows-Software und getrennte Programmierung; Abruf 10.09.2026','https://www.esu.eu/produkte/lokprogrammer/')
SOURCES[18]=('ESU','LokProgrammer Versionshinweise','5.0.9: Synchronisation bei LokSound; 5.0.11: Einführung LokPilot 5; kein artikelscharfer LP5-Mindeststand abgeleitet','https://www.esu.eu/download/software/lokprogrammer/')
SOURCES[19]=('Märklin','CAN-Protokoll 2.0','Abschnitt 8.1.3: lokomotive.cs2 und mfxuid; UID ist nicht die zugewiesene Fahradresse','https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf')
SOURCES[20]=('Vishay','Surface Mount Resistor Marking','Vierstelliger Widerstandscode; 2201 entspricht 2,2 kOhm','https://www.vishay.com/docs/20020/smdmark.pdf')
SOURCES[21]=('ESU','Profi-Prüfstand 53900','Beispiel eines Prüfgeräts, keine pauschale Freigabe für jede Decoder-/Lastkombination','https://www.esu.eu/produkte/profi-pruefstand/')

from rev9_concrete_closure import install
install(globals())
page('ICE 2976: Umbauanleitung REV9')
add('<b>Prüffassung mit vorgezogenem Decoder-Nachweis und korrigierten Messkarten</b>')
warn('Noch keine vollständige Bau- oder Betriebsfreigabe','Die Kombination Märklin 60977 / ESU 59649 ist an diesen konkreten Decodern noch nicht getestet. Die Übernahme der Märklin-Identität in die ESU-Sonderoption ist nicht vollständig belegt. Zuerst Kapitel A-C abarbeiten. Solange G0 offen ist, am ICE nur dokumentieren und spannungslos prüfen; den Zug nicht für diese Architektur zerlegen oder verdrahten. Davon getrennt dürfen A-C ausschließlich in bestätigten geeigneten Decoder-Prüfaufnahmen erfolgen.')
add('Ziel: ein automatisch angemeldeter mfx-Zug, Märklin-Sound, Rot/Weiß-Wechsel an beiden Köpfen auch im Stand und getrennt schaltbare Innenbeleuchtung. Zweiter Decoder ohne Zentralen-Traktion. Originale Märklin-ICE-Kupplungen; keine zusätzliche Längsader durch die Mittelwagen. Kurze Kupplungs-Anschlusslitzen bleiben erforderlich.')
table(['Reihenfolge','Ergebnis, das vor dem nächsten Schritt vorliegen muss'],[
('A-C: G0 - vor dem Umbau','Identität und ESU-Sonderoption geklärt; Kombination an CS3 reproduzierbar geprüft.'),
('1-3, 8-9b: G1','Tatsächliche Platinenrevisionen, Anschlussnamen und Befestigung geklärt.'),
('4-7, 21-22: G2','Motor mechanisch passend; Entstörung und Isolation am eigenen Modell geprüft.'),
('10-14b: G3','LED-Ströme, hinteres Lichtmapping, Kupplungen und Wagenpfade geprüft.'),
('17-18, 24: G4','Stufenweise Inbetriebnahme, Belastung und geschlossenes Gehäuse abgenommen.'),
('15 und 19: eigene Freigaben','60974-Anschluss und CS3-Signalhalt sind separate, bisher offene Prüfungen.')],[1.5,4.8])
add('G = Prüftor. Offen bedeutet nicht widerlegt, aber auch nicht ausführungsreif. Diese Fassung ersetzt die Arbeitsanweisungen der REV6; REV6 bleibt als Vergleich erhalten. Frühere Variantenpläne nicht parallel anwenden. Im REV9-Zielaufbau sind beide Schleifer über RT verbunden; Decoder-U+ und Funktionsausgänge bleiben getrennt.')
add('Dokumentstand 10. September 2026. Herstellerangaben, eigene Prüfmethodik und offene Nachweise werden getrennt ausgewiesen. Kein Literatur- oder KI-Konsil ersetzt Messungen am Fahrzeug. Die vollständige externe Findingtabelle liegt noch nicht vor.','small')

page('A. Decoder-Nachweis: Ausstattung und Grenzen')
table(['Anzahl / Artikel','Bestand','Für diesen Nachweis'],[
('1 x Märklin 60977','Vorhanden','Hauptdecoder; Identität und Firmware nur auslesen und sichern.'),
('1 x ESU 59649','Vorhanden','LokPilot 5 M4 / 21MTC MKL; exakten Typ beim Einlesen bestätigen.'),
('1 x Märklin 60971','Vorhanden','Märklin-Konfiguration/Sound; nicht als ESU-Sonderoptionswerkzeug einsetzen.'),
('1 Zugang: ESU 53451','Nicht bestätigt','LokProgrammer samt unterstützter Windows-Software; eigener, geliehener oder Händlerzugang.'),
('1 Windows-PC','Nicht bestätigt','Für den beschriebenen ESU-Weg; Programm- und Firmwarestände protokollieren.'),
('1 x CS3','Vorhanden','Gemeinsamer mfx-Betriebstest; keine zweite Zentrale parallel einspeisen.'),
('2 geeignete Decoder-Prüfaufnahmen','Nicht bestätigt','Für den gemeinsamen Versuch müssen beide Decoder sicher getrennte Lasten tragen. Eignung von 21MTC, AUX-Pegeln und Lasten vorher bestätigen.'),
('1 Prüfdienstleistung, ohne Artikelnummer','Bei Bedarf','Empfohlener Weg, wenn Prüfaufbau oder Identitätsübernahme nicht sicher selbst möglich sind.')],[2.0,1.2,3.4])
add('ESU 53900 ist ein dokumentierter Decoderprüfstand, aber hier keine pauschale Kaufempfehlung für zwei Märklin-/ESU-Prüfaufnahmen. Lautsprecherimpedanz, Motortyp und 21MTC-Ausgangsvariante müssen passen. Der Prüfstand enthält einen anderen Motor als den späteren 60941; keine automatische Motoreinmessung durchführen.<super>17,21</super>')
warn('Kein improvisierter Tischaufbau','Decoder nicht lose auf Metall betreiben, keine nackten LEDs als Prüflast und keine unbestätigte Widerstandslast an den Motorausgang hängen. Beim Programmieren stets nur einen Decoder verbinden. Beim gemeinsamen Betriebstest nur eine Digitalquelle an beide Gleiseingänge; niemals Ausgänge oder Decoder-U+ parallel verbinden.')
refs(17,21)

page('B. Identität und Sonderoption belegen')
add('ESU dokumentiert die Master/Slave-Einrichtung an eigenen LokSound-Decodern. Die Produktliste bestätigt M4 für 59649. Beides zusammen ist noch kein vollständiger Nachweis der Mischkombination oder einer bestimmten LokPilot-Mindestfirmware.<super>7,15,18</super>')
step('B1','60977 auslesen, nicht aktualisieren.','Nur den 60977 mit passendem Märklin-Aufbau am 60971 anschließen. Im mDecoderTool3: Decoder / Decoder-Informationen anzeigen. Typ und Firmware notieren. Dann Decoder / Decoder auslesen und Einstellungen als neues Projekt sichern; Sounds werden dabei nicht ausgelesen. Der Dialog ist kein garantierter UID-Leseweg. Nicht Decoder-Firmware aktualisieren auswählen.<super>22</super>')
step('B2','CS3 sichern, Identität klären.','60977 noch nicht registriert? Ausschließlich den Master allein unter C1/C2-Sicherheitsbedingungen anmelden; diese Einzelanmeldung ist vor B-Abschluss erlaubt. Danach CS3-Systemeinstellungen: Sichern auf USB unter neuem Namen, nicht Wiederherstellen. Fachkundig nur eine Kopie prüfen: lokomotive.cs2 vorhanden und .mfxuid eindeutig diesem 60977 zugeordnet? Das Feld ist für CS2 dokumentiert, die konkrete CS3-Sicherung noch ungeprüft. Nichts bearbeiten/zurückspielen. Gemeinsamer Slave-Versuch erst nach bestätigter Identitätszuordnung.<super>12,19</super>')
step('B3','Übernahmeformat bestätigen.','Vor jeder Eingabe muss feststehen, welche Werte in ESUs getrennte Felder Hersteller-ID und Seriennummer gehören. Herkunft, Zahlenformat und gegebenenfalls Umrechnung schriftlich festhalten. Keine DCC-Adresse, SID, Artikelnummer, Lok-Betriebsnummer oder ungeprüfte Hex-Zahl einsetzen. ESUs Beispiel 151 gehört zu ESU.')
warn('G0-STOPP: zentrale Lücke bleibt offen','Die exakte Zuordnung der Märklin-mfx-UID zu den beiden ESU-Eingabefeldern ist in den ausgewerteten Primärquellen nicht nachgewiesen. Keine Werte ausprobieren. B4 als getrennte, nur lesende Prüfung bleibt möglich. Erst mit belegter Identitätszuordnung B5 und C ausführen. Nur deren dokumentierter Erfolg gibt den weiteren ICE-Umbau frei.')
step('B4','ESU getrennt einlesen.','Am 53451 nur den 59649 in geeigneter Prüfaufnahme einlesen. Typ und Firmware prüfen, Einstellungen als Projekt sichern. Unter Decoder / Sonderoptionen muss die Master-Decoder-Synchronisation für den tatsächlich eingelesenen Decoder vorhanden sein. Fehlt sie oder scheitert Auslesen/Quittierung: stoppen; nicht beliebige CVs schreiben.')
step('B5','Erst nach B3-Bestätigung schreiben.','M4 aktiv lassen; bestätigte Masterdaten in die Sonderoption übernehmen, Einstellungen schreiben und anschließend erneut auslesen. Werte und aktivierte Option vergleichen. Keine Sounddatei eines anderen Herstellers aufspielen. Gemeinsame DCC-Adresse ist kein Ersatz für den mfx-Nachweis.')
refs(7,19,22)

page('C. Gemeinsamer CS3-Vorabtest')
warn('Nur mit bestätigter Identität und sicheren Prüfaufnahmen','Kapitel B muss abgeschlossen sein. Dieser Versuch findet vor dem Umbau statt, ohne LoDi-Platinen, Kupplungsbus und Puffer. Prüflasten sind bereits passend und geschützt angeschlossen. Zum Umstecken Digitalversorgung vollständig trennen. Bei Überlast, Geruch oder unerwartetem Motorlauf sofort abschalten.')
step('C1','Testumgebung vorbereiten.','Automatische Fahrereignisse für die Testgeräte deaktivieren, Regler auf 0. CS3-Ausgang von der Anlage trennen. Keine Gleisanschlussbox oder Programmerausgänge parallel anschließen. Aktiven mfx-Betrieb belegen; zufälliges Folgen unter DCC/MM zählt nicht. Protokolleinstellungen nur in der getrennten Testumgebung dokumentiert und rückstellbar ändern.')
table(['Versuch','Erwartung / Abbruch'],[
('C2: Hauptdecoder allein','mfx-Anmeldung oder eindeutig vorhandenen mfx-Eintrag benutzen; F0 und Sound bei Fahrstufe 0 prüfen. Kein manueller DCC-Eintrag als Ersatz.'),
('C3: Abschalten; Slave ergänzen','Beide Eingänge an derselben Quelle. Nur der gemeinsame ICE-Eintrag wird bedient. Kein neu entstandener zweiter unabhängig zu bedienender Zug. Vorbestehende Einträge nicht blind löschen oder ausblenden. Ist der Slave weiter eigenständig angemeldet und unabhängig steuerbar, ist der Test nicht bestanden.'),
('C4: F0 und Richtung bei Fahrstufe 0','Beide Prüfaufnahmen folgen dem Richtungsbefehl ohne Anrollen. F0 aus schaltet beide Stirnlichtfunktionen aus. Zeitverhalten protokollieren; keine Ein-/Ausblendverzögerung.'),
('C5: Mehrfach wiederholen','Mindestens fünf Richtungswechsel im Stand. Kein verlorener Befehl, keine Änderung des Soundzustands durch den Richtungswechsel, sofern nicht bewusst programmiert.'),
('C6: Versorgung neu starten','Gemeinsam neu starten und C4 wiederholen. Danach am fachkundigen Prüfaufbau mit getrennter Einspeiseschaltung auch unterschiedliche Einschaltreihenfolgen prüfen. Keine Decoder unter Spannung stecken.'),
('C7: Neue mfx-Adressvergabe','Für G0 erforderlich: An einer Testzentrale, die den Master noch nicht kennt, automatisch anmelden und Slave-Folgen prüfen; danach Rückkehr zur CS3. Eine geänderte Adresse nur bei eigenem Nachweis als geprüft markieren. Ohne Nachweis G0 offen; keine produktiven Lokdaten löschen.'),
('C8: Dokumentieren','Decoder- und Softwarestände, Herkunft/Format der Masterdaten, ausgelesene Slave-Einstellung, CS3-Eintrag und alle Ergebnisse sichern.')],[2.1,4.4])
add('Ein bestandener Prüfstandstest bestätigt die Adress-/Funktionskopplung, noch nicht Motor, LoDi-LEDs, Innenbeleuchtung oder Signalhalt des fertig umgebauten Zuges. Diese werden nach Einbau erneut abgenommen. Synchronisation kopiert weder Helligkeit noch Lichtmapping.')
warn('Abbruch und Rückweg','Scheitert eine Pflichtfunktion, den Gesamtumbau für diese Architektur nicht beginnen. Gesicherte Konfigurationen erhalten, Fehlerfall protokollieren und klären lassen. Keine Traktion, DCC-Ersatzlösung oder Decoderneuanschaffung stillschweigend als Zielerfüllung einsetzen.')
refs(7,15)

original('1. Bauteile und Werkzeuge bereitlegen',[
('einen passenden auswählen.','Impedanz und Baugröße nach Setunterlagen wählen; steckbare Anbindung siehe 9b.'),
('Für ESU-Einrichtung und nicht sicher messbare Lastprüfungen Zugang zu geeignetem Programmer/Prüfstand oder einem Fachbetrieb einplanen.','Zusätzlich: Zugang zum ESU 53451 mit Windows-PC und geeigneten Prüfaufnahmen nach Kapitel A. Vier einzeln isolierte Hilfsprüfleitungen für Kapitel 6a. Genaue Stecker-, Widerstands- und Befestigungsteile erst nach Maß-/Netzprüfung bestellen.')])
original('2. Das Multimeter richtig vorbereiten',[
('Einen blanken Schraubenkopf nur nach dieser Gegenprobe als Bezug verwenden.','Einen blanken Schraubenkopf nur nach dieser Gegenprobe als Bezug verwenden. Nach endgültigem Ansetzen der Klemmen und nach jeder Messreihe die positiven Gegenproben aus Kapitel 6a wiederholen.')])
original('3. Die vier elektrischen Bereiche trennen')
original('4. Altzustand am Motortriebkopf erfassen',[
('step(7,',"warn('G0 zuerst abschließen','Die folgenden Ausbauarbeiten beginnen erst nach bestandenem Decoder-Vorabnachweis aus A-C. Solange G0 offen ist, nur Fotos und äußerlich zugängliche Merkmale dokumentieren.')\nstep(7,")])
original('5. Motor 60941 montieren und entstören',[
('in der Reihenfolge der Märklin-Zeichnung einsetzen.','anhand der Märklin-Explosionszeichnung zuordnen und passend montieren. Die Beilage enthält keinen ausformulierten Montageablauf; die folgenden Arbeitsschritte sind daraus abgeleitet, keine wörtliche Herstelleranweisung.')])

page('6. Motorisolation: Messaufbau')
story.append(Sketch('motor'))
add('Dies ist eine eigene Prüfmethodik für den mechanisch montierten, elektrisch abgetrennten Motor. Die Foto-Punkte stehen in Kapitel 22. M1 und M2 sind Arbeitsnamen für die Bürstenanschlüsse; sie haben keine feste Plus-/Minuspolung.')
warn('Zuerst spannungsfrei und ohne Elektronik','Zug vollständig vom Gleis nehmen. Beide Decoder, Puffer und sonstige Energiespeicher physisch abtrennen. Beide Motorleitungen von der übrigen Elektronik lösen. Unklar gespeicherte Energie nicht durch Zeitraten oder Kurzschließen beseitigen; nach Herstelleranweisung klären. Kein Widerstandstest an gespeister Elektronik.')
step('14','Vier Hilfsprüfleitungen vorbereiten.','Jede Hilfsleitung einzeln Ende-zu-Ende messen und ihren Widerstand notieren. Kleine isolierte Prüfclips verwenden: PM1 an M1, PM2 an M2, PX an die gerade geprüfte Gegenstelle, PX2 an einen zweiten Punkt desselben Bezugspfads. Die Metallteile der Clips dürfen keine Nachbarteile berühren.')
step('15','Klemmen unverändert lassen.','Die vier Clips bleiben während einer Messreihe am Fahrzeug fest. Nur die Multimeterleitungen an den beschrifteten freien Enden umstecken. Diese freien Enden einzeln gegen Berührung sichern. Ist eine sichere Befestigung nicht möglich, Prüfung fachkundig durchführen lassen.')
table(['Gegenstelle X','Zwei Punkte für PX und PX2'],[
('Chassis','Zwei blanke, leitend zusammengehörige Stellen desselben Chassisteils.'),
('Motor-Metallrahmen','Zwei blanke Stellen des tatsächlich geprüften Rahmens; nicht pauschal mit Chassis gleichsetzen.'),
('Radmasse / Gleis 0','Zugehöriger Anschluss und eindeutig kontaktierende metallische Radfläche beziehungsweise zweiter bestätigter Punkt dieses Pfads.'),
('Schleifer / Gleis B','Schleiferfläche und eigener Schleiferanschluss. PX2 ist hier NICHT das Chassis.')],[1.8,4.7])
add('<b>Jede Gegenstelle einzeln prüfen.</b> Wenn zwei Punkte desselben Pfads nicht sicher erreichbar oder zuordenbar sind, keine scheinbar bestandene OL-Prüfung notieren. Keine Brücke zwischen B und 0 herstellen.')

page('6a. Motorisolation: jede Messreihe vollständig')
add('Multimeter: Schwarz COM, Rot V/Ω. Null-/Offenprobe nach Kapitel 2. Clips am Fahrzeug bleiben unverändert. Widerstände von Mess- und Hilfsleitungen berücksichtigen; deshalb kein allgemeiner Grenzwert wie 0,3 Ω.')
table(['Reihenfolge','Messpaar','Erwartung und Handlung'],[
('1 - positive Referenzprobe','PX - PX2','Niedriger, reproduzierbarer Widerstand wie beim geprüften Leitungsweg. Sonst Bezug oder Clips klären; nicht fortfahren.'),
('2 - positive Motorprobe','PM1 - PM2','Nach möglichem Ladeeffekt bleibender endlicher Motorwiderstand. Ein kurzer Ausschlag genügt nicht. OL: Motorfahnenkontakt, Bürsten und Motorpfad klären.'),
('3 - Isolation M1','PM1 - PX','Stabil offenen Zustand gemäß Messgeräteanleitung notieren. Jeder bleibende endliche Wert oder unklare Befund: STOPP.'),
('4 - Isolation M2','PM2 - PX','Gleiche Prüfung, eigener Protokollwert. Eine bestandene Bürste ersetzt nicht die andere.'),
('5 - Referenz-Nachprobe','PX - PX2','Muss weiterhin die positive Verbindung aus 1 zeigen.'),
('6 - Motor-Nachprobe','PM1 - PM2','Muss weiterhin den bleibenden Motorpfad aus 2 zeigen.')],[1.6,1.5,3.4])
warn('Eine fehlgeschlagene Nachprobe entwertet die Messreihe','War ein Clip lose, sind die dazwischenliegenden OL-Werte nicht als bestanden anzusehen. Kontaktproblem beheben und alle sechs Schritte wiederholen. Das Abheben einer Messspitze zeigt lediglich einen offenen Stromkreis und beweist keinen zuvor guten Kontakt.')
step('16','Bewegung und neue Gegenstellen.','Rotor vorsichtig in mehrere Positionen bringen und Drehgestell in normale Endlagen bewegen, ohne das Getriebe zu erzwingen. Nach jeder Lageänderung die komplette Sechserfolge wiederholen. Für jede weitere Gegenstelle PX/PX2 neu bestimmen und neu prüfen. Bei bewegtem oder neu angesetztem Clip ebenfalls von vorn beginnen.')
add('OL bei der Motorprobe in einer bestimmten Rotorstellung nicht durch Weiterdrehen als erledigt behandeln. Unterbrochener Bürsten-/Motorpfad bleibt eine Fehlerursache. Die Kontaktprobe bestätigt keinen vollständig gesunden Motor.')
warn('OL schließt einen falschen Kondensator nicht aus','Ein Kondensator von Bürste zu Metall kann sich beim Gleichstromtest aufladen und danach OL ergeben. Deshalb zusätzlich jeden Kondensator an beiden Enden verfolgen. Nur der bestätigte Quer-Kondensator M1-M2 bleibt im vorgesehenen Aufbau; siehe Kapitel 5 und 21.')

page('6b. Motor-Messprotokoll und Fehlerbilder')
table(['Datum / Stellung / Gegenstelle','Vorprobe X / Motor','Isolation M1 / M2','Nachprobe X / Motor'],[
('Chassis / gerade','________ / ________','________ / ________','________ / ________'),
('Motorrahmen / gerade','________ / ________','________ / ________','________ / ________'),
('Radmasse / gerade','________ / ________','________ / ________','________ / ________'),
('Schleifer / gerade','________ / ________','________ / ________','________ / ________'),
('Rotorstellung / Kurve: ______','________ / ________','________ / ________','________ / ________'),
('Rotorstellung / Kurve: ______','________ / ________','________ / ________','________ / ________'),
('Weitere Reihe: __________','________ / ________','________ / ________','________ / ________')],[2.2,1.7,1.7,1.7])
table(['SOLL','FEHLER','Folge'],[
('Referenz vor und nach der Messung leitend','Schwarzer Bezug sitzt auf Lack; M1/M2 zeigen scheinbar OL','Keine Isolationsfreigabe.'),
('Motorpfad vor und nachher bleibend messbar','Roter Motorclip sitzt auf Kunststoff; scheinbares OL','Kontakt neu herstellen, ganze Reihe wiederholen.'),
('Keine Bürsten-Metall-Verbindung','Feder oder Schraube schließt nur in Kurven','Nicht fahren; mechanische Ursache klären.'),
('Kondensatoren an beiden Enden zugeordnet','Masse-Kondensator lädt sich auf; anschließend OL','Ohmtest allein übersieht den Fehler; Sicht-/Netzprüfung nötig.')],[2.1,2.7,1.8])
add('Nach allen Prüfungen sämtliche Hilfsleitungen entfernen. Keines ihrer freien Enden darf im später bestromten Fahrzeug verbleiben. Tatsächliche Motorleitungen erst nach G1/G2 nach dem bestätigten Anschlussplan wieder anschließen.')

original('7. Versteckte Massekontakte finden',[
('Gegenprobe: Rote Spitze abheben muss OL ergeben. Bleibt die Anzeige gleich, zuerst Messgerät/Prüfclips untersuchen.','Null-/Offenprobe des Geräts und die vollständigen Vor-/Nachproben aus Kapitel 6a wiederholen. Abheben einer Spitze allein ist kein Kontaktbeweis.')])
original('8. Die rote Motorplatine sicher zuordnen',[
('Die Herstelleranleitung nennt R4/R5 für LEDs. Keine Null-Ohm-Brücke für Glühlampen übernehmen. Bestückung der eigenen Revision verifizieren.','LoDi nennt R4/R5 im Lampen-/LED-Hinweis. R3/R6-Funktion und Bestückung der eigenen Revision sind nicht gesichert. Verzinnung ist kein Brückennachweis. Keines dieser Teile auf Verdacht ändern.'),
('Rückseite und Revision fehlen','Beschriftete Anschlussseite des eigenen Exemplars fehlt'),
('Vor Montage seine Funktion messen; weder Masse noch Isolation pauschal annehmen.','Vor Montage die Befestigungsfreigabe nach Kapitel 9 abschließen; einen unbekannten Ring weder als Masse noch als isoliert voraussetzen.'),
('Vor dem Löten Aufdrucke sowie alle Anschlussbezeichnungen dokumentieren.','Die wesentlichen Gleis-, Motor- und Frontanschlüsse sind im gezeigten Bild nicht beschriftet. Vor dem Löten die andere Seite mit lesbarer Revision und Anschlüssen dokumentieren. LoDi veröffentlicht solche Beschriftungen im Herstellerbeispiel; siehe Kapitel 9a.')])

page('9. Platinenbefestigung: sichere Freigabe')
story.append(Sketch('screw',160))
step('22','Trocken prüfen.','Nur nach G0: ohne Decoder, Puffer und Lasten die tatsächliche Platine an den vorgesehenen Haltepunkten auflegen. Beide Seiten und die ganze spätere Schrauben-/Unterlegscheibenfläche ansehen. Nicht nachfeilen und keine längeren Schrauben auf Verdacht verwenden.')
step('23','Jeden Haltepunkt einzeln dokumentieren.','Für Ring A und Ring B jeweils Foto, Revision, Schraubenlänge, Auflage und mögliche Berührung festhalten. Eine sichtbare Kupferfläche ist nicht automatisch Gleismasse. Die elektrische Ringzuordnung braucht einen belastbaren revisionsbezogenen Nachweis oder fachkundige Leiterbahnprüfung.')
table(['Prüffeld','Ring A','Ring B'],[
('Aufdruck/Foto und Soll-Netz laut Nachweis','____________','____________'),
('Bestätigtes Netz / Herkunft der Zuordnung','____________','____________'),
('Schraube, Auflage und Unterseite berührungsfrei zu Fremdnetzen','____________','____________'),
('Montiert: keine neue ungewollte Verbindung','____________','____________'),
('Gehäuse geschlossen / Bewegung ebenfalls geprüft','____________','____________')],[3.5,1.5,1.5])
warn('G1-STOPP bei ungeklärtem Ring','Ohne eindeutige Zuordnung keine leitende Schraubmontage und keine Bestromung. Anfänger sollen keine eng benachbarten 21MTC-Pins mit freien Spitzen abtasten. Ein Piepton über unbekannte Bauteile ist kein Leiterbahnnachweis.')
add('Fachkundiger Ausweichweg: vollständig isolierende Halterung mit isolierter Schraubenführung auslegen. Vor Verdrahtung beide zugänglichen Ringe gegen positiv bestätigtes Chassis prüfen: kein leitender Montagekontakt. Kontaktierung vorher/nachher positiv bestätigen. Danach Radmasse über das dokumentierte MASSE-Pad verdrahten; dieser Pfad zum Chassis ist erwünscht. Eine Kunststoffscheibe nur oben genügt nicht. Maße und Passung sind offen; dies ist keine Halter-Kaufempfehlung.')
refs(1,3)

page('9a. Anschlussnamen: Motortriebkopf')
add('Herstellertext zur LoDi-Motor WiB ICE-M(-S), Beispiel 33701. Die Positionen sind erst nach Abgleich mit der Beschriftungsseite des eigenen Exemplars verbindlich. Nicht auf die unbeschriftete Bildseite von Kapitel 8 spiegeln.<super>3</super>')
table(['Aufdruck / Herstellerbezeichnung','Funktion im vorgesehenen Aufbau','Anschlussregel'],[
('SW / SCHLEIFER','Örtlicher Mittelschleifer','Nur bestätigter Rohstrompfad.'),
('RT / KUPPLUNG','Gemeinsamer Mittelleiterpfad zum anderen Kopf','Nicht mit GE oder Decoder-U+ verbinden.'),
('GE / KUPPLUNG','Geschalteter Wagenbeleuchtungspfad','Nur vorn speisen; hinten kein zweiter Decoder-Ausgang.'),
('MASSE','Gleisrückleiter / Radmasse des Kopfes','Kein Decoder-GND; sichere Radkontakte erhalten.'),
('MOT_L / MOT_R','Motoranschlüsse','Je eine Entstördrossel in Serie; Motorfahnen gegen Metall isoliert.'),
('VCC beim Frontanschluss','Gemeinsames LED-Plus laut LoDi-Zuordnung','Orange im Herstellerbeispiel. Nicht interne 21MTC-Vcc oder Radmasse.'),
('L_WS / L_RT','Weißer / roter LED-Zweig','Mit wirksamer vorgesehener Strombegrenzung; keine Lampenbrücke übernehmen.'),
('LS1 / LS2','Zwei Lautsprecheranschlüsse','Nur Lautsprecher bzw. passender Adapter; siehe 9b.'),
('AUX3 / AUX5, PANTO, S2','Zusatz-/Kontaktfelder','In dieser Fassung keine Anschlussfreigabe aus dem Namen ableiten; unbenutzt lassen, bis tatsächlich zugeordnet.')],[1.9,2.2,2.5])
step('24','Erst nach vollständiger Padzuordnung löten.','Decoder bleibt abgezogen. Jede Leitung einzeln beschriften, passend kurz abisolieren und verzinnen, ohne Zug anlöten. Lupe: keine Zinnbrücke, einzelne Litzenfäden oder Lötperlen. Nach jedem Anschluss Sollpfad prüfen, nicht erst nach der gesamten Verdrahtung.')
warn('VCC und Jumper sind revisionsabhängig zu lesen','LoDi-VCC für den beschriebenen Fronteinsatz ist nicht Pin 12 der 21MTC-Norm. Abweichende Plus-/Minus-schaltende Ausgänge nicht mischen. Bei Revisionen mit AUX-Wahl über SJ1/SJ2 niemals beide Brücken gleichzeitig setzen. SJ2 der weißen Wagenplatine hat eine andere Funktion.')
refs(3,10)

page('9b. Lautsprecher anschließen, Stecker erhalten')
add('Der 60977-Lautsprecher ist für den Steckanschluss der Märklin-Trägerplatine vorgesehen. Am vorderen LoDi-Träger werden LS1/LS2 verwendet. Daher muss die Anleitung den Übergang ausdrücklich festlegen; der Stecker muss nicht zwangsläufig abgeschnitten werden.<super>1,3</super>')
step('L1','Tatsächlichen Lautsprecher identifizieren.','Artikelset und beigefügte Lautsprecher vergleichen. Nennimpedanz und erlaubte Last aus Herstellerunterlagen bestätigen; eine Gleichstrom-Widerstandsmessung allein ist kein Nennimpedanznachweis. Nur einen zum 60977 passenden Lautsprecher verwenden.')
step('L2','Stecker vermessen.','Scharfe Ansicht von Kontaktseite und Seite, Kontaktabstand und Gehäusemaße dokumentieren. Zwei Pole oder eine weiße Gehäusefarbe reichen nicht für eine JST-/Rasterzuordnung. Solange der Gegenstecker nicht sicher bestimmt ist, Originalstecker erhalten.')
step('L3','Passenden Adapter vorbereiten.','Bevorzugt einen verifizierten zweipoligen Gegenstecker mit zwei isolierten Anschlusslitzen verwenden. Ohne Decoder und ohne angeschlossenen Lautsprecher jeden Kontakt bis zu seiner Litze auf Durchgang prüfen; zwischen den beiden getrennten Litzen darf keine Drahtbrücke bestehen. Vor-/Nachprobe der Messkontakte beachten.')
step('L4','An LS1/LS2 anlöten.','Decoder und Puffer entfernt. Je eine Adapterlitze an ein bestätigtes Audio-Pad löten, einzeln isolieren und zugentlasten. Nicht am Lautsprecher selbst oder an seiner Membran ziehen. Den fertigen Adapter vor dem Einstecken des Lautsprechers nochmals prüfen.')
step('L5','Mechanik und Funktion.','Schallkapsel sicher befestigen, Membran freihalten und Gehäusepassung prüfen. Erst nach elektrischer Freigabe Lautsprecher stecken. Erster Soundtest mit kleiner Lautstärke. Bei Verzerrung, Erwärmung oder Überlast abschalten und Ursache klären.')
warn('Audioleitungen sind kein Masseanschluss','Weder LS1 noch LS2 an Chassis, +Ub/VCC, GND oder +5V anschließen. Kein zweiter Lautsprecher parallel auf Verdacht. Steckerabschneiden wäre ein eigener Kabelumbau und wird hier nicht als notwendiger Standardschritt angewiesen.')
refs(1,3)

original('10. Front-LEDs gefahrlos identifizieren')
original('11. Hintere Vorwiderstände bestimmen',[
('Reines Zahlenbeispiel','Nicht als Einkaufsliste verwenden'),
('7,5 Ω und 7,5 kΩ unterscheiden sich um Faktor 1000.','7,5 Ω und 7,5 kΩ unterscheiden sich um Faktor 1000. Die endgültigen Werte stehen erst im ausgefüllten LED-Protokoll, nicht automatisch im Beispiel.')])

page('11a. LED-Ströme und Helligkeit abstimmen')
add('Die vordere LoDi-Strombegrenzung ist eine sinnvolle Referenz, aber ihr realer Strompfad muss zuerst zur vorhandenen Revision passen. Der Code 2201 entspricht 2,2 kΩ. Dass R4/R5/R6 im berichteten Herstellerfoto denselben Code tragen, ersetzt keine Zuordnung ihres jeweiligen Zweigs. R3-Verzinnung allein belegt keine Lampenbrücke.<super>3,20</super>')
table(['Vor endgültiger Bestückung ausfüllen','Weiß','Rot'],[
('Tatsächlicher LED-Zweig / Revision','__________','__________'),
('Maximale Versorgung am Zweig, Mess-/Nachweisweg','__________','__________'),
('Zulässiger Strom und minimale Zweigspannung / Quelle','__________','__________'),
('Vorderer wirksamer Serienwiderstand / Strompfad','__________','__________'),
('Hinterer Widerstand, Toleranz, Belastbarkeit','__________','__________'),
('Stromgrenze eingehalten / geprüft durch','__________','__________'),
('Helligkeit vorne/hinten nach Montage abgestimmt','__________','__________')],[3.8,1.4,1.4])
add('Nur unter gleicher Versorgung, angenommener LED-Flussspannung und Ansteuerung ergibt 7,5 / 2,2 ungefähr das Stromverhältnis 3,41. Beispiel Weiß bei 24 V und 3 V Flussspannung: 9,55 mA gegenüber 2,80 mA. Das ist keine Messung an diesem Zug und kein garantiertes Verhältnis der sichtbaren Helligkeit.')
step('H1','Zuerst Stromsicherheit.','Endgültige Widerstände erst aus bestätigten Eingaben auswählen. Keine Absenkung auf 2,2 kΩ nur wegen eines Fotos; keine Erhöhung von PWM-Werten als Ersatz für eine fehlende Strombegrenzung.')
step('H2','Danach optisch abstimmen.','Beide Köpfe mit eingesetzten Lichtleitern und Gehäusen bei gleichem Umgebungslicht farbweise vergleichen. Den helleren Ausgang mit Decoder-Dimmung passend reduzieren. Rot und Weiß getrennt bewerten. Dabei muss der ungedimmte Einschaltstrom bereits sicher begrenzt sein.')
warn('G3 bleibt bis zum ausgefüllten Stromnachweis offen','Die Zahlenbeispiele begründen weder eine Kauf- noch eine Lötfreigabe. Die zulässigen Daten der tatsächlichen LoDi-514-Einsätze sind hier noch nicht vollständig dokumentiert.')
refs(3,20)

class SourceDiagram(Flowable):
    def __init__(self,path):
        Flowable.__init__(self); self.path=path; self.width=350; self.height=300
    def draw(self):
        with PILImage.open(self.path) as im: iw,ih=im.size
        # Clip the unchanged complete source image to its actual diagram.
        left,top,right,bottom=.055,.23,.49,.765
        sw=(right-left)*iw; sh=(bottom-top)*ih
        scale=min(self.width/sw,self.height/sh)
        c=self.canv; c.saveState(); q=c.beginPath(); q.rect(0,0,sw*scale,sh*scale); c.clipPath(q,stroke=0)
        c.drawImage(self.path,-left*iw*scale,-(1-bottom)*ih*scale,width=iw*scale,height=ih*scale)
        c.restoreState()

page('12. Märklin-Träger im motorlosen Kopf')
story.append(SourceDiagram('/Users/martinwaelter/ICE Umbau/Arbeitsstand_REV10/bilder/ice2976_60977-p5-pads.jpg'))
add('Vergrößerter Ausschnitt der unveränderten Originalzeichnung, Märklin-Anleitung S. 5. Kein Foto des vorhandenen Trägers; Positionen erst nach Übereinstimmungsprüfung verwenden. Die links gezeichnete Buchse SUSI und die darunter liegende Lautsprecherbuchse sind getrennte Anschlüsse.<super>1</super>','small')
table(['Tatsächlicher Aufdruck laut Zeichnung','Vorgesehener Anschluss hinten'],[
('B/GR','RT-Rohstrompfad mit hinterem Schleifer.'),
('0/GL','Örtlicher Rad-/Schienenrückleiter.'),
('+Ub','Gemeinsames LED-Plus; nicht +5V, GND oder Chassis.'),
('LV','Bei der festgelegten Zuordnung in 12a: roter LED-Zweig über seinen Widerstand.'),
('LR','Bei der festgelegten Zuordnung in 12a: weißer LED-Zweig über seinen Widerstand.'),
('MR, MV, AUX1-AUX4, GND, +5V','Im hinteren Aufbau unbenutzt; vorhandene lose Litzen jeweils einzeln isolieren.')],[2.3,4.2])
warn('G1: vorhandenen Träger vorher abgleichen','Beide Seiten, Index, Bestückung und Anschlüsse müssen mit der vorgesehenen Verwendung übereinstimmen. 59649 ist die MKL-Ausführung, trotzdem keine Freigabe allein durch mechanisches Passen. +5V ist mit eingesetztem ESU kein allein durch den Aufdruck bewiesener Versorgungswert. SUSI/60974 hinten nicht anschließen.')
refs(1,10,15)

page('12a. Hinteres Rot/Weiß eindeutig zuordnen')
story.append(Sketch('led'))
add('Beide ESU-Kästen sind derselbe hintere 59649: Plus an +Ub, oberer weißer Zweig über seinen Widerstand an LR, unterer roter Zweig an LV.','small')
add('Eine feste Variante, keine Auswahl nach Intuition: Der Zugbegriff <b>vorwärts</b> bedeutet hier Motortriebkopf voraus. Auf beiden Decodern muss F0 vorwärts den physischen Ausgang Licht vorne/LV und F0 rückwärts den Ausgang Licht hinten/LR schalten. Keine zusätzlichen richtungsabhängigen Mappingzeilen dürfen das Gegenteil bewirken.')
table(['Befehl am gemeinsamen ICE','Motortriebkopf','Motorloser Kopf'],[
('F0 ein, vorwärts, Fahrstufe 0','Weiß über LoDi L_WS','Rot über Widerstand an LV'),
('F0 ein, rückwärts, Fahrstufe 0','Rot über LoDi L_RT','Weiß über Widerstand an LR'),
('F0 aus, beliebige Richtung','Weiß und Rot aus','Weiß und Rot aus')],[2.8,1.9,1.9])
step('32','Altlicht elektrisch entfernen.','Alte Lampenfassung nicht weiter elektrisch nutzen. Schleifer/Radmasse vorher zuordnen. Die neue Plusleitung darf keine Feder- oder Schraubverbindung zum Chassis haben.')
step('33','Mapping vor Verdrahtung bestätigen.','Am einzeln ausgelesenen 59649 die Funktionszuordnung entsprechend der Tabelle festlegen und speichern. Über den ESU-Zugang wieder auslesen. Nicht auf spätere freie M4-Mappingbearbeitung an der CS3 vertrauen. Wenn das Mapping anders ist, diese Verdrahtung nicht ungeprüft übernehmen.')
step('34','Träger und LEDs verbinden.','Nur bei G1 und bestätigter LED-Strombegrenzung: Plus an +Ub, Rot über eigenen Widerstand an LV, Weiß über eigenen Widerstand an LR. 21MTC-Index mit Decoderunterlagen vergleichen; nicht versetzt oder umgedreht aufstecken.')
step('35','Endkontrolle.','Unbenutzte Leitungen einzeln isolieren; GE des Wagenbusses nicht an einen hinteren Ausgang anschließen. Drehgestellbewegung, Halter und Gehäuse kontrollieren. Nach Freigabe zuerst die drei Zustände bei Fahrstufe 0 testen; danach langsame Fahrtrichtung mit ausreichendem Platz überprüfen.')
warn('Physischer Ausgang ist nicht die Lage am Zug','LV heißt Licht vorne des Decoders, nicht weißes Licht an jeder Zugnase. Durch die entgegengesetzte Einbaulage muss bei dieser festen Mappingvariante hinten Rot an LV liegen. Nicht zusätzlich unkontrolliert Fahrtrichtung oder Mapping invertieren.')
refs(1,6,15)

original('13. Mittelwagenplatinen montieren',[
('Flexible Litzen von jeder Kupplung zur vorgesehenen Platinenstelle führen.','Erst Kontaktzuordnung und passive Prüfungen nach 14a sowie Platinen-Vorprüfung nach 14b abschließen. Dann flexible Litzen von jeder Kupplung zur bestätigten Platinenstelle führen.')])

page('14. Kupplungsbus: vor dem ersten Löten')
story.append(Sketch('bus',200))
step('39','Mechanische Passprobe.','Kopf-Kupplungen E395640/E395660 und Wagenenden E374340/E374060 bleiben Teilekandidaten aus verwandten Modellen, keine bestätigte 2976-Einkaufsliste. Aufnahme, Rastung, Endprofil und Beweglichkeit des vorhandenen Modells vergleichen. Keine Passung durch Gewalt herstellen.')
step('40','Physische Kontakte fest benennen.','Jede Kupplung in eindeutig fotografierter Ansicht mit provisorischen Namen K1/K2 markieren. Durchgang von jeder Kontaktfläche zu ihrem freien Kabel bestimmen. Kein festes Links/Rechts-RT aus einem spiegelbaren Foto raten. Die Sollzuordnung nach bestätigtem RT- und GE-Anschlussplan vor dem Anlöten festhalten.')
step('41','Jede Übergangsstelle einzeln zuordnen.','Zusammengehörige Kupplungshälften stromlos verbinden und über deren freie Enden feststellen, welcher Kontakt welchen Partner berührt. Die Zuordnung vom bestätigten vorderen RT- beziehungsweise GE-Pad aus durch den Zug fortschreiben, nicht nachträglich passend umbenennen.')
table(['Unabhängiger Bezugspunkt','Sollfunktion im gewählten LoDi-Betrieb'],[
('Vorderer bestätigter LoDi-RT-Anschluss','Roh-Mittelleiterpfad RT; an der Wagenplatine an O.'),
('Vorderer bestätigter LoDi-GE-Anschluss','Geschalteter Lichtpfad GE; an der Wagenplatine an L.'),
('Wagenplatine B','In dieser zweipoligen Variante kein zusätzlicher Radmasseanschluss.'),
('Hinterer Decoder','B/GR an RT, 0/GL an eigene Radmasse. GE nicht zusätzlich speisen.')],[2.9,3.6])
warn('Nur ein freigegebener Stromkreis','Der RT-Bus verbindet beide Schleifer. Kein Überbrücken von Haupt-/Programmierausgang, Gleisanschlussbox und CS3 oder verschiedenen Boosterkreisen zulassen. Vor Umstecken immer abschalten und elektrische Trennung herstellen.')
refs(3,4,13)

page('14a. Passive Kupplungsprüfung')
add('Diese Karte gilt nur für einen tatsächlich passiven Abschnitt: beispielsweise zwei zusammengesteckte Kupplungen mit freien Anschlusslitzen. Decoder, Puffer und LoDi-Beleuchtungselektronik sind nicht angeschlossen. Die vier Enden müssen vorher unabhängig als RT-A, GE-A, RT-B, GE-B zugeordnet sein.')
step('K1','Messkontakt sichern.','Vier isolierte Hilfsclips an den vier freien Enden befestigen. Während einer Reihe keine Fahrzeugklemme verändern. Beide gewünschten Durchleitungen zuerst positiv nachweisen. Fehlt eine, die scheinbar offenen Kreuzpfade nicht als bestanden werten.')
table(['Messpaar','SOLL ohne Elektronik'],[
('RT-A - RT-B','Niedriger, stabiler Widerstand des gewünschten Pfads.'),
('GE-A - GE-B','Niedriger, stabiler Widerstand des gewünschten Pfads.'),
('RT-A - GE-B','Offen / OL bei gesicherten Messkontakten.'),
('GE-A - RT-B','Offen / OL bei gesicherten Messkontakten.')],[3.2,3.3])
step('K2','Nachproben.','Nach den beiden Kreuzmessungen beide gewünschten Durchleitungen erneut messen. Nur wenn auch diese positiven Nachproben gelingen, ist die Reihe gültig. Kupplung normal ausschwenken, danach die gesamte Folge wiederholen.')
table(['Fehlerbild','Bedeutung','Reaktion'],[
('RT-RT offen, RT-GE leitend','Kreuzung oder falsche Endpunktkennzeichnung','Zuordnung klären; nicht Bezeichnungen nachträglich tauschen.'),
('Beide Sollpfade leitend, Kreuzpfad ebenfalls direkt leitend','Draht-/Zinnbrücke oder Kurzschluss im passiven Abschnitt','Nicht anschließen; Ursache lokalisieren.'),
('Nachprobe eines Sollpfads offen','Kontakt während der Reihe verloren','Ergebnisse ungültig; Klemmen prüfen und wiederholen.'),
('Gesamtzug stimmt, einzelner Abschnitt nicht','Zwei Kreuzungen können sich außen aufheben','Jede Übergangsstelle einzeln korrigieren und erneut prüfen.')],[2.1,2.1,2.3])
warn('Diese OL-Tabelle ist keine Regel für bestückte LoDi-Leisten','Die Wagenplatine enthält absichtlich Elektronik zwischen den Versorgungswegen. Kein Bauteil und keine Leiterbahn entfernen, um für diese Tabelle ein OL zu erzwingen. Weiter mit 14b.')

page('14b. Wagen mit unveränderter LoDi-Leiste')
add('Die vorhandene Platine übernimmt die Längsdurchleitung; sie bleibt unverändert. Gemessen werden daher zuerst die eindeutigen Pad-/Kontaktzuordnungen. Elektronische Kreuzpfade werden nicht wie freie Drähte bewertet.')
step('W1','Vor Anschluss der Kupplungslitzen.','Leiste stromlos ohne weitere Verbindungen prüfen: Revision, Aufdrucke L/O/B und Betriebsart dokumentieren. L-Ende A zu L-Ende B sowie O-Ende A zu O-Ende B müssen als vorgesehene Durchleitungen bestätigt werden. Elektronische Querpfade und Messrichtung dokumentieren; bei unklarer Zuordnung fachkundig klären.')
step('W2','Jede Litze vorher einzeln prüfen.','Kupplungskontakt bis zum freien Litzenende messen, beschriften und mit der dokumentierten Sollfunktion abgleichen. Passive Kupplungsprüfung 14a abschließen, bevor die Elektronik angeschlossen wird.')
step('W3','Im bestätigten Motorplatinenbetrieb anschließen.','RT-Litzen an die vorgesehenen O-Pads, GE-Litzen an L. Kleine Bewegungsschlaufe freihalten. Keine zusätzliche Längsleitung nötig, keine Decoder-Ausgänge hinten an GE. Radkontakte der Triebköpfe bleiben erhalten.')
step('W4','Jeden Kontakt zum richtigen Pad kontrollieren.','Für jede Kupplungsseite den RT-Kontakt zum tatsächlichen O-Pad und GE zum L-Pad prüfen. Sichtkontrolle auf falsche Lötstelle oder Zinnbrücke. Danach L-L und O-O durch den ganzen Wagen erneut kontrollieren, auch bei normaler Deichselbewegung.')
step('W5','Querpfade richtig beurteilen.','Bei bestückter Leiste ist ein endlicher Messwert zwischen L/O nicht automatisch ein Fehler und OL kein pauschaler Pflichtwert. Mit dokumentiertem beziehungsweise fachkundig bestätigtem Platinenverhalten vergleichen. Auffällige Abweichung: Anschlusslitzen zur Eingrenzung wieder lösen, nicht die LoDi-Leiterbahn schneiden.')
table(['Wagen / Revision','L-L / O-O','Vier Kontakt-Pad-Zuordnungen','Querpfad / Sicht / Bewegung'],[
('____________','____________','____________','____________'),
('____________','____________','____________','____________'),
('____________','____________','____________','____________')],[1.6,1.5,2.1,2.1])
warn('Durchgang ist noch keine Stromtragfähigkeitsprüfung','Der gemeinsame RT-Pfad kann bei Ausfall des vorderen Schleifers den Motorstrom durch alle Kupplungen führen. Zulässige Wagenzahl nicht aus einem kleinen Ohm-Messstrom ableiten. Belastung und Spannungsabfall nach Kapitel 18 separat prüfen.')
refs(4)

original('15. Den vorhandenen 60974 vorbereiten',[
('refs(9,10,11)','refs(9)'),
('vor erneutem Löten trennen und korrekt entladen.','vor erneutem Löten trennen. Anschlüsse nie zum Entladen kurzschließen. Solange Restspannung nicht fachgerecht ausgeschlossen ist, keine Lötarbeit.'),
('Die Bezeichnung „VCC“ auf einer anderen Platine allein beweist keine Pinzuordnung.','LoDis VCC beim beschriebenen Frontanschluss ist LED-Plus; die Wortgleichheit beweist aber keinen SUSI-Abgriff. +Ub ist die entsprechende Funktionsplus-Bezeichnung auf der Märklin-Trägerzeichnung, +5V ist davon verschieden.'),
('Am 60977 Firmware 3.2.0.1 oder neuer nachweisen und SUSI nach Märklin einrichten.','Am 60977 Firmware 3.2.0.1 oder neuer ausschließlich auslesen und notieren; Firmware nicht durch Ändern der Versionsanzeige vermeintlich aktualisieren. Insbesondere niemals 77 in CV 7 bzw. das Firmware-Versionsfeld schreiben: Das aktiviert den Einmesslauf; ein anschließender Fahrbefehl kann bis zur Höchstgeschwindigkeit beschleunigen. SUSI nur nach Märklin einrichten.')])

page('16. Konfiguration vor dem Einbau festlegen')
warn('Der erste Synchronisationsversuch gehört nicht mehr hierher','G0 aus A-C muss bereits bestanden sein. Diese Seite dokumentiert die endgültige Fahrzeug-Konfiguration und deren erneute Prüfung nach Einbau. Sie ersetzt keinen der offenen Identitätsnachweise.')
step('45','Prüfprojekte sichern.','Die im Vorabtest verwendeten Decoder- und Softwarestände sowie Projektdateien aufbewahren. Vor späteren Änderungen je Decoder getrennt auslesen. Nie beide Decoder am Programmer lassen.')
step('46','60977 für den echten Motor vorbereiten.','Für den eingebauten 60941-HLA passenden Motortyp anhand der Märklin-Unterlagen wählen. Prüfstand-Motoreinstellungen nicht blind übernehmen. ICE-Soundprojekt mit Märklin-Werkzeug einrichten, niedrige Anfangslautstärke konfigurieren; Soundprüfung erst in Schritt 52. mfx aktiv lassen. Keine automatische Einmessfahrt auf dem kurzen Prüfgleis.')
step('47','59649 mit eindeutiger Lichtzuordnung.','Bestätigte Slave-Identität und M4-Sonderoption beibehalten; Funktion F0 vorwärts auf LV, F0 rückwärts auf LR nach Kapitel 12a prüfen. Keine Bedingungen, die Bewegung voraussetzen, keine ungewollten Fade-Zeiten. Vorhandene konkurrierende Mappingzeilen beseitigen lassen.')
step('48','Innenlicht separat belegen.','Eine freie Funktion wählen, die keinen benötigten Sound überschreibt. AUX-/Jumper-Zuordnung anhand der tatsächlichen LoDi-Motorrevision festlegen. Nicht automatisch AUX4 oder AUX1 unterstellen und nie beide Auswahlbrücken gleichzeitig setzen.')
step('49','Gegen die richtigen Sollstände auslesen.','Jeden Decoder einzeln neu auslesen. Masteridentität und Synchronisationsoption mit G0 vergleichen. Endgültiges Mapping und Fahrzeugparameter mit dem separat vor dem Schreiben gespeicherten Fahrzeugprojekt vergleichen. Gewollte Änderungen gegenüber dem Prüfstandprojekt dokumentieren; bei unerklärter Abweichung nicht bestromen.')
step('50','Sollzustände notieren, noch nicht bestromen.','F0 aus: beide Köpfe dunkel. F0 vorwärts: Motorseite weiß, Dummy rot. F0 rückwärts: Motorseite rot, Dummy weiß. Nur Konfiguration vorbereiten. Funktionstests nach den Freigaben in Kapitel 17: Hauptkopf Schritt 52, beide Köpfe Schritt 54. Fahrt ausschließlich Schritt 53; Innenlicht mit Wagen erst Schritt 56.')
add('Eine reine Adresssynchronisation überträgt keine Bremsabschnitt-Erkennung, keine Helligkeit und kein Mapping. Signalhalt und Puffern bleiben getrennte Freigaben. Firmwareänderungen können einen erneuten Kombinationstest erforderlich machen.')
refs(1,6,7,18)

original('17. Erstes Einschalten ohne Puffer',[
('Motorisolation bestanden; reale Platinen-/Steckbelegung bestätigt; die jeweils angeschlossene LED-Strombegrenzung bestätigt.','G0 bestanden; Motorisolation einschließlich Kontakt-Gegenproben bestanden; reale Platinen-/Steckbelegung bestätigt; die jeweils angeschlossene LED-Strombegrenzung bestätigt.'),
('Eine eigene Anmeldung des Slaves ist kein Prüfkriterium.','Es darf kein neuer zweiter unabhängig zu bedienender Fahrzeugeintrag entstehen. Ein vorhandener alter Eintrag wird dokumentiert, nicht als Lösung versteckt. Bei Zweifel G0 nicht als bestanden werten.'),
('Lichtzustände müssen Abschnitt 16 entsprechen.','Lichtzustände müssen Abschnitt 12a entsprechen.')])
original('18. Belastung und Gehäuseabschluss prüfen')
original('19. CS3-Bremsung später auf der Anlage')
original('20. Fehler gezielt eingrenzen und freigeben',[
('Nullprobe / Chassis-Gegenprobe','G0-Protokoll / Softwarestände / Masterdaten'),
('M1/M2 gegen Chassis, Rahmen, Radmasse, B','M1/M2 gegen alle Gegenstellen; Vor-/Nachproben 6a')])
original('21. Vergleichsfoto: Motor und Kondensatoren')

page('22. Vergleichsfoto: Motor-Messpunkte')
add('Motorisierter Vergleichskopf <b>33701</b> nach Entstörung, nicht das ursprüngliche 2976-Fahrzeug. Nase links, Kupplungsende rechts außerhalb des Fotos. Erst nach eigener Bauteilidentifikation auf den 60941-Umbau übertragen.')
story.append(MarkedPhoto(RESEARCH/'motor_c.jpg',W,[(1,.329,.334,.186,.075),(2,.367,.356,.555,.075),(3,.271,.328,.170,.674),(4,.433,.554,.554,.822)],210))
photocredit('Motor-Messpunkte; unverändertes Vergleichsfoto.', 'https://image.jimcdn.com/app/cms/image/transf/dimension%3D1920x400%3Aformat%3Djpg/path/s5b4f033edf99a04d/image/i228dda660533ed35/version/1635692091/image.jpg')
table(['Punkt / Bildposition','Bedeutung für Kapitel 6/6a'],[
('1: oberhalb der linken Bürstenhülse','M1: blanke Lötfahne; PM1 dort befestigen, nicht auf dem Kunststoff und nicht gleichzeitig an der Schraube.'),
('2: oberhalb der rechten Bürstenhülse','M2: Lötfahne am rechten Ende des Quer-Kondensators; PM2 darf keinen Nachbaranschluss überbrücken.'),
('3: Schraube links oben','Möglicher zweiter Metallreferenzpunkt; Lack/Oxid und tatsächliche Verbindung zuerst prüfen.'),
('4: Lötöse rechts unten','Möglicher Metall-/Rückleiterbezug. Nicht die rechte Motorfahne! Bezug 3-4 und zur realen Radmasse darf nicht aus der braunen Farbe allein abgeleitet werden.')],[2.0,4.6])
warn('Die gültige Messkarte steht vollständig in 6/6a','Vorprobe Referenz + Motor, dann beide Isolationswerte, danach beide positiven Nachproben. Die Fahrzeugclips bleiben dabei unverändert. Kein isolierter Kurzablauf mit „Spitze abheben“; fehlgeschlagene Nachprobe entwertet die Reihe.')

original('23. Vergleichsfoto: motorloser Triebkopf')
original('24. Prüfkarte: verdeckte Kontakte beim Schließen',[
("story.append(Sketch('screw',160))","add('Befestigungsschema und Kontaktgefahren: siehe Kapitel 9.','small')"),
('Zuerst offen die Messwerte aus Abschnitt 6/14 notieren.','Zuerst offen die Messwerte aus 6a und 14a/14b notieren.'),
('Dieselben isoliert geprüften Messpaare erneut messen.','Für Motoranschlüsse nur am Motortriebkopf: Folge 6a. Im Dummy keine Motorprobe: Zwei Punkte desselben abgetrennten Leiters und zwei Punkte des Metallbezugs jeweils positiv vorprüfen, Isolation messen, beide positiven Nachproben wiederholen. Serienwiderstand mit bekanntem Sollwert bewerten. Nicht durch LEDs messen oder freie Motorausgänge verbinden. Vor-/Nachproben im tatsächlich geschlossenen Gehäusezustand durchführen.'),
('Ist das nicht möglich, diese Prüfung fachkundig durchführen lassen.','Vier Hilfsprüfenden nach 6/6a erlauben die Vor-/Nachproben ohne Lösen der Fahrzeugclips. Ist das nicht möglich, diese Prüfung fachkundig durchführen lassen.'),
('Keine Isolierfolie ohne Prüfung über wärmeabgebende Bauteile wickeln.','Decoder nicht mit Isolierband oder Isolierfolie einwickeln. Stattdessen gefährdende Metallflächen geeignet isolieren; Freiraum und Wärmeabfuhr erhalten.')])

page('D. Offene Nachweise gezielt schließen')
table(['Noch erforderlich','Genaues Material / Prüfergebnis','Was dadurch entschieden wird'],[
('G0: Decoder-Test','ESU-Zugang; tatsächliche Firmware; belegte Masterdatenübernahme; ausgefülltes C-Protokoll','Ein mfx-Eintrag und unmittelbares Folgen ohne Traktion.'),
('Foto 1: rote LoDi-Platine','Beide Seiten senkrecht, ganze Platine; Nahaufnahme der Revision, Frontpads und R3-R6; keine bereits angeschlossene Spannung','Revisionsbezogene Pad-, Widerstands- und Jumperzuordnung.'),
('Foto 2: Haltepunkte','LoDi an vorgesehener Position ohne Decoder; beide Stützen, Schrauben und Unterseitenkontaktbereiche sichtbar; Länge und Auflage dokumentiert','Befestigung ohne unerwünschte Metallverbindung.'),
('Foto 3: hinterer Träger / Front','Beide Trägerseiten mit Index, beide Seiten eines LoDi-514-Einsatzes, ggf. vorhandene Beschriftung','21MTC-/Padabgleich und LED-Zweigstruktur.'),
('Foto 4: Lautsprecher / Kupplung','Stecker Kontakt-/Seitenansicht mit Maß; zusätzlich je vorhandene Kopf-/Wagenkupplungsaufnahme von oben/unten','Passender Gegenstecker und originale Kupplungskandidaten.'),
('60974 und Anlage','Vierpoliger bestätigter SUSI-Abgriff auf LoDi; anschließend eigene Puffer- und Signalhaltprüfungen','Nicht durch G0 oder Motorisolation automatisch freigegeben.')],[1.5,3.1,2.0])
add('Fotos zeigen Geometrie und Aufdrucke, keine unsichtbare Netzverbindung. Wenn eine Seite nur schwer zugänglich ist, nichts für ein Foto gewaltsam auseinandernehmen. Messwerte immer mit markierten Endpunkten und Messrichtung liefern.')
warn('Abschlussbericht noch ausstehend','Die vollständigen 86 konsolidierten Findings samt adversarialer Bewertung wurden nicht bereitgestellt. Daher kein behaupteter Finding-für-Finding-Abgleich und keine Übernahme ihrer Prioritäten. Die bisher geposteten Hauptbefunde sind in dieser Prüffassung berücksichtigt; die vollständige Liste bleibt ein eigener Prüfschritt.')

page('E. Dein ausgefüllter Anschlussstand')
add('Vor dem ersten Einschalten diese Werte aus den jeweiligen Arbeitskarten übertragen. Ein leeres Feld ist keine Freigabe. Bewahre die Fotos und die beiden ausgelesenen Decoderprojekte zusammen mit dieser Seite auf.')
table(['Für genau diesen ICE 2976','Einzutragen / Nachweis'],[
('60977 + 59649, Vorabtest A-C','Datum, Programmerzugang, Identitätsnachweis, Testergebnis: __________________'),
('Rote LoDi 511','Revision: ______; vorhandene Jumperstellung: ______; Innenlicht-AUX aus 8a: ______'),
('Zwei Befestigungsringe der LoDi 511','Ring A: ______; Ring B: ______; Freigabefoto/-messung nach 9: ______'),
('60941-Motor','Isolationsprotokoll 6b vollständig: ______; C90-Motortyp am 60977 rückgelesen: ______'),
('LoDi-514-Fronteinsätze','Vorn Weiß/Rot-Zweige bestätigt: ______; hinten R Weiß: ______; R Rot: ______; Belastbarkeit: ______'),
('Märklin-Träger mit ESU 59649','+Ub / LV / LR / B/GR / 0/GL und Steckindex abgeglichen: ______'),
('Lautsprecher aus 60977','Unverändertes Original: ______; Gegenstecker/Adapter: ______; Prüfung L1-L5: ______'),
('Mittelwagen','Anzahl: ______; je Wagen RT an O, GE an L, B leer; Prüfblätter 14a/14b: ______'),
('Gesamter Zug','Inbetriebnahme 52-56, Lastprüfung 57-59 und Gehäuseprüfung 24: ______'),
('60974 / Signalhalt','60974 bleibt bis eigenem Anschlussnachweis abgesteckt. CS3-Signalhalt separat nach 19 abnehmen.')],[2.5,4.0])
add('REV9 konkretisiert den vorhandenen Aufbau. Die elektrische Architektur bleibt unverändert: vorn 60977 auf LoDi 511, hinten 59649 auf Märklin-Träger, RT gemeinsam und GE nur vorn gespeist. Die eigentliche Identitätsübernahme sowie die unbekannten Revisionen werden nicht durch Formulierungen ersetzt.','small')
warn('Vor weiteren Arbeiten am ICE', 'Solange A-C nicht bestanden sind, nur den getrennten Decoder-Nachweis und die Fotos aus D beschaffen. Nach jedem späteren Wechsel einer Platine, Verdrahtung oder Decoderkonfiguration die davon betroffene Arbeitskarte erneut ausführen.')

page('Quellen und Geltungsbereich')
add('Herstellerquellen wurden mit dem vorhandenen REV5-Dokument und den ausdrücklich geteilten Zwischenberichten abgeglichen. Eigene Prüfschritte sind fachliche Ableitungen und keine wörtlichen Herstelleranweisungen. Vergleichsmodell 33701 ist nicht mit 2976 vollständig gleichgesetzt.')
add('Der frühere 60977-Direktlink lieferte HTTP 403. Der hier verwendete Ersatzlink wurde erneut geladen und per SHA-256 als identisch mit der geprüften Herstellerkopie bestätigt. S. 4/5/7 belegen Stecker, Pads und Einmessfahrt. Zusätzlich neue Bedienfolgen aus mDT3 S. 3 und CS3 S. 27 geprüft.','small')
for n in range(1,11):
    au,ti,meta,url=SOURCES[n]
    add(f'<b>{n}. {au}: {escape(ti)}</b><br/>{escape(meta)}. <a href="{escape(url,quote=True)}">Originalquelle</a>.','small')
page('Quellen, Bilder und Nachweisgrenzen')
for n in range(11,23):
    au,ti,meta,url=SOURCES[n]
    add(f'<b>{n}. {au}: {escape(ti)}</b><br/>{escape(meta)}. <a href="{escape(url,quote=True)}">Originalquelle</a>.','small')
add('Bildquellen: eigene bereitgestellte Fotos des Motors sowie image-2/4/5.jpg; LoDi-Vergleichsfotos 33701 aus den jeweils verlinkten Originalen; Märklin-Trägerzeichnung S. 5. Die Fotos wurden nicht generativ verändert. Nummern im PDF sind separate Vektormarkierungen. Einige früher zwischengespeicherte Webbilder waren nur Platzhalter und wurden nicht als Bildnachweis verwendet.','small')
warn('Verbindlicher Dokumentstatus','REV9 ist eine Prüffassung, nicht das Versprechen eines vollständig risikofreien Umbaus. Ohne G0, reale Platinenzuordnung und bestandene Einzelprüfungen keine Gesamtfreigabe. Keine erfundenen Messwerte, Hardwaretests oder vollständigen externen Konsilvoten sind in diesem Dokument enthalten.')

class ManualDoc(SimpleDocTemplate):
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and f.style.name=='h1':
            k='section-'+str(self.page); self.canv.bookmarkPage(k); self.canv.addOutlineEntry(f.getPlainText(),k,0,False)
def foot(c,doc):
    c.saveState(); c.setFont('A',8);c.setFillColor(MUTED)
    c.drawString(42,24,'REV9 - ICE 2976; konkrete Arbeitsfassung mit offenen Nachweisen')
    c.drawRightString(A4[0]-42,24,str(doc.page));c.restoreState()
