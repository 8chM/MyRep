---
title: WEG-83 – Matching Heuristics & Partial Allocation
confluence_id: 27198022
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27198022/WEG-83+Matching+Heuristics+Partial+Allocation
---

**JIRA-Link:** [WEG-83 – Matching Heuristics & Partial Allocation](https://maierharry.atlassian.net/browse/WEG-83)

## Überblick
Das Modul **Matching Heuristics & Partial Allocation** (WEG-83) ist für die intelligente Zuordnung eingehender Banktransaktionen zu offenen Posten innerhalb des Finanzsystems verantwortlich. Es nutzt heuristische Vergleichsregeln, um Zahlungen anhand von Betrag, Datum, IBAN, Verwendungszweck und Referenzen automatisch zuzuordnen. Teilzahlungen werden anteilig verbucht, und verbleibende Restbeträge fließen zurück in das Owner-Ledger (WEG-58). Das Ziel ist es, Zuordnungen zu automatisieren, die Nachvollziehbarkeit zu erhöhen und die manuelle Nachbearbeitung zu minimieren.

## Beschreibung
WEG-83 erweitert die Buchungslogik aus WEG-82 (Banking Inbound) um automatische und teilautomatische Matching-Funktionen. Das Modul arbeitet mit gewichteten Heuristiken, die verschiedene Kriterien – wie Betrag, Datum und Textähnlichkeit – kombinieren, um eine prozentuale Trefferwahrscheinlichkeit zu berechnen. Zahlungen mit hoher Übereinstimmung werden als automatische Vorschläge markiert, andere werden dem Benutzer zur Prüfung angezeigt. Teilzahlungen werden direkt auf offene Posten gebucht, während verbleibende Beträge als Restposten im Eigentümerkonto erhalten bleiben. Alle Vorgänge sind revisionssicher dokumentiert und können rückgängig gemacht werden.

Hauptfunktionen:

- **Heuristische Zuordnung:** Vergleich von Zahlungen mit offenen Posten anhand von Betrag, Datum, IBAN und Verwendungszweck.

- **Trefferwahrscheinlichkeit:** Berechnung einer Matching-Score-Bewertung (0–100 %) zur Unterstützung automatischer Entscheidungen.

- **Automatische Vorschläge:** Eindeutige 100 %-Treffer werden automatisch zugeordnet; andere erfordern manuelle Bestätigung.

- **Teilzuweisungen:** Bei Teilzahlungen wird der Betrag anteilig verbucht, und der Rest verbleibt als offener Posten.

- **Reversibilität:** Jede Zuordnung ist rücksetzbar; Re-Match-Funktion erstellt eine neue Zuordnung unter Beibehaltung der Audit-Historie.

- **Benutzerreview:** Mehrfachtreffer werden in einer priorisierten Liste dargestellt und erfordern manuelle Auswahl.

- **Audit-Trail:** Alle Zuordnungen, Änderungen und Rücknahmen werden im Audit-Log (WEG-24) protokolliert.

## Geschäftsregeln & Logik
- Zahlungen dürfen immer nur einem oder mehreren offenen Posten eindeutig zugeordnet sein.

- 100 %-Treffer werden automatisch vorgeschlagen, sofern keine Konflikte bestehen.

- Teilzahlungen erzeugen Restposten mit eigener Referenz.

- Eine Zuordnung darf nur erfolgen, wenn beide Seiten (Zahlung und Posten) valide und nicht gesperrt sind.

- Re-Matches erzeugen keine Datenlöschung, sondern einen neuen Audit-Eintrag.

## Akzeptanzkriterien
- **Gegeben** eine Zahlung mit eindeutiger Referenz und passendem Betrag &rarr; **Wenn** die Heuristik einen 100 %-Treffer findet &rarr; **Dann** wird der Posten automatisch vorgeschlagen und kann mit einem Klick bestätigt werden.

- **Gegeben** eine Teilzahlung &rarr; **Wenn** der Betrag kleiner als die offene Forderung ist &rarr; **Dann** wird der Betrag anteilig verbucht, und der Rest bleibt als offener Posten bestehen.

- **Gegeben** mehrere potenzielle Treffer &rarr; **Wenn** keine eindeutige Übereinstimmung vorliegt &rarr; **Dann** wird eine Liste der Kandidaten mit prozentualem Score angezeigt.

- **Gegeben** eine falsche Zuordnung &rarr; **Wenn** der Benutzer den Re-Match ausführt &rarr; **Dann** wird die alte Zuordnung aufgehoben und im Audit-Log protokolliert.

- **Gegeben** ein Benutzer versucht, eine Zuordnung rückwirkend zu löschen &rarr; **Wenn** die Periode geschlossen ist &rarr; **Dann** verweigert das System den Vorgang und zeigt einen Hinweis an.

## Nicht-Ziele
- Kein Einsatz von KI-basierten Lernalgorithmen im MVP.

- Keine automatisierte Rückbuchung oder Zahlungsanweisung.

- Keine eigenständige Verarbeitung von Sammelüberweisungen (Batch-Bookings).

## Kritische Fälle
- **Mehrfachtreffer:** Mehrere Posten mit identischem Betrag und Datum erfordern eine manuelle Auswahl.

- **Teilzahlungen:** Ungenau berechnete Restbeträge können zu Rundungsdifferenzen führen.

- **Falsche Zuordnung:** Muss vollständig reversibel und im Audit nachvollziehbar bleiben.

- **Abweichende Währung:** Buchungen in anderen Währungen müssen blockiert werden.

## Abhängigkeiten
- WEG-24 – Audit Log – Dokumentiert alle Zuordnungen und Re-Matches.

- WEG-58 – Owner Ledger & Balances – Verarbeitet Restposten und aktualisiert offene Forderungen.

- WEG-82 – Banking Inbound – Stellt die importierten Transaktionen bereit.

- WEG-87 – Accounting & Billing – Liefert offene Posten aus Abrechnungen.

## Offene Fragen
- Soll es konfigurierbare Schwellenwerte für das Matching-Score geben (z. B. Mindesttrefferquote für Auto-Vorschläge)?

- Soll der Benutzer eigene Matching-Regeln definieren können?

- Wie werden Rundungsdifferenzen bei Teilzuweisungen behandelt?

## Zukunftserweiterungen
- **KI-basiertes Matching:** Einsatz von Machine-Learning-Modellen zur Verbesserung der Trefferquote.

- **Benutzerdefinierte Regeln:** Regel-Editor zur Definition individueller Matching-Kriterien.

- **Selbstlernende Heuristik:** Automatische Gewichtsanpassung auf Basis historischer Zuordnungen.

- **Sammelverarbeitung:** Automatische Gruppierung ähnlicher Zahlungen.

## Verknüpfte Tasks
- [WEG-830 – Amount/Date/Reference/IBAN Heuristics](https://maierharry.atlassian.net/browse/WEG-830) – Implementierung der heuristischen Zuordnungslogik mit Teilzuweisungen und Re-Match-Funktion.

- [WEG-831 – Duplicate Detection Integration](https://maierharry.atlassian.net/browse/WEG-831) – Erkennung von Mehrfachtreffern und Dublettenprüfung.

- [WEG-832 – Matching Review UI](https://maierharry.atlassian.net/browse/WEG-832) – Oberfläche zur Anzeige und manuellen Bearbeitung von Zuordnungsvorschlägen.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Heuristische Zuordnung auf Basis von Betrag, Datum und Referenz; Teilzuweisungen, Re-Match-Funktion, Audit-Trail.

**Phase 2**

KI-gestützte Matching-Engine, regelbasierte Anpassungen, erweiterte Mehrfachtreffer-Erkennung.

**Phase 3**

Vollautomatisches Matching mit lernender Gewichtung, Batch-Verarbeitung und erweiterten Reports.