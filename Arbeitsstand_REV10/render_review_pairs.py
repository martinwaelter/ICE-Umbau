"""Contact sheets of generated PDF pages for visual QA, never modify source photographs."""
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import json
ROOT=Path(__file__).resolve().parent.parent
TMP=ROOT/'tmp/pdfs/rev10';count=json.loads((TMP/'build_report.json').read_text())['pages']
for first in range(1,count+1,2):
    pages=[]
    for n in range(first,min(first+2,count+1)):
        p=TMP/f'page-{n:02d}.png'
        if not p.exists():p=TMP/f'page-{n:03d}.png'
        im=Image.open(p).convert('RGB');pages.append(im)
    result=Image.new('RGB',(sum(im.width for im in pages)+12, max(im.height for im in pages)+26),'#c9d1d4')
    d=ImageDraw.Draw(result);x=4
    for n,im in enumerate(pages,first):
        result.paste(im,(x,22));d.text((x+8,4),f'PDF-Seite {n}',fill='black');x+=im.width+4
    result.save(TMP/f'pruefpaar-{first:02d}-{min(first+1,count):02d}.jpg',quality=90)
print('Review pairs:',(count+1)//2)
