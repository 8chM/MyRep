---
title: WEG-13 – Control-Plane & Connection Routing
confluence_id: 27591375
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27591375/WEG-13+Control-Plane+Connection+Routing
---

**JIRA-Link:** [WEG-13 – Control-Plane & Connection Routing](https://maierharry.atlassian.net/browse/WEG-13)

## Überblick

Das Modul **Control-Plane & Connection Routing** (WEG-13) verwaltet die Mandantenarchitektur des Systems und stellt sicher, dass Benutzeranfragen stets der richtigen Datenbank oder dem richtigen Schema zugeordnet werden.

Es ist das Herzstück der Mandantenfähigkeit und gewährleistet, dass jede WEG als eigene, logisch getrennte Einheit betrieben werden kann, ohne Datenlecks oder Fehlroutings.

## Beschreibung

WEG-13 implementiert eine zentrale **Directory-Datenbank** (Control-Plane), die Informationen über alle registrierten Associations (WEGs), deren Datenbankendpunkte und Status verwaltet.

Ein intelligenter **Connection Broker** entscheidet bei jeder Anfrage, auf welches Schema oder welche Datenbank zugegriffen wird.

Hauptfunktionen:

- **Directory-Registry:** Verwaltung aller Associations mit Status (active/inactive), Endpunkten und Metadaten.

- **Connection Broker:** Dynamische Zuordnung von Datenbankverbindungen basierend auf Benutzer- und Kontextinformationen.

- **Association Switcher:** Benutzer können zwischen mehreren WEGs wechseln; der Kontext wird automatisch aktualisiert.

- **Migration Orchestrator:** Verwaltung von Schema- und Datenbankmigrationen über mehrere Mandanten hinweg mit Dry-Run- und Health-Check-Funktion.

- **Audit-Logging:** Alle Routing-Entscheidungen und Änderungen an Endpunkten werden revisionssicher protokolliert.

Das Modul bildet die Grundlage für alle nachgelagerten Prozesse und ist Voraussetzung für Mehrmandantenbetrieb, Backups und Versionierung.

## Geschäftsregeln & Logik

- Jede Association muss im Directory eindeutig registriert und aktiv sein, bevor sie verwendet werden kann.

- Der Connection Broker darf nur auf aktive Endpunkte routen; inaktive Associations führen zu Fehlermeldungen.

- Änderungen an Endpunkten müssen über Health-Checks validiert und im Audit-Log dokumentiert werden.

- Ein Benutzer darf den Association Switcher nur verwenden, wenn er entsprechende Berechtigungen besitzt.

- Beim Wechsel der Association wird die aktive Kontext-ID gesetzt, sodass alle nachfolgenden Requests diesem Kontext folgen.

- Migrationen dürfen niemals simultan für denselben Endpunkt ausgeführt werden.

## Akzeptanzkriterien

- **Gegeben** ein Benutzer ist in Association A angemeldet &rarr; **Wenn** er zur Association B wechselt &rarr; **Dann** leitet der Connection Broker alle nachfolgenden Anfragen korrekt zu Schema B.

- **Gegeben** ein Datenbankendpunkt wird geändert &rarr; **Wenn** der neue Endpunkt aktiviert wird &rarr; **Dann** werden alle Anfragen dorthin geroutet und die Änderung im Audit-Log vermerkt.

- **Gegeben** eine Association ist als &bdquo;inactive&ldquo; markiert &rarr; **Wenn** ein Benutzer versucht, sie zu verwenden &rarr; **Dann** verweigert das System den Zugriff mit einer klaren Fehlermeldung.

- **Gegeben** eine Migration wird gestartet &rarr; **Wenn** der Orchestrator den Health-Check durchführt &rarr; **Dann** darf die Migration nur bei fehlerfreier Prüfung fortgesetzt werden.

- **Gegeben** der Connection Broker fällt aus &rarr; **Wenn** eine Anfrage eingeht &rarr; **Dann** erzeugt das System einen kontrollierten Fehler und bleibt stabil.

## Nicht-Ziele

- Keine Cross-Tenant-Abfragen oder Datenzusammenführungen über mehrere WEGs hinweg.

- Kein automatisches Failover zwischen Datenbankendpunkten im MVP.

- Keine dynamische Skalierung oder Sharding-Mechanismen (später geplant).

## Kritische Fälle

- **Falsches Routing:** Fehlerhafte Zuordnungen können zu Datenschutzverletzungen führen – jede Routing-Entscheidung muss nachvollziehbar sein.

- **Endpunkt-Ausfall:** Bei Verbindungsverlust darf kein undefinierter Zustand entstehen; das System muss sauber abbrechen.

- **Fehlerhafte Migration:** Abgebrochene Migrationen müssen automatisch rücksetzbar sein.

- **Deadlocks:** Gleichzeitige Migrationsprozesse dürfen sich nicht gegenseitig blockieren.

## Abhängigkeiten

- **WEG-10 – Solution Setup & Infrastructure:** Basisinfrastruktur für Directory-DB und Routing-Services.

- **WEG-12 – Error Handling, Logging & Health:** Einheitliche Logging- und Health-Mechanismen.

- **WEG-14 – Testing & CI Basics:** Testautomatisierung für Routing- und Migrationsszenarien.

- **WEG-3 – Tenant Provisioning & Administration:** Nutzung der Registry-Einträge für neue Associations.

## Offene Fragen

- Soll ein sekundärer Failover-Endpunkt je Association unterstützt werden?

- Wie soll das System bei Live-Migrations während aktiver Nutzung reagieren (Session Lock oder Graceful Switch)?

- Sollen inaktive WEGs automatisch archiviert oder exportiert werden?

## Zukunftserweiterungen

- **Blue/Green-Swaps & Zero-Downtime-Migrationen:** Endpunkte können im laufenden Betrieb gewechselt werden.

- **Failover-Mechanismen:** Automatische Umschaltung bei Endpunkt-Ausfällen.

- **Self-Service-Portale:** Administratoren können Associations selbst verwalten und Endpunkte pflegen.

- **Automatisierte Health-Matrix:** Zentrale Übersicht über alle Datenbankverbindungen und Migrationszustände.

## Verknüpfte Tasks

- **WEG-130 – Directory DB** – Implementiert Registry, Endpunkte und Mitgliedschaften.

- **WEG-131 – Connection Broker** – Verantwortlich für dynamisches Routing basierend auf Benutzerkontext.

- **WEG-132 – Association Switcher UI** – Ermöglicht Benutzern den Kontextwechsel zwischen Associations.

- **WEG-133 – Migration Orchestrator CLI** – Verwaltung von Multi-Schema-Migrationen inkl. Dry-Run.

- **WEG-134 – Migration Runbook & Health Matrix** – Dokumentation und Validierung von Migrationsprozessen.

- **WEG-135 – Directory Audit Logging** – Audit-Trail für alle Verzeichnisänderungen.

- **WEG-136 – Schema Teardown Tool** – Entwicklerwerkzeug zur Entfernung von Schemas im Dev-Modus.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Directory-Registry, Connection Broker, Association Switcher, Migration Orchestrator mit Runbooks, Health-Checks und Audit-Logs.

**Phase 2**

Blue/Green-Swaps, Zero-Downtime-Migrationen und automatisierte Failover-Strategien.

**Phase 3**

Self-Service-Portale für Association-Management, Monitoring-Dashboards und automatisierte Recovery-Mechanismen.