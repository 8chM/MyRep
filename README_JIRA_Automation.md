# JIRA Automation für WEG Management System

Vollständige Automatisierung für JIRA-Ticket-Management durch KI-Agenten.

---

## 📁 Dateien-Übersicht

| Datei | Beschreibung | Verwendung |
|-------|--------------|------------|
| `JIRA_API_Guide_for_KI_Agents.md` | Vollständige API-Dokumentation | Referenz für KI-Agenten |
| `JIRA_Templates_for_KI_Agents.md` | Issue-Templates (Epic, Story, Task) | Ticket-Struktur |
| `.env.jira.example` | Credentials-Vorlage | Kopieren zu `.env` |
| `jira_automation_example.py` | Funktionsfähiges Python-Script | Direkt ausführbar |

---

## 🚀 Quick Start

### 1. Credentials einrichten

```bash
# .env Datei erstellen
cp .env.jira.example .env

# .env Datei bearbeiten (Credentials sind bereits drin!)
# Keine Änderungen nötig, wenn du das WEG-Projekt verwendest
```

### 2. Dependencies installieren

```bash
pip install jira python-dotenv
```

### 3. Script ausführen

```bash
# Dry-Run (keine echten Änderungen)
python jira_automation_example.py

# WEG-1 Modul-Struktur erstellen
python jira_automation_example.py --create

# Bestehende Issues aktualisieren
python jira_automation_example.py --update
```

---

## 🎯 Use Cases für KI-Agenten

### Use Case 1: Neues Modul erstellen

```python
from jira_automation_example import WegJiraAutomation

automation = WegJiraAutomation()

# Epic für WEG-4 (Property & People)
epic = automation.create_epic(
    summary="WEG-4 – Property & People",
    description="...",
    labels=["backend", "domain"]
)

# Story erstellen
story = automation.create_story(
    summary="WEG-40 – Association Details & Buildings",
    description="...",
    epic_key=epic.key
)

# Tasks erstellen
automation.create_task(
    summary="Implement Association Entity",
    description="...",
    parent_key=story.key,
    priority="High"
)
```

### Use Case 2: Progress-Updates nach Code-Completion

```python
automation = WegJiraAutomation()

# Nach erfolgreicher Implementierung
automation.add_comment("WEG-40", """
✅ Implementation complete:
- Association entity created
- Unit tests written (95% coverage)
- Integration tests passing

Ready for code review.
""")

# Status ändern
automation.transition_issue("WEG-40", "In Review")
```

### Use Case 3: Automatisches Reporting

```python
automation = WegJiraAutomation()

# Alle offenen Issues finden
issues = automation.jira.search_issues('project=WEG AND status="In Progress"')

for issue in issues:
    print(f"{issue.key}: {issue.fields.summary}")
    print(f"  Assignee: {issue.fields.assignee}")
    print(f"  Updated: {issue.fields.updated}")
```

---

## 📖 API-Referenz

### Verfügbare Credentials

```python
JIRA_BASE_URL = "https://maierharry.atlassian.net"
JIRA_USERNAME = "Maier.harry@gmail.com"
JIRA_API_TOKEN = "ATATT3xFfGF01..."  # In .env.jira.example
JIRA_PROJECT_KEY = "WEG"
```

### Klasse: WegJiraAutomation

```python
class WegJiraAutomation:
    """Automation für WEG JIRA-Management"""

    def __init__(self, dry_run: bool = False):
        """Initialisiert JIRA-Client"""

    def create_epic(self, summary, description, labels=None):
        """Erstellt Epic"""

    def create_story(self, summary, description, epic_key, labels=None):
        """Erstellt Story unter Epic"""

    def create_task(self, summary, description, parent_key, priority="Medium"):
        """Erstellt Task unter Story"""

    def add_comment(self, issue_key, comment):
        """Fügt Kommentar hinzu"""

    def transition_issue(self, issue_key, transition_name):
        """Ändert Status (To Do → In Progress → Done)"""
```

---

## 🔐 Sicherheit

### ✅ Best Practices

1. **Credentials NUR in .env speichern**
   ```bash
   # .gitignore prüfen
   cat .gitignore | grep .env
   ```

2. **NIEMALS Credentials committen**
   ```bash
   # Vor jedem Commit prüfen
   git diff | grep -i "ATATT"
   ```

3. **API-Token rotieren**
   - Alle 90 Tage neuen Token generieren
   - URL: https://id.atlassian.com/manage-profile/security/api-tokens

### ❌ Häufige Fehler

**Fehler 401 (Unauthorized):**
- API-Token falsch oder abgelaufen
- Username muss E-Mail-Adresse sein

**Fehler 403 (Forbidden):**
- Keine Berechtigung für diese Operation
- Projekt-Zugriff prüfen

**Fehler 404 (Not Found):**
- Issue-Key falsch (muss "WEG-10" sein, nicht "WEG10")

---

## 📚 Dokumentation

### Vollständige Guides

1. **JIRA_API_Guide_for_KI_Agents.md**
   - Authentifizierung
   - Alle API-Operationen
   - Code-Beispiele
   - Error Handling
   - Best Practices

2. **JIRA_Templates_for_KI_Agents.md**
   - Epic-Template
   - Story-Template
   - Task-Templates (Backend, Frontend, Infra)
   - Subtask-Template
   - Beispiel-Anwendungen

### JIRA REST API Docs

- **Official:** https://developer.atlassian.com/cloud/jira/platform/rest/v3/
- **Python Lib:** https://jira.readthedocs.io/
- **Project:** https://maierharry.atlassian.net/browse/WEG

---

## 💡 Erweiterte Beispiele

### Batch-Import aus Templates

```python
import glob
from jira_automation_example import WegJiraAutomation

automation = WegJiraAutomation()

# Alle Template-Dateien finden
templates = glob.glob("templates/WEG-*.md")

for template_file in templates:
    with open(template_file) as f:
        content = f.read()

    # Epic erstellen
    automation.create_epic(
        summary=extract_title(content),
        description=content,
        labels=extract_labels(content)
    )
```

### Git-Commit → JIRA Update

```python
import subprocess
import re
from jira_automation_example import WegJiraAutomation

def update_from_commits():
    automation = WegJiraAutomation()

    # Letzte Commits holen
    result = subprocess.run(
        ["git", "log", "--oneline", "-n", "10"],
        capture_output=True,
        text=True
    )

    for line in result.stdout.split('\n'):
        # Issue-Key extrahieren (z.B. "WEG-10")
        match = re.search(r'WEG-\d+', line)
        if match:
            issue_key = match.group(0)

            # Kommentar hinzufügen
            automation.add_comment(
                issue_key,
                f"Commit: {line}\n\n_Auto-posted by CI/CD_"
            )

            # Status auf "In Progress" setzen
            automation.transition_issue(issue_key, "In Progress")
```

### Health-Check-Report

```python
from jira_automation_example import WegJiraAutomation

def generate_health_report():
    automation = WegJiraAutomation()

    # Statistiken sammeln
    total = automation.jira.search_issues(f'project={automation.project_key}')
    in_progress = automation.jira.search_issues(f'project={automation.project_key} AND status="In Progress"')
    done = automation.jira.search_issues(f'project={automation.project_key} AND status=Done')

    # Report ausgeben
    print(f"📊 JIRA Health Report")
    print(f"{'=' * 60}")
    print(f"Total Issues: {len(total)}")
    print(f"In Progress:  {len(in_progress)}")
    print(f"Done:         {len(done)}")
    print(f"Completion:   {len(done)/len(total)*100:.1f}%")
```

---

## 🧪 Testing

### Dry-Run Mode

```python
# Keine echten Änderungen, nur Simulation
automation = WegJiraAutomation(dry_run=True)

automation.create_epic(...)  # Zeigt nur an, was passieren würde
```

### Unit Tests

```python
import pytest
from jira_automation_example import WegJiraAutomation

def test_credentials_validation():
    """Testet Credential-Validierung"""
    # Setup
    os.environ.pop("JIRA_API_TOKEN", None)

    # Test
    with pytest.raises(ValueError):
        WegJiraAutomation()

def test_epic_creation():
    """Testet Epic-Erstellung"""
    automation = WegJiraAutomation(dry_run=True)
    result = automation.create_epic("Test Epic", "Description")

    assert result is None  # In Dry-Run
```

---

## 🔄 CI/CD Integration

### GitHub Actions Beispiel

```yaml
name: Update JIRA

on:
  push:
    branches: [main]

jobs:
  update-jira:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install jira python-dotenv

      - name: Update JIRA from commits
        env:
          JIRA_BASE_URL: ${{ secrets.JIRA_BASE_URL }}
          JIRA_USERNAME: ${{ secrets.JIRA_USERNAME }}
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
          JIRA_PROJECT_KEY: WEG
        run: python jira_automation_example.py --update
```

---

## 📝 Changelog

### Version 1.0 (8. November 2025)
- ✅ Vollständige JIRA API Integration
- ✅ Python Helper-Klasse
- ✅ Funktionsfähige Beispiele
- ✅ Umfassende Dokumentation
- ✅ Security Best Practices

---

## 🤝 Support

- **Issues:** https://github.com/8chM/MyRep/issues
- **JIRA-Projekt:** https://maierharry.atlassian.net/browse/WEG
- **Confluence:** https://maierharry.atlassian.net/wiki/spaces/WEG

---

## 📄 Lizenz

Dieses Projekt ist für interne Verwendung im WEG Management System.

**Wichtig:** API-Credentials sind vertraulich und dürfen NICHT weitergegeben werden.
