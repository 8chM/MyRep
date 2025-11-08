---
title: WEG-12 – Error Handling, Logging & Health
confluence_id: 27329245
version: 15
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329245/WEG-12+Error+Handling+Logging+Health
---

**JIRA-Link:** [WEG-12 – Error Handling, Logging & Health](https://maierharry.atlassian.net/browse/WEG-12)

## Überblick

Das Modul **Error Handling, Logging & Health** (WEG-12) bildet das Rückgrat der technischen Stabilität im WEG Management System.
Es sorgt für eine einheitliche Behandlung von Fehlern, eine strukturierte Protokollierung aller Ereignisse und eine kontinuierliche Überwachung der Systemgesundheit.
Ziel ist es, eine robuste Grundlage zu schaffen, die frühzeitig auf Störungen reagiert, klare Ursachenanalysen ermöglicht und die Wartbarkeit sowie Zuverlässigkeit der Plattform sicherstellt.

## Beschreibung

WEG-12 stellt zentrale Mechanismen für Fehlermanagement, Logging, Health Checks und Hintergrundprozesse bereit.
Diese Komponenten arbeiten übergreifend über alle Module hinweg und gewährleisten, dass das System transparent, nachvollziehbar und fehlertolerant funktioniert.

Hauptfunktionen:

- **Error Handling:** Einheitliche Fehlerverarbeitung durch Middleware; alle Exceptions werden in standardisierte ProblemDetails-Antworten umgewandelt.

- **Structured Logging:** JSON-basierte, korrelierbare Logs mit eindeutiger Request-ID (x-request-id); Integration mit Audit-Systemen.

- **Health Checks:** Standardisierte Endpunkte (/healthz, /readyz), die kritische Subsysteme wie Datenbank, Directory oder Scheduler prüfen.

- **Background Jobs & Scheduler:** Verwaltung zeitgesteuerter Aufgaben (Cron/Interval) mit Retry-Logik, Persistenz und Statusüberwachung.

- **Job Dashboard & Metrics:** Übersicht über alle aktiven und fehlgeschlagenen Systemjobs, inklusive Laufzeiten und Fehlerhistorie.

- **Notification Hooks:** Weiterleitung kritischer Systemfehler an das Notification Center (WEG-6).

- **Audit Integration:** Alle Log-Einträge und Fehler werden revisionssicher mit Audit-IDs (WEG-24) verknüpft.

## Geschäftsregeln & Logik

- Jede Exception wird durch die zentrale Middleware abgefangen und als ProblemDetails-Objekt zurückgegeben.

- Logs müssen vollständig, JSON-formatiert und mit Correlation-ID versehen sein.

- Health Checks prüfen ausschließlich Erreichbarkeit und Status, dürfen aber nicht blockierend wirken.

- Hintergrundjobs werden persistent gespeichert; fehlgeschlagene Jobs werden automatisch neu eingeplant.

- Scheduler unterstützt Wiederholungsstrategien (Retry-Policies) für kritische Aufgaben.

- Wiederkehrende Fehler führen zu automatischen Eskalationen über das Notification Center.

- Kritische Ausfälle (z. B. Datenbank-Fehler) versetzen das System in einen Readiness-Failure-Zustand.

## Akzeptanzkriterien

- **Gegeben:** eine Exception tritt während eines API-Calls auf &rarr; **Wenn:** sie von der Middleware verarbeitet wird &rarr; **Dann:** wird sie als ProblemDetails-Response mit Fehler-ID, Nachricht und Statuscode zurückgegeben.

- **Gegeben:** ein Request enthält eine Correlation-ID &rarr; **Wenn:** der Request abgeschlossen ist &rarr; **Dann:** erscheint diese ID in allen zugehörigen Log-Einträgen.

- **Gegeben:** ein Service ist nicht erreichbar &rarr; **Wenn:** der Health-Check ausgeführt wird &rarr; **Dann:** liefert /readyz den Status &bdquo;unhealthy&ldquo; mit Ursache.

- **Gegeben:** ein Background Job schlägt wiederholt fehl &rarr; **Wenn:** die maximale Retry-Grenze erreicht ist &rarr; **Dann:** wird ein Alarm im Notification Center ausgelöst.

- **Gegeben:** ein Administrator öffnet das Job-Dashboard &rarr; **Wenn:** ein Job blockiert ist &rarr; **Dann:** wird er mit Status &bdquo;stuck&ldquo; und Zeitstempel angezeigt.

## Nicht-Ziele

- Keine externe Monitoring-Integration (z. B. Grafana, ELK) im MVP.

- Kein automatisches Self-Healing oder Neustart von Diensten.

- Keine vollumfängliche Log-Analyse oder Textsuche im MVP.

- Keine historische Trendanalyse über Systemmetriken.

## Kritische Fälle

- **Unbehandelte Exceptions:** Das System muss in einen definierten Fehlerzustand wechseln, falls Ausnahmen nicht korrekt behandelt werden.

- **Log-Verlust:** Fehler bei Speicherung oder Rotation von Logs führen zu Lücken im Audit-Trail.

- **Scheduler Deadlocks:** Hintergrundjobs dürfen sich nicht gegenseitig blockieren; Deadlock-Erkennung erforderlich.

- **Health-Check-Latenz:** Zu lange Prüfzeiten können fehlerhafte Systemalarme auslösen.

- **Fehlende Correlation-ID:** Ohne eindeutige ID ist keine lückenlose Nachvollziehbarkeit möglich.

## Abhängigkeiten

- WEG-1 – Platform Foundation Basis für Middleware, Logging und Health-Mechanismen.

- WEG-6 – In-App Notifications Nutzung für Eskalationen bei kritischen Fehlern.

- WEG-24 – Audit Log Speicherung und Nachvollziehbarkeit aller Fehlerereignisse.

- WEG-57 – Contract Management Nutzung von Scheduler-Funktionen für Vertragsfristen.

- WEG-87 – Accounting &amp; Billing Verwendung zeitgesteuerter Prozesse zur Abrechnung.

## Offene Fragen

- Soll das Dashboard die Möglichkeit bieten, Jobs manuell neu zu starten?

- Welche Fehlerstufen sollen aktiv eskaliert werden (Critical, Warning, Info)?

- Soll ein einheitliches Fehlercode-Schema systemweit eingeführt werden?

## Zukunftserweiterungen

- **Feature:** Observability Integration – Verbindung zu externen Monitoring-Systemen (z. B. Grafana, Prometheus).

- **Feature:** Fehleranalyse & Priorisierung – Automatische Klassifizierung und Bewertung von Ursachen.

- **Feature:** Self-Healing – Automatische Neustarts und Wiederherstellung fehlerhafter Komponenten.

- **Feature:** Realtime-Dashboard – Erweiterte Visualisierung von Logs, Jobs und Systemmetriken.

## Verknüpfte Tasks

- [WEG-120 – ProblemDetails Middleware & Validation Mapping](https://maierharry.atlassian.net/browse/WEG-120) – Einheitliche Fehlerbehandlung in API-Schicht.

- [WEG-121 – Serilog JSON Logs + x-request-id Correlation](https://maierharry.atlassian.net/browse/WEG-121) – Strukturierte Log-Erfassung und Korrelation.

- [WEG-122 – /healthz & /readyz (DB/Directory Checks)](https://maierharry.atlassian.net/browse/WEG-122) – Health-Endpunkte zur Systemüberwachung.

- [WEG-123 – Log Context Enricher (User/Association/Schema)](https://maierharry.atlassian.net/browse/WEG-123) – Kontextbezogene Log-Erweiterung.

- [WEG-124 – Background Job Host & Persistence](https://maierharry.atlassian.net/browse/WEG-124) – Verwaltung von Hintergrundprozessen.

- [WEG-125 – Job Scheduling (Cron/Interval) & Retry Policies](https://maierharry.atlassian.net/browse/WEG-125) – Automatische Wiederholungsstrategien.

- [WEG-126 – Job Dashboard & Health (/jobs, metrics)](https://maierharry.atlassian.net/browse/WEG-126) – Übersicht und Monitoring von Systemjobs.

- [WEG-127 – System Jobs: Token Cleanup (Auth)](https://maierharry.atlassian.net/browse/WEG-127) – Wartungsprozesse für Authentifizierungsdaten.

- [WEG-128 – Domain Jobs: Contract Deadline Reminders](https://maierharry.atlassian.net/browse/WEG-128) – Automatische Erinnerungen für Vertragsfristen.

- [WEG-129 – Domain Jobs: Metering & Accounting Period Notifications](https://maierharry.atlassian.net/browse/WEG-129) – Automatische Hinweise zu Abrechnungsperioden.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Einheitliches Error-Handling (ProblemDetails), JSON-Logging mit Correlation-ID, Health-/Readiness-Checks, Scheduler mit Background Jobs und Dashboard-Basis.

**Phase 2**

Erweiterter Scheduler mit Retry-Analytics, Notification-Hooks für kritische Fehler und Integration in Audit-Reports.

**Phase 3**

Vollständige Observability (Metrics, Logs, Traces), Self-Healing-Mechanismen und Realtime-Dashboards mit Analysefunktionen.