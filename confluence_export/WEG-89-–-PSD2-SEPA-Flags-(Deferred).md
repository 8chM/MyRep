---
title: WEG-89 – PSD2/SEPA Flags (Deferred)
confluence_id: 27722354
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722354/WEG-89+PSD2+SEPA+Flags+Deferred
---

**JIRA-Link:** [WEG-89 – PSD2/SEPA Flags (Deferred)](https://maierharry.atlassian.net/browse/WEG-89)

## Überblick
Das Modul **PSD2/SEPA Flags (Deferred)** (WEG-89) dient als vorbereitendes Untermodul für zukünftige Banking-Integrationen nach europäischen Zahlungsrichtlinien (PSD2) und dem SEPA-Standard. Im MVP hat das Modul keine aktive Funktionalität, sondern setzt ausschließlich Datenbank- und UI-Platzhalter, um die spätere Einführung von automatisierten Zahlungsprozessen, Kontoabgleichen und Echtzeittransaktionen vorzubereiten. Ziel ist es, das System bereits technisch vorzubereiten, um in späteren Phasen nahtlos API-gestützte Bankanbindungen aktivieren zu können.

## Beschreibung
WEG-89 schafft die technische Grundlage für zukünftige PSD2- und SEPA-Funktionen, die später eine automatische Synchronisation von Bankdaten, Einzüge, Überweisungen und Echtzeit-Transaktionen ermöglichen sollen. Aktuell existieren im MVP lediglich Datenbankfelder und deaktivierte UI-Optionen, die eine spätere Aktivierung vereinfachen. Die Flags werden bei der Erstellung neuer Bankkonten gesetzt und steuern, ob die zugehörigen Funktionen aktiv sind oder nicht.

Hauptfunktionen:

- **PSD2-Flag:** Markiert, ob eine API-basierte Banking-Integration aktivierbar ist (psd2_enabled).

- **SEPA-Flag:** Kennzeichnet, ob SEPA-Lastschriften oder Überweisungen verfügbar sind (sepa_direct_debit_enabled).

- **UI-Platzhalter:** In der Kontoeinstellung sichtbare, aber deaktivierte Checkboxen mit Hinweistext &bdquo;Verfügbar in Phase 2&ldquo;.

- **Vorbereitung für OAuth2-Authentifizierung:** Technische Basis für spätere PSD2-APIs mit sicheren Tokens und Consent-Verwaltung.

- **Migration Ready:** Strukturierte Schema-Vorbereitung für den künftigen Wechsel von Datei-Import (WEG-82) zu Live-Banking.

## Geschäftsregeln & Logik
- Beide Flags werden beim Anlegen eines neuen Bankkontos standardmäßig auf *false* gesetzt.

- Es existiert keine aktive Logik im MVP; die Felder dienen ausschließlich der Vorbereitung.

- In späteren Phasen wird eine PSD2-API-Integration mit OAuth2-Authentifizierung implementiert.

- SEPA-Funktionen (Einzüge, Überweisungen) werden nur aktiv, wenn das Flag auf *true* steht.

- Änderungen an den Flags dürfen nur durch Systemmigration oder Administratoren erfolgen.

## Akzeptanzkriterien
- **Gegeben** ein Verwalter legt ein neues Bankkonto an &rarr; **Wenn** das Formular für Bankkontoeinstellungen geöffnet wird &rarr; **Dann** sind die Optionen &bdquo;PSD2-Integration aktivieren&ldquo; und &bdquo;SEPA-Lastschrift aktivieren&ldquo; sichtbar, jedoch deaktiviert und mit Hinweistext versehen.

- **Gegeben** ein Administrator öffnet die Datenbankstruktur &rarr; **Wenn** das Bankkonto-Schema angezeigt wird &rarr; **Dann** enthält es die Felder psd2_enabled und sepa_direct_debit_enabled, beide mit Standardwert *false*.

- **Gegeben** ein Benutzer versucht, die Checkboxen manuell zu aktivieren &rarr; **Wenn** das System sich im MVP-Modus befindet &rarr; **Dann** wird die Aktion verhindert und ein Hinweis angezeigt.

## Nicht-Ziele
- Keine aktive PSD2- oder SEPA-Funktion im MVP.

- Keine API-Kommunikation mit Banken oder Drittanbietern.

- Keine OAuth2-Authentifizierung oder Token-Handling.

## Kritische Fälle
- **Fehlerhafte Migration:** Flags müssen in zukünftigen Versionen konsistent migriert werden, um Integrität zu gewährleisten.

- **Unklare UI-Darstellung:** Fehlende Hinweise könnten zu Missverständnissen führen; deutliche Beschriftung erforderlich.

## Abhängigkeiten
- WEG-8 – Finance & Banking – Übergeordnetes Modul für Finanzprozesse.

- WEG-80 – Finance Master Data – Verwaltung der Bankkonten.

- WEG-82 – Banking Inbound – Zukünftige Ablösung durch PSD2-basierte Transaktionsimporte.

- WEG-24 – Audit Log – Nachverfolgung zukünftiger Aktivierungen und Änderungen.

## Offene Fragen
- Welche PSD2-API-Provider sollen unterstützt werden (z. B. FinAPI, Tink, Plaid)?

- Soll die OAuth2-Authentifizierung direkt im System oder über externe Services laufen?

- Wird eine manuelle Freigabe für SEPA-Lastschriften vorgesehen oder erfolgt diese vollautomatisch?

- Wie soll das Consent-Management umgesetzt werden (z. B. Erneuerung alle 90 Tage)?

## Zukunftserweiterungen
- Integration einer PSD2-API zur automatischen Transaktionssynchronisation.

- Aktivierung von SEPA-Lastschriften für Hausgeld-Einzüge.

- Unterstützung von Echtzeit-Überweisungen (Instant SEPA).

- Multi-Banking-Support mit zentraler Kontoübersicht.

- Automatisches Consent-Management für PSD2-Authentifizierungen.

## Verknüpfte Tasks
- [WEG-890 – Flags & Stubs for Future Sync](https://maierharry.atlassian.net/browse/WEG-890) – Implementierung der Datenbankfelder (psd2_enabled, sepa_direct_debit_enabled) und deaktivierter UI-Elemente.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Platzhalter-Flags (Datenbankfelder und UI-Stubs) ohne aktive Funktionalität.

**Phase 2**

PSD2-API-Integration, SEPA-Lastschrift-Prozesse, OAuth2-Authentifizierung.

**Phase 3**

Echtzeit-Zahlungen (Instant SEPA), Multi-Banking-Support, automatisches Consent-Management.