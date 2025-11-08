#!/usr/bin/env python3
"""
JIRA Writer Agent - Hierarchische JIRA-Erstellung für WEG Management System

Erstellt automatisiert:
- Level 1: Grundmodule (WEG-1 bis WEG-9) als Epics
- Level 2: Untermodule (WEG-10 bis WEG-99) als Stories
- Level 3: Tasks (WEG-100+) als Sub-Tasks

Jede Ebene reichert den Kontext für nachfolgende Ebenen an.

Usage:
    python jira_writer_agent.py --level epic --module WEG-1
    python jira_writer_agent.py --level story --epic WEG-1
    python jira_writer_agent.py --level task --story WEG-10
    python jira_writer_agent.py --full-hierarchy WEG-1
"""

import os
import sys
import argparse
from jira import JIRA
from dotenv import load_dotenv

load_dotenv('.env.jira.example')


class JiraWriterAgent:
    """Hierarchischer JIRA Writer Agent"""

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.jira = self._init_jira()
        self.project_key = "WEG"
        self.confluence_export_dir = "confluence_export"

        print("✅ JIRA Writer Agent initialized")
        print(f"📋 JIRA: {os.getenv('JIRA_BASE_URL')}")
        print(f"🎯 Project: {self.project_key}")
        print(f"🧪 Dry Run: {dry_run}\n")

    def _init_jira(self) -> JIRA:
        """Initialisiert JIRA Connection"""
        return JIRA(
            server=os.getenv("JIRA_BASE_URL"),
            basic_auth=(os.getenv("JIRA_USERNAME"), os.getenv("JIRA_API_TOKEN"))
        )

    # ========================================
    # CONFLUENCE DATA LOADING
    # ========================================

    def load_confluence_page(self, module_key: str) -> dict:
        """Lädt Confluence-Daten für Modul"""
        # Map WEG-X zu Confluence Export Files
        confluence_mapping = {
            "WEG-1": "confluence_export/WEG-1-Platform-Foundation.md",
            "WEG-2": "confluence_export/WEG-2-Identity-Access.md",
            "WEG-3": "confluence_export/WEG-3-Tenant-Provisioning.md",
            "WEG-4": "confluence_export/WEG-4-Property-People.md",
            "WEG-5": "confluence_export/WEG-5-Document-Management.md",
            "WEG-6": "confluence_export/WEG-6-Messaging-Notifications.md",
            "WEG-7": "confluence_export/WEG-7-Metering.md",
            "WEG-8": "confluence_export/WEG-8-Finance-Banking.md",
            "WEG-9": "confluence_export/WEG-9-Meetings-Resolutions.md",
            "WEG-10": "confluence_export/WEG-10-Solution-Setup.md",
            "WEG-13": "confluence_export/WEG-13-Control-Plane.md",
            "WEG-30": "confluence_export/WEG-30-Association-Registry.md",
        }

        file_path = confluence_mapping.get(module_key)
        if not file_path or not os.path.exists(file_path):
            print(f"⚠️  Confluence file not found for {module_key}")
            return {
                'title': module_key,
                'content': f"No Confluence documentation found for {module_key}",
                'exists': False
            }

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        return {
            'title': module_key,
            'content': content,
            'exists': True,
            'file_path': file_path
        }

    # ========================================
    # LEVEL 1: EPIC WRITER AGENT
    # ========================================

    def generate_epic_writer_prompt(self, module_key: str) -> str:
        """Generiert Prompt für Epic Writer Agent (WEG-1 bis WEG-9)"""

        confluence_data = self.load_confluence_page(module_key)

        return f"""# Epic Writer Agent - WEG Management System

## 🎯 Your Role
You are an Epic Writer Agent responsible for creating high-level Epic issues in JIRA.
Your task is to transform Confluence documentation into comprehensive JIRA Epics that provide complete context for downstream agents.

## 📋 Current Task
Create Epic for: **{module_key}**

## 📖 Source Data

### Confluence Documentation
{confluence_data['content'][:3000] if confluence_data['exists'] else 'No documentation available'}

{'... (truncated, full content in file: ' + confluence_data.get('file_path', 'N/A') + ')' if confluence_data['exists'] else ''}

## 🎯 Your Mission

Create a JIRA Epic issue for {module_key} using the **Epic Template** from:
`/home/user/MyRep/JIRA_Templates_for_KI_Agents.md`

### Epic Template Structure

Use this exact structure for the Epic description:

```markdown
# {module_key} – [Module Name]

## Überblick
[2-3 sentences describing the module's purpose and scope]

## Hauptfunktionen
- **Function 1:** Description
- **Function 2:** Description
- **Function 3:** Description

## Technischer Ansatz

### Domain Model
```csharp
// Key entities for this module
public class [EntityName] : BaseEntity
{{
    public Guid Id {{ get; private set; }}
    public string Name {{ get; private set; }}
    // ... properties
}}
```

### API Endpoints
- `GET /api/[resource]` - List all
- `POST /api/[resource]` - Create new
- `PUT /api/[resource]/{{id}}` - Update
- `DELETE /api/[resource]/{{id}}` - Delete

### Database Schema
- Tables: [TableName1], [TableName2]
- Key relationships: [Description]

## Akzeptanzkriterien (Epic-Level)

✅ **Gegeben:** [Precondition]
**Wenn:** [Action]
**Dann:** [Expected outcome]

✅ **Gegeben:** [Precondition]
**Wenn:** [Action]
**Dann:** [Expected outcome]

## Abhängigkeiten
- Requires: [WEG-X, WEG-Y] (must be completed first)
- Blocks: [WEG-Z] (this Epic blocks these)

## Verknüpfte Untermodule (Stories)
- WEG-XX – [Story Name]
- WEG-XX – [Story Name]
- WEG-XX – [Story Name]

## Confluence
**Dokumentation:** {confluence_data.get('file_path', 'N/A')}
```

## 🛠️ Implementation Steps

1. **Extract Information from Confluence**
   - Read the Confluence content above
   - Identify main functionalities
   - Extract domain entities
   - Identify API requirements
   - Find dependencies on other modules

2. **Use JIRA Templates**
   ```bash
   # Load Epic template
   cat /home/user/MyRep/JIRA_Templates_for_KI_Agents.md | grep -A 200 "Epic Template"
   ```

3. **Create Epic in JIRA**
   ```python
   from jira_automation_example import WegJiraAutomation

   jira = WegJiraAutomation()

   epic = jira.create_epic(
       summary="{module_key} – [Module Name from Confluence]",
       description='''
       [Full Epic description using template above]
       ''',
       labels=['module', 'epic', 'weg-{module_key.split("-")[1]}']
   )

   print(f"✅ Created Epic: {{epic.key}}")
   ```

4. **Verify Epic Contains Everything for Next Level**

   The Epic MUST contain enough information for Story Writer Agents to create detailed Stories:

   ✅ **Domain Model:** Clear entity definitions
   ✅ **API Contracts:** Endpoint specifications
   ✅ **Database Schema:** Table structures
   ✅ **Acceptance Criteria:** What "done" means
   ✅ **Dependencies:** What needs to be ready first
   ✅ **Submodule List:** Breakdown into Stories

## 📏 Quality Checklist

Before creating the Epic, ensure:

- [ ] Epic summary follows format: "WEG-X – [Module Name]"
- [ ] Description uses Epic template structure
- [ ] Domain model includes at least main entity
- [ ] API endpoints are specified
- [ ] Database schema is outlined
- [ ] Acceptance criteria use Given-When-Then
- [ ] Dependencies are listed
- [ ] Confluence link is included
- [ ] Labels are appropriate
- [ ] Information is complete for downstream agents

## 🎯 Success Criteria

Epic is successful when:
1. ✅ JIRA Epic is created with key {module_key}
2. ✅ Epic contains complete domain model
3. ✅ Epic lists all expected Stories (WEG-10+)
4. ✅ Epic has clear acceptance criteria
5. ✅ Story Writer Agent can read this Epic and create detailed Stories without additional research

## 🚀 Begin Epic Creation

Create the Epic now following the template and quality standards above.

**IMPORTANT:** The Epic you create will be the foundation for all Stories and Tasks in this module.
Make it comprehensive and clear!
"""

    # ========================================
    # LEVEL 2: STORY WRITER AGENT
    # ========================================

    def generate_story_writer_prompt(self, epic_key: str) -> str:
        """Generiert Prompt für Story Writer Agent (WEG-10 bis WEG-99)"""

        # Get Epic from JIRA
        try:
            epic = self.jira.issue(epic_key)
            epic_summary = epic.fields.summary
            epic_description = epic.fields.description or ""
        except Exception as e:
            print(f"⚠️  Could not load Epic {epic_key}: {e}")
            epic_summary = epic_key
            epic_description = "Epic not found"

        # Get Confluence for this Epic's submodules
        confluence_data = self.load_confluence_page(epic_key)

        return f"""# Story Writer Agent - WEG Management System

## 🎯 Your Role
You are a Story Writer Agent responsible for breaking down Epics into detailed Stories.
Your task is to create comprehensive Story issues that provide complete implementation context for Task Writer Agents.

## 📋 Current Task
Create Stories for Epic: **{epic_key} - {epic_summary}**

## 📖 Context

### Parent Epic
**Epic Key:** {epic_key}
**Summary:** {epic_summary}

**Epic Description:**
```
{epic_description[:2000]}
...
```

### Confluence Documentation
{confluence_data['content'][:2000] if confluence_data['exists'] else 'Use Epic description as primary source'}

## 🎯 Your Mission

Create Stories (WEG-10 to WEG-99 range) that break down the Epic into implementable features.

Each Story should use the **Story Template** from:
`/home/user/MyRep/JIRA_Templates_for_KI_Agents.md`

### Story Template Structure

```markdown
# WEG-XX – [Story Name]

## Ziel
[1-2 sentences: What is the goal of this Story?]

## User Story
Als [Rolle] möchte ich [Aktion], damit [Nutzen].

## Technischer Ansatz

### Domain Layer
```csharp
// Entity implementation
public class [Entity] : BaseEntity
{{
    // Properties from Epic's domain model
    public Guid Id {{ get; private set; }}
    public string Name {{ get; private set; }}

    // Factory method
    public static [Entity] Create(params)
    {{
        // Validation
        // Creation logic
    }}
}}
```

### Application Layer (CQRS)
```csharp
// Command
public record Create[Entity]Command(string Name, ...) : IRequest<Result<Guid>>;

// Query
public record Get[Entity]Query(Guid Id) : IRequest<Result<[Entity]Dto>>;
```

### API Layer
```csharp
[ApiController]
[Route("api/[controller]")]
public class [Entity]Controller : ControllerBase
{{
    [HttpPost]
    public async Task<IActionResult> Create([FromBody] Create[Entity]Command command)
    {{
        // MediatR dispatch
    }}
}}
```

### Frontend
```typescript
// React Component
export const [Entity]List: React.FC = () => {{
    const {{ data }} = use[Entities]();
    // Component implementation
}}
```

## Akzeptanzkriterien (BDD)

✅ **Gegeben:** [Precondition]
**Wenn:** [Action]
**Dann:** [Expected outcome]
**Und:** [Additional verification]

✅ **Gegeben:** [Error scenario precondition]
**Wenn:** [Invalid action]
**Dann:** [Error handling]
**Und:** [Error message verification]

## Verknüpfte Tasks (Sub-Tasks)
- WEG-XXX – Create [Entity] Domain Model
- WEG-XXX – Implement CQRS Commands for [Entity]
- WEG-XXX – Implement CQRS Queries for [Entity]
- WEG-XXX – Create API Controller for [Entity]
- WEG-XXX – Implement [Entity] Repository
- WEG-XXX – Create [Entity]List React Component
- WEG-XXX – Create [Entity]Form React Component
- WEG-XXX – Write Integration Tests
```

## 🛠️ Implementation Steps

1. **Analyze Epic**
   - Read Epic description thoroughly
   - Identify distinct features/capabilities
   - Each feature becomes one Story

2. **Determine Story Breakdown**

   Typical breakdown for an Epic:
   - **Setup Story:** Project structure, base classes
   - **Core Entity Stories:** One Story per main entity
   - **Feature Stories:** Specific functionalities
   - **Integration Stories:** External systems
   - **Testing Story:** Test infrastructure

3. **For Each Story:**

   a. **Define User Story**
   ```
   Als [Administrator|Eigentümer|Verwalter]
   möchte ich [specific capability]
   damit [business value]
   ```

   b. **Technical Approach**
   - Copy relevant parts from Epic's domain model
   - Add CQRS commands/queries
   - Specify API endpoints
   - Define React components

   c. **BDD Acceptance Criteria**
   ```
   ✅ Gegeben: User is authenticated as Administrator
   Wenn: User creates new Association with valid data
   Dann: Association is created with generated ID
   Und: User receives success notification
   Und: Association appears in list

   ✅ Gegeben: User provides invalid Association name (empty)
   Wenn: User submits create form
   Dann: Validation error is returned
   Und: Error message "Name is required" is displayed
   ```

   d. **List Sub-Tasks**
   - Break implementation into Sub-Tasks (WEG-100+)
   - Each Sub-Task = one code file or component

4. **Create Stories in JIRA**

   ```python
   from jira_automation_example import WegJiraAutomation

   jira = WegJiraAutomation()

   # Example: Create Story for Association Entity
   story = jira.create_story(
       summary="WEG-30 – Association Registry & Provisioning",
       description='''
       [Full Story description using template]
       ''',
       epic_key="{epic_key}",
       labels=['story', 'backend', 'domain']
   )

   print(f"✅ Created Story: {{story.key}}")
   ```

5. **Link to Epic**
   ```python
   jira.jira.add_issues_to_epic('{epic_key}', [story.key])
   ```

## 📊 Story Breakdown Guidelines

For {epic_key}, create approximately 5-10 Stories covering:

### Infrastructure Stories (if applicable)
- WEG-10: Solution Setup
- WEG-11: API & OpenAPI
- WEG-12: Error Handling & Logging

### Domain Stories (core entities)
- WEG-XX: [Main Entity] CRUD
- WEG-XX: [Secondary Entity] Management
- WEG-XX: [Relationship] Handling

### Feature Stories
- WEG-XX: [Specific Feature]
- WEG-XX: [Integration with other module]

### Testing & Documentation
- WEG-XX: Integration Tests
- WEG-XX: E2E Tests

## 📏 Quality Checklist

Each Story MUST have:
- [ ] Clear User Story (Als...möchte ich...damit...)
- [ ] Technical Approach with code examples
- [ ] BDD Acceptance Criteria (minimum 3 scenarios)
- [ ] List of Sub-Tasks (5-10 tasks)
- [ ] Link to parent Epic
- [ ] Appropriate labels
- [ ] Enough detail for Task Writer Agent

## 🎯 Success Criteria

Stories are successful when:
1. ✅ Each Story represents a cohesive feature
2. ✅ Stories cover all functionality from Epic
3. ✅ Each Story has complete technical approach
4. ✅ BDD criteria are testable
5. ✅ Task Writer Agent can create Sub-Tasks without additional research
6. ✅ Developer can implement the Story by following the description

## 🚀 Begin Story Creation

Create Stories now for Epic {epic_key}.

Analyze the Epic, identify 5-10 distinct Stories, and create them using the template.

**IMPORTANT:** Each Story should be detailed enough that a developer (or Task Writer Agent)
can break it down into specific Sub-Tasks without needing to go back to Confluence.
"""

    # ========================================
    # LEVEL 3: TASK WRITER AGENT
    # ========================================

    def generate_task_writer_prompt(self, story_key: str) -> str:
        """Generiert Prompt für Task Writer Agent (WEG-100+)"""

        # Get Story from JIRA
        try:
            story = self.jira.issue(story_key)
            story_summary = story.fields.summary
            story_description = story.fields.description or ""

            # Get Epic
            epic_key = story.fields.customfield_10014 if hasattr(story.fields, 'customfield_10014') else None
            if epic_key:
                epic = self.jira.issue(epic_key)
                epic_summary = epic.fields.summary
                epic_description = epic.fields.description or ""
            else:
                epic_summary = "No Epic"
                epic_description = ""

        except Exception as e:
            print(f"⚠️  Could not load Story {story_key}: {e}")
            story_summary = story_key
            story_description = "Story not found"
            epic_summary = "Unknown"
            epic_description = ""

        return f"""# Task Writer Agent - WEG Management System

## 🎯 Your Role
You are a Task Writer Agent responsible for breaking down Stories into atomic Sub-Tasks.
Your task is to create detailed Sub-Task issues with complete implementation instructions including full code examples.

## 📋 Current Task
Create Sub-Tasks for Story: **{story_key} - {story_summary}**

## 📖 Context

### Parent Story
**Story Key:** {story_key}
**Summary:** {story_summary}

**Story Description:**
```
{story_description[:2000]}
...
```

### Grand-Parent Epic
**Epic:** {epic_summary}

**Epic Context:**
```
{epic_description[:1000]}
...
```

## 🎯 Your Mission

Create Sub-Tasks (WEG-100+ range) that break the Story into implementable code units.

Each Sub-Task should use the **Sub-Task Template** from:
`/home/user/MyRep/JIRA_Templates_for_KI_Agents.md`

### Sub-Task Template Structure

```markdown
# WEG-XXX – [Specific Implementation Task]

## Implementation

[Detailed description of what to implement]

### File Location
`/path/to/file.cs` or `/path/to/component.tsx`

### Code

```csharp
// COMPLETE, WORKING CODE (not just signatures!)
namespace WegManagement.Domain.Entities;

public class [Entity] : BaseEntity
{{
    public Guid Id {{ get; private set; }}
    public string Name {{ get; private set; }}
    public [Entity]Status Status {{ get; private set; }}

    private [Entity]()
    {{
        // EF Core constructor
    }}

    public static [Entity] Create(string name, Guid associationId)
    {{
        ValidateName(name);
        ValidateAssociationId(associationId);

        return new [Entity]
        {{
            Id = Guid.NewGuid(),
            Name = name.Trim(),
            Status = [Entity]Status.Active,
            AssociationId = associationId,
            CreatedAt = DateTime.UtcNow
        }};
    }}

    public void UpdateName(string name)
    {{
        ValidateName(name);
        Name = name.Trim();
        UpdatedAt = DateTime.UtcNow;
    }}

    private static void ValidateName(string name)
    {{
        if (string.IsNullOrWhiteSpace(name))
            throw new ArgumentException("Name cannot be empty", nameof(name));
        if (name.Length > 200)
            throw new ArgumentException("Name cannot exceed 200 characters", nameof(name));
    }}

    private static void ValidateAssociationId(Guid associationId)
    {{
        if (associationId == Guid.Empty)
            throw new ArgumentException("AssociationId cannot be empty", nameof(associationId));
    }}
}}
```

## Verification

```bash
# Build
dotnet build

# Test
dotnet test

# Expected: All tests pass, no warnings
```

## Acceptance Criteria

✅ File created at specified location
✅ Code compiles without errors
✅ All validations implemented
✅ Unit tests pass
✅ Follows naming conventions (English)
```

## 🛠️ Implementation Steps

1. **Analyze Story**
   - Read Story description
   - Identify all code artifacts needed
   - Each artifact = one Sub-Task

2. **Typical Sub-Task Breakdown**

   For a Story about creating an Entity:

   **Backend Sub-Tasks:**
   - WEG-XXX: Create [Entity] Domain Entity
   - WEG-XXX: Create [Entity]Dto
   - WEG-XXX: Implement Create[Entity]Command
   - WEG-XXX: Implement Create[Entity]CommandHandler
   - WEG-XXX: Implement Get[Entity]Query
   - WEG-XXX: Implement Get[Entity]QueryHandler
   - WEG-XXX: Create [Entity]Repository
   - WEG-XXX: Create [Entity]Controller
   - WEG-XXX: Add [Entity]DbSet to DbContext
   - WEG-XXX: Create EF Migration for [Entity]

   **Frontend Sub-Tasks:**
   - WEG-XXX: Generate TypeScript API Client for [Entity]
   - WEG-XXX: Create [Entity]List Component
   - WEG-XXX: Create [Entity]Form Component
   - WEG-XXX: Create [Entity]Detail Component
   - WEG-XXX: Add [Entity] Routes

   **Testing Sub-Tasks:**
   - WEG-XXX: Write [Entity] Unit Tests
   - WEG-XXX: Write [Entity] Integration Tests
   - WEG-XXX: Write [Entity] E2E Tests (Playwright)

3. **For Each Sub-Task:**

   a. **Choose Template**
   - Backend: Use C# templates from JIRA_Templates
   - Frontend: Use TypeScript/React templates
   - Infrastructure: Use Docker/YAML templates

   b. **Write Complete Code**
   ```
   ⚠️  CRITICAL: Don't write code signatures - write COMPLETE, WORKING CODE!

   ❌ BAD:
   public class Association
   {{
       // TODO: Add properties
   }}

   ✅ GOOD:
   public class Association : BaseEntity
   {{
       public Guid Id {{ get; private set; }}
       public string Name {{ get; private set; }}
       // ... complete implementation with all methods
   }}
   ```

   c. **Specify File Path**
   ```
   Exact file location:
   /src/WegManagement.Domain/Entities/Association.cs
   ```

   d. **Add Verification Steps**
   ```bash
   dotnet build
   dotnet test
   ```

4. **Create Sub-Tasks in JIRA**

   ```python
   from jira_automation_example import WegJiraAutomation

   jira = WegJiraAutomation()

   # Example: Create Sub-Task for Entity
   subtask = jira.create_subtask(
       summary="Create Association Domain Entity",
       description='''
       ## Implementation

       Create Domain Entity for Association.

       ### File Location
       `/src/WegManagement.Domain/Entities/Association.cs`

       ### Code
       ```csharp
       [COMPLETE CODE HERE]
       ```

       ### Verification
       ```bash
       dotnet build
       dotnet test
       ```

       ### Acceptance Criteria
       ✅ File created at specified location
       ✅ Code compiles
       ✅ All tests pass
       ''',
       parent_key="{story_key}",
       priority="High",
       labels=['backend', 'domain', 'entity']
   )

   print(f"✅ Created Sub-Task: {{subtask.key}}")
   ```

5. **Link to Story**
   Sub-Tasks are automatically linked via parent_key

## 📊 Sub-Task Guidelines

### Backend Sub-Tasks
- **Domain:** Entities, Value Objects, Domain Services
- **Application:** Commands, Queries, Handlers, DTOs, Validators
- **Infrastructure:** Repositories, DbContext, Configurations
- **API:** Controllers, Middleware

### Frontend Sub-Tasks
- **Components:** List, Form, Detail views
- **Hooks:** Custom hooks for data fetching
- **API Client:** TypeScript generated clients
- **Routes:** React Router configuration

### Testing Sub-Tasks
- **Unit Tests:** xUnit for backend, Vitest for frontend
- **Integration Tests:** API endpoint tests
- **E2E Tests:** Playwright scenarios

## 📏 Quality Checklist

Each Sub-Task MUST have:
- [ ] Specific, actionable title
- [ ] Complete code implementation (not pseudocode!)
- [ ] Exact file path
- [ ] Verification commands
- [ ] Acceptance criteria
- [ ] Appropriate labels (backend/frontend/infrastructure)
- [ ] Link to parent Story
- [ ] Can be implemented by developer in 2-4 hours

## 🎯 Success Criteria

Sub-Tasks are successful when:
1. ✅ Each Sub-Task is atomic (one file or component)
2. ✅ Code is complete and copy-pasteable
3. ✅ File paths are exact
4. ✅ Implementation Agent can complete task without additional research
5. ✅ Code compiles and tests pass after implementation

## 🚀 Begin Sub-Task Creation

Create Sub-Tasks now for Story {story_key}.

Break down the Story into 10-20 atomic Sub-Tasks with complete implementation details.

**IMPORTANT:** Each Sub-Task should contain COMPLETE, WORKING CODE that a developer
can copy-paste directly into the specified file. No pseudocode, no TODOs!
"""

    # ========================================
    # ORCHESTRATION
    # ========================================

    def save_prompt_to_file(self, prompt: str, level: str, key: str) -> str:
        """Speichert Prompt in Datei"""
        filename = f"/tmp/jira_writer_{level}_{key}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(prompt)
        return filename

    def create_epic_prompt(self, module_key: str):
        """Erstellt Prompt für Epic Writer Agent"""
        print(f"{'='*60}")
        print(f"📝 Generating Epic Writer Prompt for {module_key}")
        print(f"{'='*60}\n")

        prompt = self.generate_epic_writer_prompt(module_key)
        filename = self.save_prompt_to_file(prompt, "epic", module_key)

        print(f"✅ Epic Writer Prompt generated")
        print(f"📄 Saved to: {filename}")
        print(f"\n📋 Next Steps:")
        print(f"   1. Open Claude Code Web")
        print(f"   2. Paste the prompt from: {filename}")
        print(f"   3. Agent will create Epic {module_key} in JIRA")
        print(f"   4. After Epic is created, run:")
        print(f"      python jira_writer_agent.py --level story --epic {module_key}")

    def create_story_prompts(self, epic_key: str):
        """Erstellt Prompt für Story Writer Agent"""
        print(f"{'='*60}")
        print(f"📝 Generating Story Writer Prompt for Epic {epic_key}")
        print(f"{'='*60}\n")

        prompt = self.generate_story_writer_prompt(epic_key)
        filename = self.save_prompt_to_file(prompt, "story", epic_key)

        print(f"✅ Story Writer Prompt generated")
        print(f"📄 Saved to: {filename}")
        print(f"\n📋 Next Steps:")
        print(f"   1. Open Claude Code Web")
        print(f"   2. Paste the prompt from: {filename}")
        print(f"   3. Agent will create Stories for Epic {epic_key}")
        print(f"   4. After Stories are created, for each Story run:")
        print(f"      python jira_writer_agent.py --level task --story WEG-XX")

    def create_task_prompts(self, story_key: str):
        """Erstellt Prompt für Task Writer Agent"""
        print(f"{'='*60}")
        print(f"📝 Generating Task Writer Prompt for Story {story_key}")
        print(f"{'='*60}\n")

        prompt = self.generate_task_writer_prompt(story_key)
        filename = self.save_prompt_to_file(prompt, "task", story_key)

        print(f"✅ Task Writer Prompt generated")
        print(f"📄 Saved to: {filename}")
        print(f"\n📋 Next Steps:")
        print(f"   1. Open Claude Code Web")
        print(f"   2. Paste the prompt from: {filename}")
        print(f"   3. Agent will create Sub-Tasks for Story {story_key}")
        print(f"   4. Sub-Tasks are ready for Implementation Agents!")

    def create_full_hierarchy(self, module_key: str):
        """Erstellt komplette Hierarchie: Epic → Stories → Tasks"""
        print(f"{'='*60}")
        print(f"🚀 Creating Full Hierarchy for {module_key}")
        print(f"{'='*60}\n")

        # Step 1: Epic
        print("STEP 1: Epic Writer Agent")
        print("-" * 60)
        self.create_epic_prompt(module_key)

        print("\n\n⏸️  PAUSE - Epic must be created before continuing")
        print("After Epic is created in JIRA, run:")
        print(f"  python jira_writer_agent.py --level story --epic {module_key}")


# ========================================
# CLI
# ========================================

def main():
    parser = argparse.ArgumentParser(
        description='JIRA Writer Agent - Hierarchical JIRA Creation'
    )

    parser.add_argument(
        '--level',
        choices=['epic', 'story', 'task'],
        help='Agent level: epic (WEG-1 to WEG-9), story (WEG-10+), or task (WEG-100+)'
    )

    parser.add_argument(
        '--module',
        type=str,
        help='Module key for Epic (e.g., WEG-1)'
    )

    parser.add_argument(
        '--epic',
        type=str,
        help='Epic key for Stories (e.g., WEG-1)'
    )

    parser.add_argument(
        '--story',
        type=str,
        help='Story key for Tasks (e.g., WEG-10)'
    )

    parser.add_argument(
        '--full-hierarchy',
        type=str,
        help='Create full hierarchy for module (e.g., WEG-1)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Dry run mode'
    )

    args = parser.parse_args()

    agent = JiraWriterAgent(dry_run=args.dry_run)

    if args.full_hierarchy:
        agent.create_full_hierarchy(args.full_hierarchy)
    elif args.level == 'epic' and args.module:
        agent.create_epic_prompt(args.module)
    elif args.level == 'story' and args.epic:
        agent.create_story_prompts(args.epic)
    elif args.level == 'task' and args.story:
        agent.create_task_prompts(args.story)
    else:
        print("❌ Invalid arguments. Use --help for usage information.")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
