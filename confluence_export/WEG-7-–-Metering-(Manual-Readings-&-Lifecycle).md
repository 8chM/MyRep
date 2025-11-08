---
title: WEG-7 – Metering (Manual Readings & Lifecycle)
confluence_id: 27329358
version: 19
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329358/WEG-7+Metering+Manual+Readings+Lifecycle
---

**JIRA-Link:** [WEG-7 – Metering (Manual Readings & Lifecycle)](https://maierharry.atlassian.net/browse/WEG-7)

## Beschreibung
Das Modul **WEG-7 – Metering** bildet das Fundament der Verbrauchsdatenerfassung im WEG Management System (WMS). Es erfasst, verwaltet und archiviert Zählerstände für Strom, Wasser, Heizung, Gas und vergleichbare Medien – manuell, strukturiert und revisionssicher. Das System sorgt dafür, dass Verbrauchsdaten nachvollziehbar dokumentiert und fehlerfrei an die Abrechnung (WEG-8) übergeben werden.

Ziel ist es, die Datenqualität und Transparenz zu gewährleisten, Lesekampagnen zu vereinfachen und Eigentümern, Bewohnern und Verwaltern jederzeit verlässliche Verbrauchsinformationen bereitzustellen. Das MVP konzentriert sich auf manuelle Erfassung und Validierung. In späteren Phasen werden IoT-Sensoren, Smart-Meter-Gateways und automatische Plausibilitätsanalysen ergänzt.

## Untermodule
**Untermodul**

**Beschreibung**

**WEG-70 – Meter Registry & Types (Electric/Water/Gas/Heat)**Erfasst alle Zählerarten mit Typ, Medium, Seriennummer, Standort und Status. Dient als zentrale Referenz für Zuordnung und Lebenszyklus.

**WEG-71 – Manual Readings (Validation, 24h Edit)**Oberfläche für die manuelle Eingabe von Zählerständen inklusive Validierung, Änderungsverlauf und 24-Stunden-Nachbearbeitungszeit.

**WEG-72 – Meter Lifecycle & Replacement**Verwaltung des gesamten Lebenszyklus eines Zählers – von Inbetriebnahme über Austausch bis zur Stilllegung.

**WEG-73 – Rollover & Reversed Counters (Configurable)**Behandlung von Zählern mit Ziffernüberlauf oder rückwärtslaufenden Mechanismen; automatische Korrektur von Differenzen.

**WEG-74 – Meter Hierarchies (Parent/Child)**Abbildung von Haupt- und Unterzählern inklusive Aufteilung und Summierung der Verbrauchswerte.

**WEG-75 – Reading Campaigns (Bulk Grid)**Planung, Durchführung und Nachverfolgung von Ablesekampagnen mit Erinnerungslogik und Bulk-Erfassung.

**WEG-76 – Period Lock & Snapshots (for later Billing)**Sperrung von Ablesezeiträumen und Erzeugung von Daten-Snapshots für spätere Abrechnungsläufe.

## Geschäftslogik
Das Modul ist so aufgebaut, dass Verbrauchsdaten über alle WEGs hinweg konsistent, validiert und manipulationssicher verwaltet werden:

- **Zählerstruktur:** Jeder Zähler ist einer WEG, einem Gebäude und optional einer Einheit zugeordnet. Er besitzt eine eindeutige Seriennummer, ID und Status (aktiv, defekt, ersetzt, archiviert).

- **Plausibilitätsprüfung:** Neue Eingaben werden gegen vorherige Messwerte geprüft; unrealistische Differenzen werden markiert und erfordern Bestätigung durch den Verwalter.

- **Lebenszyklusmanagement:** Beim Austausch eines defekten Geräts werden Abschluss- und Eröffnungsstände automatisch übernommen und miteinander verknüpft.

- **Zählertypen und Hierarchien:** Hauptzähler aggregieren Verbrauchsdaten mehrerer Unterzähler; Abweichungen werden systemisch überprüft.

- **Lesekampagnen:** Kampagnen können für alle oder ausgewählte Medien gestartet werden. Erinnerungen an fehlende Werte erfolgen automatisch über WEG-6 (Notifications).

- **Archivierung & Sperrlogik:** Abgeschlossene Perioden (WEG-76) werden gesperrt, Änderungen sind danach nur mit Begründung und Freigabe möglich.

- **Roll-Over-Korrektur:** System erkennt Zählerüberläufe und korrigiert Differenzen automatisch.

- **Scheduler-Integration:** Über WEG-12 werden automatische Erinnerungen, Prüfungen und periodische Plausibilitätschecks ausgelöst.

## Akzeptanzkriterien

- **Gegeben** ein berechtigter Benutzer &rarr; **Wenn** er einen Zählerstand eingibt &rarr; **Dann** validiert das System den Wert, speichert ihn versioniert und bestätigt die Eingabe.

- **Gegeben** ein defekter Zähler &rarr; **Wenn** dieser ersetzt wird &rarr; **Dann** legt das System automatisch einen neuen Zähler an, verknüpft ihn mit dem alten und übernimmt den Startwert.

- **Gegeben** eine geplante Ablesekampagne &rarr; **Wenn** das Fälligkeitsdatum erreicht wird &rarr; **Dann** werden Benachrichtigungen an zuständige Benutzer versendet.

- **Gegeben** ein Ablesezeitraum &rarr; **Wenn** der Verwalter diesen abschließt &rarr; **Dann** werden alle Werte schreibgeschützt und für die Abrechnung bereitgestellt.

- **Gegeben** ein Zähler läuft über (Roll-Over) &rarr; **Wenn** ein neuer Wert kleiner als der vorherige ist &rarr; **Dann** korrigiert das System die Differenz automatisch und dokumentiert sie im Audit-Log.

## Nicht-Ziele
- Keine automatisierte IoT-Auslesung oder direkte Smart-Meter-Integration im MVP.

- Keine grafischen Diagramme oder Verbrauchsvergleiche.

- Keine automatische Kostenumlage – diese erfolgt über WEG-8 (Finance & Billing).

- Kein direkter Datenaustausch mit Energieversorgern oder externen APIs.

## Kritische Fälle
- **Doppelte Eingaben:** Zeitgleiche Eingaben müssen durch Versionskontrolle abgefangen werden.

- **Unplausible Messwerte:** Bei starken Abweichungen werden Werte blockiert und müssen manuell bestätigt werden.

- **Defekte Geräte:** Defekte oder ersetzte Zähler dürfen keine offenen Perioden hinterlassen.

- **Fehlende Ablesung:** Scheduler erinnert automatisch, erstellt aber Eskalationsmeldungen bei Überschreitung.

## Abhängigkeiten
- WEG-12 – Error Handling, Logging & Health: Scheduler und technische Basis für Überwachung und Protokollierung.

- WEG-5 – Document Management & Templates: Speicherung von Ableseprotokollen, Fotos und PDF-Berichten.

- WEG-6 – In-App Messaging & Notifications (Basic): Versand von Erinnerungen und Ableseaufforderungen.

- WEG-8 – Finance & Banking: Weitergabe der erfassten Messwerte für Verbrauchsabrechnung.

- WEG-24 – Audit Log (User/Roles/Settings): Speicherung aller Änderungen mit Zeitstempel und Benutzer.

- WEG-26 – Data Privacy & Redaction (GDPR Base): Sicherstellung DSGVO-konformer Speicherung von personenbezogenen Messdaten.

- WEG-54 – Data Retention & Erasure: Festlegung der Aufbewahrungs- und Löschfristen für Ablesedaten.

## Offene Fragen
- Sollen Benutzer Messwerte auch über mobile Geräte mit Fotoeingabe erfassen können?

- Soll eine automatische Plausibilitätsbewertung (z. B. KI-gestützt) in Phase 2 integriert werden?

- Welche Medienarten (z. B. Fernwärme, Solaranlagen) sollen im Standard abgedeckt sein?

- Wie sollen Sammelzähler in Mehrparteienhäusern behandelt werden?

## Zukunftserweiterungen
- **IoT-Integration:** Automatische Smart-Meter-Anbindung über Gateways und APIs.

- **KI-Analysen:** Erkennung auffälliger Verbrauchsmuster oder möglicher Leckagen.

- **Verbrauchs-Dashboards:** Grafische Darstellung mit Zeitverlauf, Vergleich und Prognose.

- **Datenexport:** Schnittstellen für Energieversorger und Abrechnungsdienste.

- **Mobile App:** Offline-fähige Zählererfassung mit Kameraunterstützung.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Zählerregistrierung, manuelle Ablesung, Validierung, Roll-Over-Logik, Ablesekampagnen, Periodenabschlüsse.

**Phase 2**

IoT-Anbindung, grafische Analysen, Anomalieerkennung, Exportformate.

**Phase 3**

Vollautomatische Smart-Meter-Integration, mobile App, Predictive Maintenance.