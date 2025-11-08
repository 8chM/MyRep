---
title: WEG-33 – Association Admin Panel (Enable/Disable, Branding)
confluence_id: 28082932
version: 15
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/28082932/WEG-33+Association+Admin+Panel+Enable+Disable+Branding
---

**JIRA-Link:** [WEG-33 – Association Admin Panel (Enable/Disable, Branding)](https://maierharry.atlassian.net/browse/WEG-33)

## Überblick
Das Modul **Association Admin Panel** (WEG-33) stellt die zentrale Administrationsoberfläche für System- und WEG-Administratoren bereit.

Es dient der Verwaltung des Mandantenstatus (aktiv/deaktiviert), der individuellen Branding-Anpassung (z. B. Logo, Farben, Sprache) sowie der mandantenspezifischen Feature-Konfiguration.

Ziel ist es, eine zentrale, intuitive und revisionssichere Steuerung der Association bereitzustellen, ohne direkten Datenbankzugriff zu erfordern.

## Beschreibung
Das Admin Panel bündelt sämtliche Verwaltungsfunktionen, die auf Mandantenebene ausgeführt werden können.

Es erlaubt Administratoren, den technischen Zustand eines Mandanten zu steuern, Branding-Einstellungen vorzunehmen und Feature-Flags zu konfigurieren.

Hauptfunktionen:

- **Statusverwaltung: **Mandanten können aktiviert oder deaktiviert werden. Deaktivierte Mandanten besitzen weiterhin Lesezugriff, Schreiboperationen sind jedoch gesperrt. Der Statuswechsel wird protokolliert und wirkt sich systemweit auf alle Module aus.

- **Branding & Locale: **Anpassung von Logos, Farben und Sprachen (unterstützt durch WEG-15). Änderungen werden sofort aktiv und im Audit-Log (WEG-24) dokumentiert.

- **Feature-Flags: **Integration mit WEG-17 ermöglicht das Setzen und Entfernen mandantenspezifischer Funktionen, z. B. neue Finanz- oder Kommunikationsfeatures.

- **Administrations-Dashboard: **Übersicht über Status, Auslastung, letzte Provisionierung, Backups, Migrationen und aktive Nutzer. Dient als zentraler Einstiegspunkt für Administratoren.

## Geschäftsregeln & Logik
- Nur autorisierte Benutzer mit Rolle *SystemAdmin* oder *Manager* dürfen Status- oder Branding-Änderungen durchführen.

- Deaktivierte Mandanten dürfen keine schreibenden Aktionen mehr ausführen.

- Branding- und Locale-Änderungen gelten systemweit und werden unmittelbar nach Speicherung angewendet.

- Alle Änderungen am Mandantenstatus, Branding und Feature-Flags werden automatisch im Audit-Log (WEG-24) erfasst.

- Änderungen dürfen nicht parallel überschrieben werden – letzter gültiger Commit gewinnt.

## Akzeptanzkriterien
- **Gegeben** eine Association ist aktiv &rarr; **Wenn** sie im Admin Panel deaktiviert wird &rarr; **Dann** wird der Schreibzugriff gesperrt, der Lesezugriff bleibt erhalten, und der Status wird im UI angezeigt.

- **Gegeben** ein Administrator ändert das Logo oder die Farben &rarr; **Wenn** die Änderungen gespeichert werden &rarr; **Dann** werden sie unmittelbar systemweit übernommen und im Audit-Log dokumentiert.

- **Gegeben** ein Feature-Flag wird umgeschaltet &rarr; **Wenn** die Änderung bestätigt wird &rarr; **Dann** wird das Feature in der betroffenen Association sofort aktiviert bzw. deaktiviert.

- **Gegeben** eine Änderung des Status oder Brandings erfolgt &rarr; **Wenn** ein weiterer Administrator parallel speichert &rarr; **Dann** wird die zweite Änderung blockiert und ein Konflikt angezeigt.

- **Gegeben** das Dashboard wird geöffnet &rarr; **Wenn** der Administrator angemeldet ist &rarr; **Dann** sieht er eine Übersicht über alle relevanten Mandanteninformationen, einschließlich Status und Metriken.

## Nicht-Ziele
- Keine mandantenübergreifende Verwaltung im MVP; das Panel steuert ausschließlich eine einzelne Association.

- Kein automatisches Branding-Deployment über mehrere Mandanten hinweg.

- Keine tiefgreifende Performance- oder Auslastungsanalyse (nur Übersicht im MVP).

## Kritische Fälle
- **Fehlerhafte Deaktivierung:** Unbeabsichtigte Deaktivierung eines aktiven Mandanten darf nicht zu Datenverlust führen; Bestätigung mit Warnhinweis erforderlich.

- **Inkonsistenter Zustand:** Wenn ein Mandant im Directory deaktiviert, aber in der Anwendung aktiv ist, muss eine Synchronisation erzwungen werden.

- **Fehlerhafte Branding-Dateien:** Ungültige Dateiformate oder defekte Uploads dürfen nicht übernommen werden.

- **Feature-Flag-Konflikte:** Ungültige oder unvollständige Flags müssen automatisch abgelehnt werden.

## Abhängigkeiten
- WEG-17 – Configuration & Feature Flags (Base) – Verwaltung und Zuweisung von Feature-Flags.

- WEG-15 – Internationalization (EN/DE) Foundation – Steuerung der Sprach- und Lokalisierungseinstellungen.

- WEG-24 – Audit Log (User/Roles/Settings) – Erfassung aller Änderungen an Mandantenstatus, Branding und Features.

- WEG-13 – Control-Plane & Connection Routing – Verwaltung der Verbindungskonfiguration zwischen Directory und Mandanten-Schemas.

## Offene Fragen
- Soll das Panel mehrsprachig sein, um auch Administratoren anderer Sprachen zu unterstützen?

- Soll das Panel zusätzlich Mandanten-Metriken wie Speichernutzung, Benutzeraktivität oder API-Calls anzeigen?

- Soll ein Rückgängig-Button (&bdquo;Undo&ldquo;) für Branding-Änderungen verfügbar sein?

## Zukunftserweiterungen
- **Erweitertes Dashboard:** Anzeige von Echtzeitmetriken, Fehlerzuständen und Performance-Werten pro Mandant.

- **Temporäre Deaktivierung:** Einführung zeitgesteuerter Wartungsmodi mit automatischer Reaktivierung.

- **Multi-Tenant-Admin-Ansicht:** Übersicht und Steuerung aller Mandanten auf Systemebene.

- **Automatische E-Mail-Benachrichtigung:** Hinweis an Administratoren bei Status- oder Branding-Änderungen.

## Verknüpfte Tasks

- [WEG-330 – Enable/Disable, Branding, Locale](https://maierharry.atlassian.net/browse/WEG-330) – Implementiert die UI-Funktionen zur Aktivierung/Deaktivierung einer Association, Branding-Anpassung und Locale-Verwaltung.

- [WEG-331 – Feature Flag Integration](https://maierharry.atlassian.net/browse/WEG-331) – Bindet Feature-Flags aus WEG-17 in das Admin Panel ein.

- [WEG-332 – Dashboard Overview](https://maierharry.atlassian.net/browse/WEG-332) – Erstellt die Übersichtskomponenten (Status, Nutzer, Kapazität, letzte Aktionen).

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Aktivieren/Deaktivieren von Associations, Branding-Verwaltung (Logo, Farben, Sprache), Integration mit Feature-Flags, Audit-Logging.

**Phase 2**

Erweiterte Dashboards mit Metriken zu Nutzung, Fehlerzuständen und Last.

**Phase 3**

Temporäre Deaktivierungen (Wartungsfenster), Undo-Funktion, Multi-Tenant-Übersicht, automatisierte Benachrichtigungen.