---
name: confirm-a-signal-is-real
description: Before anything is rebuilt or moved on the strength of a signal, the agent checks that the figures behind it are current and that the gap still shows up in data the signal was not drawn from. Use it when running `ref/mkt/attribution-model` and `ref/mkt/reallocate-media-spend`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Confirm a signal is real

## What it does

Before anything is rebuilt or moved on the strength of a signal, the
agent checks that the figures behind it are current and that the gap
still shows up in data the signal was not drawn from.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Confirm the Drift**
  - `ref/mkt/attribution-model`, activity 2 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- **Confirm the Numbers Hold**
  - `ref/mkt/reallocate-media-spend`, activity 2 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
