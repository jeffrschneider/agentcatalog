---
name: decide-who-the-buy-goes-after
description: "Decides what the buy targets: the audience each channel is bought against, the terms to bid on and how they are grouped, and who is kept out or must not overlap. Use it when running `ref/mkt/media-plan`, `ref/mkt/paid-search-campaign` and `ref/mkt/target-audience-segment`."
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Decide who the buy goes after

## What it does

Decides what the buy targets: the audience each channel is bought
against, the terms to bid on and how they are grouped, and who is kept
out or must not overlap.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Build the Keyword Plan**
  - `ref/mkt/paid-search-campaign`, activity 3 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)
- **Name the Exclusions**
  - `ref/mkt/target-audience-segment`, activity 5 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Set the Channel Audience Targets**
  - `ref/mkt/media-plan`, activity 10 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
