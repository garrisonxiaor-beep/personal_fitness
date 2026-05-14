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
