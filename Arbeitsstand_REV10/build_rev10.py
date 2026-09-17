"""Reproducible complete local REV10. Preserve illustrations and all old section families."""
from pathlib import Path
from copy import deepcopy
import hashlib,importlib.util,json,re,sys,unicodedata
from html import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,Image,Flowable,KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader
from PIL import Image as PILImage
import rev10_document as docedit

ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parent
OUT=PROJECT/'output/pdf/ICE_2976_Umbauanleitung_REV10_MIT_SCHNELLANLEITUNG.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
TMP=PROJECT/'tmp/pdfs/rev10';TMP.mkdir(parents=True,exist_ok=True)
SOURCE=PROJECT/'ICE_2976_Umbauanleitung_REV9_MIT_SCHNELLANLEITUNG.pdf'
ORIGINAL=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
assert ORIGINAL=='c1c1b1a2772f0e25385ffe911041b1cd2f7351277ada2ed5d8ecbe1be0070d29'
for name,file in [('A','Arial.ttf'),('AB','Arial Bold.ttf'),('AI','Arial Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/System/Library/Fonts/Supplemental/'+file))
pdfmetrics.registerFontFamily('A',normal='A',bold='AB',italic='AI',boldItalic='AB')
W,H=A4; WIDTH=W-84
INK=colors.HexColor('#202B31');MUTED=colors.HexColor('#52616B');TEAL=colors.HexColor('#173D47');RED=colors.HexColor('#9D2024')
styles={
 'body':ParagraphStyle('body',fontName='A',fontSize=9.8,leading=13.5,textColor=INK,spaceAfter=6),
 'small':ParagraphStyle('small',fontName='A',fontSize=8.3,leading=11.2,textColor=MUTED,spaceAfter=4),
 'h1':ParagraphStyle('h1',fontName='AB',fontSize=18,leading=22,textColor=TEAL,spaceAfter=12,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='AB',fontSize=11.5,leading=14.8,textColor=TEAL,spaceBefore=7,spaceAfter=6,keepWithNext=True),
 'cell':ParagraphStyle('cell',fontName='A',fontSize=8.7,leading=11.6,textColor=INK),
 'head':ParagraphStyle('head',fontName='AB',fontSize=8.7,leading=11.6,textColor=INK),
 'warn':ParagraphStyle('warn',fontName='A',fontSize=9.3,leading=12.8,textColor=RED),
 'step':ParagraphStyle('step',fontName='A',fontSize=9.8,leading=13.5,textColor=INK,leftIndent=18,firstLineIndent=-18,spaceAfter=7),
}
spec=importlib.util.spec_from_file_location('original_figures',ROOT/'figure_namespace.py')
fig=importlib.util.module_from_spec(spec);spec.loader.exec_module(fig)
baseline=json.loads((ROOT/'rev9_sections.json').read_text())
sections=docedit.apply(deepcopy(baseline))
coverage=dict(docedit.COVERED)
for name in ('rev10_hardware','rev10_programming'):
    mod=__import__(name); result=mod.apply(sections)
    if result is not None:sections=result
    if hasattr(mod,'COVERED'):
        if isinstance(mod.COVERED,dict):coverage.update(mod.COVERED)
        else:
            for k in mod.COVERED:coverage[k]='Übernommen; reale Nachweise gemäß Fachkapitel offen.'
docedit.add_quickguide(sections)
# Safety boxes precede the relevant handgrips, not an isolated source tail.
for prefix,marker in (
    ('9c. ','Am eigenen 21MTC-Feld'),
    ('12b. ','Die Decoder nicht zwischen'),
    ('17. ','Auf deinem kurzen Prüfgleis'),
):
    chosen=next(s for s in sections if s['title'].startswith(prefix))
    matches=[e for e in chosen['elements'] if e['type']=='keep' and any(marker in p['text'] for p in docedit.walk([e]))]
    assert len(matches)==1,(prefix,marker)
    warning=matches[0];chosen['elements'].remove(warning)
    for p in docedit.walk([warning]):
        p['text']=p['text'].replace('die oben beschriebene Steckkontrolle','die nachfolgende Steckkontrolle')
    chosen['elements'].insert(1,warning)
    if prefix=='17. ':
        start=next(i for i,e in enumerate(chosen['elements']) if e.get('text','').startswith('<b>54.'))
        chosen['elements'].insert(start,{'type':'break'})
# Revision names refer to this document; historical version references in H are preserved.
for s in sections:
    s['title']=s['title'].replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
    if not s['title'].startswith('H.'):
        for e in docedit.walk(s['elements']):
            e['text']=e['text'].replace('REV9','REV10')
    for e in docedit.walk(s['elements']):
        e['text']=e['text'].replace('Diese REV10 beruht auf der vollständigen REV10','Diese REV10 beruht auf der vollständigen REV9')
        e['text']=e['text'].replace('Falls Prüfenden nach außen','Falls Prüfleitungsenden nach außen').replace('Vier Hilfsprüfenden','Vier Hilfsprüfleitungsenden')
        e['text']=e['text'].replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
keys={s['title']:'sec-'+str(i) for i,s in enumerate(sections)}
def linktext(t):
    def resolve(m):
        prefix=m.group(1)
        matches=[s for s in sections if s['title'].startswith(prefix+' ') or s['title']==prefix]
        assert len(matches)==1,('Link target',prefix,len(matches))
        target=matches[0]['title']
        return f'<link href="#{keys[target]}" color="#285E72">{escape(target)}</link>'
    return re.sub(r'\[\[(.*?)\]\]',resolve,t)

class SourceView(Flowable):
    """Viewport over the unchanged source bitmap, including all relevant warning graphics."""
    def __init__(self,kind,path=None):
        super().__init__();self.kind=kind
        if kind=='ClipDiagram':
            self.path=str(ROOT/'bilder/ice2976_stecken-006.png');self.crop=(.04,.055,.47,.925);self.width=330;self.height=400
        else:
            self.path=path;self.crop=(.045,.225,.49,.77);self.width=320;self.height=260
    def draw(self):
        with PILImage.open(self.path) as im:iw,ih=im.size
        l,t,r,b=self.crop;s=min(self.width/((r-l)*iw),self.height/((b-t)*ih))
        c=self.canv;c.saveState();q=c.beginPath();q.rect(0,0,(r-l)*iw*s,(b-t)*ih*s);c.clipPath(q,stroke=0)
        c.drawImage(self.path,-l*iw*s,-(1-b)*ih*s,width=iw*s,height=ih*s);c.restoreState()

COMPACT_PREFIXES=('B. ','8. ','9. ','9a. ','12. ','16. ')
compact_styles={k:ParagraphStyle('compact-'+k,parent=v,spaceAfter=min(v.spaceAfter,4),leading=v.leading-.3) for k,v in styles.items()}
compact_styles['small']=ParagraphStyle('compact-small',parent=styles['small'],spaceAfter=2,leading=10.8)

def flow(e,compact=False):
    typ=e['type']
    chosen=compact_styles if compact else styles
    if typ=='p':return Paragraph(linktext(e['text']),chosen.get(e['style'],chosen['body']))
    if typ=='space':return Spacer(1,e['h']*.65 if compact else e['h'])
    if typ=='break':return PageBreak()
    if typ=='keep':return KeepTogether([flow(x,compact) for x in e['items']])
    if typ=='table':
        ws=e.get('widths') or [1]*len(e['rows'][0]);ws=[WIDTH*x/sum(ws) for x in ws]
        rows=[[[flow(y,compact) for y in x['items']] if x['type']=='keep' else flow(x,compact) for x in row] for row in e['rows']]
        warning=e.get('warning') or (len(ws)==1 and any(x.get('style')=='warn' for row in e['rows'] for x in row))
        tab=Table(rows,colWidths=ws,repeatRows=0 if warning else 1,hAlign='LEFT')
        rules=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]
        if compact:rules += [('TOPPADDING',(0,0),(-1,-1),4.5),('BOTTOMPADDING',(0,0),(-1,-1),4.5)]
        if warning:rules += [('BOX',(0,0),(-1,-1),.8,RED),('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#FFF5F1'))]
        else:rules += [('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E7EEF0')),('LINEBELOW',(0,0),(-1,0),.65,MUTED),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#CED6DA'))]
        tab.setStyle(TableStyle(rules));return tab
    if typ=='image':return Image(e['path'],width=e['w'],height=e['h'])
    if typ=='MarkedPhoto':return fig.MarkedPhoto(e['path'],e['width'],e['marks'],e['height'])
    if typ=='Sketch':return fig.Sketch(e['kind'],e['plotheight'])
    if typ in ('SourceDiagram','ClipDiagram'):return SourceView(typ,e.get('path'))
    raise ValueError(e)

class Manual(SimpleDocTemplate):
    def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.section_pages={};self.current=''
    def beforeDocument(self):self.section_pages={};self.current=''
    def afterFlowable(self,f):
        if hasattr(f,'section_key'):
            self.current=f.getPlainText();self.section_pages[self.current]=self.page
            self.canv.bookmarkPage(f.section_key)
            self.canv.addOutlineEntry(self.current,f.section_key,0,False)
            self.notify('TOCEntry',(0,self.current,self.page,f.section_key))
    def afterPage(self):
        c=self.canv;c.saveState();c.setStrokeColor(colors.HexColor('#CED6DA'));c.line(42,37,W-42,37)
        c.setFillColor(MUTED);c.setFont('A',7.6)
        if self.current and not self.current.startswith('ICE 2976') and self.section_pages.get(self.current)!=self.page:
            header='Fortsetzung: '+self.current
            while pdfmetrics.stringWidth(header,'A',7.6)>WIDTH:header=header[:-2]+'…'
            c.drawString(42,H-23,header)
        c.drawString(42,24,'REV10 | ICE 2976 | Arbeitsfassung - reale Freigaben beachten')
        c.drawRightString(W-42,24,str(self.page));c.restoreState()

story=[]
toc=TableOfContents()
toc.levelStyles=[ParagraphStyle('tocentry',fontName='A',fontSize=9.2,leading=12.7,textColor=INK,spaceBefore=3,leftIndent=0,firstLineIndent=0)]
for i,s in enumerate(sections):
    if i:story.append(PageBreak())
    title=Paragraph(s['title'],styles['h1']);title.section_key=keys[s['title']];story.append(title)
    for e in s['elements']:story.append(flow(e,s['title'].startswith(COMPACT_PREFIXES)))
    if i==0:
        story += [PageBreak(),Paragraph('Orientierung - alle Kapitel sind anklickbar',styles['h1']),Paragraph('Die Reihenfolge der Freigaben steht auf der Titelseite. Die Kapitelnummer dient dem Nachschlagen. Die Schnellanleitung G.1-G.3 steht am Ende; offene Nachweise und Versionsstatus in H.',styles['small']),toc]
doc=Manual(str(OUT),pagesize=A4,leftMargin=36,rightMargin=36,topMargin=34,bottomMargin=47,title='ICE 2976 - vollständige Umbauanleitung REV10 mit Schnellanleitung',author='',subject='Überarbeitete Prüffassung: konkrete Handgriffe, offene Nachweise, CS3-CV-Programmierung')
doc.multiBuild(story)
reader=PdfReader(OUT)
assert len(reader.pages)>=69,('Unexpected abridgement',len(reader.pages))
assert len(reader.outline)==len(sections)
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==ORIGINAL
(ROOT/'rev10_sections.json').write_text(json.dumps(sections,ensure_ascii=False,indent=2))
def txt(items):return '\n'.join(e['text'] for e in docedit.walk(items))
(ROOT/'REV10_LES EFASSUNG.txt'.replace(' ','' )).write_text('\n\n'.join('### '+s['title']+'\n'+txt(s['elements']) for s in sections))
report={'output':str(OUT),'pages':len(reader.pages),'sections':len(sections),'section_pages':doc.section_pages,'coverage':coverage,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'original_sha256':ORIGINAL}
(TMP/'build_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ('section_pages','coverage')},indent=2,ensure_ascii=False))
