---
title: WEG-72 – Meter Lifecycle & Replacement
confluence_id: 27329388
version: 22
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329388/WEG-72+Meter+Lifecycle+Replacement
---

**JIRA-Link:** [WEG-72 – Meter Lifecycle & Replacement](https://maierharry.atlassian.net/browse/WEG-72)

## Überblick
Das Modul **Meter Lifecycle & Replacement** (WEG-72) verwaltet den vollständigen Lebenszyklus eines Zählers – von der Inbetriebnahme über Austausch und Defektbehandlung bis zur Stilllegung. Es stellt sicher, dass Verbrauchsdaten über den gesamten Zeitraum hinweg lückenlos erfasst und alle Wechselprozesse nachvollziehbar dokumentiert werden. Ziel ist es, Datenkonsistenz und Nachvollziehbarkeit in der Verbrauchshistorie sicherzustellen und gleichzeitig die Abhängigkeiten zu Abrechnung (WEG-8) und Verbrauchserfassung (WEG-71) zu berücksichtigen.

## Beschreibung
WEG-72 bildet den zentralen Prozess zur Steuerung und Dokumentation aller Zählerwechsel im System. Sobald ein Austausch erforderlich ist – etwa durch Defekt, Eichablauf oder geplanten Ersatz – erstellt das System automatisch einen neuen Zählerdatensatz, kopiert die relevanten Informationen und setzt den alten auf &bdquo;geschlossen&ldquo;. Der Vorgang erzeugt sowohl Abschluss- als auch Startwerte, um eine unterbrechungsfreie Verbrauchsfortführung zu gewährleisten. Jede Änderung wird revisionssicher protokolliert und ist Bestandteil des zentralen Audit-Logs.

Hauptfunktionen:

- **Zählerwechselprozess:** Automatische Erstellung eines neuen Zählers beim Austausch, inklusive Übernahme aller Metadaten (Medium, Standort, Einheit).

- **Abschluss- und Startwerte:** Automatische Erfassung der Endwerte des alten sowie der Startwerte des neuen Zählers zur Sicherstellung der Datenkontinuität.

- **Defektverwaltung:** Möglichkeit, defekte Zähler zu markieren, temporär zu deaktivieren oder vollständig stillzulegen.

- **Statusverwaltung:** Definierte Statusübergänge (*aktiv* &rarr; *defekt* &rarr; *ersetzt* &rarr; *archiviert*) mit automatischer Validierung.

- **Historisierung:** Vollständige Nachverfolgung aller Zählerwechsel mit Versionshistorie und Referenzverknüpfungen zwischen alten und neuen Datensätzen.

- **Audit-Integration:** Jeder Wechsel, Stilllegung oder Aktivierungsvorgang wird im Audit-Log (WEG-24) mit Benutzer, Zeitstempel und Grund dokumentiert.

- **Sperrlogik:** Bei offenen Ableseperioden wird ein Austausch blockiert, bis die betroffenen Vorgänge abgeschlossen sind.

- **Reporting:** Export von Austauschakten als PDF oder CSV, inklusive Vergleich der alten und neuen Werte.

## Geschäftsregeln & Logik
- Jeder Austausch erfordert eine vollständige Abschluss- und Startwertdokumentation.

- Austauschvorgänge dürfen keine offenen Ableseperioden oder ungeprüften Werte überschneiden.

- Statusänderungen erfolgen nur über vordefinierte Übergänge.

- Alte Zähler werden automatisch archiviert und dürfen nicht mehr geändert werden.

- Bei Mehrfachaustauschen innerhalb eines Gebäudes erfolgt eine sequentielle Verarbeitung nach Standortpriorität.

## Akzeptanzkriterien
- **Gegeben** ein Zähler ist defekt &rarr; **Wenn** der Austauschprozess gestartet wird &rarr; **Dann** wird ein neuer Zähler angelegt, der alte geschlossen und alle relevanten Werte im Audit-Log protokolliert.

- **Gegeben** ein Austauschdatum überschneidet sich mit einer offenen Ableseperiode &rarr; **Wenn** der Vorgang gespeichert wird &rarr; **Dann** verhindert das System den Abschluss und zeigt eine Validierungswarnung.

- **Gegeben** ein Zähler wird stillgelegt &rarr; **Wenn** der Status auf *archiviert* gesetzt wird &rarr; **Dann** wird der Zähler schreibgeschützt und aus der aktiven Nutzung entfernt.

- **Gegeben** ein neuer Zähler ersetzt einen alten &rarr; **Wenn** die Start- und Abschlusswerte übernommen werden &rarr; **Dann** ist die Verbrauchshistorie vollständig nachvollziehbar.

- **Gegeben** ein Benutzer versucht, einen archivierten Zähler zu reaktivieren &rarr; **Wenn** keine gültige Freigabe vorliegt &rarr; **Dann** verweigert das System die Änderung und erzeugt einen Audit-Eintrag.

## Nicht-Ziele
- Keine automatische Hardware-Integration für Zählerwechsel im MVP.

- Keine Berechnung von Abschreibungswerten oder Lebensdauern.

- Keine Integration von IoT-Geräten oder Smart-Meter-Schnittstellen in der ersten Phase.

## Kritische Fälle
- **Fehlerhafte Zuordnung:** Ein neuer Zähler muss immer der richtigen Einheit und dem korrekten Messpunkt zugewiesen werden.

- **Abschlusserfassung fehlt:** Wenn Abschluss- oder Startwerte fehlen, wird der Austausch blockiert.

- **Offene Perioden:** Austausch darf erst erfolgen, wenn alle vorherigen Ablesungen bestätigt wurden.

- **Bulk-Austausch:** Gleichzeitige Ersetzung vieler Zähler kann Konflikte verursachen, erfordert Prioritätslogik.

## Abhängigkeiten
- WEG-70 – Meter Registry & Types – Basisdaten der Zähler und deren Statusverwaltung.

- WEG-71 – Manual Readings – Bereitstellung von Abschluss- und Startwerten bei Wechsel.

- WEG-24 – Audit Log – Nachvollziehbarkeit aller Änderungen und Austauschvorgänge.

- WEG-54 – Retention & Archive – Archivierung und Sperrlogik für alte Zähler.

- WEG-12 – Logging & Health – Validierungsmechanismen und Systembenachrichtigungen.

## Offene Fragen
- Soll bei Massenaustauschen ein separater Workflow für Sammelverarbeitung eingeführt werden?

- Wie sollen temporäre Ersatzgeräte (z. B. bei Reparaturen) behandelt werden?

- Soll eine automatische Benachrichtigung bei Austauschdefekten ausgelöst werden?

## Zukunftserweiterungen
- **RFID-/QR-Erkennung:** Automatische Identifikation und Registrierung neuer Zähler über mobile Geräte.

- **Austauschplanung:** Zeitplaner für geplante Zählerwechsel inklusive Dienstleisterzuweisung.

- **Smart-Meter-Integration:** Automatische Aktivierung neuer Geräte über IoT-Anbindung.

- **Massenverwaltung:** Automatisierte Bulk-Austauschlogik mit Prioritätssteuerung und Statusreports.

## Verknüpfte Tasks
- [WEG-720 – Replacement with closing/opening readings](https://maierharry.atlassian.net/browse/WEG-720) – Implementierung der Austauschlogik mit Abschluss- und Startwerten, Statusverwaltung und Historienfortschreibung.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Austauschprozess mit Abschluss- und Startwerten, Statusübergängen, Audit-Log und Validierungslogik.

**Phase 2**

Bulk-Austauschprozesse, Dienstleisterintegration, automatische Zählererkennung.

**Phase 3**

Smart-Meter-Anbindung, Planungssystem mit Erinnerungsfunktionen, erweiterte Berichte.