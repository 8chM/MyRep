---
title: WEG-59 – Financial Onboarding & Initialization
confluence_id: 27722309
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722309/WEG-59+Financial+Onboarding+Initialization
---

**JIRA-Link:** [WEG-59 – Financial Onboarding & Initialization](https://maierharry.atlassian.net/browse/WEG-59)

## Überblick

Das Modul **Financial Onboarding & Initialization** (WEG-59) stellt sicher, dass beim Start einer neuen WEG alle finanziellen Daten korrekt, konsistent und nachvollziehbar initialisiert werden. Es bildet die Brücke zwischen der Erstellung einer neuen WEG (WEG-3) und den ersten produktiven Finanzvorgängen (WEG-8). Ziel ist ein kontrollierter Übergang von manuellen oder externen Buchhaltungsdaten in das System – mit Validierung, Import, Freigabe und vollständiger Dokumentation des Initialzustands.

## Beschreibung

WEG-59 definiert alle Prozesse, die notwendig sind, um eine neue WEG oder ein neues Geschäftsjahr im System zu aktivieren. Das Modul bündelt Datenmigration, Erfassung von Anfangssalden und Konsistenzprüfungen. Dabei werden Bankkonten, Eigentümerkonten, Vertragsdaten, Umlageschlüssel und offene Posten aufeinander abgestimmt, bevor die operative Buchung beginnt.

**Hauptfunktionen:**

- **Onboarding Wizard:** Geführter Prozess, der Administratoren Schritt für Schritt durch die Initialisierung führt (Konten, Eigentümer, Verträge, Umlagen).

- **CSV Templates & Validators:** Standardisierte Importvorlagen für Bank- und Eigentümerkonten; alle Eingaben werden syntaktisch und fachlich geprüft.

- **Opening Balances Import:** Übernahme der Anfangssalden aus bisherigen Systemen oder externen Quellen mit automatischer Erkennung von Inkonsistenzen.

- **Contracts/Costs Carryover:** Automatisches Überführen laufender Verträge und wiederkehrender Kostenpositionen in das neue Wirtschaftsjahr.

- **Consistency Checks & Reports:** Prüfung, ob Summen der Eigentümerkonten, Bankbestände und Umlagen übereinstimmen; Abweichungen werden hervorgehoben.

- **Snapshot & Cutover Lock:** Sperrung des Stichtagsbestands nach erfolgreichem Abschluss; dieser dient als Referenz für alle Folgeperioden.

- **Rollback & Safe-Start Option:** Möglichkeit, bei fehlerhaften Importen oder Prüfergebnissen das Onboarding rückgängig zu machen, ohne Datenverlust.

- **Approval & Sign-off Document:** Automatische Erstellung eines Freigabeprotokolls mit allen initialisierten Daten und Unterschriftenfeldern für Verwaltung und Beirat.

- **Audit Logging & Dashboard:** Vollständige Protokollierung aller Onboarding-Schritte mit Übersicht über Importstatus, Fehlermeldungen und Prüfberichte.

## Geschäftsregeln & Logik

- **Datenintegrität:** Alle importierten Datensätze müssen numerisch, strukturell und logisch konsistent sein (Summen, Salden, Zuordnungen).

- **Atomare Prozesse:** Kein Zwischenspeichern halbfertiger Onboardings – jeder Import läuft als abgeschlossener Job.

- **Abbruch bei Fehlern:** Der Importprozess darf bei Widersprüchen oder Validierungsfehlern nicht fortgesetzt werden.

- **Nachvollziehbarkeit:** Jeder Schritt (Import, Korrektur, Freigabe) wird protokolliert und ist jederzeit reproduzierbar.

- **Sperrmechanismus:** Nach erfolgreichem Abschluss sind Daten schreibgeschützt; Änderungen erfolgen nur über genehmigte Nachträge.

- **Abhängigkeit:** Das Modul ist Voraussetzung, bevor Buchungen in WEG-58 (Owner Ledger) oder WEG-87 (Accounting & Billing) aktiv werden können.

## Akzeptanzkriterien

- **Gegeben** ein neuer Verband wird im System angelegt &rarr; **Wenn** der Onboarding Wizard durchlaufen wird &rarr; **Dann** werden alle relevanten Finanzdaten vollständig initialisiert und validiert.

- **Gegeben** ein CSV-Import enthält fehlerhafte Datensätze &rarr; **Wenn** der Validator diese erkennt &rarr; **Dann** wird der Import abgebrochen und eine detaillierte Fehlermeldung angezeigt.

- **Gegeben** ein Onboarding wurde erfolgreich abgeschlossen &rarr; **Wenn** das Cutover Lock gesetzt wird &rarr; **Dann** sind alle Anfangssalden fixiert und revisionssicher archiviert.

- **Gegeben** ein Administrator führt eine Korrektur durch &rarr; **Wenn** ein Rollback initiiert wird &rarr; **Dann** wird der vorherige Stand wiederhergestellt und im Audit Log dokumentiert.

- **Gegeben** das Freigabeprotokoll wird erstellt &rarr; **Wenn** es durch Verwaltung oder Beirat bestätigt wird &rarr; **Dann** gilt der Onboarding-Prozess als abgeschlossen und wird gesperrt.

## Nicht-Ziele

- Kein automatischer Import aus Fremdsystemen über API im MVP (nur manuell über CSV).

- Keine Integration mit Steuer- oder Buchhaltungssoftware im MVP.

- Keine automatisierte Migration historischer Jahre (nur aktuelles Startjahr).

## Kritische Fälle

- **Ungültige Daten:** Falsch formatierte CSV-Dateien oder inkonsistente Salden müssen zu Abbruch und Fehlermeldung führen.

- **Fehler im Cutover:** Wenn das Lock zu früh gesetzt wird, müssen Wiederherstellungsmechanismen greifen.

- **Teilweise Importe:** Teilweise übernommene Daten (z. B. ohne Eigentümer-Zuordnung) dürfen nicht aktiviert werden.

- **Unvollständige Zustimmung:** Ohne Sign-off darf keine Buchung oder Kostenplanung starten.

## Abhängigkeiten

-  – Grundlage für die Erzeugung neuer WEGs und Datenbanken.

-  – Nutzung der Finanzstrukturen (Konten, Kategorien, Buchungsschema).

-  – Übernahme der Eigentümerkonten und Startsalden.

-  – Grundlage für erste Abrechnungsläufe nach Onboarding.

-  – Bereitstellung der initialen Daten für Audit-Reports.

-  – Speicherung aller Onboarding-Aktivitäten.

## Offene Fragen

- Soll das System alte Kontenstände versioniert speichern (z. B. Vorjahresabschlüsse)?

- Wird eine Teilfreigabe (nur Eigentümerkonten, noch nicht Bankdaten) im MVP erlaubt?

- Soll der Onboarding Wizard mehrere Banken parallel unterstützen?

## Zukunftserweiterungen

- **Direkte Importschnittstellen:** Anbindung an Buchhaltungsprogramme wie DATEV oder Lexware.

- **Automatische Vertragserkennung:** Erkennung und Zuordnung historischer Vertragsdaten.

- **Simulation:** Vorschau des neuen Wirtschaftsjahres mit Fehlerprüfung vor Freigabe.

- **KI-gestützte Validierung:** Erweiterte Prüfungen auf Plausibilität und Inkonsistenzen.

## Verknüpfte Tasks

- [WEG-590 – Onboarding Wizard](https://maierharry.atlassian.net/browse/WEG-590) – Führt Administratoren durch alle Initialisierungsschritte.

- [WEG-591 – CSV Templates & Validators](https://maierharry.atlassian.net/browse/WEG-591) – Stellt strukturierte Importformate und Prüfmechanismen bereit.

- [WEG-592 – Opening Balances Import](https://maierharry.atlassian.net/browse/WEG-592) – Übernimmt Startsalden aus bestehenden Systemen.

- [WEG-593 – Contracts/Costs Carryover](https://maierharry.atlassian.net/browse/WEG-593) – Überträgt wiederkehrende Kostenpositionen.

- [WEG-594 – Consistency Checks & Reports](https://maierharry.atlassian.net/browse/WEG-594) – Überprüft Salden und Datenkonsistenz.

- [WEG-595 – Snapshot & Cutover Lock](https://maierharry.atlassian.net/browse/WEG-595) – Sperrt den Startbestand nach Abschluss.

- [WEG-596 – Rollback & Safe-Start Option](https://maierharry.atlassian.net/browse/WEG-596) – Ermöglicht Wiederherstellung bei Fehlern.

- [WEG-597 – Approval & Sign-off Document](https://maierharry.atlassian.net/browse/WEG-597) – Erstellt Freigabeprotokoll zur Bestätigung durch Verwaltung/Beirat.

- [WEG-598 – Audit Logging](https://maierharry.atlassian.net/browse/WEG-598) – Protokolliert alle Import- und Prüfaktivitäten.

- [WEG-599 – Onboarding Dashboard](https://maierharry.atlassian.net/browse/WEG-599) – Visualisiert Fortschritt und Status des Onboardings.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Geführter Onboarding-Prozess für neue WEGs, CSV-Importe mit Validierung, Erfassung von Anfangssalden, Konsistenzprüfungen, Freigabeprotokoll, Audit-Logging, Cutover-Sperre.

**Phase 2**

Direkte Importschnittstellen (DATEV, API), automatische Vertragsübernahme, erweiterte Berichte, Simulation und Vorschau des neuen Wirtschaftsjahres.

**Phase 3**

Vollautomatische Migration historischer Daten, KI-basierte Fehlererkennung, Echtzeit-Onboarding-Assistent mit Validierung und Empfehlungen.