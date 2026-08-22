---
name: check-the-built-list
description: A sample read back against the rule it was built from. Use it when running `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Check the Built List

## What happens

A sample read back against the rule it was built from.

## Where it happens

- `ref/mkt/target-audience-segment`, activity 10 -
  [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
