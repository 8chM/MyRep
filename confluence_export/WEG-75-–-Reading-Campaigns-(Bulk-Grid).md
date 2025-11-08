---
title: WEG-75 – Reading Campaigns (Bulk Grid)
confluence_id: 27722324
version: 23
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722324/WEG-75+Reading+Campaigns+Bulk+Grid
---

**JIRA-Link:** [WEG-75 – Reading Campaigns (Bulk Grid)](https://maierharry.atlassian.net/browse/WEG-75)

## Überblick

Das Modul **Reading Campaigns** (WEG-75) bildet den zentralen Prozess zur koordinierten Erfassung, Verwaltung und Kontrolle von Zählerständen innerhalb einer Eigentümergemeinschaft. Es erlaubt die Planung und Durchführung von Sammelablesungen über mehrere Einheiten, Gebäude oder ganze WEGs hinweg und sorgt für einen einheitlichen, nachvollziehbaren Workflow. Das Ziel ist eine strukturierte, fehlerarme Datenerfassung, die die Grundlage für spätere Abrechnungen (WEG-87) und Auswertungen bildet.

## Beschreibung

WEG-75 koordiniert groß angelegte Ableseprozesse (&bdquo;Kampagnen&ldquo;) und stellt sicher, dass alle relevanten Zähler (WEG-70 ff.) innerhalb eines definierten Zeitraums erfasst und validiert werden. Das Modul bietet Funktionen zur automatischen Auswahl von Zählern, Statusüberwachung, Import und Kontrolle der erfassten Werte. Es ist vollständig mit den Modulen für Verbrauchsvalidierung, Historisierung und Abrechnung integriert und stellt alle notwendigen Informationen über eine zentrale Oberfläche bereit.

## Hauptfunktionen

- **Kampagnenverwaltung:** Erstellung, Planung und Steuerung von Sammelablesungen mit Start- und Enddatum sowie Statusverfolgung.

- **Zählerauswahl & Filter:** Automatische oder manuelle Selektion betroffener Zähler nach Typ, Gebäude oder Eigentumseinheit.

- **Bulk-Erfassung:** Erfassung mehrerer Messwerte in tabellarischer Ansicht mit sofortiger Plausibilitätsprüfung.

- **Import & Export:** Unterstützung von CSV-Importen und -Exporten zur Weitergabe an externe Ablesedienste.

- **Statusmanagement:** Echtzeit-Überwachung von offenen, laufenden und abgeschlossenen Ablesungen.

- **Fehlerkontrolle:** Anzeige von Warnungen bei fehlenden, doppelten oder unplausiblen Werten.

- **Audit-Trail:** Protokollierung aller Änderungen und Ablesevorgänge.

- **Reporting:** Zusammenfassung abgeschlossener Kampagnen als PDF- oder CSV-Bericht.

## Geschäftsregeln & Logik

- Eine Kampagne umfasst immer einen klar definierten Zeitraum und Zählerkreis.

- Nur aktive Zähler dürfen in Kampagnen aufgenommen werden.

- Abgeschlossene Kampagnen sind schreibgeschützt und revisionssicher archiviert.

- Fehlende Werte müssen vor Abschluss ergänzt oder als plausibel markiert werden.

- Jeder Ablesewert ist einem Benutzer und Zeitstempel eindeutig zugeordnet.

- Änderungen nach Abschluss sind nur über Revisionen zulässig.

## Akzeptanzkriterien

- **Gegeben** eine neue Ablesekampagne wird erstellt &rarr; **Wenn** Zähler selektiert und gestartet werden &rarr; **Dann** erscheinen alle aktiven Zähler im Ablese-Grid mit korrektem Status.

- **Gegeben** ein Benutzer erfasst Werte &rarr; **Wenn** ein Wert unplausibel ist &rarr; **Dann** erhält der Benutzer eine Warnung und der Datensatz wird markiert.

- **Gegeben** eine Kampagne wird abgeschlossen &rarr; **Wenn** alle Werte validiert sind &rarr; **Dann** wird der Status auf &bdquo;Abgeschlossen&ldquo; gesetzt und ein Audit-Eintrag erstellt.

- **Gegeben** eine Kampagne enthält fehlende Werte &rarr; **Wenn** sie exportiert wird &rarr; **Dann** werden fehlende Werte als &bdquo;nicht erfasst&ldquo; gekennzeichnet.

- **Gegeben** ein Import von CSV-Daten &rarr; **Wenn** Duplikate erkannt werden &rarr; **Dann** verhindert das System doppelte Einträge.

## Nicht-Ziele

- Keine mobile Erfassung im MVP.

- Kein automatischer Import von IoT- oder Smart-Meter-Geräten (siehe spätere Phasen).

- Keine Integration mit externen Ablesediensten über API.

## Kritische Fälle

- **Doppelte Einträge:** Mehrfache Ablesungen müssen erkannt und verhindert werden.

- **Fehlende Daten:** Lückenhafte Kampagnen dürfen nicht abgeschlossen werden.

- **Plausibilitätsfehler:** Extremwerte müssen überprüft und bestätigt werden.

- **Datenverlust:** Unterbrochene Erfassungen dürfen keine unvollständigen Datensätze hinterlassen.

## Abhängigkeiten

-  – Definition der Zähler und Typen.

-  – Basismodul zur Einzelerfassung.

-  – Nutzung der Zählerstruktur in Kampagnen.

-  – Sicherung der Daten nach Abschluss.

-  – Verwendung der Ablesedaten für Abrechnungen.

-  – Protokollierung von Kampagnenaktionen.

## Offene Fragen

- Soll eine Kampagne automatisch nach Enddatum geschlossen werden?

- Wie sollen unplausible Werte bestätigt werden – manuell oder regelbasiert?

- Ist eine Teil-Abnahme pro Gebäude notwendig?

## Zukunftserweiterungen

- **Mobile Erfassung:** Unterstützung von Tablet- oder App-basierten Ablesungen.

- **IoT-Integration:** Automatische Übernahme von Smart-Meter-Daten.

- **Kampagnen-Templates:** Wiederverwendbare Vorlagen für periodische Ablesungen.

- **Benachrichtigungen:** Automatische Erinnerungen bei offenen Werten.

## Verknüpfte Tasks

- [WEG-750 – Bulk Grid Campaign Setup](https://maierharry.atlassian.net/browse/WEG-750) – Erstellung und Konfiguration neuer Ablesekampagnen.

- [WEG-751 – CSV Import/Export](https://maierharry.atlassian.net/browse/WEG-751) – Schnittstellen zur Datenübernahme und Weitergabe.

- [WEG-752 – Campaign Validation & Close](https://maierharry.atlassian.net/browse/WEG-752) – Prüfung, Abschluss und Archivierung von Kampagnen.

- [WEG-753 – Campaign Reports](https://maierharry.atlassian.net/browse/WEG-753) – Generierung von Abschlussberichten.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Erstellung, Verwaltung und Abschluss von Ablesekampagnen, CSV-Import/-Export, Plausibilitätsprüfung, Audit-Protokollierung.

**Phase 2**

Erweiterte Validierungslogik, Teilabschlüsse, automatische Erinnerungen und Statusberichte.

**Phase 3**

Mobile Erfassung, IoT-Anbindung, Kampagnen-Templates und Smart-Reporting.