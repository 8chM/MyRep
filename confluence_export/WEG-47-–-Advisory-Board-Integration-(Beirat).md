---
title: WEG-47 – Advisory Board Integration (Beirat)
confluence_id: 27656652
version: 12
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27656652/WEG-47+Advisory+Board+Integration+Beirat
---

**JIRA-Link:** [WEG-47 – Advisory Board Integration (Beirat)](https://maierharry.atlassian.net/browse/WEG-47)

## Überblick

Das Modul **Advisory Board Integration (Beirat)** (WEG-47) bildet die organisatorische Struktur des Beirats einer Eigentümergemeinschaft digital ab und integriert dessen Aktivitäten in die operativen und administrativen Prozesse des WEG Management Systems.

Es ermöglicht die Verwaltung von Mitgliedern, Amtszeiten, Rollen (z. B. Vorsitzende:r, Stellvertreter:in, Mitglied) und Zuständigkeiten.

Ziel ist es, Beiratsentscheidungen, Freigaben und Genehmigungsprozesse rechtssicher, nachvollziehbar und effizient in das Gesamtsystem einzubetten.

Das Modul schafft Transparenz über Mandate, Rollen und Entscheidungsverläufe, während Benachrichtigungen, Erinnerungen und Audit-Logs sicherstellen, dass keine Amtszeiten unbeachtet auslaufen und jede Entscheidung dokumentiert bleibt.

## Beschreibung

WEG-47 unterstützt die Verwaltung des Beirats auf organisatorischer und prozessualer Ebene.

Jedes Mitglied besitzt eine definierte Rolle, ein Start- und Enddatum der Amtszeit und optionale Zuständigkeitsbereiche (z. B. Finanzen, Bauwesen, Kommunikation).

Die Systemlogik stellt sicher, dass ausschließlich Eigentümer:innen Mitglied werden können und Amtszeiten sich nicht überschneiden.

Ein integrierter Scheduler erinnert Verwalter:innen automatisch 30 Tage vor Ablauf einer Amtszeit und erstellt Aufgaben oder Benachrichtigungen (über WEG-6 – Messaging & Notifications).

Beiratsentscheidungen können mit Finanzprozessen (WEG-8) und Eigentümerversammlungen (WEG-9) verknüpft werden, sodass Genehmigungen, Freigaben oder Budgetentscheidungen unmittelbar im System abgebildet werden.

Alle Änderungen, Ernennungen, Verlängerungen oder Abberufungen werden revisionssicher im Audit-Log (WEG-24) dokumentiert.

Hauptfunktionen:

- **Mitgliederverwaltung:** Erfassung von Beiratsmitgliedern mit Rollen, Amtszeiten, Zuständigkeiten und Historie.

- **Rollen- und Berechtigungssteuerung:** Definition spezifischer Rechte, z. B. Einsicht in Finanzberichte oder Beschlussvorlagen.

- **Amtszeitüberwachung:** Automatische Erinnerungen vor Ablauf; keine Überschneidung von Amtsperioden.

- **Audit-Logging:** Jede Ernennung, Verlängerung oder Beendigung wird mit Zeitstempel und Begründung protokolliert.

- **Verknüpfung mit Prozessen:** Integration in Beschlusswesen (WEG-9) und Finanzfreigaben (WEG-8).

- **Benachrichtigungssystem:** Erinnerungen und Eskalationen bei unbesetzten Positionen oder auslaufenden Mandaten.

## Geschäftsregeln & Logik

- Nur aktive Eigentümer:innen können Beiratsmitglieder sein.

- Amtszeiten dürfen sich nicht überschneiden; das System verhindert doppelte Einträge.

- Ernennungen und Abberufungen sind revisionssicher zu dokumentieren.

- Rollen bestimmen den Zugriff auf Daten, Dokumente und Entscheidungsprozesse.

- Das System erinnert Verwalter:innen 30 Tage vor Ablauf eines Mandats.

- Beiratsentscheidungen können Finanz- oder Beschlussprozesse freigeben, sind jedoch nicht automatisch bindend (MVP).

## Akzeptanzkriterien

- **Gegeben** ein Eigentümer soll als Beiratsmitglied ernannt werden &rarr; **Wenn** dieser mit Rolle und Amtszeit eingetragen wird &rarr; **Dann** wird ein Audit-Eintrag erzeugt und der Scheduler plant eine Erinnerungsbenachrichtigung.

- **Gegeben** eine Amtszeit endet in 30 Tagen &rarr; **Wenn** das Datum erreicht wird &rarr; **Dann** erhält der Verwalter automatisch eine Benachrichtigung über den Ablauf.

- **Gegeben** ein neues Mitglied wird ernannt &rarr; **Wenn** es bereits eine überlappende Amtszeit gibt &rarr; **Dann** blockiert das System den Vorgang und zeigt eine Fehlermeldung an.

- **Gegeben** eine Beiratsentscheidung betrifft einen Finanzvorgang &rarr; **Wenn** die Entscheidung protokolliert wird &rarr; **Dann** wird der Vorgang im Audit-Log festgehalten und an das Finanzmodul (WEG-8) weitergeleitet.

- **Gegeben** ein Mitglied wird abberufen &rarr; **Wenn** die Änderung bestätigt wird &rarr; **Dann** wird das Mandat beendet, alle Benachrichtigungen storniert und die Änderung protokolliert.

## Nicht-Ziele

- Keine digitale Abstimmung oder elektronische Signatur im MVP.

- Keine automatisierte Genehmigung oder Ablehnung von Beschlüssen.

- Keine Verwaltung externer Beiräte oder Externe ohne Eigentümerrolle.

## Kritische Fälle

- **Überlappende Amtszeiten:** System darf keine Überschneidungen zulassen.

- **Nicht-Eigentümer:innen:** Ernennung wird blockiert und als Fehler protokolliert.

- **Abgelaufene Amtszeiten:** Bei fehlender Nachfolge wird eine Eskalationsbenachrichtigung generiert.

- **Fehlende Audit-Daten:** Unvollständige Protokolle führen zu Audit-Warnungen.

## Abhängigkeiten

-  – Versand von Erinnerungen und Eskalationen.

-  – Integration in Freigabeprozesse für Budgets oder Zahlungen.

-  – Verknüpfung von Beiratsentscheidungen mit Beschlüssen.

-  – Planung und Überwachung von Benachrichtigungsjobs.

-  – Nachvollziehbarkeit aller Änderungen.

-  – Zugriffsschutz und Datenschutz der Beiratsdaten.

## Offene Fragen

- Sollen Beiratsfreigaben für Finanzprozesse optional konfigurierbar sein?

- Soll eine digitale Unterschrift (z. B. eIDAS-konform) in Phase 2 integriert werden?

- Wie detailliert sollen Zuständigkeitsbereiche (z. B. Finanzen, Technik) gepflegt werden?

## Zukunftserweiterungen

- **Digitale Freigaben:** Online-Genehmigung von Budgets, Verträgen und Beschlüssen.

- **Erweiterte Berichte:** Dashboard zur Beiratsaktivität und Anwesenheit.

- **Elektronische Signaturen:** Vollständige Integration in Entscheidungs-Workflows.

- **Statistische Auswertungen:** Visualisierung von Amtsperioden und Freigabehistorien.

## Verknüpfte Tasks

- [WEG-470 – Advisory Board Domain Model](https://maierharry.atlassian.net/browse/WEG-470) – Modellierung der Beiratsentitäten.

- [WEG-471 – Member Assignment & Terms](https://maierharry.atlassian.net/browse/WEG-471) – Verwaltung von Mitgliedern, Amtszeiten und Rollen.

- [WEG-472 – Permission Mapping (RBAC)](https://maierharry.atlassian.net/browse/WEG-472) – Definition rollenspezifischer Berechtigungen.

- [WEG-473 – Meeting Participation Linking](https://maierharry.atlassian.net/browse/WEG-473) – Verknüpfung der Beiratsmitglieder mit Eigentümerversammlungen.

- [WEG-474 – Approval Workflows (basic)](https://maierharry.atlassian.net/browse/WEG-474) – Implementierung einfacher Genehmigungsabläufe.

- [WEG-475 – Notifications & Escalations](https://maierharry.atlassian.net/browse/WEG-475) – Erinnerungs- und Eskalationsmechanismen.

- [WEG-476 – Visibility Rules](https://maierharry.atlassian.net/browse/WEG-476) – Festlegung der Sichtbarkeitsregeln für Beiratsdaten.

- [WEG-477 – Directory & Reporting](https://maierharry.atlassian.net/browse/WEG-477) – Erzeugung von Berichten und Übersichten über Beiratsstrukturen.

- [WEG-478 – Audit Integration](https://maierharry.atlassian.net/browse/WEG-478) – Protokollierung aller Änderungen.

- [WEG-479 – Import/Export](https://maierharry.atlassian.net/browse/WEG-479) – Import und Export von Beiratsdaten.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Verwaltung der Beiratsmitglieder mit Rollen, Amtszeiten und Zuständigkeiten; Erinnerungsmechanismus, Audit-Integration, Verknüpfung zu Meetings und Finanzen.

**Phase 2**

Digitale Beschlussfassung, Freigabe-Workflows und Dashboard-Erweiterungen.

**Phase 3**

Vollständige Integration elektronischer Signaturen, Berichtsautomatisierung und erweiterte Statistiken.