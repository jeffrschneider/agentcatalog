---
name: check-the-caps-are-holding
description: Delivered frequency read against the cap that was set. Use it when running `ref/mkt/display-retargeting`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Check the Caps Are Holding

## What happens

Delivered frequency read against the cap that was set.

## Where it happens

- `ref/mkt/display-retargeting`, activity 14 -
  [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
