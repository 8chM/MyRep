---
title: WEG-30 – Association Registry & Provisioning (Schema Create)
confluence_id: 27722234
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722234/WEG-30+Association+Registry+Provisioning+Schema+Create
---

**JIRA-Link:** [WEG-30 – Association Registry & Provisioning (Schema Create)](https://maierharry.atlassian.net/browse/WEG-30)

## Überblick

Das Modul **Association Registry & Provisioning** (WEG-30) bildet den Einstiegspunkt für die Verwaltung neuer WEG-Associations innerhalb des Systems.

Es ist verantwortlich für die Erstellung neuer Mandanteninstanzen (Schemas) und die Eintragung dieser Mandanten in das zentrale Directory.

Ziel ist es, eine vollautomatische, sichere und nachvollziehbare Bereitstellung neuer WEG-Datenumgebungen zu ermöglichen, die sofort betriebsbereit sind.

## Beschreibung

WEG-30 orchestriert den gesamten Onboarding-Prozess für neue Eigentümergemeinschaften (Associations) und sorgt für die technische und organisatorische Mandantentrennung.

Das Modul interagiert dabei mit der Directory-Datenbank, um neue Einträge zu erzeugen, und mit der Datenbankinfrastruktur (über WEG-31 und WEG-32), um das Schema anzulegen und initiale Daten zu importieren.

Hauptfunktionen:

- **Schemaerstellung:** Automatische Erzeugung eines neuen Datenbankschemas für jede Association auf dem ausgewählten Endpunkt.

- **Registry-Eintrag:** Registrierung der neuen Association im zentralen Directory inklusive Name, ID, Endpunkt und Status.

- **Initiales Seeding:** Automatische Erstellung von Standarddaten wie Basisrollen, Templates, Standardkonfigurationen und Beispielobjekten.

- **Validierung & Eindeutigkeit:** Vor der Provisionierung werden Name, ID und Endpunktverfügbarkeit geprüft, um Konflikte zu vermeiden.

- **Rollback-Mechanismus:** Fehlerhafte Provisionierungen führen zu einem vollständigen Rücksetzen aller Änderungen.

- **Scheduler-Integration:** Provisionierungsvorgänge werden asynchron abgewickelt; bei Fehlern erfolgt ein automatischer Retry (über WEG-12).

- **Logging & Audit:** Alle Schritte des Provisionings werden in WEG-24 dokumentiert.

## Geschäftsregeln & Logik

- Jede neue Association muss über einen eindeutigen Namen und eine eindeutige ID verfügen.

- Ein Provisionierungsprozess darf nur gestartet werden, wenn ein gültiger Datenbankendpunkt verfügbar ist.

- Bei Fehlern während der Erstellung oder beim Seeding erfolgt ein vollständiger Rollback, um Inkonsistenzen zu verhindern.

- Das Seeding darf nur ausgeführt werden, wenn das Schema erfolgreich erstellt und validiert wurde.

- Der Status einer Association (z. B. &bdquo;in Provisioning&ldquo;, &bdquo;active&ldquo;, &bdquo;failed&ldquo;) wird während des gesamten Prozesses fortlaufend aktualisiert.

- Provisionierungen werden in einem dedizierten Warteschlangen- oder Scheduler-System verwaltet, um parallele Ausführungen zu ermöglichen.

## Akzeptanzkriterien

- **Gegeben** ein neuer Mandant wird angelegt &rarr; **Wenn** der Provisionierungsprozess gestartet wird &rarr; **Dann** wird automatisch ein neues Schema erzeugt und im Directory registriert.

- **Gegeben** ein Namenskonflikt oder Endpunktfehler tritt auf &rarr; **Wenn** dieser erkannt wird &rarr; **Dann** wird der Prozess abgebrochen, ein Rollback ausgeführt und ein Fehlerprotokoll erstellt.

- **Gegeben** die Provisionierung wurde erfolgreich abgeschlossen &rarr; **Wenn** das Seeding erfolgt &rarr; **Dann** sind alle Standardrollen, Konfigurationen und Vorlagen einsatzbereit.

- **Gegeben** der Provisionierungsprozess scheitert &rarr; **Wenn** der Scheduler das erkennt &rarr; **Dann** wird der Vorgang in einer Retry-Schleife erneut gestartet.

- **Gegeben** ein Administrator ruft das Provisionierungsprotokoll auf &rarr; **Wenn** die Ansicht geladen wird &rarr; **Dann** werden alle Schritte, Zeiten und Statusänderungen korrekt angezeigt.

## Nicht-Ziele

- Keine Mandantenzusammenführung oder -aufspaltung im MVP.

- Kein manuelles Verschieben bestehender Schemas zwischen Datenbankinstanzen.

- Kein Self-Service-Provisioning durch Endnutzer im MVP.

## Kritische Fälle

- **Doppelte Namen/IDs:** Können zu Datenkonflikten führen – das System muss sie vor der Erstellung abfangen.

- **Seed-Fehler:** Fehlende oder fehlerhafte Seed-Daten können den Mandanten unbrauchbar machen – Validierung ist zwingend erforderlich.

- **Rollback-Fehler:** Wenn ein Rollback fehlschlägt, muss der Status der Association auf &bdquo;failed&ldquo; gesetzt und eine manuelle Überprüfung erzwungen werden.

- **Mehrfache Trigger:** Parallele Provisionierungen dürfen sich nicht gegenseitig beeinflussen.

## Abhängigkeiten

-  – Auswahl und Verwaltung des Zielendpunkts für das neue Schema.

-  – Initiales Seeding von Basisdaten und Vorlagen.

-  – Fehlerbehandlung, Logging und Retry-Mechanismen.

-  – Nachvollziehbarkeit der Provisionierungsvorgänge.

-  – Übergeordnete Mandantenverwaltung.

## Offene Fragen

- Soll die Erstellung neuer Associations genehmigungspflichtig (Vier-Augen-Prinzip) erfolgen?

- Müssen Namensräume für zukünftige Associations reserviert werden, bevor die Provisionierung final ausgeführt wird?

- Soll das System bei hoher Last Provisionierungen automatisch in Warteschlangen priorisieren?

## Zukunftserweiterungen

- **Self-Service-Onboarding:** Benutzeroberfläche für Verwalter zur selbstständigen Mandantenerstellung mit automatischer Prüfung.

- **Mehrstufige Provisionierung:** Freigabeprozess durch mehrere Rollen vor finaler Aktivierung.

- **Automatische Skalierung:** Dynamische Zuordnung neuer Mandanten zu verfügbaren Datenbankinstanzen.

- **Provisioning-Monitoring:** Dashboard mit Statusanzeigen, Laufzeiten und Erfolgsraten.

## Verknüpfte Tasks

- [WEG-300 – Create Association (schema + seed)](https://maierharry.atlassian.net/browse/WEG-300) – Erstellt das Schema und führt initiale Datenimporte durch.

- [WEG-301 – Assign DB Endpoint to Association](https://maierharry.atlassian.net/browse/WEG-301) – Ordnet den neuen Mandanten einem verfügbaren Datenbankendpunkt zu.

- [WEG-302 – Provisioning Errors & Rollback](https://maierharry.atlassian.net/browse/WEG-302) – Implementiert Fehlerbehandlung, Retry und vollständige Rücksetzlogik.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Vollständiger Provisionierungsprozess inkl. Schemaerstellung, Directory-Eintrag, Basisdaten-Seeding und Rollback.

**Phase 2**

Self-Service-Onboarding-UI, Genehmigungsprozesse und asynchrone Warteschlangensteuerung.

**Phase 3**

Automatische Skalierung, intelligente Endpunktverteilung, Monitoring-Dashboard mit Statusverfolgung.