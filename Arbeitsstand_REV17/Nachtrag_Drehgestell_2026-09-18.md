# REV17 – Nachtrag: eingebautes Richtungsdrehgestell am motorlosen Kopf

**Stand: 18. September 2026.** Dieser Nachtrag aktualisiert den Fahrzeugbefund und konkretisiert die Abschnitte 2, 9, 10, 11 und 16 der [Grundanleitung](Anleitung_Grundumbau_60941_60972_LoDi514.md). Die übrigen Anforderungen bleiben unverändert: 60941 und ein 60972 im motorisierten Kopf; nur LoDi-514-Frontmodule; kein Sound; kein zweiter Decoder; keine neue elektrische Zugdurchleitung; vorhandenes Wagenlicht und U/O-Auswahl erhalten.

## 1. Neuer, tatsächlich erreichter Arbeitsstand

Der Nutzer hat die richtungsabhängige Drehgestellbaugruppe im motorlosen Kopf **bereits eingebaut**. Das neu bereitgestellte Foto zeigt die zusätzliche grüne Schalterplatine am nasenseitigen Drehgestell und drei freie Anschlusslitzen: grau, gelb und braun. Die lange Bestandsplatine 62762 und die alte klare Glühlampe sind weiterhin sichtbar.

Der Nutzer meldet folgende Durchgangsmessungen:

| Litze der neuen Schalterplatine | Berichteter Befund | Status |
|---|---|---|
| Grau | Durchgang zum Fahrgestell bei Bewegung nach links, vom Nutzer als vorwärts bezeichnet. | Vom Nutzer gemessene Schaltfunktion. |
| Gelb | Durchgang zum Fahrgestell bei Bewegung nach rechts, vom Nutzer als rückwärts bezeichnet. | Vom Nutzer gemessene Schaltfunktion. |
| Braun | Scheint die Masseleitung zu sein. | Vermutung; noch keine ausdrücklich berichtete Messung. |

**Die Aussagen der Grundanleitung, dass die Austauschbaugruppe noch nicht eingebaut und keine Richtungsbetätigung am eigenen Fahrzeug nachgewiesen sei, sind damit für dieses Exemplar überholt.** Es wird nicht erneut nach einem zu beschaffenden oder grundsätzlich passenden Drehgestell gesucht. Eine vollständige Abnahme bei montiertem Gehäuse und in Kurven ist davon zu unterscheiden.

Die grauen und gelben Leitungen werden nach dem Bericht richtungsabhängig mit dem Fahrgestell verbunden. Damit liegt ein konkreter Hinweis auf die masseschaltende Ausführung nach Abschnitt 11B vor. Ein potentialfreier Schalter nach Abschnitt 11A darf für den eingebauten Zustand nicht unterstellt werden. Noch zu bestätigen sind der dauerhafte Bezug des Fahrgestells zu Radkontakt 0, die Funktion der braunen Litze sowie die offenen Gegenstellungen.

Eine bestimmte Ersatzteilnummer oder innere Padbelegung wird aus dem Foto nicht zusätzlich behauptet. Alle Funktionsaussagen zum Nutzerexemplar beruhen auf dem neuen Nutzerbericht und dem Bild, nicht auf einer eigenen physischen Messung.

## 2. Richtung eindeutig benennen

In der quer betrachteten Aufnahme liegt die Nase links, die Kupplung rechts. Für die folgenden Zuordnungen zählen deshalb **Nase voraus** und **Kupplung voraus**, nicht eine unbestimmte globale Bezeichnung vorwärts/rückwärts:

| Bewegung des motorlosen Kopfes | Gemeldete aktive Litze | Gewünschtes Licht an dessen Nase |
|---|---|---|
| Nach links, Nase voraus | Grau | Weiß |
| Nach rechts, Kupplung voraus | Gelb | Rot |

Daraus folgt für die spätere Verdrahtung: **Grau steuert den white-Zweig, Gelb den red-Zweig, jeweils über einen eigenen Vorwiderstand.** Die Zuordnung folgt der gemessenen Bewegung, nicht allein der Kabelfarbe.

Die Grundanleitung definiert dagegen TK-A voraus, also den motorisierten Kopf voraus, als globale Vorwärtsrichtung. Bei einem normal zusammengestellten Zug ist der motorlose Kopf dann hinten und zeigt Rot. Lokale Bewegung mit der Nase des motorlosen Kopfes voraus darf daher nicht ungeprüft mit CS3-vorwärts gleichgesetzt werden.

## 3. Noch fehlende Messung: Braun und die Gegenstellungen

**Nur spannungslos messen.** Fahrzeug vollständig vom versorgten Gleis nehmen. Die drei neuen freien Litzen einzeln frei halten; ihre blanken Enden dürfen weder einander noch zufällig das Fahrgestell berühren. Die alte Glühlampe für diese Messreihe aus ihrer Fassung nehmen, damit nicht über ihren Glühfaden ein irreführender Messpfad entsteht. Die neue LED noch nicht anschließen. Kein Abkratzen von Leiterbahnen und kein erneuter Drehgestellausbau ist dafür vorgesehen.

Multimeter zunächst mit kurzgeschlossenen Messspitzen prüfen. Danach auf Widerstandsmessung beziehungsweise Durchgang umstellen. Metallfahrgestell und eine blanke leitende Radlauffläche separat als Bezug prüfen; Kunststoff oder Haftreifen sind keine geeigneten Messpunkte.

Nach kurzer Bewegung mit der Nase voraus anhalten und messen, danach nach Bewegung mit der Kupplung voraus wiederholen. Erwartung **zur Bestätigung der bisher nur vermuteten braunen Masse-/gemeinsamen Leitung**:

| Messung | Nach Bewegung Nase voraus | Nach Bewegung Kupplung voraus |
|---|---|---|
| Braun – blankes Metallfahrgestell | Niederohmig | Niederohmig |
| Braun – leitende Radlauffläche / geprüfter Radkontakt 0 | Niederohmig | Niederohmig |
| Grau – Braun | Niederohmig | Offen |
| Gelb – Braun | Offen | Niederohmig |

Niederohmig bedeutet hier nahe am Wert der kurzgeschlossenen Messspitzen und stabil, nicht lediglich irgendein Piepton über einen anderen Verbraucher. Offen bedeutet kein dauerhafter leitender Pfad; Messwert möglichst mit angeben. Die gemeldeten aktiven Grau-/Gelb-Stellungen müssen nicht als unbekannt behandelt werden; diese Tabelle ergänzt insbesondere die fehlenden Gegenstellungen und Braun.

Zusätzlich prüfen, dass Braun nicht direkt mit dem Mittelschleifer oder einem U/O-Versorgungseingang verbunden ist. Bei noch angeschlossenen anderen Verbrauchern deren Messpfade berücksichtigen, statt jeden endlichen Widerstand als Kurzschluss zu interpretieren. Falls Braun von Fahrgestell/0 getrennt bleibt, es nicht auf Verdacht dort anlöten: zunächst seine Verbindungen zu Grau und Gelb in beiden Stellungen aufnehmen.

Die Messung im Stillstand nach jeder Bewegung prüft zugleich, ob der Schalter die letzte Stellung hält. Eine feste Umschaltstrecke oder garantierte Haltefunktion wurde vom Nutzer noch nicht ausdrücklich bestätigt.

## 4. Anschlussplan nach bestätigter Masseschaltung

**Dieser Anschlussplan konkretisiert den eigenen Schaltungsentwurf 11B der Grundanleitung. Noch keine Freigabe zum Einschalten, solange Braun/0, die Versorgung und die LED-Anschlüsse nicht eindeutig sind.** Die Herstellerquellen belegen LED-Anschlüsse, fehlende Vorwiderstände und Diodendaten, nicht einen von Märklin oder LoDi freigegebenen Gesamtumbau dieser Schaltung.

Bezeichnungen: S-B ist der durchgemessene gemeinsame Ausgang der örtlichen U/O-Auswahl im motorlosen Kopf. Er führt je nach Stellung die Schleifer- oder Pantographenversorgung. S-B ist nicht der Name einer ungeprüften farbigen Litze. Radkontakt 0 bleibt der örtliche Rückleiter.

| Anschluss | Verbindung |
|---|---|
| S-B, Ausgang der örtlichen U/O-Wahl | Anode, also Seite ohne Ring, von D0. |
| Kathode von D0, Seite mit Ring | VCC des LoDi-514-Moduls. |
| white des LoDi-Moduls | Über R-W zur **neuen grauen** Drehgestelllitze. |
| red des LoDi-Moduls | Über R-R zur **neuen gelben** Drehgestelllitze. |
| Neue braune Drehgestelllitze | Nach Bestätigung an den geprüften örtlichen Rad-/Masseanschluss 0; eine vorhandene dauerhafte Verbindung dorthin bleibt erhalten. |

```text
U/O-Ausgang S-B ---- D0 (Ring zur LED) ---- LoDi VCC

LoDi white ---- R-W ---- neue GRAUE Litze
LoDi red ------ R-R ---- neue GELBE Litze

Geprüfter Radkontakt 0 -- neue BRAUNE Litze
                         [nur nach Bestätigung ihrer Funktion]
```

**Zum vollständigen Plan gehören außerdem zwei Schutzdioden:**

| Diode | Anode / Seite ohne Ring | Kathode / Seite mit Ring |
|---|---|---|
| D0: Versorgung | S-B | VCC |
| D-W: Schutz des weißen Zweiges | white, auf der LED-Seite von R-W | VCC |
| D-R: Schutz des roten Zweiges | red, auf der LED-Seite von R-R | VCC |

Alle drei Dioden: 1N4148. Bei dieser Bauform kennzeichnet der Ring die Kathode. [Q3] Die Schutzdioden liegen entgegen der LED-Durchlassrichtung zwischen Farbanschluss und VCC, nicht parallel zum Vorwiderstand. Ihre Aufgabe ist die Begrenzung einer umgekehrten Spannung an den LED-Zweigen. Die Konstruktion benötigt keine zusätzliche LoDi-Platine; diskrete Bauteile werden vollständig isoliert montiert.

R-W und R-R bleiben zunächst **je 47 kOhm / 0,25 W / 5 % oder besser** als bereits dokumentierte stromarme Prüfbestückung. Für höchstens 24 V am Lichtkreis begrenzt der kleinste Widerstandswert von 44,65 kOhm den Strom selbst ohne LED-/Diodenspannungsabzug auf höchstens etwa 0,54 mA während der leitenden Polarität. Das ist eine eigene Rechnung, keine Hersteller-Nennbestückung. Die reale Versorgung muss diese Spannungsannahme einhalten. Endgültige Helligkeit und zulässiger höherer LED-Zweigstrom bleiben offen. Die angebotenen ICE-1-Frontmodule enthalten keine Vorwiderstände. [Q1]

Die Schaltung nutzt nur eine Polarität der Digitalspannung. Sie liefert deshalb keine Zusage identischer Helligkeit zum vorderen Decoderlicht oder vollständiger Flackerfreiheit. Ein Pufferkondensator ist hier nicht vorgesehen. Bei Änderungen ist eine neue Auslegung nötig; keinen beliebigen Kondensator oder Brückengleichrichter ergänzen.

## 5. Verwechslungen am gezeigten Fahrzeug vermeiden

**Neue und alte gelbe Leitung unterscheiden:** Gemeint ist die freie gelbe Litze an der neuen kleinen grünen Schalterplatine. Die noch vorhandene gelbe Leitung zwischen alter Lampe und langer Platine ist ein anderer Strompfad. Sie darf nicht allein wegen gleicher Farbe mit der neuen gelben Litze verbunden werden. Auch die beiden braunen Leitungen sind nicht ohne Messung gleichzusetzen.

**Braun am Richtungsschalter ist kein LED-Plus:** Im LoDi-Herstellerbeispiel werden für den LED-Plusanschluss unter anderem braune beziehungsweise orange Leitungen verwendet. [Q2] Das ist keine Freigabe, die hier als Masse vermutete neue braune Drehgestelllitze an VCC zu löten. Funktionen und gemessene Netze haben Vorrang vor Farben.

**Keine Verbindung zum 60972 herstellen:** Die neuen grauen/gelben Schalterleitungen bleiben im motorlosen Kopf. Sie werden weder mit den gleichfarbigen 60972-Ausgängen noch mit dessen orangefarbenem Decoderplus verbunden. Der gewünschte unabhängige Aufbau braucht diese Zugverbindung nicht.

**Keine massereferenzierte Brücke kurzschließen:** Wenn ein Wechselspannungseingang einer Gleichrichterbrücke bereits an Radkontakt 0 liegt, darf ihr Minusausgang nicht zusätzlich über den Richtungsschalter oder direkt an dasselbe Fahrgestell/0 gelegt werden. In einer Polarität würde so eine Brückendiode einen Kurzschlusspfad bilden. Deshalb ist die potentialfreie Variante 11A für die berichtete direkte Fahrgestellumschaltung nicht einfach übertragbar. Dies ist eine Folgerung aus der Schaltung, kein pauschales Verbot jeder anders ausgelegten Brückenschaltung.

**U/O erhalten:** S-B vor dem Anschluss durchmessen. Die neue LED-Versorgung kommt hinter die vorhandene Quellenwahl, nicht automatisch direkt an den Schleifer. Das neue Foto und die Richtungsmessungen klären die U/O-Padbelegung nicht. An der langen Platine 62762 ist aufgrund dieses Nachtrags kein Leiterbahnschnitt vorgesehen.

## 6. Aktualisierte offene Punkte und Abnahme

| Punkt | Neuer Stand |
|---|---|
| Drehgestell beschaffen und montieren | Erledigt laut Nutzerbericht und neuem Foto. Keine erneute Beschaffung verlangt. |
| Radbewegung erzeugt unterschiedliche Schaltzustände | Für die aktiven Grau-/Gelb-Stellungen durch Nutzerbericht belegt. |
| Farbe für die beiden Bewegungsrichtungen | Grau zum weißen Zweig, Gelb zum roten Zweig, bezogen auf Nase/Kupplung des motorlosen Kopfes. |
| Dauerhafte braune Masse-/gemeinsame Leitung | Noch zu messen, nicht als gesichert dokumentiert. |
| Gegenseitige Ausschaltung und Halten im Stand | Gezielt bestätigen. |
| U/O-Versorgungspunkt S-B | Noch am eigenen Versorgungspfad zuzuordnen. |
| LED-Widerstände für endgültige Helligkeit | Noch offen; 47 kOhm bleibt Prüfbestückung. |
| Vollständiger elektrischer Aufbau und Betriebsabnahme | Noch nicht durchgeführt beziehungsweise nicht berichtet. |

Nach erfolgreicher Kontakt- und Versorgungsprüfung zuerst den motorlosen Kopf allein auf einem abgesicherten, getrennten Prüfabschnitt in U-Stellung testen. Es darf nur der für die tatsächliche Bewegung vorgesehene Farbzweig leuchten. Bei Kurzschlussmeldung oder unerwarteter Erwärmung sofort abschalten. Danach mit montiertem Gehäuse freies Rollen und Schwenken prüfen.

Die bekannte Systemgrenze bleibt: Der mechanische Schalter erhält keinen CS3-Richtungsbefehl und keine F0-Information. Er reagiert auf Radbewegung. Ohne zusätzlichen Steuerweg bleibt das örtliche hintere Licht unabhängig von F0 des vorderen Decoders. Ein zweiter Decoder, eine CS3-Traktion oder LoDi-Motorplatinen werden durch diesen Befund nicht erforderlich.

## Quellen und Herkunft

- **Nutzerbeleg, 18.09.2026:** neues Foto des bereits eingebauten Drehgestells sowie Bericht über Durchgang Grau/Fahrgestell bei Bewegung nach links und Gelb/Fahrgestell bei Bewegung nach rechts; Braun ausdrücklich nur als vermutete Masse. Das Foto wurde für diesen Nachtrag betrachtet, aber nicht als neue Bilddatei in das öffentliche Repository hochgeladen.
- **Q1 – Lokstoredigital, Herstellershop:** [LoDi-WiB ICE-M Front 2 Stück](https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/), Abschnitt Frontmodule: ICE-1-Frontbeleuchtung ohne Vorwiderstände. Abgerufen am 18.09.2026.
- **Q2 – Lokstoredigital, Herstellerbeispiel 33701:** [ICE 1 mit 2 Triebköpfen](https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/), LED-Anschlüsse und unterschiedliche Verwendung brauner/oranger Litzen. Dessen Gesamtplatinenlösung wird nicht übernommen. Abgerufen am 18.09.2026.
- **Q3 – Vishay:** [1N4148-Datenblatt](https://www.vishay.com/docs/81857/1n4148.pdf), insbesondere Seite 1: Kathodenkennzeichnung und elektrische Grenzwerte. Abgerufen und Seite 1 visuell geprüft am 18.09.2026.
- **Projektbasis:** [Grundanleitung REV17](Anleitung_Grundumbau_60941_60972_LoDi514.md), insbesondere 10 und 11B. Der neue Nutzerbefund aktualisiert deren bisherigen offenen Einbaustand; er ist keine eigene Hardwareprüfung durch den Verfasser.
