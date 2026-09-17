"""Integrate the CS3-CV findings into the existing complete manual, without changing REV7."""
from reportlab.platypus import Paragraph
import rev7_closed

CHANGES = [
('Bewahre die Fotos und die beiden ausgelesenen Decoderprojekte zusammen mit dieser Seite auf.', 'Bewahre Fotos, Märklin-Ausleseprojekt, ESU-CV-Altwert-/Rückleseprotokoll und Offline-Projekt samt geprüftem Export zusammen auf. Ein vollständig ausgelesenes ESU-Projekt nur beim optionalen Programmerweg ergänzen.'),
('die beiden Firmwarestände und die ausgelesene ESU-Sonderoption sichern;', 'die Firmwarestände und das CS3-CV-Rückleseprotokoll bzw. die optional ausgelesene ESU-Sonderoption sichern;'),
('Über den ESU-Zugang wieder auslesen.', 'Mapping-CVs per CS3 rücklesen (F.6); optional ESU-Programmer nutzen.'),
('Konkrete Arbeitsfassung für deinen ICE 2976 und deine vorhandenen Bauteile', 'Vollständige Arbeitsfassung mit ergänzter CS3-CV-Anleitung in Kapitel F'),
('Diese Fassung ersetzt die Arbeitsanweisungen der REV6; REV6 bleibt als Vergleich erhalten.', 'REV8 erhält den vollständigen Umfang der REV7 und ergänzt Kapitel F zur CS3-CV-Programmierung. Kapitel F hat eigene Quellennummern. REV7 bleibt unverändert erhalten.'),
('1 Zugang: ESU 53451','ESU 53451: optional'),
('LokProgrammer samt unterstützter Windows-Software; eigener, geliehener oder Händlerzugang.', 'Optionaler Hardwarezugang. CS3-CV-Weg nach F; vorerst keine Kaufpflicht.'),
('Für den beschriebenen ESU-Weg; Programm- und Firmwarestände protokollieren.', 'Für Offline-CV-Export nach F.5 oder optionalen ESU-Hardwareweg; Softwarestand notieren.'),
('Gemeinsamer mfx-Betriebstest; keine zweite Zentrale parallel einspeisen.', 'DCC-CV-Lesen/Schreiben nach F.4/F.6 und mfx-Test; keine parallele zweite Einspeisung.'),
('Für den Vorabtest: 60971 nur am 60977; ESU-Zugang zuerst beschaffen', 'Vorabtest: CS3-CV-Weg zuerst prüfen; 60971 nur am 60977'),
('Lege den 60977 und den 59649 getrennt in ihre Verpackungen. Den 59649 nicht auf den Märklin 60971 stecken. Hast du keinen Zugang zu 53451 und zwei bestätigten Prüfaufnahmen, gib beide Decoder samt Kapitel A-C einem entsprechend ausgestatteten Fachbetrieb. Dort müssen die Gleiseingänge aus genau einer CS3 versorgt werden; Motor-, Licht-, Lautsprecher- und Plusanschlüsse der Decoder bleiben getrennt. Keine LED oder Drahtlast selbst als Prüfaufnahme improvisieren.',
 '60977 und 59649 getrennt halten; den 59649 nicht auf den Märklin 60971 stecken. Zuerst den CS3-Leseweg nach F.4 und den Offline-Export nach F.5 klären. Fehlen geeignete Prüfaufnahmen, beide Decoder samt A-C und F einem Fachbetrieb geben. Nur eine CS3 speist die Gleiseingänge; Motor-, Licht-, Lautsprecher- und Plusanschlüsse bleiben getrennt. Keine LED oder Drahtlast als Prüfaufnahme improvisieren. Fehlender 53451-Zugang allein verlangt keinen Kauf.'),
('Am 53451 nur den 59649 in geeigneter Prüfaufnahme einlesen. Typ und Firmware prüfen, Einstellungen als Projekt sichern. Unter Decoder / Sonderoptionen muss die Master-Decoder-Synchronisation für den tatsächlich eingelesenen Decoder vorhanden sein. Fehlt sie oder scheitert Auslesen/Quittierung: stoppen; nicht beliebige CVs schreiben.',
 'Nur den 59649 in bestätigter Prüfaufnahme untersuchen. CS3: F.4 zuerst nur lesen, Altwerte sichern; CV191-195 sind über JMRI zugeordnet. Aktivierung und reale Firmware sind damit nicht freigegeben. Optional am 53451 vollständig einlesen und Projekt sichern. Fehlt die Sonderoption oder scheitert Quittierung, nicht schreiben. Den zusätzlichen Aktivierungsnachweis nach F.5 durchführen.'),
('M4 aktiv lassen; bestätigte Masterdaten in die Sonderoption übernehmen, Einstellungen schreiben und anschließend erneut auslesen. Werte und aktivierte Option vergleichen. Keine Sounddatei eines anderen Herstellers aufspielen. Gemeinsame DCC-Adresse ist kein Ersatz für den mfx-Nachweis.',
 'Erst nach belegten Masterwerten UND Aktivierungsfolge eine individuelle Schreibkarte freigeben. M4 aktiv lassen. CS3-Einzelwertprogrammierung mit frischem Rücklesen nach F.6; alternativ bestätigte ESU-Sonderoption verwenden. Keine fremden Sounddateien und keine gemeinsame DCC-Adresse als Ersatz. CV191 = 131 oder = 0 nicht ungeprüft als Start/Reset schreiben.'),
('Zusätzlich: Zugang zum ESU 53451 mit Windows-PC und geeigneten Prüfaufnahmen nach Kapitel A.', 'Zusätzlich: CS3-CV-Weg und Offline-Export nach F; 53451 optional, geeignete Prüfaufnahmen nach A weiterhin erforderlich.'),
('ESU-Zugang; tatsächliche Firmware; belegte Masterdatenübernahme; ausgefülltes C-Protokoll', 'CS3-Lesezugang; Firmware; Masterwerte und Aktivierung nach F; bestandenes C-Protokoll'),
('Datum, Programmerzugang, Identitätsnachweis, Testergebnis: __________________', 'Datum, CS3-/Programmierweg, Identität, Aktivierung, Testergebnis: __________________'),
('Die eigentliche Identitätsübernahme sowie die unbekannten Revisionen werden nicht durch Formulierungen ersetzt.', 'Kapitel F ergänzt den CV-Nachweis; Masterabbildung, Aktivierung und unbekannte Platinenrevisionen bleiben bis zum Nachweis offen.'),
]

def install(ns):
    rev7_closed.install(ns)
    old_p=ns['p']
    hits={before:0 for before,_ in CHANGES}
    def revised(text,style='body'):
        paragraph=old_p(text,style)
        updated=paragraph.text
        for before,after in CHANGES:
            if before in updated:
                hits[before]+=updated.count(before)
                updated=updated.replace(before,after)
        updated=updated.replace('REV7','REV8') if 'REV7 konkretisiert' in updated else updated
        if updated==paragraph.text:
            return paragraph
        return Paragraph(updated,paragraph.style)
    ns['p']=revised
    ns['REV8_HITS']=hits
