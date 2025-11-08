---
title: WEG-70 – Meter Registry & Types (Electric/Water/Gas/Heat)
confluence_id: 26968685
version: 22
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/26968685/WEG-70+Meter+Registry+Types+Electric+Water+Gas+Heat
---

**JIRA-Link:** [WEG-70 – Meter Registry & Types (Electric/Water/Gas/Heat)](https://maierharry.atlassian.net/browse/WEG-70)

## Überblick
Das Modul **Meter Registry & Types** (WEG-70) bildet das zentrale Verzeichnis für alle Verbrauchszähler innerhalb einer WEG. Es verwaltet alle relevanten Metadaten – Medium, Typ, Seriennummer, Standort und Status – und stellt sicher, dass jeder Zähler eindeutig erfasst und über seinen gesamten Lebenszyklus nachvollziehbar bleibt. Ziel ist die Schaffung einer zentralen, revisionssicheren Datenbasis für Verbrauchserfassung, Abrechnung und Wartung, die konsistent über alle Abrechnungszeiträume hinweg bleibt.

## Beschreibung
WEG-70 stellt die Grundlage sämtlicher Prozesse im Bereich **Metering** dar und dient als verbindliche Referenz für Zählerdaten innerhalb des Systems. Das Modul ermöglicht die Anlage, Pflege, Historisierung und Archivierung von Zählern, um deren Lebenszyklus vollständig digital abzubilden. Jede Änderung an einem Zähler wird nachvollziehbar dokumentiert, und die Daten stehen anderen Modulen – etwa WEG-7 (Verbrauch), WEG-8 (Finanzen) oder WEG-5 (Dokumentenmanagement) – als Quelle zur Verfügung.

Hauptfunktionen:

- **Zählererfassung:** Anlage neuer Zähler mit Pflichtfeldern (Medium, Typ, Seriennummer, Standort, Startdatum).

- **Erweiterte Informationen:** Optional können Hersteller, Eichdatum, Bemerkungen und technische Parameter hinterlegt werden.

- **Import & Export:** Unterstützung des CSV-Imports zur Massenanlage sowie strukturierter Exporte für Auswertungen.

- **Statusverwaltung:** Zähler durchlaufen definierte Stati wie *aktiv*, *defekt*, *ersetzt* oder *archiviert*.

- **Validierungslogik:** Prüfung auf doppelte Seriennummern und fehlerhafte Einträge; Verhinderung redundanter Datensätze.

- **Zuordnung:** Verknüpfung von Zählern mit Gebäuden, Einheiten oder Verbrauchsgruppen.

- **Audit-Integration:** Jede Änderung wird mit Benutzer, Zeitstempel und Grund protokolliert.

- **Archivierung:** Archivierte Zähler bleiben abrufbar, aber schreibgeschützt.

## Geschäftsregeln & Logik
- Jeder Zähler ist eindeutig einer WEG zugeordnet.

- Pflichtfelder müssen ausgefüllt sein, bevor ein Datensatz gespeichert wird.

- Statusänderungen werden protokolliert und erfordern eine Begründung.

- Archivierte Zähler dürfen nicht verändert oder gelöscht werden.

- Beim Import prüft das System automatisch auf doppelte Seriennummern.

- Nur Verwalter oder Administratoren dürfen Zähler anlegen oder entfernen.

## Akzeptanzkriterien
- **Gegeben** ein neuer Zähler wird angelegt &rarr; **Wenn** alle Pflichtfelder ausgefüllt sind &rarr; **Dann** wird der Datensatz gespeichert, der Status auf *aktiv* gesetzt und im Audit protokolliert.

- **Gegeben** eine CSV-Datei wird importiert &rarr; **Wenn** doppelte Seriennummern erkannt werden &rarr; **Dann** blockiert das System die Einträge und zeigt eine Fehlermeldung.

- **Gegeben** ein Zähler wird deaktiviert &rarr; **Wenn** der Status geändert wird &rarr; **Dann** wird er aus Abrechnungsprozessen entfernt und der Vorgang dokumentiert.

- **Gegeben** ein archivierter Zähler wird geöffnet &rarr; **Wenn** der Benutzer eine Änderung versucht &rarr; **Dann** verweigert das System die Bearbeitung mit Warnmeldung.

- **Gegeben** ein Gebäude wird gelöscht oder zusammengeführt &rarr; **Wenn** ein Zähler zugeordnet ist &rarr; **Dann** wird dieser automatisch archiviert oder neu verknüpft.

## Nicht-Ziele
- Keine automatische Erkennung von Zählern über QR-/NFC-Scanner.

- Keine Integration externer Gerätekataloge oder Herstellerdaten im MVP.

- Keine automatische Überwachung von Eichfristen in der ersten Version.

## Kritische Fälle
- **Doppelte Seriennummern:** System muss Dubletten strikt verhindern.

- **Fehlende Pflichtfelder:** Speicherung wird blockiert, bis alle Pflichtangaben vorhanden sind.

- **Ungültige Statuswechsel:** Ein Wechsel von *archiviert* auf *aktiv* ist unzulässig.

- **Unvollständige Zuordnung:** Zähler ohne gültige Einheit oder Gebäude dürfen nicht aktiviert werden.

## Abhängigkeiten
- WEG-1 – Platform Foundation – Datenmodell und API-Struktur.

- WEG-5 – Document Management – Verwaltung von Zählerdokumenten, Eichscheinen und Fotos.

- WEG-7 – Metering – Verwendung als Primärquelle für Verbrauchsdaten.

- WEG-24 – Audit Log – Protokollierung aller Änderungen.

- WEG-26 – Data Privacy & Redaction – Schutz sensibler Daten und Bilddateien.

## Offene Fragen
- Soll der CSV-Import feste Feldnamen oder konfigurierbare Zuordnungen verwenden?

- Können historische Zähler rückwirkend erfasst werden?

- Soll das Löschen eines Zählers automatische Benachrichtigungen an abhängige Module auslösen?

## Zukunftserweiterungen
- Scannen von Seriennummern per Kamera oder Mobilgerät.

- Automatische Übernahme technischer Daten über Hersteller-APIs.

- Erinnerungsfunktion für Eichfristen mit Sperrlogik.

- Grafische Visualisierung von Zählerhierarchien (Haupt-/Unterzähler).

## Verknüpfte Tasks
- [WEG-700 – Meter Types & Registry](https://maierharry.atlassian.net/browse/WEG-700) – Implementierung der zentralen Zählerregistrierung inklusive Verwaltung von Typen, Seriennummern und Statuswechseln.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Basis-Zählerregistrierung mit Pflichtfeldern, CSV-Import, Statusverwaltung, Audit-Integration und Zuordnung zu Gebäuden/Einheiten.

**Phase 2**

Erweiterter Import mit Dublettenprüfung, Scan-Funktion, verbesserte Such- und Filteroptionen.

**Phase 3**

Integration von Herstellerkatalogen, Eichüberwachung und grafischer Hierarchiedarstellung.