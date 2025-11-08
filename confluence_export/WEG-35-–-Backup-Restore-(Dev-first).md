---
title: WEG-35 – Backup/Restore (Dev-first)
confluence_id: 27329298
version: 15
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329298/WEG-35+Backup+Restore+Dev-first
---

**JIRA-Link:** [WEG-35 – Backup/Restore (Dev-first)](https://maierharry.atlassian.net/browse/WEG-35)

## Überblick

Das Modul **Backup/Restore (Dev-first)** (WEG-35) ermöglicht die Sicherung und Wiederherstellung von WEG-Datenbanken, insbesondere für Entwicklungs-, Test- und Supportzwecke.

Es bietet Administratoren die Möglichkeit, vollständige Backups einzelner Mandanten zu erstellen, diese versioniert im DMS zu speichern und bei Bedarf wiederherzustellen.

Ziel ist es, Datenintegrität und Wiederherstellbarkeit sicherzustellen, ohne den laufenden Betrieb zu gefährden – insbesondere im Rahmen der Entwicklungs- und MVP-Phase.

## Beschreibung

WEG-35 stellt manuelle und teilweise automatisierte Backup-Mechanismen bereit, um vollständige Datenstände einzelner WEG-Schemata zu sichern.

Backups werden strukturiert, versioniert und nachvollziehbar im DMS gespeichert. Das System kann über den Scheduler (WEG-12) regelmäßige Sicherungen automatisiert ausführen.

Hauptfunktionen:

- **Manual Backup:** Administratoren können vollständige WEG-Schemas manuell sichern; das System erstellt eine komprimierte Backup-Datei und legt sie im DMS ab.

- **Restore-Funktion:** Gesicherte Schemata können wiederhergestellt werden. Vor einem Restore wird automatisch ein Sicherheitsbackup des aktuellen Zustands erstellt.

- **Versionierte Backups:** Alle Sicherungen sind mit Zeitstempel, Version und Benutzerkennung versehen, um Wiederherstellungen eindeutig nachvollziehen zu können.

- **Scheduler-Integration:** Über WEG-12 können automatische Nacht- oder Wochenend-Backups geplant werden.

- **Integritätsprüfung:** Nach Erstellung oder Wiederherstellung wird jedes Backup auf Vollständigkeit und Konsistenz geprüft.

- **Auditierbarkeit:** Alle Backup- und Restore-Aktivitäten werden im Audit-Log (WEG-24) dokumentiert.

## Geschäftsregeln & Logik

- Nur Benutzer mit der Rolle *SystemAdmin* oder *Manager* dürfen Backup- oder Restore-Aktionen ausführen.

- Jeder Restore-Vorgang erstellt automatisch ein Sicherheitsbackup des aktuellen Zustands vor der Wiederherstellung.

- Versionierte Backups müssen chronologisch sortiert und eindeutig identifizierbar sein.

- Backups dürfen keine aktiven Schreibprozesse unterbrechen; sie laufen asynchron.

- Fehlerhafte Backups oder abgebrochene Wiederherstellungen werden automatisch verworfen und im Audit-Log dokumentiert.

- Die Wiederherstellung eines Mandanten darf nur erfolgen, wenn keine Benutzeraktivität im Zielsystem stattfindet.

## Akzeptanzkriterien

- **Gegeben** ein Administrator startet ein manuelles Backup &rarr; **Wenn** der Vorgang abgeschlossen ist &rarr; **Dann** wird die Backup-Datei im DMS gespeichert, versioniert und im Audit-Log erfasst.

- **Gegeben** ein Administrator startet einen Restore-Vorgang &rarr; **Wenn** das Backup erfolgreich eingespielt wird &rarr; **Dann** wird der Tenant automatisch aktiviert und alle Daten sind konsistent wiederhergestellt.

- **Gegeben** ein automatischer Backup-Zeitplan ist aktiv &rarr; **Wenn** der Scheduler die Ausführung startet &rarr; **Dann** werden Backups erstellt, validiert und archiviert, ohne den laufenden Betrieb zu stören.

- **Gegeben** ein Restore schlägt fehl &rarr; **Wenn** ein Fehler erkannt wird &rarr; **Dann** wird der Vorgang abgebrochen, das ursprüngliche Schema bleibt erhalten, und der Fehler wird im Audit-Log dokumentiert.

- **Gegeben** ein Benutzer versucht, ein Backup ohne Berechtigung auszuführen &rarr; **Wenn** der Befehl ausgelöst wird &rarr; **Dann** verweigert das System die Ausführung und erzeugt einen Audit-Eintrag.

## Nicht-Ziele

- Keine vollautomatische produktive Sicherung aller Mandanten (Snapshots).

- Keine Geo-Redundanz oder Cross-Region-Replikation im MVP.

- Keine Delta- oder inkrementellen Backups in Phase 1.

## Kritische Fälle

- **Restore Failure:** Wiederherstellungsfehler dürfen nicht zu teilweisen Datenüberschreibungen führen; das System muss atomar arbeiten.

- **Backup Integrity:** Beschädigte Backup-Dateien dürfen nicht importiert werden; Integritätsprüfungen sind zwingend.

- **Ressourcenauslastung:** Parallele Backups großer Mandanten dürfen die Systemleistung nicht beeinträchtigen.

- **Datenkonsistenz:** Wiederherstellungen dürfen nicht zu Versionskonflikten zwischen Schema und Anwendung führen.

## Abhängigkeiten

-  – Speicherung und Verwaltung der Backup-Dateien.

-  – Scheduler-Integration für geplante Backups und Fehlerüberwachung.

-  – Nachvollziehbarkeit aller Backup- und Restore-Aktivitäten.

-  – Verwaltung der Mandanteninformationen zur Backup-Zuordnung.

## Offene Fragen

- Soll die Backup-Funktion mit Verschlüsselung (z. B. AES-256) umgesetzt werden?

- Wie lange sollen Backups im DMS aufbewahrt werden (Retention-Strategie)?

- Soll der Scheduler benutzerdefinierte Zeitpläne unterstützen (z. B. wöchentlich, monatlich)?

- Soll eine E-Mail-Benachrichtigung bei erfolgreichen oder fehlgeschlagenen Backups erfolgen?

## Zukunftserweiterungen

- **Automatisierte Backup-Strategien:** Einführung regelmäßiger, zeitgesteuerter Sicherungen und inkrementeller Backups.

- **Point-in-Time-Recovery:** Wiederherstellung bis zu einem bestimmten Zeitpunkt, basierend auf Log-Shipping oder Delta-Daten.

- **Backup-Verschlüsselung:** Verschlüsselung ruhender Backups zur Erhöhung der Datensicherheit.

- **Cloud-Integration:** Speicherung von Backups in externen Cloud-Diensten (z. B. S3, Azure Blob Storage).

- **Geo-Redundanz:** Verteilung von Backups über mehrere Standorte zur Ausfallsicherheit.

## Verknüpfte Tasks

- [WEG-350 – Manual Backup/Restore Tools](https://maierharry.atlassian.net/browse/WEG-350) – Stellt CLI- und API-Befehle zum Erstellen, Validieren und Wiederherstellen von Backups bereit.

- [WEG-351 – Scheduler Integration](https://maierharry.atlassian.net/browse/WEG-351) – Bindet Backup- und Restore-Vorgänge in geplante Hintergrundprozesse ein.

- [WEG-352 – Integrity Validation Service](https://maierharry.atlassian.net/browse/WEG-352) – Prüft Backups nach Erstellung oder Wiederherstellung auf Vollständigkeit.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Manuelles Backup und Restore über UI/CLI, Speicherung im DMS, Audit-Logging, optionale Scheduler-Integration.

**Phase 2**

Automatisierte Backup-Strategien, inkrementelle Sicherungen, Cloud-Anbindung, Benachrichtigungen.

**Phase 3**

Point-in-Time-Recovery, Verschlüsselung, Geo-Redundanz und erweiterte Performance-Optimierungen.