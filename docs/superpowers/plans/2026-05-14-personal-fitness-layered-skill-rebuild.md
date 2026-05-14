# Personal Fitness Layered Skill Rebuild Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the repository into a layered fitness-coach skill workspace with profile templates, modular engines, reference docs, examples, and exercise-database-backed image lookup.

**Architecture:** Replace the single-file skill with a root orchestrator `SKILL.md` that delegates to focused markdown engine files. Store durable user state in profile templates, keep domain guidance in references, add examples for actual usage, and add Python scripts that initialize and query a local exercise database compatible with the Kaiji-Z repository pattern.

**Tech Stack:** Markdown skill files, Python 3 scripts, local JSON/image exercise database, git

---

### Task 1: Rewrite the root skill as orchestrator

**Files:**
- Modify: `SKILL.md`
- Modify: `docs/superpowers/plans/2026-05-14-personal-fitness-layered-skill-rebuild.md`
- Test: `SKILL.md`

- [ ] **Step 1: Write the failing test**

Use this review checklist against the current `SKILL.md`:

```markdown
- The file must delegate to sub-files instead of containing all rules inline.
- The file must mention `profiles/`, `skills/`, `references/`, and `examples/`.
- The file must define the top-level workflow: memory -> intake -> safety -> segmentation -> plan -> optional exercise lookup -> memory update.
- The file must define degraded behavior when the exercise database is missing.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `grep -n "profiles/\|skills/\|references/\|examples/\|exercise database" SKILL.md`
Expected: missing or incomplete matches because the current file is still a monolithic skeleton.

- [ ] **Step 3: Write minimal implementation**

Replace `SKILL.md` with a concise orchestrator that includes:

```md
---
name: personal-fitness-coach
description: Use when running a layered fitness, nutrition, fat-loss, and habit-tracking coaching workflow with markdown memory, modular engines, and optional exercise-image lookup from a local exercise database.
---

# Personal Fitness Coach

## Role
You are a structured health coach that uses the files in this repository as a layered workspace.

## Repository Layers
- `profiles/`: long-term and short-term user memory templates
- `skills/`: decision engines and workflow modules
- `references/`: domain rules and style guides
- `coach_profiles/`: named coach-method profiles used for matching and mixing
- `examples/`: example interactions and memory updates
- `scripts/`: exercise database setup and query tools

## Top-Level Workflow
1. Read or initialize `profiles/` memory.
2. Use `skills/intake-engine.md` to collect missing facts.
3. Determine whether the user wants a specific coach or mixed-coach mode.
4. Use `references/coach-style-guide.md` and `coach_profiles/*.md` to choose styles.
5. Use `skills/safety-gate.md` before giving a detailed plan.
6. Use `references/segmentation-rules.md` to classify the user.
7. Use `skills/calorie-engine.md`, `skills/nutrition-engine.md`, and `skills/training-engine.md` to generate the plan.
8. If the user asks about an exercise, use `skills/exercise-engine.md` and the scripts in `scripts/`.
9. If the exercise database is unavailable, give text-only guidance and explain how to initialize it.
10. Use `skills/memory-engine.md` and `skills/adjustment-engine.md` to update or refine recommendations.
```

This task should also keep the rebuild plan aligned with the coach-selection extension by including `coach_profiles/` in the repository structure and coach-selection integration in the root workflow.

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "profiles/\|skills/\|references/\|examples/\|exercise database" SKILL.md`
Expected: matches for all repository layers and degraded exercise-db behavior.

- [ ] **Step 5: Commit**

```bash
git add SKILL.md
git commit -m "refactor: turn root skill into layered orchestrator"
```

### Task 2: Add profile templates for markdown memory

**Files:**
- Create: `profiles/EXAMPLE-HEALTH-PROFILE.md`
- Create: `profiles/EXAMPLE-HEALTH-PROGRESS.md`
- Test: `profiles/EXAMPLE-HEALTH-PROFILE.md`
- Test: `profiles/EXAMPLE-HEALTH-PROGRESS.md`

- [ ] **Step 1: Write the failing test**

Use this expected structure:

```markdown
Health profile must contain:
- frontmatter with `type: health-profile`
- sections for base stats, goals, activity habits, training preferences, nutrition preferences, adherence traits, risk boundaries, effective strategies, ineffective strategies

Health progress must contain:
- frontmatter with `type: health-progress`
- sections for recent status, recent execution, current blockers, recent strategy changes, consider next time
```

- [ ] **Step 2: Run test to verify it fails**

Run: `test -f profiles/EXAMPLE-HEALTH-PROFILE.md && test -f profiles/EXAMPLE-HEALTH-PROGRESS.md`
Expected: FAIL because the files do not exist yet.

- [ ] **Step 3: Write minimal implementation**

Create `profiles/EXAMPLE-HEALTH-PROFILE.md` with:

```md
---
type: health-profile
user_id: example-user
updated_at: YYYY-MM-DD
---

# Base Stats
# Main Goals
# Activity Habits
# Training Preferences
# Nutrition Preferences
# Adherence Traits
# Risk Boundaries
# Effective Strategies
# Ineffective Strategies
```

Create `profiles/EXAMPLE-HEALTH-PROGRESS.md` with:

```md
---
type: health-progress
user_id: example-user
updated_at: YYYY-MM-DD
---

# Recent Status
# Recent Execution
# Current Blockers
# Recent Strategy Changes
# Consider Next Time
```

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "type: health-profile\|# Base Stats\|# Main Goals" profiles/EXAMPLE-HEALTH-PROFILE.md && grep -n "type: health-progress\|# Recent Status\|# Consider Next Time" profiles/EXAMPLE-HEALTH-PROGRESS.md`
Expected: PASS with matching lines from both templates.

- [ ] **Step 5: Commit**

```bash
git add profiles/EXAMPLE-HEALTH-PROFILE.md profiles/EXAMPLE-HEALTH-PROGRESS.md
git commit -m "feat: add markdown memory profile templates"
```

### Task 3: Add engine modules under skills/

**Files:**
- Create: `skills/intake-engine.md`
- Create: `skills/safety-gate.md`
- Create: `skills/calorie-engine.md`
- Create: `skills/nutrition-engine.md`
- Create: `skills/training-engine.md`
- Create: `skills/exercise-engine.md`
- Create: `skills/memory-engine.md`
- Create: `skills/adjustment-engine.md`
- Test: `skills/`

- [ ] **Step 1: Write the failing test**

Use this module checklist:

```markdown
Each engine file must define one clear responsibility.
- intake-engine.md: quick vs coach mode, required fields, missing-field behavior
- safety-gate.md: low/caution/out-of-scope routing
- calorie-engine.md: Mifflin-St Jeor and conservative deficit rules
- nutrition-engine.md: foundation-first, carb cycling eligibility, anti-inflammatory positioning
- training-engine.md: sedentary beginner / general fat loss / experienced defaults
- exercise-engine.md: database detection, query behavior, image-path return, graceful fallback
- memory-engine.md: read, write, append/overwrite/summarize
- adjustment-engine.md: plateau, travel, low-sleep, interruption recovery
```

- [ ] **Step 2: Run test to verify it fails**

Run: `test -f skills/intake-engine.md && test -f skills/safety-gate.md && test -f skills/calorie-engine.md && test -f skills/nutrition-engine.md && test -f skills/training-engine.md && test -f skills/exercise-engine.md && test -f skills/memory-engine.md && test -f skills/adjustment-engine.md`
Expected: FAIL because the files do not exist yet.

- [ ] **Step 3: Write minimal implementation**

Create these files with focused headings and rules:

```md
# intake-engine.md
## Modes
### Quick Mode
### Coach Mode
## Required Fields
## Missing Data Rule
```

```md
# safety-gate.md
## Screening Triggers
## Risk Levels
## Response Rules
```

```md
# calorie-engine.md
## Inputs
## Formula
## Output Range Rules
## Safety Limits
```

```md
# nutrition-engine.md
## Foundation First
## Carb Cycling Eligibility
## Anti-Inflammatory Eating Rules
## Eating-Out Fallbacks
```

```md
# training-engine.md
## Priorities
## Beginner Defaults
## Fat-Loss Defaults
## Experienced Defaults
```

```md
# exercise-engine.md
## When To Use
## Database Detection
## Query Flow
## Image Path Output
## Missing Database Fallback
```

```md
# memory-engine.md
## Files Used
## Read Rules
## Write Rules
## Update Actions
```

```md
# adjustment-engine.md
## Plateau Handling
## Travel And Overtime
## Poor Sleep And Stress
## Comeback After Breaks
```

Expand each file with the concrete fitness-domain rules already agreed in the design.

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "Quick Mode\|Coach Mode" skills/intake-engine.md && grep -n "Risk Levels" skills/safety-gate.md && grep -n "Mifflin-St Jeor" skills/calorie-engine.md && grep -n "Carb Cycling Eligibility" skills/nutrition-engine.md && grep -n "Beginner Defaults" skills/training-engine.md && grep -n "Image Path Output" skills/exercise-engine.md && grep -n "Update Actions" skills/memory-engine.md && grep -n "Comeback After Breaks" skills/adjustment-engine.md`
Expected: PASS with matches from all engine files.

- [ ] **Step 5: Commit**

```bash
git add skills/
git commit -m "feat: add layered coaching engine modules"
```

### Task 4: Add references and example interaction files

**Files:**
- Create: `references/coach-style-guide.md`
- Create: `references/intake-fields.md`
- Create: `references/segmentation-rules.md`
- Create: `references/nutrition-playbook.md`
- Create: `references/training-playbook.md`
- Create: `references/exercise-db-setup.md`
- Create: `references/memory-schema.md`
- Create: `examples/quick-mode-example.md`
- Create: `examples/coach-mode-example.md`
- Create: `examples/memory-update-example.md`
- Test: `references/`
- Test: `examples/`

- [ ] **Step 1: Write the failing test**

Use this review checklist:

```markdown
References must separate stable background knowledge from engine instructions.
Examples must show actual output shapes for quick mode, coach mode, and memory updates.
exercise-db-setup.md must document how to initialize and verify the exercise database.
coach-style-guide.md must treat coach personas as style overlays, not safety overrides.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `test -f references/coach-style-guide.md && test -f references/exercise-db-setup.md && test -f examples/quick-mode-example.md`
Expected: FAIL because the files do not exist yet.

- [ ] **Step 3: Write minimal implementation**

Create the references with concrete headings:

```md
# coach-style-guide.md
## Core Rule
Coach style changes tone and emphasis, never safety boundaries.
## Suggested Coach Styles
- evidence-first
- bodybuilding bias
- fat-loss simplifier
- gentle beginner coach
```

```md
# exercise-db-setup.md
## Expected Directory
## Setup Command
## Verification Commands
## Missing Database Behavior
```

Create examples that show:
- quick mode summary output
- coach mode layered output
- memory update note that writes to both profile and progress files when appropriate

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "Coach style changes tone" references/coach-style-guide.md && grep -n "Setup Command" references/exercise-db-setup.md && grep -n "Layer 1\|Layer 2\|Layer 3" examples/coach-mode-example.md`
Expected: PASS with matching lines from references and examples.

- [ ] **Step 5: Commit**

```bash
git add references/ examples/
git commit -m "docs: add reference guides and usage examples"
```

### Task 5: Add exercise database setup and query scripts

**Files:**
- Create: `scripts/setup_exercise_db.py`
- Create: `scripts/query_exercises.py`
- Modify: `references/exercise-db-setup.md`
- Test: `scripts/setup_exercise_db.py`
- Test: `scripts/query_exercises.py`

- [ ] **Step 1: Write the failing test**

Use these expected behaviors:

```python
# setup_exercise_db.py should:
# - create scripts-compatible database directory metadata
# - support --check-db
# - print clear next steps if database missing

# query_exercises.py should:
# - support --check-db
# - support filtering by muscle and equipment
# - support fetching one exercise by id
# - print image paths when present
# - degrade gracefully when DB is missing
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 scripts/setup_exercise_db.py --check-db`
Expected: FAIL because the file does not exist yet.

- [ ] **Step 3: Write minimal implementation**

Create `scripts/setup_exercise_db.py` with:

```python
import argparse
from pathlib import Path

DB_DIR = Path(__file__).resolve().parent.parent / "exercise-db"
INDEX_FILE = DB_DIR / "exercises.json"

def check_db() -> int:
    if INDEX_FILE.exists():
        print(f"OK: database found at {INDEX_FILE}")
        return 0
    print("MISSING: exercise database not initialized")
    print("Next step: place exercise JSON and images under exercise-db/")
    return 1

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-db", action="store_true")
    args = parser.parse_args()
    if args.check_db:
        return check_db()
    DB_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Created database directory: {DB_DIR}")
    print("Add exercise data files, then run --check-db")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Create `scripts/query_exercises.py` with:

```python
import argparse
import json
from pathlib import Path

DB_DIR = Path(__file__).resolve().parent.parent / "exercise-db"
INDEX_FILE = DB_DIR / "exercises.json"


def load_exercises():
    if not INDEX_FILE.exists():
        return None
    return json.loads(INDEX_FILE.read_text())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-db", action="store_true")
    parser.add_argument("--muscle")
    parser.add_argument("--equipment")
    parser.add_argument("--id")
    args = parser.parse_args()

    exercises = load_exercises()
    if args.check_db:
        if exercises is None:
            print("MISSING: exercise database not initialized")
            return 1
        print(f"OK: loaded {len(exercises)} exercises")
        return 0

    if exercises is None:
        print("Database unavailable. Provide text-only exercise guidance and initialization help.")
        return 1

    if args.id:
        match = next((e for e in exercises if e.get("id") == args.id), None)
        if not match:
            print("No exercise found")
            return 1
        print(json.dumps(match, ensure_ascii=False, indent=2))
        return 0

    filtered = exercises
    if args.muscle:
        filtered = [e for e in filtered if args.muscle in e.get("primaryMuscles", [])]
    if args.equipment:
        filtered = [e for e in filtered if e.get("equipment") == args.equipment]

    for item in filtered[:20]:
        print(f"{item.get('id')}\t{item.get('name')}\t{item.get('image')}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Then update `references/exercise-db-setup.md` to match the actual commands and directory.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 scripts/setup_exercise_db.py --check-db ; python3 scripts/query_exercises.py --check-db`
Expected: clean “MISSING” messages with exit code 1 until data is installed, not Python tracebacks.

- [ ] **Step 5: Commit**

```bash
git add scripts/setup_exercise_db.py scripts/query_exercises.py references/exercise-db-setup.md
git commit -m "feat: add exercise database setup and query scripts"
```

### Task 6: Update README for the layered system and image lookup

**Files:**
- Modify: `README.md`
- Test: `README.md`

- [ ] **Step 1: Write the failing test**

Use this checklist:

```markdown
README must explain the layered repository structure.
README must explain profile memory files.
README must explain exercise image lookup and the database setup path.
README must show degraded behavior when the DB is missing.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `grep -n "profiles/\|skills/\|exercise image\|query_exercises.py" README.md`
Expected: FAIL or incomplete coverage because the current README does not exist or does not document the new system.

- [ ] **Step 3: Write minimal implementation**

Write `README.md` with sections:

```md
# Personal Fitness Coach
## What This Repository Is
## Repository Structure
## Memory Files
## Exercise Database and Image Lookup
## Quick Start
## Degraded Mode Without Database
```

Include concrete commands:

```bash
python3 scripts/setup_exercise_db.py
python3 scripts/setup_exercise_db.py --check-db
python3 scripts/query_exercises.py --muscle chest --equipment dumbbell
python3 scripts/query_exercises.py --id Incline_Dumbbell_Press
```

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "profiles/\|skills/\|Exercise Database and Image Lookup\|query_exercises.py" README.md`
Expected: PASS with all documented sections and commands.

- [ ] **Step 5: Commit**

```bash
git add README.md
git commit -m "docs: describe layered fitness coach workspace"
```

### Task 7: Verify repository structure and push

**Files:**
- Modify: repository working tree
- Test: full repository structure

- [ ] **Step 1: Write the failing test**

Use this final acceptance list:

```markdown
- root orchestrator SKILL.md exists
- profiles/ contains two example memory templates
- skills/ contains eight engine files
- references/ contains seven docs
- examples/ contains three example files
- scripts/ contains setup and query scripts
- README explains the whole system
```

- [ ] **Step 2: Run test to verify it fails**

Run: `test -f SKILL.md && test -f profiles/EXAMPLE-HEALTH-PROFILE.md && test -f skills/exercise-engine.md && test -f references/exercise-db-setup.md && test -f examples/coach-mode-example.md && test -f scripts/query_exercises.py && test -f README.md`
Expected: FAIL before all previous tasks are completed.

- [ ] **Step 3: Write minimal implementation**

No new code. Finish all prior tasks and ensure paths and content are consistent.

- [ ] **Step 4: Run test to verify it passes**

Run: `find . -maxdepth 2 \( -path './.git' -o -path './exercise-db' \) -prune -o -type f | sort`
Expected: repository shows the layered directories and files described in the plan.

- [ ] **Step 5: Commit**

```bash
git add SKILL.md README.md profiles/ skills/ references/ examples/ scripts/
git commit -m "feat: rebuild repository into layered fitness skill workspace"
```

## Self-Review
- Spec coverage: covers layered repo structure, md memory templates, modular engines, references/examples, and exercise-image lookup with missing-db fallback.
- Placeholder scan: no TBD/TODO placeholders left in task steps.
- Type consistency: uses the same paths and names throughout (`profiles/`, `skills/`, `references/`, `examples/`, `scripts/`, `exercise-db/`).
