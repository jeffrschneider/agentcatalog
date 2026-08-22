---
name: watch-the-first-weeks
description: The new scores set against what the leads did. Use it when running `ref/mkt/lead-scoring-model`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Watch the First Weeks

## What happens

The new scores set against what the leads did.

## Where it happens

- `ref/mkt/lead-scoring-model`, activity 16 -
  [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
