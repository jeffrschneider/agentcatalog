---
name: watch-what-is-running
description: "Watches a live buy against what it was supposed to do and reports the gap: spend and pace, clicks and conversions, whether a test split still holds, and what came back from the people it reached. Use it when running `ref/mkt/paid-search-campaign`, `ref/mkt/test-ad-creative` and `ref/mkt/win-back-campaign`."
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Watch what is running

## What it does

Watches a live buy against what it was supposed to do and reports the
gap: spend and pace, clicks and conversions, whether a test split still
holds, and what came back from the people it reached.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Watch Delivery**
  - `ref/mkt/test-ad-creative`, activity 14 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Watch Pacing and Results**
  - `ref/mkt/paid-search-campaign`, activity 9 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)
- **Watch the Response**
  - `ref/mkt/win-back-campaign`, activity 17 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
