---
title: WEG-24 – Audit Log (User/Roles/Settings)
confluence_id: 27197992
version: 19
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27197992/WEG-24+Audit+Log+User+Roles+Settings
---

**JIRA-Link:** [WEG-24 – Audit Log (User/Roles/Settings)](https://maierharry.atlassian.net/browse/WEG-24)

## Überblick

Das Modul **Audit Log** (WEG-24) stellt eine revisionssichere Protokollierung aller sicherheitsrelevanten Ereignisse im System bereit.  

Es dient als zentrale Quelle zur Nachvollziehbarkeit von Änderungen an Benutzern, Rollen und Systemeinstellungen.  

Ziel ist die vollständige Transparenz über sicherheitskritische Aktionen und die Erfüllung gesetzlicher Anforderungen (z. B. DSGVO, GoBD, ISO 27001).

## Beschreibung

WEG-24 erfasst sämtliche sicherheitsrelevanten Vorgänge innerhalb der Plattform, unabhängig von Benutzerrolle oder Modul.  

Jeder Eintrag ist eindeutig, unveränderlich und enthält Metadaten zur Nachvollziehbarkeit.  

Das Audit-Log wird mandantengetrennt geführt, sodass jede WEG nur ihre eigenen Audit-Einträge einsehen kann.  

Hauptfunktionen:

- **Ereignisprotokollierung:** Erfassen von Aktionen wie Login/Logout, Rollenänderungen, Passwort-Resets, Änderungen an Sicherheitseinstellungen, Datenexporten oder API-Zugriffen.  

- **Mandanten-Trennung:** Audit-Einträge werden strikt pro Association gespeichert, wodurch Datenschutz und Datenhoheit gewahrt bleiben.  

- **Selbstüberwachung (Self-Audit):** Zugriffe auf das Audit-Log selbst werden ebenfalls protokolliert.  

- **Export-Funktion:** Bereitstellung von Audit-Daten als CSV, JSON oder ZIP-Archiv. Alle Exporte werden mit Prüfsummen und Parametern protokolliert.  

- **Retention & Compliance:** Löschfristen und Aufbewahrungsregeln richten sich nach den Vorgaben aus WEG-26 (Data Privacy) und WEG-54/88 (Retention & Finance Export).  

- **Filterbare UI:** Benutzeroberfläche zur Suche, Filterung und Paginierung großer Datenmengen.  

## Geschäftsregeln & Logik

- Audit-Einträge sind **append-only** – keine nachträgliche Änderung oder Löschung möglich.  

- Jeder Eintrag enthält Zeitstempel, Akteur (Actor), Zielobjekt (Target), Aktion, Ergebnis und Correlation-ID.  

- Audit-Daten werden mandantenbasiert abgelegt und dürfen nicht mandantenübergreifend abrufbar sein.  

- Zugriffe auf Audit-Endpunkte werden mit eigenen Einträgen versehen (&bdquo;Self-Audit&ldquo;).  

- Exporte dürfen nur durch berechtigte Rollen (z. B. Administrator, Auditor) erfolgen.  

- Audit-Einträge müssen nachträglich über Hash-Werte überprüfbar sein (Integritätssicherung).  

## Akzeptanzkriterien

- **Gegeben** ein Benutzer ändert eine Rolle &rarr; **Wenn** die Änderung gespeichert wird &rarr; **Dann** wird ein Audit-Eintrag mit Actor, Target, Aktion und Zeitstempel erstellt.  

- **Gegeben** ein Benutzer ruft das Audit-Log ab &rarr; **Wenn** der Zugriff erfolgt &rarr; **Dann** wird dieser ebenfalls als Audit-Eintrag (&bdquo;Self-Audit&ldquo;) protokolliert.  

- **Gegeben** ein Administrator exportiert das Audit-Log &rarr; **Wenn** der Export abgeschlossen ist &rarr; **Dann** wird der Vorgang mit Parametern und Hash-Wert im Log festgehalten.  

- **Gegeben** ein Benutzer versucht auf das Audit-Log eines anderen Mandanten zuzugreifen &rarr; **Wenn** der Zugriff erfolgt &rarr; **Dann** wird der Zugriff verweigert und im Audit-Log dokumentiert.  

- **Gegeben** ein Audit-Eintrag wird erzeugt &rarr; **Wenn** die Aufbewahrungsfrist abläuft &rarr; **Dann** wird dieser automatisch gemäß WEG-26/54 archiviert oder gelöscht.  

## Nicht-Ziele

- Keine Integration in externe SIEM- oder ELK-Systeme im MVP.  

- Keine Echtzeit-Alarmierung bei verdächtigen Aktivitäten.  

- Keine automatisierte Bewertung von Audit-Einträgen im MVP.  

## Kritische Fälle

- **Hohe Datenmengen:** Das System muss bei großen Audit-Volumina performant bleiben und Exporte in Batches durchführen.  

- **Integritätsverlust:** Eine Änderung oder Löschung eines Audit-Eintrags gilt als Sicherheitsvorfall.  

- **Dateninkonsistenz:** Zeitlich überlappende Ereignisse müssen korrekt gruppiert und sortiert werden.  

- **Fehlende Retention-Regeln:** Ohne gültige Aufbewahrungsfristen darf keine automatische Löschung erfolgen.  

## Abhängigkeiten

-  – Nutzung der zentralen Logging- und Correlation-Mechanismen.  

-  – Anwendung von Retention- und Löschrichtlinien.  

-  – Basistechnologien für Persistenz und Sicherheit.  

-  – Steuerung der Archivierungsprozesse.  

-  – Nutzung gemeinsamer Audit-Strukturen für Finanzdaten.  

## Offene Fragen

- Welche Standard-Retention (z. B. 3, 5 oder 10 Jahre) gilt im MVP?  

- Soll der Export von Audit-Logs durch eine zweite Person bestätigt werden (Vier-Augen-Prinzip)?  

- Sollen Audit-Einträge kryptografisch signiert werden, um Integrität zu gewährleisten?  

## Zukunftserweiterungen

- **Signierte Audit-Einträge** zur Integritätssicherung.  

- **Externe SIEM-Integration** (z. B. ELK, Splunk) für Echtzeit-Analysen.  

- **Alerting-Funktion** bei sicherheitskritischen Ereignissen.  

- **Automatische Audit-Berichte** mit Compliance-Zertifizierung.  

## Verknüpfte Tasks

- [WEG-240 – Audit Endpoints](https://maierharry.atlassian.net/browse/WEG-240) – Implementierung der API-Endpunkte für Abruf, Filterung und Export der Audit-Daten.  

- [WEG-241 – Audit UI (Filters/Export)](https://maierharry.atlassian.net/browse/WEG-241) – Entwicklung der Benutzeroberfläche zur Audit-Einsicht mit Filter- und Exportfunktionen.  

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Audit-Erfassung von Benutzer- und Rollenänderungen, Export als CSV/JSON, mandantengetrennte Speicherung, Self-Audit-Mechanismus.

**Phase 2**

Signierte Audit-Einträge, erweiterte Filter- und Batch-Exporte, optionale SIEM-Anbindung (ELK/Splunk).

**Phase 3**

Echtzeit-Monitoring, Alerting bei verdächtigen Aktivitäten und automatisierte Audit-Reports für Compliance-Nachweise.