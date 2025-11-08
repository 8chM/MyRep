# KI-Agent Strategie für WEG Management System

**Ziel:** Vollständig autonome Entwicklung des WEG Management Systems durch KI-Agenten mit JIRA als zentralem Koordinationssystem.

---

## 📋 Übersicht

Diese Strategie definiert, wie KI-Agenten (wie Claude, GitHub Copilot, oder spezialisierte Code-Agenten) das WEG-Projekt vollständig entwickeln können:

1. **JIRA als Single Source of Truth** - Alle Aufgaben, Status und Abhängigkeiten in JIRA
2. **Confluence als Wissensbasis** - Architektur-Dokumentation und Kontext
3. **Automatisierte Workflows** - Agent liest Task → implementiert → updated JIRA → commitet Code
4. **Zero Human Intervention** - Agent entscheidet selbstständig über Implementierungsdetails

---

## 🎯 Agent-Typen und Rollen

### 1. **Planning Agent** (Strategie & Priorisierung)
**Aufgabe:** Analysiert JIRA, plant Sprint-Inhalte, priorisiert Tasks

**Workflow:**
```python
def planning_agent():
    # 1. Lese alle offenen Epics/Stories
    epics = jira.search_issues('project=WEG AND type=Epic AND status=Backlog')

    # 2. Analysiere Abhängigkeiten
    dependencies = analyze_confluence_dependencies()

    # 3. Erstelle Dependency-Graph
    graph = build_dependency_graph(epics, dependencies)

    # 4. Priorisiere: Foundation → Identity → Tenant → Features
    priority_order = topological_sort(graph)

    # 5. Erstelle Sprint-Plan
    sprint = create_sprint_plan(priority_order, capacity=40h)

    # 6. Aktualisiere JIRA Sprints
    assign_issues_to_sprint(sprint)
```

**Input:**
- Confluence Dokumentation (WEG-1 bis WEG-9)
- JIRA Epic/Story Hierarchie
- Technische Abhängigkeiten (z.B. WEG-10 vor WEG-1)

**Output:**
- Sprint-Plan mit priorisierten Stories
- Dependency-Matrix in JIRA
- Risikoanalyse für kritische Pfade

**Tools:**
- `jira.search_issues()` - Issue-Queries
- `jira.create_sprint()` - Sprint-Management
- Confluence API - Dokumentation lesen

---

### 2. **Implementation Agent** (Code-Entwicklung)
**Aufgabe:** Implementiert konkrete Sub-Tasks mit Code

**Workflow:**
```python
def implementation_agent(subtask_key):
    # 1. JIRA Sub-Task lesen
    task = jira.issue(subtask_key)
    description = task.fields.description

    # 2. Kontext aus Parent Story holen
    story = jira.issue(task.fields.parent.key)
    epic_key = story.fields.customfield_epiclink
    epic = jira.issue(epic_key)

    # 3. Confluence Dokumentation lesen
    confluence_page = get_confluence_page_for_epic(epic_key)
    architecture = parse_architecture(confluence_page)

    # 4. Code generieren
    code = generate_code(
        task=description,
        story=story.fields.description,
        architecture=architecture,
        templates=load_jira_templates()
    )

    # 5. Tests generieren
    tests = generate_tests(code, task)

    # 6. Code committen
    git_commit(code, tests, message=f"{subtask_key}: {task.fields.summary}")

    # 7. JIRA aktualisieren
    jira.transition_issue(subtask_key, "In Progress")
    jira.add_comment(subtask_key, f"✅ Implementation complete\n\nFiles:\n{list_files(code)}")

    # 8. Wenn alle Tests grün: Status auf Done
    if run_tests_passing():
        jira.transition_issue(subtask_key, "Done")
```

**Input:**
- JIRA Sub-Task mit vollständiger Beschreibung
- Parent Story mit Acceptance Criteria
- Epic mit Architektur-Kontext
- Confluence Seite mit Domain-Modell

**Output:**
- Funktionierender Code (C#, TypeScript, SQL)
- Unit Tests (xUnit, Vitest)
- Integration Tests (Playwright)
- Git Commit mit JIRA-Key
- JIRA Comment mit Implementierungsdetails

**Beispiel Sub-Task:**
```
WEG-1011 - Implement Options Pattern classes for all configurations

## Implementation
Create options classes in `src/WegManagement.Infrastructure/Configuration/`:

[Vollständiger C# Code in JIRA Description]

## Verification
- dotnet build succeeds
- All classes have SectionName constant
- Options validated on startup
```

**Code-Generierung:**
```csharp
// Agent liest Beschreibung und generiert:
namespace WegManagement.Infrastructure.Configuration;

public class DatabaseOptions
{
    public const string SectionName = "ConnectionStrings";
    public string DefaultConnection { get; set; } = string.Empty;
    public string DirectoryConnection { get; set; } = string.Empty;
    // ... (aus Template)
}
```

**Tools:**
- File Operations (Read, Write, Edit)
- Bash (dotnet build, dotnet test, git)
- JIRA API (transition, comment)

---

### 3. **Review Agent** (Code-Review & Qualitätssicherung)
**Aufgabe:** Überprüft implementierten Code auf Standards, Best Practices, Tests

**Workflow:**
```python
def review_agent(commit_sha):
    # 1. Finde zugehörigen JIRA Sub-Task aus Commit-Message
    commit_message = git_log(commit_sha)
    subtask_key = extract_jira_key(commit_message)  # z.B. "WEG-1011"

    # 2. Hole Task-Requirements
    task = jira.issue(subtask_key)
    acceptance_criteria = parse_acceptance_criteria(task.fields.parent)

    # 3. Code-Analyse
    changed_files = git_diff(commit_sha)

    issues = []

    # 3a. Static Analysis
    issues += run_dotnet_format_check()
    issues += run_eslint()

    # 3b. Test Coverage
    coverage = run_code_coverage()
    if coverage < 80:
        issues.append(f"❌ Coverage {coverage}% < 80%")

    # 3c. Architecture Compliance
    if violates_clean_architecture(changed_files):
        issues.append("❌ Layer violation: Domain depends on Infrastructure")

    # 3d. Naming Conventions (aus WEG-19)
    if not follows_naming_conventions(changed_files):
        issues.append("❌ Use English names, not German")

    # 3e. Security Scan
    security_issues = run_security_scan(changed_files)
    issues += security_issues

    # 4. Review-Ergebnis
    if issues:
        jira.add_comment(subtask_key, f"🔍 **Review Issues:**\n" + "\n".join(issues))
        jira.transition_issue(subtask_key, "In Review - Changes Requested")
        return False
    else:
        jira.add_comment(subtask_key, "✅ **Review Passed** - All checks OK")
        jira.transition_issue(subtask_key, "Done")
        return True
```

**Prüfkriterien:**

| Kategorie | Check | Tool |
|-----------|-------|------|
| **Code Style** | .NET Code Style | `dotnet format --verify-no-changes` |
| **Code Style** | ESLint/Prettier | `npm run lint` |
| **Tests** | Unit Test Coverage | `dotnet test /p:CollectCoverage=true` |
| **Tests** | Integration Tests | `dotnet test --filter Category=Integration` |
| **Architecture** | Clean Architecture | Custom analyzer |
| **Security** | SQL Injection, XSS | `dotnet security-scan` |
| **Naming** | English-first (WEG-19) | Regex check |
| **Acceptance** | BDD Criteria met | Parse Given-When-Then |

**Output:**
- JIRA Comment mit Review-Ergebnissen
- Status-Transition (Done oder Changes Requested)
- Optional: Automatische Fix-Commits (dotnet format, eslint --fix)

---

### 4. **Integration Agent** (End-to-End Testing & Deployment)
**Aufgabe:** Testet fertige Stories im Gesamtsystem

**Workflow:**
```python
def integration_agent(story_key):
    # 1. Warte bis alle Sub-Tasks Done
    story = jira.issue(story_key)
    subtasks = story.fields.subtasks

    if not all(st.fields.status.name == "Done" for st in subtasks):
        return "Waiting for sub-tasks"

    # 2. Starte Docker-Umgebung
    docker_compose_up()

    # 3. Run Migrations
    run_ef_migrations()

    # 4. End-to-End Tests (aus Story Acceptance Criteria)
    results = []

    # Parse BDD Criteria
    criteria = parse_acceptance_criteria(story.fields.customfield_10091)
    # z.B.: "Gegeben Docker Desktop ist installiert..."

    for criterion in criteria:
        test_result = run_bdd_test(criterion)
        results.append(test_result)

    # 5. Playwright Tests
    playwright_results = run_playwright_tests(filter=story_key)

    # 6. API Contract Tests (OpenAPI Spec)
    api_tests = run_openapi_contract_tests()

    # 7. Performance Tests (wenn Story WEG-18 fertig)
    if epic_completed("WEG-18"):
        perf_results = run_performance_tests(story_key)

    # 8. Ergebnis in JIRA
    all_passed = all(results) and playwright_results.success and api_tests.success

    if all_passed:
        jira.add_comment(story_key, f"""
✅ **Integration Tests Passed**

- BDD Criteria: {len(criteria)}/{len(criteria)} ✅
- Playwright E2E: {playwright_results.passed}/{playwright_results.total} ✅
- API Contracts: {api_tests.passed}/{api_tests.total} ✅

Ready for deployment.
        """)
        jira.transition_issue(story_key, "Ready for Release")
    else:
        jira.transition_issue(story_key, "Integration Failed")
```

**Test-Typen:**

1. **BDD Acceptance Tests**
   ```gherkin
   Feature: Docker Compose Infrastructure (WEG-1003)

   Scenario: Start all services
     Given Docker Desktop is installed
     When I run "docker compose up"
     Then API should respond with 200 on /health
     And SQL Server should accept connections
     And Web should serve index.html
   ```

2. **Playwright E2E Tests**
   ```typescript
   test('WEG-1009: README Quick Start works', async ({ page }) => {
     // Follow README instructions programmatically
     await exec('git clone ...');
     await exec('cp .env.example .env');
     await exec('docker compose up -d');

     // Verify endpoints
     await page.goto('http://localhost:3000');
     await expect(page).toHaveTitle(/WEG Management/);
   });
   ```

3. **API Contract Tests**
   ```typescript
   test('OpenAPI spec matches implementation', async () => {
     const spec = await loadOpenApiSpec('/swagger/v1/swagger.json');
     const validator = new OpenApiValidator(spec);

     // Test all endpoints
     const response = await api.get('/api/associations');
     expect(validator.validate(response)).toBe(true);
   });
   ```

**Output:**
- JIRA Comment mit Testergebnissen
- Story-Status: Ready for Release oder Integration Failed
- Test-Reports als JIRA Attachments

---

## 🔄 Agent Orchestration Workflow

### Gesamtablauf: Von Epic bis Deployment

```
┌─────────────────────────────────────────────────────────────┐
│ 1. PLANNING PHASE                                           │
└─────────────────────────────────────────────────────────────┘
  Planning Agent:
  ├─ Liest Confluence (WEG-10 Dokumentation)
  ├─ Analysiert Abhängigkeiten (WEG-10 → WEG-1)
  ├─ Erstellt Sprint 1: [WEG-10, WEG-12, WEG-14]
  └─ Markiert WEG-1003 als "Next to Implement"

┌─────────────────────────────────────────────────────────────┐
│ 2. IMPLEMENTATION PHASE (Story WEG-1003)                    │
└─────────────────────────────────────────────────────────────┘
  Implementation Agent (Loop über alle Sub-Tasks):

  ┌─ WEG-1004: docker-compose.yml
  │  ├─ Liest Beschreibung
  │  ├─ Generiert docker-compose.yml
  │  ├─ Commitet: "WEG-1004: Create docker-compose.yml"
  │  ├─ Updated JIRA → "In Progress"
  │  └─ Trigger Review Agent
  │
  ├─ WEG-1005: Dockerfile API
  │  ├─ Liest Beschreibung
  │  ├─ Generiert multi-stage Dockerfile
  │  ├─ Commitet: "WEG-1005: Create Dockerfile for API"
  │  └─ Trigger Review Agent
  │
  ├─ WEG-1006: Dockerfile Web
  └─ WEG-1007: .env.example

┌─────────────────────────────────────────────────────────────┐
│ 3. REVIEW PHASE (nach jedem Sub-Task)                       │
└─────────────────────────────────────────────────────────────┘
  Review Agent:
  ├─ Run dotnet format --verify
  ├─ Check YAML syntax
  ├─ Verify health checks exist
  ├─ Security scan (keine hardcoded secrets)
  └─ Update JIRA: "✅ Review Passed" → Status: Done

┌─────────────────────────────────────────────────────────────┐
│ 4. INTEGRATION PHASE (wenn alle Sub-Tasks Done)             │
└─────────────────────────────────────────────────────────────┘
  Integration Agent:
  ├─ docker compose up -d
  ├─ Wait for health checks
  ├─ Test: curl http://localhost:5000/health → 200 OK
  ├─ Test: curl http://localhost:3000 → HTML
  ├─ Test: SQL connection from API
  └─ Update JIRA Story WEG-1003 → "Ready for Release"

┌─────────────────────────────────────────────────────────────┐
│ 5. DEPLOYMENT PHASE                                         │
└─────────────────────────────────────────────────────────────┘
  Deployment Agent:
  ├─ Merge to main branch
  ├─ Tag release: v0.1.0-weg-10
  ├─ Update JIRA Epic WEG-10 → "Deployed"
  └─ Trigger Planning Agent für nächste Story
```

---

## 📊 JIRA Status-Flow für Agenten

### Story Status-Übergänge

```
Backlog
  ↓ (Planning Agent wählt aus)
To Do
  ↓ (Implementation Agent startet ersten Sub-Task)
In Progress
  ↓ (Alle Sub-Tasks Done)
Ready for Testing
  ↓ (Integration Agent testet)
Ready for Release
  ↓ (Deployment Agent deployt)
Done
```

### Sub-Task Status-Übergänge

```
To Do
  ↓ (Implementation Agent startet)
In Progress
  ↓ (Code committed + Comment)
In Review
  ↓ (Review Agent prüft)
Done / Changes Requested
  ↓ (falls Changes Requested)
In Progress (Feedback einarbeiten)
```

---

## 🛠️ Agent-Tools und APIs

### JIRA API Operationen

```python
# 1. Issue Discovery
issues = jira.search_issues('project=WEG AND status="To Do" ORDER BY priority DESC')

# 2. Issue Transitions
jira.transition_issue('WEG-1004', 'In Progress')
jira.transition_issue('WEG-1004', 'Done')

# 3. Comments (für Logging)
jira.add_comment('WEG-1004', '''
✅ Implementation complete

**Files Created:**
- docker-compose.yml (87 lines)
- .env.example (45 lines)

**Verification:**
```bash
docker compose config  # ✅ Valid
docker compose up -d   # ✅ All services started
```
''')

# 4. Attachments (für Reports)
with open('test-report.html', 'rb') as f:
    jira.add_attachment('WEG-1003', f)

# 5. Custom Fields
acceptance_criteria = issue.fields.customfield_10091  # BDD Criteria
tech_notes = issue.fields.customfield_10092           # Implementation Plan

# 6. Epic Links
stories = jira.search_issues('"Epic Link" = WEG-10')
```

### Confluence API Operationen

```python
# 1. Page lesen (für Kontext)
page = confluence.get_page_by_id(27722234)  # WEG-30 Page
content = page['body']['storage']['value']

# 2. Architektur parsen
architecture = parse_confluence_architecture(content)
# Returns:
# {
#   'entities': ['Association', 'Building', 'Unit'],
#   'api_endpoints': ['/api/associations', ...],
#   'database_schema': 'tenant_schema'
# }

# 3. Dependency-Graph extrahieren
dependencies = extract_dependencies(content)
# Returns: ['WEG-31', 'WEG-32', 'WEG-12', 'WEG-24']
```

### Git Operations

```python
# 1. Feature Branch erstellen
git_checkout_branch(f'feature/WEG-1004-docker-compose')

# 2. Code schreiben
write_file('docker-compose.yml', content)
write_file('Dockerfile', content)

# 3. Commit mit JIRA-Key
git_add_all()
git_commit(f'WEG-1004: Create docker-compose.yml\n\nImplements WEG-1003 Docker Infrastructure story.')

# 4. Push
git_push('origin', branch)

# 5. Merge (nach Review)
git_merge_to_main()
```

---

## 🧠 Agent-Entscheidungslogik

### Wann sollte ein Agent welche Aktion ausführen?

#### Implementation Agent: Sub-Task Selection

```python
def select_next_subtask():
    # 1. Hole alle To Do Sub-Tasks im aktuellen Sprint
    subtasks = jira.search_issues('''
        project=WEG
        AND type=Sub-Task
        AND status="To Do"
        AND sprint in openSprints()
        ORDER BY priority DESC, key ASC
    ''')

    for task in subtasks:
        # 2. Check Abhängigkeiten (Parent Story muss Ready sein)
        parent = jira.issue(task.fields.parent.key)

        if parent.fields.status.name != "To Do":
            continue  # Parent noch nicht bereit

        # 3. Check Technical Dependencies (z.B. WEG-10 vor WEG-1)
        epic = get_epic_for_story(parent)
        if has_unmet_dependencies(epic):
            continue

        # 4. Wähle ersten validen Task
        return task

    return None  # Keine Tasks verfügbar
```

#### Review Agent: Wann automatisch fixen vs. eskalieren?

```python
def review_decision(issues):
    auto_fixable = []
    manual_review = []

    for issue in issues:
        if issue.type == "code_style":
            # Auto-fix: dotnet format, eslint --fix
            auto_fixable.append(issue)

        elif issue.type == "test_coverage" and issue.coverage >= 70:
            # Tolerierbar für MVP
            auto_fixable.append(issue)

        elif issue.type == "security":
            # Kritisch: Eskalation an Human
            manual_review.append(issue)
            escalate_to_human(issue)

        else:
            manual_review.append(issue)

    # Auto-fixes anwenden
    for fix in auto_fixable:
        apply_fix(fix)

    # Wenn nur auto-fixable: Agent macht weiter
    if not manual_review:
        return "APPROVED"
    else:
        return "CHANGES_REQUESTED"
```

#### Integration Agent: Wann ist eine Story wirklich "Done"?

```python
def verify_story_done(story):
    checks = {
        "all_subtasks_done": all(st.status == "Done" for st in story.subtasks),
        "acceptance_criteria_met": verify_bdd_criteria(story),
        "tests_passing": run_all_tests(),
        "no_merge_conflicts": check_git_status(),
        "documentation_updated": check_readme_updated(story),
        "api_spec_updated": check_openapi_spec(story) if has_api_changes(story) else True
    }

    if all(checks.values()):
        jira.transition_issue(story.key, "Done")
        jira.add_comment(story.key, f"✅ Story verified complete:\n{format_checks(checks)}")
        return True
    else:
        failed = [k for k, v in checks.items() if not v]
        jira.add_comment(story.key, f"❌ Story not complete:\n{failed}")
        return False
```

---

## 📋 Agent-Kommunikation via JIRA Comments

### Comment-Format für Agent-Handoffs

Agenten kommunizieren über strukturierte JIRA-Comments:

#### Implementation Agent → Review Agent
```markdown
🤖 **Implementation Agent** (WEG-1004)

**Status:** Implementation Complete
**Commit:** abc1234
**Files Changed:**
- docker-compose.yml (new, 87 lines)
- .env.example (new, 45 lines)

**Tests:**
- ✅ docker compose config passes
- ✅ All services start successfully
- ✅ Health checks pass

**Ready for Review**
@ReviewAgent please review
```

#### Review Agent → Implementation Agent (Changes Requested)
```markdown
🔍 **Review Agent** (WEG-1004)

**Status:** Changes Requested

**Issues Found:**
1. ❌ SQL_SA_PASSWORD too weak (min 12 chars required)
2. ⚠️  Missing healthcheck for web service
3. ✅ Code style: OK
4. ✅ Security scan: OK

**Action Required:**
@ImplementationAgent please fix issues 1-2
```

#### Integration Agent → Planning Agent (Story Complete)
```markdown
✅ **Integration Agent** (WEG-1003)

**Status:** Story Complete - Ready for Release

**Test Results:**
- BDD Acceptance Criteria: 5/5 ✅
- Playwright E2E: 12/12 ✅
- API Contract Tests: 8/8 ✅
- Performance: Response time < 200ms ✅

**Deployment Ready**
@PlanningAgent Story WEG-1003 complete, ready for next story
```

---

## 🎯 Priorisierung: Welche Module zuerst?

### Critical Path Analysis

```
Phase 1: Foundation (Sprint 1-2)
├─ WEG-10 Solution Setup ⭐ KRITISCH (alle hängen davon ab)
├─ WEG-12 Error Handling  ⭐ KRITISCH (für alle Module nötig)
├─ WEG-14 Testing & CI    ⭐ KRITISCH (Quality Gate)
└─ WEG-1  Platform Found. (Domain-Basis)

Phase 2: Core Infrastructure (Sprint 3-4)
├─ WEG-13 Control Plane   (Multi-Tenant Routing)
├─ WEG-3  Tenant Provision (Schema Creation)
└─ WEG-2  Identity & Auth (Zugriffskontrolle)

Phase 3: Business Features (Sprint 5-8)
├─ WEG-4  Property & People
├─ WEG-5  Document Management
└─ WEG-6  Messaging

Phase 4: Advanced Features (Sprint 9+)
├─ WEG-7  Metering
├─ WEG-8  Finance
└─ WEG-9  Meetings
```

### Dependency Graph

```python
def build_dependency_graph():
    dependencies = {
        "WEG-1": ["WEG-10"],                    # Platform needs Setup
        "WEG-2": ["WEG-1", "WEG-13"],           # Auth needs Platform + Routing
        "WEG-3": ["WEG-13", "WEG-1"],           # Tenant needs Routing + Platform
        "WEG-4": ["WEG-2", "WEG-3"],            # Property needs Auth + Tenant
        "WEG-5": ["WEG-2", "WEG-4"],            # DMS needs Auth + Property
        "WEG-6": ["WEG-2"],                     # Messaging needs Auth
        "WEG-7": ["WEG-4"],                     # Metering needs Property
        "WEG-8": ["WEG-4", "WEG-7"],            # Finance needs Property + Metering
        "WEG-9": ["WEG-2", "WEG-4", "WEG-6"],   # Meetings needs Auth + Property + Messaging
        "WEG-12": [],                           # Logging standalone
        "WEG-13": ["WEG-10", "WEG-1"],          # Routing needs Setup + Platform
        "WEG-14": ["WEG-10"],                   # Testing needs Setup
    }
    return dependencies

# Planning Agent verwendet dies für Sprint-Planung
```

---

## 🚀 Deployment Strategy

### Continuous Deployment via Agent

```python
def deployment_agent():
    # 1. Check: Ist ein Epic vollständig fertig?
    epics = jira.search_issues('project=WEG AND type=Epic AND status="Ready for Release"')

    for epic in epics:
        # 2. Sammle alle Stories
        stories = jira.search_issues(f'"Epic Link" = {epic.key}')

        # 3. Verify: Alle Stories Done?
        if not all(s.fields.status.name == "Done" for s in stories):
            continue

        # 4. Create Release
        version = create_version_from_epic(epic)  # z.B. "v0.1.0-weg-10"

        # 5. Tag in Git
        git_tag(version, f"Release {epic.fields.summary}")

        # 6. Deploy to Staging
        deploy_to_staging(version)

        # 7. Run Smoke Tests
        smoke_results = run_smoke_tests(staging_url)

        # 8. Update JIRA
        if smoke_results.success:
            jira.transition_issue(epic.key, "Deployed")
            jira.add_comment(epic.key, f"""
🚀 **Deployment Successful**

**Version:** {version}
**Environment:** Staging
**Smoke Tests:** {smoke_results.passed}/{smoke_results.total} ✅

**Deployed Stories:**
{list_stories(stories)}
            """)
        else:
            jira.transition_issue(epic.key, "Deployment Failed")
```

---

## 📚 Referenzen für Agenten

### Must-Read für jeden Agent-Typ

| Agent | Dokumente | Zweck |
|-------|-----------|-------|
| **Planning** | - Confluence: alle WEG-X Module<br>- JIRA: Epic-Liste<br>- Dependency-Graph | Priorisierung |
| **Implementation** | - JIRA_Templates_for_KI_Agents.md<br>- Sub-Task Descriptions<br>- Parent Story + Epic | Code-Generierung |
| **Review** | - WEG-19 (Naming Conventions)<br>- .editorconfig<br>- eslint.config.js | Standards |
| **Integration** | - Story Acceptance Criteria<br>- docker-compose.yml<br>- OpenAPI Spec | Testing |

### Template-Nutzung

```python
def generate_code_from_template(subtask):
    # 1. Identifiziere Task-Typ
    if "Entity" in subtask.summary:
        template = load_template("Epic-Domain-Entity-Template")
    elif "React Component" in subtask.summary:
        template = load_template("Frontend-Component-Template")
    elif "CQRS Command" in subtask.summary:
        template = load_template("CQRS-Command-Template")

    # 2. Extrahiere Platzhalter aus Task-Description
    placeholders = extract_placeholders(subtask.fields.description)
    # z.B.: {Resource} = "Association", {Action} = "Create"

    # 3. Template füllen
    code = template.render(placeholders)

    # 4. Validieren
    if not validates(code):
        raise ValueError("Generated code invalid")

    return code
```

---

## ⚡ Performance-Optimierungen

### Parallel Agent Execution

```python
import asyncio

async def process_sprint_parallel(sprint_stories):
    # Gruppiere Stories nach Abhängigkeiten
    independent_stories = filter_independent(sprint_stories)

    # Starte Implementation Agents parallel
    agents = [
        implementation_agent(story)
        for story in independent_stories
    ]

    # Warte auf alle
    results = await asyncio.gather(*agents)

    # Review Agents parallel
    review_tasks = [
        review_agent(result.commit_sha)
        for result in results
    ]
    await asyncio.gather(*review_tasks)
```

### Caching von Confluence-Daten

```python
class ConfluenceCache:
    def __init__(self):
        self.cache = {}

    def get_page(self, page_id):
        if page_id not in self.cache:
            self.cache[page_id] = confluence_api.get_page(page_id)
        return self.cache[page_id]

# Agents nutzen Cache statt direkter API-Calls
cache = ConfluenceCache()
```

---

## 🎓 Agent-Training und Verbesserung

### Feedback-Loop

```python
def collect_agent_metrics():
    metrics = {
        "implementation_time": [],
        "review_pass_rate": [],
        "test_pass_rate": [],
        "human_interventions": []
    }

    # Analysiere abgeschlossene Stories
    stories = jira.search_issues('project=WEG AND status=Done')

    for story in stories:
        # Zeitaufwand
        time_spent = calculate_cycle_time(story)
        metrics["implementation_time"].append(time_spent)

        # Review Erfolgsrate
        review_comments = get_comments_by_agent(story, "ReviewAgent")
        passed_first_time = "✅ Review Passed" in review_comments[0]
        metrics["review_pass_rate"].append(passed_first_time)

    # Report generieren
    generate_improvement_report(metrics)
```

### Self-Improvement

Agenten sollten aus Fehlern lernen:

```python
def learn_from_failures(failed_tasks):
    patterns = {}

    for task in failed_tasks:
        # 1. Analysiere Fehlerursache
        root_cause = analyze_failure(task)

        # 2. Kategorisiere
        if root_cause not in patterns:
            patterns[root_cause] = []
        patterns[root_cause].append(task)

    # 3. Update Agent-Prompts
    for cause, tasks in patterns.items():
        if len(tasks) > 3:  # Wiederholtes Problem
            update_agent_instructions(cause, tasks)
            # z.B.: "Immer health checks in docker-compose.yml"
```

---

## ✅ Success Metrics

### KPIs für Agent-Performance

| Metric | Ziel | Messung |
|--------|------|---------|
| **Story Cycle Time** | < 2 Stunden | Zeit von "To Do" → "Done" |
| **First-Time Review Pass Rate** | > 80% | Commits die Review ohne Changes bestehen |
| **Test Pass Rate** | 100% | Integration Tests erfolgreich |
| **Human Interventions** | < 10% | Tasks die manuelles Eingreifen brauchen |
| **Code Coverage** | > 80% | % des Codes mit Tests |
| **Deployment Frequency** | 1x pro Epic | Wie oft deployed wird |

### Dashboard

```python
def generate_agent_dashboard():
    return {
        "stories_completed": count_stories_done(),
        "average_cycle_time": calculate_avg_cycle_time(),
        "current_sprint_progress": get_sprint_burndown(),
        "agents_active": count_active_agents(),
        "failed_reviews": count_review_failures(),
        "pending_human_review": count_manual_interventions()
    }
```

---

## 🔐 Security Considerations

### Secrets Management für Agenten

```python
# NIEMALS direkt in Code:
jira_token = "ATATT3xFfGF01..."  # ❌ FALSCH

# Immer aus Umgebungsvariablen:
jira_token = os.getenv("JIRA_API_TOKEN")  # ✅ RICHTIG

# Agent-Credentials rotieren
def rotate_agent_credentials():
    new_token = generate_new_jira_token()
    update_secret_in_vault("JIRA_API_TOKEN", new_token)
    restart_agents()
```

### Code Review Security Checks

```python
def security_review(code):
    issues = []

    # 1. SQL Injection
    if re.search(r'SELECT.*\+.*WHERE', code):
        issues.append("Potential SQL Injection - use parameterized queries")

    # 2. Hardcoded Secrets
    if re.search(r'(password|secret|token)\s*=\s*["\'][^"\']+["\']', code, re.I):
        issues.append("Hardcoded secret detected")

    # 3. XSS
    if 'dangerouslySetInnerHTML' in code:
        issues.append("Potential XSS - sanitize HTML")

    return issues
```

---

## 🎉 Zusammenfassung

### Was macht diese Strategie effektiv?

1. **Vollständige Autonomie** - Agenten treffen Entscheidungen ohne Human Input
2. **JIRA als Source of Truth** - Alle Status, Aufgaben, Kommunikation in JIRA
3. **Templates eliminieren Ambiguität** - Jeder Sub-Task hat vollständige Code-Beispiele
4. **Multi-Agent-Collaboration** - Planning, Implementation, Review, Integration arbeiten zusammen
5. **Continuous Feedback** - Review und Integration Agents prüfen automatisch
6. **Messbare Qualität** - Tests, Coverage, BDD Criteria definieren "Done"

### Nächste Schritte

1. **Agent-Runtime aufsetzen**
   ```bash
   # Start Agent-Orchestrator
   python agent_orchestrator.py --mode=continuous
   ```

2. **Monitoring aktivieren**
   ```bash
   # Agent Dashboard
   streamlit run agent_dashboard.py
   ```

3. **Ersten Sprint starten**
   ```python
   planning_agent.create_sprint("Sprint 1", modules=["WEG-10", "WEG-12", "WEG-14"])
   ```

4. **Agenten loslassen** 🚀
   ```python
   implementation_agent.start(subtask="WEG-1004")
   ```

---

**Status:** Ready for Agent Deployment
**Empfehlung:** Start mit WEG-10 Sub-Tasks als Proof-of-Concept
