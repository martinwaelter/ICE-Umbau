from pathlib import Path
from copy import deepcopy
from html import unescape,escape
import json,re,hashlib
from pypdf import PdfReader
from layout import Layout
ROOT=Path(__file__).resolve().parent;PROJECT=ROOT.parent
BASE=PROJECT/'output/pdf/ICE_2976_Umbauanleitung_REV12_WERKSTATTFASSUNG.pdf'
assert hashlib.sha256(BASE.read_bytes()).hexdigest()=='95af61083373a0755fde8ebd5ae70233952f6283b3db652b03e71c26582bcc8e'
P={p['n']:deepcopy(p) for p in json.loads((PROJECT/'Arbeitsstand_REV12/rev12_pages.json').read_text())}
S={}
for b in P[44]['blocks']:
 m=re.search(r'<link href="([^"]+)"[^>]*><b>(Q\d+)</b> (.*?)</link>',b.get('text',''))
 if m:S[m[2]]={'id':m[2],'title':unescape(m[3]),'url':unescape(m[1])}
for name in ['sequence_changes','programming_changes','electrical_changes','root_changes']:
 module=__import__(name);module.apply(P)
 for s in getattr(module,'SOURCES',[]):
  if isinstance(s,dict):S[s['id']]=s
  else:S[s[0]]={'id':s[0],'title':s[1],'url':s[2]}
S['Q9']['title']='Märklin CS3-Changelog 2.6.0: CV-Lesen und Lesefehler'
S['Q26']['title']='Märklin CS3-Kurzanleitung ab V2.5: Anschlüsse; GFP3/Netzteil S.26'
S['Q5']['title']='LoDi-Shop: Abschnitt ICE-M Front 2 Stück, ohne Vorwiderstände'
order=[1,2,45,46,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,38,31,37,39,40,41,42,43,44]
assert len(order)==len(set(order))==46 and set(order)==set(P)
mapping={v:i for i,v in enumerate(order,1)}
def conv(x):
 if isinstance(x,str):
  x=re.sub(r'\[\[(\d+)\]\]',lambda m:'[['+str(mapping[int(m[1])])+']]',x)
  return x.replace('ICE2976_REV12','ICE2976_REV13').replace('G0','CS3-Paarprüfung')
 if isinstance(x,list):return [conv(a) for a in x]
 if isinstance(x,dict):return {k:conv(v) for k,v in x.items()}
 return x
from root_changes import small,p
P[44]['goal']='Direkte Quellen und Bildherkunft. Stand 12.09.2026; persönliche Werte und tatsächliche Prüfungen werden am eigenen Material erhoben.'
P[44]['blocks']=[dict(small(f'<link href="{escape(s["url"],quote=True)}" color="#145B64"><b>{s["id"]}</b> {escape(s["title"])}</link>'),after=2) for s in sorted(S.values(),key=lambda s:int(s['id'][1:]))]
P[44]['blocks'] += [p('<b>Bildherkunft:</b> Eigene Fotos aus REV10; Märklin-Zeichnungen Q1/Q2/Q18. LoDi-Fotos zeigen den Vergleichsumbau 33701. Alle REV12-Fotoquellen sind erhalten. Markierungen sind getrennte Überlagerungen; eigene Funktionsschemata zeigen keine maßstäbliche Padlage.'),small('REV13 korrigiert belegte Lücken und sinnvolle Klarstellungen aus dem REV12-Bericht. Unbelegte Freigabewerte wurden nicht übernommen. Eigene Ableitungen und offene Hardwareergebnisse bleiben gekennzeichnet. REV10/REV11/REV12 und Originalberichte bleiben erhalten.')]
P[44]['check']=''
# Keep the start map tied to the final page numbers.
for b in P[1]['blocks']:
 if b.get('type')=='table' and len(b.get('rows',[]))==6:
  b['rows']=[['Vorbereitung, Prüfplatz, Kupplungen',f'2–{mapping[5]}','Arbeitsplatz und reale Voraussetzungen vor Umbau'],['Decoder vorbereiten und Paar prüfen',f'{mapping[6]}–{mapping[12]}','Gerätefolge, Rohwerte und tatsächliche Reaktion'],['Motor, Fronten und Gegenkopf',f'{mapping[13]}–{mapping[24]}','Montage, Messzugang, Anschluss und LED-Zweige'],['Wagen, Konfiguration und Ersttests',f'{mapping[25]}–{mapping[36]}','Kupplungen, Lastplanung und getrennte Einzeltests'],['Anlage, Last und Endabnahme',f'{mapping[38]}–{mapping[41]}','Erst Bereich, dann Laststufen, T1–T9 und Gehäuse'],['Fehler, Ergänzungen und Quellen',f'{mapping[42]}–{mapping[44]}','Wartung, Puffer und Nachschlagen']]
pages=[]
for n in order:
 item=conv(deepcopy(P[n]));item['rev12_card']=n;item['n']=mapping[n];pages.append(item)
for p in pages:
 assert set(p.get('sources',[]))<=set(S),(p['n'],set(p.get('sources',[]))-set(S))
for n in re.findall(r'\[\[(\d+)\]\]',json.dumps(pages)):assert 1<=int(n)<=46
(ROOT/'rev13_pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
(ROOT/'sources.json').write_text(json.dumps(list(S.values()),ensure_ascii=False,indent=2))
OUT=PROJECT/'output/pdf/ICE_2976_Umbauanleitung_REV13_WERKSTATTFASSUNG.pdf';TMP=PROJECT/'tmp/pdfs/rev13';TMP.mkdir(parents=True,exist_ok=True)
layout=Layout(OUT,pages);layout.build();r=PdfReader(OUT)
assert len(r.pages)==46 and len(r.outline)==46
report={'output':str(OUT),'pages':46,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'links':sum(len(p.get('/Annots',[])) for p in r.pages),'figure_placements':len(layout.figures),'figures':layout.figures,'source_count':len(S),'rev12_to_rev13':mapping,'words_by_page':[len((p.extract_text() or '').split()) for p in r.pages]}
(TMP/'build_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));(TMP/'placements.json').write_text(json.dumps(layout.placements,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['figures','rev12_to_rev13','words_by_page']},ensure_ascii=False,indent=2))
