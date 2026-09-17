REV16  /  01  /  WERKSTATT


## 1 ICE 2976: ein Decoder, mfx

Werkstattanleitung REV16, 16.09.2026. Deine gewählte Ausstattung: HLA-Motor 60941, ein 60972 ohne Sound und zwei LoDi-514. Keine LoDi-Motorplatinen, keine Traktion, keine zusätzlichen Kabel zwischen den Fahrzeugen.

[Schema system]

[['Parameter', 'Festlegung'], ('Motor / Decoder', '60941 und 60972 im motorisierten Kopf A.'), ('Anmeldung', 'Genau ein mfx-Decoder und ein CS3-Lokeintrag.'), ('Kopflicht', 'F0 schaltet beide Köpfe; automatisch Weiß/Rot nach Fahrtrichtung.'), ('Hinterer Kopf', 'Passiver Dioden-/Widerstandsadapter, keine Decoderanmeldung.'), ('Kupplungen', 'Zwei Kontakte ausschließlich für die hintere Kopfbeleuchtung.'), ('Wagenlicht', 'Bestehende Beleuchtung lokal aus Mittelschleifer + Radkontakten.'), ('Motorstrom', 'Nur Schleifer A; beide Schleifer sind nicht parallel verbunden.')]

<b>Voraussetzung für diese konkrete Ausführung:</b> Die zwei Kupplungspole sind vom Wagenlicht und Gleisstrom frei. Jeder beleuchtete Mittelwagen benötigt seine eigene vollständige Stromaufnahme. Nur Achskontakte genügen nicht. Fehlen Mittelschleifer, ist die Material-/Versorgungsfrage auf Seite 11 vor Einbau zu lösen.

Die Zweileiterschaltung ist eine eigene Auslegung. Ihre Zustände sind rechnerisch und mit SPICE geprüft; die Abnahme am echten Decoder und Zug folgt auf den Seiten 14-15. Das ist keine Herstellerfreigabe und kein vorgetäuschter Hardwaretest.

REV16  /  02  /  WERKSTATT


## 2 Bauteile und Werkzeug bereitlegen

Bestellnachweise und tatsächlichen Besitz getrennt behandeln. Der 60972 wurde von dir als vorhanden genannt. Alles Weitere vor Arbeitsbeginn auf den Tisch legen.

[['Bauteil', 'Menge / Verwendung', 'Bestand'], ('Märklin 60972', '1 mit 21MTC-Träger', 'Vorhanden laut Nutzer.'), ('Märklin 60941', '1 vollständiger HLA-Satz', 'Bestellt; Vollständigkeit prüfen.'), ('LoDi-514', '1 Set mit zwei Frontmodulen', 'Bestellt; geliefert bereitlegen.'), ('E395640', '2 für Triebköpfe', 'Versand angegeben; Passung prüfen.'), ('E374060 / E374340', '4 bestellte Paare; Bedarf nach Wagenzahl', 'Als zugestellt angegeben.'), ('RFw, RFr, RR, RW', '4 x 47 kOhm, 0,25 W, 5 % oder besser', 'Zusätzlich erforderlich.'), ('RP1, RP2', '2 x 4,7 kOhm, 0,5 W, 5 % oder besser', 'Zusätzlich erforderlich.'), ('RS1, RS2', '2 x 1 kOhm, 1 W, 5 % oder besser', 'Zusätzlich erforderlich.'), ('D1-D4', '4 x 1N4148, bedrahtet', 'Zusätzlich erforderlich.'), ('Isolierende Montage', 'Lötstützpunkte, Schrumpfschlauch, Feinlitze', 'Bestand nicht belegt.')]

Die kleine Adapterschaltung benötigt keine LoDi-Platine. Sie wird auf isolierten Lötstützpunkten oder einem kleinen Stück Lochraster befestigt. Ein ESU-Decoder ist in dieser Ausführung nicht erforderlich. 60977, 60982, LoDi-511/512 und LoDi-510 bleiben ungenutzt.

Werkzeug: Multimeter, feine Lötstation, Entlötlitze, Schraubendreher, Pinzette, Lupe und isolierende Unterlage. Die CS3 übernimmt Anmeldung und Einrichtung über mfx; ein Windows-PC oder ESU-LokProgrammer ist für diesen Hauptweg nicht nötig.

Für die Startauslegung muss die verwendete CS3-/Netzteilkonfiguration eine maximale Spannung von 24 V am Lichtkreis einhalten. Den Netzteiltyp und die passende CS3-Einstellung prüfen. Ein beliebiger Multimeterwert am Digitalgleis belegt keine Spitzenspannung.

REV16  /  03  /  WERKSTATT


## 3 Öffnen und Leitungen zuordnen

Kopf A ist der motorisierte Triebkopf. Markiere ihn dauerhaft innen mit A, den motorlosen Kopf mit B. Die Richtung A voraus heißt in dieser Anleitung vorwärts.

Eigenes Referenzfoto aus REV10: Motor links, lange Originalplatine rechts. Kein verifizierter Lötstellenplan.

Eigenes Referenzfoto: alte Feldwicklung am Motor sichtbar. Die Padfunktionen sind im Bild nicht vollständig erkennbar.

<b>1.</b> Zug vom Gleis nehmen. Kupplungsabdeckung vorsichtig abziehen und die passende untere Gehäuseschraube lösen. Gehäuse anheben; bei Widerstand zuerst nach einer weiteren Haltestelle suchen.

<b>2.</b> Alle vorhandenen Leitungen vor dem Ablöten fotografieren. Schleifer, Radmasse, Motorbürsten, Frontlicht und beide Kupplungskontakte durch Verfolgen zuordnen; Etiketten anbringen.

<b>3.</b> Alten Fahrtrichtungsumschalter bzw. alten Decoder elektrisch vollständig vom neuen Motor- und Kopflichtkreis trennen. Neue Decoderausgänge werden nie an dessen Ausgänge angeschlossen.

<b>4.</b> Originalplatine kann als mechanischer Träger bleiben. Nur durchgemessene passive Leiterzüge als Verteiler nutzen. Keine Leiterbahn anhand eines fremden Fotos schneiden. Prüfe Schraubaugen und Schalter in beiden Stellungen gegen die geplanten Netze.

<b>Ergebnis:</b> Jede neue Leitung hat ein bekanntes Ziel. Vorhandene Wagenlichtleitungen sind separat dokumentiert. Ein noch unklarer Anschluss bleibt isoliert.

REV16  /  04  /  WERKSTATT


## 4 Hochleistungsmotor einbauen

Der 60941 ersetzt Feldmagnet, Anker und Motorschild des passenden Trommelkollektormotors. Getriebe und Fahrwerk bleiben bestehen. Die mechanische Passung am eigenen Fahrzeug ist vor dem Festziehen zu prüfen.

Märklin 60941/60943, Original-Montagezeichnung [Q2]. Gezeigtes Fahrwerk ist schematisch, kein ICE-Foto.

<b>1.</b> Bürstenfedern entlasten und alte Bürsten entnehmen. Motorleitungen ablöten. Beide Motorschildschrauben lösen; Schild, Anker und Feldmagnet entnehmen. Reihenfolge der Teile fotografieren.

<b>2.</b> Lose Verschmutzung aus dem Getriebe entfernen. Räder und Zahnräder von Hand bewegen. Ein klemmendes Getriebe vor dem Motorumbau instand setzen.

<b>3.</b> Permanentmagnet (1), fünfpoligen Anker (2) und passendes Motorschild (3) einsetzen. Ritzel sauber ins Getriebe eingreifen lassen. Schrauben (4) gleichmäßig anziehen; sie dürfen kein Zahnrad berühren.

<b>4.</b> Neue Bürsten (5) einsetzen und Federn auflegen. Drosseln (6) nach Anschlusszeichnung anbringen. Rotor/Getriebe nochmals drehen. Magnetisches Rasten ist normal; hartes Klemmen ist es nicht.

REV16  /  05  /  WERKSTATT


## 5 Motor verdrahten und isolieren

Beide Bürstenanschlüsse müssen elektrisch vom Metallfahrwerk getrennt sein. Das ist vor dem Anschluss des Decoders zu messen.

[Schema motor]

LoDi-Herstellerbeispiel 33701 [Q3]: Pfeile zeigen Entstörkondensatoren zur Masse. Nur als Vergleich verwenden.

<b>1.</b> Je eine vorgesehene Motordrossel in jede Motorleitung einfügen: 60972 grün/MV zur ersten Bürste, blau/MR zur zweiten Bürste. Lötstellen isolieren.

<b>2.</b> Kondensatoren von den Bürsten zum Chassis entfernen, sofern vorhanden. Ein Kondensator ausschließlich zwischen beiden Bürsten darf bleiben. Keine Entstörteile auf Verdacht entfernen.

<b>3.</b> Decoder und beide Motorzuleitungen für die Messung abtrennen. Multimeter zunächst mit kurzgeschlossenen Spitzen prüfen. Danach jede Bürste gegen blankes Chassis messen: kein dauerhafter Durchgang. Mehrere Rotorstellungen prüfen.

<b>4.</b> Zwischen den Bürsten ist ein endlicher, rotorabhängiger Wicklungswiderstand zu erwarten. Vor dem ersten Einschalten nochmals prüfen, dass Schrauben und Bürstenfedern das Gehäuse nicht berühren.

Im Kopf B wird kein Motor und kein Decoder eingebaut. Sein LoDi-514-Kopflicht ist gegenüber Fahrwerk, Schleifer und Wagenbeleuchtung vollständig isoliert.

REV16  /  06  /  WERKSTATT


## 6 60972 im Kopf A anschließen

Den mitgelieferten 21MTC-Träger des 60972 isoliert befestigen. Der Decoder bleibt während aller Lötarbeiten abgezogen. Anschlussnamen haben Vorrang vor Farben.

Märklin 60972, Träger und Steckrichtung [Q1]. +Ub entspricht hier dem gemeinsamen Decoderplus U+.

[['60972-Träger', 'Verbindung'], ('Rot, B/G rechts', 'Nur Mittelschleifer A; kein B-Zug über die Kupplungen.'), ('Braun, 0/G links', 'Sichere örtliche Rad-/Chassismasse.'), ('Grün / Blau, MV / MR', 'Über je eine Drossel zum 60941; siehe Seite 5.'), ('Orange, +Ub / U+', 'VCC der vorderen LoDi-514 sowie RP1/RP2 im Sender.'), ('Grau LV / Gelb LR', 'Jeweils über eigenen Widerstand zur Front, Seite 7.'), ('AUX1 / AUX2', 'Zum Zweileiter-Adapter auf Seite 8.'), ('AUX3/4, GND, +5V, SUSI', 'Unbenutzt; einzeln isolieren.')]

Träger so befestigen, dass weder Kupferflächen noch Decoderbauteile die Originalplatine oder Schrauben berühren. Die durch den fehlenden Stift kodierte Steckposition prüfen; niemals um eine Reihe versetzt stecken. Vor dem Gehäuseschluss Kabelschlaufen aus dem Bereich der Zahnräder entfernen.

REV16  /  07  /  WERKSTATT


## 7 LoDi-514 vorn: Weiß und Rot

Die Frontmodule besitzen keine Vorwiderstände [Q5]. Ohne LoDi-511/512 kommen deshalb externe Widerstände direkt in die beiden Farbzweige.

LoDi-Herstellerfoto [Q3]: Anschlussfelder red, VCC und white. Die Lage am eigenen Modul anhand der Beschriftung prüfen.

[Schema front]

<b>1.</b> Alte Frontlampen samt Fassungen ausbauen; Lichtleiter sauber lassen. LoDi-514 zuerst ohne Kleber einpassen. Halter darf Gehäuse und Lichtleiter nicht verspannen.

<b>2.</b> VCC mit orange/U+ des 60972 verbinden. Grau/LV über den Widerstand RFw mit 47 kOhm an white, gelb/LR über RFr mit 47 kOhm an red anschließen.

<b>3.</b> Beide Widerstände einzeln nachmessen und isolieren. Bei 5 % Toleranz: 44,65 bis 49,35 kOhm. Keine Verbindung von VCC zur Radmasse herstellen.

<b>Stromarme Startauslegung, kein LoDi-Nennwert:</b> 47 kOhm / 0,25 W begrenzt bei höchstens 24 V und 5 % Toleranz den Strom selbst ohne LED-Spannungsabzug auf 0,54 mA. Das Licht kann schwach ausfallen. Die Versorgungskonfiguration muss diese Spannungsgrenze einhalten; kleinere Widerstände erst nach belegtem zulässigem LED-Zweigstrom einsetzen. Die zuvor genannten 3,3 kOhm waren dafür nicht ausreichend belegt.

REV16  /  08  /  WERKSTATT


## 8 Adapter vorn: zwei Steuerleitungen

Für das hintere Kopflicht werden die verstärkten AUX1/AUX2 benutzt. Die vorderen LEDs bleiben getrennt an LV/LR. Das verhindert, dass ihre LED-Zweige als ungewollte Versorgung des hinteren Kopfes mitwirken.

[Schema sender]

<b>1.</b> RP1 (4,7 kOhm / 0,5 W) zwischen U+ orange und AUX1 braun/rot löten. RP2 gleichartig zwischen U+ und AUX2 braun/grün löten. Das sind absichtliche Widerstandsverbindungen, keine Drahtbrücken.

<b>2.</b> Von AUX1 über RS1 (1 kOhm / 1 W) zum Kupplungskontakt K1 gehen. Von AUX2 über RS2 zum Kontakt K2 gehen. Die Reihenfolge ist wichtig: RP am AUX-Knoten, RS zwischen diesem Knoten und Kupplung.

<b>3.</b> Alle Bauteile zugentlastet und isoliert befestigen. Widerstände nicht in engen Kontakt zu Gehäusekunststoff oder Decoder legen. Im normalen Betrieb entstehen an einem RP bei 24 V höchstens etwa 0,13 W.

<b>4.</b> An K1/K2 darf kein bisheriger RT-, GE-, Mittelschleifer- oder Innenlichtanschluss mehr hängen. Beide Leitungen bis zur nächsten Kupplung durchmessen.

<b>Funktion:</b> Ein eingeschalteter AUX zieht seinen Zweig nach Decoder-Minus. Der Widerstand RP hält den ausgeschalteten anderen Zweig auf Plus. Dadurch liegt zwischen K1 und K2 eine richtungsabhängige Spannung. Bei beiden AUX AUS verschwindet die Spannungsdifferenz und das hintere Licht erlischt.

REV16  /  09  /  WERKSTATT


## 9 Adapter hinten: Dioden und LoDi-514

Kopf B braucht für sein Kopflicht weder Radkontakt noch Schleifer. Die Energie kommt zusammen mit der Farbauswahl über K1/K2. VCC hier ist der lokale Punkt P des Adapters, nicht Fahrzeugmasse.

[Schema receiver]

[['Bauteil / Punkt', 'Verbindung'], ('D1', 'Anode ohne Ring an K1; Kathode mit Ring an P.'), ('D2', 'Anode ohne Ring an K2; Kathode mit Ring ebenfalls an P.'), ('P', 'An VCC und Ringseiten D1-D4; isoliert von Gleis/Chassis.'), ('RR, 47 kOhm', 'Zwischen LoDi red und K1.'), ('RW, 47 kOhm', 'Zwischen LoDi white und K2.'), ('D3, Sperrspannungsschutz', 'Anode an red-Pad; Ringseite direkt an VCC/P.'), ('D4, Sperrspannungsschutz', 'Anode an white-Pad; Ringseite direkt an VCC/P.')]

Alle vier Dioden-Ringseiten gehören an P. D3/D4 begrenzen die negative LED-Spannung. Lose Diode vor Einbau prüfen: roter Messkontakt an Anode, schwarzer an Ringseite ergibt Durchlass; umgekehrt sperrt sie. Alten Lichtumschalter und Schleiferanschluss vollständig vom neuen Lichtkreis trennen.

REV16  /  10  /  WERKSTATT


## 10 Kupplungen als Lichtverbindung

Die beiden Kupplungspole erhalten neue Funktionen: K1 und K2. Alte Farbbezeichnungen RT/GE dürfen nicht als elektrische Belegung übernommen werden. In den Wagen wird nur kontaktgleich durchgeleitet.

[Schema coupling]

<b>1.</b> Alle Fahrzeugübergänge zählen und die mechanisch passenden Kupplungen trocken einsetzen. Männliche/weibliche Gegenseite, Halterhöhe und seitliche Beweglichkeit prüfen. Unpassende Teile nicht unter Spannung mit Gewalt einpassen.

<b>2.</b> Alle bisherigen Verbraucher und Schleiferverbindungen von den beiden Durchgangsleitungen trennen. Die örtliche Wagenbeleuchtung bleibt ein eigener Stromkreis, Seite 11. Keine Kupplung darf die neuen Lichtsignale mit Gleisspannung verbinden.

<b>3.</b> Am noch von Adaptern und LEDs getrennten Kabelbaum K1 vom ersten bis zum letzten Fahrzeug niederohmig messen; anschließend K2. Jeden Wagen einzeln ergänzen und dieselbe Zuordnung erhalten.

<b>4.</b> K1 gegen K2, gegen alle Radkontakte und gegen jeden Mittelschleifer messen: kein Durchgang. Kupplungen und Drehgestelle dabei bewegen. Die Messung gilt für den unbestückten Kabelbaum, nicht für angeschlossene Halbleiter.

<b>5.</b> Erst nach bestandenem Test Adapter A und B verbinden. Wagenübergänge bei ausgeschalteter Gleisspannung kuppeln. Kein zusätzliches Kabel außen neben den Kupplungen führen.

K1 und K2 sind vollständig für das Kopflicht belegt. Ein paralleler Motor-Strombus beider Schleifer oder eine neue Wagenlichtversorgung über dieselben Pole ist in dieser Schaltung nicht enthalten. Das erklärt den Unterschied zur früheren RT/GE-Planung.

REV16  /  11  /  WERKSTATT


## 11 Mittelwagen versorgen ihr Licht selbst

Du möchtest die vorhandene Wagenbeleuchtung über die eigenen Stromabnehmer weiterbetreiben. Dafür braucht jeder Wagen eine vollständige Versorgung. Rad-/Achsschleifer allein liefern bei Märklin nur den Außenschienenanschluss.

[['Versorgung im Wagen', 'Erforderlicher Anschluss'], ('Mittelschleifer unter dem Wagen', 'Gleismitte B zum vorhandenen Lichtkreis.'), ('Rad-/Achskontakte', 'Außenschienen 0 zum vorhandenen Lichtkreis.'), ('Kupplung K1/K2', 'Nur Kopflicht durchleiten, keine Verbindung zum Wagenlicht.'), ('Vorhandene Lampen/Platine', 'Für dauernde Digitalspannung geeignet; Polung und Nennspannung prüfen.')]

<b>1.</b> Unter jeden beleuchteten Wagen schauen: Ist ein eigener Mittelschleifer vorhanden? Danach die Rad-/Achskontakte prüfen. Beides fotografieren und mit dem Multimeter bis zum Lichtkreis verfolgen.

<b>2.</b> Wenn der Lichtkreis bereits unabhängig aus diesen beiden Anschlüssen gespeist wird, bleibt er so bestehen. Eventuelle zusätzliche Verbindungen zur Kupplung trennen, damit die zwei neuen Lichtleitungen frei sind.

<b>3.</b> Wenn der Mittelschleifer fehlt, ist die lokale Versorgung noch nicht vollständig. Einen zum konkreten Wagen passenden Schleifer mit Halter nachrüsten oder das Versorgungskonzept neu festlegen. Keine Artikelnummer ohne Zuordnung zum Wagen bestellen.

<b>4.</b> Nennspannung der bestehenden Lampen bzw. Platine feststellen. Einen Wagen kurz allein auf Digitalgleis testen, ausschalten und die Lampensitze auf ungewöhnliche Erwärmung prüfen. Wagen danach einzeln ergänzen.

<b>Noch nicht belegt:</b> Aus deiner Angabe zu den Achsschleifern geht die Existenz eigener Mittelschleifer nicht sicher hervor. Die Zweileiter-Kopflichtschaltung ist deshalb an diese Vorprüfung gebunden. Fehlen sie, ist die vollständige Materialliste noch offen. Die Anleitung behauptet nicht, dass Radkontakte allein Licht erzeugen können.

Vorteil der örtlichen Versorgung: unabhängige Stromkreise und freie Kupplungspole. Nachteile: mögliche Kontaktflackerer, Schleiferreibung und Wagenlicht ohne neue gemeinsame F-Tasten-Schaltung. Dafür bleiben die vorhandenen Leuchtmittel und ihre Innenverkabelung weitgehend erhalten.

REV16  /  12  /  WERKSTATT


## 12 60972 anmelden und einrichten

Nur ein Decoder wird eingebaut. Deshalb genügt die normale mfx-Anmeldung an deiner CS3. Weder eine gemeinsame DCC-Adresse noch ein ESU-Slave oder eine Traktion ist erforderlich.

<b>1.</b> Kopf A nach bestandenem Motor-/Isolationscheck allein auf einen vollständig isolierten Prüfabschnitt stellen. Hinteren Adapter zunächst abgekoppelt lassen. CS3 einschalten und mfx-Anmeldung abwarten.

<b>2.</b> Die neue Lok eindeutig ICE 2976 nennen. Firmware-/Decoderdaten und Ausgangseinstellungen sichern. In der CS3-Lokbearbeitung die Konfiguration des angemeldeten Decoders vollständig lesen.

<b>3.</b> Den Motorbereich auf HLA/C90 einstellen. Für den 60972 nennt die DCC-Tabelle dazu Motortyp 3; unter mfx die entsprechende Motorprofil-Auswahl benutzen. Einen fremden CV-Satz nicht blind laden.

<b>4.</b> Anfahrzeit zunächst etwa 7 Sekunden, Bremszeit etwa 5 Sekunden einstellen. Höchstgeschwindigkeit zunächst begrenzen und erst nach einem sauberen Fahrtest erhöhen. Feinabgleich des Motors ist individuell.

<b>5.</b> mfx aktiviert lassen. Analogbetrieb für diese digitale Ausführung ausschalten. Die beiden Lichtausgänge und AUX1/AUX2 nach der nächsten Seite einrichten.

[['Parameter', 'Ziel'], ('Decoderanzahl', '1: Märklin 60972.'), ('Aktives Fahrprotokoll', 'mfx; automatische Anmeldung.'), ('Traktion / Slave', 'Keine.'), ('Motor', '60941, HLA/C90-Startprofil.'), ('Frontausgänge', 'LV und LR, richtungsabhängig mit F0.'), ('Hintere Lichtsteuerung', 'AUX1 und AUX2, ebenfalls F0-richtungsabhängig.'), ('AUX3/4', 'Frei, unbeschaltet.'), ('Lichteffekt / Dimmen AUX1/2', 'Normales Dauerlicht, 100 %, kein Blinken, kein Timer.')]

Die Widerstände begrenzen den LED-Strom. Dimmen ersetzt keine Vorwiderstände. AUX1/AUX2 für die Zweileiterschaltung nicht als Kupplungsimpuls, Blinklicht oder unabhängig schaltbare Zusatzfunktion betreiben.

REV16  /  13  /  WERKSTATT


## 13 F0 und Fahrtrichtung zuordnen

Alle vier Ausgänge reagieren auf dieselbe Funktion F0. Die Auswahl hängt von der Richtung ab, nicht von der Geschwindigkeit. Die Bedingung muss deshalb jeweils im Stand und während der Fahrt gelten.

[['F0', 'Zugrichtung', 'Ausgänge EIN', 'Resultat'], ('AUS', 'beliebig', 'keine', 'Beide Köpfe dunkel.'), ('EIN', 'A voraus / vorwärts', 'LV und AUX1', 'A weiß, B rot.'), ('EIN', 'B voraus / rückwärts', 'LR und AUX2', 'A rot, B weiß.')]

<b>1.</b> In der Funktionszuordnung von F0 die vorhandenen LV/LR-Einträge kontrollieren. LV darf nur bei Vorwärts aktiv sein; LR nur bei Rückwärts. Beide müssen auch im Stand schalten.

<b>2.</b> Zu F0 einen Ausgang AUX1 mit Bedingung Vorwärts ergänzen. AUX2 mit Bedingung Rückwärts ergänzen. Wenn die Oberfläche getrennte Bedingungen für Stand/Fahrt anbietet, beide Zustände aktivieren.

<b>3.</b> Werkseitige oder frühere unabhängige Zuweisungen von F1 zu AUX1 und F2 zu AUX2 entfernen. Sonst kann eine zusätzliche Taste das hintere Licht ungewollt übersteuern.

<b>4.</b> Bei AUX1/AUX2 den normalen verstärkten Lichtausgang mit voller Helligkeit, ohne Timer und ohne Sonderwirkung einstellen. Die sichtbaren Menünamen können mit Firmware und Decoderprojekt variieren; maßgeblich ist die obige Zustandstabelle.

<b>5.</b> Bei stehendem Kopf A zunächst am Sender prüfen: F0 AUS ergibt zwischen K1/K2 nahezu 0 V. F0 EIN vorwärts macht K2 gegenüber K1 positiv; rückwärts macht K1 gegenüber K2 positiv.

Messung ohne LED-Last

Multimeter auf Gleichspannung stellen, rote Spitze K2, schwarze K1. Vorwärts wird ein positiver, rückwärts ein negativer Wert erwartet. AUS liegt nahe 0 V. Die Messspitzen vorher stromlos anklemmen. Zeigt AUS eine dauerhafte Spannung, zuerst Mapping und Verdrahtung korrigieren; Kopf B noch nicht anschließen.

AUX1/AUX2 sind hier eigene Ausgänge für den hinteren Adapter. Sie werden nicht mit LV/LR zusammengelötet. Das hintere Rot/Weiß wird durch K1/K2 und den passiven Adapter bestimmt, nicht durch einen zweiten Decoder.

REV16  /  14  /  WERKSTATT


## 14 In kleinen Stufen einschalten

Die folgenden Tests sind Bestandteil des Einbaus. Eine Simulation belegt die Logik der Schaltung, kann aber falsche Lötstellen, unpassende Bauteile und reale Decoder-Effekte nicht ausschließen.

[Schema test]

<b>1.</b> Lose C-Gleise vollständig von der Anlage trennen. CS3 ausschalten und nur den Programmierausgang anschließen: B an Mittelleiter, 0 an Außenschienen. Keine Verbindung zu Booster oder zweiter Versorgung.

<b>2.</b> Kopf A allein prüfen: mfx, vorderes Licht und langsame Motorbewegung. Danach den Sender ohne hinteren Adapter gemäß Seite 13 messen.

<b>3.</b> Strom aus. Hinteren Adapter zuerst außerhalb des Fahrzeugs über die vorbereiteten K1/K2-Leitungen anschließen. F0 AUS sowie beide Richtungen testen. Vorwärts nur red, rückwärts nur white.

<b>4.</b> LED-Ströme durch Gleichspannungsmessung über RR und RW prüfen: I = U/R. Bei 47 kOhm entsprechen 10 V etwa 0,21 mA. Der jeweils ausgeschaltete Farbzweig darf nicht sichtbar leuchten. Bei falschem Verhalten ausschalten und Diodenrichtung prüfen.

<b>5.</b> Adapter isoliert in Kopf B einbauen. Danach jeden Wagenübergang einzeln ergänzen und alle drei Lichtzustände wiederholen. Wagenlicht bleibt elektrisch separat.

<b>6.</b> Für Fahrtests ein ausreichend langes freies Gleis/Oval am Hauptgleisausgang benutzen. Vor dem Umstecken ausschalten und Programmiergleisanschluss vollständig lösen.

Eine automatische Motor-Einmessfahrt ist erst auf einem freien geeigneten Oval zulässig; Märklin empfiehlt Radien über 430 mm. Sie kann stark beschleunigen. Für die erste kurze Prüfung ist sie nicht nötig. Kein dauerhaftes Fahren auf dem kurzen Tisch-Prüfabschnitt.

REV16  /  15  /  WERKSTATT


## 15 Abnahme, Vorteile und Grenzen

Nach dem Gehäuseschluss sämtliche Lichtzustände und die langsame Fahrt erneut prüfen. Nicht eingeschaltete Farbzweige müssen dunkel bleiben; die Farben beider Köpfe müssen zur tatsächlichen Fahrtrichtung passen.

[['Abnahme', 'Soll / Eintrag'], ('F0 AUS', 'Beide Köpfe dunkel: __________'), ('F0 EIN / A voraus', 'A weiß, B rot: __________'), ('F0 EIN / B voraus', 'A rot, B weiß: __________'), ('STOP, aus/ein, Richtungswechsel', 'Licht reagiert wieder korrekt: __________'), ('Kurven / Gegenkurven langsam', 'Kein Kontaktabbruch/Kurzschluss: __________'), ('5-10 Minuten Probefahrt', 'Motor, Widerstände und Lampensitze unauffällig: __________'), ('Wagenlicht unabhängig', 'Mittelschleifer und Radkontakte vorhanden/geprüft: __________')]

[['Vorteil', 'Nachteil / praktische Grenze'], ('Ein mfx-Eintrag ohne Traktion', 'Nur der vordere Schleifer speist den Motor.'), ('Ein Decoder statt komplexer Synchronisation', 'Kleine selbst zu lötende Adapterschaltung nötig.'), ('Zwei vorhandene Kupplungspole genügen', 'Beide Pole sind vollständig durch Kopflicht belegt.'), ('Keine zusätzliche Leitung zwischen Wagen', 'Mittelwagen brauchen ihre eigene komplette Lichtversorgung.'), ('Hochleistungsmotor und automatischer Lichtwechsel', 'Motorabgleich und tatsächliche Probefahrt bleiben nötig.'), ('Keine LoDi-Motorplatinen, kein Sound', 'Kein zentral geschaltetes neues Wagenlicht in dieser Stufe.')]

Bei zu schwachem Licht: zuerst Gehäuse/Lichtleiter prüfen. Die 47-kOhm-Widerstände sind eine stromarme Startauslegung; hellere Einstellung braucht den zulässigen LED-Zweigstrom. Bei falscher hinterer Farbe: K1/K2-Zuordnung und Mapping prüfen. Bei Flackern hinten: Kupplungskontakte prüfen. Bei Flackern im Wagen: seine eigenen Stromabnehmer prüfen.

<b>Bewertung:</b> Diese Ausführung erfüllt mfx, keine Traktion und möglichst wenig Elektronik am besten, sofern die Wagen lokal vollständig versorgt sind. Eine optimale gemeinsame Motor-Stromaufnahme aus beiden Schleifern ist damit nicht umgesetzt. Das ist der konkrete Preis dafür, beide vorhandenen Kupplungspole für das Kopflicht zu nutzen.

REV16  /  16  /  WERKSTATT


## 16 Nachweise und klare Ausführungsgrenzen

Die Schaltung wurde als eigene Auslegung erstellt. Motor-/Decoderanschlüsse und LED-Polarität stützen sich auf die Herstellerunterlagen. Referenzbilder sind als eigene Fotos oder Herstellervergleich gekennzeichnet.

<b>Q1</b> <link href="https://static.maerklin.de/damcontent/93/1d/931db48faf5660916556d5172c598cdf1663856135.pdf" color="#087F86">Märklin 60972/60982: Anschlüsse, Ausgänge, Motorprofil, mfx</link>

<b>Q2</b> <link href="https://static.maerklin.de/damcontent/e3/bb/e3bb202fe80385cc96835d783af5e1821670919973.pdf" color="#087F86">Märklin 60941/60943: Original-Montagezeichnung</link>

<b>Q3</b> <link href="https://lokstoredigital.jimdoweb.com/hardware/beleuchtung/lodi-motor-wib-ice1m/" color="#087F86">LoDi ICE 1: Frontanschlüsse und Motorvergleichsfoto</link>

<b>Q4</b> <link href="https://www.marklin.nl/producten/details/article/60941" color="#087F86">Märklin 60941: Trommelkollektor-Umrüstung</link>

<b>Q5</b> <link href="https://www.lodi-shop.de/produkte/beleuchtung-und-umr%C3%BCstung/lodi-wib-ice-m/" color="#087F86">LoDi Front: ohne integrierte Vorwiderstände</link>

<b>Q6</b> <link href="https://www.vishay.com/docs/81857/1n4148.pdf" color="#087F86">Vishay 1N4148: Polaritätsring und elektrische Daten</link>

Rechnung und Simulation

Vier 47-kOhm-LED-Widerstände, 5 %: bei höchstens 24 V maximal 0,54 mA je Zweig ohne LED-Spannungsabzug. Hinterer Strom fällt durch Senderwiderstände und Diode kleiner aus. Je RP 4,7 kOhm: maximal etwa 0,13 W bei 24 V; gewählt 0,5 W. Je RS 1 kOhm: gewählt 1 W. Die Bauteile sind dennoch gegen Kunststoffkontakt und Kurzschluss zu isolieren.

SPICE-Prüfung: 144 statische Fälle mit 12/18/24 V, vier AUX-Zuständen, drei gemeinsam variierten Widerstandstoleranzen und normal/offen/Kurzschluss K1-K2. Alle geprüften Zustände bestanden. Modellmaximum hinterer LED-Strom 0,421 mA; negative LED-Spannung unter 0,35 V. Repräsentative LED- und Schaltermodelle; keine Messdaten der echten LoDi-LEDs, keine vollständige transiente EMV- oder Temperaturprüfung.

Noch am realen Modell zu prüfen

Mittelschleifer der Mittelwagen, Kupplungspoltrennung, mechanische Passung, LED-Helligkeit, tatsächliches AUX-Verhalten und die endgültig geschlossenen Fahrzeuge. Die Seite 11 ist eine konkrete Bestandsprüfung, keine bereits bestätigte lokale Wagenversorgung. Ein fehlender Mittelschleifer macht einen zusätzlichen Versorgungsschritt notwendig.

Die Dokumentfassung ist fertig. Ein vollständig nachgebauter und betrieblich freigegebener Zug wird damit nicht behauptet. Die Referenzfotos geben keine ungemessenen Lötpads der Originalplatine frei. Ein ESU-Slave bleibt eine andere, zusätzlich zu prüfende Architektur und ist nicht heimlich Voraussetzung dieser Anleitung.