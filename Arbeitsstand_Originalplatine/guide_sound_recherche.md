# ICE-1-Sound für 60977: begrenzter Primärquellenbefund

Stand 12.09.2026. Keine Anleitung oder Seitenmodule verändert.

**Belegt:** Märklins [mDecoderTool3-Anleitung v3.6.0](https://streaming.maerklin.de/public-media/mdt3/pdfs/D_mDecoderTool3_A5_v360.pdf), lokal unter `belege_62762/mdt3_manual_v360.pdf` gelesen. S. 2: Software benötigt Windows-PC; CS3 oder 60971 sind Programmierwege, die Soundbibliothek wird getrennt geladen. S. 3: Auslesen sichert Einstellungen, aber keine Sounds. S. 4–6: Sound-Auswahl, Bibliothekszuweisung und Funktionen. S. 6–7: Übertragen nur Sounds/nur Einstellungen/beides. S. 8: vollständige Artikelprojekte können ebenfalls geladen und für mSD3 angepasst werden.

**Nicht primär verifiziert:** Aktuelle ICE-1-Projekt-ID, exakter jetziger Bibliotheksname oder bestimmtes Artikelprojekt für den Umbau 2976. Die aktuellen deutschen Downloadseiten waren im direkten Abruf nicht erreichbar/404; die konkrete ältere ICE1/ICE2-tgz-Datei aus Foren ist kein verifizierter heutiger mSD3-Hauptweg. Insbesondere wird keine 37702-/37703-Nummer als notwendige Projekt-ID ausgegeben.

## Kurzer Ersatztext für die Anleitung

1. In mDT3 `Sound → Soundbibliothek → vom Märklin-Server laden…` ausführen. Einen Windows-PC mit mDT3 verwenden; übertragen wird über den erkannten 60971 oder die CS3.
2. 60977 auslesen und Einstellungen sichern; diese Sicherung enthält keine Audiodaten. Neues Arbeitsprojekt als `mSD3 – Spur H0` anlegen und `ICE2976_62762` nennen.
3. Im Reiter `Sound-Auswahl` einen **Fahrsound** anlegen. Links einen ausdrücklich als **ICE 1 / BR 401** beschriebenen Bibliothekseintrag suchen und ihm per Drag-and-drop zuordnen. Ausgewählten Namen und Bibliotheksstand notieren; keinen ICE3-/ICE4-Sound aufgrund ähnlicher Bezeichnung wählen.
4. Gewünschte Zusatzgeräusche hinzufügen, danach Funktionen zuordnen. Ein vollständiges Fahrzeugprojekt alternativ nur als Ausgangspunkt verwenden: fremde Ausgangs- und Motoreinstellungen müssen angepasst werden.
5. **Vor Übertragung:** Motortyp für den 60941-HLA auf **CV52 = 3** prüfen; F0 und den unabhängig schaltbaren Wagenlicht-Ausgang **AUX1** gemäß dieser Umbauanleitung einstellen. AUX1 bleibt ungedimmtes Dauer-Ein/Aus.
6. Arbeitsprojekt speichern, dann ausdrücklich auswählen, ob Sounds, Einstellungen oder beides übertragen werden. Bei einer späteren reinen Soundänderung `nur Sounds` wählen; danach Motorwahl und Mapping kontrollieren. Eine erneute Übertragung kompletter Fremdeinstellungen darf die Umbaukonfiguration nicht überschreiben.

**Praktische Grenze:** Wird kein passender ICE-1-Eintrag angezeigt, zunächst Bibliotheksdownload erfolgreich abschließen. Eine nicht sichtbare aktuelle Sounddatei wird nicht durch eine erfundene Artikelnummer ersetzt. Der vorhandene 60977-Grundsound genügt vorläufig für Lautsprecher-/Funktionstests; das wäre jedoch noch kein bestätigtes ICE-1-Klangbild.

CV52 = 3 ist getrennt durch [Märklin 60975/60976/60977](https://static.maerklin.de/damcontent/f5/a9/f5a967e35e5b3faa19d17d36c62f586a1762409392.pdf) belegt. Mapping AUX1 ist unsere geänderte Verdrahtungsanforderung, keine vom Soundprojekt garantierte Werkseinstellung.
