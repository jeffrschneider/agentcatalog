---
name: load-an-audience-list-into-the-platforms
description: Formats an audience list for each system it is going to, delivers it, confirms it arrived, and reports how much of the list each one could actually match and reach. Use it when running `ref/mkt/segment-the-market` and `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Load an audience list into the platforms

## What it does

Formats an audience list for each system it is going to, delivers it,
confirms it arrived, and reports how much of the list each one could
actually match and reach.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Confirm the Match**
  - `ref/mkt/target-audience-segment`, activity 14 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Hand the List to the Platforms**
  - `ref/mkt/target-audience-segment`, activity 13 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Test Whether Each Segment Can Be Reached**
  - `ref/mkt/segment-the-market`, activity 10 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
