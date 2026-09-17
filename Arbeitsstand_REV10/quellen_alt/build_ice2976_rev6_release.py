"""Final pagination and consistency corrections after the focused REV6 reviews."""
from pathlib import Path
root=Path(__file__).resolve().parent
script=(root/'build_ice2976_rev6_final.py').read_text()
extra='''
replace("original('15. Den vorhandenen 60974 vorbereiten',[", "original('15. Den vorhandenen 60974 vorbereiten',[\\n('refs(9,10,11)','refs(9)'),")
replace("original('24. Prüfkarte: verdeckte Kontakte beim Schließen',[", "original('24. Prüfkarte: verdeckte Kontakte beim Schließen',[\\n(\\"story.append(Sketch('screw',160))\\",\\"add('Befestigungsschema und Kontaktgefahren: siehe Kapitel 9.','small')\\"),")
replace('Die positive Kontaktprüfung ist', 'Die positive Kontaktprüfung ist') if 'Die positive Kontaktprüfung ist' in source else None
'''
needle="exec(compile(source,str(base),'exec'),{'__file__':str(base),'__name__':'__main__'})"
assert needle in script
script=script.replace(needle,extra+'\n'+needle)
exec(compile(script,str(root/'build_ice2976_rev6_final.py'),'exec'),{'__file__':str(root/'build_ice2976_rev6_final.py'),'__name__':'__main__'})
