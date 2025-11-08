---
title: WEG-8 – Finance & Banking
confluence_id: 27460102
version: 17
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27460102/WEG-8+Finance+Banking
---

**JIRA-Link:** [WEG-8 – Finance & Banking](https://maierharry.atlassian.net/browse/WEG-8)

## Beschreibung
Das Modul **WEG-8 – Finance & Banking** bildet das finanzielle Rückgrat des WEG Management Systems (WMS). Es dient der Verwaltung sämtlicher Konten, Buchungen und Finanzflüsse innerhalb einer Eigentümergemeinschaft. Das Modul stellt sicher, dass alle Transaktionen nachvollziehbar, korrekt zugeordnet und revisionssicher gespeichert werden.

Ziel ist eine transparente und rechtssichere Abbildung sämtlicher Finanzbewegungen – von der Buchungserfassung über den Import von Kontoauszügen bis hin zur Zuordnung zu Eigentümern, Einheiten und Kostenstellen. Darüber hinaus bildet WEG-8 die Basis für Abrechnungen, Wirtschaftspläne und Finanzberichte, die in späteren Modulen (z. B. WEG-87) erzeugt werden.

Im MVP steht der **Eingang von Buchungen** im Fokus: manuelle Einträge und Kontoauszugsimporte (CSV/MT940). Zukünftige Phasen erweitern dies um automatisierten Zahlungsverkehr (SEPA/PSD2), Mahnwesen, Prognosen und Finanzexporte für Steuerberater.

## Untermodule
**Untermodul**

**Beschreibung**

**WEG-80 – Finance Master Data**Definiert Kostenarten, Umlageschlüssel (MEA/m&sup2;/Verbrauch/Fix) und Lieferanten; zentrale Quelle für Abrechnung und Budgetierung.

**WEG-81 – Accounts Setup**Verwaltung mehrerer Bankkonten pro WEG (z. B. Betriebskosten, Rücklagen), inklusive Startsalden und Zuordnung von Buchungen.

**WEG-82 – Banking Inbound (Manual + CSV/MT940)**Importpipeline für Kontoauszüge, manuelle Buchungen, Deduplikation und Vorschau vor der Freigabe.

**WEG-83 – Matching Heuristics & Partial Allocation**Automatische Zuordnung von Zahlungen zu offenen Posten anhand von Betrag, IBAN, Datum und Verwendungszweck.

**WEG-84 – Account Evolution Report**Entwicklung von Kontensalden über Zeiträume; Berechnung von Opening- und Closing-Balances.

**WEG-85 – Statement Review & Lock**Workflow zur Prüfung und abschließenden Sperrung von Kontoauszügen zur Sicherstellung der Revisionssicherheit.

**WEG-86 – Import Profiles & Duplicate Detection**Verwaltung wiederkehrender Importprofile, Erkennung und Vermeidung doppelter Transaktionen.

**WEG-87 – Accounting & Billing**Zentrale Logik für Umlagen, Periodenabschlüsse und Wirtschaftspläne auf Basis der importierten Finanzdaten.

**WEG-88 – Finance Export & Compliance**Standardisierte Exporte (CSV/XLS/PDF) mit Parameter- und Hash-Protokollierung sowie Branding.

**WEG-89 – PSD2/SEPA Flags (Deferred)**Platzhalter für zukünftige Integration des automatisierten Zahlungsverkehrs.

## Geschäftslogik
- **Kontenstruktur:** Jede WEG kann mehrere Bankkonten führen, die unterschiedlichen Zwecken dienen (z. B. Betriebskosten, Rücklagen). Jede Buchung ist eindeutig einem Konto zugeordnet.

- **Import und Validierung:** Kontoauszüge werden über Importprofile eingelesen, überprüft und dedupliziert. Erst nach Freigabe werden sie revisionssicher gespeichert.

- **Heuristisches Matching:** Eingehende Buchungen werden automatisch offenen Forderungen zugeordnet. Teilzahlungen erzeugen Restposten und werden im Audit-Log dokumentiert.

- **Finanzintegration:** Abrechnungs- und Budgetdaten (WEG-87) nutzen dieselben Kostenarten und Umlageschlüssel aus WEG-80, um fehlerfreie Übergänge zwischen Buchhaltung und Abrechnung zu gewährleisten.

- **Berichte und Exporte:** Saldenverläufe, Kontoentwicklungen und Abrechnungsunterlagen können als PDF oder CSV exportiert werden.

- **Revisionssicherheit:** Nach Freigabe (WEG-85) werden Kontoauszüge gesperrt und Änderungen ausschließlich über nachvollziehbare Revisionen erlaubt.

- **Compliance und Datenschutz:** Alle Finanzdaten unterliegen den Datenschutz- und Retention-Regeln (WEG-26, WEG-54); Exporte werden auditiert (WEG-24).

## Akzeptanzkriterien

- **Gegeben** ein Kontoauszug im CSV/MT940-Format &rarr; **Wenn** dieser importiert und geprüft wird &rarr; **Dann** wird er vollständig angezeigt, dedupliziert und nach Freigabe gesperrt.

- **Gegeben** eine eingehende Zahlung &rarr; **Wenn** die Matching-Heuristik einen Treffer findet &rarr; **Dann** ordnet das System diese Zahlung automatisch der passenden Forderung zu und dokumentiert die Zuordnung.

- **Gegeben** eine veröffentlichte Abrechnung &rarr; **Wenn** Eigentümerauszüge erzeugt werden &rarr; **Dann** enthalten diese alle Buchungen, Salden und Zuordnungen der jeweiligen Einheit.

- **Gegeben** ein Wirtschaftsplan wird erstellt &rarr; **Wenn** Vertragskosten aus WEG-57 vorliegen &rarr; **Dann** übernimmt das System diese automatisch in die Budgetposten.

- **Gegeben** ein geprüfter Kontoauszug &rarr; **Wenn** ein Export erstellt wird &rarr; **Dann** wird der Export mit Hash und Parametern protokolliert und archiviert.

## Nicht-Ziele
- Kein aktiver Zahlungsverkehr (SEPA-Dateien, Online-Banking-Sync) im MVP.

- Keine direkte Integration mit externer Finanzbuchhaltung (DATEV, ELSTER).

- Kein automatisches Mahnwesen oder Inkasso.

- Keine KI-basierten Finanzanalysen oder Prognosen in Phase 1.

## Kritische Fälle
- **Fehlimport:** Fehlerhafte Formatierung oder Importprofile führen zum Abbruch; unvollständige Daten dürfen nicht gespeichert werden.

- **Doppelte Buchungen:** Das System erkennt und blockiert doppelte Transaktionen automatisch.

- **Falsche Zuordnung:** Bei Mehrdeutigkeiten fordert das System eine manuelle Bestätigung.

- **Periodenübergreifende Änderungen:** Abgeschlossene Perioden dürfen nicht rückwirkend verändert werden.

- **Datenverlust:** Unterbrechungen beim Importprozess müssen Wiederaufnahmen ohne Datenverlust ermöglichen.

## Abhängigkeiten
- WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite): Grundlage für API, Scheduler und Datenbankstruktur der Finanzmodule.

- WEG-3 – Tenant Provisioning & Admin: Verantwortlich für die mandantenbezogene Datenhaltung und Schema-Zuweisung.

- WEG-5 – Document Management & Templates: Speicherung, Versionierung und Export von Finanzdokumenten.

- WEG-7 – Metering (Manual Readings & Lifecycle): Lieferung von Verbrauchsdaten zur Kostenverteilung.

- WEG-12 – Error Handling, Logging & Health: Scheduler und Überwachung von Importprozessen.

- WEG-21 – RBAC Roles & Policies per Association: Steuerung des rollenbasierten Zugriffs auf Finanzdaten.

- WEG-24 – Audit Log (User/Roles/Settings): Nachvollziehbare Dokumentation sämtlicher Finanzoperationen.

- WEG-26 – Data Privacy & Redaction (GDPR Base): Sicherstellung der DSGVO-Konformität und Datenanonymisierung.

- WEG-53 – Template Engine (Foundation): Erstellung strukturierter Finanzberichte und Dokumente.

- WEG-56 – PDF Branding Base (per Association): Corporate Design und Layout für alle Finanzexporte.

- WEG-57 – Contract Management (Vendors, Maintenance, Insurance): Übergabe von Vertragskosten und Laufzeiten in die Budgetplanung.

- WEG-76 – Period Lock & Snapshots (for later Billing): Verwaltung abgeschlossener Perioden und Sperrlogik für Finanzdaten.

## Offene Fragen
- Soll das System mehrere Währungen gleichzeitig unterstützen?

- Sollen Importprofile standardisiert ausgeliefert werden?

- Wie sollen fehlerhafte Zuordnungen im Audit-Log dargestellt werden?

- Ist eine digitale Signatur von Abrechnungen vorgesehen?

- Wie granular sollen Konten- und Kostenarten konfigurierbar sein?

## Zukunftserweiterungen
- **Automatisierter Zahlungsverkehr (PSD2/SEPA):** Online-Bank-Sync und Ausführung von Überweisungen.

- **Erweiterte Heuristiken & KI:** Verbesserung der Zuordnungslogik und Prognose zukünftiger Zahlungen.

- **Mahnwesen & Inkasso:** Automatische Mahnläufe mit Eskalationsstufen.

- **OCR-Import:** Automatische Erkennung von Rechnungsdokumenten und deren Zuordnung zu Buchungen.

- **FiBu-Schnittstellen:** Direkte Übergabe an DATEV oder ELSTER.

- **Dashboards:** Visualisierung von Liquidität, Budget und Prognosen.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Kernfunktionen für Buchungsimport (CSV/MT940), manuelle Eingaben, Zuordnung offener Posten, Saldenentwicklung, Review- und Lock-Workflow, Exporte mit Audit-Trail.

**Phase 2**

Automatisierter Zahlungsverkehr (SEPA/PSD2), erweiterte Heuristiken, Dashboards, OCR-Import.

**Phase 3**

KI-gestützte Finanzanalysen, FiBu-Integration, Mahnwesen und vollständige Automatisierung.