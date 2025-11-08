---
title: WEG-60 – Notification Center (List, Badges, Bulk)
confluence_id: 27591429
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27591429/WEG-60+Notification+Center+List+Badges+Bulk
---

**JIRA-Link:** [WEG-60 – Notification Center (List, Badges, Bulk)](https://maierharry.atlassian.net/browse/WEG-60)

## Überblick

Das Modul **Notification Center** (WEG-60) ist das zentrale Dashboard für alle Systembenachrichtigungen im WEG Management System. Es bietet eine strukturierte Übersicht über Ereignisse, Statusänderungen und Systemmeldungen, mit Unterstützung für Filter, Massenaktionen und Priorisierung nach Dringlichkeit. Ziel ist es, allen Benutzern eine einheitliche, übersichtliche und nachvollziehbare Darstellung relevanter Systemereignisse bereitzustellen.

## Beschreibung

Das Notification Center sammelt, verwaltet und visualisiert alle Benachrichtigungen aus den verbundenen Modulen (z. B. Finanzen, Meetings, DMS). Benachrichtigungen werden zentral gespeichert, priorisiert und können individuell bearbeitet oder archiviert werden. Das System unterscheidet zwischen Informationsmeldungen, Warnungen und kritischen Ereignissen und aktualisiert Badge-Zähler in Echtzeit.

**Hauptfunktionen:**

- **Zentrale Sammlung:** Aggregation aller Systembenachrichtigungen aus Modulen wie WEG-6, WEG-8, WEG-9 oder WEG-87.

- **Statusverwaltung:** Benutzer können Benachrichtigungen als gelesen markieren, löschen oder archivieren.

- **Badge-Zähler:** Dynamische Anzeige ungelesener Meldungen nach Kategorien (Info, Warnung, Kritisch).

- **Filter & Massenaktionen:** Sortierung und Gruppenbearbeitung nach Quelle, Typ oder Dringlichkeit.

- **Scheduler-Integration:** Periodische Bereinigung abgelaufener Notifications über den Scheduler aus WEG-12.

- **Metadatenverwaltung:** Speicherung von Quelle, Zielrolle, Zeitstempel, Kategorie, Priorität und Status je Notification.

- **Retention & Privacy:** Umsetzung von Aufbewahrungsregeln (WEG-54) und DSGVO-Vorgaben (WEG-26).

- **Auditierung:** Alle Änderungen (Lesen, Löschen, Archivieren) werden revisionssicher im Audit-Log (WEG-24) dokumentiert.

## Geschäftsregeln & Logik

- **Ereignis-Korrelation:** Jede Benachrichtigung entsteht aus einem Ereignis, das durch das Event-Mapping (WEG-64) ausgelöst wird.

- **Priorisierung:** Kritische Meldungen erscheinen priorisiert und können Eskalationen auslösen.

- **Statuswechsel:** Änderungen des Lesestatus wirken sich unmittelbar auf Badge-Zähler und Filteransichten aus.

- **Archivierung:** Archivierte Benachrichtigungen bleiben einsehbar, zählen aber nicht mehr zu aktiven Benachrichtigungen.

- **Retention:** Nach Ablauf definierter Fristen werden Notifications automatisch gelöscht oder pseudonymisiert.

- **Sicherheitsprinzip:** Nur autorisierte Benutzer sehen Benachrichtigungen, die ihrer Rolle oder zugeordneten WEG entsprechen.

## Akzeptanzkriterien

- **Gegeben** ein Ereignis wird durch ein anderes Modul ausgelöst &rarr; **Wenn** eine Mapping-Regel vorhanden ist &rarr; **Dann** erzeugt das System automatisch eine Notification im Notification Center.

- **Gegeben** ein Benutzer hat ungelesene Benachrichtigungen &rarr; **Wenn** er eine Nachricht öffnet &rarr; **Dann** reduziert sich der Badge-Zähler entsprechend.

- **Gegeben** mehrere Notifications werden ausgewählt &rarr; **Wenn** eine Massenaktion (z. B. &bdquo;Alle als gelesen markieren&ldquo;) ausgeführt wird &rarr; **Dann** werden alle betroffenen Benachrichtigungen aktualisiert und protokolliert.

- **Gegeben** eine Notification erreicht das Ende ihrer Retention-Periode &rarr; **Wenn** der Scheduler-Job läuft &rarr; **Dann** wird die Benachrichtigung automatisch gelöscht oder archiviert.

- **Gegeben** eine Notification wird gelöscht &rarr; **Wenn** sie aus dem aktiven Pool entfernt wird &rarr; **Dann** bleibt der Löschvorgang im Audit-Log nachvollziehbar.

## Nicht-Ziele

- Kein Export der Benachrichtigungen an externe Messenger oder E-Mail-Systeme im MVP.

- Keine Sound-, Push- oder Desktop-Notifications in der ersten Version.

- Keine benutzerspezifischen Layouts oder Themes im MVP.

## Kritische Fälle

- **Massenbenachrichtigungen:** Hohe Ereignisdichte kann die Performance beeinträchtigen; Paging und Lazy Loading sind erforderlich.

- **Fehlendes Event-Mapping:** Ereignisse ohne definierte Zuordnung dürfen keine Fehler auslösen, sondern werden im Audit-Log vermerkt.

- **Fehlerhafte Scheduler-Ausführung:** Benachrichtigungen dürfen nicht versehentlich gelöscht werden; Logs müssen Wiederherstellbarkeit ermöglichen.

## Abhängigkeiten

-  – Definiert, welche Ereignisse Benachrichtigungen auslösen.

-  – Steuert die automatische Bereinigung und Badge-Aktualisierung.

-  – Dokumentiert Änderungen an Notifications.

-  – Stellt DSGVO-konforme Redaktions- und Löschprozesse sicher.

-  – Definiert Aufbewahrungs- und Löschrichtlinien für Benachrichtigungen.

## Offene Fragen

- Soll das Notification Center eine Volltextsuche nach Inhalten und Kategorien unterstützen?

- Wie sollen Mehrfachbenachrichtigungen (Aggregation) gehandhabt werden, wenn ein Ereignis mehrfach auftritt?

- Wird eine visuelle Gruppierung nach Quelle (z. B. Modul oder Typ) gewünscht?

## Zukunftserweiterungen

- **Push-Notifications:** Erweiterung auf mobile Geräte und Browser-Benachrichtigungen.

- **Eskalationslogik:** Automatische Weiterleitung kritischer Ereignisse an übergeordnete Rollen.

- **Benutzerdefinierte Filter & Dashboards:** Individuelle Ansichten und gespeicherte Filter.

- **Integrationen:** Optionale Synchronisation mit externen Kommunikationssystemen.

## Verknüpfte Tasks

- [WEG-600 – Notification List/Badges/Bulk](https://maierharry.atlassian.net/browse/WEG-600) – Implementiert Listenansicht, Statussteuerung und Massenaktionen für Notifications.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Zentrales Notification Center mit Badge-Zähler, Lesestatus, Massenaktionen und Retention-Steuerung.

**Phase 2**

Einführung von Push-Notifications, Eskalationslogik und erweiterten Filteroptionen.

**Phase 3**

Benutzerdefinierte Ansichten, Synchronisation mit externen Kommunikationssystemen und KI-gestützte Ereignisaggregation.