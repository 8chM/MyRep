---
title: WEG-54 – Retention & Archive (Locked Periods)
confluence_id: 27460087
version: 11
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27460087/WEG-54+Retention+Archive+Locked+Periods
---

**JIRA-Link:** [WEG-54 – Retention & Archive (Locked Periods)](https://maierharry.atlassian.net/browse/WEG-54)

## Überblick

Das Modul **Retention & Archive (Locked Periods)** (WEG-54) stellt sicher, dass alle Dokumente innerhalb des Systems revisionssicher archiviert und gemäß gesetzlicher sowie interner Aufbewahrungsrichtlinien verwaltet werden.

Es sorgt dafür, dass Dokumente, die zu abgeschlossenen Abrechnungs- oder Wirtschaftsperioden gehören, automatisch gesperrt werden und nach Ablauf ihrer Aufbewahrungsfrist regelkonform archiviert oder gelöscht werden.

Ziel ist es, die langfristige Compliance-Sicherheit zu gewährleisten und gleichzeitig die Unversehrtheit und Nachvollziehbarkeit archivierter Daten sicherzustellen.

## Beschreibung

WEG-54 erweitert das Dokumentenmanagement (WEG-50) um Mechanismen zur Aufbewahrung, Sperrung und Archivierung von Dokumenten nach festgelegten Richtlinien.

Es ist ein essenzielles Modul zur Einhaltung von Vorschriften wie **GoBD** und **DSGVO**, insbesondere im Kontext revisionssicherer Speicherung.

Hauptfunktionen:

- **Periodenabschluss & Sperrung:** Nach dem Abschluss von Wirtschafts- oder Abrechnungsperioden werden alle zugehörigen Dokumente automatisch auf &bdquo;read-only&ldquo; gesetzt. Änderungen, Löschungen oder Ersetzungen sind danach nur noch über dokumentierte Administratorfreigaben möglich.

- **Retention Policies:** Jede Dokumentenkategorie erhält eine definierte Aufbewahrungsfrist (z. B. 10 Jahre für Buchhaltungsunterlagen). Nach Ablauf dieser Frist wird das Dokument automatisch archiviert oder gelöscht, abhängig von der zugewiesenen Policy.

- **Sperrstatus-Anzeige:** Der aktuelle Sperrstatus wird im DMS visuell angezeigt, um Administratoren und Benutzer:innen die Archivierungsphase klar zu kennzeichnen.

- **Scheduler-Integration:** Ein automatisierter Prozess prüft täglich alle Fristen und initiiert bei Ablauf die entsprechenden Aktionen (Archivierung, Löschung oder Verlängerung).

- **Audit-Protokollierung:** Jede Sperrung, Archivierung oder Freigabe wird im Audit-Log (WEG-24) revisionssicher erfasst, inklusive Zeitpunkt, Benutzer, Aktion und Begründung.

## Geschäftsregeln & Logik

- Nach Abschluss einer Periode werden alle zugehörigen Dokumente automatisch gesperrt.

- Gesperrte Dokumente dürfen nicht mehr verändert oder gelöscht werden.

- Nur Administrator:innen mit entsprechender Berechtigung (WEG-2) dürfen eine Sperre aufheben.

- Der Scheduler überwacht Aufbewahrungsfristen und initiiert automatisch Archivierungs- oder Löschvorgänge.

- Archivierte Dokumente bleiben zugänglich, aber unveränderlich.

- Alle Vorgänge werden revisionssicher im Audit-Log dokumentiert.

## Akzeptanzkriterien

- **Gegeben** eine Abrechnungsperiode ist abgeschlossen &rarr; **Wenn** der Abschluss gespeichert wird &rarr; **Dann** werden alle zugehörigen Dokumente automatisch auf &bdquo;read-only&ldquo; gesetzt.

- **Gegeben** ein Dokument ist gesperrt &rarr; **Wenn** ein Benutzer versucht, es zu bearbeiten oder zu löschen &rarr; **Dann** verweigert das System den Zugriff und protokolliert den Versuch im Audit-Log.

- **Gegeben** eine Aufbewahrungsfrist ist abgelaufen &rarr; **Wenn** der Scheduler ausgeführt wird &rarr; **Dann** archiviert oder löscht das System das Dokument automatisch gemäß Policy.

- **Gegeben** ein Administrator hebt eine Sperre auf &rarr; **Wenn** der Vorgang bestätigt wird &rarr; **Dann** wird die Aktion inklusive Benutzer, Grund und Zeit im Audit-Log vermerkt.

- **Gegeben** ein Dokument wird archiviert &rarr; **Wenn** ein Benutzer es öffnet &rarr; **Dann** kann es angezeigt, aber nicht mehr bearbeitet oder überschrieben werden.

## Nicht-Ziele

- Keine Benutzerverwaltung für individuelle Aufbewahrungsfristen.

- Kein externes Archivsystem im MVP.

- Keine automatisierte Synchronisierung mit Cloud-Archivlösungen.

## Kritische Fälle

- **Falsche Fristenkonfiguration:** Falsche Retention-Settings könnten zu vorzeitiger Löschung führen.

- **Fehlerhafte Sperrlogik:** Dokumente dürfen nach Abschluss nicht mehr editierbar sein – auch nicht durch API-Calls.

- **Unvollständige Audit-Protokollierung:** Jede Archiv- oder Löschaktion muss vollständig nachvollziehbar bleiben.

## Abhängigkeiten

-  – Verwaltung und Speicherung von Dokumenten.

-  – Scheduler-Überwachung und Fehlerprotokollierung.

-  – Erfassung und Nachvollziehbarkeit aller Sperr-, Archiv- und Löschvorgänge.

-  – Integration für DSGVO-konforme Lösch- und Aufbewahrungsprozesse.

## Offene Fragen

- Soll eine manuelle Verlängerung von Aufbewahrungsfristen durch Administrator:innen im MVP möglich sein?

- Sollen archivierte Dokumente in einer separaten Datenbank oder im selben DMS-Schema gespeichert werden?

- Müssen archivierte Dokumente erneut versioniert werden, wenn sie nach Ablauf reaktiviert werden?

## Zukunftserweiterungen

- **Automatische Compliance-Berichte** (z. B. GoBD, DSGVO) zur Nachverfolgung aller Archivierungs- und Löschvorgänge.

- **Erweiterte Retention Policies:** Unterschiedliche Fristen je nach Dokumenttyp, Kategorie oder rechtlicher Region.

- **Self-Service-Archivzugriff:** Eigentümer:innen können archivierte Dokumente über ein Portal einsehen.

- **Integrationen mit Cloud-Archivdiensten:** Anbindung an langfristige Speicherlösungen wie Azure Archive oder AWS Glacier.

## Verknüpfte Tasks

- [WEG-540 – Archive Rules; No edits in locked periods](https://maierharry.atlassian.net/browse/WEG-540) – Implementiert die Logik zur automatischen Sperrung und Archivierung von Dokumenten nach Periodenabschluss.

- [WEG-541 – Retention Policy Engine](https://maierharry.atlassian.net/browse/WEG-541) – Überwacht und steuert Fristenverwaltung für unterschiedliche Dokumenttypen.

- [WEG-542 – Audit & Compliance Hooks](https://maierharry.atlassian.net/browse/WEG-542) – Protokolliert Archiv- und Löschvorgänge vollständig im Audit-System.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Automatische Sperrung nach Periodenabschluss, Retention-Überwachung durch Scheduler, Audit-Logging und Sperrstatus-Anzeige im DMS.

**Phase 2**

Compliance-Reporting, manuelle Verlängerung von Fristen, erweiterte Policies pro Dokumententyp.

**Phase 3**

Dynamische Retention-Policies, Cloud-Archivintegration und Self-Service-Archivzugriff für Eigentümer:innen.