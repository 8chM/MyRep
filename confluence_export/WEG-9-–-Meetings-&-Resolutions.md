---
title: WEG-9 – Meetings & Resolutions
confluence_id: 27853507
version: 17
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27853507/WEG-9+Meetings+Resolutions
---

**JIRA-Link:** [WEG-9 – Meetings & Resolutions](https://maierharry.atlassian.net/browse/WEG-9)

## Beschreibung
Das Modul **WEG-9 – Meetings & Resolutions** digitalisiert die komplette Verwaltung von Eigentümerversammlungen innerhalb einer WEG. Es deckt die gesamte Prozesskette ab – von der Terminplanung über die Einladung und Abstimmung bis hin zur Protokollierung, Veröffentlichung und Nachverfolgung von Beschlüssen.

Ziel ist es, die Kommunikation zwischen Eigentümern, Beirat und Verwaltung zu vereinfachen, rechtssichere Beschlussfassungen zu gewährleisten und alle relevanten Daten zentral, nachvollziehbar und versioniert bereitzustellen. Das System unterstützt alle Meetingphasen: Vorbereitung, Durchführung und Archivierung. Beschlüsse sind unveränderlich, revisionssicher dokumentiert und eindeutig miteinander verknüpft.

Im MVP liegt der Fokus auf der **rechtssicheren digitalen Dokumentation** und der **Abbildung des Abstimmungsprozesses**. Spätere Phasen erweitern das Modul um digitale Signaturen, Online-Versammlungen und KI-gestützte Protokollerstellung.

## Untermodule
**Untermodul**

**Beschreibung**

**WEG-90 – Meetings Domain Model & Architecture**Fundamentales, mandantenfähiges Domänenmodell für Versammlungen und Beschlüsse mit Objektbeziehungen und Statusflüssen.

**WEG-91 – Agenda, Participants & Proxies**Verwaltung von Tagesordnungen, Teilnehmern und Vollmachten; Einladungsfristen, Terminüberwachung und Agenda-Versionierung.

**WEG-92 – Voting Rules Model**Konfigurierbares Abstimmungssystem mit Gewichtung nach MEA, Einheit oder Eigentümer. Enthaltungen werden gesondert erfasst.

**WEG-93 – Resolution Registry & Supersession**Zentrales Register für Beschlüsse inkl. Lebenszyklus, Verknüpfungen und Supersession-Verweise bei Folgeentscheidungen.

**WEG-94 – Meeting Minutes & Resolution Archive**Erstellung, Freigabe, Versionierung und Archivierung von Protokollen und Beschlussdokumenten.

**WEG-95 – Meetings Notifications**Versand von Einladungen, Erinnerungen, Protokollfreigaben und Follow-ups über das interne Nachrichtensystem.

**WEG-97 – Ticketing / Issue Management**Verknüpfung von Beschlüssen mit Tickets (z. B. Mängelmanagement) und Synchronisierung des Umsetzungsstatus.

**WEG-99 – Signature Placeholders**Platzhalter für künftige Integration von elektronischen Signaturen (eIDAS-konform).

## Geschäftslogik
- **Phasenmodell:** Jede Versammlung durchläuft die Phasen *Draft &rarr; Scheduled &rarr; Conducted &rarr; Closed &rarr; Archived*. Änderungen sind nur vorwärtsgerichtet möglich; archivierte Meetings sind schreibgeschützt.

- **Teilnehmerverwaltung:** Eigentümer, Beiräte und geladene Gäste werden automatisch aus der Eigentümerdatenbank (WEG-4) übernommen. Vollmachten sind personenbezogen, zeitlich begrenzt und mit Nachweisdokumenten hinterlegt.

- **Agenda & Quoren:** Tagesordnungen können flexibel erstellt, versioniert und ergänzt werden. Quoren und Einladungsfristen sind pro WEG konfigurierbar; Standard: 14 Tage.

- **Abstimmungen:** Stimmen können nach verschiedenen Gewichtungsmodellen (MEA, Einheit, Kopfzahl) abgegeben werden. Enthaltungen werden separat erfasst.

- **Beschlussregister:** Jeder Beschluss ist eindeutig identifizierbar, mit vorherigen oder aufhebenden Beschlüssen verknüpft und dauerhaft im System archiviert.

- **Protokollfreigabe:** Nach Abschluss eines Meetings wird das Protokoll als PDF generiert, gebrandet (WEG-56) und im DMS (WEG-5) versioniert abgelegt.

- **Benachrichtigungen:** Einladungen, Änderungen oder veröffentlichte Beschlüsse lösen automatische Mitteilungen aus (WEG-6).

- **Audit & Datenschutz:** Alle Aktionen – von Einladungen über Stimmabgaben bis zur Veröffentlichung – werden im Audit-Log (WEG-24) festgehalten. Personenbezogene Daten werden bei Bedarf pseudonymisiert.

## Akzeptanzkriterien

- **Gegeben** eine geplante Versammlung mit Agenda &rarr; **Wenn** Einladungen generiert werden &rarr; **Dann** erhalten alle berechtigten Teilnehmer eine Benachrichtigung und das Einladungsschreiben wird im DMS gespeichert.

- **Gegeben** ein Beschluss mit MEA-Gewichtung &rarr; **Wenn** Stimmen abgegeben werden &rarr; **Dann** berechnet das System das Ergebnis automatisch, speichert das Resultat und protokolliert es revisionssicher.

- **Gegeben** ein abgeschlossenes Meeting &rarr; **Wenn** das Protokoll freigegeben wird &rarr; **Dann** erzeugt das System ein gebrandetes PDF, legt es im DMS ab und informiert alle Beteiligten.

- **Gegeben** ein neuer Beschluss ersetzt einen bestehenden &rarr; **Wenn** dieser angenommen wird &rarr; **Dann** verknüpft das System beide Beschlüsse im Register und markiert den alten als &bdquo;ersetzt".

- **Gegeben** ein Beschluss mit verknüpftem Ticket &rarr; **Wenn** das Ticket geschlossen wird &rarr; **Dann** aktualisiert das System den Beschlussstatus und dokumentiert die Umsetzung im Audit-Log.

## Nicht-Ziele
- Keine integrierte Video- oder Telefonkonferenzfunktion.

- Keine qualifizierte elektronische Signatur im MVP.

- Keine automatische Kalender-Synchronisation (nur optionaler iCal-Export).

- Keine KI-Transkription oder Spracherkennung in Phase 1.

## Kritische Fälle
- **Ungültige Vollmachten:** Abgelaufene oder fehlerhafte Vollmachten blockieren Stimmabgaben und erzeugen Systemhinweise.

- **Fehlende Quoren:** Wenn das Quorum nicht erreicht wird, kann der Beschluss nicht angenommen werden.

- **Doppelte Beschlüsse:** Das System erkennt doppelte Beschlüsse und verhindert widersprüchliche Ergebnisse.

- **Nachträgliche Änderungen:** Bereits veröffentlichte Protokolle können nur durch neue Versionen ersetzt werden.

- **Unvollständige Freigabe:** Wenn ein Protokoll im Entwurfsstatus verbleibt, werden automatische Erinnerungen an den Moderator gesendet.

## Abhängigkeiten
- WEG-4 – Property & People: Liefert Eigentümer-, MEA- und Einheitsdaten für die Berechnung von Stimmrechten und Teilnehmerlisten.

- WEG-5 – Document Management & Templates: Verwaltet Einladungen, Protokolle und Beschlussdokumente.

- WEG-6 – In-App Messaging & Notifications (Basic): Versendet Benachrichtigungen zu Terminen, Protokollen und Änderungen.

- WEG-8 – Finance & Banking: Bindet finanzrelevante Tagesordnungspunkte wie Budget oder Wirtschaftsplan ein.

- WEG-12 – Error Handling, Logging & Health: Stellt Zeitsteuerung, Erinnerungs-Scheduler und Logging für Fristen bereit.

- WEG-24 – Audit Log (User/Roles/Settings): Dokumentiert alle Meeting- und Beschlussaktionen revisionssicher.

- WEG-26 – Data Privacy & Redaction (GDPR Base): Regelt Datenschutz, Redaktions- und Zugriffsrichtlinien für personenbezogene Daten.

- WEG-56 – PDF Branding Base (per Association): Gewährleistet einheitliches Layout und Corporate Design der Dokumente.

## Offene Fragen
- Soll asynchrones Remote-Voting erlaubt sein, und welche rechtlichen Voraussetzungen gelten dafuer?

- Welche Mehrheitsarten sollen standardmaessig unterstuetzt werden (einfach, qualifiziert, absolut)?

- Sollen externe Teilnehmer mit eingeschraenkter Sicht eingeladen werden koennen?

- Welche Kommunikationskanaele sind verbindlich (In-App, E-Mail, Post)?

## Zukunftserweiterungen
- **Digitale Signaturen:** Integration rechtssicherer eIDAS-Signaturen fuer Beschluesse und Protokolle.

- **Kalender-Synchronisation & Konferenzintegration:** Outlook/Google-Sync, Anbindung an Teams oder Zoom.

- **KI-gestuetzte Protokolle:** Automatische Zusammenfassung, Extraktion von Beschluessen und Transkriptanalyse.

- **Beschluss-Dashboard:** Uebersicht zu Status, Umsetzung und Fristen aller Beschluesse.

## Versionen & Komponenten
**Version**

**Komponente**

**MVP**

Grundfunktionen für Planung, Abstimmung, Protokollierung und Archivierung von Beschlüssen.

**Phase 2**

Digitale Signaturen, Remote-Voting, Kalender-Integration.

**Phase 3**

KI-gestützte Protokollerstellung, automatische Umsetzungskontrolle, erweiterte Mehrheitsregeln.