# ICE 2976 - Abschlussprüfung der Dokumentüberarbeitung REV10

Stand: 10.09.2026.

**Ergebnis: Dokumentüberarbeitung abgeschlossen. Keine Hardware-, Synchronisations- oder Betriebsfreigabe.**

## 1. Eindeutiger Prüfgegenstand

| Merkmal | Endstand |
|---|---|
| Datei | `output/pdf/ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf` |
| PDF-Seiten | 92 |
| Kapitel-/Abschnittsziele und PDF-Lesezeichen | 78 |
| Interne Link-Annotationen | 230; mehrere Annotationen können zum selben Kapitel gehören |
| SHA-256 | `2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0` |
| Praktische Prüfungen am Zug | Keine |
| Schreibzugriffe auf Decoder/CS3 | Keine |
| Käufe / Herstelleranfragen | Keine |

Die drei letzten Seiten enthalten die Schnellanleitung. Vollanleitung, Bilder, grafische Schalt-/Prüfdarstellungen, CS3-Kapitel und Nachweiskarten bleiben zusammen in einer PDF.

## 2. Technische Dokumentkontrollen

Die erzeugte Datei wurde erneut geöffnet, ausgelesen und vollständig gerendert. Die Prüfzahlen wurden an der Enddatei ermittelt, nicht aus einer früheren Revision übernommen.

| Prüfung | Ergebnis und Aussagegrenze |
|---|---|
| PDF lesbar und renderbar | Alle 92 Seiten erfolgreich verarbeitet. Kein bloßer Dateiexistenztest. |
| Interne Linkziele | Alle 230 Annotationen zeigen auf vorhandene Zielseiten. |
| Sichtbarer Linktext gegen Ziel | Alle 230 geprüften Beschriftungen bzw. Inhaltsverzeichnis-Seitenzahlen passen zum Zielkapitel bzw. zur Zielseite. |
| Originalbilder | Alle elf bisherigen Bildvorkommen erhalten; Vergleich der dekodierten PDF-Bilddaten per SHA-256. Die Vollständigkeit von grafischen Markierungen wurde zusätzlich visuell betrachtet. |
| Originale Kapitelbereiche | Keine bisherigen Abschnittsfamilien verloren. Die frühere Sammelkarte E wurde bewusst durch E1/E2/E3 ersetzt, die Titelseite umgeschrieben. |
| Textgrenzen | Kein maschinell festgestellter Text außerhalb der festgelegten Seitenränder. Das allein wäre noch kein Überlagerungstest; deshalb zusätzliche Sichtprüfung. |
| Veraltete kritische Formulierungen | Gezielte Negativsuche ohne Treffer, unter anderem falsche schwarze Messleitung, „ungekuppelten Dummy abkoppeln“, bereits geschlossene Registerlücke und falsche REV10-Herkunft. |
| Quellenverweise | Im Dokument erhalten und relevante Hersteller-/Implementierungsbelege im Korrekturlauf abgeglichen. Kein vollständiger erneuter Erreichbarkeitsnachweis jeder externen URL behauptet. |
| Ausgangsdateien | REV9-PDF und ursprünglicher Prüfbericht unverändert erhalten. |

Original-PDF SHA-256: `c1c1b1a2772f0e25385ffe911041b1cd2f7351277ada2ed5d8ecbe1be0070d29`.

Original-Prüfbericht SHA-256: `efb6ba4a3f84b1519b11bf4e1e1a122f0ab910a1ff729f7b6dd09a1e1a3e0554`.

## 3. Tatsächlich durchgeführte Sicht- und Gegenprüfung

Drei getrennte KI-Teilinstanzen überprüften Fachbereiche und später sämtliche gerenderten Seiten. Sie arbeiteten innerhalb desselben Projekts; das war keine Blindprüfung und kein Gutachten dreier menschlicher Elektrotechniker.

1. **Erste vollständige Satzprüfung:** 98-seitiger Zwischenstand, aufgeteilt in Seiten 1–32, 33–64 und 65–98. Alle Seiten tatsächlich als Bilder angesehen. Zusätzlich wurden gefährdete Handgriffübergänge und zusammengeführter Text geprüft.
2. **Zweite vollständige Satzprüfung:** 92-seitiger Stand mit SHA-256 `cd550ebb25e5ecdb58ef55b7e51948f2401ff4006a4ef42f7e1f27542a6ef13a`, aufgeteilt in Seiten 1–30, 31–60 und 61–92. Wieder alle Seiten tatsächlich als Bilder angesehen. In dieser Runde blieben nur ein Richtungswort in einer verschobenen Warnbox und ein ungünstiger Umbruch in Kapitel 17.
3. **Endkorrektur:** „oben beschriebene“ zu „nachfolgende Steckkontrolle“ auf S. 29. Kapitel 17 auf S. 56–57 in Motorprüfung und hinteren Kopf/Wagenprüfung aufgeteilt. Seitenzahl und sämtliche Kapitelstartseiten unverändert.
4. **Nachprüfung der Enddatei:** Erneuter vollständiger Renderlauf und automatische Prüfung. Der Seiten-Textvergleich bestätigt, dass nur S. 29, 56 und 57 gegenüber Runde 2 verändert sind. Diese drei Seiten wurden in der letzten Fassung zusätzlich als Einzelbilder durch die Hauptinstanz und eine getrennte Teilinstanz kontrolliert; beide fanden keinen abgeschnittenen Inhalt oder neuen Ablaufbruch. Die Teilinstanz bestätigte die Endprüfsumme erneut.

Die Sichtprüfung fand nach den Korrekturen keine verbliebenen konkreten abgeschnittenen Warnzeichen, Textüberlagerungen oder unvollständigen Tabellen. Das ist ein dokumentbezogenes Prüfergebnis, keine Zusage absoluter Fehlerfreiheit.

## 4. Korrekturen aus der Schlussprüfung

- Unnötige Quellen-Nachläufer in B, 8, 9, 9a, 12 und 16 ohne Inhaltskürzung beseitigt.
- Vollständigen Warnrahmen, Ausrufezeichen und Vergrößerung des Hersteller-Steckbildes erhalten.
- Sicherheitskästen zum Einsetzen und zur Einmessfahrt vor die Handgriffe gestellt.
- Fortsetzungsseiten mit zugehörigem Kapitel gekennzeichnet.
- Historischen Quellenbezug auf REV9 wiederhergestellt.
- Rückkehr zum sicheren Programmieraufbau nach Vorbereiten einer fehlenden CV-Zeile ergänzt.
- Bezeichnungen für Prüfleitungsenden und Prüfpersonen auseinandergehalten.
- Einsetz-/Abnahmeschritte entkoppelt: E1 vor Einsetzen, tatsächlicher Sitz nach Einsetzen vor Strom, Ergebnisse erst in E2/E3.
- Vorzeitige Licht-/Fahrtests aus den Montage-/Sollwertschritten entfernt; notwendige Lastplanung vor die jeweiligen Tests gestellt.

Die vollständige Rückverfolgung aller R- und W-Punkte steht in [Änderungen und Prüfstatus](</Users/martinwaelter/ICE Umbau/ICE2976_REV10_AENDERUNGEN_UND_PRUEFSTATUS.md>).

## 5. Nicht durch die Dokumentprüfung erledigt

| Offener Bereich | Warum die Anleitung hier keine Freigabe vortäuscht |
|---|---|
| mfx-Synchronisation 60977 + 59649 | Tatsächliche Masterkennung/Übernahme, Aktivierung, Firmware und reproduzierbarer Test einschließlich neuer SID fehlen. |
| CS3-Programmierung | Konkreter Geräte-/Softwarestand, verlässlicher Leseweg des Aufbaus und Verhalten bei CV-Zeilenanlage noch nachzuweisen. |
| LoDi-511-Montage und Steckfeld | Reale Rückseite/Revision, elektrische Ringzuordnung, SW/RT-Pfad, GE-Auswahl und Indexstruktur noch nicht vollständig belegt. |
| Hinterer Kopf | Eigener Schleifer, Radkontakt, Halter und Verbindungspunkte am konkreten 2976 noch nicht dokumentiert. |
| LED-Widerstände und bestückte Netze | Echte LED-Zweigdaten, sichere Messpunkte, geeignete Geräteparameter und zulässige Anzeigen fehlen. Beispielrechnungen sind keine Stücklistenfreigabe. |
| Kupplungen, Wagenzahl und Flackern | Reale 2976-Passung, Kontakttragfähigkeit, Last-/Spannungsabfall- und Funktionsprüfungen stehen aus. Richtungsunabhängige Beschaltung allein beweist keine Störungsfreiheit aller Kontakte. |
| 60974 und Signalhalt | Gesonderte Anschluss-/Systemprüfung nötig. Beide Speicher bleiben in dieser Phase abgetrennt. |

**Empfohlene nächste Welle:** G0 ohne Zugdemontage schließen; zunächst die dokumentierten Identitäts- und Offline-Exportnachweise sowie den sicheren Prüfaufbau klären. Keine Teile auf Verdacht bestellen und keine ungeprüften CV-Beispielwerte schreiben.

## 6. Ablage und Nachvollziehbarkeit

Alle neuen Dateien liegen lokal unter `/Users/martinwaelter/ICE Umbau`. Die aktuellen Unterlagen sind in [START_HIER](</Users/martinwaelter/ICE Umbau/START_HIER.md>) verlinkt.

Die lokalen Bearbeitungsquellen und Originalbilder liegen in `Arbeitsstand_REV10/`; dokumentbezogene Mess-/Renderprotokolle und Prüfabbildungen in `Pruefnachweise/REV10_Abschluss/`. Historische Originale sind nicht überschrieben. Aus der Existenz dieser Unterlagen folgt kein real ausgeführter Umbau.
