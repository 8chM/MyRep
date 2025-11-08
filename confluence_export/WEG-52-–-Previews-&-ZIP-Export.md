---
title: WEG-52 – Previews & ZIP Export
confluence_id: 27165432
version: 11
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27165432/WEG-52+Previews+ZIP+Export
---

**JIRA-Link:** [WEG-52 – Previews & ZIP Export](https://maierharry.atlassian.net/browse/WEG-52)

## Überblick

Das Modul **Previews & ZIP Export** (WEG-52) erweitert das Dokumentenmanagement-System (DMS) um komfortable Anzeige- und Exportfunktionen.

Es ermöglicht Benutzer:innen, Dokumente bereits vor dem Download im Browser als Vorschau zu betrachten und mehrere Dateien gesammelt als ZIP-Archiv herunterzuladen.

Ziel ist es, die tägliche Arbeit mit Dokumenten effizienter zu gestalten und gleichzeitig die Systemperformance und Zugriffssicherheit zu wahren.

## Beschreibung

WEG-52 ergänzt das Basismodul **DMS Core (WEG-50)** um zwei wesentliche Komfortfunktionen: **Dateivorschau** und **ZIP-Export**.

Die Vorschau ermöglicht eine schnelle Einsicht in PDFs oder Bilddateien, ohne dass diese heruntergeladen werden müssen.

Der ZIP-Export erlaubt es, mehrere Dokumente — etwa Sitzungsunterlagen oder Eigentümerabrechnungen — gesammelt in einer strukturierten ZIP-Datei bereitzustellen.

Hauptfunktionen:

- **Vorschau-Funktion (Preview Engine):** Erstellt serverseitig Thumbnails oder rendert die erste Seite von PDF-Dokumenten direkt im Browser. Unterstützt werden gängige Formate wie PDF, PNG, JPG.

- **ZIP-Export:** Bündelt mehrere ausgewählte Dokumente zu einem temporären ZIP-Archiv und stellt es für den autorisierten Benutzer zum Download bereit.

- **Freigabeprüfung (Access Validation):** Nur Dokumente, die gemäß RBAC (WEG-2) freigegeben sind, können angezeigt oder exportiert werden.

- **Audit-Protokollierung:** Jede Vorschau und jeder Export werden im **Audit Log (WEG-24)** dokumentiert — inklusive Zeit, Benutzer, Aktion und betroffenen Dokumenten.

- **Performance-Optimierung:** ZIP-Generierung und Previews laufen asynchron über Job-Queues, um die Serverlast gering zu halten.

## Geschäftsregeln & Logik

- Vorschauen sind nur für unterstützte Dateitypen aktiv (PDF, PNG, JPG).

- Die ZIP-Erstellung darf nur durch Benutzer:innen erfolgen, die alle enthaltenen Dateien lesen dürfen.

- Der ZIP-Download-Link ist nur temporär gültig (z. B. 10 Minuten).

- Preview-Daten (Thumbnails) werden gecached und regelmäßig invalidiert.

- Jeder Zugriff oder Export wird im Audit-Log festgehalten.

## Akzeptanzkriterien

- **Gegeben** ein Benutzer öffnet die Vorschau eines Dokuments &rarr; **Wenn** das Dateiformat unterstützt wird &rarr; **Dann** wird ein Thumbnail oder eine erste Seite im Browser angezeigt.

- **Gegeben** ein Benutzer öffnet eine Vorschau &rarr; **Wenn** er keine Berechtigung für das Dokument besitzt &rarr; **Dann** wird der Zugriff verweigert und im Audit-Log dokumentiert.

- **Gegeben** mehrere Dokumente sind markiert &rarr; **Wenn** der Benutzer den Export startet &rarr; **Dann** wird serverseitig ein ZIP-Archiv mit nur den berechtigten Dateien erstellt.

- **Gegeben** ein ZIP-Archiv wird generiert &rarr; **Wenn** der Benutzer den Download-Link nutzt &rarr; **Dann** ist dieser nur für den definierten Zeitraum aktiv und danach ungültig.

- **Gegeben** ein Benutzer exportiert Dokumente &rarr; **Wenn** der Export erfolgreich abgeschlossen ist &rarr; **Dann** wird ein Audit-Eintrag mit Benutzer-ID, Zeitpunkt und Dateiliste erstellt.

## Nicht-Ziele

- Kein Streaming-Preview für Videos oder Audiodateien im MVP.

- Keine Inline-Bearbeitung von Dokumenten in der Vorschau.

- Kein direkter Cloud-Sync oder Live-Link-Export.

## Kritische Fälle

- **Ungültige Dateitypen:** Nicht unterstützte Formate dürfen keine Previews erzeugen.

- **Rechteverletzung:** ZIP-Archive dürfen keine Dateien enthalten, für die keine Berechtigung besteht.

- **Leistungsengpässe:** Große ZIP-Exporte müssen asynchron behandelt werden, um Timeouts zu vermeiden.

- **Zwischenspeicherung:** Temporäre Dateien müssen nach Ablauf automatisch gelöscht werden.

## Abhängigkeiten

-  – Basisfunktionen für Dokumentenverwaltung und Dateispeicherung.

-  – Erfassung und Nachvollziehbarkeit aller Vorschau- und Exportvorgänge.

-  – Rollen- und Berechtigungsprüfung bei Zugriffen.

-  – Fehlerbehandlung bei ZIP-Generierung und Rendering-Prozessen.

## Offene Fragen

- Soll das System Wasserzeichen oder &bdquo;Confidential&ldquo;-Hinweise in Previews einfügen können?

- Dürfen Benutzer:innen ZIP-Dateien nach dem Download erneut generieren oder ist ein Cache vorgesehen?

- Ist die Vorschau auch für Office-Dokumente (DOCX, XLSX) geplant?

## Zukunftserweiterungen

- **Wasserzeichen & Signaturen:** Ergänzung digitaler Signaturen oder Wasserzeichen in Previews.

- **Erweiterte Formate:** Unterstützung für zusätzliche Dateitypen (Office, Text, E-Mail).

- **Streaming-Preview:** Vorschau großer Dateien ohne vollständigen Download.

- **Batch-Exports:** Automatisierte Exporte z. B. für Eigentümerversammlungen oder Monatsberichte.

## Verknüpfte Tasks

- [WEG-520 – PDF First-Page Preview & Image Thumbs](https://maierharry.atlassian.net/browse/WEG-520) – Implementierung der Vorschau-Engine für unterstützte Dateitypen.

- [WEG-521 – ZIP Export (selection, by link target)](https://maierharry.atlassian.net/browse/WEG-521) – Erstellung und Download temporärer ZIP-Archive.

- [WEG-522 – Audit & Access Validation](https://maierharry.atlassian.net/browse/WEG-522) – Nachverfolgung aller Vorschau- und Exportaktionen im Audit-System.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

PDF- und Bildvorschau, ZIP-Export, Freigabeprüfung, Audit-Protokollierung und temporäre Download-Links.

**Phase 2**

Wasserzeichen und digitale Signaturen, verbesserte Caching-Strategie, parallele ZIP-Erstellung.

**Phase 3**

Streaming-Previews für zusätzliche Formate (Office, E-Mail), automatisierte Batch-Exporte und Cloud-basierte Archivierung.