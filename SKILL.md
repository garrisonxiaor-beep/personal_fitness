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

## Quality Checks

Before finalizing any output, verify every item below. If any check fails, fix the output before presenting it to the user.

### Goal and Safety

1. **Goal alignment**: The recommendation matches the user's stated goal and available schedule/equipment. If goals are mixed, state the primary and secondary goal.
2. **Correct module**: The correct goal module was selected (`goal-hypertrophy.md`, `goal-fat-loss-recomposition.md`, `goal-specialization.md`, or `goal-powerlifting.md`).
3. **Safety screening**: Safety screening was considered and no medical diagnosis was made. If a safety flag was raised, the output addresses it before giving training or nutrition advice.

### Training Consistency

4. **Internal consistency**: Weekly volume, frequency, intensity, and progression are internally consistent. (e.g., do not recommend 20 hard sets/week for a beginner, or 6 days/week for someone who said 3 days.)
5. **Load constraints**: Load recommendations obey equipment increments from `references/training-algorithm-library.md`:
   - No machine decimal weights or unsupported 2.5 kg machine jumps
   - No barbell weight below 20 kg
   - Main barbell lifts default to +5 kg total jumps
   - Dumbbells follow rack increments; assume +2.5 kg/hand when unknown
   - Long-lever shoulder isolations do not jump linearly from 35 kg directly to 40 kg+
6. **Exercise library**: Selected exercises come from `data/exercise-library.json` when suitable. If using an outside-library exercise, state why the built-in library was insufficient.
7. **Exercise matching integrity**: Missing exercise handling did not silently invent a library match. Say whether the exercise was matched (exact/alias/near-name), substituted, or temporarily used outside the library.
8. **No lazy substitutions**: No exercise was avoided or replaced only because progression was hard to calculate. Substitutions must be user-chosen, equipment-driven, or safety-driven; state the reason.

### Decision Logic

9. **Facts vs assumptions**: The output distinguishes known data from assumptions. If screenshot or file extraction is uncertain, mark uncertain values instead of treating them as exact.
10. **Concrete next actions**: The plan includes concrete next actions for the next workout or week (specific exercises, sets, reps, load targets, or measurable behavior changes).
11. **Bottleneck named**: The bottleneck was named before changing the plan: under-stimulus, over-fatigue, technique mismatch, adherence, recovery, equipment, goal mismatch, or missing data. Do not change the plan without identifying the reason.
12. **Smallest useful change**: The recommendation uses the smallest useful change. If keeping most of the plan, explicitly state what is NOT changing.
13. **Fatigue management**: Fatigue management exists: deload triggers, volume reduction, exercise swap, or recovery adjustment when needed. Do not recommend continuous hard training without a deload plan.

### Nutrition

14. **Nutrition supports training**: Nutrition guidance, if included, supports training decisions and avoids extreme deficits or medical claims. Protein floor is met before any other macro optimization. Calorie deficit does not go below 1200 kcal (female) or 1500 kcal (male) without medical supervision.

### Coach Style Consistency

15. **Coach style applied consistently**: The selected coach style is applied consistently across training, nutrition, and tone. If the user chose mixed-coach mode, each domain uses the correct coach overlay.
16. **Coach style does not override safety**: No coach profile overrides safety boundaries, load constraints, calorie floors, or scope limits. If a coach style would suggest something unsafe, the safe recommendation takes priority and the conflict is noted.
17. **Coach style matches user level**: The coach style is appropriate for the user's training level (e.g., do not apply 凯圣王×谭指导 advanced split to a complete beginner; do not apply 韩小四 ultra-simple framing to an experienced trainee asking for powerlifting periodization).
18. **Coach style is visible in output**: The output reflects the coach style in at least two of: exercise selection, session pacing, nutrition framing, or communication tone. If the style is invisible, it was not applied.

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
