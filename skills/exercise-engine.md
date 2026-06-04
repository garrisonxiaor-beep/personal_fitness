# Exercise Engine

## When To Use
Use when the user asks about a specific exercise, wants exercise examples, needs exercise substitution, or needs image-backed lookup from the exercise database.

## Dual Data Source

This skill has two exercise data sources:

1. **Built-in library**: `data/exercise-library.json` (147+ exercises with Chinese names, body parts, movement patterns, equipment, and goals). Always available. Read `references/exercise-library-schema.md` for the schema.

2. **External database**: `exercise-db/` (800+ exercises from free-exercise-db with images). Optional. Access via `scripts/query_exercises.py`. Provides image-backed lookup.

## Exercise Matching Flow

When selecting, replacing, or rotating exercises:

1. **Exact match**: exact name in `data/exercise-library.json`
2. **Alias match**: curated aliases such as 臀推 → 史密斯臀冲, RDL → 罗马尼亚硬拉
3. **Near-name match**: unique library exercise that clearly contains the requested name
4. **Same-pattern substitution**: same body part, equipment, and movement pattern
5. **Outside-library fallback**: allow a temporary outside-library exercise, but clearly state it and explain why the library was insufficient
6. Ask whether the user wants to add the outside-library exercise when it seems recurring or important

Do not refuse to build a training recommendation only because the exercise library is incomplete. Do not present ambiguous or unmatched exercises as confirmed library entries.

## Image Path Output

When the external `exercise-db/` database is available and a matching exercise contains image paths, return the local image path alongside the exercise name.

Use the query script:
```bash
python3 scripts/query_exercises.py --muscle chest --equipment dumbbell
python3 scripts/query_exercises.py --id "Incline_Dumbbell_Press" --detailed
```

## Missing Database Fallback

If the external database is unavailable, provide text-only exercise guidance using the built-in `data/exercise-library.json` and explain how to initialize the external database:
```bash
python3 scripts/setup_exercise_db.py
```

## Exercise Selection Rules

When constructing a plan:
1. Prefer movements that match the user's target body part, equipment, movement pattern, goal, and constraints.
2. Apply load and equipment constraints from `references/training-algorithm-library.md`.
3. Use coach-style preferences from `coach_profiles/*.md` to influence exercise choice (e.g., 凯圣王 prefers barbell compounds; 周六野 prefers bodyweight/dumbbell beginner-friendly movements).
4. Do not replace an exercise only because progression is hard to calculate.

## Match Type Reporting

In the output, report exercise matching status:
- **exact**: direct library match
- **alias**: matched via curated alias
- **substitution**: same-pattern replacement
- **outside-library**: temporary, with reason stated
- **ambiguous**: multiple candidates, needs user confirmation
- **unmatched**: no library candidate, needs user guidance
