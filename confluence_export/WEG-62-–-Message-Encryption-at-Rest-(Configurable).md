---
title: WEG-62 – Message Encryption at Rest (Configurable)
confluence_id: 27198007
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27198007/WEG-62+Message+Encryption+at+Rest+Configurable
---

**JIRA-Link:** [WEG-62 – Message Encryption at Rest (Configurable)](https://maierharry.atlassian.net/browse/WEG-62)

## Überblick

Das Modul **Message Encryption at Rest** (WEG-62) schützt gespeicherte Nachrichten und Anhänge vor unbefugtem Zugriff, selbst bei kompromittierter Infrastruktur. Es stellt sicher, dass alle gespeicherten Kommunikationsdaten verschlüsselt und nur über authentifizierte Zugriffe lesbar sind. Ziel ist es, die Vertraulichkeit sensibler Kommunikationsinhalte zu wahren und die Anforderungen der DSGVO an Datensicherheit technisch umzusetzen.

## Beschreibung

Dieses Modul implementiert eine konfigurierbare Verschlüsselungsschicht für alle Nachrichten und Anhänge im Messaging-System (WEG-6, WEG-61). Die Verschlüsselung erfolgt **tenant-spezifisch** mit individuellen Schlüsseln, um eine strikte Datenisolation zwischen verschiedenen WEGs zu gewährleisten.

**Hauptfunktionen:**

- **Tenant-spezifische Verschlüsselung:** Jeder Mandant (WEG) erhält einen eigenen AES-256-Schlüssel. Nachrichten und Anhänge werden mit diesem Schlüssel verschlüsselt, bevor sie in der Datenbank gespeichert werden.

- **Schlüsselverwaltung (Vault-System):** Alle Schlüssel werden in einem internen, sicheren Vault gespeichert. Schlüsselrotation ist jährlich oder manuell möglich.

- **Konfigurierbarkeit:** Im Dev-Modus kann die Verschlüsselung deaktiviert werden (&bdquo;passthrough&ldquo;) – ausschließlich zu Entwicklungszwecken, dokumentiert im Audit-Log.

- **Sichere Entschlüsselung:** Zugriff auf entschlüsselte Inhalte erfolgt ausschließlich über autorisierte API-Aufrufe; Benutzeroberflächen zeigen nur entschlüsselte Inhalte nach Authentifizierung.

- **Auditierung & Logging:** Jede Verschlüsselungs- und Entschlüsselungsoperation wird protokolliert. Sicherheitsrelevante Ereignisse wie Schlüsselrotationen werden im Audit-Log (WEG-24) dokumentiert.

## Geschäftsregeln & Logik

- **Mandanten-Trennung:** Jeder Mandant hat einen eigenen Schlüssel; Schlüssel dürfen nicht wiederverwendet oder geteilt werden.

- **Rotation:** Schlüsselrotation ist jährlich vorgesehen, kann jedoch manuell durch Administratoren angestoßen werden. Alte Schlüssel bleiben für die Entschlüsselung historischer Daten aktiv, bis diese archiviert oder gelöscht werden.

- **Zugriffskontrolle:** Entschlüsselung nur über authentifizierte Prozesse; direkte Datenbankzugriffe liefern nur verschlüsselten Text.

- **Dev-Modus:** Im Entwicklungsmodus ist die Verschlüsselung deaktivierbar; jede Verwendung dieses Modus wird im Audit protokolliert.

- **Audit-Pflicht:** Jeder Zugriff, jede Rotation und jede Entschlüsselung werden nachvollziehbar dokumentiert.

## Akzeptanzkriterien

- **Gegeben** eine Nachricht wird gespeichert &rarr; **Wenn** die Verschlüsselung aktiviert ist &rarr; **Dann** wird der Inhalt verschlüsselt gespeichert und ist nur über das System entschlüsselbar.

- **Gegeben** der Dev-Modus ist aktiv &rarr; **Wenn** eine Nachricht gespeichert wird &rarr; **Dann** erfolgt keine Verschlüsselung, und dieser Zustand wird im Audit-Log vermerkt.

- **Gegeben** eine Schlüsselrotation wird durchgeführt &rarr; **Wenn** die Rotation abgeschlossen ist &rarr; **Dann** bleiben bestehende Daten weiterhin lesbar, während neue Nachrichten mit dem neuen Schlüssel verschlüsselt werden.

- **Gegeben** ein Benutzer versucht, auf verschlüsselte Daten ohne gültige Authentifizierung zuzugreifen &rarr; **Wenn** der Zugriff erfolgt &rarr; **Dann** wird dieser abgewiesen und im Audit protokolliert.

- **Gegeben** ein Schlüssel wird deaktiviert &rarr; **Wenn** dieser für alte Daten erforderlich ist &rarr; **Dann** darf keine Entschlüsselung mehr erfolgen, bis ein Wiederherstellungsschlüssel verwendet wird.

## Nicht-Ziele

- Keine Ende-zu-Ende-Verschlüsselung zwischen Clients (nur Speicherung im Backend).

- Keine Integration externer Cloud-Key-Management-Systeme (KMS) im MVP.

- Keine temporären Zwischenspeicher von entschlüsselten Daten außerhalb des RAM.

## Kritische Fälle

- **Schlüsselverlust:** Verlust eines Mandantenschlüssels führt zu dauerhaftem Datenverlust; regelmäßige Backups sind verpflichtend.

- **Unbeabsichtigte Deaktivierung:** Dev-Modus darf nicht versehentlich in produktiven Instanzen aktiv sein.

- **Rotation während Schreibvorgängen:** Gleichzeitige Schreibvorgänge während einer Schlüsselrotation müssen blockiert oder in eine Warteschlange überführt werden.

## Abhängigkeiten

-  – Datenquelle der zu verschlüsselnden Inhalte.

-  – Verwaltung der Kommunikationsdaten.

-  – Protokolliert Verschlüsselungsoperationen und Rotationen.

-  – Definiert globale Sicherheitsparameter wie Schlüssellaufzeiten und Policy-Vorgaben.

-  – Gewährleistet DSGVO-Konformität bei Löschungen und Redaktionen.

## Offene Fragen

- Soll die Schlüsselrotation automatisiert (jährlich) oder ausschließlich manuell erfolgen?

- Wie werden verschlüsselte Backups gehandhabt, um im Notfall Wiederherstellung zu ermöglichen?

- Wird eine Schlüsselhierarchie (Master-Key &rarr; Tenant-Key) zur zusätzlichen Absicherung benötigt?

## Zukunftserweiterungen

- **Externes Key Management System (KMS):** Anbindung an Cloud-Dienste wie Azure Key Vault oder AWS KMS.

- **Ende-zu-Ende-Verschlüsselung:** Schutz der Daten auch während der Übertragung zwischen Clients.

- **Rotations-Dashboard:** Administratives Interface zur Überwachung und manuellen Steuerung von Schlüsselrotationen.

- **Zugriffsbenachrichtigungen:** Notifications bei unüblichen Zugriffen oder Rotationen.

## Verknüpfte Tasks

- [WEG-620 – Toggle: prod on, dev passthrough](https://maierharry.atlassian.net/browse/WEG-620) – Ermöglicht Umschaltung zwischen Produktiv- und Entwicklungsmodus mit Protokollierung im Audit-Log.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Tenant-basierte Verschlüsselung von Nachrichten und Anhängen mit konfigurierbarem Dev-Modus und Audit-Protokollierung.

**Phase 2**

Automatisierte Schlüsselrotation und optionale Integration eines externen KMS.

**Phase 3**

Ende-zu-Ende-Verschlüsselung, Zugriffsbenachrichtigungen und erweitertes Rotations-Dashboard.