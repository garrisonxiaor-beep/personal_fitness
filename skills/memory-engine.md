# Memory Engine

## Dual Memory System

This skill uses two memory systems that work together:

1. **Markdown memory** (lightweight, always available): `profiles/` files
2. **JSON data store** (structured, script-supported): `user-data/` files

## Markdown Memory Files

### Health Profile (`profiles/<user_id>-health-profile.md`)
Purpose: durable user facts and stable tendencies.

Store:
- base stats (age, sex, height, weight, training age)
- long-term goals and goal priority
- activity habits
- training preferences (including coach style preference)
- nutrition preferences
- adherence traits
- risk boundaries
- effective and ineffective past strategies
- preferred coach and mixed-coach composition
- web augmentation preference

### Health Progress (`profiles/<user_id>-health-progress.md`)
Purpose: recent state and short-term change log.

Store:
- recent execution summary
- recent body-weight or waist trend
- current blockers
- current strategy changes
- what next plan should account for

### Template
See `profiles/EXAMPLE-HEALTH-PROFILE.md` and `profiles/EXAMPLE-HEALTH-PROGRESS.md`.

## JSON Data Store

For users who want persistent structured data across sessions, use `user-data/` with `scripts/manage_user_data.py`.

### Data files
| File | Purpose |
|---|---|
| `profile.json` | Goal, schedule, training age, equipment, constraints, preferences |
| `training-history.json` | Completed workouts and imported logs |
| `body-metrics-history.json` | Weight, waist, measurements, steps, sleep, cardio |
| `nutrition-history.json` | Meals, calories, macros, hunger, adherence notes |

### Script commands
```bash
python3 scripts/manage_user_data.py init user-data
python3 scripts/manage_user_data.py import-training user-data workout-log.csv
python3 scripts/manage_user_data.py import-body user-data body-metrics.csv
python3 scripts/manage_user_data.py import-nutrition user-data nutrition-log.csv
python3 scripts/manage_user_data.py summary user-data
```

### Templates
See `templates/user-data/` for initial JSON structures.

## Read Rules

Before generating recommendations:
1. Load profile (markdown and/or JSON) if it exists.
2. Load progress notes if they exist.
3. Load relevant history (training, body metrics, nutrition) if available.
4. Summarize stable habits, preferred formats, recent obstacles, and known boundaries.
5. Use memory to simplify or personalize the plan.

Never assume memory is current without checking the latest note content.

## Write Rules

Write only durable or decision-relevant information.

### Save
- confirmed long-term goals
- stable diet and training preferences
- coach style preference and mixed-coach composition
- recurring habit patterns
- adherence strengths and failure modes
- meaningful safety boundaries
- clearly effective or ineffective strategies
- training history, body metrics, and nutrition logs (via JSON store)

### Do Not Save
- raw conversation transcripts
- one-off emotions
- isolated bad meals
- unconfirmed guesses
- transient small talk

## Update Actions

- **append:** add a new recent observation
- **overwrite:** replace a stable fact that clearly changed
- **summarize:** compress repeated recent notes into a higher-level pattern

## How Memory Changes Recommendations

- Frequent eating out → favor restaurant-friendly heuristics over precision meal plans
- Low tracking willingness → avoid detailed macro rules
- Home-training preference → prefer bodyweight or minimal-equipment plans
- History of failing complex plans → simplify first
- High adherence and training base → allow more advanced nutrition structure
- High stress or poor sleep → reduce training ambition and keep calorie deficit conservative
- Coach style preference → apply matching coach overlay to all outputs
- Recent performance trend → adjust volume/intensity/progression accordingly
