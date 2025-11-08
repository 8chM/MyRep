---
title: WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite)
confluence_id: 27165364
version: 23
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27165364/WEG-1+Platform+Foundation+.NET+8+SQL+Server+React+Vite
---

**JIRA-Link:** [WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite)](https://maierharry.atlassian.net/browse/WEG-1)

## Beschreibung / Kernzweck

Das Modul **WEG-1 – Platform Foundation** bildet das technische Fundament des gesamten WEG Management Systems (WMS).   Es legt die Grundarchitektur fest, strukturiert die Software in klar abgegrenzte Schichten und sorgt für eine reproduzierbare Entwicklungs- und Betriebsumgebung.   Ziel ist eine stabile, modulare Plattform, auf der alle weiteren Systemkomponenten aufbauen und die zentrale Querschnittsfunktionen wie Logging, Scheduler, Mehrsprachigkeit und Konfiguration bereitstellt.  

Darüber hinaus gewährleistet WEG-1 die Konsistenz aller Module durch standardisierte Schnittstellen, Versionierung, Health-Checks und einheitliche Projektkonventionen.   Es dient als Bindeglied zwischen Entwicklung, Infrastruktur und Produktlogik und stellt sicher, dass jede neue Funktion in eine kontrollierte, skalierbare Umgebung integriert werden kann.

## Inhalte

Untermodul

Kurzbeschreibung

[WEG-10 – Solution Setup & Infrastructure](https://maierharry.atlassian.net/wiki/pages/28082893)

Erstellt das Projektgerüst, die Schichtenstruktur (API, Application, Domain, Infrastructure) und Docker-Compose-Umgebung für API, Datenbank und Web-App.

[WEG-11 – API, OpenAPI & TypeScript Client](https://maierharry.atlassian.net/wiki/pages/27165380)

Definiert API-Versionierung, erzeugt eine OpenAPI-Spezifikation und generiert typisierte TypeScript-Clients.

[WEG-12 – Error Handling, Logging & Health](https://maierharry.atlassian.net/wiki/pages/27329245)

Implementiert eine einheitliche Fehlerbehandlung (ProblemDetails), strukturiertes Logging, Health-Checks und den Basis-Scheduler.

[WEG-13 – Control-Plane & Connection Routing](https://maierharry.atlassian.net/wiki/pages/27591375)

Stellt die Mandanten-Registry bereit und steuert dynamisch die Verbindung zu den jeweiligen Datenbankschemas.

[WEG-14 – Testing & CI Basics](https://maierharry.atlassian.net/wiki/pages/27853408)

Definiert Mindestanforderungen für Unit-, Integrations- und End-to-End-Tests sowie CI-Pipelines.

[WEG-15 – Internationalization (EN/DE) Foundation](https://maierharry.atlassian.net/wiki/pages/27853423)

Schafft die Grundlage für Mehrsprachigkeit, Übersetzungskataloge und Datums-/Zahlen-Lokalisierung.

[WEG-16 – Frontend Shell, Routing & Access Guard](https://maierharry.atlassian.net/wiki/pages/27459975)

Liefert das UI-Grundgerüst, Layout, Navigation und rollenbasiertes Routing für geschützte Bereiche.

[WEG-17 – Configuration & Feature Flags (Base)](https://maierharry.atlassian.net/wiki/pages/27591390)

Vereinheitlicht Konfiguration und Feature-Verwaltung, um Funktionen mandanten- oder systemweit zu steuern.

[WEG-18 – Minimal Observability (JSON Logs, Correlation-ID)](https://maierharry.atlassian.net/wiki/pages/27459990)

Bietet grundlegendes Monitoring mit strukturierten Logs und Basis-Metriken zur Systembeobachtung.

[WEG-19 – Naming Conventions & ADRs (English-first)](https://maierharry.atlassian.net/wiki/pages/28082908)

Legt Namenskonventionen für Code, Datenbank und API fest und etabliert dokumentierte Architekturentscheidungen (ADRs).

## Geschäftslogik

WEG-1 definiert, wie das System technisch aufgebaut und betrieben wird:

- **Projektstruktur & Infrastruktur:** Das System ist in getrennte Schichten (API, Application, Domain, Infrastructure) gegliedert und wird über Docker Compose gestartet. Entwickler erhalten so mit einem Befehl (`docker compose up`) eine lauffähige Umgebung mit API, Datenbank und Web-App.

- **API-Versionierung & Integration:** Alle Schnittstellen sind versioniert (`/api/v1`). Die OpenAPI-Spezifikation wird automatisch generiert, daraus entsteht ein typisierter TypeScript-Client für das Frontend.

- **Fehlerbehandlung & Logging:** Fehler werden als standardisierte `ProblemDetails` zurückgegeben. Serilog schreibt strukturierte JSON-Logs mit `x-request-id`-Korrelation, sodass Anfragen rückverfolgbar sind.

- **Health-Checks & Scheduler:** Die Endpunkte `/healthz` und `/readyz` prüfen den Systemzustand. Ein persistenter Scheduler führt wiederkehrende Aufgaben aus (z. B. Erinnerungen, Prüfungen) und protokolliert Ergebnisse.

- **Mandanten-Routing:** Über die Control-Plane (WEG-13) werden Anfragen dynamisch auf das richtige Datenbankschema geroutet. Dadurch bleibt jede WEG logisch und technisch isoliert.

- **Mehrsprachigkeit, Feature-Flags und Konfiguration:** Das System ist standardmäßig in Deutsch und Englisch verfügbar. Funktionen lassen sich über Feature-Flags aktivieren oder deaktivieren. Konfigurationen werden zentral validiert (Fail-Fast-Prinzip).

- **CI/CD und Testing:** Eine einheitliche Pipeline sorgt für Build, Tests und Code-Qualität. Architekturentscheidungen (ADRs) dokumentieren Änderungen nachvollziehbar über den gesamten Lebenszyklus.

## Akzeptanzkriterien

- **Gegeben** ein neu geklontes Repository &rarr; **Wenn** ein Entwickler `docker compose up` ausführt &rarr; **Dann** startet das System vollständig (API, SQL-Server, Directory, Web-App) ohne Fehlermeldung.  

- **Gegeben** das System läuft &rarr; **Wenn** `/api/v1/swagger.json` aufgerufen wird &rarr; **Dann** liefert der Server eine gültige OpenAPI-Spezifikation und der TypeScript-Client kann generiert werden.  

- **Gegeben** eine unbehandelte Exception &rarr; **Wenn** sie im API-Layer auftritt &rarr; **Dann** antwortet die API mit einem `ProblemDetails`-Objekt und korrelierter Trace-ID.  

- **Gegeben** `/readyz` wird aufgerufen &rarr; **Wenn** eine Abhängigkeit (z. B. Datenbank) nicht erreichbar ist &rarr; **Dann** zeigt der Endpunkt den Fehlerstatus korrekt an.  

- **Gegeben** ein Scheduler-Job &rarr; **Wenn** der Cron-Ausdruck auslöst &rarr; **Dann** wird der Job ausgeführt, im Log dokumentiert und ggf. erneut geplant.  

- **Gegeben** eine CI-Pipeline &rarr; **Wenn** ein Pull-Request erstellt wird &rarr; **Dann** werden Build, Tests, Client-Generierung und Linting erfolgreich abgeschlossen, bevor gemerged werden darf.

## Nicht-Ziele

- Keine Verwaltung oder Bereitstellung von Cloud-Infrastruktur (Deployment-Ebene außerhalb des MVP-Scopes).

- Kein Echtzeit-Monitoring mit externen Tools (z. B. Prometheus, Grafana) im MVP.

- Keine Feature-Flags pro Benutzer (nur global oder mandantenbezogen).

- Keine alternativen API-Protokolle (gRPC, GraphQL) im MVP.

## Kritische Fälle

- **Fehlende Konfiguration:** Ungültige `.env`-Einträge verhindern den Start; das System muss mit klarer Fehlermeldung abbrechen.

- **Migrationen:** Fehlerhafte Migrationen dürfen keine halbfertigen Schemas hinterlassen; Transaktionen und Rollback sind zwingend.

- **Scheduler-Fehler:** Wiederkehrende Jobs dürfen nicht hängen bleiben; es muss ein Retry-Mechanismus bestehen.

- **Routing-Fehler:** Falsche Mandantenzuordnung führt zu Datenverwechslung; Control-Plane muss deterministisch arbeiten.

## Abhängigkeiten

Dieses Hauptmodul hängt von folgenden Untermodule und Systemkomponenten ab:

- WEG-10 – Solution Setup & Infrastructure: Grundlegende Projektstruktur und Docker-Umgebung.

- WEG-11 – API, OpenAPI & TypeScript Client: Bereitstellung typisierter Schnittstellen für Frontend-Integration.

- WEG-12 – Error Handling, Logging & Health: Zentrale Fehlerbehandlung, Logging und Scheduler-Funktion.

- WEG-13 – Control-Plane & Connection Routing: Mandanten-Routing und Datenbankverwaltung.

- WEG-14 – Testing & CI Basics: Sicherung der Code-Qualität und automatisierte Tests.

- WEG-15 – Internationalization (EN/DE) Foundation: Mehrsprachige Benutzeroberfläche.

- WEG-16 – Frontend Shell, Routing & Access Guard: UI-Grundstruktur und Zugriffsschutz.

- WEG-17 – Configuration & Feature Flags (Base): Konfigurations- und Funktionssteuerung.

- WEG-18 – Minimal Observability (JSON Logs, Correlation-ID): Monitoring-Grundlage für Logs und Metriken.

- WEG-19 – Naming Conventions & ADRs (English-first): Einheitliche Namens- und Entscheidungsrichtlinien.

## Offene Fragen

- Wann erfolgt die Umstellung von lokaler Docker-Compose-Entwicklung auf Cloud-Betrieb?

- Wie detailliert sollen ADRs (Architecture Decision Records) geführt werden?

- Sollen Feature-Flags künftig pro Mandant konfigurierbar sein?

## Zukunftserweiterungen

- **Automatisierte Cloud-Deployments:** Integration von CI/CD-Pipelines für produktive Umgebungen.

- **Observability-Stack:** Erweiterung um OpenTelemetry, Prometheus und Dashboards.

- **Feingranulare Feature-Flags:** Steuerung pro Nutzer, Rolle oder Association.

- **Alternative APIs:** Ergänzung von GraphQL oder gRPC für Integrationspartner.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Plattformgrundlage mit Docker-Compose, versionierter REST-API (`/api/v1`), zentralem Logging, Health-Checks, Scheduler, Mehrsprachigkeit (DE/EN), Frontend-Shell und Basis-Konfiguration.

**Phase 2**

Automatisierte Cloud-Deployments, Observability-Stack, erweiterte Feature-Flags (pro Mandant), Self-Service-Provisionierung und Blue/Green-Deployments.

**Phase 3**

Intelligente Plattform mit KI-gestütztem Monitoring, GraphQL/gRPC-APIs, A/B-Testing und automatisierter Validierung von ADR- und Naming-Konventionen.