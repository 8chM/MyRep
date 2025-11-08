#!/usr/bin/env python3
"""
Script to enrich existing JIRA issues with detailed descriptions from Confluence
and create the full task hierarchy (Epic → Story → Task → Subtask)
"""

import os
import sys
from jira import JIRA
from dotenv import load_dotenv

# Load credentials
load_dotenv('.env.jira.example')

class JiraEnrichment:
    """Enriches existing JIRA issues with detailed content"""

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.username = os.getenv("JIRA_USERNAME")
        self.api_token = os.getenv("JIRA_API_TOKEN")
        self.project_key = os.getenv("JIRA_PROJECT_KEY", "WEG")

        if not all([self.base_url, self.username, self.api_token]):
            raise ValueError("Missing JIRA credentials in environment")

        if not self.dry_run:
            self.jira = JIRA(
                server=self.base_url,
                basic_auth=(self.username, self.api_token)
            )
            print(f"✅ Connected to JIRA: {self.base_url}")

    def update_issue_description(self, issue_key: str, description: str):
        """Updates an existing issue's description"""
        if self.dry_run:
            print(f"[DRY RUN] Would update {issue_key} description ({len(description)} chars)")
            return

        try:
            issue = self.jira.issue(issue_key)
            issue.update(description=description)
            print(f"✅ Updated {issue_key} description")
        except Exception as e:
            print(f"❌ Failed to update {issue_key}: {e}")

    def create_story(self, summary: str, description: str, epic_key: str, labels=None):
        """Creates a Story under an Epic"""
        if self.dry_run:
            print(f"[DRY RUN] Would create Story: {summary} under {epic_key}")
            return None

        try:
            issue_dict = {
                'project': {'key': self.project_key},
                'summary': summary,
                'description': description,
                'issuetype': {'name': 'Story'},
                'labels': labels or []
            }

            story = self.jira.create_issue(fields=issue_dict)

            # Link to Epic
            self.jira.add_issues_to_epic(epic_key, [story.key])

            print(f"✅ Created Story: {story.key} - {summary}")
            return story
        except Exception as e:
            print(f"❌ Failed to create Story: {e}")
            return None

    def create_subtask(self, summary: str, description: str, parent_key: str,
                       priority: str = "Medium", labels=None):
        """Creates a Sub-Task under a Story"""
        if self.dry_run:
            print(f"[DRY RUN] Would create Sub-Task: {summary} under {parent_key}")
            return None

        try:
            issue_dict = {
                'project': {'key': self.project_key},
                'summary': summary,
                'description': description,
                'issuetype': {'name': 'Sub-Task'},
                'priority': {'name': priority},
                'parent': {'key': parent_key},
                'labels': labels or []
            }

            subtask = self.jira.create_issue(fields=issue_dict)
            print(f"✅ Created Sub-Task: {subtask.key} - {summary}")
            return subtask
        except Exception as e:
            print(f"❌ Failed to create Sub-Task: {e}")
            return None


def enrich_weg10_infrastructure(jira_enrichment: JiraEnrichment):
    """Enriches WEG-10 with full task structure"""

    epic_key = "WEG-10"

    # Update Epic description from Confluence
    epic_description = """
# WEG-10 – Solution Setup & Infrastructure

## Überblick

Das Modul **Solution Setup & Infrastructure** (WEG-10) bildet die technische Grundlage für die gesamte WEG-Plattform.
Es definiert die Struktur des Projekts, stellt die lokale Entwicklungsumgebung bereit und sorgt für eine einheitliche Konfigurationsvalidierung.

## Hauptfunktionen

- **Solution-Setup:** Klare Strukturierung nach Domain-Driven Design (DDD) mit Projekten für Api, Application, Domain, Infrastructure und Directory
- **Docker Compose Infrastructure:** Einheitliche Containerdefinitionen für SQL Server, Directory und Web-Client
- **Developer Onboarding:** Ausführliches README mit Installationsanleitung und Troubleshooting
- **Configuration Validation:** Validierung aller Konfigurationsparameter über das .NET Options Pattern
- **CI-Integration:** Build-Validierung, Docker-Linting und Pipeline-Setup

## Akzeptanzkriterien

✅ **Gegeben:** ein Entwickler klont das Repository
**Wenn:** er `docker compose up` mit gültigen .env-Dateien ausführt
**Dann:** starten API, SQL, Directory und Web-Client fehlerfrei

✅ **Gegeben:** eine fehlerhafte Umgebungsvariable
**Wenn:** der Dienst startet
**Dann:** wird der Startvorgang gestoppt mit verständlicher Fehlermeldung

✅ **Gegeben:** eine CI-Pipeline wird ausgelöst
**Wenn:** der Build ausgeführt wird
**Dann:** werden Compose-Dateien, ENV-Parameter und Build-Artefakte validiert

## Abhängigkeiten

- Basis für WEG-1 (Platform Foundation)
- Basis für WEG-12 (Error Handling, Logging & Health)
- Basis für WEG-14 (Testing & CI Basics)

## Verknüpfte Tasks

- WEG-100 – Solution Setup & Project Structure
- WEG-101 – Docker Compose Infrastructure
- WEG-102 – Developer Onboarding & Documentation
- WEG-103 – Configuration Validation & Options Pattern

**Confluence:** https://maierharry.atlassian.net/wiki/spaces/WEG/pages/28082893
"""

    print(f"\n{'='*60}")
    print(f"Enriching WEG-10 – Solution Setup & Infrastructure")
    print(f"{'='*60}\n")

    # Update Epic description
    jira_enrichment.update_issue_description(epic_key, epic_description)

    # Create WEG-101 – Docker Compose Infrastructure Story
    story_101 = jira_enrichment.create_story(
        summary="WEG-101 – Docker Compose Infrastructure",
        description="""
# WEG-101 – Docker Compose Infrastructure

## Ziel
Bereitstellung einer vollständigen lokalen Entwicklungsumgebung mit Docker Compose für API, SQL Server, Directory und Web-Client.

## User Story
Als Entwickler möchte ich mit einem einzigen Befehl (`docker compose up`) die gesamte Infrastruktur starten können, damit ich sofort mit der Entwicklung beginnen kann.

## Technischer Ansatz

### docker-compose.yml Structure
```yaml
version: '3.8'
services:
  sqlserver:
    image: mcr.microsoft.com/mssql/server:2022-latest
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=${SQL_SA_PASSWORD}
    ports:
      - "1433:1433"
    volumes:
      - sqldata:/var/opt/mssql

  api:
    build:
      context: .
      dockerfile: src/WegManagement.Api/Dockerfile
    ports:
      - "5000:8080"
    environment:
      - ConnectionStrings__DefaultConnection=${SQL_CONNECTION_STRING}
    depends_on:
      - sqlserver

  web:
    build:
      context: ./web
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    depends_on:
      - api
```

## Akzeptanzkriterien

✅ **Gegeben:** Docker Desktop ist installiert
**Wenn:** `docker compose up` ausgeführt wird
**Dann:** starten alle Services ohne Fehler

✅ **Gegeben:** Services laufen
**Wenn:** API-Healthcheck aufgerufen wird
**Dann:** antwortet der Endpoint mit 200 OK

✅ **Gegeben:** SQL Server Container läuft
**Wenn:** Verbindung mit SSMS getestet wird
**Dann:** ist die Verbindung erfolgreich
""",
        epic_key=epic_key,
        labels=["infrastructure", "docker", "devops"]
    )

    if story_101:
        # Create Sub-Tasks under WEG-101
        jira_enrichment.create_subtask(
            summary="Create docker-compose.yml with SQL Server, API, Web services",
            description="""
## Implementation

Create `docker-compose.yml` in repository root:

```yaml
version: '3.8'

services:
  sqlserver:
    image: mcr.microsoft.com/mssql/server:2022-latest
    container_name: weg-sqlserver
    environment:
      ACCEPT_EULA: Y
      SA_PASSWORD: \${SQL_SA_PASSWORD:-YourStrong@Passw0rd}
      MSSQL_PID: Developer
    ports:
      - "1433:1433"
    volumes:
      - sqlserver_data:/var/opt/mssql
    healthcheck:
      test: /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "\${SQL_SA_PASSWORD}" -Q "SELECT 1"
      interval: 30s
      timeout: 10s
      retries: 3

  api:
    build:
      context: .
      dockerfile: src/WegManagement.Api/Dockerfile
      target: development
    container_name: weg-api
    ports:
      - "5000:8080"
    environment:
      ASPNETCORE_ENVIRONMENT: Development
      ConnectionStrings__DefaultConnection: Server=sqlserver,1433;Database=WegManagement;User Id=sa;Password=\${SQL_SA_PASSWORD};TrustServerCertificate=True
      ConnectionStrings__DirectoryConnection: Server=sqlserver,1433;Database=WegDirectory;User Id=sa;Password=\${SQL_SA_PASSWORD};TrustServerCertificate=True
    depends_on:
      sqlserver:
        condition: service_healthy
    volumes:
      - ./src:/app/src

  web:
    build:
      context: ./web
      dockerfile: Dockerfile.dev
    container_name: weg-web
    ports:
      - "3000:3000"
    environment:
      VITE_API_URL: http://localhost:5000
    depends_on:
      - api
    volumes:
      - ./web/src:/app/src

volumes:
  sqlserver_data:
```

## Verification

```bash
# Start all services
docker compose up -d

# Check service status
docker compose ps

# View logs
docker compose logs -f api

# Stop services
docker compose down
```

## File Location
`/docker-compose.yml`
""",
            parent_key=story_101.key,
            priority="Highest",
            labels=["docker", "infrastructure"]
        )

        jira_enrichment.create_subtask(
            summary="Create Dockerfile for API (.NET 8)",
            description="""
## Implementation

Create multi-stage Dockerfile for .NET API:

`src/WegManagement.Api/Dockerfile`:

```dockerfile
# Build stage
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copy solution and project files
COPY ["WegManagement.sln", "./"]
COPY ["src/WegManagement.Api/WegManagement.Api.csproj", "src/WegManagement.Api/"]
COPY ["src/WegManagement.Application/WegManagement.Application.csproj", "src/WegManagement.Application/"]
COPY ["src/WegManagement.Domain/WegManagement.Domain.csproj", "src/WegManagement.Domain/"]
COPY ["src/WegManagement.Infrastructure/WegManagement.Infrastructure.csproj", "src/WegManagement.Infrastructure/"]
COPY ["src/WegManagement.Directory/WegManagement.Directory.csproj", "src/WegManagement.Directory/"]

# Restore dependencies
RUN dotnet restore "WegManagement.sln"

# Copy source code
COPY . .

# Build
WORKDIR "/src/src/WegManagement.Api"
RUN dotnet build "WegManagement.Api.csproj" -c Release -o /app/build

# Publish
FROM build AS publish
RUN dotnet publish "WegManagement.Api.csproj" -c Release -o /app/publish /p:UseAppHost=false

# Runtime stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app
EXPOSE 8080
EXPOSE 8081

COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "WegManagement.Api.dll"]

# Development stage (for hot reload)
FROM build AS development
WORKDIR /app/src
EXPOSE 8080
EXPOSE 8081
CMD ["dotnet", "watch", "run", "--project", "src/WegManagement.Api/WegManagement.Api.csproj", "--urls", "http://+:8080"]
```

## Verification

```bash
# Build image
docker build -t weg-api -f src/WegManagement.Api/Dockerfile .

# Run container
docker run -p 5000:8080 weg-api

# Test API
curl http://localhost:5000/health
```

## File Location
`/src/WegManagement.Api/Dockerfile`
""",
            parent_key=story_101.key,
            priority="Highest",
            labels=["docker", "backend"]
        )

        jira_enrichment.create_subtask(
            summary="Create Dockerfile for Web (Vite + React)",
            description="""
## Implementation

Create multi-stage Dockerfile for React/Vite:

`web/Dockerfile`:

```dockerfile
# Build stage
FROM node:20-alpine AS build
WORKDIR /app

# Copy package files
COPY package*.json ./
COPY yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy source
COPY . .

# Build for production
RUN yarn build

# Production stage
FROM nginx:alpine AS production
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

`web/Dockerfile.dev` (for development):

```dockerfile
FROM node:20-alpine
WORKDIR /app

# Copy package files
COPY package*.json ./
COPY yarn.lock ./

# Install dependencies
RUN yarn install

# Copy source
COPY . .

# Expose Vite dev server port
EXPOSE 3000

# Start dev server
CMD ["yarn", "dev", "--host", "0.0.0.0"]
```

`web/nginx.conf`:

```nginx
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://api:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Verification

```bash
# Build production image
docker build -t weg-web -f web/Dockerfile ./web

# Run container
docker run -p 3000:80 weg-web

# Test
curl http://localhost:3000
```

## File Locations
- `/web/Dockerfile`
- `/web/Dockerfile.dev`
- `/web/nginx.conf`
""",
            parent_key=story_101.key,
            priority="High",
            labels=["docker", "frontend"]
        )

        jira_enrichment.create_subtask(
            summary="Create .env.example with all required environment variables",
            description="""
## Implementation

Create `.env.example` in repository root:

```bash
# ===========================================
# WEG Management System - Environment Config
# ===========================================

# SQL Server Configuration
SQL_SA_PASSWORD=YourStrong@Passw0rd
SQL_CONNECTION_STRING=Server=localhost,1433;Database=WegManagement;User Id=sa;Password=YourStrong@Passw0rd;TrustServerCertificate=True
DIRECTORY_CONNECTION_STRING=Server=localhost,1433;Database=WegDirectory;User Id=sa;Password=YourStrong@Passw0rd;TrustServerCertificate=True

# API Configuration
ASPNETCORE_ENVIRONMENT=Development
ASPNETCORE_URLS=http://+:5000
JWT_SECRET=your-super-secret-jwt-key-min-32-chars-long-please-change-in-production
JWT_ISSUER=https://wegmanagement.local
JWT_AUDIENCE=https://wegmanagement.local
JWT_EXPIRY_MINUTES=60

# Frontend Configuration
VITE_API_URL=http://localhost:5000
VITE_APP_NAME=WEG Management System

# Feature Flags
ENABLE_SWAGGER=true
ENABLE_CORS=true
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173

# Logging
LOG_LEVEL=Information
ENABLE_CONSOLE_LOGGING=true
ENABLE_FILE_LOGGING=false
```

Also create `.env` from template:

```bash
cp .env.example .env
```

Add to `.gitignore`:

```
.env
.env.local
.env.*.local
```

## Verification

```bash
# Verify .env is ignored
git check-ignore .env

# Verify docker-compose can read variables
docker compose config
```

## File Locations
- `/.env.example`
- `/.env` (git-ignored)
- `/.gitignore`
""",
            parent_key=story_101.key,
            priority="Highest",
            labels=["configuration", "security"]
        )

    # Create WEG-102 – Developer Onboarding Story
    story_102 = jira_enrichment.create_story(
        summary="WEG-102 – Developer Onboarding & Documentation",
        description="""
# WEG-102 – Developer Onboarding & Documentation

## Ziel
Erstellen einer vollständigen README-Dokumentation, die neue Entwickler in unter 15 Minuten produktiv macht.

## User Story
Als neuer Entwickler möchte ich eine klare Schritt-für-Schritt-Anleitung haben, damit ich das Projekt lokal aufsetzen und starten kann.

## Technischer Ansatz

### README.md Struktur
1. **Projektübersicht** - Was ist WEG Management System?
2. **Voraussetzungen** - Required tools and versions
3. **Quick Start** - 5 Befehle zum Starten
4. **Projektstruktur** - Ordnerhierarchie erklärt
5. **Entwicklung** - Commands, Workflows, Best Practices
6. **Troubleshooting** - Häufige Probleme und Lösungen
7. **Weitere Ressourcen** - Links zu Confluence, JIRA, ADRs

## Akzeptanzkriterien

✅ **Gegeben:** ein neuer Entwickler folgt der README
**Wenn:** er alle Schritte ausführt
**Dann:** kann er die Anwendung in unter 15 Minuten starten

✅ **Gegeben:** ein Problem tritt auf
**Wenn:** der Entwickler die Troubleshooting-Sektion konsultiert
**Dann:** findet er die Lösung oder einen Hinweis zum nächsten Schritt

✅ **Gegeben:** die Projektstruktur wird geändert
**Wenn:** neue Ordner/Module hinzugefügt werden
**Dann:** wird die README entsprechend aktualisiert
""",
        epic_key=epic_key,
        labels=["documentation", "onboarding"]
    )

    if story_102:
        jira_enrichment.create_subtask(
            summary="Create comprehensive README.md with Quick Start",
            description="""
## Implementation

Create `/README.md`:

```markdown
# WEG Management System

Vollständiges Property Management System für deutsche Wohnungseigentümergemeinschaften (WEG).

## 🚀 Quick Start

### Voraussetzungen
- Docker Desktop 4.20+
- .NET SDK 8.0+ (optional für lokale Entwicklung)
- Node.js 20+ (optional für lokale Entwicklung)

### In 5 Schritten starten

1. **Repository klonen**
   ```bash
   git clone https://github.com/8chM/MyRep.git
   cd MyRep
   ```

2. **Umgebungsvariablen einrichten**
   ```bash
   cp .env.example .env
   # Bearbeite .env bei Bedarf
   ```

3. **Docker Container starten**
   ```bash
   docker compose up -d
   ```

4. **Datenbank migrieren**
   ```bash
   docker compose exec api dotnet ef database update
   ```

5. **Öffne die Anwendung**
   - Frontend: http://localhost:3000
   - API: http://localhost:5000
   - Swagger: http://localhost:5000/swagger

## 📁 Projektstruktur

```
MyRep/
├── src/
│   ├── WegManagement.Api/          # REST API (ASP.NET Core)
│   ├── WegManagement.Application/  # Use Cases, CQRS Commands/Queries
│   ├── WegManagement.Domain/       # Domain Entities, Value Objects
│   ├── WegManagement.Infrastructure/# EF Core, Repositories
│   └── WegManagement.Directory/    # Multi-Tenant Control Plane
├── web/                            # React/Vite Frontend
├── tests/                          # Unit & Integration Tests
├── docker-compose.yml              # Local Development Stack
└── README.md
```

## 🛠️ Entwicklung

### Backend (.NET)
```bash
# Restore packages
dotnet restore

# Build
dotnet build

# Run tests
dotnet test

# Run API locally (without Docker)
cd src/WegManagement.Api
dotnet run
```

### Frontend (React)
```bash
cd web

# Install dependencies
yarn install

# Start dev server
yarn dev

# Build for production
yarn build

# Run tests
yarn test
```

### Datenbank Migrationen
```bash
# Create new migration
dotnet ef migrations add MigrationName -p src/WegManagement.Infrastructure -s src/WegManagement.Api

# Apply migrations
dotnet ef database update -p src/WegManagement.Infrastructure -s src/WegManagement.Api

# Rollback last migration
dotnet ef database update PreviousMigrationName -p src/WegManagement.Infrastructure -s src/WegManagement.Api
```

## 🐛 Troubleshooting

### Port bereits belegt (1433, 5000, 3000)
```bash
# Finde Prozesse
lsof -i :1433
lsof -i :5000
lsof -i :3000

# Beende Prozesse oder ändere Ports in docker-compose.yml
```

### SQL Server Container startet nicht
```bash
# Überprüfe Logs
docker compose logs sqlserver

# Häufige Ursache: SA_PASSWORD zu schwach
# Setze in .env: SQL_SA_PASSWORD=YourStrong@Passw0rd123
```

### API antwortet mit 500
```bash
# Überprüfe Logs
docker compose logs api

# Überprüfe Connection String
docker compose exec api env | grep ConnectionStrings

# Migrationen anwenden
docker compose exec api dotnet ef database update
```

## 📚 Weitere Ressourcen

- **JIRA Project:** https://maierharry.atlassian.net/browse/WEG
- **Confluence:** https://maierharry.atlassian.net/wiki/spaces/WEG
- **API Docs:** http://localhost:5000/swagger (when running)

## 📄 Lizenz

Intern - Nicht für öffentliche Nutzung
```

## File Location
`/README.md`
""",
            parent_key=story_102.key,
            priority="Highest",
            labels=["documentation"]
        )

    # Create WEG-103 – Configuration Validation Story
    story_103 = jira_enrichment.create_story(
        summary="WEG-103 – Configuration Validation & Options Pattern",
        description="""
# WEG-103 – Configuration Validation & Options Pattern

## Ziel
Implementierung des .NET Options Pattern mit FluentValidation für fail-fast Konfigurationsvalidierung beim Startup.

## User Story
Als Entwickler möchte ich sofort beim Start informiert werden, wenn Konfigurationswerte fehlen oder ungültig sind, damit ich keine Zeit mit schwer zu debuggenden Runtime-Fehlern verschwende.

## Technischer Ansatz

### Options Pattern Classes
```csharp
public class DatabaseOptions
{
    public string DefaultConnection { get; set; }
    public string DirectoryConnection { get; set; }
    public int CommandTimeout { get; set; } = 30;
}

public class JwtOptions
{
    public string Secret { get; set; }
    public string Issuer { get; set; }
    public string Audience { get; set; }
    public int ExpiryMinutes { get; set; } = 60;
}
```

### Validation with FluentValidation
```csharp
public class DatabaseOptionsValidator : AbstractValidator<DatabaseOptions>
{
    public DatabaseOptionsValidator()
    {
        RuleFor(x => x.DefaultConnection)
            .NotEmpty()
            .Must(BeValidConnectionString);

        RuleFor(x => x.CommandTimeout)
            .GreaterThan(0)
            .LessThanOrEqualTo(300);
    }
}
```

## Akzeptanzkriterien

✅ **Gegeben:** eine erforderliche ENV-Variable fehlt
**Wenn:** die API startet
**Dann:** wird der Start abgebrochen mit klarer Fehlermeldung

✅ **Gegeben:** ein Connection String ist ungültig
**Wenn:** die Validierung läuft
**Dann:** wird der Fehler geloggt und der Start abgebrochen

✅ **Gegeben:** alle Konfigurationen sind gültig
**Wenn:** die API startet
**Dann:** wird ein Success-Log ausgegeben
""",
        epic_key=epic_key,
        labels=["backend", "configuration", "validation"]
    )

    if story_103:
        jira_enrichment.create_subtask(
            summary="Implement Options Pattern classes for all configurations",
            description="""
## Implementation

Create options classes in `src/WegManagement.Infrastructure/Configuration/`:

**DatabaseOptions.cs:**
```csharp
namespace WegManagement.Infrastructure.Configuration;

public class DatabaseOptions
{
    public const string SectionName = "ConnectionStrings";

    public string DefaultConnection { get; set; } = string.Empty;
    public string DirectoryConnection { get; set; } = string.Empty;
    public int CommandTimeout { get; set; } = 30;
    public int MaxRetryCount { get; set; } = 3;
    public bool EnableSensitiveDataLogging { get; set; } = false;
}
```

**JwtOptions.cs:**
```csharp
namespace WegManagement.Infrastructure.Configuration;

public class JwtOptions
{
    public const string SectionName = "Jwt";

    public string Secret { get; set; } = string.Empty;
    public string Issuer { get; set; } = string.Empty;
    public string Audience { get; set; } = string.Empty;
    public int ExpiryMinutes { get; set; } = 60;
}
```

**CorsOptions.cs:**
```csharp
namespace WegManagement.Infrastructure.Configuration;

public class CorsOptions
{
    public const string SectionName = "Cors";

    public bool Enabled { get; set; } = true;
    public string[] AllowedOrigins { get; set; } = Array.Empty<string>();
    public bool AllowCredentials { get; set; } = true;
}
```

## Verification

All option classes should:
- Have a `SectionName` constant
- Use non-nullable reference types with defaults
- Be in `WegManagement.Infrastructure.Configuration` namespace

## File Locations
- `/src/WegManagement.Infrastructure/Configuration/DatabaseOptions.cs`
- `/src/WegManagement.Infrastructure/Configuration/JwtOptions.cs`
- `/src/WegManagement.Infrastructure/Configuration/CorsOptions.cs`
""",
            parent_key=story_103.key,
            priority="Highest",
            labels=["backend", "configuration"]
        )

        jira_enrichment.create_subtask(
            summary="Add FluentValidation validators for all Options classes",
            description="""
## Implementation

Install FluentValidation:
```bash
dotnet add src/WegManagement.Infrastructure package FluentValidation
dotnet add src/WegManagement.Infrastructure package FluentValidation.DependencyInjectionExtensions
```

Create validators in `src/WegManagement.Infrastructure/Configuration/Validators/`:

**DatabaseOptionsValidator.cs:**
```csharp
using FluentValidation;

namespace WegManagement.Infrastructure.Configuration.Validators;

public class DatabaseOptionsValidator : AbstractValidator<DatabaseOptions>
{
    public DatabaseOptionsValidator()
    {
        RuleFor(x => x.DefaultConnection)
            .NotEmpty()
            .WithMessage("DefaultConnection is required")
            .Must(BeValidConnectionString)
            .WithMessage("DefaultConnection must be a valid SQL Server connection string");

        RuleFor(x => x.DirectoryConnection)
            .NotEmpty()
            .WithMessage("DirectoryConnection is required")
            .Must(BeValidConnectionString)
            .WithMessage("DirectoryConnection must be a valid SQL Server connection string");

        RuleFor(x => x.CommandTimeout)
            .GreaterThan(0)
            .LessThanOrEqualTo(300)
            .WithMessage("CommandTimeout must be between 1 and 300 seconds");

        RuleFor(x => x.MaxRetryCount)
            .GreaterThanOrEqualTo(0)
            .LessThanOrEqualTo(10)
            .WithMessage("MaxRetryCount must be between 0 and 10");
    }

    private bool BeValidConnectionString(string connectionString)
    {
        if (string.IsNullOrWhiteSpace(connectionString))
            return false;

        try
        {
            var builder = new Microsoft.Data.SqlClient.SqlConnectionStringBuilder(connectionString);
            return !string.IsNullOrEmpty(builder.DataSource);
        }
        catch
        {
            return false;
        }
    }
}
```

**JwtOptionsValidator.cs:**
```csharp
using FluentValidation;

namespace WegManagement.Infrastructure.Configuration.Validators;

public class JwtOptionsValidator : AbstractValidator<JwtOptions>
{
    public JwtOptionsValidator()
    {
        RuleFor(x => x.Secret)
            .NotEmpty()
            .WithMessage("JWT Secret is required")
            .MinimumLength(32)
            .WithMessage("JWT Secret must be at least 32 characters for security");

        RuleFor(x => x.Issuer)
            .NotEmpty()
            .WithMessage("JWT Issuer is required")
            .Must(BeValidUrl)
            .WithMessage("JWT Issuer must be a valid URL");

        RuleFor(x => x.Audience)
            .NotEmpty()
            .WithMessage("JWT Audience is required");

        RuleFor(x => x.ExpiryMinutes)
            .GreaterThan(0)
            .LessThanOrEqualTo(1440) // Max 24 hours
            .WithMessage("JWT ExpiryMinutes must be between 1 and 1440 (24 hours)");
    }

    private bool BeValidUrl(string url)
    {
        return Uri.TryCreate(url, UriKind.Absolute, out _);
    }
}
```

## File Locations
- `/src/WegManagement.Infrastructure/Configuration/Validators/DatabaseOptionsValidator.cs`
- `/src/WegManagement.Infrastructure/Configuration/Validators/JwtOptionsValidator.cs`
- `/src/WegManagement.Infrastructure/Configuration/Validators/CorsOptionsValidator.cs`
""",
            parent_key=story_103.key,
            priority="High",
            labels=["backend", "validation"]
        )

    print(f"\n✅ WEG-10 enrichment completed!\n")


def main():
    """Main execution"""
    import argparse

    parser = argparse.ArgumentParser(description='Enrich JIRA issues with detailed content')
    parser.add_argument('--dry-run', action='store_true', help='Simulate without making changes')
    parser.add_argument('--module', type=str, default='weg10',
                       help='Module to enrich (weg10, weg13, weg30, all)')

    args = parser.parse_args()

    try:
        jira = JiraEnrichment(dry_run=args.dry_run)

        if args.module in ['weg10', 'all']:
            enrich_weg10_infrastructure(jira)

        print("\n" + "="*60)
        print("✅ JIRA Enrichment Complete!")
        print("="*60)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
