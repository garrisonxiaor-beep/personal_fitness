# Training Engine

## Core Principle
Consistency and recovery come before complexity. Training decisions follow a goal-module architecture with coach-style overlays for tone, exercise preference, and session pacing.

## Goal-Module Routing

Before building or modifying a plan, route the request to the correct goal module:

- **增肌 / hypertrophy** → read `references/goal-hypertrophy.md`
  - When the request involves split choice (二/三/四/五分化), also read `references/hypertrophy-splits.md`
  - Then route to the matching split reference:
    - 二分化 → `references/split-two-division.md`
    - 三分化/PPL → `references/ppl-practical.md`
    - 四分化 → `references/split-four-division.md`
    - 五分化 → `references/split-five-division.md`
- **减脂 / 塑形 / recomposition** → read `references/goal-fat-loss-recomposition.md`
  - When the request involves calorie deficit, cardio, NEAT, plateau, body-shaping proportions, local shaping, diet breaks, or training adjustments while dieting, also read `references/fat-loss-recomposition-advanced.md`
- **部位专攻 / weak points** → read `references/goal-specialization.md`
  - When the request involves weak-point diagnosis, target-muscle feel, specific body-part specialization, or 4-8 week priority blocks, also read `references/specialization-advanced.md`
- **力量举 / SBD** → read `references/goal-powerlifting.md`
  - When the request involves SBD technique, sticking points, top singles, back-off sets, DUP, 12-week cycles, peaking, or attempt selection, also read `references/powerlifting-advanced.md`
- **Mixed goals** → choose one primary module and one secondary module; state which goal is primary.

## Shared Programming Rules

Read `references/training-algorithm-library.md` for:
- Data hierarchy (logs > trends > stated goals > general ranges)
- Load and equipment constraints (machine 5 kg, barbell +5 kg, dumbbell +2.5 kg/hand, shoulder isolation progression rules)
- Adjustment rules (add stimulus vs reduce fatigue)
- Deload triggers and options
- Plan construction order

## Programming Defaults by Goal

### Hypertrophy
- Weekly volume: start 8-12 hard sets per muscle; 10-20 for trained muscles when recovery supports it
- Frequency: 2-3 exposures per muscle per week
- Reps: 6-15 for compounds; 10-30 for isolations
- Intensity: most working sets at 0-3 RIR
- Progression: double progression (reps first, then load by smallest practical jump)

### Fat Loss / Recomposition
- Weekly volume: 8-14 hard sets per major muscle when recovery is limited
- Frequency: 2 exposures per major muscle; 3 if sessions are short and recoverable
- Conditioning: add steps or low-impact cardio gradually
- Priority: maintain load, reps, and technique while body metrics improve

### Specialization
- Priority muscle volume: 12-22 hard sets per week if recovery supports it
- Maintenance muscles: 4-8 hard sets per week
- Block length: 4-8 weeks, then reassess
- Reduce non-priority volume before adding more total weekly training

### Powerlifting
- Main lift work: mostly 1-6 reps, RPE 6-9
- Secondary variations: 3-8 reps for weak points and technical practice
- Accessories: 6-15+ reps for muscle, balance, and injury resilience
- Block structure: accumulation → strength → peaking → deload/test

## Decision Tree

When modifying an existing plan, read `references/recommendation-decision-tree.md` to:
1. Diagnose the bottleneck (under-stimulus, over-fatigue, technique mismatch, adherence, recovery, equipment, or goal mismatch)
2. Choose the smallest useful change
3. Define measurable indicators for the next 2-6 weeks

## Coach Style Modifiers

Coach style changes tone, exercise preference, session pacing, and nutrition framing. It does not override safety, load constraints, volume/frequency minimums, or the goal-module logic.

### Training-specific style effects

| Coach | Split preference | Exercise bias | Session style | Intensity tone |
|---|---|---|---|---|
| 凯圣王×谭指导 | PPL / 三分化 / 四分化 | 复合+分化，器械优先 | 节奏明确，主线清晰 | 追求渐进，敢于加量 |
| 周六野 | 全身 / 上下分化 | 入门友好，低冲击 | 温和鼓励，易坚持 | 稳定为先，不追极限 |
| Pamela Reif | PPL + HIIT | 高密度短时，居家 | 高效无废话 | 节奏快，完成度导向 |
| Coffee Lam | 恢复日 / 瑜伽日 | 拉伸+活动度 | 平稳舒缓，呼吸感强 | 低强度，感受优先 |
| 欧阳春晓 | 下肢+体态模块 | 下肢+核心，细节感强 | 细致拆解，强调发力 | 适中，关注正确感受 |
| 韩小四 | 全身 / 简单分化 | 最简单最安全 | 超友好，全程鼓励 | 最温和，不追强度 |
| 海洋饼干 | 全身 / 减脂分化 | 训练饮食联动 | 直接地气，不绕弯 | 中等，执行力导向 |

### How style modifies programming

1. **Split recommendation**: A beginner asking 增肌 gets full-body with 韩小四 style but PPL with 凯圣王×谭指导 style.
2. **Exercise selection**: Same "chest push day" uses barbell bench with 凯圣王 but push-ups or dumbbell press with 周六野.
3. **Session density**: Pamela style prefers time-efficient supersets; Coffee Lam prefers longer rest and breath focus.
4. **Progression framing**: 凯圣王 presents exact +5 kg jumps; 周六野 says "下次试试能不能多做1-2个".

## Exercise Selection

Use `data/exercise-library.json` for exercise selection and substitutions. Read `references/exercise-library-schema.md` when changing or extending the library.

If the requested exercise is not in the library:
1. Try synonym/alias/near-name matching (e.g., 臀推 vs 臀冲).
2. Search same body part, equipment, and movement pattern for substitutions.
3. Allow a temporary outside-library exercise but clearly state it and explain why.
4. Ask whether the user wants to add it to the library when it seems recurring.
5. Do not refuse to build a recommendation only because the library is incomplete.

If the external `exercise-db/` database is also available (via `scripts/query_exercises.py`), prefer it for image-backed exercise lookup. Otherwise, use the built-in `data/exercise-library.json`.

## Output Structure

When generating a training plan or adjustment, include:

1. **结论**: one short answer explaining what the user should do now
2. **目标模块**: the primary module (增肌/减脂塑形/部位专攻/力量举) + secondary if applicable
3. **教练风格**: which coach style was applied and how it shaped the plan
4. **计划调整**: split, exercises or movement patterns, sets, reps, load/RPE/RIR, rest, frequency, order
5. **动作匹配**: which exercises were exact library matches, alias matches, substitutions, or outside-library
6. **进阶规则**: how to add reps, load, sets, density, or difficulty
7. **观察指标**: performance, fatigue, soreness, sleep, bodyweight, measurements, or adherence signals to monitor
8. **需要补充**: only the missing inputs that materially affect the next decision
