---
title: WEG-61 – Messaging Threads & Attachments
confluence_id: 27329343
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329343/WEG-61+Messaging+Threads+Attachments
---

**JIRA-Link:** [WEG-61 – Messaging Threads & Attachments](https://maierharry.atlassian.net/browse/WEG-61)

## Überblick

Das Modul **Messaging Threads & Attachments** (WEG-61) stellt das interne Kommunikationssystem des WEG Management Systems bereit. Es ermöglicht strukturierte Nachrichtenverläufe (Threads) zwischen Benutzern, inklusive sicherer Dateiverknüpfungen über das Dokumentenmanagementsystem (WEG-5). Ziel ist eine sichere, nachvollziehbare und rollenbasierte interne Kommunikation innerhalb der Verwaltung und Eigentümergemeinschaften.

## Beschreibung

WEG-61 erweitert das interne Messaging-System (WEG-6) um Thread-basierte Konversationen mit Anhängen, Statusverwaltung und Audit-Funktionalität. Es dient als zentrale Kommunikationsschnittstelle zwischen Eigentümern, Beiräten und Verwaltern, wobei alle Nachrichten nachvollziehbar und datenschutzkonform gespeichert werden.

**Hauptfunktionen:**

- **Thread-Struktur:** Jede Nachricht ist Teil eines Threads, der Teilnehmer, Verlauf und Anhänge zusammenfasst.

- **DMS-Integration:** Anhänge werden im Dokumentenmanagement (WEG-5) gespeichert; das Messaging-Modul hält nur Metadaten (Absender, Empfänger, Zeitstempel, Status).

- **Gruppen- & Direktnachrichten:** Unterstützung sowohl für Gruppenkommunikation (z. B. Beirat) als auch für direkte 1:1-Chats.

- **Lesebestätigungen:** Nachrichtenstatus (sent, read, archived) wird pro Empfänger aktualisiert.

- **Soft-Delete:** Nachrichten können gelöscht werden, bleiben aber im Audit-Log (WEG-24) nachvollziehbar.

- **Anhangsverwaltung:** Alle Dateiverknüpfungen erfolgen ausschließlich über DMS-Referenzen.

- **Archivierung & Retention:** Alte Threads können archiviert oder nach Ablauf der Aufbewahrungsfrist (WEG-54) automatisch pseudonymisiert werden.

## Geschäftsregeln & Logik

- **Thread-Kontext:** Jeder Thread ist eindeutig einer Einheit, einem Ticket oder einem Modulkontext (z. B. Vertrag, Meeting) zugeordnet.

- **Zugriffssteuerung:** Nachrichten sind nur für autorisierte Teilnehmer sichtbar (RBAC, WEG-21).

- **Statusmodell:** Nachrichten durchlaufen die Stati gesendet, gelesen, archiviert. Archivierte Threads sind weiterhin im Audit-Log abrufbar.

- **DMS-Kopplung:** Anhänge werden nicht dupliziert, sondern als Referenz gespeichert; die Berechtigung folgt den DMS-Regeln.

- **Auditierung:** Jede Aktion (Erstellen, Lesen, Archivieren, Löschen) wird im Audit-Log dokumentiert.

- **Retention & Privacy:** Nachrichten unterliegen den Datenschutzrichtlinien (WEG-26) und Retention-Policies (WEG-54).

## Akzeptanzkriterien

- **Gegeben** ein Benutzer sendet eine Nachricht in einem Thread &rarr; **Wenn** der Thread Teilnehmer hat &rarr; **Dann** wird die Nachricht gespeichert und alle Empfänger erhalten eine Notification im Notification Center.

- **Gegeben** eine Datei wird als Anhang hochgeladen &rarr; **Wenn** die Nachricht gesendet wird &rarr; **Dann** wird der Anhang im DMS gespeichert und mit dem Thread verknüpft.

- **Gegeben** ein Benutzer öffnet einen Thread &rarr; **Wenn** alle enthaltenen Nachrichten gelesen werden &rarr; **Dann** wird der Thread als gelesen markiert und der Badge-Zähler reduziert.

- **Gegeben** ein Benutzer löscht eine Nachricht &rarr; **Wenn** der Soft-Delete ausgeführt wird &rarr; **Dann** bleibt die Nachricht im Audit-Log erhalten, ist aber für Benutzer nicht sichtbar.

- **Gegeben** eine Nachricht überschreitet die Aufbewahrungsfrist &rarr; **Wenn** der Retention-Job (WEG-54) läuft &rarr; **Dann** wird die Nachricht automatisch archiviert oder pseudonymisiert.

## Nicht-Ziele

- Keine Audio-, Video- oder Bildschirmübertragungen im Messaging-Modul.

- Keine Echtzeit-Ende-zu-Ende-Verschlüsselung (nur Verschlüsselung im Ruhezustand über WEG-62).

- Keine Integration mit externen Chat- oder E-Mail-Systemen im MVP.

## Kritische Fälle

- **Fehlende DMS-Referenzen:** Bei Speicherfehlern im DMS wird die Nachricht markiert, aber nicht gelöscht.

- **Thread-Kollisionen:** Gleichzeitige Bearbeitung (z. B. paralleles Archivieren) darf keine Inkonsistenzen erzeugen.

- **Fehlerhafte Statusaktualisierung:** Muss bei Netzwerkfehlern über Retry-Mechanismen korrigiert werden.

## Abhängigkeiten

-  – Erstellt Benachrichtigungen bei neuen Nachrichten oder Änderungen.

-  – Verwaltung und Speicherung der Anhänge.

-  – Verschlüsselt gespeicherte Nachrichten und Anhänge.

-  – Steuerung der Zugriffsrechte.

-  – Dokumentiert alle Kommunikationsereignisse.

-  – Legt Aufbewahrungs- und Archivierungsregeln fest.

-  – Sicherstellung DSGVO-konformer Speicherung.

## Offene Fragen

- Soll eine Thread-Suche über Volltextindizierung (z. B. Elastic) bereits im MVP enthalten sein?

- Sollen gelöschte Benutzer im Verlauf pseudonymisiert oder ausgeblendet werden?

- Wie lange sollen archivierte Threads im System verbleiben (Retention-Periode)?

## Zukunftserweiterungen

- **Mentions & Tagging:** Benutzer können andere Teilnehmer direkt ansprechen.

- **Reaktionen & Emojis:** Erweiterte Interaktion zwischen Teilnehmern.

- **Thread-Export:** Export kompletter Kommunikationsverläufe als ZIP oder PDF.

- **Offline-Funktion:** Caching von Nachrichten für mobile Clients.

## Verknüpfte Tasks

- [WEG-610 – Threads, Replies & Attachments](https://maierharry.atlassian.net/browse/WEG-610) – Implementiert die Thread-Struktur, Antwortlogik und Anhangsverknüpfungen.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Thread-basierte Nachrichten mit DMS-Integration, Lesestatus, Soft-Delete, RBAC-Absicherung und Notification-Verknüpfung.

**Phase 2**

Einführung von Mentions, Reaktionen, erweiterten Suchfunktionen und Offline-Synchronisierung.

**Phase 3**

Exportfunktionen, Integration externer Kommunikationssysteme und KI-gestützte Thread-Analyse.