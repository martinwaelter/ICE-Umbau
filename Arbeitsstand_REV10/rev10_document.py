"""Document-wide sequencing and detailed workshop corrections for REV10."""
from copy import deepcopy
import re

COVERED={'R-12':'Zeitliche Prüftore, lose Fotos vor G0','R-13':'E1/E2/E3 getrennt','R-14':'Einzeltests mit lokaler Trennregel','R-15':'Laststufen vor erster Bestromung','R-17':'Nachprogrammierung physisch getrennt','R-19':'Wiederanschluss und Gehäuse','R-20':'Eindeutige Namen','R-21':'Wiederholung nach Reihungsänderung','R-26':'Kurzfolge Wagenprüfung','R-27':'Kurzfolge Einsetzen','R-28':'Kurzfolge Gehäuseabschluss','R-29':'Kapitel-/Schrittverweise','R-30':'Schwarz an PX/PM2','R-31':'Motoranschlussvoraussetzungen','R-32':'Richtungskorrektur','R-33':'Ungekuppelten Kopf vom Gleis','R-34':'Stromgrenze bei Toleranz','R-35':'Kein Kapazitäts-Nulltest','R-36':'Wagen-Speicherzustand','R-41':'Reset/Einmessfahrt/Puffer getrennt','R-43':'Bildrahmen und Navigation neu','R-44':'Versionsstatus separat','R-45':'Realer Kondensatorzustand bleibt nachzuweisen','R-47':'Kurzfassung mit echten Vorbedingungen'}

def P(t,style='body'):return {'type':'p','style':style,'text':t}
def T(headers,rows,widths=None):
    widths=widths or [1]*len(headers)
    return {'type':'table','widths':[511.28*x/sum(widths) for x in widths],'rows':[[P(x,'head') for x in headers]]+[[P(x,'cell') for x in row] for row in rows]}
def W(title,text):return {'type':'keep','items':[{'type':'table','widths':[511.28],'warning':True,'rows':[[P(title,'head')],[P(text,'warn')]]}]}
def walk(items):
    for e in items:
        if e['type']=='p':yield e
        yield from walk(e.get('items',[]))
        for row in e.get('rows',[]):yield from walk(row)
def section(ss,prefix):
    found=[s for s in ss if s['title'].startswith(prefix)]
    assert len(found)==1,(prefix,len(found));return found[0]
def replace(s,a,b):
    hit=0
    for e in walk(s['elements']):
        if a in e['text']:hit+=1;e['text']=e['text'].replace(a,b)
    assert hit,(s['title'],a)
def step(s,number,text):
    hit=[e for e in walk(s['elements']) if re.match(r'<b>'+re.escape(str(number))+r'\.',e['text'])]
    assert len(hit)==1,(s['title'],number);hit[0]['text']=text

def apply(ss):
    cover=ss[0]
    cover['title']='ICE 2976: Umbauanleitung REV10'
    cover['elements']=[P('<b>Vollständige bebilderte Arbeits- und Prüffassung mit CS3-CV-Kapitel</b>'),
        W('Dokument überarbeitet - reale Freigaben noch offen','Märklin 60977 und ESU 59649 sind an deinen Exemplaren noch nicht gemeinsam nachgewiesen. Vor Zugdemontage G0 aus A-C und den benötigten Teilen von F bestehen. Solange G0 offen ist, nur lose Teile und äußerlich zugänglichen Bestand dokumentieren. Bestromte Decoder-Nachweise ausschließlich in den bestätigten Prüfaufnahmen durchführen.'),
        P('Ziel: genau ein automatisch nutzbarer mfx-Zugeintrag, Märklin-Sound, Rot/Weiß an beiden Köpfen auch im Stand und unabhängig schaltbare Innenbeleuchtung. Zweiter Decoder ohne Zentralen-Traktion. Originale Märklin-Kupplungen; keine zusätzliche Längsader durch Mittelwagen. Kurze Anschlusslitzen bleiben nötig.'),
        T(['Zeitpunkt / Prüftor','Was vorher tatsächlich vorliegen muss'],[
            ('Vorbereitung, noch kein G1','Lose Artikel/Revisionen und Geräte erfassen: Kapitel 0/A/D. Keine Demontage für Montagefotos.'),
            ('G0: vor Zugumbau','A-C und erforderliche Teile F: Identität, Aktivierung, Firmware, geeignete Prüfaufnahmen, physische Lichtausgänge und neue SID tatsächlich nachgewiesen.'),
            ('G2: Motor vorbereiten','Nach G0 Kapitel 4-7, 5a/6a/6b und Bilder 21/22: Mechanik, Entstörung, Motor und vollständige Motorlitzen prüfen.'),
            ('G1: Montage freigeben','Jetzt revisionsbezogene Zuordnung 8/8a/9a, Halter 9/12c und Stromaufnahme-Identifikation aus 12d. Nur Identifikation/Freigabe, noch nicht sämtliche Anschlüsse aus 9a/12d oder Funktionstest L5. G1 setzt keine bereits angeschlossenen Motorlitzen voraus.'),
            ('G3: Verdrahtung prüfen','10-14e: LED-Ströme, Lichtmapping und gegenläufige LED-Farbverdrahtung nach 12a sowie jede Kupplung/Wagenplatine. Kapitel 16c/16d je Kopf ausfüllen.'),
            ('E1: vor Fahrzeug-Erststrom','Je Kopf Vorbedingungen in E1. Lastplan 18 vor erster Laststufe, Anlagenbereich 0a. Einsetzseiten 9c/12b erst an Schritt 52/54 ausführen.'),
            ('E2/E3 und G4: nach Tests','17/17a: zulässige offene Teststufen; 18/24: Last und geschlossenes Gehäuse. Erst nach bestandenen Ergebnissen G4 bestätigen.'),
            ('Getrennte spätere Aufgaben','Kapitel 15: 60974; Kapitel 19: Signalhalt. Beide vorhandenen 60974 bleiben jetzt unverbunden.')],[1.5,4]),
        P('G0/G1/G2/G3/G4 bleiben die bekannten Prüftor-Namen; ihre zeitliche Abhängigkeit steht hier ausdrücklich. Kapitelnummern dienen dem Nachschlagen, nicht als Erlaubnis zum Überspringen dieser Reihenfolge. Jede spätere Änderung entwertet die betroffenen Prüfungen. Frühere Fassungen nicht parallel als Bauanweisung verwenden.','small'),
        P('Stand 10.09.2026. Herstellerangabe, technische Ableitung und reale Messung werden getrennt. Die Berichtigung des Prüfberichts ist eingearbeitet; Prüfstatus und weiterhin offene Nachweise stehen in H. Eine fertige PDF ersetzt keinen Test am Fahrzeug.','small')]

    s=section(ss,'5. ')
    replace(s,'MOT_L und MOT_R an der LoDi 511 bleiben bis Ende Kapitel 6b unverbunden','MOT_L/MOT_R erst nach Motorprüfung 6b und bestätigter Padzuordnung 9a anschließen')
    replace(s,'bevor alle Messreihen aus 6a bestanden sind','bevor alle Messreihen aus 6a/6b einschließlich Drosseln/Litzen bestanden und die revisionsbezogenen Pads nach 9a bestätigt sind')
    s['elements'].insert(4,P('Dokumentiere zuerst den tatsächlich gelieferten Zustand des Motorschildes: Kondensator vorhanden ja/nein, beide Anschlussenden und Kennzeichnung. Der 60941-Beilage lässt sich kein allgemeiner Kondensatorwert entnehmen. Keine eigene Nachrüstung aus einer fehlenden Teilelistenposition ableiten; unklaren Zustand klären lassen.','small'))
    replace(section(ss,'6. '),'Schwarz bleibt ausschließlich bei den Isolationsmessungen 3 und 4 an PX; die Fahrzeugclips bleiben auch bei den Vor-/Nachproben fest.','Schwarz liegt in Zeilen 1, 3, 4 und 5 der Tabelle 6a an PX; in Zeilen 2 und 6 an PM2. Die Fahrzeugclips bleiben bei allen Vor-/Nachproben fest.')
    replace(section(ss,'6b. '),'Tatsächliche Motorleitungen erst nach G1/G2 nach dem bestätigten Anschlussplan wieder anschließen.','Tatsächliche Motorleitungen erst nach vollständig bestandener Motor-/Litzenprüfung 6b und bestätigter revisionsbezogener Padzuordnung 9a anschließen; Decoder weiterhin abgezogen. Die Montagefreigabe darf nicht bereits diesen noch ausstehenden Anschluss voraussetzen.')
    replace(section(ss,'11. '),'Die Widerstandstoleranz muss auch beim kleinsten tatsächlichen Widerstand eingehalten werden.','Die zulässige LED-Stromgrenze muss auch beim kleinsten tatsächlichen Widerstand eingehalten sein: Nennwert abzüglich Toleranz.')
    s=section(ss,'11a. ')
    replace(s,'nach 60/24','nach Schritt 60 und Kapitel 24')
    s['elements'].append(W('Helligkeit nachprogrammieren: beide Decoder trennen','Gesamten Zug stromlos machen, Dummy vom Kupplungsbus und anderen Kopf trennen. Für ESU-Änderungen nur den bestätigten Einzelaufbau am getrennten Programmierplatz verwenden; Puffer bleiben ab. Eine andere CS3-Lokadresse trennt keine Elektrik. Danach betroffene Licht-/Synchronisationstests und bei Leitungsänderung die Gehäuseprüfung wiederholen.'))
    s=section(ss,'12a. ')
    step(s,35,'<b>35. Stromlose Montagekontrolle.</b> Unbenutzte Leitungen einzeln isolieren; GE hinten nicht speisen. Drehgestellbewegung, Halter und vorbereiteten Gehäusefreiraum kontrollieren; Decoder bleibt abgezogen. Jetzt keinen Licht- oder Fahrtest beginnen. Die drei Lichtzustände erst nach E1 im Einzel-/Paartest Schritt 54 prüfen. Erste Motor-Kleinstfahrt nach Schritt 53; Fahrtest des zusammengebauten Zuges ausschließlich nach 17a/18 mit dafür zugelassener Last.')
    s['elements'].append(P('Eine nötige Mappingkorrektur aus Schritt 33 nur am stromlosen, vom Kupplungsbus und anderen Kopf getrennten ESU-Aufbau vorbereiten. Erst den bestätigten Einzelprogrammierplatz versorgen. Danach die betroffenen G0-/Lichtausgangstests erneut durchführen; keine Konfiguration am gemeinsamen Zug ändern.'))
    s=section(ss,'14b. ')
    step(s,'W1','<b>W1. Ausgangszustand vor Kupplungsanschluss.</b> Wagen vom Gleis nehmen und vollständig abkuppeln. Artikel/Revision und tatsächlich vorhandene Speicher erfassen. Angeschlossenen Speicher nur nach bestätigtem Trenn-/Restspannungsverfahren behandeln; nicht kurzschließen. Die weiße MT-37700 V4.3 bleibt bestückt. Beschrifte ihre Enden mit Ende 1 und Ende 2. Miss Pad L Ende 1 gegen Pad L Ende 2, danach Pad O Ende 1 gegen Pad O Ende 2. Kontakte positiv vor/nachprüfen; die beabsichtigten L-L-/O-O-Durchleitungen müssen stabil sein. L gegen O in beiden Polungen nur nach bestätigtem Messverfahren als Ausgangswert notieren. Dieser Vergleich allein beweist keine Fehlerfreiheit der Elektronik; zusätzlich 16d beachten. Bei unklarer Durchleitung noch nichts anlöten.')
    s['elements'].append(P('Nach Drehen, Umreihen, Kupplungs- oder Platinentausch vor dem Einschalten die betroffenen Einzelkontakt-/Padzuordnungen und die neue End-zu-End-Zuordnung erneut prüfen. Zugreihung und Endorientierungen im Protokoll festhalten. Zwei vertauschte Übergänge können sich beim bloßen Gesamtdurchgang verdecken. Am bestückten Gesamtzug keine pauschale GE-gegen-Masse-Ohmgrenze anwenden.'))
    s=section(ss,'14a. ')
    for e in walk(s['elements']):
        for a,b in [('RT-A','RT-Ende 1'),('RT-B','RT-Ende 2'),('GE-A','GE-Ende 1'),('GE-B','GE-Ende 2')]:e['text']=e['text'].replace(a,b)
    s=section(ss,'16b. ')
    replace(s,'Erst dann Wagen schrittweise nach 56 und ohne 60974 nach 17a testen. Die Belastung des konkreten LoDi-/Kupplungspfads wird zusätzlich nach 18 geprüft.','Vor jeder Laststufe deren Zulässigkeit nach Kapitel 18 festlegen; erst danach Wagen nach Schritt 56 und Kapitel 17a ohne 60974 testen. Lastmessungen erfolgen im dafür begrenzten bestätigten Prüfaufbau, nicht erst nach voller Belastung.')

    s=section(ss,'17. ')
    replace(s,'Vor Schritt 52: C-Protokoll, Motorprüfung und Anschlusskarten abhaken','Vor Schritt 52/54: E1 für den jeweiligen Kopf vollständig bestehen')
    replace(s,'G0 bestanden; Motorisolation einschließlich Kontakt-Gegenproben bestanden; reale Platinen-/Steckbelegung bestätigt; die jeweils angeschlossene LED-Strombegrenzung bestätigt. Nicht bestandene Baugruppen bleiben abgetrennt. Kein Dauer-Einschalten bei wiederholter Überlastmeldung.','G0 bestanden; Motorprüfung für den Motortriebkopf; tatsächliche Montage-/Steck- und LED-Freigaben. Kapitel 16c/16d und E1 für jeden Kopf ausfüllen. Lastplan 18 bestimmt bereits vor Erststrom die zulässige Teststufe. Kein gemeinsamer Test vor den passenden Einzelprüfungen. Nicht bestandene Baugruppen bleiben abgetrennt.')
    step(s,52,'<b>52. Motortriebkopf allein prüfen.</b> STOP, Fahrstufe 0, CS3-Automatik aus. Kopf vom Gleis nehmen, Dummy/Wagenbus und alle Versorgungen sowie beide 60974 physisch trennen. E1 vorn, Motorprüfung 6b, Lichtprüfung 16c/16d und erste Laststufe nach 18 bestanden? Hilfsleitungen entfernen; freie Anschluss-/Kupplungsenden einzeln isolieren. Erst jetzt 60977 gemäß 9c einsetzen. Danach den ganzen Kopf auf das getrennte Programmiergleis setzen und nach bestätigtem Märklin-Verfahren prüfen. Zum Wechsel auf das Betriebsgleis wieder stromlos machen. Dort bei stillstehendem Motor F0/Richtung und anschließend leisen Sound prüfen; noch keine Fahrt. Ein Ausleseerfolg ersetzt keine Isolationsprüfung.')
    step(s,53,'<b>53. Motor sehr langsam prüfen.</b> Nur nach bestandenem Schritt 52 und nach Kapitel 18 für diese Motorlast zugelassener Teststufe. Gleis waagerecht, mit freiem Fahrweg und gegen Absturz gesichert. Kleinste Fahrstufe kurz anlegen, dann auf 0. Räder nicht festhalten. Bei Brummen ohne Fahrt oder auffälliger Wärme sofort Versorgung aus. Bei falscher Richtung: STOP, Kopf vom Gleis, alles physisch trennen, Decoder abziehen. Bestätigte Motorzuordnung nach 9a korrigieren; danach vollständige betroffene Motor-/Litzenprüfung 6a/6b mit positiven Kontrollen wiederholen. Keine spontane Licht- oder CV-Invertierung als Ersatz. Bei Geruch/Überlast nicht erneut einschalten, Ursache fachkundig klären.')
    step(s,54,'<b>54. Motorlosen Kopf zuerst einzeln, dann gemeinsam prüfen.</b> Hinteren Schleifer und Radkontakt nach 12d bestätigen; ohne eigene Stromaufnahme kein ungekuppelter Test. STOP, Kopf vom Gleis nehmen, Bus/Versorgungen/Puffer vollständig trennen. E1 hinten, Halter 12c, LED-Ströme und 16c/16d bestanden? Hilfsleitungen entfernen, GE und alle unbenutzten Trägerlitzen einzeln isolieren. Erst jetzt 59649 nach 12b einsetzen. Zuerst am bestätigten Einzelprüfplatz Kommunikationsfähigkeit des motorlosen Aufbaus nachweisen. Bei Lesefehler nichts schreiben: Kontakt, Versorgung, Protokoll und Quittierung getrennt klären. Erst nach beiden Einzeltests beide Köpfe ungekuppelt auf dasselbe getrennte, aus genau einer Quelle gespeiste Gleis setzen. F0/Richtung am ICE bedienen, Farben nach 12a prüfen. Loklisten-Ausgangszustand vergleichen; eine alte Karte allein ist kein neuer aktiver Decoder. Bei eigenständig steuerbarem Slave Test abbrechen.')
    step(s,55,'<b>55. Versorgung unterbrechen und neu starten.</b> Beide Köpfe ungekuppelt lassen. Versorgung abschalten und physisch trennen; den motorlosen Kopf vom Gleis nehmen. Im unveränderten geprüften Aufbau wieder aufstellen und beide neu starten. Lichtzustände müssen stimmen. Dieser Handgriff unterbricht seine Versorgung; er trennt keine bereits offene Kupplung. Alte Einträge nur bei bekannter Adresse/Wirkung prüfen, nicht wahllos löschen oder umbenennen.')
    step(s,56,'<b>56. Nur freigegebene Wagenlasten ergänzen.</b> Vor dem ersten und jedem weiteren Wagen muss Kapitel 18 genau diese Laststufe mit Helligkeit, Einschaltspitze und Kupplungspfad zulassen; unbekannte Last erlaubt auch nicht automatisch einen Wagen. Vollständig abschalten und trennen, Wagen ankoppeln, Zuordnung nach 14a/14b und optional 14c-14e sowie Vor-Erststromzustand prüfen. Danach im bestätigten begrenzten Prüfaufbau einschalten. Standtest 17a ausführen. Bus nie unter Spannung stecken. Bei Fehler die letzte Änderung stromlos zurückverfolgen; ohne Ursache keinen weiteren Einschaltversuch.')
    s['elements'].append(P('G0 prüfte lose Decoder; E1 prüft das Fahrzeug vor Strom; E2 hält die erst jetzt entstehenden Ergebnisse fest. Diese drei Nachweise nicht gegenseitig ersetzen.','small'))
    replace(s,'Erst jetzt 60977 gemäß 9c einsetzen. Danach','Erst jetzt 60977 gemäß 9c einsetzen; tatsächlichen Sitz, vollständig eingeführte Stiftreihen und Freiraum kontrollieren, solange alles physisch getrennt ist. Danach')
    replace(s,'Erst jetzt 59649 nach 12b einsetzen. Zuerst','Erst jetzt 59649 nach 12b einsetzen; tatsächlichen Sitz, Stiftreihen und Freiraum vor jeder Bestromung kontrollieren. Zuerst')

    s=section(ss,'17a. ')
    s['elements'].insert(0,W('Nur die bereits zugelassene Laststufe testen','Kapitel 18 muss vor diesem Test Wagenzahl, Helligkeit, Einschaltspitzen und Grenzwerte des konkreten Strompfads abdecken. Bereits eingeschaltetes Licht ist Last. E1 und Schritte 52-55 müssen für die beteiligten Köpfe bestanden sein.'))
    s['elements'].append(P('<b>T9. Endgültige Funktionstastenmatrix:</b> Nach dem letzten Sound-/Mappingtransfer bei Fahrstufe 0 jede belegte Taste einzeln aus/ein schalten: beide Richtungen, F0 an und aus. Erwartete Wirkung auf Front vorn/hinten, Innenlicht und Sound vorher notieren; Ist daneben eintragen. Ungewolltes Licht bei F0 aus oder eine fremde Innenlichtreaktion ist ein Fehler. Motor gegen ungewollten Lauf absichern; Einmessfunktion ausgeschlossen. Projekt-/Mappingänderung verlangt erneute betroffene Tests auch ohne Firmwarewechsel.'))
    t9=s['elements'].pop()
    s['elements'].append(P('Danach die vollständige Funktionstastenmatrix T9 nach Kapitel 17b prüfen und protokollieren.','small'))
    ss.insert(ss.index(s)+1,{'title':'17b. Endgültige Funktionstastenmatrix T9','elements':[
        W('Nach letztem Projekttransfer, nur innerhalb zugelassener Last','T1-T8 nach 17a bestanden; Testaufbau gegen ungewollte Bewegung gesichert, Fahrstufe 0 und keine Einmessfunktion. Vor Beginn für jede Funktion festlegen, was sich ändern darf. Eine beabsichtigte Lichtfunktion ist kein Fehler; eine nicht vorgesehene Reaktion schon.'),t9,
        T(['Taste / Richtung / F0','Soll vorn / hinten / innen / Sound','Ist / Ergebnis'],[['________________','________________','________________']]*8),
        P('Für jede im endgültigen Projekt belegte Taste beide Richtungen und F0 an/aus getrennt erfassen. Dieses Blatt bei Bedarf kopieren. Projekt/Mapping/Firmware ______; zugelassene Laststufe ______; Datum/Prüfer ______.'),
        P('Bei Abweichung STOP und Versorgung physisch trennen. Ursache zuerst anhand der gesicherten Einzeldecoder-Zustände eingrenzen. Keine Mappingkorrektur am verbundenen Zug. Nach gezielter Änderung nur am bestätigten Einzelprogrammierplatz die betroffenen G0-/Lichttests erneut ausführen.') ]})

    s=section(ss,'18. ')
    s['elements'].insert(0,W('Dieses Kapitel vor Schritt 52 und vor jeder höheren Laststufe lesen','Die Nummer 18 ist eine Nachschlageposition, keine Erlaubnis zur vorgezogenen vollen Belastung. Zuerst Mess-/Begrenzungsverfahren festlegen, dann die ausdrücklich zugelassene Stufe in 17/17a prüfen. Ohne bekannten sicheren Prüfaufbau bleibt Bestromung der betreffenden Last gesperrt.'))
    step(s,57,'<b>57. Lastplan und Prüfgrenzen vor Erststrom festlegen.</b> Dem Fachprüfenden Schaltbild 14, Decoderartikel, reale LoDi-Revision, LED-Zweige und geplante Wagenzahl/Helligkeit geben. Für jede Stufe erst Anschlussplan, Messgerät, Messstellen, Überstrombegrenzung/Abbruchwerte und zulässige Bauteillasten dokumentieren. Separate Stufen: Kopf vorn im Stand; Motor-Kleinstfahrt; Kopf hinten; erster Wagen; weitere Wagen; endgültige Kombination; Einspeisung nur von hinten. Auch der erste Standtest braucht passende Begrenzung. Unbekannte Lastwerte zunächst im geeigneten geschützten Fachprüfaufbau bestimmen, nicht durch Probe am ungeschützten Decoder.')
    step(s,59,'<b>59. Nur nach bestätigtem Lastplan stufenweise messen.</b> Innenlichtausgang einzeln und die gleichzeitig aktiven Licht-/AUX-Lasten des 60977 zusammen bewerten. Hintere LEDs am 59649 gehören nicht zur 60977-AUX-Summe, beeinflussen aber die RT-Versorgung. Motor, Sound, Einschaltspitzen und höchste geplante Helligkeit berücksichtigen. Niedrigere Grenzen von Kupplung, Litze und LoDi-Platine gelten zusätzlich. Der Fachprüfende trennt für Einzel-Schleiferversorgung jeweils die bestätigte Zuleitung im stromlosen Aufbau und isoliert sie einzeln. Keine Leitung unter Spannung abziehen, kein Metall unter Schleifer legen. Nach Wiederanschluss vollständige betroffene Prüfungen wiederholen. Die zulässige Wagenzahl erst nach bestandenem endgültigem Last-/Spannungsabfalltest eintragen.')
    step(s,60,'<b>60. Gehäuseabschluss nach Kapitel 24.</b> Stromlos und vollständig getrennt beginnen, Decoder/Puffer abziehen. Passive geschlossene Prüfung mit positiven Kontrollen ausführen. Wieder öffnen, Hilfsleitungen entfernen und geplante Anschlüsse herstellen. Jetzt sämtliche durch Wiederanschluss betroffenen Soll-/Fremdpfade erneut nach 16c/16d und gegebenenfalls 6a prüfen. Bei Lageänderung die entsprechende Gehäuseprüfung wiederholen. Reale Halter-/Decoderhöhe, Dachfreiheit und Wärmeabfuhr dokumentieren; bloßer Seitenblick reicht bei verdeckten Stellen nicht. Decoder stromlos einsetzen, kontrolliert schließen, danach geschlossene Funktionsprüfung innerhalb der zugelassenen Last. E3 erst nach Bestehen ausfüllen.')
    s['elements'].append(T(['Stufe / Datum','Messplan / Grenze vorab','Ergebnis / zulässige Last'],[['________________','________________','________________']]*4))

    s=section(ss,'21. ')
    replace(s,'Am 60941 bleibt nur der Kondensator zwischen den beiden Bürstenfahnen','Nur tatsächlich vorhandenen und eindeutig zugeordneten Quer-Kondensator belassen')
    replace(s,'M1-M2: Kondensator belassen.','Bestätigter vorhandener M1-M2-Quer-Kondensator: belassen. Ist keiner vorhanden oder seine Eignung unklar, dokumentieren und klären; keinen Wert erfinden oder auf Verdacht nachrüsten.')
    s['elements'].append(P('Kein allgemeiner Kapazitäts-Nulltest: „keine nF-Anzeige“ ist ohne definierten Aufbau und Messgerät kein Prüfkriterium. Sicht-/Leitungsverfolgung und gültige Motor-Isolationsreihe sind verschiedene, beide notwendige Kontrollen.','small'))
    s=section(ss,'23. ')
    replace(s,'Gewindeträger rechts oben und links oben. Neue Platine zunächst ohne Decoder auflegen. Unterseite, Schraubenende, Ring und Nachbarlötstellen beobachten; dann wie Schritt 23 prüfen. Keine Halterhöhe aus dem Foto übernehmen.','Gewindeträger rechts oben und links oben trugen die alte Platine. Sie sind keine bestätigte Aufnahme für den kleinen Märklin-Träger. Keine Montage allein nach diesem Vergleichsfoto. Hintere Halterung nach Kapitel 12c mit realer Schraubenlänge, Unterseitenabstand und Dachfreiheit prüfen; die LoDi-Ringprüfung aus 9 gilt hier nicht.')
    s=section(ss,'24. ')
    replace(s,'ursprüngliche Anschlüsse gemäß geprüftem Plan herstellen. Decoder spannungsfrei einsetzen.','vorgesehene Anschlüsse gemäß geprüftem Plan herstellen. Alle dadurch betroffenen Soll-/Fremdpfade vollständig nach 16c/16d und bei Motorlitzen 6a/6b erneut prüfen, einschließlich positiver Kontrollen. Bei geänderter Endlage die entsprechende geschlossene Prüfung wiederholen. Decoder erst nach bestandener Nachprüfung spannungsfrei einsetzen.')
    s['elements'].append(P('Den tatsächlichen Freiraum mit eingesetztem Decoder anhand dokumentierter Halter-/Bauteilhöhen und Dachgeometrie nachweisen. Ein seitlicher Blick beweist keine verdeckte Berührungsfreiheit. Keine beliebige Folie/Schraube als Ersatz freigeben. Nach spannungslosem endgültigem Schließen folgt der geschlossene Funktionstest aus E3, nicht ein erneuter ungeprüfter Lötversuch.'))

    s=section(ss,'D. ')
    replace(s,'Foto 2: Haltepunkte','Foto 2: Haltepunkte - erst nach G0')
    replace(s,'LoDi an vorgesehener Position ohne Decoder;','Kein G0-Vorfoto: erst nach dessen Bestehen und erforderlichem Ausbau. LoDi an vorgesehener Position ohne Decoder;')
    # Move historical review discussion out of the work card.
    s['elements']=[el for el in s['elements'] if not (el['type']=='keep' and any('86 konsolidierten' in p['text'] for p in walk([el])))]
    s['elements'].insert(0,P('Vor G0 nur lose Teile und äußerlich zugängliche Merkmale fotografieren. Einbau-/Montagefotos erst nach G0 und dem dafür erforderlichen Arbeitsschritt. Für ein Foto weder unbekannte Steckteile abnehmen noch den Zug vorzeitig zerlegen.'))
    s['elements'].append(T(['Zusätzlicher realer Nachweis','Genau dokumentieren'],[
        ('Prüfgerät','Multimeterartikel, Anleitung, Ω-/Diodenprüfspannung und Prüfstrom; Messpunkte/Verfahren 16c/16d.'),
        ('Hintere Aufnahme','Schleifer, Anschluss, örtlicher Radkontakt und Chassisbezug nach 12d.'),
        ('Vorhandenes Zweitsystem','Artikel/Netzteil/Software der Gleisbox und Mobile Station; unabhängiger Betrieb und bestätigter SID-Datenzugang.')]))
    i=ss.index(section(ss,'E. '))
    ss[i:i+1]=completion_cards()
    s=section(ss,'Quellen und Geltungsbereich')
    s['elements'][0]=P('Diese REV10 beruht auf der vollständigen REV9 und dem korrigierten forensischen Bericht vom 10.09.2026. Herstellerbelege, Softwareimplementierungen und technische Ableitungen bleiben getrennt; Vergleichsmodell 33701 ist nicht in allen Teilen baugleich mit 2976. Reale Messungen und Gerätewerte sind nicht vorgetäuscht.')
    for s in ss:
        for e in walk(s['elements']):
            t=e['text']
            t=t.replace('vor 52/54','vor den Schritten 52/54').replace('in 42-44','in den Schritten 42-44')
            t=t.replace('nach 60/24','nach Schritt 60 und Kapitel 24')
            t=t.replace('Die vollständige externe Findingtabelle liegt noch nicht vor.','Prüfstand und verbleibende Nachweise siehe Kapitel H.')
            e['text']=t
    return ss

def completion_cards():
    return [
    {'title':'E1. Vor dem ersten Einschalten: je Kopf','elements':[
        W('Je Kopf vor Schritt 52 beziehungsweise 54 ausfüllen','Diese Karte enthält nur vorher erfüllbare Voraussetzungen. Noch nicht ausgeführte Funktions-, Last-End- und Gehäusetests stehen in E2/E3. Ein G0-Test an losen Prüfaufnahmen ist keine Fahrzeug-Erststromfreigabe.'),
        P('Kopf: Motor / motorlos ______; Datum / Prüfer ______; zugehörige Fotos und Originalprojekte/CV-Protokolle ______.'),
        T(['Voraussetzung','Konkreter Nachweis / Ergebnis'],[
            ('G0 mit 60977/59649','Identität, Firmware, Aktivierung, C-Protokoll einschließlich geänderter SID: ______'),
            ('Montage und Netze','LoDi-Revision/Jumper, SW/RT-Pfad, Ringe/Halter 9; hinten Halter 12c und Schleifer/Radkontakt 12d: ______'),
            ('Motor nur vorn','60941 richtig montiert; 5a/6a/6b mit Drosseln/Litzen; Motortyp nachgewiesen/rückgelesen: ______'),
            ('Frontlicht','LoDi-514-Zweige, zulässiger Strom/maximale Spannung; vordere Widerstände; hinten R Weiß/Rot, Toleranz/Leistung; Mapping 12a: ______'),
            ('Lautsprecher nur vorn','Original aus 60977, Impedanz; Gegenstecker/Adapter; L1-L4 elektrisch/mechanisch, noch kein Soundtest L5: ______'),
            ('Prüfkarten','16c und 16d mit Gerät, Endpunkten, Kontaktkontrollen und bestätigter Elektronikauswertung: ______'),
            ('Laststufe','Kapitel 18: welche erste Last, Mess-/Begrenzungsaufbau, Abbruchwerte; kein offener Grenzwert: ______'),
            ('Konfiguration','Projektstand, AUX 16a/16b, tatsächliche Adressen/Protokolle; keine Einmessfunktion; einzelne Decoder getrennt: ______'),
            ('Vor Einsetzen','Gleis/Bus/Versorgungen physisch getrennt; 60974 beide ab; Hilfsleitungen entfernt; freie Litzen jeweils isoliert; Indexzuordnung und geplante Lage 9c/12b bestätigt: ______. Tatsächlichen Sitz erst nach Einsetzen vor Bestromung prüfen.'),
            ('Prüfort','Kapitel 0a: getrenntes Gleis, genau eine Quelle; Fahrstufe 0, Automatik aus: ______')],[1.5,3.8]),
        P('Erst wenn alle für diesen Kopf erforderlichen Voraussetzungen eindeutig erfüllt sind, den zutreffenden Einzeltest beginnen. Nicht „n. a.“ eintragen, um einen unbekannten Pflichtnachweis zu umgehen. E1 bestätigt keine spätere höhere Last.') ]},
    {'title':'E2. Ergebnisse der offenen Funktionstests','elements':[
        P('Diese Ergebnisse entstehen erst nach E1 und während der zugelassenen Stufen 17/17a. Datum / endgültiger Projektstand ______.'),
        T(['Prüfung','Tatsächliches Ergebnis'],[
            ('52 / Motortriebkopf allein','Kommunikation, F0/Richtung im Stand, Lautsprecher L5/leiser Sound: ______'),
            ('53 / Kleinstfahrt','Laststufe vorab zugelassen; richtige Richtung; Mechanik; keine Auffälligkeit: ______'),
            ('54 / Dummy einzeln','Eigene Stromaufnahme, bestätigtes Quittier-/Leseverfahren; Ergebnis: ______'),
            ('54 / beide ungekuppelt','F0 aus dunkel; vorwärts Motor weiß/Dummy rot; rückwärts umgekehrt; kein Anrollen nötig: ______'),
            ('55 / Neustart','Versorgungsunterbrechung und Wiederanlauf; Loklisteneinträge/Wirkung dokumentiert: ______'),
            ('56 / Wagenstufen','Je Stufe: Wagen/Endorientierung, erlaubte Last, 14a/14b und optional 14c-14e: ______'),
            ('17a/17b / T1-T9','Innenlicht bleibt im Richtungswechsel/F0-Wechsel unverändert; Sound kein Reset; endgültige Funktionstastenmatrix: ______')]),
        P('Jede Funktionstaste einzeln notieren: Taste ______; Richtung ______; F0 ______; Soll vorn/hinten/innen/Sound ______; Ist ______. Blatt bei Bedarf kopieren. Änderungen am Projekt oder an Anschlüssen verlangen die betroffenen Wiederholungsprüfungen, nicht nur eine neue Unterschrift.') ]},
    {'title':'E3. Endabnahme von Last, Gehäuse und Bereich','elements':[
        P('Erst nach den tatsächlichen Prüfungen ausfüllen. Eine offene Zeile ist eine offene Endabnahme, kein Grund, bereits notwendige E2-Prüfungen vorzutäuschen.'),
        T(['Prüfung','Endgültiger Stand / Nachweis'],[
            ('Zugzusammenstellung','Wagenzahl, Reihenfolge/Endorientierung, LoDi-Revisionen; je Wagen RT an O, GE an L; B ohne Achskontakt frei: ______'),
            ('Optionaler Radkontakt','Wagen, Kontakt/B-Pad, Vorher-/Nachhermessung, Bewegungs- und Rückmeldetest 14c-14e: ______'),
            ('Last 18','Motor/Einzelausgänge/Licht+AUX/Gesamt; Kontakte/Leiterbahnen; Einschaltspitze; höchste Helligkeit; alleinige hintere Speisung: ______'),
            ('Gehäuse 24 / Schritt 60','Passive geschlossene Prüfung; Hilfsleitungen entfernt; wiederhergestellte Pfade vollständig erneut geprüft; realer Decoderfreiraum: ______'),
            ('Geschlossene Funktion','F0/Richtung, Sound, T1-T9; Helligkeitsvergleich 11a; freigegebene Fahrt: ______'),
            ('Anlagenbereich 0a','Quelle, freigegebene Strecke, gesperrte Grenzen; Signalhalt aus 19 noch offen / separat geprüft: ______'),
            ('Puffer','Beide 60974 weiterhin abgetrennt. Eine spätere Ergänzung benötigt eigenen Anschluss- und Betriebstest.'),
            ('G4','Ergebnis bestanden/offen/fehlgeschlagen ______; Umfang, Datum, Prüfer ______')]),
        W('Änderung bedeutet erneute betroffene Prüfung','Nach Umreihen, Drehen, Teiletausch, Nachlöten oder Konfigurationsänderung nicht mit der alten Freigabe weiterfahren. Betroffene elektrische, mechanische und funktionale Karten wiederholen. Neue Strecke und Signalautomatik gesondert abnehmen.') ]}]

def add_quickguide(ss):
    def S(n,title,text,refs):return P(f'<b>{n}. {title}</b> {text}<br/><font size="8">Detailkarten: '+', '.join(f'[[{r}]]' for r in refs)+'</font>','step')
    ss.extend([
    {'title':'H. Versionsstand und verbleibende Nachweise','elements':[
        P('REV10 vom 10.09.2026 übernimmt die Korrekturen des forensisch berichtigten Prüfberichts zu REV9. Alle 47 R-Befunde und 18 W-Verdachtsbefunde wurden dort behandelt. 8 bestätigt, 32 teilweise bestätigt, 6 offen, 1 nicht bestätigt sind Bewertungen des Berichts, keine 47 abgeschlossenen Fahrzeugreparaturen.'),
        P('Die Vollanleitung, Fotos/Schaltbilder, Programmierung und Schnellanleitung bleiben zusammen erhalten. Neu beziehungsweise wesentlich präzisiert: 0a, 12d, 16c/16d, Laststufen, E1-E3, Index-/SID-Nachweis und alle kritischen Übergänge. Frühere Originaldateien bleiben unverändert; die Änderungsmatrix liegt neben dieser PDF.'),
        T(['Noch offen','Was den Punkt tatsächlich schließt'],[
            ('G0 / Decoderpaar','Reale Identität/Übernahme, Aktivierung, Firmware, geeignete Lese-/Prüfaufnahmen, physisches Mapping und neue SID samt Funktionstest.'),
            ('LoDi / Montage','Beidseitige Fotos tatsächlicher Revision, Indexstruktur, Netze/Lastpfade und Befestigung. Unbekannte schwarze Struktur nicht abnehmen.'),
            ('Motorloser Kopf','Realer Schleifer und Radkontakt; montierbarer Märklin-Träger; konkrete Verbindungspunkte.'),
            ('LED / Messgerät','Bestätigte LoDi-514-Zweige und Grenzwerte; tatsächliches Multimeter und zulässige Elektronikmessung.'),
            ('Wagen / Betrieb','2976-Kupplungspassung, Last/Spannungsabfall, Reihung und sicherer Anlagenbereich.'),
            ('Spätere Erweiterung','Puffer und CS3-Signalhalt jeweils separat; kein automatischer Mitnachweis.')]),
        P('Es wurde kein Zug gemessen, kein Decoder programmiert, keine Herstelleranfrage versendet und nichts gekauft. Die KI-Gegenprüfung ist eine Dokumentprüfung, keine Prüfung durch drei menschliche Sachverständige. Die historische vollständige 86-Finding-Rohliste lag nicht vor; der konkret bereitgestellte 47-Befund-Bericht wurde abgeglichen.','small')]},
    {'title':'G.1. Schnellanleitung: Voraussetzungen und Aufbau','elements':[
        W('Kurzfassung erst nach den verlinkten Detailkarten benutzen','G0 ist noch offen. Diese Seiten sind eine Erinnerungshilfe, keine eigenständige Löt-/Programmierfreigabe. Erst die zugehörige Detailkarte lesen und erfüllen, dann den jeweiligen Kurzschritt durchführen.'),
        S(1,'Vorabnachweis und Bestand','60977/59649, CS3 und vorhandene Mobile Station/Gleisbox dokumentieren. G0 einschließlich Masterdaten, Aktivierung, Firmware, physischen Lichtausgängen und tatsächlich geänderter SID bestehen. Bis dahin Zug nicht zerlegen; nur lose Teile/äußerlich zugängliche Fotos. Kein automatischer Programmerkauf.',['A.','B.','C.','F.4.','F.5.','D.']),
        S(2,'Motor und vollständige Leitungen','Nach G0 Altzustand dokumentieren; 60941 passend montieren. Beide Anschlüsse vorhandener Kondensatoren verfolgen; keine Werte/Nachrüstung raten. Beide Drossel-/Litzenzweige aufbauen, von LoDi getrennt lassen. Sechs Messungen mit positiven Vor-/Nachkontrollen an allen geforderten Punkten/Lagen bestehen.',['4.','5.','5a.','6a.','6b.','21.','22.']),
        S(3,'LoDi zuordnen und befestigen','Tatsächliche Revision/Jumper, Netze, SW/RT-Pfad und Halterung bestätigen. Keine unbekannte schwarze Steckstruktur abnehmen. 60977 noch nicht einsetzen. Motorlitzen erst nach 6b plus 9a anschließen.',['8.','8a.','9.','9a.','9c.']),
        S(4,'Front und Lautsprecher','LoDi-514-Zweige und Strombegrenzung bestätigen. Hinten je eigener geprüfter Widerstand für Rot/Weiß; keine Beispielwerte ungeprüft übernehmen. Vorn bestätigte Frontpads und LS1/LS2; Original-Lautsprecherstecker über den nachgewiesenen Adapter erhalten.',['9b.','10.','11.','11a.'])]},
    {'title':'G.2. Schnellanleitung: Dummy und Mittelwagen','elements':[
        S(5,'Hinteren Kopf verdrahten','Schleifer/Radkontakt und Halter tatsächlich nachweisen. B/GR an den dokumentierten gemeinsamen hinteren Schleifer-/RT-Punkt, 0/GL an örtliche Radaufnahme. +Ub an LED-Plus; Rot über eigenen Widerstand an LV, Weiß über eigenen Widerstand an LR. GE hinten sowie MR/MV, unbenutzte AUX1-4, GND/+5V und übrige freie Litzen jeweils einzeln isolieren. 59649 bleibt abgezogen.',['12.','12a.','12c.','12d.']),
        S(6,'Jeden Wagen vor dem Löten prüfen','Passung originaler Kupplungskandidaten bestätigen. Speicherzustand klären. Weiße Leiste nach 14b-W1 vorprüfen; jeden Kontakt zur freien Litze nach W2 und jedes passive Kupplungspaar nach 14a prüfen. Optionalen Achskontakt nach 14c-14e separat prüfen/anschließen. Erst dann RT an O und GE an L; B nur für örtlichen Radkontakt, sonst frei. W4/W5 und End-zu-End-Zuordnung wiederholen.',['13.','14.','14a.','14b.','14c.','14d.','14e.']),
        S(7,'Konfiguration getrennt abschließen','Nach tatsächlich bestandenem G0 die geprüfte Synchronisation erhalten. Keine Konfiguration am gemeinsamen Zug ändern. 60971 nur für 60977, niemals 59649 aufstecken. Tatsächliche Protokolle/Adressen und letzten Projektstand sichern; Änderungen nur nach bestätigter Einzel-/Indexkarte mit Rücklesen. Danach betroffene G0-/Lichttests wiederholen. Innenlicht ohne Richtungsbedingung; elektrische AUX-Art gesondert prüfen.',['16.','16a.','16b.','F.6.','F.7.']),
        W('Drei getrennte Verbote','1. Keine Reset-Schreibbefehle an CV8 in diesem Arbeitsplan. 2. Keine Einmessfahrt: am 60977 nicht 77 in CV7/Firmwarefeld schreiben; am 59649 nicht CV54=0 mit anschließendem F1 kombinieren. 3. Beide 60974 bleiben jetzt abgetrennt; später höchstens einer vorn nach eigener Anschlussfreigabe.') ]},
    {'title':'G.3. Schnellanleitung: Einschalten und Abnehmen','elements':[
        S(8,'Motortriebkopf erstmals einschalten','Vorher 0a, Lastplan 18 und E1 vorn erfüllen; 16c/16d bestanden. STOP, Kopf vom Gleis, alle Versorgungen/Bus/Puffer physisch getrennt. Hilfsleitungen entfernen, freie Enden einzeln isolieren. Erst jetzt 60977 nach 9c einsetzen und Schritt 52 ausführen. Kleinstfahrt 53 nur in dafür zugelassener Laststufe.',['0a.','16c.','16d.','E1.','18.','17.']),
        S(9,'Dummy einzeln, dann beide Köpfe','E1 hinten einschließlich 12d und 16c/16d erfüllen. Stromlos und physisch getrennt 59649 nach 12b einsetzen. Erst passenden Einzeltest des motorlosen Aufbaus bestehen; Lesefehler nicht als Kurzschlussdiagnose behandeln. Dann beide ungekuppelt aus genau einer Quelle prüfen. Vorwärts bedeutet Motortriebkopf voraus: vorn Weiß/hinten Rot; rückwärts umgekehrt; F0 aus beide dunkel.',['12b.','12d.','E1.','17.','E2.']),
        S(10,'Wagenlicht und Last','Vor jedem Wagen die betreffende Laststufe nach 18 zulassen. Unbekannte Last erlaubt auch nicht einen Wagen. Vollständig stromlos ankoppeln und Zuordnung prüfen, danach T1-T9 ausführen. Richtungswechsel ausschließlich im Stand; Innenlicht bleibt unabhängig von F0/Richtung. Fahrtest und endgültige Wagenzahl erst nach den jeweiligen Lastnachweisen.',['14b.','17a.','17b.','18.','E2.']),
        S(11,'Gehäuse und Wiederanschluss','Abschalten, vollständig trennen, Decoder entfernen; passive Gehäuseprüfung 24 mit Kontaktkontrollen ausführen. Wieder öffnen, Hilfsleitungen entfernen, Anschlüsse herstellen. Sämtliche betroffenen Prüfungen erneut bestehen; bei Lageänderung geschlossene Prüfung wiederholen. Realen Decoderfreiraum bestätigen, stromlos einsetzen/schließen. Geschlossene Funktionsprüfung und E3.',['24.','16c.','16d.','E3.']),
        S(12,'Betriebsgrenzen einhalten','Nur im geprüften Versorgungsbereich fahren. Keine Booster-/Programmier-/elektrischen Bremsgrenzen über den gemeinsamen RT-Bus verbinden. Nach Umreihen, Drehen, Teile-/Konfigurationsänderung betroffene Prüfungen wiederholen. Signalhalt und Puffer bleiben eigene spätere Abnahmen.',['0a.','19.','15.','H.']) ]}])
