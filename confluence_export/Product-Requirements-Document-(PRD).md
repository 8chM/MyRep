---
title: Product Requirements Document (PRD)
confluence_id: 36044827
version: 1
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/36044827/Product+Requirements+Document+PRD
---

## Projekt: WEG Management System (WMS)
### 1. Einleitung
Das **WEG Management System (WMS)** ist eine zentrale, modulare Plattform zur digitalen Verwaltung von **Wohnungseigentümergemeinschaften (WEGs)**.  
Es digitalisiert alle Kernprozesse der Immobilienverwaltung – von der Stammdatenpflege über Kommunikation, Dokumentation und Finanzen bis hin zu Eigentümerversammlungen, Beschlussfassungen und Abrechnungen.

**Zielgruppen:**

- **WEG-Verwalter**, die komplexe Verwaltungsaufgaben effizient und rechtssicher digital abbilden möchten.  

- **Beiräte**, die Vorgänge und Entscheidungen nachvollziehen, prüfen und freigeben.  

- **Eigentümer**, die Transparenz über Kosten, Dokumente, Beschlüsse und laufende Vorgänge wünschen.  

- **Bewohner**, die Informationen einsehen, Anliegen melden und an Kommunikationsprozessen teilnehmen.  

**Hintergrund:**  
Traditionelle WEG-Verwaltungssysteme sind häufig unflexibel, technisch veraltet und nur auf wenige Prozesse spezialisiert.  
WMS schließt diese Lücke durch eine **mandantenfähige, moderne und modulare Architektur**, die sowohl kleine Eigentümergemeinschaften als auch große Hausverwaltungen abbildet.  
Das System ersetzt isolierte Insellösungen und vereint alle Verwaltungsbereiche auf einer gemeinsamen Plattform mit klarer Rollen- und Rechteverwaltung.

### 2. Ziele und Nutzen
#### Hauptziele
- **Zentralisierung aller Verwaltungsprozesse**  
Alle relevanten Daten, Dokumente und Prozesse einer WEG werden in einem System zusammengeführt – von Eigentümerinformationen über Vertragsdetails bis hin zu Abrechnungen und Beschlüssen.  

- **Automatisierung von Routineaufgaben**  
Das System übernimmt wiederkehrende Tätigkeiten wie Fristenüberwachung, Vertragslaufzeiten, Erinnerungen, Verbrauchserfassung oder die Generierung von Standarddokumenten.  

- **Rechtssicherheit und Nachvollziehbarkeit**  
Jede Aktion, Änderung und Entscheidung wird automatisch dokumentiert. Alle Abläufe sind auditierbar, revisionssicher und DSGVO-konform.  

- **Transparenz und Vertrauen**  
Eigentümer, Beiräte und Verwalter greifen auf dieselben Daten zu – mit klar definierten Rechten, transparenten Entscheidungswegen und stets nachvollziehbarer Historie.  

- **Skalierbarkeit und Modularität**  
Durch den modularen Aufbau kann das System je nach Bedarf erweitert werden – von der Basisverwaltung bis hin zu IoT- und KI-gestützten Erweiterungen.  

#### Sekundäre Ziele
- Einheitliches, benutzerfreundliches Interface mit klarer Struktur und Mehrsprachigkeit.  

- Vollständige Digitalisierung der Abläufe – keine papierbasierten oder parallelen Systeme notwendig.  

- Reduktion von Kommunikationsaufwand durch interne Messaging- und Benachrichtigungsfunktionen.  

- Grundlage für langfristige Erweiterungen wie Smart-Meter-Integration, Banking-APIs oder mobile Apps.

### 3. Produktumfang (Scope)
WMS besteht aus **neun Hauptmodulen (WEG-1 bis WEG-9)**, die alle wesentlichen Verwaltungsfunktionen einer WEG abbilden.  
Jedes Modul ist unabhängig, aber eng mit den anderen Bereichen integriert.  
Alle Daten und Prozesse basieren auf einem einheitlichen, mandantenfähigen Datenmodell.  
Eine &bdquo;Mandanteneinheit&ldquo; entspricht einer WEG mit eigenen Benutzern, Daten, Dokumenten und Konfigurationen.

Das **MVP (Phase 1)** deckt den vollständigen Funktionsumfang ab, um eine reale WEG digital zu führen.  
Weitere Phasen erweitern den Automatisierungs- und Integrationsgrad.

### 4. Kernmodule und Aufgaben
#### **WEG-1 – Platform Foundation**
Das Fundament des Systems.  
Dieses Modul stellt die technische und organisatorische Grundlage bereit, auf der alle weiteren Komponenten aufbauen.  
Es umfasst Logging, Fehlerbehandlung, Scheduler, Health-Checks, Feature-Flags, Internationalisierung und Basis-Konfiguration.  

**Funktionen und Aufgaben:**

- Zentrale Fehlerbehandlung mit standardisierten Rückmeldungen und Problemobjekten.  

- Vollständige Protokollierung von Systemereignissen mit Korrelations-IDs.  

- Scheduler-Dienst zur zeit- und ereignisbasierten Ausführung von Aufgaben (z. B. Fristbenachrichtigungen, Datenprüfungen).  

- Status- und Health-Monitoring für Systemdienste.  

- Feature-Flag-Verwaltung, um Funktionen mandantenabhängig zu aktivieren oder zu deaktivieren.  

- Unterstützung mehrerer Sprachen (DE/EN) und regionsspezifischer Formate.  

**Ziel:**  
Ein stabiles, erweiterbares Fundament, das Sicherheit, Skalierbarkeit und Transparenz gewährleistet.

#### **WEG-2 – Identity & Access**
Regelt alle Zugriffs- und Berechtigungsmechanismen.  
Jeder Nutzer besitzt ein persönliches Konto mit zugewiesener Rolle (z. B. Verwalter, Beirat, Eigentümer, Bewohner).  
Das Modul umfasst Authentifizierung, Autorisierung, Datenschutz und Audit-Logging.

**Funktionen:**

- Benutzerregistrierung und Authentifizierung über moderne Standards.  

- Rollenkonzept (RBAC) mit granularer Berechtigungskontrolle je WEG.  

- DSGVO-Funktionen: Datenexport, Löschprozesse, Pseudonymisierung und Redaktionslogik.  

- Sicherheitsrichtlinien (Passwort-Policy, Session-Timeouts, Token-Rotation).  

- Audit-Protokoll für Benutzeraktionen und Konfigurationsänderungen.  

**Ziel:**  
Sichere, nachvollziehbare und datenschutzkonforme Verwaltung aller Nutzer und Zugriffe.

#### **WEG-3 – Tenant Provisioning & Administration**
Dieses Modul verwaltet die Mandantenstruktur.  
Jede WEG wird als eigene logische Einheit (Schema) innerhalb des Systems betrieben.  
Admins können Mandanten erstellen, aktivieren, sichern, wiederherstellen oder exportieren.

**Funktionen:**

- Automatisierte Erstellung neuer WEG-Mandanten mit Initialdaten.  

- Zentrale Übersicht über alle aktiven WEGs.  

- Backup- und Restore-Mechanismen.  

- Konfigurationsverwaltung (Branding, Sprache, Einstellungen).  

- Daten- und Schemaexporte (z. B. JSON, CSV).  

- Migrationstools und Health-Checks zur Sicherstellung der Datenintegrität.  

**Ziel:**  
Effiziente, nachvollziehbare Verwaltung mehrerer WEGs innerhalb eines zentralen Systems.

#### **WEG-4 – Property & People**
Das zentrale Modul für Stammdaten.  
Es bildet die reale und rechtliche Struktur der WEG ab – von Gebäuden über Einheiten bis zu Eigentümern, Bewohnern und Beiräten.

**Funktionen:**

- Erfassung von Gebäuden, Einheiten, Eigentümern und Bewohnern.  

- Verwaltung von Besitz- und Nutzungsverhältnissen über Zeiträume.  

- Erfassung von MEA-, Flächen- und Adressdaten.  

- CSV-Import und Validierung bestehender Daten.  

- Integration eines Beiratsmodells (Advisory Board) für Freigaben und Prüfungen.  

- Such-, Filter- und Verknüpfungsfunktionen zu Dokumenten, Verträgen und Finanzen.  

**Ziel:**  
Eine konsistente, verlässliche Datenbasis für alle weiteren Prozesse.

#### **WEG-5 – Document Management & Templates**
Das DMS ist das Archiv und die Kommunikationsschnittstelle des Systems.  
Es verwaltet alle Dateien, Vorlagen und Protokolle mit vollständiger Versionierung und Berechtigungssteuerung.

**Funktionen:**

- Upload, Versionierung, Klassifizierung und Freigabe von Dokumenten.  

- Verknüpfung mit Objekten (Einheiten, Verträgen, Beschlüssen).  

- Template-Engine für standardisierte Dokumente (z. B. Abrechnungen, Protokolle, Briefe).  

- Automatische Branding-Vorlagen pro WEG.  

- Archivierungs- und Retention-Regeln (keine Löschung ohne Archiv).  

- ZIP-Export und Vorschaufunktionen.  

**Ziel:**  
Revisionssichere Dokumentenverwaltung und standardisierte, automatisierte Dokumentenerstellung.

#### **WEG-6 – In-App Messaging & Notifications**
Dieses Modul bündelt alle Kommunikationsprozesse.  
Es reduziert externe Kommunikationskanäle (z. B. E-Mail) und sorgt für Nachvollziehbarkeit und Transparenz.

**Funktionen:**

- Interne Nachrichten zwischen Eigentümern, Beiräten und Verwaltung.  

- Systemweite Benachrichtigungen über Fristen, Beschlüsse, Vertragsänderungen.  

- Thematische Threads mit Dateianhängen.  

- Community-Board für Ankündigungen, Diskussionen und Informationsaustausch.  

- Benachrichtigungscenter mit Priorisierung und Filterfunktionen.  

- Vollständige Protokollierung und Speicherung zur späteren Nachvollziehbarkeit.  

**Ziel:**  
Vernetzte, transparente Kommunikation innerhalb der Gemeinschaft.

#### **WEG-7 – Metering**
Verwaltung und Erfassung sämtlicher Verbrauchszähler einer WEG.  
Das Modul deckt den gesamten Lebenszyklus eines Zählers ab – von der Installation bis zur Archivierung.

**Funktionen:**

- Verwaltung von Zählerarten (Strom, Wasser, Wärme, Gas).  

- Plausibilitätsprüfung und Validierung von Ablesungen.  

- Erfassung von manuellen Werten und Zählerwechseln.  

- Lesekampagnen mit Bulk-Erfassung.  

- Sperr- und Abschlussfunktionen für Abrechnungszeiträume.  

- Hierarchische Zuordnung (z. B. Haupt- und Unterzähler).  

**Ziel:**  
Zuverlässige, konsistente Verbrauchsdaten für die Finanzabrechnung.

#### **WEG-8 – Finance & Banking**
Das Finanzmodul bildet den Kern der wirtschaftlichen Verwaltung.  
Es ermöglicht die Verwaltung von Konten, Buchungen, Zuordnungen und Abrechnungen.

**Funktionen:**

- Verwaltung mehrerer Konten pro WEG.  

- Manuelle Buchungseingaben und Import über CSV/MT940.  

- Automatische Zuordnung zu Kostenarten und Umlageschlüsseln.  

- Erstellung von Wirtschaftsplänen und Jahresabrechnungen.  

- Verwaltung von Eigentümerkonten und offenen Posten.  

- Audit-Logging, Berichte und Exportfunktionen.  

**Ziel:**  
Nachvollziehbare, transparente Finanzverwaltung und revisionssichere Abrechnungsprozesse.

#### **WEG-9 – Meetings & Resolutions**
Dieses Modul digitalisiert den gesamten Ablauf von Eigentümerversammlungen.  
Von der Einladung über die Abstimmung bis hin zur Protokollierung und Umsetzung der Beschlüsse.

**Funktionen:**

- Erstellung und Verwaltung von Agenden, Teilnehmern und Vollmachten.  

- Digitale Abstimmung mit Quoren- und Mehrheitslogik.  

- Automatische Protokollerstellung und Archivierung.  

- Beschlussverfolgung mit Verknüpfung zu Aufgaben, Finanzen und Tickets.  

- Benachrichtigung der Teilnehmer über Ergebnisse und Maßnahmen.  

- Integration in das DMS zur revisionssicheren Dokumentation.  

**Ziel:**  
Effiziente, rechtssichere und nachvollziehbare Beschlussprozesse.

### 5. Nutzerrollen und Anwendungsfälle
**Rolle**

**Beschreibung**

**Beispiele für Nutzung**

**Verwalter** 

Hauptverantwortlicher der WEG 

Anlage neuer Gemeinschaften, Verwaltung von Finanzen, Erstellung von Abrechnungen, Verwaltung von Dokumenten 

**Beirat** 

Prüft, genehmigt und überwacht 

Einsicht in Abrechnungen, Freigabe von Beschlüssen, Prüfung von Budget und Verträgen 

**Eigentümer** 

Mitglied der Gemeinschaft 

Einsicht in Dokumente, Verbrauchsdaten und Beschlüsse, Teilnahme an Diskussionen 

**Bewohner** 

Nutzer der Einheiten 

Zugriff auf Mitteilungen, Mängelmeldung, Kommunikation mit Verwalter 

**Gast / Dienstleister** 

Externer Zugriff 

Erhalt und Bearbeitung bestimmter Dokumente oder Tickets innerhalb eines begrenzten Zeitraums 

### 6. Geschäftsregeln (übergreifend)
- Jede WEG ist eine geschlossene Einheit mit eigenen Daten, Dokumenten und Benutzern.  

- Aktionen erfordern gültige Berechtigungen, die durch Rollen definiert sind.  

- Änderungen werden vollständig protokolliert (Audit-Trail, Zeitstempel, Benutzerkontext).  

- Dokumente dürfen nur über Archivierungsmechanismen entfernt werden.  

- Scheduler-Jobs steuern alle wiederkehrenden Abläufe (Fristen, Erinnerungen, Abrechnungszyklen).  

- Datenschutzanforderungen werden systemweit technisch durchgesetzt.  

- Alle Module interagieren über einheitliche Ereignisse, um Prozesse zu automatisieren (z. B. Vertragsablauf &rarr; Beschluss &rarr; Abrechnung).  

### 7. Erfolgskriterien (KPIs)
- **50 % Reduktion** manueller Arbeitsschritte bei wiederkehrenden Prozessen.  

- **< 1 % Fehlerquote** bei Abrechnungen und Verbrauchsdaten.  

- **> 30 % Zeitersparnis** bei Eigentümerversammlungen und Dokumentenerstellung.  

- **&ge; 85 % Nutzerzufriedenheit** in Pilotphase.  

- Vollständige Revisions- und DSGVO-Konformität.  

- Erfolgreiche Verwaltung von mind. **10 WEGs parallel** im MVP-Betrieb.

### 8. Annahmen und Einschränkungen
- Der Betrieb erfolgt mandantenbasiert (eine WEG = ein Datenbereich).  

- System arbeitet ausschließlich online (kein Offline-Modus im MVP).  

- Externe Integrationen (SEPA, Signaturen, IoT) werden technisch vorbereitet, aber erst in Phase 2 umgesetzt.  

- Mobile Clients sind Teil von Phase 3.  

- Rechtliche Rahmenbedingungen (WEG-Gesetz, DSGVO, HGB) sind verbindlich.  

### 9. Zukunftsphasen und Erweiterungen
#### Phase 2 – Integration & Automatisierung
- Erweiterte DSGVO-Mechanismen (Löschprozesse, Anonymisierung, Datenkataloge).  

- Banking-APIs (PSD2, SEPA-Automatisierung).  

- IoT-Anbindungen für Smart-Meter-Daten.  

- Systemüberwachung (Observability-UI, Scheduler-Dashboard).  

- Erweiterte Audit- und Sicherheitsmechanismen.

#### Phase 3 – Smart & Intelligent Features
- Mobile Apps für Eigentümer und Verwalter.  

- KI-gestützte Abweichungs- und Prognoseanalysen.  

- Automatische Text- und Protokollerstellung.  

- Online-Eigentümerversammlungen und digitale Abstimmungen.  

- Chatbots und intelligente Suchfunktionen.  

### 10. Fazit
Das **WEG Management System (WMS)** bietet eine umfassende, modulare Lösung für die digitale Verwaltung von Wohnungseigentümergemeinschaften.  
Es kombiniert Effizienz, Transparenz und Rechtssicherheit in einer modernen, skalierbaren Plattform.  

Bereits in **Phase 1 (MVP)** kann eine komplette WEG operativ geführt werden – einschließlich Stammdaten, Kommunikation, Dokumentation, Finanzen und Beschlusswesen.  
Die späteren Phasen erweitern das System um Automatisierung, IoT-Integrationen und KI-gestützte Intelligenz.

**Dieses PRD dient als zentrale Grundlage** für die Planung, Priorisierung und Entwicklung aller Produktphasen und stellt sicher, dass das System den Anforderungen moderner WEG-Verwaltungen langfristig gerecht wird.