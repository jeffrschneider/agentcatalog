---
name: clear-the-exception
description: A person settles a lead no rule could place. Use it when running `ref/mkt/lead-routing`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Clear the Exception

## What happens

A person settles a lead no rule could place.

## Where it happens

- `ref/mkt/lead-routing`, activity 6 -
  [Route Inbound Lead](../../../../processes/marketing/lead-routing.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
