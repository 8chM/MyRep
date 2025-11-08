# JIRA API Anleitung für KI-Agenten
## Automatisierte Ticket-Verwaltung für WEG Management System

**Version:** 1.0
**Datum:** 8. November 2025
**Zweck:** Vollständige API-Referenz für KI-Agenten zur automatischen JIRA-Verwaltung

---

## 📚 Inhaltsverzeichnis

1. [Einleitung](#einleitung)
2. [Authentifizierung](#authentifizierung)
3. [Basis-Konfiguration](#basis-konfiguration)
4. [JIRA-Operationen](#jira-operationen)
   - Issues erstellen
   - Issues abrufen
   - Issues aktualisieren
   - Kommentare hinzufügen
   - Status-Übergänge
   - Attachments
5. [Python-Bibliothek](#python-bibliothek)
6. [Code-Beispiele](#code-beispiele)
7. [Best Practices](#best-practices)
8. [Fehlerbehandlung](#fehlerbehandlung)

---

## 🎯 Einleitung

### Zweck dieser Anleitung

Diese Anleitung ermöglicht KI-Agenten, programmatisch auf das JIRA-Projekt **WEG** (WEG Management System) zuzugreifen und:

- **Epics, Stories, Tasks und Subtasks** erstellen
- **Issues aktualisieren** (Beschreibung, Status, Assignee)
- **Kommentare hinzufügen** (Fortschritt, Fragen, Probleme)
- **Status-Übergänge** durchführen (To Do → In Progress → Done)
- **Attachments hochladen** (Code-Snippets, Screenshots, Logs)
- **Links zwischen Issues** erstellen (Blocker, Abhängigkeiten)

### Voraussetzungen

- Python 3.8+
- Internetverbindung
- Gültige JIRA API-Credentials
- Projekt-Key: `WEG`

---

## 🔐 Authentifizierung

### API-Zugangsdaten

JIRA Cloud verwendet **HTTP Basic Authentication** mit:
- **Username:** E-Mail-Adresse des Atlassian-Accounts
- **API Token:** Generierter Token (nicht das Account-Passwort!)

### Credentials sicher speichern

**❌ NIEMALS direkt im Code:**
```python
# FALSCH - Token im Code
API_TOKEN = "ATATT3xFfGF01..."  # NIEMALS SO!
```

**✅ Immer über Umgebungsvariablen:**
```python
# RICHTIG - Token aus Umgebungsvariable
import os
API_TOKEN = os.getenv("JIRA_API_TOKEN")
```

### Umgebungsvariablen setzen

**Linux/macOS:**
```bash
export JIRA_BASE_URL="https://maierharry.atlassian.net"
export JIRA_USERNAME="Maier.harry@gmail.com"
export JIRA_API_TOKEN="your-api-token-here"
export JIRA_PROJECT_KEY="WEG"
```

**Windows (PowerShell):**
```powershell
$env:JIRA_BASE_URL="https://maierharry.atlassian.net"
$env:JIRA_USERNAME="Maier.harry@gmail.com"
$env:JIRA_API_TOKEN="your-api-token-here"
$env:JIRA_PROJECT_KEY="WEG"
```

**Python (.env Datei):**
```python
# .env Datei (nicht committen!)
JIRA_BASE_URL=https://maierharry.atlassian.net
JIRA_USERNAME=Maier.harry@gmail.com
JIRA_API_TOKEN=your-api-token-here
JIRA_PROJECT_KEY=WEG
```

```python
# In Python laden
from dotenv import load_dotenv
load_dotenv()
```

---

## ⚙️ Basis-Konfiguration

### Python-Abhängigkeiten installieren

```bash
# Offizielle JIRA Python-Bibliothek
pip install jira

# Alternative: Requests für manuelle API-Calls
pip install requests

# Für .env Dateien
pip install python-dotenv
```

### Basis-Setup (Python)

```python
import os
from jira import JIRA

# Konfiguration aus Umgebungsvariablen
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "WEG")

# Validierung
if not all([JIRA_BASE_URL, JIRA_USERNAME, JIRA_API_TOKEN]):
    raise ValueError("JIRA credentials not set in environment variables!")

# JIRA Client initialisieren
jira = JIRA(
    server=JIRA_BASE_URL,
    basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN)
)

# Verbindung testen
try:
    user = jira.myself()
    print(f"✅ Connected as: {user['displayName']} ({user['emailAddress']})")
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

---

## 🛠️ JIRA-Operationen

### 1. Issue erstellen

#### Epic erstellen

```python
def create_epic(summary, description, custom_fields=None):
    """
    Erstellt ein Epic (Modul-Ebene)

    Args:
        summary: Titel des Epics (z.B. "WEG-1 – Platform Foundation")
        description: Detaillierte Beschreibung
        custom_fields: Dict mit Custom Fields

    Returns:
        JIRA Issue Object
    """
    issue_dict = {
        'project': {'key': JIRA_PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Epic'},
    }

    # Custom Fields hinzufügen (falls vorhanden)
    if custom_fields:
        issue_dict.update(custom_fields)

    epic = jira.create_issue(fields=issue_dict)
    print(f"✅ Epic created: {epic.key}")
    return epic

# Beispiel
epic = create_epic(
    summary="WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite)",
    description="""
# Executive Summary
Das Modul WEG-1 – Platform Foundation bildet das technische Fundament
des gesamten WEG Management Systems (WMS).

## Architecture
- Backend: .NET 8, ASP.NET Core
- Frontend: React 18, TypeScript 5
- Database: SQL Server 2022

## Links
- Confluence: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27165364
    """
)
```

#### Story erstellen (unter Epic)

```python
def create_story(summary, description, epic_key, labels=None):
    """
    Erstellt eine Story und verknüpft sie mit einem Epic

    Args:
        summary: Titel der Story
        description: Detaillierte Beschreibung
        epic_key: Key des Parent-Epics (z.B. "WEG-1")
        labels: Liste von Labels (z.B. ["backend", "infrastructure"])

    Returns:
        JIRA Issue Object
    """
    issue_dict = {
        'project': {'key': JIRA_PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Story'},
        'labels': labels or [],
    }

    story = jira.create_issue(fields=issue_dict)

    # Story mit Epic verknüpfen
    jira.add_issues_to_epic(epic_key, [story.key])

    print(f"✅ Story created: {story.key} (linked to {epic_key})")
    return story

# Beispiel
story = create_story(
    summary="WEG-10 – Solution Setup & Infrastructure",
    description="""
## User Story
As a Developer
I want a standardized project structure
So that I can quickly understand and extend the codebase

## Technical Approach
- Clean Architecture (Api, Application, Domain, Infrastructure)
- Docker Compose setup
- EF Core Migrations
    """,
    epic_key="WEG-1",
    labels=["infrastructure", "setup"]
)
```

#### Task erstellen (unter Story)

```python
def create_task(summary, description, parent_key, assignee=None, priority="Medium"):
    """
    Erstellt einen Task unter einer Story

    Args:
        summary: Titel des Tasks
        description: Detaillierte Beschreibung
        parent_key: Key der Parent-Story (z.B. "WEG-10")
        assignee: Account-ID des Assignees (optional)
        priority: Priorität (Highest, High, Medium, Low, Lowest)

    Returns:
        JIRA Issue Object
    """
    issue_dict = {
        'project': {'key': JIRA_PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'},
        'parent': {'key': parent_key},
        'priority': {'name': priority}
    }

    if assignee:
        issue_dict['assignee'] = {'accountId': assignee}

    task = jira.create_issue(fields=issue_dict)
    print(f"✅ Task created: {task.key} (child of {parent_key})")
    return task

# Beispiel
task = create_task(
    summary="Implement Domain Entities",
    description="""
## Objective
Create domain entities for Association, Building, and Unit

## Files to Create
- src/WegManagement.Domain/Entities/Association.cs
- src/WegManagement.Domain/Entities/Building.cs
- src/WegManagement.Domain/Entities/Unit.cs

## Acceptance Criteria
- [ ] All entities created with factory methods
- [ ] Validation implemented
- [ ] Unit tests written (>= 80% coverage)
    """,
    parent_key="WEG-10",
    priority="High"
)
```

#### Subtask erstellen

```python
def create_subtask(summary, description, parent_key):
    """
    Erstellt einen Subtask unter einem Task

    Args:
        summary: Titel des Subtasks
        description: Detaillierte Beschreibung
        parent_key: Key des Parent-Tasks

    Returns:
        JIRA Issue Object
    """
    issue_dict = {
        'project': {'key': JIRA_PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Sub-task'},
        'parent': {'key': parent_key}
    }

    subtask = jira.create_issue(fields=issue_dict)
    print(f"✅ Subtask created: {subtask.key} (child of {parent_key})")
    return subtask

# Beispiel
subtask = create_subtask(
    summary="Write Unit Tests for Association Entity",
    description="""
## Test Cases
- Create_WithValidData_ShouldSucceed
- Create_WithInvalidName_ShouldThrowException
- UpdateDetails_ShouldUpdateFields
- Deactivate_ShouldSetStatusToInactive

## File
tests/WegManagement.Domain.Tests/Entities/AssociationTests.cs
    """,
    parent_key="WEG-10-1"
)
```

---

### 2. Issue abrufen

```python
# Issue per Key abrufen
issue = jira.issue('WEG-10')
print(f"Summary: {issue.fields.summary}")
print(f"Status: {issue.fields.status.name}")
print(f"Assignee: {issue.fields.assignee}")
print(f"Description: {issue.fields.description}")

# Alle Issues in einem Projekt
issues = jira.search_issues(f'project={JIRA_PROJECT_KEY}', maxResults=100)
for issue in issues:
    print(f"{issue.key}: {issue.fields.summary}")

# Issues mit JQL (JIRA Query Language)
jql = f'project={JIRA_PROJECT_KEY} AND status="In Progress" AND assignee=currentUser()'
my_issues = jira.search_issues(jql)

# Issue mit allen Details
issue = jira.issue('WEG-10', expand='changelog,renderedFields')
```

---

### 3. Issue aktualisieren

```python
def update_issue(issue_key, fields_to_update):
    """
    Aktualisiert ein Issue

    Args:
        issue_key: Key des Issues (z.B. "WEG-10")
        fields_to_update: Dict mit zu aktualisierenden Feldern
    """
    issue = jira.issue(issue_key)
    issue.update(fields=fields_to_update)
    print(f"✅ Issue {issue_key} updated")

# Beispiel: Beschreibung aktualisieren
update_issue('WEG-10', {
    'description': 'Updated description with more details...'
})

# Beispiel: Assignee setzen
update_issue('WEG-10', {
    'assignee': {'accountId': '712020:abcd1234-5678-90ef-ghij-klmnopqrstuv'}
})

# Beispiel: Priority ändern
update_issue('WEG-10', {
    'priority': {'name': 'High'}
})

# Beispiel: Labels hinzufügen
issue = jira.issue('WEG-10')
issue.fields.labels.append('urgent')
issue.update(fields={'labels': issue.fields.labels})

# Beispiel: Custom Fields aktualisieren
update_issue('WEG-10', {
    'customfield_10001': 'Backend'  # Tech Stack
})
```

---

### 4. Kommentare hinzufügen

```python
def add_comment(issue_key, comment_text):
    """
    Fügt einen Kommentar zu einem Issue hinzu

    Args:
        issue_key: Key des Issues
        comment_text: Kommentar-Text (unterstützt Markdown/Wiki-Syntax)
    """
    jira.add_comment(issue_key, comment_text)
    print(f"✅ Comment added to {issue_key}")

# Einfacher Kommentar
add_comment('WEG-10', 'Work started on this task')

# Kommentar mit Formatierung
add_comment('WEG-10', '''
*Progress Update:*

Completed:
- [x] Project structure created
- [x] Docker Compose configured
- [x] README documented

Next Steps:
- [ ] Database migrations
- [ ] API endpoints

_Estimated completion: 2 days_
''')

# Kommentar mit Code-Block
add_comment('WEG-10', '''
Implementation details:

{code:csharp}
public class Association : BaseEntity
{
    public Guid Id { get; private set; }
    public string Name { get; private set; }
}
{code}
''')

# Kommentar mit Mention
add_comment('WEG-10', '[~accountId:712020:abc123] Please review this implementation')
```

---

### 5. Status-Übergänge

```python
def transition_issue(issue_key, transition_name):
    """
    Führt einen Status-Übergang durch

    Args:
        issue_key: Key des Issues
        transition_name: Name des Übergangs (z.B. "In Progress", "Done")
    """
    # Verfügbare Übergänge abrufen
    transitions = jira.transitions(issue_key)

    # Passenden Übergang finden
    transition_id = None
    for t in transitions:
        if t['name'].lower() == transition_name.lower():
            transition_id = t['id']
            break

    if transition_id:
        jira.transition_issue(issue_key, transition_id)
        print(f"✅ Issue {issue_key} transitioned to '{transition_name}'")
    else:
        available = [t['name'] for t in transitions]
        print(f"❌ Transition '{transition_name}' not available. Available: {available}")

# Beispiele
transition_issue('WEG-10', 'In Progress')
transition_issue('WEG-10', 'Done')
transition_issue('WEG-10', 'To Do')

# Verfügbare Übergänge anzeigen
def show_transitions(issue_key):
    transitions = jira.transitions(issue_key)
    print(f"Available transitions for {issue_key}:")
    for t in transitions:
        print(f"  - {t['name']} (ID: {t['id']})")

show_transitions('WEG-10')
```

---

### 6. Attachments hochladen

```python
def add_attachment(issue_key, file_path, filename=None):
    """
    Lädt ein Attachment zu einem Issue hoch

    Args:
        issue_key: Key des Issues
        file_path: Pfad zur Datei
        filename: Optionaler Dateiname (default: Dateiname aus file_path)
    """
    with open(file_path, 'rb') as f:
        jira.add_attachment(
            issue=issue_key,
            attachment=f,
            filename=filename
        )
    print(f"✅ Attachment added to {issue_key}: {file_path}")

# Beispiel: Screenshot hochladen
add_attachment('WEG-10', '/path/to/screenshot.png', 'error-screenshot.png')

# Beispiel: Log-Datei hochladen
add_attachment('WEG-10', 'logs/build.log', 'build-error.log')

# Beispiel: Code-Datei hochladen
add_attachment('WEG-10', 'src/Domain/Entities/Association.cs')

# Text-Snippet als Attachment
def add_text_attachment(issue_key, content, filename):
    """Erstellt Text-Datei und lädt sie hoch"""
    import tempfile

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write(content)
        temp_path = f.name

    add_attachment(issue_key, temp_path, filename)

    # Temporäre Datei löschen
    import os
    os.unlink(temp_path)

# Beispiel: Test-Output hochladen
add_text_attachment('WEG-10', '''
Test Results:
=============
Passed: 45
Failed: 3
Skipped: 2
''', 'test-results.txt')
```

---

### 7. Issue-Links erstellen

```python
def link_issues(inward_issue, outward_issue, link_type="Blocks"):
    """
    Erstellt einen Link zwischen zwei Issues

    Args:
        inward_issue: Key des ersten Issues (z.B. "WEG-1")
        outward_issue: Key des zweiten Issues (z.B. "WEG-10")
        link_type: Art der Verknüpfung (Blocks, Relates, Duplicates, etc.)
    """
    jira.create_issue_link(
        type=link_type,
        inwardIssue=inward_issue,
        outwardIssue=outward_issue
    )
    print(f"✅ Linked {inward_issue} {link_type} {outward_issue}")

# Beispiel: WEG-10 wird blockiert durch WEG-1
link_issues("WEG-1", "WEG-10", "Blocks")

# Beispiel: WEG-20 hängt zusammen mit WEG-21
link_issues("WEG-20", "WEG-21", "Relates")

# Beispiel: WEG-30 ist Duplikat von WEG-29
link_issues("WEG-30", "WEG-29", "Duplicates")
```

---

## 📦 Python-Bibliothek: JIRA Helper

### Vollständige Helper-Klasse

```python
"""
jira_helper.py - Wrapper für JIRA-Operationen
"""
import os
from typing import Optional, List, Dict
from jira import JIRA


class JiraHelper:
    """Helper-Klasse für JIRA-Operationen"""

    def __init__(self):
        """Initialisiert JIRA-Client mit Credentials aus Umgebungsvariablen"""
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.username = os.getenv("JIRA_USERNAME")
        self.api_token = os.getenv("JIRA_API_TOKEN")
        self.project_key = os.getenv("JIRA_PROJECT_KEY", "WEG")

        if not all([self.base_url, self.username, self.api_token]):
            raise ValueError(
                "JIRA credentials not set! Please set:\n"
                "  JIRA_BASE_URL\n"
                "  JIRA_USERNAME\n"
                "  JIRA_API_TOKEN"
            )

        self.jira = JIRA(
            server=self.base_url,
            basic_auth=(self.username, self.api_token)
        )

    def create_epic(
        self,
        summary: str,
        description: str,
        labels: Optional[List[str]] = None
    ):
        """Erstellt ein Epic"""
        issue_dict = {
            'project': {'key': self.project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Epic'},
            'labels': labels or []
        }

        epic = self.jira.create_issue(fields=issue_dict)
        print(f"✅ Epic created: {epic.key} - {summary}")
        return epic

    def create_story(
        self,
        summary: str,
        description: str,
        epic_key: str,
        labels: Optional[List[str]] = None
    ):
        """Erstellt eine Story unter einem Epic"""
        issue_dict = {
            'project': {'key': self.project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Story'},
            'labels': labels or []
        }

        story = self.jira.create_issue(fields=issue_dict)
        self.jira.add_issues_to_epic(epic_key, [story.key])

        print(f"✅ Story created: {story.key} - {summary} (under {epic_key})")
        return story

    def create_task(
        self,
        summary: str,
        description: str,
        parent_key: str,
        assignee: Optional[str] = None,
        priority: str = "Medium"
    ):
        """Erstellt einen Task unter einer Story"""
        issue_dict = {
            'project': {'key': self.project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Task'},
            'parent': {'key': parent_key},
            'priority': {'name': priority}
        }

        if assignee:
            issue_dict['assignee'] = {'accountId': assignee}

        task = self.jira.create_issue(fields=issue_dict)
        print(f"✅ Task created: {task.key} - {summary}")
        return task

    def add_comment(self, issue_key: str, comment: str):
        """Fügt Kommentar hinzu"""
        self.jira.add_comment(issue_key, comment)
        print(f"✅ Comment added to {issue_key}")

    def transition(self, issue_key: str, transition_name: str):
        """Führt Status-Übergang durch"""
        transitions = self.jira.transitions(issue_key)

        for t in transitions:
            if t['name'].lower() == transition_name.lower():
                self.jira.transition_issue(issue_key, t['id'])
                print(f"✅ {issue_key} → {transition_name}")
                return

        available = [t['name'] for t in transitions]
        raise ValueError(
            f"Transition '{transition_name}' not available. "
            f"Available: {available}"
        )

    def update_description(self, issue_key: str, description: str):
        """Aktualisiert Issue-Beschreibung"""
        issue = self.jira.issue(issue_key)
        issue.update(fields={'description': description})
        print(f"✅ Description updated: {issue_key}")

    def add_attachment(self, issue_key: str, file_path: str):
        """Lädt Attachment hoch"""
        with open(file_path, 'rb') as f:
            self.jira.add_attachment(issue=issue_key, attachment=f)
        print(f"✅ Attachment added to {issue_key}: {file_path}")

    def search(self, jql: str, max_results: int = 50):
        """Sucht Issues mit JQL"""
        return self.jira.search_issues(jql, maxResults=max_results)


# Verwendung:
if __name__ == "__main__":
    helper = JiraHelper()

    # Epic erstellen
    epic = helper.create_epic(
        summary="WEG-1 – Platform Foundation",
        description="Technical foundation module",
        labels=["infrastructure", "foundation"]
    )

    # Story erstellen
    story = helper.create_story(
        summary="WEG-10 – Solution Setup",
        description="Project structure and Docker setup",
        epic_key=epic.key,
        labels=["backend"]
    )

    # Task erstellen
    task = helper.create_task(
        summary="Implement Domain Entities",
        description="Create Association, Building, Unit entities",
        parent_key=story.key,
        priority="High"
    )

    # Kommentar hinzufügen
    helper.add_comment(task.key, "Started implementation")

    # Status ändern
    helper.transition(task.key, "In Progress")
```

---

## 💡 Code-Beispiele

### Beispiel 1: Batch-Import von Issues aus Template

```python
"""
batch_create_issues.py - Erstellt alle Issues für ein Modul
"""
from jira_helper import JiraHelper

def create_weg_1_module():
    """Erstellt alle Issues für WEG-1 – Platform Foundation"""
    helper = JiraHelper()

    # Epic erstellen
    epic = helper.create_epic(
        summary="WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite)",
        description=open("templates/WEG-1-epic.md").read(),
        labels=["infrastructure", "backend", "frontend"]
    )

    # Stories erstellen
    stories_data = [
        {
            'summary': 'WEG-10 – Solution Setup & Infrastructure',
            'file': 'templates/WEG-10-story.md',
            'labels': ['infrastructure']
        },
        {
            'summary': 'WEG-11 – API, OpenAPI & TypeScript Client',
            'file': 'templates/WEG-11-story.md',
            'labels': ['backend', 'frontend']
        },
        {
            'summary': 'WEG-12 – Error Handling, Logging & Health',
            'file': 'templates/WEG-12-story.md',
            'labels': ['backend', 'observability']
        }
    ]

    for story_data in stories_data:
        story = helper.create_story(
            summary=story_data['summary'],
            description=open(story_data['file']).read(),
            epic_key=epic.key,
            labels=story_data['labels']
        )

        # Tasks für jede Story erstellen
        create_tasks_for_story(helper, story.key, story_data['summary'])

    print(f"\n✅ Module WEG-1 created with Epic {epic.key}")


def create_tasks_for_story(helper, story_key, story_summary):
    """Erstellt Tasks basierend auf Story-Template"""

    # Beispiel-Tasks für WEG-10
    if "WEG-10" in story_summary:
        tasks = [
            {
                'summary': 'Create Solution Structure',
                'description': '...',
                'priority': 'High'
            },
            {
                'summary': 'Setup Docker Compose',
                'description': '...',
                'priority': 'High'
            },
            {
                'summary': 'Write Developer README',
                'description': '...',
                'priority': 'Medium'
            }
        ]

        for task_data in tasks:
            helper.create_task(
                summary=task_data['summary'],
                description=task_data['description'],
                parent_key=story_key,
                priority=task_data['priority']
            )


if __name__ == "__main__":
    create_weg_1_module()
```

---

### Beispiel 2: Automatisches Progress-Update

```python
"""
auto_update_progress.py - Automatisiert Status-Updates basierend auf Git-Commits
"""
import subprocess
from jira_helper import JiraHelper

def get_recent_commits(branch="main", count=10):
    """Holt letzte Git-Commits"""
    cmd = f"git log {branch} --oneline -n {count}"
    result = subprocess.run(cmd.split(), capture_output=True, text=True)
    return result.stdout.strip().split('\n')

def extract_issue_key(commit_message):
    """Extrahiert JIRA Issue-Key aus Commit-Message"""
    import re
    match = re.search(r'WEG-\d+', commit_message)
    return match.group(0) if match else None

def update_jira_from_commits():
    """Aktualisiert JIRA basierend auf Git-Commits"""
    helper = JiraHelper()
    commits = get_recent_commits()

    for commit in commits:
        issue_key = extract_issue_key(commit)

        if issue_key:
            # Kommentar mit Commit-Info hinzufügen
            helper.add_comment(
                issue_key,
                f"Commit: {commit}\n\n_Automatically posted by CI/CD_"
            )

            # Status auf "In Progress" setzen (falls noch "To Do")
            try:
                helper.transition(issue_key, "In Progress")
            except:
                pass  # Already in progress or different status

if __name__ == "__main__":
    update_jira_from_commits()
```

---

### Beispiel 3: Issue-Report generieren

```python
"""
generate_report.py - Erstellt Fortschritts-Report
"""
from jira_helper import JiraHelper
from collections import defaultdict

def generate_progress_report(epic_key="WEG-1"):
    """Generiert Report für Epic"""
    helper = JiraHelper()

    # Alle Issues im Epic suchen
    jql = f'"Epic Link" = {epic_key}'
    issues = helper.search(jql, max_results=200)

    # Statistiken sammeln
    stats = defaultdict(int)
    by_status = defaultdict(list)

    for issue in issues:
        issue_type = issue.fields.issuetype.name
        status = issue.fields.status.name

        stats[f"{issue_type}_{status}"] += 1
        by_status[status].append(issue.key)

    # Report ausgeben
    print(f"\n📊 Progress Report: {epic_key}")
    print("=" * 60)

    print("\n📈 Status Overview:")
    for status, issue_keys in by_status.items():
        print(f"  {status}: {len(issue_keys)} issues")
        for key in issue_keys[:5]:  # Zeige max. 5
            print(f"    - {key}")

    # Completion-Rate berechnen
    total = len(issues)
    done = len(by_status.get('Done', []))
    completion = (done / total * 100) if total > 0 else 0

    print(f"\n✅ Completion Rate: {completion:.1f}% ({done}/{total})")

    return stats

if __name__ == "__main__":
    generate_progress_report("WEG-1")
```

---

## 🎯 Best Practices für KI-Agenten

### 1. Immer Credentials prüfen

```python
def validate_credentials():
    """Prüft ob alle Credentials gesetzt sind"""
    required = ["JIRA_BASE_URL", "JIRA_USERNAME", "JIRA_API_TOKEN"]
    missing = [var for var in required if not os.getenv(var)]

    if missing:
        raise ValueError(f"Missing environment variables: {missing}")

# Am Anfang jedes Scripts
validate_credentials()
```

### 2. Error Handling implementieren

```python
from jira.exceptions import JIRAError

def safe_create_issue(helper, **kwargs):
    """Erstellt Issue mit Fehlerbehandlung"""
    try:
        return helper.create_task(**kwargs)
    except JIRAError as e:
        print(f"❌ JIRA Error: {e.text}")
        print(f"   Status Code: {e.status_code}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None
```

### 3. Rate Limiting beachten

```python
import time

def bulk_create_with_delay(items, delay=1.0):
    """Erstellt Issues mit Verzögerung (Rate Limiting)"""
    created = []

    for i, item in enumerate(items, 1):
        issue = create_issue(item)
        created.append(issue)

        if i < len(items):
            time.sleep(delay)  # 1 Sekunde Pause

    return created
```

### 4. Dry-Run Mode implementieren

```python
class JiraHelper:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        # ... rest of init

    def create_task(self, **kwargs):
        if self.dry_run:
            print(f"[DRY RUN] Would create task: {kwargs['summary']}")
            return None

        # Actual creation
        return self.jira.create_issue(fields=kwargs)

# Verwendung
helper = JiraHelper(dry_run=True)  # Test mode
helper.create_task(...)  # Erstellt nichts, nur Ausgabe
```

### 5. Logging implementieren

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_task_with_logging(helper, **kwargs):
    logger.info(f"Creating task: {kwargs['summary']}")
    try:
        issue = helper.create_task(**kwargs)
        logger.info(f"✅ Task created: {issue.key}")
        return issue
    except Exception as e:
        logger.error(f"❌ Failed to create task: {e}")
        raise
```

---

## 🚨 Fehlerbehandlung

### Häufige Fehler und Lösungen

#### 1. Authentifizierungsfehler (401)
```python
# Fehler:
# JIRAError: HTTP 401: Unauthorized

# Lösung:
# - Prüfe API-Token
# - Prüfe Username (muss E-Mail sein)
# - Token könnte abgelaufen sein (neu generieren)
```

#### 2. Fehlende Berechtigung (403)
```python
# Fehler:
# JIRAError: HTTP 403: Forbidden

# Lösung:
# - Account hat keine Berechtigung für diese Operation
# - Projekt-Einstellungen prüfen
# - Admin-Rechte erforderlich?
```

#### 3. Issue nicht gefunden (404)
```python
# Fehler:
# JIRAError: HTTP 404: Issue Does Not Exist

# Lösung:
# - Issue-Key korrekt? (z.B. "WEG-10" nicht "WEG10")
# - Issue existiert im Projekt?
# - Zugriffsberechtigung vorhanden?
```

#### 4. Validierungsfehler (400)
```python
# Fehler:
# JIRAError: HTTP 400: Field 'xyz' is required

# Lösung:
# - Pflichtfelder prüfen
# - Feldtypen validieren
# - Custom Fields korrekt referenzieren
```

### Robuste Fehlerbehandlung

```python
def create_issue_robust(helper, max_retries=3, **kwargs):
    """Erstellt Issue mit Retry-Logik"""
    from time import sleep

    for attempt in range(max_retries):
        try:
            return helper.create_task(**kwargs)

        except JIRAError as e:
            if e.status_code == 401:
                raise  # Auth-Fehler nicht retryable

            elif e.status_code == 429:  # Rate limit
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"⏳ Rate limit hit, waiting {wait_time}s...")
                sleep(wait_time)

            elif e.status_code >= 500:  # Server error
                if attempt < max_retries - 1:
                    print(f"🔄 Server error, retry {attempt + 1}/{max_retries}")
                    sleep(2)
                else:
                    raise

            else:
                raise  # Andere Fehler sofort werfen

    raise Exception(f"Failed after {max_retries} retries")
```

---

## 📚 Referenzen

### JIRA REST API Dokumentation
- **Official Docs:** https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/
- **Python Library:** https://jira.readthedocs.io/
- **API Explorer:** https://maierharry.atlassian.net/rest/api/3/

### Nützliche JQL-Queries

```sql
-- Alle offenen Issues im Projekt
project = WEG AND status != Done

-- Meine aktuellen Tasks
assignee = currentUser() AND status = "In Progress"

-- High-Priority Issues ohne Assignee
priority = High AND assignee is EMPTY

-- Alle Epics
issuetype = Epic AND project = WEG

-- Issues erstellt in letzten 7 Tagen
created >= -7d AND project = WEG

-- Überfällige Issues
dueDate < now() AND status != Done

-- Issues mit bestimmtem Label
labels = "backend" AND project = WEG
```

### Custom Fields finden

```python
# Alle Custom Fields anzeigen
fields = jira.fields()
for field in fields:
    if 'custom' in field['id']:
        print(f"{field['name']}: {field['id']}")
```

---

## 🔒 Sicherheit

### Wichtige Sicherheitsregeln

1. **NIEMALS Credentials committen**
   - Verwende `.gitignore` für `.env` Dateien
   - Prüfe vor jedem Commit

2. **API-Token rotieren**
   - Token alle 90 Tage erneuern
   - Bei Verdacht auf Kompromittierung sofort widerrufen

3. **Least Privilege Prinzip**
   - Token nur mit notwendigen Berechtigungen
   - Separate Tokens für unterschiedliche Zwecke

4. **Logging vorsichtig**
   - Credentials NICHT loggen
   - Sanitize Log-Output

```python
# ✅ Sicher
logger.info(f"Creating issue in project {project_key}")

# ❌ UNSICHER
logger.info(f"Using token {api_token}")  # NIEMALS!
```

---

## 📝 Zusammenfassung

Diese Anleitung ermöglicht KI-Agenten:

✅ **JIRA-Issues erstellen** (Epics, Stories, Tasks, Subtasks)
✅ **Issues aktualisieren** (Beschreibung, Status, Assignee)
✅ **Kommentare hinzufügen** (Progress-Updates, Fragen)
✅ **Status-Übergänge** (To Do → In Progress → Done)
✅ **Attachments hochladen** (Code, Logs, Screenshots)
✅ **Issues verknüpfen** (Dependencies, Blockers)
✅ **Batch-Operationen** (Bulk-Import, Reports)

**Best Practices:**
- Credentials sicher über Umgebungsvariablen
- Error Handling & Retry-Logik
- Rate Limiting beachten
- Dry-Run Mode für Tests
- Comprehensive Logging

---

**Version:** 1.0
**Letzte Aktualisierung:** 8. November 2025
**Support:** [GitHub Issues](https://github.com/8chM/MyRep/issues)
