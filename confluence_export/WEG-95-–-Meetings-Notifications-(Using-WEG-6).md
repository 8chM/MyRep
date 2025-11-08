---
title: WEG-95 – Meetings Notifications (Using WEG-6)
confluence_id: 27722384
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722384/WEG-95+Meetings+Notifications+Using+WEG-6
---

**JIRA-Link:** [WEG-95 – Meetings Notifications (Using WEG-6)](https://maierharry.atlassian.net/browse/WEG-95)

## Überblick
Das Modul **Meetings Notifications **(WEG-95) sorgt für die zuverlässige Kommunikation aller relevanten Meeting-Ereignisse innerhalb des WEG-Systems. Es integriert sich direkt in das zentrale Benachrichtigungssystem (WEG-6) und informiert Teilnehmer, Bevollmächtigte und betroffene Benutzer über Einladungen, Erinnerungen, Abstimmungsergebnisse und Protokollfreigaben. Das Ziel ist es, sicherzustellen, dass alle Beteiligten stets aktuell über Terminänderungen und Ergebnisse informiert sind, ohne auf externe Kommunikationskanäle angewiesen zu sein.

## Beschreibung
WEG-95 ist das Benachrichtigungs-Subsystem der Meeting-Module (WEG-90 bis WEG-94). Bei jedem relevanten Ereignis (z. B. Erstellung einer Einladung, Statusänderung, Abstimmungsabschluss oder Veröffentlichung des Protokolls) werden automatisch Benachrichtigungen an betroffene Nutzer ausgelöst. Diese Benachrichtigungen werden über die zentrale Infrastruktur von **WEG-6 (In-App Messaging & Notifications)** verteilt und berücksichtigen individuelle Benutzerpräferenzen (z. B. In-App oder E-Mail). Das Modul arbeitet vollständig mandantenfähig und nutzt den Audit-Log (WEG-24), um jeden Versandvorgang zu protokollieren.

Hauptfunktionen:

- **Automatische Einladungen:** Generiert Benachrichtigungen für alle berechtigten Teilnehmer bei Terminplanung oder -änderung.

- **Erinnerungs-Mechanismus:** Sendet Erinnerungen 24 Stunden vor Beginn des Meetings (konfigurierbar).

- **Statusänderungs-Tracking:** Informiert alle Teilnehmer bei Übergängen zwischen Meeting-Phasen (z. B. Scheduled &rarr; Conducted &rarr; Closed).

- **Abstimmungsergebnisse:** Übermittelt automatisch die finalen Ergebnisse an alle Teilnehmer nach Abschluss der Abstimmung.

- **Protokollfreigabe:** Versendet Benachrichtigungen, sobald ein Protokoll (WEG-94) finalisiert und freigegeben wurde.

- **Benutzerpräferenzen:** Nutzer können auswählen, welche Benachrichtigungen sie erhalten möchten (z. B. nur In-App oder zusätzlich E-Mail).

- **Retry-Mechanismus:** Falls ein Versand fehlschlägt (z. B. E-Mail), wird automatisch ein Wiederholungsversuch gestartet.

## Geschäftsregeln & Logik
- Alle Benachrichtigungen werden im Notification Center (WEG-6) zentral erfasst und gespeichert.

- Jeder Meeting-Statuswechsel löst definierte Benachrichtigungstypen aus (z. B. Einladung, Erinnerung, Abschluss).

- Benachrichtigungen dürfen nur an berechtigte Rollen (Teilnehmer, Beirat, Verwaltung) gesendet werden.

- Fehlgeschlagene E-Mail-Benachrichtigungen erzeugen keine Datenverluste – sie werden als In-App-Nachricht nachgehalten.

- Wiederholte Benachrichtigungen (z. B. bei mehrfacher Statusänderung) werden zusammengefasst, um Spam zu vermeiden.

## Akzeptanzkriterien
- **Gegeben** ein Meeting wird auf *Scheduled* gesetzt &rarr; **Wenn** Einladungen erzeugt werden &rarr; **Dann** erhalten alle berechtigten Teilnehmer automatisch eine In-App- und (optional) eine E-Mail-Benachrichtigung.

- **Gegeben** ein Meeting findet in 24 Stunden statt &rarr; **Wenn** die Erinnerungsfunktion aktiviert ist &rarr; **Dann** erhalten alle Teilnehmer eine automatische Erinnerung.

- **Gegeben** eine Abstimmung wird abgeschlossen &rarr; **Wenn** das Ergebnis feststeht &rarr; **Dann** erhalten alle Teilnehmer eine Benachrichtigung mit dem Abstimmungsergebnis.

- **Gegeben** das Protokoll wurde finalisiert &rarr; **Wenn** es im DMS veröffentlicht wird &rarr; **Dann** wird automatisch eine Benachrichtigung an alle Teilnehmer gesendet.

- **Gegeben** der Versand einer Benachrichtigung schlägt fehl &rarr; **Wenn** der Retry-Mechanismus aktiv ist &rarr; **Dann** erfolgt ein erneuter Zustellversuch innerhalb von 15 Minuten.

## Nicht-Ziele
- Keine SMS- oder Push-Benachrichtigungen im MVP.

- Keine individuellen Benachrichtigungszeitpunkte (nur feste Intervalle, z. B. 24 Stunden vor Meeting).

- Kein Rückkanal für Antworten oder Feedback auf Benachrichtigungen.

## Kritische Fälle
- **E-Mail-Versandfehler:** Wenn der Versand scheitert, wird automatisch eine In-App-Benachrichtigung generiert.

- **Benachrichtigungsüberflutung:** Bei mehr als 50 offenen Benachrichtigungen werden ältere Einträge gruppiert.

- **Mehrfache Statusänderung:** Das System verhindert redundante Benachrichtigungen bei kurzzeitigen Statuswechseln.

## Abhängigkeiten
- WEG-6 – In-App Messaging & Notifications – Zentrale Infrastruktur für den Versand von Nachrichten.

- WEG-2 – Identity & Access – Verwaltung von Benutzerpräferenzen und Rollenrechten.

- WEG-24 – Audit Log – Nachvollziehbarkeit von Versandvorgängen.

- WEG-94 – Meeting Minutes & Resolution Archive – Quelle für Protokollfreigabe-Events.

## Offene Fragen
- Sollen Meeting-Benachrichtigungen zukünftig auch über SMS oder Push-Nachrichten unterstützt werden?

- Welche Standard-Erinnerungsintervalle sollen konfigurierbar sein (1h, 12h, 24h)?

- Soll eine Priorisierung von Benachrichtigungstypen eingeführt werden (z. B. &bdquo;kritisch&ldquo; vs. &bdquo;informativ&ldquo;)?

## Zukunftserweiterungen
- **SMS- und Push-Benachrichtigungen:** Erweiterung um mobile Kanäle (Phase 2+).

- **Kalenderintegration:** Automatische Synchronisation mit Outlook oder Google Calendar.

- **Erweiterte Benutzerpräferenzen:** Individuelle Erinnerungseinstellungen und Benachrichtigungsfilter.

- **Analytics-Modul:** Statistische Auswertung über Zustellquoten und Nutzerinteraktion.

## Verknüpfte Tasks
- [WEG-950 – Notification Integration (WEG-6)](https://maierharry.atlassian.net/browse/WEG-950) – Integration des zentralen Benachrichtigungssystems in das Meeting-Modul.

- [WEG-951 – Einladungs-Benachrichtigungen](https://maierharry.atlassian.net/browse/WEG-951) – Automatische Versandlogik für Einladungstermine.

- [WEG-952 – Erinnerungs-Benachrichtigungen (24h vor Meeting)](https://maierharry.atlassian.net/browse/WEG-952) – Regelbasierte Erinnerung für alle Teilnehmer.

- [WEG-953 – Abstimmungsergebnis-Benachrichtigungen](https://maierharry.atlassian.net/browse/WEG-953) – Ergebnisübermittlung nach Abstimmungsende.

- [WEG-954 – Protokollfreigabe-Benachrichtigungen](https://maierharry.atlassian.net/browse/WEG-954) – Versand bei Veröffentlichung von Meeting-Protokollen.

- [WEG-955 – Benutzerpräferenzen für Benachrichtigungen](https://maierharry.atlassian.net/browse/WEG-955) – Verwaltung individueller Kommunikationsoptionen.

- [WEG-956 – E-Mail-Vorlagen & Versandlogik](https://maierharry.atlassian.net/browse/WEG-956) – Einheitliche E-Mail-Templates und Fehlerbehandlung.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Integration mit WEG-6, automatische Einladungen, Erinnerungen (24h), Abstimmungsergebnis- und Protokollbenachrichtigungen, Benutzerpräferenzen, Audit-Logging.

**Phase 2**

Einführung von SMS-/Push-Benachrichtigungen, Kalenderintegration, flexible Erinnerungsintervalle, erweiterte Präferenzsteuerung.

**Phase 3**

Analytics-Dashboard, intelligente Benachrichtigungspriorisierung, KI-gestützte Zustelloptimierung.