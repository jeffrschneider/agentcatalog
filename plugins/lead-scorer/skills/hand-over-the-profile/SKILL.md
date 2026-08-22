---
name: hand-over-the-profile
description: Each receiving agent says what it changes. Use it when running `ref/mkt/ideal-customer-profile`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Hand over the Profile

## What happens

Each receiving agent says what it changes.

## Where it happens

- `ref/mkt/ideal-customer-profile`, activity 15 -
  [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
