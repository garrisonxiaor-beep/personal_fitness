# Coach Selection And Style Research Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a coach-selection layer to the personal fitness repository with named coach profiles, mixed-coach composition rules, and optional web-research augmentation that improves follow-along recommendations without breaking the stable layered architecture.

**Architecture:** Add a new `coach_profiles/` layer plus a stronger `references/coach-style-guide.md` and integrate coach selection into the root skill, intake flow, and examples. Keep static coach profiles as the default source of truth, and allow optional web research only when the user explicitly wants newer public content or more coach-specific detail.

**Tech Stack:** Markdown skill files, markdown reference files, git, optional web research in supported environments

---

### Task 1: Add coach-profile layer to repository architecture

**Files:**
- Modify: `SKILL.md`
- Modify: `docs/superpowers/plans/2026-05-14-personal-fitness-layered-skill-rebuild.md`
- Test: `SKILL.md`

- [ ] **Step 1: Write the failing test**

Use this architecture checklist:

```markdown
- Root `SKILL.md` must mention `coach_profiles/` as a repository layer.
- Root workflow must include coach selection before plan generation.
- Root workflow must state that coach styles can be single-coach or mixed by training domain.
- Root workflow must state that web research is optional and only used when explicitly requested.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `grep -n "coach_profiles/\|coach selection\|web research" SKILL.md`
Expected: FAIL or incomplete matches because the current plan does not yet include the coach-profile layer.

- [ ] **Step 3: Write minimal implementation**

Update `SKILL.md` so it includes:

```md
## Repository Layers
- `coach_profiles/`: named coach-method profiles used for matching and mixing

## Top-Level Workflow
1. Read or initialize `profiles/` memory.
2. Use `skills/intake-engine.md` to collect missing facts.
3. Determine whether the user wants a specific coach or mixed-coach mode.
4. Use `references/coach-style-guide.md` and `coach_profiles/*.md` to choose styles.
5. Only use web research when the user explicitly asks for recent public content or deeper coach-specific detail.
```

Update the rebuild plan so the final repository structure also includes `coach_profiles/` and coach-selection integration.

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "coach_profiles/\|coach selection\|web research" SKILL.md`
Expected: PASS with all three concepts present.

- [ ] **Step 5: Commit**

```bash
git add SKILL.md docs/superpowers/plans/2026-05-14-personal-fitness-layered-skill-rebuild.md
git commit -m "refactor: add coach profile layer to skill architecture"
```

### Task 2: Create named coach profile files

**Files:**
- Create: `coach_profiles/kaishengwang-tan.md`
- Create: `coach_profiles/zoey-zhouliuye.md`
- Create: `coach_profiles/pamela-reif.md`
- Create: `coach_profiles/coffee-lam.md`
- Create: `coach_profiles/ouyang-chunxiao.md`
- Create: `coach_profiles/hanxiaosi.md`
- Create: `coach_profiles/haiyangbinggan.md`
- Test: `coach_profiles/`

- [ ] **Step 1: Write the failing test**

Use this profile schema:

```markdown
Each coach profile must include:
- Style Summary
- Best For
- Less Suitable For
- Training Bias
- Nutrition Bias
- Session Style
- Weekly Split Tendencies
- Good Pairings
- Cautions
- Adaptation Notes
```

- [ ] **Step 2: Run test to verify it fails**

Run: `test -f coach_profiles/kaishengwang-tan.md && test -f coach_profiles/zoey-zhouliuye.md && test -f coach_profiles/pamela-reif.md && test -f coach_profiles/coffee-lam.md && test -f coach_profiles/ouyang-chunxiao.md && test -f coach_profiles/hanxiaosi.md && test -f coach_profiles/haiyangbinggan.md`
Expected: FAIL because the directory and files do not exist yet.

- [ ] **Step 3: Write minimal implementation**

Create each coach profile with this structure and concrete coach-specific content:

```md
# Coach Name

## Style Summary
## Best For
## Less Suitable For
## Training Bias
## Nutrition Bias
## Session Style
## Weekly Split Tendencies
## Good Pairings
## Cautions
## Adaptation Notes
```

Use the agreed mapping:
- 凯圣王×谭指导 -> strength growth, split training, progression focus
- 周六野 -> beginner-to-intermediate fat loss and shaping, warm encouragement
- Pamela Reif -> efficient HIIT and full-body shaping, stronger intensity bias
- Coffee Lam -> yoga, mobility, low-impact shaping
- 欧阳春晓 -> leg line and posture-focused shaping
- 韩小四 -> gentle fat loss for true beginners and injury-conscious users
- 海洋饼干 -> moderate-intensity fat loss with training-and-diet balance

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "## Style Summary\|## Best For\|## Good Pairings" coach_profiles/*.md`
Expected: PASS with matching sections in all seven files.

- [ ] **Step 5: Commit**

```bash
git add coach_profiles/
git commit -m "feat: add named coach method profiles"
```

### Task 3: Strengthen the coach-style guide with matching and mixing rules

**Files:**
- Modify: `references/coach-style-guide.md`
- Create: `references/coach-research-policy.md`
- Test: `references/coach-style-guide.md`
- Test: `references/coach-research-policy.md`

- [ ] **Step 1: Write the failing test**

Use this checklist:

```markdown
coach-style-guide.md must:
- include the seven named coaches
- define single-coach selection rules
- define mixed-coach composition rules by domain (strength, cardio, yoga/recovery, nutrition tone)
- state that style overlays cannot override safety or calorie guardrails

coach-research-policy.md must:
- define when web research is allowed
- define how public research supplements but does not replace static profiles
- define that results must be summarized cautiously as public-content observations
```

- [ ] **Step 2: Run test to verify it fails**

Run: `grep -n "Pamela\|周六野\|混搭\|安全" references/coach-style-guide.md && test -f references/coach-research-policy.md`
Expected: FAIL because the current guide is missing the full coach system and policy file.

- [ ] **Step 3: Write minimal implementation**

Expand `references/coach-style-guide.md` to include:

```md
## Core Rule
Coach style changes tone, programming emphasis, and exercise preference. It never overrides safety, calorie, or scope boundaries.

## Supported Coaches
| Coach | Bias | Best For |
| --- | --- | --- |
| 凯圣王×谭指导 | 力量增长 / 三分化 | 想系统练力量和增肌的人 |
| 周六野 | 塑形 / 减脂 | 新手到中级 |
| Pamela Reif | HIIT / 全身塑形 | 有基础、追求效率 |
| Coffee Lam | 瑜伽 / 拉伸 | 喜欢柔韧和恢复 |
| 欧阳春晓 | 瘦腿 / 体态 | 关注腿型与姿态 |
| 韩小四 | 温和减脂 | 零基础、怕受伤 |
| 海洋饼干 | 减脂 / 全身塑形 | 中等强度，训练饮食并重 |

## Selection Rules
## Mixed-Coach Rules
## Conflict Resolution
```

Create `references/coach-research-policy.md` with:

```md
# Coach Research Policy

## Default Source Of Truth
Static repository coach profiles are primary.

## When To Use Web Research
Only when the user explicitly asks for recent public content, newer trends, or deeper coach-specific nuance.

## How To Use Results
Treat results as public-content observations that can refine examples, exercise choices, or style notes. Do not treat them as medical or formal certification claims.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "Supported Coaches\|Mixed-Coach Rules\|凯圣王\|Pamela" references/coach-style-guide.md && grep -n "Default Source Of Truth\|When To Use Web Research" references/coach-research-policy.md`
Expected: PASS with the required sections and policy lines.

- [ ] **Step 5: Commit**

```bash
git add references/coach-style-guide.md references/coach-research-policy.md
git commit -m "docs: add coach selection and research policy guides"
```

### Task 4: Integrate coach selection into intake and examples

**Files:**
- Modify: `skills/intake-engine.md`
- Modify: `examples/quick-mode-example.md`
- Modify: `examples/coach-mode-example.md`
- Create: `examples/coach-selection-example.md`
- Test: `skills/intake-engine.md`
- Test: `examples/coach-selection-example.md`

- [ ] **Step 1: Write the failing test**

Use this checklist:

```markdown
intake-engine.md must ask or infer:
- whether the user wants a named coach
- whether the user wants mixed-coach mode
- whether the user wants static guidance only or public-web augmentation

coach-selection-example.md must show:
- single-coach selection
- mixed-coach selection
- fallback recommendation when the user has no coach preference
```

- [ ] **Step 2: Run test to verify it fails**

Run: `grep -n "named coach\|mixed-coach\|web" skills/intake-engine.md && test -f examples/coach-selection-example.md`
Expected: FAIL because the intake flow does not yet cover coach selection.

- [ ] **Step 3: Write minimal implementation**

Update `skills/intake-engine.md` with a dedicated section:

```md
## Coach Preference Intake
Ask:
- Do you want a specific coach style?
- Do you want one coach for everything or different coaches for strength, cardio, and recovery?
- Do you want to stay with the built-in profiles only, or should I also consider recent public content if needed?
```

Create `examples/coach-selection-example.md` showing:

```md
## Example 1: Single Coach
User: 我想跟周六野练
Assistant: ...

## Example 2: Mixed Coach
User: 力量日跟凯圣王，有氧跟帕梅拉，拉伸跟 Coffee Lam
Assistant: ...

## Example 3: Recommended Coach
User: 我没有特别偏好，想减脂，平时久坐
Assistant: ...
```

Then update quick and coach mode examples so they demonstrate coach-aware outputs.

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "Coach Preference Intake\|specific coach style\|mixed-coach" skills/intake-engine.md && grep -n "Single Coach\|Mixed Coach\|Recommended Coach" examples/coach-selection-example.md`
Expected: PASS with matching sections.

- [ ] **Step 5: Commit**

```bash
git add skills/intake-engine.md examples/quick-mode-example.md examples/coach-mode-example.md examples/coach-selection-example.md
git commit -m "feat: add coach selection flow and examples"
```

### Task 5: Add coach-aware planning rules to training and nutrition engines

**Files:**
- Modify: `skills/training-engine.md`
- Modify: `skills/nutrition-engine.md`
- Modify: `skills/adjustment-engine.md`
- Test: `skills/training-engine.md`
- Test: `skills/nutrition-engine.md`
- Test: `skills/adjustment-engine.md`

- [ ] **Step 1: Write the failing test**

Use this checklist:

```markdown
training-engine.md must explain how coach style affects:
- exercise selection
- split preference
- intensity style
- home vs gym bias

nutrition-engine.md must explain how coach style affects:
- simplicity vs structure
- fat-loss tone
- whether to suggest advanced strategies

adjustment-engine.md must explain how mixed-coach plans are simplified when adherence or recovery worsens.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `grep -n "coach style" skills/training-engine.md && grep -n "coach style" skills/nutrition-engine.md && grep -n "mixed-coach" skills/adjustment-engine.md`
Expected: FAIL because coach-aware rules are not present yet.

- [ ] **Step 3: Write minimal implementation**

Add sections like:

```md
## Coach Style Modifiers
- 凯圣王×谭指导 -> strength progression, split structure, gym-friendly
- 周六野 -> beginner-friendly shaping and adherence support
- Pamela Reif -> time-efficient HIIT and higher cardiovascular density
- Coffee Lam -> mobility, recovery, stretch-heavy sessions
- 欧阳春晓 -> posture and lower-body line emphasis
- 韩小四 -> gentler pacing and safer beginner framing
- 海洋饼干 -> balanced fat-loss plus diet integration
```

And in `skills/adjustment-engine.md`:

```md
## Mixed-Coach Simplification Rule
If recovery, adherence, or schedule quality drops, collapse the plan to one primary coach plus one support coach.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "Coach Style Modifiers\|凯圣王\|Pamela" skills/training-engine.md && grep -n "Coach Style Modifiers\|海洋饼干" skills/nutrition-engine.md && grep -n "Mixed-Coach Simplification Rule" skills/adjustment-engine.md`
Expected: PASS with matching sections.

- [ ] **Step 5: Commit**

```bash
git add skills/training-engine.md skills/nutrition-engine.md skills/adjustment-engine.md
git commit -m "feat: add coach-aware planning rules"
```

### Task 6: Document public-web augmentation and repository examples

**Files:**
- Modify: `README.md`
- Modify: `examples/memory-update-example.md`
- Test: `README.md`
- Test: `examples/memory-update-example.md`

- [ ] **Step 1: Write the failing test**

Use this checklist:

```markdown
README must explain:
- named coach selection
- mixed-coach mode
- static profile default vs optional public-web augmentation
- that public-web augmentation is for newer public content, not core safety logic

memory-update-example.md must show that coach preference and coach-mix preference can be saved to profile memory.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `grep -n "mixed-coach\|coach profile\|web augmentation" README.md && grep -n "coach preference\|coach mix" examples/memory-update-example.md`
Expected: FAIL because the current docs do not yet include coach-system persistence.

- [ ] **Step 3: Write minimal implementation**

Update `README.md` with sections:

```md
## Choose Your Coach
## Mixed-Coach Mode
## Optional Public-Web Augmentation
```

Update `examples/memory-update-example.md` with lines such as:

```md
- Save to profile: preferred coach = 周六野
- Save to profile: mixed coach plan = 力量=凯圣王×谭指导, 有氧=Pamela Reif, 恢复=Coffee Lam
- Save to profile: web augmentation preference = only on request
```

- [ ] **Step 4: Run test to verify it passes**

Run: `grep -n "Choose Your Coach\|Mixed-Coach Mode\|Optional Public-Web Augmentation" README.md && grep -n "preferred coach\|mixed coach plan\|web augmentation preference" examples/memory-update-example.md`
Expected: PASS with matching lines.

- [ ] **Step 5: Commit**

```bash
git add README.md examples/memory-update-example.md
git commit -m "docs: explain coach selection and memory persistence"
```

### Task 7: Verify full coach-selection system coverage

**Files:**
- Modify: repository working tree
- Test: full repository structure

- [ ] **Step 1: Write the failing test**

Use this final acceptance list:

```markdown
- `coach_profiles/` exists with seven named coach files
- `SKILL.md` routes coach selection before plan generation
- `references/coach-style-guide.md` and `references/coach-research-policy.md` exist
- intake, training, nutrition, and adjustment engines all mention coach-aware behavior
- examples demonstrate single-coach, mixed-coach, and memory persistence
- README documents static default plus optional public-web augmentation
```

- [ ] **Step 2: Run test to verify it fails**

Run: `test -f coach_profiles/kaishengwang-tan.md && test -f references/coach-research-policy.md && test -f examples/coach-selection-example.md`
Expected: FAIL before all prior tasks are completed.

- [ ] **Step 3: Write minimal implementation**

No new code. Finish all prior tasks and ensure naming and behavior are consistent across files.

- [ ] **Step 4: Run test to verify it passes**

Run: `find . -maxdepth 2 \( -path './.git' -o -path './exercise-db' \) -prune -o -type f | sort`
Expected: repository shows the new `coach_profiles/` layer and coach-system docs/examples alongside the layered skill workspace.

- [ ] **Step 5: Commit**

```bash
git add SKILL.md README.md coach_profiles/ skills/ references/ examples/ docs/superpowers/plans/
git commit -m "feat: add coach selection and style research layer"
```

## Self-Review
- Spec coverage: covers named coach selection, mixed-coach composition, static coach profiles, optional public-web augmentation, memory persistence, and coach-aware engine rules.
- Placeholder scan: no TBD/TODO placeholders left in task steps.
- Type consistency: uses `coach_profiles/`, `coach-style-guide.md`, `coach-research-policy.md`, and the same coach names throughout.
