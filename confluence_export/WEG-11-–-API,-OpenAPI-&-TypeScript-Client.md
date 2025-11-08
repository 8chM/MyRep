---
title: WEG-11 – API, OpenAPI & TypeScript Client
confluence_id: 27165380
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27165380/WEG-11+API+OpenAPI+TypeScript+Client
---

**JIRA-Link:** [WEG-11 – API, OpenAPI & TypeScript Client](https://maierharry.atlassian.net/browse/WEG-11)

## Überblick

Das Modul **API, OpenAPI & TypeScript Client** (WEG-11) stellt die Grundlage für eine standardisierte, versionierte Schnittstelle zwischen Backend und Frontend dar.
Es sorgt dafür, dass alle Dienste der WEG-Plattform konsistent, nachvollziehbar und dokumentiert kommunizieren.
Durch eine automatisch generierte OpenAPI-Spezifikation und den zugehörigen TypeScript-Client wird eine einheitliche Vertragsbasis geschaffen, die Integrationsfehler vermeidet und Entwicklungsgeschwindigkeit steigert.

## Beschreibung

WEG-11 definiert eine klar strukturierte, versionierte REST-API, dokumentiert diese mit OpenAPI 3 (Swagger) und generiert daraus automatisch einen TypeScript-Client zur Nutzung im Frontend.
Das Modul stellt sicher, dass Backend-Änderungen reproduzierbar, validierbar und CI-integriert erfolgen.

Hauptfunktionen:

- **Versionierte API-Routen:** Alle Endpunkte folgen dem Schema /api/v{n} mit klar definierten Versionsregeln (Major für Breaking-Changes, Minor für additive Erweiterungen).

- **OpenAPI-Dokumentation:** Vollständige Spezifikation mit Schemas, Operation IDs, Tags, Fehlerdefinitionen und Parametern.

- **ProblemDetails-Schema:** Einheitliches Fehlerrückgabeformat über die gesamte Plattform.

- **TypeScript-Client-Generierung:** Automatische Erstellung und Aktualisierung mittels NSwag mit Skripten zur Regeneration bei Änderungen.

- **CI-Validierung:** Überprüfung, dass der generierte Client der aktuellen API-Version entspricht – Abweichungen führen zu Build-Fehlern.

- **Richtlinien für API-Versionierung:** Dokumentierte Vorgaben für Breaking-Changes, Deprecations und Abwärtskompatibilität.

Ziel ist eine klar definierte, transparente Schnittstelle, die interne wie externe Entwickler unterstützt und Fehlkommunikation zwischen Systemen verhindert.

## Geschäftsregeln & Logik

- Alle Endpunkte sind **explizit versioniert**; Breaking-Changes erfordern eine neue Hauptversion.

- Minor-Versionen dürfen nur additive Erweiterungen enthalten, niemals API-Verträge verändern.

- Jede veröffentlichte OpenAPI-Spezifikation muss **vollständig valide** sein (Lint-Check im CI).

- Änderungen an Schemas oder Operationen erzwingen eine automatische Regeneration des TypeScript-Clients.

- Fehlerantworten folgen **ausschließlich** dem ProblemDetails-Schema.

- Der TypeScript-Client ist Bestandteil der Build-Pipeline; divergierende Versionen führen zu Abbruch.

## Akzeptanzkriterien

- **Gegeben:** die laufende API &rarr; **Wenn:** /api/v1/swagger.json angefragt wird &rarr; **Dann:** wird ein valides OpenAPI-3-Dokument ausgeliefert, das alle registrierten Endpunkte beschreibt.

- **Gegeben:** ein CI-Build läuft &rarr; **Wenn:** der TypeScript-Client generiert wird &rarr; **Dann:** entspricht dieser exakt der veröffentlichten API-Version; Abweichungen führen zu einem Build-Fehler.

- **Gegeben:** ein Request löst eine Exception aus &rarr; **Wenn:** der Fehler vom Backend behandelt wird &rarr; **Dann:** liefert die API ein ProblemDetails-Objekt mit Fehlercode und Trace-ID zurück.

- **Gegeben:** eine neue Funktionalität verändert den API-Vertrag &rarr; **Wenn:** Breaking-Changes erkannt werden &rarr; **Dann:** wird automatisch eine neue Hauptversion /api/v{n+1} generiert und dokumentiert.

- **Gegeben:** ein Entwickler ändert ein Schema &rarr; **Wenn:** der Client regeneriert wird &rarr; **Dann:** wird ein aktualisierter TypeScript-Client erzeugt und in das Repository übernommen.

## Nicht-Ziele

- Keine GraphQL- oder gRPC-Schnittstellen im MVP.

- Keine Generierung von Clients für andere Sprachen (z. B. Java, Python) im MVP.

- Keine bidirektionale API-Synchronisierung (z. B. mit Partner-Systemen).

## Kritische Fälle

- **Server-Client-Divergenz:** Wenn der generierte Client nicht dem aktuellen API-Stand entspricht, muss der Build fehlschlagen.

- **Unvollständige Dokumentation:** Fehlende Schemas oder Fehlercodes führen zu ungültigen Clients – Linting muss das verhindern.

- **Versionierungsfehler:** Unerlaubte Änderungen ohne Versionsanhebung führen zu Integrationsproblemen.

- **Manuelle Client-Änderungen:** Direkte Modifikation des generierten Clients ist untersagt und wird durch CI geprüft.

## Abhängigkeiten

- WEG-10 – Solution Setup & Infrastructure Bereitstellung der Infrastruktur, in der die API betrieben und dokumentiert wird.

- WEG-12 – Error Handling, Logging & Health Stellt das standardisierte Fehlerformat (ProblemDetails) für alle Endpunkte bereit.

- WEG-14 – Testing & CI Basics CI-Validierung des OpenAPI-Dokuments und automatisierte Client-Regeneration.

## Offene Fragen

- Welche Naming-Konventionen (Tags, Operation IDs, Parameter) gelten verbindlich für alle Module?

- Soll die API-Dokumentation automatisch versioniert veröffentlicht werden (z. B. /docs/v1, /docs/v2)?

- Wie wird Deprecation-Handling umgesetzt – explizite Header oder Dokumentationseintrag?

## Zukunftserweiterungen

- **Feature:** Generierung zusätzlicher Clients (C#, Python) für Partner- oder Integrationssysteme.

- **Feature:** Einführung von Hypermedia- oder HATEOAS-Elementen zur API-Navigation.

- **Feature:** Erweiterung auf alternative API-Technologien wie GraphQL oder gRPC.

- **Feature:** Public-API-Portal mit Zugriffskontrolle und Auth-Tokens.

## Verknüpfte Tasks

- [WEG-110 – Enable OpenAPI & API Versioning](https://maierharry.atlassian.net/browse/WEG-110) – Aktiviert Swashbuckle, definiert /api/v1 und stellt Swagger-Dokumentation bereit.

- [WEG-111 – Generate TypeScript Client](https://maierharry.atlassian.net/browse/WEG-111) – Erstellt und integriert den Client in die CI-Pipeline.

- [WEG-112 – Client Regeneration Script](https://maierharry.atlassian.net/browse/WEG-112) – Automatisiert die Client-Neugenerierung bei API-Änderungen.

- [WEG-113 – API Error Schema Docs](https://maierharry.atlassian.net/browse/WEG-113) – Dokumentiert das Fehlerformat (ProblemDetails) in der OpenAPI-Spezifikation.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Bereitstellung der REST-API v1 mit OpenAPI-Dokumentation, TypeScript-Client-Generierung und standardisiertem Fehlerformat.

**Phase 2**

Unterstützung zusätzlicher Client-Typen (C#, Python) und formalisierte Richtlinien für Breaking-Changes.

**Phase 3**

Erweiterte API-Paradigmen (HATEOAS, GraphQL, gRPC) und Public-API-Zugänge.