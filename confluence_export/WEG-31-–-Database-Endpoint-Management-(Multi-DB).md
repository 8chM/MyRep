---
title: WEG-31 – Database Endpoint Management (Multi-DB)
confluence_id: 27329268
version: 14
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329268/WEG-31+Database+Endpoint+Management+Multi-DB
---

**JIRA-Link:** [WEG-31 – Database Endpoint Management (Multi-DB)](https://maierharry.atlassian.net/browse/WEG-31)

## Überblick

Das Modul **Database Endpoint Management** (WEG-31) verwaltet die physische Datenbankinfrastruktur, auf der die einzelnen WEG-Schemata betrieben werden.

Es speichert und überwacht alle verfügbaren Datenbankserver (Endpoints), deren Kapazitäten, Status und Zuweisungen, um sicherzustellen, dass jede neue Association (Mandant) auf einem optimalen Endpunkt provisioniert wird.

Ziel ist eine stabile, performante und nachvollziehbare Zuordnung von Schemata zu Endpunkten innerhalb der Multi-DB-Architektur.

## Beschreibung

WEG-31 stellt die logische Verwaltungs- und Überwachungsschicht für alle Datenbank-Endpunkte bereit, die in der mandantenfähigen Architektur eingesetzt werden.

Das Modul interagiert mit der **Directory-Datenbank (WEG-13)**, die alle Metadaten zu Endpunkten und deren Zuordnungen verwaltet, und unterstützt das **Provisioning-Modul (WEG-30)** bei der Anlage neuer Schemata.

Hauptfunktionen:

- **Endpoint-Registry:** Verwaltung aller Datenbank-Endpunkte mit Hostname, Kapazität, Status, Umgebung (Prod/Test) und zugewiesenen Mandanten.

- **Endpoint-Auswahl:** Automatische Auswahl des am besten geeigneten Endpunkts für neue Schemata basierend auf definierter Kapazität und Auslastung.

- **Health Monitoring:** Regelmäßige Prüfung der Erreichbarkeit und Performance der Endpunkte. Offline-Endpunkte werden automatisch deaktiviert.

- **Capacity Thresholds:** Jeder Endpunkt besitzt vordefinierte Schwellenwerte (max. Schemata, Speichergröße, Last). Wird der Grenzwert überschritten, erfolgt keine weitere Zuweisung.

- **Failover-Mechanismus:** Bei Ausfall eines Endpunkts wird dieser blockiert und die betroffenen Schemata werden in der Directory-Datenbank markiert.

- **Audit-Logging:** Alle Änderungen an Endpunktkonfigurationen und Zuweisungen werden in WEG-24 (Audit Log) dokumentiert.

## Geschäftsregeln & Logik

- Jeder Endpunkt darf nur so viele Schemata enthalten, wie in der Kapazitätskonfiguration erlaubt.

- Endpunkte mit dem Status *Offline* dürfen für keine neuen Provisionierungen verwendet werden.

- Das System priorisiert Endpunkte mit niedrigster Auslastung, kann aber durch Prioritätsstufen (z. B. Prod, Test, Dev) beeinflusst werden.

- Änderungen an Endpunkten (z. B. neue Limits oder Statuswechsel) werden sofort aktiv, erfordern keinen Neustart.

- Der Auswahlprozess ist deterministisch – identische Eingaben führen immer zum selben Endpunkt.

## Akzeptanzkriterien

- **Gegeben** ein neuer Tenant soll angelegt werden &rarr; **Wenn** mehrere Endpunkte verfügbar sind &rarr; **Dann** wird automatisch der mit der höchsten verfügbaren Kapazität gewählt.

- **Gegeben** ein Endpunkt befindet sich im Status &bdquo;Offline&ldquo; &rarr; **Wenn** ein Tenant-Provisioning gestartet wird &rarr; **Dann** wird dieser Endpunkt übersprungen und nicht verwendet.

- **Gegeben** ein Endpunkt erreicht seine Kapazitätsgrenze &rarr; **Wenn** ein weiterer Tenant angelegt wird &rarr; **Dann** erfolgt eine automatische Auswahl eines anderen verfügbaren Endpunkts.

- **Gegeben** ein Administrator deaktiviert einen Endpunkt &rarr; **Wenn** der Status gespeichert wird &rarr; **Dann** werden keine neuen Schemata diesem Endpunkt zugewiesen.

- **Gegeben** ein Endpunkt fällt während einer Provisionierung aus &rarr; **Wenn** der Health Check dies erkennt &rarr; **Dann** wird der Prozess abgebrochen und ein Rollback eingeleitet.

## Nicht-Ziele

- Keine automatische horizontale Skalierung (z. B. automatisches Hinzufügen neuer Endpunkte) im MVP.

- Keine automatische Migration bestehender Schemata zwischen Endpunkten.

- Kein Cloud-native Load-Balancing im MVP (nur manuelle Auswahl und Konfiguration).

## Kritische Fälle

- **Endpoint-Ausfall:** Muss sofort erkannt werden, damit keine Verbindungen zu inaktiven Endpunkten aufgebaut werden.

- **Kapazitätsfehler:** Falsche oder fehlende Thresholds können zu Überlastungen führen.

- **Asynchrone Statusänderungen:** Verzögerte Health-Check-Ergebnisse könnten fehlerhafte Routingentscheidungen auslösen.

- **Manuelle Fehleingaben:** Falsch konfigurierte Endpunktparameter müssen durch Validierungsregeln verhindert werden.

## Abhängigkeiten

-  – Nutzt Endpunktinformationen für das automatische Schema-Provisioning.

-  – Greift auf die Directory-Datenbank zu, um Routinginformationen zu lesen und zu aktualisieren.

-  – Protokolliert Endpunktfehler, Timeout-Ereignisse und Health-Check-Fehler.

-  – Dokumentiert Änderungen an Endpunkten und Statusübergängen.

## Offene Fragen

- Sollen Kapazitätsgrenzen dynamisch anhand von Speicherplatz und Performance-Metriken berechnet werden?

- Soll das System regionale Priorisierungen unterstützen (z. B. EU-Endpunkte bevorzugen)?

- Wird eine automatische Wiederherstellung deaktivierter Endpunkte nach erfolgreichem Health-Check gewünscht?

## Zukunftserweiterungen

- **Automatisches Discovery neuer Endpunkte** über Netzwerk- oder Cloud-APIs.

- **Kostenbasierte Auswahl** basierend auf Endpunktkosten und Leistung.

- **Automatische Skalierung** und Migration von Schemata zwischen Endpunkten.

- **Monitoring-Dashboard:** Übersicht über Auslastung, Status und Performance aller Endpunkte.

## Verknüpfte Tasks

- [WEG-310 – Endpoint CRUD](https://maierharry.atlassian.net/browse/WEG-310) – Verwaltung und Pflege von Endpunkten (Server, Datenbank, Secrets).

- [WEG-311 – Endpoint Health Check](https://maierharry.atlassian.net/browse/WEG-311) – Überwachung und Validierung der Endpunktverfügbarkeit.

- [WEG-312 – Endpoint Capacity Evaluation](https://maierharry.atlassian.net/browse/WEG-312) – Berechnung und Anpassung der verfügbaren Kapazitäten.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Verwaltung der Endpunkte (CRUD), Health-Check-Funktionalität, automatische Auswahl des optimalen Endpunkts für neue Schemata.

**Phase 2**

Automatische Erkennung neuer Endpunkte, dynamische Skalierung, Warnsysteme bei Kapazitätsengpässen.

**Phase 3**

Kostenbasierte Endpunktauswahl, geografische Priorisierung und automatisches Load-Balancing zwischen Datenbankinstanzen.