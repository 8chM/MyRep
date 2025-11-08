---
title: WEG-80 – Finance Master Data (Categories, Keys, Vendors)
confluence_id: 27329418
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329418/WEG-80+Finance+Master+Data+Categories+Keys+Vendors
---

**JIRA-Link:** [WEG-80 – Finance Master Data (Categories, Keys, Vendors)](https://maierharry.atlassian.net/browse/WEG-80)

## Überblick
Das Modul **Finance Master Data** (WEG-80) verwaltet sämtliche finanzrelevanten Stammdaten einer Eigentümergemeinschaft. Es bildet die Grundlage für alle Buchungs-, Abrechnungs- und Budgetierungsprozesse, indem es Kostenkategorien, Umlageschlüssel und Lieferanten zentral verwaltet und versioniert. Ziel ist eine konsistente, nachvollziehbare Datenbasis, die eine einheitliche Zuordnung von Kosten, Verträgen und Buchungen ermöglicht und somit fehlerfreie Abrechnungen gewährleistet.

## Beschreibung
WEG-80 dient als zentrales Stammdatenregister für alle Finanzprozesse im System. Es verwaltet **Kostenkategorien**, **Umlageschlüssel** und **Vendors (Lieferanten)** in strukturierter und versionierter Form. Die Daten werden periodisiert geführt, um Änderungen rückwirkungsfrei nachvollziehbar zu gestalten. Das Modul ist eng mit der Abrechnung (WEG-87), dem Vertragsmanagement (WEG-57) und der Buchhaltung (WEG-8) verknüpft und bildet damit die gemeinsame semantische Basis für alle finanziellen Abläufe.

Hauptfunktionen:

- **Kategorienmanagement:** Anlage und Pflege von Kostenkategorien (z. B. Allgemeinstrom, Heizung, Versicherung) mit eindeutigen Codes, Beschreibungen und Versionierung.

- **Umlageschlüsselverwaltung:** Definition variabler und fixer Verteilungsschlüssel nach MEA, m&sup2;, Verbrauch oder Einheiten; Änderungen gelten immer nur für zukünftige Perioden.

- **Vendor-Management:** Verwaltung von Lieferanten mit Stammdaten (Name, IBAN, Steuernummer, Ansprechpartner) und Zuordnung zu Verträgen (WEG-57).

- **Periodenabhängigkeit:** Automatische Versionslogik verhindert rückwirkende Änderungen in abgeschlossenen Perioden.

- **CSV-Import:** Optionale Möglichkeit zur Massenerfassung oder Migration großer Stammdatenbestände.

- **Audit-Trail:** Protokollierung aller Änderungen mit Benutzer, Zeitstempel und Änderungsgrund im zentralen Audit-Log (WEG-24).

- **Validierung & Konsistenz:** Sicherstellung eindeutiger Codes, gültiger Schlüsselverknüpfungen und konsistenter Vendor-Zuordnungen.

## Geschäftsregeln & Logik
- Jede Kategorie, jeder Schlüssel und jeder Vendor muss eindeutig benannt und identifizierbar sein.

- Änderungen werden immer versioniert und gelten ausschließlich für neue Perioden.

- Gesperrte Perioden dürfen nicht verändert werden.

- Vendors können auf &bdquo;inaktiv&ldquo; gesetzt werden, wirken sich jedoch nicht rückwirkend auf bestehende Verträge aus.

- Alle Stammdatenänderungen werden im Audit-Log dokumentiert und sind nachvollziehbar.

## Akzeptanzkriterien
- **Gegeben** eine neue Kategorie &bdquo;Allgemeinstrom&ldquo; wird mit Umlageschlüssel &bdquo;MEA&ldquo; angelegt &rarr; **Wenn** sie gespeichert wird &rarr; **Dann** ist sie in Abrechnung und Wirtschaftsplan verfügbar und korrekt zugeordnet.

- **Gegeben** ein Vendor wird einem Vertrag (WEG-57) zugeordnet &rarr; **Wenn** der Vertrag aktiviert wird &rarr; **Dann** fließen die daraus resultierenden Kosten automatisch in Budget und Abrechnung ein.

- **Gegeben** eine Kategorie wird in einer gesperrten Periode geändert &rarr; **Wenn** der Benutzer die Änderung speichert &rarr; **Dann** verhindert das System den Vorgang mit einem Hinweis auf die Periodensperre.

- **Gegeben** ein Vendor wird auf &bdquo;inaktiv&ldquo; gesetzt &rarr; **Wenn** ein neuer Vertrag erstellt wird &rarr; **Dann** steht dieser Vendor nicht mehr zur Auswahl.

## Nicht-Ziele
- Keine automatische Synchronisation mit externen Lieferantendatenbanken im MVP.

- Kein Import oder Export zu ERP-Systemen in Phase 1.

- Keine Hierarchisierung von Kategorien oder automatisierte Schlüsselvorschläge im MVP.

## Kritische Fälle
- **Doppelte Codes:** Mehrfach vorhandene Kategoriebezeichnungen müssen blockiert und gemeldet werden.

- **Schlüsseländerungen in gesperrten Perioden:** System muss diese Änderungen verhindern.

- **Fehlerhafte Vendor-Zuordnung:** Ungültige oder inaktive Vendors dürfen nicht in laufende Buchungen eingebunden werden.

- **Fehlende Validierung:** Unvollständige Stammdaten dürfen keine Freigabe erhalten.

## Abhängigkeiten
- WEG-24 – Audit Log – Dokumentiert alle Änderungen und Versionierungen.

- WEG-57 – Contract Management – Verträge referenzieren Vendors und Kostenkategorien.

- WEG-87 – Accounting & Billing – Nutzt Kategorien und Umlageschlüssel für Kostenverteilungen.

- WEG-8 – Finance & Banking – Integration in die Buchungslogik.

## Offene Fragen
- Soll es einen Systemkatalog mit Standardkategorien (z. B. Heizung, Strom, Wartung) geben?

- Sollen Vendors auch für Eigentümer nutzbar sein (z. B. Handwerker für Sondereigentum)?

- Ist eine grafische Gruppierung oder Hierarchisierung von Kategorien geplant?

## Zukunftserweiterungen
- **Hierarchische Kategorienstruktur:** Gruppierung verwandter Kostenarten für übersichtliche Berichte.

- **Externer Stammdatensync:** Automatische Aktualisierung von Lieferanteninformationen.

- **Erweiterte Reports:** Nutzungshäufigkeit, ungenutzte Kategorien, Zuordnungsstatistiken.

- **Importautomatisierung:** Regelmäßige CSV-Synchronisierung aus Fremdsystemen.

## Verknüpfte Tasks
- [WEG-800 – Categories, Allocation Keys, Vendors](https://maierharry.atlassian.net/browse/WEG-800) – Aufbau des zentralen Stammdatenregisters mit Versionierung und Periodenlogik.

- [WEG-801 – CSV Import & Validation](https://maierharry.atlassian.net/browse/WEG-801) – Import-Mechanismen für Kategorien und Vendoren.

- [WEG-802 – Vendor Activation & History](https://maierharry.atlassian.net/browse/WEG-802) – Verwaltung von Vendor-Status und Historie.

- [WEG-803 – Category Usage Reports](https://maierharry.atlassian.net/browse/WEG-803) – Auswertung der Verwendung von Kostenkategorien.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Stammdatenverwaltung für Kategorien, Umlageschlüssel und Vendors mit Versionierung, Audit-Trail und Formularerfassung.

**Phase 2**

CSV-Import, Validierung, erweiterte Reports und Konsistenzprüfungen.

**Phase 3**

Externer Stammdatensync, hierarchische Kategorien, Automatisierung von Aktualisierungen.