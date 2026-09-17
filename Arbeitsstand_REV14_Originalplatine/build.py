from pathlib import Path
from copy import deepcopy
from html import escape
import sys,json,re,hashlib
from pypdf import PdfReader
from layout import Layout
from root_changes import apply,finish,compact_and_correct,setpage,p,small
ROOT=Path(__file__).resolve().parent;PROJECT=ROOT.parent
sys.path.insert(0,str(PROJECT/'Arbeitsstand_Originalplatine'))
REF=PROJECT/'output/pdf/ICE_2976_Umbauanleitung_REV13_WERKSTATTFASSUNG.pdf'
assert hashlib.sha256(REF.read_bytes()).hexdigest()=='6a4afec36193952fa0a7040fc230c9c37356e71968e5b3dcd6244347d4308bce'
P={x['n']:deepcopy(x) for x in json.loads((PROJECT/'Arbeitsstand_REV13/rev13_pages.json').read_text())}
def repl(v):
 if isinstance(v,str):return v.replace('[[9]]','[[8]]').replace('ICE2976_REV13','ICE2976_REV14_Originalplatine')
 if isinstance(v,list):return [repl(z) for z in v]
 if isinstance(v,dict):return {k:repl(z) for k,z in v.items()}
 return v
P=repl(P);apply(P)
__import__('guide_ablauf_changes').apply(P)
L=[P[n] for n in range(1,47)]
for name in ['guide_decoder_changes','guide_elektrik_changes']:__import__(name).apply(L)
finish(P)
compact_and_correct(P)
S={x['id']:x for x in json.loads((PROJECT/'Arbeitsstand_REV13/sources.json').read_text())}
news=[('Q37','62762 beidseitige Originalfotos: Kleinanzeigen, Artikel 3331585671','https://www.kleinanzeigen.de/s-anzeige/maerklin-h0-3370-ice-3x-leiterplatten/3331585671-249-611'),('Q38','Märklin 3370: Explosionszeichnung,627620 Pos27 am Gegenkopf','https://static.maerklin.de/damcontent/ac/29/ac29ce530a37bf0a5e5e04986eed4c3a1434542471.pdf'),('Q39','Märklin 60972/60982: deutsche Anschluss-/Trägerzeichnung S5–6','https://static.maerklin.de/damcontent/da/e4/dae4fa90473657b9466d908bd6dcfa601663856106.pdf'),('Q40','ML-Train 84002016: Relaismodul,Spannung,Strom und Abmessungen','https://www.ml-train.de/herzstck-relaisplatine-weichen-train-84002016-p-531.html'),('Q41','mXion LSD Anleitung: MD-0016 Anschlussgrafik, S.35–36','https://www.micron-dynamics.de/sitecake-content/mXion%20LSD.pdf'),('Q42','Zweites62762-Bildpaar: eBay,Artikel 147416253187','https://www.ebay.de/itm/147416253187')]
for i,t,u in news:S[i]={'id':i,'title':t,'url':u}
used=set(q for x in P.values() if x['n']!=46 for q in x.get('sources',[]));used|={'Q42'}
ss=sorted([s for q,s in S.items() if q in used],key=lambda s:int(s['id'][1:]))
for n,part in [(46,ss[:22]),(47,ss[22:])]:
 blocks=[dict(small(f'<link href="{escape(s["url"],quote=True)}" color="#145B64"><b>{s["id"]}</b> {escape(s["title"])}</link>'),after=5) for s in part]
 if n==47:
  blocks += [p('<b>Bildherkunft:</b> Eigene 2976-Fotos aus REV10; Märklin-Zeichnungen Q1/Q2/Q39; weiße LoDi-Wagenfotos Q4. Fremde 62762-Fotos Q37, unabhängig gegengeprüft mit Q42 und hochauflösendem Vergleich Q3. Bilder belegen Form und sichtbare Anschlüsse, keine ungesehenen Leiterbahnfunktionen.'),p('<b>Eigene Auslegungen:</b> Elektrisch unabhängiger Aufbau auf 62762, ein aktiver Schleifer, Relaisversorgung der Wagen und konservative 47-kΩ-Frontzweige. Sie sind von Herstellerangaben getrennt gekennzeichnet. Maße, Zuordnung und tatsächliche Prüfwerte werden am eigenen Fahrzeug erhoben.'),small('Diese Ausgabe ersetzt für die Originalplatinenvariante die verstreuten Arbeitsstände. Die LoDi-REV13 bleibt als separate Alternative erhalten. Fertiggestellt ist das Dokument; Hardwareumbau und Abnahme sind vom Nutzer auszuführen. Stand 12.09.2026.')]
 setpage(P,n,'Quellen und Bildnachweise'+(' – Fortsetzung' if n==47 else ''),'Direktlinks zum belegten Material. Die Quellen-IDs der Fußzeilen führen zu dieser Übersicht.',blocks,phase='Nachschlagen | Quellen')
order=[1,2,3,4,5,6,7,9,19,15,16,17,18,22,23,24,25,26,20,8,10,11,12,13,31,32,33,34,35,36,21,37,14,27,28,29,30,38,39,40,41,42,43,44,45,46,47]
assert len(order)==len(set(order))==len(P)
mp={n:i for i,n in enumerate(order,1)}
def convert(v):
 if isinstance(v,str):return re.sub(r'\[\[(\d+)\]\]',lambda m:'[['+str(mp[int(m[1])])+']]',v)
 if isinstance(v,list):return [convert(z) for z in v]
 if isinstance(v,dict):return {k:convert(z) for k,z in v.items()}
 return v
pages=[]
for n in order:
 x=convert(P[n]);x['old_rev13_page']=n;x['n']=mp[n];pages.append(x)
__import__('final_program_audit').apply(pages)
pages[24]['goal']='60977 steuert Motor und Sound; AUX1 schaltet ausschließlich die Relaisspule. Nach allen Änderungen den vollständigen Projektstand übertragen.'
for b in pages[24]['blocks']:b['after']=min(b.get('after',7),5)
for b in pages[32]['blocks']:
 if b.get('label')=='2.':b['text']=b['text'].replace('Wieder anschließen und STOP aufheben.','Wieder anschließen, CS3 einschalten und STOP aufheben.')
# All source pointers cover the two-page source section.
OUT=PROJECT/'output/pdf/ICE_2976_Umbauanleitung_REV14_ORIGINALPLATINE_62762.pdf'
(ROOT/'pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
(ROOT/'sources.json').write_text(json.dumps(ss,ensure_ascii=False,indent=2))
layout=Layout(OUT,pages);layout.build();r=PdfReader(OUT)
report={'output':str(OUT),'pages':len(r.pages),'bookmarks':len(r.outline),'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'links':sum(len(x.get('/Annots',[])) for x in r.pages),'figures':layout.figures,'source_count':len(ss),'old_to_new':mp,'words_by_page':[len((x.extract_text() or '').split()) for x in r.pages]}
(ROOT/'build_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));(ROOT/'placements.json').write_text(json.dumps(layout.placements,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['figures','old_to_new','words_by_page']},ensure_ascii=False,indent=2))
