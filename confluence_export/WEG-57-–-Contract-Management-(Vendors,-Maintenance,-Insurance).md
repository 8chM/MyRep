---
title: WEG-57 – Contract Management (Vendors, Maintenance, Insurance)
confluence_id: 27656682
version: 13
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27656682/WEG-57+Contract+Management+Vendors+Maintenance+Insurance
---

**JIRA-Link:** [WEG-57 – Contract Management (Vendors, Maintenance, Insurance)](https://maierharry.atlassian.net/browse/WEG-57)

## Überblick

Das Modul **Contract Management (Vendors, Maintenance, Insurance)** (WEG-57) erweitert das Dokumentenmanagement (DMS) um eine vollständige Vertragsverwaltung. Es bildet sämtliche Verträge einer WEG ab – von Wartungsverträgen über Versicherungen bis hin zu Dienstleistungsvereinbarungen mit externen Partnern. Im Fokus stehen die Verwaltung von Laufzeiten, Kosten, Kündigungsfristen, Indexierungen sowie Erinnerungen an bevorstehende Vertragsereignisse. Ziel ist es, Verwaltern und Beiräten eine transparente, automatisierte und revisionssichere Übersicht über alle laufenden und abgelaufenen Verträge bereitzustellen.

## Beschreibung

WEG-57 integriert sich nahtlos in das DMS (WEG-50) und bietet eine zentrale Stelle zur Verwaltung sämtlicher Verträge. Neben den eigentlichen Vertragsdokumenten werden Metadaten, Laufzeiten, Verlängerungsbedingungen und Kostenpläne gespeichert. Automatische Fristerinnerungen und Verknüpfungen zu Finanzmodulen (WEG-8, WEG-87) sorgen für eine enge Integration in die Abrechnungssystematik.

Hauptfunktionen:

- **Vertragsstammdaten:** Verwaltung von Vertragspartnern, Vertragsarten, Laufzeiten, Kostenintervallen, Kündigungsbedingungen und Gültigkeitszeiträumen.

- **Versionierte Ablage:** Jeder Vertrag und jede Änderung (Nachtrag, Verlängerung) wird im DMS versioniert gespeichert und ist auditierbar nachvollziehbar.

- **Kündigungs- und Fristmanagement:** Automatische Scheduler-Überwachung aller Vertragsfristen; Benachrichtigungen an Verwaltung oder Beirat über WEG-6.

- **Kosten- und Indexierungssystem:** Zuordnung wiederkehrender Kosten zu Finanzkategorien, Integration mit WEG-87 (Accounting & Billing) zur automatischen Übernahme in den Wirtschaftsplan.

- **Rollenbasierte Zugriffsrechte:** Vollzugriff für Verwalter:innen, Leserechte für Beirat, eingeschränkte Einsicht für Eigentümer:innen.

- **Such- und Filterfunktionen:** Filterung nach Vertragspartner, Friststatus, Kategorie oder Ablaufdatum.

- **Vertragsstatusübersicht:** Dashboard-Ansicht mit Ampellogik (aktiv, ablaufend, abgelaufen, gekündigt).

- **Audit & Historie:** Alle Änderungen werden mit Zeitstempel, Benutzer und Änderungsgrund protokolliert (WEG-24).

## Geschäftsregeln & Logik

- Jeder Vertrag besitzt mindestens eine Laufzeit, eine Kostenkomponente und eine Kündigungsregel.

- Fristen werden systemseitig validiert und durch den Scheduler täglich überprüft.

- Vertragsverlängerungen dürfen nur erfolgen, wenn keine offenen Kündigungen vorliegen.

- Kündigungsfristen werden automatisch berechnet (z. B. &bdquo;3 Monate zum Jahresende&ldquo; &rarr; nächstmöglicher Termin).

- Jede Änderung (Kosten, Fristen, Status) erzeugt eine neue Version des Vertrags.

- Abgelaufene Verträge werden automatisch in den Status &bdquo;archiviert&ldquo; überführt.

- Fristerinnerungen erfolgen 30 Tage vor Ablauf und 7 Tage vor Enddatum.

- Verträge, die mit Kosten verknüpft sind, müssen einer Kategorie (WEG-80) zugewiesen sein.

## Akzeptanzkriterien

- **Gegeben** ein Vertrag hat eine Kündigungsfrist &rarr; **Wenn** das Kündigungsdatum erreicht wird &rarr; **Dann** sendet das System automatisch eine Benachrichtigung über WEG-6 an die Verwaltung.

- **Gegeben** ein Vertrag läuft aus &rarr; **Wenn** die Frist verstrichen ist &rarr; **Dann** wird der Vertrag automatisch auf den Status &bdquo;archiviert&ldquo; gesetzt und im DMS gesperrt.

- **Gegeben** ein neuer Nachtrag wird hochgeladen &rarr; **Wenn** der Upload bestätigt wird &rarr; **Dann** erzeugt das System eine neue Version und verknüpft sie mit dem Originalvertrag.

- **Gegeben** eine Kostenänderung wird gespeichert &rarr; **Wenn** der Vertrag einem Budget zugeordnet ist &rarr; **Dann** wird der neue Betrag automatisch im Wirtschaftsplan berücksichtigt (WEG-87).

- **Gegeben** ein Administrator prüft das Vertrags-Dashboard &rarr; **Wenn** ablaufende Verträge vorhanden sind &rarr; **Dann** werden diese farblich hervorgehoben und sortierbar dargestellt.

## Nicht-Ziele

- Keine rechtliche Vertragsprüfung oder semantische Analyse (KI-basierte Logik erst in Phase 3).

- Kein automatisches Hochladen von Vertragskopien aus externen Quellen (z. B. E-Mail).

- Keine digitale Signatur im MVP (kommt mit WEG-99 in Phase 2).

- Keine automatische Indexierung der Vertragsinhalte im MVP.

## Kritische Fälle

- **Fehlende Fristen:** Wenn keine Laufzeit angegeben ist, muss das System eine Eingabe erzwingen, bevor der Vertrag gespeichert wird.

- **Doppelte Verträge:** Mehrfach angelegte Verträge mit identischem Partner oder Zeitraum müssen erkannt und gemeldet werden.

- **Scheduler-Ausfall:** Wenn die tägliche Fristprüfung fehlschlägt, müssen ausstehende Benachrichtigungen beim nächsten Lauf nachgeholt werden.

- **Falsche Versionierung:** Überschreiben bestehender Versionen ist nicht erlaubt; jede Änderung erzeugt eine neue Revision.

- **Verknüpfungsfehler:** Kostenverknüpfungen zu Finanzmodulen dürfen keine Rundungsdifferenzen verursachen.

## Abhängigkeiten

-  – Speicherung, Versionierung und Ablage von Vertragsdokumenten.

-  – Frist- und Ablaufbenachrichtigungen.

-  – Nachvollziehbarkeit aller Vertragsänderungen.

-  – Übernahme der Vertragskosten in Umlage und Wirtschaftsplan.

-  – Scheduler-Überwachung, Fehlerprotokollierung.

-  – Scheduler-Basis und zentrale Konfiguration.

## Offene Fragen

- Soll eine automatische Verlängerung nach Ablauf standardmäßig aktiviert oder deaktiviert sein?

- Soll es möglich sein, Vertragsvorlagen (Templates) für bestimmte Typen (Versicherung, Wartung) zu definieren?

- Soll der Beirat Zugriff auf Vertragsdetails erhalten oder nur Zusammenfassungen sehen?

- Sollen Vertragskosten in mehreren Finanzperioden verteilt werden können (Splitting)?

## Zukunftserweiterungen

- **Digitale Signaturen:** Integration eIDAS-konformer Signaturen (WEG-99).

- **KI-gestützte Vertragsanalyse:** Automatische Extraktion von Laufzeiten, Beträgen und Fristen.

- **Budgetverknüpfung:** Dynamische Planung zukünftiger Kosten auf Basis bestehender Verträge.

- **Vertragsprognosen:** Frühwarnungen bei Budgetüberschreitungen.

- **API-Integrationen:** Anbindung an externe Anbieter, Versicherungen oder Energieversorger.

## Verknüpfte Tasks

- [WEG-570 – Contract CRUD (terms, renewal, cancellation alerts)](https://maierharry.atlassian.net/browse/WEG-570) – Implementiert Vertragsanlage, Verlängerungen und Fristbenachrichtigungen.

- [WEG-571 – Contract Cost Schedule & Indexation](https://maierharry.atlassian.net/browse/WEG-571) – Definiert Kostenpläne, Intervalle und Indexierungslogik.

- [WEG-572 – Contract &rarr; Billing Mapping](https://maierharry.atlassian.net/browse/WEG-572) – Automatische Integration von Vertragskosten in den Wirtschaftsplan (WEG-87).

- [WEG-573 – Contract Dashboard & Filters](https://maierharry.atlassian.net/browse/WEG-573) – Übersicht mit Filter-, Such- und Fristwarnfunktionen.

## Versionen & Komponenten

**Version**

**Komponente**

**MVP**

Vertragsverwaltung mit Laufzeit, Kosten, Kündigungsfrist, DMS-Versionierung und Scheduler-Erinnerung.

**Phase 2**

Digitale Signatur, Budgetintegration, erweiterte Frist-Workflows und Dashboard-Optimierung.

**Phase 3**

KI-gestützte Vertragsanalyse, automatische Indexierung, externe Integrationen und Budgetprognosen.