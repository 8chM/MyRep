---
title: WEG-14 – Testing & CI Basics
confluence_id: 27853408
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27853408/WEG-14+Testing+CI+Basics
---

**JIRA-Link:** [WEG-14 – Testing & CI Basics](https://maierharry.atlassian.net/browse/WEG-14)

## Überblick

Das Modul **Testing & CI Basics** (WEG-14) definiert die Grundprinzipien für Qualitätssicherung und kontinuierliche Integration im gesamten WEG Management System.

Es sorgt dafür, dass alle zentralen Funktionen automatisiert getestet, Änderungen überprüft und Builds nur nach erfolgreicher Validierung freigegeben werden.

Ziel ist eine stabile, reproduzierbare und überprüfbare Codebasis, die kontinuierlich in hoher Qualität ausgeliefert werden kann.

## Beschreibung

WEG-14 legt das Fundament für alle zukünftigen Test- und Qualitätssicherungsmaßnahmen.

Es implementiert eine automatisierte CI-Pipeline, die sämtliche Komponenten (Backend, Frontend, API-Client) auf Konsistenz und Funktionsfähigkeit prüft.

Das Modul stellt sicher, dass jede Änderung nachvollziehbar getestet und dokumentiert wird.

Hauptfunktionen:

- **xUnit Test Framework:** Einrichtung einer einheitlichen Testumgebung für Unit- und Integrationstests mit Fixture-Unterstützung.

- **Playwright Smoke Tests:** Durchführung einfacher UI-Tests, die die Kernfunktionen wie Login, Navigation und Sprachumschaltung abdecken.

- **Seed Fixtures & Test Data:** Bereitstellung reproduzierbarer Testdaten, die unabhängig voneinander funktionieren und für jede Testumgebung automatisch erstellt werden.

- **CI/CD Pipeline Integration:** Vollautomatische Ausführung von Build, Tests, TypeScript-Client-Generierung, Linting und Formatüberprüfungen in GitHub Actions oder Azure DevOps.

- **Quality Gate:** Builds dürfen nur nach erfolgreicher Testausführung und Lint-Prüfung gemerged werden.

Diese Kombination stellt sicher, dass die Software jederzeit in einem stabilen, lauffähigen Zustand gehalten wird.

## Geschäftsregeln & Logik

- Jeder **Pull-Request** muss alle Pipeline-Schritte (Build, Tests, Linting, Client-Generierung) erfolgreich durchlaufen, bevor ein Merge erlaubt ist.

- **Smoke Tests** decken die wichtigsten UI-Szenarien ab (Login, Sprache, Dashboard-Aufruf).

- **Testdaten** werden automatisch aus Seed-Skripten erstellt und dürfen keine gegenseitigen Abhängigkeiten aufweisen.

- **Tests sind deterministisch** – keine externen oder flüchtigen Abhängigkeiten (z. B. Netzwerk, Zeit).

- **Codequalität** wird über Analysetools (Analyzer, Formatierung, Linter) erzwungen.

- **Fehlgeschlagene Tests** oder **Lint-Fehler** blockieren den Merge-Prozess.

## Akzeptanzkriterien

- **Gegeben** ein Pull-Request wird geöffnet &rarr; **Wenn** die CI-Pipeline ausgeführt wird &rarr; **Dann** müssen alle Tests, Builds und Formatprüfungen erfolgreich abgeschlossen werden, bevor ein Merge möglich ist.

- **Gegeben** der Playwright-Smoke-Test läuft &rarr; **Wenn** ein Benutzer die Login-Seite aufruft &rarr; **Dann** wird die Login-Maske korrekt dargestellt und der Benutzer kann sich anmelden.

- **Gegeben** ein Benutzer aktiviert den Sprachumschalter &rarr; **Wenn** die Sprache geändert wird &rarr; **Dann** passen sich alle UI-Elemente an und der Test bestätigt dies.

- **Gegeben** Seed-Daten werden erzeugt &rarr; **Wenn** ein Integrationstest läuft &rarr; **Dann** werden alle Abhängigkeiten automatisch initialisiert, ohne manuelles Setup.

- **Gegeben** ein Lint- oder Formatfehler wird erkannt &rarr; **Wenn** der Build ausgeführt wird &rarr; **Dann** schlägt die Pipeline fehl und weist den Entwickler auf den Fehler hin.

## Nicht-Ziele

- Keine vollständige End-to-End-Abdeckung aller Benutzerflüsse (nur Basis-Smoke-Tests im MVP).

- Keine Performance-, Last- oder Sicherheitstests in der ersten Phase.

- Keine automatische Testdatengenerierung aus Produktivsystemen.

## Kritische Fälle

- **Flaky Tests:** Instabile oder zufällige Testergebnisse müssen isoliert oder entfernt werden.

- **CI-Instabilität:** Fehler in Pipeline-Skripten dürfen keine Produktiv-Builds verhindern – Recovery-Strategien sind erforderlich.

- **Fehlerhafte Testdaten:** Seed-Daten dürfen keine anderen Tests beeinflussen oder blockieren.

- **Unvollständige Coverage:** Fehlende Tests für kritische Logikbereiche müssen durch Reviews identifiziert werden.

## Abhängigkeiten

- **WEG-10 – Solution Setup & Infrastructure:** stellt Infrastruktur und Datenbank-Container für Integrationstests bereit.

- **WEG-11 – API, OpenAPI & TypeScript Client:** wird im Rahmen der CI-Validierung generiert und getestet.

- **WEG-16 – Frontend Shell, Routing & Access Guard:** dient als Ziel für die UI-Smoke-Tests.

- **WEG-12 – Error Handling, Logging & Health:** Logging-Validierung für Testfälle.

## Offene Fragen

- Sollen auch API-Contract-Tests im MVP enthalten sein, oder erst ab Phase 2?

- Soll die Pipeline automatisiert Coverage-Berichte (z. B. Codecov) generieren?

- Soll Playwright in Containerumgebungen (Headless Chrome) oder lokal laufen?

## Zukunftserweiterungen

- Einführung vollständiger **End-to-End-Testabdeckung** mit komplexeren Benutzerflüssen.

- **Mutation Testing** zur Ermittlung nicht getesteter Codepfade.

- **Contract-Tests** zwischen API und Frontend zur Sicherstellung der Schnittstellenstabilität.

- **Performance-Tests** zur Überwachung der Reaktionszeiten wichtiger Endpunkte.

- Automatisierte **Qualitätsmetriken und Dashboards** (Build-Zeit, Coverage, Testanzahl, Erfolgsquote).

## Verknüpfte Tasks

- **WEG-140 – xUnit Unit Tests & Integration Harness** – Implementiert Unit- und Integrationstest-Framework sowie Fixtures.

- **WEG-141 – Playwright Smoke Tests** – Führt Basis-End-to-End-Tests für Login und Sprache aus.

- **WEG-142 – Seed Fixtures & Test Data** – Erstellt reproduzierbare Testdaten für Unit- und Integrationstests.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Implementierung der CI-Pipeline, Unit- und Integrationstestframework (xUnit), Smoke-Tests mit Playwright, Seed-Funktionen und automatisierte Build-Validierung.

**Phase 2**

Erweiterte End-to-End-Abdeckung, Contract-Tests, Mutation-Testing und Coverage-Reports.

**Phase 3**

Automatisierte Qualitätsmetriken, Performance-Tests und dynamische Test-Dashboards.