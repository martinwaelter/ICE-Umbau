from pathlib import Path
from copy import deepcopy
import re,json,hashlib
from pypdf import PdfReader
from content import PAGES,SOURCES
from layout import Layout
ROOT=Path(__file__).resolve().parent;PROJECT=ROOT.parent
OUT=PROJECT/'output/pdf/ICE_2976_Umbauanleitung_REV11_WERKSTATTFASSUNG.pdf'
TMP=PROJECT/'tmp/pdfs/rev11'
TMP.mkdir(exist_ok=True,parents=True)
assert len(PAGES)==40
order=[1,2,3,21,22,4,5,6,7,8,9,10,11,12,13,14,18,15,16,17,19,20]+list(range(23,41))
assert len(set(order))==40
mapping={old:new for new,old in enumerate(order,1)}
def convert(x):
 if isinstance(x,str):return re.sub(r'\[\[(\d+)\]\]',lambda m:'[['+str(mapping[int(m[1])])+']]',x)
 if isinstance(x,list):return [convert(a) for a in x]
 if isinstance(x,dict):return {k:convert(v) for k,v in x.items()}
 return x
pages=[]
for i,n in enumerate(order,1):
 item=convert(deepcopy(PAGES[n]));item['original_card']=n;item['n']=i
 pages.append(item)
# Fixed overview ranges reflect final reading order.
rows=pages[0]['blocks'][2]['rows']
rows[0]=['Vorbereiten, Messmethoden, Decoder prüfen','2-11','Sichere Einzelaufnahmen und gemeinsamer mfx-Test']
rows[1]=['Motor, Platinen und Fronten montieren','12-22','Geprüfte Mechanik und eindeutige Verdrahtung']
rows[2]=['Mittelwagen und Kupplungen','23-26','Einzelübergänge, O/L und optionale Radkontakte']
# Source/reference assertions keep page links and IDs auditable.
raw=json.dumps(pages,ensure_ascii=False)
for s in re.findall(r'\[\[(\d+)\]\]',raw):assert 1<=int(s)<=40
source_ids={s[0] for s in SOURCES}
for p in pages:
 assert set(p.get('sources',[]))<=source_ids
base=PROJECT/'ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf'
orig=hashlib.sha256(base.read_bytes()).hexdigest()
assert orig=='2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0'
(ROOT/'rev11_pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
layout=Layout(OUT,pages);layout.build()
r=PdfReader(OUT);assert len(r.pages)==40;assert len(r.outline)==40
assert hashlib.sha256(base.read_bytes()).hexdigest()==orig
report={'output':str(OUT),'pages':40,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'original_rev10_sha256':orig,'original_unchanged':True,'links':sum(len(p.get('/Annots',[])) for p in r.pages),'figure_placements':len(layout.figures),'figures':layout.figures,'source_count':len(SOURCES),'old_to_new':mapping,'words_by_page':[len((p.extract_text() or '').split()) for p in r.pages]}
(TMP/'build_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
(TMP/'placements.json').write_text(json.dumps(layout.placements,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['figures','old_to_new','words_by_page']},ensure_ascii=False,indent=2))
