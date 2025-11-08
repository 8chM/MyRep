---
title: WEG-10 – Solution Setup & Infrastructure
confluence_id: 28082893
version: 12
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/28082893/WEG-10+Solution+Setup+Infrastructure
---

**JIRA-Link:** [WEG-10 – Solution Setup & Infrastructure](https://maierharry.atlassian.net/browse/WEG-10)

## Überblick

Das Modul **Solution Setup & Infrastructure** (WEG-10) bildet die technische Grundlage für die gesamte WEG-Plattform.
Es definiert die Struktur des Projekts, stellt die lokale Entwicklungsumgebung bereit und sorgt für eine einheitliche Konfigurationsvalidierung.
Ziel ist es, ein konsistentes, wartbares und leicht aufsetzbares Framework für Entwickler zu schaffen, das sowohl lokal als auch in CI/CD-Pipelines stabil funktioniert.

## Beschreibung

WEG-10 etabliert eine standardisierte **Projektarchitektur** und eine reproduzierbare **Entwicklungsumgebung**, die alle Kernkomponenten umfasst: API, Datenbank, Directory-Service und Web-Frontend.
Alle Umgebungen – lokal, test und staging – basieren auf derselben Containerstruktur, um Fehlerquellen zu minimieren und Setup-Zeiten zu verkürzen.

Hauptfunktionen:

- **Solution-Setup:** Klare Strukturierung nach Domain-Driven Design (DDD) mit Projekten für Api, Application, Domain, Infrastructure und Directory.

- **Docker Compose Infrastructure:** Einheitliche Containerdefinitionen für SQL Server, Directory und Web-Client, startbar mit einem Befehl (docker compose up).

- **Developer Onboarding:** Ausführliches README mit Installationsanleitung, Troubleshooting und Standardbefehlen.

- **Configuration Validation:** Validierung aller Konfigurationsparameter über das .NET Options Pattern; ungültige Werte stoppen den Startvorgang (Fail-Fast).

- **CI-Integration:** Build-Validierung, Docker-Linting und Pipeline-Setup zur automatischen Prüfung auf Konsistenz.

Diese Basis ist die Voraussetzung für alle weiteren Module, insbesondere WEG-1 (Platform Foundation) und WEG-12 (Logging & Health), die direkt auf die hier definierten Standards aufbauen.

## Geschäftsregeln & Logik

- Das gesamte Projekt verwendet eine **einheitliche Ordner- und Namensstruktur**, die im Repository-Standard dokumentiert ist.

- **Docker Compose** ist die einzige Quelle für lokale Infrastrukturdefinitionen; Änderungen müssen versioniert und dokumentiert werden.

- **Konfigurationsfehler** (z. B. fehlende ENV-Variablen) führen zu sofortigem Abbruch des Startvorgangs.

- Alle **Builds** werden über CI validiert, bevor neue Branches gemergt werden dürfen.

- Entwickler dürfen keine Daten direkt in Datenbanken einspielen – ausschließlich über definierte Migrationen oder Seeder.

- Die Umgebung muss innerhalb von 5 Minuten vollständig startbereit sein.

## Akzeptanzkriterien

- **Gegeben:** ein Entwickler klont das Repository &rarr; **Wenn:** er docker compose up mit gültigen .env-Dateien ausführt &rarr; **Dann:** starten API, SQL, Directory und Web-Client fehlerfrei und sind erreichbar.

- **Gegeben:** eine fehlerhafte oder fehlende Umgebungsvariable &rarr; **Wenn:** der Dienst startet &rarr; **Dann:** wird der Startvorgang gestoppt und eine verständliche Fehlermeldung ausgegeben.

- **Gegeben:** ein neuer Entwickler folgt dem README &rarr; **Wenn:** er die beschriebenen Schritte ausführt &rarr; **Dann:** kann er die Anwendung lokal ausführen und erste API-Aufrufe tätigen.

- **Gegeben:** eine CI-Pipeline wird ausgelöst &rarr; **Wenn:** der Build ausgeführt wird &rarr; **Dann:** werden Compose-Dateien, ENV-Parameter und Build-Artefakte validiert.

## Nicht-Ziele

- Keine Bereitstellung oder Konfiguration von Cloud- oder Produktionsumgebungen.

- Kein Load-Balancing oder automatisches Netzwerk-Routing.

- Keine End-to-End-Tests (werden in WEG-14 umgesetzt).

- Kein Secret- oder Credential-Management im MVP.

## Kritische Fälle

- **Port-Kollisionen:** Lokale Ports dürfen nicht mehrfach belegt sein – Troubleshooting wird im README dokumentiert.

- **Fehlende Docker-Komponenten:** Wenn Docker Desktop oder Compose fehlt, bricht das Setup mit verständlicher Fehlermeldung ab.

- **ENV-Fehler:** Falsche oder fehlende Variablen blockieren den Start – Fehlerhinweis muss den Namen der fehlenden Variable nennen.

- **Nicht kompatible Versionen:** Docker-Images müssen versioniert werden, um Reproduzierbarkeit sicherzustellen.

## Abhängigkeiten

- WEG-1 – Platform Foundation nutzt die Projektstruktur und ENV-Definitionen von WEG-10.

- WEG-12 – Error Handling, Logging & Health integriert Health Checks und Logging, die auf der Basis-Infrastruktur von WEG-10 laufen.

- WEG-14 – Testing & CI Basics verwendet Build- und Pipeline-Definitionen aus WEG-10.

- Alle weiteren Module (WEG-2 bis WEG-9) erfordern die Infrastruktur und das Setup aus diesem Modul.

## Offene Fragen

- Soll in späteren Phasen ein Devcontainer (z. B. für GitHub Codespaces) integriert werden, um lokale Installationen zu vermeiden?

- Soll eine automatische Prüfroutine (z. B. make check-env) ENV-Dateien validieren, bevor docker compose up ausgeführt wird?

- Soll die lokale SQL-Datenbank automatisch mit Demodaten befüllt werden?

## Zukunftserweiterungen

- **Feature:** Infrastructure-as-Code (IaC) – Bereitstellung automatisierter Templates (Terraform/Bicep) für Staging-Umgebungen.

- **Feature:** Secrets-Management – Integration von Azure Key Vault oder HashiCorp Vault.

- **Feature:** Advanced Monitoring – Ergänzung durch Application Insights oder Prometheus zur Laufzeitüberwachung.

- **Feature:** Container Optimization – Multi-Stage-Builds für kleinere Images und schnellere Deployments.

## Verknüpfte Tasks

- [WEG-100 – Solution Setup & Project Structure](https://maierharry.atlassian.net/browse/WEG-100) – Erstellt die Projektstruktur mit Api, Application, Domain, Infrastructure und Directory.

- [WEG-101 – Docker Compose Infrastructure](https://maierharry.atlassian.net/browse/WEG-101) – Implementiert lokale Containerdefinitionen für API, SQL und Web.

- [WEG-102 – Developer Onboarding & Documentation](https://maierharry.atlassian.net/browse/WEG-102) – Erstellt das README mit Setup- und Troubleshooting-Anleitungen.

- [WEG-103 – Configuration Validation & Options Pattern](https://maierharry.atlassian.net/browse/WEG-103) – Validiert ENV-Variablen und Konfigurationsparameter beim Start.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Grundsetup für Solution-Struktur, Docker Compose, ENV-Validierung und Onboarding-Dokumentation.

**Phase 2**

Integration von IaC-Templates, erweiterten CLI-Tools und Devcontainer-Unterstützung.

**Phase 3**

Secrets-Management, Advanced Monitoring, automatisierte Provisionierung von Testumgebungen.