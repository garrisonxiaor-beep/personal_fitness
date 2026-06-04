# 个人健身教练

分层健身技能工作空间，结合**教练风格个性化**与**系统化训练编程**。支持增肌、减脂/重塑、部位专攻和力量举，配备命名教练档案、模块化引擎、内置动作库和可选的长期用户数据持久化。

## 这是什么

一个结构化健康教练技能，能够：

- 将用户健身数据转化为目标导向、教练风格个性化的建议
- 覆盖四大编程领域：增肌、减脂/重塑、部位专攻、力量举
- 提供详细的分化指导：二分化、三分化/PPL、四分化、五分化
- 支持命名教练风格（周六野、Pamela Reif、凯圣王×谭指导 等）及混搭
- 包含内置动作库，支持别名匹配和替换逻辑
- 可选地跨会话持久化用户数据

## 仓库结构

```
├── SKILL.md                              # 根编排器
├── agents/openai.yaml                    # Codex/OpenAI UI 元数据
├── profiles/                             # 用户记忆模板
├── skills/                               # 决策引擎（9 个模块）
│   ├── intake-engine.md                  # 信息收集
│   ├── safety-gate.md                    # 安全筛查
│   ├── calorie-engine.md                 # 热量估算
│   ├── nutrition-engine.md               # 营养策略
│   ├── training-engine.md                # 训练 + 目标模块路由
│   ├── exercise-engine.md                # 动作选择 + 匹配
│   ├── memory-engine.md                  # 记忆读写
│   ├── adjustment-engine.md              # 计划调整 + 决策树
│   └── coach-research-engine.md          # 可选教练增强
├── coach_profiles/                       # 7 个命名教练档案
├── coach_research_notes/                 # 可选公开内容增强
├── data/exercise-library.json            # 内置动作库（147+ 动作）
├── references/                           # 领域规则和指南
│   ├── training-algorithm-library.md     # 共享编程规则
│   ├── recommendation-decision-tree.md   # 瓶颈 → 最小行动
│   ├── goal-hypertrophy.md               # 增肌模块
│   ├── goal-fat-loss-recomposition.md    # 减脂模块
│   ├── goal-specialization.md            # 专攻模块
│   ├── goal-powerlifting.md              # 力量举模块
│   ├── hypertrophy-splits.md             # 分化选择器
│   ├── split-two-division.md             # 二分化进阶
│   ├── ppl-practical.md                  # 三分化/PPL 进阶
│   ├── split-four-division.md            # 四分化进阶
│   ├── split-five-division.md            # 五分化进阶
│   ├── fat-loss-recomposition-advanced.md
│   ├── specialization-advanced.md
│   ├── powerlifting-advanced.md
│   ├── exercise-library-schema.md
│   ├── coach-style-guide.md
│   ├── coach-research-policy.md
│   └── ... 更多参考文档
├── scripts/                              # Python 工具
│   ├── setup_exercise_db.py              # 外部数据库设置
│   ├── query_exercises.py                # 动作查询
│   ├── manage_user_data.py               # 用户数据管理
│   └── summarize_training_logs.py        # 训练日志汇总
├── examples/                             # 使用示例
└── templates/                            # 信息收集和数据模板
```

## 选择你的教练

| 教练 | 偏重 | 最适合 |
|---|---|---|
| 凯圣王×谭指导 | 力量增长 / 三分化 | 想系统练力量和增肌的人 |
| 周六野 | 塑形 / 减脂 | 新手到中级 |
| Pamela Reif | HIIT / 全身塑形 | 有基础、追求效率 |
| Coffee Lam | 瑜伽 / 拉伸 | 喜欢柔韧和恢复 |
| 欧阳春晓 | 瘦腿 / 体态 | 关注腿型与姿态 |
| 韩小四 | 温和减脂 | 零基础、怕受伤 |
| 海洋饼干 | 减脂 / 全身塑形 | 中等强度，训练饮食并重 |

## 混搭教练模式

你可以按领域混搭教练：力量日用凯圣王×谭指导，有氧用 Pamela Reif，恢复用 Coffee Lam。

## 目标模块

| 目标 | 模块 | 进阶参考 |
|---|---|---|
| 增肌 / Hypertrophy | `goal-hypertrophy.md` + 分化指南 | `ppl-practical.md`、`split-*-division.md` |
| 减脂 / Fat Loss | `goal-fat-loss-recomposition.md` | `fat-loss-recomposition-advanced.md` |
| 部位专攻 / Specialization | `goal-specialization.md` | `specialization-advanced.md` |
| 力量举 / Powerlifting | `goal-powerlifting.md` | `powerlifting-advanced.md` |

## 动作数据库和图片查询

内置库：`data/exercise-library.json`（始终可用，147+ 动作）。

外部数据库（可选，用于图片查询）：
```bash
python3 scripts/setup_exercise_db.py
python3 scripts/setup_exercise_db.py --check-db
python3 scripts/query_exercises.py --muscle chest --equipment dumbbell
python3 scripts/query_exercises.py --id Incline_Dumbbell_Press --detailed
```

## 决策框架

每次计划修改遵循 `references/recommendation-decision-tree.md`：
1. 诊断瓶颈（刺激不足、过度疲劳、技术不匹配等）
2. 选择最小有效改变
3. 定义接下来 2-6 周的可量化指标

## 可选公开网络增强

静态教练档案是默认来源。公开网络增强是可选的，仅在用户明确要求更新公开内容或更深教练细节时使用。

## 快速开始

1. 阅读 `SKILL.md` 了解编排流程。
2. 使用 `skills/` 作为决策引擎，`references/` 作为领域规则，`coach_profiles/` 选择风格。
3. 使用 `data/exercise-library.json` 进行动作选择。
4. 仅在需要图片查询时初始化外部动作数据库。

## 无外部数据库时的降级模式

如外部数据库缺失，系统仍可使用内置库提供完整的动作指导，并说明如何初始化 `exercise-db/`。
