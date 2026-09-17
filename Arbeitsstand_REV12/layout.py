from pathlib import Path
import json, re, hashlib
from html import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle, Flowable
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from PIL import Image

ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parent
W,H=A4
M=38
CW=W-2*M
INK=colors.HexColor('#182D38'); TEAL=colors.HexColor('#145B64'); GREY=colors.HexColor('#52626B'); LINE=colors.HexColor('#C8D5D9'); RED=colors.HexColor('#9D2923')
for name,f in [('Body','Arial.ttf'),('Bold','Arial Bold.ttf'),('Italic','Arial Italic.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/System/Library/Fonts/Supplemental/'+f))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
ST={
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.3,leading=14.0,textColor=INK),
 'small':ParagraphStyle('small',fontName='Body',fontSize=8.5,leading=11.0,textColor=GREY),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=9.3,leading=12.3,textColor=INK),
 'head':ParagraphStyle('head',fontName='Bold',fontSize=9.3,leading=12.3,textColor=INK),
 'h':ParagraphStyle('h',fontName='Bold',fontSize=11.2,leading=14.0,textColor=TEAL),
 'warn':ParagraphStyle('warn',fontName='Body',fontSize=9.7,leading=13.0,textColor=RED),
}
def norm(t):
 for x in ['\u2011','\u2013','\u2014']:t=t.replace(x,'-')
 t=t.replace('→',' -&gt; ')
 return t

def para(t,style='body'):
 t=norm(t)
 t=re.sub(r'\[\[(\d+)\]\]',lambda m:f'<link href="#p{m[1]}" color="#145B64">S. {m[1]}</link>',t)
 return Paragraph(t,ST[style])

class Photo(Flowable):
 def __init__(self,path,width,maxh=220,crop=None,marks=None):
  super().__init__();self.path=str(path);self.crop=crop or [0,0,1,1];self.marks=marks or []
  with Image.open(self.path) as im:self.iw,self.ih=im.size
  l,t,r,b=self.crop;ratio=(r-l)*self.iw/((b-t)*self.ih)
  self.width=min(width,maxh*ratio);self.height=self.width/ratio
 def draw(self):
  c=self.canv;l,t,r,b=self.crop;s=self.width/((r-l)*self.iw)
  c.saveState();p=c.beginPath();p.rect(0,0,self.width,self.height);c.clipPath(p,stroke=0)
  c.drawImage(self.path,-l*self.iw*s,-(1-b)*self.ih*s,width=self.iw*s,height=self.ih*s)
  c.restoreState()
  for number,px,py,lx,ly in self.marks:
   x=(px-l)/(r-l)*self.width;y=(b-py)/(b-t)*self.height
   a=(lx-l)/(r-l)*self.width;bb=(b-ly)/(b-t)*self.height
   c.setStrokeColor(colors.white);c.setLineWidth(3.5);c.line(a,bb,x,y)
   c.setStrokeColor(RED);c.setLineWidth(1.0);c.line(a,bb,x,y)
   c.setFillColor(colors.white);c.circle(x,y,2.7,stroke=1,fill=1);c.circle(a,bb,8,stroke=1,fill=1)
   c.setFillColor(RED);c.setFont('Bold',9);c.drawCentredString(a,bb-3,str(number))

class Layout:
 def __init__(self,out,pages):
  self.c=canvas.Canvas(str(out),pagesize=A4,pageCompression=1)
  self.c.setTitle('ICE 2976 - REV12 | Bebilderte Werkstattanleitung ohne Händler')
  self.c.setAuthor('');self.c.setSubject('Überarbeitete Originalanleitung mit Arbeitskarten, Anschlussbildern und Prüfungen')
  self.pages=pages;self.placements=[];self.figures=[]
 def blockheight(self,b,w):
  return self.make(b,w)[1]
 def make(self,b,w):
  kind=b['type']
  if kind in ['p','h','small']:
   q=para(b['text'],'body' if kind=='p' else kind);_,h=q.wrap(w,1000);return q,h
  if kind=='step':
   q=para('<b>'+escape(b['label'])+'</b> '+b['text']);_,h=q.wrap(w,1000);return q,h
  if kind=='note':
   q=para('<b>'+escape(b.get('label','BEACHTEN'))+'</b> '+b['text'],'warn' if b.get('tone')=='stop' else 'cell')
   _,h=q.wrap(w-18,1000);return ('note',q,b),h+16
  if kind=='table':
   ws=b.get('widths',[1]*len(b['headers']));ws=[w*x/sum(ws) for x in ws]
   data=[[para(x,'head') for x in b['headers']]]+[[para(x,'cell') for x in row] for row in b['rows']]
   q=Table(data,colWidths=ws,hAlign='LEFT')
   q.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E6EFF0')),('LINEBELOW',(0,0),(-1,0),.6,TEAL),('LINEBELOW',(0,1),(-1,-1),.3,LINE),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
   _,h=q.wrap(w,1000);return q,h
  if kind=='figure':
   if 'path' in b:q=Photo(b['path'],w,b.get('maxh',220),b.get('crop'),b.get('marks'))
   else:
    from diagrams import Diagram
    q=Diagram(b['kind'],w,b.get('maxh',180))
   return q,q.height
  if kind=='columns':
   gap=b.get('gap',15);rr=b.get('widths',[1,1]);ws=[(w-gap)*x/sum(rr) for x in rr]
   hh=[sum(self.blockheight(x,ww)+x.get('after',7) for x in bs) for ww,bs in zip(ws,b['columns'])]
   return ('columns',b,ws),max(hh)-7
  if kind=='space':return None,b['height']
  raise ValueError(kind)
 def drawblock(self,b,x,y,w,page):
  q,h=self.make(b,w)
  if isinstance(q,tuple):
   if q[0]=='note':
    _,p,info=q; c=self.c
    c.setFillColor(colors.HexColor('#FFF3E9') if info.get('tone')=='stop' else colors.HexColor('#EDF4F3'))
    c.rect(x,y-h,w,h,stroke=0,fill=1)
    c.setFillColor(RED if info.get('tone')=='stop' else TEAL);c.rect(x,y-h,3,h,stroke=0,fill=1)
    p.drawOn(c,x+9,y-h+8)
   else:
    _,bb,ws=q;xx=x
    for ww,bs in zip(ws,bb['columns']):
     yy=y
     for item in bs:yy=self.drawblock(item,xx,yy,ww,page)
     xx+=ww+bb.get('gap',15)
  elif q is not None:
   xx=x+(w-q.width)/2 if b['type']=='figure' else x
   q.drawOn(self.c,xx,y-h)
   if b['type']=='figure':self.figures.append({'page':page,'path':b.get('path'),'kind':b.get('kind'),'width':q.width,'height':q.height})
  self.placements.append({'page':page,'type':b['type'],'x':x,'top':y,'bottom':y-h,'width':w})
  return y-h-b.get('after',7)
 def build(self):
  for i,p in enumerate(self.pages,1):
   c=self.c;c.bookmarkPage('p'+str(i));c.addOutlineEntry(f'{i:02d} | '+p['title'],'p'+str(i),0,False)
   c.setFillColor(TEAL);c.rect(0,H-10,W,10,stroke=0,fill=1)
   c.setFillColor(GREY);c.setFont('Bold',8.5);c.drawString(M,H-33,p['phase'].upper())
   c.setFont('Body',8.5);c.drawRightString(W-M,H-33,f'ARBEITSKARTE {i:02d}')
   title=Paragraph(norm(p['title']),ParagraphStyle('title',fontName='Bold',fontSize=21,leading=24,textColor=INK))
   _,th=title.wrap(CW,90);title.drawOn(c,M,H-47-th)
   y=H-47-th-11
   if p.get('goal'):y=self.drawblock({'type':'p','text':p['goal'],'after':9},M,y,CW,i)
   if p.get('before'):y=self.drawblock({'type':'note','label':'VORHER','text':p['before'],'after':10},M,y,CW,i)
   for b in p['blocks']:y=self.drawblock(b,M,y,CW,i)
   if p.get('check'):y=self.drawblock({'type':'note','label':'WEITER, WENN','text':p['check'],'after':0},M,y,CW,i)
   if y<61:raise ValueError(f'Page {i} {p["title"]}: overflow by {61-y:.1f}pt; bottom {y:.1f}')
   c.setStrokeColor(LINE);c.setLineWidth(.5);c.line(M,48,W-M,48)
   c.setFont('Body',7.7);c.setFillColor(GREY)
   c.drawString(M,35,'REV12 | ICE 2976 | 11.09.2026')
   c.drawRightString(W-M,35,f'{i} / {len(self.pages)}')
   refs=p.get('sources',[])
   c.drawString(M,23,'Quellen: '+', '.join(refs)+f' (S. {len(self.pages)})' if refs else 'Originalreferenz: REV10 | Persönliche Gerätewerte vor Anwendung eintragen')
   if i<len(self.pages):
    lab='Weiter: '+str(i+1);c.drawRightString(W-M,23,lab);c.linkAbsolute(lab,'p'+str(i+1),Rect=(W-M-68,19,W-M,30))
   c.showPage()
  c.save()
