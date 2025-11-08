---
title: WEG-43 – Unit Merge/Split Workflow (Cut-off Validations)
confluence_id: 27460072
version: 14
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27460072/WEG-43+Unit+Merge+Split+Workflow+Cut-off+Validations
---

**JIRA-Link:** [WEG-43 – Unit Merge/Split Workflow (Cut-off Validations)](https://maierharry.atlassian.net/browse/WEG-43)

## Überblick

Das Modul **Unit Merge/Split Workflow** (WEG-43) erweitert die Stammdatenverwaltung um kontrollierte Änderungsprozesse an der Gebäudestruktur.

Es deckt sowohl die Zusammenführung (Merge) mehrerer Einheiten als auch die Aufteilung (Split) einer bestehenden Einheit ab.

Ziel ist es, bauliche oder organisatorische Anpassungen an der Gebäudestruktur vollständig nachvollziehbar, revisionssicher und konsistent über alle abhängigen Module hinweg abzubilden.

Dabei prüft das System alle relevanten Zusammenhänge – etwa Eigentumsverhältnisse, Zählerzuordnungen, Flächenanteile und Abrechnungsdaten – bevor Änderungen aktiv übernommen werden.

WEG-43 stellt sicher, dass die historische Integrität der Daten auch nach umfangreichen Änderungen erhalten bleibt und keine fehlerhaften Abhängigkeiten in Folgeprozesse (z. B. Abrechnung oder Zählerwesen) übergehen.

## Beschreibung

WEG-43 erweitert die Stammdatenverwaltung um intelligente Änderungs-Workflows, die Eingriffe in die Gebäudestruktur vollständig nachvollziehbar abbilden.

Der Prozess stellt sicher, dass alle Eigentums-, Nutzungs- und Flächeninformationen aus betroffenen Einheiten korrekt zusammengeführt oder anteilig aufgeteilt werden.

Jeder Vorgang durchläuft eine Validierung aller abhängigen Module (WEG-4, WEG-7, WEG-8), bevor Änderungen übernommen werden.

Das System verhindert parallele Bearbeitungen, archiviert alte Datensätze automatisch und stellt sicher, dass die historische Datenintegrität auch nach Umbauten vollständig erhalten bleibt.

Hauptfunktionen:

- **Merge-Workflow:** Zusammenführung mehrerer Einheiten zu einer neuen Einheit mit konsolidierten MEA-, Flächen-, Eigentümer- und Zählerdaten.

- **Split-Workflow:** Aufteilung einer bestehenden Einheit in mehrere neue Einheiten, inklusive automatischer proportionaler Flächen- und MEA-Verteilung.

- **Validierungsmechanismus:** Überprüft Abhängigkeiten zu Eigentümern, Zählern und Abrechnungen; verhindert Änderungen bei offenen Vorgängen.

- **Historisierung:** Schließt betroffene Datensätze und erstellt automatisch archivierte Versionen mit Verweis auf neue Einheiten.

- **Audit-Trail:** Dokumentiert jeden Vorgang revisionssicher mit Zeitstempel, Benutzer und Status im Audit-Log (WEG-24).

- **Sperrlogik:** Blockiert temporär Änderungen an Einheiten, während ein Merge- oder Split-Prozess aktiv ist.

- **Reporting:** Erzeugt Änderungsberichte zu abgeschlossenen Vorgängen als PDF oder CSV.

## Geschäftsregeln & Logik

- Merge- und Split-Prozesse dürfen nur in offenen Perioden durchgeführt werden.

- Einheiten mit offenen Abrechnungen oder laufenden Zählerablesungen können nicht verändert werden.

- Jeder Vorgang erzeugt eine neue Version der betroffenen Einheiten – bestehende Daten werden niemals überschrieben.

- Bei fehlerhaften Eingaben oder inkonsistenten Abhängigkeiten bricht das System den Vorgang ab und setzt den ursprünglichen Zustand wieder her.

- Nach Abschluss eines Workflows werden alle resultierenden Einheiten dauerhaft miteinander verknüpft.

## Akzeptanzkriterien

- **Gegeben** mehrere aktive Einheiten sollen zusammengeführt werden &rarr; **Wenn** der Merge-Workflow validiert und ausgeführt wird &rarr; **Dann** entsteht eine neue Einheit mit korrekt aggregierten MEA-, Flächen- und Eigentümerdaten.

- **Gegeben** eine Einheit soll aufgeteilt werden &rarr; **Wenn** der Split-Workflow abgeschlossen ist &rarr; **Dann** werden neue Einheiten mit proportional verteilten MEA- und Flächenwerten erstellt.

- **Gegeben** ein Merge- oder Split-Vorgang wird gestartet &rarr; **Wenn** ein abhängiger Datensatz blockiert ist &rarr; **Dann** verhindert das System den Start und zeigt eine Validierungswarnung.

- **Gegeben** ein Workflow ist abgeschlossen &rarr; **Wenn** die Änderungen übernommen wurden &rarr; **Dann** werden alle betroffenen Datensätze archiviert und die neue Struktur im Audit-Log dokumentiert.

## Nicht-Ziele

- Keine automatisierte Berechnung baurechtlicher oder genehmigungspflichtiger Änderungen.

- Kein Import externer CAD- oder GIS-Daten.

- Keine visuelle Gebäudedarstellung oder Planansicht im MVP.

## Kritische Fälle

- **Fehlerhafte Aggregation:** Falsch berechnete Flächen oder MEA-Werte führen zu unbalancierten Eigentumsverhältnissen.

- **Unvollständige Historisierung:** Fehlende Archivdatensätze verhindern die Nachvollziehbarkeit der Änderungen.

- **Offene Zählerablesungen:** Aktive Messpunkte dürfen keine offenen Werte enthalten, bevor ein Merge/Split durchgeführt wird.

- **Parallelvorgänge:** Zeitgleiche Änderungen an derselben Einheit müssen systemseitig ausgeschlossen werden.

## Abhängigkeiten

-  – Grundlage für die Einheiten- und Eigentümerdaten.

-  – Synchronisierung der Zähler- und Verbrauchsdaten.

-  – Übernahme der Kostenverteilung nach Merge oder Split.

-  – Protokollierung aller Vorgänge und Statusänderungen.

-  – Prüfmechanismen für Flächen, MEA und Konsistenz.

## Offene Fragen

- Soll die Aufteilung nach festen Prozentwerten oder über definierte Flächenangaben erfolgen?

- Werden bei Eigentümerwechsel während eines Merge/Split-Vorgangs zusätzliche Freigaben benötigt?

- Wie sollen Zählerstände mit unterschiedlichen Stichtagen behandelt werden?

## Zukunftserweiterungen

- Unterstützung für grafische Merge-/Split-Visualisierung im Gebäudeplan.

- Automatische Vorschlagslogik für MEA- und Flächenverteilung.

- Integration in zukünftige BIM-/GIS-Schnittstellen.

- Erweiterte Änderungsprotokolle mit Änderungsvergleichen (Diff-Ansicht).

## Verknüpfte Tasks

- [WEG-430 – Unit Merge Workflow](https://maierharry.atlassian.net/browse/WEG-430) – Implementierung der Zusammenführungslogik inklusive Validierung und Archivierung.

- [WEG-431 – Unit Split Workflow](https://maierharry.atlassian.net/browse/WEG-431) – Implementierung der Aufteilungslogik mit Flächen- und MEA-Verteilung.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Merge- und Split-Workflows mit Validierung, Historisierung, Audit-Log und Reporting.

**Phase 2**

Erweiterte Prüfmechanismen, automatische MEA-/Flächenvorschläge, UI-Optimierung.

**Phase 3**

Integration von BIM-/GIS-Daten, grafische Planungsansicht und Simulationen.