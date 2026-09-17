from pathlib import Path
import json,hashlib,re
from pypdf import PdfReader
import pdfplumber
ROOT=Path(__file__).resolve().parent;P=ROOT.parent
pdf=P/'output/pdf/ICE_2976_Umbauanleitung_REV12_WERKSTATTFASSUNG.pdf'
r=PdfReader(pdf);br=json.loads((P/'tmp/pdfs/rev12/build_report.json').read_text())
assert len(r.pages)==44 and len(r.outline)==44
assert [r.get_destination_page_number(d) for d in r.outline]==list(range(44))
refs={p.indirect_reference.idnum for p in r.pages};badlinks=[]
for n,p in enumerate(r.pages,1):
 for ref in p.get('/Annots',[]):
  a=ref.get_object();dest=a.get('/Dest')
  if dest and isinstance(dest,list) and hasattr(dest[0],'idnum') and dest[0].idnum not in refs:badlinks.append(n)
assert not badlinks
badchars=[];unresolved=[]
with pdfplumber.open(pdf) as doc:
 for n,p in enumerate(doc.pages,1):
  for c in p.chars:
   if c['x0']<0 or c['x1']>p.width+.5 or c['top']<0 or c['bottom']>p.height+.5:badchars.append([n,c['text']])
  t=p.extract_text() or ''
  if re.search(r'\[\[\d+\]\]|TODO|TBD|\ufffd',t):unresolved.append(n)
assert not badchars and not unresolved
previous=P/'output/pdf/ICE_2976_Umbauanleitung_REV11_WERKSTATTFASSUNG.pdf'
assert hashlib.sha256(previous.read_bytes()).hexdigest()=='3c67f596856f5403eac6f27f1f2512379555d3611749e4a7bd94f817cc7e41cb'
oldfig=json.loads((P/'tmp/pdfs/rev11/build_report.json').read_text())['figures']
oldpaths={x['path'] for x in oldfig if x['path']}
newpaths={x['path'] for x in br['figures'] if x['path']}
assert oldpaths <= newpaths, oldpaths-newpaths
for path in newpaths: assert Path(path).is_file(),path
assert br['sha256']==hashlib.sha256(pdf.read_bytes()).hexdigest()
text_all='\n'.join(x.extract_text() or '' for x in r.pages)
for stale in ['Elektronik-Prüfplan','τ ≤','REV11 |']: assert stale not in text_all,stale

original=P/'ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf'
assert hashlib.sha256(original.read_bytes()).hexdigest()=='2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0'
qa={'pages':44,'bookmarks':44,'links':br['links'],'invalid_page_links':badlinks,'out_of_bounds_characters':badchars,'unresolved_placeholders':unresolved,'words':sum(br['words_by_page']),'figure_placements':br['figure_placements'],'photo_or_manufacturer_placements':sum(bool(x['path']) for x in br['figures']),'vector_diagram_placements':sum(bool(x['kind']) for x in br['figures']),'sources':br['source_count'],'bytes':pdf.stat().st_size,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'rev10_unchanged':True,'rev11_unchanged':True,'all_rev11_photo_sources_retained':True,'visual_review':{'root':[1,2,3,4],'electrical_agent':[3,5,18,19,30,31,32,35,36,40,41],'coverage_agent':list(range(13,18))+list(range(20,30))+list(range(37,40))+[42,43,44],'programming_agent':list(range(6,13))+[32,36,41]},'scope':'Document content/layout validation. No physical decoder programming or vehicle test performed.'}
(ROOT/'final_validation.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in qa.items() if k!='visual_review'},ensure_ascii=False,indent=2))
