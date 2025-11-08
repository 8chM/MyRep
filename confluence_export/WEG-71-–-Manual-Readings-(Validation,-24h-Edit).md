---
title: WEG-71 – Manual Readings (Validation, 24h Edit)
confluence_id: 27329373
version: 22
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329373/WEG-71+Manual+Readings+Validation+24h+Edit
---

**JIRA-Link:** [WEG-71 – Manual Readings (Validation, 24h Edit)](https://maierharry.atlassian.net/browse/WEG-71)

## Überblick
Das Modul **Manual Readings** (WEG-71) ermöglicht die manuelle Erfassung und Validierung von Zählerständen für Strom, Wasser, Wärme oder Gas. Es unterstützt Eigentümer, Verwalter und beauftragte Personen bei der Datenerfassung über eine einfache Eingabemaske mit automatischer Plausibilitätsprüfung. Alle Eingaben können innerhalb eines 24-Stunden-Fensters korrigiert werden, um versehentliche Fehleingaben zu vermeiden. Ziel ist eine präzise, revisionssichere und nutzerfreundliche Erfassung von Verbrauchsdaten als Grundlage für Abrechnung und Analyse.

## Beschreibung
WEG-71 bildet den operativen Kern der manuellen Verbrauchserfassung im System und stellt sicher, dass alle Messwerte korrekt und überprüfbar gespeichert werden. Das Modul führt Validierungen anhand historischer Werte, definierter Schwellgrenzen und Zählertypen (aus WEG-70) durch, um unplausible oder falsche Eingaben zu vermeiden. Jede Eingabe wird im Status *pending* gespeichert und nach Prüfung in *valid* oder *locked* überführt. Benutzer können innerhalb von 24 Stunden Änderungen vornehmen; danach sind nur noch administrative Korrekturen möglich. Alle Bearbeitungen werden protokolliert, um eine lückenlose Nachvollziehbarkeit sicherzustellen.

Hauptfunktionen:

- **Manuelle Erfassung:** Benutzerfreundliche Oberfläche zur Eingabe aktueller Messwerte.

- **Plausibilitätsprüfung:** Vergleich mit historischen Daten und definierten Toleranzen, Anzeige von Warnungen bei Abweichungen.

- **Bearbeitungsfenster:** 24 Stunden für nachträgliche Änderungen, danach automatische Sperre.

- **Statusverwaltung:** Werte durchlaufen die Stati *pending*, *valid* und *locked*.

- **Audit-Protokollierung:** Jede Eingabe, Änderung und Freigabe wird mit Benutzer und Zeitstempel dokumentiert.

- **Benachrichtigungssystem:** Erinnerung an bevorstehende Ablesungen und Validierungswarnungen über WEG-6.

- **Konflikterkennung:** Bei mehrfacher Eingabe desselben Zählers wird der früheste Wert priorisiert.

## Geschäftsregeln & Logik
- Nach 24 Stunden können nur Verwalter Änderungen durchführen.

- Negative oder unrealistische Werte werden blockiert oder erfordern Begründung.

- Mehrfacherfassungen werden geprüft und priorisiert.

- Alle Datensätze müssen einem aktiven Zähler aus WEG-70 zugeordnet sein.

- Jede Änderung erzeugt einen Audit-Eintrag mit Kommentar und Zeitstempel.

## Akzeptanzkriterien
- **Gegeben** ein Benutzer mit Schreibberechtigung öffnet das Formular &rarr; **Wenn** ein Messwert erfasst wird &rarr; **Dann** prüft das System den Wert, speichert ihn als *pending* und erstellt einen Audit-Eintrag.

- **Gegeben** ein Wert weicht stark vom vorherigen ab &rarr; **Wenn** der Benutzer die Warnung bestätigt und kommentiert &rarr; **Dann** wird der Datensatz gespeichert und markiert.

- **Gegeben** eine Eingabe soll geändert werden &rarr; **Wenn** die 24 Stunden noch nicht verstrichen sind &rarr; **Dann** darf der Benutzer sie korrigieren, der alte Wert bleibt archiviert.

- **Gegeben** ein Benutzer versucht nach 24 Stunden zu ändern &rarr; **Wenn** er keine Verwaltungsrechte hat &rarr; **Dann** verweigert das System die Änderung und zeigt eine Warnung.

- **Gegeben** mehrere Benutzer erfassen denselben Zähler &rarr; **Wenn** unterschiedliche Werte erkannt werden &rarr; **Dann** priorisiert das System den frühesten Eintrag.

## Nicht-Ziele
- Keine automatische Kameraerkennung oder Scan-Funktion im MVP.

- Kein Echtzeitexport an externe Systeme.

- Keine IoT-Synchronisation (geplant für spätere Module).

## Kritische Fälle
- **Abgelaufenes Bearbeitungsfenster:** Nur Verwalter dürfen nach 24 Stunden ändern.

- **Ungültige Werte:** Negative oder unrealistische Eingaben müssen begründet werden.

- **Konflikte:** Mehrfache Eingaben erzeugen Prüfwarnungen.

- **Netzwerkfehler:** Temporär ungespeicherte Eingaben werden lokal gepuffert.

## Abhängigkeiten
- WEG-1 – Platform Foundation – Datenmodell, API und Validierung.

- WEG-6 – Notifications – Erinnerungen und Warnmeldungen.

- WEG-12 – Logging & Health – Automatische Prüf- und Erinnerungsjobs.

- WEG-24 – Audit Log – Nachvollziehbarkeit aller Änderungen.

- WEG-70 – Meter Registry – Quelle der Zählerinformationen.

## Offene Fragen
- Sollen Erinnerungen automatisch oder manuell geplant werden?

- Soll ein Foto des Zählerstands als Nachweis hochgeladen werden können?

- Wie werden Konflikte bei Mehrfacheingaben behandelt (automatisch oder manuell)?

## Zukunftserweiterungen
- **Foto-Upload & OCR:** Automatische Erfassung per Smartphone.

- **Offline-Modus:** Erfassung ohne Internetverbindung.

- **KI-Plausibilitätsgrenzen:** Dynamische Toleranzen basierend auf Verbrauchsmustern.

- **Erinnerungsautomatik:** Flexible Ableseintervalle und E-Mail-/App-Benachrichtigungen.

## Verknüpfte Tasks
- [WEG-710 – Readings with Validation & 24h Edit](https://maierharry.atlassian.net/browse/WEG-710) – Implementierung der manuellen Zählerstanderfassung, Plausibilitätsprüfung und Bearbeitungslogik.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Manuelle Erfassung mit Plausibilitätsprüfung, 24h-Bearbeitungsfenster, Audit-Logging und Benachrichtigungen.

**Phase 2**

Foto-Upload, OCR-Erkennung, flexible Erinnerungsintervalle und Konflikterkennung.

**Phase 3**

KI-basierte Plausibilitätsanpassung, Offline-Modus und automatische Lernmechanismen.