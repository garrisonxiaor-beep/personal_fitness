# Personal Fitness Coach

A layered fitness skill workspace that combines **coach-style personalization** with **systematic training programming**. Supports hypertrophy, fat-loss/recomposition, body-part specialization, and powerlifting with named coach profiles, modular engines, built-in exercise library, and optional long-term user data persistence.

## What This Repository Is

A structured health-coach skill that:
- Turns user fitness data into goal-aware, coach-style-personalized recommendations
- Covers four programming domains: hypertrophy, fat loss/recomposition, body-part specialization, powerlifting
- Provides detailed split guidance: 二分化, 三分化/PPL, 四分化, 五分化
- Supports named coach styles (周六野, Pamela Reif, 凯圣王×谭指导, etc.) with mixing
- Includes a built-in exercise library with alias matching and substitution logic
- Optionally persists user data across sessions

## Repository Structure

```
├── SKILL.md                              # Root orchestrator
├── agents/openai.yaml                    # Codex/OpenAI UI metadata
├── profiles/                             # User memory templates
├── skills/                               # Decision engines (9 modules)
│   ├── intake-engine.md                  # Information collection
│   ├── safety-gate.md                    # Safety screening
│   ├── calorie-engine.md                 # Calorie estimation
│   ├── nutrition-engine.md               # Nutrition strategy
│   ├── training-engine.md                # Training + goal-module routing
│   ├── exercise-engine.md                # Exercise selection + matching
│   ├── memory-engine.md                  # Memory read/write
│   ├── adjustment-engine.md              # Plan adjustment + decision tree
│   └── coach-research-engine.md          # Optional coach augmentation
├── coach_profiles/                       # 7 named coach profiles
├── coach_research_notes/                 # Optional public-content augmentation
├── data/exercise-library.json            # Built-in exercise library (147+ exercises)
├── references/                           # Domain rules and guides
│   ├── training-algorithm-library.md     # Shared programming rules
│   ├── recommendation-decision-tree.md   # Bottleneck → smallest action
│   ├── goal-hypertrophy.md               # Hypertrophy module
│   ├── goal-fat-loss-recomposition.md    # Fat-loss module
│   ├── goal-specialization.md            # Specialization module
│   ├── goal-powerlifting.md              # Powerlifting module
│   ├── hypertrophy-splits.md             # Split selector
│   ├── split-two-division.md             # 二分化 advanced
│   ├── ppl-practical.md                  # 三分化/PPL advanced
│   ├── split-four-division.md            # 四分化 advanced
│   ├── split-five-division.md            # 五分化 advanced
│   ├── fat-loss-recomposition-advanced.md
│   ├── specialization-advanced.md
│   ├── powerlifting-advanced.md
│   ├── exercise-library-schema.md
│   ├── coach-style-guide.md
│   ├── coach-research-policy.md
│   └── ... more references
├── scripts/                              # Python tools
│   ├── setup_exercise_db.py              # External DB setup
│   └── query_exercises.py                # Exercise queries
├── examples/                             # Usage examples
└── templates/                            # Intake and data templates (Phase 3)
```

## Choose Your Coach

| Coach | Bias | Best For |
|---|---|---|
| 凯圣王×谭指导 | 力量增长 / 三分化 | 想系统练力量和增肌的人 |
| 周六野 | 塑形 / 减脂 | 新手到中级 |
| Pamela Reif | HIIT / 全身塑形 | 有基础、追求效率 |
| Coffee Lam | 瑜伽 / 拉伸 | 喜欢柔韧和恢复 |
| 欧阳春晓 | 瘦腿 / 体态 | 关注腿型与姿态 |
| 韩小四 | 温和减脂 | 零基础、怕受伤 |
| 海洋饼干 | 减脂 / 全身塑形 | 中等强度，训练饮食并重 |

## Mixed-Coach Mode

You can mix coaches by domain: strength with 凯圣王×谭指导, cardio with Pamela Reif, recovery with Coffee Lam.

## Goal Modules

| Goal | Module | Advanced |
|---|---|---|
| 增肌 / Hypertrophy | `goal-hypertrophy.md` + split guides | `ppl-practical.md`, `split-*-division.md` |
| 减脂 / Fat Loss | `goal-fat-loss-recomposition.md` | `fat-loss-recomposition-advanced.md` |
| 部位专攻 / Specialization | `goal-specialization.md` | `specialization-advanced.md` |
| 力量举 / Powerlifting | `goal-powerlifting.md` | `powerlifting-advanced.md` |

## Exercise Database and Image Lookup

Built-in library: `data/exercise-library.json` (always available, 147+ exercises).

External database (optional, for image-backed lookup):
```bash
python3 scripts/setup_exercise_db.py
python3 scripts/setup_exercise_db.py --check-db
python3 scripts/query_exercises.py --muscle chest --equipment dumbbell
python3 scripts/query_exercises.py --id Incline_Dumbbell_Press --detailed
```

## Decision Framework

Every plan modification follows `references/recommendation-decision-tree.md`:
1. Diagnose the bottleneck (under-stimulus, over-fatigue, technique mismatch, etc.)
2. Choose the smallest useful change
3. Define measurable indicators for the next 2-6 weeks

## Optional Public-Web Augmentation

Static coach profiles are the default. Public-web augmentation is optional and only used when the user explicitly asks for newer public content or deeper coach-specific detail.

## Quick Start

1. Read `SKILL.md` for the orchestration flow.
2. Use `skills/` for decision engines, `references/` for domain rules, `coach_profiles/` for style selection.
3. Use `data/exercise-library.json` for exercise selection.
4. Initialize the external exercise database only if you need image lookup.

## Degraded Mode Without External Database

If the external database is missing, the system still provides full exercise guidance using the built-in library and explains how to initialize `exercise-db/`.
