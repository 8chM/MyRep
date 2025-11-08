# 🤖 Best Practices für Autonome Claude Code Agenten

**Ziel:** Maximale Autonomie und Erfolgsrate für KI-Agenten

---

## 🎯 Kernprinzipien

### 1. **Context First - Autonomie Second**

```
❌ SCHLECHT:
"Erstelle Epic für WEG-1"

✅ GUT:
"Lies ALLE Confluence-Dokumente (Liste bereitgestellt),
extrahiere Domain-Modell, API-Specs, Abhängigkeiten,
erstelle Epic nach Template XYZ, veröffentliche in JIRA,
verifiziere Ergebnis."
```

**Regel:** Gib dem Agenten ALLE Informationen vorab, nicht schrittweise.

### 2. **Explizite Workflows statt Annahmen**

```
❌ SCHLECHT:
"Implementiere Feature X"

✅ GUT:
"1. Lies File Y
 2. Extrahiere Requirements aus Zeile 10-50
 3. Generiere Code nach Template Z
 4. Schreibe in /path/to/file.cs
 5. Führe 'dotnet build' aus
 6. Bei Fehler: Fixe und retry
 7. Committe mit Message 'WEG-XXX: Description'"
```

**Regel:** Jeder Schritt nummeriert, explizit, verifizie

rbar.

### 3. **Verification in jeden Workflow einbauen**

```python
# Nach jeder wichtigen Aktion
def verify_epic_created(epic_key):
    epic = jira.issue(epic_key)
    checks = {
        'exists': epic.key == epic_key,
        'has_description': len(epic.fields.description) > 1000,
        'has_labels': len(epic.fields.labels) > 0
    }
    assert all(checks.values()), f"Verification failed: {checks}"
```

**Regel:** Agent muss selbst prüfen, nicht User.

---

## 📋 Prompt-Struktur für Autonomie

### Template: Autonomer Agent Prompt

```markdown
# [Agent-Typ] - [Aufgabe]

## 🎯 Your Role
[Klar definierte Rolle: Was ist deine Spezialisierung?]

## 📋 Current Task
[Exakte Aufgabe mit Kontext]

## 📖 Source Data

### Data Source 1
[Vollständige Daten oder Pfad zum Laden]

### Data Source 2
[Weitere Daten...]

## 🛠️ Step-by-Step Workflow

### Step 1: [Action]
[Exakte Anweisung was zu tun ist]

**Code:**
```bash
# Executable command
cat /path/to/file.md
```

**Expected Output:**
[Was sollte rauskommen]

### Step 2: [Next Action]
...

## 📏 Quality Checklist

- [ ] Checkpoint 1
- [ ] Checkpoint 2
- [ ] ...

## 🎯 Success Criteria

[Woran erkennst du dass du erfolgreich warst?]

## 🚀 Execution Instructions

**Du bist ein autonomer Agent. Arbeite VOLLSTÄNDIG eigenständig:**
1. ✅ [Aktion 1]
2. ✅ [Aktion 2]
...

**Keine Rückfragen, keine Pausen, keine manuellen Schritte.**

**Start NOW!**
```

---

## 🔧 Technische Best Practices

### 1. **File Paths: Immer absolut**

```python
# ❌ Relativ - Agent könnte im falschen Directory sein
with open('config.json', 'r') as f:
    config = json.load(f)

# ✅ Absolut - Immer eindeutig
with open('/home/user/MyRep/config.json', 'r') as f:
    config = json.load(f)
```

### 2. **Error Handling: Retry-Logic einbauen**

```python
# ❌ Kein Error Handling
jira.create_issue(...)

# ✅ Mit Retry
max_retries = 3
for attempt in range(max_retries):
    try:
        jira.create_issue(...)
        break
    except Exception as e:
        if attempt == max_retries - 1:
            raise
        print(f"Retry {attempt + 1}/{max_retries}: {e}")
        time.sleep(2 ** attempt)
```

### 3. **Credentials: Aus Environment laden**

```python
# ❌ Hardcoded
jira = JIRA('https://domain.atlassian.net', basic_auth=('user', 'token123'))

# ✅ Environment
from dotenv import load_dotenv
load_dotenv('.env.jira.example')

jira = JIRA(
    server=os.getenv('JIRA_BASE_URL'),
    basic_auth=(os.getenv('JIRA_USERNAME'), os.getenv('JIRA_API_TOKEN'))
)
```

### 4. **Logging: Progress sichtbar machen**

```python
print("🔍 Phase 1: Reading Confluence documents...")
for doc in docs:
    print(f"   📄 Loading {doc}...")
    content = load_doc(doc)
    print(f"   ✅ Loaded {len(content)} chars")

print("\n📝 Phase 2: Creating Epic...")
epic = create_epic(...)
print(f"✅ Epic created: {epic.key}")

print("\n🔍 Phase 3: Verification...")
verify(epic)
print("✅ All checks passed!")
```

---

## 🎓 Prompt-Optimierungen für Claude Code

### 1. **Template-Referenzen: Konkrete Pfade**

```markdown
❌ VAGUE:
"Nutze das Epic-Template"

✅ SPEZIFISCH:
"Nutze das Epic-Template aus Datei:
/home/user/MyRep/JIRA_Templates_for_KI_Agents.md

Lade es mit:
```bash
cat /home/user/MyRep/JIRA_Templates_for_KI_Agents.md | grep -A 300 "# Epic Template"
```

Das Template beginnt mit '# Epic Template' und endet vor '# Story Template'."
```

### 2. **Code-Beispiele: Vollständig, nicht Pseudo**

```markdown
❌ PSEUDO-CODE:
```csharp
public class Entity
{
    // TODO: Add properties
}
```

✅ VOLLSTÄNDIG:
```csharp
namespace WegManagement.Domain.Entities;

public class Association : BaseEntity
{
    public Guid Id { get; private set; }
    public string Name { get; private set; }
    public string Description { get; private set; }

    private Association() { }

    public static Association Create(string name, string description)
    {
        if (string.IsNullOrWhiteSpace(name))
            throw new ArgumentException("Name required", nameof(name));

        return new Association
        {
            Id = Guid.NewGuid(),
            Name = name.Trim(),
            Description = description?.Trim() ?? string.Empty,
            CreatedAt = DateTime.UtcNow
        };
    }
}
```
```

### 3. **Verification: Testbare Kriterien**

```markdown
❌ VAGE:
"Stelle sicher dass das Epic gut ist"

✅ TESTBAR:
"Verifiziere:
- ✅ Epic.key == 'WEG-1'
- ✅ Epic.fields.description.length > 1000
- ✅ Epic.fields.description contains 'Domain Model'
- ✅ Epic.fields.description contains 'Akzeptanzkriterien'
- ✅ Epic.fields.labels includes 'epic'
- ✅ Epic.fields.issuetype.name == 'Epic'"
```

---

## 🔄 Information Flow zwischen Agenten

### Problem: Kontext-Verlust

```
Epic Agent erstellt Epic
  ↓ (KONTEXT VERLUST!)
Story Agent hat nur Epic-Key, muss alles neu recherchieren
  ↓ (KONTEXT VERLUST!)
Task Agent hat nur Story-Key, muss alles neu recherchieren
```

### Lösung: Kontext-Kette

```markdown
# Epic Agent Output
Epic WEG-1 erstellt mit:
- Domain Model: BaseEntity, AggregateRoot
- API Pattern: BaseApiController, Result<T>
- DB Pattern: Schema-per-Tenant
- Tech Stack: .NET 8, EF Core, React 18
- Submodules: WEG-10 bis WEG-19

→ Diese Infos sind IN der Epic-Description!

# Story Agent Input
"Lies Epic WEG-1 Description komplett.
 Du findest dort: Domain Model, API Pattern, DB Pattern.
 Nutze diese Basis für alle Stories."

→ Story enthält Epic-Kontext + Story-spezifisches

# Task Agent Input
"Lies Story WEG-XX komplett.
 Lies auch Parent Epic WEG-1 für Architektur-Kontext.
 Nutze beide für Task-Details."

→ Task hat VOLLEN Kontext: Epic + Story + Task-Details
```

**Regel:** Jede Ebene reichert Kontext an, löscht nichts.

---

## 📊 Metriken für erfolgreiche Agenten

### 1. **First-Time Success Rate**

```python
# Wie oft funktioniert Agent ohne Retry?
success_rate = successful_runs / total_runs

# Ziel: >90%
```

### 2. **Context Completeness**

```python
# Hat Agent alle Infos zum Arbeiten?
def check_context_complete(prompt):
    required = [
        'source_data',
        'step_by_step_workflow',
        'verification_steps',
        'success_criteria'
    ]
    return all(req in prompt.lower() for req in required)
```

### 3. **Autonomy Level**

```python
# Wie viele User-Interventions?
autonomy = 1 - (user_interventions / total_steps)

# Ziel: >95% (max 1 Intervention pro 20 Steps)
```

---

## 🎯 Agent-spezifische Best Practices

### Epic Writer Agent

```markdown
✅ Muss tun:
- Alle Confluence-Docs lesen (nicht nur eins!)
- Domain Model komplett definieren
- Alle Untermodule auflisten
- Dependencies klar machen
- Template exakt nutzen

❌ Nicht tun:
- "Ich erstelle jetzt ein Epic" ohne Research
- Vage Beschreibungen
- Pseudo-Code statt echtem Code
- Template ignorieren
```

### Story Writer Agent

```markdown
✅ Muss tun:
- Epic komplett lesen
- BDD Acceptance Criteria (Given-When-Then)
- Technischen Ansatz mit Code-Beispielen
- Sub-Tasks auflisten
- Links zu Epic setzen

❌ Nicht tun:
- Story ohne Epic-Kontext
- Acceptance Criteria ohne "Given-When-Then"
- Sub-Tasks vergessen
```

### Task Writer Agent

```markdown
✅ Muss tun:
- Story UND Epic lesen
- VOLLSTÄNDIGEN Code schreiben (copy-pasteable!)
- Exakte File-Pfade angeben
- Verification Commands
- Kann in 2-4h implementiert werden

❌ Nicht tun:
- TODO-Comments im Code
- Pseudo-Code
- Relative Pfade
- "Implementiere XYZ" ohne Code
```

---

## 🚀 Checkliste: Ist mein Prompt Agent-ready?

```markdown
Vor dem Starten, prüfe:

[ ] Alle erforderlichen Daten im Prompt enthalten?
[ ] Workflow ist Schritt-für-Schritt nummeriert?
[ ] Jeder Schritt hat executable Command?
[ ] Expected Output definiert?
[ ] Verification Steps enthalten?
[ ] Success Criteria klar?
[ ] Template-Pfade absolut?
[ ] Error Handling erwähnt?
[ ] "Start NOW!" am Ende?
[ ] Agent wird als autonom bezeichnet?
```

---

## 💡 Beispiel: Vorher/Nachher

### ❌ Schlecht (nicht autonom)

```markdown
Bitte erstelle Epic für WEG-1.
```

**Problem:** Agent muss raten:
- Wo sind die Infos?
- Welches Template?
- Wie veröffentlichen?
- Was ist Erfolg?

### ✅ Gut (vollständig autonom)

```markdown
# Epic Writer Agent - WEG-1

## Phase 1: Research
1. Lies /home/user/MyRep/confluence_export/WEG-1-Platform-Foundation.md
2. Extrahiere: Domain Model, API Endpoints, DB Schema
3. Lies WEG-10 bis WEG-19 Confluence-Docs
4. Notiere alle Submodules

## Phase 2: Epic Creation
1. Lade Template: cat /home/user/MyRep/JIRA_Templates_for_KI_Agents.md | grep -A 300 "# Epic Template"
2. Fülle Template mit Research-Daten
3. Domain Model: Nutze BaseEntity pattern
4. API Endpoints: Definiere REST conventions
5. Acceptance Criteria: BDD Given-When-Then Format

## Phase 3: JIRA Publishing
```python
from jira_automation_example import WegJiraAutomation
jira = WegJiraAutomation()
epic = jira.create_epic(
    summary="WEG-1 – Platform Foundation",
    description='''[TEMPLATE-BASIERTER CONTENT]''',
    labels=['platform', 'epic']
)
```

## Phase 4: Verification
- [ ] Epic.key == 'WEG-1'
- [ ] Description > 1000 chars
- [ ] Contains Domain Model
- [ ] Lists all Submodules WEG-10 to WEG-19

Success = All checks ✅

**Start NOW - Work autonomously!**
```

**Ergebnis:** Agent kann ohne Rückfragen arbeiten.

---

## 🎉 Zusammenfassung

### Die 10 Gebote für autonome Agenten:

1. **Context First** - Alle Daten vorab im Prompt
2. **Explicit Workflows** - Nummerierte Schritte
3. **Verification Built-in** - Agent prüft selbst
4. **Absolute Paths** - Nie relativ
5. **Complete Code** - Nicht TODO oder Pseudo
6. **Error Handling** - Retry-Logic einbauen
7. **Clear Success Criteria** - Was ist "done"?
8. **Template References** - Konkrete Pfade
9. **Progress Logging** - User sieht Fortschritt
10. **"Start NOW!"** - Trigger für Autonomie

**Befolge diese Regeln → 95%+ Erfolgsrate** 🚀
