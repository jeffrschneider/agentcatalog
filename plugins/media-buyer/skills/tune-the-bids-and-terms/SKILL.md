---
name: tune-the-bids-and-terms
description: Bids move and wasted terms become exclusions. Use it when running `ref/mkt/paid-search-campaign`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Tune the Bids and Terms

## What happens

Bids move and wasted terms become exclusions.

## Where it happens

- `ref/mkt/paid-search-campaign`, activity 10 -
  [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
