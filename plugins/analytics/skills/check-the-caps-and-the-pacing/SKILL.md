---
name: check-the-caps-and-the-pacing
description: The agent reads delivered frequency and spend against the caps and the dates that were set, and says where the daily limits have to move for each flight to land on its date. Use it when running `ref/mkt/display-retargeting` and `ref/mkt/reallocate-media-spend`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Check the caps and the pacing

## What it does

The agent reads delivered frequency and spend against the caps and the
dates that were set, and says where the daily limits have to move for
each flight to land on its date.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Caps Are Holding**
  - `ref/mkt/display-retargeting`, activity 14 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Correct the Pacing**
  - `ref/mkt/reallocate-media-spend`, activity 11 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
