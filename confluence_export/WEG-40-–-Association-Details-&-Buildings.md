---
title: WEG-40 – Association Details & Buildings
confluence_id: 27460057
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27460057/WEG-40+Association+Details+Buildings
---

**JIRA-Link:** [WEG-40 – Association Details & Buildings](https://maierharry.atlassian.net/browse/WEG-40)

## Überblick

Das Untermodul **Association Details & Buildings** (WEG-40) verwaltet die Stammdaten der gesamten Gemeinschaft und ihrer Gebäude.

Es bildet die organisatorische und bauliche Struktur einer WEG ab – von allgemeinen Angaben wie Name, Adresse und Baujahr bis hin zu strukturellen Merkmalen wie Etagenzahl, Gesamtfläche und Anzahl der Einheiten.

Gebäude fungieren als zentrale Referenz für weitere Module wie Finanzen (WEG-8), Metering (WEG-7) und Dokumentenmanagement (WEG-5).

Ziel ist eine saubere, nachvollziehbare und erweiterbare Abbildung der baulichen Grundlage jeder Eigentümergemeinschaft.

## Beschreibung

Jede WEG kann ein oder mehrere Gebäude enthalten, die eindeutig mit der Gemeinschaft verknüpft sind.

Das Modul stellt sicher, dass Gebäudedaten konsistent gepflegt und vollständig dokumentiert werden. Neben Stammdaten können über das Dokumentenmanagementsystem (WEG-5) relevante Unterlagen wie Baupläne, Energieausweise oder Wartungsnachweise verknüpft werden.

Hauptfunktionen:

- **Gebäudestammdaten:** Verwaltung von Name, Adresse, Baujahr, Gebäudetyp, Etagenzahl, Gesamtfläche, Einheitenzahl und Status.

- **Dokumentenverknüpfung:** Integration in das DMS (WEG-5) zur Speicherung von Energieausweisen, Plänen und Wartungsprotokollen.

- **Statusverwaltung:** Gebäude können aktiv, stillgelegt oder in Planung sein; der Status beeinflusst abhängige Prozesse.

- **Audit-Protokollierung:** Jede Änderung wird im Audit-Log (WEG-24) aufgezeichnet.

- **Validierungsregeln:** Pflichtfelder (Name, Adresse, Gebäudetyp, Baujahr) müssen ausgefüllt sein; fehlerhafte Datensätze werden blockiert.

- **Beziehung zu Einheiten:** Gebäude dienen als Container für Einheiten (WEG-41) und bilden damit die logische Hierarchie für Eigentum, Nutzung und Abrechnung.

## Geschäftsregeln & Logik

- Gebäude müssen eindeutig einer WEG zugeordnet sein.

- Archivierte Gebäude dürfen keine aktiven Einheiten mehr enthalten.

- Pflichtfelder müssen beim Erstellen oder Bearbeiten eines Gebäudes vollständig befüllt werden.

- Änderungen an Gebäudedaten werden automatisch im Audit-Log dokumentiert.

- Dokumente dürfen nur von berechtigten Rollen (Manager, SystemAdmin) angehängt oder entfernt werden.

## Akzeptanzkriterien

- **Gegeben** ein neues Gebäude wird angelegt &rarr; **Wenn** alle Pflichtfelder ausgefüllt sind &rarr; **Dann** wird das Gebäude der WEG erfolgreich zugeordnet und im Audit-Log vermerkt.

- **Gegeben** ein Gebäude mit aktiven Einheiten &rarr; **Wenn** es archiviert werden soll &rarr; **Dann** verhindert das System die Archivierung, bis alle Einheiten deaktiviert oder übertragen sind.

- **Gegeben** ein Gebäude ist aktiv &rarr; **Wenn** ein Dokument (z. B. Energieausweis) hinzugefügt wird &rarr; **Dann** wird dieses im DMS gespeichert und mit dem Gebäude verknüpft.

- **Gegeben** ein Benutzer ohne Berechtigung &rarr; **Wenn** dieser versucht, Gebäudedaten zu ändern &rarr; **Dann** wird der Vorgang blockiert und im Audit-Log als verweigerter Zugriff dokumentiert.

## Nicht-Ziele

- Keine 3D-Visualisierung oder Integration von Bauplänen in Echtzeit.

- Keine GIS- oder Katasterintegration im MVP.

- Keine automatische Datenübernahme aus externen Gebäuderegistern.

## Kritische Fälle

- **Fehlerhafte Adressdaten:** Ein Scheduler-Job prüft Adressvalidität und weist auf Unstimmigkeiten hin.

- **Unvollständige Pflichtfelder:** Unvollständige Eingaben verhindern Speicherung.

- **Statusinkonsistenzen:** Archivierte Gebäude mit aktiven Einheiten erzeugen Fehlermeldungen und Audit-Einträge.

## Abhängigkeiten

-  – Speicherung und Verknüpfung von Bau- und Energiedokumenten.

-  – Nachvollziehbarkeit sämtlicher Änderungen an Gebäudedaten.

-  – Verbindung zwischen Gebäuden und Einheiten.

-  – Nutzung der Gebäudestruktur für Verbrauchszähler.

## Offene Fragen

- Soll die Energieeffizienz direkt im Gebäudeobjekt gepflegt oder nur als verknüpftes Dokument hinterlegt werden?

- Wie detailliert sollen Gebäudedaten für künftige IoT-Integrationen (z. B. Sensorik) sein?

- Sollen Gebäude in hierarchischen Strukturen (z. B. Gebäude &rarr; Hausabschnitt &rarr; Eingang) abgebildet werden?

## Zukunftserweiterungen

- **Automatischer Dokumentenimport:** Extraktion von Baujahr und Fläche aus PDF-Dokumenten.

- **Integration von Energieausweis-Datenbanken:** Direkter Import staatlich erfasster Energieausweise.

- **IoT-Integration:** Automatische Aktualisierung von Gebäudedaten über Sensoren (z. B. Temperatur, Feuchtigkeit).

## Verknüpfte Tasks

- [WEG-400 – Association Details & Building CRUD](https://maierharry.atlassian.net/browse/WEG-400) – Implementiert Erstellen, Lesen, Bearbeiten und Löschen von Gebäudedaten.

- [WEG-401 – DMS Linking & Validation](https://maierharry.atlassian.net/browse/WEG-401) – Anbindung von Bau- und Energiedokumenten an Gebäudedatensätze.

- [WEG-402 – Status Validation Rules](https://maierharry.atlassian.net/browse/WEG-402) – Validierung der Statusübergänge (aktiv, stillgelegt, archiviert).

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Verwaltung von Gebäudestammdaten, Pflichtfeldvalidierung, DMS-Verknüpfung und Audit-Logging.

**Phase 2**

Erweiterte Dokumentenfelder (Energieeffizienz, Sanierungsnachweise), Statusabhängige Validierung.

**Phase 3**

IoT-Integration und automatisierte Datenerfassung aus Sensoren und externen Quellen.