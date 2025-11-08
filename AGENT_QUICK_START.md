# 🚀 Quick Start: KI-Agent System für WEG Management

**Ziel:** Autonome Software-Entwicklung durch Claude Code Web KI-Agents

---

## 📋 Voraussetzungen

- ✅ Python 3.11+
- ✅ JIRA Account mit API-Token
- ✅ Zugriff auf Claude Code Web
- ✅ Git Repository

---

## ⚡ 5-Minuten Setup

### 1. Repository Setup

```bash
# Repository klonen
git clone https://github.com/8chM/MyRep.git
cd MyRep

# Python Dependencies installieren
pip install jira python-dotenv
```

### 2. JIRA Credentials konfigurieren

```bash
# .env Datei erstellen
cp .env.jira.example .env.jira

# Credentials eintragen (bereits vorkonfiguriert für WEG)
# Keine Änderungen nötig wenn du das WEG-Projekt nutzt
```

### 3. Test: JIRA Verbindung

```bash
# Teste JIRA Connection
python -c "
from jira import JIRA
import os
from dotenv import load_dotenv

load_dotenv('.env.jira.example')

jira = JIRA(
    server=os.getenv('JIRA_BASE_URL'),
    basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_API_TOKEN'))
)

issues = jira.search_issues('project=WEG', maxResults=5)
print(f'✅ Connected! Found {len(issues)} issues')
for issue in issues:
    print(f'  - {issue.key}: {issue.fields.summary}')
"
```

**Erwartete Ausgabe:**
```
✅ Connected! Found 5 issues
  - WEG-1: Platform Foundation (.NET 8 + SQL Server + React/Vite)
  - WEG-2: Identity & Access (Auth, RBAC, Invitations)
  - WEG-3: Tenant Provisioning & Admin (Associations as Schemas)
  ...
```

---

## 🎯 Erste Schritte: Einzelner Task

### Schritt 1: Finde einen Task

```bash
# Zeige alle "To Do" Tasks
python agent_orchestrator.py --task WEG-1004 --dry-run
```

**Output:**
```
✅ Agent Orchestrator initialized
📋 JIRA: https://maierharry.atlassian.net
🎯 Project: WEG
🧪 Dry Run: True

============================================================
🤖 Starting INFRASTRUCTURE Agent
📋 Task: WEG-1004 - Create docker-compose.yml
============================================================

[DRY RUN] Would execute infrastructure agent for WEG-1004
[DRY RUN] Prompt preview (first 500 chars):
# Infrastructure Agent - WEG Management System

## 🎯 Your Role
You are an Infrastructure Agent specialized in Docker, CI/CD...
```

### Schritt 2: Agent-Prompt generieren

```bash
# Generiere Prompt für Task (ohne --dry-run)
python agent_orchestrator.py --task WEG-1004
```

**Output:**
```
🤖 Starting INFRASTRUCTURE Agent
📋 Task: WEG-1004 - Create docker-compose.yml

💾 Saving agent prompt to file...
✅ Prompt saved to: /tmp/agent_prompt_WEG-1004.md

📝 Next Steps:
   1. Open Claude Code Web
   2. Paste the prompt from: /tmp/agent_prompt_WEG-1004.md
   3. Agent will implement the task autonomously
   4. Agent will update JIRA when done
```

### Schritt 3: Führe Agent aus

1. **Öffne Claude Code Web**
   - Gehe zu https://claude.ai/code (oder deine Claude Code Web Instanz)

2. **Paste Agent-Prompt**
   ```bash
   # Kopiere Prompt
   cat /tmp/agent_prompt_WEG-1004.md
   ```
   - Füge den kompletten Prompt in Claude Code Web ein

3. **Agent arbeitet autonom**
   - Agent liest Task-Beschreibung
   - Agent generiert Code aus Templates
   - Agent schreibt Dateien
   - Agent testet Code
   - Agent committed
   - Agent updated JIRA

4. **Verifiziere Ergebnis**
   ```bash
   # Check Git
   git log -1

   # Check JIRA
   python -c "
   from jira import JIRA
   import os
   from dotenv import load_dotenv

   load_dotenv('.env.jira.example')
   jira = JIRA(
       server=os.getenv('JIRA_BASE_URL'),
       basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_API_TOKEN'))
   )

   issue = jira.issue('WEG-1004')
   print(f'Status: {issue.fields.status.name}')
   comments = jira.comments(issue)
   if comments:
       print(f'Latest comment: {comments[-1].body[:200]}')
   "
   ```

---

## 🏃 Sprint-Modus: Batch Processing

### Kompletten Sprint verarbeiten

```bash
# Dry-Run: Zeige was passieren würde
python agent_orchestrator.py --sprint Sprint-1 --dry-run

# Echte Ausführung
python agent_orchestrator.py --sprint Sprint-1
```

**Output:**
```
🚀 Starting Sprint: Sprint-1

📊 Found 15 tasks ready for implementation

📊 Sprint Summary:
   Total Tasks: 15
   Backend: 8
   Frontend: 5
   Infrastructure: 2

============================================================
Task 1/15
🤖 Starting BACKEND Agent
📋 Task: WEG-1011 - Implement Options Pattern classes
============================================================

💾 Saving agent prompt to file...
✅ Prompt saved to: /tmp/agent_prompt_WEG-1011.md

📝 Next Steps:
   1. Open Claude Code Web
   2. Paste the prompt...
   [... für alle 15 Tasks ...]
```

---

## 🔄 Continuous Mode: Automatisches Monitoring

### Agent läuft kontinuierlich

```bash
# Startet Agent der alle 5 Minuten nach neuen Tasks sucht
python agent_orchestrator.py --continuous
```

**Output:**
```
🔄 Starting continuous mode...
   Monitoring JIRA for new tasks every 5 minutes
   Press Ctrl+C to stop

📊 Found 3 ready tasks

📋 Task 1/3
🤖 Starting BACKEND Agent
📋 Task: WEG-2001 - Create Association Entity
...

✅ No tasks ready - waiting...
[5 Minuten Pause]

📊 Found 1 ready task
...
```

---

## 📊 Monitoring & Dashboard (Optional)

### Streamlit Dashboard starten

```bash
# Install Streamlit
pip install streamlit pandas plotly

# Start Dashboard
streamlit run agent_dashboard.py
```

**Dashboard zeigt:**
- ✅ Aktive Agents
- 📊 Sprint Progress
- 📈 Velocity Charts
- ⚠️ Blockers
- 🔍 Recent Commits

---

## 🎭 Agent-Rollen Übersicht

| Agent | Trigger | Input | Output |
|-------|---------|-------|--------|
| **Backend Agent** | JIRA Sub-Task (labels: backend) | Task + Templates | C# Code + Tests + Commit |
| **Frontend Agent** | JIRA Sub-Task (labels: frontend) | Task + API Spec | React Components + Tests |
| **Infrastructure Agent** | JIRA Sub-Task (labels: infrastructure) | Task Description | Docker/CI/CD Files |
| **Review Agent** | Git Commit | Code Changes | Review Comments |
| **QA Agent** | Story completed | Acceptance Criteria | Test Results |

---

## 🛠️ Troubleshooting

### Problem: JIRA Connection Failed

```bash
# Check Credentials
cat .env.jira.example

# Test Connection
python -c "
from jira import JIRA
jira = JIRA('https://maierharry.atlassian.net', basic_auth=('Maier.harry@gmail.com', 'YOUR_TOKEN'))
print(jira.myself())
"
```

### Problem: No Tasks Found

```bash
# Check JIRA Query
python -c "
from jira import JIRA
import os
from dotenv import load_dotenv

load_dotenv('.env.jira.example')
jira = JIRA(
    server=os.getenv('JIRA_BASE_URL'),
    basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_API_TOKEN'))
)

# List all statuses
issues = jira.search_issues('project=WEG', maxResults=100)
statuses = set(issue.fields.status.name for issue in issues)
print(f'Available statuses: {statuses}')

# Check workflow
print(f'\\nWorkflow transitions for To Do tasks:')
for issue in issues:
    if issue.fields.status.name == 'To Do':
        print(f'{issue.key}: {issue.fields.summary}')
        break
"
```

### Problem: Agent Prompt zu lang für Claude

```bash
# Verkürze Prompt durch Entfernen von Context
# Edit agent_orchestrator.py und entferne:
# - Epic Description
# - Parent Description
# Behalte nur Task Description
```

---

## 📚 Nächste Schritte

### 1. Teste mit einem einfachen Task
```bash
# Finde einfachsten Task
python agent_orchestrator.py --sprint Sprint-1 --dry-run | grep "Infrastructure"

# Führe aus
python agent_orchestrator.py --task WEG-1007  # .env.example erstellen
```

### 2. Erweitere Agent-Prompts

Edit `agent_orchestrator.py` und passe Prompts an:
- Füge projekt-spezifische Coding Standards hinzu
- Füge bevorzugte Libraries hinzu
- Füge Custom Quality Checks hinzu

### 3. Automatisierung via CI/CD

```yaml
# .github/workflows/agent-orchestrator.yml
name: Agent Orchestrator

on:
  schedule:
    - cron: '0 */6 * * *'  # Alle 6 Stunden
  workflow_dispatch:

jobs:
  run-agents:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install Dependencies
        run: pip install jira python-dotenv
      - name: Run Orchestrator
        env:
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
        run: python agent_orchestrator.py --continuous
```

---

## 🎉 Erfolg!

Du hast jetzt:
- ✅ Agent Orchestrator konfiguriert
- ✅ JIRA Integration getestet
- ✅ Ersten Task mit Agent ausgeführt
- ✅ Verstanden wie das System funktioniert

**Nächster Meilenstein:** Kompletten Sprint (WEG-10) automatisiert entwickeln lassen!

---

## 📖 Weiterführende Dokumentation

- **Rollen & Workflows:** `KI_AGENT_ROLES_AND_WORKFLOWS.md`
- **Agent Strategie:** `KI_AGENT_STRATEGY.md`
- **JIRA Templates:** `JIRA_Templates_for_KI_Agents.md`
- **JIRA API Guide:** `JIRA_API_Guide_for_KI_Agents.md`

---

**Viel Erfolg mit autonomer Software-Entwicklung! 🚀**
