#!/usr/bin/env python3
"""
JIRA Automation Example für KI-Agenten
========================================

Dieses Script zeigt, wie KI-Agenten automatisch JIRA-Tickets
für das WEG Management System erstellen können.

Verwendung:
    1. Setze Umgebungsvariablen (siehe .env.jira.example)
    2. Installiere Dependencies: pip install jira python-dotenv
    3. Führe aus: python jira_automation_example.py

Autor: System Automation
Datum: 8. November 2025
"""

import os
import sys
from typing import Optional, List
from dotenv import load_dotenv

# Umgebungsvariablen laden
load_dotenv()

try:
    from jira import JIRA
    from jira.exceptions import JIRAError
except ImportError:
    print("❌ Error: 'jira' library not installed")
    print("   Install with: pip install jira python-dotenv")
    sys.exit(1)


class WegJiraAutomation:
    """Automation-Klasse für WEG JIRA-Management"""

    def __init__(self, dry_run: bool = False):
        """
        Initialisiert JIRA-Client

        Args:
            dry_run: Wenn True, werden keine echten Änderungen vorgenommen
        """
        self.dry_run = dry_run

        # Credentials laden
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.username = os.getenv("JIRA_USERNAME")
        self.api_token = os.getenv("JIRA_API_TOKEN")
        self.project_key = os.getenv("JIRA_PROJECT_KEY", "WEG")

        # Validierung
        self._validate_credentials()

        # JIRA Client initialisieren (außer im Dry-Run-Mode)
        if not self.dry_run:
            try:
                self.jira = JIRA(
                    server=self.base_url,
                    basic_auth=(self.username, self.api_token)
                )
                # Verbindung testen
                user = self.jira.myself()
                print(f"✅ Connected to JIRA as: {user['displayName']}")
                print(f"   Email: {user['emailAddress']}")
                print(f"   Project: {self.project_key}\n")
            except JIRAError as e:
                print(f"❌ JIRA Connection Failed: {e.text}")
                print(f"   Status Code: {e.status_code}")
                sys.exit(1)
        else:
            print("🔍 DRY RUN MODE - No changes will be made\n")

    def _validate_credentials(self):
        """Validiert, dass alle Credentials gesetzt sind"""
        required = {
            "JIRA_BASE_URL": self.base_url,
            "JIRA_USERNAME": self.username,
            "JIRA_API_TOKEN": self.api_token
        }

        missing = [name for name, value in required.items() if not value]

        if missing:
            print("❌ Missing environment variables:")
            for var in missing:
                print(f"   - {var}")
            print("\nPlease set these variables or create a .env file")
            print("See .env.jira.example for reference")
            sys.exit(1)

    def create_epic(
        self,
        summary: str,
        description: str,
        labels: Optional[List[str]] = None
    ):
        """
        Erstellt ein Epic

        Args:
            summary: Epic-Titel
            description: Detaillierte Beschreibung
            labels: Liste von Labels

        Returns:
            JIRA Issue object oder None (im Dry-Run)
        """
        if self.dry_run:
            print(f"[DRY RUN] Would create Epic:")
            print(f"  Summary: {summary}")
            print(f"  Labels: {labels}")
            return None

        issue_dict = {
            'project': {'key': self.project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Epic'},
            'labels': labels or []
        }

        try:
            epic = self.jira.create_issue(fields=issue_dict)
            print(f"✅ Epic created: {epic.key}")
            print(f"   {summary}")
            print(f"   URL: {self.base_url}/browse/{epic.key}\n")
            return epic
        except JIRAError as e:
            print(f"❌ Failed to create Epic: {e.text}")
            return None

    def create_story(
        self,
        summary: str,
        description: str,
        epic_key: str,
        labels: Optional[List[str]] = None
    ):
        """
        Erstellt eine Story unter einem Epic

        Args:
            summary: Story-Titel
            description: Detaillierte Beschreibung
            epic_key: Key des Parent-Epics
            labels: Liste von Labels

        Returns:
            JIRA Issue object oder None
        """
        if self.dry_run:
            print(f"[DRY RUN] Would create Story under {epic_key}:")
            print(f"  Summary: {summary}")
            return None

        issue_dict = {
            'project': {'key': self.project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Story'},
            'labels': labels or []
        }

        try:
            story = self.jira.create_issue(fields=issue_dict)

            # Story mit Epic verknüpfen
            self.jira.add_issues_to_epic(epic_key, [story.key])

            print(f"✅ Story created: {story.key} (linked to {epic_key})")
            print(f"   {summary}")
            print(f"   URL: {self.base_url}/browse/{story.key}\n")
            return story
        except JIRAError as e:
            print(f"❌ Failed to create Story: {e.text}")
            return None

    def create_task(
        self,
        summary: str,
        description: str,
        parent_key: str,
        priority: str = "Medium",
        assignee: Optional[str] = None
    ):
        """
        Erstellt einen Task unter einer Story

        Args:
            summary: Task-Titel
            description: Detaillierte Beschreibung
            parent_key: Key der Parent-Story
            priority: Priorität (Highest, High, Medium, Low, Lowest)
            assignee: Account-ID des Assignees

        Returns:
            JIRA Issue object oder None
        """
        if self.dry_run:
            print(f"[DRY RUN] Would create Task under {parent_key}:")
            print(f"  Summary: {summary}")
            print(f"  Priority: {priority}")
            return None

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

        try:
            task = self.jira.create_issue(fields=issue_dict)
            print(f"✅ Task created: {task.key} (child of {parent_key})")
            print(f"   {summary}")
            print(f"   Priority: {priority}")
            print(f"   URL: {self.base_url}/browse/{task.key}\n")
            return task
        except JIRAError as e:
            print(f"❌ Failed to create Task: {e.text}")
            return None

    def add_comment(self, issue_key: str, comment: str):
        """Fügt Kommentar zu einem Issue hinzu"""
        if self.dry_run:
            print(f"[DRY RUN] Would add comment to {issue_key}")
            return

        try:
            self.jira.add_comment(issue_key, comment)
            print(f"✅ Comment added to {issue_key}")
        except JIRAError as e:
            print(f"❌ Failed to add comment: {e.text}")

    def transition_issue(self, issue_key: str, transition_name: str):
        """Führt Status-Übergang durch"""
        if self.dry_run:
            print(f"[DRY RUN] Would transition {issue_key} to '{transition_name}'")
            return

        try:
            transitions = self.jira.transitions(issue_key)
            transition_id = None

            for t in transitions:
                if t['name'].lower() == transition_name.lower():
                    transition_id = t['id']
                    break

            if transition_id:
                self.jira.transition_issue(issue_key, transition_id)
                print(f"✅ {issue_key} → {transition_name}")
            else:
                available = [t['name'] for t in transitions]
                print(f"❌ Transition '{transition_name}' not available")
                print(f"   Available: {available}")
        except JIRAError as e:
            print(f"❌ Failed to transition issue: {e.text}")


def example_create_module_structure():
    """
    Beispiel: Erstellt vollständige Struktur für WEG-1 Modul

    Epic → Stories → Tasks
    """
    # Initialisiere Automation (dry_run=True für Test)
    automation = WegJiraAutomation(dry_run=False)

    print("=" * 70)
    print("Creating WEG-1 – Platform Foundation Module")
    print("=" * 70)
    print()

    # Epic erstellen
    epic = automation.create_epic(
        summary="WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite)",
        description="""
# Executive Summary
Das Modul WEG-1 – Platform Foundation bildet das technische Fundament
des gesamten WEG Management Systems (WMS).

## Architecture Overview
- **Backend:** .NET 8, ASP.NET Core, Entity Framework Core
- **Frontend:** React 18, TypeScript 5, Vite
- **Database:** SQL Server 2022 (Multi-Schema)
- **Infrastructure:** Docker Compose

## Scope
### In Scope
- Solution structure (Clean Architecture)
- Docker Compose environment
- Logging & Error Handling
- API versioning with OpenAPI
- Testing framework
- Internationalization (DE/EN)

## Links
- Confluence: https://maierharry.atlassian.net/wiki/spaces/WEG/pages/27165364
        """,
        labels=["infrastructure", "backend", "frontend", "foundation"]
    )

    if not epic:
        print("❌ Epic creation failed. Aborting.")
        return

    # Story 1: WEG-10 – Solution Setup
    story1 = automation.create_story(
        summary="WEG-10 – Solution Setup & Infrastructure",
        description="""
## User Story
**As a** Developer
**I want** a standardized project structure with Docker Compose
**So that** I can quickly start development without manual setup

## Technical Approach
- Clean Architecture layers (Api, Application, Domain, Infrastructure)
- Docker Compose with SQL Server, Directory DB, Web App
- Developer README with setup instructions

## Acceptance Criteria
- [ ] Solution structure created
- [ ] Docker Compose runs successfully
- [ ] README documentation complete
- [ ] CI pipeline configured
        """,
        epic_key=epic.key,
        labels=["infrastructure", "docker"]
    )

    if story1:
        # Tasks für Story 1
        automation.create_task(
            summary="Create Solution Structure (Clean Architecture)",
            description="""
## Files to Create
```
src/
├── WegManagement.Api/
├── WegManagement.Application/
├── WegManagement.Domain/
└── WegManagement.Infrastructure/
```

## Acceptance Criteria
- [ ] All projects created
- [ ] Dependencies configured
- [ ] Build successful
            """,
            parent_key=story1.key,
            priority="High"
        )

        automation.create_task(
            summary="Setup Docker Compose (SQL Server + Web)",
            description="""
## Services to Configure
- SQL Server 2022
- Directory Database
- API (ASP.NET Core)
- Web App (React)

## Acceptance Criteria
- [ ] docker-compose.yml created
- [ ] All services start successfully
- [ ] Health checks passing
            """,
            parent_key=story1.key,
            priority="High"
        )

    # Story 2: WEG-11 – API & OpenAPI
    story2 = automation.create_story(
        summary="WEG-11 – API, OpenAPI & TypeScript Client",
        description="""
## User Story
**As a** Frontend Developer
**I want** a typed API client generated from OpenAPI spec
**So that** I have type-safe API calls in TypeScript

## Technical Approach
- Configure Swashbuckle for OpenAPI generation
- API versioning (/api/v1)
- Generate TypeScript client with openapi-generator

## Acceptance Criteria
- [ ] OpenAPI spec available at /swagger.json
- [ ] TypeScript client generated
- [ ] API versioning working
        """,
        epic_key=epic.key,
        labels=["backend", "frontend", "api"]
    )

    if story2:
        automation.create_task(
            summary="Configure OpenAPI/Swagger in ASP.NET Core",
            description="""
## Implementation
- Install Swashbuckle.AspNetCore
- Configure in Program.cs
- Add XML documentation

## Files
- src/WegManagement.Api/Program.cs
            """,
            parent_key=story2.key,
            priority="High"
        )

    print("=" * 70)
    print("✅ Module structure created successfully!")
    print("=" * 70)


def example_update_progress():
    """
    Beispiel: Aktualisiert bestehende Issues mit Progress-Kommentaren
    """
    automation = WegJiraAutomation(dry_run=False)

    # Kommentar hinzufügen
    automation.add_comment(
        "WEG-10",
        """
*Progress Update*

Completed today:
- [x] Solution structure created
- [x] All projects building successfully
- [x] Docker Compose configured

Next:
- [ ] Write README documentation
- [ ] Setup CI pipeline

_Estimated completion: 2 days_
        """
    )

    # Status ändern
    automation.transition_issue("WEG-10", "In Progress")


def main():
    """Hauptfunktion - wähle Beispiel aus"""
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--create":
        # Erstelle vollständige Modul-Struktur
        example_create_module_structure()
    elif len(sys.argv) > 1 and sys.argv[1] == "--update":
        # Update bestehende Issues
        example_update_progress()
    else:
        print("Usage:")
        print("  python jira_automation_example.py --create   # Create WEG-1 structure")
        print("  python jira_automation_example.py --update   # Update existing issues")
        print("\nOr edit this file to customize the automation")


if __name__ == "__main__":
    main()
