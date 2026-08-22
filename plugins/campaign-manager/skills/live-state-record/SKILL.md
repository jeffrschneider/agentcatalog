---
name: live-state-record
description: Writes down at a version what is actually in force right now, such as which creative sits on which line and the pools, caps and exclusions the run is operating under, so a later reading can be set against it. Use it when running `ref/mkt/display-retargeting` and `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: campaign-manager
  agent-version: "1"
---

# Live state record

## What it does

Writes down at a version what is actually in force right now, such as
which creative sits on which line and the pools, caps and exclusions the
run is operating under, so a later reading can be set against it.

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

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
