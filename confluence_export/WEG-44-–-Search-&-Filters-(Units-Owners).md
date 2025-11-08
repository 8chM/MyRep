---
title: WEG-44 – Search & Filters (Units/Owners)
confluence_id: 28082947
version: 12
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/28082947/WEG-44+Search+Filters+Units+Owners
---

**JIRA-Link:** [WEG-44 – Search & Filters (Units/Owners)](https://maierharry.atlassian.net/browse/WEG-44)

## Überblick

Das Modul **Search & Filters (Units/Owners)** (WEG-44) stellt eine zentrale und leistungsfähige Such- und Filterkomponente bereit, um Daten innerhalb einer WEG gezielt und effizient zu durchsuchen.

Es erlaubt den Zugriff auf Gebäude, Einheiten, Eigentümer:innen und Bewohner:innen sowie verknüpfte Informationen, z. B. MEA-Anteile, Flächen oder Rollen.

Ziel ist es, Nutzer:innen eine intuitive, schnelle und rollenbasierte Navigation durch komplexe Datenstrukturen zu ermöglichen – sowohl zur operativen Verwaltung als auch zur Analyse.

## Beschreibung

Die Suchfunktion bildet den primären Einstiegspunkt in die Stammdatenarbeit innerhalb des Systems.

Sie ermöglicht sowohl eine einfache Freitextsuche als auch kombinierte Filterabfragen über mehrere Entitäten hinweg (z. B. Gebäude + Eigentümer + Rolle).

Die Suchergebnisse sind dynamisch, mehrsprachig (i18n) und rollenabhängig eingeschränkt.

Caching, Paging und persistente Filter sorgen für eine hohe Performance und Benutzerfreundlichkeit – auch bei großen Datenmengen.

Hauptfunktionen:

- **Freitextsuche:** Ermöglicht die Suche nach Namen, Adressen, Einheiten-IDs, MEA-Werten oder Rollen.

- **Kombinierte Filter:** Mehrdimensionale Filterung nach Gebäuden, Eigentümerstatus, Belegung, Zeitraum, MEA-Bereich usw.

- **Rollenbasierte Sichtbarkeit:** Ergebnisse werden durch RBAC-Regeln (WEG-21) eingeschränkt. Eigentümer:innen sehen nur eigene Einheiten.

- **Favoriten & Gespeicherte Filter:** Benutzer:innen können Filtereinstellungen speichern und wiederverwenden.

- **Paging & Caching:** Leistungsoptimierte Abfragen bei großen Datenmengen.

- **Mehrsprachige Labels:** Integration der Internationalisierung (WEG-15) für einheitliche UI-Begriffe.

- **Auditierbarkeit:** Optionales Logging von Suchvorgängen für Datenschutz-Compliance (WEG-24).

## Geschäftsregeln & Logik

- Nur autorisierte Benutzer:innen können Suchvorgänge durchführen.

- Die Ergebnisse dürfen nur Daten enthalten, für die ein RBAC-Zugriffsrecht besteht.

- Suchergebnisse müssen innerhalb von zwei Sekunden geladen werden (Performance-Anforderung).

- Gespeicherte Filter sind benutzer- und rollenabhängig.

- Systemweite Caching-Strategien reduzieren Serverlast bei wiederkehrenden Suchanfragen.

## Akzeptanzkriterien

- **Gegeben** ein Benutzer wendet einen Filter an &rarr; **Wenn** die Suche ausgeführt wird &rarr; **Dann** werden die Ergebnisse innerhalb von zwei Sekunden geladen und korrekt angezeigt.

- **Gegeben** ein Benutzer ohne Berechtigung sucht nach Daten anderer Eigentümer:innen &rarr; **Wenn** die Suchabfrage ausgeführt wird &rarr; **Dann** werden ausschließlich zulässige Ergebnisse gemäß RBAC-Regeln angezeigt.

- **Gegeben** ein Benutzer speichert Filtereinstellungen &rarr; **Wenn** dieser sich erneut anmeldet &rarr; **Dann** sind die gespeicherten Filter als Favoriten verfügbar.

- **Gegeben** es existieren mehr als 500 Datensätze &rarr; **Wenn** der Benutzer eine Suche durchführt &rarr; **Dann** werden die Ergebnisse paginiert und performant angezeigt.

- **Gegeben** ein Suchvorgang wird ausgelöst &rarr; **Wenn** das Audit-Logging aktiv ist &rarr; **Dann** wird der Vorgang revisionssicher protokolliert.

## Nicht-Ziele

- Keine Volltextsuche über Dokumenteninhalte (DMS – WEG-5).

- Keine KI-basierte semantische Suche im MVP.

- Keine globale Suche über alle WEG-Mandanten hinweg.

## Kritische Fälle

- **Langsame Abfragen:** Bei Performanceproblemen werden Index- und Cacheparameter überprüft und automatisch optimiert.

- **Unvollständige Berechtigungsfilter:** Inkonsistente RBAC-Zuordnungen können zu fehlerhaften Ergebnissen führen.

- **Veraltete Cache-Daten:** Suchergebnisse müssen nach Datenänderungen invalidiert werden.

## Abhängigkeiten

-  – Berechtigungen für Benutzer:innen und Rollen.

-  – Mehrsprachige Labels und Begriffe.

-  – Zugriffsbeschränkungen und Sichtbarkeitsregeln.

-  – Optionale Protokollierung von Suchaktivitäten.

-  – Validierung der Filterparameter und Eingaben.

## Offene Fragen

- Soll die Suche über Beziehungen hinweg erweitert werden (z. B. Eigentümer &rarr; Zählerstände &rarr; Verbräuche)?

- Sollen Suchergebnisse exportierbar sein (z. B. CSV, PDF) bereits im MVP?

- Soll die Suche über alle Mandanten (Cross-WEG-Search) in späteren Phasen verfügbar sein?

## Zukunftserweiterungen

- **Volltextsuche:** Erweiterung um Suchindizes mit Relevanzgewichtung und Synonymerkennung.

- **Exportfunktionen:** Export von Suchergebnissen in CSV/PDF.

- **Erweiterte Filterlogik:** Kombinierte Filter über Module (z. B. Verträge, Zähler, Abrechnungen).

- **Suche über mehrere WEGs:** Optionales Feature für Administrator:innen mit Multi-Mandanten-Berechtigung.

## Verknüpfte Tasks

- [WEG-440 – Search & Filters (units/owners)](https://maierharry.atlassian.net/browse/WEG-440) – Implementierung der zentralen Suchlogik und Filterkombinationen.

- [WEG-441 – Saved Filters & Favorites](https://maierharry.atlassian.net/browse/WEG-441) – Verwaltung gespeicherter Filter und Favoriten im Benutzerprofil.

- [WEG-442 – Search Performance Optimization](https://maierharry.atlassian.net/browse/WEG-442) – Aufbau von Indizes und Caching-Mechanismen.

- [WEG-443 – Audit Integration](https://maierharry.atlassian.net/browse/WEG-443) – Logging relevanter Suchvorgänge und Zugriffe.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Basissuche über Gebäude, Einheiten, Eigentümer:innen und Bewohner:innen; kombinierte Filter, Paging, Caching und Favoritenverwaltung.

**Phase 2**

Einführung einer Volltextsuche mit Relevanzgewichtung und Exportfunktionen.

**Phase 3**

Erweiterte Suchlogik über Module hinweg (Finanzen, Zähler, Verträge) und Multi-Mandanten-Suche.