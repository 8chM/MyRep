# 🤖 KI-Agent Orchestrator - Neue Dateien

**Download:** `KI_Agent_Orchestrator_NEW.zip` (20 KB)

---

## 📦 Inhalt

Dieses Archiv enthält **nur die neuen Dateien** aus der aktuellen Session:

```
KI_Agent_Orchestrator_NEW.zip
├── KI_AGENT_ROLES_AND_WORKFLOWS.md    (30 KB) - Rollen & Workflow-Definitionen
├── agent_orchestrator.py               (33 KB) - Haupttool (executable)
└── AGENT_QUICK_START.md                (12 KB) - 5-Minuten Setup-Guide
```

---

## 🎯 Was ist neu?

### 1. **8 Agent-Rollen** (KI_AGENT_ROLES_AND_WORKFLOWS.md)

Detaillierte Definitionen für:
- Planning Agent (Product Owner)
- Architecture Agent (Solution Architect)
- Backend Implementation Agent (C# Developer)
- Frontend Implementation Agent (React Developer)
- Infrastructure Agent (DevOps)
- Quality Assurance Agent (QA Tester)
- Review Agent (Tech Lead)
- Orchestration Agent (Scrum Master)

**Plus:**
- Kompletter Sprint-Workflow (Tag 0-14)
- Agent-Kommunikation via JIRA Comments
- Monitoring & Dashboards
- Error Handling & Recovery

### 2. **Orchestrator Tool** (agent_orchestrator.py)

Executable Python-Script zum Starten von Agents:

```bash
# Einzelner Task
python agent_orchestrator.py --task WEG-1004

# Kompletter Sprint
python agent_orchestrator.py --sprint Sprint-1

# Continuous Mode (alle 5 min)
python agent_orchestrator.py --continuous

# Dry-Run zum Testen
python agent_orchestrator.py --task WEG-1004 --dry-run
```

**Features:**
- ✅ Automatische Task-Kategorisierung
- ✅ JIRA Integration
- ✅ Context-Sammlung (Story, Epic, Acceptance Criteria)
- ✅ Prompt-Generierung für Claude Code Web
- ✅ 3 Modi: Single Task, Sprint, Continuous

### 3. **Quick Start Guide** (AGENT_QUICK_START.md)

5-Minuten Setup zum Loslegen:
- Installation
- JIRA Configuration
- Erste Schritte
- Troubleshooting
- Beispiele

---

## 🚀 Schnellstart

### 1. Download & Extract

```bash
# Download von GitHub
wget https://github.com/8chM/MyRep/raw/claude/test-plus-plus-011CUvkzGwhF8VdUvYP2jQhB/KI_Agent_Orchestrator_NEW.zip

# Oder via git clone
git clone https://github.com/8chM/MyRep.git
cd MyRep
git checkout claude/test-plus-plus-011CUvkzGwhF8VdUvYP2jQhB

# Extract
unzip KI_Agent_Orchestrator_NEW.zip
```

### 2. Install Dependencies

```bash
pip install jira python-dotenv
```

### 3. Configure JIRA

Wenn du noch keine `.env.jira.example` hast, erstelle sie:

```bash
cat > .env.jira.example << 'EOF'
JIRA_BASE_URL=https://maierharry.atlassian.net
JIRA_USERNAME=Maier.harry@gmail.com
JIRA_API_TOKEN=ATATT3xFfGF01UJdri3M_YGpv5B-njSIyifGVq5PMqALgO9xP3347K4VxJs0kvRLfNYAAYU3sxst1cflwbXCyqupN4RwbPJvxH_G-Ljf2mKOmpfn565g14-7py9YvOoj9p9k_8PUbtGkGfPNpu7HJuBpfJ30M9H6hWKx4c5A0ooqT_Y7YS_4jwE=A7AC83CA
JIRA_PROJECT_KEY=WEG
EOF
```

### 4. Run Orchestrator

```bash
# Test mit Dry-Run
python agent_orchestrator.py --task WEG-1004 --dry-run

# Echte Ausführung
python agent_orchestrator.py --task WEG-1004
```

**Output:**
```
✅ Agent Orchestrator initialized
📋 JIRA: https://maierharry.atlassian.net
🎯 Project: WEG

============================================================
🤖 Starting INFRASTRUCTURE Agent
📋 Task: WEG-1004 - Create docker-compose.yml
============================================================

💾 Saving agent prompt to file...
✅ Prompt saved to: /tmp/agent_prompt_WEG-1004.md

📝 Next Steps:
   1. Open Claude Code Web
   2. Paste the prompt from: /tmp/agent_prompt_WEG-1004.md
   3. Agent will implement the task autonomously
```

### 5. Führe Agent aus

1. Öffne Claude Code Web
2. Kopiere Prompt: `cat /tmp/agent_prompt_WEG-1004.md`
3. Paste in Claude Code Web
4. Agent implementiert autonom!

---

## 📚 Vollständige Dokumentation

Für die **komplette Infrastruktur** (inkl. JIRA Templates, API Guide, etc.), lade:

**`KI_Agent_Infrastructure.zip`** (75 KB - 11 Dateien)

---

## 🔗 GitHub Links

Wenn das Repository auf GitHub ist:

**Neue Dateien (20 KB):**
```
https://github.com/8chM/MyRep/raw/claude/test-plus-plus-011CUvkzGwhF8VdUvYP2jQhB/KI_Agent_Orchestrator_NEW.zip
```

**Vollständige Infrastruktur (75 KB):**
```
https://github.com/8chM/MyRep/raw/claude/test-plus-plus-011CUvkzGwhF8VdUvYP2jQhB/KI_Agent_Infrastructure.zip
```

**Einzelne Dateien:**
```
https://github.com/8chM/MyRep/raw/claude/test-plus-plus-011CUvkzGwhF8VdUvYP2jQhB/agent_orchestrator.py
https://github.com/8chM/MyRep/raw/claude/test-plus-plus-011CUvkzGwhF8VdUvYP2jQhB/KI_AGENT_ROLES_AND_WORKFLOWS.md
https://github.com/8chM/MyRep/raw/claude/test-plus-plus-011CUvkzGwhF8VdUvYP2jQhB/AGENT_QUICK_START.md
```

---

## 💡 Use Cases

### Use Case 1: Entwickle einen einzelnen Task

```bash
python agent_orchestrator.py --task WEG-1011
# Agent erstellt DatabaseOptions.cs + Tests
```

### Use Case 2: Entwickle kompletten Sprint

```bash
python agent_orchestrator.py --sprint Sprint-1
# Agent generiert Prompts für alle 15 Tasks
```

### Use Case 3: Dauerhafte Automatisierung

```bash
python agent_orchestrator.py --continuous
# Agent läuft kontinuierlich, überwacht JIRA alle 5 min
```

---

## ⚙️ Konfiguration

### Eigenes JIRA-Projekt

Edit `.env.jira.example`:

```bash
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_USERNAME=your-email@example.com
JIRA_API_TOKEN=your-api-token-here
JIRA_PROJECT_KEY=YOUR_PROJECT
```

### Eigene Agent-Prompts

Edit `agent_orchestrator.py` und passe die Methoden an:
- `generate_backend_agent_prompt()`
- `generate_frontend_agent_prompt()`
- `generate_infrastructure_agent_prompt()`

---

## 🎉 Das war's!

Du hast jetzt:
- ✅ 8 spezialisierte Agent-Rollen
- ✅ Executable Orchestrator
- ✅ Komplette Workflows
- ✅ Quick Start Guide

**Viel Erfolg mit autonomer Software-Entwicklung! 🚀**

---

## 📖 Weitere Ressourcen

Im vollständigen ZIP (`KI_Agent_Infrastructure.zip`):
- JIRA_API_Guide_for_KI_Agents.md
- JIRA_Templates_for_KI_Agents.md (2,355 Zeilen!)
- KI_AGENT_STRATEGY.md
- jira_automation_example.py
- und mehr...
