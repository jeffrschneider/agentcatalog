---
name: read-what-is-already-committed
description: "Reads the calendar and reports what the period already owes: the pieces in flight, the dates that are already fixed, and the launches and campaigns that need distribution. Use it when running `ref/mkt/content-calendar` and `ref/mkt/media-plan`."
license: CC-BY-4.0
metadata:
  agent: launch-coordinator
  agent-version: "1"
---

# Read what is already committed

## What it does

Reads the calendar and reports what the period already owes: the pieces
in flight, the dates that are already fixed, and the launches and
campaigns that need distribution.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Collect What the Plan Must Carry**
  - `ref/mkt/media-plan`, activity 2 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **List What Is Already Committed**
  - `ref/mkt/content-calendar`, activity 3 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)

## What to record

The checklist at a version, a dated record each time a branch lands or
slips, the launch-day sequence as it actually fired, and the first-week
report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
