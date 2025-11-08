---
title: WEG-88 – Finance Export & Compliance (CSV/XLS/PDF, Audit)
confluence_id: 27591459
version: 10
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27591459/WEG-88+Finance+Export+Compliance+CSV+XLS+PDF+Audit
---

**JIRA-Link:** [WEG-88 – Finance Export & Compliance (CSV/XLS/PDF, Audit)](https://maierharry.atlassian.net/browse/WEG-88)

## Überblick
Das Modul **Finance Export & Compliance **(WEG-88) sorgt für standardisierte, revisionssichere Exporte aller Finanz- und Abrechnungsdaten einer WEG. Es ermöglicht Exporte in mehreren Formaten (CSV, XLS, PDF) und stellt sicher, dass alle exportierten Dateien eindeutig nachvollziehbar, überprüfbar und manipulationssicher gespeichert werden. Ziel ist es, Prüfern, Steuerberatern und Behörden einen rechtssicheren Zugriff auf geprüfte Finanzdaten zu ermöglichen.

## Beschreibung
WEG-88 erweitert die Finanzmodule um ein flexibles Export- und Prüfungsframework. Jeder Export kann parametrisiert werden (z. B. Zeitraum, Konten, Kostenstellen) und erzeugt neben der eigentlichen Datei auch einen vollständigen Audit-Eintrag. Zur Sicherstellung der Datenintegrität werden Hashwerte (SHA-256) generiert, in der Datenbank gespeichert und mit dem Export verknüpft. Alle Exporte werden in einer unveränderlichen Export-Historie protokolliert und stehen für Nachweise und Audits bereit.

Hauptfunktionen:

- **Parametrisierbare Exporte:** Filterung nach Zeitraum, Konten, Kostenstellen und Detailgrad (Summen oder Einzelposten).

- **Mehrformat-Export:** Unterstützung für CSV, XLS und PDF-Formate.

- **Integritätsprüfung:** Automatische Hash-Generierung (SHA-256) für jede Datei zur späteren Verifikation.

- **Audit-Trail:** Lückenlose Protokollierung jedes Exports (Benutzer, Timestamp, Parameter, Dateiname, Hashwert).

- **Export-Historie:** Revisionssicheres Archiv aller Exporte; keine Löschung möglich.

- **Compliance-Validierung:** Sicherstellung der Nachvollziehbarkeit gemäß GoBD- und DSGVO-Anforderungen.

## Geschäftsregeln & Logik
- Jeder Export muss eindeutig identifizierbar und mit einem Hashwert versehen sein.

- Exportparameter (Zeitraum, Filter, Format) werden in der Datenbank protokolliert.

- Hashwerte werden beim erneuten Upload überprüft, um Manipulationen auszuschließen.

- Nur Benutzer mit entsprechender Berechtigung (Verwalter / Hauptverwalter) dürfen Exporte durchführen.

- Export-Protokolle sind unveränderlich und dürfen nicht gelöscht oder überschrieben werden.

- Ein Exportvorgang gilt nur dann als erfolgreich, wenn sowohl Datei als auch Audit-Eintrag abgeschlossen sind.

## Akzeptanzkriterien
- **Gegeben** ein Verwalter möchte alle Transaktionen eines Wirtschaftsjahres exportieren &rarr; **Wenn** er den Zeitraum 01.01.2024 – 31.12.2024 auswählt &rarr; **Dann** wird eine CSV-Datei generiert, mit SHA-256-Hash versehen und im Audit-Log gespeichert.

- **Gegeben** ein Prüfer lädt eine exportierte Datei hoch &rarr; **Wenn** der gespeicherte Hash überprüft wird &rarr; **Dann** muss der Hashwert mit dem gespeicherten Wert übereinstimmen.

- **Gegeben** ein Benutzer ohne Berechtigung versucht, einen Export durchzuführen &rarr; **Wenn** der Vorgang gestartet wird &rarr; **Dann** verweigert das System den Zugriff und zeigt eine Fehlermeldung an.

- **Gegeben** ein Export wird abgeschlossen &rarr; **Wenn** das Audit-Protokoll geschrieben ist &rarr; **Dann** wird der Eintrag schreibgeschützt gespeichert und kann nicht mehr verändert werden.

- **Gegeben** ein Exportparameter ist ungültig &rarr; **Wenn** der Export gestartet wird &rarr; **Dann** bricht der Prozess ab und meldet einen Validierungsfehler.

## Nicht-Ziele
- Keine digitale Signatur oder Verschlüsselung im MVP.

- Kein automatischer Versand der Exportdateien an Dritte.

- Keine Echtzeit-Anbindung an Steuer- oder Buchhaltungssoftware.

## Kritische Fälle
- **Fehlerhafte Filterung:** Ungültige Parameter (z. B. fehlerhafte Konten) führen zu Abbruch mit Protokollierung.

- **Hash-Konflikt:** Wenn ein gespeicherter Hash nicht mit dem generierten übereinstimmt, wird der Export blockiert.

- **Datenlücken:** Fehlende oder unvollständige Daten erzeugen ein Warnflag im Audit-Log.

- **Speicherfehler:** Unvollständige Exporte dürfen keine Audit-Einträge erzeugen.

## Abhängigkeiten
- WEG-8 – Finance & Banking – Quelle für alle Buchungsdaten.

- WEG-80 – Finance Master Data – Filterlogik für Konten und Kostenstellen.

- WEG-81 – Accounts Setup – Bereitstellung der Kontostruktur und Zeiträume.

- WEG-2 – Identity & Access – Rollen- und Berechtigungssteuerung für Exporte.

- WEG-24 – Audit Log – Speicherung der Export-Historie und Hashwerte.

## Offene Fragen
- Soll die Download-Verfügbarkeit zeitlich begrenzt werden (z. B. 24 h-Links)?

- Wie werden sehr große Exporte (> 100 MB) gehandhabt – asynchron oder paginiert?

- Soll ein automatisches Export-Archiv in der Cloud entstehen?

## Zukunftserweiterungen
- **Geplante Exporte:** Scheduler-Funktion für wiederkehrende Exporte (z. B. monatlich).

- **Export-Templates:** Speicherung wiederverwendbarer Konfigurationen (z. B. Jahresabschluss).

- **DATEV-Export:** Standardisierte Schnittstelle zu externer Buchhaltungssoftware.

- **Compliance-Reports:** Automatische Generierung von Audit-Berichten für Prüfer.

## Verknüpfte Tasks
- 
## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Parametrisierbare Exporte (CSV/XLS/PDF), Hash-Generierung (SHA-256), vollständige Audit-Trail-Erfassung.

**Phase 2**

Geplante Exporte (Scheduler), Export-Templates, automatische Archivierung.

**Phase 3**

DATEV-Schnittstelle, Compliance-Reports, digitale Signaturen.