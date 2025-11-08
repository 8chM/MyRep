---
title: WEG-23 – Profile & Association Switcher
confluence_id: 27853447
version: 19
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27853447/WEG-23+Profile+Association+Switcher
---

**JIRA-Link:** [WEG-23 – Profile & Association Switcher](https://maierharry.atlassian.net/browse/WEG-23)

## Überblick

Das Modul **Profile & Association Switcher** (WEG-23) bietet Benutzern die Möglichkeit, ihr persönliches Profil zu verwalten und den Kontext zwischen verschiedenen WEGs (Associations) zu wechseln.  

Es stellt sicher, dass Benutzer jederzeit im richtigen organisatorischen Kontext arbeiten und dass Navigation, Berechtigungen und UI-Elemente dynamisch an die jeweilige Association angepasst werden.  

Ziel ist eine klare Benutzererfahrung bei Multi-Mandanten-Zugriffen sowie eine einheitliche Verwaltung persönlicher Daten und Sicherheitseinstellungen.

## Beschreibung

WEG-23 verbindet Benutzerprofilverwaltung und Mandantenkontext in einer konsistenten Oberfläche.  

Benutzer, die mehreren Associations angehören, können kontextbezogen wechseln, während alle sicherheits- und rollenbasierten Mechanismen (RBAC, Policies, Spracheinstellungen) automatisch aktualisiert werden.

Hauptfunktionen:

- **Profilseite:** Benutzer können persönliche Daten wie Name, Sprache und Passwort bearbeiten. Sicherheitsinformationen (letzte Logins, aktive Sessions) werden im MVP nur angezeigt.  

- **Association Switcher:** Benutzer können zwischen verschiedenen Associations wechseln, sofern sie dort Mitglied sind. Der aktive Kontext wird im UI hervorgehoben.  

- **Deep-Link Handling:** Links, die auf eine spezifische WEG verweisen, setzen den Kontext automatisch, sofern der Benutzer berechtigt ist.  

- **UI-Guarding:** Nach einem Kontextwechsel werden Navigation, Berechtigungen und sichtbare Komponenten neu geladen.  

- **Audit-Integration:** Jeder Kontextwechsel oder Profil-Update kann optional im Audit-Log (WEG-24) vermerkt werden.  

## Geschäftsregeln & Logik

- Spracheinstellungen gelten global pro Benutzer; Associations können jedoch einen Standardwert vorschlagen (WEG-15).  

- Nur Associations, in denen der Benutzer eine aktive Mitgliedschaft besitzt, dürfen im Switcher angezeigt werden.  

- Ein Kontextwechsel darf nur erfolgen, wenn keine schreibenden Prozesse (z. B. Formularänderungen) aktiv sind.  

- Der aktuelle Kontext (Association-ID) wird serverseitig bei jedem Request geprüft.  

- Änderungen am Profil oder Passwort erfordern gültige Authentifizierung (WEG-20).  

## Akzeptanzkriterien

- **Gegeben** ein Benutzer ist in mehreren Associations aktiv &rarr; **Wenn** er den Switcher nutzt &rarr; **Dann** aktualisieren sich Navigation, Policies und Datenkontext korrekt.  

- **Gegeben** ein Benutzer ruft einen Deep-Link zu einer anderen Association auf &rarr; **Wenn** er dort Mitglied ist &rarr; **Dann** wird der Kontext automatisch gesetzt und das UI lädt die passenden Inhalte.  

- **Gegeben** ein Benutzer versucht, eine Association zu wählen, für die er keine Berechtigung hat &rarr; **Wenn** er dies ausführt &rarr; **Dann** erhält er eine Fehlermeldung (403) und der Versuch wird im Audit-Log dokumentiert.  

- **Gegeben** ein Benutzer ändert seine Spracheinstellung &rarr; **Wenn** die Änderung gespeichert wird &rarr; **Dann** werden alle UI-Komponenten in der neuen Sprache angezeigt.  

- **Gegeben** ein Benutzer speichert sein neues Passwort &rarr; **Wenn** die Änderung erfolgreich war &rarr; **Dann** werden alle anderen Sessions automatisch beendet.  

## Nicht-Ziele

- Keine Geräteverwaltung oder Multi-Faktor-Authentifizierung im MVP.  

- Kein Self-Service für Rollen- oder Berechtigungsänderungen über das Profil.  

- Keine gleichzeitige Nutzung mehrerer aktiver Kontexte.  

## Kritische Fälle

- **Ungültige Mitgliedschaft:** Ein Benutzer ohne aktive Zugehörigkeit darf keine Association auswählen.  

- **Abgebrochener Kontextwechsel:** Bei Netzwerkunterbrechung muss das System zum letzten gültigen Kontext zurückkehren.  

- **Verlorene Sitzungen:** Bei Timeout wird der Benutzer auf die Login-Seite (WEG-20) weitergeleitet, der letzte Kontext wird aber gespeichert.  

## Abhängigkeiten

-  – Verwaltung der Spracheinstellungen pro Benutzer.  

-  – Kontrolle von Navigation und Zugriffsschutz nach Kontextwechsel.  

-  – Policies werden bei Kontextwechsel neu geladen.  

-  – Dokumentiert Änderungen an Profil oder Kontext.  

-  – Verwaltung von Passwörtern und Sessions.  

## Offene Fragen

- Soll der Kontextwechsel bei laufenden Formularen blockiert werden oder automatisch warnen?  

- Soll die Profilseite in Zukunft auch Benutzerbild oder MFA-Einstellungen enthalten?  

- Wird das System bei Sprachwechsel automatisch alle offenen Tabs synchronisieren?  

## Zukunftserweiterungen

- Geräteverwaltung und aktive Sitzungsübersicht.  

- Integration von MFA-Geräten und Sicherheitstoken.  

- Unterstützung von Benutzerbildern (Avatar) und erweiterten Profildetails.  

- Echtzeit-Synchronisierung von Spracheinstellungen zwischen Browser-Tabs.  

## Verknüpfte Tasks

- [WEG-230 – Profile Page](https://maierharry.atlassian.net/browse/WEG-230) – Implementiert die Profilseite zur Änderung von Name, Sprache und Passwort.  

- [WEG-231 – Frontend Integration of Association Switcher](https://maierharry.atlassian.net/browse/WEG-231) – Fügt den Mandanten-Switcher in die UI ein und synchronisiert Navigation und Policies.  

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Profilverwaltung (Name, Sprache, Passwort), Context-Switcher zwischen WEGs, UI-Integration und Audit-Logging.

**Phase 2**

Geräteverwaltung, aktive Sitzungsanzeige, MFA-Geräteverwaltung und Profilbild-Unterstützung.

**Phase 3**

Echtzeit-Synchronisierung, adaptive Kontextsteuerung und vollständige Integration in mobile Clients.