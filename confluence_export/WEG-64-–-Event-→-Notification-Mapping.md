---
title: WEG-64 – Event → Notification Mapping
confluence_id: 26968670
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/26968670/WEG-64+Event+Notification+Mapping
---

**JIRA-Link:** [WEG-64 – Event &rarr; Notification Mapping](https://maierharry.atlassian.net/browse/WEG-64)

## Überblick

Das Modul **Event &rarr; Notification Mapping** (WEG-64) bildet die Verbindung zwischen Systemereignissen und automatisch generierten Benachrichtigungen. Es steuert, welche Aktionen innerhalb des Systems (z. B. abgeschlossene Tickets, veröffentlichte Abrechnungen oder neue Dokumente) eine Benachrichtigung auslösen. Ziel ist es, eine konsistente, regelbasierte Ereignissteuerung zu ermöglichen, die Benachrichtigungen gezielt und rollenbasiert generiert.

## Beschreibung

WEG-64 ist die zentrale Steuerkomponente für das Event-Driven-Notification-System. Es definiert, welche Ereignisse in welchen Kontexten Benachrichtigungen erzeugen, und integriert dabei sowohl Systemereignisse als auch benutzerinitiierte Aktionen.

**Hauptfunktionen:**

- **Ereigniszuordnung:** Zuordnung von Ereignissen (z. B. "Dokument hochgeladen", "Beschluss veröffentlicht", "Ticket geschlossen") zu definierten Benachrichtigungstypen.

- **Regelbasierte Steuerung:** Ein konfigurierbares Regelwerk bestimmt, welche Zielgruppen (Rollen, Benutzer) Benachrichtigungen erhalten.

- **Mandantenspezifische Konfiguration:** Regeln können pro WEG individuell angepasst werden, um flexible und differenzierte Kommunikationsstrategien zu ermöglichen.

- **Scheduler-Integration:** Über den Scheduler (WEG-12) werden periodisch alle Ereignisse geprüft und ausstehende Benachrichtigungen generiert.

- **Auditierung:** Änderungen an Event-Regeln werden im Audit-Log (WEG-24) revisionssicher dokumentiert.

## Geschäftsregeln & Logik

- **Regelstruktur:** Jede Regel enthält Quelle (Event), Bedingung (Statusänderung, Zeitfenster), Zielrolle und Nachrichtentyp.

- **Aktivierung:** Regeln können aktiviert oder deaktiviert werden, ohne gelöscht zu werden.

- **Mandantentrennung:** Alle Regeln gelten ausschließlich innerhalb der jeweiligen WEG.

- **Scheduler-Prüfung:** Ereignisse werden in regelmäßigen Intervallen auf definierte Trigger geprüft.

- **Validierung:** Vor der Aktivierung werden Regeln auf syntaktische und semantische Korrektheit geprüft.

- **RBAC-Integration:** Nur berechtigte Rollen erhalten Benachrichtigungen, basierend auf den Richtlinien aus WEG-21.

## Akzeptanzkriterien

- **Gegeben** ein Ereignis tritt im System auf &rarr; **Wenn** eine passende Regel definiert ist &rarr; **Dann** wird automatisch eine Benachrichtigung gemäß der Regel erzeugt.

- **Gegeben** ein Administrator ändert eine bestehende Regel &rarr; **Wenn** die Änderung gespeichert wird &rarr; **Dann** wird sie im Audit-Log protokolliert und sofort wirksam.

- **Gegeben** ein Ereignis erfüllt mehrere Regeln &rarr; **Wenn** alle zutreffen &rarr; **Dann** werden alle relevanten Benachrichtigungen generiert, jeweils mit eigenem Empfängerkreis.

- **Gegeben** ein Scheduler-Zyklus läuft &rarr; **Wenn** ein Ereignis erkannt wird &rarr; **Dann** wird die zugehörige Benachrichtigung an das Notification Center (WEG-60) übermittelt.

- **Gegeben** eine Regel wird deaktiviert &rarr; **Wenn** das nächste Ereignis auftritt &rarr; **Dann** wird keine Benachrichtigung ausgelöst.

## Nicht-Ziele

- Keine komplexe Rule-Engine mit verschachtelten Bedingungen (z. B. mehrere UND/ODER-Logiken) im MVP.

- Keine UI für Echtzeit-Rule-Authoring (folgt erst in späteren Phasen).

- Keine dynamische Event-Priorisierung oder Zeitsteuerung im MVP.

## Kritische Fälle

- **Fehlerhafte Regelkonfiguration:** Kann zu ungewollten oder fehlenden Benachrichtigungen führen; Validierung notwendig.

- **Leistungsprobleme bei hoher Regelzahl:** Scheduler muss effizient mit Regelmengen skalieren.

- **Verwaiste Ereignisse:** Ereignisse ohne aktive Zuordnung dürfen nicht unbeabsichtigt Benachrichtigungen auslösen.

## Abhängigkeiten

-  – Scheduler zur periodischen Prüfung von Ereignissen.

-  – Steuerung, wer Benachrichtigungen erhalten darf.

-  – Protokollierung von Regeländerungen und Ausführungen.

-  – Darstellung der erzeugten Benachrichtigungen.

-  – Weiterleitung und Zustellung der Nachrichten.

## Offene Fragen

- Soll es eine grafische Administrationsoberfläche für Regeldefinitionen geben?

- Wie granular sollen die Bedingungen sein (z. B. Statuswechsel, Zeitfenster, Benutzeraktion)?

- Sollen Standardregeln beim Onboarding automatisch generiert werden?

## Zukunftserweiterungen

- **Komplexe Bedingungen:** Erweiterung der Regelengine um logische Operatoren (UND/ODER/NICHT).

- **UI-Editor:** Weboberfläche für Administratoren zur Erstellung und Verwaltung von Event-Regeln.

- **Zeitbasierte Trigger:** Regeln, die auf Ablaufzeiten oder Verzögerungen reagieren.

- **Vordefinierte Templates:** Standard-Regelsets für häufige Anwendungsfälle.

## Verknüpfte Tasks

- [WEG-640 – Event Mapping (DMS, Tickets, Meetings)](https://maierharry.atlassian.net/browse/WEG-640) – Implementiert die Zuordnung von Ereignissen aus DMS, Tickets und Meetings zu Benachrichtigungen.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Regelbasierte Ereignis-Zuordnung und automatische Benachrichtigungsgenerierung über Scheduler.

**Phase 2**

Einführung eines Admin-Interfaces, Validierungsmechanismen und Unterstützung komplexerer Regeln.

**Phase 3**

Temporäre und zeitgesteuerte Regeln, Vorlagen und KI-gestützte Ereigniserkennung.