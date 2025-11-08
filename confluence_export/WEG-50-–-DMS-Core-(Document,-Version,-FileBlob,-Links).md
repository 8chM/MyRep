---
title: WEG-50 – DMS Core (Document, Version, FileBlob, Links)
confluence_id: 27329313
version: 12
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329313/WEG-50+DMS+Core+Document+Version+FileBlob+Links
---

**JIRA-Link:** [WEG-50 – DMS Core (Document, Version, FileBlob, Links)](https://maierharry.atlassian.net/browse/WEG-50)

## Überblick

Das Modul **DMS Core** (WEG-50) bildet die zentrale Grundlage für das gesamte Dokumentenmanagement im WEG Management System.

Es stellt Kernfunktionen für das Hochladen, Speichern, Versionieren und Verknüpfen von Dokumenten bereit und ermöglicht die Integration von Dateien in nahezu alle Geschäftsprozesse — von Eigentümerversammlungen über Finanzberichte bis hin zu Verträgen und Mitteilungen.

Ziel ist es, eine sichere, nachvollziehbare und skalierbare Dokumentenbasis zu schaffen, die die rechtlichen und organisatorischen Anforderungen einer WEG-Verwaltung erfüllt.

## Beschreibung

Das Modul implementiert eine robuste und erweiterbare Dokumentenarchitektur, die Metadatenmanagement, Dateiversionierung und Verknüpfungen mit Objekten (z. B. Gebäude, Einheiten, Verträge) kombiniert.

Dokumente werden in einem File-Blob-Storage (lokal oder Cloud) gespeichert, während ihre Metadaten in der Datenbank verwaltet werden.

Jede Aktion (Upload, Änderung, Löschung, Download) wird revisionssicher im Audit-Log (WEG-24) protokolliert.

Hauptfunktionen:

- **Metadatenverwaltung:** Speicherung von Titel, Kategorie, MIME-Typ, Dateigröße, Ersteller, Upload-Datum, Version und Verknüpfung.

- **Dateispeicherung:** Ablage von Dateien im File-System oder in einem konfigurierbaren Blob-Storage (lokal oder Cloud).

- **Versionierung:** Jede Änderung an Metadaten oder Dateien erzeugt automatisch eine neue Version.

- **Entitätsverknüpfung:** Dokumente können direkt mit WEG-Objekten (z. B. Eigentümer, Gebäude, Verträge) verknüpft werden.

- **Validierung:** Uploads werden auf Typ, Größe und Malware geprüft (via WEG-55).

- **Berechtigungen (RBAC):** Zugriff auf Dokumente erfolgt ausschließlich über die rollenbasierte Zugriffskontrolle (WEG-2).

- **Audit-Protokollierung:** Jede Aktion wird mit Zeitstempel, Benutzer und Ereignistyp dokumentiert.

## Geschäftsregeln & Logik

- Jedes Dokument besitzt eine eindeutige GUID und eine fortlaufende Versionierung.

- Metadaten dürfen nur durch berechtigte Benutzer:innen (gemäß RBAC) bearbeitet werden.

- Die Validierungspipeline blockiert Uploads bei fehlerhaften Dateiformaten oder Malware.

- Änderungen oder Löschungen dürfen nur in offenen Bearbeitungsfenstern erfolgen.

- Dokumente sind revisionssicher; ältere Versionen bleiben erhalten und abrufbar.

## Akzeptanzkriterien

- **Gegeben** ein Benutzer lädt ein gültiges Dokument hoch &rarr; **Wenn** der Upload abgeschlossen wird &rarr; **Dann** wird das Dokument im Blob-Storage gespeichert und ein Eintrag in der Datenbank erstellt.

- **Gegeben** eine Datei mit unerlaubtem Typ oder Virenbefund &rarr; **Wenn** der Upload validiert wird &rarr; **Dann** wird der Vorgang blockiert und ein Fehler im Audit-Log erfasst.

- **Gegeben** eine Änderung an Dokumentmetadaten &rarr; **Wenn** diese gespeichert wird &rarr; **Dann** erzeugt das System automatisch eine neue Version mit referenziertem Zeitstempel.

- **Gegeben** ein Benutzer ohne Berechtigung &rarr; **Wenn** er versucht, ein Dokument zu öffnen &rarr; **Dann** wird der Zugriff verweigert und der Versuch im Audit-Log dokumentiert.

- **Gegeben** ein Dokument ist mit einem WEG-Objekt verknüpft &rarr; **Wenn** das Objekt gelöscht wird &rarr; **Dann** bleibt die Dokumentversion archiviert und die Verknüpfung wird als &bdquo;verwaist&ldquo; markiert.

## Nicht-Ziele

- Kein kollaboratives Dokumenten-Editing im MVP.

- Keine Echtzeit-Synchronisierung mit externen Cloud-Diensten (z. B. OneDrive, Google Drive).

- Keine automatische OCR-Erkennung oder Volltextsuche im MVP.

## Kritische Fälle

- **Fehlerhafte Uploads:** Abbruch bei Speicherproblemen oder unvollständigen Übertragungen.

- **Versionskonflikte:** Gleichzeitige Änderungen durch mehrere Benutzer:innen müssen blockiert werden.

- **Verlust von Referenzen:** Gelöschte Objekte dürfen keine inkonsistenten Dokumentverknüpfungen erzeugen.

## Abhängigkeiten

-  – Verwaltung der RBAC-Rollen für Dokumentzugriffe.

-  – Protokollierung aller Dateiaktionen (Upload, Versionierung, Löschung).

-  – Sicherheitsprüfung bei Uploads.

-  – Einheitliche Marken- und Layoutvorgaben bei exportierten Dokumenten.

-  – Zentrale Fehler- und Statusmeldungen.

## Offene Fragen

- Soll der Dokumentenspeicher im MVP lokal oder bereits Cloud-fähig umgesetzt werden?

- Sollen Versionen manuell wiederhergestellt oder nur lesend eingesehen werden können?

- Ist eine automatische Löschroutine für alte Versionen gewünscht (Retention)?

## Zukunftserweiterungen

- **Cloud Storage-Integration:** Unterstützung für Amazon S3, Azure Blob oder Google Cloud Storage.

- **Verschlüsselung ruhender Daten:** Implementierung von &bdquo;Encryption at Rest&ldquo; für erhöhte Datensicherheit.

- **Automatische Klassifizierung:** Tagging-System basierend auf Dokumentinhalt und Metadaten.

- **Volltextsuche und OCR:** Erweiterte Suchfunktionen und Inhaltsanalyse.

## Verknüpfte Tasks

- [WEG-500 – Upload, Versioning & Links](https://maierharry.atlassian.net/browse/WEG-500) – Grundimplementierung für Uploads, Versionierung und Entitätsverknüpfung.

- [WEG-501 – FileBlob Storage Adapter (local)](https://maierharry.atlassian.net/browse/WEG-501) – Adapter für lokale Dateispeicherung im MVP.

- [WEG-502 – Metadata Management & Version Control](https://maierharry.atlassian.net/browse/WEG-502) – Verwaltung von Versionen und Metadatenänderungen.

- [WEG-503 – Validation Pipeline & Virus Scan Integration](https://maierharry.atlassian.net/browse/WEG-503) – Prüfmechanismen bei Uploads.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Upload, Versionierung, Metadatenverwaltung, Verknüpfung mit WEG-Objekten, Audit-Logging und Virenprüfung (lokal).

**Phase 2**

Erweiterte Speicheradapter (S3/Azure), Verschlüsselung ruhender Daten, Wiederherstellungsfunktionen.

**Phase 3**

Volltextsuche, KI-basierte Dokumentklassifizierung, automatische Archivierung und Cloud-native DMS-Integration.