#!/usr/bin/env python3
"""
Exercise database setup script.

Features:
- Check if database exists
- Download from Gitee (git clone or ZIP fallback)
- Update to latest version
- Verify database integrity

Works with the free-exercise-db open source database (800+ exercises with images).
If the external database is unavailable, the built-in data/exercise-library.json
(147+ exercises) still works for text-only guidance.
"""

import os
import sys
import json
import shutil
import argparse
import subprocess
from pathlib import Path
from urllib.request import urlretrieve
from urllib.error import URLError

# Database info
DB_REPO_URL = "https://gitee.com/kaiji1126/free-exercise-db.git"
DB_ARCHIVE_URL = "https://gitee.com/kaiji1126/free-exercise-db/repository/archive/main.zip"
DB_NAME = "exercise-db"


def get_skill_dir() -> Path:
    """Get skill directory path."""
    return Path(__file__).parent.parent.resolve()


def get_db_path() -> Path:
    """Get database path."""
    return get_skill_dir() / DB_NAME


def get_exercises_path() -> Path:
    """Get exercises directory path."""
    return get_db_path() / "exercises"


def get_dist_path() -> Path:
    """Get merged file path."""
    return get_db_path() / "dist" / "exercises.json"


def check_db_exists() -> bool:
    """Check if database exists."""
    return get_exercises_path().exists() or get_dist_path().exists()


def check_git_available() -> bool:
    """Check if git is available."""
    try:
        result = subprocess.run(
            ["git", "--version"], capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except (subprocess.SubprocessError, FileNotFoundError):
        return False


def clone_with_git() -> bool:
    """Clone database using git."""
    db_path = get_db_path()
    print(f"Cloning database from Gitee...")
    print(f"Repository: {DB_REPO_URL}")
    try:
        result = subprocess.run(
            ["git", "clone", DB_REPO_URL, str(db_path)],
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode == 0:
            print("✓ Database cloned successfully!")
            return True
        print(f"✗ Clone failed: {result.stderr}")
        return False
    except subprocess.SubprocessError as e:
        print(f"✗ Clone error: {e}")
        return False


def download_with_urllib() -> bool:
    """Download database ZIP using urllib."""
    import zipfile
    import tempfile

    db_path = get_db_path()
    temp_dir = Path(tempfile.mkdtemp())

    print(f"Downloading database from Gitee...")
    print(f"URL: {DB_ARCHIVE_URL}")
    try:
        zip_path = temp_dir / "db.zip"
        urlretrieve(DB_ARCHIVE_URL, zip_path)
        print("✓ Download complete")

        print("Extracting...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        extracted_dirs = [d for d in temp_dir.iterdir() if d.is_dir()]
        if not extracted_dirs:
            print("✗ Extraction failed: no directory found")
            return False

        source_dir = extracted_dirs[0]
        if db_path.exists():
            shutil.rmtree(db_path)
        shutil.move(str(source_dir), str(db_path))
        print("✓ Extraction complete")

        shutil.rmtree(temp_dir)
        return True

    except (URLError, zipfile.BadZipFile, OSError) as e:
        print(f"✗ Download/extraction failed: {e}")
        if temp_dir.exists():
            shutil.rmtree(temp_dir, ignore_errors=True)
        return False


def setup_database(force=False) -> bool:
    """Setup the database."""
    db_path = get_db_path()

    if check_db_exists() and not force:
        print(f"✓ Database already exists: {db_path}")
        print("  Use --force to re-download")
        return True

    if force and db_path.exists():
        print("Removing old database...")
        shutil.rmtree(db_path)

    if check_git_available():
        print("Git detected, using git clone...")
        if clone_with_git():
            return True
        print("Git clone failed, trying direct download...")

    return download_with_urllib()


def update_database() -> bool:
    """Update database to latest version."""
    db_path = get_db_path()

    if not db_path.exists():
        print("Database does not exist, downloading...")
        return setup_database()

    git_dir = db_path / ".git"
    if git_dir.exists():
        print("Updating database (git pull)...")
        try:
            result = subprocess.run(
                ["git", "-C", str(db_path), "pull"],
                capture_output=True, text=True, timeout=60,
            )
            if result.returncode == 0:
                print("✓ Database updated successfully!")
                return True
            print(f"✗ Update failed: {result.stderr}")
            return False
        except subprocess.SubprocessError as e:
            print(f"✗ Update error: {e}")
            return False
    else:
        print("Database is not a git repository, re-downloading...")
        return setup_database(force=True)


def verify_database() -> bool:
    """Verify database integrity."""
    db_path = get_db_path()
    exercises_path = get_exercises_path()
    dist_path = get_dist_path()

    print(f"Verifying database: {db_path}")

    if not db_path.exists():
        print("✗ Database directory does not exist")
        return False

    if exercises_path.exists():
        exercise_count = len(list(exercises_path.glob("*")))
        print(f"✓ Found {exercise_count} exercise directories")

        sample_dirs = list(exercises_path.glob("*"))[:3]
        for d in sample_dirs:
            exercise_json = d / "exercise.json"
            if exercise_json.exists():
                try:
                    with open(exercise_json, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    print(f"  ✓ {data.get('name', d.name)}")
                except (json.JSONDecodeError, IOError) as e:
                    print(f"  ✗ {d.name}: {e}")
                    return False
        return True

    if dist_path.exists():
        try:
            with open(dist_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                print(f"✓ Found merged file with {len(data)} exercises")
                return True
            print("✗ Merged file format error")
            return False
        except (json.JSONDecodeError, IOError) as e:
            print(f"✗ Failed to read merged file: {e}")
            return False

    print("✗ Database incomplete: missing exercises/ and dist/exercises.json")
    return False


def get_db_info():
    """Get database info."""
    db_path = get_db_path()

    if not db_path.exists():
        print("Database does not exist")
        return

    print(f"Database path: {db_path}")

    exercises_path = db_path / "exercises"
    if exercises_path.exists():
        count = len(list(exercises_path.glob("*")))
        print(f"Exercise count: {count}")

    git_dir = db_path / ".git"
    if git_dir.exists():
        print("Data source: git repository")
        try:
            result = subprocess.run(
                ["git", "-C", str(db_path), "log", "-1", "--format=%h %s"],
                capture_output=True, text=True, timeout=10,
            )
            if result.returncode == 0:
                print(f"Latest commit: {result.stdout.strip()}")
        except subprocess.SubprocessError:
            pass
    else:
        print("Data source: ZIP download")


def main():
    parser = argparse.ArgumentParser(
        description="Exercise database setup tool (free-exercise-db)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python setup_exercise_db.py              # Setup database (if not exists)
  python setup_exercise_db.py --force      # Force re-download
  python setup_exercise_db.py --update     # Update to latest version
  python setup_exercise_db.py --verify     # Verify database integrity
  python setup_exercise_db.py --info       # Show database info
  python setup_exercise_db.py --check      # Check if database exists
        """
    )

    parser.add_argument("--force", action="store_true", help="Force re-download")
    parser.add_argument("--update", action="store_true", help="Update to latest version")
    parser.add_argument("--verify", action="store_true", help="Verify database integrity")
    parser.add_argument("--info", action="store_true", help="Show database info")
    parser.add_argument("--check", action="store_true", help="Check if database exists")

    args = parser.parse_args()

    if args.check:
        exists = check_db_exists()
        print(f"Database exists: {exists}")
        if exists:
            print(f"Path: {get_db_path()}")
        sys.exit(0 if exists else 1)

    if args.info:
        get_db_info()
        sys.exit(0)

    if args.verify:
        success = verify_database()
        sys.exit(0 if success else 1)

    if args.update:
        success = update_database()
        sys.exit(0 if success else 1)

    success = setup_database(force=args.force)
    if success:
        verify_database()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
