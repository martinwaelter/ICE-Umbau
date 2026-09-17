from pathlib import Path
ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parent

def p(t): return {'type':'p','text':t}
def small(t): return {'type':'small','text':t}
def step(n,t): return {'type':'step','label':str(n)+'.','text':t}
def note(t,label='STOPP',tone='stop'): return {'type':'note','text':t,'label':label,'tone':tone}
def apply(P):
 P[1]['blocks'][-2]=note('Vorhanden laut Nutzer: Multimeter, Märklin-Decoderprogrammer und CS3 mit aktueller Firmware. Am 12.09.2026 bestätigt: kein separates Prüfgleis. Deshalb Prüfabschnitt [[45]] aufbauen. Exakte Gerätetypen und Prüfaufnahmen [[6]] noch am tatsächlichen Bestand klären.','DEINE AUSSTATTUNG','info')
 P[11]['before']+=' Zum Lesen/Schreiben nur 59649 nach [[10]]/2–3 erneut am getrennten Programmiergleisausgang einrichten.'
 P[3]['blocks'][-1]['text']='Beispiel für einen isolierten 470-µF-Elko: P = (35 V)² / 10 kΩ = 0,123 W; mit C +20 % und R +5 %: τ = 5,92 s. Weitere Speicher können nachladen; entscheidend sind Nachmessungen an allen Speichern.'
 P[5]['check']='Bekannte Anschlüsse, eigene Leitungen, passive Pfade und Montage geprüft. Ersttest auf [[30]] planen; ausführen erst auf [[35]]/[[36]]. Motorisolation bleibt separat Pflicht.'
 P[45]['blocks'].insert(0,{'type':'figure','kind':'testtrack','maxh':108,'after':5})
 P[13]['sources']=list(dict.fromkeys(P[13]['sources']+['Q30']))
 P[16]['blocks'][2]['text']='Für Chassis, Motorrahmen, Radmasse und Schleifer getrennte Reihen. Arbeitsumfang dieser Anleitung: mindestens vier über eine Rotorumdrehung verteilte Stellungen, jeweils beide normalen Drehgestellendlagen. Je Lage die Sechserfolge an Bürsten und Litzenenden; Getriebe nicht erzwingen. Vier Stellungen sind eine festgelegte Stichprobe, kein Hersteller-Vollnachweis aller Winkel.'
 P[21]['blocks'][3]['text']='Vor Löten Messzugang [[40]] festlegen: außen bei geschlossenem Gehäuse zugängliche, zugentlastete Motor-Service-Trennstelle möglich? Ja: zweipolig, berührungssicher und passend zum Motorstrom ausführen; Anschlussseiten markieren. Nein: Zugang zuerst lösen, nicht als bestanden abzeichnen. Frontzweige nur nach [[18]]; freie Adern vor Löten nach [[4]] prüfen.'
 P[21]['blocks'][4]['text']='Jede Litze beschriften, Schrumpfschlauch vorher auffädeln, kurz abisolieren, bündeln/verzinnen und zugfrei löten. Nach Abkühlen Lupe: Zinnbrücken, Fäden, Lötperlen; festen Sitz prüfen. Kleine Bewegungsschlaufen frei halten. Anschluss-/Sichtprüfungen [[5]] wiederholen.'
 P[21]['check']='Leitungs- und Servicezugang dokumentiert; Anschlussprüfung bestanden. Freie Enden einzeln isoliert. Decoder erst auf [[33]] einsetzen.'
 P[22]['blocks'][2]['text']='Genau einen unveränderten Lautsprecher aus deinem 60977-Satz verwenden; Satzherkunft sichern. Er muss druckfrei passen. Herstellerleistung des 60977: 1,6 W an 8 Ω, 2,75 W an 4 Ω; dies bestimmt nicht die Impedanz deines Satzlautsprechers. Bei Ersatz gelten dessen Nennimpedanz und Belastbarkeit. Keine Impedanz aus einfachem Ohmwert erraten.'
 P[23]['blocks'][2]['text']='Träger, Halteplatte und beide hinteren LED-Widerstände trocken positionieren. Tatsächliche Bauform/Leistung aus [[18]] verwenden; keine pauschale 0,5-W-Vorgabe. Dachraum, Wärmeabstand zu Kunststoff/Litzen, freie Unterseite, Drehgestelle und Kupplungen prüfen. Widerstandskörper nicht einklemmen. Nichts bohren oder alte Metallstützen verbiegen.'
 for b in P[23]['blocks']:b['after']=5
 P[24]['before']='Halter [[23]] geklärt; Kontaktprüfung [[26]] jetzt vorziehen (Vorwärtsverweis). LED-Auslegung [[18]] belegt oder hintere LEDs getrennt/einzeln isoliert. Decoder/Puffer ab.'
 for b in P[27]['blocks']:
  if b.get('type')=='step' and b.get('label')=='2.':
   b['text']='RT-Litzen an O, GE-Litzen an L löten; flexibles Kabel mit Bewegungsschlaufe, keine zusätzliche Längsader. B bleibt frei: jetzt nur stromlose Vorbereitung [[28]]/1–3, Federlitze einzeln isolieren. Optionale B-Funktionsprobe [[28]]/4–5 erst bei der ersten Wagenstufe [[37]].'
  if 'Laststufe' in b.get('text',''):b['text']=b['text'].replace('[[30]]','[[31]]')
 P[27]['blocks'][-1]['text']=P[27]['blocks'][-1]['text'].replace('[[30]]','[[31]]')
 P[29]['blocks'][5]['text']+=' Reset, Einmessfahrt und Pufferparameter sind getrennte Vorgänge; keiner wird hier ausgelöst.'
 P[32]['blocks'][0]['rows'][8][0]='Getrennter Prüfabschnitt [[45]]; Einzel-Ersttest [[30]] vorbereitet, keine Wagen/Puffer'
 P[32]['blocks'][2]['text']='„Entfällt“ gilt nur für Motor und Lautsprecher des Gegenkopfs. Bei hinteren LEDs ist stattdessen ausdrücklich „getrennt/einzeln isoliert“ zulässig; Lichtabnahme bleibt offen. Jede andere fehlende Pflichtangabe sperrt den betroffenen Erststrom. Spätere Lastmessungen werden nicht vorweg als bestanden eingetragen.'
 P[37]['before']='Einzel-/Fronttests [[35]]/[[36]] bestanden; Wagen [[25]]–[[27]] passiv geprüft. B zunächst frei; nur Vorbereitung [[28]]/1–3 erfolgt. Bereich [[38]], begleitender Lastnachweis [[31]] vorbereitet. Betriebsausgang, Fahrstufe 0, Puffer ab. Optionale B-Probe [[28]]/4–5 erst während dieser Wagenstufe.'
 P[37]['goal']='Jeden Wagen zuerst passiv prüfen. Beim elektrischen Ergänzen die jeweilige Laststufe nach [[31]] begleiten; die endgültige Zusammenstellung vollständig testen.'
 P[37]['check']='Die vorgesehene Zusammenstellung besteht T1–T8 und Lastabnahme [[31]]. Im bereits geprüften Bereich [[38]] mit T9/Fahrtest [[39]] fortfahren.'
 P[39]['before']='T1–T8 und Lastabnahme [[31]] bestanden; Projekte dokumentiert. Nur Bereich [[38]] am Betriebsausgang; Fahrstufe 0, keine Einmessfunktion.'
 P[38]['blocks'][3]['text']='Signal/Modul und Plan zuordnen. Nur bestätigter potentialfreier Kontakt: alle Anlagen-/Modulquellen trennen, Klemmen fotografieren, zwei Kontaktadern beschriften/abnehmen und isolieren. Kontaktpunkte nach [[4]] vor/nachprüfen; Ω nur direkt am getrennten Kontakt. Wert gilt nur für diese Stellung; nicht zum Umschalten bestromen. Danach nach Foto wiederanschließen und prüfen. Unbekannte Elektronik: Herstellerplan klären oder Bereich offen lassen.'
 P[40]['before']='Vom Gleis/Bus nehmen, Decoder und Puffer herausnehmen, Motor-Serviceverbindung öffnen; Restenergie [[3]]. Zugangsentscheidung [[21]] und offene Sechserfolge [[16]] bestanden.'
 P[41]['before']='Sitz-/Zugangsprobe [[40]]/1–2 bestanden. Zug stromlos und vom Bus getrennt; die Motor-Service-Trennstelle ist außen erreichbar.'
 P[41]['blocks'][0]['text']='Hilfsleitungen entfernen; Motorlitzen noch von LoDi getrennt lassen. Sechserfolge [[15]]/[[16]] wiederholen. Geplante Innenanschlüsse herstellen und [[4]]/[[5]] prüfen. Außen zugängliche Motor-Service-Trennstelle offen lassen, ihre Motor-/Platinenseite markieren. Kein Motor-OL durch die Platine messen.'
 P[41]['blocks'][1]['text']='Innenverlauf, Halter und Zugentlastung fotografieren. Passende Decoder [[33]]/[[34]] einsetzen; reale Höhe, Dachraum und Wärmeabfuhr prüfen. Kein Decoder in Folie/Isolierband. Gefährdende Metallfläche isolieren und Abstand erhalten.'
 P[41]['blocks'][2]['text']='Gehäuse vollständig und druckfrei schließen. Jetzt Endprüfung [[40]]/3–4 am außen getrennten Motorpfad ausführen. Erst bei Erfolg außen wieder verbinden und Steckersitz/Isolation ansehen; nicht erneut öffnen oder innen umlegen. Bei jeder nötigen Innenänderung Schließen und Endprüfung wiederholen. Ein halb offenes Gehäuse ist keine Lösung.'
 P[41]['blocks'][3]['text']='Erst nach dieser Endprüfung innerhalb der geprüften Last F0/Richtung, Sound, T1–T9 und Fahrt am geschlossenen Zug wiederholen. Neuer Fehler: STOP und trennen. Nicht unter Spannung öffnen/drücken. Äußere Serviceverbindung gegen Lösen und Berührung sichern.'
 P[41]['blocks'][6]['text']='Nach Dimmung/Projektänderung betroffene Tests wiederholen. Für Zugang erneut geöffnet: Endmontage und Schließprüfung erneut ausführen, auch ohne bewusstes Umlegen. Strombegrenzung muss ungedimmt sicher sein.'
 P[42]['blocks'][0]['rows'][0][1]='Aufbau/letzte Änderung, Quellen-/Netzteilgrenze, RT/GE/0, 21MTC-Sitz und Metallkontakt'
 P[42]['blocks'][2]['text']+=' Die passende Aufnahme muss auch für spätere Änderungen erneut verfügbar sein.'
 # Edits to blocks written by other modules are keyed by content, not fragile indices.
 for b in P[35]['blocks']:
  if b.get('type')=='step' and b.get('label')=='3.':
   b['text']=b['text'].replace('Nach erneuter Ruhekontrolle bei Fahrstufe 0','STOP aufheben, erneut Ruhe prüfen; bei Fahrstufe 0')
  if 'CV51 Bit 0' in b.get('text',''):
   b['text']='Falsche Richtung: STOP, trennen. Zuerst Motorlitzen gegen [[21]] prüfen; Abweichung korrigieren und [[15]]/[[16]] wiederholen. Nur bei bestätigter Verdrahtung alternativ 60977 allein bearbeiten: CV51 Bit 0 „Motoranschluss tauschen“ mit gesichertem Altwert ändern, übrige Bits erhalten und rücklesen. Danach Richtung/Licht testen; keine zweite Umkehr über CV29/Licht.'
 P[35]['sources']=list(dict.fromkeys(P[35]['sources']+['Q10']))
 for b in P[36]['blocks']:
  if b.get('type')=='step' and b.get('label')=='2.':
   b['text']=b['text'].replace('Nach Ruhekontrolle STOP aufheben','STOP aufheben und zunächst in Ruhe beobachten')
 for b in P[30]['blocks']:
  if b.get('type')=='table' and any('60977' in str(x) for x in b.get('headers',[])):
   b['headers'][0]='60977: nur verstärkte Ausgänge'
