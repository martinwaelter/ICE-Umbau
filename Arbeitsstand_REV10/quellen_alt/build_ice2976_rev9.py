"""Build a complete, paginated REV9 without altering prior PDFs or builders."""
from pathlib import Path
import hashlib,io,json,re
from pypdf import PdfReader,PdfWriter
from pypdf.annotations import Link
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

ROOT=Path(__file__).resolve().parent
TEMP=ROOT/'tmp/pdfs/rev9';TEMP.mkdir(parents=True,exist_ok=True)
OLD=ROOT/'output/pdf/ICE_2976_Umbauanleitung_REV8_VOLLSTAENDIG_CS3.pdf'
OLD_SHA=hashlib.sha256(OLD.read_bytes()).hexdigest()

builder=ROOT/'build_ice2976_rev7.py'
prelude=builder.read_text().split("scope = {'__file__':",1)[0]
context={'__file__':str(builder)}
exec(compile(prelude,str(builder),'exec'),context)
source=context['source'].replace('from rev7_content import install','from rev9_concrete_closure import install').replace('REV7','REV9')
source=source.replace('doc=ManualDoc(str(OUT)',"OUT=ROOT/'tmp/pdfs/rev9/base.pdf'\ndoc=ManualDoc(str(OUT)")
assert 'str(doc.page)' in source
source=source.replace('str(doc.page)','str(doc.page if doc.page == 1 else doc.page + 2)')
scope={'__file__':str(ROOT/'build_ice2976_rev6.py'),'__name__':'__main__'}
exec(compile(source,str(builder),'exec'),scope)
missing=[k for k,v in scope['REV9_HITS'].items() if not v]
assert not missing,missing
base=PdfReader(TEMP/'base.pdf')
assert len(base.pages)==52,('Base pagination changed',len(base.pages))
assert len(base.outline)==52,('A construction card spilled onto another page',len(base.outline))

# Reuse the full, reviewed REV8 appendix transformations, not an older research draft.
rev8=(ROOT/'build_ice2976_rev8.py').read_text()
block=rev8.split('# Incorporate independent review corrections in the newly authored appendix only.',1)[1].split("exec(compile(code,str(research),'exec')",1)[0]
ctx={'ROOT':ROOT}
exec(compile(block,str(ROOT/'build_ice2976_rev8.py'),'exec'),ctx)
code=ctx['code'].replace('tmp/pdfs/rev8/','tmp/pdfs/rev9/').replace('REV8','REV9')
code=code.replace('Die ursprüngliche REV7 bleibt unverändert erhalten; die vollständige REV9 integriert dieses Kapitel und die dazu passenden Korrekturen im Hauptteil.',
 'Frühere Fassungen bleiben unverändert erhalten. Die vollständige REV9 verbindet alle Baukarten mit diesem CV-Kapitel und den zusätzlich geprüften Handgriffen.')
code=code.replace('self.c.drawRightString(W-LEFT,28,str(self.page))','self.c.drawRightString(W-LEFT,28,str(self.page + 54))')
code=code.replace('len(reader.pages)==12','len(reader.pages)==13').replace('len(reader.pages) == 12','len(reader.pages) == 13')
code=code.replace('len(reader.outline)==12','len(reader.outline)==13')
code=code.replace("r.start('F. Quellen: Hersteller und Implementierung')",'''r.start('F.10. Dein Leseprotokoll und fehlende Nachweise')
r.p('<b>Nur lesen, keine Zielwerte raten.</b> Diese Karte gehört zu F.4. Sie dokumentiert den tatsächlichen 59649, nicht einen Offline-Beispieldecoder. Nur nach bestätigtem Prüfaufbau beginnen; 60977 physisch getrennt, PoM aus.')
r.p('Datum / Prüfender: ____________________<br/>CS3-Version/Build vom Bildschirm: ____________________<br/>Decoderartikel 59649 / Prüfaufnahme: ____________________<br/>Firmware / verlässlicher Ausleseweg: ____________________<br/>Datei/Foto des ursprünglichen Zustands: ____________________')
r.table([
['<b>CV im 59649</b>','<b>1. Auslesen</b>','<b>2. frisches Auslesen</b>','<b>Fehler / Nachweis</b>'],
['8 (Hersteller)','________','________','Erwartet 151; niemals 8 schreiben'],
['191','________','________','________'],['192','________','________','________'],
['193','________','________','________'],['194','________','________','________'],
['195','________','________','________'],
],[.20,.18,.26,.36])
r.p('Für beide Lesungen den Lesevorgang tatsächlich neu auslösen und Abschluss sowie Fehleranzeige prüfen. Bei Lesefehler nichts schreiben. Wiederholt gleiche Altwerte sind noch keine Aktivierungsfreigabe. Diese Karte enthält absichtlich keine Zielwerte und keinen Reset.')
r.sub('Wenn kein Windows-Zugang verfügbar ist')
r.p('Für Artikel 59649 eine präzise schriftliche ESU-Bestätigung oder einen Original-Differenzexport anfordern: (1) sämtliche Aktivierungs-/Deaktivierungs-CVs und benötigte LokPilot-Firmware; (2) zulässige Herstellerkennung und exakte Übertragung einer Märklin-mSD3-Roh-UID in das ESU-Seriennummernfeld; (3) vollständige Exportfolge mit Indexwerten, soweit erforderlich. Das allgemeine ESU/ESU-Tutorial allein beantwortet diese Punkte nicht.')
r.p('Ein passender Originalnachweis kann den Windows-Offlineversuch ersetzen, nicht die abschließende Funktionsprüfung deines Decoderpaars. Es wurde keine Herstelleranfrage versendet und keine Antwort vorausgesetzt. Separat bleiben Fotos von LoDi-Rückseite/Revision, hinterer Halterung und LED-Einsätzen erforderlich.')

r.start('F. Quellen: Hersteller und Implementierung')''')
exec(compile(code,str(ROOT/'build_ice2976_cv_cs3_research.py'),'exec'),{'__file__':str(ROOT/'build_ice2976_cv_cs3_research.py'),'__name__':'__main__'})
appendix=PdfReader(TEMP/'cv_appendix.pdf')
assert len(appendix.pages)==13

def image_hashes(reader):
    values=[]
    for page in reader.pages:
        for value in page.get('/Resources',{}).get('/XObject',{}).values():
            obj=value.get_object()
            if obj.get('/Subtype')=='/Image':values.append(hashlib.sha256(obj.get_data()).hexdigest())
    return sorted(values)
assert image_hashes(PdfReader(OLD))==image_hashes(base),'A source image was changed or lost'

# Navigation is generated from actual PDF destinations, never a hand-maintained page list.
entries=[]
for item in base.outline:
    p=base.get_destination_page_number(item)
    entries.append((str(item.title),p if p==0 else p+2))
for item in appendix.outline:
    entries.append((str(item.title),54+appendix.get_destination_page_number(item)))
assert len(entries)==65
toc_path=TEMP/'navigation.pdf'
c=canvas.Canvas(str(toc_path),pagesize=(595.28,841.89))
toc_style=ParagraphStyle('toc',fontName='A',fontSize=9.4,leading=12,textColor=colors.HexColor('#20252A'))
links=[]
for sheet,chunk in enumerate((entries[:33],entries[33:]),2):
    c.bookmarkPage('nav'+str(sheet));c.addOutlineEntry('Orientierung '+str(sheet-1),'nav'+str(sheet),0)
    c.setFont('AB',20);c.drawString(42,798,'Orientierung '+str(sheet-1)+' von 2')
    c.setFont('A',9.4);c.drawString(42,775,'Kapitel anklicken. Gedruckte Seitenzahlen entsprechen den PDF-Seiten.')
    if sheet==2:
        note='Zuerst A-C und F: Nachweise am Decoderpaar. Den ICE erst nach bestandenem G0 zerlegen. Einsetzseiten 9c/12b vorher nur lesen; Decoder erst vor 52/54 stecken.'
    else:
        note='Die vollständigen Bau- und Prüfkapitel bleiben erhalten. Die neue Lesekarte F.10 sammelt echte Werte; sie gibt noch keine Synchronisations-Zielwerte frei.'
    p=Paragraph(note,toc_style);_,h=p.wrap(511,80);p.drawOn(c,42,748-h)
    y=701
    for title,target in chunk:
        p=Paragraph(title,toc_style);_,h=p.wrap(460,40)
        assert h<=24,title
        p.drawOn(c,42,y-h)
        c.setFont('A',9.4);c.drawRightString(551,y-10,str(target+1))
        links.append((sheet-1,(40,y-h-2,553,y+2),target))
        y-=max(17,h+4)
    assert y>60,(sheet,y)
    c.setFont('A',8);c.setFillColor(colors.HexColor('#53606A'));c.drawString(42,24,'REV9 - ICE 2976; Dokumentfassung mit offenen Hardware-Nachweisen');c.drawRightString(553,24,str(sheet));c.setFillColor(colors.black);c.showPage()
c.save()

writer=PdfWriter()
writer.append(base,pages=(0,1),import_outline=True)
writer.append(PdfReader(toc_path),import_outline=True)
writer.append(base,pages=(1,len(base.pages)),import_outline=True)
writer.append(appendix,import_outline=True)
for page_index,rect,target in links:
    writer.add_annotation(page_index,Link(rect=rect,target_page_index=target))
    writer.pages[page_index]['/Annots'][-1].get_object()['/Dest'][0]=writer.pages[target].indirect_reference
writer.add_metadata({'/Title':'ICE 2976 - vollständige Umbauanleitung REV9 mit CS3-CV-Programmierung','/Author':'','/Subject':'Vollständige Dokumentfassung; konkrete Handgriffe und explizite offene Hardware-Nachweise'})
OUT=ROOT/'output/pdf/ICE_2976_Umbauanleitung_REV9_VOLLSTAENDIG_CS3.pdf'
with OUT.open('wb') as stream:writer.write(stream)
final=PdfReader(OUT)
assert len(final.pages)==67 and len(final.outline)==67
assert hashlib.sha256(OLD.read_bytes()).hexdigest()==OLD_SHA
assert image_hashes(final)==image_hashes(PdfReader(OLD))

# Exact section mapping supports lossless comparison of old and new construction pages.
mapping=[]
for old_num,item in enumerate(PdfReader(OLD).outline):
    old_title=str(item.title).replace('REV8','REV9')
    matches=[(title,p) for title,p in entries if title==old_title]
    assert len(matches)==1,(old_title,matches)
    mapping.append({'old':old_num+1,'new':matches[0][1]+1,'title':old_title})
report={'output':str(OUT),'pages':67,'bookmarks':67,'toc_links':len(links),'bitmap_instances':len(image_hashes(final)),'old_sha256':OLD_SHA,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'mapping':mapping,'replacement_hits':scope['REV9_HITS']}
(TEMP/'build_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ('mapping','replacement_hits')},ensure_ascii=False,indent=2))
