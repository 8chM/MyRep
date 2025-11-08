---
title: WEG-16 – Frontend Shell, Routing & Access Guard
confluence_id: 27459975
version: 15
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27459975/WEG-16+Frontend+Shell+Routing+Access+Guard
---

**JIRA-Link:** [WEG-16 – Frontend Shell, Routing & Access Guard](https://maierharry.atlassian.net/browse/WEG-16)

## Überblick

Das Modul **Frontend Shell, Routing & Access Guard** (WEG-16) bildet das zentrale Fundament der Benutzeroberfläche des WEG Management Systems.

Es definiert die grundlegende Struktur der Webanwendung mit Navigation, Layout, Zugriffskontrolle und Benutzerführung.

Ziel ist eine performante, konsistente und sichere Nutzererfahrung, die alle Module integriert und auf rollenbasiertem Zugriff (RBAC) basiert.

## Beschreibung

WEG-16 implementiert die **App-Shell**, welche als Rahmen für alle Frontend-Komponenten dient, und integriert das Routing-System mit **Lazy Loading**, um Performance und Skalierbarkeit zu gewährleisten.

Darüber hinaus stellt das Modul sicher, dass Benutzer nur auf Inhalte zugreifen können, die ihren Rollen entsprechen, indem **Access Guards** und **Permission Checks** in alle Navigationsflüsse eingebettet werden.

Hauptfunktionen:

- **App Shell Layout:** Einheitliche Struktur aus Kopfbereich, Seitenleiste und Inhaltsbereich mit responsivem Design.

- **Routing Engine:** Modular konfiguriertes Routing mit Unterstützung für verschachtelte und dynamische Pfade.

- **Access Guards:** Durchsetzung von Berechtigungen auf Routenebene unter Verwendung des RBAC-Modells aus WEG-2.

- **Navigation & Breadcrumbs:** Dynamische Navigation mit Hervorhebung aktiver Routen und automatischer Breadcrumb-Aktualisierung.

- **UX-Konventionen:** Einheitliche Anzeige von Ladezuständen (Skeletons), Fehlerseiten (403/404) und Session-Timeouts.

Das Modul dient als Bindeglied zwischen UI-Komponenten, API-Clients (WEG-11) und den Sicherheitsmechanismen (WEG-2).

## Geschäftsregeln & Logik

- Zugriffe auf geschützte Routen sind ausschließlich für authentifizierte Benutzer mit passenden Rollen erlaubt.

- Menü- und Navigationsstrukturen werden ausschließlich aus RBAC-Policies generiert, nicht aus statischen Frontend-Listen.

- Ungültige Zugriffe führen zu standardisierten Fehlerseiten (403 – Access Denied, 404 – Not Found).

- Lazy-Loading-Mechanismen dürfen keine unautorisierten Prefetches auslösen.

- Beim Wechsel zwischen WEGs (Tenants) werden Routen und Kontexte dynamisch neu geladen.

- Session-Timeouts leiten den Benutzer automatisch zur Login-Seite um.

## Akzeptanzkriterien

- **Gegeben** ein Benutzer ist nicht angemeldet &rarr; **Wenn** er eine geschützte Route aufruft &rarr; **Dann** wird er automatisch auf die Login-Seite weitergeleitet.

- **Gegeben** ein Benutzer ohne Administratorrolle &rarr; **Wenn** er versucht, auf den Adminbereich zuzugreifen &rarr; **Dann** wird eine 403-Seite angezeigt und der Zugriff verweigert.

- **Gegeben** ein Benutzer wechselt zwischen Modulen &rarr; **Wenn** eine Route geladen wird &rarr; **Dann** wird sie korrekt hervorgehoben und die Breadcrumbs aktualisiert.

- **Gegeben** ein Benutzer verliert seine Session &rarr; **Wenn** er eine Aktion ausführt &rarr; **Dann** wird ein Session-Timeout angezeigt und der Benutzer zur Anmeldung zurückgeführt.

- **Gegeben** ein ungültiger Pfad wird aufgerufen &rarr; **Wenn** keine Route gefunden wird &rarr; **Dann** zeigt das System eine standardisierte 404-Fehlerseite an.

## Nicht-Ziele

- Kein vollständiges Design-System im MVP (Grundlayout, kein Corporate Branding).

- Keine dynamische Rechteverwaltung im Frontend – Berechtigungen werden ausschließlich vom Backend bereitgestellt.

- Keine Offline-Funktionalität oder PWA-Features im MVP.

## Kritische Fälle

- **Fehlende Berechtigungen:** Ungültige Permission-Prüfungen könnten Datenlecks verursachen – Guards müssen strikt durchgesetzt werden.

- **Routing-Konflikte:** Überlappende Pfade oder nicht eindeutige Konfigurationen können Navigation brechen.

- **Inkompatible Lazy-Loading-Pfade:** Falsche Aufteilung der Module kann Ladezeiten verlängern oder Fehler auslösen.

- **Session-Handling:** Abgelaufene Tokens müssen konsistent behandelt und Benutzer sicher abgemeldet werden.

## Abhängigkeiten

- **WEG-2 – Identity & Access:** Stellt Authentifizierung, JWT-Handling und Rollenmodell bereit.

- **WEG-11 – API, OpenAPI & TypeScript Client:** Wird für API-Aufrufe und Endpoint-Validierung genutzt.

- **WEG-15 – Internationalization (EN/DE):** Lokalisierung der Navigations- und Fehlermeldungstexte.

- **WEG-17 – Configuration & Feature Flags:** Steuerung der Sichtbarkeit von Modulen über Feature-Flags.

## Offene Fragen

- Sollen Breadcrumbs auch für tief verschachtelte Routen (z. B. /building/:id/unit/:id) automatisch generiert werden?

- Soll ein Benutzer zwischen mehreren WEGs (Tenants) über eine Dropdown-Auswahl wechseln können?

- Wie sollen ungültige Tokens bei laufender Sitzung gehandhabt werden (Silent Refresh oder Re-Login)?

## Zukunftserweiterungen

- **Design-System & Theming:** Einführung eines zentralen UI-Kit mit Branding-Optionen und Dark-Mode.

- **Multi-Tenancy-Switcher:** Direktes Umschalten zwischen Associations innerhalb der Shell.

- **Progressive Web App (PWA):** Offline-Zugriff, Caching und Installation auf mobilen Geräten.

- **Personalisierung:** Favoriten, zuletzt besuchte Seiten und modulare Dashboards.

## Verknüpfte Tasks

- **WEG-160 – Shell Layout (Header, Sidebar, Content):** Implementiert das Grundlayout und Navigationselemente.

- **WEG-161 – Routing Configuration:** Definiert die modulare Routing-Struktur mit Lazy Loading.

- **WEG-162 – Access Guards & Permission Checks:** Implementiert rollenbasierte Zugriffskontrollen.

- **WEG-163 – Breadcrumb & Active Route Highlighting:** Fügt Breadcrumb-Logik und visuelle Route-Hervorhebung hinzu.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

App-Shell mit Layout und Navigation, rollenbasierte Access-Guards, Lazy-Loaded Routing, standardisierte Fehlerseiten, Session-Timeout-Handling.

**Phase 2**

Einführung eines Design-Systems, Theming (Dark Mode, Branding), erweiterte Menülogik, Multi-Tenancy-Switcher.

**Phase 3**

Offline-Fähigkeit, PWA-Features, modulare Dashboards und Personalisierung.