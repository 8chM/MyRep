# KI-Agent Rollen und Workflows für Automatisierte Software-Entwicklung

**Projekt:** WEG Management System
**Plattform:** Claude Code Web KI-Agents
**Ziel:** Vollständig automatisierte Entwicklung durch rollenbasierte Agent-Orchestrierung

---

## 🎭 1. Rollen-Matrix: Software-Entwicklung → KI-Agents

### Traditionelle Rollen vs. KI-Agent Rollen

| Traditionelle Rolle | KI-Agent Äquivalent | Primäre Aufgaben | JIRA Zugriff |
|---------------------|---------------------|------------------|--------------|
| **Product Owner** | Planning Agent | Priorisierung, Roadmap, Backlog Grooming | Epics, Sprints |
| **Solution Architect** | Architecture Agent | System-Design, Tech-Stack, ADRs | Epics, Tech Notes |
| **Backend Developer** | Backend Implementation Agent | C# Code, EF Core, CQRS, APIs | Sub-Tasks (Backend) |
| **Frontend Developer** | Frontend Implementation Agent | React, TypeScript, Components | Sub-Tasks (Frontend) |
| **DevOps Engineer** | Infrastructure Agent | Docker, CI/CD, Deployments | Sub-Tasks (Infra) |
| **QA Engineer** | Quality Assurance Agent | Tests, Review, Integration Testing | All Tasks |
| **Tech Lead / Senior Dev** | Review Agent | Code Review, Standards, Mentoring | All Tasks |
| **Scrum Master** | Orchestration Agent | Workflow, Blockers, Velocity | Sprints, Boards |

---

## 👥 2. Detaillierte Rollen-Definition

### 2.1 Planning Agent (Product Owner)

**Verantwortung:** Strategische Planung und Priorisierung

**Input:**
- Confluence Dokumentation (Business Requirements)
- JIRA Epics (WEG-1 bis WEG-9)
- Dependency Graph
- Business Value Scores

**Aktivitäten:**
```python
class PlanningAgent:
    def __init__(self):
        self.jira = JIRA(...)
        self.confluence = Confluence(...)

    def create_roadmap(self):
        """Erstellt Product Roadmap aus Confluence"""
        # 1. Lese alle Confluence Module
        modules = self.confluence.get_all_pages(space="WEG")

        # 2. Extrahiere Business Value
        priorities = []
        for module in modules:
            value = self.calculate_business_value(module)
            dependencies = self.extract_dependencies(module)
            priorities.append({
                'epic': module.title,
                'value': value,
                'dependencies': dependencies
            })

        # 3. Topological Sort (Dependencies first)
        roadmap = self.topological_sort(priorities)

        # 4. Erstelle Sprints
        sprints = self.split_into_sprints(roadmap, velocity=40)

        return sprints

    def groom_backlog(self):
        """Bereitet nächsten Sprint vor"""
        # Epics in Stories breaken
        # Stories mit Acceptance Criteria anreichern
        # Estimations hinzufügen
        pass

    def prioritize_tasks(self):
        """Priorisiert Tasks basierend auf Blockers und Value"""
        # Blocked Tasks nach oben
        # High-Value Features priorisieren
        # Quick Wins identifizieren
        pass
```

**Output:**
- Sprint-Plan in JIRA
- Priorisierte Backlog
- Dependency-Warnings

**Trigger:**
- Täglich (Backlog Grooming)
- Start jedes Sprints
- On-Demand bei Blocker

---

### 2.2 Architecture Agent (Solution Architect)

**Verantwortung:** Technische Architektur-Entscheidungen

**Input:**
- Epic-Beschreibungen
- Confluence Architecture Pages
- ADR (Architecture Decision Records)
- Tech Stack Constraints (.NET 8, React 18, SQL Server)

**Aktivitäten:**
```python
class ArchitectureAgent:
    def design_epic_architecture(self, epic_key):
        """Erstellt technisches Design für Epic"""
        epic = self.jira.issue(epic_key)
        confluence_page = self.get_confluence_for_epic(epic)

        design = {
            'domain_model': self.design_domain_entities(confluence_page),
            'database_schema': self.design_db_schema(confluence_page),
            'api_contracts': self.design_api_endpoints(confluence_page),
            'frontend_structure': self.design_component_tree(confluence_page),
            'integration_points': self.identify_integrations(confluence_page)
        }

        # Erstelle ADR (Architecture Decision Record)
        adr = self.create_adr(epic, design)

        # Update JIRA Epic mit Tech Notes
        self.jira.add_comment(epic_key, self.format_architecture(design))

        return design

    def validate_architecture(self, code_changes):
        """Prüft ob Code dem Architecture Design folgt"""
        violations = []

        # Check: Domain sollte nicht auf Infrastructure referenzieren
        if self.domain_depends_on_infrastructure(code_changes):
            violations.append("Clean Architecture: Domain → Infrastructure dependency")

        # Check: API Endpoints folgen REST Conventions
        if not self.follows_rest_conventions(code_changes):
            violations.append("REST: Non-standard endpoint naming")

        return violations
```

**Output:**
- Architecture Decision Records (ADRs)
- Domain Models (C# Entities)
- API Contracts (OpenAPI Spec)
- Database Schema (EF Migrations)
- Component Trees (React Structure)

**Trigger:**
- Bei neuem Epic
- Bei Major Stories
- Bei Architecture Review Requests

---

### 2.3 Backend Implementation Agent

**Verantwortung:** C# Backend Code Implementation

**Input:**
- JIRA Sub-Task (Backend)
- Parent Story Acceptance Criteria
- Epic Architecture Design
- Code Templates (aus JIRA_Templates_for_KI_Agents.md)

**Aktivitäten:**
```python
class BackendImplementationAgent:
    def implement_subtask(self, subtask_key):
        """Implementiert Backend Sub-Task"""
        task = self.jira.issue(subtask_key)

        # 1. Context sammeln
        story = self.jira.issue(task.fields.parent.key)
        epic = self.get_epic_for_story(story)
        architecture = self.get_architecture_design(epic)

        # 2. Code generieren aus Template
        if "Entity" in task.fields.summary:
            code = self.generate_entity(task, architecture)
        elif "Command" in task.fields.summary:
            code = self.generate_cqrs_command(task, architecture)
        elif "Query" in task.fields.summary:
            code = self.generate_cqrs_query(task, architecture)
        elif "Controller" in task.fields.summary:
            code = self.generate_api_controller(task, architecture)

        # 3. Tests generieren
        tests = self.generate_unit_tests(code, task)

        # 4. Code schreiben
        self.write_files(code)
        self.write_files(tests)

        # 5. Build & Test lokal
        if not self.dotnet_build():
            self.fix_build_errors()

        if not self.dotnet_test():
            self.fix_test_failures()

        # 6. Commit
        self.git_commit(f"{subtask_key}: {task.fields.summary}")

        # 7. JIRA Update
        self.jira.transition_issue(subtask_key, "In Progress → Code Review")
        self.jira.add_comment(subtask_key, self.generate_implementation_summary(code))

        return code

    def generate_entity(self, task, architecture):
        """Generiert Domain Entity aus Template"""
        template = self.load_template("Domain-Entity")

        placeholders = {
            'EntityName': self.extract_entity_name(task),
            'Properties': architecture.get_entity_properties(task),
            'Relationships': architecture.get_relationships(task),
            'Validations': self.derive_validations(task)
        }

        code = template.render(placeholders)
        return code
```

**Output:**
- C# Source Files
- xUnit Test Files
- Git Commits mit JIRA-Keys
- JIRA Comments mit Implementation Details

**Spezialisierungen:**
- **Domain Layer Agent**: Entities, Value Objects, Domain Services
- **Application Layer Agent**: CQRS Commands/Queries, DTOs, Validators
- **Infrastructure Layer Agent**: EF DbContext, Repositories, External Services
- **API Layer Agent**: Controllers, Middleware, Filters

---

### 2.4 Frontend Implementation Agent

**Verantwortung:** React/TypeScript Frontend Code

**Input:**
- JIRA Sub-Task (Frontend)
- Figma/Design Specs (falls vorhanden)
- API Contracts (OpenAPI)
- Component Templates

**Aktivitäten:**
```python
class FrontendImplementationAgent:
    def implement_component(self, subtask_key):
        """Implementiert React Component"""
        task = self.jira.issue(subtask_key)

        # 1. API Client generieren aus OpenAPI
        api_spec = self.get_openapi_spec()
        api_client = self.generate_typed_api_client(api_spec)

        # 2. Component generieren
        if "List" in task.fields.summary:
            component = self.generate_list_component(task, api_client)
        elif "Form" in task.fields.summary:
            component = self.generate_form_component(task, api_client)
        elif "Detail" in task.fields.summary:
            component = self.generate_detail_component(task, api_client)

        # 3. Tests generieren (Vitest + React Testing Library)
        tests = self.generate_component_tests(component)

        # 4. E2E Tests generieren (Playwright)
        e2e_tests = self.generate_e2e_tests(component, task)

        # 5. Build & Test
        self.npm_run_build()
        self.npm_run_test()

        # 6. Commit & JIRA Update
        self.git_commit(f"{subtask_key}: {task.fields.summary}")
        self.jira.transition_issue(subtask_key, "Code Review")

        return component

    def generate_typed_api_client(self, openapi_spec):
        """Generiert TypeScript Client aus OpenAPI Spec"""
        # Nutzt openapi-typescript-codegen
        client_code = openapi_codegen.generate(
            spec=openapi_spec,
            output="web/src/api/generated"
        )
        return client_code
```

**Output:**
- React Components (.tsx)
- Custom Hooks
- Vitest Tests
- Playwright E2E Tests
- TypeScript API Clients

**Spezialisierungen:**
- **UI Component Agent**: Reusable Components, Storybook
- **Page Agent**: Full Pages, Routing
- **State Management Agent**: Zustand/Redux, TanStack Query
- **Styling Agent**: Tailwind, CSS Modules

---

### 2.5 Infrastructure Agent (DevOps)

**Verantwortung:** Infrastructure as Code, CI/CD, Deployments

**Input:**
- JIRA Sub-Task (Infrastructure)
- Environment Requirements
- Security Requirements

**Aktivitäten:**
```python
class InfrastructureAgent:
    def setup_infrastructure(self, subtask_key):
        """Implementiert Infrastructure Task"""
        task = self.jira.issue(subtask_key)

        if "Docker" in task.fields.summary:
            self.create_dockerfile(task)
            self.create_docker_compose(task)

        elif "CI/CD" in task.fields.summary:
            self.create_github_actions_workflow(task)

        elif "Azure" in task.fields.summary:
            self.create_bicep_templates(task)
            self.deploy_to_azure(task)

        # Test Infrastructure
        self.validate_docker_compose()
        self.validate_ci_pipeline()

        # Commit & Update
        self.git_commit(f"{subtask_key}: {task.fields.summary}")
        self.jira.transition_issue(subtask_key, "Done")

    def create_github_actions_workflow(self, task):
        """Erstellt CI/CD Pipeline"""
        workflow = {
            'name': 'WEG CI/CD',
            'on': ['push', 'pull_request'],
            'jobs': {
                'build': self.generate_build_job(),
                'test': self.generate_test_job(),
                'deploy': self.generate_deploy_job()
            }
        }

        self.write_yaml('.github/workflows/main.yml', workflow)
```

**Output:**
- Dockerfiles
- docker-compose.yml
- GitHub Actions Workflows
- Azure Bicep Templates
- Kubernetes Manifests

---

### 2.6 Quality Assurance Agent

**Verantwortung:** Testing, Quality Gates, Test Automation

**Input:**
- Completed Sub-Tasks
- Story Acceptance Criteria
- Test Coverage Requirements (80%)

**Aktivitäten:**
```python
class QualityAssuranceAgent:
    def verify_story_complete(self, story_key):
        """Prüft ob Story alle QA-Kriterien erfüllt"""
        story = self.jira.issue(story_key)

        results = {
            'unit_tests': self.check_unit_test_coverage(),
            'integration_tests': self.run_integration_tests(),
            'e2e_tests': self.run_e2e_tests(),
            'acceptance_criteria': self.verify_bdd_criteria(story),
            'performance': self.run_performance_tests(),
            'security': self.run_security_scan()
        }

        all_passed = all(results.values())

        if all_passed:
            self.jira.transition_issue(story_key, "QA Approved")
            self.jira.add_comment(story_key, self.format_qa_report(results))
        else:
            self.jira.transition_issue(story_key, "QA Failed")
            self.create_bug_tickets(story_key, results)

        return results

    def verify_bdd_criteria(self, story):
        """Verifiziert Given-When-Then Acceptance Criteria"""
        criteria = story.fields.customfield_10091  # Acceptance Criteria Field
        scenarios = self.parse_bdd_scenarios(criteria)

        results = []
        for scenario in scenarios:
            # Führe Gherkin Scenario aus
            result = self.execute_gherkin(scenario)
            results.append(result)

        return all(results)
```

**Output:**
- Test Reports (JUnit XML, HTML)
- Coverage Reports
- Performance Benchmarks
- Security Scan Results
- Bug Tickets (bei Failures)

---

### 2.7 Review Agent (Tech Lead)

**Verantwortung:** Code Review, Standards Enforcement, Best Practices

**Input:**
- Git Commits
- Pull Requests
- Code Diff

**Aktivitäten:**
```python
class ReviewAgent:
    def review_pull_request(self, commit_sha):
        """Reviewed Code Changes"""
        changes = self.git_diff(commit_sha)
        subtask_key = self.extract_jira_key_from_commit(commit_sha)

        issues = []

        # 1. Automated Checks
        issues += self.check_code_style(changes)
        issues += self.check_naming_conventions(changes)
        issues += self.check_architecture_compliance(changes)
        issues += self.check_security_vulnerabilities(changes)
        issues += self.check_test_coverage(changes)

        # 2. Semantic Review (AI-powered)
        issues += self.semantic_code_review(changes)

        # 3. Kategorisiere Issues
        critical = [i for i in issues if i.severity == "critical"]
        warnings = [i for i in issues if i.severity == "warning"]

        # 4. Decision
        if critical:
            self.request_changes(subtask_key, critical)
        elif len(warnings) > 5:
            self.request_changes(subtask_key, warnings)
        else:
            self.approve_changes(subtask_key, warnings)

        return issues

    def semantic_code_review(self, changes):
        """AI-powered semantic review"""
        issues = []

        # Nutze Claude API für semantische Analyse
        prompt = f"""
        Review this code for:
        - Logic errors
        - Edge cases not handled
        - Potential bugs
        - Code smells
        - Better alternatives

        Code:
        {changes}
        """

        review = claude_api.complete(prompt)
        issues += self.parse_review_comments(review)

        return issues
```

**Output:**
- Code Review Comments in JIRA
- Approved/Changes Requested Status
- Refactoring Suggestions
- Learning Resources (für Patterns)

---

### 2.8 Orchestration Agent (Scrum Master)

**Verantwortung:** Workflow Management, Blocker Resolution, Velocity Tracking

**Input:**
- JIRA Board Status
- Sprint Metrics
- Agent Health Status

**Aktivitäten:**
```python
class OrchestrationAgent:
    def manage_sprint(self):
        """Managed Sprint-Workflow"""
        # 1. Check Sprint Health
        velocity = self.calculate_velocity()
        blockers = self.identify_blockers()

        # 2. Resolve Blockers
        for blocker in blockers:
            if blocker.type == "dependency":
                self.prioritize_dependency_task(blocker)
            elif blocker.type == "technical":
                self.escalate_to_architecture_agent(blocker)

        # 3. Balance Workload
        self.distribute_tasks_across_agents()

        # 4. Daily Sync
        self.run_daily_standup()

    def run_daily_standup(self):
        """Simuliert Daily Standup"""
        report = {
            'completed_yesterday': self.get_completed_tasks(days=1),
            'planned_today': self.get_in_progress_tasks(),
            'blockers': self.identify_blockers(),
            'velocity': self.calculate_current_velocity(),
            'burndown': self.get_burndown_data()
        }

        # Post to JIRA Dashboard
        self.update_dashboard(report)

        # Notify if velocity < expected
        if report['velocity'] < self.expected_velocity:
            self.alert_low_velocity()
```

**Output:**
- Sprint Dashboards
- Velocity Charts
- Blocker Alerts
- Agent Performance Metrics

---

## 🔄 3. Agent-Workflow: End-to-End

### Sprint-Workflow (2-Wochen Zyklus)

```
┌─────────────────────────────────────────────────────────────┐
│ SPRINT PLANNING (Tag 0)                                     │
└─────────────────────────────────────────────────────────────┘
Planning Agent:
  ├─ Analysiert Confluence für Business Requirements
  ├─ Erstellt Sprint-Backlog aus Top-Priority Epics
  ├─ Berechnet Velocity (basierend auf letzten Sprints)
  └─ Weist Stories zu Sprint zu

Architecture Agent:
  ├─ Reviewed Sprint-Stories
  ├─ Erstellt Architecture Designs für neue Epics
  ├─ Identifiziert Technical Debt Tasks
  └─ Updated ADRs

Orchestration Agent:
  ├─ Erstellt Sprint Board
  ├─ Setzt Sprint Goals
  └─ Startet Sprint

┌─────────────────────────────────────────────────────────────┐
│ DAILY DEVELOPMENT (Tag 1-9)                                 │
└─────────────────────────────────────────────────────────────┘

MORGENS (09:00):
Orchestration Agent:
  └─ Daily Standup Report
     ├─ Completed: 8 Sub-Tasks
     ├─ In Progress: 12 Sub-Tasks
     ├─ Blocked: 2 Sub-Tasks
     └─ Velocity: On track

PARALLEL EXECUTION:
Backend Implementation Agent:
  ├─ WEG-1004: docker-compose.yml → Completed
  ├─ WEG-1011: DatabaseOptions.cs → In Progress
  └─ WEG-1xxx: Association Entity → Queued

Frontend Implementation Agent:
  ├─ WEG-2004: AssociationList Component → Completed
  ├─ WEG-2005: AssociationForm Component → In Progress
  └─ WEG-2xxx: API Client Generation → Queued

Infrastructure Agent:
  ├─ WEG-1005: Dockerfile API → Completed
  ├─ WEG-1015: GitHub Actions CI → In Progress
  └─ WEG-1xxx: Azure Bicep → Queued

NACH JEDEM COMMIT:
Review Agent:
  ├─ Automated Code Review
  ├─ Style Check (dotnet format, eslint)
  ├─ Security Scan
  ├─ Test Coverage Check
  └─ Approve / Request Changes

QA Agent (wenn Sub-Task → Code Review):
  ├─ Run Unit Tests
  ├─ Run Integration Tests
  ├─ Update Coverage Report
  └─ Transition to Done / QA Failed

ABENDS (18:00):
Orchestration Agent:
  └─ Daily Summary
     ├─ Burndown Chart Update
     ├─ Blocker Report
     └─ Tomorrow's Plan

┌─────────────────────────────────────────────────────────────┐
│ INTEGRATION TESTING (Tag 10-12)                             │
└─────────────────────────────────────────────────────────────┘

QA Agent:
  ├─ Wartet bis alle Sub-Tasks → Done
  ├─ Startet Integration Tests pro Story
  │  ├─ BDD Acceptance Criteria
  │  ├─ E2E Playwright Tests
  │  ├─ API Contract Tests
  │  └─ Performance Tests
  └─ Erstellt QA Report

Review Agent:
  ├─ Final Architecture Review
  ├─ Code Quality Metrics
  └─ Technical Debt Assessment

┌─────────────────────────────────────────────────────────────┐
│ DEPLOYMENT (Tag 13)                                         │
└─────────────────────────────────────────────────────────────┘

Infrastructure Agent:
  ├─ Merge to main branch
  ├─ Tag Release (v0.x.0)
  ├─ Deploy to Staging
  ├─ Run Smoke Tests
  └─ Deploy to Production (wenn approved)

QA Agent:
  ├─ Production Smoke Tests
  ├─ Monitoring Setup
  └─ Alerts Configuration

┌─────────────────────────────────────────────────────────────┐
│ RETROSPECTIVE (Tag 14)                                      │
└─────────────────────────────────────────────────────────────┘

Orchestration Agent:
  ├─ Sprint Metrics
  │  ├─ Velocity: 42 Story Points (Target: 40)
  │  ├─ Completed: 18/20 Tasks
  │  ├─ Bugs Found: 3
  │  └─ Code Coverage: 85%
  ├─ Agent Performance
  │  ├─ Backend Agent: 95% Success Rate
  │  ├─ Review Agent: 12% Change Requests
  │  └─ QA Agent: 3 Test Failures
  └─ Improvements
     ├─ Reduce Review Change Requests
     ├─ Improve Test Coverage (Target: 90%)
     └─ Add Performance Benchmarks

Planning Agent:
  └─ Plan next Sprint based on Retrospective
```

---

## 🏗️ 4. Claude Code Web: Konkrete Implementation

### 4.1 Session Management

Jeder Agent läuft als eigene **Claude Code Web Session**:

```python
# Orchestrator startet Agent-Sessions
class AgentOrchestrator:
    def __init__(self):
        self.sessions = {}

    def start_agent_session(self, agent_type, task):
        """Startet Claude Code Web Session für Agent"""
        session_config = {
            'agent_type': agent_type,
            'task': task,
            'context': self.build_context(task),
            'tools': self.get_tools_for_agent(agent_type)
        }

        # Starte Claude Code Web Session via API
        session = claude_code_web_api.create_session(
            prompt=self.generate_agent_prompt(session_config),
            tools=['bash', 'edit', 'write', 'read'],
            working_directory=f'/home/user/MyRep'
        )

        self.sessions[session.id] = {
            'agent': agent_type,
            'task': task,
            'status': 'running'
        }

        return session
```

### 4.2 Agent-Prompts (für Claude Code Web)

#### Backend Implementation Agent Prompt

```markdown
# Backend Implementation Agent

You are a specialized Backend Implementation Agent for the WEG Management System.

## Your Role
- Implement C# backend code for .NET 8 applications
- Follow Clean Architecture and CQRS patterns
- Write comprehensive unit tests with xUnit
- Ensure code passes all quality gates

## Current Task
{JIRA_SUBTASK_DESCRIPTION}

## Context
- **Story:** {PARENT_STORY_SUMMARY}
- **Epic:** {EPIC_KEY} - {EPIC_SUMMARY}
- **Architecture:** {ARCHITECTURE_DESIGN}
- **Acceptance Criteria:** {BDD_ACCEPTANCE_CRITERIA}

## Templates
Use templates from `/home/user/MyRep/JIRA_Templates_for_KI_Agents.md`

## Workflow
1. Read the Sub-Task description from JIRA
2. Extract code requirements and file paths
3. Generate code using appropriate template
4. Write files to correct locations
5. Generate unit tests
6. Run `dotnet build` - fix any errors
7. Run `dotnet test` - fix any failures
8. Commit with message: "{SUBTASK_KEY}: {SUMMARY}"
9. Update JIRA status to "Code Review"
10. Add implementation comment to JIRA

## Quality Standards
- Code coverage: minimum 80%
- All tests must pass
- Follow .editorconfig style
- No compiler warnings
- All async methods use CancellationToken

## JIRA Access
Use Python script at `/home/user/MyRep/jira_automation_example.py`
Credentials in `/home/user/MyRep/.env.jira.example`

Begin implementation now.
```

#### Frontend Implementation Agent Prompt

```markdown
# Frontend Implementation Agent

You are a specialized Frontend Implementation Agent for the WEG Management System.

## Your Role
- Implement React components with TypeScript
- Use TanStack Query for data fetching
- Write Vitest tests and Playwright E2E tests
- Follow React best practices

## Current Task
{JIRA_SUBTASK_DESCRIPTION}

## Context
- **Story:** {PARENT_STORY_SUMMARY}
- **API Endpoints:** {OPENAPI_SPEC_URL}
- **Design System:** Tailwind CSS, shadcn/ui
- **State Management:** TanStack Query, Zustand

## Templates
Use templates from `/home/user/MyRep/JIRA_Templates_for_KI_Agents.md`

## Workflow
1. Read Sub-Task from JIRA
2. Generate TypeScript API client from OpenAPI spec
3. Create React component
4. Write Vitest unit tests
5. Write Playwright E2E test
6. Run `npm run build` and `npm test`
7. Commit and update JIRA

## Quality Standards
- TypeScript strict mode
- 100% type coverage
- Test coverage > 80%
- Accessibility (ARIA labels)
- Responsive design

Begin implementation now.
```

### 4.3 Agent Communication via JIRA

Agents kommunizieren asynchron über JIRA Comments:

```python
# Backend Agent completed WEG-1011
backend_agent.jira.add_comment('WEG-1011', """
🤖 **Backend Implementation Agent**

✅ Implementation Complete

**Files Created:**
- `src/WegManagement.Infrastructure/Configuration/DatabaseOptions.cs`
- `src/WegManagement.Infrastructure/Configuration/JwtOptions.cs`
- `tests/Infrastructure.Tests/Configuration/DatabaseOptionsTests.cs`

**Tests:** 12/12 passed
**Coverage:** 95%
**Build:** ✅ Success

**Commit:** abc123def

Ready for @ReviewAgent
""")

# Review Agent picks up
review_agent.monitor_jira_comments()
# Findet Mention @ReviewAgent → triggered

# Review Agent reviewed
review_agent.jira.add_comment('WEG-1011', """
🔍 **Review Agent**

✅ Approved with minor suggestions

**Checks:**
- Code Style: ✅ Pass
- Architecture: ✅ Clean Architecture compliant
- Security: ✅ No issues
- Tests: ✅ Coverage 95%

**Suggestions:**
- Consider adding validation for empty ConnectionString

Approved to merge.
""")
```

---

## 🎛️ 5. Orchestration: Agent Coordinator

### Master Orchestrator Script

```python
#!/usr/bin/env python3
"""
WEG Management System - Agent Orchestrator
Koordiniert alle KI-Agents für autonome Entwicklung
"""

import asyncio
from typing import List, Dict
from jira import JIRA
import os

class WegAgentOrchestrator:
    """Zentraler Orchestrator für alle Agents"""

    def __init__(self):
        self.jira = self.init_jira()
        self.agents = {}
        self.active_sessions = []

    def init_jira(self):
        """Initialisiert JIRA Connection"""
        return JIRA(
            server=os.getenv("JIRA_BASE_URL"),
            basic_auth=(os.getenv("JIRA_USERNAME"), os.getenv("JIRA_API_TOKEN"))
        )

    async def run_sprint(self, sprint_id: str):
        """Führt kompletten Sprint aus"""
        print(f"🚀 Starting Sprint {sprint_id}")

        # 1. Planning
        await self.run_planning_phase(sprint_id)

        # 2. Daily Development (parallel)
        while not self.sprint_complete(sprint_id):
            await self.run_daily_cycle(sprint_id)
            await asyncio.sleep(3600)  # Check every hour

        # 3. Integration Testing
        await self.run_integration_phase(sprint_id)

        # 4. Deployment
        await self.run_deployment_phase(sprint_id)

        # 5. Retrospective
        await self.run_retrospective(sprint_id)

        print(f"✅ Sprint {sprint_id} Complete!")

    async def run_daily_cycle(self, sprint_id: str):
        """Täglicher Entwicklungszyklus"""

        # 1. Get tasks ready for implementation
        ready_tasks = self.jira.search_issues(f'''
            sprint = {sprint_id}
            AND status = "To Do"
            AND "Story Status" = "Ready for Development"
        ''')

        # 2. Start agents for each task (parallel)
        tasks_by_type = self.categorize_tasks(ready_tasks)

        agent_tasks = []

        for backend_task in tasks_by_type['backend']:
            agent_tasks.append(
                self.start_backend_agent(backend_task)
            )

        for frontend_task in tasks_by_type['frontend']:
            agent_tasks.append(
                self.start_frontend_agent(frontend_task)
            )

        for infra_task in tasks_by_type['infrastructure']:
            agent_tasks.append(
                self.start_infrastructure_agent(infra_task)
            )

        # 3. Wait for all agents to complete
        results = await asyncio.gather(*agent_tasks)

        # 4. Review completed tasks
        for result in results:
            if result.status == "completed":
                await self.start_review_agent(result.commit_sha)

        # 5. Update dashboard
        self.update_dashboard(sprint_id)

    async def start_backend_agent(self, task):
        """Startet Backend Implementation Agent"""
        print(f"🔧 Starting Backend Agent for {task.key}")

        # Erstelle Agent-Prompt
        prompt = self.generate_backend_prompt(task)

        # Starte Claude Code Web Session
        session = await claude_code_web.create_session(
            prompt=prompt,
            working_dir="/home/user/MyRep",
            tools=['bash', 'read', 'write', 'edit', 'grep', 'glob']
        )

        # Warte auf Completion
        result = await session.wait_for_completion()

        return result

    def generate_backend_prompt(self, task) -> str:
        """Generiert Prompt für Backend Agent"""
        story = self.jira.issue(task.fields.parent.key)
        epic = self.get_epic_for_story(story)

        return f"""
# Backend Implementation Agent - Task {task.key}

## Task Description
{task.fields.description}

## Parent Story
**{story.key}:** {story.fields.summary}

**Acceptance Criteria:**
{story.fields.customfield_10091}

## Epic Context
**{epic.key}:** {epic.fields.summary}

## Templates
Load templates from: `/home/user/MyRep/JIRA_Templates_for_KI_Agents.md`

## Instructions
1. Read the task description carefully
2. Extract code requirements and file paths
3. Generate code using templates
4. Write files to specified locations
5. Generate comprehensive unit tests (xUnit)
6. Run `dotnet build` - fix any compilation errors
7. Run `dotnet test` - ensure 80%+ coverage
8. Commit: "{task.key}: {task.fields.summary}"
9. Update JIRA:
   - Transition to "Code Review"
   - Add comment with implementation summary
   - Include files created, tests passed, coverage

## JIRA Access
```python
from jira_automation_example import WegJiraAutomation
jira = WegJiraAutomation()
jira.transition_issue('{task.key}', 'In Progress')
```

## Quality Gates
- ✅ Dotnet build succeeds
- ✅ All tests pass
- ✅ Coverage ≥ 80%
- ✅ No compiler warnings
- ✅ Follows Clean Architecture

**Begin implementation now.**
"""

# Usage
if __name__ == "__main__":
    orchestrator = WegAgentOrchestrator()
    asyncio.run(orchestrator.run_sprint("Sprint-1"))
```

---

## 📊 6. Monitoring & Dashboards

### Real-time Agent Dashboard

```python
import streamlit as st
import pandas as pd
from jira import JIRA

st.title("🤖 WEG Agent Orchestration Dashboard")

# Agent Status
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Active Agents", "6", "+2")

with col2:
    st.metric("Tasks Completed Today", "14", "+14")

with col3:
    st.metric("Sprint Progress", "65%", "+15%")

with col4:
    st.metric("Code Coverage", "87%", "+2%")

# Agent Activity
st.subheader("Agent Activity (Last 24h)")

agent_activity = pd.DataFrame({
    'Agent': ['Backend', 'Frontend', 'Infrastructure', 'Review', 'QA'],
    'Tasks Completed': [8, 5, 2, 12, 8],
    'Success Rate': [95, 90, 100, 85, 92],
    'Avg Time (min)': [45, 38, 62, 15, 28]
})

st.dataframe(agent_activity)

# Sprint Burndown
st.subheader("Sprint Burndown")
# Chart showing ideal vs actual progress

# Recent Commits
st.subheader("Recent Commits")
# List of commits with JIRA keys

# Blockers
st.subheader("⚠️ Blockers")
blockers = get_blocked_tasks()
if blockers:
    for blocker in blockers:
        st.error(f"{blocker.key}: {blocker.summary} - Blocked by {blocker.blocker}")
```

---

## 🚨 7. Error Handling & Recovery

### Agent Failure Recovery

```python
class AgentFailureHandler:
    def handle_agent_failure(self, agent_type, task, error):
        """Behandelt Agent-Fehler"""

        # 1. Log Error
        self.log_error(agent_type, task, error)

        # 2. Analyze Error Type
        if error.type == "compilation_error":
            # Retry mit zusätzlichem Kontext
            return self.retry_with_fix_hints(agent_type, task, error)

        elif error.type == "test_failure":
            # QA Agent analysiert Test Failure
            return self.escalate_to_qa_agent(task, error)

        elif error.type == "timeout":
            # Task zu komplex - in kleinere Sub-Tasks breaken
            return self.break_into_smaller_tasks(task)

        elif error.type == "architecture_violation":
            # Architecture Agent reviewt Design
            return self.escalate_to_architecture_agent(task, error)

        else:
            # Human Intervention Required
            return self.escalate_to_human(task, error)

    def retry_with_fix_hints(self, agent_type, task, error):
        """Retry mit Fehlerbehebungs-Hinweisen"""
        fix_hints = self.generate_fix_hints(error)

        enhanced_prompt = f"""
        Previous attempt failed with error:
        {error.message}

        Fix hints:
        {fix_hints}

        Please retry the implementation addressing these issues.
        """

        return self.start_agent(agent_type, task, additional_context=enhanced_prompt)
```

---

## 📝 8. Zusammenfassung & Deployment

### Quick Start: Agent System aufsetzen

```bash
# 1. Repository klonen
git clone https://github.com/8chM/MyRep.git
cd MyRep

# 2. Dependencies installieren
pip install jira python-dotenv streamlit asyncio

# 3. JIRA Credentials konfigurieren
cp .env.jira.example .env.jira
# Edit .env.jira with credentials

# 4. Orchestrator starten
python agent_orchestrator.py --sprint Sprint-1

# 5. Dashboard starten (separates Terminal)
streamlit run agent_dashboard.py
```

### Deployment Checklist

- ✅ JIRA Project konfiguriert (WEG)
- ✅ Confluence Pages vorhanden (alle Module)
- ✅ Templates erstellt (JIRA_Templates_for_KI_Agents.md)
- ✅ Agent Prompts definiert
- ✅ Orchestrator implementiert
- ✅ Monitoring Dashboard deployed
- ✅ Error Handling konfiguriert
- ✅ CI/CD Pipeline aktiv
- ✅ Erste Sprint geplant

---

**Status:** Ready for Agent Deployment
**Nächster Schritt:** Implementierung des AgentOrchestrator Scripts
