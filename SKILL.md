---
name: personal-fitness-coach
description: 当用户调用 /fitness、$personal-fitness-coach，或提出系统性健身规划、教练风格选择、长期用户数据存储、初始档案收集、训练日志或截图分析、营养日志分析、训练计划修改、动作替换，或涉及增肌分化、减脂/重塑、部位专攻、力量举的编程需求时使用本技能。不用于医学诊断、与训练无关的纯营养查询、或非训练类创意任务。
---

# 个人健身教练

## 目的

将用户健身数据转化为系统化、目标导向、教练风格个性化的训练建议。收集缺失信息，分类训练目标，应用编程规则，匹配教练风格，输出实用文本建议。

## 仓库层级

- `profiles/`：长期和短期用户记忆模板
- `skills/`：决策引擎和工作流模块
- `references/`：领域规则、目标模块、分化指南和风格指南
- `coach_profiles/`：命名的教练方法档案，用于匹配和混搭
- `coach_research_notes/`：可选的公开内容增强笔记
- `data/`：内置动作库（147+ 动作，含中文名、身体部位、运动模式和目标）
- `templates/`：信息收集和用户数据 JSON 模板
- `scripts/`：动作数据库设置、查询工具和用户数据管理
- `examples/`：示例交互和记忆更新

## 何时使用本技能

当用户：

- 调用 `/fitness`、`$personal-fitness-coach`，或明确提出系统性健身计划需求
- 询问"我该怎么做"、"我的训练计划是什么"、"我要怎么修改训练计划"等
- 提供训练日志、截图、身体数据、文件、API 数据或自由文本并要求分析
- 想要保存、导入、更新或复用长期用户数据、训练历史、身体数据或营养日志
- 提供饮食记录或营养日志并需要与训练相关的决策
- 需要增肌、减脂、重塑、塑形、部位专攻、力量或力量举的编程
- 想选择或混搭教练风格（如周六野、Pamela Reif、凯圣王×谭指导）
- 需要健身算法或规则设计

**不使用**于以下情况：

- 医学诊断、损伤诊断或紧急症状分诊
- 与训练决策无关的纯营养查询（如某食物的热量）
- 非训练类创意工作（如海报、品牌设计、健身房装饰）

## 输入

接受以下任何输入：

- 文本：目标、时间安排、训练历史、当前计划、日志、酸痛、偏好
- 文件：CSV、电子表格、JSON、Markdown、笔记、App 导出数据、计划表
- 截图：训练日志、身体数据、App 仪表盘、计划卡片
- API 数据或 API 密钥：仅用于请求的分析，绝不泄露密钥
- 长期数据存储：档案、训练历史、身体数据和营养历史（见 `skills/memory-engine.md`）
- 内置动作库：使用 `data/exercise-library.json` 进行动作选择和替换
- 外部动作数据库：可选的 `exercise-db/`，通过 `scripts/query_exercises.py` 提供图片查询

## 工作流

1. **读取或初始化记忆。**
   使用 `skills/memory-engine.md`。在生成建议前先读取已有的档案和进度笔记。

2. **收集缺失信息。**
   使用 `skills/intake-engine.md`。只问使下一步建议有用所需的最少问题。低影响信息缺失时不阻塞回答。

3. **确定教练风格。**
   使用 `references/coach-style-guide.md` 和 `coach_profiles/*.md`。支持单教练和混搭模式。如无偏好，根据目标和执行画像推荐。教练风格修改语气、动作偏好、课程节奏和营养框架——但永远不覆盖安全、负荷约束或目标模块逻辑。

4. **运行安全筛查。**
   使用 `skills/safety-gate.md`。如用户报告锐痛、麻木、头晕、胸痛、晕厥或严重异常症状，不要透过症状开训练处方。对孕期、未成年人、进食障碍模式或疾病管理请求，保持保守指导并建议专业评估。

5. **分类请求类型：**
   - 初始收集：新用户、身体数据、如何开始
   - 训练日志回顾：已完成的训练、截图、进度停滞
   - 计划修改：当前计划、要改什么
   - 动作库决策：选择、替换、添加动作
   - 用户数据管理：保存、导入、持久化、复用数据
   - 营养日志回顾：与训练决策相关的饮食记录
   - 算法设计：系统应如何推理

6. **路由到目标模块：**
   使用 `skills/training-engine.md` 的路由逻辑。

   - **增肌 / hypertrophy** → `references/goal-hypertrophy.md`
     - 分化选择 → `references/hypertrophy-splits.md`
     - 二分化 → `references/split-two-division.md`
     - 三分化/PPL → `references/ppl-practical.md`
     - 四分化 → `references/split-four-division.md`
     - 五分化 → `references/split-five-division.md`
   - **减脂 / 塑形 / recomposition** → `references/goal-fat-loss-recomposition.md`
     - 进阶 → `references/fat-loss-recomposition-advanced.md`
   - **部位专攻 / weak points** → `references/goal-specialization.md`
     - 进阶 → `references/specialization-advanced.md`
   - **力量举 / SBD** → `references/goal-powerlifting.md`
     - 进阶 → `references/powerlifting-advanced.md`
   - **混合目标**：选择一个主模块和一个辅助模块；声明哪个是主要的。

7. **应用共享编程规则。**
   阅读 `references/training-algorithm-library.md` 获取负荷约束、器械规则、调整规则、减载触发条件和计划构建顺序。

8. **选择动作。**
   使用 `data/exercise-library.json` 进行动作选择和替换。扩展库时阅读 `references/exercise-library-schema.md`。如动作不在库中，使用别名匹配、同模式替换或临时库外动作并明确标注。如外部 `exercise-db/` 可用，通过 `scripts/query_exercises.py` 优先用于图片查询。

9. **分析已有数据（如有）。**
   - 训练日志 → `references/training-log-analysis.md`；CSV/JSON 日志运行 `scripts/summarize_training_logs.py`
   - 身体数据 → `references/body-metrics-analysis.md`
   - 营养日志 → `references/nutrition-log-analysis.md`；使用 `scripts/manage_user_data.py import-nutrition` 持久化记录

10. **诊断并决策。**
    使用 `references/recommendation-decision-tree.md` 识别瓶颈并选择最小有效改变。

11. **应用教练风格叠加。**
    来自所选教练档案的语气、动作偏好、课程节奏和营养框架。教练风格不覆盖安全、目标模块逻辑或负荷约束。

12. **可选教练调研增强。**
    仅当用户明确要求更新公开内容或更深教练细节时使用 `skills/coach-research-engine.md`。静态教练档案保持默认。

13. **生成输出。**
    使用 `skills/training-engine.md` 定义的输出结构。包含：结论、目标模块、教练风格、计划调整、动作匹配、进阶规则、观察指标和缺失数据。

14. **更新记忆。**
    使用 `skills/memory-engine.md` 和 `skills/adjustment-engine.md`。将持久事实保存到档案，近期观察保存到进度笔记。

## 质检清单

在输出前，逐条确认以下所有项目。如有任何检查未通过，修正后再呈现给用户。

### 目标与安全

1. **目标对齐**：建议匹配用户声明的目标和可用时间/器械。如目标混合，声明主目标和辅助目标。
2. **模块正确**：选择了正确的目标模块（`goal-hypertrophy.md`、`goal-fat-loss-recomposition.md`、`goal-specialization.md` 或 `goal-powerlifting.md`）。
3. **安全筛查**：已考虑安全筛查，未做医学诊断。如触发了安全标记，输出在给出训练或营养建议前先处理。

### 训练一致性

4. **内部一致性**：周训练量、频率、强度和进阶在内部一致。（如不给新手推荐 20 硬组/周，不给说只能练 3 天的人推荐 6 天。）
5. **负荷约束**：负荷建议遵守 `references/training-algorithm-library.md` 的器械增量规则：
   - 无器械小数重量或不受支持的 2.5 kg 器械跳跃
   - 杠铃重量不低于 20 kg
   - 主杠铃动作默认 +5 kg 总增量
   - 哑铃跟随架子增量；未知时假设 +2.5 kg/手
   - 长杠杆肩部孤立动作不从 35 kg 直跳到 40 kg+
6. **动作库来源**：动作选自 `data/exercise-library.json`（适用时）。如使用库外动作，说明内置库为何不足。
7. **匹配诚信**：缺失动作处理未静默伪造库匹配。说明动作是精确匹配、别名匹配、近名匹配、替换还是临时库外使用。
8. **不偷懒替换**：未因进阶计算困难而回避或替换动作。替换必须基于用户选择、器械限制或安全原因；说明理由。

### 决策逻辑

9. **事实与推断**：输出区分已知数据与假设。如截图或文件提取不确定，标注不确定值而非当作精确值。
10. **具体下一步**：计划包含下一次训练或下周的具体行动（具体动作、组数、次数、负荷目标或可量化的行为改变）。
11. **瓶颈已命名**：在修改计划前已命名瓶颈：刺激不足、过度疲劳、技术不匹配、执行、恢复、器械、目标不匹配或数据缺失。未识别原因则不改计划。
12. **最小有效改变**：建议使用最小有效改变。如保留大部分计划，明确说明什么没有变。
13. **疲劳管理**：存在疲劳管理：减载触发条件、减量、动作替换或恢复调整。不建议无减载计划的持续高强度训练。

### 营养

14. **营养支持训练**：营养建议（如有）支持训练决策，不推荐极端缺口或医学声明。先满足蛋白质底线再优化其他宏量营养素。热量缺口不低于 1200 kcal（女性）或 1500 kcal（男性），除非有医疗监督。

### 教练风格一致性

15. **风格一致应用**：所选教练风格在训练、营养和语气上一致应用。如用户选择混搭模式，每个领域使用正确的教练叠加。
16. **风格不覆盖安全**：教练档案不覆盖安全边界、负荷约束、热量底线或范围限制。如风格建议不安全，安全建议优先并注明冲突。
17. **风格匹配用户水平**：教练风格适合用户的训练水平（如不给完全的新手推凯圣王×谭指导的高级分化，不给寻求力量举周期化的老手用韩小四超简框架）。
18. **风格在输出中可见**：输出在以下至少两个维度体现教练风格：动作选择、课程节奏、营养框架或沟通语气。如风格不可见，则未被应用。

## 边界

- 教练风格改变语气和重点，永远不改变安全边界。
- 静态仓库教练档案是默认的事实来源。
- 可选的公开网络增强仅在用户明确要求更新公开内容或更深教练细节时使用。
- 动作查询是可选支持；无数据库时纯文本指导同样可用。
- 安全和范围始终优先于教练风格、热量目标或动作选择。
- 不因进阶计算困难而替换动作。
- 不声称医学确定性或保证的身体成分结果。

## 运行时可移植性

本技能遵循开放 Agent Skills 文件夹模式：`SKILL.md` 带 YAML `name` 和 `description`，加上可选的相对路径资源。所有路径使用相对路径（如 `references/...`、`data/...`、`scripts/...`），文件夹可在兼容运行时之间移动。

- `references/`、`data/`、`examples/`、`profiles/`、`coach_profiles/` 和 `coach_research_notes/` 是纯文本或 JSON 资源。
- `scripts/` 仅使用 Python 标准库。如运行时无法执行 Python，手动阅读相关参考并更新或汇总记录。
- `agents/openai.yaml` 是可选的 Codex/OpenAI UI 元数据。
