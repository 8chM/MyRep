---
title: WEG-32 – Schema Provisioning Service (Seeding)
confluence_id: 27329283
version: 14
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329283/WEG-32+Schema+Provisioning+Service+Seeding
---

**JIRA-Link:** [WEG-32 – Schema Provisioning Service (Seeding)](https://maierharry.atlassian.net/browse/WEG-32)

## Überblick

Das Modul **Schema Provisioning Service (Seeding)** (WEG-32) ist ein zentraler Bestandteil des Mandanten-Onboardings und sorgt für die Initialisierung neuer WEG-Datenbanken.

Es erstellt die technische Datenbankstruktur, legt alle erforderlichen Tabellen, Beziehungen und Systemobjekte an und füllt diese anschließend mit standardisierten Startdaten.

Ziel ist es, sicherzustellen, dass jede neu angelegte Association nach dem Provisioning über eine vollständig betriebsfähige, valide und konsistente Grundkonfiguration verfügt.

## Beschreibung

Der Seeding-Service führt den ersten Setup-Schritt nach der Schema-Erstellung (WEG-30) aus und legt die Basis für alle weiteren Module.

Das Modul verwendet ein versioniertes Seed-Framework, das sicherstellt, dass jede WEG mit der korrekten Schema-Version und den passenden Startdaten versehen wird.

Darüber hinaus ist das System erweiterbar, sodass zusätzliche Module (z. B. WEG-4, WEG-5 oder WEG-8) eigene Seeds einbringen können.

Hauptfunktionen:

- **Datenbankschema-Initialisierung:** Erstellung von Tabellen, Views, Indizes, Constraints und Systemobjekten auf Basis des Domain-Modells.

- **Seed-Daten:** Einfügen von Basisdaten wie Standardrollen (Manager, Owner, Resident), Beispielgebäude, Grundeinstellungen, Feature-Flags und Sprachvorgaben.

- **Modulare Seed-Erweiterung:** Ermöglicht Modulen wie Property & People (WEG-4) oder Finance (WEG-8), eigene Initialdaten in den Provisionierungsprozess einzubringen.

- **Versioniertes Seeding:** Sicherstellung, dass Seeds mit der jeweiligen Software- und Schema-Version übereinstimmen.

- **Idempotente Ausführung:** Wiederholte Seeds erzeugen keine Duplikate, sondern prüfen bestehende Daten vor dem Einfügen.

- **Rollback & Fehlerbehandlung:** Bei Fehlschlägen während des Seeding-Vorgangs werden alle Änderungen zurückgesetzt, und ein Audit-Eintrag wird erstellt.

- **Logging & Monitoring:** Alle Seed-Aktivitäten werden über WEG-12 protokolliert und mit einer eindeutigen Correlation-ID versehen.

## Geschäftsregeln & Logik

- Seeds müssen immer zur aktuellen Schema-Version passen. Ein Version Mismatch führt zum Abbruch.

- Seeds dürfen keine bestehenden produktiven Daten überschreiben oder löschen.

- Alle Insert-Operationen erfolgen transaktional; Teilergebnisse sind nicht zulässig.

- Bei Wiederholung eines Seed-Laufs werden bereits angelegte Objekte übersprungen (Idempotenz).

- Nach erfolgreichem Seeding wird der Status im Directory (WEG-13) als *ready* markiert.

- Fehler beim Seeding lösen automatisch einen Retry-Vorgang über den Scheduler (WEG-12) aus.

## Akzeptanzkriterien

- **Gegeben** eine neue Association wurde erstellt &rarr; **Wenn** das Seeding ausgeführt wird &rarr; **Dann** werden alle Basisobjekte (Owner, Building, Rollen, Einstellungen) erfolgreich angelegt und validiert.

- **Gegeben** ein Fehler tritt während des Seeding-Prozesses auf &rarr; **Wenn** dieser erkannt wird &rarr; **Dann** wird der gesamte Prozess abgebrochen, ein Rollback ausgeführt und ein Audit-Eintrag erzeugt.

- **Gegeben** ein Seed-Lauf wird erneut gestartet &rarr; **Wenn** bereits vorhandene Einträge existieren &rarr; **Dann** werden diese erkannt und übersprungen, ohne Duplikate zu erzeugen.

- **Gegeben** ein Modul stellt eigene Seeds bereit &rarr; **Wenn** diese registriert sind &rarr; **Dann** werden sie automatisch in den Provisionierungsprozess integriert.

- **Gegeben** der Seed-Prozess wurde abgeschlossen &rarr; **Wenn** der Directory-Status abgefragt wird &rarr; **Dann** steht dieser auf &bdquo;ready&ldquo; und alle Logs sind im Audit nachvollziehbar.

## Nicht-Ziele

- Keine mandantenspezifischen oder benutzerdefinierten Seed-Daten im MVP.

- Kein paralleles Seeding mehrerer Module ohne zentrale Koordination.

- Keine Datenmigration aus Altsystemen innerhalb dieses Moduls.

## Kritische Fälle

- **Version mismatch:** Seeds passen nicht zur Schema-Version &rarr; Abbruch und Fehlerprotokoll.

- **Teilweise Seeds:** Unterbrechungen während des Prozesses müssen automatisch zurückgesetzt werden.

- **Leistungsprobleme:** Bei größeren Seed-Datenmengen muss der Prozess asynchron erfolgen.

- **Doppelte Initialisierung:** Wiederholte Seeding-Vorgänge dürfen keine Mehrfacheinträge erzeugen.

## Abhängigkeiten

-  – Triggert den Seeding-Prozess nach erfolgreicher Schema-Erstellung.

-  – Stellt Logging-, Retry- und Monitoring-Funktionalitäten bereit.

-  – Verwaltet den Schema-Status im Directory.

-  – Liefert das Datenmodell und technische Basisframeworks.

## Offene Fragen

- Soll der Seeding-Prozess für große Datenmengen asynchron (Scheduler-basiert) ausgeführt werden?

- Wie soll die Reihenfolge der Modul-Seeds festgelegt werden, wenn mehrere Seeds voneinander abhängen?

- Soll die Seed-Validierung bereits im Directory (Pre-Check) erfolgen oder erst nach der Schema-Erstellung?

## Zukunftserweiterungen

- **Customization Hooks:** Ermöglichen individuelle Seeds pro WEG (z. B. spezielle Rollen, Templates).

- **Versionierungs-Framework:** Automatische Migration bestehender Schemas bei Versionsänderungen.

- **Seed-Analytics:** Reporting über Seed-Dauer, Fehlerquote und Erfolgsraten.

- **Parallel-Seeding:** Unterstützung für gleichzeitige Initialisierungen bei Massenerstellungen.

## Verknüpfte Tasks

- [WEG-320 – Seeding Roles/Settings per Schema](https://maierharry.atlassian.net/browse/WEG-320) – Initialisiert Basisrollen, Grundeinstellungen und Beispielobjekte für neue Mandanten.

- [WEG-321 – Seed Validation & Consistency Checks](https://maierharry.atlassian.net/browse/WEG-321) – Prüft Datenintegrität nach Abschluss des Seedings.

- [WEG-322 – Retry & Recovery Handling](https://maierharry.atlassian.net/browse/WEG-322) – Automatisiert Wiederholungen nach Seed-Fehlern.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Standard-Seeding mit Basisdaten, Rollen, Grundeinstellungen, Idempotenz und Rollback bei Fehlern.

**Phase 2**

Erweiterbares Seed-Framework für kundenspezifische Daten und modulübergreifende Seeding-Hooks.

**Phase 3**

Versioniertes Migration-Framework, Seed-Analytics, Parallelisierung und KI-gestützte Datenvalidierung.