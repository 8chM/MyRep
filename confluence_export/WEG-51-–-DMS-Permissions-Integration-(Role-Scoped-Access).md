---
title: WEG-51 – DMS Permissions Integration (Role-Scoped Access)
confluence_id: 27656667
version: 11
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27656667/WEG-51+DMS+Permissions+Integration+Role-Scoped+Access
---

**JIRA-Link:** [WEG-51 – DMS Permissions Integration (Role-Scoped Access)](https://maierharry.atlassian.net/browse/WEG-51)

## Überblick

Das Modul **DMS Permissions Integration** (WEG-51) erweitert den Dokumentenkern (WEG-50) um eine fein granulierte rollenbasierte Zugriffskontrolle.

Es sorgt dafür, dass Benutzer:innen nur auf die Dokumente zugreifen können, die für ihre Rolle oder ihren Verantwortungsbereich bestimmt sind.

Damit stellt das Modul sicher, dass sensible Informationen — wie Finanzdaten, Eigentümerverträge oder Protokolle — nur von berechtigten Personen eingesehen oder heruntergeladen werden können.

Ziel ist es, Datenschutz, Revisionssicherheit und Transparenz innerhalb der WEG-Dokumentenverwaltung zu gewährleisten.

## Beschreibung

WEG-51 implementiert eine **Role-Scoped Access Control** (RSAC) auf Basis der im System definierten Benutzerrollen (z. B. Verwalter:in, Beirat, Eigentümer:in, Bewohner:in).

Zugriffsrechte werden kontextabhängig auf Dokumentenkategorien, Entitäten (z. B. Einheit, Gebäude, Vertrag) und Metadatenebene angewendet.

Die Integration nutzt die bestehenden RBAC-Policies aus WEG-2 und erweitert diese um eine zusätzliche Dokumentenebene.

Hauptfunktionen:

- **Rollenbasierte Sichtbarkeit:** Dokumente werden nur für Rollen angezeigt, die über entsprechende Berechtigungen verfügen (z. B. Beirat sieht Finanzberichte, Eigentümer nur Dokumente der eigenen Einheit).

- **Policy-basierte Steuerung:** Die Freigaben werden über Policies und Claims aus dem Identity-Modul (WEG-2) abgebildet; diese können zentral verwaltet werden.

- **Individualfreigaben:** Verwalter:innen können einzelne Dokumente gezielt für bestimmte Benutzer:innen oder Rollen freigeben.

- **Audit-Protokollierung:** Jeder Zugriff auf sensible Dokumente wird automatisch im Audit-Log (WEG-24) erfasst, inklusive Zeitpunkt, Benutzer und Aktionstyp.

- **Dynamische Kontextprüfung:** Berechtigungen berücksichtigen zusätzlich den Eigentumskontext, z. B. Einheit, Gebäude oder verknüpfte Verträge.

## Geschäftsregeln & Logik

- Zugriff auf Dokumente ist ausschließlich über Policies und Claims geregelt.

- Jede Dokumentenkategorie (z. B. Verträge, Protokolle, Rechnungen) besitzt eine eigene Berechtigungsstufe.

- Eigentümer:innen sehen nur Dokumente, die mit ihren Einheiten verknüpft sind.

- Beiratsmitglieder dürfen Finanz- und Sitzungsdokumente einsehen, jedoch keine vertraulichen Eigentümerdaten.

- Jede Sicht- oder Download-Aktion wird im Audit-Log (WEG-24) dokumentiert.

- Individualfreigaben überschreiben Rollenbeschränkungen nur für die Dauer der Freigabe.

## Akzeptanzkriterien

- **Gegeben** ein Eigentümer öffnet ein Dokument &rarr; **Wenn** die Kategorie für seine Einheit freigegeben ist &rarr; **Dann** wird das Dokument im Viewer angezeigt.

- **Gegeben** ein Beiratsmitglied ruft einen Finanzbericht auf &rarr; **Wenn** seine Rolle die Berechtigung &bdquo;Finance.Read&ldquo; enthält &rarr; **Dann** wird das Dokument vollständig angezeigt.

- **Gegeben** ein Verwalter vergibt eine Individualfreigabe &rarr; **Wenn** ein Eigentümer das Dokument aufruft &rarr; **Dann** erhält dieser temporären Zugriff, der nach Ablauf automatisch widerrufen wird.

- **Gegeben** ein Benutzer ohne Berechtigung öffnet ein Dokument &rarr; **Wenn** das System die Policy prüft &rarr; **Dann** wird der Zugriff verweigert und im Audit-Log registriert.

- **Gegeben** ein Administrator ändert eine Policy &rarr; **Wenn** sie aktiviert wird &rarr; **Dann** wird die neue Regel sofort systemweit angewendet und bestehende Zugriffe überprüft.

## Nicht-Ziele

- Keine externen Freigabelinks oder Cloud-Shares im MVP.

- Kein Selbstverwaltungsportal für Benutzerfreigaben.

- Keine Synchronisierung von Berechtigungen mit Drittsystemen.

## Kritische Fälle

- **Fehlkonfiguration von Policies:** Kann versehentlich zu zu weitreichenden Zugriffen führen — Audit-Prüfung erforderlich.

- **Verwaiste Dokumente:** Bei gelöschten Entitäten (z. B. Einheiten) müssen deren Zugriffsrechte automatisch entzogen werden.

- **Veraltete Individualfreigaben:** Abgelaufene Freigaben dürfen keinen Zugriff mehr ermöglichen; automatisches Cleanup notwendig.

## Abhängigkeiten

-  – Grundlage für Authentifizierung, Rollen und Claims.

-  – Definiert die zugrunde liegenden Berechtigungsrichtlinien.

-  – Erfasst Zugriffe und Änderungen an Berechtigungen.

-  – Basisfunktion für Dokumentenverwaltung und -speicherung.

-  – Integration der Datenschutzanforderungen für Zugriff und Pseudonymisierung.

## Offene Fragen

- Soll der Zugriff auf Metadaten (z. B. Dokumenttitel) unabhängig vom Dateizugriff geregelt werden?

- Wie granular sollen Administrator:innen Berechtigungen anpassen können (pro Kategorie, pro Dokument oder global)?

- Ist eine zeitgesteuerte Zugriffsbeschränkung (z. B. &bdquo;gültig bis&ldquo;) im MVP erforderlich?

## Zukunftserweiterungen

- **Temporäre Freigabelinks:** Möglichkeit zur zeitlich begrenzten Freigabe externer Dokumente.

- **Dynamische Berechtigungsmodelle:** Automatische Anpassung von Rechten basierend auf Rollen- und Objektstatus.

- **Self-Service-Freigaben:** Benutzer:innen können Dokumente selbst zur Ansicht anfordern (mit Genehmigung).

- **Zentralisierte Compliance-Berichte:** Auswertung von Zugriffsmustern und Datenschutzverletzungen.

## Verknüpfte Tasks

- [WEG-510 – Role-Scoped Access](https://maierharry.atlassian.net/browse/WEG-510) – Implementierung der Policy-Logik für rollenbasierte Dokumentenfreigaben.

- [WEG-511 – Individual Document Grants](https://maierharry.atlassian.net/browse/WEG-511) – Verwaltung von temporären, benutzerspezifischen Freigaben.

- [WEG-512 – Audit & Enforcement Hooks](https://maierharry.atlassian.net/browse/WEG-512) – Nachverfolgung aller Zugriffsevents über Middleware.

- [WEG-513 – Compliance Validation Rules](https://maierharry.atlassian.net/browse/WEG-513) – Automatische Prüfung auf DSGVO- und Datenschutzkonformität.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Implementierung der rollenbasierten Zugriffskontrolle (RBAC) für Dokumente, Integration mit Audit-Log, Individualfreigaben und Policy-basiertes Enforcement.

**Phase 2**

Temporäre Freigabelinks, granulare Rechteverwaltung pro Kategorie, automatisches Ablaufmanagement.

**Phase 3**

Dynamische Berechtigungsmodelle, Self-Service-Freigaben, Compliance-Reporting und KI-gestützte Policy-Optimierung.