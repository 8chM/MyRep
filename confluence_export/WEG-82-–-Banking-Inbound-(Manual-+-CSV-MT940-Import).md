---
title: WEG-82 – Banking Inbound (Manual + CSV/MT940 Import)
confluence_id: 27460117
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27460117/WEG-82+Banking+Inbound+Manual+CSV+MT940+Import
---

**JIRA-Link:** [WEG-82 – Banking Inbound (Manual + CSV/MT940 Import)](https://maierharry.atlassian.net/browse/WEG-82)

## Überblick
Das Modul **Banking Inbound** (WEG-82) bildet die Grundlage für den Import, die Validierung und die manuelle Erfassung von Bankbuchungen. Es erlaubt den Upload und die Analyse von Kontoauszügen im CSV- oder MT940-Format, führt Deduplikationsprüfungen durch und stellt sicher, dass Buchungen nur einmalig, korrekt und vollständig übernommen werden. Das Ziel besteht darin, Buchungen revisionssicher zu importieren und eine einheitliche Verbindung zwischen Bankdaten und Finanzprozessen (WEG-8) herzustellen.

## Beschreibung
WEG-82 verwaltet die Einleseprozesse für externe Kontoauszüge und ermöglicht zusätzlich die manuelle Erfassung einzelner Buchungen. Benutzer können Auszüge hochladen, prüfen, Zeilen selektiv übernehmen oder ausschließen und anschließend sperren, um nachträgliche Änderungen zu verhindern. Alle Importe durchlaufen Validierungs- und Deduplikationsmechanismen, die sicherstellen, dass Buchungen nur einmal verarbeitet werden. Das Modul ist vollständig in das Kontenmanagement (WEG-81) und die Deduplikationslogik (WEG-86) integriert.

Hauptfunktionen:

- **Dateiimport (CSV/MT940):** Upload von Kontoauszügen über standardisierte Formate mit automatischer Feldzuordnung.

- **Importprofile:** Verwendung von vordefinierten Profilen für unterschiedliche Banken und Dateiformate.

- **Vorschau & Deduplikation:** Anzeige aller Buchungszeilen mit Erkennung potenzieller Duplikate und Unstimmigkeiten.

- **Zeilenselektion:** Möglichkeit, einzelne Buchungen manuell zu aktivieren oder vom Import auszuschließen.

- **Saldoabgleich:** Überprüfung der Opening- und Closing-Balances zur Sicherstellung der Datenintegrität.

- **Manuelle Buchungserfassung:** Eingabe einzelner Transaktionen mit denselben Validierungsregeln wie bei Importen.

- **Sperrmechanismus:** Nach Abschluss wird der Import automatisch schreibgeschützt.

- **Audit-Trail:** Jeder Import, jede Änderung und jeder Ausschluss wird im Audit-Log (WEG-24) dokumentiert.

## Geschäftsregeln & Logik
- Jeder Import muss einem Konto (WEG-81) eindeutig zugeordnet sein.

- Doppelte Buchungen dürfen nicht mehrfach persistiert werden.

- Fehlerhafte oder unvollständige Zeilen müssen ausgeschlossen oder manuell korrigiert werden.

- Der Import darf nur mit gültigen Profilen durchgeführt werden.

- Nach der Sperrung darf kein Import mehr bearbeitet werden.

## Akzeptanzkriterien
- **Gegeben** ein MT940- oder CSV-Auszug liegt vor &rarr; **Wenn** der Benutzer ihn importiert &rarr; **Dann** zeigt das System eine Vorschau mit Deduplikationshinweisen und Saldenprüfung an.

- **Gegeben** ein falsches Importprofil wurde gewählt &rarr; **Wenn** der Benutzer den Import startet &rarr; **Dann** wird der Vorgang abgebrochen und eine Warnung angezeigt.

- **Gegeben** ein Benutzer schließt bestimmte Buchungszeilen aus &rarr; **Wenn** der Import abgeschlossen wird &rarr; **Dann** werden nur die verbleibenden Zeilen gespeichert und der Ausschluss protokolliert.

- **Gegeben** ein Import wurde abgeschlossen &rarr; **Wenn** der Benutzer versucht, ihn erneut zu öffnen &rarr; **Dann** wird der Zugriff verweigert, da der Datensatz schreibgeschützt ist.

- **Gegeben** ein Duplikat wird erkannt &rarr; **Wenn** der Benutzer den Import bestätigt &rarr; **Dann** wird eine doppelte Buchung verhindert und im Audit protokolliert.

## Nicht-Ziele
- Kein automatischer Online-Abruf von Bankauszügen im MVP.

- Keine Unterstützung für weitere Formate als CSV und MT940.

- Keine Echtzeitsynchronisation mit Bankkonten (PSD2 erst in späteren Phasen).

## Kritische Fälle
- **Falsches Profil:** Führt zu Abbruch des Imports, um Datenkorruption zu vermeiden.

- **Doppelte Importe:** Wiederholter Import derselben Datei darf keine Duplikate erzeugen.

- **Saldoabweichungen:** Differenzen zwischen Opening- und Closing-Balances müssen als Warnung angezeigt werden.

- **Unvollständige Daten:** Leere oder unlesbare Zeilen dürfen nicht persistiert werden.

## Abhängigkeiten
- WEG-12 – Error Handling, Logging & Health – Überwacht Importprozesse und Fehler.

- WEG-24 – Audit Log – Dokumentiert jeden Importvorgang und dessen Ergebnisse.

- WEG-81 – Accounts Setup – Stellt die Konten bereit, denen Buchungen zugeordnet werden.

- WEG-86 – Import Profiles & Duplicate Detection – Definiert Profile und Deduplikationslogik.

## Offene Fragen
- Soll das System typische Formatfehler (z. B. Dezimaltrennzeichen, Datumsformate) automatisch korrigieren?

- Sollen Standardprofile für gängige Banken im MVP enthalten sein?

- Soll die manuelle Buchungserfassung als separates UI oder integriert im Importdialog erfolgen?

## Zukunftserweiterungen
- **PSD2/HBCI-Pull:** Automatischer Abruf von Kontoauszügen über Schnittstellen.

- **OCR-Belegerkennung:** Automatische Erfassung von Rechnungsdaten aus PDF-Dokumenten.

- **Profil-Editor:** Benutzerfreundliche Oberfläche zum Erstellen eigener Importprofile.

- **Erweiterte Duplikaterkennung:** Abgleich über Betrag, IBAN, Datum und Verwendungszweck.

## Verknüpfte Tasks
- [WEG-820 – Manual Bank Entries (income/expense)](https://maierharry.atlassian.net/browse/WEG-820) – Manuelle Buchungserfassung mit Validierung und Kontenzuordnung.

- [WEG-821 – CSV/MT940 Import with Preview & Dedupe](https://maierharry.atlassian.net/browse/WEG-821) – Profilbasierter Import mit Vorschau und Deduplikation.

- [WEG-822 – Statement Review & Lock](https://maierharry.atlassian.net/browse/WEG-822) – Review-Workflow mit finaler Sperrung der Kontoauszüge.

- [WEG-823 – Opening/Closing Balance Handling](https://maierharry.atlassian.net/browse/WEG-823) – Verwaltung und Validierung der Start- und Schlusssalden.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Import von CSV- und MT940-Dateien, Deduplikation, Zeilenselektion, manuelle Buchungserfassung und Sperrmechanismus.

**Phase 2**

PSD2/HBCI-Anbindung, OCR-Funktionen und erweiterte Validierung.

**Phase 3**

Profil-Editor, Standardprofile für Banken und automatisierte Synchronisierung.