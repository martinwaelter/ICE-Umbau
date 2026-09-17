"""Elektrische Seiten der eigenständigen Anleitung; Eingabe finale REV13-Seiten 1–46."""
from copy import deepcopy

def apply(P):
    def page(n, **kw):
        p=P[n-1]
        p.update(kw)
    def step(n,text):return {'type':'step','label':str(n)+'.','text':text}
    def para(text):return {'type':'p','text':text}
    def note(label,text,tone='info'):return {'type':'note','label':label,'text':text,'tone':tone}
    def table(headers,rows,widths):return {'type':'table','headers':headers,'rows':rows,'widths':widths}
    def fig(kind,maxh):return {'type':'figure','kind':kind,'maxh':maxh}
    # Vorhandene fotografische Originalabbildungen erhalten.
    photos27=deepcopy(P[26]['blocks'][:4])
    photo20=deepcopy(P[19]['blocks'][0]['columns'][0])
    page(20,title='Beide Fronten: je Farbe ein eigener Widerstand',phase='Beleuchtung | konservativer Grundaufbau',
      goal='Ohne LoDi 511 entfallen R4/R5. Vier externe Widerstände begrenzen die zwei Farbzweige in beiden Köpfen.',
      before='Eigene 514-Revision und Anschlüsse mit dem Herstellerbild abgleichen. Betrieb dieser Auslegung nur bei belegter höchster Zweigspannung ≤24 V; CS3 und Netzteiltyp dokumentieren.',
      blocks=[{'type':'columns','widths':[0.8,2.2],'gap':16,'columns':[photo20,[
        para('<b>LoDi-Anschlüsse:</b> gemeinsames Plus = braun/orange, Weiß = grau, Rot = gelb [Q3]. Das braune Frontkabel ist hier kein Massekabel.'),
        para('<b>Je Kopf:</b> gemeinsames Plus an lokales Decoder-U+. Jede Farbe über einen eigenen 47-kΩ-Widerstand, 5 % oder besser, mindestens 0,25 W. Kein gemeinsamer Widerstand im Pluszweig.')]]},
        table(['Kopf / Decoderlicht','Verbindung'],[
          ['Vorn: LV / LR','LV → 47 kΩ → Weiß; LR → 47 kΩ → Rot'],
          ['Hinten: LV / LR','LV → 47 kΩ → Rot; LR → 47 kΩ → Weiß'],
          ['U+ beider Köpfe','Jeder Kopf versorgt nur seine eigene Front; Plusleitungen nicht miteinander oder mit Radmasse verbinden.']], [1,2.3]),
        note('EIGENE KONSERVATIVE AUSLEGUNG','47 kΩ ist unsere stromarme Grundbeschaltung, keine behauptete LoDi-Nennstromvorgabe. Sie kann deutlich dunkler leuchten. Ohne Abzug einer LED-Flussspannung gilt bei 24 V und 5 %: R_min = 44,65 kΩ; I_max ≤0,538 mA; P_max ≤12,9 mW.'),
        step(1,'Jeden Widerstand vor Einbau einzeln nachmessen; bei 5 % muss er zwischen 44,65 und 49,35 kΩ liegen. Keine aufgedruckte „473“ mit 4,7 kΩ verwechseln: 473 bedeutet 47 kΩ. Bauteilbeinchen und Lötstellen einzeln mit Schrumpfschlauch isolieren.'),
        step(2,'Die beiden Serienwiderstände je Kopf zugänglich befestigen, mit freier Kabellänge für die Sitzprobe. Front-Plus und Farbzuordnung vor dem Löten am passenden Originalbild bestätigen; keine unbekannte Sperrpolung ausprobieren.'),
        note('NICHT HELLER AUF VERDACHT','Ist das Licht zu dunkel, bleibt diese Beschaltung erhalten. Kleinere Widerstände erst mit belegtem zulässigem LED-Zweigstrom und Spannungshöchstwert auslegen: R_nom × (1−t) ≥ U_max / I_zul; Belastbarkeit mit Temperaturreserve prüfen. Ein DMM-Mittelwert ersetzt U_max nicht.','stop')],
      check='Vier separate 47-kΩ-Widerstände sind korrekt zugeordnet, nachgemessen und isoliert. Sicht-/Stromkontrolle bei den Einzeltests nach [[21]].',sources=['Q1','Q3','Q6'])
    page(21,title='Vier Frontzweige mit dem Multimeter prüfen',phase='Beleuchtung | während der Einzeltests',
      goal='Jede Farbe wird getrennt auf richtige Zuordnung, begrenzten Strom und brauchbare Helligkeit geprüft.',
      before='Jetzt Messpunkte vorbereiten; erst bei [[36]]/[[37]] nach [[33]] und der Beschaltung [[20]] einschalten. Motor steht. Multimeter: COM/VΩ und DC-Spannungsbereich; Strombuchse bleibt frei.',
      blocks=[fig('led_measure',135),
        step(1,'Je Farbe den zugänglichen externen Serienwiderstand markieren. Quellen entfernen, Speicher entladen. Isolierte Messclips an seine beiden Enden setzen. Keine Prüfspitze zwischen die 21MTC-Pins stecken.'),
        step(2,'Nur diese Farbe ungedimmt einschalten. Gleichspannung U_R am Widerstand ablesen; I_mittel = U_R / R_gemessen. Beispiel zur Bedienung: 18 V über 47 kΩ ergeben rund 0,383 mA. Das Beispiel ist kein Fahrzeugmesswert.'),
        step(3,'Ausschalten und physisch trennen, erst danach Clips umsetzen. Alle vier Farbzweige prüfen. Am gekoppelten Kopf-Test den gemeinsamen ICE-Eintrag bedienen. Vorn weiß/hinten rot bei Zug-Vorwärtsrichtung; umgekehrt bei Rückwärtsrichtung.'),
        table(['Kopf / Farbe','R gemessen','U_R / I_mittel','Lichtbild'],[
          ['Vorn Weiß','________','________','________'],['Vorn Rot','________','________','________'],
          ['Hinten Weiß','________','________','________'],['Hinten Rot','________','________','________']],[1,1,1.2,1]),
        note('BEWERTUNG','Bei der 47-kΩ-/24-V-Auslegung muss der beobachtete Strom ≤0,538 mA bleiben. Größerer Wert: sofort trennen; falschen Widerstand, Messbereich, Rechenfehler oder Versorgung untersuchen. Kleine Messwerte beweisen keine beliebige Spannungsspitzenfreiheit; die obere Begrenzung stammt aus [[20]].'),
        step(4,'Lichtfarbe, gleichmäßige Ausleuchtung und Helligkeit bei aufgesetztem Gehäuse beurteilen. Keine direkte LED-Verbindung herstellen, um die Helligkeit zu vergleichen. Nach Messung alle Clips entfernen; Leitungen und Widerstände dürfen beim Schließen nicht gequetscht werden.')],
      check='Alle vier Zweige sind protokolliert; Helligkeit der konservativen Beschaltung ist bewertet. Keine Messleitung bleibt am Fahrzeug.',sources=['Q1','Q3','Q6','Q27'])
    page(27,title='Mittelwagen: Standardbelegung ohne LoDi 511',
      goal='Die LoDi-Wagenplatinen bleiben. RT (B-Zug) führt Mittelleiter, GE (L-Zug) geschaltetes Licht; O bekommt örtliche Radmasse.',
      before='Wagen vollständig abkuppeln und vom Gleis nehmen. Speicher einzeln nach [[5]] behandeln. Neue Zuordnung ersetzt vollständig die bisherige LoDi-511-Belegung.',
      blocks=photos27+[
        step(1,'Ersten Wagen als Muster öffnen. Enden dauerhaft 1/2 nennen; Kupplungen, Federn und vorhandene Kabel fotografieren. Platine trocken einsetzen: Dach und Deichsel müssen ohne Druck oder Kabelzug beweglich bleiben.'),
        table(['LoDi-Standardpad [Q4]','Anschluss in dieser Anleitung'],[
          ['B an beiden Enden','RT: dauerhafter Mittelleiter vom vorderen Kopf'],
          ['L an beiden Enden','GE: über potentialfreien Relaiskontakt geschaltetes Licht'],
          ['O','Örtliche Radmassefeder; Vorbereitung und Prüfung nach [[30]]']],[1,2]),
        note('BELEG UND AUSLEGUNG','Q4 belegt L = Licht schalten, O = Radmasse, B = Mittelleiter. Die Versorgung von L über einen Relaiskontakt am Mittelleiter ist unsere daraus abgeleitete Schaltungsentscheidung. Sie wird zuerst am einzelnen Wagen nach [[40]] geprüft.'),
        step(2,'Kupplungspole nach [[28]] elektrisch zuordnen; die Farben allein genügen nicht. Danach [[29]] ausführen. SJ2/Türlicht zunächst unverändert lassen.'),
        note('ZUORDNUNG WECHSELT','Die frühere Belegung O = Mittelleiter und B = optionale Radmasse galt mit LoDi 511. Hier ist O Radmasse und B Mittelleiter. Entfernte Massefedern werden nach [[30]] wieder eingesetzt. Keine B–O-Brücke.','stop')],
      check='Wagenrevision, Padbelegung und Endorientierung sind erfasst. Noch nicht einschalten.',sources=['Q3','Q4'])
    page(29,title='Wagenkontakte vor und nach dem Löten prüfen',
      goal='B- und GE bleiben durchgängig; O bekommt einen zuverlässigen örtlichen Radkontakt.',
      before='Wagen allein, ohne Gleis/Bus, Speicher nach [[5]]. Passive Kupplungen [[28]] bestanden; Standardbelegung [[27]] lesen.',
      blocks=[table(['Vor Anschluss','Nach Anschluss'],[
        ['B Ende 1 ↔ B Ende 2','RT-Kontakt an jedem Ende → B; Längspfad erneut prüfen'],
        ['L Ende 1 ↔ L Ende 2','GE-Kontakt an jedem Ende → L; Längspfad erneut prüfen'],
        ['Kupplungslitzen einzeln zugeordnet','Jede Litze muss nur ihren zugehörigen Kontakt erreichen'],
        ['Radmassefeder separat geprüft','Freie Federlitze → O nach [[30]]']],[1.3,2]),
        step(1,'L-L und B-B zunächst positiv prüfen, mit Messleitungs-Kontrolle vor und nach jeder Reihe. Soll-Durchleitung stabil nahe dem eigenen Messleitungswiderstand. Bei unklarem Längspfad keine Litze anlöten.'),
        step(2,'RT an B und GE an L löten. Radmassefeder an O nach [[30]]. Kurze flexible Bewegungsschlaufen legen; keine Litze darf Rad oder scharfe Gehäusekante berühren. Farbmarkierungen RT/GE an beiden Enden ergänzen.'),
        step(3,'Lötstellen mit Lupe prüfen. Jeden wirklichen Kupplungskontakt bis zu seinem Pad kontrollieren, dann L-L und B-B wiederholen. Beide Deichselendlagen und mehrere Radstellungen prüfen.'),
        step(4,'Bestückte Querpfade B/O/L sind keine nackten Drähte: kein pauschales „OL“ verlangen. Optionale Elektronikvergleiche nur nach [[7]]. Bei Abweichung die zuletzt angeschlossene Litze stromlos abnehmen, Litze und Lötstelle getrennt untersuchen, korrigieren und nachprüfen.'),
        table(['Wagen / Revision','B-B / L-L','Kontakt-Pad / Bewegung','Radmasse → O'],[
          ['____________','______','____________','________'],['____________','______','____________','________'],['____________','______','____________','________']],[1.15,1,1.4,1]),
        note('STROMWEG','Der Motor wird örtlich im vorderen Kopf versorgt. Über RT fließen hinterer Decoder und Wagenversorgung; über GE das geschaltete Wagenlicht. Der hintere Schleifer bleibt elektrisch getrennt. Keine Prüfung mit alleiniger hinterer Einspeisung durchführen.')],
      check='B/L-Kontaktzuordnung und örtliche O-Radmasse jedes Wagens bestanden.',sources=['Q3','Q4'])
    page(30,title='Radmassefedern wieder einsetzen und an O anschließen',phase='Mittelwagen | Pflicht im Standardaufbau',
      goal='Ohne LoDi 511 braucht jeder Wagen im gewählten Dreileiteranschluss seine örtliche Radmasse.',
      before='Wagen abgekoppelt, vom Gleis und spannungsfrei; Speicher nach [[5]]. Eine Feder darf nur in ihre passende ursprüngliche Aufnahme zurück.',
      blocks=[step(1,'Feder, Befestigung und Litze mit dem eigenen Ausbauzustand vergleichen. Keine Achshalterung entfernen und nicht an die Achse löten. Fehlende Feder durch ein mechanisch passendes Teil für diesen Wagen ersetzen; Maße und Aufnahme vergleichen.'),
        step(2,'Feder zunächst getrennt von der Platine prüfen. Multimeter im Ohmbereich: Messspitzen kurzschließen und Eigenwert merken. Freie Federlitze gegen eine blanke berührte Achs-/Radfläche messen; stabil leitend in mehreren Radlagen. Bezugspunkt vorher/nachher positiv prüfen.'),
        step(3,'Leitende Achse und Federweg prüfen: kein Lack, Haftreifen oder Kunststoff als Bezug. Feder muss sicher berühren, ohne zu klemmen; einen schlechten Kontakt nicht durch starkes Verbiegen kaschieren.'),
        step(4,'Die positiv geprüfte Federlitze an <b>O</b> der LoDi-Wagenplatine löten. O anhand der tatsächlichen Padbeschriftung von B/L unterscheiden. B gehört jetzt zum Mittelleiter; eine Feder an B wäre falsch.'),
        step(5,'Lötstelle mit Lupe ansehen; Kontakt von Achse/Rad bis O erneut nachweisen. Räder drehen, Deichsel schwenken und Wagen von Hand rollen. Keine Litze darf an Rad oder Kupplung schleifen.'),
        table(['Wagen / Federtyp','Rad → freie Litze','Rad → O / Bewegung'],[
          ['________________','________','____________'],['________________','________','____________'],['________________','________','____________']],[1.4,1,1.3]),
        note('KEINE OPTIONALE B-PROBE','Die alte Abfolge „zuerst B frei, später Feder an B“ entfällt. In dieser Anleitung liegt Radmasse von Anfang an an O. Nach passiver Prüfung folgt der Einzelwagen-Lichttest [[40]].'),
        para('Späterer S88-Test: erst nach elektrischer Zugabnahme im geprüften Meldebereich frei–belegt–frei in beiden Orientierungen prüfen. Ein leitender Radsatz kann Kontaktgleise bereits ohne Feder melden; das ersetzt seine hier erforderliche elektrische Rückleitung zur Wagenplatine nicht.')],
      check='Jeder Wagen hat einen geprüften, leicht laufenden Radkontakt zu O. B und L sind unverändert den Kupplungsleitern zugeordnet.',sources=['Q4','Q8'])
    page(32,title='Wagenlicht über ein separates Relais schalten',phase='Schaltkarte | ohne LoDi-Motorplatine',
      goal='AUX1 schaltet nur die Relaisspule. Der potentialfreie Kontakt versorgt GE; Decoder-U+ gelangt nicht in die Kupplung.',
      before='Jetzt nur vorbereiten. Relais-Betriebstest erst nach [[33]], eingestecktem Decoder und bestandenem Ruhetest [[36]]. RT/GE nach [[27]]–[[30]] zuordnen; Bauraum samt Kabeln mit Schablone prüfen.',
      blocks=[fig('relay',155),
        para('<b>Hauptkandidat:</b> ML-Train 84002016 / mXion 0016, fertig mit Schutzdiode: 10–24 V, etwa 15 mA, Kontakt bis 2 A; ca. 32 × 15 × 15 mm [Q40/Q41]. Freier Bauraum samt Anschlüssen ist am eigenen Kopf zu prüfen.'),
        table(['Anschluss','Verbindung'],[
          ['Relais + / −','60977 U+ orange / AUX1 braun-rot'],
          ['Kontakt COM / NO','RT / GE; NC bleibt einzeln frei'],
          ['U+','Nur örtliche Front und Spuleneingang; kein Anschluss an Wagen oder Radmasse'],
          ['AUX1-Einstellung','Normal Ein/Aus, ungedimmt 100 %, keine Impuls-/Blinkfunktion']],[1,2.2]),
        note('ANSCHLUSSLAGE NACH Q41, S. 36','Bauteilseite ansehen, Zweierklemme oben: oben links = U+, oben rechts = AUX1. Dreierklemme unten: Mitte HRZ = COM → RT; links GL1 = Schließer → GE; rechts GL2 bleibt frei. Geliefertes Modul muss diesem Herstellerbild entsprechen. Schutzdiode richtig polen.'),
        step(1,'Relais zuerst allein am Decoder, Lastkontakt noch vollständig frei. DC-Spannung über +/− bei EIN prüfen: dokumentierter Bereich 10–24 V. Zentralen-/Netzteilunterlagen müssen den Betriebsbereich abdecken; kein beliebiger DMM-Mittelwert als Spitzengrenze.'),
        step(2,'Kontakt mit unabhängigem Batterie-Prüflämpchen über COM/NO testen: EIN leuchtet, AUS dunkel. Keine Ohmmessung am versorgten Fahrzeug. Danach alle Quellen trennen und den Batterieprüfkreis vollständig entfernen; erst dann COM/NO mit B-/GE verbinden.'),
        para('<b>60977:</b> Motor ≤1,1 A; Licht/AUX je ≤250 mA, gemeinsam ≤300 mA; gesamt ≤1,6 A. Relaisstrom zählt zur AUX-Summe, Wagenlichtstrom nicht. Kontakt-, Kupplungs- und Leitungsgrenzen separat einhalten.')],
      check='Vorbereitung abgeschlossen: weiter mit [[33]]. Erst während [[36]] die Relais-Prüfschritte dieser Karte ausführen; vor erstem Wagen müssen EIN/AUS und Anschlusszuordnung bestanden sein.',sources=['Q1','Q4','Q40','Q41'])
    page(39,title='Relaisversorgung und Wagenstufen prüfen',phase='Lastprüfung | ohne Messung am AUX-Wagenpfad',
      goal='Du prüfst reale Betriebszustände mit DMM und CS3. Der Wagenstrom ist durch den separaten Kontakt vom Decoderausgang getrennt.',
      before='Ausführen begleitend zu [[40]], nachdem [[33]]–[[37]] bestanden sind. Erst ohne zusätzliche Speicher; jede Änderung vollständig stromlos. Hinterer Schleifer bleibt getrennt.',
      blocks=[step(1,'Relaisprüfung [[32]] muss bestanden sein. Am Spuleneingang mit AUX1 EIN Gleichspannung prüfen: 10–24 V beim genannten Modul. Danach optional Spulenstrom in Reihe messen: Quellen trennen, geeigneten abgesicherten DC-Strombereich wählen, Leitung öffnen und Gerät einfügen. Nach Messung trennen, Originalverbindung wiederherstellen; rote Messleitung zurück nach V/Ω.'),
        note('MESSWERT EINORDNEN','Der Hersteller nennt etwa 15 mA für das Relaismodul. Das ist ein Erwartungswert, keine harte 15-mA-Grenze. Deutlich abweichender Wert, Schnarren oder Erwärmung: Anschluss/Versorgung untersuchen. 60977-AUX ≤250 mA und gesamte Licht-/AUX-Last ≤300 mA bleiben harte Decodergrenzen.'),
        step(2,'Erstwagen allein auf isolierender Unterlage, alle Räder fern von Gleis/Metall, keine weitere Kupplung: B an RT, L an GE. Den einzigen Rückweg O → Radmasse des vorderen Kopfes vorübergehend über 1 kΩ/2 W, 5 % führen. Bei belegter Gleisspannungsspitze ≤24 V sind so höchstens 25,3 mA möglich. EIN/AUS muss schon so eindeutig funktionieren; Dunkelheit allein beweist wegen Spannungsabfall keinen Fehler. Dann stromlos Prüfadern/Widerstand vollständig abbauen; erst nach diesem Erfolg den Wagen normal aufgleisen und [[40]] ausführen.'),
        step(3,'CS3-Gesamtstrom vor und nach jeder Wagenstufe bei gleichem Zustand protokollieren. Motor zunächst aus, Sound und Fronten zunächst gleich lassen; danach vorgesehene gleichzeitige Funktionen einschalten. Die Differenz dient der Diagnose und ist keine genaue einzelne Zweigmessung.'),
        note('DIGITALGLEIS IST KEIN DC-MESSPUNKT','Kein beliebiges DC-/AC-DMM in GE als vermeintlich genaue Lastmessung verwenden. Ein DMM-Mittelwert begrenzt keine Einschaltspitzen. Die frühere 250-mA-GE-Prüfung und die alleinige hintere Einspeisung entfallen: GE ist jetzt ein Relaiskontaktpfad, kein AUX-Ausgang; der Motor hängt nicht am Zugbus.'),
        step(4,'Während jeder Stufe auf flackernde Wagen, Relaisabfall, Decoder-Neustart und ungewöhnliche Erwärmung achten. Bei Fehler: STOP, Quellen entfernen, neu hinzugefügten Wagen abnehmen und Kontaktzuordnung/O-Radmasse prüfen. Nicht wiederholt einschalten, solange die Ursache offen ist.'),
        table(['Grenze / Kontrolle','Ergebnis'],[
          ['Kontakt ≤2 A; niedrigere Kupplungs-/Leitungsgrenze gilt','________'],
          ['Spule: U bei EIN / optional I','________'],
          ['Erstwagen mit 1-kΩ-Begrenzung bestanden / Wagenzahl','________'],
          ['Lichtschalten / Kontaktstabilität / Wärme','________']],[2.4,1]),
        para('LoDi beschreibt eine sanfte Ladeschaltung der Wagen. Nachgerüstete Speicher erst nach bestandener Grundstufe einzeln ergänzen; jede Erweiterung erneut prüfen. Flackerfreiheit und CS3-Anzeige sind Betriebsprüfungen, keine gemessene Bestätigung eines 2-A-Spitzenwertes.')],
      check='Jede dokumentierte Wagenstufe funktioniert stabil; der Decoder trägt nur Relais und örtliche Frontlasten. Keine pauschale numerische Spitzenstromfreigabe behaupten.',sources=['Q1','Q4','Q40','Q41'])
    old40=deepcopy(P[39]['blocks'])
    # Die bewährte achtteilige Funktionsfolge bleibt inhaltlich erhalten.
    tests=next(x for x in old40 if x['type']=='table')
    page(40,title='Wagenlicht: Standardanschluss T1 bis T8 prüfen',phase='Zugtest | stufenweise über Relais',
      goal='Jeder Wagen wird einzeln ergänzt; AUX1 betätigt das Relais, dessen Kontakt GE einschaltet.',
      before='Einzel-/Fronttests [[36]]/[[37]], Relais [[32]], passive Wagenprüfung und begrenzter Erstwagenversuch [[39]]/2 bestanden. B = Mittelleiter, O = Radmasse, L = geschaltetes Licht. Betriebsausgang, Fahrstufe 0, zunächst ohne zusätzliche Puffer.',
      blocks=[step(1,'STOP und Quellen physisch trennen. Nur den nächsten geprüften Wagen ankoppeln; Kontaktzuordnung kontrollieren. Freie Kupplungskontakte einzeln gegen zufällige Berührung sichern. Erst dann einschalten. Lastbeobachtung [[39]] je Stufe ausführen.'),tests,
        step(2,'Alle Wagen reagieren falsch: AUX1-Mapping und Relais-Ein/Aus prüfen. Relais schaltet, aber ein Wagen bleibt dunkel: B/L-Kontaktpfad und dessen O-Radmassefeder prüfen. Alle Wagen ab einer Kupplung betroffen: diesen Übergang separat untersuchen.'),
        note('ERSTER WAGEN IST DIE FUNKTIONSPROBE','Die Versorgung L = geschalteter Mittelleiter ist unsere aus der LoDi-Standardlegende abgeleitete Auslegung. Der erste eigene Wagen muss zuverlässig EIN/AUS folgen. Bei abweichendem Verhalten stromlos trennen, echte Revision/Belegung prüfen und keine weiteren Wagen hinzufügen. B/O nicht versuchsweise unter Spannung tauschen.'),
        note('PUFFER','Nachleuchten eines bereits eingebauten Speichers berücksichtigen. Keine weiteren Speicher gegen ungeklärtes Flackern ergänzen; zuerst Anschluss, Radkontakt, Relais und Versorgung untersuchen.','stop'),
        para('Wagenzahl/Reihenfolge ______; Endorientierung ______; AUX1/Taste ______; CS3-/Spulenwerte [[39]] ______; T1–T8 je Stufe ______. Während Standprüfungen Zug und Kontakte nicht berühren.')],
      check='Die vorgesehene Zusammenstellung besteht T1–T8. Danach langsamer Fahrtest [[41]] im geprüften Bereich [[38]] und abschließend geschlossen wiederholen.',sources=['Q1','Q4','Q10','Q40','Q41'])
    return P
