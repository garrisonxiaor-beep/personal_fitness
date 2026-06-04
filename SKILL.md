---
name: personal-fitness-coach
description: Use when the user invokes /fitness, $personal-fitness-coach, or asks for systematic fitness planning, coach-style selection, long-term user data storage, initial profile intake, workout-log or screenshot analysis, nutrition log analysis, training-plan modification, exercise substitution, or programming across hypertrophy splits, fat-loss/recomposition, body-part specialization, strength, or powerlifting. Avoid for medical diagnosis, unrelated nutrition-only lookup, or non-training creative tasks.
---

# Personal Fitness Coach

## Purpose

Turn user fitness data into systematic, goal-aware, coach-style-personalized training recommendations. Collect missing context, classify the training goal, apply programming rules, match coach style, and return practical text advice.

## Repository Layers

- `profiles/`: long-term and short-term user memory templates
- `skills/`: decision engines and workflow modules
- `references/`: domain rules, goal modules, split guides, and style guides
- `coach_profiles/`: named coach-method profiles used for matching and mixing
- `coach_research_notes/`: optional public-content augmentation notes for named coaches
- `data/`: built-in exercise library (147+ exercises with Chinese names, body parts, movement patterns, and goals)
- `templates/`: intake and user-data JSON templates
- `scripts/`: exercise database setup, query tools, and user data management
- `examples/`: example interactions and memory updates

## When to use this skill

Use when the user:

- Invokes `/fitness`, `$personal-fitness-coach`, or explicitly asks for a systematic fitness plan.
- Asks "我该怎么做", "我的训练计划是什么", "我要怎么修改我的训练计划", or similar planning questions.
- Provides training logs, screenshots, body metrics, files, API data, or free text and wants analysis.
- Wants to save, import, update, or reuse long-term user data, training history, body metrics, or nutrition logs.
- Provides diet records or nutrition logs and wants training-relevant decisions.
- Wants programming for hypertrophy, fat loss, recomposition, body shaping, body-part specialization, strength, or powerlifting.
- Wants to choose or mix coach styles (e.g., 周六野, Pamela Reif, 凯圣王×谭指导).
- Wants training algorithm or rules design for a fitness planning system.

Do not use when the request is only:

- Medical diagnosis, injury diagnosis, or emergency symptom triage.
- Nutrition-only lookup with no training decision, such as one food's calories.
- Non-training creative work, such as posters, branding, or gym decoration.

## Inputs

Accept any of these inputs:

- Text: goal, schedule, training history, current plan, logs, soreness, preferences.
- Files: CSV, spreadsheet, JSON, markdown, notes, exported app data, program sheets.
- Screenshots: training logs, body metrics, app dashboards, plan cards.
- API data or API keys: use only for the requested analysis; never reveal secrets in the answer.
- Long-term data store: profile, training history, body metrics, and nutrition history (see `skills/memory-engine.md`).
- Built-in exercise library: use `data/exercise-library.json` for exercise selection and substitutions.
- External exercise database: optional `exercise-db/` for image-backed exercise lookup via `scripts/query_exercises.py`.

## Workflow

1. **Read or initialize memory.**
   Use `skills/memory-engine.md`. Read existing profile and progress notes before generating recommendations.

2. **Collect missing context.**
   Use `skills/intake-engine.md` to collect missing facts. Ask only the smallest number of questions needed to make the next recommendation useful. Do not block the answer when only low-impact information is missing.

3. **Determine coach style.**
   Use `references/coach-style-guide.md` and `coach_profiles/*.md`. Support single-coach and mixed-coach modes. If no coach preference is stated, recommend based on goal and adherence profile. Coach style modifies tone, exercise preference, session pacing, and nutrition framing—but never overrides safety, load constraints, or goal-module logic.

4. **Run safety screening.**
   Use `skills/safety-gate.md`. If the user reports sharp pain, numbness, dizziness, chest pain, fainting, or severe unusual symptoms, do not prescribe training through the symptom. For pregnancy, minors, eating-disorder patterns, or disease-management requests, keep guidance conservative and suggest professional evaluation.

5. **Classify the request type:**
   - Initial intake: new user, body data, how to start
   - Training-log review: completed workouts, screenshots, stalled progress
   - Plan modification: current plan, what to change
   - Exercise-library decision: choose, substitute, add exercises
   - User-data management: save, import, persist, reuse data
   - Nutrition-log review: diet records tied to training decisions
   - Algorithm design: how the system should reason

6. **Route to goal module:**
   Use `skills/training-engine.md` for the routing logic.

   - **增肌 / hypertrophy** → `references/goal-hypertrophy.md`
     - Split choice → `references/hypertrophy-splits.md`
     - 二分化 → `references/split-two-division.md`
     - 三分化/PPL → `references/ppl-practical.md`
     - 四分化 → `references/split-four-division.md`
     - 五分化 → `references/split-five-division.md`
   - **减脂 / 塑形 / recomposition** → `references/goal-fat-loss-recomposition.md`
     - Advanced → `references/fat-loss-recomposition-advanced.md`
   - **部位专攻 / weak points** → `references/goal-specialization.md`
     - Advanced → `references/specialization-advanced.md`
   - **力量举 / SBD** → `references/goal-powerlifting.md`
     - Advanced → `references/powerlifting-advanced.md`
   - **Mixed goals**: choose one primary module and one secondary; state which is primary.

7. **Apply shared programming rules.**
   Read `references/training-algorithm-library.md` for load constraints, equipment rules, adjustment rules, deload triggers, and plan construction order.

8. **Select exercises.**
   Use `data/exercise-library.json` for exercise selection and substitutions. Read `references/exercise-library-schema.md` when extending the library. If the exercise is not in the library, use alias matching, same-pattern substitutions, or temporary outside-library exercises with clear labeling. If the external `exercise-db/` is available, prefer it for image-backed lookup via `scripts/query_exercises.py`.

9. **Analyze existing data when available.**
   - Training logs → `references/training-log-analysis.md`; run `scripts/summarize_training_logs.py` for CSV/JSON logs
   - Body metrics → `references/body-metrics-analysis.md`
   - Nutrition logs → `references/nutrition-log-analysis.md`; use `scripts/manage_user_data.py import-nutrition` to persist records

10. **Diagnose and decide.**
    Use `references/recommendation-decision-tree.md` to identify the bottleneck and choose the smallest useful change.

11. **Apply coach-style overlay.**
    Tone, exercise preference, session pacing, and nutrition framing from the selected coach profile. Coach style does not override safety, goal-module logic, or load constraints.

12. **Optional coach research augmentation.**
    Use `skills/coach-research-engine.md` only when the user explicitly asks for newer public content or deeper coach-specific detail. Static coach profiles remain the default.

13. **Produce output.**
    Use the output structure defined in `skills/training-engine.md`. Include: conclusion, goal module, coach style, plan adjustment, exercise matching, progression rules, monitoring indicators, and missing data needed.

14. **Update memory.**
    Use `skills/memory-engine.md` and `skills/adjustment-engine.md`. Save durable facts to profile, recent observations to progress notes.

## Boundaries

- Coach style changes tone and emphasis, never safety boundaries.
- Static repository coach profiles are the default source of truth.
- Optional public-web augmentation is only used when the user explicitly asks for newer public content or deeper coach-specific detail.
- Exercise lookup is optional support; text-only guidance works without the database.
- Safety and scope always come before coaching style, calorie targets, or exercise selection.
- Do not replace an exercise only because progression is hard to calculate.
- Do not claim medical certainty or guaranteed body composition outcomes.

## Runtime Portability

This skill follows the open Agent Skills folder pattern: `SKILL.md` with YAML `name` and `description`, plus optional relative resources. All paths are relative (e.g., `references/...`, `data/...`, `scripts/...`) so the folder can be moved between compatible runtimes.

- `references/`, `data/`, `examples/`, `profiles/`, `coach_profiles/`, and `coach_research_notes/` are plain text or JSON resources.
- `scripts/` use only the Python standard library. If a runtime cannot execute Python, read the relevant references and update or summarize records manually.
- `agents/openai.yaml` is optional Codex/OpenAI UI metadata.
