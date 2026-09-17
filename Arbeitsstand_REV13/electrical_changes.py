"""Electrical corrections against final REV12 numbering; remapping is done by root."""


def p(text):
    return {'type': 'p', 'text': text}


def step(number, text):
    return {'type': 'step', 'label': f'{number}.', 'text': text}


def note(text, label='STOPP', tone='stop'):
    return {'type': 'note', 'label': label, 'text': text, 'tone': tone}


def apply(P):
    # C1/C2 need not be a single parallel bank. Check every actual storage device.
    P[3]['blocks'][2]['text'] = 'Vom Gleis nehmen; Quellen und Wagenbus trennen, Decoder und beide 60974 entfernen. Jeden tatsächlich bestückten Wagenelko mit Wert/Nennspannung notieren. Leere C1/C2-Plätze benötigen keine Entladung. 60974 getrennt lassen; nicht öffnen.'
    P[3]['blocks'][3]['text'] = 'Je identifiziertem Wagenelko bis 470 µF / 35 V: COM/VΩ, V DC; Gerätefunktion vor/nachher an einer 1,5-V-Batterie prüfen. Direkt am Elko messen; über Nennspannung oder unbekannter Speicher: stoppen. Nachgemessene 10 kΩ ≥0,5 W mit isolierten Clips mindestens eine Minute direkt parallel anlegen. Spannung messen; Widerstand abnehmen, 10 s warten, nachmessen. Jeden Speicher einzeln behandeln und zum Schluss alle erneut prüfen. Erst zu Ω wechseln, wenn bei mindestens 0,01-V-Auflösung keine Restspannung angezeigt wird und das Gerätehandbuch es zulässt. Bei Rest-/wiederkehrender Spannung weiter entladen und Restquelle klären. Kein Drahtkurzschluss.'
    P[3]['blocks'][-1]['text'] = 'Eigene Rechnung für einen isolierten 470-µF-Elko: 35 V / 10 kΩ → 0,123 W; mit C +20 % und R +5 %: τ = 5,92 s. Weitere gekoppelte Speicher können länger nachladen: eine Minute ist kein Freigabekriterium. Entscheidend sind die Nachmessungen an allen Speichern.'
    P[3]['blocks'][-2]['text'] = '<b>Beschriften:</b> B, 0, M1, M2, U+, W/R (LED-Farbe) und GE sind Arbeitsnamen. Märklin-Orange kann U+, ESU/NEM-Orange Motor bedeuten: Anschlussziel und tatsächliche Farbe gemeinsam notieren.'

    # Restore a concrete stop while retaining the workable board inspection.
    P[5]['blocks'][1]['rows'][-1][1] = 'COM/VΩ, Ω; Spitzen-/Kontaktkontrolle vor/nachher. Direkter Leiter: stabiler Leitungswert ohne Bewegungsaussetzer. Ein bekannter Serienwiderstand wird gegen seinen Sollwert samt Toleranz beurteilt.'
    P[5]['blocks'][5]['text'] = 'Bestückte Querpfade nur ergänzend vergleichen: gleiches geeignetes Gerät, Bereich, Polung, Ausgangszustand und Verlauf. Kein fixes 5-Sekunden-Rezept; gleiche Werte beweisen keinen fehlerfreien Ausgangszustand. Bei unklarer Eignung auslassen. Die Anschluss-/Sichtprüfungen bleiben Pflicht.'
    P[5]['blocks'].insert(-1, note('Revision oder geplantes Kontakt-Pad-Paar nicht eindeutig zugänglich/zugeordnet: nur diese Verbindung und die davon abhängige Bestromung bleiben offen. Abdeckung: vorn, hinten und jeder Wagen nach obiger Tabelle; Motorisolation separat nach [[16]].'))

    # Manufacturer clarification is a real route; unverified 25 V/5 mA are not ratings.
    P[18]['before'] = '514-Revision und Plus/Weiß/Rot am eigenen Teil mit dem passenden Herstellerbild abgleichen. Keine LED direkt an Gleis oder Decoder anschließen.'
    P[18]['blocks'][0]['columns'][0][1]['text'] = 'LoDi: red / VCC / white.'
    P[18]['blocks'][0]['columns'][1][0]['text'] = '<b>Vorn:</b> Passende unveränderte LoDi-Frontkombination, R4/R5 erhalten. VCC an Plus, L_WS an Weiß, L_RT an Rot. Messung nach [[19]].'
    P[18]['blocks'][0]['columns'][1][1]['text'] = '<b>Hinten:</b> +Ub an Plus; Rot über R_Rot an LV, Weiß über R_Weiß an LR. Entweder Herstellerfreigabe genau dieser Kombination samt Widerständen oder Auslegung mit belegten Grenzdaten nach Tabelle.'
    P[18]['blocks'][2]['rows'][0] = ['Mindestwiderstand', 'Konservativ U_LED,min = 0 V: R_min ≥ U_max / I_zulässig. Strom in Ampere. Das kann hinten geringere Helligkeit ergeben.']
    P[18]['blocks'][2]['rows'][1] = ['Normwert / Toleranz', 'R_nom × (1 − Toleranz) ≥ R_min; nächstgrößeren Normwert wählen.']
    P[18]['blocks'][2]['rows'][2] = ['Belastbarkeit', 'P_max = U_max² / R_tatsächlich,min; mindestens Faktor 2 Reserve, Datenblatt/Einbautemperatur beachten.']
    P[18]['blocks'][3]['text'] = 'Daten fehlen: LoDi beidseitige 514-Fotos, Revision, 59649 und CS3-/Netzteiltyp nennen. Je Farbe zulässigen Strom, Polung/Zweigaufbau und geeignete Widerstände mit Versorgungshöchstwert erfragen. Alternativ eine dafür freigegebene komplette Frontbeschaltung bestätigen lassen. Antwort dem eigenen Teil zuordnen; Herstellerkontakt ist kein Händlerauftrag.'
    P[18]['blocks'][4]['text'] = 'Keine Ersatzfreigabe mit geratenen 25 V / 5 mA; ein DMM-Mittelwert belegt keine Spannungsspitze. Ohne Daten bleiben die drei hinteren LED-Adern einzeln isoliert. Mechanik, Motor- und hinterer Ruhetest dürfen weitergehen. R4/R5 nicht allein nach Aufdruck kopieren.'
    P[18]['blocks'][5]['text'] = 'Vor Löten Polung bestätigen. Diodentest nur bei belegter Prüfspannungs-/Stromeignung, Rot an Plus; OL ist kein Defektbeweis. Keine höhere Spannung oder unbekannte Sperrpolung. Widerstände einzeln nachmessen.'
    P[18]['sources'] = ['Q3', 'Q6', 'Q27']

    P[19]['before'] = 'Jetzt nur Messpunkte markieren. Ausführen erst beim Einzel-Ersttest [[35]]/[[36]], nach [[32]] und mit begründetem LED-Zweig [[18]]. DMM-Handbuch: passender Bereich, abgesicherter Stromeingang, Dauer und Gleichspannungsmessung; sonst Widerstands-Spannungsweg.'

    # Both legends are visible in the manufacturer page; explicitly choose the second.
    P[25]['title'] = 'Mittelwagen: Platine und Anschlüsse'
    P[25]['blocks'][-1]['text'] = 'LoDi-Standard: O = Radmasse, B = Mittelleiter. <b>Hier gilt die zweite Legende „Bei Verwendung der LoDi-Motor …“: O = Mittelleiter/RT, L = Licht/GE, B = Radmasse (optional)</b> [Q4]. Radkontakte beider Köpfe bleiben erhalten.'

    # Default B stays free. Optional live comparisons are only after assembly gates.
    P[28]['goal'] = 'Im Grundaufbau bleibt Wagen-B frei; LoDi erlaubt den Betrieb ohne Massefedern. Ein leitender Radsatz meldet Kontaktgleise bereits ohne B-Litze. Eine zusätzliche Feder braucht einen begründeten Zweck.'
    P[28]['before'] = 'Montagevorbereitung stromlos und abgekuppelt; Restenergie [[3]]. Eine B-Funktionsprobe findet erst begleitend zur ersten Wagenstufe [[37]] auf dem Prüfplatz [[45]] statt.'
    P[28]['blocks'][3]['text'] = 'B-Pad im passenden Revisionsbild von O/L unterscheiden. Die Tabelle dient nur dem optionalen geeigneten Elektronikvergleich nach [[5]], ohne pauschales OL-Soll. Federlitze zunächst einzeln isoliert lassen; O/RT und L/GE nach [[27]] prüfen.'
    P[28]['blocks'][4]['text'] = 'Später bei [[37]], falls B gewünscht: zuerst Innenlicht aus/ein mit freier B-Litze protokollieren. STOP, Quellen physisch trennen, Restenergie prüfen; erst dann positiv geprüfte Federlitze an B anschließen. Lötstelle/Beweglichkeit nach [[5]] prüfen. Danach dieselbe Lichtfolge und Lastmessung [[31]] wiederholen. Kein Clippen unter Spannung.'
    P[28]['blocks'][5]['text'] = 'Licht lässt sich mit B nicht mehr ausschalten oder Verhalten ändert sich unerklärt: STOP, trennen, B-Litze abnehmen und isolieren; Revision/Schaltung mit LoDi klären. Das ist ein Diagnosebefund, kein allgemein bewiesener B-Fehler. Zweiten Kontakt separat prüfen; B-B nicht voraussetzen. Von Hand rollen, Feder/Litze dürfen nicht klemmen.'
    P[28]['check'] = 'Für den Grundaufbau genügen Schritte 1–3 mit freier isolierter B-Litze. Schritte 4–5 sind die spätere optionale B-Funktionsprobe; Schritt 6 der noch spätere Rückmeldetest. Keiner davon ist Voraussetzung der ersten Wagenstufe ohne B.'

    # A DMM observation is useful but cannot provide undocumented peak margins.
    P[31]['goal'] = 'Die endgültige Wagenzahl braucht begründete Lastgrenzen. Das Multimeter ergänzt die Prüfung; ein DC-Mittelwert begrenzt keine Stromspitzen.'
    P[31]['before'] = 'Jetzt vorbereiten; ausführen begleitend ab [[37]], nach [[32]]–[[36]]. Prüfplatz [[45]] und für jede Fahrbewegung Bereich [[38]] geklärt. Konfiguration/Grenzen notieren; Änderungen nur vollständig stromlos.'
    P[31]['blocks'][1]['text'] = '<b>Nachweis 1 – Hersteller:</b> LoDi mit Revisionen, Fotos, Wagenzahl, CS3-/Netzteiltyp und 60977-AUX4 nach Dauer-/Einschaltstrom und zulässiger Konfiguration fragen. Antwort muss höchste Helligkeit, weitere Ausgänge und Leiterpfadgrenzen abdecken. Fehlende veröffentlichte Werte sind keine Freigabe.'
    P[31]['blocks'][2]['text'] = '<b>Nachweis 2 – Stromverlauf:</b> AC/DC-Stromsonde plus Speicheroszilloskop mit geeigneter mA-Auflösung, Bandbreite und Fehlerangabe verwenden. Um genau eine GE-Ader, ohne elektrischen Masseanschluss. Geeigneten Messplatz gezielt ausleihen; Gerätebezeichnungen und Kurven sichern.'
    P[31]['blocks'][3]['text'] = 'Sonde ohne Leiter nullen, nachher erneut kontrollieren. Einschalten ab dem ersten Strom mit Vortrigger erfassen; Licht aus/ein, höchste Helligkeit, beide Richtungen/Protokolle. Je weiterer Wagen dieselbe Reihe. Maßstäbe und Gerätefehler dokumentieren.'
    P[31]['blocks'][4]['text'] = 'Peak samt Unsicherheit ≤250 mA je verstärktem 60977-Ausgang; ohne Herstellerbeleg keine kurze Überlast erlauben. Obere gleichzeitige vordere Licht-/AUX-Werte zusammen ≤300 mA; hintere LEDs zählen hier nicht mit. RMS für Leitererwärmung berücksichtigen.'
    P[31]['blocks'][5]['text'] = 'Hintere Einspeisung allein: vordere Schleiferzuleitung stromlos öffnen, Enden isolieren. Im Stand alternativ sichere nichtleitende Schleiferauflage mit Kontaktkontrolle; für Fahrt Leitung wirklich trennen. Kein Papier unter fahrendem Schleifer.'
    P[31]['blocks'][6]['text'] = 'Sonde um hintere RT-Litze zur ersten Kupplung. Motor/Sound/Licht kontrolliert erfassen, Motor nie blockieren. RT-Spannungsfall entlang des Zuges nur differentiell prüfen; Leitergrenze, Kontaktunterbrechungen und Wärme beachten. Nach Wiederanschluss [[5]].'
    P[31]['blocks'].insert(-2, p('<b>Ergänzend mit deinem DMM:</b> Stromlos GE an zugänglicher Einzelader öffnen. Batteriebetriebenes DMM ohne USB/Netzverbindung, geeigneter abgesicherter DC-mA-Bereich: Rot wagenwärts, COM zum AUX; nur in Reihe. Höchste Helligkeit messen, ausschalten, Leitung wiederherstellen/prüfen, Rot zurück in V/Ω. Ergebnis ist ein Betriebs-Mittelwert; auch 40 % Reserve ersetzt keinen Peaknachweis.'))
    P[31]['blocks'][-2]['text'] = 'Kein geerdeter Oszilloskop-Masseclip an GE/RT. Shunt nur mit fachgerecht isolierter/differentieller Erfassung. Flackerfreiheit und DC-Mittelwert bestätigen keine Nenntragfähigkeit. Ohne Nachweis 1 oder 2 bleibt die numerische Lastabnahme offen.'
    P[31]['blocks'][-1]['text'] = 'Wagen/Reihenfolge ______; Nachweis/Geräte ______; GE Peak/RMS ______; ergänzender DMM-Mittelwert ______; Licht/AUX-Summe ______; RT-/Gesamtgrenze und Ist ______.'
    for block in P[31]['blocks']:
        block['after'] = 5

    P[38]['blocks'][3]['text'] = 'Je Signal/Modul Typ und Plan zuordnen. Nur bestätigter potentialfreier Schaltkontakt: sämtliche Anlagen-/Modulquellen physisch trennen, Klemmen fotografieren, die zwei Kontaktadern beschriften und am Kontakt abnehmen, freie Enden isolieren. Kontaktpunkte nach [[4]] vor/nachprüfen; Widerstand nur direkt am getrennten Kontakt messen. Keine Spannung zum Umschalten anlegen. Elektronik/unerreichbarer Kontakt: nach Herstellerplan klassifizieren oder Abschnitt unbekannt lassen.'

    # This methods card is intentionally called once during final assembly, not a loop.
    P[40]['title'] = 'Gehäuseprüfung: Sitzprobe und endgültiger Motorzweig'
    P[40]['goal'] = 'Zuerst den Messzugang vorbereiten. Die Endprüfung erfolgt nach dem endgültigen Schließen in [[41]] und verändert danach keine Innenleitung mehr.'
    P[40]['before'] = 'Alles vom Gleis/Bus, Puffer ab, Restenergie [[3]]. Motorzweig elektrisch von LoDi/Decoder trennbar. Zugangsentscheidung [[21]] und offene Sechserfolge [[16]] bestanden.'
    P[40]['blocks'][1]['text'] = '<b>Jetzt: Sitzprobe.</b> Hilfsleitungen PM1/PM2 nur motorseitig an freie Drossel-/Litzenenden, PX/PX2 an bestätigten Metallbezug. Vorhandene Öffnung und Zugentlastung fotografieren. Kein allgemeines OL durch LEDs oder bestückte Platinen. Im Gegenkopf nur tatsächlich passive Pfade prüfen.'
    P[40]['blocks'][2]['text'] = 'Gehäuse vollständig schließen, passende Schrauben anziehen und normale Drehgestelllagen prüfen; wieder öffnen. Keine Druck-/Scheuerspuren, verschobenen Clips oder eingeklemmten Adern. Ein halb offenes Gehäuse besteht die Probe nicht. Hilfsleitungen vor endgültiger Montage entfernen; weiter mit [[41]].'
    P[40]['blocks'][3]['text'] = '<b>Erst nach endgültigem Schließen auf [[41]]:</b> Versorgung getrennt lassen. Bereits montierte und zugentlastete Motor-Service-Trennstelle von außen öffnen. Der Motorzweig ist nun von LoDi/Decoder getrennt; Innenlitzen bleiben unverändert. PM1/PM2 an seine zugänglichen motorseitigen Kontakte, PX/PX2 an den bestätigten Metallbezug.'
    P[40]['blocks'][4]['label'] = 'MESSUMFANG'
    P[40]['blocks'][4]['text'] = 'Sechserfolge nach [[16]] an jeder zugänglichen Gegenstelle und normalen Drehgestelllage; Vor-/Nachproben zwingend. Bei geschlossenem Kopf nur ohne Eingriff erreichbare Rotorlagen prüfen; die vollständige Rotorreihe erfolgte offen. Prüfung bestätigt den endgültig verlegten Motorzweig, keinen pauschalen OL-Wert der angeschlossenen Decoderelektronik.'
    P[40]['blocks'][5]['text'] = 'Nach bestandener Reihe Messgerät entfernen und nur die äußere Serviceverbindung wieder stecken/sichern. Gehäuse und Innenlitzen nicht mehr öffnen/umlegen; dann Funktionsabschluss [[41]]. Bei Fehler oder nach erneutem Öffnen Ursache korrigieren, Endmontage und betroffene Reihe wiederholen.'
    P[40]['blocks'][-1]['text'] = 'Zugang/Fotos ______; Sitzprobe ______; endgültige Motorprüfung ______. Fehlt ein von außen bedienbarer geprüfter Zugang, bleibt diese Endprüfung offen; nicht durch einen Einschaltversuch ersetzen.'
    P[40]['check'] = 'Vor [[41]]: Sitz-/Zugangsprobe 1–2 bestanden. Bei [[41]] nach endgültigem Schließen: Schritte 3–4 bestanden, Serviceverbindung außen wiederhergestellt; danach nur noch Funktionsabschluss.'

    P[43]['blocks'][1]['text'] = '60974 ist für Märklin mLD3/mSD3 vorgesehen. Laut Anleitung gehört sein Stecker an die SUSI-Schnittstelle des Decoders; die weiße Buchse am 60974 führt den Bus weiter. Für den hier auf LoDi gesteckten 60977 muss der konkrete passende Anschluss anhand Revision und Kontaktansicht bestätigt werden. K1, S2 und Front-VCC sind keine bestätigten Pufferanschlüsse.'
    P[43]['blocks'][2]['text'] = 'Für eine spätere Ergänzung beide LoDi-Seiten/Revision, 60977-Firmware und unveränderten 60974-Stecker dokumentieren. Den zugänglichen SUSI-Anschluss dieser Kombination samt Kontaktansicht mit Märklin/LoDi bestätigen. Keine unbestätigte Trägerbuchse voraussetzen; Stecker nicht abschneiden.'
    P[43]['blocks'][3]['text'] = 'Nur einen passend angebundenen 60974 vorn am 60977, keinen am ESU und keine Kaskade. Firmwarebeleg [[8]] mindestens 3.2.0.1; CV7 nicht beschreiben. Lade-/Restenergie und Nachlauf festlegen; Motorpufferung anfangs aus. Danach Anschluss-, Last-, Neustart-/Halteprüfungen. Wagenlicht wird nicht automatisch gepuffert. Reset, Einmessfahrt und Pufferparameter sind getrennte Vorgänge.'
