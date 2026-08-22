---
name: restate-the-closed-periods
description: When the method behind a number changes, the agent recomputes the periods that are already closed, says what each channel gains or loses, and reissues every affected report at a new version. Use it when running `ref/mkt/attribution-model`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Restate the closed periods

## What it does

When the method behind a number changes, the agent recomputes the
periods that are already closed, says what each channel gains or loses,
and reissues every affected report at a new version.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Recompute the Closed Periods**
  - `ref/mkt/attribution-model`, activity 9 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- **Reissue the Affected Reports**
  - `ref/mkt/attribution-model`, activity 13 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
