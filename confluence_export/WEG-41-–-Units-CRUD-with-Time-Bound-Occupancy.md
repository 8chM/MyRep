---
title: WEG-41 – Units CRUD with Time-Bound Occupancy
confluence_id: 26968640
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/26968640/WEG-41+Units+CRUD+with+Time-Bound+Occupancy
---

**JIRA-Link:** [WEG-41 – Units CRUD with Time-Bound Occupancy](https://maierharry.atlassian.net/browse/WEG-41)

## Überblick

Das Modul **Units CRUD with Time-Bound Occupancy** (WEG-41) ermöglicht die Anlage, Verwaltung und Historisierung von Nutzungseinheiten innerhalb einer WEG – einschließlich Wohnungen, Gewerbeflächen, Stellplätzen oder Sondernutzungsrechten.

Jede Einheit ist einem Gebäude (WEG-40) zugeordnet und besitzt Attribute wie Nummer, Fläche, MEA-Anteil, Nutzung und Etage.

Die zeitliche Gültigkeit (Start- und Enddatum) bildet die Grundlage für die Nachvollziehbarkeit von Besitz-, Nutzungs- und Abrechnungszeiträumen.

Ziel ist eine konsistente, revisionssichere Verwaltung aller Einheiten, die als Kernobjekte für Abrechnung (WEG-87), Verbrauchserfassung (WEG-7) und Abstimmungen (WEG-92) dienen.

## Beschreibung

Das Modul definiert den Lebenszyklus einer Einheit von der Erstellung über Änderungen bis hin zur Historisierung.

Jede Änderung an relevanten Eigenschaften (z. B. Fläche, MEA, Nutzung) erzeugt automatisch eine neue Version, während die alte Version archiviert wird.

Dadurch bleibt jede Änderung nachvollziehbar und kann im Audit-Log (WEG-24) eingesehen werden.

Hauptfunktionen:

- **Einheitenerstellung (Create):** Neue Einheiten können mit Pflichtfeldern wie Nummer, Fläche, Nutzung, MEA und Etage erstellt werden.

- **Bearbeitung & Versionierung (Update):** Änderungen an einer Einheit erzeugen eine neue Version mit gültigem Start- und Enddatum.

- **Historisierung:** Alte Versionen werden gesperrt, bleiben jedoch zur Nachverfolgung im System.

- **Validierungslogik:** Verhindert Überschneidungen in den Gültigkeitszeiträumen; MEA-Summen müssen innerhalb des Gebäudes konsistent bleiben.

- **Statusverwaltung:** Einheiten können aktiv, inaktiv oder veräußert sein.

- **Beziehung zu Eigentum & Bewohnern:** Einheitliche Verknüpfung zu Besitz- und Nutzungsverhältnissen (WEG-42).

- **Integration:** Einheiten bilden die Grundlage für Finanz- und Verbrauchsdaten (WEG-8, WEG-7) und sind Teil der Voting-Logik bei Beschlüssen (WEG-92).

## Geschäftsregeln & Logik

- Jede Einheit besitzt eine eindeutige ID und ist einem Gebäude zugeordnet.

- Start- und Enddatum sind Pflichtfelder; Überschneidungen zwischen Versionen sind nicht erlaubt.

- Änderungen an MEA oder Fläche müssen zu einer Neubewertung der Gesamt-MEA-Summe führen.

- Es darf nur eine aktive Version pro Einheit existieren.

- Archivierte Einheiten sind schreibgeschützt.

- Änderungen an Einheiten werden vollständig im Audit-Log dokumentiert.

## Akzeptanzkriterien

- **Gegeben** eine neue Einheit wird angelegt &rarr; **Wenn** alle Pflichtfelder ausgefüllt sind &rarr; **Dann** wird die Einheit erfolgreich gespeichert und im Audit-Log erfasst.

- **Gegeben** eine Flächen- oder MEA-Änderung erfolgt &rarr; **Wenn** die Änderung gespeichert wird &rarr; **Dann** wird automatisch eine neue Version erzeugt und die alte historisiert.

- **Gegeben** zwei Versionen mit überlappenden Gültigkeitszeiträumen &rarr; **Wenn** der Speichervorgang ausgeführt wird &rarr; **Dann** verweigert das System die Speicherung und zeigt eine Validierungswarnung.

- **Gegeben** ein Eigentümerwechsel wird eingetragen &rarr; **Wenn** der Zeitraum nicht mit der Einheit korrespondiert &rarr; **Dann** erzeugt das System einen Validierungsfehler.

- **Gegeben** eine Einheit wird gelöscht &rarr; **Wenn** abhängige Finanz- oder Meterdaten existieren &rarr; **Dann** blockiert das System die Löschung und verweist auf die betroffenen Module.

## Nicht-Ziele

- Keine automatische Flächenberechnung aus Bauplänen oder CAD-Daten im MVP.

- Keine visuelle Darstellung von Einheiten (z. B. 3D-Modelle).

- Keine Integration externer Gebäudeinformationssysteme.

## Kritische Fälle

- **Mehrfacher Eigentümer ohne Enddatum:** System verweigert Speicherung, wenn mehrere aktive Eigentümer für dieselbe Einheit bestehen.

- **Gültigkeitsüberschneidungen:** Überschneidende Zeiträume werden automatisch erkannt und blockiert.

- **Fehlerhafte MEA-Summen:** Änderungen, die die Gesamtsumme der MEA eines Gebäudes verletzen, lösen eine Fehlermeldung aus.

- **Verwaiste Einheiten:** Einheiten ohne gültige Zuordnung zu einem Gebäude dürfen nicht bestehen bleiben.

## Abhängigkeiten

-  – Protokollierung aller Änderungen und Versionierungen.

-  – Prüfung von MEA-, Flächen- und Statuskonsistenz.

-  – Verknüpfung zu Eigentümern und Bewohnern.

-  – Übergeordnete Struktur der Gebäude.

-  – Nutzung der Einheiten für Abrechnungslogiken und Umlagen.

## Offene Fragen

- Soll das System Änderungen an Einheiten automatisch mit Abrechnungsmodulen synchronisieren (z. B. bei Flächenänderung)?

- Wie werden Einheiten mit Sondernutzungsrechten (z. B. Garten, Stellplatz) im MVP behandelt – separat oder als Erweiterung?

- Soll die Historie für inaktive Einheiten im UI angezeigt oder nur archiviert werden?

## Zukunftserweiterungen

- **Automatische Flächenberechnung:** Import und Berechnung aus hinterlegten Bauplänen.

- **Integration mit IoT-Sensorik:** Erfassung von Verbrauchsflächen, Belegungsstatus und Nutzung in Echtzeit.

- **Hierarchische Einheitengruppen:** Unterstützung für Einheitenbündel (z. B. Tiefgarage, Nebengebäude).

- **Massenbearbeitung (Bulk-Edit):** Verwaltung und Änderung mehrerer Einheiten gleichzeitig.

## Verknüpfte Tasks

- [WEG-410 – Units CRUD with Start/End Validity](https://maierharry.atlassian.net/browse/WEG-410) – Implementiert CRUD-Funktionen mit Versionierung.

- [WEG-411 – Versioning Engine](https://maierharry.atlassian.net/browse/WEG-411) – Stellt die Logik für Historisierung und Überschneidungsprüfung bereit.

- [WEG-412 – MEA Validation Hook](https://maierharry.atlassian.net/browse/WEG-412) – Prüft Änderungen an Fläche und MEA auf Konsistenz.

- [WEG-413 – UI Integration (Buildings/Units Overview)](https://maierharry.atlassian.net/browse/WEG-413) – Visualisierung der Gebäudeeinheiten.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

CRUD-Funktionen für Einheiten mit zeitlicher Gültigkeit, Versionierung, Validierungslogik und Audit-Integration.

**Phase 2**

Erweiterte Validierungs-Workflows, Bulk-Bearbeitung, Synchronisierung mit Finanz- und Metering-Daten.

**Phase 3**

Automatische Flächenberechnung aus Bauplänen, IoT-Integration und hierarchische Strukturen.