# Exercise DB Setup

## Expected Directory
Place the local database under `exercise-db/` at the repository root.

## Setup Command
Run `python3 scripts/setup_exercise_db.py` to create the directory scaffold.

## Verification Commands
- `python3 scripts/setup_exercise_db.py --check-db`
- `python3 scripts/query_exercises.py --check-db`

## Missing Database Behavior
If the database is missing, the system should fall back to text-only exercise guidance and explain how to initialize the database.
