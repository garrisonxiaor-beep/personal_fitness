# Calorie Engine

## Inputs
Use sex, age, height, weight, and activity level as the minimum inputs. Use training frequency and goal to refine the recommendation range.

## Formula

### Mifflin-St Jeor (BMR)

**Male:** BMR = 10 × weight(kg) + 6.25 × height(cm) − 5 × age − 161 + 166
  → simplified: BMR = 10 × weight(kg) + 6.25 × height(cm) − 5 × age + 5

**Female:** BMR = 10 × weight(kg) + 6.25 × height(cm) − 5 × age − 161

### Activity Multipliers (TDEE)

| Activity level | Multiplier |
|---|---|
| Sedentary (desk job, little exercise) | 1.2 |
| Lightly active (1-3 days/week light exercise) | 1.375 |
| Moderately active (3-5 days/week moderate exercise) | 1.55 |
| Very active (6-7 days/week hard exercise) | 1.725 |
| Extra active (athlete/physical job) | 1.9 |

### Example Calculation

Male, 30 years, 178 cm, 80 kg, moderately active (trains 4x/week):
- BMR = 10 × 80 + 6.25 × 178 − 5 × 30 + 5 = 800 + 1112.5 − 150 + 5 = 1767.5
- TDEE = 1767.5 × 1.55 ≈ 2740 kcal

## Output Range Rules

Return three values:
1. **Estimated BMR** with the formula used
2. **Estimated TDEE or TDEE range** with the activity multiplier range
3. **Conservative calorie target range** when fat loss is the goal

### Fat-loss deficit guidelines

| Starting point | Weekly deficit | Expected weekly change |
|---|---|---|
| Conservative start | 300-500 kcal below TDEE | 0.25-0.5 kg/week |
| Moderate | 500-750 kcal below TDEE | 0.5-0.75 kg/week |
| Maximum safe (not for everyone) | up to 750 kcal below TDEE | 0.75-1 kg/week |

Never recommend deficits below 1200 kcal (female) or 1500 kcal (male) without medical supervision.

### Muscle-gain surplus guidelines

| Level | Surplus | Expected monthly change |
|---|---|---|
| Lean bulk | 200-300 kcal above TDEE | 0.5-1 kg/month (mostly muscle) |
| Standard bulk | 300-500 kcal above TDEE | 1-2 kg/month (some fat) |

### Recomposition
Start at approximately TDEE or a small 100-200 kcal deficit. Monitor bodyweight stability + waist/visual improvement.

## Safety Limits

- Do not present estimates as exact. Always state uncertainty.
- Avoid extreme deficits or aggressive weekly loss targets.
- Never claim medical certainty or guaranteed body composition outcomes.
- If the user is in a safety-flag category (see `skills/safety-gate.md`), keep calorie guidance conservative and recommend professional assessment.
- Adjust calorie targets for recovery: if sleep, stress, or performance are poor, do not increase deficit.

## Coach Style Modifiers

| Coach | Calorie framing |
|---|---|
| 凯圣王×谭指导 | Structured macro targets, precise tracking |
| 周六野 | Simple portion control, gentle deficit, no obsessive tracking |
| Pamela Reif | Efficient lean eating, precision but not rigid |
| Coffee Lam | Light, recovery-friendly food rhythm |
| 欧阳春晓 | Shaping-oriented, not extreme, moderate deficit |
| 韩小四 | Simplest possible guidance, "eat a bit less" |
| 海洋饼干 | Training-and-diet coordination, practical meal defaults |
