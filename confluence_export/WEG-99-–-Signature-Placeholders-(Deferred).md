---
title: WEG-99 – Signature Placeholders (Deferred)
confluence_id: 27853522
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27853522/WEG-99+Signature+Placeholders+Deferred
---

**JIRA-Link:** [WEG-99 – Signature Placeholders (Deferred)](https://maierharry.atlassian.net/browse/WEG-99)

## Überblick
Das Modul **Signature Placeholders** (WEG-99) legt die technische Grundlage für die spätere Integration rechtssicherer elektronischer Signaturen. Im MVP werden noch keine echten digitalen Signaturen erzeugt, sondern Platzhalter eingefügt, die den späteren Signaturprozess simulieren. Ziel ist es, die Infrastruktur, Datenmodelle und Schnittstellen zu definieren, die für eine spätere Implementierung eIDAS-konformer Signaturen erforderlich sind.

## Beschreibung
WEG-99 stellt eine vorbereitende Komponente für digitale Signaturen dar. Es ermöglicht das Einfügen von Platzhaltern an relevanten Stellen in Protokollen, Beschlüssen und anderen rechtlich bindenden Dokumenten. Diese Platzhalter fungieren als visuelle und technische Marker, an denen in künftigen Phasen echte Signaturen angebracht werden. Darüber hinaus definiert das Modul die Schnittstellen, Datenstrukturen und Ereignisse, die für den späteren Signatur-Workflow benötigt werden, und integriert bereits die Protokollierung im Audit-Log (WEG-24).

Hauptfunktionen:

- **Platzhalter-Erzeugung:** Automatische Einfügung von Signaturfeldern bei der Erstellung von Protokollen oder Beschlüssen.

- **Signatur-Metadaten:** Speicherung von Benutzer-ID, Zeitstempel und Dokument-ID, um spätere Signaturen eindeutig zuordnen zu können.

- **API-Vorbereitung:** Definition von Endpunkten für den künftigen Signatur-Workflow (z. B. Signaturanforderung, Statusprüfung).

- **Audit-Integration:** Protokollierung aller Platzhalter-Generierungen im Audit-Log (WEG-24).

- **Mandantenfähigkeit:** Platzhalter werden für jede WEG separat erzeugt und verwaltet.

- **DMS-Verknüpfung:** Speicherung signaturfähiger Dokumente im DMS (WEG-5) mit Referenz auf Platzhalterpositionen.

## Geschäftsregeln & Logik
- Bei der Erstellung eines Protokolls oder Beschlusses werden automatisch Platzhalter an vordefinierten Positionen eingefügt.

- Jeder Platzhalter ist eindeutig identifizierbar und enthält alle relevanten Metadaten.

- Platzhalter dürfen nachträglich nicht gelöscht, sondern nur deaktiviert oder ersetzt werden.

- Das System prüft beim Abschluss eines Dokuments, ob alle vorgesehenen Platzhalter vorhanden sind.

- Alle Platzhalterereignisse (Erzeugung, Änderung, Deaktivierung) werden im Audit-Log gespeichert.

## Akzeptanzkriterien
- **Gegeben** ein Protokoll wird erstellt &rarr; **Wenn** Unterschriften erforderlich sind &rarr; **Dann** werden automatisch Platzhalter für alle benötigten Signaturen eingefügt.

- **Gegeben** ein Beschluss wird gespeichert &rarr; **Wenn** dieser Signaturen erfordert &rarr; **Dann** werden Signaturfelder mit Benutzer-ID und Zeitstempel angelegt.

- **Gegeben** ein Dokument wird abgeschlossen &rarr; **Wenn** ein Platzhalter fehlt &rarr; **Dann** wird eine Warnung angezeigt und das Speichern blockiert.

- **Gegeben** ein Platzhalter wird entfernt &rarr; **Wenn** dies geschieht &rarr; **Dann** wird der Vorgang im Audit-Log vermerkt und als &bdquo;deaktiviert&ldquo; markiert.

## Nicht-Ziele
- Keine Erstellung oder Validierung echter elektronischer Signaturen im MVP.

- Keine Integration mit eIDAS-, DocuSign- oder ähnlichen Diensten.

- Keine rechtliche Prüfung oder Verifikation von Signaturen.

## Kritische Fälle
- **Fehlende Platzhalter:** Wenn ein Dokument abgeschlossen wird, ohne dass alle vorgesehenen Platzhalter enthalten sind, muss eine Warnung erfolgen.

- **Inkonsistente Daten:** Wenn ein Platzhalter gelöscht oder fehlerhaft verknüpft wird, wird automatisch ein Audit-Eintrag erzeugt.

- **Falsche Reihenfolge:** Platzhalter müssen in logischer Reihenfolge (z. B. Verwalter, Beirat, Eigentümer) erscheinen.

## Abhängigkeiten
- WEG-5 – Document Management & Templates – Verwaltung und Speicherung signaturfähiger Dokumente.

- WEG-24 – Audit Log – Aufzeichnung von Platzhalter- und Signaturereignissen.

- WEG-94 – Meeting Minutes & Resolution Archive – Nutzung von Platzhaltern in Protokollen und Beschlussdokumenten.

## Offene Fragen
- Welche Signaturdienste sollen in Phase 2 integriert werden (z. B. DocuSign, eIDAS)?

- Sollen mehrere Signaturen pro Dokument unterstützt werden (z. B. Verwalter und Beirat)?

- Soll die Signaturreihenfolge konfigurierbar sein?

## Zukunftserweiterungen
- **eIDAS-Integration:** Anbindung rechtssicherer elektronischer Signaturen.

- **Signatur-Workflow:** Automatischer Ablauf von Signaturanfragen, Statusrückmeldungen und Genehmigungen.

- **Mehrfachsignaturen:** Unterstützung mehrerer Unterschriftenfelder pro Dokument.

- **Signatur-Dashboard:** Übersicht über ausstehende und abgeschlossene Signaturen.

## Verknüpfte Tasks
- [WEG-990 – Signatur-Platzhalter-Datenmodell](https://maierharry.atlassian.net/browse/WEG-990) – Definition des Datenmodells für Platzhalter und Metadaten.

- [WEG-991 – Platzhalter-Generierung in Protokollen](https://maierharry.atlassian.net/browse/WEG-991) – Automatische Einfügung von Platzhaltern in generierte Dokumente.

- [WEG-992 – API-Schnittstellen für Signatur-Integration](https://maierharry.atlassian.net/browse/WEG-992) – Bereitstellung von Endpunkten zur Signaturerweiterung.

- [WEG-993 – Audit-Log-Integration für Signaturen](https://maierharry.atlassian.net/browse/WEG-993) – Protokollierung von Signaturereignissen im System.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Definition des Signaturdatenmodells, Platzhaltererzeugung in Dokumenten, API-Vorbereitung, Audit-Integration.

**Phase 2**

Integration eIDAS-konformer Signaturen, Signatur-Workflow, Mehrfachsignaturen.

**Phase 3**

Signatur-Dashboard, KI-basierte Verifikationen, erweiterte Workflows mit Priorisierung.