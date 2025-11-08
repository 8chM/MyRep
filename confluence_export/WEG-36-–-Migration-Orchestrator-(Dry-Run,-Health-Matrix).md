---
title: WEG-36 – Migration Orchestrator (Dry-Run, Health Matrix)
confluence_id: 27165417
version: 18
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27165417/WEG-36+Migration+Orchestrator+Dry-Run+Health+Matrix
---

**JIRA-Link:** [WEG-36 – Migration Orchestrator (Dry-Run, Health Matrix)](https://maierharry.atlassian.net/browse/WEG-36)

## Überblick

Das Modul **Migration Orchestrator** (WEG-36) steuert die Verwaltung, Durchführung und Überwachung von Datenbankmigrationen über alle WEG-Schemata hinweg.

Es bietet Funktionen für kontrollierte Migrationsläufe, Dry-Runs zur Vorabprüfung und eine Health-Matrix zur Auswertung des Migrationserfolgs.

Ziel ist es, sichere, wiederholbare und nachvollziehbare Migrationen durchzuführen, um Schema-Änderungen in einer Multi-Tenant-Umgebung zuverlässig auszurollen.

## Beschreibung

Der Migration Orchestrator sorgt für den systemweiten, kontrollierten Ablauf aller Migrationsvorgänge.

Er prüft Abhängigkeiten, führt Migrationen tenantweise aus und dokumentiert deren Erfolg oder Fehlerzustand.

Durch Integration mit dem Scheduler (WEG-12) und dem Admin Panel (WEG-33) können Migrationen automatisiert, überwacht und erneut ausgeführt werden.

Hauptfunktionen:

- **Dry-Run:** Führt eine Simulation der Migration aus, ohne Änderungen an produktiven Daten vorzunehmen; prüft Schema-Kompatibilität und Laufzeitdauer.

- **Migration Execution:** Führt Migrationsskripte sequentiell oder parallel aus, abhängig von Systemlast und Priorität.

- **Health Matrix:** Erstellt nach jeder Migration eine Übersicht über erfolgreiche, fehlerhafte oder übersprungene Tenants – inklusive Dauer, Status und Fehlermeldungen.

- **Retry & Scheduler:** Fehlgeschlagene Migrationen werden automatisch erneut eingeplant; Verwaltung erfolgt über den Scheduler (WEG-12).

- **Progress Monitoring:** Fortschritt und Status jeder Migration sind über das Admin Panel (WEG-33) einsehbar.

- **Audit Logging:** Alle Aktionen werden im Audit-Log (WEG-24) dokumentiert, einschließlich Benutzer, Version, Tenant und Ergebnis.

## Geschäftsregeln & Logik

- Migrationen müssen **idempotent** sein – ein erneuter Lauf darf keine inkonsistenten Zustände erzeugen.

- **Dry-Runs** dürfen keine Daten verändern, sondern nur die Validierung und Protokollierung durchführen.

- Migrationen werden **pro Tenant isoliert** ausgeführt; ein Fehler darf keine anderen Mandanten beeinträchtigen.

- Jede Migration besitzt eine eindeutige **Versionskennung** und wird mit Hashwert verifiziert.

- Ein fehlerhafter Lauf darf nur über **Resume/Retry** fortgesetzt werden, niemals manuell.

- Alle Migrationsdateien werden zentral verwaltet und versioniert (über WEG-10).

## Akzeptanzkriterien

- **Gegeben** ein neues Release enthält Migrationen &rarr; **Wenn** der Migration Orchestrator gestartet wird &rarr; **Dann** führt das System die Migrationen für alle aktiven Tenants aus und erstellt eine vollständige Health-Matrix.

- **Gegeben** ein Dry-Run wird ausgeführt &rarr; **Wenn** der Prozess abgeschlossen ist &rarr; **Dann** werden keine Daten verändert, aber das Protokoll und die Ausführungszeiten dokumentiert.

- **Gegeben** eine Migration schlägt fehl &rarr; **Wenn** der Scheduler aktiv ist &rarr; **Dann** wird die Migration automatisch für den nächsten geplanten Lauf wieder eingeplant.

- **Gegeben** eine Migration wird erfolgreich abgeschlossen &rarr; **Wenn** das Audit-Log geprüft wird &rarr; **Dann** ist der Tenant-Status mit Zeit, Version und Prüfsumme korrekt dokumentiert.

- **Gegeben** mehrere Migrationen laufen parallel &rarr; **Wenn** ein Tenant blockiert ist &rarr; **Dann** wird dieser übersprungen und im Health-Report als &bdquo;skipped&ldquo; markiert.

## Nicht-Ziele

- Kein automatisches Rollout von Migrationen während aktiver Produktionsprozesse.

- Keine Live-Schemaänderungen ohne vorherige Dry-Run-Validierung.

- Kein manuelles Bearbeiten von Migrationsergebnissen über die Benutzeroberfläche.

## Kritische Fälle

- **Inkompatible Migrationen:** Fehlerhafte SQL-Skripte können Tenants unbrauchbar machen; Dry-Run-Validierung ist zwingend erforderlich.

- **Langlaufende Migrationen:** Migrationen mit hoher Laufzeit müssen überwacht, segmentiert oder gestaffelt werden.

- **Fehlerhafte Wiederholungen:** Nicht idempotente Migrationen dürfen keine doppelten Änderungen erzeugen.

- **Rollback-Risiko:** Ohne Rollback-Mechanismus können fehlerhafte Migrationen manuelles Eingreifen erfordern.

## Abhängigkeiten

-  – Scheduler- und Job-Management für automatische Retries.

-  – Speicherung und Versionierung der Migrationsskripte.

-  – Nachvollziehbarkeit aller Migrationen und Benutzeraktionen.

-  – Anzeige des Migrationsstatus und der Health-Matrix.

-  – Routing zu den jeweiligen Tenant-Datenbanken während der Migration.

## Offene Fragen

- Soll ein **Rollback-Mechanismus** pro Tenant integriert werden (automatisch oder manuell)?

- Wie soll die **Versionierung** der Migrationen im MVP verwaltet werden (z. B. EF Core, Liquibase, manuelle Skripte)?

- Soll die **Health-Matrix** als historisches Reporting exportierbar sein?

## Zukunftserweiterungen

- **Zero-Downtime-Migrationen:** Einsatz von Blue/Green-Deployment oder Shadow-Schemas zur unterbrechungsfreien Aktualisierung.

- **Online-Migrationen:** Migrationen in Echtzeit mit gleichzeitiger Datentransformation.

- **Rollback-Funktionalität:** Automatische Wiederherstellung fehlerhafter Migrationen.

- **Visualisierte Health-Matrix:** Erweiterte Dashboards mit Fehlerdetails, Statistiken und Exportfunktionen.

## Verknüpfte Tasks

- [WEG-360 – Health Matrix & Resume/Retry](https://maierharry.atlassian.net/browse/WEG-360) – Implementiert die Überwachung und Wiederaufnahme fehlerhafter Migrationen.

- [WEG-361 – Dry-Run Simulation](https://maierharry.atlassian.net/browse/WEG-361) – Führt Migrationen ohne Datenänderung aus und erstellt Ablaufprotokolle.

- [WEG-362 – Scheduler-Integration](https://maierharry.atlassian.net/browse/WEG-362) – Bindet Migrationen in geplante Systemjobs ein.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Dry-Run, Health-Matrix, manuelle und Scheduler-gestützte Migrationen, Audit-Protokollierung.

**Phase 2**

Zero-Downtime-Migrationen, automatische Rollbacks und erweiterte Überwachung.

**Phase 3**

Online-Migrationen, visuelle Health-Matrix, Live-Statistiken und Reporting-Funktionen.