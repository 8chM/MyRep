---
title: WEG-21 – RBAC Roles & Policies per Association
confluence_id: 27722204
version: 21
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27722204/WEG-21+RBAC+Roles+Policies+per+Association
---

**JIRA-Link:** [WEG-21 – RBAC Roles & Policies per Association](https://maierharry.atlassian.net/browse/WEG-21)

## Überblick

Das Modul **RBAC Roles & Policies per Association** (WEG-21) definiert das rollenbasierte Berechtigungssystem (Role-Based Access Control) innerhalb des WEG Management Systems.  

Es sorgt dafür, dass jede Aktion im System nur von autorisierten Benutzern durchgeführt werden kann und dass Berechtigungen klar strukturiert, nachvollziehbar und mandantenspezifisch zugewiesen werden.  

Ziel ist es, eine konsistente, sichere und flexible Rechteverwaltung zu gewährleisten, die sich an die Größe und Komplexität der jeweiligen WEG anpasst.

## Beschreibung

WEG-21 implementiert ein feingranulares Rollen- und Policy-Modell, das den Zugriff auf Systemfunktionen, Daten und UI-Elemente steuert.  

Jede **Association (WEG)** besitzt ihre eigenen Rollen und Berechtigungsdefinitionen, wodurch unterschiedliche Rechtekonfigurationen pro Mandant ermöglicht werden.  

Das Modul integriert sich direkt in API, UI und Audit-Log, um jede Berechtigungsentscheidung nachvollziehbar zu machen.

Hauptfunktionen:

- **Rollenmodell:** Definiert Standardrollen wie *Manager*, *Board*, *Owner* und *Resident*, die sich mandantenspezifisch erweitern lassen.  

- **Policy-Katalog:** Policies beschreiben atomare Rechte (z. B. meeting.manage, finance.view, meter.read) und können zu Rollen kombiniert werden.  

- **Context-Aware Enforcement:** Dieselbe Rolle kann in unterschiedlichen Associations abweichende Rechte haben.  

- **UI-Integration:** Sichtbare Menüs, Buttons und Aktionen werden dynamisch anhand der aktiven Policies angezeigt oder ausgeblendet.  

- **Auditierte Änderungen:** Zuweisung, Änderung und Entzug von Rollen werden revisionssicher im Audit-Log (WEG-24) dokumentiert.  

- **Versionierung:** Rollen und Policies werden versioniert gespeichert, um Änderungen über Zeit hinweg nachvollziehen zu können.  

## Geschäftsregeln & Logik

- **Standardrollen im MVP:** Manager, Board, Owner, Resident.  

- Rollen können kombiniert werden; effektive Berechtigungen ergeben sich aus der Summe aller zugewiesenen Policies.  

- **Least Privilege:** Jeder Benutzer erhält nur die minimal notwendigen Berechtigungen.  

- Änderungen an Rollen erfordern entsprechende Administratorrechte.  

- **Zirkuläre Rollenzuordnungen** (Rollen, die indirekt auf sich selbst verweisen) sind unzulässig und werden blockiert.  

- Jede Policy wird zentral definiert und kann nicht mandantenspezifisch überschrieben werden (nur Zuweisung ist mandantenbezogen).  

## Akzeptanzkriterien

- **Gegeben** ein Owner ohne Policy finance.view &rarr; **Wenn** er versucht, Finanzberichte zu öffnen &rarr; **Dann** wird der Zugriff verweigert und der Vorgang im Audit-Log protokolliert.  

- **Gegeben** ein Manager mit Policy meeting.manage &rarr; **Wenn** er ein Meeting bearbeitet &rarr; **Dann** kann er Agenden und Proxies konfigurieren.  

- **Gegeben** ein Versuch, eine Rolle zu löschen, die übergeordnete Abhängigkeiten hat &rarr; **Wenn** diese Aktion eine zirkuläre Zuordnung erzeugen würde &rarr; **Dann** blockiert das System den Vorgang.  

- **Gegeben** eine neue Rolle wird angelegt &rarr; **Wenn** sie Policies erhält &rarr; **Dann** werden diese sofort in der API- und UI-Authorisierung wirksam.  

- **Gegeben** ein Administrator entzieht mehreren Benutzern dieselbe Rolle &rarr; **Wenn** der Vorgang ausgelöst wird &rarr; **Dann** erscheint eine Warnung mit Bestätigungsaufforderung, bevor die Änderung ausgeführt wird.  

## Nicht-Ziele

- Keine Attribut- oder Claims-basierte Access Control (ABAC) im MVP.  

- Keine dynamische Policy-Berechnung aus Kontextdaten (z. B. Uhrzeit, Gerät, Standort).  

- Keine automatisierte Rechtevererbung über mehrere Associations hinweg.  

## Kritische Fälle

- **Zirkuläre Rollenzuordnung:** Das System muss verhindern, dass Rollen direkt oder indirekt aufeinander verweisen.  

- **Fehlende Standardrollen:** Beim Erstellen einer neuen WEG müssen Default-Rollen automatisch generiert werden.  

- **Fehlkonfigurierte Policies:** Ungültige oder doppelte Policy-Zuweisungen dürfen nicht gespeichert werden.  

- **Massenänderungen:** Bulk-Zuweisungen oder -Entzüge müssen abgesichert und bestätigt werden.  

## Abhängigkeiten

-  – Stellt Middleware für Policy-Prüfungen bereit.  

-  – Policies werden beim Wechsel der aktiven Association neu geladen.  

-  – Alle Rollenänderungen und Policy-Zuweisungen werden revisionssicher aufgezeichnet.  

-  – Verwaltung der Benutzeridentitäten und Verknüpfung zu Rollen.  

## Offene Fragen

- Sollen vorkonfigurierte Policy-Sets für unterschiedliche Mandantengrößen (klein, mittel, groß) ausgeliefert werden?  

- Soll der Rolleneditor UI-seitig in Echtzeit (ohne Reload) Policies aktivieren/deaktivieren können?  

- Wie sollen Konflikte bei Mehrfachzuweisungen (z. B. Owner + Board) behandelt werden – additive oder priorisierte Rechte?  

## Zukunftserweiterungen

- Einführung von **ABAC (Attribute-Based Access Control)** mit dynamischen Kontextbedingungen.  

- Delegierte Administratorrollen mit zeitlich begrenzten Berechtigungen.  

- Scoped Roles für bestimmte Gebäude, Einheiten oder Zeiträume.  

- Automatische Rechtevergabe basierend auf Benutzerstatus oder Vertragsdaten.  

## Verknüpfte Tasks

- **WEG-210 – RBAC Model & Policy Guards** – Definiert das RBAC-Datenmodell und implementiert Guard-Middleware für API-Endpunkte.  

- **WEG-211 – Policy Attributes & Middleware** – Entwickelt Attribute und Middleware zur Policy-Prüfung in API und UI.  

- **WEG-212 – Role-based Menu Visibility** – Steuert die Sichtbarkeit von Menüs und Funktionen anhand von Policies.  

- **WEG-213 – Seed Roles per Association** – Erstellt Standardrollen und Policies beim Onboarding neuer WEGs.  

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

RBAC-Grundmodell mit vordefinierten Rollen (Manager, Board, Owner, Resident), Policy-Katalog, API- und UI-Integration, Audit-Logging für Rollenänderungen.

**Phase 2**

Erweiterte Rollenlogik mit delegierten Admins, ABAC-Grundlagen, Scoped Roles und Rollenversionierung.

**Phase 3**

Dynamische Policy-Ausdrücke, automatisierte Zuweisungen, Workflow-basierte Freigaben und vollständige Kontextsteuerung.