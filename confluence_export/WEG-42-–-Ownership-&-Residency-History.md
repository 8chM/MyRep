---
title: WEG-42 – Ownership & Residency History
confluence_id: 27853462
version: 12
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27853462/WEG-42+Ownership+Residency+History
---

**JIRA-Link:** [WEG-42 – Ownership & Residency History](https://maierharry.atlassian.net/browse/WEG-42)

## Überblick

Das Modul **Ownership & Residency History** (WEG-42) verwaltet die lückenlose Historie der Eigentums- und Aufenthaltsverhältnisse innerhalb jeder Einheit.

Es stellt sicher, dass Besitz- und Nutzungsverhältnisse zeitlich konsistent, rechtssicher und nachvollziehbar dokumentiert werden.

Jede Änderung – etwa ein Eigentümerwechsel oder ein Mieterwechsel – wird automatisch versioniert, damit jederzeit nachvollzogen werden kann, wer eine Einheit in welchem Zeitraum besessen oder bewohnt hat.

Dieses Modul bildet die Grundlage für Abrechnungen, Umlageschlüssel, Stimmrechtsberechnungen und Kommunikationsprozesse innerhalb des Systems.

## Beschreibung

WEG-42 ist ein Kernelement der Stammdatenlogik und gewährleistet die Nachvollziehbarkeit aller Eigentums- und Bewohnerwechsel.

Jede Einheit (aus WEG-41) besitzt ein eigenes Historienregister, das über Start- und Endzeitpunkte definiert wird.

Sobald ein Eigentümer oder Bewohner eingetragen oder geändert wird, beendet das System automatisch den bisherigen Datensatz und erzeugt eine neue, gültige Version.

Dies ermöglicht ein vollständiges Tracking aller Änderungen über die gesamte Lebensdauer einer Einheit hinweg.

Hauptfunktionen:

- **Historienverwaltung:** Chronologische Erfassung aller Eigentümer:innen und Bewohner:innen pro Einheit mit Start- und Enddatum.

- **Automatische Versionslogik:** Bei Änderungen wird die vorherige Historie geschlossen und ein neuer Eintrag mit aktuellem Zeitstempel angelegt.

- **Miteigentum & Mehrfachnutzung:** Mehrere Eigentümer:innen oder Bewohner:innen können parallel bestehen, sofern MEA- und Nutzungsanteile korrekt verteilt sind.

- **Validierung & Konsistenz:** Überprüft, dass keine Lücken oder Überschneidungen in den Zeiträumen entstehen.

- **Audit-Trail:** Alle Änderungen werden revisionssicher mit Benutzer, Zeitstempel und Grund im Audit-Log (WEG-24) festgehalten.

- **Rollenspezifische Sichtbarkeit:** Nur autorisierte Rollen (z. B. Verwalter:innen, Beirät:innen) können die vollständige Historie einsehen. Bewohner:innen sehen ausschließlich eigene Datensätze.

- **Datenintegration:** Stellt Schnittstellen zu Abrechnung (WEG-87), Stimmrechtslogik (WEG-92) und Finanzen (WEG-8) bereit.

## Geschäftsregeln & Logik

- Jede Einheit muss mindestens einen aktiven Eigentümer besitzen.

- Zeiträume dürfen sich nicht überschneiden; jeder Tag darf nur einem Eigentümer bzw. Bewohner zugeordnet sein.

- Änderungen an Besitz- oder Aufenthaltsverhältnissen schließen automatisch die vorherige Historie.

- MEA-Anteile müssen bei Eigentümerwechseln neu validiert werden.

- Nur berechtigte Rollen dürfen Historieneinträge anlegen, ändern oder löschen.

- Alle Änderungen sind unveränderbar und werden im Audit-Trail (WEG-24) gespeichert.

## Akzeptanzkriterien

- **Gegeben** eine Einheit mit bestehender Historie &rarr; **Wenn** ein neuer Eigentümer eingetragen wird &rarr; **Dann** endet die bisherige Historie automatisch und der neue Eintrag wird mit aktuellem Startdatum angelegt.

- **Gegeben** ein Bewohnerwechsel steht an &rarr; **Wenn** ein Bewohner auszieht &rarr; **Dann** setzt das System das Enddatum des aktuellen Eintrags und archiviert ihn im Audit-Log.

- **Gegeben** zwei Historieneinträge überlappen sich zeitlich &rarr; **Wenn** der Speichervorgang ausgeführt wird &rarr; **Dann** blockiert das System die Speicherung und zeigt eine Fehlermeldung an.

- **Gegeben** ein Miteigentümerwechsel erfolgt &rarr; **Wenn** die neuen Anteile eingegeben werden &rarr; **Dann** prüft das System, ob die Gesamtsumme der MEA-Anteile korrekt ist.

- **Gegeben** ein Benutzer ohne Berechtigung &rarr; **Wenn** dieser versucht, die Historie zu ändern &rarr; **Dann** verweigert das System den Zugriff und erzeugt einen Audit-Eintrag.

## Nicht-Ziele

- Keine automatische Integration mit dem Grundbuch oder Melderegister im MVP.

- Keine KI-basierte Eigentümeridentifikation oder Dokumentvalidierung.

- Keine automatisierten Benachrichtigungen bei Bewohnerwechseln im MVP.

## Kritische Fälle

- **Fehlende Enddaten:** Das System erinnert automatisch an offene Historien ohne Enddatum.

- **Überlappende Eigentumszeiträume:** Fehlerhafte Eingaben führen zu blockierten Speichervorgängen.

- **Unklare Rechtsformen:** Komplexe Eigentumsstrukturen (z. B. GbR, Erbengemeinschaften) werden im MVP nur eingeschränkt unterstützt.

- **Inaktive Eigentümer mit aktiven Einheiten:** Validierung verhindert unvollständige Zustände.

## Abhängigkeiten

-  – Liefert die Basisdaten der Einheiten.

-  – Überprüft korrekte MEA-Verteilung und Nutzungsanteile.

-  – Dokumentiert alle Änderungen.

-  – Verknüpft Eigentümerhistorie mit Finanzperioden.

-  – Nutzt Historie zur Berechnung der Stimmrechte.

## Offene Fragen

- Wie detailliert sollen Bewohner:innen (z. B. Mieter:innen) im MVP erfasst werden?

- Soll ein Eigentümerwechsel automatisch in die Finanzmodule übernommen werden (z. B. Abrechnungszeitraum)?

- Wie wird mit gemeinschaftlichem Eigentum (z. B. Ehepartner) umgegangen – getrennte Einträge oder gemeinsamer Datensatz?

## Zukunftserweiterungen

- **Automatische Grundbuchintegration:** Synchronisation mit öffentlichen Registern (z. B. Kataster, Melderegister).

- **Benachrichtigungssystem:** Automatische E-Mail-/In-App-Hinweise bei Ablauf von Mietverträgen oder Eigentümerwechseln.

- **Erweiterte Strukturen:** Unterstützung komplexer Eigentumsmodelle (GbR, Erbengemeinschaft, juristische Personen).

- **Historienexport:** Möglichkeit, vollständige Eigentümerhistorien als CSV/PDF zu exportieren.

## Verknüpfte Tasks

- [WEG-420 – Ownership/Residency History per Unit](https://maierharry.atlassian.net/browse/WEG-420) – Implementierung der Historienverwaltung mit Zeitvalidierung.

- [WEG-421 – Overlap Validation Engine](https://maierharry.atlassian.net/browse/WEG-421) – Sicherstellung der lückenlosen Zeiträume.

- [WEG-422 – Audit Trail Integration](https://maierharry.atlassian.net/browse/WEG-422) – Dokumentiert Änderungen revisionssicher.

- [WEG-423 – MEA Validation Hook](https://maierharry.atlassian.net/browse/WEG-423) – Prüft Eigentumsanteile bei Wechseln.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Verwaltung der Eigentümer- und Bewohnerhistorien mit Zeitvalidierung, Audit-Log, MEA-Prüfung und Rollensteuerung.

**Phase 2**

Erweiterte Unterstützung für Miteigentum, juristische Personen und GbR-Strukturen.

**Phase 3**

Automatische Grundbuch-/Melderegister-Integration, Benachrichtigungen und Historienexport.