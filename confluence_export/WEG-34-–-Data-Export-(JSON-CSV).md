---
title: WEG-34 – Data Export (JSON/CSV)
confluence_id: 27656637
version: 14
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27656637/WEG-34+Data+Export+JSON+CSV
---

**JIRA-Link:** [WEG-34 – Data Export (JSON/CSV)](https://maierharry.atlassian.net/browse/WEG-34)

## Überblick

Das Modul **Data Export (JSON/CSV)** (WEG-34) ermöglicht den Export von Mandanten-Daten in verschiedenen Formaten.

Es unterstützt sowohl vollständige Datenabzüge als auch selektive Exporte einzelner Bereiche (z. B. Stammdaten, Konfigurationen oder Finanzdaten).

Ziel ist es, eine sichere, nachvollziehbare und standardisierte Exportfunktion zu bieten, die für **Datensicherung**, **Migration**, **Archivierung** und **Analysezwecke** eingesetzt werden kann – unter Berücksichtigung von Datenschutz und Auditierbarkeit.

## Beschreibung

WEG-34 stellt den zentralen Mechanismus zum Datenexport aus einer WEG-Instanz bereit.

Die Funktion ermöglicht sowohl **ad-hoc Exporte** durch Administratoren als auch automatisierte, geplante Exporte (in späteren Phasen).

Alle Exporte werden in strukturierter Form generiert und über das **Dokumentenmanagementsystem (WEG-5)** archiviert.

Hauptfunktionen:

- **Vollständige Exporte:** Erstellung eines vollständigen Daten-Snapshots einschließlich aller Tabellen, Relationen und Metadaten, geeignet für Migration oder Backup.

- **Selektive Exporte:** Export einzelner Datenbereiche (z. B. Stammdaten, Eigentümer, Gebäude, Finanzen) zur gezielten Analyse oder Weiterverarbeitung.

- **Formatunterstützung:** Bereitstellung der Exportformate **JSON** und **CSV** mit optionaler ZIP-Komprimierung.

- **DMS-Integration:** Automatische Ablage der erzeugten Exportdateien im Dokumentenmanagement (WEG-50) mit Verknüpfung zum Audit-Log.

- **Integrität & Versionierung:** Hash-Werte stellen sicher, dass Exporte nachvollziehbar und unverändert sind.

- **Datenschutzkonformität:** Berücksichtigt Privacy- und Retention-Policies aus WEG-26 (z. B. Pseudonymisierung oder Redaction sensibler Daten).

- **Prozessprotokollierung:** Jeder Exportvorgang wird vollständig dokumentiert – inklusive Benutzer, Timestamp, Datenumfang und Format.

## Geschäftsregeln & Logik

- Nur autorisierte Benutzer mit den Rollen *SystemAdmin* oder *Manager* dürfen Exporte auslösen.

- Der Exportprozess prüft vor Ausführung die Datenschutz- und Rollenrichtlinien (RBAC, WEG-21, WEG-26).

- Exporte sind mandantenspezifisch – kein Zugriff oder Zusammenführung mehrerer WEG-Schemata.

- Jeder Export wird versioniert; identische Exportparameter erzeugen reproduzierbare Ergebnisse.

- Fehlerhafte Exporte werden abgebrochen, zurückgesetzt und im Audit-Log vermerkt.

- Nach erfolgreichem Export wird das Ergebnis als Dateiobjekt im DMS gespeichert und referenziert.

## Akzeptanzkriterien

- **Gegeben** ein aktiver Mandant existiert &rarr; **Wenn** ein vollständiger Export ausgelöst wird &rarr; **Dann** erstellt das System eine JSON- oder CSV-Datei mit allen Mandantendaten und speichert diese im DMS.

- **Gegeben** ein selektiver Export wird angefordert &rarr; **Wenn** der Benutzer nur bestimmte Bereiche auswählt &rarr; **Dann** enthält die Exportdatei ausschließlich diese Daten und keine weiteren Tabellen oder Metadaten.

- **Gegeben** ein Exportvorgang ist abgeschlossen &rarr; **Wenn** das Audit-Log überprüft wird &rarr; **Dann** enthält es den Initiator, Zeitstempel, Dateigröße und Hash-Wert des Exports.

- **Gegeben** ein Benutzer ohne Berechtigung versucht, einen Export durchzuführen &rarr; **Wenn** der Prozess gestartet wird &rarr; **Dann** wird der Export verweigert und ein entsprechender Eintrag im Audit-Log erzeugt.

- **Gegeben** ein Export überschreitet die Systemgrenzen (z. B. zu große Datenmenge) &rarr; **Wenn** der Vorgang erkannt wird &rarr; **Dann** wird der Export gestoppt, in Batches aufgeteilt oder abgebrochen, und der Benutzer erhält eine Fehlermeldung.

## Nicht-Ziele

- Keine Cross-Tenant-Exporte; jeder Export bezieht sich ausschließlich auf eine einzelne WEG-Instanz.

- Keine Integration mit externen Backup- oder Cloud-Services im MVP.

- Keine Echtzeit-Synchronisation oder Datenreplikation zu Dritt-Systemen.

## Kritische Fälle

- **Große Datenmengen:** Der Export darf bei hohem Datenvolumen nicht zum Systemabbruch führen; asynchrone Verarbeitung erforderlich.

- **Datenschutzverstöße:** Fehlende Redaction-Regeln könnten sensible Daten offenlegen – Validierung muss vorgeschaltet sein.

- **Inkompatible Formate:** Exportstrukturen müssen konsistent zu Schema-Versionen bleiben, um Kompatibilitätsprobleme zu vermeiden.

- **Fehlerhafte Audit-Logs:** Unvollständige oder fehlende Log-Einträge gefährden Revisionssicherheit.

## Abhängigkeiten

-  – Speicherung und Verwaltung der Exportdateien.

-  – Protokollierung von Export-Events und Benutzeraktionen.

-  – Anwendung von Redaction- und Retention-Richtlinien.

-  – Zugriff auf Mandanten-Metadaten für die Auswahl und Strukturierung der Exportinhalte.

-  – Bereitstellung der technischen Export-API und Dateischnittstellen.

## Offene Fragen

- Soll das System periodische Exporte automatisch (z. B. monatlich oder jährlich) planen und durchführen?

- Müssen Exporte nach Erzeugung signiert oder zusätzlich verschlüsselt werden?

- Soll die Exportstruktur standardisiert (z. B. für Importe in andere Systeme) dokumentiert werden?

## Zukunftserweiterungen

- **Inkrementelle Exporte:** Exportiert nur Datenänderungen seit dem letzten Export.

- **Weitere Formate:** Unterstützung für XML, XLSX oder proprietäre Austauschformate.

- **Geplante Exporte:** Scheduler-Integration zur automatischen Generierung von Archiv- oder Sicherungs-Dumps.

- **API-basierte Exporte:** Direkter Zugriff auf strukturierte Exporte über REST-Schnittstellen.

- **Verschlüsselung & Signierung:** End-to-End-sichere Exportpakete mit Zertifikatsprüfung.

## Verknüpfte Tasks

- [WEG-340 – Export Association as JSON/CSV](https://maierharry.atlassian.net/browse/WEG-340) – Implementierung der Exportfunktion für komplette oder selektive Mandantendaten.

- [WEG-341 – Privacy-Aware Data Export](https://maierharry.atlassian.net/browse/WEG-341) – Anwendung der Datenschutzrichtlinien während des Exports.

- [WEG-342 – DMS-Integration & Versionierung](https://maierharry.atlassian.net/browse/WEG-342) – Speicherung und Verwaltung von Exportversionen im Dokumentenmanagementsystem.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Vollständiger und selektiver Export in JSON/CSV, Ablage im DMS, Audit-Protokollierung, Berechtigungsprüfung.

**Phase 2**

Unterstützung zusätzlicher Formate (XML), inkrementelle Exporte, zeitgesteuerte Abläufe.

**Phase 3**

API-basierte Datenfeeds, automatische Signierung/Verschlüsselung und Integration externer Systeme.