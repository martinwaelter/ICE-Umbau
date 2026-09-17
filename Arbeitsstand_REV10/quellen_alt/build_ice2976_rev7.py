"""Build a case-specific REV7, preserving all previous artifacts and safety corrections."""
from pathlib import Path
import ast
import hashlib
import json

root = Path(__file__).resolve().parent
previous_pdf = root / 'output/pdf/ICE_2976_Umbauanleitung_REV6_PRUEFFASSUNG.pdf'
previous_hash = hashlib.sha256(previous_pdf.read_bytes()).hexdigest()
final_path = root / 'build_ice2976_rev6_final.py'
final_code = final_path.read_text().rsplit("exec(compile(source,str(base),'exec')", 1)[0]
context = {'__file__': str(final_path)}
exec(compile(final_code, str(final_path), 'exec'), context)

def assigned(path, name):
    for node in ast.parse(path.read_text()).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise ValueError(name)

exec(assigned(root / 'build_ice2976_rev6_release.py', 'extra'), context)
closure = root / 'build_ice2976_rev6_closure.py'
context['replace'](assigned(closure, 'before'), assigned(closure, 'after'))
source = context['source'].replace('REV6', 'REV7')
source = source.replace('ICE_2976_Umbauanleitung_REV7_PRUEFFASSUNG.pdf', 'ICE_2976_Umbauanleitung_REV7_KONKRET.pdf')
source = source.replace("page('ICE 2976: Umbauanleitung REV7')", "from rev7_content import install\ninstall(globals())\npage('ICE 2976: Umbauanleitung REV7')", 1)
source = source.replace('Diese Fassung ersetzt die entsprechenden Arbeitsanweisungen der REV5.', 'Diese Fassung ersetzt die Arbeitsanweisungen der REV6; REV6 bleibt als Vergleich erhalten.')
source = source.replace("page('E. Änderungen und verbleibender Prüfstatus')", "page('E. Dein ausgefüllter Anschlussstand')", 1)
start = source.index("page('E. Dein ausgefüllter Anschlussstand')")
end = source.index("page('Quellen und Geltungsbereich')", start)
source = source[:start] + """page('E. Dein ausgefüllter Anschlussstand')
add('Vor dem ersten Einschalten diese Werte aus den jeweiligen Arbeitskarten übertragen. Ein leeres Feld ist keine Freigabe. Bewahre die Fotos und die beiden ausgelesenen Decoderprojekte zusammen mit dieser Seite auf.')
table(['Für genau diesen ICE 2976','Einzutragen / Nachweis'],[
('60977 + 59649, Vorabtest A-C','Datum, Programmerzugang, Identitätsnachweis, Testergebnis: __________________'),
('Rote LoDi 511','Revision: ______; vorhandene Jumperstellung: ______; Innenlicht-AUX aus 8a: ______'),
('Zwei Befestigungsringe der LoDi 511','Ring A: ______; Ring B: ______; Freigabefoto/-messung nach 9: ______'),
('60941-Motor','Isolationsprotokoll 6b vollständig: ______; C90-Motortyp am 60977 rückgelesen: ______'),
('LoDi-514-Fronteinsätze','Vorn Weiß/Rot-Zweige bestätigt: ______; hinten R Weiß: ______; R Rot: ______; Belastbarkeit: ______'),
('Märklin-Träger mit ESU 59649','+Ub / LV / LR / B/GR / 0/GL und Steckindex abgeglichen: ______'),
('Lautsprecher aus 60977','Unverändertes Original: ______; Gegenstecker/Adapter: ______; Prüfung L1-L5: ______'),
('Mittelwagen','Anzahl: ______; je Wagen RT an O, GE an L, B leer; Prüfblätter 14a/14b: ______'),
('Gesamter Zug','Inbetriebnahme 52-56, Lastprüfung 57-59 und Gehäuseprüfung 24: ______'),
('60974 / Signalhalt','60974 bleibt bis eigenem Anschlussnachweis abgesteckt. CS3-Signalhalt separat nach 19 abnehmen.')],[2.5,4.0])
add('REV7 konkretisiert den vorhandenen Aufbau. Die elektrische Architektur bleibt unverändert: vorn 60977 auf LoDi 511, hinten 59649 auf Märklin-Träger, RT gemeinsam und GE nur vorn gespeist. Die eigentliche Identitätsübernahme sowie die unbekannten Revisionen werden nicht durch Formulierungen ersetzt.','small')
warn('Vor weiteren Arbeiten am ICE', 'Solange A-C nicht bestanden sind, nur den getrennten Decoder-Nachweis und die Fotos aus D beschaffen. Nach jedem späteren Wechsel einer Platine, Verdrahtung oder Decoderkonfiguration die davon betroffene Arbeitskarte erneut ausführen.')

""" + source[end:]
source = source.replace("'REV7 - Prüffassung; offene Prüftore beachten'", "'REV7 - ICE 2976; konkrete Arbeitsfassung mit offenen Nachweisen'")
source = source.replace("title='ICE 2976 - Umbauanleitung REV7 Prüffassung'", "title='ICE 2976 - Umbauanleitung REV7 konkret'")
source = source.replace("subject='Vorgezogener mfx-Nachweis, Anschlussklärung, Motorisolation, Kupplungsprüfungen'", "subject='Konkrete Bauteilzuordnung, Jumperzustände und Arbeitskarten für ICE 2976'")
scope = {'__file__': str(root / 'build_ice2976_rev6.py'), '__name__': '__main__'}
exec(compile(source, str(root / 'build_ice2976_rev7.py'), 'exec'), scope)
assert hashlib.sha256(previous_pdf.read_bytes()).hexdigest() == previous_hash, 'REV6 was changed'
print(json.dumps({'rev6_unchanged_sha256': previous_hash, 'concrete_replacements': scope['REV7_HITS']}, ensure_ascii=False, indent=2))
