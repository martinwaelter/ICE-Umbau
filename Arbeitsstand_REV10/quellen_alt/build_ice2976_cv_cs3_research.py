from pathlib import Path
from html import escape
import hashlib
import random
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output/pdf/ICE_2976_CV_CS3_FORENSISCHER_NACHWEIS.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
for name, fname in [('Arial', 'Arial.ttf'), ('Arial-Bold', 'Arial Bold.ttf'), ('Arial-Italic', 'Arial Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/System/Library/Fonts/Supplemental/' + fname))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='Arial-Bold', italic='Arial-Italic', boldItalic='Arial-Bold')

COMMIT = '32eca6cddc18a55f2efdfdbc970cca96b7511827'
GH = 'https://github.com/JMRI/JMRI/blob/' + COMMIT + '/'
SOURCES = {
1: ('ESU', 'Master/Slave Adress-Synchronisation', 'o. D.; Herstellerbeispiel mit LokSound 5, Firmware ab 5.1.101', 'https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-50x/masterslave-adress-synchronisation/'),
2: ('ESU', 'LokPilot 5 - Produkt und Bestellinformationen', 'o. D.; Artikel 59649 = DCC/MM/SX/M4, 21MTC MKL', 'https://www.esu.eu/produkte/lokpilot/lokpilot-5/'),
3: ('JMRI', 'v5standardCVs.xml', 'Quellenstand 09.09.2026; Zeilen 994-1016, CV191 und CV192:4', GH + 'xml/decoders/esu/v5standardCVs.xml#L994'),
4: ('JMRI', 'ESU_LokPilot5.xml', 'Quellenstand 09.09.2026; MKL-Modell und eingebundene Definitionen, Zeilen 186, 246 und 256', GH + 'xml/decoders/ESU_LokPilot5.xml#L186'),
5: ('JMRI', 'v4advancedPane.xml', 'Quellenstand 09.09.2026; tatsächlich in LokPilot-5-Definition eingebunden; Synchronisationsbereich, Zeilen 47-63', GH + 'xml/decoders/esu/v4advancedPane.xml#L47'),
6: ('JMRI', 'CvUtil.java', 'Quellenstand 09.09.2026; Expansion einer CV-Liste, ab Zeile 44', GH + 'java/src/jmri/util/CvUtil.java#L44'),
7: ('JMRI', 'VariableTableModel.java', 'Quellenstand 09.09.2026; Standardmaske mit acht Bits, ab Zeile 274', GH + 'java/src/jmri/jmrit/symbolicprog/VariableTableModel.java#L274'),
8: ('JMRI', 'SplitVariableValue.java und SplitHexVariableValue.java', 'Quellenstand 09.09.2026; Bitoffsets und Zusammensetzung ab Zeile 95; Hexdarstellung in Unterklasse', GH + 'java/src/jmri/jmrit/symbolicprog/SplitVariableValue.java#L95'),
9: ('Märklin', 'CAN-Protokoll, Version 2.0', 'S. 19 und 28: UID/SID; S. 50-51: Datenfelder in lokomotive.cs2. CS2-Dokument, kein ungeprüfter CS3-Formatnachweis', 'https://www.maerklin.de/fileadmin/media/service/software-updates/cs2CAN-Protokoll-2_0.pdf'),
10: ('Stefan Krauß', 'Schienenformat mfx', 'Version 2.3, 17.06.2017; S. 22-23 und 39; originale Protokollanalyse', 'https://www.skrauss.de/modellbahn/Schienenformat.pdf'),
11: ('NMRA', 'S-9.2.2 Appendix A - Manufacturer IDs', '08.05.2025; 131: Trix Modelleisenbahn, 151: Electronic Solutions Ulm', 'https://www.nmra.org/sites/default/files/standards/sandrp/DCC/S/appendix_a_s-9_2_2.pdf'),
12: ('Märklin', 'Kurzanleitung Central Station 3 ab Softwareversion 2.5', 'S. 13-15: Lok bearbeiten/CV; S. 25 und 27: System und Sicherung', 'https://static.maerklin.de/damcontent/c1/ce/c1ce554ad6ad195c04e32ba1b4dd64511764068661.pdf'),
13: ('Märklin Nederland', 'Software-updates CS 3 / CS 3 plus', '18.08.2026: 2.6.2 Build 0; ältere Versionsnennung im allgemeinen Einleitungsabsatz abweichend', 'https://www.marklin.nl/service/downloads/cs3-updates'),
14: ('ESU', 'LokPilot 5 Betriebsanleitung', '8. Auflage, 24.01.2023; S. 43, Abschnitt 8.2.6: CS2/CS3; Motor-Einmessung in Abschnitt 11.1.4', 'https://www.esu.eu/download/betriebsanleitungen/digitaldecoder/?tx_esudownloads_pi1%5BdownloadItem%5D=803bc0046a0244b6416c82c6abfd385e'),
15: ('Märklin', 'CS3-Gesamtchangelog bis Version 2.6.0', 'PDF-S. 12: CV-Editor ab 2.4.0; S. 26: Vorlagenfalle; S. 2: Lesefehler; S. 10: PoM', 'https://www.maerklin.de/fileadmin/media/service/cs3/Maerklin_CS3_v2.6.0_changelog.pdf'),
16: ('Märklin', 'Lok-Konfiguration - CV-Editor', 'Herstellerhilfe 2018; unmittelbares Schreiben und Vorlagentransfer. Ältere Leseautomatik nicht unverändert übernehmen', 'https://www.maerklin.de/fileadmin/media/clubs/downloads/Loks_CV_Editor.pdf'),
17: ('ESU', 'CV-Änderungen anzeigen', 'Herstelleranleitung zur Offline-Liste und Übertragung mit DCC-Zentrale; Funktion ab Software 4.4.0', 'https://www.esu.eu/support/tipps-tricks/lokprogrammer-software-v4/cv-aenderungen-anzeigen/'),
18: ('ESU', 'LokProgrammer - PC-Software und Änderungsverzeichnis', 'Angebotener Stand 5.2.18 vom 01.05.2026; genannte Decoderfirmware 5.14.183', 'https://www.esu.eu/download/software/lokprogrammer/'),
19: ('Märklin', 'CV-Tabelle mSD3/mLD3', 'Insbesondere CV250-255 und Decoderinformationen, Index 255/255. Kein dokumentierter UID-Leseweg daraus', 'https://www.maerklin.de/fileadmin/media/service/technische_informationen/CV-Tabelle-mSD3.pdf'),
20: ('ESU', 'ECoS Betriebsanleitung, Auflage II', 'S. 24-25: Programmierung und Quittierung über Stromimpulse; keine Zusage für motorlosen 59649 an CS3', 'https://www.esu.eu/uploads/tx_esudownloads/50000_ECoS_ESUKG_DE_Betriebsanleitung_Auflage_II_eBook.pdf'),
21: ('MTB-Ontour', 'Eigener mSD3/LokPilot-V5-M4-Umbau im ICE Sinus', '26.02.2023, Beitrag 4, 21:03; originaler Erfahrungsbericht, ohne konkrete UID/CV-Werte', 'https://www.stummiforum.de/t212683f5-Umbau-ICE-Maerklin-auf-mSD-DCC.html'),
22: ('nakott', 'Wo finde ich die UID eines Lokdecoders?', '13.03.2017, Beiträge 8 und 9; originale ESU-V4-Rohdatenmessungen, nicht mSD3/V5-Freigabe', 'https://www.stummiforum.de/t147582f7-Wo-finde-ich-die-UID-eines-Lokdecoders.html'),
23: ('Stummiforum, Originaldiskussion', 'ESU LokPilot RailComPlus & Master Decoder Synchronisation geht nicht', '13.02.2026 ff.; DCC-/LokProgrammer-Test nicht mit mfx-Test verwechseln', 'https://www.stummiforum.de/t242098f5-ERLEDIGT-ESU-LokPilot-RailComPlus-Master-Decoder-Synchronisation-geht-nicht.html'),
}

W, H = 595.28, 841.89
LEFT, WIDTH = 46, W - 92
STYLE = ParagraphStyle('body', fontName='Arial', fontSize=10.6, leading=14.6, textColor=colors.HexColor('#202020'), spaceAfter=8)
SMALL = ParagraphStyle('small', parent=STYLE, fontSize=8.3, leading=10.5, spaceAfter=5)
CELL = ParagraphStyle('cell', parent=STYLE, fontSize=9.4, leading=12.4, spaceAfter=0)
HEAD = ParagraphStyle('head', parent=STYLE, fontName='Arial-Bold', fontSize=17, leading=21, spaceAfter=15)
TITLE = ParagraphStyle('title', parent=HEAD, fontSize=24, leading=29)
SUB = ParagraphStyle('sub', parent=STYLE, fontName='Arial-Bold', fontSize=12.2, leading=16, spaceBefore=6, spaceAfter=8)

class Report:
    def __init__(self):
        self.c = canvas.Canvas(str(OUT), pagesize=(W, H), pageCompression=1)
        self.c.setTitle('ICE 2976: CV-Programmierung mit der CS3')
        self.c.setAuthor('')
        self.page = 0
        self.y = 0
        self.refs = []
        self.metrics = []
    def start(self, title, main=False):
        if self.page:
            self.end()
        self.page += 1
        self.y = H - 47
        self.refs = []
        self.c.bookmarkPage('page' + str(self.page))
        self.c.addOutlineEntry(title, 'page' + str(self.page), 0, False)
        self.p(title, TITLE if main else HEAD)
    def p(self, text, style=STYLE, after=None):
        p = Paragraph(text, style)
        _, h = p.wrap(WIDTH, H)
        self.y -= h
        p.drawOn(self.c, LEFT, self.y)
        self.y -= style.spaceAfter if after is None else after
    def ref(self, *nums):
        for n in nums:
            if n not in self.refs:
                self.refs.append(n)
        return '<super>' + ','.join(f'<a href="{escape(SOURCES[n][3], quote=True)}" color="#202020">{n}</a>' for n in nums) + '</super>'
    def sub(self, s): self.p(s, SUB)
    def table(self, rows, widths):
        data = [[Paragraph(str(t), CELL) for t in row] for row in rows]
        t = Table(data, colWidths=[WIDTH * x for x in widths], hAlign='LEFT')
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0),(-1,0), colors.HexColor('#e8e8e8')),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
            ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
            ('LINEBELOW',(0,0),(-1,0),0.6,colors.HexColor('#666666')),
            ('LINEBELOW',(0,1),(-1,-1),0.35,colors.HexColor('#cccccc')),
        ]))
        _, h = t.wrap(WIDTH,H)
        self.y -= h
        t.drawOn(self.c,LEFT,self.y)
        self.y -= 12
    def flow(self, boxes):
        # One compact left-to-right schematic; no electrical pinout is implied.
        bw = (WIDTH - 22 * (len(boxes)-1)) / len(boxes)
        top = self.y
        bh = 58
        for i, text in enumerate(boxes):
            x = LEFT + i*(bw+22)
            self.c.setStrokeColor(colors.HexColor('#555555'))
            self.c.setFillColor(colors.white)
            self.c.rect(x, top-bh,bw,bh,fill=1,stroke=1)
            p = Paragraph(text,CELL)
            _,ph = p.wrap(bw-14,bh-10)
            p.drawOn(self.c,x+7,top-8-ph)
            if i < len(boxes)-1:
                sy=top-bh/2
                self.c.line(x+bw+3,sy,x+bw+19,sy)
                self.c.line(x+bw+19,sy,x+bw+15,sy+3)
                self.c.line(x+bw+19,sy,x+bw+15,sy-3)
        self.y -= bh+14
    def end(self):
        notes=[]
        for n in self.refs:
            publisher,title,detail,url=SOURCES[n]
            notes.append(Paragraph(f'{n}. {escape(publisher)}: <a href="{escape(url,quote=True)}" color="#202020">{escape(title)}</a>.',SMALL))
        note_h=sum(p.wrap(WIDTH,H)[1]+3 for p in notes)
        floor=53+note_h+9
        if self.y < floor:
            raise RuntimeError(f'Page {self.page} overlap: body bottom {self.y:.1f}, required {floor:.1f}')
        self.metrics.append((self.page,round(self.y,1),round(floor,1)))
        y=53+note_h
        if notes:
            self.c.setStrokeColor(colors.HexColor('#bbbbbb'))
            self.c.line(LEFT,y+8,LEFT+WIDTH,y+8)
        for p in notes:
            _,h=p.wrap(WIDTH,H)
            y-=h
            p.drawOn(self.c,LEFT,y)
            y-=3
        self.c.setFont('Arial',8)
        self.c.setFillColor(colors.HexColor('#555555'))
        self.c.drawRightString(W-LEFT,28,str(self.page))
        self.c.showPage()
    def save(self):
        self.end()
        self.c.save()

r=Report()
r.start('ICE 2976: CV-Programmierung mit der CS3',main=True)
r.p('<b>Die CS3 kann den ESU 59649 über DCC-CVs programmieren. Für die Master-Synchronisation sind außerdem konkrete Register gefunden: CV191 bis CV195. Ein Kaufzwang für den ESU LokProgrammer 53451 ist damit nicht begründet. Eine vollständig freigegebene Schreibfolge für Märklin 60977 plus ESU 59649 liegt jedoch noch nicht vor.</b>'+r.ref(3,14))
r.p('Untersucht wird der ICE 1 aus Märklin-Startpackung 2976: Märklin 60977 mSD3 im motorisierten Kopf, ESU 59649 LokPilot 5 M4 MKL im motorlosen Kopf. Ziel sind ein automatisch angemeldeter mfx-Zug, Sound und rot/weißer Lichtwechsel an beiden Enden ohne Traktion. ESU führt Artikel 59649 ausdrücklich als M4-fähige MKL-Ausführung.'+r.ref(2))
r.sub('Die drei getrennten Fragen')
r.table([
['<b>Frage</b>','<b>Ergebnis</b>'],
['Kann die CS3 die Register erreichen?','Ja. DCC-Programmiergleis ist vom späteren mfx-Fahrbetrieb zu unterscheiden.'],
['Welche Register gehören zur Synchronisation?','JMRI implementiert Herstellerkennung in CV191 und ein 32-Bit-Seriennummernfeld in CV192-195.'],
['Welche Werte aktivieren genau dieses Decoderpaar?','Noch offen: Aktivierungswirkung, Märklin-Kennung im ESU-Feld und tatsächliche Decoderfirmware müssen zusammenpassen.'],
],[.39,.61])
r.sub('Die vorgesehene Funktion - kein neuer Drahtbus')
r.flow(['<b>CS3</b><br/>meldet den Master an; vergibt mfx-Adresse','<b>60977</b><br/>Master für Motor, Sound und lokale Funktionen','<b>59649</b><br/>soll derselben Adresse auf dem Gleis folgen'])
r.p('Die Grafik zeigt die logische Zuordnung, keine direkte Verdrahtung von Decoder zu Decoder. ESU beschreibt automatische Adressangleichung an den Master; Funktionsmapping und Versorgung bleiben eigenständige Aufgaben. Die Herstelleranleitung erläutert ein ESU/ESU-Beispiel, nicht genau dieses Mischpaar.'+r.ref(1))
r.p('<b>Empfehlung:</b> 53451 vorerst nicht kaufen. Erst Identität und CV-Lesezugang sichern, dann den Aktivierungsexport prüfen. Dieser Nachweisbericht ergänzt REV7, ersetzt aber weder deren Isolationsprüfungen noch die ausstehende Funktionsabnahme.',after=0)

r.start('1. Die nachgewiesenen Synchronisations-CVs')
r.p('Die öffentliche Decoderdefinition von JMRI/DecoderPro enthält den LokPilot 5 MKL und bindet die CV- sowie Bedienbereichsdefinition für die Master-Synchronisation ein. Der Eintrag ist seit April 2020 vorhanden. Er ist Primärevidenz für eine Softwareimplementierung, keine schriftliche Funktionsgarantie von ESU.'+r.ref(3,4,5))
r.table([
['<b>CV im 59649</b>','<b>JMRI-Feld / Bedeutung</b>','<b>Umfang</b>'],
['191','M4MfgId: Herstellerkennung des Masters','1 Byte; 0-255'],
['192','M4SerNo: niedrigstes Byte des Seriennummernfelds','Bits 0-7'],
['193','M4SerNo: zweites Byte','Bits 8-15'],
['194','M4SerNo: drittes Byte','Bits 16-23'],
['195','M4SerNo: höchstes Byte','Bits 24-31'],
],[.20,.59,.21])
r.p('<b>Für diese fünf Register ist kein Index über CV31/CV32 nötig.</b> Die Zuordnung verwendet normale CV-Nummern unter 255. Die ESU-Erklärung zum CV-Export bestätigt, dass Indexwerte in diesem unteren Bereich nicht maßgeblich sind.'+r.ref(17))
r.sub('Bytefolge: kleines Byte zuerst')
r.p('JMRI expandiert „192:4“ zu vier aufsteigenden CVs, verwendet jeweils acht Bits und beginnt beim Zusammenfügen mit Bitoffset null. Daraus folgt die nachstehende Rechnung. Das bestätigt die Bytefolge der Implementierung, nicht die noch offene Märklin-zu-ESU-Identitätsumsetzung.'+r.ref(6,7,8))
r.p('<b>S = CV192 + 256 × CV193 + 65.536 × CV194 + 16.777.216 × CV195</b>')
r.table([
['<b>Nur Rechenbeispiel</b>','<b>CV192</b>','<b>CV193</b>','<b>CV194</b>','<b>CV195</b>'],
['S = 0x12345678','120','86','52','18'],
],[.36,.16,.16,.16,.16])
r.p('<b>Die Beispielwerte niemals in den Decoder schreiben.</b> „0x“ kennzeichnet Hexadezimalzahlen; die Tabellenwerte sind dezimal. Das Beispiel ist keine UID des vorhandenen 60977. Die Standardbelegung CV191 = 0 beweist weder „deaktiviert“ noch einen sicheren Rücksetzweg. Ein zusätzlicher Aktivierungsparameter ist öffentlich noch nicht nachgewiesen.')

r.start('2. Hersteller, Seriennummer und mfx-Adresse')
r.p('Die Zentrale identifiziert einen mfx-Decoder über seine dauerhafte UID und ordnet ihm eine Betriebsadresse zu. Märklins CAN-Dokumentation trennt diese Größen ausdrücklich. Die Beschreibung der CS2-Datei lokomotive.cs2 unterscheidet außerdem mehrere ähnlich benannte Datenfelder; sie ist noch kein Beweis für das aktuelle CS3-Backupformat.'+r.ref(9))
r.table([
['<b>Begriff</b>','<b>Für diesen Nachweis</b>'],
['mfx-UID / .mfxuid','Dauerhafte Kennung des echten 60977. Kandidat für die Identitätsprüfung; unverändert sichern.'],
['SID / mfx-Betriebsadresse','Von der Zentrale zugewiesene Adresse. Nicht als dauerhafte Masterseriennummer eintragen.'],
['.uid im Lokdatensatz','Nicht mit .mfxuid gleichsetzen. Datenfeld und Herkunft müssen zum tatsächlichen Dateiformat passen.'],
['DCC-Adresse / CV1','Betriebsadresse eines anderen Protokolls. Gleiche DCC-Adressen ergeben noch keine mfx-Synchronisation.'],
['Herstellerkennung / CV8','Identifiziert den Hersteller, nicht den individuellen Decoder.'],
['M4SerNo / CV192-195','Zielseriennummer im ESU-Synchronisationsmodell. Beziehung zur Märklin-Roh-UID noch prüfen.'],
],[.34,.66])
r.sub('Warum nicht einfach „131 plus UID“ schreiben?')
r.p('Die NMRA führt 131 für Trix Modelleisenbahn und 151 für ESU. Krauß dokumentiert 0x83 (= 131) im separaten Herstellerfeld von Märklin/Trix. Eine typische Märklin-UID mit Anfang 0x7F beginnt aber gerade nicht mit 0x83. Herstellerbyte und UID-Präfix dürfen deshalb nicht gleichgesetzt werden.'+r.ref(10,11))
r.flow(['<b>Roh-UID</b><br/>aus eindeutig zugeordnetem 60977-Datensatz','<b>Zuordnung offen</b><br/>Herstellerfeld + ESU-Zielseriennummer S','<b>Bytezerlegung</b><br/>S in CV192-195: rechnerisch nachgewiesen'])
r.p('Das mfx-Anmeldetelegramm und die CV-Speicherung verwenden außerdem unterschiedliche Darstellungen. Eine Bytefolge aus einer Netzwerknachricht darf nicht ohne Umrechnung als CV-Reihenfolge kopiert werden. Auch die vom ESU-Programmer angezeigte Seriennummer muss erst mit der Roh-UID abgeglichen werden.')
r.p('<b>Konkrete Folge:</b> Weder eine DCC-Adresse noch eine gekürzte UID, eine Firmwareversion oder der Wert 151 aus dem ESU-Beispiel darf als Masterkennung eingesetzt werden. Eine unbekannte Umrechnung wird nicht durch Ausprobieren am vollständigen Zug ersetzt.')

r.start('3. Die tatsächliche Masterkennung sichern')
r.p('Die aktuell auffindbare Herstellerveröffentlichung nennt CS3 <b>2.6.2 (Build 0), Stand 18.08.2026</b>. Das ist der recherchierte Veröffentlichungsstand, kein abgelesener Nachweis der konkreten Zentrale. Deren genaue Anzeige unter System > CS3 > Geräte- und Softwareinfo gehört in das spätere Prüfprotokoll.'+r.ref(13,15))
r.sub('Sicherung statt Suche in fremden CV-Tabellen')
r.p('Der bevorzugte nächste Datenzugang ist eine neue CS3-Sicherung nach eindeutiger mfx-Anmeldung des 60977. Ein bereits vorhandener, unzweifelhaft zugeordneter Eintrag kann verwendet werden. Ist der Decoder noch nicht in einem elektrisch geprüften Aufbau, wird für diese Datensuche kein ungeprüfter Triebkopf eingeschaltet.')
r.p('<b>1.</b> Die CS3 auf STOP stellen. In der Lokliste Namen und Artikelzuordnung des 60977-Masters dokumentieren. Bei mehreren gleich benannten ICE-Einträgen keine Zuordnung raten.<br/><b>2.</b> Einen USB-Stick an einem der beiden Daten-USB-Anschlüsse verwenden, nicht am reinen Ladeanschluss.<br/><b>3.</b> System > CS3 > Sichern öffnen. Den USB-Stick als Ziel wählen und einen neuen Namen vergeben, etwa ICE2976_vor_CV_2026-09-10. Bestehende Sicherungen nicht überschreiben.<br/><b>4.</b> Abschluss abwarten, die neue Datei kontrollieren und den Stick über die Auswurffunktion abmelden. Nicht „Wiederherstellen“ auswählen.'+r.ref(12))
r.p('Die Sicherung wird anschließend ausschließlich als Kopie untersucht. Gesucht wird der vollständig erhaltene Lokdatensatz des Masters, insbesondere ein ausdrücklich als mfx-UID ausgewiesenes Feld. Fehlt dieses oder ist die Zuordnung mehrdeutig, ist die Identität noch nicht gewonnen. Dateiname und Feldschema werden nicht aus dem CS2-Dokument für die CS3 erfunden.')
r.sub('Diese CV-Abkürzungen gelten beim 60977 nicht')
r.table([
['<b>Verführerische Angabe</b>','<b>Tatsächlich dokumentiert</b>'],
['CV250-255','Getriebe-/Radumfangs- und Bremswegparameter; keine UID.'],
['Index 255/255, CV271-274','Firmwareversionsbytes; keine UID.'],
['CV105/106','Benutzerkennung; nicht die eindeutige Werksidentität.'],
['ESU-V4: Index 0/255, CV265-268','Originalmessungen betreffen ESU V4. Keine Ausleseanweisung für den Märklin 60977.'],
],[.40,.60])
r.p('Die vollständige Märklin-CV-Tabelle und der originale ESU-V4-Vergleich geben keinen dokumentierten DCC-UID-Leseweg für diesen mSD3 her. Das bedeutet „hier nicht nachgewiesen“, nicht „technisch unmöglich“.'+r.ref(19,22))

r.start('4. CS3: zuerst ausschließlich lesen')
r.p('ESU beschreibt ausdrücklich einen zusätzlichen manuellen DCC-Eintrag zur Programmierung mit CS2/CS3, auch wenn der Decoder bereits per mfx angemeldet ist. <b>Dieser Werkstatteintrag ist keine zweite automatische Zuganmeldung und keine Traktion.</b> Die DCC-Adresse des Eintrags ist im hier verwendeten Programmiergleisverfahren nicht das Auswahlkriterium.'+r.ref(14))
r.sub('Aufbauvoraussetzung für genau den 59649')
r.p('Nur der elektrisch geprüfte ESU-59649-Aufbau darf am vollständig getrennten CS3-Programmiergleisausgang angeschlossen sein. Der Märklin 60977, der übrige Zug und jede leitende Kupplungsverbindung zu weiteren Decodern bleiben abgetrennt. Puffer bleiben bei diesem ersten Kommunikationsnachweis abgetrennt. Diese Prüfkarte beschreibt keine neue Pufferverdrahtung.')
r.p('Ein fehlender Motor kann das Quittieren von Programmierbefehlen beeinflussen. ESU erläutert den Stromimpulsmechanismus allgemein; die Quittierfähigkeit des konkreten motorlosen 59649-Aufbaus an CS3 ist noch nicht gemessen. Deshalb beginnt der Ablauf mit reinem Lesen, nicht mit einem Test-Schreibwert.'+r.ref(20))
r.sub('Bedienfolge am Bildschirm der CS3')
r.p('<b>1.</b> STOP bleibt zunächst aktiv. Lokliste > Plus beziehungsweise Bearbeiten > Lok hinzufügen öffnen. Den Namen SERVICE ESU59649 - nicht fahren vergeben, Decodertyp DCC auswählen und bestätigen.<br/><b>2.</b> Bearbeiten > Loks bearbeiten öffnen, genau diesen Serviceeintrag antippen und die Registerkarte Konfigurieren auswählen. Nicht den mfx-Master bearbeiten. PoM/Hauptgleisprogrammierung darf nicht gewählt sein.<br/><b>3.</b> Nach bestandener elektrischer Prüfung STOP aufheben. Keine Fahrstufe einstellen und keine Funktionstaste betätigen.<br/><b>4.</b> Die Zeile CV8 auswählen. Falls sie fehlt, eine CV-Zeile hinzufügen und ausschließlich im Feld CV-Nr. die 8 eintragen. <b>Das Wertefeld nicht ändern.</b><br/><b>5.</b> „Decoder auslesen“ auslösen. Erwartung für den ESU: CV8 wird fehlerfrei mit 151 gelesen. Danach nochmals wirklich lesen und beide Ergebnisse dokumentieren.<br/><b>6.</b> Erst nach zwei erfolgreichen Lesevorgängen die CVs 191, 192, 193, 194 und 195 ergänzen und lesen. Jeweils CV-Nummer, Altwert und Leseergebnis festhalten. Anschließend STOP.'+r.ref(12,15))
r.p('<b>Bei Lesefehler:</b> STOP, nichts schreiben und keinen Reset ausführen. Eine fertig abgearbeitete Liste kann fehlerhafte Einzelzeilen enthalten. Ein noch angezeigter alter Wert ist keine neue erfolgreiche Rücklesung. Stimmen Menünamen oder Anzeige nicht überein, erst den tatsächlichen Bildschirm abgleichen; die Position eines Symbols wird hier nicht behauptet.')
r.p('<b>Besonders kritisch:</b> CV8 lesen ist ungefährlich; 8 als <i>Wert</i> in CV8 schreiben ist beim ESU der Reset-Befehl. „Prog.“ beziehungsweise „Vorlagenwerte schreiben“ wird für diese Prüfkarte überhaupt nicht benutzt.'+r.ref(16))

r.start('5. Kostenloser Nachweis durch CV-Export')
r.p('ESU bietet „Extras > Geänderte CVs anzeigen“ an, damit Einstellungen aus der PC-Software mit einer DCC-Zentrale übertragen werden können. Die Änderungsmerkliste wird beim Speichern des Projekts gelöscht; ein Export muss deshalb vor dem nächsten Speichern gesichert werden. Die Software wird aktuell als Version 5.2.18 für Windows angeboten.'+r.ref(17,18))
r.p('<b>Dieser Offline-Versuch wurde noch nicht ausgeführt.</b> Er benötigt Zugang zur Windows-Software, nicht den Kauf des 53451. Die öffentlich dokumentierte allgemeine Exportfunktion beweist noch nicht, dass gerade die Synchronisationsaktivierung vollständig exportiert wird. Genau dies ist der nächste begrenzte Nachweis.')
r.sub('Versuchsplan ohne Verbindung zum Decoder')
r.table([
['<b>Vergleich</b>','<b>Was konstant bleibt</b>','<b>Gesuchte Aussage</b>'],
['A: Synchronisation aus / ein','Gleicher LokPilot-5-MKL-Projekttyp, identische Zielhersteller- und Seriennummernwerte','Welcher Registerunterschied aktiviert die Funktion? Werden weitere CVs verändert?'],
['B: Hersteller 151 / 131','Gleicher Zustand der Funktion, identisches Seriennummernfeld','Ändert die Software nur CV191 oder auch die Seriennummernbytes?'],
['C: Zwei definierte Seriennummern','Gleicher Hersteller und Aktivierungszustand','Stimmen Export und JMRI-Bytezerlegung überein?'],
],[.27,.37,.36])
r.p('Für jeden Vergleich wird derselbe gesicherte Ausgangsstand neu geöffnet. Dann ausschließlich die genannte Änderung durchführen, unter Decoder > Sonderoptionen arbeiten und den vollständigen Änderungstext sichern. Zu jeder Datei gehören Screenshot, Softwareversion, Projekttyp und die eingestellten Zahlen samt Dezimal-/Hexformat. Es wird weder „Decoderdaten schreiben“ ausgelöst noch irgendeine Projektdatei auf einen echten Decoder übertragen.'+r.ref(1))
r.p('Falls die Software die Felder beim Abschalten löscht, ihren Inhalt verändert oder die Funktion für den gewählten Projekttyp gar nicht anbietet, muss genau dieses Verhalten dokumentiert werden. Dann ist „identische Felder“ nicht erfüllt; der Unterschied darf nicht als isolierter Enable-Nachweis ausgegeben werden.')
r.sub('Was ein solcher Export klärt - und was nicht')
r.p('Ein sauberer Differenzexport kann den unbekannten Aktivierungsschritt und gegebenenfalls die Umrechnung im ESU-Eingabedialog sichtbar machen. Er beweist nicht, dass die reale Firmware des vorhandenen 59649 diese Konfiguration unterstützt. Er bestätigt auch nicht von allein, dass eine rohe Märklin-UID der richtige Eingangswert ist.')
r.p('<b>Kaufentscheidung:</b> Ein ESU-Programmer ist als Komfort-, Auslese- und Wartungswerkzeug nützlich. Für einen Parameterexport und gewöhnliche DCC-CV-Schreibvorgänge ist seine Anschaffung nicht allein aus der Aufgabenstellung ableitbar. Ein Firmwareupdate ist eine andere Tätigkeit als CV-Programmierung.')

r.start('6. CS3: einzelne CVs schreiben und kontrollieren')
r.p('<b>Diese Bedienkarte gilt erst mit einer vollständig geprüften, individuellen Werteliste.</b> Für CV191-195 fehlt diese Liste noch. Deshalb wird hier keine Hersteller-ID als fertiger Schreibwert ausgegeben. Die Reihenfolge der späteren Liste muss auch den nachgewiesenen Aktivierungsschritt enthalten; „CV191 zuletzt“ wird nicht ohne Beleg angenommen.')
r.sub('Vorbereiten: denselben einzelnen ESU verwenden')
r.p('Den 59649 wie in Abschnitt 4 allein am getrennten Programmiergleis anschließen. SERVICE ESU59649 - nicht fahren > Bearbeiten > Loks bearbeiten > den Serviceeintrag > Konfigurieren öffnen; PoM bleibt aus. Die frisch gelesenen Altwerte mit der richtigen Decoderidentität ablegen. Erst nach bestandener Aufbauprüfung STOP aufheben. Der 60977 bleibt physisch abgetrennt.')
r.sub('Pro Zeile genau dieser Ablauf')
r.p('<b>1. Nummer auswählen:</b> Die freigegebene CV-Nummer in der vorhandenen Zeile suchen. Fehlt sie, eine neue Zeile hinzufügen und nur das Nummernfeld ausfüllen. Für CV191-195 keine Index-CVs anfassen.<br/><b>2. Altwert lesen:</b> „Decoder auslesen“ auslösen, erfolgreiche Zeile kontrollieren und den Originalwert notieren. Falls der Wert von der vorbereiteten Karte abweicht, vor dem Schreiben klären, warum.<br/><b>3. Zielwert prüfen:</b> Auf der Schreibkarte CV-Nummer und Dezimalwert gegeneinander abgleichen. Der Zielwert muss für ein Byte zwischen 0 und 255 liegen. Hexzahlen mit „0x“ nicht als dezimale Zahl abtippen.<br/><b>4. Wert eingeben:</b> In derselben Zeile das <b>Wertefeld</b> antippen und ausschließlich den freigegebenen Dezimalwert eingeben. Nach Abschluss der Eingabe beziehungsweise Verlassen des Felds schreibt die CS3 den geänderten Wert direkt. <b>Kein zusätzliches „Prog.“ drücken.</b><br/><b>5. Rücklesen:</b> Abschluss abwarten, dann „Decoder auslesen“ erneut auslösen. Nur ein neu gelesener, fehlerfreier Wert, der exakt dem Ziel entspricht, gilt als bestanden.<br/><b>6. Dokumentieren:</b> Rücklesewert und Ergebnis in die Karte eintragen. Erst dann die nächste freigegebene Zeile bearbeiten.'+r.ref(15,16))
r.table([
['<b>Zeile</b>','<b>CV</b>','<b>Altwert</b>','<b>Ziel dezimal</b>','<b>Frisch gelesen</b>'],
['1 bis n','laut Freigabe','vor Schreiben','laut Freigabe','nach Schreiben'],
],[.16,.17,.20,.23,.24])
r.p('Die Tabelle ist ein Protokollschema, keine auszuführende Werteliste. Eine zusätzliche indizierte CV aus einem echten Export benötigt zuerst genau dessen CV31- und CV32-Werte. Solche zusätzlichen Register werden erst nach separater Prüfung aufgenommen, nicht aus einem anderen Decoderprojekt ergänzt.')
r.sub('Bei Fehler und am Ende')
r.p('Bei Fehlermeldung, abweichendem Rücklesewert oder unerwartetem Verhalten sofort STOP. Nicht weiterprogrammieren, nicht auf Werkseinstellung zurücksetzen. Die letzte CV kann trotz Fehlermeldung bereits geändert sein; zuerst die Ursache der fehlenden Rückmeldung prüfen. Nach erfolgreicher gesamter Liste noch einmal alle geänderten CVs lesen, Ergebnis sichern und STOP setzen. Erst danach den Programmieraufbau stromlos umstecken und den getrennten mfx-Funktionstest beginnen.')

r.start('7. Kritische Bedienfehler und konkrete Schutzregeln')
r.table([
['<b>Gefahrenstelle</b>','<b>Für diesen ICE konkret</b>'],
['CV-Nummer mit CV-Wert verwechseln','Zum Lesen der Herstellerkennung kommt 8 in das Nummernfeld. Das Wertefeld bleibt unberührt.'],
['Sofortiges Schreiben im CS3-Editor','Ein geänderter CV-Wert wird unmittelbar übernommen. Kein späterer Speicherdialog schützt vor einem vertippten Wert.'],
['Vorlagen- statt Einzelwertübertragung','„Prog.“/„Vorlagenwerte schreiben“ nicht als Bestätigung nutzen. Der Befehl kann viele Einstellungen überschreiben.'],
['Zwei Decoder am Programmiergleis','Nur den 59649 anschließen. Kupplungsbus und Master abtrennen: Ein DCC-Servicebefehl wählt nicht über die Lokadresse nur einen von beiden aus.'],
['Fehlende Quittierung','Lesefehler nicht durch wiederholtes blindes Schreiben beantworten. Bei Schreibfehlern wäre „nicht geändert“ nicht garantiert.'],
['Einmessfahrt auslösen','Bei ESU keine Kombination CV54 = 0 und danach F1. Beim Märklin-Master nicht 77 in CV7/Firmwarefeld schreiben. Für diese Aufgabe beide Felder unverändert lassen.'],
],[.34,.66])
r.p('Die CS3-Schreib- und Vorlagenfallen sind durch Märklin dokumentiert. ESU beschreibt eine schnelle automatische Einmessfahrt, die über CV54 und F1 gestartet wird. Die Märklin-mSD3-Auslösung gehört zu dessen eigener CV-Systematik; die beiden Verfahren sind nicht austauschbar.'+r.ref(14,15,16,19))
r.sub('Die Rückfallebene muss vor dem ersten Schreibvorgang stehen')
r.p('Ein späterer freigegebener Auftrag braucht je betroffener CV: Nummer, gegebenenfalls Index, frisch gelesenen Originalwert, begründeten Zielwert und erfolgreichen Rücklesewert. Ein CS3-Backup ist keine Zusage, sämtliche Decoderregister automatisch zurückzusetzen. Ein Werksreset ist ebenfalls kein Ersatz für die gesicherten Originalwerte.')
r.p('Für CV191-195 bleiben CV31 und CV32 unverändert. Sollte ein echter ESU-Export zusätzliche indizierte Register enthalten, wird deren genaue Indexfolge separat geprüft. Nicht vorsorglich eine fremde Indexgruppe schreiben. Erst recht keine aus ESU-Foren kopierten UID-Lese-CVs auf den Märklin 60977 anwenden.')
r.p('M4 wird beim ESU für den späteren Betrieb benötigt. Zur hier dokumentierten DCC-Programmiergleisprüfung gibt es keinen Grund, pauschal M4 abzuschalten, DCC-Adressen gleichzusetzen oder eine Traktion anzulegen. Solche Eingriffe würden die untersuchte Anforderung verändern, statt die Synchronisation nachzuweisen.')

r.start('8. Gegenprüfung und Anforderungsabdeckung')
r.p('Ein originaler Erfahrungsbericht von MTB-Ontour vom 26.02.2023 beschreibt einen eigenen ICE Sinus mit mSD3 im Motorkopf und LokPilot V5 M4 im Gegenkopf: Einrichtung als Slave mittels ESU-Programmer, erfolgreicher Betrieb und automatische Anmeldung. Er nennt aber keine UID/CV-Werte, Firmwarestände oder exakten Decoderartikel. Das ist ein ernstzunehmender Machbarkeitshinweis, keine übertragbare 60977/59649-Anleitung.'+r.ref(21))
r.p('Ein anderer Bericht mit „ERLEDIGT“ im Titel ist kein Gegenbeweis: Dort wurde zunächst am LokProgrammer und anschließend an einer ausschließlich mit DCC betriebenen CS3 getestet. Das kann den hier gewünschten mfx-Anmeldevorgang nicht bestätigen oder widerlegen.'+r.ref(23))
r.table([
['<b>Anforderung</b>','<b>Nach erfolgreichem Synchronisationsnachweis</b>','<b>Heute belegt?</b>'],
['Ein automatisch gefundener Zug','60977 meldet sich als Master an; kein eigenständiger Slave-Zugeintrag im normalen Betrieb.','Für genau das Paar noch zu testen.'],
['Keine Traktion','Bedienung über den mfx-Master; temporäre DCC-Service-Lok gehört nicht zum Fahrbetrieb.','Ziel der Funktion; noch kein Paar-Test.'],
['Rot/weiß sofort bei Richtungsbefehl','Beide Köpfe reagieren im Stand; kein Rollen zur Richtungserkennung nötig.','Zusätzliches Mapping und Standtest nötig.'],
['Märklin-Sound','Bleibt Aufgabe des vorhandenen 60977 und seines Soundprojekts.','Durch CV-Synchronisation nicht neu nachgewiesen.'],
['LoDi-Fronten und Innenlicht','Die gewählte Lichttechnik bleibt nutzbar; Synchronisation ersetzt keine Versorgungsschaltung.','Elektrischer Aufbau separat prüfen.'],
['Kein Zusatz-Datenkabel durch Wagen','Adresszuordnung nutzt das Gleissignal.','Kein neuer Drahtbus erforderlich; Kupplungseinbau unverändert.'],
['Kein Flackern beim Richtungswechsel','Dauerhafte Versorgung und Pufferung, nicht nur Adressgleichheit, sind entscheidend.','Mit dieser CV-Recherche nicht bewiesen.'],
],[.25,.48,.27])
r.p('Signalbremsen, Schleiferübergänge, Lastgrenzen und ununterbrochene Wagenbeleuchtung erhalten durch CV191-195 keine zusätzliche Freigabe. Insbesondere ist ein am vorderen Kopf erkannter örtlicher Bremsabschnitt keine Information, deren Übertragung die Adresssynchronisation zusichert. Dies bleibt eine eigenständige Anlagen- und Versorgungsfrage.')

r.start('9. Nachweisplan bis zur Umbaufreigabe')
r.p('Die Recherche schließt die bisherige Registerlücke. Die Umsetzung beginnt trotzdem nicht mit dem vollständigen Zug. Die folgende Reihenfolge hält Identitätsfehler, Bedienfehler und elektrische Fehler auseinander. Sie ist ein Prüfplan; nicht gemessene Ergebnisse werden nicht als bestanden eingetragen.')
r.table([
['<b>Stufe</b>','<b>Erforderliches Ergebnis</b>','<b>Aktueller Stand</b>'],
['1. Identität','Artikel 60977/59649, Firmwarestände, echte CS3-Version; eindeutig zugeordnete rohe Master-UID.','Gerätedaten/Backup fehlen.'],
['2. Kommunikation','Isolierter 59649: CV8 zweimal = 151; CV191-195 jeweils frisch und fehlerfrei gelesen.','Noch kein Hardwaretest.'],
['3. Aktivierungsexport','Offline-Differenzen erklären Enable/Disable und alle betroffenen CVs; keine Nebenänderungen unbekannt.','Noch kein Originalexport.'],
['4. Schreibkarte','Reale Masterkennung nachgewiesen; Altwerte gesichert; nur geprüfte Register und Rücklesekontrollen.','Nicht freigegeben.'],
['5. mfx-Funktion','Nur ein automatisch angemeldeter Zug; F0 und Richtungswechsel an beiden Enden bei Fahrstufe 0.','Noch offen.'],
['6. Wiederanmeldung','Erneut nachweislich andere mfx-SID; Slave folgt ohne neue Konfiguration.','Fachlich kontrollierter Test nötig.'],
],[.23,.53,.24])
r.sub('Der entscheidende Funktionstest')
r.p('Am mfx-Fahrpult des Masters werden bei Fahrstufe 0 Licht aus/ein sowie beide Richtungen geprüft. Motor-Kopf voraus muss vorne weiß und am Gegenkopf rot ergeben, in Gegenrichtung umgekehrt. Sound wird separat geprüft. Der manuelle DCC-Serviceeintrag wird nicht bedient; laufende DCC-Ereignisse dürfen das Ergebnis nicht vortäuschen.')
r.p('Ein Neustart allein beweist die Adresssynchronisation nicht, weil beide Decoder eine frühere Adresse gespeichert haben könnten. Zur Abnahme gehört eine tatsächlich neu zugewiesene, dokumentierte SID. Auch eine zweite Zentrale ist nur dann ein solcher Nachweis, wenn die Adresse nachweislich anders ist. Keine bestehende CS3-Lokdatenbank dafür pauschal löschen oder zurücksetzen.')
r.p('Als vertiefte Fachprüfung eignet sich ein kontrollierter falscher Master-Zielwert, gefolgt von einer belegten neuen Adresszuweisung und anschließendem Wiederherstellen. Dieser Negativtest ist keine Anfänger-Schreibanweisung: Er darf erst nach vollständigem Konfigurations- und Rückleseprotokoll am isolierten Prüfaufbau geplant werden.')
r.sub('Fazit')
r.p('<b>Die wirtschaftlich beste nächste Welle ist CS3 plus vorhandene Decoder, nicht ein vorsorglicher Programmerkauf.</b> Zuerst Sicherung/Identität und reiner Lesetest, parallel ein Originalexport der ESU-Sonderoption. Erst danach kann eine individuelle, zahlenfertige Schreibkarte entstehen. Der Bericht liefert einen deutlich konkreteren CV-Weg, aber noch keine Behauptung, dass der ICE bereits sicher als eine mfx-Einheit funktioniert.')

r.start('Quellen: Hersteller und Implementierung')
r.p('Quellenstand und letzte Prüfung: 10.09.2026. Quellen mit veränderlichem Inhalt wurden nach Produktgeneration und konkretem Aussageumfang eingegrenzt. Nummern entsprechen den Fußnoten. Alle Titel sind anklickbar.',SMALL)
for n in range(1,13):
    pub,title,detail,url=SOURCES[n]
    r.p(f'<b>{n}. {escape(pub)}.</b> <a href="{escape(url,quote=True)}" color="#202020">{escape(title)}</a>. {escape(detail)}.',STYLE)
r.p('JMRI-Dateien sind auf Commit '+COMMIT+' festgelegt. Die Seriennummerndarstellung lässt sich zusätzlich in <a href="'+GH+'java/src/jmri/jmrit/symbolicprog/SplitHexVariableValue.java#L48" color="#202020">SplitHexVariableValue.java</a> prüfen. Die Einführung der Register ist im <a href="https://github.com/JMRI/JMRI/commit/7d14c2747c788c1cf49eb599ddea0fd15d4b58fa" color="#202020">Commit vom 10.04.2020</a> nachvollziehbar.',SMALL)
r.p('Evidenzgrenze von JMRI: In der MKL-Modellzeile stehen unplausible Strom-/Abmessungsmetadaten; eine übersetzte Seriennummernhilfe nennt fälschlich „Dekoderversion“. Diese Angaben werden nicht übernommen. Die belastbare CV-Aussage beruht auf Variablendefinition, Einbindung und Rechenlogik gemeinsam; eine physische Decoderprüfung ersetzt das nicht.',SMALL)

r.start('Quellen: Bedienung und Gegenbelege')
for n in range(13,24):
    pub,title,detail,url=SOURCES[n]
    r.p(f'<b>{n}. {escape(pub)}.</b> <a href="{escape(url,quote=True)}" color="#202020">{escape(title)}</a>. {escape(detail)}.',STYLE)
r.sub('Umgang mit Widersprüchen')
r.p('Märklins niederländische Update-Seite nennt im präzisen Aktualisierungsabschnitt 2.6.2, während ein allgemeiner Absatz noch 2.6.1 enthält. Verwendet wird der datierte Release-Eintrag. Die CS3-Kurzanleitung ab 2.5 und das Changelog belegen die Bedienlogik; sie werden nicht als Bildschirmfoto der realen 2.6.2 ausgegeben.',SMALL)
r.p('Die ESU-Herstelleranleitung zur Synchronisation gilt ausdrücklich ihrem LokSound-5-Beispiel. Die Mindestfirmware daraus wird nicht ungeprüft auf den LokPilot 59649 übertragen. Der Ersthand-Mischbetrieb und die Originalmessungen dienen nur für die jeweils tatsächlich beschriebenen Geräte und Tests.',SMALL)
r.p('Keine manuelle Geräteprogrammierung, kein Firmwareupdate und kein physischer Testlauf ist durch diesen Bericht dokumentiert. Sein Ergebnis ist ein quellenbasierter Nachweis- und Prüfplan. Die bestehende Umbauanleitung REV7 bleibt davon unverändert.',SMALL)
r.save()

# Check the little-endian conversion independently, including unsigned boundaries.
rng=random.Random(2976)
tests=[0,1,255,256,0x12345678,0x7fffffff,0x80000000,0xffffffff]+[rng.randrange(2**32) for _ in range(1000)]
for value in tests:
    parts=[(value >> (8*i)) & 255 for i in range(4)]
    assert int.from_bytes(bytes(parts),'little') == value
    assert sum(b*256**i for i,b in enumerate(parts)) == value
assert [((0x12345678>>(8*i))&255) for i in range(4)] == [120,86,52,18]
reader=PdfReader(str(OUT))
assert len(reader.pages)==12, len(reader.pages)
assert len(reader.outline)==12
assert all(page.extract_text().strip() for page in reader.pages)
print({'output':str(OUT),'pages':len(reader.pages),'math_tests':len(tests),'layout_metrics':r.metrics,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()})
