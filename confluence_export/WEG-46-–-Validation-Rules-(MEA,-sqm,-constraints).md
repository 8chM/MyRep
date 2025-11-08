---
title: WEG-46 – Validation Rules (MEA, sqm, constraints)
confluence_id: 27722279
version: 12
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722279/WEG-46+Validation+Rules+MEA+sqm+constraints
---

**JIRA-Link:** [WEG-46 – Validation Rules (MEA, sqm, constraints)](https://maierharry.atlassian.net/browse/WEG-46)

## Überblick

Das Modul **Validation Rules** (WEG-46) definiert und verwaltet sämtliche Validierungsmechanismen für Einheiten-, Flächen- und MEA-Daten (Miteigentumsanteile).

Es stellt sicher, dass alle Stammdaten logisch konsistent, vollständig und regelkonform vorliegen, bevor sie in Finanz-, Abrechnungs- oder Eigentümerprozesse übernommen werden.

Ziel ist es, Datenqualität und Systemintegrität über alle Module hinweg zu gewährleisten und fehlerhafte Eingaben oder Importe frühzeitig zu verhindern.

## Beschreibung

WEG-46 wird automatisch bei allen relevanten Operationen wie **Erfassung, Änderung, Import oder Abrechnung** ausgelöst.

Das Modul prüft Stammdaten auf Plausibilität, mathematische Korrektheit und gesetzte Grenzwerte (z. B. MEA-Summe = 100 % &plusmn; Toleranz).

Fehlerhafte oder unvollständige Eingaben werden blockiert und mit klaren Hinweisen zur Ursache gemeldet.

Hauptfunktionen:

- **MEA-Validierung:** Sicherstellung, dass die Summe aller Miteigentumsanteile 100 % (oder innerhalb einer konfigurierbaren Toleranz) beträgt.

- **Flächenprüfung:** Keine Null-, Negativ- oder unplausiblen Flächenwerte.

- **Pflichtfeldprüfung:** Überwachung, dass alle erforderlichen Felder (z. B. Einheit, MEA, Fläche) ausgefüllt sind.

- **Automatische Prüfungen bei Importen:** Validierung aller CSV- oder API-basierten Dateneinspielungen (z. B. WEG-45).

- **Fehlerklassifizierung:** Unterscheidung zwischen Warnungen (nicht blockierend) und Fehlern (blockierend).

- **Audit-Integration:** Jede Validierung und ihr Ergebnis werden revisionssicher im Audit-Log (WEG-24) gespeichert.

- **Konfigurierbare Schwellenwerte:** Administrator:innen können Toleranzgrenzen und Prüfarten pro WEG definieren.

## Geschäftsregeln & Logik

- Alle Datensätze müssen konsistent und vollständig sein, bevor sie gespeichert oder freigegeben werden.

- Blockierende Fehler verhindern das Speichern oder Importieren, während Warnungen lediglich Hinweise ausgeben.

- Validierungen werden bei jedem Speichern, Import, Merge/Split (WEG-43) oder Finanzvorgang (WEG-8) automatisch ausgeführt.

- Prüfberichte können als Teil von Audit- oder DMS-Dokumenten abgelegt werden.

- Änderungen an Validierungsregeln sind nur durch Administrator:innen erlaubt.

## Akzeptanzkriterien

- **Gegeben** eine Einheit weist eine inkonsistente MEA-Summe auf &rarr; **Wenn** der Speichervorgang ausgeführt wird &rarr; **Dann** wird der Vorgang blockiert und eine Fehlermeldung angezeigt.

- **Gegeben** ein CSV-Import enthält Flächenwerte von 0 m&sup2; &rarr; **Wenn** der Import gestartet wird &rarr; **Dann** wird der Datensatz abgelehnt und im Fehlerbericht mit Begründung aufgeführt.

- **Gegeben** ein gültiger Datensatz mit korrekten MEA- und Flächenwerten &rarr; **Wenn** er gespeichert wird &rarr; **Dann** wird die Speicherung ohne Fehlermeldung abgeschlossen.

- **Gegeben** die Summe der MEA liegt innerhalb des Toleranzbereichs &rarr; **Wenn** die Daten gespeichert werden &rarr; **Dann** wird eine Warnung ausgegeben, aber der Vorgang zugelassen.

- **Gegeben** eine Validierung schlägt fehl &rarr; **Wenn** das Audit-Logging aktiv ist &rarr; **Dann** wird der Fehler mit Zeitstempel, Benutzer und Modul protokolliert.

## Nicht-Ziele

- Keine automatische Korrektur oder Bereinigung fehlerhafter Daten.

- Keine KI-gestützte Plausibilitätsanalyse im MVP.

- Keine Echtzeitüberwachung außerhalb definierter Prüfprozesse.

## Kritische Fälle

- **Falsche MEA-Verteilung:** Ungültige Schlüssel oder Rundungsfehler können sich auf Abrechnungen auswirken.

- **Importfehler:** Große Importe mit fehlerhaften Daten können zahlreiche Validierungsfehler verursachen – erfordern Batch-Reporting.

- **Fehlkonfigurierte Toleranzen:** Zu großzügige Einstellungen können zu unbemerkten Abweichungen führen.

## Abhängigkeiten

-  – Führt Validierungen beim Speichern von Einheiten aus.

-  – Nutzt Validierungslogik für Importdaten.

-  – Verwendet geprüfte MEA- und Flächendaten als Grundlage für Umlageschlüssel.

-  – Dokumentiert Validierungsergebnisse und Fehlermeldungen.

-  – Quelle der zu prüfenden Stammdaten.

## Offene Fragen

- Sollen Warnungen bei geringfügigen Abweichungen nur angezeigt oder bereits protokolliert werden?

- Wie granular sollen Validierungsregeln pro WEG konfigurierbar sein (global, per Gebäude, per Einheit)?

- Soll der Prüfbericht automatisch im DMS gespeichert werden (z. B. über WEG-5)?

## Zukunftserweiterungen

- **Automatische Prüfberichte:** Erstellung periodischer Reports und Archivierung im DMS.

- **Benutzerdefinierte Validierungen:** Eigene Regeln pro WEG, konfigurierbar durch Administrator:innen.

- **Erweiterte Integrationen:** Validierung von Verbrauchs-, Vertrags- und Finanzdaten in späteren Phasen.

## Verknüpfte Tasks

- [WEG-460 – MEA/sqm Constraints & Consistency](https://maierharry.atlassian.net/browse/WEG-460) – Implementierung der Validierungslogik für MEA-, Flächen- und Pflichtfeldprüfungen.

- [WEG-461 – Validation Report Generation](https://maierharry.atlassian.net/browse/WEG-461) – Automatische Erstellung von Validierungs- und Fehlerprotokollen.

- [WEG-462 – Configurable Tolerance Engine](https://maierharry.atlassian.net/browse/WEG-462) – Verwaltung individueller Grenzwerte und Prüfregeln pro WEG.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Grundvalidierungen für MEA-Summen, Flächenwerte, Pflichtfelder und Audit-Protokollierung.

**Phase 2**

Benutzerdefinierte Validierungsregeln und konfigurierbare Toleranzwerte pro WEG.

**Phase 3**

Automatische Validierungsberichte, DMS-Integration und erweiterte Datenquellenprüfungen.