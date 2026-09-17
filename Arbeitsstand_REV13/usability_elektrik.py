"""Small workshop-reading corrections against final REV13 pages 1–46."""


def apply(P):
    # Resistance calculations: define one consistent worst-case resistance.
    rows = P[20]['blocks'][2]['rows']
    rows[0] = ['Mindestwiderstand', 'U_max = belegte höchste Zweigspannung in V; I_zul = zulässiger Strom in A (mA ÷ 1000). Ohne LED-Spannungsabzug: R_min = U_max / I_zul.']
    rows[1] = ['Normwert / Toleranz', 'R_nom: Nennwert; t: Toleranz (5 % = 0,05). Normwert so wählen: R_unten = R_nom × (1 − t) ≥ R_min.']
    rows[2] = ['Belastbarkeit', 'P_max = U_max² / R_unten; Belastbarkeit bei Einbautemperatur ≥ 2 × P_max.']
    P[20]['blocks'][4]['text'] = 'Keine Werte raten; ein Multimeter-Mittelwert belegt keine Spannungsspitze. Ohne Daten die drei hinteren LED-Adern einzeln isolieren. Mechanik, Motor- und hinterer Ruhetest dürfen weitergehen. R4/R5 nicht allein nach Aufdruck kopieren.'
    P[20]['blocks'][5]['text'] = 'Polung vor Löten bestätigen. Diodentest nur bei belegter Prüfspannungs-/Stromeignung, Rot an Plus; OL beweist keinen Defekt. Keine höhere Spannung oder unbekannte Sperrpolung. Widerstände einzeln nachmessen; konservative Auslegung kann hinten dunkler sein.'

    # These are alternative measurements, not two mandatory successive operations.
    P[21]['before'] = 'Jetzt nur Messpunkte markieren. Erst bei [[36]]/[[37]], nach [[33]] und begründetem LED-Zweig [[20]] messen. Je Farbe <b>einen</b> Messweg wählen: Spannung nach 1, alternativ Strom nach 2. Gerätehandbuch: Bereich, Anschlüsse, Sicherung und zulässige Messdauer prüfen.'
    P[21]['blocks'][1]['text'] = '<b>Messweg Spannung:</b> Ohne Versorgung zugänglichen Serienwiderstand markieren. COM/VΩ, V DC (Gleichspannung). Isolierte Clips über dem Widerstand anbringen. Nur diese Farbe ungedimmt einschalten, Spannung U_R notieren; wieder ausschalten. Mit separat gemessenem R ergibt I_mittel = U_R/R. Clips entfernen. Die Strombuchse bleibt unbenutzt.'
    P[21]['blocks'][2]['text'] = '<b>Alternative Strommessung:</b> Stromlos vorn die Farbader zwischen LED und L_WS/L_RT öffnen, hinten zwischen Widerstand und LV/LR. Passenden abgesicherten Gleichstrombereich und Strombuchse laut Handbuch wählen. Rot zur LED-/Widerstandsseite, COM zur Platine; nur in Reihe. Farbe ungedimmt einschalten, Wert notieren, ausschalten. Gerät entfernen, Verbindung wiederherstellen; Rot zurück in V/Ω.'

    # Avoid repeating the complete post-solder inspection in the next numbered step.
    P[29]['blocks'][2]['text'] = 'RT-Litzen an O, GE-Litzen an L löten; flexibles Kabel mit Bewegungsschlaufe, keine zusätzliche Längsader. B bleibt frei. Nur bei geplanter Radkontaktoption [[30]]/1–3 vorbereiten; ihre Funktionsprobe 4–5 folgt bei [[40]]. Eine vorhandene lose Federlitze einzeln isolieren.'
    P[29]['blocks'][4]['text'] = 'Abweichung beim Prüfen: stromlos die zuletzt angeschlossene Litze abnehmen und einzeln prüfen; Lötstelle auf Brücke, Drahtfaden oder abgelöstes Pad untersuchen. Korrigieren und die betroffenen Prüfungen aus Schritt 3 wiederholen. Bestückte Querpfade bleiben nur der optionale Vergleich nach [[7]].'
    P[30]['before'] = 'Ohne Radkontaktoption: B frei lassen, vorhandene lose Federlitze isolieren; weiter mit [[31]]. Sonst jetzt nur Schritte 1–3 stromlos vorbereiten, Restenergie [[5]]. Funktionsprobe 4–5 später bei [[40]] auf dem Prüfplatz [[3]].'
    P[40]['before'] = 'Einzel-/Fronttests [[36]]/[[37]] bestanden; Wagen [[27]]–[[29]] passiv geprüft. B zunächst frei; nur bei gewählter Radkontaktoption [[30]]/1–3 vorbereitet. Bereich [[38]], Lastnachweis [[39]] vorbereitet. Betriebsausgang, Fahrstufe 0, Puffer ab. Optionale B-Probe 4–5 erst während dieser Wagenstufe.'

    # Explain measurement terms where they are actually used; restore disconnected feed.
    P[38]['blocks'][3]['text'] = 'Signal/Modul und Plan zuordnen. Kontakt laut Hersteller potentialfrei, also elektrisch von der Steuerelektronik getrennt: alle Quellen trennen, Klemmen fotografieren, Kontaktadern beschriften/abnehmen und isolieren. Kontaktpunkte nach [[6]] vor/nachprüfen; Ω direkt am getrennten Kontakt messen. Wert gilt nur für diese Stellung; nicht zum Umschalten bestromen. Nach Foto wiederanschließen und prüfen. Unbekannte Elektronik: Herstellerplan klären oder Bereich offen lassen.'
    P[39]['blocks'][3]['text'] = 'Beim Sondenweg: ohne Leiter nullen, nachher erneut kontrollieren. Einschalten mit Vortrigger erfassen, also mit aufgezeichnetem Vorlauf vor dem Stromanstieg. Licht aus/ein, höchste Helligkeit, beide Richtungen/Protokolle. Je weiterer Wagen dieselbe Reihe; Zeit-/Strommaßstab und Gerätefehler sichern.'
    P[39]['blocks'][4]['text'] = 'Spitzenwert (Peak) samt Messunsicherheit ≤250 mA je verstärktem 60977-Ausgang; keine unbelegte kurze Überlast. Obere gleichzeitige vordere Licht-/AUX-Werte zusammen ≤300 mA; hintere LEDs zählen hier nicht mit. Für Leitererwärmung den Effektivwert (RMS) berücksichtigen.'
    P[39]['blocks'][6]['text'] = 'Sonde um hintere RT-Litze zur ersten Kupplung. Motor/Sound/Licht kontrolliert erfassen, Motor nie blockieren. RT-Spannungsfall zwischen hinterem und vorderem Zugende nur differentiell messen; Leitergrenze, Unterbrechungen und Wärme beachten. Danach ausschalten, Sonde abnehmen, vordere Schleiferleitung wiederanschließen und nach [[7]] prüfen.'

    # The service connector is already open; do not ask to create this state again.
    P[42]['blocks'][3]['text'] = '<b>Erst nach endgültigem Schließen auf [[43]]:</b> Versorgung getrennt lassen. Prüfen, dass die außen zugängliche Motor-Service-Trennstelle weiterhin offen ist. Innenlitzen bleiben unverändert. PM1/PM2 an die motorseitigen Kontakte setzen, PX/PX2 an den bestätigten Metallbezug. Die andere Steckerhälfte zur LoDi bleibt getrennt.'
    P[43]['blocks'][0]['text'] = 'Motor-Serviceverbindung offen lassen. Am offenen Kopf Sechserfolge [[17]]/[[18]] wiederholen; <b>danach</b> Hilfsleitungen entfernen. Geplante Innenanschlüsse herstellen und [[6]]/[[7]] prüfen. Motor-/Platinenseite der äußeren Serviceverbindung markieren und getrennt lassen. Kein Motor-OL durch die Platine messen.'
