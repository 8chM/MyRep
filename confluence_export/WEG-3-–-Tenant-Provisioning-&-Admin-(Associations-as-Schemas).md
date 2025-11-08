---
title: WEG-3 – Tenant Provisioning & Admin (Associations as Schemas)
confluence_id: 27460042
version: 15
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27460042/WEG-3+Tenant+Provisioning+Admin+Associations+as+Schemas
---

**JIRA-Link:** [WEG-3 – Tenant Provisioning & Admin (Associations as Schemas)](https://maierharry.atlassian.net/browse/WEG-3)

## Beschreibung / Kernzweck

Das Modul **WEG-3 – Tenant Provisioning & Administration** bildet das organisatorische Rückgrat des WEG Management Systems (WMS). Es verwaltet alle Wohnungseigentümergemeinschaften (WEGs) als eigenständige Mandanten (&bdquo;Tenants&ldquo;) und sorgt für eine klare Trennung von Daten, Benutzern und Konfigurationen. Jede WEG erhält dabei ein eigenes Datenbankschema, wodurch maximale Sicherheit, Stabilität und Skalierbarkeit gewährleistet wird.

Ziel des Moduls ist es, WEGs effizient anlegen, verwalten, sichern und exportieren zu können – sowohl für den produktiven Betrieb als auch für Entwicklungs- und Testzwecke. Die Tenant-Verwaltung bildet die Basis, auf der sämtliche weiteren Fachmodule (z. B. Finanzen, Eigentümerverwaltung, Meetings, DMS) arbeiten.

## Inhalte

Untermodul

Kurzbeschreibung

[WEG-30 – Association Registry & Provisioning (Schema Create)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Legt neue WEGs im System an und erstellt automatisch ein eigenes Datenbankschema.

[WEG-31 – Database Endpoint Management (Multi-DB)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Verwaltet und steuert die Zuordnung von WEGs zu Datenbanken und Verbindungsendpunkten.

[WEG-32 – Schema Provisioning Service (Seeding)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Initialisiert neue WEGs mit Standardwerten, Rollen, Einstellungen und Basiskonfigurationen.

[WEG-33 – Association Admin Panel (Enable/Disable, Branding)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Bietet eine Verwaltungsoberfläche zur Aktivierung, Deaktivierung und Konfiguration von WEGs.

[WEG-34 – Data Export (JSON/CSV)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Ermöglicht den Export aller Daten einer WEG, z. B. zur Archivierung oder Systemübertragung.

[WEG-35 – Backup/Restore (Dev-first)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Erstellt Sicherungen einzelner Mandanten und unterstützt Wiederherstellungen in Testumgebungen.

[WEG-36 – Migration Orchestrator (Dry-Run, Health Matrix)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Führt strukturierte Schema- und Versionsmigrationen durch, inklusive Health-Checks und Rollback-Funktionen.

## Geschäftslogik

Das Modul steuert die gesamte Verwaltung des Lebenszyklus einer WEG – von der initialen Anlage bis hin zu Migrationen und Backups.

- **Mandantenanlage:** Beim Erstellen einer neuen WEG wird automatisch ein eigenes Schema in der Datenbank angelegt, das alle relevanten Tabellen und Standardkonfigurationen enthält.

- **Mehrmandantenfähigkeit:** Jeder Mandant ist logisch und technisch isoliert. Daten anderer WEGs sind weder einsehbar noch verknüpft.

- **Verwaltung und Konfiguration:** Über das Admin-Panel (WEG-33) können WEGs aktiviert, deaktiviert, dupliziert oder gelöscht werden.

- **Branding und Lokalisierung:** Jede WEG kann individuelle Farben, Logos und Spracheinstellungen erhalten.

- **Migrationen:** Systemupdates und Schemaänderungen erfolgen über den Migration Orchestrator (WEG-36), der alle Mandanten prüft und sicher aktualisiert.

- **Backups und Wiederherstellung:** Daten einzelner WEGs können gezielt gesichert oder in einer Entwicklungsumgebung wiederhergestellt werden.

- **Exportfunktionen:** WEGs können als vollständiges JSON- oder CSV-Paket exportiert werden, inklusive Konfiguration, Benutzern und Dokumentenverknüpfungen.

- **Audit und Nachvollziehbarkeit:** Alle Änderungen an WEGs (z. B. Aktivierung, Migration, Löschung) werden im Audit-Log (WEG-24) dokumentiert. Damit gewährleistet WEG-3 eine kontrollierte, revisionssichere Verwaltung und bildet die Grundlage für die Mandantenstruktur des gesamten Systems.

## Akzeptanzkriterien

- **Gegeben** ein Administrator legt eine neue WEG an &rarr; **Wenn** der Provisioning-Prozess abgeschlossen ist &rarr; **Dann** wird automatisch ein separates Datenbankschema erstellt und im Registry-Eintrag hinterlegt.  

- **Gegeben** eine WEG ist deaktiviert &rarr; **Wenn** sie im Admin-Panel reaktiviert wird &rarr; **Dann** werden alle zugehörigen Benutzer, Daten und Dienste wieder freigegeben.  

- **Gegeben** ein Backup-Prozess wird gestartet &rarr; **Wenn** er erfolgreich abgeschlossen ist &rarr; **Dann** steht eine vollständige Sicherung der WEG-Daten als ZIP-Archiv zur Verfügung.  

- **Gegeben** eine Migration steht an &rarr; **Wenn** der Orchestrator sie ausführt &rarr; **Dann** werden alle betroffenen WEGs geprüft, migriert und im Health-Status protokolliert.  

- **Gegeben** ein Datenexport wird initiiert &rarr; **Wenn** der Export abgeschlossen ist &rarr; **Dann** enthält das Paket alle zugehörigen Daten, Rollen, Konfigurationen und Logs der WEG.

## Nicht-Ziele

- Keine manuelle Bearbeitung von Datenbanken oder Schemas außerhalb des Systems.

- Kein globaler Zugriff auf mehrere WEGs gleichzeitig (nur über Administratorrechte).

- Keine automatische Massenmigration von WEGs im MVP (nur gezielte Updates).

- Keine externe Anbindung an ERP- oder Drittverwaltungssysteme im MVP.

## Kritische Fälle

- **Fehlerhafte Migration:** Unterbrochene Updates dürfen keine inkonsistenten Zustände erzeugen; Rollback muss garantiert sein.

- **Doppelte Registrierungen:** Eine WEG darf nur einmalig im Directory existieren; doppelte Namen oder IDs sind zu verhindern.

- **Backup-Fehler:** Fehlgeschlagene Sicherungen müssen sofort gemeldet und protokolliert werden.

- **Versehentliche Deaktivierung:** Eine deaktivierte WEG darf keine Hintergrundprozesse (z. B. Scheduler-Jobs) mehr ausführen.

- **Inkompatible Versionen:** Schema-Versionen müssen mit der Applikationsversion übereinstimmen; sonst ist ein Upgrade zu blockieren.

## Abhängigkeiten

- WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite): Bereitstellung der technischen Architektur und Schichtenstruktur.

- WEG-2 – Identity & Access (Auth, RBAC, Invitations): Verwaltung der Benutzer und Berechtigungen pro Mandant.

- WEG-13 – Control-Plane & Connection Routing: Routing von Anfragen an das jeweilige WEG-Schema.

- WEG-24 – Audit Log (User/Roles/Settings): Protokollierung sämtlicher administrativer Änderungen.

## Offene Fragen

- Soll die Erstellung neuer WEGs langfristig auch automatisiert über eine API möglich sein?

- Wie granular sollen Backups konfigurierbar sein (vollständig, selektiv oder differenziell)?

- Sollen deaktivierte WEGs automatisch archiviert oder manuell gelöscht werden?

- Wie soll die Datenversionierung über mehrere Releases hinweg gehandhabt werden?

## Zukunftserweiterungen

- **Automatische Mandanten-Skalierung:** Dynamische Ressourcenverteilung bei hoher Auslastung.

- **Mandantenübergreifende Verwaltung:** Zusammenführung oder Gruppierung mehrerer kleiner WEGs.

- **Health-Dashboards:** Zentrale Übersicht über alle WEGs mit Status, Speicherverbrauch und Performancewerten.

- **Self-Service Onboarding:** Option für Endkunden, eigene WEGs selbstständig anzulegen und zu verwalten.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Erstellung, Verwaltung und Export von WEGs, Aktivierung/Deaktivierung, Backups, Migrationen und vollständige Auditierung aller Mandantenaktionen.

**Phase 2**

Automatisierte Migrationen, API-Provisioning für neue Mandanten, Health-Checks, Reporting und Self-Service-Verwaltung.

**Phase 3**

Intelligente Mandantenverwaltung mit automatischer Skalierung, KI-basierter Konsistenzprüfung und Integration externer Systeme.