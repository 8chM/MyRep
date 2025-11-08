---
title: WEG-91 – Agenda, Participants & Proxies (Skeleton)
confluence_id: 27722369
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722369/WEG-91+Agenda+Participants+Proxies+Skeleton
---

**JIRA-Link:** [WEG-91 – Agenda, Participants & Proxies (Skeleton)](https://maierharry.atlassian.net/browse/WEG-91)

## Überblick
Das Modul **Agenda, Participants & Proxies **(WEG-91) verwaltet die Tagesordnung (TOPs), Teilnehmer und Vollmachten für Eigentümerversammlungen. Es stellt sicher, dass Agenden versioniert, Teilnehmer korrekt zugeordnet und Proxies (Stimmrechtsübertragungen) rechtssicher erfasst werden. Ziel ist es, den gesamten organisatorischen Vorlauf einer Versammlung digital und nachvollziehbar abzubilden – von der Agendaerstellung bis zur Teilnahmeprüfung vor Sitzungsbeginn.

## Beschreibung
WEG-91 erweitert das Meeting-Grundmodell (WEG-90) um die operative Verwaltung der Tagesordnung, Teilnehmer und Vollmachten. Jede Agenda wird versioniert, sobald sie nach dem Versand einer Einladung geändert wird. Diese Versionen werden im DMS (WEG-5) archiviert und sind revisionssicher nachvollziehbar. Teilnehmer (Eigentümer, Beiräte, Gäste) werden automatisch aus der Stammdatenverwaltung (WEG-4) geladen und mit ihrem Stimmgewicht verknüpft. Vollmachten (Proxies) sind personenbezogen, gelten nur für ein bestimmtes Meeting und verlieren nach dessen Abschluss automatisch ihre Gültigkeit.

Hauptfunktionen:

- **Agenda-Verwaltung:** Erfassung, Strukturierung und Begründung von Tagesordnungspunkten inklusive Referenzdokumenten.

- **Agenda-Versionierung:** Jede Änderung nach Versand der Einladungen erzeugt automatisch eine neue Version mit Änderungsprotokoll.

- **Teilnehmer-Management:** Verwaltung von Eigentümern, Beiräten und Gästen mit Rollenzuordnung und Stimmgewicht.

- **Proxy-Handling:** Erfassung und Validierung von Vollmachten zwischen Eigentümern, inklusive automatischem Ablauf nach dem Meeting.

- **Quoren-Prüfung:** Automatische Berechnung, ob das erforderliche Teilnahmequorum (nach MEA oder Anzahl) erreicht wird.

- **Einladungs-Trigger:** Generierung und Versand von Einladungshinweisen über das Notification-System (WEG-6) mit Ablage im DMS.

## Geschäftsregeln & Logik
- Änderungen an einer bereits versandten Agenda erzeugen automatisch eine neue Version; alte Versionen bleiben sichtbar.

- Proxies dürfen nur zwischen aktiven Eigentümern derselben WEG erteilt werden.

- Eine Vollmacht verliert mit Ende des Meetings automatisch ihre Gültigkeit.

- Das System prüft vor Sitzungsbeginn automatisch, ob das Teilnahmequorum erfüllt ist.

- Teilnehmerdaten werden ausschließlich aus dem Modul WEG-4 geladen und sind nicht manuell überschreibbar.

## Akzeptanzkriterien
- **Gegeben** eine finale Agenda ist erstellt &rarr; **Wenn** Einladungen generiert werden &rarr; **Dann** erhalten alle relevanten Rollen eine Benachrichtigung (WEG-6), und die Agenda wird im DMS (WEG-5) archiviert.

- **Gegeben** ein Proxy wird eingereicht &rarr; **Wenn** die Validierung erfolgreich ist &rarr; **Dann** wird das Stimmrecht automatisch übertragen und beim Quorum berücksichtigt.

- **Gegeben** ein Meeting startet &rarr; **Wenn** das Quorum nicht erreicht ist &rarr; **Dann** zeigt das System eine Warnung an und verhindert die Aktivierung des Status *Conducted*.

- **Gegeben** eine Agenda wird nach Versand der Einladung geändert &rarr; **Wenn** der Benutzer speichert &rarr; **Dann** wird automatisch eine neue Version erzeugt und im Audit-Log (WEG-24) dokumentiert.

## Nicht-Ziele
- Kein E-Mail-Versand im MVP (Benachrichtigungen ausschließlich innerhalb der Anwendung).

- Keine automatisierte Proxy-Validierung über QR-Codes oder Signaturen.

- Keine Agenda-Vorschläge durch Eigentümer im MVP.

## Kritische Fälle
- **Rollenkonflikt:** Wenn ein Beiratsmitglied versucht, eine Vollmacht für einen anderen Eigentümer zu übernehmen, wird der Vorgang abgelehnt.

- **Ungültige Teilnehmerdaten:** Wenn ein Eigentümer nicht mehr aktiv ist, darf er weder teilnehmen noch eine Vollmacht erteilen.

- **Agenda-Kollision:** Änderungen an bereits freigegebenen TOPs erfordern eine neue Version, um Revisionssicherheit zu gewährleisten.

## Abhängigkeiten
- WEG-90 – Meetings Domain Model – Grundlegende Architektur und Statuslogik.

- WEG-4 – Property & People – Quelle der Eigentümer- und Beiratsdaten.

- WEG-5 – Document Management – Ablage von Agenden und Einladungen.

- WEG-6 – Notifications – Versand von Einladungshinweisen und Systemmeldungen.

- WEG-24 – Audit Log – Protokollierung aller Änderungen an Agenda und Proxies.

## Offene Fragen
- Sollen Eigentümer in einer späteren Phase eigene TOP-Vorschläge einreichen können (z. B. bis x Tage vor Versammlung)?

- Soll die Proxy-Erteilung künftig digital signiert werden (z. B. via QR-Code oder eSign)?

- Wie granular soll die Quoren-Prüfung konfigurierbar sein (nach MEA, Anzahl, oder Eigentümergruppen)?

## Zukunftserweiterungen
- **QR-Proxies:** Digitale, signierte Vollmachten mit automatischer Validierung und ICS-Kalendereinladung.

- **Eigentümer-TOP-Vorschläge:** Eigentümer können neue Tagesordnungspunkte digital einreichen.

- **Erweiterte Quoren-Logik:** Automatische Neuberechnung und Benachrichtigung bei Änderungen der Teilnehmerliste.

## Verknüpfte Tasks
- [WEG-910 – Agenda & Participants Skeleton](https://maierharry.atlassian.net/browse/WEG-910) – Implementierung der Agenda-Verwaltung mit Versionierung und Teilnehmerhandling.

- [WEG-911 – Proxies & Validations Skeleton](https://maierharry.atlassian.net/browse/WEG-911) – Verwaltung und Validierung von Vollmachten inklusive Ablaufmechanismus.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Grundfunktionen für Agenda-Versionierung, Teilnehmer- und Proxy-Verwaltung, Quoren-Prüfung, DMS- und Notification-Integration.

**Phase 2**

QR-Proxies, Eigentümer-TOP-Vorschläge, ICS-Kalenderintegration.

**Phase 3**

Automatische Quoren-Checks, digitale Signaturen und erweiterte Validierungslogik.