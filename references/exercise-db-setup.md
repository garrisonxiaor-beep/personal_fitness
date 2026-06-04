# Exercise DB Setup

## Dual Data Source

This skill has two exercise data sources:

### Built-in Library (always available)
`data/exercise-library.json` — 147+ exercises with Chinese names, body parts, movement patterns, equipment, and goals.

No setup required. Used for text-only exercise guidance and plan construction.

Read `references/exercise-library-schema.md` for the schema.

### External Database (optional, for image-backed lookup)
`exercise-db/` — 800+ exercises from [free-exercise-db](https://gitee.com/kaiji1126/free-exercise-db) with demo images.

Provides image paths for exercise demonstration. Falls back gracefully when unavailable.

## Setup Command

```bash
python3 scripts/setup_exercise_db.py
```

This will:
1. Try git clone from Gitee (if git is available)
2. Fall back to ZIP download if git fails
3. Download the database to `exercise-db/` at the repository root

## Verification Commands

```bash
python3 scripts/setup_exercise_db.py --check-db
python3 scripts/setup_exercise_db.py --verify
python3 scripts/query_exercises.py --check-db
```

## Query Examples

```bash
# External DB queries
python3 scripts/query_exercises.py --muscle chest --equipment dumbbell
python3 scripts/query_exercises.py --force push --equipment dumbbell --level intermediate
python3 scripts/query_exercises.py --id "Incline_Dumbbell_Press" --detailed

# Built-in library queries (Chinese body parts)
python3 scripts/query_exercises.py --body-part 胸
python3 scripts/query_exercises.py --body-part 背 --movement-pattern vertical_pull

# Combined (search both sources)
python3 scripts/query_exercises.py --name 卧推

# List available values
python3 scripts/query_exercises.py --list-muscles
python3 scripts/query_exercises.py --list-equipment

# Output formats
python3 scripts/query_exercises.py --muscle chest --format json
python3 scripts/query_exercises.py --muscle chest --format ids
```

## Missing Database Behavior

If the external database is missing:
- The built-in `data/exercise-library.json` still provides full text-only exercise guidance
- The system explains how to initialize `exercise-db/` for image-backed lookup
- No functionality is blocked; only image demonstration is unavailable
