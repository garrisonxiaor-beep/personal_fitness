#!/usr/bin/env python3
"""
Free Exercise DB query script.

Features:
- Filter exercises by muscle, equipment, level, force, mechanic, category
- Query single exercise by ID
- Output in table, JSON, IDs, or detail format
- List available muscles and equipment
- Support both external free-exercise-db and built-in exercise-library.json

Works with the free-exercise-db open source database (800+ exercises with images).
Falls back to built-in data/exercise-library.json if external DB is unavailable.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional

# Paths
DB_NAME = "exercise-db"
BUILT_IN_LIBRARY = Path(__file__).resolve().parent.parent / "data" / "exercise-library.json"


def get_skill_dir() -> Path:
    return Path(__file__).parent.parent.resolve()


def get_db_path() -> Path:
    return get_skill_dir() / DB_NAME


def get_exercises_path() -> Path:
    return get_db_path() / "exercises"


def get_dist_path() -> Path:
    return get_db_path() / "dist" / "exercises.json"


def check_db_exists() -> bool:
    return get_exercises_path().exists() or get_dist_path().exists()


def load_all_exercises() -> List[Dict[str, Any]]:
    """Load all exercises from external database."""
    exercises = []

    # Try merged file first
    dist_path = get_dist_path()
    if dist_path.exists():
        with open(dist_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Fall back to per-exercise files
    exercises_path = get_exercises_path()
    if not exercises_path.exists():
        return []

    for exercise_dir in exercises_path.iterdir():
        if exercise_dir.is_dir():
            exercise_json = exercise_dir / "exercise.json"
            if exercise_json.exists():
                try:
                    with open(exercise_json, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        images_dir = exercise_dir / "images"
                        if images_dir.exists():
                            data["imagePaths"] = [
                                str(images_dir / img)
                                for img in images_dir.glob("*.jpg")
                            ]
                        exercises.append(data)
                except (json.JSONDecodeError, IOError):
                    continue

    return exercises


def load_built_in_library() -> List[Dict[str, Any]]:
    """Load exercises from built-in library."""
    if not BUILT_IN_LIBRARY.exists():
        return []
    try:
        with open(BUILT_IN_LIBRARY, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        return data.get("exercises", []) if isinstance(data, dict) else []
    except (json.JSONDecodeError, IOError):
        return []


def filter_exercises(
    exercises: List[Dict[str, Any]],
    muscle: Optional[str] = None,
    equipment: Optional[str] = None,
    level: Optional[str] = None,
    force: Optional[str] = None,
    mechanic: Optional[str] = None,
    category: Optional[str] = None,
    name: Optional[str] = None,
    exercise_id: Optional[str] = None,
    # Built-in library fields
    body_part: Optional[str] = None,
    movement_pattern: Optional[str] = None,
    goals: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Filter exercises by conditions. Supports both external DB and built-in library fields."""
    filtered = exercises

    # By ID (exact match)
    if exercise_id:
        filtered = [e for e in filtered if e.get("id", "").lower() == exercise_id.lower()]
        return filtered

    # By name (fuzzy match)
    if name:
        name_lower = name.lower()
        filtered = [
            e for e in filtered
            if name_lower in e.get("name", "").lower()
            or name_lower in e.get("name_zh", "").lower()
        ]

    # External DB fields
    if muscle:
        muscle_lower = muscle.lower()
        filtered = [
            e for e in filtered
            if muscle_lower in [m.lower() for m in e.get("primaryMuscles", [])]
            or muscle_lower in [m.lower() for m in e.get("secondaryMuscles", [])]
            or muscle_lower in str(e.get("body_part", "")).lower()
            or muscle_lower in str(e.get("body_part_id", "")).lower()
        ]

    if equipment:
        equipment_lower = equipment.lower()
        filtered = [
            e for e in filtered
            if e.get("equipment", "").lower() == equipment_lower
            or e.get("equipment_id", "").lower() == equipment_lower
        ]

    if level:
        level_lower = level.lower()
        filtered = [e for e in filtered if e.get("level", "").lower() == level_lower]

    if force:
        force_lower = force.lower()
        filtered = [e for e in filtered if e.get("force", "").lower() == force_lower]

    if mechanic:
        mechanic_lower = mechanic.lower()
        filtered = [e for e in filtered if e.get("mechanic", "").lower() == mechanic_lower]

    if category:
        category_lower = category.lower()
        filtered = [e for e in filtered if e.get("category", "").lower() == category_lower]

    # Built-in library fields
    if body_part:
        bp_lower = body_part.lower()
        filtered = [
            e for e in filtered
            if bp_lower in str(e.get("body_part", "")).lower()
            or bp_lower in str(e.get("body_part_id", "")).lower()
        ]

    if movement_pattern:
        mp_lower = movement_pattern.lower()
        filtered = [e for e in filtered if mp_lower in str(e.get("movement_pattern", "")).lower()]

    if goals:
        goals_lower = goals.lower()
        filtered = [
            e for e in filtered
            if any(goals_lower in str(g).lower() for g in e.get("goals", []))
        ]

    return filtered


def format_exercise_brief(exercise: Dict[str, Any]) -> str:
    """Format exercise brief info."""
    name = exercise.get("name_zh") or exercise.get("name", "Unknown")
    level = exercise.get("level", "-")
    equipment = exercise.get("equipment") or exercise.get("equipment_id", "-")
    primary = ", ".join(exercise.get("primaryMuscles", [])) or exercise.get("body_part", "-")
    return f"{name} | {level} | {equipment} | {primary}"


def format_exercise_detail(exercise: Dict[str, Any]) -> str:
    """Format exercise detailed info."""
    lines = []
    name = exercise.get("name_zh") or exercise.get("name", "Unknown")
    exercise_id = exercise.get("id", "")
    lines.append(f"# {name}")
    lines.append(f"**ID**: {exercise_id}")
    lines.append("")

    lines.append("## Basic Info")
    lines.append(f"- **Level**: {exercise.get('level', '-')}")
    lines.append(f"- **Equipment**: {exercise.get('equipment') or exercise.get('equipment_id', '-')}")
    lines.append(f"- **Force**: {exercise.get('force', '-')}")
    lines.append(f"- **Mechanic**: {exercise.get('mechanic', '-')}")
    lines.append(f"- **Category**: {exercise.get('category', '-')}")
    lines.append(f"- **Movement Pattern**: {exercise.get('movement_pattern', '-')}")

    primary = exercise.get("primaryMuscles", []) or [exercise.get("body_part", "")]
    secondary = exercise.get("secondaryMuscles", [])
    lines.append(f"- **Primary Muscles**: {', '.join(str(m) for m in primary if m) or '-'}")
    lines.append(f"- **Secondary Muscles**: {', '.join(str(m) for m in secondary if m) or '-'}")
    lines.append(f"- **Goals**: {', '.join(str(g) for g in exercise.get('goals', [])) or '-'}")
    lines.append("")

    instructions = exercise.get("instructions", [])
    if instructions:
        lines.append("## Instructions")
        for i, step in enumerate(instructions, 1):
            lines.append(f"{i}. {step}")
        lines.append("")

    image_paths = exercise.get("imagePaths", [])
    if image_paths:
        lines.append("## Demo Images")
        for path in image_paths:
            lines.append(f"- {path}")
        lines.append("")

    return "\n".join(lines)


def output_table(exercises: List[Dict[str, Any]]):
    """Output table format."""
    if not exercises:
        print("No matching exercises found")
        return

    print(f"Found {len(exercises)} exercises:\n")
    print("| # | Name | Level | Equipment | Primary Muscles |")
    print("|---|------|-------|-----------|-----------------|")

    for i, exercise in enumerate(exercises, 1):
        name = exercise.get("name_zh") or exercise.get("name", "-")
        level = exercise.get("level", "-")
        equipment = exercise.get("equipment") or exercise.get("equipment_id", "-")
        primary = ", ".join(exercise.get("primaryMuscles", [])) or exercise.get("body_part", "-")
        print(f"| {i} | {name} | {level} | {equipment} | {primary} |")


def output_json(exercises: List[Dict[str, Any]]):
    """Output JSON format."""
    print(json.dumps(exercises, ensure_ascii=False, indent=2))


def output_ids(exercises: List[Dict[str, Any]]):
    """Output ID list only."""
    for exercise in exercises:
        print(exercise.get("id", ""))


def output_detail(exercise: Dict[str, Any]):
    """Output detailed info."""
    print(format_exercise_detail(exercise))


def main():
    parser = argparse.ArgumentParser(
        description="Exercise query tool (free-exercise-db + built-in library)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Query parameters (external DB):
  --muscle          Target muscle (chest, lats, quadriceps, biceps, etc.)
  --equipment       Equipment type (dumbbell, barbell, "body only", machine, etc.)
  --level           Difficulty (beginner, intermediate, expert)
  --force           Force type (push, pull, static)
  --mechanic        Mechanic type (compound, isolation)
  --category        Category (strength, cardio, stretching, etc.)

Query parameters (built-in library):
  --body-part       Body part (胸, 背, 肩, 腿, 二头, 三头, 臀部, 腹部)
  --movement-pattern Movement pattern (horizontal_push, vertical_pull, etc.)
  --goals           Goal filter (hypertrophy, strength, powerlifting_support, etc.)

Shared parameters:
  --name            Exercise name fuzzy match
  --id              Exercise ID exact match

Output formats:
  --format          Output format (table, json, ids, detail)
  --detailed        Detailed mode (use with --id)

Examples:
  # Query chest dumbbell exercises
  python query_exercises.py --muscle chest --equipment dumbbell

  # Query by Chinese body part
  python query_exercises.py --body-part 胸

  # Query push exercises
  python query_exercises.py --force push --equipment dumbbell

  # Single exercise detail
  python query_exercises.py --id "Incline_Dumbbell_Press" --detailed

  # JSON output
  python query_exercises.py --muscle chest --format json

  # Check database
  python query_exercises.py --check-db
        """
    )

    # Query parameters
    parser.add_argument("--muscle", help="Target muscle (external DB)")
    parser.add_argument("--equipment", help="Equipment type")
    parser.add_argument("--level", help="Difficulty level")
    parser.add_argument("--force", help="Force type")
    parser.add_argument("--mechanic", help="Mechanic type")
    parser.add_argument("--category", help="Training category")
    parser.add_argument("--name", help="Exercise name (fuzzy match)")
    parser.add_argument("--id", dest="exercise_id", help="Exercise ID (exact match)")
    parser.add_argument("--body-part", help="Body part (built-in library: 胸/背/肩/腿/...)")
    parser.add_argument("--movement-pattern", help="Movement pattern")
    parser.add_argument("--goals", help="Goal filter")

    # Output parameters
    parser.add_argument("--format", choices=["table", "json", "ids", "detail"],
                        default="table", help="Output format")
    parser.add_argument("--detailed", action="store_true", help="Detailed mode")

    # Tool parameters
    parser.add_argument("--check-db", action="store_true", help="Check if database exists")
    parser.add_argument("--list-muscles", action="store_true", help="List all muscles")
    parser.add_argument("--list-equipment", action="store_true", help="List all equipment")

    # Source selection
    parser.add_argument("--source", choices=["external", "builtin", "all"],
                        default="all", help="Data source to query")

    args = parser.parse_args()

    # Check database
    if args.check_db:
        external_exists = check_db_exists()
        builtin_exists = BUILT_IN_LIBRARY.exists()
        print(f"External database: {'OK' if external_exists else 'MISSING'}")
        print(f"Built-in library:  {'OK' if builtin_exists else 'MISSING'}")
        if external_exists:
            print(f"External path: {get_db_path()}")
        if builtin_exists:
            print(f"Built-in path: {BUILT_IN_LIBRARY}")
        sys.exit(0 if (external_exists or builtin_exists) else 1)

    # Load exercises from selected sources
    exercises = []
    if args.source in ("external", "all"):
        if check_db_exists():
            exercises.extend(load_all_exercises())

    if args.source in ("builtin", "all") or not exercises:
        builtin = load_built_in_library()
        if builtin:
            exercises.extend(builtin)

    # List enums
    if args.list_muscles or args.list_equipment:
        if not exercises:
            print("No exercise data available")
            sys.exit(1)

        if args.list_muscles:
            muscles = set()
            for e in exercises:
                muscles.update(e.get("primaryMuscles", []))
                muscles.update(e.get("secondaryMuscles", []))
                bp = e.get("body_part", "")
                if bp:
                    muscles.add(bp)
                bpid = e.get("body_part_id", "")
                if bpid:
                    muscles.add(bpid)
            print("Available muscles:")
            for m in sorted(muscles):
                print(f"  - {m}")

        if args.list_equipment:
            equipment = set()
            for e in exercises:
                eq = e.get("equipment") or e.get("equipment_id", "")
                if eq:
                    equipment.add(eq)
            print("Available equipment:")
            for eq in sorted(equipment):
                print(f"  - {eq}")

        sys.exit(0)

    # Check we have data
    if not exercises:
        print("No exercise data available. Run setup or check data source.")
        print("  python scripts/setup_exercise_db.py")
        print("  Built-in library: data/exercise-library.json")
        sys.exit(1)

    # Filter
    filtered = filter_exercises(
        exercises,
        muscle=args.muscle,
        equipment=args.equipment,
        level=args.level,
        force=args.force,
        mechanic=args.mechanic,
        category=args.category,
        name=args.name,
        exercise_id=args.exercise_id,
        body_part=args.body_part,
        movement_pattern=args.movement_pattern,
        goals=args.goals,
    )

    if not filtered:
        print("No matching exercises found")
        sys.exit(0)

    # Output
    if args.detailed and len(filtered) == 1:
        output_detail(filtered[0])
        sys.exit(0)

    if args.format == "table":
        output_table(filtered)
    elif args.format == "json":
        output_json(filtered)
    elif args.format == "ids":
        output_ids(filtered)
    elif args.format == "detail":
        for exercise in filtered:
            output_detail(exercise)
            print("---")


if __name__ == "__main__":
    main()
