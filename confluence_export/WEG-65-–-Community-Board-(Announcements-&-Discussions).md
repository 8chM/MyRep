---
title: WEG-65 – Community Board (Announcements & Discussions)
confluence_id: 28082977
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/28082977/WEG-65+Community+Board+Announcements+Discussions
---

**JIRA-Link:** [WEG-65 – Community Board (Announcements & Discussions)](https://maierharry.atlassian.net/browse/WEG-65)

## Überblick
Das Modul Community Board (WEG-65) erweitert das Kommunikationssystem des WEG Management Systems um eine zentrale Plattform für gemeinschaftliche Diskussionen, Ankündigungen und den strukturierten Informationsaustausch zwischen Verwaltung, Beirat und Eigentümern. Ziel ist es, den internen Austausch zu fördern, Transparenz zu schaffen und den Einsatz externer Kommunikationskanäle (z. B. E-Mail oder WhatsApp) zu vermeiden. Das Board fungiert als digitales, revisionssicheres &bdquo;schwarzes Brett&ldquo; für Themen, Anfragen und Mitteilungen innerhalb einer Eigentümergemeinschaft.

## Beschreibung
WEG-65 integriert sich nahtlos in das Messaging- und Notification-System (WEG-6) und bietet einen kontrollierten, rollenbasierten Kommunikationsraum. Beiträge und Kommentare werden auditierbar gespeichert und können Benachrichtigungen im gesamten System auslösen. Die Oberfläche ist thematisch gegliedert und erlaubt eine gezielte Moderation durch Administratoren oder Beiräte.

Hauptfunktionen:

- **Board & Kategorien:** Strukturierung in Themenbereiche wie *Allgemeines*, *Wartung*, *Finanzen* oder *Versammlungen*, individuell pro WEG konfigurierbar.

- **Beiträge & Kommentare:** Erstellen, Kommentieren und Antworten durch berechtigte Nutzer (Verwaltung, Beirat, Eigentümer).

- **Anhänge & Medien:** Upload und Verwaltung von Dateien (z. B. PDFs, Bilder, Protokolle) mit sicherem, versioniertem Handling über WEG-5.

- **Moderation & Reporting:** Beiräte oder Administratoren können Beiträge prüfen, freigeben, sperren oder archivieren; missbräuchliche Inhalte können gemeldet werden.

- **Benachrichtigungen:** Automatische Alerts über neue Beiträge, Kommentare oder Moderationsaktionen via Notification Center (WEG-6).

- **Suche & Filter:** Volltextsuche über Titel, Inhalte und Kategorien; Sortierung nach Aktivität oder Aktualität.

- **RBAC-Integration:** Rollenbasierte Sichtbarkeit (z. B. Finanzthemen nur für Verwaltung/Beirat).

- **Archiv & Retention:** DSGVO-konforme Aufbewahrung, automatische Archivierung nach Ablauf definierter Fristen.

- **Audit-Integration:** Alle Aktionen (Erstellung, Änderung, Löschung) werden im Audit-Log (WEG-24) protokolliert.

## Geschäftsregeln & Logik
- Nur berechtigte Benutzer dürfen neue Themen oder Kommentare erstellen.

- Jeder Beitrag muss einer Kategorie zugeordnet werden.

- Änderungen erzeugen neue Versionen; keine stillen Edits.

- Jeder Beitrag gehört ausschließlich zu einer WEG (keine Cross-Tenant-Kommunikation).

- Archivierte Beiträge sind schreibgeschützt und können nur durch Administratoren wiederhergestellt werden.

- Benachrichtigungen werden asynchron verarbeitet, um Systemlast zu vermeiden.

## Akzeptanzkriterien
- **Gegeben** ein Benutzer mit Schreibrecht öffnet das Board &rarr; **Wenn** ein neuer Beitrag erstellt wird &rarr; **Dann** wird dieser korrekt einer Kategorie zugeordnet, gespeichert und für berechtigte Nutzer sichtbar.

- **Gegeben** ein Beitrag enthält einen Anhang &rarr; **Wenn** der Upload abgeschlossen ist &rarr; **Dann** wird die Datei sicher gespeichert, versioniert und mit dem Beitrag verknüpft.

- **Gegeben** ein Beitrag wird gemeldet &rarr; **Wenn** ein Moderator ihn prüft &rarr; **Dann** kann er gesperrt, kommentiert oder gelöscht werden, wobei ein Audit-Eintrag erstellt wird.

- **Gegeben** ein neuer Kommentar wird veröffentlicht &rarr; **Wenn** der Beitrag beobachtet wird &rarr; **Dann** erhalten der Ersteller und Abonnenten eine Benachrichtigung im Notification Center.

- **Gegeben** die Aufbewahrungsfrist eines Beitrags ist erreicht &rarr; **Wenn** der Retention-Job ausgeführt wird &rarr; **Dann** wird der Beitrag archiviert und im Audit-Protokoll vermerkt.

## Nicht-Ziele
- Keine öffentliche Kommunikation außerhalb des Systems.

- Keine Echtzeit-Chat-Funktion (siehe WEG-61).

- Kein anonymer Modus im MVP; alle Beiträge sind personalisiert.

- Keine automatische Übersetzung (i18n folgt Systemstandard).

## Kritische Fälle
- **Fehlerhafte Moderation:** Gelöschte Beiträge müssen über Audit-Versionen wiederherstellbar sein.

- **Benachrichtigungsverzögerungen:** Hohe Systemlast darf keine Verzögerungen verursachen.

- **Fehlende Rollenvalidierung:** Falsch gesetzte RBAC-Rechte könnten unbefugten Zugriff erlauben.

- **Spam oder Missbrauch:** Wiederholte Meldungen führen zur automatischen Sperrung betroffener Beiträge.

## Abhängigkeiten
- WEG-6 – In-App Messaging & Notifications – Benachrichtigungssystem für neue Beiträge und Kommentare.

- WEG-21 – RBAC Roles & Policies – Zugriffsbeschränkungen auf Basis von Rollen und Kategorien.

- WEG-5 – Document Management – Speicherung und Versionierung von Anhängen.

- WEG-24 – Audit Log – Nachvollziehbarkeit aller Änderungen und Aktionen.

- WEG-26 – Data Privacy & Redaction – Anwendung von Retention- und Redaktionsregeln.

## Offene Fragen
- Soll das Board zukünftig E-Mail- oder Push-Benachrichtigungen unterstützen?

- Wie lange sollen archivierte Beiträge aufbewahrt werden (Standard 2 Jahre)?

- Soll eine interne Kategorie für Verwaltung/Beirat vorgesehen werden?

- Wird eine Reaktions- oder Voting-Funktion im MVP benötigt?

## Zukunftserweiterungen
- **Reaktions- & Voting-Funktion:** Möglichkeit, Beiträge mit &bdquo;Likes&ldquo; oder Reaktionen zu versehen.

- **AI-gestützte Zusammenfassung:** Automatische Erstellung von Themenzusammenfassungen.

- **Mobile Push-Benachrichtigungen:** Integration in mobile Geräte.

- **Dashboard-Integration:** Anzeige aktueller Beiträge im Systemdashboard.

- **Exportfunktionen:** PDF-/ZIP-Export für Jahresberichte oder Protokolle.

## Verknüpfte Tasks
- [WEG-650 – Board & Categories](https://maierharry.atlassian.net/browse/WEG-650) – Aufbau der Boardstruktur und Kategorisierung.

- [WEG-651 – Posts, Comments, Attachments](https://maierharry.atlassian.net/browse/WEG-651) – Beitragserstellung, Kommentierung und Dateiverwaltung.

- [WEG-652 – Moderation & Reporting](https://maierharry.atlassian.net/browse/WEG-652) – Verwaltung gemeldeter Beiträge und Sperrlogik.

- [WEG-653 – Board Notifications (use WEG-6)](https://maierharry.atlassian.net/browse/WEG-653) – Integration der Benachrichtigungen ins Notification Center.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Basis-Board mit Kategorien, Beiträgen, Kommentaren, Anhängen, Rollenrechten, Benachrichtigungen und Audit-Protokoll.

**Phase 2**

Moderations-Dashboard, Spam-Filter, Voting-Funktion, erweiterte Filter & Suche, Retention-Automatisierung.

**Phase 3**

AI-Analyse, Echtzeit-Benachrichtigungen, Mobile App-Integration, Exportfunktionen und Dashboard-Widgets.