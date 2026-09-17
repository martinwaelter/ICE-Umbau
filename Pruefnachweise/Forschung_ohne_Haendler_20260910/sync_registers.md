# JMRI- und Originalquellenprüfung: Synchronisationsregister LokPilot 5

Stand: 10.09.2026. Teilprüfung ausschließlich Quellen und Softwaredefinitionen; keine Decoderkommunikation, kein Hardwaretest, keine reale Schreibfreigabe. Händlerweg ist nach Nutzerangabe nicht verfügbar.

## Ergebnis

Die Zuordnung der fünf Kandidatenregister ist auf Ebene der JMRI-Implementierung belastbar und reproduzierbar: unindiziertes CV191 enthält das Feld `M4MfgId`; CV192–195 enthalten `M4SerNo`, niederwertigstes Byte zuerst. Die Definition gilt durch gemeinsame Einbindung auch für das Modell LokPilot 5 MKL. Das löst Zuordnung und Bytefolge, aber nicht automatisch die gesamte ESU-Enable-Logik.

Der präzise offene Punkt ist nicht „CV-Programmierung generell unbelegt“, sondern: Welche CV-Werte schreibt eine passende originale LokProgrammer-5-Projektkonfiguration beim Aktivieren bzw. Deaktivieren des Synchronisationshakens, insbesondere bei bereits eingetragener Herstellerkennung/Seriennummer? JMRI besitzt für diesen Haken weder eine eigene Variable noch eine eigene Checkbox. „CV191 ungleich 0 aktiviert; 0 deaktiviert“ bleibt daher bis zum Originalvergleich eine plausible, nicht bestätigte Hypothese.

## 1. Unveränderte Definition zwischen REV10-Pin und aktuellem Stand

REV10-Pin: `32eca6cddc18a55f2efdfdbc970cca96b7511827`.
Aktuelles `master` wurde per GitHub-Tree-API auf `31e482094d472e481c1fb54f9901093c2efbfcec` aufgelöst. Beide Trees wurden vollständig geliefert (`truncated=false`). Die folgenden sieben Dateien wurden über ihre unveränderlichen Raw-URLs in beiden Ständen geladen; ihre SHA-256-Hashes sind paarweise identisch:

| Datei innerhalb JMRI | SHA-256 in beiden Ständen |
|---|---|
| `xml/decoders/ESU_LokPilot5.xml` | `862ba7341e9e9d423387291ff95e90342eeb806372528ba3cacb67e676092036` |
| `xml/decoders/esu/v5standardCVs.xml` | `db2f1b72328f6749795cd084935d53899b26379f85004d5854fbc4ee6538f7ee` |
| `xml/decoders/esu/v4advancedPane.xml` | `96899b066829426debb37a7875278dd08cfcccbd5bd572477c965c3155de63c5` |
| `xml/decoders/esu/v4decoderInfoCVs.xml` | `47660f3111b8003857bbc8d5935ac452775e975c0a05d6c3eaee55cff51a901f` |
| `java/src/jmri/jmrit/symbolicprog/SplitVariableValue.java` | `43f9aed713ca492b7b31c2d940c0a86dfd82fbf6eaf6fba4ee406cca014e2a71` |
| `java/src/jmri/jmrit/symbolicprog/SplitHexVariableValue.java` | `f26ab89c122d0fcbdf67a18fdde484636be2d361245a36c94eb40054721f8b9a` |
| `java/src/jmri/util/CvUtil.java` | `b55464a38603e0058accd4e705e4e680c1c6b913577a061e775c4ca804685934` |

[Tree REV10-Pin](https://api.github.com/repos/JMRI/JMRI/git/trees/32eca6cddc18a55f2efdfdbc970cca96b7511827?recursive=1), [Tree aktueller Pin](https://api.github.com/repos/JMRI/JMRI/git/trees/31e482094d472e481c1fb54f9901093c2efbfcec?recursive=1).

## 2. Modell- und Feldzuordnung

In `ESU_LokPilot5.xml` stehen LokPilot 5 in Zeilen 42–45 und LokPilot 5 MKL in Zeilen 186–188. Zeile 246 bindet `v5standardCVs.xml` für die Familie ein; Zeile 256 das gemeinsam benutzte Advanced-Panel. Es gibt keine eigenständige Datei `ESU_LokPilot5_MKL.xml`; eine solche URL liefert 404.

[Modellfamilie und MKL](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/ESU_LokPilot5.xml#L186), [Einbindungen](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/ESU_LokPilot5.xml#L245).

In `v5standardCVs.xml`, Zeilen 993–1017, ist nur Essential Sound Unit ausgeschlossen. CV191 ist `M4MfgId`, Standardwert 0. `M4SerNo` steht in `CV="192:4"` mit hexadezimaler Darstellung. Beide Felder sind hier weder als readOnly markiert noch von einer Firmwaregrenze abhängig. Das ist ein Nachweis dafür, wie JMRI sie behandelt; es ist kein Herstellerzertifikat für sämtliche Decoder-/Firmwarevarianten. Einige übersetzte Tooltips nennen fälschlich „Dekoderversion“, während Item und englischer Feldname die Seriennummer bezeichnen; für die Auswertung sind Item und Registerstruktur maßgeblich.

[CV-Definition aktueller Pin](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v5standardCVs.xml#L993), [gleiche Definition REV10-Pin](https://github.com/JMRI/JMRI/blob/32eca6cddc18a55f2efdfdbc970cca96b7511827/xml/decoders/esu/v5standardCVs.xml#L993).

## 3. Bytefolge ist aus ausführendem Code geklärt

`CvUtil.expandCvList` interpretiert einen positiven Doppelpunktzähler als aufsteigende Registerfolge (Zeilen 44–49, 102–120). Somit wird `192:4` zu 192, 193, 194, 195.

`SplitHexVariableValue` erbt von `SplitVariableValue` (Zeile 20). Dessen Konstruktor ordnet den CVs aufsteigende Bitpositionen zu (Zeilen 95–128). Schreiben und Rückzusammensetzen erfolgen mit den jeweiligen Bitverschiebungen (Zeilen 350–378). Ergebnis der JMRI-Interpretation:

`Seriennummer = CV192 + 256·CV193 + 65536·CV194 + 16777216·CV195`.

Dies ist eine Softwareinterpretation, keine Aufforderung, Register am Decoder zu ändern. Dezimale Anzeigewerte dürfen nicht als hexadezimale Eingabe behandelt werden; führende Nullen einer 32-Bit-Kennung sind für die eindeutige Darstellung mitzunehmen.

[CvUtil](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/util/CvUtil.java#L102), [SplitHex-Vererbung](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/jmrit/symbolicprog/SplitHexVariableValue.java#L20), [Bitzuordnung](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/jmrit/symbolicprog/SplitVariableValue.java#L95), [Zerlegung/Zusammensetzung](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/jmrit/symbolicprog/SplitVariableValue.java#L350).

## 4. Enable-Logik: was gefunden wurde und was nicht

Das Advanced-Panel stellt unter der Überschrift zur RailComPlus/M4-Synchronisation nur `M4MfgId` und `M4SerNo` dar (Zeilen 47–60). Es existiert an dieser Stelle keine Aktivierungscheckbox, kein Action-Element und keine Aktivierungsbedingung. Eine Textsuche aller 56 Dateien im Unterordner `xml/decoders/esu/` nach M4MfgId, M4SerNo, Synchronisation und CV191 fand nur diese Panel-/Variablendefinitionen sowie ein sachfremdes V3-Funktionsmapping.

[Advanced-Panel](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4advancedPane.xml#L47).

Die Historie präzisiert die Herkunft: Commit `7d14c2747c788c1cf49eb599ddea0fd15d4b58fa` vom 10.04.2020 fügte zusammen mit LokPilot-5-Unterstützung genau diese zwei Felder hinzu. Zugehöriger PR 8317 enthält keine technische Erläuterung des Enable-Verhaltens; seine Kommentare betreffen CI-Wiederholungen. Der spätere PR 9961 liefert hierzu ebenfalls keinen weiteren Nachweis. Die Definition ist also seit 2020 vorhanden, nicht erst im aktuellen Forschungsstand erfunden.

[Einführungscommit](https://github.com/JMRI/JMRI/commit/7d14c2747c788c1cf49eb599ddea0fd15d4b58fa), [PR 8317](https://github.com/JMRI/JMRI/pull/8317), [PR 9961](https://github.com/JMRI/JMRI/pull/9961).

Bewertung: Das Fehlen eines gesonderten JMRI-Schalters und der Default 0 passen zur Hypothese einer impliziten Aktivierung durch gesetzte Kennung. Sie schließen aber weder einen in JMRI fehlenden Schalter noch zusätzliche Abhängigkeiten von Seriennummer oder Protokoll aus. Deshalb keine Null-/Nichtnull-Regel als bestätigte Tatsache ausgeben.

## 5. Firmwaredefinition und abweichende Identitäten

Die tatsächliche ESU-eigene Seriennummer wird in JMRI separat als readOnly `SerNo` aus dem indizierten Bereich `0.255.265:4` erfasst. Das ist ausdrücklich ein anderes Feld als der beschreibbare Masterverweis in CV192–195.

`v4decoderInfoCVs.xml` definiert außerdem den Firmware-Build über `0.255.285:2`, Minor über `0.255.287`, Major über `0.255.288`; die zusammengefasste Version steht in `0.255.285:4`. Alle diese Felder sind im geprüften aktuellen und REV10-Stand readOnly. Die Notation bezeichnet CV31=0/CV32=255 mit Register 285ff. Die bloße JMRI-Definition ermittelt noch keine tatsächlich installierte Firmware.

[Identität](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml#L26), [Firmware](https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/xml/decoders/esu/v4decoderInfoCVs.xml#L59).

ESU nennt die Einführung der Synchronisation für LokSound 5 mit Firmware 5.1.101; LokPilot-5-Unterstützung erscheint in Software 5.0.11 mit Firmware 5.1.105. Daraus folgt kein am konkreten LokPilot überprüfter Mindeststand. Die reine Existenz neuerer Software auf dem PC sagt nichts über die Firmware des eingebauten Decoders.

[ESU-Releasehistorie](https://www.esu.eu/download/software/lokprogrammer/), [ESU-Synchronisationsbeschreibung](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/).

## 6. Suche nach Originalexporten und Praxisdateien

Gezielte Web- und GitHub-Issue-Suchen nach CV191/CV192, M4MfgId sowie Master-Synchronisation fanden keinen öffentlich zugänglichen, gepaarten Originalexport „aus/an“ für die fragliche Funktion. Dieses Negativergebnis beschreibt den geprüften Suchraum; es behauptet keine globale Nichtexistenz.

Ein Benelux-Forenbeitrag enthält einen real berichteten LokPilot-5-CV-Dump mit Firmwareangabe 5.6.143 und CV191–195 sämtlich 0. Er ist kein gepaarter Aktivierungstest und kein ESU-Primärbeleg; aus ihm folgt daher keine Enable-Regel.

[Benelux: Worstelen met de ESU LocPilot/LocSound 5 decoders](https://forum.beneluxspoor.net/index.php?topic=103356.0).

Im Stummiforum-Thema vom 13.02.2026 steht ein konkreter Originalprojekt-Dateianhang `3642-4257.zip`. Die öffentliche Ansicht zeigt jedoch ausdrücklich eine Rechtebeschränkung und nur den Dateinamen. Der Inhalt wurde nicht abgerufen; kein Umgehen der Zugriffsbeschränkung. Außerdem betrifft der Bericht LokPilot 5 + LokPilot 5 Fx und einen zunächst ungeeigneten Test am LokProgrammer bzw. reinen DCC-Betrieb an der CS3. Er bestätigt weder das gemischte mSD3-Paar noch die fragliche CV-Enable-Logik.

[Stummiforum: Synchronisation geht nicht, Beiträge 1–6](https://www.stummiforum.de/t242098f5-ERLEDIGT-ESU-LokPilot-RailComPlus-Master-Decoder-Synchronisation-geht-nicht.html).

## 7. Minimaler nächster Nachweis für die Softwarelücke

Eine reproduzierbare Offline-Differenzprüfung in originaler LokProgrammer-5-Software kann die Restlücke ohne Gleisspannung klären:

1. Passenden LokPilot-5-/MKL-Projekttyp und Softwareversion dokumentieren; eindeutige synthetische Kennung nur im Offlineprojekt benutzen.
2. Export für Synchronisation aus und für an bei identischer Kennung vergleichen; danach wieder ausschalten und nochmals vergleichen.
3. Kontrollieren, ob nur CV191 zurückgesetzt wird, alle fünf Register geändert werden oder zusätzlich andere Register/Indexbereiche betroffen sind. Auch „an, Kennung noch leer“ separat betrachten.
4. Bytefolge mit einer synthetischen, nicht symmetrischen 32-Bit-Kennung vergleichen; so lässt sich die JMRI-Interpretation unabhängig an ESU-Output überprüfen.
5. Vollständigen Vorher-/Nachher-Export sichern, weil eine Liste geänderter CVs beim Speichern zurückgesetzt wird und sonst irreführend leer sein kann.

Die Register-/Enable-Frage wäre mit diesem Originalsoftwarevergleich entscheidbar. Davon getrennt bleiben reale Masteridentität, installierte Firmware, elektrische Messfreigabe, kontrollierte CS3-Programmierung und erfolgreicher Synchronisations-/Adresswechseltest offen. Diese Teilprüfung enthält daher bewusst keine reale Schreibkarte.

[ESU: Funktionsweise der Änderungsliste](https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/).
