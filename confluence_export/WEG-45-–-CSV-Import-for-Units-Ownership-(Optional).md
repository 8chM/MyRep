---
title: WEG-45 – CSV Import for Units/Ownership (Optional)
confluence_id: 27722264
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722264/WEG-45+CSV+Import+for+Units+Ownership+Optional
---

**JIRA-Link:** [WEG-45 – CSV Import for Units/Ownership (Optional)](https://maierharry.atlassian.net/browse/WEG-45)

## Überblick

Das Modul **CSV Import for Units/Ownership** (WEG-45) ermöglicht die strukturierte und sichere Übernahme von Bestandsdaten in das WEG Management System (WMS).

Es dient insbesondere der Ersteinrichtung oder Migration von bestehenden WEG-Daten aus Fremdsystemen.

Über definierte CSV-Vorlagen können Einheiten, Eigentümer:innen und zugehörige MEA-Anteile eingelesen werden.

Das System validiert alle Datensätze auf Plausibilität, prüft Pflichtfelder, berechnet MEA-Summen und erstellt detaillierte Protokolle.

Ziel ist es, eine fehlerresistente, nachvollziehbare und skalierbare Importlösung zu bieten, die den Administrationsaufwand reduziert.

## Beschreibung

Der CSV-Import ist als optionales Werkzeug konzipiert, das Administrator:innen beim schnellen Onboarding neuer Gemeinschaften unterstützt.

Nutzer:innen können standardisierte Vorlagen herunterladen, ausfüllen und anschließend hochladen.

Das System analysiert die Datei zeilenweise, validiert die Einträge und importiert ausschließlich fehlerfreie Datensätze.

Fehlerhafte Zeilen werden im Validierungsbericht aufgeführt, inklusive Fehlerbeschreibung, Spaltenname und Zeilennummer.

Hauptfunktionen:

- **Standardisierte Vorlagen:** CSV-Strukturen mit vordefinierten Kopfzeilen (z. B. Einheit, Eigentümer, MEA, Fläche).

- **Validierung & Plausibilitätsprüfung:** Prüfung auf Pflichtfelder, MEA-Summen und konsistente Verknüpfungen.

- **Teilimporte:** Das System importiert korrekte Zeilen, während fehlerhafte übersprungen und protokolliert werden.

- **Scheduler-Integration:** Optional können automatische Importvorgänge terminiert werden.

- **Audit-Protokollierung:** Alle Importe, Validierungen und Ergebnisse werden im Audit-Log (WEG-24) gespeichert.

- **Importberichte:** Generierte CSV-/PDF-Berichte dokumentieren den gesamten Ablauf, inklusive fehlerhafter Einträge.

## Geschäftsregeln & Logik

- **Pflichtfelder:** Alle notwendigen Felder müssen vorhanden sein, sonst wird der Import blockiert.

- **MEA-Validierung:** Summen der Miteigentumsanteile müssen 100 % ergeben oder systemweit konfigurierbare Toleranzwerte einhalten.

- **Teilimporte:** Korrekte Zeilen werden importiert, fehlerhafte separat im Fehlerbericht vermerkt.

- **Protokollpflicht:** Jeder Import erzeugt einen Audit-Eintrag mit Zeitstempel und Benutzerinformationen.

- **Scheduler-Funktion:** Automatisierte Imports können zeitgesteuert ausgeführt werden.

## Akzeptanzkriterien

- **Gegeben** eine gültige CSV-Datei wird importiert &rarr; **Wenn** der Import ausgeführt wird &rarr; **Dann** werden alle Datensätze erfolgreich angelegt und ein Audit-Eintrag erzeugt.

- **Gegeben** eine CSV-Datei enthält fehlerhafte Zeilen &rarr; **Wenn** der Import ausgeführt wird &rarr; **Dann** importiert das System nur die fehlerfreien Datensätze und erstellt einen detaillierten Validierungsbericht.

- **Gegeben** ein automatischer Scheduler-Import wird gestartet &rarr; **Wenn** die Verarbeitung erfolgt &rarr; **Dann** gelten dieselben Prüfregeln und Audit-Anforderungen wie beim manuellen Import.

- **Gegeben** eine CSV-Datei fehlt ein Pflichtfeld &rarr; **Wenn** der Importvorgang gestartet wird &rarr; **Dann** wird der Vorgang blockiert und eine Fehlermeldung mit Verweis auf die betroffene Spalte angezeigt.

- **Gegeben** eine importierte Einheit hat fehlerhafte MEA-Werte &rarr; **Wenn** der Import abgeschlossen wird &rarr; **Dann** wird die Zeile verworfen und im Fehlerbericht dokumentiert.

## Nicht-Ziele

- Kein direkter Import anderer Dateiformate (z. B. XLSX, XML) im MVP.

- Keine automatische Dublettenprüfung zwischen verschiedenen WEGs.

- Kein bidirektionaler Export-Import-Mechanismus im MVP.

## Kritische Fälle

- **Falsches Format:** Falsch strukturierte CSV-Dateien führen zu Abbruch und Fehlerbericht.

- **Große Dateien:** Bei Dateien mit >10.000 Zeilen wird eine Warnung ausgegeben und der Import in Teilblöcken ausgeführt.

- **Unvollständige Referenzen:** Fehlende Zuordnungen zu Eigentümern oder Einheiten erzeugen Blockierungen.

## Abhängigkeiten

-  – Steuerung und Protokollierung von Importprozessen und Fehlern.

-  – Validierung von MEA-Summen, Pflichtfeldern und Zuordnungen.

-  – Nachvollziehbarkeit der Importe und Änderungen.

-  – Nutzung importierter Daten für die initiale Finanzkonfiguration.

## Offene Fragen

- Soll ein visuell unterstützter Import-Wizard mit Vorschau bereits im MVP integriert werden?

- Wie sollen sehr große CSV-Dateien (>100 MB) verarbeitet werden – Chunking oder asynchrone Verarbeitung?

- Sollen Importvorlagen mandantenspezifisch konfigurierbar sein?

## Zukunftserweiterungen

- **Import-Wizard:** Schritt-für-Schritt-UI mit Live-Vorschau, Validierungsfeedback und Mapping.

- **Erweiterte Formatunterstützung:** Import von XLSX, XML und JSON-Dateien.

- **Automatische Dublettenprüfung:** Erkennung und Zusammenführung mehrfach vorhandener Einträge.

- **Fehlererkennung durch KI:** Automatische Zuordnung von Feldern auch bei unvollständigen Vorlagen.

## Verknüpfte Tasks

- [WEG-450 – CSV Templates for Units/Ownership](https://maierharry.atlassian.net/browse/WEG-450) – Erstellung standardisierter CSV-Vorlagen und Pflichtfelddefinitionen.

- [WEG-451 – Import Wizard (optional later)](https://maierharry.atlassian.net/browse/WEG-451) – Entwicklung eines UI-basierten Importprozesses mit Vorschau und Benutzerführung.

- [WEG-452 – Import Scheduler Integration](https://maierharry.atlassian.net/browse/WEG-452) – Implementierung der automatisierten, zeitgesteuerten Imports.

- [WEG-453 – Validation & Error Report Generator](https://maierharry.atlassian.net/browse/WEG-453) – Erstellung von Fehler- und Erfolgsberichten nach jedem Importlauf.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Manueller CSV-Import für Einheiten und Eigentümer:innen mit Validierung, MEA-Prüfung, Audit-Logging und Fehlerbericht.

**Phase 2**

UI-basierter Import-Wizard mit Vorschau und Scheduler-Unterstützung.

**Phase 3**

Unterstützung weiterer Dateiformate (XLSX, XML), KI-basierte Feldzuordnung und Big-File-Handling.