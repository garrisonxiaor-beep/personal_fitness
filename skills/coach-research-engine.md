# Coach Research Engine

## When To Use
Use when the user explicitly asks for newer public content, deeper coach-specific nuance, or Douyin / web augmentation.

## Trigger Rules
Activate this layer only when the user clearly asks for public-web augmentation, such as:
- 结合最近公开内容
- 参考抖音看看
- deepsearch 补强
- 结合她最近公开内容再判断

Questions that do not clearly ask for public-web augmentation should stay on the static-profile path.

## Baseline-First Flow
1. Read `coach_profiles/<coach>.md` first.
2. Read `references/coach-style-guide.md` and `references/coach-research-policy.md`.
3. If the user explicitly requested augmentation, read `coach_research_notes/<coach>.md` when available.
4. Use research notes only to refine public-content nuance, examples, and recent emphasis.
5. If a research note seems to conflict with the static profile, keep the static profile as authoritative and treat the research note as recency nuance only.
6. Map the combined result back to coach recommendation, mixed-coach composition, or plan framing.

## Allowed Refinements
Research augmentation may refine:
- recent public emphasis
- recent content themes
- recent session organization patterns
- recent communication style

## Fallback Rules
If no research note exists or no fresh public signal is available:
- continue with the static profile
- clearly frame the answer as static-profile-based
- do not invent recent observations
- do not block normal coach selection output

## Boundaries
Research augmentation does not override:
- safety boundaries
- scope limits
- the core suitability model in the static profile

Treat public-web and Douyin results as public-content observations, not medical advice, certification proof, or complete evidence of a coach's system.
