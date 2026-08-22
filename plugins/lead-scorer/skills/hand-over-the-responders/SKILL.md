---
name: hand-over-the-responders
description: A contact who responds gets an owner and a next step. Use it when running `ref/mkt/win-back-campaign`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Hand over the Responders

## What happens

A contact who responds gets an owner and a next step.

## Where it happens

- `ref/mkt/win-back-campaign`, activity 16 -
  [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
