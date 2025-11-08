---
title: WEG-25 – Security Settings (MVP relaxed)
confluence_id: 27722219
version: 19
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722219/WEG-25+Security+Settings+MVP+relaxed
---

**JIRA-Link:** [WEG-25 – Security Settings (MVP relaxed)](https://maierharry.atlassian.net/browse/WEG-25)

## Überblick

Das Modul **Security Settings** (WEG-25) definiert die konfigurierbaren Sicherheitsparameter pro Association.  

Es bildet die Grundlage für Authentifizierungs- und Zugriffssicherheit und sorgt im MVP für ein ausgewogenes Verhältnis zwischen Benutzerfreundlichkeit und Basisschutz.  

Langfristig ermöglicht es die Einführung erweiterter Sicherheitsrichtlinien, adaptiver Zugriffskontrollen und Compliance-Funktionen.

## Beschreibung

WEG-25 stellt sicher, dass alle sicherheitsrelevanten Rahmenbedingungen – wie Passwortkomplexität, Session-Dauer, Fehlversuchsschwellen und Anmelderaten – mandantenspezifisch gesteuert werden können.  

Das Modul integriert sich eng in die Authentifizierungslogik (WEG-20) und dokumentiert alle Änderungen revisionssicher im Audit-Log (WEG-24).

Hauptfunktionen:

- **Passwort-Politik:** Festlegung von Mindestlänge, Komplexität (Groß-/Kleinbuchstaben, Sonderzeichen, Ziffern) und optionaler Ablaufzeit.  

- **Session & Token Timeouts:** Steuerung der Lebensdauer von Login-Sitzungen und API-Tokens, getrennt nach Rollen oder Geräten.  

- **Lockout & Rate-Limits:** Definition von Fehlversuchsgrenzen (z. B. 5 fehlerhafte Logins) sowie Begrenzung der Authentifizierungsfrequenz.  

- **Policy-Pakete:** Vordefinierte Sicherheitsstufen (&bdquo;Relaxed&ldquo;, &bdquo;Standard&ldquo;, &bdquo;Strict&ldquo;) ermöglichen einfache Konfiguration ohne technische Vorkenntnisse.  

- **Auditierbarkeit:** Jede Änderung von Sicherheitsparametern wird automatisch im Audit-Log dokumentiert.  

- **Role-Aware Defaults:** Strengere Standardrichtlinien gelten automatisch für Systemadministratoren und privilegierte Benutzer.  

## Geschäftsregeln & Logik

- Sicherheitsrichtlinien gelten mandantenspezifisch; Änderungen wirken sich nur auf nachfolgende Logins oder Token-Erstellungen aus.  

- Administratoren können Richtlinien anpassen, jedoch nicht unterhalb definierter Mindeststandards.  

- Lockout-Schwellen verhindern Brute-Force-Angriffe; Sperrungen werden automatisch nach Ablauf einer definierten Zeit aufgehoben.  

- Änderungen an Policies werden sofort aktiv, erfordern aber keine Systemneustarts.  

- Alle Sicherheitsparameter werden zentral validiert, bevor sie gespeichert werden.  

## Akzeptanzkriterien

- **Gegeben** eine neue Passwortlänge wird definiert &rarr; **Wenn** die Änderung gespeichert wird &rarr; **Dann** müssen alle zukünftigen Passwörter die neue Mindestlänge erfüllen.  

- **Gegeben** ein Administrator erhöht die Session-Timeout-Dauer &rarr; **Wenn** diese gespeichert wird &rarr; **Dann** gelten neu erstellte Sessions mit der neuen Gültigkeitsdauer.  

- **Gegeben** ein Benutzer überschreitet den Lockout-Threshold &rarr; **Wenn** der Schwellenwert erreicht ist &rarr; **Dann** wird sein Konto temporär gesperrt und ein Audit-Eintrag erzeugt.  

- **Gegeben** zu viele Anfragen werden an den Authentifizierungs-Endpunkt gesendet &rarr; **Wenn** das Rate-Limit überschritten wird &rarr; **Dann** wird der Zugriff blockiert und der Vorfall im Audit-Log protokolliert.  

- **Gegeben** ein Administrator aktiviert eine &bdquo;Strict&ldquo;-Policy &rarr; **Wenn** sie übernommen wird &rarr; **Dann** werden automatisch alle niedrigeren Richtlinienparameter angehoben.  

## Nicht-Ziele

- Keine globalen Sicherheitsrichtlinien über alle Mandanten hinweg.  

- Keine MFA- oder Conditional-Access-Regeln im MVP.  

- Kein Self-Service zur Anpassung von Sicherheitsparametern durch Endnutzer.  

## Kritische Fälle

- **Zu strenge Einstellungen:** Übermäßig restriktive Policies können Benutzer sperren; das System warnt Administratoren vor Risiken.  

- **Fehlkonfiguration:** Ungültige Timeout-Werte können zu unerwartetem Logout-Verhalten führen.  

- **Unsichere Defaults:** Zu schwache Relaxed-Profile müssen regelmäßig überprüft und aktualisiert werden.  

## Abhängigkeiten

-  – Verwendet die hier definierten Richtlinien.  

-  – Regelt differenzierte Berechtigungsprüfungen für sicherheitskritische Aktionen.  

-  – Erfasst Änderungen an Sicherheitsparametern.  

-  – Greift auf Sicherheitseinstellungen zu, um Lösch- und Redaktionsregeln zu schützen.  

## Offene Fragen

- Sollen Passwortablaufzeiten bereits im MVP implementiert werden?  

- Wird eine Benachrichtigung bei Sperrung eines Benutzerkontos benötigt (z. B. über WEG-6)?  

- Soll es eine Wiederherstellungsoption bei Lockouts für Administratoren geben?  

## Zukunftserweiterungen

- **Organisation-weite Sicherheitsrichtlinien:** Globale Policies über alle Mandanten hinweg.  

- **Conditional Access:** Zugriffsbeschränkungen auf Basis von IP- oder Gerätestandorten.  

- **Adaptive Security Profiles:** Dynamische Anpassung der Policy-Stufe anhand des Benutzerverhaltens.  

- **Security Analytics:** Berichtsfunktion zur Auswertung von Anmeldeversuchen, Sperrungen und Policy-Verstößen.  

## Verknüpfte Tasks

- [WEG-250 – Password Policy Config (relaxed MVP)](https://maierharry.atlassian.net/browse/WEG-250) – Definiert Passwortanforderungen und Mindeststandards im MVP.  

- [WEG-251 – Basic Rate Limits (auth)](https://maierharry.atlassian.net/browse/WEG-251) – Implementiert grundlegende Authentifizierungsbegrenzungen und Fehlversuchszähler.  

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Passwortregeln, Session-Timeouts, Lockout-Schwellen, Rate-Limits, Audit-Logging, Policy-Pakete (Relaxed/Standard/Strict).

**Phase 2**

Organisation-weite Sicherheitsrichtlinien, Conditional Access, adaptive Sicherheitsprofile.

**Phase 3**

Erweiterte Analytics, Echtzeitwarnungen, KI-gestützte Risikoerkennung und Selbstheilungsmaßnahmen bei Sicherheitsanomalien.