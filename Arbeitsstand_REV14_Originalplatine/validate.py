from pathlib import Path
import json,re,hashlib
import pdfplumber
from pypdf import PdfReader
R=Path(__file__).resolve().parent;P=R.parent
f=P/'output/pdf/ICE_2976_Umbauanleitung_REV14_ORIGINALPLATINE_62762.pdf'
r=PdfReader(f);pages=json.loads((R/'pages.json').read_text());placements=json.loads((R/'placements.json').read_text());build=json.loads((R/'build_report.json').read_text())
assert len(r.pages)==len(pages)==47
assert len(r.outline)==47
assert [x['n'] for x in pages]==list(range(1,48))
assert all(1<=int(n)<=47 for n in re.findall(r'\[\[(\d+)\]\]',json.dumps(pages)))
assert min(x['bottom'] for x in placements)>=61
missing=[]
for x in build['figures']:
 if x.get('path') and not Path(x['path']).is_file():missing.append(x['path'])
assert not missing
outside=[]
with pdfplumber.open(f) as pdf:
 for i,page in enumerate(pdf.pages,1):
  for w in page.extract_words():
   if w['x0']<-0.5 or w['x1']>page.width+.5 or w['top']<-.5 or w['bottom']>page.height+.5:outside.append([i,w['text'],w['x0'],w['x1']])
assert not outside,outside
src={s['id'] for s in json.loads((R/'sources.json').read_text())}
assert all(set(x.get('sources',[]))<=src for x in pages)
refs={r.pages[i].indirect_reference.idnum for i in range(len(r.pages))}
badlinks=[]
for i,page in enumerate(r.pages,1):
 for a in page.get('/Annots',[]):
  o=a.get_object();d=o.get('/Dest')
  if d and isinstance(d,list) and hasattr(d[0],'idnum') and d[0].idnum not in refs:badlinks.append(i)
assert not badlinks
old=P/'output/pdf/ICE_2976_Umbauanleitung_REV13_WERKSTATTFASSUNG.pdf'
assert hashlib.sha256(old.read_bytes()).hexdigest()=='6a4afec36193952fa0a7040fc230c9c37356e71968e5b3dcd6244347d4308bce'
report={'pdf':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'pages':47,'bookmarks':47,'links':build['links'],'figures':len(build['figures']),'photos':sum(bool(x.get('path')) for x in build['figures']),'vector_schematics':sum(bool(x.get('kind')) for x in build['figures']),'sources':len(src),'min_content_bottom_pt':min(x['bottom'] for x in placements),'outside_page_words':outside,'bad_internal_links':badlinks,'rev13_unchanged':True,'hardware_tests_performed':False}
(R/'final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
