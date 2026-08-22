---
name: tell-everyone-the-change-affects
description: Sends the notice to every customer the change touches and keeps the proof that each one was told. Use it when running `ref/mkt/pricing-change`.
license: CC-BY-4.0
metadata:
  agent: launch-coordinator
  agent-version: "1"
---

# Tell everyone the change affects

## What it does

Sends the notice to every customer the change touches and keeps the
proof that each one was told.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Serve the Notice**
  - `ref/mkt/pricing-change`, activity 10 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

## What to record

The checklist at a version, a dated record each time a branch lands or
slips, the launch-day sequence as it actually fired, and the first-week
report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
