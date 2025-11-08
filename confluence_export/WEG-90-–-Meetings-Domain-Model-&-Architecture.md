---
title: WEG-90 – Meetings Domain Model & Architecture
confluence_id: 26968745
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/26968745/WEG-90+Meetings+Domain+Model+Architecture
---

**JIRA-Link:** [WEG-90 – Meetings Domain Model & Architecture](https://maierharry.atlassian.net/browse/WEG-90)

## Überblick
Das Modul **Meetings Domain Model & Architecture** (WEG-90) bildet die technische und fachliche Grundlage für alle Meeting- und Beschlussprozesse innerhalb des Systems. Es definiert das zentrale Datenmodell für Eigentümerversammlungen, Agenda-Punkte, Teilnehmer, Vollmachten und Beschlüsse. Darüber hinaus gewährleistet es die Nachvollziehbarkeit aller Statusänderungen, eine konsistente ID-Strategie und vollständige Auditierbarkeit über alle Sitzungsverläufe hinweg.

## Beschreibung
WEG-90 legt die Domänenarchitektur für Eigentümerversammlungen fest und sorgt für einheitliche Daten- und Prozessstrukturen in allen nachgelagerten Modulen (z. B. WEG-91 ff.). Jede Versammlung (Meeting) ist als eigenständiger, mandantenfähiger Datensatz mit klaren Statusübergängen modelliert – von der Planung über die Durchführung bis zum Abschluss (Closed / Archived). Das System stellt sicher, dass nach Abschluss keine Änderungen mehr möglich sind und alle Anpassungen nur über neue Revisionen erfolgen.

Hauptfunktionen:

- **Meetings-Datenmodell:** Abbildung aller zentralen Entitäten (Meeting, Agenda, Participant, Proxy, Resolution) mit klar definierten Relationen und Statuslogik.

- **Status- und Lebenszyklussteuerung:** Jeder Vorgang (Scheduled &rarr; Conducted &rarr; Closed &rarr; Archived) folgt einem festgelegten Ablauf.

- **Konsistenzprüfungen:** Validierung von Pflichtfeldern, MEA-Werten, Stimmengewichtung, Proxies und doppelten Einträgen.

- **Audit-Integration:** Jede CRUD-Operation oder Statusänderung wird automatisch im Audit-Log (WEG-24) protokolliert.

- **Unveränderlichkeit:** Nach dem Status *Closed* oder *Archived* sind Meetings schreibgeschützt; neue Änderungen erzeugen Revisionen.

- **Fehlerbehandlung:** Transaktionen werden bei Inkonsistenzen zurückgerollt und liefern ProblemDetails-Fehlermeldungen.

## Geschäftsregeln & Logik
- Meetings sind nur planbar, wenn alle Pflichtfelder (Titel, Datum, Typ) ausgefüllt sind und mindestens eine Agenda existiert.

- Nach Abschluss (*Closed*) ist ein Meeting unveränderlich; Änderungen erfordern eine neue Version.

- Alle Teilnehmer und Proxies müssen gültige Zuordnungen und MEA-Anteile besitzen.

- Jede Abstimmung muss eindeutig einer Resolution und einer Einheit zugeordnet sein.

- Jede Datenänderung wird über WEG-24 protokolliert und mit Benutzer, Zeitstempel und Status dokumentiert.

## Akzeptanzkriterien
- **Gegeben** ein neues Meeting wird erstellt &rarr; **Wenn** alle Pflichtfelder und mindestens eine Agenda enthalten sind &rarr; **Dann** kann das Meeting geplant (*Scheduled*) werden.

- **Gegeben** ein Meeting befindet sich im Status *Conducted* &rarr; **Wenn** alle Abstimmungen abgeschlossen sind &rarr; **Dann** kann es in den Status *Closed* überführt werden, und das System erzeugt automatisch einen Protokollentwurf.

- **Gegeben** ein Meeting ist im Status *Closed* &rarr; **Wenn** ein Benutzer versucht, Änderungen vorzunehmen &rarr; **Dann** verweigert das System den Zugriff und gibt eine Validierungswarnung aus.

- **Gegeben** ein Teilnehmer wird gelöscht &rarr; **Wenn** eine Abhängigkeit zu einer Abstimmung besteht &rarr; **Dann** wird die Transaktion zurückgerollt und eine ProblemDetails-Meldung ausgegeben.

## Nicht-Ziele
- Keine Videokonferenz- oder Audiofunktionen im MVP.

- Kein eigenständiger Export außerhalb des DMS (WEG-5).

- Keine Integration externer Abstimmungstools.

## Kritische Fälle
- **Referenzfehler:** Fehlende Verknüpfungen zu Teilnehmern oder Proxies führen zum Rollback der Transaktion.

- **Statuskonflikte:** Parallele Statusänderungen durch mehrere Benutzer werden blockiert.

- **Ungültige MEA-Werte:** Falsche Summen oder doppelte Stimmen verhindern die Freigabe des Meetings.

## Abhängigkeiten
- WEG-24 – Audit Log – Protokollierung aller Statusänderungen und CRUD-Operationen.

- WEG-9 – Meetings & Resolutions – Nutzung des Domain Models für nachgelagerte Prozesse (Agenda, Abstimmung, Beschluss).

- WEG-5 – Document Management – Speicherung der Protokoll-Drafts.

## Offene Fragen
- Soll das System hybride Meetings (Präsenz + Remote) bereits strukturell unterstützen?

- Sollen Agenda-Modelle in zukünftigen Phasen versioniert werden?

## Zukunftserweiterungen
- **Versionierte Agenden:** Parametrisierte Statusmodelle je nach WEG-Satzung.

- **Hybrid-Sitzungs-Support:** Erweiterung des Modells um Remote-Teilnahmen.

- **Mehrsprachige Meetingtypen:** Anpassbare Meetingarten und Statuscodes.

## Verknüpfte Tasks
- [WEG-900 – Domain Model & Bounded Context](https://maierharry.atlassian.net/browse/WEG-900) – Implementierung des Meeting-Datenmodells mit Entitäten, Statusflüssen und Konsistenzprüfungen.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Grundmodell mit Entitäten für Meeting, Agenda, Teilnehmer, Proxies und Beschlüsse; Audit-Integration; Statusflüsse Scheduled &rarr; Conducted &rarr; Closed &rarr; Archived.

**Phase 2**

Versionierte Agenda-Modelle und parametrisierte Statuslogik.

**Phase 3**

Hybrid-Meeting-Support, erweiterte Statusflüsse und Remote-Teilnehmerintegration.