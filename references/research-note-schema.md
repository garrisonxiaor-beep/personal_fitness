# 调研笔记结构

## 目的
Use this schema for files under `coach_research_notes/<coach>.md` that capture optional public-content augmentation for a named coach.

## 必填章节
Every research note should contain:
- `# <Coach Name> Research Augmentation`
- `## Research Status`
- `## Public Content Signals`
- `## Reinforced Style Notes`
- `## Source Caveats`
- `## Integration Notes`

## 新鲜度和置信度字段
Under `## Research Status`, include:
- `source mode: public-web` or `source mode: douyin+public-web`
- `freshness: YYYY-MM-DD`
- `confidence: low / medium / high`
- `usage: optional augmentation only`

## 写作规则
- Write directional observations, not absolute truths.
- Do not claim medical authority, certification, or complete methodology from public samples.
- Keep static `coach_profiles/*.md` as the baseline.
- Use caveats when the sample window is narrow or old.
