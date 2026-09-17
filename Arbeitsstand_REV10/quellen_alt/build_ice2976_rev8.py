"""Publish one complete REV8 with all REV7 construction pages and the detailed CV appendix."""
from pathlib import Path
import hashlib
import io
import json
import re
from pypdf import PdfReader,PdfWriter
from reportlab.pdfgen import canvas

ROOT=Path(__file__).resolve().parent
TEMP=ROOT/'tmp/pdfs/rev8'
TEMP.mkdir(parents=True,exist_ok=True)
OLD=ROOT/'output/pdf/ICE_2976_Umbauanleitung_REV7_KONKRET.pdf'
old_sha=hashlib.sha256(OLD.read_bytes()).hexdigest()

# Reconstruct the already reviewed full page stream without executing its old export.
builder=ROOT/'build_ice2976_rev7.py'
prelude=builder.read_text().split("scope = {'__file__':",1)[0]
context={'__file__':str(builder)}
exec(compile(prelude,str(builder),'exec'),context)
source=context['source'].replace('from rev7_content import install','from rev8_cv_integration import install')
source=source.replace('REV7','REV8')
source=source.replace('output/pdf/ICE_2976_Umbauanleitung_REV8_KONKRET.pdf','tmp/pdfs/rev8/base.pdf')
source=source.replace('doc=ManualDoc(str(OUT)', "OUT=ROOT/'tmp/pdfs/rev8/base.pdf'\ndoc=ManualDoc(str(OUT)")
scope={'__file__':str(ROOT/'build_ice2976_rev6.py'),'__name__':'__main__'}
exec(compile(source,str(builder),'exec'),scope)
assert not [k for k,v in scope['REV8_HITS'].items() if not v], scope['REV8_HITS']

# Incorporate independent review corrections in the newly authored appendix only.
research=ROOT/'build_ice2976_cv_cs3_research.py'
code=research.read_text()
fixes=[
('output/pdf/ICE_2976_CV_CS3_FORENSISCHER_NACHWEIS.pdf','tmp/pdfs/rev8/cv_appendix.pdf'),
('S. 13-15: Lok bearbeiten/CV; S. 25 und 27: System und Sicherung','S. 13-14: Lok anlegen/bearbeiten; S. 25 und 27: System und Sicherung'),
("['<b>CS3</b><br/>meldet den Master an; vergibt mfx-Adresse','<b>60977</b><br/>Master für Motor, Sound und lokale Funktionen','<b>59649</b><br/>soll derselben Adresse auf dem Gleis folgen']", "['<b>CS3</b><br/>ordnet dem Master eine mfx-Adresse zu','<b>Gleissignal</b><br/>Anmeldung und Befehle stehen beiden Decodern zur Verfügung','<b>60977 + 59649</b><br/>Master und konfigurierter Slave sollen gemeinsam folgen']"),
('Danach nochmals wirklich lesen und beide Ergebnisse dokumentieren.','Danach „Decoder auslesen“ ein zweites Mal betätigen, Abschluss abwarten und den neuen CV8-Wert dokumentieren.'),
("überhaupt nicht benutzt.'+r.ref(16)", "überhaupt nicht benutzt.'+r.ref(14,16)"),
('Den 59649 wie in Abschnitt 4 allein am getrennten Programmiergleis anschließen. SERVICE ESU59649 - nicht fahren > Bearbeiten > Loks bearbeiten > den Serviceeintrag > Konfigurieren öffnen; PoM bleibt aus. Die frisch gelesenen Altwerte mit der richtigen Decoderidentität ablegen. Erst nach bestandener Aufbauprüfung STOP aufheben. Der 60977 bleibt physisch abgetrennt.',
 'Die CS3 auf STOP stellen. Den geprüften 59649-Aufbau wie in Abschnitt 4 allein am getrennten Programmiergleis anschließen. Bearbeiten > Loks bearbeiten > SERVICE ESU59649 - nicht fahren > Konfigurieren öffnen; PoM bleibt aus. Die in Abschnitt 4 gesicherten Altwerte bereitlegen. Erst nach Aufbauprüfung STOP aufheben. Frisches Lesen folgt in Schritt 2. Der 60977 bleibt physisch abgetrennt.'),
('Abschluss abwarten, dann „Decoder auslesen“ erneut auslösen.', 'Den Dialog bis zum Abschluss des Schreibens offen lassen; dann „Decoder auslesen“ erneut auslösen.'),
('Dauerhafte Versorgung und Pufferung, nicht nur Adressgleichheit, sind entscheidend.', 'Richtungsunabhängige Versorgung und separates Innenlicht-Mapping nach 16a/17a. Pufferung betrifft echte Kontaktunterbrechungen, nicht die Richtungsumschaltlücke.'),
('Dieser Nachweisbericht ergänzt REV7, ersetzt aber weder deren Isolationsprüfungen noch die ausstehende Funktionsabnahme.', 'Kapitel F ergänzt die vollständige REV8. Seine eigenen Quellennummern gelten nur in F; alle Isolationsprüfungen und die ausstehende Funktionsabnahme bleiben erforderlich.'),
('Die bestehende Umbauanleitung REV7 bleibt davon unverändert.', 'Die ursprüngliche REV7 bleibt unverändert erhalten; die vollständige REV8 integriert dieses Kapitel und die dazu passenden Korrekturen im Hauptteil.'),
]
for before,after in fixes:
    assert before in code,before
    code=code.replace(before,after)
code=code.replace('in Abschnitt 4','in Abschnitt F.4')
code=code.replace("r.start('ICE 2976: CV-Programmierung mit der CS3',main=True)","r.start('F. CV-Programmierung mit der CS3',main=True)")
for n in range(1,10):
    code=code.replace("r.start('"+str(n)+'. ',"r.start('F."+str(n)+'. ')
code=code.replace("r.start('Quellen:","r.start('F. Quellen:")
exec(compile(code,str(research),'exec'),{'__file__':str(research),'__name__':'__main__'})

base=PdfReader(TEMP/'base.pdf')
appendix=PdfReader(TEMP/'cv_appendix.pdf')
old=PdfReader(OLD)
assert len(base.pages)==len(old.pages)==48,(len(base.pages),len(old.pages))
assert len(appendix.pages)==12

# Verify that all illustrations and all unaffected text pages survive the rebuild.
def image_data(reader):
    found=[]
    for page in reader.pages:
        for obj in page.get('/Resources',{}).get('/XObject',{}).values():
            o=obj.get_object()
            if o.get('/Subtype')=='/Image':
                found.append(hashlib.sha256(o.get_data()).hexdigest())
    return sorted(found)
assert image_data(old)==image_data(base),'An existing bitmap changed or disappeared'
def normalized(text):
    return re.sub(r'\s+','',text.replace('REV7','REV8'))
changed=[]
for i,(a,b) in enumerate(zip(old.pages,base.pages),1):
    if normalized(a.extract_text())!=normalized(b.extract_text()): changed.append(i)
allowed={1,3,4,5,6,25,45,46,48}
assert set(changed)<=allowed,('Unexpected text change',changed)

writer=PdfWriter()
writer.append(base,import_outline=True)
writer.append(appendix,import_outline=True)
for i,page in enumerate(writer.pages[48:],49):
    layer=io.BytesIO()
    c=canvas.Canvas(layer,pagesize=(595.28,841.89))
    c.setFillColorRGB(1,1,1);c.rect(510,17,52,24,fill=1,stroke=0)
    c.setFillColorRGB(.32,.32,.32);c.setFont('Helvetica',8);c.drawRightString(549.28,28,str(i))
    c.save();layer.seek(0)
    page.merge_page(PdfReader(layer).pages[0])
writer.add_metadata({'/Title':'ICE 2976 - vollständige Umbauanleitung REV8 mit CS3-CV-Programmierung','/Author':'','/Subject':'Vollständiger Umbauumfang; konkrete CS3-Bedienung und noch offene Synchronisationsnachweise'})
OUT=ROOT/'output/pdf/ICE_2976_Umbauanleitung_REV8_VOLLSTAENDIG_CS3.pdf'
with OUT.open('wb') as stream: writer.write(stream)
assert hashlib.sha256(OLD.read_bytes()).hexdigest()==old_sha
final=PdfReader(OUT)
assert len(final.pages)==60
assert len(final.outline)==60
print(json.dumps({'output':str(OUT),'pages':len(final.pages),'bookmarks':len(final.outline),'changed_base_pages':changed,'preserved_bitmap_instances':len(image_data(old)),'rev7_unchanged_sha256':old_sha,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False,indent=2))
