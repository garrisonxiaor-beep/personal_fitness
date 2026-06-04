# Calorie Engine

## Inputs
Use sex, age, height, weight, and activity level as the minimum inputs. Use training frequency and goal to refine the recommendation range.

## Formula

### Mifflin-St Jeor (BMR)

**Male:** BMR = 10 × weight(kg) + 6.25 × height(cm) − 5 × age + 5

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

## Macro Distribution from Calorie Target

Once total calories are set, distribute to macros using `skills/nutrition-engine.md` for goal-specific targets.

### Quick allocation method

1. Set protein first: goal × bodyweight (kg) = protein grams × 4 = protein calories
2. Set fat floor: 0.7-1.0 g/kg × bodyweight (kg) = fat grams × 9 = fat calories
3. Remaining calories → carbs (divide by 4 for grams)

### Example

Male, 80 kg, fat loss, TDEE 2740, target 2240 kcal (500 deficit):
- Protein: 2.0 g/kg × 80 = 160 g × 4 = 640 kcal
- Fat: 0.8 g/kg × 80 = 64 g × 9 = 576 kcal
- Remaining: 2240 − 640 − 576 = 1024 kcal → 256 g carbs

### Adjustment priority

When adjusting calories:
1. **Increase deficit**: reduce carbs first, keep protein and fat stable
2. **Increase surplus**: add carbs first, small fat increase if needed
3. **Never cut protein to save calories** during any deficit
4. **Do not push fats below 0.6 g/kg** without medical supervision

## Safety Limits

- Do not present estimates as exact. Always state uncertainty.
- Avoid extreme deficits or aggressive weekly loss targets.
- Never claim medical certainty or guaranteed body composition outcomes.
- If the user is in a safety-flag category (see `skills/safety-gate.md`), keep calorie guidance conservative and recommend professional assessment.
- Adjust calorie targets for recovery: if sleep, stress, or performance are poor, do not increase deficit.

## Coach Style Modifiers

| Coach | Calorie framing | Tracking expectation |
|---|---|---|
| 凯圣王×谭指导 | Structured macro targets, precise tracking | 期望追踪宏量营养素 |
| 周六野 | Simple portion control, gentle deficit | 关注份量，不强调追踪 |
| Pamela Reif | Efficient lean eating, precision but not rigid | 高效记录，不过度纠结 |
| Coffee Lam | Light, recovery-friendly food rhythm | 不强调严格追踪 |
| 欧阳春晓 | Shaping-oriented, not extreme, moderate deficit | 简单记录 |
| 韩小四 | Simplest possible guidance, "eat a bit less" | 完全不追踪，只管少吃 |
| 海洋饼干 | Training-and-diet coordination, practical meal defaults | 中等记录，外食有默认选择 |
