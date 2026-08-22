---
name: split-and-hand-over-the-leads
description: The split rule applied and each side's share delivered. Use it when running `ref/mkt/co-marketing-campaign`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Split and Hand over the Leads

## What happens

The split rule applied and each side's share delivered.

## Where it happens

- `ref/mkt/co-marketing-campaign`, activity 14 -
  [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
