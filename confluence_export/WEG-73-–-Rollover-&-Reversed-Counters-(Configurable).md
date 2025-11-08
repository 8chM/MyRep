---
title: WEG-73 – Rollover & Reversed Counters (Configurable)
confluence_id: 27329403
version: 20
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27329403/WEG-73+Rollover+Reversed+Counters+Configurable
---

**JIRA-Link:** [WEG-73 – Rollover & Reversed Counters (Configurable)](https://maierharry.atlassian.net/browse/WEG-73)

## Überblick
Das Modul **Rollover & Reversed Counters** (WEG-73) behandelt Sonderfälle bei Verbrauchszählern, die aufgrund technischer Eigenschaften besondere Zählverhalten aufweisen – beispielsweise Zähler, die nach Erreichen ihres Maximalwerts wieder bei null beginnen (Roll-Over) oder rückwärts laufen können. Ziel ist die korrekte Verbrauchsberechnung und Datenvalidierung auch in diesen Fällen, um falsche Verbrauchswerte oder Abrechnungsfehler zu vermeiden. Das Modul ergänzt die Basiserfassung (WEG-71) und Zählerverwaltung (WEG-70) um eine intelligente Berechnungs- und Erkennungslogik für diese Spezialfälle.

## Beschreibung
WEG-73 erweitert die Metering-Funktionalität um Mechanismen zur automatischen Erkennung, Korrektur und Protokollierung von Roll-Over- und Rückwärtslaufereignissen. Das System interpretiert negative Differenzen oder Werte, die über definierte Grenzwerte hinausgehen, als spezielle Zählervorgänge. Diese Ereignisse werden automatisch erkannt, korrekt berechnet und revisionssicher im Audit-Log festgehalten.

Hauptfunktionen:

- **Roll-Over-Erkennung:** Automatische Identifizierung, wenn ein Zähler seinen Maximalwert erreicht und wieder bei null beginnt.

- **Rückwärtslauf-Verarbeitung:** Behandlung negativer Differenzen als valide Sonderfälle mit Anpassung der Verbrauchsberechnung.

- **Konfigurierbare Maximalwerte:** Definition individueller Grenzwerte pro Medium oder Zählertyp (z. B. Wasser, Gas, Strom, Wärme).

- **Mehrfach-Rollovers:** Unterstützung mehrerer Roll-Overs innerhalb einer Messperiode mit korrekter Summenbildung.

- **Automatische Berechnung:** Dynamische Korrektur der Verbrauchswerte über den Roll-Over hinweg, basierend auf Vorwert und Maximalgrenze.

- **Audit-Integration:** Alle Sonderfälle werden automatisch im Audit-Log (WEG-24) dokumentiert, einschließlich Zähler-ID, Zeitpunkt und Differenz.

- **Warnmeldungen:** Benachrichtigung an Verwalter bei Auffälligkeiten wie unerwarteten Verbrauchssprüngen oder mehrfachen Roll-Overs.

- **Reporting:** Übersicht der aufgetretenen Roll-Over- und Rückwärtslaufereignisse als CSV- oder PDF-Export.

## Geschäftsregeln & Logik
- Der Maximalwert eines Roll-Over-Zählers ist pro Medium konfigurierbar und wird bei Berechnung berücksichtigt.

- Negative Differenzen werden nur akzeptiert, wenn der Zählertyp *bidirektional* gekennzeichnet ist.

- Roll-Over- und Rückwärtslaufereignisse erzeugen zwingend einen Audit-Eintrag.

- Bei mehr als einem Roll-Over pro Periode erfolgt eine Korrektur der berechneten Verbrauchssumme.

- Falsch konfigurierte Maximalwerte müssen über Validierungen erkannt und gemeldet werden.

- Unplausible Werte (z. B. mehrfacher Roll-Over in kurzer Zeit) erzeugen Systemwarnungen.

## Akzeptanzkriterien
- **Gegeben** ein Zähler erreicht seinen Maximalwert &rarr; **Wenn** er auf null zurückspringt &rarr; **Dann** berechnet das System den Verbrauch korrekt über den Roll-Over hinweg und erstellt einen Audit-Eintrag.

- **Gegeben** ein rückwärtslaufender Zähler wird erfasst &rarr; **Wenn** eine negative Differenz erkannt wird &rarr; **Dann** korrigiert das System den Verbrauch und protokolliert den Sonderfall im Audit-Log.

- **Gegeben** ein Zählertyp hat keinen konfigurierten Maximalwert &rarr; **Wenn** ein Roll-Over erkannt wird &rarr; **Dann** fordert das System eine Konfiguration an und blockiert die Berechnung bis zur Klärung.

- **Gegeben** mehrere Roll-Overs innerhalb einer Periode &rarr; **Wenn** sie erkannt werden &rarr; **Dann** summiert das System die Differenzen korrekt und vermerkt alle Ereignisse im Audit.

- **Gegeben** ein ungewöhnlicher Verbrauchssprung &rarr; **Wenn** dieser außerhalb der erwarteten Toleranz liegt &rarr; **Dann** sendet das System eine Warnmeldung an den Administrator.

## Nicht-Ziele
- Keine automatische Fehlerdiagnose oder Reparaturanalyse defekter Zähler.

- Keine Unterstützung variabler Maximalwerte je Ableseperiode im MVP.

- Keine automatische Korrektur historischer Daten ohne Benutzerfreigabe.

## Kritische Fälle
- **Falsche Maximalwerte:** Fehlkonfigurationen können zu fehlerhaften Verbrauchsberechnungen führen.

- **Unklare Rückwärtsläufe:** Manipulationen oder Messfehler müssen durch Benutzerprüfung bestätigt werden.

- **Mehrfache Roll-Overs:** Mehrere Roll-Overs in kurzer Zeit erfordern eine klare Ereignisreihenfolge.

- **Fehlende Audit-Einträge:** Ohne Protokollierung verliert das System die Nachvollziehbarkeit von Verbrauchsdaten.

## Abhängigkeiten
- WEG-70 – Meter Registry & Types – Liefert die Definition und Maximalwerte pro Zählertyp.

- WEG-71 – Manual Readings – Basis der Messwerte, auf denen die Berechnungen basieren.

- WEG-24 – Audit Log – Speicherung der Roll-Over- und Rückwärtslaufereignisse.

- WEG-12 – Logging & Health – Überwachung und Fehlerprotokollierung.

## Offene Fragen
- Soll das System zwischen bidirektionalen (z. B. PV-Einspeisung) und unidirektionalen Zählern unterscheiden?

- Wie sollen mehrfach auftretende Roll-Overs visuell im Reporting dargestellt werden?

- Soll bei auffälligen Mustern automatisch eine Serviceprüfung vorgeschlagen werden?

## Zukunftserweiterungen
- **Automatische Maximalwertanpassung:** Dynamische Erkennung des Maximalwerts anhand historischer Daten oder Herstellerangaben.

- **Anomalieerkennung:** KI-basierte Erkennung ungewöhnlicher Verbrauchs- oder Roll-Over-Muster.

- **Integritätsprüfung:** Automatische Nachberechnung bei nachträglicher Änderung von Maximalwerten.

- **Benachrichtigungssystem:** Automatische E-Mail- oder Systemmeldung bei Roll-Over-Fehlern.

## Verknüpfte Tasks
- [WEG-730 – Rollover & Reversed Counters Config](https://maierharry.atlassian.net/browse/WEG-730) – Implementierung der Logik zur Erkennung und Berechnung von Roll-Over- und Rückwärtslaufereignissen einschließlich Audit-Protokollierung.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Grundfunktion für Erkennung von Roll-Over- und Rückwärtslaufereignissen, Audit-Protokollierung und konfigurierbare Maximalwerte.

**Phase 2**

Automatische Maximalwertanpassung, verbesserte Plausibilitätsprüfung und Reporting-Erweiterung.

**Phase 3**

KI-basierte Anomalieerkennung, Serviceintegration und visuelle Auswertungen.