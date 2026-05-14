# Personal Fitness Coach

## What This Repository Is
A layered Claude Code skill workspace for fitness, nutrition, fat-loss planning, coach-style selection, and markdown-based user memory.

## Repository Structure
- `SKILL.md` - root orchestrator
- `profiles/` - durable health profile and recent progress memory files
- `skills/` - modular intake, safety, calorie, nutrition, training, exercise, memory, and adjustment engines
- `references/` - stable background rules and setup guides
- `coach_profiles/` - named coach profiles for matching and mixing
- `examples/` - example outputs and memory updates
- `scripts/` - local exercise database setup and query tools

## Memory Files
Use `profiles/EXAMPLE-HEALTH-PROFILE.md` for durable facts and `profiles/EXAMPLE-HEALTH-PROGRESS.md` for recent execution, blockers, and next-step notes.

## Choose Your Coach
You can ask for a named coach style such as 周六野, Pamela Reif, Coffee Lam, 欧阳春晓, 韩小四, 海洋饼干, or 凯圣王×谭指导.

## Mixed-Coach Mode
You can mix coaches by domain, such as strength with 凯圣王×谭指导, cardio with Pamela Reif, and recovery with Coffee Lam.

## Exercise Database and Image Lookup
The local exercise database lives under `exercise-db/`. The scripts support exercise image lookup when data is installed.

```bash
python3 scripts/setup_exercise_db.py
python3 scripts/setup_exercise_db.py --check-db
python3 scripts/query_exercises.py --muscle chest --equipment dumbbell
python3 scripts/query_exercises.py --id Incline_Dumbbell_Press
```

## Optional Public-Web Augmentation
Static coach profiles are the default. Public-web augmentation is optional and should only be used when the user explicitly asks for newer public content or deeper coach-specific detail.

## Quick Start
1. Read `SKILL.md` for the orchestration flow.
2. Use the files in `profiles/`, `skills/`, and `references/` as the main workspace.
3. Initialize the exercise database only if you need exercise image lookup.

## Degraded Mode Without Database
If the database is missing, the system should still provide text-only exercise guidance and explain how to initialize `exercise-db/`.
