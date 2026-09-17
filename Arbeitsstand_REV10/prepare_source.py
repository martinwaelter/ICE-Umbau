"""Recover the full REV9 flowables locally; never execute an archived PDF export."""
from pathlib import Path
import hashlib, json, shutil, sys

HERE=Path(__file__).resolve().parent
ARCH=Path('/Users/martinwaelter/Library/CloudStorage/OneDrive-Persönlich/Documents/ChatGPT/ICE Umbau')
OLD=ARCH/'Archiv/2026-09-10_ICE2976/Arbeitsstand'
LEGACY=HERE/'quellen_alt'; LEGACY.mkdir(exist_ok=True)
ASSETS=HERE/'bilder'; ASSETS.mkdir(exist_ok=True)
names=['build_ice2976_rev5.py','build_ice2976_rev6.py','build_ice2976_rev6_final.py','build_ice2976_rev6_release.py','build_ice2976_rev6_closure.py','build_ice2976_rev7.py','build_ice2976_rev8.py','build_ice2976_rev9.py','build_ice2976_cv_cs3_research.py','rev7_content.py','rev7_additions.py','rev7_polish.py','rev7_verified.py','rev7_closed.py','rev8_cv_integration.py','rev9_concrete_closure.py']
mapping={}
for src in (ARCH/'Archiv/2026-09-10_ICE2976/Externe_Bildquellen').rglob('*'):
    if src.is_file() and src.suffix.lower() in ('.jpg','.png','.jpeg'):
        rel=src.relative_to(ARCH/'Archiv/2026-09-10_ICE2976/Externe_Bildquellen')
        dst=ASSETS/src.name
        shutil.copy2(src,dst); mapping['/'+str(rel)]=str(dst)
for src in (OLD/'tmp/pdfs/rev5/research').iterdir():
    if src.is_file():
        dst=LEGACY/'tmp/pdfs/rev5/research'/src.name
        dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst)
for name in names:
    text=(OLD/name).read_text()
    for a,b in mapping.items(): text=text.replace(a,b)
    (LEGACY/name).write_text(text)
prev='output/pdf/ICE_2976_Umbauanleitung_REV6_PRUEFFASSUNG.pdf'
(LEGACY/prev).parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(OLD/prev,LEGACY/prev)
sys.path.insert(0,str(LEGACY))
builder=LEGACY/'build_ice2976_rev7.py'
ctx={'__file__':str(builder)}
exec(compile(builder.read_text().split("scope = {'__file__':",1)[0],str(builder),'exec'),ctx)
code=ctx['source'].replace('from rev7_content import install','from rev9_concrete_closure import install').replace('REV7','REV9')
code=code.split('doc=ManualDoc(str(OUT)',1)[0]
ns={'__file__':str(LEGACY/'build_ice2976_rev6.py'),'__name__':'capture'}
exec(compile(code,str(builder),'exec'),ns)

from reportlab.platypus import Paragraph,Table,KeepTogether,Spacer,PageBreak,Image
def export(f):
    typ=type(f).__name__
    if isinstance(f,Paragraph):return {'type':'p','style':f.style.name,'text':f.text}
    if isinstance(f,PageBreak):return {'type':'break'}
    if isinstance(f,Spacer):return {'type':'space','h':f.height}
    if isinstance(f,KeepTogether):return {'type':'keep','items':[export(x) for x in f._content]}
    if isinstance(f,Table):return {'type':'table','widths':f._argW,'rows':[[export(x) if not isinstance(x,list) else {'type':'keep','items':[export(y) for y in x]} for x in row] for row in f._cellvalues]}
    if isinstance(f,Image):return {'type':'image','path':f.filename,'w':f.drawWidth,'h':f.drawHeight}
    if typ in ('MarkedPhoto','SourceDiagram','Sketch','InsertDiagram','ClipDiagram'):
        return {'type':typ,**{k:v for k,v in f.__dict__.items() if not k.startswith('_') and k not in ('canv',)}}
    raise TypeError((typ,f.__dict__))
data=[export(f) for f in ns['story']]
(HERE/'rev9_base.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
# Preserve source-defined vector figures in their original drawing implementation.
(HERE/'figure_namespace.py').write_text((LEGACY/'build_ice2976_rev5.py').read_text().split("page('ICE 2976: Umbauanleitung REV5')",1)[0])
(HERE/'captured_source.py').write_text(code)
(HERE/'source_manifest.json').write_text(json.dumps({'original_scripts':{n:hashlib.sha256((OLD/n).read_bytes()).hexdigest() for n in names},'elements':len(data),'image_mapping':mapping},indent=2,ensure_ascii=False))
print('Recovered base elements:',len(data)); print('Types:',sorted(set(d['type'] for d in data)))

# Capture the complete reviewed CV appendix as structured flowables, not page images.
rev9=(LEGACY/'build_ice2976_rev9.py').read_text()
block=rev9.split('# Reuse the full, reviewed REV8 appendix transformations, not an older research draft.',1)[1].split("exec(compile(code,str(ROOT/'build_ice2976_cv_cs3_research.py')",1)[0]
context={'ROOT':LEGACY}; exec(block,context)
acode=context['code']; an={'__file__':str(LEGACY/'build_ice2976_cv_cs3_research.py')}
exec(acode.split('class Report:',1)[0],an)
app=[]
class CaptureReport:
    def __init__(self):self.refs=[]
    def start(self,title,main=False):
        if app:self.end();app.append({'type':'break'})
        app.append({'type':'p','style':'h1','text':title});self.refs=[]
    def p(self,text,style=None,after=None):app.append({'type':'p','style':getattr(style,'name','body'),'text':text})
    def sub(self,text):app.append({'type':'p','style':'h2','text':text})
    def table(self,rows,widths):app.append({'type':'table','widths':[ns['W']*x for x in widths],'rows':[[{'type':'p','style':'head' if i==0 else 'cell','text':str(t)} for t in row] for i,row in enumerate(rows)]})
    def flow(self,boxes):self.table([boxes],[1/len(boxes)]*len(boxes))
    def ref(self,*nums):
        for n in nums:
            if n not in self.refs:self.refs.append(n)
        return '<super>'+','.join(f'<a href="{an["SOURCES"][n][3]}">F-{n}</a>' for n in nums)+'</super>'
    def end(self):
        for n in self.refs:
            pub,title,detail,url=an['SOURCES'][n]
            self.p(f'F-{n}. {pub}: <a href="{url}">{title}</a>.',an['SMALL'])
    def save(self):self.end()
an['Report']=CaptureReport
exec('r=Report()'+acode.split('r=Report()',1)[1].split('r.save()',1)[0]+'r.save()',an)
(HERE/'rev9_appendix.json').write_text(json.dumps(app,ensure_ascii=False,indent=2))

def texts(items):
    for el in items:
        if el['type']=='p':yield el['text']
        if 'items' in el:yield from texts(el['items'])
        for row in el.get('rows',[]):yield from texts(row)
sections=[]
for el in data+app:
    if el['type']=='p' and el['style']=='h1':sections.append({'title':el['text'],'elements':[]})
    elif el['type']!='break':sections[-1]['elements'].append(el)
(HERE/'rev9_sections.json').write_text(json.dumps(sections,ensure_ascii=False,indent=2))
(HERE/'rev9_source_readable.txt').write_text('\n\n'.join('### '+s['title']+'\n'+'\n'.join(texts(s['elements'])) for s in sections))
print('Sections:',len(sections),'Appendix elements:',len(app))
