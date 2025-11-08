---
title: WEG-17 – Configuration & Feature Flags (Base)
confluence_id: 27591390
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27591390/WEG-17+Configuration+Feature+Flags+Base
---

**JIRA-Link:** [WEG-17 – Configuration & Feature Flags (Base)](https://maierharry.atlassian.net/browse/WEG-17)

## Überblick
Das Modul **Configuration & Feature Flags (Base)** (WEG-17) bildet das Fundament für zentrale Konfigurationsverwaltung und kontrollierte Funktionsfreigaben im gesamten WEG Management System.

Es definiert ein einheitliches Schema für Konfigurationsparameter über das **Options-Pattern** und ermöglicht über **Feature-Flags** die gezielte Aktivierung oder Deaktivierung von Systemfunktionen.

Ziel ist eine sichere, nachvollziehbare und konsistente Steuerung von Konfigurationswerten und Features – sowohl global als auch mandantenspezifisch.

## Beschreibung
WEG-17 stellt die technische Grundlage für Konfigurationsmanagement und Feature-Steuerung bereit.

Alle Systemkomponenten lesen ihre Einstellungen aus zentral definierten Optionsklassen, die beim Start validiert werden. Ungültige Werte führen zu einem **Fail-Fast-Abbruch**, um inkonsistente Zustände zu verhindern.

Darüber hinaus ermöglicht das Modul die Definition und Verwaltung von **Feature-Flags**, die als Schalter für bestimmte Funktionsbereiche dienen.

Diese Flags können statisch über Umgebungsvariablen, Konfigurationsdateien oder – in späteren Phasen – dynamisch über eine Admin-Oberfläche gesetzt werden.

Hauptfunktionen:

- **Zentrale Konfiguration:** Einheitliche Definition aller Parameter über das Options-Pattern mit Validierungsattributen.

- **Fail-Fast-Startup:** Das System startet nur, wenn alle Konfigurationswerte gültig sind.

- **Feature-Flags:** Steuerung von Features über deklarative Schalter (z. B. EnableBilling, EnableMessaging, EnableArchive).

- **Admin-UI (Basis):** Einfache Übersicht aller Feature-Flags mit Aktivierungsstatus (nur für Administratoren).

- **Versionierte Flags:** Dokumentation der Default-Werte, Änderungen und Auswirkungen in der Systemdokumentation.

- **Mandantenspezifische Steuerung:** Integrierbar mit dem Tenant-Modul (WEG-3), um Features pro Association zu aktivieren.

## Geschäftsregeln & Logik
- Konfigurationsdateien sind verpflichtend und werden beim Start geprüft; fehlende oder ungültige Werte führen zu einem sofortigen Abbruch.

- Feature-Flags gelten standardmäßig global, können aber pro WEG (Tenant) überschrieben werden.

- Änderungen an Feature-Flags sind auditierbar und dürfen nur von Administratoren vorgenommen werden.

- Flags, die sicherheitsrelevante Bereiche betreffen, dürfen nicht clientseitig gesteuert werden.

- Konfigurationsänderungen zur Laufzeit erfordern einen Neustart (keine dynamische Reload-Funktion im MVP).

- Feature-Flags werden konsistent zwischen Backend und Frontend synchronisiert, um UI-Fehler zu vermeiden.

## Akzeptanzkriterien
- **Gegeben** eine ungültige Konfiguration &rarr; **Wenn** die Anwendung startet &rarr; **Dann** wird ein Fehler geworfen und der Dienst startet nicht.

- **Gegeben** ein Feature-Flag ist deaktiviert &rarr; **Wenn** ein Benutzer auf das entsprechende Modul zugreift &rarr; **Dann** wird das Feature im Frontend ausgeblendet oder blockiert.

- **Gegeben** ein Feature-Flag ist global aktiviert &rarr; **Wenn** ein Tenant ohne Override auf das System zugreift &rarr; **Dann** steht das Feature allen Benutzern zur Verfügung.

- **Gegeben** ein Feature-Flag wird für eine Association deaktiviert &rarr; **Wenn** ein Benutzer dieser WEG das Feature aufruft &rarr; **Dann** erhält er eine standardisierte Fehlermeldung oder &bdquo;Feature deaktiviert&ldquo;-Hinweis.

- **Gegeben** eine CI-Pipeline prüft Konfigurationen &rarr; **Wenn** ein ungültiger Wert erkannt wird &rarr; **Dann** schlägt der Build fehl und der Fehler wird im Log ausgegeben.

## Nicht-Ziele
- Keine dynamische Laufzeitkonfiguration im MVP.

- Keine automatisierte Synchronisation externer Konfigurationsquellen (z. B. Consul, Vault).

- Keine individuellen Feature-Rollouts pro Benutzer im MVP.

- Keine Echtzeitumschaltung von Feature-Flags ohne Neustart.

## Kritische Fälle
- **Fehlende Konfigurationsdatei:** Anwendung darf nicht starten, sondern muss mit Fehler abbrechen.

- **Feature-Flag-Mismatch:** Unterschiedliche Zustände zwischen Backend und Frontend dürfen nicht vorkommen – Synchronisierung zwingend erforderlich.

- **Falsche Default-Werte:** Ein versehentlich aktiviertes Flag kann kritische Systembereiche öffnen.

- **Fehlerhafte Validierung:** Ungültige Werte dürfen nicht unbemerkt bleiben.

## Abhängigkeiten
- **WEG-10 – Solution Setup & Infrastructure:** Bereitstellung von Konfigurationsdateien und ENV-Variablen.

- **WEG-3 – Tenant Provisioning & Administration:** Verwaltung mandantenspezifischer Feature-Overrides.

- **WEG-12 – Error Handling, Logging & Health:** Logging von Konfigurations- und Flag-Fehlern.

- **WEG-14 – Testing & CI Basics:** Validierung der Konfiguration innerhalb der CI-Pipeline.

## Offene Fragen
- Soll die Feature-Flag-Verwaltung im MVP bereits über eine UI erfolgen oder nur über Konfigurationsdateien?

- Wie werden Flags zwischen Backend und Frontend konsistent synchronisiert?

- Sollen Flags in späteren Phasen versioniert und historisiert werden?

## Zukunftserweiterungen
- Dynamische Konfiguration über eine Admin-UI mit Live-Reload.

- **Remote Configuration Service** (z. B. per API oder Cloud Config Server).

- **A/B-Testing** und stufenweise Rollouts (per Benutzergruppe, WEG oder Region).

- Integration eines **Config-Dashboard** zur Übersicht aller aktiven Flags und Parameter.

## Verknüpfte Tasks
- **WEG-170 – Options Pattern Configuration** – Implementiert typsichere Konfiguration mit Validierung.

- **WEG-171 – Feature-Flag System** – Fügt die Feature-Steuerung für Backend und Frontend hinzu.

- **WEG-172 – Configuration Validation** – Validiert alle Konfigurationsparameter beim Start.

- **WEG-173 – Admin-UI for Feature-Flags (Optional)** – UI-Komponente zur manuellen Aktivierung von Features.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Einführung des Options-Pattern, Validierungslogik, globale Feature-Flags mit statischer Steuerung über ENV-Dateien, Fail-Fast-Startup.

**Phase 2**

Erweiterung um Remote-Konfiguration, mandantenspezifische Overrides, UI zur Flag-Verwaltung.

**Phase 3**

Echtzeit-Feature-Management mit Zielgruppensegmentierung, automatisierte Rollouts und A/B-Testing.