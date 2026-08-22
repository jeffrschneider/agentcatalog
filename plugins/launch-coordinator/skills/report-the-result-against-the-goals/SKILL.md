---
name: report-the-result-against-the-goals
description: Reports what the run actually did, measured against the goals that were set when it started. Use it when running `ref/mkt/pricing-change` and `ref/mkt/product-launch`.
license: CC-BY-4.0
metadata:
  agent: launch-coordinator
  agent-version: "1"
---

# Report the result against the goals

## What it does

Reports what the run actually did, measured against the goals that were
set when it started.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Report the Launch**
  - `ref/mkt/product-launch`, activity 10 -
    [Launch Product](../../../../processes/marketing/product-launch.md)
- **Report the Transition**
  - `ref/mkt/pricing-change`, activity 15 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

## What to record

The checklist at a version, a dated record each time a branch lands or
slips, the launch-day sequence as it actually fired, and the first-week
report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
