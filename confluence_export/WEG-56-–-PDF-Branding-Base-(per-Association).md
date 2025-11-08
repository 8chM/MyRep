---
title: WEG-56 – PDF Branding Base (per Association)
confluence_id: 27591414
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27591414/WEG-56+PDF+Branding+Base+per+Association
---

**JIRA-Link:** [WEG-56 – PDF Branding Base (per Association)](https://maierharry.atlassian.net/browse/WEG-56)

## Überblick

Das Modul **PDF Branding Base (per Association)** (WEG-56) stellt sicher, dass alle automatisch erzeugten PDF-Dokumente einheitlich gestaltet und mit dem Corporate Branding der jeweiligen WEG versehen werden. Branding umfasst die konsistente Verwendung von Logo, Farben, Schriftarten, Kopf- und Fußzeilen sowie optionaler Wasserzeichen. Ziel ist es, dass jedes Dokument – unabhängig vom Typ oder Erstellungsprozess – optisch der Identität der jeweiligen WEG entspricht und rechtlich wie visuell professionell auftritt.

## Beschreibung

Dieses Untermodul erweitert die **Template Engine (WEG-53)** um eine Branding-Schicht, die bei jeder PDF-Erstellung angewendet wird. Das Branding wird mandantenspezifisch konfiguriert und kann zentral über das Administrator-Interface gepflegt werden. Es gilt für alle automatisch erzeugten Dokumente wie Abrechnungen, Verträge, Protokolle und Mitteilungen.

Hauptfunktionen:

- **Mandantenspezifische Branding-Einstellungen:** Jede WEG kann ihr eigenes Logo, ihre Primär- und Sekundärfarben, Schriftart und Layoutdefinitionen (z. B. Kopf-/Fußzeile) hinterlegen.

- **Versionierung & Historie:** Änderungen am Branding werden versioniert gespeichert, sodass frühere Dokumente ihr ursprüngliches Erscheinungsbild behalten.

- **Template-Integration:** Branding wird automatisch bei jeder Template-Ausgabe angewendet – unabhängig davon, ob es sich um ein Systemtemplate oder eine benutzerdefinierte Vorlage handelt.

- **Standard-Layouts:** Neben individuellem Branding stehen Standard-Layouts (&bdquo;Classic&ldquo;, &bdquo;Modern&ldquo;) zur Verfügung, falls keine WEG-spezifischen Einstellungen vorhanden sind.

- **Scheduler-Reminder:** Das System überprüft regelmäßig, ob neu angelegte WEGs ein Branding hinterlegt haben, und erinnert Administrator:innen automatisch an die Einrichtung.

- **PDF-Metadaten:** Jedes Branding kann Metadaten wie Erstellungsdatum, Copyright und Kontaktinformationen enthalten, die automatisch im PDF-Footer erscheinen.

## Geschäftsregeln & Logik

- Branding-Einstellungen sind pro WEG eindeutig und gelten systemweit.

- Änderungen erzeugen automatisch eine neue Version, um konsistente Archivierung und Nachvollziehbarkeit zu gewährleisten.

- Wenn kein Branding hinterlegt ist, wird ein Standardlayout verwendet.

- Das Branding kann ausschließlich von Administrator:innen mit entsprechender Berechtigung (WEG-2 – RBAC) geändert werden.

- Alle Branding-bezogenen Aktionen (Erstellung, Änderung, Löschung) werden im Audit-Log (WEG-24) dokumentiert.

## Akzeptanzkriterien

- **Gegeben** eine WEG hat ein individuelles Branding hinterlegt &rarr; **Wenn** ein Dokument generiert wird &rarr; **Dann** wird das definierte Branding vollständig (Logo, Farben, Layout) angewendet.

- **Gegeben** eine neue WEG wird angelegt &rarr; **Wenn** kein Branding definiert wurde &rarr; **Dann** erinnert der Scheduler automatisch an das Anlegen der Branding-Vorlage.

- **Gegeben** ein Administrator aktualisiert das Branding &rarr; **Wenn** die Änderung gespeichert wird &rarr; **Dann** wird eine neue Version erzeugt und im Audit-Log dokumentiert.

- **Gegeben** ein Dokument aus einer älteren Periode wird geöffnet &rarr; **Wenn** es mit einem älteren Branding erstellt wurde &rarr; **Dann** bleibt das ursprüngliche Layout erhalten.

- **Gegeben** keine Branding-Daten sind vorhanden &rarr; **Wenn** ein Dokument erzeugt wird &rarr; **Dann** verwendet das System automatisch das Standard-Layout.

## Nicht-Ziele

- Kein interaktiver PDF-Designer im MVP.

- Keine dynamische Farbänderung basierend auf Dokumenttyp.

- Keine mehrsprachige Branding-Unterstützung (kommt erst mit WEG-15 – Internationalization).

## Kritische Fälle

- **Fehlendes Branding:** Wenn kein Branding definiert wurde, darf kein Dokument ohne Layout erzeugt werden; stattdessen muss das Standardlayout greifen.

- **Defekte Branding-Vorlagen:** Fehlerhafte oder unvollständige Branding-Daten dürfen keine PDF-Erstellung verhindern – es wird automatisch auf das Standardlayout zurückgefallen.

- **Versionskonflikte:** Gleichzeitige Änderungen durch mehrere Administratoren müssen gesperrt oder durch Versionskontrolle verhindert werden.

- **Kompatibilitätsprobleme:** Branding darf keine Darstellungsfehler bei Templates oder DMS-Vorschauen verursachen.

## Abhängigkeiten

-  – Speicherung und Versionierung der erzeugten PDF-Dokumente.

-  – Anwendung der Branding-Schicht auf alle generierten Templates.

-  – Erfassung und Behandlung von Fehlern während der PDF-Erzeugung.

-  – Nachvollziehbarkeit aller Änderungen an Branding-Definitionen.

-  – Scheduler und Konfigurationsverwaltung für Branding-Überwachung.

## Offene Fragen

- Soll es möglich sein, mehrere Branding-Profile pro WEG zu verwalten (z. B. für verschiedene Objekte oder Abteilungen)?

- Soll Branding auf andere Dokumenttypen (z. B. HTML, DOCX) erweitert werden?

- Soll ein Live-Vorschau-Modus im Admin-Interface bereitgestellt werden?

## Zukunftserweiterungen

- **Multi-Layout-Unterstützung:** Verschiedene Layout-Stile pro WEG auswählbar.

- **Dynamisches Branding:** Anpassung des Layouts je nach Dokumenttyp (z. B. Protokoll vs. Abrechnung).

- **Template-Vorschau:** Live-Preview des Brandings in der Template Engine.

- **Externe Brand-Imports:** Möglichkeit, Corporate-Design-Vorgaben per ZIP-/JSON-Datei zu importieren.

## Verknüpfte Tasks

- [WEG-560 – Branding Base per Association](https://maierharry.atlassian.net/browse/WEG-560) – Grundlegende Implementierung des Branding-Mechanismus pro WEG.

- [WEG-561 – Branding Version Control & Audit Hooks](https://maierharry.atlassian.net/browse/WEG-561) – Versionierung und Audit-Integration für Branding-Änderungen.

- [WEG-562 – Default Branding Templates](https://maierharry.atlassian.net/browse/WEG-562) – Bereitstellung von Standard-Layouts und -Vorlagen.

- [WEG-563 – Scheduler Reminder](https://maierharry.atlassian.net/browse/WEG-563) – Erinnerung an fehlendes Branding bei neuen Mandanten.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Mandantenspezifisches Branding (Logo, Farben, Schriftarten), Standardlayout, automatische Anwendung über Template Engine, Scheduler-Reminder für fehlendes Branding.

**Phase 2**

Multi-Layout-Unterstützung, erweiterte Versionierung, Live-Vorschau im Admin-Interface.

**Phase 3**

Dynamisches Branding je Dokumenttyp, Import/Export von Branding-Profilen, Integration mit externen Designsystemen.