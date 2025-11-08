---
title: WEG-19 – Naming Conventions & ADRs (English-first)
confluence_id: 28082908
version: 14
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/28082908/WEG-19+Naming+Conventions+ADRs+English-first
---

**JIRA-Link:** [WEG-19 – Naming Conventions & ADRs (English-first)](https://maierharry.atlassian.net/browse/WEG-19)

## Überblick
Das Modul **Naming Conventions & ADRs (English-first)** (WEG-19) definiert verbindliche Regeln für Benennungen in Datenbanken, APIs und Quellcode sowie ein standardisiertes Verfahren zur Dokumentation von Architekturentscheidungen.

Ziel ist die Sicherstellung von Konsistenz, Lesbarkeit und langfristiger Wartbarkeit über alle Module hinweg. Gleichzeitig werden Architekturentscheidungen nachvollziehbar festgehalten, um technische Richtlinien und ihre Begründung transparent zu machen.

## Beschreibung
WEG-19 führt einheitliche **Namenskonventionen** und eine **leichtgewichtige ADR-Methodik (Architecture Decision Record)** ein.

Diese beiden Aspekte bilden die Grundlage für eine saubere, nachvollziehbare und dokumentierte Architektur innerhalb des gesamten WEG-Systems.

Hauptfunktionen:

- **Naming Guidelines:** Einheitliche Regeln für Entitäten, API-Routen, Dateien und Code-Bezeichner (z. B. snake_case für Datenbanktabellen, PascalCase für Klassen, kebab-case für API-Routen).

- **English-first-Standard:** Alle Bezeichner, Kommentare und ADRs werden in englischer Sprache geführt, um internationale Lesbarkeit sicherzustellen.

- **ID-Strategie:** Definition von Standard-IDs (UUID/ULID) inklusive Richtlinien zur Generierung, Speicherung und Verwendung.

- **ADR-Prozess:** Einführung eines Prozesses für das Erstellen, Versionieren und Archivieren von Architekturentscheidungen im Repository.

- **CI-Validierung:** Automatische Prüfung der Namenskonventionen über Linting-Regeln in der CI-Pipeline (Integration mit WEG-14).

- **Dokumentationsvorlage:** Bereitstellung eines ADR-Templates mit Metadaten (Datum, Entscheidung, Alternativen, Konsequenzen).

## Geschäftsregeln & Logik
- Alle neuen Entitäten, APIs und Klassen müssen die definierten Naming-Regeln einhalten.

- Abweichungen sind nur mit dokumentierter Ausnahmegenehmigung zulässig.

- Jede Architekturentscheidung, die Einfluss auf Strukturen oder Standards hat, muss durch ein ADR dokumentiert werden.

- ADRs werden versioniert und im Repository abgelegt; ältere Versionen bleiben nachvollziehbar erhalten.

- ID-Strategien werden projekteinheitlich umgesetzt, z. B. **ULIDs** für chronologische Sortierung oder **UUIDv7** für universelle Eindeutigkeit.

- Die CI-Pipeline überprüft Code- und API-Namenskonventionen automatisch bei jedem Commit.

## Akzeptanzkriterien
- **Gegeben** eine neue Datenbanktabelle wird erstellt &rarr; **Wenn** die Migration ausgeführt wird &rarr; **Dann** folgt der Tabellenname dem snake_case-Format.

- **Gegeben** eine neue API-Route wird registriert &rarr; **Wenn** sie hinzugefügt wird &rarr; **Dann** verwendet sie das kebab-case-Format gemäß den Konventionen.

- **Gegeben** eine neue Klasse wird angelegt &rarr; **Wenn** der Code überprüft wird &rarr; **Dann** entspricht der Klassenname dem PascalCase-Standard.

- **Gegeben** eine Architekturentscheidung wird getroffen &rarr; **Wenn** sie dokumentiert wird &rarr; **Dann** wird ein ADR-Dokument mit Entscheidung, Begründung und Auswirkungen erstellt und im Repository gespeichert.

- **Gegeben** ein Commit verletzt eine Naming-Regel &rarr; **Wenn** die CI-Pipeline ausgeführt wird &rarr; **Dann** schlägt der Build fehl und weist auf den Verstoß hin.

## Nicht-Ziele
- Keine automatische Übersetzung von bestehenden Namenskonventionen oder Kommentaren.

- Kein vollständiger Style-Guide für Code-Formatierung (nur Namensregeln und ADR-Prozess).

- Keine Rückwärtskompatibilität für bestehende Altstrukturen.

- Kein Echtzeit-Linting in der Entwicklungsumgebung im MVP.

## Kritische Fälle
- **Inkonsistente Bezeichner:** Abweichungen zwischen Modulen können zu Fehlinterpretationen und Integrationsproblemen führen.

- **Fehlende ADRs:** Fehlende Dokumentation erschwert die Nachvollziehbarkeit technischer Entscheidungen.

- **Falsche ID-Strategie:** Nicht eindeutige IDs oder Mischstrategien können zu Inkonsistenzen in Datenmodellen führen.

- **Fehlerhafte CI-Regeln:** Ungenaue Linting-Prüfungen könnten fälschlicherweise valide Namen ablehnen oder Verstöße übersehen.

## Abhängigkeiten
- **WEG-10 – Solution Setup & Infrastructure:** Integration der Linting-Regeln in Build- und Pipeline-Konfiguration.

- **WEG-14 – Testing & CI Basics:** Durchsetzung der Naming-Regeln und Prüfung innerhalb der CI-Prozesse.

- **WEG-12 – Error Handling, Logging & Health:** Einheitliche Namenskonventionen in Log-Ausgaben und Fehlermeldungen.

## Offene Fragen
- Soll die CI-Pipeline Naming-Verstöße als Warnung oder als Blocker behandeln?

- Wie granular sollen ADRs versioniert werden (pro Entscheidung oder Sammeldokument)?

- Müssen ADRs in späteren Phasen automatisch aus Git-Commits generiert werden?

## Zukunftserweiterungen
- **Automatische ADR-Generierung:** Erzeugung neuer ADRs auf Basis von Merge-Requests oder Architektur-Änderungen.

- **Erweiterter Style-Guide:** Ergänzung um Code-Formatierung, Kommentar-Standards und API-Design-Regeln.

- **Automatisierte Linting-Prüfungen:** Dynamische Erkennung von Naming-Verstößen durch Machine-Learning-Modelle.

- **ADR-Dashboard:** Übersicht aller getroffenen Architekturentscheidungen mit Filter- und Suchfunktion.

## Verknüpfte Tasks
- **WEG-190 – Naming Conventions Document:** Dokumentiert verbindliche Namenskonventionen und Beispiele.

- **WEG-191 – ADR Template & Process:** Erstellt ein standardisiertes ADR-Template und definiert den Workflow.

- **WEG-192 – Linting Rules for Naming Conventions:** Implementiert CI-Linting-Regeln zur Einhaltung der Standards.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Einführung konsistenter Namenskonventionen (DB, API, Code), ADR-Prozess, ID-Strategie (UUID/ULID), Integration in CI-Pipeline.

**Phase 2**

Erweiterter Style-Guide, erweiterte ADR-Richtlinien und erweiterte Linting-Prüfungen in der CI-Umgebung.

**Phase 3**

Automatische ADR-Generierung, erweiterte Audit-Funktionen und ML-basierte Erkennung von Naming-Verstößen.