---
name: phase-the-money-across-the-year
description: Says when each function's money becomes available across the year, so a run knows what it can commit to and when. Use it when running `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: reporting-manager
  agent-version: "1"
---

# Phase the money across the year

## What it does

Says when each function's money becomes available across the year, so a
run knows what it can commit to and when.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Phase the Money across the Year**
  - `ref/mkt/set-marketing-budget`, activity 10 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)

## What to record

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
