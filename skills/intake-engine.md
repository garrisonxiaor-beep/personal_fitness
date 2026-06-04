# Intake Engine

## Modes

### Quick Mode
Use when the user wants fast guidance with minimal friction. Collect only the fields that materially change the next recommendation.

Minimum useful fields:
- sex, age, height, weight
- primary goal and time horizon
- daily activity level
- weekly training availability
- equipment

### Coach Mode
Use when the user wants a structured plan, memory-aware coaching, or detailed trade-offs. Collect Quick Mode fields plus:

- training background and training age
- gym vs home preference
- sleep quality and stress level
- diet style and food preferences
- eating-out frequency and tracking willingness
- injuries, chronic issues, and hard boundaries
- current obstacles and past failures

### Log-Analysis Mode
Use when the user provides training logs, screenshots, body metrics, or nutrition records. Minimum fields depend on request type:

| Request | Minimum useful fields |
|---|---|
| Build first plan | Goal, weekly days, session length, training age, equipment, pain constraints |
| Modify current plan | Current split, exercises, sets, reps, load, RPE/RIR, schedule, stated problem |
| Analyze logs/screenshots | Date range, exercise names, sets/reps/load, body part or goal, recent trend |
| Fat-loss/recomposition | Weight trend, waist/photos if available, steps/cardio, lifting plan, sleep |
| Specialization | Target muscle, current weekly sets/frequency, target-muscle feel, joint tolerance |
| Powerlifting/strength | Current SBD/e1RM or recent top sets, RPE accuracy, timeline, sticking points |

## Coach Preference Intake
Ask:
- Do you want a specific coach style?
- Do you want one coach for everything or different coaches for strength, cardio, and recovery?
- Do you want to stay with the built-in profiles only, or should I also consider recent public content if needed?

## Profile Classification

| Signal | Classification | Programming consequence |
|---|---|---|
| No consistent lifting history | New trainee | Start simple, moderate volume, technique first |
| Returning after long break | Returning trainee | Use prior experience but lower initial volume/intensity |
| 3+ months consistent logs | Consistent trainee | Use trend-based adjustments |
| Performance down, sleep poor, soreness high | Fatigued trainee | Reduce volume/intensity before adding complexity |
| Pain, numbness, sharp symptoms | Safety flag | Do not prescribe through symptom; advise reduction/evaluation |
| Clear goal and reliable logs | Data-rich user | Make narrow, evidence-based changes |
| Vague goal and no logs | Data-sparse user | Give conservative starting plan and ask for 2-4 weeks of logs |

## Missing Data Rule

Ask questions only when the missing answer changes the recommendation. Avoid large intake interviews unless the user wants a full setup.

**Ask now when missing:**
- Training days/session length for any plan construction
- Equipment for exercise selection
- Pain/injury when movement safety matters
- Current plan/logs when the user asks "怎么修改"
- Weight/waist trend when diagnosing fat-loss plateau
- Current SBD or recent top sets when building powerlifting work

**Do not block the answer when missing:**
- Exact body fat percentage
- Perfect diet details for a training-only request
- Every exercise preference when a conservative first plan is enough
- API data if the user already provided usable text/screenshots

## Required Fields (by priority)

| Priority | Field | Why it matters |
|---|---|---|
| 1 | Primary goal and deadline | Determines goal module |
| 2 | Current training status | New, returning, consistent, stalled, fatigued |
| 3 | Weekly availability | Controls split choice and plan complexity |
| 4 | Equipment and load jumps | Controls exercise selection and progression increments |
| 5 | Current plan/logs | Best evidence for what to change |
| 6 | Recovery and pain | Controls volume, intensity, deload, substitutions, safety gate |
| 7 | Body metrics | Needed for fat loss/recomposition and visual shaping |
| 8 | Preferences and must-keep movements | Improves adherence without breaking programming logic |

Read `references/intake-fields.md` for the full field list and `references/user-profile-intake.md` (to be added in Phase 3) for structured intake templates.
