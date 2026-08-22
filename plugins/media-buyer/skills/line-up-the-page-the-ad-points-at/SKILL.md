---
name: line-up-the-page-the-ad-points-at
description: Makes sure the page behind an ad answers what that ad was bought for, and gives the campaign the address and the tracking that go with it. Use it when running `ref/mkt/landing-page` and `ref/mkt/paid-search-campaign`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Line up the page the ad points at

## What it does

Makes sure the page behind an ad answers what that ad was bought for,
and gives the campaign the address and the tracking that go with it.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Hand It to the Campaign**
  - `ref/mkt/landing-page`, activity 12 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)
- **Ready the Landing Pages**
  - `ref/mkt/paid-search-campaign`, activity 5 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
