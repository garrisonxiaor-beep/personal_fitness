# Coach Research Augmentation Design

> Add an optional public-web / Douyin research augmentation layer on top of static coach profiles so the repository can answer coach-selection questions with fresher public-content nuance without replacing the core markdown source of truth.

## Goal

Extend the existing layered fitness coach skill so it can optionally incorporate recent public coach signals when the user explicitly asks for deeper, newer, or platform-specific coach detail.

## Current Baseline

The repository already has:

- `coach_profiles/*.md` as the primary coach source of truth
- `references/coach-style-guide.md` for selection and mixing rules
- `references/coach-research-policy.md` stating that public-web augmentation is optional and user-triggered
- `SKILL.md` and `README.md` that mention optional public-web augmentation, but no dedicated workflow or file layer yet

## Recommended Approach

Add a dedicated **coach research augmentation layer** rather than folding public research into the static coach profiles.

This layer should:

- keep `coach_profiles/*.md` as the default baseline
- only activate when the user explicitly requests newer public content, deeper nuance, or Douyin / web augmentation
- store reusable research observations in markdown files
- label freshness and confidence explicitly
- fall back cleanly to static profiles when no research note exists or no public results are available

## Architecture

### New Repository Layer

Add a new directory:

- `coach_research_notes/` — optional augmentation notes for named coaches

Each file represents one coach's reusable public-content augmentation and does **not** replace the corresponding static coach profile.

### New Workflow Module

Add:

- `skills/coach-research-engine.md`

This file should define:

- when research augmentation is triggered
- what sources are allowed
- how to merge static profile conclusions with research notes
- what claims are out of bounds
- when to degrade back to static-only mode

### New References

Add:

- `references/research-source-rules.md`
- `references/research-note-schema.md`

These files should define:

- allowed source framing for public-web / Douyin observations
- restrictions on certainty, medical claims, and credential claims
- the markdown schema for each research augmentation note
- freshness and confidence conventions

### New Example

Add:

- `examples/research-augmentation-example.md`

This should show how a static profile answer becomes more specific when an augmentation note is available and explicitly requested.

## Data Model

Each augmentation note should use a stable markdown structure like:

```md
# Pamela Reif Research Augmentation

## Research Status
- source mode: public-web
- freshness: YYYY-MM-DD
- confidence: low / medium / high
- usage: optional augmentation only

## Public Content Signals
- recurring recent topics
- common class structure
- common speaking rhythm or tone
- frequently emphasized training scenarios

## Reinforced Style Notes
- how recent public content sharpens or updates the static impression
- phrased as directional observations, not absolute truths

## Source Caveats
- platform sample bias
- limited time window
- not evidence of medical qualification or complete methodology

## Integration Notes
- when to use this note
- when static profile should still dominate
```

## Composition Rules

Answers should be composed in three layers.

### Layer 1: Static baseline

Always start from:

- `coach_profiles/<coach>.md`
- `references/coach-style-guide.md`
- `references/coach-research-policy.md`

This layer determines:

- the coach's broad fit
- best-for / less-suitable-for framing
- training and nutrition bias
- pairing guidance

### Layer 2: Optional augmentation

Only read `coach_research_notes/<coach>.md` when the user explicitly asks for one of the following:

- newer public content
- Douyin or web-based nuance
- deeper coach-specific detail beyond the static profile
- recent content tendencies that may affect examples or style phrasing

This layer may refine:

- recent public emphasis
- recent content themes
- recent class organization patterns
- recent publicly visible communication style

This layer may **not** override:

- safety boundaries
- scope limitations
- the core suitability model in the static profile

### Layer 3: User mapping

Map the combined result back to the user's actual need:

- coach recommendation
- mixed-coach composition
- training / nutrition / recovery framing
- voice and tone imitation without pretending to be the coach

## Trigger Rules

The research engine should activate only when the user clearly requests it, such as:

- “结合她最近公开内容看看”
- “参考抖音看看她最近偏什么”
- “静态档案不够，帮我做一层 deepsearch 补强”
- “我想知道她最近公开内容里更常练什么”

If the user does not ask for this, the default path remains static-only.

## Fallback Rules

If no augmentation note exists, or fresh public material is unavailable:

- continue answering using static coach profiles
- clearly frame the answer as static-profile-based
- do not block normal coach selection or mixed-coach output
- do not invent recent public observations

## Freshness Rules

Each research note should include explicit freshness metadata.

Suggested interpretation:

- **fresh:** within 30 days
- **aging but usable:** 31–90 days
- **stale:** over 90 days

Older notes can still be used, but confidence should be reduced and the answer should acknowledge possible drift.

## Safety And Boundary Rules

Public-web and Douyin observations are allowed only as:

- public-content signals
- style and emphasis observations
- example-enhancement inputs

They are not allowed to become:

- medical advice
- certification or professional-status claims
- complete evidence of a coach's full system
- justification for spot-reduction claims or other unsupported body-composition claims
- personal-life inference or private-state speculation

The repository must preserve the rule that public research is an **augmentation layer**, not a replacement for the static baseline.

## Repository Impact

The following existing files should be updated to reflect the new layer:

- `SKILL.md`
- `README.md`
- `references/coach-research-policy.md`

These updates should make the augmentation layer visible in repository structure, workflow, and usage guidance.

## Testing Expectations

Implementation should prove:

1. static coach selection still works unchanged when no research is requested
2. research augmentation is only triggered on explicit request
3. missing notes degrade cleanly to static-only output
4. augmentation notes add specificity without overstating certainty
5. augmentation never overrides safety or scope boundaries

## Scope Guardrails

This design does **not** require full scraping automation, scheduled refresh, or platform-specific crawler infrastructure.

The goal is to add a reusable markdown-based augmentation layer and workflow contract, not to build an autonomous data pipeline.
