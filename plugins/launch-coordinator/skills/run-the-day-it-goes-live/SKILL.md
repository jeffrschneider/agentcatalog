---
name: run-the-day-it-goes-live
description: Fires the sequence on the day in the order the plan sets, watches each step land, and holds the run together while the switch is happening. Use it when running `ref/mkt/pricing-change` and `ref/mkt/product-launch`.
license: CC-BY-4.0
metadata:
  agent: launch-coordinator
  agent-version: "1"
---

# Run the day it goes live

## What it does

Fires the sequence on the day in the order the plan sets, watches each
step land, and holds the run together while the switch is happening.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Change the Public Price**
  - `ref/mkt/pricing-change`, activity 12 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Launch Day**
  - `ref/mkt/product-launch`, activity 8 -
    [Launch Product](../../../../processes/marketing/product-launch.md)

## What to record

The checklist at a version, a dated record each time a branch lands or
slips, the launch-day sequence as it actually fired, and the first-week
report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
