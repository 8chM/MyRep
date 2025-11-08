---
title: WEG-53 – Template Engine (Foundation)
confluence_id: 27329328
version: 12
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329328/WEG-53+Template+Engine+Foundation
---

**JIRA-Link:** [WEG-53 – Template Engine (Foundation)](https://maierharry.atlassian.net/browse/WEG-53)

## Überblick

Das Modul **Template Engine** (WEG-53) ermöglicht die automatisierte Erstellung strukturierter Dokumente aus wiederverwendbaren Vorlagen.

Es stellt sicher, dass alle systemrelevanten Dokumente wie Abrechnungen, Verträge, Protokolle oder Benachrichtigungen konsistent, vollständig und im korrekten Layout erzeugt werden.

Ziel ist eine flexible, mandantenspezifische Dokumentenerstellung mit Branding, Versionierung und Anbindung an andere Systemmodule.

## Beschreibung

WEG-53 bildet die Grundlage für die gesamte dokumentbasierte Kommunikation innerhalb des Systems.

Es ersetzt manuelle Textverarbeitung durch ein dynamisches Template-System, das Platzhalter aus verschiedenen Datenquellen (z. B. Eigentümer, Einheiten, Finanzen, Meetings) automatisch mit Live-Daten befüllt.

Hauptfunktionen:

- **Zentrale Vorlagenverwaltung:** Verwaltung und Versionierung aller Templates im System; jede Vorlage kann Platzhalter wie {{Owner.Name}} oder {{Association.Address}} enthalten.

- **Automatisches Rendering:** Platzhalter werden beim Erstellen durch aktuelle Daten ersetzt, das resultierende Dokument als PDF generiert und gebrandet (über WEG-56).

- **DMS-Integration:** Alle erzeugten Dokumente werden automatisch im Dokumentenmanagement (WEG-50) gespeichert, versioniert und revisionssicher archiviert.

- **Scheduler-Integration:** Über geplante Jobs (WEG-12) können wiederkehrende Dokumente — z. B. monatliche Berichte oder Eigentümerabrechnungen — automatisch erzeugt werden.

- **Template-Includes & Partials:** Wiederverwendbare Textbausteine oder Unterabschnitte ermöglichen modulare Templates.

- **Validierungs-Engine:** Fehlende oder ungültige Platzhalter werden erkannt und verhindern fehlerhafte Dokumente.

## Geschäftsregeln & Logik

- Alle Templates sind mandantenspezifisch und dürfen nur innerhalb der zugehörigen WEG verwendet werden.

- Jede Template-Version wird archiviert und ist revisionssicher.

- Platzhalter müssen einer bekannten Datenquelle (Domain-Entity) entsprechen.

- Branding (z. B. Logo, Farben) wird automatisch aus WEG-56 angewendet.

- Automatisch erzeugte Dokumente werden mit Zeitstempel und Quelle versehen.

## Akzeptanzkriterien

- **Gegeben** eine Vorlage enthält gültige Platzhalter &rarr; **Wenn** sie gerendert wird &rarr; **Dann** wird das vollständige PDF erstellt und im DMS versioniert gespeichert.

- **Gegeben** ein Platzhalter ist ungültig oder fehlt &rarr; **Wenn** das Dokument generiert wird &rarr; **Dann** wird ein Validierungsfehler ausgegeben und der Vorgang abgebrochen.

- **Gegeben** ein Scheduler-Job ist konfiguriert &rarr; **Wenn** der Job ausgeführt wird &rarr; **Dann** wird das Dokument automatisch erzeugt und archiviert.

- **Gegeben** ein Template wird geändert &rarr; **Wenn** eine neue Version gespeichert wird &rarr; **Dann** bleibt die alte Version im Archiv nachvollziehbar erhalten.

- **Gegeben** ein Dokument wird aus mehreren Partials zusammengesetzt &rarr; **Wenn** die Template-Engine rendert &rarr; **Dann** werden alle Teilvorlagen korrekt zusammengeführt.

## Nicht-Ziele

- Kein WYSIWYG-Template-Editor im MVP.

- Keine direkte Online-Bearbeitung von Platzhaltern durch Endnutzer:innen.

- Kein direkter Export in alternative Formate (z. B. DOCX) im MVP.

## Kritische Fälle

- **Fehlende Platzhalterdefinitionen:** Dokumente dürfen nicht generiert werden, wenn ein Platzhalter keiner Quelle zugeordnet ist.

- **Ungültige Template-Version:** Nur freigegebene Versionen dürfen produktiv verwendet werden.

- **Renderfehler:** Bei fehlerhaften Daten (z. B. Null-Referenzen) muss das System eine aussagekräftige Fehlermeldung liefern.

## Abhängigkeiten

-  – Speicherung und Versionierung der erzeugten Dokumente.

-  – Anwendung des individuellen Brandings pro Association.

-  – Erfassung von Fehlern bei der Dokumentengenerierung.

-  – Verwendung zur Erstellung von Abrechnungsdokumenten.

-  – Nutzung für Protokolle, Beschlussdokumente und Einladungen.

## Offene Fragen

- Soll die Template-Engine bereits im MVP einen internen Platzhalter-Editor enthalten?

- Müssen Templates mehrsprachig verwaltet werden (in Verbindung mit WEG-15)?

- Soll ein Freigabeprozess (Review/Publish) für Templates implementiert werden?

## Zukunftserweiterungen

- **Editor mit Live-Vorschau:** Visualisierung von Templates mit Echtzeitdaten.

- **Multi-Language-Templates:** Unterstützung mehrsprachiger Dokumente (z. B. DE/EN).

- **Template Marketplace:** Austausch standardisierter Vorlagen zwischen WEGs.

- **Automatische Aktualisierungen:** Synchronisierung von zentral gepflegten Standardtemplates.

## Verknüpfte Tasks

- [WEG-530 – Placeholder/Includes/Partials](https://maierharry.atlassian.net/browse/WEG-530) – Implementierung der Platzhalterlogik und Partials.

- [WEG-531 – Template Validation Engine](https://maierharry.atlassian.net/browse/WEG-531) – Validierung von Platzhaltern und Datenquellen.

- [WEG-532 – Scheduler Integration](https://maierharry.atlassian.net/browse/WEG-532) – Automatische Dokumentengenerierung durch geplante Jobs.

- [WEG-533 – DMS Auto-Linking](https://maierharry.atlassian.net/browse/WEG-533) – Automatische Ablage und Verknüpfung mit Objekten im DMS.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Zentrale Template-Verwaltung, Platzhalter-Engine, PDF-Rendering mit Branding, DMS-Integration, Scheduler-Unterstützung.

**Phase 2**

Live-Editor mit Vorschau, mehrsprachige Templates, erweiterte Validierung und Versionierung.

**Phase 3**

Template Marketplace, automatische Updates, Integration mit externen Template-Providern.