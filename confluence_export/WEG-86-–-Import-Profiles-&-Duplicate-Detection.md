---
title: WEG-86 – Import Profiles & Duplicate Detection
confluence_id: 27591444
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27591444/WEG-86+Import+Profiles+Duplicate+Detection
---

**JIRA-Link:** [WEG-86 – Import Profiles & Duplicate Detection](https://maierharry.atlassian.net/browse/WEG-86)

## Überblick
Das Modul **Import Profiles & Duplicate Detection** (WEG-86) erweitert die Finanz-Importlogik (WEG-82) um wiederverwendbare Importprofile und eine integrierte Deduplikationsprüfung. Es ermöglicht die Verwaltung von Mapping-Vorlagen für CSV- und MT940-Dateien und reduziert den manuellen Aufwand bei wiederkehrenden Bankimporten erheblich. Zudem schützt es vor doppelten Transaktionen, indem es automatische Prüfungen während des Imports durchführt. Ziel ist es, die Importprozesse effizienter, konsistenter und sicherer zu gestalten.

## Beschreibung
WEG-86 ermöglicht die Erstellung, Speicherung und Versionierung von Importprofilen, die definieren, wie externe Bankdaten in das interne System übernommen werden. Jedes Profil enthält Feldzuordnungen (z. B. Datum, Betrag, IBAN, Verwendungszweck) sowie Formatdefinitionen (Trennzeichen, Dezimalstellen, Datumsformate). Beim Import prüft das System automatisch, ob ein passendes Profil existiert, und übernimmt die gespeicherten Zuordnungen. Zusätzlich vergleicht ein Deduplikationsmechanismus neue Transaktionen mit bestehenden Datensätzen, um doppelte Einträge zu verhindern.

Hauptfunktionen:

- **Profilverwaltung:** Anlegen, Bearbeiten, Löschen und Versionieren von Importprofilen pro WEG.

- **Spalten-Mapping:** Definition der Zuordnung zwischen CSV-/MT940-Spalten und internen Feldern.

- **Standardprofile:** Markierung eines Profils als Standard für bestimmte Konten oder Dateitypen.

- **Deduplikation:** Automatische Prüfung auf doppelte Buchungen anhand von Betrag, Datum, IBAN und optionaler Transaktions-ID.

- **Warnmeldungen:** Doppelte Einträge werden markiert und müssen vom Verwalter bestätigt oder ausgeschlossen werden.

- **Versionierung:** Änderungen an Profilen werden revisionssicher im Audit-Log (WEG-24) dokumentiert.

- **Import-Kompatibilität:** Nahtlose Integration mit WEG-82 (Banking Inbound) für automatisierte Abläufe.

## Geschäftsregeln & Logik
- Profile sind immer WEG-spezifisch gespeichert; globale Profile sind nicht vorgesehen.

- Eine Kombination aus Betrag + Datum + IBAN innerhalb von 24 Stunden gilt als potenzielles Duplikat.

- Jede Profiländerung erzeugt eine neue Version und wird im Audit-Log erfasst.

- Importvorgänge mit Deduplikationswarnungen müssen manuell bestätigt werden.

- Es darf nur ein Standardprofil pro Konto existieren.

## Akzeptanzkriterien
- **Gegeben** ein Verwalter hat ein Importprofil &bdquo;Sparkasse Hausgeldkonto&ldquo; gespeichert &rarr; **Wenn** eine neue CSV-Datei importiert wird &rarr; **Dann** werden alle Spalten automatisch zugeordnet und eine Deduplikationsprüfung durchgeführt.

- **Gegeben** ein Import enthält doppelte Transaktionen &rarr; **Wenn** der Dedupe-Check aktiv ist &rarr; **Dann** werden die betreffenden Zeilen markiert und müssen bestätigt oder übersprungen werden.

- **Gegeben** ein Profil wird bearbeitet &rarr; **Wenn** der Benutzer Änderungen speichert &rarr; **Dann** wird automatisch eine neue Version erzeugt und im Audit-Log dokumentiert.

- **Gegeben** mehrere Profile existieren &rarr; **Wenn** eines als Standard markiert wird &rarr; **Dann** wird dieses automatisch bei künftigen Importen vorausgewählt.

- **Gegeben** ein Benutzer ohne Berechtigung versucht, ein Profil zu löschen &rarr; **Wenn** der Vorgang gestartet wird &rarr; **Dann** verweigert das System die Aktion und zeigt eine Fehlermeldung an.

## Nicht-Ziele
- Keine KI-basierte Profil-Erkennung oder Spalten-Mapping im MVP.

- Keine globale Profilfreigabe zwischen verschiedenen WEGs.

- Keine automatische Erkennung von Fuzzy-Duplikaten in Phase 1.

## Kritische Fälle
- **Falsches Mapping:** Fehlerhafte Zuordnungen können zu fehlerhaften Buchungen führen – System muss Warnungen ausgeben.

- **Unvollständige Profile:** Import ohne vollständige Feldzuordnung ist zu blockieren.

- **Mehrfache Standardprofile:** Doppelte Markierungen sind nicht zulässig.

- **Fehlender Dedupe-Check:** Wenn deaktiviert, müssen Importe mit Warnhinweis bestätigt werden.

## Abhängigkeiten
- WEG-8 – Finance & Banking – Übergeordnetes Modul für Finanzprozesse.

- WEG-82 – Banking Inbound – Quelle der zu importierenden Transaktionen.

- WEG-2 – Identity & Access – Berechtigungssteuerung für Profilmanagement.

- WEG-24 – Audit Log – Nachvollziehbarkeit aller Profiländerungen und Importe.

## Offene Fragen
- Soll es möglich sein, Profile zwischen verschiedenen WEGs zu kopieren?

- Wie granular soll der Deduplikationsalgorithmus konfigurierbar sein (z. B. Betragsabweichung &plusmn; 1 &euro;)?

- Soll eine Import-Historie pro Profil integriert werden?

## Zukunftserweiterungen
- **Fuzzy-Deduplikation:** Erkennung ähnlicher Transaktionen über Textähnlichkeit (Levenshtein-Distanz).

- **Import-Historie:** Nachverfolgung vergangener Importe mit Datei-Hash und Profilversion.

- **KI-Profil-Erkennung:** Automatische Zuordnung eines Profils basierend auf Dateiformat und Spaltenstruktur.

- **Profil-Sharing:** Möglichkeit, Profile zwischen WEGs oder Mandanten zu exportieren/importieren.

## Verknüpfte Tasks
- [WEG-860 – Save Mapping Templates (profiles)](https://maierharry.atlassian.net/browse/WEG-860) – Implementierung der Profilverwaltung mit Spaltenzuordnung, Deduplikation und Versionierung.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Verwaltung von Importprofilen (CRUD), Spaltenzuordnung, Deduplikationsprüfung mit exakten Übereinstimmungen, Versionierung.

**Phase 2**

Fuzzy-Deduplikation, Import-Historie, Profil-Export/Import.

**Phase 3**

KI-gestützte Profil-Erkennung und automatische Spaltenzuordnung.