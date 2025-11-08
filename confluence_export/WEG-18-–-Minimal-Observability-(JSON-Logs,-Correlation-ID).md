---
title: WEG-18 – Minimal Observability (JSON Logs, Correlation-ID)
confluence_id: 27459990
version: 18
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27459990/WEG-18+Minimal+Observability+JSON+Logs+Correlation-ID
---

**JIRA-Link:** [WEG-18 – Minimal Observability (JSON Logs, Correlation-ID)](https://maierharry.atlassian.net/browse/WEG-18)

## Überblick
Das Modul **Minimal Observability** (WEG-18) stellt die grundlegenden Mechanismen für Transparenz und Nachvollziehbarkeit im WEG-System bereit.

Es sorgt für strukturierte, maschinenlesbare Logs und grundlegende Metriken, um Systemzustände, Fehler und Performance-Daten zu überwachen.

Ziel ist es, Entwicklern und Administratoren eine einfache, lokale Möglichkeit zu bieten, den Systemzustand und Fehlersituationen zu analysieren, ohne komplexe externe Monitoring-Systeme einzusetzen.

## Beschreibung
WEG-18 baut auf der Logging-Infrastruktur von **WEG-12** auf und erweitert diese um kontextbasierte Metriken und Korrelation zwischen Anfragen.

Jeder Request erhält eine eindeutige **x-request-id**, mit der alle zugehörigen Logs verbunden werden.

Neben der reinen Fehlerprotokollierung werden einfache Leistungskennzahlen (z. B. Antwortzeiten, Fehlerraten) erhoben, um erste Indikatoren zur Systemgesundheit zu liefern.

Hauptfunktionen:

- **Strukturierte Logs:** Ausgabe im JSON-Format mit Zeitstempel, Schweregrad, Benutzer- und Association-Kontext.

- **Correlation-ID (x-request-id):** Einheitliche Kennung pro Request für durchgehende Nachverfolgbarkeit.

- **Grundlegende Metriken:** Messung von Request-Dauer, Fehlerrate, Ausführungszeit und Auslastung.

- **Health-Indikatoren:** Einfache lokale Abfragepunkte, um Laufzeit- und Fehlerstatus zu prüfen.

- **Entwickler-How-To:** Dokumentation und Beispiele zur Interpretation von Logs und Metriken.

- **Log-Enrichment:** Erweiterung der Logs um Benutzer-, Tenant- und Schema-Informationen (Integration mit WEG-12 und WEG-3).

## Geschäftsregeln & Logik
- Jeder eingehende Request erhält zwingend eine **x-request-id**, die für alle internen Logs und Subprozesse gilt.

- Logs dürfen keine personenbezogenen oder sensiblen Daten enthalten (Filterungspflicht).

- Fehlerhafte oder unvollständige Logs müssen automatisch als Warnung markiert werden.

- Metriken werden nur lokal aggregiert und nicht an externe Systeme übertragen.

- Nur Benutzer mit Administrator- oder Entwicklerrechten dürfen auf Metrik- oder Log-Daten zugreifen.

- Performance-Warnungen (z. B. Response > 5 Sekunden) werden automatisch protokolliert.

## Akzeptanzkriterien
- **Gegeben:** ein API-Request wird verarbeitet &rarr; **Wenn:** Logs erzeugt werden &rarr; **Dann:** enthalten alle Einträge dieselbe x-request-id.

- **Gegeben:** ein Fehler tritt auf &rarr; **Wenn:** der Log geschrieben wird &rarr; **Dann:** enthält er Stack-Trace, Benutzerkontext und Schweregrad.

- **Gegeben:** ein Request dauert länger als 5 Sekunden &rarr; **Wenn:** er abgeschlossen ist &rarr; **Dann:** wird eine Warnung mit Metrikdaten im Log vermerkt.

- **Gegeben:** ein Administrator ruft die Health-Metriken ab &rarr; **Wenn:** das System läuft &rarr; **Dann:** werden Antwortzeit, Fehlerrate und Status angezeigt.

- **Gegeben:** eine Log-Datei enthält sensible Daten &rarr; **Wenn:** ein Filter aktiv ist &rarr; **Dann:** werden diese automatisch maskiert oder entfernt.

## Nicht-Ziele
- Keine Integration in externe Monitoring- oder Dashboard-Lösungen im MVP.

- Kein Distributed Tracing oder Event-Streaming (OpenTelemetry erst ab Phase 2).

- Kein Alerting-System oder Echtzeit-Benachrichtigung bei Fehlern im MVP.

## Kritische Fälle
- **Fehlende Correlation-ID:** Ohne x-request-id kann ein Request nicht nachverfolgt werden – Log wird als unvollständig markiert.

- **Datenlecks in Logs:** Ungefilterte personenbezogene Daten dürfen nicht im Klartext erscheinen.

- **Log-Overload:** Übermäßige Log-Mengen können Speicher und Performance beeinträchtigen – Log-Level-Regeln notwendig.

- **Fehlende Metrikgrenzen:** Wenn keine Limits definiert sind, können Messwerte verfälscht oder unvollständig sein.

## Abhängigkeiten
- WEG-12 – Error Handling, Logging & Health – Basis-Logging und Health-Endpoints.

- WEG-11 – API, OpenAPI & TypeScript Client – Übergibt x-request-id an alle API-Aufrufe.

- WEG-3 – Tenant Provisioning & Administration (Associations as Schemas) – Liefert Tenant- und Schema-Kontext für Logs.

## Offene Fragen
- Sollen einfache Metriken (z. B. Ladezeit, Request-Anzahl) auch im Frontend erhoben werden?

- Wie lange sollen Logs lokal gespeichert bleiben, bevor sie automatisch gelöscht werden?

- Soll ein minimales UI-Dashboard für Metriken und Logs im Browser enthalten sein?

## Zukunftserweiterungen
- Integration in externe Monitoring-Systeme (Prometheus, Grafana).

- Einführung von **Distributed Tracing** mit OpenTelemetry.

- **Alerting-Mechanismen** für Performance-Grenzen und Fehler.

- Erweiterte Log-Analyse über Dashboards und Filterfunktionen.

## Verknüpfte Tasks
- [WEG-180 – Serilog JSON Logs](https://maierharry.atlassian.net/browse/WEG-180) – Implementiert strukturierte Log-Ausgabe.

- [WEG-181 – Correlation-ID Middleware](https://maierharry.atlassian.net/browse/WEG-181) – Fügt jedem Request eine eindeutige Kennung hinzu.

- [WEG-182 – Log Enricher (User, Association, Schema)](https://maierharry.atlassian.net/browse/WEG-182) – Ergänzt Logs mit Kontextdaten.

- [WEG-183 – Basic Metrics (Request Duration, Error Rate)](https://maierharry.atlassian.net/browse/WEG-183) – Führt lokale Metriken zur Performance-Messung ein.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Strukturierte JSON-Logs, Correlation-ID, Basis-Metriken (Response-Time, Error-Rate), Developer-How-To.

**Phase 2**

Integration in Observability-Stacks (Prometheus, Grafana), Distributed Tracing mit OpenTelemetry.

**Phase 3**

Vollständiges Monitoring-System mit Alerting, erweiterten Dashboards und automatischen Fehleranalysen.