from content import PAGES
from layout import Layout, H, CW, Paragraph, ParagraphStyle, INK
from pathlib import Path
l=Layout(Path('/tmp/unused_ice.pdf'),[])
for i,p in sorted(PAGES.items()):
 title=Paragraph(p['title'],ParagraphStyle('t',fontName='Bold',fontSize=21,leading=24,textColor=INK))
 _,th=title.wrap(CW,90);y=H-47-th-11
 if p.get('goal'):y-=l.blockheight({'type':'p','text':p['goal']},CW)+9
 if p.get('before'):y-=l.blockheight({'type':'note','label':'VORHER','text':p['before']},CW)+10
 for b in p['blocks']:y-=l.blockheight(b,CW)+b.get('after',7)
 if p.get('check'):y-=l.blockheight({'type':'note','label':'WEITER, WENN','text':p['check']},CW)
 print(f'{i:02} remaining {y-61:6.1f}pt {p["title"]}')
