---
name: take-in-what-was-decided
description: Takes in the decision that starts a run and writes down what it Use it when running `ref/mkt/pricing-change` and `ref/mkt/product-launch`.
license: CC-BY-4.0
metadata:
  agent: launch-coordinator
  agent-version: "1"
---

# Take in what was decided

## What it does

Takes in the decision that starts a run and writes down what it

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Take in the Launch**
  - `ref/mkt/product-launch`, activity 1 -
    [Launch Product](../../../../processes/marketing/product-launch.md)
- **Take in the Pricing Decision**
  - `ref/mkt/pricing-change`, activity 1 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

## What to record

The checklist at a version, a dated record each time a branch lands or
slips, the launch-day sequence as it actually fired, and the first-week
report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
