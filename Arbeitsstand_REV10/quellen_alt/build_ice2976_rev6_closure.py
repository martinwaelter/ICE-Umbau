"""Close the final review's first-registration ordering issue without editing prior builders."""
from pathlib import Path

root = Path(__file__).resolve().parent
release = root / 'build_ice2976_rev6_release.py'
script = release.read_text()
before = 'In den CS3-Systemeinstellungen Sichern wählen, USB-Speicherort und neuen Dateinamen verwenden; nicht Wiederherstellen. Der Fachkundige untersucht nur eine Kopie: Enthält sie lokomotive.cs2 und zum eindeutig identifizierten 60977 das Feld .mfxuid? Dieses Feld ist für CS2 dokumentiert; Inhalt und Zuordnung der konkreten CS3-Sicherung sind noch zu prüfen. Nichts bearbeiten oder zurückspielen.<super>12,19</super>'
after = '60977 noch nicht registriert? Ausschließlich den Master allein unter C1/C2-Sicherheitsbedingungen anmelden; diese Einzelanmeldung ist vor B-Abschluss erlaubt. Danach CS3-Systemeinstellungen: Sichern auf USB unter neuem Namen, nicht Wiederherstellen. Fachkundig nur eine Kopie prüfen: lokomotive.cs2 vorhanden und .mfxuid eindeutig diesem 60977 zugeordnet? Das Feld ist für CS2 dokumentiert, die konkrete CS3-Sicherung noch ungeprüft. Nichts bearbeiten/zurückspielen. Gemeinsamer Slave-Versuch erst nach bestätigter Identitätszuordnung.<super>12,19</super>'
needle = "extra='''"
assert script.count(needle) == 1
script = script.replace(needle, needle + '\n' + f'replace({before!r}, {after!r})' + '\n')
exec(compile(script, str(release), 'exec'), {'__file__': str(release), '__name__': '__main__'})
