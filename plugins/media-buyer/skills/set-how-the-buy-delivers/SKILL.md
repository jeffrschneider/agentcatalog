---
name: set-how-the-buy-delivers
description: Sets the dates each line runs, the money it may spend a day, how the versions rotate, and how often one person may see an ad and for how long. Use it when running `ref/mkt/display-retargeting` and `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Set how the buy delivers

## What it does

Sets the dates each line runs, the money it may spend a day, how the
versions rotate, and how often one person may see an ad and for how
long.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Set the Exposure Rules**
  - `ref/mkt/display-retargeting`, activity 11 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Set the Flights, Budgets and Rotation**
  - `ref/mkt/traffic-ad-creative`, activity 13 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
