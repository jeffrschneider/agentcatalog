---
name: test-whether-each-segment-can-be-reached
description: Whether the data finds them and the channels reach them. Use it when running `ref/mkt/segment-the-market`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Test Whether Each Segment Can Be Reached

## What happens

Whether the data finds them and the channels reach them.

## Where it happens

- `ref/mkt/segment-the-market`, activity 10 -
  [Segment the Market](../../../../processes/marketing/segment-the-market.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
