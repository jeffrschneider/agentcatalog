---
name: set-the-exits
description: What takes a contact out, and where they go next. Use it when running `ref/mkt/nurture-sequence`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Set the Exits

## What happens

What takes a contact out, and where they go next.

## Where it happens

- `ref/mkt/nurture-sequence`, activity 5 -
  [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
