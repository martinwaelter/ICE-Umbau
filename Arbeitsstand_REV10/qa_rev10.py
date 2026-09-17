"""Structural/retention checks. Visual and technical reviews remain separate."""
from pathlib import Path
from collections import Counter
import hashlib,json,re
from pypdf import PdfReader
import pdfplumber
import rev10_document as edit
ROOT=Path(__file__).resolve().parent;PROJECT=ROOT.parent;TMP=PROJECT/'tmp/pdfs/rev10'
build=json.loads((TMP/'build_report.json').read_text())
new=PdfReader(build['output']);old=PdfReader(PROJECT/'ICE_2976_Umbauanleitung_REV9_MIT_SCHNELLANLEITUNG.pdf')
sections=json.loads((ROOT/'rev10_sections.json').read_text())
baseline=json.loads((ROOT/'rev9_sections.json').read_text())
def images(pdf):
    vals=[]
    for page in pdf.pages:
        for obj in page.get('/Resources',{}).get('/XObject',{}).values():
            obj=obj.get_object()
            if obj.get('/Subtype')=='/Image':vals.append(hashlib.sha256(obj.get_data()).hexdigest())
    return Counter(vals)
def prefix(t):
    m=re.match(r'^(?:[A-Z]\.\d+\.|\d+[a-z]?\.|[A-Z][0-9]?\.)',t)
    return m.group() if m else t
new_prefixes={prefix(s['title']) for s in sections}
lost_sections=[s['title'] for s in baseline if not s['title'].startswith(('ICE 2976','E.')) and prefix(s['title']) not in new_prefixes]
image_missing=dict(images(old)-images(new))
page_refs={p.indirect_reference.idnum:i for i,p in enumerate(new.pages)}
links=[];bad_links=[]
for i,page in enumerate(new.pages):
    for aref in page.get('/Annots',[]):
        a=aref.get_object();dest=a.get('/Dest')
        if dest is None and a.get('/A',{}).get('/S')=='/GoTo':dest=a['/A']['/D']
        if dest is not None:
            try:
                if isinstance(dest,str):target=new.get_destination_page_number(new.named_destinations[dest])
                else:target=page_refs[dest[0].idnum]
                assert 0<=target<len(new.pages)
                links.append({'page':i+1,'target':target+1,'rect':list(a['/Rect'])})
            except Exception as exc:bad_links.append({'page':i+1,'dest':str(dest),'error':str(exc)})
bounds=[];sparse=[];page_text=[];link_text_checks=[];bad_link_text=[]
titles_by_page={v:k for k,v in build['section_pages'].items()}
def norm(t):return ''.join(ch.lower() for ch in t if ch.isalnum())
with pdfplumber.open(build['output']) as pdf:
    for i,page in enumerate(pdf.pages):
        chars=page.chars
        outside=[ch for ch in chars if ch['x0'] < 35 or ch['x1']>page.width-35 or ch['top']<15 or ch['bottom']>page.height-15]
        if outside:bounds.append({'page':i+1,'chars':''.join(ch['text'] for ch in outside)[:160]})
        text=page.extract_text() or '';page_text.append(text)
        if len(text)<180:sparse.append({'page':i+1,'text':text})
    for link in links:
        page=pdf.pages[link['page']-1];x0,y0,x1,y1=map(float,link['rect'])
        # Annotation bounds can differ slightly from text ascenders; centers
        # avoid collecting text from the neighboring line or the TOC dot leader.
        top,bottom=page.height-y1,page.height-y0
        cs=[ch for ch in page.chars if x0-.5<=(ch['x0']+ch['x1'])/2<=x1+.5 and top-1<=(ch['top']+ch['bottom'])/2<=bottom+1]
        visible=''.join(ch['text'] for ch in cs)
        title=titles_by_page.get(link['target'],'')
        ok=bool(norm(visible)) and (norm(visible) in norm(title) or norm(visible)==str(link['target']))
        record={'page':link['page'],'target':link['target'],'visible_text':visible,'target_title':title,'matches':ok}
        link_text_checks.append(record)
        if not ok:bad_link_text.append(record)
full='\n\f\n'.join(page_text)
(TMP/'REV10_text.txt').write_text(full)
forbidden=['Schwarz bleibt ausschließlich','Die Widerstandstoleranz muss','Dummy spannungsfrei abkoppeln','Die vollständige externe Findingtabelle liegt noch nicht vor','schließt die Registerlücke','Diese REV10 beruht auf der vollständigen REV10','Falls Prüfenden nach außen','Vier Hilfsprüfenden']
stale=[t for t in forbidden if t in full]
assert not image_missing,('Lost original images',image_missing)
assert not lost_sections,('Lost old section',lost_sections)
assert not bad_links,('Broken links',bad_links)
assert not bounds,('Text bounds',bounds)
assert not stale,('Stale wording',stale)
assert not bad_link_text,('Link text does not match target title/page',bad_link_text)
assert '16c.' in full and '16d.' in full and '12d.' in full and 'E1.' in full and 'E2.' in full and 'E3.' in full
assert page_text[-1].find('Schnellanleitung')>=0 or 'Betriebsgrenzen' in page_text[-1]
assert hashlib.sha256((PROJECT/'ICE_2976_Umbauanleitung_REV9_MIT_SCHNELLANLEITUNG.pdf').read_bytes()).hexdigest()==build['original_sha256']
check={'automated_result':'PASS','pages':len(new.pages),'sections':len(sections),'internal_links':len(links),'internal_link_text_checks':len(link_text_checks),'mismatching_link_texts':bad_link_text,'old_image_instances':sum(images(old).values()),'new_image_instances':sum(images(new).values()),'missing_images':image_missing,'missing_section_families':lost_sections,'broken_links':bad_links,'out_of_bounds':bounds,'sparse_pages_to_review':sparse,'source_unchanged':True,'hardware_tests':False,'visual_review_separate':True,'sha256':build['sha256']}
(TMP/'qa_report.json').write_text(json.dumps(check,ensure_ascii=False,indent=2))
(TMP/'links.json').write_text(json.dumps(links,indent=2))
(TMP/'link_text_checks.json').write_text(json.dumps(link_text_checks,ensure_ascii=False,indent=2))
print(json.dumps(check,ensure_ascii=False,indent=2))
