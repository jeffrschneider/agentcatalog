---
name: recompute-the-closed-periods
description: What each channel gains or loses in past periods. Use it when running `ref/mkt/attribution-model`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Recompute the Closed Periods

## What happens

What each channel gains or loses in past periods.

## Where it happens

- `ref/mkt/attribution-model`, activity 9 -
  [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
