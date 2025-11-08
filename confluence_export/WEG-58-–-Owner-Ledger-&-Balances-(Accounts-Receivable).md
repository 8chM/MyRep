---
title: WEG-58 – Owner Ledger & Balances (Accounts Receivable)
confluence_id: 27853477
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27853477/WEG-58+Owner+Ledger+Balances+Accounts+Receivable
---

**JIRA-Link:** [WEG-58 – Owner Ledger & Balances (Accounts Receivable)](https://maierharry.atlassian.net/browse/WEG-58)

## Überblick

Das Modul **Owner Ledger & Balances** (WEG-58) bildet die zentrale Grundlage für die Verwaltung sämtlicher Eigentümerkonten innerhalb des Finanzsystems. Es verwaltet Buchungen, Salden, offene Posten und Ausgleichsvorgänge pro Eigentümer und stellt sicher, dass alle geldbezogenen Transaktionen nachvollziehbar, konsistent und revisionssicher abgebildet werden. Ziel ist es, jederzeit den aktuellen finanziellen Stand jedes Eigentümers – inklusive Umlagen, Nachzahlungen, Rückerstattungen und Forderungen – korrekt auszuweisen und als Basis für Jahresabrechnungen, Wirtschaftspläne und Reporting bereitzustellen.

## Beschreibung

WEG-58 integriert die Eigentümerkontenführung vollständig in das Finanzsystem (WEG-8) und bildet damit das *Subledger* für Eigentümer. Das Modul verknüpft Buchungsvorgänge aus Abrechnungen, Banking und Verträgen, um die Finanzhistorie jedes Eigentümers lückenlos zu dokumentieren.

**Hauptfunktionen:**

- **Ledger Domain:** Verwaltung aller Buchungseinträge auf Eigentümerkonten (Soll/Haben), inklusive Umlagen, Sonderumlagen, Rückerstattungen und Zahlungseingänge.

- **Posting Types:** Vordefinierte Buchungstypen (z. B. Hausgeld, Nachzahlung, Rückzahlung, Anpassung) für einheitliche Kategorisierung.

- **Opening Balances Intake:** Initiale Erfassung der Startsalden je Eigentümer, manuell oder per Import aus vorherigen Systemen.

- **Banking/Matching Bridge:** Automatische Zuordnung von Banktransaktionen (WEG-82/83) zu offenen Forderungen.

- **Adjustments Journal:** Dokumentation nachträglicher Korrekturen mit Begründung, Ersteller und Zeitstempel.

- **Aging & Open Items Report:** Altersstrukturanalyse offener Posten mit Hervorhebung überfälliger Forderungen.

- **Owner Statements:** Generierung monatlicher oder periodischer Kontoauszüge als PDF oder CSV.

- **Audit & Locking:** Sperrmechanismen für abgeschlossene Perioden, um nachträgliche Änderungen zu verhindern.

Das Modul arbeitet eng mit den Buchungslogiken aus **Accounting & Billing (WEG-87)** und den Daten aus **Financial Onboarding (WEG-59)** zusammen. Alle Bewegungen sind vollständig rückverfolgbar und revisionssicher dokumentiert.

## Geschäftsregeln & Logik

- **Doppelte Buchführung:** Jeder Buchungsvorgang erzeugt sowohl eine Gegenbuchung im Ledger als auch einen Eintrag in der Journal-Historie.

- **Periodenbindung:** Buchungen dürfen nur in offenen Perioden erfolgen; gesperrte Perioden sind schreibgeschützt.

- **Saldo-Konsistenz:** Jeder Eigentümer muss einen nachvollziehbaren Anfangs- und Endsaldo besitzen.

- **Automatische Zuordnung:** Zahlungseingänge werden anhand von Betrag, Referenz und Datum heuristisch offenen Forderungen zugeordnet (via WEG-83).

- **Korrekturen:** Nachträgliche Änderungen sind nur über das Adjustments Journal zulässig und werden auditierbar dokumentiert.

- **Reporting-Sicherheit:** Alle Reports (Saldo, Aging, Historie) werden auf Basis des Ledger-Snapshots erstellt, nicht dynamisch auslaufend.

## Akzeptanzkriterien

- **Gegeben** eine neue Buchung wird erfasst &rarr; **Wenn** diese validiert wird &rarr; **Dann** wird sie korrekt in Soll/Haben gebucht und im Ledger protokolliert.

- **Gegeben** ein Bankeintrag wird importiert &rarr; **Wenn** ein passender offener Posten gefunden wird &rarr; **Dann** erfolgt automatische Zuordnung und Ausgleich der Forderung.

- **Gegeben** eine Periode wird abgeschlossen &rarr; **Wenn** der Abschluss durchgeführt wird &rarr; **Dann** wird der Ledger-Saldo gesperrt und für die nächste Periode übernommen.

- **Gegeben** ein Eigentümer hat offene Posten &rarr; **Wenn** ein Aging Report erstellt wird &rarr; **Dann** werden diese korrekt nach Fälligkeit und Zeitraum gegliedert angezeigt.

- **Gegeben** eine manuelle Korrektur wird vorgenommen &rarr; **Wenn** sie bestätigt wird &rarr; **Dann** wird sie als separate Buchung im Adjustments Journal protokolliert.

## Nicht-Ziele

- Kein Echtzeitbanking oder automatische SEPA-Verarbeitung im MVP.

- Keine Integration externer Buchhaltungsprogramme (DATEV) im MVP.

- Kein direktes Mahnwesen – dieses folgt erst in späteren Phasen.

## Kritische Fälle

- **Fehlende Anfangssalden:** Wenn bei Aktivierung keine Startsalden vorhanden sind, muss der Import blockiert werden.

- **Doppelte Buchungen:** Erneute Importe dürfen keine Duplikate erzeugen; doppelte Referenzen werden ignoriert.

- **Fehlerhafte Periodenschließung:** Unterbrochene Abschlüsse dürfen keine Teil-Lockings erzeugen – Recovery-Mechanismus erforderlich.

- **Falsche Zuordnung:** Falsch gematchte Zahlungen müssen rücksetzbar und auditierbar sein.

## Abhängigkeiten

-  – Finanzbuchungen, Bankimport und Kontenstruktur.

-  – Quelle für Zahlungseingänge.

-  – Zuordnung von Zahlungen zu offenen Posten.

-  – Grundlage für periodische Abrechnungen.

-  – Initiale Eigentümerkonten und Anfangssalden.

-  – Ausgabe von Ledger-Daten an externe Reports.

-  – Protokollierung von Ledger-Änderungen.

## Offene Fragen

- Soll es möglich sein, Eigentümerkonten manuell zu saldieren oder ausschließlich über Systembuchungen?

- Wie detailliert sollen Eigentümerberichte im MVP sein (Summen vs. Einzelposten)?

- Ist ein automatischer Ausgleich zwischen Eigentümerkonten (z. B. Miteigentümer) erforderlich?

## Zukunftserweiterungen

- Automatische Mahnläufe bei überfälligen Forderungen.

- Integration von Zahlungsabgleichen über PSD2/SEPA.

- Erweiterte Berichte mit Drill-Down-Funktion.

- KI-gestützte Anomalieerkennung bei Buchungen.

## Verknüpfte Tasks

- [WEG-580 – Ledger Domain & Posting Types](https://maierharry.atlassian.net/browse/WEG-580) – Aufbau des Eigentümerkontenmodells und Buchungstypen.

- [WEG-581 – Opening Balances Intake (owners)](https://maierharry.atlassian.net/browse/WEG-581) – Import und Initialisierung der Startsalden.

- [WEG-582 – Banking/Matching Posting Bridge](https://maierharry.atlassian.net/browse/WEG-582) – Verknüpfung von Zahlungen und offenen Posten.

- [WEG-583 – Charge Schedules Integration](https://maierharry.atlassian.net/browse/WEG-583) – Automatische Übernahme von Umlagen und Abrechnungsbeträgen.

- [WEG-584 – Adjustments Journal](https://maierharry.atlassian.net/browse/WEG-584) – Verwaltung nachträglicher Korrekturen.

- [WEG-585 – Aging & Open Items Report](https://maierharry.atlassian.net/browse/WEG-585) – Generierung von Fälligkeitsberichten.

- [WEG-586 – Owner Statements (PDF/CSV)](https://maierharry.atlassian.net/browse/WEG-586) – Erstellung periodischer Kontoauszüge.

- [WEG-587 – Bank Reconciliation Tools](https://maierharry.atlassian.net/browse/WEG-587) – Abgleich von Kontoauszügen mit Ledger-Daten.

- [WEG-588 – Audit Trail & Locks](https://maierharry.atlassian.net/browse/WEG-588) – Sicherstellung revisionssicherer Periodenabschlüsse.

- [WEG-589 – Data Export Hooks](https://maierharry.atlassian.net/browse/WEG-589) – Übergabe von Ledger-Daten an Finanzexporte.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Verwaltung der Eigentümerkonten mit Saldenführung, Import von Anfangssalden, manuelle Buchungen, Banking-Zuordnung, periodische Abschlüsse, PDF-/CSV-Kontoauszüge, Audit-Logs.

**Phase 2**

Erweiterte Mahnlogik, automatische Zahlungserinnerungen, SEPA-Schnittstelle, erweiterte Abstimmberichte.

**Phase 3**

KI-gestützte Erkennung fehlerhafter Buchungen, Integration mit externen Buchhaltungs-APIs, dynamische Dashboards für Liquiditätsplanung.