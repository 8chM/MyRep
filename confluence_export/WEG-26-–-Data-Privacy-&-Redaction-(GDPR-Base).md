---
title: WEG-26 – Data Privacy & Redaction (GDPR Base)
confluence_id: 27656622
version: 23
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27656622/WEG-26+Data+Privacy+Redaction+GDPR+Base
---

**JIRA-Link:** [WEG-26 – Data Privacy & Redaction (GDPR Base)](https://maierharry.atlassian.net/browse/WEG-26)

## Überblick

Das Modul **Data Privacy & Redaction** (WEG-26) stellt die datenschutzrechtliche Grundlage des WEG Management Systems dar und sorgt für die technische Umsetzung der DSGVO.  

Es ermöglicht die Identifikation, Verwaltung und Kontrolle personenbezogener Daten über alle Module hinweg.  

Ziel ist es, Datenschutzprozesse wie Auskunft, Löschung, Anonymisierung und Aufbewahrung konsistent, revisionssicher und rechtssicher zu gestalten, ohne den laufenden Betrieb zu beeinträchtigen.

## Beschreibung

WEG-26 integriert systemweite Datenschutzmechanismen, die automatisch mit sämtlichen Datenflüssen interagieren.  

Das Modul sorgt für Transparenz über personenbezogene Daten, überwacht deren Nutzung und gewährleistet die Einhaltung von Aufbewahrungs- und Löschrichtlinien.

Hauptfunktionen:

- **Subject Index & Data Catalog:** Erfassung sämtlicher Datenquellen und Zuordnung zu betroffenen Personen, inklusive Kategorie, Zweck und Speicherort.  

- **DSAR Export:** Bereitstellung personenbezogener Daten gemäß Art. 15 DSGVO als strukturiertes JSON-/ZIP-Archiv mit allen zugehörigen Dokumenten.  

- **Redaction & Pseudonymization:** Anonymisierung oder Schwärzung sensibler Inhalte in Dokumenten, Nachrichten und Protokollen anhand vordefinierter Regeln.  

- **Erasure Workflow & Legal Holds:** Automatisierte Löschprozesse basierend auf Retention-Regeln mit Ausnahme von gesperrten Datensätzen (Legal Holds).  

- **Retention Policies Engine:** Verwaltung von Aufbewahrungsfristen pro Datenkategorie mit automatischer Ausführung und Protokollierung.  

- **Privacy Access Logging:** Protokollierung jedes Zugriffs auf personenbezogene Daten mit Benutzer, Zweck und Zeitpunkt.  

- **Privacy Settings UI:** Konfigurationsoberfläche zur Verwaltung von Datenschutzrichtlinien, Fristen und DSAR-Anfragen.  

- **API Enforcement Hooks:** Technische Durchsetzung von Datenschutzrichtlinien auf API-Ebene.  

- **Audit Reports:** Erstellung regelmäßiger Berichte über DSAR-Anfragen, Löschvorgänge und Datenschutzaktivitäten.  

## Geschäftsregeln & Logik

- Der Zugriff auf personenbezogene Daten erfolgt strikt nach dem Prinzip der minimalen Rechtevergabe (&bdquo;Least Privilege&ldquo;).  

- Jeder Export, jede Redaktion und jede Löschung wird vollständig im Audit-Log (WEG-24) dokumentiert.  

- Automatische Löschungen dürfen nur erfolgen, wenn kein aktiver Legal Hold besteht.  

- Datenschutzprozesse sind transaktionssicher, asynchron und dürfen den Systembetrieb nicht unterbrechen.  

- Retention-Regeln werden zentral verwaltet und gelten mandantenspezifisch.  

## Akzeptanzkriterien

- **Gegeben** eine DSAR-Anfrage wurde bestätigt &rarr; **Wenn** der Export gestartet wird &rarr; **Dann** enthält das Paket alle personenbezogenen Daten der betroffenen Person, einschließlich Dokumente und Logs, und wird revisionssicher archiviert.  

- **Gegeben** ein Dokument hat seine Aufbewahrungsfrist erreicht &rarr; **Wenn** der Retention-Workflow ausgeführt wird &rarr; **Dann** wird es gemäß Regel anonymisiert oder gelöscht und im Privacy-Audit protokolliert.  

- **Gegeben** ein Benutzer greift auf sensible Daten zu &rarr; **Wenn** der Zugriff erfolgt &rarr; **Dann** wird dieser im Privacy Access Log mit Akteur, Zweck und Zeitpunkt erfasst.  

- **Gegeben** ein Legal Hold ist aktiv &rarr; **Wenn** der Löschlauf ausgeführt wird &rarr; **Dann** werden alle betroffenen Datensätze ausgenommen und der Grund dokumentiert.  

- **Gegeben** ein API-Aufruf verletzt eine Datenschutzrichtlinie &rarr; **Wenn** der Enforcement-Hook dies erkennt &rarr; **Dann** wird der Zugriff blockiert und ein Audit-Eintrag erstellt.  

## Nicht-Ziele

- Keine Anbindung externer Datenschutz- oder DLP-Systeme im MVP.  

- Keine juristische Prüfung oder automatische Rechtsauslegung.  

- Kein Self-Service-Portal für Eigentümer im MVP.  

## Kritische Fälle

- **Unvollständige DSAR-Exporte:** Fehlende Datenquellen werden gekennzeichnet und gemeldet.  

- **Fehlerhafte Redaktion:** Ungenaue Schwärzungsregeln können Datenschutzverletzungen verursachen.  

- **Retention-Konflikte:** Bei Widerspruch zwischen Löschregel und Legal Hold gilt der Hold als vorrangig.  

- **Batch-Löschungen:** Große Löschvorgänge müssen kontrolliert und ressourcenschonend ausgeführt werden.  

## Abhängigkeiten

-  – Umsetzung des Least-Privilege-Prinzips.  

-  – Speicherung aller Datenschutzaktionen.  

-  – Umsetzung von Lösch- und Redaktionsregeln in Dokumenten.  

-  – Synchronisierung von Retention-Regeln für Finanzdaten.  

-  – Nutzung der zentralen Logging-Infrastruktur für Datenschutzprozesse.  

## Offene Fragen

- Wie granular sollen Aufbewahrungsfristen im MVP gepflegt werden (global, pro Kategorie, pro WEG)?  

- Welche zusätzlichen Metadaten sollen DSAR-Exporte enthalten?  

- Soll es Benachrichtigungen bei DSAR-Fortschritt oder Löschaktionen geben?  

## Zukunftserweiterungen

- **KI-gestützte Erkennung sensibler Inhalte** in Dokumenten und Freitextfeldern.  

- **Internationale Datenschutzunterstützung** (CCPA, LGPD).  

- **Self-Service-Portal** für Betroffenenanfragen und Exportanforderungen.  

- **Erweiterte Echtzeit-Filterung** sensibler Datenströme über API und UI.  

## Verknüpfte Tasks

- [WEG-260 – Subject Index & Data Catalog](https://maierharry.atlassian.net/browse/WEG-260) – Erfassung personenbezogener Datenquellen und Kategorien.  

- [WEG-261 – DSAR Export (JSON/ZIP)](https://maierharry.atlassian.net/browse/WEG-261) – Generierung vollständiger Datenschutzpakete.  

- [WEG-262 – Redaction & Pseudonymization](https://maierharry.atlassian.net/browse/WEG-262) – Umsetzung von Anonymisierungs- und Schwärzungslogiken.  

- [WEG-263 – Erasure Workflow & Legal Holds](https://maierharry.atlassian.net/browse/WEG-263) – Automatische Löschungen und Sperrverwaltung.  

- [WEG-264 – Retention Policies Engine](https://maierharry.atlassian.net/browse/WEG-264) – Verwaltung und Durchsetzung von Fristen und Regeln.  

- [WEG-265 – Privacy Access Logging](https://maierharry.atlassian.net/browse/WEG-265) – Protokollierung von Zugriffen auf personenbezogene Daten.  

- [WEG-266 – Privacy Settings UI](https://maierharry.atlassian.net/browse/WEG-266) – Konfiguration von Datenschutzrichtlinien durch Administratoren.  

- [WEG-267 – API Enforcement Hooks](https://maierharry.atlassian.net/browse/WEG-267) – Durchsetzung von Datenschutzregeln auf API-Ebene.  

- [WEG-268 – Export Package Templates](https://maierharry.atlassian.net/browse/WEG-268) – Vorlagen für DSAR- und Compliance-Pakete.  

- [WEG-269 – Privacy Audit Reports](https://maierharry.atlassian.net/browse/WEG-269) – Erstellung periodischer Datenschutzberichte.  

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Erfassung personenbezogener Daten, DSAR-Export, Pseudonymisierung, Lösch- und Retention-Workflows, Zugriff-Logging, Privacy-UI und API-Enforcement.

**Phase 2**

KI-gestützte Datenklassifikation, internationale Datenschutzrichtlinien, erweiterte Maskierungslogik, detaillierte Audit-Berichte.

**Phase 3**

Self-Service-Portal, automatisierte Risikoanalysen, Echtzeit-Überwachung und Integration externer Compliance-Systeme.