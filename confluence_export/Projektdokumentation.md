---
title: Projektdokumentation
confluence_id: 27853400
version: 3
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27853400/Projektdokumentation
---

## 1. Projektname & Zielsetzung
Das **WEG Management System (WMS)** ist eine moderne, cloudfähige Plattform zur digitalen Verwaltung von **Wohnungseigentümergemeinschaften (WEGs)**.  
Ziel ist es, **Verwaltern, Beiräten und Eigentümern** eine zentrale Lösung zu bieten, mit der sie sämtliche Verwaltungs-, Kommunikations- und Abrechnungsprozesse effizient, transparent und rechtssicher abwickeln können.

Das System soll:

- die Verwaltung vollständig digital abbilden (vom Eigentümer bis zum Wirtschaftsplan),

- manuelle Prozesse automatisieren (Abrechnungen, Fristen, Protokolle, Mitteilungen),

- nachvollziehbare, revisionssichere Abläufe schaffen,

- und durch Modularität schrittweise erweitert werden können.

Der Fokus liegt dabei auf **Bedienbarkeit, Rechtssicherheit, Nachvollziehbarkeit und Skalierbarkeit** – von kleinen Eigentümergemeinschaften bis hin zu professionellen Hausverwaltungen.

## 2. Produktvision
WMS steht für eine **neue Generation der digitalen WEG-Verwaltung**.  
Während klassische Systeme auf reine Datenspeicherung setzen, verfolgt WMS das Ziel, ein **intelligentes, vernetztes Verwaltungssystem** zu schaffen, das Prozesse versteht und unterstützt, statt sie nur abzubilden.

**Kernaspekte der Vision:**

- **Transparente Verwaltung:** Jede Änderung ist nachvollziehbar, jede Aktion revisionssicher dokumentiert.  

- **Vernetzte Abläufe:** Module greifen ineinander – Beschlüsse erzeugen Aufgaben, Verträge erzeugen Fristen, Zählerstände erzeugen Abrechnungen.  

- **Automatisierte Routine:** Wiederkehrende Aufgaben laufen zeitgesteuert (Scheduler), ohne manuelle Eingriffe.  

- **Rechtssicher & DSGVO-konform:** Datenschutz, Zugriffstrennung und Audit-Trails sind integraler Bestandteil.  

- **Intuitive Nutzung:** Klare Rollen und ein moderner, reaktiver Web-Client ermöglichen eine Bedienung ohne technische Hürden.  

- **Zukunftsorientiert:** Erweiterbar für IoT-Geräte, KI-gestützte Analysen und mobile Nutzung.

## 3. Architekturprinzipien (vereinfacht dargestellt)
WMS ist modular aufgebaut.  
Jedes Hauptmodul (WEG-1 bis WEG-9) bildet einen klar abgegrenzten Geschäftsbereich ab und enthält Untermodule für spezifische Funktionen.

**Grundprinzipien:**

- **Mandantenfähig:** Jede WEG ist ein eigener Mandant mit eigenem Datenbereich (Schema).  

- **Lose Kopplung:** Module kommunizieren über standardisierte Schnittstellen.  

- **Rollenbasiert:** Zugriff und Aktionen richten sich strikt nach der Rolle (Verwalter, Beirat, Eigentümer, Bewohner).  

- **Erweiterbar:** Neue Module oder Integrationen können ohne Systembruch ergänzt werden.  

- **Stabil & Sicher:** Scheduler, Logging, Observability und Health-Monitoring sind integraler Bestandteil.  

- **Mehrsprachig:** Englische und deutsche Oberfläche für flexible Nutzung.

## 4. Produkt-Roadmap
### Phase 1 – Foundation & MVP (Aktuelle Umsetzungsphase)
**Ziel:**  
Ein vollständiges, betriebsfähiges System, mit dem eine reale WEG komplett digital verwaltet werden kann – von Eigentümerdaten über Zählerstände bis hin zu Jahresabrechnungen und Beschlüssen.

**Umfang (Module & Funktionen):**

- **WEG-1:** Platform Foundation (inkl. Logging, Scheduler, CI, Feature-Flags, Internationalisierung)

- **WEG-2:** Identity & Access (Authentifizierung, Rollenmodell, GDPR-Basis)

- **WEG-3:** Tenant Provisioning & Admin (Mandantenverwaltung, Backup/Restore, Migration)

- **WEG-4:** Property & People (Gebäude, Einheiten, Eigentümer, Bewohner, Beirat)

- **WEG-5:** Document Management & Templates (DMS, Vorlagen, Verträge, Branding)

- **WEG-6:** Messaging & Notifications (Nachrichten, Benachrichtigungen, Community Board)

- **WEG-7:** Metering (Zählerverwaltung, Hierarchien, Lesekampagnen, Sperrperioden)

- **WEG-8:** Finance & Banking (Buchungen, MT940-Import, Wirtschaftsplan, Abrechnung)

- **WEG-9:** Meetings & Resolutions (Versammlungen, Abstimmungen, Protokolle, Ticketing)

**Ergebnis:**  
Das System ist vollständig funktionsfähig, ermöglicht die operative Verwaltung einer WEG inkl. Dokumentation, Kommunikation, Abrechnung und Beschlussumsetzung.

### Phase 2 – Erweiterung & Integration
**Ziel:**  
Automatisierung, Sicherheit, Integrationen und Smart-Home-Anbindung.

**Inhalte:**

- **Erweiterte DSGVO-Mechanismen:** Vollständige Datenanonymisierung, Löschprozesse, Rechtsgrundlagen-Nachweis  

- **Erweiterte Banking-Anbindungen:** PSD2, SEPA-Automatisierung, Bank-API-Integrationen  

- **IoT & Smart Metering:** Anbindung von intelligenten Verbrauchszählern, Sensoren und Gebäudetechnik  

- **System- und Prozessüberwachung:** Observability-Dashboard, Job-Monitoring, Fehlerbenachrichtigungen  

- **Erweiterte Automatisierung:** Vertragslaufzeiten, Fristen und Aufgabenmanagement  

- **Sicherheitsoptimierung:** Audit-Erweiterungen, Verschlüsselung, erweiterte Rechteverwaltung  

**Zielbild:**  
Vollständig automatisierte und geprüfte Abläufe mit hoher Datensicherheit und Integration in externe Systeme.

### Phase 3 – Zukunft & KI
**Ziel:**  
Intelligente Verwaltung, mobile Nutzung und vorausschauende Assistenzfunktionen.

**Inhalte:**

- **Mobile & Offline-Clients:** App-Integration für Eigentümer und Verwalter  

- **Online-Versammlungen:** Abstimmungen und Beschlussfassungen digital und hybrid  

- **KI-gestützte Analysen:** Prognosen für Rücklagen, Verbrauch, Zahlungsausfälle  

- **Automatische Protokoll- und Dokumentenerstellung:** KI-gestützte Textbausteine und Zusammenfassungen  

- **Chatbots & Assistenten:** Direkte Kommunikation für Eigentümeranfragen  

- **Predictive Maintenance:** Früherkennung von Anomalien bei Energie- oder Verbrauchsdaten  

- **Erweiterte Workflows:** Prozessautomatisierung zwischen Modulen (Vertrag &rarr; Beschluss &rarr; Zahlung)

**Zielbild:**  
WMS entwickelt sich von einem Verwaltungssystem zu einer **intelligenten, selbststeuernden Plattform** für digitale Immobilienverwaltung.

## 5. Funktionsübersicht (WEG-1 bis WEG-9)
**Modul**

**Beschreibung**

**WEG-1 – Platform Foundation** 

Basisplattform mit Infrastruktur, API-Gateway, Logging, Scheduler, Feature-Flags und internationaler Mehrsprachigkeit. Sorgt für Stabilität, Sicherheit und Erweiterbarkeit. 

**WEG-2 – Identity & Access** 

Authentifizierung, Rollen- und Rechteverwaltung, Profilverwaltung und Datenschutzgrundlagen (GDPR). Ermöglicht sichere Mehrmandantenumgebungen. 

**WEG-3 – Tenant Provisioning & Admin** 

Verwaltung aller WEG-Mandanten über ein zentrales Directory. Enthält Onboarding, Backup, Branding, Export und Migration. 

**WEG-4 – Property & People** 

Verwaltung von Gebäuden, Einheiten, Eigentümern, Bewohnern und Beiräten. Enthält zeitgebundene Besitzverhältnisse, MEA-Verteilungen und CSV-Import. 

**WEG-5 – Document Management & Templates** 

DMS mit Versionierung, Berechtigungen, Vorlagen und Branding. Integriert Vertragsverwaltung, Retention Policies und automatische PDF-Erstellung. 

**WEG-6 – Messaging & Notifications** 

Interne Kommunikation mit Nachrichten-Threads, Anhängen, Community-Board und zentralem Benachrichtigungscenter. Verschlüsselt und revisionssicher. 

**WEG-7 – Metering** 

Erfassung, Verwaltung und Auswertung von Zählerständen. Unterstützt manuelle Eingaben, Hierarchien, Ersatzgeräte, Lesekampagnen und Sperrperioden. 

**WEG-8 – Finance & Banking** 

Verwaltung der Finanzströme: Konten, Buchungen, MT940-Import, Abrechnungen, Budgetplanung und Exporte. Enthält Umlageschlüssel, Wirtschaftsplan, Eigentümerkonten und Audit-Trail. 

**WEG-9 – Meetings & Resolutions** 

Digitale Eigentümerversammlungen mit Agenda, Abstimmung, Protokollierung, Beschlussarchiv und Ticket-Verknüpfungen. Ermöglicht revisionssichere Beschlussfassung. 

## 6. Abhängigkeiten & Zusammenspiel
WMS basiert auf einem **klar definierten Zusammenspiel der Module**.  
Zentrale Ereignisse (&bdquo;Events&ldquo;) verbinden die Geschäftsprozesse:  

Beispiele:  

- Wenn ein **Vertrag ausläuft (WEG-57)** &rarr; wird automatisch eine **Benachrichtigung (WEG-6)** erstellt &rarr; ein **TOP in einer Versammlung (WEG-9)** vorgeschlagen &rarr; und bei Beschluss automatisch im **Wirtschaftsplan (WEG-8)** berücksichtigt.  

- Ein neuer **Eigentümer (WEG-4)** erhält automatisiert **Zugriffsdaten (WEG-2)** und relevante **Dokumente (WEG-5)**.  

- Ein **Zählerwechsel (WEG-7)** führt automatisch zu einem Hinweis im **Abrechnungssystem (WEG-8)**.  

Diese Event-Kaskaden ermöglichen konsistente, nachvollziehbare Prozesse über alle Module hinweg.

## 7. Fazit / Zielbild
Das **WEG Management System (WMS)** definiert die digitale Immobilienverwaltung neu.  
Es ist **modular, skalierbar, sicher** und bereits in der ersten Version fähig, eine gesamte WEG vollständig digital zu führen – vom Eigentümer bis zum Wirtschaftsplan.  

Mit jeder Ausbaustufe wird WMS intelligenter, automatisierter und stärker vernetzt:  

- Phase 1 schafft die Basis,  

- Phase 2 optimiert und integriert,  

- Phase 3 macht die Verwaltung vorausschauend und intelligent.  

**Langfristige Vision:**  

Eine Plattform, die Verwaltung nicht nur digitalisiert, sondern versteht –  
Entscheidungen vorbereitet, Prozesse automatisiert und Eigentümern wie Verwaltern Zeit und Aufwand spart.