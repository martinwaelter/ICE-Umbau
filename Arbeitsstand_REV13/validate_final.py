from pathlib import Path
import json,hashlib,re
from pypdf import PdfReader
import pdfplumber
R=Path(__file__).resolve().parent;P=R.parent
pdf=P/'output/pdf/ICE_2976_Umbauanleitung_REV13_WERKSTATTFASSUNG.pdf';r=PdfReader(pdf)
br=json.loads((P/'tmp/pdfs/rev13/build_report.json').read_text())
assert len(r.pages)==46 and len(r.outline)==46
assert [r.get_destination_page_number(d) for d in r.outline]==list(range(46))
refs={p.indirect_reference.idnum for p in r.pages};badlinks=[];badrect=[];internal=external=0
for n,p in enumerate(r.pages,1):
 for ref in p.get('/Annots',[]):
  a=ref.get_object();dest=a.get('/Dest')
  if dest:
   internal+=1
   if isinstance(dest,list) and hasattr(dest[0],'idnum') and dest[0].idnum not in refs:badlinks.append(n)
  if a.get('/A',{}).get('/S')=='/URI':external+=1
  q=a.get('/Rect')
  if q and (min(q[0],q[2])<0 or max(q[0],q[2])>float(p.mediabox.width)+.5 or min(q[1],q[3])<0 or max(q[1],q[3])>float(p.mediabox.height)+.5):badrect.append(n)
assert not badlinks and not badrect
badchars=[];unresolved=[]
with pdfplumber.open(pdf) as d:
 for n,p in enumerate(d.pages,1):
  for c in p.chars:
   if c['x0']<0 or c['x1']>p.width+.5 or c['top']<0 or c['bottom']>p.height+.5:badchars.append([n,c['text']])
  t=p.extract_text() or ''
  if re.search(r'\[\[\d+\]\]|TODO|TBD|\ufffd',t):unresolved.append(n)
assert not badchars and not unresolved,(badchars,unresolved)
old=json.loads((P/'tmp/pdfs/rev12/build_report.json').read_text())
assert {f['path'] for f in old['figures'] if f['path']} <= {f['path'] for f in br['figures'] if f['path']}
expected={'ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf':'2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0','output/pdf/ICE_2976_Umbauanleitung_REV11_WERKSTATTFASSUNG.pdf':'3c67f596856f5403eac6f27f1f2512379555d3611749e4a7bd94f817cc7e41cb','output/pdf/ICE_2976_Umbauanleitung_REV12_WERKSTATTFASSUNG.pdf':'95af61083373a0755fde8ebd5ae70233952f6283b3db652b03e71c26582bcc8e','/Users/martinwaelter/Märklin Gleisplan/ICE2976_REV12_Pruefbericht.md':'d4f913f4c6484c94f219e23c4c610e0d9d1c08679cb93b20dc6a570e9f79a380'}
for name,sha in expected.items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==sha,name
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==br['sha256']
text='\n'.join(p.extract_text() or '' for p in r.pages)
for stale in ['G0','Montage S. 30/1–5','Elektronik-Prüfplan','REV12 |']:assert stale not in text,stale
out={'pdf':str(pdf),'pages':46,'bookmarks':46,'links':br['links'],'internal_links':internal,'external_links':external,'invalid_internal_links':badlinks,'invalid_link_rectangles':badrect,'out_of_bounds_characters':badchars,'unresolved_technical_placeholders':unresolved,'photo_or_manufacturer_placements':sum(bool(f['path']) for f in br['figures']),'vector_diagram_placements':sum(bool(f['kind']) for f in br['figures']),'source_count':br['source_count'],'sha256':br['sha256'],'bytes':pdf.stat().st_size,'input_files_unchanged':True,'all_rev12_photo_sources_retained':True,'hardware_tests_performed':False}
(R/'final_validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps(out,ensure_ascii=False,indent=2))
