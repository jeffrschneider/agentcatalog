---
name: take-in-what-starts-a-piece-of-work
description: Takes in whatever starts a piece of work and records what it covers, whether that is creative arriving with the plan lines it has to fill, a report that an ad ran somewhere it should not have, or a signal that a line is off its pace and by how much. Use it when running `ref/mkt/reallocate-media-spend`, `ref/mkt/traffic-ad-creative` and `ref/mkt/verify-ad-placement`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Take in what starts a piece of work

## What it does

Takes in whatever starts a piece of work and records what it covers,
whether that is creative arriving with the plan lines it has to fill, a
report that an ad ran somewhere it should not have, or a signal that a
line is off its pace and by how much.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Take in the Concern**
  - `ref/mkt/verify-ad-placement`, activity 1 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)
- **Take in the Creative and the Plan**
  - `ref/mkt/traffic-ad-creative`, activity 1 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Take in the Pacing Signal**
  - `ref/mkt/reallocate-media-spend`, activity 1 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
