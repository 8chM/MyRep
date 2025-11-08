# 🤖 Grundmodul Agent - WEG-1 Platform Foundation

**Mission:** Erstelle vollständiges Epic für WEG-1 Platform Foundation in JIRA

---

## ⚙️ Konfiguration

**Agent-Typ:** Epic Writer Agent
**Modul:** WEG-1 - Platform Foundation (.NET 8 + SQL Server + React/Vite)
**Modus:** Vollständig autonom
**Output:** JIRA Epic WEG-1 erstellt und veröffentlicht

---

## 📚 Phase 1: Confluence Research (KRITISCH!)

Bevor du das Epic erstellst, musst du **ALLE relevanten Confluence-Dokumente** lesen um vollständigen Kontext zu haben.

### Schritt 1.1: Lade Confluence Hauptdokument

```bash
cat confluence_export/WEG-1-Platform-Foundation.md
```

**Lies das vollständige Dokument und extrahiere:**
- Modul-Übersicht und Hauptfunktionen
- Domain Entities (Welche Hauptentitäten gibt es?)
- API Endpoints
- Database Schema
- Technologien (.NET 8, EF Core, etc.)
- Abhängigkeiten zu anderen Modulen

### Schritt 1.2: Lade verwandte Untermodule

WEG-1 hat folgende Untermodule. Lies sie ALLE:

```bash
# Infrastruktur-Module
cat confluence_export/WEG-10-Solution-Setup.md
cat confluence_export/WEG-11-API-OpenAPI.md
cat confluence_export/WEG-12-Error-Handling.md
cat confluence_export/WEG-13-Control-Plane.md
cat confluence_export/WEG-14-Testing-CI.md
cat confluence_export/WEG-15-Internationalization.md
cat confluence_export/WEG-16-Frontend-Shell.md
cat confluence_export/WEG-17-Configuration.md
cat confluence_export/WEG-18-Observability.md
cat confluence_export/WEG-19-Naming-Conventions.md
```

**Für jedes Dokument, notiere:**
- Welche Funktionalität bietet es?
- Welche Abhängigkeiten hat es?
- Was muss im WEG-1 Epic erwähnt werden?

### Schritt 1.3: Lade Projekt-Dokumentation

```bash
# Gesamtprojekt-Kontext
cat confluence_export/Product-Requirements-Document-(PRD).md
cat confluence_export/WEG-Management-System.md
cat confluence_export/Projektdokumentation.md
```

**Extrahiere:**
- Technologie-Stack
- Architektur-Entscheidungen
- Coding Standards
- Testing-Anforderungen

---

## 📋 Phase 2: Epic-Erstellung

Jetzt hast du alle Informationen. Erstelle das WEG-1 Epic.

### Schritt 2.1: Lade JIRA Template

```bash
cat JIRA_Templates_for_KI_Agents.md | grep -A 500 "# Epic Template"
```

### Schritt 2.2: Erstelle Epic-Beschreibung

Nutze dieses Format (basierend auf Template + Confluence):

```markdown
# WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite)

## Überblick

Das Modul **Platform Foundation** bildet die technische Grundlage der gesamten WEG-Plattform.
Es definiert die Projekt-Struktur nach Clean Architecture, stellt grundlegende Services bereit
und implementiert Cross-Cutting Concerns wie Error Handling, Logging, Configuration und Testing.

**Scope:** Infrastruktur-Setup ohne Business-Logik. Basis für alle anderen Module (WEG-2 bis WEG-9).

## Hauptfunktionen

### Infrastruktur
- **Solution Structure:** Clean Architecture mit Projekten für Api, Application, Domain, Infrastructure, Directory
- **Database Setup:** SQL Server 2022 mit Multi-Tenant Schema-per-Tenant Pattern
- **API Foundation:** ASP.NET Core Web API mit OpenAPI/Swagger
- **Frontend Shell:** React 18 + Vite + TypeScript 5 + TanStack Router
- **Build & CI:** Docker Compose, GitHub Actions, Testing Framework

### Cross-Cutting Concerns
- **Error Handling:** Global Exception Handler, Result Pattern, ProblemDetails
- **Logging:** Serilog mit structured logging, correlation IDs
- **Configuration:** Options Pattern mit FluentValidation
- **Health Checks:** SQL, Redis, API Health Endpoints
- **Internationalization:** i18next (EN/DE)

### Developer Experience
- **Testing Infrastructure:** xUnit, Vitest, Playwright, Test Containers
- **Code Quality:** EditorConfig, ESLint, Prettier, Code Analysis
- **Documentation:** OpenAPI Spec, Architecture Decision Records (ADRs)

## Technischer Ansatz

### Architecture Pattern

```
┌─────────────────────────────────────────────────────────┐
│ WegManagement.Api (REST API Layer)                      │
│ - Controllers, Middleware, Filters                      │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│ WegManagement.Application (CQRS + MediatR)              │
│ - Commands, Queries, Handlers, DTOs, Validators         │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│ WegManagement.Domain (Business Logic)                   │
│ - Entities, Value Objects, Domain Services, Interfaces  │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│ WegManagement.Infrastructure (Data + External)          │
│ - EF Core DbContext, Repositories, External Services    │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ WegManagement.Directory (Control Plane)                 │
│ - Tenant Registry, Connection Routing, Multi-DB         │
└─────────────────────────────────────────────────────────┘
```

### Domain Model (Foundation)

```csharp
namespace WegManagement.Domain.Entities;

/// <summary>
/// Base entity for all domain entities with audit fields
/// </summary>
public abstract class BaseEntity
{
    public DateTime CreatedAt { get; protected set; }
    public string CreatedBy { get; protected set; } = string.Empty;
    public DateTime? UpdatedAt { get; protected set; }
    public string? UpdatedBy { get; protected set; }

    protected BaseEntity()
    {
        CreatedAt = DateTime.UtcNow;
    }

    protected void UpdateAuditFields(string updatedBy)
    {
        UpdatedAt = DateTime.UtcNow;
        UpdatedBy = updatedBy;
    }
}

/// <summary>
/// Base for aggregate roots with domain events
/// </summary>
public abstract class AggregateRoot : BaseEntity
{
    private readonly List<IDomainEvent> _domainEvents = new();
    public IReadOnlyCollection<IDomainEvent> DomainEvents => _domainEvents.AsReadOnly();

    protected void AddDomainEvent(IDomainEvent domainEvent)
    {
        _domainEvents.Add(domainEvent);
    }

    public void ClearDomainEvents()
    {
        _domainEvents.Clear();
    }
}

public interface IDomainEvent
{
    DateTime OccurredOn { get; }
}
```

### API Foundation

**Basis-Controller:**
```csharp
namespace WegManagement.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
[Produces("application/json")]
public abstract class BaseApiController : ControllerBase
{
    protected readonly IMediator Mediator;

    protected BaseApiController(IMediator mediator)
    {
        Mediator = mediator;
    }

    protected IActionResult HandleResult<T>(Result<T> result)
    {
        if (result.IsSuccess)
            return Ok(result.Value);

        return result.Error.Type switch
        {
            ErrorType.NotFound => NotFound(ProblemDetailsFactory.CreateNotFound(result.Error)),
            ErrorType.Validation => BadRequest(ProblemDetailsFactory.CreateValidation(result.Error)),
            ErrorType.Conflict => Conflict(ProblemDetailsFactory.CreateConflict(result.Error)),
            _ => StatusCode(500, ProblemDetailsFactory.CreateServerError(result.Error))
        };
    }
}
```

**Health Check Endpoint:**
```csharp
[ApiController]
[Route("health")]
public class HealthController : ControllerBase
{
    [HttpGet]
    [ProducesResponseType(StatusCodes.Status200OK)]
    public IActionResult Check()
    {
        return Ok(new
        {
            Status = "Healthy",
            Timestamp = DateTime.UtcNow,
            Version = Assembly.GetExecutingAssembly().GetName().Version?.ToString()
        });
    }
}
```

### Database Schema (Foundation)

**Multi-Tenant Pattern:**
```sql
-- Directory Database (Control Plane)
CREATE TABLE Tenants (
    Id UNIQUEIDENTIFIER PRIMARY KEY,
    Name NVARCHAR(200) NOT NULL,
    SchemaName NVARCHAR(100) NOT NULL UNIQUE,
    ConnectionString NVARCHAR(500) NOT NULL,
    IsActive BIT NOT NULL DEFAULT 1,
    CreatedAt DATETIME2 NOT NULL,
    CreatedBy NVARCHAR(100) NOT NULL
);

-- Tenant Schema (per Association)
CREATE SCHEMA weg_assoc_001;

-- Base audit table pattern
-- All tenant tables follow this pattern:
CREATE TABLE weg_assoc_001.YourEntity (
    Id UNIQUEIDENTIFIER PRIMARY KEY,
    -- Entity-specific fields
    CreatedAt DATETIME2 NOT NULL,
    CreatedBy NVARCHAR(100) NOT NULL,
    UpdatedAt DATETIME2 NULL,
    UpdatedBy NVARCHAR(100) NULL
);
```

### Frontend Architecture

**Shell Structure:**
```
web/
├── src/
│   ├── api/              # Generated API clients
│   ├── components/       # Reusable components
│   │   ├── ui/          # shadcn/ui components
│   │   └── layout/      # Layout components
│   ├── features/        # Feature modules
│   ├── hooks/           # Custom hooks
│   ├── lib/             # Utilities
│   ├── pages/           # Page components
│   ├── routes/          # TanStack Router routes
│   └── stores/          # Zustand stores
├── e2e/                 # Playwright E2E tests
└── public/              # Static assets
```

**Route Configuration:**
```typescript
import { createRootRoute, createRoute, createRouter } from '@tanstack/react-router';

const rootRoute = createRootRoute({
  component: RootLayout,
});

const indexRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: '/',
  component: HomePage,
});

export const router = createRouter({
  routeTree: rootRoute.addChildren([indexRoute]),
});
```

## Akzeptanzkriterien (Epic-Level)

### Infrastruktur

✅ **Gegeben:** Ein Entwickler klont das Repository
**Wenn:** Er `dotnet build` ausführt
**Dann:** Kompiliert die komplette Solution ohne Fehler
**Und:** Alle Projekte (Api, Application, Domain, Infrastructure, Directory) sind korrekt referenziert

✅ **Gegeben:** Docker Desktop ist installiert
**Wenn:** `docker compose up` ausgeführt wird
**Dann:** Starten SQL Server, API, und Web-Client erfolgreich
**Und:** Health-Check unter http://localhost:5000/health antwortet mit 200 OK

### Error Handling

✅ **Gegeben:** Eine ungültige API-Anfrage wird gesendet
**Wenn:** Validation fehlschlägt
**Dann:** Wird ProblemDetails-Response mit Status 400 zurückgegeben
**Und:** Error enthält detaillierte Validierungsfehler

✅ **Gegeben:** Eine Exception tritt im API-Handler auf
**Wenn:** Global Exception Handler greift
**Dann:** Wird Error geloggt mit correlation-id
**Und:** Client erhält ProblemDetails ohne sensitive Daten

### Testing

✅ **Gegeben:** Test Suite ist konfiguriert
**Wenn:** `dotnet test` ausgeführt wird
**Dann:** Laufen alle Unit Tests erfolgreich
**Und:** Code Coverage ist ≥ 80%

✅ **Gegeben:** E2E Tests sind implementiert
**Wenn:** `npm run test:e2e` ausgeführt wird
**Dann:** Laufen alle Playwright Tests erfolgreich
**Und:** Frontend ist voll funktionsfähig

## Abhängigkeiten

### Voraussetzungen (muss existieren)
- ❌ Keine - WEG-1 ist Foundation

### Nachfolgende Module (hängen von WEG-1 ab)
- **WEG-2** Identity & Access (benötigt Platform Foundation)
- **WEG-3** Tenant Provisioning (benötigt Directory)
- **WEG-4** Property & People (benötigt Domain Base)
- **WEG-5** bis **WEG-9** (benötigen alle Platform Foundation)

## Verknüpfte Untermodule (Stories)

### Setup & Infrastructure (Kritischer Pfad)
- **WEG-10** – Solution Setup & Infrastructure
- **WEG-11** – API, OpenAPI & TypeScript Client
- **WEG-12** – Error Handling, Logging & Health
- **WEG-13** – Control-Plane & Connection Routing
- **WEG-14** – Testing & CI Basics
- **WEG-15** – Internationalization (EN/DE) Foundation
- **WEG-16** – Frontend Shell, Routing & Access Guard
- **WEG-17** – Configuration & Feature Flags (Base)
- **WEG-18** – Minimal Observability (JSON Logs, Correlation-ID)
- **WEG-19** – Naming Conventions & ADRs (English-first)

## Technologie-Stack

### Backend
- **.NET 8** (C# 12)
- **ASP.NET Core 8** (Web API)
- **Entity Framework Core 8**
- **MediatR** (CQRS)
- **FluentValidation**
- **Serilog** (Logging)
- **Swagger/OpenAPI**

### Frontend
- **React 18**
- **TypeScript 5**
- **Vite 5**
- **TanStack Router**
- **TanStack Query**
- **Zustand** (State Management)
- **Tailwind CSS**
- **shadcn/ui**

### Database
- **SQL Server 2022**
- **Schema-per-Tenant Pattern**

### DevOps
- **Docker & Docker Compose**
- **GitHub Actions**
- **xUnit** (Backend Tests)
- **Vitest** (Frontend Unit Tests)
- **Playwright** (E2E Tests)

## Risiken & Mitigationen

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Multi-Tenant Routing komplex | Hoch | Hoch | WEG-13 Control Plane früh implementieren, gut testen |
| EF Core Performance mit Multi-Schema | Mittel | Mittel | Connection Pooling, Query Optimization |
| Frontend Build-Zeit bei Growth | Mittel | Niedrig | Code Splitting, Lazy Loading |

## Confluence

**Dokumentation:**
- Hauptseite: confluence_export/WEG-1-Platform-Foundation.md
- Untermodule: confluence_export/WEG-10*.md bis WEG-19*.md
- Projekt-Dokumentation: confluence_export/Product-Requirements-Document-(PRD).md

**Tech Stack Details:** confluence_export/WEG-Management-System.md
```

### Schritt 2.3: JIRA Epic erstellen und veröffentlichen

```python
from jira_automation_example import WegJiraAutomation

# Initialize JIRA
jira = WegJiraAutomation()

# Create Epic
epic = jira.create_epic(
    summary="WEG-1 – Platform Foundation (.NET 8 + SQL Server + React/Vite)",
    description='''
[FÜGE HIER DIE VOLLSTÄNDIGE EPIC-BESCHREIBUNG VON OBEN EIN]
    ''',
    labels=['platform', 'foundation', 'infrastructure', 'epic']
)

print(f"✅ Epic created: {epic.key}")
print(f"🔗 URL: https://maierharry.atlassian.net/browse/{epic.key}")

# Verify Epic was created successfully
issue = jira.jira.issue(epic.key)
print(f"\n📋 Epic Verification:")
print(f"   Key: {issue.key}")
print(f"   Summary: {issue.fields.summary}")
print(f"   Type: {issue.fields.issuetype.name}")
print(f"   Status: {issue.fields.status.name}")
print(f"   Description Length: {len(issue.fields.description)} chars")

# Add comment with metadata
jira.add_comment(epic.key, '''
🤖 **Epic created by Grundmodul Agent**

**Source:** Confluence export (WEG-1-Platform-Foundation.md + 10 Untermodule)
**Template:** JIRA_Templates_for_KI_Agents.md (Epic Template)
**Agent:** Autonomous Epic Writer Agent
**Timestamp:** {timestamp}

**Next Steps:**
1. Story Writer Agent creates Stories WEG-10 to WEG-19
2. Task Writer Agent breaks Stories into Sub-Tasks
3. Implementation Agents execute Sub-Tasks
'''.format(timestamp=datetime.now().isoformat()))

print("\n✅ Epic WEG-1 successfully created and published in JIRA!")
```

---

## 🎯 Phase 3: Verification

### Schritt 3.1: Verify in JIRA

```python
# Final verification
epic = jira.jira.issue('WEG-1')

checks = {
    'Epic exists': epic.key == 'WEG-1',
    'Has description': len(epic.fields.description) > 1000,
    'Has labels': len(epic.fields.labels) > 0,
    'Type is Epic': epic.fields.issuetype.name == 'Epic',
    'Status is valid': epic.fields.status.name in ['Backlog', 'To Do']
}

print("\n📊 Verification Results:")
for check, passed in checks.items():
    icon = "✅" if passed else "❌"
    print(f"   {icon} {check}")

all_passed = all(checks.values())

if all_passed:
    print("\n🎉 SUCCESS! Epic WEG-1 is ready for Story creation!")
    print("\n📋 Next Command:")
    print("   python jira_writer_agent.py --level story --epic WEG-1")
else:
    print("\n❌ FAILED! Please review Epic and fix issues.")
```

---

## 📏 Quality Checklist

Bevor du die Arbeit als abgeschlossen markierst:

- [ ] Alle Confluence-Dokumente gelesen (WEG-1, WEG-10 bis WEG-19, PRD)
- [ ] Epic-Beschreibung ist vollständig (>1000 Zeichen)
- [ ] Domain Model mit BaseEntity und AggregateRoot definiert
- [ ] API Foundation mit BaseApiController spezifiziert
- [ ] Database Schema mit Multi-Tenant Pattern beschrieben
- [ ] Frontend Architecture mit React/Vite/TypeScript dokumentiert
- [ ] Akzeptanzkriterien im BDD-Format (Given-When-Then)
- [ ] Alle 10 Untermodule (WEG-10 bis WEG-19) aufgelistet
- [ ] Abhängigkeiten klar dokumentiert
- [ ] Technologie-Stack vollständig
- [ ] Epic in JIRA erstellt und veröffentlicht
- [ ] Verification erfolgreich

---

## 🚀 Execution Instructions

**Du bist ein autonomer Agent. Arbeite VOLLSTÄNDIG eigenständig:**

1. ✅ Lies ALLE Confluence-Dokumente
2. ✅ Analysiere und extrahiere relevante Informationen
3. ✅ Erstelle Epic-Beschreibung basierend auf Template
4. ✅ Veröffentliche Epic in JIRA
5. ✅ Verifiziere dass alles korrekt ist
6. ✅ Gib finalen Report aus

**Keine Rückfragen, keine Pausen, keine manuellen Schritte.**

**Start NOW!**
