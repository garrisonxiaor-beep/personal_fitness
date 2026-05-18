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
