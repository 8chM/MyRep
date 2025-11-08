---
title: WEG-92 – Voting Rules Model (MEA/Unit/Owner)
confluence_id: 26968760
version: 9
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/26968760/WEG-92+Voting+Rules+Model+MEA+Unit+Owner
---

**JIRA-Link:** [WEG-92 – Voting Rules Model (MEA/Unit/Owner)](https://maierharry.atlassian.net/browse/WEG-92)

## Überblick
Das Modul **Voting Rules Model **(WEG-92) definiert die Logik für Stimmgewichtung und Mehrheitsbildung innerhalb von Eigentümerversammlungen. Es ermöglicht Abstimmungen nach unterschiedlichen Modellen – auf Basis der Miteigentumsanteile (MEA), pro Einheit oder pro Kopf. Ziel ist es, ein flexibles, rechtssicheres und konfigurierbares Regelwerk für Abstimmungen bereitzustellen, das den individuellen Anforderungen der jeweiligen Gemeinschaft entspricht.

## Beschreibung
WEG-92 bildet das zentrale Framework für die Berechnung und Auswertung von Abstimmungen in Eigentümerversammlungen. Das Modul wird direkt durch das Meeting-System (WEG-90 / WEG-91) aufgerufen, sobald ein Beschluss oder eine Abstimmung gestartet wird. Jede Abstimmung wird anhand des konfigurierten Stimmtyps gewichtet, wobei Enthaltungen gesondert gezählt und dokumentiert werden. Im MVP werden drei Gewichtungsmodelle unterstützt: nach MEA, nach Einheit und nach Kopfzahl.

Hauptfunktionen:

- **Stimmgewichtung:** Berechnung der Stimmen basierend auf MEA, Einheitenzahl oder Eigentümerzahl.

- **Abstimmungstypen:** Unterstützung von Ja/Nein/Enthaltung mit separater Zählung von Enthaltungen.

- **Mehrheitsarten:** Unterstützung einfacher, absoluter und qualifizierter Mehrheiten (ab Phase 2).

- **Proxy-Unterstützung:** Vollmachten (aus WEG-91) werden berücksichtigt, Proxy-Ketten sind jedoch im MVP auf eine Ebene beschränkt.

- **Konfigurierbare Quoren:** Definierbare Grenzwerte (z. B. 50 %, 75 %) für die Beschlussfähigkeit.

- **Auditierbarkeit:** Jede Stimmabgabe und Berechnung wird revisionssicher im Audit-Log (WEG-24) gespeichert.

## Geschäftsregeln & Logik
- Jede Abstimmung muss genau einem gültigen Voting Model (MEA, Unit, Owner) zugeordnet sein.

- Enthaltungen zählen weder als &bdquo;Ja&ldquo; noch &bdquo;Nein&ldquo;, beeinflussen aber Quorenberechnungen.

- Proxy-Stimmen dürfen nur einmalig weitergegeben werden (keine Mehrfachdelegationen).

- Die Berechnungslogik wird nach Abschluss der Abstimmung gesperrt; Änderungen erfordern eine neue Revision.

- Bei qualifizierten Mehrheiten (Phase 2 +) sind Grenzwerte und Berechnungslogik vordefiniert, aber konfigurierbar.

## Akzeptanzkriterien
- **Gegeben** ein MEA-basiertes Voting ist aktiv &rarr; **Wenn** Stimmen abgegeben werden &rarr; **Dann** werden die Ergebnisse korrekt nach Miteigentumsanteilen gewichtet und im Audit-Log protokolliert.

- **Gegeben** ein Proxy ist vorhanden &rarr; **Wenn** der bevollmächtigte Eigentümer abstimmt &rarr; **Dann** wird das Stimmgewicht korrekt um die übertragenen MEA-Anteile erhöht.

- **Gegeben** eine Abstimmung erreicht nicht das definierte Quorum &rarr; **Wenn** die Auswertung erfolgt &rarr; **Dann** wird das Ergebnis als ungültig markiert und mit Warnhinweis versehen.

- **Gegeben** eine qualifizierte Mehrheit ist konfiguriert &rarr; **Wenn** die Ergebnisse berechnet werden &rarr; **Dann** vergleicht das System den Stimmanteil mit dem erforderlichen Schwellenwert (z. B. 75 %).

## Nicht-Ziele
- Keine Unterstützung komplexer Mehrpersonen- oder Fraktionsmodelle im MVP.

- Keine interaktive Simulation von Abstimmungsergebnissen.

- Keine dynamische Anpassung von MEA-Werten während laufender Abstimmungen.

## Kritische Fälle
- **Fehlende MEA-Daten:** Wenn eine Einheit keinen gültigen MEA-Wert hat, wird die Abstimmung blockiert und ein Validierungsfehler angezeigt.

- **Proxy-Konflikte:** Mehrfachdelegationen führen zu Fehlerstatus und Rollback.

- **Quorum-Fehler:** Falsche Schwellenwertdefinitionen können zu ungültigen Beschlüssen führen; Systemprüfung erforderlich.

## Abhängigkeiten
- WEG-90 – Meetings Domain Model – Nutzung der Abstimmungs- und Statuslogik.

- WEG-91 – Agenda, Participants & Proxies – Teilnehmer- und Vollmachtsverwaltung.

- WEG-24 – Audit Log – Speicherung der Abstimmungsergebnisse und Änderungen.

## Offene Fragen
- Soll das System im MVP bereits eine Option für qualifizierte Mehrheiten (z. B. 2/3 oder 3/4) bieten oder erst ab Phase 2?

- Müssen Enthaltungen im PDF-Protokoll explizit ausgewiesen werden?

- Sollen Stimmrechte für Beiräte gesondert behandelt werden (z. B. beratend, nicht stimmberechtigt)?

## Zukunftserweiterungen
- **Templates für qualifizierte Mehrheiten:** Vordefinierte Regelwerke für häufige Beschlussarten (2/3, 3/4, absolute Mehrheit).

- **Sondermehrheiten:** Unterstützung regional unterschiedlicher Rechtsgrundlagen (Landesrecht).

- **Simulationsmodus:** Prognose von Mehrheitsverhältnissen vor Abstimmungsbeginn.

- **Erweiterte Protokollintegration:** Vollständige Darstellung der Abstimmungsergebnisse mit Diagrammen und Statistiken.

## Verknüpfte Tasks
- [WEG-920 – Weight Models (MEA/Unit/Owner)](https://maierharry.atlassian.net/browse/WEG-920) – Implementierung der Gewichtungsmodelle für MEA-, Einheiten- und Eigentümerbasierte Abstimmungen.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Unterstützung der Voting Models (MEA, Unit, Owner), Grundlogik für Stimmengewichtung, Proxy-Unterstützung (eine Ebene), Audit-Integration.

**Phase 2**

Einführung qualifizierter Mehrheiten, Templates für gängige Beschlussarten, konfigurierbare Quoren.

**Phase 3**

Dynamische Mehrheitsregeln nach Landesrecht, Simulationsmodus und erweiterte Protokollintegration.