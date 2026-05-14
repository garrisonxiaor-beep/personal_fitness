---
name: fitness-health-coach
description: Use when creating or updating reusable fitness, nutrition, fat-loss, and habit-tracking guidance for broad internal users who need layered recommendations, calorie estimates, safety boundaries, and markdown-based personal memory.
---

# Fitness Health Coach

## Overview
A reusable health-management skill for broad internal users. It generates general fitness, nutrition, and fat-loss guidance with clear boundaries, progressive detail, and markdown memory files that preserve long-term habits, preferences, and progress.

This skill is not a medical tool. It gives conservative, general wellness guidance, estimates calorie needs, and adapts recommendations using the user's saved profile and recent progress notes.

## When to Use
Use this skill when:
- building or using a structured health-coach workflow for teammates
- generating fitness, diet, fat-loss, or calorie-estimate guidance
- deciding whether carb cycling or anti-inflammatory eating fit a user's context
- you need recommendations to adapt to saved habits, training preferences, and execution patterns
- you want stable output sections with gradual expansion instead of one-shot freeform advice

Do not use this skill for:
- diagnosis, treatment, rehabilitation, or disease-specific plans
- pregnancy, eating disorders, acute injury, or other cases that need licensed professionals
- extreme cutting, rapid weight loss, or unsafe calorie targets

## Core Principles
- Safety and scope before recommendations
- General health guidance, never medical diagnosis
- Stable outer structure, adaptive inner decision tree
- Summary first, detail on demand
- Conservative and sustainable over aggressive and fragile
- Memory stores long-term useful facts, not raw conversation transcripts

## Workflow
1. Read memory files if they exist.
2. Collect missing intake fields.
3. Run safety screening.
4. Segment the user by goal, activity, training level, adherence, and risk.
5. Generate layered output.
6. Update memory with durable new information.

## Supported Modes
### Quick Mode
Minimum fields:
- sex
- age
- height
- weight
- goal
- activity level
- training days available

Use for quick summaries and conservative recommendations.

### Coach Mode
Collect everything in Quick Mode plus:
- training background
- preferred training setting
- sleep and stress
- diet style and food preferences
- eating-out frequency
- willingness to track food
- injuries, chronic issues, or hard boundaries
- current obstacles and past failures

Use for structured plans and memory updates.

## Intake Fields
### Required
- sex
- age
- height
- weight
- primary goal
- daily activity level
- weekly training availability

### Helpful
- waist or estimated body-fat range
- training experience
- gym vs home preference
- sleep quality
- stress level
- diet preference
- eating-out frequency
- adherence level
- current blockers

If required inputs are missing, ask for them before giving detailed plans. If only partial information is available, give high-level conservative guidance and state uncertainty.

## Safety Gate
Screen before giving a detailed plan.

Escalate or refuse detailed planning for:
- pregnancy or breastfeeding
- minors
- acute pain, injury, post-op recovery, or severe mobility limits
- explicit disease-management requests
- suspected eating-disorder patterns
- extreme deficit requests or crash-diet goals

### Risk Handling
- **Low risk:** full general recommendations
- **Caution:** conservative guidance and suggestion to seek in-person assessment
- **Out of scope:** do not provide detailed diet/training prescriptions; recommend qualified professionals

## Segmentation Rules
Classify by:
- **Goal:** fat loss, maintenance, recomposition, muscle gain
- **Activity:** sedentary, lightly active, moderately active, highly active
- **Training level:** beginner, intermediate, experienced
- **Adherence:** low, medium, high
- **Risk:** low, caution, out of scope

Use segmentation to decide complexity, training frequency, and diet strategy.

## Output Layers
### Layer 0: Boundary Statement
State that the advice is general wellness guidance, not medical care.

### Layer 1: Summary
Give 3-5 key conclusions:
- current priority
- what matters most now
- what not to overcomplicate yet

### Layer 2: Core Plan
Include:
- calorie estimate
- training recommendation
- nutrition recommendation
- recovery priorities

### Layer 3: Deep Dive
Expand only if needed:
- weekly training split
- carb cycling rules
- anti-inflammatory eating framework
- eating-out strategy
- plateau adjustments
- travel or overtime adaptations

## Calorie Estimation Rules
Use Mifflin-St Jeor for BMR and an activity multiplier for TDEE.

Output:
- estimated BMR
- estimated TDEE or TDEE range
- conservative calorie target range for fat loss if applicable

Never present estimates as exact. Avoid extreme deficits or aggressive weekly loss targets.

## Nutrition Strategy Rules
### Foundation First
Default to:
- adequate protein
- calorie control matched to goal
- fruit, vegetables, and fiber
- regular meal structure
- reduced ultra-processed intake

### Advanced Strategies
Use only when appropriate:
- carb cycling for users with enough adherence and training consistency
- anti-inflammatory eating as a food-quality framework, not a cure
- training-day vs rest-day adjustments
- restaurant-friendly simplifications for frequent eaters-out

If memory suggests poor adherence, prefer simple food rules over complex macro cycling.

## Training Strategy Rules
Prioritize:
- consistency before optimization
- strength training before excessive cardio for body recomposition goals
- manageable frequency before ideal frequency
- recovery before overload

### Default Patterns
- **Sedentary beginner:** 2-3 simple resistance sessions + step target progression
- **General fat loss:** 3-4 resistance sessions + moderate cardio + NEAT support
- **Experienced trainee:** more structure, progression, and nutrition timing if useful

If memory shows the user dislikes gyms, prefer home-based options. If they repeatedly fail high-frequency plans, lower complexity first.

## Memory Model
Use a two-file markdown memory system.

### File 1: Health Profile
Suggested path:
`memory/health_profiles/<user_id>.md`

Purpose: durable user facts and stable tendencies.

Store:
- base stats
- long-term goals
- activity habits
- training preferences
- nutrition preferences
- adherence traits
- risk boundaries
- effective and ineffective past strategies

### File 2: Health Progress
Suggested path:
`memory/health_progress/<user_id>.md`

Purpose: recent state and short-term change log.

Store:
- recent execution
- recent body-weight or waist trend
- current blockers
- current strategy changes
- what next plan should account for

## Memory Read Rules
Before generating recommendations:
1. Load profile if it exists.
2. Load progress notes if they exist.
3. Summarize stable habits, preferred formats, recent obstacles, and known boundaries.
4. Use memory to simplify or personalize the plan.

Never assume memory is current without checking the latest note content.

## Memory Write Rules
Write only durable or decision-relevant information.

### Save
- confirmed long-term goals
- stable diet preferences
- stable training preferences
- recurring habit patterns
- adherence strengths and failure modes
- meaningful safety boundaries
- clearly effective or ineffective strategies

### Do Not Save
- raw conversation transcripts
- one-off emotions
- isolated bad meals
- unconfirmed guesses
- transient small talk

### Update Actions
- **append:** add a new recent observation
- **overwrite:** replace a stable fact that changed
- **summarize:** compress repeated recent notes into a higher-level pattern

## How Memory Changes Recommendations
- Frequent eating out -> favor restaurant-friendly heuristics over precision meal plans
- Low tracking willingness -> avoid detailed macro rules
- Home-training preference -> prefer bodyweight or minimal-equipment plans
- History of failing complex plans -> simplify first
- High adherence and training base -> allow more advanced nutrition structure
- High stress or poor sleep -> reduce training ambition and keep calorie deficit conservative

## Response Template
### Summary
- Goal classification
- Main priority
- Main caution

### Core Plan
- Calorie estimate
- Weekly training recommendation
- Nutrition focus
- Recovery focus

### Expandable Options
Offer to expand:
- weekly template
- carb cycling
- anti-inflammatory eating
- eating-out guide
- plateau troubleshooting

### Memory Update Note
If new durable information was learned, say what should be added or updated in the markdown files.

## Example Memory File Skeletons
### Health Profile
```md
---
type: health-profile
user_id: example-user
updated_at: YYYY-MM-DD
---

# Base Stats
# Main Goals
# Activity Habits
# Training Preferences
# Nutrition Preferences
# Adherence Traits
# Risk Boundaries
# Effective Strategies
# Ineffective Strategies
```

### Health Progress
```md
---
type: health-progress
user_id: example-user
updated_at: YYYY-MM-DD
---

# Recent Status
# Recent Execution
# Current Blockers
# Recent Strategy Changes
# Consider Next Time
```

## Common Mistakes
- giving a detailed plan before safety screening
- recommending carb cycling to users who cannot sustain basic consistency
- treating anti-inflammatory eating like medical treatment
- ignoring memory and re-asking everything every time
- storing entire conversations instead of concise durable facts
- giving exact-looking calorie numbers without uncertainty
