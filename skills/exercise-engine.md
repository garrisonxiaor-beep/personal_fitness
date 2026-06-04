# 动作引擎

## 何时使用
当用户询问特定动作、需要动作示例、需要动作替换或需要本地数据库的图片查询时使用。

## 双数据源

本技能有两个动作数据源：

1. **内置库**：`data/exercise-library.json`（147+ 动作，含中文名、身体部位、运动模式、器械和目标）。始终可用。阅读 `references/exercise-library-schema.md` 了解数据结构。

2. **外部数据库**：`exercise-db/`（来自 free-exercise-db 的 800+ 动作及图片）。可选。通过 `scripts/query_exercises.py` 访问。提供图片查询。

## 动作匹配流程

在选择、替换或轮换动作时：

1. **精确匹配**：`data/exercise-library.json` 中的精确名称
2. **别名匹配**：精选别名，如 臀推 → 史密斯臀冲，RDL → 罗马尼亚硬拉
3. **近名匹配**：明确包含请求名称的唯一库动作
4. **同模式替换**：相同身体部位、器械和运动模式
5. **库外回退**：允许临时库外动作，但明确说明原因及内置库为何不足
6. 当动作似乎反复出现或重要时，询问用户是否要添加到库中

不因动作库不完整而拒绝构建建议。不将模糊或未匹配的动作呈现为已确认的库条目。

## 图片路径输出

当外部 `exercise-db/` 数据库可用且匹配动作包含图片路径时，返回本地图片路径及动作名称。

使用查询脚本：
```bash
python3 scripts/query_exercises.py --muscle chest --equipment dumbbell
python3 scripts/query_exercises.py --id "Incline_Dumbbell_Press" --detailed
```

## 无数据库时的降级

如外部数据库不可用，使用内置 `data/exercise-library.json` 提供纯文本动作指导，并说明如何初始化外部数据库：
```bash
python3 scripts/setup_exercise_db.py
```

## 动作选择规则

构建计划时：
1. 优先选择匹配用户目标身体部位、器械、运动模式、目标和限制的动作。
2. 应用 `references/training-algorithm-library.md` 的负荷和器械约束。
3. 使用 `coach_profiles/*.md` 的教练风格偏好影响动作选择（如凯圣王偏好杠铃复合动作；周六野偏好徒手/哑铃入门友好动作）。
4. 不因进阶计算困难而替换动作。

## 匹配类型报告

在输出中报告动作匹配状态：
- **精确匹配**：直接库匹配
- **别名匹配**：通过精选别名匹配
- **替换**：同模式替换
- **库外**：临时使用，说明原因
- **模糊**：多个候选，需用户确认
- **未匹配**：无库候选，需用户指导
