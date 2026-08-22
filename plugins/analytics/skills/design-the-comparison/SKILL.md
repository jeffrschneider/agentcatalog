---
name: design-the-comparison
description: How many variants, how traffic splits, where they run. Use it when running `ref/mkt/test-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Design the Comparison

## What happens

How many variants, how traffic splits, where they run.

## Where it happens

- `ref/mkt/test-ad-creative`, activity 4 -
  [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
