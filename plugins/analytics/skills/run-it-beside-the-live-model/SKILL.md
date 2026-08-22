---
name: run-it-beside-the-live-model
description: Both score live leads, only the current one routes. Use it when running `ref/mkt/lead-scoring-model`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Run It Beside the Live Model

## What happens

Both score live leads, only the current one routes.

## Where it happens

- `ref/mkt/lead-scoring-model`, activity 12 -
  [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
