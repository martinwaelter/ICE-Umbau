from pathlib import Path
from copy import deepcopy
import sys, json, re, hashlib
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent
REV13 = PROJECT / 'Arbeitsstand_REV13'
sys.path.insert(0, str(ROOT))
sys.path.insert(1, str(REV13))
from layout import Layout

ALL = {p['n']: deepcopy(p) for p in json.loads((REV13 / 'rev13_pages.json').read_text())}

# REV13 is the corrected LoDi baseline. Keep only the action cards needed for
# the complete 2976 conversion; duplicate background cards stay out.
ORDER = [1, 2, 3, 5, 15, 16, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28,
         29, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46]
MAP = {old: new for new, old in enumerate(ORDER, 1)}

def rewrite(value):
    if isinstance(value, str):
        value = value.replace('REV13', 'REV15')
        value = value.replace('ESU 59649', 'Märklin 60972')
        value = value.replace('59649', '60972')
        value = value.replace('ESU-Änderung', '60972-Änderung')
        value = value.replace('ESU auf', '60972 auf')
        value = value.replace('ESU/NEM-Orange', 'Decoder/NEM-Orange')
        value = value.replace('Der ESU sitzt auf dem separaten leeren Träger aus dem 60977-Satz.', 'Der 60972 sitzt auf der LoDi-511-21MTC-Aufnahme.')
        value = value.replace('ESU-Unterlagen für andere Fx-micro-Modelle', 'Fremddecoder-Unterlagen für andere Fx-micro-Modelle')
        def ref(m):
            n = int(m.group(1))
            return f'[[{MAP[n]}]]' if n in MAP else 'dem nächsten Arbeitsschritt'
        return re.sub(r'\[\[(\d+)\]\]', ref, value)
    if isinstance(value, list):
        return [rewrite(x) for x in value]
    if isinstance(value, dict):
        return {k: rewrite(v) for k, v in value.items()}
    return value

pages = []
for new, old in enumerate(ORDER, 1):
    p = rewrite(deepcopy(ALL[old]))
    p['n'] = new
    p['source_card'] = old
    pages.append(p)

# Scope and inventory are deliberately concrete: no LoDi/Originalplatine mix.
p = pages[0]
p['title'] = 'Märklin ICE 1 2976 mit LoDi – Umbau Schritt für Schritt'
p['phase'] = 'START | SCOPE'
p['goal'] = ('Diese kompakte Ausgabe führt den vollständigen Umbau aus: Hochleistungsmotor, '
             'LoDi-Motorplatinen 512/511, LoDi-514-Frontlicht, Wagenlicht, stromführende Kupplungen, '
             '60977/60972-Decoder und richtungsabhängiger Lichtwechsel. Standard ist die reversible '
             'Paralleleinspeisung beider Schleifer für maximale Stromaufnahme; die Schleiferumschaltung '
             'bleibt als getrennte spätere Option dokumentiert. Jeder Schritt endet mit einer Prüfung.')
p['before'] = ('Geltungsbereich: der Märklin ICE 1 aus Startpackung 2976. Die rote LoDi-Motor WiB ICE-M-S '
               '(Art.-Nr. LoDi-512) gehört in den motorisierten Kopf. Im Grundaufbau wird ihre Umschaltfunktion '
               'nicht aktiviert: Vorderer und hinterer Schleifer werden über den RT-Rohstrombus parallel geführt. '
               'Die LoDi-Motor WiB ICE-M (Art.-Nr. LoDi-511) gehört in den motorlosen Gegenkopf. Zwei LoDi-514 '
               'werden als Frontlicht eingesetzt. Für jeden Innenwagen wird eine eigene LoDi-WiB ICE1-M '
               '(LoDi-510) benötigt; das Bordrestaurant braucht ebenfalls die dafür passende LoDi-Wagenplatine. '
               'Die 2976-Fotos und Zeichnungen bleiben Vergleichsmaterial; '
               'vor jedem Eingriff die eigene Platine, Halter und Kupplung fotografieren.')
p['blocks'] = [
    {'type':'figure','kind':'system','maxh':168,'after':5},
    {'type':'small','text':'<b>Reihenfolge:</b> öffnen → Motor/HLA → LoDi-512 → Frontlicht → LoDi-511 → RT/GE-Kupplungen → Decoder → Wagenplatinen je Wagen → Einzeltest → Endabnahme.','after':4},
    {'type':'note','label':'STOPPREGEL','tone':'stop','text':'Bei Kurzschluss, unklarer Platinenrevision, falscher Lichtfarbe oder klemmender Kupplung nicht weiterlöten. Erst die betroffene Karte und die Messung klären.','after':0},
]

p = pages[1]
p['title'] = 'Teile und Geräte vor dem Öffnen abhaken'
p['before'] = ('Vorhanden laut Bestand: 1× LoDi-512 ICE-M-S, 1× LoDi-511 ICE-M, 1× Satz LoDi-514 Front '
               '(2 Stück), Märklin 60977, Märklin 60972, Märklin 60982 (Reserve mit 8-poligem Kabelbaum), '
               'Märklin 60971 Programmer, Märklin 60941, '
               'Märklin 78792 Bordrestaurant, Multimeter und CS3 mit aktueller Firmware. Für jeden Innenwagen '
               'wird 1× LoDi-510 benötigt; die tatsächlich benötigte Anzahl wird am Zug W1…Wn gezählt. Für jeden '
               'Wagenübergang werden '
               '2× Märklin E395640 am Triebkopf sowie E374060 + E374340 für die Wagenübergänge. '
               'Pro Übergang werden zwei getrennte Kupplungspole RT und GE benötigt.')
p['blocks'] = [
    {'type':'table','headers':['Baugruppe','Benötigt','Vorher prüfen'],'widths':[1.2,2.1,1.7], 'rows':[
      ['Motor','Märklin 60941 HLA','5-polig, Bürstenfahnen frei'],
      ['Motor-Kopf','LoDi-512 / 60977','Aufdruck, 21MTC, SW/SJ'],
      ['Gegenkopf','LoDi-511 / Märklin 60972','21MTC-Platine, LED-Pads'],
      ['Frontlicht','2× LoDi-514','Weiß/Rot/Plus markieren'],
      ['Innenwagen','1× LoDi-510 je Wagen; Restaurant separat prüfen','O=RT, L=GE; B nur optional'],
      ['Kupplungen','2× E395640; E374060 + E374340','Polzahl, Richtung und Passung messen'],
    ],'after':6},
    {'type':'p','text':'Werkzeug: Multimeter, feine Lötstation, Entlöthilfe, Lupe, Kamera, isolierende Unterlage und geordnete Schraubenablage. Vor dem Löten beide Köpfe stromlos machen und jede Leitung fotografieren.','after':6},
    {'type':'note','label':'STOPP','tone':'stop','text':'Fehlt der Funktionsdecoder für den LoDi-511 oder sind die Kupplungspole unklar, nicht mit dem Einbau beginnen.','after':0},
]

for p in pages:
    if p['source_card'] == 19:
        p['title'] = 'LoDi-512 und LoDi-511 richtig erkennen'
        p['before'] = ('Vor dem Einbau die Aufdrucke fotografieren. 512 = ICE-M-S mit optionaler '
                       'Schleiferumschaltung für den motorisierten Kopf; 511 = ICE-M ohne Umschaltrelais für '
                       'den Gegenkopf. Standardbetrieb: beide Schleifer parallel auf RT, SW bleibt nur als '
                       'später nutzbare, isolierte Option frei. Stecker, SW/SJ-Jumper und Widerstände nur nach '
                       'der eigenen Platinenrevision zuordnen.')
        p['blocks'] = [
          {'type':'table','headers':['Betriebsart','Verdrahtung','Konsequenz'],'widths':[1.2,2.4,1.4], 'rows':[
            ['Standard jetzt','Vorderer und hinterer Schleifer gemeinsam auf RT; GE nur als Lichtbus','Doppelte Stromaufnahme; eine Quelle'],
            ['Spätere Option','LoDi-Schleiferumschaltung nach Herstellerplan, mit eigener Trenn-/Grenzprüfung','Signalabschnitte möglich; nicht gleichzeitig parallel'],
            ['Verbot','SW/RT, beide Decoder-Ausgänge oder zwei GE-Quellen brücken','Kurzschluss-/Decoderrisiko'],
          ],'after':6},
          {'type':'step','label':'1.','text':'Die aktuelle Platinenrevision beidseitig fotografieren und SW, RT, GE, SJ1/SJ2 sowie den örtlichen Schleiferanschluss markieren.','after':4},
          {'type':'step','label':'2.','text':'Für den Grundaufbau den vorderen Schleifer und den RT-Kupplungsbus als einen Rohstromkreis dokumentieren. SW nicht mit einem Decoder-Ausgang verbinden; der isolierte SW-Abzweig bleibt für eine spätere, getrennte Umschaltvariante erhalten.','after':4},
          {'type':'note','label':'STOPP','tone':'stop','text':'Nie gleichzeitig die beiden Schleifer parallel brücken und die Relaisumschaltung aktivieren. Vor einem späteren Wechsel muss die Parallellitze stromlos getrennt und die neue LoDi-Schaltung vollständig neu geprüft werden.','after':0},
        ]
    if p['source_card'] == 20:
        p['title'] = 'LoDi-514-Frontlicht ohne vertauschte Farben anschließen'
        p['before'] = ('Je 514 sind Weiß, Rot und gemeinsamer Plusleiter zu markieren. Weiß und Rot bekommen '
                       'ihre eigenen LoDi-Zweige; keine LED-Leitung gemeinsam auf einen Ausgang legen. Die '
                       'beiden Frontplatinen sind mechanisch seitenrichtig zuzuordnen, bevor gelötet wird.')
        p['blocks'] = [
          {'type':'figure','kind':'led','maxh':105,'after':5},
          {'type':'table','headers':['Leitung','Anschluss'],'widths':[1,2], 'rows':[
            ['Gemeinsamer Plus','Front-VCC / U+ der jeweiligen LoDi-Platine'],
            ['Weiß','L_WS bzw. Weiß-Ausgang'],
            ['Rot','L_RT bzw. Rot-Ausgang'],
          ],'after':6},
          {'type':'step','label':'1.','text':'Jede 514 fotografieren und die drei Leitungen vor dem Löten markieren. Keine Farbe aus dem 2976-Original übernehmen.','after':4},
          {'type':'step','label':'2.','text':'Weiß und Rot jeweils einzeln gegen den gemeinsamen Plus messen; RT/GE und Chassis dürfen dabei nicht verbunden sein.','after':4},
          {'type':'note','label':'STOPP','tone':'stop','text':'Falsche Farbe oder Kurzschluss: Decoder abziehen, Leitung zurückverfolgen, erst danach weiterarbeiten.','after':0},
        ]
    if p['source_card'] == 27:
        p['title'] = 'Jeden Innenwagen mit LoDi-510 ausrüsten'
        p['before'] = ('LoDi-510 ist eine Wagenplatine, nicht die zentrale Zugplatine. Für jeden vorgesehenen '
                       'Innenwagen W1…Wn wird eine eigene Platine benötigt; im Bordrestaurant ist die passende '
                       'LoDi-Variante nach Platinenaufdruck einzusetzen. RT ist der gemeinsame Rohstrombus, GE '
                       'der einzige geschaltete Innenlichtbus vom vorderen 60977.')
        p['blocks'] = [
          {'type':'step','label':'1.','text':'Alle Wagen zählen und dauerhaft W1…Wn beschriften. Pro Wagen LoDi-510, Einbaurichtung, Platinenrevision und Potentiometerstellung fotografieren. Fehlende Platinen erst beschaffen; keine Wagenplatine zwischen zwei Wagen teilen.','after':4},
          {'type':'step','label':'2.','text':'Platinen ohne Strom trocken auflegen. Dach, Fenstereinsatz, Rastnasen, Kupplungsdeichsel und Drehgestelle müssen frei bleiben. Das Potentiometer zunächst auf niedrige Helligkeit stellen; die Endhelligkeit wird erst nach der Lastprüfung erhöht.','after':4},
          {'type':'table','headers':['LoDi-510-Pad','Anschluss im 2976-Grundaufbau','Regel'],'widths':[1.2,2.2,1.6], 'rows':[
            ['O','RT-Kupplung / Roh-Mittelleiter','O-O durchgängig prüfen'],
            ['L','GE-Kupplung / geschaltetes Innenlicht','L-L durchgängig prüfen'],
            ['B','örtlicher Radkontakt','frei lassen, sofern nicht separat nachgewiesen'],
            ['SJ2/Türlicht','nur nach Platinenaufdruck','nicht mit SJ1 der Motorplatine verwechseln'],
          ],'after':6},
          {'type':'step','label':'3.','text':'RT-Litzen an O und GE-Litzen an L anschließen. Keine zusätzliche lange Steuerleitung durch den Zug ziehen. B und lose Massefedern einzeln isolieren, sofern kein eigener Radkontakt bewusst nachgerüstet wird.','after':4},
          {'type':'step','label':'4.','text':'Jeden Wagen einzeln auf L-L, O-O, L gegen O und freie Enden prüfen. Danach die Deichsel in beide Endlagen bewegen; kein Draht darf spannen oder am Rad schleifen.','after':4},
          {'type':'note','label':'STOPP','tone':'stop','text':'Ein einziger LoDi-510 beleuchtet nur einen Wagen. Ein gemeinsamer U+/GND-Draht zwischen den beiden Decoderplatinen ist nicht zulässig; der 60977 speist GE, der hintere 60972 bleibt am GE-Ende isoliert.','after':0},
        ]
    if p['source_card'] == 28:
        p['title'] = 'Stromführende Kupplungen: RT und GE durchmessen'
        p['before'] = ('Bestand laut Bestellung: 2× Märklin E395640 für die Triebkopf-Übergänge sowie '
                       'E374060 + E374340 als stromführende Wagenkupplungspaare. Jeder Übergang benötigt '
                       'zwei voneinander getrennte Pole: RT für den Rückleiter und GE für den Lichtschaltpfad. '
                       'Artikelnummer und Polzahl werden notiert; Form und Kabelfarbe beweisen keine Belegung.')
        p['blocks'] = [
          {'type':'figure','kind':'coupler','maxh':125,'after':5},
          {'type':'step','label':'1.','text':'E395640 an den beiden Triebkopf-Übergängen, E374060/E374340 an den Wagenübergängen trocken einsetzen. Jede Kontaktfläche fotografieren und vorläufig K1/K2 nennen.','after':4},
          {'type':'step','label':'2.','text':'RT-1 zu RT-2 und GE-1 zu GE-2 müssen leitend sein; RT zu GE, RT/GE zu Chassis und RT/GE zum falschen Nachbarpol müssen offen sein.','after':4},
          {'type':'step','label':'3.','text':'Kupplung in beide Endlagen bewegen und die Messung wiederholen. Bei Unterbrechung, Kreuzpfad oder mechanischem Zug nicht einbauen.','after':4},
          {'type':'note','label':'DOKUMENTIEREN','text':'Übergang, Fotoansicht, Polzahl, RT/GE-Herkunft und Messwerte auf dem Abnahmeblatt notieren.','after':0},
        ]
    if p['source_card'] == 31:
        p['title'] = '60977 und richtungsabhängiges Licht einstellen'
        p['before'] = ('Nur auf dem isolierten Prüfabschnitt programmieren. Motorisierter Kopf: vorwärts weiß, '
                       'rückwärts rot. Gegenkopf: die physische LED-Zuordnung wird gespiegelt, damit am Zugende '
                       'bei derselben Fahrtrichtung rot leuchtet. Erst danach beide Decoder gemeinsam testen.')
        p['blocks'] = [
          {'type':'table','headers':['Funktion','Soll'],'widths':[1.1,3], 'rows':[
            ['Motor','60941 vollständig geprüft; CV52 nach Märklin-Projekt, Wert dokumentieren'],
            ['Frontlicht','Weiß/Rot getrennt; AUX4 nur nach dokumentierter LoDi-Jumperstellung'],
            ['Innenlicht','60977-AUX4 → GE → L an allen LoDi-510; keine Last an LV/LR; Helligkeit je Wagen separat'],
            ['Schleifer','Standard: beide Schleifer parallel auf RT; Umschalt-AUX bleibt aus'],
            ['AUX1/AUX2','Bei der -S-Platine für spätere Schleiferumschaltung reserviert; im Parallelbetrieb keine externe Brücke'],
            ['AUX3/AUX5','AUX3 optional Fernlicht; AUX5 optional Führerstand; nur lokal und erst nach belegter Platinenrevision'],
          ],'after':5},
          {'type':'step','label':'1.','text':'60977 mit dem Märklin 60971 einzeln lesen, Projektversion und geänderte CV-Werte notieren, dann schreiben und zurücklesen.','after':4},
          {'type':'step','label':'2.','text':'60972 mit dem 60971 separat lesen. mfx im hinteren Decoder nur durch gezieltes Löschen des mfx-Bits in CV50 deaktivieren (Altwert lesen, Bit 3 löschen, übrige Bits unverändert lassen; bei Standardwert 15 ergibt das 7). Vorwärts LV und rückwärts LR so zuordnen, dass der Gegenkopf sichtbar gespiegelt leuchtet. 60982 nicht direkt auf die 21MTC setzen; sein 8-poliger Kabelbaum ist eine andere Anschlussvariante.','after':4},
          {'type':'table','headers':['Fahrtrichtung','Motor-Kopf','Gegenkopf'],'widths':[1,1.2,1.2], 'rows':[
            ['Vorwärts','weiß an / rot aus','rot an / weiß aus'],
            ['Rückwärts','rot an / weiß aus','weiß an / rot aus'],
          ],'after':5},
          {'type':'note','label':'STOPP','tone':'stop','text':'Keine automatische Einmessfahrt und kein CV-Experiment am angeschlossenen Zug. Erst Einzelkopf prüfen, dann Paarprüfung.','after':0},
        ]
    if p['source_card'] == 35:
        p['title'] = '60972 auf LoDi-511 setzen und hinten mfx-frei halten'
        p['before'] = ('Der 60972 sitzt auf der LoDi-511-21MTC-Aufnahme. Der Gegenkopf liefert Frontlicht '
                       'und nimmt den hinteren Schleifer auf; sein GE-Anschluss bleibt isoliert, damit nur der '
                       'vordere 60977 den Innenlichtbus speist. Die mfx-Abschaltung erfolgt am isolierten Decoderplatz.')
    if p['source_card'] == 46:
        p['title'] = 'Quellen, offene Bestätigungen und Abnahmeblatt'
        p['goal'] = ('Herstellerquellen belegen Plattform und Schnittstellen. Passung, Kontaktkraft, Strom '
                     'und Lichtfunktion am eigenen 2976 bleiben Messwerte und werden vor dem Schließen eingetragen.')

src = pages[-1]
src['blocks'] = [
 {'type':'p','text':'<b>Herstellerquellen:</b> LoDi-WiB ICE-M / Motor WiB ICE-M(-S), Einbaufolge für den ICE 1; Märklin 60941 Hochleistungsmotor; Märklin 60977 mSD3 SoundDecoder; Märklin 60972 mLD3 mit 21MTC; Märklin 60982 mLD3 mit Kabelbaum; Märklin Ersatzteilliste 2976/3370.'},
 {'type':'table','headers':['Eintrag','Verwendung'], 'widths':[1,3], 'rows':[
   ['LoDi-512 ICE-M-S','Motorisierter Kopf, 21-polige Schnittstelle, Schleiferumschaltung'],
   ['LoDi-511 ICE-M','Motorloser Gegenkopf, Licht- und Kupplungspfad'],
   ['LoDi-514','Je Kopf Weiß/Rot/Plus für richtungsabhängiges Frontlicht'],
   ['E395640','2 Stück; stromführende Triebkopf-Übergänge'],
   ['E374060 + E374340','Stromführende Wagenkupplungspaare laut Bestellung'],
   ['Märklin 60941','5-poliger Hochleistungsmotor und Bürstenanschlüsse'],
   ['Märklin 60977 / 60972','Sound-/Fahrdecoder vorn und 21MTC-Funktionsdecoder hinten'],
   ['Märklin 60971','Decoder-Programmer für Lesen, Schreiben und Rücklesen'],
   ['Märklin 60982','Reserve/Alternative mit 8-poligem Kabelbaum; nicht direkt auf LoDi-21MTC'],
   ['Märklin 78792','Bordrestaurant-Wagen; passende LoDi-Wagenplatine und Innenlicht erst nach RT/GE-Prüfung'],
   ['LoDi-510','Je Innenwagen eine LoDi-WiB ICE1-M; O=RT, L=GE, B optional'],
 ]},
 {'type':'note','label':'OFFEN VOR DER ENDMONTAGE','tone':'stop','text':
  'Kupplungs-Artikelnummer und Polzahl, LoDi-Platinenrevision, reale Decoderwerte, Stromaufnahme je Wagen und die Passung des eigenen 2976 sind einzutragen. Ohne diese Nachweise keine endgültige Freigabe.'},
 {'type':'p','text':'<b>Abnahme:</b> Erst 60977 allein, dann Gegenkopf, dann jeder Wagen einzeln. Nach jedem Übergang RT gegen GE auf Kurzschluss prüfen; bei falscher Lichtfarbe zuerst LED-Zuordnung und danach Decoder-Richtung prüfen.'},
]

for p in pages:
    p['sources'] = [s for s in p.get('sources', []) if s]
    p.setdefault('check', '')

OUT = PROJECT / 'output/pdf/ICE_2976_Umbauanleitung_REV15_KOMPAKT_LODI.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
layout = Layout(OUT, pages)
layout.build()
r = PdfReader(str(OUT))
assert len(r.pages) == len(pages)
report = {'output': str(OUT), 'pages': len(r.pages),
          'sha256': hashlib.sha256(OUT.read_bytes()).hexdigest(),
          'links': sum(len(p.get('/Annots', [])) for p in r.pages),
          'figures': len(layout.figures), 'order': ORDER,
          'target': 'Märklin ICE 1 2976 / LoDi-512 + LoDi-511 + 2x LoDi-514'}
(ROOT / 'build_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
(ROOT / 'compact_pages.json').write_text(json.dumps(pages, ensure_ascii=False, indent=2))
print(json.dumps(report, ensure_ascii=False, indent=2))
