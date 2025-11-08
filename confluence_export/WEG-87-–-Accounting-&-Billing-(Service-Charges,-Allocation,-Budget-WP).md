---
title: WEG-87 – Accounting & Billing (Service Charges, Allocation, Budget/WP)
confluence_id: 26968730
version: 12
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/26968730/WEG-87+Accounting+Billing+Service+Charges+Allocation+Budget+WP
---

**JIRA-Link:** [WEG-87 – Accounting & Billing (Service Charges, Allocation, Budget/WP)](https://maierharry.atlassian.net/browse/WEG-87)

## Überblick
Das Modul **Accounting & Billing** (WEG-87) ist das Kernsystem für die Verwaltung, Berechnung und Abrechnung aller gemeinschaftlichen Kosten einer WEG. Es bildet die Grundlage für Umlagen, Wirtschaftspläne und Jahresabrechnungen, um eine transparente, nachvollziehbare und rechtssichere Kostenverteilung zu gewährleisten. Das Modul vereint sämtliche Mechanismen für Kostenstellen, Verteilungsschlüssel, Sollstellungen, Anpassungsabrechnungen und Freigabeprozesse.

## Beschreibung
WEG-87 automatisiert die gesamte Prozesskette der Kostenverteilung in Eigentümergemeinschaften. Von der Erfassung und Kategorisierung der Kosten über die Berechnung von Umlagen bis hin zur Erstellung und Veröffentlichung von Abrechnungsdokumenten – jede Phase wird zentral gesteuert und nachvollziehbar dokumentiert. Das System integriert sich mit den Finanzmodulen (WEG-8) sowie den Eigentümerkonten (WEG-58) und sorgt so für eine konsistente Buchführung zwischen Sollstellungen, Zahlungseingängen und offenen Posten.

Hauptfunktionen:

- **Kostenstellen & Kontenzuordnung:** Verwaltung von Kostenarten und deren Zuordnung zu Konten wie Strom, Wartung oder Versicherung.

- **Verteilungsschlüssel:** Flexible Definition von Umlageschlüsseln nach MEA, Fläche, Verbrauch oder festen Anteilen; Kombination aus fixen und variablen Werten möglich.

- **Kostenpositionen:** Abbildung einzelner Buchungen oder aggregierter Kostenblöcke, optional mit direkter Verknüpfung zu Gebäuden oder Einheiten.

- **Wirtschaftsplan (WP):** Erstellung, Prüfung und Freigabe von Wirtschaftsplänen inklusive Sollstellungen pro Eigentümer und Zeitraum.

- **Jahresabrechnung:** Automatische Berechnung der tatsächlichen Kosten, Ermittlung von Abweichungen zum Wirtschaftsplan und Generierung von Nachzahlungen oder Gutschriften.

- **Zwischenabrechnungen:** Optionale Erstellung für Eigentümerwechsel oder unterjährige Perioden.

- **Dokumentenerstellung:** Automatische Generierung von PDF-Abrechnungen über WEG-53 (Template Engine) mit Branding nach WEG-56.

- **Plausibilitätsprüfungen:** Automatische Validierung von Schlüsseln, Summen und Differenzen vor Freigabe.

- **Revisionssicherheit:** Jede Berechnung, Änderung oder Freigabe wird im Audit-Log (WEG-24) dokumentiert.

- **Bankintegration:** Automatische Zuordnung von Buchungen aus WEG-82/83 zur Ermittlung offener Posten und Zahlungsstände.

## Geschäftsregeln & Logik
- Abrechnungen erfolgen ausschließlich in geschlossenen, versionierten Perioden.

- Umlageschlüssel müssen vollständig und widerspruchsfrei sein.

- Anpassungen (z. B. MEA-Änderungen) sind nur vor Periodenabschluss zulässig.

- Freigaben erzeugen revisionssichere Snapshots; Änderungen danach erfordern eine neue Version.

- Eigentümer ohne aktive Zuordnung werden nicht abgerechnet.

- Der Wirtschaftsplan gilt erst nach optionaler Beiratsfreigabe.

- Abweichungen > 10 % gegenüber der Vorperiode lösen eine Warnung aus.

- Bei Eigentümerwechseln wird die Periode anteilig aufgeteilt.

## Akzeptanzkriterien
- **Gegeben** eine Kostenstelle ist einer WEG zugeordnet &rarr; **Wenn** ein Wirtschaftsplan erstellt wird &rarr; **Dann** werden alle Kosten gemäß definiertem Verteilungsschlüssel korrekt verteilt.

- **Gegeben** Buchungen aus dem Banking-Modul wurden importiert &rarr; **Wenn** sie Kostenarten zugeordnet sind &rarr; **Dann** werden sie automatisch in die Abrechnung übernommen und in den Eigentümerkonten gespiegelt.

- **Gegeben** eine Jahresabrechnung ist abgeschlossen &rarr; **Wenn** Nachzahlungen entstehen &rarr; **Dann** erzeugt das System automatisch Soll-Einträge im Eigentümerkonto und protokolliert sie im Audit-Log.

- **Gegeben** ein neuer Umlageschlüssel wird erstellt &rarr; **Wenn** er aktiviert wird &rarr; **Dann** gilt er für alle zukünftigen Perioden und wird im Wirtschaftsplan berücksichtigt.

- **Gegeben** eine Abrechnung wird veröffentlicht &rarr; **Wenn** das PDF generiert wird &rarr; **Dann** enthält es alle Buchungen, Umlageschlüssel und Summen und wird archiviert.

## Nicht-Ziele
- Keine Integration mit Steuer- oder Buchhaltungssoftware (DATEV, ELSTER) im MVP.

- Kein automatischer Bankeinzug oder Zahlungsverkehr (PSD2/SEPA folgt später).

- Keine KI-basierte Kostenanalyse in Phase 1.

- Keine individuellen Freigabeprozesse je Eigentümer im MVP (nur global durch Verwaltung).

## Kritische Fälle
- **Fehlerhafte Umlageschlüssel:** Ungültige Zuordnungen führen zu falschen Berechnungen – Validierung zwingend erforderlich.

- **Unvollständige Buchungen:** Doppelte oder fehlende Einträge aus dem Banking müssen erkannt und abgefangen werden.

- **Periodenüberschneidung:** Eine neue Abrechnung darf nicht gestartet werden, wenn die vorherige nicht geschlossen ist.

- **Rundungsdifferenzen:** Dezimalabweichungen müssen automatisch ausgeglichen werden.

- **Nachträgliche Änderungen:** Anpassungen nach Freigabe erzwingen eine neue Revision, keine Überschreibungen.

## Abhängigkeiten
- WEG-8 – Finance & Banking – Grundlage für Buchungen, Kostenarten und Importdaten.

- WEG-58 – Owner Ledger & Balances – Verwaltung von Sollstellungen und offenen Posten.

- WEG-53 – Template Engine – Generierung der Abrechnungsdokumente.

- WEG-56 – PDF Branding – Anwendung des Corporate Designs.

- WEG-24 – Audit Log – Revisionssichere Nachverfolgung aller Änderungen.

- WEG-45 – CSV Import – Import von Kosten- und Schlüsseldefinitionen.

## Offene Fragen
- Soll die Split-Abrechnung bei Eigentümerwechsel automatisch erfolgen oder manuell gestartet werden?

- Wie granular sollen Umlageschlüssel gepflegt werden (global, gebäudespezifisch oder einheitenbezogen)?

- Soll der Wirtschaftsplan einen Genehmigungs-Workflow beinhalten (Beirat / Verwaltung)?

- Wie werden Rundungsdifferenzen behandelt – global oder pro Einheit?

- Soll im MVP eine Vorschau- oder Simulationsfunktion integriert werden?

## Zukunftserweiterungen
- **PSD2/SEPA-Integration:** Automatisierte Zahlungsabwicklung.

- **Simulationen:** Szenarienplanung und Budgetsimulationen.

- **KI-Kostenerkennung:** OCR-basierte Zuordnung von Buchungen.

- **Externe Schnittstellen:** DATEV- und ELSTER-Integration.

- **Finanzanalytik:** Prognosen, Diagramme und Trendanalysen.

## Verknüpfte Tasks
- [WEG-870 – Service Charges Model & Allocation Keys](https://maierharry.atlassian.net/browse/WEG-870) – Aufbau der Umlagelogik und Kontenzuordnung.

- [WEG-871 – Period Close & Adjustments](https://maierharry.atlassian.net/browse/WEG-871) – Abschluss von Perioden, Nachberechnung und Korrekturjournal.

- [WEG-872 – Annual Statement Draft / Approve / Publish](https://maierharry.atlassian.net/browse/WEG-872) – Erstellung und Veröffentlichung der Jahresabrechnungen.

- [WEG-873 – Budget Planning (Wirtschaftsplan)](https://maierharry.atlassian.net/browse/WEG-873) – Planung und Freigabe künftiger Perioden.

- [WEG-874 – Billing Documents via Templates (WEG-53 / 56)](https://maierharry.atlassian.net/browse/WEG-874) – PDF-Erstellung mit Branding.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Grundfunktionen für Umlagen, Wirtschaftsplan und Jahresabrechnung; manuelle und automatische Kostenverteilung; PDF-Erstellung; Audit-Logging.

**Phase 2**

Erweiterte Buchungslogik, Beiratsfreigabe-Workflow, Rundungsautomatik, Simulationen, Reporting und Split-Abrechnung.

**Phase 3**

KI-gestützte Kostenklassifizierung, Prognosen, SEPA-Integration, DATEV-Export und automatisierte Finanzanalysen.