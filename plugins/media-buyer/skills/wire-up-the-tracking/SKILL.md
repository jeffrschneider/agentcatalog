---
name: wire-up-the-tracking
description: "Puts the measurement on before anything runs: the parameters every ad carries, the codes that separate one source or one variant from another, and the conversions that count, each one fired once and tested. Use it when running `ref/mkt/influencer-campaign` and 3 other reference processes."
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Wire up the tracking

## What it does

Puts the measurement on before anything runs: the parameters every ad
carries, the codes that separate one source or one variant from another,
and the conversions that count, each one fired once and tested.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Build the Tracking Parameters**
  - `ref/mkt/traffic-ad-creative`, activity 9 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Set up the Tracking**
  - `ref/mkt/influencer-campaign`, activity 9 -
    [Run Influencer Campaign](../../../../processes/marketing/influencer-campaign.md)
- **Wire up Conversion Tracking**
  - `ref/mkt/paid-search-campaign`, activity 6 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)
- **Wire up the Measurement**
  - `ref/mkt/test-ad-creative`, activity 11 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
