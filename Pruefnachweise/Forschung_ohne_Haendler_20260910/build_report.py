from pathlib import Path
import re, json, hashlib, html
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader

BASE = Path(__file__).parent
OUT = BASE.parent.parent / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
STEM = 'ICE_2976_Forensische_Recherche_OHNE_HAENDLER'
MD = OUT / (STEM + '.md')
PDF = OUT / (STEM + '.pdf')
FONT = Path('/System/Library/Fonts/Supplemental')
for name, filename in [('Arial','Arial.ttf'),('Arial-Bold','Arial Bold.ttf'),('Arial-Italic','Arial Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT/filename)))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial-Italic',boldItalic='Arial-Bold')
S = {
 'p': ParagraphStyle('body',fontName='Arial',fontSize=10.1,leading=14,spaceAfter=8,textColor=colors.HexColor('#202020')),
 'title': ParagraphStyle('title',fontName='Arial-Bold',fontSize=22,leading=27,spaceAfter=17),
 'h1': ParagraphStyle('h1',fontName='Arial-Bold',fontSize=16.2,leading=20,spaceAfter=13),
 'h2': ParagraphStyle('h2',fontName='Arial-Bold',fontSize=11.4,leading=15,spaceBefore=7,spaceAfter=7),
 'cell': ParagraphStyle('cell',fontName='Arial',fontSize=9.1,leading=12,spaceAfter=0),
 'foot': ParagraphStyle('foot',fontName='Arial',fontSize=8,leading=10.6,spaceAfter=3,textColor=colors.HexColor('#555555')),
 'source': ParagraphStyle('source',fontName='Arial',fontSize=9.0,leading=12,spaceAfter=9),
}

def inline(raw):
    raw=html.escape(raw)
    raw=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',raw)
    raw=re.sub(r'`([^`]+)`',r'<font name="Arial">\1</font>',raw)
    def refs(match):
        parts=[]
        for num in re.findall(r'\d+',match.group()):
            url=SOURCES[int(num)]['url']
            parts.append('<link href="'+html.escape(url,quote=True)+'">'+num+'</link>' if url else num)
        return '<super>'+', '.join(parts)+'</super>'
    raw=re.sub(r'(?:\[\^\d+\])+',refs,raw)
    raw=re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',r'<link href="\2" color="#303030"><u>\1</u></link>',raw)
    return raw

def footer(c,doc):
    c.setFont('Arial',8)
    c.setFillColor(colors.HexColor('#666666'))
    c.drawRightString(A4[0]-45,26,str(doc.page))

def section_flow(raw):
    lines=raw.strip().splitlines(); flow=[]; i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line: i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[v.strip() for v in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[: -]+',v) for v in cells):rows.append(cells)
                i+=1
            n=len(rows[0]);width=A4[0]-90
            ratios={2:[.30,.70],3:[.24,.37,.39],4:[.12,.30,.24,.34]}.get(n,[1/n]*n)
            data=[[Paragraph(inline(('**'+v+'**') if ri==0 else v),S['cell']) for v in row] for ri,row in enumerate(rows)]
            t=Table(data,colWidths=[width*v for v in ratios],hAlign='LEFT',repeatRows=1)
            t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#555555')),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#cccccc')),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            flow.extend([t,Spacer(1,10)]);continue
        if line.startswith('# '):flow.append(Paragraph(inline(line[2:]),S['title']));i+=1;continue
        if line.startswith('## '):flow.append(Paragraph(inline(line[3:]),S['h1']));i+=1;continue
        if line.startswith('### '):flow.append(Paragraph(inline(line[4:]),S['h2']));i+=1;continue
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|')):
            para.append(lines[i].strip());i+=1
        flow.append(Paragraph(inline(' '.join(para)),S['p']))
    refs=sorted(set(map(int,re.findall(r'\[\^(\d+)\]',raw))))
    if refs:
        flow.append(Spacer(1,7))
        for n in refs:
            s=SOURCES[n]
            label=html.escape(s['short'])
            if s['url']:label=f'<link href="{html.escape(s["url"],quote=True)}">{label}</link>'
            flow.append(Paragraph(f'{n}. {label}',S['foot']))
    return flow

def build():
    global SOURCES
    data=json.loads((BASE/'report_content.json').read_text())
    SOURCES={int(k):v for k,v in data['sources'].items()}
    sections=data['sections'];story=[]
    for i,section in enumerate(sections):
        if i:story.append(PageBreak())
        story.extend(section_flow(section))
    for start in [1,16]:
        story.append(PageBreak())
        story.append(Paragraph('Quellen' if start==1 else 'Quellen und Nachweisstand',S['h1']))
        for n in range(start,min(start+15,len(SOURCES)+1)):
            s=SOURCES[n]
            link=f'<link href="{html.escape(s["url"],quote=True)}"><u>Originalquelle</u></link>.' if s['url'] else 'Lokale Quelldatei.'
            story.append(Paragraph(f'<b>{n}.</b> {html.escape(s["full"])} {link}',S['source']))
        if start==16:
            story.append(Paragraph('Nachweisstand',S['h2']))
            story.append(Paragraph(inline(data['provenance']),S['source']))
    doc=SimpleDocTemplate(str(PDF),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=42,bottomMargin=46,title='ICE 2976: Umbau ohne Händler',author='',subject='Forensische Recherche zu REV10, Master-Slave-Synchronisation, CS3 und eigenständigen Prüfungen')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    md='\n\n'.join(sections)+'\n\n## Quellen\n\n'
    for n,s in SOURCES.items():md+=f'{n}. {s["full"]} '+(f'[Originalquelle]({s["url"]}).' if s['url'] else 'Lokale Quelldatei.')+'\n\n'
    md+='## Nachweisstand\n\n'+data['provenance']+'\n\n'
    for n,s in SOURCES.items():md+=f'[^'+str(n)+']: '+s['full']+(' [Originalquelle]('+s['url']+').' if s['url'] else ' Lokale Quelldatei.')+'\n'
    MD.write_text(md)
    r=PdfReader(PDF)
    qa={'pages':len(r.pages),'page_words':[len((p.extract_text() or '').split()) for p in r.pages],'links':sum(len(p.get('/Annots',[])) for p in r.pages),'sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),'pdf':str(PDF),'markdown':str(MD)}
    (BASE/'report_qa.json').write_text(json.dumps(qa,indent=2))
    print(json.dumps(qa,indent=2))

if __name__=='__main__':build()
