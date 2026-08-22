---
name: hand-off-the-leads
description: Scored, routed, and passed to who takes them. Use it when running `ref/mkt/webinar`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Hand off the Leads

## What happens

Scored, routed, and passed to who takes them.

## Where it happens

- `ref/mkt/webinar`, activity 16 -
  [Produce Webinar](../../../../processes/marketing/webinar.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
