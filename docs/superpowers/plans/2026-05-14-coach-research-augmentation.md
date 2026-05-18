# Coach Research Augmentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a markdown-based public-web / Douyin coach research augmentation layer that is only used on explicit request and degrades cleanly to static coach profiles.

**Architecture:** Keep `coach_profiles/*.md` as the source-of-truth baseline and add a parallel `coach_research_notes/` layer for optional public-content observations. Route usage through a new `skills/coach-research-engine.md` contract, update root docs to mention the layer, and prove the trigger / fallback behavior with repository-level checks.

**Tech Stack:** Markdown docs, repository skill files, README guidance, bash grep checks

---

## File Structure

### Files to Create

- `coach_research_notes/EXAMPLE-pamela-reif.md` — example augmentation note showing freshness, confidence, public-content signals, caveats, and integration notes
- `skills/coach-research-engine.md` — workflow contract for when and how to use optional coach research augmentation
- `references/research-source-rules.md` — allowed-source framing, claim limits, and public-content boundary rules
- `references/research-note-schema.md` — canonical markdown schema for research augmentation notes
- `examples/research-augmentation-example.md` — example of static-only vs augmented coach-selection output

### Files to Modify

- `SKILL.md` — add the new repository layer and top-level workflow step for optional coach research augmentation
- `README.md` — document the new augmentation layer, note directory, and usage model
- `references/coach-research-policy.md` — expand the current short policy into explicit trigger, fallback, freshness, and boundary rules

---

### Task 1: Add the coach research engine and note schema

**Files:**
- Create: `skills/coach-research-engine.md`
- Create: `references/research-note-schema.md`
- Test: `skills/coach-research-engine.md`
- Test: `references/research-note-schema.md`

- [ ] **Step 1: Write the failing test**

Use these exact checks to define the required sections:

```bash
grep -q "# Coach Research Engine" skills/coach-research-engine.md && \
grep -q "## Trigger Rules" skills/coach-research-engine.md && \
grep -q "## Baseline-First Flow" skills/coach-research-engine.md && \
grep -q "## Fallback Rules" skills/coach-research-engine.md && \
grep -q "## Boundaries" skills/coach-research-engine.md && \
grep -q "# Research Note Schema" references/research-note-schema.md && \
grep -q "## Required Sections" references/research-note-schema.md && \
grep -q "## Freshness and Confidence Fields" references/research-note-schema.md
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
cd "/Users/bytedance/personal_fitness/.worktrees/coach-selection-style-research" && grep -q "# Coach Research Engine" skills/coach-research-engine.md
```

Expected: FAIL with `No such file or directory`

- [ ] **Step 3: Write minimal implementation**

Create `skills/coach-research-engine.md` with this content:

```md
# Coach Research Engine

## When To Use
Use when the user explicitly asks for newer public content, deeper coach-specific nuance, or Douyin / web augmentation.

## Trigger Rules
Activate this layer only when the user clearly asks for public-web augmentation, such as:
- 结合最近公开内容
- 参考抖音看看
- deepsearch 补强
- 最近公开内容里更常练什么

## Baseline-First Flow
1. Read `coach_profiles/<coach>.md` first.
2. Read `references/coach-style-guide.md` and `references/coach-research-policy.md`.
3. If the user explicitly requested augmentation, read `coach_research_notes/<coach>.md` when available.
4. Use research notes only to refine public-content nuance, examples, and recent emphasis.
5. Map the combined result back to coach recommendation, mixed-coach composition, or plan framing.

## Allowed Refinements
Research augmentation may refine:
- recent public emphasis
- recent content themes
- recent session organization patterns
- recent communication style

## Fallback Rules
If no research note exists or no fresh public signal is available:
- continue with the static profile
- clearly frame the answer as static-profile-based
- do not invent recent observations
- do not block normal coach selection output

## Boundaries
Research augmentation does not override:
- safety boundaries
- scope limits
- the core suitability model in the static profile

Treat public-web and Douyin results as public-content observations, not medical advice, certification proof, or complete evidence of a coach's system.
```

Create `references/research-note-schema.md` with this content:

```md
# Research Note Schema

## Purpose
Use this schema for files under `coach_research_notes/` that capture optional public-content augmentation for a named coach.

## Required Sections
Every research note should contain:
- `# <Coach Name> Research Augmentation`
- `## Research Status`
- `## Public Content Signals`
- `## Reinforced Style Notes`
- `## Source Caveats`
- `## Integration Notes`

## Freshness and Confidence Fields
Under `## Research Status`, include:
- `source mode: public-web` or `source mode: douyin+public-web`
- `freshness: YYYY-MM-DD`
- `confidence: low / medium / high`
- `usage: optional augmentation only`

## Writing Rules
- Write directional observations, not absolute truths.
- Do not claim medical authority, certification, or complete methodology from public samples.
- Keep static `coach_profiles/*.md` as the baseline.
- Use caveats when the sample window is narrow or old.
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```bash
cd "/Users/bytedance/personal_fitness/.worktrees/coach-selection-style-research" && \
grep -q "# Coach Research Engine" skills/coach-research-engine.md && \
grep -q "## Trigger Rules" skills/coach-research-engine.md && \
grep -q "## Baseline-First Flow" skills/coach-research-engine.md && \
grep -q "## Fallback Rules" skills/coach-research-engine.md && \
grep -q "## Boundaries" skills/coach-research-engine.md && \
grep -q "# Research Note Schema" references/research-note-schema.md && \
grep -q "## Required Sections" references/research-note-schema.md && \
grep -q "## Freshness and Confidence Fields" references/research-note-schema.md
```

Expected: PASS with exit code `0`

- [ ] **Step 5: Commit**

```bash
git add skills/coach-research-engine.md references/research-note-schema.md
git commit -m "$(cat <<'EOF'
feat: add coach research workflow contract

Define the markdown workflow and schema for optional coach research augmentation notes.
EOF
)"
```

### Task 2: Add source rules and example research note

**Files:**
- Create: `references/research-source-rules.md`
- Create: `coach_research_notes/EXAMPLE-pamela-reif.md`
- Test: `references/research-source-rules.md`
- Test: `coach_research_notes/EXAMPLE-pamela-reif.md`

- [ ] **Step 1: Write the failing test**

```bash
grep -q "# Research Source Rules" references/research-source-rules.md && \
grep -q "## Allowed Source Framing" references/research-source-rules.md && \
grep -q "## Disallowed Claims" references/research-source-rules.md && \
grep -q "# Pamela Reif Research Augmentation" coach_research_notes/EXAMPLE-pamela-reif.md && \
grep -q "## Research Status" coach_research_notes/EXAMPLE-pamela-reif.md && \
grep -q "confidence: medium" coach_research_notes/EXAMPLE-pamela-reif.md
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
cd "/Users/bytedance/personal_fitness/.worktrees/coach-selection-style-research" && grep -q "# Research Source Rules" references/research-source-rules.md
```

Expected: FAIL with `No such file or directory`

- [ ] **Step 3: Write minimal implementation**

Create `references/research-source-rules.md` with this content:

```md
# Research Source Rules

## Allowed Source Framing
Public-web and Douyin results may be used as:
- public-content signals
- style and emphasis observations
- example-enhancement inputs
- recent-theme observations

## Disallowed Claims
Do not use public samples as proof of:
- medical advice
- coaching certification or professional status
- complete methodology
- private-life facts
- guaranteed body-shaping outcomes

## Usage Rules
- Static `coach_profiles/*.md` stay primary.
- Research notes are optional augmentation only.
- If the public sample is narrow, old, or weak, reduce confidence.
- If no research note exists, answer with the static profile and say so.
```

Create `coach_research_notes/EXAMPLE-pamela-reif.md` with this content:

```md
# Pamela Reif Research Augmentation

## Research Status
- source mode: public-web
- freshness: 2026-05-14
- confidence: medium
- usage: optional augmentation only

## Public Content Signals
- Recent public content often stays short, dense, and home-friendly.
- Session framing still leans toward efficient full-body or cardio-heavy blocks.
- Public examples tend to feel completion-oriented and rhythm-driven.

## Reinforced Style Notes
- Compared with the static profile, recent public content reinforces the impression of time-efficient, high-density training.
- The public-facing tone appears more aligned with quick execution and polished follow-along structure than with detailed coaching explanation.

## Source Caveats
- This note reflects public-facing content samples, not a complete coaching system.
- Platform recency can shift quickly.
- Public emphasis does not prove universal suitability.

## Integration Notes
- Use this note only when the user explicitly asks for newer public-content nuance.
- Keep the static profile as the main suitability baseline.
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```bash
cd "/Users/bytedance/personal_fitness/.worktrees/coach-selection-style-research" && \
grep -q "# Research Source Rules" references/research-source-rules.md && \
grep -q "## Allowed Source Framing" references/research-source-rules.md && \
grep -q "## Disallowed Claims" references/research-source-rules.md && \
grep -q "# Pamela Reif Research Augmentation" coach_research_notes/EXAMPLE-pamela-reif.md && \
grep -q "## Research Status" coach_research_notes/EXAMPLE-pamela-reif.md && \
grep -q "confidence: medium" coach_research_notes/EXAMPLE-pamela-reif.md
```

Expected: PASS with exit code `0`

- [ ] **Step 5: Commit**

```bash
git add references/research-source-rules.md coach_research_notes/EXAMPLE-pamela-reif.md
git commit -m "$(cat <<'EOF'
feat: add coach research note examples

Document source-boundary rules and add an example augmentation note for coach research.
EOF
)"
```

### Task 3: Update root skill and policy docs for the new layer

**Files:**
- Modify: `SKILL.md:11-35`
- Modify: `references/coach-research-policy.md:1-10`
- Test: `SKILL.md`
- Test: `references/coach-research-policy.md`

- [ ] **Step 1: Write the failing test**

```bash
grep -q "coach_research_notes" SKILL.md && \
grep -q "skills/coach-research-engine.md" SKILL.md && \
grep -q "## Trigger Rules" references/coach-research-policy.md && \
grep -q "## Fallback Rules" references/coach-research-policy.md && \
grep -q "## Freshness Rules" references/coach-research-policy.md
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
cd "/Users/bytedance/personal_fitness/.worktrees/coach-selection-style-research" && grep -q "coach_research_notes" SKILL.md
```

Expected: FAIL with exit code `1`

- [ ] **Step 3: Write minimal implementation**

Update the repository layer list in `SKILL.md` to:

```md
## Repository Layers
- `profiles/`: long-term and short-term user memory templates
- `skills/`: decision engines and workflow modules
- `references/`: domain rules and style guides
- `coach_profiles/`: named coach-method profiles used for matching and mixing
- `coach_research_notes/`: optional public-content augmentation notes for named coaches
- `examples/`: example interactions and memory updates
- `scripts/`: exercise database setup and query tools
```

Update the top-level workflow in `SKILL.md` to:

```md
## Top-Level Workflow
1. Read or initialize `profiles/` memory.
2. Use `skills/intake-engine.md` to collect missing facts.
3. Determine whether the user wants a specific coach or mixed-coach mode.
4. Use `references/coach-style-guide.md` and `coach_profiles/*.md` to choose styles.
5. If the user explicitly asks for newer public content or deeper coach nuance, use `skills/coach-research-engine.md` and `coach_research_notes/*.md` to optionally augment the static baseline.
6. Use `skills/safety-gate.md` before giving a detailed plan.
7. Use `references/segmentation-rules.md` to classify the user.
8. Use `skills/calorie-engine.md`, `skills/nutrition-engine.md`, and `skills/training-engine.md` to generate the plan.
9. If the user asks about an exercise, use `skills/exercise-engine.md` and the scripts in `scripts/` for optional exercise lookup.
10. If the exercise database is unavailable, give text-only guidance and explain how to initialize it.
11. Use `skills/memory-engine.md` and `skills/adjustment-engine.md` to update or refine recommendations.
```

Update the boundary section in `SKILL.md` to:

```md
## Boundaries
- Coach style changes tone, programming emphasis, and exercise preference. It does not override safety boundaries.
- Static repository coach profiles are the default source of truth.
- Optional public-web augmentation is only used when the user explicitly asks for newer public content or deeper coach-specific detail.
- `coach_research_notes/*.md` are augmentation notes, not replacements for static coach profiles.
- Exercise lookup is optional support, not a requirement for general planning.
```

Replace `references/coach-research-policy.md` with:

```md
# Coach Research Policy

## Default Source Of Truth
Static repository coach profiles are primary.

## Trigger Rules
Only use coach research augmentation when the user explicitly asks for recent public content, newer trends, Douyin / web nuance, or deeper coach-specific detail.

## How To Use Results
Treat results as public-content observations that can refine examples, exercise choices, recent emphasis, or style notes. Do not treat them as medical advice, certification claims, or full methodology proof.

## Fallback Rules
If no research note exists or no usable public signal is available, answer from the static coach profile and clearly say the result is static-profile-based.

## Freshness Rules
Research notes should carry freshness metadata. Older notes may still be used, but confidence should be reduced and possible drift should be acknowledged.
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```bash
cd "/Users/bytedance/personal_fitness/.worktrees/coach-selection-style-research" && \
grep -q "coach_research_notes" SKILL.md && \
grep -q "skills/coach-research-engine.md" SKILL.md && \
grep -q "## Trigger Rules" references/coach-research-policy.md && \
grep -q "## Fallback Rules" references/coach-research-policy.md && \
grep -q "## Freshness Rules" references/coach-research-policy.md
```

Expected: PASS with exit code `0`

- [ ] **Step 5: Commit**

```bash
git add SKILL.md references/coach-research-policy.md
git commit -m "$(cat <<'EOF'
feat: wire coach research augmentation into root workflow

Expose the optional research layer in the root skill workflow and expand the coach research policy.
EOF
)"
```

### Task 4: Update README and add user-facing example

**Files:**
- Modify: `README.md:6-43`
- Create: `examples/research-augmentation-example.md`
- Test: `README.md`
- Test: `examples/research-augmentation-example.md`

- [ ] **Step 1: Write the failing test**

```bash
grep -q "coach_research_notes" README.md && \
grep -q "Coach Research Augmentation" README.md && \
grep -q "# Research Augmentation Example" examples/research-augmentation-example.md && \
grep -q "Static-only answer" examples/research-augmentation-example.md && \
grep -q "Augmented answer" examples/research-augmentation-example.md
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
cd "/Users/bytedance/personal_fitness/.worktrees/coach-selection-style-research" && grep -q "coach_research_notes" README.md
```

Expected: FAIL with exit code `1`

- [ ] **Step 3: Write minimal implementation**

Update the repository structure section in `README.md` to:

```md
## Repository Structure
- `SKILL.md` - root orchestrator
- `profiles/` - durable health profile and recent progress memory files
- `skills/` - modular intake, safety, calorie, nutrition, training, exercise, memory, adjustment, and coach research engines
- `references/` - stable background rules and setup guides
- `coach_profiles/` - named coach profiles for matching and mixing
- `coach_research_notes/` - optional public-content augmentation notes for named coaches
- `examples/` - example outputs and memory updates
- `scripts/` - local exercise database setup and query tools
```

Add this section after `## Optional Public-Web Augmentation` in `README.md`:

```md
## Coach Research Augmentation
When the user explicitly asks for newer public content, Douyin nuance, or deeper coach-specific detail, use the optional augmentation layer instead of replacing the static baseline.

- Read the static coach profile first.
- Use `skills/coach-research-engine.md` to decide whether augmentation is allowed.
- Read `coach_research_notes/*.md` only on explicit request.
- If no augmentation note exists, fall back to the static profile and say so.
```

Create `examples/research-augmentation-example.md` with this content:

```md
# Research Augmentation Example

## User
我想看 Pamela 最近公开内容有没有更偏短时高效，顺便结合她原本风格给我建议。

## Static-only answer
如果只看静态 profile，Pamela Reif 仍然更偏高效率 HIIT、全身塑形和高训练密度，更适合有一定基础、想在有限时间内提高训练密度的人。

## Augmented answer
如果再结合公开内容补强，这个印象会更偏“短时、完成度导向、居家友好”的 follow-along 风格。但这层只是一种公开内容观察，不替代静态 profile 对适配人群和强度门槛的判断。
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```bash
cd "/Users/bytedance/personal_fitness/.worktrees/coach-selection-style-research" && \
grep -q "coach_research_notes" README.md && \
grep -q "Coach Research Augmentation" README.md && \
grep -q "# Research Augmentation Example" examples/research-augmentation-example.md && \
grep -q "Static-only answer" examples/research-augmentation-example.md && \
grep -q "Augmented answer" examples/research-augmentation-example.md
```

Expected: PASS with exit code `0`

- [ ] **Step 5: Commit**

```bash
git add README.md examples/research-augmentation-example.md
git commit -m "$(cat <<'EOF'
docs: add coach research augmentation usage examples

Document the new augmentation layer in the README and add a user-facing comparison example.
EOF
)"
```

## Self-Review

### Spec coverage

- architecture: covered by Tasks 1–4
- coach research workflow module: covered by Task 1
- source rules and note schema: covered by Tasks 1–2
- augmentation note layer: covered by Task 2
- root workflow and policy updates: covered by Task 3
- README and example updates: covered by Task 4
- trigger / fallback / freshness / boundaries: covered across Tasks 1–4

### Placeholder scan

No `TBD`, `TODO`, or unresolved placeholders remain. All file paths, content, and validation commands are explicit.

### Type consistency

The plan consistently uses:

- `coach_research_notes/*.md` for augmentation notes
- `skills/coach-research-engine.md` for the workflow contract
- `references/research-note-schema.md` for the note structure
- `references/research-source-rules.md` for source and claim boundaries

These names are stable across all tasks.
