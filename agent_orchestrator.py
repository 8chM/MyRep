#!/usr/bin/env python3
"""
WEG Management System - Agent Orchestrator
Koordiniert Claude Code Web KI-Agents für autonome Software-Entwicklung

Usage:
    python agent_orchestrator.py --sprint Sprint-1
    python agent_orchestrator.py --task WEG-1004
    python agent_orchestrator.py --continuous
"""

import os
import sys
import time
import argparse
from datetime import datetime
from typing import List, Dict, Optional
from jira import JIRA
from dotenv import load_dotenv

# Load environment
load_dotenv('.env.jira.example')


class AgentOrchestrator:
    """Zentraler Orchestrator für alle WEG KI-Agents"""

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.jira = self._init_jira()
        self.project_key = "WEG"
        self.active_sessions = {}

        print("✅ Agent Orchestrator initialized")
        print(f"📋 JIRA: {os.getenv('JIRA_BASE_URL')}")
        print(f"🎯 Project: {self.project_key}")
        print(f"🧪 Dry Run: {dry_run}")

    def _init_jira(self) -> JIRA:
        """Initialisiert JIRA Connection"""
        return JIRA(
            server=os.getenv("JIRA_BASE_URL"),
            basic_auth=(os.getenv("JIRA_USERNAME"), os.getenv("JIRA_API_TOKEN"))
        )

    # ========================================
    # TASK DISCOVERY & CATEGORIZATION
    # ========================================

    def get_ready_tasks(self, sprint_id: Optional[str] = None) -> List:
        """Findet Tasks die bereit für Implementation sind"""
        if sprint_id:
            jql = f'project={self.project_key} AND sprint={sprint_id} AND status="To Do" ORDER BY priority DESC'
        else:
            jql = f'project={self.project_key} AND status="To Do" ORDER BY priority DESC, key ASC'

        tasks = self.jira.search_issues(jql, maxResults=50)

        print(f"\n📊 Found {len(tasks)} tasks ready for implementation")
        return tasks

    def categorize_task(self, task) -> str:
        """Kategorisiert Task nach Typ (Backend, Frontend, Infrastructure)"""
        summary = task.fields.summary.lower()
        labels = [label.lower() for label in task.fields.labels]

        # Check labels first
        if 'backend' in labels or 'api' in labels:
            return 'backend'
        if 'frontend' in labels or 'react' in labels or 'ui' in labels:
            return 'frontend'
        if 'infrastructure' in labels or 'docker' in labels or 'devops' in labels:
            return 'infrastructure'

        # Check summary keywords
        backend_keywords = ['entity', 'command', 'query', 'repository', 'service', 'api', 'controller', 'cqrs', 'database']
        frontend_keywords = ['component', 'page', 'form', 'list', 'react', 'ui', 'view']
        infra_keywords = ['docker', 'compose', 'dockerfile', 'ci/cd', 'pipeline', 'deploy', 'infrastructure']

        if any(keyword in summary for keyword in backend_keywords):
            return 'backend'
        if any(keyword in summary for keyword in frontend_keywords):
            return 'frontend'
        if any(keyword in summary for keyword in infra_keywords):
            return 'infrastructure'

        # Default
        return 'backend'

    def get_task_context(self, task) -> Dict:
        """Sammelt vollständigen Kontext für Task"""
        context = {
            'task_key': task.key,
            'task_summary': task.fields.summary,
            'task_description': task.fields.description or "",
            'task_type': self.categorize_task(task),
            'labels': task.fields.labels,
            'priority': task.fields.priority.name if task.fields.priority else "Medium"
        }

        # Parent Story
        if hasattr(task.fields, 'parent') and task.fields.parent:
            parent = self.jira.issue(task.fields.parent.key)
            context['parent_key'] = parent.key
            context['parent_summary'] = parent.fields.summary
            context['parent_description'] = parent.fields.description or ""

            # Acceptance Criteria (Custom Field)
            if hasattr(parent.fields, 'customfield_10091'):
                context['acceptance_criteria'] = parent.fields.customfield_10091 or ""

            # Epic (via parent)
            if hasattr(parent.fields, 'customfield_10014'):  # Epic Link field
                epic_key = parent.fields.customfield_10014
                if epic_key:
                    epic = self.jira.issue(epic_key)
                    context['epic_key'] = epic.key
                    context['epic_summary'] = epic.fields.summary
                    context['epic_description'] = epic.fields.description or ""

        return context

    # ========================================
    # AGENT PROMPT GENERATION
    # ========================================

    def generate_backend_agent_prompt(self, context: Dict) -> str:
        """Generiert Prompt für Backend Implementation Agent"""
        return f"""# Backend Implementation Agent - WEG Management System

## 🎯 Your Role
You are a Backend Implementation Agent specialized in C# .NET 8 development.
Your task is to implement high-quality backend code following Clean Architecture and CQRS patterns.

## 📋 Current Task
**Task:** {context['task_key']} - {context['task_summary']}
**Priority:** {context['priority']}

### Task Description
{context['task_description']}

## 📖 Context

### Parent Story
**Story:** {context.get('parent_key', 'N/A')} - {context.get('parent_summary', 'N/A')}

{context.get('parent_description', '')}

### Acceptance Criteria
{context.get('acceptance_criteria', 'No specific acceptance criteria provided.')}

### Epic
**Epic:** {context.get('epic_key', 'N/A')} - {context.get('epic_summary', 'N/A')}

## 🛠️ Implementation Workflow

1. **Read Task Description**
   - Extract all code requirements
   - Identify file paths and namespaces
   - Understand business logic

2. **Load Templates**
   - Use templates from `/home/user/MyRep/JIRA_Templates_for_KI_Agents.md`
   - Match task type to appropriate template (Entity, Command, Query, Controller, etc.)

3. **Generate Code**
   - Follow Clean Architecture layers
   - Use CQRS pattern for Application layer
   - Implement domain validation in Entities
   - Follow naming conventions (English-first, from WEG-19)

4. **Write Files**
   - Create files in correct project structure:
     - Domain: `src/WegManagement.Domain/Entities/`
     - Application: `src/WegManagement.Application/Features/`
     - Infrastructure: `src/WegManagement.Infrastructure/`
     - API: `src/WegManagement.Api/Controllers/`

5. **Generate Tests**
   - Create comprehensive unit tests with xUnit
   - Test files in: `tests/[ProjectName].Tests/`
   - Aim for 80%+ code coverage
   - Test edge cases and validations

6. **Build & Test**
   ```bash
   dotnet build
   dotnet test
   ```
   - Fix any compilation errors
   - Fix any test failures
   - Ensure no warnings

7. **Commit**
   ```bash
   git add .
   git commit -m "{context['task_key']}: {context['task_summary']}"
   ```

8. **Update JIRA**
   ```python
   from jira_automation_example import WegJiraAutomation
   jira = WegJiraAutomation()

   # Transition to In Progress
   jira.transition_issue('{context['task_key']}', 'In Progress')

   # Add implementation comment
   jira.add_comment('{context['task_key']}', '''
   🤖 **Backend Implementation Agent**

   ✅ Implementation Complete

   **Files Created:**
   - [list files]

   **Tests:** [X/X passed]
   **Coverage:** [X%]
   **Build:** ✅ Success

   **Commit:** [commit hash]

   Ready for @ReviewAgent
   ''')

   # Transition to Code Review
   jira.transition_issue('{context['task_key']}', 'Code Review')
   ```

## 📏 Quality Standards

### Code Quality
- ✅ Follow .editorconfig style rules
- ✅ Use C# 12 features appropriately
- ✅ All async methods accept CancellationToken
- ✅ Proper error handling with Result pattern or exceptions
- ✅ XML documentation for public APIs

### Architecture
- ✅ Clean Architecture: Domain → Application → Infrastructure → API
- ✅ Domain entities have no dependencies
- ✅ Application layer uses MediatR for CQRS
- ✅ Infrastructure implements interfaces from Application
- ✅ API controllers are thin (just routing)

### Testing
- ✅ Unit tests for all business logic
- ✅ Test coverage ≥ 80%
- ✅ Test edge cases and validations
- ✅ Use FluentAssertions for readable assertions
- ✅ Mock external dependencies with Moq

### Security
- ✅ No SQL injection (use parameterized queries)
- ✅ Input validation on all DTOs
- ✅ No hardcoded secrets
- ✅ Proper authorization checks

## 🔗 Resources

- **Templates:** `/home/user/MyRep/JIRA_Templates_for_KI_Agents.md`
- **JIRA Automation:** `/home/user/MyRep/jira_automation_example.py`
- **Credentials:** `/home/user/MyRep/.env.jira.example`
- **Strategy:** `/home/user/MyRep/KI_AGENT_STRATEGY.md`

## 🚀 Begin Implementation

Start implementing the task now following the workflow above.
Be thorough, write clean code, and ensure all quality gates pass.
"""

    def generate_frontend_agent_prompt(self, context: Dict) -> str:
        """Generiert Prompt für Frontend Implementation Agent"""
        return f"""# Frontend Implementation Agent - WEG Management System

## 🎯 Your Role
You are a Frontend Implementation Agent specialized in React 18 with TypeScript.
Your task is to implement high-quality, accessible, and performant UI components.

## 📋 Current Task
**Task:** {context['task_key']} - {context['task_summary']}
**Priority:** {context['priority']}

### Task Description
{context['task_description']}

## 📖 Context

### Parent Story
**Story:** {context.get('parent_key', 'N/A')} - {context.get('parent_summary', 'N/A')}

{context.get('parent_description', '')}

### Acceptance Criteria
{context.get('acceptance_criteria', 'No specific acceptance criteria provided.')}

## 🛠️ Implementation Workflow

1. **Generate TypeScript API Client**
   - If API endpoints exist, generate typed client from OpenAPI spec
   - Location: `web/src/api/generated/`

2. **Create React Component**
   - Use functional components with hooks
   - TypeScript with strict mode
   - Location: `web/src/components/` or `web/src/pages/`

3. **Implement Data Fetching**
   - Use TanStack Query for server state
   - Use Zustand for client state
   - Proper loading and error states

4. **Styling**
   - Use Tailwind CSS utilities
   - shadcn/ui components where applicable
   - Responsive design (mobile-first)

5. **Accessibility**
   - ARIA labels for all interactive elements
   - Keyboard navigation
   - Screen reader compatible

6. **Tests**
   - Vitest unit tests: `web/src/components/__tests__/`
   - React Testing Library
   - Playwright E2E tests: `web/e2e/`

7. **Build & Test**
   ```bash
   cd web
   npm run build
   npm run test
   npm run test:e2e
   ```

8. **Commit & Update JIRA**

## 📏 Quality Standards

- ✅ TypeScript strict mode enabled
- ✅ No `any` types
- ✅ 100% type coverage
- ✅ Test coverage ≥ 80%
- ✅ Accessibility score 100%
- ✅ Performance: LCP < 2.5s

## 🚀 Begin Implementation

Start implementing the component now.
"""

    def generate_infrastructure_agent_prompt(self, context: Dict) -> str:
        """Generiert Prompt für Infrastructure Agent"""
        return f"""# Infrastructure Agent - WEG Management System

## 🎯 Your Role
You are an Infrastructure Agent specialized in Docker, CI/CD, and cloud deployments.
Your task is to implement reliable, scalable infrastructure as code.

## 📋 Current Task
**Task:** {context['task_key']} - {context['task_summary']}
**Priority:** {context['priority']}

### Task Description
{context['task_description']}

## 🛠️ Implementation Workflow

1. **Infrastructure as Code**
   - Docker: Dockerfiles, docker-compose.yml
   - CI/CD: GitHub Actions workflows
   - Cloud: Azure Bicep templates

2. **Security**
   - No secrets in code
   - Use environment variables
   - Proper file permissions

3. **Testing**
   - Validate YAML/JSON syntax
   - Test docker compose up
   - Validate CI pipeline

4. **Commit & Update JIRA**

## 🚀 Begin Implementation
"""

    # ========================================
    # AGENT EXECUTION
    # ========================================

    def execute_task_with_agent(self, task):
        """Führt Task mit passendem Agent aus"""
        context = self.get_task_context(task)
        task_type = context['task_type']

        print(f"\n{'='*60}")
        print(f"🤖 Starting {task_type.upper()} Agent")
        print(f"📋 Task: {context['task_key']} - {context['task_summary']}")
        print(f"{'='*60}\n")

        if self.dry_run:
            print(f"[DRY RUN] Would execute {task_type} agent for {task.key}")
            print(f"[DRY RUN] Prompt preview (first 500 chars):")

            if task_type == 'backend':
                prompt = self.generate_backend_agent_prompt(context)
            elif task_type == 'frontend':
                prompt = self.generate_frontend_agent_prompt(context)
            else:
                prompt = self.generate_infrastructure_agent_prompt(context)

            print(prompt[:500] + "...\n")
            return

        # Real execution
        if task_type == 'backend':
            self.execute_backend_agent(context)
        elif task_type == 'frontend':
            self.execute_frontend_agent(context)
        else:
            self.execute_infrastructure_agent(context)

    def execute_backend_agent(self, context: Dict):
        """Führt Backend Agent aus"""
        prompt = self.generate_backend_agent_prompt(context)

        print("💾 Saving agent prompt to file...")
        prompt_file = f"/tmp/agent_prompt_{context['task_key']}.md"
        with open(prompt_file, 'w') as f:
            f.write(prompt)

        print(f"✅ Prompt saved to: {prompt_file}")
        print("\n📝 Next Steps:")
        print(f"   1. Open Claude Code Web")
        print(f"   2. Paste the prompt from: {prompt_file}")
        print(f"   3. Agent will implement the task autonomously")
        print(f"   4. Agent will update JIRA when done")

    def execute_frontend_agent(self, context: Dict):
        """Führt Frontend Agent aus"""
        prompt = self.generate_frontend_agent_prompt(context)

        prompt_file = f"/tmp/agent_prompt_{context['task_key']}.md"
        with open(prompt_file, 'w') as f:
            f.write(prompt)

        print(f"✅ Frontend Agent prompt saved to: {prompt_file}")

    def execute_infrastructure_agent(self, context: Dict):
        """Führt Infrastructure Agent aus"""
        prompt = self.generate_infrastructure_agent_prompt(context)

        prompt_file = f"/tmp/agent_prompt_{context['task_key']}.md"
        with open(prompt_file, 'w') as f:
            f.write(prompt)

        print(f"✅ Infrastructure Agent prompt saved to: {prompt_file}")

    # ========================================
    # HIGH-LEVEL WORKFLOWS
    # ========================================

    def run_sprint(self, sprint_id: str):
        """Führt kompletten Sprint aus"""
        print(f"\n🚀 Starting Sprint: {sprint_id}")

        tasks = self.get_ready_tasks(sprint_id)

        if not tasks:
            print("❌ No tasks found for this sprint")
            return

        print(f"\n📊 Sprint Summary:")
        print(f"   Total Tasks: {len(tasks)}")

        # Kategorisiere Tasks
        by_type = {'backend': 0, 'frontend': 0, 'infrastructure': 0}
        for task in tasks:
            task_type = self.categorize_task(task)
            by_type[task_type] += 1

        print(f"   Backend: {by_type['backend']}")
        print(f"   Frontend: {by_type['frontend']}")
        print(f"   Infrastructure: {by_type['infrastructure']}")

        # Execute tasks
        for i, task in enumerate(tasks, 1):
            print(f"\n{'='*60}")
            print(f"Task {i}/{len(tasks)}")
            self.execute_task_with_agent(task)

            if not self.dry_run:
                time.sleep(2)  # Small delay between tasks

        print(f"\n✅ Sprint {sprint_id} processing complete!")

    def run_single_task(self, task_key: str):
        """Führt einzelnen Task aus"""
        print(f"\n🎯 Processing single task: {task_key}")

        try:
            task = self.jira.issue(task_key)
            self.execute_task_with_agent(task)
        except Exception as e:
            print(f"❌ Error processing task {task_key}: {e}")

    def run_continuous(self):
        """Läuft kontinuierlich und überwacht JIRA für neue Tasks"""
        print("\n🔄 Starting continuous mode...")
        print("   Monitoring JIRA for new tasks every 5 minutes")
        print("   Press Ctrl+C to stop\n")

        try:
            while True:
                tasks = self.get_ready_tasks()

                if tasks:
                    print(f"\n📋 Found {len(tasks)} ready tasks")
                    for task in tasks[:5]:  # Process max 5 at a time
                        self.execute_task_with_agent(task)
                else:
                    print("✅ No tasks ready - waiting...")

                # Wait 5 minutes
                time.sleep(300)

        except KeyboardInterrupt:
            print("\n\n⏹️  Continuous mode stopped")


# ========================================
# CLI
# ========================================

def main():
    parser = argparse.ArgumentParser(
        description='WEG Agent Orchestrator - Autonomous Software Development'
    )

    parser.add_argument(
        '--sprint',
        type=str,
        help='Process all tasks in a sprint (e.g., Sprint-1)'
    )

    parser.add_argument(
        '--task',
        type=str,
        help='Process single task by key (e.g., WEG-1004)'
    )

    parser.add_argument(
        '--continuous',
        action='store_true',
        help='Run in continuous mode (monitor JIRA every 5 min)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Dry run mode (no actual execution)'
    )

    args = parser.parse_args()

    # Initialize orchestrator
    orchestrator = AgentOrchestrator(dry_run=args.dry_run)

    # Execute based on mode
    if args.sprint:
        orchestrator.run_sprint(args.sprint)
    elif args.task:
        orchestrator.run_single_task(args.task)
    elif args.continuous:
        orchestrator.run_continuous()
    else:
        print("❌ Please specify --sprint, --task, or --continuous")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
