---
title: WEG-93 – Resolution Registry & Supersession (Skeleton)
confluence_id: 27165462
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27165462/WEG-93+Resolution+Registry+Supersession+Skeleton
---

**JIRA-Link:** [WEG-93 – Resolution Registry & Supersession (Skeleton)](https://maierharry.atlassian.net/browse/WEG-93)

## Überblick
Das Modul **Resolution Registry & Supersession** (WEG-93) bildet das zentrale Register für alle Beschlüsse innerhalb der Eigentümerversammlungen. Es dient der lückenlosen Nachverfolgung, Versionierung und Supersession-Verwaltung (Aufhebung oder Ersetzung) von Beschlüssen. Jeder Beschluss bleibt dauerhaft im System gespeichert und wird über Statusänderungen (aktiv, aufgehoben, ersetzt) verwaltet, um die rechtliche Nachvollziehbarkeit sicherzustellen.

## Beschreibung
WEG-93 erweitert das Meeting-Framework (WEG-90 bis WEG-92) um eine dedizierte Beschlussverwaltung, die sämtliche Entscheidungen einer WEG strukturiert dokumentiert. Das System verfolgt den gesamten Lebenszyklus eines Beschlusses – von der Entstehung über Abstimmung, Gültigkeit bis zur eventuellen Aufhebung oder Ersetzung durch neue Beschlüsse. Beschlüsse mit finanziellen oder baulichen Folgen werden automatisch mit den relevanten Modulen **Finance & Banking (WEG-8)** bzw. **Ticketing / Issue Management (WEG-97)** verknüpft. Alle Vorgänge sind revisionssicher dokumentiert, und Änderungen erzeugen neue Revisionen statt Überschreibungen.

Hauptfunktionen:

- **Beschlussregister:** Speicherung aller Beschlüsse mit eindeutiger ID, Titel, Datum, Beschlusstext, Status und Verknüpfungen zu betroffenen Themen.

- **Statusverwaltung:** Automatische Statusänderung bei Aufhebung oder Ersetzung (Supersession).

- **Supersession-Verknüpfungen:** Bidirektionale Relationen zwischen alten und neuen Beschlüssen bei inhaltlicher Überschneidung.

- **Pflichtverknüpfungen:** Zwangsverweise auf WEG-8 (Finance) oder WEG-97 (Ticketing), sofern finanzielle oder bauliche Auswirkungen bestehen.

- **Historisierung:** Frühere Versionen eines Beschlusses bleiben lesbar und vollständig auditierbar.

- **Audit-Trail:** Jede Änderung, Freigabe oder Ersetzung wird im Audit-Log (WEG-24) erfasst.

- **Reporting:** Export offener, aktiver und aufgehobener Beschlüsse für Auswertungen und Nachverfolgung.

## Geschäftsregeln & Logik
- Beschlüsse werden niemals gelöscht, sondern ausschließlich historisiert und mit einem Status versehen.

- Eine Supersession-Verknüpfung darf nur zwischen Beschlüssen desselben Themas oder Gegenstands bestehen.

- Jeder Beschluss mit finanzieller oder baulicher Folge muss mindestens eine aktive Referenz zu WEG-8 oder WEG-97 enthalten.

- Änderungen an bestehenden Beschlüssen erzeugen automatisch neue Revisionen mit Referenz auf den Vorgänger.

- Mehrere konkurrierende Beschlüsse innerhalb derselben Sitzung müssen manuell durch die Verwaltung freigegeben werden.

## Akzeptanzkriterien
- **Gegeben** ein neuer Beschluss wird angelegt &rarr; **Wenn** ein bestehender Beschluss zum selben Thema existiert &rarr; **Dann** erstellt das System automatisch eine Supersession-Verknüpfung und markiert den alten Beschluss als &bdquo;superseded&ldquo;.

- **Gegeben** ein Beschluss betrifft ein Thema mit finanziellen Auswirkungen &rarr; **Wenn** der Benutzer versucht, ihn ohne Finance-Referenz (WEG-8) zu speichern &rarr; **Dann** blockiert das System den Vorgang und gibt eine Fehlermeldung aus.

- **Gegeben** ein Beschluss wird geändert &rarr; **Wenn** die Änderung gespeichert wird &rarr; **Dann** erzeugt das System automatisch eine neue Revision und verknüpft sie mit dem Original.

- **Gegeben** ein Beschluss wird als aufgehoben markiert &rarr; **Wenn** dieser Status gesetzt wird &rarr; **Dann** wird der Beschluss schreibgeschützt und im Register archiviert.

## Nicht-Ziele
- Keine juristische Bewertung oder automatische Rechtsauslegung von Beschlüssen.

- Keine automatische Erstellung von Supersession-Verknüpfungen zwischen inhaltlich ähnlichen, aber nicht identischen Themen.

- Kein Workflow für rechtliche Prüfungen im MVP.

## Kritische Fälle
- **Doppelte Beschlüsse:** Mehrere Beschlüsse zum selben Thema ohne Supersession führen zu Inkonsistenzen; Warnung erforderlich.

- **Fehlende Pflichtverknüpfung:** Beschlüsse mit Finanzfolge ohne zugehörige WEG-8-Referenz werden blockiert.

- **Mehrfach-Supersession:** Ketten von Beschlüssen (A &rarr; B &rarr; C) müssen konsistent gehalten werden, um Rückverweise zu ermöglichen.

## Abhängigkeiten
- WEG-90 – Meetings Domain Model – Struktur und Statussteuerung der Eigentümerversammlung.

- WEG-91 – Agenda & Participants – Quelle der Agenda und Verknüpfung zu einzelnen Beschlusspunkten.

- WEG-92 – Voting Rules Model – Grundlage für die Berechnung und Gültigkeit von Beschlussmehrheiten.

- WEG-8 – Finance & Banking – Referenzen bei finanziellen Auswirkungen.

- WEG-97 – Ticketing & Issue Management – Referenzen bei baulichen oder operativen Umsetzungsmaßnahmen.

- WEG-24 – Audit Log – Nachvollziehbarkeit aller Änderungen und Supersession-Ereignisse.

## Offene Fragen
- Sollen Beschlüsse zusätzlich nach Themenkategorien (Finanzen, Bau, Ordnung, Sonstiges) gruppiert werden?

- Soll eine manuelle Freigabe durch den Beirat oder die Verwaltung erforderlich sein, bevor Supersessions aktiv werden?

- Soll das System automatisch Beschlüsse als &bdquo;abgeschlossen&ldquo; markieren, sobald alle verknüpften Maßnahmen (Tickets/Finanzen) umgesetzt sind?

## Zukunftserweiterungen
- **Supersession-Visualisierung:** Darstellung von Beschlussketten und Versionshistorien in einem Graph-View.

- **Kategorisierung:** Einführung von Beschlusskategorien für schnellere Filterung und Analyse.

- **KPI-Dashboard:** Kennzahlen zu offenen, umgesetzten und aufgehobenen Beschlüssen.

- **Automatisierte Cross-Modul-Analyse:** Verknüpfung von Beschlussfolgen mit Finanz- und Ticketdaten zur Statusermittlung.

## Verknüpfte Tasks
- [WEG-930 – Resolution Registry Skeleton](https://maierharry.atlassian.net/browse/WEG-930) – Zentrales Register für alle Beschlüsse mit Lebenszyklusverwaltung.

- [WEG-931 – Supersession Links (repeal/supersede/amend)](https://maierharry.atlassian.net/browse/WEG-931) – Implementierung der bidirektionalen Verknüpfungen zwischen alten und neuen Beschlüssen.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Grundlegendes Beschlussregister mit Supersession-Logik, Pflichtverknüpfungen zu WEG-8 und WEG-97, Statussteuerung (aktiv, superseded, aufgehoben), Audit-Integration.

**Phase 2**

Erweiterte Supersession-Verwaltung, KPI-Dashboard, Kategorienstruktur.

**Phase 3**

Graphische Visualisierung, automatische Statusableitung aus Finanz- und Ticketdaten, erweiterte Berichtslogik.