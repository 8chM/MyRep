---
title: WEG-74 – Meter Hierarchies (Parent/Child)
confluence_id: 26968700
version: 23
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/26968700/WEG-74+Meter+Hierarchies+Parent+Child
---

**JIRA-Link:** [WEG-74 – Meter Hierarchies (Parent/Child)](https://maierharry.atlassian.net/browse/WEG-74)

## Überblick
Das Modul **Meter Hierarchies** (WEG-74) erweitert das Zählermanagement (WEG-7) um die Möglichkeit, Messgeräte in hierarchischen Strukturen abzubilden. Es ermöglicht die Modellierung von Haupt-, Zwischen- und Unterzählern, um komplexe Messketten vollständig digital darzustellen. Ziel ist die transparente Nachverfolgung von Verbräuchen über verschiedene Ebenen hinweg, insbesondere in Mehrparteiengebäuden mit Zwischenverteilungen oder Hauptzählern. Durch diese Strukturierung werden Plausibilitätsprüfungen, Verbrauchsanalysen und Abrechnungsprozesse deutlich präziser und nachvollziehbarer.

## Beschreibung
WEG-74 bildet die logischen Beziehungen zwischen Zählern einer WEG ab, indem es jedem Zähler einen **Parent-Zähler** (übergeordnet) und beliebig viele C**hild-Zähler** (untergeordnet) zuweist. Diese Beziehungen schaffen die Grundlage für Berechnungen, Prüfungen und Verteilungen in der Abrechnung (WEG-87) sowie für Verbrauchsanalysen und Fehlersuchen. Das Modul validiert jede Änderung automatisch und stellt sicher, dass keine fehlerhaften oder zyklischen Verknüpfungen entstehen. Darüber hinaus unterstützt es die grafische Darstellung der Zählerhierarchie im Frontend und sorgt für konsistente Historienführung bei Austausch oder Deaktivierung einzelner Zähler.

Hauptfunktionen:

- **Hierarchische Strukturierung:** Erstellung und Pflege von Parent/Child-Beziehungen zwischen Zählern mit flexibler Tiefe (mehrstufige Hierarchien).

- **Summenzähler-Funktion:** Definition von Hauptzählern als Aggregationspunkte zur Erfassung und Verrechnung von Gesamtverbräuchen.

- **Konsistenzprüfung:** Automatische Kontrolle, ob Child-Verbräuche in Summe den Parent-Verbrauch plausibel ergänzen oder überschreiten.

- **Graphische Visualisierung:** Darstellung der Zählerhierarchie in Baumstruktur mit Statusindikatoren (aktiv, defekt, ersetzt).

- **Automatische Verbrauchsverteilung:** Aufteilung von Gesamtverbräuchen auf untergeordnete Zähler bei fehlenden Einzelablesungen.

- **Historisierung:** Vollständige Nachverfolgung von Parent/Child-Beziehungen bei Austausch, Ersatz oder Deaktivierung von Zählern.

- **Audit-Integration:** Protokollierung aller Änderungen mit Benutzer, Zeitstempel und Aktion.

- **Reporting:** Export der Hierarchiedaten und Plausibilitätsprüfungen als PDF oder CSV.

## Geschäftsregeln & Logik
- Jeder Zähler kann genau einen Parent, aber mehrere Child-Zähler besitzen.

- Hauptzähler dürfen keine übergeordneten Zähler haben.

- Hierarchien dürfen keine Zyklen enthalten; solche Verknüpfungen werden blockiert.

- Nur aktive Zähler dürfen in Hierarchien verwendet werden.

- Beim Deaktivieren eines Zählers werden untergeordnete Beziehungen automatisch neu bewertet.

- Abrechnungen (WEG-87) berücksichtigen Parent/Child-Strukturen bei Verbrauchsverteilungen automatisch.

- Fehlende Ablesungen untergeordneter Zähler werden anteilig ergänzt.

## Akzeptanzkriterien
- **Gegeben** eine WEG besitzt mehrere Zähler &rarr; **Wenn** ein Parent-Child-Verhältnis erstellt wird &rarr; **Dann** werden beide Zähler korrekt verknüpft und in der Hierarchie dargestellt.

- **Gegeben** ein Parent-Zähler und seine Child-Meter besitzen Verbrauchsdaten &rarr; **Wenn** eine Konsistenzprüfung durchgeführt wird &rarr; **Dann** meldet das System Abweichungen, falls Child-Summen größer als der Parent-Verbrauch sind.

- **Gegeben** ein Zähler wird deaktiviert oder ersetzt &rarr; **Wenn** die Hierarchie neu berechnet wird &rarr; **Dann** übernimmt der neue Zähler die Rolle des alten und die Historie wird aktualisiert.

- **Gegeben** eine Abrechnung nutzt einen Hauptzähler &rarr; **Wenn** Child-Daten fehlen &rarr; **Dann** wird der Verbrauch anteilig verteilt und der Vorgang dokumentiert.

- **Gegeben** ein Benutzer öffnet die Hierarchieansicht &rarr; **Wenn** ein Zähler mit mehreren Abhängigkeiten angezeigt wird &rarr; **Dann** erscheinen Parent- und Child-Zähler visuell verknüpft mit Status und Tooltip.

## Nicht-Ziele
- Keine automatische Erkennung von Hierarchien durch externe Smart-Meter-Systeme im MVP.

- Kein Import hierarchischer Daten aus Fremdsystemen.

- Keine Simulation oder virtuelle Verbrauchsverteilung in Phase 1.

## Kritische Fälle
- **Doppelte Zuordnung:** Ein Zähler darf nicht mehreren Parent-Zählern gleichzeitig zugeordnet werden.

- **Fehlende Child-Werte:** Wenn untergeordnete Zähler keine Werte liefern, muss das System Schätzungen oder Warnungen auslösen.

- **Hierarchie-Inkonsistenz:** Rückverweise oder Zyklen werden blockiert und protokolliert.

- **Falsche Historie:** Beim Austausch eines Zählers darf die Historie nicht überschrieben, sondern versioniert werden.

## Abhängigkeiten
- WEG-7 – Metering – Basisdaten und Verwaltung der Messwerte.

- WEG-72 – Meter Lifecycle & Replacement – Verwaltung von Zählerstatus und Austauschhistorie.

- WEG-75 – Reading Campaigns – Nutzung der Hierarchie für Sammelablesungen.

- WEG-76 – Locks & Snapshots – Sicherung der Konsistenz bei periodischen Sperren.

- WEG-87 – Accounting & Billing – Verwendung für Verbrauchsverteilung und Umlagelogik.

- WEG-88 – Finance Export & Compliance – Einbindung in Exportberichte.

## Offene Fragen
- Soll die Hierarchie über Drag-and-Drop bearbeitbar sein oder ausschließlich per Formular?

- Soll die Konsistenzprüfung automatisch nach jeder Ablesung oder periodisch erfolgen?

- Wie sollen fehlende Child-Werte im Audit dokumentiert werden?

## Zukunftserweiterungen
- **Smart-Meter-Integration:** Automatische Erkennung und Aktualisierung von Hierarchien.

- **Interaktive Visualisierung:** Erweiterte grafische Darstellung mit Zoom, Tooltipps und Filterung.

- **Trendanalysen:** Erkennung und Visualisierung von Verbrauchsabweichungen innerhalb der Hierarchie.

- **Simulationsmodus:** Prognose von Energieverbräuchen und Plausibilitätsmodellen.

## Verknüpfte Tasks
- [WEG-740 – Parent/Child Meter Hierarchies](https://maierharry.atlassian.net/browse/WEG-740) – Aufbau des hierarchischen Modells zwischen Zählern.

- [WEG-741 – Hierarchy Visualization UI](https://maierharry.atlassian.net/browse/WEG-741) – Darstellung und Bearbeitung der Hierarchie im Frontend.

- [WEG-742 – Consistency Checks](https://maierharry.atlassian.net/browse/WEG-742) – Prüfung der Plausibilität zwischen Parent- und Child-Zählern.

- [WEG-743 – Hierarchy Persistence & History](https://maierharry.atlassian.net/browse/WEG-743) – Speicherung der Historie und Beziehungen.

- [WEG-744 – Integration in Reading Campaigns (WEG-75)](https://maierharry.atlassian.net/browse/WEG-744) – Nutzung der Hierarchie in Sammelablesungen.

- [WEG-745 – Hierarchy Validation Service](https://maierharry.atlassian.net/browse/WEG-745) – Laufende Prüfung auf Zyklen und Unstimmigkeiten.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Erstellung und Verwaltung von Parent/Child-Beziehungen, Konsistenzprüfung, manuelle Pflege, grafische Anzeige, Audit-Protokollierung.

**Phase 2**

Erweiterte Berechnungen und automatische Verbrauchsverteilung, Validierungs-API, hierarchische Reports und Schätzmechanismen.

**Phase 3**

Integration mit Smart-Meter-Systemen, automatische Erkennung, interaktive Visualisierung und KI-gestützte Anomalieerkennung.