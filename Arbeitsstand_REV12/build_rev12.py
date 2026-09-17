from pathlib import Path
from copy import deepcopy
import json,re,hashlib,sys
from pypdf import PdfReader
from overrides import PAGES
from layout import Layout
ROOT=Path(__file__).resolve().parent;PROJECT=ROOT.parent
sys.path.append(str(PROJECT/'Arbeitsstand_REV11'))
from content import SOURCES as ORIGINAL_SOURCES
SOURCES=deepcopy(ORIGINAL_SOURCES)
SOURCES.extend([
 ('Q24','Märklin: CV-Editor, Vorlagenwerte und Zahleneingabe','https://www.maerklin.de/fileadmin/media/clubs/downloads/Loks_CV_Editor.pdf'),
 ('Q25','JMRI SplitVariableValue: abgeleitete Byte-Reihenfolge','https://github.com/JMRI/JMRI/blob/31e482094d472e481c1fb54f9901093c2efbfcec/java/src/jmri/jmrit/symbolicprog/SplitVariableValue.java'),
 ('Q26','Märklin CS3-Handbuch: Programmiergleis und GFP3-Anzeige','https://static.maerklin.de/damcontent/c1/ce/c1ce554ad6ad195c04e32ba1b4dd64511764068661.pdf'),
 ('Q27','Fluke 87/89: Widerstandsmessung und Bauteilpfade','https://assets.fluke.com/manuals/87_89iv_umeng0200.pdf'),
 ('Q28','RailCommunity RCN-210: DCC-Gleissignal und Asymmetrie','https://normen.railcommunity.de/RCN-210.pdf'),
 ('Q29','ESU 53900: originale Prüfstand-Anleitung','https://www.esu.eu/download/betriebsanleitungen/profi-pruefstand/?no_cache=1&tx_esudownloads_pi1%5BdownloadItem%5D=3e2cdb190091da48cc2030b2734bbd32'),
 ('Q30','Märklin 60941: Eignung für Trommelkollektormotoren','https://www.marklin.com/products/details/article/60941'),
 ('Q33','Tektronix: Stromsonde und Messwiderstand am Oszilloskop','https://www.tek.com/en/documents/application-note/making-accurate-current-measurements-power-supplies-oscilloscopes'),
 ('Q34','Fluke: Kondensatoren entladen und Spannung nachprüfen','https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-measure-capacitance'),
])

# Agent additions use existing REV11 card identifiers. Renumber only once below.
for name in ['programming_replacements.json']:
 path=ROOT/name
 if not path.exists():raise FileNotFoundError(path)
 data=json.loads(path.read_text())
 if isinstance(data,dict) and 'replacements' in data:
  for s in data.get('additional_sources',[]):
   if s['id'] not in {x[0] for x in SOURCES}:SOURCES.append((s['id'],s['title'],s['url']))
  data=data['replacements']+data.get('additional_pages',[])
 elif isinstance(data,dict) and 'pages' in data:data=data['pages']
 if isinstance(data,dict):data=[dict(v,n=int(k)) for k,v in data.items()]
 for p in data:PAGES[int(p['n'])]=p
PAGES[41]['blocks'][0]={'type':'figure','path':str(ROOT/'60970_schalter.png'),'maxh':190,'crop':[.04,.31,.78,.923]}
from electrical import apply_electrical
apply_electrical(PAGES)
SOURCES.sort(key=lambda x:int(x[0][1:]))

order=[1,2,3,4,5,6,41,7,8,9,10,11,12,13,14,15,16,17,42,18,19,20,21,22,23,24,25,26,27,28,43,29,30,31,32,33,34,44,35,36,37,38,39,40]
assert len(order)==len(set(order))==44
assert set(order)==set(PAGES),(set(order)-set(PAGES),set(PAGES)-set(order))
mapping={n:i for i,n in enumerate(order,1)}
def convert(x):
 if isinstance(x,str):
  return re.sub(r'\[\[(\d+)\]\]',lambda m:'[['+str(mapping[int(m[1])])+']]',x).replace('ICE2976_REV11','ICE2976_REV12')
 if isinstance(x,list):return [convert(a) for a in x]
 if isinstance(x,dict):return {k:convert(v) for k,v in x.items()}
 return x
from overrides import small,p,tab
PAGES[40]['goal']='Direkte Originalquellen und Bildherkunft. Quellenstand 11.09.2026; persönliche Messergebnisse bleiben vom Anwender zu erheben.'
PAGES[40]['blocks']=[dict(small(f'<link href="{url.replace("&","&amp;")}" color="#145B64"><b>{key}</b> {label}</link>'),after=3) for key,label,url in SOURCES]
PAGES[40]['blocks'] += [p('<b>Bildherkunft:</b> Eigene Fotos unverändert aus deiner REV10; Märklin-Zeichnungen aus Q1/Q2/Q18; LoDi-Vergleichsfotos zeigen den Herstellerumbau 33701, nicht deinen fertig umgebauten Zug. Nummern liegen als separate Markierungen über den Bildern. Eigene Funktionsschemata behaupten keine maßstäbliche Padlage.'),small('REV12 korrigiert die Ausführungslücken der REV11. Ausgewählte Messungen wurden konkretisiert, SID-Erweiterung und tatsächliche Lastabnahme getrennt. Originale REV10/REV11 und die nachvollziehbaren Prüfberichte bleiben erhalten. Keine Hardwareprüfung wurde als bereits durchgeführt eingetragen.')]
PAGES[40]['check']=''
rows=PAGES[1]['blocks'][2]['rows']
rows[0]=['Vorbereitung und eigene CS3-Paarprüfung',f'2–{mapping[11]}','Klare Gerätefolge, Identität und tatsächlich folgende Ausgänge']
rows[1]=['Motor, Platinen und Fronten',f'{mapping[12]}–{mapping[22]}','Motorprüfung, LED-Zweige, sichere Montage und Verdrahtung']
rows[2]=['Mittelwagen und Kupplungen',f'{mapping[23]}–{mapping[26]}','Jeder Übergang; optionale Radkontakte ohne Abnahmeschleife']
rows[3]=['Konfiguration, Last und Erststrom',f'{mapping[27]}–{mapping[33]}','Einzelköpfe, tatsächliche Messungen und definierte Laststufen']
rows[4]=['Zug, Anlage und Gehäuseabschluss',f'{mapping[34]}–{mapping[37]}','T1–T9, eigener Anlagenbereich und geschlossene Endprüfung']
rows[5]=['Fehler, spätere Ergänzungen, Quellen',f'{mapping[38]}–{mapping[40]}','Wartung, Puffer und Signalhalt getrennt']
pages=[]
for i,n in enumerate(order,1):
 item=convert(deepcopy(PAGES[n]));item['original_card']=n;item['n']=i;pages.append(item)
raw=json.dumps(pages,ensure_ascii=False)
for s in re.findall(r'\[\[(\d+)\]\]',raw):assert 1<=int(s)<=44
ids={s[0] for s in SOURCES}
for p in pages:assert set(p.get('sources',[]))<=ids,(p['n'],p.get('sources'))
OUT=PROJECT/'output/pdf/ICE_2976_Umbauanleitung_REV12_WERKSTATTFASSUNG.pdf';TMP=PROJECT/'tmp/pdfs/rev12';TMP.mkdir(exist_ok=True,parents=True)
base=PROJECT/'ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf';prev=PROJECT/'output/pdf/ICE_2976_Umbauanleitung_REV11_WERKSTATTFASSUNG.pdf'
assert hashlib.sha256(base.read_bytes()).hexdigest()=='2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0'
assert hashlib.sha256(prev.read_bytes()).hexdigest()=='3c67f596856f5403eac6f27f1f2512379555d3611749e4a7bd94f817cc7e41cb'
(ROOT/'rev12_pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
layout=Layout(OUT,pages);layout.build();r=PdfReader(OUT)
assert len(r.pages)==44 and len(r.outline)==44
report={'output':str(OUT),'pages':44,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'links':sum(len(p.get('/Annots',[])) for p in r.pages),'figure_placements':len(layout.figures),'figures':layout.figures,'source_count':len(SOURCES),'old_to_new':mapping,'words_by_page':[len((p.extract_text() or '').split()) for p in r.pages]}
(TMP/'build_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));(TMP/'placements.json').write_text(json.dumps(layout.placements,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['figures','old_to_new','words_by_page']},ensure_ascii=False,indent=2))
