---
title: WEG-81 – Accounts Setup (Multiple Accounts per Association)
confluence_id: 26968715
version: 10
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/26968715/WEG-81+Accounts+Setup+Multiple+Accounts+per+Association
---

**JIRA-Link:** [WEG-81 – Accounts Setup (Multiple Accounts per Association)](https://maierharry.atlassian.net/browse/WEG-81)

## Überblick
Das Modul **Accounts Setup** (WEG-81) ermöglicht die Einrichtung, Verwaltung und Nachverfolgung mehrerer Bankkonten pro Eigentümergemeinschaft. Jede WEG kann beliebig viele Konten führen – z. B. Betriebskosten-, Rücklagen- oder Instandhaltungskonten –, um finanzielle Bewegungen strukturiert zu trennen. Das Ziel besteht darin, Buchungen eindeutig zuzuordnen, den Zahlungsverkehr transparent zu gestalten und spätere Abrechnungen auf einer sauberen Kontenbasis aufzubauen.

## Beschreibung
WEG-81 bildet die zentrale Verwaltungsebene für Bankkonten im Finanzsystem. Es erlaubt die Anlage, Konfiguration und Statussteuerung mehrerer Konten pro WEG. Jedes Konto wird mit Startsaldo, Bezeichnung, Typ und optionalen Attributen (z. B. &bdquo;Treuhand&ldquo; oder &bdquo;Rücklage&ldquo;) gepflegt. Bei Bedarf kann ein Konto als Standardkonto markiert werden, das automatisch bei manuellen Buchungen vorausgewählt wird. Inaktive oder geschlossene Konten bleiben in Berichten erhalten, werden jedoch von neuen Buchungen ausgeschlossen.

Hauptfunktionen:

- **Mehrkontenverwaltung:** Anlage und Verwaltung beliebig vieler Konten pro WEG, jeweils mit eindeutiger Bezeichnung und Startsaldo.

- **Kontotypen & Tags:** Klassifizierung nach Verwendungszweck (z. B. Betriebskosten, Rücklage, Instandhaltung) mit optionalen Markierungen.

- **Standardkonto-Logik:** Möglichkeit, ein Konto als Standard für manuelle Buchungen zu definieren.

- **Statusverwaltung:** Konten können aktiv, inaktiv oder geschlossen sein; geschlossene Konten sind schreibgeschützt.

- **Lösch- und Sperrlogik:** Löschung ist nur möglich, wenn keine Buchungen oder Journalreferenzen existieren; andernfalls erfolgt Deaktivierung.

- **Audit-Trail:** Jede Änderung, Deaktivierung oder Wiederaktivierung wird revisionssicher im Audit-Log (WEG-24) protokolliert.

- **Kontoübersicht:** Tabellarische Ansicht aller Konten mit Saldo, Status und letzten Bewegungen.

## Geschäftsregeln & Logik
- Jede Buchung muss genau einem Konto zugeordnet sein.

- Startsaldo ist bei der Anlage verpflichtend.

- Konten können nicht gelöscht werden, wenn Buchungen existieren; sie müssen deaktiviert werden.

- Änderungen an Konten dürfen abgeschlossene Perioden nicht betreffen.

- Ein Konto kann immer nur einer WEG zugeordnet sein.

## Akzeptanzkriterien
- **Gegeben** ein neues Konto wird angelegt &rarr; **Wenn** der Benutzer Startsaldo, Name und Typ eingibt &rarr; **Dann** wird das Konto erstellt und erscheint in der Übersicht als aktiv.

- **Gegeben** eine manuelle Buchung wird erfasst &rarr; **Wenn** kein Konto ausgewählt ist &rarr; **Dann** verhindert das System die Speicherung und fordert zur Auswahl eines Kontos auf.

- **Gegeben** ein Konto enthält Buchungen &rarr; **Wenn** der Benutzer versucht, es zu löschen &rarr; **Dann** verweigert das System den Vorgang und bietet stattdessen eine Deaktivierung an.

- **Gegeben** ein Konto ist deaktiviert &rarr; **Wenn** der Benutzer neue Buchungen vornimmt &rarr; **Dann** steht dieses Konto nicht zur Auswahl.

- **Gegeben** ein Konto ist als Standard markiert &rarr; **Wenn** eine manuelle Buchung geöffnet wird &rarr; **Dann** ist dieses Konto automatisch vorausgewählt.

## Nicht-Ziele
- Keine direkte Bankkontoeröffnung oder -schließung über APIs.

- Keine Verwaltung von Kredit- oder Fremdwährungskonten im MVP.

- Keine automatische Saldenabfrage im MVP.

## Kritische Fälle
- **Fehlender Startsaldo:** Anlage ohne Startsaldo darf nicht möglich sein.

- **Falsche Kontozuordnung:** Falsch zugeordnete Buchungen müssen korrigierbar, aber revisionssicher dokumentiert sein.

- **Versehentliche Löschung:** Das System muss verhindern, dass Konten mit Buchungen gelöscht werden.

- **Dateninkonsistenz:** Änderungen am Kontotyp dürfen keine bestehenden Buchungen beeinflussen.

## Abhängigkeiten
- WEG-24 – Audit Log – Protokollierung aller Kontoänderungen und Statuswechsel.

- WEG-82 – Banking Inbound – Quelle für importierte Buchungen, die Konten zugeordnet werden müssen.

- WEG-84 – Account Evolution Report – Grundlage für periodische Saldenberichte.

- WEG-87 – Accounting & Billing – Nutzung der Konten für Buchungs- und Abrechnungsprozesse.

## Offene Fragen
- Soll das System Mehrwährungskonten mit automatischer Umrechnung unterstützen?

- Welche Kontotags (z. B. &bdquo;Treuhand&ldquo;, &bdquo;Rücklage&ldquo;) sollen standardmäßig verfügbar sein?

- Ist eine Validierung der IBANs im MVP erforderlich?

## Zukunftserweiterungen
- **PSD2-Anbindung:** Direkter Zugriff auf Banksalden und Transaktionen über Schnittstellen.

- **Automatische Saldenabgleiche:** Regelmäßiger Soll/Ist-Vergleich zwischen Bank und System.

- **Mehrwährungsfähigkeit:** Verwaltung und Umrechnung von Fremdwährungskonten.

- **Erweiterte Reports:** Darstellung der Kontenbewegungen über Zeiträume mit Filter- und Exportoptionen.

## Verknüpfte Tasks
- [WEG-810 – Multiple Accounts per Association](https://maierharry.atlassian.net/browse/WEG-810) – Implementierung der Mehrkontoverwaltung mit Status- und Standardkontofunktion.

- [WEG-811 – Account Validation & Rules](https://maierharry.atlassian.net/browse/WEG-811) – Prüfregeln zur Kontoeinrichtung und Saldenlogik.

- [WEG-812 – Account Overview UI](https://maierharry.atlassian.net/browse/WEG-812) – Benutzeroberfläche zur Verwaltung und Übersicht aller Konten.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Einrichtung mehrerer Konten pro WEG, Startsaldo, Standardkonto-Logik, Aktiv-/Inaktiv-Status und Audit-Trail.

**Phase 2**

PSD2-Schnittstellen, automatische Saldenabgleiche und erweiterte Validierungsregeln.

**Phase 3**

Mehrwährungsfähigkeit, Bankintegration und erweiterte Berichts- und Exportfunktionen.