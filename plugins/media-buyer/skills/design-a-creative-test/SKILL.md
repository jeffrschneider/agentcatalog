---
name: design-a-creative-test
description: "Designs a test of one change: what is being changed and what it should improve, how many variants there are, how the traffic splits, where they run, and how much exposure has to build up before the result counts. Use it when running `ref/mkt/test-ad-creative`."
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Design a creative test

## What it does

Designs a test of one change: what is being changed and what it should
improve, how many variants there are, how the traffic splits, where they
run, and how much exposure has to build up before the result counts.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Design the Comparison**
  - `ref/mkt/test-ad-creative`, activity 4 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Name the Change to Test**
  - `ref/mkt/test-ad-creative`, activity 3 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Set the Evidence Bar**
  - `ref/mkt/test-ad-creative`, activity 5 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
