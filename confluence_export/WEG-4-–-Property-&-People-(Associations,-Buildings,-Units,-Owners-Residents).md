---
title: WEG-4 – Property & People (Associations, Buildings, Units, Owners/Residents)
confluence_id: 27722249
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722249/WEG-4+Property+People+Associations+Buildings+Units+Owners+Residents
---

**JIRA-Link:** [WEG-4 – Property & People (Associations, Buildings, Units, Owners/Residents)](https://maierharry.atlassian.net/browse/WEG-4)

## Beschreibung / Kernzweck

Das Modul **WEG-4 – Property & People** bildet das Fundament für die gesamte Verwaltung von Immobilien- und Personenstammdaten im WEG Management System (WMS). Es verknüpft Gebäude, Einheiten, Eigentümer und Bewohner in einer strukturierten, nachvollziehbaren und mandantenspezifischen Datenbasis. Alle weiteren Module – etwa Dokumentenmanagement, Finanzen, Kommunikation oder Eigentümerversammlungen – greifen auf diese zentrale Datenquelle zu.

Ziel des Moduls ist es, die komplexen Beziehungen innerhalb einer Eigentümergemeinschaft übersichtlich, rechtssicher und versionsgeführt abzubilden. Es sorgt dafür, dass Besitz- und Nutzungsverhältnisse über Zeiträume hinweg vollständig nachvollziehbar bleiben, dass Miteigentumsanteile (MEA) konsistent berechnet werden und dass jede Einheit eindeutig einem Gebäude und einem oder mehreren Eigentümern zugeordnet ist.

## Inhalte

Untermodul

Kurzbeschreibung

[WEG-40 – Association Details & Buildings](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Verwaltung der Stammdaten einer WEG und ihrer Gebäude (Adresse, Baujahr, Energieeffizienz, Gebäudetyp und Basisdokumente).

[WEG-41 – Units CRUD with Time-Bound Occupancy](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Anlage, Änderung und Versionierung von Nutzungseinheiten (Wohnungen, Gewerbe, Stellplätze) mit zeitlich begrenzter Gültigkeit.

[WEG-42 – Ownership & Residency History](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Historienverwaltung von Eigentums- und Bewohnerwechseln; stellt sicher, dass alle Änderungen nachvollziehbar und lückenlos dokumentiert sind.

[WEG-43 – Unit Merge/Split Workflow (Cut-off Validations)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Verwaltung von baulichen Änderungen wie Zusammenführungen oder Aufteilungen von Einheiten mit vollständiger Datenübernahme.

[WEG-44 – Search & Filters (Units/Owners)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Such- und Filterfunktionen für Gebäude, Einheiten und Personen, basierend auf Rollen und Berechtigungen.

[WEG-45 – CSV Import for Units/Ownership](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Import vorhandener Stammdaten über CSV mit Plausibilitätsprüfungen und automatischer Dubletten-Erkennung.

[WEG-46 – Validation Rules (MEA, sqm, constraints)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Einheitliche Prüfmechanismen für Miteigentumsanteile, Flächen, Adressformate und Pflichtangaben.

[WEG-47 – Advisory Board Integration (Beirat)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Verwaltung der Beiratsstruktur inklusive Mitglieder, Amtszeiten, Zuständigkeiten und Rollenverknüpfung mit Eigentümern.

## Geschäftslogik

Das Modul bildet die zentrale Geschäftslogik für alle Stammdatenvorgänge:

- **Strukturierte Datenhaltung:** Jede WEG besteht aus mindestens einem Gebäude mit zugeordneten Einheiten. Jede Einheit besitzt klar definierte Merkmale (Fläche, MEA, Nutzungstyp, Adresse).

- **Eigentumsbeziehungen:** Jede Einheit ist einem oder mehreren Eigentümern zugeordnet. Bei Miteigentum werden die Anteile prozentual oder nach MEA-Werten hinterlegt.

- **Bewohnerverwaltung:** Neben Eigentümern können Bewohner (Mieter, Angehörige) separat gepflegt werden; zeitliche Gültigkeiten sichern eine korrekte Historie.

- **Historisierung:** Alle Änderungen – etwa Eigentümerwechsel, Flächenkorrekturen oder Umbauten – werden versioniert gespeichert. Alte Datensätze bleiben archiviert, um rechtliche Nachvollziehbarkeit zu gewährleisten.

- **Validierung & Konsistenz:** Automatische Prüfungen stellen sicher, dass MEA-Summen korrekt sind (1000/1000), Flächenangaben konsistent bleiben und keine Überschneidungen bei Zeiträumen auftreten.

- **Such- und Filterfunktionen:** Eigentümer, Bewohner und Einheiten können nach Namen, Adressen, MEA oder Status durchsucht werden; Zugriffe sind rollenbasiert beschränkt.

- **Import & Export:** Bestehende Daten können strukturiert importiert oder exportiert werden, um Migrationen aus Altbeständen zu ermöglichen.

- **Audit-Sicherheit:** Alle Änderungen werden mit Benutzer, Zeitstempel und Änderungsgrund protokolliert. Das Audit-Log (WEG-24) stellt die Revisionsfähigkeit sicher.

- **Beiratsintegration:** Beiratsmitglieder werden direkt mit Eigentümern verknüpft; Amtszeiten und Aufgabenbereiche werden automatisch überwacht und dokumentiert.

## Akzeptanzkriterien

- **Gegeben** eine neue Einheit wird angelegt &rarr; **Wenn** sie gespeichert wird &rarr; **Dann** wird automatisch ein MEA-Anteil vergeben und die Gesamtsumme validiert.  

- **Gegeben** ein Eigentümerwechsel erfolgt &rarr; **Wenn** die Änderung bestätigt wird &rarr; **Dann** werden alle Beziehungen (Einheiten, MEA, Rollen) aktualisiert und im Audit-Log dokumentiert.  

- **Gegeben** ein Beirat wird neu gewählt &rarr; **Wenn** die Amtszeit beginnt &rarr; **Dann** werden die neuen Rollen aktiviert und die alten automatisch beendet.  

- **Gegeben** ein CSV-Import wird ausgeführt &rarr; **Wenn** Datensätze fehlerhaft sind &rarr; **Dann** werden diese mit detaillierten Hinweisen zur Korrektur markiert.  

- **Gegeben** eine Suche nach einem Eigentümer &rarr; **Wenn** Filter angewendet werden &rarr; **Dann** werden nur Daten angezeigt, für die der Benutzer berechtigt ist.

## Nicht-Ziele

- Keine vollständige CRM-Funktion (z. B. Vertriebsprozesse oder Interessentenverwaltung).

- Keine direkte Anbindung an Grundbuch- oder Katasterämter im MVP.

- Keine automatische Geodatenvalidierung (z. B. Adresskoordinaten).

- Keine automatischen Nachfolgeprozesse bei Todesfällen oder Erbfolgen.

## Kritische Fälle

- **MEA-Fehler:** Falsche Summen oder Rundungsfehler müssen sofort gemeldet werden; Speicherung ist zu verhindern.

- **Verwaiste Einheiten:** Einheiten ohne Eigentümer dürfen nicht existieren; das System erzwingt Korrektur vor Freigabe.

- **Doppelte Eigentümerdatensätze:** Beim Import werden Dubletten erkannt und müssen manuell zusammengeführt werden.

- **Zeitliche Überschneidungen:** Historische und aktuelle Eigentums- oder Bewohnerdaten dürfen sich nicht überlappen.

- **Fehlerhafte Rollenverknüpfung:** Beiratsrollen dürfen nicht gleichzeitig mehrfach vergeben werden.

## Abhängigkeiten

- WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite): Stellt technische Basis und Logging bereit.

- WEG-2 – Identity & Access (Auth, RBAC, Invitations): Verwaltet Benutzer und Zugriffsrechte.

- WEG-3 – Tenant Provisioning & Admin (Associations as Schemas): Liefert die Mandantenstruktur.

- WEG-24 – Audit Log (User/Roles/Settings): Erfasst Änderungen an Eigentums-, Einheiten- und Bewohnerdaten.

- WEG-87 – Accounting & Billing (Service Charges, Allocation, Budget/WP): Nutzt Eigentümer- und Flächeninformationen für Umlagen.

## Offene Fragen

- Wie sollen Gemeinschaften bürgerlichen Rechts (GbR) oder Erbengemeinschaften abgebildet werden?

- Welche Rundungsregeln gelten für MEA-Berechnungen?

- Soll ein optionaler Adress-Validierungsservice (z. B. Google Maps API) in späteren Phasen integriert werden?

- Müssen Beirat- und Eigentümerdaten bei Eigentümerwechseln automatisch synchronisiert werden?

## Zukunftserweiterungen

- **Grundbuch-Integration:** Automatischer Import offizieller Eigentümerdaten.

- **Erweiterte CRM-Funktion:** Nachverfolgung von Kommunikation und Aufgaben auf Personenebene.

- **Geodaten-Anbindung:** Integration von Karten und automatischer Adressprüfung.

- **Mobile Oberfläche:** Zugriff auf Stammdaten für Verwalter über mobile Endgeräte.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Verwaltung von Gebäuden, Einheiten, Eigentümern und Bewohnern mit MEA-Validierung, Historisierung, CSV-Import und Audit-Protokollierung.

**Phase 2**

Erweiterte CRM-Funktionen, Grundbuch-Anbindung und erweiterte Beiratsverwaltung.

**Phase 3**

Geodaten-Integration, mobile Nutzung, intelligente Validierung und KI-gestützte Dublettenerkennung.