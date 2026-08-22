---
name: record-what-was-learned
description: Closes the run with what is worth repeating and what to avoid the next time this is run. Use it when running `ref/mkt/pricing-change` and `ref/mkt/product-launch`.
license: CC-BY-4.0
metadata:
  agent: launch-coordinator
  agent-version: "1"
---

# Record what was learned

## What it does

Closes the run with what is worth repeating and what to avoid the next
time this is run.

## Where it happens

The agent does this in one activity across two reference processes. Each
one names the activity as that process words it.

- **Record What Was Learned**
  - `ref/mkt/pricing-change`, activity 16 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
  - `ref/mkt/product-launch`, activity 11 -
    [Launch Product](../../../../processes/marketing/product-launch.md)

## What to record

The checklist at a version, a dated record each time a branch lands or
slips, the launch-day sequence as it actually fired, and the first-week
report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
