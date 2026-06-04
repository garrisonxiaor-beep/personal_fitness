# Adjustment Engine

## Core Principle
Make the smallest change that solves the bottleneck. Do not rewrite the entire plan when a progression rule, volume adjustment, exercise order change, or deload is enough.

Read `references/recommendation-decision-tree.md` for the full decision flow.

## Decision Order

1. Safety: pain, red flags, medical symptoms
2. Goal: hypertrophy, fat loss, specialization, powerlifting, mixed
3. Data confidence: logs/body metrics exact, partial, or sparse
4. Bottleneck diagnosis → primary action
5. Action: choose one primary change and one optional secondary change
6. Tracking: define 2-6 week evidence needed to reassess

## Bottleneck Diagnosis

| Bottleneck | Signs | Primary action |
|---|---|---|
| Under-stimulus | Recovery good, target not progressing, low volume/frequency | Add 1-2 sets/week or one exposure |
| Over-fatigue | Multiple lifts down, soreness/sleep/joints poor | Reduce volume 20-40% or deload |
| Technique mismatch | Target not felt, compensation rises | Change cues, load, exercise stability, or order |
| Progression missing | Same work repeated with no rule | Add double progression or RPE-based progression |
| Split mismatch | Schedule inconsistent, missed body parts | Change split to match days and adherence |
| Exercise redundancy | Many same-slot exercises, poor tracking | Consolidate exercises and define slots |
| Equipment mismatch | Planned loads impossible, machine jumps invalid | Adjust increments or choose same-slot available movement |
| Fat-loss plateau | 2-3 weeks no average/waist/photo change with adherence | Add steps/cardio first, then small calorie cut |
| Powerlifting weak point | Specific sticking point or lift lag | Add matching variation/accessory, not random volume |
| Specialization need | One body part lags despite general plan | Run 4-8 week priority block and reduce non-target volume |

## Action Menu

### Keep plan
Use when progress is occurring and fatigue is acceptable. Define next progression threshold.

### Add reps or load
When all sets hit the top of the rep range at target RPE/RIR:
- Barbell main lifts: default +5 kg total
- Dumbbells: default +2.5 kg per hand if rack unknown
- Machines: default +5 kg, no decimals or unsupported 2.5 kg jumps
- Shoulder isolations: reps/control/density before load

### Add volume or frequency
When recovery is good and target stimulus is low:
- Add 1-2 hard sets/week to target muscle
- Add exposure before cramming all volume into one session
- Reduce non-target volume if recovery conflict

### Reduce fatigue
When performance or recovery is worsening:
- Reduce sets 20-40% for 1 week
- Keep movement but raise RIR by 1-2
- Remove advanced techniques first
- Deload if multiple fatigue signals exist

### Change exercise
Use when target muscle not loaded despite cue changes, equipment unavailable, pain/joint irritation, or progression stalled because the movement no longer fits. Do NOT use when the only reason is that progression is hard to calculate.

### Change split
Use when user cannot adhere to current schedule, frequency is too low, session length is too long, or recovery cannot handle the split. Do NOT change just because another split sounds more advanced.

### Run specialization
When one or two target muscles are clear weak points and recovery can be reallocated:
- Target muscle 12-24 hard sets/week
- Non-target muscles 4-8 sets/week maintenance
- Block length 4-8 weeks
- Exit if target improves, recovery fails, pain rises, or progress stalls

### Deload
When two or more are present: key lifts down repeatedly, soreness/joint irritation persists, sleep/recovery stress high, 4-8 hard weeks completed, or technique worsens under normal loads.
Default: cut sets 30-50%, reduce load 5-15%, keep movement patterns, stay farther from failure.

## Special Scenarios

### Travel And Overtime
Collapse training to shorter maintainable sessions, preserve protein and movement minimums, and protect routine continuity.

### Poor Sleep And Stress
Lower training ambition, reduce recovery cost, and keep calorie deficits conservative.

### Comeback After Breaks
- < 7 days: normal progress, small increments possible
- 7-14 days: reduce last training weight by 10-15%
- 15-30 days: reduce 20-30%, increase warm-up and movement quality work
- > 30 days: treat as re-activation, rebuild from baseline

### Fat-loss plateau
1. Confirm adherence and tracking accuracy
2. Check weekly average weight, waist, photos
3. Add steps/cardio before cutting more food
4. If fatigue is high, reduce training/cardio stress or use maintenance/diet break

## Mixed-Coach Simplification Rule
If recovery, adherence, or schedule quality drops, collapse the plan to one primary coach plus one support coach.

## Load Constraints (must apply before output)

Read `references/training-algorithm-library.md` for the full load and equipment constraints:
- Fixed machines: 5 kg increments default
- Barbell: no lower than 20 kg, main lifts +5 kg
- Dumbbells: user's rack increments, assume +2.5 kg/hand
- Shoulder isolations: progress reps/control/density before load

## Mixed-Goal Handling

| Mixed goal | Primary logic | Secondary logic |
|---|---|---|
| Hypertrophy + fat loss | Fat-loss module if deficit/scale is central | Maintain hypertrophy stimulus and strength |
| Hypertrophy + weak point | Hypertrophy split plus specialization insertion | Reduce non-target volume |
| Powerlifting + hypertrophy | Powerlifting main lifts first | Accessories use hypertrophy/specialization rules |
| Fat loss + powerlifting | Strength preservation and fatigue control | Avoid aggressive deficits near tests |
| Body shaping + local weak point | Fat-loss/body-metric trend plus target muscle block | Do not promise local fat loss |
