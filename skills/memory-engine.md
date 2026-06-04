# 记忆引擎

## 双记忆系统

本技能使用两套协同工作的记忆系统：

1. **Markdown 记忆**（轻量，始终可用）：`profiles/` 文件
2. **JSON 数据存储**（结构化，脚本支持）：`user-data/` 文件

## Markdown 记忆文件

### 健康档案（`profiles/<user_id>-health-profile.md`）
用途：持久用户事实和稳定倾向。

存储：
- 基础数据（年龄、性别、身高、体重、训练年限）
- 长期目标和目标优先级
- 活动习惯
- 训练偏好（包括教练风格偏好）
- 营养偏好
- 执行特征
- 风险边界
- 有效和无效的过往策略
- 偏好教练和混搭组合
- 公开增强偏好

### 健康进度（`profiles/<user_id>-health-progress.md`）
用途：近期状态和短期变更日志。

存储：
- 近期执行摘要
- 近期体重或腰围趋势
- 当前障碍
- 当前策略变更
- 下次计划应考虑什么

### 模板
见 `profiles/EXAMPLE-HEALTH-PROFILE.md` 和 `profiles/EXAMPLE-HEALTH-PROGRESS.md`。

## JSON 数据存储

对于想要跨会话持久化结构化数据的用户，使用 `user-data/` 和 `scripts/manage_user_data.py`。

### 数据文件
| 文件 | 用途 |
|---|---|
| `profile.json` | 目标、时间表、训练年限、器械、限制、偏好 |
| `training-history.json` | 已完成的训练和导入的日志 |
| `body-metrics-history.json` | 体重、腰围、测量、步数、睡眠、有氧 |
| `nutrition-history.json` | 餐食、热量、宏量营养素、饥饿、执行笔记 |

### 脚本命令
```bash
python3 scripts/manage_user_data.py init user-data
python3 scripts/manage_user_data.py import-training user-data workout-log.csv
python3 scripts/manage_user_data.py import-body user-data body-metrics.csv
python3 scripts/manage_user_data.py import-nutrition user-data nutrition-log.csv
python3 scripts/manage_user_data.py summary user-data
```

### 模板
见 `templates/user-data/` 获取初始 JSON 结构。

## 读取规则

生成建议前：
1. 如存在，加载档案（markdown 和/或 JSON）。
2. 如存在，加载进度笔记。
3. 如可用，加载相关历史（训练、身体数据、营养）。
4. 概括稳定习惯、偏好格式、近期障碍和已知边界。
5. 用记忆简化或个性化计划。

绝不假设记忆是最新的，除非检查了最新笔记内容。

## 写入规则

只写入持久或决策相关的信息。

### 保存
- 确认的长期目标
- 稳定的饮食和训练偏好
- 教练风格偏好和混搭组合
- 反复出现的习惯模式
- 执行优势和失败模式
- 重要的安全边界
- 明确有效或无效的策略
- 训练历史、身体数据和营养日志（通过 JSON 存储）

### 不保存
- 原始对话文本
- 一次性情绪
- 偶尔的糟糕一餐
- 未确认的猜测
- 短暂闲聊

## 更新操作

- **追加**：添加新的近期观察
- **覆盖**：替换明显改变的稳定事实
- **汇总**：将重复的近期笔记压缩为更高层级的模式

## 记忆如何改变建议

- 经常外食 → 偏好餐厅友好启发法而非精确饮食计划
- 追踪意愿低 → 避免详细宏量规则
- 居家训练偏好 → 偏好徒手或最少器械计划
- 复杂计划反复失败 → 先简化
- 高执行力和训练基础 → 允许更高级的营养结构
- 高压力或睡眠差 → 降低训练野心，保持热量缺口保守
- 教练风格偏好 → 在所有输出中应用匹配的教练叠加
- 近期表现趋势 → 据此调整训练量/强度/进阶
