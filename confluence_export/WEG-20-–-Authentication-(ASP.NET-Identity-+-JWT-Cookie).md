---
title: WEG-20 – Authentication (ASP.NET Identity + JWT/Cookie)
confluence_id: 27656607
version: 19
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27656607/WEG-20+Authentication+ASP.NET+Identity+JWT+Cookie
---

**JIRA-Link:** [WEG-20 – Authentication (ASP.NET Identity + JWT/Cookie)](https://maierharry.atlassian.net/browse/WEG-20)

## Überblick

Das Modul **Authentication** (WEG-20) stellt die zentrale Authentifizierungsschicht des WEG Management Systems bereit.  

Es ermöglicht die Anmeldung über Benutzername und Passwort, verwaltet Sitzungen für Web-Clients über Cookies und stellt JSON Web Tokens (JWT) für API-Zugriffe bereit.  

Ziel ist die sichere, skalierbare und nachvollziehbare Authentifizierung von Benutzern mit klarer Trennung zwischen Authentifizierung (AuthN) und Autorisierung (AuthZ).

## Beschreibung

WEG-20 implementiert die grundlegende Benutzeranmeldung, Sitzungsverwaltung und Token-basierte Sicherheit für das gesamte System.  

Das Modul nutzt **ASP.NET Identity** als Basis für die Verwaltung von Benutzern, Passwörtern und Anmeldeinformationen.  

Die Architektur trennt Web-Sessions (Cookies) und API-Tokens (JWT), um flexible Nutzung in Browsern und externen Anwendungen zu ermöglichen.

Hauptfunktionen:

- **Password-based Sign-In:** Benutzer melden sich mit Benutzername und Passwort an; die Passwort-Hashing-Richtlinien werden durch WEG-25 vorgegeben.  

- **Session-Cookies (Web):** Für Browser-Clients werden sichere Cookies gesetzt. Sie unterstützen Sign-Out über alle Geräte und automatische Invalidierung nach Passwortänderung.  

- **JWT für APIs:** Für API-Zugriffe werden signierte, kurzlebige JWTs ausgestellt, die Benutzer-ID, Rollen und optional Tenant-Information enthalten.  

- **Refresh-Token Rotation:** Jeder Refresh-Token kann nur einmal verwendet werden; neue Tokens werden automatisch generiert, alte ungültig gemacht.  

- **Lockout & Timeouts:** Fehlversuche führen zu temporären Sperren; Token- und Sessionlaufzeiten sind konfigurierbar und können je WEG variieren.  

- **Token Cleanup:** Hintergrundprozesse (über WEG-12 Scheduler) löschen abgelaufene Tokens und inaktive Sessions regelmäßig.  

## Geschäftsregeln & Logik

- Eine gültige Authentifizierung ist Voraussetzung für alle geschützten API-Endpunkte.  

- Tokens werden signiert und enthalten nur minimale Claims (UserID, Roles, Tenant).  

- Refresh-Tokens sind einmalig und werden bei jeder Nutzung rotiert.  

- Lockout- und Timeout-Richtlinien greifen global und mandantenspezifisch.  

- Passwortänderungen führen zum Widerruf aller aktiven Sessions und Tokens.  

- Jeder Login-, Logout- oder Token-Refresh-Vorgang wird im Audit-Log (WEG-24) dokumentiert.  

## Akzeptanzkriterien

- **Gegeben** ein Benutzer mit gültigen Credentials &rarr; **Wenn** er sich anmeldet &rarr; **Dann** erhält er ein Session-Cookie oder JWT.  

- **Gegeben** ein abgelaufenes JWT &rarr; **Wenn** ein gültiger Refresh-Token verwendet wird &rarr; **Dann** wird ein neues JWT ausgestellt.  

- **Gegeben** mehrere Fehlversuche &rarr; **Wenn** die Lockout-Schwelle erreicht wird &rarr; **Dann** wird das Konto temporär gesperrt und eine Audit-Meldung erzeugt.  

- **Gegeben** ein Passwort wird geändert &rarr; **Wenn** der Benutzer angemeldet ist &rarr; **Dann** werden alle bestehenden Tokens ungültig gemacht.  

- **Gegeben** ein Refresh-Token wird erneut verwendet &rarr; **Wenn** er bereits verbraucht wurde &rarr; **Dann** wird die Anfrage abgelehnt und der Benutzer muss sich neu anmelden.  

## Nicht-Ziele

- Keine Integration mit OAuth2 oder OpenID Connect im MVP.  

- Keine Multi-Factor Authentication (MFA/2FA) in Phase 

- Keine Gerätebindung oder Risikoanalyse im MVP.  

- Kein Single-Sign-On zwischen mehreren Systemen.  

## Kritische Fälle

- **Brute-Force Attacken:** Wiederholte Anmeldeversuche müssen durch Rate-Limits und Lockouts unterbunden werden.  

- **Token-Diebstahl:** Bei Verdacht auf Missbrauch müssen alle aktiven Tokens widerrufen werden.  

- **Session-Hijacking:** Cookies müssen HttpOnly, Secure und mit SameSite-Einschränkungen gesetzt werden.  

- **Race-Conditions:** Gleichzeitige Refresh-Token-Anfragen müssen verhindert oder sequentiell abgearbeitet werden.  

## Abhängigkeiten

-  – Bereitstellung der API- und Authentifizierungsinfrastruktur.  

-  – Standardisiertes Fehler-Logging bei Authentifizierungsvorgängen.  

-  – Autorisierung nach erfolgreicher Anmeldung.  

-  – Verwaltung von Passwort-Politik, Lockout-Schwellen und Timeouts.  

## Offene Fragen

- Welche Standard-Laufzeiten sollen für JWTs und Refresh-Tokens im MVP gelten?  

- Sollen parallele Sessions auf mehreren Geräten erlaubt sein, oder wird bei jeder Anmeldung die vorherige beendet?  

- Soll die Passwort-Zurücksetzung über Token oder durch Verwalter erfolgen?  

## Zukunftserweiterungen

- Unterstützung für **OAuth2/OpenID Connect**.  

- Einführung von **Multi-Factor Authentication (MFA)** mit TOTP oder WebAuthn.  

- Gerätebindung und adaptive Risikoanalyse.  

- **Single-Sign-On (SSO)** für verbundene Systeme.  

- Adaptive Session-Verwaltung mit Kontextanalyse (z. B. Ort, Gerät, IP-Adresse).  

## Verknüpfte Tasks

- [WEG-200 – Authentication Endpoints (login/refresh/logout)](https://maierharry.atlassian.net/browse/WEG-200) – Implementiert Authentifizierungsendpunkte.  

- [WEG-201 – Password Hashing & Policies](https://maierharry.atlassian.net/browse/WEG-201) – Definiert Hashing-Verfahren und Passwortregeln.  

- [WEG-202 – Lockout & Rate Limiting](https://maierharry.atlassian.net/browse/WEG-202) – Implementiert Schutzmechanismen gegen Brute-Force-Angriffe.  

- [WEG-203 – Session & Token Timeouts](https://maierharry.atlassian.net/browse/WEG-203) – Konfiguriert Ablaufzeiten für Tokens und Sessions.  

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Authentifizierung über Benutzername und Passwort, Session-Cookies für Web, JWT für APIs, Refresh-Token-Rotation, Lockout-Mechanismen, Token-Cleanup.

**Phase 2**

Einführung von MFA/2FA (TOTP, WebAuthn), Gerätebindung, risikobasierte Authentifizierung.

**Phase 3**

Single-Sign-On (OIDC/SAML), adaptive Sessions, Integration mit externen Identity-Providern.