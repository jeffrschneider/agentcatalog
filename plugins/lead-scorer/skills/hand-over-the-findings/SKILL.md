---
name: hand-over-the-findings
description: Each receiving agent says what it changes. Use it when running `ref/mkt/analyze-customer-base`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Hand over the Findings

## What happens

Each receiving agent says what it changes.

## Where it happens

- `ref/mkt/analyze-customer-base`, activity 17 -
  [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
