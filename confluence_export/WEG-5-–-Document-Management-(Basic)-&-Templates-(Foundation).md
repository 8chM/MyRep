---
title: WEG-5 – Document Management (Basic) & Templates (Foundation)
confluence_id: 27722294
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722294/WEG-5+Document+Management+Basic+Templates+Foundation
---

**JIRA-Link:** [WEG-5 – Document Management (Basic) & Templates (Foundation)](https://maierharry.atlassian.net/browse/WEG-5)

## Beschreibung / Kernzweck

Das Modul **WEG-5 – Document Management & Templates** bildet die Grundlage für sämtliche Dokumentenprozesse im WEG Management System (WMS). Es dient der sicheren, zentralen Verwaltung, Versionierung und Freigabe von Dokumenten – von Abrechnungen und Verträgen bis hin zu Eigentümerversammlungsprotokollen und Kontoauszügen. Ziel ist eine strukturierte, nachvollziehbare und revisionssichere Ablage sämtlicher WEG-relevanter Unterlagen sowie eine automatisierte Erzeugung standardisierter Dokumente auf Basis dynamischer Vorlagen.

Das System gewährleistet höchste Transparenz und Rechtssicherheit durch mandantenbezogene Trennung, rollenbasierte Zugriffssteuerung, automatisierte Archivierung und vollständige Audit-Protokollierung. Neben klassischen Dokumentenprozessen integriert WEG-5 auch das Finanzdokumentenhandling (WEG-58/59) für Kontoauszüge, Abrechnungsdokumente und Bilanzberichte.

## Inhalte

Untermodul

Kurzbeschreibung

[WEG-50 – DMS Core (Document, Version, FileBlob, Links)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Kernlogik für Upload, Speicherung, Versionierung und Verknüpfung von Dokumenten mit anderen Systemelementen.

[WEG-51 – DMS Permissions Integration (Role-Scoped Access)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Rollenbasierte Zugriffskontrolle, die definiert, welche Benutzergruppen auf welche Dokumente zugreifen dürfen.

[WEG-52 – Previews & ZIP Export](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Vorschau für PDF und Bilddateien sowie Export mehrerer Dokumente als ZIP-Archiv.

[WEG-53 – Template Engine (Foundation)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Automatische Generierung strukturierter Dokumente anhand definierter Vorlagen mit Platzhaltern.

[WEG-54 – Retention & Archive (Locked Periods)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Revisionssichere Archivierung abgeschlossener Dokumente und Sperrung in abgeschlossenen Perioden.

[WEG-55 – Virus Scan Hook (Stub)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Sicherheitsprüfung für Uploads; blockiert infizierte oder nicht erlaubte Dateien.

[WEG-56 – PDF Branding Base (per Association)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Einheitliches Erscheinungsbild automatisch erzeugter PDFs im Design der jeweiligen WEG.

[WEG-57 – Contract Management (Vendors, Maintenance, Insurance)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Verwaltung von Verträgen mit Lieferanten, Wartungsfirmen und Versicherungen, inklusive Fristenüberwachung.

[WEG-58 – Owner Ledger & Balances (Accounts Receivable)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Generierung von Kontoauszügen und Buchungsnachweisen als PDF/CSV direkt aus dem Eigentümerkonto.

[WEG-59 – Financial Onboarding & Initialization](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Import initialer Finanzdaten und Erzeugung der dazugehörigen Dokumentation (z. B. Startsalden-Reports, Prüfprotokolle).

## Geschäftslogik

Das Modul bildet den zentralen Kern aller dokumentenbezogenen Prozesse innerhalb des Systems:

- **Dokumentenverwaltung:** Alle Dokumente werden mandantengetrennt gespeichert. Änderungen erzeugen automatisch neue Versionen, die im Verlauf nachvollziehbar bleiben.

- **Zugriffssteuerung:** Der Zugriff erfolgt auf Basis der Rollen aus WEG-2; Eigentümer sehen nur eigene Dokumente, Beiräte Finanzunterlagen, Verwalter alle Daten.

- **Template-Engine:** Wiederkehrende Dokumente – etwa Abrechnungen, Beschlussprotokolle, Kontoauszüge oder Verträge – werden über Vorlagen mit Platzhaltern automatisch erzeugt.

- **Audit-Nachvollziehbarkeit:** Jede Aktion (Upload, Änderung, Freigabe, Download) wird mit Zeitstempel, Benutzer und Aktion im Audit-Log (WEG-24) gespeichert.

- **Archivierung & Retention:** Nach Abschluss eines Wirtschaftsjahres oder Projekts werden Dokumente automatisch archiviert und gegen Änderungen gesperrt.

- **Vertragsverwaltung:** Fristen und Verlängerungen werden systemisch überwacht; bei Annäherung an Kündigungstermine erfolgen automatische Benachrichtigungen.

- **Finanzdokumente:** Kontoauszüge (WEG-58) und Onboarding-Protokolle (WEG-59) werden automatisch generiert, archiviert und mit dem DMS verknüpft.

- **Such- und Exportfunktionen:** Eine Volltextsuche ermöglicht das Auffinden von Dokumenten anhand von Inhalt, Metadaten oder Kategorien. Mehrere Dokumente können gesammelt exportiert werden.

- **Integrität & Sicherheit:** Uploads werden auf Viren geprüft, Metadaten validiert und durch rollenbasierte Policies geschützt.

## Akzeptanzkriterien

- **Gegeben** ein Benutzer mit Upload-Berechtigung &rarr; **Wenn** er ein Dokument hochlädt &rarr; **Dann** wird es versioniert, kategorisiert und für berechtigte Nutzer sichtbar.  

- **Gegeben** eine Vorlage &rarr; **Wenn** ein Dokument daraus generiert wird &rarr; **Dann** ersetzt das System automatisch alle Platzhalter und erstellt eine neue, archivierte Version.  

- **Gegeben** ein Vertrag mit definierter Laufzeit &rarr; **Wenn** die Kündigungsfrist erreicht wird &rarr; **Dann** werden die verantwortlichen Benutzer über das Benachrichtigungssystem informiert.  

- **Gegeben** ein Eigentümerkonto (WEG-58) &rarr; **Wenn** ein Kontoauszug generiert wird &rarr; **Dann** wird das Dokument im DMS archiviert und der Eigentümer erhält Zugriff.  

- **Gegeben** ein Finanz-Onboarding-Prozess (WEG-59) &rarr; **Wenn** dieser abgeschlossen wird &rarr; **Dann** erzeugt das System automatisch ein Prüfprotokoll und speichert es revisionssicher.  

- **Gegeben** eine archivierte Periode &rarr; **Wenn** ein Benutzer versucht, ein gesperrtes Dokument zu bearbeiten &rarr; **Dann** wird die Aktion blockiert und im Audit-Log vermerkt.

## Nicht-Ziele

- Keine gleichzeitige Bearbeitung von Dokumenten (keine Echtzeit-Kollaboration).

- Keine Integration mit externen Cloud-Diensten (z. B. Google Drive, SharePoint) im MVP.

- Keine automatische Texterkennung (OCR) oder KI-gestützte Klassifikation im MVP.

- Kein Workflow-Editor für Genehmigungsprozesse (nur vordefinierte Abläufe).

## Kritische Fälle

- **Berechtigungsfehler:** Dokumente dürfen niemals von unberechtigten Benutzern geöffnet oder gelöscht werden.

- **Versionskonflikte:** Gleichzeitige Änderungen erzeugen neue Versionen, die manuell geprüft werden müssen.

- **Fehlerhafte Vorlagen:** Template-Fehler müssen erkannt und durch Standardvorlagen ersetzt werden.

- **Speicherlimits:** Große Uploads können den Speicher belasten; Monitoring und automatische Archivierung sind erforderlich.

- **Fehlerhafte Finanzdokumente:** Unvollständige Kontoauszüge oder Reports dürfen nicht veröffentlicht werden; es muss ein Validierungsprozess stattfinden.

## Abhängigkeiten

- WEG-2 – Identity & Access (Auth, RBAC, Invitations): Rollen- und Berechtigungslogik.

- WEG-6 – In-App Messaging & Notifications: Benachrichtigungen bei Fristen, Genehmigungen und Statusänderungen.

- WEG-24 – Audit Log (User/Roles/Settings): Dokumentation aller Aktionen.

- WEG-12 – Error Handling, Logging & Health: Scheduler für Fristen und automatische Dokumentenerzeugung.

- WEG-87 – Accounting & Billing (Service Charges, Allocation, Budget/WP): Nutzung von Templates für Finanzberichte und Abrechnungen.

- WEG-58 – Owner Ledger & Balances (Accounts Receivable): Bereitstellung von Kontoauszügen und Abrechnungsnachweisen.

- WEG-59 – Financial Onboarding & Initialization: Integration von Onboarding-Berichten und Import-Protokollen.

## Offene Fragen

- Welche maximale Dateigröße soll pro Upload im MVP erlaubt sein?

- Sollen PDF-Dokumente mit digitalen Signaturen versehen werden können?

- Wie lange müssen archivierte Dokumente gemäß DSGVO aufbewahrt werden?

- Soll es ein Standard-Template-Set geben, das für alle WEGs bereitgestellt wird?

- Sollen Kontoauszüge (WEG-58) automatisch mit den Bankdaten synchronisiert werden?

## Zukunftserweiterungen

- **Kollaborative Dokumentenbearbeitung:** Echtzeit-Kommentierung und Änderungsverfolgung.

- **OCR-Integration:** Texterkennung und automatische Kategorisierung eingescannter Dokumente.

- **Digitale Signaturintegration:** Anbindung an E-Signatur-Dienste (z. B. DocuSign, Adobe Sign).

- **Externe Cloud-Anbindung:** Synchronisation mit Cloud-Speichern.

- **Automatische Indexierung:** Volltextindizierung aller archivierten PDF- und Finanzdokumente.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Kern-DMS mit Upload, Versionierung, rollenbasiertem Zugriff, Templates, Audit-Protokollierung, Vertragsüberwachung, Finanzdokumentintegration (WEG-58/59) und Retention.

**Phase 2**

Erweiterte Suche, OCR-Integration, kollaborative Workflows, SEPA-Dokumente, erweiterte Fristenlogik und automatische Finanzberichte.

**Phase 3**

Externe DMS- und Cloud-Anbindungen, digitale Signaturen, KI-gestützte Dokumentenklassifikation und dynamische Finanzreport-Erstellung.