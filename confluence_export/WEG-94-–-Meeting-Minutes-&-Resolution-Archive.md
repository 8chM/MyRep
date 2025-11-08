---
title: WEG-94 – Meeting Minutes & Resolution Archive
confluence_id: 27329433
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329433/WEG-94+Meeting+Minutes+Resolution+Archive
---

**JIRA-Link:** [WEG-94 – Meeting Minutes & Resolution Archive](https://maierharry.atlassian.net/browse/WEG-94)

## Überblick
Das Modul **Meeting Minutes & Resolution Archive** (WEG-94) dient der revisionssicheren Dokumentation und Archivierung abgeschlossener Eigentümerversammlungen. Es verwaltet automatisch erzeugte Sitzungsprotokolle, Beschlüsse und begleitende Anhänge und stellt diese dauerhaft im DMS (WEG-5) bereit. Ziel ist es, sämtliche Beschlussfassungen und Protokolle nachvollziehbar, versioniert und mandantenfähig zu speichern und jederzeit abrufbar zu machen.

## Beschreibung
WEG-94 erweitert das Meeting-Framework (WEG-90 ff.) um eine vollständige Protokollierungs- und Archivierungslogik. Nach Abschluss einer Versammlung (Status *Closed*) generiert das System automatisch ein finales Protokoll mit allen Tagesordnungspunkten, Abstimmungsergebnissen, Teilnehmern und Vollmachten. Das Dokument wird als PDF im DMS (WEG-5) abgelegt, versioniert und mit dem Audit-Log (WEG-24) verknüpft. Korrekturen oder Nachträge erzeugen stets neue Versionen, um die Revisionssicherheit zu gewährleisten. Über Filterfunktionen können archivierte Sitzungen nach Zeitraum, Themen oder Beschlussstatus durchsucht werden.

Hauptfunktionen:

- **Protokoll-Generierung:** Automatische Erstellung des Abschlussprotokolls nach Meeting-Ende mit allen relevanten Daten.

- **Archivierung & Versionierung:** Dauerhafte Speicherung im DMS mit Historienverfolgung älterer Versionen.

- **Volltextsuche:** Durchsuchbarkeit aller archivierten Protokolle, Beschlüsse und Kommentare.

- **Zugriff & Berechtigung:** Rollenbasierte Sichtbarkeit (z. B. Verwalter, Beirat, Eigentümer) gemäß RBAC-Regeln aus WEG-2.

- **Audit-Trail:** Jede Änderung oder Nachbearbeitung wird mit Zeitstempel, Benutzer und Grund dokumentiert.

- **Synchronisierung:** Lokale Zwischenspeicherung, falls das DMS temporär nicht erreichbar ist, mit automatischer Nachsynchronisierung.

## Geschäftsregeln & Logik
- Nach Abschluss eines Meetings wird automatisch ein Protokoll erstellt, versioniert und im DMS archiviert.

- Änderungen an einem abgeschlossenen Protokoll erzeugen zwingend eine neue Version; ältere Versionen bleiben unverändert erhalten.

- Gelöschte Protokolle sind nicht erlaubt – nur neue Revisionen dürfen erstellt werden.

- Zugriff auf archivierte Protokolle ist rollenbasiert und protokolliert.

- Bei DMS-Ausfällen werden Daten lokal zwischengespeichert und nach Wiederherstellung automatisch synchronisiert.

## Akzeptanzkriterien
- **Gegeben** ein Meeting befindet sich im Status *Closed* &rarr; **Wenn** das Protokoll erstellt wird &rarr; **Dann** wird automatisch ein finales Dokument im DMS (WEG-5) gespeichert und archiviert.

- **Gegeben** ein archiviertes Protokoll wird korrigiert &rarr; **Wenn** der Benutzer die Änderung speichert &rarr; **Dann** wird eine neue Version erstellt und die alte Revision bleibt im Audit-Log sichtbar.

- **Gegeben** ein Benutzer sucht im Archiv &rarr; **Wenn** ein Suchbegriff eingegeben wird &rarr; **Dann** liefert das System alle passenden Protokolle, Beschlüsse und Kommentare.

- **Gegeben** das DMS ist vorübergehend nicht erreichbar &rarr; **Wenn** ein Meeting abgeschlossen wird &rarr; **Dann** wird das Protokoll lokal zwischengespeichert und später synchronisiert.

## Nicht-Ziele
- Kein direkter Export außerhalb des DMS im MVP (z. B. E-Mail-Versand oder externe Ablage).

- Keine automatische Archivierung von Entwurfs- oder Zwischenprotokollen.

- Keine Integration mit externen Archivsystemen in Phase 1.

## Kritische Fälle
- **Versionierungskonflikt:** Wenn während der Protokollerstellung eine Änderung fehlschlägt, wird die Transaktion abgebrochen und eine Fehlermeldung ausgegeben.

- **DMS-Ausfall:** Temporäre Nichterreichbarkeit führt zu lokaler Zwischenspeicherung, aber keine Datenverluste.

- **Fehlerhafte Rechtevergabe:** Zugriffsbeschränkungen müssen strikt gemäß WEG-2 durchgesetzt werden.

## Abhängigkeiten
- WEG-5 – Document Management & Templates – Speicherung und Versionierung der Protokolle.

- WEG-2 – Identity & Access – Rollen- und Rechteverwaltung für Protokollzugriffe.

- WEG-24 – Audit Log – Nachvollziehbarkeit von Änderungen, Zugriffen und Versionen.

- WEG-93 – Resolution Registry – Referenzen auf Beschlüsse, die im Protokoll dokumentiert sind.

## Offene Fragen
- Sollen Protokolle automatisch als PDF mit Unterschriftsfeldern generiert werden?

- Welche Aufbewahrungsfristen sollen gelten (unbefristet oder gesetzlich geregelt)?

- Soll es eine Funktion geben, um Beschlussprotokolle mit digitalen Signaturen zu versehen?

## Zukunftserweiterungen
- **KI-Zusammenfassungen:** Automatische Generierung von Kurzprotokollen auf Basis der Beschlüsse.

- **Elektronische Signaturen:** eIDAS-konforme Signierung von Abschlussprotokollen.

- **Multi-Format-Export:** Export als PDF, DOCX oder JSON für externe Integrationen.

- **Archiv-Dashboard:** Statistische Auswertungen über Anzahl, Themen und Beschlussstatus.

## Verknüpfte Tasks
- [WEG-940 – Protokoll-Generierung & Finalisierung](https://maierharry.atlassian.net/browse/WEG-940) – Automatische Erstellung und Ablage finaler Meeting-Protokolle.

- [WEG-941 – Archiv-Suchfunktion & Filter](https://maierharry.atlassian.net/browse/WEG-941) – Implementierung der Volltextsuche und Filteroptionen im Archiv.

- [WEG-942 – Versionierung & Audit-Trail](https://maierharry.atlassian.net/browse/WEG-942) – Nachverfolgung und Speicherung aller Protokollrevisionen.

- [WEG-943 – DMS-Integration (WEG-5)](https://maierharry.atlassian.net/browse/WEG-943) – Anbindung an das Dokumentenmanagementsystem.

- [WEG-944 – Beschluss-Export & Reporting](https://maierharry.atlassian.net/browse/WEG-944) – Export von Beschlussprotokollen in standardisierte Formate.

- [WEG-945 – Rechtliche Aufbewahrungsfristen](https://maierharry.atlassian.net/browse/WEG-945) – Definition und Umsetzung gesetzlicher Aufbewahrungsregeln.

- [WEG-946 – Automatische Benachrichtigungen bei Protokollfreigabe](https://maierharry.atlassian.net/browse/WEG-946) – Information der Beteiligten bei Veröffentlichung neuer Versionen.

- [WEG-947 – Protokoll-Templates & Formatierung](https://maierharry.atlassian.net/browse/WEG-947) – Gestaltung und Anpassung der Protokollvorlagen.

- [WEG-948 – Zugriffsrechte-Verwaltung (RBAC)](https://maierharry.atlassian.net/browse/WEG-948) – Definition und Anwendung von Sichtbarkeits- und Bearbeitungsrechten.

- [WEG-949 – Archiv-Dashboard & Statistiken](https://maierharry.atlassian.net/browse/WEG-949) – Darstellung von Kennzahlen und Filteranalysen über archivierte Meetings.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Automatische Protokollerstellung, DMS-Integration, Versionierung, Audit-Trail, Suche und rollenbasierte Zugriffssteuerung.

**Phase 2**

Export- und Reporting-Funktionen, automatische Benachrichtigungen, rechtliche Aufbewahrungsfristen.

**Phase 3**

KI-basierte Zusammenfassungen, elektronische Signaturen, Dashboard-Auswertungen und Multi-Format-Exporte.