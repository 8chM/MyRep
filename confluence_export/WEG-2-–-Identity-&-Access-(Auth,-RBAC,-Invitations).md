---
title: WEG-2 – Identity & Access (Auth, RBAC, Invitations)
confluence_id: 27460012
version: 12
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27460012/WEG-2+Identity+Access+Auth+RBAC+Invitations
---

**JIRA-Link:** [WEG-2 – Identity & Access (Auth, RBAC, Invitations)](https://maierharry.atlassian.net/browse/WEG-2)

## Beschreibung / Kernzweck

Das Modul **WEG-2 – Identity & Access** regelt die zentrale Benutzerverwaltung, Authentifizierung und Rechtevergabe im WEG Management System (WMS). Es stellt sicher, dass jede Aktion im System eindeutig einem Benutzer zugeordnet werden kann und dass Zugriffe ausschließlich gemäß definierter Rollen und Berechtigungen erfolgen. Ziel ist eine sichere, transparente und datenschutzkonforme Verwaltung von Identitäten und Zugriffsrechten über alle WEGs hinweg.

Das Modul sorgt dafür, dass Benutzer (Verwalter, Beiräte, Eigentümer und Dienstleister) nur die Daten sehen und bearbeiten können, die ihrer Rolle und jeweiligen WEG zugeordnet sind. Neben Authentifizierung und Autorisierung implementiert WEG-2 auch Datenschutz- und Audit-Funktionen, die gesetzliche Vorgaben wie die DSGVO erfüllen.

## Inhalte

Untermodul

Kurzbeschreibung

[WEG-20 – Authentication (ASP.NET Identity + JWT/Cookie)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Verwaltet Benutzeranmeldung, Sitzungen, Tokens und Passwortregeln.

[WEG-21 – RBAC Roles & Policies per Association](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Definiert rollenbasierte Zugriffskontrollen für jede WEG und regelt Berechtigungen.

[WEG-22 – Invitations & Password Reset (Link/QR, no Email)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Ermöglicht sichere Benutzerregistrierung über Einladungen oder QR-Codes sowie Passwortzurücksetzung ohne E-Mail.

[WEG-23 – Profile & Association Switcher](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Bietet eine Profilverwaltung und erlaubt Benutzern, zwischen mehreren WEGs zu wechseln.

[WEG-24 – Audit Log (User/Roles/Settings)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Protokolliert sicherheitsrelevante Ereignisse wie Logins, Rollenänderungen oder Datenschutzaktionen.

[WEG-25 – Security Settings (MVP relaxed)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Legt grundlegende Sicherheitsrichtlinien (z. B. Passwortlänge, Sitzungsdauer, Rate Limits) fest.

[WEG-26 – Data Privacy & Redaction (GDPR Base)](https://maierharry.atlassian.net/wiki/pages/PLACEHOLDER)

Stellt Datenschutzfunktionen bereit, wie Datenexport, Redaktions- und Löschprozesse nach DSGVO.

## Geschäftslogik

WEG-2 stellt sicher, dass jeder Benutzer eindeutig authentifiziert wird und ausschließlich die ihm zugewiesenen Bereiche des Systems nutzen darf.

- **Benutzerverwaltung:** Alle Benutzerkonten werden zentral verwaltet. Die Identität basiert auf ASP.NET Identity mit Unterstützung für JWT-Token und Cookie-Authentifizierung.

- **Rollen- und Rechtekonzept:** Zugriff auf Funktionen und Daten erfolgt über ein fein granular konfigurierbares RBAC-System (Role-Based Access Control). Rollen wie *Verwalter*, *Beirat*, *Eigentümer* oder *Dienstleister* bestimmen, welche Aktionen in welcher WEG erlaubt sind.

- **Mehrmandantenfähigkeit:** Benutzer können mehreren WEGs zugeordnet sein. Der Mandantenwechsel erfolgt über das Profilmenü, wobei pro WEG unterschiedliche Berechtigungen gelten.

- **Einladungsmanagement:** Neue Benutzer werden über sichere Einladungs- oder QR-Codes hinzugefügt, ohne dass direkte E-Mail-Kommunikation erforderlich ist.

- **Auditierbarkeit:** Alle Änderungen an Benutzer- oder Rollendaten werden im Audit Log (WEG-24) mit Zeitstempel und Verantwortlichem erfasst.

- **Datenschutz:** Das System erfüllt die DSGVO-Basisanforderungen. Über WEG-26 können personenbezogene Daten pseudonymisiert, exportiert oder gelöscht werden.

- **Sicherheitsrichtlinien:** Grundlegende Mechanismen wie Passwortregeln, Rate Limits und Session Timeouts sorgen für Basisschutz gegen Missbrauch.

## Akzeptanzkriterien

- **Gegeben** ein Benutzer mit gültigen Zugangsdaten &rarr; **Wenn** er sich anmeldet &rarr; **Dann** erhält er Zugriff auf die ihm zugeordneten WEGs und Rollen.  

- **Gegeben** ein Benutzer hat mehrere WEG-Mitgliedschaften &rarr; **Wenn** er den Mandanten wechselt &rarr; **Dann** werden dessen spezifische Rechte sofort übernommen.  

- **Gegeben** ein Benutzer wird deaktiviert &rarr; **Wenn** er versucht, sich anzumelden &rarr; **Dann** wird der Zugriff verweigert und der Vorgang protokolliert.  

- **Gegeben** eine Rollenänderung wird vorgenommen &rarr; **Wenn** diese gespeichert wird &rarr; **Dann** sind die neuen Berechtigungen unmittelbar aktiv.  

- **Gegeben** eine Datenschutzanfrage (DSAR) &rarr; **Wenn** ein Export ausgeführt wird &rarr; **Dann** enthält dieser alle personenbezogenen Daten des Benutzers.  

- **Gegeben** ein Passwort wird zurückgesetzt &rarr; **Wenn** der Benutzer sich neu anmeldet &rarr; **Dann** wird er zur Änderung des Passworts aufgefordert.

## Nicht-Ziele

- Kein externer Login (z. B. Google, Apple, Microsoft) im MVP.

- Keine Integration externer SSO-Systeme.

- Keine erweiterte Sicherheitszertifizierung (z. B. ISO 27001) im MVP.

- Kein rollenbasierter Workflow für Genehmigungen – folgt in späteren Phasen.

## Kritische Fälle

- **Rollenfehler:** Ungültige oder doppelte Rollenzuweisungen dürfen nicht gespeichert werden.

- **Inaktive Benutzer:** Müssen automatisch nach festgelegtem Zeitraum gesperrt werden.

- **Audit-Lücken:** Unprotokollierte Änderungen an Benutzerrechten gefährden die Nachvollziehbarkeit.

- **Fehlerhafte DSGVO-Prozesse:** Ungenaue oder unvollständige Datenexports führen zu Compliance-Verstößen.

## Abhängigkeiten

- WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite): nutzt Infrastruktur, Logging und Scheduler.

- WEG-24 – Audit Log (User/Roles/Settings): erfasst Änderungen an Benutzern und Rollen.

- WEG-26 – Data Privacy & Redaction (GDPR Base): stellt DSGVO-Funktionen bereit.

- WEG-3 – Tenant Provisioning & Admin: verwaltet Mandanten und ihre Zuordnung zu Benutzern.

## Offene Fragen

- Soll Zwei-Faktor-Authentifizierung (2FA) ab Phase 2 verpflichtend oder optional werden?

- Sollen Benutzerrechte künftig importiert/exportiert werden können (z. B. aus CSV)?

- Wird ein zentraler Passwort-Reset durch Administratoren erlaubt sein?

- Wie lange sollen Audit-Einträge für Sicherheitsereignisse gespeichert werden?

## Zukunftserweiterungen

- **Zwei-Faktor-Authentifizierung (2FA):** Optionales Sicherheitsverfahren für sensible Aktionen.

- **SSO-Integration:** Einbindung externer Identitätsanbieter (Azure AD, Keycloak).

- **Dynamische Rollenmodelle:** Anpassbare Rollen und Berechtigungssets pro WEG.

- **Anmeldeanalyse:** Statistiken über Login-Versuche, Fehler und Inaktivität.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Benutzerverwaltung, Authentifizierung, RBAC-Rollenmodell, Einladungsmanagement, Audit-Logging, Datenschutzgrundfunktionen.

**Phase 2**

Zwei-Faktor-Authentifizierung, SSO-Integration, erweiterte Datenschutzfunktionen und zentrale Passwort-Policies.

**Phase 3**

Automatische Rechteprüfung per KI, dynamische Rollenzuweisung basierend auf Verhalten, Compliance-Berichte und zentrale Zugriffsüberwachung.