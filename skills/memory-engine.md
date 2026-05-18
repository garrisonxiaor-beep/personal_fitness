# Memory Engine

## Files Used
Use a health profile file for durable facts and a health progress file for recent status and short-term changes.

## Read Rules
Read existing profile and progress notes before generating a detailed recommendation. Summarize stable habits, preferred formats, current blockers, and known boundaries.

## Write Rules
Store durable user facts, recurring patterns, effective strategies, ineffective strategies, and meaningful safety boundaries. Do not store raw conversation transcripts or one-off small talk.

## Update Actions
- **append:** add a recent observation
- **overwrite:** replace a stable fact that clearly changed
- **summarize:** compress repeated notes into a higher-level pattern
