---
title: WEG-76 – Period Lock & Snapshots (for later Billing)
confluence_id: 27165447
version: 20
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27165447/WEG-76+Period+Lock+Snapshots+for+later+Billing
---

**JIRA-Link:** [WEG-76 – Period Lock & Snapshots (for later Billing)](https://maierharry.atlassian.net/browse/WEG-76)

## Überblick
Das Modul **Period Lock & Snapshots** (WEG-76) stellt sicher, dass erfasste Zählerstände, Verbräuche und Finanzdaten nach Abschluss einer Abrechnungsperiode unveränderlich und nachvollziehbar bleiben. Es ist das Fundament für die revisionssichere Abrechnung und verhindert nachträgliche Änderungen, die Abweichungen in Wirtschaftsplänen oder Jahresabrechnungen verursachen könnten. Das Ziel besteht darin, Datenintegrität über alle Module hinweg sicherzustellen und konsistente Berechnungsgrundlagen für Audits, Berichte und gesetzliche Prüfungen zu schaffen.

## Beschreibung
WEG-76 definiert Sperrmechanismen für Zeiträume, die in der Abrechnung (WEG-87) oder Datenerfassung (WEG-7x-Reihe) verwendet werden. Nach dem Abschluss einer Periode werden automatisch **Sperr- und Snapshot-Einträge** erstellt, welche den Datenstand einfrieren und Änderungen verhindern. Diese Snapshots dienen gleichzeitig als Referenz für Wiederholungsberechnungen, Vergleiche und externe Prüfungen.

Hauptfunktionen:

- **Perioden-Sperren:** Markierung abgeschlossener Abrechnungszeiträume als &bdquo;locked&ldquo; mit unveränderlichen Datensätzen.

- **Snapshots:** Erstellung vollständiger Datenkopien (Zählerstände, Buchungen, Eigentümer, Umlagen) zum Zeitpunkt des Abschlusses.

- **Rollback-Schutz:** Verhindert versehentliche oder unautorisierte Änderungen nach Freigabe.

- **Differenz-Analyse:** Vergleich aktueller Daten mit historischen Snapshots zur Erkennung nachträglicher Abweichungen.

- **Audit-Integration:** Speicherung aller Sperr- und Snapshot-Ereignisse im Audit-Log (WEG-24).

- **Wiederherstellung:** Möglichkeit, Snapshots für Prüfer oder Wiederholungsabrechnungen bereitzustellen.

- **Abhängigkeiten:** Synchronisierte Sperrung mit Banking-, Abrechnungs- und Metering-Daten.

## Geschäftsregeln & Logik
- Eine Periode kann nur geschlossen werden, wenn alle zugehörigen Kampagnen (WEG-75) abgeschlossen sind.

- Gesperrte Perioden dürfen weder bearbeitet noch gelöscht werden.

- Jede Sperre erzeugt automatisch einen Snapshot-Datensatz.

- Snapshots enthalten ausschließlich bestätigte, validierte Werte.

- Nur Benutzer mit Administrator- oder Revisionsrolle dürfen Sperren aufheben.

- Jede Wiederherstellung erzeugt einen neuen Audit-Eintrag.

## Akzeptanzkriterien
- **Gegeben** eine Abrechnungsperiode ist abgeschlossen &rarr; **Wenn** der Lock aktiviert wird &rarr; **Dann** sind alle zugehörigen Daten schreibgeschützt und revisionssicher archiviert.

- **Gegeben** ein Benutzer versucht, Daten in einer gesperrten Periode zu ändern &rarr; **Wenn** die Aktion ausgeführt wird &rarr; **Dann** blockiert das System den Vorgang und zeigt eine Warnung an.

- **Gegeben** ein Snapshot wird erstellt &rarr; **Wenn** die Daten exportiert werden &rarr; **Dann** enthält der Export alle relevanten Informationen zum Abschlusszeitpunkt.

- **Gegeben** eine Wiederherstellung wird angefordert &rarr; **Wenn** ein Prüfer einen Snapshot öffnet &rarr; **Dann** zeigt das System den historischen Stand ohne Änderungen an.

- **Gegeben** neue Daten weichen von einem Snapshot ab &rarr; **Wenn** eine Differenzanalyse durchgeführt wird &rarr; **Dann** werden Abweichungen hervorgehoben und dokumentiert.

## Nicht-Ziele
- Keine automatische Wiederherstellung alter Daten ohne Benutzerfreigabe.

- Kein paralleles Bearbeiten mehrerer Perioden im MVP.

- Kein Vergleich über mehrere WEGs hinweg.

## Kritische Fälle
- **Fehlende Sperre:** Wenn eine Periode ungesperrt bleibt, können nachträgliche Änderungen unbemerkt bleiben.

- **Fehlerhafte Snapshots:** Unvollständige Datenkopien können zu falschen Prüfberichten führen.

- **Unsachgemäße Wiederherstellung:** Alte Datenstände dürfen den Live-Betrieb nicht überschreiben.

- **Rollenfehler:** Unautorisierte Benutzer dürfen keine Sperren aufheben.

## Abhängigkeiten
- WEG-75 – Reading Campaigns – Abschluss aller Kampagnen Voraussetzung für Sperre.

- WEG-8 – Finance & Banking – Einbeziehung offener Posten und Buchungen.

- WEG-87 – Accounting & Billing – Nutzung der Snapshots für Abrechnungsgrundlagen.

- WEG-24 – Audit Log – Dokumentation aller Sperr- und Wiederherstellungsaktionen.

## Offene Fragen
- Soll das System periodische Sperren automatisch nach Ablauf eines Monats aktivieren?

- Sollen Snapshots manuell exportierbar sein oder ausschließlich über Prüfprozesse zugänglich?

- Wie lange sollen Snapshots revisionssicher aufbewahrt werden?

## Zukunftserweiterungen
- **Automatische Periodensperren:** Zeitgesteuerte Lock-Prozesse.

- **Versionsvergleich:** Differenzanalyse über mehrere Jahre hinweg.

- **Erweiterte Audit-Reports:** Darstellung von Sperr- und Wiederherstellungsverläufen.

- **API-Export:** Bereitstellung von Snapshots für externe Prüfsysteme.

## Verknüpfte Tasks
- [WEG-760 – Period Lock Implementation](https://maierharry.atlassian.net/browse/WEG-760) – Technische Umsetzung des Sperr- und Snapshot-Mechanismus.

- [WEG-761 – Snapshot Exporter](https://maierharry.atlassian.net/browse/WEG-761) – Export und Bereitstellung von Snapshots.

- [WEG-762 – Lock Validation](https://maierharry.atlassian.net/browse/WEG-762) – Validierung abgeschlossener Perioden.

- [WEG-763 – Differential Analysis Tool](https://maierharry.atlassian.net/browse/WEG-763) – Vergleich aktueller und historischer Daten.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Sperrung abgeschlossener Perioden, Erstellung von Snapshots, Audit-Protokollierung, Wiederherstellung über Prüfzugriff.

**Phase 2**

Automatische Sperren, periodische Prüfungen, erweiterte Exportfunktionen, Differenzanalyse.

**Phase 3**

API-basierter Zugriff, mehrjährige Vergleiche, KI-gestützte Abweichungsanalyse.