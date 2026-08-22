---
name: take-in-the-trigger
description: What drifted, or which channel is now sending traffic. Use it when running `ref/mkt/attribution-model`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Take in the Trigger

## What happens

What drifted, or which channel is now sending traffic.

## Where it happens

- `ref/mkt/attribution-model`, activity 1 -
  [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
