---
name: record-what-is-running
description: "Writes down at a version what is live: which creative runs on which line, and the pools, caps and exclusions in force behind it. Use it when running `ref/mkt/display-retargeting` and `ref/mkt/traffic-ad-creative`."
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Record what is running

## What it does

Writes down at a version what is live: which creative runs on which
line, and the pools, caps and exclusions in force behind it.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Record What Is Live**
  - `ref/mkt/traffic-ad-creative`, activity 17 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Record What Is in Force**
  - `ref/mkt/display-retargeting`, activity 16 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
