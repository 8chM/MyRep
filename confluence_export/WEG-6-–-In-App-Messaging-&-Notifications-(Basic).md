---
title: WEG-6 – In-App Messaging & Notifications (Basic)
confluence_id: 27853492
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27853492/WEG-6+In-App+Messaging+Notifications+Basic
---

**JIRA-Link:** [WEG-6 – In-App Messaging & Notifications (Basic)](https://maierharry.atlassian.net/browse/WEG-6)

## Beschreibung / Kernzweck

Das Modul **WEG-6 – In-App Messaging & Notifications** ist die zentrale Kommunikations- und Informationsplattform des WEG Management Systems (WMS). Es verbindet alle Benutzergruppen – Verwalter, Beirat, Eigentümer, Bewohner und Dienstleister – über eine einheitliche Oberfläche, in der Benachrichtigungen, Mitteilungen und Ankündigungen kontextbezogen, nachvollziehbar und sicher bereitgestellt werden.

Jedes relevante Ereignis im System, wie etwa eine neue Abrechnung, eine bevorstehende Versammlung, der Ablauf einer Vertragsfrist oder ein veröffentlichtes Dokument, kann automatisch eine Benachrichtigung erzeugen oder eine direkte Nachricht an bestimmte Rollen und Gruppen senden.

Ziel ist es, die Kommunikation vollständig innerhalb des Systems abzubilden und redundante E-Mail-Kommunikation zu vermeiden. Das Modul fungiert als Kommunikations-Backbone für alle fachlichen Prozesse und stellt sicher, dass jede relevante Aktion im System nachvollziehbar kommuniziert wird.

## Inhalte

**Untermodul**

**Kurzbeschreibung**

[WEG-60 – Notification Center (List, Badges, Bulk)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Zentrales Benachrichtigungs-Dashboard mit Filter- und Priorisierungsfunktionen, Lesestatus und Massenaktionen.

[WEG-61 – Messaging Threads & Attachments](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Internes Nachrichtensystem mit strukturierter Thread-Logik, DMS-Verknüpfung (WEG-5), Anhängen und Lesebestätigungen.

[WEG-62 – Message Encryption at Rest (Configurable)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Verschlüsselung aller gespeicherten Nachrichteninhalte und Anhänge pro Mandant; Schlüsselverwaltung über internes Vault-System.

[WEG-63 – Messaging Search / Filter / Batch](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Volltextsuche und Filterung nach Typ, Empfänger und Status; Massenaktionen für Threads.

[WEG-64 – Event &rarr; Notification Mapping](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Regelbasiertes Mapping von Systemereignissen (z. B. Vertragsänderung, neues Dokument) in Benachrichtigungen.

[WEG-65 – Community Board (Announcements & Discussions)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Digitales schwarzes Brett für Ankündigungen, Diskussionen und Aushänge mit Moderations- und Archivierungsfunktionen.

## Geschäftslogik

- **Rollenbasierte Zustellung:** Nachrichten und Benachrichtigungen werden nur an Benutzer gesendet, deren Rolle und Kontext (WEG, Einheit, Gebäude) zutreffen. Die Berechtigungen werden aus WEG-21 (RBAC) übernommen.

- **Ereignisbasierte Kommunikation:** Alle Systemereignisse (z. B. DMS-Upload, Vertragsablauf, Ticketänderung, Beschlussfreigabe) können über das Event-Mapping (WEG-64) automatisch Benachrichtigungen auslösen.

- **Thread-Organisation:** Nachrichten werden in thematischen Threads geführt, die bestimmten Entitäten (WEG, Gebäude, Eigentümer, Ticket, Vertrag) zugeordnet sind.

- **Priorisierung:** Benachrichtigungen werden nach Wichtigkeit sortiert (hoch, mittel, niedrig) und über Scheduler (WEG-12) eskaliert, falls unbeantwortet.

- **Auditierbarkeit:** Jede Aktion – Erstellen, Lesen, Löschen, Archivieren – wird über WEG-24 (Audit Log) revisionssicher protokolliert.

- **Datenschutz und Retention:** Nachrichten und Anhänge unterliegen den Datenschutz- und Archivierungsrichtlinien aus WEG-26 (Privacy) und WEG-54 (Retention).

- **Sicherheit:** Nachrichteninhalte und Anhänge werden verschlüsselt gespeichert (WEG-62) und sind ausschließlich für berechtigte Benutzer lesbar.

- **Scheduler-Integration:** Erinnerungen und wiederkehrende Systembenachrichtigungen werden automatisch durch den Scheduler (WEG-12) erstellt.

## Akzeptanzkriterien

- **Gegeben** ein Systemereignis (z. B. neuer Vertrag) &rarr; **Wenn** es im Event-Mapping konfiguriert ist &rarr; **Dann** wird automatisch eine Benachrichtigung im Notification Center erzeugt.  

- **Gegeben** ein Benutzer erhält eine neue Nachricht &rarr; **Wenn** er eingeloggt ist &rarr; **Dann** erscheint ein Hinweis im Notification Center und der Thread wird als ungelesen markiert.  

- **Gegeben** eine Vertragskündigung erreicht ihr Enddatum &rarr; **Wenn** der Scheduler läuft &rarr; **Dann** wird eine Fristen-Erinnerung an Verwalter und Beirat versendet.  

- **Gegeben** eine Ankündigung im Community Board &rarr; **Wenn** sie von einem Moderator freigegeben wird &rarr; **Dann** ist sie für alle berechtigten Benutzer sichtbar.  

- **Gegeben** ein Benutzer verliert seine Berechtigung &rarr; **Wenn** seine Rolle geändert wird &rarr; **Dann** verliert er automatisch den Zugriff auf vertrauliche Konversationen.

## Nicht-Ziele

- Keine Integration in externe Messenger oder E-Mail-Systeme im MVP.

- Kein Echtzeit-Chat über WebSockets oder Push-Notifications.

- Keine automatischen Übersetzungen von Nachrichten in andere Sprachen.

- Kein Workflow-Editor für Kommunikationsabläufe im MVP.

## Kritische Fälle

- **Scheduler-Verzögerungen:** Erinnerungen dürfen bei Verzögerungen nicht verloren gehen.

- **Verwaiste Threads:** Beim Entfernen eines Teilnehmers bleiben Threads erhalten, aber personenbezogene Daten werden anonymisiert.

- **Rollenwechsel:** Der Benutzer verliert bei Rollenänderung sofort den Zugriff auf nicht mehr erlaubte Threads.

- **DMS-Ausfall:** Bei Ausfall des DMS (WEG-5) bleiben Nachrichtentexte erhalten, Anhänge werden nachträglich synchronisiert.

## Abhängigkeiten

- WEG-5 – Document Management (Basic) & Templates (Foundation): Speicherung und Verknüpfung von Anhängen.

- WEG-12 – Error Handling, Logging & Health: Scheduler und Logging-Infrastruktur für Erinnerungen.

- WEG-21 – RBAC Roles & Policies per Association: Steuerung der Nachrichten- und Benachrichtigungsrechte.

- WEG-24 – Audit Log (User/Roles/Settings): Revisionssichere Dokumentation aller Kommunikationsvorgänge.

- WEG-26 – Data Privacy & Redaction (GDPR Base): Verwaltung von Lösch- und Anonymisierungsprozessen.

- WEG-54 – Retention & Archive (Locked Periods): Definition von Aufbewahrungsfristen für Nachrichten.

- WEG-57 – Contract Management (Vendors, Maintenance, Insurance): Vertragsereignisse erzeugen Benachrichtigungen.

## Offene Fragen

- Soll das Notification Center konfigurierbare Filter und Benutzerpräferenzen unterstützen?

- Wann soll die Mobile-Push-Integration (Android/iOS) erfolgen und mit welchem Authentifizierungsverfahren?

- Soll das Event-Mapping (WEG-64) über eine Administratoroberfläche konfigurierbar sein?

- Sollen Board-Beiträge (WEG-65) automatisch nach Ablauf archiviert oder gelöscht werden?

## Zukunftserweiterungen

- **Mobile Push-Notifications:** Versand an mobile Geräte über native Apps.

- **KI-gestützte Priorisierung:** Automatische Gewichtung und Zusammenfassung wichtiger Nachrichten.

- **Kalenderintegration:** Export relevanter Ereignisse (Meetings, Fristen) als ICS-Dateien.

- **Smart Summary:** KI-basierte Zusammenfassung längerer Diskussionsverläufe.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Notification Center, Messaging (Threads & Attachments), Community Board, Event&rarr;Notification-Mapping, rollenbasierte Zustellung.

**Phase 2**

Echtzeit-Chat, Mobile Push-Notifications, Mentions & Reactions, konfigurierbares Notification-Mapping.

**Phase 3**

KI-gestützte Priorisierung, Smart Summaries, Kalenderintegration und mehrsprachige Messaging-Unterstützung.