---
title: WEG-63 – Messaging Search / Filter / Batch
confluence_id: 26968655
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/26968655/WEG-63+Messaging+Search+Filter+Batch
---

**JIRA-Link:** [WEG-63 – Messaging Search / Filter / Batch](https://maierharry.atlassian.net/browse/WEG-63)

## Überblick

Das Modul **Messaging Search / Filter / Batch** (WEG-63) erweitert das interne Kommunikationssystem um eine leistungsfähige Such- und Verwaltungsfunktion. Es ermöglicht die gezielte Suche nach Nachrichten, Threads oder Absendern, kombiniert mit Filtern, Sortierungen und Massenaktionen. Ziel ist es, Benutzern ein effizientes Werkzeug für das Auffinden, Analysieren und Bearbeiten von Kommunikationsinhalten zu bieten.

## Beschreibung

Dieses Modul integriert Such- und Verwaltungsmechanismen in das Messaging-System (WEG-6, WEG-61). Die Suchlogik basiert auf einem asynchron aktualisierten Suchindex, der eine hohe Performance bei minimaler Systembelastung sicherstellt. Neben der Volltextsuche bietet das Modul umfangreiche Filteroptionen und sichere Batch-Aktionen, um Nachrichten gezielt zu verwalten.

**Hauptfunktionen:**

- **Volltextsuche:** Durchsuchung von Nachrichteninhalten, Absendern, Empfängern, Zeiträumen und Einheiten.

- **Filter & Sortierung:** Eingrenzung der Ergebnisse nach Status (z. B. gesendet, gelesen, archiviert), Nachrichtentyp, Modulzugehörigkeit oder Zeitraum.

- **Batch-Operationen:** Gleichzeitige Aktionen auf mehrere Threads, z. B. Archivieren, Löschen oder Markieren als gelesen.

- **Asynchroner Suchindex:** Der Index wird periodisch aktualisiert, um Schreibvorgänge im Messaging-System nicht zu beeinträchtigen.

- **RBAC-Integration:** Berechtigungen für Such- und Batch-Aktionen werden über das Rollenmodell (WEG-21) gesteuert.

- **Audit-Logging:** Jede Massenaktion wird revisionssicher dokumentiert (WEG-24).

## Geschäftsregeln & Logik

- **Mandantenbezogene Suche:** Ergebnisse sind stets auf die aktuelle WEG beschränkt; keine mandantenübergreifenden Suchen im MVP.

- **Indexaktualisierung:** Neue oder geänderte Nachrichten werden in Intervallen indexiert, um die Systemlast zu reduzieren.

- **Batch-Aktionen:** Nur Benutzer mit entsprechenden Rollen (z. B. Verwalter) dürfen Aktionen auf mehrere Nachrichten gleichzeitig ausführen.

- **Lesestatus:** Suchergebnisse berücksichtigen den individuellen Lesestatus je Benutzer.

- **Auditierung:** Alle Änderungen und Aktionen werden im Audit-Log (WEG-24) festgehalten.

## Akzeptanzkriterien

- **Gegeben** ein Benutzer verwendet die Volltextsuche &rarr; **Wenn** er einen Begriff eingibt &rarr; **Dann** werden alle Nachrichten angezeigt, die den Suchbegriff im Inhalt, Betreff oder Absender enthalten.

- **Gegeben** ein Benutzer setzt mehrere Filter (z. B. Zeitraum und Status) &rarr; **Wenn** die Suche ausgeführt wird &rarr; **Dann** erscheinen nur Nachrichten, die allen Filterkriterien entsprechen.

- **Gegeben** mehrere Threads sind ausgewählt &rarr; **Wenn** eine Batch-Aktion ausgeführt wird &rarr; **Dann** wird die Aktion auf alle markierten Threads angewendet und protokolliert.

- **Gegeben** der Suchindex wird aktualisiert &rarr; **Wenn** neue Nachrichten hinzugefügt wurden &rarr; **Dann** erscheinen diese nach der nächsten Indexaktualisierung automatisch in den Suchergebnissen.

- **Gegeben** ein Benutzer versucht, eine Batch-Aktion ohne Berechtigung auszuführen &rarr; **Wenn** die Anfrage gesendet wird &rarr; **Dann** verweigert das System die Aktion und protokolliert den Vorfall im Audit-Log.

## Nicht-Ziele

- Keine mandantenübergreifende Suche über alle WEGs hinweg.

- Keine Integration mit externen Suchsystemen (z. B. ElasticSearch) im MVP.

- Kein Reporting oder komplexe Query-Builder-Funktionalität.

## Kritische Fälle

- **Index-Fehler:** Fehlerhafte oder verzögerte Indexaktualisierungen können zu unvollständigen Suchergebnissen führen.

- **Leistungsprobleme:** Große Datenmengen erfordern Paging und Limitierungen, um die Performance zu sichern.

- **Berechtigungsfehler:** Falsch konfigurierte RBAC-Policies könnten unbefugte Aktionen erlauben.

## Abhängigkeiten

-  – Berechtigungslogik für Such- und Batch-Aktionen.

-  – Quelle der durchsuchbaren Inhalte.

-  – Dokumentation aller Massenaktionen.

-  – Stellt sicher, dass verschlüsselte Daten nur über autorisierte Suchen sichtbar sind.

## Offene Fragen

- Soll die Suche in Zukunft mandantenübergreifend (für Multi-WEG-Administratoren) verfügbar sein?

- Wie groß darf die maximale Ergebnisliste sein, bevor Paging greift (Performance-Ziel)?

- Soll die Suche auch Anhänge aus dem DMS (WEG-5) einbeziehen?

## Zukunftserweiterungen

- **Erweiterte Filterlogik:** Volltextsuche in Anhängen über DMS-Volltextindex.

- **Suchvorschläge:** Intelligente Keyword-Vervollständigung.

- **Exportfunktionen:** Export der Trefferliste als CSV oder PDF.

- **KI-gestützte Relevanzbewertung:** Sortierung der Ergebnisse nach Wichtigkeit.

## Verknüpfte Tasks

- [WEG-630 – Messaging Search / Filters / Bulk Actions](https://maierharry.atlassian.net/browse/WEG-630) – Implementiert Such- und Batchlogik sowie UI-Integration.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Volltextsuche mit Filteroptionen, RBAC-basierten Batch-Aktionen und Audit-Logging.

**Phase 2**

Erweiterte Filterfunktionen, Suchvorschläge und optimierte Indexierung.

**Phase 3**

Exportfunktionen, KI-basierte Relevanzbewertung und mandantenübergreifende Suche.