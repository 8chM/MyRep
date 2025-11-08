---
title: WEG-85 – Statement Review & Lock
confluence_id: 27722339
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722339/WEG-85+Statement+Review+Lock
---

**JIRA-Link:** [WEG-85 – Statement Review & Lock](https://maierharry.atlassian.net/browse/WEG-85)

## Überblick
Das Modul **Statement Review & Lock **(WEG-85) stellt sicher, dass importierte Kontoauszüge nach ihrer Überprüfung durch den Verwalter nicht mehr verändert werden können. Es dient als Kontroll- und Freigabeschicht für die in **WEG-82 – Banking Inbound** importierten Bankdaten und bildet die Grundlage für revisionssichere Finanzprozesse. Ziel ist es, Änderungen nach der Freigabe vollständig zu verhindern und gleichzeitig alle Aktionen transparent im Audit-Log nachzuverfolgen.

## Beschreibung
WEG-85 erweitert den Importprozess (WEG-82) um eine strukturierte Prüf- und Freigabelogik. Verwalter können Kontoauszüge prüfen, freigeben und anschließend sperren, um unautorisierte Änderungen auszuschließen. Der Sperrmechanismus (&bdquo;Write-Lock&ldquo;) verhindert, dass Transaktionen, Zuordnungen oder Salden nach der Freigabe angepasst werden. Nur Hauptverwalter können den Lock aufheben, wobei jeder Vorgang protokolliert wird.

Hauptfunktionen:

- **Review-Workflow:** Kontoauszüge können vor der Freigabe geprüft, korrigiert und validiert werden.

- **Write-Lock:** Nach Freigabe werden Kontoauszüge schreibgeschützt; keine weiteren Änderungen sind möglich.

- **Lock-Aufhebung:** Nur Hauptverwalter dürfen den Lock mit Begründung aufheben.

- **Audit-Trail:** Jede Freigabe, Sperrung oder Entsperrung wird im Audit-Log (WEG-24) protokolliert.

- **Benachrichtigung:** Bei Lock-Änderungen werden betroffene Benutzer automatisch informiert.

- **Sichtbarkeitsregeln:** Nur autorisierte Benutzer mit Rolle *Verwalter* oder höher dürfen Freigaben durchführen.

## Geschäftsregeln & Logik
- Nach einer Freigabe sind keine Änderungen an Transaktionen, Zuordnungen oder Salden mehr zulässig.

- Lock-Aufhebungen erfordern eine dokumentierte Begründung.

- Jeder Lock-Zustand wird eindeutig versioniert.

- Bei Rollback einer Sperrung wird der ursprüngliche Status wiederhergestellt, ohne Daten zu löschen.

- Eine gleichzeitige Freigabe durch mehrere Benutzer ist blockiert.

## Akzeptanzkriterien
- **Gegeben** ein Kontoauszug ist importiert &rarr; **Wenn** der Verwalter ihn prüft und auf &bdquo;Freigeben & Sperren&ldquo; klickt &rarr; **Dann** wird der Auszug schreibgeschützt und alle Änderungen sind gesperrt.

- **Gegeben** ein Hauptverwalter hebt einen Lock auf &rarr; **Wenn** er eine Begründung eingibt &rarr; **Dann** wird der Vorgang protokolliert und alle betroffenen Benutzer erhalten eine Benachrichtigung.

- **Gegeben** ein Benutzer versucht, einen gesperrten Kontoauszug zu ändern &rarr; **Wenn** der Lock aktiv ist &rarr; **Dann** verweigert das System die Änderung und zeigt eine Warnung an.

- **Gegeben** ein Lock wurde versehentlich gesetzt &rarr; **Wenn** der Rollback erfolgt &rarr; **Dann** wird der ursprüngliche Status wiederhergestellt und im Audit-Log dokumentiert.

- **Gegeben** mehrere Benutzer versuchen gleichzeitig eine Freigabe &rarr; **Wenn** ein Lock aktiv ist &rarr; **Dann** wird der zweite Freigabeversuch blockiert.

## Nicht-Ziele
- Keine automatische Freigabe nach Import.

- Keine digitale Signatur oder Stempelung der Kontoauszüge im MVP.

- Kein automatischer Plausibilitätscheck über die Importlogik von WEG-82 hinaus.

## Kritische Fälle
- **Fehl-Lock:** Eine unbeabsichtigte Sperrung muss rollback-fähig und dokumentiert sein.

- **Paralleländerungen:** Gleichzeitige Freigaben dürfen nicht zu widersprüchlichen Zuständen führen.

- **Fehlende Berechtigung:** Benutzer ohne ausreichende Rechte dürfen keine Lock-Änderungen durchführen.

## Abhängigkeiten
- WEG-8 – Finance & Banking – Übergeordnetes Modul für Finanzdaten.

- WEG-82 – Banking Inbound – Quelle der Kontoauszüge und Importdaten.

- WEG-2 – Identity & Access – Verwaltung von Benutzerrollen und Berechtigungen.

- WEG-24 – Audit Log – Protokollierung aller Review- und Lock-Vorgänge.

## Offene Fragen
- Soll eine mehrstufige Freigabe (z. B. Verwalter &rarr; Hauptverwalter &rarr; Prüfer) bereits in Phase 2 umgesetzt werden?

- Sollen Benutzer über Lock-Änderungen per In-App-Notification (WEG-6) informiert werden?

## Zukunftserweiterungen
- **Multi-Stage-Approval:** Mehrstufiger Freigabeprozess mit optionaler Prüferrolle.

- **Digitale Signatur:** Integration von Signaturen oder Prüfstempeln für Kontoauszüge.

- **Automatische Erinnerungen:** Benachrichtigung bei ausstehenden Freigaben oder nicht gesperrten Statements.

## Verknüpfte Tasks
- [WEG-822 – Statement Review & Lock](https://maierharry.atlassian.net/browse/WEG-822) – Implementierung der Prüf- und Sperrlogik mit Audit-Integration und Berechtigungsprüfung (bereits Bestandteil von WEG-82).

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Review-Workflow, Write-Lock-Mechanismus, Freigabeprozess und Audit-Protokollierung (bereits Teil von WEG-82).

**Phase 2**

Multi-Stage-Approval, erweiterte Benachrichtigungen und digitale Signaturen.

**Phase 3**

Automatisierte Prüfungen, Erinnerungsfunktionen und Compliance-Berichte.