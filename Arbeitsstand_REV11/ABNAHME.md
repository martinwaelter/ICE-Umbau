# REV11 – Abschluss der Dokumentüberarbeitung

Stand: 11.09.2026. Auftrag: die vom Nutzer benannte REV10 korrigieren, mit ausgewählten detaillierten Originalbildern und Zeichnungen zu einer überschaubaren, vollständigen Werkstattfolge zusammenstellen und die letzten Korrekturen einschließlich des Ablaufs ohne Händler einarbeiten.

## Ergebnis

- Eine PDF mit 40 Seiten, 22 Bild- und Schemaeinsätzen (13 Fotos/Herstellerabbildungen, 9 Vektorschemen), 23 Quellen, 40 Lesezeichen und 199 Verknüpfungen.
- Finale PDF: `output/pdf/ICE_2976_Umbauanleitung_REV11_WERKSTATTFASSUNG.pdf`.
- SHA-256: `3c67f596856f5403eac6f27f1f2512379555d3611749e4a7bd94f817cc7e41cb`.
- Unveränderte REV10-Referenz, SHA-256: `2a07914135e92b066701b02029ab4315c624083dd5cb5890774b7b629d7f0ec0`.

## Prüfung

Die inhaltliche Abdeckung wurde unabhängig gegen die REV10 geprüft. Die Programmierkarten und alle 40 gerenderten Seiten wurden visuell kontrolliert. Dabei gefundene Layout- und Ablaufprobleme wurden behoben und die betroffenen Seiten erneut geprüft. Dazu gehören Zeichnungsbeschriftungen, Bildausschnitte und Lesbarkeit, die getrennten CV-Listen für Index- und Firmwaredaten, die Reihenfolge der Firmwareermittlung und die bedingte AUX4-Einstellung.

Die abschließende automatisierte Prüfung ist in `final_validation.json` dokumentiert: keine ungültigen internen Seitenziele, keine außerhalb der Seiten liegenden Textzeichen, keine nicht aufgelösten redaktionellen Platzhalter; 40 Seiten und 40 Lesezeichen; Original-Hash unverändert.

## Prüfgrenze und nächste praktische Arbeit

Abgeschlossen ist die Dokumentüberarbeitung einschließlich Quellen-, Inhalts-, Verweis- und Layoutprüfung. Kein physischer Umbau, kein Decoderzugriff und keine Fahrzeugmessung wurden ausgeführt. Die Anleitung benennt die noch am eigenen Material zu ermittelnden Werte am jeweiligen Arbeitsschritt. Als nächstes sind die vorbereitenden Messkarten und die Decoderpaar-Prüfung mit tatsächlichen Werten abzuarbeiten; erst danach folgen die davon abhängigen Umbauarbeiten.
