---
name: run-the-duty-cycle
description: Opens a period of duty by carrying in whatever was left open last time, and closes it by naming what is still open and handing that to the next period. Use it when running `ref/mkt/moderate-community`.
license: CC-BY-4.0
metadata:
  agent: community-manager
  agent-version: "1"
---

# Run the duty cycle

## What it does

Opens a period of duty by carrying in whatever was left open last time,
and closes it by naming what is still open and handing that to the next
period.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Close the Cycle**
  - `ref/mkt/moderate-community`, activity 15 -
    [Moderate User Community](../../../../processes/marketing/moderate-community.md)
- **Open the Cycle**
  - `ref/mkt/moderate-community`, activity 1 -
    [Moderate User Community](../../../../processes/marketing/moderate-community.md)

## What to record

Every reply logged, every escalation with the reason it was flagged, and
a recurring-questions summary at the cadence the process sets.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
