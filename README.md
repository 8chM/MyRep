# Atlassian API Integration & Confluence Export

Dieses Repository enthält Tools für den Zugriff auf JIRA und Confluence sowie einen vollständigen Export aller Confluence-Seiten.

## Inhalt

### 1. API-Test-Skripte

**Voraussetzungen:**
- Python 3
- `requests` Bibliothek: `pip install requests`
- Umgebungsvariable `ATLASSIAN_API_TOKEN` gesetzt

**Skripte:**

- `test_atlassian_api.py` - Testet JIRA- und Confluence-API-Zugriff
- `list_confluence_pages.py` - Listet alle Seiten im WEG-Space auf
- `test_final.py` - Finaler Test mit spezifischer Seite
- `download_confluence_to_markdown.py` - Exportiert alle Confluence-Seiten als Markdown

**Verwendung:**

```bash
# API-Token als Umgebungsvariable setzen
export ATLASSIAN_API_TOKEN='your-token-here'

# Optional: Username und Base URL anpassen
export ATLASSIAN_USERNAME='your-email@example.com'
export JIRA_BASE_URL='https://your-instance.atlassian.net'

# Skripte ausführen
python3 test_atlassian_api.py
python3 list_confluence_pages.py
python3 download_confluence_to_markdown.py
```

### 2. Confluence Export

**Verzeichnis:** `confluence_export/`

**Inhalt:**
- 85 Confluence-Seiten als Markdown
- Alle WEG-Epics und Features (WEG-1 bis WEG-99)
- Product Requirements Document (PRD)
- Projektdokumentation

**Frontmatter-Format:**
Jede Markdown-Datei enthält Metadaten:
```yaml
---
title: Seitentitel
confluence_id: 12345678
version: 1
url: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/...
---
```

## Sicherheit

**Wichtig:** API-Tokens niemals im Code committen!

- Verwende die `.env.example` als Vorlage
- Erstelle eine `.env` Datei (wird automatisch ignoriert)
- Setze Umgebungsvariablen in der Shell

## Struktur

```
.
├── README.md
├── .env.example                          # Vorlage für Credentials
├── .gitignore                            # Ignoriert .env Dateien
├── test_atlassian_api.py                 # JIRA/Confluence Tests
├── list_confluence_pages.py              # Seiten auflisten
├── test_final.py                         # Einzelseitentest
├── download_confluence_to_markdown.py    # Markdown-Export
└── confluence_export/                    # 85 exportierte Seiten
    ├── Product-Requirements-Document-(PRD).md
    ├── Projektdokumentation.md
    ├── WEG-1-–-Platform-Foundation-...md
    └── ...
```

## API-Dokumentation

- [JIRA Cloud REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Confluence Cloud REST API](https://developer.atlassian.com/cloud/confluence/rest/v1/intro/)

## Statistiken

- **Confluence-Seiten:** 85
- **JIRA-Projekte:** 2 (WEG, WMS)
- **Markdown-Dateien:** 11.452+ Zeilen
