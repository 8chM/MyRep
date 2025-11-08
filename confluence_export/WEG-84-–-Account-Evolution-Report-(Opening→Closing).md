---
title: WEG-84 – Account Evolution Report (Opening→Closing)
confluence_id: 27656697
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27656697/WEG-84+Account+Evolution+Report+Opening+Closing
---

**JIRA-Link:** [WEG-84 – Account Evolution Report (Opening&rarr;Closing)](https://maierharry.atlassian.net/browse/WEG-84)

## Überblick
Das Modul **Account Evolution Report** (WEG-84) ermöglicht es dem Verwalter, die Entwicklung von Kontensalden über einen definierten Zeitraum hinweg nachzuvollziehen. Es stellt sicher, dass alle Bewegungen zwischen Anfangs- und Endsaldo nachvollziehbar, konsistent und revisionssicher dokumentiert sind. Ziel ist es, die Buchhaltungslogik transparent zu machen und eine einfache Überprüfung der Finanzentwicklung pro Konto oder Kontengruppe zu gewährleisten.

## Beschreibung
WEG-84 stellt eine periodische Auswertung der finanziellen Entwicklung aller oder einzelner Bankkonten einer WEG bereit. Der Report zeigt pro Konto die Anfangssalden (Opening Balance), alle Transaktionen im gewählten Zeitraum und die daraus resultierenden Endsalden (Closing Balance). Die Daten werden aus den Modulen **WEG-80 (Finance Master Data)**, **WEG-81 (Accounts Setup)**, WEG-**82 (Banking Inbound) **und **WEG-83 (Matching)** aggregiert. Der Bericht dient sowohl der internen Kontrolle als auch externen Prüfungen und unterstützt die Erstellung der Jahresabrechnung (WEG-87).

Hauptfunktionen:

- **Periodenbasierte Berichterstellung:** Darstellung der Saldenentwicklung pro Konto, Zeitraum und Buchungsart.

- **Saldo-Nachvollziehbarkeit:** Berechnung der Opening- und Closing-Balances inklusive Plausibilitätsprüfung.

- **Transaktionsaggregation:** Zusammenfassung von Einnahmen, Ausgaben und Umlagen innerhalb der gewählten Periode.

- **Differenzanalyse:** Automatische Prüfung, ob Opening Balance + Transaktionen = Closing Balance ergibt.

- **Filter- und Gruppierungsoptionen:** Selektion nach Zeitraum, Kontotyp oder Kontogruppe.

- **Warnsystem:** Hinweise bei fehlenden Opening-Balances, unplausiblen Summen oder negativen Endsalden.

- **Exportfunktionen:** Generierung von Berichten als PDF, CSV oder XLS.

- **Audit-Trail:** Jede Reportgenerierung wird mit Zeitstempel und Benutzer im Audit-Log (WEG-24) dokumentiert.

## Geschäftsregeln & Logik
- Opening Balance = Closing Balance der Vorperiode oder manuell erfasster Startwert (aus WEG-59).

- Closing Balance = Opening Balance + Summe aller Transaktionen im Zeitraum.

- Differenzen zwischen erwarteten und berechneten Werten werden als Warnungen gekennzeichnet.

- Negative Salden sind nur bei Verbindlichkeitskonten erlaubt.

- Reports dürfen keine überlappenden Zeiträume beinhalten.

- Jeder Bericht ist revisionssicher archiviert und kann erneut reproduziert werden.

## Akzeptanzkriterien
- **Gegeben** eine WEG mit vollständigen Transaktionsdaten &rarr; **Wenn** der Verwalter einen Report für ein bestimmtes Konto und Jahr erstellt &rarr; **Dann** zeigt der Bericht Opening Balance, Transaktionssumme und Closing Balance mit Plausibilitätsprüfung an.

- **Gegeben** ein Konto besitzt keine Opening Balance &rarr; **Wenn** der Bericht generiert wird &rarr; **Dann** wird eine Warnmeldung ausgegeben und das Konto im Ergebnis markiert.

- **Gegeben** es bestehen Differenzen zwischen erwarteter und tatsächlicher Closing Balance &rarr; **Wenn** der Report erzeugt wird &rarr; **Dann** erscheint ein Warnsymbol und ein Hinweis im Bericht.

- **Gegeben** der Benutzer aktiviert den Export &rarr; **Wenn** der Report abgeschlossen ist &rarr; **Dann** wird dieser als PDF/CSV/XLS bereitgestellt und im Audit protokolliert.

- **Gegeben** ein Report überlappt mit einem bestehenden Zeitraum &rarr; **Wenn** die Erstellung gestartet wird &rarr; **Dann** verhindert das System die doppelte Periodenauswertung.

## Nicht-Ziele
- Keine grafische Darstellung oder Trendanalyse im MVP.

- Keine KI-basierte Anomalieerkennung in der ersten Version.

- Kein automatischer Versand von Reports.

## Kritische Fälle
- **Fehlende Opening Balance:** Verhindert korrekte Berechnung – System muss Warnung anzeigen.

- **Periodenüberschneidung:** Doppelte Transaktionszählung muss blockiert werden.

- **Fehlerhafte Aggregation:** Negative oder unplausible Summen müssen markiert werden.

- **Datenänderung nach Reportgenerierung:** Änderungen an Transaktionen dürfen Report-Revisionen nicht überschreiben.

## Abhängigkeiten
- WEG-8 – Finance & Banking – Hauptmodul für Finanzdaten und Buchungssystem.

- WEG-80 – Finance Master Data – Struktur und Kategorisierung der Konten.

- WEG-81 – Accounts Setup – Kontenbasis mit Startsalden.

- WEG-82 – Banking Inbound – Quelle für Transaktionen.

- WEG-83 – Matching Heuristics – Zuordnung von Zahlungen zu offenen Posten.

- WEG-87 – Accounting & Billing – Grundlage für Jahresabschlüsse.

- WEG-24 – Audit Log – Dokumentation der Reporterstellung.

## Offene Fragen
- Soll der Report nachträgliche Korrekturen und Anpassungen automatisch historisieren?

- Wie granular sollen Zeiträume wählbar sein (monatlich, quartalsweise, jährlich)?

- Soll ein Vergleich zweier Jahre (Jahr-über-Jahr) im MVP enthalten sein oder erst später folgen?

## Zukunftserweiterungen
- **Drill-Down & Detailansicht:** Direkter Zugriff auf Einzeltransaktionen über Klick auf Summenwerte.

- **Vergleichsberichte:** Gegenüberstellung mehrerer Wirtschaftsjahre zur Trendanalyse.

- **Grafische Darstellung:** Visualisierung der Kontenentwicklung als Diagramm.

- **KI-basierte Anomalieerkennung:** Automatische Erkennung ungewöhnlicher Saldenabweichungen.

## Verknüpfte Tasks
- [WEG-840 – Opening&rarr;Closing Report](https://maierharry.atlassian.net/browse/WEG-840) – Implementierung der Reporting-Logik mit Berechnung, Validierung und Exportfunktionen.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Basisreport mit Opening/Closing Balance, Transaktionssummen, Differenzanalyse, PDF-/CSV-Export und Audit-Logging.

**Phase 2**

Drill-Down-Ansicht, Vergleichsberichte und XLS-Export.

**Phase 3**

Grafische Darstellung, KI-gestützte Anomalieerkennung und Automatisierungsfunktionen.