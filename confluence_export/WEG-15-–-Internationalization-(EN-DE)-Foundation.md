---
title: WEG-15 – Internationalization (EN/DE) Foundation
confluence_id: 27853423
version: 14
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27853423/WEG-15+Internationalization+EN+DE+Foundation
---

**JIRA-Link:** [WEG-15 – Internationalization (EN/DE) Foundation](https://maierharry.atlassian.net/browse/WEG-15)

## Überblick

Das Modul **Internationalization (EN/DE) Foundation** (WEG-15) stellt die sprachliche Grundlage des gesamten Systems bereit.

Es ermöglicht die vollständige Nutzung der Anwendung in **Deutsch** und **Englisch**, einschließlich Übersetzungen von UI-Texten, Datums- und Zahlenformaten sowie der Benutzer- und Association-basierten Spracheinstellungen.

Ziel ist eine konsistente, international nutzbare Benutzeroberfläche, die sowohl technisch als auch organisatorisch mehrsprachige Verwaltungen unterstützt.

## Beschreibung

WEG-15 implementiert die internationale Ausrichtung der Plattform über standardisierte **i18n-Kataloge**, ein dynamisches **Locale-Management** und einen **Sprach-Switcher**, der in der Frontend-Shell eingebunden ist.

Jede Association kann ihre Standardsprache festlegen, während Benutzer eine eigene bevorzugte Sprache auswählen können.

Hauptfunktionen:

- **i18n-Kataloge (EN/DE):** Enthalten alle Systemtexte, Fehlermeldungen und UI-Elemente mit eindeutigen, englischen Key-Bezeichnern.

- **Sprache-Switcher im Frontend:** Ermöglicht das Umschalten zwischen Deutsch und Englisch; die gewählte Sprache wird im Benutzerprofil gespeichert.

- **Locale-basiertes Format:** Automatische Anpassung von Datums-, Zeit- und Zahlenformaten an die regionale Einstellung der Association.

- **Linting & Validation:** Automatisierte Prüfung der i18n-Keys auf Vollständigkeit und Inkonsistenzen im CI-Prozess.

- **Fallback-System:** Fehlt eine Übersetzung, wird der englische Key angezeigt und ein Warnhinweis im Log ausgegeben.

Das Modul gewährleistet somit nicht nur eine konsistente Übersetzung, sondern auch eine valide Formatierung aller sprachabhängigen Inhalte.

## Geschäftsregeln & Logik

- Standardsprachen sind **Deutsch (de-DE)** und **Englisch (en-US)**.

- Übersetzungsschlüssel sind eindeutig, beschreibend und ausschließlich auf Englisch definiert.

- Fehlende Übersetzungen müssen sichtbar gemacht und protokolliert werden.

- Locale-Einstellungen können global (Systemstandard) oder je Association festgelegt werden.

- Benutzerindividuelle Spracheinstellungen haben Vorrang vor der Association-Einstellung.

- Zahl- und Datumsformate müssen in allen Modulen konsistent angewendet werden.

## Akzeptanzkriterien

- **Gegeben** ein Benutzer ist in der Web-App angemeldet &rarr; **Wenn** er den Sprache-Switcher nutzt &rarr; **Dann** wird die gesamte UI dynamisch zwischen Deutsch und Englisch umgeschaltet, und die Auswahl wird dauerhaft gespeichert.

- **Gegeben** eine Association verwendet das Locale &bdquo;de-DE&ldquo; &rarr; **Wenn** Zahlen oder Daten angezeigt werden &rarr; **Dann** werden sie mit deutschem Dezimal- und Datumsformat dargestellt (z. B. 1.234,56 &euro; / 31.12.2025).

- **Gegeben** ein neuer i18n-Key wird hinzugefügt &rarr; **Wenn** keine Übersetzung vorliegt &rarr; **Dann** wird der Key-Name im UI angezeigt und eine Warnung im Log erzeugt.

- **Gegeben** ein Benutzer erstellt ein neues Konto &rarr; **Wenn** keine individuelle Sprache gewählt wurde &rarr; **Dann** übernimmt das System automatisch die Sprache der Association.

- **Gegeben** die CI-Pipeline läuft &rarr; **Wenn** ein i18n-Lint-Check ausgeführt wird &rarr; **Dann** werden fehlende oder doppelte Keys als Fehler gemeldet.

## Nicht-Ziele

- Keine Unterstützung weiterer Sprachen im MVP (z. B. Französisch, Spanisch).

- Keine maschinelle Übersetzung über externe APIs (z. B. DeepL, Google Translate).

- Keine dynamische Übersetzung benutzergenerierter Inhalte (z. B. Freitexte).

## Kritische Fälle

- **Fehlende Übersetzungen:** Unübersetzte Keys dürfen nicht unbemerkt bleiben – sie müssen visuell auffallen.

- **Falsche Locale-Einstellungen:** Falsche Zahlen- oder Datumsformate können zu Fehlinterpretationen führen.

- **Unvollständige Kataloge:** Unterschiedliche Katalogversionen zwischen Modulen führen zu Inkonsistenzen und müssen im CI-Prozess erkannt werden.

## Abhängigkeiten

- **WEG-16 – Frontend Shell, Routing & Access Guard:** Integration des Sprache-Switchers und Anwendung der Locale-Einstellungen im Frontend.

- **WEG-3 – Tenant Provisioning & Administration:** Verwaltung der Association-basierten Spracheinstellungen.

- **WEG-14 – Testing & CI Basics:** Validierung der i18n-Linting-Prozesse innerhalb der CI-Pipeline.

## Offene Fragen

- Sollen zusätzliche Sprachen (z. B. Französisch, Italienisch) bereits architektonisch vorbereitet werden?

- Wie sollen Übersetzungen für dynamische Inhalte (z. B. E-Mails, Dokumente) im späteren Verlauf umgesetzt werden?

- Soll die Benutzer-Sprache automatisch anhand des Browser-Locales erkannt werden?

## Zukunftserweiterungen

- Unterstützung zusätzlicher Sprachen mit zentralem Übersetzungsmanagement.

- Integration professioneller Übersetzungs-Workflows (Import/Export über PO-Dateien oder externe Dienste).

- KI-gestützte Übersetzungsvorschläge für neue Texte.

- Benutzer- und Modul-spezifische Lokalisierung (z. B. unterschiedliche Sprachen für Frontend und DMS-Dokumente).

## Verknüpfte Tasks

- **WEG-150 – i18n Catalogs (EN/DE)** – Implementiert Übersetzungskataloge für Deutsch und Englisch.

- **WEG-151 – Language Switcher UI** – Erstellt den Sprache-Switcher und speichert Benutzerpräferenzen.

- **WEG-152 – Number & Date Formatting Rules** – Definiert Formatierungsregeln für Datums- und Zahlenwerte.

- **WEG-153 – i18n Key Extraction & Validation Scripts** – Stellt Skripte zur Extraktion und Validierung der i18n-Keys bereit.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

i18n-Kataloge für EN/DE, Sprache-Switcher, Zahl-/Datums-Lokalisierung, CI-Linting für Übersetzungsschlüssel.

**Phase 2**

Erweiterung um zusätzliche Sprachen und Einführung eines Übersetzungs-Workflows.

**Phase 3**

Automatische Übersetzungen, zentrale Übersetzungsverwaltung und KI-gestützte Lokalisierung.