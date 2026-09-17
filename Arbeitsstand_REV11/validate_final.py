from pathlib import Path
import json,hashlib,re
from pypdf import PdfReader
import pdfplumber
ROOT=Path(__file__).resolve().parent;P=ROOT.parent
pdf=P/'output/pdf/ICE_2976_Umbauanleitung_REV11_WERKSTATTFASSUNG.pdf'
r=PdfReader(pdf);br=json.loads((P/'tmp/pdfs/rev11/build_report.json').read_text())
assert len(r.pages)==40 and len(r.outline)==40
assert [r.get_destination_page_number(d) for d in r.outline]==list(range(40))
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
original=P/'ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf'
assert hashlib.sha256(original.read_bytes()).hexdigest()=='2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0'
qa={'pages':40,'bookmarks':40,'links':br['links'],'invalid_page_links':badlinks,'out_of_bounds_characters':badchars,'unresolved_placeholders':unresolved,'words':sum(br['words_by_page']),'figure_placements':br['figure_placements'],'photo_or_manufacturer_placements':sum(bool(x['path']) for x in br['figures']),'vector_diagram_placements':sum(bool(x['kind']) for x in br['figures']),'sources':br['source_count'],'bytes':pdf.stat().st_size,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'rev10_unchanged':True,'visual_review':{'root':[1,2,3,4,5,6,10,24,28],'visual_agent':list(range(12,24))+[30,31],'coverage_agent':list(range(24,30))+list(range(32,41)),'programming_agent':list(range(7,12))},'scope':'Document content/layout validation. No physical decoder programming or vehicle test performed.'}
(ROOT/'final_validation.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in qa.items() if k!='visual_review'},ensure_ascii=False,indent=2))
