---
title: WEG-22 – Invitations & Password Reset (Link/QR, no Email)
confluence_id: 27460027
version: 21
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27460027/WEG-22+Invitations+Password+Reset+Link+QR+no+Email
---

**JIRA-Link:** [WEG-22 – Invitations & Password Reset (Link/QR, no Email)](https://maierharry.atlassian.net/browse/WEG-22)

## Überblick
Das Modul **Invitations & Password Reset** (WEG-22) ermöglicht den sicheren Benutzer-Onboarding- und Passwort-Zurücksetzungsprozess **ohne E-Mail-Infrastruktur**.  

Einladungen und Passwort-Reset-Links werden über **direkte URLs oder QR-Codes** bereitgestellt, die zeitlich begrenzt, einmalig gültig und revisionssicher verwaltet werden.  

Ziel ist es, eine DSGVO-konforme, flexible und vollständig auditierbare Benutzeraktivierung zu gewährleisten, auch in Umgebungen ohne E-Mail-Kommunikation.

## Beschreibung
WEG-22 deckt die gesamte Logik rund um Benutzeraktivierung, Passwort-Initialisierung und Zurücksetzung ab.  

Die Architektur basiert auf einem sicheren Token-Mechanismus, bei dem Tokens gehasht gespeichert, nur einmal verwendbar und nach Ablauf automatisch gelöscht werden.  

Diese Lösung ist besonders für vor-Ort- oder papierbasierte Onboarding-Prozesse geeignet und ersetzt klassische E-Mail-basierte Registrierungen.

Hauptfunktionen:

- **Einladungen (Invitation Tokens):** Manager oder Administratoren generieren Einladungs-Links oder QR-Codes, die einem neuen Benutzer zugeordnet werden. Nach Aufruf kann der Benutzer sein initiales Passwort setzen und die Nutzungsbedingungen akzeptieren.  

- **Passwort-Zurücksetzung (Reset Tokens):** Passwort-Resets verwenden dieselbe Token-Logik. Bei Nutzung wird das alte Passwort deaktiviert, alle aktiven Sessions werden beendet, und der Benutzer legt ein neues Passwort fest.  

- **QR-Unterstützung:** Für Präsenz-Onboarding (z. B. in WEG-Versammlungen) können QR-Codes mit begrenzter Gültigkeit erzeugt werden.  

- **Token-Sicherheit:** Tokens werden **gehasht** gespeichert (kein Klartext), sind an Benutzer gebunden, verfallen automatisch nach definierter Zeit (via WEG-25) und sind nach einmaliger Nutzung ungültig.  

- **Audit-Trail:** Jeder Token-Vorgang (Erstellung, Verwendung, Ablauf, Fehlversuch) wird in WEG-24 protokolliert.  

## Geschäftsregeln & Logik
- Tokens sind **einmalig** gültig und verfallen nach Ablaufzeit.  

- Einladungen dürfen ausschließlich von Rollen mit Berechtigung (manager.invite) erstellt werden.  

- Ablaufzeiten, Fehlversuchslimits und maximale Token-Anzahl pro Benutzer werden über **WEG-25 – Security Settings** konfiguriert.  

- Nach Einlösung eines Reset-Tokens werden alle aktiven Sessions des Benutzers automatisch beendet.  

- QR-Codes enthalten keine sensiblen Daten, sondern nur die Token-ID mit Prüfsumme.  

- Jeder Token besitzt eine eindeutige Audit-ID für Nachvollziehbarkeit.  

## Akzeptanzkriterien
- **Gegeben** ein Invitation-Token ist aktiv &rarr; **Wenn** ein neuer Benutzer den Link aufruft &rarr; **Dann** kann er sein Passwort setzen und der Account wird aktiviert.  

- **Gegeben** ein Reset-Token ist gültig &rarr; **Wenn** der Benutzer es nutzt &rarr; **Dann** werden alle aktiven Sessions beendet und das neue Passwort gespeichert.  

- **Gegeben** derselbe Token wird erneut genutzt &rarr; **Wenn** der zweite Aufruf erfolgt &rarr; **Dann** wird der Zugriff verweigert und im Audit-Log dokumentiert.  

- **Gegeben** ein Token ist abgelaufen &rarr; **Wenn** der Benutzer versucht, es zu verwenden &rarr; **Dann** erhält er eine Fehlermeldung und der Administrator kann einen neuen Token generieren.  

- **Gegeben** ein Administrator erstellt eine Einladung &rarr; **Wenn** die Token-Erstellung erfolgreich ist &rarr; **Dann** wird ein Audit-Eintrag mit Ersteller, Ziel und Ablaufzeit erzeugt.  

## Nicht-Ziele
- Keine E-Mail- oder SMS-Zustellung im MVP.  

- Keine Integration mit externen Identity-Providern.  

- Kein automatischer Import externer Benutzerlisten.  

- Keine Self-Service-Registrierung ohne Einladung.  

## Kritische Fälle
- **Mehrfachnutzung:** Tokens dürfen nur einmal gültig sein; erneute Nutzung muss verweigert und protokolliert werden.  

- **Abgelaufene Tokens:** Abgelaufene Tokens dürfen keinen Zugriff ermöglichen und müssen inaktive Status erhalten.  

- **Token-Verlust:** Verlust eines Tokens darf keine Sicherheitslücke darstellen – nur autorisierte Administratoren dürfen Ersatz-Tokens erstellen.  

- **Ungültige QR-Links:** QR-Codes müssen serverseitig validiert werden, bevor sie eingelöst werden können.  

## Abhängigkeiten
- WEG-2 – Identity & Access – Grundlage für Benutzerverwaltung und Passwort-Authentifizierung.  

- WEG-24 – Audit Log – Dokumentiert alle Token-bezogenen Aktionen (Erstellung, Nutzung, Ablauf).  

- WEG-25 – Security Settings – Steuert Ablaufzeiten, Fehlversuche und Token-Limits.  

- WEG-5 – Document Management – Integration von Nutzungsbedingungen oder Policy-Dokumenten in den Aktivierungsprozess.  

- WEG-21 – RBAC Roles & Policies per Association – Legt fest, welche Rollen Einladungen erstellen oder Tokens zurücksetzen dürfen.  

## Offene Fragen
- Soll die Annahme von AGB oder Datenschutzrichtlinien verpflichtend sein, bevor der Account aktiviert wird?  

- Wie lange sollen QR-Codes gültig sein (z. B. 24 h, 7 Tage)?  

- Soll das System automatisch ungültige Tokens bereinigen oder manuell durch Administratoren?  

## Zukunftserweiterungen
- Versand von Tokens über E-Mail oder SMS.  

- Bulk-Invites für mehrere Eigentümer gleichzeitig.  

- Delegierte Einladungen durch Beiratsmitglieder.  

- Temporäre Gastzugänge für Dienstleister.  

- Integration in Mobile-App-Flows für Onboarding per QR-Scan.  

## Verknüpfte Tasks
- [WEG-220 – Invitation Link Generation](https://maierharry.atlassian.net/browse/WEG-220) – Generiert einmalige Aktivierungslinks mit Ablaufdatum.  

- [WEG-221 – Password Reset Link Generation](https://maierharry.atlassian.net/browse/WEG-221) – Erstellt sichere Reset-Tokens und verwaltet Gültigkeit.  

- [WEG-222 – Token Storage (hashed) & Expiry](https://maierharry.atlassian.net/browse/WEG-222) – Implementiert Speicherung, Ablaufsteuerung und Löschung abgelaufener Tokens.  

- [WEG-223 – QR Export](https://maierharry.atlassian.net/browse/WEG-223) – Generiert QR-Codes für Vor-Ort-Registrierungen.  

- [WEG-224 – Audit for Invitations/Resets](https://maierharry.atlassian.net/browse/WEG-224) – Protokolliert alle Token-bezogenen Aktivitäten im Audit-Log.  

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Token-basierte Einladung und Passwort-Zurücksetzung über Links oder QR, gehashte Speicherung, Ablaufverwaltung, Audit-Logging.

**Phase 2**

Versand über E-Mail/SMS, Bulk-Invites, Delegated Invites und konfigurierbare Ablaufzeiten.

**Phase 3**

Integration in Mobile-App, temporäre Gastzugänge, automatische Token-Bereinigung und DSGVO-konforme Löschprozesse.