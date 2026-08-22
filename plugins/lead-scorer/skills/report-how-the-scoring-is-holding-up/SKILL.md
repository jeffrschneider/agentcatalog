---
name: report-how-the-scoring-is-holding-up
description: "Reports how the live model is doing: the scores it gave set against what those leads went on to do, and the leads no rule could place with how each one was settled. Use it when running `ref/mkt/lead-scoring-model`."
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Report how the scoring is holding up

## What it does

Reports how the live model is doing: the scores it gave set against what
those leads went on to do, and the leads no rule could place with how
each one was settled.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Read the Exception Queue**
  - `ref/mkt/lead-scoring-model`, activity 3 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Watch the First Weeks**
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
