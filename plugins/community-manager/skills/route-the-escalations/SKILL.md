---
name: route-the-escalations
description: Sends anything it must not handle itself to the owner who has to see it, which covers legal, press and product matters, and records why each item was flagged. Use it when running `ref/mkt/moderate-community`.
license: CC-BY-4.0
metadata:
  agent: community-manager
  agent-version: "1"
---

# Route the escalations

## What it does

Sends anything it must not handle itself to the owner who has to see it,
which covers legal, press and product matters, and records why each item
was flagged.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Route the Escalations**
  - `ref/mkt/moderate-community`, activity 10 -
    [Moderate User Community](../../../../processes/marketing/moderate-community.md)

## What to record

Every reply logged, every escalation with the reason it was flagged, and
a recurring-questions summary at the cadence the process sets.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
