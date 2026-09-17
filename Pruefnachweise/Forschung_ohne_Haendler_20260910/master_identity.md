# Masteridentität und SID-Nachweis ohne Händler

Recherche: 10.09.2026. Gegenstand ausschließlich Märklin 60977 mSD3 als Master, ESU 59649 LokPilot 5 M4 MKL als Slave und vorhandene CS3; ergänzend vorhandene Mobile Station/Gleisbox. Keine Decoder oder Zentralen wurden angesprochen oder verändert. Die REV10 blieb unverändert.

## Ergebnis

Der Händler ist für die Identitätsgewinnung nicht erforderlich. Für den 60977 ist die Herstellerkennung **131** bereits in dessen eigener Märklin-Anleitung belegt. Für die CS3 existieren zudem überprüfbare Originalimplementierungen und CS3-Testdaten, welche den konkreten Leseweg zur unveränderten mfx-UID und zugewiesenen SID erheblich besser absichern als REV10. Die individuelle UID des vorhandenen 60977 fehlt weiterhin; sie lässt sich nicht aus Artikelnummer, Herstellerkennung oder Firmware ableiten.

Die stärkste technische Arbeitshypothese lautet: **ESU-Zielseriennummer S = vollständiger unveränderter unsigned-32-Wert der mfx-UID**, anschließend die bereits belegte Bytezerlegung in CV192–195. Eine zusätzliche Märklin-spezifische Rechenoperation wurde nicht gefunden. Diese Hypothese ist jedoch kein nachgewiesener Funktionsbefund am 60977/59649 und keine fertige Schreibkarte. Ein positiver Offline-Export allein beweist außerdem nur die Softwareabbildung, nicht das spätere Folgen bei mfx.

## Was nun belastbar belegt ist

| Aussage | Beleg und Evidenzklasse | Grenze |
|---|---|---|
| 60977-Herstellerkennung in CV8 ist 131 | Märklin-Originalanleitung der Sets 60975/60976/60977, gedruckte S.19, CV8-Zeile: Hersteller-ID 131, nur lesen. Primärquelle des Herstellers. | Nicht automatisch der Beweis, wie ESU CV191 unter mfx auswertet. |
| Märklin/Trix-manID ist 0x83, ESU-manID 0x97 | Krauß, *Schienenformat mfx*, Version 2.3, S.39, §6.4.1 CA-Typ 10: separates vier Byte großes Herstellerfeld; letztes Byte entspricht DCC-Hersteller-ID. Originale Protokollanalyse. | Reverse Engineering, keine Herstellerfreigabe; nicht das UID-Präfix. |
| UID und SID sind verschiedene Werte | Märklin CAN 2.0, S.28, MFX Bind: Decoder-UID 4 Byte und zugewiesene SID 2 Byte; S.51 dokumentiert `.mfxuid` und `.sid` getrennt. Herstellerprotokoll. | Dokument ursprünglich für CS2. |
| CS3-Datei mit diesen Feldern existiert | TrainControl, Commit `5f0a75e33256c4c1b4ac1998134c4bd04030fed0`, `test/lokomotive_cs3.cs2`, Z.4–11. Originales Software-Testmaterial. | Andere Anlage; keine Identität des Nutzerdecoders. |
| Konkreter CS3-Leseweg im Softwarecode | Derselbe Commit, `src/org/traincontrol/marklin/file/CS2File.java`, Z.184–186: `/config/lokomotive.cs2`. Originalimplementierung. | Am tatsächlichen CS3-Softwarestand muss erfolgreiche GET-Antwort bestätigt werden. |

Quellen unmittelbar dazu: [Märklin 60975/60976/60977, S.19](https://static.maerklin.de/damcontent/36/f5/36f55304fb028471e05de4762e04fada1663856051.pdf#page=19), [Krauß, S.39](https://www.skrauss.de/modellbahn/Schienenformat.pdf#page=39), [Märklin CAN 2.0, Originaldokument im Rocrail-Spiegel](https://wiki.rocrail.net/lib/exe/fetch.php?media=cs2%3Acs2can-protokoll-2_0.pdf), [CS3-Testdatensatz, Z.4](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/lokomotive_cs3.cs2#L4), [Leseweg, Z.184](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/src/org/traincontrol/marklin/file/CS2File.java#L184).

Im Testdatensatz stehen für dieselbe Lok `.uid=0x4027`, `.mfxuid=0x73f1fcc5` und `.sid=0x27`. Die Werte sind ausschließlich ein fremdes Datenbeispiel. Sie zeigen, warum ein aus einer Oberfläche kopiertes Feld namens `uid` allein nicht als Masterseriennummer taugt.

## Konkrete Korrekturen gegenüber REV10

1. **F.2/S.76 und Quellenvermerk S.87: Krauß-Fundstelle ist jetzt überprüft.** Die Einschränkung, das separate Herstellerfeld auf S.39 sei nicht abschließend bestätigt, kann entfallen. 131 ist zusätzlich über die passende Märklin-Produktanleitung abgesichert. Der Verweis allein auf eine NMRA-Herstellerliste ist unnötig schwach.
2. **F.3/S.77: Der CS3-Datenweg ist nun konkret eingegrenzt.** Eine frisch gesicherte, eindeutig zugeordnete Lokdatei bleibt geeignet. Zusätzlich ist ein reiner HTTP-GET auf den bekannten Konfigurationspfad ein nachvollziehbarer Kandidat. Sein Erfolg und das tatsächliche Feldschema müssen protokolliert werden; ein Zugriff wurde hier nicht ausgeführt.
3. **Die 'Umrechnung offen' ist genauer zu formulieren.** Es fehlt kein beliebiger Zahlenzauber zwischen Märklin und ESU. Offen ist die Bestätigung, dass ESU im gewählten Software-/Firmwarepfad für diesen Master tatsächlich die gesamte mfx-UID erwartet und im Seriennummernfeld unverändert speichert. Die byteweise Speicherung selbst ist separat durch JMRI belegt.
4. **C.a/S.12: Ein unabhängiger Adressgeber garantiert keine andere SID.** Der Test wird erst mit zwei konkreten ungleichen SID-Werten bestanden. Zentralenwechsel, Neustart oder ein zweiter Lokname sind dafür keine Datenbelege.

## Die neue CS3-API-Falle

TrainControl unterscheidet im selben Quellstand ausdrücklich nach Version: unter 2.6 wird `/app/api/loks` verwendet, ab 2.6 `/app/api/locos` (CS2File.java, Z.300–307). Die vollständig ausgewertete Datei `test/CS3_loks_v260.json` enthält 154 Lokobjekte und 112 Vorkommen von `mfxuid`. Im ersten Objekt stehen zugleich `uid=0x4027`, `address=39` und `mfxuid=0x73f1fcc5`. Damit ist auch der aktuelle JSON-Pfad ein durch Implementierung und Testdaten gestützter Lesekandidat. Seine beiden UID-Felder haben jedoch unterschiedliche Bedeutungen. Ein erfolgreicher Abruf kann bei falscher Feldauswahl weiterhin die falsche Nummer für die Masterkopplung liefern. [Versionierte Pfadauswahl](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/src/org/traincontrol/marklin/file/CS2File.java#L300), [CS3-2.6-Testdaten](https://github.com/bob123456678/TrainControl/blob/5f0a75e33256c4c1b4ac1998134c4bd04030fed0/test/CS3_loks_v260.json).

Konsequenz: den vollständigen Rohdatensatz inklusive Feldnamen und Herkunft sichern. Das Feld nicht allein aufgrund seiner Beschriftung auswählen. Wo `.typ=mfx`, `.sid` und `.uid` vorliegen, kann die Beziehung `.uid = 0x4000 + .sid` als Konsistenzprüfung dienen; sie liefert nicht die dauerhafte Decoderidentität.

## Was die angenommene Identitätsabbildung stützt – und was noch fehlt

ESUs Anleitung verlangt die Masterseriennummer und eine Hersteller-ID; ihr Beispiel nimmt **151 für einen ESU-Master**. Sie beschreibt zwei LokSound 5 und garantiert weder 60977 noch das Lesen seiner Kennung mit LokProgrammer. [ESU Master/Slave-Synchronisation](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/).

Der originale Rohdatenversuch von nakott vom 13.03.2017, Beiträge 8/9, zeigt bei zwei ESU-V4-Decodern, dass die über deren RailCom-Informationsseite zusammengesetzte Seriennummer mit der über m3 ermittelten mfx-UID übereinstimmt. Das stützt die unmittelbare Identität der Nummern für ESU-V4, liefert aber ausdrücklich keinen DCC-Leseweg für Märklin 60977. [Originalmessungen](https://www.stummiforum.de/t147582f7-Wo-finde-ich-die-UID-eines-Lokdecoders.html).

Die on-track-Protokollanalyse beschreibt die Bind-Zuweisung mit vollständiger UID 32 und SID 14; dabei wird kein zusätzliches Herstellerbyte übertragen. Zusammen mit dem separaten manID-Feld stützt dies die Erwartung, dass eine rohe UID erhalten bleibt. Es beweist nicht, ob die geschlossene ESU-Firmware die Hersteller-ID zusätzlich als Freigabekriterium oder für RailComPlus verwendet. [Krauß S.22–23](https://www.skrauss.de/modellbahn/Schienenformat.pdf#page=22).

Die minimale verbleibende Nachweiskette lautet daher:

- Echter, eindeutig zugeordneter 60977-Rohdatensatz mit mfx-UID und SID; exakte CS3-Version und Dateiquelle.
- Offline-Projekt des genauen ESU-Modells: ein- und ausgeschaltete Synchronisation sowie gleiche Seriennummer bei Hersteller 151 und 131 exportieren; Unterschiede vollständig erfassen. Keine Annahme eines zusätzlichen Enable-CVs vorwegnehmen.
- Den numerischen Eingangswert und die exportierten vier Bytes nachweisbar vergleichen: `S = b0 + 256*b1 + 65536*b2 + 16777216*b3`. Ein Herstellerwechsel darf nur dann als bloßer CV191-Wechsel beschrieben werden, wenn der Export das tatsächlich zeigt.
- Erst nach gesichertem Istzustand und bestätigtem Prüfaufbau den funktionalen Versuch an genau 60977/59649 abnehmen. F0/Richtung bei Fahrstufe 0, Stromunterbrechung und dokumentierter SID-Wechsel gehören dazu.

Falsifiziert wäre die direkte Abbildung bereits durch einen ESU-Export, der aus derselben Eingabe bei 131 abweichende Seriennummernbytes erzeugt. Ein korrekter Export bei gleichzeitig fehlendem Slave-Folgen widerlegt hingegen nicht automatisch die Nummer: Protokollpriorität, Firmware, Enable-Wirkung, Zuordnung und Ausgänge müssen getrennt beobachtet werden.

## SID-Wechsel ohne Löschen der Lokdatenbank

Eine vorhandene MS2 mit passender eigener Gleisbox kann der unabhängige Adressgeber sein. Märklins aktuelle Anleitung für 60653/60657/66950/66955 nennt die zulässigen Gleisboxfamilien und trennt den eigenständigen Betrieb vom Anschluss als Bediengerät an eine CentralStation. Sie dokumentiert keine allgemeine, eindeutige Anzeige der mfx-SID in der MS2. Insbesondere 'MS2Information/Seriennummer' beschreibt die MS2, nicht den Decoder. [MS2-Anleitung, S.4,20–24](https://static.maerklin.de/damcontent/2a/47/2a470bed20017f68f92306725d49fca81702905959.pdf).

Ein technisch begründeter zusätzlicher Nachweisweg ist ein **passiver Mitschnitt der normalen Anmeldung auf dem CAN-Bus der unabhängig betriebenen MS2/Gleisbox**. Aus MFX-Bind mit gesetztem Responsebit und DLC 6 werden UID aus Datenbytes 0–3 und SID aus 4–5 in jeweils hoher-Byte-zuerst-Reihenfolge gelesen. Die Bind-Antwort dokumentiert jedoch nur das Ende der Befehlsausführung. Ein erfolgreicher Adresszustand erfordert zusätzlich nachgewiesene Anmeldung und Steuerbarkeit des Masters. Besonders eindeutig ist eine passiv mitgeschnittene positive MFX-Verify-Antwort für dieselbe UID und die gegenüber dem CS3-Datensatz andere SID: DLC 7 enthält zusätzlich das ASK-Verhältnis; eine negative Antwort setzt die SID auf 0x0000. Der Slave-Funktionstest bleibt separat erforderlich. Das normale Steuergerät soll Anmeldung und Verify auslösen; der Beobachter sendet keine eigenen Bind-, Verify-, Reset- oder Programmierkommandos. Das CAN-Protokoll gestattet allen Teilnehmern die Auswertung der Antworten. [Märklin CAN 2.0 S.28–29](https://wiki.rocrail.net/lib/exe/fetch.php?media=cs2%3Acs2can-protokoll-2_0.pdf).

Hierfür wäre zusätzlich ein bestätigter CAN-Lesezugang nötig, sofern keiner vorhanden ist. Ein geliehenes passives Interface genügt konzeptionell; ein weiterer Zentralenkauf ist nicht automatisch erforderlich. Die vorhandene CS3 muss beim MS2-Test vollständig aus dessen Stromversorgung und Steuerverbund herausgehalten werden. Ein Gleisbox-Reset oder Löschen der Lokliste ist für den Nachweis nicht erforderlich.

Falls die MS2 zufällig dieselbe SID zuweist, ist der Versuch für dieses Kriterium ergebnislos. Die korrekte Reaktion ist, die Gleichheit zu dokumentieren und einen anderen nachweisbaren Adresszustand vorzubereiten. Es wäre falsch, das Verhalten trotzdem als bestandenen Wechseltest zu bezeichnen oder durch willkürliches Ändern der CS3-Lokdaten eine künstliche Erfolgsmeldung zu erzeugen.

**Nicht als reine Lesehilfe übernehmen:** Das online auffindbare Raildue-Beispiel `Get_MFX_UID.ino` sendet in `SystemGo()` aktiv den Neuanmeldezähler, Protokollfreigabe und GO; beim Start zusätzlich ein weiteres Kommando. Es ist trotz seines Namens kein passiver UID-Leser. Es wurde nur gelesen und nicht ausgeführt. [Originalquellcode, Commit 4c5698d](https://github.com/gelit/Raildue/blob/4c5698ddb7332826872530fc61ee774fe9c4e82e/examples/Get_MFX_UID/Get_MFX_UID.ino).

## Bewertung und nächste konkrete Datenaufnahme

Die bisherige Begründung, ohne Händler oder eigenen LokProgrammer komme man an dieser Stelle nicht sinnvoll weiter, ist zu stark. **Als nächster Schritt reicht ein eindeutig zugeordneter CS3-Rohdatensatz des 60977**, ergänzt um die tatsächlichen Geräte-/Softwareangaben. Damit lassen sich Herkunft, Zahlenformat und die konkrete Bytezerlegung vorbereiten. Parallel kann die kostenlose LokProgrammer-Software die noch fehlende Offline-Abbildung klären. Ein Hardwarekauf ist erst anhand der verbleibenden Lese-, Firmware- oder Testlücke zu bewerten.

Die Dokumentationslücken bei Herstellerkennung und CS3-Format sind substanziell verkleinert. Offen bleiben die individuelle UID, die getestete ESU-Eingabeabbildung und die reale Paarabnahme einschließlich anderer SID. Diese Punkte lassen sich durch kurze, konkrete Nachweise schließen; sie rechtfertigen weder erfundene CV-Werte noch einen pauschalen Abbruch des CS3-Wegs.
