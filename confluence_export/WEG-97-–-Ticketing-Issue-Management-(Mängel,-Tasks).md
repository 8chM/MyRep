---
title: WEG-97 – Ticketing / Issue Management (Mängel, Tasks)
confluence_id: 27198037
version: 10
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27198037/WEG-97+Ticketing+Issue+Management+M+ngel+Tasks
---

**JIRA-Link:** [WEG-97 – Ticketing / Issue Management (Mängel, Tasks)](https://maierharry.atlassian.net/browse/WEG-97)

## Überblick
Das Modul **Ticketing / Issue Management** (WEG-97) dient der strukturierten Erfassung, Bearbeitung und Nachverfolgung von Aufgaben, Mängeln und internen To-Dos innerhalb einer Eigentümergemeinschaft. Es bildet das zentrale Werkzeug für operatives Aufgaben- und Mängelmanagement und schafft Transparenz für Verwaltung, Beirat, Eigentümer und Dienstleister. Ziel ist eine revisionssichere und nachvollziehbare Bearbeitung sämtlicher Vorgänge – von der Meldung bis zur vollständigen Erledigung.

## Beschreibung
WEG-97 integriert ein vollwertiges Ticket-System in das WEG Management System. Tickets können aus verschiedenen Quellen entstehen: durch manuelle Erstellung, automatisch über andere Module (z. B. **WEG-9 Meetings** oder **WEG-6 Messaging**) oder durch Systemereignisse (z. B. Vertragsabläufe aus **WEG-57 Contract Management**). Jedes Ticket verfügt über eine eindeutige ID, Kategorie, Priorität, Status, Fälligkeit, Verantwortlichen und Historie.

Das Modul kombiniert technisches Aufgabenmanagement mit der fachlichen Nachvollziehbarkeit aller WEG-Prozesse. Alle Änderungen, Kommentare und Anhänge werden automatisch versioniert, und der gesamte Lebenszyklus eines Tickets ist über das Audit-Log (WEG-24) nachvollziehbar.

Hauptfunktionen:

- **Ticket-Lebenszyklus:** Vollständiger Workflow von Erstellung über Bearbeitung bis Abschluss, mit festen Statusübergängen (*Open &rarr; In Progress &rarr; Resolved &rarr; Closed*).

- **Kategorisierung & Priorisierung:** Strukturierung nach Typen (Mangel, Aufgabe, Anfrage, Beschlussumsetzung) und Dringlichkeit.

- **Objektverknüpfung:** Direkte Zuordnung zu Gebäuden, Einheiten oder einer gesamten WEG (Integration mit WEG-4).

- **Kommunikation:** Integration mit **WEG-6** für automatische Benachrichtigungen bei Statusänderungen, Kommentaren oder neuen Aufgaben.

- **Anhänge & Nachweise:** Upload und Verwaltung von Fotos, PDFs und Protokollen über das DMS (WEG-5).

- **Rollen & Zuständigkeiten:** Zuweisung von Tickets an Verwaltung, Beirat oder externe Dienstleister, inklusive zeitlich begrenzter Zugriffe.

- **SLA-Überwachung:** Automatische Kontrolle von Reaktions- und Bearbeitungszeiten, Eskalation bei Fristüberschreitungen.

- **Filter & Reporting:** Übersichtliche Dashboards für offene, geschlossene und überfällige Tickets.

- **Audit & Historie:** Jede Aktion (Statuswechsel, Kommentar, Änderung) wird im Audit-Log dokumentiert.

## Geschäftsregeln & Logik
- Jedes Ticket hat eine eindeutige ID und folgt klar definierten Statusübergängen.

- Eigentümer und Bewohner dürfen nur Tickets für eigene Einheiten anlegen oder einsehen.

- Beiräte sehen alle Tickets ihrer WEG, können aber keine fremden bearbeiten.

- Dienstleister erhalten nur Zugriff auf zugewiesene Tickets und für eine begrenzte Zeit.

- Tickets mit hoher Priorität erzeugen automatische Benachrichtigungen an die Verwaltung.

- Geschlossene Tickets sind schreibgeschützt; Änderungen erzeugen eine neue Revision.

- SLA-Fristen werden systemseitig überwacht, Verstöße werden automatisch eskaliert.

## Akzeptanzkriterien
- **Gegeben** ein Benutzer erstellt ein Ticket &rarr; **Wenn** Kategorie, Priorität und Objekt angegeben werden &rarr; **Dann** wird das Ticket gespeichert und im Dashboard angezeigt.

- **Gegeben** ein Ticket befindet sich in Bearbeitung &rarr; **Wenn** der Status auf &bdquo;Resolved&ldquo; geändert wird &rarr; **Dann** wird der Abschlusszeitpunkt protokolliert und das Ticket gesperrt.

- **Gegeben** ein Dienstleister erhält ein Ticket &rarr; **Wenn** die SLA-Zeit überschritten wird &rarr; **Dann** wird automatisch eine Eskalationsbenachrichtigung an die Verwaltung gesendet.

- **Gegeben** ein Eigentümer erstellt ein Ticket &rarr; **Wenn** die Verwaltung antwortet oder den Status ändert &rarr; **Dann** wird der Eigentümer über das Notification-System informiert.

- **Gegeben** ein Ticket wird geschlossen &rarr; **Wenn** eine Audit-Abfrage erfolgt &rarr; **Dann** sind alle Änderungen (Status, Kommentare, Zuweisungen) vollständig nachvollziehbar dokumentiert.

## Nicht-Ziele
- Keine Integration mit externen Helpdesk- oder Ticketsystemen im MVP.

- Kein automatischer Import aus E-Mails oder Telefonaten.

- Keine KI-basierte Kategorisierung oder Priorisierung.

- Kein frei konfigurierbarer Workflow-Designer (nur vordefinierte Status).

## Kritische Fälle
- **Fehlerhafte Zuordnung:** Ein Ticket wird der falschen Einheit oder WEG zugewiesen &rarr; Umverteilung durch Verwaltung erforderlich.

- **SLA-Verstoß:** Fristenüberwachung funktioniert nicht &rarr; Automatische Eskalation darf nicht ausbleiben.

- **Parallele Bearbeitung:** Mehrere Benutzer bearbeiten gleichzeitig &rarr; System priorisiert die zuletzt gespeicherte Änderung.

- **Unvollständiger Abschluss:** Ticket wird geschlossen, obwohl Unteraufgaben noch offen sind &rarr; Validierung erforderlich.

- **Fehlende Zuweisung:** Ticket ohne Bearbeiter &rarr; automatische Eskalation nach Ablauf der Reaktionszeit.

## Abhängigkeiten
- WEG-5 – Document Management – Speicherung und Versionierung von Ticket-Anhängen.

- WEG-6 – Messaging & Notifications – Kommunikation und Benachrichtigungen.

- WEG-9 – Meetings & Resolutions – Verknüpfung mit Beschlüssen und Protokollpunkten.

- WEG-24 – Audit Log – Revisionssichere Nachverfolgung aller Änderungen.

- WEG-4 – Property & People – Zuordnung zu Gebäuden, Einheiten und Eigentümern.

## Offene Fragen
- Soll das System eine Eskalationskette (z. B. 48 h &rarr; Beirat, 72 h &rarr; Verwaltung) unterstützen?

- Sollen Eigentümer Tickets selbst schließen dürfen oder nur kommentieren?

- Soll eine Integration zu externen Wartungsportalen (z. B. Handwerker-Systeme) vorgesehen werden?

- Wie granular sollen SLA-Zeiten definiert werden (global, pro Kategorie oder Tickettyp)?

- Soll es wiederkehrende Aufgaben (z. B. Wartungszyklen) geben?

## Zukunftserweiterungen
- **Mobile App-Integration:** Direkte Erstellung von Tickets mit Foto-Upload.

- **KI-gestützte Priorisierung:** Automatische Einschätzung der Dringlichkeit.

- **E-Mail- und Chat-Integration:** Automatische Ticket-Erstellung aus externen Nachrichten.

- **Wiederkehrende Aufgaben:** Automatische Generierung zyklischer Tickets (Wartung, Reinigung etc.).

- **Analyse-Dashboard:** KPI-Berichte (Bearbeitungszeiten, SLA-Erfüllung, offene Tickets pro WEG).

## Verknüpfte Tasks
- [WEG-970 – Ticket Lifecycle (Open &rarr; In Progress &rarr; Resolved &rarr; Closed)](https://maierharry.atlassian.net/browse/WEG-970) – Abbildung des vollständigen Workflows.

- [WEG-971 – Unit/Building Linking & Attachments](https://maierharry.atlassian.net/browse/WEG-971) – Verknüpfung von Tickets mit Objekten und Dokumenten.

- [WEG-972 – Assignment & SLA (basic)](https://maierharry.atlassian.net/browse/WEG-972) – Verwaltung von Zuständigkeiten und Fristen.

- [WEG-973 – Ticket &rarr; Meeting Agenda Link (optional)](https://maierharry.atlassian.net/browse/WEG-973) – Verbindung mit Tagesordnungspunkten aus Eigentümerversammlungen.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Ticket-Erstellung, Bearbeitung, Statusverfolgung, Benachrichtigungen, Anhänge, Audit-Logging.

**Phase 2**

SLA-Überwachung, Eskalationsketten, erweitertes Reporting, externe Wartungssystem-Integration.

**Phase 3**

Mobile-App-Integration, KI-Priorisierung, wiederkehrende Aufgaben, Analyse-Dashboard.